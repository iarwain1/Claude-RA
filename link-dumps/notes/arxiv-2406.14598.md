# SORRY-Bench: Systematically Evaluating Large Language Model Safety Refusal

**arXiv:** https://arxiv.org/abs/2406.14598
**Authors:** Tinghao Xie, Xiangyu Qi, Yi Zeng, Yangsibo Huang, Udari Madhushani Sehwag, Kaixuan Huang, Luxi He, Boyi Wei, Dacheng Li, Ying Sheng, Ruoxi Jia, Bo Li, Kai Li, Danqi Chen, Peter Henderson, Prateek Mittal
**Date:** 2024-06-20 (v1), revised 2025-03-01 (v2)

## Abstract

Evaluating aligned large language models' (LLMs) ability to recognize and reject unsafe user requests is crucial for safe, policy-compliant deployments. Existing evaluation efforts face three limitations that SORRY-Bench addresses:

1. **Coarse-grained taxonomies**: Existing methods over-represent some topics. Among ten evaluated datasets, self-harm instruction refusals are 3x less represented than fraudulent activities tests.

2. **Linguistic diversity overlooked**: Different languages, dialects, and formatting are only implicitly considered.

SORRY-Bench improvements:
- Fine-grained taxonomy of 44 potentially unsafe topics
- 440 class-balanced unsafe instructions
- Human-in-the-loop compilation methods

## Claude Summary

SORRY-Bench addresses critical gaps in LLM safety refusal evaluation:

**Problem**: Current safety benchmarks have uneven coverage - some harm categories are tested 3x more than others, creating blind spots in safety assessment.

**Solution**: A balanced, fine-grained benchmark with:
- 44 unsafe topic categories (vs. coarse categories in prior work)
- 440 balanced test cases
- Explicit consideration of linguistic variation

This is important because:
- Imbalanced testing creates false confidence in safety
- Real attacks will target under-tested categories
- Policy compliance requires comprehensive coverage

Strong author team from Princeton, Berkeley, etc.

## Relevance

Essential for AI safety evaluation. Provides better methodology for assessing LLM refusal capabilities. Useful for comparing model safety and identifying coverage gaps.
