---
id: contributing.en
title: "Contribution and acceptance workflow"
kind: reference
status: maintained
domains:
  - repository
translation_of: contributing
---

# Chapter 1\_Contribution_and_acceptance_workflow

[简体中文](CONTRIBUTING.md) | **English**

Read the [repository instructions](agents_en.md) and [Git rules](governance/conventions/git_guide_en.md). After cloning, run `python scripts/setup_repository.py` from the repository root. It configures only this repository's hooks, commit template, and fast-forward pull policy.

To add a skill, create one package under `skills/`, provide `name` and `description` in `SKILL.md`, and add references and scripts only when needed. Register the package in `scripts/skill_registry.json` and update the skill catalogs in [Chinese](README.md#12_技能目录) and [English](readme_en.md#12_skill_catalog). Do not create empty template directories.

Before committing, run the checks in the README and inspect the staged diff. Changes to skill behavior also need validation in an appropriate real task; structural checks cannot establish that the skill works well in practice. Preview installation differences with `python scripts/sync_skills.py check`. Once the repository content is ready, run `apply`, then `check`. Applying changes overwrites local edits to matching destination files. Extra destination files block the whole batch; review their provenance first.

When moving or deleting files, update all references and registry entries. Revert published commits instead of rewriting history. Write accurate Chinese commit results and meaningful bullet details. Do not commit credentials or generated caches.

Update paired Chinese and English repository guides in the same change, including commands, behavior boundaries, and navigation. Give translations a unique document ID and a `translation_of` field pointing to the source document's ID. Translations are reading views of the same policy; they must not introduce independent rules or register duplicate skills. Do not describe untranslated skill references as available in English.
