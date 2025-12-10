# Find Citing Papers

Find papers that cite a given reference: $ARGUMENTS

This command helps follow citation trails by finding papers that cite an important work.

## Steps

1. Confirm which review you're working on.

2. Identify the target paper:
   - $ARGUMENTS may be a reference key, title, DOI, or arXiv ID
   - Look up in `references.yaml` if it's a key
   - If not found, search for it

3. Search for citing papers:
   - Use WebSearch: `"<paper title>" cited by`
   - Use WebSearch: `site:semanticscholar.org "<paper title>" citations`
   - Use WebSearch: `site:scholar.google.com cites:<identifier>`
   - Look for "Cited by N" links on paper pages

4. For papers found that cite the target:
   - Extract metadata (title, authors, year, URL)
   - Assess relevance to the review
   - Check if already in collection (avoid duplicates)
   - Note why it cited the target paper (if apparent)

5. Prioritize based on:
   - Relevance to review topic
   - Recency (more recent often more relevant)
   - Citation count of the citing paper
   - Whether it's a survey/review (often good for context)

6. Add new relevant papers to `references.yaml`:
   - Note the citation relationship
   - Set `source: citation-trail`

7. Add high-priority items to reading queue with reason

8. Report to user:
   - Target paper: <title>
   - Papers found citing it: N
   - Relevant to review: N
   - Already in collection: N
   - Added new references: N
   - Notable citing papers (brief descriptions)

9. Ask user:
   - Should any be prioritized for reading?
   - Are there other key papers to trace citations from?
   - Should we also find what the target paper cites?

10. Commit changes

## Finding What a Paper Cites

If the user asks to find papers cited BY a reference (rather than papers citing it):
1. Fetch the paper's reference section
2. Extract citations from the Related Work section
3. Prioritize based on how prominently they're discussed
4. Note the context of each citation

## Tips

- Highly-cited papers often have hundreds of citers - focus on most relevant
- Recent citers may have built on or extended the work
- Survey papers citing the target often provide good context
- Papers that cite multiple references in your collection are likely relevant
