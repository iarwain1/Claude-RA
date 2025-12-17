# Experimental Design for Evaluating Prompt Effectiveness

**Draft Report**
**Date:** December 2025

---

## Executive Summary

This report addresses experimental design considerations for evaluating prompt effectiveness in LLM systems. While much practitioner literature focuses on *what* to measure, less attention has been given to *how* to design rigorous experiments that yield valid, reproducible conclusions about prompt quality.

Key challenges include:
- Non-deterministic outputs requiring statistical treatment
- Confounding variables (model versions, temperature, context)
- Lack of ground truth for subjective quality dimensions
- Rapid model evolution invalidating historical comparisons

This report synthesizes experimental design principles with emerging best practices from LLM evaluation literature.

---

## 1. Fundamental Design Considerations

### 1.1 Research Questions in Prompt Evaluation

Before designing an experiment, clarify the research question type:

| Question Type | Example | Design Implications |
|---------------|---------|---------------------|
| **Comparative** | "Is Prompt A better than Prompt B?" | A/B testing, paired comparisons |
| **Optimization** | "What prompt maximizes metric X?" | Iterative experimentation, search |
| **Diagnostic** | "Why does this prompt fail on case Y?" | Error analysis, case studies |
| **Generalization** | "Does this prompt work across contexts?" | Stratified sampling, cross-validation |
| **Threshold** | "Does this prompt meet quality bar Z?" | Acceptance testing, confidence intervals |

### 1.2 Units of Analysis

| Unit | Description | When to Use |
|------|-------------|-------------|
| **Single output** | One prompt → one response | Fine-grained analysis |
| **Prompt-input pair** | Same prompt, varied inputs | Input sensitivity analysis |
| **Prompt variant** | Varied prompts, same inputs | Prompt comparison |
| **Session/conversation** | Multi-turn interaction | Agentic/conversational systems |
| **User-level** | Aggregated across user's interactions | Production A/B tests |

### 1.3 The Reproducibility Challenge

LLM experiments face unique reproducibility challenges:

**Sources of Variance:**
- **Sampling variance** - Non-zero temperature produces different outputs
- **Model drift** - API models change without notice
- **Context sensitivity** - Small input changes cause large output changes
- **Positional effects** - Order of examples/instructions matters

**Mitigation Strategies:**
| Strategy | Implementation |
|----------|----------------|
| Fix temperature | Use temperature=0 for deterministic outputs when possible |
| Log model version | Record exact model ID (e.g., `claude-3-5-sonnet-20241022`) |
| Multiple runs | Generate n>1 outputs per condition, report distributions |
| Seed control | Use fixed seeds where APIs support them |
| Snapshot inputs | Version control all prompts, inputs, and evaluation criteria |

---

## 2. Experimental Designs

### 2.1 Within-Subject (Paired) Designs

**Structure:** Same inputs evaluated under multiple prompt conditions.

```
Input_1 → [Prompt_A] → Output_1A
Input_1 → [Prompt_B] → Output_1B
Input_2 → [Prompt_A] → Output_2A
Input_2 → [Prompt_B] → Output_2B
...
```

**Advantages:**
- Controls for input difficulty variation
- Higher statistical power (paired comparisons)
- Smaller sample sizes needed

**Disadvantages:**
- Cannot detect prompt × input interactions without larger designs
- Order effects if evaluation is sequential

**Statistical Analysis:**
- Paired t-test or Wilcoxon signed-rank for continuous metrics
- McNemar's test for binary pass/fail
- Mixed-effects models for more complex designs

**When to Use:**
- Comparing prompt variants
- A/B testing prompts on fixed test sets
- Regression testing after prompt changes

### 2.2 Between-Subject Designs

**Structure:** Different inputs (or users) assigned to different prompt conditions.

```
Input_1 → [Prompt_A] → Output_1A
Input_2 → [Prompt_A] → Output_2A
Input_3 → [Prompt_B] → Output_3B
Input_4 → [Prompt_B] → Output_4B
...
```

**Advantages:**
- No carryover effects
- More realistic for production A/B tests
- Can measure user-level effects

**Disadvantages:**
- Requires larger samples
- Input/user variation adds noise
- Randomization critical

**Statistical Analysis:**
- Independent t-test or Mann-Whitney U
- Chi-square for categorical outcomes
- ANCOVA to control for covariates

**When to Use:**
- Production A/B tests with real users
- When prompt exposure affects subsequent behavior
- Measuring adoption/engagement metrics

### 2.3 Factorial Designs

**Structure:** Systematically vary multiple factors.

```
Example: 2×2 factorial (Prompt Style × Few-Shot Examples)

                    Few-Shot: No    Few-Shot: Yes
Prompt Style: Terse      A              B
Prompt Style: Verbose    C              D
```

**Advantages:**
- Detect interactions between factors
- Efficient exploration of design space
- Identifies which factors matter most

**Disadvantages:**
- Conditions multiply quickly (2^k for k binary factors)
- Requires more test inputs
- Analysis more complex

**Statistical Analysis:**
- ANOVA or mixed-effects models
- Post-hoc comparisons with correction (Bonferroni, Tukey)

**When to Use:**
- Understanding which prompt components matter
- Optimizing across multiple dimensions
- Research-oriented investigations

### 2.4 Sequential/Adaptive Designs

**Structure:** Use results from early trials to guide later ones.

**Approaches:**
| Approach | Description |
|----------|-------------|
| **Bandit algorithms** | Shift traffic toward better-performing variants |
| **Bayesian optimization** | Model response surface, sample informatively |
| **Early stopping** | Terminate inferior variants before full sample |

**Advantages:**
- More efficient than fixed designs
- Reduces exposure to poor variants
- Faster iteration

**Disadvantages:**
- More complex to implement
- Harder to get clean statistical comparisons
- Risk of premature convergence

**When to Use:**
- High-volume production systems
- Costly evaluation (human labeling)
- Many variants to explore

---

## 3. Sampling and Test Set Design

### 3.1 Test Set Construction

**Key Principle from Literature:**
> "Use dimensional structure (categories of user query variation); avoid unstructured 'give me test queries' prompts" (Husain & Shankar, 2025)

**Dimensional Sampling Framework:**

1. **Identify dimensions** of variation in your use case:
   - Query complexity (simple, moderate, complex)
   - Domain area (if multi-domain)
   - Input length (short, medium, long)
   - Edge cases (malformed input, adversarial, empty)

2. **Create stratified sample** ensuring coverage:
   ```
   Dimension 1: Complexity    [Simple: 40%, Moderate: 40%, Complex: 20%]
   Dimension 2: Domain        [Domain A: 50%, Domain B: 50%]
   Dimension 3: Edge cases    [Normal: 90%, Edge: 10%]
   ```

3. **Size each stratum** based on importance and variance

### 3.2 Sample Size Considerations

**For Binary Outcomes (Pass/Fail):**

| Effect Size | Samples per Condition (80% power, α=0.05) |
|-------------|------------------------------------------|
| Large (20% difference) | ~80 |
| Medium (10% difference) | ~300 |
| Small (5% difference) | ~1,200 |

**For Continuous Metrics:**

Rule of thumb: 30+ samples per condition for Central Limit Theorem; more for high-variance outputs.

**Practical Guidance:**
- Start with 100+ test cases for initial evaluation
- Scale up for production A/B tests (thousands of users)
- Use power analysis if statistical significance required

### 3.3 Synthetic Data Generation

**When Ground Truth Exists:**
> "Documents → extract facts → generate questions those facts would answer (reverse process)" (Husain & Shankar, 2025)

**When Ground Truth is Scarce:**
- Use LLMs to generate diverse test inputs
- Human-validate a subset
- Apply dimensional structure to generation prompts
- Consider adversarial generation for robustness testing

**Caution:**
> "Synthetic prompts can outperform human-curated data" for some tasks (Zhao et al., 2025), but may miss real-world distribution.

---

## 4. Controlling Confounds

### 4.1 Common Confounding Variables

| Confound | Description | Mitigation |
|----------|-------------|------------|
| **Model version** | API models change | Log exact model ID, pin versions |
| **Temperature** | Affects output variance | Fix at 0 for comparisons, or sample multiple |
| **Context window** | Prior conversation affects output | Reset context between trials |
| **Time of day** | API latency/behavior may vary | Randomize timing, block by time |
| **Prompt position** | Order of examples matters | Randomize or counterbalance |
| **Evaluator fatigue** | Human raters degrade over time | Randomize presentation order |
| **Criteria drift** | Evaluation standards evolve | Anchor with reference examples |

### 4.2 Blocking and Stratification

**Blocking:** Group similar inputs, compare within blocks.
```
Block 1 (Simple queries): Prompt_A vs Prompt_B
Block 2 (Complex queries): Prompt_A vs Prompt_B
→ Analyze: Effect of prompt controlling for complexity
```

**Stratification:** Ensure balanced representation across strata.
```
Stratum 1 (Domain A): 50 inputs → 25 to Prompt_A, 25 to Prompt_B
Stratum 2 (Domain B): 50 inputs → 25 to Prompt_A, 25 to Prompt_B
```

### 4.3 Randomization

**Critical for causal inference.** Randomize:
- Assignment of inputs to prompt conditions
- Order of conditions in within-subject designs
- Order of items for human evaluation
- Selection of test cases from larger pools

---

## 5. Measurement and Evaluation

### 5.1 Choosing Metrics

**The Three-Level Framework (adapted from Husain, 2024):**

| Level | Metric Type | Example | When to Use |
|-------|-------------|---------|-------------|
| **Level 1** | Objective/automated | Format compliance, latency, cost | Always; foundation |
| **Level 2** | LLM-as-judge | Quality ratings, correctness | Scalable subjective evaluation |
| **Level 3** | Human evaluation | Expert ratings, user satisfaction | Ground truth, validation |

**Metric Selection Principles:**
1. Start with Level 1 metrics (fast, cheap, reproducible)
2. Add Level 2 for subjective dimensions
3. Validate Level 2 against Level 3 (human agreement)
4. Prefer binary (Pass/Fail) over ordinal (1-5 scales)

### 5.2 LLM-as-Judge Validation

**Required Before Trusting LLM Judgments:**

1. **Collect human labels** on 100+ examples (Husain, 2024)
2. **Compute agreement metrics:**
   - True Positive Rate (TPR): P(Judge=Fail | Human=Fail)
   - True Negative Rate (TNR): P(Judge=Pass | Human=Pass)
3. **Iterate** through 3-4 rounds until acceptable agreement
4. **Use TPR/TNR to correct** aggregate estimates

**Agreement Benchmarks:**
- Simple tasks: 90%+ agreement achievable
- Complex cognitive tasks: 64-68% agreement observed (O'Brien, 2025)

### 5.3 Inter-Rater Reliability

For human evaluation, measure and report:

| Metric | Use Case |
|--------|----------|
| **Cohen's κ** | Two raters, categorical |
| **Fleiss' κ** | Multiple raters, categorical |
| **ICC** | Multiple raters, continuous |
| **Krippendorff's α** | General purpose, handles missing data |

**Minimum Standards:**
- κ > 0.6 for substantial agreement
- κ > 0.8 for strong agreement
- Report raw agreement rates alongside κ

---

## 6. Analysis and Inference

### 6.1 Statistical Tests by Design

| Design | Metric Type | Recommended Test |
|--------|-------------|------------------|
| Paired (within-subject) | Binary | McNemar's test |
| Paired (within-subject) | Continuous | Paired t-test, Wilcoxon |
| Independent (between-subject) | Binary | Chi-square, Fisher's exact |
| Independent (between-subject) | Continuous | t-test, Mann-Whitney |
| Factorial | Any | ANOVA, mixed-effects models |
| Multiple comparisons | Any | Bonferroni, Holm, Tukey HSD |

### 6.2 Effect Size Reporting

**Always report effect sizes, not just p-values:**

| Metric Type | Effect Size Measure |
|-------------|---------------------|
| Binary outcomes | Odds ratio, risk difference |
| Continuous outcomes | Cohen's d, Hedges' g |
| Correlations | Pearson's r, Spearman's ρ |

**Interpretation (Cohen's d):**
- Small: d ≈ 0.2
- Medium: d ≈ 0.5
- Large: d ≈ 0.8

### 6.3 Confidence Intervals

Report confidence intervals for key estimates:
- Pass rate: 95% CI using Wilson or Clopper-Pearson
- Mean scores: 95% CI using t-distribution or bootstrap
- Differences: 95% CI for Prompt_A - Prompt_B

**Example Reporting:**
> "Prompt A achieved 78% pass rate (95% CI: 72-84%) compared to Prompt B at 65% (95% CI: 58-72%), a difference of 13 percentage points (95% CI: 4-22%, p < 0.01)."

### 6.4 Handling Multiple Comparisons

When comparing multiple prompts or metrics:

| Method | Approach | When to Use |
|--------|----------|-------------|
| **Bonferroni** | Divide α by number of tests | Conservative, few comparisons |
| **Holm** | Sequential Bonferroni | Less conservative |
| **Benjamini-Hochberg** | Control false discovery rate | Many comparisons, exploratory |
| **Pre-registration** | Declare primary outcome | Confirmatory experiments |

---

## 7. Practical Workflows

### 7.1 Error Analysis → Evaluation Design

**Recommended Sequence (from Husain, 2024):**

```
1. OBSERVE
   └── Review 100+ production traces
   └── Journal observations (open coding)

2. CATEGORIZE
   └── Develop failure taxonomy (axial coding)
   └── Identify error categories and frequencies

3. DESIGN EVALS
   └── Write evaluators for discovered (not imagined) errors
   └── Prioritize by frequency and severity

4. EXPERIMENT
   └── Test prompt modifications against baseline
   └── Use appropriate experimental design

5. ITERATE
   └── Review 100+ fresh traces every 2-4 weeks
   └── Update taxonomy and evaluators
```

### 7.2 Prompt Comparison Workflow

**For Comparing Two Prompts:**

```
1. PREPARE
   ├── Define success criteria (Level 1, 2, 3 metrics)
   ├── Construct test set (dimensional sampling)
   └── Set sample size based on effect size of interest

2. EXECUTE
   ├── Run both prompts on all test inputs
   ├── Fix model version, temperature
   └── Collect outputs and metadata

3. EVALUATE
   ├── Apply Level 1 metrics (automated)
   ├── Apply Level 2 metrics (LLM-as-judge, validated)
   └── Optional: Level 3 sample for validation

4. ANALYZE
   ├── Compute pass rates and confidence intervals
   ├── Test for statistical significance (paired design)
   └── Report effect sizes

5. DECIDE
   ├── Consider practical significance (not just statistical)
   ├── Account for cost/latency tradeoffs
   └── Document decision and rationale
```

### 7.3 Production A/B Testing

**For Live Traffic Experiments:**

```
1. GATE
   ├── Define success metrics and guardrails
   ├── Set minimum detectable effect
   └── Calculate required sample size

2. RANDOMIZE
   ├── Assign users (not requests) to conditions
   ├── Ensure balanced allocation
   └── Log assignment for analysis

3. MONITOR
   ├── Track guardrail metrics (errors, latency)
   ├── Early stopping rules for harm
   └── Daily health checks

4. ANALYZE
   ├── Intent-to-treat analysis (as randomized)
   ├── Account for multiple comparisons
   └── Check for heterogeneous effects (subgroups)

5. SHIP OR REVERT
   ├── Practical significance threshold
   ├── Consider long-term effects
   └── Document learnings
```

---

## 8. Threats to Validity

### 8.1 Internal Validity

| Threat | Description | Mitigation |
|--------|-------------|------------|
| **Selection bias** | Non-random test case selection | Random sampling, stratification |
| **Instrumentation** | Measurement changes over experiment | Fix evaluation criteria, anchor examples |
| **History** | External events affect outcomes | Short experiment duration, control group |
| **Maturation** | Model changes during experiment | Pin model version, short duration |
| **Testing effects** | Prior exposure affects performance | Between-subject design or washout |

### 8.2 External Validity

| Threat | Description | Mitigation |
|--------|-------------|------------|
| **Population validity** | Test set ≠ production distribution | Sample from production, stratify |
| **Ecological validity** | Lab conditions ≠ real use | Production A/B tests, realistic test sets |
| **Temporal validity** | Results don't generalize over time | Periodic re-evaluation, monitoring |
| **Model validity** | Results don't generalize across models | Multi-model testing, document model |

### 8.3 Construct Validity

| Threat | Description | Mitigation |
|--------|-------------|------------|
| **Metric mismatch** | Metrics don't capture true quality | Validate against human judgment |
| **Gaming** | Optimization to metric, not quality | Multiple metrics, human spot-checks |
| **Criteria drift** | Standards evolve unconsciously | Anchor ratings, periodic calibration |

---

## 9. Reporting Standards

### 9.1 Minimum Reporting Requirements

**Every prompt evaluation report should include:**

1. **Research Question:** What comparison/question was investigated?

2. **Experimental Design:**
   - Design type (within/between-subject, factorial)
   - Sample size and how determined
   - Randomization procedure

3. **Materials:**
   - Exact prompts used (or reference to version-controlled prompts)
   - Model and version (e.g., `claude-3-5-sonnet-20241022`)
   - Temperature and other parameters

4. **Test Set:**
   - Size and composition
   - Sampling procedure
   - Any known limitations

5. **Metrics:**
   - Definitions of all metrics
   - For LLM-as-judge: validation results (TPR/TNR)
   - For human evaluation: inter-rater reliability

6. **Results:**
   - Point estimates with confidence intervals
   - Effect sizes
   - Statistical tests and p-values

7. **Limitations:**
   - Known threats to validity
   - Scope of generalization

### 9.2 Example Results Table

| Metric | Prompt A | Prompt B | Difference | 95% CI | p-value |
|--------|----------|----------|------------|--------|---------|
| Pass Rate | 78% | 65% | +13 pp | [4, 22] | 0.006 |
| Avg. Quality (1-5) | 4.2 | 3.8 | +0.4 | [0.1, 0.7] | 0.012 |
| Latency (ms) | 450 | 420 | +30 | [-10, 70] | 0.14 |
| Cost ($/1K) | $2.40 | $1.80 | +$0.60 | - | - |

*N=200 test cases, paired design, model: claude-3-5-sonnet-20241022, temp=0*

---

## 10. Summary: Key Principles

1. **Define the research question** before choosing a design—comparison, optimization, diagnosis, or threshold?

2. **Use within-subject designs** when comparing prompts on fixed test sets—higher power, smaller samples.

3. **Control confounds ruthlessly**—pin model versions, fix temperature, randomize order, log everything.

4. **Construct test sets dimensionally**—stratify by complexity, domain, and edge cases.

5. **Validate LLM-as-judge** against human labels before trusting—measure TPR/TNR on 100+ examples.

6. **Report effect sizes and confidence intervals**—not just p-values.

7. **Document everything**—exact prompts, model versions, sampling procedures, limitations.

8. **Start with error analysis**—design evaluations for discovered failures, not imagined ones.

9. **Iterate continuously**—re-evaluate after changes, update test sets, watch for drift.

10. **Distinguish statistical from practical significance**—a 2% improvement may not matter; a 20% improvement does.

---

## References

**From Literature Review:**
- Husain (2024) - Error analysis methodology, three-level framework
- Husain (2024) - LLM-as-judge validation with TPR/TNR
- Husain & Shankar (2025) - Dimensional test set construction
- O'Brien (2025) - LLM-judge agreement rates (64-68%)
- Zhao et al. (2025) - Synthetic data generation

**General Experimental Design:**
- Shadish, Cook & Campbell (2002) - Experimental and Quasi-Experimental Designs
- Cohen (1988) - Statistical Power Analysis for the Behavioral Sciences
