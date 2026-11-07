"""Cache SMA 335 question texts to a local file so analysis runs without the database."""
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

from django.db.models import Q  # noqa: E402

from prep.models import PrepQuestion, PrepTopic  # noqa: E402


def main() -> None:
    out = Path(__file__).resolve().parent / "texts.json"
    rows = (
        PrepQuestion.objects.filter(Q(topic__course_id=57) | Q(paper__course_id=57))
        .only("id", "topic_id", "paper_id", "question_latex", "solution_latex", "marks", "number", "verification_status")
        .distinct()
        .order_by("id")
    )
    payload = [
        {
            "id": q.id,
            "topic": q.topic_id,
            "paper": q.paper_id,
            "number": q.number,
            "marks": str(q.marks),
            "status": q.verification_status,
            "text": q.question_latex or "",
            "solution_len": len(q.solution_latex or ""),
        }
        for q in rows
    ]
    topics = [{"id": t.id, "title": t.title} for t in PrepTopic.objects.filter(course_id=57).order_by("id")]
    out.write_text(json.dumps({"questions": payload, "topics": topics}, ensure_ascii=False), encoding="utf-8")
    print(f"cached {len(payload)} questions, {len(topics)} topics -> {out}")


if __name__ == "__main__":
    main()
