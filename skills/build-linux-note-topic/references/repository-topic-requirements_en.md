# Refined requirements for repository AI topics

> **Language / 语言** · [← 简体中文](repository-topic-requirements.md) · **English (current)**

## Contents

- [Source and Priority](#1-source-and-priority)
- [One sentence main line](#2-one-sentence-main-line)
- [Select chapter skeleton according to question type](#3-select-the-chapter-skeleton-according-to-the-question-type)
- [Bottom line of content common to all topics](#4-common-content-bottom-line-for-all-topics)
- [Zero-based terminology access control](#41-beginner-terminology-acceptance-gate)
- [Structural classification zero-based access control](#42-structural-classification-beginner-oriented-acceptance-gate)
- [Four consecutive questions on syntax, interfaces and configuration](#5-four-consecutive-questions-on-syntax-interface-and-configuration)
- [Multiple viewing angles are a condition requirement](#6-multiple-perspectives-are-a-requirement)
- [Sample code requirement](#7-sample-code-requirements)
- [Charts and tables requirements](#8-requirements-for-charts-and-tables)
- [Source code reading reuse structure](#9-source-code-reading-reuse-structure)
- [Debugging, Verification and Delivery](#10-debugging-verification-and-delivery)
- [Historical requirements that should not be promoted to general hard rules](#11-historical-requirements-that-should-not-be-elevated-to-universal-hard-rules)
- [Simplified Acceptance Checklist](#12-streamline-the-acceptance-checklist)

## 1. Source and priority

This reference is extracted from the following materials currently in the repository:

- Current identified “technical book/topic generation” requirement baseline;
- `tools/ai/topic_summary_requirements/P01_主题章节的要求.md` ～ `P05_主题章节的要求.md`；
- `tools/ai/application/mermaid_require.md`；
- Writing, information architecture, source code, and topic organization requirements for current repository `AGENTS.md`.

The general cognitive design of technical books is subject to [topic-design.md](topic-design_en.md); this file is responsible for making it fall into the question type, directory and format constraints of linux-note. The historical requirements are oriented to different manuscripts, question types, and time points, and cannot be mechanically superimposed into a set of fixed chapter templates. When a conflict occurs, follow the following order: the user's explicit request, the current `AGENTS.md`, the current information architecture and format specifications, and the extraction rules of this reference; the question templates in the historical files are only used as structures for on-demand selection.

## 2. One sentence main line

Complete the following closed loop around a clear theme:

> Establish a system panorama and reader coordinates → Clarify the problem to be solved or the task to be completed → Explain why the old solution or wrong model seems to be valid and how the gaps are exposed → Expand the actors, states, data structures and dynamic processes → Map to source code, hardware, configuration or interface → Give complete usage and examples → Provide observable verification → Explain engineering constraints, boundaries, alternatives and subsequent relationships.

This thread is a common bottom line and does not require all chapters to have the same title.

The main text must also pass **broken link continuous reading**: assuming that the publication hides the URL and the reader does not click on the link, the current chapter can still complete the concepts, problems, solutions, dynamic processes and conclusions promised by the title. Links are only responsible for supplementing versioned evidence, complete function bodies, or cross-topic depth, and cannot replace the first explanation. The presence of titles, diagrams, stage tables, source code links, and checklists only indicates that the material exists, but does not mean that the chapter has formed a cognitive path.

At the same time, **official material reading guidance** is provided: keep precise table of contents entries and reading questions next to key concepts and conclusions, and do not just list reference materials at the end. The evidence granularity, name verification and acceptance of the two reading paths are uniformly adopted [Independent explanation and official data traceability](official_source_reading_en.md#independent-explanation-and-official-information-traceability), and no separate set of citation templates will be created.

## 3. Select the chapter skeleton according to the question type

| Question type | Priority skeleton | Content that must be strengthened |
| --- | --- | --- |
| Kernel mechanism, concurrency and competition | Problem pressure → Abstract mechanism → Real condition reinforcement → Linux implementation → Usage → Cost and choice | State ownership, communication path, S0...Sn, role graph, end-to-end timing, source code evidence |
| Data structure, algorithm and API | Usage issues → Minimum correct usage → Common operations → Internal structure and dynamic algorithm → Implementation → Complexity and choice | Error model, Before/After, boundary conditions, failure cleanup; algorithm question on-demand problem type identification, naive solution, hidden testing and deformation |
| Chips, controllers and communication protocols | System location → One complete transaction → Signals/timing → Registers and state machines → Driver mapping → Board-level constraints → Debugging | Participating devices, signal directions, sampling edges, register states, waveforms, platform capabilities and electrical boundaries |
| Driver interface, DTS, U-Boot, Buildroot or configuration syntax | Topic introduction → Data structure → Developer perspective → User/platform perspective → Illustrations → Examples → Debugging and verification → Summary | Four consecutive syntax questions, mapping of configuration to kernel objects, user observable results, consequences of incorrect configuration |
| Application-oriented usage of modules or primitives | Concepts → What can be done/cannot be done → Core patterns → Mashups and boundaries → Common pitfalls → Minimal templates → Checklist | Context restrictions, combination order, anti-patterns, pasteable templates |
| Engineering system, upgrade and deployment | Goals and constraints → Resources/layout → State machine and normal process → Failure and recovery → Build deployment → Observation and acceptance | Flash/RAM/Bandwidth budget, link and mirror layout, power-off/rollback, idempotence, security boundary and target environment achievability |
| Complete chapters for publication | Background and goals → Principles and implementation → Usage → Interfaces/Tools → Differences and limitations → Complete examples → Summary | Complete chapters, continuous titles, explanations of chart codes, and connections with previous and subsequent chapters |

Determine the question type first, and then cut the skeleton. All historical templates such as "seven-stage method", "eight-step method", "three tables per chapter" and "pure causal chain" must not be forced to be applied at the same time.

When the same question type also contains public APIs, multiple implementation families, or configuration variants, execution must continue within the skeleton:

```text
Realistic problems and naive models
→ Why new modules or changing dimensions appear
→ Identity and relationship coordinates of modules, platforms, architectures, families or generations
→ Public concepts and interfaces
→ Orthogonal classification axis
→ Common end-to-end skeleton
→ Discuss public implementations by functional module and compare variant differences
→ Source code or experimental verification paired with the conclusion
```

The classification axis is implemented internally earlier than the variant; the functional module defaults to the main axis that implements depth. Only when the variant changes most of the participants, the proof method and the completion path, it becomes an independent article vertically. The same public implementation must not be packaged into "Variant A complete source code chain" and "Variant B complete source code chain" respectively, and then expand by module for the third time later.

## 4. Common content bottom line for all topics

Regardless of which skeleton is used, the following issues should be covered as applicable:

1. **Topics and Results:** What does this article focus on, and what process can the reader reconstruct, what choices are made, or what actions are completed after completion.
2. **Background and motivation:** What was solved by the original plan, default behavior or status quo, and how the specific gap was formed.
3. **Objects and states:** Who are the participants, where the state or configuration is saved, who writes, who reads, and when it is converted.
4. **Mechanism and implementation point:** How to implement abstract principles into data structures, call chains, configuration items, registers or user interfaces.
5. **Usage and closed loop:** Provide a sufficiently complete process of initialization, normal path, failure path, cleanup and dismantling.
6. **Observation and Verification:** Provide commands, logs, traces, sysfs, `dmesg`, experiments, or other actionable evidence, and describe expected results.
7. **Boundaries and Choices:** Describe what can and cannot be done, common misuses, alternatives, and applicable conditions.
8. **Summary and connection:** Extract key invariants, check items, and their relationship with previous and subsequent topics.
9. **Transferability:** Give a variant, load, or failure condition that has not been stated verbatim, allowing the reader to continue derivation using the established model.
10. **Terminology entry:** For concepts that readers have not yet established and must rely on for current reasoning, the necessary names, meanings, responsibilities, and boundaries are first explained; continuous textbooks can review clear prerequisite knowledge, and independent introductory articles can complete the prerequisites on their own. The observation material in which the title raises the question and is followed by the explanation does not require full definition in advance.

If an item is irrelevant to the current topic, you can omit it, but you cannot use a vague conclusion to replace the key derivation that underlies the choice of the solution.

## 4.1. Beginner terminology acceptance gate

The knowledge text of linux-note can be arranged as a continuous textbook, or can be read as independent articles or reference pages; the prerequisites are determined according to the reading contract of SKILL.md. The continuous textbook gives the full formal English name and accurate Chinese name when the concept is first established, and then connects it with a brief review and a clear front-end entry, without re-teaching the entire set of definitions in each chapter. The independent introductory article completes the premise of its own commitment. When commands, projects, implementation families, historical nicknames and source code identifiers are not abbreviations, indicate the nature of the name and do not make up the full name.

The first definition of the "name and prominence" rule according to [Text Terms Access Control](reader_first_writing_en.md#beginner-terminology-acceptance-gate-align-language-first-then-expand-concepts) is bolded as **Chinese Name (English Full Name, ABBR)**, and the abbreviation is omitted when there is no common abbreviation. Try to keep half-width spaces between bold and adjacent plain text, and do not force spaces next to punctuation points. Later, I mentioned whether to highlight the reading focus, do not bold the entire paragraph, and do not write Markdown bold tags into the source code, commands, identifiers or Mermaid syntax.

Check whether titles, navigation, text, tables, figures, code, configuration, and logs require readers to use unestablished knowledge. It is allowed to ask questions or demonstrate phenomena to be explained first; it is not allowed to let unfamiliar nouns assume unexplained reasoning premises. When nouns are intensive, the learning stage is divided and gradually introduced by tasks. A centralized glossary cannot be used to replace the progressive explanation, nor can subsequent definitions be used to make up for the current reasoning breakpoint.

For each term that affects the boundaries of understanding or conclusion, answer at least:

1. What is the Chinese and English name, or why is it just a proper name/identifier that cannot be expanded;
2. Does it belong to a concept, role, state, phase, implementation family, execution model, strategy, diagnostic, configuration, or source code symbol?
3. What it really is when it doesn’t rely on the jargon of this topic;
4. Who owns or uses it in the current scenario, what it receives, what it changes, and when it takes effect;
5. What it doesn't guarantee, who it's most likely to be confused with, what version, architecture or Kconfig boundaries are;
6. Where are the minimal local explanation for the current chapter and the full title anchor for authoritative depth.

New proper nouns appearing in definitions must first be explained recursively. Links are only responsible for in-depth and evidence, and cannot replace local explanations; a local sentence cannot pretend to be a complete tutorial. When an ordinary English word is given a private meaning by a subsystem, it is treated as a proper noun, and the naming subject, scope, actual object or state placement point is explained. When the space is insufficient, split or add front entries, and do not skip the alignment of terms and directly expand the concepts.

## 4.2. Structural classification beginner-oriented acceptance gate

linux-note does not treat topic structures already known by the author as reader knowledge. Even if modules, categories, platforms, architectures, products, implementation families, versions, and generations appear in user goals, official material catalogs, or topic outlines, their identities, levels, and relationships must be explained first before assuming the responsibility of reading diversion or comparison.

Combined goals can be used in working blueprints, such as "public mechanism + vertical implementation of multiple platforms + intergenerational comparison"; the formal reading route must expand it into "real events or tasks → simple solutions → gaps → new modules → identity and relationships → minimum closed loop → first set of implementation → new constraints → subsequent implementation or intergenerational → coaxial comparison." You cannot directly use the final category as the opening table of contents. By default, readers already know what platforms and generations are.

Before comparison, the topic of hardware and platform establishes the relationship between "standard or instruction set architecture, processor core or controller implementation, SoC integration, development board connection, firmware, operating system framework and driver" based on facts. The software topic accordingly establishes the relationship of "contract, framework, implementation, configuration, caller, and operation result". Each name has to answer: what it is, why it exists, who it is connected to, who defines or implements it, and what axis it is distinguished from adjacent names.

The first platform or implementation first independently closes its own identity and a complete transaction; subsequent platforms or generations are introduced by new scale, capabilities or constraints. Before the objects on both sides have been independently created, a difference table, a table of advantages and disadvantages, or a conclusive generational overview must not be given first. When comparing, distinguish between specification differences, implementation differences, chip integration differences, board-level differences, configuration differences and software version differences, which cannot be collectively referred to as "different platforms."

## 5. Four consecutive questions on syntax, interface and configuration

When encountering a DTS property, kernel interface, configuration item, command, or syntax, answer at least:

1. What is its role and semantics;
2. In what scenario, stage or execution context is it used;
3. What happens if you don’t write it, write it wrong, or use the default value;
4. Which driver, parser, call or register path it is consumed by.

Draw and explain as needed when DTS or configuration mapping is involved:

```text
Configuration/Syntax → Parsing entry → Kernel object or descriptor → Driver usage path → Hardware or user observable results
```

Only expand fields directly related to the syntax, and do not list structures without boundaries for the purpose of displaying source code. Mapping can be one-to-many, many-to-one, or the original value will no longer be retained after conversion. The "one-to-one correspondence between attributes and structures" in the historical template cannot be regarded as an implementation fact; the inclusion, reference, parsing, and calling relationships of objects are checked separately.

## 6. Multiple perspectives are a requirement

- **Developer perspective:** How to call API, how to write callbacks, context, error handling and resource release.
- **User Perspective:** What can the user space see, how to operate and verify.
- **Platform Perspective:** How DTS, ACPI, SoC, BSP or build configuration affects behavior.
- **Kernel Perspective:** How data structures, call chains, configuration branches, and state transitions fulfill the contract.

Driver, interface, and configuration topics often require multiple perspectives; purely abstract mechanism chapters can retain only the perspective relevant to the proof. Do not repeat irrelevant content just to get the perspective.

## 7. Sample code requirements

- Examples should compile, or at least be well-structured and clear of uncompiled environment boundaries.
- Covers allocation/initialization, release or registration, normal operation, failure cleanup, undo, and final deallocation.
- The repository's own examples use Chinese comments; clearly mark the reference boundaries when quoting the upstream source code as it is.
- Use text or diagrams to illustrate the execution logic before the example, and explain the key steps, invariants, and observable results after the example.
- Only when the topic involves the resource hosting API, compare the non-`devm_` and `devm_` versions, and explain the release logic and applicable boundaries; devres must not be forcibly extended to all topics.
- Minimal templates serve reuse, but cannot omit statements that exactly determine correctness.

## 8. Requirements for charts and tables

- Diagrams are used to explain state changes, communications, call chains, ownership or hierarchical relationships that are difficult to see visually through text. Diagrams are not piled in a fixed number.
- The concurrency mechanism complies with the current `AGENTS.md`: at least include role/state relationship diagrams and end-to-end sequence diagrams, and label actions or state flows.
- Mermaid `sequenceDiagram` uses `autonumber` by default. The explanation behind the diagram uses step numbers to locate key transitions; wide timing diagrams that do not provide a positionable sequence shall not be delivered.
- If the two compared paths have different conclusions about whether the event occurred, the set of participants, or the proving conditions, use two independent timing diagrams that reuse the same set of object names, and mark the difference with color; do not use a single diagram `alt` to put mutually exclusive events on the same timeline.
- Mermaid uses native syntax, uses English double quotes for node labels, and names in the figure are consistent with the text and code; comply with the current rules of `tools/ai/application/mermaid_require.md`.
- Do not escape the entire piece of Mermaid as HTML, nor use transparent `level` sub-images to forge hierarchies; when you really need to display special characters, use tag escapes supported by the target Mermaid version and actually render them. "Not block escaping" cannot be extended to prohibit Mermaid's own legal syntax.
- Tables are prioritized for side-by-side comparisons, interface overviews, status matrices, and delivery checks; "three fixed tables per chapter" are no longer used as a mandatory acceptance gate for all question types.
- Automatic auditing checks the necessary code, relationship diagrams, and sequence diagrams by topic as a whole, and does not use "one copy for each chapter" as an alarm condition.

## 9. Source code reading reuse structure

- When the same source code topic includes both module reading and specific implementation explanations, use `navigation/` and `source_explanations/` under `research/source_reading/<topic>/` to separate responsibilities, and do not mix the two types of Markdown in the root directory of the topic.
- `navigation/` contains a total reading index and source code concept introduction organized by sub-functions/modules. The general index links all module guides; the module guides use source code to explain module responsibilities, participants, status, call chains and reading order. They can include application code, pseudocode, tables and Mermaid, but do not expand upstream macros or function bodies step by step.
- `source_explanations/` organizes documents according to specific macros, functions, fields or closely related implementation clusters; the same implementation of the same version has only one authoritative explanation title. Each implementation explanation links back to the general index and the introduction of the module it belongs to, and provides the upstream relative position, Chinese Doxygen comments supplemented by the repository, Chinese inline source code, implementation principles, calling context and status side effects.
- When the knowledge text uses version source code evidence for the first time, link the total reading index and related module introduction. When encountering a specific interface or checkpoint, link "relative file path + Typora complete title fragment", and do not copy the existing source code implementation explanation.
- When a data structure or field cluster is first responsible for mechanism reasoning, the current chapter first locally describes the type, owner, current responsibility, and reader/writer, and then uses the complete title anchor to jump to the authoritative structure/state machine/version implementation explanation; neither just throws the structure name, nor copies the entire field.
- After the directory is moved, the topic outline, source code baseline, Markdown/Obsidian and other incoming links will be synchronized, and the old paths will be cleared from the entire repository without retaining compatible copies.

## 10. Debugging, Verification and Delivery

- Every important conclusion should explain how to observe it, not just give the command a name.
- The debugging section at least states the operation steps, expected output, failure phenomena and positioning direction.
- Experiments must describe the environment, version, configuration, execution method, expected results, and cleanup method.
- If the chapters are too long, they will be divided into whole sections as boundaries and cannot be cut off in the middle of codes, tables, figures or derivation.
- Freeze the working book blueprint and chapter contracts before generating them in batches; subsequent batches must not be reduced to abstracts due to the growth of context. When evidence overturns the design, the outline and affected chapters should be revised simultaneously.
- The output directly adheres to the current title, metadata, relative links and Chinese code comment specifications of the repository, and does not copy the old numbering style in the historical template.
- The special chapter file for readers uses `PXX_中文主题.md`. The Chinese name directly describes the content of this article. Necessary product names, abbreviations and technical symbols can be retained. The domain directory continues to use English `snake_case`, and the stable ID, source code path and official attachment name will not be translated accordingly; existing files will only be renamed within the scope of this naming or reorganization, and the real caller and anchor point will be synchronized.
- Check content scope, source code boundaries, sample completeness, diagram syntax, links, metadata and `git diff --check` before delivery.

## 11. Historical requirements that should not be elevated to universal hard rules

The following content is only used when explicitly requested by the corresponding project or user:

- Fixed seven-part formula, eight-step method, or three tables per chapter;
- It is an absolute requirement to choose one of "module as the key link" or "problem-driven"; the current core mechanism topic gives priority to the causal learning chain specified by the repository;
- Fixed i.MX6ULL, GIC version, kernel version or a certain DTS node as default example for all themes;
- All chapters must have four perspectives: user, developer, platform and kernel;
- All resource topics must display version `devm_`;
- Each chapter must make up the quantity for the charts;
- Any old Mermaid HTML escaping rules.

These historical terms can still be used as templates for specific manuscripts, but they cannot cover the current repository specifications or this user's intent.

## 12. Streamline the acceptance checklist

- [ ] The chapter skeleton that matches the question type has been selected, and no conflicting historical templates have been superimposed.
- [ ] The modules, platforms, architectures, implementation families and generations in the working blueprint have not directly become readers’ pre-knowledge; the formal reading route has established the identity, level and relationship of each object from real-life problems.
- [ ] The first platform or implementation has independently closed the minimum transaction, and subsequent platforms or generations are launched by new constraints; no difference conclusion is given in advance before the objects on both sides are established.
- [ ] When multiple family or configuration variants exist, common contracts, orthogonal classification axes, and common skeletons are established before the first variant is implemented.
- [ ] A module × variant matrix has been established; the public implementation is only taught once, and each variant only expands the true differences in actors, status, communication, completion conditions and costs.
- [ ] Combining applications, life cycles, diagnostics and selections does not break the necessary pre-chain from public interfaces to classification coordinates; experiments can refer back to specific module conclusions or variant differences.
- [ ] Topics, reader outcomes, background motivations, and applicable boundaries are clear.
- [ ] The reading prerequisites have been clearly stated according to the continuous textbook, independent articles or reference pages; new concepts have received necessary explanations before participating in reasoning, and the established pre-knowledge has received an appropriate amount of review. There is no definition of another word with a string of unknown words, nor mechanical repetition of complete definitions.
- [ ] For the first time, the overall definition of terms is highlighted, and the Chinese name, official English name and applicable abbreviation can be directly compared; no full name is made up for product model or identifier.
- [ ] Next to the key explanations are verified official material catalog entries and reading questions. Norms, implementations, platforms, teaching deductions and experimental observations are not mixed; both broken-link reading and traceable reading are established.
- [ ] The working book blueprint, chapter dependencies, and contracts for each chapter have been completed before the main text; the formal outline only links to real documents.
- [ ] Start by establishing a panoramic view of system location and interaction without getting directly into APIs, registers or source code.
- [ ] Key misunderstandings are deduced through "wrong model → specific contradiction → minimal correction → correct model".
- [ ] Selects the viewing angle required for the current topic and allows each angle to reuse the same set of objects, stages, and events.
- [ ] Key mechanisms give dynamic processes rather than just listing definitions, properties, fields or interfaces.
- [ ] Key actors, state locations, data structures and execution chains can correspond to each other.
- [ ] Syntax, interface or configuration answer the functions, scenarios, error consequences and implementation points.
- [ ] Examples cover normal, failed, cleanup and teardown paths, and code comments comply with repository specifications.
- [ ] Diagrams and tables explain real relationships without heaping structures on quantities or single renderers.
- [ ] Provides executable verification methods, expected results, and fault location directions.
- [ ] Source code conclusions have version, configuration and upstream relative path boundaries.
- [ ] An introduction to the general index and module concepts of `navigation/`, and a clear explanation of the specific implementation responsibilities of `source_explanations/`; the same source code implementation of the same version is only expanded once.
- [ ] The general index links to the introduction of all modules, and each implementation explanation links back to the general index and the introduction of the module it belongs to; the knowledge text also provides two levels of reading entrances and specific implementation title entrances, and Typora fragments can be jumped directly.
- [ ] The promise of the title has been fulfilled in the current document; the main narrative remains intact after all links are broken, and the links do not provide a first explanation of alternative concepts, module responsibilities, state transitions, or implementation principles.
- [ ] Each major module forms a local closed loop of "Concepts and types → Problems → Solutions and status communication → Reader predictions/counterexamples → Implementation or source code verification". The default mainline precedes optimization, diagnosis, version differences and other execution models.
- [ ] Tables, figures, stages, and evidence indexes each answer a different question, without using element stacking or tautology to pretend to be depth of content.
- [ ] Only the scope of typesetting, structural adjustment or content modification is consistent with this user authorization.
- [ ] Titles, Metadata, Links, Mermaid and `git diff --check` have been verified or accurately stated restrictions.

---

> **Language / 语言** · [← 简体中文](repository-topic-requirements.md) · **English (current)**
