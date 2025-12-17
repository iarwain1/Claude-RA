# There Are Only 6 RAG Evals

**Authors:** Jason Liu
**Year:** 2025 (May)
**URL:** https://jxnl.co/writing/2025/05/19/there-are-only-6-rag-evals/

## Key Contributions

1. **Simplified RAG evaluation framework:** Reduces complexity to 6 core metrics
2. **Three-tier structure:** Traditional IR → Primary RAG → Advanced metrics
3. **Conditional relationship framing:** Q, C, A relationships cover all evaluation aspects
4. **Practical prioritization:** Debug retrieval first, then generation

## Overview

Argues that RAG evaluation feels needlessly complex, but there are fundamentally only 6 ways to evaluate a RAG system. The framework uses Question (Q), Context (C), and Answer (A) components and their conditional relationships.

## Core Framework

### The Three Components

| Component | Description |
|-----------|-------------|
| **Q (Question)** | User query/input |
| **C (Context)** | Retrieved documents/chunks |
| **A (Answer)** | Generated response |

### Conditional Relationships

> "Looking at this through the lens of conditional relationships gives exactly six possible relationships—no more, no less."

| Relationship | What It Measures |
|--------------|------------------|
| **C\|Q** | Is context relevant to question? |
| **A\|C** | Is answer faithful to context? (groundedness) |
| **A\|Q** | Does answer address the question? |
| **C\|A** | Does context support the answer? |
| **Q\|C** | Is the question answerable from context? |
| **Q\|A** | Does the question match what was answered? |

## Three-Tier Structure

### Tier 1: Retrieval Metrics (Foundation)

> "Use precision, recall, MAP@K, and MRR@K to tune your retriever—these don't require LLM evaluation and provide quick feedback cycles."

| Metric | Description |
|--------|-------------|
| Precision@K | Relevant docs in top K |
| Recall@K | Found relevant docs / total relevant |
| MAP@K | Mean average precision |
| MRR@K | Mean reciprocal rank |

**Key insight:** Fast to compute, no LLM needed, quick iteration.

### Tier 2: Primary RAG Relationships

Core metrics for most use cases:
- **C\|Q:** Context relevance to query
- **A\|C:** Answer faithfulness/groundedness
- **A\|Q:** Answer relevance to question

### Tier 3: Advanced Metrics

> "Use them for monthly evaluations, major releases, and strategic decisions."

- **C\|A:** Context supports answer
- **Q\|C:** Question answerability from context
- **Q\|A:** Question-answer alignment

**Domain variation:** Medical RAG needs stronger C\|A (evidence requirements).

## Practical Guidance

### Evaluation Workflow

> "Debug retrieval first using IR metrics, then tackle generation quality using properly validated LLM judges."

1. **Start with Tier 1:** Fix retrieval problems first
2. **Move to Tier 2:** Evaluate core relationships
3. **Tier 3 for deep analysis:** Major releases, strategic decisions

### Relation to Error Analysis

> "In addition to Jason's six evals, error analysis on your specific data may reveal domain-specific failure modes that warrant their own metrics."

## Relevance to Review

**Highly relevant for RAG evaluation specifically.** Key insights:

### For Prompt Evaluation

1. **Retrieval separate from generation:** Evaluate independently before combining
2. **Six relationships cover all cases:** No hidden evaluation dimensions
3. **Tiered approach:** Start simple, add complexity as needed
4. **Domain-specific metrics:** Medical, legal may need different emphasis

### Alignment with Husain Guidance

| Liu Framework | Husain Guidance | Assessment |
|---------------|-----------------|-----------|
| Tier 1 IR metrics | Separate retrieval from generation | **Strongly aligned** |
| Tier 2 primary | Core RAG evaluation | **Aligned** |
| Error analysis addition | Domain-specific failure modes | **Strongly aligned** |
| LLM judges for generation | LLM-as-judge for subjective | **Aligned** |

### Mapping to Subtopics

| Tier | Primary Subtopic |
|------|-----------------|
| Tier 1 | automated-metrics |
| Tier 2 | llm-as-judge (for generation) |
| Tier 3 | evaluation-frameworks |

### Implications for Prompt Evaluation

| RAG Component | Prompt Evaluation Insight |
|---------------|--------------------------|
| Retrieval query prompts | Evaluate C\|Q relationship |
| Generation prompts | Evaluate A\|C, A\|Q relationships |
| System prompts | May affect all relationships |

## Citations to Follow

- Information retrieval metrics literature
- LLM judge validation approaches
- Domain-specific RAG evaluation papers

## Questions/Notes

- **Strength:** Elegantly simple framework (6 metrics)
- **Strength:** Conditional relationship framing is mathematically complete
- **Strength:** Practical tiered approach
- **Strength:** Directly referenced by Hamel Husain
- **Gap:** Less guidance on specific metric implementations
- **Gap:** LLM judge validation not detailed
- **Connects to:** husain2025evalsfaq (RAG evaluation), automated-metrics subtopic
- **Currency:** May 2025, current

## Evidence Quality

**Medium for framework guidance.** Provides clear conceptual framework but limited empirical validation. Strong for "what to measure"; implementation details left to reader.
