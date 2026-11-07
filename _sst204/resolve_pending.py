"""Resolve the 23 SST 204 'pending' questions.

Each pending row is an AI reconstruction whose declaring original is now a
repaired, published row in the SAME paper. Editorial decision:

* the authentic extracted text wins (reconstructions of the same source were
  frequently off-topic, e.g. a Poisson question rewritten as a normal one);
* therefore the 23 pending duplicates are retired;
* the surviving originals get a verified worked solution and their leftover
  extraction artefacts (page footers, stray markdown) removed, so nothing is
  lost and nothing is shown twice.

Run with no arguments for a dry run; pass --apply to write.
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

COURSE_ID = 46  # SST 204 - Probability and Statistics 1

# --------------------------------------------------------------------------
# Worked solutions for the surviving originals (hand-derived, numerically
# cross-checked with Python/sympy).
# --------------------------------------------------------------------------

POISSON_TYPOS = r"""Let $X$ be the number of typos on a randomly selected page, with $X \sim \mathrm{Poisson}(\lambda)$ and $\lambda = 3$. Then

$$
P(X=x) = \frac{e^{-3} 3^x}{x!}, \qquad x = 0, 1, 2, \dots
$$

**(i)** It is easier to work with the complement:

$$
P(X \ge 1) = 1 - P(X = 0) = 1 - e^{-3} = 1 - 0.049787 \approx 0.9502 .
$$

So the probability that a page carries at least one typo is approximately $0.9502$.

**(ii)** We need the two smallest possible counts:

$$
P(X \le 1) = P(X=0) + P(X=1) = e^{-3} + 3e^{-3} = 4e^{-3} = 4(0.049787) \approx 0.1991 .
$$

So the probability that a page carries at most one typo is approximately $0.1991$.
"""

BINOMIAL_UNIFORM = r"""Write $X \sim B(12, p)$, so that

$$
P(X=k) = \binom{12}{k} p^k (1-p)^{12-k}.
$$

**(1) With $p = 0.2$**

(i) Taking $k = 5$,

$$
P(X=5) = \binom{12}{5}(0.2)^5(0.8)^7 = 792 \times 0.00032 \times 0.2097152 \approx 0.0532 .
$$

(ii) Only three values reach $10$ or more:

$$
P(X \ge 10) = \sum_{k=10}^{12} \binom{12}{k}(0.2)^k(0.8)^{12-k}.
$$

Term by term, $\binom{12}{10}(0.2)^{10}(0.8)^2 = 66(1.024\times 10^{-7})(0.64) \approx 4.33\times 10^{-6}$, $\binom{12}{11}(0.2)^{11}(0.8) = 12(2.048\times 10^{-8})(0.8) \approx 1.97\times 10^{-7}$ and $(0.2)^{12} = 4.096\times 10^{-9}$. Hence

$$
P(X \ge 10) \approx 4.33\times 10^{-6} + 1.97\times 10^{-7} + 4.10\times 10^{-9} \approx 4.53\times 10^{-6},
$$

a probability of roughly $0.0000045$.

**(2)** Since $P(X=0) = (1-p)^{12} = 0.05$,

$$
1-p = 0.05^{1/12} \approx 0.7791 \quad\Longrightarrow\quad p \approx 0.2209 .
$$

So $p = 0.221$ to three decimal places.

**(3)** With $n = 12$ and $\operatorname{Var}(X) = 12p(1-p) = 1.92$,

$$
p(1-p) = 0.16 \quad\Longrightarrow\quad p^2 - p + 0.16 = 0 .
$$

That factorises as $(p-0.2)(p-0.8) = 0$, so the possible values are $p = 0.2$ or $p = 0.8$.

**The game with sticks.** Let $L$ be the length of a stick, with $L \sim U(7, 10)$. Its density is $\frac{1}{3}$ on $[7,10]$.

(i) The stick is shorter than $9.5$ cm with probability

$$
P(L < 9.5) = \frac{9.5-7}{10-7} = \frac{2.5}{3} \approx 0.8333 .
$$

(ii) The heaviest of three sticks exceeds $9.5$ cm unless all three are shorter than $9.5$ cm, so

$$
P(\text{win bag of sweets}) = 1 - \left(\frac{2.5}{3}\right)^3 = 1 - 0.5787 \approx 0.4213 .
$$

(iii) Let $Y$ be the number of the six sticks shorter than $9.5$ cm. Then $Y \sim B\left(6, \frac{5}{6}\right)$ and

$$
P(Y > 4) = \binom{6}{5}\left(\frac{5}{6}\right)^5\left(\frac{1}{6}\right) + \left(\frac{5}{6}\right)^6 \approx 0.4019 + 0.3349 \approx 0.7368 .
$$
"""

TELEPHONE = r"""**(i)** The probabilities must add up to one. Summing the table with $p$ kept symbolic,

$$
p + \frac{1}{5} + \frac{1}{4} + \frac{1}{5} + 2p + \frac{3}{20} + p = 1 .
$$

The coefficients of $p$ give $4p$, and the constants give

$$
\frac{1}{5} + \frac{1}{4} + \frac{1}{5} + \frac{3}{20} = \frac{4}{20} + \frac{5}{20} + \frac{4}{20} + \frac{3}{20} = \frac{16}{20} = \frac{4}{5} .
$$

Hence $4p + \frac{4}{5} = 1$, so $4p = \frac{1}{5}$ and $p = \frac{1}{20}$, as required.

With $p = \frac{1}{20}$ the distribution is

$$
P(X=0)=\frac{1}{20},\quad P(X=1)=\frac{1}{5},\quad P(X=2)=\frac{1}{4},\quad P(X=3)=\frac{1}{5},\quad P(X=4)=\frac{1}{10},\quad P(X=5)=\frac{3}{20},\quad P(X=6)=\frac{1}{20}.
$$

**(ii)** Working with the complement,

$$
P(X \ge 3) = 1 - P(X \le 2) = 1 - \left(\frac{1}{20} + \frac{1}{5} + \frac{1}{4}\right) = 1 - \left(\frac{1}{20} + \frac{4}{20} + \frac{5}{20}\right) = 1 - \frac{1}{2} = \frac{1}{2} .
$$

**(iii)** The expectation is

$$
E(X) = \sum_{x=0}^{6} x\,P(X=x) = 0 + \frac{1}{5} + \frac{2}{4} + \frac{3}{5} + \frac{4}{10} + \frac{15}{20} + \frac{6}{20} .
$$

Putting everything over $20$, this is $\frac{4+10+12+8+15+6}{20} = \frac{55}{20} = \frac{11}{4} = 2.75$, so the office expects $2.75$ calls in the hour.

**(iv)** By definition

$$
M_X(t) = E\left(e^{tX}\right) = \sum_{x=0}^{6} e^{tx} P(X=x),
$$

so

$$
M_X(t) = \frac{1}{20} + \frac{1}{5}e^{t} + \frac{1}{4}e^{2t} + \frac{1}{5}e^{3t} + \frac{1}{10}e^{4t} + \frac{3}{20}e^{5t} + \frac{1}{20}e^{6t} .
$$

**(v)** Differentiating once,

$$
M_X'(t) = \frac{1}{5}e^{t} + \frac{1}{2}e^{2t} + \frac{3}{5}e^{3t} + \frac{2}{5}e^{4t} + \frac{3}{4}e^{5t} + \frac{3}{10}e^{6t},
$$

and at $t = 0$ this is $\frac{1}{5}+\frac{1}{2}+\frac{3}{5}+\frac{2}{5}+\frac{3}{4}+\frac{3}{10} = \frac{11}{4}$, confirming $E(X) = 2.75$.

Differentiating again,

$$
M_X''(t) = \frac{1}{5}e^{t} + e^{2t} + \frac{9}{5}e^{3t} + \frac{8}{5}e^{4t} + \frac{15}{4}e^{5t} + \frac{9}{5}e^{6t},
$$

so at $t=0$,

$$
E\left(X^2\right) = M_X''(0) = \frac{1}{5} + 1 + \frac{9}{5} + \frac{8}{5} + \frac{15}{4} + \frac{9}{5} = \frac{4+20+36+32+75+36}{20} = \frac{203}{20} = 10.15 .
$$

Therefore

$$
\operatorname{Var}(X) = E\left(X^2\right) - \left[E(X)\right]^2 = 10.15 - 7.5625 = 2.5875,
$$

and the standard deviation is

$$
\sigma_X = \sqrt{2.5875} \approx 1.6086 .
$$

So the mean is $2.75$ calls and the standard deviation is approximately $1.61$ calls.
"""

STICKS_UNIFORM = r"""Let $L$ be the length of a stick, with $L \sim U(7, 10)$. Its density is $\frac{1}{3}$ on $[7, 10]$ and zero elsewhere, so for $7 \le a < b \le 10$,

$$
P(a < L < b) = \frac{b-a}{10-7} = \frac{b-a}{3}.
$$

**(i)** The probability that a stick is shorter than $9.5$ cm is

$$
P(L < 9.5) = \frac{9.5 - 7}{3} = \frac{2.5}{3} \approx 0.8333 .
$$

**(ii)** The longest of three sticks exceeds $9.5$ cm unless all three are shorter than $9.5$ cm, and the three draws are independent. Hence

$$
P(\text{win a bag of sweets}) = 1 - P(\text{all three} < 9.5) = 1 - \left(\frac{2.5}{3}\right)^3 .
$$

Since $\left(\frac{2.5}{3}\right)^3 = \frac{15.625}{27} \approx 0.5787$,

$$
P(\text{win a bag of sweets}) \approx 1 - 0.5787 = 0.4213 .
$$

**(iii)** Let $Y$ be the number of the six sticks that are shorter than $9.5$ cm. Each stick is short with probability $p = \frac{5}{6}$, so $Y \sim B\left(6, \frac{5}{6}\right)$ and

$$
P(Y > 4) = P(Y=5) + P(Y=6) = \binom{6}{5}\left(\frac{5}{6}\right)^5\left(\frac{1}{6}\right) + \left(\frac{5}{6}\right)^6 .
$$

Now $\binom{6}{5}\left(\frac{5}{6}\right)^5\left(\frac{1}{6}\right) = 6 \cdot \frac{3125}{7776} \cdot \frac{1}{6} = \frac{3125}{7776} \approx 0.4019$ and $\left(\frac{5}{6}\right)^6 = \frac{15625}{46656} \approx 0.3349$, so

$$
P(\text{win a soft toy}) \approx 0.4019 + 0.3349 = 0.7368 .
$$
"""

IQ_NORMAL = r"""Let $X$ be the IQ score, with $X \sim N(100, 225)$. The standard deviation is

$$
\sigma = \sqrt{225} = 15 .
$$

A candidate qualifies when the score lies in the top $1\%$, so the cut-off $c$ must satisfy $P(X \ge c) = 0.01$, that is $P(X < c) = 0.99$. Standardising with $Z = \dfrac{X-100}{15} \sim N(0,1)$,

$$
P\left(Z < \frac{c-100}{15}\right) = 0.99 .
$$

The $99$th percentile of the standard normal distribution is $z_{0.99} \approx 2.3263$, hence

$$
\frac{c-100}{15} = 2.3263 \quad\Longrightarrow\quad c = 100 + 15(2.3263) = 134.895 .
$$

So the cut-off point should be set at about $134.9$, or $135$ if only whole scores are reported.
"""

COIN_AND_DICE = r"""**(b)** Let $X$ be the number of tails in three tosses of a fair coin. Then $X \sim B\left(3, \frac{1}{2}\right)$, so

$$
E(X) = np = 3\left(\frac{1}{2}\right) = \frac{3}{2} = 1.5 ,
$$

$$
\operatorname{Var}(X) = np(1-p) = 3\left(\frac{1}{2}\right)\left(\frac{1}{2}\right) = \frac{3}{4} = 0.75 ,
$$

and

$$
\sigma_X = \sqrt{\frac{3}{4}} = \frac{\sqrt{3}}{2} \approx 0.8660 .
$$

**(d)** One throw of two dice gives $36$ equally likely ordered outcomes. A total of $8$ arises from $(2,6)$, $(3,5)$, $(4,4)$, $(5,3)$ and $(6,2)$, so the success probability on a single throw is

$$
p = \frac{5}{36} .
$$

Let $N$ be the number of throws needed to obtain the first total of $8$. Then $N$ is geometric with parameter $p$, so

$$
E(N) = \frac{1}{p} = \frac{36}{5} = 7.2
$$

and

$$
\operatorname{Var}(N) = \frac{1-p}{p^2} = \frac{31/36}{25/1296} = \frac{31}{36}\cdot\frac{1296}{25} = \frac{1116}{25} = 44.64 .
$$

The number of throws *before* a total of $8$ is obtained is $N-1$, which shifts the mean by one and leaves the variance unchanged:

$$
E(N-1) = \frac{36}{5} - 1 = \frac{31}{5} = 6.2, \qquad \operatorname{Var}(N-1) = \frac{1116}{25} = 44.64 .
$$

So the mean number of throws before a total of $8$ is $6.2$ and the variance is $44.64$ (equivalently, the mean number of throws including the successful one is $7.2$ with the same variance).
"""

RADISH = r"""Let $X$ be the number of the nine seeds that germinate. Each seed germinates independently with probability $0.8$, so $X \sim B(9, 0.8)$ and

$$
P(X = k) = \binom{9}{k} (0.8)^k (0.2)^{9-k} .
$$

**(i)** For no germination at all,

$$
P(X = 0) = (0.2)^9 = 5.12 \times 10^{-7},
$$

which is about $0.0000005$.

**(ii)** For at least seven,

$$
P(X \ge 7) = P(X=7) + P(X=8) + P(X=9),
$$

and term by term $\binom{9}{7}(0.8)^7(0.2)^2 = 36(0.2097152)(0.04) \approx 0.30199$, $\binom{9}{8}(0.8)^8(0.2) = 9(0.16777216)(0.2) \approx 0.30199$ and $(0.8)^9 \approx 0.13422$. Hence

$$
P(X \ge 7) \approx 0.30199 + 0.30199 + 0.13422 = 0.7382 .
$$

**(iii)** The expected number is

$$
E(X) = np = 9(0.8) = 7.2 ,
$$

so the gardener can expect about seven of the nine seeds to germinate.
"""

DENSITY_TRANSFORM = r"""First recover $k$. Since $f$ must integrate to one over $[-1, 1]$,

$$
\int_{-1}^{1} kx^2(1-x)\,dx = k\left[\frac{x^3}{3} - \frac{x^4}{4}\right]_{-1}^{1} = k\left(\frac{2}{3} - 0\right) = \frac{2k}{3} = 1,
$$

so $k = \frac{3}{2}$ and

$$
f(x) = \frac{3}{2}x^2(1-x), \qquad -1 \le x \le 1 .
$$

Now $Y = 1 - X$ maps $[-1,1]$ onto $[0,2]$, and $X = 1 - Y$. For $0 \le y \le 2$,

$$
G(y) = P(Y \le y) = P(1 - X \le y) = P(X \ge 1 - y) = \int_{1-y}^{1} \frac{3}{2}x^2(1-x)\,dx .
$$

Since $\frac{3}{2}x^2(1-x) = \frac{3}{2}x^2 - \frac{3}{2}x^3$,

$$
G(y) = \left[\frac{x^3}{2} - \frac{3x^4}{8}\right]_{1-y}^{1} = \frac{1}{8} - \frac{(1-y)^3}{2} + \frac{3(1-y)^4}{8} .
$$

Differentiating with respect to $y$,

$$
g(y) = \frac{3(1-y)^2}{2} - \frac{3(1-y)^3}{2} = \frac{3}{2}(1-y)^2\bigl[1 - (1-y)\bigr],
$$

so

$$
g(y) = \frac{3}{2}y(1-y)^2, \qquad 0 \le y \le 2,
$$

and $g(y) = 0$ otherwise. As a check,

$$
\int_{0}^{2} \frac{3}{2}y(1-y)^2\,dy = \frac{3}{2}\left[\frac{y^2}{2} - \frac{2y^3}{3} + \frac{y^4}{4}\right]_{0}^{2} = \frac{3}{2}\left(2 - \frac{16}{3} + 4\right) = 1 .
$$
"""

COMPANY_PROFIT = r"""**(i)** The random variable $X$ takes the three values $2.5$, $0.2$ and $-0.3$ (millions) with probabilities $0.4$, $0.25$ and $0.35$, so its distribution is

$$
\begin{array}{c|ccc}
x & 2.5 & 0.2 & -0.3 \\ \hline
P(X = x) & 0.4 & 0.25 & 0.35
\end{array}
$$

**(ii)** The expected profit is

$$
E(X) = (2.5)(0.4) + (0.2)(0.25) + (-0.3)(0.35) = 1 + 0.05 - 0.105 = 0.945 .
$$

For the second moment,

$$
E\left(X^2\right) = (2.5)^2(0.4) + (0.2)^2(0.25) + (-0.3)^2(0.35) = 2.5 + 0.01 + 0.0315 = 2.5415 .
$$

Hence

$$
\operatorname{Var}(X) = 2.5415 - (0.945)^2 = 2.5415 - 0.893025 = 1.648475 ,
$$

and the standard deviation is

$$
\sigma_X = \sqrt{1.648475} \approx 1.2839 .
$$

So the standard deviation of the annual profit is approximately $1.28$ million.
"""

# --------------------------------------------------------------------------
# Groups: surviving original -> solution
# --------------------------------------------------------------------------

GROUPS: dict[str, tuple[list[int], str]] = {
    "poisson_typos": ([1798, 1875, 1988, 2042, 2155, 2258], POISSON_TYPOS),
    "binomial_uniform": ([1806, 2050], BINOMIAL_UNIFORM),
    "sticks_uniform": ([1997, 2164, 2267], STICKS_UNIFORM),
    "telephone": ([1825], TELEPHONE),
    "iq_normal": ([1945, 2087, 2112, 2190, 2295], IQ_NORMAL),
    "coin_dice": ([2005, 2275], COIN_AND_DICE),
    "radish": ([2040], RADISH),
    "density_transform": ([2067], DENSITY_TRANSFORM),
    "company_profit": ([2079, 2183], COMPANY_PROFIT),
}

# Trailing / leading extraction artefacts to remove from survivors.
ARTEFACT_TRIMS: dict[int, list[str]] = {
    1825: ["**INVOLVEMENT IN EXAMINATION IRREGULARITY SHALL LEAD TO DISCONTINUATION**"],
    1988: ["- ****\n\n"],
    2155: ["- ****\n\n"],
    2258: ["- ****\n\n"],
    1997: ["\n\n---"],
    2164: ["\n\n---"],
    2267: ["\n\n---"],
    2005: ["***INVOLVEMENT IN EXAMINATION IRREGULARITY SHALL LEAD TO DISCONTINUATION***"],
    2275: ["***INVOLVEMENT IN EXAMINATION IRREGULARITY SHALL LEAD TO DISCONTINUATION***"],
}


def clean(text: str, pk: int) -> str:
    for marker in ARTEFACT_TRIMS.get(pk, []):
        text = text.replace(marker, "")
    if pk in (2005, 2275):
        text = text.replace("CamScanner", "")
    text = text.replace("possible values of \\(P\\)", "possible values of \\(p\\)")
    lines = [ln.rstrip() for ln in text.split("\n")]
    return "\n".join(lines).strip()


def main() -> None:
    apply = "--apply" in sys.argv

    pending = list(
        PrepQuestion.objects.filter(
            topic__course_id=COURSE_ID, verification_status="pending"
        ).order_by("id")
    )
    print(f"pending rows: {len(pending)}")

    survivors: list[int] = [pk for ids, _ in GROUPS.values() for pk in ids]
    survivor_set = set(survivors)
    orphan_children = [
        q.id for q in pending if q.reconstructed_from_id not in survivor_set
    ]
    if orphan_children:
        raise SystemExit(
            f"pending rows whose original is not a survivor: {orphan_children}"
        )
    unused = survivor_set - {q.reconstructed_from_id for q in pending}
    if unused:
        raise SystemExit(f"survivors that no pending row points to: {sorted(unused)}")

    rows = {q.id: q for q in PrepQuestion.objects.filter(pk__in=survivors)}
    missing = [pk for pk in survivors if pk not in rows]
    if missing:
        raise SystemExit(f"missing survivor rows: {missing}")

    # 1. back up everything we are about to touch
    backup = {
        "deleted": [
            {
                "id": q.id,
                "paper_id": q.paper_id,
                "topic_id": q.topic_id,
                "number": q.number,
                "reconstructed_from": q.reconstructed_from_id,
                "question_latex": q.question_latex,
                "solution_latex": q.solution_latex,
                "marks": str(q.marks),
            }
            for q in pending
        ],
        "survivors": {
            str(pk): {
                "question_latex": rows[pk].question_latex,
                "solution_latex": rows[pk].solution_latex,
            }
            for pk in survivors
        },
    }
    if apply:
        out = Path(__file__).resolve().parent / "pending_resolution_backup.json"
        out.write_text(json.dumps(backup, indent=1, ensure_ascii=False), encoding="utf-8")
        print("backup written:", out)

    # 2. clean + solve survivors
    changed_q = changed_s = 0
    for _key, (ids, solution) in GROUPS.items():
        for pk in ids:
            q = rows[pk]
            new_q = clean(q.question_latex or "", pk)
            if new_q != q.question_latex:
                changed_q += 1
            if (q.solution_latex or "").strip() != solution.strip():
                changed_s += 1
            if apply:
                q.question_latex = new_q
                q.solution_latex = solution
                q.save(update_fields=["question_latex", "solution_latex"])

    print(f"survivors: {len(survivors)} | question text cleaned: {changed_q} | solutions set: {changed_s}")

    # 3. retire the duplicate pending reconstructions
    if apply:
        deleted = PrepQuestion.objects.filter(pk__in=[q.id for q in pending]).delete()
        print("deleted:", deleted)

    if not apply:
        print("\nDRY RUN - nothing written. Re-run with --apply.")


if __name__ == "__main__":
    main()
