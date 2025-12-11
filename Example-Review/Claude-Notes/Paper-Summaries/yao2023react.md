# ReAct: Synergizing Reasoning and Acting in Language Models

**Authors:** Yao, Shunyu; Zhao, Jeffrey; Yu, Dian
**Year:** 2023
**URL:** https://arxiv.org/abs/2210.03629

## Key Contributions
- Introduced ReAct paradigm: interleaving reasoning and acting
- Demonstrated improved performance over reasoning-only or acting-only approaches
- Showed benefits across diverse tasks (QA, fact verification, games)

## Methodology
- Prompted LLMs to generate both "thoughts" and "actions"
- Thoughts: reasoning about current situation, what to do next
- Actions: interactions with environment (search, lookup, etc.)
- Compared against chain-of-thought (reasoning only) and action-only baselines

## Key Findings
- ReAct outperforms baselines on HotpotQA, FEVER, and ALFWorld
- Reasoning traces help recover from errors
- Acting grounds reasoning in real information
- Synergy between reasoning and acting is greater than sum of parts

## Example Pattern
```
Thought: I need to find when the creator of Python was born
Action: Search[Python programming language creator]
Observation: Python was created by Guido van Rossum...
Thought: Now I need to find Guido van Rossum's birth date
Action: Search[Guido van Rossum birth date]
...
```

## Relevance to Review
Seminal paper introducing a widely-adopted agent pattern. Most modern LLM agents use some form of ReAct or build upon it.

## Citations to Follow
- Chain-of-Thought prompting (Wei et al.)
- Self-ask (Press et al.)
- Inner Monologue (Huang et al.)

## Questions/Notes
- How does this scale to more complex, multi-step tasks?
- What are the failure modes when reasoning goes wrong?
- How does model size affect ReAct performance?
