# Appendix A, Section 2.3: Econometrics and Causal Inference

## Overview

Econometrics provides statistical methods for estimating causal effects, particularly from observational data where randomized experiments aren't feasible. When we can't randomly assign AI use, how can we still learn about AI's causal effects?

The fundamental problem of causal inference is that we can't observe counterfactuals—we can't see what would have happened to AI users if they hadn't used AI, or what would have happened to non-users if they had. Every causal inference method is a strategy for approximating these unobservable counterfactuals.

For AI evaluation, econometric methods are essential because randomized experiments are often impractical. Organizations adopt AI for business reasons, not randomly. Users choose to use AI based on their needs and capabilities. These selection processes create correlation between AI use and outcomes that may have nothing to do with AI's causal effect.

---

## Core Concepts

### The Fundamental Problem of Causal Inference

Consider estimating AI's effect on productivity. For user i, we want to compare:
- Yi(1) = productivity if user i uses AI
- Yi(0) = productivity if user i doesn't use AI

The causal effect for user i is Yi(1) - Yi(0). But we only observe one of these outcomes—the one corresponding to what actually happened. The other is counterfactual and unobservable.

All causal inference methods are strategies for approximating the missing counterfactual, typically by finding comparison cases that are similar to the treated cases in all relevant respects except the treatment.

### Difference-in-Differences (DiD)

DiD compares changes over time between treatment and control groups:

**Effect = (Treatment After - Treatment Before) - (Control After - Control Before)**

The logic: even if treatment and control groups differ at baseline, if they would have followed parallel trends without treatment, the difference in their changes estimates the causal effect.

For AI, DiD might compare productivity changes in departments that adopted AI versus departments that didn't. The key assumption is parallel trends: absent AI adoption, the groups would have experienced similar productivity changes. This assumption is untestable but can be probed by examining pre-treatment trends.

### Regression Discontinuity (RD)

RD exploits sharp cutoffs in treatment assignment. If AI access is granted based on a score threshold (employees above some performance rating get AI tools), we can compare those just above and just below the cutoff. Since they're similar in all respects except being on different sides of the cutoff, any difference in outcomes is attributable to treatment.

RD provides highly credible causal estimates but only for units near the cutoff—the local average treatment effect (LATE). Effects might differ for units far from the cutoff.

### Instrumental Variables (IV)

IV uses exogenous variation in treatment exposure to isolate causal effects. An "instrument" is a variable that:
1. Affects treatment (strong first stage)
2. Affects outcome only through treatment (exclusion restriction)

If a random subset of users received AI training (the instrument), and training affects AI use (which affects productivity), we can use training as an instrument to estimate AI's causal effect on productivity—even though AI use itself isn't random.

Finding valid instruments is difficult. The exclusion restriction—that the instrument affects outcomes only through treatment—is untestable and often questionable.

### Propensity Score Methods

Propensity scores model the probability of treatment given observed characteristics. Matching treated and control units with similar propensity scores creates groups that are comparable on observed variables.

For AI, propensity score matching might match AI users with non-users who have similar job roles, tenure, prior performance, and other observed characteristics. If matched pairs have similar outcomes, AI doesn't help; if AI users do better, that difference estimates the causal effect.

The critical assumption is selection on observables: conditional on observed characteristics, treatment assignment is as-if random. If unobserved factors also influence selection (motivation, interest in technology), the method fails.

### Synthetic Control

Synthetic control constructs a comparison case by weighting control units to match the treated unit's pre-treatment characteristics. For a single organization adopting AI, synthetic control creates a "synthetic" comparison organization from weighted combinations of non-adopting organizations.

This is useful when there's one treated unit or few treated units, making traditional methods infeasible. The synthetic control should closely match the treated unit's pre-treatment trajectory.

### Heterogeneous Treatment Effects

Average treatment effects may mask important variation. AI might help some users (novices) while not helping others (experts). Subgroup analysis examines effects for different populations.

Modern causal machine learning methods (causal forests, etc.) can discover heterogeneity data-driven, identifying which user characteristics predict larger or smaller effects.

---

## What Transfers to AI Evaluation

**Counterfactual thinking** is essential. What would have happened without AI? Every AI impact claim implies a counterfactual; making that counterfactual explicit improves reasoning.

**Selection bias awareness** is crucial. Who adopts AI is not random. Differences between AI users and non-users may reflect selection, not AI effects. Every observational AI study should grapple with selection.

**DiD and related designs** are directly applicable to AI rollouts. When organizations adopt AI at different times or in different departments, quasi-experimental designs can extract causal evidence.

**Heterogeneity analysis** is essential for AI. Average effects may mislead when effects vary dramatically across users. Understanding for whom AI works is as important as whether it works on average.

---

## What Breaks for Generative AI

**Stable unit treatment value assumption (SUTVA)** requires that one unit's treatment doesn't affect another unit's outcomes. AI use by one person may affect others—through shared documents, changed workflows, or competitive dynamics. Interference between units complicates causal interpretation.

**Treatment definition** is problematic. What does "using AI" mean? Once for a quick answer? Continuously throughout work? With expert prompting or novice prompting? The treatment is heterogeneous and hard to define.

**Long pre-treatment periods** are needed for DiD and synthetic control to establish pre-treatment trends. AI is too new for long pre-periods; technology changes during the study window.

**Exclusion restrictions** are hard to satisfy. Finding instruments that affect AI use but affect outcomes only through AI use is difficult.

---

## What Can Be Adapted

**Staggered adoption designs** exploit that different units adopt AI at different times. Modern DiD methods handle staggered adoption while accounting for heterogeneous effects.

**Event study designs** examine outcomes relative to adoption date, revealing dynamics of AI effects—immediate impacts, learning curves, long-term effects.

**Causal forests** can discover heterogeneity in AI effects, identifying user or task characteristics that predict larger or smaller benefits.

**Sensitivity analysis** for unobserved confounding quantifies how much hidden bias would be needed to explain away results. This helps assess robustness of causal claims.

---

## Implications for AI Evaluation

**When RCTs aren't feasible, quasi-experimental methods can provide evidence.** DiD, RD, IV, and synthetic control all offer strategies for causal inference from observational data.

**Selection into AI use is a major concern.** Any observational AI study must address why some users adopt and others don't. What confounders might explain apparent effects?

**Look for natural experiments.** Situations where AI access varies for reasons unrelated to productivity—randomization by management, staggered rollouts, technical constraints—provide the best quasi-experimental opportunities.

**Analyze heterogeneity.** Don't stop at average effects. Who benefits most? Who doesn't benefit? Under what conditions? Heterogeneity analysis provides actionable insights.

**Be explicit about assumptions.** Every causal inference method requires assumptions (parallel trends, exclusion restrictions, selection on observables). State the assumptions. Assess their plausibility. Conduct sensitivity analysis.

---

## Key References

- **Angrist, J.D., & Pischke, J.S. (2009). *Mostly Harmless Econometrics*.** Accessible introduction to causal inference methods.

- **Cunningham, S. (2021). *Causal Inference: The Mixtape*.** Modern treatment with clear explanations and code.

- **Huntington-Klein, N. (2021). *The Effect: An Introduction to Research Design and Causality*.** Excellent introduction emphasizing intuition.

- **Athey, S., & Imbens, G.W. (2017). "The State of Applied Econometrics: Causality and Policy Evaluation." *Journal of Economic Perspectives*.** Overview from leading causal inference researchers.

- **Wager, S., & Athey, S. (2018). "Estimation and Inference of Heterogeneous Treatment Effects Using Random Forests." *Journal of the American Statistical Association*.** Causal forests methodology.

- **Abadie, A., Diamond, A., & Hainmueller, J. (2010). "Synthetic Control Methods for Comparative Case Studies." *Journal of the American Statistical Association*.** Synthetic control methodology.

---

## Connections to Other Sections

Econometrics connects to several other disciplines covered in this appendix:

- **Section 2.1 (Experimental Design)** provides the foundation; econometrics extends causal inference to non-experimental settings.

- **Section 3.1-3.2 (Economics)** applies econometric methods to IT and productivity measurement questions directly relevant to AI.

- **Section 5.3 (Organizational Behavior)** highlights implementation and adoption factors that create selection bias in AI studies.

- **Section 6.2 (Program Evaluation)** shares concern for causal inference about interventions, with complementary frameworks.

- **Section 2.5 (Survey Methodology)** addresses data collection methods often used in econometric analyses.

---

*[End of Section 2.3]*
