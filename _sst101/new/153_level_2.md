## 1. Foundational Concepts, Definitions, and Axioms

### 1.1 Moments as functionals that encode shape

A moment is an average of a power of a deviation from a chosen reference point. The definition is deliberately general, because the single family of quantities indexed by the integer order $r$ contains, as special cases, the arithmetic mean, the variance, the two shape coefficients of the preceding topic and the building blocks of the moment generating function. What changes from one member of the family to another is only the order and the reference point.

Two reference points dominate the theory. Moments about zero, written $\bar{x^{r}}$, use the origin of the measurement scale and are convenient for algebraic work because the powers of the observations can be expanded by the binomial theorem. Moments about the mean, written $m_r$, use the arithmetic mean and are called central moments; they are the natural shape descriptors because they are unchanged when every observation is shifted by a constant.

Between the two sits a computational device. Moments about an arbitrary origin $A$, written $m_r'$, are easy to compute by hand when $A$ is a round number or a class mark, and exact algebraic identities convert them into central moments. The whole of the computational method in this topic rests on those identities.

### 1.2 Formal definitions

> **Definition (Moment about zero).** For observations $x_1, \dots, x_n$, the $r$-th moment about zero is

$$
\bar{x^{r}} = \frac{1}{n}\sum_{i=1}^{n} x_i^{r}, \qquad r = 1, 2, 3, \dots
$$

> **Definition (Central moment).** The $r$-th moment about the arithmetic mean is

$$
m_r = \frac{1}{n}\sum_{i=1}^{n}\left(x_i - \bar{x}\right)^{r} .
$$

> **Definition (Working moment).** For an arbitrary origin $A$ and deviations $d_i = x_i - A$, the $r$-th moment about $A$ is

$$
m_r' = \frac{1}{n}\sum_{i=1}^{n} d_i^{r} .
$$

The prime is not a derivative and not decoration: it distinguishes moments about $A$ from moments about the mean, and the two differ by a quantity that grows with the distance between $A$ and $\bar{x}$.

### 1.3 Grouped data and coded data

For frequency data with distinct values or class marks $x_1, \dots, x_k$ and frequencies $f_1, \dots, f_k$, every definition acquires a weight and the divisor becomes the total frequency.

$$
n = \sum_{i=1}^{k} f_i, \qquad m_r' = \frac{1}{n}\sum_{i=1}^{k} f_i d_i^{r}, \qquad m_r = \frac{1}{n}\sum_{i=1}^{k} f_i\left(x_i - \bar{x}\right)^{r} .
$$

For grouped data with equal class widths $c$, the further substitution $d_i = c u_i$ factors the scale out of the sum entirely.

$$
m_r' = \frac{1}{n}\sum_{i=1}^{k} f_i\left(c u_i\right)^{r} = c^{r}\left(\frac{1}{n}\sum_{i=1}^{k} f_i u_i^{r}\right) .
$$

The coded column $f_i u_i^{r}$ consists of small integers, so the arithmetic can be done mentally, and the factor $c^{r}$ is applied once at the end. If central moments are computed in the coded scale, the rescaled central moment is $c^{r}$ times the coded one, because a change of scale multiplies every deviation by $c$ and a constant factor passes through the averaging.

### 1.4 The four central moments and their interpretation

| Order | Symbol | Expression | Interpretation |
|---|---|---|---|
| 1 | $m_1$ | $\frac{1}{n}\sum\left(x_i - \bar{x}\right)$ | identically zero; a check on the arithmetic |
| 2 | $m_2$ | $\frac{1}{n}\sum\left(x_i - \bar{x}\right)^{2}$ | the variance; the spread about the mean |
| 3 | $m_3$ | $\frac{1}{n}\sum\left(x_i - \bar{x}\right)^{3}$ | the asymmetry; positive for a right tail |
| 4 | $m_4$ | $\frac{1}{n}\sum\left(x_i - \bar{x}\right)^{4}$ | the weight of the tails; basis of kurtosis |

The fourth moment is not a measure of spread in competition with the second. It answers a different question: how much of the total variation is contributed by observations that lie a long way from the mean. A distribution with the same variance but heavier tails has a larger fourth moment, and that is exactly what the kurtosis coefficients report.

### 1.5 Axioms of the averaging operator

> **Axiom (Linearity).** For constants $a$ and $b$, the average of $a + b y_i$ equals $a$ plus $b$ times the average of $y_i$.

Linearity is what allows every expansion in this topic to be carried out term by term, and it is why the mean of a sum is the sum of the means.

> **Axiom (Translation).** Adding a constant $a$ to every observation adds $a$ to the mean and leaves every central moment unchanged.

Translation invariance is the formal reason central moments describe shape rather than location.

> **Axiom (Scaling).** Multiplying every observation by a constant $b$ multiplies the $r$-th central moment by $b^{r}$ and leaves every standardised ratio unchanged.

Scaling is the formal reason the coefficients $\beta_1$ and $\beta_2$ are comparable between variables measured in different units.

## 2. Theorems, Lemmas, and Analytical Properties

### 2.1 Lemma: the first central moment vanishes

> **Lemma 1.** For any finite data set, $m_1 = 0$.

The proof is a two-line application of linearity, and it is given in Section 3. The lemma has practical force: a non-zero computed first central moment is proof of an arithmetic error, never a discovery about the data.

### 2.2 Theorem: the second central moment is the variance and is minimal

> **Theorem 2.** $m_2$ equals the descriptive variance $s^{2}$, and for every constant $c$,

$$
\frac{1}{n}\sum_{i=1}^{n}\left(x_i - c\right)^{2} = m_2 + \left(\bar{x} - c\right)^{2} \ge m_2 .
$$

The identity shows that the second moment about any point equals the variance plus the squared distance from that point to the mean. Two consequences follow immediately. The variance is the smallest second moment available, and the conversion identity $m_2 = m_2' - \left(m_1'\right)^{2}$ is exactly this statement rearranged, since $m_1' = \bar{x} - A$.

### 2.3 Theorem: the third central moment and asymmetry

> **Theorem 3.** If a distribution is symmetric about its mean then $m_3 = 0$. If $m_3 > 0$ the cubed positive deviations dominate, which occurs when the right tail is longer and heavier in the cubed sense; if $m_3 < 0$ the left tail dominates.

The theorem is one-directional. A zero third moment is necessary for symmetry but not sufficient, because a long thin tail on one side can be cancelled by a short thick shoulder on the other. The sign of $m_3$ is nevertheless the standard directional reading of moment skewness, and it is the sign that must be quoted when only the moment coefficient $\beta_1$ is available.

### 2.4 Theorem: the fourth central moment and tail weight

> **Theorem 4.** $m_4 > 0$ for every non-degenerate data set, and $m_4 \ge m_2^{2}$, with equality exactly for a two-point distribution.

The inequality follows from the Cauchy–Schwarz inequality applied to $\left(x_i - \bar{x}\right)^{2}$ and the constant one, and it is the reason $\beta_2 = m_4/m_2^{2}$ can never fall below one. The fourth moment is dominated by the largest deviations, since a deviation twice as large contributes sixteen times as much rather than four times as much.

### 2.5 Standardised moment ratios

Raw moments carry units. The $r$-th central moment has units of the variable raised to the power $r$, so it cannot be compared between variables measured in different units. Dividing by the appropriate power of the standard deviation removes the units.

$$
\alpha_r = \frac{m_r}{m_2^{\frac{r}{2}}} .
$$

The first two standardised ratios are the ones in use.

$$
\gamma_1 = \alpha_3 = \frac{m_3}{m_2^{\frac{3}{2}}}, \qquad \beta_2 = \alpha_4 = \frac{m_4}{m_2^{2}} .
$$

The quantity $\beta_1 = \gamma_1^{2}$ is the squared form of the skewness ratio, and $\gamma_2 = \beta_2 - 3$ is the excess kurtosis. The names beta and gamma are conventions: $\beta_1$ and $\beta_2$ are the unshifted squared or fourth-power ratios, while $\gamma_1$ and $\gamma_2$ are the signed third ratio and the shifted fourth ratio.

### 2.6 Theorem: the general translation identity

> **Theorem 5.** For any origin $A$ and any order $r$,

$$
m_r' = \sum_{j=0}^{r}\binom{r}{j} m_j\left(\bar{x} - A\right)^{r-j}, \qquad m_0 = 1 .
$$

The identity is the binomial expansion of $\left(x_i - A\right)^{r} = \left[\left(x_i - \bar{x}\right) + \left(\bar{x} - A\right)\right]^{r}$ averaged over the data. It generates every conversion formula in either direction, and it is the fastest way to answer a question that supplies moments about one origin and asks for moments about another.

### 2.7 Theorem: behaviour under an affine transformation

> **Theorem 6.** If $y_i = a + b x_i$, then $m_r\left(y\right) = b^{r} m_r\left(x\right)$ for every $r \ge 1$, hence every standardised ratio of even order is unchanged and every standardised ratio of odd order is multiplied by the sign of $b$.

The first part follows because $y_i - \bar{y} = b\left(x_i - \bar{x}\right)$, so each deviation is multiplied by $b$ and the $r$-th power by $b^{r}$. The second follows by substituting into the ratio and cancelling powers of $\left|b\right|$. Consequently $\beta_1$ and $\beta_2$ are pure shape measures, while $m_2$, $m_3$ and $m_4$ are not.

### 2.8 The moment generating function

> **Definition (Moment generating function).** For a random variable $X$, the moment generating function is

$$
M_X\left(t\right) = E\left[e^{tX}\right],
$$

defined for those real $t$ for which the expectation is finite.

Expanding the exponential in a power series and averaging term by term gives the moment expansion.

$$
M_X\left(t\right) = \sum_{r=0}^{\infty} m_r'\frac{t^{r}}{r!} = 1 + m_1't + m_2'\frac{t^{2}}{2} + m_3'\frac{t^{3}}{6} + \dots
$$

The name is justified by differentiation at the origin.

$$
m_r' = \left.\frac{d^{r}}{dt^{r}}M_X\left(t\right)\right|_{t=0} .
$$

The analogous function for the central moments multiplies by $e^{-t\bar{x}}$.

$$
M_{X - \bar{x}}\left(t\right) = e^{-t\bar{x}}M_X\left(t\right) = \sum_{r=0}^{\infty} m_r\frac{t^{r}}{r!} .
$$

Two facts make the device powerful. If the moment generating function exists in a neighbourhood of zero then it determines the distribution, so two distributions with the same moments are identical; and a sum of independent variables has a moment generating function equal to the product of the individual functions, which turns convolution of distributions into multiplication of functions.

### 2.9 Cumulants and the link to the shape coefficients

The cumulants are the coefficients in the logarithm of the moment generating function.

$$
K_X\left(t\right) = \log M_X\left(t\right) = \sum_{r=1}^{\infty}\kappa_r\frac{t^{r}}{r!} .
$$

The first four cumulants are directly interpretable.

$$
\kappa_1 = \bar{x}, \qquad \kappa_2 = m_2, \qquad \kappa_3 = m_3, \qquad \kappa_4 = m_4 - 3m_2^{2} .
$$

The fourth cumulant is precisely the numerator of the excess kurtosis, since $\gamma_2 = \kappa_4/m_2^{2}$. For a normal distribution every cumulant beyond the second vanishes, which is an elegant restatement of the fact that the normal curve has zero skewness and zero excess kurtosis. Cumulants are also additive for independent variables, so the cumulants of a sum are the sums of the cumulants, a property that the moments themselves do not possess.

### 2.10 Summary of analytical properties

| Quantity | Depends on | Value for a normal distribution | Invariant under translation | Scales as |
|---|---|---|---|---|
| $m_2$ | all observations | $\sigma^{2}$ | yes | $b^{2}$ |
| $m_3$ | all observations | $0$ | yes | $b^{3}$ |
| $m_4$ | all observations | $3\sigma^{4}$ | yes | $b^{4}$ |
| $\gamma_1$ | all observations | $0$ | yes | sign of $b$ |
| $\beta_2$ | all observations | $3$ | yes | unchanged |
| $\kappa_4$ | all observations | $0$ | yes | $b^{4}$ |

## 3. Formal Proofs, Derivations, and Methods

### 3.1 Derivation of the first central moment

By linearity of the average,

$$
m_1 = \frac{1}{n}\sum_{i=1}^{n}\left(x_i - \bar{x}\right) = \frac{1}{n}\sum_{i=1}^{n} x_i - \frac{1}{n}\sum_{i=1}^{n}\bar{x} .
$$

The first term is $\bar{x}$ by definition, and the second is $n\bar{x}/n = \bar{x}$, so the difference is zero. For grouped data the same computation uses $n = \sum f_i$ and gives $m_1 = \bar{x} - \bar{x} = 0$.

### 3.2 Derivation of the second central moment identity

Write $x_i - \bar{x} = \left(x_i - A\right) - \left(\bar{x} - A\right)$ and expand the square.

$$
\left(x_i - \bar{x}\right)^{2} = \left(x_i - A\right)^{2} - 2\left(x_i - A\right)\left(\bar{x} - A\right) + \left(\bar{x} - A\right)^{2} .
$$

Averaging over the data and using linearity,

$$
m_2 = \frac{1}{n}\sum\left(x_i - A\right)^{2} - 2\left(\bar{x} - A\right)\frac{1}{n}\sum\left(x_i - A\right) + \left(\bar{x} - A\right)^{2} .
$$

The three averaged terms are $m_2'$, $m_1'$ and one, so

$$
m_2 = m_2' - 2\left(\bar{x} - A\right)m_1' + \left(\bar{x} - A\right)^{2} = m_2' - 2\left(m_1'\right)^{2} + \left(m_1'\right)^{2} = m_2' - \left(m_1'\right)^{2} .
$$

The same algebra, read in reverse, proves that the variance is the smallest second moment about any point.

### 3.3 Derivation of the third central moment identity

Expanding the cube of the difference and averaging gives four sums.

$$
m_3 = \frac{1}{n}\sum\left(x_i - A\right)^{3} - 3\left(\bar{x} - A\right)\frac{1}{n}\sum\left(x_i - A\right)^{2} + 3\left(\bar{x} - A\right)^{2}\frac{1}{n}\sum\left(x_i - A\right) - \left(\bar{x} - A\right)^{3} .
$$

Substituting the working moments and $\bar{x} - A = m_1'$,

$$
m_3 = m_3' - 3m_1'm_2' + 3\left(m_1'\right)^{3} - \left(m_1'\right)^{3} = m_3' - 3m_1'm_2' + 2\left(m_1'\right)^{3} .
$$

The combination of the last two terms is the step most often omitted. Its effect is not small: omitting it changes the answer by exactly $\left(m_1'\right)^{3}$, which can reverse the sign of a small third moment.

### 3.4 Derivation of the fourth central moment identity

Expanding the fourth power of the difference, using the binomial coefficients $1, 4, 6, 4, 1$, and averaging,

$$
m_4 = \frac{1}{n}\sum\left(x_i - A\right)^{4} - 4\left(\bar{x} - A\right)\frac{1}{n}\sum\left(x_i - A\right)^{3} + 6\left(\bar{x} - A\right)^{2}\frac{1}{n}\sum\left(x_i - A\right)^{2} - 4\left(\bar{x} - A\right)^{3}\frac{1}{n}\sum\left(x_i - A\right) + \left(\bar{x} - A\right)^{4} .
$$

Substituting the working moments,

$$
m_4 = m_4' - 4m_1'm_3' + 6\left(m_1'\right)^{2}m_2' - 4\left(m_1'\right)^{4} + \left(m_1'\right)^{4} .
$$

Collecting the last two terms gives the final form.

$$
m_4 = m_4' - 4m_1'm_3' + 6\left(m_1'\right)^{2}m_2' - 3\left(m_1'\right)^{4} .
$$

The same argument with the multinomial coefficients of order five and six produces the higher identities.

$$
m_5 = m_5' - 5m_1'm_4' + 10\left(m_1'\right)^{2}m_3' - 10\left(m_1'\right)^{3}m_2' + 4\left(m_1'\right)^{5},
$$

$$
m_6 = m_6' - 6m_1'm_5' + 15\left(m_1'\right)^{2}m_4' - 20\left(m_1'\right)^{3}m_3' + 15\left(m_1'\right)^{4}m_2' - 5\left(m_1'\right)^{6} .
$$

The patterns repay inspection. The coefficient of the leading term is always one, the coefficient of the second term is minus $r$, and the final constant collects all the powers of $m_1'$ that arise from the terms of order $r$ and $r-1$.

### 3.5 Proof that symmetry annihilates the odd central moments

Suppose the data are symmetric about the mean, so that every observation $\bar{x} - h$ is accompanied by an observation $\bar{x} + h$ of the same frequency, and any unpaired observation equals $\bar{x}$.

For odd $r$, the contribution of one pair is

$$
f\left(-h\right)^{r} + f\left(h\right)^{r} = -fh^{r} + fh^{r} = 0 .
$$

Every pair contributes zero and any unpaired observation at the mean contributes zero, so the whole sum vanishes and $m_r = 0$ for every odd $r$. In particular $m_1 = 0$ and $m_3 = 0$, and therefore $\gamma_1 = 0$ and $\beta_1 = 0$.

The converse fails, and a counterexample makes the failure vivid. Take the six observations $0$, $1$, $4$, $4$, $4$ and $7$. Their mean is $3.33$ and their median is $4$, so the two averages already disagree and the shape is plainly not a mirror image: there is a thin left tail at zero and one and a single bump on the right at seven. A direct computation gives $m_2 = 5.222$, $m_3 = 0.074$ and $\gamma_1 = 0.006$, so the third central moment is almost exactly zero and the moment coefficient of skewness reports near-perfect symmetry. The fourth moment of the same data is $55.74$, giving $\beta_2 = 2.04$, and the coefficient of kurtosis detects the flatness that the skewness coefficient misses. Moment skewness is therefore a weighted summary, not a test for symmetry.

### 3.6 Proof of the moment generating function expansion

Assume the expectation exists for $t$ in some open interval containing zero, so that the exponential can be expanded and the average taken term by term.

$$
E\left[e^{tX}\right] = E\left[\sum_{r=0}^{\infty}\frac{\left(tX\right)^{r}}{r!}\right] = \sum_{r=0}^{\infty}\frac{t^{r}}{r!}E\left[X^{r}\right] .
$$

The $r$-th term of the series is $m_r' t^{r}/r!$, so the coefficient of $t^{r}$ is $m_r'/r!$. Differentiating $r$ times kills every term of lower order and multiplies the $r$-th term by $r!$, while every term of higher order retains a positive power of $t$; setting $t = 0$ therefore leaves exactly $m_r'$. The argument for the central generating function is identical after the substitution $X \mapsto X - \bar{x}$.

### 3.7 Derivation of the normal moments from its generating function

For a normal variable with mean $\mu$ and variance $\sigma^{2}$ the moment generating function is

$$
M_X\left(t\right) = \exp\left(\mu t + \frac{1}{2}\sigma^{2}t^{2}\right) .
$$

Differentiating twice,

$$
M_X'\left(t\right) = \left(\mu + \sigma^{2}t\right)M_X\left(t\right), \qquad M_X''\left(t\right) = \left[\sigma^{2} + \left(\mu + \sigma^{2}t\right)^{2}\right]M_X\left(t\right) .
$$

Setting $t = 0$ and using $M_X\left(0\right) = 1$ gives $m_1' = \mu$ and $m_2' = \sigma^{2} + \mu^{2}$, so the variance is $m_2 = \sigma^{2}$ as expected. Continuing the differentiation and evaluating at zero gives the third and fourth raw moments, from which the central moments follow.

$$
m_3 = 0, \qquad m_4 = 3\sigma^{4}, \qquad \beta_2 = \frac{3\sigma^{4}}{\sigma^{4}} = 3 .
$$

The vanishing of the third central moment and the value three for the fourth are the two facts on which the entire vocabulary of skewness and kurtosis is built.

### 3.8 Method: moments of a grouped distribution by coding

1. Confirm that the classes have equal width $c$; if not, use class marks and the direct formulas.
2. Compute each class mark as the midpoint of the class boundaries, not of the stated limits.
3. Choose $A$ equal to a central class mark, and compute $u_i = \left(x_i - A\right)/c$. Verify that the $u_i$ are consecutive integers.
4. Build the columns $f_i u_i$, $f_i u_i^{2}$, $f_i u_i^{3}$ and $f_i u_i^{4}$, and total each one.
5. Divide each total by $n$ to obtain the coded working moments, and apply the conversion identities to obtain the coded central moments.
6. Multiply the coded central moments by $c^{r}$ to return to the original units.
7. Report $\bar{x} = A + c\,m_1'$, $s = \sqrt{m_2}$, and the standardised coefficients.
8. Verify $\beta_1 \ge 0$, $\beta_2 \ge 1$ and $\beta_2 \ge \beta_1 + 1$ before writing the interpretation.

### 3.9 Method: from moments to shape coefficients

1. Identify which moments are given and about which origin.
2. If the origin is not the mean, use Theorem 5 to translate, or use the conversion identities of Sections 3.2 to 3.4 in the direction required.
3. Compute $m_2$, $m_3$ and $m_4$ about the mean as an intermediate stage; never substitute working moments directly into a shape coefficient.
4. Form $\gamma_1 = m_3/m_2^{3/2}$, $\beta_1 = \gamma_1^{2}$, $\beta_2 = m_4/m_2^{2}$ and $\gamma_2 = \beta_2 - 3$.
5. State the direction from the sign of $m_3$ and the strength from the size of $\beta_1$ or $\gamma_1$.
6. Classify the kurtosis by comparing $\beta_2$ with three.

## 4. Representative Worked Examples and Solutions

### 4.1 Problem: moments of five values about an off-centre origin

Compute the first four moments about the mean for the observations 2, 4, 6, 8 and 10 using the assumed origin $A = 3$, and verify the results by computing the central moments directly.

### 4.2 Solution: convert, then verify directly

Step 1. Build the table of deviations from $A = 3$ and their powers.

| $x$ | $d$ | $d^{2}$ | $d^{3}$ | $d^{4}$ |
|---|---|---|---|---|
| 2 | $-1$ | 1 | $-1$ | 1 |
| 4 | 1 | 1 | 1 | 1 |
| 6 | 3 | 9 | 27 | 81 |
| 8 | 5 | 25 | 125 | 625 |
| 10 | 7 | 49 | 343 | 2401 |
| Total | 15 | 85 | 495 | 3109 |

Step 2. Divide each total by five.

$$
m_1' = 3, \qquad m_2' = 17, \qquad m_3' = 99, \qquad m_4' = 621.8 .
$$

Step 3. Recover the mean and confirm it by inspection.

$$
\bar{x} = A + m_1' = 6 .
$$

Step 4. Apply the conversion identities.

$$
m_2 = 17 - 3^{2} = 8, \qquad m_3 = 99 - 3(3)(17) + 2(3)^{3} = 0,
$$

$$
m_4 = 621.8 - 4(3)(99) + 6(3)^{2}(17) - 3(3)^{4} = 108.8 .
$$

Step 5. Verify directly from the mean. The deviations from six are $-4, -2, 0, 2, 4$, whose squares are $16, 4, 0, 4, 16$ and whose fourth powers are $256, 16, 0, 16, 256$.

$$
m_2 = \frac{40}{5} = 8, \qquad m_3 = \frac{-64 - 8 + 0 + 8 + 64}{5} = 0, \qquad m_4 = \frac{544}{5} = 108.8 .
$$

Step 6. Compute the coefficients.

$$
\beta_1 = 0, \qquad \beta_2 = \frac{108.8}{64} = 1.7, \qquad \gamma_2 = -1.3 .
$$

Step 7. Interpret. The direct computation reproduces the converted values exactly, which is the point of the exercise. The distribution is symmetric, and its coefficient of kurtosis of $1.7$ is well below three, so it is strongly platykurtic: five evenly spaced observations cannot produce heavy tails.

### 4.3 Problem: a set with one extreme value

For the observations 2, 3, 4, 5 and 16, compute the four central moments about the mean using the assumed origin $A = 5$, then compute the skewness and kurtosis coefficients.

### 4.4 Solution: the outlier dominates the third and fourth moments

Step 1. Build the table with $d = x - 5$.

| $x$ | $d$ | $d^{2}$ | $d^{3}$ | $d^{4}$ |
|---|---|---|---|---|
| 2 | $-3$ | 9 | $-27$ | 81 |
| 3 | $-2$ | 4 | $-8$ | 16 |
| 4 | $-1$ | 1 | $-1$ | 1 |
| 5 | $0$ | 0 | 0 | 0 |
| 16 | $11$ | 121 | $1331$ | 14641 |
| Total | $5$ | $135$ | $1295$ | $14739$ |

Step 2. Divide by five to obtain the working moments.

$$
m_1' = 1, \qquad m_2' = 27, \qquad m_3' = 259, \qquad m_4' = 2947.8 .
$$

Step 3. Recover the mean.

$$
\bar{x} = 5 + 1 = 6 .
$$

Step 4. Convert to central moments.

$$
m_2 = 27 - 1 = 26,
$$

$$
m_3 = 259 - 3(1)(27) + 2(1)^{3} = 259 - 81 + 2 = 180,
$$

$$
m_4 = 2947.8 - 4(1)(259) + 6(1)^{2}(27) - 3(1)^{4} = 2947.8 - 1036 + 162 - 3 = 2070.8 .
$$

Step 5. Verify against a direct computation. The deviations from six are $-4, -3, -2, -1$ and $10$, whose squares sum to $130$, whose cubes sum to $900$, and whose fourth powers sum to $10354$.

$$
m_2 = \frac{130}{5} = 26, \qquad m_3 = \frac{900}{5} = 180, \qquad m_4 = \frac{10354}{5} = 2070.8 .
$$

Step 6. Compute the standard deviation and the coefficients.

$$
s = \sqrt{26} = 5.099, \qquad \gamma_1 = \frac{180}{26^{\frac{3}{2}}} = \frac{180}{132.57} = 1.358, \qquad \beta_1 = 1.358^{2} = 1.843,
$$

$$
\beta_2 = \frac{2070.8}{26^{2}} = \frac{2070.8}{676} = 3.063, \qquad \gamma_2 = 0.063 .
$$

Step 7. Interpret and check. The positive third moment and the large value of $\gamma_1$ show a strong right skew created by the single observation of sixteen. The coefficient of kurtosis of $3.063$ is only just above three, so the distribution is very mildly leptokurtic despite the outlier, because one extreme value raises the fourth moment by roughly as much as it raises the square of the variance. Pearson's inequality is satisfied, since $3.063$ exceeds $1.843 + 1 = 2.843$.

### 4.5 Problem: moments and shape coefficients for a grouped wage table

The daily wages of one hundred workers are grouped in classes of width five.

| Wage class | 3–7 | 8–12 | 13–17 | 18–22 | 23–27 | 28–32 | 33–37 |
|---|---|---|---|---|---|---|---|
| Number of workers | 4 | 10 | 20 | 36 | 16 | 12 | 2 |

Compute the first four moments about the mean and the four shape coefficients.

### 4.6 Solution: work in the original units, then cross-check in the coded units

Step 1. Take the class marks as the midpoints $5, 10, 15, 20, 25, 30, 35$, the assumed origin $A = 20$ and the class width $c = 5$, so that $d = x - 20$ and $u = d/5$.

| Class mark $x$ | $f$ | $d$ | $u$ | $fd$ | $fd^{2}$ | $fd^{3}$ | $fd^{4}$ |
|---|---|---|---|---|---|---|---|
| 5 | 4 | $-15$ | $-3$ | $-60$ | 900 | $-13500$ | 202500 |
| 10 | 10 | $-10$ | $-2$ | $-100$ | 1000 | $-10000$ | 100000 |
| 15 | 20 | $-5$ | $-1$ | $-100$ | 500 | $-2500$ | 12500 |
| 20 | 36 | $0$ | $0$ | $0$ | 0 | 0 | 0 |
| 25 | 16 | $5$ | $1$ | $80$ | 400 | 2000 | 10000 |
| 30 | 12 | $10$ | $2$ | $120$ | 1200 | 12000 | 120000 |
| 35 | 2 | $15$ | $3$ | $30$ | 450 | 6750 | 101250 |
| Total | 100 | | | $-30$ | $4450$ | $-5250$ | $546250$ |

Step 2. Divide by $n = 100$ to obtain the working moments in the original units.

$$
m_1' = -0.3, \qquad m_2' = 44.5, \qquad m_3' = -52.5, \qquad m_4' = 5462.5 .
$$

Step 3. Recover the mean and apply the conversion identities.

$$
\bar{x} = 20 + \left(-0.3\right) = 19.7,
$$

$$
m_2 = 44.5 - 0.09 = 44.41,
$$

$$
m_3 = -52.5 - 3\left(-0.3\right)\left(44.5\right) + 2\left(-0.3\right)^{3} = -52.5 + 40.05 - 0.054 = -12.504,
$$

$$
m_4 = 5462.5 - 4\left(-0.3\right)\left(-52.5\right) + 6\left(0.09\right)\left(44.5\right) - 3\left(0.0081\right) = 5462.5 - 63 + 24.03 - 0.024 = 5423.51 .
$$

Step 4. Cross-check in the coded units. With $d = 5u$ the coded working moments are $m_1'\left(u\right) = -0.06$, $m_2'\left(u\right) = 1.78$, $m_3'\left(u\right) = -0.42$ and $m_4'\left(u\right) = 8.74$.

$$
m_2\left(u\right) = 1.78 - 0.0036 = 1.7764, \qquad m_2 = 25 \times 1.7764 = 44.41,
$$

$$
m_3\left(u\right) = -0.42 - 3\left(-0.06\right)\left(1.78\right) + 2\left(-0.000216\right) = -0.100032, \qquad m_3 = 125 \times \left(-0.100032\right) = -12.504 .
$$

Both routes agree, which confirms the arithmetic.

Step 5. Compute the coefficients.

$$
s = \sqrt{44.41} = 6.664, \qquad \gamma_1 = \frac{-12.504}{6.664^{3}} = -0.042, \qquad \beta_1 = 0.0018,
$$

$$
\beta_2 = \frac{5423.51}{44.41^{2}} = \frac{5423.51}{1972.25} = 2.750, \qquad \gamma_2 = -0.250 .
$$

Step 6. Interpret. The third moment is very small and negative, so the wage distribution is almost symmetric with a barely detectable left skew; the coefficient $\beta_1 = 0.0018$ is essentially zero. The coefficient of kurtosis of $2.750$ is below three, so the distribution is mildly platykurtic, its tails being lighter than a normal curve with the same variance. The consistency conditions hold because $2.750$ exceeds $0.0018 + 1$.

### 4.7 Problem: moments from a moment generating function

A random variable takes the value zero with probability $0.4$ and the value one with probability $0.6$. Use its moment generating function to find the four central moments and the coefficients of skewness and kurtosis.

### 4.8 Solution: differentiate the generating function, then convert

Step 1. Write the moment generating function by averaging $e^{tX}$ over the two possible values.

$$
M_X\left(t\right) = 0.4\,e^{0} + 0.6\,e^{t} = 0.4 + 0.6e^{t} .
$$

Step 2. Differentiate and evaluate at zero. Every derivative of $0.6e^{t}$ is $0.6e^{t}$, which equals $0.6$ at $t = 0$, so every raw moment of positive order equals $0.6$.

$$
m_1' = m_2' = m_3' = m_4' = 0.6 .
$$

Step 3. Convert to central moments using the identities.

$$
m_2 = 0.6 - 0.36 = 0.24,
$$

$$
m_3 = 0.6 - 3\left(0.6\right)\left(0.6\right) + 2\left(0.216\right) = 0.6 - 1.08 + 0.432 = -0.048,
$$

$$
m_4 = 0.6 - 4\left(0.6\right)\left(0.6\right) + 6\left(0.36\right)\left(0.6\right) - 3\left(0.1296\right) = 0.6 - 1.44 + 1.296 - 0.3888 = 0.0672 .
$$

Step 4. Compute the coefficients.

$$
\gamma_1 = \frac{-0.048}{0.24^{\frac{3}{2}}} = \frac{-0.048}{0.11758} = -0.408, \qquad \beta_1 = 0.1667,
$$

$$
\beta_2 = \frac{0.0672}{0.0576} = 1.1667, \qquad \gamma_2 = -1.833 .
$$

Step 5. Interpret. The negative third moment reflects the fact that the smaller probability is attached to the larger value, so the distribution has a short right shoulder rather than a long right tail. The coefficient of kurtosis of $1.1667$ is the smallest value that a distribution on two points can have, and it is far below three, so the distribution is strongly platykurtic with no tail at all beyond the two support points.

Step 6. Verify Pearson's inequality exactly.

$$
\beta_1 + 1 = 1.1667 = \beta_2 .
$$

Equality holds because a two-point distribution is precisely the case in which the inequality of Section 3 of the companion topic is sharp. This example is therefore also a check that the inequality has been stated correctly.

### 4.9 Problem: moments of an exponential distribution from its generating function

An exponential variable with rate $\lambda = 0.5$ has moment generating function $M\left(t\right) = \lambda/\left(\lambda - t\right)$ for $t < \lambda$. Find its four central moments and both shape coefficients.

### 4.10 Solution: expand the generating function and convert

Step 1. Write the generating function as a geometric series.

$$
M\left(t\right) = \frac{0.5}{0.5 - t} = \frac{1}{1 - 2t} = \sum_{r=0}^{\infty}\left(2t\right)^{r} .
$$

Step 2. Match coefficients with the moment expansion $M\left(t\right) = \sum m_r' t^{r}/r!$ to read off the raw moments.

$$
m_r' = r!\,2^{r}, \qquad m_1' = 2, \quad m_2' = 8, \quad m_3' = 48, \quad m_4' = 384 .
$$

Step 3. Convert to central moments.

$$
m_2 = 8 - 4 = 4,
$$

$$
m_3 = 48 - 3\left(2\right)\left(8\right) + 2\left(8\right) = 48 - 48 + 16 = 16,
$$

$$
m_4 = 384 - 4\left(2\right)\left(48\right) + 6\left(4\right)\left(8\right) - 3\left(16\right) = 384 - 384 + 192 - 48 = 144 .
$$

Step 4. Compute the coefficients.

$$
\gamma_1 = \frac{16}{4^{\frac{3}{2}}} = \frac{16}{8} = 2, \qquad \beta_1 = 4, \qquad \beta_2 = \frac{144}{16} = 9, \qquad \gamma_2 = 6 .
$$

Step 5. Interpret. The exponential distribution is strongly right skewed, with a coefficient of skewness of two and a coefficient of kurtosis of nine, three times the normal value. The interpretation is that long waits are far more common than a normal curve would suggest, which is why queueing and reliability calculations cannot use normal approximations without correction.

Step 6. Verify the standard results. For an exponential distribution with rate $\lambda$ the general formulas are $\gamma_1 = 2$ and $\beta_2 = 9$, independent of $\lambda$, which is consistent with the requirement that standardised coefficients be invariant under a change of scale.

## 5. Mathematical Extensions, Limits, and Common Errors

The moment machinery is exact and elementary, but it has limits that matter in application: moments need not exist, moments that exist need not determine the distribution, and sample moments are noisy. This section sets out those limits and then lists the computational errors that recur in scripts.

### 5.1 Existence of moments

A moment of order $r$ exists only if the average of the $r$-th powers is finite. For distributions with very heavy tails, such as the Cauchy distribution, even the first moment fails to exist, and the sample mean does not converge to anything stable. For others the first moment exists but the second does not, so the variance is infinite and the coefficient of kurtosis cannot be formed at all.

The practical consequence is that a computed kurtosis should be interpreted with care when the data show a few extraordinarily large values. In such cases the fourth moment is dominated by one or two observations, and the value will change dramatically if those observations are altered or removed. Reporting a kurtosis computed from such data as though it were a stable property of the population is a mistake.

### 5.2 The moment problem

Even when every moment exists, the sequence of moments does not always determine the distribution. Two different distributions can share all their moments, a phenomenon known as the moment problem. The uniqueness statement quoted in Section 2.8 requires the additional assumption that the moment generating function exists in a neighbourhood of zero, which rules out the pathological cases. For the descriptive purposes of this topic the distinction rarely matters, but it is the reason textbooks are careful to say that a distribution is determined by its moments only under a growth condition.

### 5.3 Grouping and the Sheppard correction

When continuous data are grouped, each observation is replaced by a class mark, which introduces a rounding error of up to half a class width. If the underlying distribution is smooth and the classes are of equal width $c$, the variance computed from class marks exceeds the true variance by approximately $c^{2}/12$. The corrected variance is therefore

$$
s^{2}_{\text{corrected}} = s^{2}_{\text{grouped}} - \frac{c^{2}}{12} .
$$

The correction is small when the class width is small relative to the standard deviation and substantial when the classes are coarse. Higher moments have analogous but more complicated corrections, and they are rarely applied by hand. In an examination the grouped moments are reported uncorrected, because the grouped distribution is the data; the correction belongs to the interpretation of data that were grouped from a finer original record.

### 5.4 Sample moments and their bias

The moments defined in this topic divide by $n$ and describe the data in hand. When the same formulas are applied to a sample in order to estimate population moments, the estimators are biased. The variance estimator with divisor $n$ underestimates the population variance on average by the factor $\left(n-1\right)/n$, which is why the divisor $n-1$ is used for estimation. The bias of the third and fourth moment estimators is more complicated and depends on the population values themselves.

The sampling variability of the standardised coefficients is also large. For a normal population the sample coefficient of skewness has standard error approximately $\sqrt{6/n}$, and the sample excess kurtosis has standard error approximately $\sqrt{24/n}$. With a hundred observations these are about $0.245$ and $0.490$, so small computed values of either coefficient are entirely consistent with normality.

### 5.5 Extensions: cumulants, additivity and the normal distribution

The cumulants introduced in Section 2.9 are the natural language for combining distributions. Because the moment generating function of a sum of independent variables is the product of the individual functions, the cumulant generating function of a sum is the sum of the individual cumulant generating functions, and therefore the cumulants add. Moments do not add in this simple way, since the second moment of a sum includes twice the covariance.

The normal distribution is the unique distribution whose cumulants of order three and above all vanish. That single fact explains why the normal curve is the reference for kurtosis: it has no shape information beyond its mean and variance, so any departure of $\gamma_2$ from zero is evidence of structure that the first two moments cannot describe.

### 5.6 Common errors and how to avoid them

- Dividing by the number of classes instead of the total frequency. The divisor is $n = \sum f_i$ in every formula, including the coded ones.
- Confusing $m_r$ with $m_r'$. The prime marks an assumed origin; substituting a working moment into a shape coefficient produces a number that depends on the arbitrary choice of origin and is therefore meaningless.
- Applying the conversion identities in the wrong order. Each identity uses earlier ones, so the computation proceeds from $m_1'$ upwards.
- Omitting the combination of like terms. The third identity ends in $2\left(m_1'\right)^{3}$ and the fourth in $-3\left(m_1'\right)^{4}$; writing $1$ and $-4$ instead are the two classic errors.
- Forgetting the powers of the class width. Coded central moments must be multiplied by $c^{2}$, $c^{3}$ and $c^{4}$ for the second, third and fourth moments respectively.
- Adding the correction in the second identity instead of subtracting it. A variance larger than the uncorrected second moment is impossible.
- Reporting a negative second moment or a negative fourth moment. Both are averages of even powers and cannot be negative.
- Reporting a negative $\beta_1$. It is a square; the direction belongs to $\gamma_1$ or to $m_3$.
- Comparing $\beta_2$ with zero. The comparison is with three, unless the excess form has already been computed.
- Treating a quoted quadruple of moments as necessarily realisable. Real moments satisfy $\beta_2 \ge 1$ and $\beta_2 \ge \beta_1 + 1$, and a quoted set that violates either condition is not the moment set of any data.
- Forgetting that the first central moment must be zero. A non-zero value signals an arithmetic slip in the table, and every later moment inherits the error.
- Using class limits rather than class boundaries when computing class marks. A class written as 3–7 for continuous data covers the boundaries 2.5 to 7.5, so its mark is 5 and its width is 5; using the limits instead of the boundaries shifts every mark and changes both the mean and the higher moments.
