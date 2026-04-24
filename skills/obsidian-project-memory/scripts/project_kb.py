#!/usr/bin/env python3
from __future__ import annotations

import argparse
import importlib.util
import json
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


kb_common = _load_module(KB_COMMON_PATH, 'opencode_obsidian_kb_common')
core_project_kb = _load_module(PROJECT_KB_PATH, 'opencode_obsidian_project_kb')

# Re-export commonly imported helpers for legacy modules.
find_repo_root = kb_common.find_repo_root
resolve_binding = kb_common.resolve_binding
now_iso = kb_common.now_iso
titleize_slug = kb_common.titleize_slug


DEFAULT_KIND_STATUS = {
    'knowledge': 'active',
    'paper': 'active',
    'experiment': 'active',
    'result': 'active',
    'report': 'active',
    'writing': 'draft',
}


def _normalize_note_rel(note: str) -> str:
    note = note.strip().replace('\\', '/')
    if not note.endswith('.md') and not note.endswith('.canvas'):
        note += '.md'
    return note


def _default_note_rel(kind: str, title: str) -> str:
    folder = kb_common.NOTE_KIND_TO_FOLDER.get(kind)
    if not folder:
        raise SystemExit(f'Unsupported note kind: {kind}')
    slug = kb_common.slugify(title) or 'untitled-note'
    suffix = '.canvas' if kind == 'map' else '.md'
    return f'{folder}/{slug}{suffix}'


def _prepare_content(content: str, *, kind: str, title: str, project_slug: str) -> str:
    text = content if content.endswith('\n') else content + '\n'
    text = kb_common.set_frontmatter_value(text, 'type', kind)
    text = kb_common.set_frontmatter_value(text, 'title', title)
    text = kb_common.set_frontmatter_value(text, 'project', project_slug)
    text = kb_common.set_frontmatter_value(text, 'status', DEFAULT_KIND_STATUS.get(kind, 'active'))
    text = kb_common.set_frontmatter_value(text, 'updated', kb_common.now_iso())
    return text


def writeback_note(argv: list[str]) -> int:
    parser = argparse.ArgumentParser(description='Compatibility writeback helper for OpenCode Scholar.')
    parser.add_argument('--cwd', default='.')
    parser.add_argument('--project-id', default='')
    parser.add_argument('--kind', required=True)
    parser.add_argument('--query', default='')
    parser.add_argument('--note', default='')
    parser.add_argument('--title', default='')
    parser.add_argument('--content-file', required=True)
    args = parser.parse_args(argv)

    repo_root = kb_common.find_repo_root(Path(args.cwd).resolve())
    binding = kb_common.resolve_binding(repo_root, args.project_id or None)
    project_root = binding.project_root

    if args.note:
        rel_path = _normalize_note_rel(args.note)
        target_path = project_root / rel_path
    else:
        query = (args.query or args.title).strip()
        candidates = kb_common.search_note_candidates(project_root, args.kind, query, limit=1) if query else []
        if candidates:
            target_path = candidates[0]
            rel_path = target_path.relative_to(project_root).as_posix()
        else:
            title_seed = (args.title or args.query or 'Untitled Note').strip()
            rel_path = _default_note_rel(args.kind, title_seed)
            target_path = project_root / rel_path

    raw_content = Path(args.content_file).read_text(encoding='utf-8')
    title = (args.title or target_path.stem.replace('-', ' ').title()).strip()
    final_content = _prepare_content(raw_content, kind=args.kind, title=title, project_slug=binding.project_slug)
    existed = target_path.exists()
    kb_common.write_text(target_path, final_content)
    kb_common.registry_add_or_update(project_root, rel_path)
    kb_common.update_index(project_root)
    daily = kb_common.ensure_today_daily(project_root, binding.project_slug)
    daily_ref = kb_common.relative_note_path(daily, binding.vault_path)
    kb_common.prepend_recent_change(project_root, f'Writeback {"updated" if existed else "created"} [[{rel_path[:-3]}]] via compatibility helper.')
    kb_common.update_project_memory(
        repo_root,
        binding.project_id,
        project_root,
        binding.hub_note,
        binding.note_language,
        summary=f'Compatibility writeback {"updated" if existed else "created"} [[{rel_path[:-3]}]]; see [[{daily_ref[:-3]}]].',
    )
    print(json.dumps({
        'project_id': binding.project_id,
        'created': not existed,
        'updated': existed,
        'note': rel_path,
        'daily_note': daily_ref,
    }, ensure_ascii=False, indent=2))
    return 0


def main() -> int:
    if len(sys.argv) > 1 and sys.argv[1] == 'writeback-note':
        return writeback_note(sys.argv[2:])
    return core_project_kb.main()


if __name__ == '__main__':
    raise SystemExit(main())
