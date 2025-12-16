# Noise Contrastive Alignment of Language Models with Explicit Rewards

**arXiv:** https://arxiv.org/abs/2402.05369
**Authors:** Huayu Chen, Guande He, Lifan Yuan, Ganqu Cui, Hang Su, Jun Zhu
**Date:** 2024-02-08 (v1), revised 2024-10-30 (v3)

## Abstract

User intentions are typically formalized as evaluation rewards to be maximized when fine-tuning language models (LMs). Existing alignment methods, such as Direct Preference Optimization (DPO), are mainly tailored for pairwise preference data where rewards are implicitly defined rather than explicitly given.

This paper introduces a general framework for LM alignment, leveraging Noise Contrastive Estimation (NCE) to bridge the gap in handling reward datasets explicitly annotated with scalar evaluations.

The framework comprises two parallel algorithms:
- **NCA**: Noise Contrastive Alignment
- **InfoNCA**: Information-theoretic variant

Both enable the direct extraction of an LM policy from reward data as well as preference data. The paper also shows that the DPO loss is a special case of their proposed InfoNCA objective under pairwise preference settings.

## Claude Summary

This paper extends alignment methods beyond pairwise preferences (DPO) to handle explicit scalar rewards. This is useful because:

1. Not all feedback comes as pairwise comparisons
2. Scalar rewards are more informative than binary preferences
3. Unifies preference and reward-based alignment

The NCE framework provides theoretical grounding and shows DPO as a special case. This contributes to the technical foundations of RLHF-style alignment.

## Relevance

Important for AI alignment methodology. Extends the toolkit for training LLMs from human feedback beyond standard preference-based approaches.
