"""检查中英文覆盖、译文版本及语言内导航，不修改文件。"""

import hashlib
import json
import os
from collections import Counter
from pathlib import Path
import re
from urllib.parse import unquote, urlsplit


def language_navigation(path, counterpart, language):
    target = os.path.relpath(counterpart, path.parent).replace("\\", "/")
    if language == "zh":
        return f"> **语言 / Language** · **简体中文（当前）** · [English →]({target})"
    return f"> **Language / 语言** · [← 简体中文]({target}) · **English (current)**"


def navigation_issues(path, counterpart, language):
    text = path.read_text(encoding="utf-8-sig")
    if text.startswith("---\n"):
        text = text.split("\n---", 1)[-1]
    lines = [line.strip() for line in text.splitlines() if line.strip()]
    expected = language_navigation(path, counterpart, language)
    issues = []
    if len(lines) < 2 or not lines[0].startswith("# ") or lines[1] != expected:
        issues.append("标题下缺少可见语言导航或目标错误")
    if not lines or lines[-1] != expected:
        issues.append("文末缺少可见语言导航或目标错误")
    return issues


def skill_pair_structure(source, translation):
    """保护翻译中的信息组织及字面代码；不声称证明翻译语义。"""
    issues = []
    for label, pattern in (
        ("标题", r"^#{1,6}\s+"),
        ("列表项", r"^\s*(?:[-*+] |\d+[.)] )"),
        ("表格行", r"^\|"),
        ("代码围栏", r"^```"),
    ):
        if len(re.findall(pattern, source, re.M)) != len(re.findall(pattern, translation, re.M)):
            issues.append(f"双语{label}数量不一致")
    literals = [Counter(re.findall(r"(?<!`)`([^`\n]+)`(?!`)", text)) for text in (source, translation)]
    if literals[0] != literals[1]:
        issues.append("双语行内代码标识不一致")
    return issues


def content_hash(path):
    return hashlib.sha256(path.read_text(encoding="utf-8-sig").encode("utf-8")).hexdigest()


def markdown_links(path):
    text = path.read_text(encoding="utf-8-sig")
    text = re.sub(r"^```.*?^```[^\n]*", "", text, flags=re.M | re.S)
    text = re.sub(r"`[^`\n]+`", "", text)
    return re.findall(r"\[[^\]\n]*\]\(([^\s)]+)(?:\s+[^)]*)?\)", text)


def check_translations(root, markdown_files):
    registry_path = root / "scripts/translation_registry.json"
    if not registry_path.is_file():
        return ["缺少中英文翻译台账"]
    registry = json.loads(registry_path.read_text(encoding="utf-8"))
    if registry.get("schema_version") != 1:
        return ["不支持的翻译台账版本"]
    errors = []
    owners = {}
    pairs = registry["pairs"]
    for pair in pairs:
        for language in ("zh", "en"):
            name = pair[language]
            path = root / name
            if name in owners:
                errors.append(f"翻译路径重复：{name}")
            owners[name] = language
            if not path.resolve().is_relative_to(root.resolve()) or not path.is_file():
                errors.append(f"翻译文件缺失或越界：{name}")
                continue
            if content_hash(path) != pair[language + "_sha256"]:
                errors.append(f"翻译已变化，需复核两种语言并更新台账：{name}")
    actual = set(markdown_files)
    if actual != set(owners):
        errors.append(f"双语覆盖不完整：未登记={sorted(actual-set(owners))} 多余={sorted(set(owners)-actual)}")
    for pair in pairs:
        source = root / pair["zh"]
        translation = root / pair["en"]
        if pair["zh"].startswith("skills/") and source.is_file() and translation.is_file():
            errors.extend(f"{pair['zh']}：{issue}" for issue in skill_pair_structure(
                source.read_text(encoding="utf-8-sig"), translation.read_text(encoding="utf-8-sig")
            ))
        for language, other in (("zh", "en"), ("en", "zh")):
            path = root / pair[language]
            if not path.is_file():
                continue
            errors.extend(f"{pair[language]}：{issue}" for issue in navigation_issues(
                path, root / pair[other], language
            ))
            prose = re.sub(r"^```.*?^```[^\n]*", "", path.read_text(encoding="utf-8-sig"), flags=re.M | re.S)
            prose = re.sub(r"`[^`\n]+`", "", prose)
            if re.search(r"\[[^\]\n]+\]\s+\(", prose):
                errors.append(f"Markdown 链接被空白拆开：{pair[language]}")
            switch = (root / pair[other]).resolve()
            switched = False
            for link in markdown_links(path):
                parts = urlsplit(link.strip("<>"))
                if parts.scheme or parts.netloc or not parts.path:
                    continue
                target = (path.parent / unquote(parts.path)).resolve()
                if target == switch:
                    switched = True
                    continue
                if target.suffix == ".md" and target.is_relative_to(root.resolve()):
                    relative = target.relative_to(root.resolve()).as_posix()
                    if relative in owners and owners[relative] != language:
                        errors.append(f"导航跨语言：{pair[language]} -> {link}")
            if not switched:
                errors.append(f"缺少语言切换：{pair[language]}")
    return errors
