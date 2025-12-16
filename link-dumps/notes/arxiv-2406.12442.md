# Abstraction-of-Thought Makes Language Models Better Reasoners

**arXiv:** https://arxiv.org/abs/2406.12442
**Authors:** Ruixin Hong, Hongming Zhang, Xiaoman Pan, Dong Yu, Changshui Zhang
**Date:** 2024-06-18 (v1), revised 2024-09-26 (v2)

## Abstract

Abstract reasoning, the ability to reason from the abstract essence of a problem, serves as a key to generalization in human reasoning. However, eliciting language models to perform reasoning with abstraction remains unexplored.

This paper seeks to bridge this gap by introducing a novel structured reasoning format called Abstraction-of-Thought (AoT). The uniqueness of AoT lies in its explicit requirement for varying levels of abstraction within the reasoning process. This approach could elicit language models to first contemplate on the abstract level before incorporating concrete details, which is overlooked by the prevailing step-by-step Chain-of-Thought (CoT) method.

To align models with the AoT format, they present AoT Collection, a generic finetuning dataset consisting of 348k high-quality samples with AoT reasoning processes, collected via an automated and scalable pipeline.

## Claude Summary

Abstraction-of-Thought (AoT) proposes moving beyond flat chain-of-thought reasoning to hierarchical abstraction. The key insight: humans don't just reason step-by-step; they also move between levels of abstraction.

Key contributions:
1. **AoT Format**: Structured reasoning that explicitly requires abstraction levels
2. **AoT Collection**: 348k training samples for aligning models to this format
3. **Improved generalization**: Abstract-first reasoning may improve transfer

This connects to the broader question of how to elicit better reasoning from LLMs and whether current prompting techniques capture the full range of human reasoning strategies.

## Relevance

Relevant for AI capabilities research and reasoning improvement. May inform evaluation design - testing both concrete and abstract reasoning. Interesting for understanding the space of possible reasoning strategies.
