# Scan Blogs and Newsletters

Scan blog or newsletter archives for relevant papers and references: $ARGUMENTS

This command processes blogs, newsletters, or RSS feeds to find papers and sources relevant to the review.

## Steps

1. Confirm which review you're working on.

2. Identify the source(s):
   - $ARGUMENTS may be a blog URL, RSS feed, or list of blogs
   - If the user has a list in the review folder, read it

3. For each blog/newsletter:
   a. Fetch the main page or archive page
   b. Identify the archive structure (pagination, date-based, categories)
   c. Look for relevant posts based on:
      - Keywords related to the review topic
      - Posts that link to papers
      - Posts with academic references

4. For each relevant post found:
   a. Extract any paper links (arXiv, DOI, PDF links)
   b. Note the context (why the blogger mentioned it)
   c. Extract the blogger's commentary/summary if useful

5. For each paper/source found:
   - Fetch metadata (title, authors, year)
   - Assess relevance to the review
   - Assign priority based on:
     - How strongly the blogger recommended it
     - Relevance to review topic
     - Recency and citation count (if available)

6. Add to `reviews/<review-name>/references.yaml`:
   - Set `source: blog`
   - Note which blog it came from
   - Include blogger's context if relevant

7. Add high-priority items to reading queue

8. Update `subtopics.yaml` if new themes emerge

9. Report to user:
   - Blogs/newsletters scanned: N
   - Relevant posts found: N
   - Papers/references extracted: N
   - Added to references: N
   - New subtopics identified
   - Blogs worth monitoring for future updates

10. Ask user:
    - Any blogs to add to regular monitoring?
    - Should any references be prioritized differently?
    - Are there specific posts to examine more closely?

11. Commit changes

## Blog Types to Handle

- AI/ML research blogs (e.g., distill.pub, lilianweng.github.io)
- Company research blogs (Google AI, OpenAI, Anthropic)
- Newsletter archives (e.g., The Batch, Import AI)
- Academic group blogs
- Personal researcher blogs

## Tips

- Recent posts (last 6-12 months) are usually most relevant
- Pay attention to "best of" or "year in review" posts
- Note if a paper is mentioned by multiple bloggers
- Blogger commentary can help prioritize papers
