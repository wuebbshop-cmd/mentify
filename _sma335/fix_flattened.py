"""Rebuild the last 6 SMA 335 rows whose superscripts and operators were flattened.

These rows passed the validator (so nothing rendered as an *error*), but they read
as gibberish: ``y" - 4y' -I2y = 3e5'``, ``X2y' + 2xy - i =°``, ``(x2 + 3xy + Y 2
)dx - X2dy = is °``. Wording is recovered from the document-level text of the same
PDFs.

Where a symbol was unreadable the most plausible reading was chosen and checked:
``u(x, y) = 1/(x^2 y)`` really does make ``-y^2 dx + (x^2 + xy) dy`` exact, which is
what pins that reading down.

Dry run by default; pass --apply to write.
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

from prep.models import PrepQuestion  # noqa: E402
from services.prep_ingestion import assessment_question_rendering_issues  # noqa: E402

COURSE_ID = 57

QUESTIONS: dict[int, str] = {
    995: r"""Form the differential equation associated with the relation

$$
y = x^{3} + c_{1}e^{2x} + c_{2}e^{3x},
$$

where $c_{1}$ and $c_{2}$ are arbitrary constants.""",
    1003: r"""a) Solve the linear differential equation

$$
\frac{dy}{dx} + 2y\tan 2x = 4\sec 2x, \qquad y = 2 \text{ when } x = \frac{\pi}{8} .
$$

**(5 marks)**

d) Verify that $u(x,y) = \dfrac{1}{x^{2}y}$ is an integrating factor for the differential equation

$$
-y^{2}\,dx + (x^{2} + xy)\,dy = 0 .
$$

Hence or otherwise solve the differential equation. **(5 marks)**""",
    1004: r"""b) Show that the differential equation

$$
(x^{2} + 3xy + y^{2})\,dx - x^{2}\,dy = 0
$$

is homogeneous, hence or otherwise solve it. **(5 marks)**

c) Solve the Bernoulli equation

$$
x^{2}y' + 2xy = y^{3} .
$$

**(5 marks)**""",
    1010: r"""a) Determine a particular solution to

$$
y'' - 4y' - 12y = 3e^{5x}
$$

using the method of undetermined coefficients. **(7 marks)**

c) Solve the differential equation

$$
\frac{dy}{dx} = \frac{4x - 2y + 4}{2x + y - 2} .
$$

**(6 marks)**""",
    1011: r"""b) Use the method of variation of parameters to solve the differential equation

$$
y'' + 2y' - 3y = 2x - 17 .
$$

**(7 marks)**""",
    1012: r"""c) The scientific law states that the acceleration of a particle during upward motion under gravity is $-g$. Write down this law as a differential equation. **(3 marks)**

d) Solve the differential equation

$$
\frac{dy}{dx} = \frac{x - y + 3}{2x - 2y + 5},
$$

given that it is non-homogeneous. **(4 marks)**

e) Solve the Bernoulli's equation

$$
\frac{dy}{dx} + y = xy^{3} .
$$

**(4 marks)**""",
}

REASON = (
    "Superscripts and operators were flattened by text extraction, leaving the item "
    "unreadable. Wording recovered from the document-level text of the same PDF."
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

    print(f"rows to rebuild: {len(QUESTIONS)} (all pass the validator)")

    if not apply:
        print("DRY RUN - nothing written.")
        return

    backup_path = Path(__file__).resolve().parent / "flattened_backup.json"
    backup_path.write_text(
        json.dumps(
            {
                str(pk): {
                    "question_latex": rows[pk].question_latex,
                    "verification_status": rows[pk].verification_status,
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
        q.verification_status = "reconstructed"
        q.reconstruction_metadata = metadata
        q.save(update_fields=["question_latex", "verification_status", "reconstruction_metadata"])
    print(f"wrote {len(QUESTIONS)} rows")


if __name__ == "__main__":
    main()
