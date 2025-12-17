# A Survey of Context Engineering for Large Language Models

**Authors:** Lingrui Mei, Jiayu Yao, Yuyao Ge, Yiwei Wang, Baolong Bi, Yujun Cai, Jiazhi Liu, Mingyu Li, Zhong-Zhi Li, Duzhen Zhang, Chenlin Zhou, Jiayi Mao, Tianze Xia, Jiafeng Guo, Shenghua Liu
**Year:** 2025 (July)
**URL:** https://arxiv.org/abs/2507.13334

## Key Contributions

1. **Introduces Context Engineering as formal discipline** - transcends simple prompt design to encompass systematic optimization of information payloads for LLMs
2. **Comprehensive taxonomy** decomposing Context Engineering into Foundational Components and System Implementations
3. **Massive scale:** 165 pages, 1,400+ papers reviewed, establishing technical roadmap for the field
4. **Critical research gap identified:** Models understand complex contexts but struggle to generate equally sophisticated outputs

## Methodology

Systematic literature review of 1,400+ research papers. Provides evolution timeline from 2020-2025 showing progression from foundational RAG to multi-agent architectures.

## Key Findings

### Taxonomy: Foundational Components

| Component | Description | Sub-areas |
|-----------|-------------|-----------|
| **Context Retrieval & Generation** | Acquiring contextual information | Prompt-based generation, external knowledge acquisition |
| **Context Processing** | Handling context content | Long sequence processing, self-refinement, structured info integration |
| **Context Management** | Organizing context | Memory hierarchies, compression, optimization |

### Taxonomy: System Implementations

| System Type | Description | Variants |
|-------------|-------------|----------|
| **RAG** | Retrieval-Augmented Generation | Modular, agentic, graph-enhanced architectures |
| **Memory Systems** | Persistent interactions | Enables context retention across sessions |
| **Tool-Integrated Reasoning** | External tool use | Function calling, environmental interaction |
| **Multi-Agent Systems** | Coordinated agents | Communication, orchestration protocols |

### Critical Research Gap

> "A fundamental asymmetry exists between model capabilities. While current models, augmented by advanced context engineering, demonstrate remarkable proficiency in understanding complex contexts, they exhibit pronounced limitations in generating equally sophisticated, long-form outputs."

**Implication for evaluation:** Must separately assess comprehension (input processing) vs. generation (output quality).

### Performance Benchmarks

- **AIME2024 improvement:** GPT-4.1 performance increased from 26.7% to 43.3% through structured cognitive operation sequences
- Demonstrates measurable impact of context engineering on reasoning tasks

### Evolution Timeline (2020-2025)

- **2020-2021:** Foundational RAG systems
- **2022-2023:** Modular RAG, memory augmentation
- **2024-2025:** Sophisticated multi-agent architectures, tool-integrated reasoning

## Relevance to Review

**Highly relevant for understanding the broader landscape of context engineering evaluation.** Key insights:

### For Prompt Evaluation

1. **Context Engineering > Prompt Engineering** - Prompts are just one component of the broader context optimization challenge
2. **Two-part evaluation needed:**
   - Can the model understand the context provided? (comprehension)
   - Can the model generate appropriate outputs? (generation quality)
3. **System-level evaluation:** RAG, memory, tools, multi-agent all require different evaluation approaches

### Mapping to Evaluation Approaches

| Context Engineering Component | Relevant Evaluation Approach |
|-------------------------------|------------------------------|
| Context Retrieval | IR metrics (Recall@k, Precision@k) - aligns with husain2025evalsfaq |
| Context Processing | Long-context benchmarks |
| RAG Systems | Two-stage: retrieval + generation evaluation |
| Memory Systems | Consistency, retention, appropriate recall |
| Tool-Integrated Reasoning | Tool selection accuracy, parameter extraction |
| Multi-Agent Systems | Coordination effectiveness, role fulfillment |

### Key Insight for This Review

Context Engineering framing suggests **prompt evaluation is a subset of context evaluation.** Effective prompt evaluation must consider:
- What other context is provided (system prompts, retrieved docs, tool results)
- How context is processed and managed
- The comprehension vs. generation asymmetry

## Citations to Follow

- **Companion GitHub repo:** Awesome-Context-Engineering - comprehensive implementation guides
- **AIME2024 benchmark** - cognitive operation sequences evaluation
- **Individual papers** on RAG evaluation, memory systems evaluation
- **Graph-enhanced RAG** architectures (GraphRAG)

## Questions/Notes

- **Strength:** Most comprehensive survey of context engineering (1,400+ papers)
- **Strength:** Establishes formal discipline and taxonomy
- **Strength:** Identifies critical gap (comprehension vs. generation asymmetry)
- **Practical insight:** Context Engineering as umbrella term helps organize evaluation approaches
- **Gap:** Limited specific guidance on *how* to evaluate each component
- **Gap:** Taxonomy is descriptive, not prescriptive for evaluation
- **Currency:** July 2025, very current
- **Connects to:** husain2025evalsfaq (RAG evaluation, agentic evaluation align with taxonomy)

## Evidence Quality

**High for taxonomy and landscape coverage.** Systematic review of 1,400+ papers provides authoritative taxonomy. Cannot directly cite for specific evaluation methodologies (survey scope is broader than evaluation). Strong for "what components exist" and "how systems are architected"; weaker for "how to evaluate."
