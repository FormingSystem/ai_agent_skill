"""验证漏译、过期译文、错误语言跳转和重复登记会被拒绝。"""

import json
from pathlib import Path
import tempfile
import unittest

from check_translations import check_translations, content_hash, skill_pair_structure, language_navigation, navigation_issues
from update_translation_registry import update_reviewed


class translations_test(unittest.TestCase):
    def test_skill_translation_preserves_identifiers(self):
        self.assertTrue(skill_pair_structure("# 标题\n使用 `safe_api`", "# Title\nUse `other_api`"))

    def test_skill_translation_cannot_drop_list_items(self):
        self.assertTrue(skill_pair_structure("# 标题\n- 规则一\n- 规则二", "# Title\n- First rule"))

    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory()
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name)
        (self.root / "scripts").mkdir()
        self.files = ["a.md", "a_en.md", "b.md", "b_en.md"]
        for name in self.files:
            english = name.endswith("_en.md")
            other = name.replace("_en.md", ".md") if english else name.replace(".md", "_en.md")
            nav = language_navigation(self.root / name, self.root / other, "en" if english else "zh")
            body = "[Body](b_en.md)" if english else "[正文](b.md)"
            (self.root / name).write_text(f"# Title\n\n{nav}\n\n{body}\n\n{nav}\n", encoding="utf-8")
        self.pairs = [{"zh": stem + ".md", "en": stem + "_en.md"} for stem in ("a", "b")]
        self.save()

    def save(self):
        for pair in self.pairs:
            for language in ("zh", "en"):
                pair[language + "_sha256"] = content_hash(self.root / pair[language])
        (self.root / "scripts/translation_registry.json").write_text(json.dumps({"schema_version": 1, "pairs": self.pairs}), encoding="utf-8")

    def test_valid_pairs(self):
        self.assertEqual(check_translations(self.root, self.files), [])

    def test_unregistered_document(self):
        self.assertTrue(check_translations(self.root, self.files + ["new.md"]))

    def test_changed_source_requires_review(self):
        (self.root / "a.md").write_text("new instruction", encoding="utf-8")
        self.assertTrue(check_translations(self.root, self.files))

    def test_english_navigation_cannot_fall_back_to_chinese(self):
        path = self.root / "a_en.md"
        path.write_text(path.read_text(encoding="utf-8").replace("[Body](b_en.md)", "[Body](b.md)"), encoding="utf-8")
        self.save()
        self.assertEqual(check_translations(self.root, self.files), ["导航跨语言：a_en.md -> b.md"])

    def test_missing_switch(self):
        (self.root / "a_en.md").write_text("[Body](b_en.md)\n", encoding="utf-8")
        self.save()
        self.assertTrue(check_translations(self.root, self.files))

    def test_translator_spacing_cannot_hide_links(self):
        path = self.root / "a_en.md"
        path.write_text(path.read_text(encoding="utf-8").replace("[Body](", "[Body] ("), encoding="utf-8")
        self.save()
        self.assertEqual(check_translations(self.root, self.files), ["Markdown 链接被空白拆开：a_en.md"])

    def test_duplicate_pair(self):
        self.pairs.append(dict(self.pairs[0]))
        self.save()
        self.assertTrue(check_translations(self.root, self.files))

    def test_explicit_review_updates_pair(self):
        path = self.root / "a_en.md"
        path.write_text(path.read_text(encoding="utf-8").replace("[Body]", "Reviewed clarification.\n\n[Body]"), encoding="utf-8")
        update_reviewed(self.root, ["a.md"])
        self.assertEqual(check_translations(self.root, self.files), [])

    def test_unknown_review_does_not_write(self):
        registry = self.root / "scripts/translation_registry.json"
        before = registry.read_bytes()
        with self.assertRaises(ValueError):
            update_reviewed(self.root, ["a.md", "missing.md"])
        self.assertEqual(registry.read_bytes(), before)

    def test_body_link_is_not_visible_navigation(self):
        path = self.root / "a.md"
        path.write_text("# Title\n\nProse mentions [English](a_en.md).\n", encoding="utf-8")
        self.assertEqual(len(navigation_issues(path, self.root / "a_en.md", "zh")), 2)

    def test_footer_cannot_switch_to_another_topic(self):
        path = self.root / "a.md"
        text = path.read_text(encoding="utf-8")
        last = text.rfind("a_en.md")
        path.write_text(text[:last] + text[last:].replace("a_en.md", "b_en.md", 1), encoding="utf-8")
        self.assertEqual(len(navigation_issues(path, self.root / "a_en.md", "zh")), 1)

    def test_front_matter_does_not_hide_header_navigation(self):
        path = self.root / "a.md"
        path.write_text("---\ntitle: Example\n---\n\n" + path.read_text(encoding="utf-8"), encoding="utf-8")
        self.assertEqual(navigation_issues(path, self.root / "a_en.md", "zh"), [])
