# Logicbreaks: A Framework for Understanding Subversion of Rule-based Inference

**arXiv:** [2407.00075](https://arxiv.org/abs/2407.00075)
**Authors:** Anton Xue, Avishree Khare, Rajeev Alur, Surbhi Goel, Eric Wong
**Date:** 2024-06-21
**Categories:** cs.AI, cs.CL, cs.CR

## Abstract

We study how to subvert large language models (LLMs) from following prompt-specified rules. We first formalize rule-following as inference in propositional Horn logic, a mathematical system in which rules have the form "if $P$ and $Q$, then $R$" for some propositions $P$, $Q$, and $R$. Next, we prove that although small transformers can faithfully follow such rules, maliciously crafted prompts can still mislead both theoretical constructions and models learned from data. Furthermore, we demonstrate that popular attack algorithms on LLMs find adversarial prompts and induce attention patterns that align with our theory. Our novel logic-based framework provides a foundation for studying LLMs in rule-based settings, enabling a formal analysis of tasks like logical reasoning and jailbreak attacks.

---
*Metadata fetched via arxiv API on 2025-12-31*
