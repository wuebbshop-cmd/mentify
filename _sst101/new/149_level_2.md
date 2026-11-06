## 1. Foundational Concepts, Definitions, and Axioms

### 1.1 The inferential problem stated exactly

Statistical inference begins with an asymmetry. The population is fixed but invisible; the sample is visible but random. A parameter is a functional of the population distribution, written $\theta$, and it does not move. A statistic is a function of the sample that contains no unknown quantities, and it moves with every repetition of the sampling. Estimation is the attempt to learn $\theta$ from a statistic, and the theory of estimation is the study of how well that attempt can succeed.

Three objects must be distinguished with care, because later formulas depend on which one is meant.

The population distribution is the probability law of a single observation drawn at random from the population. Its mean $\mu$ and variance $\sigma^{2}$ are parameters, and statements such as $\text{E}(x_i) = \mu$ and $\text{Var}(x_i) = \sigma^{2}$ refer to that law.

The sample is a vector $\left(x_1, x_2, \dots, x_n\right)$ of random variables. Before the data are collected each $x_i$ is a random variable; after collection each is a number. A statistic inherits randomness from the sample, and every probability statement in this topic is a statement about the statistic before it is observed.

The sampling distribution of a statistic is its probability distribution over all samples of size $n$. The standard error is the standard deviation of that distribution. Everything that follows is a consequence of knowing, or approximating, the sampling distribution.

> **Definition (Random sample).** A random sample of size $n$ is a vector of independent random variables $x_1, \dots, x_n$, each having the same distribution as the population.

Independence and identical distribution are separate assumptions and both are used. Independence is needed for variances to add; identical distribution is needed for the common mean and variance to be the population values. Random sampling without replacement produces dependence, which is precisely why the finite population correction appears later.

### 1.2 Estimators, estimates and the sampling distribution

An estimator is a rule, decided before the data arrive, for converting a sample into a guess. An estimate is the number the rule produces once the data have arrived. The estimator is random and has a distribution; the estimate is fixed and has none.

> **Definition (Point estimator and point estimate).** A point estimator $\hat{\theta}$ is a statistic used to estimate a parameter $\theta$. A point estimate is the numerical value of $\hat{\theta}$ computed from a realised sample.

The distinction has real consequences. It makes sense to ask for the variance of an estimator, because an estimator is a random variable. It does not make sense to ask for the variance of an estimate. When a textbook writes $\text{Var}(\bar{x}) = \sigma^{2}/n$ it is describing the estimator; when it writes $\bar{x} = 252$ it is reporting an estimate.

Standard estimators are few and are worth stating as a body of convention.

> **Definition (Standard point estimators).** For a random sample of size $n$, the sample mean $\bar{x}$, the sample variance $s^{2}$ and the sample proportion $\hat{p}$ are defined by

$$
\bar{x} = \frac{1}{n}\sum_{i=1}^{n} x_i, \qquad s^{2} = \frac{1}{n-1}\sum_{i=1}^{n}\left(x_i - \bar{x}\right)^{2}, \qquad \hat{p} = \frac{X}{n},
$$

where $X$ is the number of successes and $\hat{p}$ estimates the population proportion $p$.

The three formulas are not arbitrary. The first two are the sufficient statistics of a normal sample, a fact proved in Section 2.5. The third is the mean of a variable coded one for success and zero for failure, so it inherits the theory of the sample mean.

### 1.3 Interval estimation

A point estimator answers "what value?" and says nothing about its own accuracy. An interval estimator answers "which values are consistent with the data?" and in doing so reports the accuracy explicitly.

> **Definition (Interval estimator).** An interval estimator is a pair of statistics $\left(L, U\right)$ with $L \le U$, computed from the sample, such that the random interval $\left[L, U\right]$ is claimed to contain $\theta$ with a stated probability.

> **Definition (Confidence interval).** A confidence interval for $\theta$ with confidence level $1 - \alpha$ is a realised pair $\left(l, u\right)$ produced by a procedure satisfying

$$
\text{P}_{\theta}\left(L \le \theta \le U\right) = 1 - \alpha \quad \text{for every } \theta .
$$

The subscript on the probability symbol records that the probability is computed under the true parameter value, and the phrase "for every $\theta$" is what makes the guarantee uniform. A procedure that covered the parameter $95\%$ of the time for some values and $60\%$ of the time for others would not deserve the name.

The familiar structure follows from the definition. Every interval in this topic has the form

$$
\text{estimate} \pm \text{multiplier} \times \text{standard error} ,
$$

in which the multiplier is a quantile of the sampling distribution of a standardised statistic and the standard error is the standard deviation of the estimator. Writing the margin of error as $E$ and the width as $W$,

$$
E = z_{\alpha/2}\,\text{SE}, \qquad W = 2E .
$$

### 1.4 The confidence level as a coverage probability

The confidence level is a property of the procedure and is identical to the coverage probability of the random interval.

> **Definition (Confidence level and coverage).** The confidence level of an interval procedure is the probability $1 - \alpha$ that the random interval covers $\theta$. The error rate $\alpha$ is split between the two tails in a two-sided procedure, so that $\text{P}\left(\theta < L\right) = \alpha/2$ and $\text{P}\left(\theta > U\right) = \alpha/2$.

Two consequences follow formally. First, the realised interval has no probability attached to it: once $\left(l, u\right)$ is computed, the event $\left\{l \le \theta \le u\right\}$ is deterministic and its probability is either zero or one. Second, the coverage statement concerns the joint distribution of $\left(L, U\right)$, not the conditional distribution of $\theta$ given the data. A statement of the latter kind requires a prior distribution and belongs to Bayesian inference, where the credible interval is a genuinely different object even when its endpoints coincide numerically.

### 1.5 Pivotal quantities

Every interval in this topic is obtained by inverting a pivot, and the pivot is worth isolating as a concept because it explains why some intervals use the normal curve and others use the t curve.

> **Definition (Pivot).** A pivot is a function $Q\left(x_1, \dots, x_n; \theta\right)$ of the sample and the parameter whose distribution does not depend on $\theta$ or on any other unknown parameter.

A pivot converts a probability statement about a known distribution into a probability statement about the unknown parameter. If $Q$ has a distribution free of unknowns, then for any $\alpha$ a number $q$ can be found with $\text{P}\left(-q \le Q \le q\right) = 1 - \alpha$, and the inequality can be solved for $\theta$. The interval is exactly the solution set.

For a normal sample with known variance the pivot is $\left(\bar{x} - \mu\right)/\left(\sigma/\sqrt{n}\right)$, which is standard normal. For a normal sample with unknown variance the pivot is $\left(\bar{x} - \mu\right)/\left(s/\sqrt{n}\right)$, which is t distributed with $n-1$ degrees of freedom. For a proportion the pivot is approximately standard normal. The three intervals of the topic are therefore three applications of one idea.

### 1.6 Properties of estimators

Four properties are used to rank estimators. Each is a statement about the sampling distribution, and each answers a different question.

> **Definition (Unbiasedness).** An estimator $\hat{\theta}$ is unbiased for $\theta$ if $\text{E}(\hat{\theta}) = \theta$ for every admissible $\theta$. The bias is $\text{B}(\hat{\theta}) = \text{E}(\hat{\theta}) - \theta$.

Unbiasedness says the estimator has no systematic lean. It does not say the estimator is accurate on any single sample: an unbiased estimator can have an enormous variance and be almost always far from the truth. The mean squared error combines both defects,

$$
\text{MSE}(\hat{\theta}) = \text{Var}(\hat{\theta}) + \left[\text{B}(\hat{\theta})\right]^{2} ,
$$

and is the quantity that a decision-theoretic comparison would minimise. A slightly biased estimator with a much smaller variance can beat an unbiased one on this criterion, which is why shrinkage estimators exist.

> **Definition (Efficiency).** Among unbiased estimators of $\theta$, the one with the smallest variance is called efficient. The relative efficiency of two unbiased estimators $\hat{\theta}_1$ and $\hat{\theta}_2$ is the ratio $\text{Var}(\hat{\theta}_1)/\text{Var}(\hat{\theta}_2)$.

Efficiency is a comparative notion unless a lower bound on variance is available. The Cramér–Rao bound supplies that bound, and an estimator attaining it is efficient in the absolute sense.

> **Definition (Consistency).** An estimator $\hat{\theta}_n$ is consistent for $\theta$ if $\hat{\theta}_n \to \theta$ in probability as $n \to \infty$, that is, if for every $\varepsilon > 0$,

$$
\text{P}\left(\left|\hat{\theta}_n - \theta\right| > \varepsilon\right) \to 0 .
$$

Consistency is a large-sample property and says nothing about any fixed $n$. A consistent estimator may be badly biased at every finite sample size; consistency constrains only the limit. Conversely an unbiased estimator may fail to be consistent if its variance does not shrink.

> **Definition (Sufficiency).** A statistic $T$ is sufficient for $\theta$ if the conditional distribution of the sample given $T$ does not depend on $\theta$.

Sufficiency says that $T$ exhausts the information about $\theta$ carried by the sample. Once $T$ is known, further inspection of the individual observations yields no additional information about the parameter. It is the strongest of the four properties, and it is checked in practice by the factorisation criterion of Section 2.5.

### 1.7 The sampling distribution of the mean

> **Theorem (Mean and variance of the sample mean).** For a random sample with $\text{E}(x_i) = \mu$ and $\text{Var}(x_i) = \sigma^{2}$,

$$
\text{E}(\bar{x}) = \mu, \qquad \text{Var}(\bar{x}) = \frac{\sigma^{2}}{n}, \qquad \text{SE}(\bar{x}) = \frac{\sigma}{\sqrt{n}} .
$$

The standard error is the operational content of the second identity. It is the yardstick against which the distance between $\bar{x}$ and $\mu$ is measured, and it is what turns a raw difference in grams into a dimensionless number of standard errors that a table can interpret.

When $\sigma$ is unknown, the estimated standard error substitutes $s$:

$$
\widehat{\text{SE}}(\bar{x}) = \frac{s}{\sqrt{n}} .
$$

The substitution is not innocent. It changes the sampling distribution of the standardised statistic from normal to t, and the change is material for small $n$.

### 1.8 The standard error of a proportion

A proportion is the mean of a zero-one variable. Coding a success as one and a failure as zero, the population mean of the coded variable is $p$ and its variance is $p(1-p)$. The mean and variance formulas for $\bar{x}$ therefore apply without modification.

> **Theorem (Standard error of a sample proportion).** For $X$ successes in $n$ independent trials,

$$
\text{E}(\hat{p}) = p, \qquad \text{Var}(\hat{p}) = \frac{p(1-p)}{n}, \qquad \text{SE}(\hat{p}) = \sqrt{\frac{p(1-p)}{n}} .
$$

The variance depends on the unknown $p$, which is the source of every difficulty in the proportion case. Estimating it by substituting $\hat{p}$ gives the estimated standard error used in the Wald interval, and the substitution is what makes the Wald interval approximate rather than exact.

### 1.9 The central limit theorem and its licensing role

> **Theorem (Lindeberg–Lévy central limit theorem).** Let $x_1, \dots, x_n$ be independent and identically distributed with mean $\mu$ and finite variance $\sigma^{2}$. Then

$$
\frac{\sqrt{n}\left(\bar{x} - \mu\right)}{\sigma} \to Z \sim \text{N}\left(0, 1\right)
$$

in distribution as $n \to \infty$.

The theorem is what allows normal-based intervals to be applied to data that are not normal. Its hypotheses are weak: independence, identical distribution and a finite variance. No assumption is made about symmetry or about the shape of the population density.

The theorem also explains why the normal interval is only approximate at moderate $n$. The rate of convergence depends on the skewness and kurtosis of the population. For a symmetric population the approximation is good at $n = 15$; for a strongly skewed population such as an exponential, $n$ of fifty or more may be needed for the tails to be accurate at the $99\%$ level.

### 1.10 Standing assumptions

The assumptions used throughout are gathered here so that they can be checked against any question.

| Assumption | What it buys | Where it is used |
| --- | --- | --- |
| Random sampling | every unit has a known selection probability | coverage statements |
| Independence | variances add | $\text{Var}(\bar{x}) = \sigma^{2}/n$ |
| Finite variance | the central limit theorem applies | normal approximation |
| Known $\sigma$ | the pivot is standard normal | $z$ interval |
| Normal population | the pivot is exactly t | $t$ interval |
| Large $n$ | $\hat{p}$ is approximately normal | Wald and Wilson intervals |

Each assumption is load-bearing, and dropping one breaks a specific result rather than the whole edifice. Independence can be replaced by a known covariance structure, which is exactly what the finite population correction does. Normality can be replaced by a large sample, which is exactly what the central limit theorem does. Neither substitution is free, and both are recorded in the formulas as conditional factors.

### 1.11 Notation

| Symbol | Meaning |
| --- | --- |
| $\theta$ | generic parameter |
| $\hat{\theta}$ | generic estimator |
| $1 - \alpha$ | confidence level |
| $z_{\alpha/2}$ | standard normal upper $\alpha/2$ point |
| $t_{\alpha/2,\,n-1}$ | t upper $\alpha/2$ point on $n-1$ degrees of freedom |
| $E$ | margin of error, the half-width |
| $N$ | finite population size |

## 2. Theorems, Lemmas, and Analytical Properties

### 2.1 Unbiasedness of the sample mean

> **Theorem.** For a random sample of any size $n$ from a population with finite mean $\mu$, the sample mean is unbiased: $\text{E}(\bar{x}) = \mu$.

The proof needs only linearity of expectation, and it is given in Section 3.1. Unbiasedness holds at every $n$, including $n = 1$, and it holds whether or not the population is symmetric, because linearity of expectation requires no distributional assumption at all.

### 2.2 The variance of the sample mean

> **Theorem.** For independent observations with common variance $\sigma^{2}$, $\text{Var}(\bar{x}) = \sigma^{2}/n$. If the sample is drawn without replacement from a finite population of size $N$, then

$$
\text{Var}(\bar{x}) = \frac{\sigma^{2}}{n}\cdot\frac{N-n}{N-1} .
$$

The independent case is proved by the additivity of variance, which requires zero covariance between distinct observations. Sampling without replacement destroys that independence, because the units remaining in the population after the first draw are no longer representative of the whole, and the resulting negative covariance is exactly what produces the correction factor.

> **Corollary (Standard error of the mean).** Taking square roots,

$$
\text{SE}(\bar{x}) = \frac{\sigma}{\sqrt{n}}\sqrt{\frac{N-n}{N-1}} .
$$

The correction factor equals one when $N$ is infinite and equals zero when $n = N$. It is monotonically decreasing in $n/N$, so the larger the fraction sampled the greater the gain from the correction.

### 2.3 The sample variance and its bias

> **Theorem.** For a random sample of size $n \ge 2$ with variance $\sigma^{2}$, the estimator $s^{2}$ with divisor $n-1$ is unbiased: $\text{E}(s^{2}) = \sigma^{2}$.

The proof is in Section 3.3. Two companion facts are worth recording. First, the naive estimator with divisor $n$ has expectation $\left(n-1\right)\sigma^{2}/n$, so its bias is $-\sigma^{2}/n$, negative and vanishing only as $n$ grows. Second, the sample standard deviation $s$ is not unbiased for $\sigma$: by Jensen's inequality applied to the concave square root, $\text{E}(s) < \sigma$. The bias in $s$ is small for moderate $n$ and is usually ignored, but it is real.

### 2.4 Consistency of the sample mean

> **Theorem.** If $\text{Var}(x_i) = \sigma^{2} < \infty$, then $\bar{x}$ is a consistent estimator of $\mu$.

The proof uses Chebyshev's inequality, which for any $\varepsilon > 0$ gives

$$
\text{P}\left(\left|\bar{x} - \mu\right| \ge \varepsilon\right) \le \frac{\text{Var}(\bar{x})}{\varepsilon^{2}} = \frac{\sigma^{2}}{n\varepsilon^{2}} \to 0 .
$$

The bound is crude numerically: it would require $n$ in the thousands to certify a two-standard-error accuracy. Its purpose is qualitative, and qualitatively it is decisive, because the right-hand side tends to zero for every fixed $\varepsilon$.

Consistency is not implied by unbiasedness alone. An estimator with mean $\theta$ and variance growing with $n$ would be unbiased and inconsistent. What the argument uses is that the variance shrinks, which is a consequence of averaging independent observations rather than of unbiasedness.

### 2.5 Sufficiency of the normal sample statistics

> **Theorem (Factorisation criterion).** A statistic $T$ is sufficient for $\theta$ if and only if the joint density factors as

$$
f\left(x_1, \dots, x_n; \theta\right) = g\left(T; \theta\right) h\left(x_1, \dots, x_n\right)
$$

for functions $g$ and $h$ with $h$ free of $\theta$.

> **Theorem (Sufficiency for the normal family).** For a normal sample, the pair $\left(\bar{x}, s^{2}\right)$ is jointly sufficient for $\left(\mu, \sigma^{2}\right)$.

The verification is a single algebraic identity. Writing the sum of squares about $\mu$ as a sum about $\bar{x}$ plus $n$ times the squared distance from $\bar{x}$ to $\mu$,

$$
\sum_{i=1}^{n}\left(x_i - \mu\right)^{2} = \sum_{i=1}^{n}\left(x_i - \bar{x}\right)^{2} + n\left(\bar{x} - \mu\right)^{2},
$$

the likelihood becomes

$$
L\left(\mu, \sigma^{2}\right) = \left(2\pi\sigma^{2}\right)^{-n/2}\exp\left\{-\frac{\left(n-1\right)s^{2} + n\left(\bar{x} - \mu\right)^{2}}{2\sigma^{2}}\right\},
$$

which depends on the data only through $\bar{x}$ and $s^{2}$. The factorisation criterion is satisfied with $h \equiv 1$. No other feature of the sample — the order of the observations, their spread about the mean beyond $s^{2}$, the presence of outliers — carries additional information about $\mu$ and $\sigma^{2}$ under normality. This is the formal reason the whole topic is built on two numbers.

### 2.6 Efficiency and the Cramér–Rao bound

> **Theorem (Cramér–Rao inequality).** Under regularity conditions, any unbiased estimator $\hat{\theta}$ satisfies

$$
\text{Var}(\hat{\theta}) \ge \frac{1}{n\,I_1\left(\theta\right)},
$$

where $I_1\left(\theta\right)$ is the Fisher information in a single observation.

> **Corollary.** For a normal population with known $\sigma^{2}$, the sample mean attains the bound, since $I_1\left(\mu\right) = 1/\sigma^{2}$ and hence the bound is $\sigma^{2}/n$.

The sample mean is therefore efficient, not merely unbiased. The median is also unbiased for a symmetric population but is less efficient: for normal data its asymptotic variance is $\pi\sigma^{2}/\left(2n\right)$, giving an asymptotic relative efficiency of

$$
\text{ARE}\left(\text{median}, \text{mean}\right) = \frac{2}{\pi} \approx 0.6366 .
$$

The median would need about $\pi/2 \approx 1.571$ times as many observations as the mean to achieve the same precision. The comparison reverses for heavy-tailed populations, where the median can be far more efficient, which is the standard argument for robust location estimators.

### 2.7 The t pivot

> **Theorem (Student's t).** Let $x_1, \dots, x_n$ be a random sample from a normal population with mean $\mu$. Then

$$
T = \frac{\bar{x} - \mu}{s/\sqrt{n}}
$$

has a t distribution with $n-1$ degrees of freedom.

The result requires two ingredients: that $\bar{x}$ and $s^{2}$ are independent, which is a special property of the normal family, and that $\left(n-1\right)s^{2}/\sigma^{2}$ is chi-squared with $n-1$ degrees of freedom. Writing

$$
T = \frac{Z}{\sqrt{V/\nu}}, \qquad Z = \frac{\bar{x} - \mu}{\sigma/\sqrt{n}}, \qquad V = \frac{\left(n-1\right)s^{2}}{\sigma^{2}}, \qquad \nu = n-1,
$$

exhibits $T$ in the defining form of a t variable. The unknown $\sigma$ cancels between numerator and denominator, which is exactly why the statistic is a pivot.

The density of the t distribution is symmetric and bell shaped with heavier tails than the normal, and it converges to the standard normal as $\nu \to \infty$. Heavier tails mean larger quantiles, so intervals built with $t$ are wider than those built with $z$ at the same confidence level.

### 2.8 Inversion of the pivot as the source of the interval

> **Theorem (Pivot inversion).** If $Q\left(\theta\right)$ is a pivot and $q_1, q_2$ satisfy $\text{P}\left(q_1 \le Q \le q_2\right) = 1 - \alpha$, then the set

$$
\left\{\theta : q_1 \le Q\left(\theta\right) \le q_2\right\}
$$

is a confidence set with level $1 - \alpha$.

For the normal mean with known variance the set is an interval because $Q$ is monotone decreasing in $\mu$. The same monotonicity holds in the unknown-variance case. The resulting intervals are exactly the ones derived step by step in Section 3.

### 2.9 The Wald and Wilson intervals as two inversions

Both interval forms for a proportion come from the same pivot,

$$
Z = \frac{\hat{p} - p}{\sqrt{p(1-p)/n}},
$$

and differ in how the inequality is solved.

> **Theorem (Wald interval).** Replacing $p$ by $\hat{p}$ inside the standard error and inverting gives

$$
\hat{p} \pm z_{\alpha/2}\sqrt{\frac{\hat{p}(1-\hat{p})}{n}} .
$$

> **Theorem (Wilson interval).** Solving the quadratic inequality in $p$ exactly gives the endpoints

$$
\frac{n\hat{p} + \frac{z^{2}}{2} \pm z\sqrt{n\hat{p}\left(1-\hat{p}\right) + \frac{z^{2}}{4}}}{n + z^{2}} ,
$$

where $z = z_{\alpha/2}$.

The Wald form is a linear approximation to the Wilson form, obtained by treating the standard error as constant in $p$. The approximation is excellent when $\hat{p}$ is near one half and $n$ is large, and it fails badly when $\hat{p}$ is near zero or one, where the standard error varies rapidly and the Wald limits can leave the parameter space.

Two structural properties of the Wilson interval follow directly from its formula. Its centre is a weighted average of $\hat{p}$ and one half, with weights $n$ and $z^{2}$, so it is pulled towards one half, and the pull is strong for small $n$. Its half-width is smaller than the Wald half-width divided by the same inflation factor, and the net effect keeps the limits inside the unit interval.

### 2.10 Width, elasticity, and the three levers

> **Theorem (Width elasticities).** For the known-variance interval for a mean,

$$
W = 2\,z_{\alpha/2}\frac{\sigma}{\sqrt{n}}, \qquad \frac{\partial W}{\partial n}\cdot\frac{n}{W} = -\frac{1}{2}, \qquad \frac{\partial W}{\partial \sigma}\cdot\frac{\sigma}{W} = 1 .
$$

The elasticities are the cleanest statement of the trade-offs. The width is unit-elastic in the standard deviation: a ten per cent increase in variability produces a ten per cent increase in width. It is half-elastic in the sample size: a ten per cent increase in the sample buys only a five per cent reduction in width, so halving the width requires quadrupling the sample.

The confidence level enters through the multiplier, and its effect is best read from the multipliers themselves: $1.645$, $1.960$ and $2.576$ for $90\%$, $95\%$ and $99\%$. Moving from $95\%$ to $99\%$ multiplies the width by $2.576/1.960 \approx 1.314$, a thirty-one per cent increase. Moving from $95\%$ to $90\%$ multiplies it by $0.839$, a sixteen per cent reduction.

For a proportion the width is $2z\sqrt{\hat{p}(1-\hat{p})/n}$, whose variability factor is largest at $\hat{p} = 0.5$ and tends to zero at the boundaries. This gives the useful rule that an interval for a proportion near one half is the most expensive to narrow.

### 2.11 Duality with hypothesis tests

> **Theorem (Interval–test duality).** Let $C$ be the confidence set of level $1-\alpha$ obtained by inverting a pivot $Q\left(\theta\right)$, and for a hypothesised value $\theta_0$ let the test reject when $Q\left(\theta_0\right)$ falls outside the central $1-\alpha$ region. Then $\theta_0 \in C$ if and only if the test does not reject $\theta_0$.

The proof is a restatement: both statements assert the same inequality. The practical value is large. A single interval answers every two-sided question about the parameter at that level, because membership in the interval is equivalent to non-rejection. An examination candidate who has already computed a $95\%$ interval can answer a question about a $5\%$ test without further arithmetic, and vice versa.

The duality fails in one respect worth knowing. Interval and test duality is exact for two-sided procedures and for one-sided procedures taken separately. Mixing a two-sided interval with a one-sided test breaks the correspondence, which is a common source of contradictions in written answers.

### 2.12 One-sided coverage

> **Theorem (One-sided bound).** The lower bound $L = \bar{x} - z_{\alpha}\sigma/\sqrt{n}$ satisfies $\text{P}\left(L \le \mu\right) = 1 - \alpha$.

The statement is one-sided because the event of interest is a single inequality. The error probability $\alpha$ is placed entirely in the lower tail of the sampling distribution of $\bar{x}$, which is why the multiplier is $z_{\alpha}$ rather than $z_{\alpha/2}$. For $95\%$ confidence the one-sided multiplier is $1.645$ against the two-sided $1.960$, so the one-sided bound is closer to the estimate and the corresponding interval extends to infinity in one direction.

### 2.13 Summary of the principal results

| Result | Statement | Source |
| --- | --- | --- |
| Unbiased mean | $\text{E}(\bar{x}) = \mu$ | linearity of expectation |
| Variance of mean | $\text{Var}(\bar{x}) = \sigma^{2}/n$ | independence |
| Unbiased variance | $\text{E}(s^{2}) = \sigma^{2}$ | degrees-of-freedom correction |
| Standard error of proportion | $\sqrt{p(1-p)/n}$ | zero-one coding |
| Normal pivot | $\left(\bar{x} - \mu\right)\sqrt{n}/\sigma \sim \text{N}\left(0,1\right)$ | central limit theorem |
| t pivot | $\left(\bar{x} - \mu\right)\sqrt{n}/s \sim t_{n-1}$ | normal sampling |
| Sample size for a mean | $n = \left(z\sigma/E\right)^{2}$ | inverting the margin |
| Sample size for a proportion | $n = z^{2}p^{*}\left(1-p^{*}\right)/E^{2}$ | inverting the margin |

## 3. Formal Proofs, Derivations, and Methods

### 3.1 Proof that the sample mean is unbiased

Step 1. Express the estimator as a linear combination of the observations.

$$
\bar{x} = \sum_{i=1}^{n}\frac{1}{n}x_i
$$

Step 2. Apply linearity of expectation, which holds for any random variables with finite means and requires no independence.

$$
\text{E}(\bar{x}) = \sum_{i=1}^{n}\frac{1}{n}\text{E}\left(x_i\right)
$$

Step 3. Substitute the common population mean.

$$
\text{E}(\bar{x}) = \sum_{i=1}^{n}\frac{1}{n}\mu = \frac{1}{n}\cdot n\mu = \mu
$$

Step 4. Conclude that the bias is zero at every sample size, since the argument used no approximation.

### 3.2 Proof of the variance of the sample mean, with and without replacement

Step 1. Write the variance of the linear combination, allowing for covariance between distinct observations.

$$
\text{Var}(\bar{x}) = \frac{1}{n^{2}}\left[\sum_{i=1}^{n}\text{Var}\left(x_i\right) + \sum_{i \ne j}\text{Cov}\left(x_i, x_j\right)\right]
$$

Step 2. For independent sampling every covariance is zero and the variance collapses.

$$
\text{Var}(\bar{x}) = \frac{1}{n^{2}}\cdot n\sigma^{2} = \frac{\sigma^{2}}{n}
$$

Step 3. For sampling without replacement from a finite population of size $N$, the covariance between two distinct draws is the negative quantity

$$
\text{Cov}\left(x_i, x_j\right) = -\frac{\sigma^{2}}{N-1}, \qquad i \ne j .
$$

Step 4. Count the covariances. There are $n\left(n-1\right)$ ordered pairs with distinct indices.

$$
\text{Var}(\bar{x}) = \frac{1}{n^{2}}\left[n\sigma^{2} - n\left(n-1\right)\frac{\sigma^{2}}{N-1}\right]
$$

Step 5. Factor out $\sigma^{2}/n$ and combine the remaining terms over the common denominator $N-1$.

$$
\text{Var}(\bar{x}) = \frac{\sigma^{2}}{n}\left[1 - \frac{n-1}{N-1}\right] = \frac{\sigma^{2}}{n}\cdot\frac{N-n}{N-1}
$$

Step 6. Check the two limiting cases. When $N \to \infty$ the factor tends to one and the independent-sampling result is recovered; when $n = N$ the factor is zero, as it must be, since a census has no sampling error.

The negative covariance has an intuitive reading. Drawing a large value on the first draw removes a large value from the remaining population, so the second draw is on average smaller. Averaging several such draws therefore produces a less variable result than averaging independent draws would.

### 3.3 Proof that the sample variance with divisor n minus one is unbiased

Step 1. Write the sum of squared deviations from the sample mean and insert and remove the population mean.

$$
\sum_{i=1}^{n}\left(x_i - \bar{x}\right)^{2} = \sum_{i=1}^{n}\left[\left(x_i - \mu\right) - \left(\bar{x} - \mu\right)\right]^{2}
$$

Step 2. Expand the square, producing three terms.

$$
\sum_{i=1}^{n}\left(x_i - \mu\right)^{2} - 2\left(\bar{x} - \mu\right)\sum_{i=1}^{n}\left(x_i - \mu\right) + n\left(\bar{x} - \mu\right)^{2}
$$

Step 3. Evaluate the middle sum by noting that the sum of deviations from $\mu$ is $n$ times the mean deviation.

$$
\sum_{i=1}^{n}\left(x_i - \mu\right) = n\left(\bar{x} - \mu\right)
$$

Step 4. Substitute and cancel the two middle terms.

$$
\sum_{i=1}^{n}\left(x_i - \bar{x}\right)^{2} = \sum_{i=1}^{n}\left(x_i - \mu\right)^{2} - n\left(\bar{x} - \mu\right)^{2}
$$

Step 5. Take expectations term by term, using $\text{E}\left(x_i - \mu\right)^{2} = \sigma^{2}$ and $\text{E}\left(\bar{x} - \mu\right)^{2} = \sigma^{2}/n$.

$$
\text{E}\left[\sum_{i=1}^{n}\left(x_i - \bar{x}\right)^{2}\right] = n\sigma^{2} - n\cdot\frac{\sigma^{2}}{n} = \left(n-1\right)\sigma^{2}
$$

Step 6. Divide both sides by $n-1$ and use linearity of expectation.

$$
\text{E}\left[\frac{1}{n-1}\sum_{i=1}^{n}\left(x_i - \bar{x}\right)^{2}\right] = \sigma^{2}
$$

Step 7. Record the bias of the naive divisor. Dividing by $n$ instead gives expectation $\left(n-1\right)\sigma^{2}/n$, so the bias is $-\sigma^{2}/n$, which vanishes as $n$ grows but is never zero.

### 3.4 Derivation of the standard error of a proportion

Step 1. Code each trial as an indicator variable taking the value one with probability $p$.

$$
y_i = \begin{cases} 1 & \text{with probability } p \\ 0 & \text{with probability } 1 - p \end{cases}
$$

Step 2. Compute the mean of the indicator.

$$
\text{E}\left(y_i\right) = 1\cdot p + 0\cdot\left(1-p\right) = p
$$

Step 3. Compute its second moment and then its variance.

$$
\text{E}\left(y_i^{2}\right) = 1^{2}\cdot p + 0^{2}\cdot\left(1-p\right) = p
$$

$$
\text{Var}\left(y_i\right) = p - p^{2} = p\left(1-p\right)
$$

Step 4. Note that the sample proportion is the mean of the indicators.

$$
\hat{p} = \frac{1}{n}\sum_{i=1}^{n} y_i = \bar{y}
$$

Step 5. Apply the variance formula for a sample mean to obtain the standard error.

$$
\text{Var}(\hat{p}) = \frac{p\left(1-p\right)}{n}, \qquad \text{SE}(\hat{p}) = \sqrt{\frac{p\left(1-p\right)}{n}}
$$

Step 6. Substitute $\hat{p}$ for $p$ to obtain the estimated standard error used in practice, and note that this substitution is the only approximation in the Wald interval.

### 3.5 Derivation of the confidence interval for a mean with known variance

Step 1. State the pivot and its exact distribution under normality, or its approximate distribution by the central limit theorem.

$$
Z = \frac{\bar{x} - \mu}{\sigma/\sqrt{n}} \sim \text{N}\left(0, 1\right)
$$

Step 2. Choose the quantiles that leave $\alpha/2$ in each tail.

$$
\text{P}\left(-z_{\alpha/2} \le Z \le z_{\alpha/2}\right) = 1 - \alpha
$$

Step 3. Substitute the definition of the pivot.

$$
\text{P}\left(-z_{\alpha/2} \le \frac{\bar{x} - \mu}{\sigma/\sqrt{n}} \le z_{\alpha/2}\right) = 1 - \alpha
$$

Step 4. Multiply through by the positive quantity $\sigma/\sqrt{n}$.

$$
\text{P}\left(-z_{\alpha/2}\frac{\sigma}{\sqrt{n}} \le \bar{x} - \mu \le z_{\alpha/2}\frac{\sigma}{\sqrt{n}}\right) = 1 - \alpha
$$

Step 5. Subtract $\bar{x}$ throughout, reversing both inequalities.

$$
\text{P}\left(-\bar{x} - z_{\alpha/2}\frac{\sigma}{\sqrt{n}} \le -\mu \le -\bar{x} + z_{\alpha/2}\frac{\sigma}{\sqrt{n}}\right) = 1 - \alpha
$$

Step 6. Multiply by minus one, reversing the inequalities a second time and restoring their original direction.

$$
\text{P}\left(\bar{x} - z_{\alpha/2}\frac{\sigma}{\sqrt{n}} \le \mu \le \bar{x} + z_{\alpha/2}\frac{\sigma}{\sqrt{n}}\right) = 1 - \alpha
$$

Step 7. Identify the random limits and confirm the definition of a confidence interval.

$$
L = \bar{x} - z_{\alpha/2}\frac{\sigma}{\sqrt{n}}, \qquad U = \bar{x} + z_{\alpha/2}\frac{\sigma}{\sqrt{n}}
$$

Step 8. Check the algebra numerically on the standard case. With $\sigma = 12$, $n = 36$ and $z = 1.96$ the half-width is $3.92$, so an observed mean of $252$ yields the interval from $248.08$ to $255.92$.

### 3.6 Derivation of the confidence interval for a mean with unknown variance

Step 1. Start from the pivot that would be used if $\sigma$ were known.

$$
Z = \frac{\bar{x} - \mu}{\sigma/\sqrt{n}}
$$

Step 2. Replace $\sigma$ by the estimator $s$ and define the resulting ratio.

$$
T = \frac{\bar{x} - \mu}{s/\sqrt{n}}
$$

Step 3. Express the ratio in terms of a standard normal variable and a chi-squared variable. The independence of $\bar{x}$ and $s^{2}$ is a property of normal sampling and is what permits the combination.

$$
T = \frac{Z}{\sqrt{V/\left(n-1\right)}}, \qquad V = \frac{\left(n-1\right)s^{2}}{\sigma^{2}} \sim \chi^{2}_{n-1}
$$

Step 4. Recognise the defining structure of a t variable with $n-1$ degrees of freedom, and note that $\sigma$ has cancelled.

$$
T \sim t_{n-1}
$$

Step 5. Write the central probability statement with t quantiles.

$$
\text{P}\left(-t_{\alpha/2,\,n-1} \le T \le t_{\alpha/2,\,n-1}\right) = 1 - \alpha
$$

Step 6. Invert exactly as in the known-variance case, using the positive quantity $s/\sqrt{n}$.

$$
\text{P}\left(\bar{x} - t_{\alpha/2,\,n-1}\frac{s}{\sqrt{n}} \le \mu \le \bar{x} + t_{\alpha/2,\,n-1}\frac{s}{\sqrt{n}}\right) = 1 - \alpha
$$

Step 7. Compare the two multipliers at a fixed sample size to see the cost of not knowing $\sigma$. At $n = 25$ the t multiplier is $2.064$ against the normal $1.960$, so the interval is about five per cent wider. At $n = 5$ the t multiplier is $2.776$ and the penalty is over forty per cent.

### 3.7 Derivation of the Wald interval

Step 1. Write the approximate pivot for a proportion.

$$
Z = \frac{\hat{p} - p}{\sqrt{p\left(1-p\right)/n}}
$$

Step 2. State the central probability.

$$
\text{P}\left(-z \le Z \le z\right) = 1 - \alpha
$$

Step 3. Substitute and clear the denominator.

$$
\text{P}\left(\hat{p} - z\sqrt{\frac{p\left(1-p\right)}{n}} \le p \le \hat{p} + z\sqrt{\frac{p\left(1-p\right)}{n}}\right) \approx 1 - \alpha
$$

Step 4. Replace the unknown $p$ in the standard error by $\hat{p}$, which is the step that destroys exactness and produces the Wald form.

$$
\left[\hat{p} - z\sqrt{\frac{\hat{p}\left(1-\hat{p}\right)}{n}}, \;\; \hat{p} + z\sqrt{\frac{\hat{p}\left(1-\hat{p}\right)}{n}}\right]
$$

Step 5. Note the two consequences. The interval is symmetric about $\hat{p}$, which is convenient, and its width is fixed once $\hat{p}$ is known, which is convenient for reporting but wrong in the tails, where the true standard error is much smaller than the plug-in value suggests.

### 3.8 Derivation of the Wilson interval by solving the quadratic

Step 1. Begin with the exact inequality before any substitution.

$$
\left(\hat{p} - p\right)^{2} \le z^{2}\frac{p\left(1-p\right)}{n}
$$

Step 2. Clear the denominator of $n$.

$$
n\left(\hat{p} - p\right)^{2} \le z^{2}p\left(1-p\right)
$$

Step 3. Expand both sides.

$$
n\hat{p}^{2} - 2n\hat{p}p + np^{2} \le z^{2}p - z^{2}p^{2}
$$

Step 4. Collect everything on the left as a quadratic in $p$.

$$
\left(n + z^{2}\right)p^{2} - \left(2n\hat{p} + z^{2}\right)p + n\hat{p}^{2} \le 0
$$

Step 5. The quadratic opens upwards, so the inequality holds between the two roots. Apply the quadratic formula, dividing the coefficients by $n + z^{2}$.

$$
p = \frac{2n\hat{p} + z^{2} \pm \sqrt{\left(2n\hat{p} + z^{2}\right)^{2} - 4n\left(n + z^{2}\right)\hat{p}^{2}}}{2\left(n + z^{2}\right)}
$$

Step 6. Simplify the discriminant by expanding and cancelling the terms in $\hat{p}^{2}$.

$$
\left(2n\hat{p} + z^{2}\right)^{2} - 4n\left(n+z^{2}\right)\hat{p}^{2} = z^{2}\left[4n\hat{p}\left(1-\hat{p}\right) + z^{2}\right]
$$

Step 7. Take the square root, which is legitimate because the bracket is non-negative, and divide numerator and denominator by $2n$ to obtain the standard form.

$$
p = \frac{\hat{p} + \frac{z^{2}}{2n} \pm z\sqrt{\frac{\hat{p}\left(1-\hat{p}\right)}{n} + \frac{z^{2}}{4n^{2}}}}{1 + \frac{z^{2}}{n}}
$$

Step 8. Identify the centre and half-width. The centre is the weighted average of $\hat{p}$ and one half, and the half-width is the square-root term divided by the inflation factor.

$$
\tilde{p} = \frac{\hat{p} + \frac{z^{2}}{2n}}{1 + \frac{z^{2}}{n}}, \qquad h = \frac{z\sqrt{\frac{\hat{p}\left(1-\hat{p}\right)}{n} + \frac{z^{2}}{4n^{2}}}}{1 + \frac{z^{2}}{n}}
$$

Step 9. Multiply numerator and denominator of the centre by $n$ to recover the form quoted in Section 2.9, and check that the limits stay inside the unit interval for every admissible $\hat{p}$.

### 3.9 Derivation of the sample size formulas

Step 1. Write the margin of error for a mean and name the target value.

$$
E = z_{\alpha/2}\frac{\sigma}{\sqrt{n}}
$$

Step 2. Rearrange to isolate the square root.

$$
\sqrt{n} = \frac{z_{\alpha/2}\sigma}{E}
$$

Step 3. Square both sides.

$$
n = \left(\frac{z_{\alpha/2}\sigma}{E}\right)^{2}
$$

Step 4. Repeat for a proportion using the planning value $p^{*}$.

$$
E = z_{\alpha/2}\sqrt{\frac{p^{*}\left(1-p^{*}\right)}{n}} \quad \Longrightarrow \quad n = \frac{z_{\alpha/2}^{2}p^{*}\left(1-p^{*}\right)}{E^{2}}
$$

Step 5. Insert the finite population correction and solve again. Writing $n_0$ for the uncorrected requirement,

$$
E = z_{\alpha/2}\frac{\sigma}{\sqrt{n}}\sqrt{\frac{N-n}{N-1}} \quad \Longrightarrow \quad n = \frac{n_0}{1 + \frac{n_0 - 1}{N}}
$$

Step 6. Justify the last step. Squaring the corrected margin and rearranging gives a linear equation in $n$ rather than a quadratic, because the factor $\left(N-n\right)/\left(N-1\right)$ is linear in $n$; solving it produces the displayed form. The corrected size is always smaller than $n_0$, which is the reward for sampling a large fraction of a small population.

Step 7. Round upwards in all three formulas. The margin of error is a decreasing function of $n$, so any rounding down violates the target.

### 3.10 Method for one-sided bounds

Step 1. Decide from the wording whether the question asks for a lower bound, an upper bound, or both.

Step 2. Select the one-sided multiplier $z_{\alpha}$ or $t_{\alpha,\,n-1}$, using $\alpha$ itself rather than $\alpha/2$.

Step 3. Compute the standard error exactly as in the two-sided case.

Step 4. Add or subtract the product of multiplier and standard error according to direction.

Step 5. State the bound as an inequality rather than as a pair of limits, for example that the mean exceeds the lower bound with the stated confidence.

### 3.11 Method for converting between an interval and a test

Step 1. Identify the null value $\theta_0$ and the significance level, which equals $1 - \left(1-\alpha\right)$.

Step 2. If an interval is available, compare $\theta_0$ with the limits: inside means no rejection, outside means rejection.

Step 3. If a test statistic is available, compute it and compare with the critical value.

Step 4. To move from a test to an interval, collect all $\theta_0$ that would not be rejected. For a two-sided z test this set is the interval of Section 3.5, which closes the loop.

## 4. Representative Worked Examples and Solutions

### 4.1 Problem: an interval with a known standard deviation

A production line fills jars. The fill volume has a known standard deviation of $15$ millilitres. A sample of $25$ jars gives a mean fill of $48.6$ millilitres. Construct a $95\%$ confidence interval and state the width.

### 4.2 Solution: apply the pivot with the normal multiplier

Step 1. Record the inputs. The sample mean is $\bar{x} = 48.6$, the population standard deviation is $\sigma = 15$, the sample size is $n = 25$, and $z_{0.025} = 1.96$.

Step 2. Compute the standard error of the mean.

$$
\text{SE} = \frac{15}{\sqrt{25}} = \frac{15}{5} = 3
$$

Step 3. Compute the margin of error.

$$
E = 1.96 \times 3 = 5.88
$$

Step 4. Form the limits.

$$
L = 48.6 - 5.88 = 42.72, \qquad U = 48.6 + 5.88 = 54.48
$$

Step 5. Report the width as twice the margin.

$$
W = 2 \times 5.88 = 11.76
$$

Step 6. Interpret. We are $95\%$ confident that the mean fill of all jars lies between $42.72$ and $54.48$ millilitres, and the interval is $11.76$ millilitres wide.

Step 7. Check that the interval is centred on the estimate and that the half-width equals two standard errors, both of which hold by construction.

### 4.3 Problem: an interval with an unknown standard deviation

A sample of $25$ components has a mean lifetime of $68.4$ hours and a standard deviation of $5.2$ hours. Construct a $95\%$ confidence interval, and compare it with the interval that would have been obtained had the standard deviation been known.

### 4.4 Solution: the t multiplier replaces the normal multiplier

Step 1. Record the inputs and the degrees of freedom. Here $\bar{x} = 68.4$, $s = 5.2$, $n = 25$ and $n - 1 = 24$.

Step 2. Look up the two-sided $95\%$ t quantile on $24$ degrees of freedom, which is $2.064$.

Step 3. Compute the estimated standard error.

$$
\widehat{\text{SE}} = \frac{5.2}{\sqrt{25}} = \frac{5.2}{5} = 1.04
$$

Step 4. Compute the margin of error with the t multiplier.

$$
E_t = 2.064 \times 1.04 = 2.1466
$$

Step 5. Form the limits.

$$
L = 68.4 - 2.1466 = 66.25, \qquad U = 68.4 + 2.1466 = 70.55
$$

Step 6. Compute the margin that the normal multiplier would have produced for comparison.

$$
E_z = 1.96 \times 1.04 = 2.0384
$$

Step 7. Quantify the difference.

$$
\frac{E_t - E_z}{E_z} \times 100\% \approx 5.31\%
$$

Step 8. Interpret. The correct interval runs from $66.25$ to $70.55$; using the normal multiplier would have produced the too-narrow limits $66.36$ and $70.44$, understating the margin by about five per cent. The penalty is modest here because $24$ degrees of freedom is a moderate amount of information, but the direction of the error is always the same: the normal multiplier is never the conservative choice when $\sigma$ is estimated.

### 4.5 Problem: Wald and Wilson intervals for the same proportion

In a random sample of $400$ employees, $92$ use public transport to work. Construct both the Wald and the Wilson $95\%$ confidence intervals for the population proportion and compare them.

### 4.6 Solution: two inversions of one pivot

Step 1. Compute the sample proportion.

$$
\hat{p} = \frac{92}{400} = 0.23
$$

Step 2. Compute the estimated standard error.

$$
\sqrt{\frac{0.23 \times 0.77}{400}} = \sqrt{\frac{0.1771}{400}} = \sqrt{0.00044275} \approx 0.02104
$$

Step 3. Compute the Wald margin.

$$
1.96 \times 0.02104 = 0.04124
$$

Step 4. State the Wald limits.

$$
L_W = 0.23 - 0.04124 = 0.18876, \qquad U_W = 0.23 + 0.04124 = 0.27124
$$

Step 5. Compute the Wilson centre using $\tilde{p} = \left(x + z^{2}/2\right)/\left(n + z^{2}\right)$ with $x = 92$ and $z^{2} = 3.8416$.

$$
\tilde{p} = \frac{92 + 1.9208}{400 + 3.8416} = \frac{93.9208}{403.8416} \approx 0.23257
$$

Step 6. Compute the Wilson half-width.

$$
h = 1.96\sqrt{\frac{0.23257 \times 0.76743}{403.8416}} \approx 1.96 \times 0.021023 \approx 0.04120
$$

Step 7. State the Wilson limits.

$$
L_Z = 0.23257 - 0.04120 = 0.19137, \qquad U_Z = 0.23257 + 0.04120 = 0.27377
$$

Step 8. Compare. The two intervals agree to within about three tenths of one percentage point at each end. The Wilson centre is shifted towards one half by $0.00257$, and its half-width is fractionally smaller. At $n = 400$ with $\hat{p}$ near a quarter, the linear approximation inside the Wald form is doing no harm.

Step 9. Interpret. We are $95\%$ confident that the proportion of all employees using public transport lies between $18.9\%$ and $27.1\%$ on the Wald form, or between $19.1\%$ and $27.4\%$ on the Wilson form. Either statement is defensible at this sample size, and the difference is far smaller than the rounding of the report.

### 4.7 Problem: a small sample with a small proportion

In a pilot study of $20$ users of a new feature, $3$ report a problem. Construct the Wald and Wilson $95\%$ intervals and comment on the difference.

### 4.8 Solution: where the Wald form breaks down

Step 1. Compute the sample proportion.

$$
\hat{p} = \frac{3}{20} = 0.15
$$

Step 2. Compute the estimated standard error.

$$
\sqrt{\frac{0.15 \times 0.85}{20}} = \sqrt{\frac{0.1275}{20}} = \sqrt{0.006375} \approx 0.07984
$$

Step 3. Compute the Wald margin.

$$
1.96 \times 0.07984 \approx 0.15649
$$

Step 4. State the Wald limits and inspect them.

$$
L_W = 0.15 - 0.15649 = -0.00649, \qquad U_W = 0.15 + 0.15649 = 0.30649
$$

Step 5. Record the defect. The lower limit is negative, which is impossible for a proportion. The interval also implies a precision that a sample of twenty cannot support.

Step 6. Compute the Wilson centre.

$$
\tilde{p} = \frac{3 + 1.9208}{20 + 3.8416} = \frac{4.9208}{23.8416} \approx 0.20640
$$

Step 7. Compute the Wilson half-width.

$$
h = 1.96\sqrt{\frac{0.20640 \times 0.79360}{23.8416}} \approx 1.96 \times 0.08289 \approx 0.16246
$$

Step 8. State the Wilson limits.

$$
L_Z = 0.20640 - 0.16246 = 0.04394, \qquad U_Z = 0.20640 + 0.16246 = 0.36885
$$

Step 9. Interpret the comparison. The Wilson interval runs from about $4.4\%$ to $36.9\%$ and lies entirely inside the permissible range; it is also much wider than the Wald interval on the upper side and much more sensible on the lower side. With only three successes the data are weakly informative, and the honest interval says so.

Step 10. State the lesson. Both intervals are approximations to the same exact binomial inversion, but the Wald approximation treats the standard error as constant in $p$, and that treatment fails when $\hat{p}$ is close to a boundary. The Wilson form solves the inequality exactly and therefore respects the parameter space.

### 4.9 Problem: sample size with a finite population

A health authority wishes to estimate the mean systolic blood pressure of the $2000$ adults in a district, with a margin of error of $2$ millimetres of mercury at $95\%$ confidence. A pilot study suggests a standard deviation of $12$. Find the required sample size, first ignoring and then applying the finite population correction.

### 4.10 Solution: compute the uncorrected size, then deflate it

Step 1. Compute the uncorrected sample size.

$$
n_0 = \left(\frac{1.96 \times 12}{2}\right)^{2} = \left(11.76\right)^{2} = 138.30
$$

Step 2. Round up to the next whole number.

$$
n_0 = 139
$$

Step 3. Compute the correction factor using the rounded value.

$$
1 + \frac{n_0 - 1}{N} = 1 + \frac{138}{2000} = 1.069
$$

Step 4. Divide the uncorrected size by the factor.

$$
n = \frac{139}{1.069} = 130.03
$$

Step 5. Round up again, since the corrected size must also be a whole number and must not fall short.

$$
n = 131
$$

Step 6. Interpret. Measuring $131$ adults out of $2000$ is enough, because the sample already covers more than six per cent of the population and the correction recognises the extra information that this represents. Ignoring the correction would waste eight interviews.

Step 7. Check the direction of the correction. The corrected size is smaller than the uncorrected size, as it must be, and it approaches the uncorrected size as $N$ grows.

### 4.11 Problem: an interval and a test that must agree

Using the jar data of Section 4.1, with $\bar{x} = 48.6$, $\sigma = 15$ and $n = 25$, test at the $5\%$ level whether the mean fill is $50$ millilitres, and confirm the conclusion from the interval alone.

### 4.12 Solution: membership in the interval is non-rejection

Step 1. State the hypotheses.

$$
H_0: \mu = 50, \qquad H_1: \mu \ne 50
$$

Step 2. Compute the test statistic using the standard error already found.

$$
z = \frac{48.6 - 50}{3} = \frac{-1.4}{3} \approx -0.4667
$$

Step 3. Compare with the critical value for a two-sided $5\%$ test, which is $1.96$.

$$
\left|-0.4667\right| = 0.4667 < 1.96
$$

Step 4. Conclude that the null hypothesis is not rejected at the $5\%$ level.

Step 5. Confirm from the interval. The $95\%$ interval computed earlier runs from $42.72$ to $54.48$, and the value $50$ lies inside it, so non-rejection is exactly what the duality requires.

Step 6. Confirm the boundary case by testing a value just outside the interval, namely $54$. The statistic is

$$
z = \frac{48.6 - 54}{3} = -1.8,
$$

whose absolute value is below $1.96$, so $54$ is still not rejected, and indeed $54$ lies inside the interval. Testing the value $55$ gives

$$
z = \frac{48.6 - 55}{3} \approx -2.133,
$$

whose absolute value exceeds $1.96$, so $55$ is rejected, and $55$ lies outside the upper limit of $54.48$. Both checks agree with the interval.

Step 7. Interpret. The data are compatible with a true mean fill of $50$ millilitres, since a difference of $1.4$ millilitres is less than half a standard error. The interval and the test are two ways of saying the same thing, and the agreement in the boundary case confirms that the arithmetic of both has been done correctly.

## 5. Mathematical Extensions, Limits, and Common Errors

### 5.1 Interpretation: the procedure, not the interval

The formal definition of coverage makes the correct interpretation unavoidable. The probability statement is

$$
\text{P}_{\theta}\left(L \le \theta \le U\right) = 1 - \alpha,
$$

and it is a statement about the joint distribution of the random endpoints $L$ and $U$. It says that if the whole experiment were repeated, the intervals produced would cover the fixed parameter in a proportion $1-\alpha$ of repetitions.

Three misreadings must be rejected explicitly.

The first is that a realised interval contains the parameter with probability $0.95$. Once $l$ and $u$ are numbers, the event is settled; the probability is zero or one and is unknown. What can be said is that $95\%$ of intervals produced by this method succeed.

The second is that $95\%$ of the population lies inside the interval. A confidence interval is an interval for a parameter, not a tolerance interval for data. A $95\%$ confidence interval for a mean computed from $400$ observations may be a few units wide while the observations themselves span a hundred units.

The third is that the confidence level is a property of the realised interval that could be improved by looking at the data again. Any data-dependent widening or narrowing that is not part of the pre-specified procedure destroys the coverage guarantee. This is why choosing the sample size after seeing a preliminary interval, or discarding an interval that looks too wide, invalidates the stated level.

### 5.2 Coverage, conservatism, and the failure of the Wald interval

The Wald interval is not merely approximate in the sense of having small numerical error; it can have seriously deficient coverage. For $n = 20$ and a true proportion near $0.15$, nominal $95\%$ Wald intervals cover the truth far less than $95\%$ of the time, sometimes below $85\%$. The Wilson interval does much better, with coverage close to nominal for all $p$ and $n$ of reasonable size.

The reason is structural. The Wald interval's width is determined by $\hat{p}$, which is itself noisy. When $\hat{p}$ happens to land close to a boundary, the interval becomes very narrow at exactly the moment the data are least informative, and the narrow interval then misses the parameter. The Wilson interval avoids this by inverting the exact inequality, so its width responds correctly to the evidence.

A practical rule, due to Brown, Cai and DasGupta, is that the Wald interval should not be used unless $n\hat{p} \ge 10$ and $n\left(1-\hat{p}\right) \ge 10$. When either condition fails, the Wilson interval or an exact binomial interval should be used instead. Examinations often require the Wald interval by convention, but a candidate who notices the failure earns credit for saying so.

### 5.3 Sensitivity of the width

The three levers on width have different economic characters, and it is worth summarising them in a single place.

| Quantity increased | Effect on width | Size of effect | Controllable by the investigator |
| --- | --- | --- | --- |
| Confidence level | increases | multiplier rises from $1.645$ to $2.576$ across the usual range | yes, as a policy choice |
| Sample size | decreases | proportional to $1/\sqrt{n}$ | yes, at a cost |
| Population standard deviation | increases | proportional to $\sigma$ | no |
| Proportion near one half | increases | factor $\sqrt{\hat{p}\left(1-\hat{p}\right)}$ maximal at one half | no |
| Finite population correction | decreases | factor $\sqrt{\left(N-n\right)/\left(N-1\right)}$ | partly |

The table makes the planning problem concrete. An investigator who needs a specified width must either accept a lower confidence level or buy a larger sample, and the exchange rate between the two is read directly from the multipliers. Doubling the sample reduces the width by about thirty per cent, from $1/\sqrt{n}$ to $1/\sqrt{2n}$; raising the confidence level from $95\%$ to $99\%$ increases the width by thirty-one per cent. Neither is free.

### 5.4 Limits of the method

The normal interval for a mean requires either a normal population or a large sample. The central limit theorem supplies the second route, but its accuracy in the tails is what matters for a $99\%$ interval, and tail accuracy converges more slowly than central accuracy. For a strongly skewed population a sample of thirty may give a $95\%$ interval that is acceptable and a $99\%$ interval that is not.

The t interval requires a normal population exactly. It is robust to mild non-normality and to outliers, because the sample standard deviation is itself sensitive to outliers but the t quantiles grow to accommodate small samples. It is not robust to severe skewness with a small sample.

The proportion intervals require independent trials with constant $p$. Cluster sampling, stratified designs and unequal probability sampling all change the variance of $\hat{p}$ and therefore the standard error. The design effect, the ratio of the true variance under the design to the variance under simple random sampling, must be applied; ignoring it understates the standard error and produces intervals that are too narrow.

Finally, no interval repairs a biased sample. The coverage guarantee is a statement about a probability distribution generated by random selection. If the sample is a convenience sample of volunteers, the distribution of $\hat{p}$ is not the one the formula assumes, and the stated confidence level is a fiction no matter how careful the arithmetic.

### 5.5 Errors that recur in written work

The first error is to use $z$ when $t$ is required. The trigger is simple: if the population standard deviation is unknown and the sample is small, the t multiplier is required. Using $1.96$ with five degrees of freedom understates the margin by about twenty-four per cent.

The second error is to divide by $n$ instead of by $\sqrt{n}$ when computing the standard error. The resulting number is far too small and the interval far too narrow. A quick dimensional check helps: the standard error must have the same units as the observations and must be smaller than the sample standard deviation.

The third error is to use the two-sided multiplier for a one-sided bound. For $95\%$ confidence the one-sided multiplier is $1.645$; using $1.96$ produces a bound that is too conservative and loses marks for the wrong convention.

The fourth error is to omit the finite population correction when the sample is a large fraction of the population. The omission is conservative rather than dangerous, but it misstates the precision achieved.

The fifth error is to interpret the confidence level as a probability about the realised interval, or as a claim about the proportion of the data captured. Both misreadings are treated in Section 5.1 and both are penalised heavily because they misrepresent what the method delivers.

The sixth error is to report an interval without units, without the population, or without the confidence level. An interval of $42.72$ to $54.48$ is meaningless without knowing that the units are millilitres and the population is jars on one production line.

### 5.6 Extensions worth knowing

Three extensions lie just beyond the syllabus and are useful for understanding where the theory goes.

The first is the delta method, which produces standard errors for smooth functions of estimators. If $\hat{\theta}$ has standard error $\text{SE}\left(\hat{\theta}\right)$, then for a differentiable function $g$ the standard error of $g\left(\hat{\theta}\right)$ is approximately $\left|g'\left(\theta\right)\right|\text{SE}\left(\hat{\theta}\right)$. This is how standard errors for odds ratios, rates and elasticities are constructed.

The second is the bootstrap, which replaces the analytical standard error by a simulation. Resampling the observed data with replacement many times and recomputing the estimator each time produces an empirical sampling distribution, whose quantiles give an interval. The bootstrap requires no distributional assumption and is the standard tool when no pivot is available.

The third is the Bayesian credible interval, which is the posterior interval for $\theta$ given a prior and the data. It does have the interpretation that a confidence interval lacks, namely that $\theta$ lies in the interval with a stated posterior probability, but it requires a prior and it answers a different question. With a flat prior and a normal model the two intervals coincide numerically, which is a useful check on intuition but not a licence to interpret one as the other.

The relationship between intervals and tests extends into these areas unchanged. Every confidence set is the collection of parameter values not rejected by some test, and every test has a corresponding confidence set. This duality is the reason the two halves of inference are taught together, and it is the deepest structural fact in the subject.
