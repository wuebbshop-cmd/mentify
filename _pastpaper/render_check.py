"""End-to-end render check for one course's topic pages and paper pages.

Uses the exact querysets the views use, then asserts every distinct question reaches the
template, numbers stay unique inside a paper, and nothing renders a broken statement.

Usage: python _pastpaper/render_check.py <course_id>
"""
from __future__ import annotations

import io
import os
import re
import sys
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(BASE_DIR))
os.chdir(BASE_DIR)
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings.development")
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")

import django  # noqa: E402

django.setup()

from django.db.models import Q  # noqa: E402

from prep.models import PrepPaper, PrepQuestion, PrepTopic  # noqa: E402
from services.prep_ai_router import normalize_math_delimiters  # noqa: E402
from services.prep_ingestion import (  # noqa: E402
    assessment_question_rendering_issues,
    learner_visible_assessment_questions,
)

_STRANDED_ENV = re.compile(r"\\begin\{([a-zA-Z*]+)\}")


def norm(text: str) -> str:
    return " ".join(normalize_math_delimiters(text or "").split()).casefold()


def strict_issues(text: str) -> list[str]:
    issues = list(assessment_question_rendering_issues(text))
    body = text or ""
    if body.count("$$") % 2:
        issues.append("odd number of $$ fences")
    outside = " ".join(body.split("$$")[0::2])
    if _STRANDED_ENV.search(outside):
        issues.append("environment outside display math")
    for line in body.splitlines():
        if line.strip() == "$":
            issues.append("stranded $ line")
    return issues


def unexplained_drops(records, shown: set[str]) -> list[tuple[int, str]]:
    rows = list(records)
    superseded = {q.reconstructed_from_id for q in rows if q.reconstructed_from_id}
    out = []
    for q in rows:
        if assessment_question_rendering_issues(q.question_latex):
            continue
        if norm(q.question_latex) in shown or q.id in superseded:
            continue
        out.append((q.id, f"hidden but distinct: {norm(q.question_latex)[:90]!r}"))
    return out


def main() -> None:
    if len(sys.argv) < 2:
        raise SystemExit("usage: render_check.py <course_id>")
    course_id = int(sys.argv[1])
    bad = 0

    print("== topic pages ==")
    for topic in PrepTopic.objects.filter(course_id=course_id).order_by("id"):
        topic_match = Q(topic=topic) | (
            Q(topic__isnull=True) & Q(paper__course=topic.course) & Q(topic_label__icontains=topic.title)
        )
        records = (
            PrepQuestion.objects.filter(
                topic_match, verification_status__in=PrepQuestion.LEARNER_VISIBLE_STATUSES
            )
            .filter(Q(paper__isnull=True) | Q(paper__is_published=True))
            .select_related("paper")
            .order_by("question_type", "paper__created_at", "number", "id")
        )
        rendered = learner_visible_assessment_questions(records)
        shown = {norm(q.question_latex) for q in rendered}
        reasons = unexplained_drops(records, shown)
        problems = [(q.id, strict_issues(q.question_latex)) for q in rendered if strict_issues(q.question_latex)]
        status = "OK" if not reasons and not problems else "FAIL"
        if reasons or problems:
            bad += 1
        print(f"  {topic.id} rows={records.count():4d} shown={len(rendered):4d} {status}")
        for qid, why in (problems + reasons)[:3]:
            print(f"      q{qid}: {why}")

    print("== paper pages ==")
    for paper in PrepPaper.objects.filter(course_id=course_id).order_by("id"):
        records = paper.questions.filter(
            verification_status__in=PrepQuestion.LEARNER_VISIBLE_STATUSES
        ).order_by("number", "id")
        rendered = learner_visible_assessment_questions(records)
        shown = {norm(q.question_latex) for q in rendered}
        reasons = unexplained_drops(records, shown)
        numbers = [q.number for q in rendered]
        dupes = len(numbers) - len(set(numbers))
        status = "OK" if not reasons and not dupes else "FAIL"
        if reasons or dupes:
            bad += 1
        published = "pub " if paper.is_published else "HIDDEN"
        print(f"  {str(paper.id)[:30]:30} {published} rows={records.count():4d} shown={len(rendered):4d} dup_numbers={dupes} {status}")
        for qid, why in reasons[:3]:
            print(f"      q{qid}: {why}")
    print("FAILURES:", bad)


if __name__ == "__main__":
    main()
