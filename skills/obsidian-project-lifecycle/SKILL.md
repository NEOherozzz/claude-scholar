---
name: obsidian-project-lifecycle
description: Compatibility shim for KB lifecycle actions. Prefer obsidian-project-kb-core.
---

# Obsidian Project Lifecycle (Compatibility Shim)

Use `obsidian-project-kb-core` for archive, purge, rename, detach, and rebuild actions.

Compatibility helper:

```bash
python3 "${CODEX_HOME:-$HOME/.codex}/skills/obsidian-project-kb-core/scripts/project_kb.py" lifecycle --cwd "$PWD" --mode archive
python3 "${CODEX_HOME:-$HOME/.codex}/skills/obsidian-project-kb-core/scripts/project_kb.py" note-lifecycle --cwd "$PWD" --mode rename --note "Experiments/old.md" --dest "Experiments/new.md"
```
