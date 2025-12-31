# Arena Expert Model Comparison

**Organization:** LMArena Team
**Date:** December 2025 (data from December 1, 2025)
**Type:** Benchmark Analysis / User Study
**URL:** https://news.lmarena.ai/arena-expert-model-comparison/

## Key Contributions

1. **First large-scale expert vs. novice comparison**: 139 frontier AI models evaluated by expert users vs. general users
2. **Quantified expert preference divergence**: Median +15 advantage for thinking models, -9 for non-thinking (24-point gap)
3. **Company-level differences identified**: Anthropic models show +22 average expert advantage (highest among major providers)
4. **Architecture ≠ expert preference**: Claude Opus 4.5 (non-thinking) shows +85 expert advantage, outperforming many thinking models
5. **Empirical validation of user heterogeneity hypothesis**: Confirms expert/novice preferences differ markedly

## Methodology

**Data Source:**
- LMArena platform (crowdsourced model comparison)
- Data snapshot from December 1, 2025
- User-generated prompts and blind preference ratings

**Sample:**
- **139 frontier models** analyzed (ELO rating 1300+)
- **42 thinking models** (extended reasoning, chain-of-thought)
- **97 non-thinking models** (standard inference)
- **Major providers**: Anthropic, OpenAI, Google, xAI, Alibaba, DeepSeek

**Metric:**
- **"Expert Advantage"** = performance differential between expert-user ratings and general-user ratings
- Positive number = experts rate higher than general users
- Negative number = general users rate higher than experts

**Quality Controls:**
- Style control filtering (control for output verbosity, formatting preferences)
- Minimum performance thresholds (ELO 1300+)
- Comparison of general user preferences vs. expert-only prompts

## Key Findings

### 1. Architecture Type Correlates with Expert Preference (But Not Perfectly)

**Median expert advantage by architecture:**
- **Thinking models**: +15 (experts prefer over general users)
- **Non-thinking models**: -9 (general users prefer over experts)
- **Gap**: 24-point difference

**But architecture doesn't determine outcome:**
- Claude Opus 4.5 (non-thinking): +85 expert advantage (highest of any model)
- o1-preview (thinking): -11 expert advantage (despite thinking architecture)
- **Implication**: Architecture is signal, not determinant

### 2. Massive Company-Level Differences

**Average expert advantage by company:**
1. **Anthropic: +22** (experts strongly prefer)
2. **Alibaba: +14** (experts moderately prefer)
3. **OpenAI: -3** (near neutral)
4. **Google: Negative** (exact number not provided)
5. **DeepSeek: Negative** (exact number not provided)

**Anthropic dominance:**
- Claude Opus 4.5 (non-thinking): +85 (highest overall)
- Claude Sonnet 4.5 Thinking: +57 (very high for thinking model)
- Both models show strongest expert preference in their categories

### 3. Expert Preferences Diverge from General Users

**Implications:**
- General user benchmarks (like standard LMArena) may not predict expert utility
- Models optimized for general users may underperform for experts
- Need expert-specific evaluation for professional/enterprise use cases

### 4. Thinking Models NOT Universally Better for Experts

**Contradicts simple narrative:**
- Not all thinking models show expert advantage (e.g., o1-preview: -11)
- Best non-thinking model (+85) outperforms median thinking model (+15)
- **Quality of implementation matters more than architecture choice**

## Relevance to GenAI Productivity Review

### Part 1: The Benchmark-Utility Gap

**HIGHLY RELEVANT.** This finding directly illuminates one source of benchmark-utility gap:

**User heterogeneity creates evaluation challenge:**
- General benchmarks (crowd ratings) don't predict expert utility
- 24-point gap between expert/novice preferences is substantial
- Models ranked highly by general users may underperform for professionals
- **Connection to real-world deployment**: Most productivity applications are used by experts (professionals), not general users

**Connects to other gaps:**
- [bean2025construct](bean2025construct.md): Benchmarks don't measure what they claim—this adds that they measure for wrong user population
- [brand2025benchmarking](brand2025benchmarking.md): Setup variables create 11-15% variance; user population could create even more

### Part 2: The State of the Field (Literature Review)

**CRITICAL empirical finding.** Must be included as evidence for user heterogeneity in AI utility.

**Connects to existing productivity findings:**
- **Brynjolfsson (customer service)**: 34% gain for novices, quality DECLINE for experts
  - LMArena shows experts prefer different models than novices
  - Explains why same tool has opposite effects by skill level
- **Noy & Zhang (writing tasks)**: Quality improvement varies by writer skill
  - LMArena provides mechanism: experts need different model characteristics
- **anthropic2025workdec** ([anthropic2025workdec](anthropic2025workdec.md)): 50% gains at AI company (experts)
  - Anthropic models show +22 expert advantage—their own employees may be using better-suited models for experts

### Part 3: A Framework for AI Evaluation

**CRITICAL for evaluation design:**

**Evaluator selection matters:**
1. **General user evaluations ≠ expert utility**: 24-point gap
2. **DoD should use expert evaluators**: Military professionals, not crowd ratings
3. **Match evaluator population to end-user population**: Acquisition officers should use acquisition expert evaluators

**Implications for evaluation protocols:**
1. **Separate expert and novice evaluations**: Don't average across skill levels
2. **Weight by target user population**: If 80% of users are experts, use expert ratings
3. **Test for heterogeneity**: Measure performance variance by user skill level
4. **Consider architecture-user fit**: Thinking models may suit some experts, not others

### Part 4: Practical Guidance for Acquisition Decision-Makers

**Key lessons for DoD acquisition:**

1. **Don't rely on general benchmarks for professional use:**
   - LMArena general rankings don't predict expert preference
   - 24-point gap means model ranking could completely flip for experts
   - Require expert evaluations for professional/military applications

2. **Match evaluation to end-user skill level:**
   - Acquisition officers = experts → use expert evaluations
   - Intelligence analysts = experts → use expert evaluations
   - Operational planners = experts → use expert evaluations
   - General public-facing systems (e.g., benefits portal) → general user evaluations acceptable

3. **Thinking models ≠ automatically better for experts:**
   - Claude Opus 4.5 (non-thinking): +85 expert advantage
   - Median thinking model: +15
   - Don't pay premium for thinking architecture without validating expert preference

4. **Company/implementation quality matters:**
   - Anthropic: +22 average expert advantage
   - OpenAI: -3 (near neutral)
   - Google/DeepSeek: Negative
   - **Quality differences larger than architecture differences**

5. **Pilot with actual expert users:**
   - Don't extrapolate from benchmarks or demos
   - Test with military professionals doing real tasks
   - Measure preference heterogeneity within DoD user populations

### Part 5: T&E Considerations for GenAI-Based Systems

**T&E framework implications:**

1. **User segmentation required:**
   - Identify user skill levels in target population
   - Test separately for novices and experts
   - Report results by segment (don't average)

2. **Expert panel composition:**
   - Use actual subject matter experts (not general crowd)
   - Match expert domain to application domain
   - Consider within-expert heterogeneity (junior vs. senior experts)

3. **Comparative testing:**
   - Compare models with expert users (not just benchmarks)
   - Blind preference tests like LMArena methodology
   - Control for style/formatting preferences (per LMArena filtering)

4. **Architecture evaluation:**
   - Test thinking vs. non-thinking with expert users
   - Don't assume architectural superiority without empirical validation
   - Consider cost-benefit (thinking models typically more expensive)

### Part 6: Research Agenda and Investment Priorities

**Research gaps highlighted:**

1. **Military expert preferences:**
   - Do military professionals show same expert preference patterns as LMArena users?
   - What model characteristics matter most for military experts?
   - Heterogeneity within military (intel vs. logistics vs. operations)?

2. **Skill-level × task interaction:**
   - Which tasks show largest expert/novice divergence?
   - LMArena: general conversation; what about specialized military tasks?
   - Need task-specific expert evaluation

3. **Expert advantage mechanisms:**
   - WHY do experts prefer different models?
   - Better prompting? Different quality standards? Different use cases?
   - Understanding mechanism could inform training

4. **Thinking model value proposition:**
   - When do thinking models actually benefit experts?
   - Cost-benefit analysis (thinking models more expensive)
   - Military applications where extended reasoning justified?

5. **Longitudinal expert preference:**
   - As general users become more expert, do preferences converge?
   - Learning curve effects on model preference?
   - Training implications for DoD adoption

**Investment priorities:**

- Fund DoD-specific expert preference studies (military professionals, real tasks)
- Develop expert evaluation panels for acquisition testing
- Research mechanisms of expert preference (inform training)
- Validate thinking model value for military applications
- Study heterogeneity within military expert populations

## Critical Assessment

**Strengths:**
- Large sample (139 models, multiple providers)
- Real-world platform (LMArena) with actual users
- Blind preference methodology (reduces bias)
- Style controls (separates substance from presentation)
- Clear quantification (expert advantage metric)
- Timely (December 2025 data)

**Limitations:**
- **User self-selection**: LMArena users who identify as "experts" may not be representative of all experts
- **Domain generality**: "Expert" not defined by domain—may include programmers, writers, researchers, etc.
- **Task coverage**: LMArena prompts may not represent all use cases (likely skewed toward coding, creative writing)
- **No objective performance measures**: Preference ratings, not task accuracy/quality
- **Company bias**: Anthropic dominance could reflect user base (tech-savvy early adopters)
- **Snapshot in time**: December 1, 2025 data—model landscape changes rapidly
- **Limited methodology detail**: Blog post format, not peer-reviewed paper
- **No statistical significance testing reported**: Don't know confidence intervals on expert advantage numbers

**Currency:** Excellent—December 2025 data, very recent.

**Evidence Quality:** Medium-High. Large real-world dataset with good methodology (blind preferences, style controls), but limited detail on statistical rigor, user demographics, and task distribution. Blog post format (not peer-reviewed) is limitation. However, LMArena is respected platform with established methodology.

## Connections to Other References

**Strongly supports:**
- **Brynjolfsson (customer service)**: 34% gain for novices, decline for experts
  - LMArena provides mechanism: experts and novices need different model characteristics
  - Same model can't optimize for both populations
- **Noy & Zhang (Science)**: Quality improvements vary by writer skill
  - LMArena shows experts rate models differently—explains heterogeneous quality effects

**Connects to:**
- [anthropic2025workdec](anthropic2025workdec.md): 50% productivity gain at Anthropic
  - Anthropic employees = experts + Anthropic models show +22 expert advantage
  - Their high productivity may partly reflect good expert-model fit
- [pan2025agents](pan2025agents.md): 74% of production agents use human evaluation
  - Expert preferences matter for agent evaluation too
  - Human evaluators should match end-user skill level

**Contrasts with:**
- **General benchmarks**: MMLU, HumanEval, etc. don't segment by user skill
  - LMArena shows this masks important heterogeneity
  - Need expert-specific benchmarks for professional applications

**Methodological complement to:**
- [bean2025construct](bean2025construct.md): Benchmarks don't measure what they claim
  - LMArena adds: and they measure for wrong user population
- [brand2025benchmarking](brand2025benchmarking.md): 11-15% variance from scaffolds
  - User population could be even larger source of variance

## Questions/Notes

1. **What defines "expert" in LMArena?**
   - Self-identified? Task-specific? General technical proficiency?
   - Need clear operationalization for DoD application

2. **Why such large company differences?**
   - Anthropic +22, OpenAI -3, Google negative
   - Training data? RLHF approach? Design philosophy?
   - Understanding source could inform acquisition requirements

3. **What drives Claude Opus 4.5 dominance (+85)?**
   - Specific capabilities experts value?
   - Higher accuracy? Better reasoning? Different output style?
   - Would inform DoD model selection criteria

4. **Task-specific heterogeneity?**
   - Do expert advantages vary by task type?
   - Coding vs. writing vs. analysis?
   - Military tasks different from LMArena task distribution?

5. **Can models optimize for both experts and novices?**
   - Or fundamental tradeoff?
   - If tradeoff, how should DoD navigate (mixed user populations)?

6. **How stable are expert preferences?**
   - As novices gain experience, do preferences shift toward current expert preferences?
   - Training implications for DoD adoption

7. **Statistical significance?**
   - Blog post doesn't report confidence intervals or p-values
   - How reliable are the reported differences?
   - Need full statistical analysis for acquisition decisions

## Citation Guidance

**Appropriate uses:**
- Citing expert/novice preference divergence (24-point gap)
- Documenting need for expert-specific evaluation
- Supporting user heterogeneity in AI utility
- Citing Claude Opus 4.5 expert advantage (+85)
- Referencing company-level quality differences (Anthropic +22)
- Motivating evaluator selection considerations

**Inappropriate uses:**
- Claiming all experts prefer Anthropic models (sample may not be representative)
- Using to make claims about specific military expert preferences (different population)
- Citing as peer-reviewed research (blog post format)
- Claiming thinking models don't help experts (some do, quality matters more than architecture)
- Applying specific numbers without confidence intervals (statistical significance unknown)
- Ignoring task-specific effects (LMArena task distribution may not match DoD applications)

**Citation note:** High-quality analysis from respected platform (LMArena), but blog post format and limited methodological detail are limitations. Suitable for citing as "recent evidence of expert-novice preference divergence" with appropriate caveats about generalizability to specific domains (like military applications). The core finding (experts prefer different models than novices) is robust and important, but specific model rankings and company differences should be cited cautiously pending more detailed analysis.

**DoD relevance:** HIGH. Most DoD AI applications will be used by military professionals (experts), not general public. General benchmarks and crowd ratings don't predict expert utility. This finding strongly supports need for expert evaluation panels in acquisition testing and cautions against relying on general-purpose benchmarks for professional/military applications.

**Practical value:** Immediately actionable—DoD acquisition can:
1. Require expert evaluations (not general benchmarks) for professional systems
2. Test for user heterogeneity in pilots (do results vary by user skill?)
3. Consider that thinking models may not be worth premium for all expert applications
4. Pay attention to company-level quality differences (large and consistent)
