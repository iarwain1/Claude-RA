# On Scalable Oversight with Weak LLMs Judging Strong LLMs

**arXiv:** https://arxiv.org/abs/2407.04622
**Authors:** (OpenAI Safety team - Jan Leike, et al.)
**Date:** 2024-07

## Abstract

This paper explores scalable oversight - specifically whether weaker LLMs can effectively judge or evaluate stronger LLMs. This is a key challenge for AI safety: as AI systems become more capable, human oversight becomes increasingly difficult.

## The Core Problem

**Scalable oversight challenge:**
- Human evaluators cannot always assess superhuman AI outputs
- Need methods for oversight that scale with AI capability
- Can weaker models help supervise stronger ones?

## Key Questions

1. Can weak LLMs reliably identify errors in strong LLM outputs?
2. Under what conditions does weak-to-strong supervision work?
3. What are the limitations of this approach?

## Relevance to AI Safety

**Why this matters:**
- Human oversight will eventually be insufficient for advanced AI
- Need automated methods to complement human judgment
- Understanding weak-to-strong dynamics informs alignment strategy

**Connections to other work:**
- Related to debate and recursive reward modeling
- Informs scalable alignment approaches
- Important for AI governance (how do we evaluate models we can't fully understand?)

## Claude Summary

This paper tackles a fundamental question in AI safety: how do we maintain oversight of systems that exceed our ability to evaluate directly?

**Core tension**: If we need strong AI to evaluate strong AI, we have a bootstrapping problem. Weak-to-strong evaluation offers one potential solution.

**Practical implications**:
- Evaluation pipelines using smaller models as judges
- Understanding when LLM-as-judge can be trusted
- Limits of automated oversight

**Open questions**:
- How much capability gap is acceptable?
- What kinds of errors do weak judges miss?
- Can this be combined with human oversight effectively?

## Relevance

Essential for AI safety research on scalable oversight. As models become more capable, this problem becomes more pressing. Informs both research directions and governance approaches to AI evaluation.
