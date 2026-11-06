## 1. Definitions and index convention

Let $X$ be supported on the non-negative integers, with $p_k=P(X=k)$ and p.g.f.

$$
P(s)=\sum_{k=0}^{\infty}p_ks^k.
$$

Use the explicit conventions

$$
F_k=P(X\le k)=\sum_{j=0}^{k}p_j,
\qquad
Q_k=P(X>k)=\sum_{j=k+1}^{\infty}p_j,
\qquad k\ge0.
$$

Thus $F_k+Q_k=1$. The upper tail is strict; it excludes the cutoff. If an exam defines an upper tail by $P(X\ge k)$, shift the sequence: $P(X\ge k)=Q_{k-1}$ for $k\ge1$. Write the event before the series or formula. This one line prevents the most common index error in this topic.

Define the generating functions

$$
R(s)=\sum_{k=0}^{\infty}F_ks^k,
\qquad
Q(s)=\sum_{k=0}^{\infty}Q_ks^k.
$$

These are ordinary generating functions of cumulative sequences, not generally p.g.f.s: their coefficients need not be nonnegative and sum to one.

Because $F_k+Q_k=1$ at every index, the generating functions also satisfy

$$
R(s)+Q(s)=\sum_{k=0}^{\infty}(F_k+Q_k)s^k
=\sum_{k=0}^{\infty}s^k=\frac{1}{1-s},\qquad |s|<1.
$$

The closed forms produce the same identity when their numerators are added. It is an effective global check, while the constant coefficients check the two boundary events separately.

## 2. Formula sheet and boundary values

The required identities for $|s|<1$ are

$$
R(s)=\frac{P(s)}{1-s},
\qquad
Q(s)=\frac{1-P(s)}{1-s}.
$$

Do not interchange the numerators. The lower cumulative sequence starts at $F_0=p_0$; the strict upper sequence starts at $Q_0=1-p_0$. Consequently the constant coefficients of the two generating functions must be $p_0$ and $1-p_0$ respectively.

The one-step recurrences are

$$
F_0=p_0,\qquad F_k-F_{k-1}=p_k\quad(k\ge1),
$$

$$
Q_0=1-p_0,\qquad Q_{k-1}-Q_k=p_k\quad(k\ge1).
$$

The sign in the upper-tail recurrence is reversed because increasing the threshold from $k-1$ to $k$ removes the probability mass at $k$ from the strict tail.

## 3. Difference-equation proof

### Lower cumulative sequence

Multiply $F_k-F_{k-1}=p_k$ by $s^k$ and sum for $k\ge1$:

$$
\sum_{k=1}^{\infty}p_ks^k
=\sum_{k=1}^{\infty}F_ks^k
-\sum_{k=1}^{\infty}F_{k-1}s^k.
$$

The left side is $P(s)-p_0$. The right side is $[R(s)-F_0]-sR(s)=[R(s)-p_0]-sR(s)$. Therefore

$$
P(s)-p_0=R(s)-p_0-sR(s),
$$

so $P(s)=(1-s)R(s)$ and

$$
R(s)=\frac{P(s)}{1-s}.
$$

The series shifts can be audited without relying on shorthand:

$$
\sum_{k=1}^{\infty}F_ks^k=R(s)-F_0=R(s)-p_0,
\qquad
\sum_{k=1}^{\infty}F_{k-1}s^k=sR(s).
$$

Thus $P(s)-p_0=[R(s)-p_0]-sR(s)$, and the two boundary terms $p_0$ cancel. The coefficient of $s^0$ in the result is then $p_0$, as it must be. This is the lower-tail proof in its safest exam form: state the starting index, remove the constant term, and only then shift the second sum.

### Strict upper tail

Multiply $Q_{k-1}-Q_k=p_k$ by $s^k$ and sum for $k\ge1$:

$$
P(s)-p_0=sQ(s)-[Q(s)-Q_0]
=(s-1)Q(s)+Q_0.
$$

Substitute $Q_0=1-p_0$:

$$
P(s)-p_0=(s-1)Q(s)+1-p_0.
$$

Hence $P(s)-1=(s-1)Q(s)$, and

$$
Q(s)=\frac{1-P(s)}{1-s}.
$$

The boundary term is decisive. If $Q_0$ is incorrectly set to $p_0$, the numerator will be wrong even if the remaining summation is done correctly.

The upper-tail boundary can be checked in event notation: $Q_0=P(X>0)=1-P(X=0)=1-p_0$. With this value, the summed difference becomes

$$
P(s)-p_0=sQ(s)-Q(s)+Q_0
=(s-1)Q(s)+1-p_0.
$$

After canceling $p_0$, $P(s)-1=(s-1)Q(s)$. Dividing numerator and denominator by $-1$ gives $Q(s)=(1-P(s))/(1-s)$. The sign changes together in the numerator and denominator; changing only one sign is an algebra error.

## 4. Direct-summation proof and convergence

For the lower cumulative sequence, substitute $F_k=\sum_{j=0}^{k}p_j$ and reverse the order of summation:

$$
R(s)=\sum_{k=0}^{\infty}\sum_{j=0}^{k}p_js^k
=\sum_{j=0}^{\infty}p_j\sum_{k=j}^{\infty}s^k.
$$

For $|s|<1$, $\sum_{k=j}^{\infty}s^k=s^j/(1-s)$. Thus

$$
R(s)=\frac{1}{1-s}\sum_{j=0}^{\infty}p_js^j
=\frac{P(s)}{1-s}.
$$

For the strict upper tail, each $p_j$ contributes to $Q_0$ through $Q_{j-1}$:

$$
Q(s)=\sum_{j=1}^{\infty}p_j\sum_{k=0}^{j-1}s^k.
$$

The inner finite sum is $(1-s^j)/(1-s)$, so

$$
Q(s)=\frac{\sum_{j=1}^{\infty}p_j-\sum_{j=1}^{\infty}p_js^j}{1-s}
=\frac{(1-p_0)-(P(s)-p_0)}{1-s}
=\frac{1-P(s)}{1-s}.
$$

The direct-summation proof makes the coefficient counts visible; the difference-equation proof is usually shorter under exam time. The geometric series and rearrangement are justified for $|s|<1$. State this range when using these analytic series identities.

For the lower tail, the same count can be expanded as

$$
R(s)=p_0(1+s+s^2+\cdots)
+p_1(s+s^2+s^3+\cdots)
+p_2(s^2+s^3+s^4+\cdots)+\cdots.
$$

Collecting the coefficient of $s^k$ gives exactly $p_0+p_1+\cdots+p_k=F_k$. For the upper tail,

$$
Q(s)=p_1+p_2(1+s)+p_3(1+s+s^2)+\cdots,
$$

and the coefficient of $s^k$ is $p_{k+1}+p_{k+2}+\cdots=Q_k$. This coefficient-counting view explains both formulas independently of the recurrence method.

## 5. Worked coefficient check

Take $p_0=1/2$, $p_1=1/3$, $p_2=1/6$, with all later probabilities zero. Then

$$
P(s)=\frac12+\frac13s+\frac16s^2.
$$

The lower cumulative probabilities are $F_0=1/2$, $F_1=5/6$, and $F_k=1$ for $k\ge2$. Therefore

$$
R(s)=\frac12+\frac56s+s^2+s^3+\cdots
=\frac12+\frac56s+\frac{s^2}{1-s}.
$$

The strict upper probabilities are $Q_0=1/2$, $Q_1=1/6$, and $Q_k=0$ for $k\ge2$, hence $Q(s)=1/2+s/6$. Substituting into the identities gives

$$
\frac{P(s)}{1-s}=R(s),
\qquad
\frac{1-P(s)}{1-s}=Q(s).
$$

Check index zero directly: $[s^0]R(s)=F_0=p_0=1/2$, while $[s^0]Q(s)=Q_0=1-p_0=1/2$. At index one, $F_1+Q_1=5/6+1/6=1$. The coefficient checks confirm the endpoint convention independently of the algebraic derivation.

The complete coefficient lists for the first few indices are

| $k$ | $p_k$ | $F_k=P(X\le k)$ | $Q_k=P(X>k)$ |
| ---: | ---: | ---: | ---: |
| 0 | $1/2$ | $1/2$ | $1/2$ |
| 1 | $1/3$ | $5/6$ | $1/6$ |
| 2 | $1/6$ | 1 | 0 |
| 3 | 0 | 1 | 0 |

Expanding the lower-tail function gives

$$
R(s)=\left(\frac12+\frac13s+\frac16s^2\right)(1+s+s^2+\cdots)
=\frac12+\frac56s+s^2+s^3+\cdots.
$$

For the upper tail,

$$
Q(s)=\frac{1-(\frac12+\frac13s+\frac16s^2)}{1-s}
=\frac12+\frac16s.
$$

The vanishing coefficients after $s^1$ agree with the fact that no outcome exceeds 2. A table is particularly useful in examinations because it makes it impossible to hide an endpoint shift inside algebra.

## 6. Infinite-support worked example

Let $X$ count failures before the first success in independent Bernoulli trials, with success probability $p$ and $q=1-p$. Then $P(X=k)=pq^k$ for $k\ge0$, and its p.g.f. is

$$
P(s)=\sum_{k=0}^{\infty}pq^ks^k=\frac{p}{1-qs}.
$$

The event $X>k$ requires at least $k+1$ failures, so $Q_k=q^{k+1}$ and

$$
Q(s)=\sum_{k=0}^{\infty}q^{k+1}s^k=\frac{q}{1-qs}.
$$

Using the general upper-tail identity gives the same result:

$$
\frac{1-P(s)}{1-s}
=\frac{1-p/(1-qs)}{1-s}
=\frac{q}{1-qs}.
$$

The lower cumulative probabilities are $F_k=1-q^{k+1}$, so

$$
R(s)=\frac{P(s)}{1-s}=\frac{p}{(1-qs)(1-s)}.
$$

Unlike the finite-support example, these tails have nonzero coefficients at every index. The formulas remain unchanged; only the sequence of probabilities differs.

## 7. Exam-mode checklist and traps

1. State the support and define $p_k=P(X=k)$.
2. Copy the event exactly: $X\le k$, $X>k$, or $X\ge k$.
3. Define the sequence at index zero and write its constant coefficient.
4. For lower cumulative probabilities, use $F_k-F_{k-1}=p_k$; for strict upper tails, use $Q_{k-1}-Q_k=p_k$.
5. In a difference proof, sum from $k=1$ and keep the boundary term. In a direct proof, count how many powers each $p_j$ contributes.
6. State $|s|<1$ for the geometric-series argument.
7. Check the final coefficient at $s^0$ and verify $F_k+Q_k=1$.

### Alternative upper-tail convention

If the problem defines $T_k=P(X\ge k)$ for $k\ge1$, then $T_k=Q_{k-1}$. Its series indexed with powers $s^{k-1}$ is

$$
\sum_{k=1}^{\infty}T_ks^{k-1}=Q(s),
$$

while the same terms paired with powers $s^k$ give $sQ(s)$. Do not use the strict-tail formula unchanged when the event includes the threshold. For a finite check, $P(X\ge1)=1-p_0=Q_0$, whereas $P(X>1)=Q_1$.

### Convergence and the point $s=1$

The geometric-series derivations require $|s|<1$. Although a p.g.f. satisfies $P(1)=1$, the expressions $P(s)/(1-s)$ and $(1-P(s))/(1-s)$ have denominator zero at $s=1$. Their limits cannot be obtained by direct substitution. The lower cumulative series has coefficients tending to 1, so it diverges as $s$ approaches 1 from below. The upper-tail series may converge or diverge depending on the distribution. If a boundary limit is requested, examine the tail sequence separately.

Two degenerate checks are useful. If $p_0=1$, then $X=0$ with probability one, $P(s)=1$, $F_k=1$, and $Q_k=0$ for every $k\ge0$; the formulas give $R(s)=1/(1-s)$ and $Q(s)=0$. If $p_0=0$, then $Q_0=1$ and $F_0=0$, which checks the two constant terms at the opposite boundary.

### Efficient proof layout under exam conditions

For a lower tail, write $F_0=p_0$ and $F_k-F_{k-1}=p_k$. Sum from $k=1$, explicitly identify $P(s)-p_0$, $R(s)-p_0$, and $sR(s)$, cancel the boundary term, and state $R(s)=P(s)/(1-s)$. For a strict upper tail, write $Q_0=1-p_0$ and $Q_{k-1}-Q_k=p_k$; sum from $k=1$, retain $Q_0$ in the shifted sum, then solve to obtain $Q(s)=(1-P(s))/(1-s)$. Finish by checking the constant coefficient. This compact layout displays the event convention, recurrence, initial condition, and algebra that earn the key proof marks.

Frequent exam errors: switching $>$ to $\ge$ without a one-index shift; using $P(s)/(1-s)$ for the strict upper tail; dropping the $p_0$ or $Q_0$ term; summing a lower tail from $j=1$ rather than $j=0$; claiming the tail generating function is a p.g.f.; and treating the value at $s=1$ by direct substitution even though the displayed quotient has denominator zero. If a limit at 1 is needed, it must be handled separately and may diverge for an unbounded support.