# Chain-of-Thought Prompting Elicits Reasoning in Large Language Models

**arXiv:** https://arxiv.org/abs/2201.11903
**Authors:** Jason Wei, Xuezhi Wang, Dale Schuurmans, Maarten Bosma, Brian Ichter, Fei Xia, Ed Chi, Quoc Le, Denny Zhou (Google Brain)
**Date:** 2022-01-28 (v1), revised 2023-01-10 (v6)
**Venue:** NeurIPS 2022

## Abstract

This paper explores how generating a chain of thought -- a series of intermediate reasoning steps -- significantly improves the ability of large language models to perform complex reasoning.

The authors show how such reasoning abilities emerge naturally in sufficiently large language models via a simple method called chain of thought prompting, where a few chain of thought demonstrations are provided as exemplars in prompting.

Experiments on three large language models show that chain of thought prompting improves performance on a range of arithmetic, commonsense, and symbolic reasoning tasks.

## Key Results

The empirical gains can be striking:
- Prompting a 540B-parameter language model with just eight chain of thought exemplars achieves state of the art accuracy on the GSM8K benchmark of math word problems

## Claude Summary

Chain-of-Thought (CoT) is one of the most influential prompting papers, demonstrating that LLMs can reason better when prompted to show their work:

**Key insight**: Including step-by-step reasoning examples in prompts dramatically improves performance on reasoning tasks.

**Emergent ability**: CoT benefits only appear in large models (~100B+ parameters), suggesting reasoning capabilities emerge at scale.

**Simple technique**: Just add "Let's think step by step" or provide worked examples - no model changes needed.

**Impact**: Spawned an entire field of prompting research (ToT, GoT, self-consistency, etc.) and changed how people interact with LLMs.

## Relevance

**Foundational for prompting research.** Understanding CoT is essential for effective LLM use. The paper established that prompting can unlock latent capabilities.
