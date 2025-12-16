# Mistral 7B

**arXiv:** https://arxiv.org/abs/2310.06825
**Authors:** Albert Q. Jiang, Alexandre Sablayrolles, Arthur Mensch, Chris Bamford, Devendra Singh Chaplot, et al. (Mistral AI)
**Date:** 2023-10-10
**License:** Apache 2.0

## Abstract

Mistral 7B is a 7-billion-parameter language model engineered for superior performance and efficiency.

- Outperforms Llama 2 13B across all benchmarks
- Outperforms Llama 1 34B in reasoning, math, and code

## Key Technical Innovations

1. **Grouped-Query Attention (GQA)**: Faster inference, reduced memory
2. **Sliding Window Attention (SWA)**: Handle arbitrary length sequences efficiently
3. **Theoretical attention span**: ~131K tokens with W=4096

## Key Results

- 7B model beats 13B Llama 2
- Mistral 7B Instruct beats Llama 2 13B Chat
- Apache 2.0 license (fully open)

## Claude Summary

Mistral 7B demonstrated that architectural innovations could match larger model performance:

**Efficiency focus**: GQA + SWA enable:
- Faster inference
- Lower memory
- Longer effective context

**Market impact**: Mistral AI quickly became a major player:
- Founded by ex-DeepMind/Meta researchers
- Raised significant funding
- Followed with Mixtral (MoE), Mistral Large

**Key insight**: 7B with smart architecture ≈ 13B with standard architecture

The success of Mistral showed that the open-source model race isn't just about scale.

## Relevance

Important for understanding efficient LLM architectures. Demonstrates that architectural innovations can substitute for scale. Key competitor in the open-source model space.
