---
name: zotero-obsidian-bridge
description: Use this skill when Zotero is the literature source of truth and the bound project KB should receive paper source notes under Sources/Papers plus project-linked synthesis in Knowledge and Writing.
version: 0.3.0
---

# Zotero Obsidian Bridge

Use this skill when papers live in Zotero and the project KB should receive project-local notes.

Default flow:

```text
Zotero -> Sources/Papers -> Knowledge -> Writing -> Maps/literature.canvas
```

## Core stance

- Zotero owns collection metadata, attachments, PDFs, annotations, and full text when available.
- The project KB owns durable project-facing notes, synthesis, cross-note links, and writing-ready literature structure.
- Resolve or bootstrap the project through `obsidian-project-kb-core` before ingesting.
- Keep one canonical paper note per paper under `Sources/Papers/`.
- Treat `Sources/Papers/` notes as source-centered notes, not final literature synthesis.
- Route durable synthesis into `Knowledge/`.
- Route manuscript-facing deliverables into `Writing/`.
- Keep `Maps/literature.canvas` as the default derived artifact, not the source of truth.
- Update `_system/registry.md`, `02-Index.md`, and today's `Daily/` after substantial ingestion or synthesis.
- Repo-local `.opencode/project-memory/*` remains runtime binding metadata only.

## Evidence extraction requirement

Core papers and papers with reusable claims should include an evidence record. Abstract-only or placeholder notes may stay in `To-Read` until there is enough evidence to extract a reusable claim.

```md
## Evidence Record

Evidence ID:
Source:
Source type: full paper | preprint | dataset | experiment artifact | project note | abstract-only | webpage placeholder
Supports:
Contradicts:
Method / dataset / metric:
Limitation:
Project relevance:
Claim strength: speculative | observed | supported | strong
```

Use `../research-ideation/references/research-contract.md` as the shared contract for Evidence Records and claim strength definitions.

Before synthesis lands in `Knowledge/` or `Writing/`, apply the shared Claim Promotion Gate:
- every promoted claim must point back to an Evidence Record ID,
- source type must be strong enough for the claim,
- abstract-only and webpage-placeholder items cannot support durable claims,
- allowed wording and forbidden stronger wording must be preserved when the claim may later enter a report, manuscript, or rebuttal.

## Default workflow

1. Resolve the current project with `obsidian-project-kb-core`.
   - If the repo is already bound, use the existing vault project root.
   - If it looks like a research repo but is not bound, bootstrap it first.
2. Read Zotero items from the requested collection, query, DOI list, or explicit item set.
   - If the user asked for full collection coverage, do not stop at a representative subset.
   - If MCP transport fails but a local Zotero fallback is available, use that instead of stopping.
3. For each paper:
   - get metadata,
   - get full text when available,
   - get annotations/notes when helpful,
   - create or update the canonical note in `Sources/Papers/`.
4. Keep each paper note source-centered:
   - summary,
   - key claims,
   - methods,
   - evidence,
   - limitations,
   - project relevance,
   - links to related papers and synthesis notes.
5. When the batch yields durable synthesis, create or update project notes such as:
   - `Knowledge/Literature Overview.md`
   - `Knowledge/Method Taxonomy.md`
   - `Knowledge/Research Gaps.md`
   - `Writing/related-work-draft.md` only when promoted claims pass the evidence gate
6. Refresh `Maps/literature.canvas` when the user asked for the literature map or when the workflow explicitly depends on it.
7. Run deterministic follow-up maintenance:
   - `_system/registry.md`
   - `02-Index.md`
   - today's `Daily/`
   - repo-local `.opencode/project-memory/{project_id}.md`

## Default outputs

- `Sources/Papers/*.md` - one canonical source note per paper
- `Knowledge/*.md` - durable project-facing literature synthesis
- `Writing/*.md` - writing-oriented literature outputs when requested
- `Maps/literature.canvas` - derived literature map when needed

## Safety rules

- Do not dump raw full text into the KB.
- Do not create a duplicate paper note if the canonical note already exists.
- Do not route paper ingestion into top-level `Papers/`; use `Sources/Papers/`.
- Do not treat `Sources/Papers/` notes as the final literature review.
- Do not create extra canvases or `.base` files unless the user asked for them.
- If a relationship is uncertain, keep it in the note body or `Daily/` instead of manufacturing durable structure.
- Do not promote abstract-only or webpage-placeholder notes into `Knowledge`, `Writing`, manuscript, or rebuttal claims.

## References

Load only what is needed:
- `references/WORKFLOW.md`
- `references/PAPER-NOTE-SCHEMA.md`
- `references/COLLECTION-INVENTORY-SCHEMA.md`
- `references/LOCAL-ZOTERO-FALLBACK.md`
- `examples/example-collection-inventory.md`
- `scripts/verify_paper_notes.py`
- `../obsidian-literature-workflow/references/PAPER-NOTE-SCHEMA.md`
- `../obsidian-literature-workflow/references/CANVAS-WORKFLOW.md`
