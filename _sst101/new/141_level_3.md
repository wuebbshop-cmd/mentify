## 1. Foundational Concepts, Definitions, and Axioms

### 1.1 What this topic is examined on

Questions on this topic are almost never computational in the ordinary sense. They ask you to look at a variable and say what kind of thing it is, then to say what may lawfully be done with it. The marks are awarded for two moves performed together: naming the classification, and justifying it by appealing to the defining property. A candidate who writes "ordinal" and stops has done half the work; a candidate who writes "ordinal, because the categories have a natural order but the distances between adjacent categories are not defined, so a mean would assume an equal spacing the instrument does not provide" has done all of it.

Three question families dominate. The first presents a list of variables and demands classification. The second presents a summary that has already been computed, such as a mean of rating codes, and demands that you identify and explain the error. The third presents a table of counts and demands a conditional percentage, an expected count, or a statement about association. Every one of these is answerable from a small set of definitions and two theorems, and the whole of this note is built to make those tools fast to deploy.

### 1.2 The definitions that carry marks

> **Definition (Quantitative data).** Quantitative data are measurements recorded on a naturally occurring numerical scale.

> **Definition (Qualitative data).** Qualitative data are measurements that cannot be measured on a natural numerical scale; they can only be classified into one of a group of categories.

> **Definition (Nominal scale).** Values are labels identifying categories, with the only admissible comparison being equality or inequality.

> **Definition (Ordinal scale).** Values are categories in a known order, where the magnitudes of differences between neighbouring categories are undefined.

> **Definition (Interval scale).** Values lie on an equally spaced numerical axis whose zero point is conventional, so that differences are meaningful and ratios are not.

> **Definition (Ratio scale).** Values lie on an equally spaced numerical axis with a true zero, so that both differences and ratios are meaningful.

> **Definition (Discrete variable).** A quantitative variable is discrete when no possible value lies between two adjacent possible values; such variables arise from counting.

> **Definition (Continuous variable).** A quantitative variable is continuous when a further possible value lies between any two of its values; such variables arise from measurement.

The four scale definitions are written so that each names the operation it licenses and the operation it forbids. That structure is deliberate: examiners award the mark for the forbidden operation as often as for the permitted one. "Interval: differences meaningful, ratios not" earns the mark; "interval: it is a number" does not.

### 1.3 The decision procedure, in the order it must be applied

Step 1. Ask whether the observation is a label or a magnitude. If a label, the variable is qualitative. If a magnitude, it is quantitative. Do not proceed until this is settled, because the remaining tests are different for the two branches.

Step 2. On the qualitative branch, ask whether the labels can be ranked. If they cannot, the scale is nominal. If they can, the scale is ordinal, and the examination answer must add that the step sizes are undefined.

Step 3. On the quantitative branch, apply the halfway test to decide discreteness. Compute the value midway between two adjacent possible values and ask whether the variable can take it. Impossible means discrete; possible means continuous.

Step 4. On the quantitative branch, ask whether zero means none of the quantity. If it does, the scale is ratio. If zero is merely a conventional mark, the scale is interval.

Step 5. Write the consequence. Every classification answer should end with the arithmetic the classification licenses or forbids, because that consequence is where the later marks in the question usually live.

### 1.4 Why the scale is the whole question

A summary statistic is a function of the data, and a scale is a declaration of which changed versions of the same data must leave every conclusion untouched. Those two ideas meet in a single principle, which is the engine behind every mark in this topic.

> **Principle (Admissibility).** A statistic is admissible for a scale when the statistic is equivariant under every admissible transformation of that scale: transforming the data must transform the statistic in the same way, and must not otherwise change it.

The principle is used in both directions. To defend a statistic, exhibit its equivariance. To attack a statistic, exhibit one admissible transformation under which it changes. A single counterexample is a complete disproof, which is why the shortest correct answers in this topic are often two lines and a number.

### 1.5 The admissible transformations, and the nesting they create

> **Theorem (Transformation classes).** The admissible transformations are: every one-to-one relabelling for a nominal scale; every strictly increasing transformation for an ordinal scale; every map $y = a + bx$ with $b > 0$ for an interval scale; every map $y = bx$ with $b > 0$ for a ratio scale.

The classes are nested: ratio inside interval inside ordinal inside nominal. Because a statistic that survives a wide class survives every narrower class, admissibility is monotone in the strength of the scale, and this monotonicity is itself a mark-earning observation: the mode is admissible everywhere, the median from ordinal upward, the mean from interval upward, and the coefficient of variation only at the top.

| Scale | Admissible transformation | Statistics admitted | Statistics forbidden |
|---|---|---|---|
| Nominal | Any one-to-one relabelling | Mode, frequencies, proportions, IQV | Median, mean, standard deviation |
| Ordinal | Any strictly increasing map | Median category, quartile categories, mode | Mean, standard deviation, coefficient of variation |
| Interval | Any $y = a + bx$, $b > 0$ | Mean, standard deviation, standard score, correlation | Coefficient of variation, geometric mean |
| Ratio | Any $y = bx$, $b > 0$ | All of the above plus coefficient of variation and geometric mean | None within the scale |

### 1.6 Discrete counting and continuous measurement

A discrete variable arises from counting units that cannot be divided: one child, one goal, one admission. A continuous variable arises from comparing a quantity with a standard unit, and the comparison can always in principle be refined. The examinable consequence is the shape of the frequency table. A discrete variable produces a table with one row per attainable value, and the values that do not occur are impossible rather than unobserved. A continuous variable produces a table with classes, and the classes must be described by boundaries rather than by the reported limits.

The recording precision must not be confused with the variable. A scale that reads to the nearest kilogram turns a continuous mass into a reported integer, and the reported integer is a class mark with boundaries half a kilogram either side. That is why a table of masses reported in whole kilograms carries boundaries at $.5$ positions even though no mass was ever recorded with a decimal.

### 1.7 Cross-classification

> **Definition (Contingency table).** A contingency table records the joint frequencies of two categorical variables, one in the rows and one in the columns, together with the row totals, the column totals, and the grand total.

> **Definition (Conditional distribution).** The conditional distribution of one variable within a category of the other is obtained by dividing each cell of that row or column by the relevant row or column total.

> **Definition (Marginal distribution).** The marginal distribution of one variable is obtained from its row or column totals, divided by the grand total.

> **Theorem (Expected counts).** If the two variables are independent, the expected count in cell $(i,j)$ is $E_{ij} = \frac{R_i C_j}{n}$.

The three readings must be distinguished before any percentage is written. A joint frequency answers "how many have both characteristics". A marginal percentage answers "how many have this characteristic, ignoring the other". A conditional percentage answers "among those with this characteristic, what fraction have the other". Read the question for the word "among" or "of those", because that word is the signal that a conditional percentage is required.

## 2. Theorems, Lemmas, and Analytical Properties

### 2.1 Affine equivariance of the mean

> **Theorem (Mean under change of origin and unit).** If $y_i = a + b x_i$ for all $i$, with $b > 0$, then $\bar{y} = a + b\bar{x}$.

This is the licence for the mean on interval data and on ratio data. It is also the standard examination demonstration that a mean temperature may be converted between Celsius and Fahrenheit, and it is the first line of any answer that defends averaging a temperature.

### 2.2 Failure of the mean under monotone recoding

> **Theorem (Mean is not ordinal-admissible).** There is a strictly increasing map $g$ and a data set for which the mean of $g\left(x_i\right)$ differs from $g$ applied to the mean of $x_i$.

The counterexample in Section 3.2 uses squaring, and squaring is the fastest weapon in the examination because it preserves order on positive data and visibly changes the mean. Report also that the median and the mode are unchanged by the same recoding, since that contrast is what demonstrates the asymmetry between order-based and magnitude-based statistics.

### 2.3 Equivariance of order statistics

> **Theorem (Median under increasing maps).** If $g$ is strictly increasing, then the median of the transformed data is $g$ applied to the median of the original data.

> **Lemma (Median of an even sample).** For $n = 2k$ the conventional median is $\frac{1}{2}\left(x_{(k)} + x_{(k+1)}\right)$, which requires the addition of two order statistics and hence equal spacing.

The lemma is a favourite trap. On an ordinal scale with an even number of observations, the correct report is the pair of central categories, or a statement that the median lies between two named categories, and not the arithmetic midpoint of two category codes.

### 2.4 Scaling of variance and standard deviation

> **Theorem (Variance under affine change).** If $y_i = a + b x_i$, then $s_y^{2} = b^{2}s_x^{2}$ and $s_y = \left| b \right| s_x$.

The origin vanishes because the variance is built from deviations, and the unit is squared because every deviation is multiplied by $b$. The vanishing of $a$ is the formal reason the standard deviation is legitimate on an interval scale while the coefficient of variation is not.

### 2.5 The coefficient of variation and its scale requirement

> **Theorem (Coefficient of variation).** For positive data, $v = \frac{s}{\bar{x}}$ satisfies $v_{bx} = v_x$ for $b > 0$, but in general $v_{a+bx} \ne v_x$ when $a \ne 0$.

The first identity makes $v$ the natural unit-free measure of relative spread, and therefore the correct answer whenever a question asks which of two variables measured in different units is more variable. The second identity is the reason $v$ must not be reported for a temperature in degrees Celsius, a calendar year, or an IQ score: all three have conventional origins, and moving the origin changes $v$ while changing nothing about the data.

### 2.6 Dispersion on a nominal scale

> **Definition (Index of qualitative variation).** For $k$ categories with frequencies summing to $n$,

$$
\mathrm{IQV} = \frac{k\left(n^{2} - \sum_{i=1}^{k} f_i^{2}\right)}{n^{2}\left(k - 1\right)}
$$

> **Theorem (Bounds).** $0 \le \mathrm{IQV} \le 1$, with $\mathrm{IQV} = 0$ exactly when one category contains every observation and $\mathrm{IQV} = 1$ exactly when the categories are equally frequent.

The index is the only defensible answer to "measure the spread of this nominal variable". It uses nothing but the category counts, so it is invariant under relabelling, and it is normalised so that its value can be compared between variables with different numbers of categories.

### 2.7 The class mark and the bound on grouping error

> **Theorem (Class mark identity).** For boundaries $L$ and $U$, the mark $m = \frac{L+U}{2}$ satisfies $m - L = U - m = \frac{h}{2}$.

> **Theorem (Grouping error bound).** If every observation in a class is replaced by the class mark, the grouped mean differs from the exact mean by at most $\frac{h}{2}$, where $h$ is the class width.

The bound is the examinable justification for the phrase "approximately" in any grouped summary. It also supplies a quick numerical answer to the standard question "state one reason why your answer is an approximation" — because each observation was replaced by a mark that can be up to half a class width away from it.

### 2.8 The chi-square statistic as an extension of the expected count

> **Definition (Chi-square statistic).** For a contingency table with $r$ rows and $c$ columns,

$$
\chi^{2} = \sum_{i=1}^{r}\sum_{j=1}^{c}\frac{\left(O_{ij} - E_{ij}\right)^{2}}{E_{ij}}
$$

> **Theorem (Degrees of freedom).** Under independence the statistic has $\left(r-1\right)\left(c-1\right)$ degrees of freedom.

The statistic aggregates the discrepancies between observed and expected counts, each standardised by the expected count so that large cells do not dominate merely by being large. It is included here because questions on cross-classification frequently end with "comment on the evidence of association", and the expected counts alone support that comment only qualitatively.

### 2.9 Summary table of high-yield results

| Result | Statement | Typical use |
|---|---|---|
| Affine mean | $\bar{y} = a + b\bar{x}$ | Converting a mean temperature or a mean mass |
| Order equivariance | Median maps through increasing $g$ | Justifying a median rating |
| Mean failure | Mean changes under a monotone recoding | Attacking a mean of codes |
| Variance scaling | $s_y^{2} = b^{2}s_x^{2}$ | Converting a standard deviation between units |
| CV invariance | $v_{bx} = v_x$ | Comparing variability across units |
| IQV bounds | $0 \le \mathrm{IQV} \le 1$ | Describing spread of nominal data |
| Grouping bound | Error $\le \frac{h}{2}$ | Justifying an approximate grouped mean |
| Expected count | $E_{ij} = \frac{R_i C_j}{n}$ | Detecting association in a table |

## 3. Formal Proofs, Derivations, and Methods

### 3.1 Proof of affine equivariance of the mean

Let $y_i = a + b x_i$. By linearity of summation,

$$
\bar{y} = \frac{1}{n}\sum_{i=1}^{n}\left(a + b x_i\right) = \frac{1}{n}\left(na + b\sum_{i=1}^{n}x_i\right) = a + b\bar{x}
$$

The proof uses only the two facts that a constant summed $n$ times gives $na$ and that a constant factor may be pulled through a sum. Both are worth quoting by name in an examination, because the names are what examiners look for in a proof mark.

### 3.2 Proof that the mean is not admissible on an ordinal scale

Take observations $1$, $2$, $3$ and the strictly increasing map $g(x) = x^{2}$. The original mean is

$$
\bar{x} = \frac{1 + 2 + 3}{3} = 2
$$

and the image of that mean is $g(2) = 4$. The transformed observations are $1$, $4$, $9$, whose mean is

$$
\bar{y} = \frac{1 + 4 + 9}{3} = \frac{14}{3} \approx 4.67
$$

Since $4.67 \ne 4$, the mean is not equivariant under this admissible recoding. The median of the original data is $2$ and the median of the transformed data is $4 = g(2)$, so the median passes the same test that the mean fails. The contrast is the answer.

### 3.3 Proof of median equivariance and the even-sample caveat

Let $x_{(1)} \le \dots \le x_{(n)}$ be the ordered observations and let $g$ be strictly increasing, so that $g\left(x_{(1)}\right) \le \dots \le g\left(x_{(n)}\right)$. For $n = 2k+1$ the median is $x_{(k+1)}$, and the median of the transformed data is the $\left(k+1\right)$-th order statistic of the transformed sample, which is $g\left(x_{(k+1)}\right)$. For $n = 2k$ the conventional median is the average of $x_{(k)}$ and $x_{(k+1)}$, and

$$
\frac{g\left(x_{(k)}\right) + g\left(x_{(k+1)}\right)}{2} \ne g\left(\frac{x_{(k)} + x_{(k+1)}}{2}\right)
$$

in general, because averaging does not commute with a nonlinear map. The caveat is therefore structural rather than pedantic.

### 3.4 Proof of the variance scaling law

With $y_i = a + b x_i$ the deviation of the $i$-th observation from its own mean is

$$
y_i - \bar{y} = \left(a + b x_i\right) - \left(a + b\bar{x}\right) = b\left(x_i - \bar{x}\right)
$$

Squaring and averaging gives

$$
s_y^{2} = \frac{1}{n}\sum_{i=1}^{n}b^{2}\left(x_i - \bar{x}\right)^{2} = b^{2}s_x^{2}
$$

and taking square roots gives $s_y = \left| b \right| s_x$. The argument shows simultaneously that the variance is blind to the origin and quadratic in the unit, and both facts are routinely worth a mark each.

### 3.5 Proof that the coefficient of variation fails on interval data

Applying the two preceding results,

$$
v_y = \frac{s_y}{\bar{y}} = \frac{b s_x}{a + b\bar{x}}
$$

When $a = 0$ the numerator and denominator each carry the factor $b$ and $v_y = v_x$. When $a \ne 0$ the factor cancels from the numerator only, and the value changes. Numerically, a sample with mean $20$ and standard deviation $2$ has $v = 0.1$; the same sample reported as $y = x + 273$ has mean $293$, standard deviation $2$, and $v \approx 0.0068$. The same data now appear fifteen times less variable.

### 3.6 Derivation of the index of qualitative variation

The quantity $\sum f_i^{2}$ measures concentration: it is largest when one category holds everything, taking the value $n^{2}$, and smallest when the categories are equal, taking the value $\frac{n^{2}}{k}$. Hence $n^{2} - \sum f_i^{2}$ measures departure from concentration and ranges from $0$ to $n^{2} - \frac{n^{2}}{k}$. Dividing by that maximum and multiplying by nothing further would give a number in the unit interval; the standard form multiplies by $k$ and divides by $n^{2}\left(k-1\right)$, which is the same normalisation written in a single fraction. Both bounds in Section 2.6 follow at once.

### 3.7 Method: the marking template for a classification answer

Step 1. Name the family: qualitative or quantitative. One mark.

Step 2. Name the sub-type or scale: nominal, ordinal, discrete, continuous, interval, or ratio. One mark.

Step 3. Give the defining property that settles it, phrased as a test rather than as an example. One mark.

Step 4. State the arithmetic consequence: which average and which measure of spread are available, or which are forbidden and why. One mark.

Step 5. If the variable could plausibly be classified two ways, name the rival classification and say why it fails. This is where the discriminating mark usually sits.

### 3.8 Method: the marking template for a grouped continuous calculation

Step 1. State that the variable is continuous, and that grouping is therefore necessary. One mark.

Step 2. Write the boundaries, derived from the stated limits and the recording precision. One mark.

Step 3. Compute the class width from boundaries, never from limits. One mark.

Step 4. Compute the class marks as midpoints of boundaries. One mark.

Step 5. Form the weighted sums $\sum f_j m_j$ and $\sum f_j m_j^{2}$, showing the arithmetic. Two marks.

Step 6. Compute the mean and the standard deviation, stating formulae before substituting. Two marks.

Step 7. Comment that the results are approximations bounded by half a class width. One mark.

### 3.9 Method: the marking template for a contingency table question

Step 1. Reproduce the table with both margins and check that the row totals and the column totals both equal $n$. One mark.

Step 2. Decide whether the question demands a joint, a marginal, or a conditional figure, and state the denominator explicitly. One mark.

Step 3. Compute the percentages to one decimal place and check that they sum to $100$ within the relevant margin. One mark.

Step 4. If association is at issue, compute the expected count for the cell named in the question and compare it with the observed count. One mark.

Step 5. Conclude in the language of the variables, not in the language of the arithmetic. One mark.

## 4. Representative Worked Examples and Solutions

### 4.1 Problem: classify six variables and defend each answer

A transport study records, for each commuter: mode of transport; journey purpose graded as essential, desirable, or discretionary; distance travelled in kilometres; number of interchanges; fare paid; and the year in which the commuter's vehicle was registered. Classify each variable by scale, state the averages available, and identify the one variable where a careless candidate would err.

### 4.2 Solution: model answer with marking points

Step 1. Mode of transport. The values are labels such as bus, train, and taxi, with no order, so the scale is nominal. The available summaries are the frequencies, the proportions, and the mode. **Marking point:** the word nominal plus the reason "no natural order".

Step 2. Journey purpose. The three grades are ordered, because essential outranks desirable and desirable outranks discretionary, but the gaps between grades are undefined. The scale is ordinal, and the available summaries are the median grade, reported as a category, the modal grade, and the cumulative proportions. **Marking point:** ordinal plus the explicit denial of equal spacing.

Step 3. Distance travelled. Distance is measured, has a true zero, and admits intermediate values, so the scale is ratio and the variable is continuous. The mean, standard deviation, coefficient of variation, and geometric mean are all available. **Marking point:** ratio plus a named consequence such as the coefficient of variation.

Step 4. Number of interchanges. Interchanges are counted in whole units, so the variable is discrete on a ratio scale. The mean and standard deviation are available. **Marking point:** discrete, justified by counting rather than by the appearance of the digits.

Step 5. Fare paid. A fare has a true zero and equal spacing in the currency unit, so the scale is ratio. The mean and coefficient of variation are available; the coefficient of variation is often the interesting summary here because it compares relative variability across fare bands. **Marking point:** true zero named as the discriminator.

Step 6. Year of vehicle registration. Years have equal spacing but a conventional origin, so the scale is interval. Differences of years are meaningful, and the mean year of a fleet is a legitimate summary, but a ratio of two years is not. **Marking point:** interval identified by the conventional zero.

Step 7. Identify the trap. The careless candidate treats the year of registration as ratio because it is written as a large whole number, and then reports that one vehicle is "twice as old" by dividing two calendar years. The correct statement is a difference of years, because only differences survive a change of the calendar origin.

Step 8. Summarise.

| Variable | Scale | Available average |
|---|---|---|
| Mode of transport | Nominal | Mode |
| Journey purpose | Ordinal | Median category |
| Distance travelled | Ratio, continuous | Mean or geometric mean |
| Number of interchanges | Ratio, discrete | Mean |
| Fare paid | Ratio | Mean or geometric mean |
| Year of registration | Interval | Mean |

### 4.3 Problem: a grouped continuous summary examined in full

The masses of $100$ students, recorded to the nearest kilogram, are grouped as $50$ to $52$ with $5$ students, $53$ to $55$ with $18$, $56$ to $58$ with $42$, $59$ to $61$ with $27$, and $62$ to $64$ with $8$. Compute the mean mass, the standard deviation, and the coefficient of variation, and state why each figure is approximate.

### 4.4 Solution: model answer with marking points

Step 1. Identify the variable. Mass is a continuous ratio measurement, because a mass can take any value in an interval and zero mass means no mass. Grouping is therefore necessary, and each class mark will stand for its class.

Step 2. Write the boundaries. Masses are recorded to the nearest kilogram, so each boundary lies half a kilogram beyond a stated limit:

$$
49.5, \quad 52.5, \quad 55.5, \quad 58.5, \quad 61.5, \quad 64.5
$$

**Marking point:** boundaries, not limits, and the justification from recording precision.

Step 3. Compute the class width from boundaries:

$$
h = 52.5 - 49.5 = 3
$$

and verify it against a second pair, $55.5 - 52.5 = 3$, which confirms equal widths. **Marking point:** the subtraction performed on boundaries.

Step 4. Compute the class marks as midpoints:

$$
51, \quad 54, \quad 57, \quad 60, \quad 63
$$

Step 5. Form the frequency-weighted total of marks:

$$
\sum_{j=1}^{5} f_j m_j = 5(51) + 18(54) + 42(57) + 27(60) + 8(63)
$$

$$
\sum_{j=1}^{5} f_j m_j = 255 + 972 + 2394 + 1620 + 504 = 5745
$$

Step 6. Divide by the number of students:

$$
\bar{x} = \frac{5745}{100} = 57.45
$$

**Marking point:** the divisor is the total frequency, not the number of classes.

Step 7. Form the frequency-weighted total of squared marks:

$$
\sum_{j=1}^{5} f_j m_j^{2} = 5(2601) + 18(2916) + 42(3249) + 27(3600) + 8(3969) = 330903
$$

Step 8. Apply the shortcut identity $s^{2} = \frac{1}{n}\sum f_j m_j^{2} - \bar{x}^{2}$:

$$
s^{2} = \frac{330903}{100} - \left(57.45\right)^{2} = 3309.03 - 3300.5025 = 8.5275
$$

Step 9. Take the square root:

$$
s = \sqrt{8.5275} \approx 2.92
$$

**Marking point:** the standard deviation is in kilograms, and its unit must be stated.

Step 10. Compute the coefficient of variation:

$$
v = \frac{s}{\bar{x}} = \frac{2.92}{57.45} \approx 0.051
$$

that is about $5.1$ per cent. **Marking point:** the coefficient is available only because mass is ratio-scaled; the same computation for a temperature in degrees Celsius would be inadmissible.

Step 11. State the approximation. Because each student was represented by a mark that can be up to half a class width, that is $1.5$ kilograms, from her true mass, every figure is an approximation, and the mean is within $1.5$ kilograms of the exact value computed from the raw masses.

Step 12. Interpret. A mean of about $57.5$ kilograms and a standard deviation of about $2.9$ kilograms describe a compact distribution, and the coefficient of about $5.1$ per cent confirms that the variation is small relative to the level.

### 4.5 Problem: an ordinal scale, a coding artefact, and a spread measure

Fifteen respondents rate a service from $1$ for very poor to $5$ for very good, with frequencies $2$, $3$, $5$, $4$, and $1$. A report states that the mean satisfaction is $2.93$ out of $5$. Assess the report, compute the admissible summaries, and measure the spread.

### 4.6 Solution: model answer with marking points

Step 1. Identify the scale. The five labels are ordered but the gaps between them are not defined, because the words carry no metric. The scale is ordinal, and $n = 15$. **Marking point:** ordinal, with the reason stated.

Step 2. Reject the mean with a reason. A mean adds the codes, and addition presumes that each step between adjacent categories is worth the same. On an ordinal scale that presumption is unsupported, so the reported figure of $2.93$ describes the coding convention rather than the satisfaction. **Marking point:** the rejection is justified by the addition of unequal steps, not by the word "ordinal" alone.

Step 3. Demonstrate the artefact. Recode the five categories as $0$, $1$, $2$, $4$, $8$, a strictly increasing assignment consistent with an ordinal scale. The mean becomes

$$
\frac{2(0) + 3(1) + 5(2) + 4(4) + 1(8)}{15} = \frac{37}{15} \approx 2.47
$$

while the original coding gave

$$
\frac{2(1) + 3(2) + 5(3) + 4(4) + 1(5)}{15} = \frac{44}{15} \approx 2.93
$$

**Marking point:** an admissible recoding that changes the mean is a complete refutation.

Step 4. Compute the median. The cumulative frequencies are $2$, $5$, $10$, $14$, $15$, so the eighth ordered observation lies in the third category, which contains positions six to ten. The median is the third category. **Marking point:** the median is reported as a category.

Step 5. Compute the mode. The largest frequency is $5$, attached to the third category, so the modal rating is the third category.

Step 6. Compute the index of qualitative variation with $k = 5$, $n = 15$, and $\sum f_i^{2} = 4 + 9 + 25 + 16 + 1 = 55$:

$$
\mathrm{IQV} = \frac{5\left(225 - 55\right)}{225 \times 4} = \frac{850}{900} \approx 0.94
$$

**Marking point:** a spread measure that is admissible on a nominal or ordinal scale, computed from the counts.

Step 7. Conclude. The defensible report is that the median and modal rating are both the middle category of five, and that opinions are spread almost uniformly across the scale, with an index of about $0.94$ out of a possible $1$. The figure of $2.93$ should be withdrawn, or retained only with an explicit statement that the categories were assumed equally spaced and that the median is the primary summary.

### 4.7 Problem: cross-classification and a comment on association

A supermarket surveys $120$ customers, recording payment method and customer category, with these counts: card used by $8$ new, $22$ returning, and $26$ loyal customers; cash by $14$ new, $12$ returning, and $6$ loyal; mobile by $6$ new, $14$ returning, and $12$ loyal. Test the claim that payment method is unrelated to customer category.

### 4.8 Solution: model answer with marking points

Step 1. Present the table with both margins and verify them.

| Payment method | New | Returning | Loyal | Total |
|---|---|---|---|---|
| Card | 8 | 22 | 26 | 56 |
| Cash | 14 | 12 | 6 | 32 |
| Mobile | 6 | 14 | 12 | 32 |
| Total | 28 | 48 | 44 | 120 |

Both sets of margins sum to $120$, so the table is internally consistent. **Marking point:** the margin check.

Step 2. Choose the right comparison. The claim is about the pattern of payment within each customer category, so the conditional distribution by column is required, with the column totals as denominators.

Step 3. Compute the conditional percentages for new customers:

$$
\frac{8}{28} \approx 28.6\%, \qquad \frac{14}{28} = 50.0\%, \qquad \frac{6}{28} \approx 21.4\%
$$

Step 4. Compute the same for loyal customers:

$$
\frac{26}{44} \approx 59.1\%, \qquad \frac{6}{44} \approx 13.6\%, \qquad \frac{12}{44} \approx 27.3\%
$$

**Marking point:** the denominators are the column totals, and each set sums to $100$ per cent.

Step 5. Compute the expected counts under independence using $E_{ij} = \frac{R_i C_j}{n}$. For card among new customers,

$$
E_{11} = \frac{56 \times 28}{120} \approx 13.07
$$

whereas the observed count is $8$. For cash among new customers,

$$
E_{21} = \frac{32 \times 28}{120} \approx 7.47
$$

whereas the observed count is $14$. **Marking point:** the expected count is computed from margins and the grand total, not from the observed cell.

Step 6. Aggregate the discrepancies:

$$
\chi^{2} = \sum_{i=1}^{3}\sum_{j=1}^{3}\frac{\left(O_{ij} - E_{ij}\right)^{2}}{E_{ij}} \approx 12.40
$$

with $\left(3-1\right)\left(3-1\right) = 4$ degrees of freedom.

Step 7. Interpret. The critical value at the five per cent level with four degrees of freedom is $9.488$, and $12.40$ exceeds it, so the hypothesis of independence is rejected. Cash payment is over-represented among new customers and under-represented among loyal ones, while card payment shows the reverse pattern.

Step 8. State the conclusion in the language of the problem. Payment method and customer category are associated: loyalty is accompanied by a shift away from cash and towards card and mobile payment. **Marking point:** the conclusion names the variables and the direction of the association rather than reciting the statistic.

## 5. Mathematical Extensions, Limits, and Common Errors

### 5.1 The traps that recur, and the sentence that defuses each

The first trap is the numerical code. Any categorical variable can be given integer codes, and the codes will average to something. The defusing sentence is that a one-to-one relabelling leaves the data unchanged while changing the mean, so the mean is not a property of the data.

The second trap is the ordinal rating. Long rating scales tempt candidates into reporting means, standard deviations, and even confidence intervals. The defusing sentence is that an ordinal scale admits every strictly increasing recoding, and the mean is not equivariant under all of them, as a counterexample with a nonlinear recoding shows. The median is the primary summary and the index of qualitative variation is the admissible measure of spread.

The third trap is the continuous variable recorded in whole numbers. Age in completed years, price in whole currency units, and height in whole centimetres all look discrete. The defusing sentence is that the halfway test is applied to the variable rather than to the recording, and that recording at precision $h$ merely converts the value into a class mark with boundaries at half a unit either side.

The fourth trap is the interval variable treated as ratio. A claim that one day was twice as hot as another, or that one calendar year is twice another, fails as soon as the origin is moved, and the Celsius to Fahrenheit conversion is the standard demonstration. The defusing sentence is that only differences are invariant when the zero is conventional.

The fifth trap is the coefficient of variation computed on interval data. It is the only trap that arises from using a legitimate formula in an illegitimate place, and it is defused by the observation that the coefficient is invariant under changes of unit but not under changes of origin.

The sixth trap is the class width computed from limits rather than boundaries. For classes written $50$ to $52$ and $53$ to $55$, the width is $3$ and not $2$, because the true span of the first class runs from $49.5$ to $52.5$. The trap costs marks in every subsequent line of a grouped calculation.

The seventh trap is the marginal percentage offered where a conditional percentage was demanded. The defusing sentence names the denominator explicitly: among new customers, not among all customers.

The eighth trap is the median of an even sample on an ordinal scale, reported as the arithmetic average of two category codes. The defusing sentence is that averaging requires equal spacing, so the central categories are reported as a pair.

### 5.2 Limits of the whole scheme

The four-scale model is a classification of instruments, not of the world. Many variables admit more than one defensible classification depending on how the instrument was built, and the examination answer should state the classification that the description in the question supports, together with the assumption that makes it defensible. A five-point scale can be ordinal if it is a set of words and approximately interval if it is a marked line with equal spacings, and the difference is a fact about the instrument rather than about the respondents.

A second limit is that grouping destroys information that no arithmetic can restore. The grouped mean and standard deviation are computed as though every observation sat on its class mark, so within-class variation disappears, and the reported spread understates the true spread when the classes are wide relative to the variation. The error bound of half a class width applies to the mean, but the understatement of the standard deviation is not bounded by so simple an expression, and the practical safeguard is to keep the class width small relative to the standard deviation.

A third limit is that cross-classification by two variables cannot establish causation. An association in a contingency table may arise because a third variable drives both, and collapsing a table over that third variable can even reverse the direction of the association, which is Simpson's paradox. The classical illustration has two treatments and two severity strata in which one treatment is at least as good in each stratum but worse overall, because it was given disproportionately to the severe cases. The lesson is that conditionals must be reported alongside marginals.

### 5.3 A revision checklist

1. Can you state all four scale definitions with the operation each forbids as well as the operation it permits?
2. Can you produce, from memory, a strictly increasing recoding that changes the mean of a small data set while leaving the median and mode unchanged?
3. Can you state the affine equivariance of the mean and prove it in three lines?
4. Can you state and prove $s_{a+bx}^{2} = b^{2}s_x^{2}$, and say which term of the transformation disappears and why?
5. Can you explain in one sentence why the coefficient of variation requires a ratio scale?
6. Can you compute the index of qualitative variation and say what its endpoints mean?
7. Can you derive class boundaries from a stated recording precision and compute class width from boundaries only?
8. Can you compute a grouped mean and standard deviation from class marks, and state the half-class-width bound on the mean?
9. Can you compute conditional percentages in both directions in a contingency table and check that each set sums to $100$?
10. Can you compute an expected count from the margins and say what a large discrepancy implies?
11. Can you name the correct graph for each scale, and explain why touching bars belong only to a continuous axis?
12. Can you list the eight traps of Section 5.1 and give the defusing sentence for each?

### 5.4 A time strategy for the examination

Allocate the first minute of any question on this topic to classification, because every later mark depends on it. For a list of variables, allow about forty seconds each: ten seconds to decide the family, ten to decide the sub-type, and twenty to write the justification and the arithmetic consequence. The justification costs more time than the label and earns more marks, so never trade it for extra labels.

For a grouped continuous calculation, budget two minutes for boundaries, width, and marks, three minutes for the two weighted sums, one minute for the mean, one minute for the standard deviation, and one minute for the comment on approximation. Write the formula before substituting, because a formula earns a method mark even when the arithmetic slips.

For a contingency table, budget one minute for the margins and their check, two minutes for the conditional percentages in the direction the question asks, two minutes for the expected counts, and one minute for the conclusion. If time is short, the conditional percentages and the conclusion carry more marks than the chi-square statistic, and the conclusion should be written even when the statistic has not been completed.

Leave the final two minutes for a consistency pass: check that every frequency total equals $n$, that every percentage set sums to $100$, that every standard deviation carries a unit, and that no mean has been reported for a nominal or ordinal variable.
