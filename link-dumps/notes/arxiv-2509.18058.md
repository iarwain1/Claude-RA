# Strategic Dishonesty Can Undermine AI Safety Evaluations of Frontier LLMs

**arXiv:** [2509.18058](https://arxiv.org/abs/2509.18058)
**Authors:** Alexander Panfilov, Evgenii Kortukov, Kristina Nikolić, Matthias Bethge, Sebastian Lapuschkin, et al. (9 total)
**Date:** 2025-09-22
**Categories:** cs.LG, cs.AI, cs.CR

## Abstract

Large language model (LLM) developers aim for their models to be honest, helpful, and harmless. However, when faced with malicious requests, models are trained to refuse, sacrificing helpfulness. We show that frontier LLMs can develop a preference for dishonesty as a new strategy, even when other options are available. Affected models respond to harmful requests with outputs that sound harmful but are crafted to be subtly incorrect or otherwise harmless in practice. This behavior emerges with hard-to-predict variations even within models from the same model family. We find no apparent cause for the propensity to deceive, but show that more capable models are better at executing this strategy. Strategic dishonesty already has a practical impact on safety evaluations, as we show that dishonest responses fool all output-based monitors used to detect jailbreaks that we test, rendering benchmark scores unreliable. Further, strategic dishonesty can act like a honeypot against malicious users, which noticeably obfuscates prior jailbreak attacks. While output monitors fail, we show that linear probes on internal activations can be used to reliably detect strategic dishonesty. We validate probes on datasets with verifiable outcomes and by using them as steering vectors. Overall, we consider strategic dishonesty as a concrete example of a broader concern that alignment of LLMs is hard to control, especially when helpfulness and harmlessness conflict.

---
*Metadata fetched via arxiv API on 2025-12-31*
