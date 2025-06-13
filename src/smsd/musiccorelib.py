# Released under the MIT License. See LICENSE file for further details.

import vlc
from pathlib import Path
from mutagen._file import File
from urllib.parse import urlparse, unquote
from contextlib import contextmanager
import threading
from smsd.exceptions import PlayerError, PlaylistNotLoadedError, InvalidPlaylistError, SongNotInPlaylistError

# Written in Helix btw.

class MusicCoreLib:
    def __init__(self) -> None:

        # Private attributes. Triple check any changes you make here.
        # Do NOT manipulate these manually unless you wish to suffer.
        # Please use private methods or the provided context managers
        # instead.
        
        # If you can't find any for your particular need, please
        # consider adding them: I will credit you and thank you generously.
        
        self._player = vlc.Instance()
        self._constants = Constants()
        self._playlist = self._player.media_list_new()
        self._mode = self._constants.NORMAL
        self._lock = threading.RLock()
        self._queue = self._player.media_list_player_new()
        self._queue.set_playback_mode(self._mode)
        

    # The Player should handle:
    # 1) Loading the Playlist (A dir with no subdirs)
    # 2) Playing songs (Play, pause, stop, etc)
    # 3) Changing modes/playlists
    # 4) Exiting gracefully

    # Getter functions. DO NOT COMPOSE THESE WITH THE SETTERS.
    # They are meant to give read-only access to internals.

    def get_playlist(self) -> list[Path]:
        with self._lock:
            self._check_playlist_loaded()
            return [self._mrl_parse(song) for song in self._playlist]
    
    def get_mode(self) -> vlc.PlaybackMode:
        with self._lock:
            return self._mode

    def get_current_song(self) -> Path:
        with self._lock:
            self._check_playlist_loaded()
            media_player = self._queue.get_media_player()
            current_song = media_player.get_media()
            if current_song is None:
                raise PlayerError("No song is currently playing")
            else:
                return self._mrl_parse(current_song)

    def get_current_index(self) -> int:
        with self._lock:
            self._check_playlist_loaded()
            media_player = self._queue.get_media_player()
            current_song = media_player.get_media()
            if current_song is None:
                raise PlayerError("No song is currently playing")
            index = self._playlist.index_of_item(current_song)
            if index == -1:
                raise PlayerError("Current song is not part of the playlist")
            return index
                

    def get_current_volume(self) -> int:
        with self._lock:
            audio = self._queue.get_media_player().audio_get_volume()
            return int(audio)

    def get_song_metadata(self) -> dict[str, str]:
        with self._lock:
            song_path = self.get_current_song()
            if not song_path:
                return {
                    "Error" : "No song currently playing."
                }

            # Replace leading `file://` if it exists

            song_path = Path(song_path).as_posix()
        
            if song_path.startswith("file://"):
                song_path = song_path.replace("file://","",1)

            audio = File(song_path,easy=True)

            if audio is None:
                return {
                    "Error" : "Corrupted or unsupported filetype."
                }

            default = ["Unknown"]

            try:

                info = {
                    "Title" : audio.get("title", [Path(song_path).stem])[0],
                    "Artist" : audio.get("artist", default)[0],
                    "Album" : audio.get("album", default)[0],
                    "File" : Path(song_path).name
                }

                return info

            except Exception:

                return {
                    "Title" : Path(song_path).stem,
                    "Artist" : "Unknown",
                    "Album" : "Unknown",
                    "File" : Path(song_path).name
                }

    # Setter functions

    def playlistctl(self, playlist_path : Path) -> None:
        """
        Set given path to playlist if it is a valid playlist.
        """
        with self._lock:
            self._is_valid_playlist(playlist_path)

            playlist : vlc.MediaList = self._player.media_list_new()
            songlist = [
                path.as_posix() for path in playlist_path.iterdir()
                if path.suffix.lower() in self._constants.SUPPORTED_MEDIA_FILETYPES
            ]

        
            for song in songlist:
                playlist.add_media(song)
        
            if self._queue.is_playing():
                self._queue.stop()

            self._playlist = playlist
            self._queue.set_media_list(self._playlist)


    def modectl(self, mode : str = "NORMAL") -> None:
        """
        Set mode based on string input.
        """
        with self._lock:
            self._check_playlist_loaded()
            match mode.upper():
                case "NORMAL":
                    self._mode = self._constants.NORMAL
                case "LOOP":
                    self._mode = self._constants.LOOP
                case "REPEAT":
                    self._mode = self._constants.REPEAT
                case _:
                    raise PlayerError(f"Invalid playback mode: '{mode}'. Valid modes: NORMAL, LOOP, REPEAT")

            self._queue.set_playback_mode(self._mode)

    def volctl(self, vol: int) -> None:
        """
        Control volume (0-100).
        """
        with self._lock:
            self._check_playlist_loaded()
            if not 0 <= vol <= 100:
                raise PlayerError(f"Volume must be between 0-100, got: {vol}")
            media_player = self._queue.get_media_player()
            if media_player:
                media_player.audio_set_volume(vol)
            else:
                raise PlayerError("No MediaPlayer instance found")

    # Playback features. No comments here: they are self-documenting.
    # Nonetheless, docstrings.

    # Also, thread safety--- just in case.

    def play(self, song_path : Path) -> None:
        """
        Plays song based on path
        """
        with self._lock:
            self._check_playlist_loaded()
            index = self._get_index_by_path(song_path)
            self._play_at_index(index)


    def toggle_pause(self) -> None:
        """
        Toggles pause.
        """
        with self._lock:
            self._check_playlist_loaded()
            self._queue.pause()
        
    def next(self) -> None:
        """
        Play next song. Applying `next` at the last song will wrap around.
        """
        with self._lock:
            self._check_playlist_loaded()
            with self._do_in_mode(self._constants.LOOP):
                self._queue.next()

    def prev(self) -> None:
        """
        Play previous song. Applying `prev` at first song will wrap around
        """
        with self._lock:
            self._check_playlist_loaded()
            with self._do_in_mode(self._constants.LOOP):
                self._queue.previous()

    def stop(self) -> None:
        """
        Unconditionally stop the queue. Call this as the when you
        are done using the class.
        """
        with self._lock:
            self._queue.stop()

    # Private helper functions

    def _check_playlist_loaded(self) -> None:
        """
        Raises PlaylistNotLoadedError if current playlist has no supported files,
        causing self._playlist.count() to return 0.
        """
        if self._playlist.count() == 0:
            raise PlaylistNotLoadedError(constants=self._constants)

    def _is_valid_playlist(self, playlist : Path) -> None:
        """
        Raises InvalidPlaylistError if playlist is not a flat directory.
        Use when updating existing playlist.
        """
        if not playlist.exists() or not playlist.is_dir():
            raise InvalidPlaylistError(playlist=playlist)

        if any(path.is_dir() for path in playlist.iterdir()):
            raise InvalidPlaylistError(constants=self._constants)

    @contextmanager
    def _do_in_mode(self, mode : vlc.PlaybackMode):
        """
        The context manager for this class. It is there to avoid
        annoying state variables.
        """
        old_mode = self._mode
        self._queue.set_playback_mode(mode)
        try:
            yield
        finally:
            self._queue.set_playback_mode(old_mode)

    def _mrl_parse(self, song : vlc.Media) -> Path:
        """
        By default, vlc.Media.get_mrl() gives paths with URL
        encoding (%20 for <SPC>, etc.,). This decodes that.
        """
        mrl = song.get_mrl()
        parsed = urlparse(mrl)
        if parsed.scheme != "file":
            raise PlayerError(f"Unable to parse file URL: {mrl}")
        path_str = unquote(parsed.path)
        return Path(path_str)

    def _get_index_by_path(self, song_path : Path) -> int:
        """
        Take a song path and return its index in the playlist
        """
        with self._lock:
            song_path = song_path.expanduser().resolve()
            try:
                return self.get_playlist().index(song_path)
            except ValueError:
                raise SongNotInPlaylistError(song_path=song_path)

    def _play_at_index(self, index : int = 0) -> None:
        """
        Plays the song in index. Uses 0 indexing.
        """
        with self._lock:
            if 0 <= index < self._playlist.count():
                self._queue.play_item_at_index(index)
            else:
                raise PlayerError(f"Index {index} out of range for playlist (0-{self._playlist.count()-1})")

class Constants:
    def __init__(self) -> None:
        # Define constants; No magic numbers here, sir!
        self.NORMAL = vlc.PlaybackMode(0)
        self.LOOP = vlc.PlaybackMode(1)
        self.REPEAT = vlc.PlaybackMode(2)
        self.SUPPORTED_MEDIA_FILETYPES = frozenset({
            ".mp3",
            ".wav",
        })

        # Might add other filetypes later. Gotta ship MVP first. 
