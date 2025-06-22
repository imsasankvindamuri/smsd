# Released under the MIT License. See LICENSE file for further details.

import shutil
from yt_dlp import YoutubeDL
from pathlib import Path
from smsd.utils.exceptions import NoYTMetadataFoundError, InvalidPlaylistError
from difflib import SequenceMatcher
import unicodedata
import asyncio

class Downloader:
    """Async wrapper for the internal _Downloader class."""
    
    def __init__(self) -> None:
        """Initialize the async downloader wrapper."""
        self._downloader = _Downloader()
    
    async def get_url_entries(self, url: str) -> dict[str, str]:
        """Extract video entries from a playlist or single video URL.
        
        Args:
            url: YouTube URL (video or playlist)
            
        Returns:
            Dict mapping video titles to their URLs
        """
        return await asyncio.to_thread(self._downloader.get_url_entries, url)
    
    async def download_to_path(self, playlist: Path, songlist: list[str]) -> dict:
        """Legacy download method - avoid using due to throttling issues.
        
        Args:
            playlist: Directory path to download songs to
            songlist: List of YouTube URLs to download
            
        Returns:
            Status report dict with success/failure information
        """
        return await asyncio.to_thread(self._downloader.download_to_path, playlist, songlist)
    
    async def download(self, url: str, chosen_urls: dict[str, str], playlist: Path) -> dict:
        """Download selected songs from a playlist to local directory.
        
        Args:
            url: Original playlist URL
            chosen_urls: Dict mapping song titles to their URLs
            playlist: Local directory to save downloaded songs
            
        Returns:
            Status report dict with download results
        """
        return await asyncio.to_thread(self._downloader.download, url, chosen_urls, playlist)

class _Downloader:
    """Internal synchronous downloader implementation."""
    
    def __init__(self) -> None:
        """Initialize the YoutubeDL downloader."""
        self._ydl = YoutubeDL

    def get_url_entries(self, url: str) -> dict[str, str]:
        """Extract video entries from a YouTube URL without downloading.
        
        Args:
            url: YouTube URL (video or playlist)
            
        Returns:
            Dict mapping video titles to their URLs
            
        Raises:
            NoYTMetadataFoundError: If URL metadata cannot be extracted
        """
        ydl_opts = {
            'quiet': True,
            'no_warnings': True,
            'extract_flat': True
        }

        with self._ydl(ydl_opts) as ydl:
            try:
                info = ydl.extract_info(url, download=False)
                if info is None:
                    raise NoYTMetadataFoundError(url)
                if 'entries' not in info:
                    return {info.get('title', url): url}

                result = {}
                for entry in info['entries']:
                    if entry and entry.get('title'):
                        video_url = entry.get('webpage_url') or f"https://youtube.com/watch?v={entry['id']}"
                        result[entry['title']] = video_url
                return result
            except Exception:
                raise NoYTMetadataFoundError(url)

    def download_to_path(self, playlist: Path, songlist: list[str]) -> dict:
        """Legacy download method that suffers from throttling issues.
        
        DEPRECATED: Use download() method instead.
        
        Args:
            playlist: Directory path to download songs to
            songlist: List of YouTube URLs to download
            
        Returns:
            Status report with success/failure lists
            
        Raises:
            InvalidPlaylistError: If playlist directory is invalid
            ValueError: If songlist format is incorrect
        """
        status_report = {
            "playlist_path": playlist.expanduser().resolve(),
            "song_list": songlist,
            "success": [],
            "failure": []
        }

        if not playlist.exists() or not playlist.is_dir() or any(path.is_dir() for path in playlist.iterdir()):
            raise InvalidPlaylistError(playlist=playlist)
        if not isinstance(songlist, list) or any(not isinstance(song, str) for song in songlist):
            raise ValueError(f"Invalid input for songlist={songlist}; input must be list of URLs.")
        
        ydl_opts = {
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
            'outtmpl': f'{playlist}/%(title)s.%(ext)s',
            'noplaylist': True,
        }

        with self._ydl(ydl_opts) as ydl:
            for song in songlist:
                try:
                    ydl.download([song])
                    status_report["success"].append(song)
                except Exception as e:
                    status_report['failure'].append({
                        "song": song,
                        "cause_of_failure": f"{e}"
                    })

        return status_report

    def download(self, url: str, chosen_urls: dict[str, str], playlist: Path) -> dict:
        """Download selected songs from a playlist with improved matching.
        
        Downloads the entire playlist to a temp directory, then moves only
        the selected songs to the target playlist directory.
        
        Args:
            url: Original YouTube playlist URL
            chosen_urls: Dict mapping song titles to their URLs
            playlist: Local directory to save selected songs
            
        Returns:
            Status report dict with download results
            
        Raises:
            InvalidPlaylistError: If playlist directory is invalid
            ValueError: If chosen_urls format is incorrect
        """
        song_name_list = list(chosen_urls.keys())

        status_report = {
            "playlist_path": playlist.expanduser().resolve(),
            "song_list": chosen_urls,
            "success": [],
            "failure": [],
        }

        if not playlist.exists() or not playlist.is_dir() or any(path.is_dir() for path in playlist.iterdir()):
            raise InvalidPlaylistError(playlist=playlist)
        if not isinstance(song_name_list, list) or any(not isinstance(song, str) for song in song_name_list):
            raise ValueError(f"Invalid input for songlist={chosen_urls}; Required mapping: dict mapping title to URLs.")
    
        tmp = playlist / "tmp"
        tmp.mkdir(exist_ok=True)

        try:
            ydl_opts = {
                'format': 'bestaudio/best',
                'postprocessors': [
                    {
                        'key': 'FFmpegExtractAudio',
                        'preferredcodec': 'mp3',
                        'preferredquality': '192',
                    },
                    {
                        'key': 'EmbedThumbnail',
                        'already_have_thumbnail': False,
                    },
                    {
                        'key': 'FFmpegMetadata',
                        'add_metadata': True,
                    }
                ],
                'outtmpl': f'{tmp}/%(title)s.%(ext)s',
                'writethumbnail': True,
                'writeinfojson': True,
            }
            with self._ydl(ydl_opts) as ydl:
                ydl.download([url])

            downloaded_files = list(tmp.glob("*.mp3"))
            for file in downloaded_files:
                if any(self._titles_match(file.stem, title) for title in song_name_list):
                    try:
                        target = playlist / file.name
                        shutil.move(str(file), str(target))
                        status_report['success'].append({
                            'song': f'{file.stem}',
                            'path': target,
                        })
                    except Exception as e:
                        status_report['failure'].append({
                            'song': f'{file.stem}',
                            'error': f'{e}'
                        })

            downloaded_song_names = [item['song'] for item in status_report['success']]
            for requested_song in song_name_list:
                if not any(self._titles_match(downloaded_name, requested_song) for downloaded_name in downloaded_song_names):
                    status_report['failure'].append({
                        'song': requested_song,
                        'error': 'Song not found in downloaded playlist'
                    })

            return status_report
        finally:
            if tmp.exists():
                shutil.rmtree(tmp)
        
    def _titles_match(self, filename: str, selected_title: str, threshold: float = 0.6) -> bool:
        """Check if a filename matches a selected title using fuzzy matching.
        
        First tries exact substring matching, then falls back to fuzzy
        string similarity matching.
        
        Args:
            filename: Downloaded file's stem name
            selected_title: User-selected song title
            threshold: Minimum similarity ratio for fuzzy matching
            
        Returns:
            True if titles are considered a match
        """
        def normalize_string(s: str) -> str:
            """Normalize Unicode string for comparison."""
            return unicodedata.normalize('NFKD', s).lower().strip()
    
        norm_filename = normalize_string(filename)
        norm_title = normalize_string(selected_title)
    
        # Check if one contains the other (original logic)
        if norm_title in norm_filename or norm_filename in norm_title:
            return True
    
        # Fuzzy matching as fallback
        similarity = SequenceMatcher(None, norm_filename, norm_title).ratio()
        return similarity >= threshold
