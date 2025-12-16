# Automated Red Teaming with GOAT: the Generative Offensive Agent Tester

**arXiv:** https://arxiv.org/abs/2410.01606
**Authors:** Maya Pavlova, Erik Brinkman, Krithika Iyer, Vitor Albiero, Joanna Bitton, Hailey Nguyen, Joe Li, Cristian Canton Ferrer, Ivan Evtimov, Aaron Grattafiori
**Date:** 2024-10-02

## Abstract

Red teaming assesses how LLMs can produce content violating norms, policies, and safety rules. However, most automated methods don't represent how humans actually interact with AI.

**The gap**: Real users don't have ML expertise, don't access model internals, and don't spend lots of time crafting single adversarial prompts. They use techniques shared online and exploit multi-turn conversations.

## The GOAT System

**Generative Offensive Agent Tester (GOAT)** simulates plain-language adversarial conversations using multiple prompting techniques.

**Process:**
1. Given violating objective + attack information
2. Attacker LLM converses with target LLM
3. Each turn: "observation, thought, and strategy" reasoning
4. External judge evaluates final conversation

**Attack repertoire:**
- Instantiated with 7 red teaming attacks
- Encourages reasoning through available methods
- Adapts based on target model's responses

## Key Results

Superior Attack Success Rate (ASR@10):
- **97%** against Llama 3.1
- **88%** against GPT-4-Turbo

Outperforms existing methods (e.g., Crescendo) within equivalent query budgets.

## Claude Summary

GOAT addresses a key gap in automated red teaming:

**Why realistic attacks matter**:
- Most automated methods use techniques unavailable to typical users
- Real jailbreaks spread through social channels
- Multi-turn conversations enable escalation tactics
- Understanding realistic threats is essential for practical safety

**Key innovation**: Agent-based approach with reasoning allows adaptive, multi-turn attacks that mirror human behavior better than optimization-based methods.

**Concerning results**: Very high success rates against frontier models suggest current defenses may be inadequate against persistent, realistic attackers.

## Relevance

Important tool for realistic red teaming. From Meta AI, suggesting internal use for model safety. High success rates are concerning for current safety approaches. Useful for understanding the actual threat landscape.
