# PromptCoT 2.0: Scaling Prompt Synthesis for Large Language Model Reasoning

**Authors:** Xueliang Zhao, Wei Wu, Jian Guan, Zhuocheng Gong, Lingpeng Kong
**Year:** 2025 (September)
**URL:** https://arxiv.org/abs/2509.19894

## Key Contributions

1. **EM-based prompt synthesis:** Replaces hand-crafted heuristics with learnable optimization
2. **Domain-agnostic framework:** Works across mathematics and programming
3. **Two training regimes:** Self-Play (no teacher) and Supervised Fine-Tuning
4. **State-of-the-art results:** New benchmarks at 30B scale

## Overview

Addresses the bottleneck of high-quality training problems for LLM reasoning. Human-curated datasets are costly and limited; existing synthetic corpora are often too easy or narrow. PromptCoT 2.0 uses an EM loop to iteratively refine rationales that guide prompt construction.

## Methodology

### Core Innovation

> "PromptCoT 2.0 is a scalable framework that replaces hand-crafted heuristics with an expectation-maximization (EM) loop, where rationales are iteratively refined to guide prompt construction."

### Training Regimes

| Regime | Description | Use Case |
|--------|-------------|----------|
| **Self-Play** | Strong models improve autonomously via verifiable feedback | No stronger teacher available |
| **SFT** | Weaker models learn from teacher-distilled traces | Bootstrapping smaller models |

### PromptCoT 1.0 → 2.0 Evolution

| Version | Approach |
|---------|----------|
| 1.0 | Inject rationales into prompt synthesis to increase difficulty |
| 2.0 | EM-based optimization, fully learnable, domain-agnostic |

## Key Findings

### Self-Play Results (Qwen3-30B-A3B-Thinking-2507)

| Benchmark | Improvement |
|-----------|-------------|
| AIME 24 | +4.4 |
| AIME 25 | +4.8 |
| HMMT 25 | +5.3 |
| LiveCodeBench v5 | +6.1 |
| LiveCodeBench v6 | +5.0 |
| Codeforces | +35 Elo |

### SFT Results (Qwen2.5-7B-Instruct)

Training solely on synthetic prompts:
- **AIME 24:** 73.1 accuracy
- **AIME 25:** 65.6 accuracy
- **LiveCodeBench v5:** 53.4 accuracy

> "Surpassing models trained on human or hybrid data."

### Data Scale

- **4.8M fully synthetic prompts + trajectories** for SFT
- Self-play datasets: 11K (30B) and 48K (4B)

## Relevance to Review

**Relevant for automated prompt optimization.** Key insights:

### For Prompt Evaluation

1. **Synthetic prompt generation:** Can create evaluation data at scale
2. **Difficulty calibration:** EM loop can target specific difficulty levels
3. **Verifiable feedback:** Self-play relies on verifiable task outcomes
4. **Domain-agnostic:** Framework generalizes across math and code

### Implications for Evaluation

| PromptCoT Concept | Evaluation Implication |
|-------------------|----------------------|
| Synthetic prompts | Can generate eval test cases |
| Difficulty scaling | Control complexity of evaluation scenarios |
| Self-play verification | Automated correctness checking |
| Domain transfer | Evaluation frameworks may generalize |

### Connections to Other Work

| Related Concept | Connection |
|-----------------|------------|
| ACE framework | Both use iterative refinement, different goals |
| Husain synthetic data | PromptCoT more structured than "give me test queries" |
| Benchmark generation | Could generate harder benchmark problems |

### Limitations for This Review

- **Focus on reasoning tasks:** Math and code, may not generalize to all prompting
- **Model training focus:** Less about evaluation, more about training data
- **Verifiable tasks only:** Requires ground truth for self-play

## Citations to Follow

- PromptCoT 1.0 paper
- AIME and HMMT benchmark details
- LiveCodeBench methodology
- Self-play learning literature

## Questions/Notes

- **Strength:** Strong empirical results across multiple benchmarks
- **Strength:** Domain-agnostic design
- **Strength:** Open-source implementation available
- **Practical insight:** Synthetic prompts can outperform human-curated data
- **Limitation:** Requires verifiable feedback (not all prompts have this)
- **Limitation:** Focused on reasoning, not evaluation methodology
- **Gap:** No discussion of evaluating the generated prompts themselves
- **Connects to:** ace2025contextengineering (automated improvement), prompt-optimization subtopic
- **Currency:** September 2025, very current

## Evidence Quality

**High for empirical claims.** Clear benchmark improvements with specific numbers. State-of-the-art results add credibility. Limitation: focused on training data generation rather than evaluation.
