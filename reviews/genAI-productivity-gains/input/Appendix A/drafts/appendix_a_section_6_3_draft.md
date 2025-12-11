# Appendix A, Section 6.3: Educational Measurement

## Overview

Educational measurement assesses learning and achievement. While focused on students rather than AI, the field offers insights relevant to AI evaluation—particularly around high-stakes testing, test security, and the effects of testing on what gets taught and learned.

Educational measurement has decades of experience with testing problems that are highly relevant to AI: how tests change behavior, how test security matters, and how high stakes corrupt measurement.

---

## Core Concepts

### High-Stakes Testing

When test results have significant consequences:
- Student graduation, placement, or advancement
- Teacher evaluation and accountability
- School ratings and resources

High stakes change behavior. People optimize for what's measured, sometimes at the expense of what matters.

**Campbell's Law**: "The more any quantitative social indicator is used for social decision-making, the more subject it will be to corruption pressures and the more apt it will be to distort and corrupt the social processes it is intended to monitor."

For AI, benchmark results are increasingly high-stakes:
- Model reputation and marketing
- Investment decisions
- Regulatory scrutiny
- Deployment decisions

This creates pressure to optimize benchmarks specifically, potentially at the expense of general capability.

### Test Security

Maintaining valid test results requires keeping test content secure:

**Preventing item leakage**: Test questions shouldn't be available before the test.

**Detecting cheating**: Identifying when test-takers have prior access to items.

**Protecting items**: Keeping items secure for future use.

**Item banking**: Managing pools of items that can be drawn from.

For AI, benchmark security parallels test security:
- If AI is trained on benchmark items (the AI equivalent of "leaking" the test), scores are inflated
- Benchmark contamination through internet-scale training data is a novel security challenge
- Detecting contamination is difficult but essential
- Protecting benchmark items may require keeping them private

### Teaching to the Test

When tests have consequences, instruction shifts toward what's tested:

**Beneficial alignment**: Teaching what tests measure, when tests measure what matters. If tests measure important skills, teaching to the test is good.

**Harmful narrowing**: Teaching only what's tested, neglecting other important content. Curriculum shrinks to test content.

**Score inflation**: Scores rise without underlying improvement. Getting better at the test without getting better at what it's supposed to measure.

For AI, "training to the benchmark" is analogous:
- AI may be optimized for benchmark performance in ways that don't generalize
- Benchmark scores may improve without genuine capability improvement
- The gap between benchmark performance and real-world performance may grow

### Score Inflation and Construct Validity

When scores rise faster than the underlying construct:

**Score inflation**: Test scores improve but actual capability doesn't proportionally improve. The relationship between score and capability degrades.

**Construct underrepresentation**: Test measures only part of the construct. Scores improve on measured aspects while unmeasured aspects stagnate.

**Teaching to the rubric**: Meeting the letter of criteria without meeting the spirit.

For AI, score inflation concerns are acute:
- Benchmark optimization may inflate scores
- Models may get better at benchmarks without proportional improvement in real capability
- The benchmark-to-real gap may grow over time

### Standard Setting

Determining cut scores (pass/fail thresholds) requires judgment:

**What level of performance is "proficient"?** Not a purely empirical question.

**Methods** (Angoff, bookmark, contrasting groups) structure expert judgment but don't eliminate it.

**Cut scores are not purely empirical**: They involve values about acceptable risk and minimum competence.

**Consequences matter**: Where you set the cut determines false positives and false negatives.

For AI, standard setting applies:
- At what benchmark score is AI "good enough" for a task?
- What performance level is sufficient for deployment?
- These decisions require judgment about acceptable risk
- Cut scores for AI should be set with purpose and consequences in mind

### Measurement Invariance

Does the test measure the same thing across groups?

**Differential Item Functioning (DIF)**: Items function differently for different groups beyond true ability differences.

**Measurement equivalence**: Same scores should mean the same thing across contexts.

For AI, measurement invariance asks:
- Does benchmark performance mean the same thing across different AI systems?
- Do benchmarks function the same way for different model architectures?

---

## What Transfers to AI Evaluation

**Test security**: Benchmark contamination is the AI equivalent of test leakage. Security matters.

**Campbell's Law**: Metrics become targets and lose validity when stakes are high.

**Teaching to the test**: AI may be optimized for benchmarks specifically. Don't assume benchmark improvement means capability improvement.

**Standard setting**: Determining capability thresholds requires judgment. Be explicit about how thresholds are set.

**Score inflation**: Monitor for the gap between scores and actual capability growing over time.

---

## What Breaks for Generative AI

**Test administration**: Traditional tests have controlled administration. AI "test-taking" is less controlled.

**Security mechanisms**: Traditional security (proctoring, item release schedules) don't work for AI trained on internet data.

**Clear constructs**: Educational constructs (reading comprehension, math ability) are clearer than AI capability constructs.

**Defined curricula**: Educational testing assumes defined content. AI capability isn't bounded by curriculum.

---

## What Can Be Adapted

**Item-level analysis**: Examining performance at item level to detect anomalies and contamination.

**Adaptive testing**: Selecting items based on prior performance to improve efficiency and security.

**Construct validity studies**: Empirically examining what benchmarks actually measure.

**Standard setting panels**: Using expert judgment to establish meaningful thresholds.

---

## Implications for AI Evaluation

**Treat benchmark security seriously.** Contamination inflates scores and degrades validity.

**Expect optimization for evaluation** as benchmark stakes increase. Campbell's Law applies.

**Use multiple, varied measures** to resist gaming. Don't rely on single benchmarks.

**Apply standard setting thinking** to determine capability thresholds. Be explicit about how "good enough" is defined.

**Monitor for score inflation.** Track whether benchmark improvement corresponds to real capability improvement.

---

## Key References

- **Koretz, D. (2008). *Measuring Up: What Educational Testing Really Tells Us*.** Accessible treatment of testing limitations and gaming.

- **Cizek, G.J., & Wollack, J.A. (Eds.). (2016). *Handbook of Quantitative Methods for Detecting Cheating on Tests*.** Detection methodology.

- **Haladyna, T.M., & Rodriguez, M.C. (2013). *Developing and Validating Test Items*.** Item development methodology.

- **Shepard, L.A. (1997). "The Centrality of Test Use and Consequences for Test Validity." *Educational Measurement: Issues and Practice*.** Consequences and validity.

- **Linn, R.L. (2000). "Assessments and Accountability." *Educational Researcher*.** High-stakes testing effects.

---

## Connections to Other Sections

Educational measurement connects to several other disciplines covered in this appendix:

- **Section 2.2 (Psychometrics)** provides the measurement theory foundation.

- **Section 6.1 (AI Safety Evaluation)** addresses benchmark contamination from AI perspective.

- **Section 1.4 (Traditional ML)** addresses benchmark methodology for machine learning.

- **Section 5.5 (I-O Psychology)** addresses selection testing with related concepts.

- **Section 4.4 (Audit)** shares concern for integrity of assessment processes.

---

*[End of Section 6.3]*
