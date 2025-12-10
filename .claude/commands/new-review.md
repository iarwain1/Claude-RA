# Create New Literature Review

Create a new literature review project named "$ARGUMENTS".

## Steps

1. Create the directory structure at `reviews/$ARGUMENTS/`:
   - Copy `templates/references.yaml` to `reviews/$ARGUMENTS/references.yaml`
   - Copy `templates/reading-queue.yaml` to `reviews/$ARGUMENTS/reading-queue.yaml`
   - Copy `templates/subtopics.yaml` to `reviews/$ARGUMENTS/subtopics.yaml`
   - Copy `templates/notes/questions.md` to `reviews/$ARGUMENTS/notes/questions.md`
   - Copy `templates/input/README.md` to `reviews/$ARGUMENTS/input/README.md`
   - Create `reviews/$ARGUMENTS/notes/paper-summaries/.gitkeep`
   - Create `reviews/$ARGUMENTS/notes/themes/.gitkeep`
   - Create `reviews/$ARGUMENTS/reports/.gitkeep`
   - Create `reviews/$ARGUMENTS/input/link_dumps/.gitkeep`
   - Create `reviews/$ARGUMENTS/input/notes/.gitkeep`

2. Update the metadata in each YAML file:
   - Set `review_name` to "$ARGUMENTS"
   - Set `created` and `last_updated` to today's date

3. Check if the user has already placed input materials in the review folder:
   - Look for project_description.md, outline.md, or similar
   - Check for link_dumps/ or notes/ folders with content
   - If found, acknowledge them

4. Ask the user:
   - What is the main topic/research question for this review?
   - Do you have input materials to add to `input/`? (project description, link dumps, notes)
   - What subtopics do you expect to explore?

5. If the user provides a project description or has one in input/:
   - Read it to understand the topic
   - Extract initial research questions for `notes/questions.md`
   - Suggest initial subtopics based on the description

6. Update `references.yaml` with the topic

7. Create an initial commit for the new review

8. Report what was created and suggest next steps:
   - "Add your input materials to `reviews/$ARGUMENTS/input/`"
   - "Then run `/process-sources input/link_dumps/` to extract relevant links"
   - "And `/scan-notes input/notes/` to find references in your notes"
   - "Or `/search <topic>` to start finding papers"
