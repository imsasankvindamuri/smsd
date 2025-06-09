# Released under the MIT License. See LICENSE file for further details.

import vlc

# ++++++++++ EXCEPTIONS ++++++++++ #

class PlayerError(Exception):
    """Base exception for player-related errors."""
    def __init__(self, message="An error occurred with the music player"):
        super().__init__(message)

class PlaylistNotLoadedError(PlayerError):
    """Raised when an operation requires a playlist but none is loaded."""
    def __init__(self, message=None, constants=None):
        if message is None:
            if constants:
                supported_types = list(constants.SUPPORTED_MEDIA_FILETYPES)
                message = (
                    f"No playlist is loaded, or loaded playlist is empty. "
                    f"Please load a playlist with supported filetypes: {supported_types}"
                )
            else:
                message = (
                    "No playlist is loaded, or loaded playlist is empty. "
                    "Please load a playlist with supported audio files."
                )
        super().__init__(message)

class InvalidPlaylistError(PlayerError):
    """Raised when the playlist directory is invalid."""
    def __init__(self, message=None, path=None, constants=None):
        if message is None:
            if path:
                message = f"'{path}' is not a valid playlist directory"
            else:
                if constants:
                    supported_types = list(constants.SUPPORTED_MEDIA_FILETYPES)
                    message = (
                        f"Invalid playlist: must be a flat directory containing "
                        f"only supported audio files {supported_types}"
                    )
                else:
                    message = (
                        "Invalid playlist: must be a flat directory containing "
                        "only supported audio files"
                    )
        super().__init__(message)

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
