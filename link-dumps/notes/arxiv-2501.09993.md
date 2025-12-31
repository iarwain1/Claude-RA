# Agent-as-Judge for Factual Summarization of Long Narratives

**arXiv:** [2501.09993](https://arxiv.org/abs/2501.09993)
**Authors:** Yeonseok Jeong, Minsoo Kim, Seung-won Hwang, Byung-Hak Kim
**Date:** 2025-01-17
**Categories:** cs.CL

## Abstract

Large Language Models (LLMs) have demonstrated near-human performance in summarization tasks based on traditional metrics such as ROUGE and BERTScore. However, these metrics do not adequately capture critical aspects of summarization quality, such as factual accuracy, particularly for long narratives (>100K tokens). Recent advances, such as LLM-as-a-Judge, address the limitations of metrics based on lexical similarity but still exhibit factual inconsistencies, especially in understanding character relationships and states. In this work, we introduce NarrativeFactScore, a novel "Agent-as-a-Judge" framework for evaluating and refining summaries. By leveraging a Character Knowledge Graph (CKG) extracted from input and generated summaries, NarrativeFactScore assesses the factual consistency and provides actionable guidance for refinement, such as identifying missing or erroneous facts. We demonstrate the effectiveness of NarrativeFactScore through a detailed workflow illustration and extensive validation on widely adopted benchmarks, achieving superior performance compared to competitive methods. Our results highlight the potential of agent-driven evaluation systems to improve the factual reliability of LLM-generated summaries.

---
*Metadata fetched via arxiv API on 2025-12-31*
