# Dancing in Chains: Reconciling Instruction Following and Faithfulness in Language Models

**arXiv:** [2407.21417](https://arxiv.org/abs/2407.21417)
**Authors:** Zhengxuan Wu, Yuhao Zhang, Peng Qi, Yumo Xu, Rujun Han, et al. (9 total)
**Date:** 2024-07-31
**Categories:** cs.CL

## Abstract

Modern language models (LMs) need to follow human instructions while being faithful; yet, they often fail to achieve both. Here, we provide concrete evidence of a trade-off between instruction following (i.e., follow open-ended instructions) and faithfulness (i.e., ground responses in given context) when training LMs with these objectives. For instance, fine-tuning LLaMA-7B on instruction following datasets renders it less faithful. Conversely, instruction-tuned Vicuna-7B shows degraded performance at following instructions when further optimized on tasks that require contextual grounding. One common remedy is multi-task learning (MTL) with data mixing, yet it remains far from achieving a synergic outcome. We propose a simple yet effective method that relies on Rejection Sampling for Continued Self-instruction Tuning (ReSet), which significantly outperforms vanilla MTL. Surprisingly, we find that less is more, as training ReSet with high-quality, yet substantially smaller data (three-fold less) yields superior results. Our findings offer a better understanding of objective discrepancies in alignment training of LMs.

---
*Metadata fetched via arxiv API on 2025-12-31*
