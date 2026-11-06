## 1. Foundational Concepts, Definitions, and Axioms

### 1.1 The decision problem stated exactly

Estimation asks what value a parameter takes. Testing asks whether a specific value, or a specific set of values, can be maintained in the face of the data. The two questions are related but not identical, and the difference is one of decision rather than of arithmetic: a test ends in one of exactly two verdicts, and any procedure that ends in two verdicts must be judged by how often each verdict is wrong.

Let $x_1, \dots, x_n$ be a random sample from a distribution indexed by a parameter $\theta \in \Theta$. A hypothesis is a subset $\Theta_0 \subset \Theta$. The problem is to decide, on the basis of the sample, whether $\theta$ lies in $\Theta_0$ or in its complement.

> **Definition (Statistical hypothesis).** A statistical hypothesis is a statement that the parameter $\theta$ belongs to a specified subset of the parameter space $\Theta$. A hypothesis is simple if the subset contains exactly one point and composite otherwise.

> **Definition (Null and alternative).** The null hypothesis is $H_0: \theta \in \Theta_0$ and the alternative hypothesis is $H_1: \theta \in \Theta_1$, where $\Theta_1 = \Theta \setminus \Theta_0$. The two sets are disjoint and their union is the whole parameter space.

Three consequences follow from this set-theoretic definition and are worth stating because they are frequently violated in practice.

The hypotheses must be exhaustive, so that no value of $\theta$ is left unclassified. Writing $H_0: \mu = 50$ against $H_1: \mu > 52$ leaves the interval $\left(50, 52\right]$ unclassified and makes the procedure incoherent.

The hypotheses must be disjoint, so that no value is claimed by both. Writing $H_0: \mu \le 50$ against $H_1: \mu \ge 50$ assigns $50$ to both and inflates the error rates at that boundary point.

The null hypothesis is usually the one that can be defended by default, and it usually contains the value that would make the parameter irrelevant to the decision at hand.

The logical structure is that of reductio ad absurdum, adapted to a probabilistic setting. In a mathematical contradiction one assumes a proposition $P$, derives a consequence $Q$, and shows that $Q$ is false; the assumption $P$ then fails. In a statistical test one assumes $\theta = \theta_0$, derives that the observed statistic has a known distribution, and finds that the observed value lies in a region of that distribution with probability $\alpha$ or less. The consequence is not impossible, only improbable, so the rejection of $\theta_0$ is a decision rule rather than a proof. Two features of the adaptation are worth isolating: the smaller the tail probability, the closer the argument comes to a contradiction; and no finite value of the tail probability ever makes it a contradiction, which is why a rejected null is described as unsupported rather than as false.

### 1.2 Simple, composite, one-sided and two-sided hypotheses

A simple null pins the parameter down, as in $H_0: \mu = 50$. A composite null allows a range, as in $H_0: \mu \le 50$. The distinction matters because the distribution of the test statistic is fully determined only under a simple null, so any composite null requires the error probability to be controlled uniformly over its values.

> **Definition (One-sided and two-sided alternatives).** For a scalar parameter $\theta$ and a null value $\theta_0$,

$$
H_1: \theta > \theta_0 \quad \text{(upper one-sided)}, \qquad H_1: \theta < \theta_0 \quad \text{(lower one-sided)}, \qquad H_1: \theta \ne \theta_0 \quad \text{(two-sided)} .
$$

The shape of the alternative is not a stylistic preference. It determines the rejection region, and therefore the critical values, and therefore the verdict. A two-sided alternative at level $\alpha$ divides its allowance equally between the two tails; a one-sided alternative spends the whole allowance in one tail.

Choosing the alternative after inspecting the data is not a test at level $\alpha$ at all. If the direction is chosen to match the sign of the observed deviation, the effective two-sided error rate becomes $2\alpha$, and the reported level is false. The alternative must be fixed by the scientific question, before the sample is examined.

### 1.3 Test functions, rejection regions and the size of a test

A test is a rule that maps every possible sample to one of two decisions. It is convenient to describe it by the set of samples on which it rejects.

> **Definition (Rejection region and test function).** The rejection region $R$ is the subset of the sample space on which $H_0$ is rejected. Equivalently, the test function is $\phi\left(x\right) = 1$ when $x \in R$ and $\phi\left(x\right) = 0$ otherwise, and the test rejects when $\phi = 1$.

> **Definition (Size and level).** The size of a test with rejection region $R$ is $\sup_{\theta \in \Theta_0} \text{P}_{\theta}\left(X \in R\right)$. The test has level $\alpha$ if its size does not exceed $\alpha$, that is, if $\text{P}_{\theta}\left(X \in R\right) \le \alpha$ for every $\theta \in \Theta_0$.

The supremum matters when the null is composite. A test of $H_0: \mu \le 50$ that controls the error probability at $\mu = 50$ but not at $\mu = 49$ would not have level $\alpha$, because the null includes $\mu = 49$. In the standard one-sided problems the error probability is largest at the boundary value, so controlling it there controls it everywhere; this monotonicity is proved in Section 2.2.

The distinction between size and level is also the distinction between an exact and a conservative test. A test whose size equals $\alpha$ is exact. A test whose size is strictly less than $\alpha$ at every null value is conservative, and a conservative test is legitimate but less powerful.

### 1.4 The test statistic and the standardised distance

A test is implemented through a scalar summary of the sample.

> **Definition (Test statistic).** A test statistic $T = T\left(x_1, \dots, x_n\right)$ is a function of the sample whose distribution is known, at least approximately, under $H_0$ and does not depend on any unknown parameter.

The last clause is what makes the statistic usable. If the distribution of $T$ under $H_0$ depended on $\sigma$, no single table of critical values would serve, because the table would have to be indexed by an unknown quantity.

All the test statistics in this topic are standardised distances between an estimate and the null value,

$$
T = \frac{\hat{\theta} - \theta_0}{\text{SE}\left(\hat{\theta}\right)} \quad \text{or} \quad T = \frac{\hat{\theta} - \theta_0}{\widehat{\text{SE}}\left(\hat{\theta}\right)} ,
$$

where the first form applies when the standard error is known exactly and the second when it must be estimated. The first produces a normal or chi-square reference distribution; the second produces a $t$ or $F$ distribution, whose extra variability is the price of estimation.

A statistic of this form is sometimes called a pivot or an asymptotically pivotal quantity. In estimation theory a pivot has a distribution free of all unknowns, which is what allows an interval to be constructed by inversion. In testing theory the same object is compared against its null distribution, which is what allows a critical value to be computed. The object is identical; only the use differs.

### 1.5 The p-value defined exactly

The critical value approach fixes the level first and then compares. The p-value approach computes the smallest level at which the observed data would reject, and this gives a definition that is precise rather than descriptive.

> **Definition (p-value).** Let $T$ be a test statistic with observed value $t_{\text{obs}}$, and for each $\alpha$ let $R_{\alpha}$ be the rejection region of a level $\alpha$ test. The p-value is

$$
p\left(t_{\text{obs}}\right) = \inf\left\{ \alpha : t_{\text{obs}} \in R_{\alpha} \right\} .
$$

For the standard tests the regions are nested, $R_{\alpha} \subset R_{\alpha'}$ whenever $\alpha < \alpha'$, so the infimum is attained and the p-value is the level at which the observed value sits exactly on the boundary of the rejection region. In the one-sided normal case this reduces to $p = \text{P}_{H_0}\left(T \ge t_{\text{obs}}\right)$; in the two-sided symmetric case it reduces to $p = 2\,\text{P}_{H_0}\left(T \ge \left| t_{\text{obs}} \right|\right)$.

Two structural facts follow at once. First, under $H_0$ the p-value has a uniform distribution on the interval from zero to one, so a p-value below $\alpha$ occurs with probability exactly $\alpha$. Second, the rule "reject when $p \le \alpha$" is equivalent to the rule "reject when $t_{\text{obs}} \in R_{\alpha}$" by the definition itself; the equivalence is not an empirical observation but an identity.

### 1.6 Errors, their probabilities, and the power function

A test can fail in two directions, and a full description of a test requires both probabilities as functions of the true parameter.

> **Definition (Type I and Type II errors).** A Type I error occurs when $H_0$ is rejected although $\theta \in \Theta_0$, and its probability is $\alpha\left(\theta\right) = \text{P}_{\theta}\left(X \in R\right)$ for $\theta \in \Theta_0$. A Type II error occurs when $H_0$ is not rejected although $\theta \in \Theta_1$, and its probability is $\beta\left(\theta\right) = 1 - \text{P}_{\theta}\left(X \in R\right)$ for $\theta \in \Theta_1$.

> **Definition (Power function).** The power function of a test is $\pi\left(\theta\right) = \text{P}_{\theta}\left(X \in R\right)$, defined for every $\theta \in \Theta$. On $\Theta_0$ it equals the Type I error probability; on $\Theta_1$ it equals one minus the Type II error probability, that is, the power.

The power function is the single object that describes a test completely. Its value at the null value is the size, its values on the alternative region measure the ability to detect departures, and its shape reveals whether the test is well designed. A test with a power function that dips below $\alpha$ somewhere in the null region is invalid, because the size is a supremum.

The four levers on power are the distance between the true value and the null value, the population variance, the sample size and the level. Only the sample size improves power without sacrificing the Type I error rate.

### 1.7 The two schools and what each contributes

The p-value and the fixed-level decision rule come from different traditions, and the difference explains several apparent inconsistencies in applied writing.

The Fisherian tradition treats the p-value as a continuous measure of evidence and resists the idea that a sharp verdict should be delivered at a conventional threshold. Its language is "the data are not consistent with the hypothesis" and its emphasis is on the strength of evidence.

The Neyman–Pearson tradition treats testing as a decision problem with explicit error rates. Its language is "reject" or "fail to reject", and its central result, the Neyman–Pearson lemma, identifies the most powerful test for a given size.

Modern practice mixes the two: a test is pre-specified with a level, and the p-value is reported alongside the decision so that a reader can apply a different threshold. The mixture is harmless provided the two ideas are not confused. In particular, the p-value is not a posterior probability that the null is true, and no amount of Fisherian language makes it one.

### 1.8 Assumptions required by each test

Each statistic has a reference distribution that is valid only under stated conditions. The conditions are collected here because most of the serious errors in applied testing are assumption failures rather than arithmetic failures.

| Test | Reference distribution | Independence | Distributional assumption | Other conditions |
| --- | --- | --- | --- | --- |
| One-sample z | standard normal | required | none if $n$ large | $\sigma$ known |
| One-sample t | Student t, $n-1$ df | required | normal population, or $n$ large | $s$ estimated |
| Paired t | Student t, $n-1$ df | required on pairs | normal differences | pairs meaningful |
| Two-sample t | Student t, $n_1 + n_2 - 2$ df | required | normal populations | equal variances assumed |
| Proportion z | standard normal | required | none if counts large | $np_0$ and $n\left(1 - p_0\right)$ at least $10$ |
| Chi-square fit | chi-square, $k - 1 - m$ df | required | none if counts large | every expected count at least $5$ |
| Chi-square independence | chi-square, $\left(r-1\right)\left(c-1\right)$ df | required | none if counts large | every expected count at least $5$ |
| Variance ratio F | F, $\left(n_1 - 1, n_2 - 1\right)$ df | required | normal populations | none |

The "or $n$ large" qualifications are central limit theory in disguise. They are not permission to ignore the distribution entirely; they say that the sample must be large enough for the standardised statistic to be approximately normal, and the required size grows with the skewness of the population.

### 1.9 Notation

The notation below is used throughout and matches the estimation theory that precedes this topic.

| Symbol | Meaning |
| --- | --- |
| $\mu_0$ | the value of the mean specified by $H_0$ |
| $\sigma$, $s$ | population and sample standard deviations |
| $\bar{x}$, $s^{2}$ | sample mean and sample variance with divisor $n - 1$ |
| $\text{SE}$ | standard error of the estimator used in the numerator |
| $z_{\alpha}$ | upper $\alpha$ point of the standard normal distribution |
| $t_{\alpha, \nu}$ | upper $\alpha$ point of the t distribution with $\nu$ degrees of freedom |
| $\chi^{2}_{\alpha, \nu}$ | upper $\alpha$ point of the chi-square distribution with $\nu$ degrees of freedom |
| $F_{\alpha, \nu_1, \nu_2}$ | upper $\alpha$ point of the F distribution |
| $O_{ij}$, $E_{ij}$ | observed and expected counts in cell $\left(i, j\right)$ |

The convention on quantiles is uniform: $z_{\alpha}$ is the value with area $\alpha$ to its right, so $z_{0.025} = 1.96$ and $z_{0.05} = 1.645$. The same convention applies to the $t$, chi-square and $F$ tables, so that a two-sided test at level $\alpha$ uses the point with area $\alpha/2$ to the right.

## 2. Theorems, Lemmas, and Analytical Properties

### 2.1 The Neyman–Pearson lemma

The foundational optimality result identifies the best possible test when both hypotheses are simple.

> **Theorem (Neyman–Pearson).** Let $f_0$ and $f_1$ be the densities of the sample under $H_0$ and $H_1$ respectively. For a given size $\alpha$, the most powerful test rejects $H_0$ for large values of the likelihood ratio $\Lambda = f_1\left(x\right)/f_0\left(x\right)$; that is, the rejection region has the form

$$
R = \left\{ x : \frac{f_1\left(x\right)}{f_0\left(x\right)} \ge k \right\}
$$

with $k$ chosen so that $\text{P}_{0}\left(X \in R\right) = \alpha$.

The lemma says that evidence should be measured by how much better the alternative explains the data than the null does, and that no other test of the same size can beat this one. Every test statistic in this topic is a monotone function of a likelihood ratio for the appropriate model, which is why the standard tests are optimal in their class rather than merely conventional.

For a normal sample with known variance, the likelihood ratio for $H_0: \mu = \mu_0$ against $H_1: \mu = \mu_1$ with $\mu_1 > \mu_0$ simplifies to a monotone function of $\bar{x}$, and therefore to a monotone function of $z$. The $z$ test is thus the most powerful test of its size for these simple hypotheses.

### 2.2 Monotone likelihood ratio and uniformly most powerful one-sided tests

A family of densities has a monotone likelihood ratio in a statistic $T$ if the ratio $f_{\theta_2}/f_{\theta_1}$ is a non-decreasing function of $T$ whenever $\theta_2 > \theta_1$.

> **Theorem (Karlin–Rubin).** If the family has a monotone likelihood ratio in $T$, then for testing $H_0: \theta \le \theta_0$ against $H_1: \theta > \theta_0$ the test that rejects for $T \ge c$ is uniformly most powerful of its size, and its power function is non-decreasing in $\theta$.

The exponent of the normal family with known variance is linear in the sufficient statistic, so the monotone likelihood ratio property holds with $T = \bar{x}$. The one-sided $z$ test is therefore uniformly most powerful among all level $\alpha$ tests, not merely the best among tests of the same algebraic form.

Two consequences are worth recording. First, the power function of a one-sided test is monotone, so the size is attained at the boundary $\theta = \theta_0$ and controlling the error probability there controls it throughout the null region. Second, no uniformly most powerful test exists for a two-sided alternative, because the direction of the best test depends on which side of the null the true value lies. The two-sided test is instead uniformly most powerful unbiased, or optimal within the symmetric class.

### 2.3 The distribution of the z statistic

> **Lemma (Null distribution of z).** For a random sample of size $n$ from a population with mean $\mu_0$ and known variance $\sigma^{2}$, the statistic

$$
z = \frac{\bar{x} - \mu_0}{\sigma/\sqrt{n}}
$$

has mean zero and variance one, and is exactly standard normal when the population is normal and approximately standard normal otherwise.

The exactness in the normal case follows because a linear combination of independent normal variables is normal. The approximation otherwise is the central limit theorem. The approximation is what licenses the large-sample use of the test, and its accuracy in the tails is what determines the accuracy of small p-values.

### 2.4 The distribution of the t statistic

When $\sigma$ is replaced by $s$, the resulting statistic has a distribution that does not depend on $\sigma$ but does depend on $n$.

> **Theorem (Student t).** If $Z$ is standard normal and $U$ is chi-square with $\nu$ degrees of freedom, and $Z$ and $U$ are independent, then

$$
T = \frac{Z}{\sqrt{U/\nu}}
$$

has the t distribution with $\nu$ degrees of freedom, with density

$$
f_T\left(t\right) = \frac{\Gamma\left(\frac{\nu + 1}{2}\right)}{\sqrt{\nu\pi}\,\Gamma\left(\frac{\nu}{2}\right)} \left(1 + \frac{t^{2}}{\nu}\right)^{-\frac{\nu + 1}{2}} .
$$

For a normal sample, $\left(\bar{x} - \mu\right)/\left(\sigma/\sqrt{n}\right)$ is standard normal and $\left(n - 1\right)s^{2}/\sigma^{2}$ is chi-square with $n - 1$ degrees of freedom. The two are independent, a fact proved in Section 3.2 by an orthogonal transformation. Substituting into the ratio gives

$$
t = \frac{\bar{x} - \mu}{s/\sqrt{n}} = \frac{\dfrac{\bar{x} - \mu}{\sigma/\sqrt{n}}}{\sqrt{\dfrac{\left(n - 1\right)s^{2}}{\sigma^{2}} \Big/ \left(n - 1\right)}} ,
$$

which is exactly the ratio form, with $n - 1$ degrees of freedom. The cancellation of $\sigma$ is the point of the construction: the statistic is a pivot even though $\sigma$ is unknown.

The density is symmetric about zero and has heavier tails than the standard normal, with the excess decaying as $\nu$ grows. The variance is $\nu/\left(\nu - 2\right)$ for $\nu > 2$, which exceeds one and approaches one from above, another expression of the same extra variability.

### 2.5 The chi-square distribution and the degrees of freedom of a goodness-of-fit test

> **Theorem (Sum of squared standard normals).** If $Z_1, \dots, Z_k$ are independent standard normal variables, then $\sum_{i=1}^{k} Z_i^{2}$ has the chi-square distribution with $k$ degrees of freedom.

Pearson's statistic is a sum of squares of standardised cell deviations, but the deviations are not independent, because they must sum to zero. The dependence costs exactly one degree of freedom, and the general statement is a quadratic form in a singular covariance matrix.

> **Theorem (Pearson).** For a multinomial sample of size $n$ with cell probabilities $p_1, \dots, p_k$, the statistic

$$
\chi^{2} = \sum_{i=1}^{k} \frac{\left(O_i - np_i\right)^{2}}{np_i}
$$

converges in distribution to a chi-square variable with $k - 1$ degrees of freedom as $n \to \infty$ with all $np_i$ bounded away from zero.

If $m$ parameters are estimated from the data before the expected counts are computed, each estimated parameter costs one further degree of freedom, so the reference distribution is chi-square with $k - 1 - m$ degrees of freedom. The loss occurs because the fitted expected counts are closer to the observed counts than the true expected counts would be, and the statistic computed with fitted counts is correspondingly smaller on average.

### 2.6 The degrees of freedom of a contingency table

> **Theorem (Independence test).** For an $r \times c$ contingency table with fixed margins and $n \to \infty$, the statistic

$$
\chi^{2} = \sum_{i=1}^{r}\sum_{j=1}^{c} \frac{\left(O_{ij} - E_{ij}\right)^{2}}{E_{ij}}, \qquad E_{ij} = \frac{R_i C_j}{n}
$$

converges in distribution to a chi-square variable with $\left(r - 1\right)\left(c - 1\right)$ degrees of freedom under the null hypothesis of independence, where $R_i$ and $C_j$ are the row and column totals.

The degrees of freedom are the number of free cell probabilities under the alternative minus the number under the null. Under the alternative the $rc$ cell probabilities sum to one, leaving $rc - 1$ free parameters. Under independence each cell probability is a product of a row effect and a column effect, so there are $r - 1$ free row probabilities and $c - 1$ free column probabilities, leaving $r + c - 2$ free parameters. The difference is

$$
\left(rc - 1\right) - \left(r + c - 2\right) = rc - r - c + 1 = \left(r - 1\right)\left(c - 1\right) .
$$

The formula is not a convention to be memorised; it is a count of the restrictions that independence imposes. A $2 \times 2$ table imposes one restriction, hence one degree of freedom, and a $3 \times 2$ table imposes two.

### 2.7 The F distribution and the variance-ratio test

> **Theorem (Variance ratio).** Let $s_1^{2}$ and $s_2^{2}$ be sample variances from independent normal samples of sizes $n_1$ and $n_2$. Then

$$
F = \frac{s_1^{2}/\sigma_1^{2}}{s_2^{2}/\sigma_2^{2}}
$$

has the F distribution with $\nu_1 = n_1 - 1$ and $\nu_2 = n_2 - 1$ degrees of freedom, and under $H_0: \sigma_1^{2} = \sigma_2^{2}$ the statistic reduces to $s_1^{2}/s_2^{2}$.

The result follows from writing each sample variance as a scaled chi-square variable and forming the ratio of two independent scaled chi-square variables divided by their degrees of freedom. The $F$ density is skewed to the right, and its reciprocal is an $F$ variable with the degrees of freedom interchanged, which is why a table containing only upper points suffices for a two-sided test.

### 2.8 The duality between tests and confidence intervals

> **Theorem (Duality).** Let $C\left(x\right)$ be a $100\left(1 - \alpha\right)\%$ confidence set for $\theta$ constructed by inverting a family of level $\alpha$ tests. Then $\theta_0 \in C\left(x\right)$ if and only if the level $\alpha$ test does not reject $H_0: \theta = \theta_0$. Conversely, any family of level $\alpha$ tests for point nulls generates a confidence set with coverage $1 - \alpha$ by collecting the non-rejected values.

The proof is in Section 3.7 and consists of a single complement. The theorem is the reason a two-sided test and an interval never disagree, and it is the reason a report that gives both must give them at the same level.

### 2.9 Properties of the power function

> **Lemma (Shape of the power function).** For the two-sided z test of $H_0: \mu = \mu_0$ with known variance, the power function is

$$
\pi\left(\mu\right) = 1 - \Phi\left(z_{\alpha/2} - \delta\right) + \Phi\left(-z_{\alpha/2} - \delta\right), \qquad \delta = \frac{\sqrt{n}\left(\mu - \mu_0\right)}{\sigma} .
$$

Four properties follow by inspection.

At $\mu = \mu_0$ the two terms cancel to give $\pi\left(\mu_0\right) = \alpha$, so the size equals the level exactly.

The function is symmetric about $\mu_0$, because $\delta$ enters only through its square in the combination of the two terms.

The function increases as $\left| \delta \right|$ increases, so power improves with the distance from the null value, with the sample size and with the inverse of the standard deviation.

The function tends to one as $\left| \mu - \mu_0 \right| \to \infty$, because the rejection region eventually lies entirely above or below the alternative's distribution.

The one-sided power function is a single term, $\pi\left(\mu\right) = 1 - \Phi\left(z_{\alpha} - \delta\right)$ for an upper-tailed test, and it increases monotonically from $\alpha$ at the null value to one.

### 2.10 The p-value as a random variable

> **Lemma (Uniformity under the null).** If the test statistic is continuous and the null hypothesis is true, then the p-value has the uniform distribution on $\left(0, 1\right)$.

The argument is a change of variable. For a one-sided upper test the p-value is $p = 1 - F_0\left(T\right)$ where $F_0$ is the null distribution function. Then for $0 \le u \le 1$,

$$
\text{P}\left(p \le u\right) = \text{P}\left(1 - F_0\left(T\right) \le u\right) = \text{P}\left(T \ge F_0^{-1}\left(1 - u\right)\right) = u .
$$

Uniformity explains why a p-value below $0.05$ occurs exactly five per cent of the time under the null, and it explains why p-values are not directly comparable across studies with different designs: the distribution under the alternative depends on power, so a smaller p-value may reflect a larger effect or merely a larger sample.

It also warns against the practice of treating $0.049$ and $0.051$ as qualitatively different. Both are draws from a continuous distribution, and the threshold is a convention imposed on a continuum.

### 2.11 Summary of the principal results

The table compresses the theoretical results into the form in which they are applied.

| Result | Content | Consequence for practice |
| --- | --- | --- |
| Neyman–Pearson | likelihood ratio maximises power at fixed size | standard tests are optimal, not arbitrary |
| Karlin–Rubin | monotone likelihood ratio gives uniformly most powerful one-sided tests | one-sided tests are legitimate and powerful |
| Student t | ratio of normal to root mean square chi-square | t replaces z when variance is estimated |
| Pearson | standardised squared counts converge to chi-square | count data are tested by chi-square |
| Degrees of freedom | free parameters under alternative minus under null | $\left(r - 1\right)\left(c - 1\right)$ for a table |
| Duality | interval membership equals non-rejection | test and interval cannot disagree |
| Uniformity | p-value is uniform under the null | threshold $\alpha$ gives error rate $\alpha$ |

## 3. Formal Proofs, Derivations, and Methods

### 3.1 Derivation of the one-sample z test

Let $x_1, \dots, x_n$ be independent with mean $\mu$ and known variance $\sigma^{2}$. By linearity of expectation,

$$
\text{E}\left(\bar{x}\right) = \frac{1}{n}\sum_{i=1}^{n}\text{E}\left(x_i\right) = \mu ,
$$

and by independence of the summands,

$$
\text{Var}\left(\bar{x}\right) = \frac{1}{n^{2}}\sum_{i=1}^{n}\text{Var}\left(x_i\right) = \frac{n\sigma^{2}}{n^{2}} = \frac{\sigma^{2}}{n} .
$$

Standardising gives a variable with mean zero and variance one,

$$
Z = \frac{\bar{x} - \mu}{\sigma/\sqrt{n}}, \qquad \text{E}\left(Z\right) = 0, \quad \text{Var}\left(Z\right) = 1 .
$$

Under $H_0$ the mean is $\mu_0$, so the statistic used in the test is the same expression with $\mu$ replaced by $\mu_0$, and its distribution is the same. If the population is normal the distribution is exactly standard normal for every $n$; otherwise the central limit theorem gives convergence in distribution.

The rejection region follows from the alternative. For $H_1: \mu > \mu_0$ the region is $\left\{ Z \ge z_{\alpha} \right\}$, because large values of $\bar{x}$ are the outcomes the alternative predicts. For $H_1: \mu \ne \mu_0$ the region is $\left\{ \left| Z \right| \ge z_{\alpha/2} \right\}$, because both directions are evidence and the level is split.

### 3.2 Derivation of the t statistic and its exact distribution

Let the population be normal with mean $\mu$ and variance $\sigma^{2}$, and let $s^{2}$ be the unbiased sample variance. Two facts are needed: that $s^{2}$ is independent of $\bar{x}$, and that $\left(n - 1\right)s^{2}/\sigma^{2}$ is chi-square with $n - 1$ degrees of freedom.

For independence, write the deviations from the sample mean as a linear transformation of the centred observations. The transformation matrix that maps $\left(x_1 - \mu, \dots, x_n - \mu\right)$ to $\left(\bar{x} - \mu, x_1 - \bar{x}, \dots, x_n - \bar{x}\right)$ is orthogonal up to scale, so the transformed vector has independent normal components. The first component is $\bar{x} - \mu$ and the remaining components determine $s^{2}$, hence the independence.

For the chi-square law, note that

$$
\frac{\left(n - 1\right)s^{2}}{\sigma^{2}} = \sum_{i=1}^{n}\left(\frac{x_i - \bar{x}}{\sigma}\right)^{2} ,
$$

and that the vector of standardised deviations is the projection of a standard normal vector onto the subspace orthogonal to the vector of ones, a subspace of dimension $n - 1$. The squared length of that projection is a sum of squares of $n - 1$ independent standard normals, hence chi-square with $n - 1$ degrees of freedom.

Now form the ratio. The quantity

$$
\frac{\bar{x} - \mu}{\sigma/\sqrt{n}}
$$

is standard normal, and it is independent of the chi-square variable. Dividing by the square root of the chi-square variable over its degrees of freedom gives

$$
\frac{\dfrac{\bar{x} - \mu}{\sigma/\sqrt{n}}}{\sqrt{\dfrac{\left(n - 1\right)s^{2}}{\sigma^{2}} \Big/ \left(n - 1\right)}} = \frac{\bar{x} - \mu}{s/\sqrt{n}} ,
$$

which is the $t$ statistic, and which by definition of the $t$ distribution has $n - 1$ degrees of freedom.

### 3.3 Derivation of the test for a proportion

Let $X$ be binomial with parameters $n$ and $p$, and let $\hat{p} = X/n$. Then $\text{E}\left(\hat{p}\right) = p$ and $\text{Var}\left(\hat{p}\right) = p\left(1 - p\right)/n$.

Under $H_0: p = p_0$ the variance is fully determined, so the standardised statistic

$$
z = \frac{\hat{p} - p_0}{\sqrt{p_0\left(1 - p_0\right)/n}}
$$

has mean zero and variance one under the null. By the central limit theorem for binomial proportions, applied through the normal approximation to the binomial, $z$ converges in distribution to standard normal.

The same construction can be read as a score test. The log-likelihood for a single observation is $\ell\left(p\right) = x\log p + \left(1 - x\right)\log\left(1 - p\right)$, whose score at $p_0$ is $\left(x - p_0\right)/\left(p_0\left(1 - p_0\right)\right)$ and whose information is $1/\left(p_0\left(1 - p_0\right)\right)$. The score statistic divided by the root of $n$ times the information is exactly the $z$ above, which is another route to the same formula and explains why the null standard error must be used.

Replacing $p_0$ by $\hat{p}$ in the denominator produces the Wald statistic, whose distribution is closer to normal in the middle of the range but which behaves poorly near zero and one because the estimated variance can collapse.

### 3.4 Derivation of Pearson's chi-square statistic

Let $O = \left(O_1, \dots, O_k\right)$ be multinomial with parameters $n$ and $p = \left(p_1, \dots, p_k\right)$. Define the standardised deviations

$$
Y_i = \frac{O_i - np_i}{\sqrt{np_i}} .
$$

The means are zero. For the variances, since $O_i$ is binomial with parameters $n$ and $p_i$,

$$
\text{Var}\left(Y_i\right) = \frac{np_i\left(1 - p_i\right)}{np_i} = 1 - p_i .
$$

For the covariances, since $\text{Cov}\left(O_i, O_j\right) = -np_ip_j$ for $i \ne j$,

$$
\text{Cov}\left(Y_i, Y_j\right) = \frac{-np_ip_j}{\sqrt{np_i}\sqrt{np_j}} = -\sqrt{p_ip_j} .
$$

Hence the covariance matrix of $Y$ is $\Sigma = I - qq^{T}$ where $q$ has entries $\sqrt{p_i}$. The vector $q$ has unit length, so $\Sigma q = q - q\left(q^{T}q\right) = 0$, and on the orthogonal complement of $q$ the matrix acts as the identity. Its eigenvalues are therefore $0$ once and $1$ a total of $k - 1$ times.

By the multivariate central limit theorem, $Y$ converges in distribution to a normal vector with covariance $\Sigma$. A quadratic form $Y^{T}Y$ in such a vector has, in the limit, the distribution of a sum of squares of independent standard normals, one for each non-zero eigenvalue. There are $k - 1$ of them, so

$$
\chi^{2} = \sum_{i=1}^{k} Y_i^{2} = \sum_{i=1}^{k}\frac{\left(O_i - np_i\right)^{2}}{np_i} \xrightarrow{d} \chi^{2}_{k-1} .
$$

This is the derivation of both the formula and its degrees of freedom. The statistic is the squared length of a vector constrained to a subspace of dimension $k - 1$, and the dimension of that subspace is exactly the degrees of freedom.

### 3.5 Derivation of the degrees of freedom in a contingency table

Let the table have $r$ rows and $c$ columns and let $p_{ij}$ be the cell probabilities, with $n$ fixed.

Under the general multinomial model the parameters are the $rc$ cell probabilities subject to the single constraint $\sum_{ij} p_{ij} = 1$, giving $rc - 1$ free parameters.

Under independence, $p_{ij} = p_{i\cdot}p_{\cdot j}$, where the row probabilities satisfy $\sum_i p_{i\cdot} = 1$ and the column probabilities satisfy $\sum_j p_{\cdot j} = 1$. The number of free parameters is therefore $\left(r - 1\right) + \left(c - 1\right) = r + c - 2$.

The number of restrictions that independence imposes is the difference,

$$
\left(rc - 1\right) - \left(r + c - 2\right) = rc - r - c + 1 = \left(r - 1\right)\left(c - 1\right) .
$$

Each restriction removes one dimension from the space in which the standardised deviations live, and by the same quadratic-form argument as in Section 3.4 the squared length of a vector in the remaining $\left(r - 1\right)\left(c - 1\right)$ dimensional subspace is asymptotically chi-square with that many degrees of freedom.

The expected counts $E_{ij} = R_iC_j/n$ are the maximum likelihood estimates under independence, which is why the statistic is computed with them rather than with the true $np_{ij}$: the true values contain unknown parameters, and substituting the estimates costs no additional degrees of freedom here because the margins are treated as fixed.

### 3.6 Derivation of the F statistic

For a normal sample of size $n_1$, the quantity $\left(n_1 - 1\right)s_1^{2}/\sigma_1^{2}$ is chi-square with $n_1 - 1$ degrees of freedom, and similarly for the second sample. Independence of the samples makes the two chi-square variables independent.

> **Definition (F distribution).** If $U$ and $V$ are independent chi-square variables with $\nu_1$ and $\nu_2$ degrees of freedom, then $F = \left(U/\nu_1\right)/\left(V/\nu_2\right)$ has the F distribution with $\left(\nu_1, \nu_2\right)$ degrees of freedom.

Substituting the scaled sample variances gives

$$
F = \frac{\dfrac{\left(n_1 - 1\right)s_1^{2}}{\sigma_1^{2}\left(n_1 - 1\right)}}{\dfrac{\left(n_2 - 1\right)s_2^{2}}{\sigma_2^{2}\left(n_2 - 1\right)}} = \frac{s_1^{2}/\sigma_1^{2}}{s_2^{2}/\sigma_2^{2}} .
$$

Under $H_0: \sigma_1^{2} = \sigma_2^{2}$ the unknown variances cancel and the statistic becomes $s_1^{2}/s_2^{2}$, whose distribution is free of all unknowns. Large values indicate that the first population is more variable, small values that it is less variable.

### 3.7 Proof of the duality between tests and intervals

Let $\hat{\theta}$ be an estimator with standard error $\text{SE}$ and suppose the standardised quantity has a symmetric distribution with critical value $c$ at level $\alpha$. The two-sided test of $H_0: \theta = \theta_0$ rejects when

$$
\frac{\left| \hat{\theta} - \theta_0 \right|}{\text{SE}} > c .
$$

This inequality is equivalent, by multiplying through by the positive $\text{SE}$, to

$$
\left| \hat{\theta} - \theta_0 \right| > c\,\text{SE} ,
$$

which in turn is the negation of

$$
\hat{\theta} - c\,\text{SE} \le \theta_0 \le \hat{\theta} + c\,\text{SE} .
$$

The set of $\theta_0$ satisfying the last inequality is precisely the confidence interval $\left[ \hat{\theta} - c\,\text{SE}, \hat{\theta} + c\,\text{SE} \right]$. Therefore

$$
\text{reject } H_0 \iff \theta_0 \notin \left[ L, U \right] .
$$

Taking probabilities under the true value $\theta_0$,

$$
\text{P}_{\theta_0}\left(\theta_0 \in \left[ L, U \right]\right) = 1 - \text{P}_{\theta_0}\left(\text{reject}\right) = 1 - \alpha ,
$$

so the interval has coverage $1 - \alpha$ exactly when the test has size $\alpha$. The argument is reversible, which gives the converse construction: the set of null values not rejected at level $\alpha$ is a $100\left(1 - \alpha\right)\%$ confidence set.

### 3.8 Derivation of the power function and the sample size formula

Consider the two-sided z test with rejection region $\left| z \right| > z_{\alpha/2}$ and let the true mean be $\mu$. Define the non-centrality parameter

$$
\delta = \frac{\sqrt{n}\left(\mu - \mu_0\right)}{\sigma} .
$$

The statistic $z$ has a normal distribution with mean $\delta$ and variance one under $\mu$, so

$$
\pi\left(\mu\right) = \text{P}\left(z > z_{\alpha/2}\right) + \text{P}\left(z < -z_{\alpha/2}\right) = 1 - \Phi\left(z_{\alpha/2} - \delta\right) + \Phi\left(-z_{\alpha/2} - \delta\right) .
$$

At $\delta = 0$ the two terms are $\Phi\left(-z_{\alpha/2}\right)$ and $\Phi\left(-z_{\alpha/2}\right)$, which sum to $\alpha$ by the definition of the critical value.

For the sample size, let the alternative of interest be $\mu_1 > \mu_0$ and let the required power be $1 - \beta$. Ignoring the negligible lower tail, the requirement is

$$
1 - \Phi\left(z_{\alpha/2} - \delta\right) \ge 1 - \beta ,
$$

which is $z_{\alpha/2} - \delta \le -z_{\beta}$, or $\delta \ge z_{\alpha/2} + z_{\beta}$. Substituting the definition of $\delta$ and solving for $n$ gives

$$
n \ge \frac{\left(z_{\alpha/2} + z_{\beta}\right)^{2}\sigma^{2}}{\left(\mu_1 - \mu_0\right)^{2}} .
$$

For a one-sided test the single critical value $z_{\alpha}$ replaces $z_{\alpha/2}$, which reduces the required sample size, and for a paired design $\sigma$ is replaced by the standard deviation of the differences.

### 3.9 The procedure written as a fixed algorithm

The method below is the order in which the steps must be executed; the numbering is not cosmetic, because steps 1 to 3 must precede any inspection of the data.

Step 1. Identify the parameter, its null value and the alternative, and write the hypotheses in symbols with a sentence of interpretation.

Step 2. State the model assumptions and select the statistic whose null distribution is known under those assumptions.

Step 3. Fix the level $\alpha$ and obtain the critical value or values for the correct number of tails and the correct degrees of freedom.

Step 4. Compute the standard error and the statistic, reporting them separately.

Step 5. Decide, by comparing the statistic with the critical value or the p-value with $\alpha$.

Step 6. Interpret the decision in the language of the problem, stating the population, the direction and the level, and adding what the decision does not establish.

## 4. Representative Worked Examples and Solutions

### 4.1 Problem: a two-sided z test with the interval check

A filling machine has a known standard deviation of $8$ grams. A sample of $49$ packets has a mean mass of $502.5$ grams, and the target mean is $500$ grams. Test at the $5\%$ level whether the mean differs from the target, and confirm the conclusion with a confidence interval.

### 4.2 Solution: statistic, p-value and interval

Step 1. State the hypotheses.

$$
H_0: \mu = 500, \qquad H_1: \mu \ne 500 .
$$

Step 2. Compute the standard error.

$$
\text{SE} = \frac{8}{\sqrt{49}} = \frac{8}{7} = 1.142857 .
$$

Step 3. Compute the statistic.

$$
z = \frac{502.5 - 500}{1.142857} = \frac{2.5}{1.142857} = 2.1875 .
$$

Step 4. Compare with the critical values $\pm 1.96$. Since $2.1875 > 1.96$, reject $H_0$.

Step 5. Compute the two-sided p-value.

$$
p = 2\left(1 - \Phi\left(2.1875\right)\right) = 2 \times 0.01435 = 0.0287 .
$$

Step 6. Construct the $95\%$ interval.

$$
502.5 \pm 1.96 \times 1.142857 = 502.5 \pm 2.24 ,
$$

so the interval is from $500.26$ to $504.74$.

Step 7. Check the duality. The null value $500$ lies outside the interval, which is exactly the statement that the test rejects. The two procedures agree because they are the same inequality.

Step 8. Interpret. There is evidence at the $5\%$ level that the mean mass differs from $500$ grams, and the interval suggests the true mean lies between about $500.3$ and $504.7$ grams.

### 4.3 Problem: a one-sided test and its power function

A component has a known standard deviation of $10$ units and a target mean of $100$. A sample of $25$ is taken and the test is $H_0: \mu = 100$ against $H_1: \mu > 100$ at the $5\%$ level. State the rejection region in terms of the sample mean, compute the power at true means of $101$, $102$, $104$ and $106$, and find the sample size needed for power $0.90$ at a true mean of $104$.

### 4.4 Solution: translating the region and computing power

Step 1. Compute the standard error.

$$
\text{SE} = \frac{10}{\sqrt{25}} = 2 .
$$

Step 2. Write the rejection region for the statistic, using the one-sided critical value $1.645$.

$$
z > 1.645 \iff \bar{x} > 100 + 1.645 \times 2 = 103.29 .
$$

Step 3. Express the power at a true mean $\mu$ as a normal probability with standard error two.

$$
\pi\left(\mu\right) = \text{P}\left(\bar{x} > 103.29\right) = 1 - \Phi\left(\frac{103.29 - \mu}{2}\right) .
$$

Step 4. Evaluate at $\mu = 101$.

$$
\pi\left(101\right) = 1 - \Phi\left(1.145\right) = 1 - 0.874 = 0.126 .
$$

Step 5. Evaluate at $\mu = 102$.

$$
\pi\left(102\right) = 1 - \Phi\left(0.645\right) = 1 - 0.740 = 0.260 .
$$

Step 6. Evaluate at $\mu = 104$.

$$
\pi\left(104\right) = 1 - \Phi\left(-0.355\right) = 0.639 .
$$

Step 7. Evaluate at $\mu = 106$.

$$
\pi\left(106\right) = 1 - \Phi\left(-1.355\right) = 0.912 .
$$

Step 8. Compute the sample size for power $0.90$ at $\mu = 104$.

$$
n \ge \frac{\left(1.645 + 1.2816\right)^{2} \times 100}{\left(104 - 100\right)^{2}} = \frac{8.565 \times 100}{16} = 53.5 ,
$$

so $54$ observations are required.

Step 9. Interpret. The test is weak at a departure of one or two units, because such a departure is only half a standard error or one standard error away from the null value. Power reaches $0.912$ only at a departure of six units, and obtaining good power at four units requires more than doubling the sample.

### 4.5 Problem: a one-sample t test

A sample of $10$ measurements from a normal process has mean $25.4$ and standard deviation $4.2$. Test at the $5\%$ level whether the mean exceeds $22$.

### 4.6 Solution: a t test with nine degrees of freedom

Step 1. State the hypotheses.

$$
H_0: \mu = 22, \qquad H_1: \mu > 22 .
$$

Step 2. Compute the standard error.

$$
\frac{s}{\sqrt{n}} = \frac{4.2}{\sqrt{10}} = \frac{4.2}{3.1623} = 1.3282 .
$$

Step 3. Compute the statistic.

$$
t = \frac{25.4 - 22}{1.3282} = \frac{3.4}{1.3282} = 2.560 .
$$

Step 4. Obtain the critical value. On $9$ degrees of freedom the one-sided $5\%$ point is $1.833$.

Step 5. Compare. Since $2.560 > 1.833$, reject $H_0$.

Step 6. Bound the p-value from tables. The one-sided $2.5\%$ point is $2.262$ and the $1\%$ point is $2.821$, so $0.01 < p < 0.025$; the exact value is $0.0153$.

Step 7. Interpret. The mean exceeds $22$ at the $5\%$ level. Note that a $z$ test would have given $z = 2.560$ against a critical value of $1.645$, also rejecting, but the margin would have been overstated.

### 4.7 Problem: a paired t test

Ten workers are timed on two methods of assembling a unit, and the differences in time, method A minus method B, are $1.0$, $0.5$, $0.9$, $-0.2$, $0.6$, $0.0$, $0.8$, $0.3$, $-0.1$ and $0.2$ minutes. Test at the $5\%$ level whether the two methods differ in mean time.

### 4.8 Solution: reducing the design to a one-sample problem

Step 1. State the hypotheses in terms of the mean difference $\mu_d$.

$$
H_0: \mu_d = 0, \qquad H_1: \mu_d \ne 0 .
$$

Step 2. Compute the mean difference.

$$
\bar{d} = \frac{1.0 + 0.5 + 0.9 - 0.2 + 0.6 + 0.0 + 0.8 + 0.3 - 0.1 + 0.2}{10} = \frac{4.0}{10} = 0.40 .
$$

Step 3. Compute the sum of squared deviations from the mean difference.

$$
\sum \left(d_i - \bar{d}\right)^{2} = 1.64 .
$$

Step 4. Compute the sample variance and standard deviation of the differences.

$$
s_d^{2} = \frac{1.64}{9} = 0.1822, \qquad s_d = 0.4269 .
$$

Step 5. Compute the standard error.

$$
\frac{s_d}{\sqrt{10}} = \frac{0.4269}{3.1623} = 0.1350 .
$$

Step 6. Compute the statistic with nine degrees of freedom.

$$
t = \frac{0.40}{0.1350} = 2.963 .
$$

Step 7. Compare with the two-sided $5\%$ critical value $2.262$. Since $2.963 > 2.262$, reject $H_0$.

Step 8. Report the p-value, which is approximately $0.016$.

Step 9. Interpret. The methods differ in mean time, and the paired design is what makes the test sensitive: the between-worker variation is removed by differencing, so the standard error refers only to the variability of the differences.

### 4.9 Problem: a two-sample t test with a pooled variance

Two production methods are compared. Method A gives times $12$, $15$, $14$, $11$ and $13$; method B gives $16$, $18$, $15$, $17$ and $19$. Test at the $5\%$ level whether the mean times differ, assuming equal population variances.

### 4.10 Solution: pooling and testing

Step 1. Compute the sample means.

$$
\bar{x}_A = \frac{12 + 15 + 14 + 11 + 13}{5} = \frac{65}{5} = 13, \qquad \bar{x}_B = \frac{16 + 18 + 15 + 17 + 19}{5} = \frac{85}{5} = 17 .
$$

Step 2. Compute the sample variances.

$$
s_A^{2} = \frac{1 + 4 + 1 + 4 + 0}{4} = 2.5, \qquad s_B^{2} = \frac{1 + 1 + 4 + 0 + 4}{4} = 2.5 .
$$

Step 3. Compute the pooled variance with $5 + 5 - 2 = 8$ degrees of freedom.

$$
s_p^{2} = \frac{4 \times 2.5 + 4 \times 2.5}{8} = \frac{20}{8} = 2.5 .
$$

Step 4. Compute the standard error of the difference.

$$
\text{SE} = \sqrt{s_p^{2}\left(\frac{1}{5} + \frac{1}{5}\right)} = \sqrt{2.5 \times 0.4} = \sqrt{1} = 1 .
$$

Step 5. Compute the statistic.

$$
t = \frac{13 - 17}{1} = -4 .
$$

Step 6. Compare with the two-sided critical value $2.306$ on $8$ degrees of freedom. Since $\left| -4 \right| > 2.306$, reject $H_0$.

Step 7. Report the p-value, which is approximately $0.004$.

Step 8. Interpret. The mean times differ, and method B is slower by about four units. The equal-variance assumption is supported by the two sample variances being identical, which is why pooling is reasonable here.

### 4.11 Problem: a test for a proportion

In a sample of $400$ customers, $232$ say they would recommend a product. Test at the $5\%$ level whether the population proportion differs from $0.55$.

### 4.12 Solution: a score statistic with a null standard error

Step 1. State the hypotheses.

$$
H_0: p = 0.55, \qquad H_1: p \ne 0.55 .
$$

Step 2. Compute the sample proportion.

$$
\hat{p} = \frac{232}{400} = 0.58 .
$$

Step 3. Compute the null standard error.

$$
\text{SE}_0 = \sqrt{\frac{0.55 \times 0.45}{400}} = \sqrt{0.00061875} = 0.024875 .
$$

Step 4. Check the approximation.

$$
np_0 = 220, \qquad n\left(1 - p_0\right) = 180 ,
$$

both far above the threshold of ten.

Step 5. Compute the statistic.

$$
z = \frac{0.58 - 0.55}{0.024875} = \frac{0.03}{0.024875} = 1.206 .
$$

Step 6. Compare with $1.96$. Since $1.206 < 1.96$, do not reject $H_0$.

Step 7. Compute the p-value.

$$
p = 2\left(1 - \Phi\left(1.206\right)\right) = 2 \times 0.1139 = 0.2278 .
$$

Step 8. Interpret. The data are consistent with a population proportion of $0.55$. The observed excess of three percentage points is only about $1.2$ standard errors, well inside the range that sampling variation produces.

### 4.13 Problem: a goodness-of-fit test

A random sample of $100$ respondents chooses among three brands, with counts $48$, $32$ and $20$. Test at the $5\%$ level whether the three brands are equally preferred.

### 4.14 Solution: three categories and two degrees of freedom

Step 1. State the hypotheses.

$$
H_0: p_1 = p_2 = p_3 = \frac{1}{3}, \qquad H_1: \text{not all three proportions are equal} .
$$

Step 2. Compute the common expected count.

$$
E_i = 100 \times \frac{1}{3} = 33.333 \quad \text{for each brand} .
$$

Step 3. Compute the three contributions.

$$
\frac{\left(48 - 33.333\right)^{2}}{33.333} = 6.453, \qquad \frac{\left(32 - 33.333\right)^{2}}{33.333} = 0.053, \qquad \frac{\left(20 - 33.333\right)^{2}}{33.333} = 5.333 .
$$

Step 4. Add them.

$$
\chi^{2} = 6.453 + 0.053 + 5.333 = 11.84 .
$$

Step 5. Determine the degrees of freedom, with no parameter estimated from the data.

$$
\nu = 3 - 1 = 2 .
$$

Step 6. Compare with the critical value $5.991$. Since $11.84 > 5.991$, reject $H_0$.

Step 7. Report the p-value, which is approximately $0.0027$.

Step 8. Interpret. Preference is not uniform. The largest contributions come from the first and third brands, whose counts of $48$ and $20$ depart most from the common expected count of $33.3$.

### 4.15 Problem: a test of independence in a three-by-two table

A quality record classifies $250$ units by shift and by whether the unit was defective. The counts are $12$ defective among $90$ morning units, $8$ among $80$ afternoon units and $20$ among $80$ night units. Test at the $5\%$ level whether defect status is independent of shift.

### 4.16 Solution: expected counts, statistic and degrees of freedom

Step 1. State the hypotheses. The null is independence of the two classifications.

Step 2. Assemble the totals.

| Shift | Defective | Not defective | Row total |
| --- | --- | --- | --- |
| Morning | 12 | 78 | 90 |
| Afternoon | 8 | 72 | 80 |
| Night | 20 | 60 | 80 |
| Column total | 40 | 210 | 250 |

Step 3. Compute the expected defective counts as row total times column total over the grand total.

$$
E_{11} = \frac{90 \times 40}{250} = 14.4, \qquad E_{21} = \frac{80 \times 40}{250} = 12.8, \qquad E_{31} = \frac{80 \times 40}{250} = 12.8 .
$$

Step 4. Compute the expected non-defective counts by subtraction within each row.

$$
E_{12} = 90 - 14.4 = 75.6, \qquad E_{22} = 80 - 12.8 = 67.2, \qquad E_{32} = 80 - 12.8 = 67.2 .
$$

Step 5. Compute each contribution.

$$
\frac{\left(12 - 14.4\right)^{2}}{14.4} = 0.400, \qquad \frac{\left(78 - 75.6\right)^{2}}{75.6} = 0.076 ,
$$

$$
\frac{\left(8 - 12.8\right)^{2}}{12.8} = 1.800, \qquad \frac{\left(72 - 67.2\right)^{2}}{67.2} = 0.343 ,
$$

$$
\frac{\left(20 - 12.8\right)^{2}}{12.8} = 4.050, \qquad \frac{\left(60 - 67.2\right)^{2}}{67.2} = 0.771 .
$$

Step 6. Add the six contributions.

$$
\chi^{2} = 0.400 + 0.076 + 1.800 + 0.343 + 4.050 + 0.771 = 7.440 .
$$

Step 7. Determine the degrees of freedom.

$$
\nu = \left(3 - 1\right)\left(2 - 1\right) = 2 .
$$

Step 8. Compare with $5.991$. Since $7.440 > 5.991$, reject $H_0$.

Step 9. Report the p-value, approximately $0.024$, and interpret. Defect status is associated with shift. The association is driven by the night shift, where $20$ defectives were observed against $12.8$ expected, and the morning shift, which has fewer defectives than expected.

### 4.17 Problem: comparing two variances

Two suppliers deliver components measured on a normal scale. A sample of $25$ from supplier one gives a variance of $36$, and a sample of $16$ from supplier two gives a variance of $12$. Test at the $5\%$ level whether the population variances differ.

### 4.18 Solution: the variance ratio and its two degrees of freedom

Step 1. State the hypotheses.

$$
H_0: \sigma_1^{2} = \sigma_2^{2}, \qquad H_1: \sigma_1^{2} \ne \sigma_2^{2} .
$$

Step 2. Compute the ratio with the larger variance in the numerator.

$$
F = \frac{36}{12} = 3.00 .
$$

Step 3. Record the degrees of freedom.

$$
\nu_1 = 25 - 1 = 24, \qquad \nu_2 = 16 - 1 = 15 .
$$

Step 4. Obtain the upper critical value for a two-sided test at $5\%$, which uses the $2.5\%$ upper point of the $F$ distribution.

$$
F_{0.025, 24, 15} = 2.701 .
$$

Step 5. Compare. Since $3.00 > 2.701$, reject $H_0$.

Step 6. Report the p-value, approximately $0.016$.

Step 7. Interpret. The evidence indicates that the two population variances differ, with supplier one the more variable. The conclusion depends heavily on the normality assumption, because the $F$ test is not robust to heavy tails.

### 4.19 Problem: an interval and a test that must agree

A sample of $36$ observations from a normal population has mean $52.4$ and standard deviation $6.0$. Construct the $95\%$ interval for the mean and test $H_0: \mu = 50$ against a two-sided alternative at the $5\%$ level.

### 4.20 Solution: one calculation read two ways

Step 1. Compute the standard error with $35$ degrees of freedom.

$$
\frac{s}{\sqrt{n}} = \frac{6.0}{6} = 1.00 .
$$

Step 2. Obtain the critical value $t_{0.025, 35} = 2.030$.

Step 3. Construct the interval.

$$
52.4 \pm 2.030 \times 1.00 = \left[50.37, 54.43\right] .
$$

Step 4. Test by the interval. Since $50$ lies outside the interval, reject $H_0$.

Step 5. Confirm by the statistic.

$$
t = \frac{52.4 - 50}{1.00} = 2.40, \qquad 2.40 > 2.030 .
$$

Step 6. Interpret. The two procedures agree by the duality theorem, not by coincidence. Note also that a $99\%$ interval would be $52.4 \pm 2.724 = \left[49.68, 55.12\right]$, which contains $50$, and correspondingly the $1\%$ two-sided test would not reject.

## 5. Mathematical Extensions, Limits, and Common Errors

### 5.1 The misinterpretations of the p-value

The p-value is the most widely misread statistic in applied work, and the misreadings are systematic rather than random.

It is not the probability that the null hypothesis is true. A p-value of $0.03$ does not mean there is a three per cent chance that $H_0$ holds. It means that a result at least this extreme would arise three per cent of the time if $H_0$ held. The two statements differ by a Bayesian inversion that requires a prior, and in realistic settings the difference can be enormous: with a prior probability of $0.5$ on the null, a p-value of $0.05$ can still leave the null more probable than not.

It is not the probability that the result was due to chance. Chance is not a hypothesis that can be given a probability in this framework; the p-value conditions on the null, and the null is a statement about the parameter, not about the mechanism.

The complement of the p-value is not the probability that the result will replicate. Replication depends on the power of the original study, and a p-value just below the threshold is, by the uniformity lemma, the least reproducible kind of result.

It is not a measure of effect size. A p-value combines the size of the departure with the precision of the estimate, so a tiny effect measured with great precision can produce a smaller p-value than a large effect measured badly.

It is not comparable across different test statistics without care. A p-value from a one-sided test is a different quantity from a p-value from a two-sided test on the same data, and mixing them across a literature produces a bias in the apparent strength of evidence.

### 5.2 The inferential errors that follow from a misinterpreted p-value

The first inferential error is treating non-rejection as evidence of equality. "No significant difference" is compatible with a large true difference that the sample was too small to detect, and the correct statement is a statement about the data, not about the parameter.

The second is the fallacy of the transposed conditional, in which $\text{P}\left(\text{data} \mid H_0\right)$ is read as $\text{P}\left(H_0 \mid \text{data}\right)$. The two are related only through Bayes' theorem, and the base rate of true nulls across a field of study dominates the conversion.

The third is the error of accepting the null when a one-sided test in the wrong direction fails to reject. A one-sided test has essentially no power in the direction it ignores, so its failure there says nothing.

The fourth is the error of interpreting a confidence interval as a probability statement about the parameter. As established in the estimation theory, coverage is a property of the procedure; a realised interval either contains the parameter or does not.

### 5.3 Multiplicity and the inflation of the error rate

If $m$ independent hypotheses are each tested at level $\alpha$, the probability of at least one false rejection is $1 - \left(1 - \alpha\right)^{m}$, which rises quickly. With $m = 20$ and $\alpha = 0.05$ the probability is $0.64$, so a study that tests twenty null hypotheses will usually report at least one spurious "significant" finding.

The Bonferroni correction replaces $\alpha$ by $\alpha/m$, which controls the probability of any false rejection at $\alpha$ but is conservative when the tests are correlated. The Holm procedure applies the same correction sequentially and is uniformly more powerful. Modern practice also reports false discovery rate control, which bounds the expected proportion of false rejections among the rejected hypotheses rather than the probability of any false rejection.

Multiplicity also explains why a result that is significant in one study and not in another need not be contradictory. Two studies of the same effect differ in power, and a smaller study will fail to reach significance more often even when the effect is real.

### 5.4 Limits of the standard tests

Every test in this topic is a large-sample or normal-theory approximation, and each has a regime in which the approximation fails.

The $z$ test fails when the population is strongly skewed and the sample is small, because the central limit theorem has not yet taken effect. The failure is worst in the tail, so a nominal $1\%$ test may have an actual size several times larger.

The $t$ test requires normality for exactness and is sensitive to outliers through $s$. A single wild observation inflates the standard deviation and can mask a real effect, or, if it lies in the direction of the alternative, can create one.

The chi-square tests require expected counts of at least about five. With smaller counts the discreteness of the multinomial distribution becomes important and the nominal p-value is inaccurate. Exact conditional tests, such as Fisher's exact test for a two-by-two table, avoid the approximation.

The $F$ test for variances is the least robust of the group. It assumes normal populations and is severely distorted by heavy tails; a test with nominal size $5\%$ can have actual size above $20\%$ for $t$ distributed data with four degrees of freedom.

No test repairs a biased sample. Every p-value in this topic is computed under a model that includes random sampling, and if the sample is a convenience sample the model is false and the stated error rates are fictions.

### 5.5 Power in the design of a study

Power analysis belongs before the data are collected, and it answers a question that the test itself cannot: how large a sample is needed to make the test informative?

The ingredients are the level, the desired power, the standard deviation and the smallest departure worth detecting. The last of these is a scientific judgement, not a statistical one, and choosing it too small produces an unaffordable sample while choosing it too large produces a study that cannot detect anything important.

A study with power $0.80$ has a Type II error probability of $0.20$, which is four times the Type I error probability at the conventional level. This asymmetry is deliberate only when a missed effect is cheaper than a false alarm. When a missed effect is the more costly error, power should be set higher.

Post hoc power, computed from the observed effect after the study is finished, is a transformed p-value and adds no information. The legitimate use of power is prospective.

### 5.6 Extensions that generalise the framework

The likelihood ratio test generalises every procedure in this topic. For a null that fixes some parameters, the statistic $-2\log\Lambda$ compares the maximised log-likelihood under the null with the maximised log-likelihood overall, and it converges to a chi-square distribution with degrees of freedom equal to the number of restrictions. All the tests above are special cases, and the chi-square degrees-of-freedom rules follow from counting restrictions.

Analysis of variance extends the two-sample comparison to three or more groups. The $F$ statistic compares the variability between group means with the variability within groups, and the null hypothesis is that all group means are equal. The two-sample $t$ test is the special case of two groups, and the two statistics satisfy $F = t^{2}$.

Resampling methods replace the reference distribution by an empirical one. The permutation test recomputes the statistic under random reassignments of the labels, and the bootstrap resamples the data with replacement; both avoid the normal-theory approximations and are the standard remedies when the sample is small or the distribution is unknown.
