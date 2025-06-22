# Released under the MIT License. See LICENSE file for further details.

import asyncio
from pathlib import Path
from datetime import datetime

from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.text import Text
from rich.prompt import Prompt, Confirm
from rich import box
from rich.rule import Rule

from smsd.utils.asynchronous.musiccorelib import MusicCoreLib, Mode
from smsd.utils.asynchronous.warmfuzzies import WarmFuzzies
from smsd.utils.asynchronous.ydl_wrapper import Downloader
from smsd.utils.exceptions import PlayerError, UnFuzzifyablePathError

# Initialize Rich console
console = Console()


async def event_loop() -> None:
    async with MusicCoreLib() as player:
        music_dir = Path.home() / "Music"
        warmfuzzies = WarmFuzzies(music_dir)
        downloader = Downloader()

        # Welcome message with style
        console.print(Panel.fit(
            "[bold cyan]🎵 smsd - The Simple Music Pseudo Daemon[/bold cyan]\n"
            "[dim](Async Wrapper)[/dim]",
            border_style="cyan"
        ))
        
        console.print(f"[dim]📁 Default music directory:[/dim] [yellow]{music_dir}[/yellow]")
        console.print("[dim]💡 Type '[bold]help[/bold]' to see available commands.[/dim]\n")

        async def show_now_playing() -> None:
            try:
                song = await player.get_current_song()
                idx = await player.get_current_index()
                
                panel = Panel(
                    f"[bold green]♪ {song.stem}[/bold green]\n[dim]Track {idx + 1}[/dim]",
                    title="[bold]🎵 Now Playing[/bold]",
                    border_style="green"
                )
                console.print(panel)
            except PlayerError as e:
                console.print(f"[bold red]❌ Error:[/bold red] {e}")

        async def show_playlist() -> None:
            try:
                playlist = await player.get_playlist()
                if not playlist:
                    console.print("[yellow]📋 No playlist loaded.[/yellow]")
                    return
                
                table = Table(title=f"🎵 Playlist ({len(playlist)} songs)", box=box.ROUNDED)
                table.add_column("Track", justify="right", style="cyan", no_wrap=True)
                table.add_column("Song", style="magenta")
                
                for i, song in enumerate(playlist):
                    table.add_row(str(i + 1), Path(song).stem)
                
                console.print(table)
            except PlayerError as e:
                console.print(f"[bold red]❌ Error:[/bold red] {e}")

        async def show_volume() -> None:
            try:
                vol = await player.get_current_volume()
                
                # Create a visual volume bar
                bar_length = 20
                filled = int((vol / 100) * bar_length)
                bar = "█" * filled + "░" * (bar_length - filled)
                
                console.print(f"[bold]🔊 Volume:[/bold] {vol}% [{bar}]")
            except PlayerError as e:
                console.print(f"[bold red]❌ Error:[/bold red] {e}")

        async def load_playlist() -> None:
            try:
                with console.status("[bold green]Loading playlist...", spinner="dots"):
                    selected_playlist = await warmfuzzies.select_playlist()
                    await player.playlistctl(selected_playlist)
                
                console.print(f"[bold green]✅ Loaded playlist:[/bold green] [cyan]{selected_playlist}[/cyan]")
                await play_song()
            except (PlayerError, UnFuzzifyablePathError, IndexError) as e:
                console.print(f"[bold red]❌ Error:[/bold red] {e}")

        async def play_song() -> None:
            try:
                playlist = await player.get_playlist()
                selected_song = await warmfuzzies.select_one_song(playlist)
                
                with console.status("[bold green]Loading song...", spinner="dots"):
                    await player.load_song(Path(selected_song))
                
                await show_now_playing()
            except (PlayerError, UnFuzzifyablePathError, IndexError) as e:
                console.print(f"[bold red]❌ Error:[/bold red] {e}")

        async def download_songs() -> None:
            try:
                console.print(Rule("[bold cyan]🔽 Download Songs[/bold cyan]"))
                
                url = Prompt.ask("[bold]Enter the YouTube URL (playlist or video)[/bold]", console=console)
                if not url:
                    console.print("[yellow]⚠️ No URL entered. Cancelled.[/yellow]")
                    return

                with console.status("[bold green]Fetching URL entries...", spinner="dots"):
                    song_entries = await downloader.get_url_entries(url)
                
                if not song_entries:
                    console.print("[red]❌ No downloadable entries found.[/red]")
                    return

                if len(list(song_entries.keys())) > 1:
                    full_playlist = Confirm.ask(
                        f"[bold]Would you like to download the full playlist?[/bold]",
                        default=True,
                        console=console
                    )
                    if full_playlist:
                        chosen_urls = song_entries
                    else:
                        chosen_urls = await warmfuzzies.select_download_songs(song_entries)
                else:
                    chosen_urls = song_entries

                existing_playlist = Confirm.ask(
                    "[bold]Would you like to download the songs to an existing playlist?[/bold]",
                    default=True,
                    console=console
                )
                
                if existing_playlist:
                    selected_playlist = await warmfuzzies.select_playlist()
                else:
                    playlist_name = Prompt.ask(
                        "[bold]Please enter the name for your playlist[/bold]",
                        default=f"Playlist_{datetime.now().strftime('%Y-%m-%d_%H.%M.%S')}",
                        console=console
                    )
                    selected_playlist = music_dir / playlist_name
                    if selected_playlist.exists():
                        console.print(f"[red]❌ {selected_playlist} already exists... Aborting.[/red]")
                        return
                    selected_playlist.mkdir()

                with console.status("[bold green]Downloading...", spinner="dots"):
                    status = await downloader.download(url, chosen_urls, selected_playlist)
                
                print_download_status(status)

            except Exception as e:
                console.print(f"[bold red]❌ Error during download:[/bold red] {e}")

        def print_download_status(status: dict) -> None:
            """Print a beautifully formatted download status report using Rich"""
            total_requested = len(status['song_list'])
            successful_count = len(status['success'])
            failed_count = len(status['failure'])

            # Create main panel content
            content = Text()
            content.append(f"📁 Playlist: ", style="bold")
            content.append(f"{status['playlist_path'].name}\n", style="cyan")
            content.append(f"📊 Summary: ", style="bold")
            content.append(f"{successful_count}/{total_requested} successful", style="green")

            # Success table
            if successful_count > 0:
                success_table = Table(title="✅ Successfully Downloaded", box=box.MINIMAL, show_header=False)
                success_table.add_column("Song", style="green")
                
                for item in status['success']:
                    song_name = item['song']
                    display_name = song_name[:50] + "..." if len(song_name) > 50 else song_name
                    success_table.add_row(f"✓ {display_name}")

            # Failure table
            if failed_count > 0:
                failure_table = Table(title="❌ Failed Downloads", box=box.MINIMAL, show_header=False)
                failure_table.add_column("Song", style="red")
                failure_table.add_column("Error", style="dim red")
                
                for item in status['failure']:
                    song_name = item['song']
                    error = item['error']
                    display_name = song_name[:45] + "..." if len(song_name) > 45 else song_name
                    failure_table.add_row(f"✗ {display_name}", error)

            # Status message
            if successful_count == total_requested:
                status_msg = "[bold green]🎉 All downloads completed successfully![/bold green]"
            elif successful_count == 0:
                status_msg = "[bold red]💥 All downloads failed. Check your internet connection or try again later.[/bold red]"
            else:
                success_rate = (successful_count / total_requested) * 100
                status_msg = f"[bold yellow]📈 Success rate: {success_rate:.1f}%[/bold yellow]"

            # Display everything
            console.print(Panel(content, title="[bold]📊 Download Report[/bold]", border_style="cyan"))
            
            if successful_count > 0:
                console.print(success_table)
            if failed_count > 0:
                console.print(failure_table)
            
            console.print(Panel.fit(status_msg, border_style="green" if successful_count == total_requested else "yellow"))

        async def dispatch(cmd: str) -> bool:
            match cmd:
                case "play":
                    await play_song()
                case "start":
                    try:
                        await player.play()
                        console.print("[bold green]▶️ Playback started[/bold green]")
                        await show_now_playing()
                    except (PlayerError, IndexError) as e:
                        console.print(f"[bold red]❌ Error:[/bold red] {e}")
                case "pause":
                    try:
                        await player.toggle_pause()
                        console.print("[bold yellow]⏸️ Playback toggled[/bold yellow]")
                    except PlayerError as e:
                        console.print(f"[bold red]❌ Error:[/bold red] {e}")
                case "next":
                    try:
                        await player.next()
                        console.print("[bold cyan]⏭️ Next track[/bold cyan]")
                        await show_now_playing()
                    except PlayerError as e:
                        console.print(f"[bold red]❌ Error:[/bold red] {e}")
                case "prev":
                    try:
                        await player.prev()
                        console.print("[bold cyan]⏮️ Previous track[/bold cyan]")
                        await show_now_playing()
                    except PlayerError as e:
                        console.print(f"[bold red]❌ Error:[/bold red] {e}")
                case "stop":
                    try:
                        await player.stop()
                        console.print("[bold red]⏹️ Playback stopped[/bold red]")
                    except PlayerError as e:
                        console.print(f"[bold red]❌ Error:[/bold red] {e}")
                case "vol":
                    try:
                        vol_input = Prompt.ask(
                            "[bold]Enter volume (0-100) or leave blank to show current[/bold]",
                            default="",
                            console=console
                        )
                        if not vol_input:
                            await show_volume()
                        else:
                            vol = int(vol_input)
                            await player.volctl(vol)
                            console.print(f"[bold green]🔊 Volume set to {vol}%[/bold green]")
                    except ValueError:
                        console.print("[bold red]❌ Invalid input. Enter a number between 0 and 100.[/bold red]")
                    except PlayerError as e:
                        console.print(f"[bold red]❌ Error:[/bold red] {e}")
                case "load":
                    await load_playlist()
                case "mode":
                    try:
                        mode = await warmfuzzies.select_mode(["NORMAL", "LOOP", "REPEAT", "SHUFFLE"])
                        await player.modectl(Mode[mode.capitalize()])
                        console.print(f"[bold green]🔄 Mode set to {mode}[/bold green]")
                    except (PlayerError, KeyError, IndexError) as e:
                        console.print(f"[bold red]❌ Error:[/bold red] {e}")
                case "list":
                    await show_playlist()
                case "now":
                    await show_now_playing()
                case "status":
                    try:
                        is_playing = await player.is_playing()
                        mode = await player.get_mode()
                        vol = await player.get_current_volume()
                        
                        status_table = Table(box=box.ROUNDED, title="🎵 Player Status")
                        status_table.add_column("Property", style="cyan")
                        status_table.add_column("Value", style="green")
                        
                        status_table.add_row("Status", "🔊 Playing" if is_playing else "⏸️ Stopped")
                        status_table.add_row("Mode", f"🔄 {mode.value}")
                        status_table.add_row("Volume", f"🔊 {vol}%")
                        
                        console.print(status_table)
                        
                        if is_playing:
                            await show_now_playing()
                    except PlayerError as e:
                        console.print(f"[bold red]❌ Error:[/bold red] {e}")
                case "clear":
                    console.clear()
                case "help":
                    show_help()
                case "dload":
                    await download_songs()
                case "exit":
                    console.print("[bold cyan]👋 Goodbye![/bold cyan]")
                    return False
                case _:
                    console.print("[bold red]❓ Unknown command.[/bold red] Type '[bold]help[/bold]' to see available commands.")
            return True

        def show_help() -> None:
            """Display a beautifully formatted help menu"""
            help_table = Table(title="🎵 Available Commands", box=box.ROUNDED)
            help_table.add_column("Command", style="cyan", no_wrap=True)
            help_table.add_column("Description", style="white")
            
            commands = [
                ("play", "🎵 Select and play a song from the current playlist"),
                ("start", "▶️ Start playing the current playlist from current position"),
                ("pause", "⏸️ Toggle pause/play"),
                ("next", "⏭️ Play next song"),
                ("prev", "⏮️ Play previous song"),
                ("stop", "⏹️ Stop playback"),
                ("vol", "🔊 Set or show volume (0-100)"),
                ("load", "📁 Load a playlist"),
                ("mode", "🔄 Set playback mode (NORMAL, LOOP, REPEAT, SHUFFLE)"),
                ("list", "📋 Show current playlist"),
                ("now", "🎵 Show now playing"),
                ("status", "📊 Show player status (playing/stopped, mode, volume)"),
                ("clear", "🧹 Clear the screen"),
                ("dload", "🔽 Download songs from a YouTube URL to a playlist"),
                ("help", "❓ Show this help message"),
                ("exit", "👋 Exit the player")
            ]
            
            for cmd, desc in commands:
                help_table.add_row(cmd, desc)
            
            console.print(help_table)

        # Main event loop
        show_help()
        while True:
            try:
                cmd = Prompt.ask("[bold cyan]🎵[/bold cyan]", console=console).strip().lower()
                if not await dispatch(cmd):
                    break
            except (KeyboardInterrupt, EOFError):
                console.print("\n[bold cyan]👋 Exiting...[/bold cyan]")
                break


def main() -> None:
    asyncio.run(event_loop())


if __name__ == "__main__":
    main()
