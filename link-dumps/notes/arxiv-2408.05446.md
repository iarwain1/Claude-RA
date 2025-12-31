# Ensemble everything everywhere: Multi-scale aggregation for adversarial robustness

**arXiv:** [2408.05446](https://arxiv.org/abs/2408.05446)
**Authors:** Stanislav Fort, Balaji Lakshminarayanan
**Date:** 2024-08-08
**Categories:** cs.CV, cs.LG

## Abstract

Adversarial examples pose a significant challenge to the robustness, reliability and alignment of deep neural networks. We propose a novel, easy-to-use approach to achieving high-quality representations that lead to adversarial robustness through the use of multi-resolution input representations and dynamic self-ensembling of intermediate layer predictions. We demonstrate that intermediate layer predictions exhibit inherent robustness to adversarial attacks crafted to fool the full classifier, and propose a robust aggregation mechanism based on Vickrey auction that we call \textit{CrossMax} to dynamically ensemble them. By combining multi-resolution inputs and robust ensembling, we achieve significant adversarial robustness on CIFAR-10 and CIFAR-100 datasets without any adversarial training or extra data, reaching an adversarial accuracy of $\approx$72% (CIFAR-10) and $\approx$48% (CIFAR-100) on the RobustBench AutoAttack suite ($L_\infty=8/255)$ with a finetuned ImageNet-pretrained ResNet152. This represents a result comparable with the top three models on CIFAR-10 and a +5 % gain compared to the best current dedicated approach on CIFAR-100. Adding simple adversarial training on top, we get $\approx$78% on CIFAR-10 and $\approx$51% on CIFAR-100, improving SOTA by 5 % and 9 % respectively and seeing greater gains on the harder dataset. We validate our approach through extensive experiments and provide insights into the interplay between adversarial robustness, and the hierarchical nature of deep representations. We show that simple gradient-based attacks against our model lead to human-interpretable images of the target classes as well as interpretable image changes. As a byproduct, using our multi-resolution prior, we turn pre-trained classifiers and CLIP models into controllable image generators and develop successful transferable attacks on large vision language models.

---
*Metadata fetched via arxiv API on 2025-12-31*
