"""Print each topic's assignments with the part text that triggered them."""
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

from prep.models import PrepTopic  # noqa: E402

PLAN = Path(__file__).resolve().parent / "topic_plan.json"


def main() -> None:
    topics = {t.id: t.title for t in PrepTopic.objects.filter(course_id=57)}
    plan = json.loads(PLAN.read_text(encoding="utf-8"))
    wanted = [int(x) for x in sys.argv[1:]] or sorted(topics)

    for tid in wanted:
        members = [p for p in plan if tid in p["targets"]]
        print("=" * 100)
        print(f"TOPIC {tid} {topics[tid]}  ({len(members)})")
        for p in members:
            labels = [e.split(":")[0] for e in p["evidence"].get(str(tid), [])]
            matched = [pt for pt in p["parts"] if pt[1:pt.find(")")] in labels] if labels else p["parts"][:1]
            print(f"  {p['id']} (was {p['current']}) parts={labels}")
            for snippet in matched[:3]:
                print(f"      {snippet}")


if __name__ == "__main__":
    main()
