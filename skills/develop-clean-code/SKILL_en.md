---
name: develop-clean-code
description: Write, refactor, or review code using the user's snake_case, Clean Code, short-function, reuse, object-oriented design, and Doxygen requirements, primarily for C/C++ and embedded systems. Use when applying the user's clang-format configuration, Linux kernel or Zephyr engineering style, a 50-line executable-code limit per function, and a 2000-line file limit unless necessary; not for ordinary prose editing or implicit repository-wide refactoring.
---

# Develop clear and maintainable code using the user's conventions

> **Language / 语言** · [← 简体中文](SKILL.md) · **English (current)**

Integrate naming, responsibilities, state ownership, error handling, and documentation comments that can produce a manual. Formatting checks do not establish design or behavioral correctness. Use these instructions for English-language tasks.

## Establish the target and convention sources

- Verify the target project's full path, Git root, contributor rules, language, build process, and authorized scope. Preserve unrelated uncommitted work. The skill directory is not the target project root.
- Read the effective project formatting configuration and actual modules before selecting the baseline for the current request. For project-owned code, use the user's clang-format configuration; the bundled [format configuration](assets/cpp.clang-format) is a portable snapshot. See [Formatting and manual generation](references/format_and_manual_en.md) for usage and provenance. Checking that a file exists is insufficient; do not silently substitute the tool's default style.
- The user's configuration derives from WebKit, uses 4 spaces, and disables tabs; do not describe that layout as native Linux kernel formatting. Draw on kernel and Zephyr practices for clear interfaces, explicit lifetimes, layering, and error paths without conflating all their rules. When modifying actual upstream code, identify differences from the user's preferences and resolve their application using the explicit request and target contribution rules; do not overwrite the entire upstream formatting or documentation system.

## Naming and Clean Code

- Use English `snake_case` for project-owned files, directories, namespaces, types, classes, functions, methods, variables, members, and protocol fields. Macros and constants may use `UPPER_SNAKE_CASE`. Do not switch class names to `PascalCase` or ordinary project-owned interfaces to `camelCase`.
- Preserve names required by language syntax, operating systems, or third-party contracts, including overrides and external ABIs. Identify these boundaries without extending exceptions to a framework's customary style. Renaming must update actual callers, build entry points, serialized fields, and documentation without mechanically breaking external contracts.
- Give each function one nameable action and each module one cohesive responsibility. Names should express domain objects and actions, with booleans expressing conditions. Avoid obscure abbreviations, magic numbers, hidden side effects, and large blocks of commented-out implementation.
- Control nesting through clear conditions, early returns, and layered interfaces while releasing acquired resources on every exit path. Use centralized cleanup labels in C and RAII in C++ as appropriate to the environment; do not duplicate cleanup merely to prohibit jumps formally.

## Function and file length

Every function, method, constructor, destructor, and lambda must contain **at most 50 lines of executable code**. Count physical lines containing code in the formatted body, including declarations and initialization, conditions and loops, calls, returns, error cleanup, macro invocations, and code in conditional-preprocessor branches. Exclude the signature, blank lines, comment-only lines, and lines containing only braces. Count every code-bearing line of a multiline expression. Check nested lambdas independently as well; they cannot conceal an oversized enclosing body.

- Do not pack multiple statements onto one line or evade the limit through macros or meaningless forwarding functions. Formatter support for short one-line functions does not permit compressing complex logic.
- When the limit is exceeded, extract meaningful private methods or helpers around independent responsibilities, state phases, or resource boundaries. Pass required state explicitly through parameters or object members rather than introducing globals to shorten functions.
- Code files should contain at most **2000 physical lines**, including comments and blank lines, unless a larger file is necessary. Split interfaces and implementations along cohesive module boundaries and update builds, includes, and documentation groups. Do not arbitrarily slice files or remove necessary comments to meet the count.
- For a necessarily larger file, record its path, actual line count, concrete reason it cannot reasonably be split, and maintenance approach. Identify the provenance and generation entry point for generated or third-party files. Do not edit generated output by hand or exempt ordinary business code through this exception. Do not relax the 50-line rule on your own.

Use existing syntax-aware project tools to locate candidates, then verify actual function boundaries and the counting convention above. Plain line counts, regular expressions, and statement counts do not measure executable lines per function equivalently. Without a reliable tool, review each affected function and record the results rather than claiming repository-wide automated verification.

## Object-oriented design and reuse

- Identify each object's state, behavior, lifetime, and invariants before choosing interfaces. Objects own their state and maintain valid states through public operations; merely renaming scattered globals and procedural functions is not object-oriented design.
- In C, organize objects through structure instances, explicit instance parameters, and module interfaces, hiding implementation where needed. Introduce operation tables and function pointers only for actual multiple implementations or replaceable backends. In C++, encapsulate invariants with classes and resource ownership with RAII; prefer composition and use inheritance for genuine substitution. Do not migrate kernel or Zephyr C code to C++ merely to use classes.
- Search existing libraries, shared modules, and callers before adding code. Consolidate stable duplication with the same semantics into one implementation, placing platform differences behind clear adaptation boundaries. Do not create parallel implementations by copying and renaming.
- Base reuse on real needs. Do not merge different contracts because a few lines look alike, or invent universal base classes, plugin systems, or frameworks for nonexistent callers. Avoid stateless utility classes containing only static functions.
- Make borrowing versus ownership, initialization versus destruction, thread versus interrupt context, locks and shared state, and object states after success or failure explicit. Keep dependencies testable and directional; reusable layers must not depend back on specific business logic.

## Doxygen comments and manuals

Use Doxygen documentation comments for project-owned files, interfaces, types, fields, enums, and nontrivial internal functions. Write explanations in Chinese by default while preserving real identifiers. Document purpose, parameter directions and constraints, units, nullability, return values and errors, ownership, and lifetime. Explain concurrency, blocking, interrupt restrictions, and failure side effects according to the actual contract. Necessary inline comments explain reasons and invariants rather than paraphrasing syntax.

Maintain one authoritative contract at the interface declaration and explain implementation decisions at the definition; avoid duplicate parameter documentation that can drift. Use module groups, pages, examples, and links so output works as a manual rather than a list of function names. Follow [Formatting and manual generation](references/format_and_manual_en.md) to use the Doxygen template and validate output. Linux kernel-doc and Doxygen differ; do not mix their syntax and claim both generation paths have been verified.

## Delivery verification

1. Review naming, executable lines per function, total file lines, responsibility boundaries, actual reuse points, and object lifetimes within the change. Explain necessary file-length exceptions.
2. Run formatting checks with the selected configuration and verified tool version, inspect formatting changes, then run appropriate compilation, static checks, and tests. Cover failures, rollback, and boundaries when resources or state transitions change.
3. Generate documentation and inspect diagnostics and rendered module entry points, type members, parameters, return values, and cross-references. If tooling is unavailable, report that the manual build is unverified; comment syntax alone does not establish successful generation.
4. Inspect staged changes and deliver only the authorized scope. Reuse the target project's commit, synchronization, and release processes; invoking this skill does not itself authorize commits, pushes, or publication.

---

> **Language / 语言** · [← 简体中文](SKILL.md) · **English (current)**
