# Appendix A, Section 2.2: Psychometrics and Measurement Theory

## Overview

Psychometrics is the science of psychological measurement—the discipline that asks what it means to measure something that cannot be directly observed. When we measure height, we can put a ruler against a person. When we measure intelligence, capability, or attitude, we must infer unobservable constructs from observable behaviors.

For AI evaluation, psychometrics matters because AI "capability" is itself an unobservable construct. We don't directly observe capability; we observe performance on specific tasks and infer capability from those observations. The relationship between observable performance and underlying capability is precisely what psychometrics theorizes.

Psychometrics has developed sophisticated frameworks for understanding reliability (consistency of measurement), validity (whether we're measuring what we intend), and the relationship between test items and latent traits. These frameworks offer deep insights for AI evaluation, though their assumptions often don't hold cleanly for AI systems.

---

## Core Concepts

### Reliability

Reliability refers to the consistency or repeatability of measurement. An unreliable measure gives different results on different occasions even when the underlying thing being measured hasn't changed.

**Test-retest reliability** asks whether the same measure gives consistent results over time. If we evaluate AI on a benchmark today and again next week, do we get the same score? For AI, test-retest reliability is complicated by both stochastic outputs and potential model updates.

**Inter-rater reliability** asks whether different judges agree. When humans evaluate AI outputs, do different evaluators rate the same output similarly? Low inter-rater reliability suggests the evaluation criteria are unclear or subjective.

**Internal consistency** asks whether different items measuring the same construct agree. If a benchmark has 100 questions intended to measure "reasoning ability," do performance levels correlate across questions? High internal consistency suggests the questions measure a coherent construct.

**Standard error of measurement** quantifies how much scores would vary due to measurement error alone. An AI that scores 85% on a benchmark might have a true score anywhere from 82% to 88% given measurement uncertainty.

### Validity (Expanded)

Validity asks whether we're measuring what we intend to measure. Psychometrics has developed nuanced validity concepts:

**Content validity** asks whether the test adequately samples the domain it claims to measure. A "general reasoning" benchmark that only includes math problems has poor content validity—it doesn't cover the full domain of reasoning. Most AI benchmarks have uncertain content validity: How well does HumanEval sample real programming tasks? How well does MMLU sample human knowledge?

**Criterion validity** asks whether the test predicts relevant outcomes:
- **Concurrent validity**: Does the test correlate with current criterion measures? Does benchmark performance correlate with current expert ratings of capability?
- **Predictive validity**: Does the test predict future outcomes? Does benchmark performance predict real-world deployment success?

Predictive validity is the key question for AI evaluation: do benchmark scores predict operational value? This is largely unknown for most AI benchmarks.

**Construct validity** asks whether the test measures the theoretical construct it claims to measure:
- **Convergent validity**: Does the test correlate with other measures of the same construct? Do different reasoning benchmarks agree?
- **Discriminant validity**: Does the test not correlate with measures of different constructs? If a "reasoning" test correlates perfectly with a "memorization" test, maybe it's measuring memorization.

Construct validity for AI benchmarks is poorly understood. When an AI scores well on a "reasoning" benchmark, is it reasoning or pattern-matching or something else entirely?

### Classical Test Theory (CTT)

Classical test theory models observed scores as the sum of true scores plus error:

**Observed Score = True Score + Error**

The true score represents the person's actual level on the construct; error represents random measurement variability. Reliability is defined as the ratio of true score variance to observed score variance—how much of the variability in observed scores reflects genuine differences versus measurement noise.

For AI, CTT provides a framework for understanding benchmark variability. Some variability in AI performance reflects genuine capability differences (between models); some reflects measurement noise (stochastic outputs, sample of test items).

### Item Response Theory (IRT)

Item Response Theory provides a more sophisticated framework that models the probability of correct response as a function of both person ability and item characteristics:

- **Item difficulty**: Some items are harder than others
- **Item discrimination**: Some items better distinguish high-ability from low-ability
- **Guessing**: For multiple-choice, even zero-ability has some probability of guessing correctly

IRT allows items to be on a common scale, enables adaptive testing (selecting items based on previous responses), and provides more nuanced information about ability levels.

For AI benchmarks, IRT thinking suggests that not all benchmark items are equally informative. Some items might distinguish between capable and less-capable models (high discrimination); others might not. Benchmark design could be optimized by selecting items with high discrimination at relevant ability levels.

### Generalizability Theory (G-Theory)

Generalizability theory extends classical reliability to account for multiple sources of measurement error simultaneously. Variance in observed scores might come from:

- Person/model differences (what we want to measure)
- Item differences (some questions harder than others)
- Rater differences (human judges disagree)
- Occasion differences (stochastic variation)
- Interactions among these factors

G-theory partitions variance into components, revealing which sources of error are largest. For AI evaluation with human raters, G-theory might reveal that rater disagreement contributes more measurement error than item sampling.

### Standard Setting

Standard setting determines cut scores—thresholds for categorizing performance (pass/fail, proficient/not proficient). These decisions are fundamentally judgmental, not purely statistical. Methods like the Angoff method have experts estimate what minimally competent performance looks like.

For AI, standard setting questions arise constantly: At what benchmark score should we consider an AI "capable" of a task? What performance level is sufficient for deployment? These thresholds require judgment that combines measurement with values about acceptable risk.

---

## What Transfers to AI Evaluation

**Reliability concepts** directly apply. AI evaluations have measurement error from multiple sources—stochastic outputs, item sampling, human raters. Quantifying and reporting reliability (through multiple samples, inter-rater agreement, confidence intervals) is essential.

**The validity framework** is foundational. Every AI benchmark should be examined for:
- Content validity: Does it adequately sample the domain?
- Criterion validity: Does it predict real-world performance?
- Construct validity: Does it measure what it claims?

Most AI benchmarks have unknown validity in these senses.

**Criterion validity** is the key question: Do benchmarks predict operational value? Pursuing criterion validation studies—correlating benchmark performance with deployment outcomes—would dramatically improve evaluation quality.

**Multiple sources of error** should be recognized and measured. When AI evaluation involves human judgment (rating outputs, detecting errors), inter-rater reliability should be assessed and reported.

---

## What Breaks for Generative AI

**Stable trait assumption** underlies psychometrics. Tests measure relatively stable individual differences. But AI "capabilities" aren't stable—they change with model updates, prompting strategies, and fine-tuning. The entire framework assumes something stable to measure.

**Population and norming** make sense for human testing. A score of 85 means performance at the 85th percentile of some reference population. For AI, there's no natural reference population. What population should AI benchmark scores be normed against?

**Test security** assumes examinees haven't seen the test items before. For AI, training data may include benchmark items—benchmark contamination is the AI equivalent of test leakage. Psychometric methods assume this doesn't happen.

**Individual differences framing** focuses on variation between persons. AI evaluation often focuses on a single "entity" (a model), with variance being across runs or items rather than across individuals. The conceptual mapping is awkward.

---

## What Can Be Adapted

**IRT for benchmark design** could optimize which items to include. Items with high discrimination at relevant ability levels provide more information than items everyone gets right or everyone gets wrong.

**G-theory for evaluation design** can identify dominant sources of error. If rater disagreement dominates, invest in clearer rubrics and rater training. If item sampling dominates, use larger item sets.

**Reliability estimation methods** can be applied—computing agreement across raters, consistency across items, stability across runs. The specific techniques need adaptation but the underlying logic holds.

**Standard setting methods** could be adapted for determining AI capability thresholds, involving experts in judging what performance levels are adequate for specific uses.

---

## Implications for AI Evaluation

**Apply the validity framework rigorously.** For any AI benchmark, ask: What's the evidence for content validity? Criterion validity? Construct validity? Most benchmarks lack such evidence.

**Quantify and report reliability.** Report inter-rater agreement when humans evaluate. Report consistency across multiple runs. Report confidence intervals, not just point estimates.

**Recognize that criterion validity is the key question.** Content validity and face validity are necessary but not sufficient. What matters is whether benchmark performance predicts real-world value. Pursue criterion validation studies.

**Use IRT thinking in benchmark design.** Not all items are equally informative. Optimize benchmarks by selecting discriminating items at relevant ability levels.

**Be aware that many psychometric assumptions don't hold.** AI capabilities aren't stable traits. There's no natural reference population. Training may include test items. Apply psychometric insights while recognizing their limits.

---

## Key References

- **Cronbach, L.J., & Meehl, P.E. (1955). "Construct Validity in Psychological Tests." *Psychological Bulletin*.** Foundational paper on construct validity.

- **Messick, S. (1989). "Validity." In *Educational Measurement* (3rd ed.).** Comprehensive treatment of unified validity concept.

- **Kane, M.T. (2013). "Validating the Interpretations and Uses of Test Scores." *Journal of Educational Measurement*.** Argument-based validity framework.

- **Brennan, R.L. (2001). *Generalizability Theory*.** Definitive treatment of G-theory.

- **Embretson, S.E., & Reise, S.P. (2000). *Item Response Theory for Psychologists*.** Accessible introduction to IRT.

- **AERA, APA, & NCME. (2014). *Standards for Educational and Psychological Testing*.** Authoritative standards for measurement.

---

## Connections to Other Sections

Psychometrics connects to several other disciplines covered in this appendix:

- **Section 2.1 (Experimental Design)** shares concern for validity, though experimental validity focuses on causal inferences while psychometric validity focuses on measurement.

- **Section 5.5 (I-O Psychology)** applies psychometric principles to personnel selection and performance appraisal—frameworks directly applicable to "evaluating AI like hiring."

- **Section 6.3 (Educational Measurement)** extends psychometric concepts to high-stakes testing with concerns about test security and teaching to the test.

- **Section 7.1 (Metrology)** provides complementary perspective on measurement uncertainty and traceability from physical measurement sciences.

- **Section 2.5 (Survey Methodology)** applies measurement principles to self-report data collection.

- **Section 1.4 (Traditional ML Evaluation)** applies measurement concepts to model evaluation metrics.

---

*[End of Section 2.2]*
