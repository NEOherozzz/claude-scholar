---
name: obsidian-writeback
description: Compatibility command for deterministic canonical-note writeback into the bound project KB.
args:
  - name: kind
    description: knowledge, paper, experiment, result, report, or writing
    required: true
  - name: query
    description: Semantic query used to resolve the best existing canonical note when no explicit note path is given
    required: false
  - name: note
    description: Explicit project-relative note path to create or update
    required: false
  - name: title
    description: Preferred title when creating a new note
    required: false
tags: [Research, Obsidian, Writeback, Deprecated]
---

# /obsidian-writeback (compatibility)

Use `/kb-*` plus `obsidian-project-kb-core` as the default workflow.

Keep this command only when you need a deterministic compatibility entrypoint that creates or updates exactly one canonical note in the bound KB.

## Default workflow

1. Resolve the bound project KB.
2. Read the minimum context first:
   - `.opencode/project-memory/{project_id}.md`
   - `00-Hub.md`
   - `01-Plan.md`
   - the best matching canonical note, if it already exists
3. Prepare the final markdown content before writing.
4. Save that content to a temporary file.
5. Call the compatibility helper:

```bash
python3 "${OPENCODE_DIR:-$HOME/.opencode}/skills/obsidian-project-memory/scripts/project_kb.py" writeback-note \
  --cwd "$PWD" \
  --kind "$kind" \
  --query "$query" \
  --title "$title" \
  --content-file "$temp_file"
```

If the target path is already known, prefer:

```bash
python3 "${OPENCODE_DIR:-$HOME/.opencode}/skills/obsidian-project-memory/scripts/project_kb.py" writeback-note \
  --cwd "$PWD" \
  --kind "$kind" \
  --note "$note" \
  --title "$title" \
  --content-file "$temp_file"
```

## What the helper updates

- the resolved canonical note,
- normalized frontmatter (`type`, `title`, `project`, `status`, `updated`),
- `_system/registry.md`,
- `02-Index.md`,
- today's `Daily/` note,
- `00-Hub.md` recent changes,
- repo-local `.opencode/project-memory/{project_id}.md`.

## Preferred targets

Use this compatibility path for one-shot deterministic writeback into:
- `Knowledge/*.md`
- `Sources/Papers/*.md`
- `Experiments/*.md`
- `Results/*.md`
- `Results/Reports/*.md`
- `Writing/*.md`

## Final response

Include:
- whether the helper created or updated the note,
- the final canonical note path,
- the related daily/project-memory surfaces,
- the recommended `/kb-*` replacement for future use.
