"""Review only the risky part of a plan: questions whose current topic is being dropped.

Usage: python _pastpaper/review_moves.py <course_id> [width]
"""
from __future__ import annotations

import io
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent


def main() -> None:
    course_id = int(sys.argv[1])
    width = int(sys.argv[2]) if len(sys.argv) > 2 else 110
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
    plan = json.loads((HERE / f"topic_plan_{course_id}.json").read_text(encoding="utf-8"))
    cache = json.loads((HERE / f"cache_{course_id}.json").read_text(encoding="utf-8"))
    titles = {t["id"]: t["title"] for t in cache["topics"]}
    rows = {q["id"]: q for q in cache["questions"]}

    seen = set()
    moves = 0
    for p in plan:
        q = rows[p["id"]]
        key = (" ".join((q["text"] or "").split()))[:200]
        if key in seen:
            continue
        seen.add(key)
        if p["current"] in p["targets"] or not p["current"]:
            continue
        moves += 1
        ev = ";".join(f"{k}:{','.join(v)[:50]}" for k, v in p["evidence"].items())
        print(f"\nq{p['id']} {titles[p['current']][:34]} -> {[titles[t][:22] for t in p['targets']]}")
        print(f"   {' '.join((q['text'] or '').split())[:width]}")
        print(f"   ev {ev[:220]}")
    print(f"\ndistinct questions whose current topic is dropped: {moves}")


if __name__ == "__main__":
    main()
