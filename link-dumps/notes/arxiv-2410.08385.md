# Language model developers should report train-test overlap

**arXiv:** [2410.08385](https://arxiv.org/abs/2410.08385)
**Authors:** Andy K Zhang, Kevin Klyman, Yifan Mai, Yoav Levine, Yian Zhang, et al. (7 total)
**Date:** 2024-10-10
**Categories:** cs.LG, cs.AI, cs.CY

## Abstract

Language models are extensively evaluated, but correctly interpreting evaluation results requires knowledge of train-test overlap which refers to the extent to which the language model is trained on the very data it is being tested on. The public currently lacks adequate information about train-test overlap: most models have no public train-test overlap statistics, and third parties cannot directly measure train-test overlap since they do not have access to the training data. To make this clear, we document the practices of 30 model developers, finding that just 9 developers report train-test overlap: 4 developers release training data under open-source licenses, enabling the community to directly measure train-test overlap, and 5 developers publish their train-test overlap methodology and statistics. By engaging with language model developers, we provide novel information about train-test overlap for three additional developers. Overall, we take the position that language model developers should publish train-test overlap statistics and/or training data whenever they report evaluation results on public test sets. We hope our work increases transparency into train-test overlap to increase the community-wide trust in model evaluations.

---
*Metadata fetched via arxiv API on 2025-12-31*
