# A Rosetta Stone for AI Benchmarks

**Authors:** Anson Ho, Jean-Stanislas Denain, David Atanasov, Samuel Albanie, Rohin Shah
**Affiliations:** Epoch AI, DeepMind (Rohin Shah - AI safety researcher)
**Date:** November 28, 2025
**Type:** Academic Research Paper
**arXiv:** [2512.00193](https://arxiv.org/abs/2512.00193)

## Key Contributions

1. **Statistical framework for benchmark unification**: "Stitches benchmarks together" on single numerical scale despite different formats, domains, and difficulty levels
2. **Addresses benchmark saturation problem**: Enables long-term capability tracking even as individual benchmarks saturate
3. **Model-agnostic approach**: Works without assuming how capabilities evolve with time or compute
4. **Three validated applications**: Progress measurement, capability forecasting, cross-benchmark model comparison
5. **Safety relevance**: Rohin Shah involvement suggests connection to safety-relevant capability tracking

## Methodology

**Statistical Framework:**
- Likely uses Item Response Theory (IRT) or similar psychometric methods
- Calibrates model capabilities and benchmark difficulties on unified scale
- Enables cross-benchmark comparison without direct evaluation
- Works across different benchmark families and formats

**Applications Demonstrated:**
1. **Progress measurement**: Track AI capability trends over time despite benchmark turnover
2. **Capability forecasting**: Predict future model capabilities based on historical trends
3. **Cross-benchmark comparison**: Compare models evaluated on different benchmarks

**Key Innovation:** Framework doesn't require assumptions about scaling laws or capability evolution—data-driven calibration only.

## Key Findings

### 1. Benchmark Saturation is Tractable Problem

Most AI benchmarks saturate within years or months, making long-run trend analysis difficult. This framework solves the problem by:
- Creating unified capability scale across benchmarks
- Enabling comparison even when models aren't evaluated on same benchmarks
- Supporting longitudinal analysis despite benchmark lifecycle turnover

### 2. Cross-Benchmark Calibration is Possible

Despite vast differences in benchmark formats (multiple choice, code generation, dialogue, etc.), statistical calibration can place them on common scale:
- Model capabilities → numerical scores on unified scale
- Benchmark difficulties → numerical ratings on same scale
- Enables "apples-to-apples" comparison across benchmark families

### 3. Capability Forecasting Without Scaling Law Assumptions

Framework enables capability prediction without assuming specific functional form (power law, exponential, etc.):
- Data-driven approach more robust than parametric assumptions
- Can detect changes in progress rate (acceleration/deceleration)
- Important for AI safety and policy planning

## Relevance to GenAI Productivity Review

### Part 1: The Benchmark-Utility Gap

**Moderate relevance.** While focused on benchmark-to-benchmark comparison rather than benchmark-to-utility gap, provides important context:

**Benchmark saturation dynamics:**
- Rapid saturation (months to years) means benchmarks have short useful life
- Creates pressure to constantly develop new benchmarks
- Contributes to benchmark proliferation and inconsistent measurement

**Doesn't directly address utility gap:**
- Framework unifies *benchmarks*, not benchmarks-to-real-world-utility
- Could theoretically extend to include operational metrics, but paper doesn't demonstrate this

**Connection to [bean2025construct](bean2025construct.md):** Bean shows benchmarks often don't measure what they claim (construct validity). Ho et al. assume benchmarks are valid measures and focus on calibration. Complementary problems: even if calibration works, underlying validity issues remain.

### Part 2: The State of the Field (Literature Review)

**Important methodological contribution.** Represents sophisticated approach to persistent measurement problem in AI evaluation. Should be included as example of advanced evaluation methodology, though not directly about productivity.

### Part 3: A Framework for AI Evaluation

**Valuable for evaluation design:**

**For DoD evaluators:**
1. **Benchmark lifecycle management**: Plan for saturation; need portfolio of benchmarks at different difficulty levels
2. **Cross-benchmark comparison**: Use statistical calibration when vendors evaluated on different benchmarks
3. **Capability forecasting**: Predict when current systems will become inadequate
4. **Unified capability assessment**: Track organizational capability trends despite changing evaluation tools

**Limitations for DoD:**
- Framework requires substantial data (many models × many benchmarks)
- DoD may not have luxury of many evaluations
- Assumes benchmarks measure same underlying construct (questionable per Bean et al.)

### Part 4: Practical Guidance for Acquisition Decision-Makers

**Practical lessons:**

1. **Benchmark saturation is normal:**
   - Don't be surprised when benchmarks saturate quickly
   - Plan for benchmark turnover in evaluation strategy
   - Maintain portfolio of benchmarks at varying difficulty levels

2. **Cross-vendor comparison is possible but complex:**
   - Vendors will report scores on different benchmarks
   - Statistical calibration can help (but requires expertise)
   - Consider requiring common benchmark subset for fair comparison

3. **Capability forecasting has value:**
   - Can predict when systems will need refresh/upgrade
   - Helps with acquisition timeline planning
   - But requires historical data and stable evaluation approach

4. **Be cautious with unified scores:**
   - Attractive to collapse multiple benchmarks into single number
   - But loses information about jagged frontier (different strengths/weaknesses)
   - Use for trend analysis, not point-in-time decisions

### Part 5: T&E Considerations for GenAI-Based Systems

**T&E framework implications:**

1. **Longitudinal testing strategy:**
   - Plan for benchmark portfolio evolution
   - Use calibration to maintain consistency across benchmark changes
   - Track relative position even as absolute benchmarks change

2. **Cross-system comparison:**
   - When systems evaluated on different benchmarks, use statistical calibration
   - Requires psychometric expertise (consider contractor support)

3. **Capability tracking:**
   - Monitor both absolute performance and relative-to-frontier position
   - Detect when system falling behind state-of-art

### Part 6: Research Agenda and Investment Priorities

**Research directions:**

1. **Extend to operational metrics:**
   - Can "Rosetta Stone" framework unify benchmarks AND operational performance?
   - Could link benchmark scores to real-world productivity, safety, reliability
   - Would directly address benchmark-utility gap

2. **DoD-specific calibration:**
   - Build calibration dataset for military-relevant benchmarks
   - Enable cross-vendor comparison on DoD tasks
   - Support capability forecasting for defense applications

3. **Limitations research:**
   - When does calibration break down? (e.g., fundamentally different capabilities)
   - How much data needed for reliable calibration?
   - How to handle jagged frontier (different capability profiles)?

4. **Safety applications:**
   - Rohin Shah involvement suggests safety focus
   - Could support risk forecasting (when will dangerous capabilities emerge?)
   - Important for proactive safety planning

## Critical Assessment

**Strengths:**
- Addresses real, persistent problem (benchmark saturation)
- Sophisticated statistical methodology
- Model-agnostic approach (doesn't assume scaling laws)
- Three validated applications demonstrated
- Strong author team (Epoch AI, DeepMind)
- Rohin Shah involvement signals AI safety relevance

**Limitations:**
- **Data requirements**: Needs many models × many benchmarks for calibration
- **Assumes construct validity**: Calibration doesn't fix underlying validity problems ([bean2025construct](bean2025construct.md))
- **Benchmark-to-benchmark only**: Doesn't link to real-world utility
- **Collapses jagged frontier**: Unified scale loses information about differential strengths
- **Limited detail**: Note file based on abstract—full paper methodology unclear
- **Not yet peer-reviewed**: November 2025 preprint

**Currency:** Excellent—November 2025, very recent work.

**Evidence Quality:** Unclear from available information (abstract only). Strong author team and Epoch AI affiliation suggest high quality, but full methodology and results not available in note file. Should read full paper for complete assessment.

## Connections to Other References

**Methodological complement to:**
- [bean2025construct](bean2025construct.md): Bean addresses construct validity (what benchmarks measure); Ho addresses calibration (how to compare across benchmarks). Both needed for sound evaluation.
- [brand2025benchmarking](brand2025benchmarking.md): Brand shows 11-15% variance from scaffolds; Ho's calibration could potentially account for some scaffold variance

**Addresses saturation problem mentioned in:**
- Multiple references note rapid benchmark saturation
- This framework provides potential solution

**Doesn't directly connect to:**
- Productivity studies (different focus)
- Production agent reality ([pan2025agents](pan2025agents.md))
- Benchmark-utility gap (calibrates benchmarks, doesn't link to utility)

**Could theoretically extend to:**
- Unified scale including both benchmarks AND operational metrics
- Would require someone to do the work of calibrating real-world performance against benchmarks
- Potentially valuable future direction

## Questions/Notes

1. **What statistical method exactly?**
   - Note file suggests IRT (Item Response Theory)
   - Need to read full paper for details
   - Important for understanding assumptions and limitations

2. **How much data required for calibration?**
   - DoD may not have resources for extensive benchmarking
   - What's minimum dataset for reliable calibration?

3. **How to handle jagged frontier?**
   - Unified scale collapses multidimensional capabilities to one number
   - Loses information about differential strengths/weaknesses
   - Can framework preserve capability profiles?

4. **Can this extend to operational metrics?**
   - Framework calibrates benchmarks to each other
   - Could it calibrate benchmarks to real-world utility?
   - Would directly address benchmark-utility gap if possible

5. **Safety applications?**
   - Rohin Shah is AI safety researcher
   - How does this support safety work?
   - Capability forecasting for dangerous capabilities?

6. **How robust to construct validity failures?**
   - Bean et al. show many benchmarks don't measure what they claim
   - If benchmarks measure different things, calibration may be meaningless
   - Need to validate construct similarity before calibration

## Citation Guidance

**Appropriate uses:**
- Citing framework for cross-benchmark comparison
- Documenting benchmark saturation as tractable problem
- Supporting capability forecasting methodology
- Explaining need for benchmark portfolio management
- Referencing statistical approaches to benchmark calibration

**Inappropriate uses:**
- Claiming this solves benchmark-utility gap (it doesn't—calibrates benchmarks to each other, not to utility)
- Using without considering construct validity issues (calibration ≠ validity)
- Citing as peer-reviewed work (preprint as of Nov 2025)
- Applying to DoD without considering data requirements and operational constraints
- Collapsing jagged frontier without acknowledging information loss

**Citation note:** High-quality preprint from strong team (Epoch AI, DeepMind). Rohin Shah involvement suggests AI safety relevance. Suitable for citing as "recent methodological work on benchmark calibration" with caveats about preprint status and limited detail available. Should read full paper before relying heavily on specific methodological claims.

**DoD relevance:** Moderate direct relevance (benchmark calibration for cross-vendor comparison), but could become highly relevant if extended to include operational metrics. Framework provides sophisticated approach to persistent measurement problem (benchmark saturation), which DoD will face in long-term AI acquisition programs. Worth monitoring as methodology matures.

**Note for full paper review:** This summary based on abstract and note file only. Should read full paper for:
- Detailed statistical methodology
- Data requirements and sample sizes
- Validation results for three applications
- Limitations and assumptions
- Potential extensions to operational metrics
