---
id: agents
title: "AI_Agent_Skill_项目上下文"
kind: reference
status: maintained
domains:
  - repository
---

# 第1章\_AI_Agent_Skill_项目上下文

修改前核对用户指定的完整路径及 Git 根目录；默认使用当前打开的项目文件夹。路径冲突先说明，禁止在同名旧副本中继续操作。先读本文件、[README](README.md)、[信息架构](governance/architecture/repository_information_architecture.md) 和 [Git 规范](governance/conventions/git_guide.md)。

## 1.1\_职责与权威来源

本仓库集中维护自定义技能。`skills/` 是技能权威源，Codex 安装目录仅为运行镜像；修改先在仓库完成并验证，再显式同步。系统技能与第三方插件由其安装器维护，不纳入本仓库。不得提交缓存、凭据、日志或机器运行配置。

## 1.2\_文件管理

- 继承 linux-note 的职责分层、单一权威来源和相对链接原则，不创建无实际内容的目录。
- 仓库自有新文件、目录及代码标识符使用英文 `snake_case`，常量可使用 `UPPER_SNAKE_CASE`。技能包名称沿用其现有 `name` 和连字符命名；`SKILL.md`、`README.md`、`AGENTS.md`、`LICENSE`、框架要求的方法等保留契约名称。现有迁入资源保留原名以维持引用。
- 正式治理文档具有稳定 `id`、`title`、`kind`、`status`、`domains`，章节采用本文件的编号格式。技能 Markdown 是运行指令，保留原生格式，不套用知识正文元数据或章节编号。
- 引用尽量使用相对路径。移动、改名、拆分、删除后同步技能入口、注册表、文档和调用方，检查旧路径、缺失目标和重复 ID。
- 不随意删除既有材料。清理前查清调用关系和影响；安装镜像中的额外文件须先审查，不静默删除。
- 按最新需求干净重构，不增加旧入口转发、双实现或无人维护的兼容路径。确认数据所有权、外部调用和平台边界后再修改。

## 1.3\_编辑与验证

保持中文说明与中文代码注释；技术教学默认面向 C/C++ 开发者。这里复用 Python 审计和同步工具是既有工具链的工程需要，不改变教学语言偏好。修改技能时读齐关联参考资料，保持触发条件准确、步骤可执行、验证边界诚实，不凭自动检查宣称实际任务已通过。

运行 `python scripts/check_repository.py`、`python -m unittest discover -s scripts -p 'test_*.py'` 和 `git diff --check`。按改动运行对应技能脚本；安装后运行 `python scripts/sync_skills.py check`。无法运行的检查明确说明原因。

## 1.4\_Git_协作

远端主线沿用已有 `main`，仅接收验证通过的快进提交；任务分支默认 `codex/`。提交遵守 linux-note 的中文结果与条目明细格式，启用 `.githooks/commit-msg` 和提交模板。推送前 fetch，出现分叉先核对并处理冲突；禁止强推已交付历史，撤销使用 revert。其他任务的未提交内容不混入本次提交。
