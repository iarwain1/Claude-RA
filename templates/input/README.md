# Input Materials

Place your starting materials for this literature review here:

## Suggested Organization

```
input/
├── project_description.md    # What you're trying to research
├── outline.md                # Any preliminary outline or structure
├── link_dumps/               # Files with collected URLs/hyperlinks
│   ├── bookmarks.md
│   ├── reading_list.docx
│   └── ...
└── notes/                    # Your existing notes on the topic
    ├── ideas.md
    ├── background.docx
    └── ...
```

## Supported Formats

- **Markdown** (.md) - Preferred, fully readable
- **Word documents** (.doc, .docx) - Claude can read these
- **Plain text** (.txt) - Fully readable
- **PDFs** (.pdf) - Claude can read these

## What Claude Will Do

When you start your review, ask Claude to:

1. **Read your project description** to understand the topic
2. **Process your link dumps** with `/process-sources input/link_dumps/`
3. **Scan your notes** with `/scan-notes input/notes/`

Claude will:
- Extract relevant URLs from your link dumps
- Note which links were bolded/highlighted as promising
- Pull references and context from your existing notes
- Use your outline to guide subtopic organization

## Tips

- **Don't worry about relevance** - Claude will filter for what's relevant
- **Keep original formatting** - Bold/highlights help indicate priority
- **Include context** - Any notes around links help Claude understand why you saved them
