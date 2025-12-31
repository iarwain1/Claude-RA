# On Subjective Uncertainty Quantification and Calibration in Natural Language Generation

**arXiv:** [2406.05213](https://arxiv.org/abs/2406.05213)
**Authors:** Ziyu Wang, Chris Holmes
**Date:** 2024-06-07
**Categories:** cs.CL, cs.AI, cs.LG

## Abstract

Applications of large language models often involve the generation of free-form responses, in which case uncertainty quantification becomes challenging. This is due to the need to identify task-specific uncertainties (e.g., about the semantics) which appears difficult to define in general cases. This work addresses these challenges from a perspective of Bayesian decision theory, starting from the assumption that our utility is characterized by a similarity measure that compares a generated response with a hypothetical true response. We discuss how this assumption enables principled quantification of the model's subjective uncertainty and its calibration. We further derive a measure for epistemic uncertainty, based on a missing data perspective and its characterization as an excess risk. The proposed methods can be applied to black-box language models. We illustrate the methods on question answering and machine translation tasks. Our experiments provide a principled evaluation of task-specific calibration, and demonstrate that epistemic uncertainty offers a promising deferral strategy for efficient data acquisition in in-context learning.

---
*Metadata fetched via arxiv API on 2025-12-31*
