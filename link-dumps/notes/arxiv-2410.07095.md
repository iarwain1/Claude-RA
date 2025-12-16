# MLE-bench: Evaluating Machine Learning Agents on Machine Learning Engineering

**arXiv:** https://arxiv.org/abs/2410.07095
**Authors:** Jun Shern Chan, Neil Chowdhury, Oliver Jaffe, James Aung, Dane Sherburn, Evan Mays, Giulio Starace, Kevin Liu, Leon Maksin, Tejal Patwardhan, Lilian Weng, Aleksander Mądry (OpenAI)
**Date:** 2024-10-09 (v1), revised 2025-02-26 (v6)
**Venue:** ICLR 2025

## Abstract

MLE-bench is a benchmark for measuring how well AI agents perform at machine learning engineering. The authors curate 75 ML engineering-related competitions from Kaggle, creating a diverse set of challenging tasks that test real-world ML engineering skills such as training models, preparing datasets, and running experiments.

They establish human baselines for each competition using Kaggle's publicly available leaderboards. The best-performing setup—OpenAI's o1-preview with AIDE scaffolding—achieves at least the level of a Kaggle bronze medal in 16.9% of competitions.

In addition to the main results, the authors investigate various forms of resource scaling for AI agents and the impact of contamination from pre-training.

## Claude Summary

MLE-bench is an important capability benchmark from OpenAI that evaluates AI agents on realistic ML engineering tasks. Using real Kaggle competitions provides authentic difficulty calibration against human performance.

Key findings:
- Best AI setup (o1-preview + AIDE) achieves bronze-level performance on ~17% of tasks
- Significant gap remains between AI and expert human ML engineers
- Resource scaling and contamination effects are analyzed

This benchmark is useful for tracking progress toward AI systems that can autonomously conduct ML research - a capability with significant implications for AI development acceleration.

## Relevance

Important capability benchmark for AI agents. Relevant for understanding current limitations of AI in complex technical domains. Useful for tracking dangerous capability thresholds (autonomous AI research).

## Resources

- GitHub: https://github.com/openai/mle-bench/
