# Literature Review Agent

An AI-powered research assistant for conducting comprehensive literature reviews. This agent acts as your personal Research Assistant, handling the tedious aspects of literature review while keeping you informed and in control throughout the process.

## Features

### Reference Gathering
- **URL Processing**: Extract and follow links from bookmarks, markdown files, or plain text URL lists
- **Blog/Newsletter Scanning**: Crawl RSS feeds and blog archives for relevant content
- **Academic Search**: Automated searches on arXiv and Semantic Scholar
- **Local File Processing**: Parse Obsidian vaults, PDFs, and note collections
- **Citation Following**: Discover new references by following citation trails

### Organization & Prioritization
- **Intelligent Tagging**: AI-powered categorization into subtopics
- **Relevance Ranking**: Automatic prioritization based on your research questions
- **Duplicate Detection**: Smart deduplication across multiple sources
- **Reading Queue**: Organized queue sorted by priority

### Analysis & Note-Taking
- **Document Reading**: Full-text extraction from PDFs and web pages
- **Key Point Extraction**: AI-powered identification of important findings
- **Automated Notes**: Generate structured notes while reading
- **Quote Capture**: Save important quotes with context

### Synthesis & Reporting
- **Subtopic Summaries**: AI-generated summaries for each research area
- **Full Report Generation**: Comprehensive literature review documents
- **Export Formats**: Markdown, BibTeX, and more
- **Progress Tracking**: Real-time statistics and progress reports

### Interactive Communication
- **Continuous Updates**: Regular progress notifications
- **Question Prompts**: Agent asks for clarification when needed
- **Insight Sharing**: Highlights particularly interesting findings
- **Feedback Integration**: Adjusts based on your responses

## Installation

### Prerequisites
- Python 3.10 or higher
- Anthropic API key

### Setup

1. Clone the repository:
```bash
git clone https://github.com/yourusername/Claude-Literature-Review-Agent.git
cd Claude-Literature-Review-Agent
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install the package:
```bash
pip install -e .
```

4. Set up your API key:
```bash
cp .env.example .env
# Edit .env and add your ANTHROPIC_API_KEY
```

## Quick Start

### Interactive Mode (Recommended for First-Time Users)

```bash
lit-review interactive
```

This launches a guided session where the agent will:
1. Ask about your research topic
2. Help you configure sources
3. Guide you through each phase of the review

### Command-Line Mode

```bash
# Start a new project
lit-review new "AI Agents and Autonomous Systems"

# Gather references from configured sources
lit-review gather

# Organize and prioritize references
lit-review organize

# Read and analyze papers
lit-review read --count 10

# Generate the final report
lit-review report

# Check project status
lit-review status
```

## Configuration

### Project Configuration

Create a `config.yaml` file (see `config/default.yaml` for template):

```yaml
llm:
  model: "claude-sonnet-4-20250514"
  max_tokens: 4096

search:
  arxiv_enabled: true
  arxiv_max_results: 50
  semantic_scholar_enabled: true

processing:
  extract_citations: true
  follow_citations_depth: 1

communication:
  update_frequency: "regular"
  ask_before_major_actions: true
```

### Source Types

#### URL Lists
Plain text or markdown files containing URLs:
```
# My Research Links
- [Attention Is All You Need](https://arxiv.org/abs/1706.03762)
- [BERT Paper](https://arxiv.org/abs/1810.04805)
https://example.com/interesting-paper
```

#### Blogs/Newsletters
RSS feeds or blog URLs:
- The agent will automatically discover RSS feeds
- Extracts links from posts to academic papers
- Filters for relevance to your topic

#### Local Notes (Obsidian-Compatible)
- Reads markdown files from your notes folder
- Extracts tags and links
- Supports YAML frontmatter

## Usage Examples

### Python API

```python
import asyncio
from literature_review_agent import LiteratureReviewAgent
from literature_review_agent.models import SourceConfig

async def main():
    # Create agent
    agent = LiteratureReviewAgent()

    # Start a new project
    await agent.start_new_project(
        topic_name="Large Language Models",
        topic_description="Research on transformer-based language models...",
        key_questions=[
            "What are the scaling laws for LLMs?",
            "How do different training approaches compare?",
        ],
        key_terms=["transformer", "language model", "GPT", "scaling"],
    )

    # Add sources
    await agent.add_source(SourceConfig(
        name="My Bookmarks",
        source_type="url_list",
        path="/path/to/bookmarks.md",
    ))

    await agent.add_source(SourceConfig(
        name="AI Blog",
        source_type="blog",
        url="https://example-ai-blog.com",
    ))

    # Run the research process
    await agent.gather_references()
    await agent.organize_references()
    await agent.read_papers(max_papers=20)
    await agent.generate_report()

    await agent.close()

asyncio.run(main())
```

### Custom Callbacks

```python
from literature_review_agent import LiteratureReviewAgent
from literature_review_agent.models import AgentMessage

def my_message_handler(message: AgentMessage):
    if message.message_type == "insight":
        print(f"Important: {message.content}")
    elif message.message_type == "question":
        print(f"Agent asks: {message.content}")

def my_input_handler(prompt: str, options: list[str] | None) -> str:
    # Custom input handling (e.g., from a GUI)
    return input(prompt)

agent = LiteratureReviewAgent(
    message_callback=my_message_handler,
    input_callback=my_input_handler,
)
```

## Research Process

The agent follows a structured research process:

### 1. Initialization
- Define research topic and questions
- Configure sources (URL lists, blogs, local files)
- Set search parameters

### 2. Reference Gathering
- Process URLs from your collections
- Crawl blog/newsletter archives
- Search academic databases (arXiv, Semantic Scholar)
- Extract links from local notes

### 3. Organization
- Evaluate relevance of each reference
- Assign priorities (Critical, High, Medium, Low)
- Suggest and create subtopics
- Build reading queue

### 4. Reading & Analysis
- Read full text of high-priority papers
- Extract key findings and methodology
- Take structured notes
- Identify citations to follow

### 5. Citation Following
- Find papers cited in "Related Work" sections
- Discover foundational papers
- Add promising leads to the queue
- Identify new subtopics

### 6. Synthesis
- Generate summaries for each subtopic
- Compile key findings across the literature
- Create comprehensive report
- Export in various formats

## Output

### Literature Review Report
A comprehensive markdown document including:
- Executive summary
- Subtopic summaries with key findings
- Annotated bibliography
- Open questions and future directions

### Data Files
- `references.json`: All collected references
- `notes.json`: Research notes
- `subtopics.json`: Topic organization
- `project.json`: Project state

### Export Formats
- Markdown (default)
- BibTeX (for citations)
- Plain text

## Tips for Best Results

1. **Be Specific**: Detailed research questions help the agent prioritize better
2. **Start with Your Links**: The agent can find new sources, but your curated links are valuable starting points
3. **Review Subtopics**: Confirm or adjust suggested subtopics early
4. **Iterate**: Run multiple reading sessions, following new leads each time
5. **Check Insights**: The agent highlights important findings - don't miss them!

## Architecture

```
literature_review_agent/
├── agent.py           # Main orchestrator
├── cli.py             # Command-line interface
├── models.py          # Data models
├── collectors/        # Source collectors
│   ├── arxiv_collector.py
│   ├── blog_collector.py
│   ├── local_collector.py
│   ├── semantic_scholar_collector.py
│   ├── url_collector.py
│   └── web_collector.py
├── managers/          # Data management
│   ├── note_manager.py
│   ├── reference_manager.py
│   └── subtopic_manager.py
├── processors/        # Document processing
│   ├── analyzer.py
│   ├── document_reader.py
│   └── report_generator.py
└── utils/             # Utilities
    ├── config.py
    ├── logging.py
    ├── persistence.py
    └── text.py
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

MIT License - see LICENSE file for details.

## Acknowledgments

- Built with [Claude](https://www.anthropic.com/claude) by Anthropic
- Uses [Semantic Scholar API](https://www.semanticscholar.org/product/api) for academic search
- arXiv integration via [arxiv.py](https://github.com/lukasschwab/arxiv.py)
