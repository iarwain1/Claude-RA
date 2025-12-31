# Self-Evaluation as a Defense Against Adversarial Attacks on LLMs

**arXiv:** [2407.03234](https://arxiv.org/abs/2407.03234)
**Authors:** Hannah Brown, Leon Lin, Kenji Kawaguchi, Michael Shieh
**Date:** 2024-07-03
**Categories:** cs.LG, cs.CL, cs.CR

## Abstract

We introduce a defense against adversarial attacks on LLMs utilizing self-evaluation. Our method requires no model fine-tuning, instead using pre-trained models to evaluate the inputs and outputs of a generator model, significantly reducing the cost of implementation in comparison to other, finetuning-based methods. Our method can significantly reduce the attack success rate of attacks on both open and closed-source LLMs, beyond the reductions demonstrated by Llama-Guard2 and commonly used content moderation APIs. We present an analysis of the effectiveness of our method, including attempts to attack the evaluator in various settings, demonstrating that it is also more resilient to attacks than existing methods. Code and data will be made available at https://github.com/Linlt-leon/self-eval.

---
*Metadata fetched via arxiv API on 2025-12-31*
