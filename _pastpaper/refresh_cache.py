"""Refresh a course's past-paper cache snapshot."""

import io
import json
import os
import sys
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(BASE_DIR))
os.chdir(BASE_DIR)
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings.development")
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")

import django

django.setup()

from django.db.models import Q

from prep.models import PrepQuestion

HERE = Path(__file__).resolve().parent


def main() -> None:
    if len(sys.argv) != 2:
        raise SystemExit("usage: refresh_cache.py <course_id>")
    course_id = int(sys.argv[1])
    questions = []
    qs = PrepQuestion.objects.filter(
        Q(topic__course_id=course_id) | Q(paper__course_id=course_id),
        verification_status__in=PrepQuestion.LEARNER_VISIBLE_STATUSES,
    ).select_related("topic", "paper").order_by("paper_id", "number", "id")
    for q in qs:
        questions.append(
            {
                "id": q.id,
                "topic": q.topic_id,
                "paper": str(q.paper_id) if q.paper_id else None,
                "number": q.number,
                "marks": q.marks,
                "status": q.verification_status,
                "text": q.question_latex or "",
                "solution_len": len(q.solution_latex or ""),
                "copy_of": (q.reconstruction_metadata or {}).get("cross_listed_from"),
            }
        )
    data = {"course_id": course_id, "questions": questions}
    out = HERE / f"cache_{course_id}.json"
    out.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"course={course_id} questions={len(questions)} cache={out}")


if __name__ == "__main__":
    main()
