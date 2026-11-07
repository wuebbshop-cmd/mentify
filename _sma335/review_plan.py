"""Review the SMA 335 topic plan before applying it."""
from __future__ import annotations

import json
import os
import sys
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(BASE_DIR))
os.chdir(BASE_DIR)
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings.development")

import django  # noqa: E402

django.setup()

from prep.models import PrepQuestion, PrepTopic  # noqa: E402

PLAN = Path(__file__).resolve().parent / "topic_plan.json"


def main() -> None:
    plan = json.loads(PLAN.read_text(encoding="utf-8"))
    topics = {t.id: t.title for t in PrepTopic.objects.filter(course_id=57)}
    texts = {q.id: (q.question_latex or "") for q in PrepQuestion.objects.filter(pk__in=[p["id"] for p in plan])}

    unmatched = [p for p in plan if any("no signature" in v for v in p["evidence"].values())]
    print(f"### unmatched ({len(unmatched)})")
    for p in unmatched:
        print(f"  {p['id']} current={p['current']}: {texts[p['id']][:150].replace(chr(10), ' ')}")

    print()
    moves = [p for p in plan if p["current"] not in p["targets"]]
    print(f"### would move out of current topic: {len(moves)}")
    for p in moves[:15]:
        print(f"  {p['id']} {p['current']} -> {p['targets']}: {texts[p['id']][:110].replace(chr(10), ' ')}")

    print()
    print("### per-topic sample with evidence")
    for tid in sorted(topics):
        members = [p for p in plan if tid in p["targets"]]
        if not members:
            print(f"\n-- {tid} {topics[tid]}: NONE")
            continue
        print(f"\n-- {tid} {topics[tid]}: {len(members)}")
        for p in members[:3]:
            ev = p["evidence"].get(str(tid), [])
            print(f"   {p['id']} {texts[p['id']][:110].replace(chr(10), ' ')}")
            print(f"        evidence: {ev}")


if __name__ == "__main__":
    main()
