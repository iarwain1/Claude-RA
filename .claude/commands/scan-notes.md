# Scan Notes Folder

Scan a local notes folder (e.g., Obsidian vault) for relevant references and insights: $ARGUMENTS

This command processes the user's existing notes and documents to extract references and context relevant to the review.

## Steps

1. Confirm which review you're working on.

2. Identify the notes folder:
   - $ARGUMENTS should be a path to the notes folder
   - Common structures: Obsidian vault, markdown folder, mixed documents

3. Scan the folder structure:
   - Use Glob to find all markdown files (*.md)
   - Also look for: *.txt, *.pdf (note: PDFs need user upload)
   - Note the folder organization (may indicate topics)

4. For each file, extract:
   a. **References/Links**:
      - URLs to papers (arXiv, DOI links, etc.)
      - Citations in text (e.g., "Smith et al. 2024")
      - Bibliography sections

   b. **Context**:
      - What topic is the note about?
      - User's comments about papers/sources
      - Questions or areas of interest

   c. **Connections** (especially for Obsidian):
      - [[wikilinks]] between notes
      - Tags (#topic)
      - Folder structure

5. Assess relevance to the review:
   - Match note topics to review topic
   - Prioritize notes with many relevant references
   - Note user's existing insights on the topic

6. For each relevant reference found:
   - Fetch metadata if URL available
   - Use context from notes to assess priority
   - Note the user's existing thoughts

7. Add to `<review-name>/References/references.yaml`:
   - Set `source: user-provided`
   - Include path to source note
   - Include user's context/commentary

8. Identify themes from the notes:
   - Map to existing subtopics
   - Suggest new subtopics based on note organization
   - Note areas where user already has substantial notes

9. Optionally, create links back:
   - Note which review papers connect to which user notes
   - This helps integrate new reading with existing knowledge

10. Report to user:
    - Files scanned: N
    - Relevant to review: N
    - References extracted: N
    - New references (not already in collection): N
    - Themes/subtopics identified
    - User's existing insights on the topic
    - Suggested connections to existing notes

11. Ask user:
    - Should any notes be incorporated directly?
    - Are there specific folders to focus on?
    - Any references to prioritize based on existing notes?

12. Commit changes

## Handling Different Note Formats

### Obsidian Vaults
- Respect .obsidian folder (don't scan)
- Parse [[wikilinks]] for connections
- Use tags and folder structure for topics
- Look for dataview queries that might list papers

### Plain Markdown
- Look for YAML frontmatter
- Parse standard markdown links
- Check for bibliography sections

### Mixed Folders
- Identify file types
- Skip binary files
- Ask user about PDFs (need upload)

## Tips

- The user's own notes often contain valuable context
- Note organization reflects how the user thinks about topics
- Existing annotations/highlights indicate priority
- Questions in notes suggest areas to explore
