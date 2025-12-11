# Appendix A, Section 8.4: What's Genuinely New

## Overview

Some AI evaluation challenges don't have good precedents from existing disciplines. These genuinely novel challenges require new approaches rather than adaptation of existing methods.

This section identifies the truly unprecedented aspects of AI evaluation—where existing disciplines provide limited guidance.

---

## Novel Challenges

### 1. Unbounded Output Evaluation

**The challenge**: No prior field has evaluated systems that produce outputs from an essentially unlimited space.

- Classification has k classes
- Regression has one number
- Traditional software has specified output formats
- Language models produce arbitrary text

The entire machinery of enumerable-output evaluation (confusion matrices, classification metrics, output verification) doesn't apply. There's no prior art for systematically evaluating unbounded generative output.

**Why it's novel**: Human creative work produces unbounded outputs, but we don't evaluate human creativity systematically at scale. We have literary criticism, not literary measurement. AI evaluation requires measurement of unbounded output, not just appreciation.

**What's needed**: New frameworks for:
- Sampling strategies for unbounded output spaces
- Quality dimensions for open-ended text
- Aggregation methods for heterogeneous outputs
- Scalable evaluation that doesn't require human review of everything

### 2. The Jagged Capability Frontier

**The challenge**: The pattern of high capability immediately adjacent to surprising failure is unprecedented.

Traditional systems have understood capability boundaries—they work within specification and don't work outside it. You know where the edge is.

AI exhibits high capability on some instances while failing on nearly identical instances. The capability boundary is fractal, unpredictable, and varies across tasks. "Jaggedness" means you can't know where failures will occur.

**Why it's novel**: No prior system has had such unpredictable capability boundaries. Physical systems degrade gracefully. Software fails at predictable limits. AI fails surprisingly.

**What's needed**: New frameworks for:
- Dense capability sampling
- Boundary detection and characterization
- Communicating jagged reliability to users
- Decision-making under jagged uncertainty

### 3. The Specification Depth Problem

**The challenge**: Much of AI's value lies in handling tasks that couldn't be specified precisely enough to automate traditionally.

But if we could specify the task precisely, we could automate it without AI. This creates a fundamental tension: the tasks where AI is most valuable are the tasks hardest to specify—and therefore hardest to evaluate.

**Why it's novel**: Traditional automation required precise specification before automation. AI reverses this: it automates tasks we can't specify. But we need specifications to evaluate.

**What's needed**: New frameworks for:
- Evaluating performance on underspecified tasks
- Quality assessment without clear criteria
- "I know it when I see it" made systematic
- Managing the tension between specification and value

### 4. Benchmark Contamination Via Training

**The challenge**: Traditional test security prevents examinees from seeing test items in advance. AI training may include benchmark items in training corpora—not through intentional cheating but through internet-scale data collection.

This "data contamination" inflates benchmark performance in ways that don't reflect true capability. It creates a novel threat to evaluation validity that doesn't have direct precedent.

**Why it's novel**: Traditional test security assumes examinees are separate from test development. AI training consumes the internet, which contains benchmarks. The contamination mechanism is structural, not adversarial.

**What's needed**: New frameworks for:
- Contamination detection
- Contamination-resistant benchmark design
- Decontamination methods
- Alternative capability assessment

### 5. Continuous Evolution During Deployment

**The challenge**: Most evaluation paradigms assume a stable system: test it, then deploy it.

AI systems may change continuously—through model updates, fine-tuning, or prompt engineering—without clear version boundaries. The entity evaluated may differ from the entity deployed, and the entity deployed today may differ from the entity deployed tomorrow.

**Why it's novel**: Traditional systems have versioning. You test version 1.0, deploy version 1.0. AI may change without clear version boundaries, sometimes without user knowledge.

**What's needed**: New frameworks for:
- Continuous evaluation during deployment
- Change detection and characterization
- Validity decay models
- Version-independent capability assessment

### 6. Skill Amplification

**The challenge**: The same AI system produces dramatically different outcomes for different users. A novice may barely use AI capability; an expert may achieve remarkable results.

This "skill amplification" means system capability is entangled with user skill in ways that complicate evaluation. Traditional automation provides more uniform augmentation.

**Why it's novel**: Traditional tools have more consistent effects. A calculator produces the same answer regardless of user skill. AI effectiveness varies enormously with prompting skill, domain knowledge, and verification capability.

**What's needed**: New frameworks for:
- User-conditional capability assessment
- Skill-capability interaction measurement
- Equitable evaluation across skill levels
- Separating system capability from user skill

### 7. The "Vibes" Quality Problem

**The challenge**: For many AI tasks, experts recognize quality when they see it but struggle to articulate criteria precisely enough for reliable measurement.

This isn't unique to AI, but the breadth of AI applications (writing, coding, analysis, conversation) across so many quality dimensions makes it particularly acute. How do you systematically evaluate something when "you know it when you see it" is the best quality criterion available?

**Why it's novel**: "Vibes" have always mattered for creative work, but AI requires measurement at scale. You can't have experts review every output. The gap between recognition and articulation is a measurement problem.

**What's needed**: New frameworks for:
- Articulating implicit quality criteria
- Converting "vibes" to rubrics
- Scalable quality assessment
- Expert disagreement handling

---

## Approaches Being Developed

The field is actively working on these challenges. Emerging approaches include:

**For unbounded output**: Multi-dimensional rubrics, comparative evaluation (A vs. B rather than absolute scoring), hierarchical evaluation

**For jagged frontier**: Dense capability sampling, failure boundary characterization, uncertainty quantification

**For specification depth**: Human-in-the-loop evaluation, preference learning, task decomposition

**For contamination**: Held-out benchmarks, novel task generation, contamination detection methods

**For continuous evolution**: Continuous monitoring infrastructure, drift detection, rolling evaluation

**For skill amplification**: User stratification, controlled user studies, skill-normalized evaluation

**For vibes**: Structured rubric development, calibrated human evaluation, LLM-assisted evaluation

---

## Implications

These novel challenges mean:
- Can't simply apply existing methods
- Must develop new approaches
- Should expect immaturity and evolution
- Need tolerance for uncertainty
- Should combine multiple imperfect approaches

---

*[End of Section 8.4]*
