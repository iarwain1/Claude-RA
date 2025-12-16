# GaLore: Memory-Efficient LLM Training by Gradient Low-Rank Projection

**arXiv:** https://arxiv.org/abs/2403.02436
**Authors:** Jiawei Zhao, Zhenyu Zhang, Beidi Chen, Zhangyang Wang, Anima Anandkumar, Yuandong Tian
**Date:** 2024-03

## Abstract

GaLore (Gradient Low-Rank Projection) is a training strategy that allows full-parameter learning while being more memory-efficient than common low-rank adaptation methods like LoRA. The key idea is to project gradients into a low-rank space during training, which significantly reduces memory usage for optimizer states while still enabling training of all model parameters.

The method demonstrates that pre-training a 7B parameter LLaMA model can be done on consumer GPUs with 24GB memory without model parallelism, checkpointing, or offloading strategies.

## Claude Summary

GaLore addresses a critical bottleneck in LLM training: memory consumption from optimizer states (which can be 2-3x the model size for Adam).

**Key insight**: During training, gradients are approximately low-rank. By projecting gradients to low-rank subspaces, you can maintain low-rank optimizer states while still updating all parameters.

**Advantages over LoRA**:
- Full-parameter learning (not just adapter weights)
- No architectural changes
- Better performance potential

**Practical impact**: 7B model training on consumer 24GB GPUs opens LLM pre-training to researchers without access to large GPU clusters.

## Relevance

Important for democratizing LLM training. May enable more diverse model development outside large labs. Relevant for understanding efficient training techniques.
