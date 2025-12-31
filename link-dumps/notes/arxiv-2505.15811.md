# On the creation of narrow AI: hierarchy and nonlocality of neural network skills

**arXiv:** [2505.15811](https://arxiv.org/abs/2505.15811)
**Authors:** Eric J. Michaud, Asher Parker-Sartori, Max Tegmark
**Date:** 2025-05-21
**Categories:** cs.LG

## Abstract

We study the problem of creating strong, yet narrow, AI systems. While recent AI progress has been driven by the training of large general-purpose foundation models, the creation of smaller models specialized for narrow domains could be valuable for both efficiency and safety. In this work, we explore two challenges involved in creating such systems, having to do with basic properties of how neural networks learn and structure their representations. The first challenge regards when it is possible to train narrow models from scratch. Through experiments on a synthetic task, we find that it is sometimes necessary to train networks on a wide distribution of data to learn certain narrow skills within that distribution. This effect arises when skills depend on each other hierarchically, and training on a broad distribution introduces a curriculum which substantially accelerates learning. The second challenge regards how to transfer particular skills from large general models into small specialized models. We find that model skills are often not perfectly localized to a particular set of prunable components. However, we find that methods based on pruning can still outperform distillation. We investigate the use of a regularization objective to align desired skills with prunable components while unlearning unnecessary skills.

---
*Metadata fetched via arxiv API on 2025-12-31*
