"""Show the distinct statements of a course, so classification works on unique text.

Usage: python _pastpaper/distinct.py <course_id> [width]
"""
from __future__ import annotations

import json
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path

HERE = Path(__file__).resolve().parent
_MARKER = re.compile(r"^(?:[\s:;,.()\[\]|*_#-]+|\(\s*[a-z0-9]{1,3}\s*\)|[a-z0-9]{1,3}\s*[).:]\s*)+", re.I)


def signature(text: str) -> str:
    return _MARKER.sub("", " ".join((text or "").split()).casefold())


def main() -> None:
    import io

    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
    course_id = int(sys.argv[1])
    width = int(sys.argv[2]) if len(sys.argv) > 2 else 120
    data = json.loads((HERE / f"cache_{course_id}.json").read_text(encoding="utf-8"))
    titles = {t["id"]: t["title"] for t in data["topics"]}
    groups: dict[str, list[dict]] = defaultdict(list)
    for q in data["questions"]:
        groups[signature(q["text"])].append(q)
    print(f"rows={len(data['questions'])} distinct={len(groups)}")
    spread = Counter(len(v) for v in groups.values())
    print("rows per distinct statement:", dict(sorted(spread.items())))
    for sig, qs in sorted(groups.items(), key=lambda kv: (-len(kv[1]), kv[0])):
        topics = sorted({q["topic"] for q in qs})
        print(f"\nx{len(qs)} topics={topics} ids={[q['id'] for q in qs][:6]}")
        print(f"   {sig[:width]}")


if __name__ == "__main__":
    main()
