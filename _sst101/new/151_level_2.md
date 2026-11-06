## 1. Foundational Concepts, Definitions, and Axioms

### 1.1 The bivariate problem: description and prediction

Bivariate analysis is the study of two quantities measured on the same individuals or occasions. It contains two distinct activities that are frequently confused and must be kept apart.

**Correlation analysis** deals with the association between two or more variables. It asks whether a relationship exists, how strong it is, and in which direction it runs. It is symmetric: neither quantity is privileged, and interchanging them leaves every conclusion untouched.

**Regression analysis** attempts to establish the nature of the relationship. It asks: given a value of one quantity, what value of the other should be predicted? It is asymmetric: one quantity is designated the independent, explanatory or predictor variable, and the other the dependent or response variable.

The distinction is not pedantic. A symmetric summary cannot answer a directional question, and a directional fit cannot answer a symmetric one. Everything that follows divides along this line.

### 1.2 The scatter diagram and the visual grammar of association

Before any coefficient is computed, the paired data should be plotted. Each observation contributes a point with the first quantity measured along the horizontal axis and the second along the vertical axis. The resulting cloud is the **scatter diagram**, and its features organise the whole subject.

Four features are read from the cloud.

**Direction.** If the cloud rises as it moves to the right, the association is **positive**: large values of one quantity accompany large values of the other, and small values accompany small values. If the cloud falls as it moves to the right, the association is **negative**.

**Strength.** A cloud confined to a narrow band along a straight track indicates a strong linear association. A cloud filling a roughly circular or elliptical region with the long axis only weakly marked indicates a weak one. Strength refers to the narrowness of the band, not to its steepness.

**Form.** The band may be straight or curved. Correlation and the regression lines developed here describe straight bands. A pronounced curve produces a coefficient that understates the tightness of the relationship, sometimes severely; a symmetric curve such as a parabola produces a coefficient near zero even though the relationship is exact.

**Unusual points.** A single point far from the band, or a small group separated from the main cloud, can dominate every summary statistic computed from the data. Such points are called **influential**, and their influence on the coefficient can be assessed only by recomputing with the point removed.

A fifth feature, less often discussed but important in practice, is **clustering**. If the cloud contains two or more distinct groups, the association computed over the whole cloud may be entirely due to the separation of the groups and may be absent, or even reversed, within each group.

### 1.3 Notation and the algebra of sums

Let $(x_1, y_1), \dots, (x_n, y_n)$ be $n$ paired observations. The means are

$$
\bar{x} = \frac{1}{n}\sum_{i=1}^{n} x_i, \qquad \bar{y} = \frac{1}{n}\sum_{i=1}^{n} y_i .
$$

Two quantities recur so often that they are given names. The **corrected sums of squares and products** are

$$
S_{xx} = \sum_{i=1}^{n}\left(x_i - \bar{x}\right)^{2}, \qquad S_{yy} = \sum_{i=1}^{n}\left(y_i - \bar{y}\right)^{2}, \qquad S_{xy} = \sum_{i=1}^{n}\left(x_i - \bar{x}\right)\left(y_i - \bar{y}\right) .
$$

The descriptive variances and covariance use the divisor $n$.

$$
s_x^{2} = \frac{S_{xx}}{n}, \qquad s_y^{2} = \frac{S_{yy}}{n}, \qquad \text{Cov}(x,y) = \frac{S_{xy}}{n}
$$

The three corrected sums can be obtained without computing individual deviations, by the identities

$$
S_{xx} = \sum x_i^{2} - \frac{1}{n}\left(\sum x_i\right)^{2}, \qquad S_{yy} = \sum y_i^{2} - \frac{1}{n}\left(\sum y_i\right)^{2}, \qquad S_{xy} = \sum x_i y_i - \frac{1}{n}\sum x_i \sum y_i .
$$

> **Lemma (Zero-sum).** $\sum_{i=1}^{n}\left(x_i - \bar{x}\right) = 0$ and $\sum_{i=1}^{n}\left(y_i - \bar{y}\right) = 0$.

The lemma follows from $\sum x_i = n\bar{x}$. It matters because it licenses the algebraic step used repeatedly below: a sum of products of deviations may be expanded by replacing $\sum x_i$ with $n\bar{x}$ wherever it appears.

### 1.4 Covariance: definition, sign and units

> **Definition (Covariance).** The covariance of two variates is

$$
\text{Cov}(x,y) = \frac{1}{n}\sum_{i=1}^{n}\left(x_i - \bar{x}\right)\left(y_i - \bar{y}\right) .
$$

The product $\left(x_i - \bar{x}\right)\left(y_i - \bar{y}\right)$ is positive when the observation lies in the same direction from both means and negative when it lies in opposite directions. The covariance is therefore the average of a collection of signed products, and its sign reports the predominant behaviour of the cloud.

The covariance is **bilinear**: for constants $\alpha, \beta, \gamma, \delta$,

$$
\text{Cov}(\alpha + \beta x, \gamma + \delta y) = \beta\delta\,\text{Cov}(x,y) .
$$

It is also symmetric, $\text{Cov}(x,y) = \text{Cov}(y,x)$, and it satisfies $\text{Cov}(x,x) = \text{Var}(x)$. Those three facts make it the natural building block for everything else, and they are also its limitation: the covariance carries the units of $x$ multiplied by the units of $y$, so its numerical size cannot be interpreted as a strength. Doubling the unit in which $x$ is measured doubles the covariance while changing nothing about the data.

### 1.5 Pearson's product-moment coefficient

> **Definition (Coefficient of correlation).** As a measure of the degree of linear relationship between the variates, the coefficient of correlation is defined by

$$
r_{xy} = \frac{\text{Cov}(x,y)}{\sqrt{\text{Var}(x) \times \text{Var}(y)}} .
$$

Substituting the definitions of the covariance and the two variances,

$$
r_{xy} = \frac{\frac{1}{n}\sum\left(x_i - \bar{x}\right)\left(y_i - \bar{y}\right)}{\sqrt{\left[\frac{1}{n}\sum\left(x_i - \bar{x}\right)^{2}\right]\left[\frac{1}{n}\sum\left(y_i - \bar{y}\right)^{2}\right]}} .
$$

This is the **product-moment formula for linear correlation**, also called Karl Pearson's correlation coefficient. An equivalent reading is that $r$ is the covariance of the two quantities after each has been standardised to unit spread. Standardisation removes the units, and what remains is a pure number lying between $-1$ and $1$.

### 1.6 The computational form and the short method

Multiplying out the definition and cancelling the common factor $\frac{1}{n}$ produces the computational form.

$$
r_{xy} = \frac{n\sum x_i y_i - \sum x_i \sum y_i}{\sqrt{\left\{\left[n\sum x_i^{2} - \left(\sum x_i\right)^{2}\right]\left[n\sum y_i^{2} - \left(\sum y_i\right)^{2}\right]\right\}}}
$$

Dividing numerator and denominator by $n$ gives the compact version in corrected sums.

$$
r_{xy} = \frac{S_{xy}}{\sqrt{S_{xx}\,S_{yy}}}
$$

Because $r$ is unchanged by a shift of origin and by a positive change of scale, the arithmetic may be performed on **coded** quantities $u_i = x_i - A$ and $v_i = y_i - B$, or on scaled quantities $u_i = \left(x_i - A\right)/h$ and $v_i = \left(y_i - B\right)/k$ with $h, k > 0$. Either coding preserves the coefficient exactly. Choosing $A$ and $B$ near the centres of the respective lists, and $h$ and $k$ equal to convenient round steps, reduces the numbers involved and removes most of the risk of arithmetic error.

### 1.7 Simple linear regression and the least squares criterion

For studying the relationship between two variables $X$ and $Y$, the simplest regression equation is of the form

$$
Y = a + bX
$$

where $a$ and $b$ are constants. This equation specifies the linear regression of $Y$ on $X$. The constant $b$, which is the slope of the regression line, is called the **coefficient of regression of $Y$ on $X$**.

The constants are not chosen by eye but by a rule. For any candidate values of $a$ and $b$, the fitted value at $x_i$ is $a + bx_i$ and the residual is $y_i - a - bx_i$. The **least squares criterion** selects the pair $(a, b)$ minimising the residual sum of squares

$$
Q(a,b) = \sum_{i=1}^{n}\left(y_i - a - bx_i\right)^{2} .
$$

> **Definition (Least squares regression line of $Y$ on $X$).** The regression line of $Y$ on $X$ is $Y = a + bX$, where $a$ and $b$ satisfy the **normal equations**

$$
\sum y = na + b\sum x
$$

> and

$$
\sum xy = a\sum x + b\sum x^{2} .
$$

> **Definition (Least squares regression line of $X$ on $Y$).** The regression line of $X$ on $Y$ is $X = c + dY$, where $c$ and $d$ satisfy the normal equations

$$
\sum x = nc + d\sum y
$$

> and

$$
\sum xy = c\sum y + d\sum y^{2} .
$$

The structural parallel is exact. In each system the first equation is obtained by summing the line equation over all observations; the second is obtained by multiplying the line equation by the explanatory variable and then summing. Section 3 derives both systems from the minimisation problem.

### 1.8 The two regression lines and why they differ

Regression is directional, so two lines exist. The line of $Y$ on $X$ is obtained by minimising vertical distances from the points to the line. The line of $X$ on $Y$ is obtained by minimising horizontal distances. Because a vertical gap and a horizontal gap of the same absolute size are different lengths in the plane, the two minimisations select different lines.

The two lines coincide only when every point lies exactly on a single straight track, which is precisely the case $r^{2} = 1$. In every other case the line of $Y$ on $X$ is the shallower of the two when both are drawn as a graph of $Y$ against $X$: its slope is smaller in magnitude than the slope of the other line once that other line has also been written with $Y$ as the subject. That is why using the wrong line for a prediction always produces an answer pulled towards the mean of the response.

### 1.9 Determination and the standard error of estimate

> **Definition (Coefficient of determination).** The coefficient of determination is $r_{xy}^{2}$.

Its interpretation rests on the decomposition of the total sum of squares of the response into a part accounted for by the fitted line and a part left in the residuals.

$$
S_{yy} = SSR + SSE
$$

Here $SSR = \sum\left(\hat{y}_i - \bar{y}\right)^{2}$ is the regression sum of squares and $SSE = \sum\left(y_i - \hat{y}_i\right)^{2}$ is the residual sum of squares. Dividing by $S_{yy}$ shows that $r^{2} = SSR/S_{yy}$ is the proportion of the total variation explained by the straight-line fit.

> **Definition (Standard error of estimate).** For the fitted line of $Y$ on $X$,

$$
s_e = \sqrt{\frac{SSE}{n-2}} .
$$

The divisor $n-2$ reflects the two degrees of freedom consumed by estimating the intercept and the slope. The quantity is measured in the units of $Y$ and estimates the standard deviation of the residuals, so it describes the typical size of the vertical error made by the fitted line.

### 1.10 Ranks and Spearman's coefficient

When the values are ordinal, or when the numerical scale is unreliable, association is measured on ranks.

> **Definition (Spearman's rank correlation coefficient).** Let $n$ be the number of individuals ranked according to two characters $A$ and $B$, and let $x$ and $y$ be the ranks with respect to $A$ and $B$. If no rank is repeated in either series, both take the values $1, 2, \dots, n$ and

$$
r_s = 1 - \frac{6\sum d^{2}}{n\left(n^{2}-1\right)}
$$

> where $d = x - y$ is the difference between the ranks.

When any value is repeated, the tied individuals share the average of the ranks they would otherwise have occupied, and the sum of squared differences must be corrected.

$$
r_s = 1 - \frac{6\left[\sum d^{2} + \sum \frac{m\left(m^{2}-1\right)}{12}\right]}{n\left(n^{2}-1\right)}
$$

The inner sum runs over every group of tied values, and $m$ is the number of values in that group. The correction is added inside the bracket, so it always reduces the size of $r_s$.

### 1.11 Summary of notation

| Symbol | Meaning | Divider |
| --- | --- | --- |
| $n$ | Number of paired observations | None |
| $\bar{x}$, $\bar{y}$ | Means of the two lists | None |
| $S_{xx}$, $S_{yy}$ | Corrected sums of squares | None |
| $S_{xy}$ | Corrected sum of products | None |
| $s_x$, $s_y$ | Standard deviations | $n$ |
| $\text{Cov}(x,y)$ | Covariance | $n$ |
| $r_{xy}$ | Pearson's coefficient | None |
| $b_{yx}$, $b_{xy}$ | Regression slopes | None |
| $s_e$ | Standard error of estimate | $n-2$ |
| $r_s$ | Spearman's coefficient | None |

## 2. Theorems, Lemmas, and Analytical Properties

### 2.1 Boundedness

> **Theorem (Boundedness of the correlation coefficient).** For any paired observations with $S_{xx} > 0$ and $S_{yy} > 0$,

$$
-1 \le r_{xy} \le 1 .
$$

Equivalently, $\lvert r_{xy}\rvert \le 1$. The bound is an instance of the Cauchy–Schwarz inequality applied to the vectors of deviations, and the proof appears in Section 3. Its practical content is that $r$ has a fixed scale, so a value of $0.5$ means the same thing in a study of blood pressure and in a study of examination marks.

### 2.2 The equality cases

> **Theorem (Perfect linearity).** $r_{xy} = 1$ if and only if there exist constants $\alpha$ and $\beta > 0$ such that $y_i = \alpha + \beta x_i$ for every $i$. Similarly $r_{xy} = -1$ if and only if the same holds with $\beta < 0$.

The condition for equality in Cauchy–Schwarz is that the two deviation vectors are proportional. Proportionality of the deviations is exactly the statement that the points lie on a straight line.

### 2.3 Symmetry

> **Lemma (Symmetry).** $r_{xy} = r_{yx}$.

Interchanging $x$ and $y$ exchanges the roles of $S_{xx}$ and $S_{yy}$ and leaves $S_{xy}$ unchanged, so the value of the coefficient is unaffected. The symmetry is what makes correlation a description of the pair rather than of a direction.

### 2.4 Invariance under affine transformation

> **Theorem (Origin and scale).** Let $u_i = \alpha + \beta x_i$ and $v_i = \gamma + \delta y_i$ with $\beta \ne 0$ and $\delta \ne 0$. Then

$$
r_{uv} = \text{sign}\left(\beta\delta\right) r_{xy} .
$$

In particular the coefficient is numerically independent of origin and scale: it is unchanged when constants are added, and unchanged when every value is multiplied by a positive constant. Multiplication by a negative constant reverses the sign. This theorem is the justification for every coding shortcut used in computation.

### 2.5 Bilinearity of covariance

> **Theorem (Bilinearity).** For constants $\alpha, \beta, \gamma, \delta$ and variates $x, y, z$,

$$
\text{Cov}(\alpha + \beta x, \gamma + \delta y) = \beta\delta\,\text{Cov}(x,y)
$$

> and $\text{Cov}(x, y + z) = \text{Cov}(x,y) + \text{Cov}(x,z)$.

The two properties, together with symmetry and $\text{Cov}(x,x) = \text{Var}(x)$, make the covariance a symmetric bilinear form on the space of variates. Almost every identity in this topic can be derived by manipulating it with those four rules alone, and the identity $\text{Var}(x + y) = \text{Var}(x) + \text{Var}(y) + 2\text{Cov}(x,y)$ is the most frequently used instance.

### 2.6 Slope, correlation and spread

> **Theorem (Regression slopes).** The least squares slopes satisfy

$$
b_{yx} = r_{xy}\frac{s_y}{s_x}, \qquad b_{xy} = r_{xy}\frac{s_x}{s_y} .
$$

Three consequences follow at once. The sign of each slope equals the sign of $r$. The slope carries units while $r$ does not. And the size of the slope says nothing on its own about the strength of the association, because it is inflated whenever the response is more variable than the predictor.

### 2.7 Product of the regression coefficients

> **Theorem (Product identity).** $b_{yx}\,b_{xy} = r_{xy}^{2}$.

Multiplying the two expressions in the previous theorem cancels the ratio of standard deviations. The identity is exact, not approximate, and serves as a routine check: the geometric mean of the two slopes has magnitude $\lvert r\rvert$, and the product of the slopes can never exceed one.

### 2.8 Concurrence at the point of averages

> **Lemma (Common point).** Both fitted lines pass through $(\bar{x}, \bar{y})$.

Because $a = \bar{y} - b_{yx}\bar{x}$ and $c = \bar{x} - b_{xy}\bar{y}$, substituting the mean of the predictor into either line returns the mean of the response. Geometrically, the two lines intersect exactly at the centroid of the cloud.

### 2.9 Orthogonality of residuals

> **Lemma (Normal-equation consequences).** For the least squares line of $Y$ on $X$,

$$
\sum e_i = 0, \qquad \sum x_i e_i = 0
$$

> where $e_i = y_i - a - bx_i$ are the residuals.

These two identities are precisely the two normal equations rewritten. The first says the residuals sum to zero, so the fitted line passes through the centroid. The second says the residuals are uncorrelated with the predictor, which is the algebraic reason the decomposition of the next theorem holds exactly with no cross term.

### 2.10 The determination identity

> **Theorem (Decomposition of variation).** For the least squares line of $Y$ on $X$,

$$
\sum\left(y_i - \bar{y}\right)^{2} = \sum\left(\hat{y}_i - \bar{y}\right)^{2} + \sum\left(y_i - \hat{y}_i\right)^{2}
$$

> and therefore

$$
r_{xy}^{2} = 1 - \frac{SSE}{S_{yy}} .
$$

Since $SSE \ge 0$ and $SSR \ge 0$, the theorem also re-establishes $0 \le r^{2} \le 1$.

### 2.11 The standard error and the spread of the response

> **Theorem (Relation between s_e and s_y).** With $s_y^{2} = S_{yy}/n$,

$$
s_e^{2} = \frac{n}{n-2}s_y^{2}\left(1 - r_{xy}^{2}\right) .
$$

The factor $\frac{n}{n-2}$ exceeds one and compensates for the two estimated parameters. When $r^{2} = 0$ the fitted line explains nothing and $s_e^{2} = \frac{n}{n-2}s_y^{2}$, slightly larger than the variance of the response itself; when $r^{2} = 1$ the standard error vanishes. For moderate or large $n$ the correction factor is close to one and $s_e$ is approximately $s_y\sqrt{1-r^{2}}$.

### 2.12 Zero correlation and independence

> **Theorem (Independence implies zero correlation).** If $x$ and $y$ are independent then $\text{Cov}(x,y) = 0$ and hence $r_{xy} = 0$. The converse is false.

Independence makes the expected product of deviations factorise, so the covariance vanishes. For the converse, the deterministic relation $y = x^{2}$ with $x$ symmetrically distributed about zero has zero covariance and zero correlation while being perfectly dependent. A coefficient of zero therefore certifies only the absence of a linear component.

### 2.13 Spearman's coefficient as a product-moment coefficient

> **Theorem (Rank coefficient is a correlation).** If $x$ and $y$ are untied ranks, then $r_s$ equals the product-moment correlation coefficient computed on the ranks.

Because the ranks take exactly the values $1, \dots, n$ in both series, the two variances are equal and known, and the covariance can be expressed in terms of $\sum d^{2}$. The derivation in Section 3 makes this explicit, and the consequence is that every theorem about $r$ transfers automatically to $r_s$.

## 3. Formal Proofs, Derivations, and Methods

### 3.1 Derivation of the computational formula

Begin with the definition written in full.

$$
r_{xy} = \frac{\sum\left(x_i - \bar{x}\right)\left(y_i - \bar{y}\right)}{\sqrt{\left[\sum\left(x_i - \bar{x}\right)^{2}\right]\left[\sum\left(y_i - \bar{y}\right)^{2}\right]}}
$$

Expand the numerator.

$$
\sum\left(x_i - \bar{x}\right)\left(y_i - \bar{y}\right) = \sum x_i y_i - \bar{y}\sum x_i - \bar{x}\sum y_i + n\bar{x}\bar{y}
$$

Substituting $\sum x_i = n\bar{x}$ and $\sum y_i = n\bar{y}$ collapses the last three terms into $n\bar{x}\bar{y}$, so the numerator is $\sum x_i y_i - n\bar{x}\bar{y}$. Expanding the first bracket of the denominator in the same way,

$$
\sum\left(x_i - \bar{x}\right)^{2} = \sum x_i^{2} - n\bar{x}^{2}
$$

and the second bracket is $\sum y_i^{2} - n\bar{y}^{2}$. Substituting $n\bar{x}\bar{y} = \frac{1}{n}\sum x_i\sum y_i$ and $n\bar{x}^{2} = \frac{1}{n}\left(\sum x_i\right)^{2}$ gives

$$
r_{xy} = \frac{\sum x_i y_i - \frac{1}{n}\sum x_i \sum y_i}{\sqrt{\left[\sum x_i^{2} - \frac{1}{n}\left(\sum x_i\right)^{2}\right]\left[\sum y_i^{2} - \frac{1}{n}\left(\sum y_i\right)^{2}\right]}} .
$$

Multiplying numerator and denominator by $n$ produces the raw-score version quoted in Section 1, and the identity $S_{xy}/\sqrt{S_{xx}S_{yy}}$ follows by definition of the corrected sums.

### 3.2 Proof of the bound by Cauchy–Schwarz

Let $a_i = x_i - \bar{x}$ and $b_i = y_i - \bar{y}$. The Cauchy–Schwarz inequality for real vectors states

$$
\left(\sum a_i b_i\right)^{2} \le \left(\sum a_i^{2}\right)\left(\sum b_i^{2}\right) .
$$

The right-hand side is positive whenever the two lists are not constant, so taking positive square roots gives

$$
\left\lvert \sum a_i b_i \right\rvert \le \sqrt{\left(\sum a_i^{2}\right)\left(\sum b_i^{2}\right)} .
$$

Dividing both sides by the right-hand quantity yields $\lvert r_{xy}\rvert \le 1$. Equality holds exactly when the vector $b$ is a scalar multiple of $a$, that is, when all the points lie on one straight line.

### 3.3 Proof of invariance

Write $u_i = \alpha + \beta x_i$. Then $\bar{u} = \alpha + \beta\bar{x}$ and therefore $u_i - \bar{u} = \beta\left(x_i - \bar{x}\right)$. Applying the same reasoning to $v$,

$$
S_{uu} = \beta^{2} S_{xx}, \qquad S_{vv} = \delta^{2} S_{yy}, \qquad S_{uv} = \beta\delta\, S_{xy} .
$$

Substituting into $r_{uv} = S_{uv}/\sqrt{S_{uu}S_{vv}}$,

$$
r_{uv} = \frac{\beta\delta\,S_{xy}}{\lvert \beta\delta \rvert\sqrt{S_{xx}S_{yy}}} = \text{sign}\left(\beta\delta\right) r_{xy} .
$$

The absolute value in the denominator appears because a square root is non-negative. The theorem follows, and the special case $\beta = \delta = 1$ gives the shift of origin.

### 3.4 Derivation of the normal equations

The criterion is

$$
Q(a,b) = \sum_{i=1}^{n}\left(y_i - a - bx_i\right)^{2} .
$$

Expand the square and sum term by term.

$$
Q(a,b) = \sum y_i^{2} - 2a\sum y_i - 2b\sum x_i y_i + na^{2} + 2ab\sum x_i + b^{2}\sum x_i^{2}
$$

Differentiating with respect to each unknown and setting the derivatives to zero,

$$
\frac{\partial Q}{\partial a} = -2\sum y_i + 2na + 2b\sum x_i = 0
$$

$$
\frac{\partial Q}{\partial b} = -2\sum x_i y_i + 2a\sum x_i + 2b\sum x_i^{2} = 0 .
$$

Dividing each by two and rearranging produces the normal equations

$$
\sum y = na + b\sum x, \qquad \sum xy = a\sum x + b\sum x^{2} .
$$

For the line of $X$ on $Y$ the same argument with the roles exchanged gives $\sum x = nc + d\sum y$ and $\sum xy = c\sum y + d\sum y^{2}$.

### 3.5 Uniqueness of the solution

The Hessian matrix of second derivatives is

$$
H = \begin{pmatrix} 2n & 2\sum x_i \\ 2\sum x_i & 2\sum x_i^{2} \end{pmatrix}
$$

with determinant $4\left(n\sum x_i^{2} - \left(\sum x_i\right)^{2}\right) = 4nS_{xx}$. When the $x$ values are not all equal, $S_{xx} > 0$, the determinant is positive and the leading entry $2n$ is positive, so $H$ is positive definite and $Q$ is strictly convex. The stationary point is therefore the unique global minimum.

### 3.6 Solving the normal equations

Divide the first normal equation by $n$ to obtain $\bar{y} = a + b\bar{x}$, hence

$$
a = \bar{y} - b\bar{x} .
$$

Substituting into the second normal equation,

$$
\sum x_i y_i = \left(\bar{y} - b\bar{x}\right)\sum x_i + b\sum x_i^{2} .
$$

Replacing $\sum x_i$ by $n\bar{x}$ and collecting terms in $b$,

$$
\sum x_i y_i - n\bar{x}\bar{y} = b\left(\sum x_i^{2} - n\bar{x}^{2}\right) .
$$

The left side is $S_{xy}$ and the bracket is $S_{xx}$, so

$$
b = \frac{S_{xy}}{S_{xx}}, \qquad a = \bar{y} - \frac{S_{xy}}{S_{xx}}\bar{x} .
$$

Exchanging the roles of the two quantities gives

$$
d = \frac{S_{xy}}{S_{yy}}, \qquad c = \bar{x} - \frac{S_{xy}}{S_{yy}}\bar{y} .
$$

### 3.7 Derivation of the slope formulas and the product identity

Starting from $b_{yx} = S_{xy}/S_{xx}$ and inserting the definition of $r$,

$$
b_{yx} = \frac{S_{xy}}{\sqrt{S_{xx}S_{yy}}} \cdot \frac{\sqrt{S_{yy}}}{\sqrt{S_{xx}}} = r_{xy}\frac{s_y}{s_x} .
$$

Repeating with the roles exchanged gives $b_{xy} = r_{xy}s_x/s_y$. Multiplying,

$$
b_{yx}b_{xy} = r_{xy}^{2}\frac{s_y}{s_x}\frac{s_x}{s_y} = r_{xy}^{2} .
$$

### 3.8 Proof of the decomposition of variation

Write $y_i - \bar{y} = \left(\hat{y}_i - \bar{y}\right) + e_i$ where $e_i = y_i - \hat{y}_i$. Squaring and summing,

$$
\sum\left(y_i - \bar{y}\right)^{2} = \sum\left(\hat{y}_i - \bar{y}\right)^{2} + 2\sum\left(\hat{y}_i - \bar{y}\right)e_i + \sum e_i^{2} .
$$

The cross term vanishes. To see why, note that $\hat{y}_i - \bar{y} = b\left(x_i - \bar{x}\right)$, so

$$
\sum\left(\hat{y}_i - \bar{y}\right)e_i = b\sum\left(x_i - \bar{x}\right)e_i = b\left(\sum x_i e_i - \bar{x}\sum e_i\right) = 0
$$

by the two orthogonality identities of Section 2.9. Hence $S_{yy} = SSR + SSE$, and dividing by $S_{yy}$ gives

$$
1 = \frac{SSR}{S_{yy}} + \frac{SSE}{S_{yy}} .
$$

Since $SSR = b^{2}S_{xx} = \frac{S_{xy}^{2}}{S_{xx}}$, the first ratio equals $\frac{S_{xy}^{2}}{S_{xx}S_{yy}} = r_{xy}^{2}$.

### 3.9 Derivation of the standard error relation

From $SSE = S_{yy}\left(1 - r^{2}\right)$ and $s_y^{2} = S_{yy}/n$,

$$
s_e^{2} = \frac{SSE}{n-2} = \frac{S_{yy}\left(1-r^{2}\right)}{n-2} = \frac{n}{n-2}\,s_y^{2}\left(1-r^{2}\right) .
$$

The relation shows that the residual scatter is a fraction $\sqrt{1-r^{2}}$ of the total scatter of the response, inflated slightly by the degrees-of-freedom correction.

### 3.10 Derivation of Spearman's formula

For untied ranks both series take the values $1, 2, \dots, n$, so

$$
\sum x = \sum y = 1 + 2 + \cdots + n = \frac{n\left(n+1\right)}{2}
$$

and

$$
\sum x^{2} = \sum y^{2} = 1^{2} + 2^{2} + \cdots + n^{2} = \frac{n\left(n+1\right)\left(2n+1\right)}{6} .
$$

The variance of either set of ranks is therefore

$$
\text{Var}(x) = \text{Var}(y) = \frac{1}{n}\sum x^{2} - \left(\frac{\sum x}{n}\right)^{2} = \frac{\left(n+1\right)\left(2n+1\right)}{6} - \frac{\left(n+1\right)^{2}}{4} = \frac{n^{2}-1}{12} .
$$

Now let $d = x - y$. Because the mean rank is the same in both series, the mean of $d$ is zero, so

$$
\sum d^{2} = \sum\left(\left(x - \bar{x}\right) - \left(y - \bar{y}\right)\right)^{2} = \sum\left(x-\bar{x}\right)^{2} + \sum\left(y-\bar{y}\right)^{2} - 2\sum\left(x-\bar{x}\right)\left(y-\bar{y}\right) .
$$

Dividing by $n$,

$$
\frac{1}{n}\sum d^{2} = \text{Var}(x) + \text{Var}(y) - 2\,\text{Cov}(x,y) .
$$

Substituting the rank variance twice and solving for the covariance,

$$
\text{Cov}(x,y) = \frac{n^{2}-1}{12} - \frac{1}{2n}\sum d^{2} .
$$

Finally,

$$
r_s = \frac{\text{Cov}(x,y)}{\sqrt{\text{Var}(x)\text{Var}(y)}} = \frac{\frac{n^{2}-1}{12} - \frac{1}{2n}\sum d^{2}}{\frac{n^{2}-1}{12}} = 1 - \frac{6\sum d^{2}}{n\left(n^{2}-1\right)} .
$$

### 3.11 Why ties require a correction

When $m$ individuals share a value, each receives the average of the ranks they would otherwise have occupied. Averaging compresses the spread of the ranks: the sum of squared deviations of the ranks is reduced by exactly $\frac{m\left(m^{2}-1\right)}{12}$ for that group. Consequently $\text{Var}(x)$ is smaller than $\frac{n^{2}-1}{12}$, the relation between $\sum d^{2}$ and the covariance no longer holds as derived, and the computed $r_s$ is too small in magnitude.

The remedy is to add $\frac{m\left(m^{2}-1\right)}{12}$ back into the bracket for every tied group, restoring the correct total. With the correction applied,

$$
r_s = 1 - \frac{6\left[\sum d^{2} + \sum \frac{m\left(m^{2}-1\right)}{12}\right]}{n\left(n^{2}-1\right)} .
$$

The correction is applied separately to each series and then combined, because ties in the first series and ties in the second both compress the corresponding variance.

### 3.12 Method: the full computation sequence for a bivariate data set

Step 1. Plot the pairs mentally and note the direction, the narrowness of the band, and any unusual points.

Step 2. Build a table with columns for $x$, $y$, $xy$, $x^{2}$ and $y^{2}$ and a totals row.

Step 3. Compute $S_{xy}$, $S_{xx}$ and $S_{yy}$ from the totals.

Step 4. Compute $r = S_{xy}/\sqrt{S_{xx}S_{yy}}$ and report $r^{2}$.

Step 5. Compute $b_{yx} = S_{xy}/S_{xx}$ and $a = \bar{y} - b_{yx}\bar{x}$.

Step 6. Compute $b_{xy} = S_{xy}/S_{yy}$ and $c = \bar{x} - b_{xy}\bar{y}$.

Step 7. Verify that $b_{yx}b_{xy} = r^{2}$ and that both lines pass through $(\bar{x},\bar{y})$.

Step 8. Compute $SSE = S_{yy}\left(1-r^{2}\right)$ and $s_e = \sqrt{SSE/(n-2)}$.

Step 9. Answer any prediction question with the line whose subject matches the quantity to be predicted, and state whether the input lies inside the observed range.

## 4. Representative Worked Examples and Solutions

### 4.1 Problem: marks in calculus and statistics

The marks of eight students in calculus and in statistics are recorded.

| Calculus ($X$) | 55 | 44 | 33 | 47 | 42 | 65 | 51 | 63 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Statistics ($Y$) | 43 | 52 | 35 | 38 | 51 | 43 | 48 | 50 |

Fit the two least squares lines, compute the correlation coefficient and the coefficient of determination, and compute the standard error of estimate.

### 4.2 Solution: both lines, the coefficient, determination and residual scatter

Step 1. Accumulate the five sums.

| $X$ | $Y$ | $XY$ | $X^{2}$ | $Y^{2}$ |
| --- | --- | --- | --- | --- |
| 55 | 43 | 2,365 | 3,025 | 1,849 |
| 44 | 52 | 2,288 | 1,936 | 2,704 |
| 33 | 35 | 1,155 | 1,089 | 1,225 |
| 47 | 38 | 1,786 | 2,209 | 1,444 |
| 42 | 51 | 2,142 | 1,764 | 2,601 |
| 65 | 43 | 2,795 | 4,225 | 1,849 |
| 51 | 48 | 2,448 | 2,601 | 2,304 |
| 63 | 50 | 3,150 | 3,969 | 2,500 |
| $\sum 400$ | $\sum 360$ | $\sum 18{,}129$ | $\sum 20{,}818$ | $\sum 16{,}476$ |

Step 2. Compute the corrected sums with $n = 8$.

$$
S_{xy} = 18{,}129 - \frac{1}{8}\left(400\right)\left(360\right) = 18{,}129 - 18{,}000 = 129
$$

$$
S_{xx} = 20{,}818 - \frac{1}{8}\left(400\right)^{2} = 20{,}818 - 20{,}000 = 818
$$

$$
S_{yy} = 16{,}476 - \frac{1}{8}\left(360\right)^{2} = 16{,}476 - 16{,}200 = 276
$$

Step 3. Compute the correlation coefficient.

$$
r_{xy} = \frac{129}{\sqrt{\left(818\right)\left(276\right)}} = \frac{129}{\sqrt{225{,}768}} = \frac{129}{475.15} \approx 0.2715
$$

Step 4. Report the coefficient of determination.

$$
r^{2} = 0.2715^{2} \approx 0.0737
$$

Step 5. Fit the line of $Y$ on $X$ from the normal equations.

$$
360 = 8a + 400b, \qquad 18{,}129 = 400a + 20{,}818b
$$

Step 6. Multiply the first equation by $50$ and subtract it from the second.

$$
18{,}129 - 18{,}000 = \left(20{,}818 - 20{,}000\right)b
$$

$$
129 = 818b \quad\Rightarrow\quad b = 0.15770
$$

Step 7. Recover the intercept.

$$
a = \frac{360 - 400\left(0.15770\right)}{8} = \frac{360 - 63.08}{8} = 37.115
$$

$$
Y = 37.115 + 0.1577X
$$

Step 8. Fit the line of $X$ on $Y$.

$$
400 = 8c + 360d, \qquad 18{,}129 = 360c + 16{,}476d
$$

Step 9. Multiply the first equation by $45$ and subtract it from the second.

$$
18{,}129 - 18{,}000 = \left(16{,}476 - 16{,}200\right)d
$$

$$
129 = 276d \quad\Rightarrow\quad d = 0.46739
$$

Step 10. Recover the second intercept.

$$
c = \frac{400 - 360\left(0.46739\right)}{8} = \frac{400 - 168.26}{8} = 28.967
$$

$$
X = 28.967 + 0.4674Y
$$

Step 11. Verify the product identity.

$$
b_{yx}\,b_{xy} = \left(0.15770\right)\left(0.46739\right) = 0.07371 = r^{2}
$$

Step 12. Compute the residual scatter.

$$
SSE = S_{yy}\left(1 - r^{2}\right) = 276\left(0.92629\right) = 255.66
$$

$$
s_e = \sqrt{\frac{255.66}{8-2}} = \sqrt{42.61} \approx 6.53
$$

Step 13. Interpret. The association is positive but weak: only about seven per cent of the variation in statistics marks goes with the variation in calculus marks. The standard error of $6.53$ is larger than the standard deviation of the statistics marks, which is $\sqrt{276/8} = 5.87$; that happens for small samples because the divisor $n-2 = 6$ inflates the residual variance by a factor of $8/6$. The fitted line is therefore a poor predictor for these eight students, and a claim that calculus marks determine statistics marks would be badly overstated.

### 4.3 Problem: ages and systolic blood pressure, computed by coding

The ages in years and systolic blood pressures of twelve students are recorded. Compute the correlation coefficient by the short method, fit the line of blood pressure on age, and predict the pressure of a student aged $50$.

| $x$ | 56 | 42 | 72 | 36 | 63 | 47 | 55 | 49 | 38 | 42 | 68 | 60 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| $y$ | 147 | 125 | 160 | 118 | 149 | 128 | 150 | 145 | 115 | 140 | 152 | 155 |

### 4.4 Solution: code, tabulate, then restore the units

Step 1. Choose the codes $u = x - 52$ and $v = y - 140$. These are shifts of origin only, so by the invariance theorem the coefficient computed on $u$ and $v$ equals the coefficient on $x$ and $y$.

Step 2. Build the coded table.

| $x$ | $y$ | $u$ | $v$ | $u^{2}$ | $v^{2}$ | $uv$ |
| --- | --- | --- | --- | --- | --- | --- |
| 56 | 147 | 4 | 7 | 16 | 49 | 28 |
| 42 | 125 | -10 | -15 | 100 | 225 | 150 |
| 72 | 160 | 20 | 20 | 400 | 400 | 400 |
| 36 | 118 | -16 | -22 | 256 | 484 | 352 |
| 63 | 149 | 11 | 9 | 121 | 81 | 99 |
| 47 | 128 | -5 | -12 | 25 | 144 | 60 |
| 55 | 150 | 3 | 10 | 9 | 100 | 30 |
| 49 | 145 | -3 | 5 | 9 | 25 | -15 |
| 38 | 115 | -14 | -25 | 196 | 625 | 350 |
| 42 | 140 | -10 | 0 | 100 | 0 | 0 |
| 68 | 152 | 16 | 12 | 256 | 144 | 192 |
| 60 | 155 | 8 | 15 | 64 | 225 | 120 |
| | | $\sum 4$ | $\sum 4$ | $\sum 1{,}552$ | $\sum 2{,}502$ | $\sum 1{,}766$ |

Step 3. Compute the corrected sums of the coded values.

$$
S_{uv} = 1{,}766 - \frac{1}{12}\left(4\right)\left(4\right) = 1{,}766 - 1.333 = 1{,}764.667
$$

$$
S_{uu} = 1{,}552 - \frac{1}{12}\left(4\right)^{2} = 1{,}552 - 1.333 = 1{,}550.667
$$

$$
S_{vv} = 2{,}502 - \frac{1}{12}\left(4\right)^{2} = 2{,}502 - 1.333 = 2{,}500.667
$$

Step 4. Compute the coefficient on the coded values.

$$
r_{uv} = \frac{1{,}764.667}{\sqrt{\left(1{,}550.667\right)\left(2{,}500.667\right)}} = \frac{1{,}764.667}{1{,}969.19} \approx 0.8961
$$

Step 5. Apply the invariance theorem.

$$
r_{xy} = r_{uv} = 0.8961, \qquad r^{2} = 0.8031
$$

Step 6. Fit the line of blood pressure on age. Because only the origin was shifted, the slope is unchanged and the original intercept is recovered from the original means.

$$
b_{yx} = \frac{S_{uv}}{S_{uu}} = \frac{1{,}764.667}{1{,}550.667} = 1.1380
$$

$$
\bar{x} = \frac{628}{12} = 52.333, \qquad \bar{y} = \frac{1{,}684}{12} = 140.333
$$

$$
a = 140.333 - \left(1.1380\right)\left(52.333\right) = 140.333 - 59.556 = 80.778
$$

$$
Y = 80.778 + 1.1380X
$$

Step 7. Predict the pressure of a student aged $50$.

$$
Y = 80.778 + 1.1380\left(50\right) = 80.778 + 56.900 = 137.68
$$

Step 8. Check that the prediction at the mean age returns the mean pressure.

$$
80.778 + 1.1380\left(52.333\right) = 80.778 + 59.556 = 140.33
$$

Step 9. Interpret. Ages and systolic pressures are strongly and positively associated, with about eighty per cent of the variation in pressure accounted for by the straight-line relation with age. The slope of $1.138$ says that one further year of age goes with about $1.14$ units of pressure on the fitted line, and the prediction of $137.7$ for a student aged $50$ lies inside the observed age range from $36$ to $72$.

### 4.5 Problem: ten items where ranks are tied

Two characteristics are graded on ten items. Obtain Spearman's rank correlation coefficient and interpret it.

| Item | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| $X$ | 68 | 64 | 75 | 50 | 64 | 80 | 75 | 40 | 55 | 64 |
| $Y$ | 62 | 58 | 68 | 45 | 81 | 60 | 68 | 48 | 50 | 70 |

### 4.6 Solution: averaged ranks and the tie correction

Step 1. Rank the $X$ series from smallest to largest. The value $40$ takes rank $1$, $50$ takes rank $2$, $55$ takes rank $3$. The value $64$ occurs three times and would occupy ranks $4$, $5$ and $6$, so each occurrence takes the average $5$. The value $68$ takes rank $7$. The value $75$ occurs twice and would occupy ranks $8$ and $9$, so each occurrence takes $8.5$. The value $80$ takes rank $10$.

Step 2. Rank the $Y$ series in the same direction. The value $45$ takes rank $1$, $48$ takes rank $2$, $50$ takes rank $3$, $58$ takes rank $4$, $60$ takes rank $5$, $62$ takes rank $6$. The value $68$ occurs twice and would occupy ranks $7$ and $8$, so each occurrence takes $7.5$. The value $70$ takes rank $9$ and $81$ takes rank $10$.

Step 3. Set out the ranks, the differences and their squares.

| Item | $X$ | $Y$ | Rank of $X$ | Rank of $Y$ | $d$ | $d^{2}$ |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | 68 | 62 | 7 | 6 | 1 | 1 |
| 2 | 64 | 58 | 5 | 4 | 1 | 1 |
| 3 | 75 | 68 | 8.5 | 7.5 | 1 | 1 |
| 4 | 50 | 45 | 2 | 1 | 1 | 1 |
| 5 | 64 | 81 | 5 | 10 | -5 | 25 |
| 6 | 80 | 60 | 10 | 5 | 5 | 25 |
| 7 | 75 | 68 | 8.5 | 7.5 | 1 | 1 |
| 8 | 40 | 48 | 1 | 2 | -1 | 1 |
| 9 | 55 | 50 | 3 | 3 | 0 | 0 |
| 10 | 64 | 70 | 5 | 9 | -4 | 16 |
| Total | | | | | | $\sum 72$ |

Step 4. Compute the tie corrections. In the $X$ series the value $75$ occurs twice and the value $64$ occurs three times.

$$
\frac{2\left(2^{2}-1\right)}{12} = \frac{6}{12} = 0.5, \qquad \frac{3\left(3^{2}-1\right)}{12} = \frac{24}{12} = 2
$$

so the $X$ series contributes $2.5$. In the $Y$ series the value $68$ occurs twice, contributing $0.5$. The combined correction is therefore $3$.

Step 5. Compute the denominator.

$$
n\left(n^{2}-1\right) = 10\left(100-1\right) = 990
$$

Step 6. Substitute into the corrected formula.

$$
r_s = 1 - \frac{6\left(72 + 3\right)}{990} = 1 - \frac{450}{990} = 1 - 0.4545 = 0.5455
$$

Step 7. Interpret. A rank coefficient of $0.545$ indicates a moderate positive agreement between the two orderings. The value is well below one, and the items that drive it down are the fifth and sixth, where the ordering of the two characteristics is almost reversed. Omitting the tie correction would give $1 - 432/990 = 0.564$, which overstates the agreement; the correction is small here but it is not optional.

### 4.7 Problem: reconstructing both lines from summary values

A data set gives $n = 10$ pairs with $\bar{x} = 10$, $\bar{y} = 20$, $s_x = 5$, $s_y = 8$ and $r_{xy} = 0.9$. Find both regression lines, predict $Y$ when $X = 12$, and predict $X$ when $Y = 24$.

### 4.8 Solution: slopes from the theorem, intercepts from the centroid

Step 1. Compute the slope of $Y$ on $X$ from $b_{yx} = r s_y/s_x$.

$$
b_{yx} = 0.9\left(\frac{8}{5}\right) = 0.9\left(1.6\right) = 1.44
$$

Step 2. Compute the intercept from $a = \bar{y} - b_{yx}\bar{x}$.

$$
a = 20 - 1.44\left(10\right) = 20 - 14.4 = 5.6
$$

$$
Y = 5.6 + 1.44X
$$

Step 3. Compute the slope of $X$ on $Y$.

$$
b_{xy} = 0.9\left(\frac{5}{8}\right) = 0.9\left(0.625\right) = 0.5625
$$

Step 4. Compute the second intercept.

$$
c = 10 - 0.5625\left(20\right) = 10 - 11.25 = -1.25
$$

$$
X = -1.25 + 0.5625Y
$$

Step 5. Verify the product identity.

$$
\left(1.44\right)\left(0.5625\right) = 0.81 = 0.9^{2}
$$

Step 6. Predict $Y$ at $X = 12$.

$$
Y = 5.6 + 1.44\left(12\right) = 5.6 + 17.28 = 22.88
$$

Step 7. Predict $X$ at $Y = 24$.

$$
X = -1.25 + 0.5625\left(24\right) = -1.25 + 13.5 = 12.25
$$

Step 8. Interpret. Both lines rise, as they must when $r$ is positive. Their slopes, $1.44$ and $0.5625$, are reciprocal only when the association is perfect; here their product is $0.81$. The two predictions are not inverses of one another: predicting $Y$ from $X = 12$ gives $22.88$, but feeding $22.88$ back into the second line gives $X = 11.62$ rather than $12$. That asymmetry is intrinsic to least squares and is not an arithmetic error.

## 5. Mathematical Extensions, Limits, and Common Errors

### 5.1 The divisor question

Three divisors appear in this topic and they answer three different questions. Dividing a corrected sum of squares by $n$ describes the spread of the observations actually in hand. Dividing by $n-1$ gives an unbiased estimator of a population variance when the data are regarded as a sample. Dividing a residual sum of squares by $n-2$ gives an unbiased estimator of the residual variance, because two parameters have been estimated from the same data.

For the correlation coefficient itself the divisor is irrelevant, since the same factor appears in numerator and denominator and cancels. That is one reason $r$ is such a convenient summary: it is the same number whichever convention the surrounding textbook uses for variance. The standard error of estimate is not so fortunate, and a note that reports $s_e$ without stating the divisor is ambiguous by a factor of $\sqrt{n/(n-2)}$, which is about five per cent for $n = 20$ but nearly twenty-two per cent for $n = 6$.

### 5.2 Association, causation and the lurking variable

A correlation of any size, however close to one, is evidence of association only. Three alternative explanations must always be weighed before a causal claim is entertained.

**Common cause.** An unmeasured quantity may drive both variables. The association between ice-cream sales and drowning deaths is real, strong and entirely explained by temperature. The correlation is not wrong; the causal reading of it is.

**Reverse causation.** The direction of influence may be the opposite of the one assumed. A correlation between class attendance and marks is equally consistent with attendance raising marks and with motivated students both attending and scoring well.

**Coincidence.** Two series that both trend over time will correlate strongly whatever their subject matter. With enough pairs of quantities available, a spurious correlation near one can always be found.

Only randomised manipulation of the input, holding other influences fixed, supports a causal conclusion. Regression is a description of how a response co-varies with a predictor in the observed data; it is not a mechanism.

### 5.3 Extrapolation and restriction of range

The fitted line is defined for all values of the predictor, but it is only supported by data over the observed range. Outside that range the straight track may bend, and the response may be bounded when the line is not. A line fitted to ages from $36$ to $72$ will happily return a pressure of $94$ for an age of $12$ and a pressure of $194$ for an age of $100$, and neither number should be reported without a clear statement that it is an extrapolation.

The opposite problem is restriction of range. If the data cover only a narrow band of the predictor, the cloud is a short segment of a track and its direction is hard to determine; the coefficient is depressed towards zero even when the underlying relation is tight. Two studies of the same physical relationship can therefore report very different coefficients simply because one sampled a wide range of the predictor and the other a narrow one.

### 5.4 Product-moment and rank coefficients compared

| Feature | Pearson's $r$ | Spearman's $r_s$ |
| --- | --- | --- |
| Input | Raw values | Ranks |
| Measures | Straight-line association | Monotone association |
| Sensitive to outliers | Strongly | Weakly |
| Sensitive to scale of measurement | Needs interval data | Needs only ordinal data |
| Effect of a monotone transformation | Changes the value | Unchanged |
| Ties | No special treatment | Correction required |
| Bounds | $-1$ to $1$ | $-1$ to $1$ |

The comparison explains when each should be preferred. When the values are trustworthy and the relationship is expected to be linear, Pearson's coefficient uses more information and is more efficient. When the values are ordinal, or contain extreme observations, or the relationship is monotone but curved, the rank coefficient is the safer summary. A large gap between the two computed on the same data is itself informative: it usually signals either an outlier or a curved relationship.

### 5.5 Robustness and influential observations

The correlation coefficient has a breakdown point of zero. A single observation placed far from the rest can move $r$ from nearly zero to nearly one, because the product $\left(x_i-\bar{x}\right)\left(y_i-\bar{y}\right)$ for that observation grows without bound while all the others stay fixed. Regression slopes are equally vulnerable.

The practical remedy is not a different formula but a habit: plot the data, and recompute after removing any point that sits far from the band. If the coefficient changes sharply, the original value describes one unusual observation rather than the bulk of the data, and that fact belongs in the report.

### 5.6 Errors that recur in examinations

- **Using the wrong line for a prediction.** Predicting $Y$ requires $Y = a + b_{yx}X$; predicting $X$ requires $X = c + b_{xy}Y$. Rearranging one line to do the other's job gives a systematically wrong answer.
- **Swapping the two slopes.** The slope of $Y$ on $X$ is $S_{xy}/S_{xx}$, with the predictor's corrected sum of squares in the denominator. Using $S_{yy}$ instead produces the other line.
- **Reporting $r^{2}$ as $r$.** A coefficient of determination of $0.81$ corresponds to a correlation of $0.9$, not $0.81$.
- **Taking a square root and losing the sign.** Recovering $r$ from $r^{2}$ requires the sign of $S_{xy}$ or of the regression slopes.
- **Forgetting the factor $\frac{1}{n}$ in the corrected sums.** The quantity subtracted is $\frac{1}{n}\sum x \sum y$, not $\sum x \sum y$.
- **Summing rather than averaging the deviations.** A sum of deviations is always zero; it is the sum of squared deviations that carries the information.
- **Ranking one series in the opposite direction.** The sign of $r_s$ then reverses.
- **Giving tied values consecutive ranks.** Tied values must share the average of the ranks they would have occupied.
- **Omitting the tie correction.** The uncorrected formula overstates the magnitude of $r_s$.
- **Squaring the rank differences after rounding them.** Tied ranks produce half-integers, and their squares are exact fractions such as $2.25$; rounding them corrupts the total.
- **Computing $s_e$ with divisor $n$.** The standard error of estimate uses $n-2$ degrees of freedom.
- **Treating a small $r$ as evidence of no relationship.** A curved relationship can give a coefficient near zero.
- **Treating a large $r$ as evidence of cause.** Association is not a mechanism.

### 5.7 Regression to the mean and further directions

One consequence of the two-line structure deserves separate comment. Because each regression line has slope of magnitude at most $s_y/s_x$ and is shrunk by the factor $r$, predicted values always lie closer to their mean than the corresponding observed values do. A student whose first score was far above average is predicted to score closer to average next time. This is not a failure of the method; it is a mathematical consequence of an imperfect correlation, and it explains a great many apparent regressions in real data, from sporting form to medical screening.

Beyond this topic lie several natural extensions. The distribution of $r$ under random sampling allows the construction of confidence intervals and tests of the hypothesis that the population correlation is zero. The same least squares algebra with several predictors gives multiple regression, in which the coefficient of determination is again the proportion of variation explained. The decomposition of total variation into explained and residual parts is the identity on which the analysis of variance rests. Each of these is a continuation of the same two ideas: measure how quantities move together, and use that measurement to predict.
