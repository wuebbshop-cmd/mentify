"""Surgical repair of SMA 102 past-paper rows."""

from __future__ import annotations

import argparse
import io
import json
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

from prep.models import PrepQuestion  # noqa: E402
from services.prep_ingestion import assessment_question_rendering_issues  # noqa: E402

COURSE_ID = 36
HERE = Path(__file__).resolve().parent
BACKUP = HERE / "sma102_repair_backup.json"

TEXT = {
    476: r"""The quadratic equation \(x^2=(k-1)x+k\) has negative roots that differ by 3. Find:
(a) each root; **[4 marks]**
(b) the constant \(k\). **[1 mark]**""",
    479: r"""If the roots of the equation \(x^2-5x-7=0\) are \(\alpha\) and \(\beta\), find the equation whose roots are \(\frac{\alpha}{\beta}\) and \(\frac{\beta}{\alpha}\).""",
    485: r"""\(\alpha\) and \(\beta\) are the roots of the quadratic equation \(x^2-(k+2)x+k=0\).
(a) Find \(\alpha+\beta\) and \(\alpha\beta\) in terms of \(k\). **[2 marks]**
(b) If \((\alpha+1)(\beta+2)=4\), show that \(k\alpha=-2k\). **[2 marks]**
(c) Hence find the two values of \(k\). **[2 marks]**""",
    489: r"""The quadratic equation \(4x^2+7x-5=0\) has roots \(\alpha\) and \(\beta\). Find the quadratic equation whose roots are \(\alpha^2\) and \(\beta^2\), and leave your answer in the form \(ax^2+bx+c=0\), where \(a,b,c\in\mathbb{N}\).""",
    477: r"Solve the equation \(2x^3+5x^2-x-6=0\).",
    480: r"Factorize the polynomial \(f(x)=x^3-7x-6\) completely.",
    481: r"Find the remainder when \(f(x)=3x^3-7x^2+2x-3\) is divided by \(1-2x\).",
    488: r"Factorize completely \(f(x)=2x^3+x^2-8x-4\). Hence solve \(f(x)=0\).",
    490: r"""\(f(x)=2x^3+ax^2+bx-6\), where \(a\) and \(b\) are constants. When \(f(x)\) is divided by \(2x-1\), the remainder is \(-5\). When \(f(x)\) is divided by \(x+2\), there is no remainder. Find \(a\) and \(b\), and hence factorize \(f(x)\) completely.""",
    500: r"""Find the values of \(a\) and \(b\) if the polynomial \(2x^3+ax+b-15\) is divisible by both \(x-4\) and \(2x-1\). **[5 marks]**

Factorize \(x^4+x^3-3x^2-4x-4\) completely. **[4 marks]**

Solve the equation \(2^{2x-1}-9(2^{x-2})+1=0\). **[5 marks]**""",
    502: r"""1. State De Moivre's Theorem. **[2 marks]**
2. Find \((1+j\sqrt{3})^6\) and express your answer in the form \(a+bj\). **[5 marks]**
3. Simplify \(\frac{(1+j)^2}{1-j}\). **[4 marks]**
4. Given \(z_1=3-2j\), \(z_2=-3-4j\), and \(z_3=j-2\):
   1. Obtain \(3z_1-2z_2+z_3\). **[4 marks]**
   2. If \(z_1=r_1(\cos\theta_1+j\sin\theta_1)\) and \(z_2=r_2(\cos\theta_2+j\sin\theta_2)\), express \(\frac{z_1}{z_2}\) in terms of \(r_1,r_2,\theta_1,\theta_2\). **[5 marks]**""",
    505: r"""1. Prove by mathematical induction that
\[
1+3+5+\cdots+(2n-1)=n^2
\]
for every positive integer \(n\). **[3 marks]**

2. Express \(\frac{3+4i}{2+i}=x+iy\), where \(x,y\in\mathbb R\), and find \(x\) and \(y\). **[3 marks]**

3. Find \((1+i)^{20}\) and find the fourth roots of \(1\). **[7 marks]**

4. The roots of the equation \(3x^2-17x+2=0\) are \(\alpha\) and \(\beta\). Determine a quadratic equation whose roots are \(\alpha+1\) and \(\beta+1\). **[5 marks]**

5. A polynomial \(f(x)=6x^3+kx^2+x-2\) has \(3x-1\) as a factor. Determine \(k\). **[4 marks]**

6. In how many ways can 6 men and 6 women be seated at a round table so that men and women alternate? **[3 marks]**""",
    512: r"""1. Let \(f(x)=x^3-4x^2+ax+b\). If \(f(x)\) is divisible by \(x-3\) and leaves a remainder of \(4\) when divided by \(x-1\), find \(a\) and \(b\). **[3 marks]**

2. The roots of the quadratic equation \(2x^2+7x-3=0\) are \(\alpha\) and \(\beta\). Find a quadratic equation whose roots are \(\alpha+4\) and \(\beta+4\). **[5 marks]**

3. In a class of 100 students, 35 study Geography, 45 study History, and 10 study both. How many study either subject and how many study neither? **[3 marks]**

4. Solve the inequality \(|2x-1|<x+6\). **[4 marks]**

5. Simplify
\[
(A^c\cap B)\cup(A\cap B)\cup(A\cap B^c).
\]
**[1 mark]**""",
    522: r"""Find the values of \(a\) and \(b\) if the polynomial \(2x^3+ax+b-15\) is divisible by both \(x-4\) and \(2x-1\). **[5 marks]**

Factorize \(x^4+x^3-3x^2-4x-4\) completely. **[4 marks]**

Solve the equation \(2^{2x-1}-9(2^{x-2})+1=0\). **[5 marks]**""",
    527: r"""- (a) Find \(k\) so that the equation \(4x^2-8kx+9=0\) has roots which differ by 4, and hence find the resulting quadratic equations. **[5 Marks]**
- (b) Solve the inequality \(3x^2-8x+7>2x^2-3x+1\). **[5 Marks]**
- (c) When \(f(x)\) is divided by \(x+1\), the remainder is \(-9\), and when it is divided by \(2x-1\), the remainder is \(3\). Find the remainder when \(f(x)\) is divided by \((x+1)(2x-1)\). **[5 Marks]**
- (d) Solve the equation \(3x^3+7x^2-22x-8=0\). **[5 Marks]**""",
}

FOOTERS = (
    r"\n+\*\*INVOLVEMENT IN ANY EXAMINATION IRREGULARITY SHALL LEAD TO DISCONTINUATION\*\*.*\Z",
    r"\n+\*INVOLVEMENT IN ANY EXAMINATION IRREGULARITY SHALL LEAD TO DISCONTINUATION\*.*\Z",
    r"\n+\*\*Page \d+(?: of \d+)?\*\*.*\Z",
    r"\bINVOLVEMENT\s+IN\s+(?:ANY\s+)?EXAMINATION\s+IRREGULARITY\s+SHALL\s+LEAD\s+TO\s+DISCONTINUATION\b",
    r"\bPage\s+\d+\s+of\s+\d+\b",
    r"@\w+\d*\s+Nokia\s+\w+\d*",
)


def clean_visible_text(text: str) -> str:
    cleaned = text.strip()
    cleaned = re.sub(r"^(?:-\s*Compulsory-\s*|-\s*\}\s*|}\s*|\}\}\s*|\*\*\s*)+", "", cleaned)
    for pattern in FOOTERS:
        cleaned = re.sub(pattern, "", cleaned.strip(), flags=re.I | re.S)
    cleaned = cleaned.replace("\ufffd", "")
    cleaned = re.sub(r"[ \t]+\n", "\n", cleaned)
    cleaned = re.sub(r"\n{3,}", "\n\n", cleaned)
    return cleaned.strip()


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--apply", action="store_true")
    args = parser.parse_args()

    rows = list(
        PrepQuestion.objects.filter(
            Q(topic__course_id=COURSE_ID) | Q(paper__course_id=COURSE_ID)
        )
        .select_related("topic", "paper")
        .distinct()
        .order_by("id")
    )
    replacements = [
        q for q in rows if q.reconstructed_from_id and q.verification_status == "pending"
    ]
    source_ids = sorted({q.reconstructed_from_id for q in rows if q.reconstructed_from_id})

    print(f"SMA 102: {len({q.id for q in rows})} unique rows")
    print(f"superseded originals: {len(source_ids)}")
    print(f"pending replacements: {len(replacements)}")

    repairs = []
    for q in rows:
        if q.id in source_ids:
            continue
        new_text = TEXT.get(q.id)
        if new_text is None:
            new_text = clean_visible_text(q.question_latex or "")
        else:
            new_text = clean_visible_text(new_text)
        if new_text != (q.question_latex or ""):
            remaining = assessment_question_rendering_issues(new_text)
            repairs.append((q.id, q.verification_status, new_text, remaining))

    print(f"text repairs: {len(repairs)}")
    for qid, status, _text, remaining in repairs:
        print(f"  q{qid} {status}: {'OK' if not remaining else remaining}")

    if not args.apply:
        print("DRY RUN - nothing written. Re-run with --apply.")
        return 0

    backup = {
        str(q.id): {
            "question_latex": q.question_latex,
            "solution_latex": q.solution_latex,
            "verification_status": q.verification_status,
            "topic_id": q.topic_id,
            "number": q.number,
            "marks": q.marks,
            "reconstruction_metadata": q.reconstruction_metadata,
            "reconstructed_from_id": q.reconstructed_from_id,
        }
        for q in rows
    }
    BACKUP.write_text(json.dumps(backup, ensure_ascii=False, indent=1), encoding="utf-8")

    for qid, _status, new_text, remaining in repairs:
        if remaining:
            raise RuntimeError(f"q{qid} remains invalid: {remaining}")
        q = PrepQuestion.objects.get(pk=qid)
        q.question_latex = new_text
        if q.verification_status == "pending":
            q.verification_status = "reconstructed"
        q.save(update_fields=["question_latex", "verification_status"])

    for q in replacements:
        metadata = dict(q.reconstruction_metadata or {})
        metadata["review_status"] = "promoted_replacement"
        PrepQuestion.objects.filter(pk=q.id).update(
            verification_status="reconstructed",
            reconstruction_metadata=metadata,
        )

    deleted, _ = PrepQuestion.objects.filter(pk__in=source_ids).delete()
    print(f"deleted source rows: {deleted}")
    print(f"backup: {BACKUP}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
