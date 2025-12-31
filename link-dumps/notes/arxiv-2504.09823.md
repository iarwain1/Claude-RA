# RAKG:Document-level Retrieval Augmented Knowledge Graph Construction

**arXiv:** [2504.09823](https://arxiv.org/abs/2504.09823)
**Authors:** Hairong Zhang, Jiaheng Si, Guohang Yan, Boyuan Qi, Pinlong Cai, et al. (8 total)
**Date:** 2025-04-14
**Categories:** cs.IR

## Abstract

With the rise of knowledge graph based retrieval-augmented generation (RAG) techniques such as GraphRAG and Pike-RAG, the role of knowledge graphs in enhancing the reasoning capabilities of large language models (LLMs) has become increasingly prominent. However, traditional Knowledge Graph Construction (KGC) methods face challenges like complex entity disambiguation, rigid schema definition, and insufficient cross-document knowledge integration. This paper focuses on the task of automatic document-level knowledge graph construction. It proposes the Document-level Retrieval Augmented Knowledge Graph Construction (RAKG) framework. RAKG extracts pre-entities from text chunks and utilizes these pre-entities as queries for RAG, effectively addressing the issue of long-context forgetting in LLMs and reducing the complexity of Coreference Resolution. In contrast to conventional KGC methods, RAKG more effectively captures global information and the interconnections among disparate nodes, thereby enhancing the overall performance of the model. Additionally, we transfer the RAG evaluation framework to the KGC field and filter and evaluate the generated knowledge graphs, thereby avoiding incorrectly generated entities and relationships caused by hallucinations in LLMs. We further developed the MINE dataset by constructing standard knowledge graphs for each article and experimentally validated the performance of RAKG. The results show that RAKG achieves an accuracy of 95.91 % on the MINE dataset, a 6.2 % point improvement over the current best baseline, GraphRAG (89.71 %). The code is available at https://github.com/LMMApplication/RAKG.

---
*Metadata fetched via arxiv API on 2025-12-31*
