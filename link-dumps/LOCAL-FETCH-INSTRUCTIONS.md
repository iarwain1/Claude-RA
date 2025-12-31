# Task: Fetch arXiv Metadata for Link Dumps Database

You need to run a Python script that fetches paper metadata (titles, abstracts, authors) from the arXiv API for a literature review database. The script is already written and located in the repository.

## Prerequisites

1. Make sure you have Python 3.7+ installed
2. No additional packages needed (uses only standard library)

## Steps

### 1. Navigate to the link-dumps directory

```bash
cd /path/to/Claude-RA/link-dumps
```

### 2. Test that the APIs are accessible

```bash
python fetch_metadata_local.py --test
```

You should see output like:
```
Testing API connectivity...
1. Testing arXiv API...
   ✓ arXiv API: Working
2. Testing Semantic Scholar API...
   ✓ Semantic Scholar API: Working
```

### 3. Run the full fetch

This processes ~482 unprocessed papers:

```bash
python fetch_metadata_local.py
```

This will take approximately 30 minutes due to rate limiting (3 sec delay between batches of 50).

**Alternative - process in smaller batches:**
```bash
python fetch_metadata_local.py --limit 100
```

## What the Script Does

- Reads `links.yaml` to find arXiv entries without notes
- Fetches metadata from arXiv API (primary) with Semantic Scholar as fallback
- Creates markdown note files in `notes/` directory with abstracts
- Updates `links.yaml` with proper titles and publication dates
- Creates a backup file before modifying anything

## Expected Output

When complete, you'll see a summary like:
```
SUMMARY
============================================================
Entries processed:    482
Metadata retrieved:   470
Titles updated:       470
Note files created:   465
Failed to retrieve:   12
```

## After Running

### 1. Verify the results

```bash
ls -la notes/ | tail -20
cat notes/arxiv-2312.06942.md  # Check a sample note
```

### 2. Commit and push the changes

```bash
git add links.yaml notes/
git commit -m "Add: Batch processed arXiv metadata for ~470 papers"
git push origin main
```

## Troubleshooting

| Problem | Solution |
|---------|----------|
| arXiv API fails | Use `--semantic-only` flag to use Semantic Scholar instead |
| Rate limited | Increase `DELAY_BETWEEN_BATCHES` in the script (default: 3 seconds) |
| Need to restore | `cp links.yaml.backup-YYYYMMDD-HHMMSS links.yaml` |
| Partial run | Re-running the script skips already-processed entries |
