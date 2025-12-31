# Evaluating Human Alignment and Model Faithfulness of LLM Rationale

**arXiv:** [2407.00219](https://arxiv.org/abs/2407.00219)
**Authors:** Mohsen Fayyaz, Fan Yin, Jiao Sun, Nanyun Peng
**Date:** 2024-06-28
**Categories:** cs.CL, cs.AI

## Abstract

We study how well large language models (LLMs) explain their generations through rationales -- a set of tokens extracted from the input text that reflect the decision-making process of LLMs. Specifically, we systematically study rationales derived using two approaches: (1) popular prompting-based methods, where prompts are used to guide LLMs in generating rationales, and (2) technical attribution-based methods, which leverage attention or gradients to identify important tokens. Our analysis spans three classification datasets with annotated rationales, encompassing tasks with varying performance levels. While prompting-based self-explanations are widely used, our study reveals that these explanations are not always as "aligned" with the human rationale as attribution-based explanations. Even more so, fine-tuning LLMs to enhance classification task accuracy does not enhance the alignment of prompting-based rationales. Still, it does considerably improve the alignment of attribution-based methods (e.g., InputXGradient). More importantly, we show that prompting-based self-explanation is also less "faithful" than attribution-based explanations, failing to provide a reliable account of the model's decision-making process. To evaluate faithfulness, unlike prior studies that excluded misclassified examples, we evaluate all instances and also examine the impact of fine-tuning and accuracy on alignment and faithfulness. Our findings suggest that inconclusive faithfulness results reported in earlier studies may stem from low classification accuracy. These findings underscore the importance of more rigorous and comprehensive evaluations of LLM rationales.

---
*Metadata fetched via arxiv API on 2025-12-31*
