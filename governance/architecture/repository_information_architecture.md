---
id: governance.architecture.repository_information_architecture
title: "技能仓库信息架构"
kind: reference
status: maintained
domains:
  - repository
---

# 第1章\_技能仓库信息架构

## 1.1\_按职责保存唯一来源

沿用 linux-note 的文件治理思想，按技能仓库实际职责组织材料，不复制知识库的空目录结构。

| 位置 | 职责 |
| --- | --- |
| `skills/<name>/SKILL.md` | 技能触发条件与运行入口 |
| `skills/<name>/references/` | 按需读取的规则与参考资料 |
| `skills/<name>/scripts/` | 技能自身的可执行辅助工具 |
| `skills/<name>/agents/` | 代理界面配置 |
| `scripts/skill_registry.json` | 安装同步登记，新增技能必须登记 |
| `scripts/` | 仓库检查、安装镜像同步及测试 |
| `governance/` | 架构、贡献规则与模板 |
| `.githooks/`、`.github/workflows/` | 提交校验与 CI |

## 1.2\_源文件与安装镜像

编辑仓库 → 结构与链接检查 → 同步测试 → 人工审查 → 提交 → 同步安装镜像 → 一致性检查。安装镜像不反向覆盖仓库；迁入时先核对双方差异，保留有效内容。同步遇到未登记的额外文件会拒绝写入，必须先处理其归属。

技能所操作的目标项目由用户当前任务决定，技能文件所在目录不自动成为目标项目根目录。已有技能中明确的本机路径属于原有工作环境提示，使用前仍须验证；跨机器使用应按真实环境调整，不把提示当作可访问性保证。

## 1.3\_迁移来源

2026-10-29 首次收录四个自定义技能。`build-linux-note-topic` 对比 linux-note 仓库副本与当前安装副本，保留安装副本中关于讲解定位、路径读取者和审稿重写的补充；其余技能来自当前自定义技能安装目录。运行缓存不入库。

同步程序、测试、提交钩子和模板复用 linux-note 的实现，并调整新仓库路径。许可证逐字继承 linux-note 的 GNU GPL 第 2 版文本；远端初始化时的 GPLv3 按本次迁移要求替换，原始提交仍留在历史中。
