# Released under the MIT License. See LICENSE file for further details.

import shutil
from yt_dlp import YoutubeDL
from pathlib import Path
from smsd.utils.exceptions import NoYTMetadataFoundError, InvalidPlaylistError
from difflib import SequenceMatcher
import unicodedata
import asyncio
import re

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
            Status report with success/failure lists (MODIFIED FORMAT)
            
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
            for song_url in songlist:
                try:
                    # Get the title first to track what we downloaded
                    info = ydl.extract_info(song_url, download=False)
                    song_title = info.get('title', 'Unknown Title') if info else 'Unknown Title'
                    
                    ydl.download([song_url])
                    
                    # Find the downloaded file
                    mp3_files = list(playlist.glob("*.mp3"))
                    downloaded_file = None
                    for mp3_file in mp3_files:
                        if self._titles_match(mp3_file.stem, song_title):
                            downloaded_file = mp3_file
                            break
                    
                    status_report["success"].append({
                        "song": song_title,
                        "url": song_url,
                        "path": downloaded_file
                    })
                except Exception as e:
                    status_report['failure'].append({
                        "song": song_url,
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
        choose_legacy_method = len(chosen_urls) < 10
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

        if choose_legacy_method:
            print('Using legacy method as number of requested songs are less than 10...')
            # Convert chosen_urls to list of URLs and call legacy method
            return self.download_to_path(playlist, list(chosen_urls.values()))

        tmp = playlist / "tmp"
        tmp.mkdir(exist_ok=True)

        try:
            # Download individual songs instead of entire playlist to avoid extra downloads
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
                'noplaylist': True,  # Important: don't download entire playlist
            }
            
            with self._ydl(ydl_opts) as ydl:
                # Download only the chosen songs
                for song_title, song_url in chosen_urls.items():
                    try:
                        print(f"Downloading: {song_title}")
                        ydl.download([song_url])
                        
                        # Find the downloaded file
                        downloaded_files = list(tmp.glob("*.mp3"))
                        matched_file = None
                        
                        for file in downloaded_files:
                            if self._titles_match(file.stem, song_title):
                                matched_file = file
                                break
                        
                        if matched_file:
                            target = playlist / matched_file.name
                            shutil.move(str(matched_file), str(target))
                            status_report['success'].append({
                                'song': song_title,
                                'path': target,
                            })
                            print(f"Successfully downloaded: {song_title}")
                        else:
                            status_report['failure'].append({
                                'song': song_title,
                                'error': 'Downloaded file not found or not matched'
                            })
                    except Exception as e:
                        status_report['failure'].append({
                            'song': song_title,
                            'error': f'{e}'
                        })

            return status_report
        finally:
            if tmp.exists():
                shutil.rmtree(tmp)
        
    def _titles_match(self, filename: str, selected_title: str, threshold: float = 0.8) -> bool:
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
        
        # Debug output
        print(f"Matching: '{norm_filename}' vs '{norm_title}'")
    
        # Check if one contains the other (original logic)
        if norm_title in norm_filename or norm_filename in norm_title:
            print(f"Exact match found")
            return True
    
        # Fuzzy matching as fallback with higher threshold
        similarity = SequenceMatcher(None, norm_filename, norm_title).ratio()
        print(f"Similarity: {similarity}")
        is_match = similarity >= threshold
        if is_match:
            print(f"Fuzzy match found")
        return is_match
