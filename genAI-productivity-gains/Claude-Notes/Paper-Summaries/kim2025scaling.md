# Towards a Science of Scaling Agent Systems

**Authors:** Yubin Kim, Ken Gu, Chanwoo Park, Chunjong Park, Samuel Schmidgall, A. Ali Heydari, Yao Yan, Zhihan Zhang, Yuchen Zhuang, Mark Malhotra, Paul Pu Liang, Hae Won Park, Yuzhe Yang, Xuhai Xu, Yilun Du, Shwetak Patel, Tim Althoff, Daniel McDuff, Xin Liu
**Affiliations:** MIT, Google, Meta, University of Washington, and other institutions (19 authors total)
**Date:** December 9, 2025 (revised December 17, 2025)
**Type:** Academic Research Paper
**arXiv:** [2512.08296](https://arxiv.org/abs/2512.08296)
**Categories:** cs.AI, cs.MA (Artificial Intelligence, Multiagent Systems)

## Key Contributions

1. **First systematic study of scaling laws for LLM agent coordination**: Addresses gap in understanding multi-agent system scaling compared to well-established single-model scaling laws
2. **Controlled evaluation across 180 configurations**: 5 agent architectures × multiple benchmarks × multiple LLM families
3. **Predictive framework**: Coordination metrics that successfully predict optimal strategies across most configurations
4. **Three critical scaling effects identified**: Tool-coordination tradeoff, diminishing coordination returns, topology-dependent error propagation
5. **Empirical validation on frontier models**: Results hold across state-of-the-art LLMs

## Methodology

**Research Design:**
- **Architectures tested**: 5 variants (single-agent + 4 multi-agent coordination structures)
- **Benchmarks**: Multiple task types (parallelizable vs. sequential reasoning)
- **LLM families**: Multiple frontier models
- **Total configurations**: 180 (5 architectures × benchmarks × models)
- **Analysis**: Cross-validation of predictive model for coordination strategy selection

**Multi-Agent Variants:**
- Centralized coordination
- Decentralized coordination
- Hierarchical coordination
- Sequential coordination

## Key Findings

### 1. Three Critical Scaling Effects

**Tool Usage vs. Multi-Agent Overhead Trade-off:**
- Under fixed computational budgets, there's fundamental tension
- Adding agents means less budget for tool usage
- Adding tools means less budget for coordination
- **Implication**: Must optimize architecture for budget constraints

**Diminishing Returns from Coordination:**
- Coordination benefits plateau once single-agent performance reaches ~45%
- Below 45%: Multi-agent coordination can provide substantial gains
- Above 45%: Additional agents add overhead without proportional benefit
- **Implication**: Don't add multi-agent complexity if single agent is already good enough

**Topology-Dependent Error Propagation:**
- Error rates vary significantly based on coordination structure
- Sequential architectures propagate errors more
- Parallel/centralized architectures more robust
- **Implication**: Architecture choice affects reliability, not just performance

### 2. Performance Results by Task Type

**Parallelizable tasks:**
- **Centralized coordination: 80.8% improvement** over single-agent
- Multi-agent coordination highly effective
- Well-suited for divide-and-conquer problems

**Sequential reasoning tasks:**
- **Performance degraded across ALL multi-agent variants**
- Single-agent outperformed multi-agent
- Coordination overhead outweighed collaboration benefits
- **Implication**: Multi-agent ≠ always better

### 3. Predictive Framework Success

- Successfully predicts optimal coordination strategies for most configurations
- Uses coordination metrics (task parallelizability, error propagation, overhead)
- Enables informed architectural decisions without exhaustive testing
- **Implication**: Can guide architecture selection for new tasks/domains

## Relevance to GenAI Productivity Review

### Part 1: The Benchmark-Utility Gap

**Moderate relevance.** While not directly about benchmarks, highlights that agent system evaluation must account for:
- Task characteristics (parallelizable vs. sequential)
- Budget constraints (tool vs. coordination tradeoff)
- Coordination overhead (which benchmarks may not capture)

Connects to [pan2025agents](pan2025agents.md): Production agents are constrained by budgets (68% need human at ≤10 steps), which aligns with Kim et al.'s tool-coordination tradeoff finding.

### Part 2: The State of the Field (Literature Review)

**Important inclusion.** Represents state-of-the-art thinking on agent system scaling. Complements other agent evaluation work:
- [pan2025agents](pan2025agents.md): Production agent reality (short chains, human-in-loop)
- Kim et al.: Theoretical framework for when multi-agent makes sense

### Part 3: A Framework for AI Evaluation

**Highly relevant for evaluation design:**

**Task-Architecture Matching Principle:**
- Parallelizable tasks → Multi-agent with centralized coordination
- Sequential reasoning → Single-agent (multi-agent degrades performance)
- **For DoD evaluations**: Must match architecture to task type, not assume multi-agent is always better

**45% Performance Threshold:**
- If single-agent already achieves >45% on task, multi-agent coordination likely not worth overhead
- **For DoD evaluations**: Test single-agent baseline first; only add multi-agent complexity if needed

**Budget Constraint Awareness:**
- Fixed budgets create tool-coordination tradeoffs
- **For DoD evaluations**: Evaluate under realistic budget constraints, not unlimited compute

### Part 4: Practical Guidance for Acquisition Decision-Makers

**Key lessons for DoD acquisition:**

1. **Multi-agent ≠ automatically better:**
   - Sequential reasoning tasks showed degraded performance with multi-agent
   - Don't add architectural complexity without task-specific justification

2. **Match architecture to task type:**
   - Parallelizable tasks (e.g., multi-source intelligence fusion): Multi-agent with centralized coordination (80.8% improvement)
   - Sequential reasoning (e.g., legal analysis, strategic planning): Single-agent (multi-agent degrades)

3. **Budget constraints matter:**
   - Tool usage vs. coordination is zero-sum under fixed budgets
   - Plan computational budgets around actual operational constraints
   - Don't extrapolate from unlimited-compute research demos

4. **45% threshold for coordination:**
   - Test single-agent baseline first
   - Only add multi-agent if single-agent <45% performance
   - Avoid premature optimization with complex architectures

5. **Error propagation varies by topology:**
   - Sequential architectures propagate errors
   - Centralized/parallel more robust
   - **For mission-critical systems**: Choose architectures that minimize error propagation

### Part 5: T&E Considerations for GenAI-Based Systems

**Evaluation framework implications:**

1. **Task characterization required:**
   - Before evaluating multi-agent system, characterize task (parallelizable vs. sequential)
   - Different architectures for different task types

2. **Baseline comparison:**
   - Always evaluate single-agent baseline
   - Multi-agent must justify overhead cost

3. **Budget-constrained testing:**
   - Test under operational budget constraints
   - Measure tool-coordination tradeoffs

4. **Error propagation testing:**
   - Test error propagation for chosen topology
   - Sequential architectures need extra scrutiny

### Part 6: Research Agenda and Investment Priorities

**Critical for research planning:**

**DoD-specific multi-agent applications:**
- **Intelligence fusion** (parallelizable): Multi-agent likely beneficial
- **Strategic planning** (sequential reasoning): Single-agent likely better
- **Collaborative autonomous vehicles**: Need error propagation analysis
- **Multi-domain operations**: Complex coordination requirements

**Research gaps:**
1. **Domain-specific scaling laws**: Do these results generalize to military domains?
2. **Human-agent coordination**: This paper is LLM-only; add human to mix?
3. **Adversarial environments**: How do coordination strategies change under attack?
4. **Real-time constraints**: How do latency requirements affect coordination choices?
5. **Heterogeneous agents**: This studied homogeneous LLMs; what about mixed capabilities?

**Investment priorities:**
- Fund DoD-specific agent scaling studies (military tasks, adversarial environments)
- Develop evaluation frameworks for task characterization (parallelizable vs. sequential)
- Research error propagation in safety-critical multi-agent systems
- Study human-agent coordination scaling (not just agent-agent)

## Critical Assessment

**Strengths:**
- Systematic evaluation across 180 configurations
- Multiple architectures, benchmarks, and model families
- Identifies actionable principles (45% threshold, task-architecture matching)
- Predictive framework enables generalization
- Strong author team (MIT, Google, Meta, UW)
- Validated on frontier models (not just older/smaller models)

**Limitations:**
- **Homogeneous agents**: All agents use same LLM; doesn't study heterogeneous teams
- **Task coverage**: Benchmark tasks may not represent all real-world scenarios
- **No human-in-the-loop**: Studies agent-agent coordination only, not human-agent
- **Cost-free evaluation**: Assumes evaluation/testing is free (not true in DoD context)
- **Non-adversarial**: Doesn't consider adversarial environments or attacks
- **Short timeframe**: December 2025 preprint, not yet peer-reviewed

**Currency:** Excellent—December 2025, very recent work on emerging topic (multi-agent systems).

**Evidence Quality:** High. Systematic evaluation with 180 configurations, multiple validation approaches, and strong author team. Preprint status (not peer-reviewed yet) is minor limitation given quality of work.

## Connections to Other References

**Directly connects to:**
- [pan2025agents](pan2025agents.md): Pan shows production agents are short (≤10 steps), constrained, human-in-loop. Kim shows why: tool-coordination tradeoffs under budgets, and multi-agent overhead often not worth it.
- **Agent evaluation benchmarks**: Kim's framework suggests many agent benchmarks may not capture coordination overhead and error propagation

**Contrasts with:**
- **Research demos of long-horizon autonomous agents**: Kim shows multi-agent can degrade performance on sequential tasks, yet research often assumes more agents = better

**Complements:**
- [bean2025construct](bean2025construct.md): Bean shows benchmarks often don't measure what they claim; Kim adds that agent benchmarks may not capture coordination overhead
- [brand2025benchmarking](brand2025benchmarking.md): Brand shows 11-15% variance from scaffolds; Kim's framework suggests scaffold choice (single vs. multi-agent) could have even larger impact

**Relevant to:**
- **DoD multi-agent applications**: Intelligence fusion, collaborative autonomy, multi-domain operations
- **T&E framework**: Need task characterization (parallelizable vs. sequential) before choosing architecture

## Questions/Notes

1. **Do these scaling laws generalize to military domains?**
   - Benchmarks used are general (not military-specific)
   - Need validation on DoD-relevant tasks

2. **How does human-agent coordination change the scaling laws?**
   - This paper is agent-agent only
   - Most DoD applications will have humans in loop
   - Do the same tradeoffs apply?

3. **What about adversarial environments?**
   - Multi-agent coordination could be attacked/disrupted
   - Do coordination strategies need to change under attack?

4. **How to characterize tasks as "parallelizable" vs. "sequential"?**
   - Paper doesn't provide clear operationalization
   - DoD evaluators need concrete criteria

5. **What's the 45% threshold for DoD tasks?**
   - Threshold derived from benchmark tasks
   - May be different for military applications
   - Need DoD-specific validation

6. **Cost of evaluation:**
   - Paper assumes testing is free
   - DoD testing is expensive and time-constrained
   - How to apply framework when can't test all 180 configurations?

## Citation Guidance

**Appropriate uses:**
- Citing 80.8% improvement for parallelizable tasks with centralized coordination
- Documenting multi-agent degradation on sequential reasoning tasks
- Supporting task-architecture matching principle
- Citing 45% coordination threshold
- Referencing tool-coordination tradeoff under budget constraints
- Supporting need for single-agent baselines before multi-agent

**Inappropriate uses:**
- Claiming these scaling laws definitely apply to military domains (not validated)
- Using to make claims about human-agent coordination (study is agent-agent only)
- Citing as peer-reviewed work (still preprint as of Dec 2025)
- Applying 45% threshold without domain-specific validation
- Ignoring adversarial considerations (study assumes cooperative environment)

**Citation note:** High-quality preprint from strong author team (MIT, Google, Meta, UW) with systematic evaluation. Suitable for citing in technical reports as "recent research on agent scaling" with caveat that it's not yet peer-reviewed and focused on LLM-agent coordination (not human-agent). Findings should be validated in DoD-specific contexts before relying on them for major acquisition decisions.

**DoD relevance:** While not DoD-specific, this paper provides important theoretical framework for understanding when multi-agent architectures make sense. Particularly relevant as DoD explores multi-agent collaborative systems for intelligence, autonomy, and multi-domain operations. The task-architecture matching principle and coordination overhead insights could save DoD from over-investing in multi-agent complexity where single-agent would suffice.
