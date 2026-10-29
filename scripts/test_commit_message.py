"""验证继承的提交钩子接受中文明细并拒绝不合规信息。"""

from pathlib import Path
import shutil
import subprocess
import tempfile
import unittest


class commit_message_test(unittest.TestCase):
    def test_commit_contract(self):
        shell = shutil.which("sh")
        if shell is None:
            git = shutil.which("git")
            candidate = Path(git).resolve().parents[1] / "bin/sh.exe" if git else Path("")
            if not candidate.is_file():
                self.fail("找不到用于执行 Git hook 的 sh")
            shell = str(candidate)
        hook = Path(__file__).resolve().parents[1] / ".githooks/commit-msg"
        cases = [
            ("feat(skill/install): 支持安装技能\n\n- 校验文件来源与同步方向\n", True),
            ("docs(技能/说明): 补充使用说明\n\n- 说明验证步骤\n", True),
            ("fix: english only\n\n- 明细\n", False),
            ("update: 修改技能\n\n- 明细\n", False),
            ("docs: 补充说明\n", False),
            ("docs: 补充说明\n- 没有空行\n", False),
            ("docs: 补充说明\n\n不合规正文\n", False),
        ]
        with tempfile.TemporaryDirectory() as temporary:
            message = Path(temporary) / "message.txt"
            for content, expected in cases:
                with self.subTest(content=content):
                    message.write_text(content, encoding="utf-8", newline="\n")
                    result = subprocess.run([shell, hook.as_posix(), message.as_posix()], capture_output=True)
                    self.assertEqual(result.returncode == 0, expected, result.stderr)


if __name__ == "__main__":
    unittest.main()
