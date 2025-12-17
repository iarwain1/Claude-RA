# Advancing the Test Science of LLM-enabled Systems: A Survey of Factors and Conditions that Matter Most

**Authors:** Karen O'Brien (Modern Technology Solutions, Inc.)
**Year:** 2025 (September)
**URL:** https://itea.org/journals/volume-46-3/advancing-the-test-science-of-llm-enabled-systems/

## Key Contributions

1. **DoD T&E perspective** on LLM evaluation - bridges gap between academic/industry practices and military scientific rigor
2. **Factor and condition identification** for LLM-enabled system performance
3. **LLM-as-Judge limitations** for complex cognitive tasks - recommends human SME scoring
4. **Architecture-based evaluation** - each functional node is a potential evaluation point
5. **Reusable test designs** for ongoing performance monitoring

## Overview

Addresses the gap between LLM testing practices in academia/industry and DoD test and evaluation (T&E) scientific standards. Focuses on Warfighter applications where LLM limitations demand rigorous testing for mission success.

## Key Findings

### Architecture-Based Evaluation

> "Because the architectures of LLM-enabled systems vary significantly—ranging from providing input directly to the LLM model to more complex systems that embed LLMs as a component wrapped in layers of guardrails and software interfaces—it is critical to obtain an architecture diagram. Each functional node, and connection between nodes, is a potential source of evaluation questions, factors, and conditions."

**Implication:** Evaluation must be tailored to system architecture, not generic across all LLM applications.

### LLM-as-Judge Limitations

> "LLM-as-Judge may be suitable for low-level cognitive tasks (such as recall or list) for which there is exactly one correct answer, however, for more complex cognitive tasks, such as summarization, reasoning, and disambiguation, where more judgment and nuance is required, human subject matter experts (SMEs) may be a better choice to score responses."

**Cognitive task spectrum:**
| Task Type | LLM-as-Judge Suitability | Recommended Scorer |
|-----------|-------------------------|-------------------|
| Recall/List | Suitable | LLM or Human |
| Single correct answer | Suitable | LLM |
| Summarization | Less suitable | Human SME |
| Reasoning | Less suitable | Human SME |
| Disambiguation | Less suitable | Human SME |

### Agreement Rates (External Research Cited)

- **Dietetics domain:** 68% agreement between SMEs and LLM judges
- **Mental health domain:** 64% agreement between SMEs and LLM judges

These rates highlight the gap when evaluating complex cognitive tasks.

### Challenges to Probe

The paper identifies specific LLM behaviors that require testing:
- **Model sycophancy** - Agreeing with user even when incorrect
- **Reversal curse** - Difficulty with bidirectional knowledge
- **Scoring consistency** - Variability in automated scoring

### Test Design Philosophy

> "The methodologies described require a substantial up-front investment to design appropriate tests for LLM-enabled systems, given requirements and available resources. However, once created, the test design can be reused to monitor the performance of LLM-enabled systems over time."

**Key insight:** Investment in rigorous test design pays off through reusability for ongoing monitoring.

## Relevance to Review

**Highly relevant for rigorous evaluation methodology.** Key insights:

### Alignment with Practitioner Guidance

| ITEA Recommendation | Husain Guidance | Assessment |
|--------------------|-----------------|------------|
| Human SME for complex tasks | Domain experts evaluate | **Strongly aligned** |
| Architecture-specific evaluation | Error analysis per workflow stage | **Aligned** |
| Reusable test designs | Test suite accumulation | **Aligned** |
| LLM-as-Judge for simple tasks | LLM-as-judge for objective failures | **Aligned** |

### Novel Contributions

1. **DoD scientific rigor standard** - Higher bar than typical industry practice
2. **Explicit cognitive task categorization** - Clear guidance on when LLM-as-judge fails
3. **Architecture diagram requirement** - Systematic identification of evaluation points
4. **Specific challenge areas** - Sycophancy, reversal curse, scoring as test targets

### Implications for Different Prompt Types

| Prompt Type | ITEA-Informed Approach |
|-------------|----------------------|
| Simple queries | LLM-as-Judge acceptable |
| Complex reasoning prompts | Human SME scoring required |
| System prompts | Architecture-based evaluation points |
| Multi-component systems | Evaluate each node and connection |

## Citations to Follow

- DoD Director, Operational Test and Evaluation 2009 standards
- Defense and Aerospace Test and Analysis Workshop presentation
- Literature on model sycophancy, reversal curse

## Questions/Notes

- **Strength:** DoD rigor provides higher standard than typical industry guidance
- **Strength:** Explicit cognitive task categorization is actionable
- **Strength:** Architecture-based approach is systematic
- **Practical insight:** 68% and 64% agreement rates quantify LLM-as-judge limitations
- **Gap:** Limited specifics on how to implement reusable test designs
- **Gap:** No discussion of automated test generation
- **Connects to:** husain2024llmjudge (LLM-as-judge methodology), husain2025evalsfaq (agentic evaluation)
- **Currency:** September 2025, very current
- **Author context:** 20+ years Army civilian experience, Chief Evaluator background

## Evidence Quality

**Medium-high for methodology guidance.** Based on DoD T&E experience and literature survey. Strong for "what rigorous evaluation requires"; weaker for empirical validation of recommendations. The 68%/64% agreement rates are cited from external research (not original study).
