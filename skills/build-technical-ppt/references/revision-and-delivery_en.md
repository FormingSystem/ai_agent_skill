# Keep modifications, synchronization and acceptance

> **Language / 语言** · [← 简体中文](revision-and-delivery.md) · **English (current)**

## The latest saved draft is the baseline

Before modification, check the full path, Git root and current target file, record the target file summary and time, and back up the latest draft. Check the cover, screenshots, text color, notes, annotations, user-adjusted blank lines and graphic positions. Existing generators and native reconstruction sources may be lagging behind, and they cannot be up-to-date by default.

When a PPT is open with unsaved edits, read or take a safe copy from an available document session first; do not force close user documents. Only when it is true that the latest content cannot be obtained or the occupied file cannot be written, the specific obstruction will be explained. The modification authorization will not be confirmed again. Compare the initial summary again before saving the official draft; if the user saves it in the meantime, it will be merged with the new draft and cannot be overwritten directly.

Only style modifications are based on the original structure, retaining irrelevant media, relationships, notes, masters, and layers. Check relationship target, ID, content type, master/layout registration and XML element order when modifying OOXML directly; "ZIP can be unpacked" is not enough to guarantee that PowerPoint will not prompt for repair. Adopt the safe author process of currently available demonstration tools and do not solidify a temporary script or tool cache directory as a dependency.

## Split and sync

Independent topics use consecutive three-digit main serial numbers `P001`, `P002`, and `P003`. `P002_01` is not used to replace the new independent chapter. The platform process does not use the `_Windows` and `_Linux` file suffixes at the same time. According to the user's final agreement, they stay in the same topic directory and no longer separate entrances for the platform.

PPT and supporting MD have the same main file name; the text, slides, notes and supporting commands remain in the same stage. MD provides complete explanations and branches, while PPT focuses on key relationships and actions. If necessary, missing images can be extracted from PPT to text assets, and observation points and version/path descriptions can be added. Screenshots cannot replace commands.

Synchronize when splitting/renaming/adding or deleting pages:

- Official document name, cover, chapter and section numbers.
- Table of contents, outline, reading entry, stable anchor points and page range.
- PPT notes, source links, supporting command files and links to them.
- Natively rebuild sources, source manifests and existing build entries.

The experimental directory or constructed products will not be moved without authorization due to changes in chapter numbers. If necessary, the retained historical identification will be stated. Only the materials that are truly affected this time will be synchronized, and we will not extend the organization to irrelevant code or modify the style of the entire repository.

## different levels of acceptance

Select the corresponding inspection according to the modified content, and it is forbidden to equate passing a certain layer with passing all:

| Level | Evidence required |
| --- | --- |
| Explanation | Cold reading from the beginning, premise, object, cause and effect, action and result are continuous |
| Source | The current version of the document, official description and implementation location correspond to each other |
| Operation text | The commands after export/copy are continuous, and newlines, quotation marks, indents, line continuations and comments are retained |
| Illustrations and layout | Check 1.2x line spacing and independent paragraph spacing, render page by page for visual inspection, and make sure the graphics, colors, text, links, footers and page numbers are clear |
| Native file | Package relationship is valid; open normally with PowerPoint, no repair prompt, check native rendering |
| Synchronization | The supporting MD/notes/navigation are valid, and the content of the current official draft and the reconstructed draft are consistent |
| Experiment | Verify actual operation in an executable and authorized environment; clarify platform, version and untested scope |

Visual inspection goes beyond thumbnails: look at the full affected page, focusing on dense code, long paths, border text, any master footers, and light and dark theme graphics. Automatic bounds checking assists in detecting overflows and does not replace visual inspection. Simple color matching does not require re-burning or unrelated compilation.

If the native reconstruction is just a ZIP repackage, the contents of each part are compared instead of the entire package hash; the ZIP timestamp and ordering will change the entire package bytes. Confirm that the final delivery document is a verified document. You cannot verify the candidate and then write an unchecked official draft. Comply with delivery validation requirements when using user-specified formatting tools.

Existing workspaces, virtual environments, tools, and build directories are checked first and then reused. Deleting .west, uninstalling the environment, migrating Git history, or resetting the global configuration to prove that the command is correct is not allowed; when these actions are required, they are still processed according to the actual request and environment constraints, and are not deduced from the PPT editor's authorization.

## Delivery and review records

Complete the actual file modifications within the scope of authorization, and then briefly deliver the official file that can be opened. Don’t call “preparing for revision” or “having written the rules” as completion of revision. When the user requires all PPTs to be inventoried and processed, all affected documents cannot be delivered only as sample pages.

Save the maintenance records of "user comments, implementation location, and verification scope" and retain the source of the comments. Only update the repository AGENTS.md and write agreement and status documents when required by the project agreement; do not change global skills, irrelevant configurations or long-term memory without authorization. The skill creation/update itself occurs upon explicit user request.

Recording platforms that are not running, native acceptance that cannot be performed, and experiments that have not yet been verified cannot be used as the results of this round based on historical success. The author's test logs or native maintenance processes are not included in the PPT and notes for readers, and the maintenance records are left in the agreed location of the project.

---

> **Language / 语言** · [← 简体中文](revision-and-delivery.md) · **English (current)**
