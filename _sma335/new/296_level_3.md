## 1. Foundational Concepts, Definitions, and Axioms

### 1.1 What the examiner is testing

Every question on this topic is assembled from four separable skills, and the mark scheme pays for them in a predictable order. The first skill is classification: deciding, from the normalised equation, whether the expansion point is ordinary, regular singular or irregular. The second is template selection: writing the correct one of the two shapes of answer, with the correct statement about which coefficients are free. The third is bookkeeping: differentiating, substituting, aligning indices and reading off the recurrence without losing a term. The fourth is case analysis at a singular point: deciding whether the second solution is a plain Frobenius series, a series with a logarithm, or a series that may or may not carry a logarithm.

Those four skills are worth roughly two marks, one mark, five to seven marks and three to four marks respectively in a typical fifteen-mark question. The arithmetic of the coefficients is worth two to four marks, and it is the part that most often collapses when the recurrence is wrong. The strategic conclusion is immediate: secure the first two skills in the first minute, because they are cheap, and spend the saved time on the alignment, which is where the heavy marks sit.

The governing formulae are short enough to write at the top of the answer booklet before starting.

$$
\frac{d^{2}y}{dx^{2}}+p(x)\frac{dy}{dx}+q(x)y=0,\qquad p_{0}=\lim_{x\to 0}xp(x),\qquad q_{0}=\lim_{x\to 0}x^{2}q(x)
$$

$$
r(r-1)+p_{0}r+q_{0}=0
$$

$$
F(s)=s^{2}+\left(p_{0}-1\right)s+q_{0}=\left(s-r_{1}\right)\left(s-r_{2}\right)
$$

Everything else in the topic is a consequence of those three lines together with the index-shift rule. A candidate who writes them down, and who knows that the coefficient of $c_{n}$ in the general relation is $F(n+r)$, can reconstruct any recurrence under examination pressure.

### 1.2 High-yield results and their mark values

The table lists what is examined directly, with the marks usually attached in a first-year paper. The values are indicative rather than universal, but the relative weighting is stable across papers: derivations and complete solutions carry more than statements, and classification is always cheap.

| Result | Statement | Typical marks |
| --- | --- | --- |
| Classification | Compute $xp$ and $x^{2}q$; ordinary, regular or irregular | 1 to 2 |
| Template | $y=\sum c_{n}x^{n}$ at an ordinary point, $y=x^{r}\sum c_{n}x^{n}$ at a regular singular point | 1 |
| Indicial equation | $r(r-1)+p_{0}r+q_{0}=0$ | 1 to 2 |
| Recurrence | Align indices, equate coefficients of $x^{m}$ | 3 to 5 |
| Coefficients | Compute to the requested power | 2 to 4 |
| Second solution | Two series, logarithm forced, or logarithm possible | 2 to 4 |
| Radius | Distance to the nearest singular point | 1 to 2 |
| First-order recurrence | $(n+1)c_{n+1}+\sum_{k=0}^{n}p_{k}c_{n-k}=q_{n}$ | 2 to 3 |
| Non-homogeneous | Series forcing or variation of parameters | 3 to 5 |
| Verification | Substitute back and simplify | 1 to 3 |

Two conclusions follow. First, the indicial equation and the template together are worth only three marks, yet they determine everything afterwards, so they must never be postponed. Second, the recurrence and the coefficient arithmetic together carry roughly half the paper, which is why the alignment must be written out rather than performed mentally.

### 1.3 The shapes of question that are asked

The topic is examined through a small number of recurring patterns. Recognising the pattern in the first ten seconds tells you which template to write before you have done any algebra.

| Pattern | What is asked | Usual marks |
| --- | --- | --- |
| Ordinary point, full solution | Classify, then two independent series | 12 to 15 |
| Ordinary point, truncated | Series to a stated power, sometimes with initial conditions | 8 to 10 |
| Regular singular, classification only | Show regular, state the indicial equation | 4 to 6 |
| Regular singular, full solution | Both roots, both series, case stated | 12 to 15 |
| Second solution form only | State and justify the form, no coefficients | 3 to 4 |
| Non-homogeneous | Particular solution plus complementary function | 8 to 10 |
| Radius of convergence | Nearest singular point, real or complex | 2 to 3 |
| Verification | Show a given series satisfies the equation | 3 to 5 |

The pattern "second solution form only" is a gift, and it is frequently missed. It asks for the structure, not the coefficients, so the answer is a sentence plus a formula: if the roots are equal, $y_{2}=y_{1}\ln x+x^{r}\sum b_{n}x^{n}$; if they differ by a positive integer $N$, $y_{2}=C y_{1}\ln x+x^{r_{2}}\sum b_{n}x^{n}$ with $C$ possibly zero.

### 1.4 Recognition in ten seconds

The recognition sequence has four questions, and each answer is a single word.

- Is the coefficient of the second derivative free of zeros at the expansion point? If not, the point is singular and the Frobenius machinery is needed; divide by the coefficient first and classify on the normalised form.
- Is $xp(x)$ finite at the point? If not, the point is irregular and the method fails; say so and stop.
- Is $x^{2}q(x)$ finite at the point? If yes, the point is regular singular; if no, irregular.
- If the point is ordinary, is the nearest singular point at distance $R$? Quote $R$ as the radius.

Three examples show how fast the classification is. The equation $\left(x^{2}-1\right)y''+3xy'+xy=0$ normalises to coefficients with denominator $x^{2}-1$, so $0$ is ordinary with radius one. The equation $2x^{2}y''-xy'+\left(1-x^{2}\right)y=0$ normalises to $p$ equal to $-1$ over $2x$, so $0$ is singular, and $xp$ equal to $-\frac{1}{2}$ makes it regular. The equation $x^{3}y''+xy=0$ normalises to $q$ equal to $x^{-2}$, so $x^{2}q$ equal to $x^{-1}$ blows up and the point is irregular.

A fourth pattern deserves separate mention. An equation such as $x^{2}y''+3xy'+\left(1-x\right)y=0$ has $p_{0}=3$ and $q_{0}=1$, so the indicial polynomial is $s^{2}+2s+1$, a perfect square. The perfect square is the signal for a repeated root, and therefore for a logarithm, and it can be recognised before any substitution is attempted. Examiners like this because it separates candidates who understand the discriminant from those who merely follow steps.

### 1.5 Templates, free parameters, and the count of constants

At an ordinary point the template is

$$
y=\sum_{n=0}^{\infty}c_{n}x^{n},
$$

and the coefficient relations determine $c_{2},c_{3},c_{4},\dots$ from $c_{0}$ and $c_{1}$ without ever determining those two. The count is therefore two, and the general solution is $c_{0}y_{1}+c_{1}y_{2}$ with $y_{1}$ computed from $\left(c_{0},c_{1}\right)=\left(1,0\right)$ and $y_{2}$ from $\left(0,1\right)$.

At a regular singular point the template is

$$
y=x^{r}\sum_{n=0}^{\infty}c_{n}x^{n},\qquad c_{0}\neq 0 ,
$$

and the count is again two, but the parameters are not $c_{0}$ and $c_{1}$: they are $a_{0}$ together with the two admissible values of $r$. The condition $c_{0}\neq 0$ is essential to the derivation of the indicial equation, because the argument that the bracket vanishes divides by $c_{0}$. A candidate who allows $c_{0}=0$ loses the indicial equation and, with it, the marks for the case analysis.

For a non-homogeneous equation the count is still two, and the structure is $y_{p}$ plus the general homogeneous solution. The particular solution is fixed by the forcing and can be computed with either free coefficient set to any convenient value, because any change in those values is absorbed by the homogeneous part.

### 1.6 The derivations that are examinable as bookwork

Four derivations recur as bookwork, and each has a fixed shape that can be reproduced in about six lines.

The first is the shift of index

$$
\sum_{n=N}^{\infty}A_{n}x^{n+k}=\sum_{m=N+k}^{\infty}A_{m-k}x^{m},
$$

which is proved by the substitution $m=n+k$ and deserves one mark.

The second is the first-order recurrence, obtained by differentiating $\sum c_{n}x^{n}$ and multiplying the coefficient series by the unknown series.

The third is the indicial equation, obtained by multiplying the equation by $x^{2}$ so that the coefficients become analytic, substituting the Frobenius template, and reading the lowest power.

The fourth is the logarithmic case, obtained either from the derivative of the general solution with respect to $r$ or from reduction of order. The second route is shorter to write and shows the origin of the logarithm more clearly, and it is the one used in Section 3.5.

## 2. Theorems, Lemmas, and Analytical Properties

### 2.1 The index-shift lemma

> **Lemma.** For integers $N$ and $k$,
>
> $$
> \sum_{n=N}^{\infty}A_{n}x^{n+k}=\sum_{m=N+k}^{\infty}A_{m-k}x^{m},\qquad \sum_{n=N}^{\infty}A_{n}x^{n-k}=\sum_{m=N-k}^{\infty}A_{m+k}x^{m}.
> $$

> **Working form.** The coefficient of $x^{m}$ in $x^{k}y$ is $c_{m-k}$, and the coefficient of $x^{m}$ in $x^{k}y'$ is $\left(m-k+1\right)c_{m-k+1}$, with coefficients of negative index taken as zero.

The working form is what is actually used, and it should be applied mechanically. For $x^{2}y''$ the coefficient of $x^{m}$ is $(m+2)(m+1)c_{m+2}$, obtained by taking $k=2$ and remembering that differentiating twice multiplies by $(m+2)(m+1)$. For $xy$ the coefficient of $x^{m}$ is $c_{m-1}$, which vanishes at $m=0$.

### 2.2 The identity theorem

> **Lemma.** If $\sum a_{n}x^{n}=0$ on an interval around $0$, then every $a_{n}=0$. Consequently two series agreeing on an interval have equal coefficients.

Every coefficient comparison in the topic rests on this lemma. Its practical force is that a single differential equation becomes an infinite family of algebraic relations, one for each power.

### 2.3 The ordinary-point theorem and the radius bound

> **Theorem.** If $0$ is an ordinary point, the equation has two linearly independent solutions analytic at $0$, and every solution on the interval is a combination of them.

> **Corollary (radius).** If the singular points nearest to $0$ are at distance $R$, the two series converge at least for $\left|x\right|<R$.

The radius is a property of the coefficients, and the distance may be complex. For $\left(1+x^{2}\right)y''+y=0$ the singular points are at $\pm i$, so the radius about $0$ is one although no real singular point exists.

### 2.4 The Frobenius theorem

> **Theorem.** If $0$ is a regular singular point, there is at least one solution
>
> $$
> y=x^{r}\sum_{n=0}^{\infty}c_{n}x^{n},\qquad c_{0}\neq 0,
> $$
>
> where $r$ is a root of the indicial equation, and the series converges for $0<\left|x\right|<R$.

The word "at least one" is the whole content of the case analysis that follows. The theorem never promises two, and a candidate who assumes two loses the marks attached to the exceptional cases.

### 2.5 The indicial lemma and the factorisation

> **Lemma.** With $xp(x)=\sum p_{m}x^{m}$ and $x^{2}q(x)=\sum q_{m}x^{m}$, the admissible exponents satisfy
>
> $$
> F(r)=r(r-1)+p_{0}r+q_{0}=0 .
> $$

> **Corollary (the divisor identity).** With roots $r_{1}$ and $r_{2}$,
>
> $$
> F(s)=\left(s-r_{1}\right)\left(s-r_{2}\right),\qquad r_{1}+r_{2}=1-p_{0},\qquad r_{1}r_{2}=q_{0}.
> $$

The corollary is the single most useful examinable fact in the topic, because it converts the case analysis into one question: at which integer $n$ does $F(n+r)$ vanish? Writing $r=r_{j}$ gives

$$
F\left(n+r_{j}\right)=n\left(n+r_{j}-r_{k}\right),
$$

which vanishes at $n=0$ (always, and that is why $c_{0}$ is free) and at $n=r_{k}-r_{j}$, which is a positive integer only when the larger root is the one being used and the difference is an integer.

### 2.6 The three cases

> **Theorem.** Let $r_{1}$, $r_{2}$ be the indicial roots with $r_{1}-r_{2}$ not a negative real number.
>
> (a) If $r_{1}-r_{2}$ is not an integer, both solutions are Frobenius series.
>
> (b) If $r_{1}=r_{2}$, then $y_{1}=x^{r_{1}}\sum a_{n}x^{n}$ and $y_{2}=y_{1}\ln x+x^{r_{1}}\sum b_{n}x^{n}$, with a non-zero coefficient of the logarithm in every normalisation.
>
> (c) If $r_{1}-r_{2}=N$ is a positive integer, then $y_{2}=C y_{1}\ln x+x^{r_{2}}\sum b_{n}x^{n}$, where $C$ may be zero.

> **Justification in one line.** Applying reduction of order to $y_{1}=x^{r_{1}}u$ gives an integrand proportional to $x^{r_{2}-r_{1}-1}$ times an analytic function, and the logarithm appears exactly when that exponent is a negative integer.

The exponent formula is worth memorising, because it answers every case question in a single step. The exponent is $r_{2}-r_{1}-1$. Equal roots give exponent $-1$, so a logarithm is certain. A positive integer difference $N$ gives exponent $-N-1$, so a logarithm appears only if the coefficient of $x^{N}$ in the analytic factor is non-zero. A non-integer difference gives no logarithm at all.

### 2.7 Superposition, forcing and variation of parameters

> **Theorem.** With $L[y]=y''+py'+qy$, if $L[y_{h}]=0$ and $L[y_{p}]=F$ then $L[y_{p}+y_{h}]=F$, and the general solution of $L[y]=F$ is $y_{p}+y_{h}$.

> **Corollary (series forcing).** If $F=\sum f_{n}x^{n}$ is analytic at $0$, the ordinary template may be substituted directly and matched against the $f_{n}$. Only the relations for the powers present in $F$ are altered.

> **Lemma (variation of parameters).** A particular solution is
>
> $$
> y_{p}=-y_{1}\int\frac{y_{2}F}{W}\,dx+y_{2}\int\frac{y_{1}F}{W}\,dx,\qquad W=y_{1}y_{2}'-y_{1}'y_{2}.
> $$

The two routes must agree up to a homogeneous solution, and that fact is itself a check: if the series particular solution and the variation-of-parameters particular solution differ by something that is not a combination of $y_{1}$ and $y_{2}$, one of the two is wrong.

### 2.8 The divisor test as a single unifying statement

Every ordinary-point recurrence has a divisor $(m+2)(m+1)$ that never vanishes, and every Frobenius recurrence has a divisor containing $F(n+r)$, which does vanish at the indicial roots. That single difference explains the whole case analysis, and it also explains why the free-constant count differs.

| Situation | Divisor of the recurrence | Free data | Consequence |
| --- | --- | --- | --- |
| Ordinary point | $(m+2)(m+1)$, never zero | $c_{0}$ and $c_{1}$ | Two analytic solutions |
| Regular singular, non-integer difference | $F(n+r_{1})$ and $F(n+r_{2})$, zero only at $n=0$ | $c_{0}$ for each root | Two Frobenius solutions |
| Regular singular, equal roots | $n^{2}$ at $r=\rho$ | $c_{0}$ only | One series plus a logarithm |
| Regular singular, integer difference $N$ | $n\left(n-N\right)$ at $r=r_{2}$ | $c_{0}$ obstructed at $n=N$ | One series plus a possible logarithm |

The table is the fastest revision aid in the topic, because it reduces four separate procedures to one question about a divisor.

### 2.9 Two corollaries that earn marks cheaply

> **Corollary (parity).** If the equation contains only even powers of $x$ apart from the derivative terms that preserve parity, the recurrence links $c_{m+2}$ to $c_{m}$ and the odd and even coefficient chains are independent.

Legendre's equation $(1-x^{2})y''-2xy'+\lambda y=0$ exhibits this exactly, with recurrence $c_{m+2}=\frac{m(m+1)-\lambda}{(m+2)(m+1)}c_{m}$. When $\lambda=n(n+1)$ the chain of the same parity as $n$ terminates, producing a polynomial, and the other chain does not.

> **Corollary (identification).** If the computed series is recognised as the expansion of an elementary function, that function is the solution, by uniqueness.

Identification is the cheapest verification available and is accepted in place of a substitution check when the series is a standard one.

### 2.10 What "state the form" questions require

When a question asks for the form of the second solution without the coefficients, the full answer has three parts: the roots, the case, and the displayed form. Anything less loses marks. The model answer reads: the indicial roots are $r_{1}=2$ and $r_{2}=1$, their difference is the positive integer one, so case (c) applies and

$$
y_{2}=C\,y_{1}\ln x+x\sum_{n=0}^{\infty}b_{n}x^{n},
$$

where $C$ may be zero and must be determined if the coefficient of the logarithm is required. Stating that $C$ may be zero is part of the answer, because the examiner is testing whether the candidate knows that an integer difference does not by itself force a logarithm.

## 3. Formal Proofs, Derivations, and Methods

### 3.1 The shift lemma, as it should be written for marks (1 to 2 marks)

Step 1. State the claim.

$$
\sum_{n=N}^{\infty}A_{n}x^{n+k}=\sum_{m=N+k}^{\infty}A_{m-k}x^{m}
$$

Step 2. Substitute. Put $m=n+k$. As $n$ runs over the integers from $N$ upwards, $m$ runs over the integers from $N+k$ upwards, and the map is a bijection, so no term is created and none is lost.

Step 3. Replace the summand. Since $n=m-k$ and $x^{n+k}=x^{m}$, the term $A_{n}x^{n+k}$ becomes $A_{m-k}x^{m}$.

Step 4. Conclude. The two sums contain the same terms in the same order, so they are equal, and the lower limit has moved with the exponent as claimed.

The mark is awarded for the sentence "as $n$ runs from $N$, $m$ runs from $N+k$". Candidates who write only the formula omit the only substantive statement in the proof.

### 3.2 The first-order recurrence (4 marks)

Step 1. Expand the coefficient function and the forcing in powers of $x$, and state the radius.

$$
P(x)=\sum_{k=0}^{\infty}p_{k}x^{k},\qquad Q(x)=\sum_{n=0}^{\infty}q_{n}x^{n}
$$

Step 2. Differentiate the template and shift the index so that the result is a sum of powers $x^{n}$.

$$
y=\sum_{n=0}^{\infty}c_{n}x^{n}\qquad\Longrightarrow\qquad y'=\sum_{n=0}^{\infty}(n+1)c_{n+1}x^{n}
$$

Step 3. Form the product, collecting by total degree.

$$
P(x)y=\sum_{n=0}^{\infty}\left(\sum_{k=0}^{n}p_{k}c_{n-k}\right)x^{n}
$$

Step 4. Substitute into $y'+Py=Q$, equate the coefficient of $x^{n}$, and isolate the term containing $c_{n+1}$.

$$
(n+1)c_{n+1}+\sum_{k=0}^{n}p_{k}c_{n-k}=q_{n}
$$

Step 5. Solve for $c_{n+1}$.

$$
c_{n+1}=\frac{q_{n}-p_{0}c_{n}-\sum_{k=1}^{n}p_{k}c_{n-k}}{n+1}
$$

Step 6. Conclude that the divisor $n+1$ never vanishes, so every coefficient is determined by the previous ones and no obstruction of the Frobenius type can occur. This is the reason a first-order equation has one analytic solution family rather than a case analysis.

The marks are usually one for the differentiation, one for the product, one for the equating, one for the solved form. The conclusion in Step 6 is often worth a further mark in a "explain why the solution is unique" part.

### 3.3 The ordinary-point recurrence in general form (6 marks)

Step 1. Set up the normalised equation with analytic coefficients and the plain template.

$$
y''+p(x)y'+q(x)y=0,\qquad p=\sum_{k\ge 0}p_{k}x^{k},\qquad q=\sum_{k\ge 0}q_{k}x^{k},\qquad y=\sum_{n\ge 0}c_{n}x^{n}
$$

Step 2. Differentiate twice and shift.

$$
y''=\sum_{n=0}^{\infty}(n+2)(n+1)c_{n+2}x^{n}
$$

Step 3. Form the two products by total degree.

$$
p y'=\sum_{n=0}^{\infty}\left(\sum_{k=0}^{n}p_{k}(n-k+1)c_{n-k+1}\right)x^{n},\qquad q y=\sum_{n=0}^{\infty}\left(\sum_{k=0}^{n}q_{k}c_{n-k}\right)x^{n}
$$

Step 4. Add, equate the coefficient of $x^{n}$ to zero, and display the three $k=0$ terms separately.

$$
(n+2)(n+1)c_{n+2}+p_{0}(n+1)c_{n+1}+q_{0}c_{n}+\sum_{k=1}^{n}\left[p_{k}(n-k+1)c_{n-k+1}+q_{k}c_{n-k}\right]=0
$$

Step 5. Solve for $c_{n+2}$.

$$
c_{n+2}=-\frac{p_{0}(n+1)c_{n+1}+q_{0}c_{n}+\sum_{k=1}^{n}\left[p_{k}(n-k+1)c_{n-k+1}+q_{k}c_{n-k}\right]}{(n+2)(n+1)}
$$

Step 6. Draw both conclusions. The divisor is never zero, so the relation determines $c_{2},c_{3},\dots$ indefinitely; and neither $c_{0}$ nor $c_{1}$ ever appears as the isolated unknown, so both remain free. The two free constants are the reason the general solution is available from a single calculation.

The six marked stages are: setup, differentiated series, products, collected relation, solved recurrence, and the statement about freedom. The final statement is the one most often omitted, and it is worth a mark because it is the answer to "why are there two solutions?".

### 3.4 The indicial equation (4 marks)

Step 1. Multiply the equation by $x^{2}$ so that both products become analytic at the singular point.

$$
x^{2}y''+x\left(xp(x)\right)y'+x^{2}q(x)y=0
$$

Step 2. Write the two products as series with constant terms $p_{0}$ and $q_{0}$.

$$
xp(x)=p_{0}+p_{1}x+\cdots,\qquad x^{2}q(x)=q_{0}+q_{1}x+\cdots
$$

Step 3. Substitute $y=\sum c_{n}x^{n+r}$ and collect the lowest power. Only $n=0$ in the first term and $m=n=0$ in the two products contribute to $x^{r}$.

$$
\left[r(r-1)+p_{0}r+q_{0}\right]c_{0}x^{r}+\left(\text{higher powers}\right)=0
$$

Step 4. Equate the coefficient of $x^{r}$ to zero and divide by $c_{0}\neq 0$.

$$
r(r-1)+p_{0}r+q_{0}=0
$$

Step 5. Record the general coefficient relation, whose divisor is the key to the case analysis.

$$
F(n+r)c_{n}+\sum_{m=1}^{n}\left[p_{m}(n+r-m)+q_{m}\right]c_{n-m}=0,\qquad F(s)=s(s-1)+p_{0}s+q_{0}
$$

The marks are: one for multiplying by $x^{2}$, one for the substitution, one for identifying the lowest power, one for dividing by $c_{0}$ and stating the quadratic. Step 5 is usually expected as part of the same question and carries the marks for the recurrence.

### 3.5 Reduction of order and the origin of the logarithm (6 marks)

Step 1. State the reduction formula. If $y_{1}$ solves $y''+py'+qy=0$, a second independent solution is

$$
y_{2}=y_{1}\int\frac{\exp\left(-\int p\,dx\right)}{y_{1}^{2}}\,dx .
$$

Step 2. Justify it briefly. Substituting $y_{2}=vy_{1}$ removes the term in $v$ and leaves $\left(v'y_{1}^{2}\right)'=-p\,v'y_{1}^{2}$, which integrates at once.

Step 3. Insert the Frobenius structure. Write $y_{1}=x^{r_{1}}u(x)$ with $u$ analytic and $u(0)=1$, and write $p=p_{0}x^{-1}+(\text{analytic})$, so that

$$
\exp\left(-\int p\,dx\right)=x^{-p_{0}}v(x)
$$

with $v$ analytic and $v(0)\neq 0$.

Step 4. Compute the exponent of $x$ in the integrand, using $r_{1}+r_{2}=1-p_{0}$.

$$
-p_{0}-2r_{1}=r_{2}-r_{1}-1
$$

Step 5. Write the integrand with an analytic factor $g=v/u^{2}$, where $g(0)\neq 0$.

$$
\frac{\exp\left(-\int p\,dx\right)}{y_{1}^{2}}=x^{r_{2}-r_{1}-1}g(x)
$$

Step 6. Read off the three cases from the exponent.

- If $r_{1}-r_{2}$ is not an integer, the exponent is not a negative integer, the integral is $x^{r_{2}-r_{1}}$ times an analytic function, and $y_{2}$ is a plain Frobenius series.
- If $r_{1}=r_{2}$, the exponent is $-1$, and the integral contains $g(0)\ln x$ with $g(0)\neq 0$, so a logarithm is forced.
- If $r_{1}-r_{2}=N$ is a positive integer, the exponent is $-N-1$, and among the terms of $x^{-N-1}g(x)$ exactly the term $g_{N}x^{-1}$ integrates to a logarithm, so a logarithm appears if and only if $g_{N}\neq 0$.

Step 7. Conclude that cases (b) and (c) of the theorem are the same phenomenon seen at two different exponents, and that the coefficient of the logarithm is the analytic coefficient $g_{N}$ of the expansion.

The marks are: one for the formula, one for the justification, one for the substitution of the Frobenius structure, one for the exponent calculation, and two for reading off the cases. The exponent calculation is the discriminating step, and writing it explicitly is worth the time.

### 3.6 The ordinary-point answer, in exam order

The following sequence matches a typical mark scheme line by line.

1. Normalise and classify. State the singular points, confirm that the chosen point is ordinary, and quote the radius. One or two marks.
2. Write $y=\sum c_{n}x^{n}$ and state that $c_{0}$ and $c_{1}$ are arbitrary. One mark.
3. Display $y'$ and $y''$ with shifted indices. One mark.
4. Substitute and multiply out, writing each contribution against the power $x^{m}$.
5. Write the coefficient of $x^{0}$ and the coefficient of $x^{1}$ as separate equations. Two marks, and this is where the free constants are protected.
6. State the general recurrence. Two marks.
7. Compute the requested coefficients, keeping $c_{0}$ and $c_{1}$ symbolic. Two to four marks.
8. Write the answer as two explicit series, one multiplying $c_{0}$ and one multiplying $c_{1}$. One mark.
9. Verify, either by substituting the first terms back or by identification. One mark.

### 3.7 The Frobenius answer, in exam order

1. Normalise, identify the singular point, and verify regularity by computing $xp$ and $x^{2}q$. Two marks.
2. Read $p_{0}$ and $q_{0}$ as the values at zero. One mark.
3. Write and solve the indicial equation, naming the roots. Two marks.
4. Substitute the template with the factor $x^{r}$ kept visible. One mark.
5. Collect, and read the coefficient of $x^{r}$ as confirmation of the indicial equation. One mark.
6. Read the coefficient of $x^{r+1}$, which usually forces the first coefficient after $c_{0}$ to vanish. One mark.
7. Read the coefficient of $x^{n+r}$ for $n\ge 2$ as the recurrence, displaying the divisor $F(n+r)$ explicitly. Three marks.
8. Work the larger root completely. Two to three marks.
9. State the case and justify it from the difference of the roots, then handle the smaller root or the logarithm. Three to four marks.
10. Write the general solution with the factor $x^{r}$ included, and state the interval. One mark.

### 3.8 The non-homogeneous answer, in exam order

1. Solve the homogeneous equation first, however the question is phrased. The homogeneous solutions are needed in either route. Half the marks of the question.
2. Choose the route. If the forcing is a polynomial or a single function and the homogeneous solutions are elementary, use variation of parameters. If the forcing is a power series or the answer must be in series form, match coefficients.
3. On the series route, substitute the ordinary template into the full equation and write the coefficient relations, marking which ones are altered by the forcing.
4. On the variation-of-parameters route, compute $W$ first, then the two integrals, then assemble and simplify.
5. Add the complementary function and state the general solution with two constants.
6. Verify by substitution, and note that the answer is only defined up to a homogeneous solution.

### 3.9 Presentation habits that earn marks

Three habits separate a script that scores from one that does not.

The first is to write every series with its lower limit visible. A sum written without a lower limit invites the examiner to assume the wrong one, and it invites the candidate to make the same mistake.

The second is to keep the factor $x^{r}$ outside the display until the last line. Coefficients are then numbers, and the powers of $x$ are never tracked twice.

The third is to state the case explicitly before using it. The sentence "the roots differ by one half, which is not an integer, so both solutions are Frobenius series" is worth a mark on its own, and omitting it costs the mark even when the series are correct.

## 4. Representative Worked Examples and Solutions

Each model solution below is written as it should appear in a script, with the mark-earning step identified. The totals are indicative.

### 4.1 Problem: model solution 1, first order [8 marks]

Solve $y'=2xy$ subject to $y(0)=1$, giving terms up to $x^{8}$.

### 4.2 Solution: the odd coefficients are killed by the starting values

Step 1 (1 mark). State the template and its derivative.

$$
y=\sum_{n=0}^{\infty}c_{n}x^{n},\qquad y'=\sum_{n=0}^{\infty}(n+1)c_{n+1}x^{n}
$$

Step 2 (1 mark). Substitute and shift the right-hand side.

$$
\sum_{n=0}^{\infty}(n+1)c_{n+1}x^{n}=2x\sum_{n=0}^{\infty}c_{n}x^{n}=\sum_{n=1}^{\infty}2c_{n-1}x^{n}
$$

Step 3 (1 mark). Take the constant term separately, since the right-hand side has none.

$$
c_{1}=0
$$

Step 4 (1 mark). Take the coefficient of $x^{n}$ for $n\ge 1$ and state the recurrence.

$$
(n+1)c_{n+1}=2c_{n-1}
$$

Step 5 (2 marks). Run the recurrence from $c_{0}=1$.

$$
c_{2}=\frac{2c_{0}}{2}=1,\qquad c_{3}=\frac{2c_{1}}{3}=0,\qquad c_{4}=\frac{2c_{2}}{4}=\frac{1}{2},\qquad c_{5}=0,\qquad c_{6}=\frac{2c_{4}}{6}=\frac{1}{6},\qquad c_{8}=\frac{2c_{6}}{8}=\frac{1}{24}
$$

Step 6 (1 mark). Write the answer.

$$
y=1+x^{2}+\frac{x^{4}}{2}+\frac{x^{6}}{6}+\frac{x^{8}}{24}+\cdots
$$

Step 7 (1 mark). Verify and identify. Differentiating gives $2x+2x^{3}+x^{5}+\frac{x^{7}}{3}$, which equals $2xy$ term by term, and the constant term is one, so both the equation and the condition hold. The series is $e^{x^{2}}$, consistent with the elementary solution.

Examiner notes. The separate treatment of $n=0$ in Step 3 is a marked step; candidates who apply the general recurrence at $n=0$ obtain $c_{1}=0$ by accident and then divide by one at $n=1$, which is still correct, but they lose the mark for the separate relation and often lose the parity argument in Step 5.

### 4.3 Problem: model solution 2, ordinary point [13 marks]

Find the general solution of $\left(x^{2}-1\right)y''+3xy'+xy=0$ in powers of $x$, up to and including the term in $x^{7}$.

### 4.4 Solution: three series aligned against a common power

Step 1 (2 marks). Normalise and classify.

$$
y''+\frac{3x}{x^{2}-1}y'+\frac{x}{x^{2}-1}y=0
$$

The coefficient functions are rational with denominator $\left(x-1\right)\left(x+1\right)$, so the singular points are $1$ and $-1$. The point $0$ is ordinary, and the radius of convergence is at least one.

Step 2 (1 mark). Write the template with both derivatives.

$$
y=\sum_{n=0}^{\infty}c_{n}x^{n},\qquad y'=\sum_{n=0}^{\infty}(n+1)c_{n+1}x^{n},\qquad y''=\sum_{n=0}^{\infty}(n+2)(n+1)c_{n+2}x^{n}
$$

Step 3 (2 marks). Multiply out and align every contribution against $x^{m}$.

$$
x^{2}y''=\sum_{m=0}^{\infty}m(m-1)c_{m}x^{m},\qquad -y''=-\sum_{m=0}^{\infty}(m+2)(m+1)c_{m+2}x^{m}
$$

$$
3xy'=\sum_{m=0}^{\infty}3m c_{m}x^{m},\qquad xy=\sum_{m=1}^{\infty}c_{m-1}x^{m}
$$

Step 4 (2 marks). Write the two lowest relations separately, because the last sum starts at $m=1$.

$$
-2c_{2}=0\qquad\Longrightarrow\qquad c_{2}=0
$$

$$
3c_{1}+c_{0}-6c_{3}=0\qquad\Longrightarrow\qquad c_{3}=\frac{3c_{1}+c_{0}}{6}
$$

Step 5 (2 marks). State the general recurrence for $m\ge 1$.

$$
m(m+2)c_{m}+c_{m-1}-(m+2)(m+1)c_{m+2}=0\qquad\Longrightarrow\qquad c_{m+2}=\frac{m(m+2)c_{m}+c_{m-1}}{(m+1)(m+2)}
$$

Step 6 (2 marks). Compute the remaining coefficients.

$$
c_{4}=\frac{2\cdot 4\,c_{2}+c_{1}}{3\cdot 4}=\frac{c_{1}}{12},\qquad c_{5}=\frac{3\cdot 5\,c_{3}+c_{2}}{4\cdot 5}=\frac{3c_{1}+c_{0}}{8}
$$

$$
c_{6}=\frac{4\cdot 6\,c_{4}+c_{3}}{5\cdot 6}=\frac{c_{0}}{180}+\frac{c_{1}}{12},\qquad c_{7}=\frac{5\cdot 7\,c_{5}+c_{4}}{6\cdot 7}=\frac{105c_{0}+317c_{1}}{1008}
$$

Step 7 (1 mark). Assemble the general solution.

$$
y=c_{0}\left(1+\frac{x^{3}}{6}+\frac{x^{5}}{8}+\frac{x^{6}}{180}+\frac{5x^{7}}{48}+\cdots\right)+c_{1}\left(x+\frac{x^{3}}{2}+\frac{x^{4}}{12}+\frac{3x^{5}}{8}+\frac{x^{6}}{12}+\frac{317x^{7}}{1008}+\cdots\right)
$$

Step 8 (1 mark). Check the two lowest relations against the equation: the coefficient of $x^{0}$ is $-2c_{2}$, which vanishes, and the coefficient of $x^{1}$ is $3c_{1}+c_{0}-6c_{3}$, which vanishes by Step 4.

Examiner notes. The recurrence in Step 5 contains a term $c_{m-1}$, not $c_{m+1}$, which is unusual and is the point of the question. Candidates who mis-shift the $xy$ term obtain a recurrence linking $c_{m+2}$ to $c_{m}$ only and produce a solution that fails at the first substitution. The mark for Step 4 is awarded for treating $m=0$ separately, and the mark for Step 8 for a genuine check.

### 4.5 Problem: model solution 3, regular singular point [14 marks]

Find the general solution of $2x^{2}y''-xy'+\left(1-x^{2}\right)y=0$ about $x=0$.

### 4.6 Solution: two roots, a non-integer difference, two series

Step 1 (2 marks). Normalise and classify.

$$
y''-\frac{1}{2x}y'+\frac{1-x^{2}}{2x^{2}}y=0,\qquad xp(x)=-\frac{1}{2},\qquad x^{2}q(x)=\frac{1-x^{2}}{2}
$$

Both products are polynomials, hence analytic at $0$, so the point is a regular singular point.

Step 2 (1 mark). Read the two constants.

$$
p_{0}=-\frac{1}{2},\qquad q_{0}=\frac{1}{2}
$$

Step 3 (2 marks). Write and solve the indicial equation.

$$
r(r-1)-\frac{r}{2}+\frac{1}{2}=0\qquad\Longrightarrow\qquad 2r^{2}-3r+1=0\qquad\Longrightarrow\qquad r=1,\ r=\frac{1}{2}
$$

Step 4 (1 mark). Substitute the template, keeping the factor $x^{r}$ visible.

$$
y=\sum_{n=0}^{\infty}c_{n}x^{n+r},\qquad y'=\sum_{n=0}^{\infty}(n+r)c_{n}x^{n+r-1},\qquad y''=\sum_{n=0}^{\infty}(n+r)(n+r-1)c_{n}x^{n+r-2}
$$

Step 5 (1 mark). Collect and factor the bracket on the unshifted terms.

$$
2(n+r)(n+r-1)-(n+r)+1=\left(2(n+r)-1\right)\left(n+r-1\right)
$$

Step 6 (1 mark). Read the coefficient of $x^{r+1}$.

$$
\left(2r+1\right)r\,c_{1}=0\qquad\Longrightarrow\qquad c_{1}=0
$$

Step 7 (2 marks). Read the coefficient of $x^{n+r}$ for $n\ge 2$ and display the divisor.

$$
\left(2(n+r)-1\right)\left(n+r-1\right)c_{n}=c_{n-2}\qquad\Longrightarrow\qquad c_{n}=\frac{c_{n-2}}{\left(2(n+r)-1\right)\left(n+r-1\right)}
$$

Step 8 (2 marks). Work the larger root $r=1$.

$$
c_{2}=\frac{c_{0}}{5\cdot 2}=\frac{c_{0}}{10},\qquad c_{4}=\frac{c_{2}}{9\cdot 4}=\frac{c_{0}}{360},\qquad c_{6}=\frac{c_{4}}{13\cdot 6}=\frac{c_{0}}{28080}
$$

$$
y_{1}=x\left(1+\frac{x^{2}}{10}+\frac{x^{4}}{360}+\frac{x^{6}}{28080}+\cdots\right)
$$

Step 9 (2 marks). Work the smaller root $r=\frac{1}{2}$ and state the case.

$$
c_{2}=\frac{c_{0}}{4\cdot\frac{3}{2}}=\frac{c_{0}}{6},\qquad c_{4}=\frac{c_{2}}{8\cdot\frac{7}{2}}=\frac{c_{0}}{168},\qquad c_{6}=\frac{c_{4}}{12\cdot\frac{11}{2}}=\frac{c_{0}}{11088}
$$

The difference of the roots is $\frac{1}{2}$, which is not an integer, so case (a) applies and no logarithm appears.

Step 10 (1 mark). Write the general solution and the interval.

$$
y=Ax\left(1+\frac{x^{2}}{10}+\frac{x^{4}}{360}+\cdots\right)+Bx^{1/2}\left(1+\frac{x^{2}}{6}+\frac{x^{4}}{168}+\cdots\right),\qquad x>0
$$

Examiner notes. Two marks are attached to the statement of the case in Step 9, and they are lost if the candidate produces two series without saying why two are available. The factor $x$ in $y_{1}$ and the factor $x^{1/2}$ in $y_{2}$ are separate marks; a solution that omits them satisfies nothing.

### 4.7 Problem: model solution 4, non-homogeneous [10 marks]

Solve $y''+y=x$ in powers of $x$.

### 4.8 Solution: one coefficient relation is altered by the forcing

Step 1 (3 marks). Substitute the template into the homogeneous left-hand side in aligned form.

$$
\sum_{n=0}^{\infty}(n+2)(n+1)c_{n+2}x^{n}+\sum_{n=0}^{\infty}c_{n}x^{n}=x
$$

Step 2 (2 marks). Compare coefficients, noting that the right-hand side is $1\cdot x+0\cdot x^{2}+\cdots$ and has no constant term.

$$
2c_{2}+c_{0}=0,\qquad 6c_{3}+c_{1}=1,\qquad (n+2)(n+1)c_{n+2}+c_{n}=0\quad\left(n\ne 1\right)
$$

Step 3 (2 marks). Solve the relations with convenient values $c_{0}=1$, $c_{1}=0$.

$$
c_{2}=-\frac{1}{2},\qquad c_{3}=\frac{1}{6},\qquad c_{4}=\frac{1}{24},\qquad c_{5}=-\frac{1}{120},\qquad c_{6}=-\frac{1}{720},\qquad c_{7}=\frac{1}{5040}
$$

Step 4 (1 mark). Write the series.

$$
y=1-\frac{x^{2}}{2}+\frac{x^{3}}{6}+\frac{x^{4}}{24}-\frac{x^{5}}{120}-\frac{x^{6}}{720}+\frac{x^{7}}{5040}+\cdots
$$

Step 5 (1 mark). Identify the structure. The even part with signs is $\cos x$, and the remaining odd terms are $x-\sin x$, so the general solution is

$$
y=\left(1-\frac{x^{2}}{2}+\frac{x^{4}}{24}-\frac{x^{6}}{720}+\cdots\right)+\left(\frac{x^{3}}{6}-\frac{x^{5}}{120}+\frac{x^{7}}{5040}-\cdots\right)=A\cos x+B\sin x+x .
$$

Step 6 (1 mark). Verify. With $y=A\cos x+B\sin x+x$, the second derivative is $-A\cos x-B\sin x$, so $y''+y=x$ identically.

Examiner notes. The single non-zero coefficient on the right-hand side alters exactly one relation, and the mark is awarded for identifying which. Candidates who alter the general recurrence lose the mark and every subsequent coefficient.

### 4.9 Problem: model solution 5, equal roots [6 marks]

Solve $4x^{2}y''+y=0$ about $x=0$.

### 4.10 Solution: the repeated root forces a logarithm

Step 1 (1 mark). Normalise, classify and compute the constants.

$$
y''+\frac{1}{4x^{2}}y=0,\qquad xp(x)=0,\qquad x^{2}q(x)=\frac{1}{4},\qquad p_{0}=0,\ q_{0}=\frac{1}{4}
$$

Step 2 (1 mark). Write the indicial equation.

$$
r(r-1)+\frac{1}{4}=0\qquad\Longrightarrow\qquad \left(r-\frac{1}{2}\right)^{2}=0\qquad\Longrightarrow\qquad r=\frac{1}{2}\ \text{(repeated)}
$$

Step 3 (1 mark). State the first solution, noting that the coefficient relation is $4n^{2}c_{n}=0$ for $n\ge 1$.

$$
y_{1}=x^{1/2}
$$

Step 4 (2 marks). State and use the equal-root form.

$$
y_{2}=y_{1}\ln x+x^{1/2}\sum_{n=0}^{\infty}b_{n}x^{n}=x^{1/2}\ln x
$$

Step 5 (1 mark). Write the general solution and verify both families.

$$
4x^{2}\left(-\frac{1}{4}x^{-3/2}\right)+x^{1/2}=0,\qquad 4x^{2}\left(-\frac{1}{4}x^{-3/2}\ln x\right)+x^{1/2}\ln x=0
$$

$$
y=x^{1/2}\left(A+B\ln x\right)
$$

Examiner notes. The mark in Step 4 is awarded for the displayed form $y_{1}\ln x+x^{r}\sum b_{n}x^{n}$, even before any coefficient is found. A candidate who writes only $y=x^{1/2}$ has found one solution of a second-order equation and loses the marks for the case.

## 5. Mathematical Extensions, Limits, and Common Errors

### 5.1 The trap table

The table lists the errors that are actually made in examinations, with the symptom each produces and the cure. Reading the symptom column is the fastest way to diagnose a script that does not check out.

| Trap | How it arises | Symptom | Cure |
| --- | --- | --- | --- |
| Index shift without moving the limit | Writing $x^{2}y''$ as $\sum n(n-1)c_{n}x^{n}$ and adding it to an unshifted sum | The recurrence is off by one power; substitution fails at the lowest power | Rename with a new letter and move the lower limit at the same time |
| Forgetting the lower starting index in Frobenius | Starting the $c_{n}$ recurrence at $n=0$ or treating $c_{1}$ as free | Division by $F(r)$, which is zero; a lost $c_{0}$; a spurious free constant | Read $n=0$, then $n=1$, then $n\ge 2$ as three separate relations |
| Equal roots treated as two series | Writing $x^{r_{1}}\sum a_{n}x^{n}$ and $x^{r_{2}}\sum b_{n}x^{n}$ with $r_{1}=r_{2}$ | Two identical series claimed to be independent | Use $y_{2}=y_{1}\ln x+x^{\rho}\sum b_{n}x^{n}$ and say why |
| Integer difference assumed to force a log | Applying the theorem without computing the coefficient | A superfluous $\ln x$ in an Euler equation | Compute $g_{N}$ from the reduction formula; if it vanishes, drop the log |
| Integer difference assumed to forbid a log | Concluding from distinct roots that both series are plain | A missing logarithm, so only one solution is presented | Check whether the divisor vanishes at $n=N$; if it does, the log may appear |
| Dividing by a vanishing divisor | Solving $F(n+r)c_{n}=(\text{known})$ by division when $F$ vanishes | A coefficient that is infinite or a contradiction ignored | Stop and record the obstruction; do not divide |
| Dropping the factor $x^{r}$ | Presenting the bracket only | The answer satisfies the equation only when $r=0$ | Keep $x^{r}$ outside every display until the final line |
| Allowing $c_{0}=0$ in Frobenius | Treating $c_{0}$ as an ordinary coefficient | Indicial equation lost or a third constant claimed | State $c_{0}\neq 0$ and divide by it explicitly |
| Classifying the un-normalised equation | Reading the coefficient of $y''$ instead of $p$ and $q$ | A point called singular when it is ordinary, or the reverse | Divide by the coefficient of $y''$ first, always |
| Infinite radius claimed | Ignoring complex singular points | A series used outside its interval | Locate all singularities, real and complex, then quote the distance |
| Two roots mixed in one recurrence | Carrying $r$ symbolically to the end | A recurrence containing both roots | Fix one root, finish that series, then start the other |
| Forcing ignored in the general recurrence | Using the homogeneous recurrence for every $n$ | The particular solution is a homogeneous one and $L[y]\ne F$ | Mark which powers of $F$ are non-zero and alter only those relations |
| Verification omitted | Stopping at the series | An unchecked arithmetic slip in a coefficient | Substitute the first few terms, or identify the series |

### 5.2 Marking priorities

The distribution of marks rewards a specific order of work, and a candidate who follows it will finish more questions in the same time.

The first priority is the classification and the template, because they are worth three marks and cost one minute. The second is the recurrence, because it is worth about a third of the question and everything numerical depends on it. The third is the case statement at a singular point, which is worth two to three marks and consists of one sentence. The fourth is the coefficient arithmetic, which is worth two to four marks and is mechanical. The verification is worth one mark and should be attempted only if time allows.

Two habits cost marks disproportionately. Writing a sum without its lower limit invites the examiner to assume the wrong one even when the mathematics is right. Presenting a final answer without the factor $x^{r}$ converts a correct computation into a wrong answer, because the displayed solution does not solve the equation.

### 5.3 Time strategy

A fifteen-mark question should take about twenty-five minutes, which is between one and two minutes per mark.

| Stage | Minutes | Must be complete before moving on |
| --- | --- | --- |
| Read, normalise, classify | 2 | Singular points and radius written down |
| Template and derivatives | 2 | The template displayed with its two derivatives |
| Multiply out and align | 6 | Every contribution written against the same power |
| Two lowest relations | 3 | The coefficients of $x^{0}$ and $x^{1}$ solved |
| General recurrence | 2 | Divider displayed and factorised |
| Coefficients to the required order | 5 | Requested number of non-zero terms |
| Second root, case statement | 4 | The case named and justified |
| Final answer, interval, check | 2 | Two independent solutions and the interval |

The plan reserves nothing for the verification, and that is deliberate: the verification is the first item to abandon under time pressure, because a wrong coefficient usually shows up as a failure of the final check anyway and the check itself earns only one mark. What must never be abandoned is the case statement, which earns more marks than the arithmetic it accompanies.

A three-hour paper with six questions leaves about thirty minutes per question. The topic question is usually the longest, so the sensible allocation is thirty minutes there and twenty-five for each of the others, with the last fifteen minutes reserved for checking the classification and the presence of $x^{r}$ in every answer.

### 5.4 Revision checklist

Work through the list and tick only what can be reproduced from memory without notes.

- State the three conditions for the first-order equation $y'=f(x,y)$ and explain what each one prevents.
- Derive the first-order recurrence $c_{n+1}=\left(q_{n}-p_{0}c_{n}-\sum_{k=1}^{n}p_{k}c_{n-k}\right)/(n+1)$ from the template.
- Prove the index-shift lemma in two lines, including the sentence about the range of the new letter.
- Normalise any given equation and list its singular points with their classification.
- Write the ordinary-point recurrence in general form and explain why exactly two coefficients are free.
- Derive the indicial equation $r(r-1)+p_{0}r+q_{0}=0$ from the substitution of $y=x^{r}\sum c_{n}x^{n}$.
- Factor the indicial polynomial as $(s-r_{1})(s-r_{2})$ and quote $r_{1}+r_{2}=1-p_{0}$ and $r_{1}r_{2}=q_{0}$.
- State the three cases of the second solution with the correct coefficient in front of $\ln x$.
- Derive the exponent $r_{2}-r_{1}-1$ from the reduction-of-order formula.
- Compute a full ordinary-point solution to the term in $x^{5}$ without error in the alignment.
- Compute two Frobenius series for a non-integer difference of roots, including the factors $x^{r}$.
- Solve one homogeneous and one non-homogeneous equation by variation of parameters and check the agreement with the series particular solution.
- Quote the radius of convergence for an equation with real and with complex singular points.
- Recognise an irregular singular point and state why the method fails there.

### 5.5 Where the method stops

Three limitations are worth stating in an examination when a question asks for comment.

The first is the radius. A series about an ordinary point is guaranteed only up to the nearest singular point, measured in the complex plane. For $\left(1+x^{2}\right)y''+y=0$ the nearest singularities are at $\pm i$, so the radius is one although the equation has no real singular point. The series may converge further in special cases, but the guarantee stops there.

The second is the irregular singular point, where no Frobenius series exists. For $x^{3}y''+y=0$ the product $x^{2}q$ equals $x^{-1}$, which blows up, and the substitution forces $c_{0}=0$, contradicting the normalisation. Solutions there behave like exponentials of reciprocal powers, and describing them requires asymptotic rather than convergent series.

The third is the boundary of the singular point itself. A Frobenius solution with non-integer exponent is defined on $x>0$ or on $x<0$ but not across the origin, because $x^{1/2}$ is not real for negative $x$. Questions that ask for the interval of validity are testing exactly this point.

An extension worth knowing is that the same machinery defines the classical special functions. Legendre's equation produces the Legendre polynomials when the recurrence terminates, Bessel's equation produces the Bessel functions with exponents $\pm\nu$ and a logarithm when $2\nu$ is an integer, and Hermite's equation produces the Hermite polynomials by the same termination mechanism. In each case the series is not an approximation to the function but the definition of it.

### 5.6 The five lines worth memorising

The whole topic reduces to five displayed statements, and a candidate who can write them at the top of the page can reconstruct every answer.

$$
p_{0}=\lim_{x\to 0}xp(x),\qquad q_{0}=\lim_{x\to 0}x^{2}q(x)
$$

$$
F(s)=s(s-1)+p_{0}s+q_{0}=\left(s-r_{1}\right)\left(s-r_{2}\right)
$$

$$
F(n+r)c_{n}+\sum_{m=1}^{n}\left[p_{m}(n+r-m)+q_{m}\right]c_{n-m}=0
$$

$$
y_{2}=y_{1}\int\frac{\exp\left(-\int p\,dx\right)}{y_{1}^{2}}\,dx,\qquad \text{exponent}=r_{2}-r_{1}-1
$$

$$
y_{p}=-y_{1}\int\frac{y_{2}F}{W}\,dx+y_{2}\int\frac{y_{1}F}{W}\,dx
$$

The first pair classifies the point, the second pair produces the recurrence and the case analysis, and the fifth line handles the non-homogeneous equation. Nothing else in the topic is needed under examination conditions.
