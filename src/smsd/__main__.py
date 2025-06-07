# SiMP/src/simp/__main__.py

from smsd.musiccorelib import MusicCoreLib, PlayerError
from pathlib import Path
import os

def main() -> None:
    player = MusicCoreLib()
    music_dir = Path.home() / "Music"

    print("Welcome to SiMP - The Simple Music Player")
    print(f"Default music directory: {music_dir}")
    print("Type 'help' to see available commands.\n")

    def show_now_playing() -> None:
        try:
            song = player.get_current_song()
            idx = player.get_current_index()
            print(f"Now playing [{idx}]: {song.name}")
        except PlayerError as e:
            print(f"Error: {e}")

    def show_metadata() -> None:
        try:
            mdata = player.get_song_metadata()
            for k, v in mdata.items():
                print(f"{k}: {v}")
        except PlayerError as e:
            print(f"Error: {e}")

    def show_playlist() -> None:
        try:
            playlist = player.get_playlist()
            if not playlist:
                print("No playlist loaded.")
                return
            print(f"Playlist ({len(playlist)} songs):")
            for i, song in enumerate(playlist):
                print(f"  [{i}]: {song.name}")
        except PlayerError as e:
            print(f"Error: {e}")

    def show_current_index() -> None:
        try:
            idx = player.get_current_index()
            print(f"Current song index: [{idx}]")
        except PlayerError as e:
            print(f"Error: {e}")

    def show_volume() -> None:
        try:
            vol = player.get_current_volume()
            print(f"Current volume: {vol}%")
        except PlayerError as e:
            print(f"Error: {e}")

    # Command dispatcher
    def dispatch(cmd: str) -> bool:
        match cmd:
            case "play":
                try:
                    idx = int(input("Enter song index (default 0): ") or "0")
                    player.play(idx)
                except ValueError:
                    print("Invalid index. Must be an integer.")
                except PlayerError as e:
                    print(f"Error: {e}")

            case "pause":
                try:
                    player.toggle_pause()
                except PlayerError as e:
                    print(f"Error: {e}")

            case "clear":
                os.system("cls" if os.name == "nt" else "clear")

            case "exit":
                try:
                    player.stop()
                except PlayerError:
                    pass
                print("Goodbye.")
                return False

            case "load":
                print(f"Enter path to playlist directory (default: {music_dir}):")
                path_input = input(">>> ").strip()
                try:
                    path = Path(path_input).expanduser().resolve() if path_input else music_dir
                    player.playlistctl(path)
                    print(f"Loaded playlist: {path}")
                    show_playlist()
                except PlayerError as e:
                    print(f"Error: {e}")

            case "mode":
                print("Available modes: NORMAL, LOOP, REPEAT")
                mode = input("Enter mode: ").strip().upper()
                try:
                    player.modectl(mode)
                    print(f"Mode set to {mode}")
                except PlayerError as e:
                    print(f"Error: {e}")

            case "next":
                try:
                    player.next()
                    show_now_playing()
                except PlayerError as e:
                    print(f"Error: {e}")

            case "prev":
                try:
                    player.prev()
                    show_now_playing()
                except PlayerError as e:
                    print(f"Error: {e}")

            case "vol":
                try:
                    vol_input = input("Enter volume (0-100) or leave blank to show current: ").strip()
                    if not vol_input:
                        show_volume()
                    else:
                        vol = int(vol_input)
                        player.volctl(vol)
                        print(f"Volume set to {vol}%")
                except ValueError:
                    print("Invalid input. Enter a number between 0 and 100.")
                except PlayerError as e:
                    print(f"Error: {e}")

            case "now":
                show_now_playing()

            case "mdata":
                show_metadata()

            case "playlist":
                show_playlist()

            case "index":
                show_current_index()

            case "help":
                print("""
Available commands:
  load     - Load a playlist directory
  play     - Play track at index
  pause    - Toggle pause
  mode     - Change playback mode (NORMAL, LOOP, REPEAT)
  next     - Play next track
  prev     - Play previous track
  vol      - Set or show volume (0-100)
  playlist - Show current playlist
  index    - Show current song index
  now      - Show current song
  mdata    - Show metadata of current song
  clear    - Clear screen
  exit     - Exit the player
  help     - Show this message
                """)

            case _:
                print("Unknown command. Type 'help' to see available commands.")

        return True

    # REPL loop
    try:
        while True:
            try:
                cmd = input(">>> ").strip().lower()
                if not dispatch(cmd):
                    break
            except Exception as e:
                print(f"Unexpected error: {e}")
    except (KeyboardInterrupt, EOFError):
        print("\nExiting gracefully.")
        try:
            player.stop()
        except Exception:
            pass
