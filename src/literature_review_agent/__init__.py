"""
Literature Review Agent - An AI-powered research assistant for comprehensive literature reviews.

This agent helps researchers:
- Gather references from URLs, blogs, newsletters, and academic databases
- Organize and tag references by subtopic
- Read and analyze papers, taking detailed notes
- Follow citation trails to discover new sources
- Synthesize findings into comprehensive reports
"""

__version__ = "0.1.0"

from .agent import LiteratureReviewAgent
from .models import (
    Reference,
    Note,
    ResearchTopic,
    ResearchProject,
    SubTopic,
)

__all__ = [
    "LiteratureReviewAgent",
    "Reference",
    "Note",
    "ResearchTopic",
    "ResearchProject",
    "SubTopic",
]
