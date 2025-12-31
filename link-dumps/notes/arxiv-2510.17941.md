# Believe It or Not: How Deeply do LLMs Believe Implanted Facts?

**arXiv:** [2510.17941](https://arxiv.org/abs/2510.17941)
**Authors:** Stewart Slocum, Julian Minder, Clément Dumas, Henry Sleight, Ryan Greenblatt, et al. (7 total)
**Date:** 2025-10-20
**Categories:** cs.CL, cs.AI

## Abstract

Knowledge editing techniques promise to implant new factual knowledge into large language models (LLMs). But do LLMs really believe these facts? We develop a framework to measure belief depth and use it to evaluate the success of knowledge editing techniques. We operationalize belief depth as the extent to which implanted knowledge 1) generalizes to related contexts (e.g. Fermi estimates several logical steps removed), 2) is robust to self-scrutiny and direct challenge, and 3) is represented similarly to genuine knowledge (as measured by linear probes). Our evaluations show that simple prompting and mechanistic editing techniques fail to implant knowledge deeply. In contrast, Synthetic Document Finetuning (SDF) - where models are trained on LLM-generated documents consistent with a fact - often succeeds at implanting beliefs that behave similarly to genuine knowledge. However, SDF's success is not universal, as implanted beliefs that contradict basic world knowledge are brittle and representationally distinct from genuine knowledge. Overall, our work introduces measurable criteria for belief depth and enables the rigorous evaluation necessary for deploying knowledge editing in real-world applications.

---
*Metadata fetched via arxiv API on 2025-12-31*
