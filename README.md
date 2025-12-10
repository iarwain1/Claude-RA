# Literature Review Agent

An AI-powered research assistant for conducting comprehensive literature reviews, built on the **Claude Agent SDK**. This agent acts as your personal Research Assistant, autonomously handling research tasks while communicating with you throughout the process.

## Built on Claude Agent SDK

This project demonstrates how to build a sophisticated research agent using the Claude Agent SDK. The agent uses **custom MCP tools** to:

- Search academic databases (arXiv, Semantic Scholar)
- Process bookmarks, blogs, and local files
- Manage references with intelligent deduplication
- Take structured research notes
- Generate reports and exports

The SDK's agentic loop handles tool selection and execution, allowing the agent to autonomously decide which tools to use based on your requests.

## Features

### Reference Gathering
- **Academic Search**: Automated searches on arXiv and Semantic Scholar
- **URL Processing**: Extract and follow links from bookmarks and markdown files
- **Blog/Newsletter Scanning**: Crawl RSS feeds and extract paper links
- **Local File Processing**: Parse Obsidian vaults, PDFs, and note collections
- **Citation Following**: Discover new references through citation trails

### Intelligent Organization
- **AI-Powered Prioritization**: Claude evaluates relevance and sets priorities
- **Subtopic Discovery**: Automatically identifies themes in the literature
- **Smart Deduplication**: Recognizes duplicates across sources
- **Reading Queue**: Prioritized list of papers to read

### Analysis & Note-Taking
- **Document Reading**: Full-text extraction from PDFs and web pages
- **Automated Notes**: Generate structured notes with key findings
- **Quote Capture**: Save important quotes with context
- **Connection Discovery**: Identify links between papers

### Synthesis & Reporting
- **Progress Reports**: Real-time statistics and status
- **Subtopic Summaries**: AI-generated summaries for each area
- **Export Formats**: Markdown and BibTeX

## Installation

### Prerequisites
- Python 3.10 or higher
- Anthropic API key

### Setup

```bash
# Clone the repository
git clone https://github.com/yourusername/Claude-Literature-Review-Agent.git
cd Claude-Literature-Review-Agent

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install the package
pip install -e .

# Set up your API key
cp .env.example .env
# Edit .env and add your ANTHROPIC_API_KEY
```

## Quick Start

### Interactive Mode (Recommended)

```bash
lit-review interactive
```

This launches an interactive session where you can chat with the agent:

```
You: Search arXiv for papers on LLM agents published in 2024
  [Using: search_arxiv]

Found 20 papers on arXiv:
- Agents: An Open-source Framework for Autonomous Language Agents
  Park et al. (2024)
  arXiv: 2309.07870
  ...

Added 18 new references to collection.

You: Show me the reading queue
  [Using: get_reading_queue]

Reading queue (5 papers):
1. [HIGH] A Survey on Large Language Model based Autonomous Agents
   ID: abc123 | Wang et al.
...
```

### Single Query Mode

```bash
# Send a single query
lit-review query "Search Semantic Scholar for transformer architecture papers"

# Gather references on a topic
lit-review gather "Large Language Model Agents"

# Generate a report
lit-review report
```

### CLI Commands

```bash
lit-review interactive    # Interactive chat mode
lit-review query "..."    # Single query
lit-review gather "..."   # Gather references on topic
lit-review organize       # Organize and prioritize
lit-review read -n 5      # Read top 5 papers from queue
lit-review report         # Generate report
lit-review status         # Show statistics
```

## Architecture

The agent is built using the Claude Agent SDK with custom MCP tools:

```
┌─────────────────────────────────────────────────────┐
│                   Claude Agent SDK                   │
│  ┌─────────────────────────────────────────────┐   │
│  │              Agent Loop                      │   │
│  │  (Tool selection, execution, reasoning)      │   │
│  └─────────────────────────────────────────────┘   │
│                        │                            │
│  ┌─────────────────────┴───────────────────────┐   │
│  │           Custom MCP Tools                   │   │
│  ├──────────────────┬──────────────────────────┤   │
│  │ Reference Tools  │ Search Tools             │   │
│  │ - add_reference  │ - search_arxiv           │   │
│  │ - search_refs    │ - search_semantic_scholar│   │
│  │ - update_priority│ - get_paper_citations    │   │
│  │ - get_queue      │ - get_recommendations    │   │
│  ├──────────────────┼──────────────────────────┤   │
│  │ Note Tools       │ Source Tools             │   │
│  │ - create_note    │ - process_url_file       │   │
│  │ - search_notes   │ - process_blog_feed      │   │
│  │ - get_findings   │ - scan_local_folder      │   │
│  ├──────────────────┼──────────────────────────┤   │
│  │ Subtopic Tools   │ Report Tools             │   │
│  │ - create_subtopic│ - generate_progress      │   │
│  │ - add_finding    │ - export_bibtex          │   │
│  │ - set_summary    │ - export_markdown        │   │
│  └──────────────────┴──────────────────────────┘   │
└─────────────────────────────────────────────────────┘
                         │
┌────────────────────────┴────────────────────────────┐
│                   Data Layer                         │
│  ┌─────────────┐ ┌─────────────┐ ┌─────────────┐   │
│  │ References  │ │    Notes    │ │  Subtopics  │   │
│  │   Manager   │ │   Manager   │ │   Manager   │   │
│  └─────────────┘ └─────────────┘ └─────────────┘   │
└─────────────────────────────────────────────────────┘
```

### Project Structure

```
src/literature_review_agent/
├── sdk_agent.py          # Main SDK-based agent
├── sdk_tools/            # Custom MCP tools
│   ├── server.py         # MCP server creation
│   ├── reference_tools.py
│   ├── note_tools.py
│   ├── search_tools.py
│   ├── source_tools.py
│   ├── subtopic_tools.py
│   └── report_tools.py
├── collectors/           # Data source collectors
├── managers/             # Data management
├── processors/           # Document processing
├── hooks.py              # Agent hooks
├── models.py             # Data models
└── cli.py                # CLI interface
```

## Python API

```python
import anyio
from literature_review_agent import SDKLiteratureReviewAgent

async def main():
    agent = SDKLiteratureReviewAgent()

    # Send queries to the agent
    response = await agent.query(
        "Search arXiv for papers on transformer architectures and "
        "add the most relevant ones to the collection"
    )
    print(response)

    # Or use the higher-level methods
    await agent.gather_references(
        topic="Large Language Model Agents",
        on_progress=print
    )

    await agent.organize_references()
    await agent.read_papers(count=5)
    await agent.generate_report()

anyio.run(main)
```

### Custom Callbacks

```python
def on_message(msg: str):
    print(f"Agent: {msg}")

def on_tool_use(tool_name: str, args: dict):
    print(f"Using tool: {tool_name}")

response = await agent.query(
    "Your research query",
    on_message=on_message,
    on_tool_use=on_tool_use,
)
```

## Configuration

Create a `config.yaml` file:

```yaml
llm:
  model: "claude-sonnet-4-20250514"
  max_tokens: 4096

search:
  arxiv_enabled: true
  arxiv_max_results: 50
  semantic_scholar_enabled: true
  semantic_scholar_max_results: 50

processing:
  extract_citations: true
  follow_citations_depth: 1

communication:
  update_frequency: "regular"
```

## Available Tools

The agent has access to 25+ specialized tools:

### Reference Management
| Tool | Description |
|------|-------------|
| `add_reference` | Add a new reference to the collection |
| `search_references` | Search by query, tags, status, priority |
| `update_reference_priority` | Set priority (critical/high/medium/low) |
| `update_reference_status` | Track reading progress |
| `get_reading_queue` | Get prioritized reading list |
| `get_reference_stats` | Collection statistics |

### Academic Search
| Tool | Description |
|------|-------------|
| `search_arxiv` | Search arXiv preprints |
| `search_semantic_scholar` | Search Semantic Scholar |
| `get_paper_citations` | Find papers citing a paper |
| `get_paper_references` | Find papers cited by a paper |
| `get_recommendations` | AI-powered paper recommendations |

### Source Processing
| Tool | Description |
|------|-------------|
| `process_url_file` | Process bookmarks/URL lists |
| `process_blog_feed` | Process RSS feeds |
| `scan_local_folder` | Scan Obsidian/local files |
| `fetch_webpage_content` | Fetch and extract web content |

### Notes & Organization
| Tool | Description |
|------|-------------|
| `create_note` | Create research note |
| `create_subtopic` | Create subtopic for organization |
| `add_subtopic_finding` | Record key finding |
| `generate_progress_report` | Generate status report |

## Tips for Best Results

1. **Be Specific**: "Search arXiv for papers on attention mechanisms in transformers" works better than "find AI papers"

2. **Use Natural Language**: The agent understands complex requests like "Find the most cited papers on BERT and add them to the reading queue"

3. **Iterate**: Start broad, then drill down into specific subtopics

4. **Follow Citations**: Ask the agent to find papers citing important works

5. **Check Progress**: Regularly ask for a progress report to see where you are

## License

MIT License - see LICENSE file for details.

## Acknowledgments

- Built with [Claude Agent SDK](https://docs.anthropic.com/en/docs/claude-code/sdk) by Anthropic
- Uses [Semantic Scholar API](https://www.semanticscholar.org/product/api) for academic search
- arXiv integration via [arxiv.py](https://github.com/lukasschwab/arxiv.py)
