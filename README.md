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
│  ├── templates/             # Templates for new reviews     │
│  └── reviews/               # Your literature reviews       │
│      └── <your-review>/                                     │
│          ├── references.yaml                                │
│          ├── reading-queue.yaml                             │
│          ├── subtopics.yaml                                 │
│          └── notes/                                         │
└─────────────────────────────────────────────────────────────┘
```

## Quick Start

### 1. Clone and Open in Claude Code

```bash
git clone https://github.com/yourusername/Claude-Literature-Review-Agent.git
cd Claude-Literature-Review-Agent
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

## Skills

Skills provide detailed methodologies that Claude uses automatically when relevant. They're adapted from [K-Dense-AI/claude-scientific-writer](https://github.com/K-Dense-AI/claude-scientific-writer) (MIT License).

| Skill | Description |
|-------|-------------|
| `systematic-review` | 7-phase PRISMA-based methodology for rigorous literature reviews |
| `paper-analysis` | Critical evaluation framework with bias detection and quality rating |
| `citation-helper` | BibTeX formatting, citation styles, and reference validation |

These skills are invoked automatically:
- Starting a review → `systematic-review` guides planning
- Reading papers → `paper-analysis` ensures thorough evaluation
- Exporting citations → `citation-helper` ensures proper formatting

## Repository Structure

```
Claude-Literature-Review-Agent/
├── CLAUDE.md                    # Agent instructions
├── README.md                    # This file
├── .gitignore
├── LICENSE
│
├── .claude/
│   ├── commands/                # Slash commands
│   │   ├── new-review.md        # Create new review
│   │   ├── search.md            # Search databases
│   │   ├── add-paper.md         # Add single paper
│   │   ├── process-sources.md   # Batch process URLs
│   │   ├── scan-blogs.md        # Scan blog archives
│   │   ├── scan-notes.md        # Scan notes folders
│   │   ├── find-citing.md       # Citation chaining
│   │   ├── read-next.md         # Read next paper
│   │   ├── summarize.md         # Summarize paper
│   │   ├── status.md            # Review status
│   │   ├── organize.md          # Organize by subtopic
│   │   ├── synthesize.md        # Generate report
│   │   └── export-bib.md        # Export BibTeX
│   └── skills/                  # Research methodologies
│       ├── systematic-review/
│       ├── paper-analysis/
│       └── citation-helper/
│
├── templates/                   # Templates for new reviews
│   ├── references.yaml
│   ├── reading-queue.yaml
│   ├── subtopics.yaml
│   └── notes/
│       └── questions.md
│
├── reviews/                     # Individual literature reviews
│   └── example/                 # Example review (see below)
│       ├── references.yaml
│       ├── reading-queue.yaml
│       ├── subtopics.yaml
│       ├── notes/
│       │   ├── paper-summaries/
│       │   ├── themes/
│       │   └── questions.md
│       └── reports/
│
├── resources/                   # Shared resources
│
└── custom-agent/                # Standalone Python agent (alternative)
    ├── pyproject.toml
    ├── src/
    └── ...
```

## Review Data Files

### references.yaml
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

### reading-queue.yaml
```yaml
queue:
  - key: smith2024transformers
    priority: 8
    reason: "Highly cited, directly relevant"
    status: pending      # pending, in-progress, done, skipped
```

### subtopics.yaml
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

## Example Review

See `reviews/example/` for a complete example of a literature review on "LLM Agents" with:
- 3 references (2 read, 1 in queue)
- 4 subtopics
- Paper summaries in `notes/paper-summaries/`
- Theme notes in `notes/themes/`

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
- Claude creates structured notes in `notes/paper-summaries/`
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

See the [security discussion](https://simonwillison.net/2025/Jun/16/the-lethal-trifecta/) for more on AI agent security.

## Alternative: Standalone Python Agent

If you prefer a standalone CLI application with direct API access to arXiv and Semantic Scholar, see the `custom-agent/` directory. This requires:
- Python 3.10+
- Anthropic API key
- Installation: `pip install -e custom-agent/`

## Tips

1. **Commit often** - Use git to track progress
2. **Be specific** - "Search arXiv for attention mechanisms in vision transformers 2024" > "find AI papers"
3. **Iterate** - Start broad, then drill into subtopics
4. **Follow citations** - Ask Claude to find papers citing important works
5. **Check progress** - Use `/status` regularly

## License

MIT License - see LICENSE file for details.
