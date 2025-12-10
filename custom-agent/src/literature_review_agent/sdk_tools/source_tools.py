"""
Source processing tools for the Claude Agent SDK.

These tools allow the agent to process various source types:
- URL files and bookmark lists
- Blog RSS feeds
- Local files and Obsidian vaults
- Web pages
"""

import asyncio
from pathlib import Path
from typing import Any

from claude_code_sdk import tool

from ..collectors import URLCollector, BlogCollector, LocalFileCollector
from .reference_tools import get_ref_manager


# Collector instances
_url_collector: URLCollector | None = None
_blog_collector: BlogCollector | None = None
_local_collector: LocalFileCollector | None = None


def get_url_collector() -> URLCollector:
    global _url_collector
    if _url_collector is None:
        _url_collector = URLCollector()
    return _url_collector


def get_blog_collector() -> BlogCollector:
    global _blog_collector
    if _blog_collector is None:
        _blog_collector = BlogCollector()
    return _blog_collector


def get_local_collector() -> LocalFileCollector:
    global _local_collector
    if _local_collector is None:
        _local_collector = LocalFileCollector()
    return _local_collector


@tool(
    name="process_url_file",
    description="Process a file containing URLs (txt or markdown). Extracts links and adds them to the reference collection.",
    input_schema={
        "type": "object",
        "properties": {
            "file_path": {"type": "string", "description": "Path to the URL list file"},
            "follow_links": {
                "type": "boolean",
                "description": "Follow links to extract more metadata",
                "default": True
            },
            "max_depth": {
                "type": "integer",
                "description": "Depth for following links",
                "default": 1
            }
        },
        "required": ["file_path"]
    }
)
async def process_url_file(args: dict[str, Any]) -> dict:
    """Process a file containing URLs."""
    collector = get_url_collector()
    file_path = Path(args["file_path"])

    if not file_path.exists():
        return {"content": [{"type": "text", "text": f"File not found: {file_path}"}]}

    result = await collector.collect(
        file_paths=[file_path],
        follow_links=args.get("follow_links", True),
        max_depth=args.get("max_depth", 1),
    )

    if result.errors:
        error_msg = f"\nErrors: {'; '.join(result.errors[:3])}"
    else:
        error_msg = ""

    # Add to collection
    manager = get_ref_manager()
    new_count, updated = manager.add_batch(result.references)

    lines = [
        f"Processed URL file: {file_path.name}",
        f"Found {len(result.references)} references",
        f"Added {new_count} new, updated {updated} existing",
    ]

    if result.references:
        lines.append("\nSample references found:")
        for ref in result.references[:5]:
            lines.append(f"- {ref.title[:60]}...")

    lines.append(error_msg)
    return {"content": [{"type": "text", "text": "\n".join(lines)}]}


@tool(
    name="process_blog_feed",
    description="Process a blog or newsletter RSS feed. Extracts posts and links to papers/articles.",
    input_schema={
        "type": "object",
        "properties": {
            "feed_url": {"type": "string", "description": "RSS feed URL (or blog URL to auto-discover feed)"},
            "max_entries": {
                "type": "integer",
                "description": "Maximum entries to process",
                "default": 50
            },
            "extract_links": {
                "type": "boolean",
                "description": "Extract links from post content",
                "default": True
            },
            "days_back": {
                "type": "integer",
                "description": "Only include posts from the last N days (optional)"
            }
        },
        "required": ["feed_url"]
    }
)
async def process_blog_feed(args: dict[str, Any]) -> dict:
    """Process a blog RSS feed."""
    collector = get_blog_collector()

    from datetime import datetime, timedelta
    date_from = None
    if args.get("days_back"):
        date_from = datetime.now() - timedelta(days=args["days_back"])

    result = await collector.collect(
        feed_urls=[args["feed_url"]] if "rss" in args["feed_url"].lower() or "feed" in args["feed_url"].lower() else None,
        blog_urls=[args["feed_url"]] if "rss" not in args["feed_url"].lower() and "feed" not in args["feed_url"].lower() else None,
        max_entries=args.get("max_entries", 50),
        date_from=date_from,
        extract_links=args.get("extract_links", True),
    )

    if result.errors:
        error_msg = f"\nErrors: {'; '.join(result.errors[:3])}"
    else:
        error_msg = ""

    # Add to collection
    manager = get_ref_manager()
    new_count, updated = manager.add_batch(result.references)

    lines = [
        f"Processed blog/feed: {args['feed_url']}",
        f"Found {len(result.references)} references",
        f"Added {new_count} new, updated {updated} existing",
    ]

    if result.references:
        lines.append("\nSample posts/links found:")
        for ref in result.references[:5]:
            lines.append(f"- {ref.title[:60]}...")

    lines.append(error_msg)
    return {"content": [{"type": "text", "text": "\n".join(lines)}]}


@tool(
    name="scan_local_folder",
    description="Scan a local folder for notes, PDFs, and documents. Works with Obsidian vaults.",
    input_schema={
        "type": "object",
        "properties": {
            "folder_path": {"type": "string", "description": "Path to the folder to scan"},
            "file_types": {
                "type": "array",
                "items": {"type": "string"},
                "description": "File extensions to include",
                "default": [".md", ".txt", ".pdf"]
            },
            "recursive": {
                "type": "boolean",
                "description": "Scan subdirectories",
                "default": True
            },
            "extract_links": {
                "type": "boolean",
                "description": "Extract URLs from text files",
                "default": True
            }
        },
        "required": ["folder_path"]
    }
)
async def scan_local_folder(args: dict[str, Any]) -> dict:
    """Scan a local folder for documents."""
    collector = get_local_collector()
    folder_path = Path(args["folder_path"])

    if not folder_path.exists():
        return {"content": [{"type": "text", "text": f"Folder not found: {folder_path}"}]}

    result = await collector.collect(
        paths=[folder_path],
        file_types=args.get("file_types", [".md", ".txt", ".pdf"]),
        recursive=args.get("recursive", True),
        extract_links=args.get("extract_links", True),
    )

    if result.errors:
        error_msg = f"\nErrors: {'; '.join(result.errors[:3])}"
    else:
        error_msg = ""

    # Add to collection
    manager = get_ref_manager()
    new_count, updated = manager.add_batch(result.references)

    lines = [
        f"Scanned folder: {folder_path}",
        f"Found {len(result.references)} references",
        f"Added {new_count} new, updated {updated} existing",
    ]

    if result.warnings:
        lines.append(f"\nWarnings: {len(result.warnings)} files had issues")

    if result.references:
        lines.append("\nSample items found:")
        for ref in result.references[:5]:
            lines.append(f"- [{ref.ref_type.value}] {ref.title[:50]}...")

    lines.append(error_msg)
    return {"content": [{"type": "text", "text": "\n".join(lines)}]}


@tool(
    name="fetch_webpage_content",
    description="Fetch and extract content from a webpage. Use this to read articles, blog posts, or paper abstracts.",
    input_schema={
        "type": "object",
        "properties": {
            "url": {"type": "string", "description": "URL to fetch"},
            "extract_links": {
                "type": "boolean",
                "description": "Also extract links from the page",
                "default": False
            }
        },
        "required": ["url"]
    }
)
async def fetch_webpage_content(args: dict[str, Any]) -> dict:
    """Fetch content from a webpage."""
    from ..processors import DocumentReader

    reader = DocumentReader()

    try:
        from ..models import Reference
        ref = Reference(id="temp", title="Webpage", url=args["url"])
        content = await reader._read_webpage(args["url"])

        if not content:
            return {"content": [{"type": "text", "text": f"Could not extract content from {args['url']}"}]}

        # Truncate if too long
        if len(content) > 15000:
            content = content[:15000] + "\n\n[Content truncated...]"

        lines = [f"Content from {args['url']}:\n", "---", content]

        if args.get("extract_links"):
            collector = get_url_collector()
            result = await collector.collect(urls=[args["url"]], follow_links=False)
            if result.references:
                manager = get_ref_manager()
                new_count, _ = manager.add_batch(result.references)
                lines.append(f"\n---\nExtracted {new_count} new links from page.")

        return {"content": [{"type": "text", "text": "\n".join(lines)}]}

    except Exception as e:
        return {"content": [{"type": "text", "text": f"Error fetching {args['url']}: {e}"}]}
    finally:
        await reader.close()
