---
id: readme.en
title: "AI Agent Skill"
kind: reference
status: maintained
domains:
  - repository
translation_of: readme
---

# Chapter 1\_AI_Agent_Skill

> **Language / 语言** · [← 简体中文](README.md) · **English (current)**

This repository maintains custom Codex skills together with their scripts, references, and agent configuration. Edit the repository source; the installation directory is a runtime copy. Built-in system skills and third-party plugins are outside this repository's scope.

## 1.1\_Getting_started

Install Git and Python 3.12 or later. Clone the repository and enter its root directory:

```bash
git clone git@github.com:FormingSystem/ai_agent_skill.git
cd ai_agent_skill
python -m pip install -r requirements_dev.txt
python scripts/setup_repository.py
python scripts/check_repository.py
python -m unittest discover -s scripts -p 'test_*.py'
```

The setup script configures commit hooks, the commit template, and fast-forward-only pulls for this repository only. The checker validates skill metadata, registry entries, paths, and relative Markdown links and heading anchors. Synchronization tests use temporary directories and do not modify your real installation.

Review installation differences, then synchronize from this repository to `$CODEX_HOME/skills`. When `CODEX_HOME` is unset, the destination is `.codex/skills` under your home directory:

```bash
python scripts/sync_skills.py check
python scripts/sync_skills.py apply
python scripts/sync_skills.py check
```

`check` returns 0 when copies match, 1 when synchronization is needed, and 2 for registry or directory errors. `apply` replaces matching destination files. It rejects symbolic links, junctions, overlapping source and destination directories, and extra destination files. It never copies installation changes back into the repository. Use `--codex-home <directory>` to select a separate installation. After synchronization, check that the skills are available in a new session.

## 1.2\_Skill_catalog

| Skill | Purpose |
| --- | --- |
| [build-linux-note-topic](skills/build-linux-note-topic/SKILL_en.md) | Write, restructure, format, and audit technical books and knowledge topics. |
| [build-technical-ppt](skills/build-technical-ppt/SKILL_en.md) | Create and revise technical tutorial presentations and companion Markdown. |
| [develop-loop-desktop](skills/develop-loop-desktop/SKILL_en.md) | Develop the Loop desktop workstation. |
| [develop-typora-code](skills/develop-typora-code/SKILL_en.md) | Develop the standalone TyporaCode project. |
| [maintain-bilingual-repository](skills/maintain-bilingual-repository/SKILL_en.md) | Maintain complete bilingual content, page switches, and language-local navigation. |

Project-specific skills require their target projects and dependencies. Recheck environment hints against the directory the user has actually selected.

Repository guides, all skill instructions, and all reference documents have Chinese and English bodies, with a language switch on every page. Chinese navigation stays in Chinese and English navigation stays in English. Shared scripts, identifiers, command arguments, original paths, and third-party materials keep their actual names; there is only one runtime implementation. The skill entry routes to instructions in the user's language, and translations are synchronized with the skill.

`scripts/translation_registry.json` records bilingual coverage and content hashes. Repository checks reject missing translations, stale hashes, missing language switches, and incorrect cross-language navigation. After reviewing both versions of a changed page, run `python scripts/update_translation_registry.py --reviewed <Chinese-file-path>` to record the reviewed hashes. This command does not translate text or prove semantic equivalence.

## 1.3\_Maintenance

- [Contributor instructions](agents_en.md)
- [Information architecture and migration provenance](governance/architecture/repository_information_architecture_en.md)
- [Contribution and acceptance workflow](contributing_en.md)
- [Git collaboration and commit rules](governance/conventions/git_guide_en.md)

File management follows linux-note's single-source ownership, responsibility-based directories, relative links, stable metadata, and synchronized references. Skills retain their native format. Commit subjects must still include a Chinese result, followed by bullet-point details; the inherited hook checks the format. The existing remote mainline is `main`.

## 1.4\_License

The [GNU General Public License, version 2](LICENSE), is copied from linux-note. Preserve provenance and existing copyright notices. The GPLv3 license in the remote initialization commit was replaced as requested during migration; that commit remains in history.

---

> **Language / 语言** · [← 简体中文](README.md) · **English (current)**
