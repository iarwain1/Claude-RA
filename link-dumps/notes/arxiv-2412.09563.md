# Does Representation Matter? Exploring Intermediate Layers in Large Language Models

**arXiv:** https://arxiv.org/abs/2412.09563
**Authors:** Oscar Skean, Md Rifat Arefin, Yann LeCun, Ravid Shwartz-Ziv
**Date:** 2024-12-12

## Abstract

Understanding what defines a good representation in large language models (LLMs) is fundamental to both theoretical understanding and practical applications. In this paper, the authors investigate the quality of intermediate representations in various LLM architectures, including Transformers and State Space Models (SSMs).

They find that intermediate layers often yield more informative representations for downstream tasks than the final layers. To measure representation quality, they adapt and apply a suite of metrics—such as prompt entropy, curvature, and augmentation-invariance—originally proposed in other contexts.

Their empirical study reveals significant architectural differences, how representations evolve throughout training, and how factors like input randomness and prompt length affect each layer. Notably, they observe a bimodal pattern in the entropy of some intermediate layers and consider potential explanations tied to training data.

## Claude Summary

This Yann LeCun co-authored paper provides empirical analysis of where "good" representations live in LLMs. Key findings:

1. **Intermediate > Final layers**: Middle layers often have more informative representations than final layers for downstream tasks
2. **Architectural differences**: Transformers vs SSMs show different representation patterns
3. **Training dynamics**: How representations evolve through training
4. **Bimodal entropy**: Some layers show bimodal entropy patterns

The metrics used (prompt entropy, curvature, augmentation-invariance) provide quantitative tools for analyzing representation quality.

## Relevance

Important for interpretability research - suggests looking at intermediate layers rather than just final outputs. Useful for understanding where semantic information is encoded in LLMs.
