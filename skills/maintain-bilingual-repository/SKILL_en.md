---
name: maintain-bilingual-repository
description: Establish, complete, and maintain Chinese and English reading paths in code or documentation repositories, including skill instructions and references, per-page language switching, language-local links and anchors, translation coverage checks, and synchronized delivery. Use for repository-wide bilingual support, broken switches or links, and translation drift; not for isolated sentence translation or language questions without a repository task.
---

# Maintain a Chinese and English repository

> **Language / 语言** · [← 简体中文](SKILL.md) · **English (current)**

Provide two complete reading paths from the homepage through instructions and references and back. An English catalog does not replace English body text, and having two files does not make a language switch discoverable. Use these instructions for English-language tasks.

## Establish scope and existing conventions

- Verify the user-selected directory, Git root, contributor rules, branch, and uncommitted work. Edit within the authorized scope and keep other tasks' changes separate.
- Inventory the README, contribution and governance documents, skill instructions, every referenced document, and actual reading entry points. Do not reduce repository-wide bilingual support to homepage translation.
- Inspect existing language directories, filename suffixes, document IDs, generators, and readers. Reuse a maintainable existing approach. Without an established convention, pair the original with a sibling `_en.md` file and use relative links.
- Distinguish translatable project-owned prose from shared code and configuration, original evidence, and third-party material. Preserve real paths, API names, and command arguments; do not invent English pages for external sources. Keep original licenses and version evidence according to their provenance.

## Translate complete content while preserving contracts

Process all in-scope paragraphs, lists, tables, legends, and non-executable explanatory diagrams. Preserve prerequisites, exceptions, normal and failure paths, operational boundaries, and evidence levels. Long documents may be handled in batches, but maintain the full inventory and finish every batch.

- Preserve code identifiers, executable commands, paths, configuration keys, numbers, and units. Handle translatable comments or diagram labels separately from executable syntax. Bilingual reading does not require two runtime implementations.
- Keep one runtime registration per skill. Explain language selection at the entry point and distribute both language bodies and their references together. Do not invent runtime locale fields; use only verified interface configuration fields.
- Use translation services only for material permitted to be sent to that service; do not send unapproved private content. Review machine drafts for meaning, especially prohibitions, exceptions, cancellation, rollback, and temporal ordering. Terms such as `stage`, `commit`, `capability`, `fail closed`, publication/release, and safety/liveness need their engineering meanings.
- Compare paragraphs, headings, lists, tables, fences, and literal code, then review differences individually. Matching structure, hashes, and valid links do not establish semantic equivalence; do not claim a full manual paragraph review merely because checks pass.

## Make language switches visibly usable

Place a prominent language navigation block beneath the title and at the end of every paired document. Identify the current language and link the other language directly to the corresponding version of that same page. A prose mention, hidden comment, or homepage-only link does not provide per-page switching.

Use ordinary Markdown navigation supported by the reader. Markdown files switch pages through links; do not claim to have installed a global GitHub language control or remembered client preference. If the project already has a website language router, integrate with its actual capabilities.

Verify the trip from the current document to its translation and back. It must not return to the homepage, another same-language copy, or a different topic. Check the footer switch on long pages as well. When the user cannot find a switch, inspect the actual file, revision, rendered view, and position instead of repeatedly asserting that it exists.

## Keep navigation within the selected language

- Chinese pages normally open Chinese content and English pages open English content. Explicit language switches are the cross-language exception. Identify the actual language of shared resources and external material without translations.
- Parse relative paths and fragments before rewriting links. Avoid broad replacements that damage code, URLs, quoted examples, or file identities.
- Map translated heading anchors using the actual renderer's rules, including numbering, punctuation, duplicate headings, and explicit anchors. Cover contents lists, self-links, cross-document deep links, and return paths.
- Watch for translation-inserted spaces between a Markdown link's closing bracket and opening parenthesis: they can break the link while escaping a naïve checker. Also inspect emphasis, table columns, and fences.

## Track coverage and prevent drift

Maintain one registry of source pages, translations, and maintenance status. Additions, deletions, and renames must update the pairs. If the project uses content hashes, update them only after reviewing both versions; automatically refreshing hashes does not establish translation consistency.

Reuse or extend repository checks to detect unpaired in-scope files, missing targets, duplicate registrations, stale translation versions, missing header or footer switches, incorrect switch destinations, cross-language navigation, and broken heading anchors. Add meaningful regression cases for demonstrated failures; matching generated wording alone is not behavioral verification.

## Validate and deliver

1. Inspect an ordinary reference page, a long skill page, and a governance page with metadata in a real Markdown rendering. Check header and footer controls and both directions of navigation; report which pages were actually previewed.
2. Run structure, link, language-coverage, relevant test, and staged-diff checks. A successful network request does not establish that the linked page and body language are correct.
3. When distributing skills, use existing repository tooling to preview, apply, and recheck changes. Do not overwrite unreviewed installation-only files or promote an installed copy into the source of truth.
4. Complete commits or pushes already authorized by the user and verify local and remote commit identity. Preserve other uncommitted work. Report the complete scope, actual verification, and remaining limitations; never use “bilingual support” to conceal untranslated body text.

---

> **Language / 语言** · [← 简体中文](SKILL.md) · **English (current)**
