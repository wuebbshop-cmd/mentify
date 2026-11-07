"""Generate the past-paper question audit for level 100-300 courses.

Read-only. Produces course_past_paper_question_audit.md in the repository root.

Visibility rule mirrors the app (prep/views.py): a question is learner-visible when
its verification_status is one of PrepQuestion.LEARNER_VISIBLE_STATUSES and its paper
is published (or it has no paper at all).
"""

from __future__ import annotations

import os
import re
import sys
from collections import defaultdict
from datetime import datetime, timezone as dt_timezone

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
if BASE_DIR not in sys.path:
    sys.path.insert(0, BASE_DIR)
os.chdir(BASE_DIR)
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings.development")

import django

django.setup()

from django.db.models import Count, Q

from prep.models import PrepCourse, PrepPaper, PrepQuestion

VIS = PrepQuestion.LEARNER_VISIBLE_STATUSES
BANDS = (100, 200, 300)
OUT = os.path.join(BASE_DIR, "course_past_paper_question_audit.md")


def level_of(code: str):
    match = re.search(r"\d{3}", code or "")
    return int(match.group(0)[0]) * 100 if match else None


def visible_qs(queryset):
    return queryset.filter(verification_status__in=VIS).filter(
        Q(paper__isnull=True) | Q(paper__is_published=True)
    )


def short(text, limit=70):
    text = re.sub(r"\s+", " ", str(text or "")).strip()
    return text if len(text) <= limit else text[: limit - 1] + "…"


def course_questions(course):
    """Questions belonging to a course, whether via their paper or their topic.

    A generated practice variant can hang off a topic with no paper at all, and the
    app shows those too, so both routes must be counted. Rows are de-duplicated by id
    because a question can match both routes.
    """
    rows = PrepQuestion.objects.filter(
        Q(paper__course=course) | Q(topic__course=course)
    ).values(
        "id",
        "topic_id",
        "verification_status",
        "question_type",
        "solution_latex",
        "paper__is_published",
    )
    seen = {}
    for row in rows:
        seen.setdefault(row["id"], row)
    return list(seen.values())


def topic_rows(course, questions):
    """Group one course's questions by topic, in syllabus order."""
    by_topic = defaultdict(list)
    for question in questions:
        by_topic[question["topic_id"]].append(question)

    topics = list(course.topics.filter(is_active=True).order_by("order", "id"))
    rows = []
    for topic in topics:
        rows.append((topic.title, by_topic.pop(topic.pk, [])))
    for topic_id, items in by_topic.items():
        if topic_id is None:
            rows.append(("(not mapped to any topic)", items))
        else:
            rows.append((f"(inactive topic id {topic_id})", items))
    return rows


def summarise(items):
    """Collapse one topic's questions into the display cells."""
    if not items:
        return None
    vis = [
        q
        for q in items
        if q["verification_status"] in VIS
        and (q["paper__is_published"] is None or q["paper__is_published"])
    ]
    flagged = sum(1 for q in items if q["verification_status"] == "flagged")
    pending = sum(1 for q in items if q["verification_status"] == "pending")
    blank_solution = sum(1 for q in vis if not str(q["solution_latex"] or "").strip())
    types = defaultdict(int)
    for q in vis:
        types[q["question_type"]] += 1
    return {
        "total": len(items),
        "visible": len(vis),
        "flagged": flagged,
        "pending": pending,
        "blank_solution": blank_solution,
        "types": dict(types),
    }


def cell(stats):
    if stats is None:
        return "NO QUESTIONS"
    if stats["visible"] == 0:
        parts = []
        if stats["flagged"]:
            parts.append(f"{stats['flagged']} flagged")
        if stats["pending"]:
            parts.append(f"{stats['pending']} pending")
        detail = f" ({', '.join(parts)})" if parts else ""
        return f"HIDDEN - 0 of {stats['total']} visible{detail}"
    breakdown = "/".join(
        str(stats["types"].get(key, 0)) for key in ("authentic", "adapted", "generated")
    )
    text = f"VISIBLE {stats['visible']} of {stats['total']} (auth/adapt/gen {breakdown})"
    if stats["blank_solution"]:
        text += f"; {stats['blank_solution']} without solution"
    hidden = stats["flagged"] + stats["pending"]
    if hidden:
        text += f"; {stats['flagged']} flagged, {stats['pending']} pending"
    return text


def main():
    paper_counts = dict(
        PrepPaper.objects.values_list("course_id").annotate(n=Count("id"))
    )
    by_paper = dict(
        PrepQuestion.objects.filter(paper__course__isnull=False)
        .values_list("paper__course_id")
        .annotate(n=Count("id"))
    )
    by_topic = dict(
        PrepQuestion.objects.filter(topic__course__isnull=False)
        .values_list("topic__course_id")
        .annotate(n=Count("id"))
    )
    course_ids = set(paper_counts) | set(by_paper) | set(by_topic)
    courses = []
    for course in PrepCourse.objects.filter(pk__in=course_ids).order_by("code"):
        band = level_of(course.code)
        if band not in BANDS:
            continue
        papers = paper_counts.get(course.pk, 0)
        questions = len(course_questions(course))
        if not papers and not questions:
            continue
        courses.append((band, course, papers, questions))

    courses.sort(key=lambda item: (item[0], item[1].code))

    totals = {
        "courses": len(courses),
        "papers": 0,
        "questions": 0,
        "visible": 0,
        "flagged": 0,
        "pending": 0,
        "verified": 0,
        "auto": 0,
        "recon": 0,
        "no_topic": 0,
        "blank_solution": 0,
    }
    per_band = {band: {"courses": 0, "questions": 0, "visible": 0} for band in BANDS}

    lines = []
    add = lines.append
    add("# Past Paper Question Audit — Level 100 to 300 Courses")
    add("")
    stamp = datetime.now(dt_timezone.utc).astimezone().strftime("%Y-%m-%d %H:%M %Z")
    add(f"**Audit time:** {stamp}  ")
    add(
        "**Scope:** Every course whose code number falls in the 100, 200 or 300 band "
        "(for example SMA 330 is a 300-level course) and which has at least one past paper "
        "or one extracted question. Level 400 courses are deliberately excluded and will be "
        "audited separately."
    )
    add(
        "**Method:** Read-only database audit. For each course the report lists every active "
        "topic with the number of questions that are currently learner-visible, broken down by "
        "question type, together with the questions that are hidden because they are flagged or "
        "still pending verification. No question, paper or cache record was modified."
    )
    add("")
    add("## How to read this report")
    add("")
    add(
        "- **VISIBLE n of m** — n questions are shown to learners. The bracket separates them "
        "into auth (authentic past-paper), adapt (adapted) and gen (generated variants). "
        "A question counts as visible when its verification status is verified, auto_validated "
        "or reconstructed *and* its paper is published."
    )
    add(
        "- **HIDDEN** — a question exists for the topic but none of it reaches a learner, because "
        "every question is flagged for correction or still pending verification."
    )
    add("- **NO QUESTIONS** — the topic has no extracted question at all.")
    add(
        "- **without solution** — the question is visible but its worked solution is empty, so a "
        "learner sees the problem with nothing to mark their attempt against."
    )
    add(
        "- **not mapped to any topic** — the question exists on a published paper but was never "
        "attributed to a syllabus topic, so it does not appear under any topic page."
    )
    add("")

    # First pass for summary numbers.
    course_blocks = []
    for band, course, papers, questions in courses:
        question_rows = course_questions(course)
        rows = topic_rows(course, question_rows)
        stats_rows = [(title, summarise(items)) for title, items in rows]
        status_counts = defaultdict(int)
        for q in question_rows:
            status_counts[q["verification_status"]] += 1
        vis = [
            q
            for q in question_rows
            if q["verification_status"] in VIS
            and (q["paper__is_published"] is None or q["paper__is_published"])
        ]
        no_topic = sum(1 for q in question_rows if q["topic_id"] is None)
        blank = sum(1 for q in vis if not str(q["solution_latex"] or "").strip())
        course_blocks.append(
            {
                "band": band,
                "course": course,
                "papers": papers,
                "questions": questions,
                "rows": stats_rows,
                "visible": len(vis),
                "flagged": status_counts.get("flagged", 0),
                "pending": status_counts.get("pending", 0),
                "verified": status_counts.get("verified", 0),
                "auto": status_counts.get("auto_validated", 0),
                "recon": status_counts.get("reconstructed", 0),
                "no_topic": no_topic,
                "blank": blank,
            }
        )
        totals["papers"] += papers
        totals["questions"] += questions
        totals["visible"] += len(vis)
        totals["flagged"] += status_counts.get("flagged", 0)
        totals["pending"] += status_counts.get("pending", 0)
        totals["verified"] += status_counts.get("verified", 0)
        totals["auto"] += status_counts.get("auto_validated", 0)
        totals["recon"] += status_counts.get("reconstructed", 0)
        totals["no_topic"] += no_topic
        totals["blank_solution"] += blank
        per_band[band]["courses"] += 1
        per_band[band]["questions"] += questions
        per_band[band]["visible"] += len(vis)

    hidden_total = totals["questions"] - totals["visible"]
    add("## Summary")
    add("")
    add(f"- Courses in scope: **{totals['courses']}**")
    add(f"- Published past papers: **{totals['papers']}**")
    add(f"- Extracted questions: **{totals['questions']}**")
    add(f"- Learner-visible questions: **{totals['visible']}**")
    add(f"- Hidden questions: **{hidden_total}** (flagged {totals['flagged']}, pending {totals['pending']})")
    add(
        f"- Verification breakdown: verified **{totals['verified']}**, "
        f"auto-validated **{totals['auto']}**, reconstructed **{totals['recon']}**"
    )
    add(f"- Questions not attributed to any topic: **{totals['no_topic']}**")
    add(f"- Visible questions with an empty solution: **{totals['blank_solution']}**")
    add("")
    add("| Band | Courses | Questions | Visible | Hidden | Visible share |")
    add("|---|---|---|---|---|---|")
    for band in BANDS:
        row = per_band[band]
        hidden = row["questions"] - row["visible"]
        share = f"{row['visible'] / row['questions']:.0%}" if row["questions"] else "n/a"
        add(f"| {band} | {row['courses']} | {row['questions']} | {row['visible']} | {hidden} | {share} |")
    add("")

    # Where to begin.
    ranked = sorted(
        course_blocks,
        key=lambda block: (block["questions"] - block["visible"]),
        reverse=True,
    )
    add("## Where to begin")
    add("")
    add(
        "Courses ranked by the absolute number of hidden questions, which is the volume of work "
        "waiting before the paper bank is fully usable."
    )
    add("")
    add("| Rank | Course | Questions | Visible | Hidden | Flagged | Pending | Not mapped to a topic |")
    add("|---|---|---|---|---|---|---|---|")
    rank = 0
    for block in ranked:
        hidden = block["questions"] - block["visible"]
        if hidden == 0 and block["no_topic"] == 0:
            continue
        rank += 1
        add(
            f"| {rank} | {block['course'].code} — {short(block['course'].title, 34)} | "
            f"{block['questions']} | {block['visible']} | {hidden} | {block['flagged']} | "
            f"{block['pending']} | {block['no_topic']} |"
        )
    add("")

    add("## Course-by-course status")
    add("")
    for block in course_blocks:
        course = block["course"]
        add(f"### {course.code} - {course.title}")
        add("")
        add(
            f"Papers **{block['papers']}** · Questions **{block['questions']}** · "
            f"Visible **{block['visible']}** · Flagged **{block['flagged']}** · "
            f"Pending **{block['pending']}** · Not mapped to a topic **{block['no_topic']}**"
        )
        add("")
        add("| Topic | Question status |")
        add("|---|---|")
        for title, stats in block["rows"]:
            add(f"| {short(title, 76)} | {cell(stats)} |")
        if not block["rows"]:
            add("| (no active topics) | NO QUESTIONS |")
        add("")

    add("## Notes on interpretation")
    add("")
    add(
        "A question that is flagged has been extracted but failed the automatic consistency checks, "
        "so it is withheld rather than shown. A pending question has never been through verification. "
        "Both are recoverable, but by different work: a flagged question needs its statement or solution "
        "corrected, while a pending question needs to be verified from the source paper."
    )
    add("")
    add(
        "Questions that are not mapped to any topic still display on the paper view, but they never "
        "appear under a topic, so a learner revising a specific topic will not find them. Mapping them "
        "is usually the cheapest improvement available, because no new extraction is required."
    )
    add("")
    add(
        "This audit describes the application's own visibility rules, not a browser-by-browser review "
        "of each paper page. It also does not judge whether an individual question is mathematically "
        "correct; it reports only the state the app has recorded."
    )
    add("")

    with open(OUT, "w", encoding="utf-8", newline="\n") as handle:
        handle.write("\n".join(lines))

    print(f"wrote {OUT}")
    print(
        f"courses={totals['courses']} papers={totals['papers']} questions={totals['questions']} "
        f"visible={totals['visible']} flagged={totals['flagged']} pending={totals['pending']} "
        f"no_topic={totals['no_topic']} blank_solution={totals['blank_solution']}"
    )


if __name__ == "__main__":
    main()
