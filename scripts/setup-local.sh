#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
BASE_SETUP_SCRIPT="$SCRIPT_DIR/setup.sh"

info()  { echo -e "\033[1;34m[INFO]\033[0m $*"; }
warn()  { echo -e "\033[1;33m[WARN]\033[0m $*"; }
error() { echo -e "\033[1;31m[ERROR]\033[0m $*"; exit 1; }

usage() {
  cat <<'EOF'
Usage:
  bash scripts/setup-local.sh [--project-dir <path>]
  bash scripts/setup-local.sh [path]

Description:
  Install Claude Scholar into a project-scoped directory instead of global ~/.claude.
  The target install location is:

    <project-dir>/.claude

Examples:
  bash scripts/setup-local.sh --project-dir /path/to/my-project
  bash scripts/setup-local.sh --project-dir .
  bash scripts/setup-local.sh
  bash scripts/setup-local.sh /path/to/my-project

Notes:
  - This script reuses scripts/setup.sh internally with HOME redirected.
  - No files are written to your real ~/.claude unless --project-dir points there.
  - It also patches project settings.json so hooks and CLAUDE_PLUGIN_ROOT resolve
    to <project-dir>/.claude at runtime.
EOF
}

PROJECT_DIR="$PWD"

while [ "$#" -gt 0 ]; do
  case "$1" in
    --project-dir)
      shift
      [ "$#" -gt 0 ] || error "--project-dir requires a path"
      PROJECT_DIR="$1"
      ;;
    -h|--help)
      usage
      exit 0
      ;;
    *)
      if [ -z "$1" ]; then
        error "Unknown argument: $1"
      fi
      PROJECT_DIR="$1"
      ;;
  esac
  shift
done

[ -f "$BASE_SETUP_SCRIPT" ] || error "Base installer not found: $BASE_SETUP_SCRIPT"

mkdir -p "$PROJECT_DIR"

if ! PROJECT_DIR_ABS="$(cd "$PROJECT_DIR" && pwd)"; then
  error "Cannot resolve project directory: $PROJECT_DIR"
fi

TARGET_CLAUDE_DIR="$PROJECT_DIR_ABS/.claude"
IS_MACOS=0
if [ "$(uname -s)" = "Darwin" ]; then
  IS_MACOS=1
fi

clean_appledouble() {
  local scan_dir="$1"
  [ -d "$scan_dir" ] || return 0

  if command -v dot_clean >/dev/null 2>&1; then
    dot_clean -m "$scan_dir" >/dev/null 2>&1 || true
  fi
  find "$scan_dir" -name '._*' -delete 2>/dev/null || true
}

info "Project directory: $PROJECT_DIR_ABS"
info "Install target: $TARGET_CLAUDE_DIR"
warn "This installation is project-scoped and will not use global ~/.claude."

if [ "$IS_MACOS" -eq 1 ]; then
  info "macOS detected: enabling AppleDouble suppression for local install."
  export COPYFILE_DISABLE=1
  export COPY_EXTENDED_ATTRIBUTES_DISABLE=1
  HOME="$PROJECT_DIR_ABS" bash "$BASE_SETUP_SCRIPT"
else
  HOME="$PROJECT_DIR_ABS" bash "$BASE_SETUP_SCRIPT"
fi

SETTINGS_FILE="$TARGET_CLAUDE_DIR/settings.json"
if [ -f "$SETTINGS_FILE" ]; then
  CLAUDE_LOCAL_SETTINGS="$SETTINGS_FILE" node <<'NODE'
const fs = require('fs');

const settingsPath = process.env.CLAUDE_LOCAL_SETTINGS;
const settings = JSON.parse(fs.readFileSync(settingsPath, 'utf8'));

settings.env = settings.env || {};
settings.env.CLAUDE_PLUGIN_ROOT = '.claude';
delete settings.env.GITHUB_PERSONAL_ACCESS_TOKEN;

for (const matchers of Object.values(settings.hooks || {})) {
  if (!Array.isArray(matchers)) continue;
  for (const matcher of matchers) {
    const hooks = Array.isArray(matcher.hooks) ? matcher.hooks : [];
    for (const hook of hooks) {
      if (typeof hook.command !== 'string') continue;
      const m = hook.command.match(/\.claude\/hooks\/([A-Za-z0-9._-]+\.js)/);
      if (!m) continue;
      const hookFile = m[1];
      hook.command = `node ".claude/hooks/${hookFile}"`;
    }
  }
}

if (settings.mcpServers) {
  delete settings.mcpServers.zotero;
}

fs.writeFileSync(settingsPath, JSON.stringify(settings, null, 2) + '\n');
NODE
  info "Patched project settings.json with relative paths (CLAUDE_PLUGIN_ROOT=.claude)."
else
  warn "No settings.json found at $SETTINGS_FILE; skipped local path patching."
fi

if [ "$IS_MACOS" -eq 1 ]; then
  # Clean both the plugin directory and project root because macOS may create
  # AppleDouble sidecars for directory metadata at parent levels on some volumes.
  clean_appledouble "$TARGET_CLAUDE_DIR"
  clean_appledouble "$PROJECT_DIR_ABS"
  info "macOS cleanup complete: removed existing ._ files under $PROJECT_DIR_ABS"
fi

info "Project-scoped install complete."
