# Mapping from concept to implementation and input and output

[简体中文](concept_implementation_mapping.md) | **English**

This reference is used for conversion between specifications and products, contracts and source codes, logical objects and actual carriers. The point is to allow the reader to reconstruct correspondences rather than to memorize an additional set of names. Simple same-level facts do not need to be applied to the complete table diagram; when there is sharing, distributed implementation, or inclusion/connection ambiguity, they must be expanded in place in the text.

## Fix the concept first, then introduce the implementation

The concept phase answers "what responsibilities, status, inputs, outputs, and guarantees must be there", and the implementation phase answers "who uses what carrier and path to fulfill these responsibilities". Advance in the following order:

1. Establish a concept from the current problem, select a specification or contract and its version, and use the formal terminology of the layer; indicate whether objects are counted by cores, tasks, queues, connections, or other units.
2. Introduce the selected product, software implementation or integration example and explain the level and version it belongs to. The first appearance of the implementation name indicates what type of object it is, and cannot just be given an alias.
3. Before using the implementation name explanation function, put the established responsibilities and status on the actual carrier one by one, and explain the quantity, attribution and connection.
4. Reuse the same scenario from the concept stage, demonstrate how the mapping works along the way through configuration and runtime, and finally discuss the costs and benefits of shared resources, layout, scaling, and power.

When explaining the beginning and switching between levels, use a short line to clearly inform the reader of the current level and basis, and then proceed to the explanation. For example:

- **Level of explanation: conceptual level.** This section describes the roles and guarantees required by a given version of a specification.
- **Explanation level: implementation layer.** This section describes the actual modules, status, and access paths for a product revision or software submission.
- **Level of explanation: mapping from concept to implementation.** This section maps the aforementioned specification roles to currently implemented carriers.

In the actual text, "a certain specification" and "a certain product" are replaced with verified names and versions; specific examples such as chip integration must also indicate the instance identity. Labels should be placed after the title and before the explanation, and cannot be hidden in the glossary, metadata or sources at the end of the text; consecutive paragraphs at the same level should not be labeled repeatedly, and when the title has clearly given the level and object, there is no need to add another line. When a section is advanced across layers, it should be re-marked at the actual switch point, and a general "implementation" label cannot be used to cover the specification definition and product selection.

Functional components in a specification do not automatically equal independent physical modules; software objects do not automatically equal independent threads or processes; nor do register address windows automatically equal the physical location of the state behind them. When the implementation manual follows the canonical name, or when the manufacturer uses two product names as synonyms, it explains the naming scope and cannot extend this synonymous relationship to the canonical layer.

## Crossing module boundaries and current issues

Mapping can only occur between objects that have stated relationships. The use of "numbers", "states", "domains" or "maps" in both modules is not a good reason to present them side by side; while physical sources and hardware endpoints are currently being interpreted, this does not automatically extend to firmware descriptions or operating system resource management.

Before introducing another module, first determine whether it has the necessary responsibilities for the current step:

1. **The current derivation does not depend on it:** No side branch reminders are inserted. Keep relevant knowledge in the responsible module; when there is a valid explanation that needs to be reorganized, move it to its responsible position or reuse the existing authoritative explanation, and do not discard unique knowledge to remove branches.
2. **There is indeed a handover or the boundary must be drawn:** Point out the module and management objects, explain what it receives, what it produces, who maintains it, and why it needs to be distinguished currently; only expand the relationships that are sufficient to complete the reasoning of this section, and then accurately link the existing responsible chapters.
3. **Responsible chapter has not yet been implemented:** If it is not the current premise, it will not be introduced temporarily; if it is the current premise, the necessary explanations must be supplemented within the current scope of authorization first, and cannot be replaced by a vague "we will talk about it later". Unknown implementations are explicitly acknowledged and do not fabricate bases or jump locations.

For example, to compare private sources with the same number between two processing units, you can close the corresponding processing unit, source number, and status window; to redirect a shared source to another processing unit, you can only track the source identity and target fields. At this time, suddenly adding "the number displayed by the operating system may be different" will insert another set of management rules into the hardware judgment. Only when entering into the issue of how the operating system takes over hardware notifications does it introduce its interrupt management module and explain how the hardware number participates in the search of this module; firmware description conversion is another boundary and cannot be confused with the runtime software number.

This rule governs expression and dependencies and does not force all topics to be hardware-only or software-only. If the software of the configuration register, exception entry, device processing and completion notification are in the current transaction, they must still be declared as executors. What we really want to avoid are useless cross-module comparisons and dangling prompts that only throw out conclusions without the corresponding modules and basis. The next question that naturally arises from the current conclusion can be asked at the end of the chapter; if the rules of another module have been asserted, the above minimum explanation must be completed first.

## Changes and invariances must be bound to actions and time points

Conclusions such as "the number remains unchanged", "the state is independent" and "only the target changes" must let the reader know which attribute of which object is being compared, what operations have been performed, and which two moments are being observed. Readers cannot be asked to first guess the dimensions the author wants to compare and then eliminate concurrent events on their own.

First use a direct answer to determine the scope of the current comparison. The user only asks "Has the number of the original source changed after changing the receiver?" and then compares the receiver and source numbers; it is not possible to add enable, clear, other object writing or irrelevant state machines to meet the writing template. **Figures should clarify current conclusions and not expand on current issues.** The following elements are used to check whether the current conclusion is valid, and do not require each item to be expanded into independent paragraphs or new operations.

Within the current comparison range, use a fixed instance to describe what is required:

| Comparison elements | What must be stated |
| --- | --- |
| Objects and attributes | How a specific object is selected; whether it is comparing identity, enablement, target, content or running status, it cannot be replaced by a general "it" |
| Initial conditions | The value or relationship of this property before the operation; which inputs, concurrent writers, and ongoing transactions have been pinned or excluded |
| Trigger action | Who modifies which field through which entry, or which event promotes the state transition |
| Observation time points | The time points when the operation is issued, received, written visible, cache invalid, synchronization completed, etc. cannot be mixed; only the time point when the current inference dependency is expanded |
| Modification result | How the modified attribute changes from the old value to the new value; why the attribute not selected by this operation is not directly modified by it |
| Independent changes | Whether other writers, input events, confirmations, completions, etc. may still change the relevant status; if these events are excluded, the condition should be made clear |

When multiple objects or fields that can change independently are involved, and words alone are easily confusing, a before-and-after comparison table, side-by-side sequence diagram or flow chart must be provided where the key comparison is made for the first time, so that readers can directly see the actions and change scope currently being asked. The comparison table only places the comparison items required to answer this question; the sequence diagram or flow chart only expands the propagation, waiting and validation sequences that this question depends on. The text explains cause and effect along the diagram. You cannot add a decorative diagram with only nouns after a long concept, nor can you expand the scope of operations in order to fill the diagram. A simple one-step variation of a single object does not force the drawing to form.

"The fields of object B are not modified by this writing operation of A" does not mean "all states of B remain unchanged". If only enabling is discussed, make it clear; if the input may still change the pending state, explain it separately. Changing the target field does not mean changing the source identity, nor does it mean that the processing process that is already being executed is immediately migrated. When identities need to be compared, point out which coordinates or indexes determine the identity; change the index to access another object and modify the attributes of the original object respectively.

In particular, asynchronous propagation cannot just list "old value before writing, new value after writing": it should indicate when the old value or the new value is allowed, and after which verified completion conditions can rely on the new value. The data is only guaranteed to be updated in the end and does not create an immediate effect or a specific handshake mechanism; when the cache may be refreshed in advance, it does not write "must still be the old value" before synchronization is completed. The completion flag for one operation cannot be used as a completion guarantee for another type of register write or command.

"Stay unchanged" in the chart should be tested by rhetorical questions: **Relative to which move has it remained unchanged? What conditions were fixed? Are there independent events that would overturn this conclusion?** Only fills in the necessary boundaries of this conclusion, and does not list all actions that may change other states. If the answer requires another module, the necessary handover and accurate entry should be established according to the previous section; irrelevant numbering or status systems will not be added to the current comparison.

## Put the corresponding relationship into responsibilities and status

Use the text and necessary correspondence tables to answer the following questions at the first level crossing. The precise quantity, placement and sharing granularity are only required to be within the scope required for current reasoning and the data can be confirmed; when it is not disclosed, clearly unknown and reliable interfaces are guaranteed to be valid conclusions. You cannot make up details for filling in the form, and you cannot judge the lack of undisclosed information as a failure to explain. The table is a tool for organizing the basis, not a template that must be repeated mechanically in each section.

| Mapping items | Relationships that must be established |
| --- | --- |
| Concept identity | Specification/contract name, version, responsibility, logical object counting unit and quantity |
| Implementation identity | Product/source code name, version, belongs to physical module, internal functional partition, software object, executor or address view |
| Corresponding quantity | One carrier carries several logical objects. Is the responsibility of a logical object distributed on several carriers? What distinction does logical isolation rely on |
| State landing point | Which state is actually saved by which module or data structure, who is responsible for updating and using it; where are the shared state and per-object state respectively |
| Access and communication | Configuration entrance, actual access target, forwarding path, running input and output and respective interfaces; how to select objects by identity or index |
| Formation timing | Which structures are determined at design/synthesis/integration time, which ones are established at startup/enumeration time, and which ones are allowed to be changed at runtime |
| Evidence boundaries | Which specifications support responsibilities, which implementation documents support placement points, which integration documents support native quantities; what has not been disclosed |

You cannot end the mapping with "implemented part of it" or "integrated together": you must list the responsibilities and status of the current block, and list the carriers of the remaining responsibilities. If the information only confirms the function allocation but does not disclose the internal RTL or storage circuit, it directly indicates that the function allocation has been determined and the internal microstructure is not yet known; therefore, the proven implementation cannot be returned to a vague "related".

Distinguish the following relationships without using an unlabeled arrow:

- **Implementation:** Specific logic or code fulfills an abstract responsibility, which does not mean that the two are two entities connected in series.
- **Contains:** The actual module or object has certain parts, fields or functional partitions inside; indicate whether it is a confirmed physical composition or only divided by function.
- **Connection:** Two actual endpoints passing content via port, message, shared memory, or call, indicating direction and content.
- **Address View:** An address or interface exposes a set of accessible states. The entry, decoding point, and storage point may be different, and its actual path must be tracked.

"One logical role per CPU" and "one physical block serves multiple CPUs" can be established at the same time, but they are not the end of the explanation: it is also necessary to point out how the status of each CPU is distinguished, whether the processing logic is shared, and how the interface identifies objects. Only write "merge multiple independent components" if the data proves that the original entities were indeed merged; otherwise, describe the current internal composition directly and do not fabricate the process of independence and then integration.

## Let’s first explain the objects passed across components

The same wiring does not mean the communication model is the same. When readers understand multi-component systems as cascades, pipelines, or message forwarding, they must first confirm which relationships in this model hold, and then explain the interface facts where divergence occurs: an arrow represents a single event signal, identity data, candidate results, or configuration commands; what can the receiver know from it. We cannot start by saying "attributes are still managed upstream" and then leave it up to the reader to guess how the attributes participate in downstream processing.

Distinguish between persistent configuration, current data obtained from the configuration, and the receiver's own processing rules. Passing a value upstream for downstream processing according to established rules does not automatically mean modifying the downstream configuration, handing over the entire object, or requiring the downstream to copy the upstream implementation. Use a minimum transaction to explain how the sender obtains this data and what the receiver does based on it; only the currently necessary fields and meanings are given. When the protocol is not disclosed, it indicates that this is a logical message representation and does not fabricate message encoding, storage copies, or beat-by-beat processes.

When multiple stages are called "screening, inspection, and management", write down the input set, judgment basis, and output of each stage respectively, and indicate what information or constraints are newly incorporated in the later stage. If the reader wonders "why this information is needed", temporarily remove it from the same scene to show that the recipient will not be able to distinguish between two situations that require different processing, and then restore the minimum necessary information. The necessity of explaining the boundary in this way does not eliminate doubts by repeating the definition of responsibilities; the revision should be integrated into the original derivation and follow [Reconstructing the continuous text from questioning](explanation-quality_en.md#71-reconstruction-of-continuous-text-from-questioning).

## Build an input-output model for each actual participant

Extract status and ports from the current running process, rather than just following the manual table of contents and introducing components one by one. Each participant in this scenario explains:

| Question | What should be given in the text |
| --- | --- |
| Who the input comes from | The actual upstream endpoint, the incoming request/data/signal, and the interface or shared state |
| What is the current basis | This component's own access, selection, output rules and status positions; separately explained with the rules of other components |
| Who changed the configuration | Writer, access entry, target identification, necessary forwarding, final modified field/register status and the logic to read it |
| To whom the output is given | The actual downstream endpoint, output content, selection conditions and the state changes caused |
| How to give feedback | Who generated the response, confirmation, completion or error, what path it took to return, and whose status was finally updated |

Access through component A does not mean that the functional status of A is modified; A's policy affects which requests B receives, nor does it mean that A directly configures B. Track the **configuration access path, normal request/data path, and response/completion path** separately; add their control paths when low power is involved, and do not mix them into the same flow because they share the same module.

Reading the register may simultaneously trigger a state transition. Explain the location where the read value is generated, the return direction and the side effects of reading. Do not mix "observe", "confirm" and "complete" into a general access. The set state and the reaction after receiving the notification must also be distinguished; shadow states and synchronization lines are only introduced if there is evidence that replicas and synchronization mechanisms exist.

When faced with "whether to configure a large block or each object function inside", we should directly explain: which object is selected from which interface by the software, which state inside which module is modified, and which piece of logic is used. "Affected an object" cannot be used as the basis for "writing the state of the object", nor can you draw an independent entity outside the module based on a logical name.

## Shared interfaces, grouping and physical benefits must have implementation paths

When multiple objects share a communication channel, explain at which level they are aggregated, how they are selected or reused, how the source/destination is identified, how the receiver is dispatched, and how the return information finds the original object. When the information does not disclose the arbitration algorithm, it only describes the confirmed selection function and unknown algorithm, and does not invent named circuits or strategies.

You cannot claim to have solved the problem of parallel to series connection by directly merging multiple arrows into one line. Messaging, time division multiplexing, and electrical serial links are not the same concept; the transport protocol may have a multi-bit data bus. Only when the data provides interface width, connection topology or comparison basis can we quantitatively claim how many signal lines have been reduced; if some lines still exist, explain which section of the line has been reduced.

Names such as "group", "cluster" and "domain" must indicate what they are divided into. Computing topologies, communication port sharing ranges, cache domains, clock domains, and power domains cannot be equated simply by having the same name. Explain who determines membership when, what policies can be changed by software configuration, and whether connections or membership can actually be changed; allowing selection of targets does not equate to being able to reorganize physical groupings. The number of physical blocks deduced from the number of cores, software enumeration number or address window number must be supported by current integration data.

Routing and power gains should be derived from previous state locations and communication paths: which segments of wire are shortened or shared, which logic can be shut down independently, which state must be retained, and how wake-ups are handed off. Without evidence, the time limit is limited to design deduction, and reasonable motives are not written into the fact that the product has been implemented.

## Figures must allow readers to distinguish boundaries from actions

When there is containment/connection ambiguity, the relationship diagram is given first, and then the operation is traced. If necessary, split it into a "concept-to-implementation correspondence diagram" and an "actual transaction path diagram"; different diagrams use the object names to prevent readers from guessing the pairing again. Pictures are placed where readers first need to judge the relationship. External links and end-of-chapter pictures cannot replace the current explanation.

- The box indicates the physical module, internal functional partitions or logical attribution; what is expressed by the nesting of the outer box must be explained in the legend, and functional grouping cannot be used to imply the chip layout.
- The actual communication arrow connects the actual endpoints that have a handover relationship, indicating the direction, action and content; when crossing the boundary of software, hardware or interface, write the call, instruction or transaction clearly. Concept-to-carrier mapping lines are marked with meanings such as "implemented thereby" and cannot be mixed with communication lines, nor can they string the abstract role and the carrier that implements it into two additional execution steps.
- The software executor, hardware interface and local event source are located separately, and one "CPU" node cannot be used to initiate requests or receive responses for all paths.
- Requests and returns are drawn in opposite directions. Write clearly what transactions the read value return, operation confirmation, and completion message belong to, and do not let the same arrow bear the opposite direction at the same time.
- If the same color only indicates the corresponding relationship between objects, the legend shall indicate this; the same color, adjacent positions, and dotted grouping cannot replace evidence of inclusion or physical distance.
- Each important connection in the diagram should be able to find a specific connection in the main text; the "both", "inside" and "this block" in the main text must have unique objects to refer to, and be renamed when the endpoints change.

## Check if the layers are still mixed with a minimal instance

The following are pedagogical assumptions, not specifications for any real controller: The contract states that each processing unit has one endpoint role, four in total. The product uses module M to save four copies of endpoint private status, and uses module G to save four copies of control records and provide access. Therefore, the responsibilities of the four logical roles are distributed among M and G. M cannot be drawn as externally connected to four independent endpoint devices, nor can each private state of M be regarded as a complete role.

The private state write to endpoint 2 is received and forwarded by G, and finally the record corresponding to endpoint 2 in M is modified; the write control record is landed in G. The entry points for the two operations are the same, but the status targets are different. Whether there is a shared arbiter and whether the record is saved by a flip-flop or SRAM is not provided and is not reproduced in the figure. This example only corrects the corresponding relationship and access path. The actual topic must be replaced with verified objects and evidence.

## Cold reading acceptance and misunderstanding repair

Hide the work blueprint and external links, read the text according to the declared pre-knowledge, and check whether you can answer:

1. Can I see the hierarchical annotations and corresponding objects before explaining? Which layer, specification or implementation does the current name come from? Are the two names aliases at the same level, or function and carrier?
2. How many logical objects, actual modules or software carriers have been confirmed in the current scenario? Where is the per-object state and what is shared? Are undisclosed quantities, placement points, or sharing granularities clearly marked?
3. Write a setting of object X, where to enter, how to find X, and what is finally modified? Should object Y be changed at the same time and on what basis?
4. What actual endpoints does a request pass through, who handles it according to their own rules, and who gives output and returns?
5. Does changing the software target selection change where the request goes, the content of the state, or the physical membership? Which structures are determined before running?
6. Which landing points have been determined by the data, and which microstructures have not yet been disclosed? Are there extra copies of devices, connections, or states that are not evident in the diagram?
7. Does each cross-module noun in this section participate in the current derivation? Have the necessary cross-module relationships been identified with modules, management objects and actual handovers, and accurate entrances given? Is there any dangling conclusion that just says "another number is different" or "will be explained later"?
8. Can "change/change" correspond to specific objects, attributes, actions, initial conditions and observation time points? Is there a comparison table or sequence diagram that can be read directly for the comparison of multiple objects or fields? Is it still possible for independent events to change other states? Does the text state that the scope of a single write is permanent?

Answers can only come from written text and factual evidence. Being able to recite "logic and physics are different" but not being able to complete the above tracing is still not clear. This check is a semantic independent reading review, and term scanning, graph syntax checking, and new keywords cannot prove passing.

When readers repeatedly ask "who includes whom, who is connected to whom, and who is configured," they regard this as evidence that the corresponding model has not been established. First, answer the asked questions about the relationship and applicable levels directly, then review the original data and revise the relationship diagram, status points and one round of operations; do not continue to add aliases, repeat "only implement part of it" or use longer disclaimers to maintain the original vague model. The scope of the revision is still subject to the current authorization, and the user's request to check the diagram first cannot be used as a reason to continue to correct the text.
