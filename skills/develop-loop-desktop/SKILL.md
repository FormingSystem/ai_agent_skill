---
name: develop-loop-desktop
description: Review, implement, refactor, secure, test, or document the Loop Markdown desktop workstation in F:\git_storage\linux-note\tools\practice_tool. Use when continuing Loop Electron/TypeScript/C++ desktop development, changing its IPC or Native Service, editing the explorer/editor/preview/save architecture, updating implementation status, or retiring the old browser practice prototype.
---

# Develop Loop Desktop

## Ground in the current architecture

1. Read the repository `AGENTS.md`, root `README.md`, and `tools/practice_tool/docs/architecture/implementation_status.md`.
2. Read the authority documents named by the implementation-status item being changed. Treat accepted ADRs and current product/engineering documents as the implementation baseline.
3. Inspect `git status`, the relevant code, tests, dependency manifests, and real call graph before proposing or editing.
4. Treat the root browser `src/`, `banks/`, IndexedDB, and Bash lifecycle as the retiring `0.1.0` prototype. Do not import from it or add compatibility, forwarding, dual writes, or fallback services.

## Resolve design before code

1. Select the next explicit milestone or gate from `implementation_status.md`; do not invent a parallel roadmap.
2. If requirements, ownership, protocol, state transitions, failure behavior, or acceptance criteria are missing or contradictory, update the authoritative design and add or supersede an ADR when the decision is architectural.
3. Review the design for process ownership, capability scope, path and file identity, data ownership, cancellation, stale results, error recovery, resource bounds, cross-platform behavior, and testability.
4. Start implementation only after the design leaves no material decision to the implementer.

## Implement cleanly

- Use the newest target architecture without legacy compatibility unless the developer explicitly requests migration.
- Keep Main responsible for Electron lifecycle and dialogs, Native Service responsible for filesystem capabilities and persistent document services, Renderer responsible for UI and in-memory editor state, and workers/frames responsible for untrusted rendering.
- Keep Renderer sandboxed and path-free. Expose fixed, typed, runtime-validated use-case APIs; reject generic IPC, paths, URLs, commands, and unknown fields.
- Use English `snake_case` for project-owned files, identifiers, object fields, IPC fields, and protocol fields. Preserve framework-required upstream names only where syntax demands them.
- Fail closed on stale capabilities, identity changes, links, boundary escapes, malformed inputs, oversized payloads, and unsupported write semantics.
- Make every state visible and distinct: Dirty is not saved, backed up is not saved, request sent is not success, and stale asynchronous work cannot overwrite current state.
- Avoid tracked build outputs, local state, absolute paths, secrets, and diagnostics containing Markdown bodies.

## Validate and report evidence

1. Add regression tests at the lowest layer that can reproduce each behavior, then add integration or smoke coverage for cross-process flows.
2. Run the desktop TypeScript tests/build, Native CMake build/CTest, relevant smoke/security/audit checks, old-prototype regression checks while it remains, and `git diff --check`.
3. Use only the repository-supported Bash environment for root `format.sh`; record the exact limitation when it is unavailable instead of substituting Git Bash or silently claiming success.
4. Inspect the complete diff for legacy imports, absolute paths, protocol drift, unbounded allocations, missing runtime validation, generated artifacts, and inaccurate documentation.
5. Update `implementation_status.md` only with commands and evidence actually observed. Leave unverified platform or release gates incomplete.
6. Do not stage, commit, push, install system runtimes, delete legacy/user data, or update memories unless the user explicitly requests it.
