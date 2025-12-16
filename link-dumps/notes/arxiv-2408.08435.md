# Automated Design of Agentic Systems (ADAS)

**arXiv:** https://arxiv.org/abs/2408.08435
**Authors:** Shengran Hu, Cong Lu, Jeff Clune
**Date:** 2024-08-15
**Venue:** ICLR 2025
**GitHub:** https://github.com/ShengranHu/ADAS

## Abstract

ADAS is a newly forming research area that aims to automatically create powerful agentic system designs, including inventing novel building blocks and/or combining them in new ways.

**Key insight**: The history of ML teaches that hand-designed solutions are eventually replaced by learned solutions. Agent architectures may follow this pattern.

## Meta Agent Search

The paper presents **Meta Agent Search**: an algorithm where a meta agent iteratively programs new agentic systems.

**How it works:**
- Entire agentic system defined in code
- Meta agent discovers new agents by programming
- Builds upon archive of prior agents
- Continuously refines discovered designs

**Theoretical basis**: Turing completeness of programming languages implies any conceivable agentic system can be discovered in code space.

## Key Results

Automatically created agents improve performance by up to 14% across tasks:

- **ARC Challenge**: Outperforms COT and Self-Consistency baselines
- **Reading Comprehension (DROP)**: +13.6 F1 improvement over SOTA
- **Math (MGSM)**: +14.4% accuracy over baselines

**Transfer**: Discovered agents maintain performance when transferred across different models and domains.

## Claude Summary

ADAS represents an interesting approach to automating agent architecture design:

**The bet**: Just as neural architecture search found designs humans wouldn't, meta-agent search might discover novel agentic patterns.

**Why it might work**:
- Large search space of possible agent designs
- Clear optimization signal (task performance)
- Code representation is flexible and expressive

**Caveats**:
- Current improvements are incremental, not revolutionary
- Search is expensive and may not generalize
- Hand-designed agents still competitive for many tasks

**Connection to AI safety**: Automated agent design could produce agents with unexpected behaviors. Need to consider safety as agents become self-designing.

## Relevance

Important for understanding the future of agent development. If meta-agent search scales, it could accelerate agent capability improvements. Relevant to discussions about recursive self-improvement and AI safety.
