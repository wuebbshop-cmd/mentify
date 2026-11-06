## 1. Foundational Concepts, Definitions, and Axioms

### 1.1 What the examiner is testing

Every question on this topic is a request for one of two things. Either it asks for a single number that describes how widely a set of observations spreads, or it asks you to compare two sets of observations and say which one is more stable relative to its own level. The first request is answered by an absolute measure of dispersion, the second by a relative measure. Almost all the marks on the topic come from four skills: selecting the right formula for the data format you have been given, executing that formula without arithmetic slips, converting between the raw, assumed-mean and coded routes, and writing one sentence that interprets the number in the context of the question. The theory behind the formulas is examined less often, but the identities linking them are favourites in the longer questions because they let a single two-mark step separate candidates who understand the structure from those who have memorised only the definition.

The whole topic therefore rewards a strategy: learn the small set of master formulas, learn the three algebraic identities that generate all the shortcuts, and practise the four data formats — raw list, frequency table, grouped frequency table, and summarised group statistics — until the first move in each is automatic.

### 1.2 The object of study

A measure of central tendency reduces a data set to one representative value. It answers where the data sit, and nothing else. Two data sets may share the same mean to the last decimal place and still differ in everything that matters operationally: one may be predictable and the other erratic. Dispersion is the property that separates them, and a measure of dispersion is a non-negative number that grows as the observations move away from a central value and equals zero exactly when every observation is identical.

> **Definition (Absolute measure of dispersion).** An absolute measure is expressed in the units of the observations, or in the square of those units. It changes if the units change. The range, the interquartile range, the quartile deviation, the mean absolute deviation, the variance and the standard deviation are absolute.

> **Definition (Relative measure of dispersion).** A relative measure is a ratio of two quantities carrying the same units and is therefore dimensionless. It is unchanged by a change of units. The coefficient of range, the coefficient of quartile deviation and the coefficient of variation are relative.

This absolute-relative split is the organising principle of every comparison question. A question that asks "which set is more variable" when the two sets are measured on the same scale can be answered with a standard deviation. A question that asks the same thing when one set is in shillings and the other in marks, or when the two means are far apart, can only be answered with a coefficient of variation. Choosing the wrong one is a reportable error, not a stylistic preference.

### 1.3 Notation fixed for the whole topic

Let $x_1, x_2, \dots, x_n$ be $n$ observations of a variable $X$ and let

$$
\bar{x} = \frac{1}{n}\sum_{i=1}^{n} x_i
$$

be their arithmetic mean. For frequency data let the distinct values be $x_1, \dots, x_k$ with frequencies $f_1, \dots, f_k$ and total frequency

$$
n = \sum_{i=1}^{k} f_i .
$$

For grouped data the value $x_i$ is replaced by the class mark $m_i$, which is the midpoint of the class, and $f_i$ is the class frequency. When a working variable is introduced by coding, it is written $u_i$ or $d_i$; when a general origin is used it is written $A$; when a class width is used it is written $h$ or $c$.

Every formula in this note divides the sum of squared deviations by $n$, the number of observations actually in hand. That is the descriptive convention and it is the one the examination uses unless a question explicitly says that the data are a sample from a larger population and asks for an unbiased estimate. In that one situation the divisor becomes $n-1$ and the estimate is written

$$
s_{n-1}^{2} = \frac{1}{n-1}\sum_{i=1}^{n}\left(x_i - \bar{x}\right)^{2} .
$$

The two conventions differ by the factor $\frac{n}{n-1}$, which is close to one for large $n$ and about $1.33$ for $n = 4$. Section 5 explains when each is legitimate so that the distinction is never mistaken for an arithmetic error.

### 1.4 The range and its coefficient

> **Definition (Range).** With $x_g = \max\left(x_1, \dots, x_n\right)$ and $x_l = \min\left(x_1, \dots, x_n\right)$, the range is $R = x_g - x_l$.

The range is the width of the narrowest interval containing all the observations. It is a function of two order statistics and nothing else, so a single misrecorded value can change it arbitrarily. Its breakdown point is zero: no matter how many observations there are, one contamination destroys it.

> **Definition (Coefficient of range).** The coefficient of range is

$$
\frac{x_g - x_l}{x_g + x_l} .
$$

The denominator is the sum of the extremes rather than a mean because it is guaranteed positive for non-negative data and vanishes only in the degenerate case where both extremes are zero. For non-negative data the coefficient lies between $0$ and $1$; it equals $0$ only when all observations coincide and tends to $1$ as the smaller extreme becomes negligible beside the larger. Being a ratio of two lengths, it is unit-free.

### 1.5 Quantiles, the interquartile range and the quartile deviation

> **Definition (Quantiles).** For $0 < p < 1$ the $p$-quantile $Q(p)$ is a value at or below which a proportion $p$ of the observations lie. The median is $Q(0.5)$, the lower quartile is $Q_1 = Q(0.25)$, the upper quartile is $Q_3 = Q(0.75)$, and the $p$-th percentile is $Q(p/100)$.

> **Definition (Interquartile range and quartile deviation).** The interquartile range is $IQR = Q_3 - Q_1$ and the quartile deviation is

$$
Q = \frac{1}{2}\left(Q_3 - Q_1\right) .
$$

> **Definition (Coefficient of quartile deviation).** The coefficient of quartile deviation is

$$
\frac{Q_3 - Q_1}{Q_3 + Q_1} .
$$

The quartile deviation is the half-width of the interval holding the middle half of the observations. Because $Q_1$ and $Q_3$ sit at fixed ranks rather than at the extremes, roughly a quarter of the data may be replaced by arbitrary values without moving either quartile. That positive breakdown point is why the measure is preferred for skewed data and for data suspected of containing outliers. The price is blindness in the tails: two data sets with identical quartiles may differ enormously in their largest and smallest values and will be reported as equally dispersed. Note also that the quartile deviation is not a mean of deviations, so it does not carry an interpretation as "average distance from the centre"; it is a half-width of a central interval.

### 1.6 The mean absolute deviation

> **Definition (Mean absolute deviation).** The mean absolute deviation of $n$ observations about a constant $c$ is

$$
\frac{1}{n}\sum_{i=1}^{n}\left|x_i - c\right| .
$$

When $c = \bar{x}$ the quantity is the mean absolute deviation about the mean; when $c = Q_2$ it is the mean absolute deviation about the median.

The absolute value prevents the algebraic cancellation that annihilates any average of signed deviations. The result is in the original units and is less influenced by extremes than the standard deviation because it does not square. The cost is algebraic: the absolute value function has a corner at zero, so the measure does not decompose as cleanly as the variance when groups are pooled or when the data are rescaled.

### 1.7 The variance and the standard deviation

> **Definition (Variance).** The variance of $n$ observations is

$$
s^{2} = \frac{1}{n}\sum_{i=1}^{n}\left(x_i - \bar{x}\right)^{2},
$$

and for frequency or grouped data with $n = \sum_{i=1}^{k} f_i$ it is

$$
s^{2} = \frac{1}{n}\sum_{i=1}^{k} f_i\left(x_i - \bar{x}\right)^{2} .
$$

> **Definition (Standard deviation).** The standard deviation is $s = \sqrt{s^{2}}$, the non-negative square root of the variance.

Squaring does three jobs at once. It removes the sign of each deviation so no cancellation occurs; it makes the sum differentiable in the centre, which is what makes the minimisation and decomposition results of Section 2 true; and it gives large deviations disproportionately large weight, which is appropriate whenever large errors are disproportionately costly. The standard deviation restores the original units, because the square root of a mean of squared quantities measured in units of $X$ is measured in units of $X$. A standard deviation of $3.24$ marks means typical departures from the mean are of the order of three marks; a variance of $10.48$ square marks means the same thing but is not directly interpretable.

### 1.8 The coefficient of variation

> **Definition (Coefficient of variation).** For a data set with non-zero mean, the coefficient of variation is

$$
CV = \frac{s}{\bar{x}},
$$

usually reported as a percentage $100\,\frac{s}{\bar{x}}$ per cent.

The units of $s$ and $\bar{x}$ cancel, so the quantity is dimensionless and behaves like a relative risk. A coefficient of $0.08$ says that the standard deviation is eight per cent of the mean. Two production lines whose outputs are measured in different currencies, two examination papers marked out of different totals, or two investments whose returns sit at very different levels can all be compared on this scale. The smaller coefficient marks the more consistent, more homogeneous, less risky set. Two conditions must be checked before the measure is used: the mean must be non-zero, and it should be positive for the percentage interpretation to make sense, since a negative mean reverses the direction of the ranking.

### 1.9 Moments about an origin and about the mean

Let $A$ be any real constant, called the working origin. The $r$-th moment about $A$ of a set of observations is

$$
m_r'(A) = \frac{1}{n}\sum_{i=1}^{n}\left(x_i - A\right)^{r} .
$$

The two values that matter here are the first moment about $A$, which measures where the data sit relative to $A$, and the second moment about $A$, which measures spread about $A$. The second moment about the mean, $m_2'(\bar{x})$, is exactly the variance. The moments about the origin zero, that is about $A = 0$, are the raw moments and are written $m_1'$ and $m_2'$ without an argument. Every shortcut formula in this topic is an application of the identity relating $m_2'(A)$ to $m_2'(\bar{x})$, derived in Section 3.

### 1.10 The four data formats and the first move for each

Recognising the format before touching a formula is worth more marks than any single computation, because each format has a standard opening move.

| Data format | What you are given | Standard first move |
|---|---|---|
| Raw list | Individual observations | Compute $\sum x_i$ and $\sum x_i^{2}$ |
| Discrete frequency table | Values with counts | Build $fx$ and $fx^{2}$ columns |
| Grouped frequency table | Classes with counts | Replace each class by its mark, then code |
| Summary statistics | $n$, mean, variance per group | Use the pooled mean, then the decomposition |

For a grouped table the class mark is the midpoint, and the class width $h$ is the difference between consecutive lower class limits. Coding by $u_i = \frac{m_i - A}{h}$ turns the marks into small integers, which is the single most reliable defence against arithmetic error in a long table.

### 1.11 The measures compared

| Measure | Formula | Units | Uses all data | Outlier resistance |
|---|---|---|---|---|
| Range | $x_g - x_l$ | Original | No, two values | None |
| Quartile deviation | $\frac{1}{2}\left(Q_3 - Q_1\right)$ | Original | Middle half only | High |
| Mean absolute deviation | $\frac{1}{n}\sum\left\lvert x_i - \bar{x}\right\rvert$ | Original | Yes | Moderate |
| Variance | $\frac{1}{n}\sum\left(x_i - \bar{x}\right)^{2}$ | Squared | Yes | Low |
| Standard deviation | $\sqrt{s^{2}}$ | Original | Yes | Low |
| Coefficient of variation | $\frac{s}{\bar{x}}$ | None | Yes | Low |

Read the outlier resistance column as a warning rather than a ranking of quality. A measure that ignores outliers cannot detect contamination, and a measure that is destroyed by outliers cannot be trusted until the data have been cleaned. The examination expects you to match the measure to the purpose rather than to declare one measure best.

## 2. Theorems, Lemmas, and Analytical Properties

### 2.1 The high-yield list

Six results generate almost every calculation in this topic. They are stated here with the conditions under which each is valid; the proofs occupy Section 3.

> **Result 1 (Zero-sum lemma).** For any data set, $\sum_{i=1}^{n}\left(x_i - \bar{x}\right) = 0$.

> **Result 2 (Computational formula).** With $n = \sum f_i$,

$$
s^{2} = \frac{1}{n}\sum_{i=1}^{k} f_i x_i^{2} - \bar{x}^{2} .
$$

> **Result 3 (Second-moment identity).** For any real $A$,

$$
\frac{1}{n}\sum_{i=1}^{n}\left(x_i - A\right)^{2} = s^{2} + \left(\bar{x} - A\right)^{2} .
$$

> **Result 4 (Coding formula).** If $u_i = \frac{x_i - A}{h}$ with $h \ne 0$, then

$$
\bar{x} = A + h\bar{u}, \qquad s_x^{2} = h^{2}s_u^{2} .
$$

> **Result 5 (Linear transformation).** If $y_i = a x_i + b$ with constants $a$, $b$, then

$$
\bar{y} = a\bar{x} + b, \qquad s_y^{2} = a^{2}s_x^{2}, \qquad s_y = \left|a\right| s_x .
$$

> **Result 6 (Combined variance).** For $k$ groups with sizes $n_j$, means $\bar{x}_j$ and variances $s_j^{2}$,

$$
s^{2} = \frac{1}{N}\sum_{j=1}^{k} n_j\left[s_j^{2} + \left(\bar{x}_j - \bar{x}\right)^{2}\right], \qquad N = \sum_{j=1}^{k} n_j ,
$$

where $\bar{x} = \frac{1}{N}\sum_{j=1}^{k} n_j \bar{x}_j$ is the pooled mean.

Each of these is an identity, not an approximation, so it may be used in either direction. Result 3 is used forwards to obtain a variance from a second moment about a convenient origin and backwards to obtain a second moment about an arbitrary point from a known variance. Result 6 is the only one that contains a term with no counterpart in the individual groups, and that term is the whole point of the combined-variance question.

### 2.2 The between-group term made explicit

Result 6 splits the total variance into two parts that have separate names. The within-group part is the weighted average of the group variances,

$$
s_W^{2} = \frac{1}{N}\sum_{j=1}^{k} n_j s_j^{2},
$$

and the between-group part is the weighted variance of the group means about the pooled mean,

$$
s_B^{2} = \frac{1}{N}\sum_{j=1}^{k} n_j\left(\bar{x}_j - \bar{x}\right)^{2} .
$$

The decomposition is

$$
s^{2} = s_W^{2} + s_B^{2} .
$$

Three consequences follow immediately and each is a standard examination point. First, the combined variance can never be smaller than the weighted average of the group variances, because $s_B^{2} \ge 0$. Second, if all the group means are equal then the between-group term vanishes and the combined variance is exactly the weighted average of the group variances. Third, a combined variance may be far larger than every individual group variance — a point that surprises candidates who expect pooling to average things out. Two tightly clustered groups whose centres are far apart produce a pooled set that is very widely spread.

### 2.3 Inequalities worth memorising

> **Result 7 (Mean absolute deviation is at most the standard deviation).** For every data set,

$$
\frac{1}{n}\sum_{i=1}^{n}\left|x_i - \bar{x}\right| \le s .
$$

> **Result 8 (Popoviciu's inequality).** For every data set with range $R$ and standard deviation $s$, $s \le \frac{R}{2}$, with equality only when exactly half the observations sit at each extreme.

> **Result 9 (The mean minimises squared error; the median minimises absolute error).** For any constant $c$,

$$
\sum_{i=1}^{n}\left(x_i - c\right)^{2} \ge \sum_{i=1}^{n}\left(x_i - \bar{x}\right)^{2}
$$

with equality only at $c = \bar{x}$, and

$$
\sum_{i=1}^{n}\left|x_i - c\right| \ge \sum_{i=1}^{n}\left|x_i - Q_2\right|
$$

with equality for any median $Q_2$.

Result 9 explains why the variance is defined about the mean and the mean absolute deviation is often reported about the median. Each centre is the natural anchor for its own loss function, and using the wrong anchor inflates the measure. A candidate who computes the mean absolute deviation about an arbitrary value and reports it as the mean absolute deviation about the mean has computed a different, larger quantity.

Result 8 is a useful sanity check. A standard deviation exceeding half the range is impossible, so an answer of that kind signals an arithmetic slip rather than a genuinely dispersed set. It also gives a fast one-line bound in multiple-choice items.

### 2.4 Properties of the coefficient of variation

> **Result 10 (Invariance under change of scale).** If $y_i = a x_i$ with $a > 0$ and $\bar{x} > 0$, then $CV_y = CV_x$.

> **Result 11 (Sensitivity to change of origin).** If $y_i = x_i + b$ with $b \ne 0$, then $CV_y = \frac{s}{\bar{x} + b} \ne CV_x$ in general.

These two results are the formal statement of a fact that catches many candidates: the coefficient of variation is a measure of relative, not absolute, position. Changing units — multiplying every observation by a positive constant — leaves it untouched, which is exactly what a unit-free measure must do. Shifting every observation by an additive constant changes it, because the standard deviation is unchanged while the mean moves. Converting temperatures between scales that differ by an offset therefore changes the coefficient of variation, whereas converting between units that differ only by a factor does not.

> **Result 12 (Interpretation as relative risk).** Writing $\bar{x} > 0$, the coefficient of variation is the ratio of the typical departure to the level of the data. If $CV_A < CV_B$ then relative to its own mean the set $A$ is more consistent than $B$, and this conclusion does not depend on the units of either set.

Result 12 is the entire content of the standard comparison question. The phrase "more consistent" translates as "smaller coefficient of variation", never as "smaller standard deviation" unless the two means are equal.

### 2.5 Range-based and quartile-based coefficients

> **Result 13 (Coefficient of range).** For non-negative data, $0 \le \frac{x_g - x_l}{x_g + x_l} < 1$.

> **Result 14 (Coefficient of quartile deviation).** For non-negative data with $Q_1 > 0$, $0 \le \frac{Q_3 - Q_1}{Q_3 + Q_1} < 1$.

Both coefficients are ratios of a spread to a level, and both are unchanged by a rescaling of the data by a positive constant. They differ in the portion of the data they use. The coefficient of range is governed entirely by the two extreme values and therefore inherits the range's fragility. The coefficient of quartile deviation is governed by the central half and is the appropriate relative measure for skewed distributions where the standard deviation is not a good summary of spread. Neither coefficient should be used to compare a data set whose values are all negative, because the denominators then behave counter-intuitively.

### 2.6 Grouped data and its systematic bias

When a grouped table is used, every observation inside a class is replaced by the class mark. The variance computed from the marks therefore ignores the spread of the observations within each class and is smaller than the variance of the original observations. Writing $h$ for the class width, the shortfall is approximately $\frac{h^{2}}{12}$ per class, which is the variance of a value assumed uniformly spread across an interval of width $h$. The corrected estimate is

$$
s_{\text{corrected}}^{2} \approx s_{\text{grouped}}^{2} + \frac{h^{2}}{12},
$$

a form known as Sheppard's correction. The qualification matters: the correction is an approximation, it assumes the classes are of equal width and that the distribution is smooth across class boundaries, and it should not be applied when the variable is discrete or when the classes are open-ended. In an examination it is used only when a question explicitly asks for it.

### 2.7 What a zero dispersion means

> **Result 15 (Vanishing dispersion characterises constant data).** For a data set with $n \ge 1$, $s^{2} = 0$ if and only if $x_1 = x_2 = \dots = x_n$.

The forward direction is immediate from the definition, since a sum of squares of non-negative terms can be zero only if every term is zero. The converse is trivial. The result is worth stating because it fixes the lower end of the scale: dispersion is never negative, and the value zero carries a definite meaning rather than being a formal boundary. It also justifies reading a small variance as a statement about homogeneity and a large one as a statement about heterogeneity, with the caveat that "small" and "large" are relative to the units and the level of the data.

### 2.8 Summary of the working formulas

| Quantity | Raw data | Frequency data |
|---|---|---|
| Mean | $\frac{1}{n}\sum x_i$ | $\frac{1}{n}\sum f_i x_i$ |
| Second moment about zero | $\frac{1}{n}\sum x_i^{2}$ | $\frac{1}{n}\sum f_i x_i^{2}$ |
| Variance | $\frac{1}{n}\sum x_i^{2} - \bar{x}^{2}$ | $\frac{1}{n}\sum f_i x_i^{2} - \bar{x}^{2}$ |
| Standard deviation | $\sqrt{s^{2}}$ | $\sqrt{s^{2}}$ |
| Coefficient of variation | $\frac{s}{\bar{x}}$ | $\frac{s}{\bar{x}}$ |
| Coded variance | $h^{2}\left[\frac{1}{n}\sum f_i u_i^{2} - \bar{u}^{2}\right]$ | same, with $u_i = \frac{x_i - A}{h}$ |

The two columns are the same formula once $f_i = 1$ is substituted throughout, which is why a single derivation serves both cases. For grouped data the same table applies with $x_i$ read as the class mark $m_i$, provided the marks are equally spaced so that a single width $h$ describes the coding.

## 3. Formal Proofs, Derivations, and Methods

### 3.1 Proof of the zero-sum lemma

Start from the definition of the mean and distribute the summation.

$$
\sum_{i=1}^{n}\left(x_i - \bar{x}\right) = \sum_{i=1}^{n} x_i - \sum_{i=1}^{n}\bar{x}
$$

The first sum is $n\bar{x}$ by the definition of $\bar{x}$, and the second is $n\bar{x}$ because $\bar{x}$ is a constant added $n$ times.

$$
\sum_{i=1}^{n}\left(x_i - \bar{x}\right) = n\bar{x} - n\bar{x} = 0
$$

The same argument with weights gives $\sum_{i=1}^{k} f_i\left(x_i - \bar{x}\right) = 0$, since $\sum f_i x_i = n\bar{x}$ and $\sum f_i \bar{x} = n\bar{x}$. This lemma is used in every derivation that follows, and it is the reason the cross-term disappears when a sum of squared deviations is expanded about a new origin.

### 3.2 Derivation of the computational formula

Expand the square and sum term by term.

$$
\sum_{i=1}^{n}\left(x_i - \bar{x}\right)^{2} = \sum_{i=1}^{n} x_i^{2} - 2\bar{x}\sum_{i=1}^{n} x_i + \sum_{i=1}^{n}\bar{x}^{2}
$$

The middle term is $-2\bar{x}\left(n\bar{x}\right) = -2n\bar{x}^{2}$ and the last is $n\bar{x}^{2}$, so

$$
\sum_{i=1}^{n}\left(x_i - \bar{x}\right)^{2} = \sum_{i=1}^{n} x_i^{2} - 2n\bar{x}^{2} + n\bar{x}^{2} = \sum_{i=1}^{n} x_i^{2} - n\bar{x}^{2} .
$$

Dividing by $n$ gives the computational form.

$$
s^{2} = \frac{1}{n}\sum_{i=1}^{n} x_i^{2} - \bar{x}^{2}
$$

Replacing each unit count by a weight produces the frequency version quoted as Result 2. The practical value of the form is that it needs only two totals, $\sum f_i x_i$ and $\sum f_i x_i^{2}$, so a single working table serves both the mean and the variance and a transcription error in one column does not propagate into a second pass over the data.

### 3.3 Derivation of the second-moment identity

Let $A$ be arbitrary and write $x_i - A = \left(x_i - \bar{x}\right) + \left(\bar{x} - A\right)$. Squaring and summing,

$$
\sum_{i=1}^{n}\left(x_i - A\right)^{2} = \sum_{i=1}^{n}\left(x_i - \bar{x}\right)^{2} + 2\left(\bar{x} - A\right)\sum_{i=1}^{n}\left(x_i - \bar{x}\right) + n\left(\bar{x} - A\right)^{2} .
$$

The middle sum is zero by the lemma of Section 3.1, so

$$
\sum_{i=1}^{n}\left(x_i - A\right)^{2} = \sum_{i=1}^{n}\left(x_i - \bar{x}\right)^{2} + n\left(\bar{x} - A\right)^{2} .
$$

Divide by $n$ and recognise the first term on the right as the variance.

$$
\frac{1}{n}\sum_{i=1}^{n}\left(x_i - A\right)^{2} = s^{2} + \left(\bar{x} - A\right)^{2}
$$

The identity says that the second moment about any origin exceeds the variance by the squared distance from that origin to the mean. It therefore also proves Result 9 in its squared form, because the added term is non-negative and vanishes only at $A = \bar{x}$. Rearranged, it gives the assumed-mean route to the variance,

$$
s^{2} = \frac{1}{n}\sum_{i=1}^{n}\left(x_i - A\right)^{2} - \left(\bar{x} - A\right)^{2},
$$

which is the version to quote when a question supplies a second moment about a stated origin.

### 3.4 Derivation of the coding formula

Let $u_i = \frac{x_i - A}{h}$, so that $x_i = A + h u_i$. The mean transforms linearly.

$$
\bar{x} = \frac{1}{n}\sum_{i=1}^{n}\left(A + h u_i\right) = A + h\bar{u}
$$

For the variance, apply the transformation to each deviation.

$$
x_i - \bar{x} = \left(A + h u_i\right) - \left(A + h\bar{u}\right) = h\left(u_i - \bar{u}\right)
$$

Squaring, summing and dividing by $n$,

$$
s_x^{2} = \frac{1}{n}\sum_{i=1}^{n} h^{2}\left(u_i - \bar{u}\right)^{2} = h^{2} s_u^{2} .
$$

Combining the two results with the computational form for $s_u^{2}$ gives the working formula

$$
s_x^{2} = h^{2}\left[\frac{1}{n}\sum_{i=1}^{k} f_i u_i^{2} - \bar{u}^{2}\right]
$$

where $\bar{u} = \frac{1}{n}\sum f_i u_i$. The restoration of the units happens in the single factor $h^{2}$, which is why the coded column may be computed in whatever small integers are convenient.

### 3.5 Proof of the linear transformation theorem

Let $y_i = a x_i + b$. Then

$$
\bar{y} = \frac{1}{n}\sum_{i=1}^{n}\left(a x_i + b\right) = a\bar{x} + b .
$$

For the variance,

$$
y_i - \bar{y} = a x_i + b - \left(a\bar{x} + b\right) = a\left(x_i - \bar{x}\right),
$$

so

$$
s_y^{2} = \frac{1}{n}\sum_{i=1}^{n} a^{2}\left(x_i - \bar{x}\right)^{2} = a^{2} s_x^{2} .
$$

Taking square roots gives $s_y = \left|a\right| s_x$, the absolute value being necessary because the standard deviation is non-negative while $a$ may be negative. The proof shows precisely where each constant acts: the additive constant $b$ moves the mean and leaves the spread untouched, while the multiplicative constant $a$ scales both the mean and the standard deviation and scales the variance by its square.

### 3.6 Derivation of the combined variance

Consider first two groups with sizes $n_1$, $n_2$, means $\bar{x}_1$, $\bar{x}_2$ and variances $s_1^{2}$, $s_2^{2}$. Let $N = n_1 + n_2$ and let $\bar{x}$ be the pooled mean, which by the definition of the mean is

$$
\bar{x} = \frac{n_1\bar{x}_1 + n_2\bar{x}_2}{N} .
$$

The total sum of squared deviations about the pooled mean splits into a contribution from each group.

$$
\sum_{\text{all}}\left(x - \bar{x}\right)^{2} = \sum_{\text{group }1}\left(x - \bar{x}\right)^{2} + \sum_{\text{group }2}\left(x - \bar{x}\right)^{2}
$$

Inside group $1$, write $x - \bar{x} = \left(x - \bar{x}_1\right) + \left(\bar{x}_1 - \bar{x}\right)$ and expand.

$$
\sum_{1}\left(x - \bar{x}\right)^{2} = \sum_{1}\left(x - \bar{x}_1\right)^{2} + 2\left(\bar{x}_1 - \bar{x}\right)\sum_{1}\left(x - \bar{x}_1\right) + n_1\left(\bar{x}_1 - \bar{x}\right)^{2}
$$

The middle sum vanishes by the zero-sum lemma applied within the group, and the first sum is $n_1 s_1^{2}$.

$$
\sum_{1}\left(x - \bar{x}\right)^{2} = n_1 s_1^{2} + n_1\left(\bar{x}_1 - \bar{x}\right)^{2}
$$

The identical argument in group $2$ gives $n_2 s_2^{2} + n_2\left(\bar{x}_2 - \bar{x}\right)^{2}$. Adding and dividing by $N$,

$$
s^{2} = \frac{1}{N}\left[n_1 s_1^{2} + n_2 s_2^{2} + n_1\left(\bar{x}_1 - \bar{x}\right)^{2} + n_2\left(\bar{x}_2 - \bar{x}\right)^{2}\right] .
$$

The extension to $k$ groups is the same expansion repeated, which yields Result 6. The first brace of terms is the within-group component and the second is the between-group component; the second is the only place the group means appear other than through the pooled mean.

### 3.7 Proof that the mean absolute deviation is at most the standard deviation

Let $d_i = x_i - \bar{x}$ and let $z_i$ be the sign of $d_i$, so that $\left|d_i\right| = z_i d_i$ and $z_i^{2} = 1$ for every $i$ with $d_i \ne 0$. By the Cauchy-Schwarz inequality applied to the vectors $\left(z_1, \dots, z_n\right)$ and $\left(d_1, \dots, d_n\right)$,

$$
\left(\sum_{i=1}^{n} z_i d_i\right)^{2} \le \left(\sum_{i=1}^{n} z_i^{2}\right)\left(\sum_{i=1}^{n} d_i^{2}\right) .
$$

Since $\left|d_i\right| = z_i d_i$ and $z_i^{2} \le 1$, the inequality becomes

$$
\left(\sum_{i=1}^{n}\left|d_i\right|\right)^{2} \le n\sum_{i=1}^{n} d_i^{2} .
$$

Divide by $n^{2}$ and take square roots.

$$
\frac{1}{n}\sum_{i=1}^{n}\left|d_i\right| \le \sqrt{\frac{1}{n}\sum_{i=1}^{n} d_i^{2}} = s
$$

Equality holds exactly when all the deviations have the same magnitude, that is when every observation lies at $\bar{x} - s$ or at $\bar{x} + s$. In that configuration the mean absolute deviation and the standard deviation coincide, which is the extreme case of the inequality.

### 3.8 Proof of Popoviciu's inequality

Let the observations lie in $\left[x_l, x_g\right]$ with range $R = x_g - x_l$. For every observation, $\left(x_i - x_l\right)\left(x_g - x_i\right) \ge 0$, because both factors are non-negative.

$$
x_i^{2} - \left(x_l + x_g\right)x_i + x_l x_g \ge 0
$$

Averaging over $i$ and writing $\mu = \bar{x}$ for the mean of the raw values,

$$
\frac{1}{n}\sum x_i^{2} - \left(x_l + x_g\right)\mu + x_l x_g \ge 0 .
$$

Since $\frac{1}{n}\sum x_i^{2} = s^{2} + \mu^{2}$, substitution gives

$$
s^{2} + \mu^{2} - \left(x_l + x_g\right)\mu + x_l x_g \ge 0 .
$$

Complete the square in $\mu$ using $\mu^{2} - \left(x_l + x_g\right)\mu = \left(\mu - \frac{x_l + x_g}{2}\right)^{2} - \left(\frac{x_g - x_l}{2}\right)^{2}$.

$$
s^{2} \ge \left(\frac{x_g - x_l}{2}\right)^{2} - \left(\mu - \frac{x_l + x_g}{2}\right)^{2}
$$

The second term on the right is at most zero in magnitude, so dropping it strengthens the inequality to $s^{2} \ge \left(\frac{R}{2}\right)^{2} - \left(\mu - \text{midpoint}\right)^{2}$, and the weakest possible case is $\mu$ at the midpoint, where $s^{2} = \frac{R^{2}}{4}$ if all mass sits at the two ends. Hence $s \le \frac{R}{2}$ in every case, with equality only for a two-point distribution with equal masses at the extremes.

### 3.9 Method: variance and standard deviation of grouped data by coding

The following procedure is the one to follow mechanically in an examination.

Step 1. Copy the classes and frequencies into a working table and total the frequency column, labelling the total $n$.

Step 2. Write the class mark $m_i$ for each class as the average of its limits.

Step 3. Choose a working origin $A$ equal to the mark of a middle class and a width $h$ equal to the common class width. Confirm that the marks are equally spaced before using a single $h$.

Step 4. Form the coded column $u_i = \frac{m_i - A}{h}$. These must be consecutive integers; if they are not, the width has been chosen wrongly.

Step 5. Compute the two totals $\sum f_i u_i$ and $\sum f_i u_i^{2}$.

Step 6. Compute $\bar{u} = \frac{1}{n}\sum f_i u_i$ and restore the mean by $\bar{x} = A + h\bar{u}$.

Step 7. Compute $s_u^{2} = \frac{1}{n}\sum f_i u_i^{2} - \bar{u}^{2}$ and restore by $s_x^{2} = h^{2} s_u^{2}$.

Step 8. Take the square root and, if asked, divide by the mean for the coefficient of variation.

The check at the end is that $s_x$ must not exceed half the range of the marks. A violation means the coded column or a total is wrong.

### 3.10 Method: quartiles and quartile deviation for grouped data

Step 1. Total the frequencies to obtain $n$ and build a cumulative frequency column.

Step 2. Locate the class containing the $\frac{n}{4}$-th observation. That is the first class whose cumulative frequency reaches or passes $\frac{n}{4}$.

Step 3. Interpolate inside that class using

$$
Q_1 = L_1 + \frac{\frac{n}{4} - F_1}{f_1}\,h_1 ,
$$

where $L_1$ is the lower class boundary, $F_1$ the cumulative frequency before the class, $f_1$ the class frequency and $h_1$ the class width.

Step 4. Repeat with $\frac{3n}{4}$ to obtain $Q_3$.

Step 5. Form $Q = \frac{1}{2}\left(Q_3 - Q_1\right)$ and, if a relative measure is required, the coefficient $\frac{Q_3 - Q_1}{Q_3 + Q_1}$.

Step 6. Sanity-check that $Q_1 < Q_2 < Q_3$ and that $Q$ is smaller than half the range.

### 3.11 Method: pooled variance from group summaries

Step 1. Label each group with its size $n_j$, mean $\bar{x}_j$ and standard deviation $s_j$.

Step 2. Convert every standard deviation to a variance, since the decomposition is additive only in squared units.

Step 3. Compute $N = \sum n_j$ and the pooled mean $\bar{x} = \frac{1}{N}\sum n_j \bar{x}_j$.

Step 4. For each group form the two pieces $n_j s_j^{2}$ and $n_j\left(\bar{x}_j - \bar{x}\right)^{2}$.

Step 5. Add all pieces, divide by $N$, and take the square root if the standard deviation is required.

Step 6. State separately the within-group and between-group components when a question asks for them, since the split explains why the pooled variance may exceed every group variance.

### 3.12 Method: repairing a summary after an error is discovered

When a question reports that one observation was misread, do not recompute the whole data set. Work with the two sufficient totals.

Step 1. Reconstruct $\sum x_i = n\bar{x}$ and $\sum x_i^{2} = n\left(s^{2} + \bar{x}^{2}\right)$ from the stated mean and standard deviation.

Step 2. Replace the wrong value $w$ by the correct value $c$ in both totals: add $c - w$ to the first and $c^{2} - w^{2}$ to the second.

Step 3. Divide by $n$ to obtain the corrected mean and the corrected second moment about zero.

Step 4. Subtract the square of the corrected mean from the corrected second moment to obtain the corrected variance.

Step 5. Take the square root, then recheck the coefficient of variation if the question asks how the relative spread changed.

## 4. Representative Worked Examples and Solutions

### 4.1 Problem: grouped marks, complete set of measures

The marks of $40$ candidates in a test marked out of $30$ are grouped as follows. Compute the mean, the variance, the standard deviation and the coefficient of variation, and state the range of the marks that the grouping permits.

| Class | $0$ to $4$ | $5$ to $9$ | $10$ to $14$ | $15$ to $19$ | $20$ to $24$ | $25$ to $29$ |
|---|---|---|---|---|---|---|
| Frequency | $4$ | $8$ | $14$ | $10$ | $3$ | $1$ |

### 4.2 Solution: code the class marks, then restore the units

Step 1. Verify the total frequency and record the class marks and the coded values. Take the working origin $A = 17$, the mark of the fourth class, and the width $h = 5$.

| Class | Mark $m$ | $f$ | $u = \frac{m - 17}{5}$ | $fu$ | $fu^{2}$ |
|---|---|---|---|---|---|
| $0$ to $4$ | $2$ | $4$ | $-3$ | $-12$ | $36$ |
| $5$ to $9$ | $7$ | $8$ | $-2$ | $-16$ | $32$ |
| $10$ to $14$ | $12$ | $14$ | $-1$ | $-14$ | $14$ |
| $15$ to $19$ | $17$ | $10$ | $0$ | $0$ | $0$ |
| $20$ to $24$ | $22$ | $3$ | $1$ | $3$ | $3$ |
| $25$ to $29$ | $27$ | $1$ | $2$ | $2$ | $4$ |
| Total | — | $40$ | — | $-37$ | $89$ |

Marking point: the totals $n = 40$, $\sum fu = -37$ and $\sum fu^{2} = 89$ earn the method marks for the table, even if later arithmetic slips.

Step 2. Compute the coded mean.

$$
\bar{u} = \frac{-37}{40} = -0.925
$$

Step 3. Restore the mean using $\bar{x} = A + h\bar{u}$.

$$
\bar{x} = 17 + 5\left(-0.925\right) = 17 - 4.625 = 12.375
$$

The mean mark is $12.375$ out of $30$.

Step 4. Compute the coded variance.

$$
s_u^{2} = \frac{89}{40} - \left(-0.925\right)^{2} = 2.225 - 0.855625 = 1.369375
$$

Step 5. Restore the variance by multiplying by $h^{2} = 25$.

$$
s^{2} = 25 \times 1.369375 = 34.234375
$$

Step 6. Take the square root for the standard deviation.

$$
s = \sqrt{34.234375} \approx 5.851
$$

Step 7. Compute the coefficient of variation as a percentage.

$$
CV = \frac{5.851}{12.375} \times 100 \approx 47.28 \text{ per cent}
$$

Step 8. Interpret and check. The typical mark departs from the mean by about $5.85$ marks, which is almost half the mean, so the group is very heterogeneous. The check $s \le \frac{1}{2}\left(27 - 2\right) = 12.5$ is satisfied, so the answer is at least internally consistent. The permitted range of the underlying raw marks is from $0$ to $29$, but the marks themselves span at most $2$ to $27$ as class marks, so the true range of the raw data lies between $25$ and $29$.

Marking points: one mark for the coded table, one for the mean, one for the coded variance, one for restoring the variance, one for the standard deviation, one for the coefficient of variation, and one for the interpretation.

### 4.3 Problem: the second moment about a stated origin

The seven observations $8, 10, 12, 14, 16, 18, 20$ are summarised by a second moment about the origin $20$ equal to $52$. Recover the mean, the variance and the standard deviation, and verify the result by computing the variance about the mean directly.

### 4.4 Solution: subtract the squared gap

Step 1. State the identity to be used, with $A = 20$.

$$
\frac{1}{n}\sum_{i=1}^{n}\left(x_i - A\right)^{2} = s^{2} + \left(\bar{x} - A\right)^{2}
$$

Step 2. Compute the mean, which the question does not give directly.

$$
\bar{x} = \frac{8 + 10 + 12 + 14 + 16 + 18 + 20}{7} = \frac{98}{7} = 14
$$

Step 3. Substitute the known second moment and the squared gap.

$$
52 = s^{2} + \left(14 - 20\right)^{2} = s^{2} + 36
$$

Step 4. Solve for the variance.

$$
s^{2} = 52 - 36 = 16
$$

Step 5. Take the square root.

$$
s = 4
$$

Step 6. Verify by direct computation about the mean. The deviations are $-6, -4, -2, 0, 2, 4, 6$.

$$
\frac{1}{7}\left(36 + 16 + 4 + 0 + 4 + 16 + 36\right) = \frac{112}{7} = 16
$$

Step 7. Interpret. The second moment about $20$ overstates the variance by $36$, the square of the distance from the mean to the working origin. Using a far origin inflates the raw second moment but never loses information, because the correction is exact.

Marking points: one mark for the identity, one for the mean, one for the subtraction, one for the square root, one for the verification.

### 4.5 Problem: three groups pooled

Three departments report the following wage statistics. Compute the pooled mean, the pooled variance and the pooled standard deviation, and decompose the pooled variance into its within-group and between-group parts.

| Department | Workers $n_j$ | Mean wage | Standard deviation |
|---|---|---|---|
| $A$ | $40$ | $55$ | $6$ |
| $B$ | $60$ | $65$ | $8$ |
| $C$ | $100$ | $70$ | $10$ |

### 4.6 Solution: pool the mean, then add the between-group term

Step 1. Convert every standard deviation into a variance.

$$
s_A^{2} = 36, \qquad s_B^{2} = 64, \qquad s_C^{2} = 100
$$

Step 2. Total the sizes.

$$
N = 40 + 60 + 100 = 200
$$

Step 3. Compute the pooled mean as a weighted average.

$$
\bar{x} = \frac{40(55) + 60(65) + 100(70)}{200} = \frac{2200 + 3900 + 7000}{200} = \frac{13100}{200} = 65.5
$$

Step 4. Compute each group's squared gap from the pooled mean.

$$
\bar{x}_A - \bar{x} = 55 - 65.5 = -10.5, \qquad \bar{x}_B - \bar{x} = 65 - 65.5 = -0.5, \qquad \bar{x}_C - \bar{x} = 70 - 65.5 = 4.5
$$

Step 5. Form the two components for each group.

$$
40\left(36 + 110.25\right) = 40 \times 146.25 = 5850
$$

$$
60\left(64 + 0.25\right) = 60 \times 64.25 = 3855
$$

$$
100\left(100 + 20.25\right) = 100 \times 120.25 = 12025
$$

Step 6. Add and divide by the total size.

$$
s^{2} = \frac{5850 + 3855 + 12025}{200} = \frac{21730}{200} = 108.65
$$

Step 7. Take the square root.

$$
s = \sqrt{108.65} \approx 10.42
$$

Step 8. Separate the components. The within-group part is the weighted average of the group variances.

$$
s_W^{2} = \frac{40(36) + 60(64) + 100(100)}{200} = \frac{1440 + 3840 + 10000}{200} = \frac{15280}{200} = 76.4
$$

The between-group part is the rest.

$$
s_B^{2} = 108.65 - 76.4 = 32.25
$$

Step 9. Interpret. The pooled variance exceeds every group variance except that of department $C$, which is the effect of the between-group term. The centres are $10.5$ and $4.5$ units apart respectively, and that separation adds $32.25$ square units of variance that exists only because the groups were pooled.

Marking points: one for the weighted mean, two for the three group contributions, one for the division by $N$, one for the square root, one for each component of the decomposition.

### 4.7 Problem: a change of units and origin

A set of temperatures measured in degrees Celsius has mean $25$ and standard deviation $4$. Convert to degrees Fahrenheit using $F = 1.8C + 32$ and state the mean, variance and standard deviation in the new scale. Compute the coefficient of variation in both scales and comment on the difference.

### 4.8 Solution: apply the transformation theorem term by term

Step 1. Identify the constants in the linear relation, $a = 1.8$ and $b = 32$.

Step 2. Transform the mean.

$$
\bar{F} = 1.8(25) + 32 = 45 + 32 = 77
$$

Step 3. Transform the variance by the square of the multiplier.

$$
s_F^{2} = \left(1.8\right)^{2}\left(4\right)^{2} = 3.24 \times 16 = 51.84
$$

Step 4. Transform the standard deviation by the multiplier itself.

$$
s_F = 1.8 \times 4 = 7.2
$$

Step 5. Compute the coefficient of variation in the Celsius scale.

$$
CV_C = \frac{4}{25} \times 100 = 16 \text{ per cent}
$$

Step 6. Compute the coefficient of variation in the Fahrenheit scale.

$$
CV_F = \frac{7.2}{77} \times 100 \approx 9.35 \text{ per cent}
$$

Step 7. Comment. The standard deviation scaled by the factor $1.8$ while the mean received both the multiplication and the shift of $32$, so the ratio changed. This is the behaviour predicted by Results 10 and 11: a pure change of scale leaves the coefficient of variation untouched, but a change of origin moves it. A relative measure is therefore only comparable between data sets expressed on the same kind of scale, which is one reason comparisons of temperature variability are normally made in a single stated scale.

Marking points: one for the mean, one for the variance, one for the standard deviation, two for the two coefficients, one for the observation about origin versus scale.

### 4.9 Problem: quartile deviation of a grouped distribution

The weekly earnings of fifty workers, in hundreds of shillings, are grouped as follows. Compute the lower and upper quartiles, the quartile deviation and its coefficient, and compare the quartile deviation with the range.

| Earnings | $0$ to $10$ | $10$ to $20$ | $20$ to $30$ | $30$ to $40$ | $40$ to $50$ | $50$ to $60$ |
|---|---|---|---|---|---|---|
| Workers | $5$ | $10$ | $15$ | $10$ | $8$ | $2$ |

### 4.10 Solution: locate the classes, then interpolate

Step 1. Build the cumulative frequency column and confirm the total.

| Earnings | $f$ | Cumulative $f$ |
|---|---|---|
| $0$ to $10$ | $5$ | $5$ |
| $10$ to $20$ | $10$ | $15$ |
| $20$ to $30$ | $15$ | $30$ |
| $30$ to $40$ | $10$ | $40$ |
| $40$ to $50$ | $8$ | $48$ |
| $50$ to $60$ | $2$ | $50$ |

Step 2. Locate the lower quartile. The rank required is $n/4 = 12.5$, which is first reached in the class $10$ to $20$, where the cumulative frequency jumps from $5$ to $15$.

Step 3. Interpolate for $Q_1$ with $L = 10$, $F = 5$, $f = 10$ and $h = 10$.

$$
Q_1 = 10 + \frac{12.5 - 5}{10}\left(10\right) = 10 + 7.5 = 17.5
$$

Step 4. Locate the upper quartile. The rank required is $3n/4 = 37.5$, reached in the class $30$ to $40$, where the cumulative frequency passes from $30$ to $40$.

Step 5. Interpolate for $Q_3$ with $L = 30$, $F = 30$, $f = 10$ and $h = 10$.

$$
Q_3 = 30 + \frac{37.5 - 30}{10}\left(10\right) = 30 + 7.5 = 37.5
$$

Step 6. Compute the quartile deviation.

$$
Q = \frac{1}{2}\left(37.5 - 17.5\right) = \frac{1}{2}\left(20\right) = 10
$$

Step 7. Compute the coefficient of quartile deviation.

$$
\frac{Q_3 - Q_1}{Q_3 + Q_1} = \frac{20}{55} \approx 0.364
$$

Step 8. Compare with the range. The full spread of the classes is from $0$ to $60$, so the range of the class limits is $60$ and the quartile deviation is $10$, one sixth of it. The quartile deviation describes the middle half of the workers, from $17.5$ to $37.5$ hundred shillings, and is unaffected by the two workers earning between $50$ and $60$.

Marking points: one for the cumulative column, one for locating each quartile class, two for the two interpolations, one for the quartile deviation, one for the coefficient, one for the comparison with the range.

### 4.11 Problem: repairing a summary statistic

A clerk computed the mean and standard deviation of twenty observations as $40$ and $5$. A later audit found that one observation had been entered as $25$ when the correct value was $52$. Find the corrected mean, variance and standard deviation.

### 4.12 Solution: rebuild the two sufficient totals

Step 1. Reconstruct the total of the observations from the stated mean.

$$
\sum x_i = n\bar{x} = 20 \times 40 = 800
$$

Step 2. Reconstruct the total of squares from the stated standard deviation.

$$
\sum x_i^{2} = n\left(s^{2} + \bar{x}^{2}\right) = 20\left(25 + 1600\right) = 32500
$$

Step 3. Replace the wrong value in the first total.

$$
\sum x_i^{\text{new}} = 800 + \left(52 - 25\right) = 827
$$

Step 4. Replace the wrong value in the second total.

$$
\sum \left(x_i^{\text{new}}\right)^{2} = 32500 + \left(52^{2} - 25^{2}\right) = 32500 + \left(2704 - 625\right) = 34579
$$

Step 5. Divide to obtain the corrected mean.

$$
\bar{x}^{\text{new}} = \frac{827}{20} = 41.35
$$

Step 6. Subtract the square of the new mean from the new second moment about zero.

$$
s_{\text{new}}^{2} = \frac{34579}{20} - \left(41.35\right)^{2} = 1728.95 - 1709.8225 = 19.1275
$$

Step 7. Take the square root.

$$
s_{\text{new}} = \sqrt{19.1275} \approx 4.373
$$

Step 8. Interpret. The corrected data are slightly more concentrated around a slightly higher mean, so the standard deviation falls from $5$ to about $4.37$. Both changes are in the expected direction: raising a below-average observation toward an above-average value pulls the mean up and reduces the spread.

Marking points: one for each reconstructed total, one for each replacement, one for the new mean, one for the new variance, one for the square root.

### 4.13 Problem: which process is more consistent

Two machines fill packets. Machine $A$ fills an average of $150$ grams with standard deviation $12$ grams. Machine $B$ fills an average of $90$ grams with standard deviation $9$ grams. Separately, a clerk's weekly wage averages $12000$ shillings with standard deviation $900$ shillings, while the same clerk's typing speed averages $55$ words per minute with standard deviation $6$ words per minute. Which machine is more consistent, and which of the clerk's two measurements is relatively more variable?

### 4.14 Solution: compare percentages, not raw spreads

Step 1. Compute the coefficient of variation for machine $A$.

$$
CV_A = \frac{12}{150} \times 100 = 8 \text{ per cent}
$$

Step 2. Compute the coefficient of variation for machine $B$.

$$
CV_B = \frac{9}{90} \times 100 = 10 \text{ per cent}
$$

Step 3. Compare. Machine $A$ has the larger standard deviation but the smaller coefficient of variation, so relative to its own mean machine $A$ is more consistent. The comparison must be made on the coefficients, because the two means differ; comparing $12$ with $9$ would have given the opposite and wrong answer.

Step 4. Compute the coefficient of variation for the wage.

$$
CV_w = \frac{900}{12000} \times 100 = 7.5 \text{ per cent}
$$

Step 5. Compute the coefficient of variation for the typing speed.

$$
CV_t = \frac{6}{55} \times 100 \approx 10.91 \text{ per cent}
$$

Step 6. Compare across the two different measurements. The typing speed is the relatively more variable of the two, at about $10.9$ per cent against $7.5$ per cent. The comparison is legitimate only because the coefficient of variation is unit-free; grams against shillings, or shillings against words per minute, cannot be compared in any other way.

Step 7. State the conclusion in the language of the question. Machine $A$ is the more consistent filler, and the clerk's typing speed is the more variable of the two recorded characteristics.

Marking points: one mark for each of the four coefficients, one for the correct ranking of the machines, one for the correct ranking of the two measurements, one for the explicit statement that units cancel.

### 4.15 Problem: the mean absolute deviation and its optimal centre

For the five observations $2, 3, 5, 8, 12$, compute the mean absolute deviation about the mean and about the median, compute the standard deviation, and check the inequality of Result 7.

### 4.16 Solution: two centres, two averages

Step 1. Compute the mean.

$$
\bar{x} = \frac{2 + 3 + 5 + 8 + 12}{5} = \frac{30}{5} = 6
$$

Step 2. List the absolute deviations from the mean and add them.

$$
\left\lvert 2 - 6\right\rvert = 4, \quad \left\lvert 3 - 6\right\rvert = 3, \quad \left\lvert 5 - 6\right\rvert = 1, \quad \left\lvert 8 - 6\right\rvert = 2, \quad \left\lvert 12 - 6\right\rvert = 6
$$

$$
\sum_{i=1}^{5}\left\lvert x_i - 6\right\rvert = 4 + 3 + 1 + 2 + 6 = 16
$$

Step 3. Divide by the number of observations.

$$
\text{MAD about the mean} = \frac{16}{5} = 3.2
$$

Step 4. Identify the median, which is the third of the five ordered values.

$$
Q_2 = 5
$$

Step 5. Repeat the absolute deviations about the median and average them.

$$
\left\lvert 2 - 5\right\rvert = 3, \quad \left\lvert 3 - 5\right\rvert = 2, \quad \left\lvert 5 - 5\right\rvert = 0, \quad \left\lvert 8 - 5\right\rvert = 3, \quad \left\lvert 12 - 5\right\rvert = 7
$$

$$
\text{MAD about the median} = \frac{3 + 2 + 0 + 3 + 7}{5} = \frac{15}{5} = 3.0
$$

Step 6. Compute the variance and standard deviation for comparison.

$$
s^{2} = \frac{16 + 9 + 1 + 4 + 36}{5} = \frac{66}{5} = 13.2, \qquad s = \sqrt{13.2} \approx 3.633
$$

Step 7. Check both inequalities. The mean absolute deviation about the mean is $3.2$, which is less than the standard deviation $3.633$, so Result 7 holds. The mean absolute deviation about the median is $3.0$, which is smaller than the value about the mean, so the median is the better centre for this loss function, exactly as Result 9 predicts.

Step 8. Interpret. The two absolute measures differ by $0.2$ because the single large observation at $12$ pulls the mean to the right of the median and therefore inflates the deviations from the mean. The standard deviation is larger than both because squaring gives the observation at $12$ a weight of $36$ in the sum, more than half the total. For skewed data of this kind, the median-based summary is the more faithful description of a typical departure.

## 5. Mathematical Extensions, Limits, and Common Errors

### 5.1 The traps that cost the most marks

The first trap is dividing by the wrong quantity. Every formula in this topic divides by $n$; the $n-1$ divisor belongs only to an unbiased estimate of a population variance from a sample, and a question that wants it will say so. Substituting $n-1$ into a descriptive calculation is an error, and so is substituting $n$ into an estimation calculation.

The second trap is forgetting to restore the units after coding. A coded variance is in squared coded units. If the working variable is $u = \frac{m - A}{h}$, the variance must be multiplied by $h^{2}$ before it means anything, and the standard deviation by $h$. An answer of $\sqrt{1.369375} = 1.17$ for the marks example is dimensionally meaningless; the correct value is $5.851$ marks.

The third trap is using a single class width when the classes are unequal. Coding assumes equal spacing. If the classes are not equally spaced, compute the marks and use the raw computational formula with $\sum f m$ and $\sum f m^{2}$ rather than coding.

The fourth trap is pooling variances by averaging them. The pooled variance is not $\frac{s_1^{2} + s_2^{2}}{2}$ unless the two groups have equal sizes and equal means. The between-group term must be included, and for groups whose centres differ it dominates.

The fifth trap is comparing standard deviations across data sets with different means or different units. The comparison the examination wants is almost always the coefficient of variation, and the phrase "more consistent" is a signal to compute it.

The sixth trap is computing the mean absolute deviation about the wrong centre. About the mean it is $\frac{1}{n}\sum\left|x_i - \bar{x}\right|$; about the median it is a different and smaller number. Quoting the smaller one as if it were the mean-based measure is a conceptual error, not a rounding difference.

The seventh trap is misreading the quartile coefficient. It is $\frac{Q_3 - Q_1}{Q_3 + Q_1}$, not $\frac{Q_3 - Q_1}{Q_2}$ and not $\frac{Q}{Q_3}$. The denominator is the sum of the two quartiles, and the value must lie between $0$ and $1$ for non-negative data.

### 5.2 Answer shapes that earn full marks

A dispersion question is normally marked against four things: the correct formula quoted or implied by the working, a correct working table, correct arithmetic, and an interpretive sentence. The interpretive sentence is worth a mark and is routinely omitted. It should state the size of a typical departure in the units of the data and, when two sets are compared, name the more consistent one and the reason.

Where a question asks for a comment, the comment must refer to the numbers obtained. "The coefficient of variation of machine $A$ is $8$ per cent and of machine $B$ is $10$ per cent, so machine $A$ is more consistent" earns the mark; "machine $A$ is better" does not. Where a question asks for the effect of a change, the answer should name the transformation theorem and state which part of the summary is affected.

### 5.3 Limits of each measure in practice

The range is unusable for contaminated data and uninformative for large samples, because it grows with the sample size even when the underlying distribution is fixed. The quartile deviation is robust but discards half the data and cannot distinguish two sets that agree in their quartiles. The mean absolute deviation is intuitive and robust-ish but does not decompose under pooling. The variance decomposes beautifully and drives all of inferential statistics, but it is in squared units and is dominated by a handful of extreme observations. The standard deviation repairs the units but inherits the sensitivity. The coefficient of variation is the only one of the six that is genuinely comparable across scales, but it requires a positive mean and it is meaningless for data that can legitimately be zero or negative, such as a profit figure or a temperature in degrees Celsius.

A further limit is that the coefficient of variation is not invariant under a change of origin, as Result 11 shows. Two laboratories reporting the same measurements on scales offset from one another will report different coefficients, and the difference is an artefact of the scale rather than a property of the data.

### 5.4 Revision checklist and time strategy

Work through the following list before the examination and tick each item only when you can do it without notes.

1. State the six measures, classify each as absolute or relative, and name the units of each.
2. Derive the computational formula for the variance from the definition in three lines.
3. Derive the second-moment identity and use it in both directions.
4. Write the coding formula with the restoration factors $h$ and $h^{2}$ and explain why each appears.
5. Prove the linear transformation result for the mean, variance and standard deviation.
6. Derive the combined variance and identify the within-group and between-group components.
7. Compute quartiles for grouped data by interpolation and check the ordering.
8. Compute the coefficient of variation and use it to rank consistency.
9. Repair a mean and variance after a misrecorded observation, using only two totals.
10. Quote the bounds $s \le \frac{R}{2}$ and $MAD \le s$ as checks.

For timing, allocate roughly one minute per mark and reserve the last few minutes of any dispersion question for the interpretation and the sanity checks. A grouped-table calculation is the longest item on the topic; if it appears with eight or more marks, begin it immediately and treat the working table as the deliverable, because a partially completed table with correct totals earns most of the available method marks even if the final square root is not reached. If a question offers a choice between a coding route and a raw route, take the coding route whenever the class marks are equally spaced and the numbers are large, and never spend time on a raw route that requires squaring four-digit marks by hand.

### 5.5 Where the topic leads

The variance defined here is the same quantity that appears as the second central moment of a probability distribution, and the decomposition of Section 3.6 is the finite-sample form of the law of total variance, in which the variance of a pooled population equals the mean of the conditional variances plus the variance of the conditional means. The coefficient of variation reappears as a measure of relative risk in finance and as a measure of assay precision in laboratory work. The standardisation step implicit in the coefficient of variation, dividing a deviation by a scale, becomes the $z$-score of the normal distribution, and that transformation is the bridge from describing one data set to comparing a value against a whole population.
