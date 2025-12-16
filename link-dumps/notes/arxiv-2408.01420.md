# Mission Impossible: A Statistical Perspective on Jailbreaking LLMs

**arXiv:** https://arxiv.org/abs/2408.01420
**Authors:** Jingtong Su, Julia Kempe, Karen Ullrich
**Date:** 2024-08-02

## Abstract

LLMs are trained on text data with limited quality control, leading to potential unintended or harmful behaviors. Preference alignment (e.g., RLHF) fine-tunes LLMs with carefully crafted examples of desired behavior.

**Problem**: Even aligned LLMs can be jailbroken through adversarial input modifications.

This paper provides theoretical insights into preference alignment and jailbreaking from a statistical perspective.

## Key Contribution: E-RLHF

A simple modification to RLHF called **E-RLHF** (Expected RLHF) that aims to increase the likelihood of safe responses.

**Results**: E-RLHF outperforms RLHF on all alignment problems from AdvBench and HarmBench without sacrificing model performance.

## Theoretical Insights

The paper analyzes:
- Why jailbreaking works from a statistical perspective
- What properties of alignment make models vulnerable
- How to modify training to reduce vulnerability

## Statistical Perspective

**Key insight**: Standard RLHF optimizes for expected reward but doesn't explicitly minimize the probability of harmful outputs. E-RLHF addresses this by focusing on the tail of the distribution.

## Claude Summary

This paper takes a principled approach to understanding jailbreaking:

**Why theory matters**: Most jailbreaking research is empirical (find attacks, test defenses). This paper asks: what properties of alignment mathematically determine vulnerability?

**Practical contribution**: E-RLHF is a drop-in replacement for RLHF that improves robustness without hurting performance. This is rare - usually robustness comes at a cost.

**Limitations**: The theory relies on assumptions that may not hold in practice. Empirical validation is limited to specific benchmarks.

**Connection to safety**: Understanding why jailbreaking works can inform more robust alignment approaches.

## Relevance

Important for understanding alignment from first principles. Provides both theoretical framework and practical improvement. Useful for researchers working on robust alignment and jailbreak defenses.
