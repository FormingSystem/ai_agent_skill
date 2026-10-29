# Thematic design reference

> **Language / 语言** · [← 简体中文](topic-design.md) · **English (current)**

## Contents

- [Confirm reader result](#1-determine-reader-results)
- [Clear term dependencies and expand concepts](#11-clear-terminology-dependencies-and-then-expand-concepts)
- [Let the topic structure itself be built from scratch](#12-let-the-topic-structure-itself-be-built-from-scratch)
- [Independent explanation and official data traceability](#13-independent-explanation-and-official-information-tracing)
- [Subject to this editing permission](#2-obey-this-editing-permission)
- [Perform generation twice](#3-perform-two-passes-of-generation)
- [Determine the classification axis and module variant matrix](#31-determine-the-classification-axis-and-module-variant-matrix)
- [Prepare penetration scene](#4-prepare-to-run-through-the-scene)
- [Select chapter roles according to responsibilities](#5-select-chapter-roles-according-to-responsibilities)
- [Decision to merge and split](#6-decide-on-mergers-and-splits)
- [Create a contract for each chapter](#7-establish-a-contract-for-each-chapter)
- [Continuous Reading and Anti-Formalist Acceptance](#continuous-reading-and-anti-formalist-acceptance)
- [Distinguish between abstract mechanism and concrete implementation](#8-distinguish-between-abstract-mechanism-and-concrete-implementation)
- [Reinforced simple model](#9-reinforce-the-naive-model)
- [Maintain the independence of authoritative topics](#10-keep-authoritative-topics-independent)
- [Let the outline become a learning map](#11-make-the-outline-a-learning-map)
- [Preserve the breakthrough path from the wrong model to the correct model](#12-preserve-the-breakthrough-path-from-the-wrong-model-to-the-right-model)
- [Using multi-view dynamic processes and distinguishing abstraction layers](#13-use-multi-perspective-dynamic-processes-and-differentiate-between-layers-of-abstraction)
- [Adjust the order of explanation according to question type](#14-adjust-the-order-of-explanations-according-to-question-types)
- [Generate in batches but maintain depth](#15-build-in-batches-but-maintain-depth)
- [Acceptance based on transferable mental model](#16-acceptance-with-transferable-mental-models)

## 1. Determine reader results

First, write down the starting point of the reader: what has been mastered, what is missing, and what wrong model is most likely to be brought into the topic. Then write down the results that must be able to be reconstructed or judged after completing the topic. Prioritize issues that require reconstruction of timelines, state machines, communication paths, or ownership relationships:

- Before and after the event, each state belongs to which participant;
- What conditions closed the old user collection;
- Which evidence proves that the operation was completed;
- How a local fact becomes a shared or global fact;
- Who wakes up the waiter, or who performs the delayed action;
- Which cost disappeared from the fast path and where it was moved;
- Under what constraints is the original plan more suitable, and under what constraints can the new mechanism be established.

Refuse to use "understand the main API" or "understand the principles" as topic goals unless they have been broken down into observable, reasonable tasks.

## 1.1. Clear terminology dependencies and then expand concepts

The default reader has the foundation declared by the user, but does not know the topic private vocabulary that has not been established yet. Press SKILL.md first to determine the reading contract for continuous textbooks, independent introductory articles or reference pages. Continuous textbooks clarify the preceding chapters and briefly review key understandings; independent articles complete the premises within the scope of the commitment. "Be engaged in the development of this subsystem" and "have seen the source code" cannot be regarded as implicit prerequisites, nor should the entire introductory process be repeated just because chapters can be opened separately.

Establish a working term dependency ledger during the first design pass:

| Ledger items | Questions that must be answered |
| --- | --- |
| Original writing | How to actually spell the text, source code, configuration or tool? |
| Chinese and English name | What are the abbreviated English Full Name and the exact Chinese name respectively? |
| Nature of the name | Is it an abbreviation, a proper name, a historical nickname, a command, or a source code identifier? Is it made clear when the full name does not exist, rather than making up the etymology? |
| Term Type | Is it a concept, contract, role, state, phase, implementation family, execution model, optimization, diagnostic, configuration, source code symbol, format, artifact, or tool? |
| Simple definition | Without using other slang words in this topic, how can you explain what it is in one or two sentences? |
| Current Responsibilities | What does it receive, read, hold, modify, or output across the scenario, who owns it, and when does it take effect? |
| Prepositional terms | What words must be understood before understanding this word? Are these words already ranked first? |
| Confusing items and boundaries | Who is it most likely to be confused with? What are the classification axis, non-guaranteed matters, version/architecture/Kconfig boundaries? |
| First appearance | Does it first appear in title, text, table, figure, code, configuration or log? Is the access card in the previous or immediately adjacent location? |
| In-depth entry | Where is the complete title of the current text, the precise title anchor of the authoritative topic, or the official information? |

Check the new names in titles, navigation, tables, figures, code, configuration, and logs in the order that the reader actually sees them. When a title raises a question or shows a phenomenon followed by an explanation, it does not mean that the reader has mastered the concept; you cannot use unknown premises in key reasoning and then ask the reader to find the answer a few pages later. When new concepts are formally established, the required names and explanations are given. Continuous textbooks briefly review established concepts when they are later cited. It is not mandatory to repeat the full English name and complete definition in each chapter.

Terms are sorted by dependency. Entries without prepositions or which only rely on common words are explained first, and then derived concepts are introduced layer by layer. If a definition contains words that have not yet been aligned, these prepositions are first recursively completed; "explaining the current term with more terms" is regarded as the term debt not being cleared. Only when the dependencies required for current reasoning in the ledger have been closed, the text enters the classification, comparison, mechanism, source code or configuration matrix.

Each word with reasoning responsibility completes at least the following entry cards:

1. For Chinese and English names and applicable abbreviations, mark the first definition according to the "name and prominence" rules of [Text Terms Access Control](reader_first_writing_en.md#beginner-terminology-acceptance-gate-align-language-first-then-expand-concepts); non-abbreviations indicate the nature of names such as proper names/identifiers, and do not make up full names;
2. The type it belongs to and whether it is on the same category axis as other names in the same table;
3. Homespun definitions that do not rely on topical jargon;
4. The input, output, state ownership, triggering time or usage location of the current scene;
5. What's not guaranteed, miscellaneous items, and version/configuration boundaries;
6. Local explanations for the current chapter are enough to keep reading, as well as precise entry points to click on when you need more depth.

Links and local explanations have different responsibilities: text explanations keep readers connected, and precise links are responsible for depth, edition evidence, or clear preceding chapters. If multiple unfamiliar words appear in a row, the learning stages should be broken down according to knowledge dependence and gradually introduced by specific tasks; do not use a concentrated list of terms at the beginning to retain the original jump. Entry cards are the author's interpretive responsibility and are not a fixed form that readers must read. Only when the object has been established, the classification, panoramic relationship and source code implementation are compared.

Topic-project-specific naming must be additionally explained: who defines the name, whether it refers to a concept or an implementation object/state in the topic, where the state falls and who owns it, and how it relates to the common meaning of the word. Once ordinary English words are given special meanings by the subsystem, they are also treated as proper nouns.

Cold reading checks the stated pre-knowledge: whether the reader can tell what the current object is, what it does here, and use it to explain the phenomenon or predict the result of modification. The new name leads to the continuous question "what is this word again?" indicating that the dependence is still not closed. Abbreviated spellings and precise entries are used for verification, and reciting the full name is not a substitute for understanding. Space pressure is no reason to skip explanations; split learning phases or move in-depth material that is not currently necessary.

## 1.2. Let the topic structure itself be built from scratch

Ground Zero isn’t just about “explaining terms the first time they appear.” The modules, classifications, platforms, architectures, products, implementation families, versions, and generations used by the author to plan the entire book may themselves be knowledge that readers have not yet established. For example, "universal model + vertical implementation of two platforms + comparison of generational differences" can be a working blueprint, but it cannot directly become a publication-type reading entry, because it assumes that readers already know what a platform is, why the two platforms are comparable, and what the implementation family and the standard generation are.

### 1.2.1. Distinguish between author structure and reader structure

- **Author Structure** Answer what modules, platforms and comparison items the material is ultimately divided into, allowing for the use of final classification in advance to help inventory evidence;
- **Reader Structure** Answer the reader's current established concepts as to why a new role, name, or classification needs to be introduced here; only use objects and relationships that have already been explained.

After the design is completed, the author structure must be translated into a reader causal chain. If a certain chapter title, reading stage or comparison table can only be understood when the reader knows the final classification of the topic in advance, continue to add pre-questions, identity positioning or relationship coordinates. Do not use an opening glossary to cover up structural dependencies.

### 1.2.2. Establish identity and relationship for each structural object

Before each module, platform, architecture, product, implementation family, version or generation enters classification and comparison, answer in turn:

1. **What is it:** Is it a concept, specification, hardware implementation, chip integration, board-level product, software module, configuration or version label?
2. **Why it exists:** Which real-world problem, scale, capability, or gap in legacy solutions requires it;
3. **Where is it located:** What is the upstream input, downstream output, owner, and position within a complete transaction;
4. **Who it is composed with:** Which objects contain it, implement it, describe it, call it or be driven by it;
5. **Who is it different from:** Whether adjacent names are in the same classification axis, and the difference is based on responsibility, hierarchy, implementation, configuration or time evolution;
6. **How it is observed:** By which specification, source code, configuration, logs, registers, experiments or physical identification.

For hardware platform question types, first establish relationship coordinates similar to the following as needed:

```text
specification or instruction set architecture
→ Processor core, controller or protocol implementation
→ Integrated within SoC
→ Development board external connection
→ Firmware configuration
→ Operating system framework and device driver
→ User observable behavior
```

This is not a fixed hardware catalog, but an identity chain that prevents cross-layer mixing. The specific topic must replace the abstract node with the current object and explain "who defines whom, who implements whom, who contains whom, who configures whom, and who drives whom". The software topic also uses the same principle to establish the relationship of "contract → framework → implementation → configuration → caller → running result" instead of directly giving a list of implementation families.

### 1.2.3. Establish independently first, then compare the differences

The first platform or implementation is used to formalize the abstract model into a complete set of identities and transactions, not just as a column in a lookup table. The second platform or next-generation implementation should be led by specific gaps in the previous model that arise at new scales, new capabilities, or new constraints. The comparison is only established after the objects on both sides have completed "what, why, where, who is connected to and how to operate".

Generations cannot be explained by version number ordering. It must first explain what the old generation has solved, then show how the new condition limits a certain module of the old generation, and then indicate which part of the participants, status, communication, completion conditions or costs the new generation has changed; and finally form a merged list. Platform differences cannot only list chip parameters, but also distinguish what comes from specifications, processor implementation, SoC integration, board-level connections, firmware configuration, operating system implementation and running configuration.

Causal deduction explains why responsibilities are useful. It does not prove that a certain product division is the only feasible design, nor does it automatically prove the manufacturer's design motivation at that time. Distinguish between "this responsibility is required to meet constraints", "this product chooses this carrier" and "historical data clearly records this reason"; the latter two are supported by implementation data and historical evidence respectively. Alternative platforms can reflect different trade-offs without first writing off the previous platform as wrong or obsolete.

### 1.2.4. Zero-based reading generation chain

For topics with multi-modules, multi-platforms or multi-generations, the combined goals will be rewritten by default as:

```text
real events or tasks
→ Simple solutions and their value
→ Specific questions that current solutions cannot answer
→ Only introduce new roles or modules that are needed to solve the problem
→ Name new objects and establish identities, hierarchies and relationships
→ Close a minimum transaction
→ Map to the first specific platform or implementation
→ Expose gaps with new scale, new capabilities, or new constraints
→ Launch follow-up platforms and realize family or intergenerational
→ Perform coaxial comparison of objects that have been created separately
→ Back to Applications, Deployments, Diagnostics and Selection
```

This chain constrains the sequence of revelations and does not require that they become mechanically eponymous chapters. The acceptance question is: when the reader first sees the classification or comparison, can he tell without guessing what each object is, which layer it is on, who it is connected to, why the comparison is needed at this time, and which axis the difference comes from.

## 1.3. Independent explanation and official information tracing

When designing a special topic, you must read [Independent Explanation and Official Data Traceability](official_source_reading_en.md) in its entirety, and include the official evidence, external charts and register reference information required for key explanations into the design ledger. This reference stipulates the document identity, proximity positioning, fact boundaries and local presentation; the writing and delivery of the text still must be through disconnected reading and traceability reading respectively, and you cannot wait for the completion of the text to just supplement the reference list.

## 2. Obey this editing permission

First press "Confirm editing authorization first" of `SKILL.md` to select typesetting only, structural adjustment to retain content, or content modification/rewriting mode. This reference only determines how to design the topic and does not extend the authority to modify the text.

Document the work tree and reviewed materials at the beginning of the task. Only when typesetting, only the responsibilities and dependencies of existing chapters are shown; when the structure is adjusted, the inventoried content is completely moved; when the content is modified, supplementary deductions, model corrections, or text rewriting are allowed.

## 3. Perform two passes of generation

When creating, expanding, or rewriting a topic, design first and then write.

The first step is to establish a special design account book:

| Design items | Content |
| --- | --- |
| Reader's starting point | Prior knowledge, task context and most likely error model |
| Reader results | The process, proof, or choice that ultimately leads to reconstruction |
| Term dependency | Chinese and English names, types, dependency order, first occurrence and precise entry of private words in this topic |
| Structural dependencies | Which modules, platforms, architectures, families or generations have been preset by the author; how are they first independently established and then classified and compared |
| Panoramic positioning | The hierarchy of the topic in the system, upstream and downstream modules and input and output |
| Throughout the scenario | Realistic load, scale, actors and shared objects |
| Old plan | Already guaranteed, actual value and scope of application |
| Fault Chain | Sequential steps from triggering condition to error or stall |
| Error model | Why it seems to be true, which counterexample causes the contradiction, and what minimum correction is needed |
| Obligation of Proof | Safety, Liveness, Sequence, Lifetime or Isolation |
| Execution model | Configurations and contexts that change actor definitions, state locations, or proof methods |
| State axis | Single state machine or multiple sets of orthogonal states |
| Observation Perspective | Necessary collection of concepts, states, timing, callers, source code, hardware or engineering perspectives |
| Engineering Constraints | Resource, Build, Deployment, Recovery, Observation, and Platform Limitations |
| Evidence plan | The destination location of stable knowledge, version source code, experiments and platform evidence; the official document identity, directory location and issues to be checked corresponding to key concepts |

Then select chapter roles, draw **complete** dependencies, and create contracts for each chapter. Only after the second time do I write the text according to the dependency diagram. Don't generate a lot of chapters first and then work backwards to figure out why they exist.

The typesetting task alone does not re-establish the technical model; the first pass is changed to a content ledger, mapping existing information units to reading stages and destinations.

## 3.1. Determine the classification axis and module variant matrix

When a topic has both public semantics or public APIs, as well as multiple implementation families, configuration branches, or execution models, you cannot just draw the chapter causal chain, but also draw the **category axis and module variant matrix** first. Otherwise, it is easy to talk about a certain configuration as a complete topic vertically, and then repeat the common modules in another configuration.

The classification axis must precede the variant internal implementation, but must precede the concept, object identity, and relational coordinates that make up the axis. The author can draw the final matrix in advance in the working ledger; the text cannot directly display the matrix when the reader does not yet know what the columns are and why they are comparable. First derive the responsibilities or constraints that may change from real-life problems, and then name the classification axes and variants.

First put the names back on their respective orthogonal axes:

| Category axis | Questions answered | Common misalignments |
| --- | --- | --- |
| Public contracts/APIs | What callers can rely on across implementations | Wrote internal optimizations into API semantics |
| Guard domains or semantic flavors | Which actors and objects belong to the same wait domain | Aligned as a "type" with the underlying implementation family |
| Implement the family | Which set of core algorithms and data structures honor the contract | Replace the family definition with a local directory name |
| Execution model | How conditions such as preemption, migration, blocking, interruption, etc. change participants or proofs | Replicate the complete system for changing the configuration of only one module |
| Run strategy or optimization | How to change the cost or notification path of normal/accelerated, unloading, batch processing, etc. | Interrupt the default main line in advance |
| Diagnostic facilities | How to observe or inspect functional paths | Write inspector status as functional status |

Classification results must be implemented within the first variant before entering the formal reading route. Then create a matrix with functional modules as rows:

| Module | Public concepts and inputs and outputs | Public implementation | Variant A delta | Variant B delta | Evidence | Experiment |
| --- | --- | --- | --- | --- | --- | --- |
| A responsibility that can be learned independently | Why it exists, what it receives, what it outputs | Roles and status shared across variants | Only changes are recorded | Only changes are recorded | Source code/specification | Corresponding certification obligations |

The default reading order proceeds line by line: module concepts and common responsibilities are covered first, followed by a side-by-side comparison of variants. Only if a variant changes most of the end-to-end participant set, proof method, control flow and completion conditions, a separate vertical article is necessary. If the same common executors, data structures, and complete timings appear repeatedly in two variant chapters, you should return to the matrix and re-determine the main axis, rather than relying on "see above for details" to maintain two empty chapters.

Composite applications, object life cycles, diagnostics and selections must not interrupt necessary dependencies on public interfaces and classification coordinates. Experiments used to establish current understanding in continuous textbooks are carried out locally in the text of the corresponding unit; comprehensive exercises can be arranged at the end, and independent experiment articles can have another entrance, but the centralized experiment catalog cannot replace the current steps. Each experiment should correspond to a clear module conclusion or variation difference, allowing readers to explain "which condition to change, which state to observe, and which proof to support."

## 4. Prepare to run through the scene

When comparing different designs, reuse the same scenario as much as possible:

| Project | Required Content |
| --- | --- |
| Load | Read and write frequency, number of CPUs, latency, memory, sleep and teardown constraints |
| Actors | Named tasks, CPUs, interrupts, callbacks, devices and data structures |
| Protected object | Formal entry, shared state, object or hardware transaction |
| Existing design | What guarantees it provides, and why it is currently correct |
| Fault Chain | Orderly steps from triggering condition to error observation, race, UAF, stall or leak |
| Required guarantees | Security, sequence, lifecycle, progressivity, or isolation properties |
| Evidence | Required source code versions, configurations, traces, experiments, or benchmarks |

First give the specific scenario and necessary code, and then derive the abstract role from the constraints. The code here is used to fix the problem site; the full API template can appear after the abstract contract is established.

## 5. Select chapter roles according to responsibilities

The local RCU topic provides the following reusable responsibilities instead of a fixed number or fixed number:

| Chapter Role | Problem Solved | Conditions of Use |
| --- | --- | --- |
| Problem pressure | What did the old solution solve and how did the gap gradually form | All topics |
| Abstract mechanism | How to derive roles, boundaries and proof obligations from constraints without relying on target system fields | When the mechanism cannot be defined solely by API |
| Minimum usage closed loop | How abstract actions correspond to interfaces, normal paths, failure paths, and teardowns | When there is a public API or calling protocol |
| Composition and life cycle | How multiple independent mechanisms are handed over by the module to which the object belongs | When references, callbacks, work queues or composite allocations are involved |
| Perform model proof | Why security holds true in a certain configuration or context | When different models have different sets of participants or proof methods |
| Source code implementation mapping | Prove how the model is implemented as fields, write paths, read paths and completion conditions | When versioned implementation evidence is required |
| Realistic condition reinforcement | Which preemption, migration, interruption, offline, out-of-order or delay conditions break down the naive model | When real operating conditions will change the model |
| Unified state and communication panorama | How multiple sets of states and multiple communication paths complete an operation cycle | Distributed or hierarchical mechanism |
| Sub-state machine depth | How to advance the key modules independently in the unified panorama | When a single general diagram is not enough to explain the implementation |
| Implementation families and configurations | Which guarantees, actors, and costs change with different variants | When alternative implementations exist |
| Application, diagnosis and selection | How to combine correctly, observe faults and choose alternatives | The end of all complete topics |

After the abstract contract is established, the minimum correct usage should be implemented earlier than the large section, so that subsequent source code discussions have a specific focus.

## 6. Decide on mergers and splits

**Hard length constraint: Markdown documents must not exceed 10,000 words unless necessary.** According to the unified caliber statistics of `SKILL.md`, if it exceeds the boundary, it will be reviewed whether there is a complete and independent learning problem boundary. Complete experimental instructions, necessary long codes, continuous operation cycles and derivation, as well as situations where they are only slightly exceeded and splitting will produce short tails, can be retained and recorded with specific reasons; there will be no mechanical card count, and no separate article-by-article review and approval. If it is obviously too long and contains multiple independent issues, it must be split. The original tables, figures, examples and necessary derivation must be completely migrated and cannot be compressed into a summary to pass the line; the numbering, navigation, precise anchor points, review maps and other real callers involved in the split must be synchronized, and "too much information" must not be exempted from review.

Chapter roles can be combined or omitted:

- When there is only a simple execution model, the proof and source-code mapping can be the same;
- When there is no cross-mechanism ownership, combination and life cycle chapters are not created;
- When the status is not hierarchical and the communication path is simple, it is not mandatory to establish a unified general diagram;
- Variant chapters are not created for aligned RCU when no family is implemented;
- When one sub-state machine is not enough for independent learning, it is reserved in the unified implementation chapter;
- When an article simultaneously bears two sets of independent proofs, two complete life cycles or multiple configuration models and affects continuous reading, it should be split even if it does not reach the length threshold.
- When multiple variants share most of the end-to-end modules, merge the common implementations based on the modules and compare the differences; the entire implementation chain must not be copied just because the Kconfig name is different.

The number of documents is determined by proof boundaries and reading continuity, not by the number of RCU chapters, seven-paragraph history, or eight-step method.

## 7. Establish a contract for each chapter

Record for each chapter before writing the main text:

| Contract items | Contents that must be clear |
| --- | --- |
| Preliminary conclusion | This chapter allows assumptions about what the reader already knows |
| Preposition of terms | Which proper nouns are used for the first time in this chapter, how to complete the entry card before use, and define whether the dependency has been closed |
| Questions in this chapter | Which main problem does this chapter only solve |
| Why now | What questions arise naturally from the previous chapter that make this chapter a necessary step now |
| Throughout the scene | Which objects, actors, and time boundaries continue to be reused |
| Wrong model or counterexample | What misconceptions will be dispelled in this chapter, or what conditions will be used to test the current model |
| New model | Which roles, states, constraints or communication paths are added |
| Output conclusion | What can be proved after the end of this chapter |
| Evidence | What is supported by specifications, code, source code, configuration, diagrams, traces or experiments; when official comparison is required, what are the nearest entrances and reading issues |
| Follow-up Gap | Which question is intentionally left to the next chapter |

The chapter contract is not an additional document that must be submitted; priority will be given to writing the streamlined results into the reading map of `大纲.md`.

Chapters are connected by open issues, not just by file numbers. The beginning of each chapter recycles the output of the previous chapter and exposes a new gap; the main text only introduces the model increments required to solve the gap at a time; the end makes clear the new conclusions of this chapter and the evidence that has yet to be realized in the next chapter. Do not force the API chapter, source code chapter, and diagnostics chapter to use the same section template for the sake of uniformity.

This contract must also be implemented down to the smallest detail. Follow [Explanation on Writing Section 8.1](explanation-quality_en.md#81-the-text-between-the-titles-must-be-connected) to check each scene or perspective change. Do not use titles to replace the main text, or use the background at the beginning of the chapter as evidence that the entire chapter has been continuous.

## Continuous Reading and Anti-Formalist Acceptance

After establishing the chapter contract and before starting the main text, you must read [Continuous Reading and Anti-Formalism Acceptance](reader_continuity_review_en.md) in full, and use title contract, broken link reading, module closed loop and representation increment to check whether the design is reasonable. Recheck the title and the actual link after the text is rewritten or the responsibilities change; perform a independent reading review and retelling before delivery. Structural audits can only assist these judgments and cannot replace any of them.

## 8. Distinguish between abstract mechanism and concrete implementation

Abstract chapters derive necessary roles, responsibilities, states, and inputs and outputs, using the terminology of the current specification or contract, without preemptively replacing concepts with physical blocks of a product or Linux fields. First, fix how logical objects are counted and what state each object should maintain independently.

When entering the implementation chapter, first follow [Concept to Implementation Mapping and Input and Output](concept_implementation_mapping_en.md) to establish the corresponding relationship between the standard role and the actual module, field, register, and execution path, and then start a specific run. The mapping must be entered into the text before the first use of the implementation term inference, and cannot be left to the end of the chapter or in external links. The existence of a certain field in the source code does not constitute a reason for the existence of abstract responsibilities; the architecture requires each object to have a function, nor does it constitute evidence of independent physical partitioning of each object.

When the proof methods of the main execution models are indeed different, first create proofs separately, and then map the source codes separately; when only the fields are different but the proofs are the same, put them into the same implementation chapter for comparison, and do not mechanically split the chapters into pairs.

## 9. Reinforce the naive model

Select applicable counterexamples from [mechanism-reasoning.md](mechanism-reasoning_en.md) to check for future actors, preemptive migrations, asynchronous propagation, overlapping rounds, interrupting offline, object escapes, memory reordering, and teardown races.

Every time a gap is discovered, a state, a communication path, a constraint, or an explicit unsupported scenario must be added. When the counterexample does not change the model, indicate which existing invariant it is covered by.

## 10. Keep authoritative topics independent

When a mechanism relies on cache coherence, memory orderinging, atomic operations, scheduling, krefs, or other reusable mechanisms:

- Save the complete general tutorial in its own authoritative location;
- Keep the dependency and its failure consequences in the current scenario;
- Add links where the prerequisite knowledge is actually used;
- Avoid creating micro-"extended concepts" that cannot stand on their own as research topics;
- Make sure that the linked authoritative topics have their own scenarios, derivations, evidence, and experiments where applicable.

## 11. Make the outline a learning map

The outline first draws a chapter dependency diagram, and then explains each chapter:

- preliminary conclusion;
- Issues addressed in this chapter;
- New roles, statuses or certifications;
- Hand over to the open questions of the next chapter.

The working blueprint must plan a complete chain of chapters; the formal outline of the repository only links to real documents, does not copy the explanations of each chapter, and does not list unimplemented imaginary chapters as completed content. When generated in batches, the formal outline, forward and backward navigation, and open questions are updated every time a chapter is completed. As the reader follows the default order, he should be able to see how the model is gradually refined by questions and counterexamples.

## 12. Preserve the breakthrough path from the wrong model to the right model

For key mechanisms that are easy to misunderstand, do not announce the answer directly, but proceed in the following closed loop:

```text
Why the error model seems to hold true
→ Fixed participants, status positions and chronological order
→ Use specific counterexamples to deduce contradictions
→ Only add the states, roles, communications or constraints required to resolve this round of conflicts
→ Reinterpret the original scene with the correct model
→ Describe conditions that are still not covered
```

Merely listing "common misunderstandings" without showing how they lead to contradictions does not constitute a breakthrough in understanding. Counterexamples must change the model, or explicitly override an existing invariant.

## 13. Use multi-perspective dynamic processes and differentiate between layers of abstraction

Select concepts, data structures, state machines, time/timing, CPU/threads/interrupts, callers, source code, hardware and engineering deployment perspectives by topic, without mechanically adding them together. All perspectives reuse the same set of key objects, stages, and events, explicitly illustrating inter-layer mapping:

```text
definition ≠ implementation
API contract ≠ internal algorithm
Logical state ≠ specific field or register
Software synchronization ≠ hardware cache consistency or memory ordering
Protocol guarantee ≠ controller or platform capabilities
Stable model ≠ source code organization of a certain version
```

Key conclusions show at least one complete cycle: pre-transition state, triggering actions, intermediate propagation, completion conditions, post-transition state, and failed branches. Diagrams are used for roles, states, timing, Before/After, hierarchies, data flows, and life cycles; arrows mark actions or state flows, and text explains key transitions. Mermaid uses `<br/>` for newlines and does not use `\n`.

First use the mechanism to explain why it is true, and then use specifications, source code, experiments, logs, traces, waveforms or benchmarks to prove how the current implementation performs. Mark inferences and boundaries when the evidence is insufficient, and do not use "probably so" to complete it.

## 14. Adjust the order of explanations according to question types

| Question type | Priority order of cognition |
| --- | --- |
| Data Structures, Algorithms and APIs | Usage Issues → Minimum Correct Usage → Common Operations and Failure Cleanup → Internal Structure and Dynamic Algorithms → Implementation Evidence → Complexity, Boundaries and Choices |
| Hardware, chips and protocols | System location and conceptual responsibilities → Implement module, status and interface mapping → One complete transaction → Signals and timing → Register and controller status → Driver mapping → Board-level constraints |
| Kernel mechanism and concurrency | Problem pressure → Abstract proof → Real condition reinforcement → State and communication closed loop → Source code evidence → Application selection |
| Engineering Systems | Goals and Environment → Resource Budget → Build and Image or Deployment Layout → Startup and Run Process → Failure Recovery → Observable Verification |

The original order of the data is only used as a query entry and does not directly serve as a learning order. Data structure/API questions first solve "how to use it correctly" after the minimum contract is established; engineering questions must include resource, construction, deployment, recovery and observation constraints.

## 15. Build in batches but maintain depth

Long topics can be written in batches, but first freeze the complete working blueprint and contract for each chapter. With complete chapters or complete subsections as batch boundaries, each batch recovers preconclusions and records the conclusions that have been fulfilled, open questions and the next batch of evidence. Subsequent batches continue to satisfy the same causality, dynamic processes, and evidence gating and do not become abstracts due to context growth.

Space pressure is no reason to delete the "why", failure chains, critical state transitions, failure cleanup, or boundary conditions. When evidence overturns the blueprint, explicitly revise the outline and affected chapters.

## 16. Acceptance with transferable mental models

The completion standard is not length, knowledge points, source code or number of diagrams, but whether the reader can:

- Draw the location of the subject in the system, key objects and the complete dynamic process;
- Gradually derive gaps from the guarantees of the old scheme and test faulty models with counterexamples;
- Distinguish between abstract guarantees, API contracts, current implementation, and platform boundaries;
- Continue derivation under new loads, configurations, or failure conditions not directly covered;
- Select the original solution, current mechanism or alternative solution according to constraints;
- Describe what source code, experimental or observational evidence is needed to confirm the inference.

Whether the final acceptance definition is clear, whether the causal chain is closed, whether the model is self-consistent, whether the dynamic process is complete, whether the hierarchical mapping is clear, whether the boundaries are operable, and whether the model supports continued reasoning.

---

> **Language / 语言** · [← 简体中文](topic-design.md) · **English (current)**
