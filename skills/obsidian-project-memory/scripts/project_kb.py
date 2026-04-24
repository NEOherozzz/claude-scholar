#!/usr/bin/env python3
from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

CORE_DIR = Path(__file__).resolve().parents[2] / 'obsidian-project-kb-core' / 'scripts'
KB_COMMON_PATH = CORE_DIR / 'kb_common.py'
PROJECT_KB_PATH = CORE_DIR / 'project_kb.py'
if str(CORE_DIR) not in sys.path:
    sys.path.insert(0, str(CORE_DIR))


def _load_module(path: Path, name: str):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f'Unable to load module from {path}')
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


kb_common = _load_module(KB_COMMON_PATH, 'codex_obsidian_kb_common')
core_project_kb = _load_module(PROJECT_KB_PATH, 'codex_obsidian_project_kb')

# Re-export commonly imported helpers for legacy modules.
find_repo_root = kb_common.find_repo_root
resolve_binding = kb_common.resolve_binding
now_iso = kb_common.now_iso
titleize_slug = kb_common.titleize_slug


def main() -> int:
    return core_project_kb.main()


if __name__ == '__main__':
    raise SystemExit(main())
