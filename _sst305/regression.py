"""Regression check: does running the repair again break any now-clean row?"""
from __future__ import annotations

import os
import sys
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(BASE_DIR))
sys.path.insert(0, str(Path(__file__).resolve().parent))
os.chdir(BASE_DIR)
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings.development")

import django  # noqa: E402

django.setup()

from django.db.models import Q  # noqa: E402

from prep.models import PrepQuestion  # noqa: E402
from repair import repair_text  # noqa: E402
from services.prep_ingestion import assessment_question_rendering_issues  # noqa: E402


def main() -> None:
    rows = PrepQuestion.objects.filter(Q(topic__course_id=27) | Q(paper__course_id=27)).distinct()
    broken = []
    changed = 0
    for q in rows:
        before = q.question_latex or ""
        if assessment_question_rendering_issues(before):
            continue
        after, _changes = repair_text(before)
        if after == before:
            continue
        changed += 1
        if assessment_question_rendering_issues(after):
            broken.append(q.id)
    print(f"clean rows that the repair would rewrite: {changed}")
    print(f"clean rows the repair would BREAK: {broken}")


if __name__ == "__main__":
    main()
