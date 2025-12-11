# Appendix A, Section 2.1: Experimental Design and Analysis

## Overview

Experimental design is the science of structuring studies to support valid causal inferences. When we want to know whether an intervention causes an effect—not just whether it correlates with an outcome—we need experimental methods that isolate the causal relationship from confounding factors.

For AI evaluation, this matters profoundly. The central question "Does AI improve productivity?" is a causal question. Observing that AI users perform better than non-users doesn't establish that AI caused the improvement—users who adopt AI may differ systematically from those who don't. Rigorous experimental design provides frameworks for moving from correlation to causation.

This section surveys the core concepts of experimental design, examines their applicability to AI evaluation, identifies where the assumptions of experimental methodology become strained, and draws implications for evaluation practice.

---

## Core Concepts

### Randomized Controlled Trials (RCTs)

The randomized controlled trial is the gold standard for causal inference. Its logic is elegant: randomly assign units (people, teams, organizations) to treatment and control conditions. Because assignment is random, the groups should be comparable on all characteristics—both observed and unobserved—except for the treatment itself. Any systematic difference in outcomes can therefore be attributed to the treatment.

RCTs for AI might randomly assign some workers to use AI tools while others use traditional methods, then compare productivity outcomes. Random assignment ensures that differences in outcomes reflect AI's causal effect, not pre-existing differences between users who would choose to adopt AI versus those who wouldn't.

The power of randomization comes from what it eliminates: selection bias (users choosing AI are different), confounding (some third factor causing both AI adoption and productivity), and reverse causation (productive people adopting AI rather than AI making people productive). Without randomization, all these alternatives remain plausible.

### Validity Types

Experimental methodology distinguishes several types of validity:

**Internal validity** asks: Can we attribute observed effects to the treatment? Did the intervention actually cause the outcome? Threats to internal validity include selection bias, confounding, measurement error, and experimental artifacts. High internal validity means we can be confident the treatment caused the effect.

**External validity** asks: Do findings generalize beyond the study? Results from one setting, population, or time may not transfer to others. A study of programmers using Copilot may not generalize to analysts using ChatGPT, or to the same programmers six months later when both tools and skills have evolved.

**Construct validity** asks: Are we measuring what we intend to measure? If we measure "productivity" by lines of code, do lines of code actually capture productivity? If we measure AI's effect on a specific benchmark, does that construct represent real-world capability?

**Statistical conclusion validity** asks: Are our statistical inferences appropriate? With sufficient data? Using appropriate methods? Accounting for multiple comparisons? A study might be well-designed but underpowered to detect real effects, or might claim significance that doesn't survive appropriate corrections.

These validity types often trade off. Tightly controlled laboratory experiments may have high internal validity but low external validity. Field studies may have higher external validity but struggle with internal validity because conditions can't be fully controlled.

### Control and Comparison Conditions

Every experiment requires comparison—but comparison to what? The choice of control condition profoundly affects interpretation:

**No-treatment control** compares treatment to nothing. Workers using AI versus workers using no tools. This shows whether AI helps relative to nothing, but doesn't reveal whether AI helps relative to alternatives.

**Active control** compares treatment to an alternative intervention. Workers using AI versus workers using traditional search engines and documentation. This shows AI's marginal value above existing tools.

**Placebo control** attempts to control for expectation effects. In medicine, sugar pills; for AI, perhaps a non-functional AI interface that gives users the belief they're using AI. This is often impractical for AI studies but highlights the question: how much of AI's apparent benefit comes from users believing they have a powerful tool?

**Within-subjects design** exposes the same people to both conditions (with and without AI), controlling for individual differences. But this creates order effects and learning confounds.

**Between-subjects design** assigns different people to different conditions, avoiding carryover effects but requiring larger samples to account for individual variation.

For AI evaluation, comparison condition choice is crucial. Comparing AI to nothing overstates AI's value; comparing to best alternatives understates it. The appropriate comparison depends on the decision being informed.

### Confounding and Bias

Even well-designed experiments can suffer from biases:

**Selection bias** occurs when treatment and control groups differ systematically. In AI studies, if AI adoption is voluntary, users who choose to adopt may differ in motivation, technical skill, or task characteristics.

**Attrition bias** occurs when participants drop out differentially. If frustrated AI users abandon the study while frustrated control participants persist, remaining AI users appear more successful than they actually are.

**Experimenter effects** occur when experimenters' expectations influence outcomes. An evaluator who believes AI is helpful may unconsciously score AI-assisted work more favorably.

**Demand characteristics** occur when participants guess the study's hypothesis and behave accordingly. Workers who know they're in an "AI productivity study" may try harder when using AI.

**Hawthorne effects** occur when being observed changes behavior. Workers being studied may work differently regardless of experimental condition.

### Statistical Power and Sample Size

Power analysis determines how many observations are needed to detect effects of a given size with acceptable confidence. Underpowered studies may fail to detect real effects (Type II error), while studies with many comparisons may find spurious effects (Type I error).

Effect sizes in AI studies vary widely. A study powered to detect a 50% productivity improvement will miss a 10% improvement—which may still be practically significant. Sample size planning requires prior estimates of expected effect size and acceptable error rates.

Multiple comparisons compound the problem. If you test AI effects on ten different outcome measures, you expect one significant result by chance at p < 0.10 even if AI has no effect. Pre-registration of hypotheses and appropriate statistical corrections help address this.

### Replication and Reproducibility

The replication crisis in psychology and other fields highlighted that many published findings don't reproduce. Causes include low statistical power, flexible analysis methods ("p-hacking"), publication bias favoring positive results, and genuine context-dependence.

Pre-registration addresses some concerns: committing to hypotheses and analysis plans before seeing data constrains researcher degrees of freedom. Registered reports go further, accepting papers for publication based on methods before results are known.

For AI evaluation, replication faces additional challenges: models change, tools update, and user skills evolve. An experiment with GPT-3.5 may not replicate with GPT-4. This isn't a flaw in the original study—it reflects genuinely changing technology.

---

## What Transfers to AI Evaluation

Several elements of experimental methodology transfer directly:

**The validity framework** provides essential vocabulary for assessing AI evaluation quality. Every AI study can be examined for internal validity (is the causal claim supported?), external validity (do findings generalize?), and construct validity (do measurements capture what matters?). This framework structures critical assessment.

**Control condition thinking** is essential. AI claims are meaningful only relative to comparison. What would have happened without AI? What would happen with alternative tools? Making comparison conditions explicit forces clearer thinking about AI's contribution.

**Bias awareness** helps identify threats to evaluation credibility. Who chose to use AI? Who dropped out? How were outcomes measured? Systematic consideration of potential biases improves evaluation design and interpretation.

**Power analysis** should inform evaluation planning. How large an effect should this study be able to detect? Is the sample size adequate? Acknowledging power limitations helps calibrate confidence in results.

**Pre-registration** reduces researcher degrees of freedom. Committing to analysis plans before seeing data constrains the flexibility that enables spurious findings.

---

## What Breaks for Generative AI

Several assumptions of experimental methodology become strained for AI evaluation:

**Treatment stability** is assumed throughout experimental methodology—the treatment is the same for all participants and doesn't change during the study. AI systems change continuously. A three-month experiment may span multiple model updates. The "treatment" a participant receives in month three may differ from month one.

**Blinding** is often impossible. In medical trials, patients can be blinded to whether they receive drug or placebo. In AI studies, users typically know whether they're using AI. This creates potential for expectation effects—users may perform better with AI partly because they expect AI to help.

**Standardized treatment** is assumed—everyone receives the same intervention. But AI use is highly variable. One user may prompt expertly; another may prompt poorly. The "treatment" depends on how users interact with the AI. This is like studying a drug where dosage varies based on how patients feel about it.

**Stable outcomes** are assumed—the outcome measure means the same thing across conditions. But AI may change what work means. If AI-assisted writing produces different kinds of documents than unassisted writing, comparing "productivity" may be comparing apples and oranges.

**Ecological validity** is challenged. Laboratory experiments with defined tasks may not capture real-world AI use, which is embedded in complex workflows with interruptions, iteration, and judgment. But field experiments sacrifice control for realism.

**Effect size stability** is assumed for meta-analysis—the underlying effect doesn't change across studies. AI effect sizes likely do change as technology improves and users learn. Meta-analytic combination of AI studies is problematic when the "treatment" differs fundamentally across studies.

---

## What Can Be Adapted

**Quasi-experimental designs** don't require randomization but still support causal inference under certain assumptions. When randomized experiments aren't feasible, quasi-experiments offer alternatives (see Section 2.3 on econometrics).

**Mixed methods** combine quantitative experiments with qualitative investigation. Experiments establish whether AI has effects; qualitative methods help understand how and why. For AI, understanding the mechanism—how users interact with AI, what prompting strategies work—is as important as measuring effects.

**Adaptive designs** modify study protocols based on interim results. If early results suggest AI helps some users but not others, the study can shift focus. This flexibility is valuable for rapidly evolving technology.

**N-of-1 trials** study single individuals over time, alternating between conditions. For AI use that's highly personalized, individual-level experiments may be more informative than between-group comparisons.

---

## Implications for AI Evaluation

**Apply the validity framework.** For any AI evaluation, ask: What's the evidence for internal validity? How far do findings generalize? Do measurements capture what matters? This framework structures critical assessment.

**Make comparison conditions explicit.** Relative to what? No tools? Current tools? Previous AI versions? Human experts? The choice of comparison determines what claims can be supported.

**Design with bias awareness.** Consider selection, attrition, experimenter, and demand biases. Build in safeguards: random assignment where possible, blinded assessment where feasible, measurement of potential confounders.

**Plan for adequate power.** Don't run underpowered studies. Estimate expected effect sizes, calculate required sample sizes, and acknowledge power limitations.

**Consider pre-registration.** For important evaluations, commit to hypotheses and analysis plans before seeing data. This won't solve all problems but reduces researcher flexibility that enables spurious findings.

**Accept trade-offs.** Internal validity often trades off against external validity. Laboratory control sacrifices ecological validity. Choose designs appropriate to the questions and decisions at stake.

**Don't expect stability.** AI changes. Users learn. Effects may not replicate six months later—not because the original study was wrong, but because the world changed. Build this expectation into interpretation.

---

## Key References

- **Shadish, W.R., Cook, T.D., & Campbell, D.T. (2002). *Experimental and Quasi-Experimental Designs for Generalized Causal Inference*.** The definitive treatment of experimental validity and design.

- **Gerber, A.S., & Green, D.P. (2012). *Field Experiments: Design, Analysis, and Interpretation*.** Comprehensive guide to experiments in field settings.

- **Simmons, J.P., Nelson, L.D., & Simonsohn, U. (2011). "False-Positive Psychology." *Psychological Science*.** Influential paper on researcher degrees of freedom and the need for pre-registration.

- **Open Science Collaboration. (2015). "Estimating the Reproducibility of Psychological Science." *Science*.** Landmark replication study with lessons for all empirical fields.

- **Nosek, B.A., et al. (2018). "The Preregistration Revolution." *PNAS*.** Case for pre-registration in empirical research.

---

## Connections to Other Sections

Experimental design concepts connect to several other disciplines covered in this appendix:

- **Section 1.1 (Software Testing)** shares the concern with systematic coverage and the difficulty of exhaustive testing.

- **Section 2.2 (Psychometrics)** provides frameworks for measurement reliability and validity that complement experimental validity.

- **Section 2.3 (Econometrics)** extends causal inference to non-experimental settings with quasi-experimental methods.

- **Section 2.4 (Qualitative Methods)** provides complementary approaches for understanding how and why effects occur.

- **Section 5.4 (JDM)** illuminates cognitive biases that affect both AI users and evaluators in experimental settings.

- **Section 6.4 (Clinical Trial Methodology)** offers related frameworks for phased evaluation and adaptive designs.

---

*[End of Section 2.1]*
