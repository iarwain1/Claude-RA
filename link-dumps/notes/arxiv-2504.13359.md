# Cost-of-Pass: An Economic Framework for Evaluating Language Models

**arXiv:** [2504.13359](https://arxiv.org/abs/2504.13359)
**Authors:** Mehmet Hamza Erol, Batu El, Mirac Suzgun, Mert Yuksekgonul, James Zou
**Date:** 2025-04-17
**Categories:** cs.AI, cs.CL

## Abstract

The widespread adoption of AI systems in the economy hinges on their ability to generate economic value that outweighs their inference costs. Evaluating this tradeoff requires metrics that account for both performance and costs. We propose a framework grounded in production theory for evaluating language models by combining accuracy and inference cost. We introduce "cost-of-pass", the expected monetary cost of generating a correct solution. We then define the "frontier cost-of-pass" as the minimum cost-of-pass achievable across available models or the "human-expert, using the approximate cost of hiring an expert. Our analysis reveals distinct economic insights. First, lightweight models are most cost-effective for basic quantitative tasks, large models for knowledge-intensive ones, and reasoning models for complex quantitative problems, despite higher per-token costs. Second, tracking this frontier cost-of-pass over the past year reveals significant progress, particularly for complex quantitative tasks where the cost has roughly halved every few months. Third, to trace key innovations driving this progress, we examine counterfactual frontiers: estimates of cost-efficiency without specific model classes. We find that innovations in lightweight, large, and reasoning models have been essential for pushing the frontier in basic quantitative, knowledge-intensive, and complex quantitative tasks, respectively. Finally, we assess the cost-reductions afforded by common inference-time techniques like majority voting and self-refinement, finding that their marginal accuracy gains rarely justify their costs. Our findings underscore that complementary model-level innovations are the primary drivers of cost-efficiency, and our economic framework provides a principled tool for measuring this progress and guiding deployment.

---
*Metadata fetched via arxiv API on 2025-12-31*
