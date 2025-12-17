---
name: large-file-handling
description: Strategies for processing large files that exceed context window limits. Use when dealing with PDFs, documents, markdown files, or any content too large to load at once. Provides chunking, hierarchical navigation, and targeted extraction techniques.
---

# Large File Handling Framework

This skill provides systematic approaches for working with files that exceed Claude Code's context window, ensuring you can still extract, analyze, and process large documents effectively.

## When to Use This Skill

- File exceeds ~100,000 tokens (~75,000 words or ~400 pages)
- Read tool returns truncation warnings
- User mentions file is "very large", "lengthy", or "exceeds context"
- Working with books, comprehensive reports, or large codebases
- Processing multiple large documents in sequence

## Core Principles

1. **Never load blindly** - Always check file size and structure first
2. **Be strategic** - Ask user what they need before reading everything
3. **Work hierarchically** - Navigate by structure (chapters, sections, headings)
4. **Use targeted extraction** - Read only relevant portions
5. **Summarize progressively** - Build understanding incrementally
6. **Track context** - Keep notes on what you've read and where you are

## Strategy Selection

Choose your approach based on file type and task:

| File Type | Primary Strategy | Tools |
|-----------|------------------|-------|
| PDF (academic) | Structured navigation by sections | Read (pages), WebFetch (if URL) |
| PDF (book/report) | Hierarchical chunking by chapters | Read (page ranges) |
| Markdown | Header-based navigation | Read (line ranges), Grep |
| Word docs | Section-based reading | Read (after conversion) |
| Code files | Function/class extraction | Grep, Glob, Read (ranges) |
| Data files | Sampling + targeted queries | Bash (head/tail), Read (ranges) |

## Handling Different File Types

### 1. Large PDFs (Papers, Books, Reports)

#### Step 1: Reconnaissance
```bash
# Check file size first
ls -lh <file.pdf>

# For very large PDFs (>50MB), warn user about processing time
```

#### Step 2: Extract Structure
- Use Read tool to get first few pages (TOC, abstract, introduction)
- Identify document structure (chapters, sections)
- Ask user: "What specific sections are you interested in?"

#### Step 3: Targeted Reading
- Read specific page ranges using `offset` and `limit` parameters
- For academic papers: Abstract → Introduction → Methodology → Results → Discussion → Conclusion
- For books: TOC → Relevant chapters only
- Create summaries as you go

**Example workflow:**
```markdown
1. Read pages 1-10 (TOC + Introduction)
2. Identify key chapters/sections
3. Ask user which sections to prioritize
4. Read those sections with Read tool (page ranges)
5. Create progressive summary in Claude-Notes/
6. Offer to read additional sections as needed
```

### 2. Large Markdown Files

#### Step 1: Map the Structure
```bash
# Extract all headers to see document structure
grep -E "^#{1,6} " large-file.md
```

#### Step 2: Navigate by Sections
- Use Grep to find specific sections
- Read specific line ranges using `offset` and `limit`
- Build a mental map of the document structure

#### Step 3: Targeted Extraction
```markdown
1. Ask user what they're looking for
2. Use Grep to find relevant sections
3. Read those sections specifically
4. Cross-reference related sections as needed
```

**Example:**
```bash
# Find all sections about "authentication"
grep -n -i "authentication" docs.md

# Read lines 450-550 that contain auth section
# Use Read with offset=449, limit=100
```

### 3. Large Code Files

#### Strategy: Index-Driven Exploration

```bash
# Get file statistics
wc -l large-file.py

# Extract function/class signatures
grep -n "^def \|^class " large-file.py

# Extract specific function
grep -A 50 "def function_name" large-file.py
```

#### Best Practices:
- Use Glob to find related files first
- Use Grep to locate specific functions/classes
- Read only the functions/classes of interest
- Ask user which components they need help with

### 4. Large Data Files (CSV, JSON, logs)

#### Strategy: Sampling + Targeted Queries

```bash
# Check size and structure
ls -lh data.csv
head -n 20 data.csv    # First 20 lines
tail -n 20 data.csv    # Last 20 lines

# Count lines
wc -l data.csv

# Sample middle sections
sed -n '1000,1020p' data.csv
```

#### For JSON:
```bash
# Pretty print first record
head -n 100 data.json | jq '.[0]'

# Get schema/keys
jq 'keys' data.json | head -n 50
```

## Progressive Summarization Technique

When processing large documents, use this pattern:

### Level 1: Overview (1-2 paragraphs)
- Document type, length, main topic
- Purpose and intended audience
- Overall structure

### Level 2: Section Summaries (1-3 sentences each)
- Key point of each major section
- Important findings or arguments
- Notable data or examples

### Level 3: Detailed Notes (as needed)
- Deep dive into specific sections user cares about
- Quotes, data, technical details
- Cross-references and citations

**Save summaries as you go:**
```
Claude-Notes/Large-Files/
├── <filename>-overview.md
├── <filename>-section-summaries.md
└── <filename>-detailed-notes.md
```

## Chunking Strategies

### Fixed-Size Chunking
Good for: Uniform documents without clear structure
- Read 50-100 pages/10,000-20,000 lines at a time
- Create summary after each chunk
- Build progressive understanding

### Semantic Chunking
Good for: Structured documents (papers, reports, books)
- Chunk by chapter, section, or topic
- Maintain document hierarchy
- Easier to navigate and reference

### Sliding Window
Good for: Finding specific information
- Use when searching for specific content
- Overlap chunks by 10-20% to avoid missing context
- Use Grep to locate first, then read surrounding context

## Handling Multiple Large Files

When processing several large files:

1. **Triage first**
   ```markdown
   Create inventory:
   - file1.pdf - 500 pages - Priority: High
   - file2.pdf - 300 pages - Priority: Medium
   - file3.pdf - 150 pages - Priority: Low
   ```

2. **Process strategically**
   - Start with highest priority
   - Read abstracts/TOCs of all first
   - Identify overlapping content
   - Avoid redundant reading

3. **Cross-reference as you go**
   - Note when files cite each other
   - Track themes across documents
   - Build unified understanding

## Communication Protocol

### Always Tell the User:

1. **At Start**:
   - "This file is [X] pages/lines. I'll read it strategically."
   - "What specific sections or information do you need?"

2. **During Processing**:
   - "I've read sections A, B, C. Key findings: ..."
   - "Would you like me to continue to section D?"

3. **At Decision Points**:
   - "I found 5 chapters on [topic]. Which should I prioritize?"
   - "This section is 100 pages. Should I summarize or read in detail?"

4. **When Stuck**:
   - "This file is too large to load completely. Can you tell me which parts matter most?"
   - "Would it be helpful if I create a detailed table of contents first?"

## Tool Parameter Guide

### Read Tool with Large Files

```python
# For large files, use offset and limit:
Read(
    file_path="/path/to/large-file.md",
    offset=1000,    # Start at line 1000 (0-indexed: line 1001)
    limit=500       # Read 500 lines
)

# Reading strategy:
# 1. Read first 100 lines (overview)
# 2. Use Grep to find sections of interest
# 3. Read those sections with targeted offset/limit
# 4. Create progressive summary
```

### Grep for Navigation

```bash
# Find all section headers in markdown
grep -n "^#" large-file.md

# Find specific topic with context
grep -n -C 5 "important term" large-file.md

# Case-insensitive search
grep -n -i "pattern" large-file.md
```

## Quality Checklist

Before considering large file processing complete:

- [ ] Confirmed file size and structure
- [ ] Asked user what they need (don't assume)
- [ ] Read/skimmed most relevant sections
- [ ] Created summaries for processed content
- [ ] Tracked what's been read vs. not read
- [ ] Offered to read additional sections
- [ ] Saved notes for future reference
- [ ] Communicated progress clearly

## Common Pitfalls to Avoid

1. **Don't try to load entire file** - You'll hit context limits
2. **Don't read linearly** - Jump to relevant sections
3. **Don't assume what user needs** - Ask first
4. **Don't forget to summarize** - Build understanding incrementally
5. **Don't lose track** - Note what you've read and what's left
6. **Don't over-extract** - Get what's needed, not everything

## Example Workflows

### Workflow 1: Academic Paper (Large Appendix)

```markdown
User: "Summarize this 200-page paper on transformer architectures"

Your approach:
1. Check file size (200 pages = ~150,000 words, too large)
2. Read pages 1-10 (abstract, intro, structure)
3. Respond: "This is a lengthy paper with extensive appendices.
   The main paper is pages 1-40. Would you like:
   a) Summary of main paper only
   b) Detailed review of specific sections
   c) Analysis of particular experiments"
4. Based on response, read targeted sections
5. Create structured summary
6. Offer to dive deeper into specific areas
```

### Workflow 2: Technical Documentation

```markdown
User: "Find information about authentication in this 1000-page manual"

Your approach:
1. Check file size
2. Use Grep to search for "authentication"
3. Find sections: pages 150-180, 340-360, 890-910
4. Read those specific page ranges
5. Synthesize findings across sections
6. Create consolidated authentication guide
```

### Workflow 3: Large Codebase File

```markdown
User: "Explain how the User class works in models.py" (5000 lines)

Your approach:
1. Check file size: wc -l models.py
2. Extract class structure: grep -n "^class " models.py
3. Find User class: grep -n "class User" models.py
4. Read User class + related methods (targeted lines)
5. Search for User references in other parts if needed
6. Create explanation with line number references
```

## Advanced Techniques

### 1. Hierarchical Table of Contents Generation

For unstructured large files, create TOC:
```bash
# Extract structure
grep -n "^#" document.md > toc.txt

# Or for PDFs (if text extractable)
# Create outline of major sections
```

### 2. Keyword Density Analysis

Find most important topics:
```bash
# Word frequency (most mentioned terms)
cat file.txt | tr ' ' '\n' | sort | uniq -c | sort -rn | head -20
```

### 3. Cross-Reference Mapping

Track internal references:
- Note when sections reference each other
- Build dependency graph
- Identify core vs. supplementary content

### 4. Collaborative Reading with User

For very large files:
- User reads some sections
- You read others
- Cross-check findings
- Build unified understanding

---

## Integration with Research Workflow

When using this skill in literature reviews:

1. **Add to reading queue** with size estimate
2. **Use targeted reading** for summaries
3. **Create multi-part notes** (overview + detailed)
4. **Tag extracted sections** by relevance
5. **Link to specific page/line numbers** in references

**Note Template for Large Files:**
```markdown
# [Large Document Title]

**Type:** [Book/Report/Paper]
**Length:** [X pages/lines]
**Sections Read:** [List sections processed]
**Sections Skipped:** [What wasn't read and why]

## Overview
[High-level summary from initial scan]

## Detailed Notes by Section
### Section 1 (pages X-Y)
[Notes]

### Section 2 (pages A-B)
[Notes]

## Key Takeaways
[Synthesized findings]

## Sections for Future Reading
- [ ] Section Z (pages N-M) - [reason to read]
```

---

*This skill helps you work efficiently with large files while maintaining quality and avoiding context limitations. Always prioritize user needs and communicate your approach clearly.*
