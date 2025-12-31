# Idiosyncrasies in Large Language Models

**arXiv:** [2502.12150](https://arxiv.org/abs/2502.12150)
**Authors:** Mingjie Sun, Yida Yin, Zhiqiu Xu, J. Zico Kolter, Zhuang Liu
**Date:** 2025-02-17
**Categories:** cs.CL

## Abstract

In this work, we unveil and study idiosyncrasies in Large Language Models (LLMs) -- unique patterns in their outputs that can be used to distinguish the models. To do so, we consider a simple classification task: given a particular text output, the objective is to predict the source LLM that generates the text. We evaluate this synthetic task across various groups of LLMs and find that simply fine-tuning text embedding models on LLM-generated texts yields excellent classification accuracy. Notably, we achieve 97.1% accuracy on held-out validation data in the five-way classification problem involving ChatGPT, Claude, Grok, Gemini, and DeepSeek. Our further investigation reveals that these idiosyncrasies are rooted in word-level distributions. These patterns persist even when the texts are rewritten, translated, or summarized by an external LLM, suggesting that they are also encoded in the semantic content. Additionally, we leverage LLM as judges to generate detailed, open-ended descriptions of each model's idiosyncrasies. Finally, we discuss the broader implications of our findings, including training on synthetic data, inferring model similarity, and robust evaluation of LLMs. Code is available at https://github.com/locuslab/llm-idiosyncrasies.

---
*Metadata fetched via arxiv API on 2025-12-31*
