# Emergence of Linear Truth Encodings in Language Models

**arXiv:** [2510.15804](https://arxiv.org/abs/2510.15804)
**Authors:** Shauli Ravfogel, Gilad Yehudai, Tal Linzen, Joan Bruna, Alberto Bietti
**Date:** 2025-10-17
**Categories:** cs.CL

## Abstract

Recent probing studies reveal that large language models exhibit linear subspaces that separate true from false statements, yet the mechanism behind their emergence is unclear. We introduce a transparent, one-layer transformer toy model that reproduces such truth subspaces end-to-end and exposes one concrete route by which they can arise. We study one simple setting in which truth encoding can emerge: a data distribution where factual statements co-occur with other factual statements (and vice-versa), encouraging the model to learn this distinction in order to lower the LM loss on future tokens. We corroborate this pattern with experiments in pretrained language models. Finally, in the toy setting we observe a two-phase learning dynamic: networks first memorize individual factual associations in a few steps, then -- over a longer horizon -- learn to linearly separate true from false, which in turn lowers language-modeling loss. Together, these results provide both a mechanistic demonstration and an empirical motivation for how and why linear truth representations can emerge in language models.

---
*Metadata fetched via arxiv API on 2025-12-31*
