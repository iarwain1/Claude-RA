# Appendix A, Section 2.5: Survey Methodology

## Overview

Survey methodology is the science of collecting self-report data through questionnaires. Surveys ask people about their behaviors, experiences, attitudes, and beliefs. For AI evaluation, surveys can measure perceived productivity, satisfaction with AI tools, attitudes toward AI adoption, and self-reported usage patterns.

Survey data is relatively easy and inexpensive to collect at scale, making it attractive for AI evaluation. However, survey methodology reveals numerous pitfalls: what people report may not match what they actually do, question wording can bias responses, and who responds may not represent the population of interest.

---

## Core Concepts

### Questionnaire Design

Question design profoundly affects responses:

**Item wording** matters: "How helpful is AI?" versus "How much does AI slow you down?" elicit different frames. Leading questions bias responses. Double-barreled questions (asking about two things) create ambiguity.

**Response options** shape answers: Open-ended versus closed-ended, number of scale points, labeling of points, presence of midpoint—all affect responses in ways that can be arbitrary.

**Question order** affects answers: Earlier questions prime later ones. Sensitive questions should come later. General questions before specific questions can anchor responses.

**Social desirability** bias leads respondents to answer in socially approved ways. Reporting AI use as helpful may feel more acceptable than admitting it doesn't help.

**Acquiescence bias** leads some respondents to agree with statements regardless of content. Mixing positively and negatively worded items can detect this.

### Validated Scales

Validated scales provide established measures with known properties:

**Technology Acceptance Model (TAM)** scales measure perceived usefulness and ease of use—key predictors of technology adoption.

**UTAUT** (Unified Theory of Acceptance and Use of Technology) extends TAM with additional constructs: social influence, facilitating conditions, and demographics.

**NASA-TLX** measures perceived workload across multiple dimensions—useful for assessing AI's cognitive load effects.

Using validated scales ensures comparability across studies and provides psychometric properties (reliability, validity) that custom questions lack.

### Sampling

**Probability sampling** gives every member of a population a known probability of selection, enabling generalization to the population. Random sampling is the ideal.

**Non-probability sampling** (convenience samples, volunteer samples) can't support population generalization. Most AI surveys are non-probability samples of whoever chooses to respond.

**Stratified sampling** ensures representation of key subgroups. For AI surveys, stratifying by role, experience, or AI usage patterns may improve representativeness.

**Response rates** and non-response bias: If only 20% of invited participants respond, the 80% who didn't respond may differ systematically. AI enthusiasts may be more likely to respond to AI surveys, biasing results toward positive attitudes.

### Measurement Error

**Self-report accuracy** is limited. People don't always know their own behavior. "How often do you use AI?" may be answered inaccurately. Actual usage logs often diverge from self-reports.

**Recall bias** affects questions about past behavior. "How did your productivity change after AI adoption?" requires remembering productivity before and after—often inaccurately.

**Reference period** matters: "In the past week" is more accurate than "in general" but may capture atypical periods.

**Social desirability** leads to over-reporting of socially approved behaviors (careful AI verification) and under-reporting of disapproved behaviors (uncritical AI acceptance).

### Survey Modes

Different survey modes have different properties:

**Online surveys** are inexpensive and fast but suffer from coverage bias (who has internet access?) and often low response rates.

**Phone surveys** allow clarification and probing but are expensive and suffer declining response rates.

**In-person surveys** achieve highest response rates and allow observation but are most expensive.

**Mixed-mode surveys** combine approaches, potentially improving coverage and response.

---

## What Transfers to AI Evaluation

**Questionnaire design principles** apply: careful item wording, validated scales where available, attention to question order and response options.

**Non-response awareness** is essential: Who responds to AI surveys? Are they representative? Self-selected respondents to AI research may be unusually interested in AI.

**Self-report limitations** should be recognized: What people say about AI may not match what they do with AI.

**Validated instruments** provide better measurement properties than ad hoc questions. TAM and UTAUT scales are directly relevant to AI adoption.

---

## What Breaks for Generative AI

**Self-report accuracy for AI use** is questionable. Do people know how much AI helps them? The studies showing perceived productivity gains exceeding actual gains suggest not. Users may not accurately perceive AI's contribution to their work.

**Rapidly changing context** challenges surveys about stable phenomena. AI tools and user skills change quickly; survey results become outdated.

**Comparison baselines** are unclear. "How much does AI help?" compared to what? Users may lack accurate memories of pre-AI productivity.

**Construct definitions** are unstable. What does "AI use" mean in a survey? Occasional queries? Deep integration? The construct itself is poorly defined.

---

## What Can Be Adapted

**Experience sampling** captures experience in real time: brief surveys triggered during AI use, asking about the current experience rather than relying on recall.

**Diary methods** have users record AI use as it happens, improving accuracy over retrospective reports.

**Combined with behavioral data**: Survey responses can be validated against actual usage logs where available. This calibrates how much to trust self-reports.

**Longitudinal surveys** track the same respondents over time, capturing how perceptions and use evolve as AI changes and users learn.

---

## Implications for AI Evaluation

**User surveys are valuable but have known limitations.** They provide information about perceptions and attitudes that other methods can't access.

**Self-reported productivity may not match actual productivity.** Validate survey findings against behavioral measures where possible.

**Consider who responds.** Volunteer samples of AI users may not represent typical users. Report response rates and consider non-response bias.

**Use validated scales where available.** Technology acceptance scales (TAM, UTAUT) provide established measures.

**Combine with other methods.** Surveys provide breadth; combine with qualitative methods for depth and behavioral data for validation.

**Ask about specific behaviors, not just attitudes.** "How often in the past week did you use AI for drafting documents?" is more accurate than "How helpful is AI for your work?"

---

## Key References

- **Groves, R.M., et al. (2009). *Survey Methodology* (2nd ed.).** Comprehensive treatment from leading survey methodologists.

- **Dillman, D.A., Smyth, J.D., & Christian, L.M. (2014). *Internet, Phone, Mail, and Mixed-Mode Surveys* (4th ed.).** Practical guide to survey design and administration.

- **Tourangeau, R., Rips, L.J., & Rasinski, K. (2000). *The Psychology of Survey Response*.** Cognitive processes underlying survey response.

- **Venkatesh, V., et al. (2003). "User Acceptance of Information Technology: Toward a Unified View." *MIS Quarterly*.** UTAUT model and technology acceptance measurement.

- **Davis, F.D. (1989). "Perceived Usefulness, Perceived Ease of Use, and User Acceptance of Information Technology." *MIS Quarterly*.** Original TAM paper.

---

## Connections to Other Sections

Survey methodology connects to several other disciplines covered in this appendix:

- **Section 2.2 (Psychometrics)** provides the measurement theory underlying validated survey scales.

- **Section 2.4 (Qualitative Methods)** offers complementary approaches—qualitative exploration can inform survey development.

- **Section 5.3 (Organizational Behavior)** uses surveys extensively for measuring adoption, attitudes, and organizational factors.

- **Section 5.1 (HCI)** employs usability surveys and satisfaction measures.

- **Section 3.2 (Productivity Measurement)** highlights that self-reported productivity may differ from actual productivity.

---

*[End of Section 2.5]*
