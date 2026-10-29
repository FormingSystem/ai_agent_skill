# 格式基准与可生成的手册

> **语言 / Language** · **简体中文（当前）** · [English →](format_and_manual_en.md)

本页在接入格式化或文档构建时读取。设计与长度约束见 [技能主指令](../SKILL.md)。这里的工具只验证各自边界，不自动证明 Clean Code、对象设计或高复用。

## 格式快照来源与应用

[cpp.clang-format](../assets/cpp.clang-format) 来自用户于 2026-10-29 提供的同名文件。原始字节的 SHA-256 为 `3b28a88974a4088a898fd503b419e6c278105b26a59ea58dcae7e922b3b80d86`；随包版本仅规范换行与行末空白，不改变配置值。本仓库维护分发快照，后续更新先与用户指定来源比较并复核，不能自动用未知外部副本覆盖。使用者不依赖提供者的机器盘符。

配置采用 WebKit 基础样式，4 空格缩进、禁用 Tab、不重排 include、指针与引用左对齐，并对函数、类、控制语句使用不同的花括号规则。clang-format 18.1.8 已能解析；其他版本必须自行验证，不能忽略未知选项后声称应用了完整规范。未显式设置的行为来自该版本的基础样式，应固定项目工具版本，避免升级悄悄改变排版。

自有新项目可把快照复制为项目根目录的 `.clang-format`，记录来源并纳入版本管理。已有项目先检查生效配置、子目录覆盖和受影响文件，按本次范围合入，不覆盖无关设置。以下命令均从 **目标项目根目录** 执行，路径替换为真实待检查文件：

```bash
# 当前目录：目标项目根目录，已经存在 .clang-format。
clang-format --version
clang-format --style=file:.clang-format --dump-config
clang-format --style=file:.clang-format --dry-run --Werror src/device.cpp
```

需要应用格式时，仅处理本次授权文件，再审查差异：

```bash
# 当前目录：同一目标项目根目录。
clang-format --style=file:.clang-format -i src/device.cpp
git diff --check
git diff -- src/device.cpp
```

快照中的 `QualifierAlignment: Right` 会调整限定符位置，须结合宏、类型别名及编译结果审查语义，不能把所有格式差异当作纯空白。`AllowShortFunctionsOnASingleLine: All` 保留用户原值；多语句压行仍受主指令禁止。clang-format 不检查 snake_case、函数执行行数、文件拆分、资源所有权或复用质量，这些必须另行审查。

## Doxygen 的契约位置

使用 `/** ... */` 文档块和 `@` 命令；短成员说明可用 `/**< ... */`。文件用 `@file` 说明职责，模块用 `@defgroup`、`@ingroup` 建立归属，接口用 `@brief`、`@param`、`@return` 或 `@retval` 记录真实契约。按需补充 `@pre`、`@post`、`@note`、`@warning` 与 `@see`，不把所有标签机械填满。

下例是接口注释模板，函数行为必须由真实实现兑现；它不是已实现的驱动，也不允许凭示例编造返回码：

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

声明处说明调用者可依赖的行为，实现处说明算法、状态转换及资源处理原因。字段注释要写单位、有效范围与所有者，而非重复字段名。接口变化时同步契约与相应示例；不通过开启全量提取掩盖缺失注释。

## 手册构建入口

[doxyfile](../assets/doxyfile) 是自有项目的最小配置模板。项目已有 Doxygen 或 Zephyr 文档构建时复用原入口；没有时复制到项目合适的文档目录，按实际情况填写项目名、输入目录及输出语言。模板假设从项目根目录运行且存在 `include`、`src`，输出到 `build/docs`；只扫描真实的自有源码与文档，不把整个工作区或依赖目录当输入。输出目录按项目规则忽略，不提交生成缓存。

```bash
# 当前目录：目标项目根目录；模板已配置为 docs/doxyfile。
doxygen --version
mkdir -p build/docs
doxygen docs/doxyfile
```

上例使用 Bash，先显式创建输出目录；PowerShell 中将创建目录一行替换为 `New-Item -ItemType Directory -Force build/docs`。

成功后打开 `build/docs/html/index.html`，检查模块导航、类型与成员、参数方向、错误返回和交叉链接。模板将文档警告视为错误，保留未文档化检查；修复告警的真实原因，不用关闭检查换取绿色结果。不要只检查进程退出码：必须确认预期接口实际出现在正确模块中。HTML 成功不代表 PDF 手册或实板程序已经验证。

## 与上游风格的边界

- [Linux coding style](https://www.kernel.org/doc/html/latest/process/coding-style.html) 是内核贡献风格来源，不能用用户的 4 空格配置声称满足其 8 列 Tab 缩进要求。
- [Zephyr coding style](https://docs.zephyrproject.org/latest/contribute/style/index.html) 与 [Doxygen style](https://docs.zephyrproject.org/latest/contribute/style/doxygen.html) 用于目标项目的版本化核对；真实上游任务继续使用该版本的配置、模块分组和验证入口。
- [Linux kernel-doc](https://www.kernel.org/doc/html/latest/doc-guide/kernel-doc.html) 是另一套注释语法。自有项目默认遵守本次 Doxygen 要求；维护原有内核注释时不混入不被其构建链支持的标签，也不把 kernel-doc 冒称为 Doxygen 验证结果。
- [Clang 格式选项](https://clang.llvm.org/docs/ClangFormatStyleOptions.html) 和 [Doxygen 文档块](https://www.doxygen.nl/manual/docblocks.html) 用于核对已安装版本的配置与语法。网页 latest 内容可能变化，项目交付记录实际工具版本。

---

> **语言 / Language** · **简体中文（当前）** · [English →](format_and_manual_en.md)
