---
name: build-technical-ppt
description: "Make, rewrite, split and repair technical tutorial PPT for beginners, and synchronize the supporting Markdown. It is suitable for engineering environment, tool chain, source code architecture, interface, driver and experimental explanation, emphasizing copyable commands, source basis, Mermaid diagram, semantic color matching, manual modification retention and native acceptance. It is used when the user requires making PPT according to personal technical tutorial specifications; it is not automatically applied when editing Markdown, general business reports or marketing presentations."
---

# Technical tutorial PPT production

[简体中文](SKILL.md) | **English**

Use this English version and its English references for English-language tasks. Respond in the language requested by the user.

Let readers understand the relationship, follow the demonstration and review through PPT, and complete experiments independently through supporting Markdown. Readers have a foundation in programming and may be new to the current topic. Variable tables, command stacks, glossaries, or official links cannot be used in place of explanations.

This skill summarizes the production requirements that users have repeatedly confirmed in the Zephyr tutorial. The user's current instructions and the latest saved manuscript shall prevail; project-specific facts do not generalize to regulations for all projects. Do not turn skills into additional approval steps, nor do you only deliver specifications, sample chapters or inspection reports because there are many rules.

## Choose your current working style

- **Typesetting or color matching only:** Keep the technical content, code, screenshots, notes and diagram meanings, and fix the layout and visual classification. Don't rewrite textbooks casually.
- **Structure or split:** Inventory existing units of information, move them by complete topic, retain premises, branches, and experiments, and synchronize numbering with all references.
- **Supplement or rewrite:** When users say "can't understand" or "didn't explain clearly why", fix the actual explanation chain and examples. Merely adding legends, sources or remarks does not count as a solution.

First check the target absolute path and the Git root directory to which it belongs. The user-specified path takes precedence over the old copy saved by the application; if there is a conflict, please explain first and cannot continue in the old directory with the same name. Read the applicable AGENTS.md, current directory description, supporting MD, PPT and generation/reconstruction entry, and check for uncommitted modifications.

When actually making PPT, if the current environment provides the `presentations:Presentations` skill, reading it at the same time is responsible for native file operations, tool selection and verification; this skill is responsible for teaching quality and user style. There is no requirement to start the PPT author tool when only summarizing rules. The dependency path is found from the current skill directory and running environment, and a certain cached version path cannot be copied.

## Read reference by task

- Create, supplement or rewrite content: Read [explanation, basis and executable examples](references/teaching-and-evidence_en.md).
- To create, rearrange, color or add graphics: read [icon, color, cover and footer](references/visual-language_en.md).
- Modify existing files, split, synchronize and deliver: Read [preserve modifications, synchronization and acceptance](references/revision-and-delivery_en.md).
- The current task belongs to the Zephyr + UCRT64 tutorial: Rereading [Zephyr Project Conventions](references/zephyr-profile_en.md). Other projects do not load their drive letters, versions, commands and chapter numbers.

## Basic Contract of Arrangement and Explanation

1. Start with a real application or a problem at hand for the reader, first establish objects and responsibilities, and then talk about inputs, mechanisms, actions, and observations.
The text must allow readers to understand and operate it without opening the quotation; the source code must be verified by the author, the rules refined, and then explained thoroughly in the text. Links, filenames, and "read the source yourself" are not substitutes for explanations. When correcting, check the erroneous relationship between the existing text and the PPT at the same time, and do not just add a page of correct conclusions.
2. Each core theme is independently divided into modules, explaining the pre-input, current tasks, completed products and subsequent entrances. The general architecture is explained separately, and the specific modules describe their own models after reviewing the relevant interfaces. When there is a lot of content, split it up reasonably and don’t end by reducing the font size, omitting premises, or condensing it into an outline.
When the user sets an upper limit on the number of pages, first allocate the number of pages (including covers) according to core issues, merge duplicate concepts, and leave detailed troubleshooting and advanced branches in MD; the upper limit cannot be regarded as a goal that must be filled. When merging another PPT, first extract its complementary relationships, examples and basis, instead of splicing the two contents sequentially.
3. Markdown writes complete explanations, branches, operations, output judgments and recovery; PPT focuses on relationships and key actions in the same order. You cannot paste the entire MD page into PPT, nor can you hide the execution prerequisites in notes. When the user does not request or the project does not have a supporting MD, it will not be expanded to a complete set of books out of thin air.
4. Each operation describes the system, terminal, working directory, prerequisites, complete actions, observable results, and return points after failure. The first use of each file indicates its origin, when it should exist, and who generated it.
5. Engineering access is explained from the user side first: who gives the input, who reads it, how to find it, what to generate, and how to participate in the construction. You cannot jump from "File Existence" to "Project Automatic Identification", nor can you only describe the internal structure of the package without explaining the external call entry. The architecture explanation must distinguish interface responsibilities, implementation reuse scope, instance configuration and source code maintenance boundaries; the directory location itself cannot prove layering or versatility. First explain the reasons for selecting the component and the responsibility for the alternative route before requesting the download.
6. The key conclusions give the immediate official description entrance, repository document path and implementation positioning. Explain the specific site and entrance of the web page. Don't just write "Search Repositories". The basis must be verifiable, and understanding cannot rely on readers to search the entire repository first.

## The basic contract between vision and editing

- Keep the current cover, speaker, screenshots, annotations, manual color matching and layout adjustments. Back up the latest save before modifying; old generators cannot overwrite new content.
- Variables/parameters, files/paths, interface functions, and terminal commands are colored separately. Similar objects are consistent in the text, code, and figures, and the legends and text jointly explain the categories; see the visual reference for specific colors.
- The code uses a continuous, editable native text area, colored by rich text, and cannot be broken into word text boxes, pictures, or non-executable omitted fragments. Long operations leave intact the copied text material that can be opened.
- Multi-line text in text, code, tables and figures uses 1.2x line spacing by default, using real paragraph spacing properties, without fixed point size or blank line simulation. The white space between paragraphs is controlled separately, and overflow and adjacent objects are reviewed after adjustment; the font size cannot be reduced or pressed back to single size for the included content. The title, cover, and single-line footer retain the series layout. See the visual reference for specific implementation.
- Use mind maps, flow charts, and sequence diagrams according to relationships; keep the numbering of stage diagrams consistent with the current position. The supporting MD retains the Mermaid source, and the PPT retains the maintainable illustration. Figures should answer specific questions and are not a substitute for causal explanations.
- Consider text color and background in pairs, check for light and dark reading; fixing a light background but letting the text follow a dark theme is a known failure pattern. MD does not hardcode the text color of PPT.
- The personal series uses the master non-text footer signature, the text automatic page numbering is unified in the lower right corner, and the cover retains the speaker and does not display the page number. It must not fall back to a large diagonal watermark covering the main text. New brands, other authors follow their current template.

## Completion conditions

Follow [Acceptance Process](references/revision-and-delivery_en.md) to check beginners’ understanding, technical basis, command text, visual rendering and file integrity respectively. At least answer: Does the reader know what to do, why to do it, where to do it, who reads the input, where to look for success, and how to continue or resume safely.

Formal documents, supporting MD, notes, navigation, command materials and reconstruction sources are synchronized according to the scope of this impact. Valid export does not mean that PowerPoint has no repair prompts, successful rendering does not mean that the experiment has passed, and the old build log does not mean that the current round of actual measurement. Describe the true scope of verification and do not replace page-by-page reading with automated checks.

When encountering global feedback, implement it into all affected official materials; you cannot just modify the rules or dialogue responses. When the same problem occurs again, check the current round of execution and acceptance omissions, and do not blame the lack of execution of existing rules on skills.
