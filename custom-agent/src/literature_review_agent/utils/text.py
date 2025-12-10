"""Text processing utilities for the Literature Review Agent."""

import re
from typing import Optional
from urllib.parse import urlparse

import tiktoken


def extract_urls_from_text(text: str) -> list[str]:
    """Extract all URLs from plain text.

    Args:
        text: Text to extract URLs from

    Returns:
        List of extracted URLs
    """
    # URL regex pattern
    url_pattern = re.compile(
        r'https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+[/\w\-._~:/?#\[\]@!$&\'()*+,;=%]*'
    )
    urls = url_pattern.findall(text)
    return list(set(urls))  # Remove duplicates


def extract_urls_from_markdown(text: str) -> list[tuple[str, str]]:
    """Extract URLs and their anchor text from markdown.

    Args:
        text: Markdown text to extract URLs from

    Returns:
        List of (url, anchor_text) tuples
    """
    # Markdown link pattern: [text](url)
    md_pattern = re.compile(r'\[([^\]]+)\]\(([^)]+)\)')
    matches = md_pattern.findall(text)

    results = []
    for anchor, url in matches:
        # Skip non-http URLs (e.g., mailto:, file:)
        if url.startswith(('http://', 'https://')):
            results.append((url, anchor.strip()))

    # Also get plain URLs
    plain_urls = extract_urls_from_text(text)
    existing_urls = {url for url, _ in results}
    for url in plain_urls:
        if url not in existing_urls:
            results.append((url, ""))

    return results


def extract_arxiv_ids(text: str) -> list[str]:
    """Extract arXiv IDs from text.

    Args:
        text: Text to extract arXiv IDs from

    Returns:
        List of arXiv IDs (e.g., "2301.07041")
    """
    # arXiv ID patterns
    patterns = [
        r'arxiv[:\s]*(\d{4}\.\d{4,5}(?:v\d+)?)',  # arxiv:2301.07041
        r'arxiv\.org/abs/(\d{4}\.\d{4,5}(?:v\d+)?)',  # arxiv.org/abs/2301.07041
        r'arxiv\.org/pdf/(\d{4}\.\d{4,5}(?:v\d+)?)',  # arxiv.org/pdf/2301.07041
    ]

    ids = []
    for pattern in patterns:
        matches = re.findall(pattern, text, re.IGNORECASE)
        ids.extend(matches)

    return list(set(ids))


def extract_dois(text: str) -> list[str]:
    """Extract DOIs from text.

    Args:
        text: Text to extract DOIs from

    Returns:
        List of DOIs
    """
    # DOI pattern
    doi_pattern = re.compile(
        r'10\.\d{4,}/[^\s<>\"\'\)\]]+',
        re.IGNORECASE
    )
    dois = doi_pattern.findall(text)
    # Clean up trailing punctuation
    cleaned = [re.sub(r'[.,;:!?\)\]]+$', '', doi) for doi in dois]
    return list(set(cleaned))


def clean_text(text: str) -> str:
    """Clean and normalize text.

    Args:
        text: Text to clean

    Returns:
        Cleaned text
    """
    # Replace multiple whitespace with single space
    text = re.sub(r'\s+', ' ', text)
    # Remove leading/trailing whitespace
    text = text.strip()
    # Remove control characters (except newline and tab)
    text = re.sub(r'[\x00-\x08\x0b\x0c\x0e-\x1f\x7f-\x9f]', '', text)
    return text


def truncate_text(text: str, max_tokens: int, model: str = "cl100k_base") -> str:
    """Truncate text to a maximum number of tokens.

    Args:
        text: Text to truncate
        max_tokens: Maximum number of tokens
        model: Tokenizer model to use

    Returns:
        Truncated text
    """
    try:
        encoding = tiktoken.get_encoding(model)
    except Exception:
        encoding = tiktoken.get_encoding("cl100k_base")

    tokens = encoding.encode(text)
    if len(tokens) <= max_tokens:
        return text

    truncated_tokens = tokens[:max_tokens]
    truncated_text = encoding.decode(truncated_tokens)

    # Try to end at a sentence boundary
    last_period = truncated_text.rfind('.')
    last_newline = truncated_text.rfind('\n')
    boundary = max(last_period, last_newline)

    if boundary > len(truncated_text) * 0.8:  # Only if we keep most of the text
        truncated_text = truncated_text[:boundary + 1]

    return truncated_text + "..."


def count_tokens(text: str, model: str = "cl100k_base") -> int:
    """Count tokens in text.

    Args:
        text: Text to count tokens in
        model: Tokenizer model to use

    Returns:
        Number of tokens
    """
    try:
        encoding = tiktoken.get_encoding(model)
    except Exception:
        encoding = tiktoken.get_encoding("cl100k_base")

    return len(encoding.encode(text))


def is_academic_url(url: str) -> bool:
    """Check if URL is from an academic source.

    Args:
        url: URL to check

    Returns:
        True if URL appears to be from an academic source
    """
    academic_domains = [
        'arxiv.org',
        'doi.org',
        'semanticscholar.org',
        'scholar.google.com',
        'pubmed.ncbi.nlm.nih.gov',
        'nature.com',
        'science.org',
        'sciencedirect.com',
        'springer.com',
        'wiley.com',
        'ieee.org',
        'acm.org',
        'openreview.net',
        'papers.nips.cc',
        'proceedings.mlr.press',
        'aclanthology.org',
        'biorxiv.org',
        'medrxiv.org',
        'ssrn.com',
        'researchgate.net',
        'academia.edu',
    ]

    parsed = urlparse(url)
    domain = parsed.netloc.lower()

    return any(academic in domain for academic in academic_domains)


def normalize_title(title: str) -> str:
    """Normalize a paper title for comparison.

    Args:
        title: Title to normalize

    Returns:
        Normalized title
    """
    # Lowercase
    title = title.lower()
    # Remove punctuation
    title = re.sub(r'[^\w\s]', '', title)
    # Normalize whitespace
    title = ' '.join(title.split())
    return title
