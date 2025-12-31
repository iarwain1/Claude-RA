# Time Matters: Scaling Laws for Any Budget

**arXiv:** [2406.18922](https://arxiv.org/abs/2406.18922)
**Authors:** Itay Inbar, Luke Sernau
**Date:** 2024-06-27
**Categories:** cs.LG, cs.AI

## Abstract

A primary cost driver for training large models is wall-clock training time. We show that popular time estimates based on FLOPs are poor estimates, and construct a more accurate proxy based on memory copies. This allows us to accurately estimate the training speed of a transformer model from its hyperparameters. Combined with a scaling law curve like Chinchilla, this allows us to accurately predict the final loss of a model from a simple equation. We show that this expression is accurate across a wide range of model hyperparameter values, enabling us to analytically make architectural decisions and train models more efficiently. Crucially, this analysis predicts that in contrast to existing literature, models should be wider rather than deeper, as the benefits of speed outweigh the benefits of depth.

---
*Metadata fetched via arxiv API on 2025-12-31*
