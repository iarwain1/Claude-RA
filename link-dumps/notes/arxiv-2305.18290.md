# Direct Preference Optimization: Your Language Model is Secretly a Reward Model

**arXiv:** https://arxiv.org/abs/2305.18290
**Authors:** Rafael Rafailov, Archit Sharma, Eric Mitchell, Stefano Ermon, Christopher D. Manning, Chelsea Finn (Stanford University)
**Date:** 2023-05
**Venue:** NeurIPS 2023 (Outstanding Paper Award)

## Abstract

Direct Preference Optimization (DPO) is an algorithm for training language models from human preferences without reinforcement learning. The key insight is that the standard RLHF objective with KL-divergence constraint can be optimized directly using a simple classification loss on preference data.

DPO bypasses the need to:
1. Train an explicit reward model
2. Sample from the policy during training
3. Use complex RL algorithms like PPO

## How It Works

DPO reparameterizes the reward model in terms of the policy itself, allowing direct optimization on preference pairs with a simple loss function:

```
L_DPO = -log σ(β log(π(y_w)/π_ref(y_w)) - β log(π(y_l)/π_ref(y_l)))
```

Where y_w is the preferred response and y_l is the dispreferred response.

## Claude Summary

DPO revolutionized LLM alignment by simplifying the RLHF pipeline:

**RLHF (before DPO)**:
1. Collect preferences
2. Train reward model
3. Use PPO to optimize policy against reward model
4. Complex, unstable, expensive

**DPO**:
1. Collect preferences
2. Optimize directly with classification loss
3. Simple, stable, efficient

**Key insight**: The policy implicitly defines a reward model, so you can skip explicit reward modeling.

**Impact**: Now the dominant approach for preference-based fine-tuning. Most open-source alignment uses DPO or variants.

## Relevance

**Critical for AI alignment.** Transformed how LLMs are aligned to human preferences. One of the most influential papers in modern LLM training. Understanding DPO is essential for alignment research.
