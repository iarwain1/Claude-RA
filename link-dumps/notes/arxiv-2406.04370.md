# Large Language Model Confidence Estimation via Black-Box Access

**arXiv:** [2406.04370](https://arxiv.org/abs/2406.04370)
**Authors:** Tejaswini Pedapati, Amit Dhurandhar, Soumya Ghosh, Soham Dan, Prasanna Sattigeri
**Date:** 2024-06-01
**Categories:** cs.CL, cs.AI, cs.LG

## Abstract

Estimating uncertainty or confidence in the responses of a model can be significant in evaluating trust not only in the responses, but also in the model as a whole. In this paper, we explore the problem of estimating confidence for responses of large language models (LLMs) with simply black-box or query access to them. We propose a simple and extensible framework where, we engineer novel features and train a (interpretable) model (viz. logistic regression) on these features to estimate the confidence. We empirically demonstrate that our simple framework is effective in estimating confidence of Flan-ul2, Llama-13b, Mistral-7b and GPT-4 on four benchmark Q\&A tasks as well as of Pegasus-large and BART-large on two benchmark summarization tasks with it surpassing baselines by even over $10\%$ (on AUROC) in some cases. Additionally, our interpretable approach provides insight into features that are predictive of confidence, leading to the interesting and useful discovery that our confidence models built for one LLM generalize zero-shot across others on a given dataset.

---
*Metadata fetched via arxiv API on 2025-12-31*
