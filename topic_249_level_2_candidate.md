## 1. What a generating function represents

A sequence is an ordered list of numbers, such as $a_0,a_1,a_2,\ldots$. A generating function stores the terms of that sequence as the coefficients of powers of a variable. Instead of working with the entries separately, we study one power series whose coefficient at $s^k$ is $a_k$.

For example, the sequence $1,1,1,\ldots$ is represented by $1+s+s^2+s^3+\cdots$. The variable $s$ is a bookkeeping device: its exponent records the position in the sequence. It need not represent time, probability, or a physical quantity unless a later application assigns it that meaning.

Generating functions are useful because they turn sequence operations into algebra. A recurrence relation can become an equation in a function; shifts in a sequence become factors of $s$; and coefficients can be recovered by differentiation or expansion. The function is therefore a compact representation of the sequence, not a replacement for checking what its coefficients mean.

## 2. Definition and coefficient extraction

Let $\{a_k\}_{k\ge0}$ be a sequence of real numbers. Its ordinary generating function (g.f.) is the power series

$$
A(s)=a_0+a_1s+a_2s^2+a_3s^3+\cdots
=\sum_{k=0}^{\infty}a_ks^k.
$$

If this series converges for values of $s$ in an interval about zero, it defines a function there. The interval of convergence is part of the analytic description. In formal power-series work, the same coefficient algebra can be used without first evaluating the series numerically.

The coefficients can be recovered from derivatives at zero. Differentiating $k$ times gives a constant term $k!a_k$ plus terms containing positive powers of $s$. Setting $s=0$ removes those later terms, so

$$
a_k=\frac{A^{(k)}(0)}{k!}
=\left.\frac{1}{k!}\frac{d^k A(s)}{ds^k}\right|_{s=0}.
$$

For example,

$$
A'(s)=a_1+2a_2s+3a_3s^2+\cdots,
$$

so $A'(0)=a_1$. Differentiating again,

$$
A''(s)=2a_2+6a_3s+12a_4s^2+\cdots,
$$

hence $A''(0)=2a_2$ and $a_2=A''(0)/2!$. In general, $A^{(k)}(0)=k!a_k$. The factorial is essential; omitting it gives the wrong coefficient for every $k\ge2$.

## 3. Standard sequence examples

### 3.1 Constant sequence

If $a_k=1$ for every $k\ge0$, then

$$
A(s)=1+s+s^2+s^3+\cdots.
$$

This is the geometric series with first term 1 and common ratio $s$. For $|s|<1$,

$$
A(s)=\frac{1}{1-s}.
$$

The restriction matters: the infinite geometric series does not converge at $s=1$ or outside the unit interval on the real line. The rational expression is the sum of the series only where that series converges.

### 3.2 A sequence shifted by three zero terms

For the sequence $0,0,0,1,1,1,\ldots$, the first nonzero coefficient is $a_3=1$. Therefore

$$
A(s)=s^3+s^4+s^5+\cdots
=s^3(1+s+s^2+\cdots)
=\frac{s^3}{1-s},\qquad |s|<1.
$$

The factor $s^3$ records the three initial zero coefficients. It shifts the sequence’s nonzero terms to indices 3 and above; it does not change the geometric-series factor.

### 3.3 Reciprocal-factorial sequence

For $a_k=1/k!$,

$$
A(s)=1+s+\frac{s^2}{2!}+\frac{s^3}{3!}+\cdots=e^s.
$$

This is the Maclaurin series for the exponential function. Unlike the preceding geometric examples, this power series converges for every real or complex value of $s$.

### 3.4 Binomial-coefficient sequence

For a fixed nonnegative integer $n$, define $a_k=\binom{n}{k}$ for $0\le k\le n$ and $a_k=0$ for $k>n$. The generating function is finite:

$$
A(s)=\sum_{k=0}^{n}\binom{n}{k}s^k=(1+s)^n,
$$

by the binomial theorem. For example, when $n=3$, $A(s)=1+3s+3s^2+s^3$. Coefficient extraction checks the result: $A''(0)/2!=6/2=3=\binom{3}{2}$.

These examples show different patterns: a constant sequence produces a geometric series; initial zeros introduce a power of $s$; factorial denominators produce the exponential series; and binomial coefficients produce a polynomial.

### 3.5 Using differentiation to generate a new sequence

The geometric series also gives a useful derived example. For $|s|<1$,

$$
1+s+s^2+s^3+\cdots=\frac{1}{1-s}.
$$

Differentiate both sides term by term within the interval of convergence:

$$
1+2s+3s^2+4s^3+\cdots=\frac{1}{(1-s)^2}.
$$

Multiplying by $s$ gives

$$
s+2s^2+3s^3+4s^4+\cdots=\frac{s}{(1-s)^2}.
$$

Thus the sequence $0,1,2,3,\ldots$ has generating function $s/(1-s)^2$. This is a consequence of the series already given in the lesson, not a separate memorized formula. It illustrates how a generating function can transform one known sequence into a related one.

The same method gives a coefficient check. For the shifted sequence $0,0,0,1,1,\ldots$, its function is $s^3/(1-s)$. The coefficient $a_3$ can be recovered as

$$
a_3=\frac{A^{(3)}(0)}{3!}=1.
$$

Differentiation therefore works in both directions: it can help build a series, and derivatives at zero can retrieve its coefficients.

## 4. Finding a generating function from a recurrence

A generating function can convert a recurrence into an algebraic equation. The source example has

$$
a_n+a_{n-1}-16a_{n-2}+20a_{n-3}=0,\qquad n\ge3,
$$

with initial values $a_0=0$, $a_1=1$, and $a_2=-1$. Let

$$
A(s)=\sum_{n=0}^{\infty}a_ns^n.
$$

Multiply the recurrence by $s^n$ and sum over $n\ge3$. Treat each shifted sum carefully:

$$
\sum_{n=3}^{\infty}a_ns^n=A(s)-a_0-a_1s-a_2s^2=A(s)-s+s^2,
$$

$$
\sum_{n=3}^{\infty}a_{n-1}s^n=s\sum_{m=2}^{\infty}a_ms^m=s(A(s)-s),
$$

$$
\sum_{n=3}^{\infty}a_{n-2}s^n=s^2\sum_{m=1}^{\infty}a_ms^m=s^2A(s),
$$

and

$$
\sum_{n=3}^{\infty}a_{n-3}s^n=s^3A(s).
$$

Substitute these four expressions into the summed recurrence:

$$
[A(s)-s+s^2]+s[A(s)-s]-16s^2A(s)+20s^3A(s)=0.
$$

The initial-value terms $+s^2$ and $-s^2$ cancel. Collecting the terms containing $A(s)$ gives

$$
A(s)(1+s-16s^2+20s^3)=s,
$$

so the generating function is

$$
A(s)=\frac{s}{1+s-16s^2+20s^3}.
$$

This is the central recurrence technique: multiply by $s^n$, sum over the recurrence’s valid indices, replace shifted sums by $A(s)$ minus the initial terms, then solve for $A(s)$. The initial conditions determine the numerator; losing one of them changes the function.

A coefficient check confirms the setup. The first terms are $a_0=0$, $a_1=1$, $a_2=-1$. The recurrence gives $a_3=17$, $a_4=-53$, and $a_5=345$. Expanding the rational function about zero begins

$$
A(s)=s-s^2+17s^3-53s^4+345s^5+\cdots,
$$

which matches the recurrence. This check is valuable because an indexing or sign error in the shifted sums can still produce a plausible-looking rational function.

The same relation can be read in reverse. Multiplying the proposed generating function by its denominator gives

$$
(1+s-16s^2+20s^3)A(s)=s.
$$

Comparing coefficients of equal powers of $s$ reproduces the initial values and the recurrence. For example, the coefficient of $s^2$ is $a_2+a_1-16a_0=0$, which is $-1+1-0=0$; the coefficient of $s^3$ is $a_3+a_2-16a_1+20a_0=0$, which is $17-1-16=0$. This coefficient comparison is an independent way to verify the algebraic answer.

## 5. How to use and interpret the function

A generating function can be used in either direction. Starting with a sequence, sum its terms with powers of $s$ to obtain $A(s)$. Starting with a function, expand it as a power series or differentiate at zero to recover a coefficient. When the generating function is rational, algebraic manipulation may make coefficient patterns or recurrence relations easier to identify.

Several operations follow directly from the definition. If two sequences have generating functions $A(s)$ and $B(s)$, then the termwise sum of their sequences has generating function $A(s)+B(s)$. Multiplying every coefficient by a constant $c$ gives $cA(s)$. If a sequence is shifted right by $m$ places by inserting $m$ zeros before its first term, its generating function is multiplied by $s^m$. For example, shifting $1,1,1,\ldots$ right by three places gives $s^3/(1-s)$. These simple operations are useful for reading sequence changes without rewriting every coefficient.

The convergence range must be respected when the series is treated as an ordinary analytic sum. For example, $1/(1-s)$ equals $1+s+s^2+\cdots$ only for $|s|<1$. The same rational expression may be algebraically defined at other points where its denominator is nonzero, but there it is not the sum of that original infinite series. Keep the distinction between the formal power series and its analytic value clear.

For a probability sequence, the coefficients may be probabilities and the generating function becomes a probability generating function. That is a special application with additional properties, such as coefficients that are nonnegative and sum to one. A general generating function can have arbitrary real coefficients and should not automatically be interpreted as a probability model.

## 6. Exam method and common errors

For a direct sequence problem:

1. Write the coefficient indexing clearly, beginning with $a_0$.
2. Form $A(s)=\sum_{k\ge0}a_ks^k$ and identify any initial zero shift.
3. Recognize a geometric, exponential, or binomial series only after checking its coefficients.
4. State the convergence interval when using an infinite series formula.
5. If extracting a coefficient by derivatives, evaluate the $k$th derivative at zero and divide by $k!$.

For a recurrence problem:

1. State the recurrence’s starting index and all initial values.
2. Multiply by $s^n$ and sum from that starting index, not automatically from zero.
3. Rewrite each shifted sum separately, displaying the initial terms removed.
4. Collect coefficients of $A(s)$ and solve the resulting equation.
5. Expand enough terms to check that the initial values and recurrence are reproduced.

Common errors include treating $s$ as a probability; omitting $a_0$ or another initial term; shifting the wrong index in sums such as $a_{n-2}$; forgetting the factorial in coefficient extraction; using a geometric-series formula outside its convergence range; or calling every generating function a probability generating function. A correct answer explains how the coefficients correspond to the original sequence.