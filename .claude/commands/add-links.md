# Add Links to Database

Process new links and add them to the link-dumps database.

## Input

The user provides links in one of these formats:
1. **Direct text** - URLs/hyperlinks pasted into chat, optionally with notes
2. **File** - A file path containing links (txt, md, doc, docx, pdf)
3. **Multiple items** - Mix of URLs and notes/comments

## Process

For each link provided:

1. **Extract URL** - Get the canonical URL
2. **Fetch metadata** - Use WebFetch to get:
   - Title
   - Authors (if available)
   - Publication date
   - Abstract/description
3. **Assign tags** - Based on content, assign appropriate tags from `link-dumps/tags.yaml`:
   - Domain tags (ai-safety, evaluations, agents, etc.)
   - Content type tags (paper, blog-post, tool, etc.)
   - Source tags (arxiv, github, substack, etc.)
4. **Set importance** - Default to `normal`, adjust if user specifies
5. **Generate ID** - Create unique ID (arxiv-XXXX.XXXXX or domain-hash)
6. **Add to database** - Append to `link-dumps/links.yaml`

## Output

After processing:
1. Report number of links added
2. List any links that couldn't be processed (with reasons)
3. Show tags assigned to each link
4. Update `link-dumps/CHANGELOG.md` with summary

## Example Usage

```
/add-links

Here are some new links:

https://arxiv.org/abs/2412.12345 - Important paper on alignment
https://www.anthropic.com/news/new-research - Check this one
[This blog post](https://example.com/post) has good analysis

Notes:
- The arxiv paper should be high priority
- Tag the anthropic one with "interpretability"
```

## Handling User Notes

When the user includes notes/comments with links:
- Parse inline notes (after URL or in brackets)
- Store in the `notes` field as inline content
- Use notes to inform tag selection and importance
