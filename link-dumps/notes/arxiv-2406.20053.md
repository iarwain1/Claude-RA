# Covert Malicious Finetuning: Challenges in Safeguarding LLM Adaptation

**arXiv:** [2406.20053](https://arxiv.org/abs/2406.20053)
**Authors:** Danny Halawi, Alexander Wei, Eric Wallace, Tony T. Wang, Nika Haghtalab, et al. (6 total)
**Date:** 2024-06-28
**Categories:** cs.CR, cs.AI, cs.CL

## Abstract

Black-box finetuning is an emerging interface for adapting state-of-the-art language models to user needs. However, such access may also let malicious actors undermine model safety. To demonstrate the challenge of defending finetuning interfaces, we introduce covert malicious finetuning, a method to compromise model safety via finetuning while evading detection. Our method constructs a malicious dataset where every individual datapoint appears innocuous, but finetuning on the dataset teaches the model to respond to encoded harmful requests with encoded harmful responses. Applied to GPT-4, our method produces a finetuned model that acts on harmful instructions 99% of the time and avoids detection by defense mechanisms such as dataset inspection, safety evaluations, and input/output classifiers. Our findings question whether black-box finetuning access can be secured against sophisticated adversaries.

---
*Metadata fetched via arxiv API on 2025-12-31*
