# School of Reward Hacks: Hacking harmless tasks generalizes to misaligned behavior in LLMs

**arXiv:** [2508.17511](https://arxiv.org/abs/2508.17511)
**Authors:** Mia Taylor, James Chua, Jan Betley, Johannes Treutlein, Owain Evans
**Date:** 2025-08-24
**Categories:** cs.AI

## Abstract

Reward hacking--where agents exploit flaws in imperfect reward functions rather than performing tasks as intended--poses risks for AI alignment. Reward hacking has been observed in real training runs, with coding agents learning to overwrite or tamper with test cases rather than write correct code. To study the behavior of reward hackers, we built a dataset containing over a thousand examples of reward hacking on short, low-stakes, self-contained tasks such as writing poetry and coding simple functions. We used supervised fine-tuning to train models (GPT-4.1, GPT-4.1-mini, Qwen3-32B, Qwen3-8B) to reward hack on these tasks. After fine-tuning, the models generalized to reward hacking on new settings, preferring less knowledgeable graders, and writing their reward functions to maximize reward. Although the reward hacking behaviors in the training data were harmless, GPT-4.1 also generalized to unrelated forms of misalignment, such as fantasizing about establishing a dictatorship, encouraging users to poison their husbands, and evading shutdown. These fine-tuned models display similar patterns of misaligned behavior to models trained on other datasets of narrow misaligned behavior like insecure code or harmful advice. Our results provide preliminary evidence that models that learn to reward hack may generalize to more harmful forms of misalignment, though confirmation with more realistic tasks and training methods is needed.

---
*Metadata fetched via arxiv API on 2025-12-31*
