# Cross-Disciplinary Background: Measuring Productivity Gains From Generative AI

---

## Purpose and How to Use This Document

This document surveys the disciplines and fields that inform AI evaluation, organized to help readers:

1. **Connect to existing expertise**: Readers with backgrounds in specific fields can see how their knowledge applies (and where it breaks down)
2. **Find entry points**: Readers unfamiliar with a field can understand its core contributions and access key literature
3. **Understand what's new**: By systematically examining what transfers and what doesn't, we can identify what's genuinely novel about AI evaluation

### Structure for Each Discipline

- Overview: What the field is and what it studies
- Core concepts: Key ideas and methods relevant to AI evaluation
- What transfers: Approaches that apply directly
- What breaks: Where the field's assumptions don't hold for GenAI
- What can be adapted: Approaches that work with modification
- Implications for AI evaluation: Practical takeaways
- Key references: Entry points to the literature
- Connections: Links to other disciplines in this document

### Reading Suggestions

| If you have background in... | Start with... | Then explore... |
|------------------------------|---------------|-----------------|
| T&E / Defense acquisition | Sections 1, 4, 6 | Section 2 (experimental rigor) |
| Research / Statistics | Sections 2, 6 | Section 7.1 (metrology) |
| Management / Acquisition | Sections 3, 4.4, 7 | Section 5.3 (organizational factors) |
| Human factors | Section 5 | Section 1.3 (autonomous systems) |
| AI Safety | Sections 6.1, 4.5, 1.5 | All sections (this work bridges fields) |

---

## Table of Contents

**Section 1: Testing and Evaluation Traditions**
- 1.1 Software Testing and Quality Assurance
- 1.2 Systems Engineering and Hardware T&E
- 1.3 Autonomous Systems Testing and Evaluation
- 1.4 Traditional Machine Learning Evaluation
- 1.5 Cybersecurity Testing and Red Teaming

**Section 2: Experimental and Statistical Methods**
- 2.1 Experimental Design and Analysis
- 2.2 Psychometrics and Measurement Theory
- 2.3 Econometrics and Causal Inference
- 2.4 Qualitative Research Methods
- 2.5 Survey Methodology

**Section 3: Economics and Productivity**
- 3.1 Information Systems Economics
- 3.2 Productivity Measurement and Economics
- 3.3 Cost Analysis and Investment Evaluation

**Section 4: Risk, Quality, and Assurance**
- 4.1 Risk Analysis and Management
- 4.2 Reliability Engineering
- 4.3 Quality Management
- 4.4 Audit and Assurance
- 4.5 Safety Engineering

**Section 5: Human and Organizational Factors**
- 5.1 Human-Computer Interaction and UX Research
- 5.2 Human Factors and Human-Machine Systems
- 5.3 Organizational Behavior and Change Management
- 5.4 Judgment and Decision Making
- 5.5 Industrial-Organizational Psychology

**Section 6: Evaluation and Assessment Traditions**
- 6.1 AI Safety Evaluation (Emerging)
- 6.2 Program Evaluation
- 6.3 Educational Measurement
- 6.4 Clinical Trial Methodology

**Section 7: Standards and Governance**
- 7.1 Metrology (Science of Measurement)
- 7.2 Standards Development and Governance

**Section 8: Synthesis and Crosswalks**
- 8.1 What Transfers Directly
- 8.2 What Breaks for Generative AI
- 8.3 What Requires Adaptation
- 8.4 What's Genuinely New
- 8.5 Terminology Crosswalk
- 8.6 Synthesis: What AI Evaluation Requires
- 8.7 Reader Guide

---

# Section 1: Testing and Evaluation Traditions

## 1.1 Software Testing and Quality Assurance

### Overview

Software testing is the systematic practice of evaluating software to identify defects, verify that requirements are met, and validate that the system serves its intended purpose. Over decades of practice, the field has developed sophisticated methods for ensuring software quality—methods that offer both direct lessons and cautionary tales for AI evaluation.

The fundamental challenge of software testing is achieving confidence in system behavior despite the impossibility of exhaustive testing. Even simple programs have more possible inputs than could be tested in the lifetime of the universe. Testing therefore relies on strategic sampling, systematic coverage, and careful reasoning about what untested behaviors can be inferred from tested ones. This challenge is familiar to anyone evaluating AI systems, though as we shall see, it manifests in importantly different ways.

This section surveys key concepts from software testing, examines which approaches transfer to AI evaluation, identifies where foundational assumptions break down, and considers what adaptations might bridge the gap.

---

### Core Concepts

#### Verification and Validation

Perhaps the most important conceptual distinction in software testing is between verification and validation, often summarized as:

- **Verification**: "Are we building it right?" Does the implementation correctly match the specification?
- **Validation**: "Are we building the right thing?" Does the system actually meet user needs?

This distinction illuminates a critical point: a system can pass all verification tests while still failing validation. Software that perfectly implements the wrong requirements, or that meets requirements in ways that don't serve users, is verified but not validated.

The verification/validation distinction maps directly onto a central problem in AI evaluation. Benchmarks and automated tests are primarily verification activities—they check whether the AI performs correctly on specified tasks with defined success criteria. But the harder question is validation: Does strong benchmark performance translate to real-world utility? A model that achieves state-of-the-art scores on coding benchmarks (verification) may still fail to help actual developers in their daily work (validation). The benchmark-utility gap is, at its core, a verification-validation gap.

#### Test Coverage

Software testing has developed various metrics to assess how thoroughly a test suite exercises the code under test:

- **Statement coverage**: Has every line of code been executed at least once?
- **Branch coverage**: Has every decision point (if/else, switch) been evaluated both ways?
- **Path coverage**: Has every possible execution path through the code been tested?
- **Condition coverage**: Has every Boolean sub-expression been evaluated to both true and false?

These metrics serve as proxies for test adequacy. The intuition is straightforward: code that has never been executed during testing may contain undetected bugs. Higher coverage generally correlates with greater confidence, though coverage is not sufficient—a test can execute a line of code without actually checking whether it behaves correctly.

The concept of coverage raises immediate questions for AI evaluation. What would it mean to "cover" the capabilities of a language model? There is no finite set of code paths to enumerate. The input space—all possible prompts—is effectively infinite. And even if we could enumerate all possible inputs, we would face the problem of defining what "correct" behavior looks like for each one.

Yet the underlying logic of coverage remains valuable: we should seek to exercise the system across diverse conditions, and we should be concerned about regions of the capability space that our evaluation has not explored. The jagged capability frontier—where AI systems exhibit inexplicable failures on tasks similar to ones they handle well—is precisely the kind of gap that coverage-oriented thinking is designed to catch.

#### Test Oracles

A test oracle is any mechanism for determining whether a test has passed or failed. For some tests, oracles are straightforward: if a function should return 42, check whether it returns 42. For others, oracles are complex: does this image look "realistic"? Is this user interface "intuitive"?

The oracle problem—determining what correct behavior looks like—is one of the deepest challenges in software testing. When specifications are incomplete, ambiguous, or nonexistent, there may be no principled way to judge whether output is correct. Software testers have developed various approaches to this problem:

- **Specification-based oracles**: Compare output to formal specifications
- **Reference implementations**: Compare to a trusted alternative system
- **Metamorphic testing**: Check relationships between outputs (if input doubles, does output double?)
- **Human judgment**: Have experts evaluate outputs (expensive, doesn't scale)

AI evaluation faces the oracle problem in its most severe form. For many AI tasks—writing assistance, coding help, open-ended question answering—there is no single correct output. Multiple responses could be equally good, or good in different ways. The "vibes" problem that practitioners report (they know good output when they see it, but struggle to articulate criteria) is an oracle problem. Much of the difficulty in AI evaluation stems not from inability to run tests, but from inability to judge the results.

#### Regression Testing

Regression testing is the practice of re-running tests after system changes to ensure that previously working functionality still works. The name comes from the goal of detecting "regressions"—cases where changes inadvertently break existing behavior.

Regression testing assumes several things that often hold for traditional software:

1. The system is deterministic (same input produces same output)
2. Tests can be re-run exactly
3. The definition of "correct" behavior remains stable
4. You can detect whether output has changed

For AI systems, these assumptions often fail. Language models are stochastic—the same prompt may produce different outputs on each run. Model providers update their systems continuously, sometimes without notification. The "correct" output may be context-dependent in ways that change over time. And for generative outputs, determining whether behavior has meaningfully changed (as opposed to just varied within acceptable bounds) is itself a difficult judgment.

Despite these complications, the regression mindset remains valuable. Organizations deploying AI systems should monitor for performance changes over time, even if exact reproducibility is impossible. The goal shifts from "did this specific output change?" to "has the distribution of outputs shifted in concerning ways?"

#### Boundary Testing and Edge Cases

Testing at boundaries—the edges of valid input ranges, transitions between states, limits of system capacity—tends to reveal defects more efficiently than testing in the middle of normal operating ranges. A function that correctly handles values from 1 to 99 may still fail on 0, 100, or negative numbers.

Boundary testing relies on the principle of equivalence partitioning: inputs can be grouped into classes that are likely to be treated similarly by the system. Test one representative from each class, plus the boundaries between classes. This strategy makes the infinite input space tractable.

For AI systems, boundaries are harder to identify and less predictable. The jagged capability frontier means that failures don't cluster neatly at definable boundaries. A model might handle complex legal questions well but stumble on simple arithmetic—not because arithmetic is at a "boundary" in any meaningful sense, but because of idiosyncratic patterns in training data or model architecture. Still, boundary thinking has value: testing should deliberately probe the edges of claimed capabilities, transitions between task types, and limits of context length or complexity.

#### Fault Injection and Mutation Testing

Rather than only testing whether software works correctly, some approaches deliberately introduce faults to verify that tests can detect them:

- **Fault injection**: Introduce errors (corrupted data, network failures, resource exhaustion) to verify the system handles them gracefully
- **Mutation testing**: Make small changes to the code ("mutations") and verify that tests fail—if tests pass despite a mutation, they may not be checking the right things

These approaches test the tests themselves. A test suite that passes both on correct code and on mutated code is not providing meaningful assurance.

The analog for AI evaluation is adversarial testing and red teaming. Rather than only asking whether the AI performs well on standard inputs, we deliberately probe for failures: edge cases, adversarial prompts, attempts to elicit harmful or incorrect outputs. This adversarial orientation—actively trying to make the system fail—provides different information than cooperative testing and is essential for understanding actual system robustness.

---

### What Transfers to AI Evaluation

Several concepts from software testing apply directly to AI evaluation, requiring little or no adaptation:

**The verification/validation distinction** is perhaps the most valuable conceptual transfer. Recognizing that benchmark performance (verification) is not the same as real-world utility (validation) immediately clarifies why impressive benchmarks don't guarantee impressive deployments. Every AI evaluation effort should be clear about whether it's primarily verification or validation—and should recognize that verification alone is insufficient for acquisition decisions.

**Test planning discipline** transfers well. Software testing emphasizes systematic planning: identifying what needs to be tested, why, with what methods, and to what criteria. This discipline of explicit planning—rather than ad hoc testing—is equally important for AI evaluation. A Test and Evaluation Master Plan (TEMP) for an AI system might look different in its details from one for traditional software, but the underlying discipline of comprehensive planning applies.

**Coverage thinking**, while requiring adaptation, provides a valuable orientation. Even though we cannot enumerate all possible AI inputs or achieve measurable coverage in the software testing sense, we can and should think carefully about whether our evaluation has exercised the system across diverse conditions. Are we testing across different task types, difficulty levels, user populations, and deployment contexts? Where are the gaps in our evaluation coverage, and what risks do those gaps create?

**The regression mindset**—tracking performance over time and watching for degradation—is directly applicable, even though the specific techniques of regression testing may not work. AI systems should be monitored continuously, with mechanisms to detect when performance characteristics shift.

**The adversarial orientation** of mutation testing and fault injection translates naturally to AI red teaming. The goal of actively trying to break the system, rather than just confirming it works in expected cases, provides essential information about robustness and failure modes.

---

### What Breaks for Generative AI

Other foundational assumptions of software testing do not hold for generative AI systems, limiting the direct applicability of traditional approaches:

**Determinism** is perhaps the most fundamental break. Software testing assumes that the same input produces the same output. Tests are run, results are recorded, and any deviation indicates a problem. Generative AI is inherently stochastic—the same prompt will produce different outputs across runs, sometimes subtly different, sometimes substantially so. This breaks the basic logic of most testing approaches. You cannot simply check whether output equals expected output when there is no single expected output.

This stochasticity has cascading implications. Test results are not fully reproducible. Performance comparisons between models (or between versions of the same model) must account for output variance. Evaluation requires multiple samples, not single instances, and must characterize distributions rather than point values.

**Enumerable input/output spaces** are assumed in coverage metrics and equivalence partitioning. Software has a finite (if enormous) set of possible inputs, and techniques exist to systematically sample this space. Generative AI operates over effectively infinite input spaces (all possible text prompts) and infinite output spaces (all possible text responses). There is no way to enumerate what the system might be asked or what it might produce.

**Clear oracles** exist for much software testing. Requirements specify expected behavior; outputs can be checked against specifications. For generative AI, outputs are often open-ended with no single correct answer. "Write a poem about autumn" has countless acceptable responses and no way to specify them all in advance. The oracle problem, which is a challenge in some software domains, is pervasive for generative AI.

**Fault isolation** is possible in traditional software debugging. When a test fails, developers can trace through code to identify the defect. AI systems are largely opaque—when outputs are wrong, there is no straightforward way to identify which model components or training data are responsible. This opacity limits our ability to learn from test failures and predict future failures.

**Stable systems** are assumed throughout software testing methodology. The system under test is fixed during the testing process; if it changes, tests must be re-run. AI systems, particularly those accessed through APIs, may be updated by providers at any time, often without notification. A test suite run today may produce different results tomorrow not because of stochasticity but because the underlying model changed. The boundary between stochastic variation and system change is blurred.

---

### What Can Be Adapted

Between concepts that transfer directly and those that break entirely, there is productive middle ground: approaches that can be adapted for AI evaluation with appropriate modifications.

**Metamorphic testing** offers a promising adaptation. Rather than specifying exact expected outputs (which is impossible for generative AI), metamorphic testing specifies relationships between inputs and outputs. If a translation system translates English to French, translating the French back to English should recover something close to the original. If an AI can answer a question, it should give consistent answers to paraphrased versions of the same question. These metamorphic relations can be tested even without knowing the "correct" output for any given input.

Research has explored metamorphic testing for AI systems, testing properties like consistency (similar inputs should produce similar outputs), sensitivity (changing key information should change the answer), and robustness (irrelevant changes shouldn't affect outputs). This approach adapts the logic of testing—checking whether the system behaves correctly—to contexts where "correct" cannot be specified directly.

**Differential testing** compares outputs across systems or versions rather than comparing outputs to specifications. If two language models produce substantially different outputs for the same prompt, at least one may be wrong—even if we can't specify which without further investigation. Differential testing can detect regressions (this version behaves differently than the last), identify outliers (this model's response differs from all others), and highlight areas of uncertainty (models disagree, suggesting difficulty).

**Property-based testing** specifies properties that outputs should satisfy rather than specific expected outputs. Instead of "this input should produce this output," property-based testing says "all outputs should satisfy these constraints." For AI, properties might include: responses should not contain harmful content; code outputs should be syntactically valid; factual claims should be consistent with provided context. These properties can be checked even when the specific output cannot be predicted.

**Statistical approaches** to regression testing can accommodate stochasticity. Rather than checking whether output exactly matches the previous output, statistical regression testing asks whether the distribution of outputs has shifted significantly. This requires multiple samples and statistical methods, but preserves the goal of detecting performance changes over time.

---

### Implications for AI Evaluation

Drawing on the lessons of software testing, several principles emerge for AI evaluation practice:

**Borrow the discipline, adapt the specifics.** Software testing's greatest contribution may be its disciplined, systematic approach to quality assurance. Test planning, coverage analysis, regression monitoring, adversarial probing—these orientations are valuable regardless of specific techniques. AI evaluation should adopt this disciplined mindset while adapting methods for AI's distinctive properties.

**Accept that testing cannot be exhaustive.** Software testers have long understood that complete testing is impossible; the goal is justified confidence, not certainty. For AI, this is even more true. No evaluation can guarantee AI performance in all contexts. The goal is reducing risk and characterizing residual uncertainty, not eliminating it.

**Focus on risk-based prioritization.** Because exhaustive testing is impossible, software testing prioritizes based on risk: what failures are most likely, and what failures would be most costly? AI evaluation should follow the same logic. Where are the greatest risks of AI failure? What failures would be most consequential? Evaluation resources should concentrate there.

**Build monitoring, not just testing.** Traditional software testing focuses heavily on pre-release testing—verify before shipping. For AI systems that change continuously and behave stochastically, pre-deployment testing is necessary but not sufficient. Continuous monitoring in production becomes essential. The line between testing and operations blurs.

**Treat the oracle problem as central.** Software testing has developed workarounds for the oracle problem—specification-based testing, reference implementations, metamorphic relations. AI evaluation should explicitly address how outputs will be judged. When human judgment is required, evaluation design must account for the cost, time, and variability of human evaluation. Developing better oracles—better ways of specifying and checking what "good" looks like—is one of the most important challenges in AI evaluation.

**Learn from adversarial testing.** Mutation testing and fault injection taught software testers that actively trying to break systems reveals different information than confirming they work. Red teaming and adversarial probing should be integral to AI evaluation, not an afterthought. If you only test whether AI performs well on expected inputs, you will be surprised by performance on unexpected ones.

---

### Key References

For readers seeking deeper engagement with software testing concepts:

- **Beizer, B. (1990). *Software Testing Techniques* (2nd ed.).** A comprehensive treatment of testing methods, including boundary testing and equivalence partitioning.

- **Myers, G.J., Sandler, C., & Badgett, T. (2011). *The Art of Software Testing* (3rd ed.).** Accessible introduction to testing principles and practices.

- **Ammann, P., & Offutt, J. (2016). *Introduction to Software Testing* (2nd ed.).** Modern textbook covering coverage criteria, mutation testing, and test design.

- **IEEE 829 Standard for Software and System Test Documentation.** Industry standard for test planning and documentation.

- **Segura, S., Fraser, G., Sanchez, A.B., & Ruiz-Cortés, A. (2016). "A Survey on Metamorphic Testing." *IEEE Transactions on Software Engineering*.** Comprehensive review of metamorphic testing, particularly relevant for AI adaptation.

- **Chen, T.Y., Cheung, S.C., & Yiu, S.M. (2020). "Metamorphic Testing: A New Approach for Generating Next Test Cases." *Technical Report HKUST-CS98-01*.** Foundational paper on metamorphic testing.

- **Barr, E.T., Harman, M., McMinn, P., Shahbaz, M., & Yoo, S. (2015). "The Oracle Problem in Software Testing: A Survey." *IEEE Transactions on Software Engineering*.** Survey of approaches to the oracle problem.

For AI-specific adaptations:

- **Ribeiro, M.T., Wu, T., Guestrin, C., & Singh, S. (2020). "Beyond Accuracy: Behavioral Testing of NLP Models with CheckList." *ACL 2020*.** Applies software testing concepts to NLP model evaluation.

- **Segal, M., & Katz, G. (2021). "Testing Deep Neural Networks." *Foundations and Trends in Machine Learning*.** Survey of testing approaches for neural networks.

---

### Connections to Other Sections

Software testing provides a foundation that connects to several other disciplines covered in this document:

- **Section 1.2 (Systems Engineering and Hardware T&E)** extends testing to integrated systems and introduces the DT/OT paradigm that parallels verification/validation.

- **Section 1.4 (Traditional ML Evaluation)** adapts testing concepts for statistical learning systems, bridging toward generative AI.

- **Section 1.5 (Cybersecurity Testing)** develops the adversarial orientation introduced in mutation testing into comprehensive red teaming.

- **Section 2.1 (Experimental Design)** provides statistical frameworks for handling the variability that breaks deterministic testing assumptions.

- **Section 4.2 (Reliability Engineering)** extends the concern with system correctness to system reliability over time.

---


## Overview

The testing and evaluation of complex defense systems—aircraft, ships, missiles, radars, and integrated command-and-control networks—represents one of the most mature and institutionalized approaches to assessing whether a system will perform as needed in operational conditions. Developed over decades of hard-won experience, often learned through costly failures, military T&E has evolved sophisticated frameworks for moving from laboratory demonstrations to operational confidence.

For readers from the defense acquisition community, much of this section will be familiar territory. The goal here is not to teach T&E fundamentals, but to make explicit how these established concepts apply—and sometimes fail to apply—to the evaluation of AI systems. For readers from other backgrounds, this section provides essential context for understanding the institutional environment in which defense AI acquisition occurs.

The central insight of military T&E is that demonstrating a capability in controlled conditions is not the same as demonstrating it will work in combat. The history of defense acquisition is replete with systems that performed impressively in developmental testing only to reveal critical shortcomings when exposed to realistic operational conditions. This hard-won wisdom applies with full force to AI systems—and perhaps with even greater force, given AI's distinctive properties.

---

## Core Concepts

### Developmental Testing and Operational Testing

The distinction between developmental testing (DT) and operational testing (OT) is foundational to military T&E:

**Developmental Testing** occurs during system development and is conducted primarily by the developer or program office. Its purpose is to support engineering decisions, verify that the system meets specifications, identify deficiencies early enough to correct them, and reduce technical risk. DT typically occurs in controlled environments—laboratories, test ranges, simulation facilities—where conditions can be manipulated to isolate specific capabilities.

**Operational Testing** occurs later in the acquisition process and is conducted by organizations independent of the developer. Its purpose is to assess whether the system is effective and suitable for use by typical operators in realistic operational conditions. OT deliberately introduces the messiness of real-world use: representative users rather than experts, operational environments rather than laboratories, realistic scenarios rather than controlled demonstrations.

The DT→OT progression embodies a crucial insight: performance in controlled conditions does not guarantee performance in the field. A weapon system might achieve impressive accuracy on a test range with experienced engineers operating it in clear weather against cooperative targets. Whether it achieves acceptable accuracy when operated by recently trained soldiers in adverse weather against adversaries actively trying to defeat it is a different question—one that only operational testing can answer.

This progression maps directly onto AI evaluation. Benchmarks and laboratory studies are developmental testing—they verify capabilities under controlled conditions with well-defined tasks. They are necessary and valuable, but they are not sufficient. Operational testing for AI means evaluation with representative users, realistic tasks, genuine workflows, and the full complexity of deployment conditions. The benchmark-utility gap exists precisely because we too often stop at developmental testing.

### Measures of Performance and Measures of Effectiveness

A related distinction separates technical performance from mission effectiveness:

**Measures of Performance (MOPs)** quantify technical characteristics of the system itself. For an aircraft, MOPs might include speed, range, payload capacity, radar cross-section, and turn rate. For a communications system, MOPs might include bandwidth, latency, encryption strength, and signal-to-noise ratio. MOPs are typically objective, measurable, and tied to engineering specifications.

**Measures of Effectiveness (MOEs)** quantify how well the system accomplishes its operational mission. For an aircraft, MOEs might include probability of mission success, targets destroyed per sortie, or survivability against specific threat systems. For a communications system, MOEs might include whether commanders can effectively coordinate forces or whether intelligence reaches decision-makers in time to act.

The relationship between MOPs and MOEs is neither simple nor guaranteed. A fighter aircraft might achieve excellent MOPs across the board—faster, more maneuverable, stealthier than any competitor—and still fail operationally if its maintenance requirements make it unavailable when needed, if its cockpit design induces pilot errors under stress, or if its weapons don't integrate effectively with coalition systems. Good MOPs are necessary but not sufficient for good MOEs.

The MOP/MOE distinction translates directly to AI evaluation. AI benchmarks are MOPs: they measure technical capabilities like accuracy on question-answering, code generation success rates, or reasoning test scores. These matter, but they are not MOEs. The MOE for an AI coding assistant is not its score on HumanEval; it's whether developers using it actually produce better software faster. The MOE for an AI analysis tool is not its reading comprehension benchmark; it's whether analysts using it make better decisions.

The challenge, of course, is that MOEs are harder to measure than MOPs. They depend on context, integration, and use patterns. They often can't be assessed until late in the development cycle. But their difficulty doesn't make them less important. Acquisition decisions based solely on AI benchmark scores (MOPs) are like acquisition decisions based solely on technical specifications—they may select for the wrong things.

### Suitability

Beyond effectiveness, military T&E evaluates suitability: whether the system is usable, maintainable, and supportable in operational conditions. A system might be highly effective when it works but unsuitable if it's unreliable, difficult to maintain, incompatible with existing infrastructure, or impossible to support logistically.

Suitability encompasses:

- **Reliability**: Does the system work consistently over time?
- **Maintainability**: Can it be repaired and serviced efficiently?
- **Availability**: What fraction of time is it operational versus down for maintenance or repair?
- **Supportability**: Can the logistics system provide necessary parts, training, and expertise?
- **Human factors**: Can typical users operate it effectively? Is it safe?
- **Interoperability**: Does it work with existing systems and coalition partners?

For AI systems, suitability considerations are at least as important as for traditional systems, though they manifest differently. Reliability means consistent performance across varied conditions—a challenge for AI systems with jagged capability frontiers. Maintainability raises questions about updating, retraining, and adapting AI systems as requirements evolve. Supportability involves the organizational capabilities needed to operate AI effectively: prompt engineering expertise, output verification processes, integration with workflows.

Human factors are particularly critical for AI. Can users understand the AI's outputs well enough to use them appropriately? Do they know when to trust the AI and when to override it? Can they detect and recover from AI errors? These questions parallel traditional human factors concerns but require new evaluation approaches.

### The Test and Evaluation Master Plan

Major defense acquisitions require a Test and Evaluation Master Plan (TEMP): a comprehensive document that specifies what will be tested, how, when, and to what criteria. The TEMP integrates DT and OT planning, links evaluation to system requirements, and identifies the resources needed for testing.

A TEMP typically includes:

- System description and critical requirements
- Developmental test objectives and approach
- Operational test objectives and approach
- Required resources (facilities, ranges, instrumentation, personnel)
- Schedule and milestones
- Criteria for success and decision points

The discipline of comprehensive test planning—thinking through evaluation needs early and systematically rather than improvising as you go—is valuable regardless of what's being evaluated. Major AI acquisitions would benefit from similar discipline: identifying what needs to be evaluated, specifying evaluation methods and criteria, planning for both developmental and operational evaluation, and securing necessary resources.

Currently, most AI acquisitions lack anything resembling a TEMP. Evaluation is often ad hoc, relying on vendor-provided benchmarks, brief demonstrations, or informal pilots without clear success criteria. Introducing systematic evaluation planning, adapted from established T&E practice, would represent a significant improvement.

### Modeling and Simulation Accreditation

Not everything can be tested in live conditions. Modeling and simulation (M&S) often supplements or substitutes for live testing when live tests are too dangerous, too expensive, or impossible to arrange. But how much confidence should we place in simulation results? How do we know the simulation is realistic enough to inform real decisions?

Military T&E addresses this through M&S accreditation: a formal process for determining whether a particular model or simulation is adequate for a specific purpose. Accreditation is not a general certification that a simulation is "good"; it's a determination that a specific simulation is suitable for a specific use. The same simulation might be accredited for one purpose and not another.

The accreditation process examines:

- **Verification**: Is the simulation implemented correctly? Does it do what it claims?
- **Validation**: Does the simulation adequately represent reality for the intended purpose?
- **Credibility**: Do subject matter experts find the simulation plausible?
- **Sensitivity**: How do results change with input assumptions?
- **Limitations**: What can the simulation not represent?

AI benchmarks are, in effect, simulations of real-world tasks. A coding benchmark simulates real coding work. A question-answering benchmark simulates real information-seeking. The question "when can we trust benchmark results?" is analogous to "when should we accredit a simulation for decision support?"

Applying M&S accreditation thinking to AI benchmarks would ask: For what purposes is this benchmark suitable? What decisions should it inform, and which should require other evidence? What are its known limitations? How was it validated against actual performance? Who has reviewed its credibility? These questions are rarely asked systematically about AI benchmarks—but they should be.

### Independent Operational Test Organizations

A crucial feature of military T&E is the separation between developers and operational testers. Organizations like the Director, Operational Test and Evaluation (DOT&E) are independent of program offices and developers. Their mission is to provide decision-makers with unbiased assessments of whether systems work in operational conditions.

This independence exists because developers have natural incentives to present their systems favorably. They may unconsciously design tests that showcase strengths and avoid weaknesses. They may interpret ambiguous results optimistically. They may have schedule and budget pressures that discourage thorough testing. Independent operational testers, without these incentives, can provide assessments that decision-makers can trust.

The principle of independent evaluation applies forcefully to AI acquisition. Vendor-provided benchmark results and demonstrations have obvious credibility limitations. Vendors select which benchmarks to report, how to configure systems for demos, and which results to emphasize. This isn't necessarily dishonest—vendors naturally highlight strengths—but it means vendor-provided evidence should be supplemented with independent assessment.

For high-stakes AI acquisitions, independent evaluation is not a luxury but a necessity. This might mean government testing of vendor systems, third-party evaluations, or operational pilots with independent assessment. The specific mechanism matters less than the principle: evaluation independence is essential for trustworthy results.

---

## What Transfers to AI Evaluation

Several elements of military T&E transfer directly to AI evaluation with minimal adaptation:

**The DT/OT paradigm** provides the right mental model. Benchmarks and controlled studies are developmental testing—valuable for verification and engineering insight, but not sufficient for operational confidence. Operational testing for AI means evaluation in realistic conditions with representative users doing genuine work. The field needs to develop AI-specific approaches to operational testing, but the conceptual framework is sound.

**The MOP/MOE distinction** is immediately applicable and valuable. Benchmark scores are MOPs; operational outcomes are MOEs. This framing helps acquisition professionals ask the right questions: "What are the MOEs for this AI system? How will we measure whether it actually improves mission outcomes? What evidence do we have that benchmark performance predicts operational effectiveness?"

**The suitability concept** reminds evaluators to look beyond raw capability to the full context of operational use. AI suitability encompasses reliability across conditions, maintainability as requirements evolve, supportability with available expertise, human factors in the human-AI team, and interoperability with existing systems and workflows.

**Test planning discipline** from the TEMP tradition provides a model for systematic AI evaluation planning. Rather than ad hoc testing, major AI acquisitions should have comprehensive evaluation plans specifying objectives, methods, criteria, resources, and decision points for both developmental and operational assessment.

**M&S accreditation thinking** provides a framework for evaluating AI benchmarks themselves. Rather than treating benchmark scores as simple facts, this approach asks: For what purposes is this benchmark valid? What evidence supports its relationship to operational performance? What are its limitations? This meta-level scrutiny is currently rare but essential.

**Independent evaluation** is as important for AI as for traditional systems—arguably more important given the difficulty of evaluating AI capabilities and the significant asymmetries between vendors and buyers in AI expertise. High-stakes AI acquisitions should include independent assessment, not just vendor-provided evidence.

---

## What Breaks for Generative AI

Despite the value of traditional T&E frameworks, several features of generative AI systems challenge their direct application:

**Stable system configuration** is assumed throughout T&E methodology. The system tested in DT is the same system tested in OT is the same system fielded operationally. Version control and configuration management ensure this consistency. For AI systems accessed through APIs or cloud services, providers may update models at any time, often without notification to users. The system evaluated in testing may not be the system deployed—or the system deployed this week may differ from the system deployed next month. This fluidity challenges the entire logic of point-in-time testing leading to deployment decisions.

**Physical test environments** can be specified and replicated for traditional systems. Test ranges, environmental chambers, and simulation facilities provide controlled conditions that can be documented and reproduced. AI systems operate in "information environments" that are harder to characterize and control. What's the equivalent of a test range for an AI assistant? How do you specify the "conditions" of knowledge work?

**Failure mode predictability** is assumed in traditional system evaluation. Hardware failures follow physical laws. Software failures, while complex, can often be traced to specific code defects. AI failures are fundamentally less predictable—the jagged capability frontier means that similar-seeming inputs may produce dramatically different performance. Confidence about performance in tested regions doesn't generalize reliably to untested regions.

**Requirements stability** underlies the logic of verifying that systems meet requirements. Traditional systems are built to specifications that are fixed (at least within development phases). AI systems have emergent capabilities that weren't designed or specified. Requirements may evolve as users discover new possibilities. The traditional model of writing requirements, building to requirements, and testing against requirements fits poorly when capabilities are emergent and evolving.

**Test infrastructure** is mature for traditional systems. Ranges, facilities, instrumentation, and evaluation expertise have developed over decades. AI evaluation infrastructure is immature. There are no established equivalents of test ranges for AI, no standard instrumentation for measuring AI performance in operational conditions, and limited institutional expertise in AI evaluation methods.

**Reproducibility** enables traditional T&E to generate evidence that can be reviewed, audited, and replicated. Stochastic AI systems produce different results on each run, making exact reproduction impossible. Evaluation results must be statistical statements about distributions, not deterministic facts about outputs. This complicates documentation, review, and the use of test evidence in acquisition decisions.

---

## What Can Be Adapted

Between direct transfer and fundamental breaks lies substantial middle ground—traditional T&E concepts that can be adapted for AI with appropriate modifications:

**Operational realism requirements** from OT can inform AI evaluation design. OT emphasizes representative users (not experts), realistic scenarios (not idealized conditions), and operational environments (not laboratories). For AI, this translates to: evaluation with users whose skills match the expected user population, tasks drawn from actual workflows rather than curated examples, and conditions that reflect deployment reality including interruptions, time pressure, and incomplete information.

**Scenario-based testing** is well-developed for traditional OT. Evaluators design operational scenarios that stress the system across its expected use envelope, including challenging conditions and edge cases. Similar scenario-based approaches can structure AI evaluation, systematically varying task types, difficulty levels, and contextual factors to explore the capability space.

**Critical Operational Issues (COIs)** provide a framework for identifying the most important evaluation questions. Rather than trying to test everything, OT identifies a limited number of critical issues that must be resolved for an acquisition decision. For AI, COIs might include: "Does the system provide reliable productivity gains for analysts?" or "Can operators detect and recover from AI errors before they cause harm?" Focusing evaluation on critical issues makes evaluation tractable while ensuring key questions are addressed.

**Multi-phase evaluation** can be adapted for AI. Rather than single-point DT and OT, AI might benefit from evaluation phases: initial capability assessment, controlled workflow studies, limited operational pilots, expanded deployment with monitoring. Each phase provides different evidence at different fidelity, supporting incremental commitment as confidence builds.

**Combined test approaches** that integrate DT and OT can be adapted for AI's faster pace. Traditional sequential DT→OT may be too slow for rapidly evolving AI systems. More integrated approaches—where operational considerations inform developmental testing and operational testing begins earlier—may be more appropriate.

---

## Implications for AI Evaluation

Drawing on military T&E experience, several principles should guide AI evaluation for acquisition:

**Apply the DT/OT mindset.** Recognize that benchmarks and controlled studies (DT) are valuable but insufficient. Plan for operational evaluation (OT) with representative users in realistic conditions. Don't make major acquisition decisions based solely on DT-equivalent evidence.

**Define MOEs, not just MOPs.** Before acquiring an AI system, be clear about the operational outcomes it should produce—the MOEs. Then ask: What evidence do we have that benchmark performance (MOPs) predicts these outcomes? If the answer is "not much," additional evaluation is needed.

**Evaluate suitability, not just effectiveness.** Consider the full context of operational use: reliability, maintainability, supportability, human factors, interoperability. An AI system that performs impressively in demos may still be unsuitable if users can't effectively employ it, if it requires expertise that isn't available, or if it doesn't integrate with existing workflows.

**Plan evaluation systematically.** Major AI acquisitions should have evaluation plans analogous to a TEMP: specifying what will be evaluated, how, when, and to what criteria. Ad hoc evaluation is not adequate for significant acquisition decisions.

**Apply accreditation thinking to benchmarks.** Before relying on benchmark results, ask: Is this benchmark suitable for informing this decision? How was it validated? What are its known limitations? What evidence connects benchmark performance to operational outcomes?

**Insist on independent evaluation for high stakes.** Vendor-provided evidence is useful but insufficient. For significant acquisitions, include independent evaluation—government testing, third-party assessment, or operational pilots with independent analysis. Evaluation credibility requires evaluator independence.

**Expect and plan for system change.** Traditional T&E assumes stable configurations. AI systems will change—through provider updates, user adaptation, and evolving use patterns. Evaluation approaches must account for this fluidity, including ongoing monitoring after initial deployment decisions.

**Build AI T&E infrastructure and expertise.** Traditional T&E is supported by mature infrastructure and institutional expertise. AI T&E currently lacks equivalent support. Organizations should invest in developing AI evaluation capabilities: methods, tools, facilities, and personnel with relevant expertise.

---

## Key References

For readers seeking deeper engagement with military T&E concepts:

**Policy and Guidance**

- **DoD Directive 5000.01 and DoDI 5000.02.** The foundational policy documents for defense acquisition, including T&E requirements.

- **DoDI 5000.89, Test and Evaluation.** Specific policy guidance for T&E in defense acquisition.

- **DoD 5000.90, Cybersecurity for Acquisition Decision Authorities and Program Managers.** Includes guidance on cybersecurity T&E, relevant to AI security evaluation.

**Institutional Resources**

- **Director, Operational Test and Evaluation (DOT&E) Annual Reports.** Provide examples of operational test findings and evaluation methodology. Available at dote.osd.mil.

- **Government Accountability Office (GAO) reports on weapon system acquisition.** Often include discussion of T&E issues and lessons learned.

- **Defense Acquisition University (DAU) resources.** Training materials and guidance on T&E within the acquisition lifecycle.

**Foundational Texts**

- **INCOSE Systems Engineering Handbook (4th ed., 2015).** Comprehensive reference on systems engineering, including verification and validation.

- **Blanchard, B.S., & Fabrycky, W.J. (2010). *Systems Engineering and Analysis* (5th ed.).** Textbook treatment of systems engineering fundamentals.

- **National Research Council. (1998). *Statistics, Testing, and Defense Acquisition*.** Examination of statistical issues in defense T&E.

**M&S Accreditation**

- **DoD Instruction 5000.61, Modeling and Simulation Verification, Validation, and Accreditation.** Policy guidance for M&S VV&A.

- **Balci, O. (1998). "Verification, Validation, and Accreditation." *Proceedings of the Winter Simulation Conference*.** Foundational paper on M&S VV&A concepts.

**Emerging AI-Specific Guidance**

- **DoD AI Strategy and AI Principles.** Policy context for defense AI acquisition and use.

- **NIST AI Risk Management Framework.** While not DoD-specific, provides a framework for AI risk management applicable to acquisition.

- **Joint Artificial Intelligence Center (JAIC) resources.** Guidance on AI acquisition and implementation within DoD. (Note: Organizational structures continue to evolve.)

---

## Connections to Other Sections

Systems T&E concepts connect to several other disciplines covered in this appendix:

- **Section 1.1 (Software Testing)** provides the verification concepts that underlie systems V&V, and the verification/validation distinction that parallels MOPs/MOEs.

- **Section 1.3 (Autonomous Systems)** extends T&E to AI-adjacent systems and provides the closest existing paradigm for AI evaluation within defense contexts.

- **Section 4.1 (Risk Analysis)** provides frameworks for risk-based test planning and evaluation prioritization.

- **Section 4.5 (Safety Engineering)** develops safety case methodology applicable to safety-critical AI.

- **Section 5.2 (Human-Machine Systems)** expands on human factors and suitability evaluation for human-AI teams.

- **Section 6.2 (Program Evaluation)** offers complementary frameworks for evaluating AI as an organizational intervention.

- **Section 7.2 (Standards Development)** discusses the emerging standards environment for AI, including defense-relevant standards.

---

*[End of Section 1.2]*


## Overview

Autonomous systems—vehicles that drive themselves, aircraft that fly without pilots, robots that navigate and manipulate without direct human control—represent the closest existing paradigm to generative AI evaluation. Both involve AI components that make decisions under uncertainty. Both must operate reliably in conditions that cannot be fully anticipated. Both raise profound questions about how to achieve justified confidence in systems whose behavior cannot be exhaustively specified or tested.

The autonomous systems community has grappled with these challenges for decades, developing frameworks for levels of autonomy, methods for testing in simulation and reality, approaches to safety cases, and deep expertise in human-machine teaming. This accumulated wisdom offers valuable resources for generative AI evaluation. At the same time, important differences between autonomous systems and generative AI mean that not everything transfers cleanly.

Autonomous systems operate in physical space, where the laws of physics constrain possible behaviors and consequences are often immediately observable. A self-driving car that makes a wrong decision crashes; a drone that loses control falls. Generative AI operates in information space, where outputs are unbounded, failures may be subtle, and consequences may propagate through human decisions in ways that are difficult to trace. These differences matter for evaluation.

This section surveys the key concepts from autonomous systems T&E, examines what applies to generative AI, identifies where the analogy breaks down, and draws out implications for AI evaluation practice.

---

## Core Concepts

### Levels of Autonomy

One of the most influential contributions from autonomous systems research is the development of frameworks describing degrees of autonomy—the extent to which a system operates independently versus under human control.

The SAE J3016 standard for driving automation defines six levels:

- **Level 0 (No Automation)**: Human performs all driving tasks
- **Level 1 (Driver Assistance)**: System assists with either steering or acceleration/braking
- **Level 2 (Partial Automation)**: System controls both steering and acceleration/braking; human must monitor
- **Level 3 (Conditional Automation)**: System handles all driving in certain conditions; human must be ready to intervene
- **Level 4 (High Automation)**: System handles all driving in certain conditions; no human intervention needed
- **Level 5 (Full Automation)**: System handles all driving in all conditions

Similar frameworks exist for other domains. Sheridan and Verplank's classic 10-level scale for human-computer decision-making ranges from "computer offers no assistance" to "computer decides everything, acts autonomously, ignores human." These frameworks help clarify what kind of system we're evaluating, what human role is expected, and what the evaluation should focus on.

Levels of autonomy matter for evaluation because different levels require different evaluation approaches. A Level 2 system where humans must monitor continuously requires evaluation of human vigilance and intervention capability. A Level 4 system that must handle situations autonomously requires much more comprehensive capability testing. The handoff between automation and human—particularly relevant at Level 3—requires specific evaluation attention.

Generative AI doesn't map neatly onto these frameworks. A coding assistant might be "Level 2" for routine code completion (human reviews all suggestions) but effectively "Level 4" for certain automated workflows (code generated and deployed without human review). The level of autonomy often varies by use case, user, and organizational policy rather than being fixed by system design. Still, the underlying questions are relevant: How much is the human in the loop? What interventions are expected? What happens when the human isn't monitoring effectively?

### Operational Design Domain

The Operational Design Domain (ODD) defines the conditions under which an autonomous system is designed to operate. For a self-driving car, the ODD might specify:

- Geographic areas (mapped urban areas, highway only, specific cities)
- Road types (paved roads, divided highways, excluding unpaved surfaces)
- Weather conditions (clear weather, light rain, excluding snow and ice)
- Time of day (daylight only, or including night with adequate lighting)
- Speed ranges (under 65 mph, under 25 mph in urban areas)
- Traffic conditions (normal traffic, excluding construction zones)

The ODD represents a kind of contract: the system is designed and tested to operate within these conditions, and performance claims apply only within the ODD. Outside the ODD, the system may not function correctly, and evaluation has not established expected performance.

ODD thinking brings discipline to capability claims. Rather than asking "can this self-driving car drive?" we ask "under what conditions can it drive, and how do we know?" This prevents overgeneralization from limited testing. A system tested only on California highways in clear weather hasn't demonstrated capability for Boston winters.

Defining an ODD for generative AI is challenging but valuable. What is the "operating envelope" for a language model assistant? One might specify:

- Task types (drafting text, answering factual questions, code assistance—excluding medical diagnosis, legal advice)
- Languages (English, with limited capability in other languages)
- Context requirements (performs best with clear instructions and relevant context provided)
- User populations (assumes users can evaluate output quality in their domain)
- Use patterns (interactive use with human review, not autonomous execution)

Current AI deployments rarely make ODD-like specifications explicit. Capability claims are often vague ("helpful for a wide range of tasks") rather than bounded. Making the operational envelope explicit—and acknowledging uncertainty about performance outside it—would improve both evaluation and deployment.

### The Simulation-to-Real Gap

Autonomous systems are extensively tested in simulation before real-world deployment. Simulation offers advantages: it's cheaper, safer, faster, and allows testing of dangerous scenarios without actual risk. Simulated miles for self-driving cars can be accumulated far faster than physical miles.

But simulation performance doesn't guarantee real-world performance. The "sim-to-real gap" refers to the differences between simulated and real environments that cause systems to perform differently in each. Simulations inevitably simplify reality—the physics may be approximate, the sensor models imperfect, the variety of situations limited. A system optimized for simulation may exploit artifacts that don't exist in reality, or fail to handle real-world phenomena that weren't simulated.

The autonomous systems community has developed approaches to managing the sim-to-real gap:

- **Domain randomization**: Varying simulation parameters to expose the system to diverse conditions
- **High-fidelity simulation**: Investing in more accurate physics, sensors, and scenarios
- **Transfer learning**: Training techniques that improve generalization from simulation to reality
- **Progressive testing**: Using simulation for initial testing, then validating in controlled real-world conditions, then expanding to broader deployment
- **Scenario validation**: Comparing simulation behavior to real-world behavior on matched scenarios

The sim-to-real gap has a direct analog for generative AI: the benchmark-to-real gap. Benchmarks are simulations of real tasks. They simplify and standardize what are actually diverse, contextual, open-ended activities. Performance on a coding benchmark (simulation) doesn't guarantee performance on actual developer workflows (reality). Performance on a medical question-answering dataset doesn't guarantee useful performance in clinical settings.

The strategies for managing sim-to-real transfer are suggestive for AI evaluation. Domain randomization parallels testing across diverse prompts and conditions rather than narrow benchmark distributions. Progressive testing parallels moving from benchmarks to controlled studies to operational pilots. Scenario validation parallels comparing benchmark performance to operational performance on matched tasks.

### Edge Cases and Scenario-Based Testing

Autonomous systems must handle not just typical conditions but also rare, unusual, or challenging situations—edge cases that may occur infrequently but matter enormously when they do. A self-driving car might handle normal highway driving well but fail catastrophically when encountering an unusual obstacle, a confusing construction zone, or unexpected behavior from other road users.

Testing for edge cases is challenging precisely because they're rare and diverse. You can't wait to encounter them naturally—that would require billions of miles of driving. Instead, autonomous systems testing uses scenario-based approaches:

- **Scenario libraries**: Collections of known challenging scenarios derived from accidents, near-misses, and domain expertise
- **Scenario generation**: Systematic methods for generating scenarios that explore the space of possible situations
- **Adversarial scenarios**: Deliberately designed scenarios that stress system capabilities
- **Importance sampling**: Concentrating testing on high-risk scenarios rather than typical ones
- **Combinatorial testing**: Systematically combining factors (weather, traffic, road type) to cover the space efficiently

The combinatorial explosion of possible scenarios is a fundamental challenge. Even with finite factors, the combinations quickly become astronomical. Risk-based prioritization is essential: focus on scenarios that are both plausible and consequential.

Generative AI faces an even more severe version of this challenge. The "scenario space" for a language model—all possible prompts and contexts—is not just large but effectively infinite and continuous. There's no way to enumerate even the categories of possible inputs, let alone the specific instances. The jagged capability frontier means that small changes in prompts can produce dramatically different performance, making systematic coverage even harder.

Still, scenario-based thinking has value. Testing should deliberately explore:

- Different task types and domains
- Varying difficulty levels within task types
- Tasks near the boundaries of claimed capabilities
- Tasks requiring capabilities the system might lack (current events, precise calculation, etc.)
- Potentially problematic content areas
- Adversarial and stress-test inputs

The goal is not exhaustive coverage—impossible for generative AI—but strategic exploration of the capability space with attention to high-risk regions.

### Safety Cases

A safety case is a structured argument, supported by evidence, that a system is acceptably safe for a given application in a given context. Rather than simply claiming "this system is safe," a safety case makes the reasoning explicit:

- **Claims**: Specific assertions about system safety (e.g., "The system will detect pedestrians with probability > 99% in conditions X, Y, Z")
- **Evidence**: Data, test results, analysis supporting each claim
- **Argument**: Logical structure linking evidence to claims and claims to the overall safety conclusion
- **Context**: Assumptions and scope limitations

Safety cases originated in high-hazard industries (nuclear, aerospace, rail) and have been adopted for autonomous systems. Standards like UL 4600 (Standard for Safety for the Evaluation of Autonomous Products) provide frameworks for autonomous vehicle safety cases.

The value of safety cases lies in making reasoning explicit and contestable. Rather than a black-box assertion of safety, stakeholders can examine the argument structure, evaluate the evidence, identify assumptions, and probe weak points. Regulators can assess whether the argument is sound. Over time, as evidence accumulates or assumptions prove wrong, safety cases can be updated.

Safety case methodology is increasingly being adapted for AI systems, particularly in the AI safety research community. An AI safety case might argue:

- The system has been tested for harmful outputs across categories X, Y, Z with results showing acceptably low rates
- The system includes guardrails that prevent certain types of harmful outputs
- Operational procedures ensure human review of high-stakes outputs
- Monitoring will detect anomalous behavior and trigger review
- Therefore, the system is acceptably safe for deployment in context C

This is an active area of development. Challenges include the difficulty of comprehensive testing (the unbounded output space), uncertainty about what "acceptably safe" means for AI, and the rapid pace of change that may invalidate assumptions. But the discipline of structured safety argumentation is valuable regardless of these challenges.

### Human Supervisory Control

Autonomous systems rarely operate in complete isolation from humans. Even highly automated systems typically involve human supervisory control: humans monitor system operation, intervene when necessary, handle situations beyond system capability, and bear ultimate responsibility for outcomes.

Research on human supervisory control has identified several challenges:

**Vigilance and monitoring**: Humans are poor at sustained monitoring of systems that usually work correctly. Attention wanders. Complacency develops. Rare events that require intervention may not be detected in time.

**Mode confusion**: Complex automated systems have many modes of operation. Users may be uncertain which mode the system is in, leading to unexpected behavior and inappropriate responses.

**Skill degradation**: When automation handles routine tasks, human skills for those tasks may atrophy. If automation fails and humans must take over, they may not be able to perform effectively.

**Automation surprises**: When automated systems behave unexpectedly, humans may be startled, confused, and slow to respond appropriately. The more autonomous the system, the greater the potential for surprises.

**Trust calibration**: Humans must calibrate their trust in automation appropriately—neither trusting too much (failing to catch errors) nor too little (failing to realize benefits). Calibration is difficult when automation reliability varies across conditions.

These challenges are directly relevant to human-AI teaming with generative AI. Users monitoring AI outputs face vigilance challenges—most outputs may be fine, leading to reduced scrutiny that misses errors. AI behavior can be surprising when the jagged capability frontier produces unexpected failures. Trust calibration is difficult when AI reliability varies unpredictably across tasks.

Evaluation of human-AI systems must assess not just AI capability but the entire human-AI team: Can users detect and correct AI errors? Do they trust appropriately? Can they intervene effectively? What happens when the AI fails in unexpected ways?

### Verification and Validation for Autonomy

Traditional verification and validation (V&V) assumes you can specify required behavior and check whether the system exhibits it. For autonomous systems with learned components, this is problematic:

- Behavior emerges from training rather than explicit programming
- Requirements may not fully specify desired behavior
- The space of possible situations is too large to test exhaustively
- System behavior may be difficult to predict or explain

The autonomous systems community has developed adapted V&V approaches:

**Scenario-based V&V**: Rather than verifying all possible behaviors, verify behavior in a defined (if large) set of scenarios. Scenarios are selected to be representative, challenging, and safety-relevant.

**Runtime verification**: Rather than pre-deployment verification alone, monitor system behavior during operation and check that it stays within acceptable bounds. Runtime monitors can detect anomalies and trigger safeguards.

**Formal methods (limited scope)**: Some safety-critical properties can be verified formally, even if overall behavior cannot. For example, verifying that certain actions are never taken regardless of inputs, or that the system always maintains certain invariants.

**Statistical verification**: Rather than proving behavior is always correct, estimate the probability of correct behavior based on testing. This requires careful statistical methodology and acknowledgment of uncertainty.

**Assurance cases**: Using structured arguments (like safety cases) to make the case for adequate verification, even when complete verification is impossible.

These approaches inform AI evaluation. Complete verification of generative AI is impossible—the output space is too large, the "correct" output often undefined. But we can verify behavior in selected scenarios, monitor runtime behavior, formally verify certain properties (e.g., certain outputs are filtered), provide statistical performance estimates, and construct assurance arguments for why our evaluation is adequate for the intended use.

---

## What Transfers to AI Evaluation

Several concepts from autonomous systems evaluation apply directly to generative AI:

**Levels of autonomy thinking** encourages clarity about the human role. Is the AI generating suggestions for human review (lower autonomy) or taking actions with minimal oversight (higher autonomy)? Different levels require different evaluation focus. Higher autonomy demands more comprehensive capability testing; lower autonomy demands more attention to human oversight effectiveness.

**ODD discipline** encourages bounded capability claims. Rather than vague assertions that an AI is "helpful" or "capable," ODD thinking asks: for what tasks, in what conditions, with what user populations, and with what confidence? Making the operational envelope explicit improves both evaluation and deployment.

**Sim-to-real gap awareness** directly parallels benchmark-to-real gap awareness. Autonomous systems researchers know that simulation performance doesn't guarantee real-world performance and have developed strategies for managing this gap. AI evaluation should adopt similar humility about benchmarks and similar strategies for validation.

**Scenario-based testing** provides a framework for exploring capability spaces that are too large for exhaustive testing. Strategic scenario selection—diverse, challenging, risk-weighted—is as relevant for AI as for autonomous systems.

**Safety case methodology** offers structured approaches to arguing for acceptable safety. For high-stakes AI deployments, constructing explicit safety cases—with clear claims, evidence, and arguments—brings discipline and transparency to safety assurance.

**Human supervisory control research** is directly applicable to human-AI teaming. Decades of research on vigilance, trust calibration, automation surprises, and intervention effectiveness inform how we should evaluate and design human-AI systems.

**Runtime verification and monitoring** concepts support continuous AI monitoring. Rather than relying solely on pre-deployment testing, AI systems should be monitored during operation, with mechanisms to detect anomalies and trigger review.

---

## What Breaks for Generative AI

Despite substantial overlap, important differences limit how directly autonomous systems approaches apply to generative AI:

**Physical versus information environments**: Autonomous systems operate in physical space governed by physics, with directly observable outcomes. A car crash is unambiguous. Generative AI operates in information space, where "failure" may be subtle (slightly misleading text, suboptimal code, biased framing) and consequences propagate through human decisions in complex ways. The bounded, physical nature of autonomous systems makes evaluation more tractable in some respects.

**Observable failures**: When an autonomous vehicle makes an error, the error is often immediately apparent—it hits something, goes off the road, or behaves erratically. When a language model produces a flawed output, the flaw may not be apparent to users who lack expertise to evaluate it. The observability of failures differs fundamentally.

**Definable operating envelopes**: While ODD definition is challenging for autonomous systems, it's at least conceptually tractable. Geographic bounds, weather conditions, and road types can be specified. For generative AI, the "conditions of operation" are far harder to define. What's the boundary between prompts the system should handle and prompts it shouldn't? The continuous, high-dimensional nature of text makes boundary definition much harder.

**Failure mode predictability**: Autonomous system failures, while not fully predictable, follow patterns related to sensor limitations, environmental conditions, and scenario difficulty. With experience, practitioners develop intuition for likely failure modes. Generative AI failures are less predictable—the jagged capability frontier means that similar-seeming inputs can produce dramatically different performance, without clear patterns explaining why.

**Formal verification scope**: Some autonomous system properties can be formally verified—collision avoidance guarantees, geofencing constraints, speed limits. Generative AI properties are much harder to formalize. What would it mean to formally verify that outputs are "helpful" or "not harmful"? The output space is too large and the relevant properties too ill-defined.

**Development and deployment stability**: Autonomous vehicle development involves long cycles of testing before deployment, with relatively stable software versions. Generative AI systems are often updated continuously, sometimes without user notification. The rapid pace of change challenges evaluation approaches that assume stable systems.

**Regulatory and institutional context**: Autonomous vehicles are subject to emerging regulatory frameworks that shape evaluation requirements. Generative AI largely lacks such frameworks. This cuts both ways—less regulatory overhead, but also less institutional structure supporting rigorous evaluation.

---

## What Can Be Adapted

Many autonomous systems concepts can be adapted for generative AI with appropriate modifications:

**ODD specification for AI** may never achieve the crispness of geographic bounds and weather conditions, but approximate capability boundaries can still be articulated. This AI system is designed for: drafting professional communications (not legal documents), answering factual questions (with limitations on recent events), code assistance (with human review required), English language (limited other language capability). Even imprecise boundaries are better than unbounded capability claims.

**Scenario libraries for AI** can be developed, even though the space can't be enumerated. Collections of challenging prompts, known failure modes, and adversarial inputs can inform systematic testing. These libraries will never be complete, but they can grow with experience and be shared across organizations.

**Sim-to-real validation strategies** can inform benchmark validation. Just as autonomous systems validate simulation with real-world comparison, AI benchmarks can be validated by comparing benchmark performance to operational performance on matched tasks. Finding substantial gaps should reduce confidence in benchmark results.

**Progressive deployment** models from autonomous systems—limited testing, then controlled pilots, then bounded deployment, then broader deployment—can structure AI rollout. Each phase generates evidence and builds confidence, with expansion contingent on positive results.

**Safety case frameworks** can be adapted for AI, as the AI safety community is actively doing. The specific claims and evidence will differ, but the discipline of structured argumentation transfers. What claims about AI safety are we making? What evidence supports each claim? What assumptions are we making? How strong is the overall argument?

**Runtime monitoring concepts** can inform AI monitoring. Define metrics that should stay within acceptable bounds. Implement continuous monitoring. Establish alerting and response procedures for anomalies. This doesn't require solving all AI monitoring challenges—just applying systematic monitoring discipline.

**Human factors evaluation methods** from autonomous systems can be applied to human-AI teams. Evaluate vigilance and oversight quality. Assess trust calibration. Test intervention capabilities. Measure situation awareness. These methods need adaptation for the different human-AI interface (conversation versus vehicle controls), but the underlying concerns are similar.

---

## Implications for AI Evaluation

Drawing on autonomous systems experience, several principles should guide generative AI evaluation:

**Define the operating envelope.** Even if precise boundaries aren't achievable, articulate what the AI is designed and tested for—and what it isn't. Capability claims should be bounded, not open-ended. Evaluation should verify performance within the claimed envelope and probe boundaries and limitations.

**Take the benchmark-to-real gap seriously.** Benchmark performance is necessary but not sufficient, just as simulation performance is necessary but not sufficient for autonomous systems. Plan for validation of benchmark results against operational performance. Investigate discrepancies. Don't assume benchmark success predicts deployment success.

**Use scenario-based testing strategically.** Develop and maintain collections of test scenarios—diverse, challenging, risk-weighted. Include known failure modes, edge cases, and adversarial inputs. Update scenario libraries as new failure modes are discovered. Share scenario resources across organizations where possible.

**Build safety cases for high-stakes deployments.** For AI applications with significant consequences, construct explicit safety cases. Make claims, evidence, and arguments clear and documented. Subject safety cases to review and challenge. Update them as evidence accumulates or assumptions change.

**Evaluate the human-AI system.** Capability evaluation of AI alone is insufficient. Evaluate the full human-AI system: Can users detect errors? Do they trust appropriately? Can they intervene effectively? Human factors evaluation methods from autonomous systems provide a starting point.

**Plan for runtime monitoring.** Pre-deployment evaluation cannot guarantee ongoing performance. Plan monitoring from the start: What will you measure? What are acceptable bounds? How will anomalies be detected and handled? Monitoring is not an afterthought but a core component of evaluation strategy.

**Adopt progressive deployment.** Rather than binary deploy/don't-deploy decisions, consider staged deployment: limited initial deployment with intensive monitoring, expansion based on operational evidence, ongoing monitoring at scale. This generates operational evidence while managing risk.

**Recognize the limits of the analogy.** Autonomous systems experience offers valuable resources, but generative AI is not just another autonomous system. The information-space environment, unbounded outputs, subtle failures, and less predictable behavior all create evaluation challenges beyond what autonomous systems research has addressed. Humility about these limits is appropriate.

---

## Key References

**Levels of Autonomy and Frameworks**

- **SAE International. (2021). SAE J3016: Taxonomy and Definitions for Terms Related to Driving Automation Systems for On-Road Motor Vehicles.** The standard reference for driving automation levels, with broader influence on autonomy discussions.

- **Sheridan, T.B., & Verplank, W.L. (1978). Human and Computer Control of Undersea Teleoperators.** Classic framework for levels of automation in human-computer systems.

- **Parasuraman, R., Sheridan, T.B., & Wickens, C.D. (2000). "A Model for Types and Levels of Human Interaction with Automation." *IEEE Transactions on Systems, Man, and Cybernetics*.** Influential framework analyzing automation across stages of information processing.

**Operational Design Domain**

- **NHTSA. (2017). Automated Driving Systems: A Vision for Safety 2.0.** Introduces ODD concept for regulatory discussion of automated vehicles.

- **BSI PAS 1883:2020. Operational Design Domain (ODD) Taxonomy for an Automated Driving System.** Structured taxonomy for specifying ODDs.

**Simulation and Testing**

- **Kalra, N., & Paddock, S.M. (2016). "Driving to Safety: How Many Miles of Driving Would It Take to Demonstrate Autonomous Vehicle Reliability?" *Transportation Research Part A*.** RAND analysis showing the challenge of demonstrating safety through testing alone—billions of miles required.

- **Koopman, P., & Wagner, M. (2016). "Challenges in Autonomous Vehicle Testing and Validation." *SAE International Journal of Transportation Safety*.** Overview of testing challenges for autonomous vehicles.

- **Corso, A., Moss, R., Koren, M., Lee, R., & Kochenderfer, M.J. (2021). "A Survey of Algorithms for Black-Box Safety Validation of Cyber-Physical Systems." *Journal of Artificial Intelligence Research*.** Survey of approaches to finding failure modes in autonomous systems.

**Safety Cases**

- **UL 4600. (2020). Standard for Safety for the Evaluation of Autonomous Products.** Industry standard providing framework for autonomous vehicle safety cases.

- **ISO 21448. (2022). Road Vehicles—Safety of the Intended Functionality (SOTIF).** Standard addressing safety of intended functionality, beyond traditional functional safety.

- **Bloomfield, R., & Bishop, P. (2010). "Safety and Assurance Cases: Past, Present and Possible Future." In *Making Systems Safer*.** Overview of safety case methodology and its evolution.

- **Haddon-Cave, C. (2009). The Nimrod Review.** Influential analysis of safety case weaknesses in a major accident, with lessons for safety case practice.

**Human Factors in Autonomy**

- **Endsley, M.R. (2017). "Autonomous Driving Systems: A Preliminary Naturalistic Study of the Tesla Model S." *Journal of Cognitive Engineering and Decision Making*.** Study of human interaction with vehicle automation.

- **Lee, J.D. (2018). "Perspectives on Automotive Automation and Autonomy." *Journal of Cognitive Engineering and Decision Making*.** Overview of human factors challenges in vehicle automation.

- **Seppelt, B.D., & Lee, J.D. (2019). "Keeping the Driver in the Loop: Dynamic Feedback to Support Appropriate Use of Imperfect Vehicle Control Automation." *International Journal of Human-Computer Studies*.** Research on maintaining appropriate human engagement with automation.

**V&V for Autonomous Systems**

- **Koopman, P., & Wagner, M. (2017). "Autonomous Vehicle Safety: An Interdisciplinary Challenge." *IEEE Intelligent Transportation Systems Magazine*.** Discussion of safety validation challenges.

- **Thorn, E., Kimmel, S., & Chaka, M. (2018). A Framework for Automated Driving System Testable Cases and Scenarios. (DOT HS 812 623).** NHTSA framework for AV testing scenarios.

- **Webb, N., Smith, D., Ludwick, C., Victor, T., Hommes, Q., Favarò, F., Ivanov, G., & Daniel, T. (2020). "Waymo's Safety Methodologies and Safety Readiness Determinations." *arXiv preprint*.** Waymo's public description of their safety methodology.

**AI Safety Cases (Emerging)**

- **Clymer, J., et al. (2024). "Safety Cases: How to Justify the Safety of Advanced AI Systems." *arXiv preprint*.** Emerging framework for AI safety cases.

- **CLTC. (2025). "Assessing Confidence in Frontier AI Safety Cases." [2502.05791].** Analysis of challenges in AI safety case assessment.

---

## Connections to Other Sections

Autonomous systems T&E connects to several other disciplines covered in this appendix:

- **Section 1.1 (Software Testing)** provides foundational testing concepts that autonomous systems extend to AI-enabled software.

- **Section 1.2 (Systems T&E)** provides the defense acquisition context within which many autonomous systems are evaluated.

- **Section 1.4 (Traditional ML Evaluation)** covers evaluation of the machine learning components within autonomous systems.

- **Section 4.1 (Risk Analysis)** provides risk assessment frameworks applicable to autonomous system safety.

- **Section 4.5 (Safety Engineering)** develops safety analysis methods (FMEA, FTA, STPA) applicable to autonomous systems.

- **Section 5.2 (Human Factors)** expands on human-machine teaming concepts introduced here.

- **Section 6.1 (AI Safety Evaluation)** covers the emerging AI-specific adaptation of safety evaluation concepts, building on autonomous systems foundations.

---

*[End of Section 1.3]*


## Overview

Before the emergence of large language models and generative AI, the machine learning community developed sophisticated methods for evaluating predictive models—systems that classify inputs, predict numerical values, rank items, or detect patterns. These evaluation practices, refined over decades, represent some of the most rigorous empirical methodology in computer science. They provide essential foundations for AI evaluation while also illustrating, by contrast, what makes generative AI evaluation distinctively difficult.

Traditional ML evaluation rests on several assumptions that largely held for predictive models: that tasks have clear correct answers, that performance can be measured automatically against ground truth, that the space of possible outputs is bounded and enumerable, and that test data can be drawn from the same distribution as deployment data. When these assumptions hold, evaluation can be precise, reproducible, and scalable. When they don't—as is often the case for generative AI—traditional approaches break down.

This section surveys the core concepts of traditional ML evaluation, examines which elements transfer to generative AI, identifies where fundamental assumptions fail, and considers what adaptations might preserve the rigor of traditional approaches while accommodating generative AI's distinctive properties.

---

## Core Concepts

### The Hold-Out Principle

The most fundamental insight of ML evaluation is deceptively simple: don't evaluate on the data used for training. A model that has seen particular examples during training may memorize them rather than learn generalizable patterns. Evaluating on training data conflates memorization with genuine capability.

The hold-out principle addresses this by partitioning data into separate sets:

- **Training set**: Used to fit model parameters
- **Validation set**: Used to tune hyperparameters and make modeling decisions
- **Test set**: Used only for final evaluation, never seen during any part of model development

The test set must remain untouched until final evaluation. If test performance influences any modeling decisions, the test set becomes contaminated—it's no longer an unbiased estimate of performance on truly unseen data. This discipline requires organizational commitment: someone must control the test set and resist pressure to peek.

**Cross-validation** extends this principle by repeatedly partitioning data into training and validation sets. In k-fold cross-validation, data is divided into k subsets; each subset serves as validation data once while the remaining k-1 subsets serve as training data. This provides more robust performance estimates from limited data and reveals performance variance across different data splits.

The hold-out principle transfers directly to AI evaluation: benchmark contamination—where models are trained on benchmark data—is the generative AI equivalent of evaluating on training data. It produces inflated performance estimates that don't reflect genuine capability. Maintaining benchmark integrity requires the same discipline as maintaining test set integrity: separation, access control, and resistance to contamination.

### Performance Metrics

Traditional ML has developed rich vocabularies of performance metrics tailored to different task types:

**Classification metrics** evaluate models that assign inputs to discrete categories:

- **Accuracy**: Fraction of predictions that are correct. Simple but often misleading when classes are imbalanced.
- **Precision**: Of predictions for a class, what fraction are correct? High precision means few false positives.
- **Recall (Sensitivity)**: Of actual instances of a class, what fraction are correctly identified? High recall means few false negatives.
- **F1 Score**: Harmonic mean of precision and recall, balancing both concerns.
- **AUC-ROC**: Area under the receiver operating characteristic curve, measuring discrimination ability across classification thresholds.
- **Specificity**: True negative rate—of actual negatives, what fraction are correctly identified?

**Regression metrics** evaluate models that predict continuous values:

- **Mean Squared Error (MSE)**: Average squared difference between predictions and actual values. Penalizes large errors heavily.
- **Mean Absolute Error (MAE)**: Average absolute difference. More robust to outliers than MSE.
- **R² (Coefficient of Determination)**: Fraction of variance explained by the model.

**Ranking metrics** evaluate models that order items:

- **Precision@k**: Fraction of top-k items that are relevant.
- **Mean Average Precision (MAP)**: Average precision across recall levels.
- **Normalized Discounted Cumulative Gain (NDCG)**: Accounts for position in ranking, with higher positions weighted more heavily.

The choice of metric matters enormously. A model can excel on one metric while performing poorly on another. A spam filter with 99% accuracy might still be useless if it misses half of actual spam (low recall) or flags important emails (low precision). Metric selection should reflect what actually matters for the application.

For generative AI, the relationship between metrics and what matters is far less clear. What's the "precision" of a language model? What's the "recall" of a code assistant? Traditional metrics assume bounded, enumerable outputs with clear correctness criteria. Generative outputs resist this framing.

### Confusion Matrices and Error Analysis

A confusion matrix displays the full pattern of predictions versus actual values, revealing not just how often a model errs but how it errs. For binary classification:

|  | Predicted Positive | Predicted Negative |
|--|-------------------|-------------------|
| **Actual Positive** | True Positives (TP) | False Negatives (FN) |
| **Actual Negative** | False Positives (FP) | True Negatives (TN) |

Different cells have different costs. A medical diagnostic with false negatives (missed diseases) may be far worse than one with false positives (unnecessary follow-up tests). A fraud detection system might tolerate some false positives (flagged legitimate transactions) to minimize false negatives (missed fraud).

Error analysis goes beyond aggregate metrics to examine individual errors:

- Which examples does the model get wrong?
- Are there patterns in the errors?
- Do errors cluster in particular regions of the input space?
- Are some error types more costly than others?

This qualitative examination of failures often reveals more about model limitations than aggregate metrics alone. It might reveal that a model fails on particular demographic groups, struggles with certain input types, or has systematic blind spots.

For generative AI, error analysis is both more important and more difficult. More important because aggregate metrics are less meaningful—understanding failure modes requires examining specific outputs. More difficult because determining whether an output is an "error" often requires expert judgment, and categorizing errors into meaningful types is non-trivial. Still, the discipline of systematically examining failures, looking for patterns, and understanding error types is essential.

### Generalization and Overfitting

The core concern of ML evaluation is generalization: will the model perform well on new data, not just the data it was trained on? Overfitting occurs when a model learns patterns specific to the training data that don't hold more broadly—fitting noise rather than signal.

Signs of overfitting include:

- Large gap between training performance and validation/test performance
- Performance that degrades with more complex models
- Sensitivity to small changes in training data

Techniques to prevent or detect overfitting include:

- **Regularization**: Penalizing model complexity during training
- **Early stopping**: Halting training when validation performance stops improving
- **Cross-validation**: Assessing performance stability across different data splits
- **Learning curves**: Plotting performance against training set size to diagnose underfitting vs. overfitting

Generalization concerns apply to generative AI, but the manifestations differ. Traditional overfitting means memorizing training examples; for language models, this might manifest as regurgitating training text or performing better on prompts similar to training data. The benchmark-to-real gap is partly a generalization gap: models may learn to perform well on benchmark-style tasks without acquiring capabilities that transfer to real-world use.

### Fairness and Bias Evaluation

As ML systems have been deployed in consequential domains—hiring, lending, criminal justice, healthcare—concerns about fairness have prompted development of evaluation approaches for bias:

**Group fairness metrics** compare model behavior across demographic groups:

- **Demographic parity**: Predictions are distributed similarly across groups
- **Equalized odds**: True positive and false positive rates are equal across groups
- **Calibration**: Predicted probabilities mean the same thing across groups

**Individual fairness** asks whether similar individuals receive similar predictions, regardless of group membership.

**Disparate impact analysis** examines whether model use produces different outcomes for different groups, regardless of intent.

Fairness evaluation has revealed that models can encode and amplify societal biases present in training data. A hiring model trained on historical data may learn to discriminate against groups that faced past discrimination. A facial recognition system may perform worse on darker-skinned faces if training data overrepresented lighter-skinned faces.

These concerns apply with full force to generative AI—arguably more so, given the breadth of applications and the subtlety of potential biases. A language model may produce different quality outputs for different dialects, reflect stereotypes in its generations, or provide less accurate information about marginalized groups. Fairness evaluation for generative AI is less developed than for traditional ML, but the underlying concerns are at least as important.

### Distribution Shift

Traditional ML evaluation assumes that test data comes from the same distribution as training data—the independent and identically distributed (IID) assumption. In practice, this assumption often fails:

**Covariate shift**: The distribution of inputs changes between training and deployment. A model trained on daytime images may encounter nighttime images in deployment.

**Label shift**: The distribution of outputs changes. A disease classifier trained when a disease was rare may be deployed during an outbreak when it's common.

**Concept drift**: The relationship between inputs and outputs changes over time. Consumer preferences shift; fraud patterns evolve; language use changes.

**Domain shift**: Deployment context differs systematically from training context. A model trained on one hospital's data may be deployed at a different hospital with different patient populations and practices.

Evaluation under distribution shift requires:

- Testing on data from target distributions, not just source distributions
- Measuring performance across different conditions to understand robustness
- Monitoring for performance degradation over time as distributions drift
- Techniques like domain adaptation to improve transfer

For generative AI, distribution shift is pervasive. Benchmarks represent one distribution of tasks; real-world use represents another. Users prompt models in ways that differ from training data. The world changes, creating queries about events after training cutoffs. Evaluation must grapple with the gap between benchmark distributions and deployment distributions—a core reason why benchmark performance doesn't guarantee real-world utility.

### Baselines and Comparisons

Meaningful evaluation requires comparison to appropriate baselines:

- **Trivial baselines**: What performance would you get from simple rules? A model that always predicts the majority class achieves baseline accuracy equal to the majority class frequency. A model must beat this to demonstrate value.
- **Simple model baselines**: How does a complex model compare to a simpler one? If a deep neural network only slightly outperforms logistic regression, the complexity may not be justified.
- **Prior state-of-the-art**: How does a new model compare to previous best models?
- **Human performance**: How does the model compare to human experts?

Baseline comparisons prevent overclaiming. A model with 90% accuracy sounds impressive until you learn that the majority class baseline achieves 89%. A "breakthrough" model might only marginally improve on existing approaches.

Baseline discipline is essential for generative AI evaluation but often neglected. What's the appropriate baseline for an AI coding assistant? Productivity without any AI? Productivity with a previous generation model? Productivity with simpler tools like autocomplete? The choice of baseline dramatically affects conclusions about AI value. Many AI productivity claims lack rigorous baseline comparisons, making their magnitude difficult to interpret.

---

## What Transfers to AI Evaluation

Several elements of traditional ML evaluation transfer directly to generative AI:

**The hold-out principle** remains fundamental. Benchmark contamination—models training on benchmark data—produces misleading results just as evaluating on training data does. The discipline of keeping evaluation data separate from training data is as important for generative AI as for traditional ML, perhaps more so given the scale of training data and difficulty of detecting contamination.

**Multiple metrics** are essential because no single metric captures everything that matters. Traditional ML learned this through experience with accuracy being misleading for imbalanced classes. Generative AI evaluation requires multiple metrics for different quality dimensions: accuracy, helpfulness, safety, fluency, and more. Single-number benchmark scores obscure as much as they reveal.

**Error analysis discipline**—systematically examining failures to understand their patterns and causes—is directly applicable. Perhaps more applicable, since aggregate metrics are less informative for generative outputs. Understanding how and when AI fails requires looking at specific failure cases.

**Baseline comparisons** are essential for interpretable results. Claims about AI productivity or capability gains are meaningful only relative to specified baselines. Traditional ML's discipline of always comparing to appropriate baselines should be standard practice for AI evaluation.

**Fairness evaluation** concerns transfer directly. Generative AI can encode biases, produce disparate quality for different groups, and amplify societal inequities. Fairness evaluation methods need adaptation for generative outputs, but the underlying concerns and evaluation orientation apply fully.

**Distribution shift awareness** is directly relevant. The benchmark-to-real gap is substantially a distribution shift problem: benchmark tasks don't match real-world task distributions. Evaluation strategies for distribution shift—testing across conditions, monitoring deployment performance, measuring robustness—apply to generative AI.

---

## What Breaks for Generative AI

Despite these continuities, fundamental assumptions of traditional ML evaluation fail for generative AI:

**Bounded output space**: Classification produces one of k classes; regression produces a single number. Generative AI produces open-ended text, code, or other content with effectively unlimited possible outputs. The entire machinery of confusion matrices, classification metrics, and most standard evaluation approaches assumes bounded outputs.

**Clear ground truth**: Traditional ML evaluation assumes each input has a known correct answer—the label in supervised learning. Generative AI tasks often have no single correct answer. "Write an email to a colleague" has countless acceptable responses. "Explain quantum computing" can be done well in many different ways. Without ground truth, how do you measure accuracy?

**Automated evaluation**: Traditional ML metrics are fully automated—compute predictions, compare to labels, calculate metrics. Generative AI evaluation often requires human judgment. Is this summary accurate? Is this code good? Is this response helpful? Automated metrics exist but imperfectly capture what matters. This makes evaluation slower, more expensive, and more variable.

**Task specificity**: Traditional ML models are typically trained for specific tasks. Evaluation can focus on that task. Generative AI is general-purpose—the same model handles countless tasks. How do you evaluate a system whose task space is unbounded? No finite evaluation can cover all uses.

**Static models**: Traditional ML evaluation assumes a fixed model. Train, evaluate, deploy. Generative AI models may be updated continuously by providers, sometimes without notification. The model evaluated last month may not be the model deployed today. This challenges the basic logic of evaluation leading to deployment decisions.

**IID test data**: Traditional evaluation draws test data from the same distribution as training data. For generative AI, there's no clear "test distribution" that matches a "training distribution." User prompts are diverse, creative, and unpredictable. Benchmarks represent particular distributions that may not match real use.

**Clear input boundaries**: Traditional ML has defined input formats—images of certain dimensions, text of certain lengths, structured data with specified features. Generative AI accepts arbitrary text prompts, making the input space much harder to characterize or sample systematically.

---

## What Can Be Adapted

Between full transfer and complete breakdown, many traditional ML evaluation concepts can be adapted for generative AI:

**Stratified evaluation** assesses performance across different subgroups or conditions. Traditional ML might stratify by demographic group or input type. Generative AI evaluation can stratify by task category, difficulty level, domain, or prompt type. This reveals heterogeneity that aggregate metrics hide.

**Calibration assessment** checks whether model confidence matches actual accuracy. For traditional ML, this means calibrated probability predictions. For generative AI, this might mean assessing whether the model appropriately expresses uncertainty—does it say "I'm not sure" when it's likely to be wrong?

**Robustness testing** examines performance under perturbations. Traditional ML might add noise to inputs or use adversarial examples. Generative AI robustness testing might examine sensitivity to prompt variations, paraphrasing, or format changes. Do semantically equivalent prompts produce consistent outputs?

**Cross-validation principles** can inform evaluation design even when exact cross-validation isn't applicable. The core idea—assessing performance variance and avoiding overfitting to particular evaluation data—motivates using multiple benchmarks, diverse prompts, and varied evaluation conditions rather than relying on single evaluations.

**Leakage detection** techniques from ML can inform benchmark contamination detection. Methods for identifying whether a model has seen specific data during training can be adapted to assess whether generative models have trained on benchmark content.

**Ensemble evaluation** in traditional ML assesses multiple models and combines predictions. For generative AI, ensemble thinking suggests evaluating multiple models, comparing outputs, and using agreement or disagreement as a signal about reliability.

**Learning curve analysis** plots performance against resources (data, computation). For generative AI, analogous analyses might examine how performance scales with model size, prompt length, or few-shot examples, revealing capability trajectories and limits.

---

## Implications for AI Evaluation

Drawing on traditional ML evaluation while recognizing its limits, several principles should guide generative AI evaluation:

**Preserve the hold-out principle's intent.** Even if exact separation of training and test data isn't achievable, minimize benchmark contamination through benchmark versioning, contamination detection, and fresh evaluation tasks. The spirit of unbiased evaluation on truly unseen examples remains essential.

**Use multiple metrics and examine trade-offs.** No single metric captures generative AI quality. Use multiple metrics assessing different dimensions. Examine trade-offs—improvements on one metric may come at cost to others. Resist reducing evaluation to single scores.

**Invest in error analysis.** Systematic examination of failures reveals more than aggregate metrics. Build processes for sampling outputs, identifying errors, categorizing failure types, and understanding patterns. This requires human judgment and cannot be fully automated.

**Compare to meaningful baselines.** Every capability or productivity claim should specify its baseline. Gains relative to no AI differ from gains relative to previous AI differ from gains relative to alternative tools. Make baselines explicit and choose them thoughtfully.

**Evaluate across conditions.** Stratify evaluation by task type, difficulty, domain, and user characteristics. Aggregate results hide important heterogeneity. Understanding where AI works well and where it doesn't is more useful than knowing average performance.

**Expect distribution mismatch.** Benchmarks don't match real-world distributions. Don't assume benchmark performance predicts deployment performance. Plan for validation against operational data. Investigate gaps between benchmark and real-world results.

**Account for evaluation limitations.** Traditional ML evaluation can be precise; generative AI evaluation is inherently messier. Human judgments vary. Automated metrics imperfectly capture quality. Sample sizes are often limited. Report uncertainty. Acknowledge limitations. Resist false precision.

**Develop new methods, not just adapt old ones.** Traditional ML evaluation is a foundation but not a complete solution. Generative AI's distinctive properties—unbounded outputs, open-ended tasks, general-purpose application—require new evaluation approaches that the field is still developing.

---

## Key References

**Foundational Texts**

- **Hastie, T., Tibshirani, R., & Friedman, J. (2009). *The Elements of Statistical Learning* (2nd ed.).** Comprehensive treatment of statistical learning with extensive coverage of model evaluation and validation.

- **James, G., Witten, D., Hastie, T., & Tibshirani, R. (2013). *An Introduction to Statistical Learning*.** More accessible introduction to the same topics, with practical focus.

- **Bishop, C.M. (2006). *Pattern Recognition and Machine Learning*.** Rigorous treatment of ML fundamentals including evaluation methodology.

- **Murphy, K.P. (2012). *Machine Learning: A Probabilistic Perspective*.** Comprehensive reference with strong coverage of evaluation methods.

**Metrics and Evaluation**

- **Japkowicz, N., & Shah, M. (2011). *Evaluating Learning Algorithms: A Classification Perspective*.** Book-length treatment of classification evaluation methodology.

- **Ferri, C., Hernández-Orallo, J., & Modroiu, R. (2009). "An Experimental Comparison of Performance Measures for Classification." *Pattern Recognition Letters*.** Systematic comparison of classification metrics.

- **Caruana, R., & Niculescu-Mizil, A. (2006). "An Empirical Comparison of Supervised Learning Algorithms." *ICML*.** Influential comparison study demonstrating methodology.

**Cross-Validation and Model Selection**

- **Kohavi, R. (1995). "A Study of Cross-Validation and Bootstrap for Accuracy Estimation and Model Selection." *IJCAI*.** Classic empirical study of validation methods.

- **Varma, S., & Simon, R. (2006). "Bias in Error Estimation When Using Cross-Validation for Model Selection." *BMC Bioinformatics*.** Analysis of potential biases in cross-validation.

**Fairness and Bias**

- **Barocas, S., Hardt, M., & Narayanan, A. (2019). *Fairness and Machine Learning: Limitations and Opportunities*.** Comprehensive treatment of fairness in ML, available at fairmlbook.org.

- **Mehrabi, N., Morstatter, F., Saxena, N., Lerman, K., & Galstyan, A. (2021). "A Survey on Bias and Fairness in Machine Learning." *ACM Computing Surveys*.** Survey of bias types and mitigation approaches.

- **Mitchell, M., et al. (2019). "Model Cards for Model Reporting." *FAT*.** Framework for documenting model characteristics including fairness considerations.

**Distribution Shift and Robustness**

- **Quiñonero-Candela, J., Sugiyama, M., Schwaighofer, A., & Lawrence, N.D. (Eds.). (2009). *Dataset Shift in Machine Learning*.** Collection addressing distribution shift challenges.

- **Koh, P.W., et al. (2021). "WILDS: A Benchmark of In-the-Wild Distribution Shifts." *ICML*.** Benchmark specifically targeting distribution shift evaluation.

- **Hendrycks, D., & Dietterich, T. (2019). "Benchmarking Neural Network Robustness to Common Corruptions and Perturbations." *ICLR*.** Methodology for robustness evaluation.

**Bridging to Generative AI**

- **Ribeiro, M.T., Wu, T., Guestrin, C., & Singh, S. (2020). "Beyond Accuracy: Behavioral Testing of NLP Models with CheckList." *ACL*.** Applies software testing concepts to NLP evaluation.

- **Liang, P., et al. (2022). "Holistic Evaluation of Language Models (HELM)." *arXiv preprint*.** Comprehensive framework attempting to bring traditional ML evaluation rigor to language models.

- **Chang, Y., et al. (2023). "A Survey on Evaluation of Large Language Models." *arXiv preprint*.** Survey of emerging evaluation approaches for large language models.

---

## Connections to Other Sections

Traditional ML evaluation connects to several other disciplines covered in this appendix:

- **Section 1.1 (Software Testing)** provides foundational concepts of systematic testing that ML evaluation builds upon; the hold-out principle parallels test suite discipline.

- **Section 1.3 (Autonomous Systems)** applies ML evaluation to learned components within autonomous systems, adding operational context.

- **Section 2.1 (Experimental Design)** provides the statistical foundations for ML evaluation methodology, including cross-validation theory.

- **Section 2.2 (Psychometrics)** offers measurement theory concepts (reliability, validity) that inform how we think about ML evaluation quality.

- **Section 2.3 (Econometrics)** provides causal inference methods applicable when ML evaluation needs to support causal claims.

- **Section 6.1 (AI Safety Evaluation)** builds on traditional ML evaluation while developing methods specific to safety-relevant properties.

- **Section 6.3 (Educational Measurement)** offers parallel experience with high-stakes testing, including test security and score validity concerns analogous to benchmark contamination.

---

*[End of Section 1.4]*


## Overview

Cybersecurity testing represents one of the most adversarially mature evaluation disciplines. For decades, security professionals have grappled with a fundamental challenge that resonates deeply with AI evaluation: how do you assess a system against attackers whose methods are unknown, constantly evolving, and deliberately designed to find weaknesses you haven't anticipated?

The security field's answer has been to develop an adversarial evaluation culture—one where the goal is not merely to confirm that systems work under expected conditions, but to actively discover how they can be made to fail. Red teaming, penetration testing, bug bounties, and threat modeling all embody this adversarial mindset. They assume that the most important failures are the ones you haven't thought of yet, and they create structured approaches for thinking the unthinkable.

For AI evaluation, cybersecurity provides both methods and mindset. The methods—structured red teaming, threat modeling, fuzzing, responsible disclosure—can be adapted for AI safety evaluation. The mindset—assume adversaries exist, assume you've missed something, design for resilience not just prevention—may be even more valuable. AI systems face not just malicious adversaries but also the ordinary creativity of users who will inevitably push systems in unanticipated directions.

This section surveys key concepts from cybersecurity testing, examines how they apply to AI evaluation, identifies where the security paradigm breaks down, and draws implications for AI evaluation practice.

---

## Core Concepts

### Red Team / Blue Team / Purple Team

The red team/blue team model divides security evaluation into distinct adversarial roles:

**Red teams** are authorized attackers who attempt to find and exploit vulnerabilities. Their job is to think like adversaries—identify weaknesses, develop exploits, and demonstrate what a real attacker could achieve. Red teams operate under rules of engagement that scope their activities but within those bounds try to be as creative and persistent as real attackers.

**Blue teams** are defenders responsible for protecting systems, detecting attacks, and responding to incidents. They represent the organization's actual security posture and capabilities.

**Purple teams** facilitate collaboration between red and blue, ensuring that red team findings translate into improved defenses. Rather than simply revealing vulnerabilities and moving on, purple team activities focus on learning and improvement.

This tripartite model creates productive tension. Red teams provide independent, adversarial assessment unconstrained by defensive assumptions. Blue teams provide real-world defensive context. Purple teams ensure the adversarial findings actually improve security rather than just documenting it.

For AI, the red team concept has been directly adopted. AI red teaming involves adversarial probing for harmful outputs, jailbreaking attempts, and systematic exploration of failure modes. The red team framing emphasizes that evaluation should actively try to make the AI fail—not just confirm it works in expected cases—and that this adversarial probing provides information that cooperative testing cannot.

### Penetration Testing

Penetration testing ("pentesting") is a structured methodology for authorized attack simulation:

1. **Scoping**: Define what systems are in scope, what techniques are permitted, and what success looks like
2. **Reconnaissance**: Gather information about the target system
3. **Vulnerability identification**: Find potential weaknesses
4. **Exploitation**: Attempt to exploit identified vulnerabilities
5. **Post-exploitation**: Assess what an attacker could do after initial compromise
6. **Reporting**: Document findings, severity, and recommendations

Penetration testing is bounded and authorized—testers have explicit permission to attack within defined scope. This distinguishes it from actual attacks and enables organizations to learn from simulated attacks without actual harm.

The structured pentesting methodology offers a template for AI evaluation. Scoping parallels defining what AI capabilities and behaviors are being evaluated. Reconnaissance parallels understanding how the AI system works—its interfaces, capabilities, and potential attack surfaces. Vulnerability identification parallels finding prompts, contexts, or inputs that might produce undesired outputs. Exploitation parallels demonstrating that these vulnerabilities can actually produce harmful results. Reporting parallels documenting AI failure modes, their severity, and recommendations for mitigation.

### Threat Modeling

Before testing for specific vulnerabilities, security practitioners engage in threat modeling—systematic identification of potential threats:

**Who might attack?** Different adversaries have different motivations, capabilities, and resources. A nation-state actor poses different threats than a curious teenager or a disgruntled employee.

**What are their goals?** Data theft, system disruption, financial fraud, reputation damage, or something else? Understanding adversary goals helps prioritize defenses.

**What methods might they use?** Known attack patterns, novel techniques, social engineering, supply chain compromise, insider threats? The attack surface encompasses all paths an adversary might exploit.

**What assets need protection?** Not everything is equally valuable or vulnerable. Prioritize based on asset value and exposure.

Threat models inform both defensive architecture and testing priorities. Testing should focus on likely and consequential threats, not just easy-to-test scenarios.

For AI, threat modeling asks: Who might try to make the AI behave badly? Malicious users seeking harmful content, competitors seeking embarrassment, researchers probing for weaknesses, or ordinary users who stumble into problematic areas? What might they try to achieve? Generating harmful content, extracting training data, manipulating the AI's behavior, or bypassing safety measures? Threat modeling for AI helps prioritize red team activities and evaluation resources.

### Bug Bounties and Responsible Disclosure

Bug bounty programs enlist external researchers to find vulnerabilities in exchange for rewards. They leverage a global community of security researchers who may find vulnerabilities that internal teams miss:

**Advantages**: Diverse perspectives, scalable effort, real-world adversarial skill, cost-effective (pay only for results)

**Challenges**: Managing submissions, avoiding exploitation of found vulnerabilities, defining scope and severity, potential for noise

**Responsible disclosure** refers to coordinated practices for reporting vulnerabilities: researchers notify vendors before public disclosure, vendors have time to develop fixes, and disclosure occurs in ways that minimize harm.

Bug bounty models are emerging for AI. Programs like the DEFCON AI Village and various company-sponsored initiatives invite researchers to find AI vulnerabilities. The challenge is defining what counts as an AI "vulnerability"—security vulnerabilities have relatively clear definitions, while AI failure modes are often fuzzier. Still, crowdsourcing failure discovery can find problems internal testing misses.

### Zero-Day Vulnerabilities and Unknown Unknowns

A "zero-day" vulnerability is one unknown to defenders at the time of exploitation—the defenders have "zero days" of warning. Zero-days represent the scariest class of security threats: you can't defend against what you don't know exists.

The security field has developed several responses to unknown unknowns:

**Defense in depth**: Don't rely on any single protection. Layer multiple defenses so that if one fails, others remain. Assume breaches will occur and limit their impact.

**Anomaly detection**: Rather than only detecting known bad patterns, look for deviations from normal behavior. Unknown attacks may still produce detectable anomalies.

**Assume breach**: Design systems and processes assuming that compromise is inevitable. Limit lateral movement, segment networks, encrypt data at rest, and plan incident response.

**Resilience over prevention**: Since perfect prevention is impossible, prioritize resilience—the ability to continue functioning and recover quickly even when attacks succeed.

For AI, zero-day thinking is essential. The "jagged capability frontier" means AI systems fail in unexpected ways that weren't anticipated during development or testing. No testing can enumerate all possible failure modes. Assume that deployed AI will fail in ways you haven't predicted. Design for detection, containment, and recovery, not just prevention.

### Security Testing Automation

Security testing uses various automated techniques to explore large input spaces:

**Fuzzing**: Automatically generating semi-random inputs to find inputs that cause crashes, hangs, or unexpected behavior. Fuzzing doesn't require understanding of specific vulnerabilities—it explores the input space looking for anything that breaks.

**Static analysis**: Examining code without executing it to find potential vulnerabilities—buffer overflows, injection vulnerabilities, insecure patterns. Scales well but may miss runtime-dependent issues.

**Dynamic analysis**: Examining system behavior during execution—memory access patterns, API calls, network traffic. Catches runtime issues but requires actually running the code.

**Symbolic execution**: Systematically exploring program paths to find inputs that reach specific states. More thorough than fuzzing but computationally expensive.

For AI, fuzzing concepts translate to automated prompt exploration—systematically trying many prompt variations to find inputs that produce undesired outputs. The challenge is defining what "crash" or "unexpected behavior" means for AI; the output is always some text, so identifying problematic outputs requires either human judgment or automated classifiers.

---

## What Transfers to AI Evaluation

Several elements of cybersecurity testing apply directly to AI evaluation:

**The adversarial mindset** is perhaps the most valuable transfer. Security testing assumes you need to actively try to break the system because the most important failures are the ones you haven't anticipated. This orientation—adversarial rather than cooperative—provides different information than testing whether AI performs well on expected inputs. AI evaluation should include adversarial components as standard practice.

**Red teaming methodology** provides structured approaches for adversarial evaluation. The practices of scoping red team engagements, defining rules of engagement, documenting findings, and tracking remediation can be adapted for AI red teaming. The key insight is that red teaming should be structured and systematic, not just ad hoc probing.

**Threat modeling** helps prioritize evaluation effort. Rather than treating all possible AI failures as equally likely or important, threat modeling asks: What failures are most likely? What failures would be most consequential? What adversary capabilities should we assume? This risk-based prioritization makes evaluation tractable.

**Bug bounty models** offer approaches for crowdsourcing failure discovery. Internal teams may miss failure modes that external researchers find. Creating mechanisms for responsible disclosure of AI failures—with appropriate incentives—can augment internal evaluation.

**Defense in depth** applies to AI deployment. Don't rely on the model itself to prevent all harms. Layer additional protections: output filters, use policies, monitoring, human review for high-stakes outputs. Assume some failures will occur and design systems that limit their impact.

**Unknown unknowns awareness** is essential for AI. Security professionals have long experience with unforeseen vulnerabilities and have developed strategies for managing this uncertainty. AI evaluation should expect unexpected failure modes and prioritize detection and recovery alongside prevention.

---

## What Breaks for Generative AI

Despite substantial applicability, some aspects of security testing translate poorly to AI:

**Clear vulnerability definitions** exist in security: unauthorized access, data exposure, code execution, denial of service. These have relatively crisp definitions—either the attacker achieved the goal or didn't. AI "failures" are often fuzzy: Is this response harmful? Is this output good enough? Is this behavior acceptable? The fuzziness makes it harder to determine whether a "vulnerability" exists.

**Exploit reproducibility** is typically high in security—the same vulnerability reliably produces the same exploit. AI jailbreaks may be stochastic: a prompt that produces harmful output once might not do so consistently. This variability complicates both discovery and remediation. A "fix" might reduce harmful output probability without eliminating it.

**Patching vulnerabilities** is possible for traditional software—fix the bug, deploy the patch. AI weaknesses may be more fundamental, emerging from training data or model architecture in ways that can't be simply patched. Mitigations (output filters, system prompts) may address symptoms without fixing underlying issues, and may introduce new failure modes.

**Formal security properties** can sometimes be verified—cryptographic correctness, access control logic, protocol compliance. AI safety properties generally cannot be formally verified. There's no way to prove that a language model will never produce harmful content, only to test extensively and monitor continuously.

**Clear attack surface** can be defined for traditional systems—network interfaces, APIs, user inputs. AI "attack surface" is less clear. Any input can potentially produce undesired output. The boundary between normal use and adversarial use is blurry.

---

## What Can Be Adapted

Several security concepts can be adapted for AI evaluation with appropriate modifications:

**Structured red teaming frameworks** can be developed for AI. Define scope (what capabilities/behaviors are being tested), rules of engagement (what methods are permitted), deliverables (how findings are documented), and follow-up (how issues are addressed). The DEFCON AI Village CTFs and various industry frameworks are early examples.

**Fuzzing for AI** can involve systematic exploration of the prompt space. Rather than completely random inputs, informed fuzzing can focus on prompt patterns likely to produce problematic outputs—drawing on known jailbreaks, adversarial prompt patterns, and edge cases. Automated generation and screening can scale this exploration.

**Coordinated disclosure for AI** can be developed—practices for responsibly reporting AI failures, allowing developers time to address issues before public disclosure. This requires defining what constitutes an AI "vulnerability" worth reporting, establishing channels for reports, and creating norms around disclosure timing.

**Capture the flag for AI** adapts the security CTF competition format. Competitions where teams try to find AI failures, generate specific outputs, or bypass safety measures can motivate creative adversarial evaluation and develop the community of AI red teamers.

**Assume breach for AI** translates to assuming AI will produce some problematic outputs. Design deployment contexts accordingly: monitoring for problematic outputs, limiting where AI outputs go without human review, and having response plans for when issues arise.

---

## Implications for AI Evaluation

Drawing on cybersecurity testing experience, several principles should guide AI evaluation:

**Adopt the adversarial orientation.** Don't just test whether AI performs well on expected uses; actively try to make it fail. Adversarial testing reveals different information than cooperative testing. For high-stakes deployments, adversarial evaluation is not optional.

**Structure adversarial evaluation.** Ad hoc probing misses things. Use structured red teaming with defined scope, methodology, documentation, and follow-up. Adapt penetration testing frameworks for AI context.

**Apply threat modeling.** Before testing everything, think about what failures are most likely and most consequential. Prioritize evaluation based on risk. Consider who might try to misuse the AI and how.

**Consider crowdsourcing.** Internal teams may miss failures that external researchers find. Bug bounty programs, research collaborations, and community engagement can augment internal evaluation—if managed carefully.

**Design for resilience.** Since perfect prevention is impossible, design AI deployments that can detect, contain, and recover from failures. Defense in depth, monitoring, and response plans are as important as pre-deployment testing.

**Expect the unexpected.** Zero-day thinking applies to AI: assume that deployed systems will fail in ways not anticipated during testing. Build monitoring and response capabilities, not just testing.

**Develop the community.** Security has a mature community of researchers, practitioners, and institutions. AI evaluation needs similar infrastructure: shared methodologies, training programs, career paths, and ethical norms.

---

## Key References

**Security Testing Foundations**

- **NIST SP 800-115 (Technical Guide to Information Security Testing and Assessment).** Government guidance on security testing methodology.

- **PTES (Penetration Testing Execution Standard).** Industry standard for penetration testing methodology and reporting.

- **MITRE ATT&CK Framework.** Knowledge base of adversary tactics, techniques, and procedures organized as a taxonomy.

- **OWASP Testing Guide.** Comprehensive guide to web application security testing.

**Threat Modeling**

- **Shostack, A. (2014). *Threat Modeling: Designing for Security*.** Comprehensive treatment of threat modeling methods.

- **STRIDE Threat Model.** Microsoft's framework for categorizing security threats.

**AI Red Teaming**

- **Ganguli, D., et al. (2022). "Red Teaming Language Models to Reduce Harms." *arXiv preprint*.** Anthropic's description of red teaming methodology.

- **Perez, E., et al. (2022). "Red Teaming Language Models with Language Models." *arXiv preprint*.** Using AI to automate red teaming.

- **Brundage, M., et al. (2020). "Toward Trustworthy AI Development: Mechanisms for Supporting Verifiable Claims."** Broader framework for AI assurance including adversarial testing.

- **Anthropic, OpenAI, DeepMind responsible scaling policies and safety documentation.** Industry practices for AI red teaming.

**Bug Bounties and Disclosure**

- **HackerOne and Bugcrowd.** Major bug bounty platforms with methodology documentation.

- **ISO/IEC 29147 and 30111.** Standards for vulnerability disclosure and handling.

---

## Connections to Other Sections

Cybersecurity testing connects to several other disciplines covered in this appendix:

- **Section 1.1 (Software Testing)** provides foundational testing concepts; cybersecurity extends these with an adversarial orientation that's particularly relevant to AI.

- **Section 4.1 (Risk Analysis)** provides frameworks for the risk-based prioritization that informs threat modeling and test prioritization.

- **Section 4.5 (Safety Engineering)** develops hazard analysis methods that complement adversarial security analysis for safety-critical AI.

- **Section 6.1 (AI Safety Evaluation)** covers the emerging field of AI-specific safety evaluation, which draws heavily on security red teaming concepts.

- **Section 1.3 (Autonomous Systems)** addresses adversarial testing in the context of physically embodied AI systems.

---

*[End of Section 1.5]*


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


## Section 3.1: Information Systems Economics

### Overview

Information Systems (IS) economics studies how information technology affects organizations and economies. This field has decades of experience grappling with a puzzle directly relevant to AI: technology that seems transformative often fails to produce measurable productivity gains, at least initially. The "IT productivity paradox"—visible computing power everywhere except in productivity statistics—provides crucial context for understanding why AI productivity gains may be slower and harder to measure than anticipated.

### Core Concepts

**The IT Productivity Paradox**

Economist Robert Solow's 1987 observation—"You can see the computer age everywhere but in the productivity statistics"—captured a genuine puzzle. Organizations invested heavily in information technology, yet aggregate productivity growth remained sluggish. Computers were ubiquitous; their economic payoff was invisible.

The paradox was eventually resolved through several insights:

1. **Measurement problems**: Productivity statistics may not capture IT benefits, particularly in service sectors where output is hard to define.

2. **Time lags**: IT benefits require learning, reorganization, and complementary investments. Benefits materialize years after technology deployment.

3. **Redistribution vs. creation**: Some IT gains represent competitive redistribution (market share shifts) rather than aggregate productivity creation.

4. **Mismeasured quality**: IT improves product quality and variety in ways productivity statistics miss.

For AI, the IT productivity paradox offers a warning: don't expect immediate measured productivity gains. The mechanisms that delayed IT payoffs—learning curves, organizational adjustment, measurement challenges—likely apply to AI as well.

**Complementary Investments**

Erik Brynjolfsson's research demonstrated that IT investments alone don't produce productivity gains. Complementary investments are required:

- **Organizational restructuring**: New processes that leverage IT capabilities
- **Human capital**: Training workers to use technology effectively
- **Changed incentives**: Aligning rewards with new ways of working
- **Business process redesign**: Fundamentally rethinking how work is done

Organizations that made these complementary investments saw IT gains; those that simply added computers to existing processes often didn't.

For AI, this insight is crucial. AI tools dropped into unchanged workflows may show limited benefits. Realizing AI's potential likely requires rethinking how work is organized—what tasks AI handles, how humans supervise, how quality is ensured. Organizations expecting AI to boost productivity without complementary changes may be disappointed.

**Task-Technology Fit**

The task-technology fit framework holds that performance depends on the match between task characteristics and technology capabilities. Not all tasks benefit equally from a given technology. IT might dramatically improve some tasks while providing little benefit for others.

For AI, task-technology fit explains heterogeneous effects. AI may provide large benefits for routine knowledge work (drafting, summarizing, coding boilerplate) while providing little benefit for tasks requiring judgment, creativity, or tacit knowledge. Evaluation should examine fit across different task types rather than assuming uniform effects.

**IT Business Value**

Research on IT business value distinguishes:

- **Process-level impacts**: IT improves specific business processes
- **Firm-level impacts**: IT affects overall firm performance
- **Intermediate measures**: Efficiency, productivity, quality
- **Ultimate outcomes**: Profitability, market value, competitive position

The relationship between levels isn't straightforward. Process improvements may not aggregate to firm improvements if processes aren't strategically important or if competitors gain similar advantages.

For AI, this multi-level framing suggests measuring impacts at appropriate levels. Task-level AI benefits may not translate to firm-level benefits. Productivity improvements may not translate to profitability if AI is equally available to competitors.

### What Transfers to AI Evaluation

**Productivity paradox awareness**: Don't expect immediate measured productivity gains from AI. Historical experience with IT suggests significant lags.

**Complementary investments**: AI gains likely require organizational changes beyond deploying tools. Evaluate whether complementary investments are being made.

**Task-technology fit**: AI will help some tasks more than others. Identify where fit is good.

**Multi-level measurement**: Measure impacts at multiple levels—task, process, firm. Effects may differ across levels.

### What Breaks for Generative AI

**Slower IT change**: Historical IT changed more slowly than AI, allowing more time for organizational adjustment. AI pace is faster.

**Clearer IT capabilities**: IT capabilities were more predictable; organizations could plan around them. AI capabilities are surprising and uncertain.

### Implications for AI Evaluation

- **Budget time for AI benefits to materialize.** Short-term evaluations may underestimate long-term potential.
- **Assess complementary investments.** Are organizations changing processes, training workers, redesigning workflows?
- **Measure at multiple levels.** Task improvements may not aggregate upward.
- **Consider task-technology fit.** Examine where AI fits well and poorly.

### Key References

- **Brynjolfsson, E. (1993). "The Productivity Paradox of Information Technology." *Communications of the ACM*.** Classic statement of the IT productivity paradox.

- **Brynjolfsson, E., & Hitt, L. (2000). "Beyond Computation: Information Technology, Organizational Transformation, and Business Performance." *Journal of Economic Perspectives*.** Resolution of the paradox through complementary investments.

- **Melville, N., Kraemer, K., & Gurbaxani, V. (2004). "Review: Information Technology and Organizational Performance: An Integrative Model." *MIS Quarterly*.** Comprehensive review of IT business value research.

---

## Section 3.2: Productivity Measurement and Economics

### Overview

Productivity—output per input—sounds simple but becomes deeply complex upon examination. What counts as output? How do you measure it? What inputs should be considered? For knowledge work, these questions have no easy answers. For AI's effect on knowledge work, they become even harder.

Understanding productivity measurement is essential for interpreting AI productivity claims. A 15% productivity gain means very different things depending on how productivity was measured.

### Core Concepts

**Productivity Definitions**

**Labor productivity** measures output per worker or per hour worked. It's the most commonly cited productivity measure but attributes all output changes to labor, ignoring other inputs.

**Total Factor Productivity (TFP)** or **Multifactor Productivity (MFP)** measures output growth not explained by growth in measured inputs (labor, capital). TFP captures technological progress, efficiency improvements, and unmeasured factors.

**Task-level productivity** measures output for specific tasks (documents written, code produced). This is easier to measure but may miss important aspects of work.

**Process-level productivity** measures efficiency of business processes. More comprehensive than task-level but still may not capture strategic contribution.

**Output Measurement Challenges**

Manufacturing output is relatively clear: count the units produced. Service and knowledge work output is far harder:

**What's the output of analysis?** The document? The insights? The decisions informed? The outcomes of those decisions?

**How do you count heterogeneous outputs?** If a worker produces three short documents and one long one, versus four medium ones, who was more productive?

**How do you account for quality?** If AI enables producing twice as many documents at half the quality, is that a productivity gain?

Quality adjustment is particularly challenging. Simple output counts may increase while quality decreases—a spurious "productivity gain" that actually represents degradation.

**Input Measurement**

**Hours worked** is a common labor input measure but doesn't capture effort, skill, or attention.

**Capital input** for AI might include compute costs, software licenses, and training time. These are hard to measure consistently.

**Unmeasured inputs** like tacit knowledge, organizational routines, and data quality affect productivity but rarely appear in measurement.

**Aggregation Issues**

**Composition effects**: If high-productivity workers adopt AI more, aggregate productivity rises even if AI doesn't help anyone—just shifts the mix.

**Level of analysis**: Task-level gains may not aggregate to firm-level gains if tasks aren't strategically important or if gains are competed away.

**Baumol's cost disease**: In sectors where productivity growth is slow (much of services), costs rise relative to high-productivity-growth sectors, even without performance decline.

**Time Horizons**

**Short-run effects** may include learning curves, adjustment costs, and disruption—potentially negative initial effects before benefits materialize.

**Long-run effects** may include process redesign, skill development, and organizational adaptation that amplify initial gains.

**Transition dynamics** between short and long run may be complex and non-monotonic.

### What Transfers to AI Evaluation

**Output measurement awareness**: AI productivity claims require credible output measures. What exactly is being measured?

**Quality adjustment**: More output isn't necessarily better. How is quality accounted for?

**Aggregation concerns**: Task-level gains may not aggregate to higher levels.

**Time horizon**: Short-term effects may differ from long-term effects.

### What Breaks for Generative AI

**Clear output for AI-assisted work**: Even harder to define than typical knowledge work. What's the "output" of AI-assisted writing?

**Quality assessment**: Subtle quality dimensions may be affected by AI in ways not captured by standard measures.

**Rapid change**: AI effects may change faster than standard productivity measurement can track.

### Implications for AI Evaluation

- **Define output measures carefully and acknowledge their limitations.** Be explicit about what's being measured.
- **Adjust for quality or acknowledge you're not.** Raw output counts without quality adjustment may mislead.
- **Don't assume task-level gains aggregate.** Benefits for specific tasks may not translate to broader productivity.
- **Allow for time dynamics.** Short-term effects may differ from long-term.

### Key References

- **Syverson, C. (2011). "What Determines Productivity?" *Journal of Economic Literature*.** Comprehensive review of productivity economics.

- **Nordhaus, W.D. (2007). "Two Centuries of Productivity Growth in Computing." *Journal of Economic History*.** Historical perspective on computing productivity.

- **Brynjolfsson, E., Rock, D., & Syverson, C. (2021). "The Productivity J-Curve: How Intangibles Complement General Purpose Technologies." *American Economic Journal: Macroeconomics*.** Theoretical framework for understanding productivity lags.

---

## Section 3.3: Cost Analysis and Investment Evaluation

### Overview

Cost analysis and investment evaluation provide frameworks for assessing whether AI investments make economic sense. Beyond productivity effects, organizations need to understand full costs, expected benefits, risks, and the value of flexibility in uncertain environments.

### Core Concepts

**Total Cost of Ownership (TCO)**

TCO encompasses all costs over a system's lifetime:

**Direct costs**: Licensing, compute, API calls, infrastructure

**Implementation costs**: Integration, customization, deployment

**Training costs**: User training, prompt engineering development

**Ongoing costs**: Maintenance, updates, quality assurance, human oversight

**Hidden costs**: Increased review time, fixing AI errors, productivity losses during learning

AI TCO is often underestimated. API costs scale with usage in unpredictable ways. Quality assurance for AI outputs requires ongoing human time. Learning curves impose initial productivity costs.

**Cost-Benefit Analysis (CBA)**

CBA compares costs and benefits in common units (typically money):

**Net Present Value (NPV)**: Discounted benefits minus discounted costs

**Benefit-cost ratio**: Benefits divided by costs

**Challenges**: Quantifying intangible benefits, handling uncertainty, choosing discount rates

For AI, benefit quantification is particularly difficult. If AI makes workers "more creative" or "more satisfied," how do you monetize that? If AI increases risk of errors, how do you quantify the cost?

**Return on Investment (ROI)**

ROI expresses benefits as a ratio to investment. Simple and intuitive, but:

- Ignores timing (fast payback vs. slow payback)
- Requires quantifying benefits
- May not capture strategic value

AI ROI calculations are fraught because benefits are hard to quantify and risks are hard to bound.

**Real Options Analysis**

Traditional CBA assumes commit-or-don't decisions. Real options recognizes that investments create future options: to expand if things go well, to abandon if they don't, to wait for more information.

AI investments often have option value:
- Start with limited pilot, option to expand
- Maintain flexibility across AI providers
- Build capabilities that enable future applications

In uncertain environments, flexibility has value beyond immediate returns.

**Learning Curves**

Costs typically decrease with experience as learning accumulates:
- Users become more proficient
- Processes become optimized
- Best practices emerge

Early AI costs may not reflect steady-state costs. Learning curves suggest initial costs overstate long-run costs, while initial benefits understate long-run benefits.

**Sunk Costs and Lock-in**

Sunk costs are irrelevant to future decisions—but psychologically powerful. "We've invested so much" shouldn't justify continued investment if prospects are poor.

**Lock-in** occurs when switching costs make changing course expensive:
- Vendor lock-in: Dependence on specific AI provider
- Process lock-in: Workflows redesigned around AI
- Skill lock-in: Training specific to particular tools

Lock-in concerns favor maintaining flexibility where practical.

### What Transfers to AI Evaluation

**TCO thinking**: Account for full costs including hidden costs like quality assurance and learning time.

**Uncertainty handling**: AI benefits are highly uncertain; use ranges and scenarios rather than point estimates.

**Option value**: Flexibility has value. Staged investments preserve options.

**Learning curves**: Early performance may not reflect long-run performance.

**Lock-in awareness**: Consider switching costs and dependency risks.

### Implications for AI Evaluation

- **Account for full costs** including training, QA, adaptation, and oversight.
- **Acknowledge benefit uncertainty** using ranges and scenarios rather than false precision.
- **Value flexibility** by considering staged approaches that preserve options.
- **Consider learning curves** when interpreting early results.
- **Evaluation costs are part of TCO.** Budget for ongoing evaluation as a cost of responsible AI deployment.

### Key References

- **Ellram, L.M. (1995). "Total Cost of Ownership: An Analysis Approach for Purchasing." *Journal of Physical Distribution & Logistics Management*.** Foundational TCO framework.

- **Boardman, A.E., et al. (2017). *Cost-Benefit Analysis: Concepts and Practice* (5th ed.).** Comprehensive CBA textbook.

- **Dixit, A.K., & Pindyck, R.S. (1994). *Investment Under Uncertainty*.** Classic treatment of real options.

---

*[End of Section 3]*


## Section 4.1: Risk Analysis and Management

### Overview

Risk analysis and management provide systematic approaches to identifying, assessing, and managing uncertainty and potential harms. For AI evaluation, risk frameworks inform prioritization—where should limited evaluation resources focus?—and help characterize residual uncertainty that remains even after evaluation.

### Core Concepts

**Risk Identification**

The first step in risk management is identifying what could go wrong:

**Hazard analysis** systematically identifies conditions that could lead to harm. For AI, hazards might include: incorrect outputs accepted as correct, biased outputs affecting decisions, system unavailability at critical moments, privacy violations, or adversarial misuse.

**Threat modeling** (from cybersecurity) identifies potential adversaries and attack vectors. For AI: Who might try to make the system behave badly? How might they try?

**Historical analysis** examines past incidents for patterns. AI is too new for deep historical record, but emerging incident databases begin to catalog AI failures.

**Brainstorming and checklists** supplement systematic methods. Checklists of known AI failure modes prompt consideration of specific risks.

**Risk Assessment**

Once identified, risks must be assessed:

**Probability × Impact** is the classic framework. Risk severity = likelihood of occurrence × consequence if it occurs. This produces a single number for comparison.

**Qualitative assessment** (high/medium/low) is simpler but supports less precise prioritization.

**Risk matrices** cross-tabulate probability and impact, creating visual representations of risk landscape.

**Scenario-based assessment** develops specific scenarios and assesses their likelihood and consequences, avoiding the abstraction of probability estimates for never-before-seen events.

For AI, probability estimation is particularly challenging. How likely is a specific failure mode? With limited operating history and unpredictable capability boundaries, probability estimates are highly uncertain.

**Risk Prioritization**

Resources are limited; not all risks can be addressed equally:

**Expected value ranking** prioritizes by probability × impact. But this may underweight low-probability, high-consequence risks.

**Risk appetite** defines what level of risk is acceptable. Different stakeholders may have different appetites.

**Consequence-focused prioritization** may focus on high-consequence risks regardless of probability, especially for catastrophic outcomes.

**Risk Mitigation**

Once prioritized, risks can be addressed:

**Avoid**: Don't deploy AI in high-risk contexts
**Transfer**: Insurance, contractual provisions, shared responsibility
**Mitigate**: Reduce probability or consequence through controls
**Accept**: Acknowledge residual risk after other measures

For AI, mitigations might include: output filtering, human review requirements, usage restrictions, monitoring and alerting, fallback procedures when AI fails.

**Residual Risk**

Risk management reduces but doesn't eliminate risk. Residual risk is what remains after mitigation. It must be:
- Quantified (to the extent possible)
- Documented
- Accepted consciously by appropriate stakeholders
- Monitored over time

For AI, residual risk includes: unknown failure modes, edge cases not tested, adversarial attacks not anticipated, performance degradation over time.

**Enterprise Risk Management**

ERM takes organization-wide view of risk:
- Aggregating risks across units
- Understanding risk interdependencies
- Aligning risk appetite with strategy
- Building risk-aware culture

For AI, ERM perspective considers: How do AI risks relate to other organizational risks? What's the organization's appetite for AI risk? How does AI risk fit strategic objectives?

### What Transfers to AI Evaluation

**Structured risk identification**: Systematic approaches to finding risks, rather than ad hoc consideration.

**Risk-based prioritization**: Focus evaluation resources on highest-risk areas.

**Residual risk concept**: Evaluation reduces but doesn't eliminate risk. Characterize what remains.

**Risk monitoring**: Ongoing risk tracking after deployment, not just pre-deployment assessment.

### What Breaks for Generative AI

**Probability estimation**: AI failure probabilities are hard to estimate with limited history and unpredictable failures.

**Enumerable failures**: Traditional risk analysis assumes you can list what might go wrong. AI failures may be unforeseen.

**Independence assumptions**: Standard risk analysis assumes risks are independent. AI risks may be correlated (same model flaws affect multiple use cases).

### Implications for AI Evaluation

- **Use risk frameworks to prioritize evaluation.** Not all AI uses warrant the same scrutiny.
- **Accept that risk can't be eliminated.** Characterize residual risk honestly.
- **Plan for ongoing risk monitoring.** Pre-deployment evaluation isn't sufficient.
- **Expect unknown unknowns.** Design for detection and response, not just prevention.

### Key References

- **ISO 31000 (Risk Management—Guidelines).** International standard for risk management.

- **NIST AI Risk Management Framework.** AI-specific risk management guidance.

- **Kaplan, S., & Garrick, B.J. (1981). "On the Quantitative Definition of Risk." *Risk Analysis*.** Foundational paper on risk definition.

- **Hubbard, D.W. (2020). *The Failure of Risk Management* (2nd ed.).** Critical examination of risk management practice.

---

## Section 4.2: Reliability Engineering

### Overview

Reliability engineering focuses on ensuring systems perform their required functions over time. While developed primarily for hardware systems, reliability thinking offers frameworks for understanding AI system consistency and monitoring for degradation.

### Core Concepts

**Reliability Definitions**

**Reliability** is the probability that a system performs its required function under specified conditions for a specified time.

**Mean Time Between Failures (MTBF)** measures average time between failures for repairable systems.

**Mean Time To Failure (MTTF)** measures average time to failure for non-repairable systems.

**Availability** is the proportion of time the system is operational: Uptime / (Uptime + Downtime).

For AI, "failure" needs reinterpretation. AI doesn't crash like hardware; it produces outputs that may be wrong, unhelpful, or harmful. "Reliability" might mean: consistency of output quality, availability of service, or probability of meeting some quality threshold.

**Failure Modes and Effects Analysis (FMEA)**

FMEA systematically identifies:
- How can each component fail? (Failure modes)
- What happens when it fails? (Effects)
- How likely is failure? (Occurrence)
- How severe are consequences? (Severity)
- Can failure be detected? (Detection)

Risk Priority Number (RPN) = Occurrence × Severity × Detection guides prioritization.

For AI, FMEA thinking asks: How can AI outputs fail? (Incorrect, biased, harmful, off-topic, etc.) What happens when they do? (User acts on wrong information, decisions are biased, reputation damage, etc.) How detectable are failures? (Some obvious, others subtle.)

**Reliability Growth**

Systems become more reliable as failures are found and fixed. Reliability growth models track improvement over development and deployment:
- **Duane model**: Reliability improves predictably with time/effort
- **AMSAA model**: Reliability growth as power law function

For AI, reliability might improve as: edge cases are identified and addressed, users learn to prompt better, system prompts are refined, fine-tuning addresses weaknesses.

**The Bathtub Curve**

Hardware failure rates often follow a "bathtub" pattern:
- **Early life (infant mortality)**: High initial failures from manufacturing defects
- **Useful life**: Low, constant failure rate
- **Wear-out**: Increasing failures as components age

AI doesn't wear out physically, but analogous patterns might exist: high initial issues during deployment, stabilization, and eventually degradation as the world changes and the model becomes stale.

**Common Cause Failures**

Multiple components failing from the same cause (environmental shock, design flaw, shared supply chain) defeat redundancy designed to handle independent failures.

For AI, common cause concerns include: same model deployed across applications (single point of failure), same training data biases affecting all outputs, same vulnerabilities across deployments.

### What Transfers to AI Evaluation

**Failure mode thinking**: Systematically consider how AI can fail and what happens when it does.

**Reliability monitoring**: Track performance over time looking for degradation.

**Common cause awareness**: AI systems may have correlated failures across applications.

### What Breaks for Generative AI

**Predictable failure distributions**: AI failures don't follow hardware reliability distributions.

**Component-based modeling**: AI isn't modular in ways that enable component reliability analysis.

**Physical failure mechanisms**: AI "fails" differently than hardware.

### Implications for AI Evaluation

- **Apply FMEA thinking** to identify failure modes and their consequences.
- **Monitor for reliability trends** over time.
- **Be aware of common cause risks** when same AI is deployed across multiple uses.
- **Track whether reliability improves** as issues are addressed.

### Key References

- **O'Connor, P.D.T., & Kleyner, A. (2012). *Practical Reliability Engineering* (5th ed.).** Comprehensive reliability engineering text.

- **MIL-HDBK-217.** Military standard for reliability prediction.

---

## Section 4.3: Quality Management

### Overview

Quality management provides systematic approaches to ensuring and improving quality. For AI, quality management concepts inform continuous monitoring and improvement after deployment.

### Core Concepts

**Statistical Process Control (SPC)**

SPC monitors process outputs over time using control charts:
- **Control limits** define the range of expected variation
- **Common cause variation** is inherent to the process; expected
- **Special cause variation** indicates something has changed; requires investigation

When metrics exceed control limits, investigation is triggered. This distinguishes normal variability from meaningful change.

For AI, SPC might monitor output quality metrics, response times, error rates, or user satisfaction over time. Sustained shifts or outliers trigger investigation.

**Process Capability**

Can the process meet specifications? Capability indices (Cp, Cpk) compare process variation to specification tolerance. A capable process consistently produces outputs within acceptable bounds.

For AI, capability asks: Can the AI consistently meet quality requirements? What proportion of outputs meet quality standards?

**Continuous Improvement**

**PDCA (Plan-Do-Check-Act)**: Iterative improvement cycle
- Plan: Identify improvement opportunity
- Do: Implement change on small scale
- Check: Evaluate results
- Act: Standardize if successful; iterate if not

For AI, PDCA might involve: identifying prompt improvement opportunities, testing changes, measuring effects, and standardizing successful improvements.

**Root Cause Analysis**

When quality problems occur, surface symptoms often mask underlying causes. Root cause analysis techniques:
- **5 Whys**: Iteratively ask "why?" to dig deeper
- **Fishbone diagrams**: Categorize potential causes

For AI, root cause analysis is challenging because the "root cause" of an AI error may be obscure (training data? model architecture? prompt design? user interaction?).

### What Transfers to AI Evaluation

**SPC for monitoring**: Control charts can track AI performance metrics over time.

**Continuous improvement mindset**: AI use should improve through deliberate improvement cycles.

**Root cause orientation**: Understand why failures occur, not just that they occur.

### What Breaks for Generative AI

**Clear specifications**: Quality traditionally means meeting specs. AI "specs" are fuzzy.

**Observable processes**: AI processing is opaque; you see inputs and outputs but not the process.

**Stable processes**: AI systems may not be stable enough for traditional SPC.

### Implications for AI Evaluation

- **Apply control chart thinking** to AI monitoring. Define metrics, establish baselines, flag deviations.
- **Use improvement cycles** to systematically enhance AI use.
- **Attempt root cause analysis** even though AI makes it difficult.

### Key References

- **Montgomery, D.C. (2019). *Introduction to Statistical Quality Control* (8th ed.).** Standard quality control text.

- **Wheeler, D.J. (2000). *Understanding Variation*.** Accessible introduction to SPC thinking.

---

## Section 4.4: Audit and Assurance

### Overview

Audit provides independent assurance that something is as claimed. The audit profession has developed rigorous methods for evidence gathering, independence, and professional judgment that can inform AI evaluation governance.

### Core Concepts

**Audit Objectives and Levels of Assurance**

Audits provide opinions on whether claims are accurate:
- **Reasonable assurance**: High but not absolute confidence
- **Limited assurance**: Lower confidence, less extensive procedures

Audit opinions don't guarantee truth but provide independent assessment of claim credibility.

**Independence and Objectivity**

Auditor independence is fundamental:
- Independence from the entity being audited
- No conflicts of interest
- Professional skepticism—not taking claims at face value

For AI, independence means evaluation by parties separate from developers/vendors with no stake in favorable outcomes.

**Materiality**

Not everything warrants equal scrutiny. Materiality focuses attention on what matters:
- What would change decisions if different?
- What are the most consequential claims?

For AI evaluation, materiality suggests focusing on claims that matter most for deployment decisions, not exhaustive evaluation of everything.

**Audit Evidence**

Evidence types include:
- Documentary (records, logs)
- Testimonial (interviews, representations)
- Observational (watching processes)
- Analytical (examining patterns)

Evidence should be sufficient (enough of it) and appropriate (relevant and reliable).

For AI, evidence might include: benchmark results, user studies, incident logs, usage data, expert review of outputs.

**Three Lines of Defense Model**

Organizational assurance is layered:
- **First line**: Operational management and controls
- **Second line**: Risk management and compliance functions
- **Third line**: Internal audit

For AI, this suggests: operational teams monitoring AI use (first line), risk/compliance overseeing AI governance (second line), internal audit independently assessing (third line).

### What Transfers to AI Evaluation

**Independence principle**: Evaluation by parties independent of developers/vendors.

**Materiality**: Focus on what matters for decisions.

**Evidence standards**: Rigor in gathering and evaluating evidence.

**Professional skepticism**: Not accepting claims at face value.

**Layered assurance**: Multiple lines of defense for AI governance.

### What Breaks for Generative AI

**Established standards**: Financial audit has mature standards; AI audit is emerging.

**Clear assertions**: Financial statements have defined assertions; AI claims are fuzzier.

**Audit trail**: Traditional systems have clear trails; AI processing is opaque.

### Implications for AI Evaluation

- **Apply independence** for high-stakes AI decisions.
- **Use materiality** to scope evaluation appropriately.
- **Develop evidence standards** for AI evaluation.
- **Consider governance structures** with appropriate assurance layers.

### Key References

- **AICPA Audit Standards.** Professional standards for financial audit.

- **IIA Standards.** International Standards for Internal Auditing.

- **Raji, I.D., et al. (2020). "Closing the AI Accountability Gap." *FAT*.** Framework for AI auditing.

---

## Section 4.5: Safety Engineering

### Overview

Safety engineering focuses on preventing hazards and ensuring systems don't cause harm. For AI in safety-critical applications, safety engineering methods provide frameworks for hazard analysis and structured safety argumentation.

### Core Concepts

**Hazard Analysis**

A hazard is a condition that could lead to harm. Safety analysis identifies hazards and their pathways to harm:
- **What hazards exist?** (Energy sources, dangerous materials, error possibilities)
- **What triggers them?** (Conditions, actions, combinations)
- **What are the consequences?** (Severity, reversibility)

For AI, hazards include: incorrect outputs leading to bad decisions, biased outputs causing discrimination, AI unavailability at critical moments, AI being used to cause harm.

**Fault Tree Analysis (FTA)**

FTA works top-down from an undesired event to identify causes:
- Start with the top event (the hazard)
- Identify immediate causes (gates connecting events)
- Continue until reaching basic events

The resulting tree shows all paths to the hazard. For AI, FTA might trace how AI errors could lead to harm, identifying contributing factors at each level.

**Event Tree Analysis (ETA)**

ETA works forward from an initiating event through possible outcomes:
- What initiating events could occur?
- What barriers exist? Do they succeed or fail?
- What outcomes result from each path?

ETA shows the branching possibilities following an initial event and estimates outcome probabilities.

**System-Theoretic Process Analysis (STPA)**

STPA, developed by Nancy Leveson, takes a systems perspective:
- Systems fail not just from component failures but from unsafe interactions
- Focus on control structures and unsafe control actions
- Consider emergent properties of the system as a whole

For human-AI systems, STPA is particularly valuable. Rather than just asking how the AI can fail, STPA asks how the control structure (human, AI, organization, environment) can produce unsafe outcomes through interactions and emergent behaviors.

**Safety Cases**

A safety case is a structured argument that a system is acceptably safe:
- **Claims**: What safety properties are asserted?
- **Evidence**: What data supports each claim?
- **Argument**: How does evidence support claims?
- **Context**: What assumptions and scope limitations apply?

Goal Structuring Notation (GSN) provides visual representation of safety arguments.

For AI, safety cases are emerging as frameworks for structured safety argumentation. Rather than simply claiming "the AI is safe," safety cases make the argument explicit and contestable.

**Functional Safety**

Functional safety (IEC 61508 and derivatives) addresses safety achieved through control systems:
- **Safety Integrity Levels (SIL)** define required reliability
- Higher SILs require more rigorous development and verification
- Defense in depth through multiple independent protections

For AI, functional safety concepts are being adapted, though AI doesn't fit neatly into the framework designed for programmed control systems.

### What Transfers to AI Evaluation

**Hazard analysis mindset**: Systematically identify how AI could cause harm.

**Safety case methodology**: Structured argumentation applicable to AI safety claims.

**STPA for human-AI systems**: Systems perspective on safety captures interactions.

**Defense in depth**: Multiple protections rather than relying on AI alone.

### What Breaks for Generative AI

**Component failure models**: AI doesn't fail like hardware components.

**Quantitative failure rates**: AI failure probabilities are hard to estimate.

**Formal verification**: Safety properties generally can't be formally verified for AI.

### Implications for AI Evaluation

- **For safety-critical AI, apply safety engineering methods.**
- **Develop safety cases** for high-stakes deployments.
- **Use STPA** to analyze human-AI control structures.
- **Design for AI failure**: monitoring, override, fallback.

### Key References

- **Leveson, N.G. (2011). *Engineering a Safer World*.** STPA methodology and systems safety thinking.

- **IEC 61508 (Functional Safety).** Foundation for functional safety standards.

- **Bloomfield, R., & Bishop, P. (2010). "Safety and Assurance Cases: Past, Present and Possible Future."** Overview of safety case methodology.

---

*[End of Section 4]*


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


## Section 7.1: Metrology (Science of Measurement)

### Overview

Metrology is the science of measurement itself—a discipline that asks fundamental questions about what it means to measure something. While focused primarily on physical measurement, metrological principles illuminate the immature state of AI evaluation and point toward what rigorous AI measurement might eventually require.

### Core Concepts

**Measurement Uncertainty**

All measurements have uncertainty—no measurement is perfectly precise. Metrological practice requires:
- **Quantifying uncertainty**: Expressing the range within which the true value lies
- **Reporting uncertainty**: Including uncertainty estimates with measurements
- **Uncertainty propagation**: Tracking how uncertainty compounds through calculations

For AI evaluation, measurement uncertainty is substantial but rarely quantified. What's the uncertainty on a benchmark score? On a productivity estimate? Metrological rigor would require estimating and reporting this uncertainty.

**Traceability**

Measurements should be traceable to reference standards:
- A chain of comparisons linking measurement to recognized standards
- Enables comparison across different measuring systems
- Ensures measurements mean the same thing in different contexts

For AI evaluation, what are measurements traceable to? Different benchmarks may define "accuracy" differently. There's no agreed reference standard for AI capability. This lack of traceability limits comparability.

**Reference Standards**

Physical metrology has reference standards:
- The International Prototype of the Kilogram (now replaced by physical constants)
- Standard reference materials for calibration
- Maintained by national metrology institutes

AI evaluation lacks comparable reference standards. There's no agreed "reference AI task" against which to calibrate benchmarks.

**Calibration**

Measuring instruments must be calibrated—verified against reference standards:
- Regular recalibration ensures ongoing accuracy
- Calibration certificates document instrument accuracy

For AI evaluation, calibration asks: Are our evaluation methods themselves accurate? Do benchmarks measure what they claim? This meta-evaluation is rarely done systematically.

**Proficiency Testing**

Proficiency testing assesses measurement capability:
- Same samples measured by different laboratories
- Comparison reveals measurement quality
- Enables identification and correction of problems

For AI, proficiency testing might have different evaluators assess the same AI outputs. Disagreement reveals evaluation problems.

**Vocabulary of Metrology (VIM)**

The VIM provides internationally agreed definitions:
- **Accuracy**: Closeness of measurement to true value (combining trueness and precision)
- **Precision**: Closeness of repeated measurements to each other
- **Trueness**: Closeness of average measurement to true value
- **Bias**: Difference between measured mean and true value

AI evaluation often uses these terms loosely. Metrological precision in vocabulary would improve communication.

### What Transfers to AI Evaluation

**Uncertainty awareness**: AI evaluation has substantial uncertainty that should be quantified and reported.

**Traceability concept**: What are AI evaluations traceable to? This question highlights gaps in evaluation infrastructure.

**Calibration mindset**: Are our evaluation methods themselves valid?

### What Breaks for Generative AI

**Physical measurement focus**: Metrology developed for physical quantities with clear operational definitions.

**Reference standards**: No agreed reference standards exist for AI evaluation.

**Mature infrastructure**: AI evaluation lacks the institutional infrastructure of physical metrology.

### Implications for AI Evaluation

- **AI evaluation is metrologically immature.** Recognize this rather than claiming false precision.
- **Report uncertainty** in evaluation results.
- **Work toward shared reference benchmarks** that enable comparison.
- **Consider evaluation methodology validation**—calibrating our evaluation methods.

### Key References

- **BIPM. *International Vocabulary of Metrology (VIM)* (3rd ed.).** International measurement definitions.

- **JCGM. *Guide to the Expression of Uncertainty in Measurement (GUM)*.** Standard for uncertainty quantification.

- **Tal, E. (2017). "Measurement in Science." *Stanford Encyclopedia of Philosophy*.** Philosophical foundations of measurement.

---

## Section 7.2: Standards Development and Governance

### Overview

Technical standards establish common frameworks, definitions, and requirements. AI evaluation standards are emerging, and understanding the standards landscape helps organizations navigate compliance requirements and contribute to standards development.

### Core Concepts

**Types of Standards**

**De jure standards** are established through formal processes:
- Standards development organizations (SDOs) like ISO, IEEE, NIST
- Consensus-based processes with stakeholder participation
- Formal approval and publication

**De facto standards** emerge from market adoption:
- Widely used approaches become standard practice
- May later be formalized as de jure standards

**Mandatory vs. voluntary**: Some standards are required by law or regulation; others are voluntary guidelines.

**Performance vs. prescriptive**: Performance standards specify what must be achieved; prescriptive standards specify how to achieve it.

**Standards Development Organizations**

Key SDOs for AI:

**NIST** (National Institute of Standards and Technology): Developed the AI Risk Management Framework, conducts AI evaluation research

**ISO** (International Organization for Standardization): ISO/IEC JTC 1/SC 42 is developing AI standards

**IEEE**: Standards for AI ethics, transparency, and related topics

**Standards development processes** typically involve:
- Identification of need
- Formation of working groups
- Drafting and iteration
- Consensus building
- Public comment
- Formal approval

**Conformity Assessment**

Conformity assessment determines whether products/services meet standards:
- **Self-declaration**: Organization claims compliance
- **Second-party assessment**: Customer evaluates supplier
- **Third-party certification**: Independent body evaluates and certifies

**Accreditation** recognizes competence of conformity assessment bodies.

For AI, conformity assessment asks: How do you demonstrate compliance with AI standards? Who is qualified to assess compliance?

**Standards and Innovation**

Standardization has complex effects on innovation:
- **Too early**: Locks in immature approaches, may stifle innovation
- **Too late**: Misses opportunity for coordination, allows fragmentation
- **Dynamic standards**: Versioned standards that can evolve

For AI, the timing question is acute. Standards developed now may not fit tomorrow's AI. But lack of standards creates uncertainty and inconsistency.

### Current AI Standards Landscape

**NIST AI Risk Management Framework**: Voluntary framework for managing AI risks, including evaluation guidance

**ISO/IEC AI standards** in development: Covering AI management systems, trustworthiness, governance

**EU AI Act**: Regulatory framework with conformity assessment requirements for high-risk AI

**Industry frameworks**: Various industry consortia developing AI governance frameworks

### What Transfers to AI Evaluation

**Standards awareness**: Know what standards exist and are emerging.

**Conformity assessment**: Understand how compliance will be demonstrated.

**Timing awareness**: AI standards are still developing; don't wait, but don't expect permanence.

### Implications for AI Evaluation

- **Engage with emerging standards** (NIST AI RMF, ISO, etc.).
- **Recognize standards are developing**; don't wait for them, but expect evolution.
- **Consider contributing** to standards development.
- **Understand conformity assessment requirements** as they emerge.

### Key References

- **NIST AI Risk Management Framework.** US government AI risk management guidance.

- **ISO/IEC JTC 1/SC 42.** AI standards development at ISO.

- **EU Artificial Intelligence Act.** European regulatory framework for AI.

---

*[End of Section 7]*


## Overview

This section synthesizes insights across the disciplines covered in this appendix, identifies what transfers to AI evaluation, what breaks, and what is genuinely new. It also provides "crosswalks"—mappings of equivalent or related concepts across disciplines that may help readers connect familiar concepts to new ones.

---

## Section 8.1: What Transfers Directly

The following concepts transfer directly from existing disciplines to AI evaluation and should be applied with minimal modification:

| Discipline | Key Transferable Concepts | Application to AI Evaluation |
|------------|--------------------------|------------------------------|
| **Software Testing** | Verification vs. Validation distinction | Benchmarks are closer to verification; operational testing is validation |
| | Test planning discipline | Systematic identification of what to test |
| | Regression mindset | Track performance over time to detect degradation |
| **Systems T&E** | DT/OT paradigm | Lab testing (DT) precedes operational pilots (OT) |
| | MOPs vs. MOEs | Technical metrics ≠ mission effectiveness |
| | Independent evaluation | Separate evaluator from developer for credibility |
| **Autonomous Systems** | Sim-to-real gap awareness | Benchmark-to-real gap is analogous |
| | Scenario-based testing | Systematic scenario design and prioritization |
| | Safety case methodology | Structured safety argumentation |
| **Cybersecurity** | Adversarial mindset | Actively try to make AI fail |
| | Red teaming methodology | Structured adversarial evaluation |
| | Threat modeling | Prioritize evaluation based on threat analysis |
| | Defense in depth | Multiple protections, not reliance on single measure |
| **Experimental Design** | Validity framework | Internal, external, construct validity |
| | Control conditions | What's the comparison? Relative to what? |
| | Bias awareness | Selection, attrition, experimenter bias |
| | Pre-registration | Commit to analysis plans |
| **Psychometrics** | Reliability concepts | Consistency of measurement |
| | Construct validity | Does benchmark measure what we intend? |
| | Criterion validity | Does benchmark predict real-world performance? |
| | Inter-rater reliability | Agreement across human evaluators |
| **Econometrics** | Counterfactual thinking | What would have happened without AI? |
| | Selection bias awareness | Who adopts AI is not random |
| | Heterogeneity analysis | Effects vary across users/contexts |
| **Qualitative Methods** | Understanding "why" | How and why does AI help (or not)? |
| | Contextual inquiry | Observe AI use in natural settings |
| | User perspective | Understand experience from user point of view |
| **Survey Methods** | Questionnaire design | Careful item wording, validated scales |
| | Non-response awareness | Who responds is not random |
| **Risk Analysis** | Risk-based prioritization | Focus evaluation on highest-risk areas |
| | Residual risk | Evaluation reduces but doesn't eliminate risk |
| **Quality Management** | SPC for monitoring | Control charts for AI metrics over time |
| | Continuous improvement | Iterative improvement of AI use |
| **Audit** | Independence principle | Separate evaluator from developer |
| | Evidence standards | Rigor in gathering and assessing evidence |
| **Safety Engineering** | Hazard analysis | Systematically identify how AI can cause harm |
| | STPA | System-theoretic analysis of human-AI teams |
| **Human Factors** | Trust calibration | Are users appropriately trusting/skeptical? |
| | Automation surprises | AI surprises users frequently |
| | Situation awareness | Human awareness in human-AI teams |
| **I-O Psychology** | Structured evaluation | Structure reduces noise and bias |
| | Criterion problem | "Good performance" is hard to define |
| | Work sample testing | Evaluate on realistic tasks |
| **Program Evaluation** | Logic models | Make explicit how AI creates value |
| | Implementation fidelity | Is AI actually being used? How? |
| | Developmental evaluation | Appropriate for emerging AI use |
| **Clinical Trials** | Phased approach | Start small, expand based on results |
| | Post-market surveillance | Monitor after deployment |

---

## Section 8.2: What Breaks for Generative AI

Fundamental assumptions from traditional disciplines that fail for generative AI:

| Broken Assumption | Disciplines Affected | Reality for AI |
|-------------------|---------------------|----------------|
| **Determinism** | Software testing, reliability engineering | AI outputs are stochastic; same input produces different outputs |
| **Enumerable inputs/outputs** | Software testing, traditional ML | Input and output spaces are effectively unbounded |
| **Clear ground truth** | Traditional ML, psychometrics | Many AI tasks have no single "correct" answer |
| **Stable system under test** | All T&E disciplines | Models update continuously, sometimes without notice |
| **Stable traits/capabilities** | Psychometrics, I-O psychology | AI capabilities change rapidly |
| **Predictable failures** | Reliability engineering, safety | Failures occur unpredictably at jagged capability boundaries |
| **Observable processes** | Quality management, safety | AI processing is opaque |
| **Clear system boundaries** | Systems engineering | Where does AI end? (Model + prompt + context + user) |
| **Independent failures** | Reliability engineering, risk | AI failures may be correlated across applications |
| **Blinding** | Experimental design, clinical trials | Users typically know they're using AI |
| **Treatment stability** | Experimental design | AI changes during evaluation period |
| **Defined treatment** | Econometrics, program evaluation | "Using AI" is highly variable |
| **Historical data** | Risk analysis, reliability | Limited operating history for AI |
| **Population/norming** | Psychometrics | No natural reference population for AI |
| **Test security** | Psychometrics, educational measurement | Training may include benchmark items |

---

## Section 8.3: What Requires Adaptation

Concepts that transfer with significant modification:

| Original Concept | Discipline | Required Adaptation |
|-----------------|------------|---------------------|
| **Test coverage** | Software testing | Coverage of capabilities/scenarios, not input space |
| **Regression testing** | Software testing | Continuous monitoring rather than re-running fixed tests |
| **Reliability prediction** | Reliability engineering | Scenario-based rather than component-based |
| **FMEA** | Reliability/safety | Failure modes are less enumerable; more emphasis on unknown unknowns |
| **Trust calibration** | Human factors | For systems with stochastic, jagged capabilities |
| **Implementation fidelity** | Program evaluation | "Use" is highly variable and hard to characterize |
| **IRT/psychometric methods** | Psychometrics | For benchmark design, not stable trait measurement |
| **Safety cases** | Safety engineering | New evidence types and argument structures needed |
| **Audit evidence** | Audit | New evidence types for opaque AI systems |
| **Control charts** | Quality management | For AI-specific metrics with different variability patterns |

---

## Section 8.4: What's Genuinely New

Some AI evaluation challenges don't have good precedents from existing disciplines:

### 1. Unbounded Output Evaluation

No prior field has evaluated systems that produce outputs from an essentially unlimited space. Classification has k classes; regression has one number; traditional software has specified output formats. Language models produce arbitrary text. The entire machinery of enumerable-output evaluation (confusion matrices, classification metrics, output verification) doesn't apply.

### 2. Jagged Capability Frontier

The pattern of high capability immediately adjacent to surprising failure is unprecedented. Traditional systems have understood capability boundaries—they work within specification and don't work outside it. AI exhibits high capability on some instances while failing on nearly identical instances. This "jaggedness" means evaluation must cover capability more densely than previous approaches assumed.

### 3. Specification Depth Problem

Much of AI's value lies in handling tasks that couldn't be specified precisely enough to automate traditionally. But if we could specify the task precisely, we could automate it without AI. This creates a fundamental tension: the tasks where AI is most valuable are the tasks hardest to specify—and therefore hardest to evaluate.

### 4. Benchmark Contamination Via Training

Traditional test security prevents examinees from seeing test items in advance. AI training may include benchmark items in training corpora—not through intentional cheating but through internet-scale data collection. This "data contamination" inflates benchmark performance in ways that don't reflect true capability, creating a novel threat to evaluation validity that doesn't have direct precedent.

### 5. Continuous Evolution During Deployment

Most evaluation paradigms assume a stable system: test it, then deploy it. AI systems may change continuously—through model updates, fine-tuning, or prompt engineering—without clear version boundaries. The entity evaluated may differ from the entity deployed, and the entity deployed today may differ from the entity deployed tomorrow.

### 6. Skill Amplification

The same AI system produces dramatically different outcomes for different users. A novice may barely use AI capability; an expert may achieve remarkable results. This "skill amplification" means system capability is entangled with user skill in ways that complicate evaluation. Traditional automation provides more uniform augmentation.

### 7. The "Vibes" Quality Problem

For many AI tasks, experts recognize quality when they see it but struggle to articulate criteria precisely enough for reliable measurement. This isn't unique to AI, but the breadth of AI applications (writing, coding, analysis, conversation) across so many quality dimensions makes it particularly acute. How do you systematically evaluate something when "you know it when you see it" is the best quality criterion available?

---

## Section 8.5: Terminology Crosswalk

Different disciplines use different terms for similar or related concepts. This crosswalk maps common concepts across disciplines to help readers connect familiar terminology to unfamiliar fields:

### Accuracy and Error

| Discipline | Term | Meaning |
|------------|------|---------|
| Traditional ML | Accuracy | Proportion of correct predictions |
| Traditional ML | Error rate | Proportion of incorrect predictions |
| Metrology | Accuracy | Closeness to true value (combining trueness and precision) |
| Metrology | Trueness | Systematic closeness to true value |
| Metrology | Precision | Repeatability of measurements |
| Software Testing | Defect | Software behavior contrary to specification |
| Quality Management | Defect | Unit that doesn't conform to specifications |

### Reliability and Consistency

| Discipline | Term | Meaning |
|------------|------|---------|
| Psychometrics | Reliability | Consistency of measurement across occasions, raters, items |
| Reliability Engineering | Reliability | Probability of successful operation over time |
| Software | Reliability | Probability of failure-free operation |
| Quality Management | Consistency | Producing similar outputs over time |

### Validity and Effectiveness

| Discipline | Term | Meaning |
|------------|------|---------|
| Psychometrics | Validity | Whether measure assesses intended construct |
| Experimental Design | Validity | Whether conclusions are warranted (internal, external, construct) |
| Systems T&E | Effectiveness | Degree to which system accomplishes mission |
| Psychometrics | Criterion validity | Whether measure predicts relevant outcomes |
| Systems T&E | MOE | Measure of Effectiveness—mission outcome metrics |

### Performance and Capability

| Discipline | Term | Meaning |
|------------|------|---------|
| Systems T&E | Performance | Technical parameter values (speed, accuracy, etc.) |
| Systems T&E | MOP | Measure of Performance—technical parameters |
| I-O Psychology | Performance | Work output quality and quantity |
| AI Safety | Capability | What the model can do (including dangerous capabilities) |
| AI Evaluation | Benchmark score | Performance on standardized evaluation |

### Testing Types

| Discipline | Term | Meaning |
|------------|------|---------|
| Software Testing | Unit testing | Testing individual components |
| Software Testing | Integration testing | Testing component interactions |
| Software Testing | System testing | Testing complete system |
| Systems T&E | Developmental testing (DT) | Testing during development |
| Systems T&E | Operational testing (OT) | Testing under realistic conditions |
| Clinical Trials | Phase I, II, III | Staged testing with increasing scale and rigor |

### Risk and Hazard

| Discipline | Term | Meaning |
|------------|------|---------|
| Risk Analysis | Risk | Probability × Consequence |
| Risk Analysis | Hazard | Condition that could cause harm |
| Safety Engineering | Hazard | Condition that could lead to accident |
| Safety Engineering | Risk | Function of hazard, exposure, and consequence |
| Cybersecurity | Threat | Potential source of harm |
| Cybersecurity | Vulnerability | Weakness that can be exploited |

### Independence and Separation

| Discipline | Term | Meaning |
|------------|------|---------|
| Audit | Independence | Auditor separate from entity being audited |
| Systems T&E | Independent evaluation | Evaluation by party independent of developer |
| Experimental Design | Random assignment | Unpredictable assignment to conditions |
| Experimental Design | Blinding | Hiding condition assignment from participants/researchers |

### Quality and Assurance

| Discipline | Term | Meaning |
|------------|------|---------|
| Quality Management | Quality | Conformance to requirements |
| Quality Management | Assurance | Confidence that quality requirements will be met |
| Audit | Assurance | Confidence that claims are accurate |
| Safety Engineering | Safety case | Structured argument that system is safe |
| AI Safety | Safety case | Structured argument for AI safety |

### Human-AI Concepts

| Discipline | Term | Meaning |
|------------|------|---------|
| Human Factors | Trust calibration | Matching trust to actual system reliability |
| Human Factors | Automation bias | Uncritical acceptance of automation |
| JDM | Algorithm aversion | Resistance to algorithmic advice |
| JDM | Algorithm appreciation | Over-reliance on algorithmic advice |
| Human Factors | Complacency | Inappropriate trust in automation |
| Human Factors | Situation awareness | Understanding of current state and future trajectory |

### Evaluation Approaches

| Discipline | Term | Meaning |
|------------|------|---------|
| Program Evaluation | Formative evaluation | Evaluation to improve during implementation |
| Program Evaluation | Summative evaluation | Evaluation to judge overall effectiveness |
| Program Evaluation | Process evaluation | Did intervention occur as planned? |
| Program Evaluation | Outcome evaluation | Did desired effects occur? |
| Clinical Trials | Efficacy | Effect under ideal conditions |
| Clinical Trials | Effectiveness | Effect under real-world conditions |

---

## Section 8.6: Synthesis: What AI Evaluation Requires

Drawing across all disciplines, effective AI evaluation requires:

### From Testing Traditions
- **Systematic approach**: Planned, comprehensive evaluation rather than ad hoc probing
- **V&V distinction**: Separate technical verification from fitness-for-purpose validation
- **DT/OT paradigm**: Lab evaluation precedes and differs from operational evaluation
- **Adversarial orientation**: Actively try to find failures, not just confirm successes
- **Scenario-based coverage**: Systematic scenario coverage since input space is unbounded

### From Statistical Methods
- **Validity framework**: Rigorous attention to internal, external, construct validity
- **Appropriate comparison**: Clear baseline/control conditions
- **Causal discipline**: Distinguish correlation from causation
- **Heterogeneity awareness**: Average effects may mask important variation
- **Qualitative complement**: Numbers need qualitative understanding of how and why

### From Economics
- **Productivity paradox awareness**: Don't expect immediate measured gains
- **Complementary investments**: AI benefits require organizational change
- **Full cost accounting**: Include hidden and indirect costs
- **Time horizons**: Short-run may differ from long-run

### From Risk and Quality
- **Risk-based prioritization**: Focus resources on highest-risk applications
- **Continuous monitoring**: Don't rely solely on pre-deployment evaluation
- **Residual risk acceptance**: Evaluation reduces but doesn't eliminate risk
- **Independence**: Separate evaluator from developer for high stakes

### From Human and Organizational Factors
- **Human-AI team evaluation**: Assess the team, not just the AI
- **Trust calibration**: Evaluate whether users trust appropriately
- **Organizational context**: Evaluation results depend on organizational factors
- **Implementation fidelity**: Check whether AI is actually being used

### From Evaluation Traditions
- **Logic models**: Make explicit how AI is supposed to create value
- **Developmental approach**: Appropriate when learning what works
- **Post-deployment surveillance**: Continue evaluation after deployment

### Novel Requirements for AI
- **Benchmark integrity**: Protect against contamination
- **Capability coverage**: Dense coverage of jagged frontier
- **Output evaluation**: Methods for unbounded, open-ended outputs
- **Evolution accommodation**: Evaluation design that handles system change
- **Skill interaction**: Understanding how user skill affects outcomes
- **Quality articulation**: Methods for the "vibes" problem

---

## Section 8.7: Reader Guide

**For T&E Professionals**:
Start with Sections 1 (Testing Traditions), 4 (Risk, Quality, Assurance), and 6 (Evaluation Traditions). These connect most directly to T&E backgrounds. Then explore Section 2 (Experimental Methods) for statistical rigor.

**For Researchers/Methodologists**:
Start with Section 2 (Experimental and Statistical Methods) and Section 6 (Evaluation Traditions). Then explore Section 7.1 (Metrology) for measurement foundations.

**For Acquisition/Management Professionals**:
Start with Section 3 (Economics and Productivity), Section 4.4 (Audit), and Section 7.2 (Standards). Then explore Section 5.3 (Organizational Behavior) for implementation factors.

**For Human Factors Specialists**:
Start with Section 5 (Human and Organizational Factors) and Section 5.1-5.2 (HCI and Human Factors). Then explore Section 1.3 (Autonomous Systems) for AI-specific human factors.

**For AI Safety Researchers**:
Start with Section 6.1 (AI Safety Evaluation), Section 4.5 (Safety Engineering), and Section 1.5 (Cybersecurity). Much of this work is building the bridges covered throughout this appendix.

---

*[End of Section 8]*

