## 1. Scope, notation, and support

Let $X$ be a non-negative integer-valued random variable with probability mass function $p_k=P(X=k)$, $k=0,1,2,\ldots$, satisfying $p_k\ge0$ and $\sum_{k=0}^{\infty}p_k=1$. Its probability generating function (p.g.f.) is

$$
P(s)=\sum_{k=0}^{\infty}p_ks^k=E[s^X].
$$

This lesson studies two cumulative sequences and their ordinary generating functions. Define the lower cumulative probability

$$
r_k=P(X\le k)=\sum_{j=0}^{k}p_j,
$$

and the strict upper tail

$$
q_k=P(X>k)=\sum_{j=k+1}^{\infty}p_j.
$$

Their generating functions are

$$
R(s)=\sum_{k=0}^{\infty}r_ks^k,
\qquad Q(s)=\sum_{k=0}^{\infty}q_ks^k.
$$

The tail sequences are not generally probability mass functions. In particular, their coefficients need not sum to one, so $R$ and $Q$ should be called generating functions, not p.g.f.s. Because $r_k+q_k=1$, the two sequences are complements at the same index.

This complement identity follows from the partition $\{X\le k\}\cup\{X>k\}$, whose events are disjoint and cover every possible value. It is an index-matched statement: $r_k+q_k=1$, not $r_k+q_{k-1}=1$. The p.g.f. $P(s)$ stores point probabilities; $R(s)$ and $Q(s)$ store cumulative probabilities. The difference in what their coefficients represent is why they have different numerators despite sharing the denominator $1-s$.

## 2. Lower cumulative probabilities: difference derivation

The lower cumulative sequence starts at $r_0=p_0$ and adds one probability at each step:

$$
r_k-r_{k-1}=p_k,\qquad k\ge1.
$$

Multiply by $s^k$ and sum for $k\ge1$:

$$
\sum_{k=1}^{\infty}p_ks^k
=\sum_{k=1}^{\infty}r_ks^k-\sum_{k=1}^{\infty}r_{k-1}s^k.
$$

The left side is $P(s)-p_0$. The first sum on the right is $R(s)-r_0$; the second is $sR(s)$. Since $r_0=p_0$,

$$
P(s)-p_0=R(s)-p_0-sR(s),
$$

so

$$
R(s)=\frac{P(s)}{1-s},\qquad |s|<1.
$$

The initial term is important. It cancels because the lower cumulative sequence begins at $r_0=p_0$; if the sum is shifted or its initial term omitted, the resulting numerator will be wrong.

The lower-tail recurrence is not assumed to hold at $k=0$ with an undefined $r_{-1}$. Starting at $k=1$ gives $P(s)-p_0$ on the left. On the right, removing the initial coefficient from $R(s)$ gives $R(s)-r_0$, while shifting $r_{k-1}$ forward by one power gives $sR(s)$. Substituting $r_0=p_0$ makes the two boundary terms cancel. This is the complete reason the result has numerator $P(s)$ rather than $P(s)-p_0$ or $P(s)+p_0$.

## 3. Lower cumulative probabilities: direct summation

Substitute $r_k=\sum_{j=0}^{k}p_j$ into $R(s)$:

$$
R(s)=\sum_{k=0}^{\infty}\sum_{j=0}^{k}p_js^k.
$$

Reverse the summation order. For fixed $j$, the coefficient $p_j$ appears for every $k\ge j$:

$$
R(s)=\sum_{j=0}^{\infty}p_j\sum_{k=j}^{\infty}s^k.
$$

For $|s|<1$, the inner geometric series is $s^j/(1-s)$. Therefore

$$
R(s)=\sum_{j=0}^{\infty}p_j\frac{s^j}{1-s}
=\frac{P(s)}{1-s}.
$$

This derivation makes the accumulation structure explicit: every exact probability remains included in all lower-tail values after its index.

With the finite example in Section 5, reversing the sums gives

$$
R(s)=\frac12(1+s+s^2+\cdots)
+\frac13(s+s^2+s^3+\cdots)
+\frac16(s^2+s^3+s^4+\cdots).
$$

Collecting coefficients produces $1/2$, then $1/2+1/3=5/6$, then $1/2+1/3+1/6=1$ for every later power. The series therefore agrees term by term with the cumulative sequence. This coefficient-level interpretation is often the clearest way to explain the lower-tail formula.

## 4. Strict upper tail: two derivations

For the strict upper tail, $q_0=1-p_0$ and, for $k\ge1$,

$$
q_{k-1}-q_k=p_k.
$$

Multiply by $s^k$ and sum over $k\ge1$:

$$
P(s)-p_0=sQ(s)-[Q(s)-q_0]
=(s-1)Q(s)+q_0.
$$

Using $p_0+q_0=1$ and solving gives

$$
Q(s)=\frac{1-P(s)}{1-s},\qquad |s|<1.
$$

A direct-summation proof begins with $q_k=\sum_{j=k+1}^{\infty}p_j$:

$$
Q(s)=\sum_{k=0}^{\infty}\sum_{j=k+1}^{\infty}p_js^k
=\sum_{j=1}^{\infty}p_j\sum_{k=0}^{j-1}s^k.
$$

The inner finite geometric sum is $(1-s^j)/(1-s)$. Hence

$$
Q(s)=\frac{\sum_{j=1}^{\infty}p_j-\sum_{j=1}^{\infty}p_js^j}{1-s}
=\frac{(1-p_0)-(P(s)-p_0)}{1-s}
=\frac{1-P(s)}{1-s}.
$$

Both methods give the same result. The recurrence method emphasizes the boundary probability $q_0$; the direct method emphasizes how often each $p_j$ appears among the strict tails.

For a finite distribution with support ending at $m$, the upper-tail sum can also be written without an infinite inner series:

$$
Q(s)=p_1+p_2(1+s)+p_3(1+s+s^2)+\cdots
+p_m(1+s+\cdots+s^{m-1}).
$$

The term $p_0$ does not appear because $X=0$ is never greater than a non-negative cutoff. The constant coefficient is $p_1+\cdots+p_m=1-p_0=q_0$; the coefficient of $s$ is $p_2+\cdots+p_m=q_1$. These coefficient checks recover the strict upper-tail definition directly.

## 5. Worked finite-support example and checks

Let $P(X=0)=1/2$, $P(X=1)=1/3$, and $P(X=2)=1/6$. The probabilities sum to one, and

$$
P(s)=\frac12+\frac13s+\frac16s^2.
$$

The lower cumulative sequence is $r_0=1/2$, $r_1=5/6$, and $r_k=1$ for $k\ge2$. The upper sequence is $q_0=1/2$, $q_1=1/6$, and $q_k=0$ for $k\ge2$. Thus

$$
R(s)=\frac12+\frac56s+s^2+s^3+\cdots
=\frac12+\frac56s+\frac{s^2}{1-s},
$$

$$
Q(s)=\frac12+\frac16s.
$$

The formula check is

$$
\frac{P(s)}{1-s}=R(s),
\qquad
\frac{1-P(s)}{1-s}=Q(s).
$$

At index zero, the constant coefficients are $r_0=p_0=1/2$ and $q_0=1-p_0=1/2$. At index one, $r_1+q_1=5/6+1/6=1$. These boundary checks expose a strict-versus-inclusive indexing error immediately.

Expanding the lower-tail quotient confirms each coefficient:

$$
\frac{P(s)}{1-s}
=\left(\frac12+\frac13s+\frac16s^2\right)(1+s+s^2+\cdots)
=\frac12+\frac56s+s^2+s^3+\cdots.
$$

For the strict upper tail,

$$
\frac{1-P(s)}{1-s}
=\frac{\frac12-\frac13s-\frac16s^2}{1-s}
=\frac12+\frac16s.
$$

The upper series terminates because $Q_k=0$ once $k$ is at least the largest support point. The lower series does not terminate: after the support is exhausted, every lower cumulative probability is 1, so its generating function contains the infinite tail $s^m/(1-s)$.

### Infinite-support example: geometric distribution

The approved module also gives the geometric p.g.f. Let $X$ count failures before the first success, with success probability $p$ and $q=1-p$. Then $P(X=k)=pq^k$ for $k\ge0$, and

$$
P(s)=\sum_{k=0}^{\infty}pq^ks^k=\frac{p}{1-qs}.
$$

The event $X>k$ requires at least $k+1$ failures, so $q_k=q^{k+1}$. Its generating function is

$$
Q(s)=\sum_{k=0}^{\infty}q^{k+1}s^k=\frac{q}{1-qs}.
$$

The general formula gives the same answer:

$$
\frac{1-P(s)}{1-s}
=\frac{1-p/(1-qs)}{1-s}
=\frac{q}{1-qs}.
$$

Similarly, $r_k=1-q^{k+1}$ and $R(s)=P(s)/(1-s)$. Unlike the finite-support example, the upper-tail coefficients never become zero, but they decrease geometrically when $0<q<1$. This example confirms that the formulas apply to an infinite sequence of nonzero probabilities as well as a finite table.

## 6. Convergence, conventions, and exam checks

For $|s|<1$, the geometric-series manipulations converge absolutely, allowing the summation order to be exchanged in the direct derivations. The p.g.f. itself is defined at least for $|s|\le1$ for a probability distribution, but the tail-generating-function formulas are stated on $|s|<1$ because of the denominator $1-s$ and the series derivation.

Some texts use “upper tail” for $P(X\ge k)$. With the convention here, $q_k=P(X>k)$, so

$$
P(X\ge k)=q_{k-1},\qquad k\ge1.
$$

There is a compact identity that combines both tails. Since $r_k+q_k=1$ for every $k$,

$$
R(s)+Q(s)=\sum_{k=0}^{\infty}(r_k+q_k)s^k
=\sum_{k=0}^{\infty}s^k=\frac{1}{1-s},\qquad |s|<1.
$$

The two closed forms give the same check:

$$
\frac{P(s)}{1-s}+\frac{1-P(s)}{1-s}=\frac{1}{1-s}.
$$

If the numerators have been swapped or a tail is shifted by one index, this identity will generally fail. Along with the constant-coefficient checks, it is a quick audit for the completed derivation.

Coefficient by coefficient, the identity says that each index contributes exactly one unit across the two complementary events. It does not say that either sequence alone sums to one; the sum $\sum_k r_k$ or $\sum_k q_k$ may be infinite. The convergent power-series identity is valid for $|s|<1$ and is consistent with the probabilistic partition at every fixed cutoff.
If a generating function is defined with powers $s^k$ starting at $k=1$, it differs by a factor of $s$ from a series reindexed to begin at zero. State both the event and the series index before applying a formula.

For instance, define $H(s)=\sum_{k=1}^{\infty}P(X\ge k)s^{k-1}$. Since $P(X\ge k)=q_{k-1}$, the coefficient sequence is $q_0,q_1,q_2,\ldots$, so $H(s)=Q(s)$. If instead the same probabilities are paired with $s^k$, the series is $sQ(s)$. A correct tail probability formula can therefore appear to differ by one factor of $s$ solely because the indexing convention changed.

For an exam proof, define $p_k$, the support, the chosen cumulative sequence, and its generating function; write the one-step recurrence including its initial value; multiply by powers of $s$; sum from the correct lower index; simplify boundary terms; and check the constant coefficient. The final formulas are $R(s)=P(s)/(1-s)$ for $P(X\le k)$ and $Q(s)=(1-P(s))/(1-s)$ for $P(X>k)$. Frequent errors are swapping these numerators, omitting $p_0$ or $q_0$, claiming a tail sequence is itself a p.g.f., and using $P(X\ge k)$ without adjusting the index.

Do not substitute $s=1$ directly into either quotient: the denominator vanishes. Although $P(1)=1$ for a probability generating function, the limiting value of a tail generating function depends on the distribution and may be infinite. The identities in this lesson are established for $|s|<1$. If an endpoint limit is requested, analyze it separately rather than canceling $0/0$ informally.