# Appendix A, Section 1.2: Systems Engineering and Hardware Testing & Evaluation

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
