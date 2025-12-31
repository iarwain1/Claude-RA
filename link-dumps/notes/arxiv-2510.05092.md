# Learning to Interpret Weight Differences in Language Models

**arXiv:** [2510.05092](https://arxiv.org/abs/2510.05092)
**Authors:** Avichal Goel, Yoon Kim, Nir Shavit, Tony T. Wang
**Date:** 2025-10-06
**Categories:** cs.LG, cs.AI, cs.CL

## Abstract

Finetuning (pretrained) language models is a standard approach for updating their internal parametric knowledge and specializing them to new tasks and domains. However, the corresponding model weight changes ("weight diffs") are not generally interpretable. While inspecting the finetuning dataset can give a sense of how the model might have changed, these datasets are often not publicly available or are too large to work with directly. Towards the goal of comprehensively understanding weight diffs in natural language, we introduce Diff Interpretation Tuning (DIT), a method that trains models to describe their own finetuning-induced modifications. Our approach uses synthetic, labeled weight diffs to train a DIT-adapter, which can be applied to a compatible finetuned model to make it describe how it has changed. We demonstrate in two proof-of-concept settings (reporting hidden behaviors and summarizing finetuned knowledge) that our method enables models to describe their finetuning-induced modifications using accurate natural language descriptions.

---
*Metadata fetched via arxiv API on 2025-12-31*
