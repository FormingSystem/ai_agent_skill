---
name: build-linux-note-topic
description: "Create, extend, rewrite, reorganize or format technical books and knowledge topics in linux-note. For beginners of the topic, the textbook is compiled according to the changes in readers' understanding and can be read continuously. It uses examples, complete cause-and-effect explanations, hands-on experiments, progressive exercises and natural tone to build understanding and transfer ability. It also supports independent introductory articles and reference pages. Applicable to system technology topics such as Linux kernel, concurrency, drivers, hardware, protocols, embedded engineering and development tools, etc. Provide versioned source code or specification evidence, project boundaries and verification when needed. Layout-only tasks preserve the technical semantics and information units, and the teaching style repairs modify the actual text as authorized."
---

# Building linux-note technical books and topics

> **Language / 语言** · [← 简体中文](SKILL.md) · **English (current)**

Use this English version and its English references for English-language tasks. Respond in the language requested by the user.

Build a body of knowledge that is maintainable, verifiable, and supports continued reasoning over the long term, rather than one long answer. By default, readers have not mastered the abbreviations, source code slang, implementation family names, and project project-specific naming of this topic; first let readers acquire the language needed to enter the concepts, and then organize the material according to cognitive paths. Always distinguish between stable knowledge, versioned source code evidence, experimentation, platform differences, and navigation.

## Make it clear as a condition for completion

The teaching text is completed on the condition that readers can explain, predict, operate and modify. When users require "explain clearly at all costs", within the scope of the authorized topic, the completeness of explanation takes priority over length, generation speed, token saving and single-round closing; if longer text, chapters or multiple rounds of verification are needed, continue to complete. Premise, derivation, command meaning, status changes and recovery after failure must not be omitted in order to save space, nor should "there is already a lot of content", official links or automatic test passes replace the reader's understanding. Delivery responses can be concise and the teaching material cannot therefore be condensed into a summary.

Speaking clearly is not the same as piling up word count. **Markdown documents must not exceed 10,000 words unless necessary; when exceeding, the necessity of splitting must be reviewed, and borderless stacking cannot continue.** Chinese is counted according to Chinese characters, and English is counted according to consecutive words. The main text, tables and code/image text are all included, excluding Front Matter, link targets and HTML tags; use `scripts/audit_document_length.py` for unified statistics. When the length is obviously too large and it contains questions that can be studied independently, split it by question or learning stage. Complete experimental instructions, long but necessary codes, operation cycles and derivation that require continuous reading can exceed the threshold; even if they are only slightly exceeded and the splitting will only leave a short tail, the coherence should also be preserved, and the content should not be forced to be demolished or compressed for the sake of numbers. Just record the specific reasons for retention, and do not require additional user approval for each article. "There is a lot of information" is not a reason. The reason should explain which section of reading or operation will be damaged by splitting it. Causal explanations, original evidence, and the complete operating cycle should be retained. Do not evade the threshold by deleting necessary content, turning text into images, or moving essential explanations elsewhere. After splitting, synchronize the serial number, outline, previous and next chapters, all title anchors and actual callers. Each article has its own problems and closed loops.

Keep the user's existing programming and engineering foundation, but do not regard familiarity with one language as mastering the modules, project organization, and operating rules of another language used in experiments. Supplement the knowledge on which the current experiment is based, and do not expand on irrelevant grammar; each explanation should solve a specific understanding obstacle. When users report that it is "obscure", "outline-like" or "only commands", the explanation chain of the actual chapter must be checked and rewritten. You cannot just add experimental README, glossary, navigation or reference links and claim that the problem is solved.

When writing or rewriting the teaching text, read [Explanation of Writing and Reader Understanding and Acceptance](references/explanation-quality_en.md), and use the independent reading review to check the acceptance and understanding process. Checklists, scripts, and coverage are supporting evidence and do not replace this acceptance.

## By default, it is written as a textbook that can be read continuously.

For C/C++ developers in this repository, teaching examples, mechanism models and supporting tests use C/C++ by default; do not use Python or other languages unless necessary. Exceptions must come from the specific learning task or the real interface of the tool being taught, not just because it is more convenient for the author to implement. Before using the exception, explain its indispensable responsibilities in this experiment, and complete the language and operating conditions required by the reader as follows. When users update their language requirements, they should review the codes, tests, commands and materials that have been introduced in this round, and cannot only restrict subsequent new content.

The teaching text of knowledge topics defaults to a patient, equal, and step-by-step teaching material narrative, and organizes knowledge based on changes in readers' understanding, rather than filling in item by item options, source code fields, or review lists. When users refer to textbooks such as "C Primer Plus" and "C++ Primer Plus", they must implement the required learnability: running through examples, gradually increasing difficulty, natural transitions, appropriate amounts of humor, hands-on experiments and guided thinking; use original content, and do not promise to reproduce the wording of the original book or to obtain the full text of the original book.

Select a reading contract first: **Continuous textbook chapters** can rely on clearly listed preceding chapters, and use brief reviews to recall established understandings without repeating complete definitions;**Independent introductory articles** must locally complete the topic premises within the scope of commitment;**Reference pages** are mainly based on inquiries, and do not force stories and experiments. Markdown files can be opened individually, which does not mean that it must be re-taught the entire topic from scratch. The terms "first explanation", "partial closed loop" and audit below and in the reference documents are all implemented in accordance with this contract.

Explain necessary concepts before current reasoning requires them. The title is allowed to raise questions that have yet to be answered, and it is also allowed to first show a phenomenon to be explained and expand immediately; it is not required to define all the words in the title before the title. Completeness is ensured by the complete set of teaching materials and clear dependencies, without cramming all options, exceptions and implementation details into the first contact. The author's ledger and review requirements remain in the work record, and the text does not show a set of acceptance forms to readers.

**Cross-module content must have a current purpose and cannot be mentioned in passing just because the names are similar.** When this section explains an identity, status or input-output relationship, it is first closed within the object and the layer it belongs to; the rules of different modules such as hardware source number, firmware description number, operating system management number, etc. are not put into a set of unprepared judgments. If deleting this branch does not affect the current derivation, the main text will not insert this branch, and the existing valid knowledge will be returned to its responsible module. When cross-module explanation is really needed, first name the module, the objects it manages, and its specific handover relationship with the current object, explain locally the minimum conclusion needed at the moment, and then give the precise chapter entry that actually exists; the link is responsible for deepening and verification, and cannot replace the explanation of this relationship. It is forbidden to just write "not necessarily the same" or "explain later" without explaining who is responsible, why it is needed now and where to continue. Software initiating configuration, processing equipment, or completing handshakes are real participation actions in hardware transactions and are not removed just because the word "software" appears; the management mechanism of the specific operating system determines whether to enter based on current reasoning needs. See [Crossing Module Boundaries and Current Issues](references/concept_implementation_mapping_en.md#crossing-module-boundaries-and-current-issues) for details.

The title can summarize the conclusion or raise questions, but it does not count as an explanation that has been completed in the main text. Each section should capture the objects, conditions, and unresolved questions brought by the reader from the above; when changing the scene, executor, time stage, or observation level, explain the changes in current reasoning needs and their reasons in the main text. Word order prioritizes moving from known objects to new conditions, actions, and results, not letting words like "therefore, now, this way, it" rely on premises written only in the title or in the author's mind. Follow [Explanation on Writing Section 8.1](references/explanation-quality_en.md#81-the-text-between-the-titles-must-be-connected) to check for cross-title boundaries; do not repeat titles mechanically, and do not impose transitional sentences for naturally coherent paragraphs.

Experiments embed the places where knowledge changes, forming experiences that are predictable, observable, explainable, and modifiable; they cannot be just an acceptance attachment at the end of a chapter. Natural humor serves the purpose of on-the-spot understanding, without ridiculing readers, being cute, or cramming jokes in quantity. For detailed writing methods, practice gradients and sample chapter calibration, see [Explanation of writing methods and reader understanding and acceptance](references/explanation-quality_en.md).

By default, the continuous textbook will write the experiments of this unit in the main text of this unit, and the supporting source code, configuration and input data will be placed in the special material directory. The main text shows the complete small program or configuration required for the current experiment, which can be executed after explanation; the material links are only for convenience of access and comparison, and do not assume the core teaching steps. Each unit only uses the established knowledge and the new knowledge being explained in this unit; it is not allowed to jump to the comprehensive practical training containing subsequent concepts from the introductory chapters, nor to inject the entire course premise into low-level experiments in order to make each linked page "independently closed loop". Please see Section 5 of the explanation of writing method for specific arrangement and inspection.

Operation teaching uses on-the-spot explanations: copyable command blocks are marked with comments to indicate the execution location and necessary environment, and commands or non-detachable operating units are followed by meaning and observation results. The associated explanation must follow [Pair command and description at reading position](references/explanation-quality_en.md#41-pairing-of-commands-and-instructions-at-the-reading-position) gives a conspicuous and unique positioning anchor: the original name and line number of the reused code, configuration file and key, output field, node or step number in the diagram, so that readers can directly know where the text is talking. Keep the code reproducible, verify the anchor points after modification, and do not leave the reader to "guess the correspondence". Establish the relationship between the experimental directory, the source end and the user end, the language module and the Git repository first; explain the difference and actual positioning method when the agreed file name and the author's customized name appear for the first time. Distinguish between files that have not yet been generated and files that already exist. Complete the creation action first and then ask to open the product. For multi-step experiments, the general route is given first, and the same picture and number are reused at the entrance of each step and the current step is highlighted; the repeated navigation diagram assumes the positioning responsibility and is not subject to the deduplication requirements of "representing increments" below. See sections 4.2 and 8.2 of the explanation of writing methods for details.

When users give global comments, save the baseline with comments and record the correspondence between "original opinion → general rules → all affected texts"; local cases are used to refine actual gaps, and tool names, drive letters, or special cases of a certain experiment are not written as global regulations. After the text is repaired, the comments can be moved to the review record, keeping the original text and implementation position. You cannot just delete the mark or just add the rule.

When receiving review comments or readers’ questions, follow [Reconstruct continuous text from questions](references/explanation-quality_en.md#71-reconstruction-of-continuous-text-from-questioning) to re-examine the study sequence of the topic and rewrite the affected complete explanation process. The main text is intended for readers who have never seen the conversation, and is to be accepted based on readability, fluency, guidance, professionalism, and practical reproducibility; answers are not allowed to be added one by one in the order in which the feedback is received, and the review background is not allowed to be written as a teaching background. When component wiring causes misunderstandings, follow [First explain the objects passed across components](references/concept_implementation_mapping_en.md#lets-first-explain-the-objects-passed-across-components) to explain what the interface carries, and then talk about responsibilities and hierarchical processing.

When adding a new chapter to the textbook or correcting the overall writing method, first complete a representative complete sample chapter and verify the experiment to check whether the language, rhythm, content depth and exercises meet the goals, and then proceed according to this quality benchmark. The sample chapter is not an additional approval level: continue working when there is clear authorization, and do not set the default process to wait for the user to confirm chapter by chapter; nor can the sample chapter be used to replace the authorized complete delivery.

## Confirm editing authorization first

Select and describe one of the following modes before editing:

1. **Layout-only:** Applicable to situations where the user explicitly only requires formatting, navigation, numbering, map reading, or layout with reference to a certain topic, especially when the material has been reviewed. Preserves technical semantics, information content, code semantics, diagram meaning, experiments and check items; allows adjustment of heading numbering, white space, lists, tables, navigation, anchor points and other mechanical expressions required for typesetting. When users request to improve teaching material narrative, teaching style, or experimental guidance, they should not mistakenly select this mode just because "style" is mentioned.
2. **Structure-preserving content (structure-preserving):** Applicable to situations where the user explicitly requests splitting, merging, moving or rearranging. Take inventory of each reviewed content unit, move it in its entirety, and do not abbreviate it.
3. **Content modification or rewriting (rewrite):** Applicable to situations where the user explicitly requires addition, error correction, expansion, optimization, rewriting, compression, deduplication, replacement or deletion. Whether the material has been reviewed does not constitute a permanent prohibition on modification; the scope of modification shall not exceed this authorization.

Refactoring alone automatically selects neither rewrite mode nor layout-only mode. It should be judged based on qualifiers such as "reviewed", "typesetting only", "supplementary content", and "rewritten"; if different choices will substantially change the results and the context cannot be determined, confirm first before changing the technical semantics. Very long files, duplicate rules, a cleaner target structure, or warnings from general auditing do not constitute authorization to delete.

## Starting with repository facts

1. Read the current repository's `AGENTS.md`, root `README.md`, information architecture documentation, target topic outline, and Git specification.
2. Check `git status` before editing. Use the target work tree at the beginning of the task as the content baseline to record committed and uncommitted materials; whether to modify its technical content is determined by this user authorization.
3. Only when adding or modifying evidence conclusions, the corresponding specification, chip manual, source code tree or experimental environment will be located and the identity will be verified; when external Linux source code is involved, the version will be rediscovered and checked according to the current repository instructions.
4. Inventory the target directory, incoming links, outgoing links, document IDs, publication lists, Atlas portals, Obsidian products and related authoritative topics.
5. In layout-only mode, inventory and organize existing problem scenarios, and do not replace the original scenarios with new ones, nor change their technical conclusions. In the content creation model, first identify the specific issues that readers need to reconstruct.

Before starting to create, expand or reorganize topics, read [references/topic-design.md](references/topic-design_en.md) and [references/repository-topic-requirements.md](references/repository-topic-requirements_en.md) in order: first establish the cognitive path of technical books, and then select the repository question type skeleton and chapter roles. Do not mechanically superimpose the historical templates of P01~P05. When analyzing concurrency, asynchronous, lifecycle, or multi-role state mechanisms, read [references/mechanism-reasoning.md](references/mechanism-reasoning_en.md). Before mapping the conclusion to the Linux source code, read [references/source-evidence.md](references/source-evidence_en.md). Use [references/rcu-case-study.md](references/rcu-case-study_en.md) when you need to understand how local RCU topics implement reading maps; use [references/lockdep-case-study.md](references/lockdep-case-study_en.md) when involving Lockdep, KCSAN, debug objects, sanitizers, assertions, or other dynamic checkers. Cases are used for correction methods and do not provide a fixed number of articles or field templates. Use [references/review-checklist.md](references/review-checklist_en.md) before delivery.

## Design first and then generate

When creating, expanding or rewriting a topic, perform the generation twice. Complete the design of the entire book first and then start the text:

1. The first step is to establish a working topic blueprint and a terminology dependency ledger, clarifying the reader's starting point and outcome, terminology entry sequence, system panorama, through-scenarios, problem chains, error models, dynamic processes, observation perspectives, hierarchical mapping, engineering constraints and evidence plans;
2. Select chapter responsibilities according to question types, establish a complete chapter dependency graph and each chapter contract, and ensure that each chapter answers "why we talk now, what we take over, what we only solve, and what we leave behind";
3. The main text is generated based on the dependency graph for the second time, allowing the model to be reversely revised if there is insufficient evidence, and not allowing to write a large number of chapters first and then looking for the reason for existence.

The repository officially `大纲.md` only registers real clickable chapters. When generating in batches, the complete plan is retained in the working blueprint, and the formal outline is synchronized after each chapter is implemented; no empty placeholder files or dead links are allowed. The layout-only mode does not re-derive the technical model; the first pass is changed to a content ledger, mapping existing information units to reading stages and destination locations.

## Module identity and classification coordinates

When designing, reorganizing, creating, expanding or rewriting a topic, you must first establish the identities and relationships of modules, platforms, architectures, products, families and generations according to [Module Identity and Classification Coordinates](references/reader_first_writing_en.md#let-modules-platforms-and-generations-be-built-from-scratch), and then organize public responsibilities and differences according to the [Category Axis and Module Variation Matrix](references/reader_first_writing_en.md#first-determine-the-classification-axis-and-module-variant-matrix) of the same article. The final classification known by the author cannot be used as the reader's entry point, nor can it be compared in advance when the classification object has not yet been established.

## Text entry, terminology and continuous reading access control

Before creating, expanding or rewriting the text, you must read the [Text Entry, Terminology and Continuous Reading Access Control](references/reader_first_writing_en.md) in full, complete the chapter entry, terminology dependencies and module closed loops, and perform the independent reading review mandatory acceptance gate chapter by chapter before delivery. The titles, tables, figures, source codes and links that have appeared cannot replace the reader's understanding; this reference retains all entry cards and acceptance conditions and cannot be skipped by automatic audit.

## Balances independent explanations with guidance on reading official materials

The topic must support two kinds of reading at the same time: you can understand the design, concepts and boundaries from the text without opening the official information; when you need to go in depth, you can trace the specific directory location of the official document from the references next to the key explanations. Adopt the evidence contract of [Independent Explanation and Official Material Traceability](references/official_source_reading_en.md#independent-explanation-and-official-information-traceability): mark the document identity and version, chapter number and original title, verifiable entrance and reading questions, distinguish specification requirements, implementation selection, platform integration, teaching deduction and experimental observation. The reference list cannot replace the nearest citation, nor can the citation replace the text explanation.

Chart completion first explains access control through cause and effect: **Background and specific gaps → Why this responsibility or design choice is needed → What can be done and a complete process → Table comparison or refinement**. The sentence "For the convenience of query" or "The manual is as follows" before the table cannot be used to replace the background, function and significance of the appearance; after hiding the table, readers should still be able to explain why the object is needed and how it works, and the table then provides precise fields, values ​​or comparison increments. The necessity of hardware responsibilities and the choice of physical division of a certain product are explained separately, without making up the sole historical cause; for specific inspection, see the self-sufficiency rules in the following chart.

When the reasoning, calculation, comparison or practice answers in the text rely on external charts, please follow [External chart implementation and self-sufficiency of teaching materials](references/official_source_reading_en.md#implementation-of-external-charts-and-self-sufficiency-of-teaching-materials) to present the necessary content and chart reading instructions at the point of first use; do not just give chart numbers, page numbers or links for readers to complete on their own. Before delivery, check the charts one by one to cover the ledger, and verify that readers can draw conclusions from local materials while hiding external links.

The registers and register groups actually explained or used in the text must also list the currently required addresses or access methods, fields and read and write effects according to the [Local lookup table of registers and register groups](references/official_source_reading_en.md#local-lookup-tables-for-registers-and-register-groups); the register name list and manual link cannot replace this table.

The special chapter files that readers browse directly use `PXX_中文主题.md`, which allows the necessary technical identification to be retained; the stable ID, English directory, source code path or official attachment name will not be changed due to Chinese naming. For details, see [Repository Naming and Delivery Requirements](references/repository-topic-requirements_en.md#10-debugging-verification-and-delivery).

## Build understanding from big picture, error models and dynamic processes

The topic begins by explaining "what it is, what problem it solves, where it is in the system, and who it interacts with" before going into APIs, registers, data structures or source code. Panorama only establishes coordinates and does not dump all the terms of mature implementation in advance.

The key mechanisms that are easily misunderstood unfold in the following order:

```text
Why the error model seems to hold true
→ What contradictions occur on specific participants, statuses and timelines?
→ Only increase the model increment required to resolve the current contradiction
→ Reinterpret the original scene with the correct model
→ Explain the conditions and next steps that are not covered yet
```

The same mechanism selects concepts, data structures, state machines, time/timing, CPU/threads/interrupts, callers, source code, hardware and engineering deployment perspectives on demand. All perspectives must reuse the same set of key objects, stages, and events, and must not be written as a list of disconnected knowledge points.

Key conclusions must demonstrate the dynamic process: pre-transition state, triggering actions, intermediate propagation, completion conditions, post-transition state, and failed branches. Diagrams are the second set of expression systems for status, timing, Before/After, hierarchy, data flow, roles, and life cycles; arrows mark actions or status flows, and the text explains key transitions. Decorative diagrams may not be used in place of derivation, Mermaid wraps using `<br/>`, not `\n`.

Each Mermaid `sequenceDiagram` must provide a positionable sequence number, and `autonumber` is used by default; the key transition instructions after the picture must quote these step numbers, not just "before" and "after". When two solutions, configurations or failed/normal paths need to be compared, if they have different conclusions about "whether an action occurred at the same moment", participant set or proof conditions, use two independent timing diagrams that reuse the same set of object names, and mark the difference with color; only branch within one diagram when the two paths truly share the same timeline and `alt` does not cause ambiguity that the event has occurred/not occurred.

## Strictly distinguish abstraction layers and establish mappings

The concept stage uses the terminology of the selected specification or contract to first establish responsibilities, status, input and output, and object counting units; when entering product, platform, or source code implementation, the version and level are first explained, and then the actual carriers by which these concepts are realized are explained, and then the internal processes and benefits are launched. Even if specification terms and product terms have the same name, they cannot be synonymous, have the same boundary, or have the same number; implementation names must not be used to replace unestablished concepts.

When explaining the start, switching levels, and section entrances that can be entered independently, first use a short line visible to the reader to mark **Explanation Level: Concept Layer** or**Explanation Level: Implementation Layer**, and indicate the specification/contract or product/source code version; when bridging the two layers, mark**Explanation Level: Concept to Implementation Mapping**. Annotations must appear before the main text is expanded, and cannot only exist in the author's blueprint, metadata, or at the end of the text; consecutive paragraphs at the same level should not be repeated paragraph by paragraph, and there is no need to add another line when the title has clearly marked the level and object.

When it comes to cross-layer correspondence, physical partitioning, shared implementation, or when users ask "include or connect, and who to configure", you must read [Concept to Implementation Mapping and Input and Output](references/concept_implementation_mapping_en.md). The text accomplishes three things at the first cross-layer: ** Count the logical objects and implementation carriers that can be confirmed by the data; distinguish implementation, inclusion, connection and address views; follow an operation to the location where the state is actually saved and modified**. When one module carries multiple logical objects and one logical responsibility is dispersed among multiple modules, the confirmed responsibilities and status points should be explained one by one, and the undisclosed parts should be clearly marked; the corresponding relationship cannot be replaced by "integration" or "partially implemented", nor can one draw an independent physical device per core based on one logical object per core.

Figures and text use the same set of objects and borders. The relationship diagram illustrates whether the box represents a physical module, functional partition, or logical ownership; the transaction diagram marks the actual endpoints and directions of request, configuration, response, and completion respectively. The visible address of the software, the access entrance and the location of the status are explained separately. The forwarded access is not written to modify the status of the entry module itself, nor does it create independent objects and status synchronization lines. Explain convergence, selection, and target identification when multiple objects share interfaces; establish implementation paths before talking about routing, grouping, or power gains, and differentiate between structures determined at design/integration time and strategies configurable at runtime.

Also check the API contract and internal mechanism, software synchronization and hardware consistency, protocol guarantee and platform capability, stable model and version source code respectively, and guarantees cannot be borrowed across layers. Check the mapping with the corresponding level of specifications, implementation manuals, source code, or experiments. Internal structures that have not yet been disclosed are clearly marked as unknown, and confirmed attributions are stated directly; established relationships must not be obscured with uncertain details. Before delivery, use the independent reading review questions in the mapping reference to test whether the reader can locate the actual object, track the configuration, and predict the results. You cannot just check whether "logical and physical differences" are written.

**Changes and invariants must be bound to specific operations.** First answer the current question directly, and then point out the comparison object, action, time before operation and after taking effect, and necessary conditions; "not affected by this operation" cannot be written as "never change". For confusing relationships, use a before-and-after table or a sequence diagram, which only displays the dimensions required for this question and does not introduce additional operations for filling in the table. Follow [Changes and invariants must be bound to actions and time points](references/concept_implementation_mapping_en.md#changes-and-invariances-must-be-bound-to-actions-and-time-points) to check the necessary boundaries.

## Adjust the order of explanation according to question type

- **Data structure and API:** After the minimum concept and contract are established, common operations, minimum correct usage, failure cleanup and typical patterns are given as early as possible, and then the internal structure, dynamic algorithm, implementation evidence and performance selection are introduced; when algorithm questions are involved, question type identification, simple solutions, optimization motivations, complexity, hidden boundaries, error prone points and deformations are supplemented.
- **Hardware, chips and protocols:** Starting from the system location and conceptual responsibilities, first map the specification roles to the selected implemented modules, states and interfaces, and then unfold the signals, timing, registers, drivers and board-level constraints along a complete transaction; do not directly repeat the data sheet directory.
- **Kernel mechanism and concurrency:** Starting from problem pressure and abstract proof, closed state ownership, communication, completion notification and source code evidence; the concurrency mechanism at least provides role/state relationship diagram and end-to-end sequence diagram.
- **Engineering system:** Also include resource budget, build output, image or deployment layout, startup process, fault recovery, observability and acceptance; a solution that is theoretically correct but cannot be implemented in the target environment is not considered complete.

## Distinguish product responsibilities

The conclusion is saved according to the product concept; the specific source code implementation of the same version is only expanded once:

| Hierarchy | Responsibilities |
| --- | --- |
| `knowledge/` | Cross-version stable mechanisms, causal explanations, API contracts and choice boundaries |
| `research/source_reading/` | Precise version, configuration, source code path, fields, functions and call chain |
| `labs/` | Minimum reproducible experiment to verify a single conclusion |
| `platforms/` | Architecture, SoC, BSP or development board specific behavior |
| `atlas/` and topic `大纲.md` | Reading order and links, do not copy the second tutorial |
| `reference/` | Query-oriented API, command, term or external data index |

The dynamic validator topic also separately records: the true functional state of the mechanism being checked, the shadow state of the current task/CPU, the global history accumulated across time, and whether the checker itself is enabled, recursively suppressed, exhausted, or has been stopped. The check event may occur before the function attempt or in the failed fallback path. The true sequence must be checked. It cannot be inferred that the function action has been completed just from names such as `acquire` and `release`.

The `knowledge/` text and the `research/source_reading/<topic>/navigation/` module concept introduction can retain necessary overlap around the same mechanism, but cannot replace each other: the former establishes a stable causal model, interface contract and application selection across versions, while the latter organizes source-code entry point, status placement, function collaboration and reading order for a specific version. The same terminology, status stage, call chain conclusion or necessary background shall not be directly judged as duplicate, nor shall the editing of one layer automatically delete, synchronize, merge or rewrite another layer. A single expansion only constrains the upstream macro body, function body and sentence-by-sentence implementation instructions of the same version; only when the user scope or link, version and fact boundaries are clear and affect both layers at the same time, both sides will be reviewed and modified independently.

In content-preserving restructure or rewrite mode, general hardware, compiler, memory ordering, or object lifecycle interpretation cannot be moved until the destination has been documented. In the layout-only mode, the display form can be adjusted according to the layout objectives and authoritative links can be added, but the technical semantics must not be changed or the original information units should be omitted.

## Source code reading organization and implementation explanation

When using versioned source code evidence in the body of knowledge, or when creating, modifying, organizing, or reviewing source code concept introductions and implementation explanations for tasks, you must read [Source Code Reading Organization and Implementation Explanation](references/source_documentation_workflow_en.md) and [Source Code Evidence Specifications](references/source-evidence_en.md) in full. Based on this, establish a general index, module concept introduction, unique implementation title and precise interconnection, explain source code symbols that affect behavior item by item, and verify that readers can predict the impact of local modifications; source-code links cannot replace local explanation, and external source code trees must not be modified.

## Keep traceable across chapter stages and data structures

When the downstream chapter enlarges the complete cycle, state machine, stage table or function module that has been established in the upstream chapter, you cannot just write "Undertake PXX". A **stage back link** must be established:

1. If the upstream stage table needs to be accurately referenced by other chapters, place the table under a complete title that can be stably jumped according to the true handover boundary; do not rely on a single table row without a title anchor.
2. For downstream chapters, if new numbers such as R0~Rn, T0~Tn, etc. are created for local modules, a "local stage → upstream public stage" crosstab will be given before the first expansion, with each row linked to the complete title anchor of the upstream.
3. The text, tables, figures, source code, and subsequent experiments all reuse this cross-relationship; the two sets of stages must not be allowed to advance independently, and then readers are required to align themselves.

When a data structure, object field cluster, register block or protocol header takes on reasoning responsibilities for the first time, it must also provide **local minimal explanation + independent structure entry**: the local first explains what type it is, who owns it, what the current field saves in this handover, who writes and who reads; then use the full title anchor to link to the authoritative data structure, state machine or versioned implementation explanation. If there is an authoritative entry, reuse it directly without copying all the fields of the structure; if it does not exist, create an independent explanation only when the structure can be reused across scenarios or this chapter cannot be self-contained at the required scope, without creating micro-documents for each field.

## Establish a cause-and-effect learning chain

Use this section when designing new material or organizing existing chapters in your outline. The formatting-only mode only changes the reading organization and presentation form, and does not re-demonstrate or replace the reviewed technical content.

Unless the specific domain demonstrates that another order is clearer, the following order is used:

1. **Issue Pressure:** Show the real load, the actors, the old scheme, the guarantees provided by the old scheme, and the precise staggering or size of the exposure gap.
2. **Abstract deduction:** Deduces roles, states, time bounds, and proof obligations from constraints without using Linux field names.
3. **Minimum closed loop:** After the abstract contract is established, the minimum correct interface, normal path, failure path, cleanup and dismantling should be provided as soon as possible, so that subsequent implementation discussions can have a specific focus.
4. **Classification coordinates and common skeleton:** When there are multiple families or configurations, distinguish the orthogonal axes first, and talk about the roles, modules and complete cycles shared across variants only once.
5. **Model Differentiation and Hardening:** Split the execution model only if the set of participants or proof methods are indeed different; use applicable counterexamples to test future participants, asynchronous windows, migrations, overlaps, reordering, and object escapes.
6. **Module implementation and variant differences:** Map the abstract state to address, owner, writer, reader, communication and completion conditions according to functional modules; public implementation first, then compare variant differences, only split for truly independent sub-state machines or implementation families.
7. **Application, Experimentation, and Choice:** Provide combinations, diagnostics, observable experiments, misuse, cost transfers, and alternative conditions to indicate when the original solution is still more appropriate.
8. **Evidence and Navigation:** Save stable knowledge, versioned source code, experiment and platform evidence by responsibility, update outline, previous/next article links, stable ID and repository check.

Maintain the cognitive suspense chain: first retell the established conclusion, and then raise a specific problem that it cannot explain; use counterexamples to expose the missing state dimensions, and only add the roles, states, communication paths or constraints required to solve this round of counterexamples; then use source code or experiments to realize the new model, and hand over the unresolved problems to the next chapter. Do not present all fields and terminology of a mature mechanism at once before the problem arises.

The beginning of a chapter gives priority to explaining "what has been proved in the previous chapter → what still cannot be explained → what this chapter only solves", and the end of the chapter explains "what can be proved now → what still cannot be explained → what continues to be tracked in the next chapter". This is a mental bridge and does not require mechanical use of the same section headings.

After the text is rewritten or the responsibilities are expanded, follow [Title Contract](references/reader_continuity_review_en.md#title-deed) to recheck the current title, parent-child scope, and sibling issue advancement relationship; the title should allow readers to see specific objects and their design issues, cause and effect, or role relationships, and old generalizations that have broken the contract cannot be retained. The title does not need to be a question, and it does not rely on lengthening or stacking terms to express the completeness; after the name is changed, Typora's complete title anchor, actual link and navigation will be synchronized.

Don't force all stages into one file. If a document hosts multiple independently learnable mechanisms, or if source code details interrupt causal explanations, the document should be split. Short bridging documents should only be retained if continuity responsibilities are truly assumed.

## Let the chapters responsible for proof start from specific scenarios.

Use this section when creating or rewriting content. In layout-only mode, the technical semantics of the reviewed scenes are preserved and only their order and relationships are made explicit.

Before talking about theory, establish:

- Named loads and their sizes;
- Specific tasks, CPUs, interrupts, threads, callbacks or devices;
- The storage location of shared state;
- A real or structurally complete code path sufficient to fix the problem site;
- Expected interleaving and observable failures;
- Correctness properties that need to be protected.

The theory that addresses this scenario is then explained. The full application code must cover allocation, publication, error cleanup, teardown processes, and critical race statements; the minimal live code in the problem chapter does not have to assume full responsibility for the final API template in advance.

## Write the complete example into a small closed loop that can be accepted

Mere code blocks do not constitute a "complete instance". When the user requires a complete, specific, runnable or sufficient example to explain the purpose, at least close the following content:

1. **Requirement background:** Who encounters what limitations in what tasks, and why the current syntax, macros, interfaces or mechanisms are needed;
2. **Environment and Boundaries:** Language/kernel/tool version, configuration and runtime context; indicate whether it is upstream as-is code, fully structured tutorial code, or a scenario fragment that isolates the problem;
3. **Input and preparation:** Necessary types, status, initialization, call entry and test data, do not let key objects appear out of thin air;
4. **Normal and failure paths:** Show successful actions, at least one failure or incorrect usage related to the topic, and accompanying rollback, cleanup, release, or exit;
5. **Step-by-step process:** Expand key macros, call chains, state changes, evaluation times or artifact flows so that conclusions can be derived from the process;
6. **Observation and Acceptance:** Give executable commands or clearly observe the location, expected output/diagnosis/status, and explain what the results prove;
7. **Proof Boundary:** Describe what this example cannot prove, which platforms or configurations require additional verification, and link to authoritative implementations or specifications.

Example complexity is tailored to the topic, but statements that happen to determine correctness cannot be omitted. Orphaned functions, declarations without callers, success paths without cleanup, commands without expected results, macro definitions without expansion of call locations, shall not be marked as complete instances. If only a minimal scene is needed for this chapter, it should be clearly called a "scenario fragment" or a "cropped example" and linked to the complete instance that has been closed.

The topic of concurrency or multi-role mechanics as a whole includes at least:

- A role/state diagram with arrows indicating the flow of states or ownership;
- An end-to-end sequence diagram covering the normal path and key branches that change state ownership;
- Reuse the same set of S0, S1... cycles for the complete state mechanism and illustrate it with a phase table;
- Clearly distinguish between safety and liveness;
- Explain where the removed costs go and the choice boundaries.

Diagrams and tables should be put into corresponding chapters according to the need for proof, and there is no requirement to have a separate set for each article.

Mermaid uses `<br/>` for newlines and must not use `\n`.

## Explicitly model distributed state

First explain whether the mechanism is a single state machine or composed of multiple orthogonal state axes. Distinguish between the current state, the historical events that have been latched, the generational evidence that binds operating cycles, and the pending debt that remains unpaid. Each stage is recorded:

| Must-have facts | Must-answer questions |
| --- | --- |
| Trigger conditions | What events cause the mechanism to enter this stage? |
| Before and after transition | Which precise state changed? |
| Storage location | In which structure, task, per-CPU region, node, object, or global address is the state located? |
| Writer | Which execution context completed the write? |
| Reader | Which subsequent path consumes this status? |
| Communication method | Local write, shared memory, lock, polling, callback, wake-up, IPI or hierarchical reporting? |
| Exit conditions | What conditions must be met to enter the next stage? |

When the mechanism actually has corresponding state transfer, aggregation or asynchronous completion, the following loop is closed; if there is no such link, the actual completion method is explained, and no shared registration or background thread is created for the application list:

1. How does local state become shared state when state ownership changes?
2. How local evidence converges into global conclusions;
3. How does the waiting party or delayed action know that the conclusion has been completed.

Clearly state whether the mechanism uses direct registration/notification, or indirect proof through "invariants + observed events" that the participant has crossed the boundary. Why a future participant does not belong to the current set must be demonstrated by entry, generation, or protocol boundaries.

When removing a global registration or notification from a fast path, describe how the transferred work appears in the normal per-operation path, the special state transition path, and the deferred or forced path.

## Handle object lifecycle individually

Distinguish between publication reachability, temporary protected access, long-term ownership, grace period completion, callback execution, and final memory destruction. Before combining RCU, kref/refcount, locks, work queues, or module teardowns, draw an allocation versus ownership diagram.

There can only be one final destruction protocol per allocation. Do not imply that independent mechanisms automatically notify or adapt. Make it clear which module callback transfers control from one mechanism to the next.

## Refactor, verify and deliver

Before each task of this skill is delivered, you must read and execute [Refactor, Verify, and Deliver](references/delivery_validation_en.md) in full, save the baseline as authorized, migrate the content in full, synchronize the real caller, run length, structure, continuous reading and terminology auditing, and applicable content conservation checks. Script reports require manual judgment and cannot replace independent reading review; accurately report performed and unexecuted verifications. `apply_patch` is used for editing and shall not be staged or committed without the explicit request of the user.

---

> **Language / 语言** · [← 简体中文](SKILL.md) · **English (current)**
