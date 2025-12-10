"""
Command-line interface for the Literature Review Agent.

Usage:
    lit-review new <topic>           Start a new research project
    lit-review load <project_dir>    Load an existing project
    lit-review gather                Gather references from sources
    lit-review organize              Organize and prioritize references
    lit-review read [--count=N]      Read and analyze papers
    lit-review report                Generate the literature review report
    lit-review interactive           Run in interactive mode
    lit-review status                Show project status
"""

import asyncio
import sys
from pathlib import Path
from typing import Optional

from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt, Confirm
from rich.progress import Progress, SpinnerColumn, TextColumn
from rich.table import Table

from .agent import LiteratureReviewAgent
from .models import AgentMessage, SourceConfig
from .utils.config import load_config, save_config, Config


console = Console()


def create_rich_callback(console: Console):
    """Create a message callback using Rich formatting.

    Args:
        console: Rich console instance

    Returns:
        Callback function
    """
    def callback(message: AgentMessage) -> None:
        style_map = {
            "update": "blue",
            "question": "yellow",
            "insight": "green",
            "request_feedback": "magenta",
            "summary": "cyan",
        }
        style = style_map.get(message.message_type, "white")

        if message.message_type == "summary":
            console.print(Panel(message.content, title="Summary", style=style))
        elif message.message_type == "insight":
            console.print(f"[bold {style}]💡 {message.content}[/]")
        elif message.message_type == "question":
            console.print(f"[bold {style}]❓ {message.content}[/]")
        else:
            console.print(f"[{style}]{message.content}[/]")

    return callback


def create_rich_input(console: Console):
    """Create an input callback using Rich prompts.

    Args:
        console: Rich console instance

    Returns:
        Callback function
    """
    def callback(prompt: str, options: list[str] | None = None) -> str:
        if options:
            console.print(f"\n[bold]{prompt}[/]")
            for i, opt in enumerate(options, 1):
                console.print(f"  [cyan]{i}[/]. {opt}")
            response = Prompt.ask("Enter choice")
            try:
                idx = int(response) - 1
                if 0 <= idx < len(options):
                    return options[idx]
            except ValueError:
                pass
            return response
        else:
            return Prompt.ask(f"\n[bold]{prompt}[/]")

    return callback


async def cmd_new(topic: str, config: Config) -> None:
    """Start a new research project.

    Args:
        topic: Research topic name
        config: Configuration
    """
    console.print(f"[bold green]Starting new project: {topic}[/]")

    agent = LiteratureReviewAgent(
        config=config,
        message_callback=create_rich_callback(console),
        input_callback=create_rich_input(console),
    )

    description = Prompt.ask("Describe your research focus in detail")

    questions = []
    console.print("\nEnter key research questions (empty line to finish):")
    while True:
        q = Prompt.ask("Question", default="")
        if not q:
            break
        questions.append(q)

    key_terms = Prompt.ask(
        "Key search terms (comma-separated)",
        default=topic
    ).split(",")

    await agent.start_new_project(
        topic_name=topic,
        topic_description=description,
        key_questions=questions,
        key_terms=[t.strip() for t in key_terms],
    )

    # Ask about sources
    while Confirm.ask("Would you like to add a source?"):
        source_type = Prompt.ask(
            "Source type",
            choices=["url_list", "blog", "notes_folder"],
        )
        name = Prompt.ask("Source name")

        if source_type == "url_list":
            path = Prompt.ask("Path to URL list file")
            await agent.add_source(SourceConfig(
                name=name,
                source_type="url_list",
                path=path,
            ))
        elif source_type == "blog":
            url = Prompt.ask("Blog URL or RSS feed")
            await agent.add_source(SourceConfig(
                name=name,
                source_type="blog",
                url=url,
            ))
        elif source_type == "notes_folder":
            path = Prompt.ask("Path to notes folder")
            await agent.add_source(SourceConfig(
                name=name,
                source_type="notes_folder",
                path=path,
            ))

    await agent.close()
    console.print("[bold green]Project created successfully![/]")


async def cmd_gather(config: Config) -> None:
    """Gather references from all sources.

    Args:
        config: Configuration
    """
    agent = LiteratureReviewAgent(
        config=config,
        message_callback=create_rich_callback(console),
        input_callback=create_rich_input(console),
    )

    project = await agent.load_existing_project(config.data_dir / "project")
    if not project:
        console.print("[red]No project found. Start a new project first.[/]")
        return

    with Progress(
        SpinnerColumn(),
        TextColumn("[progress.description]{task.description}"),
        console=console,
    ) as progress:
        task = progress.add_task("Gathering references...", total=None)
        new_refs = await agent.gather_references()
        progress.update(task, completed=True)

    console.print(f"[green]Added {new_refs} new references[/]")
    await agent.close()


async def cmd_organize(config: Config) -> None:
    """Organize and prioritize references.

    Args:
        config: Configuration
    """
    agent = LiteratureReviewAgent(
        config=config,
        message_callback=create_rich_callback(console),
        input_callback=create_rich_input(console),
    )

    project = await agent.load_existing_project(config.data_dir / "project")
    if not project:
        console.print("[red]No project found.[/]")
        return

    await agent.organize_references()
    await agent.close()


async def cmd_read(count: int, config: Config) -> None:
    """Read and analyze papers.

    Args:
        count: Number of papers to read
        config: Configuration
    """
    agent = LiteratureReviewAgent(
        config=config,
        message_callback=create_rich_callback(console),
        input_callback=create_rich_input(console),
    )

    project = await agent.load_existing_project(config.data_dir / "project")
    if not project:
        console.print("[red]No project found.[/]")
        return

    processed = await agent.read_papers(max_papers=count)
    console.print(f"[green]Processed {processed} papers[/]")
    await agent.close()


async def cmd_report(config: Config) -> None:
    """Generate the literature review report.

    Args:
        config: Configuration
    """
    agent = LiteratureReviewAgent(
        config=config,
        message_callback=create_rich_callback(console),
        input_callback=create_rich_input(console),
    )

    project = await agent.load_existing_project(config.data_dir / "project")
    if not project:
        console.print("[red]No project found.[/]")
        return

    report = await agent.generate_report()
    console.print(f"[green]Report generated![/]")
    await agent.close()


async def cmd_interactive(config: Config) -> None:
    """Run in interactive mode.

    Args:
        config: Configuration
    """
    agent = LiteratureReviewAgent(
        config=config,
        message_callback=create_rich_callback(console),
        input_callback=create_rich_input(console),
    )

    await agent.run_interactive()
    await agent.close()


async def cmd_status(config: Config) -> None:
    """Show project status.

    Args:
        config: Configuration
    """
    agent = LiteratureReviewAgent(
        config=config,
        message_callback=create_rich_callback(console),
        input_callback=create_rich_input(console),
    )

    project = await agent.load_existing_project(config.data_dir / "project")
    if not project:
        console.print("[red]No project found.[/]")
        return

    # Display status table
    table = Table(title=f"Project: {project.name}")
    table.add_column("Metric", style="cyan")
    table.add_column("Value", style="green")

    ref_stats = agent.ref_manager.get_statistics()
    note_stats = agent.note_manager.get_statistics()

    table.add_row("Phase", project.phase)
    table.add_row("Total References", str(ref_stats["total"]))
    table.add_row("Completed", str(ref_stats["by_status"].get("completed", 0)))
    table.add_row("In Queue", str(ref_stats["by_status"].get("queued", 0)))
    table.add_row("Total Notes", str(note_stats["total"]))
    table.add_row("Subtopics", str(agent.subtopic_manager.get_statistics()["total"]))

    console.print(table)
    await agent.close()


def main():
    """Main CLI entry point."""
    import argparse

    parser = argparse.ArgumentParser(
        description="Literature Review Agent - AI-powered research assistant",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
    lit-review new "AI Agents"
    lit-review gather
    lit-review read --count 5
    lit-review report
    lit-review interactive
        """,
    )

    parser.add_argument(
        "--config",
        "-c",
        type=Path,
        help="Path to config file",
    )
    parser.add_argument(
        "--data-dir",
        "-d",
        type=Path,
        help="Data directory for project files",
    )

    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    # new command
    new_parser = subparsers.add_parser("new", help="Start a new research project")
    new_parser.add_argument("topic", help="Research topic name")

    # load command
    load_parser = subparsers.add_parser("load", help="Load existing project")
    load_parser.add_argument("project_dir", type=Path, help="Project directory")

    # gather command
    subparsers.add_parser("gather", help="Gather references from sources")

    # organize command
    subparsers.add_parser("organize", help="Organize and prioritize references")

    # read command
    read_parser = subparsers.add_parser("read", help="Read and analyze papers")
    read_parser.add_argument("--count", "-n", type=int, default=10, help="Number of papers")

    # report command
    subparsers.add_parser("report", help="Generate literature review report")

    # interactive command
    subparsers.add_parser("interactive", help="Run in interactive mode")

    # status command
    subparsers.add_parser("status", help="Show project status")

    args = parser.parse_args()

    if not args.command:
        parser.print_help()
        sys.exit(1)

    # Load configuration
    config = load_config(args.config)
    if args.data_dir:
        config.data_dir = args.data_dir
    config.setup_directories()

    # Run command
    try:
        if args.command == "new":
            asyncio.run(cmd_new(args.topic, config))
        elif args.command == "gather":
            asyncio.run(cmd_gather(config))
        elif args.command == "organize":
            asyncio.run(cmd_organize(config))
        elif args.command == "read":
            asyncio.run(cmd_read(args.count, config))
        elif args.command == "report":
            asyncio.run(cmd_report(config))
        elif args.command == "interactive":
            asyncio.run(cmd_interactive(config))
        elif args.command == "status":
            asyncio.run(cmd_status(config))
        else:
            parser.print_help()

    except KeyboardInterrupt:
        console.print("\n[yellow]Interrupted by user[/]")
        sys.exit(0)
    except Exception as e:
        console.print(f"[red]Error: {e}[/]")
        if config.debug:
            raise
        sys.exit(1)


if __name__ == "__main__":
    main()
