# Security Challenges in AI Agent Deployment: Insights from a Large Scale Public Competition

**arXiv:** [2507.20526](https://arxiv.org/abs/2507.20526)
**Authors:** Andy Zou, Maxwell Lin, Eliot Jones, Micha Nowak, Mateusz Dziemian, et al. (17 total)
**Date:** 2025-07-28
**Categories:** cs.AI, cs.CL, cs.CY

## Abstract

Recent advances have enabled LLM-powered AI agents to autonomously execute complex tasks by combining language model reasoning with tools, memory, and web access. But can these systems be trusted to follow deployment policies in realistic environments, especially under attack? To investigate, we ran the largest public red-teaming competition to date, targeting 22 frontier AI agents across 44 realistic deployment scenarios. Participants submitted 1.8 million prompt-injection attacks, with over 60,000 successfully eliciting policy violations such as unauthorized data access, illicit financial actions, and regulatory noncompliance. We use these results to build the Agent Red Teaming (ART) benchmark - a curated set of high-impact attacks - and evaluate it across 19 state-of-the-art models. Nearly all agents exhibit policy violations for most behaviors within 10-100 queries, with high attack transferability across models and tasks. Importantly, we find limited correlation between agent robustness and model size, capability, or inference-time compute, suggesting that additional defenses are needed against adversarial misuse. Our findings highlight critical and persistent vulnerabilities in today's AI agents. By releasing the ART benchmark and accompanying evaluation framework, we aim to support more rigorous security assessment and drive progress toward safer agent deployment.

---
*Metadata fetched via arxiv API on 2025-12-31*
