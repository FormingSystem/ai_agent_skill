# Source code reading organization and implementation explanation

[简体中文](source_documentation_workflow.md) | **English**

When using versioned source code evidence in the body of knowledge, or when creating, modifying, organizing, or reviewing source code concept introductions and implementation explanations for tasks, you must read this document in its entirety and execute the [Source Code Evidence Specification](source-evidence_en.md) at the same time. The versioning responsibilities here do not extend authorization to modify other texts or external source trees.

## Use module concept introduction and unique implementation to explain related text

When the knowledge chapter relies on the versioned kernel source code, two complementary paths are established: "Text → Total Reading Index → Introduction to Related Module Concepts → Specific Implementation Explanation" and "Specific Interfaces in the Text → Specific Title of Implementation Explanation":

1. When the same source code topic has both concept reading and implementation explanations, use the English `snake_case` subdirectory under `research/source_reading/<topic>/`: `navigation/` saves a total reading index and source code concept introductions organized by sub-functions or modules, `source_explanations/` only saves specific implementation explanations of macros, fields and function bodies.
2. The module concept introduction explains sub-function goals, participants, status, call chain, reading order and conclusion. You can use application scenario code, pseudocode, tables and Mermaid, but does not expand the upstream macro body or function body. The implementation explanation must give the upstream relative position, Chinese Doxygen reading instructions clearly marked as a repository supplement, cropped source code with Chinese comments, implementation principles, calling context and status side effects.
3. The conceptual intersection between the main text and the module concept introduction is an intentional dual perspective. It does not participate in source code deduplication, nor does it establish an automatic synchronization relationship. When reviewing, first determine what tasks the two documents help readers accomplish, and then determine whether they are actually duplicated implementations of the same version; cross-layer deletion and modification only based on terminology, field names, stage names, or call chain similarity is not allowed.
4. Only one authoritative source code explanation title is selected for a macro, function, field or configuration branch within the same version boundary. This title will be directly reused when multiple knowledge texts or call chains encounter it, and the macro body and complete explanation must not be copied separately. Related interfaces can be aggregated into an independently readable explanation file according to the same functional class, without creating micro files for each macro.
5. When the knowledge text starts using versioned source code evidence, link to the total reading index and related module concept introduction in `navigation/`; list the interfaces or checkpoints actually used in this chapter near the demonstration code, explain the functions, calling context and consequences of misuse one by one, and directly link to the corresponding title in `source_explanations/`. You cannot just link the file and let the reader search again.
6. The module concept introduction only expands on the status location, communication and timing unique to this sub-function. When encountering specific macros, fields or function bodies, precise links are retained and source code blocks are not repeated; authoritative implementation explanations use the associated entry table to backlink the total index, corresponding module introduction and knowledge scenarios.
7. The "mechanism used" must distinguish between functional paths and inspection paths. For example, mark locks, state transitions, memory ordering, GP and callbacks with Sparse, Lockdep, debug objects, assertions or alarms respectively; when checking the macro embedding function API, explain the expansion after checking is turned on/off and the coverage boundary of dynamic checking.
8. Stable interface semantics, causal models, and selection boundaries are only saved in `knowledge/`; precise versions of macro bodies, fields, branches, and line numbers are only saved in `research/source_reading/`. Synchronously updates all callers after moving to the responsibility subdirectory, without retaining old path aliases or compatible copies.
9. Update the topic outline and source code baseline entry to clearly distinguish between "Total Reading Index", "Module Concept Introduction" and "Source Code Implementation Explanation". The general index links all module introductions, and the module introduction accurately links the implementation title used. The realization document link back corresponds to the module introduction and general index; as long as any knowledge text links to `source_explanations/`, it must also provide the `navigation/` reading entrance.
10. When the user requires "full information synchronization", the topic outline and adjacent text, parent outline, general index and module introduction, implementation explanation related entrance, source code baseline, Atlas map/route/content index, repository homepage, as well as the real publishing list and Obsidian caller are audited layer by layer according to responsibility. You cannot just search the topic name, nor synchronize the text into a mutual mirror; you should synchronize the entry, version/configuration boundary, implementation ownership and affected rules, and make the reading-oriented entry as direct as possible to the complete title anchor.

The anchor fragment must be equal to the complete text after rendering of the target title, for example, the title source code `## 5.3\_rcu\_replace\_pointer接口实现` corresponds to `source_explanations/P05_xxx.md#5.3_rcu_replace_pointer接口实现`. Source code explains the title to avoid symbols such as `()` that will interfere with Markdown link parsing; when the title changes, all incoming links are updated simultaneously, and structural auditing is used to verify that the target title actually exists.

When you need to build or review this structure, read [references/source-evidence.md](source-evidence_en.md) for an introduction to module concepts and a unique implementation specification.

## Map conclusions to source code, but do not replace explanation with source code

Use `rg` to trace definitions, callers, configuration branches, and status writes. The common mechanism prioritizes checking upstream public directories. Architectural code is examined only if the conclusion relies on instructions, barriers, exception entries, cache maintenance, page tables, or other architectural contracts.

Every important source code conclusion is recorded:

- Kernel version and related `.config` options;
- Upstream relative source code path;
- Structures and fields;
- Functions and caller/callee relationships;
- The status before and after function execution;
- Execution context and locking, preemption, and IRQ constraints;
- Does this conclusion belong to a stable contract, an implementation detail, or a platform-specific fact?

## Establish source code symbol coverage ledger and accept modification capabilities

After entering `research/source_reading/<topic>/source_explanations/`, the goal is no longer just to verify the mechanism with source code, but to allow readers to continue tracking and safely modify the implementation. Adopt the **no unexplained symbols** rule: structures, fields, global objects, macros, functions and key parameters that appear in source code excerpts, call chains, stage tables or flow charts and affect control flow, status, synchronization, configuration or life cycle must meet one of the following three:

1. Fully explained under the currently only implementation heading;
2. Use Typora’s precise title anchors to link to existing authoritative implementation explanations;
3. Clearly mark mechanical statements or clipped intervals that are not relevant to the conclusion of this round and explain why they can be omitted.

First press **Realize Ownership** to decide where to modify. The data structure, algorithm and query of the general framework are uniquely expanded in the framework topic; the subsystem topic only expands its own instances, initialization parameters, event access, calling timing, configuration degradation and consumption scenarios, and accurately links the framework implementation. You must not omit the role of this instance in the current subsystem because the object type belongs to another topic, nor copy the framework core to each caller topic.

You must not allow `extern` declarations, static keys, global instances, initializers, degenerate branches of configuration, auxiliary wrappers, callback context markers, or inspector objects to appear solely within a code block without explanation in the text. The name seems intuitive, the object does not directly change the functional state, or the same type has been discussed in other topics, which cannot be a reason to skip the role and calling position of this instance.

Before editing, create a source code symbol coverage ledger and record at least:

| Symbol or implementation cluster | Questions that must be answered |
| --- | --- |
| Implementation Ownership | Is the common framework or the current subsystem responsible for unfolding, and which unique header does the cross boundary link to? |
| Declaration and definition | In which header file is it declared, in which implementation file is it defined, and who needs to access it across translation units? |
| Identity and initialization | Does the initial value come from static initialization, startup path or first use; how to determine the key, name and lifetime? |
| Writing and reading | Which path modifies or registers the status, and which path queries, consumes or clears it? |
| Calling and timing | Before or after functional actions; how to pair failure, nesting, rollback and asynchronous windows? |
| Configuration expansion | Related How do objects, macros, functions and return values change when Kconfig is turned on and off? |
| State Side Effects | Is the functional state, inspector shadow state, historical state, or diagnostic life state being modified? |
| Modification boundaries | When changing fields, initializers, call order, or configuration branches, which invariants, callers, and tests must be synchronized? |
| Explanation location | Where is the current title, other authoritative titles, or justified cropping instructions? |

The source code implementation explanation provides at least a diagram that can locate object relationships and status addresses, as well as an end-to-end sequence diagram covering entry, status registration or modification, consumption, exit/rollback; simple leaf functions can only be reused when the diagram of the upper-level implementation cluster has been completely covered, and the diagram must not only stay at the abstract mechanism layer. Figures, source code excerpts, status tables, and text must use the same set of specific symbols.

Each implementation cluster adds a modifiability description after "Implementation Principle" to answer: What invariants does the current code depend on, where is the minimum safe modification point, and which configuration branches, call points, exception paths, pairing actions, and observable verification must be checked synchronously after changes. Only when readers can trace from declaration to definition, from initialization to consumption, from normal path to degradation/rollback path, and can predict the scope of influence of a local modification, the source code explanation is complete.

The external kernel source tree must not be modified. When the source tree is unavailable, source code verification is clearly marked as incomplete and details must not be reconstructed from memory. Old version differences must be localized to precise field or call chain boundaries, and vague compatibility conclusions must not be used.
