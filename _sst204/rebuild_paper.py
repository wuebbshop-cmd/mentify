"""Rebuild the 12 SST 204 questions of the 'Final Examination Paper (2025/2026)'.

The source PDF was scanned in two columns and the stored text is column-
interleaved nonsense ("There are 15 applicantsfor a job ... 9 of / in Financial
Engineering. If5 of these these applicants have a degree"), so the questions were
reconstructed from the legible fragments plus the worked solutions already held
for the same sub-questions. Every numeric answer below was re-derived with
sympy/Python before being written.

The same document was also ingested a second time as paper
``sst204-doc-9632df35`` with one row per page (5 rows, even worse text). That
duplicate is unpublished so learners see the paper once.

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

from prep.models import PrepPaper, PrepQuestion  # noqa: E402

DUPLICATE_PAPER = "sst204-doc-9632df35"

QUESTIONS: dict[int, str] = {
    1101: r"""(a) State two conditions for a real valued function \(f(x)\) to be a probability distribution function of a continuous random variable \(X\). **(2 Marks)**""",
    1102: r"""(b) Let \(Y\) be a continuous random variable with a probability density function given by

$$
f(y) = \begin{cases} k(y+2), & 0 \le y \le 3 \\ 0, & \text{otherwise} \end{cases}
$$

(i) Determine the value of the constant \(k\). **(2 Marks)**

(ii) Determine the distribution function (cumulative distribution function) of \(Y\). **(2 Marks)**

(iii) Find \(E[4Y-1]\) and \(\operatorname{Var}[4Y-1]\). **(4 Marks)**

(c) Let \(h(t)=\ln(M(t))\), where \(M(t)\) is the moment generating function of a distribution. Show that \(h'(0)=\mu\) and \(h''(0)=\sigma^2\), where \(\mu\) and \(\sigma^2\) are the mean and variance of the distribution. **(6 Marks)**""",
    1103: r"""(d) There are 15 applicants for a job at the Central Bank of Kenya, and 9 of these applicants have a degree in Financial Engineering. If 5 of these applicants are randomly selected for an interview, find the probability that:

(i) three applicants have a degree in Financial Engineering; **(2 Marks)**

(ii) at most three have a degree in Financial Engineering. **(2 Marks)**

(e) If \(X\) is a random variable which is normally distributed with mean \(10\) and variance \(16\), find \(P(|X-10|<3)\). **(4 Marks)**""",
    1104: r"""(f) The number of male mates of a queen bee was found to have a Poisson distribution with parameter \(\lambda = 4.7\). Find the probability that the number, \(X\), of male mates of a queen bee is

(i) exactly 3; **(2 Marks)**

(ii) at most 2; **(1 Mark)**

(iii) between 1 and 3 inclusive. **(2 Marks)**""",
    1105: r"""(g) Let \(X\) have the probability distribution function

$$
f(x) = \begin{cases} \dfrac{2x}{9}, & 0 < x < 3 \\ 0, & \text{otherwise} \end{cases}
$$

Find the probability distribution function of the new random variable \(U = X^2\). **(3 Marks)**""",
    1106: r"""(a) Let \(X\) be a discrete random variable with probability distribution given by

$$
f(x) = \begin{cases} k(x+2), & x = 1, 2, 3, 4, 5 \\ 0, & \text{otherwise} \end{cases}
$$

(i) Sketch the graph of \(f(x)\). **(1 Mark)**

(ii) Determine the distribution function of \(X\) and sketch its graph. **(5 Marks)**

(b) The distribution function of a continuous random variable \(Y\) is given by

$$
G(y) = \begin{cases} 0, & y < 0 \\ 1 - \cos y, & 0 \le y \le \dfrac{\pi}{2} \\ 1, & y > \dfrac{\pi}{2} \end{cases}
$$

(i) Determine the probability distribution function of \(Y\). **(2 Marks)**

(ii) Obtain the mode and median of \(Y\). **(6 Marks)**

(iii) Compute \(P\left(\dfrac{\pi}{6} < Y < \dfrac{\pi}{3}\right)\). **(2 Marks)**""",
    1107: r"""(c) Let \(X\) be a continuous random variable with probability density function

$$
f(x) = \begin{cases} \tfrac{1}{2}(x+1), & -1 < x < 1 \\ 0, & \text{otherwise} \end{cases}
$$

Compute the variance of \(4X + 10\). **(4 Marks)**""",
    1108: r"""(a) Let \(X\) be a discrete random variable with probability distribution given by

$$
f(x) = \begin{cases} \tfrac{1}{6}, & x = 1, 2, 3, 4, 5, 6 \\ 0, & \text{otherwise} \end{cases}
$$

(i) Obtain the moment generating function of \(X\). **(3 Marks)**

(ii) Hence determine the mean and variance of \(X\). **(7 Marks)**

(b) In a statistics course final examination, \(15\%\) of the students fail. Using the Poisson approximation, find the probability that in a random sample of 100 students who took the final examination exactly 20 will fail. **(4 Marks)**""",
    1109: r"""(c) Suppose a discrete random variable \(X\) has a Poisson distribution with parameter \(\lambda\); further suppose that \(P(X=2)=P(X=1)\). Find \(E(X)\). **(6 Marks)**""",
    1110: r"""(b) Let \(X\) be normally distributed with mean \(\mu\) and variance \(\sigma^2\), and suppose that \(P(X<60)=0.90\) and \(P(X<70)=0.95\). Find \(\mu\) and \(\sigma\). **(4 Marks)**""",
    1111: r"""(c) A continuous random variable \(X\) has probability density function

$$
f(x) = \begin{cases} a + bx + cx^2, & 0 < x < 1 \\ 0, & \text{otherwise} \end{cases}
$$

Given that \(E(X)=\dfrac{1}{4}\) and \(\operatorname{Var}(X)=\dfrac{3}{80}\), determine the values of the constants \(a\), \(b\) and \(c\). **(7 Marks)**""",
    1112: r"""(a) Suppose a continuous random variable \(X\) has a beta distribution with parameters \(\alpha\) and \(\beta\) (\(\alpha>0\), \(\beta>0\)), that is

$$
f(x) = \begin{cases} \dfrac{1}{B(\alpha,\beta)}\,x^{\alpha-1}(1-x)^{\beta-1}, & 0 < x < 1 \\ 0, & \text{otherwise} \end{cases} \qquad \text{where } B(\alpha,\beta)=\frac{\Gamma(\alpha)\Gamma(\beta)}{\Gamma(\alpha+\beta)}
$$

Find \(E(X^k)\), where \(k\) is a positive integer. **(8 Marks)** Hence obtain the mean and variance of \(X\).

(b) A continuous random variable \(X\) has a probability density function given by

$$
f(x) = \begin{cases} \lambda e^{-\lambda x}, & x > 0,\ \lambda > 0 \\ 0, & \text{otherwise} \end{cases}
$$

Determine the moment generating function of \(X\) and hence find the mean and variance. **(7 Marks)**

(c) Suppose that \(X\) has the discrete probability distribution

$$
\begin{array}{c|ccc}
x & -2 & 1 & 2 \\ \hline
f(x) & \tfrac{1}{4} & \tfrac{1}{4} & \tfrac{1}{2}
\end{array}
$$

Find the distribution of the random variable \(Y = 4X + 1\). **(5 Marks)**""",
}

SOLUTIONS: dict[int, str] = {
    1101: r"""A real valued function \(f(x)\) is a probability density function of a continuous random variable \(X\) when

$$
f(x) \ge 0 \quad \text{for every real } x,
$$

and

$$
\int_{-\infty}^{\infty} f(x)\,dx = 1 .
$$

The first condition makes every probability non-negative; the second makes the total probability one. Any function satisfying both is a legitimate density, and the distribution function is then \(F(x)=\int_{-\infty}^{x} f(t)\,dt\).""",
    1102: r"""**(i)** A density must integrate to one, so

$$
\int_{0}^{3} k(y+2)\,dy = k\left[\frac{y^2}{2}+2y\right]_{0}^{3} = k\left(\frac{9}{2}+6\right) = \frac{21k}{2} = 1,
$$

hence \(k = \dfrac{2}{21}\).

**(ii)** For \(0 \le y \le 3\),

$$
F(y) = \int_{0}^{y} \frac{2}{21}(t+2)\,dt = \frac{2}{21}\left(\frac{y^2}{2}+2y\right) = \frac{y^2+4y}{21},
$$

with \(F(y)=0\) for \(y<0\) and \(F(y)=1\) for \(y>3\). As a check, \(F(3)=\frac{9+12}{21}=1\).

**(iii)** Using the density,

$$
E(Y) = \int_{0}^{3} y\cdot\frac{2}{21}(y+2)\,dy = \frac{2}{21}\left[\frac{y^3}{3}+y^2\right]_{0}^{3} = \frac{2}{21}(9+9) = \frac{12}{7},
$$

and

$$
E\left(Y^2\right) = \int_{0}^{3} y^2\cdot\frac{2}{21}(y+2)\,dy = \frac{2}{21}\left[\frac{y^4}{4}+\frac{2y^3}{3}\right]_{0}^{3} = \frac{2}{21}\left(\frac{81}{4}+18\right) = \frac{51}{14}.
$$

Therefore

$$
\operatorname{Var}(Y) = \frac{51}{14}-\left(\frac{12}{7}\right)^2 = \frac{51}{14}-\frac{144}{49} = \frac{357-288}{98} = \frac{69}{98}.
$$

For the linear transformation,

$$
E[4Y-1] = 4E(Y)-1 = 4\left(\frac{12}{7}\right)-1 = \frac{41}{7},
$$

and

$$
\operatorname{Var}[4Y-1] = 16\,\operatorname{Var}(Y) = 16\left(\frac{69}{98}\right) = \frac{552}{49}.
$$

**(c)** Differentiating \(h(t)=\ln M(t)\),

$$
h'(t)=\frac{M'(t)}{M(t)}, \qquad h''(t)=\frac{M''(t)M(t)-\left[M'(t)\right]^2}{\left[M(t)\right]^2}.
$$

Since \(M(0)=1\), \(M'(0)=E(X)=\mu\) and \(M''(0)=E\left(X^2\right)\), we get

$$
h'(0) = \frac{M'(0)}{M(0)} = \mu,
$$

and

$$
h''(0) = \frac{M''(0)M(0)-\left[M'(0)\right]^2}{\left[M(0)\right]^2} = E\left(X^2\right)-\mu^2 = \sigma^2 .
$$

So the first two derivatives of the cumulant generating function \(h\) give the mean and the variance, as required.""",
    1103: r"""Let \(X\) be the number of selected applicants who hold a degree in Financial Engineering. Selecting 5 applicants from 15 without replacement, of whom 9 have the degree, gives a hypergeometric distribution:

$$
P(X=x) = \frac{\binom{9}{x}\binom{6}{5-x}}{\binom{15}{5}}, \qquad x = 0,1,2,3,4,5,
$$

with \(\binom{15}{5} = 3003\).

**(i)** For exactly three,

$$
P(X=3) = \frac{\binom{9}{3}\binom{6}{2}}{3003} = \frac{84 \times 15}{3003} = \frac{1260}{3003} \approx 0.4196 .
$$

**(ii)** For at most three we add the four admissible counts:

$$
P(X \le 3) = \frac{\binom{9}{0}\binom{6}{5}+\binom{9}{1}\binom{6}{4}+\binom{9}{2}\binom{6}{3}+\binom{9}{3}\binom{6}{2}}{3003}.
$$

The numerators are \(1\times 6 = 6\), \(9\times 15 = 135\), \(36\times 20 = 720\) and \(84\times 15 = 1260\), giving

$$
P(X \le 3) = \frac{6+135+720+1260}{3003} = \frac{2121}{3003} \approx 0.7063 .
$$

**(e)** Here \(X \sim N(10, 16)\), so \(\sigma = 4\). Standardising with \(Z=\dfrac{X-10}{4}\),

$$
P(|X-10|<3) = P\left(|Z| < \frac{3}{4}\right) = P(-0.75 < Z < 0.75) = 2\Phi(0.75)-1 .
$$

Since \(\Phi(0.75) \approx 0.7734\),

$$
P(|X-10|<3) \approx 2(0.7734)-1 = 0.5468 .
$$""",
    1104: r"""With \(X \sim \mathrm{Poisson}(4.7)\),

$$
P(X=x) = \frac{e^{-4.7}\,4.7^{x}}{x!}, \qquad x = 0,1,2,\dots
$$

**(i)** For exactly three,

$$
P(X=3) = \frac{e^{-4.7}\,4.7^{3}}{3!} = \frac{e^{-4.7}(103.823)}{6} \approx 0.1574 .
$$

**(ii)** For at most two,

$$
P(X \le 2) = e^{-4.7}\left(1 + 4.7 + \frac{4.7^2}{2}\right) = e^{-4.7}(1+4.7+11.045) \approx 0.1523 .
$$

**(iii)** For between one and three inclusive,

$$
P(1 \le X \le 3) = e^{-4.7}\left(4.7 + \frac{4.7^2}{2} + \frac{4.7^3}{6}\right) = e^{-4.7}(4.7+11.045+17.3038) \approx 0.3006 .
$$""",
    1105: r"""First confirm that \(f\) is a density:

$$
\int_{0}^{3}\frac{2x}{9}\,dx = \left[\frac{x^2}{9}\right]_{0}^{3} = 1 .
$$

The transformation \(u=x^2\) is increasing on \(0<x<3\), with inverse \(x=\sqrt{u}\) and \(\dfrac{dx}{du}=\dfrac{1}{2\sqrt{u}}\). Since \(0<x<3\) gives \(0<u<9\),

$$
f_U(u) = f_X\left(\sqrt{u}\right)\left|\frac{dx}{du}\right| = \frac{2\sqrt{u}}{9}\cdot\frac{1}{2\sqrt{u}} = \frac{1}{9}, \qquad 0 < u < 9,
$$

and \(f_U(u)=0\) otherwise.

Equivalently, from the distribution function, for \(0<u<9\)

$$
F_U(u) = P\left(X^2 \le u\right) = P\left(X \le \sqrt{u}\right) = \int_{0}^{\sqrt{u}}\frac{2x}{9}\,dx = \frac{u}{9},
$$

and differentiating gives \(f_U(u)=\dfrac{1}{9}\). So \(U\) is uniform on \((0,9)\).""",
    1106: r"""**(a)** A probability mass function must sum to one:

$$
\sum_{x=1}^{5} k(x+2) = k(3+4+5+6+7) = 25k = 1,
$$

so \(k = \dfrac{1}{25}\).

(i) On the five points \(x=1,\dots,5\) the probabilities are \(\dfrac{3}{25}, \dfrac{4}{25}, \dfrac{5}{25}, \dfrac{6}{25}, \dfrac{7}{25}\). The graph is five vertical spikes of those heights at \(x=1,2,3,4,5\), rising steadily, and it is zero everywhere else.

(ii) The distribution function is the running total:

$$
F(1)=\frac{3}{25}, \quad F(2)=\frac{7}{25}, \quad F(3)=\frac{12}{25}, \quad F(4)=\frac{18}{25}, \quad F(5)=\frac{25}{25}=1,
$$

with \(F(x)=0\) for \(x<1\) and \(F(x)=1\) for \(x \ge 5\). In closed form, for \(x \in \{1,2,3,4,5\}\),

$$
F(x) = \frac{1}{25}\left(\frac{x(x+1)}{2}+2x\right) = \frac{x^2+5x}{50},
$$

and the graph is a step function that jumps by \(\dfrac{x+2}{25}\) at each integer \(x=1,\dots,5\).

**(b)** (i) Differentiating \(G\) where it is differentiable,

$$
g(y) = G'(y) = \sin y, \qquad 0 < y < \frac{\pi}{2},
$$

and \(g(y)=0\) otherwise. As a check, \(\int_{0}^{\pi/2}\sin y\,dy = 1\).

(ii) The density \(\sin y\) increases on \(\left(0,\frac{\pi}{2}\right)\), so its maximum is at the right endpoint and the mode is

$$
\frac{\pi}{2}.
$$

The median \(m\) solves \(G(m)=\frac{1}{2}\):

$$
1-\cos m = \frac{1}{2} \quad\Longrightarrow\quad \cos m = \frac{1}{2} \quad\Longrightarrow\quad m = \frac{\pi}{3}.
$$

(iii) Using \(P(a<Y<b)=G(b)-G(a)=\cos a-\cos b\),

$$
P\left(\frac{\pi}{6}<Y<\frac{\pi}{3}\right) = \cos\frac{\pi}{6}-\cos\frac{\pi}{3} = \frac{\sqrt{3}}{2}-\frac{1}{2} = \frac{\sqrt{3}-1}{2} \approx 0.3660 .
$$""",
    1107: r"""First note that \(f\) is a density:

$$
\int_{-1}^{1}\frac{1}{2}(x+1)\,dx = \frac{1}{2}\left[\frac{x^2}{2}+x\right]_{-1}^{1} = \frac{1}{2}(2) = 1 .
$$

Now

$$
E(X) = \int_{-1}^{1} x\cdot\frac{1}{2}(x+1)\,dx = \frac{1}{2}\left[\frac{x^3}{3}+\frac{x^2}{2}\right]_{-1}^{1} = \frac{1}{2}\left(\frac{2}{3}\right) = \frac{1}{3},
$$

and

$$
E\left(X^2\right) = \int_{-1}^{1} x^2\cdot\frac{1}{2}(x+1)\,dx = \frac{1}{2}\left[\frac{x^4}{4}+\frac{x^3}{3}\right]_{-1}^{1} = \frac{1}{2}\left(\frac{2}{3}\right) = \frac{1}{3}.
$$

Hence

$$
\operatorname{Var}(X) = \frac{1}{3}-\left(\frac{1}{3}\right)^2 = \frac{1}{3}-\frac{1}{9} = \frac{2}{9}.
$$

For a linear transformation \(\operatorname{Var}(aX+b)=a^2\operatorname{Var}(X)\), so

$$
\operatorname{Var}(4X+10) = 16\cdot\frac{2}{9} = \frac{32}{9} \approx 3.556 .
$$

The additive constant \(10\) does not affect the variance.""",
    1108: r"""**(a)** Here \(P(X=x)=\dfrac{1}{6}\) for \(x=1,2,3,4,5,6\).

(i) By definition \(M_X(t)=E\left(e^{tX}\right)\), so

$$
M_X(t) = \frac{1}{6}\sum_{x=1}^{6} e^{tx} = \frac{1}{6}\left(e^{t}+e^{2t}+e^{3t}+e^{4t}+e^{5t}+e^{6t}\right),
$$

with \(M_X(0)=1\). For \(t\neq 0\) this may also be written as the finite geometric sum

$$
M_X(t) = \frac{e^{t}\left(e^{6t}-1\right)}{6\left(e^{t}-1\right)} .
$$

(ii) Differentiating term by term,

$$
M_X'(t) = \frac{1}{6}\sum_{x=1}^{6} x\,e^{tx}, \qquad M_X''(t) = \frac{1}{6}\sum_{x=1}^{6} x^2 e^{tx}.
$$

At \(t=0\), using \(1+2+3+4+5+6=21\),

$$
E(X) = M_X'(0) = \frac{21}{6} = \frac{7}{2},
$$

and using \(1^2+2^2+3^2+4^2+5^2+6^2 = 91\),

$$
E\left(X^2\right) = M_X''(0) = \frac{91}{6}.
$$

Therefore

$$
\operatorname{Var}(X) = \frac{91}{6}-\left(\frac{7}{2}\right)^2 = \frac{91}{6}-\frac{49}{4} = \frac{182-147}{12} = \frac{35}{12}.
$$

**(b)** Let \(Y\) be the number of the 100 students who fail. Then \(Y \sim \mathrm{Bin}(100, 0.15)\), and the Poisson approximation uses

$$
\lambda = np = 100(0.15) = 15 .
$$

Hence

$$
P(Y = 20) \approx \frac{e^{-15}\,15^{20}}{20!} \approx 0.0418 .
$$

So the probability that exactly 20 of the 100 students fail is approximately \(0.0418\).""",
    1109: r"""For \(X \sim \mathrm{Poisson}(\lambda)\),

$$
P(X=k) = \frac{e^{-\lambda}\lambda^{k}}{k!}, \qquad k = 0,1,2,\dots
$$

The condition \(P(X=2)=P(X=1)\) reads

$$
\frac{e^{-\lambda}\lambda^{2}}{2!} = \frac{e^{-\lambda}\lambda^{1}}{1!},
$$

so, cancelling the positive factor \(e^{-\lambda}\lambda\) (valid because \(\lambda>0\)),

$$
\frac{\lambda}{2} = 1 \quad\Longrightarrow\quad \lambda = 2 .
$$

For a Poisson random variable the mean equals the parameter, so

$$
E(X) = \lambda = 2 .
$$

As a check, \(P(X=1)=\dfrac{e^{-2}2}{1}=2e^{-2}\) and \(P(X=2)=\dfrac{e^{-2}4}{2}=2e^{-2}\), which agree.""",
    1110: r"""Standardising with \(Z=\dfrac{X-\mu}{\sigma}\sim N(0,1)\),

$$
P(X<60) = P\left(Z<\frac{60-\mu}{\sigma}\right) = 0.90, \qquad P(X<70) = P\left(Z<\frac{70-\mu}{\sigma}\right) = 0.95 .
$$

From the standard normal table, \(z_{0.90}\approx 1.2816\) and \(z_{0.95}\approx 1.6449\). Therefore

$$
\frac{60-\mu}{\sigma} = 1.2816, \qquad \frac{70-\mu}{\sigma} = 1.6449 .
$$

Subtracting the first equation from the second eliminates \(\mu\):

$$
\frac{10}{\sigma} = 1.6449-1.2816 = 0.3633 \quad\Longrightarrow\quad \sigma = \frac{10}{0.3633} \approx 27.53 .
$$

Substituting back,

$$
\mu = 60 - 1.2816(27.53) \approx 60 - 35.28 = 24.72 .
$$

As a check, \(\mu + 1.6449(27.53) \approx 70\), as required. So \(\mu \approx 24.72\) and \(\sigma \approx 27.53\).""",
    1111: r"""The three conditions on a density and its first two moments are

$$
\int_{0}^{1}\left(a+bx+cx^2\right)dx = 1, \qquad \int_{0}^{1} x\left(a+bx+cx^2\right)dx = E(X), \qquad \int_{0}^{1} x^2\left(a+bx+cx^2\right)dx = E\left(X^2\right).
$$

Integrating term by term gives

$$
\frac{a}{3}+\frac{b}{2}+c = 1, \qquad \frac{a}{4}+\frac{b}{3}+\frac{c}{2} = \frac{1}{4}, \qquad \frac{a}{5}+\frac{b}{4}+\frac{c}{3} = E\left(X^2\right).
$$

For the right-hand side of the third equation, use \(\operatorname{Var}(X)=E\left(X^2\right)-\left[E(X)\right]^2\):

$$
E\left(X^2\right) = \frac{3}{80}+\left(\frac{1}{4}\right)^2 = \frac{3}{80}+\frac{1}{16} = \frac{3+5}{80} = \frac{1}{10}.
$$

So the system is

$$
\frac{a}{3}+\frac{b}{2}+c = 1, \qquad \frac{a}{4}+\frac{b}{3}+\frac{c}{2} = \frac{1}{4}, \qquad \frac{a}{5}+\frac{b}{4}+\frac{c}{3} = \frac{1}{10}.
$$

Subtracting the second equation from the first eliminates \(c\) in the form \(\frac{a}{3}-\frac{a}{4}+\frac{b}{2}-\frac{b}{3}+\frac{c}{2}=\frac{3}{4}\), that is

$$
\frac{a}{12}+\frac{b}{6}+\frac{c}{2} = \frac{3}{4}. \tag{1}
$$

Multiplying the first equation by \(\frac{1}{2}\) gives \(\frac{a}{6}+\frac{b}{4}+\frac{c}{2}=\frac{1}{2}\), and subtracting this from (1),

$$
a\left(\frac{1}{12}-\frac{1}{6}\right)+b\left(\frac{1}{6}-\frac{1}{4}\right) = \frac{1}{4} \quad\Longrightarrow\quad -\frac{a}{12}-\frac{b}{12} = \frac{1}{4} \quad\Longrightarrow\quad a+b = -3. \tag{2}
$$

Similarly, subtracting the third equation from the second gives

$$
a\left(\frac{1}{4}-\frac{1}{5}\right)+b\left(\frac{1}{3}-\frac{1}{4}\right)+c\left(\frac{1}{2}-\frac{1}{3}\right) = \frac{1}{4}-\frac{1}{10},
$$

that is \(\frac{a}{20}+\frac{b}{12}+\frac{c}{6}=\frac{3}{20}\), and multiplying the first equation by \(\frac{1}{6}\) gives \(\frac{a}{18}+\frac{b}{12}+\frac{c}{6}=\frac{1}{6}\). Subtracting,

$$
a\left(\frac{1}{20}-\frac{1}{18}\right) = \frac{3}{20}-\frac{1}{6} = \frac{9-10}{60} = -\frac{1}{60},
$$

so \(a\left(-\frac{1}{180}\right)=-\frac{1}{60}\), giving \(a = 3\). From (2), \(b=-3-3=-6\), and from the first equation

$$
c = 1-\frac{a}{3}-\frac{b}{2} = 1-1+3 = 3 .
$$

Therefore \(a=3\), \(b=-6\), \(c=3\), that is

$$
f(x) = 3-6x+3x^2 = 3(1-x)^2, \qquad 0<x<1 .
$$

As checks: \(f(x)=3(1-x)^2 \ge 0\) on \((0,1)\), \(\int_{0}^{1}3(1-x)^2 dx = 1\),

$$
E(X) = \int_{0}^{1} 3x(1-x)^2 dx = 3\left(\frac{1}{2}-\frac{2}{3}+\frac{1}{4}\right) = \frac{1}{4},
$$

and

$$
E\left(X^2\right) = \int_{0}^{1} 3x^2(1-x)^2 dx = 3\left(\frac{1}{3}-\frac{1}{2}+\frac{1}{5}\right) = \frac{1}{10},
$$

so \(\operatorname{Var}(X)=\frac{1}{10}-\frac{1}{16}=\frac{3}{80}\), as given.""",
    1112: r"""**(a)** By definition

$$
E\left(X^k\right) = \frac{1}{B(\alpha,\beta)}\int_{0}^{1} x^{k}\,x^{\alpha-1}(1-x)^{\beta-1}\,dx = \frac{1}{B(\alpha,\beta)}\int_{0}^{1} x^{(\alpha+k)-1}(1-x)^{\beta-1}\,dx .
$$

The remaining integral is the beta function \(B(\alpha+k,\beta)\), so

$$
E\left(X^k\right) = \frac{B(\alpha+k,\beta)}{B(\alpha,\beta)} = \frac{\Gamma(\alpha+k)\Gamma(\alpha+\beta)}{\Gamma(\alpha)\Gamma(\alpha+\beta+k)},
$$

since the \(\Gamma(\beta)\) factors cancel.

Taking \(k=1\),

$$
E(X) = \frac{\Gamma(\alpha+1)\Gamma(\alpha+\beta)}{\Gamma(\alpha)\Gamma(\alpha+\beta+1)} = \frac{\alpha}{\alpha+\beta},
$$

using \(\Gamma(\alpha+1)=\alpha\Gamma(\alpha)\). Taking \(k=2\),

$$
E\left(X^2\right) = \frac{\alpha(\alpha+1)}{(\alpha+\beta)(\alpha+\beta+1)},
$$

so

$$
\operatorname{Var}(X) = \frac{\alpha(\alpha+1)}{(\alpha+\beta)(\alpha+\beta+1)}-\frac{\alpha^2}{(\alpha+\beta)^2} = \frac{\alpha\beta}{(\alpha+\beta)^2(\alpha+\beta+1)} .
$$

**(b)** For \(f(x)=\lambda e^{-\lambda x}\) on \(x>0\),

$$
M_X(t) = E\left(e^{tX}\right) = \int_{0}^{\infty} \lambda e^{-(\lambda-t)x}\,dx = \frac{\lambda}{\lambda-t}, \qquad t < \lambda .
$$

Differentiating,

$$
M_X'(t) = \frac{\lambda}{(\lambda-t)^2}, \qquad M_X''(t) = \frac{2\lambda}{(\lambda-t)^3}.
$$

At \(t=0\),

$$
E(X) = M_X'(0) = \frac{1}{\lambda}, \qquad E\left(X^2\right) = M_X''(0) = \frac{2}{\lambda^2},
$$

hence

$$
\operatorname{Var}(X) = \frac{2}{\lambda^2}-\frac{1}{\lambda^2} = \frac{1}{\lambda^2} .
$$

**(c)** The transformation \(Y=4X+1\) is increasing, so each value of \(X\) maps to one value of \(Y\) with the same probability: \(X=-2 \mapsto Y=-7\), \(X=1 \mapsto Y=5\) and \(X=2 \mapsto Y=9\). Hence

$$
\begin{array}{c|ccc}
y & -7 & 5 & 9 \\ \hline
P(Y=y) & \tfrac{1}{4} & \tfrac{1}{4} & \tfrac{1}{2}
\end{array}
$$

and the probabilities still sum to one. As a check, \(E(Y)=4E(X)+1\), and \(E(X)=(-2)\left(\frac14\right)+1\left(\frac14\right)+2\left(\frac12\right)=\frac34\), giving \(E(Y)=4\).""",
}


def main() -> None:
    apply = "--apply" in sys.argv

    rows = {q.id: q for q in PrepQuestion.objects.filter(pk__in=QUESTIONS)}
    missing = [pk for pk in QUESTIONS if pk not in rows]
    if missing:
        raise SystemExit(f"missing rows: {missing}")

    backup = {
        str(pk): {
            "question_latex": rows[pk].question_latex,
            "solution_latex": rows[pk].solution_latex,
            "verification_status": rows[pk].verification_status,
            "reconstruction_metadata": rows[pk].reconstruction_metadata,
        }
        for pk in QUESTIONS
    }

    if apply:
        backup_path = Path(__file__).resolve().parent / "rebuild_paper_backup.json"
        backup_path.write_text(json.dumps(backup, indent=1, ensure_ascii=False, default=str), encoding="utf-8")
        print("backup written:", backup_path)

        for pk, question in QUESTIONS.items():
            q = rows[pk]
            metadata = dict(q.reconstruction_metadata or {})
            metadata["reason"] = (
                "Source PDF scanned in two columns; stored extraction text was "
                "column-interleaved and unreadable. Question rebuilt from the legible "
                "fragments and re-solved."
            )
            q.question_latex = question
            q.solution_latex = SOLUTIONS[pk]
            q.verification_status = "reconstructed"
            q.reconstruction_metadata = metadata
            q.save(
                update_fields=[
                    "question_latex",
                    "solution_latex",
                    "verification_status",
                    "reconstruction_metadata",
                ]
            )
        print(f"rebuilt {len(QUESTIONS)} questions")

        dup = PrepPaper.objects.filter(pk=DUPLICATE_PAPER).first()
        if dup is None:
            print("duplicate paper already gone")
        else:
            dup.is_published = False
            dup.save(update_fields=["is_published"])
            print(f"unpublished duplicate paper {DUPLICATE_PAPER} "
                  f"({PrepQuestion.objects.filter(paper_id=DUPLICATE_PAPER).count()} rows hidden)")
    else:
        print(f"would rebuild {len(QUESTIONS)} questions: {sorted(QUESTIONS)}")
        print(f"would unpublish duplicate paper {DUPLICATE_PAPER}")
        print("DRY RUN - nothing written.")


if __name__ == "__main__":
    main()
