---
name: citation-helper
description: Citation and bibliography management for academic research. Use this skill when generating BibTeX entries, formatting citations, validating references, or exporting bibliographies. Ensures accurate, properly formatted citations.
---

# Citation Helper

This skill assists with managing citations and generating properly formatted bibliographies for your literature review.

## When to Use This Skill

- Converting paper metadata to BibTeX format
- Validating citation accuracy
- Generating bibliographies in various styles
- Checking reference completeness
- Formatting in-text citations

## BibTeX Entry Types

### Common Entry Types

| Type | Use For |
|------|---------|
| `@article` | Journal articles |
| `@inproceedings` | Conference papers |
| `@book` | Books |
| `@incollection` | Book chapters |
| `@techreport` | Technical reports |
| `@phdthesis` | PhD dissertations |
| `@mastersthesis` | Master's theses |
| `@misc` | arXiv preprints, websites, other |
| `@online` | Web resources (with access date) |

### Required Fields by Type

**@article**:
```bibtex
@article{key,
  author = {Last, First and Last2, First2},
  title = {Article Title},
  journal = {Journal Name},
  year = {2024},
  volume = {10},
  number = {2},
  pages = {1--15},
  doi = {10.xxxx/xxxxx}
}
```

**@inproceedings**:
```bibtex
@inproceedings{key,
  author = {Last, First},
  title = {Paper Title},
  booktitle = {Proceedings of Conference Name},
  year = {2024},
  pages = {100--110},
  publisher = {Publisher},
  doi = {10.xxxx/xxxxx}
}
```

**@misc (for arXiv)**:
```bibtex
@misc{key,
  author = {Last, First},
  title = {Paper Title},
  year = {2024},
  eprint = {2401.12345},
  archiveprefix = {arXiv},
  primaryclass = {cs.CL}
}
```

## Key Generation Convention

Generate consistent, memorable keys:

```
[firstauthor][year][keyword]
```

Examples:
- `vaswani2017attention` - Vaswani et al.'s 2017 attention paper
- `brown2020gpt3` - Brown et al.'s GPT-3 paper
- `smith2024survey` - Smith's 2024 survey

Rules:
- Lowercase first author's last name
- 4-digit year
- Short keyword from title (lowercase)
- No spaces or special characters

## Author Formatting

### Standard Format
```
Last, First and Last2, First2 and Last3, First3
```

### Examples
```bibtex
author = {Smith, John and Doe, Jane},
author = {Van Rossum, Guido},
author = {de la Cruz, Maria},
author = {O'Brien, Patrick}
```

### Many Authors
For papers with many authors, list all or use:
```bibtex
author = {Smith, John and others}
```

## Title Formatting

### Preserving Capitalization
Use braces to preserve capitalization of acronyms and proper nouns:

```bibtex
title = {{BERT}: Pre-training of Deep Bidirectional {Transformers}},
title = {Exploring {GPT-4}'s Capabilities in {NLP} Tasks}
```

### Special Characters
```bibtex
title = {The {$\alpha$}-{$\beta$} Algorithm},
title = {M{\"u}ller's Method}
```

## DOI Best Practices

- Always include DOI when available
- Format: `doi = {10.xxxx/xxxxx}` (without URL prefix)
- DOIs are permanent; prefer over URLs
- For arXiv, use `eprint` field instead

## Converting from references.yaml

When exporting from your `references.yaml` to BibTeX:

```yaml
# From references.yaml
- key: smith2024transformers
  title: "Transformers for Scientific Discovery"
  authors: ["Smith, J.", "Doe, A."]
  year: 2024
  url: "https://arxiv.org/abs/2401.12345"
  source: arxiv
```

```bibtex
# To BibTeX
@misc{smith2024transformers,
  author = {Smith, J. and Doe, A.},
  title = {Transformers for Scientific Discovery},
  year = {2024},
  eprint = {2401.12345},
  archiveprefix = {arXiv},
  primaryclass = {cs.LG}
}
```

## Validation Checklist

Before finalizing bibliography:

- [ ] All required fields present for entry type
- [ ] Author names consistently formatted
- [ ] Titles properly capitalized (braces where needed)
- [ ] Years are 4 digits
- [ ] DOIs included where available
- [ ] No duplicate keys
- [ ] Keys follow naming convention
- [ ] Special characters properly escaped
- [ ] URLs have access dates if needed

## Common Citation Styles

### APA (7th Edition)
```
Smith, J., & Doe, A. (2024). Paper title. Journal Name, 10(2), 1-15. https://doi.org/10.xxxx/xxxxx
```

### IEEE
```
[1] J. Smith and A. Doe, "Paper title," Journal Name, vol. 10, no. 2, pp. 1-15, 2024.
```

### Chicago
```
Smith, John, and Alice Doe. "Paper Title." Journal Name 10, no. 2 (2024): 1-15.
```

### Nature
```
Smith, J. & Doe, A. Paper title. Journal Name 10, 1-15 (2024).
```

## In-Text Citation Formats

### Narrative
- APA: Smith and Doe (2024) found that...
- IEEE: Smith and Doe [1] found that...

### Parenthetical
- APA: Previous work has shown... (Smith & Doe, 2024)
- IEEE: Previous work has shown... [1]

### Multiple Citations
- APA: (Smith, 2024; Doe, 2023; Brown et al., 2022)
- IEEE: [1]-[3] or [1, 2, 3]

## Handling Edge Cases

### No Author
```bibtex
author = {{Organization Name}},
# or
author = {{Anonymous}}
```

### In Press
```bibtex
year = {in press},
note = {Accepted for publication}
```

### Preprints
```bibtex
note = {Preprint, not peer-reviewed}
```

### Multiple Works Same Author/Year
```bibtex
@article{smith2024a,
  ...
}
@article{smith2024b,
  ...
}
```

## Quick Commands

| Task | Action |
|------|--------|
| Export all refs | `/export-bib` |
| Validate citations | Check against this guide |
| Convert DOI to BibTeX | Use WebFetch on `https://doi.org/[doi]` with `Accept: application/x-bibtex` concept |

---

*Adapted from K-Dense-AI/claude-scientific-writer citation-management skill (MIT License).*
