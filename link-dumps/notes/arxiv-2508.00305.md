# Systematic Evaluation of Optimization Techniques for Long-Context Language Models

**arXiv:** [2508.00305](https://arxiv.org/abs/2508.00305)
**Authors:** Ammar Ahmed, Sheng Di, Franck Cappello, Zirui Liu, Jingoo Han, et al. (6 total)
**Date:** 2025-08-01
**Categories:** cs.CL, cs.LG, cs.PF

## Abstract

Large language models (LLMs) excel across diverse natural language processing tasks but face resource demands and limited context windows. Although techniques like pruning, quantization, and token dropping can mitigate these issues, their efficacy in long-context scenarios and system evaluation remains underexplored. This paper systematically benchmarks these optimizations, characterizing memory usage, latency, and throughput, and studies how these methods impact the quality of text generation. We first analyze individual optimization methods for two LLM architectures supporting long context and then systematically evaluate combinations of these techniques to assess how this deeper analysis impacts performance metrics. We subsequently study the scalability of individual optimization methods on a larger variant with 70 billion-parameter model. Our novel insights reveal that naive combination inference optimization algorithms can adversely affect larger models due to compounded approximation errors, as compared to their smaller counterparts. Experiments show that relying solely on F1 obscures these effects by hiding precision-recall trade-offs in question answering tasks. By integrating system-level profiling with task-specific insights, this study helps LLM practitioners and researchers explore and balance efficiency, accuracy, and scalability across tasks and hardware configurations.

---
*Metadata fetched via arxiv API on 2025-12-31*
