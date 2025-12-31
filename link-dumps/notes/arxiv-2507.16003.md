# Learning without training: The implicit dynamics of in-context learning

**arXiv:** [2507.16003](https://arxiv.org/abs/2507.16003)
**Authors:** Benoit Dherin, Michael Munn, Hanna Mazzawi, Michael Wunder, Javier Gonzalvo
**Date:** 2025-07-21
**Categories:** cs.CL, cs.LG

## Abstract

One of the most striking features of Large Language Models (LLMs) is their ability to learn in-context. Namely at inference time an LLM is able to learn new patterns without any additional weight update when these patterns are presented in the form of examples in the prompt, even if these patterns were not seen during training. The mechanisms through which this can happen are still largely unknown. In this work, we show that the stacking of a self-attention layer with an MLP, allows the transformer block to implicitly modify the weights of the MLP layer according to the context. We argue through theory and experimentation that this simple mechanism may be the reason why LLMs can learn in-context and not only during training. Specifically, we show how a transformer block implicitly transforms a context into a low-rank weight-update of its MLP layer.

---
*Metadata fetched via arxiv API on 2025-12-31*
