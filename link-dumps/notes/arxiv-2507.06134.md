# OpenAgentSafety: A Comprehensive Framework for Evaluating Real-World AI Agent Safety

**arXiv:** [2507.06134](https://arxiv.org/abs/2507.06134)
**Authors:** Sanidhya Vijayvargiya, Aditya Bharat Soni, Xuhui Zhou, Zora Zhiruo Wang, Nouha Dziri, et al. (7 total)
**Date:** 2025-07-08
**Categories:** cs.AI

## Abstract

Recent advances in AI agents capable of solving complex, everyday tasks, from scheduling to customer service, have enabled deployment in real-world settings, but their possibilities for unsafe behavior demands rigorous evaluation. While prior benchmarks have attempted to assess agent safety, most fall short by relying on simulated environments, narrow task domains, or unrealistic tool abstractions. We introduce OpenAgentSafety, a comprehensive and modular framework for evaluating agent behavior across eight critical risk categories. Unlike prior work, our framework evaluates agents that interact with real tools, including web browsers, code execution environments, file systems, bash shells, and messaging platforms; and supports over 350 multi-turn, multi-user tasks spanning both benign and adversarial user intents. OpenAgentSafety is designed for extensibility, allowing researchers to add tools, tasks, websites, and adversarial strategies with minimal effort. It combines rule-based analysis with LLM-as-judge assessments to detect both overt and subtle unsafe behaviors. Empirical analysis of five prominent LLMs in agentic scenarios reveals unsafe behavior in 51.2% of safety-vulnerable tasks with Claude-Sonnet-3.7, to 72.7% with o3-mini, highlighting critical safety vulnerabilities and the need for stronger safeguards before real-world deployment.

---
*Metadata fetched via arxiv API on 2025-12-31*
