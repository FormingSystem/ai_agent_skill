---
id: agents.en
title: "AI Agent Skill contributor instructions"
kind: reference
status: maintained
domains:
  - repository
translation_of: agents
---

# Chapter 1\_AI_Agent_Skill_contributor_instructions

[简体中文](AGENTS.md) | **English**

Before editing, verify the complete user-selected path and its Git root. Default to the currently open project folder. Explain path conflicts before proceeding, and never continue in an old copy with the same name. Read these instructions, the [README](readme_en.md), [architecture](governance/architecture/repository_information_architecture_en.md), and [Git rules](governance/conventions/git_guide_en.md).

## 1.1\_Responsibilities_and_source_of_truth

This repository maintains custom skills. `skills/` is authoritative; the Codex installation directory is a runtime copy. Edit and validate repository files before explicitly synchronizing them. System skills and third-party plugins remain managed by their installers. Do not commit caches, credentials, logs, or machine runtime configuration.

## 1.2\_File_management

- Follow linux-note's responsibility-based organization, single-source ownership, and relative-link conventions. Do not create directories without actual content.
- Use English `snake_case` for new repository-owned files, directories, and code identifiers. Constants may use `UPPER_SNAKE_CASE`. Preserve existing hyphenated skill package names and their `name` values. Keep contract names such as `SKILL.md`, `README.md`, `AGENTS.md`, `LICENSE`, and framework-mandated methods. Retain imported resource names so their references remain valid.
- Formal governance documents have stable `id`, `title`, `kind`, `status`, and `domains` metadata and numbered headings. Skill Markdown is runtime instruction content: keep its native format rather than applying knowledge-document metadata or chapter numbering.
- Prefer relative links. When moving, renaming, splitting, or deleting files, update skill entry points, registry entries, documentation, and callers; check obsolete paths, missing targets, and duplicate IDs.
- Do not casually delete existing material. Establish callers and impact first. Review extra installation files before removing them; never silently delete them.
- Refactor toward current requirements without forwarding old entry points, maintaining two implementations, or leaving unowned compatibility paths. Confirm ownership, external callers, and platform boundaries before changing them.

## 1.3\_Editing_and_validation

Maintain Chinese and English repository reading guides together. Skill instructions retain their original language and a single authoritative implementation. Code comments remain Chinese by default, and technical teaching targets C/C++ developers. Reusing the existing Python audit and synchronization tools is an engineering requirement, not a change to the teaching-language preference. Read related references before editing a skill. Keep triggers accurate, steps executable, and verification claims honest: automated checks do not establish successful real-task behavior.

Run `python scripts/check_repository.py`, `python -m unittest discover -s scripts -p 'test_*.py'`, and `git diff --check`. Run relevant skill scripts for the change. After installation, run `python scripts/sync_skills.py check`. Explain any checks that could not run.

## 1.4\_Git_collaboration

Keep the existing `main` mainline and integrate only validated fast-forward changes. Use `codex/` for task branches by default. Inherit linux-note's Chinese commit-result and bullet-detail format, `.githooks/commit-msg`, and commit template. Fetch before pushing; inspect divergence and resolve conflicts. Never force-push delivered history; use revert. Keep other tasks' uncommitted changes out of the commit.

## 1.5\_Bilingual_reading

The README, contribution guide, contributor instructions, architecture, and Git guide have Chinese and English versions linked in both directions. Update corresponding versions together when requirements, commands, or directory boundaries change. English headings use `Chapter N` and the same numeric hierarchy; retain escaped underscores. English translation filenames use `_en.md`, with unique IDs and `translation_of` pointing to the original ID. Translations express the same policy and are not separate runtime skill registrations. Mark untranslated skill instructions and detailed references accurately; English navigation alone does not make their bodies bilingual.
