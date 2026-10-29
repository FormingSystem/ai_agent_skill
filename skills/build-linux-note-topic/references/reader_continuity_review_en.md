# Continuous Reading and Anti-Formalist Acceptance

> **Language / 语言** · [← 简体中文](reader_continuity_review.md) · **English (current)**

The thematic design must pass both **content correctness** and**continuous reading** two types of acceptance. Table of contents, links, tables, diagrams, source code symbols and version information are only means of expression or evidence and cannot replace readers' modeling along the text. When any of the following situations occurs, even if all structural audits pass, the chapter will still be judged to be unqualified:

- The title promises to explain the concept, mechanism or source code implementation, but the main text mainly introduces the data location, file diversion and external entrance;
- After the link target is deleted or clicks are disabled, key concepts, problems, solutions or state transitions cannot be derived from the current text;
- The reader must first understand test orchestration, configuring exceptions, or subsequent chapters to know what this chapter is addressing;
- Titles, tables, figures, codes or configurations use the topic's private name first, followed by explanations in the text, or the definition itself continues to rely on unexplained terms;
- The same process is transcribed repeatedly in multiple tables, diagrams and lists, but no new judgment ability is produced;
- H2 simply restates H1, or goes directly to the next heading without any explanation below it;
- Concepts, actors, status addresses, process stages, configuration variants, optimization and diagnostic facilities are juxtaposed on the same layer;
- The chapter has fully announced in advance the model increments that should be derived through counterexamples in the next chapter;
- The review can only confirm that "all the elements are there", but cannot restate a main line from the problem to the conclusion in a short language.

## title deed

Before writing the text, translate the title into a reader task:

| Title promise | The current chapter must be fulfilled locally | What cannot substitute for it |
| --- | --- | --- |
| Basic concept or principle | Definition, boundary, difference from adjacent concepts, minimal dynamic process | Terminology link or noun list |
| Problems and proof models | Old model value, specific contradictions, minimum modifications and proof boundaries | Directly announce mature solutions |
| Status and communication mechanism | Participants, status locations, write-read relationships and complete cycles | Field list or general diagram |
| Source code implementation, source code explanation or source code mechanism | Module responsibilities, input and output, key status, real call chain and local source code evidence | Source code index, jump table or "see other documents for details" |
| Experiment and verification | Environment, steps, expected results, failure phenomena and proof boundaries | Command name or unexecuted example |
| Navigation or Index | Diversion Conditions, Reading Order and Entry Responsibilities | Second Mechanism Tutorial |

If the knowledge text only explains the implementation model that is stable across versions, accurate expressions such as "implementation model, status and communication" should be used in the title, and the precise function body should be linked to the research layer. If the title clearly promises function-by-function source code implementation, the text responsibilities and storage location must comply with the source code reading specifications, and the navigation file cannot be disguised as the implementation text.

**The rewritten title review is also a delivery gate.**Re-execute the following checks after content expansion, reorganization or error correction. Just because the title originally exists does not mean it is still suitable by default:

1. **Check the current contract:** In one sentence, summarize the problem that the revised text actually solves, and then compare it with the title promise. If the text has been expanded from the interface position to design motivation, status responsibilities, or cross-component processes, the title should also reflect the current main issue; you cannot just correct the text and leave a title that is too narrow in scope or outdated in focus.
2. **Check parent-child scope and sibling advancement:** The parent title must cover the questions that the child sections jointly answer, and the subtitles each bear an identifiable increment; the sibling title should be able to see how the question continues to advance, rather than a string of unrelated module names. When a child section extends beyond the parent scope, adjust the parent title or organizational relationship within the authorization scope, and do not use a generalized parent title to cover up the separation.
3. **Prioritize writing objects and problems:** The title of the textbook mechanism should try to point out the current specific object, as well as the design issue being explained, cause and effect or role relationship; only write general terms such as "function, parameter, mapping", etc., which will easily obscure why it is mentioned at this time. Such names are only used when this section actually undertakes the corresponding query, directory or positioning tasks. Do not rename the mechanism explanation to parameter description just because a parameter table appears.
4. **Read only the title, then go back to the main text for acceptance:** For the time being, only read the current title, parent title, and adjacent sibling titles. Readers should be able to identify the mechanism advancement and the position of this section; then check whether the main text fulfills the promise. The title does not assume the abstract of the full text, nor does it require a long word count or many terms to be complete, nor does it force all titles to be changed into questions or use the same template.
5. **Synchronized title dependencies:** After renaming, retrieve the old title and its complete fragment after rendering, update the Typora complete title anchor, Markdown and Obsidian actual link, as well as the topic outline, front and back navigation and other real call entries; synchronize document title metadata when H1 is involved. Then check that the new anchor point actually exists, that there are no unprocessed references to the old fragment, and that you cannot just change the visible link text.

## Broken link reading test

Before delivery, treat all hyperlinks as non-clickable, retain only the visible text of the current file, and check whether readers can answer:

1. What is the core concept that appears for the first time in this chapter, and which similar types differ from it;
2. What issues were raised at which specific site;
3. What roles, states, communications or constraints have been added to the current module;
4. How a normal process goes from input to output;
5. Which source code, experiment or specification only proves the conclusion that has been stated;
6. What this chapter can prove now, what the next chapter still needs to solve.

Any question that can only be answered by clicking on a link means that the link assumes the responsibility of the text. The fix is ​​to write the minimum explanation required for the current scene back locally, and then retain the precise link for in-depth tracking; it is not to copy the complete external tutorial.

## Module local closed loop

When a chapter contains multiple implementation modules, they will be closed one by one according to the problem dependencies, without giving the full component directory first. Each module forms at least the following reading actions:

```text
Basic concepts and type positioning
→ Specific problems faced by the current module
→ Solution and status/communication changes
→ Let readers predict an intermediate state, counterexample, or failure consequence
→ Verify with implementation, source code, experiments or logs
→ Hand the new conclusion to the next module
```

"Guiding readers to think" cannot degenerate into questions without answers. The question must be placed before the answer, allowing readers to use the established model to make predictions; subsequent source code or experiments will confirm, correct or break down this prediction.

## Main line, branch and presentation budget

Start by freezing a default configuration, a normal path, and a set of through objects. Optimization, diagnostics, version differences, special configurations and the next execution model are processed in partitions after the mainline is closed. Each time a new representation is added, the question it answers alone is recorded:

- Role diagrams are used to locate status or ownership;
- Sequence diagrams are used to expose execution order and asynchronous windows;
- The state table is used to compare readers and writers before and after conversion;
- Source code excerpts are used to verify specific implementation points;
- The dense evidence index is used for review or in-depth reading and does not occupy the main narrative; precise official comparisons next to key concepts remain in the main text.

If two representations answer the same question and do not add new judgment ability, keep the clearer one. The evidence ledger, batch link list, and full field coverage table should remain at the reference, research, or review level; this does not exempt the nearest citation required by [Official Source Tracing](official_source_reading_en.md#independent-explanation-and-official-information-traceability), and the reading guide cannot be removed altogether.

## Cold reading and retelling access control

The final review is based on the declared reader base and independent reading review of previous chapters, without checking the author's blueprint or relying on temporary jumps to fill holes. Check whether the key concepts can be used to explain phenomena and predict results, and then retell why this chapter continues the previous chapter, what problems it solves, how to draw conclusions, and what is left to continue learning. Also check why adjacent paragraphs appear in sequence, whether there are questions worth predicting before the experiment, and whether the answers have derivation rather than just the results. If the retelling is only the file name and field name, or a large number of unknown premises must be filled in before continuing to rewrite. Self-independent reading review cannot be called trial reading with real readers, and automated scripts cannot be used to validate the reading experience.

---

> **Language / 语言** · [← 简体中文](reader_continuity_review.md) · **English (current)**
