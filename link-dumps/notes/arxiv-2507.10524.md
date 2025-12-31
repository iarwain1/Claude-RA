# Mixture-of-Recursions: Learning Dynamic Recursive Depths for Adaptive Token-Level Computation

**arXiv:** [2507.10524](https://arxiv.org/abs/2507.10524)
**Authors:** Sangmin Bae, Yujin Kim, Reza Bayat, Sungnyun Kim, Jiyoun Ha, et al. (11 total)
**Date:** 2025-07-14
**Categories:** cs.CL, cs.LG

## Abstract

Scaling language models unlocks impressive capabilities, but the accompanying computational and memory demands make both training and deployment expensive. Existing efficiency efforts typically target either parameter sharing or adaptive computation, leaving open the question of how to attain both simultaneously. We introduce Mixture-of-Recursions (MoR), a unified framework that combines the two axes of efficiency inside a single Recursive Transformer. MoR reuses a shared stack of layers across recursion steps to achieve parameter efficiency, while lightweight routers enable adaptive token-level thinking by dynamically assigning different recursion depths to individual tokens. This allows MoR to focus quadratic attention computation only among tokens still active at a given recursion depth, further improving memory access efficiency by selectively caching only their key-value pairs. Beyond these core mechanisms, we also propose a KV sharing variant that reuses KV pairs from the first recursion, specifically designed to further decrease memory footprint. Across model scales ranging from 135M to 1.7B parameters, MoR forms a new Pareto frontier: at equal training FLOPs and smaller model sizes, it significantly lowers validation perplexity and improves few-shot accuracy, while delivering higher throughput compared with vanilla and existing recursive baselines. These gains demonstrate that MoR is an effective path towards large-model quality without incurring large-model cost.

---
*Metadata fetched via arxiv API on 2025-12-31*
