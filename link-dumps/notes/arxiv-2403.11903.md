# A Closer Look at Claim Decomposition

**arXiv:** [2403.11903](https://arxiv.org/abs/2403.11903)
**Authors:** Miriam Wanner, Seth Ebner, Zhengping Jiang, Mark Dredze, Benjamin Van Durme
**Date:** 2024-03-18
**Categories:** cs.CL

## Abstract

As generated text becomes more commonplace, it is increasingly important to evaluate how well-supported such text is by external knowledge sources. Many approaches for evaluating textual support rely on some method for decomposing text into its individual subclaims which are scored against a trusted reference. We investigate how various methods of claim decomposition -- especially LLM-based methods -- affect the result of an evaluation approach such as the recently proposed FActScore, finding that it is sensitive to the decomposition method used. This sensitivity arises because such metrics attribute overall textual support to the model that generated the text even though error can also come from the metric's decomposition step. To measure decomposition quality, we introduce an adaptation of FActScore, which we call DecompScore. We then propose an LLM-based approach to generating decompositions inspired by Bertrand Russell's theory of logical atomism and neo-Davidsonian semantics and demonstrate its improved decomposition quality over previous methods.

---
*Metadata fetched via arxiv API on 2025-12-31*
