# A Careful Examination of Large Language Model Performance on Grade School Arithmetic

**arXiv:** https://arxiv.org/abs/2405.00332
**Authors:** Hugh Zhang, Jeff Da, Dean Lee, Vaughn Robinson, Catherine Wu, Will Song, Tiffany Zhao, Pranav Raja, Charlotte Zhuang, Dylan Slack, Qin Lyu, Sean Hendryx, Russell Kaplan, Michele Lunati, Summer Yue (Scale AI)
**Date:** 2024-05-01 (v1), revised 2024-11-22 (v4)

## Abstract

Large language models (LLMs) have achieved impressive success on many benchmarks for mathematical reasoning. However, there is growing concern that some of this performance actually reflects dataset contamination, where data closely resembling benchmark questions leaks into the training data, instead of true reasoning ability.

To investigate this claim rigorously, they commissioned Grade School Math 1000 (GSM1k), designed to mirror the style and complexity of the established GSM8k benchmark, the gold standard for measuring elementary mathematical reasoning.

The authors ensured that the two benchmarks are comparable across important metrics such as human solve rates, number of steps in solution, answer magnitude, and more.

When evaluating leading open- and closed-source LLMs on GSM1k, they observed accuracy drops of up to 8%, with several families of models showing evidence of systematic overfitting across almost all model sizes.

## Claude Summary

GSM1k is a "clean" benchmark designed to detect contamination in GSM8k, the standard math reasoning benchmark. Key findings:

1. **Up to 8% accuracy drops**: Models perform worse on GSM1k vs GSM8k
2. **Systematic overfitting**: Multiple model families show signs across all sizes
3. **Contamination evidence**: Performance gaps suggest benchmark leakage

This paper provides important evidence that reported math reasoning progress may be inflated by contamination. It complements GSM-Symbolic (2410.05229) in questioning the validity of GSM8k as a reasoning measure.

Methodologically, creating matched "clean" benchmarks is a valuable approach for detecting contamination.

## Relevance

Critical for evaluation methodology. Provides evidence of benchmark contamination affecting reported AI capabilities. Important for understanding true vs. apparent progress in AI reasoning.
