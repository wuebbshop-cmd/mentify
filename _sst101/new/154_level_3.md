## 1. Foundational Concepts, Definitions, and Axioms

### 1.1 What this topic actually tests

This is a survey topic, and survey topics are examined differently from technical ones. You will rarely be asked to prove a result here. You will be asked to do four things: recognise which field a scenario belongs to, name the correct statistical instrument, compute it correctly under time pressure, and interpret the number in the language of the field. Almost every lost mark in this topic falls into one of three buckets: the wrong instrument, correct arithmetic with a misread table, or a correct number with no interpretation.

The syllabus names five fields: economics, business, medicine, the social sciences, and engineering. Each contributes one or two characteristic instruments, and each instrument has one characteristic trap. Mastering the topic therefore means holding five pairs in memory, plus the general machinery of description and inference that all five share.

The shared machinery is short. Descriptive statistics uses numerical and graphical methods to find patterns in a data set and present them conveniently. Inferential statistics uses sample data to make estimates, decisions, predictions, or other generalizations about a larger set of data. A population is the set of units of interest, a variable is a characteristic of a unit, a sample is a subset of units, a statistical inference is a generalization from sample to population, and a measure of reliability is a statement attached to that generalization which quantifies confidence in it. Every question in this topic is a special case of that chain.

### 1.2 Command words and what they demand

The mark scheme is driven by the command word, so read it before reading the data.

- **State** or **define** requires one sentence, no example. Two marks at most, and the mark is for the precise phrase, not for a paraphrase that loses the qualifying clause.
- **Distinguish** requires two statements in parallel, usually with the phrase "whereas". A single definition earns one mark out of two.
- **Calculate** requires the substituted values, the arithmetic, and the result with its units. Marks are allocated to the substitution and the result separately, so an unexplained final number earns at most half.
- **Interpret** requires a sentence in the vocabulary of the scenario, mentioning the units and the direction. "The index is 116.67" earns nothing; "the same basket costs 16.67 per cent more" earns the mark.
- **Comment on** requires a judgement plus a reason, and the reason must be a number from the working. Unsupported opinion earns nothing.
- **Explain why** requires a mechanism, not a definition. In this topic the mechanism is nearly always about variation, bias, or base rates.

### 1.3 The five-field map

The five fields map onto five instruments, and the map should be memorised in both directions. The middle column below is the formula; the right column is the sentence that earns the interpretation mark.

| Field | Characteristic instrument | The interpretation sentence |
|---|---|---|
| Economics | Laspeyres and Paasche price indexes, real versus nominal | The same basket now costs this percentage more, so real income has changed by this percentage |
| Business | Fraction nonconforming, control limits, regression forecast | The process is or is not stable; the forecast is this value plus or minus this interval |
| Medicine | Sensitivity, specificity, predictive values, relative and absolute risk | A positive result means this probability of disease at this prevalence; this many patients must be treated |
| Social sciences | Survey proportion with standard error, Likert composite, index construction | Support lies in this interval; the composite index is this value, built this way |
| Engineering | Capability ratio, control limits, reliability, tolerance, calibration | The process can or cannot meet the tolerance; this proportion fails by this time |

### 1.4 Definitions to reproduce accurately

> **Definition (Descriptive and inferential statistics).** Descriptive statistics uses numerical and graphical methods to look for patterns in a data set and to present that information in a convenient form. Inferential statistics uses sample data to make estimates, decisions, predictions, or other generalizations about a larger set of data.

> **Definition (Population, variable, sample, inference, reliability).** A population is a set of units that we are interested in studying; a variable is a characteristic of an individual population unit; a sample is a subset of the units of a population; a statistical inference is an estimate, prediction, or other generalization about a population based on sample information; a measure of reliability is a statement, usually associated with an inference, that quantifies confidence in it.

> **Definition (Quantitative and qualitative data).** Quantitative data are measurements recorded on a naturally occurring numerical scale; qualitative data cannot be measured on a natural numerical scale and can only be classified into one of a group of categories.

> **Definition (Index number).** An index number expresses the value of a variable, or the cost of a basket of goods, in one period as a percentage of its value in a base period.

> **Definition (Sensitivity and specificity).** Sensitivity is the probability of a positive test given disease; specificity is the probability of a negative test given no disease.

> **Definition (Predictive value).** The predictive value of a positive test is the probability of disease given a positive test.

> **Definition (Control limits).** Control limits are the centre line of a chart plus and minus three standard errors of the plotted statistic.

> **Definition (Process capability).** The capability ratio is the specification width divided by six process standard deviations; the centred capability ratio uses the distance from the process mean to the nearer specification limit.

> **Definition (Reliability).** Reliability is the probability that an item performs its required function for a stated period under stated conditions.

### 1.5 The formula sheet as a set of axioms

Five formulas generate almost every calculation in this topic. Write them from memory in the first two minutes of the exam.

**Index numbers.** With base prices and quantities $p_{0i}, q_{0i}$ and current prices $p_{1i}$,

$$
I_L = \frac{\sum p_{1i}q_{0i}}{\sum p_{0i}q_{0i}}\times 100, \qquad I_P = \frac{\sum p_{1i}q_{1i}}{\sum p_{0i}q_{1i}}\times 100 .
$$

**Predictive value.** With sensitivity $s$, specificity $c$ and prevalence $\pi$,

$$
\text{PPV} = \frac{s\pi}{s\pi + (1-c)(1-\pi)} .
$$

**Standard error of a proportion and its interval.**

$$
\text{SE} = \sqrt{\frac{\hat{p}(1-\hat{p})}{n}}, \qquad \hat{p} \pm z\sqrt{\frac{\hat{p}(1-\hat{p})}{n}} .
$$

**Control limits.**

$$
\text{UCL} = \bar{\bar{x}} + \frac{3\sigma}{\sqrt{n}}, \qquad \text{LCL} = \bar{\bar{x}} - \frac{3\sigma}{\sqrt{n}} .
$$

**Capability and its defect rate.**

$$
C_p = \frac{U-L}{6\sigma}, \qquad p_{\text{defect}} = 2\left(1-\Phi\left(3C_p\right)\right) .
$$

**Reliability.**

$$
R(t) = e^{-\lambda t}, \qquad \text{MTTF} = \frac{1}{\lambda} .
$$

### 1.6 How marks are distributed in this topic

A typical question in this topic is worth between eight and twenty marks and is structured as three parts: a definition or identification part worth two to four marks, a computation worth five to ten, and an interpretation or comment worth three to five. The interpretation part is the cheapest to lose and the cheapest to secure, because it is usually one sentence. Candidates who run out of time almost always run out during the computation and therefore forfeit the interpretation marks as well, which is why the time strategy in Section 5 matters more than any formula.

## 2. Theorems, Lemmas, and Analytical Properties

### 2.1 Index-number properties you may be asked to state

> **Property (Proportionality).** If every price is multiplied by a constant, the index is multiplied by that constant.

> **Property (Commensurability).** The index is unaffected by a change in the units of measurement applied consistently to all items.

> **Property (Time reversal).** Comparing period 1 with period 0 should give the reciprocal of comparing period 0 with period 1.

> **Lemma (Laspeyres-Paasche ordering).** When households substitute away from items whose relative prices have risen, the Paasche index is less than the Laspeyres index.

The ordering lemma is examined as a comment rather than as a proof. The expected sentence is that the base-weighted index overstates the cost of the current standard of living because it holds quantities fixed at a pattern that households have since abandoned.

> **Corollary (Fisher as a compromise).** The geometric mean of the two indexes,
> 
> $$
> I_F = \sqrt{I_L I_P},
> $$
> 
> satisfies both reversal tests and lies between them.

### 2.2 The base-rate lemma and its consequences

> **Lemma (Predictive value increases with prevalence).** For fixed sensitivity and specificity both above one half, the predictive value of a positive test increases with the prevalence.

The examinable consequence is the screening paradox: a test with sensitivity 0.95 and specificity 0.90 applied where prevalence is 0.02 gives a predictive value of only about 0.162, so five out of six positive results are false. The lemma explains why the same test is useful in a clinic and useless as a mass screen.

> **Property (Odds form).** A positive result multiplies the prior odds of disease by the positive likelihood ratio
> 
> $$
> \text{LR}^{+} = \frac{\text{sensitivity}}{1-\text{specificity}} .
> $$

### 2.3 Standard-error lemmas

> **Lemma (Variance of a proportion).** For $n$ independent observations, $\text{Var}(\hat{p}) = p(1-p)/n$.

> **Lemma (Variance of a difference of proportions).** For independent samples of sizes $n_1$ and $n_0$,
> 
> $$
> \text{Var}\left(\hat{p}_1 - \hat{p}_0\right) = \frac{p_1(1-p_1)}{n_1} + \frac{p_0(1-p_0)}{n_0} .
> $$

> **Lemma (Design effect).** Under cluster sampling with cluster size $m$ and intraclass correlation $\rho$, the variance is inflated by $1 + (m-1)\rho$.

The design-effect lemma is the standard route to a comment mark in a social-science question: a cluster sample of 500 respondents drawn from 20 clusters of 25 with $\rho = 0.05$ carries the information of only 227 independent respondents, because $1 + 24(0.05) = 2.2$.

### 2.4 Control-chart results

> **Theorem (False-alarm probability at three sigma).** For a normally distributed plotted statistic, the probability that a single point falls outside a three-sigma limit while the process is stable is $0.0027$.

> **Corollary (Average run length).** The expected number of plotted points before a false alarm is $1/0.0027 = 370$.

> **Property (Runs rules).** A run of seven consecutive points on one side of the centre line, or six consecutive points trending in one direction, signals a shift even when no point exceeds a limit, because such patterns are rare under stability.

The average run length is the standard justification for the constant three, and it is worth one or two marks when a question asks why three sigma is used rather than two.

### 2.5 Capability results

> **Theorem (Defect rate from capability).** For a centred normal process,
> 
> $$
> p_{\text{defect}} = 2\left(1-\Phi\left(3C_p\right)\right).
> $$

Three values should be memorised as anchors, because they convert a capability ratio into an answer instantly.

| Capability $C_p$ | $3C_p$ | Defect rate | Parts per million |
|---|---|---|---|
| 0.833 | 2.5 | 0.0124 | 12 420 |
| 1.000 | 3.0 | 0.0027 | 2700 |
| 1.333 | 4.0 | 0.0000633 | 63 |

> **Property (Centred capability).** When the process is off centre, $C_{pk} < C_p$, and the defect rate is governed by $C_{pk}$ rather than by $C_p$.

The property is examined as a trap: a candidate who computes $C_p = 1.4$ for an off-centre process and declares it capable has answered the wrong question.

### 2.6 Reliability results

> **Theorem (Exponential reliability).** With constant hazard $\lambda$, $R(t) = e^{-\lambda t}$ and $\text{MTTF} = 1/\lambda$.

> **Property (Memorylessness).** For an exponential lifetime, the probability of surviving a further $t$ hours does not depend on the age already reached.

> **Definition (B10 life).** The B10 life is the time by which ten per cent of items have failed, obtained from
> 
> $$
> R(t) = 0.9 \quad \text{gives} \quad t = \frac{-\ln(0.9)}{\lambda} .
> $$

### 2.7 Survival and mortality results

> **Theorem (Product-limit form).** With $d_j$ failures at $t_j$ among $n_j$ at risk,
> 
> $$
> \hat{S}(t) = \prod_{t_j \le t}\left(1-\frac{d_j}{n_j}\right).
> $$

> **Property (Censoring).** A censored subject leaves the risk set at the censoring time without contributing a failure, so the denominator of the hazard at later times shrinks.

> **Definition (Crude mortality rate).** Deaths in a period divided by person-time at risk, usually per 1000 person-years.

The examinable point is that the crude rate is not comparable between populations with different age structures, which is why standardised rates exist.

### 2.8 Regression and elasticity results

> **Theorem (Least squares fit).** For $n$ pairs,
> 
> $$
> b = \frac{S_{xy}}{S_{xx}}, \qquad a = \bar{y} - b\bar{x}, \qquad r^{2} = \frac{S_{xy}^{2}}{S_{xx}S_{yy}} .
> $$

> **Property (Elasticity of a linear demand function).** For $Q = a + bp$,
> 
> $$
> \varepsilon = \frac{p}{Q}\cdot b ,
> $$
> 
> which varies along the line even though the slope is constant.

The last property is a frequent trap. The slope is constant, the elasticity is not, and a question that asks for "the" elasticity must specify the price at which it is evaluated.

### 2.9 Measurement and index-construction results

> **Lemma (Variance of a composite).** For a sum of items,
> 
> $$
> \text{Var}\left(\sum X_j\right) = \sum \text{Var}\left(X_j\right) + 2\sum_{j<l}\text{Cov}\left(X_j, X_l\right).
> $$

> **Property (Geometric aggregation penalises imbalance).** For fixed sum, the geometric mean is largest when the components are equal, so a composite built as a geometric mean cannot be raised by improving one dimension at the expense of another.

> **Definition (Min-max normalisation).** $I = (x - x_{\min})/(x_{\max} - x_{\min})$.

### 2.10 The tolerance-interval result

> **Property (Coverage of a k-sigma interval).** For a normal population, the interval $\mu \pm k\sigma$ covers the proportion
> 
> $$
> 2\Phi(k) - 1 .
> $$

The multipliers to remember are 1.96 for 95 per cent, 2.576 for 99 per cent, and 3 for 99.73 per cent. A tolerance interval computed from a finite sample must use a larger multiplier than these, because the sample mean and standard deviation are themselves uncertain, and the multiplier shrinks towards the normal quantile as the sample grows.

## 3. Formal Proofs, Derivations, and Methods

### 3.1 The four-step exam routine

Every calculation in this topic yields to the same four steps, and performing them in order prevents nearly all avoidable errors.

Step 1. Write down the given quantities with their symbols, and write down what is required with its symbol. This takes twenty seconds and prevents the commonest error, which is computing the quantity that was not asked for.

Step 2. Write the formula in symbols before substituting any numbers. A formula written first can earn method marks even if the arithmetic fails.

Step 3. Substitute, and compute in one direction only, writing each intermediate value on its own line. Never recompute a rounded value; carry full precision and round once at the end.

Step 4. State the result with units, then write one interpretative sentence naming the field and the decision. The interpretative sentence is worth between one and three marks and takes one line.

### 3.2 Bayes under exam conditions

Starting from the definition of conditional probability,

$$
P\left(D \mid T^{+}\right) = \frac{P\left(D \cap T^{+}\right)}{P\left(T^{+}\right)} ,
$$

apply the multiplication rule to the numerator and the law of total probability to the denominator over the partition $\{D, D'\}$:

$$
P\left(D \mid T^{+}\right) = \frac{P\left(T^{+} \mid D\right)P(D)}{P\left(T^{+} \mid D\right)P(D) + P\left(T^{+} \mid D'\right)P(D')} .
$$

Substituting sensitivity, specificity and prevalence gives the working form

$$
\text{PPV} = \frac{s\pi}{s\pi + (1-c)(1-\pi)} .
$$

In an exam, the fastest and least error-prone presentation is a table of 10 000 people rather than the formula, because the table makes the arithmetic auditable and shows the examiner that the direction of the table is understood. Either route earns full marks if the numbers are right; the table route is easier to check under time pressure.

### 3.3 Three-sigma limits from the standard error

Let individual measurements have mean $\mu$ and standard deviation $\sigma$, and let subgroups of $n$ be drawn independently. The subgroup mean has variance $\sigma^{2}/n$, so its standard deviation is $\sigma/\sqrt{n}$. Three standard errors either side of the centre line gives

$$
\text{UCL} = \mu + \frac{3\sigma}{\sqrt{n}}, \qquad \text{LCL} = \mu - \frac{3\sigma}{\sqrt{n}} .
$$

Under normality, the probability that one point lies outside is $2(1-\Phi(3)) = 0.0027$, so the expected number of points before a false alarm is 370. When $\mu$ and $\sigma$ are estimated from a baseline of subgroups, the tabulated constants for the mean range replace the direct standard deviation, but the structure of the limits is unchanged.

### 3.4 Capability to parts per million

For a centred process the distance from the mean to either limit is $(U-L)/2$, and in units of standard deviations this is

$$
\frac{(U-L)/2}{\sigma} = 3C_p .
$$

The fraction outside the limits is therefore

$$
p = 2\left(1-\Phi\left(3C_p\right)\right).
$$

For $C_p = 1$ this is 0.0027, or 2700 parts per million. For $C_p = 1.333$ it is $2\Phi(-4)$, which is 0.0000633, or 63 parts per million. For $C_p = 0.833$ it is $2\Phi(-2.5)$, which is 0.0124, or 12 420 parts per million. The conversion is steep, so a modest reduction in standard deviation buys a large reduction in scrap.

### 3.5 Interval for a proportion and the sample-size inversion

The central limit theorem gives

$$
\frac{\hat{p}-p}{\sqrt{p(1-p)/n}} \sim N(0,1),
$$

so replacing $p$ by $\hat{p}$ in the denominator and inverting the inequality gives

$$
\hat{p} - z\sqrt{\frac{\hat{p}(1-\hat{p})}{n}} \le p \le \hat{p} + z\sqrt{\frac{\hat{p}(1-\hat{p})}{n}} .
$$

Setting the half-width equal to a required margin $E$ and solving for $n$ gives

$$
n = \frac{z^{2}p(1-p)}{E^{2}} ,
$$

with $p = 0.5$ used as the conservative planning value when no estimate exists. If the design is clustered, multiply the result by the design effect.

### 3.6 Exponential reliability and its inverse uses

With constant hazard, $R(t) = e^{-\lambda t}$, so $\lambda = -\ln R(t)/t$ and $\text{MTTF} = 1/\lambda$. The three examinable uses are forward (find the survival probability at a stated time), inverse (find the time at which a stated proportion survive, which is the B10 life when the proportion is 0.9), and comparative (find how long a redundant system survives, which requires the product of survival functions for independent components).

### 3.7 Why the two indexes differ

With normalised base weights $w_{0i}$ and current weights $w_{1i}$,

$$
I_L = \sum_{i} w_{0i}r_i, \qquad I_P = \sum_{i} w_{1i}r_i, \qquad r_i = \frac{p_{1i}}{p_{0i}} ,
$$

so

$$
I_P - I_L = \sum_{i}\left(w_{1i}-w_{0i}\right)r_i .
$$

The weight change is negative for items whose relative prices rose, because households buy less of them, and each such item has a relatively high $r_i$. The sum is therefore negative, which is the ordering lemma. A question that asks why the Paasche index is lower wants exactly this argument in words: substitution moves weight away from the items that became expensive.

### 3.8 Question patterns across the five fields

**Economics.** The standard pattern gives a table of prices and quantities for two periods and asks for one index, then for a comment on the difference between two indexes, then for a real-income statement. The marks are for the two expenditure sums, the division, the identification of the weighting, and the deflation sentence. A second pattern gives price and quantity series and asks for the elasticity at a stated price, in which case the marks are for the slope, the ratio, and the comment that demand is elastic or inelastic.

**Business.** The standard pattern gives counts of defectives from a run of samples and asks for a control chart, then for a judgement on one sample, then for the action to be taken. The marks are for the centre line, the standard error, the limits, the comparison, and the recommendation to investigate rather than to adjust the limits. A second pattern gives monthly sales and asks for a forecast, where the marks are for the slope, the intercept, the substituted future value, and the warning about extrapolation. A third gives weekly demand with a mean and a standard deviation, together with a lead time and a service level, and asks for a safety stock and a reorder point; the marks are for the standard deviation of demand over the lead time, the normal quantile, the buffer, and the reorder point.

**Medicine.** The standard pattern gives a two-by-two table and asks for sensitivity, specificity and predictive values, then for a comment on the effect of prevalence. The marks are for the two column readings, the two row readings, and the base-rate sentence. A second pattern gives trial counts and asks for relative risk, absolute risk reduction and number needed to treat, where the marks are for the two risks, the ratio, the difference, the reciprocal and the statement that the absolute measure drives the decision.

**Social sciences.** The standard pattern gives a survey result and asks for an estimate, an interval, and a comment on whether a majority exists. The marks are for the proportion, the standard error, the multiplier, the interval in percentage points, and the conclusion with its uncertainty. A second pattern gives Likert frequencies and asks for a mean and a comment on the scale's limitations.

**Engineering.** The standard pattern gives specification limits and a process standard deviation and asks for capability and expected defect rate. The marks are for the width, the ratio, the standardised distance, the tail probability, and the recommendation to reduce variation. A second pattern gives failure times and asks for reliability at a stated time and for the mean time to failure. A third gives two small samples under two settings and asks for the pooled variance, the standard error of the difference and a conclusion, where the marks are for the pooled variance, the standard error, the statistic and the interpretation in the units of the measurement. A fourth gives paired readings of a standard and an instrument and asks for the calibration line and an inverse estimate, where the marks are for the slope, the intercept, the inversion and the refusal to extrapolate.

### 3.9 Trap table

Each error listed here reappears every year, and the third column names the correction that earns the mark.

| Trap | What candidates do | What earns the mark |
|---|---|---|
| Index versus percentage change | Report a rise of 116.67 per cent | Report a rise to 116.67 per cent, that is of 16.67 per cent |
| Reading a two-by-two table in the wrong direction | Divide a row total by a column total for sensitivity | Read sensitivity down the disease column, predictive value across the positive row |
| Predictive value quoted without prevalence | Give 0.95 as the chance of disease given a positive test | Give the predictive value at the stated prevalence, and say it would change elsewhere |
| Relative risk reported alone | Say the risk was halved and stop | Add the absolute reduction and the number needed to treat |
| Odds ratio used as a relative risk | Report 0.58 as a 42 per cent reduction when events are common | State that the odds ratio overstates the relative risk when the outcome is common |
| Control limits treated as specification limits | Conclude the process is acceptable because points are inside the limits | Distinguish stability from capability, and compare with the specification separately |
| Limits computed from the data being judged | Estimate the standard deviation from the out-of-control period | Estimate from a baseline period known to be stable |
| Standard error of a mean confused with a standard deviation | Divide by $n$ instead of $\sqrt{n}$ | Use $\sigma/\sqrt{n}$, and say which quantity is being plotted |
| Capability computed off centre | Quote $C_p$ alone | Quote $C_{pk}$ as well when the mean is not centred |
| Tolerance interval equated with a confidence interval | Use $\pm 1.96s$ and claim 95 per cent of items | State that the interval covers items, so the multiplier exceeds the normal quantile |
| Extrapolating a calibration line | Convert a reading far outside the standards | Refuse to extrapolate and state the calibrated range |
| Elasticity treated as constant | Quote one elasticity for a whole linear demand curve | Evaluate at the stated price and note that elasticity varies along the line |
| Likert mean reported as an amount | Say the average respondent agrees | Say the average code is 3.15 and note the equal-spacing assumption |
| Cluster sample treated as simple random | Use $n$ in the standard error | Apply the design effect and report the effective sample size |
| Confounding ignored in an observational comparison | Conclude that the treatment caused the difference | Name the confounder and the design that would remove it |
| Multiplicity ignored | Report the smallest $p$-value out of twenty tests | Report the number of tests, or compare with the adjusted level |
| Significance treated as importance | Conclude that a 1.2-second improvement matters | Separate statistical from practical significance and state the minimum effect of interest |
| Missing reliability statement | Give a point estimate and stop | Attach an interval or a confidence to every inferential claim |

## 4. Representative Worked Examples and Solutions

### 4.1 Model solution 1: three indexes and a real-income statement

**Question.** A household buys three items. In the base period it bought 50 units at 60, 30 units at 90, and 20 units at 120. In the current period the prices are 75, 90 and 150, and the quantities are 45, 32 and 22. Compute the Laspeyres and Paasche price indexes, comment on the difference, and state the change in real income if nominal income rose by 10 per cent. [12 marks]

Step 1. Compute the base-period expenditure. [1 mark]

$$
\sum p_0q_0 = 50(60) + 30(90) + 20(120) = 3000 + 2700 + 2400 = 8100 .
$$

Step 2. Price the base basket at current prices. [2 marks]

$$
\sum p_1q_0 = 50(75) + 30(90) + 20(150) = 3750 + 2700 + 3000 = 9450 .
$$

Step 3. Form the Laspeyres index. [1 mark]

$$
I_L = \frac{9450}{8100}\times 100 = 116.67 .
$$

Step 4. Price the current basket at base prices and at current prices. [2 marks]

$$
\sum p_0q_1 = 45(60) + 32(90) + 22(120) = 2700 + 2880 + 2640 = 8220 ,
$$

$$
\sum p_1q_1 = 45(75) + 32(90) + 22(150) = 3375 + 2880 + 3300 = 9555 .
$$

Step 5. Form the Paasche index. [1 mark]

$$
I_P = \frac{9555}{8220}\times 100 = 116.24 .
$$

Step 6. Comment on the difference. [2 marks] The Paasche index is 0.43 points lower than the Laspeyres index because the household changed what it bought in response to the price changes. Its purchases of the first item, whose price rose by 25 per cent, fell from 50 units to 45, so the weight on that item's high relative fell from 0.370 to 0.329, while the weight on the second item, whose price did not change, rose from 0.333 to 0.350. The shift of weight towards the cheaper relative pulls the current-weighted index down, so the base-weighted index slightly overstates the rise in the cost of the household's present standard of living. The gap is small because the substitutions were small.

Step 7. Deflate nominal income. [2 marks]

$$
\text{real income index} = \frac{110}{116.67}\times 100 = 94.29 .
$$

Step 8. Interpret. [1 mark] A nominal rise of 10 per cent against a price rise of 16.67 per cent leaves real income 5.71 per cent lower, so the household can buy less than before.

### 4.2 Model solution 2: control chart, judgement, and capability

**Question.** A factory inspects 250 items each day. Over 25 days known to be stable, 750 items in total were defective. (a) Construct a three-sigma control chart for the daily fraction defective. (b) State the action for a day on which 45 items were defective and for a day on which 50 were. (c) The critical dimension has specification limits 0.75 and 1.25 with a stable process standard deviation of 0.06. Compute the capability and the expected defect rate. [14 marks]

Step 1. Compute the centre line. [1 mark]

$$
\bar{p} = \frac{750}{25(250)} = \frac{750}{6250} = 0.12 .
$$

Step 2. Compute the standard error of a daily fraction. [2 marks]

$$
\sigma_{\hat{p}} = \sqrt{\frac{0.12(0.88)}{250}} = \sqrt{0.0004224} = 0.02055 .
$$

Step 3. Form the limits. [2 marks]

$$
\text{UCL} = 0.12 + 3(0.02055) = 0.1817, \qquad \text{LCL} = 0.12 - 3(0.02055) = 0.0583 .
$$

Step 4. Judge the two days. [2 marks] The first day gives $45/250 = 0.18$, which is below 0.1817 and therefore inside the limits; the process should be left alone. The second day gives $50/250 = 0.20$, which exceeds 0.1817 and signals a change; the cause should be investigated before any adjustment is made.

Step 5. Comment on the near miss. [1 mark] The first day sits within 0.002 of the upper limit, which is not itself a signal because a single point inside the limits is ordinary variation, but a second consecutive high day would justify action under the runs rules.

Step 6. Compute the capability ratio. [2 marks]

$$
C_p = \frac{1.25 - 0.75}{6(0.06)} = \frac{0.50}{0.36} = 1.389 .
$$

Step 7. Convert to a defect rate. [2 marks]

$$
3C_p = 4.167, \qquad p_{\text{defect}} = 2\left(1-\Phi(4.167)\right) \approx 3.1\times 10^{-5},
$$

which is about 31 parts per million.

Step 8. Interpret and recommend. [2 marks] The process is capable, since the natural spread of $0.36$ is well inside the specification width of $0.50$, and the expected defect rate of 31 parts per million is negligible in most production settings. The correct recommendation is to leave the process alone and to monitor it, because adjusting a capable and stable process increases variation.

### 4.3 Model solution 3: a screening test at two prevalences

**Question.** A test for a condition has sensitivity 0.95 and specificity 0.90. (a) Compute the predictive value of a positive result and of a negative result when the prevalence is 0.02. (b) Repeat the positive predictive value when the test is used in a clinic where prevalence is 0.30. (c) Comment on the use of the test as a mass screen. [12 marks]

Step 1. Take a hypothetical 10 000 people at prevalence 0.02. [1 mark] Of these, 200 have the condition and 9800 do not.

Step 2. Compute the four cells. [3 marks] Of the 200 with the condition, $0.95(200) = 190$ test positive and 10 test negative. Of the 9800 without it, $0.10(9800) = 980$ test positive and $0.90(9800) = 8820$ test negative.

Step 3. Tabulate and check the margins. [1 mark]

| | Condition present | Condition absent | Total |
|---|---|---|---|
| Test positive | 190 | 980 | 1170 |
| Test negative | 10 | 8820 | 8830 |
| Total | 200 | 9800 | 10 000 |

Step 4. Compute the positive predictive value. [1 mark]

$$
\text{PPV} = \frac{190}{1170} = 0.162 .
$$

Step 5. Compute the negative predictive value. [1 mark]

$$
\text{NPV} = \frac{8820}{8830} = 0.9989 .
$$

Step 6. Repeat at prevalence 0.30 by Bayes. [2 marks]

$$
\text{PPV} = \frac{0.95(0.30)}{0.95(0.30) + 0.10(0.70)} = \frac{0.285}{0.285 + 0.070} = 0.803 .
$$

Step 7. Comment on mass screening. [2 marks] At a prevalence of 0.02, only 16.2 per cent of positive results are true, so 838 of every 1000 positives would be referred unnecessarily, which is both costly and harmful. At a prevalence of 0.30 the same test gives a predictive value of 0.803 and is genuinely useful. The test has not changed; the base rate has. A mass screen is therefore justified only if a cheap and safe confirmatory test follows, or if the condition is serious enough that the harm of a false negative outweighs 838 unnecessary referrals.

Step 8. State the general rule. [1 mark] Sensitivity and specificity are properties of the test, whereas predictive values are properties of the test in a population, and any report that quotes the first as if it were the second overstates the value of the test.

### 4.4 Model solution 4: a survey proportion with a design effect

**Question.** In a survey of 500 households selected in 25 clusters of 20, 285 households support a levy. (a) Estimate the population proportion with a 95 per cent interval under simple random sampling. (b) The intraclass correlation is estimated as 0.05; recompute the interval. (c) State the sample size needed for a margin of three percentage points. [13 marks]

Step 1. Compute the sample proportion. [1 mark]

$$
\hat{p} = \frac{285}{500} = 0.57 .
$$

Step 2. Compute the standard error. [2 marks]

$$
\text{SE} = \sqrt{\frac{0.57(0.43)}{500}} = \sqrt{0.0004902} = 0.02214 .
$$

Step 3. Form the interval. [2 marks]

$$
0.57 \pm 1.96(0.02214) \quad \text{gives} \quad 0.5266 \text{ to } 0.6134 .
$$

Step 4. Comment on the majority question. [1 mark] The interval lies entirely above 0.50, so the survey supports the conclusion that a majority favours the levy, at the 5 per cent level.

Step 5. Compute the design effect. [2 marks]

$$
\text{deff} = 1 + (20-1)(0.05) = 1.95, \qquad n_{\text{eff}} = \frac{500}{1.95} = 256 .
$$

Step 6. Recompute the interval. [2 marks]

$$
\text{SE}_{\text{cluster}} = 0.02214\sqrt{1.95} = 0.03092 ,
$$

$$
0.57 \pm 1.96(0.03092) \quad \text{gives} \quad 0.5094 \text{ to } 0.6306 .
$$

Step 7. Comment on the effect. [1 mark] The conclusion survives, but the interval is half again as wide, and a survey of 500 clustered households carries about as much information as 256 independent ones. Reporting the nominal sample size without the design effect overstates the precision.

Step 8. Compute the required sample size. [2 marks]

$$
n = \frac{(1.96)^{2}(0.57)(0.43)}{(0.03)^{2}} = 1046.2, \quad \text{so } 1047 ,
$$

and with the design effect, $1046.2(1.95) = 2040.1$, so about 2041 households.

### 4.5 Model solution 5: reporting a trial

**Question.** In a randomised trial with 400 patients per arm, 32 patients on the new treatment and 52 on the control had the event within one year. Compute the risks, the relative risk, the absolute risk reduction, the number needed to treat and the odds ratio, with a 95 per cent interval for the relative risk. Comment on which measure should guide the decision. [14 marks]

Step 1. Compute the two risks. [2 marks]

$$
r_1 = \frac{32}{400} = 0.08, \qquad r_0 = \frac{52}{400} = 0.13 .
$$

Step 2. Compute the relative risk. [1 mark]

$$
\text{RR} = \frac{0.08}{0.13} = 0.615 .
$$

Step 3. Compute the absolute risk reduction. [1 mark]

$$
\text{ARR} = 0.13 - 0.08 = 0.05 .
$$

Step 4. Compute the number needed to treat. [1 mark]

$$
\text{NNT} = \frac{1}{0.05} = 20 .
$$

Step 5. Compute the odds ratio. [2 marks]

$$
\text{OR} = \frac{32/368}{52/348} = \frac{0.0870}{0.1494} = 0.582 .
$$

Step 6. Compute the interval for the relative risk on the log scale. [3 marks]

$$
\text{SE}\left(\ln \text{RR}\right) = \sqrt{\frac{1}{32} - \frac{1}{400} + \frac{1}{52} - \frac{1}{400}} = \sqrt{0.04548} = 0.2133 ,
$$

$$
\exp\left(\ln 0.615 \pm 1.96(0.2133)\right) \quad \text{gives} \quad 0.405 \text{ to } 0.935 .
$$

Step 7. Comment on which measure guides the decision. [2 marks] The relative risk of 0.615 says the event rate is reduced by 38.5 per cent, and the interval excludes one, so the effect is real. The absolute reduction of five percentage points says that twenty patients must be treated for one year to prevent one event. The adoption decision depends on the absolute measure and on the cost and harm of treatment, not on the relative measure, because the same relative reduction applied to a rarer event would require very many more patients to be treated.

Step 8. Comment on the odds ratio. [2 marks] The odds ratio of 0.582 is further from one than the relative risk of 0.615 because the outcome is common. Reporting it as a 42 per cent reduction while the risk reduction is 38.5 per cent, and the absolute reduction five points, would overstate the finding.

Step 9. Convert to survival and to a mortality rate. [2 marks] The one-year survival is $1 - 0.08 = 0.92$ on the new treatment and $1 - 0.13 = 0.87$ on the control. If the 400 control patients each contributed one year of follow-up, the mortality rate is

$$
\frac{52}{400}\times 100 = 13 \text{ per } 100 \text{ person-years} ,
$$

against $32/400 \times 100 = 8$ per 100 person-years on the new treatment. The rate ratio of $8/13 = 0.615$ coincides with the relative risk here only because every patient was followed for exactly one year, and the two measures diverge as soon as follow-up times differ.

### 4.6 Model solution 6: reliability and the tolerance question

**Question.** A component has a constant failure rate of 0.000125 per hour. (a) Compute the mean time to failure and the probability of surviving 2000 and 8000 hours. (b) Compute the B10 life. (c) A shaft has specification limits 24.6 and 25.4 with a stable process standard deviation of 0.10 and a centred mean. Compute the capability and expected defect rate, and explain why a tolerance interval computed from 25 shafts must be wider than the interval of 1.96 standard deviations. [14 marks]

Step 1. Compute the mean time to failure. [1 mark]

$$
\text{MTTF} = \frac{1}{0.000125} = 8000 \text{ hours} .
$$

Step 2. Compute the survival probabilities. [2 marks]

$$
R(2000) = e^{-0.000125(2000)} = e^{-0.25} = 0.7788 ,
$$

$$
R(8000) = e^{-0.000125(8000)} = e^{-1} = 0.3679 .
$$

Step 3. Comment on the mean. [1 mark] About 22 per cent of components fail within 2000 hours and about 63 per cent within the mean lifetime, so the mean time to failure is not the age by which most items survive; the exponential distribution is strongly skewed to the right.

Step 4. Compute the B10 life. [2 marks]

$$
t = \frac{-\ln(0.9)}{0.000125} = \frac{0.10536}{0.000125} = 843 \text{ hours} .
$$

Step 5. Compute the capability ratio. [2 marks]

$$
C_p = \frac{25.4 - 24.6}{6(0.10)} = \frac{0.80}{0.60} = 1.333 .
$$

Step 6. Convert to a defect rate. [2 marks]

$$
p_{\text{defect}} = 2\left(1-\Phi(4)\right) = 6.33\times 10^{-5},
$$

which is about 63 parts per million.

Step 7. Explain the tolerance interval. [2 marks] A confidence interval covers a parameter and has half-width $1.96\sigma/\sqrt{n}$, which shrinks with the sample. A tolerance interval covers individual shafts, so its half-width is a multiple of $\sigma$ itself and does not shrink to zero. When the mean and standard deviation must be estimated from 25 shafts, the multiplier must exceed 1.96 to allow for the sampling error in both estimates, so the interval that covers 95 per cent of production with 95 per cent confidence is wider than $\pm 1.96s$. The multiplier decreases towards 1.96 as the sample grows.

Step 8. Conclude. [2 marks] The process is capable, with a natural spread of 0.60 inside the specification width of 0.80, and the expected defect rate is about 63 parts per million. A tolerance claim about individual shafts, however, requires the wider interval and the stated confidence, and cannot be made from a sample of 25 without that qualification.

### 4.7 Model solution 7: a survival curve with censoring

**Question.** Ten patients are followed after diagnosis. Deaths occur at 3, 5, 5 and 8 months, one patient is censored at 6 months, and five patients are alive at the end of the study. Estimate the survival function, state the survival at eight months, and explain why the censored patient cannot simply be excluded. [10 marks]

Step 1. Tabulate the distinct failure times and the deaths at each. [1 mark] Failures occur at $t = 3$ with one death, $t = 5$ with two deaths and $t = 8$ with one death.

Step 2. Determine the risk set at each failure time. [3 marks] Ten are at risk at 3 months. Nine are at risk at 5 months, because one has died. Six are at risk at 8 months, because three have died and one has been censored.

Step 3. Compute the conditional survival factor at each failure time. [2 marks]

$$
1 - \frac{1}{10} = 0.90, \qquad 1 - \frac{2}{9} = 0.7778, \qquad 1 - \frac{1}{6} = 0.8333 .
$$

Step 4. Multiply cumulatively and state the estimate at eight months. [2 marks]

$$
\hat{S}(8) = 0.90(0.7778)(0.8333) = 0.583 .
$$

Step 5. Explain the treatment of the censored patient. [1 mark] The patient censored at six months was known to be alive at three and five months, so that patient belongs in the risk sets at those times and contributes information; after six months nothing is known, so the patient leaves the risk set without being counted as a failure or as a survivor to eight months. Excluding the patient altogether would discard the information contributed before censoring; counting the patient as a survivor to eight months would overstate survival.

Step 6. Comment on precision. [1 mark] With ten patients the estimate rests on four events, so a confidence interval is wide and the curve should be reported with its numbers at risk rather than as a bare percentage.

## 5. Mathematical Extensions, Limits, and Common Errors

### 5.1 The high-yield list

The following statements are the ones most often worth a mark, and each should be reproducible in one sentence.

An index number is a ratio of two expenditures expressed as a percentage, and an index of 116.67 means a rise of 16.67 per cent. The Laspeyres index holds base quantities fixed and overstates the cost of the current standard of living when substitution occurs; the Paasche index uses current quantities and requires data that are often unavailable; the Fisher index is their geometric mean and satisfies both reversal tests. Real income is nominal income divided by a price index.

A least squares line has slope $S_{xy}/S_{xx}$ and passes through the means, and the square of the correlation is the proportion of corrected variation explained. The elasticity of a linear demand function is $bp/Q$ and varies along the line. A forecast is conditional on the fitted relationship and is not valid outside the observed range of the predictor.

Sensitivity and specificity read down the columns of a two-by-two table and are properties of the test; predictive values read across the rows and depend on prevalence. The positive likelihood ratio is sensitivity divided by one minus specificity. A positive result multiplies the prior odds by that ratio. Relative risk, absolute risk reduction, number needed to treat and odds ratio answer different questions, and the absolute measures govern the decision.

The standard error of a proportion is the square root of $p(1-p)/n$, the interval is the estimate plus and minus 1.96 standard errors, and the sample size for a margin $E$ is $z^{2}p(1-p)/E^{2}$. Clustering inflates the variance by $1+(m-1)\rho$, so the effective sample size is smaller than the nominal one. A Likert mean is an average of codes, and a composite index depends on its normalisation, weights and aggregation rule.

Control limits are the centre line plus and minus three standard errors, and the false-alarm probability is 0.0027 per point, giving an average run length of 370. Capability is the specification width divided by six standard deviations, and the defect rate for a centred process is $2(1-\Phi(3C_p))$. A tolerance interval covers items, not a parameter, and needs a multiplier larger than the normal quantile. Reliability under a constant hazard is exponential, with mean life the reciprocal of the hazard, and the B10 life is $-\ln(0.9)/\lambda$.

### 5.2 Errors that cost marks, ranked by frequency

- Computing the percentage change and calling it the index, or the reverse.
- Reading a two-by-two table in the wrong direction, which reverses sensitivity and predictive value.
- Quoting a predictive value without the prevalence at which it was computed.
- Reporting a relative risk with no absolute measure.
- Using $n$ instead of $\sqrt{n}$ in a standard error.
- Reporting a standard deviation when a standard error was asked for.
- Treating control limits as specification limits.
- Estimating the process standard deviation from the period under investigation.
- Quoting $C_p$ when the process is off centre.
- Ignoring the design effect in a clustered survey.
- Extrapolating a calibration or regression line beyond its range.
- Reporting a mean of ordinal codes as an amount.
- Offering a conclusion with no uncertainty and no units.
- Running out of time before the interpretation marks, which are the cheapest marks in the paper.

### 5.3 Where each method stops working

A price index measures the cost of a basket and not welfare, so a rise in the index is compatible with a rise in welfare if quality improved, and a base-weighted index overstates the cost of a fixed standard of living when substitution is substantial. A regression line describes a conditional mean inside the observed range and supports no causal claim without a design that identifies the effect. A diagnostic table describes one threshold in one population, and moving the threshold trades sensitivity against specificity. A control chart detects departures from a baseline and cannot detect a problem that was present when the baseline was set. A capability ratio assumes approximate normality and a stable process, and a non-normal characteristic can produce a large nominal capability with a substantial real defect rate. A reliability model assumes a hazard form, and the exponential model is wrong for components in a wear-out phase. A composite index is a construction whose ranking depends on its indicators, ranges, weights and aggregation.

### 5.4 Ethical and reporting obligations, in exam form

A question may ask what should be reported alongside a result. The marks are for completeness and for naming the reason.

Report the design and the sampling frame, because they determine the population to which the conclusion extends. Report the sample size and the response rate, because a low response rate threatens representativeness more than it threatens precision. Report the interval and the confidence level, because a point estimate alone conceals the uncertainty. Report every outcome specified in advance, because selective reporting is how a literature becomes false. Report the number of comparisons, because twenty tests at the 5 per cent level produce at least one false positive with probability 0.64. Report harms as fully as benefits. Report conflicts of interest. Preserve the data so that the analysis can be reproduced. State one thing the study could not answer.

### 5.5 Revision checklist

Work through this list until every item can be done from memory, and mark each item only when it has been done without notes.

- Write the five definitions of population, variable, sample, inference and reliability, and give one applied example of each.
- Distinguish descriptive from inferential use in three sentences, one per field.
- Write the Laspeyres and Paasche formulas and state which overstates the cost of living and why.
- Compute an index from a table of four items in under six minutes, including both expenditure sums.
- Deflate a nominal income by an index and interpret the result in one sentence.
- Fit a least squares line from a table of six pairs and predict at a stated value.
- Compute the elasticity of a linear demand function at a stated price and classify it.
- Fill a two-by-two diagnostic table from sensitivity, specificity and prevalence, and compute both predictive values.
- State why predictive value falls when prevalence falls, using the odds form.
- Compute relative risk, absolute risk reduction, number needed to treat and odds ratio from trial counts.
- Compute a proportion, its standard error and a 95 per cent interval, and invert the formula for a required sample size.
- Apply a design effect and state the effective sample size.
- Compute a Likert mean and standard deviation from frequencies, and state the measurement caveat.
- Normalise three indicators and aggregate them geometrically.
- Compute control limits for a fraction and for a subgroup mean.
- Compute the false-alarm probability and the average run length, and justify the constant three.
- Compute a capability ratio, the standardised distance and the expected parts per million.
- Compute reliability at a stated time, the mean time to failure, and the B10 life.
- Explain the difference between a confidence interval and a tolerance interval in two sentences.
- Compute a Kaplan-Meier survival estimate from a small table with censoring.
- Name the confounder in an observational comparison and the design that would remove it.
- Distinguish statistical from practical significance with a numerical example.
- State the reporting obligations in six bullets.

### 5.6 Time strategy in the examination

The arithmetic in this topic is arithmetic, not insight, and it is where time disappears. The following allocation assumes a two-hour paper with a compulsory question and a choice of others.

Spend the first three minutes reading the whole paper and marking each question as quick, medium or long. The quick questions are the definitional parts, and they should be attempted first because they cannot overrun.

For any calculation worth ten marks, allow twelve minutes: two to write the given and required quantities, one to write the formula, six to compute, two for the interpretation, and one to check the units. If a calculation is not finished at twelve minutes, write the remaining formula steps in symbols, because method marks are awarded for a correct structure even when the arithmetic is incomplete, and move on.

Leave the final eight minutes for the interpretation sentences of every question attempted, since a paper with correct numbers and no interpretations typically loses a fifth of the available marks. Check three things on each answer in that final sweep: the direction of every two-by-two reading, the presence of a unit or a percentage sign, and the presence of an uncertainty statement wherever an inference was made.

If a question asks for a comment and the arithmetic has gone wrong, still write the comment conditionally. A sentence such as "an index of this size would imply that real income had fallen, because the price rise exceeds the nominal rise" earns the interpretation mark even when the index itself is wrong, provided the reasoning is visible.

### 5.7 Consolidation

This topic is the closing survey of the course, and it is examined as an exercise in recognition and execution rather than in derivation. The five fields draw on one structure: a quantity is formed as a ratio of a signal to a scale, its uncertainty is expressed as a standard error built from the amount of information available, and a decision is taken by comparing the quantity with the uncertainty. The index number, the elasticity, the defect fraction, the predictive value, the relative risk, the capability ratio and the hazard are all instances of that structure, and the standard error, the confidence interval, the control limit and the tolerance interval are all instances of the second.

A candidate who can move between the five vocabularies without losing the structure, who reads every table in the correct direction, and who never reports a number without its units and its uncertainty, will score well in this topic regardless of which field the question happens to come from.
