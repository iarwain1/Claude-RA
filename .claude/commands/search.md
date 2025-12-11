# Search for Papers

Search for academic papers related to: "$ARGUMENTS"

## Steps

1. First, confirm which review you're working on. Check for recent context or ask the user.

2. Use WebSearch to find relevant papers:
   - Search: `site:arxiv.org $ARGUMENTS`
   - Search: `$ARGUMENTS research paper 2023..2025`
   - Search: `$ARGUMENTS survey OR review`

3. For each relevant result found (aim for 5-10):
   - Extract: title, authors, year, URL, abstract snippet
   - Assess relevance and assign priority (1-10)
   - Identify potential subtopics

4. Add new references to `<review-name>/References/references.yaml`

5. Add high-priority papers (7+) to `<review-name>/References/reading-queue.yaml`

6. Report findings to user:
   - List papers found with brief descriptions
   - Highlight most promising ones
   - Suggest related searches
   - Ask if any should be prioritized differently

7. Commit changes with message "Add papers from search: $ARGUMENTS"
