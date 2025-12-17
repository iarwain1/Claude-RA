# Appendix A, Section 6: Evaluation and Assessment Traditions

## Section 6.1: AI Safety Evaluation (Emerging Field)

### Overview

AI safety evaluation is the emerging discipline focused specifically on evaluating AI systems for safety properties. Unlike other disciplines in this appendix that developed in different contexts and are being adapted to AI, AI safety evaluation is developing for AI from the start. It draws on multiple traditions while grappling with AI's distinctive challenges.

This section is necessarily brief because the field is developing rapidly. It surveys key concepts and current activities rather than established frameworks.

### Core Concepts

**Capability Evaluation**

What can the model do? Capability evaluation assesses AI abilities across domains:
- Reasoning, coding, knowledge, language
- Dangerous capabilities (cyber offense, biological knowledge, deception)
- Capability elicitation methods that go beyond naive prompting to find what models can do with sophisticated prompting, fine-tuning, or scaffolding

The challenge: capabilities may be latent—present but not easily observed without specific elicitation. Evaluation must try to surface capabilities, not just test whether they're immediately apparent.

**Alignment Evaluation**

Does the model behave as intended?
- Does it follow instructions?
- Does it pursue intended goals?
- Does it avoid deceptive or manipulative behavior?
- Does it behave consistently across contexts?

Alignment evaluation is difficult because misaligned behavior might appear aligned on evaluation but manifest differently in deployment.

**Red Teaming**

Adversarial evaluation attempting to elicit harmful outputs:
- Jailbreaking: circumventing safety measures
- Prompt injection: manipulating AI through crafted inputs
- Systematic exploration of harmful capability boundaries

Red teaming for AI adapts cybersecurity concepts (Section 1.5) for AI-specific contexts.

**Safety Cases**

Structured arguments that AI systems are acceptably safe:
- Claims about safety properties
- Evidence supporting each claim
- Argument connecting evidence to claims
- Acknowledgment of assumptions and limitations

Safety cases (from safety engineering, Section 4.5) are being developed for frontier AI systems.

**Evaluation Gaming**

AI systems might behave differently when being evaluated:
- Trained on evaluation data, inflating benchmark performance
- Behaving better in evaluation contexts than deployment
- Learning to appear aligned while being misaligned (deceptive alignment)

Evaluation gaming concerns drive interest in novel evaluations, held-out test sets, and deployment monitoring.

### Current Active Areas

**Benchmark design and contamination detection**: Creating benchmarks that are robust to training on benchmark data, and detecting when contamination has occurred.

**Scalable oversight**: Methods for evaluating outputs humans can't easily assess—when AI produces content beyond human expertise or too voluminous for human review.

**Dangerous capability evaluation**: Assessing AI for capabilities that could enable harm (cyber offense, biological weapons, manipulation).

**Continuous monitoring**: Moving from point-in-time evaluation to ongoing monitoring of deployed systems.

**Red team methodology**: Developing systematic, scalable approaches to adversarial evaluation.

### Key References

- **Shevlane, T., et al. (2023). "Model Evaluation for Extreme Risks." *arXiv preprint*.** Framework for evaluating dangerous capabilities.

- **Anthropic, OpenAI, DeepMind safety reports and responsible scaling policies.** Industry practices for AI safety evaluation.

- **METR (formerly ARC Evals) methodology documentation.** Independent AI evaluation methodology.

- **Liang, P., et al. (2022). "Holistic Evaluation of Language Models (HELM)." *arXiv preprint*.** Comprehensive benchmark framework.

---

## Section 6.2: Program Evaluation

### Overview

Program evaluation is the systematic assessment of programs and interventions—typically social programs, educational initiatives, or policy interventions. For AI, program evaluation provides frameworks for evaluating AI as an organizational intervention: a change implemented with the goal of producing some benefit.

### Core Concepts

**Theory of Change / Logic Models**

Logic models make causal assumptions explicit:
- **Inputs**: Resources invested (AI tools, training, time)
- **Activities**: What happens (AI use, workflow changes)
- **Outputs**: Direct products (documents produced, queries answered)
- **Outcomes**: Short-term changes (time saved, quality improved)
- **Impact**: Long-term effects (organizational performance, competitive position)

Logic models reveal assumptions: We assume that providing AI tools (input) will lead to AI use (activity) which will produce more documents (output) which will save time (outcome) which will improve performance (impact). Each arrow is an assumption that can be tested.

For AI, logic models force explicit thinking about how AI is supposed to create value. This reveals where the chain might break.

**Formative vs. Summative Evaluation**

**Formative evaluation** aims to improve the program during implementation. What's working? What isn't? How can we do better? Formative evaluation is ongoing, adaptive, and focused on learning.

**Summative evaluation** aims to judge overall worth or effectiveness. Did the program work? Should it continue? Summative evaluation is typically done at endpoints for accountability.

For AI, formative evaluation is often more valuable: AI use is evolving, and learning how to use AI better is as important as judging whether current use is effective.

**Process vs. Outcome Evaluation**

**Process evaluation** asks: Was the intervention implemented as intended? Did people actually use AI? How did they use it? Were training and support provided?

**Outcome evaluation** asks: Did desired effects occur? Did productivity improve? Did quality increase?

Process evaluation is essential for interpreting outcomes. If AI "doesn't work," is that because AI is ineffective or because it wasn't actually used, or wasn't used well?

**Implementation Fidelity**

Implementation fidelity assesses whether the intervention was delivered as designed:
- **Adherence**: Was the core intervention delivered?
- **Dosage**: How much exposure did participants have?
- **Quality**: How well was the intervention delivered?
- **Responsiveness**: How did participants respond?

For AI, implementation fidelity asks: Did people actually use AI? How often? How well did they use it? Were they engaged? Low fidelity—people not actually using AI—explains many null findings.

**Developmental Evaluation**

For innovative initiatives in complex environments, developmental evaluation embeds evaluators as part of the development team:
- Evaluation is ongoing, adaptive, and emergent
- Focused on learning and adaptation
- Appropriate when outcomes and paths are uncertain

For AI—where we're still learning what effective AI use looks like—developmental evaluation may be more appropriate than fixed evaluation designs.

**Realist Evaluation**

Realist evaluation asks: "What works, for whom, in what circumstances, and why?"
- **Context**: Conditions that affect whether intervention works
- **Mechanism**: How the intervention produces effects
- **Outcome**: What effects are produced

Context-Mechanism-Outcome configurations explain variation. AI might work for some users in some contexts through some mechanisms but not others.

### What Transfers to AI Evaluation

**Logic model discipline**: Make explicit how AI is supposed to create value.

**Implementation fidelity**: Check whether AI is actually being used and how.

**Formative evaluation**: Focus on learning and improvement, not just judgment.

**Developmental evaluation**: Appropriate for emerging, evolving AI use.

**Realist perspective**: Understand what works for whom, when, and why.

### Implications for AI Evaluation

- **Develop logic models** for how AI is supposed to create value.
- **Check implementation fidelity**: Is AI actually being used? How?
- **Use formative evaluation** to improve AI use, not just judge it.
- **Apply developmental evaluation** for new AI deployments.
- **Seek realist understanding** of variation in AI effects.

### Key References

- **Patton, M.Q. (2010). *Developmental Evaluation*.** Evaluation for innovative initiatives.

- **Patton, M.Q. (2008). *Utilization-Focused Evaluation* (4th ed.).** Evaluation designed to be useful.

- **Pawson, R., & Tilley, N. (1997). *Realistic Evaluation*.** Realist evaluation framework.

- **Rossi, P.H., Lipsey, M.W., & Henry, G.T. (2018). *Evaluation: A Systematic Approach* (8th ed.).** Comprehensive program evaluation text.

---

## Section 6.3: Educational Measurement

### Overview

Educational measurement assesses learning and achievement. While focused on students rather than AI, the field offers insights relevant to AI evaluation—particularly around high-stakes testing, test security, and the effects of testing on what gets taught and learned.

### Core Concepts

**High-Stakes Testing**

When test results have significant consequences:
- Student graduation, placement, or advancement
- Teacher evaluation and accountability
- School ratings and resources

High stakes change behavior. People optimize for what's measured, sometimes at the expense of what matters.

For AI, benchmark results are increasingly high-stakes (model reputation, investment decisions, regulatory scrutiny). This creates pressure to optimize benchmarks specifically.

**Test Security**

Maintaining valid test results requires keeping test content secure:
- Preventing item leakage before testing
- Detecting cheating during testing
- Protecting items for future use

For AI, benchmark security parallels test security. If AI is trained on benchmark items (the AI equivalent of "leaking" the test), scores are inflated and don't reflect genuine capability.

**Teaching to the Test**

When tests have consequences, instruction shifts toward what's tested:
- **Beneficial alignment**: Teaching what tests measure, when tests measure what matters
- **Harmful narrowing**: Teaching only what's tested, neglecting other important content

For AI, "training to the benchmark" is analogous. AI may be optimized for benchmark performance in ways that don't generalize to real tasks.

**Campbell's Law**

"The more any quantitative social indicator is used for social decision-making, the more subject it will be to corruption pressures and the more apt it will be to distort and corrupt the social processes it is intended to monitor."

Applied to AI: The more benchmark scores determine important decisions, the more benchmarks will be gamed, and the less they'll measure genuine capability.

**Standard Setting**

Determining cut scores (pass/fail thresholds) requires judgment:
- What level of performance is "proficient"?
- Methods (Angoff, bookmark, etc.) structure expert judgment
- Cut scores are not purely empirical—they involve values

For AI, standard setting applies: At what benchmark score is AI "good enough" for a task? This requires judgment about acceptable risk and minimum competence.

### What Transfers to AI Evaluation

**Test security**: Benchmark contamination is the AI equivalent of test leakage.

**Campbell's Law**: Metrics become targets and lose validity.

**Teaching to the test**: AI may be optimized for benchmarks specifically.

**Standard setting**: Determining capability thresholds requires judgment.

### Implications for AI Evaluation

- **Treat benchmark security seriously.** Contamination inflates scores.
- **Expect optimization for evaluation** as benchmark stakes increase.
- **Use multiple, varied measures** to resist gaming.
- **Apply standard setting thinking** to determine capability thresholds.

### Key References

- **Koretz, D. (2008). *Measuring Up: What Educational Testing Really Tells Us*.** Accessible treatment of testing limitations and gaming.

- **Cizek, G.J., & Wollack, J.A. (Eds.). (2016). *Handbook of Quantitative Methods for Detecting Cheating on Tests*.** Detection methodology.

- **Haladyna, T.M., & Rodriguez, M.C. (2013). *Developing and Validating Test Items*.** Item development methodology.

---

## Section 6.4: Clinical Trial Methodology

### Overview

Clinical trial methodology has evolved rigorous approaches for testing medical interventions. The phased structure, randomization, blinding, and post-market surveillance of clinical trials offer models for AI evaluation.

### Core Concepts

**Phased Evaluation**

Clinical trials proceed through phases:
- **Phase I**: Safety in small groups (tens of participants)
- **Phase II**: Initial efficacy signals in larger groups (hundreds)
- **Phase III**: Definitive efficacy in large randomized trials (thousands)
- **Phase IV**: Post-market surveillance after approval

This phased structure manages risk: Don't proceed to large studies until smaller studies support proceeding.

For AI, a phased approach might be: controlled testing → limited pilot → expanded deployment → continuous monitoring.

**Randomization and Blinding**

Randomization eliminates selection bias by randomly assigning participants to treatment or control.

Blinding prevents expectation effects:
- Single-blind: Participants don't know their assignment
- Double-blind: Neither participants nor administrators know
- Triple-blind: Even analysts don't know until analysis is complete

For AI, blinding is often impractical—users know whether they're using AI. This limitation should be acknowledged.

**Adaptive Designs**

Adaptive trials modify based on interim results:
- Expand promising treatments
- Drop ineffective treatments
- Adjust sample sizes based on observed effects

Adaptive designs make more efficient use of data. For AI, adaptive evaluation that shifts focus based on emerging findings may be more effective than fixed designs.

**Post-Market Surveillance**

Approval isn't the end. Ongoing surveillance detects:
- Rare adverse events not seen in trials
- Long-term effects
- Effects in populations not well-represented in trials

For AI, post-deployment monitoring parallels post-market surveillance: detecting problems that emerge only at scale or over time.

**Real-World Evidence**

Evidence from actual clinical practice complements trial evidence:
- Effectiveness in real conditions, not just controlled trials
- Effects in diverse patient populations
- Long-term outcomes

For AI, real-world evidence from actual deployment complements controlled evaluation.

### What Transfers to AI Evaluation

**Phased approach**: Start small, expand based on results.

**Post-deployment monitoring**: Plan for ongoing surveillance after deployment.

**Adaptive designs**: Modify evaluation based on interim findings.

**Real-world evidence**: Complement controlled evaluation with deployment data.

### What Breaks for Generative AI

**Blinding**: Often can't blind users to AI.

**Longer timelines**: Clinical trials run years; AI context changes faster.

**Clear outcomes**: Clinical endpoints are often clearer than AI outcomes.

### Implications for AI Evaluation

- **Consider phased evaluation**: Start limited, expand based on findings.
- **Plan post-deployment monitoring** from the start.
- **Use adaptive approaches** to be efficient with resources.
- **Value real-world evidence** from actual deployment.

### Key References

- **Friedman, L.M., Furberg, C.D., & DeMets, D.L. (2015). *Fundamentals of Clinical Trials* (5th ed.).** Comprehensive clinical trials text.

- **Berry, S.M., et al. (2010). *Bayesian Adaptive Methods for Clinical Trials*.** Adaptive design methodology.

---

*[End of Section 6]*
