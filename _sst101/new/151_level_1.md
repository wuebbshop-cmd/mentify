## 1. Foundational Concepts, Definitions, and Axioms

### 1.1 A shopkeeper's notebook

Imagine a shopkeeper who sells cold drinks beside a busy bus stop. Every evening she writes two numbers in a notebook: the highest temperature recorded that day, and the number of bottles she sold. After a month she flicks back through the pages and notices something she had already half suspected. The hot days and the big sales sit on the same pages. When the temperature climbs, the number of bottles climbs with it. When a cool spell arrives, the sales figures shrink.

Now picture a second trader a few metres away who sells umbrellas. His notebook tells the opposite story: the hotter the day, the fewer umbrellas leave his stall. One number rises while the other falls.

Finally, consider a third column that could be added to either notebook: the number of letters in the surname of the first customer of the day. There is no reason at all for that number to move with the temperature. Some hot days begin with a long surname, some with a short one, and the same is true of cool days.

Three notebooks, three different situations, and the whole of this topic is contained in them. Two quantities measured on the same occasions either tend to move together, tend to move in opposite directions, or show no tendency at all. Measuring that tendency, and putting a single number on it, is **correlation**. Drawing a straight line through the pattern so that a missing value can be guessed is **regression**. The shopkeeper's notebook is worth keeping in mind, because every symbol that follows is only a careful way of writing down what she saw.

### 1.2 From notebook pages to a scatter picture

The first tool is not a formula but a drawing. Take each day and make it a dot: temperature measured along the horizontal direction, bottles sold measured up the vertical direction. A month of trading becomes a cloud of dots. Statisticians call this cloud a **scatter diagram**, and reading it is a skill worth acquiring before any arithmetic begins, because the arithmetic is only a summary of what the eye already sees.

Four features of the cloud matter.

The first is **direction**. If the cloud drifts upward as it moves to the right, larger values of the first quantity go with larger values of the second. That is called a **positive association**. If the cloud drifts downward as it moves to the right, larger values of the first go with smaller values of the second, and that is a **negative association**.

The second is **strength**. A cloud that is long and thin, so that the dots sit almost on a single straight track, shows a strong association. A cloud that is round, or scattered like handfuls of sand, shows a weak association. Strength is about how nearly the dots can be covered by a straight track, not about how steep the track would be.

The third is **form**. The track may be straight, or it may bend. A bending track is still an association, but the methods in this topic are built for straight tracks. They measure **linear** association and nothing else.

The fourth is **irregularity**. A single dot far away from the rest, or a small cluster sitting off to one side, can pull any summary number towards itself. Such points deserve a second look before they are trusted, because a mis-typed figure in a notebook produces exactly the same picture as a genuinely unusual day.

### 1.3 The words we will use

| Word | What it means in plain language |
| --- | --- |
| Bivariate data | Data in which two quantities are measured on each individual or occasion |
| Variate | One of the quantities, taking different values from individual to individual |
| Scatter diagram | A plot of the paired observations as dots in the plane |
| Positive association | Larger values of one quantity accompany larger values of the other |
| Negative association | Larger values of one quantity accompany smaller values of the other |
| Linear association | Association whose track is a straight line |
| Independent variable | The quantity used as the input for a prediction |
| Dependent variable | The quantity being predicted |
| Residual | The vertical gap between an observed dot and a fitted line |
| Extrapolation | Predicting outside the range of values actually observed |

### 1.4 The data as a list of pairs

Notation now becomes unavoidable, so every symbol will be said in words before it is used.

We measure two quantities on each of $n$ individuals or occasions. The count $n$ is simply how many pairs we have. For the $i$-th individual we write the pair $(x_i, y_i)$. The letter $i$ is a label, not a value: it counts from $1$ up to $n$. The symbol $x_i$ means "the value of the first quantity for individual $i$", and $y_i$ means "the value of the second quantity for the same individual".

Subscripts are sometimes a nuisance, so the whole list is often written with the subscript dropped: $x$ and $y$ stand for the two quantities, and the pair $(x, y)$ stands for one observation. Every formula in this topic treats $x$ and $y$ in exactly the same way, apart from the formulas for the regression lines, where the roles are deliberately made different.

### 1.5 The average of each list

Before asking whether the two lists move together, we need to know where each list sits. The **mean** of the first list is written $\bar{x}$, read as "x bar", and is the total of the values divided by how many there are.

$$
\bar{x} = \frac{1}{n}\sum_{i=1}^{n} x_i
$$

The symbol $\sum$ is the Greek capital sigma and means "add up". The expression under it, $i = 1$, says where to start, and the expression above it, $n$, says where to stop. So the right-hand side says: add $x_1, x_2$ and so on up to $x_n$, then divide by $n$. The mean of the second list, written $\bar{y}$, is defined in exactly the same way with $y$ in place of $x$.

### 1.6 Moving together: the idea of covariance

The heart of the subject is a single product. For each individual, ask two questions. Is this individual's $x$ above the average $x$? Is this individual's $y$ above the average $y$? Write the answers as signed distances, $x_i - \bar{x}$ and $y_i - \bar{y}$, where a positive number means "above average" and a negative number means "below average".

Now multiply the two signed distances together. The product has a simple meaning:

- If both distances are positive, or both are negative, the product is **positive**, and the individual sits in the same corner of the cloud as the general trend.
- If one distance is positive and the other negative, the product is **negative**, and the individual works against the trend.

Adding these products over all individuals and dividing by $n$ gives a single number called the **covariance**.

$$
\text{Cov}(x, y) = \frac{1}{n}\sum_{i=1}^{n}\left(x_i - \bar{x}\right)\left(y_i - \bar{y}\right)
$$

A large positive covariance means the products are mostly positive, so the two quantities rise and fall together. A large negative covariance means the products are mostly negative, so they move in opposite directions. A covariance near zero means the positive and negative products cancel, so there is no straight-line tendency.

The covariance has one serious defect: its size depends on the units. Measure the first quantity in shillings instead of thousands of shillings and the covariance changes by a factor of a thousand, even though nothing about the association has changed. A number that jumps when a unit is changed cannot be a good measure of strength.

### 1.7 Pearson's correlation coefficient

The defect is repaired by dividing each quantity by its own spread. The spread used is the **standard deviation**, written $s_x$ for the first quantity and $s_y$ for the second, and defined as the square root of the average squared distance from the mean.

$$
s_x = \sqrt{\frac{1}{n}\sum_{i=1}^{n}\left(x_i - \bar{x}\right)^{2}}
$$

> **Definition (Pearson's correlation coefficient).** For paired observations $(x_1, y_1), \dots, (x_n, y_n)$ the product-moment correlation coefficient is

$$
r_{xy} = \frac{\text{Cov}(x, y)}{\sqrt{\text{Var}(x)\,\text{Var}(y)}}
$$

> where $\text{Cov}(x,y)$ is the covariance and $\text{Var}(x) = s_x^{2}$, $\text{Var}(y) = s_y^{2}$ are the two variances.

Read the definition aloud in words: divide the amount by which the two quantities move together by the product of the amounts by which each moves on its own. The division removes the units, because a covariance in units of $x$ times units of $y$ is divided by a product carrying exactly those units. What survives is a pure number, and being pure it can be compared across quite different problems.

The definition above is elegant but awkward to compute, because it requires every deviation from every mean. Multiplying out the brackets and simplifying gives the **computational form**, which needs only five sums.

$$
r_{xy} = \frac{n\sum x_i y_i - \sum x_i \sum y_i}{\sqrt{\left\{\left[n\sum x_i^{2} - \left(\sum x_i\right)^{2}\right]\left[n\sum y_i^{2} - \left(\sum y_i\right)^{2}\right]\right\}}}
$$

Every symbol in that expression has already been explained. The sum $\sum x_i y_i$ means: for each individual multiply the two values together, then add the products. The sums $\sum x_i^{2}$ and $\sum y_i^{2}$ mean: square each value first, then add. The count $n$ multiplies in two places.

Dividing top and bottom by $n$ gives the version most often used in practice, where each bracket is a sum of squared deviations written in a form that avoids computing deviations individually.

$$
r_{xy} = \frac{\sum x_i y_i - \frac{1}{n}\sum x_i \sum y_i}{\sqrt{\left\{\left[\sum x_i^{2} - \frac{1}{n}\left(\sum x_i\right)^{2}\right]\left[\sum y_i^{2} - \frac{1}{n}\left(\sum y_i\right)^{2}\right]\right\}}}
$$

The quantity $\sum x_i^{2} - \frac{1}{n}\left(\sum x_i\right)^{2}$ is written $S_{xx}$ and called the **corrected sum of squares of x**. In the same way $S_{yy}$ is the corrected sum of squares of $y$, and $S_{xy} = \sum x_i y_i - \frac{1}{n}\sum x_i \sum y_i$ is the **corrected sum of products**. With this shorthand the coefficient becomes simply

$$
r_{xy} = \frac{S_{xy}}{\sqrt{S_{xx}\,S_{yy}}} .
$$

### 1.8 What the square of r tells you

Suppose somebody reports $r = 0.9$. Is nine tenths of the story explained? Not quite: the number that answers that question is $r^{2} = 0.81$, so about eighty-one per cent of the variation in one quantity goes with the variation in the other, and about nineteen per cent does not. The quantity $r^{2}$ is called the **coefficient of determination**, and it is always between $0$ and $1$ because $r$ is always between $-1$ and $1$.

The name is well chosen. When a line is fitted and used to predict, the total variation of the response can be split into a part accounted for by the line and a part left over as scattered error. The ratio of the accounted-for part to the total is exactly $r^{2}$. A coefficient of determination of $0.81$ therefore says the fitted line accounts for eighty-one per cent of the total variation.

### 1.9 Regression: fitting a straight line

Correlation describes. Regression predicts. To predict we nominate one quantity as the input, called the **independent variable**, and the other as the output, called the **dependent variable**. The convention in this topic is that $X$ is the independent variable and $Y$ the dependent variable.

> **Definition (Simple linear regression of Y on X).** The regression equation of $Y$ on $X$ has the form

$$
Y = a + bX
$$

> where $a$ and $b$ are constants. The constant $b$ is the slope and is called the **coefficient of regression of Y on X**; the constant $a$ is the intercept, the value the line takes when $X = 0$.

The slope is the answer to a practical question: by how much does the predicted $Y$ change when $X$ increases by one unit? If $b = 1.2$ and $X$ is hours of revision while $Y$ is marks, then one extra hour of revision goes with about $1.2$ extra marks on the fitted line.

No straight line passes exactly through every dot, so the line must be chosen by a rule. The rule used throughout is **least squares**. For a candidate line, measure the vertical gap between each dot and the line. Those gaps are called residuals. Square each gap, so that a gap above the line and a gap below the line cannot cancel, and add the squares. The least squares line is the one line, among all possible straight lines, that makes that total as small as possible. Section 3 shows where the resulting equations come from; for now the important point is that the rule is a genuine minimisation, not an arbitrary choice.

### 1.10 Why there are two regression lines

Because regression is directional, there are two of them. The line of $Y$ on $X$ predicts $Y$ from $X$ and is written $Y = a + bX$. The line of $X$ on $Y$ predicts $X$ from $Y$ and is written $X = c + dY$. The two lines are different unless the association is perfect.

Why? Least squares minimises vertical gaps for the first line and horizontal gaps for the second. A vertical gap and a horizontal gap are not the same distance, so the two minimisations choose different lines. Only when every dot lies exactly on one straight track do vertical and horizontal gaps agree, and only then do the two lines coincide.

### 1.11 Ranks and Spearman's coefficient

Sometimes the values themselves are unreliable or unavailable, but the order is known. Two judges may place the same eight dishes first, second, third and so on without agreeing on any numerical score. Sometimes the data are genuinely ordinal, such as a preference rating. In such cases we work with **ranks**.

Give rank $1$ to the smallest value of a list, rank $2$ to the next, and so on up to rank $n$. Then compute the correlation between the two lists of ranks. The result is **Spearman's rank correlation coefficient**, written $r_s$.

> **Definition (Spearman's coefficient, untied ranks).** Let $d_i$ be the difference between the rank of individual $i$ in the first list and the rank of the same individual in the second list. If no rank is repeated in either list, then

$$
r_s = 1 - \frac{6\sum d_i^{2}}{n\left(n^{2} - 1\right)} .
$$

The denominator $n\left(n^{2}-1\right)$ is a fixed number once the sample size is known, so the whole formula is governed by the single quantity $\sum d_i^{2}$, the sum of squared rank differences. Perfect agreement gives every $d_i = 0$, hence $r_s = 1$. Complete disagreement gives a large sum of squared differences and a value near $-1$.

When ranks are repeated, the formula needs a small correction, because tied individuals do not receive the distinct ranks $1$ to $n$. The correction is developed in Section 3.

### 1.12 The two ideas side by side

| Question | Tool | Symbol | Symmetric? |
| --- | --- | --- | --- |
| How strong and which way is the straight-line association? | Correlation | $r_{xy}$ | Yes |
| What value of $Y$ should be expected for a given $X$? | Regression of $Y$ on $X$ | $Y = a + bX$ | No |
| What value of $X$ should be expected for a given $Y$? | Regression of $X$ on $Y$ | $X = c + dY$ | No |
| How closely do two orderings agree? | Rank correlation | $r_s$ | Yes |

## 2. Theorems, Lemmas, and Analytical Properties

### 2.1 The coefficient never leaves the interval from minus one to one

> **Theorem (Boundedness of r).** For any paired observations with non-zero spread in both quantities, $-1 \le r_{xy} \le 1$.

The proof, given in Section 3, is an application of the Cauchy–Schwarz inequality. For everyday work the theorem has two uses. It is a guarantee that the number is interpretable on a fixed scale, and it is a check on arithmetic: any computed value outside the interval is simply wrong, and the error is in the sums, not in the theory.

### 2.2 The extreme values describe perfect straight tracks

> **Theorem (Characterisation of the extremes).** The equality $r_{xy} = 1$ holds if and only if all the points lie on a straight line of positive slope. The equality $r_{xy} = -1$ holds if and only if all the points lie on a straight line of negative slope.

When every point lies on one straight track, every deviation from the mean in the first quantity is matched by a proportional deviation in the second, with the same constant of proportionality throughout. Then the covariance attains its largest possible value relative to the two spreads, and the ratio reaches exactly one in absolute value.

### 2.3 Neither origin nor scale affects the coefficient

> **Theorem (Invariance).** Let $u_i = \alpha + \beta x_i$ and $v_i = \gamma + \delta y_i$ with $\beta \ne 0$ and $\delta \ne 0$. Then $r_{uv} = r_{xy}$ if $\beta\delta > 0$, and $r_{uv} = -r_{xy}$ if $\beta\delta < 0$.

In words: adding a constant to every value of a quantity, or multiplying every value by a positive constant, leaves the correlation untouched. Multiplying by a negative constant reverses the sign.

This is the most useful practical fact in the whole topic. Because a change of origin and a positive change of scale are permitted, the arithmetic can be done on small, round numbers. Subtracting a convenient constant from every $x$ and every $y$ is called the **short method** or the **method of deviations**, and it can turn a long multiplication into a mental one.

### 2.4 The coefficient is symmetric

> **Lemma (Symmetry).** $r_{xy} = r_{yx}$.

The formula for $r$ treats the two quantities identically: interchanging them swaps the two brackets under the square root and leaves the numerator unchanged. Symmetry is what distinguishes correlation from regression. Correlation does not care which quantity is called input and which is called output; regression cares a great deal.

### 2.5 A coefficient of zero says only that there is no straight track

> **Theorem (Independence implies zero correlation, but not conversely).** If two quantities are probabilistically independent then $r_{xy} = 0$. The converse fails: there are strongly related quantities for which $r_{xy} = 0$.

The second half of the statement is the one that matters in practice. Take $x$ equally spaced from $-2$ to $2$ and take $y = x^{2}$. The relationship is exact and completely deterministic, yet the covariance vanishes because positive and negative deviations of $x$ are matched by the same positive deviation of $y$, and the products cancel. A value of zero therefore certifies the absence of a *linear* tendency, and nothing more.

### 2.6 The slope and the correlation are different animals

> **Theorem (Relation between slope and coefficient).** For the line of $Y$ on $X$ the slope is

$$
b_{yx} = r_{xy}\frac{s_y}{s_x}
$$

> and for the line of $X$ on $Y$ the slope is

$$
b_{xy} = r_{xy}\frac{s_x}{s_y} .
$$

Two consequences are immediate. First, the slope carries units, because it is a ratio of a spread in $y$ to a spread in $x$; the correlation does not. Second, the sign of the slope is the sign of $r$, so a positive slope and a positive correlation always accompany one another, and a negative slope always accompanies a negative correlation.

A steep slope does not imply a strong correlation. If the standard deviation of $y$ is large compared with that of $x$, the slope can be large in size while the points are widely scattered around the line.

### 2.7 The two slopes multiply to the square of the coefficient

> **Theorem (Product of the regression coefficients).** With $b_{yx}$ and $b_{xy}$ as above,

$$
b_{yx}\,b_{xy} = r_{xy}^{2} .
$$

Multiply the two expressions in the previous theorem: the factors $s_y/s_x$ and $s_x/s_y$ cancel to one, leaving $r^{2}$. The result is a powerful consistency check. If a calculation gives two slopes whose product exceeds one, or is negative while both slopes are positive, then at least one of the numbers is wrong. The theorem also shows that the geometric mean of the two slopes has size equal to the absolute correlation.

### 2.8 Both lines pass through the point of averages

> **Lemma (Common point).** The line of $Y$ on $X$ and the line of $X$ on $Y$ both pass through the point $(\bar{x}, \bar{y})$.

Substituting $X = \bar{x}$ into $Y = a + bX$ gives $Y = \bar{y} - b\bar{x} + b\bar{x} = \bar{y}$, because the intercept was chosen as $a = \bar{y} - b\bar{x}$. The same substitution in the other line gives the same point. Geometrically, the two fitted lines cross exactly at the centre of the cloud of dots.

### 2.9 The coefficient of determination lies between zero and one

> **Theorem (Determination).** Write the total sum of squared deviations of the response as $S_{yy}$, the sum of squared residuals from the fitted line as $SSE$, and the part accounted for by the line as $SSR = S_{yy} - SSE$. Then

$$
r_{xy}^{2} = \frac{SSR}{S_{yy}} = 1 - \frac{SSE}{S_{yy}} .
$$

Because a sum of squares cannot be negative, $0 \le SSR \le S_{yy}$ and therefore $0 \le r^{2} \le 1$. The square of the correlation is thus a proportion, and can be reported as a percentage without ambiguity.

### 2.10 The standard error of estimate measures the leftover scatter

> **Definition (Standard error of estimate).** For the line of $Y$ on $X$ fitted to $n$ pairs, the standard error of estimate is

$$
s_e = \sqrt{\frac{SSE}{n-2}} .
$$

The numerator is the sum of squared residuals: what the line failed to explain. The divisor is $n-2$ rather than $n$ because two quantities, the intercept and the slope, were estimated from the same data, and each estimate consumes one degree of freedom. The standard error is expressed in the units of $Y$, so it can be interpreted directly as a typical size of the vertical gap between an observation and the line. When $r^{2} = 1$ the residuals all vanish and $s_e = 0$; when $r^{2} = 0$ the line explains nothing and $s_e$ is at its largest.

### 2.11 Rank correlation inherits the bounds

> **Theorem (Bounds for Spearman's coefficient).** For untied ranks, $r_s$ lies between $-1$ and $1$, and it equals $1$ exactly when the two orderings are identical and $-1$ exactly when one ordering is the reverse of the other.

The reason is that $r_s$ is itself a product-moment correlation, computed on the ranks rather than on the raw values. Ranks are a perfectly legitimate pair of lists, so every theorem proved about $r$ applies to $r_s$ without change.

## 3. Formal Proofs, Derivations, and Methods

### 3.1 The computational form of the coefficient

Start from the definition with the covariance and the two variances written out in full.

$$
r_{xy} = \frac{\frac{1}{n}\sum\left(x_i - \bar{x}\right)\left(y_i - \bar{y}\right)}{\sqrt{\left[\frac{1}{n}\sum\left(x_i - \bar{x}\right)^{2}\right]\left[\frac{1}{n}\sum\left(y_i - \bar{y}\right)^{2}\right]}}
$$

The factor $\frac{1}{n}$ appears once in the numerator and once inside each bracket of the denominator, so under the square root it appears once overall. Numerator and denominator therefore carry the same factor and it cancels.

$$
r_{xy} = \frac{\sum\left(x_i - \bar{x}\right)\left(y_i - \bar{y}\right)}{\sqrt{\left[\sum\left(x_i - \bar{x}\right)^{2}\right]\left[\sum\left(y_i - \bar{y}\right)^{2}\right]}}
$$

Now expand the numerator using the fact that sums and constants may be interchanged.

$$
\sum\left(x_i - \bar{x}\right)\left(y_i - \bar{y}\right) = \sum x_i y_i - \bar{y}\sum x_i - \bar{x}\sum y_i + n\bar{x}\bar{y}
$$

Since $\sum x_i = n\bar{x}$ and $\sum y_i = n\bar{y}$, the last three terms collapse.

$$
\sum\left(x_i - \bar{x}\right)\left(y_i - \bar{y}\right) = \sum x_i y_i - n\bar{x}\bar{y}
$$

Applying the same expansion to each squared sum, and using $n\bar{x}\bar{y} = \frac{1}{n}\sum x_i \sum y_i$ together with $n\bar{x}^{2} = \frac{1}{n}\left(\sum x_i\right)^{2}$, produces

$$
r_{xy} = \frac{\sum x_i y_i - \frac{1}{n}\sum x_i \sum y_i}{\sqrt{\left[\sum x_i^{2} - \frac{1}{n}\left(\sum x_i\right)^{2}\right]\left[\sum y_i^{2} - \frac{1}{n}\left(\sum y_i\right)^{2}\right]}} .
$$

This is the working formula. It requires only the five sums $\sum x_i$, $\sum y_i$, $\sum x_i y_i$, $\sum x_i^{2}$ and $\sum y_i^{2}$, all of which can be accumulated in a single pass through the data.

### 3.2 Why a shift of origin leaves the coefficient unchanged

Let $u_i = x_i - A$ for a constant $A$. The mean of the new list is $\bar{u} = \bar{x} - A$, so each deviation is untouched.

$$
u_i - \bar{u} = \left(x_i - A\right) - \left(\bar{x} - A\right) = x_i - \bar{x}
$$

The deviations, and therefore the sum of products and the sums of squares, are identical for the new list. Hence $r_{uv} = r_{xy}$ for any paired shift. The same argument works for a positive scale change: writing $u_i = \beta x_i$ with $\beta > 0$ multiplies every deviation by $\beta$, so numerator and denominator both gain a factor $\beta$ in the first bracket and the factor cancels. A negative $\beta$ multiplies deviations by a negative number, which reverses the sign of the numerator only.

### 3.3 Where the normal equations come from

The least squares rule chooses $a$ and $b$ to minimise the total of squared vertical gaps.

$$
Q(a, b) = \sum_{i=1}^{n}\left(y_i - a - bx_i\right)^{2}
$$

Treat $Q$ as a function of the two unknowns. Expand the square.

$$
Q(a, b) = \sum y_i^{2} - 2a\sum y_i - 2b\sum x_i y_i + na^{2} + 2ab\sum x_i + b^{2}\sum x_i^{2}
$$

Differentiate with respect to $a$ and with respect to $b$, treating the other unknown as a constant.

$$
\frac{\partial Q}{\partial a} = -2\sum y_i + 2na + 2b\sum x_i
$$

$$
\frac{\partial Q}{\partial b} = -2\sum x_i y_i + 2a\sum x_i + 2b\sum x_i^{2}
$$

At the minimum both derivatives vanish. Dividing each by two and rearranging gives the pair of **normal equations**.

$$
\sum y = na + b\sum x
$$

$$
\sum x y = a\sum x + b\sum x^{2}
$$

The second derivatives are the constants $2n$ and $2\sum x_i^{2}$, both positive, and the determinant $n\sum x_i^{2} - \left(\sum x_i\right)^{2}$ is positive whenever the $x$ values are not all equal. The stationary point is therefore a genuine minimum, and it is unique.

### 3.4 Solving the normal equations

Divide the first normal equation by $n$ to obtain $\bar{y} = a + b\bar{x}$, which rearranges to

$$
a = \bar{y} - b\bar{x} .
$$

Substitute this into the second normal equation.

$$
\sum x_i y_i = \left(\bar{y} - b\bar{x}\right)\sum x_i + b\sum x_i^{2}
$$

Replacing $\sum x_i$ by $n\bar{x}$ and collecting the terms in $b$,

$$
\sum x_i y_i - n\bar{x}\bar{y} = b\left(\sum x_i^{2} - n\bar{x}^{2}\right) .
$$

The left side is $S_{xy}$ and the bracket on the right is $S_{xx}$, so

$$
b = \frac{S_{xy}}{S_{xx}} .
$$

The intercept follows from $a = \bar{y} - b\bar{x}$. For the line of $X$ on $Y$ the whole derivation repeats with the roles exchanged, giving

$$
d = \frac{S_{xy}}{S_{yy}}, \qquad c = \bar{x} - d\bar{y} .
$$

### 3.5 Why the slope equals the correlation times the spread ratio

Starting from $b = S_{xy}/S_{xx}$, multiply and divide by $\sqrt{S_{yy}}$.

$$
b = \frac{S_{xy}}{\sqrt{S_{xx}\,S_{yy}}} \cdot \frac{\sqrt{S_{yy}}}{\sqrt{S_{xx}}}
$$

The first factor is exactly $r_{xy}$. Since $\sqrt{S_{yy}}/\sqrt{S_{xx}} = s_y/s_x$ when both spreads are computed with the same divisor, the result is

$$
b_{yx} = r_{xy}\frac{s_y}{s_x} .
$$

Repeating the argument for the other line gives $b_{xy} = r_{xy}s_x/s_y$, and multiplying the two expressions yields $b_{yx}b_{xy} = r_{xy}^{2}$.

### 3.6 Why the square of the coefficient is a proportion

Write each observation as the fitted value plus its residual, $y_i = \hat{y}_i + e_i$ where $\hat{y}_i = a + bx_i$. Sum the squares.

$$
\sum\left(y_i - \bar{y}\right)^{2} = \sum\left(\hat{y}_i - \bar{y}\right)^{2} + 2\sum\left(\hat{y}_i - \bar{y}\right)e_i + \sum e_i^{2}
$$

The middle term vanishes because the residuals sum to zero and are uncorrelated with the fitted values, a consequence of the two normal equations. What remains is the decomposition

$$
S_{yy} = SSR + SSE .
$$

Dividing by $S_{yy}$ gives $1 = SSR/S_{yy} + SSE/S_{yy}$. The first ratio is $r^{2}$, which can be confirmed by substituting $b = S_{xy}/S_{xx}$ into the expression for $SSR$.

### 3.7 Method: computing the coefficient from a table

Set out the data in a table with five columns: the pair, the product $xy$, the square $x^{2}$ and the square $y^{2}$. Add a totals row. Then proceed in a fixed order.

Step 1. Count the pairs and record $n$.

Step 2. Compute $S_{xy} = \sum xy - \frac{1}{n}\sum x \sum y$.

Step 3. Compute $S_{xx} = \sum x^{2} - \frac{1}{n}\left(\sum x\right)^{2}$.

Step 4. Compute $S_{yy} = \sum y^{2} - \frac{1}{n}\left(\sum y\right)^{2}$.

Step 5. Form $r = S_{xy}/\sqrt{S_{xx}S_{yy}}$ and fix the sign from the sign of $S_{xy}$.

Step 6. Square the result to report the coefficient of determination.

### 3.8 Method: computing Spearman's coefficient

Step 1. Rank the first list from smallest to largest, giving rank $1$ to the smallest value.

Step 2. Rank the second list in the same direction.

Step 3. For ties, give every tied value the average of the ranks it would have occupied.

Step 4. Form the differences $d_i$ and square them.

Step 5. Add the squares and, if any ties occurred, add the correction $\frac{m\left(m^{2}-1\right)}{12}$ for each group of $m$ tied values.

Step 6. Substitute into $r_s = 1 - \frac{6\left(\sum d_i^{2} + \text{correction}\right)}{n\left(n^{2}-1\right)}$ and interpret.

### 3.9 Method: predicting with the correct line

Step 1. Decide which quantity is to be predicted. That quantity must be alone on the left of the equation.

Step 2. Select the line whose subject matches. To predict $Y$, use $Y = a + bX$. To predict $X$, use $X = c + dY$.

Step 3. Substitute the given value of the other quantity and evaluate.

Step 4. Check that the given value lies inside the range of the observed data. If it does not, say plainly that the answer is an extrapolation.

### 3.10 A pre-answer checklist

Before writing a final answer, confirm that the coefficient lies between minus one and one, that its sign matches the sign of the slope, that the product of the two regression slopes equals the square of the coefficient, and that the point of averages satisfies both line equations. Each of these is a cheap test that catches a large share of arithmetic slips.

## 4. Representative Worked Examples and Solutions

### 4.1 Problem: six pairs of revision hours and marks

Six students recorded the hours they revised for a test and the marks they obtained.

| Revision hours ($x$) | 1 | 2 | 3 | 4 | 5 | 6 |
| --- | --- | --- | --- | --- | --- | --- |
| Marks ($y$) | 3 | 5 | 4 | 7 | 8 | 9 |

Compute Pearson's correlation coefficient and the coefficient of determination, and say in words what they mean.

### 4.2 Solution: build the table and compute the coefficient

Step 1. Set out the working values with one row per student.

| $x$ | $y$ | $xy$ | $x^{2}$ | $y^{2}$ |
| --- | --- | --- | --- | --- |
| 1 | 3 | 3 | 1 | 9 |
| 2 | 5 | 10 | 4 | 25 |
| 3 | 4 | 12 | 9 | 16 |
| 4 | 7 | 28 | 16 | 49 |
| 5 | 8 | 40 | 25 | 64 |
| 6 | 9 | 54 | 36 | 81 |
| $\sum 21$ | $\sum 36$ | $\sum 147$ | $\sum 91$ | $\sum 244$ |

Step 2. Record the count.

$$
n = 6
$$

Step 3. Compute the corrected sum of products.

$$
S_{xy} = 147 - \frac{1}{6}\left(21\right)\left(36\right) = 147 - 126 = 21
$$

Step 4. Compute the corrected sum of squares of the revision hours.

$$
S_{xx} = 91 - \frac{1}{6}\left(21\right)^{2} = 91 - 73.5 = 17.5
$$

Step 5. Compute the corrected sum of squares of the marks.

$$
S_{yy} = 244 - \frac{1}{6}\left(36\right)^{2} = 244 - 216 = 28
$$

Step 6. Form the coefficient.

$$
r = \frac{21}{\sqrt{\left(17.5\right)\left(28\right)}} = \frac{21}{\sqrt{490}} = \frac{21}{22.136} \approx 0.9487
$$

Step 7. Square the coefficient.

$$
r^{2} = 0.9487^{2} \approx 0.9000
$$

Step 8. Interpret. The value $0.9487$ is positive and close to one, so the two quantities move together strongly along a straight track: students who revised longer tended to score higher. The coefficient of determination of $0.9$ says that ninety per cent of the variation in marks is accounted for by the straight-line relation with revision hours, leaving about ten per cent to everything else.

### 4.3 Problem: fit the line of marks on revision hours

Fit the least squares line of $Y$ on $X$ for the six students and state the meaning of each constant.

### 4.4 Solution: normal equations step by step

Step 1. Write the normal equations for the line $Y = a + bX$.

$$
\sum y = na + b\sum x
$$

$$
\sum xy = a\sum x + b\sum x^{2}
$$

Step 2. Substitute the five sums and the count.

$$
36 = 6a + 21b
$$

$$
147 = 21a + 91b
$$

Step 3. Multiply the first equation by $3.5$ so that the coefficient of $a$ matches the second.

$$
126 = 21a + 73.5b
$$

Step 4. Subtract this equation from the second.

$$
21 = 17.5b
$$

Step 5. Solve for the slope.

$$
b = \frac{21}{17.5} = 1.2
$$

Step 6. Substitute back into the first equation.

$$
36 = 6a + 21\left(1.2\right) = 6a + 25.2
$$

$$
a = \frac{36 - 25.2}{6} = \frac{10.8}{6} = 1.8
$$

Step 7. Write the fitted line.

$$
Y = 1.8 + 1.2X
$$

Step 8. Interpret the constants. The slope $1.2$ says that, on the fitted line, one further hour of revision goes with $1.2$ further marks. The intercept $1.8$ is the predicted mark for a student who revised for no hours at all, and it is a reminder that the intercept is often a mathematical convenience rather than a real possibility.

Step 9. Check the line passes through the point of averages, where the mean of $x$ is $21/6 = 3.5$ and the mean of $y$ is $36/6 = 6$.

$$
1.8 + 1.2\left(3.5\right) = 1.8 + 4.2 = 6
$$

### 4.5 Problem: predict, and fit the other line

Use the fitted line to predict the mark of a student who revises for $7$ hours. Then fit the line of $X$ on $Y$ and use it to predict the revision hours of a student who scored $10$ marks.

### 4.6 Solution: two predictions from two lines

Step 1. Substitute $X = 7$ into the line of $Y$ on $X$.

$$
Y = 1.8 + 1.2\left(7\right) = 1.8 + 8.4 = 10.2
$$

Step 2. Comment on that answer. The predicted mark is about $10.2$. The observed revision hours ran from $1$ to $6$, so predicting at $7$ is a modest step beyond the data and should be reported with a little caution.

Step 3. Fit the line of $X$ on $Y$ using the second pair of normal equations.

$$
\sum x = nc + d\sum y
$$

$$
\sum xy = c\sum y + d\sum y^{2}
$$

Step 4. Substitute the sums.

$$
21 = 6c + 36d
$$

$$
147 = 36c + 244d
$$

Step 5. Multiply the first equation by $6$ so that the coefficient of $c$ matches the second.

$$
126 = 36c + 216d
$$

Step 6. Subtract this from the second equation.

$$
21 = 28d
$$

Step 7. Solve for the slope.

$$
d = \frac{21}{28} = 0.75
$$

Step 8. Substitute back.

$$
21 = 6c + 36\left(0.75\right) = 6c + 27
$$

$$
c = \frac{21 - 27}{6} = -1
$$

Step 9. Write the second fitted line.

$$
X = -1 + 0.75Y
$$

Step 10. Predict the revision hours of a student who scored $10$ marks.

$$
X = -1 + 0.75\left(10\right) = -1 + 7.5 = 6.5
$$

Step 11. Compare the two lines. They are plainly different: one predicts marks from hours, the other predicts hours from marks. Their slopes have product

$$
1.2 \times 0.75 = 0.9
$$

which equals $r^{2}$ exactly, confirming the worked values.

### 4.7 Problem: two tests, five candidates

Five candidates sat two tests. Their raw marks are recorded, and the marks are to be compared by ordering rather than by their numerical size.

| Candidate | 1 | 2 | 3 | 4 | 5 |
| --- | --- | --- | --- | --- | --- |
| Test A mark ($x$) | 10 | 20 | 30 | 40 | 55 |
| Test B mark ($y$) | 20 | 10 | 30 | 50 | 40 |

Compute Spearman's rank correlation coefficient and interpret the result.

### 4.8 Solution: ranks, differences, coefficient

Step 1. Rank the Test A marks from smallest to largest. The smallest is $10$, so it takes rank $1$; $20$ takes rank $2$; $30$ takes rank $3$; $40$ takes rank $4$; $55$ takes rank $5$.

Step 2. Rank the Test B marks in the same direction. The smallest is $10$, which takes rank $1$; then $20$ takes rank $2$; $30$ takes rank $3$; $40$ takes rank $4$; $50$ takes rank $5$.

Step 3. Form the differences and their squares.

| Candidate | Test A rank | Test B rank | $d$ | $d^{2}$ |
| --- | --- | --- | --- | --- |
| 1 | 1 | 2 | -1 | 1 |
| 2 | 2 | 1 | 1 | 1 |
| 3 | 3 | 3 | 0 | 0 |
| 4 | 4 | 5 | -1 | 1 |
| 5 | 5 | 4 | 1 | 1 |
| Total | | | | $\sum 4$ |

Step 4. Substitute into the formula with $n = 5$ and $\sum d^{2} = 4$.

$$
r_s = 1 - \frac{6\left(4\right)}{5\left(25 - 1\right)}
$$

Step 5. Evaluate the denominator.

$$
5\left(25 - 1\right) = 5 \times 24 = 120
$$

Step 6. Complete the calculation.

$$
r_s = 1 - \frac{24}{120} = 1 - 0.2 = 0.8
$$

Step 7. Interpret. A value of $0.8$ says the two orderings agree strongly but not exactly. Only the third candidate holds the same place in both rankings, and the remaining four are exchanged in two adjacent pairs, which is why the coefficient stops short of one.

Step 8. Compare with the product-moment coefficient computed on the raw marks, which is $r = 0.7696$ with square $0.5922$. The two measures agree about the direction and roughly about the strength. That is typical: ranks discard information about how far apart the raw values lie, so the two coefficients need not be equal.

## 5. Mathematical Extensions, Limits, and Common Errors

### 5.1 Mistakes beginners make

**Reading the sign backwards.** A negative coefficient does not mean a weak relationship. It means the two quantities move in opposite directions, and a value of $-0.9$ is a very strong relationship indeed. Strength is the size of the number; direction is the sign.

**Treating a zero coefficient as proof of no relationship.** A coefficient of zero rules out a straight track and nothing else. A curve, a cycle, or a threshold effect can all produce zero correlation while being perfectly deterministic.

**Confusing correlation with the slope.** The slope tells you how fast the predicted response changes per unit of the input, and it changes if either quantity is measured in different units. The correlation is unchanged by any change of units.

**Using the wrong line for a prediction.** Having fitted $Y = a + bX$, a student is sometimes asked to predict $X$. The right answer uses $X = c + dY$, not a rearrangement of the first line. Rearranging the first line gives the wrong answer because the two least squares fits minimise different gaps.

**Forgetting to square the rank differences.** The formula needs the sum of the *squares* of the differences. Summing the differences themselves gives zero whenever the two lists have the same mean rank, which is always the case for untied ranks.

**Ranking the two lists in opposite directions.** If one list is ranked from smallest to largest and the other from largest to smallest, the sign of the coefficient is reversed. Rank both lists the same way.

**Applying the untied formula when ties exist.** Repeated values mean repeated ranks, and the plain formula is then too small in size. The correction term must be added.

**Rounding too early.** Squaring amplifies small errors. Carry at least four significant figures through the intermediate stages, and round only the final answer.

### 5.2 Association is not the same thing as cause

The single most important limitation of the whole topic is that a correlation between two quantities does not show that one causes the other. Three alternatives must always be considered.

The first is **reverse causation**. If ice-cream sales and drowning deaths rise together, it may be that neither causes the other, and yet a naive reading suggests that eating ice cream is dangerous. The real explanation is a third quantity: hot weather drives both.

The second is a **common cause**, or lurking variable. A lurking variable is one that has not been measured but that influences both quantities of interest. The correlation between them is real, but the mechanism runs through the unmeasured quantity.

The third is plain **coincidence**, which becomes more likely as more pairs of quantities are examined. Two series that both drift upward over twenty years will correlate strongly even if they have nothing whatever to do with one another.

Only a controlled experiment, in which the input is varied deliberately while everything else is held fixed, can establish causation. An observational correlation, however strong, cannot.

### 5.3 Predicting outside the observed range

A fitted line is a summary of the data that were used to fit it, and it has no authority beyond them. Predicting at an input value far outside the observed range is called **extrapolation**, and it is dangerous for a simple reason: the straight track may bend once it leaves the region where dots were observed.

A line fitted to revision hours between $1$ and $6$ can say something sensible about $7$ hours. It cannot say anything trustworthy about $40$ hours, because nobody in the data set ever revised for $40$ hours. Marks are also bounded above, while a straight line is not, so the line will eventually predict impossible values. An extrapolated prediction should always be labelled as such, and it should never be reported as though it were an observation.

### 5.4 What the coefficient cannot see

The coefficient is blind to anything that is not a straight track. It is also easily distorted by a single unusual point: one dot placed far from the rest can move a coefficient from $0.2$ to $0.8$ on its own. A narrow range of input values depresses the coefficient even when the underlying relation is tight, because a short stretch of a straight track is hard to distinguish from noise. And when observations are averages over large groups rather than individuals, the coefficient computed between the averages is typically larger in size than the coefficient between individuals, a phenomenon known as the ecological effect.

### 5.5 The topic in one paragraph

Two quantities measured together can be described by a scatter diagram, summarised by a correlation coefficient, and used for prediction through a regression line. The coefficient $r$ lies between minus one and one, carries no units, is unchanged by a shift of origin or a positive change of scale, and has a square that reports the proportion of variation accounted for. The least squares line of $Y$ on $X$ and the line of $X$ on $Y$ are different lines that meet at the point of averages and whose slopes multiply to $r^{2}$. When only order is available, Spearman's coefficient compares rankings instead of values. None of these instruments, however carefully applied, can turn an association into a proof of cause.

### 5.6 Where this leads

The ideas here are the doorway to a great deal of later work. Once a residual has been defined, it becomes natural to ask whether the residuals are small enough to be explained by chance, and that question leads to tests of significance for a correlation coefficient and for a regression slope. Once one input has been handled, it becomes natural to ask about several inputs at once, and that leads to multiple regression, where the same least squares rule is applied with more than one explanatory quantity. The decomposition of total variation into explained and unexplained parts, used here in its simplest form, reappears as the analysis of variance. Throughout, the discipline is the same: describe first, then predict, and never confuse the two.
