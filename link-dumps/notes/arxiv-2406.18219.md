# A Closer Look into Mixture-of-Experts in Large Language Models

**arXiv:** [2406.18219](https://arxiv.org/abs/2406.18219)
**Authors:** Ka Man Lo, Zeyu Huang, Zihan Qiu, Zili Wang, Jie Fu
**Date:** 2024-06-26
**Categories:** cs.CL, cs.LG

## Abstract

Mixture-of-experts (MoE) is gaining increasing attention due to its unique properties and remarkable performance, especially for language tasks. By sparsely activating a subset of parameters for each token, MoE architecture could increase the model size without sacrificing computational efficiency, achieving a better trade-off between performance and training costs. However, the underlying mechanism of MoE still lacks further exploration, and its modularization degree remains questionable. In this paper, we make an initial attempt to understand the inner workings of MoE-based large language models. Concretely, we comprehensively study the parametric and behavioral features of three popular MoE-based models and reveal some intriguing observations, including 1) Neurons act like fine-grained experts; 2) The router of MoE usually selects experts with larger output norms; 3) The expert diversity increases as the layer increases, while the last layer is an outlier, which is further validated by an initial experiment. Based on the observations, we also provide suggestions for a broad spectrum of MoE practitioners, such as router design and expert allocation. We hope this work could shed light on future research on the MoE framework and other modular architectures. Code is available at https://github.com/kamanphoebe/Look-into-MoEs.

---
*Metadata fetched via arxiv API on 2025-12-31*
