#!/usr/bin/env python3
"""
Fetch metadata from arXiv API for all arXiv links in the database.
Updates links.yaml with titles, authors, dates, and creates note files with abstracts.
"""

import re
import urllib.request
import urllib.parse
import xml.etree.ElementTree as ET
import time
import os
from datetime import datetime

# Configuration
BATCH_SIZE = 100  # arXiv recommends max 200, we use 100 to be safe
DELAY_BETWEEN_BATCHES = 3  # seconds
LINKS_FILE = 'links.yaml'
NOTES_DIR = 'notes'

def extract_arxiv_ids(content):
    """Extract all arXiv IDs and their entry IDs from links.yaml."""
    pattern = r'  - id: (arxiv-[\d.v]+)\n    title: "([^"]*)"\n    url: "https://arxiv\.org/abs/([\d.v]+)"'
    matches = re.findall(pattern, content)
    return [(m[0], m[1], m[2]) for m in matches]

def fetch_arxiv_batch(arxiv_ids):
    """Fetch metadata for a batch of arXiv IDs."""
    # Clean IDs (remove version numbers for API query)
    clean_ids = [re.sub(r'v\d+$', '', aid) for aid in arxiv_ids]
    id_list = ','.join(clean_ids)

    api_url = f"http://export.arxiv.org/api/query?id_list={id_list}&max_results={len(clean_ids)}"

    headers = {
        'User-Agent': 'Claude-RA-Literature-Review/1.0 (https://github.com/iarwain1/Claude-RA; research tool)'
    }

    req = urllib.request.Request(api_url, headers=headers)

    try:
        with urllib.request.urlopen(req, timeout=60) as response:
            return response.read().decode('utf-8')
    except Exception as e:
        print(f"  Error fetching batch: {e}")
        return None

def parse_arxiv_response(xml_content):
    """Parse arXiv API XML response."""
    results = {}

    try:
        root = ET.fromstring(xml_content)
    except ET.ParseError as e:
        print(f"  XML parse error: {e}")
        return results

    ns = {'atom': 'http://www.w3.org/2005/Atom', 'arxiv': 'http://arxiv.org/schemas/atom'}

    for entry in root.findall('atom:entry', ns):
        # Get arXiv ID
        id_elem = entry.find('atom:id', ns)
        if id_elem is None:
            continue

        arxiv_url = id_elem.text
        arxiv_id = arxiv_url.split('/')[-1]
        # Remove version for matching
        arxiv_id_base = re.sub(r'v\d+$', '', arxiv_id)

        # Get title
        title_elem = entry.find('atom:title', ns)
        title = title_elem.text.strip().replace('\n', ' ').replace('  ', ' ') if title_elem is not None else None

        # Get abstract
        summary_elem = entry.find('atom:summary', ns)
        abstract = summary_elem.text.strip() if summary_elem is not None else None

        # Get authors
        authors = []
        for author in entry.findall('atom:author', ns):
            name_elem = author.find('atom:name', ns)
            if name_elem is not None:
                authors.append(name_elem.text)

        # Get published date
        published_elem = entry.find('atom:published', ns)
        published = published_elem.text[:10] if published_elem is not None else None

        # Get updated date
        updated_elem = entry.find('atom:updated', ns)
        updated = updated_elem.text[:10] if updated_elem is not None else None

        # Get categories
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
            'date_updated': updated,
            'categories': categories
        }

    return results

def create_note_file(entry_id, arxiv_id, data, notes_dir):
    """Create a note file with the paper's abstract."""
    if not data.get('abstract'):
        return None

    filename = f"{entry_id}.md"
    filepath = os.path.join(notes_dir, filename)

    # Skip if file already exists
    if os.path.exists(filepath):
        return None

    authors_str = ', '.join(data['authors'][:5])
    if len(data['authors']) > 5:
        authors_str += f", et al. ({len(data['authors'])} total)"

    content = f"""# {data['title']}

**arXiv:** [{arxiv_id}](https://arxiv.org/abs/{arxiv_id})
**Authors:** {authors_str}
**Date:** {data['date_published']}
**Categories:** {', '.join(data['categories'][:3])}

## Abstract

{data['abstract']}
"""

    with open(filepath, 'w') as f:
        f.write(content)

    return filename

def update_links_yaml(content, updates, notes_created):
    """Update links.yaml with fetched metadata."""
    updated_count = 0

    for entry_id, data in updates.items():
        if not data.get('title'):
            continue

        # Escape title for YAML
        title = data['title'].replace('"', '\\"')

        # Update title
        pattern = rf'(  - id: {re.escape(entry_id)}\n    title: ")[^"]*(")'
        if re.search(pattern, content):
            content = re.sub(pattern, rf'\1{title}\2', content)
            updated_count += 1

        # Add authors if we have them
        if data.get('authors'):
            # Check if authors field already exists
            authors_check = rf'  - id: {re.escape(entry_id)}.*?authors:'
            if not re.search(authors_check, content, re.DOTALL):
                # Add authors after URL
                authors_yaml = '\n'.join([f'      - name: "{a}"' for a in data['authors'][:10]])
                pattern = rf'(  - id: {re.escape(entry_id)}\n    title: "[^"]*"\n    url: "[^"]+")'
                replacement = rf'\1\n    authors:\n{authors_yaml}'
                content = re.sub(pattern, replacement, content)

        # Add date_published if we have it
        if data.get('date_published'):
            # Check if date_published already exists
            date_check = rf'  - id: {re.escape(entry_id)}.*?date_published:'
            if not re.search(date_check, content, re.DOTALL):
                pattern = rf'(  - id: {re.escape(entry_id)}.*?importance: \w+)'
                replacement = rf'\1\n    date_published: "{data["date_published"]}"'
                content = re.sub(pattern, replacement, content, flags=re.DOTALL)

        # Add notes reference if we created a note file
        if entry_id in notes_created:
            notes_check = rf'  - id: {re.escape(entry_id)}.*?notes:'
            if not re.search(notes_check, content, re.DOTALL):
                pattern = rf'(  - id: {re.escape(entry_id)}.*?archived: (?:true|false))'
                replacement = rf'\1\n    notes:\n      - type: file\n        path: "notes/{notes_created[entry_id]}"'
                content = re.sub(pattern, replacement, content, flags=re.DOTALL)

    return content, updated_count

def main():
    print("arXiv Metadata Fetcher")
    print("=" * 50)

    # Read links.yaml
    print(f"\nReading {LINKS_FILE}...")
    with open(LINKS_FILE, 'r') as f:
        content = f.read()

    # Extract arXiv entries
    entries = extract_arxiv_ids(content)
    print(f"Found {len(entries)} arXiv entries")

    # Create notes directory if needed
    os.makedirs(NOTES_DIR, exist_ok=True)

    # Process in batches
    all_results = {}
    notes_created = {}
    failed_ids = []

    for i in range(0, len(entries), BATCH_SIZE):
        batch = entries[i:i+BATCH_SIZE]
        batch_num = i // BATCH_SIZE + 1
        total_batches = (len(entries) + BATCH_SIZE - 1) // BATCH_SIZE

        print(f"\nBatch {batch_num}/{total_batches}: Fetching {len(batch)} papers...")

        arxiv_ids = [e[2] for e in batch]  # Get arXiv IDs
        xml_response = fetch_arxiv_batch(arxiv_ids)

        if xml_response:
            results = parse_arxiv_response(xml_response)
            print(f"  Received metadata for {len(results)} papers")

            # Map results back to entry IDs and create note files
            for entry_id, old_title, arxiv_id in batch:
                arxiv_id_base = re.sub(r'v\d+$', '', arxiv_id)
                if arxiv_id_base in results:
                    all_results[entry_id] = results[arxiv_id_base]

                    # Create note file
                    note_file = create_note_file(entry_id, arxiv_id, results[arxiv_id_base], NOTES_DIR)
                    if note_file:
                        notes_created[entry_id] = note_file
                else:
                    failed_ids.append(arxiv_id)
        else:
            failed_ids.extend([e[2] for e in batch])

        # Rate limiting
        if i + BATCH_SIZE < len(entries):
            print(f"  Waiting {DELAY_BETWEEN_BATCHES}s before next batch...")
            time.sleep(DELAY_BETWEEN_BATCHES)

    # Update links.yaml
    print(f"\nUpdating {LINKS_FILE}...")
    updated_content, update_count = update_links_yaml(content, all_results, notes_created)

    with open(LINKS_FILE, 'w') as f:
        f.write(updated_content)

    # Summary
    print("\n" + "=" * 50)
    print("SUMMARY")
    print("=" * 50)
    print(f"Total arXiv entries: {len(entries)}")
    print(f"Metadata fetched: {len(all_results)}")
    print(f"Titles updated: {update_count}")
    print(f"Note files created: {len(notes_created)}")
    print(f"Failed to fetch: {len(failed_ids)}")

    if failed_ids:
        print(f"\nFailed IDs (first 10): {failed_ids[:10]}")

    print(f"\nDone! Check {NOTES_DIR}/ for new note files.")

if __name__ == '__main__':
    main()
