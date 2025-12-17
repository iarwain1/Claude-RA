# Agentic Context Engineering: Evolving Contexts for Self-Improving Language Models

**Authors:** Qizheng Zhang, Changran Hu, Shubhangi Upasani, Boyuan Ma, Fenglu Hong, Vamsidhar Kamanuru, Jay Rainton, Chen Wu, Mengmeng Ji, Hanchen Li, Urmish Thakker, James Zou, Kunle Olukotun
**Affiliations:** Stanford University, SambaNova Systems, UC Berkeley
**Year:** 2025 (October)
**URL:** https://arxiv.org/abs/2510.04618

## Key Contributions

1. **ACE framework** - Treats contexts as evolving "playbooks" rather than static prompts
2. **Three-role architecture:** Generator, Reflector, Curator for context evolution
3. **Addresses brevity bias and context collapse** - Common problems in iterative prompting
4. **No labeled supervision required** - Adapts using natural execution feedback
5. **Significant performance gains:** +10.6% AppWorld, +8.6% finance reasoning, 86.9% latency reduction

## Methodology

ACE maintains context as a living "playbook" through three components:

| Role | Function |
|------|----------|
| **Generator** | Executes tasks, produces trajectories (reasoning/tool calls), exposes helpful vs harmful moves |
| **Reflector** | Distills concrete lessons from execution traces |
| **Curator** | Converts lessons into typed delta items with helpful/harmful counters, merges deterministically |

### Key Design Choices

- **Small delta items** merged incrementally (avoids brevity bias)
- **De-duplication and pruning** keeps playbook targeted (avoids context collapse)
- **Helpful/harmful counters** track strategy effectiveness over time

## Key Findings

### Performance Results

| Benchmark | Improvement |
|-----------|-------------|
| AppWorld agent tasks | +10.6% |
| Finance reasoning | +8.6% |
| Latency reduction | ~86.9% vs baselines |

**AppWorld leaderboard:** ACE matches top-ranked production-level agent on overall average, surpasses on harder test-challenge split, despite using smaller open-source model.

### Key Problems Addressed

**Brevity bias:** Prior approaches drop domain insights for concise summaries
**Context collapse:** Iterative rewriting erodes details over time

**Solution:** Incremental delta merging with explicit helpful/harmful tracking.

### Self-Improvement Without Supervision

> "Notably, ACE could adapt effectively without labeled supervision and instead by leveraging natural execution feedback."

Learns from task execution outcomes rather than human labels.

## Relevance to Review

**Relevant for automated prompt/context optimization.** Key insights:

### For Prompt Evaluation

1. **Context evolution requires evaluation feedback** - ACE uses execution success/failure
2. **Brevity bias is measurable** - Context length compression is a failure mode to watch
3. **Context collapse is measurable** - Detail erosion over iterations is trackable
4. **Helpful/harmful tracking** - Binary classification of strategy effectiveness

### Mapping to Evaluation Needs

| ACE Concept | Evaluation Implication |
|-------------|----------------------|
| Generator trajectories | Rich data for error analysis |
| Reflector lessons | Systematic failure categorization |
| Curator counters | Quantitative strategy assessment |
| Playbook evolution | Longitudinal prompt quality tracking |

### Automated Optimization Implications

ACE suggests prompts/contexts can be:
- Evolved based on execution outcomes
- Tracked for quality degradation (collapse, brevity)
- Improved without human labeling

**But:** Still needs evaluation signal to determine if execution succeeded.

### Connects to Evaluation Subtopics

- **Prompt optimization:** Direct method for context improvement
- **Agentic evaluation:** Designed for agent task execution
- **Automated metrics:** Implicit evaluation through execution success

## Citations to Follow

- **Dynamic Cheatsheet** - Prior work on adaptive memory
- **AppWorld benchmark** - Agent task evaluation
- **GitHub repository:** https://github.com/ace-agent/ace-appworld

## Questions/Notes

- **Strength:** Addresses real problems (brevity bias, context collapse)
- **Strength:** Quantitative improvements on multiple benchmarks
- **Strength:** No labeled supervision requirement
- **Practical insight:** Execution feedback can drive context improvement
- **Limitation:** Requires tasks with clear success/failure signals
- **Limitation:** May not generalize to open-ended generation tasks
- **Gap:** No discussion of human evaluation of evolved contexts
- **Gap:** Unclear how to detect when evolution is going wrong
- **Connects to:** mei2025contextengineering (context engineering taxonomy), guo2025agentbenchmark (agent evaluation)
- **Currency:** October 2025, very current

## Evidence Quality

**Medium-high for empirical claims.** Clear benchmark results with specific numbers. Results on established benchmarks (AppWorld) add credibility. Limitation: focused on task completion rather than subjective quality evaluation.
