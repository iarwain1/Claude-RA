# Are We Done with MMLU?

**arXiv:** https://arxiv.org/abs/2406.04127
**Authors:** Aryo Pradipta Gema, Joshua Ong Jun Leang, Giwon Hong, Alessio Devoto, Alberto Carlo Maria Mancino, Rohit Saxena, Xuanli He, Yu Zhao, Xiaotang Du, Mohammad Reza Ghasemi Madani, Claire Barale, Robert McHardy, Joshua Harris, Jean Kaddour, Emile van Krieken, Pasquale Minervini
**Date:** 2024-06

## Abstract

MMLU (Massive Multitask Language Understanding) has become one of the most popular benchmarks for evaluating large language models. However, this paper conducts a detailed analysis revealing significant quality issues with the benchmark.

## Key Findings

**Error Analysis Results:**
- Significant portion of questions contain errors
- Incorrect ground truth labels
- Ambiguous questions with multiple valid answers
- Poorly worded questions

**MMLU-Redux:**
The authors propose a corrected subset that addresses identified issues through manual review and fixes.

## Types of Issues Found

1. **Wrong ground truth**: Labeled answer is incorrect
2. **Ambiguous questions**: Multiple valid interpretations
3. **Missing information**: Questions lack needed context
4. **Outdated information**: Questions based on old data

## Claude Summary

This paper is an important critique of one of the most widely used LLM benchmarks:

**Why this matters**:
- MMLU scores are frequently cited for model comparisons
- Leaderboard rankings influence research and deployment decisions
- Errors in the benchmark can mislead progress assessment

**Implications**:
- Small differences in MMLU scores may be meaningless
- Need for more careful benchmark construction
- Community should consider MMLU-Redux or other alternatives

**Broader lesson**: Benchmark quality directly affects our ability to measure progress. A flawed benchmark can lead to optimizing for the wrong things.

## Relevance

Critical for anyone using MMLU to evaluate models. Part of growing literature on benchmark quality and evaluation methodology. Relevant to discussions about how we measure AI progress and capabilities.
