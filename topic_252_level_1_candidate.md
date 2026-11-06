## 1. Start with one probability distribution

A discrete random variable is a number that can take separate countable values. For example, $X$ might count how many calls arrive in a time period, so $X$ could be 0, 1, 2, and so on. Let $p_k=P(X=k)$ be the chance that the count is exactly $k$.

The probabilities $p_0,p_1,p_2,\ldots$ describe exact outcomes. A cumulative probability combines several exact outcomes. It answers a question such as “what is the chance of no more than 3?” or “what is the chance of more than 3?” The word **cumulative** means that we add the probabilities as we move along the possible values.

Two common cumulative quantities are:

- The **lower cumulative probability** through $k$: chance that $X$ is at most $k$.
- The **strict upper-tail probability** after $k$: chance that $X$ is greater than $k$.

The cutoff and the inequality are important. “At most 3” includes 3; “greater than 3” starts at 4.

## 2. Lower tail and upper tail in a small example

Suppose $X$ can be 0, 1, or 2 with probabilities 0.5, $1/3$, and $1/6$:

| Value $k$ | 0 | 1 | 2 |
| --- | ---: | ---: | ---: |
| Exact probability $p_k$ | 0.5 | $1/3$ | $1/6$ |

These probabilities add to 1. The lower cumulative probability is

$$
F_k=P(X\le k)=\sum_{j=0}^{k}p_j.
$$

Thus $F_0=0.5$, $F_1=0.5+1/3=5/6$, and $F_2=1$. For any larger cutoff, the probability remains 1 because all possible values have already been included.

The strict upper tail is

$$
Q_k=P(X>k)=\sum_{j=k+1}^{\infty}p_j.
$$

For this example, $Q_0=1/3+1/6=0.5$, $Q_1=1/6$, and $Q_2=0$. At each cutoff, exactly one of these events happens: $X\le k$ or $X>k$. So

$$
F_k+Q_k=1.
$$

This complement check is a simple way to catch a missed endpoint.

The values can be organized in one table:

| Cutoff $k$ | Exact chance $p_k$ | Lower tail $F_k=P(X\le k)$ | Strict upper tail $Q_k=P(X>k)$ |
| ---: | ---: | ---: | ---: |
| 0 | $1/2$ | $1/2$ | $1/2$ |
| 1 | $1/3$ | $5/6$ | $1/6$ |
| 2 | $1/6$ | 1 | 0 |
| 3 or more | 0 | 1 | 0 |

Read a row from left to right. At cutoff 1, for example, the lower event includes outcomes 0 and 1, while the strict upper event contains only outcome 2. The two sides add to 1 because they split all possible outcomes without overlap.

## 3. The probability generating function

A probability generating function (p.g.f.) stores all the exact probabilities in one power series:

$$
P(s)=p_0+p_1s+p_2s^2+\cdots
=\sum_{k=0}^{\infty}p_ks^k.
$$

The coefficient of $s^k$ is the probability of the exact value $k$. The variable $s$ is a mathematical tool, not another probability. In the small example,

$$
P(s)=0.5+\frac13s+\frac16s^2.
$$

The lower-tail probabilities are cumulative sums. Each $p_j$ appears in $F_j,F_{j+1},F_{j+2},\ldots$. In the generating function, those repeated powers make a geometric series:

$$
F(s)=\sum_{k=0}^{\infty}F_ks^k
=\sum_{j=0}^{\infty}p_j(s^j+s^{j+1}+s^{j+2}+\cdots).
$$

For $|s|<1$, the inner series is $s^j/(1-s)$. Taking out the common factor gives

$$
F(s)=\frac{P(s)}{1-s}.
$$

This formula packages every lower cumulative probability into one function. It does not mean that $F(s)$ itself is a probability distribution.

The formula can be checked by expanding it. For the example,

$$
F(s)=\left(\frac12+\frac13s+\frac16s^2\right)(1+s+s^2+s^3+\cdots).
$$

The constant coefficient is $1/2$. The coefficient of $s$ is $1/2+1/3=5/6$. The coefficient of $s^2$ is $1/2+1/3+1/6=1$. Every later coefficient is also 1 because all three probabilities have then been included. This reproduces the lower-tail table. Multiplying by $1/(1-s)$ is a compact way to repeat each probability in every later cumulative total.

In general, if the exact value is $j$, it is counted in every lower-tail event with cutoff $k=j,j+1,j+2,\ldots$. Its contribution is

$$
p_j(s^j+s^{j+1}+s^{j+2}+\cdots)=\frac{p_js^j}{1-s}.
$$

Adding these contributions over all $j$ gives $P(s)/(1-s)$. This viewpoint explains why lower cumulative probabilities use a factor $1/(1-s)$: every exact probability remains included as the cutoff moves upward.

## 4. Generating function of the strict upper tail

The strict upper-tail probability $Q_k=P(X>k)$ adds probabilities starting at $k+1$. A fixed $p_j$ appears in the tails $Q_0,Q_1,\ldots,Q_{j-1}$. Its contribution to the generating function is therefore

$$
p_j(1+s+s^2+\cdots+s^{j-1}).
$$

This finite geometric sum is $(1-s^j)/(1-s)$. Adding the contributions from all possible $j$ gives

$$
Q(s)=\sum_{j=1}^{\infty}p_j\frac{1-s^j}{1-s}.
$$

The first part of the numerator sums the probabilities above zero, which is $1-p_0$. The second part is $\sum_{j=1}^{\infty}p_js^j=P(s)-p_0$. Subtracting gives $(1-p_0)-(P(s)-p_0)=1-P(s)$. That is why the strict upper-tail formula has $1-P(s)$ in its numerator.

$$
Q(s)=\sum_{k=0}^{\infty}Q_ks^k
=\frac{1-P(s)}{1-s},\qquad |s|<1.
$$

For the small example, this gives

$$
Q(s)=\frac{1-(0.5+\frac13s+\frac16s^2)}{1-s}
=0.5+\frac16s.
$$

The coefficient of $s^0$ is $Q_0=0.5$, and the coefficient of $s^1$ is $Q_1=1/6$, just as calculated directly. There are no later terms because the largest possible value is 2.

The same result can be seen by listing what remains above each cutoff. The constant term is $Q_0=P(X>0)=p_1+p_2=1/2$. The coefficient of $s$ is $Q_1=P(X>1)=p_2=1/6$. For cutoff 2 and beyond, no value is greater than the cutoff, so those coefficients are zero. This also explains why the upper-tail function in this finite example is just $1/2+s/6$.

Notice the two numerators: lower cumulative probabilities use $P(s)$, while the strict upper tails use $1-P(s)$. Interchanging them gives the wrong sequence.

The coefficients explain this difference. The probability $p_0$ is included in every lower tail, so it contributes $p_0(1+s+s^2+\cdots)$. It is never included in a strict upper tail because no non-negative value is less than zero. The probability $p_1$ is included in $Q_0$ but not $Q_1$, so it contributes only $p_1$ to the upper-tail series. The probability $p_2$ is included in $Q_0$ and $Q_1$, so it contributes $p_2(1+s)$.

In general, $p_j$ contributes $p_js^j/(1-s)$ to the lower-tail series, because it remains included from cutoff $j$ onward. It contributes $p_j(1+s+\cdots+s^{j-1})$ to the strict upper series, because it is above cutoffs 0 through $j-1$ only. The first contribution produces numerator $P(s)$; the second finite sum produces numerator $1-P(s)$. Thinking about one coefficient at a time is often easier than memorizing the two formulas.

## 5. Two ways to understand the formulas

The first way is to notice repeated sums. Lower tails keep adding each probability as the cutoff grows; upper tails keep summing the probabilities still beyond the cutoff. Grouping these repeated terms creates a geometric series.

The second way uses differences between neighboring tail values. For lower tails, moving the cutoff from $k-1$ to $k$ adds exactly one new probability:

$$
F_k-F_{k-1}=p_k,\qquad k\ge1.
$$

For strict upper tails, moving the cutoff one step higher removes the probability at $k$:

$$
Q_{k-1}-Q_k=p_k,\qquad k\ge1.
$$

These simple changes explain why the two generating-function formulas have different numerators. The lower cumulative series starts with $F_0=p_0$. The strict upper series starts with $Q_0=1-p_0$. Forgetting those first values is the usual source of an off-by-one error.

For the numeric example, the first lower-tail difference is $F_1-F_0=5/6-1/2=1/3=p_1$. The next is $F_2-F_1=1-5/6=1/6=p_2$. For the upper tail, $Q_0-Q_1=1/2-1/6=1/3=p_1$, and $Q_1-Q_2=1/6-0=1/6=p_2$. Each new exact probability is precisely the amount added to the lower tail or removed from the upper tail.

A different book may call $P(X\ge k)$ the upper tail. That event includes the cutoff, so it equals the strict upper tail one index earlier: $P(X\ge k)=Q_{k-1}$ for $k\ge1$. Always write the event before using a formula.

For the example, $P(X\ge1)=p_1+p_2=1/2$, which equals $Q_0$, not $Q_1$. Meanwhile $P(X>1)=p_2=1/6$, which equals $Q_1$. These answers differ because one event includes outcome 1 and the other does not. A table’s heading or a book’s notation can use either convention, so check the inequality rather than relying on the phrase “upper tail” alone.

## 6. Exam steps and common mistakes

1. Write $p_k=P(X=k)$ and check the probabilities add to 1.
2. Write the event exactly: $X\le k$, $X>k$, or $X\ge k$.
3. Define the cumulative sequence and its index beginning at 0.
4. Define the p.g.f. $P(s)$ of the exact probabilities.
5. Use $F(s)=P(s)/(1-s)$ for the lower cumulative sequence.
6. Use $Q(s)=(1-P(s))/(1-s)$ for the strict upper tail.
7. Check the first coefficient: $F_0=p_0$ and $Q_0=1-p_0$.
8. Check that $F_k+Q_k=1$ for each cutoff.

Common mistakes are including $p_k$ in a strict upper tail, omitting it from a lower cumulative probability, shifting the powers of $s$ by one, and calling a tail generating function a p.g.f. The formulas assume a non-negative integer-valued random variable and are used for $|s|<1$. If a different support or tail convention is given, restate the index and derive the corresponding formula before substituting.

The denominator also deserves attention. The displayed expressions have $1-s$ below the numerator, so do not simply substitute $s=1$ into them. The original probability generating function satisfies $P(1)=1$, but a tail series may behave differently at 1. In this lesson the formulas are derived within $|s|<1$; any value at the boundary needs its own limiting argument. For a finite distribution the coefficients can still be checked directly from the table, as we did above.

For a finite support ending at $m$, every cutoff $k\ge m$ has $F_k=1$ and $Q_k=0$. In the example with largest value 2, this gives $F_2=F_3=\cdots=1$ and $Q_2=Q_3=\cdots=0$. Checking the behavior beyond the last possible value is a quick way to confirm that the tail direction and endpoint have been handled correctly.