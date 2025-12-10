"""
Command-line interface for the Literature Review Agent.

Usage:
    lit-review interactive           Run in interactive mode (recommended)
    lit-review query "<prompt>"      Send a single query to the agent
    lit-review gather "<topic>"      Gather references on a topic
    lit-review organize              Organize and prioritize references
    lit-review read [--count=N]      Read and analyze papers
    lit-review report                Generate the literature review report
    lit-review status                Show project status

The CLI uses the Claude Agent SDK for intelligent, tool-based research automation.
"""

import sys
from pathlib import Path
from typing import Optional

import anyio
from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt
from rich.table import Table
from rich.live import Live
from rich.spinner import Spinner
from rich.text import Text

from .sdk_agent import SDKLiteratureReviewAgent
from .utils.config import load_config, Config


console = Console()


def print_message(msg: str) -> None:
    """Print a message from the agent."""
    console.print(f"[blue]{msg}[/]")


def print_tool_use(tool_name: str, args: dict) -> None:
    """Print tool usage notification."""
    # Simplify tool name
    if tool_name.startswith("mcp__literature-review__"):
        tool_name = tool_name.replace("mcp__literature-review__", "")
    console.print(f"  [dim][Using: {tool_name}][/dim]")


async def cmd_interactive(config: Config) -> None:
    """Run the agent in interactive mode.

    Args:
        config: Configuration
    """
    console.print(Panel.fit(
        "[bold cyan]Literature Review Agent[/bold cyan]\n"
        "[dim]Powered by Claude Agent SDK[/dim]",
        border_style="cyan"
    ))

    agent = SDKLiteratureReviewAgent(
        config=config,
        data_dir=config.data_dir,
        output_dir=config.output_dir,
    )

    console.print(
        "\n[bold]Welcome![/bold] I'm your research assistant.\n"
        "Tell me about your research topic, or try commands like:\n"
        "  • 'Search arXiv for papers on transformer architectures'\n"
        "  • 'Process my bookmarks at ~/research/bookmarks.md'\n"
        "  • 'Show the reading queue'\n"
        "  • 'Generate a progress report'\n"
        "\nType [bold]exit[/bold] to quit.\n"
    )

    while True:
        try:
            user_input = Prompt.ask("\n[bold green]You[/bold green]")

            if user_input.lower() in ["exit", "quit", "q"]:
                console.print("\n[cyan]Goodbye! Your research has been saved.[/cyan]")
                break

            if not user_input.strip():
                continue

            console.print()

            # Query the agent
            response = await agent.query(
                prompt=user_input,
                on_message=print_message,
                on_tool_use=print_tool_use,
            )

        except KeyboardInterrupt:
            console.print("\n[yellow]Interrupted. Your research has been saved.[/yellow]")
            break
        except Exception as e:
            console.print(f"[red]Error: {e}[/red]")


async def cmd_query(prompt: str, config: Config) -> None:
    """Send a single query to the agent.

    Args:
        prompt: Query to send
        config: Configuration
    """
    agent = SDKLiteratureReviewAgent(
        config=config,
        data_dir=config.data_dir,
        output_dir=config.output_dir,
    )

    console.print(f"[dim]Query: {prompt}[/dim]\n")

    response = await agent.query(
        prompt=prompt,
        on_message=print_message,
        on_tool_use=print_tool_use,
    )


async def cmd_gather(topic: str, config: Config) -> None:
    """Gather references on a topic.

    Args:
        topic: Research topic
        config: Configuration
    """
    console.print(f"[bold]Gathering references on:[/bold] {topic}\n")

    agent = SDKLiteratureReviewAgent(
        config=config,
        data_dir=config.data_dir,
        output_dir=config.output_dir,
    )

    count = await agent.gather_references(
        topic=topic,
        on_progress=print_message,
    )

    console.print(f"\n[green]Found {count} total references[/green]")


async def cmd_organize(config: Config) -> None:
    """Organize and prioritize references.

    Args:
        config: Configuration
    """
    console.print("[bold]Organizing references...[/bold]\n")

    agent = SDKLiteratureReviewAgent(
        config=config,
        data_dir=config.data_dir,
        output_dir=config.output_dir,
    )

    await agent.organize_references(on_progress=print_message)

    console.print("\n[green]Organization complete![/green]")


async def cmd_read(count: int, config: Config) -> None:
    """Read and analyze papers.

    Args:
        count: Number of papers to read
        config: Configuration
    """
    console.print(f"[bold]Reading up to {count} papers...[/bold]\n")

    agent = SDKLiteratureReviewAgent(
        config=config,
        data_dir=config.data_dir,
        output_dir=config.output_dir,
    )

    processed = await agent.read_papers(
        count=count,
        on_progress=print_message,
    )

    console.print(f"\n[green]Processed {processed} papers[/green]")


async def cmd_report(config: Config) -> None:
    """Generate the literature review report.

    Args:
        config: Configuration
    """
    console.print("[bold]Generating report...[/bold]\n")

    agent = SDKLiteratureReviewAgent(
        config=config,
        data_dir=config.data_dir,
        output_dir=config.output_dir,
    )

    output_path = await agent.generate_report(on_progress=print_message)

    console.print(f"\n[green]Report saved to: {output_path}[/green]")


async def cmd_status(config: Config) -> None:
    """Show project status.

    Args:
        config: Configuration
    """
    # Initialize managers through SDK tools
    from .sdk_tools.reference_tools import init_reference_manager, get_ref_manager
    from .sdk_tools.note_tools import init_note_manager, get_note_manager
    from .sdk_tools.subtopic_tools import init_subtopic_manager, get_subtopic_manager

    init_reference_manager(config.data_dir)
    init_note_manager(config.data_dir)
    init_subtopic_manager(config.data_dir)

    ref_stats = get_ref_manager().get_statistics()
    note_stats = get_note_manager().get_statistics()
    subtopic_stats = get_subtopic_manager().get_statistics()

    # Display status table
    table = Table(title="Literature Review Status")
    table.add_column("Category", style="cyan")
    table.add_column("Metric", style="white")
    table.add_column("Value", style="green")

    # References
    table.add_row("References", "Total", str(ref_stats["total"]))
    table.add_row("", "Discovered", str(ref_stats["by_status"].get("discovered", 0)))
    table.add_row("", "In Queue", str(ref_stats["by_status"].get("queued", 0)))
    table.add_row("", "Completed", str(ref_stats["by_status"].get("completed", 0)))

    # Priority breakdown
    table.add_row("Priority", "Critical", str(ref_stats["by_priority"].get("critical", 0)))
    table.add_row("", "High", str(ref_stats["by_priority"].get("high", 0)))
    table.add_row("", "Medium", str(ref_stats["by_priority"].get("medium", 0)))

    # Notes
    table.add_row("Notes", "Total", str(note_stats["total"]))
    table.add_row("", "Key Findings", str(note_stats["by_type"].get("key_finding", 0)))

    # Subtopics
    table.add_row("Subtopics", "Total", str(subtopic_stats["total"]))
    table.add_row("", "Findings", str(subtopic_stats["total_findings"]))
    table.add_row("", "Questions", str(subtopic_stats["total_questions"]))

    console.print(table)


def main():
    """Main CLI entry point."""
    import argparse

    parser = argparse.ArgumentParser(
        description="Literature Review Agent - AI-powered research assistant using Claude Agent SDK",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
    lit-review interactive
    lit-review query "Search arXiv for papers on LLM agents"
    lit-review gather "Large Language Model Agents"
    lit-review read --count 5
    lit-review report
    lit-review status
        """,
    )

    parser.add_argument(
        "--config", "-c",
        type=Path,
        help="Path to config file",
    )
    parser.add_argument(
        "--data-dir", "-d",
        type=Path,
        help="Data directory for research files",
    )
    parser.add_argument(
        "--output-dir", "-o",
        type=Path,
        help="Output directory for reports",
    )

    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    # interactive command (default/recommended)
    subparsers.add_parser(
        "interactive",
        help="Run in interactive mode (recommended)"
    )

    # query command
    query_parser = subparsers.add_parser(
        "query",
        help="Send a single query to the agent"
    )
    query_parser.add_argument("prompt", help="Query to send")

    # gather command
    gather_parser = subparsers.add_parser(
        "gather",
        help="Gather references on a topic"
    )
    gather_parser.add_argument("topic", help="Research topic")

    # organize command
    subparsers.add_parser(
        "organize",
        help="Organize and prioritize references"
    )

    # read command
    read_parser = subparsers.add_parser(
        "read",
        help="Read and analyze papers from the queue"
    )
    read_parser.add_argument(
        "--count", "-n",
        type=int,
        default=5,
        help="Number of papers to read"
    )

    # report command
    subparsers.add_parser(
        "report",
        help="Generate literature review report"
    )

    # status command
    subparsers.add_parser(
        "status",
        help="Show project status"
    )

    args = parser.parse_args()

    # Default to interactive if no command
    if not args.command:
        args.command = "interactive"

    # Load configuration
    config = load_config(args.config)
    if args.data_dir:
        config.data_dir = args.data_dir
    if args.output_dir:
        config.output_dir = args.output_dir
    config.setup_directories()

    # Run command
    try:
        if args.command == "interactive":
            anyio.run(cmd_interactive, config)
        elif args.command == "query":
            anyio.run(cmd_query, args.prompt, config)
        elif args.command == "gather":
            anyio.run(cmd_gather, args.topic, config)
        elif args.command == "organize":
            anyio.run(cmd_organize, config)
        elif args.command == "read":
            anyio.run(cmd_read, args.count, config)
        elif args.command == "report":
            anyio.run(cmd_report, config)
        elif args.command == "status":
            anyio.run(cmd_status, config)
        else:
            parser.print_help()

    except KeyboardInterrupt:
        console.print("\n[yellow]Interrupted by user[/yellow]")
        sys.exit(0)
    except Exception as e:
        console.print(f"[red]Error: {e}[/red]")
        if config.debug:
            raise
        sys.exit(1)


if __name__ == "__main__":
    main()
