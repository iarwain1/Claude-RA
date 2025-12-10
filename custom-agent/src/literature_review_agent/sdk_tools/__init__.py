"""
Custom MCP tools for the Literature Review Agent using Claude Agent SDK.

This module provides tools that the agent can use during research:
- Reference management (add, search, update, organize)
- Note taking and management
- Academic search (arXiv, Semantic Scholar)
- URL and blog processing
- Document reading
- Report generation
"""

from .reference_tools import (
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
    create_note,
    get_notes_for_reference,
    search_notes,
    get_key_findings,
)

from .search_tools import (
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
    create_subtopic,
    list_subtopics,
    add_subtopic_finding,
    add_subtopic_question,
    set_subtopic_summary,
)

from .report_tools import (
    generate_progress_report,
    export_references_bibtex,
    export_references_markdown,
)

from .server import create_literature_review_server

__all__ = [
    # Reference tools
    "add_reference",
    "search_references",
    "update_reference_priority",
    "update_reference_status",
    "get_reading_queue",
    "get_reference_stats",
    "add_reference_tag",
    "assign_subtopic",
    # Note tools
    "create_note",
    "get_notes_for_reference",
    "search_notes",
    "get_key_findings",
    # Search tools
    "search_arxiv",
    "search_semantic_scholar",
    "get_paper_citations",
    "get_paper_references",
    "get_recommendations",
    # Source tools
    "process_url_file",
    "process_blog_feed",
    "scan_local_folder",
    "fetch_webpage_content",
    # Subtopic tools
    "create_subtopic",
    "list_subtopics",
    "add_subtopic_finding",
    "add_subtopic_question",
    "set_subtopic_summary",
    # Report tools
    "generate_progress_report",
    "export_references_bibtex",
    "export_references_markdown",
    # Server
    "create_literature_review_server",
]
