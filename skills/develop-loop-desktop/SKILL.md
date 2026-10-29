---
name: develop-loop-desktop
description: "审查、开发、重构、安全加固、测试或记录 F:\\git_storage\\linux-note\\tools\\practice_tool 中的 Loop Markdown 桌面工作台。适用于继续 Loop Electron/TypeScript/C++ 开发、修改 IPC 或 Native Service、调整资源管理器/编辑器/预览/保存架构、更新实现状态及退役旧浏览器练习原型。"
---

# Loop 桌面工作台开发

> **语言 / Language** · **简体中文（当前）** · [English →](SKILL_en.md)

For English-language tasks, follow [the English instructions](SKILL_en.md) and their English references. Respond in the language requested by the user.

## 以当前架构为基础

1. 阅读项目 `AGENTS.md`、根目录 `README.md` 和 `tools/practice_tool/docs/architecture/implementation_status.md`。
2. 阅读正在修改的实现状态条目所指定的权威文档。以已接受的 ADR 和当前产品、工程文档为实现基线。
3. 提议或修改前检查 `git status`、相关代码、测试、依赖清单和真实调用关系。
4. 将根目录浏览器 `src/`、`banks/`、IndexedDB 和 Bash 生命周期视为待退役的 `0.1.0` 原型。不得从其导入实现，也不增加兼容、转发、双写或回退服务。

## 先解决设计，再编写代码

1. 从 `implementation_status.md` 选择下一个明确的里程碑或验收关卡，不另建并行路线图。
2. 需求、所有权、协议、状态转换、失败行为或验收标准缺失或矛盾时，更新权威设计；属于架构决策时新增或替代 ADR。
3. 检查进程所有权、能力授权范围、路径与文件身份、数据所有权、取消、过期结果、错误恢复、资源边界、跨平台行为和可测试性。
4. 设计不再把重大待决事项留给实现者后，才开始实现。

## 干净实现

- 除非开发者明确要求迁移，否则按最新目标架构实现，不保留历史兼容逻辑。
- Main 负责 Electron 生命周期和对话框；Native Service 负责文件系统能力授权及持久化文档服务；Renderer 负责 UI 和内存编辑状态；workers/frames 负责不可信渲染。
- Renderer 保持沙箱隔离，不接触路径。提供固定、强类型、经运行时校验的用例 API；拒绝通用 IPC、路径、URL、命令和未知字段。
- 项目自有文件、标识符、对象字段、IPC 字段及协议字段使用英文 `snake_case`；仅在语法要求时保留框架规定的上游名称。
- 遇到过期的能力凭证、身份变化、链接、边界逃逸、畸形输入、超限负载或不支持的写入语义时，拒绝操作，保持安全关闭。
- 让状态可见且明确区分：Dirty 不代表已保存，已备份不代表已保存，已发送请求不代表成功，过期异步任务不得覆盖当前状态。
- 不跟踪构建产物、本地状态、绝对路径、秘密信息及包含 Markdown 正文的诊断记录。

## 验证并报告证据

1. 在能够复现行为的最低层增加回归测试，再为跨进程流程补集成或冒烟覆盖。
2. 运行桌面 TypeScript 测试与构建、Native CMake 构建与 CTest、适用的冒烟/安全/审计检查、旧原型仍存在时的回归检查，以及 `git diff --check`。
3. 根目录 `format.sh` 仅使用仓库支持的 Bash 环境；环境不可用时记录具体限制，不替换为 Git Bash 或声称已通过。
4. 审查完整差异中的旧实现导入、绝对路径、协议偏移、无界分配、缺失的运行时校验、生成产物和不准确文档。
5. 只根据实际观察的命令与证据更新 `implementation_status.md`；未验证的平台或发布关卡继续保持未完成。
6. 未经用户明确要求，不暂存、提交、推送、安装系统运行时、删除旧数据或用户数据，也不更新记忆。

---

> **语言 / Language** · **简体中文（当前）** · [English →](SKILL_en.md)
