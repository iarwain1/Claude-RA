# Judging the Judges: Evaluating Alignment and Vulnerabilities in LLMs-as-Judges

**arXiv:** https://arxiv.org/abs/2406.12624
**Authors:** Aman Singh Thakur, Kartik Choudhary, Venkat Srinik Ramayapally, Sankaran Vaidyanathan, Dieuwke Hupkes (UMass, Meta)
**Date:** 2024-06-18
**GitHub:** https://github.com/UMass-Meta-LLM-Eval/llm_eval

## Abstract

The LLM-as-a-judge paradigm offers a promising solution to scalability challenges of human evaluation. However, there are open questions about its strengths, weaknesses, and potential biases.

This paper presents a comprehensive study of various LLMs acting as judges:
- 13 judge models of different sizes and families
- 9 "examtaker" models (base and instruction-tuned)
- Controlled scenario with high inter-human agreement

## Key Findings

**Alignment with humans:**
- Only the best (largest) models achieve reasonable alignment
- Still quite far behind inter-human agreement
- Scores may differ by up to 5 points from human-assigned scores
- Only GPT-4 and LLaMA-3 70B perform well among those tested

**Vulnerabilities identified:**
- Sensitivity to prompt complexity and length
- Tendency toward leniency
- Scores from 80%+ aligned judges can be 20 points apart

**Metrics insight:**
- Cohen's kappa is superior metric for evaluation
- Most aligned in scores ≠ most discriminative
- Some poorly-aligned judges (JudgeLM-7B) outperform in ranking because biases are systematic

## Claude Summary

This paper provides rigorous empirical grounding for the LLM-as-judge paradigm:

**Key takeaways**:
- Don't assume LLM judges are reliable - validate for your use case
- Larger models are better, but still imperfect
- Consider what you're optimizing: absolute scores vs. rankings

**Practical implications**:
- Using LLM judges introduces systematic biases
- Multiple judges may be needed for reliability
- Human validation remains important

**Methodological contribution**: The distinction between score alignment and ranking ability is important - a biased but consistent judge may be useful for comparisons even if absolute scores are unreliable.

## Relevance

Critical for anyone using LLM-as-judge evaluation. Documents concrete limitations that should inform evaluation methodology. Useful for researchers designing evaluation pipelines and for interpreting results from existing LLM-based evaluations.
