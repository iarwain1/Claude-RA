# Know Thy Judge: On the Robustness Meta-Evaluation of LLM Safety Judges

**arXiv:** [2503.04474](https://arxiv.org/abs/2503.04474)
**Authors:** Francisco Eiras, Eliott Zemour, Eric Lin, Vaikkunth Mugunthan
**Date:** 2025-03-06
**Categories:** cs.LG, cs.CR

## Abstract

Large Language Model (LLM) based judges form the underpinnings of key safety evaluation processes such as offline benchmarking, automated red-teaming, and online guardrailing. This widespread requirement raises the crucial question: can we trust the evaluations of these evaluators? In this paper, we highlight two critical challenges that are typically overlooked: (i) evaluations in the wild where factors like prompt sensitivity and distribution shifts can affect performance and (ii) adversarial attacks that target the judge. We highlight the importance of these through a study of commonly used safety judges, showing that small changes such as the style of the model output can lead to jumps of up to 0.24 in the false negative rate on the same dataset, whereas adversarial attacks on the model generation can fool some judges into misclassifying 100% of harmful generations as safe ones. These findings reveal gaps in commonly used meta-evaluation benchmarks and weaknesses in the robustness of current LLM judges, indicating that low attack success under certain judges could create a false sense of security.

---
*Metadata fetched via arxiv API on 2025-12-31*
