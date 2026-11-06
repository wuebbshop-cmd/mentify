## 1. Foundational Concepts, Definitions, and Axioms

### 1.1 A courtroom in your head

Imagine a courtroom where a single question must be settled: did the accused do the thing, or not? The law answers with a deliberate asymmetry. Nobody begins by assuming guilt. The court begins by presuming innocence, and it places the whole burden of proof on the prosecution. The defence does not have to prove innocence; it has only to raise doubt. If the prosecution's evidence survives every reasonable objection, the verdict is guilty. If it does not, the verdict is not guilty, and that verdict is not a declaration of innocence. It is a statement that the evidence was too weak to overturn the presumption.

Picture the same structure applied to a number instead of a person. A factory claims that its machine fills each packet with 500 grams of tea. An inspector suspects the machine is overfilling. The inspector cannot weigh every packet ever produced, because that would destroy the product and take forever. So the inspector weighs a sample, computes the sample mean, and asks a sharper question: if the machine really were filling to 500 grams on average, how surprising would a sample mean of this size be? That question, and nothing else, is the engine of hypothesis testing.

Think of the presumption of innocence as a starting position that the data must dislodge. That starting position is called the null hypothesis. Think of the claim the investigator wants to establish as the alternative hypothesis. Think of the standard of proof as a threshold fixed before the evidence is examined; that threshold is the significance level. Think of the strength of the evidence as a single number computed from the sample; that number is the test statistic. Think of the verdict as one of exactly two words: reject, or do not reject.

The analogy is not decoration. Every rule in this topic follows from it. The presumption is never proved, only retained or abandoned. Absence of evidence is not evidence of absence. A stricter standard of proof makes wrongful convictions rarer and missed convictions commoner, and no amount of clever argument removes that trade-off. An investigator who understands the courtroom already understands the statistics.

### 1.2 What a hypothesis is in statistics

A hypothesis in statistics is a statement about a population, not about a sample. "The mean fill of all packets is 500 grams" is a hypothesis. "The mean fill of the forty packets I weighed is 498.6 grams" is a measurement, not a hypothesis, because it can be checked by looking at the data and involves no uncertainty.

A hypothesis is called simple when it names one exact value of the parameter, and composite when it allows a range. The statement that the population mean $\mu$ equals $500$ is simple. The statement that $\mu$ exceeds $500$ is composite, because it is true for infinitely many values.

Two hypotheses are set against each other.

> **Definition (Null hypothesis).** The null hypothesis, written $H_0$, is the statement that is presumed true at the start of the investigation. It usually says that nothing has changed, that there is no effect, or that a parameter takes a specified value.

> **Definition (Alternative hypothesis).** The alternative hypothesis, written $H_1$, is the statement that the investigator hopes or fears is true. It is the claim that must be supported by evidence strong enough to dislodge $H_0$.

The two must be mutually exclusive and, between them, exhaustive, so that exactly one of them is true in reality. If $H_0$ says the mean is $500$ and $H_1$ says the mean is not $500$, one of them is true and the other false, with no gap. Writing them so that they overlap, or so that a gap remains, is a common and costly beginner error.

The word "null" does not mean "nothing happens". It means "no departure from the stated value". The word "alternative" does not mean "the opposite"; it means "the set of values left over once the null value is removed", and that set can be one-sided or two-sided.

The whole procedure is the statistical form of proof by contradiction. In pure mathematics one assumes a statement, deduces a consequence, and shows the consequence is impossible; the assumption then falls. In statistics the deduction is probabilistic rather than certain, so the final step is softened: one assumes the null hypothesis, deduces that a result like the observed one has a small probability, and concludes that the assumption is hard to maintain. Because the deduction is only improbable rather than impossible, the conclusion is a decision with a known error rate rather than a proof. That single difference is why every test carries a significance level and why no test ever delivers certainty.

### 1.3 Why the null gets the presumption

It is worth asking why the null hypothesis receives the presumption of innocence and the alternative receives the burden of proof. The answer is that the null is the position that will be defended by default, and a default must be stable. If the null were rejected on flimsy evidence, every routine measurement would generate a dramatic announcement. Fixing the null as the presumption forces the data to clear a hurdle before anything is declared.

There is a second reason, and it is arithmetical. A probability can be computed precisely at a single value of a parameter, but not over a range. Under $H_0$ the parameter is pinned to one number, so the distribution of the test statistic is fully determined and probabilities can be calculated. Under $H_1$ the parameter roams, so no single distribution exists unless a particular value is named. This asymmetry is the technical reason the whole procedure is built around the null.

### 1.4 The test statistic as a standardised distance

The sample gives a number, and the null hypothesis names a value. The obvious first step is to measure the distance between them. If the sample mean is $52.5$ grams and the null value is $50$ grams, the distance is $2.5$ grams. But a distance in grams means nothing on its own. Two and a half grams is enormous if the natural scatter from sample to sample is a tenth of a gram, and negligible if the scatter is fifty grams.

The fix is to divide the distance by the natural scatter. That scatter is the standard error, the standard deviation of the estimator, and it measures how much the sample mean typically wanders when nothing but chance is at work.

> **Definition (Standard error).** The standard error of the sample mean is the standard deviation of its sampling distribution, and it equals $\sigma/\sqrt{n}$ when the population standard deviation $\sigma$ is known and is estimated by $s/\sqrt{n}$ when it is not.

> **Definition (Test statistic, standard form).** A test statistic is a quantity computed from the sample, and containing no unknown parameter, whose value is compared with a known distribution. The standard form measures the distance between an estimate and the null value in units of standard error,

$$
\text{test statistic} = \frac{\text{estimate} - \text{null value}}{\text{standard error}} .
$$

The result is a pure number, free of units, and therefore comparable across problems, variables and scales. A value of $2.5$ always means "two and a half standard errors away from the null value", whether the underlying measurement is a mass in grams or a price in shillings.

The standard error itself deserves a sentence of plain explanation. It is not the spread of the data. It is the spread of the average. Averages wobble less than individual observations, and they wobble less the more observations there are. Dividing by the standard error rather than by the standard deviation is what makes a large sample count as stronger evidence than a small one.

### 1.5 The significance level and the critical region

Before examining the data, the investigator chooses how much doubt is enough. This choice is expressed as a number between zero and one.

> **Definition (Significance level).** The significance level, written $\alpha$, is the probability that the procedure rejects $H_0$ when $H_0$ is in fact true. It is the risk of a false alarm that the investigator is willing to take.

Common choices are $\alpha = 0.05$, $\alpha = 0.01$ and $\alpha = 0.10$. The choice is a judgement about consequences, not a law of nature. A test for a fatal defect in an aircraft part should use a small $\alpha$, because a false alarm is far cheaper than a missed defect. A preliminary screen for a rare condition may use a larger $\alpha$, because a false alarm merely triggers a second, better test.

The level carves the distribution of the test statistic, computed under $H_0$, into two parts: a central region where the observed value is unremarkable, and a tail or pair of tails where the observed value is surprising. The surprising part is the rejection region, also called the critical region.

> **Definition (Critical value and rejection region).** The critical value is the boundary of the rejection region, and the rejection region is the set of values of the test statistic for which $H_0$ is rejected. Under $H_0$ the rejection region has probability $\alpha$.

For a two-sided test of a mean with known variance, the statistic is standard normal under $H_0$, and the rejection region is the two tails beyond $\pm z_{\alpha/2}$. At $\alpha = 0.05$ the critical values are $-1.96$ and $+1.96$, so the rejection region has probability $0.025$ in each tail and $0.05$ in total. At $\alpha = 0.01$ the critical values are $\mp 2.576$.

### 1.6 The p-value

The critical value approach requires the investigator to fix a level first. An alternative and now more common approach reverses the order: compute the strength of the evidence, then compare it with whatever level the reader prefers.

> **Definition (p-value).** The p-value is the probability of obtaining a test statistic at least as extreme as the one observed, computed under the assumption that $H_0$ is true.

The phrase "at least as extreme" is doing real work. It means "as far from what $H_0$ predicts as the observed value, or further, in the direction or directions indicated by $H_1$". If the observed statistic is $2.5$ and the alternative is two-sided, the p-value is the probability that a standard normal variable exceeds $2.5$ in absolute value, which is

$$
p = 2\,\text{P}\left(Z > 2.5\right) = 2 \times 0.0062 = 0.0124 .
$$

The p-value is therefore a tail area, and it is always between zero and one. A small p-value means the observed result would be rare if $H_0$ were true, which is evidence against $H_0$. A large p-value means the observed result is unremarkable under $H_0$, which is not evidence for $H_0$; it is merely an absence of evidence against it.

The decision rule is simple. Reject $H_0$ when $p \le \alpha$, and do not reject $H_0$ when $p > \alpha$. This rule and the critical value rule always give the same answer, a fact proved in a later section and relied on throughout.

### 1.7 One-sided and two-sided alternatives

The alternative hypothesis decides which tail or tails count as evidence. Three shapes are possible.

A two-sided alternative says only that the parameter differs from the null value, written $H_1: \mu \ne \mu_0$. Evidence against $H_0$ is a sample mean that is too large or too small, so both tails form the rejection region and $\alpha$ is split between them.

A one-sided alternative says the parameter lies above the null value, written $H_1: \mu > \mu_0$. Only an unusually large sample mean counts as evidence, so only the upper tail forms the rejection region and the whole of $\alpha$ sits there.

A second one-sided form says the parameter lies below the null value, written $H_1: \mu < \mu_0$, and only the lower tail is used.

The practical consequence is that a one-sided test at $5\%$ uses the critical value $1.645$, whereas a two-sided test at $5\%$ uses $1.96$. The one-sided test is more powerful in the direction it is looking and completely blind in the other direction. It is legitimate only when a departure in the opposite direction would be ignored or handled separately, and the direction must be fixed before the data arrive. Choosing the direction after seeing whether the sample mean is high or low is a serious error, because it doubles the effective false-alarm rate.

### 1.8 Two kinds of mistake, and power

A verdict can be wrong in two ways, and the courtroom analogy gives both names.

A Type I error is rejecting $H_0$ when $H_0$ is true; the accused is convicted though innocent. Its probability is exactly $\alpha$, by construction, because $\alpha$ is defined as the probability that the rejection region is entered when $H_0$ holds.

A Type II error is failing to reject $H_0$ when $H_0$ is false; the guilty party walks free. Its probability is written $\beta$. Unlike $\alpha$, it is not chosen in advance and is not a single number: it depends on how false $H_0$ actually is. A mean that is only a hair away from the null value is very hard to detect, so $\beta$ is near one minus something small; a mean that is far away is easy to detect, so $\beta$ is near zero.

The complement of $\beta$ is the probability of detecting a genuine departure, and it has its own name.

> **Definition (Power).** The power of a test is the probability of rejecting $H_0$ when $H_0$ is false, so power $= 1 - \beta$. It is a function of the true parameter value, not a single number.

Power rises when the sample is larger, when $\alpha$ is larger, when the true value is further from the null value, and when the population is less variable. Of these, only the sample size and the significance level are under the investigator's control, and only the sample size improves both error rates at once. Raising $\alpha$ to gain power is simply deciding to be wrong more often in the other direction.

### 1.9 The fixed procedure

Every hypothesis test in this topic, however elaborate the formula, follows the same five moves. Learning the moves separately from the formulas is what allows an unfamiliar test to be handled calmly.

Step 1. State the hypotheses in symbols, naming the parameter and the null value, and decide from the wording whether the alternative is one-sided or two-sided.

Step 2. Choose the test statistic and its distribution under $H_0$, which requires knowing what is assumed about the population and what is known about its variance.

Step 3. Fix the significance level $\alpha$ and obtain the critical value or values from the appropriate table.

Step 4. Compute the statistic from the sample and compare it with the critical value, or compute the p-value and compare it with $\alpha$.

Step 5. State the decision in the language of the problem, and say what it does and does not mean.

The order matters. Steps 1 to 3 must be completed before the data are inspected, otherwise the test is contaminated by the very evidence it is meant to assess.

### 1.10 The symbols used in this topic

The notation is conventional and compact, and each symbol is worth reading aloud in words until it becomes automatic. Every symbol below reappears in the later sections.

| Symbol | Read aloud as | What it stands for |
| --- | --- | --- |
| $H_0$ | the null hypothesis | the presumption under test, usually a single parameter value |
| $H_1$ | the alternative hypothesis | the departure the investigator wants to detect |
| $\alpha$ | alpha | the probability of rejecting a true null, fixed in advance |
| $\beta$ | beta | the probability of failing to reject a false null |
| $1 - \beta$ | power | the probability of detecting a false null |
| $z$ | zed or zee | the standard normal test statistic used when the variance is known |
| $t$ | tee | the Student statistic used when the variance is estimated |
| $\chi^{2}$ | chi squared | the statistic used for counts and categories |
| $F$ | eff | the ratio statistic used to compare two variances |
| $p$ | the p-value | the probability of a result at least as extreme, under the null |

Two of these symbols, $\alpha$ and $\beta$, are probabilities of error and therefore live in the interval from zero to one. Two of them, $z$ and $t$, are standardised distances and can be any real number. The chi-square statistic and the $F$ statistic are non-negative by construction, because both are built from squares or from a ratio of non-negative quantities.

## 2. Theorems, Lemmas, and Analytical Properties

### 2.1 The alternative hypothesis selects the rejection region

The first property explains why the alternative cannot be chosen after the data are seen.

> **Lemma (Direction of the rejection region).** If the test statistic is a monotone increasing function of the estimate, then a one-sided alternative of the form $\mu > \mu_0$ places the whole rejection region in the upper tail, and a two-sided alternative places half of $\alpha$ in each tail.

The reasoning is a single sentence. The rejection region must be the set of sample outcomes that are more probable under the alternative than under the null. If the alternative says the true mean is larger, then large sample means are the outcomes the alternative predicts, so large sample means constitute evidence. If the alternative says only that the mean is different, then both very large and very small sample means are evidence, and fairness requires that the false-alarm risk be divided equally between the two directions.

This is why the two-sided critical value $1.96$ is larger than the one-sided value $1.645$ at the same level. The two-sided test must guard two doors, so each door is watched less closely. Both tests hold the false-alarm probability at $5\%$, but they are asking different questions, and neither is uniformly better than the other.

A direct consequence is that a two-sided test can never reject when the corresponding one-sided test in the correct direction fails to reject. The converse can happen, and the difference is largest for statistics near the boundary, exactly where choices matter most.

### 2.2 The p-value is a tail area under the null distribution

The second property fixes what the p-value is a probability of.

> **Lemma (p-value as an extreme-tail probability).** Let $T$ be the test statistic and let $t_{\text{obs}}$ be its observed value. If the rejection region has the form $T \ge c$ for a one-sided upper test, then $p = \text{P}_{H_0}\left(T \ge t_{\text{obs}}\right)$. If the rejection region is two-sided and symmetric, then $p = 2\,\text{P}_{H_0}\left(T \ge \left| t_{\text{obs}} \right|\right)$.

The definition uses the observed value as the boundary, so the p-value is literally the area beyond the observation. Because the boundary moves with the data, the p-value is a random variable before the sample is drawn, while the critical value is a fixed number chosen in advance.

The two procedures agree because of this identity: the observed value exceeds the critical value exactly when the tail area beyond the observed value is smaller than the tail area beyond the critical value, and the latter is $\alpha$ by construction. A statistic in the rejection region therefore has a p-value below $\alpha$, and a statistic outside it has a p-value above $\alpha$.

### 2.3 A smaller p-value is stronger evidence, but not a probability about the null

It is natural to treat the p-value as a measure of how likely the null hypothesis is. That reading is wrong, and the reason is structural rather than a matter of caution.

The p-value is computed under the assumption that $H_0$ is true. It is $\text{P}\left(\text{data at least this extreme} \mid H_0\right)$. What a reader usually wants is $\text{P}\left(H_0 \mid \text{data}\right)$, which is a different quantity and cannot be obtained without a prior probability for $H_0$. The two are related by Bayes' theorem, and the relation depends on the prior, so no amount of data analysis alone converts one into the other.

A numerical illustration makes the gap concrete. Suppose a disease affects one person in a thousand, and a screening test has a $5\%$ false-positive rate and perfect sensitivity. A positive result has a p-value of $0.05$ against the null of no disease. Yet the probability that a positively screened person actually has the disease is only about two per cent, because the healthy majority is so large that its five per cent dwarfs the sick minority. The p-value and the probability that the null is true therefore differ here by a factor of about twenty: the p-value is $0.05$, while the probability of no disease given a positive result is about $0.98$. They are simply not the same quantity.

### 2.4 A stricter level lowers the false-alarm rate

> **Lemma (Monotonicity in the level).** If the rejection region for level $\alpha_1$ is contained in the rejection region for $\alpha_2$ with $\alpha_1 < \alpha_2$, then any hypothesis rejected at $\alpha_1$ is also rejected at $\alpha_2$.

This follows immediately from the nesting of tail regions: shrinking the level pushes the critical value further into the tail, so the rejection region shrinks. The practical implication is that a decision is not a property of the data alone but of the data together with the level. Reporting only "significant" without the level is incomplete; reporting the p-value is better, because the reader can apply any level.

### 2.5 The two error probabilities move in opposite directions

For a fixed sample size and a fixed test statistic, lowering $\alpha$ raises $\beta$. The reason is geometric: a smaller rejection region is harder to enter, both when $H_0$ is true and when it is false. Since the power is the probability of entering the region when $H_0$ is false, power falls.

Three levers change this trade-off rather than merely sliding along it.

The first is the distance between the true value and the null value. A larger distance separates the two distributions, so both error probabilities can be small at once.

The second is the population variability. Less scatter means the two distributions are narrower and easier to tell apart.

The third is the sample size. Because the standard error shrinks like $1/\sqrt{n}$, a larger sample narrows both distributions and pushes them apart in standardised units. This is the only lever that reduces both error probabilities simultaneously without changing the question being asked.

### 2.6 The link between a two-sided test and a confidence interval

A two-sided test at level $\alpha$ and a confidence interval at confidence level $1 - \alpha$ are two views of one calculation.

> **Theorem (Duality).** For a parameter $\theta$, a two-sided test of $H_0: \theta = \theta_0$ at level $\alpha$ rejects exactly those values $\theta_0$ that lie outside the $100\left(1 - \alpha\right)\%$ confidence interval for $\theta$.

The mechanism is a single inequality. The test rejects when the standardised distance exceeds the critical value,

$$
\left| \frac{\hat{\theta} - \theta_0}{\text{SE}} \right| > z_{\alpha/2} ,
$$

and the interval is the set of $\theta_0$ for which that same inequality is reversed,

$$
\hat{\theta} - z_{\alpha/2}\,\text{SE} \le \theta_0 \le \hat{\theta} + z_{\alpha/2}\,\text{SE} .
$$

The two statements are negations of each other, so membership in the interval and non-rejection are the same event.

The duality is more than a convenience. It says that a confidence interval carries all the information of every two-sided test at that level simultaneously, and it explains why an interval that contains the null value corresponds to a non-significant result. It also warns against a common inconsistency: computing a $99\%$ interval and then testing at $5\%$ produces conclusions that appear to contradict one another, even though each is correct at its own level.

### 2.7 Degrees of freedom in the count-based tests

The chi-square statistic sums squared standardised gaps between observed and expected counts. Its reference distribution is chi-square, and the single number that fixes that distribution is the degrees of freedom.

For a goodness-of-fit test with $k$ categories the degrees of freedom are $k - 1$. One degree of freedom is spent because the expected counts must add to the same total as the observed counts, so the last expected count is determined once the others are fixed.

For a test of independence in a table with $r$ rows and $c$ columns the degrees of freedom are $\left(r - 1\right)\left(c - 1\right)$. Each row's expected counts must add to that row's total, which costs one degree of freedom per row, and each column's expected counts must add to that column's total, which costs one degree of freedom per column. The counting gives $rc - r - c + 1$, which factorises as $\left(r - 1\right)\left(c - 1\right)$.

A further degree of freedom is lost whenever a parameter is estimated from the data before the expected counts are computed. This is why a goodness-of-fit test in which two parameters are estimated from the sample uses $k - 1 - 2 = k - 3$ degrees of freedom.

### 2.8 The test for a single proportion

Counts obey the same logic as means once each observation is coded one for success and zero for failure. The sample proportion is then the sample mean of a zero-one variable, and its standard error under the null is $\sqrt{p_0\left(1 - p_0\right)/n}$.

> **Lemma (Proportion test statistic).** Under $H_0: p = p_0$, the statistic

$$
z = \frac{\hat{p} - p_0}{\sqrt{p_0\left(1 - p_0\right)/n}}
$$

is approximately standard normal for large $n$, where $\hat{p} = X/n$ and $X$ is the number of successes.

The standard error uses $p_0$, not $\hat{p}$, because the test statistic must be computed under the assumption that $H_0$ is true. Using $\hat{p}$ in the denominator would make the statistic's distribution depend on the data in a way that spoils the reference distribution, and it is a frequent source of small-sample distortion.

The approximation is adequate when both $np_0$ and $n\left(1 - p_0\right)$ exceed about five or ten. When they do not, exact binomial probabilities should be used instead.

### 2.9 The test for the ratio of two variances

Two populations can be compared through the ratio of their estimated variances. If the populations are normal and independent, then under the null hypothesis that the variances are equal, the ratio of the two sample variances divided by the true ratio follows an $F$ distribution.

> **Lemma (Variance-ratio statistic).** For independent normal samples of sizes $n_1$ and $n_2$ with sample variances $s_1^{2}$ and $s_2^{2}$, the statistic

$$
F = \frac{s_1^{2}}{s_2^{2}}
$$

follows an $F$ distribution with $n_1 - 1$ degrees of freedom in the numerator and $n_2 - 1$ in the denominator when the two population variances are equal.

The $F$ distribution is skewed to the right and is indexed by two degrees of freedom, one for each variance in the ratio. Because it is not symmetric, the two tails are not mirror images, and the usual convention is to put the larger variance on top and compare against the upper critical value only. This convention works because the reciprocal of an $F$ variable with $\left(d_1, d_2\right)$ degrees of freedom is an $F$ variable with $\left(d_2, d_1\right)$ degrees of freedom.

### 2.10 A summary of the principal results

The whole topic can be compressed into a small table, and the compression is useful for revision precisely because it strips away the incidental detail of each problem.

| Question asked | Statistic | Reference distribution | Degrees of freedom |
| --- | --- | --- | --- |
| One mean, variance known | $z = \left(\bar{x} - \mu_0\right)/\left(\sigma/\sqrt{n}\right)$ | standard normal | none |
| One mean, variance estimated | $t = \left(\bar{x} - \mu_0\right)/\left(s/\sqrt{n}\right)$ | Student t | $n - 1$ |
| Two means, variances assumed equal | pooled two-sample t | Student t | $n_1 + n_2 - 2$ |
| Paired means | one-sample t on differences | Student t | $n - 1$ |
| One proportion | $z$ with null standard error | standard normal | none |
| Goodness of fit | sum of squared standardised gaps | chi-square | $k - 1 - m$ |
| Independence in a table | sum of squared standardised gaps | chi-square | $\left(r - 1\right)\left(c - 1\right)$ |
| Equality of two variances | ratio of sample variances | F | $n_1 - 1$ and $n_2 - 1$ |

Two rows of that table describe comparisons between groups rather than a single group, and they deserve a sentence each in words.

A paired comparison arises when the same subject is measured twice, before and after a treatment. The two measurements are dependent, so they cannot be treated as two independent samples. The remedy is to compute one difference per subject and to test whether the mean difference is zero, using a one-sample t test on the differences with $n - 1$ degrees of freedom. Differences remove the between-subject variation, which is why a paired design is usually far more sensitive than treating the columns as independent groups.

An independent two-sample comparison arises when two separate groups are measured, for example two machines or two teaching methods. The statistic is the difference of the sample means divided by its standard error, and the standard error is built from a pooled estimate of the common variance when the two population variances are assumed equal. Its degrees of freedom are two fewer than the total number of observations.

Each row of this table is a complete recipe once the null value, the alternative and the sample summary are known. The skill an examination rewards is not memorising the rows but recognising which row a question belongs to.

## 3. Formal Proofs, Derivations, and Methods

### 3.1 Where the standard normal statistic comes from

The derivation of the $z$ statistic uses three facts already established in the theory of estimation.

The first is that the sample mean of independent observations has expectation $\mu$ and variance $\sigma^{2}/n$. The expectation follows from linearity, and the variance follows from independence, because the variance of a sum of independent terms is the sum of their variances.

The second is that subtracting the mean and dividing by the standard deviation produces a variable with mean zero and variance one. This standardisation is exact, not approximate, and requires no distributional assumption.

The third is the central limit theorem, which says that for large $n$ the standardised sample mean is approximately standard normal whatever the shape of the population.

Combining the three gives the statistic and its reference distribution.

$$
Z = \frac{\bar{x} - \mu_0}{\sigma/\sqrt{n}} \;\dot\sim\; \text{N}\left(0, 1\right) \quad \text{under } H_0 .
$$

When the population is itself normal the approximation is exact for every $n$, which is why the $z$ test is exact for normal data with known variance. When the population is not normal the approximation improves as $n$ grows, and a common rule of thumb is that $n$ of at least thirty is adequate unless the population is severely skewed.

### 3.2 Why the standard error, and not the standard deviation, is the divisor

A short algebraic check explains the choice. Suppose the divisor were the population standard deviation $\sigma$ instead of $\sigma/\sqrt{n}$. Then the statistic would be $\left(\bar{x} - \mu_0\right)/\sigma$, and repeating the experiment with four times as many observations would multiply the statistic by two on average, purely because the sample was larger. The threshold for significance would then depend on the sample size in an unmanageable way, and the same data pattern would be judged differently at different sizes for no reason connected to the evidence.

Dividing by the standard error removes the sample-size effect exactly, because the standard error already contains the $1/\sqrt{n}$ factor. The resulting statistic has the same distribution at every sample size, so a single table of critical values serves all cases.

### 3.3 Why a t statistic replaces z when the variance is estimated

In practice $\sigma$ is rarely known. Replacing it with the sample standard deviation $s$ is the obvious move, but it changes the distribution of the statistic, and the change is not small in small samples.

The reason is that $s$ is itself random. The numerator and the denominator of

$$
t = \frac{\bar{x} - \mu_0}{s/\sqrt{n}}
$$

both vary from sample to sample, and the denominator can happen to be small, which inflates the ratio. The resulting distribution therefore has heavier tails than the normal, meaning that large values occur more often than the normal curve suggests.

The exact distribution was derived by Gosset and published under the pen name Student. It depends on the sample size through a single parameter, the degrees of freedom. For $n$ observations the statistic follows a $t$ distribution with $n - 1$ degrees of freedom, and the shape approaches the normal as $n - 1$ grows.

The practical consequence is that critical values are larger than the normal ones in small samples. With nine degrees of freedom the two-sided $5\%$ critical value is $2.262$ rather than $1.96$, an inflation of fifteen per cent. With thirty degrees of freedom it is $2.042$, and with a hundred it is $1.984$. The penalty for estimating the variance is real but shrinks quickly.

### 3.4 Why the chi-square statistic is a sum of squared standardised gaps

The chi-square test compares counts. For each category the observed count $O_i$ is compared with the count $E_i$ that the null hypothesis predicts, and the gap is standardised by dividing by the predicted count.

The reason the divisor is $E_i$ rather than its square root is that a count behaves like a sum of independent trials, whose variance equals its mean. For a binomial count with mean $E_i$, the variance is $E_i\left(1 - p_i\right)$, and for small probabilities this is close to $E_i$. Standardising the gap therefore means dividing by the standard deviation, which is approximately $\sqrt{E_i}$, and then squaring the result gives a term $\left(O_i - E_i\right)^{2}/E_i$.

Summing these standardised squared gaps over the categories gives the statistic

$$
\chi^{2} = \sum_{i=1}^{k} \frac{\left(O_i - E_i\right)^{2}}{E_i} .
$$

Under $H_0$ the sum of squares of approximately standard normal quantities is approximately chi-square, and the approximation improves as the expected counts grow. The rule of thumb is that every expected count should be at least five, and that no more than a fifth of them should be below five.

### 3.5 The five-step method carried out in full

The procedure is worth writing out as a template, because the marks in an examination are attached to the steps rather than to the final word.

Step 1. Identify the parameter, the null value, and the alternative. Write $H_0$ and $H_1$ in symbols and add a sentence in words.

Step 2. Name the assumptions. State whether the population is normal or the sample large, and whether the variance is known or estimated. Name the statistic and its distribution under $H_0$.

Step 3. Fix $\alpha$ and find the critical value or values from the table for the correct degrees of freedom and the correct number of tails.

Step 4. Compute the statistic, showing the standard error separately from the numerator, because most arithmetic errors occur in the standard error.

Step 5. Compare, decide, and interpret. Either state that the statistic lies in the rejection region or state the p-value, then translate the decision into a sentence about the population, and add what the decision does not establish.

### 3.6 The p-value method carried out in full

The p-value method follows the same first two steps and then diverges.

Step 3 becomes: compute the statistic and locate the observed value in the null distribution, without reference to $\alpha$.

Step 4 becomes: compute the tail area. For a one-sided upper test that is the area above the observed value; for a one-sided lower test it is the area below; for a two-sided test it is twice the smaller tail.

Step 5 becomes: compare the p-value with $\alpha$ and decide. Reporting the p-value itself, rather than only the verdict, allows any reader to apply a different level.

### 3.7 Checking that the two methods agree

The agreement is not a coincidence and can be verified in one line. Let $c$ be the critical value for level $\alpha$ in a one-sided upper test, chosen so that $\text{P}\left(T \ge c\right) = \alpha$. The p-value is $p = \text{P}\left(T \ge t_{\text{obs}}\right)$. Because the tail probability decreases as its boundary moves to the right, the inequality $t_{\text{obs}} \ge c$ holds exactly when $p \le \alpha$.

The same argument applies to the two-sided case with the absolute value of the statistic and with $\alpha/2$ in each tail. There is therefore no situation in which the two methods disagree, and an answer that reports one conclusion from the critical value and the opposite from the p-value contains an arithmetic error somewhere.

## 4. Representative Worked Examples and Solutions

### 4.1 Problem: a two-sided test of a mean with a known standard deviation

A machine is set to fill bags with a mean mass of $50$ grams. The standard deviation of the filling process is known from long experience to be $4$ grams. A random sample of $16$ bags has a mean mass of $52.5$ grams. Test at the $5\%$ level whether the mean mass differs from $50$ grams.

### 4.2 Solution: the z test with both decision rules

Step 1. State the hypotheses. The word "differs" makes the alternative two-sided.

$$
H_0: \mu = 50, \qquad H_1: \mu \ne 50 .
$$

Step 2. Choose the statistic. The variance is known, so the standard normal statistic applies.

$$
Z = \frac{\bar{x} - \mu_0}{\sigma/\sqrt{n}} .
$$

Step 3. Compute the standard error.

$$
\frac{\sigma}{\sqrt{n}} = \frac{4}{\sqrt{16}} = \frac{4}{4} = 1 .
$$

Step 4. Compute the statistic.

$$
Z = \frac{52.5 - 50}{1} = 2.5 .
$$

Step 5. Obtain the critical values. For a two-sided test at $\alpha = 0.05$ they are $\pm 1.96$.

Step 6. Compare. Since $2.5 > 1.96$, the observed value lies in the rejection region, so $H_0$ is rejected.

Step 7. Confirm with the p-value.

$$
p = 2\,\text{P}\left(Z > 2.5\right) = 2 \times 0.0062 = 0.0124 .
$$

Since $0.0124 < 0.05$, the decision is the same.

Step 8. Interpret. There is sufficient evidence at the $5\%$ level that the mean fill differs from $50$ grams. The sample mean is above the target, so the evidence points to overfilling.

### 4.3 Problem: the same data with a one-sided alternative

Using the same sample, test whether the mean mass exceeds $50$ grams at the $5\%$ level.

### 4.4 Solution: one tail instead of two

Step 1. State the hypotheses. The phrase "exceeds" fixes the direction in advance.

$$
H_0: \mu = 50, \qquad H_1: \mu > 50 .
$$

Step 2. The statistic is unchanged.

$$
Z = \frac{52.5 - 50}{1} = 2.5 .
$$

Step 3. The critical value for a one-sided test at $\alpha = 0.05$ is $1.645$.

Step 4. Compare. Since $2.5 > 1.645$, reject $H_0$.

Step 5. Compute the one-sided p-value.

$$
p = \text{P}\left(Z > 2.5\right) = 0.0062 .
$$

Step 6. Note that the p-value is exactly half the two-sided value, and that both decisions agree here.

Step 7. Interpret. There is sufficient evidence at the $5\%$ level that the mean mass exceeds $50$ grams.

### 4.5 Problem: a case where the number of tails changes the verdict

Suppose a sample from a normal population with known standard deviation gives $Z = 1.80$. Compare the conclusions of the two-sided and the one-sided tests at the $5\%$ level.

### 4.6 Solution: the boundary region where the choice matters

Step 1. Compute the two-sided p-value.

$$
p = 2\,\text{P}\left(Z > 1.80\right) = 2 \times 0.0359 = 0.0718 .
$$

Step 2. Compare with $0.05$. Since $0.0718 > 0.05$, the two-sided test does not reject $H_0$.

Step 3. Compute the one-sided p-value.

$$
p = \text{P}\left(Z > 1.80\right) = 0.0359 .
$$

Step 4. Compare with $0.05$. Since $0.0359 < 0.05$, the one-sided test rejects $H_0$.

Step 5. Explain the discrepancy. The same evidence is being judged against two different questions. The two-sided test asks whether the mean is different, and it must reserve half of its false-alarm risk for the lower tail, so it is cautious about an upper-tail result. The one-sided test asks only whether the mean is larger, and it spends its entire allowance on the upper tail.

Step 6. Draw the lesson. The alternative must be chosen from the scientific question before the data are seen. If the direction were chosen after observing that the sample mean was above the target, the nominal $5\%$ level would be false, because the investigator would effectively have had two chances to find an extreme value.

### 4.7 Problem: a test of a mean with an estimated standard deviation

A sample of $9$ components from a normal production process has a mean lifetime of $12.4$ hours and a standard deviation of $1.5$ hours. Test at the $5\%$ level whether the mean lifetime differs from $11$ hours.

### 4.8 Solution: the t test with eight degrees of freedom

Step 1. State the hypotheses.

$$
H_0: \mu = 11, \qquad H_1: \mu \ne 11 .
$$

Step 2. Note that $\sigma$ is unknown and the sample is small, so the $t$ statistic is required.

$$
t = \frac{\bar{x} - \mu_0}{s/\sqrt{n}} \quad \text{with } n - 1 = 8 \text{ degrees of freedom} .
$$

Step 3. Compute the standard error.

$$
\frac{s}{\sqrt{n}} = \frac{1.5}{3} = 0.5 .
$$

Step 4. Compute the statistic.

$$
t = \frac{12.4 - 11}{0.5} = \frac{1.4}{0.5} = 2.8 .
$$

Step 5. Obtain the critical value. The two-sided $5\%$ value on $8$ degrees of freedom is $2.306$.

Step 6. Compare. Since $2.8 > 2.306$, reject $H_0$.

Step 7. Report the p-value, which is approximately $0.023$.

Step 8. Interpret. The mean lifetime differs from $11$ hours at the $5\%$ level. Had the normal critical value $1.96$ been used, the conclusion would have been the same here, but the margin would have been overstated; with smaller samples the difference between the two tables becomes decisive.

### 4.9 Problem: a test of a single proportion

In a sample of $100$ voters, $58$ support a proposal. Test at the $5\%$ level whether the population support differs from one half.

### 4.10 Solution: the normal approximation to the binomial

Step 1. State the hypotheses with $p$ as the population proportion.

$$
H_0: p = 0.5, \qquad H_1: p \ne 0.5 .
$$

Step 2. Compute the sample proportion.

$$
\hat{p} = \frac{58}{100} = 0.58 .
$$

Step 3. Compute the null standard error, using the null value of $p$.

$$
\text{SE}_0 = \sqrt{\frac{0.5 \times 0.5}{100}} = \sqrt{0.0025} = 0.05 .
$$

Step 4. Compute the statistic.

$$
z = \frac{0.58 - 0.5}{0.05} = \frac{0.08}{0.05} = 1.6 .
$$

Step 5. Check the approximation conditions.

$$
np_0 = 50 \ge 10, \qquad n\left(1 - p_0\right) = 50 \ge 10 .
$$

Step 6. Compare with the critical value $1.96$. Since $1.6 < 1.96$, do not reject $H_0$.

Step 7. Compute the p-value.

$$
p = 2\,\text{P}\left(Z > 1.6\right) = 2 \times 0.0548 = 0.1096 .
$$

Step 8. Interpret. There is insufficient evidence at the $5\%$ level to conclude that support differs from one half. The sample proportion is higher than one half, but a difference of eight percentage points with a sample of a hundred is well within the range that chance produces when the true proportion is one half.

### 4.11 Problem: a chi-square goodness-of-fit test

A die is rolled $120$ times, giving counts of $18$, $22$, $25$, $15$, $20$ and $20$ on the six faces. Test at the $5\%$ level whether the die is fair.

### 4.12 Solution: six categories and five degrees of freedom

Step 1. State the hypotheses. The null is that each face has probability one sixth; the alternative is that at least one probability differs.

$$
H_0: p_i = \frac{1}{6} \text{ for } i = 1, \dots, 6, \qquad H_1: \text{not all } p_i \text{ are equal to } \frac{1}{6} .
$$

Step 2. Compute the expected counts under the null.

$$
E_i = 120 \times \frac{1}{6} = 20 \quad \text{for every face} .
$$

Step 3. Compute the squared standardised gaps, face by face.

$$
\frac{\left(18 - 20\right)^{2}}{20} = 0.20, \quad \frac{\left(22 - 20\right)^{2}}{20} = 0.20, \quad \frac{\left(25 - 20\right)^{2}}{20} = 1.25 ,
$$

$$
\frac{\left(15 - 20\right)^{2}}{20} = 1.25, \quad \frac{\left(20 - 20\right)^{2}}{20} = 0, \quad \frac{\left(20 - 20\right)^{2}}{20} = 0 .
$$

Step 4. Add the six terms.

$$
\chi^{2} = 0.20 + 0.20 + 1.25 + 1.25 + 0 + 0 = 2.90 .
$$

Step 5. Determine the degrees of freedom. There are six categories and no parameter estimated from the data, so

$$
\nu = 6 - 1 = 5 .
$$

Step 6. Obtain the critical value. The $5\%$ upper point of the chi-square distribution on five degrees of freedom is $11.07$.

Step 7. Compare. Since $2.90 < 11.07$, do not reject $H_0$.

Step 8. Interpret. The observed counts are consistent with a fair die. No evidence of bias has been found at the $5\%$ level, and the p-value of about $0.72$ shows that counts this uneven are entirely ordinary.

### 4.13 Problem: a chi-square test of independence

A survey of $200$ employees records whether each uses public transport and whether each works in the office or from home. Among $100$ office workers, $50$ use public transport. Among $100$ home workers, $30$ use public transport. Test at the $5\%$ level whether the two variables are independent.

### 4.14 Solution: a two-by-two table with one degree of freedom

Step 1. Lay out the observed counts with totals.

| Group | Uses public transport | Does not use public transport | Row total |
| --- | --- | --- | --- |
| Office workers | 50 | 50 | 100 |
| Home workers | 30 | 70 | 100 |
| Column total | 80 | 120 | 200 |

Step 2. State the hypotheses. The null is independence; the alternative is that the proportion using public transport depends on the group.

Step 3. Compute the expected count in each cell as the row total times the column total divided by the grand total.

$$
E_{11} = \frac{100 \times 80}{200} = 40, \qquad E_{12} = \frac{100 \times 120}{200} = 60 ,
$$

$$
E_{21} = \frac{100 \times 80}{200} = 40, \qquad E_{22} = \frac{100 \times 120}{200} = 60 .
$$

Step 4. Compute each squared standardised gap.

$$
\frac{\left(50 - 40\right)^{2}}{40} = 2.500, \qquad \frac{\left(50 - 60\right)^{2}}{60} = 1.667 ,
$$

$$
\frac{\left(30 - 40\right)^{2}}{40} = 2.500, \qquad \frac{\left(70 - 60\right)^{2}}{60} = 1.667 .
$$

Step 5. Add them.

$$
\chi^{2} = 2.500 + 1.667 + 2.500 + 1.667 = 8.333 .
$$

Step 6. Determine the degrees of freedom.

$$
\nu = \left(2 - 1\right)\left(2 - 1\right) = 1 .
$$

Step 7. Compare with the critical value $3.841$. Since $8.33 > 3.841$, reject $H_0$.

Step 8. Interpret. Usage of public transport is associated with the working arrangement. The office group uses it at a rate of $50\%$ against $30\%$ for the home group, and a gap of that size in samples of a hundred each would be unusual if the two groups shared a common rate.

### 4.15 Problem: the probability of the two errors

A machine fills bags with a standard deviation of $4$ grams, and $16$ bags are sampled. The test is two-sided at the $5\%$ level with a null mean of $50$ grams. Find the probability of a Type I error, the probability of a Type II error and the power, if the true mean is $54$ grams.

### 4.16 Solution: translating the rejection region into a statement about the sample mean

Step 1. Write the rejection region for the statistic.

$$
\text{reject } H_0 \text{ if } Z < -1.96 \text{ or } Z > 1.96 .
$$

Step 2. Convert it into a rejection region for the sample mean, using a standard error of one gram.

$$
\bar{x} < 50 - 1.96 = 48.04 \qquad \text{or} \qquad \bar{x} > 50 + 1.96 = 51.96 .
$$

Step 3. State the Type I error probability. By construction it is the level.

$$
\alpha = 0.05 .
$$

Step 4. Compute the power at a true mean of $54$ grams, which is the probability that the sample mean exceeds $51.96$ when the mean is $54$.

$$
\text{P}\left(\bar{x} > 51.96\right) = \text{P}\left(Z > \frac{51.96 - 54}{1}\right) = \text{P}\left(Z > -2.04\right) = 0.9793 .
$$

Step 5. Add the lower-tail contribution, which is the probability that the sample mean falls below $48.04$ when the mean is $54$.

$$
\text{P}\left(Z < \frac{48.04 - 54}{1}\right) = \text{P}\left(Z < -5.96\right) \approx 0 .
$$

Step 6. State the power and the Type II error probability.

$$
\text{power} \approx 0.9793, \qquad \beta = 1 - 0.9793 = 0.0207 .
$$

Step 7. Interpret. If the machine were overfilling by four grams, the test would detect it $97.9\%$ of the time. A departure of that size is easy to see with a standard error of one gram, which is why the power is so high.

## 5. Mathematical Extensions, Limits, and Common Errors

### 5.1 Ten mistakes that beginners make

The first mistake, and the most important, is to say that the p-value is the probability that the null hypothesis is true. It is not. The p-value is the probability of the observed result, or something more extreme, given that the null hypothesis is true. The conditional runs in the opposite direction from the one people assume, and reversing it requires a prior probability that the test alone cannot supply.

The second mistake is to say that a large p-value proves the null hypothesis. A large p-value says the data are compatible with the null; it does not say the null is correct. A tiny sample can produce a large p-value for a wildly false null, simply because the sample is too small to see anything.

The third mistake is to read "do not reject" as "accept". The verdict of not guilty does not establish innocence, and a non-significant result does not establish equality. The correct phrasing is "there is insufficient evidence at this level to conclude otherwise".

The fourth mistake is to choose the alternative after seeing the data. Deciding on a one-sided test because the sample mean came out above the null value doubles the effective false-alarm rate and destroys the stated level.

The fifth mistake is to use the sample standard deviation in the denominator of a $z$ test when the sample is small. If $\sigma$ is estimated and $n$ is small, the $t$ table is required, and the normal critical value is too permissive.

The sixth mistake is to use $\hat{p}$ instead of $p_0$ in the standard error of a proportion test. The null standard error is the one that makes the statistic's distribution known under $H_0$.

The seventh mistake is to confuse the standard deviation with the standard error. The first describes the spread of single observations; the second describes the spread of an average, and it is smaller by a factor of $\sqrt{n}$.

The eighth mistake is to quote a p-value without a level. A p-value of $0.03$ is significant at $5\%$ and not at $1\%$, and the reader needs to know which question was asked.

The ninth mistake is to treat statistical significance as practical importance. With a large enough sample, a difference of no practical consequence becomes statistically significant, because the standard error shrinks while the difference does not.

The tenth mistake is to apply a chi-square test when the expected counts are tiny. The reference distribution is an approximation that requires expected counts of at least about five; with smaller counts the true p-value can be far from the nominal one.

### 5.2 Reading a p-value correctly

The safest way to read a p-value is to say the whole sentence rather than the abbreviation. A p-value of $0.0124$ means that if the null hypothesis were true, a result at least as far from the null value as the one observed would occur about one time in eighty. That sentence contains the conditional, the direction and the null, and none of them can be dropped without changing the meaning.

It is equally important to keep the p-value separate from the effect size. A p-value answers "is there evidence of a departure?" and says nothing about "how large is the departure?". Two studies can report the same p-value while estimating effects that differ by a factor of ten, because one used a much larger sample and detected a much smaller departure.

Finally, the p-value is not a measure of the probability that the result will replicate. Replication depends on power, on the size of the true effect, and on the number of hypotheses tested. A single small p-value from a small study is weak evidence in a way that the number alone conceals.

### 5.3 What the tests assume, and what happens when the assumptions fail

The $z$ and $t$ tests for a mean assume independent observations. Serially correlated data, such as measurements taken minute by minute in the same batch, violate this and understate the standard error, producing p-values that are too small. The remedy is a variance estimate that accounts for the correlation, not a larger significance level.

The $t$ test additionally assumes a normal population when the sample is small. Moderate departures from normality are tolerable, because the test is fairly robust, but severe skewness with a handful of observations can distort the level badly.

The chi-square tests assume independent observations and adequate expected counts. They also assume that the categories are mutually exclusive and exhaustive, so that every observation falls in exactly one cell. Correlated observations, such as several responses from the same person, inflate the statistic.

The $F$ test for two variances is the most sensitive to assumptions of all. It requires normal populations and independent samples, and it is badly distorted by heavy tails. Many practitioners avoid it altogether and use a robust or resampling alternative.

### 5.4 Where the subject goes next

Three extensions are worth knowing by name. The first is the likelihood ratio test, which constructs a statistic from the ratio of the maximised likelihood under the null to the maximised likelihood overall, and which covers all the tests in this topic as special cases. The second is the analysis of variance, which generalises the two-sample $t$ test to three or more groups and uses the same $F$ distribution. The third is the multiple-testing problem, where testing many hypotheses at once inflates the chance of at least one false alarm, and where corrections such as the Bonferroni rule divide the level by the number of tests.

All three rest on the same courtroom logic. A claim is presumed true, evidence must dislodge it, and the standard of proof is fixed in advance. What changes is only the arithmetic of the evidence.
