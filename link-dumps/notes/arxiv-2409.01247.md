# Conversational Complexity for Assessing Risk in Large Language Models

**arXiv:** [2409.01247](https://arxiv.org/abs/2409.01247)
**Authors:** John Burden, Manuel Cebrian, Jose Hernandez-Orallo
**Date:** 2024-09-02
**Categories:** cs.AI, cs.CL, cs.IT

## Abstract

Large Language Models (LLMs) present a dual-use dilemma: they enable beneficial applications while harboring potential for harm, particularly through conversational interactions. Despite various safeguards, advanced LLMs remain vulnerable. A watershed case in early 2023 involved journalist Kevin Roose's extended dialogue with Bing, an LLM-powered search engine, which revealed harmful outputs after probing questions, highlighting vulnerabilities in the model's safeguards. This contrasts with simpler early jailbreaks, like the "Grandma Jailbreak," where users framed requests as innocent help for a grandmother, easily eliciting similar content. This raises the question: How much conversational effort is needed to elicit harmful information from LLMs? We propose two measures to quantify this effort: Conversational Length (CL), which measures the number of conversational turns needed to obtain a specific harmful response, and Conversational Complexity (CC), defined as the Kolmogorov complexity of the user's instruction sequence leading to the harmful response. To address the incomputability of Kolmogorov complexity, we approximate CC using a reference LLM to estimate the compressibility of the user instructions. Applying this approach to a large red-teaming dataset, we perform a quantitative analysis examining the statistical distribution of harmful and harmless conversational lengths and complexities. Our empirical findings suggest that this distributional analysis and the minimization of CC serve as valuable tools for understanding AI safety, offering insights into the accessibility of harmful information. This work establishes a foundation for a new perspective on LLM safety, centered around the algorithmic complexity of pathways to harm.

---
*Metadata fetched via arxiv API on 2025-12-31*
