# Great Models Think Alike and this Undermines AI Oversight

**arXiv:** https://arxiv.org/abs/2502.04313
**Authors:** Shashwat Goel, Joschka Struber, Ilze Amanda Auzina, Karuna K Chandra, et al.
**Date:** 2025-02-06 (v1), revised 2025-06-12 (v2)
**Website:** https://model-similarity.github.io/

## Abstract

As LM capabilities advance, evaluating and supervising them at scale is getting harder for humans. There is hope that other language models can automate these tasks - what the authors call **"AI Oversight."**

## Key Contributions

**1. CAPA Metric:**
- Chance Adjusted Probabilistic Agreement
- Measures LM similarity based on overlap in model mistakes

**2. LLM-as-a-Judge Bias:**
- Shows LLM judges favor models similar to themselves
- Generalizes recent self-preference findings

**3. Weak-to-Strong Generalization:**
- Complementary knowledge between weak supervisor and strong student is crucial
- Similar models may not provide useful supervision

**4. Concerning Trend:**
Model mistakes are becoming more similar with increasing capabilities.

## Why This Matters

**Correlated failures:**
- If models make similar mistakes, using one model to oversee another won't catch errors
- AI oversight may systematically miss the same problems

**Implications for safety:**
- LLM-as-judge may be biased toward model's own failure modes
- Scalable oversight requires model diversity

## Claude Summary

This paper identifies a fundamental problem with AI oversight:

**The core issue**: As models converge in capability, they converge in mistakes too. This undermines using AI to oversee AI.

**Why model similarity matters**:
- Similar models make similar errors
- Judge models favor similar responses
- Weak-to-strong supervision requires complementary knowledge

**For AI safety**: If we plan to use AI for scalable oversight, we need to account for model similarity. Diverse models may be essential.

**Practical recommendation**: Report and correct for model similarity in AI oversight applications.

## Relevance

**Critical for scalable oversight research.** Identifies a fundamental limitation of using AI to supervise AI. Important for LLM-as-judge methodologies and weak-to-strong generalization research.
