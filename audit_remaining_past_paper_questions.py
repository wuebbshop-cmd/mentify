"""Generate a read-only worklist of remaining past-paper question gaps."""

from __future__ import annotations

import os
import sys
from datetime import datetime
from zoneinfo import ZoneInfo

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
if BASE_DIR not in sys.path:
    sys.path.insert(0, BASE_DIR)
os.chdir(BASE_DIR)
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings.development")

import django

django.setup()

from audit_past_paper_questions import BANDS, cell, course_questions, level_of, summarise, topic_rows
from prep.models import PrepCourse, PrepPaper

OUT = os.path.join(BASE_DIR, "course_past_paper_question_audit.md")


def has_remaining_work(stats) -> bool:
    return (
        stats is None
        or stats["visible"] < stats["total"]
        or bool(stats["blank_solution"])
    )


def main() -> None:
    paper_course_ids = PrepPaper.objects.values_list("course_id", flat=True).distinct()
    question_course_ids = set()
    for course in PrepCourse.objects.filter(topics__questions__isnull=False).distinct():
        question_course_ids.add(course.pk)
    for course in PrepCourse.objects.filter(papers__questions__isnull=False).distinct():
        question_course_ids.add(course.pk)

    courses = [
        course
        for course in PrepCourse.objects.filter(pk__in=set(paper_course_ids) | question_course_ids).order_by("code")
        if level_of(course.code) in BANDS
    ]

    all_questions = 0
    all_visible = 0
    hidden = 0
    blank_solution = 0
    unmapped = 0
    remaining: list[tuple[object, int, list[tuple[str, dict | None]], int]] = []

    for course in courses:
        questions = course_questions(course)
        all_questions += len(questions)
        visible = sum(
            1
            for question in questions
            if question["verification_status"] in {"verified", "auto_validated", "reconstructed"}
            and (question["paper__is_published"] is None or question["paper__is_published"])
        )
        all_visible += visible
        hidden += len(questions) - visible
        rows = [(title, summarise(items)) for title, items in topic_rows(course, questions)]
        remaining_rows = [(title, stats) for title, stats in rows if has_remaining_work(stats)]
        course_unmapped = sum(1 for question in questions if question["topic_id"] is None)
        course_blank = sum(
            1
            for question in questions
            if question["verification_status"] in {"verified", "auto_validated", "reconstructed"}
            and (question["paper__is_published"] is None or question["paper__is_published"])
            and not str(question["solution_latex"] or "").strip()
        )
        blank_solution += course_blank
        unmapped += course_unmapped
        if remaining_rows or course_unmapped:
            remaining.append((course, len(questions), remaining_rows, course_unmapped))

    stamp = datetime.now(ZoneInfo("Africa/Nairobi")).strftime("%Y-%m-%d %H:%M EAT")
    lines: list[str] = []
    add = lines.append
    add("# Remaining Past Paper Question Worklist")
    add("")
    add(f"**Audit time:** {stamp}  ")
    add(
        "**Scope:** Courses in the 100, 200 and 300 bands with past papers or extracted questions. "
        "Courses and topics with fully learner-visible questions and worked solutions are omitted."
    )
    add(
        "**Method:** Read-only database audit. A topic remains when it has no learner-visible "
        "question, hidden questions, or a visible question without a worked solution."
    )
    add("")
    add("## Summary")
    add("")
    add(f"- Courses checked: **{len(courses)}**")
    add(f"- Extracted questions checked: **{all_questions}**")
    add(f"- Learner-visible questions: **{all_visible}**")
    add(f"- Hidden questions: **{hidden}**")
    add(f"- Visible questions without solutions: **{blank_solution}**")
    add(f"- Questions not mapped to a topic: **{unmapped}**")
    add(f"- Courses with remaining work: **{len(remaining)}**")
    add("")
    add("## Remaining Courses and Topics")
    add("")
    for course, question_count, rows, course_unmapped in remaining:
        add(f"### {course.code} - {course.title}")
        add("")
        add(f"Questions checked: **{question_count}**  ")
        if course_unmapped:
            add(f"Not mapped to a topic: **{course_unmapped}**  ")
        add("")
        add("| Topic | Remaining question work |")
        add("|---|---|")
        for title, stats in rows:
            add(f"| {title} | {cell(stats)} |")
        if course_unmapped:
            add(f"| (not mapped to any topic) | {course_unmapped} question(s) need topic mapping |")
        add("")

    if not remaining:
        add("All in-scope topics have learner-visible questions with worked solutions.")
        add("")

    with open(OUT, "w", encoding="utf-8", newline="\n") as handle:
        handle.write("\n".join(lines))

    print(
        f"wrote {OUT}: courses={len(courses)} remaining_courses={len(remaining)} "
        f"questions={all_questions} visible={all_visible}"
    )


if __name__ == "__main__":
    main()
