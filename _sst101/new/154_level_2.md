## 1. Foundational Concepts, Definitions, and Axioms

### 1.1 One problem, five vocabularies

Applied statistics is a single method wearing five professional costumes. In every field the structure is identical: a population of units is defined, a variable is measured on a sample drawn from it, a summary of the sample is computed, a probability model converts that summary into a statement about the population, and a measure of reliability qualifies the statement. The differences between economics, business, medicine, the social sciences and engineering are differences in what the variable is, how the sample is obtained, and what a mistake costs.

That last difference matters more than is usually admitted. When a retail chain mis-forecasts demand, the error is absorbed by inventory and written off. When a screening programme misclassifies a patient, the error is absorbed by a human body. The mathematics of the two errors is the same; the asymmetry of their consequences dictates different standards of evidence, different sample sizes, and different reporting conventions.

### 1.2 The two modes of use

The distinction between description and inference is a distinction of intent, not of technique. The same arithmetic can serve either mode.

> **Definition (Descriptive statistics).** Descriptive statistics uses numerical and graphical methods to look for patterns in a data set and to present that information in a convenient form.

> **Definition (Inferential statistics).** Inferential statistics uses sample data to make estimates, decisions, predictions, or other generalizations about a larger set of data.

A statement such as "the mean of these 80 invoices is 4200 units of currency" is descriptive, because it describes the eighty invoices actually examined. The statement "the mean invoice value in the whole ledger lies between 3900 and 4500 units of currency, with 95 per cent confidence" is inferential, because it makes a claim about invoices never examined and attaches a quantified uncertainty to that claim. The inference is possible only because a probability model was assumed for the sampling process; without that model, the second sentence has no more content than the first.

### 1.3 Formal vocabulary of an applied study

> **Definition (Population, variable, sample, inference, reliability).** A population is a set of units, usually people, objects, transactions, or events, that we are interested in studying. A variable is a characteristic or property of an individual population unit. A sample is a subset of the units of a population. A statistical inference is an estimate, prediction, or some other generalization about a population based on information contained in a sample. A measure of reliability is a statement, usually associated with a statistical inference, that quantifies confidence in it.

Beyond the five elements, applied work requires three further formal objects.

> **Definition (Estimator and estimate).** An estimator is a rule, specified before the data are seen, that assigns a value to each possible sample. An estimate is the value the rule takes on the particular sample observed.

> **Definition (Standard error).** The standard error of an estimator is the standard deviation of its sampling distribution; it measures how much the estimate would vary if the sampling were repeated.

> **Definition (Bias).** The bias of an estimator is the difference between the expected value of the estimator over repeated sampling and the true value of the parameter.

The distinction between standard error and bias is the distinction between precision and accuracy. An estimator with a small standard error and a large bias produces tight intervals around the wrong number, and no increase in sample size will repair it.

### 1.4 Measurement scales and the arithmetic they licence

Applied work is constrained by measurement. Nominal data support only classification and counting, so the only summary is a set of proportions. Ordinal data support ordering, so medians and ranks are legitimate but means are a convention. Interval data support differences but not ratios, so a temperature of 20 degrees is not "twice as warm" as 10 degrees. Ratio data support the full arithmetic, including the coefficient of variation, because the zero is meaningful.

The classification matters procedurally. A Likert item is ordinal, so a mean of the codes 1 to 5 describes an average code rather than an average amount of agreement; the claim that the average respondent sits between "neutral" and "agree" requires an additional assumption that the five points are equally spaced. That assumption is usually made and should usually be declared.

### 1.5 Definitions for economics

> **Definition (Price relative).** For item $i$, the price relative comparing period $1$ with period $0$ is $p_{1i}/p_{0i}$, usually multiplied by 100.

> **Definition (Index number).** An index number expresses the value of a variable, or of the price of a basket of goods, in one period as a percentage of its value in a base period.

> **Definition (Laspeyres price index).** With base-period quantities $q_{0i}$ held fixed,
> 
> $$
> I_L = \frac{\sum_{i=1}^{k} p_{1i}q_{0i}}{\sum_{i=1}^{k} p_{0i}q_{0i}} \times 100 .
> $$

> **Definition (Paasche price index).** With current-period quantities $q_{1i}$,
> 
> $$
> I_P = \frac{\sum_{i=1}^{k} p_{1i}q_{1i}}{\sum_{i=1}^{k} p_{0i}q_{1i}} \times 100 .
> $$

> **Definition (Base-weighted and current-weighted aggregates).** A base-weighted index fixes the quantity weights at a reference period; a current-weighted index revises them at every comparison period. The first measures the cost of a constant standard of living, and the second measures the cost of the current pattern of consumption.

> **Definition (Real and nominal quantities).** A nominal quantity is measured in current money; a real quantity is measured in base-period money and is obtained by dividing the nominal quantity by an appropriate price index.

The distinction between real and nominal is the single most consequential definition in applied economics, because a nominal increase accompanied by a larger price increase is a real decline.

### 1.6 Definitions for business

> **Definition (Fraction nonconforming).** If $D$ items in a sample of $n$ are defective, the sample fraction nonconforming is $\hat{p} = D/n$.

> **Definition (Control chart).** A control chart is a time-ordered plot of a statistic computed from successive subgroups, together with a centre line and control limits derived from the natural variability of the statistic.

> **Definition (Control limits).** The upper and lower control limits are the centre line plus and minus $k$ standard errors of the plotted statistic, with $k$ conventionally equal to 3.

> **Definition (Demand function and elasticity).** A demand function expresses quantity demanded as a function of price and other variables. The point elasticity of demand with respect to price is
> 
> $$
> \varepsilon = \frac{p}{Q}\cdot\frac{dQ}{dp},
> $$
> 
> and for a linear demand function $Q = a + bp$ it equals $bp/Q$.

> **Definition (Sales forecast).** A sales forecast is a prediction of future sales obtained from a fitted model, reported as a central value together with a prediction interval.

The convention $k = 3$ is not arbitrary. It is chosen so that a stable process generates a false signal rarely, and the arithmetic of that rarity is derived in Section 3.

### 1.7 Definitions for medicine

> **Definition (Prevalence and incidence).** Prevalence is the proportion of a population that has a condition at a specified time. Incidence is the number of new cases arising per unit of person-time at risk.

> **Definition (Sensitivity and specificity).** Sensitivity is the probability of a positive test given that the condition is present; specificity is the probability of a negative test given that the condition is absent.

> **Definition (Predictive values).** The predictive value of a positive test is the probability that the condition is present given a positive test; the predictive value of a negative test is the probability that the condition is absent given a negative test.

> **Definition (Likelihood ratio).** The positive likelihood ratio is $\text{sens}/(1-\text{spec})$ and the negative likelihood ratio is $(1-\text{sens})/\text{spec}$.

> **Definition (Risk, relative risk, risk difference, odds ratio).** For risks $r_1$ in the treated group and $r_0$ in the control group, the relative risk is $r_1/r_0$, the absolute risk reduction is $r_0 - r_1$, and the odds ratio is
> 
> $$
> \text{OR} = \frac{r_1/(1-r_1)}{r_0/(1-r_0)} .
> $$
> 
> The number needed to treat is the reciprocal of the absolute risk reduction.

> **Definition (Survival function and hazard).** The survival function $S(t)$ is the probability of surviving beyond time $t$. The hazard function $h(t)$ is the instantaneous failure rate among those still at risk.

The distinction between a ratio measure and an absolute measure is the distinction between how much the risk is multiplied and how many people are affected. A halving of a risk from 0.02 to 0.01 is a relative risk of 0.5, which sounds dramatic, and an absolute reduction of one percentage point, which may not justify the cost.

### 1.8 Definitions for the social sciences

> **Definition (Survey measurement).** A survey measures a construct by asking questions; the measurement is a response, not an observation of a physical quantity, and it carries response error in addition to sampling error.

> **Definition (Likert scale).** A Likert item offers an ordered set of response categories, conventionally five or seven, coded by integers; a Likert scale is the sum or mean of several such items intended to measure one construct.

> **Definition (Sampling design).** A sampling design specifies the mechanism by which units enter the sample: simple random sampling, stratified sampling, systematic sampling, cluster sampling, or a multistage combination.

> **Definition (Index construction).** A composite index combines several indicators into one number by rescaling each indicator to a common range and then aggregating, usually by a weighted arithmetic mean or a geometric mean.

> **Definition (Design effect).** The design effect is the ratio of the variance of an estimator under the actual sampling design to its variance under simple random sampling of the same size; a value above one means the effective sample size is smaller than the nominal one.

The design effect is the reason headline sample sizes mislead. A cluster sample of 4000 respondents from 40 villages may carry the information of fewer than 1500 independent respondents, because respondents in one village resemble one another.

### 1.9 Definitions for engineering

> **Definition (Specification limits and tolerance).** Specification limits are the bounds within which a product is acceptable, fixed by design. A tolerance interval is a statistical interval expected to contain a stated proportion of the population of produced items with a stated confidence.

> **Definition (Process capability).** With specification limits $L$ and $U$ and process standard deviation $\sigma$,
> 
> $$
> C_p = \frac{U-L}{6\sigma}, \qquad C_{pk} = \min\left(\frac{U-\mu}{3\sigma}, \frac{\mu-L}{3\sigma}\right).
> $$

> **Definition (Reliability function).** The reliability $R(t)$ is the probability that an item performs its required function for a stated period under stated conditions; for a constant hazard $\lambda$, $R(t) = e^{-\lambda t}$ and the mean time to failure is $1/\lambda$.

> **Definition (Designed experiment).** A designed experiment is a planned set of runs in which controlled factors are varied systematically so that their effects can be estimated independently of one another.

> **Definition (Calibration).** Calibration is the estimation of the relationship between an instrument reading and the true value of the quantity, together with the inverse use of that relationship to infer a true value from a reading.

### 1.10 The axioms of an applied study

Four working principles govern every application below, and each is stated as a rule that can be violated.

Axiom 1 (Definition before measurement). The population, the variable and the decision rule must be fixed before the data are examined. Otherwise the analysis can always be made to produce a preferred answer.

Axiom 2 (Randomisation or representativeness). Either units are allocated to treatments at random, or they are selected from the population by a known probability mechanism. Without one of these, the sampling error of the estimate may be computable while the bias is not.

Axiom 3 (Uncertainty is part of the answer). Every inferential statement carries a standard error, an interval, or a confidence. A number without a measure of reliability is a description masquerading as a finding.

Axiom 4 (Proportionality of evidence to cost). The strength of the design must be commensurate with the cost of an error. A study whose mistake would harm people requires stronger evidence than one whose mistake would misplace an order.

## 2. Theorems, Lemmas, and Analytical Properties

### 2.1 Properties required of a price index

A price index is a function of prices and quantities, and four properties are conventionally required of it.

> **Property (Proportionality).** If every price is multiplied by a constant $c$, the index is multiplied by $c$.

> **Property (Commensurability).** The index is invariant to the units in which prices and quantities are measured, provided a unit change is applied consistently.

> **Property (Determinateness).** The index does not vanish, become infinite, or become negative for positive prices and quantities.

> **Property (Time reversal).** An index that compares period 1 with period 0 should be the reciprocal of the index that compares period 0 with period 1, multiplied by 100 appropriately.

The Laspeyres index satisfies proportionality and commensurability but fails time reversal and, generally, factor reversal. The Fisher index, defined as the geometric mean of the Laspeyres and Paasche indexes, satisfies both reversal tests, which is why it is preferred in official statistics.

> **Theorem (Laspeyres-Paasche ordering).** If the quantity weights are revised towards items whose relative prices have fallen, then $I_P \le I_L$.

The proof is presented in Section 3.2. The economic content is substitution: when a price rises, households buy less of it, so a base-weighted index overstates the cost of the current standard of living.

### 2.2 Properties of the least squares line

> **Theorem (Normal equations).** The minimisers of $\sum_{i=1}^{n}\left(y_i - a - bx_i\right)^2$ satisfy
> 
> $$
> \sum_{i=1}^{n}\left(y_i - a - bx_i\right) = 0, \qquad \sum_{i=1}^{n}x_i\left(y_i - a - bx_i\right) = 0 .
> $$

Two consequences are used constantly. First, the fitted line passes through the point of means, so $\bar{y} = a + b\bar{x}$. Second, the residuals sum to zero, so the fitted values and the residuals are uncorrelated. Neither consequence requires normality; both are algebraic.

> **Theorem (Coefficient of determination).** With $S_{yy}$ the corrected total sum of squares and $S_{xy}$, $S_{xx}$ the corrected sums of products and squares,
> 
> $$
> r^{2} = \frac{S_{xy}^{2}}{S_{xx}S_{yy}}, \qquad r = \frac{S_{xy}}{\sqrt{S_{xx}S_{yy}}} .
> $$

The square of the correlation equals the proportion of the corrected total variation explained by the line, which is what licenses the phrase "the model explains 99.6 per cent of the variation" in a business forecast.

### 2.3 Bayes and the base-rate property

> **Theorem (Bayes for a dichotomous test).** With $D$ the event of disease and $T^{+}$ a positive test,
> 
> $$
> P\left(D \mid T^{+}\right) = \frac{P\left(T^{+} \mid D\right)P(D)}{P\left(T^{+} \mid D\right)P(D) + P\left(T^{+} \mid D'\right)P(D')} .
> $$

> **Theorem (Monotonicity of the predictive value in prevalence).** For fixed sensitivity and specificity, the predictive value of a positive test is strictly increasing in the prevalence, provided both sensitivity and specificity exceed one half.

This monotonicity theorem is the formal statement of the clinician's rule of thumb that a test is more informative in a population where the disease is common. A screening test applied to the general population will produce mostly false positives even when its sensitivity and specificity both exceed 0.9.

> **Property (Odds form).** In odds,
> 
> $$
> \frac{P\left(D \mid T^{+}\right)}{P\left(D' \mid T^{+}\right)} = \frac{P\left(T^{+} \mid D\right)}{P\left(T^{+} \mid D'\right)} \cdot \frac{P(D)}{P(D')} ,
> $$
> 
> so a positive result multiplies the prior odds of disease by the positive likelihood ratio.

### 2.4 Sampling properties used in survey inference

> **Theorem (Mean and variance of a sample proportion).** For $n$ independent Bernoulli trials with success probability $p$, the sample proportion has
> 
> $$
> E\left(\hat{p}\right) = p, \qquad \text{Var}\left(\hat{p}\right) = \frac{p(1-p)}{n} .
> $$

> **Theorem (Central limit theorem for a proportion).** As $n$ increases, the standardised quantity
> 
> $$
> \frac{\hat{p} - p}{\sqrt{p(1-p)/n}}
> $$
> 
> converges in distribution to the standard normal distribution.

The practical rule is that the normal approximation is adequate when both $n\hat{p}$ and $n(1-\hat{p})$ exceed about ten; otherwise an exact binomial interval is required.

> **Theorem (Design effect and effective sample size).** Under cluster sampling the variance of a mean is inflated by a factor
> 
> $$
> \text{deff} = 1 + (m-1)\rho ,
> $$
> 
> where $m$ is the cluster size and $\rho$ the intraclass correlation, so the effective sample size is $n/\text{deff}$.

### 2.5 Survival and mortality quantities

> **Theorem (Relation between survival and hazard).** For a continuous failure time with hazard $h(t)$,
> 
> $$
> S(t) = \exp\left(-\int_{0}^{t}h(u)\,du\right).
> $$

> **Theorem (Product-limit estimator).** With distinct failure times $t_j$, $d_j$ failures at $t_j$ and $n_j$ subjects at risk just before $t_j$,
> 
> $$
> \hat{S}(t) = \prod_{t_j \le t}\left(1 - \frac{d_j}{n_j}\right).
> $$

The product-limit form is the Kaplan-Meier estimator. Its essential feature is that subjects censored between failure times leave the risk set without contributing a failure, which is how incomplete follow-up is handled without discarding information.

> **Definition (Crude mortality rate).** The crude mortality rate is the number of deaths in a period divided by the person-time at risk in that period, usually expressed per 1000 person-years.

### 2.6 Control-chart properties

> **Theorem (Distribution of the subgroup mean).** If subgroups of size $n$ are drawn from a process with mean $\mu$ and standard deviation $\sigma$, the subgroup mean has mean $\mu$ and standard deviation $\sigma/\sqrt{n}$.

> **Theorem (False-alarm probability).** With three-sigma limits and a normally distributed statistic, the probability that a single plotted point falls outside a limit while the process is unchanged is
> 
> $$
> 2\left(1 - \Phi(3)\right) = 0.0027 .
> $$

> **Theorem (Average run length).** For independent plotted statistics, the average number of points plotted before a false alarm is $1/0.0027 = 370.4$.

The average run length is the figure that justifies the choice $k=3$. Two-sigma limits would alarm on average every 22 points, which is too often to be useful; four-sigma limits would alarm once in about 31 000 points, which is too rarely to catch a real shift promptly.

### 2.7 Capability and expected nonconformance

> **Theorem (Expected fraction nonconforming).** For a normally distributed quality characteristic with mean $\mu$ and standard deviation $\sigma$, the expected fraction outside the specification limits is
> 
> $$
> p = \Phi\left(\frac{L-\mu}{\sigma}\right) + 1 - \Phi\left(\frac{U-\mu}{\sigma}\right).
> $$

> **Corollary (Centred process).** If the process is centred so that $\mu = (L+U)/2$, then
> 
> $$
> p = 2\left(1 - \Phi\left(3C_p\right)\right).
> $$

The corollary is the reason capability ratios are quoted at all: a single number converts into an expected defect rate through the normal tail. A capability of 1.33 corresponds to $3C_p = 4$ and a defect rate of about 63 parts per million.

### 2.8 Tolerance-interval logic

> **Definition (Statistical tolerance interval).** A tolerance interval with content $p$ and confidence $\gamma$ is an interval computed from a sample that contains at least a proportion $p$ of the population with probability $\gamma$.

The logic differs from that of a confidence interval in the object being covered. A confidence interval covers a parameter; a tolerance interval covers individual items. Consequently a tolerance interval is always wider than the corresponding confidence interval for the mean, because individual items scatter about the mean.

For a normal population, an interval of the form $\bar{x} \pm k s$ covers a proportion $2\Phi(k)-1$ of the population when the mean and standard deviation are known. Substituting estimates introduces sampling error, so the multiplier $k$ used in practice exceeds the normal quantile and decreases towards it as the sample grows. For 95 per cent content the limiting multiplier is 1.96, and for 99 per cent content it is 2.576. The practical statement is that a tolerance interval must be justified by the sample it came from, which is why the confidence level is part of its definition.

### 2.9 Likert composites and index construction

> **Theorem (Variance of a sum of items).** For items $X_1, \dots, X_m$ forming a composite $C = \sum X_j$,
> 
> $$
> \text{Var}(C) = \sum_{j=1}^{m}\text{Var}\left(X_j\right) + 2\sum_{j<l}\text{Cov}\left(X_j, X_l\right).
> $$

The covariance terms are the point of a composite. Items that measure the same construct covary positively, so the composite variance is dominated by the shared signal while independent response noise partly cancels, and the reliability of the composite rises with the number of items and with their average intercorrelation.

> **Definition (Min-max normalisation).** An indicator $x$ with observed minimum $x_{\min}$ and maximum $x_{\max}$ is rescaled to
> 
> $$
> I = \frac{x - x_{\min}}{x_{\max} - x_{\min}} .
> $$

> **Definition (Geometric aggregation).** A composite index of normalised indicators $I_1, \dots, I_m$ may be formed as the geometric mean
> 
> $$
> G = \left(\prod_{j=1}^{m} I_j\right)^{1/m} .
> $$

The geometric mean penalises imbalance: a country that is strong on two dimensions and weak on the third scores lower than its arithmetic mean suggests, which is the intended behaviour of a human-development style index.

### 2.10 Table of applied quantities, estimators and standard errors

| Field | Quantity | Estimator | Standard error or spread |
|---|---|---|---|
| Economics | Cost of a fixed basket | Laspeyres index | Sampling error of component prices |
| Business | Defect rate | $\hat{p} = D/n$ | $\sqrt{\hat{p}(1-\hat{p})/n}$ |
| Business | Mean sales | $\bar{y}$ | $s/\sqrt{n}$ |
| Medicine | Sensitivity | $a/(a+c)$ | $\sqrt{\text{sens}(1-\text{sens})/(a+c)}$ |
| Medicine | Risk difference | $r_1 - r_0$ | $\sqrt{r_1(1-r_1)/n_1 + r_0(1-r_0)/n_0}$ |
| Social science | Support proportion | $\hat{p}$ | $\sqrt{\hat{p}(1-\hat{p})/n}\times\sqrt{\text{deff}}$ |
| Social science | Mean Likert score | $\bar{x}$ | $s/\sqrt{n}$ |
| Engineering | Subgroup mean | $\bar{x}$ | $\sigma/\sqrt{n}$ |
| Engineering | Failure rate | $d/T$ | $\sqrt{d}/T$ for a Poisson count |

The table is worth memorising as a single structure: every standard error in applied statistics is a spread divided by the square root of an amount of information.

## 3. Formal Proofs, Derivations, and Methods

### 3.1 Derivation of Bayes for predictive value

Let $D$ be the event that the disease is present and $T^{+}$ the event of a positive test. By the definition of conditional probability,

$$
P\left(D \mid T^{+}\right) = \frac{P\left(D \cap T^{+}\right)}{P\left(T^{+}\right)} .
$$

The numerator is rewritten by applying the multiplication rule in the other order,

$$
P\left(D \cap T^{+}\right) = P\left(T^{+} \mid D\right)P(D) .
$$

The denominator is expanded by the law of total probability over the partition $\{D, D'\}$,

$$
P\left(T^{+}\right) = P\left(T^{+} \mid D\right)P(D) + P\left(T^{+} \mid D'\right)P(D') .
$$

Substituting both pieces gives the stated form. Writing sensitivity for $P(T^{+}\mid D)$, specificity for $P(T^{-}\mid D')$ so that $P(T^{+}\mid D') = 1-\text{specificity}$, and prevalence for $P(D)$,

$$
\text{PPV} = \frac{\text{sens}\times\text{prev}}{\text{sens}\times\text{prev} + (1-\text{spec})(1-\text{prev})} .
$$

Differentiating the right side with respect to prevalence shows that it is increasing whenever both sens and spec exceed one half, which establishes the monotonicity property.

### 3.2 Derivation of the Laspeyres-Paasche ordering

Write the Laspeyres index as a base-expenditure-weighted average of price relatives,

$$
I_L = \frac{\sum_{i} p_{1i}q_{0i}}{\sum_{i} p_{0i}q_{0i}} = \sum_{i} w_{0i}\frac{p_{1i}}{p_{0i}}, \qquad w_{0i} = \frac{p_{0i}q_{0i}}{\sum_{j} p_{0j}q_{0j}} .
$$

Write the Paasche index in the same way, using current expenditure weights,

$$
I_P = \frac{\sum_{i} p_{1i}q_{1i}}{\sum_{i} p_{0i}q_{1i}} = \sum_{i} w_{1i}\frac{p_{1i}}{p_{0i}}, \qquad w_{1i} = \frac{p_{0i}q_{1i}}{\sum_{j} p_{0j}q_{1j}} .
$$

Both indexes are weighted means of the same set of relatives, so their difference is governed by how the weights shift between the two weight vectors. If the quantity of an item falls when its relative price rises, the current-expenditure weights move towards items whose relatives are low, and the weighted mean falls. With $r_i = p_{1i}/p_{0i}$ and weights normalised to sum to one, the difference is a weighted covariance between the relative and the change in weight,

$$
I_P - I_L = \sum_{i}\left(w_{1i} - w_{0i}\right)r_i ,
$$

and this sum is negative under the stated substitution assumption, because the items whose weight rose are those whose relative price fell. The inequality is therefore a statement about household behaviour rather than about arithmetic.

### 3.3 Derivation of three-sigma limits from the standard error

Suppose the quality characteristic of individual items is distributed with mean $\mu$ and standard deviation $\sigma$, and successive subgroups of $n$ items are drawn independently. The subgroup mean $\bar{X}$ has mean $\mu$ and variance $\sigma^{2}/n$ by the properties of the sum of independent variables. Hence the standard deviation of the plotted statistic is

$$
\sigma_{\bar{X}} = \frac{\sigma}{\sqrt{n}} .
$$

Setting the limits at three standard errors either side of the centre line gives

$$
\text{UCL} = \mu + 3\frac{\sigma}{\sqrt{n}}, \qquad \text{LCL} = \mu - 3\frac{\sigma}{\sqrt{n}} .
$$

Under approximate normality, the probability that one plotted point lies outside a limit is

$$
P\left(\left|Z\right| > 3\right) = 2\left(1 - \Phi(3)\right) = 0.0027 ,
$$

and because successive points are independent under a stable process, the number of points until a false alarm is geometric with mean $1/0.0027 = 370.4$. This is the derivation that converts the arbitrary-looking constant three into a statement about the frequency of nuisance alarms.

In practice $\mu$ and $\sigma$ are replaced by estimates from a baseline period, and control charts then use constants tabulated for the sample range or sample standard deviation. The structure of the limits, however, never changes: a centre line plus and minus three estimated standard errors.

### 3.4 Tolerance-interval logic and the coverage of a k-sigma interval

Consider an interval centred on the process mean with half-width $k\sigma$. If the characteristic is normally distributed, the proportion covered is

$$
P\left(\left|X-\mu\right| \le k\sigma\right) = 2\Phi(k) - 1 .
$$

Substituting $k=1$ gives 0.6827, $k=2$ gives 0.9545, and $k=3$ gives 0.9973. A manufacturer who wants to claim that 95 per cent of items fall inside a stated band must therefore set the band at about two standard deviations either side of the mean, and a manufacturer who wants 99 per cent must set it at about 2.576 standard deviations.

The statistical subtlety appears when $\mu$ and $\sigma$ are unknown. Replacing them by $\bar{x}$ and $s$ computed from $n$ items introduces sampling error, so the interval $\bar{x} \pm ks$ with $k$ equal to the normal quantile covers the nominal proportion only on average over repeated samples, and in a particular sample it may cover less. A tolerance interval multiplies by a larger factor, chosen so that the stated proportion is covered with the stated confidence. As $n$ grows the required factor decreases towards the normal quantile, and as $n$ becomes small the factor grows sharply. The design consequence is that a tolerance claim cannot be made from a handful of items.

### 3.5 Derivation of the interval for a survey proportion and the sample-size formula

By the central limit theorem, for large $n$,

$$
\frac{\hat{p} - p}{\sqrt{p(1-p)/n}} \sim N(0,1) .
$$

Replacing the unknown $p$ in the denominator by $\hat{p}$ gives the estimated standard error, and the interval with confidence $1-\alpha$ is

$$
\hat{p} \pm z_{1-\alpha/2}\sqrt{\frac{\hat{p}(1-\hat{p})}{n}} .
$$

To choose $n$ in advance, set the desired margin of error $E$ equal to the half-width and solve:

$$
E = z_{1-\alpha/2}\sqrt{\frac{p(1-p)}{n}} \quad \text{implies} \quad n = \frac{z^{2}_{1-\alpha/2}\,p(1-p)}{E^{2}} .
$$

Because $p$ is unknown at the design stage, the conservative choice $p = 0.5$ is used when no prior estimate exists, since $p(1-p)$ is maximised there.

### 3.6 Derivation of the expected defect rate from a capability ratio

For a centred process, the distance from the mean to each specification limit is

$$
\frac{U-L}{2} = 3C_p\sigma .
$$

Dividing by $\sigma$ gives the number of standard deviations separating the mean from the limit, namely $3C_p$. The fraction outside the limits is therefore

$$
p = 2\left(1 - \Phi\left(3C_p\right)\right).
$$

For $C_p = 1$ this gives 0.0027, or 2700 parts per million; for $C_p = 1.33$ it gives $2\Phi(-4) = 63$ parts per million; for $C_p = 0.833$ it gives $2\Phi(-2.5) = 0.0124$, that is 12 420 parts per million. The conversion is monotone and steep, which is why a small improvement in capability produces a large reduction in scrap.

### 3.7 Derivation of the exponential reliability function

Let $R(t)$ be the probability of surviving beyond $t$ and suppose the hazard $\lambda$ is constant. Over a short interval of length $\Delta t$, the probability of failing is approximately $\lambda\Delta t$, so

$$
R(t+\Delta t) \approx R(t)\left(1 - \lambda\Delta t\right) .
$$

Rearranging and letting $\Delta t$ tend to zero gives the differential equation

$$
\frac{dR}{dt} = -\lambda R(t),
$$

whose solution with $R(0)=1$ is $R(t) = e^{-\lambda t}$. The mean lifetime follows by integration,

$$
\text{MTTF} = \int_{0}^{\infty}R(t)\,dt = \int_{0}^{\infty}e^{-\lambda t}dt = \frac{1}{\lambda} .
$$

The memoryless property is a consequence, not an additional assumption: for $s, t > 0$,

$$
P\left(T > s+t \mid T > s\right) = \frac{e^{-\lambda(s+t)}}{e^{-\lambda s}} = e^{-\lambda t} .
$$

### 3.8 Method: analysis of a two-group trial

Step 1. Tabulate events and totals for each arm and compute each arm's risk.

Step 2. Compute the relative risk as the ratio of risks and the absolute risk reduction as their difference. Report both, because they answer different questions.

Step 3. Compute the number needed to treat as the reciprocal of the absolute risk reduction, and round up, because a fraction of a patient is meaningless.

Step 4. Compute the odds ratio and note that it approximates the relative risk only when the outcome is rare.

Step 5. Attach intervals. For the relative risk, work on the log scale with standard error $\sqrt{1/a - 1/n_1 + 1/c - 1/n_0}$, where $a$ and $c$ are the event counts, and exponentiate the limits.

Step 6. Interpret in absolute terms, since the decision to adopt a treatment depends on how many patients must be treated to prevent one event.

### 3.9 Method: analysis of a designed experiment with two levels of one factor

Step 1. State the factor, its levels, the response, and the number of replicates fixed in advance.

Step 2. Compute the group means and the group variances.

Step 3. Pool the variances, weighting each by its degrees of freedom, to obtain the pooled variance.

Step 4. Compute the standard error of the difference in means as the pooled standard deviation times the square root of the sum of the reciprocals of the group sizes.

Step 5. Form the test statistic as the difference divided by its standard error, and compare with the appropriate critical value on the pooled degrees of freedom.

Step 6. Report the difference with its interval, and state whether the difference is large enough to matter in the units of the problem.

### 3.10 Method: calibration and inverse prediction

Step 1. Prepare standards of known value and record the instrument response for each, in random order to avoid drift effects.

Step 2. Fit the least squares line of response on true value, and check that the residuals show no curvature.

Step 3. Use the fitted line to predict the response for a new standard as a check on the instrument.

Step 4. Invert the line to infer a true value from a new reading, and state that the inverse estimate carries wider uncertainty than the forward prediction.

Step 5. Report the calibration range, and refuse to extrapolate outside it, because the linear relationship is established only within the range of the standards.

## 4. Representative Worked Examples and Solutions

### 4.1 Problem: three price indexes for one basket

A household budget covers four items. The base-period prices and quantities, and the current-period prices and quantities, are as follows.

| Item | Base price | Base quantity | Current price | Current quantity |
|---|---|---|---|---|
| Bread | 40 | 100 | 50 | 120 |
| Milk | 30 | 200 | 36 | 210 |
| Sugar | 80 | 50 | 100 | 45 |
| Cooking oil | 150 | 20 | 180 | 25 |

Compute the Laspeyres, Paasche and Fisher price indexes, and interpret the difference between the first two.

### 4.2 Solution: four expenditure sums, then three ratios

Step 1. Compute base-period expenditure at base prices and quantities:

$$
\sum p_{0}q_{0} = 4000 + 6000 + 4000 + 3000 = 17000 .
$$

Step 2. Compute current-period prices at base quantities:

$$
\sum p_{1}q_{0} = 5000 + 7200 + 5000 + 3600 = 20800 .
$$

Step 3. Form the Laspeyres index:

$$
I_L = \frac{20800}{17000}\times 100 = 122.35 .
$$

Step 4. Compute base prices at current quantities:

$$
\sum p_{0}q_{1} = 4800 + 6300 + 3600 + 3750 = 18450 .
$$

Step 5. Compute current prices at current quantities:

$$
\sum p_{1}q_{1} = 6000 + 7560 + 4500 + 4500 = 22560 .
$$

Step 6. Form the Paasche index:

$$
I_P = \frac{22560}{18450}\times 100 = 122.28 .
$$

Step 7. Form the Fisher index as the geometric mean:

$$
I_F = \sqrt{1.22353 \times 1.22276}\times 100 = 122.31 .
$$

Step 8. Interpret. The Paasche index is slightly lower than the Laspeyres index because the household reduced its purchases of sugar and increased its purchases of bread, whose relative price rose least. The gap of 0.07 index points is small here because the substitution was small; in a long run of high inflation the gap becomes substantial.

Step 9. Convert to a statement about living standards. If nominal income rose by 12 per cent, the real income index is

$$
\frac{112}{122.35}\times 100 = 91.54 ,
$$

so real income fell by about 8.5 per cent. A report that mentioned only the 12 per cent nominal rise would reverse the meaning of the data.

### 4.3 Problem: estimating demand and its elasticity

A retailer records the price of an item in shillings and the quantity sold in hundreds of units over four periods.

| Price | 10 | 20 | 30 | 40 |
|---|---|---|---|---|
| Quantity | 90 | 74 | 58 | 42 |

Fit a linear demand function and compute the point elasticity at a price of 30.

### 4.4 Solution: regress quantity on price, then scale the slope

Step 1. Compute the means:

$$
\bar{p} = 25, \qquad \bar{Q} = 66 .
$$

Step 2. Compute the corrected sums:

$$
S_{pp} = 3000 - \frac{100^{2}}{4} = 500, \qquad S_{pQ} = 5800 - \frac{100 \times 264}{4} = -800 .
$$

Step 3. Compute the slope:

$$
b = \frac{-800}{500} = -1.6 .
$$

Step 4. Compute the intercept:

$$
a = 66 - (-1.6)(25) = 106 .
$$

Step 5. State the fitted demand function and check it against one observation:

$$
Q = 106 - 1.6p, \qquad \text{at } p = 30, \quad Q = 106 - 48 = 58 ,
$$

which reproduces the observed value exactly, as it must for a perfect linear fit.

Step 6. Compute the point elasticity at a price of 30:

$$
\varepsilon = \frac{p}{Q}\cdot b = \frac{30}{58}(-1.6) = -0.83 .
$$

Step 7. Interpret. Demand is inelastic at that price, since the elasticity lies between zero and minus one in absolute value: a one per cent rise in price reduces quantity by about 0.83 per cent, so revenue rises. The retailer's pricing decision follows from the sign and size of the elasticity, not from the fitted line alone.

### 4.5 Problem: a control chart for a defect rate

A factory inspects 200 items each day. Over 20 days of stable production the total number of defectives was 640. Set up a control chart for the daily fraction nonconforming, and judge a day on which 16 items were defective.

### 4.6 Solution: centre line, standard error, three of them

Step 1. Estimate the process fraction nonconforming:

$$
\bar{p} = \frac{640}{20 \times 200} = \frac{640}{4000} = 0.032 .
$$

Step 2. Compute the standard error of a daily fraction based on 200 items:

$$
\sigma_{\hat{p}} = \sqrt{\frac{0.032 \times 0.968}{200}} = \sqrt{0.00015488} = 0.01245 .
$$

Step 3. Form the limits:

$$
\text{UCL} = 0.032 + 3(0.01245) = 0.0694, \qquad \text{LCL} = 0.032 - 3(0.01245) < 0 .
$$

Step 4. Truncate the lower limit at zero, because a negative fraction is impossible.

Step 5. Convert the day in question to a fraction and compare:

$$
\hat{p}_{\text{day}} = \frac{16}{200} = 0.08 > 0.0694 .
$$

Step 6. Interpret. The day lies above the upper control limit, so the process was not stable on that day. The correct action is to investigate the cause, not to widen the limits, because the limits describe what the process does when nothing has changed.

Step 7. Note the false-alarm rate. With three-sigma limits the expected number of days between false alarms is about 370, so an isolated signal on one day out of twenty is unlikely to be chance.

### 4.7 Problem: a diagnostic test in two populations

A test has sensitivity 0.90 and specificity 0.92. Compute the predictive value of a positive result in a clinic where prevalence is 0.10, and in a screening programme where prevalence is 0.01.

### 4.8 Solution: the same test, two base rates

Step 1. Build the clinic table for 1000 people, of whom 100 have the disease. Of the diseased, $0.90 \times 100 = 90$ test positive. Of the 900 healthy, $0.08 \times 900 = 72$ test positive. Of the healthy, $0.92 \times 900 = 828$ test negative, and of the diseased, 10 test negative.

| | Disease present | Disease absent | Total |
|---|---|---|---|
| Test positive | 90 | 72 | 162 |
| Test negative | 10 | 828 | 838 |
| Total | 100 | 900 | 1000 |

Step 2. Read the predictive value of a positive result across the first row:

$$
\frac{90}{162} = 0.5556 .
$$

Step 3. Read the predictive value of a negative result across the second row:

$$
\frac{828}{838} = 0.9881 .
$$

Step 4. Repeat for the screening population by Bayes, with prevalence 0.01:

$$
P\left(D \mid T^{+}\right) = \frac{0.90 \times 0.01}{0.90 \times 0.01 + 0.08 \times 0.99} = \frac{0.009}{0.009 + 0.0792} = 0.1020 .
$$

Step 5. Compare. The same test, with the same sensitivity and specificity, gives a positive result that is correct 55.6 per cent of the time in the clinic and only 10.2 per cent of the time in the screening programme. The test has not changed; the base rate has.

Step 6. Compute the likelihood ratio as a compact summary:

$$
\text{LR}^{+} = \frac{0.90}{1 - 0.92} = 11.25 ,
$$

so a positive result multiplies the prior odds of disease by about eleven. In the screening population the prior odds are about 1 to 99, and eleven times those odds are still odds of about 1 to 9.

### 4.9 Problem: reporting a clinical trial

In a randomised trial with 100 patients per arm, 15 patients on the new treatment and 30 on the control experienced the event. Compute the risks, the relative risk, the absolute risk reduction, the number needed to treat, and the odds ratio.

### 4.10 Solution: two ratios, one difference, one reciprocal

Step 1. Compute the risks:

$$
r_1 = \frac{15}{100} = 0.15, \qquad r_0 = \frac{30}{100} = 0.30 .
$$

Step 2. Compute the relative risk:

$$
\text{RR} = \frac{0.15}{0.30} = 0.50 .
$$

Step 3. Compute the absolute risk reduction:

$$
\text{ARR} = 0.30 - 0.15 = 0.15 .
$$

Step 4. Compute the number needed to treat:

$$
\text{NNT} = \frac{1}{0.15} = 6.67, \quad \text{so } 7 \text{ patients} .
$$

Step 5. Compute the odds ratio:

$$
\text{OR} = \frac{0.15/0.85}{0.30/0.70} = \frac{0.1765}{0.4286} = 0.412 .
$$

Step 6. Attach an interval to the relative risk on the log scale:

$$
\text{SE}\left(\ln \text{RR}\right) = \sqrt{\frac{1}{15} - \frac{1}{100} + \frac{1}{30} - \frac{1}{100}} = 0.2828 ,
$$

$$
\exp\left(-0.6931 \pm 1.96(0.2828)\right) \quad \text{gives} \quad 0.287 \text{ to } 0.870 .
$$

Step 7. Interpret all four numbers together. Halving the risk sounds decisive, and it is real, because the interval for the relative risk excludes one. But the decision to adopt the treatment depends on the absolute reduction of 15 percentage points, which means seven patients treated to prevent one event. The odds ratio of 0.41 overstates the relative risk of 0.50 because the outcome is common, and reporting the odds ratio alone in this setting would exaggerate the effect.

### 4.11 Problem: a survey proportion with a design requirement

A random sample of 400 households finds that 248 support a proposed levy. Estimate the population proportion with a 95 per cent interval, and determine the sample size needed for a margin of three percentage points.

### 4.12 Solution: estimate, interval, then solve for the sample size

Step 1. Compute the sample proportion:

$$
\hat{p} = \frac{248}{400} = 0.62 .
$$

Step 2. Compute the standard error:

$$
\text{SE} = \sqrt{\frac{0.62 \times 0.38}{400}} = \sqrt{0.000589} = 0.02427 .
$$

Step 3. Form the interval:

$$
0.62 \pm 1.96(0.02427) \quad \text{gives} \quad 0.5724 \text{ to } 0.6676 .
$$

Step 4. State the result in percentage points: between 57.2 and 66.8 per cent, a margin of 4.8 points either way.

Step 5. Solve for the sample size at a margin of three points, using the estimate as a planning value:

$$
n = \frac{(1.96)^{2}(0.62)(0.38)}{(0.03)^{2}} = \frac{0.9051}{0.0009} = 1005.6, \quad \text{so } 1006 .
$$

Step 6. Compare with the conservative choice that assumes no prior knowledge:

$$
n = \frac{(1.96)^{2}(0.25)}{(0.03)^{2}} = 1067.1, \quad \text{so } 1068 .
$$

Step 7. Interpret. Quadrupling the sample from 400 to 1600 would halve the margin to about 2.4 points, because the margin is inversely proportional to the square root of the sample size. Any claim that a larger sample gives a "much more accurate" result must be quantified in this way, since doubling the sample only reduces the margin by about thirty per cent.

### 4.13 Problem: summarising a Likert scale

Two hundred respondents rate a service on a five-point scale, coded 1 to 5, with the following frequencies.

| Score | 1 | 2 | 3 | 4 | 5 |
|---|---|---|---|---|---|
| Frequency | 20 | 40 | 60 | 50 | 30 |

Compute the mean score, the standard deviation, and a 95 per cent interval for the mean score.

### 4.14 Solution: weighted mean, weighted variance, standard error

Step 1. Compute the total frequency and the weighted sum:

$$
n = 200, \qquad \sum f x = 20 + 80 + 180 + 200 + 150 = 630 .
$$

Step 2. Compute the mean score:

$$
\bar{x} = \frac{630}{200} = 3.15 .
$$

Step 3. Compute the weighted sum of squares and the variance:

$$
\sum f x^{2} = 20 + 160 + 540 + 800 + 750 = 2270 ,
$$

$$
s^{2} = \frac{2270}{200} - (3.15)^{2} = 11.35 - 9.9225 = 1.4275 .
$$

Step 4. Compute the standard deviation:

$$
s = \sqrt{1.4275} = 1.195 .
$$

Step 5. Compute the standard error and the interval:

$$
\text{SE} = \frac{1.195}{\sqrt{200}} = 0.0845, \qquad 3.15 \pm 1.96(0.0845) \quad \text{gives} \quad 2.98 \text{ to } 3.32 .
$$

Step 6. Interpret with the measurement caveat. The average code is 3.15, between "neutral" and "agree", and the interval excludes 3.0, so the average is credibly above the neutral point. The interval is narrow because the sample is large, and the conclusion that the service is rated slightly above neutral does not depend on the equal-spacing assumption, whereas any claim about how much above neutral does.

### 4.15 Problem: constructing a composite index

Three indicators are normalised to the range zero to one, giving values 0.7154, 0.62 and 0.55. Aggregate them by a geometric mean and by an arithmetic mean, and comment.

### 4.16 Solution: two aggregations of the same three numbers

Step 1. Multiply the three normalised values:

$$
0.7154 \times 0.62 \times 0.55 = 0.24395 .
$$

Step 2. Take the cube root:

$$
G = (0.24395)^{1/3} = 0.6248 .
$$

Step 3. Compute the arithmetic mean for comparison:

$$
A = \frac{0.7154 + 0.62 + 0.55}{3} = 0.6285 .
$$

Step 4. Interpret the difference. The geometric mean is lower, and the gap is largest exactly when the indicators are most unequal, which is the property the index is designed to have. A country cannot compensate a very weak dimension with strength elsewhere.

Step 5. Note the normalisation choice. Changing the minimum or maximum of any indicator changes its normalised value and therefore the index, so the index is a construction rather than a measurement, and its construction must be reported.

### 4.17 Problem: capability and expected scrap

A process produces shafts with mean diameter 50.00 millimetres and standard deviation 0.20 millimetres. The specification is 49.50 to 50.50. Compute the capability ratios and the expected fraction nonconforming.

### 4.18 Solution: ratios first, then the normal tail

Step 1. Compute the allowed width and the natural width:

$$
U - L = 1.00, \qquad 6\sigma = 1.20 .
$$

Step 2. Compute the capability ratio:

$$
C_p = \frac{1.00}{1.20} = 0.833 .
$$

Step 3. Compute the centred capability ratio, which here equals the first because the process is centred:

$$
C_{pk} = \min\left(\frac{0.50}{0.60}, \frac{0.50}{0.60}\right) = 0.833 .
$$

Step 4. Compute the distance from the mean to a limit in standard deviations:

$$
z = \frac{0.50}{0.20} = 2.5 .
$$

Step 5. Convert to a defect rate:

$$
p = 2\left(1 - \Phi(2.5)\right) = 0.0124,
$$

that is 1.24 per cent, or 12 420 parts per million.

Step 6. Interpret and decide. The process is centred, so the whole problem is variation. Reducing the standard deviation to 0.15 would raise the capability to 1.11 and reduce the defect rate to about 0.09 per cent; reducing it to 0.125 would raise the capability to 1.33 and reduce the defect rate to about 63 parts per million. Centring the process cannot help, because it is already centred.

### 4.19 Problem: reliability of a component

A component has a constant failure rate of 0.0002 per hour. Compute the mean time to failure, the probability of surviving 1000 hours, and the probability of surviving 2000 hours.

### 4.20 Solution: reciprocate the hazard, then exponentiate

Step 1. Compute the mean time to failure:

$$
\text{MTTF} = \frac{1}{0.0002} = 5000 \text{ hours} .
$$

Step 2. Compute the survival probability at 1000 hours:

$$
R(1000) = e^{-0.0002 \times 1000} = e^{-0.2} = 0.8187 .
$$

Step 3. Compute the survival probability at 2000 hours:

$$
R(2000) = e^{-0.4} = 0.6703 .
$$

Step 4. Interpret. About 18 per cent of components fail within their mean lifetime, which is a consequence of the skewness of the exponential distribution and a frequent source of confusion: the mean is not the age by which most items have failed. The probability of surviving a further 1000 hours given survival to 1000 hours is $0.6703/0.8187 = 0.819$, the same as the probability of surviving the first 1000 hours, which is the memoryless property.

### 4.21 Problem: a designed comparison of two cutting speeds

Five tools are run at each of two speeds. Tool life in hours is as follows.

| Speed | Tool lives |
|---|---|
| A | 24, 26, 25, 23, 27 |
| B | 30, 32, 29, 31, 33 |

Test whether the speeds differ, and state the result in the units of the problem.

### 4.22 Solution: means, pooled variance, standard error, test statistic

Step 1. Compute the means:

$$
\bar{x}_A = 25, \qquad \bar{x}_B = 31 .
$$

Step 2. Compute the group sums of squares and variances:

$$
\sum\left(x - \bar{x}_A\right)^{2} = 10, \qquad \sum\left(x - \bar{x}_B\right)^{2} = 10,
$$

$$
s^{2}_{A} = s^{2}_{B} = \frac{10}{4} = 2.5 .
$$

Step 3. Pool the variances, which coincide here:

$$
s^{2}_{p} = \frac{10 + 10}{8} = 2.5, \qquad s_p = 1.581 .
$$

Step 4. Compute the standard error of the difference:

$$
\text{SE} = s_p\sqrt{\frac{1}{5} + \frac{1}{5}} = 1.581\sqrt{0.4} = 1.00 .
$$

Step 5. Compute the test statistic:

$$
t = \frac{31 - 25}{1.00} = 6.0 \quad \text{on } 8 \text{ degrees of freedom} .
$$

Step 6. Compare with the critical value of 2.306 at the 5 per cent level, and conclude that the difference is real.

Step 7. Interpret in units. The difference is 6 hours of tool life, and a 95 per cent interval is $6 \pm 2.306(1.00)$, that is 3.7 to 8.3 hours. Whether six additional hours justifies the higher speed depends on the cost of tool changes, which is an engineering judgement and not a statistical one.

### 4.23 Problem: calibrating an instrument

Five standards of known value give the following readings.

| True value | 10 | 20 | 30 | 40 | 50 |
|---|---|---|---|---|---|
| Reading | 21 | 40 | 62 | 79 | 101 |

Fit the calibration line and estimate the true value corresponding to a reading of 79.

### 4.24 Solution: fit the line, then invert it

Step 1. Compute the means and the corrected sums:

$$
\bar{x} = 30, \qquad \bar{y} = 60.6, \qquad S_{xx} = 1000, \qquad S_{xy} = 1990 .
$$

Step 2. Compute the slope and intercept:

$$
b = \frac{1990}{1000} = 1.99, \qquad a = 60.6 - 1.99(30) = 0.90 .
$$

Step 3. State the fitted line:

$$
\hat{y} = 0.90 + 1.99x .
$$

Step 4. Invert the line for a reading of 79:

$$
x = \frac{79 - 0.90}{1.99} = \frac{78.10}{1.99} = 39.25 .
$$

Step 5. Sanity-check the answer. The reading of 79 was observed at a true value of 40, and the fitted line returns 39.25, a small shrinkage towards the mean that is characteristic of least squares fitting.

Step 6. State the limits. The line is valid only between true values of 10 and 50. Using it to convert a reading of 150 would be an extrapolation with no supporting standards, and the uncertainty of the inverse estimate is wider than that of the forward prediction, because the error in the slope is amplified when the line is inverted.

### 4.25 Problem: survival after diagnosis

Ten patients are followed after diagnosis. Deaths occur at 3, 5, 5 and 8 months, and one patient is lost to follow-up at 6 months; the remaining five are still alive at the end of the study. Estimate the survival function, and compute the mortality rate if a larger register records 45 deaths over 1200 person-years of follow-up.

### 4.26 Solution: risk sets, factors, cumulative product

Step 1. List the distinct failure times in order and count the failures at each: $t = 3$ with $d = 1$, $t = 5$ with $d = 2$, $t = 8$ with $d = 1$.

Step 2. Determine the number at risk just before each failure time. At $t = 3$ all ten are at risk. At $t = 5$, one has died, so nine are at risk. At $t = 8$, one has died and two have died, and one has been censored at 6 months, so six remain at risk.

Step 3. Compute the conditional survival factors:

$$
1 - \frac{1}{10} = 0.90, \qquad 1 - \frac{2}{9} = 0.7778, \qquad 1 - \frac{1}{6} = 0.8333 .
$$

Step 4. Multiply cumulatively:

$$
\hat{S}(3) = 0.90, \qquad \hat{S}(5) = 0.90(0.7778) = 0.70, \qquad \hat{S}(8) = 0.70(0.8333) = 0.5833 .
$$

Step 5. Interpret. About 70 per cent of patients survive beyond five months and about 58 per cent beyond eight months. The patient censored at six months contributes to the risk sets at three and five months and then leaves, which is why the denominator at eight months is six rather than seven; discarding that patient would waste information, and counting them as a survivor to eight months would overstate survival.

Step 6. Compute the mortality rate for the register:

$$
\frac{45}{1200}\times 1000 = 37.5 \text{ deaths per 1000 person-years} .
$$

Step 7. Interpret with the standard caveat. The rate is an average over the whole follow-up period and is not comparable between populations of different age structure without standardisation, because a population with more elderly people will show a higher crude rate whatever the underlying risk.

### 4.27 Problem: inventory and a sales forecast

Weekly demand for an item is approximately normal with mean 500 units and standard deviation 60 units, and the replenishment lead time is four weeks. Compute the safety stock and the reorder point for a 95 per cent service level, and state the effect of raising the service level to 99 per cent.

### 4.28 Solution: a normal quantile applied to lead-time demand

Step 1. Compute the standard deviation of demand over the lead time, assuming independence between weeks:

$$
\sigma_{L} = \sigma\sqrt{L} = 60\sqrt{4} = 120 \text{ units} .
$$

Step 2. Read the normal quantile for the service level: $z = 1.645$ for 95 per cent and $z = 2.326$ for 99 per cent.

Step 3. Compute the safety stock at 95 per cent:

$$
\text{SS} = z\sigma_{L} = 1.645(120) = 197.4, \quad \text{so about } 198 \text{ units} .
$$

Step 4. Compute the reorder point as expected lead-time demand plus safety stock:

$$
500(4) + 197.4 = 2197.4, \quad \text{so about } 2197 \text{ units} .
$$

Step 5. Repeat at 99 per cent:

$$
\text{SS} = 2.326(120) = 279.1, \quad \text{so about } 279 \text{ units} ,
$$

which is 81 units more than at 95 per cent.

Step 6. Interpret. The safety stock is not a forecast; it is the buffer that covers the upper tail of forecast error, and it grows with the square root of the lead time and linearly with the service-level multiplier. Raising the service level from 95 to 99 per cent cuts the expected number of stock-out cycles by a factor of five while raising the holding cost by about 41 per cent, and the trade-off is a management decision informed by the two numbers rather than by the statistics alone.

## 5. Mathematical Extensions, Limits, and Common Errors

### 5.1 Confounding and the reversal of a comparison

Confounding occurs when a third variable is associated with both the exposure and the outcome, so that the observed association measures the confounder as much as the exposure. The effect can be large enough to reverse the direction of a comparison, and the reversal has a name.

Suppose a hospital reports survival under two treatments, split by severity.

| Severity | Treatment A survivors | Treatment A total | Treatment B survivors | Treatment B total |
|---|---|---|---|---|
| Mild | 400 | 500 | 9 | 10 |
| Severe | 10 | 100 | 90 | 200 |
| All | 410 | 600 | 99 | 210 |

Within the mild stratum, A survives 80 per cent and B survives 90 per cent, so B is better. Within the severe stratum, A survives 10 per cent and B survives 45 per cent, so B is better again. Overall, A survives $410/600 = 68.3$ per cent while B survives $99/210 = 47.1$ per cent, so the pooled comparison reverses the conclusion and appears to show A as the superior treatment.

The mechanism is the case mix. A treated 500 mild and 100 severe patients, so four fifths of its patients were in the stratum with the high survival rate. B treated 10 mild and 200 severe patients, so nineteen twentieths of its patients were in the stratum where survival is low for everyone. The pooled comparison therefore measures the allocation policy as much as the treatment, and a hospital that reported only the bottom row would be reporting its own admission rules.

The remedies are randomisation, which balances the case mix in expectation, stratification, which compares within strata, or adjustment by a model, and each of them requires the confounder to have been measured.

### 5.2 Selection bias and non-response

Selection bias arises when the units observed are not a fair sample of the units of interest, and it is not repaired by sample size. A response rate of 30 per cent in a household income survey means that 70 per cent of the population is represented only through the assumption that non-responders resemble responders, and that assumption is usually false in the direction that matters: income non-response is highest at both extremes.

The formal statement is that the estimate converges to the mean of the responding subpopulation, not to the mean of the population. In symbols, if $R$ indicates response,

$$
E\left(\bar{x}\right) = E\left(X \mid R = 1\right) \ne E(X) .
$$

The practical remedies are a sampling frame that covers the population, weighting by known population totals, and follow-up of non-responders to estimate the size of the difference.

### 5.3 Multiplicity and p-hacking

Every hypothesis test carries a probability of a false positive equal to the significance level when the null hypothesis is true. Testing many hypotheses therefore produces apparent discoveries by construction. If twenty independent null hypotheses are tested at the 5 per cent level with nothing really happening, the probability of at least one significant result is

$$
1 - 0.95^{20} = 0.6415 ,
$$

and for fifteen tests it is $1 - 0.95^{15} = 0.5367$. Neither number depends on the subject matter, the quality of the data, or the skill of the analyst.

Three practices turn this arithmetic into a published falsehood. Testing many outcomes and reporting the significant one is selective reporting. Adding observations until significance is reached is optional stopping, which invalidates the nominal level. Choosing the analysis after inspecting the data is specification searching. The defences are pre-registration of the primary outcome and analysis, reporting of every outcome measured, and a multiplicity adjustment such as the Bonferroni rule, which compares each $p$-value with $\alpha/m$ for $m$ tests, or 0.0025 when twenty tests are performed at the 5 per cent level.

### 5.4 Statistical significance and practical significance

A test answers whether an effect could plausibly be zero. It does not answer whether the effect is large enough to act on, and the two answers diverge systematically with sample size. A difference of 0.05 units with a standard error of 0.01 yields a $z$ of 5 and a $p$-value below 0.001, and it is still a difference of 0.05 units. Conversely, a difference of 20 units with a standard error of 12 yields a $z$ of 1.67 and no significance at the 5 per cent level, and it may still be the most important finding available.

The discipline that resolves this is to fix the minimum effect of practical interest before the study, and to choose the sample size so that the interval would separate that effect from zero. This is the concept of power, and its absence is the commonest defect in small applied studies: a study too small to detect the effect it was designed to find produces a null result that is uninformative rather than reassuring.

### 5.5 The cost of statistical error, field by field

In economics, an index number is an input to contracts, pensions and interest rates, so a bias is transmitted to millions of payments and is difficult to retract. A base-weighted index that overstates inflation by half a point per year, compounded over a decade, misstates real wages permanently.

In business, the cost of a forecasting error is asymmetric. Over-forecasting ties capital in inventory that may become obsolete; under-forecasting loses sales and goodwill. Because the two costs differ, the optimal forecast is not the mean of the predictive distribution but a quantile determined by the cost ratio, a point that separates competent forecasting from naive extrapolation.

In medicine, the two errors of a diagnostic test have different weights, and a policy that reports only overall accuracy conceals which error is being made. In a screening programme for a treatable disease with a cheap confirmatory test, false positives are tolerable and false negatives are dangerous, so sensitivity is weighted more heavily than specificity, and the choice of threshold follows from that weighting.

In the social sciences, an error affects a group that is often absent from the sample and therefore unable to contest the finding. The cost is compounded because social measurements feed policy, and policy allocates resources.

In engineering, an error in a tolerance or a reliability estimate is a safety question. A reliability figure quoted from a handful of accelerated tests, without a confidence statement, is not evidence of safety.

### 5.6 Ethical and reporting obligations

The ethical obligations of applied statistics follow from the asymmetry of cost: the analyst usually bears little of it.

- Report the design, the sampling frame and the response rate before the findings, so that a reader can judge the reach of the conclusions.
- Report point estimates with intervals and state the confidence level.
- Report all outcomes specified in advance, including those that showed nothing.
- Report the number of comparisons and adjust the level, or state explicitly that no adjustment was made.
- Distinguish association from causation in the grammar of the report, not only in a footnote.
- Do not select a subgroup after inspecting the data and present it as the primary analysis.
- Preserve the data and the analysis code so that the result can be reproduced.
- Declare conflicts of interest, including who funded the work and who will benefit from the conclusion.
- Report harm as fully as benefit. A trial that reports only the primary efficacy outcome omits the information a patient needs.

### 5.7 The specific limits of each tool

Each technique in this topic has a boundary beyond which it is misapplied, and the boundary is a property of the method rather than of the user.

A Laspeyres index measures the cost of a fixed basket and therefore overstates the cost of maintaining a given standard of living when relative prices change and households substitute. A Paasche index requires current quantity data that are usually unavailable at the time the index is needed. Neither measures welfare, and a rise in the index is compatible with a rise in welfare if quality has improved.

A regression line describes the conditional mean of the response within the observed range of the predictor. It does not describe individuals, it does not establish causation, and it does not extrapolate. A high coefficient of determination is compatible with a badly specified model, because it measures fit inside the sample and not validity outside it.

A two-by-two diagnostic table describes a test at one threshold in one population. Moving the threshold trades sensitivity against specificity along the receiver operating characteristic curve, and moving to a population with a different prevalence changes the predictive values while leaving sensitivity and specificity unchanged.

A control chart detects departures from the historical pattern. It cannot detect a shift that occurred before the baseline was established, and it cannot tell whether the process is capable, only whether it is stable. A process in perfect control and centred outside its specification produces scrap with impeccable consistency.

A tolerance interval is a statement about a population of items and requires the sample to be representative of that population. An interval computed from items produced on one machine, in one shift, does not cover the output of other machines.

A reliability function assumes a hazard model. The exponential model with its constant hazard is convenient and often wrong for mechanical components, which typically show a wear-out phase with increasing hazard; using the exponential model beyond the infant-mortality period understates the risk of failure.

A composite index is a construction whose value depends on the choice of indicators, the normalisation ranges, the aggregation rule and the weights. Two defensible constructions of the same concept can rank countries differently, and the ranking is a property of the construction.

### 5.8 Common errors, collected

- Confusing the value of an index with the percentage change: an index of 122.35 means a rise of 22.35 per cent, not of 122.35 per cent.
- Computing a simple aggregate price index, which lets an expensive item with a small market share dominate.
- Reporting a nominal change without deflating by a price index.
- Interpreting a regression slope as a causal effect.
- Extrapolating a fitted line beyond the observed range of the predictor.
- Computing a predictive value from a sample whose prevalence differs from the population to which the claim is applied.
- Confusing sensitivity with predictive value, or reading a two-by-two table across the rows when the columns are required.
- Reporting a relative risk without the absolute risk, or an odds ratio as if it were a relative risk when the outcome is common.
- Quoting a proportion without a standard error, or with a standard error that ignores the design effect.
- Applying the normal approximation to a proportion with fewer than about ten successes or ten failures.
- Treating control limits as specification limits, or a stable process as a capable one.
- Estimating the process standard deviation from the same data used to judge the process.
- Adjusting a process in response to common-cause variation, which increases the variation.
- Quoting a capability ratio without stating whether the process is centred.
- Using a tolerance interval from a sample that is not representative of the production population.
- Assuming an exponential reliability model for a component in its wear-out phase.
- Aggregating a composite index with arithmetic means when balance between dimensions is the intended property.
- Testing many hypotheses and reporting one, or adding data until significance appears.
- Treating statistical significance as practical importance.
- Omitting the measure of reliability, which converts a finding into an assertion.

### 5.9 The single structure behind the five fields

The closing observation of this topic is that every applied quantity studied here is a ratio of a signal to a scale, and every inferential statement is that ratio compared with the variability expected under no effect.

The index number is a ratio of two expenditures. The elasticity is a ratio of two relative changes. The defect fraction is a ratio of two counts. The predictive value is a ratio of a cell to a margin. The relative risk is a ratio of two ratios. The capability ratio is a ratio of a tolerance to six standard deviations. The hazard is a ratio of events to exposure. The standardised deviation is a ratio of a departure to a spread.

Once this is seen, the workflow of an applied study becomes a single drill that can be executed in any field: name the signal, name its scale, form the ratio, attach the uncertainty, and state the decision that the ratio and its uncertainty jointly support. The differences between economics, business, medicine, the social sciences and engineering then reduce to differences in the numerator and the denominator, and to differences in what a mistake costs the people who did not commission the study.
