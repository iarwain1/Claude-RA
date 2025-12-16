# AI Agents That Matter

**arXiv:** https://arxiv.org/abs/2407.01502
**Authors:** Sayash Kapoor, Benedikt Stroebl, Zachary S. Siegel, Nitya Nadgir, Arvind Narayanan (Princeton)
**Date:** 2024-07-01
**Website:** https://agents.cs.princeton.edu/

## Abstract

This paper rethinks evaluations and benchmarks to build AI agents that are useful in the real world. The analysis reveals several shortcomings in current agent benchmarks and evaluation practices that hinder real-world usefulness.

## Key Problems Identified

1. **Narrow focus on accuracy**: No attention to other metrics like cost
2. **SOTA agents are needlessly complex and costly**: Community has reached mistaken conclusions about accuracy gains
3. **Inadequate holdout sets**: Leads to fragile agents that overfit
4. **Lack of standardization**: Pervasive lack of reproducibility

## Key Findings

**Cost-controlled evaluations needed:**
- Simple approaches outperform many SOTA complex agent architectures on HumanEval while costing much less
- Without cost control, researchers develop extremely costly agents just to top leaderboards

**Joint optimization of accuracy and cost:**
- Visualizing results as Pareto curve opens new design space
- Modified DSPy framework lowered cost while maintaining accuracy on HotPotQA

**Overfitting is pervasive:**
- Agents take shortcuts specific to benchmarks
- Need principled framework for avoiding overfitting

## Distinct Benchmarking Needs

Model developers vs. downstream developers need different benchmarks. Case study of NovelQA shows how evaluation-focused benchmarks can differ from application-focused ones.

## Claude Summary

This paper is essential reading for anyone working on LLM agents:

**Core message**: The agent community is optimizing for the wrong things. Accuracy-only leaderboards incentivize complex, expensive agents that don't transfer to real-world use.

**Practical implications**:
- Always report cost alongside accuracy
- Consider Pareto frontiers, not just top scores
- Simpler agents may be better for production

**Methodological contribution**: Framework for cost-controlled evaluation and joint optimization that could improve agent research.

## Relevance

Critical for AI agent research and deployment. Provides principled critique of current practices and concrete recommendations. From a well-respected group (Narayanan's team has done similar critiques in ML evaluation more broadly).
