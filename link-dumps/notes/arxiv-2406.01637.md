# Teams of LLM Agents can Exploit Zero-Day Vulnerabilities

**arXiv:** [2406.01637](https://arxiv.org/abs/2406.01637)
**Authors:** Yuxuan Zhu, Antony Kellermann, Akul Gupta, Philip Li, Richard Fang, et al. (7 total)
**Date:** 2024-06-02
**Categories:** cs.MA, cs.AI

## Abstract

LLM agents have become increasingly sophisticated, especially in the realm of cybersecurity. Researchers have shown that LLM agents can exploit real-world vulnerabilities when given a description of the vulnerability and toy capture-the-flag problems. However, these agents still perform poorly on real-world vulnerabilities that are unknown to the agent ahead of time (zero-day vulnerabilities).
  In this work, we show that teams of LLM agents can exploit real-world, zero-day vulnerabilities. Prior agents struggle with exploring many different vulnerabilities and long-range planning when used alone. To resolve this, we introduce HPTSA, a system of agents with a planning agent that can launch subagents. The planning agent explores the system and determines which subagents to call, resolving long-term planning issues when trying different vulnerabilities. We construct a benchmark of 14 real-world vulnerabilities and show that our team of agents improve over prior agent frameworks by up to 4.3X.

---
*Metadata fetched via arxiv API on 2025-12-31*
