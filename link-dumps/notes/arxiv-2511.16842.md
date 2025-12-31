# Fantastic Bugs and Where to Find Them in AI Benchmarks

**arXiv:** [2511.16842](https://arxiv.org/abs/2511.16842)
**Authors:** Sang Truong, Yuheng Tu, Michael Hardy, Anka Reuel, Zeyu Tang, et al. (11 total)
**Date:** 2025-11-20
**Categories:** cs.AI, cs.CL, cs.LG

## Abstract

Benchmarks are pivotal in driving AI progress, and invalid benchmark questions frequently undermine their reliability. Manually identifying and correcting errors among thousands of benchmark questions is not only infeasible but also a critical bottleneck for reliable evaluation. In this work, we introduce a framework for systematic benchmark revision that leverages statistical analysis of response patterns to flag potentially invalid questions for further expert review. Our approach builds on a core assumption commonly used in AI evaluations that the mean score sufficiently summarizes model performance. This implies a unidimensional latent construct underlying the measurement experiment, yielding expected ranges for various statistics for each item. When empirically estimated values for these statistics fall outside the expected range for an item, the item is more likely to be problematic. Across nine widely used benchmarks, our method guides expert review to identify problematic questions with up to 84\% precision. In addition, we introduce an LLM-judge first pass to review questions, further reducing human effort. Together, these components provide an efficient and scalable framework for systematic benchmark revision.

---
*Metadata fetched via arxiv API on 2025-12-31*
