## 1. Foundational Concepts, Definitions, and Axioms

### 1.1 Dispersion as a property of a data set

A measure of central tendency reduces a set of observations to a single representative value. It answers the question "where does the bulk of the data lie?" and nothing more. Two data sets may share a mean, a median and even a mode, and still differ in every respect that matters to a decision-maker: one may be tightly clustered and the other widely scattered. The property that separates them is dispersion, and a measure of dispersion is a number that quantifies how far the observations depart from a representative central value.

Formally, a measure of dispersion is a functional of the sample, that is, a rule that assigns a single non-negative real number to every finite set of observations, with the property that the number is zero exactly when all observations coincide and increases as the observations move apart in a suitable sense. Several such functionals are in common use, and they differ in how they aggregate the departures: some look only at the extremes, some at a central portion, some at every observation with signs removed, and some at every observation after squaring.

The distinction between absolute and relative measures organises the whole topic.

> **Definition (Absolute measure of dispersion).** An absolute measure of dispersion is expressed in the same units as the observations, or in the square of those units. The range, the interquartile range, the quartile deviation, the mean absolute deviation, the standard deviation and the variance are absolute measures.

> **Definition (Relative measure of dispersion).** A relative measure of dispersion is a ratio of two quantities carrying the same units, and is therefore dimensionless. It permits comparison of variability between data sets measured in different units or standing at very different levels. The coefficient of range, the coefficient of quartile deviation and the coefficient of variation are relative measures.

### 1.2 Notation and the two divisor conventions

Let $x_1, x_2, \dots, x_n$ denote $n$ observations of a variable $X$, and let

$$
\bar{x} = \frac{1}{n}\sum_{i=1}^{n} x_i
$$

denote their arithmetic mean. When the data are summarised by frequencies, let the distinct values be $x_1, \dots, x_k$ with frequencies $f_1, \dots, f_k$ and total $n = \sum_{i=1}^{k} f_i$. For grouped data the values $x_j$ are replaced by class marks $m_j$ and $f_j$ is the class frequency. In every formula below, the divisor is the total number of observations $n$, so the quantities defined are the descriptive variance and standard deviation of the data in hand.

A different convention divides the sum of squared deviations by $n-1$ and is used when the data are regarded as a sample from a larger population and the aim is to estimate the population variance without bias. That estimator is written

$$
s_{n-1}^{2} = \frac{1}{n-1}\sum_{i=1}^{n}\left(x_i - \bar{x}\right)^2
$$

and differs from the descriptive variance by the factor $\frac{n}{n-1}$, which exceeds one. The two conventions answer different questions: the descriptive quantity describes the spread of the observations actually measured, while the estimator attempts to describe the spread of a population from which they were drawn. This topic works with the descriptive convention throughout; the estimator is discussed again in Section 5 so that the difference is not confused with an error.

### 1.3 The range

> **Definition (Range).** Let $x_g = \max\left(x_1, \dots, x_n\right)$ and $x_l = \min\left(x_1, \dots, x_n\right)$. The range is $R = x_g - x_l$.

The range is a function of the two extreme order statistics only. It is the width of the smallest interval that contains all the data, which makes it the most direct possible statement of how far the data stretch. Its statistical weakness is that its breakdown point is zero: replacing a single observation by an arbitrarily large value makes the range arbitrarily large, no matter how many observations there are. It therefore has no resistance to contamination and is unsuitable whenever recording errors or genuine outliers may be present.

> **Definition (Coefficient of range).** The coefficient of range is $\frac{x_g - x_l}{x_g + x_l}$.

The denominator is the sum of the extremes rather than, for instance, the mean, because it guarantees a denominator that is positive whenever the data are non-negative and that is zero only in the degenerate case where both extremes vanish. The coefficient lies between $0$ and $1$ for non-negative data, equals $0$ only when all observations are equal, and approaches $1$ as the smallest observation becomes negligible compared with the largest.

### 1.4 Quantiles, the interquartile range and the quartile deviation

> **Definition (Quantiles).** For $0 < p < 1$, the $p$-quantile of a data set is a value $Q(p)$ such that a proportion $p$ of the observations lie at or below it. The median is $Q(0.5)$, the first quartile is $Q_1 = Q(0.25)$, the third quartile is $Q_3 = Q(0.75)$, and the $p$-th percentile is $Q(p/100)$.

> **Definition (Interquartile range and quartile deviation).** The interquartile range is $IQR = Q_3 - Q_1$. The quartile deviation, also called the semi-interquartile range, is $Q = \frac{1}{2}\left(Q_3 - Q_1\right)$.

> **Definition (Coefficient of quartile deviation).** The coefficient of quartile deviation is $\frac{Q_3 - Q_1}{Q_3 + Q_1}$.

The quartile deviation is the half-width of the interval containing the middle half of the observations. Because $Q_1$ and $Q_3$ are order statistics at fixed ranks rather than at the extremes, the quartile deviation has a positive breakdown point: up to roughly a quarter of the observations may be replaced by arbitrary values without moving $Q_1$ or $Q_3$ at all. This is the property that makes it the preferred measure for skewed distributions and for data containing extreme values.

The price paid for that resistance is a complete blindness to the tails. Two data sets with identical quartiles may differ enormously in their largest and smallest values, and the quartile deviation will report them as equally dispersed.

### 1.5 The mean absolute deviation

> **Definition (Mean absolute deviation).** The mean absolute deviation of $n$ observations about a constant $c$ is $\frac{1}{n}\sum_{i=1}^{n}\left|x_i - c\right|$. When $c = \bar{x}$ the quantity is the mean absolute deviation about the mean, and when $c = Q_2$ it is the mean absolute deviation about the median.

The absolute value is the device that prevents the algebraic cancellation which destroys any attempt to average signed deviations. The resulting measure is in the original units, is easy to explain, and is less sensitive to extreme values than the standard deviation because it does not square. It is nevertheless harder to handle algebraically: the absolute value function is not differentiable at zero, so the mean absolute deviation does not decompose as cleanly as the variance when data sets are combined or transformed.

### 1.6 The variance and the standard deviation

> **Definition (Variance).** The variance of $n$ observations is

$$
s^2 = \frac{1}{n}\sum_{i=1}^{n}\left(x_i - \bar{x}\right)^2
$$

and for frequency data with $n = \sum_{i=1}^{k} f_i$ it is

$$
s^2 = \frac{1}{n}\sum_{i=1}^{k} f_i\left(x_i - \bar{x}\right)^2 .
$$

> **Definition (Standard deviation).** The standard deviation is the non-negative square root of the variance, $s = \sqrt{s^2}$.

The variance is the mean of the squared deviations. Squaring serves three purposes simultaneously: it removes the sign of each deviation so that no cancellation occurs; it makes the function differentiable everywhere, which is what allows the decomposition theorems of Section 2; and it gives large deviations disproportionately large weight, which is desirable when large errors are disproportionately costly. The standard deviation restores the original units, since the square root of a mean of squared quantities measured in units of $X$ is measured in units of $X$.

The variance is not, in general, the square of a typical deviation. It is the mean of the squared deviations, and by Jensen's inequality the mean of the squares is at least the square of the mean absolute deviation, with equality only in the degenerate case of constant data. This is why the standard deviation always exceeds the mean absolute deviation unless all observations coincide.

### 1.7 The coefficient of variation

> **Definition (Coefficient of variation).** For data with mean $\bar{x} \ne 0$, the coefficient of variation is

$$
C.V = \frac{s}{\bar{x}} \times 100\% .
$$

The coefficient of variation expresses the standard deviation as a percentage of the mean. It is the natural measure of relative dispersion for data measured on a ratio scale, because on such a scale the ratio of two observations is meaningful and the ratio of the spread to the level is therefore meaningful. It is not meaningful on an interval scale with an arbitrary zero, since the value of $\bar{x}$ depends on the choice of zero and hence so does the coefficient. For that reason a coefficient of variation computed from temperatures in degrees Celsius is not comparable with one computed from the same temperatures in degrees Fahrenheit, while a coefficient computed from masses in kilograms is identical to one computed from the same masses in pounds.

### 1.8 Moments about an origin and about the mean

> **Definition (Second moment about an origin).** For a constant $A$, the second moment of the observations about $A$ is $m_2(A) = \frac{1}{n}\sum_{i=1}^{n}\left(x_i - A\right)^2$.

> **Definition (Second moment about the mean).** Taking $A = \bar{x}$ gives the second moment about the mean, $\mu_2 = \frac{1}{n}\sum_{i=1}^{n}\left(x_i - \bar{x}\right)^2$, which is precisely the variance.

The two quantities differ by the squared distance between $A$ and the mean, and the exact relationship is the subject of Section 2.4. This single identity underlies the computational formula, the assumed-mean method, the coding method and the shortcut formula for grouped data, so it is worth treating as the central result of the topic rather than as a computational trick.

### 1.9 Grouped data and its vocabulary

Grouped data require their own vocabulary because several formulas depend on precise definitions.

- A **class interval** is a symbol defining a class, for example $10\text{–}19$.
- The numbers $10$ and $19$ are the **class limits**, the lower limit and the upper limit respectively.
- The **class boundaries** are the true dividing lines between adjacent classes. For integer data recorded to the nearest unit, the boundaries are $9.5$ and $19.5$.
- The **class width** is the difference between the upper and lower boundaries, $h = 19.5 - 9.5 = 10$, and not the difference between the limits.
- The **class mark** is the midpoint of the class, $m = \frac{1}{2}\left(9.5 + 19.5\right) = 14.5$, which is the representative value substituted for every observation in the class.
- The **cumulative frequency** of a class is the number of observations in that class and all lower classes, and is the quantity used to locate quantiles.

When the classes have a common width $h$ and marks forming an arithmetic progression with common difference $h$, the coded values $u_j = \frac{m_j - A}{h}$ are consecutive integers, which is what makes the coding method so economical.

### 1.10 Classification of the measures

| Measure | Absolute or relative | Units | Uses every observation | Breakdown behaviour |
|---|---|---|---|---|
| Range | Absolute | Original | No, two values | Zero breakdown point |
| Interquartile range | Absolute | Original | No, middle half only | Ignores up to a quarter of the data |
| Quartile deviation | Absolute | Original | No, middle half only | Ignores up to a quarter of the data |
| Mean absolute deviation | Absolute | Original | Yes | Bounded influence |
| Variance | Absolute | Squared | Yes | Unbounded influence |
| Standard deviation | Absolute | Original | Yes | Unbounded influence |
| Coefficient of range | Relative | None | No | Zero breakdown point |
| Coefficient of quartile deviation | Relative | None | No | Ignores up to a quarter |
| Coefficient of variation | Relative | None | Yes | Unbounded influence |

## 2. Theorems, Lemmas, and Analytical Properties

### 2.1 The zero-sum lemma

> **Lemma (Deviations from the mean sum to zero).** For any observations with mean $\bar{x}$, $\sum_{i=1}^{n}\left(x_i - \bar{x}\right) = 0$.

The lemma is proved in Section 3.1. Its consequence is structural rather than numerical: any measure built by averaging the signed deviations is identically zero and therefore carries no information. Every genuine measure of dispersion must therefore apply a non-negative transformation to the deviations before averaging, which is exactly what the absolute value and the square do.

### 2.2 The mean as the minimiser of squared error

> **Theorem (Minimum squared error).** The function $g(c) = \sum_{i=1}^{n}\left(x_i - c\right)^2$ attains its unique minimum over the real line at $c = \bar{x}$, and the minimum value is $n s^2$.

This theorem gives the variance a variational interpretation: it is the smallest possible average squared distance from the data to any single point, and the point achieving it is the mean. The variance can therefore be described without reference to the mean at all, as the minimum average squared deviation, which is often the more illuminating description.

The analogous statement for absolute deviations is weaker: the sum $\sum_{i=1}^{n}\left|x_i - c\right|$ is minimised at any median of the data, and the minimiser need not be unique. When $n$ is odd the median is unique and the minimum is attained there; when $n$ is even every value between the two central order statistics attains the same minimum.

### 2.3 The computational formula

> **Theorem (Second moment identity).** For any constant $A$,
>
> $$m_2(A) = s^2 + \left(\bar{x} - A\right)^2$$

Equivalently, $s^2 = m_2(A) - \left(\bar{x} - A\right)^2$. Three special cases carry most of the practical weight.

- Setting $A = 0$ gives $s^2 = \frac{1}{n}\sum_{i=1}^{n} x_i^2 - \bar{x}^2$, the computational formula: the mean of the squares minus the square of the mean.
- Setting $A$ equal to a convenient round value gives the assumed-mean method, in which the arithmetic involves small deviations instead of large observations.
- Setting $A = \bar{x}$ returns the definition, since the second term vanishes.

For frequency data the identity reads $s^2 = \frac{1}{n}\sum_{j=1}^{k} f_j\left(m_j - A\right)^2 - \left(\bar{x} - A\right)^2$, and the coded form with $u_j = \frac{m_j - A}{h}$ is $s_x^2 = h^2\left[\frac{1}{n}\sum_{j=1}^{k} f_j u_j^2 - \bar{u}^2\right]$.

### 2.4 The linear transformation theorem

> **Theorem (Affine transformations).** If $y_i = a + b x_i$ for constants $a$ and $b$, then $\bar{y} = a + b\bar{x}$, $s_y^2 = b^2 s_x^2$, $s_y = \left|b\right| s_x$, $R_y = \left|b\right| R_x$ and $Q_y = \left|b\right| Q_x$.

The theorem separates the two operations. Translation, controlled by $a$, moves the centre and leaves every measure of spread untouched. Scaling, controlled by $b$, multiplies every measure of spread by the size of the factor and every measure of spread in squared units by the square of the factor. The absolute value appears because all measures of dispersion are non-negative and because a negative $b$ reverses the order of the data without changing its width.

The coefficient of variation does not obey a rule of this simple form. Under $y = a + bx$ with $b > 0$ the coefficient becomes $\frac{b s_x}{a + b\bar{x}} \times 100\%$, which equals the original only when $a = 0$. Relative dispersion is therefore invariant under change of unit but not under change of origin.

### 2.5 The combined variance decomposition

> **Theorem (Pooling decomposition).** Let two groups have sizes $n_1, n_2$, means $\bar{x}_1, \bar{x}_2$ and variances $s_1^2, s_2^2$, and let $\bar{x} = \frac{n_1\bar{x}_1 + n_2\bar{x}_2}{n_1 + n_2}$. Then the variance of the pooled data is
>
> $$s^2 = \frac{n_1\left[s_1^2 + \left(\bar{x}_1 - \bar{x}\right)^2\right] + n_2\left[s_2^2 + \left(\bar{x}_2 - \bar{x}\right)^2\right]}{n_1 + n_2}$$

The numerator is the total sum of squares about the pooled mean, decomposed into a within-group part $n_1 s_1^2 + n_2 s_2^2$ and a between-group part $n_1\left(\bar{x}_1 - \bar{x}\right)^2 + n_2\left(\bar{x}_2 - \bar{x}\right)^2$. The decomposition is exact and exhaustive: no residual term survives. Written in general form for $k$ groups,

$$
\sum_{j=1}^{k}\sum_{i=1}^{n_j}\left(x_{ji} - \bar{x}\right)^2 = \sum_{j=1}^{k} n_j s_j^2 + \sum_{j=1}^{k} n_j\left(\bar{x}_j - \bar{x}\right)^2 ,
$$

which is the elementary form of the analysis-of-variance identity: total variation equals variation within groups plus variation between groups.

Two corollaries are worth stating separately. First, if all group means are equal then the between-group term vanishes and the pooled variance is the size-weighted average of the group variances. Second, if the group means differ, the pooled variance always exceeds that weighted average, and the excess can be arbitrarily large.

### 2.6 The mean absolute deviation is bounded by the standard deviation

> **Theorem (Comparison of absolute and squared aggregation).** For any observations, $\frac{1}{n}\sum_{i=1}^{n}\left|x_i - \bar{x}\right| \le s$, with equality if and only if all deviations have the same absolute value.

The inequality is an instance of the Cauchy–Schwarz inequality, or equivalently of Jensen's inequality applied to the convex function $t \mapsto t^2$. Its practical content is that the two measures never contradict one another about which of two data sets is more dispersed in the same units, but they do not agree numerically, and the standard deviation is always at least as large.

### 2.7 Vanishing dispersion characterises constant data

> **Theorem (Vanishing criterion).** For observations $x_1, \dots, x_n$ with mean $\bar{x}$, the following are equivalent: (i) all observations are equal; (ii) $s^2 = 0$; (iii) $s = 0$; (iv) the mean absolute deviation about the mean is zero; (v) $R = 0$; (vi) $Q_3 - Q_1 = 0$.

The proof, given in Section 3.9, rests on the fact that each measure is a sum or a maximum of non-negative terms, and a sum of non-negative terms vanishes only when every term vanishes. The theorem matters because it identifies what a zero dispersion actually certifies: perfect homogeneity, and nothing weaker. A very small but non-zero dispersion certifies near-homogeneity, and the two cases must not be conflated in interpretation.

### 2.8 The standard deviation is bounded by half the range

> **Lemma (Popoviciu's inequality).** For observations lying between a minimum $x_l$ and a maximum $x_g$, the variance satisfies $s^2 \le \frac{1}{4}\left(x_g - x_l\right)^2$, and therefore $s \le \frac{1}{2}R$.

The bound is attained in the limiting case where half the observations sit at the minimum and half at the maximum. It is a useful sanity check: a computed standard deviation exceeding half the range is arithmetically impossible and signals an error in the working.

### 2.9 The mean absolute deviation is minimised at the median

> **Lemma (Optimality of the median for absolute error).** The function $h(c) = \sum_{i=1}^{n}\left|x_i - c\right|$ is minimised at any median of the data.

Together with the theorem of Section 2.2 this gives a complete picture of why two different centres appear in the topic. The mean minimises squared error and is therefore the natural centre for the variance and standard deviation; the median minimises absolute error and is therefore the natural centre for the mean absolute deviation and for the quartile-based measures.

### 2.10 Grouped data underestimate the true variance

> **Theorem (Grouping error for the variance).** Let the observations in class $j$ have mean $\mu_j$ and variance $\sigma_j^2$, and let $m_j$ be the class mark. Then the true variance of the raw observations equals the grouped variance computed from the class marks plus the frequency-weighted average of the within-class variances:
>
> $$s_{\text{true}}^2 = s_{\text{grouped}}^2 + \frac{1}{n}\sum_{j=1}^{k} f_j\left[\sigma_j^2 + \left(\mu_j - m_j\right)^2\right]$$

Because the added term is a weighted average of non-negative quantities, the grouped variance never exceeds the true variance. The discrepancy is small when the classes are narrow and the observations are roughly uniformly spread within each class, and it can be corrected approximately by subtracting $\frac{h^2}{12}$ from the grouped variance, a correction attributed to Sheppard. The correction assumes that the underlying distribution is smooth and that the classes are of equal width, and it should not be applied to heavily skewed data or to distributions with spikes at the class marks.

## 3. Formal Proofs, Derivations, and Methods

### 3.1 Proof of the zero-sum lemma

Write the sum of deviations and split it using linearity of summation.

$$
\sum_{i=1}^{n}\left(x_i - \bar{x}\right) = \sum_{i=1}^{n} x_i - \sum_{i=1}^{n}\bar{x}
$$

By definition of the mean, $\sum_{i=1}^{n} x_i = n\bar{x}$, and the sum of the constant $\bar{x}$ taken $n$ times is $n\bar{x}$. Hence

$$
\sum_{i=1}^{n}\left(x_i - \bar{x}\right) = n\bar{x} - n\bar{x} = 0 .
$$

### 3.2 Proof that the mean minimises the sum of squared deviations

Define $g(c) = \sum_{i=1}^{n}\left(x_i - c\right)^2$ and expand each square.

$$
g(c) = \sum_{i=1}^{n} x_i^2 - 2c\sum_{i=1}^{n} x_i + nc^2
$$

This is a quadratic in $c$ with leading coefficient $n > 0$, so it is strictly convex and has a unique minimiser. Differentiating with respect to $c$,

$$
g'(c) = -2\sum_{i=1}^{n} x_i + 2nc
$$

and setting $g'(c) = 0$ gives $nc = \sum_{i=1}^{n} x_i$, that is $c = \bar{x}$. Since $g''(c) = 2n > 0$, the stationary point is the global minimum. Substituting $c = \bar{x}$ into $g$ recovers $n s^2$, which establishes the stated minimum value.

### 3.3 Derivation of the second moment identity

Start from the average squared distance from an arbitrary constant $A$ and write each deviation as a deviation from the mean plus a fixed gap.

$$
x_i - A = \left(x_i - \bar{x}\right) + \left(\bar{x} - A\right)
$$

Squaring and summing,

$$
\sum_{i=1}^{n}\left(x_i - A\right)^2 = \sum_{i=1}^{n}\left(x_i - \bar{x}\right)^2 + 2\left(\bar{x} - A\right)\sum_{i=1}^{n}\left(x_i - \bar{x}\right) + n\left(\bar{x} - A\right)^2 .
$$

The middle sum vanishes by the zero-sum lemma, so division by $n$ yields

$$
m_2(A) = s^2 + \left(\bar{x} - A\right)^2 .
$$

Setting $A = 0$ produces the computational formula immediately, since $m_2(0) = \frac{1}{n}\sum x_i^2$ and $\left(\bar{x} - 0\right)^2 = \bar{x}^2$.

### 3.4 Derivation of the coding formulas

Let $u_i = \frac{x_i - A}{h}$ with $h \ne 0$, so that $x_i = A + h u_i$. Averaging is linear, so

$$
\bar{x} = \frac{1}{n}\sum_{i=1}^{n}\left(A + h u_i\right) = A + h\bar{u} .
$$

Each deviation from the mean is $h$ times the corresponding coded deviation.

$$
x_i - \bar{x} = \left(A + h u_i\right) - \left(A + h\bar{u}\right) = h\left(u_i - \bar{u}\right)
$$

Squaring and averaging multiplies the coded variance by $h^2$.

$$
s_x^2 = \frac{1}{n}\sum_{i=1}^{n} h^2\left(u_i - \bar{u}\right)^2 = h^2 s_u^2
$$

Combining this with the computational formula for the coded values gives the working form used for grouped data.

$$
s_x^2 = h^2\left[\frac{1}{n}\sum_{j=1}^{k} f_j u_j^2 - \bar{u}^2\right]
$$

### 3.5 Proof of the linear transformation theorem

For $y_i = a + b x_i$, linearity of averaging gives $\bar{y} = a + b\bar{x}$, and subtracting the two identities gives $y_i - \bar{y} = b\left(x_i - \bar{x}\right)$. Squaring and averaging,

$$
s_y^2 = b^2 \cdot \frac{1}{n}\sum_{i=1}^{n}\left(x_i - \bar{x}\right)^2 = b^2 s_x^2 .
$$

Taking non-negative square roots gives $s_y = \left|b\right| s_x$. For the range, the transformation is monotone when $b > 0$, so the extremes map to the extremes and $R_y = b R_x$; when $b < 0$ the order is reversed, so the greatest maps to the least and $R_y = -b R_x$. In either case $R_y = \left|b\right| R_x$. The same monotonicity argument applies to order statistics, so every quantile transforms as $Q_y(p) = a + b Q_x(p)$ when $b > 0$, and therefore $Q_y = \left|b\right| Q_x$.

### 3.6 Derivation of the pooled variance for two groups

Write the total sum of squares about the pooled mean and split it by group.

$$
\sum_{i=1}^{n_1}\left(x_{1i} - \bar{x}\right)^2 + \sum_{i=1}^{n_2}\left(x_{2i} - \bar{x}\right)^2
$$

For the first group, insert and subtract its own mean inside the bracket.

$$
\left(x_{1i} - \bar{x}\right) = \left(x_{1i} - \bar{x}_1\right) + \left(\bar{x}_1 - \bar{x}\right)
$$

Squaring the right-hand side and summing term by term,

$$
\sum_{i=1}^{n_1}\left(x_{1i} - \bar{x}\right)^2 = \sum_{i=1}^{n_1}\left(x_{1i} - \bar{x}_1\right)^2 + 2\left(\bar{x}_1 - \bar{x}\right)\sum_{i=1}^{n_1}\left(x_{1i} - \bar{x}_1\right) + n_1\left(\bar{x}_1 - \bar{x}\right)^2 .
$$

The first sum is $n_1 s_1^2$ by definition and the middle sum is zero by the zero-sum lemma, so

$$
\sum_{i=1}^{n_1}\left(x_{1i} - \bar{x}\right)^2 = n_1\left[s_1^2 + \left(\bar{x}_1 - \bar{x}\right)^2\right] .
$$

Repeating the computation for the second group and dividing the total by $n_1 + n_2$ gives the pooled variance. The extension to $k$ groups is immediate because the argument never used the number of groups.

### 3.7 Proof that the mean absolute deviation is at most the standard deviation

Let $d_i = x_i - \bar{x}$ and apply the Cauchy–Schwarz inequality to the vectors $\left(\left|d_1\right|, \dots, \left|d_n\right|\right)$ and $\left(1, \dots, 1\right)$.

$$
\sum_{i=1}^{n}\left|d_i\right| \le \left(\sum_{i=1}^{n} d_i^2\right)^{\frac{1}{2}}\left(\sum_{i=1}^{n} 1\right)^{\frac{1}{2}}
$$

Dividing both sides by $n$,

$$
\frac{1}{n}\sum_{i=1}^{n}\left|d_i\right| \le \left(\frac{1}{n}\sum_{i=1}^{n} d_i^2\right)^{\frac{1}{2}} = s .
$$

Equality in Cauchy–Schwarz holds exactly when the two vectors are proportional, which here means that all $\left|d_i\right|$ are equal. This is the promised equality condition.

### 3.8 Proof of Popoviciu's inequality

Suppose all observations lie in the interval with endpoints $x_l$ and $x_g$. For every observation, $\left(x_i - x_l\right)\left(x_g - x_i\right) \ge 0$ because both factors are non-negative. Summing and dividing by $n$,

$$
\frac{1}{n}\sum_{i=1}^{n}\left[\left(x_l + x_g\right)x_i - x_i^2 - x_l x_g\right] \ge 0 .
$$

Using linearity and writing $S = x_l + x_g$,

$$
S\bar{x} - \frac{1}{n}\sum_{i=1}^{n} x_i^2 - x_l x_g \ge 0 .
$$

Since $\frac{1}{n}\sum x_i^2 = s^2 + \bar{x}^2$, substitution gives

$$
s^2 \le S\bar{x} - x_l x_g - \bar{x}^2 = \left(\bar{x} - x_l\right)\left(x_g - \bar{x}\right) .
$$

The right-hand side is a product of two non-negative numbers whose sum is the range, and such a product is maximised when the two factors are equal, giving $\left(\bar{x} - x_l\right)\left(x_g - \bar{x}\right) \le \frac{1}{4}\left(x_g - x_l\right)^2$. Hence $s^2 \le \frac{1}{4}R^2$, which is the stated bound.

### 3.9 Proof that vanishing dispersion characterises constant data

Suppose first that $s^2 = 0$. Then $\frac{1}{n}\sum_{i=1}^{n}\left(x_i - \bar{x}\right)^2 = 0$ is a sum of non-negative terms equal to zero, so each term vanishes, giving $x_i = \bar{x}$ for every $i$. Hence all observations are equal, and each of the other measures is zero because every deviation is zero, every absolute deviation is zero, the range is zero and the two quartiles coincide.

Conversely, if all observations equal a common value $c$, then $\bar{x} = c$ and every deviation vanishes, so $s^2 = 0$, $s = 0$, the mean absolute deviation is zero, the range is zero and $Q_3 = Q_1$. This closes the chain of equivalences.

The proof also shows why a small numerical value must not be read as exact homogeneity. Rounding can produce a zero variance for data that are merely almost equal, and floating-point arithmetic can produce a tiny positive variance for data that are exactly equal. In both cases the theorem is a statement about exact arithmetic, and the interpretation must take the precision of the data into account.

### 3.10 Proof of scaling invariance of the coefficient of variation

Let $y_i = b x_i$ with $b > 0$. Then $\bar{y} = b\bar{x}$ and $s_y = b s_x$, so

$$
\frac{s_y}{\bar{y}} = \frac{b s_x}{b\bar{x}} = \frac{s_x}{\bar{x}} .
$$

The factor cancels, so the coefficient of variation is unchanged. If instead $y_i = a + b x_i$ with $a \ne 0$, then

$$
\frac{s_y}{\bar{y}} = \frac{\left|b\right| s_x}{a + b\bar{x}} ,
$$

which differs from the original because the translation has changed the denominator without changing the numerator. This is the formal reason that relative dispersion is meaningful only on a scale whose zero is fixed by the nature of the variable.

### 3.11 Method: variance and standard deviation of grouped data by coding

1. Verify that the classes have a common width $h$; otherwise use the direct method with class marks.
2. Compute each class mark $m_j$ as the average of the class boundaries.
3. Select an assumed mean $A$ equal to a central class mark, and record $h$.
4. Compute the coded values $u_j = \frac{m_j - A}{h}$ and check that they are consecutive integers.
5. Build the table of columns $f_j$, $u_j$, $f_j u_j$ and $f_j u_j^2$, and total each column.
6. Compute $\bar{u} = \frac{1}{n}\sum f_j u_j$ and $s_u^2 = \frac{1}{n}\sum f_j u_j^2 - \bar{u}^2$.
7. Convert with $\bar{x} = A + h\bar{u}$ and $s_x^2 = h^2 s_u^2$, then take the positive square root.
8. Check the answer against the bounds $0 \le s_x \le \frac{1}{2}R$ and against the magnitude of $h$.

### 3.12 Method: quantiles and quartile deviation for grouped data

1. Form the cumulative frequency column and verify that its last entry equals $n$.
2. Compute the target ranks $\frac{n}{4}$, $\frac{n}{2}$ and $\frac{3n}{4}$.
3. Identify for each target the class in which the cumulative frequency first reaches it.
4. Apply the interpolation formula $Q(p) = L + \frac{pn - F}{f}h$, where $L$ is the lower class boundary, $F$ the cumulative frequency below the class, $f$ the class frequency and $h$ the class width.
5. Verify the ordering $Q_1 \le Q_2 \le Q_3$ and that each lies inside its identified class.
6. Form the interquartile range, the quartile deviation and the coefficient.

### 3.13 Method: chaining transformations

When a variable is transformed more than once, the rules compose. If $y = a + bx$ and $z = c + dy$, then $z = \left(c + ad\right) + \left(bd\right)x$, so the mean transforms by the composite affine map and the standard deviation by the product of the absolute slopes.

$$
\bar{z} = c + d\bar{y} = c + d\left(a + b\bar{x}\right), \qquad s_z = \left|d\right|\left|b\right| s_x
$$

This composition rule is the fastest way to handle unit conversions that pass through an intermediate scale, such as converting a standard deviation in degrees Celsius into degrees Fahrenheit through the multiplication by $1.8$ and the addition of $32$.

## 4. Representative Worked Examples and Solutions

### 4.1 Problem: the second moment identity in action

For the five observations $5$, $7$, $9$, $11$ and $13$, compute the second moment about $A = 10$, and use the identity to obtain the variance and standard deviation.

### 4.2 Solution: compute the moment about the chosen origin, then subtract the squared gap

Step 1. Compute the mean.

$$
\bar{x} = \frac{5 + 7 + 9 + 11 + 13}{5} = \frac{45}{5} = 9
$$

Step 2. Form the deviations from $A = 10$ and square them.

$$
\left(-5\right)^2 = 25, \quad \left(-3\right)^2 = 9, \quad \left(-1\right)^2 = 1, \quad 1^2 = 1, \quad 3^2 = 9
$$

Step 3. Average the squared deviations to obtain the second moment about $A$.

$$
m_2(10) = \frac{25 + 9 + 1 + 1 + 9}{5} = \frac{45}{5} = 9
$$

Step 4. Compute the squared gap between the mean and the chosen origin.

$$
\left(\bar{x} - A\right)^2 = \left(9 - 10\right)^2 = 1
$$

Step 5. Subtract the squared gap to obtain the variance.

$$
s^2 = m_2(10) - \left(\bar{x} - A\right)^2 = 9 - 1 = 8
$$

Step 6. Verify from the definition, using deviations from the mean $-4$, $-2$, $0$, $2$ and $4$.

$$
s^2 = \frac{16 + 4 + 0 + 4 + 16}{5} = \frac{40}{5} = 8
$$

Step 7. Take the positive square root.

$$
s = \sqrt{8} \approx 2.83
$$

Step 8. Interpret. The average squared distance from the arbitrary point $10$ is $9$, while the average squared distance from the mean is only $8$; the difference of $1$ is exactly the squared distance from $10$ to the mean, confirming the identity numerically.

### 4.3 Problem: grouped data by location and scale changes

A distribution is given by the classes $5\text{–}9$, $10\text{–}14$, $15\text{–}19$, $20\text{–}24$, $25\text{–}29$ and $30\text{–}34$ with frequencies $3$, $4$, $6$, $5$, $4$ and $3$. Find the mean, variance and standard deviation by changing both the location, using $A = 17$, and the scale, using the common class width.

### 4.4 Solution: code the class marks, then restore the units

Step 1. Compute the class marks as midpoints of the class boundaries $4.5, 9.5, \dots, 34.5$, obtaining $7$, $12$, $17$, $22$, $27$ and $32$.

Step 2. Confirm the class width.

$$
h = 9.5 - 4.5 = 5
$$

Step 3. Compute the coded values $u = \frac{m - 17}{5}$, obtaining $-2$, $-1$, $0$, $1$, $2$ and $3$.

Step 4. Accumulate the four columns.

| Class | $m$ | $f$ | $u$ | $fu$ | $fu^2$ |
|---|---|---|---|---|---|
| $5\text{–}9$ | $7$ | $3$ | $-2$ | $-6$ | $12$ |
| $10\text{–}14$ | $12$ | $4$ | $-1$ | $-4$ | $4$ |
| $15\text{–}19$ | $17$ | $6$ | $0$ | $0$ | $0$ |
| $20\text{–}24$ | $22$ | $5$ | $1$ | $5$ | $5$ |
| $25\text{–}29$ | $27$ | $4$ | $2$ | $8$ | $16$ |
| $30\text{–}34$ | $32$ | $3$ | $3$ | $9$ | $27$ |
| Total | | $25$ | | $12$ | $64$ |

Step 5. Compute the coded mean.

$$
\bar{u} = \frac{12}{25} = 0.48
$$

Step 6. Restore the location.

$$
\bar{x} = 17 + 5\left(0.48\right) = 19.4
$$

Step 7. Compute the coded variance.

$$
s_u^2 = \frac{64}{25} - 0.48^2 = 2.56 - 0.2304 = 2.3296
$$

Step 8. Restore the scale.

$$
s_x^2 = 25\left(2.3296\right) = 58.24
$$

Step 9. Take the positive square root.

$$
s_x = \sqrt{58.24} \approx 7.63
$$

Step 10. Check against Popoviciu's bound. The range of the class marks is $32 - 7 = 25$, so the standard deviation cannot exceed $12.5$; the computed value of $7.63$ satisfies the bound, and it is about one and a half class widths.

### 4.5 Problem: the combined variance of three subgroups

Three subgroups of workers have the following summaries: subgroup A has $50$ workers with mean wage $61.0$ and standard deviation $8.0$; subgroup B has $100$ workers with mean wage $70.8$ and standard deviation $9.0$; subgroup C has $120$ workers with mean wage $80.5$ and standard deviation $10.0$. Find the mean and standard deviation of the whole group, and the coefficient of variation of each subgroup and of the whole group.

### 4.6 Solution: pool the means, then decompose the total sum of squares

Step 1. Sum the frequencies.

$$
n = 50 + 100 + 120 = 270
$$

Step 2. Compute the total of the group totals.

$$
\sum_{j=1}^{3} n_j\bar{x}_j = 50\left(61.0\right) + 100\left(70.8\right) + 120\left(80.5\right) = 3050 + 7080 + 9660 = 19790
$$

Step 3. Divide by the total number of workers.

$$
\bar{x} = \frac{19790}{270} \approx 73.296
$$

Step 4. Compute each group's gap from the combined mean.

$$
\bar{x}_1 - \bar{x} \approx 61.0 - 73.296 = -12.296
$$

$$
\bar{x}_2 - \bar{x} \approx 70.8 - 73.296 = -2.496
$$

$$
\bar{x}_3 - \bar{x} \approx 80.5 - 73.296 = 7.204
$$

Step 5. Square each gap and add the group's own variance.

$$
s_1^2 + \left(\bar{x}_1 - \bar{x}\right)^2 \approx 64 + 151.199 = 215.199
$$

$$
s_2^2 + \left(\bar{x}_2 - \bar{x}\right)^2 \approx 81 + 6.231 = 87.231
$$

$$
s_3^2 + \left(\bar{x}_3 - \bar{x}\right)^2 \approx 100 + 51.893 = 151.893
$$

Step 6. Weight each contribution by the group size.

$$
50\left(215.199\right) = 10759.95
$$

$$
100\left(87.231\right) = 8723.10
$$

$$
120\left(151.893\right) = 18227.16
$$

Step 7. Add the weighted contributions and divide by the total size.

$$
s^2 \approx \frac{10759.95 + 8723.10 + 18227.16}{270} = \frac{37710.21}{270} \approx 139.67
$$

Step 8. Take the positive square root.

$$
s \approx \sqrt{139.67} \approx 11.82
$$

Step 9. Compute the coefficient of variation for each subgroup.

$$
C.V_A = \frac{8.0}{61.0}\left(100\%\right) \approx 13.11\%
$$

$$
C.V_B = \frac{9.0}{70.8}\left(100\%\right) \approx 12.71\%
$$

$$
C.V_C = \frac{10.0}{80.5}\left(100\%\right) \approx 12.42\%
$$

Step 10. Compute the coefficient of variation for the whole group.

$$
C.V = \frac{11.82}{73.296}\left(100\%\right) \approx 16.12\%
$$

Step 11. Interpret. Each subgroup on its own is relatively homogeneous, with a coefficient of variation between twelve and thirteen per cent, yet the whole group is decidedly more heterogeneous at about sixteen per cent. The increase is not caused by any subgroup becoming more variable; it is caused entirely by the between-group term, since the three subgroup means differ by almost twenty currency units.

### 4.7 Problem: a change of scale and origin

A set of temperatures in degrees Celsius has mean $20$ and standard deviation $3$. Convert to degrees Fahrenheit using $F = 1.8C + 32$ and describe what happens to the centre, the spread and the relative spread.

### 4.8 Solution: apply the transformation theorem term by term

Step 1. Transform the mean using $\bar{F} = 1.8\bar{C} + 32$.

$$
\bar{F} = 1.8\left(20\right) + 32 = 36 + 32 = 68
$$

Step 2. Transform the standard deviation using $s_F = \left|1.8\right| s_C$, since the additive constant does not affect spread.

$$
s_F = 1.8\left(3\right) = 5.4
$$

Step 3. Transform the variance using the square of the factor.

$$
s_F^2 = 1.8^2\left(3^2\right) = 3.24\left(9\right) = 29.16
$$

Step 4. Compute the coefficient of variation on the Celsius scale.

$$
C.V_C = \frac{3}{20}\left(100\%\right) = 15\%
$$

Step 5. Compute the coefficient of variation on the Fahrenheit scale.

$$
C.V_F = \frac{5.4}{68}\left(100\%\right) \approx 7.94\%
$$

Step 6. Interpret. The two coefficients differ, so the coefficient of variation is not invariant under a change of origin. This is not an arithmetic error but a warning about the appropriate use of the measure: temperature on the Celsius and Fahrenheit scales has an arbitrary zero, so a ratio of spread to level has no physical meaning, and the coefficient should not be computed for such data at all.

### 4.9 Problem: comparing consistency with the coefficient of variation

Benny and Flora were graded in eleven subjects. Benny's scores were $3$, $11$, $12$, $10$, $12$, $10$, $4$, $10$, $2$, $0$ and $4$. Flora's scores were $6$, $10$, $10$, $4$, $4$, $5$, $8$, $9$, $1$, $6$ and $5$. Compute the coefficient of variation for each and decide who was the less consistent candidate.

### 4.10 Solution: two sets, two computational tables, one comparison

Step 1. Sum Benny's scores.

$$
\sum x = 3 + 11 + 12 + 10 + 12 + 10 + 4 + 10 + 2 + 0 + 4 = 78
$$

Step 2. Compute Benny's mean.

$$
\bar{x}_B = \frac{78}{11} \approx 7.091
$$

Step 3. Sum the squares of Benny's scores.

$$
\sum x^2 = 9 + 121 + 144 + 100 + 144 + 100 + 16 + 100 + 4 + 0 + 16 = 754
$$

Step 4. Apply the computational formula to Benny.

$$
s_B^2 = \frac{754}{11} - \left(\frac{78}{11}\right)^2 \approx 68.545 - 50.281 = 18.264
$$

$$
s_B \approx \sqrt{18.264} \approx 4.274
$$

Step 5. Sum Flora's scores and the squares of her scores.

$$
\sum x = 6 + 10 + 10 + 4 + 4 + 5 + 8 + 9 + 1 + 6 + 5 = 68
$$

$$
\sum x^2 = 36 + 100 + 100 + 16 + 16 + 25 + 64 + 81 + 1 + 36 + 25 = 500
$$

Step 6. Apply the computational formula to Flora.

$$
\bar{x}_F = \frac{68}{11} \approx 6.182
$$

$$
s_F^2 = \frac{500}{11} - \left(\frac{68}{11}\right)^2 \approx 45.455 - 38.215 = 7.240
$$

$$
s_F \approx \sqrt{7.240} \approx 2.691
$$

Step 7. Compute the two coefficients of variation.

$$
C.V_B = \frac{4.274}{7.091}\left(100\%\right) \approx 60.3\%
$$

$$
C.V_F = \frac{2.691}{6.182}\left(100\%\right) \approx 43.5\%
$$

Step 8. Compare and conclude. Benny's coefficient of variation exceeds Flora's, and his standard deviation is also larger in raw units, so the conclusion is unambiguous on either measure: Benny is the less consistent, less homogeneous candidate, and his marks are the more variable of the two sets.

### 4.11 Problem: the mean absolute deviation and its optimal centre

For the observations $2$, $3$, $5$, $8$ and $20$, compute the mean absolute deviation about the mean and about the median, and compute the standard deviation.

### 4.12 Solution: two centres, two absolute averages

Step 1. Compute the mean.

$$
\bar{x} = \frac{2 + 3 + 5 + 8 + 20}{5} = \frac{38}{5} = 7.6
$$

Step 2. Form the absolute deviations from the mean.

$$
\left|2 - 7.6\right| = 5.6, \quad \left|3 - 7.6\right| = 4.6, \quad \left|5 - 7.6\right| = 2.6, \quad \left|8 - 7.6\right| = 0.4, \quad \left|20 - 7.6\right| = 12.4
$$

Step 3. Average them.

$$
\frac{5.6 + 4.6 + 2.6 + 0.4 + 12.4}{5} = \frac{25.6}{5} = 5.12
$$

Step 4. Identify the median, which is the third value in the ordered list, namely $5$.

Step 5. Form the absolute deviations from the median and average them.

$$
\frac{3 + 2 + 0 + 3 + 15}{5} = \frac{23}{5} = 4.6
$$

Step 6. Compute the variance and standard deviation for comparison.

$$
s^2 = \frac{2^2 + 3^2 + 5^2 + 8^2 + 20^2}{5} - 7.6^2 = \frac{4 + 9 + 25 + 64 + 400}{5} - 57.76
$$

$$
s^2 = \frac{502}{5} - 57.76 = 100.4 - 57.76 = 42.64
$$

$$
s = \sqrt{42.64} \approx 6.53
$$

Step 7. Compare the three numbers. The mean absolute deviation about the median, $4.6$, is smaller than the mean absolute deviation about the mean, $5.12$, as the theory predicts, and both are below the standard deviation of $6.53$, which the Cauchy–Schwarz inequality requires. The gap between $6.53$ and $5.12$ is large because the single observation $20$ contributes $12.4$ to the absolute total but $153.76$ to the squared total.

### 4.13 Problem: correcting an erroneous observation

The mean and variance of twenty observations are $10$ and $4$ respectively. One observation was recorded as $8$ but its true value is $12$. Find the corrected mean, variance and standard deviation.

### 4.14 Solution: repair the two sufficient totals

Step 1. Recover the original total.

$$
\sum x = n\bar{x} = 20\left(10\right) = 200
$$

Step 2. Recover the original sum of squares from $\sum x^2 = n\left(s^2 + \bar{x}^2\right)$.

$$
\sum x^2 = 20\left(4 + 100\right) = 2080
$$

Step 3. Correct the total by removing the wrong value and inserting the right one.

$$
\sum x = 200 - 8 + 12 = 204
$$

Step 4. Correct the sum of squares in the same way.

$$
\sum x^2 = 2080 - 64 + 144 = 2160
$$

Step 5. Compute the corrected mean.

$$
\bar{x} = \frac{204}{20} = 10.2
$$

Step 6. Compute the corrected variance.

$$
s^2 = \frac{2160}{20} - 10.2^2 = 108 - 104.04 = 3.96
$$

Step 7. Take the positive square root.

$$
s = \sqrt{3.96} \approx 1.99
$$

Step 8. Interpret. The correction has raised the mean by $0.2$ and lowered the variance from $4$ to $3.96$, because the replacement value lies closer to the new mean than the erroneous one did to the old mean. The method works because the mean and variance together determine the two totals $\sum x$ and $\sum x^2$, and those totals can be repaired one observation at a time.

### 4.15 Problem: recovering the variance from a total

The mean of twenty numbers is $15$ and the sum of their squares is $4820$. Find the variance and the standard deviation.

### 4.16 Solution: substitute into the computational formula

Step 1. Compute the mean of the squares.

$$
\frac{1}{n}\sum_{i=1}^{20} x_i^2 = \frac{4820}{20} = 241
$$

Step 2. Square the mean.

$$
\bar{x}^2 = 15^2 = 225
$$

Step 3. Subtract.

$$
s^2 = 241 - 225 = 16
$$

Step 4. Take the positive square root.

$$
s = 4
$$

Step 5. Interpret. The average squared deviation is $16$ in squared units, so a typical observation lies about $4$ units from the mean of $15$. The answer is exact because no rounding was required at any stage.

### 4.17 Problem: quartile deviation of grouped data

The marks of $100$ candidates fall into the classes $10\text{–}20$, $20\text{–}30$, $30\text{–}40$, $40\text{–}50$, $50\text{–}60$, $60\text{–}70$ and $70\text{–}80$ with frequencies $8$, $14$, $22$, $26$, $16$, $10$ and $4$. Compute $Q_1$, $Q_3$, the quartile deviation and its coefficient.

### 4.18 Solution: locate, interpolate, then combine

Step 1. Build the cumulative frequencies: $8$, $22$, $44$, $70$, $86$, $96$ and $100$, which total $n = 100$.

Step 2. Fix the target ranks at $\frac{n}{4} = 25$ and $\frac{3n}{4} = 75$.

Step 3. Identify the first quartile class as $30\text{–}40$, since its cumulative frequency $44$ is the first to reach $25$.

Step 4. Interpolate with $L = 30$, $F = 22$, $f = 22$ and $h = 10$.

$$
Q_1 = 30 + \frac{25 - 22}{22}\left(10\right) = 30 + 1.364 \approx 31.36
$$

Step 5. Identify the third quartile class as $50\text{–}60$, since its cumulative frequency $86$ is the first to reach $75$.

Step 6. Interpolate with $L = 50$, $F = 70$, $f = 16$ and $h = 10$.

$$
Q_3 = 50 + \frac{75 - 70}{16}\left(10\right) = 50 + 3.125 = 53.125
$$

Step 7. Form the interquartile range and the quartile deviation.

$$
IQR = 53.125 - 31.364 = 21.761
$$

$$
Q = \frac{21.761}{2} \approx 10.88
$$

Step 8. Form the coefficient of quartile deviation.

$$
\frac{Q_3 - Q_1}{Q_3 + Q_1} = \frac{21.761}{84.489} \approx 0.258
$$

Step 9. Interpret. The middle half of the candidates spans about $21.8$ marks, so the half-width of that middle band is about $10.9$ marks and is about a quarter of the combined level of the two quartiles. Because the measure uses only the middle half, it is unaffected by the precise marks of the lowest and highest candidates.

## 5. Mathematical Extensions, Limits, and Common Errors

### 5.1 The divisor question: $n$ or $n-1$

The formulas in this topic divide by $n$, the number of observations. A different quantity, obtained by dividing by $n-1$, appears whenever the observations are treated as a sample from a larger population and the objective is an unbiased estimate of the population variance. The two are related by

$$
s_{n-1}^{2} = \frac{n}{n-1} s^{2} ,
$$

so the estimator is always the larger of the two and the difference matters most when $n$ is small. For $n = 10$ the factor is $\frac{10}{9}$, an increase of about eleven per cent; for $n = 100$ it is about one per cent. The choice is not a matter of taste but of purpose: describe the data in hand and divide by $n$; estimate the variance of a population and divide by $n-1$. A note on a data set that reports one divisor when the other was intended is arithmetically wrong, but a note that fails to say which convention it uses is merely ambiguous.

### 5.2 Grouping error and its correction

When data are grouped, the class mark stands in for every observation in its class, and the within-class variation is lost. The identity of Section 2.10 states that the true variance equals the grouped variance plus a non-negative weighted average of the within-class variances and the squared offsets of the within-class means from the marks. The grouped variance is therefore a lower bound, and the shortfall is bounded by the largest within-class variance, which cannot exceed $\frac{h^2}{4}$ for a class of width $h$.

If the observations are roughly uniformly spread within each class and the distribution is smooth, the shortfall is approximately $\frac{h^2}{12}$, which suggests the Sheppard correction

$$
s_{\text{corrected}}^2 \approx s_{\text{grouped}}^2 - \frac{h^2}{12} .
$$

The correction reduces the variance, and can in principle produce a negative value if it is applied to data whose grouped variance is already very small, which is one indication that it has been applied outside its intended conditions. It should not be used for heavily skewed distributions, for distributions with a spike at a class mark, or when the classes have unequal widths.

### 5.3 Limits of the measures and the meaning of robustness

The four absolute measures differ sharply in how they respond to contamination. The range has a breakdown point of zero, since one observation can move it without limit. The quartile deviation has a breakdown point of about one quarter, since replacing fewer than a quarter of the observations cannot move the quartiles past the replaced region. The mean absolute deviation and the standard deviation both have breakdown points of zero, because a single very large observation drives both to infinity, but their influence functions differ: the standard deviation weights a deviation by its own size, so the influence of an extreme observation grows without bound, whereas the mean absolute deviation weights every deviation equally in magnitude and grows only linearly.

That difference explains a familiar practical rule. When a data set is believed to be clean, the standard deviation is preferred, because it uses all the information and has the algebraic properties that make combination and transformation possible. When a data set may contain errors or genuine extremes, the quartile deviation or the mean absolute deviation is preferred, because the answer will not be dictated by a handful of values. The choice is a judgement about the data-generating process, not a mathematical preference.

A further limit concerns the interpretation of the standard deviation as a description of shape. The standard deviation says nothing about skewness, so two data sets with the same mean and the same standard deviation may have entirely different shapes. Statements of the form "about two thirds of the observations lie within one standard deviation of the mean" are exact only for the normal distribution and should not be asserted for arbitrary data. What can be asserted universally is Chebyshev's inequality, which guarantees that at least a proportion $1 - \frac{1}{t^2}$ of the observations lie within $t$ standard deviations of the mean for any $t > 1$, and Popoviciu's inequality, which bounds the standard deviation by half the range.

### 5.4 Units, scale types and the validity of relative measures

The absolute measures carry the units of the data, except the variance, which carries their square. The relative measures carry no units at all. Relative measures are legitimate only when the variable is measured on a ratio scale, that is, when the zero of the scale is fixed by the nature of the quantity so that ratios of values are meaningful. Mass, length, time, income and counts satisfy this condition. Temperature on the Celsius or Fahrenheit scale does not, because the zero is a convention, and a coefficient of variation computed from such data changes when the unit changes. The coefficient of variation is also unstable when the mean is close to zero, since a small change in the mean produces a large change in the ratio, and it is undefined when the mean is exactly zero.

### 5.5 Errors that recur in examinations

- **Dividing by the number of classes.** Every formula in this topic divides by the total frequency $n$, not by the number of rows $k$.
- **Using the wrong divisor for the wrong purpose.** Dividing by $n-1$ when a descriptive variance is requested, or by $n$ when an unbiased estimate is requested, is a conceptual error rather than a slip.
- **Computing the class width from limits.** For classes $10\text{–}19$ and $20\text{–}29$ the width is $10$; the difference between the limits, $9$, is not the width.
- **Using class limits instead of class marks.** Every product in a grouped computation uses the mark, not the limit.
- **Reversing the computational formula.** The variance is the mean of the squares minus the square of the mean; reversing the subtraction gives a negative variance.
- **Squaring the sum instead of the mean.** The quantity squared in the second term is $\bar{x}$, not $\sum x$.
- **Forgetting the square on the class width.** When restoring the scale of a coded variance the factor is $h^2$, not $h$.
- **Omitting the between-group term.** The pooled variance is not the weighted average of the group variances unless the group means coincide.
- **Confusing variance and standard deviation units.** A variance is in squared units and cannot be quoted in the units of the data.
- **Inverting the coefficient of variation.** The definition is $\frac{s}{\bar{x}}$, not $\frac{\bar{x}}{s}$.
- **Reading a larger coefficient of variation as greater consistency.** The interpretation runs the other way: larger coefficient, more variable.
- **Applying the coefficient of variation to interval-scale data.** A coefficient computed from temperatures is not comparable across scales.
- **Rounding the mean before squaring.** Carry at least four significant figures through the intermediate stages, because squaring amplifies a rounding error.
- **Treating a small variance as a zero variance.** Only exact equality of all observations makes the variance exactly zero.

### 5.6 Where the topic leads

The variance and the standard deviation are the entry point to a large part of what follows in statistics. The decomposition of total variation into within-group and between-group parts, proved here for two groups, is the algebraic foundation of the analysis of variance, where the same identity is used to test whether several group means could plausibly be equal. The standardisation implicit in the coefficient of variation, which divides a deviation by a measure of scale, reappears in the $z$-score $\frac{x - \bar{x}}{s}$ and hence in every normal-distribution calculation. The idea that a measure of dispersion should be a functional with desirable invariance properties reappears in the study of estimators, where the sampling variance of an estimator measures its precision in exactly the sense that the variance of a data set measures its spread.

The connection to risk is equally direct. In finance, the standard deviation of returns is the conventional measure of total risk, and the coefficient of variation is the conventional measure of risk per unit of expected return, which is why a portfolio with a larger standard deviation is not automatically judged riskier than one with a smaller standard deviation but a much smaller mean. The same logic applies in agriculture, where a variety with a higher mean yield and a higher standard deviation may still be preferred; in manufacturing, where a tolerance is a statement about an acceptable standard deviation; and in public health, where the variability of a measurement across clinics is as important as its average. In each case the question is the same one this topic answers: how far, typically, do the observations sit from the centre, and how should that distance be expressed so that it can be compared fairly with something else.
