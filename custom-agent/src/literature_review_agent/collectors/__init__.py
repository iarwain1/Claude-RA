"""
Source collectors for gathering references from various sources.

This module provides collectors for:
- URL lists and markdown files
- Blogs and newsletters (RSS feeds)
- arXiv
- Semantic Scholar
- Web search
- Local files (Obsidian notes, PDFs, etc.)
"""

from .base import BaseCollector, CollectorResult
from .url_collector import URLCollector
from .arxiv_collector import ArxivCollector
from .semantic_scholar_collector import SemanticScholarCollector
from .web_collector import WebCollector
from .local_collector import LocalFileCollector
from .blog_collector import BlogCollector

__all__ = [
    "BaseCollector",
    "CollectorResult",
    "URLCollector",
    "ArxivCollector",
    "SemanticScholarCollector",
    "WebCollector",
    "LocalFileCollector",
    "BlogCollector",
]
