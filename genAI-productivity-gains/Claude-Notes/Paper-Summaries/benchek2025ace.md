# The AI Consumer Index (ACE)

**Authors:** Julien Benchek, Rohit Shetty, Benjamin Hunsberger, Ajay Arun, Zach Richards, Brendan Foody, Osvald Nitski, Bertie Vidgen
**Affiliations:** Not specified in note (likely industry/research lab based on benchmark scope)
**Date:** December 4, 2025 (v1), revised December 9, 2025 (v3)
**Type:** Benchmark Paper
**arXiv:** [2512.04921](https://arxiv.org/abs/2512.04921)

## Key Contributions

1. **First consumer task benchmark**: Evaluates frontier AI on everyday consumer tasks (shopping, food, gaming, DIY)
2. **Grounding-based evaluation**: Novel methodology dynamically checks whether responses are grounded in retrieved web sources
3. **Hidden holdout set**: 400 test cases (prevents overfitting) + 80 open-source dev cases (CC-BY license)
4. **Low frontier performance documented**: Top model (GPT-5 Thinking=High) scores only 56.1%
5. **Domain-specific variation**: Shopping domain shows <50% performance (significant gaps across consumer activities)

## Methodology

**Benchmark Design:**
- **Test cases**: 400 (hidden holdout set for leaderboard)
- **Dev set**: 80 cases (open-sourced with CC-BY license)
- **Domains**: 4 consumer activities
  1. Shopping
  2. Food (recipes, nutrition, etc.)
  3. Gaming
  4. DIY (home improvement, repairs, etc.)

**Evaluation Setup:**
- **Web search enabled** (realistic consumer use case)
- **Grounding check**: Responses must be grounded in retrieved web sources
- **Dynamic grading**: Checks specific parts of response against sources (not just binary correct/incorrect)
- **10 frontier models evaluated** (as of Dec 2025)

**Novel Grounding Methodology:**
- Checks whether relevant response parts are grounded in retrieved web sources
- Prevents credit for hallucinated information
- More realistic than traditional benchmark evaluation (consumers need reliable info, not creative guesses)

## Key Findings

### 1. Low Overall Performance (56.1% Top Score)

**Leaderboard (Top 3):**
1. **GPT-5 (Thinking = High): 56.1%** (top performer)
2. **o3 Pro (Thinking = On): 55.2%**
3. **GPT-5.1 (Thinking = High): 55.1%**

**Interpretation:**
- Even best models fail on nearly half of consumer tasks
- Substantial gap between frontier capabilities and practical consumer utility
- Thinking models show advantage (top 3 all use thinking/reasoning)

### 2. Significant Domain Variation

**Shopping domain: <50%** (top model underperforms)
- Lower than other domains
- Suggests specific challenges in product search, price comparison, recommendations

**Implication:**
- Uneven capability profiles across consumer activities
- Can't assume performance on one task predicts performance on others
- Reinforces "jagged frontier" concept from other research

### 3. Web Grounding is Critical Bottleneck

**Grounding-based evaluation methodology reveals:**
- Models struggle to properly ground responses in retrieved sources
- May generate plausible-sounding but unverified information
- Gap between retrieval and reliable synthesis

## Relevance to GenAI Productivity Review

### Part 1: The Benchmark-Utility Gap

**Provides complementary perspective.** Most productivity studies focus on professional work (coding, writing, customer service), but consumer tasks represent large potential economic impact.

**56.1% top score illustrates utility gap:**
- Frontier models can't reliably handle everyday consumer tasks
- Suggests benchmark-to-utility gap extends beyond professional productivity
- Even basic "search and synthesize" tasks challenging

**Connects to:**
- [bean2025construct](bean2025construct.md): Benchmarks may not measure what they claim—ACE explicitly tests practical utility
- **Scale Remote Labor Index** (2.5% automation): Professional tasks hard to automate; ACE shows consumer tasks also challenging

**Different from:**
- Productivity benchmarks (professional work)
- Academic benchmarks (abstract reasoning)
- ACE tests practical, everyday utility

### Part 2: The State of the Field (Literature Review)

**Moderate inclusion priority.** Not directly about productivity gains, but provides important context:
- Broadens view of AI capabilities beyond professional productivity
- Documents frontier model limitations on practical tasks
- Shows grounding/retrieval challenges

**Complements other findings:**
- Professional productivity studies (limited automation success)
- ACE: Consumer task automation also limited
- **Pattern**: High benchmark scores ≠ practical utility across domains

### Part 3: A Framework for AI Evaluation

**Grounding-based evaluation methodology is valuable innovation:**

**For DoD evaluations:**
1. **Require grounding checks**: Don't credit responses unless grounded in evidence
   - Critical for intelligence analysis, operational planning
   - Hallucinated information is worse than no information
2. **Web-enabled evaluation**: Test models as they'll be used (with retrieval/search)
   - More realistic than static knowledge tests
3. **Domain-specific testing**: Performance varies significantly across domains
   - Test in actual military domains (don't extrapolate from shopping/DIY)

**Limitations of ACE for DoD:**
- Consumer tasks ≠ military tasks
- But methodology (grounding checks, domain-specific evaluation) is transferable

### Part 4: Practical Guidance for Acquisition Decision-Makers

**Key lessons for DoD acquisition:**

1. **Don't assume web-enabled AI solves retrieval problems:**
   - Even with web search, top model only 56.1%
   - Retrieval + synthesis is harder than it looks
   - Test grounding quality, not just response plausibility

2. **Expect domain-specific performance:**
   - Shopping <50% while overall 56.1%
   - Military domains may have own performance profiles
   - Can't extrapolate from general benchmarks to specific DoD applications

3. **Grounding is critical for mission outcomes:**
   - ACE penalizes ungrounded responses
   - DoD should too (hallucinated intel analysis = mission failure)
   - Require evidence trails for AI-generated outputs

4. **Consumer utility ≠ irrelevant to DoD:**
   - Many military personnel use AI for personal tasks
   - Consumer-facing DoD services (benefits, recruitment, family support)
   - Dual-use applications

5. **Thinking models may help:**
   - Top 3 all use thinking/reasoning modes
   - But still only 56.1%—not silver bullet
   - Cost-benefit analysis required

### Part 5: T&E Considerations for GenAI-Based Systems

**Grounding-based evaluation is applicable to DoD:**

1. **Evidence grounding requirements:**
   - For intelligence analysis: Require AI to cite sources
   - For operational planning: Ground recommendations in doctrine/precedent
   - For technical analysis: Link claims to specifications/data

2. **Domain-specific test suites:**
   - Develop military equivalents of ACE domains
   - Intelligence tasks, logistics tasks, planning tasks, etc.
   - Measure cross-domain variation (like shopping <50%)

3. **Retrieval + synthesis testing:**
   - Don't test knowledge alone (unrealistic)
   - Test with realistic information access (databases, manuals, intelligence feeds)
   - Measure grounding quality separately from response quality

4. **Hallucination detection:**
   - ACE methodology could adapt to detect ungrounded military claims
   - Critical for safety in high-stakes decisions

### Part 6: Research Agenda and Investment Priorities

**Research gaps:**

1. **Military consumer tasks:**
   - Service members use AI for personal tasks (housing, benefits, education)
   - Need DoD-specific consumer benchmark
   - Dual-use applications

2. **Professional task grounding:**
   - ACE tests consumer tasks; what about professional/military grounding?
   - Intelligence analysis grounding requirements
   - Technical documentation synthesis grounding

3. **Grounding methodology for military sources:**
   - ACE uses web sources; military uses classified databases
   - Adapt grounding checks for restricted information environments
   - Citation/audit trail requirements

4. **Domain-specific performance prediction:**
   - ACE shows shopping <50%; what predicts military domain performance?
   - Can we forecast domain-specific success without full evaluation?

**Investment priorities:**
- Develop grounding-based evaluation tools for military applications
- Build military task benchmarks across domains (intel, logistics, planning, technical)
- Research grounding requirements for different military use cases
- Fund tools for evidence trail verification in AI systems

## Critical Assessment

**Strengths:**
- Fills important gap (consumer tasks vs. academic/professional benchmarks)
- Novel grounding-based methodology
- Hidden holdout set (prevents overfitting)
- Open dev set (80 cases with CC-BY license)
- Domain-specific analysis (not just overall score)
- Realistic setup (web search enabled)
- Recent (December 2025)

**Limitations:**
- **Limited scope**: Only 4 consumer domains (shopping, food, gaming, DIY)
- **Small dev set**: 80 open cases may not be enough for development
- **Consumer focus**: Not directly relevant to professional/military productivity
- **Grounding methodology details unclear**: Note file doesn't provide full methodology
- **Limited model coverage**: 10 frontier models (as of Dec 2025)
- **No difficulty analysis**: Don't know which types of tasks are hardest
- **Preprint status**: arXiv paper, not yet peer-reviewed
- **No user study**: Benchmark evaluation only (not tested with real consumers)

**Currency:** Excellent—December 2025, very recent.

**Evidence Quality:** Medium. Sound benchmark design with novel grounding methodology, but limited detail available in note file. Need full paper for complete assessment of methodology rigor and validation. Preprint status (not peer-reviewed) is limitation.

## Connections to Other References

**Methodological innovation:**
- [bean2025construct](bean2025construct.md): Bean critiques benchmarks for construct validity; ACE addresses by explicitly testing practical utility
- [brand2025benchmarking](brand2025benchmarking.md): Brand shows 11-15% variance from scaffolds; ACE controls by testing with realistic setup (web search enabled)

**Complements productivity findings:**
- **Scale Remote Labor Index**: 2.5% automation on professional tasks
- **ACE**: 56.1% (actually 43.9% failure rate) on consumer tasks
- **Pattern**: Both professional and consumer automation challenging

**Contrasts with:**
- **Academic benchmarks** (MMLU, etc.): High scores on abstract reasoning
- **ACE**: Low scores on practical tasks
- **Reinforces**: Benchmark-utility gap across domains

**Grounding connects to:**
- [pan2025agents](pan2025agents.md): 74% of production agents use human evaluation
  - Grounding checks could partially automate validation
  - But ACE shows even grounding is hard (56.1%)

**Domain variation connects to:**
- **Jagged frontier concept** (Toner, BCG/Wharton)
- Shopping <50%, other domains higher
- Can't assume uniform capability across tasks

## Questions/Notes

1. **What makes shopping domain harder?**
   - <50% vs. 56.1% overall
   - Product search complexity? Price comparison? Subjective preferences?
   - Understanding could inform military applications (logistics = shopping-like?)

2. **How does grounding methodology work exactly?**
   - Dynamic checking against sources
   - But how to handle partial grounding?
   - What about synthesis (combining multiple sources)?

3. **Would military tasks show similar performance?**
   - Consumer tasks are lower stakes
   - Military tasks may be harder (classified sources, adversarial environments)
   - Need DoD-specific benchmarking

4. **How does thinking mode help?**
   - Top 3 all use thinking/reasoning
   - What aspect of consumer tasks benefits from extended reasoning?
   - Cost-benefit analysis (thinking modes more expensive)

5. **Hallucination rates?**
   - Grounding methodology catches ungrounded responses
   - What % of failures are hallucinations vs. other errors?
   - Critical for understanding safety risks

6. **User satisfaction vs. grounding accuracy:**
   - Grounding is objective metric
   - But do users care? Or prefer plausible-sounding hallucinations?
   - Important for understanding real-world deployment

7. **Improvement trajectory:**
   - 56.1% now; what was it for earlier models?
   - Progress rate on practical tasks vs. academic benchmarks?
   - Forecasting when consumer automation becomes viable

## Citation Guidance

**Appropriate uses:**
- Citing 56.1% top score as evidence of practical utility gap
- Documenting grounding-based evaluation methodology
- Supporting domain-specific performance variation (shopping <50%)
- Referencing consumer task benchmark as complement to professional productivity studies
- Citing novel evaluation approach (checking grounding in retrieved sources)

**Inappropriate uses:**
- Claiming consumer tasks irrelevant to military (dual-use, service member personal use, public-facing DoD services)
- Using consumer task performance to predict professional/military performance (different domains)
- Citing as peer-reviewed research (preprint as of Dec 2025)
- Claiming all retrieval tasks will show similar performance (only 4 domains tested)
- Using specific model rankings without caveats (benchmark may not be representative)

**Citation note:** Sound benchmark design addressing important gap (practical consumer utility), but preprint status and limited methodological detail in note file are limitations. Grounding-based evaluation methodology is valuable innovation that could transfer to military applications. Suitable for citing as "recent evidence of frontier model limitations on practical tasks" with appropriate caveats.

**DoD relevance:** Moderate direct relevance (consumer tasks ≠ military tasks), but HIGH methodological relevance. Grounding-based evaluation approach is directly applicable to military intelligence analysis, operational planning, and technical documentation synthesis. The core insight (frontier models struggle with practical retrieval + synthesis tasks) likely generalizes to military domains. Domain-specific performance variation (shopping <50%) suggests military applications will also show uneven capability profiles requiring domain-specific evaluation.

**Practical value for DoD:**
1. Adopt grounding-based evaluation for military applications
2. Expect domain-specific performance variation (test in actual military domains)
3. Don't assume web-enabled AI solves retrieval problems (56.1% top score)
4. Develop evidence trail requirements for AI-generated military outputs
5. Consider dual-use applications (service member personal use, public-facing services)
