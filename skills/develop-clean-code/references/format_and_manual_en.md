# Formatting baseline and generated manuals

> **Language / 语言** · [← 简体中文](format_and_manual.md) · **English (current)**

Read this page when integrating formatting or documentation builds. See the [skill instructions](../SKILL_en.md) for design and length constraints. Each tool verifies its own scope, not Clean Code, object design, or reuse quality automatically.

## Formatting snapshot provenance and use

[cpp.clang-format](../assets/cpp.clang-format) comes from the same-named file provided by the user on 2026-10-29. The original bytes have SHA-256 `3b28a88974a4088a898fd503b419e6c278105b26a59ea58dcae7e922b3b80d86`; the bundled version only normalizes line endings and trailing whitespace, without changing values. This repository maintains the distributed snapshot. Review later updates against the user-designated source rather than automatically overwriting it from an unknown external copy. Consumers do not depend on the provider's machine drive letters.

The configuration derives from WebKit, uses 4-space indentation, disables tabs and include sorting, aligns pointers and references to the left, and applies distinct brace rules to functions, classes, and control statements. clang-format 18.1.8 can parse it; verify other versions rather than ignoring unknown options and claiming full application. Unspecified behavior comes from that version's base style, so pin the project tool version to avoid unnoticed formatting changes during upgrades.

For a new project-owned codebase, copy the snapshot to the project root as `.clang-format`, record its provenance, and track it in version control. In existing projects, inspect the effective configuration, subdirectory overrides, and affected files before integrating it within scope; preserve unrelated settings. Run the following from the **target project root**, replacing the example path with an actual file:

```bash
# Working directory: the target project root, with .clang-format already present.
clang-format --version
clang-format --style=file:.clang-format --dump-config
clang-format --style=file:.clang-format --dry-run --Werror src/device.cpp
```

Apply formatting only to authorized files and inspect the changes:

```bash
# Working directory: the same target project root.
clang-format --style=file:.clang-format -i src/device.cpp
git diff --check
git diff -- src/device.cpp
```

The snapshot's `QualifierAlignment: Right` moves qualifiers; review semantics alongside macros, type aliases, and compilation results rather than treating every change as whitespace-only. `AllowShortFunctionsOnASingleLine: All` preserves the user's setting, but the main instructions still prohibit packing multiple statements onto one line. clang-format does not check snake_case, executable lines per function, file decomposition, resource ownership, or reuse quality; review those separately.

## Where Doxygen contracts belong

Use `/** ... */` documentation blocks and `@` commands; brief member comments may use `/**< ... */`. Describe file responsibilities with `@file`, module membership with `@defgroup` and `@ingroup`, and actual interface contracts with `@brief`, `@param`, and `@return` or `@retval`. Add `@pre`, `@post`, `@note`, `@warning`, and `@see` where useful rather than mechanically filling every tag.

The following interface-comment template describes behavior that an actual implementation must provide. It is not an implemented driver and does not authorize inventing return codes. Its explanatory comments remain Chinese, following the default source-comment convention:

```c
/**
 * @brief 将一帧数据复制到发送队列。
 * @param[in,out] channel 已初始化且由调用方持有的通道，不能为 NULL。
 * @param[in] data 帧内容，不能为 NULL；返回后调用方可复用此缓冲区。
 * @param[in] size 帧字节数，范围为 1 到通道约定的最大帧长。
 * @retval 0 数据已入队，不代表硬件已发送完成。
 * @retval -EINVAL 参数无效，队列保持不变。
 * @retval -ENOSPC 队列空间不足，本次没有入队。
 * @note 此接口不等待空闲空间；调用方必须串行化对同一通道的访问。
 */
int channel_enqueue(struct channel* channel, unsigned char const* data, size_t size);
```

Document caller-visible guarantees at declarations and explain algorithm, state-transition, and resource-handling decisions at definitions. Member comments should specify units, valid ranges, and ownership instead of repeating identifiers. Update contracts and examples when interfaces change; do not enable extraction of everything to disguise missing comments.

## Manual build entry point

[doxyfile](../assets/doxyfile) is a minimal template for project-owned code. Reuse existing Doxygen or Zephyr documentation builds when present. Otherwise, copy it into an appropriate project documentation directory and configure the actual project name, inputs, and output language. The template assumes execution from the project root with `include` and `src` directories, writing to `build/docs`. Scan actual project-owned source and documentation rather than the entire workspace or dependencies. Ignore generated output according to project rules and do not commit caches.

```bash
# Working directory: the target project root; the configured template is docs/doxyfile.
doxygen --version
mkdir -p build/docs
doxygen docs/doxyfile
```

The example uses Bash and explicitly creates the output directory first. In PowerShell, replace that directory-creation line with `New-Item -ItemType Directory -Force build/docs`.

After a successful build, open `build/docs/html/index.html` and inspect module navigation, types and members, parameter directions, error returns, and cross-references. The template treats documentation warnings as errors and retains undocumented-entity checks. Fix their causes rather than disabling checks for a passing result. Verify that expected interfaces appear in the correct module instead of relying only on the exit code. Successful HTML generation does not validate a PDF manual or a program on hardware.

## Boundaries with upstream styles

- [Linux coding style](https://www.kernel.org/doc/html/latest/process/coding-style.html) governs kernel contributions; the user's 4-space configuration cannot be claimed to meet its 8-column tab indentation requirement.
- [Zephyr coding style](https://docs.zephyrproject.org/latest/contribute/style/index.html) and [Doxygen style](https://docs.zephyrproject.org/latest/contribute/style/doxygen.html) inform checks against the target project's version. Actual upstream tasks continue using that version's configuration, module groups, and validation entry points.
- [Linux kernel-doc](https://www.kernel.org/doc/html/latest/doc-guide/kernel-doc.html) has a different comment syntax. Project-owned code defaults to the requested Doxygen convention. When maintaining existing kernel comments, do not add unsupported tags or report kernel-doc results as Doxygen validation.
- [Clang formatting options](https://clang.llvm.org/docs/ClangFormatStyleOptions.html) and [Doxygen comment blocks](https://www.doxygen.nl/manual/docblocks.html) help verify configuration and syntax for installed versions. Latest webpages can change; record the actual tools used for delivery.

---

> **Language / 语言** · [← 简体中文](format_and_manual.md) · **English (current)**
