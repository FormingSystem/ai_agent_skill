# Kernel source code evidence reference

[简体中文](source-evidence.md) | **English**

## 1. Establish a baseline

Obtain the source tree location according to the current repository instructions and check:

```text
Top-level Makefile version
target architecture
Related .config configuration items
Common implementation directory
Architecture-specific implementation catalog
Vendor/BSP Boundary
```

At the same time, the official repository identity and immutable commits are recorded, distinguishing the current working tree HEAD, fixed commits for verification, generated configurations, and actual running images. It must be clear whether the source code belongs to the upstream, stable version, manufacturer version or local patch version; the actual running configuration must not be inferred just because a certain branch exists or the top-level Makefile defaults to a certain architecture. When using fixed commit forensics because the current HEAD is different, state in the record that you cannot mix working tree contents with old commit identities.

## 2. Search by status transition

You must not search only API definitions. For each S phase, trace:

1. field declaration;
2. initialize;
3. each writer;
4. Each reader that changes control flow;
5. caller and callee chain;
6. Lock, IRQ, preemption, task, CPU or process context requirements;
7. Wake-up, callback, IPI, polling or hierarchical propagation;
8. Cleanup and error paths.

Priority is given to `rg`. Search for the exact field name and assignment location first, then read enough context to determine branching and ownership.

## 3. Establish an evidence matrix

Each important conclusion is documented:

| Conclusion | Version/Configuration | Path | Function/Field | Writer | Reader | Sequence/Lock | Meaning |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Local debt occurs | Exact configuration item | Upstream relative path | Exact field | Execution context | Subsequent path | Required constraints | What this status bit proves |
| Report local debt | Precise configuration items | Path | Function chain | Reporter | Aggregator | Lock/barrier | Communication direction |
| Achieve global completion | Precise configuration items | Path | Sequence number/waiting field | Coordinator | Waiter | Wake-up condition | Why it is safe to continue |

Tables should not be allowed to replace causal explanations or end-to-end timing.

Establish a four-layer evidence chain for the conclusion that bears the key derivation:

1. **Abstract invariants:** Causal or protocol guarantees that hold regardless of concrete versions;
2. **Source code placement:** The fields, write paths, read paths and completion conditions that carry this guarantee in the current version;
3. **Boundary tags:** Clarify API contracts, common implementations, configuration branches, architecture or vendor boundaries;
4. **Observable evidence:** Traces, logs, experiments, indicators, or failures that support or refute the conclusion.

The text can use short tags or evidence tables to express these four layers, but "find the source code field" cannot be directly regarded as an abstract conclusion that has been proven.

### 3.1\_Establish source code symbol coverage ledger

Before entering into the specific implementation explanation, first take stock of the source code excerpts, call chains and symbols in the diagram that will affect the control flow, status, synchronization, configuration or life cycle of this chapter. First determine **implementation ownership**: the data structures, algorithms and queries of the general framework are uniquely developed in the framework topic; the subsystem topic is responsible for its own instances, initialization parameters, event access, call timing, configuration degradation and consumption scenarios, and accurately links the framework implementation.

The coverage ledger contains at least: declaration, definition, initialization, writer, reader, state before and after calling, configuration switch, error or rollback path, life cycle, authoritative explanation title and modification impact area. Use **no unexplained symbols** access control: key structures, fields, global objects, static keys, macros, functions and parameters cannot appear only in code blocks. When the current title is not expanded, it must be accurately linked to the existing title; when it is indeed a mechanical statement or cut content irrelevant to the current conclusion, the omission boundaries and reasons must be marked.

In particular, an object must not be omitted because it belongs to the inspection path. The inspector shadow state also needs to account for declarations, identities, event pairings, query consumption, and closing configuration branches, but it cannot be written as a functional state.

It is recommended to use the following ledgers:

| Symbol or implementation cluster | Ownership | Declaration/definition | Initialization and lifetime | Write/register | Read/consume | Configuration branch | Status category | Modification impact | Authoritative title |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Exact name | Framework/subsystem | Upstream relative path | Static/Startup/First use | Call point and before and after state | Query point and control flow consequences | Turn on/off expansion | Function/current shadow/history/life state | Required caller and test | Full title anchor |

The ledger serves the purpose of evidence collection and review, and is not required to be submitted as is; the text can be split into source code indexes, status tables, diagrams and modifiable lists, but the facts corresponding to any column cannot be lost.

## 4. Establish module concept introduction and unique implementation explanation

When the same source code topic has both reading navigation and source code explanation, the following directory of responsibilities is adopted:

```text
research/source_reading/<topic>/
├── navigation/ # General index, and source code concept introduction of sub-functions/modules
└── source_explanations/ # Explanation of the unique source code implementation of specific macros, functions and fields
```

`navigation/` is more than just a list of links: it contains a general reading index, as well as introductions to source code concepts organized by sub-functions or modules. The module introduction borrows the source code to answer "What problem does this module solve, what participants and states are there, how the call chain is closed, and in what order it should be read." You can use application examples, pseudocode, tables, and Mermaid, but do not expand the upstream macro body or function body piece by piece. `source_explanations/` is oriented to specific implementations, saving precise versions of macros, functions, fields and configuration branches, and restoring the code piece by piece using Chinese Doxygen comments, Chinese inline comments and implementation principle explanations. The former is to understand the module by borrowing source code, and the latter is to understand the implementation function by function.

When a module has multiple configurations or execution models, the module introduction first talks about common responsibilities and shared call skeletons, and then explains the status, branches, and completion conditions of each variant in parallel. A set of navigation chains containing the same common modules must not be duplicated for each configuration; independent vertical module navigation should be established only if the variant replaces most of the actors, the proof domain, and the complete control flow.

The same version and the same source code implementation are only expanded under the authoritative title of `source_explanations/`. The general index links to the module introduction. When the module introduction encounters a specific implementation, it links to the title accurately. The knowledge text also leads the reader to the general index, related module introduction and the implementation title directly encountered in this scenario.

### 4.1\_Links can only serve as evidence and cannot replace explanations.

The only expansion restriction of the source code is **the same version of the function body, macro body and sentence-by-sentence implementation instructions**. It does not prohibit the knowledge text and module introduction from explaining concepts, responsibilities, status changes and causal relationships in the current scenario. The "Avoid duplication of source code" error must not be implemented as "Keep only links in the current chapter".

All continuations using versioned source code must pass the following checks:

1. **Local explanation first:** Before the link appears, the text has already explained what type the current symbol belongs to, what problem it solves, what its input and output are, what states it modifies, and what guarantees it cannot provide.
2. **Testify after the link:** The precise title link is used to view the unique function body, configuration branch, complete field domain or modified boundary; readers can understand why the current module exists and how to advance the main line without clicking the link.
3. **No links dominate the opening:** The file list, source code baseline, general index, module introduction and implementation title must not appear before the reader's entrance. At the beginning, the scene, remaining questions, and testable results after reading are fixed, and then the entrance is given where evidence is actually needed.
4. **Source code title fulfillment:** If the title promises "source code implementation, source code explanation, source code mechanism", the current chapter must provide implementation principles and local source code evidence module by module. Only navigation and jump must be renamed to "Index, Navigation, Evidence Entry"; only accurate titles such as "Implementation Model, Status and Communication" should be used when cross-version stable mapping occurs.
5. **Types are hierarchical first:** Before entering the call chain, separate abstract concepts, request objects, execution contexts, state carriers, configuration variants, optimization branches and diagnostic facilities. They cannot be listed as a set of source code nouns at the same time.
6. **Publication broken link test:** Assuming that the publication hides the URL, the reader does not leave the current page, and the concepts, problems, solutions, module collaboration and completion conditions are still continuously established. Missing link targets only reduce in-depth evidence and do not fracture the main narrative.

If the knowledge text requires a short piece of source code to confirm the status, you can use a short excerpt or faithful pseudocode that is sufficient to support the current conclusion, and clarify its evidence boundaries; the complete function body, sentence-by-sentence Chinese comments, and modifiable instructions are still only saved in `source_explanations/`. The so-called unique expansion cannot be a reason to omit the explanation of the current scene.

### 4.2\_Full information synchronization matrix

"Full information synchronization" synchronizes discovery portals, fact boundaries, and implementation ownership, rather than synchronizing the full text of documents with different responsibilities. Check item by item:

| Hierarchy | Closed loops that must be checked |
| --- | --- |
| Stable text | Topic outline, parent outline, previous/next article, adjacent mechanism boundaries |
| Source code navigation | The total reading index enumerates all module introductions; the precise link of module introductions realizes the title |
| Implementation explanation | General index of related entrance backlinks, introduction to the corresponding modules, knowledge scenarios and cross-topics |
| Evidence identity | `SOURCE_BASELINE.md` Register version, configure boundaries, save files and read entrance |
| Full repository discovery | Stable text and total reading index can be found on Atlas maps, routes, content indexes and repository homepages |
| Orchestration caller | Only update the real existing publication list, Obsidian, Canvas/Base and other inbound links; do not create placeholder files if they do not exist |

Each layer first determines the task that the reader wants to complete, and then decides whether to link to the file entry or the specific title. When the source code baseline, Atlas, and repository homepage belong to the navigation entry, the complete title anchor is also given priority to prevent readers from searching again after falling to the top of the file.

When the knowledge chapter contains demonstration code, first create an interface list near the code:

| Interface or checkpoint | Function of this scenario | Calling context | Consequences of omission or misuse | Versioned source code explanation |
| --- | --- | --- | --- | --- |
| Public API | Which state transition step is completed | Process/IRQ/lock/preemption constraints | Which guarantee is broken | `source_explanations/PXX_源码讲解.md#N.N_接口标题` |
| Debug checkpoints | Which call statement to check | Required Kconfig and checker state | False negative, misused, or overridden boundaries | `source_explanations/PXX_源码讲解.md#N.N_检查标题` |

When the knowledge text enters the versioned source code evidence for the first time, it links to the total reading index in `navigation/`, and then links to the relevant module introduction; when encountering a specific interface, it directly links to the unique source code implementation title. The source code implementation explanation is organized in the following order:

1. Use the associated entry table to link back to the total reading index, the introduction to the module to which it belongs, the knowledge scenario and the call chain that requires the interface;
2. Give the implementation index of a specific macro, function or field, and link the name to the corresponding title of the current implementation file; under this title, link the upstream relative source code file saved in the repository;
3. Cut out the original implementation that is sufficient to support the conclusion without changing the source code semantics, clearly mark the omitted intervals, and add Chinese Doxygen comments and Chinese inline comments of "repository supplement, non-upstream original text";
4. A single column of "Implementation Principles", describing the state before and after execution, caller/callee, execution context, lock/preemption/interrupt constraints, error path, configuration branch and state side effects;
5. Separate functional mechanisms and inspection mechanisms, and explain the expansion, static or dynamic attributes, and uncovered paths after inspection is turned on/off;
6. The backlink stabilization mechanism, diagnosis, experiments and topic outlines will not be copied from other source code documents.

Each implementation cluster also provides a **Modability Statement** after the "Implementation Principle": indicating the current invariants, the minimum safe modification surface, entry/exit or success/rollback actions that must remain paired, affected Kconfig branches, callers and verification methods. Provide at least one specific object/state address relationship diagram and one specific function end-to-end timing diagram; if you reuse the existing diagram of the upper-level implementation cluster, you must accurately link and explain which arrow the current symbol falls on. When readers can only retell the call chain but cannot predict the impact of local modifications, they cannot judge that the source code explanation is complete.

Functional paths include truly changing state or establishing guaranteed locks, atomic operations, memory orderinging, state machines, notifications, GPs, and callbacks. Check paths include Sparse, Lockdep, debug objects, KASAN/KCSAN, assertions and alerts. Check macros, even if embedded within a public API, must not be written as algorithms themselves; turning off checks usually only removes diagnostics and does not automatically cancel the API contract.

First check whether `source_explanations/` already has an authoritative title of the same version, same macro, function or field. If the title already exists, only the incoming links and necessary association entries will be added; if there is no title, the existing explanation document will be supplemented according to the implementation relevance, and a new document will be created only when the version boundary, implementation cluster or calling context can be independently established. New issues at the module level enter `navigation/`’s module concept introduction. Module summary and function-by-function implementation must not be mixed into the same file, nor must an unmaintainable source code micro-topic be created for each interface.

Chapter links for Typora must include the file path and the full title fragment, not just `PXX_源码讲解.md`. The fragment is written according to the title rendering result: `\_` in the title source code is written as `_` in the link fragment. Interface headers avoid symbols such as parentheses that would truncate Markdown link targets; structural audits must verify both target files and target headers. After moving the directory, the old path will be cleared across the repository and no compatible copies will be retained.

## 5. Classify each conclusion

- **API Contract:** Guarantees that callers can rely on across implementations.
- **Generic Implementation:** The current kernel design in upstream public code.
- **Configuration branch:** Only true under the described Kconfig selection.
- **Architecture implementation:** Depends on the specific architecture path and cannot be extrapolated.
- **Vendor/BSP Behavior:** Binds confirmed vendor submissions, configurations and actual platforms, local directory names cannot be used as this boundary.
- **Inference:** Derived from multiple source code facts but not directly stated by the source code; must be clearly marked as an inference.

## 6. Compare versions where changes occurred

When comparing older kernels, check:

- status location, not just field spelling;
- Reader definition and Kconfig selection;
- Function body and calling path;
- How completion/awakening is delivered;
- contextual tracking or architectural integration;
- Callback execution context.

Only after checking both versions at the same time can we write a conclusion such as "Prove that the skeleton remains stable, but the state X moved from A to B." Link or save accurate legacy source code evidence.

## 7. Preserve evidence but do not create source code forks

Only when the repository uses source code snapshots as long-term evidence, the selected upstream relative files will be saved to `research/source_reading/linux/`, and the version and source will be recorded. The saved copy must be hashed against the declared source tree.

Knowledge curation tasks must not edit, format, or commit external source trees, nor modify their Git configuration.

## 8. Check for common errors

The following source code writing errors are rejected:

- Because a certain function exists, it is asserted that the current configuration must call it;
- Treat old kernel field names as current implementation;
- Compress asynchronous local to global windows into one call;
- Describe business writers as directly performing grace period coordination;
- Describe timeouts, forced paths, or stall detectors as permissions that can violate security;
- Explain task-level debt in terms of CPU-level state, or vice versa;
- Describe implementation optimization as the only semantics of the API;
- Copies line numbers without recording version and file context.
- The complete source code with version is piled at the end of the knowledge text, but there is no independent source code appendix and two-way navigation;
- Only interpret the function macro body and miss the check branch embedded in it, or mistakenly write the check branch as a functional guarantee;
- Since there are no warnings from a dynamic check, it is asserted that unexecuted paths and future interleaving have been proven.

## 9. Additional evidence for dynamic validators

When the topic involves Lockdep, KCSAN, debug objects, sanitizers, assertions, or other runtime checkers, read [lockdep-case-study.md](lockdep-case-study_en.md), and additionally build:

1. The true functional state of the mechanism being examined and who wrote it;
2. The current shadow state maintained by the inspector;
3. Type, dependency, call or alert history accumulated across time;
4. Checker enablement, recursion suppression, capacity exhaustion, and outage status;
5. Check the precise sequence of events relative to function attempt, success, failure, cancellation and release;
6. There is no configuration, checker validity, event access, and path coverage on which the alarm conclusion depends.

When the same checker is reused by multiple subsystems, the checker core status and query implementation are uniquely expanded in the checker source code topic; the subsystem only expands its own virtual identity, adaptation macros and calling conditions, and uses Typora precise title anchor links in both directions.
