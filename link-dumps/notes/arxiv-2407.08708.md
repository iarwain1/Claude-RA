# eyeballvul: a future-proof benchmark for vulnerability detection in the wild

**arXiv:** [2407.08708](https://arxiv.org/abs/2407.08708)
**Authors:** Timothee Chauvin
**Date:** 2024-07-11
**Categories:** cs.CR, cs.AI, cs.LG

## Abstract

Long contexts of recent LLMs have enabled a new use case: asking models to find security vulnerabilities in entire codebases. To evaluate model performance on this task, we introduce eyeballvul: a benchmark designed to test the vulnerability detection capabilities of language models at scale, that is sourced and updated weekly from the stream of published vulnerabilities in open-source repositories. The benchmark consists of a list of revisions in different repositories, each associated with the list of known vulnerabilities present at that revision. An LLM-based scorer is used to compare the list of possible vulnerabilities returned by a model to the list of known vulnerabilities for each revision. As of July 2024, eyeballvul contains 24,000+ vulnerabilities across 6,000+ revisions and 5,000+ repositories, and is around 55GB in size.

---
*Metadata fetched via arxiv API on 2025-12-31*
