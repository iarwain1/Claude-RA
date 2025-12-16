# Me, Myself, and AI: The Situational Awareness Dataset (SAD) for LLMs

**arXiv:** https://arxiv.org/abs/2407.04694
**Authors:** Rudolf Laine, Bilal Chughtai, Jan Betley, Kaivalya Hariharan, Jeremy Scheurer, Mikita Balesni, Marius Hobbhahn, Alexander Meinke, Owain Evans
**Date:** 2024-07-05
**GitHub:** https://github.com/lrudl/sad
**Website:** https://situational-awareness-dataset.org/

## Abstract

This paper defines "situational awareness" as a model's knowledge of itself and its circumstances. It explores:
- Do LLMs know they are LLMs?
- Do they reliably act on this knowledge?
- Are they aware of current circumstances (e.g., being deployed vs. evaluated)?

## The SAD Benchmark

**7 task categories, 13,000+ questions**

Tests include:
1. Recognizing own generated text
2. Predicting own behavior
3. Determining if prompt is from internal evaluation or deployment
4. Following instructions that depend on self-knowledge

## Key Findings

**Results across 16 LLMs:**
- All models perform better than chance
- Even highest-scoring (Claude 3 Opus) far from human baseline on certain tasks
- Chat models outperform base models on SAD
- Chat model advantage is specific to SAD (not general knowledge)

## Why Situational Awareness Matters

**Benefits:**
- Enhances capacity for autonomous planning and action
- Useful for automation

**Risks:**
- Novel AI safety and control concerns
- Models that know they're being evaluated might behave differently
- Potential for strategic behavior

## Claude Summary

SAD addresses a crucial question for AI safety - do models know what they are?

**Why this matters for safety**:
- Situationally aware models might game evaluations
- Deployment vs. evaluation behavior could diverge
- Self-knowledge enables more sophisticated deception

**Key contribution**: Breaks down situational awareness into measurable components rather than treating it as a monolithic concept.

**Limitations to consider**:
- Behavioral tests can't prove absence of awareness
- Models might have awareness without revealing it
- Self-reports may not reflect internal states

## Relevance

**Critical for AI safety research.** Situational awareness is a key concern for advanced AI systems. This benchmark provides tools to measure and track it as models improve. Important for understanding deceptive alignment and evaluation gaming risks.
