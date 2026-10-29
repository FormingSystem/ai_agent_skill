"""在维护者复核中英文正文后，显式记录指定文档对的内容摘要。"""

import argparse
import json
from pathlib import Path

from check_translations import content_hash


def update_reviewed(root, names):
    path = root / "scripts/translation_registry.json"
    registry = json.loads(path.read_text(encoding="utf-8"))
    pairs = {pair["zh"]: pair for pair in registry["pairs"]}
    unknown = set(names) - set(pairs)
    if unknown:
        raise ValueError(f"未登记的中文文档：{sorted(unknown)}")
    for name in names:
        pair = pairs[name]
        for language in ("zh", "en"):
            document = root / pair[language]
            if not document.resolve().is_relative_to(root.resolve()):
                raise ValueError("翻译路径越界")
            pair[language + "_sha256"] = content_hash(document)
    # 所有指定文档都能读取后才写回，避免半批更新。
    path.write_text(json.dumps(registry, ensure_ascii=False, indent=2) + "\n", encoding="utf-8", newline="\n")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--reviewed", nargs="+", required=True, help="已复核的中文文件相对路径 / Reviewed Chinese source paths")
    args = parser.parse_args()
    update_reviewed(Path(__file__).resolve().parents[1], args.reviewed)
    print(f"Recorded reviewed pairs: {len(set(args.reviewed))}")
