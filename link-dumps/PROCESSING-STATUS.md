# Link Processing Status

**Last Updated:** 2025-12-16

## Summary

- **Total links:** 618
- **Fully processed (with notes):** 21
- **Titles updated:** 21+
- **Pending full processing:** ~597

## Access Issues

Due to rate limiting and access restrictions, the following sources could not be directly fetched:

### Blocked by WebFetch (403 errors)
- **arxiv.org** - All arXiv papers blocked
- **anthropic.com** - Most pages blocked
- **openai.com** - Most pages blocked
- **lesswrong.com** - Blocked
- **alignmentforum.org** - Blocked
- **rand.org** - Blocked
- **blog.langchain.com** - Blocked

### Workaround Used
WebSearch was used to retrieve metadata and abstracts from search results, which worked for many papers but is slower and less complete than direct access.

## Links with Full Notes

The following links have been fully processed with abstracts/summaries in the `notes/` directory:

1. `arxiv-2411.00640` - Adding Error Bars to Evals
2. `arxiv-2405.19550` - Stress-Testing Capability Elicitation
3. `arxiv-2406.04313` - Improving Alignment with Short Circuiting
4. `arxiv-2512.07810` - Auditing Games for Sandbagging
5. `arxiv-2509.15541` - Stress Testing Deliberative Alignment
6. `arxiv-2504.05259` - Evaluating Control Measures for LLM Agents
7. `anthropic-how-ai-transforming-work` - How AI is Transforming Work at Anthropic
8. `arxiv-2407.09468` - AI Risk Management Should Incorporate Both Safety and Security
9. `arxiv-2406.02061` - MixEval: Deriving Wisdom of the Crowd
10. `arxiv-2407.14937` - Sycophancy to Subterfuge: Investigating Reward-Tampering
11. `arxiv-2411.12820` - BALROG: Benchmarking Agentic LLM Reasoners
12. `arxiv-2411.08088` - SWE-bench+ and MB+
13. `arxiv-2407.07890` - Representation Engineering: A Top-Down Approach
14. `arxiv-2401.03188` - Survey on V&V, T&E of Neurosymbolic AI
15. `arxiv-2407.16216` - Comprehensive Survey of LLM Alignment Techniques
16. `arxiv-2407.12784` - GenAI Paradox: What It Can Create, It May Not Understand
17. `arxiv-2407.11969` - Internal Consistency and Self-Feedback in LLMs
18. `arxiv-2412.02159` - Jailbreak Defense in a Narrow Domain
19. `arxiv-2503.19887` - AI Threats via Incident Regime
20. `arxiv-2504.13839` - Audit Cards: Contextualizing AI Evaluations
21. `arxiv-2504.15585` - LLM(-Agent) Full Stack Safety Survey

## Links Still Needing Processing

### High Priority (marked > or >> in original dumps)
All 14 high-importance links have had titles and importance updated. Notes still needed for:
- Most high-importance links

### By Source Type

| Source | Count | Status |
|--------|-------|--------|
| arXiv | 536 | Titles from URLs only; abstracts needed |
| Other | 60 | Need fetching/summarization |
| X/Twitter | 9 | Social media, limited metadata available |
| OpenAI | 3 | Need fetching |
| Substack | 3 | Need fetching |
| GitHub | 2 | Need fetching |
| Anthropic | 2 | 1 done, 1 pending |
| Google | 2 | Need fetching |
| Alignment Forum | 1 | Need fetching |
| LessWrong | 1 | Need fetching |

## Recommended Next Steps

1. **Batch process arXiv papers** - Use a local script or API to fetch arXiv metadata in bulk
2. **Process high-importance links first** - Focus on the 14 marked with > or >>
3. **Add notes incrementally** - Process links as they become relevant to active reviews
4. **Use WebSearch** - When direct access fails, search for paper titles to get metadata

## Notes Format

Each note file in `notes/` follows this template:

```markdown
# Paper Title

**arXiv/URL:** [link]
**Authors:** Names
**Date:** YYYY-MM-DD

## Abstract

[Original abstract from paper]

## Claude Summary

[2-3 paragraph summary including key findings and relevance]
```
