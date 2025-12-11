# Appendix A, Section 8.6: Synthesis—What AI Evaluation Requires

## Overview

Drawing across all disciplines covered in this appendix, this section synthesizes what comprehensive AI evaluation requires. This represents the accumulated wisdom of multiple fields applied to the AI evaluation challenge.

---

## From Testing Traditions

Effective AI evaluation requires:

**Systematic approach**: Planned, comprehensive evaluation rather than ad hoc probing. Know what you're testing and why. Have coverage strategies.

**V&V distinction**: Separate technical verification (does AI meet specifications?) from fitness-for-purpose validation (does AI serve users' needs?). Both matter; neither is sufficient.

**DT/OT paradigm**: Lab evaluation precedes and differs from operational evaluation. Benchmarks are necessary but not sufficient. Operational testing with real users in real contexts is essential.

**Adversarial orientation**: Actively try to find failures, not just confirm successes. Red teaming, edge case exploration, boundary probing.

**Scenario-based coverage**: Systematic scenario coverage since input space is unbounded. Design scenarios to explore capability systematically.

---

## From Statistical Methods

Effective AI evaluation requires:

**Validity framework**: Rigorous attention to internal, external, and construct validity. Are conclusions warranted? Do they generalize? Are we measuring what we intend?

**Appropriate comparison**: Clear baseline/control conditions. "AI improves performance" is meaningless without specifying compared to what.

**Causal discipline**: Distinguish correlation from causation. Selection effects, confounding, and reverse causation threaten causal claims.

**Heterogeneity awareness**: Average effects may mask important variation. Examine who benefits and who doesn't.

**Qualitative complement**: Numbers need qualitative understanding of how and why. Mixed methods are stronger than either alone.

---

## From Economics

Effective AI evaluation requires:

**Productivity paradox awareness**: Don't expect immediate measured gains. IT history suggests significant lags before benefits materialize.

**Complementary investments**: AI benefits require organizational change. Training, process redesign, and workflow restructuring accompany AI deployment.

**Full cost accounting**: Include hidden and indirect costs. TCO exceeds visible costs.

**Time horizons**: Short-run may differ from long-run. Learning curves, adaptation, and maturation affect results.

---

## From Risk and Quality

Effective AI evaluation requires:

**Risk-based prioritization**: Focus resources on highest-risk applications. Not all AI uses warrant the same scrutiny.

**Continuous monitoring**: Don't rely solely on pre-deployment evaluation. Ongoing monitoring catches problems that emerge over time.

**Residual risk acceptance**: Evaluation reduces but doesn't eliminate risk. Acknowledge what remains.

**Independence**: Separate evaluator from developer for high stakes. Self-evaluation lacks credibility.

---

## From Human and Organizational Factors

Effective AI evaluation requires:

**Human-AI team evaluation**: Assess the team, not just the AI. AI capability alone doesn't determine outcomes.

**Trust calibration**: Evaluate whether users trust appropriately. Neither over-trust nor under-trust is desirable.

**Organizational context**: Evaluation results depend on organizational factors. Context shapes outcomes.

**Implementation fidelity**: Check whether AI is actually being used. And how. Failed adoption explains many null findings.

---

## From Evaluation Traditions

Effective AI evaluation requires:

**Logic models**: Make explicit how AI is supposed to create value. What's the theory of change?

**Developmental approach**: Appropriate when learning what works. AI is still new; we're still learning.

**Post-deployment surveillance**: Continue evaluation after deployment. Problems emerge over time.

---

## Novel Requirements for AI

Beyond established disciplines, AI requires:

**Benchmark integrity**: Protect against contamination. Benchmark security is essential for valid scores.

**Capability coverage**: Dense coverage of the jagged frontier. The boundary is fractal and unpredictable.

**Output evaluation**: Methods for unbounded, open-ended outputs. New frameworks needed.

**Evolution accommodation**: Evaluation design that handles system change. AI changes continuously.

**Skill interaction**: Understanding how user skill affects outcomes. AI effectiveness depends on use.

**Quality articulation**: Methods for the "vibes" problem. Making implicit quality criteria explicit.

---

## Consolidated Checklist

Before evaluating AI, consider:

### Planning
- [ ] What should AI do? (job analysis)
- [ ] How is AI supposed to create value? (logic model)
- [ ] What could go wrong? (threat modeling)
- [ ] Where should evaluation focus? (risk-based prioritization)
- [ ] What's the comparison? (control condition)

### Execution
- [ ] Is evaluation structured? (reduce bias and noise)
- [ ] Is adversarial testing included? (red teaming)
- [ ] Are scenarios realistic? (operational realism)
- [ ] Is AI actually being used? (implementation fidelity)
- [ ] Is the human-AI team evaluated? (not just AI capability)
- [ ] Is trust calibration assessed? (appropriate reliance)
- [ ] Are qualitative methods included? (understand how and why)

### Interpretation
- [ ] Is uncertainty quantified? (confidence intervals)
- [ ] Is heterogeneity analyzed? (who benefits?)
- [ ] Are selection effects considered? (who participates is not random)
- [ ] Is residual risk acknowledged? (evaluation doesn't guarantee safety)
- [ ] Is post-deployment monitoring planned? (evaluation continues)

### Cross-Cutting
- [ ] Is evaluation independent? (separate from developer)
- [ ] Is evolution expected? (AI changes)
- [ ] Is the benchmark-to-real gap acknowledged? (criterion validity)

---

## What This Requires Organizationally

Effective AI evaluation requires organizational capabilities:

**Expertise**: Knowledge of evaluation methods, AI technology, and domain context.

**Independence**: Ability to evaluate without bias from development or procurement interests.

**Resources**: Time, personnel, and budget for thorough evaluation.

**Infrastructure**: Tools and systems for continuous monitoring.

**Culture**: Willingness to surface problems and act on findings.

**Leadership support**: Organizational commitment to evidence-based AI decisions.

---

*[End of Section 8.6]*
