## 1. Foundational Concepts, Definitions, and Axioms

### 1.1 What is actually being examined

Every question on this topic is one of five tasks, and each task has a fixed opening move. A question either asks for a description of association, for a correlation coefficient, for one or both regression lines, for a prediction, or for a rank coefficient. The examiner is not testing whether you can admire a scatter diagram; the examiner is testing whether you can choose the correct formula, execute it without arithmetic error, and interpret the number in one sentence.

Three further facts shape every answer. First, correlation is symmetric and regression is not, so a question that says "regress $Y$ on $X$" is asking for a different object from one that says "regress $X$ on $Y$". Second, the arithmetic is almost entirely bookkeeping: five sums, three corrected sums, two slopes. Third, the interpretation marks are awarded for a sentence that names the direction, names the strength, and states the proportion of variation explained. An answer that computes $0.9849$ and stops has thrown away marks that were free.

### 1.2 The definitions the marking scheme expects

> **Definition (Correlation).** In a bivariate distribution there are two variates $x$ and $y$. If a change in one affects a change in the other, the variables are said to be correlated; otherwise they are said to be uncorrelated. If an increase or decrease in one results in an increase or decrease in the other, the correlation is positive; otherwise it is negative.

> **Definition (Pearson's coefficient).** As a measure of the degree of linear relationship between the variates, the coefficient of correlation is

$$
r_{xy} = \frac{\text{Cov}(x,y)}{\sqrt{\text{Var}(x)\times\text{Var}(y)}}
$$

> where $\text{Cov}(x,y)$ denotes the covariance, given by $\frac{1}{n}\sum\left(x_i-\bar{x}\right)\left(y_i-\bar{y}\right)$.

> **Definition (Regression of Y on X).** The simplest regression equation is $Y = a + bX$, where $a$ and $b$ are constants. This specifies the linear regression of $Y$ on $X$, and $b$ is the coefficient of regression of $Y$ on $X$.

> **Definition (Least squares).** The constants are determined by the normal equations $\sum y = na + b\sum x$ and $\sum xy = a\sum x + b\sum x^{2}$; equivalently they minimise $\sum\left(y_i - a - bx_i\right)^{2}$.

> **Definition (Spearman's coefficient).** For ranks with no repetition, $r_s = 1 - \frac{6\sum d^{2}}{n\left(n^{2}-1\right)}$, where $d$ is the difference between the ranks.

### 1.3 Scatter diagrams: the thirty-second read

Before touching a calculator, look at the shape of the cloud. Four readings are worth recording, because they will be needed for the interpretation mark.

**Direction.** A cloud rising to the right gives a positive coefficient; falling to the right gives a negative one.

**Narrowness.** A tight band gives a coefficient near $1$ or $-1$ in magnitude; a diffuse cloud gives a coefficient near $0$.

**Curvature.** A bowed band means the linear coefficient will understate the strength of the relationship. If the bow is symmetric, the coefficient may be close to zero despite an exact relationship.

**Isolation.** A point detached from the band is influential. Any claim about the coefficient must be qualified if such a point is present.

A reliable examination habit is to state these four readings in one sentence before the arithmetic, because that sentence is usually worth a mark on its own and it protects against a nonsensical computed value.

### 1.4 Notation and the algebra of corrected sums

Let $\left(x_1,y_1\right),\dots,\left(x_n,y_n\right)$ be $n$ paired observations with means $\bar{x}$ and $\bar{y}$. The three corrected sums are

$$
S_{xx} = \sum x_i^{2} - \frac{1}{n}\left(\sum x_i\right)^{2}, \qquad S_{yy} = \sum y_i^{2} - \frac{1}{n}\left(\sum y_i\right)^{2}, \qquad S_{xy} = \sum x_i y_i - \frac{1}{n}\sum x_i \sum y_i .
$$

All three are non-negative except $S_{xy}$, which carries the sign of the association. The descriptive variances and covariance are $s_x^{2} = S_{xx}/n$, $s_y^{2} = S_{yy}/n$ and $\text{Cov}(x,y) = S_{xy}/n$.

The quantities $S_{xx}$, $S_{yy}$ and $S_{xy}$ are the only intermediates that matter. Once they are correct, everything else is a short division. Most lost marks on this topic come from a single wrong total in the table, so the table itself deserves as much care as the final answer.

### 1.5 The coefficient and its computational forms

Three forms of the same number are in circulation, and the examiner will accept any of them provided the arithmetic is right.

$$
r_{xy} = \frac{S_{xy}}{\sqrt{S_{xx}S_{yy}}} = \frac{n\sum x_i y_i - \sum x_i\sum y_i}{\sqrt{\left[n\sum x_i^{2}-\left(\sum x_i\right)^{2}\right]\left[n\sum y_i^{2}-\left(\sum y_i\right)^{2}\right]}}
$$

The third form, obtained by dividing numerator and denominator of the second by $n$, is the one that pairs most naturally with the corrected sums.

$$
r_{xy} = \frac{\sum x_i y_i - \frac{1}{n}\sum x_i\sum y_i}{\sqrt{\left[\sum x_i^{2}-\frac{1}{n}\left(\sum x_i\right)^{2}\right]\left[\sum y_i^{2}-\frac{1}{n}\left(\sum y_i\right)^{2}\right]}}
$$

For hand computation the coded version is fastest. Writing $u_i = x_i - A$ and $v_i = y_i - B$ with $A$ and $B$ chosen near the respective means leaves $r$ unchanged while shrinking every entry.

### 1.6 The least squares line and the normal equations

The line of $Y$ on $X$ is $Y = a + bX$. Its constants solve

$$
\sum y = na + b\sum x, \qquad \sum xy = a\sum x + b\sum x^{2} .
$$

Written in corrected sums the solution is immediate.

$$
b_{yx} = \frac{S_{xy}}{S_{xx}}, \qquad a = \bar{y} - b_{yx}\bar{x}
$$

The line of $X$ on $Y$ is $X = c + dY$, whose constants solve

$$
\sum x = nc + d\sum y, \qquad \sum xy = c\sum y + d\sum y^{2}
$$

with solution

$$
b_{xy} = \frac{S_{xy}}{S_{yy}}, \qquad c = \bar{x} - b_{xy}\bar{y} .
$$

The distinction is worth stating in a single sentence that can be written under examination pressure: the line that predicts $Y$ divides by $S_{xx}$, and the line that predicts $X$ divides by $S_{yy}$.

### 1.7 The connection between the slopes and the coefficient

> **Theorem (Slope identities).** With $s_x$ and $s_y$ the standard deviations,

$$
b_{yx} = r_{xy}\frac{s_y}{s_x}, \qquad b_{xy} = r_{xy}\frac{s_x}{s_y}, \qquad b_{yx}b_{xy} = r_{xy}^{2} .
$$

These three identities turn a great many examination questions into one-line computations. Given $r$, the two standard deviations and the two means, both lines follow immediately. Given the two lines, $r$ is recovered as the square root of the product of the slopes, with the sign taken from the slopes themselves.

### 1.8 Determination and the standard error of estimate

The coefficient of determination is $r_{xy}^{2}$. It is the proportion of the total variation of the response that the fitted line accounts for.

$$
S_{yy} = SSR + SSE, \qquad r_{xy}^{2} = \frac{SSR}{S_{yy}} = 1 - \frac{SSE}{S_{yy}}
$$

The standard error of estimate converts the leftover sum of squares into the units of the response.

$$
s_e = \sqrt{\frac{SSE}{n-2}} = \sqrt{\frac{S_{yy}\left(1-r^{2}\right)}{n-2}}
$$

The divisor $n-2$ is not optional. Two constants were estimated, so two degrees of freedom are gone.

### 1.9 Rank correlation and the tied-rank correction

For untied ranks the coefficient is

$$
r_s = 1 - \frac{6\sum d^{2}}{n\left(n^{2}-1\right)}
$$

and for tied ranks

$$
r_s = 1 - \frac{6\left[\sum d^{2} + \sum\frac{m\left(m^{2}-1\right)}{12}\right]}{n\left(n^{2}-1\right)} .
$$

The correction is applied once for each group of $m$ equal values, separately in each series. Tied values receive the average of the ranks they would have occupied. Both facts are examinable, and the second is the one most often forgotten.

### 1.10 The formula table

| Quantity | Formula | Condition |
| --- | --- | --- |
| Corrected sum of products | $S_{xy} = \sum xy - \frac{1}{n}\sum x\sum y$ | None |
| Corrected sum of squares of $x$ | $S_{xx} = \sum x^{2} - \frac{1}{n}\left(\sum x\right)^{2}$ | None |
| Pearson's coefficient | $r = S_{xy}/\sqrt{S_{xx}S_{yy}}$ | $S_{xx} > 0$, $S_{yy} > 0$ |
| Slope of $Y$ on $X$ | $b_{yx} = S_{xy}/S_{xx}$ | $S_{xx} > 0$ |
| Intercept of $Y$ on $X$ | $a = \bar{y} - b_{yx}\bar{x}$ | None |
| Slope of $X$ on $Y$ | $b_{xy} = S_{xy}/S_{yy}$ | $S_{yy} > 0$ |
| Intercept of $X$ on $Y$ | $c = \bar{x} - b_{xy}\bar{y}$ | None |
| Determination | $r^{2} = b_{yx}b_{xy}$ | None |
| Standard error | $s_e = \sqrt{S_{yy}\left(1-r^{2}\right)/(n-2)}$ | $n > 2$ |
| Rank coefficient | $r_s = 1 - 6\sum d^{2}/\left[n\left(n^{2}-1\right)\right]$ | No ties |
| Tied rank coefficient | $r_s = 1 - 6\left[\sum d^{2}+\text{correction}\right]/\left[n\left(n^{2}-1\right)\right]$ | Ties corrected |

## 2. Theorems, Lemmas, and Analytical Properties

### 2.1 The bound and the equality case

> **Theorem.** For any paired data with non-zero spread, $-1 \le r_{xy} \le 1$.

> **Theorem.** $r_{xy} = 1$ if and only if all the points lie on a straight line of positive slope, and $r_{xy} = -1$ if and only if all the points lie on a straight line of negative slope.

The bound is a Cauchy–Schwarz inequality on the deviation vectors; the proof is in Section 3.2. Its examination use is diagnostic: a computed coefficient outside the interval means a wrong total, not a subtle theoretical point.

### 2.2 Invariance: why coding is always permitted

> **Theorem (Origin and scale).** If $u_i = \alpha + \beta x_i$ and $v_i = \gamma + \delta y_i$ with $\beta \ne 0$, $\delta \ne 0$, then $r_{uv} = \text{sign}\left(\beta\delta\right) r_{xy}$.

In particular the coefficient is numerically independent of origin and scale, which is the property usually quoted in the definition list. Its practical value in an examination is enormous: subtracting a convenient constant from every entry, or dividing by a common factor, cannot change the answer, and it can turn a wearying multiplication into a mental one.

### 2.3 Symmetry

> **Lemma.** $r_{xy} = r_{yx}$.

The coefficient takes no account of which quantity is the predictor. This is precisely what regression does not do, and the contrast is a standard one-mark question.

### 2.4 Slopes, spread ratio and the product identity

> **Theorem.** $b_{yx} = r_{xy}s_y/s_x$, $b_{xy} = r_{xy}s_x/s_y$ and $b_{yx}b_{xy} = r_{xy}^{2}$.

Three examination consequences follow. The sign of each slope equals the sign of $r$. The two slopes have the same sign as one another. And the geometric mean of the slopes, taken with sign, has magnitude $\lvert r\rvert$.

### 2.5 Concurrence at the centroid

> **Lemma.** Both fitted lines pass through $\left(\bar{x},\bar{y}\right)$.

This is the quickest available check on an intercept. Substituting $\bar{x}$ into the line of $Y$ on $X$ must return $\bar{y}$; if it does not, the intercept is wrong.

### 2.6 Orthogonality and the decomposition

> **Lemma.** For the least squares line of $Y$ on $X$ the residuals satisfy $\sum e_i = 0$ and $\sum x_i e_i = 0$.

> **Theorem.** $S_{yy} = SSR + SSE$ and $r_{xy}^{2} = SSR/S_{yy}$.

The orthogonality identities are exactly the two normal equations rewritten. They are the reason the decomposition carries no cross term, and therefore the reason $r^{2}$ is a clean proportion rather than an approximation.

### 2.7 The standard error relations

> **Theorem.** $s_e^{2} = \frac{n}{n-2}s_y^{2}\left(1-r_{xy}^{2}\right)$.

The factor $n/(n-2)$ is the price of estimating two constants. For $n = 10$ it is $1.25$; the standard error is therefore about twelve per cent larger than a naive $\sqrt{s_y^{2}\left(1-r^{2}\right)}$ would suggest. Examiners sometimes ask for the standard error precisely to see whether the divisor $n-2$ has been used.

### 2.8 Zero correlation is not independence

> **Theorem.** Independence implies $r_{xy} = 0$, but $r_{xy} = 0$ does not imply independence.

The standard counterexample is $y = x^{2}$ with $x$ symmetrically distributed about zero. The relationship is exact and the coefficient is zero. Any comment that claims a zero coefficient proves "no relationship" is wrong and is routinely penalised.

### 2.9 Properties of the rank coefficient

> **Theorem.** For untied ranks, $-1 \le r_s \le 1$, with equality exactly when the two orderings coincide or are exact reversals.

> **Lemma.** Spearman's coefficient equals the product-moment coefficient computed on the ranks.

Because it is a product-moment coefficient on specially simple data, every property of $r$ transfers: it is bounded, symmetric, and unchanged by any monotone relabelling that preserves order. The last property is what makes it immune to the effect of a transformation such as taking logarithms.

### 2.10 The five self-checks

| Check | What it catches |
| --- | --- |
| Is $\lvert r\rvert \le 1$? | Corrupted totals |
| Do the two slopes have the same sign? | A sign slip in one normal equation |
| Is $b_{yx}b_{xy} = r^{2}$? | A denominator taken from the wrong variable |
| Does each line return $\bar{y}$ at $\bar{x}$? | A wrong intercept |
| Is $0 \le r^{2} \le 1$ and $0 \le SSE \le S_{yy}$? | An impossible residual sum of squares |

## 3. Formal Proofs, Derivations, and Methods

### 3.1 Derivation of the computational formula

Starting from the definition and expanding the numerator,

$$
\sum\left(x_i-\bar{x}\right)\left(y_i-\bar{y}\right) = \sum x_i y_i - \bar{y}\sum x_i - \bar{x}\sum y_i + n\bar{x}\bar{y} = \sum x_i y_i - n\bar{x}\bar{y}
$$

by the zero-sum lemma applied to the means. The same expansion applied to each squared sum gives

$$
\sum\left(x_i-\bar{x}\right)^{2} = \sum x_i^{2} - n\bar{x}^{2}, \qquad \sum\left(y_i-\bar{y}\right)^{2} = \sum y_i^{2} - n\bar{y}^{2} .
$$

Substituting $n\bar{x}\bar{y} = \frac{1}{n}\sum x_i\sum y_i$ and $n\bar{x}^{2} = \frac{1}{n}\left(\sum x_i\right)^{2}$ produces

$$
r_{xy} = \frac{\sum x_i y_i - \frac{1}{n}\sum x_i\sum y_i}{\sqrt{\left[\sum x_i^{2}-\frac{1}{n}\left(\sum x_i\right)^{2}\right]\left[\sum y_i^{2}-\frac{1}{n}\left(\sum y_i\right)^{2}\right]}} .
$$

### 3.2 Proof of the bound

Put $a_i = x_i - \bar{x}$ and $b_i = y_i - \bar{y}$. Cauchy–Schwarz gives

$$
\left(\sum a_i b_i\right)^{2} \le \left(\sum a_i^{2}\right)\left(\sum b_i^{2}\right) .
$$

Taking square roots and dividing by the positive right-hand side yields $\lvert r_{xy}\rvert \le 1$. Equality requires $b_i = \lambda a_i$ for a constant $\lambda$, which is the statement that every point lies on the line $y = \bar{y} + \lambda\left(x-\bar{x}\right)$.

### 3.3 Derivation of the normal equations

The criterion is $Q(a,b) = \sum\left(y_i-a-bx_i\right)^{2}$. Expanding,

$$
Q = \sum y_i^{2} - 2a\sum y_i - 2b\sum x_i y_i + na^{2} + 2ab\sum x_i + b^{2}\sum x_i^{2} .
$$

Differentiating and equating to zero,

$$
\frac{\partial Q}{\partial a} = -2\sum y_i + 2na + 2b\sum x_i = 0, \qquad \frac{\partial Q}{\partial b} = -2\sum x_i y_i + 2a\sum x_i + 2b\sum x_i^{2} = 0 .
$$

Dividing by two and rearranging gives the pair $\sum y = na + b\sum x$ and $\sum xy = a\sum x + b\sum x^{2}$. The Hessian has determinant $4nS_{xx} > 0$ with positive leading entry, so the stationary point is the unique minimum.

### 3.4 Solving the normal equations

Dividing the first normal equation by $n$ gives $\bar{y} = a + b\bar{x}$, hence $a = \bar{y} - b\bar{x}$. Substituting into the second,

$$
\sum x_i y_i = \left(\bar{y}-b\bar{x}\right)\sum x_i + b\sum x_i^{2}
$$

which rearranges to

$$
\sum x_i y_i - n\bar{x}\bar{y} = b\left(\sum x_i^{2} - n\bar{x}^{2}\right),
$$

that is $S_{xy} = b S_{xx}$. Hence $b = S_{xy}/S_{xx}$ and $a = \bar{y}-b\bar{x}$. Exchanging the roles of the variables gives $d = S_{xy}/S_{yy}$ and $c = \bar{x}-d\bar{y}$.

### 3.5 Derivation of the slope identities

Inserting the definition of $r$ into the expression for $b_{yx}$,

$$
b_{yx} = \frac{S_{xy}}{S_{xx}} = \frac{S_{xy}}{\sqrt{S_{xx}S_{yy}}}\cdot\frac{\sqrt{S_{yy}}}{\sqrt{S_{xx}}} = r_{xy}\frac{s_y}{s_x} .
$$

Applying the same argument to the other line gives $b_{xy} = r_{xy}s_x/s_y$, and multiplying yields $b_{yx}b_{xy} = r_{xy}^{2}$.

### 3.6 Derivation of the decomposition

Write $y_i - \bar{y} = \left(\hat{y}_i-\bar{y}\right) + e_i$. Squaring and summing,

$$
S_{yy} = \sum\left(\hat{y}_i-\bar{y}\right)^{2} + 2\sum\left(\hat{y}_i-\bar{y}\right)e_i + \sum e_i^{2} .
$$

The cross term is $b\sum\left(x_i-\bar{x}\right)e_i = b\left(\sum x_i e_i - \bar{x}\sum e_i\right) = 0$ by the orthogonality identities. Hence $S_{yy} = SSR + SSE$, and since $SSR = b^{2}S_{xx} = S_{xy}^{2}/S_{xx}$,

$$
\frac{SSR}{S_{yy}} = \frac{S_{xy}^{2}}{S_{xx}S_{yy}} = r_{xy}^{2} .
$$

### 3.7 Derivation of the standard error

From $SSE = S_{yy}\left(1-r^{2}\right)$ and $s_y^{2} = S_{yy}/n$,

$$
s_e^{2} = \frac{SSE}{n-2} = \frac{S_{yy}\left(1-r^{2}\right)}{n-2} = \frac{n}{n-2}s_y^{2}\left(1-r^{2}\right) .
$$

### 3.8 Derivation of Spearman's formula

For untied ranks each series takes the values $1$ to $n$, so

$$
\sum x = \frac{n\left(n+1\right)}{2}, \qquad \sum x^{2} = \frac{n\left(n+1\right)\left(2n+1\right)}{6}
$$

and the variance of either set of ranks is

$$
\text{Var}(x) = \frac{\left(n+1\right)\left(2n+1\right)}{6} - \frac{\left(n+1\right)^{2}}{4} = \frac{n^{2}-1}{12} .
$$

Since $\bar{x} = \bar{y}$, the mean of $d = x-y$ is zero, so dividing $\sum d^{2} = \sum\left(\left(x-\bar{x}\right)-\left(y-\bar{y}\right)\right)^{2}$ by $n$ gives

$$
\frac{1}{n}\sum d^{2} = \text{Var}(x) + \text{Var}(y) - 2\,\text{Cov}(x,y) .
$$

Substituting the rank variance twice and solving,

$$
\text{Cov}(x,y) = \frac{n^{2}-1}{12} - \frac{1}{2n}\sum d^{2} .
$$

Dividing by $\frac{n^{2}-1}{12}$ produces

$$
r_s = 1 - \frac{6\sum d^{2}}{n\left(n^{2}-1\right)} .
$$

### 3.9 Why the tie correction is what it is

A group of $m$ tied values shares the average of the $m$ consecutive ranks it would have occupied. Compared with distinct ranks, the deviations of those $m$ ranks from the mean are compressed, and the sum of their squared deviations is smaller by exactly $\frac{m\left(m^{2}-1\right)}{12}$. Because the derivation of Section 3.8 assumed the full rank variance $\frac{n^{2}-1}{12}$, the computed $\sum d^{2}$ is too small and must be increased by that amount for every tied group, in each series. The corrected formula is therefore

$$
r_s = 1 - \frac{6\left[\sum d^{2} + \sum\frac{m\left(m^{2}-1\right)}{12}\right]}{n\left(n^{2}-1\right)} .
$$

### 3.10 The seven question patterns and their opening moves

**Pattern 1: describe the association.** Produce the scatter reading in one sentence, naming direction, strength, form and any unusual point. No arithmetic is usually required, but a coefficient is often accepted as support.

**Pattern 2: compute Pearson's coefficient.** Build the five-column table, obtain the totals, form $S_{xy}$, $S_{xx}$, $S_{yy}$, then divide. Interpret with direction, strength and the square.

**Pattern 3: fit one or both regression lines.** Use the normal equations, or the corrected-sum form $b = S_{xy}/S_{xx}$ with $a = \bar{y}-b\bar{x}$. Always state which variable is the subject.

**Pattern 4: predict.** Substitute into the line whose subject is the quantity to be predicted. Comment on whether the input lies inside the observed range.

**Pattern 5: comment on the adequacy of the fit.** Report $r^{2}$ as a percentage and $s_e$ in the units of the response, and say plainly what remains unexplained.

**Pattern 6: compute Spearman's coefficient.** Rank both series in the same direction, average tied ranks, form $\sum d^{2}$, add the tie correction, substitute.

**Pattern 7: reconstruct from summary values.** Use $b_{yx} = r s_y/s_x$ and $b_{xy} = r s_x/s_y$ together with the centroid to write both lines; or, given the two lines, take $r^{2}$ as the product of the slopes and the means as their intersection.

### 3.11 The standard examination routine

Step 1. Read the question and underline which variable is to be predicted, if any.

Step 2. Draw or sketch the cloud and write one sentence of description.

Step 3. Build the working table with columns for the pair, the product, and the two squares. Check each product twice.

Step 4. Add the totals row and count $n$.

Step 5. Compute $S_{xy}$, $S_{xx}$ and $S_{yy}$ and write them down explicitly, because they are separately marked.

Step 6. Compute $r$, then $r^{2}$.

Step 7. Compute the slopes and intercepts required, stating each line with its subject.

Step 8. Answer prediction parts, noting the range.

Step 9. Run the five self-checks of Section 2.10.

Step 10. Write the interpretation sentence and, where asked, the caution about causation.

### 3.12 Recovering a coefficient from two regression lines

When a question supplies the two lines in the form $a_1x + b_1y + c_1 = 0$ and $a_2x + b_2y + c_2 = 0$, three steps settle it.

Step 1. Rearrange each line so that a single variable is the subject, and identify which is the line of $Y$ on $X$ and which is the line of $X$ on $Y$ by looking at which variable has been isolated.

Step 2. Read off the two slopes as positive numbers if both lines have been written with positive slopes; then $r^{2}$ is their product and $r$ takes the common sign of the slopes.

Step 3. Solve the two lines simultaneously to obtain $\left(\bar{x},\bar{y}\right)$, since both fitted lines pass through the centroid.

The method fails if the two lines given are actually the same line, since then $r^{2} = 1$ and the mean cannot be recovered by intersection. A quick check is that the slopes must multiply to a value at most one; if they multiply to more than one, one of the equations has been misread.

## 4. Representative Worked Examples and Solutions

### 4.1 Model Solution 1: problem

Ten students recorded the hours of supervised revision they completed in a week and the mark they obtained in a test marked out of one hundred.

| Student | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Revision hours ($X$) | 4 | 6 | 7 | 9 | 10 | 12 | 13 | 15 | 16 | 18 |
| Test mark ($Y$) | 41 | 48 | 45 | 56 | 58 | 64 | 61 | 70 | 74 | 79 |

i. Compute Pearson's correlation coefficient and the coefficient of determination.
ii. Fit the two least squares regression lines.
iii. Estimate the mark of a student who revises for $14$ hours, and the revision hours of a student who scores $60$ marks.
iv. Compute the standard error of estimate and comment on the adequacy of the straight-line model.

### 4.2 Model Solution 1: solution with marking points

**Part (i).**

Step 1. Build the working table with every intermediate column.

| $X$ | $Y$ | $XY$ | $X^{2}$ | $Y^{2}$ |
| --- | --- | --- | --- | --- |
| 4 | 41 | 164 | 16 | 1,681 |
| 6 | 48 | 288 | 36 | 2,304 |
| 7 | 45 | 315 | 49 | 2,025 |
| 9 | 56 | 504 | 81 | 3,136 |
| 10 | 58 | 580 | 100 | 3,364 |
| 12 | 64 | 768 | 144 | 4,096 |
| 13 | 61 | 793 | 169 | 3,721 |
| 15 | 70 | 1,050 | 225 | 4,900 |
| 16 | 74 | 1,184 | 256 | 5,476 |
| 18 | 79 | 1,422 | 324 | 6,241 |
| $\sum 110$ | $\sum 596$ | $\sum 7{,}068$ | $\sum 1{,}400$ | $\sum 36{,}944$ |

Step 2. Record $n = 10$ and compute the three corrected sums.

$$
S_{xy} = 7{,}068 - \frac{1}{10}\left(110\right)\left(596\right) = 7{,}068 - 6{,}556 = 512
$$

$$
S_{xx} = 1{,}400 - \frac{1}{10}\left(110\right)^{2} = 1{,}400 - 1{,}210 = 190
$$

$$
S_{yy} = 36{,}944 - \frac{1}{10}\left(596\right)^{2} = 36{,}944 - 35{,}521.6 = 1{,}422.4
$$

Step 3. Compute the coefficient.

$$
r_{xy} = \frac{512}{\sqrt{\left(190\right)\left(1{,}422.4\right)}} = \frac{512}{\sqrt{270{,}256}} = \frac{512}{519.86} \approx 0.9849
$$

Step 4. Compute the coefficient of determination.

$$
r^{2} = 0.9849^{2} \approx 0.9700
$$

**Part (ii).**

Step 5. Compute the slope of $Y$ on $X$.

$$
b_{yx} = \frac{S_{xy}}{S_{xx}} = \frac{512}{190} = 2.6947
$$

Step 6. Compute the intercept of $Y$ on $X$ from the means $\bar{x} = 11$ and $\bar{y} = 59.6$.

$$
a = 59.6 - \left(2.6947\right)\left(11\right) = 59.6 - 29.642 = 29.958
$$

$$
Y = 29.958 + 2.6947X
$$

Step 7. Compute the slope of $X$ on $Y$.

$$
b_{xy} = \frac{S_{xy}}{S_{yy}} = \frac{512}{1{,}422.4} = 0.3600
$$

Step 8. Compute the second intercept.

$$
c = 11 - \left(0.3600\right)\left(59.6\right) = 11 - 21.453 = -10.453
$$

$$
X = -10.453 + 0.3600Y
$$

Step 9. Verify the product identity.

$$
\left(2.6947\right)\left(0.3600\right) = 0.9701 \approx r^{2}
$$

**Part (iii).**

Step 10. Estimate the mark at $14$ hours using the line of $Y$ on $X$.

$$
Y = 29.958 + 2.6947\left(14\right) = 29.958 + 37.726 = 67.68
$$

Step 11. Estimate the revision hours at $60$ marks using the line of $X$ on $Y$.

$$
X = -10.453 + 0.3600\left(60\right) = -10.453 + 21.600 = 11.15
$$

Step 12. Note the range. The observed revision hours run from $4$ to $18$ and the observed marks from $41$ to $79$, so both inputs lie inside the observed ranges and neither answer is an extrapolation.

**Part (iv).**

Step 13. Compute the residual sum of squares.

$$
SSE = S_{yy}\left(1-r^{2}\right) = 1{,}422.4\left(0.03002\right) = 42.70
$$

Step 14. Compute the standard error of estimate with divisor $n-2 = 8$.

$$
s_e = \sqrt{\frac{42.70}{8}} = \sqrt{5.3375} \approx 2.31
$$

Step 15. Comment. The coefficient of determination says that about ninety-seven per cent of the variation in test marks is accounted for by the straight-line relation with revision hours, and the standard error says that a prediction is typically wrong by about $2.3$ marks. The model is therefore a good one over the observed range, but the comment should stop short of claiming that revision causes the marks: the two quantities were merely observed together.

**Marking points.**

- Table of five columns with a correct totals row: 3 marks, awarded one each for the products, the $X$ squares and the $Y$ squares.
- The three corrected sums stated explicitly: 3 marks.
- Coefficient correct to four significant figures: 2 marks.
- Coefficient of determination with a percentage interpretation: 1 mark.
- Each regression line, correct coefficients and correct subject: 2 marks each.
- Each prediction: 1 mark each.
- Statement that both inputs lie inside the observed range: 1 mark.
- Standard error with divisor $n-2$: 2 marks.
- Interpretation sentence naming direction, strength, proportion explained and the caution about causation: 2 marks.

### 4.3 Model Solution 2: problem

Two assessors graded eight projects. Grades are to be compared by ordering. The marks awarded are recorded.

| Project | A | B | C | D | E | F | G | H |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Assessor 1 ($X$) | 82 | 75 | 75 | 90 | 66 | 58 | 90 | 71 |
| Assessor 2 ($Y$) | 78 | 80 | 72 | 85 | 60 | 55 | 88 | 74 |

Compute Spearman's rank correlation coefficient and interpret it.

### 4.4 Model Solution 2: solution with marking points

Step 1. Rank the $X$ marks from smallest to largest. In ascending order the marks are $58$, $66$, $71$, $75$, $75$, $82$, $90$, $90$. The value $75$ occurs twice and would occupy ranks $4$ and $5$, so each takes $4.5$. The value $90$ occurs twice and would occupy ranks $7$ and $8$, so each takes $7.5$.

Step 2. Rank the $Y$ marks in the same direction. The ascending order is $55$, $60$, $72$, $74$, $78$, $80$, $85$, $88$, and no value repeats, so the ranks are $1$ to $8$ in that order.

Step 3. Record the ranks, the differences and the squared differences.

| Project | $X$ | $Y$ | Rank of $X$ | Rank of $Y$ | $d$ | $d^{2}$ |
| --- | --- | --- | --- | --- | --- | --- |
| A | 82 | 78 | 6 | 5 | 1 | 1 |
| B | 75 | 80 | 4.5 | 6 | -1.5 | 2.25 |
| C | 75 | 72 | 4.5 | 3 | 1.5 | 2.25 |
| D | 90 | 85 | 7.5 | 7 | 0.5 | 0.25 |
| E | 66 | 60 | 2 | 2 | 0 | 0 |
| F | 58 | 55 | 1 | 1 | 0 | 0 |
| G | 90 | 88 | 7.5 | 8 | -0.5 | 0.25 |
| H | 71 | 74 | 3 | 4 | -1 | 1 |
| Total | | | | | | $\sum 7$ |

Step 4. Compute the tie correction for the $X$ series. The value $75$ occurs twice and the value $90$ occurs twice.

$$
\frac{2\left(2^{2}-1\right)}{12} = 0.5, \qquad \frac{2\left(2^{2}-1\right)}{12} = 0.5
$$

The $X$ series therefore contributes $1$. The $Y$ series has no ties and contributes $0$. The combined correction is $1$.

Step 5. Compute the denominator.

$$
n\left(n^{2}-1\right) = 8\left(64-1\right) = 504
$$

Step 6. Substitute into the corrected formula.

$$
r_s = 1 - \frac{6\left(7 + 1\right)}{504} = 1 - \frac{48}{504} = 1 - 0.0952 = 0.9048
$$

Step 7. Interpret. A rank coefficient of $0.905$ indicates very strong agreement between the two orderings. Project F is placed last by both assessors and project E is placed second last by both, which is where most of the agreement comes from; the only material disagreement concerns projects B and C, which the two assessors order differently.

**Marking points.**

- Ranks for the first series with averaged ties: 2 marks.
- Ranks for the second series: 1 mark.
- Table of differences and squared differences: 2 marks.
- Tie correction identified and evaluated as $1$: 2 marks.
- Denominator $504$ and final answer $0.9048$: 2 marks.
- Interpretation naming strength and identifying the source of disagreement: 2 marks.

### 4.5 Model Solution 3: problem

For ten days of trading, the following totals were recorded for advertising expenditure $X$ and sales $Y$, both in hundreds of units of currency: $n = 10$, $\sum x = 120$, $\sum y = 250$, $\sum xy = 3{,}400$, $\sum x^{2} = 1{,}700$, $\sum y^{2} = 7{,}000$. The values of $X$ lay between $2$ and $20$.

i. Compute the correlation coefficient and the coefficient of determination.
ii. Obtain both regression lines.
iii. Predict sales when advertising expenditure is $15$ and comment on a prediction at $40$.

### 4.6 Model Solution 3: solution with marking points

Step 1. Compute the three corrected sums.

$$
S_{xy} = 3{,}400 - \frac{1}{10}\left(120\right)\left(250\right) = 3{,}400 - 3{,}000 = 400
$$

$$
S_{xx} = 1{,}700 - \frac{1}{10}\left(120\right)^{2} = 1{,}700 - 1{,}440 = 260
$$

$$
S_{yy} = 7{,}000 - \frac{1}{10}\left(250\right)^{2} = 7{,}000 - 6{,}250 = 750
$$

Step 2. Compute the coefficient.

$$
r_{xy} = \frac{400}{\sqrt{\left(260\right)\left(750\right)}} = \frac{400}{\sqrt{195{,}000}} = \frac{400}{441.59} \approx 0.9058
$$

Step 3. Compute the coefficient of determination.

$$
r^{2} = 0.9058^{2} \approx 0.8205
$$

Step 4. Compute the means.

$$
\bar{x} = \frac{120}{10} = 12, \qquad \bar{y} = \frac{250}{10} = 25
$$

Step 5. Fit the line of $Y$ on $X$.

$$
b_{yx} = \frac{400}{260} = 1.5385, \qquad a = 25 - \left(1.5385\right)\left(12\right) = 25 - 18.462 = 6.538
$$

$$
Y = 6.538 + 1.5385X
$$

Step 6. Fit the line of $X$ on $Y$.

$$
b_{xy} = \frac{400}{750} = 0.5333, \qquad c = 12 - \left(0.5333\right)\left(25\right) = 12 - 13.333 = -1.333
$$

$$
X = -1.333 + 0.5333Y
$$

Step 7. Verify the product identity and the centroid.

$$
\left(1.5385\right)\left(0.5333\right) = 0.8205 = r^{2}
$$

$$
6.538 + 1.5385\left(12\right) = 25
$$

Step 8. Predict sales at an advertising expenditure of $15$.

$$
Y = 6.538 + 1.5385\left(15\right) = 6.538 + 23.078 = 29.62
$$

Step 9. Comment on a prediction at $40$. The observed expenditure lay between $2$ and $20$, so $40$ is outside the data and the answer would be an extrapolation. Evaluating it anyway gives

$$
Y = 6.538 + 1.5385\left(40\right) = 6.538 + 61.540 = 68.08
$$

which grossly exceeds anything the ten recorded days produced and should not be reported as a forecast. No evidence in the data supports the assumption that the straight track continues beyond $20$.

**Marking points.**

- Three corrected sums: 3 marks.
- Coefficient: 2 marks; determination with interpretation: 1 mark.
- Both means: 1 mark.
- Each line: 2 marks.
- Verification using $b_{yx}b_{xy} = r^{2}$: 1 mark.
- Prediction at $15$: 1 mark.
- Recognition that $40$ is outside the observed range and a clear statement that the result is an extrapolation: 2 marks.

### 4.7 Model Solution 4: problem

The two lines of regression of $Y$ on $X$ and of $X$ on $Y$ are given as

$$
0.8X - Y + 12 = 0
$$

$$
X - 0.45Y - 1 = 0 .
$$

Find the coefficient of correlation and the means of $X$ and $Y$.

### 4.8 Model Solution 4: solution with marking points

Step 1. Rearrange the first line to make $Y$ its subject.

$$
Y = 12 + 0.8X
$$

This is the line of $Y$ on $X$, so $b_{yx} = 0.8$.

Step 2. Rearrange the second line to make $X$ its subject.

$$
X = 1 + 0.45Y
$$

This is the line of $X$ on $Y$, so $b_{xy} = 0.45$.

Step 3. Obtain $r^{2}$ as the product of the two slopes.

$$
r^{2} = b_{yx}b_{xy} = \left(0.8\right)\left(0.45\right) = 0.36
$$

Step 4. Take the positive square root, because both slopes are positive.

$$
r_{xy} = \sqrt{0.36} = 0.6
$$

Step 5. Solve the two lines simultaneously, since both pass through the centroid.

$$
X = 1 + 0.45\left(12 + 0.8X\right) = 1 + 5.4 + 0.36X
$$

$$
0.64X = 6.4 \quad\Rightarrow\quad \bar{x} = 10
$$

Step 6. Recover the mean of $Y$ from either line.

$$
\bar{y} = 12 + 0.8\left(10\right) = 20
$$

Step 7. Check both equations at the point $\left(10, 20\right)$.

$$
0.8\left(10\right) - 20 + 12 = 0, \qquad 10 - 0.45\left(20\right) - 1 = 0
$$

Step 8. Report the ratio of spreads implied by the slopes, as a check.

$$
\frac{s_y}{s_x} = \frac{b_{yx}}{r} = \frac{0.8}{0.6} = 1.333, \qquad r\frac{s_x}{s_y} = 0.6\left(0.75\right) = 0.45
$$

The second calculation reproduces $b_{xy}$, so the two slopes are mutually consistent.

**Marking points.**

- Both lines rearranged with the correct subject: 2 marks.
- Identification of the two slopes: 1 mark.
- Product of the slopes and the value $r^{2} = 0.36$: 2 marks.
- Correct sign of $r$ with a reason: 1 mark.
- Simultaneous solution for the means: 3 marks.
- Check that both equations vanish at the centroid: 1 mark.

### 4.9 Model Solution 5: problem

The coefficient of rank correlation between two sets of ranks is $0.8$ and the sum of squares of the differences in ranks is $33$. Find the number of individuals ranked.

### 4.10 Model Solution 5: solution with marking points

Step 1. Write the untied formula and substitute the known values.

$$
0.8 = 1 - \frac{6\left(33\right)}{n\left(n^{2}-1\right)}
$$

Step 2. Rearrange so that the unknown appears on one side.

$$
\frac{198}{n\left(n^{2}-1\right)} = 0.2
$$

Step 3. Invert.

$$
n\left(n^{2}-1\right) = \frac{198}{0.2} = 990
$$

Step 4. Solve by inspection, since $n$ is a positive integer. For $n = 10$,

$$
10\left(100 - 1\right) = 10\left(99\right) = 990
$$

Step 5. Confirm that no smaller integer works. For $n = 9$ the value is $9\left(80\right) = 720$, which is below $990$; for $n = 11$ it is $11\left(120\right) = 1{,}320$, which is above. The solution is unique.

$$
n = 10
$$

Step 6. Report. Ten individuals were ranked, and since the data contain no ties the correction term does not arise.

**Marking points.**

- Correct substitution into the rank formula: 1 mark.
- Correct rearrangement to $n\left(n^{2}-1\right) = 990$: 2 marks.
- Value $n = 10$: 2 marks.
- Justification that the integer solution is unique: 1 mark.

## 5. Mathematical Extensions, Limits, and Common Errors

### 5.1 The trap catalogue

| Trap | How it appears | The correction |
| --- | --- | --- |
| Swapping the variables in a regression line | Fitting $X = c + dY$ when $Y$ on $X$ was asked | The subject names the predicted variable |
| Using the wrong line for a prediction | Rearranging $Y = a + bX$ to predict $X$ | Use $X = c + dY$ instead |
| Miscomputing ranks with ties | Giving tied values consecutive ranks | Average the ranks they would have occupied |
| Omitting the tie correction | Using the untied formula on tied data | Add $\frac{m\left(m^{2}-1\right)}{12}$ per tied group |
| Extrapolating silently | Predicting far outside the observed range | State the range and label the answer |
| Reporting $r^{2}$ as $r$ | Quoting $0.81$ when the coefficient is $0.9$ | Take the square root and restore the sign |
| Losing the sign of $r$ | Taking a positive square root by habit | The sign is the sign of $S_{xy}$ |
| Omitting $\frac{1}{n}$ in a corrected sum | Subtracting $\sum x\sum y$ instead of $\frac{1}{n}\sum x\sum y$ | The factor is unavoidable |
| Using $n$ instead of $n-2$ for $s_e$ | Dividing the residual sum of squares by $n$ | Two parameters were estimated |
| Reading a zero coefficient as no relationship | Concluding independence from $r = 0$ | Zero rules out only a linear component |

### 5.2 Trap 1: swapping the variables in the regression line

The line of $Y$ on $X$ minimises vertical gaps; the line of $X$ on $Y$ minimises horizontal gaps. They are different lines, and neither is a rearrangement of the other. A question that says "regress $Y$ on $X$" wants the equation with $Y$ alone on the left and the slope $S_{xy}/S_{xx}$. Writing the equation with $X$ alone on the left has answered a different question and normally attracts no marks, even if the coefficients are internally consistent.

The distinction is easy to remember through the denominator: the line whose subject is $Y$ carries $S_{xx}$ underneath, because $X$ is the predictor whose variation has to be scaled away. The line whose subject is $X$ carries $S_{yy}$ underneath.

### 5.3 Trap 2: predicting with the wrong line

Rewriting $Y = a + bX$ as $X = \left(Y-a\right)/b$ produces an equation that looks like a regression of $X$ on $Y$ but is not one. The reciprocal $1/b$ of a slope has nothing to do with the true slope $d = S_{xy}/S_{yy}$, and the gap between them can be enormous when the correlation is weak.

Take the eight students whose calculus marks $X$ and statistics marks $Y$ give $S_{xy} = 129$, $S_{xx} = 818$ and $S_{yy} = 276$. The correct lines are $Y = 37.115 + 0.1577X$ and $X = 28.967 + 0.4674Y$. The reciprocal of the first slope is enormous compared with the true second slope.

$$
\frac{1}{0.1577} = 6.341 \quad\text{whereas}\quad d = 0.4674
$$

A student who scores $50$ in statistics is therefore predicted to have a calculus mark of

$$
X = 28.967 + 0.4674\left(50\right) = 52.34 .
$$

A candidate who instead rearranges the first line obtains

$$
X = \frac{50 - 37.115}{0.1577} = \frac{12.885}{0.1577} = 81.7,
$$

which is out by nearly thirty marks. The rearrangement is not a small approximation error; it is the wrong line, and it always exaggerates the distance of the prediction from the mean.

### 5.4 Trap 3: ranks with ties

Tied values must share the average of the ranks they would have occupied, and the correction must then be added. Both parts are examinable.

Reconsider the eight projects graded by two assessors, where the first assessor gave two marks of $75$ and two of $90$. Suppose the tied marks were given consecutive ranks instead, taking $4$ and $5$ for the two $75$ marks and $7$ and $8$ for the two $90$ marks. Choosing the arrangement $6, 4, 5, 7, 2, 1, 8, 3$ for the ranks of $X$ gives differences $1$, $-2$, $2$, $0$, $0$, $0$, $0$, $-1$ and a sum of squared differences of $10$. Without any correction,

$$
r_s = 1 - \frac{6\left(10\right)}{504} = 1 - 0.1190 = 0.8810 .
$$

The correct answer is $0.9048$. The wrong method has understated the agreement by about two and a half percentage points, and it has done so by an amount that depends on how the tied marks were arbitrarily ordered, which is the clearest sign that the method is unsound.

A second error is to correct one series only. If the correction of $1$ had been omitted while the averaged ranks were retained, the answer would have been $1 - 42/504 = 0.9167$, which overstates the agreement. The correction is applied in both series, whether or not both contain ties.

### 5.5 Trap 4: extrapolation

A fitted line has no authority outside the range of the predictor that was observed. In the ten-student example the revision hours ran from $4$ to $18$, and the line $Y = 29.958 + 2.6947X$ gives

$$
29.958 + 2.6947\left(30\right) = 110.8
$$

for a student who revises for thirty hours. The test is marked out of one hundred, so the prediction is not merely uncertain, it is impossible. When a question asks for a prediction outside the observed range, the full-mark answer is to give the arithmetic and then say plainly that the value is an extrapolation and that the linear relation has not been shown to hold there.

### 5.6 Trap 5: reading the square as the coefficient, and losing the sign

The two numbers $r$ and $r^{2}$ are frequently interchanged under time pressure. A coefficient of determination of $0.81$ belongs to a correlation of $0.9$ in magnitude, and a determination of $0.49$ belongs to a correlation of $0.7$. Reporting the determination where the coefficient was requested is an error of substance, not of presentation, because the two describe different things: $r$ measures the closeness of the straight track, while $r^{2}$ measures the proportion of variation accounted for.

The sign is lost in the reverse direction, when a candidate recovers $r$ from $r^{2}$ mechanically. There is no information in $r^{2}$ about direction; the sign must be taken from the sign of $S_{xy}$, from the sign of either regression slope, or from the direction of the cloud.

### 5.7 The comment mark: correlation, causation and the limits of the model

Nearly every question on this topic ends with the word "comment" or "interpret". A complete comment does four things and no more.

First, name the direction: positive or negative, in the language of the two variables rather than in the language of symbols. Second, name the strength, using the square as well as the coefficient: "strong, with about ninety-seven per cent of the variation in marks accounted for". Third, name the limits: the range over which the model was fitted, and any unusual observation that influenced it. Fourth, refuse the causal claim explicitly, because the data are observational.

The fourth point deserves elaboration, since it is the one most often missed. Three alternatives to causation must be considered. A **common cause** may drive both variables, as hot weather drives both ice-cream sales and drowning deaths. **Reverse causation** may run the other way, so that the response influences the predictor rather than the contrary. And plain **coincidence** will produce strong correlations between series that merely trend together over time. Only a controlled experiment, in which the predictor is varied deliberately and everything else is held fixed, can separate these explanations. A regression line is a description of how a response co-varies with a predictor in the observed data; it is not a mechanism, and no amount of arithmetic turns it into one.

### 5.8 Revision checklist

- Can you write the five definitions from memory, including the phrase "degree of linear relationship"?
- Can you state all three forms of Pearson's coefficient and say when each is convenient?
- Can you produce a correct five-column working table for ten pairs in under four minutes?
- Can you compute $S_{xy}$, $S_{xx}$ and $S_{yy}$ without consulting a formula sheet?
- Can you state both normal equation systems and solve them by elimination as well as by the corrected-sum shortcut?
- Can you write both regression lines with the correct subject and the correct denominator?
- Can you quote $b_{yx}b_{xy} = r^{2}$ and use it as a check?
- Can you explain why the two lines differ, in one sentence about vertical and horizontal gaps?
- Can you compute and interpret $r^{2}$ as a percentage?
- Can you compute $s_e$ with the divisor $n-2$ and say what its units are?
- Can you rank a series with ties by averaging, and evaluate the correction $\frac{m\left(m^{2}-1\right)}{12}$?
- Can you recover $r$ and the two means from two given regression lines?
- Can you invert the rank formula to find $n$ from $r_s$ and $\sum d^{2}$?
- Can you give three reasons why a correlation does not establish causation?
- Can you explain in one sentence why extrapolation is unsafe?

### 5.9 Time strategy in the examination

A question of this type is worth between twelve and twenty marks and should be allocated about one and a half minutes per mark.

**First two minutes.** Read the whole question and underline every quantity that must be produced. Decide which variable is the predictor in each part. Sketch the cloud roughly if the raw data are given; the sketch costs thirty seconds and yields the description sentence.

**Next six to eight minutes.** Build the working table. Check each product and each square as it is written, because a single error here contaminates everything downstream. Add the totals twice.

**Next four minutes.** Compute the three corrected sums and the coefficient. Write each corrected sum on its own line, since they are separately marked. Compute the two slopes and the two intercepts only if the question asks for them.

**Next two minutes.** Answer the prediction parts, then run the five self-checks. A failed check costs a minute to trace and saves several marks.

**Last two to three minutes.** Write the interpretation. Four sentences are enough: direction, strength with the square, the observed range, and the refusal of a causal claim. This is the cheapest block of marks in the whole question and it is the one most often abandoned when time runs short, so it should be written before any optional refinement of the arithmetic.

Two habits protect the time budget. Carry at least four significant figures through the intermediate stages and round only the final answer, because squaring amplifies early rounding. And never restart a table from scratch on discovering an error: locate the single wrong cell, correct it, and adjust the totals, which takes a fraction of the time.

### 5.10 The topic in one paragraph

Two quantities measured together are described by a scatter diagram, summarised by a coefficient that lies between minus one and one and carries no units, and used for prediction through two different least squares lines whose slopes multiply to the square of that coefficient. The square reports the proportion of variation accounted for; the standard error reports the typical size of the leftover error in the units of the response. When only order is available, ranks replace values and a small correction repairs the effect of ties. The coefficient changes when a single unusual point is added, says nothing whatever about curvature, and says nothing whatever about cause. Used within its range, with its residual scatter reported alongside it, the fitted line is one of the most useful summaries in statistics; used outside that range, or read as a mechanism, it is one of the most misleading.
