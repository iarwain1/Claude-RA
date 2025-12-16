# Prover-Verifier Games Improve Legibility of LLM Outputs

**arXiv:** https://arxiv.org/abs/2407.13692
**Authors:** OpenAI (Jan Leike, et al.)
**Date:** 2024-07

## Abstract

This paper explores using game-theoretic approaches to improve the legibility (readability/understandability) of language model outputs. The goal is to make LLM outputs more human-readable and easier to verify.

## Key Concepts

**Prover-Verifier Games:**
- **Prover**: Model that generates solutions/explanations
- **Verifier**: Model that evaluates correctness and understandability
- Adversarial game setting drives improvement

**Legibility:**
- Making outputs not just correct, but clearly readable
- Enabling human verification
- Important for oversight and safety

## Training Approach

By training in this adversarial game setting:
- Prover learns to produce outputs that are correct AND legible
- Verifier pressure ensures explanations are actually useful
- Results in more checkable, verifiable outputs

## Safety Implications

**Why legibility matters for alignment:**
- Humans can more easily verify correct outputs
- Easier to catch errors or deception
- Supports scalable oversight

**Connections to other work:**
- Related to debate (AI Alignment via Debate)
- Supports interpretability goals
- Helps with the "trust but verify" approach to AI deployment

## Claude Summary

This paper addresses a practical problem for AI safety: how do we get models to show their work in a way we can actually check?

**Core insight**: You can train for legibility by setting up a game where outputs must be understandable to a verifier, not just correct.

**Practical applications**:
- Math problem solving with verifiable steps
- Code generation with readable logic
- Decision explanations that humans can audit

**Limitations**: Game dynamics may not fully capture what humans find legible. Verifier model may have blind spots.

## Relevance

Important for scalable oversight and AI safety. Addresses how to make AI outputs more amenable to human verification. From OpenAI's safety team, part of their broader work on alignment through debate-like mechanisms.
