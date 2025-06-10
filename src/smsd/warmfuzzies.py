# Released under the MIT License. See LICENSE file for further details.

import os
from pyfzf.pyfzf import FzfPrompt
from pathlib import Path
from smsd.exceptions import UnFuzzifyablePathError

# This class is a thin wrapper around the FzfPrompt()
# class. It has a couple responsiblities:
# - Allow for song selection
# - Allow for playlist selection
# - Allow for multiple song selection when downloading

Mode = str

class WarmFuzzies:
    def __init__(self, rootpath) -> None:

        self._multichoice = (
            '--multi '
            '--header="<TAB>=Toggle Select, <RET>=Confirm, <ESC>=Cancel" '
            '--cycle'
        )
        self._singlechoice = (
            '--header="<RET>=Confirm, <ESC>=Cancel" '
            '--cycle'
        )
        self._fzf = FzfPrompt()
        self._rootpath = Path()
        self = self.set_rootpath(rootpath)

    def select_one_song(self, playlist : list[Path]) -> Path:
        return Path(self._fzf.prompt(playlist, self._singlechoice)[0])

    def select_playlist(self) -> Path:
        self._check_valid_path(self._rootpath)
        playlist_set = [playlist for playlist in self._rootpath.iterdir() if playlist.is_dir()]
        return Path(self._fzf.prompt(playlist_set, self._singlechoice)[0])

    def select_mode(self, modes : list[Mode]) -> Mode:
        return Mode(self._fzf.prompt(modes, self._singlechoice)[0])

    # Helper funcs

    def set_rootpath(self, path : str | Path) -> None:
        self._check_valid_path(path)
        self._rootpath = Path(path)


    def _check_valid_path(self, path : str | Path) -> None:
        path = Path(path).expanduser().resolve()
        condt = path.exists() and path.is_dir() and os.access(path, os.R_OK | os.X_OK)
        if not condt:
            raise UnFuzzifyablePathError(path)
