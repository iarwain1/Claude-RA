# Process Source List

Process a file or list of URLs to find relevant references: $ARGUMENTS

This command handles the user's collected links - URLs gathered over time that may be relevant to the review.

## Steps

1. Confirm which review you're working on.

2. Identify the source:
   - If $ARGUMENTS is a file path, read the file
   - If $ARGUMENTS is a URL to a bookmarks file, fetch it
   - If the user provides URLs directly, use those

3. Parse the input to extract URLs:
   - Handle markdown links: `[text](url)`
   - Handle plain URLs
   - Handle HTML bookmarks exports
   - Handle bullet lists with URLs

4. For each URL found (process in batches of 5-10):
   a. Fetch the URL using WebFetch
   b. Determine if it's relevant to the review topic
   c. If relevant:
      - Extract: title, authors (if paper), date, key points
      - Assess relevance and assign priority (1-10)
      - Identify potential subtopics
   d. If not relevant, note why and skip

5. Add relevant references to `<review-name>/References/references.yaml`
   - Set `source: user-provided`
   - Include where the link came from (if known)

6. Add high-priority items (7+) to reading queue

7. Report to user:
   - Total URLs processed: N
   - Relevant: N (added to references)
   - Not relevant: N (with brief reasons)
   - High priority items added to queue: N
   - Detected themes/subtopics
   - Any URLs that couldn't be accessed

8. Ask user:
   - Should any be re-prioritized?
   - Are there other source files to process?
   - Should we search for related papers?

9. Commit changes with message "Process source list: <filename or count> URLs"

## Tips

- Process URLs in batches to avoid overwhelming
- Group related URLs together when reporting
- Note duplicates (same paper from different sources)
- Flag particularly promising finds
