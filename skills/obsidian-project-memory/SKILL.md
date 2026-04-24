---
name: obsidian-project-memory
description: Compatibility shim for the new project-scoped KB workflow. Prefer obsidian-project-kb-core for new work.
---

# Obsidian Project Memory (Compatibility Shim)

This legacy skill name is kept for one transition window in OpenCode.

Use `obsidian-project-kb-core` as the default authority for:
- project bootstrap
- note routing
- registry and index updates
- daily maintenance
- lifecycle actions
- lint and link-repair orchestration

Compatibility helper path:

```bash
python3 "${OPENCODE_DIR:-$HOME/.opencode}/skills/obsidian-project-memory/scripts/project_kb.py" detect --cwd "$PWD"
python3 "${OPENCODE_DIR:-$HOME/.opencode}/skills/obsidian-project-memory/scripts/project_kb.py" sync --cwd "$PWD"
python3 "${OPENCODE_DIR:-$HOME/.opencode}/skills/obsidian-project-memory/scripts/project_kb.py" writeback-note --cwd "$PWD" --kind knowledge --query "overview" --title "Project Overview" --content-file "$temp_file"
```

The compatibility script delegates to the new KB core implementation and follows the new vault-first layout rooted at `Research/{project-slug}/`.
