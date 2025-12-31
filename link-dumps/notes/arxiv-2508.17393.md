# Agent-Testing Agent: A Meta-Agent for Automated Testing and Evaluation of Conversational AI Agents

**arXiv:** [2508.17393](https://arxiv.org/abs/2508.17393)
**Authors:** Sameer Komoravolu, Khalil Mrini
**Date:** 2025-08-24
**Categories:** cs.CL, cs.AI

## Abstract

LLM agents are increasingly deployed to plan, retrieve, and write with tools, yet evaluation still leans on static benchmarks and small human studies. We present the Agent-Testing Agent (ATA), a meta-agent that combines static code analysis, designer interrogation, literature mining, and persona-driven adversarial test generation whose difficulty adapts via judge feedback. Each dialogue is scored with an LLM-as-a-Judge (LAAJ) rubric and used to steer subsequent tests toward the agent's weakest capabilities. On a travel planner and a Wikipedia writer, the ATA surfaces more diverse and severe failures than expert annotators while matching severity, and finishes in 20--30 minutes versus ten-annotator rounds that took days. Ablating code analysis and web search increases variance and miscalibration, underscoring the value of evidence-grounded test generation. The ATA outputs quantitative metrics and qualitative bug reports for developers. We release the full methodology and open-source implementation for reproducible agent testing: https://github.com/KhalilMrini/Agent-Testing-Agent

---
*Metadata fetched via arxiv API on 2025-12-31*
