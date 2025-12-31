# Large Language Models Must Be Taught to Know What They Don't Know

**arXiv:** [2406.08391](https://arxiv.org/abs/2406.08391)
**Authors:** Sanyam Kapoor, Nate Gruver, Manley Roberts, Katherine Collins, Arka Pal, et al. (10 total)
**Date:** 2024-06-12
**Categories:** cs.LG, cs.AI, cs.CL

## Abstract

When using large language models (LLMs) in high-stakes applications, we need to know when we can trust their predictions. Some works argue that prompting high-performance LLMs is sufficient to produce calibrated uncertainties, while others introduce sampling methods that can be prohibitively expensive. In this work, we first argue that prompting on its own is insufficient to achieve good calibration and then show that fine-tuning on a small dataset of correct and incorrect answers can create an uncertainty estimate with good generalization and small computational overhead. We show that a thousand graded examples are sufficient to outperform baseline methods and that training through the features of a model is necessary for good performance and tractable for large open-source models when using LoRA. We also investigate the mechanisms that enable reliable LLM uncertainty estimation, finding that many models can be used as general-purpose uncertainty estimators, applicable not just to their own uncertainties but also the uncertainty of other models. Lastly, we show that uncertainty estimates inform human use of LLMs in human-AI collaborative settings through a user study.

---
*Metadata fetched via arxiv API on 2025-12-31*
