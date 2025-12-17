# AI Evals FAQ (LLM Evals: Everything You Need to Know)

**Authors:** Hamel Husain, Shreya Shankar
**Year:** 2025
**URL:** https://hamel.dev/blog/posts/evals-faq/

## Key Contributions

1. **Comprehensive FAQ format** covering common evaluation questions from 2000+ practitioners trained
2. **Agentic workflow evaluation** methodology with two-level approach (end-to-end + step-level)
3. **RAG evaluation** framework separating retrieval (IR metrics) from generation (LLM-as-judge)
4. **Synthetic data generation** best practices using dimensional structure
5. **Anti-patterns** identified: eval-driven development, excessive model selection focus

## Methodology

Compiled from course materials and consulting experience. Practical Q&A format addressing real practitioner questions.

## Key Findings

### Evaluating Agentic Workflows

**Two-level approach:**

| Level | Focus | Method |
|-------|-------|--------|
| End-to-end | "Did we meet the user's goal?" | Human/LLM judges with precise success rules |
| Step-level | Individual component quality | Score tool choice, parameter extraction, error handling, context retention, efficiency |

**Transition failure matrices:** Transform overwhelming agent complexity into actionable insights by showing which state transitions cause most failures.

### RAG Evaluation

**Separate retrieval from generation:**

| Component | Evaluation Method |
|-----------|-------------------|
| Retrieval | IR metrics: Recall@k, Precision@k, MRR |
| Generation | Error analysis → human labels → LLM-as-judge |

**Synthetic test data for retrieval:** Take documents from corpus → extract key facts → generate questions those facts would answer. This reverse process creates query-document pairs without manual annotation.

**"RAG is Dead" clarification:** The viral claim was specifically about naive vector DB retrieval for coding agents, not RAG generally. Modern tools still use retrieval—just agentic search instead of pure vector similarity.

### Multi-Step Workflow Evaluation

- Use **both outcome and process metrics**
- Process metrics (step count, time, resources) are easier to debug—tackle first
- **Segment error analysis by stage:** Early stage errors cascade, so early improvements have most impact

### Synthetic Data Generation

**Common mistake:** Prompting "give me test queries" without structure → generic, repetitive outputs

**Better approach:** Define **dimensions** (categories describing different aspects of user queries). Each dimension captures one type of variation in user behavior.

**Limitations:**
- Can mislead or mask issues
- LLMs miss structure/nuance of specialized documents (legal, medical, technical)
- Real examples needed for critical edge cases

### Eval-Driven Development

**Generally no.** Unlike traditional software with predictable failure modes, LLMs have infinite failure surface area.

**Better approach:** Start with error analysis. Write evaluators for errors you discover, not errors you imagine.

**Exception:** Known constraints with exact success criteria (e.g., "never mention competitors").

### Model Selection Time

**Don't fixate on model selection.** Start with error analysis first.

> "I suggest not thinking of switching model as the main axes of how to improve your system off the bat without evidence. Does error analysis suggest that your model is the problem?"

### Same Model for Task and Evaluation

**Usually fine.** The judge is doing a different task than your main pipeline. While research shows models can exhibit bias evaluating their own outputs, what matters is alignment with human judgments.

### Annotation Tools

- **One domain expert** who understands users as quality decision maker ("benevolent dictator")
- **Notebooks** are the single most effective tool—arbitrary code, visualization, fast iteration
- **Build most evaluators from scratch**—generic metrics rarely capture what matters

## Relevance to Review

**Highly relevant for prompt evaluation scope.** Key insights:

1. **Agentic prompt evaluation** needs two levels: outcome success + step diagnostics
2. **RAG prompts** need separate retrieval vs. generation evaluation
3. **Synthetic data** can bootstrap evaluation but has limits
4. **Don't pre-specify** evaluation criteria—discover through error analysis
5. **Model switching** is not the primary improvement lever for prompts

### Implications for Different Prompt Types

| Prompt Type | Evaluation Approach |
|-------------|---------------------|
| User prompts (consumer) | Error analysis → failure taxonomy → targeted evals |
| System prompts | End-to-end + component-level evaluation |
| Agentic/tool prompts | Two-level: task success + step diagnostics |
| RAG prompts | Separate retrieval (IR) from generation (LLM judge) |

## Citations to Follow

- **Jason Liu** - "There Are Only 6 RAG Evals" (referenced for RAG framework)
- **Shreya Shankar** - Co-author, academic research on evaluation
- **Claude Code / agentic search** - Example of modern retrieval approach

## Questions/Notes

- **Strength:** Practical FAQ format addresses real practitioner pain points
- **Strength:** Transition failure matrices for agentic systems is actionable
- **Gap:** Limited discussion of evaluating prompt *design* vs. prompt *outputs*
- **Gap:** Assumes production data exists—less guidance for pre-deployment evaluation
- **Useful heuristic:** "Does error analysis suggest your model is the problem?" before switching models
- **Currency:** December 2025, very current

## Evidence Quality

**Medium-High for practical guidance.** Synthesized from course materials with 2000+ practitioners. Strong for "what questions practitioners have" and "what approaches work in practice." Cannot cite for controlled empirical comparisons.
