# Released under the MIT License. See LICENSE file for further details.

from pathlib import Path
import os

# ++++++++++ EXCEPTIONS ++++++++++ #

class PlayerError(Exception):
    """Base exception for player-related errors."""
    def __init__(self, message="An error occurred with the music player"):
        super().__init__(message)

class PlaylistNotLoadedError(PlayerError):
    """Raised when an operation requires a playlist but none is loaded."""
    def __init__(self, message=None, supported_types=None):
        if message is None:
            if supported_types:
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
    def __init__(self, message=None, playlist=None, supported_types=None):
        if message is None:
            if playlist:
                message = f"'{playlist}' is not a valid playlist directory"
            else:
                if supported_types:
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

class SongNotInPlaylistError(PlayerError):
    """Raised when given song is not in playlist"""
    def __init__(self, message=None, song_path=None):
        if song_path is not None:
            message = f"Given song path {song_path} not found in current playlist."
        else:
            message = "Given song path not found in current playlist."
        super().__init__(message)


class FuzzyError(Exception):
    """Base class for fzf-related related exceptions"""
    def __init__(self, message="An error occurred while fuzzy finding.") -> None:
        super().__init__(message)

class UnFuzzifyablePathError(FuzzyError):
    """Raised when provided path is cannot be used for fuzzyfinding"""
    def __init__(self, rootpath, message=None) -> None:
        if message is None:
            if not isinstance(rootpath, Path):
                message = f"Expected `Path` instance, got {rootpath}"
            elif not rootpath.exists():
                message = f"Nonexistent `Path` instance provided: {rootpath.resolve()}"
            elif not rootpath.is_dir():
                message = f"Expected directory path, got filepath {rootpath.resolve()}"
            elif not os.access(rootpath, os.R_OK | os.X_OK):
                message = f"Insufficient file permissions to access directory {rootpath.resolve()}"
            else:
                message = f"Unexpected error accessing path: {rootpath.resolve()}"
        super().__init__(message)


class YTError(Exception):
    """Base class for yt-dlp related exceptions"""
    def __init__(self, message="An error occurred in yt-dlp") -> None:
        super().__init__(message)

class NoYTMetadataFoundError(YTError):
    """Raised when yt-dlp fails to extract metadata for url"""
    def __init__(self, url=None, message=None) -> None:
        if message is None:
            if url is None:
                message = "An unexpected error occurred while extracting metadata from given url"
            else:
                message = f"An unexpected error occurred while extracting metadata from {url}"
        super().__init__(message)
