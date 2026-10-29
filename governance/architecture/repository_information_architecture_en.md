---
id: governance.architecture.repository_information_architecture.en
title: "Skill repository information architecture"
kind: reference
status: maintained
domains:
  - repository
translation_of: governance.architecture.repository_information_architecture
---

# Chapter 1\_Skill_repository_information_architecture

[简体中文](repository_information_architecture.md) | **English**

## 1.1\_One_source_per_responsibility

Apply linux-note's file-governance principles to the actual responsibilities of this skill repository. Do not reproduce the knowledge repository's directory tree as empty placeholders.

| Location | Responsibility |
| --- | --- |
| `skills/<name>/SKILL.md` | Skill triggers and runtime entry point |
| `skills/<name>/references/` | Rules and reference material loaded as needed |
| `skills/<name>/scripts/` | Executable helpers belonging to a skill |
| `skills/<name>/agents/` | Agent interface configuration |
| `scripts/skill_registry.json` | Installation synchronization registry; register each new skill |
| `scripts/` | Repository checks, installation synchronization, and tests |
| `governance/` | Architecture, contribution rules, and templates |
| `.githooks/`, `.github/workflows/` | Commit validation and CI |

## 1.2\_Source_files_and_installation_copies

Edit the repository → check structure and links → test synchronization → review → commit → synchronize the installation → check consistency. Installation copies never overwrite repository source. During migration, compare both copies and preserve valid content. Extra unregistered destination files block synchronization until their ownership is resolved.

The current user task determines the project a skill operates on. The directory containing the skill is not automatically that project's root. Explicit local paths in imported skills are environment hints, not availability guarantees. Verify them before use and adapt them to the actual machine.

## 1.3\_Migration_provenance

Four custom skills were first imported on 2026-10-29. For `build-linux-note-topic`, the linux-note repository copy was compared with the current installed copy. Additions about locating explanations, path consumers, and rewriting from review feedback were retained. The other skills came from the current custom-skill installation. Runtime caches are excluded.

The synchronization program, tests, commit hook, and template reuse linux-note implementations with paths adjusted for this repository. The license is an exact copy of linux-note's GNU GPL version 2 text. The remote's initial GPLv3 license was replaced as requested; the original commit remains in history.

## 1.4\_Language_views

Chinese repository guides and their `_en.md` English counterparts express the same requirements. Each translation has its own stable ID and a `translation_of` field identifying the original. Both pages link to each other, and changes to instructions and commands update both views. Skill runtime files remain in `skills/` with one registry entry per skill; reading translations do not create additional executable packages. Skill instructions and all references also have paired bodies: `SKILL.md` is the Chinese entry and `SKILL_en.md` is the English reading entry. Shared scripts and agent configuration have one implementation, with bilingual interface descriptions; translations are synchronized with the package. The translation registry records every page pair and its reviewed hashes, covering all repository Markdown and language-local navigation.
