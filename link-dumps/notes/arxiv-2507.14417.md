# Inverse Scaling in Test-Time Compute

**arXiv:** [2507.14417](https://arxiv.org/abs/2507.14417)
**Authors:** Aryo Pradipta Gema, Alexander Hägele, Runjin Chen, Andy Arditi, Jacob Goldman-Wetzler, et al. (14 total)
**Date:** 2025-07-19
**Categories:** cs.AI, cs.CL

## Abstract

We construct evaluation tasks where extending the reasoning length of Large Reasoning Models (LRMs) deteriorates performance, exhibiting an inverse scaling relationship between test-time compute and accuracy. Our evaluation tasks span four categories: simple counting tasks with distractors, regression tasks with spurious features, deduction tasks with constraint tracking, and advanced AI risks. We identify five distinct failure modes when models reason for longer: 1) Claude models become increasingly distracted by irrelevant information; 2) OpenAI o-series models resist distractors but overfit to problem framings; 3) models shift from reasonable priors to spurious correlations; 4) all models show difficulties in maintaining focus on complex deductive tasks; and 5) extended reasoning may amplify concerning behaviors, with Claude Sonnet 4 showing increased expressions of self-preservation. These findings suggest that while test-time compute scaling remains promising for improving model capabilities, it may inadvertently reinforce problematic reasoning patterns. Our results demonstrate the importance of evaluating models across diverse reasoning lengths to identify and address these failure modes in LRMs.

---
*Metadata fetched via arxiv API on 2025-12-31*
