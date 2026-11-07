"""End-to-end render check for SMA 335 topic pages and paper pages.

Uses the exact querysets the views use, then asserts every distinct question reaches the
template and that nothing renders a broken statement.
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

COURSE_ID = 57
_STRANDED_ENV = re.compile(r"\\begin\{([a-zA-Z*]+)\}")


def norm_text(text: str) -> str:
    return " ".join(normalize_math_delimiters(text or "").split()).casefold()



def strict_issues(text: str) -> list[str]:
    """App checks plus the ones it deliberately ignores."""
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
    """Rows that should display but do not, with no legitimate reason.

    Legitimate reasons: the statement fails the app's own rendering gate, a cleaner
    reconstruction supersedes it, or the identical statement already renders from a twin row.
    """
    rows = list(records)
    superseded = {q.reconstructed_from_id for q in rows if q.reconstructed_from_id}
    unexplained = []
    for q in rows:
        if assessment_question_rendering_issues(q.question_latex):
            continue
        if norm_text(q.question_latex) in shown:
            continue
        if q.id in superseded:
            continue
        unexplained.append((q.id, f"hidden but distinct: {norm_text(q.question_latex)[:90]!r}"))
    return unexplained


def main() -> None:
    norm = lambda t: " ".join(normalize_math_delimiters(t or "").split())  # noqa: E731

    print("== topic pages ==")
    bad = 0
    for topic in PrepTopic.objects.filter(course_id=COURSE_ID).order_by("id"):
        topic_match = Q(topic=topic) | (
            Q(topic__isnull=True)
            & Q(paper__course=topic.course)
            & Q(topic_label__icontains=topic.title)
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
        shown = {norm_text(q.question_latex) for q in rendered}
        reasons = unexplained_drops(records, shown)
        problems = [(q.id, strict_issues(q.question_latex)) for q in rendered if strict_issues(q.question_latex)]
        status = "OK" if not reasons and not problems else "FAIL"
        if reasons or problems:
            bad += 1
        print(f"  {topic.id} rows={records.count():3d} shown={len(rendered):3d} {status}")
        for qid, why in problems[:3]:
            print(f"      q{qid}: {why}")
        for qid, why in reasons[:3]:
            print(f"      q{qid}: {why}")

    print("== paper pages ==")
    for paper in PrepPaper.objects.filter(course_id=COURSE_ID).order_by("id"):
        records = paper.questions.filter(
            verification_status__in=PrepQuestion.LEARNER_VISIBLE_STATUSES
        ).order_by("number", "id")
        rendered = learner_visible_assessment_questions(records)
        shown = {norm_text(q.question_latex) for q in rendered}
        reasons = unexplained_drops(records, shown)
        numbers = [q.number for q in rendered]
        dupes = len(numbers) - len(set(numbers))
        published = "pub " if paper.is_published else "HIDDEN"
        status = "OK" if not reasons and not dupes else "FAIL"
        if reasons or dupes:
            bad += 1
        print(
            f"  {paper.id[:26]:26} {published} rows={records.count():3d} shown={len(rendered):3d} "
            f"duplicate_numbers={dupes} {status}"
        )
        for qid, why in reasons[:3]:
            print(f"      q{qid}: {why}")
    print("FAILURES:", bad)


if __name__ == "__main__":
    main()

