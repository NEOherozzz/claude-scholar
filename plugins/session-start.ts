/**
 * Session Start Plugin - Display project status on session.created
 * Hook: event (filters for session.created)
 */
import { detectResearchRepoCandidate, getGitInfo, getProjectMemoryBinding, getTodoInfo } from "./lib/common";
import type { Plugin } from "@opencode-ai/plugin";

export const SessionStartPlugin: Plugin = async (ctx) => {
  return {
    async event({ event }) {
      if (event.type !== "session.created") return;
      const cwd = ctx.directory;
      const git = getGitInfo(cwd);
      const todo = getTodoInfo(cwd);
      const binding = getProjectMemoryBinding(cwd);
      const candidate = detectResearchRepoCandidate(cwd);

      let msg = `📂 ${cwd}\n`;
      if (git.is_repo) {
        msg += `Branch: ${git.branch}`;
        msg += git.has_changes ? ` | ${git.changes_count} uncommitted\n` : " | clean\n";
      }
      if (todo.found) {
        msg += `Todos: ${todo.pending} pending / ${todo.done} done\n`;
      }
      if (binding.bound) {
        msg += `🧠 Obsidian project memory: bound (${binding.projectId || "unknown-project"})\n`;
        if (binding.vaultRoot) msg += `  - Vault root: ${binding.vaultRoot}\n`;
        if (binding.memoryPath) msg += `  - Memory: ${binding.memoryPath}\n`;
        msg += "  - Suggested commands: /kb-sync, /kb-status\n";
      } else if (candidate.candidate) {
        msg += "🧠 Obsidian project memory: research repo candidate\n";
        msg += `  - Detected markers: ${candidate.markers.join(", ")}\n`;
        msg += "  - Suggested command: /kb-init\n";
      }
      console.log(msg.trimEnd());
    },
  };
};
