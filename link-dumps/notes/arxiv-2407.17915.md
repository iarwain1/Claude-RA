# The Dark Side of Function Calling: Pathways to Jailbreaking Large Language Models

**arXiv:** [2407.17915](https://arxiv.org/abs/2407.17915)
**Authors:** Zihui Wu, Haichang Gao, Jianping He, Ping Wang
**Date:** 2024-07-25
**Categories:** cs.CR, cs.AI

## Abstract

Large language models (LLMs) have demonstrated remarkable capabilities, but their power comes with significant security considerations. While extensive research has been conducted on the safety of LLMs in chat mode, the security implications of their function calling feature have been largely overlooked. This paper uncovers a critical vulnerability in the function calling process of LLMs, introducing a novel "jailbreak function" attack method that exploits alignment discrepancies, user coercion, and the absence of rigorous safety filters. Our empirical study, conducted on six state-of-the-art LLMs including GPT-4o, Claude-3.5-Sonnet, and Gemini-1.5-pro, reveals an alarming average success rate of over 90\% for this attack. We provide a comprehensive analysis of why function calls are susceptible to such attacks and propose defensive strategies, including the use of defensive prompts. Our findings highlight the urgent need for enhanced security measures in the function calling capabilities of LLMs, contributing to the field of AI safety by identifying a previously unexplored risk, designing an effective attack method, and suggesting practical defensive measures. Our code is available at https://github.com/wooozihui/jailbreakfunction.

---
*Metadata fetched via arxiv API on 2025-12-31*
