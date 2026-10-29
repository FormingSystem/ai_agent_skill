---
id: governance.conventions.git_guide.en
title: "Git collaboration, commits, and releases"
kind: reference
status: maintained
domains:
  - governance
translation_of: governance.conventions.git_guide
---

# Chapter 1\_Git_collaboration_commits_and_releases

[简体中文](git_guide.md) | **English**

## 1.1\_Purpose

Git history must identify the project or module and its verifiable result. Skill instructions and repository tooling use the same commit syntax. Do not use obsolete types such as `add`, `update`, `rewrite`, `structure`, or `meta`.

Each commit should be independently reviewable and reversible. Include required tests, schemas, help, and documentation with the implementation. Separate independent governance changes, content rewrites, and releases.

## 1.2\_Branches_and_workspaces

`main` is the releasable mainline and accepts validated fast-forward changes only. Confirm the repository and inspect existing work before editing; never operate in an old same-named copy or stage another task's changes.

```bash
git rev-parse --show-toplevel
git status --short --branch
```

These commands identify the repository root, branch, and pending changes. Resolve path mismatches and establish ownership of existing changes first. The examples below assume that `origin` has been verified, the remote mainline is `main`, and the example branch and adjacent directory do not already exist.

Use meaningful short-lived branches, with the `codex/` prefix for Codex-created branches. Branch names are independent of commit types. If parallel work requires separate indexes and files, fetch in the repository root and create an isolated worktree:

```bash
git fetch origin
git worktree add ../work-repository-validation \
  -b codex/repository-validation origin/main
```

Fetch updates remote-tracking refs without checking them out. The new worktree starts explicitly at `origin/main`; it does not copy uncommitted changes. Choose a different starting point explicitly when earlier commits are needed.

Before integration, fetch in the task worktree. Only rewrite commits that are private, unpushed, and undelivered:

```bash
git fetch origin
git rebase origin/main
```

If conflicts cannot be resolved reliably, retain diagnostics and use `git rebase --abort`. Do not apply this history-rewriting workflow to delivered branches; preserve shared commits and merge the mainline into the task branch as appropriate, then validate again, or follow an explicitly authorized migration plan.

After applicable checks pass, use the clean mainline worktree to integrate:

```bash
git switch main
git merge --ff-only codex/repository-validation
```

If fast-forward integration fails, inspect the branch relationship instead of forcing a branch move. This updates local history only. Push or release according to the user's authorization.

## 1.3\_Commit_subjects

The inherited format remains the same for English-speaking contributors:

```text
<type>[(<project>/<module>)]!?: <result containing Chinese>

- Meaningful detail
- Another detail when needed
```

The entire scope is optional. It may contain one project or two project/module components; there is no project, module, or language allowlist. Chinese and English scopes are allowed. Whitespace, parentheses, colons, and extra slashes are forbidden because they break the syntax. English scopes matching directory names are a maintainer preference, not a language restriction in the hook. `!` marks a breaking change.

| Type | Purpose |
| --- | --- |
| `feat` | Add observable user or developer capability |
| `fix` | Correct behavior |
| `refactor` | Change implementation or architecture without primarily adding features |
| `perf` | Improve performance or resource use |
| `security` | Change permissions, validation, supply chains, or security boundaries |
| `content` | Add or rewrite knowledge and research content |
| `docs` | Change usage, design, or governance documentation |
| `test` | Add or adjust tests and verification tools |
| `build` | Change dependencies, builds, installation, or packaging |
| `ci` | Change automated checks or release pipelines |
| `release` | Publish versions or synchronize release manifests |
| `revert` | Reverse an established historical change |
| `chore` | Maintenance without changing product, knowledge, or build semantics |

Scopes such as `knowledge/rcu`, `repository/git`, `repository/format`, `repository/obsidian`, and `publication` are examples, not a fixed list. A valid subject might be `docs(repository/git): 更新分支与提交规范`. Avoid vague results such as “update information” or “fix some issues.”

## 1.4\_Commit_bodies

Every commit needs a blank line after the subject and at least one nonempty detail beginning with `- `. Put each detail on its own line, without additional section headings or prose blocks. Explain the problem, substantive change, resulting behavior, or actual verification. Do not merely repeat the title, leave placeholders, or claim tests that were not run.

```text
refactor(repository/format): 统一文档检查入口

- 集中标题、元数据与链接检查
- 保持检查模式只读
- 验证中文路径与标题锚点
```

Write a summary for reviewers rather than a list of files, file counts, or line counts. Include a path only when it helps locate an important implementation. Describe a reference-counting fix by its ownership guarantees, for example, rather than by how many chapters changed.

The hook only uses a non-ASCII test as a rough filter for Chinese results. It cannot identify the language or verify the claim. Review the actual Chinese wording and diff even when syntax validation passes.

## 1.5\_Commit_scope

A commit should produce one coherent result: a feature with its necessary schema, tests, and help; one content module; a verifiable architectural refactor; one security-boundary change; or a release. Do not mechanically split by file type or combine unrelated modules under a vague result.

Corrections during long tasks still use this format. The hook rejects automatically generated `fixup!` subjects, so `git commit --fixup` is not a supported default. If all affected commits remain private, unpushed, and undelivered, interactive rebase may squash or fix up them with a compliant final message. Do not disable hooks or rewrite delivered history for convenience.

## 1.6\_Precommit_checks

Enable versioned rules from the repository root using local configuration, never `--global`:

```bash
git config core.hooksPath .githooks
git config commit.template governance/templates/git_commit_message.txt
```

The existing audit and synchronization tools require Python 3.12 or later. Install dependencies and run:

```bash
python -m pip install -r requirements_dev.txt
python scripts/check_repository.py
python -m unittest discover -s scripts -p 'test_*.py'
git diff --check
```

These checks cover structure, metadata, links, and synchronization boundaries. They do not replace real-task skill acceptance. Check installation consistency separately with `python scripts/sync_skills.py check`.

Inspect the index as well as the working tree. Replace the example path below with the file actually changed:

```bash
git add -- path/to/changed_file.md
git diff --cached --check
git diff --cached
```

Shell scripts with a shebang intended for direct execution must use Git mode `100755`; source-only libraries use `100644`.

## 1.7\_Undoing_changes_and_editing_history

- Correct working-tree mistakes by editing them.
- The last private, unpushed, undelivered commit may be amended; validate the final diff again.
- Organize temporary private commits with interactive rebase under the preceding constraints, without creating hook-rejected temporary subjects.
- For pushed or delivered commits, preserve history. Prepare the reverse change with `git revert --no-commit <commit>`, review it, then commit a compliant Chinese `revert` result and bullet details. Git's generated English revert subject is not compliant. Confirm the correct mainline parent before reverting a merge.
- Do not reset, forcibly move, or force-push the mainline.
- Only an explicitly authorized repository-wide history migration may use `--force-with-lease`, after creating and verifying a complete bundle backup.

## 1.8\_Repository_versions

Use date-based release tags such as `ai_agent_skill-v2026.10`. Complete content, assembled-output, and link verification before release.

## 1.9\_Excluded_content

Do not commit temporary test outputs, editor caches, build artifacts, `.local`, `node_modules`, `dist`, logs, credentials, access tokens, or regenerable intermediate files. Avoid machine-specific absolute paths in long-lived technical evidence. An explicitly agreed discovery path in `AGENTS.md` is an environment hint, not source identity, and does not justify embedding local paths in evidence.

Do not import large materials with unverified provenance or authorization, or isolated experiments without an entry guide, environment description, and verification conclusions.
