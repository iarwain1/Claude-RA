# Appendix A, Section 5: Human and Organizational Factors

## Section 5.1: Human-Computer Interaction and User Experience Research

### Overview

Human-Computer Interaction (HCI) studies how people interact with computers and technology. The field provides methods for understanding how users actually work with systems—not how designers intend them to work, but how they actually work in practice. For AI evaluation, HCI methods reveal how users experience AI, what strategies they develop, and where friction arises.

### Core Concepts

**Usability**

Usability has multiple dimensions:
- **Effectiveness**: Can users accomplish their goals?
- **Efficiency**: How much effort does it take?
- **Satisfaction**: How do users feel about the experience?
- **Learnability**: How easily can new users become proficient?
- **Error rates**: How often do errors occur? How easily are they recovered?

For AI, usability extends to: Can users effectively prompt AI? Can they recognize and correct AI errors? Is the interaction efficient, or do iteration and error-correction consume time?

**User-Centered Design**

UCD puts users at the center of design:
- Understand users and their contexts
- Involve users throughout design
- Iterate based on user feedback
- Evaluate with actual users

For AI, UCD suggests: understanding how actual workers would use AI (not how designers imagine), involving users in developing AI integration, iterating based on real-world feedback.

**Usability Evaluation Methods**

**Heuristic evaluation**: Experts review against usability principles (visibility of system status, match to real world, user control, consistency, error prevention, etc.)

**Cognitive walkthrough**: Step through tasks from user perspective, asking: Will users know what to do? Will they recognize that correct actions are available? Will they understand feedback?

**Usability testing**: Observe real users attempting realistic tasks. Think-aloud protocols have users verbalize their thoughts while working.

For AI, these methods can be applied: heuristic review of AI interfaces, cognitive walkthroughs of AI-assisted workflows, observation of users working with AI.

**Contextual Inquiry**

Contextual inquiry studies work in its natural context—observing and interviewing workers in their actual work environment:
- Observe actual practice, not idealized procedures
- Interview about work in context
- Build understanding of work structure and meaning

For AI, contextual inquiry reveals how AI integrates (or doesn't) into complex workflows, informal workarounds users develop, and gaps between intended and actual use.

**Task Analysis**

**Hierarchical Task Analysis (HTA)** breaks work into goals, sub-goals, and operations—the structure of what workers do.

**Cognitive Task Analysis (CTA)** examines the cognitive demands of work—what decisions are made, what knowledge is required, what makes tasks difficult.

For AI integration, task analysis identifies: Which tasks might AI support? What cognitive demands might AI reduce? What human judgment must remain?

**Mental Models**

Users develop mental models of how systems work. These may be incomplete or inaccurate, but they guide interaction.

For AI, mental model questions include: Do users understand what AI can and can't do? Do they have accurate models of when AI is reliable? Mismatched mental models lead to misuse.

**Situated Action**

Lucy Suchman's influential work showed that action is always situated in specific contexts. Users don't follow predetermined plans; they improvise with available resources in response to local circumstances.

For AI, this suggests evaluation in realistic contexts, not isolated tasks. How users work with AI in situated practice may differ from how they respond to standardized evaluation tasks.

### What Transfers to AI Evaluation

**Usability methods** can evaluate AI interfaces and interactions.

**Contextual inquiry** reveals real AI use patterns, workarounds, and problems.

**Task analysis** identifies where AI fits in work structure.

**Mental models** highlight user understanding and misunderstanding of AI.

**Situated action** emphasizes evaluation in realistic contexts.

### What Breaks for Generative AI

**Clear task definition**: HCI often assumes defined tasks; AI use is more open-ended.

**Consistent system behavior**: Usability assumes consistent responses; AI varies.

**Error definition**: What counts as an "error" when AI output is probabilistic?

### Implications for AI Evaluation

- **Use HCI methods** to understand how users actually work with AI.
- **Conduct contextual inquiry** in real work settings.
- **Assess mental models**: Do users understand AI capabilities and limits?
- **Recognize situated nature** of AI use.

### Key References

- **Nielsen, J. (1993). *Usability Engineering*.** Classic usability text.

- **Beyer, H., & Holtzblatt, K. (1998). *Contextual Design*.** Comprehensive contextual inquiry methodology.

- **Suchman, L. (1987). *Plans and Situated Actions*.** Foundational work on situated action and technology use.

- **Amershi, S., et al. (2019). "Guidelines for Human-AI Interaction." *CHI*.** AI-specific interaction guidelines.

---

## Section 5.2: Human Factors and Human-Machine Systems

### Overview

Human factors engineering studies how humans interact with systems, emphasizing human capabilities and limitations. For human-AI teaming, this field provides deep expertise on trust, automation, workload, and situation awareness—directly applicable to understanding how people work with AI.

### Core Concepts

**Human Information Processing**

Human cognition has well-documented characteristics and limitations:
- **Attention** is limited and selective
- **Working memory** can hold only a few items
- **Long-term memory** is vast but retrieval is imperfect
- **Decision making** uses heuristics and is subject to biases

AI assistance interacts with these characteristics. AI might reduce cognitive load (good) or add new monitoring demands (bad). AI might support decision making or induce new biases.

**Workload**

Workload refers to mental and physical demands on operators:
- **Underload** can lead to boredom, vigilance failure, skill degradation
- **Overload** can lead to errors, stress, and breakdown
- Assessment methods like NASA-TLX measure perceived workload

AI's effect on workload is not straightforwardly reducing. AI might reduce some task demands while adding monitoring demands. Managing AI output quality is itself work.

**Situation Awareness**

Endsley's model of situation awareness has three levels:
- **Level 1**: Perception of elements in the environment
- **Level 2**: Comprehension of their meaning
- **Level 3**: Projection of future status

Loss of situation awareness is implicated in many accidents. For human-AI teams: Does AI support or undermine situation awareness? If AI handles tasks automatically, does the human lose awareness of what's happening?

**Trust in Automation**

Trust determines whether and how humans use automation:
- **Overtrust (complacency)**: Accepting automation outputs uncritically
- **Undertrust (disuse)**: Not using automation when it would help
- **Calibrated trust**: Matching trust to actual reliability

Trust calibration is difficult when reliability varies across conditions. The jagged capability frontier makes AI trust calibration particularly challenging.

**Automation Surprises**

When automation behaves unexpectedly, humans experience "automation surprises":
- "What's it doing?"
- "Why did it do that?"
- "What will it do next?"

Mode confusion—not knowing what mode the automation is in—contributes to surprises. AI's unpredictable behavior generates frequent surprises.

**Levels of Automation**

Sheridan and Verplank's 10-level scale ranges from fully manual to fully autonomous:
1. Human does everything
2. Computer offers suggestions
3. Computer suggests one alternative
...
10. Computer does everything, ignores human

Different levels have different evaluation needs. Human-in-the-loop systems need human vigilance evaluation. Autonomous systems need comprehensive capability testing.

**Skill Degradation**

When automation handles tasks, human skills for those tasks may atrophy. If automation fails and humans must take over, they may not be able to perform effectively.

For AI, skill degradation concerns ask: If workers rely on AI for tasks, do their underlying skills decline? Can they perform without AI if needed?

### What Transfers to AI Evaluation

**Trust calibration research** directly applies. Are users trusting AI appropriately?

**Automation surprises** occur frequently with AI. Understanding and mitigating them is essential.

**Situation awareness** concepts apply to human-AI teams.

**Workload effects** should be measured, not assumed positive.

**Skill degradation** is a legitimate concern for AI-assisted work.

### What Breaks for Generative AI

**Predictable automation**: Traditional automation is more predictable than AI.

**Defined interfaces**: AI interaction is often conversational, not button-based.

**Stable reliability**: AI reliability varies unpredictably across tasks.

### Implications for AI Evaluation

- **Evaluate the human-AI team**, not just AI capability.
- **Assess trust calibration**: Are users appropriately skeptical or trusting?
- **Monitor for automation surprises** and their effects.
- **Consider workload** effects holistically.
- **Track potential skill effects** over time.

### Key References

- **Parasuraman, R., & Riley, V. (1997). "Humans and Automation: Use, Misuse, Disuse, Abuse." *Human Factors*.** Classic typology of automation use problems.

- **Lee, J.D., & See, K.A. (2004). "Trust in Automation: Designing for Appropriate Reliance." *Human Factors*.** Comprehensive review of automation trust.

- **Endsley, M.R. (2016). *Designing for Situation Awareness* (2nd ed.).** Situation awareness framework and measurement.

---

## Section 5.3: Organizational Behavior and Change Management

### Overview

Organizational behavior studies how organizations function; change management addresses how to navigate organizational transitions. AI adoption is organizational change—it affects roles, processes, skills, and relationships. Understanding organizational factors is essential for interpreting AI evaluation results.

### Core Concepts

**Technology Adoption Models**

**Technology Acceptance Model (TAM)**: Adoption depends on:
- Perceived usefulness: Will this help me?
- Perceived ease of use: Is this hard?

**Diffusion of Innovations**: Adoption follows patterns:
- Innovators adopt first
- Early adopters next
- Early majority
- Late majority
- Laggards

**UTAUT** (Unified Theory of Acceptance and Use of Technology) integrates multiple models, adding social influence, facilitating conditions, and demographics.

For AI, adoption models predict that: perceived usefulness and ease of use drive adoption; adoption won't be uniform; early adopters differ from later adopters.

**Absorptive Capacity**

Organizations differ in ability to recognize, assimilate, and apply new knowledge. High absorptive capacity enables learning from AI; low absorptive capacity limits benefits.

Absorptive capacity depends on:
- Prior relevant knowledge
- Internal communication
- Learning orientation
- Resources for experimentation

Organizations with low absorptive capacity may struggle to benefit from AI regardless of AI capability.

**Organizational Change Models**

**Lewin's model**: Unfreeze → Change → Refreeze. Destabilize current state, implement change, stabilize new state.

**Kotter's 8 steps**: Create urgency, build coalition, form vision, communicate vision, remove obstacles, create wins, build on change, anchor in culture.

These models highlight that technology deployment is organizational change requiring deliberate management.

**Resistance to Change**

Resistance arises from:
- Uncertainty about the future
- Loss of control or competence
- Perceived threats to status or security
- Poor communication or involvement

Resistance isn't irrational—it often reflects legitimate concerns about poorly planned change. Distinguishing legitimate concerns from resistance per se is important.

**Implementation Research**

Why do implementations succeed or fail?
- **Implementation fidelity**: Was the intervention delivered as intended?
- **Contextual factors**: Organizational readiness, leadership support, resources
- **Adaptation**: How was the intervention adapted to local context?

AI implementation success depends on more than AI capability—organizational factors determine whether capable AI delivers benefits.

### What Transfers to AI Evaluation

**Adoption models** help predict and interpret adoption patterns.

**Absorptive capacity** explains organizational differences in AI benefits.

**Change management** frames AI deployment as organizational change requiring active management.

**Implementation research** highlights organizational factors affecting outcomes.

### What Breaks for Generative AI

**Slower change context**: Traditional change models assumed slower change than AI brings.

**Clearer technology**: AI is more ambiguous than technologies change models were developed for.

### Implications for AI Evaluation

- **Evaluation results depend on organizational context.** Same AI may perform differently in different organizations.
- **Failed pilots may reflect change management**, not AI limitations.
- **Assess organizational readiness** before expecting benefits.
- **Support ongoing organizational learning** about AI.

### Key References

- **Rogers, E.M. (2003). *Diffusion of Innovations* (5th ed.).** Classic adoption theory.

- **Venkatesh, V., et al. (2003). "User Acceptance of Information Technology: Toward a Unified View." *MIS Quarterly*.** UTAUT model.

- **Kotter, J.P. (2012). *Leading Change*.** Change management framework.

---

## Section 5.4: Judgment and Decision Making (JDM)

### Overview

JDM research studies how people make judgments and decisions, including systematic biases. This research is directly relevant to understanding how humans use (and misuse) AI advice—and how human evaluators of AI may be biased in their assessments.

### Core Concepts

**Heuristics and Biases**

Humans use cognitive shortcuts (heuristics) that usually work but can lead to systematic errors:

**Availability**: Judging likelihood by how easily examples come to mind. Dramatic AI successes may be more available than routine failures.

**Anchoring**: Estimates influenced by initial values. AI suggestions may anchor human judgment even when suggestions are wrong.

**Representativeness**: Judging probability by similarity to stereotypes. An AI output that "sounds right" may be accepted even if it's wrong.

**Confirmation bias**: Seeking and interpreting information to confirm existing beliefs. Users who believe AI helps may notice confirming cases.

**Algorithm Aversion**

People often resist algorithmic recommendations even when algorithms outperform humans:
- Seeing an algorithm err reduces trust more than seeing a human err
- People want control and understanding
- Perfect algorithms are less trusted than imperfect humans

For AI, algorithm aversion may cause underuse of helpful AI.

**Algorithm Appreciation**

The flip side: over-reliance on algorithmic advice:
- **Automation bias**: Accepting AI recommendations uncritically
- **Diffusion of responsibility**: AI suggested it, so user feels less responsible
- Particularly strong when AI is perceived as authoritative

For AI, algorithm appreciation may cause overuse and uncritical acceptance.

**Advice Taking**

Research on judge-advisor systems shows:
- People typically discount advice (weight it less than 50%)
- Discounting depends on perceived advisor expertise, confidence, and relationship to own beliefs
- AI as advisor: Do users discount AI advice appropriately?

**Calibration**

Calibration is match between confidence and accuracy:
- Overconfidence: People are often more confident than accuracy warrants
- Poor calibration leads to bad decisions

For AI users, calibration asks: Do users know when to trust AI? Are they appropriately confident in AI-assisted outputs?

**Noise**

Noise is variability in judgments that should be identical:
- Different judges give different ratings to the same case
- Same judge gives different ratings at different times

Human evaluation of AI outputs is noisy. This noise contributes to measurement error in AI evaluation.

### What Transfers to AI Evaluation

**Bias awareness**: Both AI users and AI evaluators are subject to cognitive biases.

**Algorithm aversion/appreciation**: Affects AI adoption and use patterns.

**Calibration**: Do users know when to trust AI?

**Noise**: Human evaluation is inherently variable.

### Implications for AI Evaluation

- **Design evaluation to reduce bias** (structure, blinding where possible).
- **Evaluate for appropriate AI reliance**, not just AI use.
- **Quantify and account for noise** in human evaluation.
- **Consider training** for calibrated AI use.

### Key References

- **Kahneman, D. (2011). *Thinking, Fast and Slow*.** Accessible introduction to heuristics and biases.

- **Kahneman, D., Sibony, O., & Sunstein, C.R. (2021). *Noise*.** Systematic treatment of judgment variability.

- **Dietvorst, B.J., Simmons, J.P., & Massey, C. (2015). "Algorithm Aversion." *Journal of Experimental Psychology: General*.** Algorithm aversion research.

---

## Section 5.5: Industrial-Organizational (I-O) Psychology

### Overview

I-O psychology applies psychological principles to workplace settings. It provides frameworks for personnel selection, performance appraisal, and training that inform the "evaluate AI like hiring an employee" metaphor central to practical AI evaluation.

### Core Concepts

**Job Analysis**

Job analysis systematically studies job requirements:
- **Tasks**: What activities comprise the job?
- **KSAOs**: What Knowledge, Skills, Abilities, and Other characteristics are needed?

For AI, job analysis asks: What tasks should AI perform? What capabilities are required? This parallels defining what AI should do before evaluating whether it can.

**Personnel Selection**

Selection research identifies predictors of job performance:
- General cognitive ability is a strong predictor across jobs
- Specific abilities matter for specific jobs
- Work samples predict performance better than general tests

For AI, selection thinking suggests: evaluate AI on tasks representative of actual use (work samples), not just general benchmarks.

**Validity Generalization**

Does selection test validity generalize across contexts?

Meta-analytic evidence shows some generalization (cognitive ability predicts performance broadly) and some context-dependence (specific skills matter for specific jobs).

For AI, validity generalization asks: Does benchmark performance generalize across contexts? Evidence suggests limited generalization—the benchmark-to-real gap.

**The Criterion Problem**

What is "good performance"? The criterion problem recognizes this isn't obvious:
- **Ultimate criterion**: Theoretical ideal performance
- **Actual criterion**: What we can actually measure
- **Criterion deficiency**: What's missing from our measure
- **Criterion contamination**: What's measured that shouldn't be

For AI, the criterion problem is central. "Good AI output" isn't well-defined. Benchmarks may be criterion-deficient (missing important aspects) or contaminated (measuring irrelevant factors).

**Structured vs. Unstructured Assessment**

Research consistently shows structured assessment outperforms unstructured:
- Structured interviews beat unstructured interviews
- Rating scales with behavioral anchors beat global ratings
- Structure reduces noise and bias

For AI evaluation, structure improves assessment quality. Structured rubrics, defined criteria, and systematic procedures beat unstructured "vibes."

**Performance Appraisal**

Performance appraisal methods include:
- Rating scales (behaviorally anchored or otherwise)
- Multi-source feedback (360-degree)
- Ranking and forced distribution

Appraisal biases include: halo effect (one positive aspect inflates all ratings), leniency (reluctance to rate poorly), recency (recent events weighted heavily).

For AI output evaluation, these biases apply. Structured evaluation with clear criteria reduces bias.

**Training Evaluation**

Kirkpatrick's four levels:
1. **Reaction**: Did participants like the training?
2. **Learning**: Did participants learn the content?
3. **Behavior**: Did participants change behavior on the job?
4. **Results**: Did the organization see results?

For AI user training, Kirkpatrick's model applies: Do users like AI training? Do they learn effective AI use? Do they use AI differently? Do outcomes improve?

### What Transfers to AI Evaluation

**Job analysis**: Define what AI should do before evaluating.

**Work sample testing**: Evaluate on realistic tasks, not just benchmarks.

**The criterion problem**: Recognize difficulty defining "good" AI output.

**Structured evaluation**: Use structure to reduce noise and bias.

**Training evaluation**: Apply Kirkpatrick to AI training programs.

### What Breaks for Generative AI

**Human-centric frameworks**: I-O psychology is about humans; AI is different.

**Stable traits**: I-O psychology assumes relatively stable individual differences.

### Implications for AI Evaluation

- **Apply job analysis thinking**: What should AI do? What capabilities are needed?
- **Use work sample evaluation**: Test on realistic tasks.
- **Apply structured evaluation**: Reduce noise and bias through structure.
- **Recognize the criterion problem**: Defining good output is hard.

### Key References

- **Schmidt, F.L., & Hunter, J.E. (1998). "The Validity and Utility of Selection Methods in Personnel Psychology." *Psychological Bulletin*.** Meta-analysis of selection methods.

- **Campion, M.A., Palmer, D.K., & Campion, J.E. (1997). "A Review of Structure in the Selection Interview." *Personnel Psychology*.** Structure in assessment.

- **Kirkpatrick, J.D., & Kirkpatrick, W.K. (2016). *Kirkpatrick's Four Levels of Training Evaluation*.** Training evaluation framework.

---

*[End of Section 5]*
