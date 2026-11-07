"""Diagnose flagged/pending past-paper rows for one course.

Usage: python _pastpaper/diagnose.py <course_id>
"""
from __future__ import annotations

import io
import os
import sys
from collections import Counter
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(BASE_DIR))
os.chdir(BASE_DIR)
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings.development")
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")

import django  # noqa: E402

django.setup()

from django.db.models import Q  # noqa: E402

from prep.models import PrepQuestion  # noqa: E402
from services.prep_ingestion import assessment_question_rendering_issues  # noqa: E402


def main() -> None:
    course_id = int(sys.argv[1])
    rows = list(
        PrepQuestion.objects.filter(Q(topic__course_id=course_id) | Q(paper__course_id=course_id))
        .select_related("paper")
        .order_by("verification_status", "id")
    )
    print("statuses:", dict(Counter(q.verification_status for q in rows)))
    bad = [q for q in rows if assessment_question_rendering_issues(q.question_latex)]
    print("rows failing the rendering gate:", len(bad))
    print("issue frequency:", dict(Counter(i.split(":")[0] for q in bad for i in assessment_question_rendering_issues(q.question_latex))))
    for q in bad:
        issues = assessment_question_rendering_issues(q.question_latex)
        text = " ".join((q.question_latex or "").split())
        print(f"\nq{q.id} [{q.verification_status}] paper={str(q.paper_id)[-8:]} issues={issues}")
        print(f"   {text[:220]}")
        if len(text) > 220:
            print(f"   ...{text[-120:]}")


if __name__ == "__main__":
    main()
