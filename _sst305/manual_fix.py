"""Final SST 305 pass: the 10 rows the deterministic rules cannot fix.

Three groups:

* ``74``, ``75``, ``77`` were extracted as plain text with the mathematics lost
  (the Poisson indicator even came through as ``(cid:40)``). They are rebuilt from
  the CAT 2 source text.
* ``194`` ends mid-sentence and ``195`` is its orphaned tail, so the tail is folded
  back in and ``195`` retired.
* ``207`` and ``217`` stop at an advertising box before the table they need; the
  same question survives intact as row ``197``, which is reused.
* ``215`` has two tables from a different question pasted into it, and ``237`` still
  has a broken fence.
* ``228`` and ``234`` already pass the validator - their flag is stale, and running
  the repair over them actually *introduces* a defect, so they are promoted untouched.

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

COURSE_ID = 27

Q_74 = r"""Let $x_{1}, x_{2}, \ldots, x_{n}$ denote a random sample from a Beta distribution

$$
f(x, \alpha, \beta) = \frac{\Gamma(\alpha+\beta)}{\Gamma\alpha\,\Gamma\beta}\, x^{\alpha-1}(1-x)^{\beta-1}, \qquad 0 < x < 1,
$$

with parameters $\alpha > 0$, $\beta > 0$ unknown. Show that the family of Beta distributions with parameters $\alpha$ and $\beta$ unknown belongs to a two-parameter exponential family, hence determine a jointly sufficient statistic for $\alpha$ and $\beta$. **(3 marks)**"""

Q_75 = r"""Let $x_{1}, x_{2}, x_{3}, \ldots, x_{n}$ be a random sample, and take $\phi(\theta) = \theta^{1-\theta}$. Find

(a) Fisher's information $I(\theta)$ **(3 marks)**

(b) the Cramér-Rao lower bound for $d(x)$ **(3 marks)**

(c) the minimum variance best unbiased estimator of $\theta$. **(3 marks)**"""

Q_77 = r"""Suppose that $x_{1}, x_{2}, \ldots, x_{n}$ form a random sample from a Poisson distribution with mean $\lambda > 0$. Given the estimator

$$
\delta(X) = \begin{cases} 1, & x = 0 \\ 0, & x > 0 \end{cases}
$$

(a) Show that $E(\delta(X)) = e^{-\lambda}$. **(2 marks)**

(b) Find an unbiased estimator of $e^{-\lambda}$ with a smaller value than $\delta(X)$. (Hint: you may use $T = \sum_{i=1}^{n} X_{i}$ as a sufficient statistic in this case.) **(4 marks)**"""

Q_215 = r"""a) Let $X_{1}, X_{2}, \dots, X_{n}$ be i.i.d. as $B(k, p)$ (binomial with parameters $k$ and $p$), where both $k$ and $p$ are unknown. Find, by the method of moments, the estimators of $k$ and $p$. **(10 marks)**

[You may find this useful: If $X$ is $B(n,p)$, then $E(X) = np$ and the variance of $X$ is $np(1-p)$.]

b) In (a) above, assume $k$ is known. Show whether the moment estimator of $p$ is

i. unbiased; **(4 marks)**

ii. consistent. **(6 marks)**"""

Q_237 = r"""a) A random sample of 18 venture-capital investments in the fiber optics sector yields the following data, in US dollars:

$$
\begin{array}{ccccccccc}
2.04 & 5.48 & 5.60 & 5.96 & 6.27 & 10.51 & 4.13 & 5.58 & 5.74 \\
6.67 & 8.63 & 6.71 & 4.98 & 6.66 & 7.71 & 8.64 & 9.21 & 5.95
\end{array}
$$

(i) Determine a $95\%$ confidence interval for the mean amount, $\mu$, of all venture-capital investments in the fiber optics sector. Assume that the population standard deviation is $2.04$ dollars.

(ii) Interpret your findings in part (i). **(1 mark)**

(iii) Find a $99\%$ confidence interval for $\mu$. **(3 marks)**

(iv) Which confidence interval yields a more precise estimate of $\mu$? Explain your answer. **(1 mark)**

b) Measurements on the percentage of enrichment of 12 fuel rods were reported as follows:

$$
\begin{array}{cccccccccccc}
2.94 & 3 & 2.9 & 2.75 & 3 & 2.95 & 2.75 & 2.95 & 2.92 & 2.81 & 3.05 & 2.8
\end{array}
$$

If $\sum X = 34.82$ and $\sum X^{2} = 101.1486$, find a $99\%$ two-sided confidence interval on the mean percentage of enrichment of the fuel rods. Can we state that the mean percentage of enrichment is $2.95\%$? Why? **(5 marks)**

c) A random sample of 100 boys has a mean height of $152.3$ cm and a standard deviation of $6$ cm, while a random sample of 120 girls of the same age has a mean height of $148.6$ cm and a standard deviation of $5$ cm. Construct a $95\%$ confidence interval for the difference in overall mean height between boys and girls, $\mu_{1} - \mu_{2}$, where $\mu_{1}$ and $\mu_{2}$ are the mean heights of boys and girls respectively. Assume that the populations of heights of boys and girls have unequal variances. **(5 marks)**"""

Q_194_TAIL = r"""

i. unbiased; **(4 marks)**

ii. consistent. **(6 marks)**"""

REPLACE = {74: Q_74, 75: Q_75, 77: Q_77, 215: Q_215, 237: Q_237}
PROMOTE_UNTOUCHED = [228, 234]
DELETE = [195]
COPY_FROM_197 = [207, 217]


def main() -> None:
    apply = "--apply" in sys.argv

    for pk, text in REPLACE.items():
        issues = assessment_question_rendering_issues(text)
        if issues:
            raise SystemExit(f"{pk} fails the validator: {issues}")
    for pk in PROMOTE_UNTOUCHED:
        current = PrepQuestion.objects.get(pk=pk).question_latex or ""
        issues = assessment_question_rendering_issues(current)
        if issues:
            raise SystemExit(f"{pk} is not actually clean: {issues}")
    source = PrepQuestion.objects.get(pk=197).question_latex or ""
    if assessment_question_rendering_issues(source):
        raise SystemExit("197 is not clean, cannot copy")

    print(f"rebuild: {sorted(REPLACE)}")
    print(f"copy from 197: {COPY_FROM_197}")
    print(f"fold 195 into 194, then delete 195")
    print(f"promote untouched: {PROMOTE_UNTOUCHED}")

    if not apply:
        print("DRY RUN - nothing written.")
        return

    backup_path = Path(__file__).resolve().parent / "manual_backup.json"
    backup = {
        str(pk): {
            "question_latex": PrepQuestion.objects.get(pk=pk).question_latex,
            "verification_status": PrepQuestion.objects.get(pk=pk).verification_status,
        }
        for pk in sorted(set(REPLACE) | set(PROMOTE_UNTOUCHED) | set(COPY_FROM_197) | set(DELETE) | {194})
    }
    backup_path.write_text(json.dumps(backup, indent=1, ensure_ascii=False, default=str), encoding="utf-8")
    print("backup written:", backup_path)

    for pk, text in REPLACE.items():
        q = PrepQuestion.objects.get(pk=pk)
        metadata = dict(q.reconstruction_metadata or {})
        metadata["reason"] = (
            "Text extraction lost the mathematics (plain-text fractions, superscripts "
            "and a character-map placeholder). Rebuilt from the source document."
        )
        q.question_latex = text
        q.verification_status = "reconstructed"
        q.reconstruction_metadata = metadata
        q.save(update_fields=["question_latex", "verification_status", "reconstruction_metadata"])
    print(f"rebuilt {len(REPLACE)}")

    row194 = PrepQuestion.objects.get(pk=194)
    row194.question_latex = (row194.question_latex or "").rstrip() + Q_194_TAIL
    row194.save(update_fields=["question_latex"])
    issues = assessment_question_rendering_issues(row194.question_latex)
    print("194 after fold:", issues or "clean")

    for pk in COPY_FROM_197:
        q = PrepQuestion.objects.get(pk=pk)
        metadata = dict(q.reconstruction_metadata or {})
        metadata["reason"] = (
            "Extraction stopped at an advertising box before the table this question "
            "needs. The intact copy of the same question (row 197) is reused."
        )
        q.question_latex = source
        q.verification_status = "reconstructed"
        q.reconstruction_metadata = metadata
        q.save(update_fields=["question_latex", "verification_status", "reconstruction_metadata"])
    print(f"restored {len(COPY_FROM_197)} from 197")

    for pk in PROMOTE_UNTOUCHED:
        q = PrepQuestion.objects.get(pk=pk)
        q.verification_status = "auto_validated"
        q.save(update_fields=["verification_status"])
    print(f"promoted {PROMOTE_UNTOUCHED}")

    deleted = PrepQuestion.objects.filter(pk__in=DELETE).delete()
    print("deleted orphan fragment:", deleted)


if __name__ == "__main__":
    main()
