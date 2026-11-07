"""Print a classification plan for review, one line per question.

Usage: python _pastpaper/review_plan.py <course_id> [width]
"""
from __future__ import annotations

import io
import json
import sys
from collections import Counter, defaultdict
from pathlib import Path

HERE = Path(__file__).resolve().parent


def main() -> None:
    course_id = int(sys.argv[1])
    width = int(sys.argv[2]) if len(sys.argv) > 2 else 90
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
    plan = json.loads((HERE / f"topic_plan_{course_id}.json").read_text(encoding="utf-8"))
    cache = json.loads((HERE / f"cache_{course_id}.json").read_text(encoding="utf-8"))
    titles = {t["id"]: t["title"] for t in cache["topics"]}
    rows = {q["id"]: q for q in cache["questions"]}

    groups: dict[tuple, list[dict]] = defaultdict(list)
    for p in plan:
        groups[tuple(p["targets"])].append(p)
    print("groups by target set:", len(groups))
    for targets, items in sorted(groups.items(), key=lambda kv: (-len(kv[1]), kv[0])):
        print(f"\n== targets {list(targets)} ({len(items)} rows) {'+'.join(titles[t][:18] for t in targets)}")
        for p in items:
            text = " ".join((rows[p['id']]["text"] or "").split())
            ev = ";".join(f"{k}:{','.join(v)[:40]}" for k, v in p["evidence"].items())
            print(f"  q{p['id']} cur={p['current']} :: {text[:width]}")
            print(f"      ev {ev[:150]}")


if __name__ == "__main__":
    main()
