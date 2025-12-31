# TUMIX: Multi-Agent Test-Time Scaling with Tool-Use Mixture

**arXiv:** [2510.01279](https://arxiv.org/abs/2510.01279)
**Authors:** Yongchao Chen, Jiefeng Chen, Rui Meng, Ji Yin, Na Li, et al. (9 total)
**Date:** 2025-09-30
**Categories:** cs.CL, cs.AI

## Abstract

While integrating tools like Code Interpreter and Search has significantly enhanced Large Language Model (LLM) reasoning in models like ChatGPT Agent and Gemini-Pro, practical guidance on optimal tool use is lacking. The core challenge is effectively combining textual reasoning, coding, and search for diverse questions. In this paper, we propose Tool-Use Mixture (TUMIX), an ensemble framework that runs multiple agents in parallel, each employing distinct tool-use strategies and answer paths. Agents in TUMIX iteratively share and refine responses based on the question and previous answers. In experiments, TUMIX achieves significant gains over state-of-the-art tool-augmented and test-time scaling methods, delivering an average accuracy improvement of up to 3.55% over the best baseline on Gemini-2.5-Pro and Gemini-2.5-Flash across key reasoning benchmarks, with near-equal inference costs. We find that agent diversity and quality are crucial and can be enhanced by using LLMs to auto-optimize agent designs. Furthermore, TUMIX can halt refinement upon reaching sufficient confidence, preserving performance at only 49% of the inference cost. Further scaling can achieve higher performance, albeit at a greater cost.

---
*Metadata fetched via arxiv API on 2025-12-31*
