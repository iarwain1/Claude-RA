# Select, Read, and Write: A Multi-Agent Framework of Full-Text-based Related Work Generation

**arXiv:** [2505.19647](https://arxiv.org/abs/2505.19647)
**Authors:** Xiaochuan Liu, Ruihua Song, Xiting Wang, Xu Chen
**Date:** 2025-05-26
**Categories:** cs.CL

## Abstract

Automatic related work generation (RWG) can save people's time and effort when writing a draft of related work section (RWS) for further revision. However, existing methods for RWG always suffer from shallow comprehension due to taking the limited portions of references papers as input and isolated explanation for each reference due to ineffective capturing the relationships among them. To address these issues, we focus on full-text-based RWG task and propose a novel multi-agent framework. Our framework consists of three agents: a selector that decides which section of the papers is going to read next, a reader that digests the selected section and updates a shared working memory, and a writer that generates RWS based on the final curated memory. To better capture the relationships among references, we also propose two graph-aware strategies for selector, enabling to optimize the reading order with constrains of the graph structure. Extensive experiments demonstrate that our framework consistently improves performance across three base models and various input configurations. The graph-aware selectors outperform alternative selectors, achieving state-of-the-art results. The code and data are available at https://github.com/1190200817/Full_Text_RWG.

---
*Metadata fetched via arxiv API on 2025-12-31*
