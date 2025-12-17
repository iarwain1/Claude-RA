# Open Research Questions

Questions and gaps identified during the literature review.

## Main Research Questions

- How do you evaluate prompt effectiveness when the "correct" output is subjective or task-dependent?
- What metrics best capture prompt quality across different use cases (consumer chat, system prompts, agentic workflows)?
- How do you balance automated evaluation (scalability) with human evaluation (accuracy)?
- How do evaluation approaches differ between one-off prompts vs. system-level prompt design?
- What role should LLM-as-judge play in prompt evaluation, and what are its limitations?

## Emerging Questions

Based on initial source review:

- How does the "three levels" framework (assertions → model-based → A/B tests) apply to different prompt types?
- What is the relationship between error analysis and eval design?
- How do you measure LLM-as-judge agreement with human judgments systematically?
- What is the "tools trap" and how does it affect evaluation practices?
- How do you prevent "context collapse" in iterative prompting workflows?
- What makes synthetic data generation effective for evaluation?

## Gaps in Literature

To investigate:

- Evaluation methodologies specific to *user* prompts vs. *system* prompts
- Cross-model evaluation (do good prompts for GPT-4 transfer to Claude?)
- Real-time evaluation for interactive/streaming use cases
- Evaluation of prompt robustness and edge cases
- Cost-benefit analysis of different evaluation approaches
