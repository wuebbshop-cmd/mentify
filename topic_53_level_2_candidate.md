## 1. Purpose and Statistical Context

### 1.1 Estimating a difference between two population means

Many estimation problems compare two groups rather than estimate one population mean in isolation. Examples in the approved lesson include comparing petrol consumption for two additives and comparing measurements from two independent normal populations. The parameter of interest is the difference $\mu_1-\mu_2$, where $\mu_1$ is the mean in population 1 and $\mu_2$ is the mean in population 2.

Because the population means are unknown, use independent samples to estimate them. The point estimate of their difference is $\bar X_1-\bar X_2$. An interval estimate adds a lower and upper confidence limit to describe the sampling uncertainty in that estimate.

### 1.2 Learning goals

After this lesson, a learner should be able to:

- State the model assumptions for two independent normal samples.
- Construct a confidence interval for $\mu_1-\mu_2$ when the common variance is known.
- Construct a confidence interval when the populations have a common but unknown variance.
- Calculate and interpret the pooled sample variance and the standard error of the difference.
- Use the correct normal or Student's $t$ critical value and degrees of freedom.
- Preserve the order of the population difference when interpreting the sign of the interval.

## 2. Definitions and Assumptions

### 2.1 Two independent samples

Let $X_{11},\ldots,X_{1n_1}$ be a random sample of size $n_1$ from population 1, and let $X_{21},\ldots,X_{2n_2}$ be an independent random sample of size $n_2$ from population 2. The lesson models them as

$$
X_{1i}\sim N(\mu_1,\sigma^2),\qquad
X_{2j}\sim N(\mu_2,\sigma^2),
$$

with the two samples independent. In this lesson's pooled-variance case, the two populations share a common variance $\sigma^2$. Their means may differ.

Write

$$
\bar X_1=\frac{1}{n_1}\sum_{i=1}^{n_1}X_{1i},\qquad
\bar X_2=\frac{1}{n_2}\sum_{j=1}^{n_2}X_{2j}.
$$

The target is $\mu_1-\mu_2$, and the natural point estimate is $\bar X_1-\bar X_2$. The order matters: reversing the population labels changes the sign of the target and the interval center.

### 2.2 Difference of sample means

Independence gives

$$
E(\bar X_1-\bar X_2)=\mu_1-\mu_2.
$$

If the common variance $\sigma^2$ is known, the variance of the difference is

$$
\operatorname{Var}(\bar X_1-\bar X_2)
=\frac{\sigma^2}{n_1}+\frac{\sigma^2}{n_2}
=\sigma^2\left(\frac{1}{n_1}+\frac{1}{n_2}\right).
$$

Therefore its standard deviation is $\sigma\sqrt{1/n_1+1/n_2}$. When $\sigma^2$ is unknown, the common variance is estimated by pooling the two sample variances.

### 2.3 Confidence coefficient

For confidence coefficient $1-\alpha$, the interval procedure is designed to cover the fixed difference $\mu_1-\mu_2$ in a proportion $1-\alpha$ of repeated samples under the model. In an equal-tailed interval, the two tails each receive probability $\alpha/2$. This describes the long-run coverage of the procedure; it does not mean the fixed mean difference is random after the interval is computed.

## 3. Methods and Interpretation

### 3.1 Common variance known

When the two populations are independent and normal with the same known variance $\sigma^2$, the standardized difference

$$
Z=\frac{(\bar X_1-\bar X_2)-(\mu_1-\mu_2)}
{\sigma\sqrt{1/n_1+1/n_2}}
$$

has a standard normal distribution. Let $z_{\alpha/2}$ be the positive standard-normal critical value with upper-tail probability $\alpha/2$. Then

$$
P(-z_{\alpha/2}<Z<z_{\alpha/2})=1-\alpha.
$$

Rearranging for the unknown difference gives

$$
\boxed{(\bar x_1-\bar x_2)\pm z_{\alpha/2}\sigma
\sqrt{\frac{1}{n_1}+\frac{1}{n_2}}}.
$$

The center is the observed difference in sample means. The margin of error is the critical value multiplied by the standard error. If the population variances are equal and known, the common $\sigma$ is used in this standard error.

### 3.2 Common variance unknown: pooled $t$ interval

When the population variances are equal but their common value is unknown, estimate it by the pooled sample variance

$$
S_p^2=\frac{(n_1-1)S_1^2+(n_2-1)S_2^2}
{n_1+n_2-2}.
$$

Here $S_1^2$ and $S_2^2$ are the usual sample variances with denominators $n_1-1$ and $n_2-1$. The weights are the respective degrees of freedom, so this is not generally the simple average of the two variances. Let $S_p=\sqrt{S_p^2}$. Under independent normal sampling with a common variance,

$$
T=\frac{(\bar X_1-\bar X_2)-(\mu_1-\mu_2)}
{S_p\sqrt{1/n_1+1/n_2}}
$$

has Student's $t$ distribution with $n_1+n_2-2$ degrees of freedom. Therefore the confidence interval is

$$
\boxed{(\bar x_1-\bar x_2)\pm t_{\alpha/2,\,n_1+n_2-2}
S_p\sqrt{\frac{1}{n_1}+\frac{1}{n_2}}}.
$$

The degrees of freedom are the total sample size minus two because the two sample means are estimated. Keep the two tasks separate: first pool the variances, then calculate the standard error of the mean difference.

### 3.3 Interpreting the interval

If the interval is entirely above zero, it supports a positive difference $\mu_1-\mu_2$ at the corresponding two-sided confidence level. If it is entirely below zero, it supports a negative difference. If it contains zero, zero remains a plausible value for the difference under this procedure. That does not prove the means are equal; it means the interval does not establish a nonzero difference at that confidence level.

## 4. Worked Applications

### 4.1 Steel rods: common variance unknown

A verified assessment compares tensile strengths from two independent normal processes with a common but unknown variance. The sample summaries are

$$
n_1=10,\quad \bar x_1=72.5,\quad s_1^2=16,
\qquad n_2=12,\quad \bar x_2=68.0,\quad s_2^2=20.
$$

Construct a $95\%$ interval for $\mu_1-\mu_2$.

**Step 1: Identify the case and degrees of freedom.** The populations are independent normal populations with a common unknown variance, so use the pooled $t$ interval. The degrees of freedom are

$$
\nu=n_1+n_2-2=10+12-2=20.
$$

For a $95\%$ interval, $\alpha=0.05$ and $t_{0.025,20}=2.086$.

**Step 2: Calculate the pooled variance.**

$$
S_p^2=\frac{(10-1)(16)+(12-1)(20)}{20}
=\frac{144+220}{20}=18.2,
$$

so $S_p=\sqrt{18.2}\approx4.2661$.

**Step 3: Calculate the standard error.**

$$
SE=S_p\sqrt{\frac{1}{10}+\frac{1}{12}}
=\sqrt{18.2\left(\frac{1}{10}+\frac{1}{12}\right)}
\approx1.8267.
$$

**Step 4: Calculate the margin and interval.** The sample difference is $72.5-68.0=4.5$. The margin is

$$
ME=2.086(1.8267)\approx3.8105.
$$

Thus

$$
\mu_1-\mu_2\in4.5\pm3.8105
\approx(0.69,\;8.31).
$$

The interval is positive throughout, so it supports a higher mean tensile strength for process 1 than process 2 under the equal-variance model.

### 4.2 Petrol additives: lecture data and pooled interval

The lecture gives two independent groups of nine cars. Their measured consumption values, in miles per gallon, are

- Additive 1: $32.3,37.3,35.3,33.7,31.9,30.0,34.6,32.8,36.4$.
- Additive 2: $38.4,34.8,36.6,32.0,33.9,35.7,37.5,39.3,34.3$.

For this worked application, assume the two normal populations have a common unknown variance, as in the lesson's pooled case. Let population 1 refer to Additive 1 and population 2 to Additive 2.

**Step 1: Calculate sample summaries.**

$$
n_1=n_2=9,\qquad \bar x_1\approx33.8111,\qquad \bar x_2\approx35.8333,
$$

$$
s_1^2\approx5.4011,\qquad s_2^2=5.4800.
$$

The estimated difference is $\bar x_1-\bar x_2\approx-2.0222$ miles per gallon.

**Step 2: Pool the sample variances.**

$$
S_p^2=\frac{8(5.4011)+8(5.4800)}{16}\approx5.4406,
\qquad S_p\approx2.3325.
$$

**Step 3: Calculate the standard error and critical value.**

$$
SE=S_p\sqrt{\frac19+\frac19}\approx1.0996.
$$

The degrees of freedom are $9+9-2=16$. For a $95\%$ interval, $t_{0.025,16}\approx2.1199$.

**Step 4: Form and interpret the interval.**

$$
ME\approx2.1199(1.0996)\approx2.3310,
$$

$$
\mu_1-\mu_2\in-2.0222\pm2.3310
\approx(-4.3532,\;0.3087)\text{ miles per gallon}.
$$

The interval includes zero, so these data do not establish a nonzero difference in mean consumption at the 95% level under the assumed pooled model. The interval still reports the range of differences compatible with this procedure.

## 5. Revision Summary and Common Errors

### 5.1 Quick method selection

- **Common variance known:** use the standard-normal critical value and $\sigma\sqrt{1/n_1+1/n_2}$.
- **Common variance unknown:** calculate $S_p^2$, use $S_p\sqrt{1/n_1+1/n_2}$, and use $t$ with $n_1+n_2-2$ degrees of freedom.
- Keep the target order explicit. The interval is for $\mu_1-\mu_2$, not an unordered comparison.
- Interpret the sign and whether zero is inside the interval.

### 5.2 Common errors

- Using the pooled formula without stating the common-variance assumption.
- Reversing $\mu_1-\mu_2$ while leaving the sample difference as $\bar x_1-\bar x_2$.
- Averaging $s_1^2$ and $s_2^2$ without their degrees-of-freedom weights.
- Using $n_1+n_2-1$ or $n_1+n_2$ instead of $n_1+n_2-2$ for the pooled $t$ degrees of freedom.
- Forgetting to take the square root of $S_p^2$ before using $S_p$ in the standard error.
- Adding standard errors instead of variances inside $1/n_1+1/n_2$.
- Using $z$ when the common variance is unknown.
- Saying that an interval containing zero proves the means are equal.
- Interpreting a positive interval without defining which group is population 1 and which is population 2.
- Reporting more decimal places than the input summaries justify.''