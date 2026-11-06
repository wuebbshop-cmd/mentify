## 1. Purpose and Statistical Context

### 1.1 Why estimate with an interval?

A point estimate gives one sample-based value for an unknown population parameter. Because different random samples can produce different point estimates, a single number does not show the uncertainty caused by sampling. Interval estimation instead gives a lower and an upper confidence limit and a procedure designed to capture the fixed population parameter with a stated long-run frequency.

For a confidence coefficient $1-\alpha$, a $100(1-\alpha)\%$ confidence interval is constructed so that the procedure has coverage probability $1-\alpha$ under its assumptions. The interval endpoints are random before the sample is observed; after the data are collected, the endpoints are fixed. The confidence level describes the repeated-sampling performance of the procedure, not a probability that the already fixed parameter changes after the interval is computed.

This lesson assumes a normal population and treats four cases: a population mean with known variance, a population mean with unknown variance, a population variance with known mean, and a population variance with unknown mean. Correctly identifying which quantities are known is essential because it determines the pivot, critical-value distribution, and degrees of freedom.

### 1.2 Learning goals

By the end of this lesson, a learner should be able to:

- Explain confidence limits and the meaning of the confidence coefficient.
- Derive a confidence interval for a normal population mean when $\sigma^2$ is known.
- Derive the $t$-interval for a normal population mean when $\sigma^2$ is unknown.
- Construct a confidence interval for $\sigma^2$ when the population mean is known.
- Construct a confidence interval for $\sigma^2$ when the population mean is unknown.
- Choose the correct degrees of freedom and place chi-square critical values in the correct order.
- Interpret an interval in the context and units of the original parameter.

## 2. Definitions and Assumptions

### 2.1 Confidence coefficient and confidence limits

Let $\theta$ be a fixed unknown parameter and let $C_1$ and $C_2$ be sample-dependent endpoints. A two-sided interval procedure has confidence coefficient $1-\alpha$ when

$$
P_\theta(C_1<\theta<C_2)=1-\alpha.
$$

The value $\alpha$ is the probability assigned to the two tails combined. For an equal-tailed interval, each tail has probability $\alpha/2$. The lower and upper confidence limits are $C_1$ and $C_2$.

The correct interpretation is: if the same sampling procedure were repeated many times under the model, about $100(1-\alpha)\%$ of the intervals constructed this way would cover the fixed parameter. The interval is not a statement that $1-\alpha$ of individual population values lie between its endpoints; it concerns a parameter, not individual observations.

### 2.2 Normal-sample notation

Let $X_1,\ldots,X_n$ be an independent random sample from a normal population with mean $\mu$ and variance $\sigma^2$. Define

$$
\bar X=\frac{1}{n}\sum_{i=1}^{n}X_i,
\qquad
S^2=\frac{1}{n-1}\sum_{i=1}^{n}(X_i-\bar X)^2.
$$

Here $\bar X$ estimates the population mean and $S^2$ is the unbiased sample variance. The sample standard deviation is $S=\sqrt{S^2}$. Keep $S$ and $S^2$ distinct: mean intervals use a standard error, while variance intervals are built from a chi-square pivot involving a sum of squared deviations.

### 2.3 Assumptions

The formulas in this lesson require a random sample from a normal population. Observations must be independent and drawn from the same population. In the known-variance mean case, the value of $\sigma^2$ is supplied and treated as known. In the unknown-variance mean case, it is estimated using $S^2$. For the variance interval, the question must state whether $\mu$ is known or estimated from the sample; that choice changes the chi-square degrees of freedom.

## 3. Methods and Interpretation

### 3.1 Confidence interval for $\mu$ when $\sigma^2$ is known

For a normal sample,

$$
\bar X\sim N\!\left(\mu,\frac{\sigma^2}{n}\right).
$$

When $\sigma$ is known, the standardized variable

$$
Z=\frac{\bar X-\mu}{\sigma/\sqrt n}
$$

has the standard normal distribution. Let $z_{\alpha/2}$ denote the positive critical value with upper-tail probability $\alpha/2$, so that $P(-z_{\alpha/2}<Z<z_{\alpha/2})=1-\alpha$. Rearranging gives

$$
\boxed{\bar x\pm z_{\alpha/2}\frac{\sigma}{\sqrt n}}.
$$

The standard error is $\sigma/\sqrt n$, and the margin of error is $z_{\alpha/2}\sigma/\sqrt n$. Increasing $n$ reduces this margin; increasing the confidence level increases the critical value and widens the interval.

### 3.2 Confidence interval for $\mu$ when $\sigma^2$ is unknown

When the variance is unknown, estimate it with

$$
S^2=\frac{1}{n-1}\sum_{i=1}^{n}(X_i-\bar X)^2.
$$

For an independent normal sample, the pivot

$$
T=\frac{\bar X-\mu}{S/\sqrt n}
$$

has Student's $t$ distribution with $n-1$ degrees of freedom. If $t_{\alpha/2,n-1}$ is the positive upper-tail critical value, rearranging the central probability statement gives

$$
\boxed{\bar x\pm t_{\alpha/2,n-1}\frac{s}{\sqrt n}}.
$$

Use the $t$ distribution because replacing the known $\sigma$ with the estimated $S$ adds uncertainty. Under the normal model this is the exact finite-sample interval. The degrees of freedom are $n-1$ because the sample mean is estimated from the same observations when computing $S^2$.

### 3.3 Confidence interval for $\sigma^2$ when $\mu$ is known

If $\mu$ is known, the normal-sample pivot is

$$
Q=\frac{\sum_{i=1}^{n}(X_i-\mu)^2}{\sigma^2}\sim\chi^2_n.
$$

Let $q_{p,n}$ denote the lower-tail $p$ quantile of a chi-square distribution with $n$ degrees of freedom. Then

$$
P\!\left(q_{\alpha/2,n}<Q<q_{1-\alpha/2,n}\right)=1-\alpha.
$$

Solving the inequalities for $\sigma^2$ reverses the order of the denominators:

$$
\boxed{\left[\frac{\sum_{i=1}^{n}(x_i-\mu)^2}{q_{1-\alpha/2,n}},\;
\frac{\sum_{i=1}^{n}(x_i-\mu)^2}{q_{\alpha/2,n}}\right]}.
$$

The upper-tail quantile notation often used in tables writes the same limits with the larger chi-square critical value in the lower endpoint's denominator and the smaller critical value in the upper endpoint's denominator. Always state which quantile convention is being used.

### 3.4 Confidence interval for $\sigma^2$ when $\mu$ is unknown

When $\mu$ is unknown, estimate it by $\bar X$. The normal-sample pivot is

$$
Q=\frac{(n-1)S^2}{\sigma^2}
=\frac{\sum_{i=1}^{n}(X_i-\bar X)^2}{\sigma^2}\sim\chi^2_{n-1}.
$$

The resulting interval is

$$
\boxed{\left[\frac{(n-1)s^2}{q_{1-\alpha/2,n-1}},\;
\frac{(n-1)s^2}{q_{\alpha/2,n-1}}\right]}.
$$

The degrees of freedom are $n-1$, rather than $n$, because one degree of freedom is used to estimate $\mu$. The interval is generally asymmetric around $s^2$ because the chi-square distribution is not symmetric.

### 3.5 Decision table for choosing the pivot

| Target | Known quantity | Pivot distribution | Degrees of freedom |
|---|---|---|---|
| $\mu$ | $\sigma^2$ known | Standard normal $Z$ | Not applicable |
| $\mu$ | $\sigma^2$ unknown | Student's $t$ | $n-1$ |
| $\sigma^2$ | $\mu$ known | Chi-square | $n$ |
| $\sigma^2$ | $\mu$ unknown | Chi-square | $n-1$ |

Use the row that matches the actual assumptions in the question. Do not select a pivot from the sample size or confidence level alone.

## 4. Worked Applications

### 4.1 Known variance: steel-rod mean

A sample of $n=25$ steel rods has sample mean $\bar x=10.02$ mm. The population standard deviation is known to be $\sigma=0.05$ mm. Construct a $95\%$ confidence interval for $\mu$.

**Step 1: Choose the pivot.** The population is normal and $\sigma$ is known, so use the standard-normal interval. Here $\alpha=0.05$ and $z_{0.025}=1.96$.

**Step 2: Calculate the standard error.**

$$
\frac{\sigma}{\sqrt n}=\frac{0.05}{\sqrt{25}}=0.01\text{ mm}.
$$

**Step 3: Calculate the margin of error.**

$$
1.96(0.01)=0.0196\text{ mm}.
$$

**Step 4: State the interval.**

$$
10.02\pm0.0196=(10.0004,\;10.0396)\text{ mm}.
$$

The interval is in millimetres because both the sample mean and standard error are in millimetres.

### 4.2 Unknown variance: lecture's muzzle-velocity sample

The lecture gives eight muzzle velocities in metres per second:

$$
3005,\;2925,\;2935,\;2965,\;2995,\;3005,\;2937,\;2905.
$$

For a $95\%$ interval, the source reports $\bar x=2959$, $s=39.1$, $n=8$, and $t_{0.025,7}=2.365$.

**Step 1: Choose the pivot.** The variance is unknown and the population is assumed normal, so use $t$ with $n-1=7$ degrees of freedom.

**Step 2: Calculate the standard error.**

$$
\frac{s}{\sqrt n}=\frac{39.1}{\sqrt8}\approx13.824.
$$

**Step 3: Calculate the margin.**

$$
2.365\frac{39.1}{\sqrt8}\approx32.69.
$$

**Step 4: Form and interpret the interval.**

$$
2959\pm32.69=(2926.31,\;2991.69)\text{ metres per second}.
$$

This agrees, to rounding, with the lecture's limits $2926.3$ and $2991.7$.

### 4.3 Variance with known mean: lecture's sample

The lecture gives nine observations $8.6,7.9,8.3,6.4,8.4,9.8,7.2,7.8,7.5$, from a normal population with known mean $\mu=8$. It reports

$$
\sum_{i=1}^{9}(x_i-8)^2=7.35.
$$

For a $95\%$ interval, the chi-square degrees of freedom are $n=9$. Using the lecture's critical values $q_{0.025,9}=2.70$ and $q_{0.975,9}=19.02$ (lower-tail quantile convention),

$$
\sigma^2\in\left[\frac{7.35}{19.02},\;\frac{7.35}{2.70}\right]
\approx(0.386,\;2.722).
$$

The larger chi-square quantile is in the lower endpoint denominator; the smaller quantile is in the upper endpoint denominator.

### 4.4 Variance with unknown mean: same lecture sample

For the same nine observations, now suppose $\mu$ is unknown. The source gives $\bar x\approx7.99$, $s^2\approx7.349$, and $n=9$. The degrees of freedom are $n-1=8$, and the lecture's lower-tail critical values are $q_{0.025,8}=2.18$ and $q_{0.975,8}=17.53$.

The numerator is

$$
(n-1)s^2=8(7.349)=58.792.
$$

Therefore

$$
\sigma^2\in\left[\frac{58.792}{17.53},\;\frac{58.792}{2.18}\right]
\approx(3.354,\;26.969).
$$

Compared with the known-mean case, estimating $\mu$ reduces the degrees of freedom from $9$ to $8$.

### 4.5 Assessment check: known variance and an unknown-mean variance interval

An assessment gives $n=25$, $\sum x_i=3700$, $\sum x_i^2=573000$, and a known population variance $\sigma^2=800$. The sample mean is

$$
\bar x=\frac{3700}{25}=148.
$$

For a $98\%$ confidence interval with known variance, $\alpha=0.02$, $z_{0.01}\approx2.32635$, and the standard error is

$$
\sqrt{\frac{800}{25}}=\sqrt{32}\approx5.657.
$$

Thus

$$
148\pm2.32635\sqrt{32}\approx(134.840,\;161.160).
$$

If the same sample is used for a variance interval with unknown mean, first calculate

$$
s^2=\frac{\sum x_i^2-(\sum x_i)^2/n}{n-1}
=\frac{573000-3700^2/25}{24}
=\frac{25400}{24}\approx1058.333.
$$

For a $98\%$ interval, the lower-tail chi-square quantiles with $24$ degrees of freedom are approximately $q_{0.01,24}=10.8564$ and $q_{0.99,24}=42.9798$. Hence

$$
\sigma^2\in\left[\frac{24s^2}{42.9798},\;\frac{24s^2}{10.8564}\right]
\approx(590.975,\;2339.642).
$$

This second calculation uses $n-1=24$ degrees of freedom because the mean is estimated from the sample.

## 5. Revision Summary and Common Errors

### 5.1 Formula and choice checklist

1. Identify whether the target is $\mu$ or $\sigma^2$.
2. Record whether $\sigma^2$ and $\mu$ are known or unknown.
3. For $\mu$ with known $\sigma$, use $z$ and standard error $\sigma/\sqrt n$.
4. For $\mu$ with unknown $\sigma$, use $t_{n-1}$ and $s/\sqrt n$.
5. For $\sigma^2$ with known $\mu$, use $\sum(X_i-\mu)^2$ and chi-square with $n$ degrees of freedom.
6. For $\sigma^2$ with unknown $\mu$, use $(n-1)S^2$ and chi-square with $n-1$ degrees of freedom.
7. Check the critical-value convention and put the larger chi-square quantile in the denominator of the lower limit.
8. State the interval in the target parameter's units and interpret it in the problem context.

### 5.2 Common errors

- Saying the parameter itself has probability $1-\alpha$ of being inside the already calculated interval; the confidence statement describes the repeated-sampling procedure.
- Using a $z$ critical value when $\sigma^2$ is unknown instead of the $t$ pivot required by the normal model.
- Using $n$ rather than $n-1$ degrees of freedom for the unknown-mean variance interval.
- Using $n-1$ rather than $n$ when the population mean is known and the sum of squared deviations is taken from that known value.
- Reversing the chi-square denominators and obtaining a lower endpoint larger than the upper endpoint.
- Forgetting to square or square-root the appropriate quantity: mean intervals use a standard deviation in the standard error, while the variance interval estimates $\sigma^2$ directly.
- Confusing the confidence coefficient $1-\alpha$ with the tail probability $\alpha/2$.
- Reporting an interval without its units or without stating which population parameter it estimates.
- Using a sample-variance formula with denominator $n$ when the source's unbiased sample variance uses denominator $n-1$.''