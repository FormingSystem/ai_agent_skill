"""仅配置本技能仓库的 Git 协作规则。"""
from pathlib import Path
import subprocess


def main():
    repo_root = Path(__file__).resolve().parents[1]
    git_root = subprocess.check_output(["git", "rev-parse", "--show-toplevel"], cwd=repo_root, text=True).strip()
    if Path(git_root).resolve() != repo_root:
        raise SystemExit("Git 根目录不匹配")
    for key, value in {
        "core.hooksPath": ".githooks",
        "commit.template": "governance/templates/git_commit_message.txt",
        "pull.ff": "only",
    }.items():
        subprocess.run(["git", "config", "--local", key, value], cwd=repo_root, check=True)
    print("已配置提交钩子、模板和快进拉取")


if __name__ == "__main__":
    main()
