# PrimeGuard: Safe and Helpful LLMs through Tuning-Free Routing

**arXiv:** [2407.16318](https://arxiv.org/abs/2407.16318)
**Authors:** Blazej Manczak, Eliott Zemour, Eric Lin, Vaikkunth Mugunthan
**Date:** 2024-07-23
**Categories:** cs.AI, cs.CL, cs.CR

## Abstract

Deploying language models (LMs) necessitates outputs to be both high-quality and compliant with safety guidelines. Although Inference-Time Guardrails (ITG) offer solutions that shift model output distributions towards compliance, we find that current methods struggle in balancing safety with helpfulness. ITG Methods that safely address non-compliant queries exhibit lower helpfulness while those that prioritize helpfulness compromise on safety. We refer to this trade-off as the guardrail tax, analogous to the alignment tax. To address this, we propose PrimeGuard, a novel ITG method that utilizes structured control flow.
  PrimeGuard routes requests to different self-instantiations of the LM with varying instructions, leveraging its inherent instruction-following capabilities and in-context learning. Our tuning-free approach dynamically compiles system-designer guidelines for each query. We construct and release safe-eval, a diverse red-team safety benchmark. Extensive evaluations demonstrate that PrimeGuard, without fine-tuning, overcomes the guardrail tax by (1) significantly increasing resistance to iterative jailbreak attacks and (2) achieving state-of-the-art results in safety guardrailing while (3) matching helpfulness scores of alignment-tuned models. Extensive evaluations demonstrate that PrimeGuard, without fine-tuning, outperforms all competing baselines and overcomes the guardrail tax by improving the fraction of safe responses from 61% to 97% and increasing average helpfulness scores from 4.17 to 4.29 on the largest models, while reducing attack success rate from 100% to 8%.
  PrimeGuard implementation is available at https://github.com/dynamofl/PrimeGuard and safe-eval dataset is available at https://huggingface.co/datasets/dynamoai/safe_eval.

---
*Metadata fetched via arxiv API on 2025-12-31*
