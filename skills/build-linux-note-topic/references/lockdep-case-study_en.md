# Lockdep case: state layering of dynamic verification mechanism

[简体中文](lockdep-case-study.md) | **English**

This case comes from the independent Lockdep topic of the repository: the stable entrance is `knowledge/linux/synchronization_and_asynchrony/synchronization/lockdep/大纲.md`, and the version source-code entry point is `research/source_reading/lockdep/navigation/P01_Linux_6.12_Lockdep源码导读.md`. It complements the less expanded **Dynamic Checker** writing approach in RCU cases and does not require all topics to fork Lockdep's file count or fields.

## 1. First separate the functional state and shadow state

Dynamic validator topics recognize at least two causal chains:

```text
functional path
→ Really change mutex, object, memory, schedule or device state

Check path
→ Receive events, maintain shadow state, verify contracts and report
```

For example, mutex owner and waiting queue determine actual lock acquisition and release. `lockdep_map`, `held_locks[]` and lock class diagram only verify the reported lock protocol. Turning off the check does not cancel the functional contract; passing the check does not replace the proof of functional correctness.

When writing other debugging mechanisms, ask the same questions first: whether the check state is just a projection of the functional state, what false positives/negatives will be caused by missing events or incorrect classification, and whether the checker will actively modify the functional results.

## 2. Dynamic validators usually have more than one set of states

The Lockdep topic clearly distinguishes between:

| Status axis | Time scale | Typical problems |
| --- | --- | --- |
| The status of the function being checked | The current actual execution | Whether the function primitive is actually successful and whether the object still exists |
| Current shadow state | Current task or CPU | What events the inspector thinks are currently open |
| Historical knowledge across time | Global | Which types, sequences, dependencies, or combinations of calls have been observed in the past |
| Checker life status | Global/local | Check whether it is enabled, recursion suppressed, whether capacity is exhausted, whether it has been explicitly stopped by an error path |

Other dynamic validators use these axes only if applicable, but must not collapse "checker compiled", "checker currently valid", "target path covered" and "no errors reported" into a Boolean conclusion.

## 3. Accurately mark the relative sequence of events and functional actions

The check event does not necessarily occur after the functional action. Lockdep In order to model waiting dependencies, the acquire annotation of the blocking lock may occur before the actual functional lock is acquired; when the acquisition fails, the release annotation can be used to roll back the shadow record.

When writing a dynamic inspection topic, you must check:

1. Whether the event is reported before the function is attempted, after success, or before/after release;
2. How to cancel the shadow state when function fails, cancels, times out or exits abnormally;
3. When does provisional candidate status become official current status;
4. When the current event ends, which local states are revoked and which global history is retained;
5. How to isolate when a checker recurses into itself, IRQ/NMI, or concurrently writes global state.

Guessing the time boundary based only on function names such as `acquire`, `release`, `check`, etc. is not qualified.

## 4. The identity classification itself is the proof input

Dynamic validators often group a large number of instances into some logical category. Lockdep instance, `lockdep_map`, key, lock class and subclass division of labor description:

- Classification that is too broad may incorrectly combine different protocols and result in false positives;
- Classification that is too narrow may prevent the same protocol from being closed across instances and result in false negatives;
- The lifetime of a taxonomic identity must cover historical knowledge references;
- Changing categories, adding subclasses, or turning off verification cannot be used as default fixes to suppress alarms.

When creating topics on other verification mechanisms, if there is a type ID, allocation site, object class, domain, or annotation key, also explain how it is formed, when it is recycled, and the bidirectional consequences of misclassification.

## 5. Current evidence and historical closure cannot be mixed.

Lockdep's `held_locks[]` saves current's currently valid check record; it contains pairing status that blocks acquisition attempts and cannot be used to conclude that the actual lock has been acquired. The lock class dependency graph answers what order has been observed historically. Ordinary release cancels or rebuilds the current record, and does not delete the existing dependency history due to this unlock.

The reusable writing method is:

```text
evidence of current events
→ Generate candidate relationships
→ Check with combined history across time
→ Distinguish between history writing during check and successful current record submission
→ Only the local state will be rolled back when the current event ends
```

For example, this repository fixes the new lock-chain path in the pinned Linux 6.12.20 implementation by first registering the lock-chain cache and then performing relevant verification; when the check fails, some global content may have been left, and the outage status needs to be observed at the same time. The verification process cannot be imagined as a transaction that "submits all at once if everything succeeds, and rolls back all history if it fails." The specific entry is the rule sequence and cache boundary of `research/source_reading/lockdep/navigation/P03_Linux_6.12_Lockdep依赖图与规则引擎模块导读.md` in the repository.

If the dynamic checker also uses cache, it must be stated when cache registration occurs, what expensive checks are omitted by hits, and what current state must still be maintained. "Skip repeated verification" cannot be written as "there is no inspection cost at all in this event".

## 6. No reports must be accompanied by validity and coverage conditions

The "no alarm" of the dynamic inspection topic is at least bound to:

- The corresponding Kconfig/build option is indeed enabled;
- The checker is not currently explicitly stopped due to a bad path, internal inconsistency, or capacity exhaustion;
- The target component path has actually been executed;
- Complete reporting of functional primitives or custom mechanisms;
- Identity classifications, event types, and context models are consistent with real protocols.

The diagnostics chapter should provide checker health status, capacity counts, coverage paths, and expected reports rather than just giving a switch name.

## 7. Division of source code materials

The Lockdep topic continues to verify the responsibilities of `navigation/` and `source_explanations/`:

- The general index organizes the source code map, main call chain and recommended reading order;
- The module introduction talks about three types of functional loops: identity/event, graph rule, and query/diagnosis;
- Implementation explanation uniquely expands Chinese Doxygen, Chinese inline source code and status side effects according to specific structures and function clusters;
- RCU only references Lockdep core queries, and Lockdep only references RCU virtual map and alarm adaptation. Both parties maintain their respective implementations to avoid cross-topic duplication.

This shows that "one authoritative explanation of the same implementation" also applies to the intersection of two source code topics: first select the authoritative title according to implementation ownership, and then establish a two-way precise link.

When synchronizing the full amount of information in the Lockdep topic, it is necessary to review along the discovery chain: synchronization general outline and lock/RCU adjacent topics can enter the stable text, Atlas map, learning route, content index and repository homepage can respectively discover the text and source code general index, `SOURCE_BASELINE.md` can locate saved files and reading entrances with anchor points. This only synchronizes the discovery of relationships and version facts, and does not require these entries to copy Lockdep's inspection model.

## 8. Dynamic validator delivery verification

- [ ] Functional state, current shadow state, historical knowledge and inspector life state have been distinguished.
- [ ] The sequence of event reporting relative to function attempts, success, failure, and release has been checked.
- [ ] Identity classification rules, lifetime, false positive and false negative consequences explained.
- [ ] How the current state generates candidate relationships, and how candidates are submitted are closed loops in history.
- [ ] Boundaries for cache, capacity, recursion suppression, shutdown, and shutdown configurations have been stated.
- [ ] No warning conclusion also records enabled status, checker validity and coverage.
- [ ] The checking mechanism is not written as a functional guarantee, and the functional contract does not disappear when checking is turned off.
- [ ] There is only one authoritative explanation title for the specific source code implementation across topics, and Typora is used for precise anchor point inter-linking.
