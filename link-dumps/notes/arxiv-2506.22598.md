# RExBench: Can coding agents autonomously implement AI research extensions?

**arXiv:** [2506.22598](https://arxiv.org/abs/2506.22598)
**Authors:** Nicholas Edwards, Yukyung Lee, Yujun Audrey Mao, Yulu Qin, Sebastian Schuster, et al. (6 total)
**Date:** 2025-06-27
**Categories:** cs.CL

## Abstract

Agents based on Large Language Models (LLMs) have shown promise for performing sophisticated software engineering tasks autonomously. In addition, there has been progress towards developing agents that can perform parts of the research pipeline in machine learning and the natural sciences. We argue that research extension and its implementation is a critical capability for such systems, and introduce RExBench to support the evaluation of this capability. RExBench is a benchmark consisting of 12 realistic research experiment implementation tasks that aim to investigate research hypotheses that have not previously been implemented. Each task is set up as an extension to an existing research paper and codebase, accompanied by domain expert-written instructions. RExBench is robust to data contamination, and supports an automatic evaluation infrastructure that executes agent outputs to determine whether the success criteria are met. We use this benchmark to evaluate nine LLM agents implemented using three different frameworks: aider, Claude Code, and OpenHands. We find that all agents evaluated fail to autonomously implement the majority of the extensions. Although the success rate improves with additional human-written hints, the best performance under this setting remains below 40%. This indicates that current agents are still short of being able to handle realistic research extension tasks without substantial human guidance.

---
*Metadata fetched via arxiv API on 2025-12-31*
