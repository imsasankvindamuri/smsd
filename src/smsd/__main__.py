# Released under the MIT License. See LICENSE file for further details.

import asyncio
from pathlib import Path
from datetime import datetime
import os

from smsd.utils.asynchronous.musiccorelib import MusicCoreLib, Mode  # Updated import
from smsd.utils.synchronous.warmfuzzies import WarmFuzzies
from smsd.utils.synchronous.ydl_wrapper import Downloader
from smsd.utils.exceptions import PlayerError, UnFuzzifyablePathError


async def event_loop() -> None:
    # Use the async wrapper instead of the old async version
    async with MusicCoreLib() as player:  # Using context manager for clean resource management
        music_dir = Path.home() / "Music"
        warmfuzzies = WarmFuzzies(music_dir)
        downloader = Downloader()

        print("Welcome to smsd - The Simple Music Pseudo Daemon (Async Wrapper)")
        print(f"Default music directory: {music_dir}")
        print("Type 'help' to see available commands.\n")

        async def show_now_playing() -> None:
            try:
                song = await player.get_current_song()
                idx = await player.get_current_index()
                print(f"Now playing [{idx}]: {song.name}")
            except PlayerError as e:
                print(f"Error: {e}")

        async def show_playlist() -> None:
            try:
                playlist = await player.get_playlist()
                if not playlist:
                    print("No playlist loaded.")
                    return
                print(f"Playlist ({len(playlist)} songs):")
                for i, song in enumerate(playlist):
                    print(f"  [{i}]: {Path(song).name}")
            except PlayerError as e:
                print(f"Error: {e}")

        async def show_volume() -> None:
            try:
                vol = await player.get_current_volume()
                print(f"Current volume: {vol}%")
            except PlayerError as e:
                print(f"Error: {e}")

        async def load_playlist() -> None:
            try:
                selected_playlist = warmfuzzies.select_playlist()
                await player.playlistctl(selected_playlist)
                print(f"Loaded playlist: {selected_playlist}")
                await play_song()
            except (PlayerError, UnFuzzifyablePathError, IndexError) as e:
                print(f"Error: {e}")

        async def play_song() -> None:
            try:
                playlist = await player.get_playlist()
                selected_song = warmfuzzies.select_one_song(playlist)
                await player.load_song(Path(selected_song))
                await show_now_playing()
            except (PlayerError, UnFuzzifyablePathError, IndexError) as e:
                print(f"Error: {e}")

        async def download_songs() -> None:
            try:
                print("Enter the YouTube URL (playlist or video): ")
                url = input("> ").strip()
                if not url:
                    print("No URL entered. Cancelled.")
                    return

                song_entries = downloader.get_url_entries(url)
                if not song_entries:
                    print("No downloadable entries found.")
                    return

                if len(list(song_entries.keys())) > 1:
                    full_playlist = input(f"Would you like to download the full playlist? [Y/n]: ").lower() or "y"
                    if full_playlist == "y":
                        chosen_urls = song_entries
                    elif full_playlist == "n":
                        chosen_urls = warmfuzzies.select_download_songs(song_entries)
                    else:
                        print(f"Error parsing input: {full_playlist}")
                        return
                else:
                    chosen_urls = song_entries

                existing_playlist = input(f"Would you like to download the songs to an existing playlist? [Y/n]: ").lower() or "y"
                if existing_playlist == "y":
                    selected_playlist = warmfuzzies.select_playlist()
                elif existing_playlist == "n":
                    playlist_name = input("Please enter the name for your playlist or press <RET> for a default playlist name: ") or f"Playlist_{datetime.now().strftime('%Y-%m-%d_%H.%M.%S')}"
                    selected_playlist = music_dir / playlist_name
                    if selected_playlist.exists():
                        print(f"{selected_playlist} already exists... Aborting.")
                        return
                    selected_playlist.mkdir()
                else:
                    print(f"Error parsing input: {existing_playlist}")
                    return

                status = downloader.download(url, chosen_urls, selected_playlist)
                print_download_status(status)

            except Exception as e:
                print(f"Error during download: {e}")

        def print_download_status(status: dict) -> None:
            """Print a nicely formatted download status report"""
            total_requested = len(status['song_list'])
            successful_count = len(status['success'])
            failed_count = len(status['failure'])

            print("\n" + "=" * 60)
            print(" DOWNLOAD REPORT")
            print("=" * 60)
            print(f"󰲸 Playlist: {status['playlist_path'].name}")
            print(f" Summary: {successful_count}/{total_requested} successful")

            if successful_count > 0:
                print(f"\n Successfully Downloaded ({successful_count}):")
                for item in status['success']:
                    song_name = item['song']
                    display_name = song_name[:50] + "..." if len(song_name) > 50 else song_name
                    print(f"    {display_name}")

            if failed_count > 0:
                print(f"\n✗ Failed Downloads ({failed_count}):")
                for item in status['failure']:
                    song_name = item['song']
                    error = item['error']
                    display_name = song_name[:45] + "..." if len(song_name) > 45 else song_name
                    print(f"   ✗ {display_name}")
                    print(f"     └─ Error: {error}")

            if successful_count == total_requested:
                print(f"\n󱁖 All downloads completed successfully!")
            elif successful_count == 0:
                print(f"\n All downloads failed. Check your internet connection or try again later.")
            else:
                success_rate = (successful_count / total_requested) * 100
                print(f"\n Success rate: {success_rate:.1f}%")

            print("=" * 60 + "\n")

        async def dispatch(cmd: str) -> bool:
            match cmd:
                case "play":
                    await play_song()
                case "start":  # Added start command to begin playback of current playlist
                    try:
                        await player.play()
                        await show_now_playing()
                    except (PlayerError, IndexError) as e:
                        print(f"Error: {e}")
                case "pause":
                    try:
                        await player.toggle_pause()
                    except PlayerError as e:
                        print(f"Error: {e}")
                case "next":
                    try:
                        await player.next()
                        await show_now_playing()
                    except PlayerError as e:
                        print(f"Error: {e}")
                case "prev":
                    try:
                        await player.prev()
                        await show_now_playing()
                    except PlayerError as e:
                        print(f"Error: {e}")
                case "stop":
                    try:
                        await player.stop()
                        print("Playback stopped.")
                    except PlayerError as e:
                        print(f"Error: {e}")
                case "vol":
                    try:
                        vol_input = input("Enter volume (0-100) or leave blank to show current: ").strip()
                        if not vol_input:
                            await show_volume()
                        else:
                            vol = int(vol_input)
                            await player.volctl(vol)
                            print(f"Volume set to {vol}%")
                    except ValueError:
                        print("Invalid input. Enter a number between 0 and 100.")
                    except PlayerError as e:
                        print(f"Error: {e}")
                case "load":
                    await load_playlist()
                case "mode":
                    try:
                        mode = warmfuzzies.select_mode(["NORMAL", "LOOP", "REPEAT", "SHUFFLE"])
                        await player.modectl(Mode[mode.capitalize()])
                        print(f"Mode set to {mode}")
                    except (PlayerError, KeyError, IndexError) as e:
                        print(f"Error: {e}")
                case "list":
                    await show_playlist()
                case "now":
                    await show_now_playing()
                case "status":  # Added status command to show current state
                    try:
                        is_playing = await player.is_playing()
                        mode = await player.get_mode()
                        vol = await player.get_current_volume()
                        print(f"Status: {'Playing' if is_playing else 'Stopped'}")
                        print(f"Mode: {mode.value}")
                        print(f"Volume: {vol}%")
                        if is_playing:
                            await show_now_playing()
                    except PlayerError as e:
                        print(f"Error: {e}")
                case "clear":
                    os.system("cls" if os.name == "nt" else "clear")
                case "help":
                    show_help()
                case "dload":
                    await download_songs()
                case "exit":
                    print("Goodbye.")
                    return False  # Context manager will handle cleanup
                case _:
                    print("Unknown command. Type 'help' to see available commands.")
            return True

        def show_help() -> None:
            print("\nAvailable commands:")
            print("  play    - Select and play a song from the current playlist")
            print("  start   - Start playing the current playlist from current position")
            print("  pause   - Toggle pause/play")
            print("  next    - Play next song")
            print("  prev    - Play previous song")
            print("  stop    - Stop playback")
            print("  vol     - Set or show volume (0-100)")
            print("  load    - Load a playlist")
            print("  mode    - Set playback mode (NORMAL, LOOP, REPEAT, SHUFFLE)")
            print("  list    - Show current playlist")
            print("  now     - Show now playing")
            print("  status  - Show player status (playing/stopped, mode, volume)")
            print("  clear   - Clear the screen")
            print("  dload   - Download songs from a YouTube URL to a playlist")
            print("  help    - Show this help message")
            print("  exit    - Exit the player\n")

        # Main event loop
        show_help()
        while True:
            try:
                cmd = input("> ").strip().lower()
                if not await dispatch(cmd):
                    break
            except (KeyboardInterrupt, EOFError):
                print("\nExiting.")
                break  # Context manager will handle cleanup


def main() -> None:
    asyncio.run(event_loop())
