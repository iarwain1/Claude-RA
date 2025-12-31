# Machine Unlearning Fails to Remove Data Poisoning Attacks

**arXiv:** [2406.17216](https://arxiv.org/abs/2406.17216)
**Authors:** Martin Pawelczyk, Jimmy Z. Di, Yiwei Lu, Ayush Sekhari, Gautam Kamath, et al. (6 total)
**Date:** 2024-06-25
**Categories:** cs.LG, cs.AI, cs.CR

## Abstract

We revisit the efficacy of several practical methods for approximate machine unlearning developed for large-scale deep learning. In addition to complying with data deletion requests, one often-cited potential application for unlearning methods is to remove the effects of poisoned data. We experimentally demonstrate that, while existing unlearning methods have been demonstrated to be effective in a number of settings, they fail to remove the effects of data poisoning across a variety of types of poisoning attacks (indiscriminate, targeted, and a newly-introduced Gaussian poisoning attack) and models (image classifiers and LLMs); even when granted a relatively large compute budget. In order to precisely characterize unlearning efficacy, we introduce new evaluation metrics for unlearning based on data poisoning. Our results suggest that a broader perspective, including a wider variety of evaluations, are required to avoid a false sense of confidence in machine unlearning procedures for deep learning without provable guarantees. Moreover, while unlearning methods show some signs of being useful to efficiently remove poisoned data without having to retrain, our work suggests that these methods are not yet ``ready for prime time,'' and currently provide limited benefit over retraining.

---
*Metadata fetched via arxiv API on 2025-12-31*
