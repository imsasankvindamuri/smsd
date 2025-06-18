from enum import Enum
import threading
from typing import Self
import vlc
from pathlib import Path
import asyncio
from contextlib import contextmanager
from smsd.utils.exceptions import PlayerError, PlaylistNotLoadedError, InvalidPlaylistError, SongNotInPlaylistError
import random
from urllib.parse import urlparse, unquote

class Mode(Enum):
    """Playback modes for the music player."""
    Normal = "Normal"      # Play through playlist once
    Loop = "Loop"          # Loop entire playlist
    Repeat = "Repeat"      # Repeat current song
    Shuffle = "Shuffle"    # Random playback order

class MusicCoreLib:
    """
    Async wrapper around the synchronous music player.
    
    Provides async interface for music playback with support for playlist management,
    different playback modes, and volume control. Uses asyncio.to_thread to wrap
    synchronous VLC operations.
    
    Usage:
        async with MusicCoreLib() as player:
            await player.playlistctl(Path("./music"))
            await player.play()
    """
    
    def __init__(self) -> None:
        """Initialize async wrapper with underlying sync player."""
        self._sync_player = _SyncMusicPlayer()
    
    # Getters
    
    async def get_playlist(self) -> list[str]:
        """Get current playlist as list of file paths."""
        return await asyncio.to_thread(self._sync_player.get_playlist)
    
    async def get_mode(self) -> Mode:
        """Get current playback mode."""
        return await asyncio.to_thread(self._sync_player.get_mode)
    
    async def get_current_song(self) -> Path:
        """Get path to currently loaded song."""
        return await asyncio.to_thread(self._sync_player.get_current_song)
    
    async def get_current_index(self) -> int:
        """Get index of current song in playlist."""
        return await asyncio.to_thread(self._sync_player.get_current_index)
    
    async def get_current_volume(self) -> int:
        """Get current volume level (0-100)."""
        return await asyncio.to_thread(self._sync_player.get_current_volume)
    
    # Setters
    
    async def playlistctl(self, playlist_path: Path) -> Self:
        """
        Load playlist from directory containing audio files.
        
        Args:
            playlist_path: Directory containing supported audio files
            
        Returns:
            Self for method chaining
        """
        await asyncio.to_thread(self._sync_player.playlistctl, playlist_path)
        return self
    
    async def modectl(self, mode: Mode) -> Self:
        """
        Set playback mode.
        
        Args:
            mode: Playback mode (Normal, Loop, Repeat, Shuffle)
            
        Returns:
            Self for method chaining
        """
        await asyncio.to_thread(self._sync_player.modectl, mode)
        return self
    
    async def volctl(self, vol: int) -> Self:
        """
        Set volume level.
        
        Args:
            vol: Volume level (0-100)
            
        Returns:
            Self for method chaining
        """
        await asyncio.to_thread(self._sync_player.volctl, vol)
        return self
    
    # Playback Functions
    
    async def load_song(self, song_path: Path) -> None:
        """Load and start playing specific song from current playlist."""
        await asyncio.to_thread(self._sync_player.load_song, song_path)
    
    async def toggle_pause(self) -> None:
        """Toggle pause state of current playback."""
        await asyncio.to_thread(self._sync_player.toggle_pause)
    
    async def next(self) -> None:
        """Skip to next song based on current mode."""
        await asyncio.to_thread(self._sync_player.next)
    
    async def prev(self) -> None:
        """Go to previous song based on current mode."""
        await asyncio.to_thread(self._sync_player.prev)
    
    async def exit(self) -> None:
        """Clean up resources and stop playback."""
        await asyncio.to_thread(self._sync_player.exit)
    
    # Convenience methods for common operations
    
    async def play(self) -> None:
        """Start playing the current song if playlist is loaded."""
        if await self.get_playlist():
            current_song = await self.get_current_song()
            await self.load_song(current_song)
    
    async def stop(self) -> None:
        """Stop playback immediately."""
        await asyncio.to_thread(self._sync_player.stop)
    
    async def is_playing(self) -> bool:
        """Check if audio is currently playing."""
        return await asyncio.to_thread(self._sync_player._player.is_playing)
    
    # Context manager support for clean resource management
    
    async def __aenter__(self):
        """Async context manager entry."""
        return self
    
    async def __aexit__(self, exc_type, exc_val, exc_tb):
        """Async context manager exit with cleanup."""
        await self.exit()


class _SyncMusicPlayer:
    """
    Synchronous music player implementation using VLC backend.
    
    Handles playlist management, playback modes, and uses a daemon thread
    for event-driven playback control. Not intended for direct use - 
    use MusicCoreLib async wrapper instead.
    """
    
    def __init__(self) -> None:
        """Initialize VLC player with daemon thread for playback control."""
        # VLC setup
        self._instance = vlc.Instance()
        self._player = self._instance.media_player_new()
        self._event_mgmt = self._player.event_manager()
        
        # Playlist state
        self._playlist: list[str] = []
        self._index = 0
        self._previous_shuffle_index = None
        self._mode = Mode.Normal
        
        # Configuration
        self._supported_media_filetypes = frozenset({
            ".mp3", ".wav", ".flac", ".ogg"
        })
        
        # Threading
        self._lock = threading.RLock()
        self._event_registry = []
        self._daemon_call = threading.Event()
        self._kill_daemon = False

        # Start daemon thread for playback control
        self._daemon = threading.Thread(target=self._daemon_loop, daemon=True)
        self._daemon.start()
        self._handle_modes()

    def get_playlist(self) -> list[str]:
        """Get current playlist as resolved file paths."""
        with self._lock:
            return [
                self._mrl_parse(song).expanduser().resolve().as_posix()
                for song in self._playlist
            ]

    def get_mode(self) -> Mode:
        """Get current playback mode."""
        with self._lock:
            return self._mode

    def get_current_song(self) -> Path:
        """Get path to currently selected song."""
        with self._lock:
            self._check_playlist_loaded()
            return self._mrl_parse(self._playlist[self._index])

    def get_current_index(self) -> int:
        """Get index of current song in playlist."""
        with self._lock:
            self._check_playlist_loaded()
            return self._index

    def get_current_volume(self) -> int:
        """Get current volume level from VLC player."""
        with self._lock:
            vol = self._player.audio_get_volume()
            if not 0 <= vol <= 100:
                raise PlaylistNotLoadedError(supported_types=self._supported_media_filetypes)
            return vol

    def playlistctl(self, playlist_path: Path) -> None:
        """
        Load playlist from directory containing audio files.
        
        Stops current playback and loads all supported audio files
        from the specified directory in sorted order.
        
        Args:
            playlist_path: Directory containing audio files
        """
        with self._lock:
            self._is_valid_playlist(playlist_path)
            if self._player.is_playing():
                self._player.stop()
            self._playlist = sorted (
                path.expanduser().resolve().as_uri() for path in playlist_path.iterdir()
                if path.suffix.lower() in self._supported_media_filetypes
            )
            self._index = 0

    def modectl(self, mode) -> None:
        """Set playback mode (Normal, Loop, Repeat, Shuffle)."""
        with self._lock:
            self._mode = mode

    def volctl(self, vol: int) -> None:
        """
        Set volume level.
        
        Args:
            vol: Volume level between 0-100
        """
        with self._lock:
            if not 0 <= vol <= 100:
                raise PlayerError(f"Volume must be between 0-100; got: {vol}")
            self._player.audio_set_volume(vol)

    def load_song(self, song_path: Path) -> None:
        """
        Load and play specific song from current playlist.
        
        Args:
            song_path: Path to song file that must exist in current playlist
        """
        with self._lock:
            self._check_playlist_loaded()
            idx = self._get_index_by_path(song_path)
            self._call_index_daemon(idx)

    def toggle_pause(self) -> None:
        """Toggle pause state of current playback."""
        with self._lock:
            self._check_playlist_loaded()
            self._player.pause()

    def next(self) -> None:
        """Skip to next song, temporarily using Loop mode for wrapping."""
        with self._lock:
            self._check_playlist_loaded()
            with self._mode_change(Mode.Loop):
                playlist_len = len(self._playlist)
                self._call_index_daemon((self._index + 1) % playlist_len)
                

    def prev(self) -> None:
        """Go to previous song, temporarily using Loop mode for wrapping."""
        with self._lock:
            self._check_playlist_loaded()
            with self._mode_change(Mode.Loop):
                playlist_len = len(self._playlist)
                self._call_index_daemon((self._index - 1) % playlist_len)

    def stop(self) -> None:
        """Stop the music player"""
        with self._lock:
            self._player.stop()

    def exit(self) -> None:
        """Clean up all resources including daemon thread and VLC player."""
        with self._lock:
            # Signal the daemon to stop
            self._kill_daemon = True
            self._daemon_call.set()  # Wake up the daemon if it's waiting

            # Wait for the daemon to terminate
            if self._daemon.is_alive():
                self._daemon.join(timeout=1.0)

            # Clean up VLC resources
            self._player.stop()
            if self._event_registry:
                for event in self._event_registry:
                    self._event_mgmt.event_detach(event)
                self._event_registry = []
            
    def _check_playlist_loaded(self) -> None:
        """Ensure playlist is loaded before operations that require it."""
        if len(self._playlist) == 0:
            raise PlaylistNotLoadedError(supported_types=self._supported_media_filetypes)

    def _is_valid_playlist(self, playlist : Path) -> None:
        """Validate that path is a directory containing only files."""
        if not playlist.exists() or not playlist.is_dir() or any(path.is_dir() for path in playlist.iterdir()):
            raise InvalidPlaylistError(playlist=playlist, supported_types=self._supported_media_filetypes)

    @contextmanager
    def _mode_change(self, mode : Mode):
        """
        Temporarily change playback mode within context.
        
        Used for operations like next/prev that need different behavior
        than the current mode (e.g., wrapping in Normal mode).
        """
        old_mode = self.get_mode()
        self.modectl(mode)
        try:
            yield
        finally:
            self.modectl(old_mode)

    def _get_index_by_path(self, path : Path) -> int:
        """Find playlist index for given song path."""
        song_path = path.expanduser().resolve()
        try:
            playlist = self._playlist
            return playlist.index(song_path.as_uri())
        except ValueError:
            raise SongNotInPlaylistError(song_path=song_path.as_posix())

    def _call_index_daemon(self, index : int = 0) -> None:
        """
        Signal daemon thread to play song at given index.
        
        ALWAYS USE THIS TO SET THE FUCKING INDEX... unless you like suffering ig
        
        Args:
            index: Playlist index to play
        """
        if not 0 <= index < len(self._playlist):
            raise PlaylistNotLoadedError(supported_types=self._supported_media_filetypes)
        self._index = index
        self._daemon_call.set()
        

    def _daemon_loop(self) -> None:
        """
        Main daemon thread loop for handling playback events.
        
        Waits for signals to play specific indices and handles
        the actual VLC media loading and playback start.
        """
        while not self._kill_daemon:
            self._daemon_call.wait()
            if self._kill_daemon:
                break
            self._play_current_index()
            self._daemon_call.clear()

    def _handle_modes(self) -> None:
        """Set up VLC event handlers for automatic mode-based playback."""
        self._event_mgmt.event_attach(vlc.EventType.MediaPlayerEndReached, self._on_song_end)
        self._event_registry.append(vlc.EventType.MediaPlayerEndReached)

    def _mrl_parse(self, mrl : str) -> Path:
        """Parse VLC media resource locator (file:// URI) to Path object."""
        parsed = urlparse(mrl)
        if parsed.scheme != "file":
            raise PlayerError(f"Unable to parse file URL: {mrl}")
        path_str = unquote(parsed.path)
        return Path(path_str)

    def _play_current_index(self) -> None:
        """Load and start playing song at current index."""
        length = len(self._playlist)
        if 0 <= self._index < length:
            self._player.set_media(self._instance.media_new(self._playlist[self._index]))
            self._player.play()
        else:
            raise PlayerError(f"Index {self._index} out of range for playlist (0-{length-1})")

    def _on_song_end(self, event) -> None:
        """
        VLC event handler for when current song finishes.
        
        Implements mode-specific behavior:
        - Normal: Play next song, stop at end
        - Loop: Play next song, wrap to beginning  
        - Repeat: Replay current song
        - Shuffle: Play random song (avoiding immediate repeats)
        """
        with self._lock:
            playlist_len = len(self._playlist)
            if not playlist_len:
                return
            match self._mode:
                case Mode.Normal:
                    if 0 <= self._index < playlist_len - 1:
                        self._call_index_daemon(self._index + 1)
                    else:
                        pass

                case Mode.Loop:
                    self._call_index_daemon((self._index + 1) % playlist_len)

                case Mode.Repeat:
                    self._call_index_daemon(self._index)

                case Mode.Shuffle:
                    if playlist_len > 1:
                        new_index = random.choice([
                            i for i in range(playlist_len)
                            if i != self._previous_shuffle_index
                        ])
                        self._previous_shuffle_index = self._index
                    else:
                        new_index = 0
                    self._call_index_daemon(new_index)
