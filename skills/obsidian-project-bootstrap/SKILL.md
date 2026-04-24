---
name: obsidian-project-bootstrap
description: Compatibility shim for project bootstrap. Prefer obsidian-project-kb-core.
---

# Obsidian Project Bootstrap (Compatibility Shim)

Use `obsidian-project-kb-core` for new project bootstrap work.

Preferred helper:

```bash
python3 "${OPENCODE_DIR:-$HOME/.opencode}/skills/obsidian-project-kb-core/scripts/project_kb.py" bootstrap --cwd "$PWD" --vault-path "$OBSIDIAN_VAULT_PATH"
```

This legacy skill name should not recreate the old compact `Papers/`-first layout.
