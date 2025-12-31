# SOS! Soft Prompt Attack Against Open-Source Large Language Models

**arXiv:** [2407.03160](https://arxiv.org/abs/2407.03160)
**Authors:** Ziqing Yang, Michael Backes, Yang Zhang, Ahmed Salem
**Date:** 2024-07-03
**Categories:** cs.CR, cs.CL, cs.LG

## Abstract

Open-source large language models (LLMs) have become increasingly popular among both the general public and industry, as they can be customized, fine-tuned, and freely used. However, some open-source LLMs require approval before usage, which has led to third parties publishing their own easily accessible versions. Similarly, third parties have been publishing fine-tuned or quantized variants of these LLMs. These versions are particularly appealing to users because of their ease of access and reduced computational resource demands. This trend has increased the risk of training time attacks, compromising the integrity and security of LLMs. In this work, we present a new training time attack, SOS, which is designed to be low in computational demand and does not require clean data or modification of the model weights, thereby maintaining the model's utility intact. The attack addresses security issues in various scenarios, including the backdoor attack, jailbreak attack, and prompt stealing attack. Our experimental findings demonstrate that the proposed attack is effective across all evaluated targets. Furthermore, we present the other side of our SOS technique, namely the copyright token -- a novel technique that enables users to mark their copyrighted content and prevent models from using it.

---
*Metadata fetched via arxiv API on 2025-12-31*
