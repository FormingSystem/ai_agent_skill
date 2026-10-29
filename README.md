---
id: readme
title: "AI_Agent_Skill"
kind: reference
status: maintained
domains:
  - repository
---

# 第1章\_AI_Agent_Skill

**简体中文** | [English](readme_en.md)

集中维护自定义 Codex 技能及其脚本、参考资料和代理配置。仓库源码是维护入口，安装目录是运行镜像。系统内置技能和第三方插件不在收录范围内。

## 1.1\_开始使用

需要 Git、Python 3.12+。在终端克隆后进入仓库：

```bash
git clone git@github.com:FormingSystem/ai_agent_skill.git
cd ai_agent_skill
python -m pip install -r requirements_dev.txt
python scripts/setup_repository.py
python scripts/check_repository.py
python -m unittest discover -s scripts -p 'test_*.py'
```

`setup_repository.py` 仅配置此仓库的提交钩子、模板和快进拉取。检查脚本核对技能元数据、注册关系、文件路径和 Markdown 相对链接目标；同步测试在临时目录运行，不修改真实安装。

确认安装差异后，从仓库单向同步到 `$CODEX_HOME/skills`；未设置 `CODEX_HOME` 时使用用户目录下的 `.codex/skills`：

```bash
python scripts/sync_skills.py check
python scripts/sync_skills.py apply
python scripts/sync_skills.py check
```

`check` 返回 0 表示一致，1 表示需要同步，2 表示注册或目录异常。`apply` 会覆盖镜像同名文件，拒绝链接、相互包含的目录和镜像多余文件，不回写仓库。可使用 `--codex-home <目录>` 指定独立安装环境。同步完成后在新会话检查技能是否已被加载。

## 1.2\_技能目录

| 技能 | 用途 |
| --- | --- |
| [build-linux-note-topic](skills/build-linux-note-topic/SKILL.md) | 编写、重构与检查技术知识专题 |
| [build-technical-ppt](skills/build-technical-ppt/SKILL.md) | 制作与修订技术教程 PPT 及配套 Markdown |
| [develop-loop-desktop](skills/develop-loop-desktop/SKILL.md) | Loop 桌面工作台开发 |
| [develop-typora-code](skills/develop-typora-code/SKILL.md) | TyporaCode 独立工程开发 |

项目类技能需要相应项目及其依赖；技能内部的环境提示必须按当前用户指定目录重新核对。

仓库阅读与维护指南提供中英文版本。技能运行指令和详细参考资料保留原有语言，目前以中文为主，技能链接并非完整英文译本。同名技能只维护一个运行包，阅读译文不新增运行时注册。

## 1.3\_维护入口

- [协作者规则](AGENTS.md)
- [信息架构与迁移来源](governance/architecture/repository_information_architecture.md)
- [贡献与验收流程](CONTRIBUTING.md)
- [Git 提交与发布规范](governance/conventions/git_guide.md)

文件管理继承 linux-note 的单一权威来源、职责分层、相对链接、稳定元数据和变更同步原则；技能保留其原生格式。提交采用中文结果加条目明细，由原仓库钩子校验。主线沿用远端已有的 `main`。

## 1.4\_许可证

继承 linux-note 的 [GNU General Public License 第 2 版](LICENSE)，保留来源和已有版权声明。远端初始化提交中的 GPLv3 已按迁移要求替换，历史提交保留。
