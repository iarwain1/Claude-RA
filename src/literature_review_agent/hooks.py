"""
Hooks for the Literature Review Agent.

This module provides hooks for:
- Logging tool usage
- User notifications
- Permission checks
"""

import json
from datetime import datetime
from pathlib import Path
from typing import Any, Callable

from claude_code_sdk import HookResult


# Callback types
MessageCallback = Callable[[str, str], None]  # (message_type, content)


class AgentHooks:
    """
    Hooks manager for the Literature Review Agent.

    Provides pre/post tool hooks for logging, notifications, and permissions.
    """

    def __init__(
        self,
        log_file: Path | None = None,
        message_callback: MessageCallback | None = None,
        verbose: bool = False,
    ):
        """Initialize hooks.

        Args:
            log_file: Path to log file for tool usage
            message_callback: Callback for user notifications
            verbose: Whether to log all tool calls
        """
        self.log_file = log_file
        self.message_callback = message_callback
        self.verbose = verbose

        # Tool call counter
        self.tool_calls = 0
        self.tool_history: list[dict] = []

        # Tools that should notify the user
        self.notable_tools = {
            "search_arxiv": "Searching arXiv",
            "search_semantic_scholar": "Searching Semantic Scholar",
            "get_paper_citations": "Finding citations",
            "get_paper_references": "Finding references",
            "process_url_file": "Processing URL file",
            "process_blog_feed": "Processing blog feed",
            "scan_local_folder": "Scanning local folder",
            "create_subtopic": "Creating subtopic",
            "create_note": "Taking notes",
            "generate_progress_report": "Generating report",
            "export_references_bibtex": "Exporting BibTeX",
            "export_references_markdown": "Exporting markdown",
        }

    def _log(self, entry: dict) -> None:
        """Write a log entry."""
        if self.log_file:
            self.log_file.parent.mkdir(parents=True, exist_ok=True)
            with open(self.log_file, "a") as f:
                f.write(json.dumps(entry) + "\n")

    def _notify(self, message_type: str, content: str) -> None:
        """Send a notification to the user."""
        if self.message_callback:
            self.message_callback(message_type, content)

    async def pre_tool_hook(
        self,
        tool_name: str,
        tool_input: dict[str, Any],
    ) -> HookResult:
        """
        Pre-tool execution hook.

        Called before each tool is executed. Can be used for:
        - Logging
        - User notifications
        - Permission checks
        - Input modification

        Args:
            tool_name: Name of the tool being called
            tool_input: Input arguments for the tool

        Returns:
            HookResult indicating whether to proceed
        """
        self.tool_calls += 1
        timestamp = datetime.now().isoformat()

        # Log the call
        entry = {
            "timestamp": timestamp,
            "tool": tool_name,
            "input": tool_input,
            "call_number": self.tool_calls,
        }
        self._log(entry)
        self.tool_history.append(entry)

        # Verbose logging
        if self.verbose:
            print(f"  [{self.tool_calls}] Calling: {tool_name}")

        # Notify user for notable tools
        # Extract base tool name (remove mcp__ prefix)
        base_name = tool_name
        if tool_name.startswith("mcp__literature-review__"):
            base_name = tool_name.replace("mcp__literature-review__", "")

        if base_name in self.notable_tools:
            description = self.notable_tools[base_name]
            self._notify("tool_start", f"{description}...")

        # Always allow (no blocking)
        return HookResult.ALLOW

    async def post_tool_hook(
        self,
        tool_name: str,
        tool_input: dict[str, Any],
        tool_output: Any,
    ) -> None:
        """
        Post-tool execution hook.

        Called after each tool completes. Used for:
        - Logging results
        - User notifications
        - Statistics tracking

        Args:
            tool_name: Name of the tool that was called
            tool_input: Input arguments used
            tool_output: Output from the tool
        """
        timestamp = datetime.now().isoformat()

        # Log completion
        entry = {
            "timestamp": timestamp,
            "tool": tool_name,
            "status": "completed",
            "output_preview": str(tool_output)[:200] if tool_output else None,
        }
        self._log(entry)

        # Notify for certain completions
        base_name = tool_name
        if tool_name.startswith("mcp__literature-review__"):
            base_name = tool_name.replace("mcp__literature-review__", "")

        # Special notifications for search completions
        if base_name in ["search_arxiv", "search_semantic_scholar"]:
            if "Found" in str(tool_output):
                self._notify("tool_complete", str(tool_output)[:100])

    def get_statistics(self) -> dict:
        """Get hook statistics.

        Returns:
            Dictionary of statistics
        """
        # Count by tool
        tool_counts: dict[str, int] = {}
        for entry in self.tool_history:
            tool = entry["tool"]
            tool_counts[tool] = tool_counts.get(tool, 0) + 1

        return {
            "total_calls": self.tool_calls,
            "by_tool": tool_counts,
        }


def create_logging_hook(log_dir: Path) -> AgentHooks:
    """
    Create a hooks instance configured for logging.

    Args:
        log_dir: Directory for log files

    Returns:
        Configured AgentHooks instance
    """
    log_file = log_dir / f"agent_log_{datetime.now().strftime('%Y%m%d_%H%M%S')}.jsonl"
    return AgentHooks(log_file=log_file, verbose=True)


def create_interactive_hooks(
    message_callback: MessageCallback,
    log_dir: Path | None = None,
) -> AgentHooks:
    """
    Create a hooks instance for interactive mode.

    Args:
        message_callback: Callback for user messages
        log_dir: Optional log directory

    Returns:
        Configured AgentHooks instance
    """
    log_file = None
    if log_dir:
        log_file = log_dir / f"session_{datetime.now().strftime('%Y%m%d_%H%M%S')}.jsonl"

    return AgentHooks(
        log_file=log_file,
        message_callback=message_callback,
        verbose=False,
    )
