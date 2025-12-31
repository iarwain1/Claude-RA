# Why Benchmarking is Hard

**URL:** https://epoch.ai/gradient-updates/why-benchmarking-is-hard
**Authors:** Florian Brand, Jean-Stanislas Denain
**Date:** December 23, 2025
**Type:** Research Article

## Summary

Benchmarking AI systems presents substantial obstacles because numerous variables affect final scores across two critical areas: benchmark setup and model access through APIs.

## Main Challenges

### 1. Benchmark Setup Variables

- **Prompts:** Different prompt formulations yield different results
- **Sampling parameters:** Temperature, top-p, etc. significantly impact performance
- **Scaffolds:** "Scaffolds have a huge impact on agentic benchmarks" (11-15% variance on SWE-bench Verified)
- **Execution environments:** Runtime conditions matter
- **Scoring methods:** Different evaluation approaches produce different scores

### 2. API Access Issues

**Provider-Specific Problems:**
- Rate-limit errors
- Truncated responses
- Hidden token limits
- Timeout issues
- Newly released models handled less reliably than established ones

**Impact on Scores:**
- Selecting different API providers yields noticeably divergent results for identical models
- Variables compound across the evaluation stack
- Final scores diverge significantly from developer-reported numbers

## Implications for Research

**Resource Barrier:** This complexity particularly burdens smaller organizations—academics and hobbyists lack resources to navigate multiple API implementations and troubleshoot provider-specific issues, creating evaluation barriers that slow independent assessment of model capabilities.

## Relevance

**Critical for AI evaluation research.** Highlights systematic challenges in comparing models fairly. Important for understanding why benchmark results may not replicate and why independent evaluations are difficult.

---
*Metadata fetched via WebFetch on 2025-12-31*
