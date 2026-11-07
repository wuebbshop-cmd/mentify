"""Final clean-up: two trailing mark runs and the last flattened multi-part item."""
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

from prep.models import PrepQuestion  # noqa: E402
from repair import is_acceptable, repair_text  # noqa: E402
from services.prep_ingestion import assessment_question_rendering_issues  # noqa: E402

Q_1018 = r"""a) Determine the differential equation whose solution is

$$
y = A\cos 8x + B\sin 8x .
$$

**(4 marks)**

b) Solve the differential equation

$$
\frac{dy}{dx} = \sin x .
$$

**(3 marks)**

c) Solve the differential equation

$$
\frac{dy}{dx} + y\cot x = \operatorname{cosec} x .
$$

**(5 marks)**

d) Solve the differential equation

$$
(2D^{2} + 2D + 3)y = x^{3} .
$$

**(8 marks)**"""

REASON = (
    "Two-column scan flattened the fractions and superscripts. Wording recovered "
    "from the document-level text of the same PDF."
)


def main() -> None:
    apply = "--apply" in sys.argv

    # 1) trailing bold runs on two already-clean rows
    trim = []
    for pk in (1605, 1644):
        q = PrepQuestion.objects.get(pk=pk)
        before = q.question_latex or ""
        after, changes = repair_text(before)
        ok, why = is_acceptable(before, after)
        if after == before or not ok:
            print(f"ID {pk}: skipped ({why or 'no change'})")
            continue
        trim.append((q, after, changes))
        print(f"ID {pk}: {changes}")

    issues = assessment_question_rendering_issues(Q_1018)
    if issues:
        raise SystemExit(f"1018 fails the validator: {issues}")

    if not apply:
        print(f"\nwould trim {len(trim)} rows and rebuild ID 1018")
        print("DRY RUN - nothing written.")
        return

    for q, after, _changes in trim:
        q.question_latex = after
        q.save(update_fields=["question_latex"])

    q = PrepQuestion.objects.get(pk=1018)
    metadata = dict(q.reconstruction_metadata or {})
    metadata["reason"] = REASON
    q.question_latex = Q_1018
    q.verification_status = "reconstructed"
    q.reconstruction_metadata = metadata
    q.save(update_fields=["question_latex", "verification_status", "reconstruction_metadata"])
    print(f"applied: trimmed {len(trim)}, rebuilt 1018")


if __name__ == "__main__":
    main()
