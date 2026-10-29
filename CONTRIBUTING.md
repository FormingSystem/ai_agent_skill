---
id: contributing
title: "贡献与验收流程"
kind: reference
status: maintained
domains:
  - repository
---

# 第1章\_贡献与验收流程

**简体中文** | [English](contributing_en.md)

先读 [项目约定](AGENTS.md) 和 [Git 规范](governance/conventions/git_guide.md)。首次克隆运行 `python scripts/setup_repository.py`，它仅配置当前仓库的钩子、提交模板和快进拉取策略。

新增技能时在 `skills/` 建立唯一包，提供 `SKILL.md` 的 `name` 与 `description`，按需加入参考资料和脚本，并登记 `scripts/skill_registry.json`、同步更新中英文 [技能目录](README.md#12_技能目录)。不要创建空的模板目录。

提交前运行 README 的检查命令，审查暂存差异；技能行为变化还应在对应真实任务中验证，自动结构检查不能代替效果验收。使用 `python scripts/sync_skills.py check` 预览安装差异，确认仓库内容正确后执行 `apply`，再执行 `check`。`apply` 会替换同名文件的本地修改，额外文件会阻止整批同步，请先核对来源。

移动或删除文件时同步全部引用及注册表；已发布提交以 revert 撤销。按实际结果写中文提交标题和明细，不提交凭据或生成缓存。

仓库阅读文档的中英文版本随同一变更维护，包括命令、行为边界和导航。译文使用独立文档 ID，并以 `translation_of` 指向原文 ID。译文是同一规则的阅读视图，不独立增加规则或注册同名技能；新增或修改技能主指令、参考文档及阅读入口时，两种语言须同时落地，并登记 `scripts/translation_registry.json`。先复核内容，再运行 `python scripts/update_translation_registry.py --reviewed <中文文件路径>` 更新摘要；该动作不代替语义审查。
