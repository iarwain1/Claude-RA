# Appendix A, Section 5.4: Judgment and Decision Making (JDM)

## Overview

JDM research studies how people make judgments and decisions, including systematic biases and departures from rationality. This research is directly relevant to understanding how humans use (and misuse) AI advice—and how human evaluators of AI may be biased in their assessments.

The heuristics-and-biases tradition, pioneered by Kahneman and Tversky, has documented numerous ways human judgment systematically departs from normative standards. These biases affect how people interact with AI and how they evaluate AI performance.

---

## Core Concepts

### Heuristics and Biases

Humans use cognitive shortcuts (heuristics) that usually work but can lead to systematic errors:

**Availability**: Judging likelihood by how easily examples come to mind. Dramatic, recent, or vivid events are overweighted.
- For AI: Dramatic AI successes may be more available than routine failures. A few impressive demos may create inflated impressions.

**Anchoring**: Estimates influenced by initial values, even irrelevant ones. Insufficient adjustment from anchors.
- For AI: AI suggestions may anchor human judgment even when suggestions are wrong. Users may adjust insufficiently from AI starting points.

**Representativeness**: Judging probability by similarity to stereotypes, ignoring base rates.
- For AI: An AI output that "sounds right" may be accepted even if it's factually wrong. Surface fluency creates impression of correctness.

**Confirmation bias**: Seeking and interpreting information to confirm existing beliefs. Discounting disconfirming evidence.
- For AI: Users who believe AI helps may notice confirming cases. Evaluators with prior beliefs may find confirming evidence.

**Hindsight bias**: After learning outcomes, believing they were predictable all along.
- For AI: After AI failures, claiming "I knew that would happen" even if you didn't.

**Overconfidence**: Excessive confidence in own judgments. Confidence exceeds accuracy.
- For AI: Users may be overconfident in AI-assisted work, believing AI made it better than it actually is.

### Algorithm Aversion

People often resist algorithmic recommendations even when algorithms outperform humans:

- Seeing an algorithm err reduces trust more than seeing a human err
- People want control and understanding
- Perfect algorithms are less trusted than imperfect humans who can improve
- People prefer to keep humans in the loop even when algorithms are superior

For AI, algorithm aversion may cause underuse of helpful AI. Users may reject good AI suggestions because they don't trust or understand them.

### Algorithm Appreciation

The flip side: over-reliance on algorithmic advice:

**Automation bias**: Accepting AI recommendations uncritically. Failing to notice AI errors.

**Diffusion of responsibility**: AI suggested it, so user feels less responsible. "The AI said to do it."

**Authority effect**: AI perceived as authoritative, so suggestions are accepted without scrutiny.

Algorithm appreciation is particularly strong when:
- AI is perceived as expert or authoritative
- Users lack confidence in their own judgment
- Time pressure discourages critical evaluation

For AI, algorithm appreciation may cause overuse and uncritical acceptance. Users may accept AI outputs without verification.

### Advice Taking

Research on judge-advisor systems shows:

**Advice discounting**: People typically discount advice, weighting it less than their own judgment. They weight their own opinion more heavily than advisors' opinions.

**Factors affecting discounting**:
- Perceived advisor expertise
- Advisor confidence
- Relationship to own beliefs
- Track record and feedback

**AI as advisor**: Do users discount AI advice appropriately? Evidence suggests AI is both over-trusted (when it sounds good) and under-trusted (when users are skeptical of "machines").

### Calibration

Calibration is match between confidence and accuracy:

**Overconfidence**: People are often more confident than accuracy warrants. Claiming 90% confidence when accuracy is 70%.

**Underconfidence**: Less common; sometimes in domains of high uncertainty.

**Calibration training**: Can improve calibration through feedback.

For AI users, calibration asks:
- Do users know when to trust AI?
- Are they appropriately confident in AI-assisted outputs?
- Can calibration be improved through training and feedback?

### Noise

Noise is unwanted variability in judgments that should be identical:

**Between-judge noise**: Different judges give different ratings to the same case.

**Within-judge noise**: Same judge gives different ratings at different times.

**System noise**: Aggregate variability in judgments across the system.

Human evaluation of AI outputs is noisy. This noise contributes to measurement error in AI evaluation. Different evaluators may rate the same AI output differently; same evaluator may rate it differently at different times.

### Decision Hygiene

Kahneman et al. recommend "decision hygiene" to reduce bias and noise:

**Aggregate independent judgments**: Multiple judges; aggregate rather than rely on one.

**Structure judgment**: Break complex judgments into components; use checklists and rubrics.

**Sequence information**: Don't expose judges to irrelevant information that might bias them.

**Delay intuition**: Get component judgments before overall assessment.

These principles apply to AI evaluation: structured rubrics, multiple evaluators, independent judgments, explicit criteria.

---

## What Transfers to AI Evaluation

**Bias awareness**: Both AI users and AI evaluators are subject to cognitive biases. Design evaluation to reduce bias.

**Algorithm aversion/appreciation**: Affects AI adoption and use patterns. Neither under-use nor over-use is desirable.

**Calibration**: Do users know when to trust AI? Calibration is essential for appropriate AI use.

**Noise**: Human evaluation is inherently variable. Quantify and account for noise.

**Decision hygiene**: Structure, independence, and aggregation improve judgment quality.

---

## What Breaks for Generative AI

**Clear correct answers**: Much JDM research uses tasks with objectively correct answers. Many AI tasks don't have single correct answers.

**Stable algorithms**: JDM research on algorithms assumed stable, deterministic systems. AI is stochastic and changing.

**Simple advice**: Judge-advisor research often involves simple advice. AI provides complex, varied outputs.

---

## What Can Be Adapted

**Calibration training** to help users develop appropriate AI trust. Feedback on when AI was reliable/unreliable.

**Structured evaluation** to reduce evaluator bias and noise. Rubrics, independent judgments, aggregation.

**De-biasing interventions** for AI users and evaluators. Awareness training, checklists, structured processes.

---

## Implications for AI Evaluation

**Design evaluation to reduce bias** (structure, blinding where possible). Bias affects evaluators, not just AI users.

**Evaluate for appropriate AI reliance**, not just AI use. Neither aversion nor uncritical acceptance is desirable.

**Quantify and account for noise** in human evaluation. Inter-rater reliability should be measured.

**Consider training** for calibrated AI use. Users can improve calibration with appropriate feedback.

**Use decision hygiene** in evaluation processes. Structure, independence, aggregation.

---

## Key References

- **Kahneman, D. (2011). *Thinking, Fast and Slow*.** Accessible introduction to heuristics and biases.

- **Kahneman, D., Sibony, O., & Sunstein, C.R. (2021). *Noise*.** Systematic treatment of judgment variability.

- **Dietvorst, B.J., Simmons, J.P., & Massey, C. (2015). "Algorithm Aversion." *Journal of Experimental Psychology: General*.** Algorithm aversion research.

- **Logg, J.M., Minson, J.A., & Moore, D.A. (2019). "Algorithm Appreciation." *Organizational Behavior and Human Decision Processes*.** Algorithm appreciation research.

- **Sniezek, J.A., & Buckley, T. (1995). "Cueing and Cognitive Conflict in Judge-Advisor Decision Making." *Organizational Behavior and Human Decision Processes*.** Advice taking research.

---

## Connections to Other Sections

JDM connects to several other disciplines covered in this appendix:

- **Section 5.2 (Human Factors)** addresses trust calibration and automation bias from different perspective.

- **Section 2.2 (Psychometrics)** addresses measurement reliability related to noise concepts.

- **Section 5.5 (I-O Psychology)** addresses structured assessment that reduces bias and noise.

- **Section 2.1 (Experimental Design)** addresses bias in experimental settings.

- **Section 4.4 (Audit)** emphasizes professional skepticism related to bias resistance.

---

*[End of Section 5.4]*
