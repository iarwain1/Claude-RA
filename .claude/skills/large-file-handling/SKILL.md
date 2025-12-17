---
name: large-file-handling
description: Strategies for reading AND writing large files that exceed context window limits. Use when dealing with PDFs, documents, markdown files, or any content too large to load or generate at once. Provides chunking, hierarchical navigation, targeted extraction, and incremental writing techniques.
---

# Large File Handling Framework

This skill provides systematic approaches for working with files that exceed Claude Code's context window, ensuring you can still extract, analyze, process, AND generate large documents effectively.

## When to Use This Skill

**For Reading:**
- File exceeds ~100,000 tokens (~75,000 words or ~400 pages)
- Read tool returns truncation warnings
- User mentions file is "very large", "lengthy", or "exceeds context"
- Working with books, comprehensive reports, or large codebases
- Processing multiple large documents in sequence

**For Writing:**
- User asks to generate content exceeding ~5,000 lines
- Creating comprehensive documentation, reports, or datasets
- Generating code files with extensive functionality
- Building large configuration files or data exports
- Any output that might approach context limits

## CRITICAL: Proactive Triggering

**ALWAYS check file size BEFORE attempting to read or write. This is NOT optional.**

### Before Reading Any File:

```bash
# Check line count
wc -l <file>

# Check file size in human-readable format
ls -lh <file>

# Quick heuristic:
# - If > 10,000 lines → Use chunking strategies
# - If > 50,000 lines → Definitely use this skill
# - If > 100MB → Warn user and use extreme caution
```

**If you receive a truncation warning from Read tool:**
- IMMEDIATELY stop trying to read the whole file
- Switch to chunked/targeted reading approach
- Explain situation to user
- Ask what specific sections they need

### Before Writing Large Content:

**If the user requests:**
- "Generate a comprehensive X"
- "Create full documentation for Y"
- "Write all the code for Z"
- Anything suggesting >5,000 lines of output

**You MUST:**
1. Estimate the output size
2. Warn user if it will be large
3. Offer alternatives:
   - Write incrementally (section by section)
   - Split into multiple files
   - Create outline first, then fill in parts
   - Generate summary/template only

**Example Response:**
```
"Generating a comprehensive API documentation for this codebase
would produce ~20,000 lines, which exceeds my context window.

I can instead:
a) Create a modular structure with separate files per module
b) Generate section by section, letting you review each
c) Create detailed outline + key examples, then fill specific sections
d) Focus on the most important 5-10 endpoints first

Which approach would you prefer?"
```

## Core Principles

### For Reading:
1. **Never load blindly** - Always check file size and structure first
2. **Be strategic** - Ask user what they need before reading everything
3. **Work hierarchically** - Navigate by structure (chapters, sections, headings)
4. **Use targeted extraction** - Read only relevant portions
5. **Summarize progressively** - Build understanding incrementally
6. **Track context** - Keep notes on what you've read and where you are

### For Writing:
1. **Estimate before generating** - Calculate expected output size
2. **Warn proactively** - Tell user if output will be large
3. **Offer alternatives** - Suggest splitting, incremental writing, or modular approaches
4. **Write incrementally** - Generate in chunks rather than all at once
5. **Use Edit over Write** - Modify sections of existing files rather than regenerating
6. **Structure modularly** - Design outputs that can be split across files

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

## Writing Large Files: Strategies & Best Practices

When you need to generate large files, use these strategies to avoid context limitations.

### 1. Size Estimation

Before writing, estimate the output size:

```python
# Rough estimation guide:
# - 1 line of code ≈ 40-80 characters ≈ 10-20 tokens
# - 1 paragraph prose ≈ 100-200 words ≈ 130-260 tokens
# - 1 page (double-spaced) ≈ 250 words ≈ 330 tokens

# Examples:
# - 100-function API ≈ 5,000-10,000 lines ≈ Too large
# - Comprehensive docs (50 pages) ≈ 12,500 words ≈ Too large
# - Large config file (1000+ entries) ≈ May be too large
```

**Action:** If estimated output > 5,000 lines or 50,000 tokens, trigger incremental strategies.

### 2. Incremental Writing Strategies

#### Strategy A: Section-by-Section Generation

Instead of generating entire file at once, create it piece by piece:

```markdown
**Step 1:** Create file structure/skeleton
**Step 2:** Write Section 1, let user review
**Step 3:** Write Section 2, let user review
**Step 4:** Continue until complete

**Benefits:**
- Stay within context limits
- User can provide feedback early
- Easier to revise specific parts
- Avoid losing work if errors occur
```

**Implementation:**
```markdown
1. Create outline/structure first (Write)
2. For each section:
   - Generate content
   - Append using bash: echo "content" >> file.md
   - OR use Edit to add to existing file
   - Report progress to user
3. Final review and polish
```

#### Strategy B: Multi-File Approach

Split large output across multiple files:

```markdown
**When to use:**
- API docs (one file per endpoint)
- Large codebase generation (one file per module)
- Comprehensive reports (one file per chapter)
- Test suites (one file per test category)

**Structure:**
project/
├── README.md (overview + navigation)
├── part-1-introduction.md
├── part-2-methodology.md
├── part-3-results.md
└── part-4-conclusions.md
```

**Benefits:**
- Each file stays manageable
- Easier to edit specific parts
- Better organization
- Can process in parallel if needed

#### Strategy C: Template + Fill Pattern

Create template first, fill details later:

```markdown
1. Generate comprehensive outline/template
2. User reviews structure
3. Fill in high-priority sections first
4. Fill remaining sections on request
5. User specifies which sections need detail

**Example:**
# API Documentation [Template]

## Endpoint: /users
[DETAIL PENDING]

## Endpoint: /posts
[DETAIL PENDING]

# API Documentation [After Fill]

## Endpoint: /users
[FULL DETAILS ADDED]

## Endpoint: /posts
[DETAIL PENDING - user didn't request yet]
```

### 3. Tool Selection for Large Writes

| Tool | When to Use | Max Recommended Size |
|------|-------------|---------------------|
| **Write** | Creating new files, small-to-medium outputs | < 2,000 lines |
| **Edit** | Modifying existing files, adding sections | Any size (targets specific sections) |
| **Bash (echo >>)** | Appending content incrementally | Unlimited (used iteratively) |
| **Bash (cat << EOF)** | Writing medium blocks of content | < 1,000 lines per operation |

### 4. Incremental Writing with Edit Tool

For existing large files, use Edit instead of regenerating:

```markdown
**Scenario:** User wants to add content to 10,000-line file

**WRONG approach:**
1. Read entire file (truncated!)
2. Try to Write new version (context exceeded!)

**RIGHT approach:**
1. Use Grep to find insertion point
2. Read only surrounding context (200 lines)
3. Use Edit to insert new content
4. Verify with targeted Read
```

**Example:**
```python
# Find where to insert
grep -n "def main():" large_file.py  # Returns line 8543

# Read context around insertion point
Read(file_path="large_file.py", offset=8540, limit=10)

# Use Edit to insert new function
Edit(
    file_path="large_file.py",
    old_string="def main():\n    ...",
    new_string="def new_function():\n    ...\n\ndef main():\n    ..."
)
```

### 5. Appending Content Progressively

For building files incrementally:

```bash
# Create initial file
echo "# Report Title" > report.md
echo "" >> report.md

# Add sections incrementally
echo "## Introduction" >> report.md
echo "Content here..." >> report.md
echo "" >> report.md

# Add more sections as needed
echo "## Methodology" >> report.md
echo "More content..." >> report.md

# Report progress to user after each section
```

### 6. Handling User Requests for Large Outputs

#### Common Request Patterns:

| Request | Likely Size | Recommended Approach |
|---------|-------------|---------------------|
| "Generate complete test suite" | Very Large | Multi-file, test categories in separate files |
| "Write full documentation" | Very Large | Multi-file by topic + index |
| "Create comprehensive dataset" | Very Large | Generate script to create it, or sample subset |
| "Build entire application" | Very Large | Scaffold structure, implement key features only |
| "Translate/convert whole file" | Large | Process in chunks, may need multiple passes |

#### Response Template:

```markdown
User: "Generate [large output X]"

Your response:
"I estimate this would produce approximately [X] lines/pages,
which exceeds my context window capacity.

To handle this effectively, I recommend:

[Option A]: [Split into N files/sections]
- Benefit: [...]
- Structure: [...]

[Option B]: [Incremental generation]
- Benefit: [...]
- Process: [...]

[Option C]: [Template/outline approach]
- Benefit: [...]
- Process: [...]

Which approach works best for your needs? Or would you like
to focus on a specific subset first?"
```

### 7. Quality Control for Large Outputs

When generating large content incrementally:

- [ ] **Track progress**: Tell user which sections are done
- [ ] **Validate as you go**: Check each section before moving on
- [ ] **Maintain consistency**: Keep style, formatting, naming consistent
- [ ] **Version control**: Commit after each major section
- [ ] **Test incrementally**: For code, test each module as generated
- [ ] **Cross-reference**: Ensure sections connect properly
- [ ] **Navigation aids**: Add TOC, links, index for large docs

### 8. Warning Signs You're Writing Too Much

**STOP and reconsider approach if:**
- Your Write operation exceeds 2,000 lines
- You're generating similar content repetitively (can it be templated/scripted?)
- User asked for "everything" or "complete" (clarify scope)
- You feel uncertain if it will fit (it probably won't)
- The file you're creating would be hard for user to navigate

**Alternative solutions:**
- Generate a script that creates the content
- Create example + template for user to replicate
- Build modular components user can combine
- Focus on core/critical parts only

### 9. Example: Generating Large Documentation

```markdown
**User Request:** "Create complete API documentation for this service"

**Your Response:**
"I count 47 endpoints in this service. Complete documentation
would be ~15,000 lines.

I'll create a modular documentation structure:

docs/
├── README.md (overview, getting started)
├── authentication.md
├── users/
│   ├── list-users.md
│   ├── create-user.md
│   └── ...
├── posts/
│   ├── list-posts.md
│   └── ...
└── errors.md

I'll start with:
1. README.md (structure + navigation)
2. Authentication (most important)
3. 3-5 most-used endpoints as examples

Then you can tell me which other endpoints to document in detail.

Sound good?"

**User:** "Yes, perfect"

**Your Actions:**
1. Create docs/ folder structure
2. Write README.md with TOC
3. Write authentication.md
4. Write 3-5 key endpoint docs
5. Report completion, await next instructions
```

### 10. Large File Writing Checklist

Before writing large content:
- [ ] Estimated output size
- [ ] Warned user if size is problematic
- [ ] Offered alternatives (multi-file, incremental, template)
- [ ] Got user approval on approach
- [ ] Planned section/file structure

While writing:
- [ ] Writing incrementally (not all at once)
- [ ] Reporting progress after each section
- [ ] Validating output quality
- [ ] Maintaining consistent style

After writing:
- [ ] Verified all sections complete
- [ ] Created navigation aids (TOC, index)
- [ ] Tested (for code) or proofread (for docs)
- [ ] Committed to version control

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

### For Reading Large Files:

- [ ] Checked file size BEFORE attempting to read
- [ ] Asked user what they need (don't assume)
- [ ] Read/skimmed most relevant sections
- [ ] Created summaries for processed content
- [ ] Tracked what's been read vs. not read
- [ ] Offered to read additional sections
- [ ] Saved notes for future reference
- [ ] Communicated progress clearly

### For Writing Large Files:

- [ ] Estimated output size before generating
- [ ] Warned user if output will be large
- [ ] Offered alternative approaches
- [ ] Got user approval on approach
- [ ] Generated content incrementally
- [ ] Validated each section before moving on
- [ ] Reported progress throughout
- [ ] Created navigation aids (TOC, index, etc.)

## Common Pitfalls to Avoid

### Reading Pitfalls:
1. **Don't try to load entire file** - You'll hit context limits
2. **Don't read linearly** - Jump to relevant sections
3. **Don't assume what user needs** - Ask first
4. **Don't forget to summarize** - Build understanding incrementally
5. **Don't lose track** - Note what you've read and what's left
6. **Don't over-extract** - Get what's needed, not everything

### Writing Pitfalls:
1. **Don't generate blindly** - Estimate size first
2. **Don't try to Write 5,000+ lines at once** - Use incremental approaches
3. **Don't ignore truncation warnings** - Switch strategies immediately
4. **Don't regenerate large files** - Use Edit for modifications
5. **Don't create single massive files** - Split into modular structure
6. **Don't forget to warn user** - Tell them if output will be large BEFORE generating

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

### Workflow 3: Large Codebase File (Reading)

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

### Workflow 4: Generating Large Test Suite (Writing)

```markdown
User: "Generate comprehensive unit tests for all 50 API endpoints"

Your approach:
1. Estimate: 50 endpoints × ~100 lines/test = ~5,000 lines total
2. Respond: "This would generate ~5,000 lines across 50 test files.
   I'll create a modular test structure:

   tests/
   ├── test_users.py (user endpoint tests)
   ├── test_posts.py (post endpoint tests)
   ├── test_auth.py (auth endpoint tests)
   └── ... (organized by resource)

   I'll start with:
   a) Test framework setup + helpers
   b) Tests for 5 most critical endpoints
   c) Then we can add more as needed

   Sound good?"
3. Get user approval
4. Create test structure (Write conftest.py, base classes)
5. Write 5 priority test files incrementally
6. Report completion, ask which endpoints to test next
```

### Workflow 5: Adding to Existing Large File (Writing)

```markdown
User: "Add error handling to all functions in this 8,000-line file"

Your approach:
1. Check file size: wc -l large_module.py (8,000 lines)
2. DON'T try to Read entire file
3. Extract function signatures: grep -n "^def " large_module.py
4. Count functions: ~80 functions found
5. Respond: "I found 80 functions. Adding error handling to all
   would require modifying 8,000 lines.

   I recommend:
   a) Start with the 10 most critical functions (you specify)
   b) Create error handling pattern, apply to high-risk functions first
   c) Generate a script to add standard error handling to remaining functions

   Which functions are highest priority?"
6. For each function:
   - Use Grep to find function
   - Read function with context (offset/limit)
   - Use Edit to add error handling
   - Test
7. Report progress after each function
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
