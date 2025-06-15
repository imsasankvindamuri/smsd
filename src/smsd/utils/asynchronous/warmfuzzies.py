# Released under the MIT License. See LICENSE file for further details.

import os
from pyfzf.pyfzf import FzfPrompt
from pathlib import Path
from smsd.utils.exceptions import UnFuzzifyablePathError, PlaylistNotLoadedError
import asyncio

# This class is a thin wrapper around the FzfPrompt()
# class. It has a couple responsiblities:
# - Allow for song selection
# - Allow for playlist selection
# - Allow for multiple song selection when downloading
#
# It is a helper function to act as a pseudo-TUI

Mode = str

class WarmFuzzies:
    def __init__(self, rootpath) -> None:
        self._warmfuzzies = _WarmFuzzies(rootpath)

    async def select_one_song(self, playlist : list[str]) -> str:
        return await asyncio.to_thread(self._warmfuzzies.select_one_song, playlist)

    async def select_playlist(self) -> Path:
        return await asyncio.to_thread(self._warmfuzzies.select_playlist)

    async def select_mode(self, modes : list[Mode]) -> Mode:
        return await asyncio.to_thread(self._warmfuzzies.select_mode, modes)

    async def select_download_songs(self, songname_to_url : dict[str,str]) -> dict:
        return await asyncio.to_thread(self._warmfuzzies.select_download_songs, songname_to_url)

    async def set_rootpath(self, path : str | Path) -> None:
        return await asyncio.to_thread(self._warmfuzzies.set_rootpath, path)

class _WarmFuzzies:
    def __init__(self, rootpath) -> None:

        self._multichoice = (
            '--multi '
            '--header="<TAB>=Toggle Select, <RET>=Confirm, <ESC>=Cancel" '
            '--cycle '
        )
        self._singlechoice = (
            '--header="<RET>=Confirm, <ESC>=Cancel" '
            '--cycle '
        )
        self._fzf = FzfPrompt()
        self._rootpath = Path()
        self.set_rootpath(rootpath)

    def select_one_song(self, playlist : list[str]) -> str:
        name_to_path = {Path(song).stem : song for song in playlist}
        if len(name_to_path) == 0:
            raise PlaylistNotLoadedError
        select_song = self._fzf.prompt(name_to_path.keys(), self._singlechoice)[0]
        return name_to_path[select_song]

    def select_playlist(self) -> Path:
        self._check_valid_path(self._rootpath)
        playlist_set = [playlist for playlist in self._rootpath.iterdir() if playlist.is_dir()]
        name_to_path = {playlist.stem : playlist for playlist in playlist_set}
        select_playlist = self._fzf.prompt(name_to_path.keys(), self._singlechoice)[0]
        return name_to_path[select_playlist]

    def select_mode(self, modes : list[Mode]) -> Mode:
        return Mode(self._fzf.prompt(modes, self._singlechoice)[0])

    def select_download_songs(self, songname_to_url : dict[str,str]) -> dict:
        if len(songname_to_url) == 1:
            return songname_to_url
        select_songs = self._fzf.prompt(songname_to_url.keys(), self._multichoice)
        return {
            song : songname_to_url[song] for song in select_songs
        }

    # Helper funcs

    def set_rootpath(self, path : str | Path) -> None:
        self._check_valid_path(path)
        self._rootpath = Path(path)


    def _check_valid_path(self, path : str | Path) -> None:
        path = Path(path).expanduser().resolve()
        condt = path.exists() and path.is_dir() and os.access(path, os.R_OK | os.X_OK)
        if not condt:
            raise UnFuzzifyablePathError(path)
