"""Cache a course's past-paper questions and topics to JSON for offline analysis.

Usage: python _pastpaper/cache.py <course_id>
"""
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
    if len(sys.argv) < 2:
        raise SystemExit("usage: cache.py <course_id>")
    course_id = int(sys.argv[1])
    out = Path(__file__).resolve().parent / f"cache_{course_id}.json"
    rows = (
        PrepQuestion.objects.filter(Q(topic__course_id=course_id) | Q(paper__course_id=course_id))
        .only("id", "topic_id", "paper_id", "question_latex", "solution_latex", "marks", "number", "verification_status", "reconstruction_metadata")
        .distinct()
        .order_by("id")
    )
    questions = []
    for q in rows:
        questions.append(
            {
                "id": q.id,
                "topic": q.topic_id,
                "paper": q.paper_id,
                "number": q.number,
                "marks": q.marks,
                "status": q.verification_status,
                "text": q.question_latex or "",
                "solution_len": len((q.solution_latex or "").strip()),
                "copy_of": (q.reconstruction_metadata or {}).get("cross_listed_from"),
            }
        )
    topics = [
        {"id": t.id, "title": t.title, "order": t.order, "subtopics": t.subtopics}
        for t in PrepTopic.objects.filter(course_id=course_id).order_by("id")
    ]
    out.write_text(json.dumps({"questions": questions, "topics": topics}, ensure_ascii=False), encoding="utf-8")
    print(f"course {course_id}: {len(questions)} questions, {len(topics)} topics -> {out}")
    for t in topics:
        print(f"  {t['id']}  {t['title']}")


if __name__ == "__main__":
    main()
