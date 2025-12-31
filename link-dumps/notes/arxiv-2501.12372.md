# Is Long Context All You Need? Leveraging LLM's Extended Context for NL2SQL

**arXiv:** [2501.12372](https://arxiv.org/abs/2501.12372)
**Authors:** Yeounoh Chung, Gaurav T. Kakkar, Yu Gan, Brenton Milne, Fatma Ozcan
**Date:** 2025-01-21
**Categories:** cs.DB, cs.AI

## Abstract

Large Language Models (LLMs) have demonstrated impressive capabilities across a range of natural language processing tasks. In particular, improvements in reasoning abilities and the expansion of context windows have opened new avenues for leveraging these powerful models. NL2SQL is challenging in that the natural language question is inherently ambiguous, while the SQL generation requires a precise understanding of complex data schema and semantics. One approach to this semantic ambiguous problem is to provide more and sufficient contextual information.
  In this work, we explore the performance and the latency trade-offs of the extended context window (a.k.a., long context) offered by Google's state-of-the-art LLM (\textit{gemini-1.5-pro}). We study the impact of various contextual information, including column example values, question and SQL query pairs, user-provided hints, SQL documentation, and schema. To the best of our knowledge, this is the first work to study how the extended context window and extra contextual information can help NL2SQL generation with respect to both accuracy and latency cost. We show that long context LLMs are robust and do not get lost in the extended contextual information. Additionally, our long-context NL2SQL pipeline based on Google's \textit{gemini-pro-1.5} achieve strong performances on various benchmark datasets without finetuning and expensive self-consistency based techniques.

---
*Metadata fetched via arxiv API on 2025-12-31*
