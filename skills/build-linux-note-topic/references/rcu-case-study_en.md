# RCU Case: Reusable Design Decisions

[简体中文](rcu-case-study.md) | **English**

Treat the RCU topics in the repository as concrete examples of the approach, not as templates for mechanical replication. Its authoritative entry is `knowledge/linux/synchronization_and_asynchrony/synchronization/rcu/大纲.md`.

## Contents

- [Content Protection Experience](#0-content-protection-experience)
- [Source code evidence cannot be degraded into link routing](#01_source-code-evidence-cannot-degenerate-into-link-routing)
- [RCU terminology must be decoded first](#02_rcu-terms-must-be-decoded-first)
- [RCU must first be classified according to the orthogonal axis](#1-rcu-must-first-be-classified-according-to-orthogonal-axes)
- [Decisive scene split](#2-decisive-scene-split)
- [State Ownership Experience](#3-state-ownership-experience)
- [Experience with RCU and kref](#4-rcus-experience-with-kref)
- [Cost experience](#5-cost-experience)
- [Source code evidence experience](#6-source-code-evidence-experience)
- [Experimental experience](#7-experimental-experience)
- [Cognitive suspense experience](#8-cognitive-suspense-experience)

## 0. Content protection experience

The RCU method is a reading architecture method and is not a natural compression target. Applying RCU style to notes that have been reviewed and only required to be formatted this time means manifesting stages, prerequisites, solved problems, and follow-up questions while retaining technical semantics, proof models, source code implementations, variants, diagnostics, experiments, and selected materials; it does not mean replacing the raw materials with a newly written short tutorial. These may be modified within the scope of authorization if the user explicitly requests rewriting or compression.

When the user only requires typesetting, the technical semantics and information units of each chapter should be retained, and mechanical expressions such as numbering, blanks, lists, tables, navigation, and anchor points can be adjusted, and a reading map can be added to the periphery. Splitting, merging, rewriting or deduplication is performed according to the editing mode explicitly authorized by the user.

## 0.1\_Source code evidence cannot degenerate into link routing

After the RCU knowledge text enters the source code layer, **explanation of the local completion mechanism** is still required. Source code unique expansion does not allow knowledge chapters to be written as a collection of source code file lists, module navigation, precise title links, and evidence checklists.

Taking a round of ordinary Tree RCU synchronization waiting as an example, the total number of relevant functional modules must at least close the following problems:

1. What is the waiting object of `synchronize_rcu()`, and who will hold the completion responsibility after the writer goes to sleep;
2. GP request, physical GP, GP kthread, `rcu_state` belong to concept, request, executor or state carrier respectively;
3. How is the CPU local QS evidence latched, and why is it not yet a shared completion conclusion?
4. How `rcu_data`, `rcu_node` and the root node aggregate local facts into global completion;
5. After GP is completed, how does the callback or dedicated wait path return the results to the original writer.

Each question is progressed according to "Basic concepts → Background gaps → Solutions → Reader predictions → Source code evidence". They can be classified into synchronization waiting, GP, QS, tree aggregation and callback modules respectively, and do not need to be fully borne by one vertical source code chapter. EQS, SRS, strict GP, force-QS, stall, preemptive task debt, version differences and Lockdep can only enter the corresponding module branch after the default mainline is closed. If readers cannot answer the above five questions after hiding all links, it means that the main text has degenerated into a routing page and must be rewritten or renamed.

The knowledge text can explain the current scenario with short source code excerpts, faithful pseudocode and state diagrams; the complete function-by-function implementation, Chinese Doxygen and modifiability instructions are still saved in `source_explanations/`. The difference between the two levels of responsibilities is the granularity of evidence, not "one is responsible for speaking and the other is only responsible for jumping".

## 0.2\_RCU terms must be decoded first

The RCU literature uses both paper abbreviations, Linux implementation family names, Kconfig notations, source code identifiers, and pedagogical terms introduced in this topic for reasoning purposes. They cannot be defaulted to a set of "RCU common sense" that everyone understands. According to the reading contract of SKILL.md, new concepts necessary for current reasoning are explained in place, and the prerequisite knowledge that has been clearly established is briefly reviewed; the entire glossary is not repeated at the beginning of each chapter. Classification tables, GP trees, state debts, and source code call chains must rely on acquired knowledge.

Distinguish at least the following name properties:

| First appearance of writing | What must be told to the reader first in this chapter |
| --- | --- |
| RCU | The English abbreviation of Read-Copy Update, and what actions the three words correspond to in this scenario; you cannot just give the full name and then enter the source code immediately. |
| SMP | The English abbreviation of Symmetric Multiprocessing; it describes a multi-processor/multi-Central Processing Unit (CPU) execution environment and is not an RCU type. |
| GP | The English abbreviation of Grace Period; indicating that it is a logical waiting boundary that is to be proven to be completed, not a thread, a tree, or a fixed duration. |
| QS | English abbreviation for Quiescent State; it is local evidence of which type of actor has crossed the old access boundary, and whether it is sufficient in the current configuration. |
| Tree RCU, Tiny RCU | The implementation family name of Linux ordinary RCU. Tree/Tiny is not an abbreviation that needs to be expanded; explain the implementation scale and structural differences corresponding to the naming. |
| `CONFIG_PREEMPT_RCU` | Kconfig configuration symbol; indicates that it changes the read-side execution model and proof debt placement of Tree RCU, without writing it as a second GP tree or another set of public APIs. |
| "CPU debt" "task debt" | This topic is a teaching model word used to explain "who still owes the current GP a proof of completion". It is not a Linux public API, a formal Kconfig type, or a source code field of the same name that must exist. This must then be mapped to the true state location. |

This table only demonstrates name decoding and cannot be used as a permanent explanation-free certificate for subsequent chapters. Classified chapters such as P04 that can be opened independently must still give the Chinese and English names or the nature of the name, a local explanation and an accurate link at the first appearance. Each row in the classification table must also indicate whether it belongs to a protection domain, an implementation family, an execution model, a runtime policy, or a diagnostic facility; readers must not be allowed to guess the basis for classification based solely on the appearance of the English family name, configuration fragment, or policy abbreviation.

If there are new English role names, status abbreviations, generation names, protected domain names, forced path abbreviations or callback uninstall abbreviations in the definition of RCU private terms, first align these words recursively, or use ordinary Chinese that have been explained. Links to other chapters can only provide depth and source code evidence, but cannot allow the basic semantic dependence of the current sentence to jump.

## 1. RCU must first be classified according to orthogonal axes

RCU also contains public APIs, different protection domains, underlying implementation families, read-side execution models, GP strategies, callback execution strategies, and diagnostic facilities. They are not the same level of "type":

| Category axis | Examples in RCU | Questions readers need to answer first |
| --- | --- | --- |
| Public Semantics and API | `rcu_read_lock()`, `rcu_dereference()`, `call_rcu()`, `synchronize_rcu()` | What the interface promises and which internal options are hidden |
| Protection domain or reader definition | Ordinary RCU, SRCU, Tasks RCU | Which type of participant is waiting, and whether the reader can block or migrate |
| Implementation family | Tree RCU, Tiny RCU | What core structure is used to implement ordinary RCU semantics |
| Tree RCU read-side execution model | `CONFIG_PREEMPT_RCU=y/n` | The old reader debt is only with the CPU, or will be transferred to the task registration |
| GP operation strategy | normal, expedited | How to exchange system disturbance for waiting delay |
| callback execution strategy | local execution, NOCB offloading | who promotes and executes mature callback |
| Diagnostic facilities | stall, Lockdep, Sparse | What to observe or check and not replace which functional guarantee |

The classification coordinates must precede any "non-preemptible full source chain" or "preemptive full source chain". Recommended thematic stages are:

| Stages | Main Reader Tasks |
| --- | --- |
| Common concepts and interfaces | Establish a minimum closed loop of release, read-side critical section, GP, QS, callback and object recycling |
| Type and configuration coordinates | Distinguish between protection domains, implementation families, and Tree RCU preemption models, and know what choices are hidden by the public API |
| Differences between module implementation and variants | Discuss public responsibilities by module, and then compare non-preemption/preemption differences |
| Application and experimentation | Combine life cycle, diagnosis, selection, and use experiments to verify the previous specific certification obligations |

Object lifecycle combinations (e.g. RCU + kref) belong to the apply phase. It can provide an independent entrance after the common API, but cannot be inserted into the default main line of "Public Interface → Classification Coordinates → Tree RCU Public Skeleton".

### 1.1\_Tree\_RCU compares the preemption difference by module

Tree RCU's common GP requests, node topology, callback segments, and synchronization waits cannot be covered in two configuration chapters. The module matrix contains at least:

| Function module | Public responsibility | Non-preemptible delta | Preemptive delta |
| --- | --- | --- | --- |
| Read-side entry and exit | Establish a common RCU critical section contract | The read-side execution model does not allow tasks to be preempted; the specific entry may be a no-op according to the configuration, and the shared reader identity is not registered | The task saves the nested state and is allowed to be preempted |
| QS/EQS evidence | Exclude old executions before GP | CPU QS is enough to pay off normal reader debt | Debt may be transferred to task registration on context switch |
| GP request and life cycle | Merge request, start generation, wait, cleanup | Basically follow the shared GP control path | Basically follow the shared GP control path |
| `rcu_node` aggregation | Aggregate local evidence into completion at the root | Mainly waiting for CPU/subtree bits | After the CPU bit is cleared, it may still wait for blocked task |
| callback and synchronous waiting | bind target GP, obtain execution qualification, wake up or release | basically follow the shared completion-delivery path | basically follow the shared completion-delivery path |
| Slow path and operation strategy | EQS, FQS, stall, expedited, hotplug, NOCB | Only the applicable differences are explained | Only the applicable differences are explained |

The old "non-preemption proof + non-preemption complete source code → preemption proof + preemption complete source code → later expanded by public module" will cause the public implementation to appear three times and postpone the classification until the reader has entered the field, which is an anti-pattern that is clearly rejected in this case. There are indeed different proofs for non-preemption and preemption, but the differences are concentrated in reader state ownership, QS validity and node completion conditions; the proof difference should be compared side by side by the same scenario in the corresponding module.

When applying to other themes, the difference between common modules and variants must also be determined first. Simple mechanisms to merge issues, abstractions, and implementations; only split vertically if variants change most of the full cycle, and no empty chapters may be created for the number of historical RCU files.

## 2. Decisive scene split

Two tasks that both "execute reader code" may belong to different sets:

- Tasks that have been created but are blocked outside the read-side critical section by gating do not get the old pointer;
- Tasks that have taken the old pointer and are subsequently preempted still carry the old reader debt.

This distinction forces the topic to establish a CPU proof model and a task proof model separately. It also shows that the scene must accurately explain when the reading side enters and when the pointer is read. It cannot just say that there is a reader thread. Having entered the relevant old read-side interval but not yet reading a pointer is the third case: it cannot be inferred that the implementation will not wait for this interval just because "there is no old pointer yet". Whether the object can be obtained by this task and what evidence needs to be collected in this round of RCU must be explained separately.

## 3. State ownership experience

The RCU implementation cannot be said to be a counter:

- The task-local nesting state represents a preemptible reader that is still in the critical section, even if it is preempted and not running at the moment;
- Context switching can transfer life cycle debt to the shared node list;
- Per-CPU state records current grace period observations and local quiescent state evidence;
- Node masks aggregate CPU or child node debt;
- Global state coordination grace period generation;
- The callback or completion hands the result to the recycler.

A core teaching obligation is to explain each transfer rather than just listing the structures.

## 4. RCU’s experience with kref

RCU and kref do not automatically notify each other, but the module to which the object belongs combines the two.

Distinguish at least the following models:

1. An object published by RCU gets a long-term kref within the read-side window;
2. A publication reference survives until the end of the grace period and is released by the callback;
3. An RCU version root holds multiple independently allocated kref data block references;
4. The short reader borrows the root object's ownership of the data block, and the escape reader obtains its own data block reference.

Each allocation must have only one final release agreement. `kref_put()` calls the release provided by the caller when the count reaches zero; the empty callback is the module's own choice, not the default behavior of kref, nor the RCU handover mechanism.

## 5. Cost experience

A large number of short readers will not result in an old copy or kref operation being performed on every read. When the update rate and recycling latency are relatively stable, there are no long-term references that escape, and the measurement is based on exclusive retired bytes, the average retired memory can be estimated by the following formula:

```text
Retired version generation rate
× Grace period/callback delay
× Number of bytes exclusive to each retired version
```

This is not a peak upper bound; burst updates, ongoing backlogs, shared blocks, and long-term references require separate accounting. Long read-side extents, high update rates, large exclusive root objects, callback starvation, and high escape ratios are distinct costs that must be treated separately for valid comparisons.

## 6. Source code evidence experience

When a set of RCU source code materials requires service module understanding, specific implementation tracking, and multiple knowledge texts, `research/source_reading/rcu/` is split into two layers according to responsibilities:

- `navigation/` contains a total reading index, as well as guides for functional modules such as interface, read side/QS, GP, node aggregation, callback, operation strategy and implementation family; non-preemption/preemption differences are explained side by side in relevant modules. Only families such as SRCU and Tasks/Tiny that truly change the complete proof domain retain independent guides;
- `source_explanations/` is oriented to specific macros, functions, fields or closely related implementation clusters, providing upstream relative positions, Chinese Doxygen comments supplemented by the repository, source code with Chinese inline comments and implementation principles; the same implementation of the same version is only expanded once.

When the knowledge text enters the source code evidence for the first time, it links to the general reading index and related module introduction. When it encounters a specific interface or checkpoint, it accurately links to the unique source code implementation title. When module introductions and other call chain documents encounter existing public implementation explanations, they will only be quoted and no longer copy macro or function bodies.

For Linux 6.12, RCU source code chapter tracking:

- Synchronously wait for requests and wake up;
- Grace period generation activation and cleanup;
- Node mask initialization;
- Per-CPU identification of new generations;
- Local static evidence latch;
- Asynchronously report to the node tree;
- Registration and final unblocking of preempted tasks;
- Context tracking evidence in user mode/idle mode;
- The callback is eligible for execution and actually executed.

After entering the specific implementation layer, a symbol coverage ledger must be established. Just because the previous mechanism model has been established, the virtual lock, static key, configuration initializer, wrapper function or callback context mark in the implementation cannot be compressed into a sentence of "access Lockdep". For example, the **general Lockdep data structure and query algorithm** of `rcu_lock_map`, `rcu_bh_lock_map`, `rcu_sched_lock_map` and `rcu_callback_map` are uniquely deployed by the Lockdep topic; the RCU topic must independently track the `extern` statements and `update.c` of these instances. Definitions, wait types, acquire/release call sites, current shadow holding records, RCU query/assertion consumers, and `CONFIG_DEBUG_LOCK_ALLOC=n` degenerate branches. Also explain that they check for identity rather than function locks, and how modifying the order of calls or missing a pair can change the diagnostic results.

"The prefix belongs to the general framework" does not mean "the instance also belongs to the framework topic". The cross-implementation is split according to ownership: the framework topic explains `lockdep_map → lock class → held_locks[] → 查询`, and the RCU topic explains how its four maps use this path. The standard also applies to GP, QS, callback, NOCB, hot plug and other source code implementation clusters.

Differences in Linux 5.10 are documented in specific fields and call chain boundaries, rather than being generalized as "basically the same". Other kernel mechanisms also follow the same standard.

## 7. Experimental experience

The RCU experiment is intentionally structured into two phases:

- Release old versions before allowing gated future readers to perform first lookups;
- Let the reader get the old pointer before it gets preempted on the same CPU, and prove that the grace period waits for it to finally unlock.

Completion, CPU binding, timed release, and event timestamps make causal boundaries observable; the true order cannot be inferred just from the order displayed by printk. The current preemption phase also requires at least two online CPUs, the ability to preempt ordinary RCU, the full preemption running mode other than PREEMPT_RT, and the use of FIFO threads on the same CPU to create observation windows. The configuration and steps are subject to `labs/kernel/rcu/P01_晚到读者与抢占读者/README.md`; the method examples do not mean that the target kernel has been run this time. The experiment approximates the specified scheduling conditions and does not claim to reproduce the uncontrollable "999 queued tasks" verbatim.

## 8. Cognitive suspense experience

What keeps readers engaged in RCU special topics is not the format of the titles, but the way open questions are passed from chapter to chapter:

- P01 proved that there are still gaps in locks and atomic pointer exchanges, and P02 deduced the release boundary and GP;
- P05 first closes the Tree RCU public S0~S9 cycle, and then P06 uses the preempted reader to derive the difference between the CPU debt and the task debt;
- P08 first establishes the GP generation and coordinator life cycle, and then P09 and P10 track local QS evidence and node tree convergence in sequence;
- P11 only solves when the callback is eligible for execution, and P12 then solves when and who actually executes it.

When applying to other topics, maintain the "one question, one increment" approach: first let the current model be completely established, then use the smallest counterexample to expose a gap, only introduce the state or path required to solve the gap, and finally use source code or experiments to realize it. Don't list all the components of a mature implementation in advance before problems arise.
