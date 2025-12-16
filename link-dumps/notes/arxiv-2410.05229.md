# GSM-Symbolic: Understanding the Limitations of Mathematical Reasoning in Large Language Models

**arXiv:** https://arxiv.org/abs/2410.05229
**Authors:** Iman Mirzadeh, Keivan Alizadeh, Hooman Shahrokhi, Oncel Tuzel, Samy Bengio, Mehrdad Farajtabar (Apple)
**Date:** 2024-10-07 (v1), revised 2025-08-27 (v2)
**Venue:** ICLR 2025

## Abstract

Recent advancements in Large Language Models (LLMs) have sparked interest in their formal reasoning capabilities, particularly in mathematics. The GSM8K benchmark is widely used to assess the mathematical reasoning of models on grade-school-level questions. While the performance of LLMs on GSM8K has significantly improved in recent years, it remains unclear whether their mathematical reasoning capabilities have genuinely advanced, raising questions about the reliability of the reported metrics.

To address these concerns, the authors conduct a large-scale study on several SOTA open and closed models and introduce GSM-Symbolic, an improved benchmark created from symbolic templates that allow for the generation of a diverse set of questions.

## Claude Summary

This Apple research paper challenges the validity of GSM8K as a reasoning benchmark. By creating GSM-Symbolic with templatized questions, they can generate variations that test whether models truly reason or merely pattern-match to training data.

Key finding: Models show significant performance variance on semantically equivalent problems with different surface forms, suggesting benchmark contamination and pattern matching rather than genuine mathematical reasoning.

This is important methodological work showing that benchmark saturation doesn't necessarily indicate capability improvement - a critical insight for AI capability evaluation.

## Relevance

Essential for understanding benchmark validity and the difference between apparent and genuine AI capabilities. Directly relevant to AI evaluation methodology and the construct validity concerns raised in other evaluation papers.

## Resources

- GitHub: https://github.com/apple/ml-gsm-symbolic
