## 1. Foundational Concepts, Definitions, and Axioms

### 1.1 What the examiner is testing

Every question on this topic reduces to one of four tasks, and each has a fixed answer shape.

The first task is to put an equation into normalised form. The second is to locate its singular points. The third is to classify each singular point as regular or irregular by computing two limits. The fourth is to state, in the words of the existence theorem, what kind of series solution is guaranteed at each point. A question may ask for one of these tasks alone or for all four in sequence, and the marks are distributed in proportion to the work shown.

The definitions must be reproduced precisely, because a definition with a missing clause earns nothing. Learn the following four statements word for word, together with the notation they use.

> **Definition (normalised form).** A second-order linear homogeneous equation
>
> $$
> a_{0}(x)y''+a_{1}(x)y'+a_{2}(x)y=0
> $$
>
> with $a_{0}(x)\neq0$ is put in normalised form by dividing by $a_{0}$, giving
>
> $$
> y''+P(x)y'+Q(x)y=0, \qquad P=\frac{a_{1}}{a_{0}}, \quad Q=\frac{a_{2}}{a_{0}} .
> $$

> **Definition (ordinary and singular points).** A point $x_{0}$ is an ordinary point of the normalised equation if both $P$ and $Q$ are analytic at $x_{0}$. If at least one of them is not analytic at $x_{0}$, then $x_{0}$ is a singular point.

> **Definition (regular singular point).** A singular point $x_{0}$ is a regular singular point if both products
>
> $$
> \left(x-x_{0}\right)P(x) \qquad \text{and} \qquad \left(x-x_{0}\right)^{2}Q(x)
> $$
>
> are analytic at $x_{0}$.

> **Definition (irregular singular point).** A singular point which is not regular is called an irregular singular point.

Three phrases in those definitions carry marks and are routinely omitted. The first is "at least one", which makes the singular case the negation of the ordinary case and not a separate condition. The second is the two different powers, one bracket for $P$ and two brackets for $Q$; using the same power twice is an automatic loss. The third is the word analytic, which is a stronger statement than "finite", although at an isolated point the two coincide and the limit test may be used.

### 1.2 The limit test, in the form you will write it

> **Test (regularity by limits).** Let $x_{0}$ be a singular point. Then $x_{0}$ is regular singular if and only if both limits
>
> $$
> p_{0}=\lim_{x\to x_{0}}\left(x-x_{0}\right)P(x), \qquad q_{0}=\lim_{x\to x_{0}}\left(x-x_{0}\right)^{2}Q(x)
> $$
>
> exist and are finite.

The two numbers $p_{0}$ and $q_{0}$ are not incidental. They are the coefficients of the indicial equation, so a question that asks for exponents after classification gives the marks for these limits twice over.

A classification answer that consists only of the conclusion is worth very little. The examiner wants to see, for each singular point, the simplified products and the evaluated limits. In practice this means the following two computations, written out for each point.

$$
\left(x-x_{0}\right)P(x)=\text{(simplified expression)}\to p_{0},
$$

$$
\left(x-x_{0}\right)^{2}Q(x)=\text{(simplified expression)}\to q_{0}.
$$

Then a one-line verdict. Anything shorter is an assertion, not a computation.

### 1.3 The three-way summary you should be able to reproduce

| Nature of $x_{0}$ | Test outcome | Solution guaranteed | Validity |
| --- | --- | --- | --- |
| Ordinary | $P$ and $Q$ analytic at $x_{0}$ | two independent series $\sum C_{n}\left(x-x_{0}\right)^{n}$ | $\lvert x-x_{0}\rvert<R$, $R\ge$ distance to nearest singular point |
| Regular singular | singular, both products analytic | at least one series $\left(x-x_{0}\right)^{r}\sum C_{n}\left(x-x_{0}\right)^{n}$, $C_{0}\neq0$ | $0<\lvert x-x_{0}\rvert<R$ |
| Irregular singular | singular, at least one product not analytic | nothing is guaranteed | not applicable |

The third column is where most marks are lost. At an ordinary point the guarantee is two solutions; at a regular singular point it is one solution plus a possible second one with a logarithm; at an irregular singular point it is no guarantee at all. Writing "two solutions" for a regular singular point, or "no solution" for an irregular one, contradicts the theorem.

### 1.4 Terminology that the examiner uses interchangeably

Several phrases mean the same thing and are used without warning.

The phrase "analytic at $x_{0}$" is sometimes replaced by "regular at $x_{0}$" when applied to a coefficient function, but never when applied to a point of the equation. A "regular point" is not standard usage in this course; the standard pair is ordinary and singular.

The phrase "does not become infinite at $x_{0}$" appears in informal statements of analyticity. It is a necessary condition only, and in this course every function tested is a rational function or a trigonometric function with isolated zeros, for which finiteness and analyticity coincide. Use the safe phrasing: a rational function is analytic wherever its denominator does not vanish.

The phrase "power series solution about $x_{0}$" always refers to the centre of expansion. A series about $x_{0}=2$ is written in powers of $x-2$, never in powers of $x$. Mixing the centre into the products is the single most common computational slip: at $x_{0}=2$ the products are $\left(x-2\right)P$ and $\left(x-2\right)^{2}Q$, not $xP$ and $x^{2}Q$.

### 1.5 The role of the coefficient of the second derivative

The classification never uses $a_{0}$, $a_{1}$ or $a_{2}$ directly; it uses $P$ and $Q$ after division. This has two consequences that decide many marks.

First, the singular points are not simply the zeros of $a_{0}$. They are the points where $P$ or $Q$ fails to be analytic after cancellation. A zero of $a_{0}$ that also divides $a_{1}$ and $a_{2}$ produces no singularity at all. The equation

$$
\left(x^{2}-4\right)y''+(x-2)y'=0
$$

has $a_{0}$ vanishing at $x=2$, yet

$$
P=\frac{x-2}{x^{2}-4}=\frac{1}{x+2}, \qquad Q=0,
$$

so $x=2$ is ordinary.

Second, singular points can occur where $a_{0}$ does not vanish. The equation

$$
y''+\frac{1}{x-3}y'+y=0
$$

has $a_{0}=1$ everywhere, and yet $x=3$ is singular because $P$ blows up there. So the search for singular points must be conducted on $P$ and $Q$, not on $a_{0}$.

## 2. Theorems, Lemmas, and Analytical Properties

### 2.1 High-yield results and their mark values

The table lists the results that appear in almost every paper, with the marks typically attached to a correct statement and correct use. The values are indicative of weighting, not a contract.

| Result | What earns the marks | Typical marks |
| --- | --- | --- |
| Normalisation | dividing by $a_{0}$ and naming $P$ and $Q$ correctly | 2 |
| Locating singular points | listing the points where $P$ or $Q$ is not analytic, after cancellation | 2 |
| First regularity test | forming and simplifying $\left(x-x_{0}\right)P$ and evaluating the limit | 2 |
| Second regularity test | forming and simplifying $\left(x-x_{0}\right)^{2}Q$ and evaluating the limit | 2 |
| Verdict at a point | regular if both limits finite, irregular otherwise, with the failing test named | 1 |
| Statement of the solution form | correct form and correct interval for the classification obtained | 2 |
| Indicial equation | correct quadratic and both roots | 3 |
| Radius of a series solution | distance to the nearest singular point, or ratio test | 2 |
| Analyticity test | producing a power series and its radius, or identifying a pole | 2 |
| Standard equations | Legendre, Bessel, hypergeometric classifications quoted correctly | 4 |

Two habits convert these weights into marks. Always write the simplified product before the limit, because the simplification is where the algebra marks sit. Always name the test that fails when a point is irregular, because a bare verdict hides the reason and often loses the final mark.

### 2.2 The classification theorem

> **Theorem (classification).** Let $P$ and $Q$ be analytic on a punctured neighbourhood of $x_{0}$. Then $x_{0}$ is exactly one of: an ordinary point, a regular singular point, an irregular singular point.

The hypothesis of analyticity on a punctured neighbourhood is what makes the trichotomy exhaustive. In every equation of this course it holds automatically, because the coefficients are analytic and $a_{0}$ has isolated zeros.

> **Theorem (pole-order form of the test).** Under the same hypothesis, $x_{0}$ is a regular singular point if and only if $P$ has a pole of order at most one at $x_{0}$ and $Q$ has a pole of order at most two at $x_{0}$.

The pole-order form is the fastest route to a verdict when the coefficients are rational. Read the order of the pole by inspection of the factored denominator, and the classification follows without any limit computation. The limit computation remains the safer presentation, because it displays the algebra that the examiner is marking.

### 2.3 The existence theorem, stated in examinable form

> **Theorem (ordinary point).** If $x_{0}$ is an ordinary point, the equation has two linearly independent solutions
>
> $$
> y=\sum_{n=0}^{\infty}C_{n}\left(x-x_{0}\right)^{n},
> $$
>
> and every solution near $x_{0}$ is a linear combination of them. Each series converges at least for $\left|x-x_{0}\right|<R$, where $R$ is the distance from $x_{0}$ to the nearest singular point.

> **Theorem (regular singular point).** If $x_{0}$ is a regular singular point, the equation has at least one nontrivial solution
>
> $$
> y=\left(x-x_{0}\right)^{r}\sum_{n=0}^{\infty}C_{n}\left(x-x_{0}\right)^{n}, \qquad C_{0}\neq0,
> $$
>
> valid on a deleted interval $0<\left|x-x_{0}\right|<R$. The exponent $r$ is a root of the indicial equation
>
> $$
> r(r-1)+p_{0}r+q_{0}=0,
> $$
>
> where $p_{0}$ and $q_{0}$ are the finite limits of the two tests. If the roots differ by a non-integer, two such solutions exist; if they differ by an integer or coincide, the second solution may contain a term in $\ln\left(x-x_{0}\right)$.

> **Theorem (irregular singular point).** If $x_{0}$ is an irregular singular point, the existence of a solution of either of the above forms is not assured.

Three words in these statements are load-bearing: "two" at an ordinary point, "at least one" at a regular singular point, and "not assured" at an irregular one. Reproduce those words exactly.

### 2.4 The indicial equation and what it delivers

> **Lemma (indicial equation).** Let $x_{0}$ be a regular singular point, $t=x-x_{0}$, and let $p_{0}$, $q_{0}$ be the limits of $tP$ and $t^{2}Q$ at $t=0$. If $y=t^{r}\sum C_{n}t^{n}$ with $C_{0}\neq0$ solves the equation, then
>
> $$
> r(r-1)+p_{0}r+q_{0}=0 .
> $$

The lemma turns the classification into quantitative information. Four cases arise, and each has a standard conclusion.

| Roots of the indicial equation | Number of Frobenius solutions | Second solution |
| --- | --- | --- |
| real, difference not an integer | two | same form, with the other exponent |
| real, difference an integer | one guaranteed | may contain a logarithm |
| equal | one guaranteed | contains a logarithm with coefficient one |
| complex conjugates | two | same form, with complex exponents |

For complex roots the solutions are real only after taking combinations, and the real solutions then contain $\cos\left(\beta\ln t\right)$ and $\sin\left(\beta\ln t\right)$ multiplied by $t^{\alpha}$, where the roots are $\alpha\pm i\beta$.

### 2.5 The three standard equations as quotable results

> **Theorem (Legendre).** For $\left(1-x^{2}\right)y''-2xy'+p(p+1)y=0$, the singular points are $x=\pm1$, both regular; every other finite point is ordinary; the exponents at each of $\pm1$ are $0$ and $0$.

> **Theorem (Bessel).** For $x^{2}y''+xy'+\left(x^{2}-n^{2}\right)y=0$, the only singular point is $x=0$ and it is regular, with exponents $n$ and $-n$; every nonzero point is ordinary.

> **Theorem (hypergeometric).** For $x(1-x)y''+\left[c-(a+b+1)x\right]y'-aby=0$ with $c$ not a non-positive integer, the singular points are $x=0$ and $x=1$, both regular; the exponents are $0$ and $1-c$ at $x=0$, and $0$ and $c-a-b$ at $x=1$; every other finite point is ordinary.

Each of these three is proved by the same two products, and a question that asks you to verify one of them wants exactly that computation, not a quotation. Quote the result only when the question asks for the classification without proof.

### 2.6 The shapes of questions asked

| Question pattern | Typical wording | Required response |
| --- | --- | --- |
| Locate and classify | "Locate and classify the singular points" | normalise, list points, test each with both products, verdict |
| Verify a claim | "Show that $x=0$ is a regular singular point" | the two products, both limits, then the verdict |
| Ordinary point demonstration | "Show that $x=0$ is an ordinary point" | exhibit $P$ and $Q$, argue analyticity at the point |
| Nature of the solution | "State the nature of the power series solution near each singular point" | quote the relevant clause of the existence theorem |
| Exponents | "Find the exponents at the singular point" | compute $p_{0}$, $q_{0}$, solve the indicial quadratic |
| Radius | "State the radius of convergence of the series about $x_{0}$" | distance to nearest singular point, or ratio test |
| Analyticity | "Determine whether the function is analytic at the point" | power series with radius, or identify the obstruction |

The wording "state the nature of the solution" is the one that catches students who have learned the classification but not the theorem. A complete answer names the form of the series and the interval on which it is valid.

### 2.7 Two results that are often misquoted

The first is the claim that at a regular singular point the series converges for $\left|x-x_{0}\right|<R$ including the centre. It does not: the correct interval is the deleted interval $0<\left|x-x_{0}\right|<R$, because the factor $\left(x-x_{0}\right)^{r}$ may be infinite at the centre. The distinction matters whenever $r$ is negative or complex.

The second is the claim that at an ordinary point the radius equals the distance to the nearest singular point. The theorem gives "at least", not "equals". The actual radius can be larger, as it is for Legendre's equation with $p$ a non-negative integer, where one solution is a polynomial with infinite radius.

## 3. Formal Proofs, Derivations, and Methods

### 3.1 Deriving the two tests from the normalised form

The tests are not conventions; they follow from the requirement that the three terms of the equation be capable of cancelling one another.

Let $x_{0}$ be singular and put $t=x-x_{0}$. Since $P$ is analytic on a punctured disc around the origin, it has a Laurent expansion

$$
P(t)=\sum_{k=-\infty}^{\infty}b_{k}t^{k}
$$

with only finitely many negative powers. Multiply by one power of $t$:

$$
tP(t)=\sum_{k=-\infty}^{\infty}b_{k}t^{k+1}.
$$

The product is analytic at the origin exactly when no negative power appears, which requires $b_{k}=0$ for every $k\le-2$. That is exactly the statement that the principal part of $P$ is at most $\frac{b_{-1}}{t}$, that is, that $P$ has a pole of order at most one. In that case

$$
p_{0}=\lim_{t\to0}tP(t)=b_{-1}.
$$

Repeating the argument with two powers of $t$ gives

$$
t^{2}Q(t)=\sum_{k=-\infty}^{\infty}d_{k}t^{k+2},
$$

which is analytic at the origin exactly when $d_{k}=0$ for every $k\le-3$, that is, when $Q$ has a pole of order at most two; then

$$
q_{0}=\lim_{t\to0}t^{2}Q(t)=d_{-2}.
$$

The balance argument explains why these orders and no others. Multiply the equation by $t^{2}$ and insert the model solution $y=t^{r}$:

$$
t^{2}y''=r(r-1)t^{r}, \qquad t^{2}Py'=r\left(tP\right)t^{r}, \qquad t^{2}Qy=\left(t^{2}Q\right)t^{r}.
$$

All three terms carry the power $t^{r}$ precisely when $tP$ and $t^{2}Q$ are bounded. If $P$ had a pole of order two, the middle term would carry the power $t^{r-1}$ while the other two carried $t^{r}$, and no choice of $r$ could cancel the leading term. The condition is therefore forced, not chosen.

A limit that is finite is the same thing as a removable singularity, which is the same thing as an analytic extension, so the limit form and the analyticity form of the test are interchangeable. In an examination the limit form is used, because it can be written down and evaluated.

### 3.2 Why the tests cannot be applied to ordinary points

> **Proposition.** If $x_{0}$ is an ordinary point, then $\left(x-x_{0}\right)P$ and $\left(x-x_{0}\right)^{2}Q$ are both analytic at $x_{0}$.

Both products are products of a polynomial and an analytic function, and the product of two functions analytic at a point is analytic there. The proposition is immediate, and it has a sharp consequence: the two tests give a positive answer at every ordinary point as well as at every regular singular point. They therefore cannot distinguish those two cases, and the classification must begin by locating the singular points.

This is why the standard answer template of Section 3.4 begins with "the singular points are ...", not with "applying the tests". A script that starts with the tests will classify the whole real line as regular singular and lose the marks for ordinary points entirely.

### 3.3 Deriving the indicial equation

Write, near a regular singular point with $t=x-x_{0}$,

$$
P=\frac{p_{0}}{t}+P_{1}(t), \qquad Q=\frac{q_{0}}{t^{2}}+\frac{q_{1}}{t}+Q_{1}(t),
$$

with $P_{1}$ and $Q_{1}$ analytic. Substitute $y=t^{r}\sum C_{n}t^{n}$ and multiply by $t^{2}$. The three contributions are

$$
t^{2}y''=\sum_{n=0}^{\infty}(n+r)(n+r-1)C_{n}t^{n+r},
$$

$$
t^{2}Py'=\sum_{n=0}^{\infty}p_{0}(n+r)C_{n}t^{n+r}+\cdots ,
$$

$$
t^{2}Qy=\sum_{n=0}^{\infty}q_{0}C_{n}t^{n+r}+\cdots ,
$$

where the dots denote powers $t^{n+r+1}$ and higher. The lowest power present is $t^{r}$, occurring only when $n=0$, and its coefficient must vanish:

$$
C_{0}\left[r(r-1)+p_{0}r+q_{0}\right]=0 .
$$

Because $C_{0}\neq0$, the bracket vanishes, which is the indicial equation. Equating the coefficient of $t^{r+1}$ to zero then determines $C_{1}$ in terms of $C_{0}$, and each subsequent power determines one more coefficient, so the whole series is determined by the single number $C_{0}$.

For the Euler equation, where $P_{1}$ and $Q_{1}$ vanish, the argument collapses to a one-line computation:

$$
t^{2}y''+p_{0}ty'+q_{0}y=0 \quad\text{with}\quad y=t^{r} \quad\text{gives}\quad \left[r(r-1)+p_{0}r+q_{0}\right]t^{r}=0 .
$$

### 3.4 The answer template for a classification question

Write the following seven lines for every singular point, in this order. The order is what makes the answer readable and what lets the examiner find the marks quickly.

1. State the normalised equation and name $P$ and $Q$ explicitly, with the denominators factored.
2. State the singular points, with the reason: the points where $P$ or $Q$ is not analytic.
3. For the first singular point, write $\left(x-x_{0}\right)P(x)$ and simplify it to a single fraction.
4. Evaluate $p_{0}$ as the limit, and say that the function is analytic there because the denominator does not vanish.
5. Repeat with $\left(x-x_{0}\right)^{2}Q(x)$ and $q_{0}$.
6. Give the verdict at that point, naming the failing test if the point is irregular.
7. Repeat for each remaining singular point, then state the solution form guaranteed at each.

Step 4 deserves a word of explanation. Saying only "$p_{0}=1$, finite" earns the arithmetic mark but not the analyticity mark, because finiteness at the limit is being used as a proxy for analyticity. The safe sentence is: the simplified product is a rational function whose denominator is nonzero at $x_{0}$, hence it is analytic there, and its value is $p_{0}$.

### 3.5 Analyticity tests through series and radius

When a question asks whether a function is analytic at a point, there are two routes, and both are examinable.

The series route writes the function as a power series and states the radius. A function is analytic at $x_{0}$ exactly when such a series exists with a positive radius. For example,

$$
\frac{1}{1-x}=1+x+x^{2}+x^{3}+\cdots , \qquad R=1,
$$

so the function is analytic at $0$ with radius one. The ratio of successive coefficients is one, so the radius is one by the ratio test, and the same conclusion follows from the pole at $x=1$.

The obstruction route identifies a point where the function cannot be analytic. A function that becomes infinite at $x_{0}$ cannot be analytic there, and a function whose nearest complex obstruction is at distance $d$ has radius $d$. The example that every examiner likes is

$$
\frac{1}{1+x^{2}}=\sum_{n=0}^{\infty}(-1)^{n}x^{2n}, \qquad R=1,
$$

which is finite for every real $x$ yet has radius one about the origin, because of the poles at $x=\pm i$. This example shows that radius is governed by complex obstructions and not by the appearance of a real formula.

The ratio test in the form used in this course is

$$
R=\lim_{n\to\infty}\left|\frac{C_{n}}{C_{n+1}}\right|,
$$

valid when the limit exists. For a series whose coefficients are eventually zero the radius is infinite, which is the case for polynomial solutions.

### 3.6 Speed techniques that do not cost marks

Three shortcuts save time without weakening the answer, provided the written solution still shows the products.

The first is pole counting. For a rational coefficient written with its denominator factored, the order of the pole at $x_{0}$ is the multiplicity of $x_{0}$ in the denominator minus its multiplicity in the numerator, after cancellation. A point is regular singular exactly when the order for $P$ is at most one and the order for $Q$ is at most two. This decides the verdict instantly, and the limit computation is then written to justify it.

The second is pattern recognition for the common shapes. The following table covers almost every case that appears in a paper.

| Coefficient shape near $x_{0}$ | First test | Second test | Verdict |
| --- | --- | --- | --- |
| $P$ finite, $Q$ finite | passes | passes | ordinary |
| $P$ like $\frac{1}{x-x_{0}}$, $Q$ like $\frac{1}{\left(x-x_{0}\right)^{2}}$ | passes | passes | regular singular |
| $P$ like $\frac{1}{\left(x-x_{0}\right)^{2}}$ | fails | irrelevant | irregular |
| $Q$ like $\frac{1}{\left(x-x_{0}\right)^{3}}$ | passes or fails | fails | irregular |
| $P$ like $\frac{1}{x-x_{0}}$, $Q$ like $\frac{1}{\left(x-x_{0}\right)^{3}}$ | passes | fails | irregular |

The third is substitution after cancellation. Once the product has been simplified and the denominator no longer vanishes at $x_{0}$, the limit equals the value obtained by substituting. No further algebra is needed, and writing the substitution makes the argument complete.

## 4. Representative Worked Examples and Solutions

### 4.1 Problem: classify Legendre's equation completely

Classify all points of $\left(1-x^{2}\right)y''-2xy'+p(p+1)y=0$, find the exponents at the singular points, and state the nature of the series solution about $x_{0}=0$. This is a twelve-mark question.

### 4.2 Solution: model answer with marking points

Step 1 (2 marks). Divide by $1-x^{2}$ and factor, using $1-x^{2}=-(x-1)(x+1)$.

$$
y''+\frac{-2x}{1-x^{2}}y'+\frac{p(p+1)}{1-x^{2}}y=0, \qquad P=\frac{2x}{(x-1)(x+1)}, \quad Q=\frac{-p(p+1)}{(x-1)(x+1)}
$$

Step 2 (1 mark). State the singular points. These are the points where $P$ or $Q$ is not analytic, namely $x=1$ and $x=-1$. Every other real number is ordinary, and $x_{0}=0$ in particular is ordinary.

Step 3 (2 marks). Test $x=1$.

$$
(x-1)P=\frac{2x}{x+1}, \qquad p_{0}=\frac{2}{2}=1
$$

The denominator $x+1$ equals $2$ at $x=1$, so the product is analytic there and the limit is $1$.

Step 4 (2 marks). Complete the second test at $x=1$.

$$
(x-1)^{2}Q=\frac{-p(p+1)(x-1)}{x+1}, \qquad q_{0}=0
$$

The product is a polynomial divided by $x+1$, hence analytic at $x=1$, with value zero. Both tests succeed, so $x=1$ is a regular singular point.

Step 5 (3 marks). Repeat at $x=-1$.

$$
(x+1)P=\frac{2x}{x-1}\to1, \qquad (x+1)^{2}Q=\frac{-p(p+1)(x+1)}{x-1}\to0
$$

The denominators equal $-2$ at $x=-1$, so both products are analytic there. Hence $x=-1$ is a regular singular point.

Step 6 (1 mark). Write the indicial equation at $x=1$, using $p_{0}=1$ and $q_{0}=0$.

$$
r(r-1)+r=r^{2}=0
$$

The exponent is $r=0$, repeated. The same values occur at $x=-1$, so the exponents there are also $0$ and $0$.

Step 7 (1 mark). State the nature of the solution about $x_{0}=0$. Since zero is an ordinary point, there are two independent solutions

$$
y=\sum_{n=0}^{\infty}C_{n}x^{n},
$$

converging at least for $\left|x\right|<1$, because the nearest singular points are at distance one.

Step 8 (check). Verify the conclusion is consistent with a known solution. For $p=1$ the equation is $\left(1-x^{2}\right)y''-2xy'+2y=0$ and $y=x$ satisfies it, since the second-derivative term vanishes and $-2x+2x=0$. A polynomial has infinite radius, which does not contradict the guaranteed radius of at least one.

### 4.3 Problem: one equation, two different singular points

Locate and classify the singular points of $\left(x^{4}-2x^{3}+x^{2}\right)y''+2(x-1)y'+x^{2}y=0$ and state the nature of the solution near each. This is a ten-mark question.

### 4.4 Solution: model answer with marking points

Step 1 (2 marks). Factor the coefficient of the second derivative and normalise.

$$
x^{4}-2x^{3}+x^{2}=x^{2}(x-1)^{2}, \qquad y''+\frac{2}{x^{2}(x-1)}y'+\frac{1}{(x-1)^{2}}y=0
$$

so that $P=\frac{2}{x^{2}(x-1)}$ and $Q=\frac{1}{(x-1)^{2}}$.

Step 2 (1 mark). The singular points are $x=0$ and $x=1$, the only points where these functions are not analytic.

Step 3 (2 marks). Test $x=0$ with the first product.

$$
xP=\frac{2}{x(x-1)}
$$

The denominator vanishes at $x=0$ and the numerator does not, so the product is not analytic at $0$ and has no finite limit. The first test fails.

Step 4 (2 marks). Test $x=0$ with the second product, to show that the failure is not repaired.

$$
x^{2}Q=\frac{x^{2}}{(x-1)^{2}}\to0
$$

This product is analytic at $0$ with value zero, but one failed test is decisive. Hence $x=0$ is an irregular singular point, and no series solution is guaranteed there.

Step 5 (2 marks). Test $x=1$.

$$
(x-1)P=\frac{2}{x^{2}}\to2, \qquad (x-1)^{2}Q=1\to1
$$

Both are analytic at $x=1$, with finite values. Hence $x=1$ is a regular singular point.

Step 6 (1 mark). State the solution forms. Near $x=1$ there is at least one solution

$$
y=(x-1)^{r}\sum_{n=0}^{\infty}C_{n}(x-1)^{n}, \qquad C_{0}\neq0,
$$

on a deleted interval, with $r$ a root of the indicial equation. Near $x=0$ nothing is guaranteed.

Step 7 (check). Verify the indicial equation at $x=1$ reproduces the exponents. With $p_{0}=2$ and $q_{0}=1$,

$$
r(r-1)+2r+1=r^{2}+r+1=0,
$$

so $r=\frac{-1\pm i\sqrt{3}}{2}$, a complex conjugate pair, consistent with oscillatory unbounded behaviour as $x\to1$.

### 4.5 Problem: classification, exponents and coefficients

For $2x^{2}y''-xy'+(x-5)y=0$, classify $x=0$, find the exponents, and compute the first three coefficients of the solution belonging to the larger exponent. This is a twelve-mark question.

### 4.6 Solution: model answer with marking points

Step 1 (2 marks). Normalise.

$$
y''-\frac{1}{2x}y'+\frac{x-5}{2x^{2}}y=0, \qquad P=-\frac{1}{2x}, \quad Q=\frac{x-5}{2x^{2}}
$$

Step 2 (2 marks). Apply the first test.

$$
xP=-\frac{1}{2}\to-\frac{1}{2}
$$

The product is constant, hence analytic, so the first test passes with $p_{0}=-\frac{1}{2}$.

Step 3 (2 marks). Apply the second test.

$$
x^{2}Q=\frac{x-5}{2}\to-\frac{5}{2}
$$

The product is a polynomial, hence analytic, so the second test passes with $q_{0}=-\frac{5}{2}$. The point $x=0$ is a regular singular point.

Step 4 (2 marks). Form and solve the indicial equation.

$$
r(r-1)-\frac{1}{2}r-\frac{5}{2}=0 \;\Longrightarrow\; 2r^{2}-3r-5=0 \;\Longrightarrow\; r=\frac{3\pm7}{4}
$$

The exponents are $r=\frac{5}{2}$ and $r=-1$. Their difference is $\frac{7}{2}$, not an integer, so two independent Frobenius solutions are guaranteed.

Step 5 (2 marks). Derive the recurrence by substituting $y=\sum c_{n}x^{n+r}$ into the original equation and equating the coefficient of $x^{n+r}$ to zero.

$$
\left[2(n+r)(n+r-1)-(n+r)-5\right]c_{n}+c_{n-1}=0
$$

$$
c_{n}=-\frac{c_{n-1}}{2(n+r)(n+r-1)-(n+r)-5}, \qquad n\ge1
$$

Step 6 (1 mark). Evaluate at $r=\frac{5}{2}$ with $c_{0}=1$. For $n=1$,

$$
c_{1}=-\frac{1}{2\cdot\frac{7}{2}\cdot\frac{5}{2}-\frac{7}{2}-5}=-\frac{1}{9},
$$

and for $n=2$,

$$
c_{2}=-\frac{-1/9}{2\cdot\frac{9}{2}\cdot\frac{7}{2}-\frac{9}{2}-5}=\frac{1}{198}.
$$

Step 7 (1 mark). State the answer.

$$
y=x^{5/2}\left(1-\frac{x}{9}+\frac{x^{2}}{198}-\cdots\right)
$$

Step 8 (check). Substitute the computed coefficients back into the recurrence and confirm both denominators: for $n=1$ the denominator is $17.5-3.5-5=9$, and for $n=2$ it is $31.5-4.5-5=22$, which reproduces $c_{1}=-\frac{1}{9}$ and $c_{2}=\frac{1}{198}$. The solution begins with the exponent $\frac{5}{2}$ and the coefficient $1$, as the theorem requires.

### 4.7 Problem: singular points created by a trigonometric coefficient

Locate and classify the singular points of $(\sin x)y''+(\cos x)y'+\frac{1}{x}y=0$. This is a ten-mark question.

### 4.8 Solution: model answer with marking points

Step 1 (2 marks). Normalise.

$$
y''+\cot x\,y'+\frac{1}{x\sin x}y=0, \qquad P=\cot x, \quad Q=\frac{1}{x\sin x}
$$

Step 2 (1 mark). The singular points are the integer multiples of $\pi$, together with $x=0$, which is included in that list. Every other point is ordinary.

Step 3 (2 marks). Test $x=0$ with the first product, using $\frac{\sin x}{x}\to1$.

$$
xP=\frac{x\cos x}{\sin x}=x\cdot\frac{1}{\sin x}\cdot\cos x\to1
$$

Since $\frac{\sin x}{x}$ is analytic at $0$ with value $1$, its reciprocal is analytic there, so the product is analytic and the first test passes.

Step 4 (2 marks). Test $x=0$ with the second product.

$$
x^{2}Q=\frac{x^{2}}{x\sin x}=\frac{x}{\sin x}\to1
$$

This is analytic at $0$ with value $1$, so the second test passes and $x=0$ is a regular singular point.

Step 5 (2 marks). Test $x=\pi$, writing $u=x-\pi$ and using $\cot x=\cot u$ near $\pi$.

$$
(x-\pi)P=u\cot u\to1, \qquad (x-\pi)^{2}Q=\frac{u^{2}}{(\pi+u)\sin(\pi+u)}\to0
$$

Both products are analytic at $u=0$, so $x=\pi$ is a regular singular point. The same computation applies at every multiple of $\pi$.

Step 6 (1 mark). State the conclusion and the exponents. All singular points are regular, so the equation has at least one Frobenius solution near each of them. At $x=0$ the coefficients $p_{0}=1$ and $q_{0}=1$ give

$$
r(r-1)+r+1=r^{2}+1=0,
$$

so the exponents are $r=\pm i$, a complex conjugate pair. At $x=\pi$ the coefficients are $p_{0}=1$ and $q_{0}=0$, giving $r(r-1)+r=r^{2}=0$, so the exponents are $0$ and $0$, a repeated root, and a logarithm must be expected in the second solution there.

## 5. Mathematical Extensions, Limits, and Common Errors

### 5.1 What the marking actually rewards

Three things earn marks in this topic, and they are independent of one another: the algebra of the normalisation, the explicit computation of the two products and their limits, and the accuracy of the concluding sentence about the guaranteed solution. A candidate who classifies correctly but writes no solution sentence loses the last block of marks; a candidate who writes a beautiful solution sentence after an incorrect classification loses everything downstream, because the sentence depends on the verdict.

The trap table below collects the errors that appear most often in scripts. Read it as a checklist to run over your own answer before moving on, not as a list of exotic possibilities; every entry has been seen repeatedly.

### 5.2 The trap table

| Trap | How it typically appears | Why it is wrong | Correct move |
| --- | --- | --- | --- |
| Confusing singular with regular singular | "the equation has a regular singular point at $x=1$" without any test | every point is ordinary or singular; regular and irregular subdivide the singular case only | first prove the point is singular, then apply both tests |
| Using $x$ instead of $x-x_{0}$ | multiplying by $x$ when the point is $x_{0}=2$ | the products must measure distance from the singular point | use $\left(x-x_{0}\right)P$ and $\left(x-x_{0}\right)^{2}Q$ |
| Using the same power twice | computing $\left(x-x_{0}\right)P$ and $\left(x-x_{0}\right)Q$ | $Q$ needs two factors because its term carries one more derivative | one factor for $P$, two for $Q$ |
| Testing only $P$ | stopping after $p_{0}$ is finite | regularity requires both products to be analytic | evaluate both limits at every singular point |
| Accepting an infinite limit | writing "$p_{0}=\infty$, so the point is regular" | an infinite limit means the product is not analytic | verdict is irregular, and say which test failed |
| Classifying before locating | applying the tests at $x=0$ of an equation with no singular points | both tests pass automatically at ordinary points | list the singular points first |
| Ignoring cancellation | declaring $x=2$ singular because $a_{0}$ vanishes there | a common factor may cancel and remove the singularity | normalise and simplify before listing points |
| Claiming two series at a regular singular point | "the two solutions are $\sum C_{n}x^{n+r}$" | only one Frobenius solution is guaranteed | one solution, plus a possible second with a logarithm |
| Claiming no solution at an irregular point | "the equation has no solution near $x=0$" | the theorem promises nothing, which is not a denial | say that no such solution is assured |
| Writing the radius as an equality | "$R$ equals the distance to the nearest singular point" | the theorem only gives a lower bound | write "at least the distance to the nearest singular point" |
| Using a non-deleted interval | "valid for $\lvert x-x_{0}\rvert<R$" at a regular singular point | the exponent may make the solution infinite at the centre | write $0<\lvert x-x_{0}\rvert<R$ |
| Rejecting complex exponents | "no real exponents, so the method fails" | complex roots are permitted and give oscillatory solutions | accept the pair and interpret it |
| Arithmetic on the indicial quadratic | losing the sign when $q_{0}$ is negative | the quadratic is $r(r-1)+p_{0}r+q_{0}=0$, signs included | substitute the computed limits carefully |
| Dividing through at a zero of $a_{0}$ | normalising across $x=1$ without comment | division is invalid where $a_{0}$ vanishes | restrict to an interval avoiding the zeros |

### 5.3 The two traps that cost the most

The first is the conflation of "singular" with "regular singular". The words sound alike and the tests look like a formality, so a script often reads: "$x=0$ is a singular point, therefore it is a regular singular point". That inference is invalid. Singularity and regularity are different assertions, established by different computations: singularity by the failure of analyticity, regularity by the success of two products. A useful discipline is to write the verdict in two stages, for example "$P$ is not analytic at $x=0$, so $x=0$ is singular; and since $xP\to1$ and $x^{2}Q\to-1$ are finite, it is regular". The two stages make the logic visible, and an examiner awards both parts.

The second is the misapplication of the tests. Three variants dominate. Multiplying by the wrong power is the most common: using $x^{2}P$ and $x^{2}Q$ together, which artificially rescues a genuinely irregular point and produces a false verdict of regular. Testing only the first product is the next: the equation of Section 4.3 passes the first test and fails the second, and stopping early reverses the answer. Applying the tests at ordinary points is the third: it produces a page of correct limits followed by a wrong set of labels, because the ordinary points have been absorbed into the singular class.

The remedy in all three cases is the same. Write the two products as a labelled pair, simplify each, evaluate each, and only then write the verdict. The layout does the checking for you.

### 5.4 Revision checklist

Work through the list until every item can be done without notes.

- State the four definitions — normalised form, ordinary point, singular point, regular singular point — word for word.
- Explain in one sentence why the tests use one factor for $P$ and two for $Q$.
- Normalise an equation given with a non-unit coefficient on $y''$, and state where the division is invalid.
- List the singular points of a rational-coefficient equation after cancellation, not before.
- Apply both tests at a singular point with the algebra written out.
- Give the verdict with the reason, naming the failing test when the point is irregular.
- Derive the indicial equation in three lines from the Frobenius substitution.
- Solve an indicial quadratic with negative and fractional coefficients.
- Classify the singular points of Legendre's, Bessel's and the hypergeometric equations from memory, and justify each.
- State the radius guaranteed about an ordinary point, and compute a radius by the ratio test.
- Write the three clauses of the existence theorem with the words "two", "at least one" and "not assured".
- Explain why an irregular point does not mean that no solution exists.
- Recognise the four indicial cases and say what each implies about logarithms.
- Quote the two standard expansions $\frac{1}{1-x}$ and $\frac{1}{1+x^{2}}$ with their radii.
- Explain why $\frac{1}{1+x^{2}}$ has radius one although it has no real singularity.

### 5.5 Time strategy for the examination

A classification question of about ten marks should take roughly eighteen minutes: two minutes to normalise and list the singular points, three minutes per singular point for the two products, one minute for the indicial equation if asked, and the remainder for the concluding sentence and the check. A twelve-mark question with coefficients takes about twenty-two minutes.

The order of work should be rigid. Normalise first, because every later step depends on $P$ and $Q$. List the singular points second, because the tests are meaningless without them. Test each point third, writing the two products before evaluating anything. Write the conclusion fourth, using the exact wording of the theorem. Check fifth, by substituting the computed exponents back into the quadratic or by testing a known solution.

Two pieces of advice save time under pressure. If the algebra of a product looks heavy, factor the denominator first; the cancellation usually collapses the expression to something that can be evaluated by substitution. If the classification is unclear, fall back on pole counting: read the order of the pole of $P$ and of $Q$ at the point, and the verdict follows immediately, after which the limits can be written to justify it. Never leave a singular point unclassified, because a partial list loses more marks than an imperfect verdict on a complete list.

### 5.6 Extensions worth knowing for longer questions

Three extensions appear in harder papers and cost little to prepare.

The point at infinity is handled by the substitution $x=\frac{1}{t}$, under which $\frac{dy}{dx}=-t^{2}\frac{dY}{dt}$ and $\frac{d^{2}y}{dx^{2}}=t^{4}\frac{d^{2}Y}{dt^{2}}+2t^{3}\frac{dY}{dt}$. Applying this to Legendre's equation produces an equation whose coefficients at $t=0$ pass both tests, so infinity is a regular singular point, and Legendre's equation is Fuchsian: all its singular points, infinity included, are regular.

Equations all of whose singular points are regular are called Fuchsian, and the hypergeometric equation is the model case with regular singular points at $0$, $1$ and infinity. Recognising this class allows a quick sanity check: if a computation produces an irregular point for one of these classical equations, the computation is wrong.

The behaviour of solutions near a regular singular point is governed by the real parts of the exponents. A negative real part means the solution grows without bound as $x\to x_{0}$, a positive real part means it tends to zero, and a zero real part means it remains of moderate size. Complex exponents add oscillation in $\ln\left(x-x_{0}\right)$. This is the quantitative form of the statement that solutions at a regular singular point need not be defined at the point.

### 5.7 The subject in one paragraph

One normalises, one locates, one tests, one concludes. Normalising divides by the coefficient of the second derivative and produces the two functions $P$ and $Q$ that the whole theory examines. Locating lists the points where those functions fail to be analytic, after every cancellation has been performed. Testing multiplies by one factor of the distance for $P$ and by two for $Q$, simplifies, and evaluates; if both results are finite the point is regular, and if either is infinite or fails to exist the point is irregular. Concluding quotes the matching clause of the existence theorem: two series at an ordinary point, at least one series with an exponent at a regular singular point, and no assurance at an irregular one. Every mark in the topic sits somewhere in that sentence, and every error catalogued above is a departure from it.

