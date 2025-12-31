# An alignment safety case sketch based on debate

**arXiv:** [2505.03989](https://arxiv.org/abs/2505.03989)
**Authors:** Marie Davidsen Buhl, Jacob Pfau, Benjamin Hilton, Geoffrey Irving
**Date:** 2025-05-06
**Categories:** cs.AI

## Abstract

If AI systems match or exceed human capabilities on a wide range of tasks, it may become difficult for humans to efficiently judge their actions -- making it hard to use human feedback to steer them towards desirable traits. One proposed solution is to leverage another superhuman system to point out flaws in the system's outputs via a debate. This paper outlines the value of debate for AI safety, as well as the assumptions and further research required to make debate work. It does so by sketching an ``alignment safety case'' -- an argument that an AI system will not autonomously take actions which could lead to egregious harm, despite being able to do so. The sketch focuses on the risk of an AI R\&D agent inside an AI company sabotaging research, for example by producing false results. To prevent this, the agent is trained via debate, subject to exploration guarantees, to teach the system to be honest. Honesty is maintained throughout deployment via online training. The safety case rests on four key claims: (1) the agent has become good at the debate game, (2) good performance in the debate game implies that the system is mostly honest, (3) the system will not become significantly less honest during deployment, and (4) the deployment context is tolerant of some errors. We identify open research problems that, if solved, could render this a compelling argument that an AI system is safe.

---
*Metadata fetched via arxiv API on 2025-12-31*
