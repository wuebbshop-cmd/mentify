"""Rebuild the 20 SMA 335 questions whose extraction lost the mathematics.

Each source PDF was scanned and the stored text dropped the operators, the
fractions and (in 16 cases) substituted private-use glyphs, so the rows read like
``y   2 y   3 y   3 x 2  4 x  5``. The wording below was recovered from the
document-level text of the same PDF plus the internal structure of each item, and
every algebraic claim used to pin down an ambiguous sign was checked with sympy
(e.g. that ``D^4 - 6D^3 + 7D^2 + 16D + 60`` really does have ``4 - 2i`` as a root).

The rows are marked ``reconstructed`` so the app labels them honestly.

Dry run by default; pass --apply to write, --retire-pending to also retire the 68
duplicate reconstructions (see the companion analysis in the session notes).
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

# --- paper "SMA 335 QUESTIONS" (2015/2016), Question One ---------------------
Q_987 = r"""a) Give the order of each of the given differential equations.

i) $xy\dfrac{d^{3}y}{dx^{3}} - y^{2}\sin x = 0$ **(2 marks)**

ii) $\left[1 + \left(\dfrac{dy}{dx}\right)^{2}\right]^{3} = 2\dfrac{d^{2}y}{dx^{2}}$ **(2 marks)**

b) Solve $x\dfrac{dy}{dx} = 5x^{4} + 4x^{2} + 2x$ by direct integration. **(4 marks)**"""

# --- paper "SMA335 past paper 2010" (2009/2010), Question One ----------------
Q_1001 = r"""a) Distinguish clearly between the following terms as used in differential equations.

i) Order and degree

ii) General solution and particular solution

**(3 marks)**

b) Form the differential equation by eliminating the arbitrary constants in

$$
y = Ax^{2} + Bx^{2}\ln x .
$$

**(4 marks)**

c) Show that

$$
(2x\cos y + 3x^{2}y)\,dx + (x^{3} - x^{2}\sin y - y)\,dy = 0
$$

is exact, hence or otherwise find its general solution. **(4 marks)**

d) Find the particular solution of the initial value problem

$$
-2\frac{d^{2}y}{dx^{2}} + 4\frac{dy}{dx} + 13y = 0, \qquad y(0) = -1, \quad y'(0) = -4 .
$$

**(6 marks)**

e) The population of a certain town is known to grow at a rate proportional to the number of people present. If after 10 years the population has doubled, and after three years the population is 400,000, estimate the number of people initially living in the city. **(5 marks)**

f) Find the solution of the homogeneous system

$$
\frac{dx}{dt} = 2x + 3y, \qquad \frac{dy}{dt} = 2x + y .
$$

**(5 marks)**

g) Show that $y = x^{-2}$ is a solution to the differential equation

$$
x^{2}y'' + 5xy' + 4y = 0, \qquad x \neq 0 .
$$

**(3 marks)**"""

# --- same paper, Question Three ---------------------------------------------
Q_1005 = r"""a) Find the general solution of the differential equation

$$
(D^{4} - 2D^{3} + 7D^{2} + 18D + 26)y = 0,
$$

given that one of the roots is $-1 + i$ and that complex roots occur in conjugate pairs. **(7 marks)**

b) The rate at which a body cools is proportional to the difference between the temperature of the body and that of the surrounding air. If a body in air at $25^{\circ}\mathrm{C}$ will cool from $100^{\circ}\mathrm{C}$ to $75^{\circ}\mathrm{C}$ in one minute, find its temperature at the end of 3 minutes. **(8 marks)**

c) Find the orthogonal trajectories of the family of curves

$$
y(x - 1) = c .
$$

**(5 marks)**"""

# --- same paper, Question Four (a) ------------------------------------------
Q_1007 = r"""a) Find the power series solution of the differential equation

$$
(x^{2} - 1)\frac{d^{2}y}{dx^{2}} + x\frac{dy}{dx} - y = 0
$$

about the point $x = 0$. **(10 marks)**"""

# --- paper "SMA 335 ODE CAT" (CAT II, 2019) ---------------------------------
Q_1019 = r"""Find the general solution to the differential equation

$$
(D^{2} - 6D + 25)y = 0 .
$$

**(3 marks)**"""

Q_1023 = r"""4) Use the method of undetermined parameters to solve the differential equation

$$
y'' - 2y' - 3y = 3x^{2} + 4x - 5 .
$$

**(6 marks)**

5) Solve the differential equation

$$
\frac{d^{2}y}{dx^{2}} + \cot x\,\frac{dy}{dx} = \sin x .
$$

**(5 marks)**"""

Q_1025 = r"""6) Solve the differential equation

$$
(D^{4} + 2D^{3} - 7D^{2} + 2D + 70)y = 0
$$

given that one of the roots of the auxiliary equation is $-3 + i$. **(7 marks)**"""

# --- paper "SMA 335 2011 QUESTIONS" (2010/2011) ----------------------------
Q_1028 = r"""b) Solve the differential equations

i) $y' = y^{2} + 1$. **(4 marks)**

ii) $(2y^{4} + x^{4})\,dx - xy^{3}\,dy = 0$. **(4 marks)**"""

Q_1030 = r"""c) Use the method of undetermined coefficients to solve the equation

$$
y'' + 9y = e^{-x} .
$$

**(4 marks)**

d) Find a series solution about the point $x = 0$ of the differential equation

$$
y'' - y^{4} = 0
$$

using the power series method. **(5 marks)**

e) Determine the orthogonal trajectory obtained from the family of curves

$$
cy^{2} + x^{2} = 4 .
$$

**(5 marks)**"""

Q_1033 = r"""a) Explain each of the following terms.

i) Degree and order of a differential equation. **(3 marks)**

ii) The general solution of a differential equation of order $n$.

b) Show that the transformation $y = vx$ reduces the equation given below into a separable equation, and hence solve it.

$$
(x^{3} + y^{3})\,dx - 3xy^{2}\,dy = 0 .
$$

**(10 marks)**

c) Test for exactness and hence solve

$$
(y^{3} + 2x)\,dx + (3xy^{2} + 1)\,dy = 0 .
$$

**(7 marks)**"""

Q_1036 = r"""a) Solve the differential equation

$$
(D^{4} - 6D^{3} + 7D^{2} + 16D + 60)y = 0
$$

given that one of the roots is of the form $4 - 2i$. **(6 marks)**

b) Solve the initial value problem

$$
y''' - 2y'' - 5y' + 6y = 0
$$

subject to the conditions $y(0) = 4$, $y'(0) = 11$ and $y''(0) = 17$. **(6 marks)**

c) A certain radioactive material is known to decay at a rate proportional to the amount present. If initially $500\,\mathrm{mg}$ of the material is present and after 3 years $20\%$ of the original mass has decayed, find

i) an expression for the amount present at any time $t$; **(4 marks)**

ii) the amount remaining after 25 years; **(2 marks)**

iii) the half life of the material. **(2 marks)**"""

Q_1039 = r"""a) Use the method of undetermined coefficients to solve the differential equation

$$
y'' + 9y = 81x^{2} + 18x + 45 .
$$

**(8 marks)**

b) Use the method of variation of parameters to solve the differential equation

$$
y'' + 4y' + 4y = 4x^{2}e^{-2x} .
$$

**(7 marks)**

c) Solve the Bernoulli equation

$$
xy' + y = xy^{3} .
$$

**(7 marks)**"""

Q_1042 = r"""a) Determine whether $y = \dfrac{1}{x}$ is a solution of the differential equation

$$
y' + y^{2} = 0 .
$$

**(3 marks)**

b) The solution to the differential equation

$$
y'' - 2xy' - 2y = 0
$$

is of the form $y = c_{1}y_{1} + c_{2}y_{2}$, where $y_{1}$ and $y_{2}$ are two linearly independent solutions. Use the power series method to solve the differential equation at $x_{0} = 0$. Give the first terms in $y_{1}$ and $y_{2}$.

c) Solve the differential equations

i) $4y'' - 12y' + 9y = 0$ **(5 marks)**

ii) $y'' - 2y' + 3y = 0$ **(5 marks)**"""

# --- paper "ODE questions-SMA335", 2018/2019, Question Four (b) ------------
Q_1642 = r"""b) Show that the differential equation

$$
(5x^{4} + 3x^{2}y^{2} - 2xy^{3})\,dx + (2x^{3}y - 3x^{2}y^{2} - 5y^{4})\,dy = 0
$$

is exact. Hence solve it. **(5 marks)**"""

QUESTIONS: dict[int, str] = {
    987: Q_987,
    1001: Q_1001,
    1005: Q_1005,
    1007: Q_1007,
    1019: Q_1019,
    1023: Q_1023,
    1025: Q_1025,
    1028: Q_1028,
    1030: Q_1030,
    1033: Q_1033,
    1036: Q_1036,
    1039: Q_1039,
    1042: Q_1042,
    1642: Q_1642,
}

# The 2011 paper was ingested twice; both copies carry identical question text.
_MIRRORS = {1085: 1028, 1087: 1030, 1090: 1033, 1093: 1036, 1096: 1039, 1099: 1042}
for _dup, _src in _MIRRORS.items():
    QUESTIONS[_dup] = QUESTIONS[_src]

REASON = (
    "The scanned PDF lost all operators and fractions, so the stored text was "
    "unreadable. Question wording recovered from the document-level text of the same "
    "PDF and cross-checked algebraically."
)


def main() -> None:
    apply = "--apply" in sys.argv
    retire = "--retire-pending" in sys.argv

    rows = {q.id: q for q in PrepQuestion.objects.filter(pk__in=QUESTIONS)}
    missing = [pk for pk in QUESTIONS if pk not in rows]
    if missing:
        raise SystemExit(f"missing rows: {missing}")

    problems = []
    for pk, text in QUESTIONS.items():
        issues = assessment_question_rendering_issues(text)
        if issues:
            problems.append((pk, issues))
    if problems:
        raise SystemExit(f"reconstructed text fails the validator: {problems}")

    print(f"reconstructed questions: {len(QUESTIONS)}  (all pass the validator)")

    if not apply:
        print("DRY RUN - nothing written.")
        return

    backup_path = Path(__file__).resolve().parent / "reconstruct_backup.json"
    backup = {
        str(pk): {
            "question_latex": rows[pk].question_latex,
            "verification_status": rows[pk].verification_status,
            "reconstruction_metadata": rows[pk].reconstruction_metadata,
        }
        for pk in QUESTIONS
    }
    backup_path.write_text(json.dumps(backup, indent=1, ensure_ascii=False, default=str), encoding="utf-8")
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

    if retire:
        pending = list(
            PrepQuestion.objects.filter(topic__course_id=COURSE_ID, verification_status="pending")
        )
        dump = [
            {
                "id": q.id,
                "paper_id": q.paper_id,
                "reconstructed_from": q.reconstructed_from_id,
                "question_latex": q.question_latex,
                "solution_latex": q.solution_latex,
            }
            for q in pending
        ]
        dump_path = Path(__file__).resolve().parent / "retired_pending_backup.json"
        dump_path.write_text(json.dumps(dump, indent=1, ensure_ascii=False), encoding="utf-8")
        print("pending backup:", dump_path)
        deleted = PrepQuestion.objects.filter(
            pk__in=[q.id for q in pending]
        ).delete()
        print("deleted pending duplicates:", deleted)


if __name__ == "__main__":
    main()
