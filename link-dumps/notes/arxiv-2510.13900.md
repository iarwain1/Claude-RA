# Narrow Finetuning Leaves Clearly Readable Traces in Activation Differences

**arXiv:** [2510.13900](https://arxiv.org/abs/2510.13900)
**Authors:** Julian Minder, Clément Dumas, Stewart Slocum, Helena Casademunt, Cameron Holmes, et al. (7 total)
**Date:** 2025-10-14
**Categories:** cs.CL, cs.AI

## Abstract

Finetuning on narrow domains has become an essential tool to adapt Large Language Models (LLMs) to specific tasks and to create models with known unusual properties that are useful for research. We show that narrow finetuning creates strong biases in LLM activations that can be interpreted to understand the finetuning domain. These biases can be discovered using simple tools from model diffing - the study of differences between models before and after finetuning. In particular, analyzing activation differences on the first few tokens of random text and steering by adding this difference to the model activations produces text similar to the format and general content of the finetuning data. We demonstrate that these analyses contain crucial information by creating an LLM-based interpretability agent to understand the finetuning domain. With access to the bias, the agent performs significantly better compared to baseline agents using simple prompting. Our analysis spans synthetic document finetuning for false facts, emergent misalignment, subliminal learning, and taboo word guessing game models across different architectures (Gemma, LLaMA, Qwen) and scales (1B to 32B parameters). We suspect these biases reflect overfitting and find that mixing pretraining data into the finetuning corpus largely removes them, though residual risks may remain. Our work (1) demonstrates that narrowly finetuned models have salient traces of their training objective in their activations and suggests ways to improve how they are trained, (2) warns AI safety and interpretability researchers that the common practice of using such models as a proxy for studying broader finetuning (e.g., chat-tuning) might not be realistic, and (3) highlights the need for deeper investigation into the effects of narrow finetuning and development of truly realistic case studies for model-diffing, safety and interpretability research.

---
*Metadata fetched via arxiv API on 2025-12-31*
