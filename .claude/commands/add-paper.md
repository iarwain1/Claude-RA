# Add Paper from URL

Add a paper to the current literature review from: $ARGUMENTS

## Steps

1. Confirm which review you're working on.

2. Fetch the URL using WebFetch to extract:
   - Title
   - Authors
   - Year/date
   - Abstract or summary
   - DOI if available

3. Generate a reference key (format: `firstauthor2024keyword`)

4. Determine the source type:
   - arxiv.org → source: arxiv
   - semanticscholar.org → source: semantic-scholar
   - Blog/newsletter → source: blog
   - Other → source: web

5. Ask the user:
   - What priority (1-10) should this paper have?
   - What subtopics does it relate to?
   - Should it be added to the reading queue?

6. Add to `<review-name>/References/references.yaml`

7. If priority >= 6, add to `<review-name>/References/reading-queue.yaml`

8. Commit with message "Add reference: <title>"

9. Report success and offer to:
   - Search for related papers
   - Read and summarize the paper now
   - Add more papers
