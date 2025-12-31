# Subtle Risks, Critical Failures: A Framework for Diagnosing Physical Safety of LLMs for Embodied Decision Making

**arXiv:** [2505.19933](https://arxiv.org/abs/2505.19933)
**Authors:** Yejin Son, Minseo Kim, Sungwoong Kim, Seungju Han, Jian Kim, et al. (8 total)
**Date:** 2025-05-26
**Categories:** cs.AI

## Abstract

Large Language Models (LLMs) are increasingly used for decision making in embodied agents, yet existing safety evaluations often rely on coarse success rates and domain-specific setups, making it difficult to diagnose why and where these models fail. This obscures our understanding of embodied safety and limits the selective deployment of LLMs in high-risk physical environments. We introduce SAFEL, the framework for systematically evaluating the physical safety of LLMs in embodied decision making. SAFEL assesses two key competencies: (1) rejecting unsafe commands via the Command Refusal Test, and (2) generating safe and executable plans via the Plan Safety Test. Critically, the latter is decomposed into functional modules, goal interpretation, transition modeling, action sequencing, enabling fine-grained diagnosis of safety failures. To support this framework, we introduce EMBODYGUARD, a PDDL-grounded benchmark containing 942 LLM-generated scenarios covering both overtly malicious and contextually hazardous instructions. Evaluation across 13 state-of-the-art LLMs reveals that while models often reject clearly unsafe commands, they struggle to anticipate and mitigate subtle, situational risks. Our results highlight critical limitations in current LLMs and provide a foundation for more targeted, modular improvements in safe embodied reasoning.

---
*Metadata fetched via arxiv API on 2025-12-31*
