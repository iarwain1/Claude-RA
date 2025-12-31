# Shipping at Inference Speed

**URL:** https://steipete.me/posts/2025/shipping-at-inference-speed
**Author:** Peter Steinberger
**Date:** 2025
**Type:** Blog Post / Development Practice

## Core Concept

Developing software at a pace limited primarily by **AI model inference time** rather than human coding ability. The bottleneck shifts from writing code to waiting for model processing.

## Key Practices

### Model Selection
**Strategy:** Use proven, powerful models consistently
- GPT-5.2-codex on "high" reasoning effort
- "I don't wanna spend time thinking about different modes or ultrathink"
- Prioritize reliability over experimentation with new tools

### Iterative Development Approach

**Pattern:**
1. Build something quickly
2. Test it
3. Observe how it feels in real use
4. Refine based on actual interaction

**Not:** Comprehensive upfront planning
**Instead:** Constant model feedback and rapid iteration

### Context Management

**With Superior Models:**
- Maintain fuller context across sessions
- Don't restart for new tasks
- Allow models to reference previous work
- Context accumulation improves performance

### Practical Workflow

**Efficient Patterns:**
- Start projects as CLIs before adding UI layers
- Use extensive in-project documentation to guide models
- Leverage cross-project references (avoid reinventing solutions)
- Commit directly to main (skip branch management overhead)

**Focus:** Remove friction from iteration cycles

## Development Implications

### What Becomes the Bottleneck

**No longer limited by:**
- Coding ability
- Typing speed
- Remembering syntax

**Now limited by:**
- Thoughtful system design decisions
- Choosing frameworks
- Designing data flow
- Picking dependencies
- Architectural choices

### Commoditization of Application Logic

**Commoditized:** Moving data between interfaces, basic CRUD operations, standard implementations

**Strategic Value Shifts to:**
- Architectural decisions
- Domain understanding
- System design
- Technology selection

## Fundamental Change

**Traditional development:** Human writes code → code runs
**Inference-speed development:** Human describes intent → AI generates code → iterate rapidly

The **pace** is set by inference, not implementation.

## Implications

### For Developers
- Judgment and taste matter more than coding speed
- Architecture and design become primary skills
- Domain knowledge increasingly valuable
- Ability to iterate and refine becomes critical

### For Organizations
- Speed of shipping increases dramatically
- Skill requirements shift toward design and domain expertise
- Traditional coding bottlenecks disappear
- New bottlenecks emerge around decision-making

## Relevance

**Important for understanding AI-augmented development.** Shows how development workflow fundamentally changes with powerful coding agents. Identifies new bottlenecks and skill requirements. Practical patterns from real experience.

---
*Metadata fetched via WebFetch on 2025-12-31*
