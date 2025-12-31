#!/usr/bin/env python3
"""
Enhanced metadata fetcher for arXiv papers using multiple APIs.
Run this script LOCALLY on your machine (not in Claude Code remote environment).

Features:
- Primary: arXiv API for arXiv papers
- Fallback: Semantic Scholar API (works for arXiv and other papers)
- Creates note files with abstracts
- Updates links.yaml with metadata

Usage:
    python fetch_metadata_local.py                    # Process all unprocessed papers
    python fetch_metadata_local.py --limit 50        # Process 50 papers
    python fetch_metadata_local.py --test            # Test APIs first
    python fetch_metadata_local.py --semantic-only   # Use only Semantic Scholar
"""

import re
import urllib.request
import urllib.parse
import xml.etree.ElementTree as ET
import json
import time
import os
import argparse
from datetime import datetime
from pathlib import Path

# Configuration
ARXIV_BATCH_SIZE = 50  # arXiv recommends max 200
SEMANTIC_SCHOLAR_BATCH_SIZE = 100  # S2 allows 100 per request
DELAY_BETWEEN_BATCHES = 3  # seconds
DELAY_BETWEEN_APIS = 1  # seconds between individual API calls
LINKS_FILE = 'links.yaml'
NOTES_DIR = 'notes'

# API endpoints
ARXIV_API = "http://export.arxiv.org/api/query"
S2_API = "https://api.semanticscholar.org/graph/v1/paper"
S2_BATCH_API = "https://api.semanticscholar.org/graph/v1/paper/batch"


def test_apis():
    """Test connectivity to both APIs."""
    print("Testing API connectivity...")

    # Test arXiv
    print("\n1. Testing arXiv API...")
    try:
        url = f"{ARXIV_API}?id_list=2312.06942&max_results=1"
        req = urllib.request.Request(url, headers={'User-Agent': 'Claude-RA/1.0'})
        with urllib.request.urlopen(req, timeout=30) as resp:
            data = resp.read().decode('utf-8')
            if '<entry>' in data:
                print("   [OK] arXiv API: Working")
            else:
                print("   [X] arXiv API: No data returned")
    except Exception as e:
        print(f"   [X] arXiv API: {e}")

    # Test Semantic Scholar
    print("\n2. Testing Semantic Scholar API...")
    try:
        url = f"{S2_API}/arXiv:2312.06942?fields=title,abstract,authors,year"
        req = urllib.request.Request(url, headers={'User-Agent': 'Claude-RA/1.0'})
        with urllib.request.urlopen(req, timeout=30) as resp:
            data = json.loads(resp.read())
            if data.get('title'):
                print(f"   [OK] Semantic Scholar API: Working")
                print(f"      Found: {data['title'][:60]}...")
            else:
                print("   [X] Semantic Scholar API: No data returned")
    except Exception as e:
        print(f"   [X] Semantic Scholar API: {e}")

    print("\nTest complete.")


def extract_arxiv_entries(content):
    """Extract all arXiv entries that need processing from links.yaml."""
    # Match entries with arXiv URLs
    pattern = r'  - id: (arxiv-[\d.v]+)\n    title: "([^"]*)"\n[^-]*?url: "https://arxiv\.org/abs/([\d.v]+)"'
    matches = re.findall(pattern, content, re.DOTALL)

    entries = []
    for entry_id, title, arxiv_id in matches:
        # Check if already has notes (skip if so)
        entry_block_match = re.search(
            rf'  - id: {re.escape(entry_id)}.*?(?=\n  - id:|$)',
            content,
            re.DOTALL
        )
        if entry_block_match:
            entry_block = entry_block_match.group(0)
            # Skip if already has notes
            if 'notes:' in entry_block and 'path:' in entry_block:
                continue

        entries.append((entry_id, title, arxiv_id))

    return entries


def fetch_arxiv_batch(arxiv_ids):
    """Fetch metadata from arXiv API for a batch of IDs."""
    clean_ids = [re.sub(r'v\d+$', '', aid) for aid in arxiv_ids]
    id_list = ','.join(clean_ids)

    url = f"{ARXIV_API}?id_list={id_list}&max_results={len(clean_ids)}"
    headers = {'User-Agent': 'Claude-RA-Literature-Review/1.0'}

    req = urllib.request.Request(url, headers=headers)

    try:
        with urllib.request.urlopen(req, timeout=60) as response:
            return response.read().decode('utf-8')
    except Exception as e:
        print(f"  arXiv API error: {e}")
        return None


def parse_arxiv_response(xml_content):
    """Parse arXiv API XML response into structured data."""
    results = {}

    try:
        root = ET.fromstring(xml_content)
    except ET.ParseError as e:
        print(f"  XML parse error: {e}")
        return results

    ns = {'atom': 'http://www.w3.org/2005/Atom', 'arxiv': 'http://arxiv.org/schemas/atom'}

    for entry in root.findall('atom:entry', ns):
        id_elem = entry.find('atom:id', ns)
        if id_elem is None:
            continue

        arxiv_url = id_elem.text
        arxiv_id = arxiv_url.split('/')[-1]
        arxiv_id_base = re.sub(r'v\d+$', '', arxiv_id)

        title_elem = entry.find('atom:title', ns)
        title = title_elem.text.strip().replace('\n', ' ').replace('  ', ' ') if title_elem is not None else None

        summary_elem = entry.find('atom:summary', ns)
        abstract = summary_elem.text.strip() if summary_elem is not None else None

        authors = []
        for author in entry.findall('atom:author', ns):
            name_elem = author.find('atom:name', ns)
            if name_elem is not None:
                authors.append(name_elem.text)

        published_elem = entry.find('atom:published', ns)
        published = published_elem.text[:10] if published_elem is not None else None

        categories = []
        for cat in entry.findall('atom:category', ns):
            term = cat.get('term')
            if term:
                categories.append(term)

        results[arxiv_id_base] = {
            'title': title,
            'authors': authors,
            'abstract': abstract,
            'date_published': published,
            'categories': categories,
            'source': 'arxiv'
        }

    return results


def fetch_semantic_scholar(arxiv_id):
    """Fetch metadata from Semantic Scholar API for a single arXiv paper."""
    clean_id = re.sub(r'v\d+$', '', arxiv_id)
    url = f"{S2_API}/arXiv:{clean_id}?fields=title,abstract,authors,year,venue,citationCount,externalIds"

    headers = {'User-Agent': 'Claude-RA-Literature-Review/1.0'}
    req = urllib.request.Request(url, headers=headers)

    try:
        with urllib.request.urlopen(req, timeout=30) as response:
            data = json.loads(response.read())

            if not data.get('title'):
                return None

            authors = [a.get('name', '') for a in data.get('authors', [])]

            return {
                'title': data.get('title'),
                'authors': authors,
                'abstract': data.get('abstract'),
                'date_published': str(data.get('year')) if data.get('year') else None,
                'venue': data.get('venue'),
                'citation_count': data.get('citationCount'),
                'source': 'semantic_scholar'
            }
    except urllib.error.HTTPError as e:
        if e.code == 404:
            return None  # Paper not found
        print(f"  S2 API error for {arxiv_id}: {e}")
        return None
    except Exception as e:
        print(f"  S2 API error for {arxiv_id}: {e}")
        return None


def fetch_semantic_scholar_batch(arxiv_ids):
    """Fetch metadata from Semantic Scholar API for multiple papers."""
    results = {}

    # Convert to S2 format
    paper_ids = [f"arXiv:{re.sub(r'v[0-9]+$', '', aid)}" for aid in arxiv_ids]

    url = S2_BATCH_API
    headers = {
        'User-Agent': 'Claude-RA-Literature-Review/1.0',
        'Content-Type': 'application/json'
    }

    payload = json.dumps({
        "ids": paper_ids,
        "fields": "title,abstract,authors,year,venue,citationCount"
    }).encode('utf-8')

    req = urllib.request.Request(url, data=payload, headers=headers, method='POST')

    try:
        with urllib.request.urlopen(req, timeout=60) as response:
            data = json.loads(response.read())

            for i, paper in enumerate(data):
                if paper is None:
                    continue

                arxiv_id = arxiv_ids[i]
                arxiv_id_base = re.sub(r'v\d+$', '', arxiv_id)

                authors = [a.get('name', '') for a in paper.get('authors', [])]

                results[arxiv_id_base] = {
                    'title': paper.get('title'),
                    'authors': authors,
                    'abstract': paper.get('abstract'),
                    'date_published': str(paper.get('year')) if paper.get('year') else None,
                    'venue': paper.get('venue'),
                    'citation_count': paper.get('citationCount'),
                    'source': 'semantic_scholar'
                }

            return results
    except Exception as e:
        print(f"  S2 batch API error: {e}")
        # Fall back to individual requests
        print("  Falling back to individual requests...")
        for arxiv_id in arxiv_ids:
            result = fetch_semantic_scholar(arxiv_id)
            if result:
                arxiv_id_base = re.sub(r'v\d+$', '', arxiv_id)
                results[arxiv_id_base] = result
            time.sleep(0.5)  # Rate limit for individual requests
        return results


def create_note_file(entry_id, arxiv_id, data, notes_dir):
    """Create a markdown note file for a paper."""
    if not data.get('abstract'):
        return None

    filename = f"{entry_id}.md"
    filepath = os.path.join(notes_dir, filename)

    # Skip if file exists and has content
    if os.path.exists(filepath) and os.path.getsize(filepath) > 100:
        return None

    authors_str = ', '.join(data['authors'][:5])
    if len(data['authors']) > 5:
        authors_str += f", et al. ({len(data['authors'])} total)"

    # Build content
    content = f"""# {data['title']}

**arXiv:** [{arxiv_id}](https://arxiv.org/abs/{arxiv_id})
**Authors:** {authors_str}
**Date:** {data.get('date_published', 'Unknown')}
"""

    if data.get('categories'):
        content += f"**Categories:** {', '.join(data['categories'][:3])}\n"

    if data.get('venue'):
        content += f"**Venue:** {data['venue']}\n"

    if data.get('citation_count'):
        content += f"**Citations:** {data['citation_count']}\n"

    content += f"\n## Abstract\n\n{data['abstract']}\n"

    content += f"\n---\n*Metadata fetched via {data.get('source', 'unknown')} API on {datetime.now().strftime('%Y-%m-%d')}*\n"

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

    return filename


def update_links_yaml(content, updates, notes_created):
    """Update links.yaml with fetched metadata."""
    updated_count = 0

    for entry_id, data in updates.items():
        if not data.get('title'):
            continue

        # Escape title for YAML
        title = data['title'].replace('"', '\\"').replace('\n', ' ')

        # Update title
        pattern = rf'(  - id: {re.escape(entry_id)}\n    title: ")[^"]*(")'
        if re.search(pattern, content):
            content = re.sub(pattern, rf'\1{title}\2', content)
            updated_count += 1

        # Add/update date_published
        if data.get('date_published'):
            # Check if already exists
            entry_match = re.search(
                rf'(  - id: {re.escape(entry_id)}.*?)((?=\n  - id:)|$)',
                content,
                re.DOTALL
            )
            if entry_match:
                entry_block = entry_match.group(1)
                if 'date_published:' not in entry_block:
                    # Find a good place to insert (after importance)
                    insert_pattern = rf'(  - id: {re.escape(entry_id)}.*?importance: \w+)'
                    if re.search(insert_pattern, content, re.DOTALL):
                        content = re.sub(
                            insert_pattern,
                            rf'\1\n    date_published: "{data["date_published"]}"',
                            content,
                            flags=re.DOTALL,
                            count=1
                        )

        # Add notes reference - check both newly created and existing files
        note_filename = f"{entry_id}.md"
        note_filepath = os.path.join('notes', note_filename)

        # Check if note file exists (either just created or already present)
        should_add_notes = entry_id in notes_created or os.path.exists(note_filepath)

        if should_add_notes:
            entry_match = re.search(
                rf'(  - id: {re.escape(entry_id)}.*?)((?=\n  - id:)|$)',
                content,
                re.DOTALL
            )
            if entry_match:
                entry_block = entry_match.group(1)
                if 'notes:' not in entry_block:
                    # Find end of entry to insert notes
                    insert_pattern = rf'(  - id: {re.escape(entry_id)}.*?archived: (?:true|false))'
                    if re.search(insert_pattern, content, re.DOTALL):
                        content = re.sub(
                            insert_pattern,
                            rf'\1\n    notes:\n      - type: file\n        path: "notes/{note_filename}"',
                            content,
                            flags=re.DOTALL,
                            count=1
                        )

    return content, updated_count


def main():
    parser = argparse.ArgumentParser(description='Fetch paper metadata from arXiv and Semantic Scholar')
    parser.add_argument('--limit', type=int, help='Maximum number of papers to process')
    parser.add_argument('--test', action='store_true', help='Test API connectivity only')
    parser.add_argument('--semantic-only', action='store_true', help='Use only Semantic Scholar API')
    parser.add_argument('--arxiv-only', action='store_true', help='Use only arXiv API')
    args = parser.parse_args()

    print("=" * 60)
    print("Paper Metadata Fetcher")
    print("=" * 60)

    if args.test:
        test_apis()
        return

    # Read links.yaml
    print(f"\nReading {LINKS_FILE}...")
    try:
        with open(LINKS_FILE, 'r', encoding='utf-8') as f:
            content = f.read()
    except FileNotFoundError:
        print(f"Error: {LINKS_FILE} not found. Run from link-dumps directory.")
        return

    # Extract entries needing processing
    entries = extract_arxiv_entries(content)
    print(f"Found {len(entries)} arXiv entries without notes")

    if args.limit:
        entries = entries[:args.limit]
        print(f"Processing limited to {len(entries)} entries")

    if not entries:
        print("No entries to process!")
        return

    # Create notes directory
    os.makedirs(NOTES_DIR, exist_ok=True)

    # Process entries
    all_results = {}
    notes_created = {}
    failed_ids = []

    if args.semantic_only:
        # Use Semantic Scholar only
        print("\nUsing Semantic Scholar API only...")
        for i in range(0, len(entries), SEMANTIC_SCHOLAR_BATCH_SIZE):
            batch = entries[i:i+SEMANTIC_SCHOLAR_BATCH_SIZE]
            batch_num = i // SEMANTIC_SCHOLAR_BATCH_SIZE + 1
            total_batches = (len(entries) + SEMANTIC_SCHOLAR_BATCH_SIZE - 1) // SEMANTIC_SCHOLAR_BATCH_SIZE

            print(f"\nBatch {batch_num}/{total_batches}: {len(batch)} papers via Semantic Scholar...")

            arxiv_ids = [e[2] for e in batch]
            results = fetch_semantic_scholar_batch(arxiv_ids)

            print(f"  Retrieved: {len(results)}")

            for entry_id, old_title, arxiv_id in batch:
                arxiv_id_base = re.sub(r'v\d+$', '', arxiv_id)
                if arxiv_id_base in results:
                    all_results[entry_id] = results[arxiv_id_base]
                    note_file = create_note_file(entry_id, arxiv_id, results[arxiv_id_base], NOTES_DIR)
                    if note_file:
                        notes_created[entry_id] = note_file
                else:
                    failed_ids.append(arxiv_id)

            if i + SEMANTIC_SCHOLAR_BATCH_SIZE < len(entries):
                print(f"  Waiting {DELAY_BETWEEN_BATCHES}s...")
                time.sleep(DELAY_BETWEEN_BATCHES)
    else:
        # Primary: arXiv, Fallback: Semantic Scholar
        print("\nUsing arXiv API (primary) with Semantic Scholar fallback...")

        for i in range(0, len(entries), ARXIV_BATCH_SIZE):
            batch = entries[i:i+ARXIV_BATCH_SIZE]
            batch_num = i // ARXIV_BATCH_SIZE + 1
            total_batches = (len(entries) + ARXIV_BATCH_SIZE - 1) // ARXIV_BATCH_SIZE

            print(f"\nBatch {batch_num}/{total_batches}: {len(batch)} papers...")

            arxiv_ids = [e[2] for e in batch]

            # Try arXiv first
            if not args.semantic_only:
                print("  Trying arXiv API...")
                xml_response = fetch_arxiv_batch(arxiv_ids)
                if xml_response:
                    results = parse_arxiv_response(xml_response)
                    print(f"  arXiv returned: {len(results)}")
                else:
                    results = {}
            else:
                results = {}

            # Find missing ones for Semantic Scholar fallback
            missing_ids = []
            for entry_id, old_title, arxiv_id in batch:
                arxiv_id_base = re.sub(r'v\d+$', '', arxiv_id)
                if arxiv_id_base not in results:
                    missing_ids.append(arxiv_id)

            if missing_ids and not args.arxiv_only:
                print(f"  Trying Semantic Scholar for {len(missing_ids)} missing papers...")
                time.sleep(DELAY_BETWEEN_APIS)
                s2_results = fetch_semantic_scholar_batch(missing_ids)
                results.update(s2_results)
                print(f"  S2 returned: {len(s2_results)}")

            # Process results
            for entry_id, old_title, arxiv_id in batch:
                arxiv_id_base = re.sub(r'v\d+$', '', arxiv_id)
                if arxiv_id_base in results:
                    all_results[entry_id] = results[arxiv_id_base]
                    note_file = create_note_file(entry_id, arxiv_id, results[arxiv_id_base], NOTES_DIR)
                    if note_file:
                        notes_created[entry_id] = note_file
                else:
                    failed_ids.append(arxiv_id)

            if i + ARXIV_BATCH_SIZE < len(entries):
                print(f"  Waiting {DELAY_BETWEEN_BATCHES}s...")
                time.sleep(DELAY_BETWEEN_BATCHES)

    # Update links.yaml
    print(f"\nUpdating {LINKS_FILE}...")
    updated_content, update_count = update_links_yaml(content, all_results, notes_created)

    # Backup original
    backup_file = f"{LINKS_FILE}.backup-{datetime.now().strftime('%Y%m%d-%H%M%S')}"
    with open(backup_file, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"  Backed up to {backup_file}")

    # Write updated content
    with open(LINKS_FILE, 'w', encoding='utf-8') as f:
        f.write(updated_content)

    # Summary
    print("\n" + "=" * 60)
    print("SUMMARY")
    print("=" * 60)
    print(f"Entries processed:    {len(entries)}")
    print(f"Metadata retrieved:   {len(all_results)}")
    print(f"Titles updated:       {update_count}")
    print(f"Note files created:   {len(notes_created)}")
    print(f"Failed to retrieve:   {len(failed_ids)}")

    if failed_ids:
        print(f"\nFailed IDs (first 10):")
        for fid in failed_ids[:10]:
            print(f"  - {fid}")

    print(f"\nDone! Notes saved to {NOTES_DIR}/")


if __name__ == '__main__':
    main()
