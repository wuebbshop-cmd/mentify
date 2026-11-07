"""Last structural pass for SMA 335.

Three things:

1. ``sma335-doc-5a5f9882`` is the same paper as ``sma335-doc-a2814f82`` ingested 23
   seconds earlier without a source-document link, so it is unpublished.
2. Rows recovered from the assignment PDF (``699aa25e``) were split so badly that
   fragments of one question ended up in another (``Solve y' = x + x^2y^2`` was
   missing its numerator, which sat in the next row). Those are rebuilt from the
   document text.
3. The recoverable rows that were never attached to a topic are mapped to the topic
   their content belongs to, so they finally render.

Left untouched and reported to the user instead: the two vector-calculus rows in
paper ``5800930e`` (wrong subject for this course), the 10 empty source stubs, and
the 12 ``Adapted from Question N`` duplicates.
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

from prep.models import PrepPaper, PrepQuestion, PrepTopic  # noqa: E402
from services.prep_ingestion import assessment_question_rendering_issues  # noqa: E402

DUPLICATE_PAPER = "sma335-doc-5a5f9882"

QUESTIONS: dict[int, str] = {
    993: r"""a) Verify that $Ax^{2} + By^{2} = 1$ is the solution of the differential equation

$$
xy\frac{d^{2}y}{dx^{2}} + x\left(\frac{dy}{dx}\right)^{2} - y\frac{dy}{dx} = 0 .
$$

**(10 marks)**

b) If the population of a country doubles in 50 years, in how many years will it triple under the assumption that the rate of increase is proportional to the number of inhabitants? **(10 marks)**""",
    996: r"""Solve the differential equation

$$
y\left(1 + x^{2}\right)^{1/2}\,dy + x\sqrt{1 + y^{2}}\,dx = 0 .
$$

**(5 marks)**""",
    997: r"""Solve

$$
\sin^{-1}x\,\frac{dy}{dx} + y = 0, \qquad y\left(\tfrac{1}{2}\right) = \frac{\sqrt{1 - x^{2}}}{2} .
$$

**(4 marks)**""",
    998: r"""Solve the differential equation

$$
y' = \frac{xy^{2} - y}{x + x^{2}y^{2}} .
$$

**(5 marks)**""",
    999: r"""Solve

$$
(x + y)\,dy + (x - y)\,dx = 0 .
$$

**(7 marks)**""",
    1000: r"""Use the method of variation of parameters to solve

$$
y'' - 2y' + y = \frac{e^{x}}{1 + x^{2}} .
$$

**(5 marks)**""",
    1021: r"""Solve the initial value problem

$$
y'' + y' - 6y = 0, \qquad y(0) = 1, \quad y'(0) = 0 .
$$

**(5 marks)**""",
    1022: r"""Define the Wronskian of two functions, hence determine whether the functions $t$ and $e^{2t}$ are linearly independent or not. **(4 marks)**""",
    1480: r"""Solve the initial value problem

$$
9y'' - 12y' + 4y = 0, \qquad y(0) = 2, \quad y'(0) = -1 .
$$

**(6 marks)**""",
    1481: r"""Cobalt-60 is a radioactive element that is used in medical radiology. It has a half-life of 5.3 years. Suppose that an initial sample of Cobalt-60 has a mass of 100 grams. How long will it take for $90\%$ of the sample to decay? **(6 marks)**""",
    1482: r"""Solve

$$
(D^{4} + 2D^{2} + 1)y = 0 .
$$

**(6 marks)**""",
    1511: r"""(a) Find the differential equation of the orthogonal trajectories of the family of curves

$$
x^{2} + y^{2} = C .
$$

**(8 marks)**

(b) A small amount of a certain one-celled organism is placed in a beaker of liquid substance (food) and is kept stirred. The growth of the organism is known to satisfy the differential equation

$$
\frac{dp}{dt} = kp,
$$

where $p$ is the population during the initial phase of its growth. If the population triples in two hours, determine the natural growth rate $k$ and the doubling time. **(6 marks)**

(c) Solve the following differential equation using variation of parameters

$$
y'' - y' - 2y = \sin x .
$$

**(6 marks)**""",
}

TOPIC_MAP: dict[int, int] = {
    993: 171,   # verifying a proposed solution
    997: 172,   # first order, variables separable
    999: 172,   # homogeneous first order
    1021: 289,  # second order homogeneous, constant coefficients
    1022: 171,  # Wronskian / linear independence
    1480: 289,
    1481: 297,  # radioactive decay application
    1482: 293,  # linear equations of order n
    1511: 172,  # orthogonal trajectories
}

REASON = (
    "Fragments of neighbouring questions were mixed into this row by the text "
    "extraction. Rebuilt from the document-level text of the same PDF."
)


def main() -> None:
    apply = "--apply" in sys.argv

    rows = {q.id: q for q in PrepQuestion.objects.filter(pk__in=QUESTIONS)}
    missing = [pk for pk in QUESTIONS if pk not in rows]
    if missing:
        raise SystemExit(f"missing rows: {missing}")

    problems = [(pk, assessment_question_rendering_issues(t)) for pk, t in QUESTIONS.items()]
    problems = [(pk, i) for pk, i in problems if i]
    if problems:
        raise SystemExit(f"text fails the validator: {problems}")

    valid_topics = set(PrepTopic.objects.filter(course_id=57).values_list("id", flat=True))
    bad_topics = {k: v for k, v in TOPIC_MAP.items() if v not in valid_topics}
    if bad_topics:
        raise SystemExit(f"unknown topics: {bad_topics}")

    print(f"rows to rebuild: {len(QUESTIONS)} | rows to map: {len(TOPIC_MAP)}")
    print(f"paper to unpublish: {DUPLICATE_PAPER}")

    if not apply:
        print("DRY RUN - nothing written.")
        return

    backup_path = Path(__file__).resolve().parent / "structure_backup.json"
    backup_path.write_text(
        json.dumps(
            {
                str(pk): {
                    "question_latex": rows[pk].question_latex,
                    "verification_status": rows[pk].verification_status,
                    "topic_id": rows[pk].topic_id,
                }
                for pk in QUESTIONS
            },
            indent=1,
            ensure_ascii=False,
            default=str,
        ),
        encoding="utf-8",
    )
    print("backup written:", backup_path)

    for pk, text in QUESTIONS.items():
        q = rows[pk]
        metadata = dict(q.reconstruction_metadata or {})
        metadata["reason"] = REASON
        q.question_latex = text
        q.reconstruction_metadata = metadata
        fields = ["question_latex", "reconstruction_metadata"]
        if q.verification_status in ("flagged", "pending"):
            q.verification_status = "reconstructed"
            fields.append("verification_status")
        if pk in TOPIC_MAP:
            q.topic_id = TOPIC_MAP[pk]
            q.topic_label = ""
            fields += ["topic", "topic_label"]
        q.save(update_fields=fields)
    print(f"wrote {len(QUESTIONS)} rows")

    dup = PrepPaper.objects.filter(pk=DUPLICATE_PAPER).first()
    if dup and dup.is_published:
        dup.is_published = False
        dup.save(update_fields=["is_published"])
        print("unpublished duplicate paper", DUPLICATE_PAPER)


if __name__ == "__main__":
    main()
