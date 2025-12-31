# SitEmb-v1.5: Improved Context-Aware Dense Retrieval for Semantic Association and Long Story Comprehension

**arXiv:** [2508.01959](https://arxiv.org/abs/2508.01959)
**Authors:** Junjie Wu, Jiangnan Li, Yuqing Li, Lemao Liu, Liyan Xu, et al. (9 total)
**Date:** 2025-08-03
**Categories:** cs.CL

## Abstract

Retrieval-augmented generation (RAG) over long documents typically involves splitting the text into smaller chunks, which serve as the basic units for retrieval. However, due to dependencies across the original document, contextual information is often essential for accurately interpreting each chunk. To address this, prior work has explored encoding longer context windows to produce embeddings for longer chunks. Despite these efforts, gains in retrieval and downstream tasks remain limited. This is because (1) longer chunks strain the capacity of embedding models due to the increased amount of information they must encode, and (2) many real-world applications still require returning localized evidence due to constraints on model or human bandwidth.
  We propose an alternative approach to this challenge by representing short chunks in a way that is conditioned on a broader context window to enhance retrieval performance -- i.e., situating a chunk's meaning within its context. We further show that existing embedding models are not well-equipped to encode such situated context effectively, and thus introduce a new training paradigm and develop the situated embedding models (SitEmb). To evaluate our method, we curate a book-plot retrieval dataset specifically designed to assess situated retrieval capabilities. On this benchmark, our SitEmb-v1 model based on BGE-M3 substantially outperforms state-of-the-art embedding models, including several with up to 7-8B parameters, with only 1B parameters. Our 8B SitEmb-v1.5 model further improves performance by over 10% and shows strong results across different languages and several downstream applications.

---
*Metadata fetched via arxiv API on 2025-12-31*
