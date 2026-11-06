## 1. Foundational Concepts, Definitions, and Axioms

### 1.1 What the examiner is actually testing

Estimation questions look varied but are remarkably few in kind. Almost every question in this topic asks the candidate to do one of five things: name and compute a point estimate; build an interval from a stated confidence level; choose between the normal and the t multiplier; invert a margin of error to obtain a sample size; or explain, in words, what the confidence level means. A question may combine two or three of these, but it will not go outside them.

The marks are distributed predictably. Roughly half are for correct arithmetic and correct limits. Roughly a third are for the choice of method: the right multiplier, the right standard error, the right treatment of a finite population or a one-sided request. The remainder are for interpretation and for recognising when a standard method does not apply. Candidates who lose marks usually lose them on the second group, because the arithmetic is easy to practise and the judgement is not.

This note is organised around those three groups of marks. The results are stated in the form in which they are used, the derivations are given in the form in which they are reproduced under time pressure, and the worked solutions carry explicit marking points so that the shape of a full-mark answer is visible.

### 1.2 The definitions in examination wording

> **Definition (Point estimate).** A point estimate is a single value computed from a sample and used as the best guess for an unknown population parameter. The sample mean $\bar{x}$ is the point estimate of the population mean $\mu$; the sample proportion $\hat{p}$ is the point estimate of the population proportion $p$.

> **Definition (Interval estimate).** An interval estimate is a range of values, with a lower limit and an upper limit, within which the parameter is expected to lie. It is constructed as the point estimate plus or minus a margin of error.

> **Definition (Confidence level).** The confidence level is the probability, usually $95\%$, that the procedure which builds the interval produces an interval containing the true parameter. It is a property of the procedure, not of any single realised interval.

Three sentences carry the definitions, and each has a phrase that earns a mark. In the first, "single value" and "unknown parameter" are the phrases. In the second, "range" and "margin of error". In the third, "procedure" and "repeated samples". An answer that writes only "a confidence level is how sure we are" earns nothing, because it names no mechanism.

The error rate is the complement of the confidence level,

$$
\alpha = 1 - \left(1 - \alpha\right) \quad \text{written in practice as} \quad \alpha = 1 - \text{confidence level},
$$

so a $95\%$ level corresponds to $\alpha = 0.05$, a $99\%$ level to $\alpha = 0.01$, and a $90\%$ level to $\alpha = 0.10$. Every multiplier in the topic is indexed by $\alpha$ or by $\alpha/2$, and getting that index right is the difference between a correct and an incorrect interval.

### 1.3 The five quantities every question supplies or demands

Every numerical question in this topic can be read off a list of five quantities. Identifying them before writing anything prevents most errors.

The five are the parameter type, which is a mean or a proportion; the confidence level, which fixes the multiplier; the sample size $n$; the point estimate, which is $\bar{x}$ or $\hat{p}$; and the spread, which is $\sigma$ if known, $s$ if estimated, or the quantity $\hat{p}\left(1-\hat{p}\right)$ for a proportion. If a sixth quantity appears, it is either the population size $N$, which triggers the finite population correction, or a target margin of error, which triggers the sample size formula.

A useful discipline is to write the five quantities on one line before starting. For example: mean, $95\%$, $n = 20$, $\bar{x} = 14.32$, $s = 2.41$ with $\sigma$ unknown. The last clause decides the multiplier, and it is the clause most often omitted.

### 1.4 The critical values as an exam instrument

The multipliers are supplied in most examinations, but fluency with them saves time and catches errors.

| Confidence level | Two-sided $z$ | One-sided $z$ | Typical use |
| --- | --- | --- | --- |
| $90\%$ | $1.645$ | $1.282$ | exploratory work |
| $95\%$ | $1.960$ | $1.645$ | the default level |
| $98\%$ | $2.326$ | $2.054$ | cautious reporting |
| $99\%$ | $2.576$ | $2.326$ | strong evidence demanded |

The t quantiles are needed whenever the population standard deviation is unknown, and a short table covers almost every question.

| Degrees of freedom | $t$ at $95\%$ two-sided | $t$ at $99\%$ two-sided | $t$ at $95\%$ one-sided |
| --- | --- | --- | --- |
| $4$ | $2.776$ | $4.604$ | $2.132$ |
| $9$ | $2.262$ | $3.250$ | $1.833$ |
| $15$ | $2.131$ | $2.947$ | $1.753$ |
| $19$ | $2.093$ | $2.861$ | $1.729$ |
| $24$ | $2.064$ | $2.797$ | $1.711$ |
| $29$ | $2.045$ | $2.756$ | $1.699$ |

Reading the second table correctly is a frequent source of lost marks. The column headed $95\%$ two-sided contains the value that leaves $2.5\%$ in each tail, not the value that leaves $5\%$ in one tail. The two conventions differ, and the difference at $19$ degrees of freedom is between $2.093$ and $1.729$, which is large enough to change a reported interval appreciably.

### 1.5 The formula sheet

Everything computational in the topic fits on one page.

| Quantity | Formula | Condition |
| --- | --- | --- |
| Standard error of a mean | $\sigma/\sqrt{n}$ | $\sigma$ known |
| Estimated standard error of a mean | $s/\sqrt{n}$ | $\sigma$ unknown |
| Standard error of a proportion | $\sqrt{\hat{p}\left(1-\hat{p}\right)/n}$ | large $n$ |
| Interval for a mean | $\bar{x} \pm z\,\sigma/\sqrt{n}$ | $\sigma$ known |
| Interval for a mean | $\bar{x} \pm t\,s/\sqrt{n}$ | $\sigma$ unknown |
| Wald interval for a proportion | $\hat{p} \pm z\sqrt{\hat{p}\left(1-\hat{p}\right)/n}$ | $n\hat{p} \ge 10$ |
| Wilson centre | $\left(x + z^{2}/2\right)/\left(n + z^{2}\right)$ | always valid |
| Sample size for a mean | $\left(z\sigma/E\right)^{2}$ | rounded up |
| Sample size for a proportion | $z^{2}p^{*}\left(1-p^{*}\right)/E^{2}$ | rounded up |
| Finite population factor | $\sqrt{\left(N-n\right)/\left(N-1\right)}$ | without replacement |

The conditions column is not decoration. Each formula is valid only inside its condition, and an answer that applies a formula outside its condition is worth less than an answer that names the condition and chooses a different route. Two conditions matter most: $n\hat{p} \ge 10$ for the Wald interval, and a normal population for the t interval at small $n$.

### 1.6 Notation as it appears in questions

Questions use a small vocabulary of symbols, and a misreading of one is fatal.

The symbol $\mu$ is a population mean and is unknown. The symbol $\bar{x}$ is a sample mean and is computed. The same pair distinguishes $\sigma$ from $s$ and $p$ from $\hat{p}$. The symbol $E$ denotes the margin of error and is a half-width, not a full width, so a question that asks for a margin of error of $2$ grams is satisfied by an interval $4$ grams wide. The symbol $N$ denotes the population size and only appears when the finite population correction is in play.

Two further conventions are worth stating. A confidence level of $95\%$ may be written as $0.95$; both forms are used interchangeably and neither is more correct. And a sample size answer must be an integer, so the final step of every sample size calculation is a rounding decision, and the decision is always upwards.

### 1.7 Confidence in one sentence

The sentence that earns the interpretation mark, and nothing shorter, is: the confidence level is the long-run proportion of intervals produced by this procedure that contain the true parameter. Everything else that can be said about the confidence level is a consequence of that sentence, and every misinterpretation listed in Section 5 is a violation of it.

## 2. Theorems, Lemmas, and Analytical Properties

### 2.1 The high-yield results

> **Result 1 (Unbiasedness).** $\text{E}(\bar{x}) = \mu$ for any sample size.

> **Result 2 (Standard error).** $\text{SE}(\bar{x}) = \sigma/\sqrt{n}$, and the estimated version is $s/\sqrt{n}$.

> **Result 3 (Proportion standard error).** $\text{SE}(\hat{p}) = \sqrt{p\left(1-p\right)/n}$.

> **Result 4 (Interval structure).** Every interval in the topic is an estimate plus or minus a multiplier times a standard error.

> **Result 5 (Multiplier choice).** Known $\sigma$ uses $z$; unknown $\sigma$ uses $t$ on $n-1$ degrees of freedom; a proportion uses $z$.

> **Result 6 (Width).** Width is proportional to the multiplier, proportional to the spread, and inversely proportional to the square root of the sample size.

> **Result 7 (Sample size).** Inverting the margin of error gives $n = \left(z\sigma/E\right)^{2}$ for a mean and $n = z^{2}p^{*}\left(1-p^{*}\right)/E^{2}$ for a proportion.

> **Result 8 (Duality).** A value lies inside the $1-\alpha$ interval exactly when a two-sided test at level $\alpha$ does not reject it.

Eight results cover the computational content of the topic. The remaining theorems in this section explain why each holds, which is what a question asking for a derivation requires.

### 2.2 The pivot structure behind every interval

> **Theorem (Pivot inversion).** If $Q\left(\theta\right)$ has a distribution free of $\theta$, and $q$ satisfies $\text{P}\left(-q \le Q \le q\right) = 1-\alpha$, then the set of $\theta$ satisfying $-q \le Q\left(\theta\right) \le q$ is a confidence set of level $1-\alpha$.

The theorem is worth stating in the examination because it justifies every formula at once. The mean case uses

$$
Q\left(\mu\right) = \frac{\bar{x} - \mu}{\sigma/\sqrt{n}},
$$

the unknown-variance case uses the same expression with $s$ in place of $\sigma$, and the proportion case uses the same expression with $\hat{p}$ and $\sqrt{\hat{p}\left(1-\hat{p}\right)/n}$ in place. Only the distribution attached to $Q$ changes: standard normal in the first and third cases, t with $n-1$ degrees of freedom in the second.

### 2.3 The two standard-error identities

> **Theorem.** Under independent sampling, $\text{Var}(\bar{x}) = \sigma^{2}/n$; under sampling without replacement from a finite population, $\text{Var}(\bar{x}) = \left(\sigma^{2}/n\right)\left(N-n\right)/\left(N-1\right)$.

> **Theorem.** For a sample proportion, $\text{Var}(\hat{p}) = p\left(1-p\right)/n$.

Both follow from the same argument: a mean of independent terms has variance equal to the common variance divided by the number of terms. The proportion version is the special case in which the terms are indicators, so the common variance is $p\left(1-p\right)$. The finite population version differs only because the terms are negatively correlated.

The practical reading is that the standard error is the currency in which all distances in this topic are measured. A difference of $1.4$ millilitres means nothing on its own; a difference of $0.47$ standard errors is interpretable, and a difference of two standard errors is the boundary of a $95\%$ interval.

### 2.4 The t correction and when it bites

> **Theorem.** If the population is normal and $\sigma$ is estimated by $s$, then $\left(\bar{x} - \mu\right)/\left(s/\sqrt{n}\right)$ is t distributed with $n-1$ degrees of freedom.

The correction is large where it is needed and negligible where it is not. At $n = 5$ the $95\%$ two-sided multiplier is $2.776$ against the normal $1.960$, so a candidate who uses $z$ understates the margin by about twenty-nine per cent. At $n = 25$ the multiplier is $2.064$, and the understatement is about five per cent. Beyond $n$ of about a hundred the difference is under two per cent and the choice hardly matters.

Three examination consequences follow. A question that gives $\sigma$ explicitly wants $z$. A question that gives $s$ and a sample size below about thirty wants $t$. A question that gives $s$ and a sample size above about a hundred may accept either, but the marker will expect a sentence saying that the difference is negligible.

### 2.5 Wald against Wilson

> **Theorem (Wald interval).** $\hat{p} \pm z\sqrt{\hat{p}\left(1-\hat{p}\right)/n}$, approximate.

> **Theorem (Wilson interval).** The endpoints are

$$
\frac{n\hat{p} + \frac{z^{2}}{2} \pm z\sqrt{n\hat{p}\left(1-\hat{p}\right) + \frac{z^{2}}{4}}}{n + z^{2}} .
$$

The Wald interval is the one most questions expect, and the Wilson interval is the one that survives small samples and extreme proportions. The Wald limits can fall outside the interval from zero to one, which is an impossibility that a marker will notice. The Wilson limits cannot, because they are derived by solving the exact quadratic inequality rather than by substituting an estimate into the standard error.

A safe examination policy is to compute the Wald interval as required, then add one sentence: the Wilson interval is preferred when $n\hat{p}$ or $n\left(1-\hat{p}\right)$ is below ten, and here those counts are so many that the two agree closely. That sentence demonstrates exactly the judgement that the harder marks are awarded for.

### 2.6 Width and its elasticities

> **Theorem.** For the known-variance interval,

$$
W = 2z_{\alpha/2}\frac{\sigma}{\sqrt{n}} .
$$

Three comparative statements follow, and they are examined directly.

Halving the width requires quadrupling the sample, because the width falls as one over the square root of $n$. This is the single most examined consequence of the formula and the single most useful fact in study design.

Raising the confidence level from $95\%$ to $99\%$ multiplies the width by $2.576/1.960 \approx 1.314$, an increase of about thirty-one per cent. Lowering it from $95\%$ to $90\%$ multiplies the width by $0.839$, a reduction of about sixteen per cent.

Increasing the spread by a factor multiplies the width by the same factor, since $\sigma$ enters linearly. For a proportion, the spread term $\sqrt{\hat{p}\left(1-\hat{p}\right)}$ is largest at $\hat{p} = 0.5$ and equals $0.5$ there, so a proportion near one half gives the widest interval at a fixed sample size.

### 2.7 Sample size and its rounding rule

> **Theorem.** For a target margin $E$,

$$
n = \left(\frac{z_{\alpha/2}\sigma}{E}\right)^{2}, \qquad n = \frac{z_{\alpha/2}^{2}p^{*}\left(1-p^{*}\right)}{E^{2}} .
$$

Two habits prevent the standard errors. First, express $E$ in the same units as the estimate: a margin of two percentage points is $E = 0.02$, not $E = 2$. Second, round upwards, and say so explicitly, because a fractional sample size is not attainable and rounding down breaks the promise made to the reader.

When the population is finite, the corrected size is smaller:

$$
n = \frac{n_0}{1 + \frac{n_0 - 1}{N}},
$$

where $n_0$ is the uncorrected value. The formula is examined less often than the plain version but appears whenever a question mentions a known population size together with a required precision.

### 2.8 One-sided bounds and the multiplier swap

> **Theorem.** A $1-\alpha$ lower bound for a mean is $\bar{x} - z_{\alpha}\sigma/\sqrt{n}$, and an upper bound is $\bar{x} + z_{\alpha}\sigma/\sqrt{n}$.

The single difference from the two-sided case is the multiplier. For $95\%$ confidence the one-sided value is $1.645$ and the two-sided value is $1.960$. The one-sided bound is therefore closer to the estimate, which is correct: reserving error probability for a tail that will never be used is wasteful.

A one-sided question is recognised by wording. Phrases such as "at least", "no less than", "a lower bound", "exceeds with $95\%$ confidence" and "the minimum plausible value" all signal a one-sided treatment. Phrases such as "between" and "lies within" signal a two-sided treatment.

### 2.9 The finite population correction

> **Theorem.** Multiplication of the standard error by $\sqrt{\left(N-n\right)/\left(N-1\right)}$ is required when sampling without replacement from a finite population.

The factor is below one whenever $n > 1$, so the corrected interval is always narrower than the uncorrected one. This direction surprises candidates who expect a correction to be conservative. The reason is that a large sample from a small population leaves very little unobserved, so the estimate is genuinely more precise than the independent-sampling formula suggests.

The factor can change a conclusion, which is why it is examined. A test statistic of $-1.889$ does not reject a two-sided null at the $5\%$ level, but the same data with a corrected standard error of $1.685$ instead of $1.8$ give a statistic of $-2.018$, which does reject. The correction is not cosmetic.

### 2.10 Duality restated for the examination

> **Theorem.** For a two-sided test at level $\alpha$, the set of null values not rejected is exactly the confidence interval of level $1-\alpha$.

The theorem saves time in two directions. Given an interval, a test question becomes a comparison of one number with two limits. Given a test, an interval question becomes a search for the set of values that would not be rejected. The correspondence is exact only when the two procedures use the same distributional assumption, so a $z$ interval pairs with a $z$ test and a $t$ interval pairs with a $t$ test.

A frequent examination request is to explain why the interval is more informative than the test. The answer uses the duality: the interval reports, for every candidate value at once, whether it is compatible with the data, whereas the test answers the question for one value only.

### 2.11 Short-answer territory: estimator properties and the limit theorem

Some papers carry a short-answer part worth several marks, and the four estimator properties together with the central limit theorem are its usual content. Each admits a one-sentence definition and a one-sentence justification, and both sentences are needed for full credit.

> **Definition (Unbiasedness).** An estimator is unbiased if its expectation equals the parameter for every admissible value, so that repeated sampling shows no systematic lean.

> **Definition (Efficiency).** Among unbiased estimators, the efficient one has the smallest variance, and it is the preferred choice because its sampling distribution is the most concentrated about the parameter.

> **Definition (Consistency).** An estimator is consistent if it converges to the parameter in probability as the sample size grows, so that enough data guarantees arbitrary accuracy.

> **Definition (Sufficiency).** A statistic is sufficient if the conditional distribution of the sample given that statistic does not depend on the parameter, so that no further feature of the data carries additional information about it.

The two properties that are actually used in this topic are unbiasedness and consistency, and both are properties of the sample mean. Unbiasedness is established by linearity of expectation and holds at every $n$. Consistency is established by the variance formula together with Chebyshev's inequality, since $\text{Var}(\bar{x}) = \sigma^{2}/n$ tends to zero and an unbiased estimator with vanishing variance converges to its target. Efficiency is the reason the sample mean is preferred to the sample median for normal data, where the median needs about $\pi/2 \approx 1.571$ times as many observations to reach the same precision. Sufficiency is the reason the topic needs only two summary numbers, $\bar{x}$ and $s^{2}$, rather than the whole data set.

The central limit theorem supplies the fourth ingredient, and its examination statement is a single sentence: for independent observations with finite variance, the standardised sample mean converges in distribution to the standard normal, whatever the shape of the population. That sentence is the licence for every $z$ multiplier in the topic, and it is the reason a normal-based interval can be built for data that are not themselves normal. The qualification that matters in an answer is the sample size: thirty is a rough threshold for mildly skewed data, and strongly skewed data require more, especially in the tails where $99\%$ intervals live.

| Property | Holds for the sample mean | How it is shown | Why the examiner asks |
| --- | --- | --- | --- |
| Unbiasedness | at every $n$ | linearity of expectation | justifies the point estimate |
| Efficiency | for normal data | Cramér–Rao bound | justifies preferring $\bar{x}$ to the median |
| Consistency | whenever $\sigma^{2}$ is finite | variance tends to zero | justifies large-sample intervals |
| Sufficiency | for normal data | factorisation of the likelihood | justifies using only $\bar{x}$ and $s^{2}$ |

A short answer that names the property, states it formally, and attaches the sample mean as the example will earn all of its marks. A short answer that says only "unbiased means fair" will earn none, because it names no expectation and no parameter.

## 3. Formal Proofs, Derivations, and Methods

### 3.1 The derivation to reproduce under pressure

The two-sided interval for a mean with known $\sigma$ is the derivation that examiners ask for, and it takes five lines.

Step 1. Standardise and state the distribution.

$$
Z = \frac{\bar{x} - \mu}{\sigma/\sqrt{n}} \sim \text{N}\left(0,1\right)
$$

Step 2. Write the central probability.

$$
\text{P}\left(-z_{\alpha/2} \le Z \le z_{\alpha/2}\right) = 1 - \alpha
$$

Step 3. Substitute and multiply through by the standard error.

$$
\text{P}\left(\bar{x} - z_{\alpha/2}\frac{\sigma}{\sqrt{n}} \le \mu \le \bar{x} + z_{\alpha/2}\frac{\sigma}{\sqrt{n}}\right) = 1 - \alpha
$$

Step 4. Read off the limits, noting that the rearrangement required subtracting $\bar{x}$ and multiplying by minus one, which reverses the inequalities twice.

$$
L = \bar{x} - z_{\alpha/2}\frac{\sigma}{\sqrt{n}}, \qquad U = \bar{x} + z_{\alpha/2}\frac{\sigma}{\sqrt{n}}
$$

Step 5. State the interpretation as a property of the procedure, not of the particular numbers.

### 3.2 The t interval in four lines

Step 1. Replace $\sigma$ by $s$ in the standardised quantity and name the new distribution.

$$
T = \frac{\bar{x} - \mu}{s/\sqrt{n}} \sim t_{n-1}
$$

Step 2. Write the central probability with t quantiles.

$$
\text{P}\left(-t_{\alpha/2,\,n-1} \le T \le t_{\alpha/2,\,n-1}\right) = 1 - \alpha
$$

Step 3. Invert exactly as before, since $s/\sqrt{n}$ is positive.

$$
\text{P}\left(\bar{x} - t_{\alpha/2,\,n-1}\frac{s}{\sqrt{n}} \le \mu \le \bar{x} + t_{\alpha/2,\,n-1}\frac{s}{\sqrt{n}}\right) = 1 - \alpha
$$

Step 4. State the degrees of freedom explicitly. They are $n-1$, not $n$, because one degree of freedom was spent estimating the mean inside $s$.

### 3.3 The standard error of a proportion, in three lines

Step 1. Code each trial as an indicator with mean $p$ and variance $p\left(1-p\right)$.

Step 2. Note that the sample proportion is the mean of the indicators.

Step 3. Apply the variance of a sample mean.

$$
\text{Var}(\hat{p}) = \frac{p\left(1-p\right)}{n}, \qquad \text{SE}(\hat{p}) = \sqrt{\frac{p\left(1-p\right)}{n}}
$$

### 3.4 The sample size inversion

Step 1. Write the margin of error and set it equal to the target.

$$
E = z_{\alpha/2}\frac{\sigma}{\sqrt{n}}
$$

Step 2. Isolate the square root.

$$
\sqrt{n} = \frac{z_{\alpha/2}\sigma}{E}
$$

Step 3. Square, and record that the result must be rounded up.

$$
n = \left(\frac{z_{\alpha/2}\sigma}{E}\right)^{2}
$$

Step 4. For a proportion, replace $\sigma$ by the planning standard deviation $\sqrt{p^{*}\left(1-p^{*}\right)}$ and repeat the same three operations.

### 3.5 The marking-scheme algorithm

A full-mark answer to a computational question has five visible stages, and each stage usually carries a mark independently of the others.

Step 1. Write the quantities and the multiplier, naming the distribution used and the degrees of freedom if any. Markers award this mark for the declaration, not for the number.

Step 2. Write the standard error expression before evaluating it. A candidate who writes the correct expression but miscalculates loses one mark; a candidate who writes only a wrong number loses two.

Step 3. Write the margin of error as multiplier times standard error.

Step 4. State the two limits with the units attached.

Step 5. Write one sentence of interpretation naming the population, the parameter, the units and the confidence level.

The fifth stage is routinely omitted and routinely worth a mark. An answer ending at a pair of numbers is marked as incomplete regardless of the arithmetic.

### 3.6 The multiplier decision rule

The choice between $z$ and $t$ is decided by two questions asked in a fixed order.

First, is the population standard deviation $\sigma$ given in the question? If yes, use $z$ immediately and do not look further. Second, if $\sigma$ is not given but $s$ is, the sample standard deviation has been used in place of $\sigma$, so the t distribution applies with $n-1$ degrees of freedom. The size of $n$ does not change the rule; it changes only the penalty for getting it wrong, which shrinks as $n$ grows.

A third case arises with proportions. There $z$ is always used, because the interval is based on the normal approximation to the binomial rather than on an estimated variance in the same sense. The condition for using it is a large enough count of successes and failures, not the presence of a known $\sigma$.

### 3.7 The proportion method in four moves

Step 1. Compute $\hat{p} = x/n$ and record $x$ and $n$ separately, since both are needed for the Wilson form and for the condition check.

Step 2. Check the counts $n\hat{p}$ and $n\left(1-\hat{p}\right)$ against the threshold of ten. Record the check in the answer.

Step 3. Compute the standard error using $\hat{p}$ and form the Wald interval.

Step 4. If the counts fail the threshold, or if the question asks for it, compute the Wilson form and comment on the difference.

### 3.8 The ten-second check

Before the answer is handed in, four checks catch most numerical errors.

The first is that the interval is centred on the point estimate, which it must be for the Wald and normal forms. The second is that the half-width equals multiplier times standard error, and the standard error is smaller than the sample standard deviation whenever $n > 1$. The third is that the limits lie in the admissible range: proportions between zero and one, masses positive, and percentages between zero and a hundred. The fourth is that a narrower interval corresponds to a smaller confidence level or a larger sample, never the reverse.

## 4. Representative Worked Examples and Solutions

### 4.1 Question pattern one: an interval when the spread must be estimated

A random sample of $20$ packets of a chemical has a mean mass of $14.32$ grams and a standard deviation of $2.41$ grams. The masses are known to be normally distributed.

Part (a). Construct a $95\%$ confidence interval for the population mean mass.

Part (b). Construct a $99\%$ confidence interval from the same data and explain the difference in width.

### 4.2 Model solution: t interval with marking points

Step 1. List the quantities and fix the multiplier.

$$
n = 20, \quad \bar{x} = 14.32, \quad s = 2.41, \quad \text{df} = 19, \quad t_{0.025,\,19} = 2.093
$$

Step 2. Compute the estimated standard error.

$$
\widehat{\text{SE}} = \frac{s}{\sqrt{n}} = \frac{2.41}{\sqrt{20}} = \frac{2.41}{4.4721} \approx 0.5389
$$

Step 3. Compute the margin of error for part (a).

$$
E = 2.093 \times 0.5389 \approx 1.1279
$$

Step 4. State the limits for part (a).

$$
L = 14.32 - 1.1279 = 13.19, \qquad U = 14.32 + 1.1279 = 15.45
$$

Step 5. Interpret part (a) in one sentence.

We are $95\%$ confident that the mean mass of all packets produced lies between $13.19$ grams and $15.45$ grams.

Step 6. Repeat for part (b) with the $99\%$ quantile on $19$ degrees of freedom.

$$
t_{0.005,\,19} = 2.861, \qquad E = 2.861 \times 0.5389 \approx 1.5418
$$

Step 7. State the limits for part (b).

$$
L = 14.32 - 1.5418 = 12.78, \qquad U = 14.32 + 1.5418 = 15.86
$$

Step 8. Explain the difference. The width has risen from $2.26$ grams to $3.08$ grams because the multiplier has risen from $2.093$ to $2.861$. Nothing about the data has changed; the wider interval is the price of a stronger guarantee.

Step 9. Add the observation that earns the judgement mark. Had the normal multiplier $1.96$ been used in part (a), the margin would have been $1.0562$ and the interval from $13.26$ to $15.38$, which is about six per cent too narrow. With only $19$ degrees of freedom the t correction cannot be ignored.

**Marking points.** M1, one mark for stating $n$, $\bar{x}$, $s$ and the correct degrees of freedom. M2, one mark for the standard error expression $s/\sqrt{n}$ and one for its value. M3, one mark for the correct multiplier $2.093$ with $19$ degrees of freedom. M4, one mark for the margin and one for both limits with units. M5, one mark for the interpretation mentioning the population and the confidence level. M6, one mark for the $99\%$ interval with the correct multiplier $2.861$. M7, one mark for the explanation of the width change in terms of the multiplier. M8, one mark for the comment on the t correction.

### 4.3 Question pattern two: a proportion with a design requirement

In a random sample of $250$ customers, $60$ say they would recommend a product.

Part (a). Construct a $95\%$ Wald confidence interval for the population proportion.

Part (b). Construct the Wilson interval and compare.

Part (c). How large a sample would be needed to estimate the proportion to within three percentage points at $95\%$ confidence, using the sample value as a planning value?

Part (d). State the sample size that would be required had no planning value been available.

### 4.4 Model solution: three linked parts and one design question

Step 1. Compute the sample proportion and record the counts.

$$
\hat{p} = \frac{60}{250} = 0.24, \qquad n\hat{p} = 60, \qquad n\left(1-\hat{p}\right) = 190
$$

Step 2. Check the condition for the Wald form. Both counts exceed ten, so the normal approximation is adequate and the Wald interval may be reported.

Step 3. Compute the estimated standard error.

$$
\sqrt{\frac{0.24 \times 0.76}{250}} = \sqrt{\frac{0.1824}{250}} = \sqrt{0.0007296} \approx 0.02701
$$

Step 4. Compute the margin of error.

$$
E = 1.96 \times 0.02701 \approx 0.05294
$$

Step 5. State the Wald limits for part (a).

$$
L = 0.24 - 0.05294 = 0.1871, \qquad U = 0.24 + 0.05294 = 0.2929
$$

Step 6. Interpret part (a). We are $95\%$ confident that the proportion of all customers who would recommend the product lies between $18.7\%$ and $29.3\%$.

Step 7. Compute the Wilson centre for part (b), using $z^{2} = 3.8416$.

$$
\tilde{p} = \frac{60 + 1.9208}{250 + 3.8416} = \frac{61.9208}{253.8416} \approx 0.2439
$$

Step 8. Compute the Wilson half-width.

$$
h = 1.96\sqrt{\frac{0.2439 \times 0.7561}{253.8416}} \approx 1.96 \times 0.02695 \approx 0.05283
$$

Step 9. State the Wilson limits.

$$
L = 0.2439 - 0.05283 = 0.1911, \qquad U = 0.2439 + 0.05283 = 0.2968
$$

Step 10. Compare the two forms. The centres differ by $0.0039$ and the widths by $0.0002$. At this sample size and this proportion the linear approximation in the Wald form is harmless, and either interval supports the same conclusion.

Step 11. Compute the sample size for part (c), with $E = 0.03$ and $p^{*} = 0.24$.

$$
n = \frac{1.96^{2} \times 0.24 \times 0.76}{0.03^{2}} = \frac{0.7007}{0.0009} \approx 778.56
$$

Step 12. Round upwards and state the answer.

$$
n = 779
$$

Step 13. Compute the sample size for part (d) with the safe planning value $p^{*} = 0.5$.

$$
n = \frac{1.96^{2} \times 0.5 \times 0.5}{0.03^{2}} = \frac{0.9604}{0.0009} \approx 1067.11
$$

Step 14. Round upwards and explain the difference.

$$
n = 1068
$$

The difference of $289$ customers is the cost of ignorance about the true proportion. Choosing $0.5$ guarantees the target for any value of $p$, because $p\left(1-p\right)$ is maximised there, while a planning value near $0.24$ exploits what the pilot sample has already revealed.

**Marking points.** M1, one mark for $\hat{p} = 0.24$ and one for checking $n\hat{p}$ and $n\left(1-\hat{p}\right)$ against ten. M2, one mark for the standard error expression and one for its value. M3, one mark for the margin and one for both limits as proportions or percentages, consistently. M4, one mark for the interpretation naming the population. M5, one mark for the Wilson centre with the correct $z^{2}/2$ adjustment, and one for the Wilson half-width. M6, one mark for the comparison and for the statement that the two forms agree here. M7, one mark for $E = 0.03$ expressed as a proportion rather than as $3$. M8, one mark for the correct sample size formula and one for rounding upwards to $779$. M9, one mark for using $p^{*} = 0.5$ in part (d) and one for the explanation of why $0.5$ is the safe choice.

### 4.5 Question pattern three: a finite population, a one-sided bound and a test

A district has $800$ households. A random sample of $100$ households uses a mean of $42.6$ units of electricity per week, and the standard deviation of weekly use in the district is known to be $18$ units.

Part (a). Construct a $95\%$ confidence interval for the mean weekly use, applying the finite population correction.

Part (b). Construct a $95\%$ lower confidence bound for the mean weekly use.

Part (c). Test at the $5\%$ level whether the mean weekly use is $46$ units, and state what would have happened had the correction been omitted.

### 4.6 Model solution: three parts, one set of ingredients

Step 1. Record the quantities.

$$
N = 800, \quad n = 100, \quad \bar{x} = 42.6, \quad \sigma = 18, \quad z_{0.025} = 1.96
$$

Step 2. Compute the uncorrected standard error.

$$
\frac{\sigma}{\sqrt{n}} = \frac{18}{10} = 1.8
$$

Step 3. Compute the finite population correction factor.

$$
\sqrt{\frac{N-n}{N-1}} = \sqrt{\frac{800-100}{800-1}} = \sqrt{\frac{700}{799}} \approx \sqrt{0.8761} \approx 0.9360
$$

Step 4. Apply the factor.

$$
\text{SE} = 1.8 \times 0.9360 = 1.6848
$$

Step 5. Compute the margin of error for part (a).

$$
E = 1.96 \times 1.6848 \approx 3.3022
$$

Step 6. State the interval.

$$
L = 42.6 - 3.3022 = 39.30, \qquad U = 42.6 + 3.3022 = 45.90
$$

Step 7. Interpret part (a). We are $95\%$ confident that the mean weekly use of all $800$ households lies between $39.30$ and $45.90$ units.

Step 8. Compute the one-sided allowance for part (b) with the one-sided multiplier $1.645$.

$$
1.645 \times 1.6848 \approx 2.7715
$$

Step 9. State the lower bound.

$$
L = 42.6 - 2.7715 = 39.83
$$

Step 10. Interpret part (b). We are $95\%$ confident that the mean weekly use is at least $39.83$ units, a bound that is higher, and therefore stronger, than the lower limit of the two-sided interval.

Step 11. Perform the test for part (c). State the hypotheses and compute the statistic with the corrected standard error.

$$
H_0: \mu = 46, \qquad H_1: \mu \ne 46, \qquad z = \frac{42.6 - 46}{1.6848} = \frac{-3.4}{1.6848} \approx -2.018
$$

Step 12. Compare with the critical value and conclude.

$$
\left|-2.018\right| = 2.018 > 1.96
$$

The null hypothesis is rejected at the $5\%$ level. The interval of part (a) confirms this, since $46$ lies above the upper limit of $45.90$.

Step 13. Repeat the test without the correction to answer the final part.

$$
z = \frac{42.6 - 46}{1.8} = -1.889, \qquad \left|-1.889\right| = 1.889 < 1.96
$$

Step 14. Interpret the comparison. Omitting the correction would have led to the opposite conclusion: the null value would not have been rejected, and the uncorrected interval would have run from $39.07$ to $46.13$, containing $46$. The correction changes the decision, which is why a question that states the population size must be answered with it.

**Marking points.** M1, one mark for the uncorrected standard error and one for the correction factor. M2, one mark for the corrected standard error, which is the discriminating step. M3, one mark for the margin and one for both limits. M4, one mark for the interpretation. M5, one mark for using $1.645$ rather than $1.96$ in part (b), and one for the correct direction of the bound. M6, one mark for the test statistic and one for the comparison with $1.96$. M7, one mark for linking the conclusion to the interval. M8, one mark for showing that the uncorrected test gives the opposite conclusion, and one for explaining why the correction is legitimate rather than optional.

### 4.7 Question pattern four: designing the study

A geologist wishes to estimate the mean concentration of a mineral in a region to within $2.5$ parts per million at $95\%$ confidence. A pilot study of twelve specimens gave a standard deviation of $18$ parts per million.

Part (a). Find the required sample size.

Part (b). The budget allows only $150$ specimens. State the precision that can be achieved with that budget.

Part (c). State what confidence level could be used with $150$ specimens to achieve the original precision.

### 4.8 Model solution: invert the margin, then invert it again

Step 1. Record the planning values and the target.

$$
\sigma \approx 18, \quad E = 2.5, \quad z_{0.025} = 1.96
$$

Step 2. Apply the sample size formula for part (a).

$$
n = \left(\frac{1.96 \times 18}{2.5}\right)^{2} = \left(\frac{35.28}{2.5}\right)^{2} = \left(14.112\right)^{2} \approx 199.15
$$

Step 3. Round upwards.

$$
n = 200
$$

Step 4. Explain the rounding. A sample of $199$ would give a margin of

$$
1.96 \times \frac{18}{\sqrt{199}} \approx 1.96 \times 1.2761 \approx 2.501,
$$

which exceeds the target by a small amount, so $199$ is not admissible and $200$ is.

Step 5. Compute the precision available with $150$ specimens for part (b).

$$
E = 1.96 \times \frac{18}{\sqrt{150}} = 1.96 \times 1.4697 \approx 2.881
$$

Step 6. Interpret part (b). With $150$ specimens the estimate is accurate to about $2.88$ parts per million rather than $2.5$, so the study would fall short of its design target by about fifteen per cent.

Step 7. Compute the confidence level attainable at the original precision with $150$ specimens for part (c). The required multiplier is the ratio of the target margin to the standard error.

$$
z = \frac{2.5}{1.4697} \approx 1.701
$$

Step 8. Convert the multiplier to a confidence level. A standard normal variable exceeds $1.701$ in each tail with probability about $0.0445$, so the two-sided confidence level is

$$
1 - 2\left(0.0445\right) = 0.911.
$$

Step 9. Interpret part (c). With $150$ specimens the original precision can be claimed only at about $91\%$ confidence, so the design is a genuine trade-off between precision and reliability, not a rounding problem.

Step 10. Add the sensitivity remark. Since the sample size depends on the square of the planning standard deviation, an understated pilot value is dangerous: if the true standard deviation were $20$ rather than $18$, the required size would be about $246$ rather than $200$.

**Marking points.** M1, one mark for the correct formula and one for substituting the target margin as $2.5$ rather than as a percentage. M2, one mark for the arithmetic and one for rounding upwards with a reason. M3, one mark for the demonstration that $199$ fails the target. M4, one mark for the margin achievable with $150$ specimens. M5, one mark for inverting the margin to obtain $z = 1.701$ and one for converting it into a confidence level. M6, one mark for the sensitivity remark, which is the discriminating mark in this question.

## 5. Mathematical Extensions, Limits, and Common Errors

### 5.1 The four traps that cost the most marks

**Trap one: reading the confidence level as a probability about a fixed parameter.** The offending sentence is "there is a $95\%$ probability that $\mu$ lies between $13.19$ and $15.45$". The parameter is a fixed number and the limits are fixed numbers, so there is no probability left to state. The correct sentence refers to the procedure: $95\%$ of intervals built this way capture $\mu$. A second version of the same trap replaces the parameter by the data and claims that $95\%$ of the observations lie inside the interval, which confuses a confidence interval with a tolerance interval.

**Trap two: using $z$ when $t$ is required.** The trigger is the word "estimated" or the absence of a population standard deviation. At $19$ degrees of freedom the correct multiplier is $2.093$ and the normal value is $1.960$; using the normal value makes the interval about six per cent too narrow and understates the margin by about the same amount. The error is invisible in the arithmetic and fatal to the conclusion, because it claims a precision the data do not support.

**Trap three: omitting the finite population correction.** When the question supplies $N$ and $n$ with $n/N$ appreciable, the factor $\sqrt{\left(N-n\right)/\left(N-1\right)}$ must be applied. The omission widens the interval and can reverse a test conclusion, as the third model solution shows. The direction of the error is conservative for an interval but wrong for a decision.

**Trap four: misinterpreting the interval as a statement about individuals.** The sentence "we are $95\%$ confident that a randomly chosen packet weighs between $13.19$ and $15.45$ grams" is wrong on two counts: the interval is for the mean, not for an individual, and the confidence level does not apply to predictions. A prediction interval, which is much wider, would be the correct object for that question.

A fifth trap is worth naming separately because it is arithmetic rather than conceptual: treating the margin of error as the full width. A question demanding a margin of error of $2$ units requires an interval of width $4$, and a candidate who designs a study for a width of $2$ has bought four times more precision than was asked for.

### 5.2 The error catalogue with its usual cost

| Error | Consequence | Usual deduction |
| --- | --- | --- |
| Dividing by $n$ instead of $\sqrt{n}$ | standard error far too small | method mark and accuracy mark |
| Using $1.96$ with small $n$ and unknown $\sigma$ | interval too narrow | multiplier mark |
| Using $1.96$ for a one-sided $95\%$ bound | bound too conservative | multiplier mark |
| Ignoring the finite population correction | interval too wide, decision may reverse | accuracy marks |
| Rounding a sample size down | target margin not met | final mark |
| Reporting limits without units | uninterpretable answer | interpretation mark |
| No interpretation sentence | answer judged incomplete | interpretation mark |
| $95\%$ read as a probability about $\mu$ | conceptual error | interpretation mark and often more |

The pattern in the right-hand column is worth noticing. Arithmetic slips cost one mark and are usually forgiven downstream, because a marker follows the candidate's own numbers. Errors of judgement cost the mark for the judgement and often the mark for the interpretation as well, because the interpretation then states something false.

### 5.3 Limits of every method in the topic

The normal and t intervals for a mean require a normal population, or a large sample by the central limit theorem. Small samples from strongly skewed populations break both, and no multiplier repairs them. A $99\%$ interval is more sensitive to this than a $95\%$ interval, because tail accuracy converges more slowly than central accuracy.

The Wald interval for a proportion requires both $n\hat{p}$ and $n\left(1-\hat{p}\right)$ to be at least about ten. Below that threshold the limits can escape the unit interval and the coverage falls well short of nominal. The Wilson interval is the appropriate replacement.

Every interval in the topic assumes a probability sample. A convenience sample, a volunteer sample or a sample with substantial nonresponse does not have the sampling distribution on which the formula rests, so the stated confidence level is nominal only. This is the limitation that no amount of arithmetic can detect, and a sentence acknowledging it is often worth a mark in a discussion question.

Finally, the intervals are for a single parameter at a time. If several parameters are estimated from the same data and each is given a $95\%$ interval, the chance that all of them are simultaneously covered is below $95\%$. Simultaneous coverage requires a Bonferroni adjustment, in which each interval is built at level $1 - \alpha/k$ for $k$ parameters.

### 5.4 Time strategy in the examination

Estimation questions are usually quick once the multiplier has been chosen correctly, so the time is best spent on the choice rather than on the arithmetic.

| Stage | Time | What to do |
| --- | --- | --- |
| Read and classify | 1 minute | mean or proportion, one-sided or two-sided, finite population or not |
| Write the quantities | 1 minute | five quantities, multiplier, degrees of freedom |
| Standard error | 2 minutes | expression first, then value |
| Interval or bound | 2 minutes | margin, then limits, then units |
| Interpretation | 1 minute | population, parameter, units, confidence level |
| Check | 1 minute | centre, half-width, admissible range |

A full interval question should take about eight minutes, and a three-part question about fifteen. If a candidate is still computing a square root after four minutes, the multiplier or the standard error expression is probably wrong, and it is faster to restart the calculation than to hunt for the slip.

Two time-saving rules are worth adopting. Write the standard error expression before evaluating it, because a marker can award the method mark even when the arithmetic fails, and a candidate can see the method is right while hunting the slip. And keep the confidence level and the multiplier on the same line, because the commonest single mistake in the topic is a mismatch between them.

### 5.5 Revision checklist

The following checklist is ordered by the frequency with which each item is examined. An item is ticked only when the corresponding calculation can be performed without notes.

- State the three definitions in the wording of Section 1.2, including the words "single value", "range" and "procedure".
- Compute $\bar{x}$ and $s$ from raw data, and state which one is the point estimate and which is the spread.
- Write the standard error of a mean in both forms, with $\sigma$ and with $s$.
- Choose between $z$ and $t$ from the wording of a question, and state the degrees of freedom.
- Reproduce the five-line derivation of the interval from the pivot.
- Build a two-sided interval for a mean with known $\sigma$ and with unknown $\sigma$.
- Build a Wald interval for a proportion and check the counts against ten.
- Build a Wilson interval and explain when it is preferred.
- Use the one-sided multiplier $1.645$ for a $95\%$ lower or upper bound, and explain why it is smaller than $1.960$.
- Apply the finite population correction and explain its direction.
- Invert a margin of error to obtain a sample size for a mean and for a proportion, and round upwards.
- Use $p^{*} = 0.5$ when no planning value is available, and explain why it is safe.
- Explain the effect of confidence level, sample size and variability on width, with the factor by which each acts.
- State the duality between intervals and tests and use it in both directions.
- Write an interpretation sentence that names the population, the parameter, the units and the confidence level.
- Name the four traps of Section 5.1 and the correction for each.

### 5.6 The final-week schedule

Six short sessions are more effective than one long one, because the material is procedural and procedures are consolidated by spaced repetition.

Day one. Rewrite the formula sheet from memory and check it. Compute two intervals, one for a mean and one for a proportion, from raw data.

Day two. Reproduce the pivot derivation twice, once with $z$ and once with $t$. Then answer a question that supplies $\sigma$ and a question that supplies only $s$, and note the difference in the multiplier.

Day three. Work the four model solutions of Section 4 without looking at the answers, then compare step by step. Mark the work against the marking points.

Day four. Do the sample size calculations in both directions: given a target margin find $n$, and given $n$ find the margin. Include one finite population case.

Day five. Write out the four traps and the correct statements that replace them. Practise the interpretation sentence until it can be produced in one line.

Day six. Attempt a full past paper under time pressure, then mark it against the checklist of Section 5.5 and list only the unticked items for a final review.

The night before the examination, read the checklist and the trap list and nothing else. The arithmetic is already there; what fails under pressure is the choice of multiplier and the interpretation sentence, and both are verbal skills that a last reading consolidates.
