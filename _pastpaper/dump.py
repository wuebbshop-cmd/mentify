"""Print cached questions grouped by their current topic, for classification design.

Usage: python _pastpaper/dump.py <course_id> [width]
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent


def main() -> None:
    course_id = int(sys.argv[1])
    width = int(sys.argv[2]) if len(sys.argv) > 2 else 110
    data = json.loads((HERE / f"cache_{course_id}.json").read_text(encoding="utf-8"))
    titles = {t["id"]: t["title"] for t in data["topics"]}
    buckets: dict[int | None, list[dict]] = {}
    for q in data["questions"]:
        buckets.setdefault(q["topic"], []).append(q)
    for topic_id, qs in sorted(buckets.items(), key=lambda kv: (kv[0] is None, kv[0] or 0)):
        print(f"\n### {topic_id} {titles.get(topic_id, 'UNMAPPED')}  ({len(qs)} rows)")
        for q in qs:
            text = " ".join((q["text"] or "").split())
            print(f"  q{q['id']} n{q['number']} :: {text[:width]}")


if __name__ == "__main__":
    main()
