"""检查技能注册、元数据、相对链接目标与缓存隔离，不修改文件。"""

import ast
import json
from pathlib import Path
import re
import subprocess
import sys
from urllib.parse import unquote, urlsplit

import yaml

from check_translations import check_translations


def front_matter(path):
    text = path.read_text(encoding="utf-8-sig")
    if not text.startswith("---\n"):
        raise ValueError(f"缺少 Front Matter：{path}")
    parts = text.split("\n---", 1)
    if len(parts) != 2:
        raise ValueError(f"未闭合 Front Matter：{path}")
    data = yaml.safe_load(parts[0][4:])
    if not isinstance(data, dict):
        raise ValueError(f"元数据必须为映射：{path}")
    return data


def heading_anchors(path):
    text = path.read_text(encoding="utf-8-sig")
    text = re.sub(r"^```.*?^```[^\n]*", "", text, flags=re.M | re.S)
    anchors = set(re.findall(r'(?:id|name)=["\']([^"\']+)', text))
    counts = {}
    for heading in re.findall(r"^#{1,6}\s+(.+)$", text, re.M):
        heading = re.sub(r"<[^>]+>", "", heading).strip().lower()
        slug = re.sub(r"[^\w\- ]", "", heading).replace(" ", "-")
        count = counts.get(slug, 0)
        counts[slug] = count + 1
        anchors.add(f"{slug}-{count}" if count else slug)
    return anchors


def check_repository(root):
    errors = []
    registry = json.loads((root / "scripts/skill_registry.json").read_text(encoding="utf-8"))
    if registry.get("schema_version") != 1:
        errors.append("不支持的注册表版本")
    names = []
    for item in registry["skills"]:
        name = item["name"]
        names.append(name)
        if not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", name):
            errors.append(f"非法技能名称：{name}")
            continue
        if item != {"name": name, "source": f"skills/{name}",
                    "mirror": f"codex_home/skills/{name}", "direction": "repository_to_codex"}:
            errors.append(f"注册关系不正确：{name}")
        try:
            data = front_matter(root / "skills" / name / "SKILL.md")
            if data.get("name") != name or not isinstance(data.get("description"), str) or not data["description"].strip():
                errors.append(f"技能名称或描述无效：{name}")
        except (OSError, ValueError, yaml.YAMLError) as error:
            errors.append(str(error))
    actual = {path.name for path in (root / "skills").iterdir() if path.is_dir()}
    if set(names) != actual or len(names) != len(set(names)):
        errors.append("技能目录与注册表不一致或重复登记")
    doc_ids = set()
    files = subprocess.check_output(
        ["git", "ls-files", "--cached", "--others", "--exclude-standard", "-z"], cwd=root
    ).decode("utf-8").split("\0")
    for relative in sorted(set(filter(None, files))):
        path = root / relative
        if not path.is_file():
            continue
        if path.is_symlink() or path.is_junction():
            errors.append(f"不支持链接：{relative}")
        if re.search(r"[\s，。：；（）]|__|(^|/)_|_(/|$)", relative):
            errors.append(f"路径不符合命名规范：{relative}")
        if "__pycache__" in path.parts or path.suffix in {".pyc", ".pyo"}:
            errors.append(f"缓存被提交：{relative}")
        if path.suffix == ".py":
            try:
                ast.parse(path.read_text(encoding="utf-8-sig"), filename=relative)
            except SyntaxError as error:
                errors.append(str(error))
        if path.suffix != ".md":
            continue
        if not relative.startswith("skills/"):
            try:
                data = front_matter(path)
                if any(not data.get(key) for key in ("id", "title", "kind", "status", "domains")):
                    errors.append(f"治理元数据不完整：{relative}")
                if data.get("id") in doc_ids:
                    errors.append(f"重复文档 ID：{relative}")
                doc_ids.add(data.get("id"))
            except (ValueError, yaml.YAMLError) as error:
                errors.append(str(error))
        text = path.read_text(encoding="utf-8-sig")
        text = re.sub(r"^```.*?^```[^\n]*", "", text, flags=re.M | re.S)
        for link in re.findall(r"\[[^\]\n]*\]\(([^\s)]+)(?:\s+[^)]*)?\)", text):
            parts = urlsplit(link.strip("<>"))
            if parts.scheme or parts.netloc:
                continue
            target = path.parent / unquote(parts.path) if parts.path else path
            if not target.exists():
                errors.append(f"链接目标不存在：{relative} -> {link}")
            elif parts.fragment and target.suffix == ".md":
                if unquote(parts.fragment).lower() not in heading_anchors(target):
                    errors.append(f"标题锚点不存在：{relative} -> {link}")
        if re.search(r"^(<<<<<<< |=======\s*$|>>>>>>> )", text, re.M):
            errors.append(f"存在冲突标记：{relative}")
    errors.extend(check_translations(root, {
        name for name in files if name.endswith(".md") and (root / name).is_file()
    }))
    return errors


if __name__ == "__main__":
    issues = check_repository(Path(__file__).resolve().parents[1])
    for issue in issues:
        print(issue, file=sys.stderr)
    print(f"repository check: errors={len(issues)}")
    sys.exit(bool(issues))
