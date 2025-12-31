# None of the Others: a General Technique to Distinguish Reasoning from Memorization in Multiple-Choice LLM Evaluation Benchmarks

**arXiv:** [2502.12896](https://arxiv.org/abs/2502.12896)
**Authors:** Eva Sánchez Salido, Julio Gonzalo, Guillermo Marco
**Date:** 2025-02-18
**Categories:** cs.CL

## Abstract

In LLM evaluations, reasoning is often distinguished from recall/memorization by performing numerical variations to math-oriented questions. Here we introduce a general variation method for multiple-choice questions that completely dissociates the correct answer from previously seen tokens or concepts, requiring LLMs to understand and reason (rather than memorizing) in order to answer correctly. Using this method, we evaluate state-of-the-art proprietary and open-source LLMs on two datasets available in English and Spanish: the public MMLU benchmark and the private UNED-Access 2024 dataset. Results show that all models experience remarkable accuracy drops under our proposed variation, with an average loss of 57% on MMLU and 50% on UNED-Access 2024, ranging from 10% to 93% across models. Notably, the most accurate model in our experimentation (OpenAI-o3-mini) is not the most robust (DeepSeek-R1-70B), suggesting that the best models in standard evaluations may not be the ones with better reasoning capabilities. Also, we see larger accuracy drops in public (vs private) datasets and questions posed in their original language (vs a manual translation), which are signs of contamination and also point to a relevant role of recall/memorization in current LLMs' answers.

---
*Metadata fetched via arxiv API on 2025-12-31*
