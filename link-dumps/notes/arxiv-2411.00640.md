# Adding Error Bars to Evals: A Statistical Approach to Language Model Evaluations

**arXiv:** [2411.00640](https://arxiv.org/abs/2411.00640)
**Authors:** Evan Miller
**Date:** 2024-11-01

## Abstract

Evaluations are critical for understanding the capabilities of large language models (LLMs). Fundamentally, evaluations are experiments; but the literature on evaluations has largely ignored the literature from other sciences on experiment analysis and planning.

This article shows researchers with some training in statistics how to think about and analyze data from language model evaluations. Conceptualizing evaluation questions as having been drawn from an unseen super-population, we present formulas for analyzing evaluation data, measuring differences between two models, and planning an evaluation experiment.

We make a number of specific recommendations for running language model evaluations and reporting experiment results in a way that minimizes statistical noise and maximizes informativeness.

## Claude Summary

This paper addresses a significant gap in LLM evaluation methodology by bringing statistical rigor from other scientific fields to AI benchmarking. The key contribution is treating evaluation questions as samples from a population, which allows proper statistical inference about model capabilities. This is important because many evaluation papers report benchmark scores without proper error bars or statistical significance testing.

**Key takeaways:**
- Evaluations should be treated as statistical experiments with proper experimental design
- Error bars and confidence intervals should be standard in evaluation reporting
- Sample size planning matters for detecting meaningful differences between models
