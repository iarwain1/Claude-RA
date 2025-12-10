"""
MCP Server creation for the Literature Review Agent.

This module creates an in-process MCP server that provides all the
research tools to the Claude Agent SDK.
"""

from pathlib import Path
from typing import Any

from claude_code_sdk import create_sdk_mcp_server

from .reference_tools import (
    init_reference_manager,
    add_reference,
    search_references,
    update_reference_priority,
    update_reference_status,
    get_reading_queue,
    get_reference_stats,
    add_reference_tag,
    assign_subtopic,
)

from .note_tools import (
    init_note_manager,
    create_note,
    get_notes_for_reference,
    search_notes,
    get_key_findings,
)

from .search_tools import (
    init_search_tools,
    search_arxiv,
    search_semantic_scholar,
    get_paper_citations,
    get_paper_references,
    get_recommendations,
)

from .source_tools import (
    process_url_file,
    process_blog_feed,
    scan_local_folder,
    fetch_webpage_content,
)

from .subtopic_tools import (
    init_subtopic_manager,
    create_subtopic,
    list_subtopics,
    add_subtopic_finding,
    add_subtopic_question,
    set_subtopic_summary,
)

from .report_tools import (
    init_report_tools,
    generate_progress_report,
    export_references_bibtex,
    export_references_markdown,
)


def create_literature_review_server(
    data_dir: Path,
    output_dir: Path,
    arxiv_max_results: int = 50,
    semantic_scholar_max_results: int = 50,
) -> Any:
    """
    Create an MCP server with all literature review tools.

    Args:
        data_dir: Directory for storing research data (references, notes, etc.)
        output_dir: Directory for output files (reports, exports)
        arxiv_max_results: Maximum results for arXiv searches
        semantic_scholar_max_results: Maximum results for Semantic Scholar searches

    Returns:
        MCP server instance for use with ClaudeAgentOptions
    """
    # Ensure directories exist
    data_dir.mkdir(parents=True, exist_ok=True)
    output_dir.mkdir(parents=True, exist_ok=True)
    (data_dir / "references").mkdir(exist_ok=True)
    (data_dir / "notes").mkdir(exist_ok=True)

    # Initialize all managers and tools
    init_reference_manager(data_dir)
    init_note_manager(data_dir)
    init_subtopic_manager(data_dir)
    init_search_tools(arxiv_max_results, semantic_scholar_max_results)
    init_report_tools(output_dir)

    # Create MCP server with all tools
    server = create_sdk_mcp_server(
        name="literature-review",
        version="0.2.0",
        tools=[
            # Reference management
            add_reference,
            search_references,
            update_reference_priority,
            update_reference_status,
            get_reading_queue,
            get_reference_stats,
            add_reference_tag,
            assign_subtopic,

            # Note management
            create_note,
            get_notes_for_reference,
            search_notes,
            get_key_findings,

            # Academic search
            search_arxiv,
            search_semantic_scholar,
            get_paper_citations,
            get_paper_references,
            get_recommendations,

            # Source processing
            process_url_file,
            process_blog_feed,
            scan_local_folder,
            fetch_webpage_content,

            # Subtopic management
            create_subtopic,
            list_subtopics,
            add_subtopic_finding,
            add_subtopic_question,
            set_subtopic_summary,

            # Reports
            generate_progress_report,
            export_references_bibtex,
            export_references_markdown,
        ]
    )

    return server


# List of all tool names for use in allowed_tools
ALL_LITERATURE_REVIEW_TOOLS = [
    # Reference management
    "mcp__literature-review__add_reference",
    "mcp__literature-review__search_references",
    "mcp__literature-review__update_reference_priority",
    "mcp__literature-review__update_reference_status",
    "mcp__literature-review__get_reading_queue",
    "mcp__literature-review__get_reference_stats",
    "mcp__literature-review__add_reference_tag",
    "mcp__literature-review__assign_subtopic",

    # Note management
    "mcp__literature-review__create_note",
    "mcp__literature-review__get_notes_for_reference",
    "mcp__literature-review__search_notes",
    "mcp__literature-review__get_key_findings",

    # Academic search
    "mcp__literature-review__search_arxiv",
    "mcp__literature-review__search_semantic_scholar",
    "mcp__literature-review__get_paper_citations",
    "mcp__literature-review__get_paper_references",
    "mcp__literature-review__get_recommendations",

    # Source processing
    "mcp__literature-review__process_url_file",
    "mcp__literature-review__process_blog_feed",
    "mcp__literature-review__scan_local_folder",
    "mcp__literature-review__fetch_webpage_content",

    # Subtopic management
    "mcp__literature-review__create_subtopic",
    "mcp__literature-review__list_subtopics",
    "mcp__literature-review__add_subtopic_finding",
    "mcp__literature-review__add_subtopic_question",
    "mcp__literature-review__set_subtopic_summary",

    # Reports
    "mcp__literature-review__generate_progress_report",
    "mcp__literature-review__export_references_bibtex",
    "mcp__literature-review__export_references_markdown",
]

# Built-in tools that the agent should also have access to
BUILT_IN_TOOLS = [
    "Read",        # Read files
    "Write",       # Write files
    "Glob",        # Find files
    "Grep",        # Search file contents
    "WebFetch",    # Fetch web content
    "WebSearch",   # Search the web
]
