# Literature Review Agent

An AI-powered research assistant for conducting systematic literature reviews. Use **Claude Code** directly as your research assistant, with all your data stored in version-controlled files.

## How It Works

This repo turns Claude Code into a literature review agent through:
- **CLAUDE.md** - Instructions that guide Claude's behavior as a research assistant
- **Slash commands** - Quick workflows like `/search`, `/summarize`, `/status`
- **Skills** - Detailed methodologies for systematic reviews, paper analysis, and citations
- **Structured data files** - YAML files for references, notes, and organization
- **Git versioning** - Full history of your research progress

```
┌─────────────────────────────────────────────────────────────┐
│                    Claude Code                               │
│              (Your Claude Max subscription)                  │
├─────────────────────────────────────────────────────────────┤
│  Built-in Tools:                                            │
│  • WebSearch - Find papers on arXiv, Google Scholar         │
│  • WebFetch - Read paper abstracts and blog posts           │
│  • Read/Edit/Write - Manage your research files             │
│  • Git - Track changes and sync progress                    │
└─────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────┐
│              This Repository                                 │
│  ├── CLAUDE.md              # Agent instructions            │
│  ├── .claude/commands/      # Slash commands                │
│  ├── .claude/skills/        # Research methodologies        │
│  ├── Templates/             # Templates for new reviews     │
│  └── <Your-Review>/         # Your literature reviews       │
│      ├── User-Input/        # YOUR starting materials       │
│      ├── References/        # Processed reference data      │
│      ├── Claude-Notes/      # Notes Claude creates          │
│      ├── Drafts/            # Draft sections                │
│      └── Status-Reports/    # Progress tracking             │
└─────────────────────────────────────────────────────────────┘
```

## Quick Start

### 1. Clone and Open in Claude Code

```bash
git clone https://github.com/yourusername/Claude-RA.git
cd Claude-RA
```

Open this folder in Claude Code (web, desktop, or CLI).

### 2. Create a New Literature Review

```
/new-review my-research-topic
```

Claude will create a new review directory with all the necessary files.

### 3. Start Researching

```
/search transformer attention mechanisms 2024

/add-paper https://arxiv.org/abs/2401.12345

/status

/read-next

/synthesize
```

Or just chat naturally:
> "Find recent papers on LLM agents and add the most relevant ones to my collection"

## Starting with Your Own Materials

If you have existing materials (project descriptions, collected links, notes), here's how to use them:

### 1. Create the review and add your files

```
/new-review my-topic
```

Then copy your files into the `User-Input/` folder:

```
my-topic/User-Input/
├── project_description.md      # What you're researching
├── outline.md                  # Any preliminary structure
├── References/                 # PDFs, papers to process
│   ├── important-paper.pdf
│   └── ...
├── Notes/                      # Your existing notes
│   ├── background.md
│   └── ...
└── Link Dumps/                 # Your collected URLs (optional)
    ├── bookmarks.md
    └── reading_list.docx
```

### 2. Process your materials

```
# Have Claude read your project description
"Read my project description in User-Input/ and set up the review"

# Process your collected links
/process-sources User-Input/References/

# Scan your notes for references
/scan-notes User-Input/Notes/
```

Claude will:
- Extract relevant URLs from your link dumps
- Note bolded/highlighted links as higher priority
- Pull references and context from your notes
- Filter for what's relevant to this review

### 3. Continue with normal workflow

After processing your inputs, continue with `/search`, `/read-next`, etc.

## Adding New Materials Mid-Review

When you have new materials to add during an ongoing review:

1. **Drop files** into `User-Input/References/` or `User-Input/Notes/`

2. **Create `User-Input/NEW.md`** to tell Claude what to process:
   ```markdown
   # New Materials - Dec 11, 2025

   ## To Process
   - [ ] References/new-paper.pdf - high priority, summarize
   - [ ] Notes/meeting-notes.md - extract any citations

   ## Instructions
   Focus on methodology sections. Priority: high.
   ```

3. **Tell Claude** "check for new input" - it will process items, check them off, and delete NEW.md when done

## Providing Feedback on Claude's Work

Three options for commenting on drafts or notes:

### Option A: Inline HTML Comments
```markdown
This claim needs stronger evidence. <!-- FEEDBACK: Add 2-3 more citations -->
```

### Option B: FEEDBACK.md File
Create `<Review>/FEEDBACK.md`:
```markdown
# Feedback - Dec 11

## Drafts/section-1.md
- Line 45: Too technical, simplify
- Missing: transition paragraph

## Claude-Notes/Paper-Summaries/smith2024.md
- Add limitations section
```

### Option C: Direct Conversation
Just tell Claude what to change.

## Slash Commands

### Setup & Status
| Command | Description |
|---------|-------------|
| `/new-review <name>` | Create a new literature review |
| `/status` | Show review progress and statistics |

### Gathering Sources
| Command | Description |
|---------|-------------|
| `/search <query>` | Search academic databases for papers |
| `/add-paper <url>` | Add a single paper from URL |
| `/process-sources <file>` | Batch process a file of URLs you've collected |
| `/scan-blogs <url>` | Scan blog/newsletter archives for papers |
| `/scan-notes <folder>` | Scan Obsidian vault or notes folder |
| `/find-citing <paper>` | Find papers that cite a reference |

### Reading & Analysis
| Command | Description |
|---------|-------------|
| `/read-next` | Read and summarize the next paper in queue |
| `/summarize <key>` | Summarize a specific paper |
| `/organize` | Organize references by subtopics |

### Output
| Command | Description |
|---------|-------------|
| `/synthesize` | Generate literature review report |
| `/export-bib` | Export references as BibTeX |

### Link Database
| Command | Description |
|---------|-------------|
| `/add-links` | Add new links to cross-project database |
| `/search-links <query>` | Search/filter link database by text, tags, importance |

## Skills

Skills provide detailed methodologies that Claude uses automatically when relevant.

| Skill | Description |
|-------|-------------|
| `systematic-review` | 7-phase PRISMA-based methodology for rigorous literature reviews |
| `paper-analysis` | Critical evaluation framework with bias detection and quality rating |
| `citation-helper` | BibTeX formatting, citation styles, and reference validation |
| `large-file-handling` | Strategies for processing files that exceed context limits (PDFs, documents, etc.) |

These skills are invoked automatically:
- Starting a review → `systematic-review` guides planning
- Reading papers → `paper-analysis` ensures thorough evaluation
- Exporting citations → `citation-helper` ensures proper formatting
- Large files (>100K tokens) → `large-file-handling` provides chunking and targeted extraction

## Repository Structure

```
Claude-RA/
├── CLAUDE.md                    # Agent instructions
├── README.md                    # This file
├── .gitignore
├── LICENSE
│
├── .claude/
│   ├── commands/                # Slash commands
│   │   ├── new-review.md
│   │   ├── search.md
│   │   ├── add-paper.md
│   │   ├── add-links.md         # Add links to database
│   │   ├── search-links.md      # Search link database
│   │   ├── process-sources.md
│   │   ├── scan-blogs.md
│   │   ├── scan-notes.md
│   │   ├── find-citing.md
│   │   ├── read-next.md
│   │   ├── summarize.md
│   │   ├── status.md
│   │   ├── organize.md
│   │   ├── synthesize.md
│   │   └── export-bib.md
│   └── skills/                  # Research methodologies
│       ├── systematic-review/
│       ├── paper-analysis/
│       ├── citation-helper/
│       └── large-file-handling/
│
├── link-dumps/                  # Cross-project link database
│   ├── links.yaml               # Main link database (618 entries)
│   ├── tags.yaml                # Hierarchical tag taxonomy
│   ├── CHANGELOG.md             # Database change history
│   ├── research-notes.md        # Tag system design docs
│   ├── figures/                 # Key figures from links
│   ├── notes/                   # Detailed notes
│   └── *.docx                   # Original source files
│
├── Templates/                   # Templates for new reviews
│   ├── User-Input/
│   ├── References/
│   ├── Claude-Notes/
│   ├── Drafts/
│   └── Status-Reports/
│
├── Example-Review/              # Example review
│   ├── User-Input/              # Your starting materials
│   │   ├── References/
│   │   └── Notes/
│   ├── References/              # Processed reference data
│   │   ├── references.yaml
│   │   ├── reading-queue.yaml
│   │   └── subtopics.yaml
│   ├── Claude-Notes/            # Notes Claude creates
│   │   ├── Paper-Summaries/
│   │   ├── Themes/
│   │   └── questions.md
│   ├── Drafts/                  # Draft sections and reports
│   └── Status-Reports/          # Progress tracking
│
└── <Your-Review>/               # Your reviews at root level
```

## Review Data Files

### References/references.yaml
```yaml
references:
  - key: smith2024transformers
    title: "Transformers for Scientific Discovery"
    authors: ["Smith, J.", "Doe, A."]
    year: 2024
    url: "https://arxiv.org/abs/2401.12345"
    priority: 8          # 1-10, higher = more important
    subtopics: ["transformers", "scientific-ml"]
    read: false
    notes_file: null
```

### References/reading-queue.yaml
```yaml
queue:
  - key: smith2024transformers
    priority: 8
    reason: "Highly cited, directly relevant"
    status: pending      # pending, in-progress, done, skipped
```

### References/subtopics.yaml
```yaml
subtopics:
  - name: transformers
    description: "Transformer architectures"
    key_findings:
      - "Finding 1"
    open_questions:
      - "Question 1"
    reference_keys: ["smith2024transformers"]
```

## Workflow

### 1. Gather Sources
- `/search` - Find papers on arXiv, Google Scholar
- `/add-paper` - Add specific papers by URL
- `/process-sources` - Batch process your collected URL lists
- `/scan-blogs` - Extract papers from blog/newsletter archives
- `/scan-notes` - Find references in your Obsidian vault
- `/find-citing` - Follow citation trails from key papers

### 2. Organize
- `/organize` - Group references by theme
- Claude identifies subtopics and tags papers
- Update priorities based on relevance

### 3. Read & Note
- `/read-next` - Read papers from queue (highest priority first)
- Claude creates structured notes in `Claude-Notes/Paper-Summaries/`
- Uses `paper-analysis` skill for critical evaluation
- Discovers new papers to add from Related Work sections

### 4. Synthesize
- `/synthesize` - Generate the literature review report
- `/export-bib` - Export citations
- Iterate: go back to gathering if gaps are found

## Security Note

This approach is more secure than MCP-based alternatives because:
- **Sandboxed**: Claude only accesses files in this repo
- **No external APIs**: Uses Claude's built-in web search (no API keys)
- **Version controlled**: All changes tracked in git
- **Limited exfiltration**: Can only push to your own GitHub repo

## Link Dumps Database

The `link-dumps/` directory is a cross-project database for collecting and organizing links that can be used across all literature reviews.

### Why a Separate Database?

- **Cross-project access**: Links collected for one review may be useful for others
- **Persistent collection**: Keep collecting links even when not actively reviewing
- **Rich metadata**: More fields than review-specific references.yaml
- **Hierarchical tags**: Flexible categorization with polyhierarchy support

### Quick Usage

**Add new links:**
```
/add-links

https://arxiv.org/abs/2412.12345 - Important paper on X
https://anthropic.com/research/new - High priority

Notes: First one relates to alignment
```

**Search links:**
```
/search-links alignment                    # Text search
/search-links #ai-safety #paper            # By tags
/search-links importance:high              # By importance
```

### Database Files

| File | Description |
|------|-------------|
| `links.yaml` | Main database with 618 entries |
| `tags.yaml` | Hierarchical tag taxonomy (80+ tags, 3 facets) |
| `CHANGELOG.md` | All database changes |
| `research-notes.md` | Tag system design decisions |

### Tag Facets

1. **Domain**: ai-safety, evaluations, agents, governance, economics, etc.
2. **Content Type**: paper, blog-post, tool, dataset, tutorial, etc.
3. **Source**: arxiv, github, anthropic, openai, lesswrong, etc.

See `CLAUDE.md` for full documentation of the link-dumps system.

## Tips

1. **Commit often** - Use git to track progress
2. **Be specific** - "Search arXiv for attention mechanisms in vision transformers 2024" > "find AI papers"
3. **Iterate** - Start broad, then drill into subtopics
4. **Follow citations** - Ask Claude to find papers citing important works
5. **Check progress** - Use `/status` regularly
6. **Use NEW.md** - When adding materials mid-review, create NEW.md so Claude knows what's new
7. **Use the link database** - Search `/search-links` before starting a new review to find existing relevant links

## License

MIT License - see LICENSE file for details.
