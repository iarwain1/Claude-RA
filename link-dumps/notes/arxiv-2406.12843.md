# Can Go AIs be adversarially robust?

**arXiv:** [2406.12843](https://arxiv.org/abs/2406.12843)
**Authors:** Tom Tseng, Euan McLean, Kellin Pelrine, Tony T. Wang, Adam Gleave
**Date:** 2024-06-18
**Categories:** cs.LG, cs.AI, stat.ML

## Abstract

Prior work found that superhuman Go AIs can be defeated by simple adversarial strategies, especially "cyclic" attacks. In this paper, we study whether adding natural countermeasures can achieve robustness in Go, a favorable domain for robustness since it benefits from incredible average-case capability and a narrow, innately adversarial setting. We test three defenses: adversarial training on hand-constructed positions, iterated adversarial training, and changing the network architecture. We find that though some of these defenses protect against previously discovered attacks, none withstand freshly trained adversaries. Furthermore, most of the reliably effective attacks these adversaries discover are different realizations of the same overall class of cyclic attacks. Our results suggest that building robust AI systems is challenging even with extremely superhuman systems in some of the most tractable settings, and highlight two key gaps: efficient generalization of defenses, and diversity in training. For interactive examples of attacks and a link to our codebase, see https://goattack.far.ai.

---
*Metadata fetched via arxiv API on 2025-12-31*
