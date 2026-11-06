## 1. Purpose and Statistical Context

### 1.1 Where least squares fits in estimation

Statistical estimation uses information from a sample to learn about an unknown population characteristic. A population characteristic is called a parameter; a quantity calculated from observed sample data is a statistic. In regression, the parameters describe how a response variable changes with an explanatory variable. The method of least squares estimates those regression parameters by choosing the line whose fitted values are, in total, as close as possible to the observed responses in squared-error terms.

This lesson concerns fitting a straight line. It does not claim that every relationship in data is linear. Rather, it begins with the working model that the mean response changes linearly with the explanatory value. The line's intercept and slope are unknown constants, and the sample is used to estimate them.

### 1.2 Learning goals for this topic

After studying this topic, a learner should be able to:

- Express a straight-line model in scalar notation and in matrix notation.
- Explain what a residual is and why least squares minimizes the sum of squared residuals.
- Derive the two normal equations by differentiating the sum of squared errors.
- Solve for the least-squares slope and intercept from summary sums or from the matrix formula.
- Build the design matrix, parameter vector, and response vector for given observations.
- Interpret the fitted line and check the arithmetic in a worked problem.
- State why, under the source's zero-mean error assumptions, the least-squares coefficient estimators are unbiased.

### 1.3 Why use a line and why square errors?

Suppose measurements $y_1,\ldots,y_n$ are observed at explanatory values $x_1,\ldots,x_n$. If the mean of $Y$ varies linearly with $X$, the model is

$$
y_i=\alpha+\beta x_i+e_i,\qquad i=1,2,\ldots,n.
$$

Here $\alpha+\beta x_i$ is the line's fitted mean at $x_i$, while $e_i$ represents the difference between the observed value and that line. A candidate line can lie above some observations and below others. The signed differences could cancel if simply added, even if the line fits poorly. Squaring each difference makes every contribution nonnegative and gives larger residuals more influence. The method selects $\alpha$ and $\beta$ to minimize

$$
S(\alpha,\beta)=\sum_{i=1}^{n}e_i^2
=\sum_{i=1}^{n}(y_i-\alpha-\beta x_i)^2.
$$

The result is called the least-squares fitted line. It is the line with the smallest sum of squared vertical residuals among straight lines for the given data.

## 2. Definitions and Assumptions

### 2.1 The straight-line regression model

The approved lecture material assumes observations at explanatory values $x_1,\ldots,x_n$ and models the corresponding responses as

$$
y_i=\alpha+\beta x_i+e_i.
$$

The symbols have these meanings:

- $y_i$ is the observed response for observation $i$.
- $x_i$ is the given explanatory value for observation $i$.
- $\alpha$ is the intercept, the fitted mean response at $x=0$.
- $\beta$ is the slope, the change in fitted mean response for a one-unit increase in $x$.
- $e_i$ is the error for observation $i$, the difference between the response and its modelled mean.
- $n$ is the number of paired observations.

The source assumes the errors are independent, have mean zero, and share variance $\sigma^2$:

$$
E(e_i)=0,\qquad \operatorname{Var}(e_i)=\sigma^2.
$$

The fitted value and residual should not be confused. For estimated coefficients, the fitted value is $\hat y_i=\hat\alpha+\hat\beta x_i$, and the residual is $r_i=y_i-\hat y_i$. The original model error $e_i$ is not directly observed because the true parameters are unknown; the residual is calculated after fitting the line.

### 2.2 The least-squares criterion

For any proposed pair $(\alpha,\beta)$, the residual at point $i$ is $y_i-\alpha-\beta x_i$. The total squared error is therefore

$$
S(\alpha,\beta)=\sum_{i=1}^{n}(y_i-\alpha-\beta x_i)^2.
$$

Least squares chooses the coefficients that give the smallest possible value of $S$. The observations $x_i$ are treated as the given design values in this calculation. A unique straight-line fit requires the explanatory values not all to be identical; otherwise the intercept and slope cannot be separately determined from the data.

### 2.3 Matrix notation and dimensions

For $n$ observations, stack all responses into one column vector, place a column of ones beside the explanatory values, and stack the two unknown coefficients into another column vector:

$$
\mathbf y=
\begin{pmatrix}
y_1\\
y_2\\
\vdots\\
y_n
\end{pmatrix},\qquad
X=
\begin{pmatrix}
1&x_1\\
1&x_2\\
\vdots&\vdots\\
1&x_n
\end{pmatrix},\qquad
\boldsymbol\theta=
\begin{pmatrix}
\alpha\\
\beta
\end{pmatrix},\qquad
\mathbf e=
\begin{pmatrix}
e_1\\
e_2\\
\vdots\\
e_n
\end{pmatrix}.
$$

The model becomes

$$
\mathbf y=X\boldsymbol\theta+\mathbf e.
$$

The dimensions provide a useful check: $\mathbf y$ is $n\times1$, $X$ is $n\times2$, $\boldsymbol\theta$ is $2\times1$, and $\mathbf e$ is $n\times1$. Thus $X\boldsymbol\theta$ is also $n\times1$, as required to represent all fitted responses. The first column of $X$ contains ones because the model has an intercept; the second contains the observed $x_i$ values because the slope multiplies $x_i$.

For matrices, the prime symbol denotes transpose. The least-squares criterion can be written compactly as

$$
S(\boldsymbol\theta)=\mathbf e^{\mathsf T}\mathbf e
=(\mathbf y-X\boldsymbol\theta)^{\mathsf T}(\mathbf y-X\boldsymbol\theta).
$$

The matrix $X^{\mathsf T}X$ is $2\times2$ and $X^{\mathsf T}\mathbf y$ is $2\times1$. The inverse $(X^{\mathsf T}X)^{-1}$ exists when the two columns of $X$ are linearly independent. In straight-line fitting, that condition holds when the observed $x_i$ values are not all the same.

## 3. Methods and Interpretation

### 3.1 Deriving the normal equations from the scalar criterion

Start with

$$
S(\alpha,\beta)=\sum_{i=1}^{n}(y_i-\alpha-\beta x_i)^2.
$$

At a minimum, the first partial derivatives with respect to the two unknown coefficients equal zero. Differentiating with respect to $\alpha$ gives

$$
\frac{\partial S}{\partial\alpha}
=-2\sum_{i=1}^{n}(y_i-\alpha-\beta x_i)=0.
$$

Divide by $-2$ and collect terms:

$$
\sum_{i=1}^{n}y_i=n\alpha+\beta\sum_{i=1}^{n}x_i.
$$

Differentiating with respect to $\beta$ gives

$$
\frac{\partial S}{\partial\beta}
=-2\sum_{i=1}^{n}x_i(y_i-\alpha-\beta x_i)=0,
$$

so

$$
\sum_{i=1}^{n}x_i y_i
=\alpha\sum_{i=1}^{n}x_i+\beta\sum_{i=1}^{n}x_i^2.
$$

These two equations are the normal equations. They are simultaneous equations for $\alpha$ and $\beta$ and can be solved directly or recognized as the components of the matrix equation.

### 3.2 Slope and intercept formulas

Write the sample means as

$$
\bar x=\frac{1}{n}\sum_{i=1}^{n}x_i,\qquad
\bar y=\frac{1}{n}\sum_{i=1}^{n}y_i.
$$

Solving the normal equations gives the least-squares slope

$$
\hat\beta=
\frac{n\sum_{i=1}^{n}x_i y_i-(\sum_{i=1}^{n}x_i)(\sum_{i=1}^{n}y_i)}
{n\sum_{i=1}^{n}x_i^2-(\sum_{i=1}^{n}x_i)^2}.
$$

An equivalent centered form is

$$
\hat\beta=
\frac{\sum_{i=1}^{n}(x_i-\bar x)(y_i-\bar y)}
{\sum_{i=1}^{n}(x_i-\bar x)^2}.
$$

The intercept is

$$
\hat\alpha=\bar y-\hat\beta\bar x.
$$

The centered slope formula compares how $x_i$ and $y_i$ vary together with how much the $x_i$ values vary. The intercept formula ensures the fitted line passes through $(\bar x,\bar y)$, since $\hat\alpha+\hat\beta\bar x=\bar y$. This is an algebraic property of a line fitted with an intercept.

The denominator of $\hat\beta$ is zero if all $x_i$ values are identical. In that case the data provide no horizontal variation with which to determine a slope separately from the intercept. Always check that the denominator is nonzero before using the formula.

### 3.3 Deriving the matrix estimator

Let $\boldsymbol\theta=(\alpha,\beta)^{\mathsf T}$. Because $\mathbf e=\mathbf y-X\boldsymbol\theta$, the sum of squared errors is

$$
S(\boldsymbol\theta)
=(\mathbf y-X\boldsymbol\theta)^{\mathsf T}(\mathbf y-X\boldsymbol\theta).
$$

Expanding the product gives

$$
S(\boldsymbol\theta)
=\mathbf y^{\mathsf T}\mathbf y
-\mathbf y^{\mathsf T}X\boldsymbol\theta
-\boldsymbol\theta^{\mathsf T}X^{\mathsf T}\mathbf y
+\boldsymbol\theta^{\mathsf T}X^{\mathsf T}X\boldsymbol\theta.
$$

The two middle terms are equal scalars, even though they are written as transposes of one another. Differentiating with respect to the coefficient vector gives

$$
\frac{\partial S}{\partial\boldsymbol\theta}
=-2X^{\mathsf T}\mathbf y+2X^{\mathsf T}X\boldsymbol\theta.
$$

Set this gradient equal to the zero vector:

$$
X^{\mathsf T}X\hat{\boldsymbol\theta}=X^{\mathsf T}\mathbf y.
$$

These are the matrix normal equations. When $X^{\mathsf T}X$ is invertible, solve them to obtain

$$
\hat{\boldsymbol\theta}
=(X^{\mathsf T}X)^{-1}X^{\mathsf T}\mathbf y.
$$

The second derivative matrix of $S$ is $2X^{\mathsf T}X$. If $X$ has full column rank, this matrix is positive definite, so the stationary point is the unique minimum of the squared-error criterion. This explains why the normal equations produce the least-squares fit rather than a maximum or a saddle point.

For the straight-line design matrix, multiplying out the normal equations gives

$$
X^{\mathsf T}X=
\begin{pmatrix}
n&\sum x_i\\
\sum x_i&\sum x_i^2
\end{pmatrix},\qquad
X^{\mathsf T}\mathbf y=
\begin{pmatrix}
\sum y_i\\
\sum x_i y_i
\end{pmatrix}.
$$

Thus the matrix method and the two scalar normal equations are the same calculation written in different notation.

### 3.4 Unbiasedness and coefficient covariance

Under the source assumptions, $E(\mathbf e)=\mathbf0$. The estimator can be written as

$$
\hat{\boldsymbol\theta}
=(X^{\mathsf T}X)^{-1}X^{\mathsf T}(X\boldsymbol\theta+\mathbf e)
=\boldsymbol\theta+(X^{\mathsf T}X)^{-1}X^{\mathsf T}\mathbf e.
$$

Taking expectations while treating the design matrix as fixed gives

$$
E(\hat{\boldsymbol\theta})
=\boldsymbol\theta+(X^{\mathsf T}X)^{-1}X^{\mathsf T}E(\mathbf e)
=\boldsymbol\theta.
$$

Therefore $\hat\alpha$ and $\hat\beta$ are unbiased estimators of $\alpha$ and $\beta$ under the zero-mean error assumption. This does not say that every fitted line equals the true line for one particular sample; unbiasedness describes the average over repeated samples under the model.

If the errors are independent and each has variance $\sigma^2$, then $\operatorname{Var}(\mathbf e)=\sigma^2 I$. It follows that

$$
\operatorname{Var}(\hat{\boldsymbol\theta})
=(X^{\mathsf T}X)^{-1}X^{\mathsf T}\operatorname{Var}(\mathbf e)X(X^{\mathsf T}X)^{-1}
=\sigma^2(X^{\mathsf T}X)^{-1}.
$$

This formula describes the covariance of the two estimated coefficients under the stated assumptions. It is not a formula for the variance of the responses themselves.

### 3.5 Interpreting the fitted line

After calculating the estimates, write the fitted relationship as

$$
\hat y=\hat\alpha+\hat\beta x.
$$

The intercept is the fitted response at $x=0$. The slope is the change in fitted response for a one-unit increase in $x$. If the slope is negative, the fitted response decreases as $x$ increases; if it is positive, it increases. These are descriptions of the fitted line, not proof that changing $x$ causes a change in $y$.

For each observed $x_i$, the fitted value is $\hat y_i=\hat\alpha+\hat\beta x_i$, and the residual is $r_i=y_i-\hat y_i$. Positive residuals lie above the fitted line and negative residuals lie below it. The least-squares criterion minimizes the sum of the squared residuals.

## 4. Worked Applications

### 4.1 Five-point straight-line fit from the lecture example

Fit $y=\alpha+\beta x$ to the five observations

$$
\begin{array}{c|ccccc}
x_i&-2&-1&0&1&2\\
\hline
y_i&0&0&1&1&3
\end{array}
$$

**Step 1: Form the design matrix and response vector.** The first column of the design matrix contains ones for the intercept, and the second contains the observed $x_i$ values:

$$
X=
\begin{pmatrix}
1&-2\\
1&-1\\
1&0\\
1&1\\
1&2
\end{pmatrix},\qquad
\mathbf y=
\begin{pmatrix}
0\\
0\\
1\\
1\\
3
\end{pmatrix},\qquad
\boldsymbol\theta=
\begin{pmatrix}
\alpha\\
\beta
\end{pmatrix}.
$$

The model is $\mathbf y=X\boldsymbol\theta+\mathbf e$.

**Step 2: Calculate $X^{\mathsf T}X$ and $X^{\mathsf T}\mathbf y$.** The explanatory values sum to zero and their squared sum is ten. The response values sum to five, and the cross-product sum is

$$
\sum x_i y_i=(-2)(0)+(-1)(0)+(0)(1)+(1)(1)+(2)(3)=7.
$$

Therefore

$$
X^{\mathsf T}X=
\begin{pmatrix}
5&0\\
0&10
\end{pmatrix},\qquad
X^{\mathsf T}\mathbf y=
\begin{pmatrix}
5\\7
\end{pmatrix}.
$$

**Step 3: Solve the normal equations.**

$$
\begin{pmatrix}
5&0\\
0&10
\end{pmatrix}
\begin{pmatrix}
\hat\alpha\\
\hat\beta
\end{pmatrix}
=
\begin{pmatrix}
5\\
7
\end{pmatrix}.
$$

The first row gives $5\hat\alpha=5$, so $\hat\alpha=1$. The second gives $10\hat\beta=7$, so $\hat\beta=0.7$.

**Step 4: State and interpret the fitted line.**

$$
\hat y=1+0.7x.
$$

The line crosses the vertical axis at one. For each one-unit increase in $x$, the fitted value increases by $0.7$ units. The point $(\bar x,\bar y)=(0,1)$ lies on the fitted line, since the sample means are $\bar x=0$ and $\bar y=1$.

**Step 5: Check the result using residuals.** The fitted values at $x=-2,-1,0,1,2$ are $-0.4,0.3,1,1.7,2.4$. The corresponding residuals are $0.4,-0.3,0,-0.7,0.6$. Their sum is zero, as expected for a least-squares line with an intercept, and the sum of squared residuals is

$$
0.4^2+(-0.3)^2+0^2+(-0.7)^2+0.6^2=1.10.
$$

This supplies an independent arithmetic check of the fitted line and the least-squares criterion.

### 4.2 Seven-point matrix question from the verified CAT

The verified assessment asks for a straight-line fit to

$$
\begin{array}{c|rrrrrrr}
x_i&6&-4&10&8&4&13&2\\
\hline
y_i&20&18&6&2&13&22&5
\end{array}
$$

**Step 1: Set up the matrices.**

$$
X=
\begin{pmatrix}
1&6\\
1&-4\\
1&10\\
1&8\\
1&4\\
1&13\\
1&2
\end{pmatrix},\qquad
\boldsymbol\theta=
\begin{pmatrix}
\alpha\\
\beta
\end{pmatrix},\qquad
\mathbf y=
\begin{pmatrix}
20\\
18\\
6\\
2\\
13\\
22\\
5
\end{pmatrix}.
$$

**Step 2: Calculate the required sums.**

$$
\sum x_i=39,\qquad \sum y_i=86,\qquad \sum x_i^2=405,\qquad \sum x_i y_i=472.
$$

For example, $\sum x_i y_i=6(20)+(-4)(18)+10(6)+8(2)+4(13)+13(22)+2(5)=472$. The squared-value total is $6^2+(-4)^2+10^2+8^2+4^2+13^2+2^2=405$.

**Step 3: Form the normal equations.**

$$
X^{\mathsf T}X=
\begin{pmatrix}
7&39\\
39&405
\end{pmatrix},\qquad
X^{\mathsf T}\mathbf y=
\begin{pmatrix}
86\\472
\end{pmatrix}.
$$

Thus

$$
\begin{pmatrix}
7&39\\
39&405
\end{pmatrix}
\begin{pmatrix}
\hat\alpha\\
\hat\beta
\end{pmatrix}
=
\begin{pmatrix}
86\\
472
\end{pmatrix}.
$$

**Step 4: Check invertibility and solve.** The determinant is

$$
7(405)-39^2=2835-1521=1314\ne0,
$$

so the coefficient matrix is invertible. Its inverse is

$$
(X^{\mathsf T}X)^{-1}
=\frac{1}{1314}
\begin{pmatrix}
405&-39\\
-39&7
\end{pmatrix}.
$$

Therefore

$$
\hat\alpha
\frac{405(86)-39(472)}{1314}
\frac{16422}{1314}
\frac{2737}{219}
\approx12.4977,
$$

and

$$
\hat\beta
\frac{-39(86)+7(472)}{1314}
\frac{-50}{1314}
-\frac{25}{657}
\approx-0.0381.
$$

**Step 5: State the fitted line.**

$$
\hat y=12.4977-0.0381x.
$$

The estimated slope is negative, so the fitted response decreases by about $0.0381$ units for each one-unit increase in $x$. This describes the fitted line for these observations; it should not be interpreted as a causal conclusion.

**Step 6: Check with the original normal equations.** Using the rounded estimates,

$$
7(12.4977)+39(-0.0381)\approx86,
$$

$$
39(12.4977)+405(-0.0381)\approx472.
$$

The small differences, if any, are due to rounding. Using the exact fractions satisfies the two equations exactly.

### 4.3 Reading the matrix formula as a repeatable procedure

For a new straight-line dataset, the matrix solution follows the same sequence:

1. Keep each $x_i$ paired with its corresponding $y_i$.
2. Form the $n\times2$ matrix with a leading column of ones and a second column of $x_i$ values.
3. Form the $n\times1$ response vector.
4. Calculate $X^{\mathsf T}X$ and $X^{\mathsf T}\mathbf y$.
5. Check that the determinant is nonzero for the two-parameter straight-line case.
6. Solve the normal equations, or calculate $(X^{\mathsf T}X)^{-1}X^{\mathsf T}\mathbf y$.
7. Write the fitted line and interpret the sign and units of its slope.
8. Check the calculations using the normal equations, the sample means, or residuals.

## 5. Revision Summary and Common Errors

### 5.1 Essential results to remember

- The source model is $y_i=\alpha+\beta x_i+e_i$, with independent errors of mean zero and common variance $\sigma^2$.
- Least squares minimizes $S=\sum_{i=1}^{n}(y_i-\alpha-\beta x_i)^2$.
- The scalar normal equations are $\sum y_i=n\alpha+\beta\sum x_i$ and $\sum x_i y_i=\alpha\sum x_i+\beta\sum x_i^2$.
- The slope can be calculated from the centered cross-products, and the intercept is $\hat\alpha=\bar y-\hat\beta\bar x$.
- In matrix form, $\mathbf y=X\boldsymbol\theta+\mathbf e$ and $\hat{\boldsymbol\theta}=(X^{\mathsf T}X)^{-1}X^{\mathsf T}\mathbf y$, provided $X^{\mathsf T}X$ is invertible.
- Under the source's zero-mean error assumption, the least-squares coefficient estimators are unbiased. Under independence and common error variance, their covariance matrix is $\sigma^2(X^{\mathsf T}X)^{-1}$.
- The fitted line passes through $(\bar x,\bar y)$ when an intercept is included.

### 5.2 Common errors and how to avoid them

- **Leaving out the intercept column.** For the model $\alpha+\beta x_i$, the design matrix must have a column of ones. Without it, the model is forced through the origin, which is a different model.
- **Pairing an $x_i$ with the wrong $y_i$.** Keep the row order identical in $X$ and $\mathbf y$.
- **Confusing $X$ and $X^{\mathsf T}X$.** $X$ is $n\times2$; $X^{\mathsf T}X$ is $2\times2$. The dimensions of every multiplication should agree.
- **Using $X X^{\mathsf T}$ in the coefficient formula.** The correct normal matrix is $X^{\mathsf T}X$, and the right side is $X^{\mathsf T}\mathbf y$.
- **Omitting parentheses in the squared-error criterion.** The residual is $y_i-\alpha-\beta x_i$; square the entire residual, not only one term.
- **Losing the sign in the slope numerator.** Compute $n\sum x_i y_i-(\sum x_i)(\sum y_i)$ carefully, or use the centered formula.
- **Using rounded values too early.** Keep exact fractions through the matrix solution, then round the final coefficients.
- **Ignoring singularity.** If the $x_i$ values do not vary, the denominator in the slope formula is zero and $X^{\mathsf T}X$ cannot be inverted.
- **Confusing residuals with model errors.** Residuals use fitted coefficients and are observable after fitting; model errors refer to deviations from the unknown true regression relationship.
- **Overstating what the fitted line means.** A negative or positive slope describes the fitted association in the observed data; it does not by itself prove cause and effect.
- **Claiming unbiasedness without its condition.** The expectation calculation uses $E(\mathbf e)=\mathbf0$ and treats the design values as fixed.
- **Forgetting the distinction between criterion and estimate.** $S$ is the quantity minimized; $\hat\alpha$ and $\hat\beta$ are the estimates at its minimum.

### 5.3 Suggested answer plan for a six-mark matrix question

A complete compact answer should show the model in matrix form, correctly write $X$, $\boldsymbol\theta$, and $\mathbf y$, calculate $X^{\mathsf T}X$ and $X^{\mathsf T}\mathbf y$, solve the normal equations or use the inverse formula, and state the fitted line. Show enough intermediate arithmetic that a marker can see where each coefficient came from. Finish with one check, such as substitution into the normal equations or verification that the fitted line passes through $(\bar x,\bar y)$.
'''
