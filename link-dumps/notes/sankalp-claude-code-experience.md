# My Experience with Claude Code 2.0

**URL:** https://sankalp.bearblog.dev/my-experience-with-claude-code-20-and-how-to-get-better-at-using-coding-agents/
**Author:** Sankalp
**Type:** Blog Post / User Experience
**Date:** 2025

## Summary

User experience report and practical guide for getting better at using Claude Code 2.0 and coding agents generally. Emphasizes context management, strategic agent use, and developing domain expertise.

## What Worked Well

### Superior Communication
- **Opus 4.5** excels at explaining changes and pair programming
- Better intent detection than competing tools
- Acts as collaborative partner, not just code generator

### Faster Feedback Loops
- High throughput enables "visceral progress"
- Speed advantage in both thinking and raw throughput
- Faster iteration cycles improve development experience

### Product Engineering
- Claude Code's harness, UI/UX, and integrations create "magical experience"
- Thoughtful features: syntax highlighting, checkpointing
- Well-designed tool ecosystem

## What Didn't Work

### Model Issues
- **Sonnet 4.5** produced "haphazard changes" leading to bugs
- Earlier iterations struggled with consistency

### Context Management
- **MCP servers bloat context** - tool definitions consume tokens upfront
- Increases costs unnecessarily
- Context fills up quickly on complex tasks

### Sub-Agent Overhead
- Parallel exploration agents can be overkill
- Created UI flickering issues in some cases

## Key Recommendations

### 1. Context Engineering
**Critical Insight:** Tool results fill your context window rapidly

**Best Practice:**
- Monitor context usage
- Use compaction or start new conversations at 60% capacity on complex tasks
- Be strategic about what stays in context

### 2. Strategic Sub-Agent Use
**Effective Pattern:**
- Let Explore agents search codebases
- Read relevant files yourself after exploration
- Ensures "all that ingested context can attend to each other"

**Avoid:** Letting agents accumulate context without your direct engagement

### 3. Complementary Model Usage
**Multi-Model Strategy:**
- GPT-5.2-Codex for code review and bug detection
- Claude for execution and explanation
- Use strengths of each model

### 4. Build Domain Expertise
**Fundamental Principle:**
"Experience builds judgement and taste" - more important than chasing latest releases

**Focus on:**
- Developing better judgment about code quality
- Building taste for good architecture
- Understanding your domain deeply

### 5. Experimental Mindset
**Recommendation:**
Try models on unexpected tasks to develop intuition about actual capabilities

**Philosophy:**
Play and experiment rather than passively consuming releases

## Overarching Philosophy

**Effective AI augmentation requires:**
1. Updating tooling strategically
2. Upskilling in your domain
3. Maintaining experimental mindset
4. Active engagement with context and tools

Not about using latest features, but developing judgment and workflow that amplifies your capabilities.

## Relevance

**Important for coding agent users.** Provides practical, experience-based guidance on getting value from Claude Code. Shows common pitfalls and effective patterns. Emphasizes fundamentals over feature-chasing.

---
*Metadata fetched via WebFetch on 2025-12-31*
