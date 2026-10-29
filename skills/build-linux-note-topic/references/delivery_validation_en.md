# Refactor, verify and deliver

[简体中文](delivery_validation.md) | **English**

This document must be read and executed in its entirety before each assignment in this skill is delivered. Path adjustment, content preservation in layout-only edits only, source code hashing, construction and experimentation are still performed according to each clear applicable condition; no additional tasks will be expanded for conditions that are not triggered.

## clean refactoring

When the chapter order or path changes:

1. First record the selected editing mode and content baseline;
2. Inventory every H2/H3 chapter, code block, diagram, table, lab, checklist, and link before moving;
3. Map each retained content unit to a destination and do not delete another piece of content just because it looks similar;
4. Layout-only mode preserves document identity, technical semantics, and all information units; allows documented mechanical typesetting changes and does not require byte-for-byte or line-for-line identity;
5. Structural adjustment patterns that retain content move units intact, retaining original wording unless bridging content must change;
6. Content modification or rewrite mode only modifies explicitly authorized content;
7. Update the topic outline and previous/next article navigation links;
8. Update Markdown, Obsidian, Atlas, publication list, source-code mapping and other real callers; use [Layered Audit Requirements for Source Code and Text Entries](source_documentation_workflow_en.md#use-module-concept-introduction-and-unique-implementation-to-explain-related-text) when synchronizing all information, and record non-existent callers as requiring no modification;
9. Search old file names and IDs across the repository;
10. Make sure that no irrelevant dirty files or reviewed content are overwritten.

Edit with `apply_patch`. Do not stage or commit changes, or modify external source trees, unless the user explicitly requests those actions.

## Verification before delivery

First, count the length of Markdown documents in this round, and review them one by one if they exceed the threshold; according to the [length rules of the main entrance](../SKILL_en.md#make-it-clear-as-a-condition-for-completion), decide whether to retain or split based on actual conditions such as complete experiments, necessary code, continuous derivation, or slight excess, and record the reasons. The OVER in the script means that it needs to be judged, and does not automatically mean that delivery has failed:

```text
python <skill-dir>/scripts/audit_document_length.py <file-or-directory> ...
```

First run the built-in structural audit:

```text
python <skill-dir>/scripts/audit_topic.py <topic-directory> --repo-root <repository-root>
```

Run a continuous reading risk audit for each chapter created, expanded, or rewritten this time:

```text
python <skill-dir>/scripts/audit_reader_continuity.py <chapter.md> --strict
```

This script can only detect mechanically observable risks such as link dominance, title echo, empty sections, unfulfilled source-explanation headings, and overlong modules. **Script passing cannot replace [text independent reading review mandatory acceptance gate](reader_first_writing_en.md#performing-anti-formalism-and-hard-gated-continuous-reading)**. Issues reported in strict mode must be revised, or a specific reason for retention directly related to the reader's task given in the delivery notes; "the rules require linking to be complete" cannot be used as a reason.

Then run the term first occurrence audit to obtain the candidate ledger of abbreviation, configuration name and backtick source code identifier:

```text
python <skill-dir>/scripts/audit_terminology_onboarding.py <chapter.md> --strict
```

The script only checks for machine-recognizable candidate words, the first occurrence position, and whether there are Chinese and English expansions or name type signals nearby; it cannot understand whether the terms are interpreted correctly, nor can it discover all topic project-specific shorthand. Questions reported in strict mode must be completed, or specific reasons should be given one by one for "why it is not a term, why the current window has been explained, and why it belongs to prerequisite knowledge that has been clearly established and reviewed". Do not spoil reading by reinserting full names and definitions in each chapter to eliminate window warnings. After the script is passed, it still needs to be manually checked whether the new concepts rely on unexplained words and whether the reader has obtained the understanding required for the current reasoning.

Also run the built-in content conservation audit for layout-only tasks with a clean Git baseline:

```text
python <skill-dir>/scripts/audit_content_conservation.py <topic-directory> --repo-root <repository-root> --baseline <baseline-ref>
```

If there are uncommitted reviewed material when the task begins, a separate pre-modification snapshot or content ledger should be saved, as `HEAD` alone cannot represent the baseline. Record the number of rows, headings, code fences, tables, and Mermaid figures before and after modifications, and prove that each content unit within the preservation scope has a destination. The content conservation script performs a strict line-level comparison: failure indicates a discrepancy that requires manual reconciliation, and does not automatically equate to loss of technical content. Mechanical changes necessary for typesetting can be stated item by item and accepted; semantic changes beyond authorization, unexplained reduction or omission of information are considered errors. Then when the runtime environment is available, perform formatting of the repository itself, metadata/link checks, targeted builds or experimental compilations, and `git diff --check`. Use the repository renderer to parse Mermaid when possible. The source code copy hash is checked only if the source code evidence falls within this scope.

When the required environment is unavailable, complete all safe static checks and accurately report that validation was not performed and why. Uncompiled experiments or unrendered graphs must not be described as having been performed.

## Deliver by results

Report:

- new paths to causal reading;
- Reader starting from scratch entry, term dependency order, and project-specific naming that still requires manual confirmation;
- Selected editing mode and content conservation count;
- The actual scenarios, state machines, source code and experimental changes that occurred within this scope;
- When external charts are involved in this round, the charts cover ledgers, text placement points, and uncovered items;
- The moved or renamed authoritative location and updated caller;
- Passed verification;
- Verifications not performed and their reasons;
- Whether staged or committed.

The final response should be shorter than the topic itself. Link to an outline and a few representative files, rather than listing every modified file.
