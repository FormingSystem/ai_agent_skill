# Illustrations, colors, covers and footers

> **Language / 语言** · [← 简体中文](visual-language.md) · **English (current)**

## Keep existing designs

First look at the latest saved PPT and the original manual color marking, and then make modifications. The created series cover, screenshot annotation, font size level and semantic color are input constraints and are not decorations that can be reset with the old generator. When adjusting only the color, keep the text, paragraphs, shape geometry and notes; when rearranging is required, adjust it based on the actual overflow and reading order.

The main text should select text, comparison tables, codes or diagrams according to the explanatory content, and do not mechanically arrange each page into cards. Command, interface, and relationship diagrams remain editable. Long pages should be split into complete questions first, and all content cannot be squeezed out by reducing font size.

## 1.2x line spacing and white space between paragraphs

The multi-line text in the text, code, tables and figures of personal technical tutorials should be uniformly spaced **1.2 times**. In PowerPoint, it corresponds to "Paragraph → Line Spacing → Multiple → 1.2", which is a paragraph attribute. It does not mean that the font size is multiplied by 1.2 and then changed to a fixed point size. During program processing, confirm that the final PPT saved is indeed 120% line spacing, for example, the `a:lnSpc/a:spcPct` value of DrawingML is `120000`, and review it in the native application.

Line spacing and distance before/after paragraph are controlled separately. Use paragraph spacing between logical paragraphs of text, calibrated on a page basis starting at 12 pt; do not rely on blank paragraphs for support. To repair old manuscripts, you can replace purely typesetting empty paragraphs with paragraph spacing, and retain the order and text of non-empty paragraphs. Blank lines, indents, and line breaks in the code have structural significance and should be kept intact, with only the line spacing changed.

First retain the original font size, text color and alignment, then check the height of the text box, the blank space of the nodes in the image, the height of the table row and the distance from the source link/footer. Adjust the frame height and object spacing when necessary. If the content is still too much, split the page according to the complete operation or relationship; do not reduce the line spacing, reduce the font size, and do not delete necessary explanations to eliminate overflow. The center label in the picture needs to check the actual text boundary, not just the shape boundary.

The cover, title, single-line stage label, source link, signature and page number follow the existing series layout; newly added multi-line titles are also prioritized 1.2 times and checked separately. Markdown does not have uniform line spacing settings across readers, does not insert HTML, blank lines, or modify the user's global theme for synchronizing PPT.

## Semantic color matching of technical objects

The following are the confirmed color combinations of the user's personal technical tutorial under light-colored canvas; if there is an updated and clear design for existing materials, they will be retained first and processed according to current requirements.

| Object | Color Value | Example |
| --- | --- | --- |
| Variables, parameters, configuration fields | Dark orange `#B84E00` | `BOARD`, `ZEPHYR_SDK_INSTALL_DIR`, `-D`, `cmake-ext` |
| File, path | Blue `#0070C0` | `CMakeLists.txt`, `module.yml`, `samples/hello_world` |
| Interface functions, build language commands/macros | Dark green `#087B3D` | `find_package`, `target_sources`, `zephyr_get` |
| Terminal command | Purple `#A02B93` | `cmake`, `west`, `export` |
| General description | Dark `#29263B` | Consecutive text |
| Auxiliary tags, footer | Gray `#646173` | Legend guide, signature |

Provide a small legend the first time it appears and do not require it to be repeated on every page. The same object remains consistent in text, code, and figures, but the entire section is not colored; links retain a recognizable underline style. Color is auxiliary information, text still describes the object type, and the conclusion cannot be lost in grayscale reading.

Judging from the context, you cannot just do full-text regular replacement: `cmake` can be a directory or command; `Kconfig` can be a file or configuration system; `cmake-ext` is a complete field; `west zephyr-export` is a command combination; the fragment of the same name of the function in the path is still the path. Complete paths are colored overall, and variables and their values ​​are not forced into the same category.

Use rich text fragments in the same text box to color, without changing the text content of the command and source code. When adjusting the color of an existing document, compare the paragraph text before and after exporting to prevent spaces, line breaks, or quotation marks from being lost after splitting and running.

## Draw abstract relationships clearly

| Relationships to explain | Suitable diagrams | Highlights to check |
| --- | --- | --- |
| What parts does the system consist of | Mind map, hierarchy diagram | Classification levels and responsibilities of each part |
| How a task is completed | Flowchart | Input, processing sequence, branches and products |
| Who calls whom first, what is passed, what is returned | Sequence diagram | Calling direction, stages and execution boundaries |
| Which step of the total experiment we are currently in | Stage diagram | The same number, current stage, and products before and after |
| What are the differences between the two routes | Parallel processes or tables | Same inputs, different actions, results and conditions |

The question to be answered is explained before the diagram, and the key connections are explained after the diagram. The process arrows must have real sequence or dependency meaning; the sequence diagram distinguishes between script calls in the same process and independent process tools, and each file cannot be drawn as a service. Don’t just pile up all the graphics randomly to satisfy “having a picture”.

MD saves the Mermaid source first, and PPT synchronizes its graphics and stages. When the user requires an editable graph, use native editable nodes and connections; when using a rendered graph, the source file is still retained, and the nodes in the graph cannot be claimed to be directly editable. Text-dense Mermaid diagrams are broken down in reading order to ensure readability at the final viewing size.

## light and dark theme

Markdown text, inline code, and syntax highlighting follow the reader theme by default and do not inject fixed HTML colors. Mermaid stage highlighting prioritizes borders and line widths to avoid locking only light-colored fills while retaining light text in dark themes.

When custom coloring is necessary, set foreground and background in pairs, and review all branches, labels, and edges. Render light and dark themes respectively, and check the HTML tag/SVG text differences of the readers used. The fixed canvas of PPT is used for color testing independently, and dark theme screenshots are not directly copied. Contrast measurement aids judgment and cannot replace visual inspection of the final image.

## Cover, signature and page numbers

The personal series retains the user-selected background cover and speaker `lizhaojun`. The final agreement is that the horizontal footer signature of each page master should be placed in the non-text area, and the large diagonal watermark in the text should be cancelled. There is no page number on the cover, and the page number of the text is unified in the lower right corner, showing the actual slide serial number.

The master is located behind the normal page content, and images may cover it; the solution is to reserve a footer area and require text, images, codes, tables, and links to be avoided instead of raising the signature to the top of the text. Cover all actually used masters/layouts, and new pages will automatically inherit them; clean up duplicate signatures on ordinary pages, and check that no background graphics are hidden.

The existing dimensions of the 1280 × 720 personal series can be used as a reference for retention. Change the canvas and check the proportions without forcing these coordinates to other templates:

- Signature box: Left 64, Top 676, Width 150, Height 28; horizontally left aligned, vertically centered, Microsoft YaHei 13.5 pt, no borders/padding.
- The white background is signed `#646173`, the dark cover is signed `#D4CDE8`, and the text is opaque.
- Page number box: left 1140, top 676, width 76, height 28, right aligned, same font size as signature.
- Only turn off the spelling check for signatures; distinguish red spelling wavy lines, shape edges, and screenshot manual marks first. You cannot turn off full text proofreading or delete user comments by mistake for signatures.

Watermarks explicitly requested by other authors, other brands, and users are retained according to their templates and are not automatically added lizhaojun.

---

> **Language / 语言** · [← 简体中文](visual-language.md) · **English (current)**
