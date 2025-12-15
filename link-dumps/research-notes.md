# Tag System Research Notes

This document records research findings on best practices for hierarchical tagging systems, conducted December 2025.

## Key Concepts

### Polyhierarchy
A taxonomy structure where terms can have multiple parent terms. This allows flexible categorization without duplicating entries.

**Source**: [Synaptica - On Polyhierarchy](https://synaptica.com/on-polyhierarchy/)

### Rules for Valid Polyhierarchy

1. **The All-Some Rule**: A term may have multiple parents if and only if each parent fulfills the criteria for permitted broader-narrower term relationships. The term and all its children must properly belong under each parent.

2. **Example**: "Educational software" can have both "Software" and "Educational products" as parents because it IS a kind of software AND IS a kind of educational product.

**Source**: [Hedden Information Management - Polyhierarchy in Taxonomies](https://www.hedden-information.com/polyhierarchy-in-taxonomies/)

### Best Practices

1. **Avoid mixing hierarchical relationship types**
   - Taxonomy standards describe three kinds of hierarchical relationships:
     - Generic-specific (is-a)
     - Generic-instance (is-an-instance-of)
     - Whole-part (is-part-of)
   - Don't create polyhierarchy that combines different types

2. **Avoid cross-facet polyhierarchy**
   - Facets should be mutually exclusive so they can be combined for filtering
   - Limit to 2-3 polyhierarchies across an entire faceted taxonomy

3. **Avoid overuse**
   - The most common mistake is giving terms multiple parents without sufficient reason
   - Each polyhierarchical relationship should be clearly justified

**Source**: [NN/Group - Polyhierarchies Improve Findability](https://www.nngroup.com/articles/polyhierarchy/)

### Taxonomy vs. Ontology

- **Taxonomy**: Organizes concepts hierarchically, defines categories, synonyms, and preferred terms
- **Ontology**: Goes further, mapping relationships, attributes, and rules about how concepts connect

For this link database, we use a taxonomic approach with limited ontological elements (relationships between links).

**Source**: [Synaptica - Knowledge Management, Knowledge Graphs, and Ontologies](https://synaptica.com/knowledge-management-knowledge-graphs-and-ontologies/)

### PKM Tagging Approaches

Two main paradigms:

1. **Hierarchical (top-down)**: Pre-defined structure, good for consistent categorization
2. **Network (bottom-up)**: Emergent structure through linking, more flexible

Our approach: **Hybrid** - Use hierarchical tags for broad categories, but allow network-style relationships between links.

**Source**: [Forte Labs - A Complete Guide to Tagging for Personal Knowledge Management](https://fortelabs.com/blog/a-complete-guide-to-tagging-for-personal-knowledge-management/)

### Faceted Classification

Rather than asking "Where do I put this?", ask "How can I describe this?"

Recommended limits:
- Top-level facets: 10-15 maximum
- Depth per facet: 2-4 levels

**Source**: [Contify - Guidelines For Building Your Taxonomy](https://www.contify.com/resources/blog/guidelines-for-building-your-taxonomy/)

## Design Decisions for This System

### Chosen Structure: Faceted + Polyhierarchical

1. **Top-level facets** (mutually exclusive dimensions):
   - Domain (AI Safety, AI Capabilities, Policy, Economics, etc.)
   - Content Type (Paper, Blog Post, Tool, Dataset, etc.)
   - Source Type (arXiv, Blog, News, Social Media, etc.)

2. **Within-facet hierarchy**: Allow polyhierarchy within Domain facet only
   - Example: "Alignment Faking" can be under both "Deception" and "Alignment"

3. **Cross-references via relationships**: Use `related_links` field rather than cross-facet polyhierarchy

### Tag Naming Conventions

- Use lowercase with hyphens: `ai-safety`, `red-teaming`
- Prefer specific over general: `llm-evaluations` over `evals`
- Include acronym expansion in tag metadata

### Importance Levels

- `low`: Background/contextual interest only
- `normal`: Relevant to current research
- `high`: Key paper or resource for active work
- `very-high`: Essential/foundational reference
