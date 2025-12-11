# Appendix A, Section 2: Experimental and Statistical Methods

## Section 2.1: Experimental Design and Analysis

### Overview

Experimental design is the science of structuring studies to support valid causal inferences. When we want to know whether an intervention causes an effect—not just whether it correlates with an outcome—we need experimental methods that isolate the causal relationship from confounding factors.

For AI evaluation, this matters profoundly. The central question "Does AI improve productivity?" is a causal question. Observing that AI users perform better than non-users doesn't establish that AI caused the improvement—users who adopt AI may differ systematically from those who don't. Rigorous experimental design provides frameworks for moving from correlation to causation.

This section surveys the core concepts of experimental design, examines their applicability to AI evaluation, identifies where the assumptions of experimental methodology become strained, and draws implications for evaluation practice.

### Core Concepts

**Randomized Controlled Trials (RCTs)**

The randomized controlled trial is the gold standard for causal inference. Its logic is elegant: randomly assign units (people, teams, organizations) to treatment and control conditions. Because assignment is random, the groups should be comparable on all characteristics—both observed and unobserved—except for the treatment itself. Any systematic difference in outcomes can therefore be attributed to the treatment.

RCTs for AI might randomly assign some workers to use AI tools while others use traditional methods, then compare productivity outcomes. Random assignment ensures that differences in outcomes reflect AI's causal effect, not pre-existing differences between users who would choose to adopt AI versus those who wouldn't.

The power of randomization comes from what it eliminates: selection bias (users choosing AI are different), confounding (some third factor causing both AI adoption and productivity), and reverse causation (productive people adopting AI rather than AI making people productive). Without randomization, all these alternatives remain plausible.

**Validity Types**

Experimental methodology distinguishes several types of validity:

**Internal validity** asks: Can we attribute observed effects to the treatment? Did the intervention actually cause the outcome? Threats to internal validity include selection bias, confounding, measurement error, and experimental artifacts. High internal validity means we can be confident the treatment caused the effect.

**External validity** asks: Do findings generalize beyond the study? Results from one setting, population, or time may not transfer to others. A study of programmers using Copilot may not generalize to analysts using ChatGPT, or to the same programmers six months later when both tools and skills have evolved.

**Construct validity** asks: Are we measuring what we intend to measure? If we measure "productivity" by lines of code, do lines of code actually capture productivity? If we measure AI's effect on a specific benchmark, does that construct represent real-world capability?

**Statistical conclusion validity** asks: Are our statistical inferences appropriate? With sufficient data? Using appropriate methods? Accounting for multiple comparisons? A study might be well-designed but underpowered to detect real effects, or might claim significance that doesn't survive appropriate corrections.

These validity types often trade off. Tightly controlled laboratory experiments may have high internal validity but low external validity. Field studies may have higher external validity but struggle with internal validity because conditions can't be fully controlled.

**Control and Comparison Conditions**

Every experiment requires comparison—but comparison to what? The choice of control condition profoundly affects interpretation:

**No-treatment control** compares treatment to nothing. Workers using AI versus workers using no tools. This shows whether AI helps relative to nothing, but doesn't reveal whether AI helps relative to alternatives.

**Active control** compares treatment to an alternative intervention. Workers using AI versus workers using traditional search engines and documentation. This shows AI's marginal value above existing tools.

**Placebo control** attempts to control for expectation effects. In medicine, sugar pills; for AI, perhaps a non-functional AI interface that gives users the belief they're using AI. This is often impractical for AI studies but highlights the question: how much of AI's apparent benefit comes from users believing they have a powerful tool?

**Within-subjects design** exposes the same people to both conditions (with and without AI), controlling for individual differences. But this creates order effects and learning confounds.

**Between-subjects design** assigns different people to different conditions, avoiding carryover effects but requiring larger samples to account for individual variation.

For AI evaluation, comparison condition choice is crucial. Comparing AI to nothing overstates AI's value; comparing to best alternatives understates it. The appropriate comparison depends on the decision being informed.

**Confounding and Bias**

Even well-designed experiments can suffer from biases:

**Selection bias** occurs when treatment and control groups differ systematically. In AI studies, if AI adoption is voluntary, users who choose to adopt may differ in motivation, technical skill, or task characteristics.

**Attrition bias** occurs when participants drop out differentially. If frustrated AI users abandon the study while frustrated control participants persist, remaining AI users appear more successful than they actually are.

**Experimenter effects** occur when experimenters' expectations influence outcomes. An evaluator who believes AI is helpful may unconsciously score AI-assisted work more favorably.

**Demand characteristics** occur when participants guess the study's hypothesis and behave accordingly. Workers who know they're in an "AI productivity study" may try harder when using AI.

**Hawthorne effects** occur when being observed changes behavior. Workers being studied may work differently regardless of experimental condition.

**Statistical Power and Sample Size**

Power analysis determines how many observations are needed to detect effects of a given size with acceptable confidence. Underpowered studies may fail to detect real effects (Type II error), while studies with many comparisons may find spurious effects (Type I error).

Effect sizes in AI studies vary widely. A study powered to detect a 50% productivity improvement will miss a 10% improvement—which may still be practically significant. Sample size planning requires prior estimates of expected effect size and acceptable error rates.

Multiple comparisons compound the problem. If you test AI effects on ten different outcome measures, you expect one significant result by chance at p < 0.10 even if AI has no effect. Pre-registration of hypotheses and appropriate statistical corrections help address this.

**Replication and Reproducibility**

The replication crisis in psychology and other fields highlighted that many published findings don't reproduce. Causes include low statistical power, flexible analysis methods ("p-hacking"), publication bias favoring positive results, and genuine context-dependence.

Pre-registration addresses some concerns: committing to hypotheses and analysis plans before seeing data constrains researcher degrees of freedom. Registered reports go further, accepting papers for publication based on methods before results are known.

For AI evaluation, replication faces additional challenges: models change, tools update, and user skills evolve. An experiment with GPT-3.5 may not replicate with GPT-4. This isn't a flaw in the original study—it reflects genuinely changing technology.

### What Transfers to AI Evaluation

Several elements of experimental methodology transfer directly:

**The validity framework** provides essential vocabulary for assessing AI evaluation quality. Every AI study can be examined for internal validity (is the causal claim supported?), external validity (do findings generalize?), and construct validity (do measurements capture what matters?). This framework structures critical assessment.

**Control condition thinking** is essential. AI claims are meaningful only relative to comparison. What would have happened without AI? What would happen with alternative tools? Making comparison conditions explicit forces clearer thinking about AI's contribution.

**Bias awareness** helps identify threats to evaluation credibility. Who chose to use AI? Who dropped out? How were outcomes measured? Systematic consideration of potential biases improves evaluation design and interpretation.

**Power analysis** should inform evaluation planning. How large an effect should this study be able to detect? Is the sample size adequate? Acknowledging power limitations helps calibrate confidence in results.

**Pre-registration** reduces researcher degrees of freedom. Committing to analysis plans before seeing data constrains the flexibility that enables spurious findings.

### What Breaks for Generative AI

Several assumptions of experimental methodology become strained for AI evaluation:

**Treatment stability** is assumed throughout experimental methodology—the treatment is the same for all participants and doesn't change during the study. AI systems change continuously. A three-month experiment may span multiple model updates. The "treatment" a participant receives in month three may differ from month one.

**Blinding** is often impossible. In medical trials, patients can be blinded to whether they receive drug or placebo. In AI studies, users typically know whether they're using AI. This creates potential for expectation effects—users may perform better with AI partly because they expect AI to help.

**Standardized treatment** is assumed—everyone receives the same intervention. But AI use is highly variable. One user may prompt expertly; another may prompt poorly. The "treatment" depends on how users interact with the AI. This is like studying a drug where dosage varies based on how patients feel about it.

**Stable outcomes** are assumed—the outcome measure means the same thing across conditions. But AI may change what work means. If AI-assisted writing produces different kinds of documents than unassisted writing, comparing "productivity" may be comparing apples and oranges.

**Ecological validity** is challenged. Laboratory experiments with defined tasks may not capture real-world AI use, which is embedded in complex workflows with interruptions, iteration, and judgment. But field experiments sacrifice control for realism.

**Effect size stability** is assumed for meta-analysis—the underlying effect doesn't change across studies. AI effect sizes likely do change as technology improves and users learn. Meta-analytic combination of AI studies is problematic when the "treatment" differs fundamentally across studies.

### What Can Be Adapted

**Quasi-experimental designs** don't require randomization but still support causal inference under certain assumptions. When randomized experiments aren't feasible, quasi-experiments offer alternatives (see Section 2.3 on econometrics).

**Mixed methods** combine quantitative experiments with qualitative investigation. Experiments establish whether AI has effects; qualitative methods help understand how and why. For AI, understanding the mechanism—how users interact with AI, what prompting strategies work—is as important as measuring effects.

**Adaptive designs** modify study protocols based on interim results. If early results suggest AI helps some users but not others, the study can shift focus. This flexibility is valuable for rapidly evolving technology.

**N-of-1 trials** study single individuals over time, alternating between conditions. For AI use that's highly personalized, individual-level experiments may be more informative than between-group comparisons.

### Implications for AI Evaluation

**Apply the validity framework.** For any AI evaluation, ask: What's the evidence for internal validity? How far do findings generalize? Do measurements capture what matters? This framework structures critical assessment.

**Make comparison conditions explicit.** Relative to what? No tools? Current tools? Previous AI versions? Human experts? The choice of comparison determines what claims can be supported.

**Design with bias awareness.** Consider selection, attrition, experimenter, and demand biases. Build in safeguards: random assignment where possible, blinded assessment where feasible, measurement of potential confounders.

**Plan for adequate power.** Don't run underpowered studies. Estimate expected effect sizes, calculate required sample sizes, and acknowledge power limitations.

**Consider pre-registration.** For important evaluations, commit to hypotheses and analysis plans before seeing data. This won't solve all problems but reduces researcher flexibility that enables spurious findings.

**Accept trade-offs.** Internal validity often trades off against external validity. Laboratory control sacrifices ecological validity. Choose designs appropriate to the questions and decisions at stake.

**Don't expect stability.** AI changes. Users learn. Effects may not replicate six months later—not because the original study was wrong, but because the world changed. Build this expectation into interpretation.

### Key References

- **Shadish, W.R., Cook, T.D., & Campbell, D.T. (2002). *Experimental and Quasi-Experimental Designs for Generalized Causal Inference*.** The definitive treatment of experimental validity and design.

- **Gerber, A.S., & Green, D.P. (2012). *Field Experiments: Design, Analysis, and Interpretation*.** Comprehensive guide to experiments in field settings.

- **Simmons, J.P., Nelson, L.D., & Simonsohn, U. (2011). "False-Positive Psychology." *Psychological Science*.** Influential paper on researcher degrees of freedom and the need for pre-registration.

- **Open Science Collaboration. (2015). "Estimating the Reproducibility of Psychological Science." *Science*.** Landmark replication study with lessons for all empirical fields.

---

## Section 2.2: Psychometrics and Measurement Theory

### Overview

Psychometrics is the science of psychological measurement—the discipline that asks what it means to measure something that cannot be directly observed. When we measure height, we can put a ruler against a person. When we measure intelligence, capability, or attitude, we must infer unobservable constructs from observable behaviors.

For AI evaluation, psychometrics matters because AI "capability" is itself an unobservable construct. We don't directly observe capability; we observe performance on specific tasks and infer capability from those observations. The relationship between observable performance and underlying capability is precisely what psychometrics theorizes.

Psychometrics has developed sophisticated frameworks for understanding reliability (consistency of measurement), validity (whether we're measuring what we intend), and the relationship between test items and latent traits. These frameworks offer deep insights for AI evaluation, though their assumptions often don't hold cleanly for AI systems.

### Core Concepts

**Reliability**

Reliability refers to the consistency or repeatability of measurement. An unreliable measure gives different results on different occasions even when the underlying thing being measured hasn't changed.

**Test-retest reliability** asks whether the same measure gives consistent results over time. If we evaluate AI on a benchmark today and again next week, do we get the same score? For AI, test-retest reliability is complicated by both stochastic outputs and potential model updates.

**Inter-rater reliability** asks whether different judges agree. When humans evaluate AI outputs, do different evaluators rate the same output similarly? Low inter-rater reliability suggests the evaluation criteria are unclear or subjective.

**Internal consistency** asks whether different items measuring the same construct agree. If a benchmark has 100 questions intended to measure "reasoning ability," do performance levels correlate across questions? High internal consistency suggests the questions measure a coherent construct.

**Standard error of measurement** quantifies how much scores would vary due to measurement error alone. An AI that scores 85% on a benchmark might have a true score anywhere from 82% to 88% given measurement uncertainty.

**Validity (Expanded)**

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

**Classical Test Theory (CTT)**

Classical test theory models observed scores as the sum of true scores plus error:

**Observed Score = True Score + Error**

The true score represents the person's actual level on the construct; error represents random measurement variability. Reliability is defined as the ratio of true score variance to observed score variance—how much of the variability in observed scores reflects genuine differences versus measurement noise.

For AI, CTT provides a framework for understanding benchmark variability. Some variability in AI performance reflects genuine capability differences (between models); some reflects measurement noise (stochastic outputs, sample of test items).

**Item Response Theory (IRT)**

Item Response Theory provides a more sophisticated framework that models the probability of correct response as a function of both person ability and item characteristics:

- **Item difficulty**: Some items are harder than others
- **Item discrimination**: Some items better distinguish high-ability from low-ability
- **Guessing**: For multiple-choice, even zero-ability has some probability of guessing correctly

IRT allows items to be on a common scale, enables adaptive testing (selecting items based on previous responses), and provides more nuanced information about ability levels.

For AI benchmarks, IRT thinking suggests that not all benchmark items are equally informative. Some items might distinguish between capable and less-capable models (high discrimination); others might not. Benchmark design could be optimized by selecting items with high discrimination at relevant ability levels.

**Generalizability Theory (G-Theory)**

Generalizability theory extends classical reliability to account for multiple sources of measurement error simultaneously. Variance in observed scores might come from:

- Person/model differences (what we want to measure)
- Item differences (some questions harder than others)
- Rater differences (human judges disagree)
- Occasion differences (stochastic variation)
- Interactions among these factors

G-theory partitions variance into components, revealing which sources of error are largest. For AI evaluation with human raters, G-theory might reveal that rater disagreement contributes more measurement error than item sampling.

**Standard Setting**

Standard setting determines cut scores—thresholds for categorizing performance (pass/fail, proficient/not proficient). These decisions are fundamentally judgmental, not purely statistical. Methods like the Angoff method have experts estimate what minimally competent performance looks like.

For AI, standard setting questions arise constantly: At what benchmark score should we consider an AI "capable" of a task? What performance level is sufficient for deployment? These thresholds require judgment that combines measurement with values about acceptable risk.

### What Transfers to AI Evaluation

**Reliability concepts** directly apply. AI evaluations have measurement error from multiple sources—stochastic outputs, item sampling, human raters. Quantifying and reporting reliability (through multiple samples, inter-rater agreement, confidence intervals) is essential.

**The validity framework** is foundational. Every AI benchmark should be examined for:
- Content validity: Does it adequately sample the domain?
- Criterion validity: Does it predict real-world performance?
- Construct validity: Does it measure what it claims?

Most AI benchmarks have unknown validity in these senses.

**Criterion validity** is the key question: Do benchmarks predict operational value? Pursuing criterion validation studies—correlating benchmark performance with deployment outcomes—would dramatically improve evaluation quality.

**Multiple sources of error** should be recognized and measured. When AI evaluation involves human judgment (rating outputs, detecting errors), inter-rater reliability should be assessed and reported.

### What Breaks for Generative AI

**Stable trait assumption** underlies psychometrics. Tests measure relatively stable individual differences. But AI "capabilities" aren't stable—they change with model updates, prompting strategies, and fine-tuning. The entire framework assumes something stable to measure.

**Population and norming** make sense for human testing. A score of 85 means performance at the 85th percentile of some reference population. For AI, there's no natural reference population. What population should AI benchmark scores be normed against?

**Test security** assumes examinees haven't seen the test items before. For AI, training data may include benchmark items—benchmark contamination is the AI equivalent of test leakage. Psychometric methods assume this doesn't happen.

**Individual differences framing** focuses on variation between persons. AI evaluation often focuses on a single "entity" (a model), with variance being across runs or items rather than across individuals. The conceptual mapping is awkward.

### What Can Be Adapted

**IRT for benchmark design** could optimize which items to include. Items with high discrimination at relevant ability levels provide more information than items everyone gets right or everyone gets wrong.

**G-theory for evaluation design** can identify dominant sources of error. If rater disagreement dominates, invest in clearer rubrics and rater training. If item sampling dominates, use larger item sets.

**Reliability estimation methods** can be applied—computing agreement across raters, consistency across items, stability across runs. The specific techniques need adaptation but the underlying logic holds.

**Standard setting methods** could be adapted for determining AI capability thresholds, involving experts in judging what performance levels are adequate for specific uses.

### Implications for AI Evaluation

**Apply the validity framework rigorously.** For any AI benchmark, ask: What's the evidence for content validity? Criterion validity? Construct validity? Most benchmarks lack such evidence.

**Quantify and report reliability.** Report inter-rater agreement when humans evaluate. Report consistency across multiple runs. Report confidence intervals, not just point estimates.

**Recognize that criterion validity is the key question.** Content validity and face validity are necessary but not sufficient. What matters is whether benchmark performance predicts real-world value. Pursue criterion validation studies.

**Use IRT thinking in benchmark design.** Not all items are equally informative. Optimize benchmarks by selecting discriminating items at relevant ability levels.

**Be aware that many psychometric assumptions don't hold.** AI capabilities aren't stable traits. There's no natural reference population. Training may include test items. Apply psychometric insights while recognizing their limits.

### Key References

- **Cronbach, L.J., & Meehl, P.E. (1955). "Construct Validity in Psychological Tests." *Psychological Bulletin*.** Foundational paper on construct validity.

- **Messick, S. (1989). "Validity." In *Educational Measurement* (3rd ed.).** Comprehensive treatment of unified validity concept.

- **Kane, M.T. (2013). "Validating the Interpretations and Uses of Test Scores." *Journal of Educational Measurement*.** Argument-based validity framework.

- **Brennan, R.L. (2001). *Generalizability Theory*.** Definitive treatment of G-theory.

- **Embretson, S.E., & Reise, S.P. (2000). *Item Response Theory for Psychologists*.** Accessible introduction to IRT.

---

## Section 2.3: Econometrics and Causal Inference

### Overview

Econometrics provides statistical methods for estimating causal effects, particularly from observational data where randomized experiments aren't feasible. When we can't randomly assign AI use, how can we still learn about AI's causal effects?

The fundamental problem of causal inference is that we can't observe counterfactuals—we can't see what would have happened to AI users if they hadn't used AI, or what would have happened to non-users if they had. Every causal inference method is a strategy for approximating these unobservable counterfactuals.

For AI evaluation, econometric methods are essential because randomized experiments are often impractical. Organizations adopt AI for business reasons, not randomly. Users choose to use AI based on their needs and capabilities. These selection processes create correlation between AI use and outcomes that may have nothing to do with AI's causal effect.

### Core Concepts

**The Fundamental Problem of Causal Inference**

Consider estimating AI's effect on productivity. For user i, we want to compare:
- Yi(1) = productivity if user i uses AI
- Yi(0) = productivity if user i doesn't use AI

The causal effect for user i is Yi(1) - Yi(0). But we only observe one of these outcomes—the one corresponding to what actually happened. The other is counterfactual and unobservable.

All causal inference methods are strategies for approximating the missing counterfactual, typically by finding comparison cases that are similar to the treated cases in all relevant respects except the treatment.

**Difference-in-Differences (DiD)**

DiD compares changes over time between treatment and control groups:

Effect = (Treatment After - Treatment Before) - (Control After - Control Before)

The logic: even if treatment and control groups differ at baseline, if they would have followed parallel trends without treatment, the difference in their changes estimates the causal effect.

For AI, DiD might compare productivity changes in departments that adopted AI versus departments that didn't. The key assumption is parallel trends: absent AI adoption, the groups would have experienced similar productivity changes. This assumption is untestable but can be probed by examining pre-treatment trends.

**Regression Discontinuity (RD)**

RD exploits sharp cutoffs in treatment assignment. If AI access is granted based on a score threshold (employees above some performance rating get AI tools), we can compare those just above and just below the cutoff. Since they're similar in all respects except being on different sides of the cutoff, any difference in outcomes is attributable to treatment.

RD provides highly credible causal estimates but only for units near the cutoff—the local average treatment effect (LATE). Effects might differ for units far from the cutoff.

**Instrumental Variables (IV)**

IV uses exogenous variation in treatment exposure to isolate causal effects. An "instrument" is a variable that:
1. Affects treatment (strong first stage)
2. Affects outcome only through treatment (exclusion restriction)

If a random subset of users received AI training (the instrument), and training affects AI use (which affects productivity), we can use training as an instrument to estimate AI's causal effect on productivity—even though AI use itself isn't random.

Finding valid instruments is difficult. The exclusion restriction—that the instrument affects outcomes only through treatment—is untestable and often questionable.

**Propensity Score Methods**

Propensity scores model the probability of treatment given observed characteristics. Matching treated and control units with similar propensity scores creates groups that are comparable on observed variables.

For AI, propensity score matching might match AI users with non-users who have similar job roles, tenure, prior performance, and other observed characteristics. If matched pairs have similar outcomes, AI doesn't help; if AI users do better, that difference estimates the causal effect.

The critical assumption is selection on observables: conditional on observed characteristics, treatment assignment is as-if random. If unobserved factors also influence selection (motivation, interest in technology), the method fails.

**Synthetic Control**

Synthetic control constructs a comparison case by weighting control units to match the treated unit's pre-treatment characteristics. For a single organization adopting AI, synthetic control creates a "synthetic" comparison organization from weighted combinations of non-adopting organizations.

This is useful when there's one treated unit or few treated units, making traditional methods infeasible. The synthetic control should closely match the treated unit's pre-treatment trajectory.

**Heterogeneous Treatment Effects**

Average treatment effects may mask important variation. AI might help some users (novices) while not helping others (experts). Subgroup analysis examines effects for different populations.

Modern causal machine learning methods (causal forests, etc.) can discover heterogeneity data-driven, identifying which user characteristics predict larger or smaller effects.

### What Transfers to AI Evaluation

**Counterfactual thinking** is essential. What would have happened without AI? Every AI impact claim implies a counterfactual; making that counterfactual explicit improves reasoning.

**Selection bias awareness** is crucial. Who adopts AI is not random. Differences between AI users and non-users may reflect selection, not AI effects. Every observational AI study should grapple with selection.

**DiD and related designs** are directly applicable to AI rollouts. When organizations adopt AI at different times or in different departments, quasi-experimental designs can extract causal evidence.

**Heterogeneity analysis** is essential for AI. Average effects may mislead when effects vary dramatically across users. Understanding for whom AI works is as important as whether it works on average.

### What Breaks for Generative AI

**Stable unit treatment value assumption (SUTVA)** requires that one unit's treatment doesn't affect another unit's outcomes. AI use by one person may affect others—through shared documents, changed workflows, or competitive dynamics. Interference between units complicates causal interpretation.

**Treatment definition** is problematic. What does "using AI" mean? Once for a quick answer? Continuously throughout work? With expert prompting or novice prompting? The treatment is heterogeneous and hard to define.

**Long pre-treatment periods** are needed for DiD and synthetic control to establish pre-treatment trends. AI is too new for long pre-periods; technology changes during the study window.

**Exclusion restrictions** are hard to satisfy. Finding instruments that affect AI use but affect outcomes only through AI use is difficult.

### What Can Be Adapted

**Staggered adoption designs** exploit that different units adopt AI at different times. Modern DiD methods handle staggered adoption while accounting for heterogeneous effects.

**Event study designs** examine outcomes relative to adoption date, revealing dynamics of AI effects—immediate impacts, learning curves, long-term effects.

**Causal forests** can discover heterogeneity in AI effects, identifying user or task characteristics that predict larger or smaller benefits.

### Implications for AI Evaluation

**When RCTs aren't feasible, quasi-experimental methods can provide evidence.** DiD, RD, IV, and synthetic control all offer strategies for causal inference from observational data.

**Selection into AI use is a major concern.** Any observational AI study must address why some users adopt and others don't. What confounders might explain apparent effects?

**Look for natural experiments.** Situations where AI access varies for reasons unrelated to productivity—randomization by management, staggered rollouts, technical constraints—provide the best quasi-experimental opportunities.

**Analyze heterogeneity.** Don't stop at average effects. Who benefits most? Who doesn't benefit? Under what conditions? Heterogeneity analysis provides actionable insights.

**Be explicit about assumptions.** Every causal inference method requires assumptions (parallel trends, exclusion restrictions, selection on observables). State the assumptions. Assess their plausibility. Conduct sensitivity analysis.

### Key References

- **Angrist, J.D., & Pischke, J.S. (2009). *Mostly Harmless Econometrics*.** Accessible introduction to causal inference methods.

- **Cunningham, S. (2021). *Causal Inference: The Mixtape*.** Modern treatment with clear explanations and code.

- **Huntington-Klein, N. (2021). *The Effect: An Introduction to Research Design and Causality*.** Excellent introduction emphasizing intuition.

- **Athey, S., & Imbens, G.W. (2017). "The State of Applied Econometrics: Causality and Policy Evaluation." *Journal of Economic Perspectives*.** Overview from leading causal inference researchers.

- **Wager, S., & Athey, S. (2018). "Estimation and Inference of Heterogeneous Treatment Effects Using Random Forests." *Journal of the American Statistical Association*.** Causal forests methodology.

---

## Section 2.4: Qualitative Research Methods

### Overview

Qualitative research methods aim to understand phenomena through rich description, interpretation, and attention to context and meaning. Where quantitative methods measure and count, qualitative methods describe and interpret. Where quantitative methods ask "how much," qualitative methods ask "how" and "why."

For AI evaluation, qualitative methods are essential complements to quantitative approaches. Numbers can tell us that AI improves productivity by 15%, but they can't tell us how users experience AI, what strategies work, where frustrations arise, or why some users succeed while others struggle. These questions require qualitative investigation.

The "vibes" problem in AI evaluation—knowing good output when you see it but struggling to articulate criteria—is fundamentally a qualitative challenge. Understanding what quality means, how experts recognize it, and why some AI outputs feel right while others don't requires qualitative inquiry.

### Core Concepts

**Ethnography and Participant Observation**

Ethnography involves extended immersion in a setting to understand practice from participants' perspectives. Rather than brief surveys or experiments, ethnographers spend significant time observing, participating, and building deep understanding.

For AI, ethnographic approaches might involve researchers embedded in teams using AI, observing how AI integrates into workflows, what problems arise, and how practices evolve. This reveals things surveys miss: informal workarounds, unspoken norms, emergent practices.

**Interviews**

Interviews range from structured (fixed questions, standardized for comparison) to unstructured (open-ended exploration following participant's lead):

**Structured interviews** ensure comparable data across participants but may miss unexpected insights.

**Semi-structured interviews** cover key topics while allowing flexibility to pursue emergent themes.

**Unstructured interviews** maximize depth and participant voice but make comparison difficult.

**Focus groups** leverage group dynamics—participants respond to each other, surfacing shared understandings and disagreements.

For AI evaluation, interviews can explore user experience, perceived value, frustrations, and strategies. They're particularly valuable for understanding heterogeneity: why does AI work better for some users than others?

**Grounded Theory**

Grounded theory builds theory inductively from data rather than testing pre-specified hypotheses. Researchers collect data, code it for themes, compare cases, and iteratively develop theoretical understanding.

For emerging phenomena like AI use, grounded theory is valuable: we don't know enough to specify hypotheses in advance. Grounded theory develops frameworks from what's observed rather than imposing external categories.

**Case Study Methodology**

Case studies investigate bounded cases in depth using multiple data sources. A case study of AI adoption in a particular organization might draw on interviews, documents, observations, and quantitative data to build comprehensive understanding.

Case studies support analytic generalization—generalization to theory rather than to populations. The goal isn't claiming that findings apply to all organizations, but developing theoretical insights that might transfer.

**Process Tracing**

Process tracing examines causal mechanisms—not just whether X affects Y, but how. By tracing the sequence of events, decisions, and mechanisms linking cause to effect, process tracing provides within-case causal inference.

For AI, process tracing might examine how AI adoption leads (or fails to lead) to productivity gains: What sequence of changes occurred? What mechanisms operated? Where did the chain break?

**Validity in Qualitative Research**

Qualitative research has different validity concepts:

**Credibility** parallels internal validity—are findings credible given the data? Techniques include prolonged engagement, triangulation (multiple sources), and member checking (verifying interpretations with participants).

**Transferability** parallels external validity—can findings transfer to other contexts? Thick description enables readers to judge transferability to their contexts.

**Dependability** parallels reliability—would the study produce similar findings if repeated? Audit trails document procedures for scrutiny.

**Confirmability** addresses researcher bias—are findings grounded in data rather than researcher preconceptions? Reflexivity acknowledges researcher positioning.

### What Transfers to AI Evaluation

**Understanding "why"** is qualitative methods' core contribution. When AI helps some users but not others, qualitative inquiry can reveal why—what strategies successful users employ, what barriers others face.

**Exploratory power** is essential when we don't know what to measure. Qualitative methods can identify important dimensions before quantitative measurement.

**Context sensitivity** captures how AI use is embedded in work practices, relationships, and organizational systems. Decontextualized metrics may miss these crucial factors.

**User perspective** understands AI from the user's point of view—how they experience AI, what it means to them, what frustrations and satisfactions they encounter.

### What Breaks for Generative AI

**Generalization concerns** arise: qualitative findings from one setting may not transfer to others. Sample sizes are small. Representativeness isn't the goal.

**Resource intensity** limits scale. Deep qualitative work requires time and expertise. It can't be applied to thousands of cases.

**Credibility for some audiences** is limited. Stakeholders accustomed to quantitative evidence may discount qualitative findings. This is often a mistake—qualitative evidence provides different but equally important insights.

### Implications for AI Evaluation

**Use qualitative methods to understand how and why.** Numbers tell you AI helps by 15%; qualitative methods tell you how users experience this, what makes it work, where it fails.

**Employ qualitative methods when you don't know what to measure.** Early exploration should be qualitative before settling on metrics.

**Observe AI use in practice.** Surveys and experiments miss what observation catches—workarounds, informal practices, integration into complex workflows.

**Combine with quantitative methods.** Mixed methods provide comprehensive understanding: quantitative for how much, qualitative for how and why.

### Key References

- **Creswell, J.W., & Poth, C.N. (2018). *Qualitative Inquiry and Research Design* (4th ed.).** Comprehensive introduction to qualitative traditions.

- **Yin, R.K. (2018). *Case Study Research and Applications* (6th ed.).** Definitive guide to case study methodology.

- **Miles, M.B., Huberman, A.M., & Saldaña, J. (2014). *Qualitative Data Analysis* (3rd ed.).** Practical guide to analyzing qualitative data.

- **Charmaz, K. (2014). *Constructing Grounded Theory* (2nd ed.).** Modern approach to grounded theory.

- **Suchman, L. (1987). *Plans and Situated Actions*.** Classic study of human-computer interaction in context.

---

## Section 2.5: Survey Methodology

### Overview

Survey methodology is the science of collecting self-report data through questionnaires. Surveys ask people about their behaviors, experiences, attitudes, and beliefs. For AI evaluation, surveys can measure perceived productivity, satisfaction with AI tools, attitudes toward AI adoption, and self-reported usage patterns.

Survey data is relatively easy and inexpensive to collect at scale, making it attractive for AI evaluation. However, survey methodology reveals numerous pitfalls: what people report may not match what they actually do, question wording can bias responses, and who responds may not represent the population of interest.

### Core Concepts

**Questionnaire Design**

Question design profoundly affects responses:

**Item wording** matters: "How helpful is AI?" versus "How much does AI slow you down?" elicit different frames. Leading questions bias responses. Double-barreled questions (asking about two things) create ambiguity.

**Response options** shape answers: Open-ended versus closed-ended, number of scale points, labeling of points, presence of midpoint—all affect responses in ways that can be arbitrary.

**Question order** affects answers: Earlier questions prime later ones. Sensitive questions should come later. General questions before specific questions.

**Social desirability** bias leads respondents to answer in socially approved ways. Reporting AI use as helpful may feel more acceptable than admitting it doesn't help.

**Validated scales** provide established measures with known properties. The Technology Acceptance Model (TAM) scales measure perceived usefulness and ease of use with validated items.

**Sampling**

**Probability sampling** gives every member of a population a known probability of selection, enabling generalization to the population. Random sampling is the ideal.

**Non-probability sampling** (convenience samples, volunteer samples) can't support population generalization. Most AI surveys are non-probability samples of whoever chooses to respond.

**Response rates** and non-response bias: If only 20% of invited participants respond, the 80% who didn't respond may differ systematically. AI enthusiasts may be more likely to respond to AI surveys, biasing results toward positive attitudes.

**Measurement Error**

**Self-report accuracy** is limited. People don't always know their own behavior. "How often do you use AI?" may be answered inaccurately. Actual usage logs often diverge from self-reports.

**Recall bias** affects questions about past behavior. "How did your productivity change after AI adoption?" requires remembering productivity before and after—often inaccurately.

**Reference period** matters: "In the past week" is more accurate than "in general" but may capture atypical periods.

### What Transfers to AI Evaluation

**Questionnaire design principles** apply: careful item wording, validated scales where available, attention to question order and response options.

**Non-response awareness** is essential: Who responds to AI surveys? Are they representative? Self-selected respondents to AI research may be unusually interested in AI.

**Self-report limitations** should be recognized: What people say about AI may not match what they do with AI.

### What Breaks for Generative AI

**Self-report accuracy for AI use** is questionable. Do people know how much AI helps them? The studies showing perceived productivity gains exceeding actual gains suggest not.

**Rapidly changing context** challenges surveys about stable phenomena. AI tools and user skills change quickly; survey results become outdated.

### What Can Be Adapted

**Experience sampling** captures experience in real time: brief surveys triggered during AI use, asking about the current experience rather than relying on recall.

**Diary methods** have users record AI use as it happens, improving accuracy over retrospective reports.

**Combined with behavioral data**: Survey responses can be validated against actual usage logs where available.

### Implications for AI Evaluation

**User surveys are valuable but have known limitations.** They provide information about perceptions and attitudes that other methods can't access.

**Self-reported productivity may not match actual productivity.** Validate survey findings against behavioral measures where possible.

**Consider who responds.** Volunteer samples of AI users may not represent typical users.

**Use validated scales where available.** Technology acceptance scales (TAM, UTAUT) provide established measures.

### Key References

- **Groves, R.M., et al. (2009). *Survey Methodology* (2nd ed.).** Comprehensive treatment from leading survey methodologists.

- **Dillman, D.A., Smyth, J.D., & Christian, L.M. (2014). *Internet, Phone, Mail, and Mixed-Mode Surveys* (4th ed.).** Practical guide to survey design and administration.

- **Tourangeau, R., Rips, L.J., & Rasinski, K. (2000). *The Psychology of Survey Response*.** Cognitive processes underlying survey response.

- **Venkatesh, V., et al. (2003). "User Acceptance of Information Technology: Toward a Unified View." *MIS Quarterly*.** UTAUT model and technology acceptance measurement.

---

*[End of Section 2]*
