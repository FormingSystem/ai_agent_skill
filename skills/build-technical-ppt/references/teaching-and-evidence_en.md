# Explanation, basis and executable examples

> **Language / 语言** · [← 简体中文](teaching-and-evidence.md) · **English (current)**

## Establish understanding first, then go into details

Choose an official application that actually exists or a minimal complete example to run. Explain what readers currently have, what they are missing, and what problems they will solve next, and then introduce tools or interfaces. Calling readers "readers" does not use "students, trainees, classmates" and does not presuppose a teacher-student relationship.

Clearly differentiate between download, decompression/installation, project discovery, configuration, compilation, execution and hardware verification. The front-end host tools are arranged before use; the environment preparation chapter is not mixed with the complete compilation experiment. Readers need to understand the dependent version from the compilation mechanism, explain its decision relationship, and put the actual compilation back into the corresponding experimental chapter.

Each page is organized around a relationship or operation, with questions asked on the previous page being continued on the following page. The main text explains the complete cause and effect, and the PPT retains the key links required for understanding, without using extremely short labels so that readers can only listen to oral supplements. Notes are suitable for supplementary evidence, narrative clues and historical comments, and do not assume the sole prerequisite for execution.

The general interface system is an independent chapter, and each module reviews the relevant interfaces before explaining its own input and products. Split topics according to changes in understanding; there is no unified page limit, nor do you delete branches that readers need in order to appear streamlined.

When the user specifies the length, this limit shall prevail. First list a small number of core questions that must be answered in this book, give each page a clear role, and then check for duplication. The download and access topic first uses the package relationship diagram and the directory after installation to explain the object, and then organizes the operation by "get → install → hand over to the user → verify the actual selection". The technical basis is close to the conclusion to avoid bringing readers into the entire construction system just to show the source code.

When integrating reference drafts, retain their useful causal relationships, correct technical errors, placeholder commands, and inapplicable suggestions; delete production process content such as "rectification goals" and "suggested replacement outlines." PPT retains a main line that can be followed and necessary alternative entrances, and MD is responsible for downloading exceptions, complete branches, and in-depth evidence. Repeating using the same concept on the contents page, conclusion page, and table page does not mean making it clearer.

Optional configurations must be marked as optional where the action occurs and described alongside the default route. You cannot write the next step that must be done first, and then add the sentence "actually not necessary" every few pages. A complete example of an interface must show who it is passed to and where to look for success; it doesn't just say "append this -D", and it doesn't mix compilation commands that depend on unprepared download steps into the required download steps.

## Engineering mechanisms must have access points

Textbooks bear the cost of explanation. The author first reads the source code, extracts "what the object is, why it exists, who reads it, what conditions take effect, what the reader does, and how to judge the result", and then writes a continuous explanation; the quotation is placed after the corresponding explanation for checking. You cannot use "Based on: link; read a file locally" to end an unexplained mechanism, nor can you treat the listed source code path as the content itself. When readers check the source code, they should be reviewing the rules they have understood, rather than completing the explanations omitted by the author.

When comparing the official route to the self-assembled route, keep the same application, hardware goals, and observable results, and itemize the changes in responsibilities caused by the input changes. For each core component, first verify whether it is actually provided by the main repository, obtained from an external manifest, or accessed by the project itself; downloading, discovery, and actual compilation are different stages. You must not deduce from a certain vendor's package naming that all goals require a package with the same name, nor must you use "nothing to do with another vendor" to avoid where the current goal is to be implemented.

Taking package or module access as an example, the explanation chain should be completely walked through:

1. What the consumer holds: application directory, module root, SDK root, target identity, etc.
2. Which program is given what input: parameters, configuration file, environment, registration information or project list.
3. Who reads and discovers: files/functions, scan scope, conditions and default behavior.
4. What is produced: a parsed directory, a derived variable, a build record, a build target, or a command.
5. How to participate in the current project and verify: executed entries, added source code, header files, compilers and products.

The internal organization of the module will be explained later. Separate "how to enter modules into the project" and "how to organize the internal access code of the module" to avoid answering only the second half of a question.

When describing the interface, cover as needed: the tools it belongs to, usage, input or derived results, readers, default values or discovery rules, value forms, save locations, valid ranges, combination relationships, cancellation and update methods. Don't mechanically create large lists for each word.

Special distinction is made between the current terminal environment, build cache, project presets, current user registration information, and Python virtual environment. Explain clearly "which search mechanism is registered to, who will use it, and how long it will last" instead of general "permanent configuration". First demonstrate the common route of successful default discovery, and then explain the conditional route such as fixed version or active type change. Optional interfaces cannot be written as required operations.

## Documents and sources

When asking readers to open or modify a file for the first time, indicate one of the following states, and indicate the location and action in place:

| Source/Status | What should be explained |
| --- | --- |
| Original official source code | Which source code root to compare, which version to check, read or modify |
| Official external download | Download tools/lists/release attachments, location and version basis |
| Tutorial included | Material entrance and how to obtain it, does not imply the original existence of the official tree |
| Readers create by themselves | Create file or directory, complete location, content and creation stage |
| Tool generation | Which operation is generated, when should it appear after success, and which step to return to if missing |

If the directory does not exist, it will not be immediately judged as accidental deletion. First confirm the stage, root directory, version and source. Read-only excerpts are marked locally in the text, code blocks, and PPT to prevent readers from treating the excerpts as files that must be created or replaced.

Prioritize using upstream supported tools and manifests to obtain managed dependencies, and check revisions with actual directories. Web pages are used to check sources, issue assets, maintain status, or explain selections; manual ZIP is used for offline/tool-unavailable branches that are really necessary, and there is no need to artificially increase the necessary experiments of renaming after downloading or creating self-created source records.

The web page route clearly states the location of the site, organization/repository, page or tag, and search box, and gives direct links. The source code conclusion also provides the official document web page, repository document files and the location of the read code. The line number is only used as an aid. Description of the difference between fixed submission and latest page; check according to the current source code after upgrade. Differentiate between repository building, maintenance permissions, list collection, build discovery, chip support and real board availability, and cannot replace each other.

## Copyable operations

The code block/area clearly indicates whether it is a terminal command, configuration file content, read-only source code, interface form indication, or expected output. Do not mix terminal prompts and output so that readers may accidentally copy them. Highlight with the corresponding language, the comment must conform to that language.

The complete operating unit identifies the system, terminals, locations and premises. Commands are followed by meaning, success output, and failure checks; don't keep the reader paired between long code and distant explanations. When switching terminals, the working directory, path writing, and environment are re-accounted for, and variables are not automatically inherited across shells.

Prioritize using project native variables. When you really need to customize a variable, explain its author's agreed nature, definition location and purpose, and prompt the source nearby each time it is reused. Avoid making the author's path tests, temporary interpreters, or experimental environments mandatory for readers.

Keep complete line breaks, quotation marks, indentation, line continuation characters and comments within a code area. Step-by-step paging can only be split at the operation boundary; the complete executable script also provides an openable supporting file and text anchor. Color matching relies on rich text in the same frame, not splitting into multiple word text boxes. Screenshots are for observation only.

## Examples of compilation and new support

To compile the example, first confirm that the board does exist in the current source code, and introduce the chip, architecture, board target name, required dependencies, applications, complete commands and observable products. The newly created virtual board in the official tutorial cannot pretend to be supported in the current tree.

New development boards/chips adopt a comparable official style: the original files of the reference board correspond to the new files one by one, explaining the reasons and discovery chain for each change, and then gradually adding hardware identities, device trees, startup and drivers. Readers should understand how modifications allow their goals to enter the build and cannot just download the completed results.

When there is a "new practice board" and an "actual target board for this time", clearly define the division of labor between the two and bring them both into the route. The success of QEMU or the official reference board cannot be written as the actual measurement success of the target board.

## Cold reading acceptance

Re-read from the first operation without relying on the implicit knowledge in the author's mind: can you find the file currently mentioned; can you identify the command or configuration; can you explain the basis for choosing this version; can you connect the input to the reader and the output; can you determine whether it was not downloaded, not found, not included in the build, or running abnormally after failure.

If readers still need to search the entire repository, guess file sources, or splice screenshots by themselves, fix the text. Filling in a variable table, posting a bunch of official links, or claiming "the video will tell you" cannot replace this fix.

---

> **Language / 语言** · [← 简体中文](teaching-and-evidence.md) · **English (current)**
