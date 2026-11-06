## 1. Foundational Concepts, Definitions, and Axioms

### 1.1 What an examination actually rewards

A hypothesis-testing question is marked not on the final word but on the visible chain of reasoning. The marks are attached to identifiable stages: the hypotheses written in symbols, the standard error computed correctly, the statistic evaluated, the critical value quoted with the right number of tails and degrees of freedom, the decision stated, and the interpretation written in the language of the problem. A candidate who reaches the correct verdict through a correct chain earns everything; a candidate who guesses the verdict earns almost nothing.

This section therefore builds the answer template first and the theory second, so that every later result can be dropped into a fixed slot. The template has six slots, and almost every question in this topic is worth between five and twelve marks because it contains between five and twelve identifiable steps.

The logic behind the template is a probabilistic version of proof by contradiction. The null hypothesis is assumed, a consequence about the test statistic is deduced, and the consequence is found to be improbable. In mathematics the consequence would be impossible and the assumption would fall outright; in statistics the consequence is merely improbable, so the assumption is abandoned by a decision rule with a known error rate. Every mark scheme rewards that structure because every mark scheme rewards visible reasoning.

### 1.2 Writing the hypotheses

The hypotheses are worth a mark each in most marking schemes, and they are the cheapest marks in the topic. Three rules cover every case.

Rule one: name the parameter in symbols. For a mean use $\mu$, for a proportion use $p$, for a variance use $\sigma^{2}$, and say in words what the symbol refers to.

Rule two: put the equality in the null. The null always contains an equals sign, written $=$, $\le$ or $\ge$. It never contains a strict inequality.

Rule three: let the wording decide the alternative. "Differs", "has changed", "is not equal to" produce a two-sided alternative. "Exceeds", "is greater than", "has increased" produce an upper one-sided alternative. "Is less than", "has decreased", "has fallen below" produce a lower one-sided alternative.

The three standard forms each carry their own critical value at the $5\%$ level: $1.96$ in both tails for the two-sided alternative, $1.645$ in the upper tail for the upper one-sided alternative, and $-1.645$ in the lower tail for the lower one-sided alternative.

| Wording in the question | Null | Alternative | Critical value at $5\%$ |
| --- | --- | --- | --- |
| "differs from", "has changed" | $H_0: \theta = \theta_0$ | $H_1: \theta \ne \theta_0$ | $1.96$ in both tails |
| "exceeds", "is greater than" | $H_0: \theta = \theta_0$ | $H_1: \theta > \theta_0$ | $1.645$ upper only |
| "is less than", "has fallen" | $H_0: \theta = \theta_0$ | $H_1: \theta < \theta_0$ | $-1.645$ lower only |

A frequent loss of marks arises from writing the hypotheses about the sample rather than the population. The statement $\bar{x} \ne 100$ is not a hypothesis; it is a fact about the data. The hypothesis is a statement about $\mu$, and the sample mean is only the evidence.

### 1.3 The four test statistics on one page

Every question in this topic uses one of four statistics. The table gives the formula, the reference distribution, the degrees of freedom and the condition that selects it.

| Situation | Statistic | Reference distribution | Degrees of freedom | Selecting condition |
| --- | --- | --- | --- | --- |
| Mean, $\sigma$ known | $\left(\bar{x} - \mu_0\right)/\left(\sigma/\sqrt{n}\right)$ | standard normal | none | question states the population standard deviation |
| Mean, $\sigma$ estimated | $\left(\bar{x} - \mu_0\right)/\left(s/\sqrt{n}\right)$ | Student t | $n - 1$ | question gives the sample standard deviation |
| Paired difference | $\bar{d}/\left(s_d/\sqrt{n}\right)$ | Student t | $n - 1$ | same subjects measured twice |
| Two independent means | $\left(\bar{x}_1 - \bar{x}_2\right)/\text{SE}$ | Student t | $n_1 + n_2 - 2$ | two separate groups, equal variances |
| Single proportion | $\left(\hat{p} - p_0\right)/\sqrt{p_0\left(1 - p_0\right)/n}$ | standard normal | none | counts of a category out of a total |
| Goodness of fit | $\sum \left(O - E\right)^{2}/E$ | chi-square | $k - 1 - m$ | one classification compared with a theory |
| Independence | $\sum \sum \left(O - E\right)^{2}/E$ | chi-square | $\left(r - 1\right)\left(c - 1\right)$ | two classifications cross-tabulated |
| Two variances | $s_1^{2}/s_2^{2}$ | F | $n_1 - 1$, $n_2 - 1$ | question asks about variability |

The selecting condition in the last column is what the examiner writes into the wording. Learning to read the wording backwards, from the phrasing to the row of the table, is the single most valuable exam skill in this topic.

### 1.4 Critical values worth memorising

Tables are supplied in most examinations, but fluency with the common values saves minutes and prevents tail errors.

| Quantity | Level $10\%$ | Level $5\%$ | Level $1\%$ |
| --- | --- | --- | --- |
| Two-sided normal | $1.645$ | $1.96$ | $2.576$ |
| One-sided normal | $1.282$ | $1.645$ | $2.326$ |
| Two-sided $t$, $8$ df | $1.860$ | $2.306$ | $3.355$ |
| Two-sided $t$, $15$ df | $1.753$ | $2.131$ | $2.947$ |
| Upper chi-square, $1$ df | $2.706$ | $3.841$ | $6.635$ |
| Upper chi-square, $2$ df | $4.605$ | $5.991$ | $9.210$ |
| Upper chi-square, $5$ df | $9.236$ | $11.070$ | $15.086$ |

Two habits around tables prevent most errors. First, identify the number of tails before opening the table, because the two-sided $5\%$ value is the one-sided $2.5\%$ value. Second, identify the degrees of freedom before opening the table, because the t and chi-square tables are indexed by them and the F table by two of them.

### 1.5 The p-value and the decision rule

The p-value is the probability of a result at least as extreme as the observed one, computed on the assumption that the null hypothesis is true.

> **Definition (p-value).** For a test statistic $T$ with observed value $t_{\text{obs}}$, the p-value is $\text{P}_{H_0}\left(T \text{ is at least as extreme as } t_{\text{obs}}\right)$, where "at least as extreme" follows the direction or directions of the alternative.

The decision rule is $p \le \alpha$ implies rejection and $p > \alpha$ implies no rejection. A p-value quoted without a level is incomplete, and a p-value quoted with the wrong number of tails is wrong by a factor of two.

The two decision routes are listed below with the exact arithmetic that links them.

| Route | What is computed | Rejection condition | Where the level enters |
| --- | --- | --- | --- |
| Critical value | the statistic and the boundary | statistic beyond the boundary | fixed before the data are seen |
| p-value | the tail area beyond the statistic | $p \le \alpha$ | applied after the computation |

The two routes always agree. If a candidate reports rejection from one and non-rejection from the other, an arithmetic slip has occurred, and the slip is nearly always in the standard error.

### 1.6 The four outcomes of a decision

Every test ends in one of four combinations of reality and verdict, and the two-by-two arrangement is worth writing down because examination questions frequently ask for it.

| | $H_0$ true | $H_0$ false |
| --- | --- | --- |
| Reject $H_0$ | Type I error, probability $\alpha$ | correct decision, probability $1 - \beta$ |
| Do not reject $H_0$ | correct decision, probability $1 - \alpha$ | Type II error, probability $\beta$ |

The significance level is the probability of the top-left cell, and the power is the probability of the top-right cell. Lowering $\alpha$ moves probability mass from the top-left cell to the bottom-right cell, which is why power falls unless the sample grows.

Two conventions matter for marks. The phrase "accept $H_0$" is normally penalised, because a test never establishes a null hypothesis; the accepted phrasing is "do not reject $H_0$" or "there is insufficient evidence to reject $H_0$". The phrase "the probability that $H_0$ is true" is always penalised when attached to a p-value.

### 1.7 The six-step answer template

The template below is the one used in every model solution in Section 4. Writing the step labels into the answer costs a line and earns method marks even when arithmetic slips.

Step 1. Define the parameter and state $H_0$ and $H_1$ in symbols, with a sentence of interpretation.

Step 2. Name the test and the reference distribution, and state the conditions that justify the choice.

Step 3. Compute the standard error, showing the substitution.

Step 4. Compute the test statistic, showing the substitution.

Step 5. Obtain the critical value or the p-value, and compare.

Step 6. State the decision and interpret it in context, naming the population, the direction and the level.

### 1.8 Notation

| Symbol | Meaning | Typical figure |
| --- | --- | --- |
| $\alpha$ | significance level | $0.05$ |
| $\beta$ | probability of a Type II error | $0.20$ |
| $1 - \beta$ | power | $0.80$ |
| $z_{\alpha/2}$ | two-sided normal critical value | $1.96$ |
| $t_{\alpha/2, \nu}$ | two-sided t critical value | $2.131$ at $15$ df |
| $\chi^{2}_{\alpha, \nu}$ | upper chi-square critical value | $5.991$ at $2$ df |
| $p$ | p-value | $0.024$ |
| $\hat{p}$ | sample proportion | $0.58$ |

## 2. Theorems, Lemmas, and Analytical Properties

### 2.1 Question patterns and the test each one demands

Examination questions reuse a small number of openings, and each opening signals a test. The recognition table that follows converts wording into method in a single glance.

| Opening in the question | Test signalled | Reason |
| --- | --- | --- |
| "A random sample of 40 items has mean ... the population standard deviation is known to be ..." | one-sample z | $\sigma$ is supplied, so no t correction is needed |
| "The sample standard deviation was ..." | one-sample t | $\sigma$ must be estimated, so t is required |
| "Ten patients were measured before and after treatment" | paired t | the same subjects appear twice, so differences are analysed |
| "Two independent samples from two machines" | two-sample t | separate groups, so a difference of means is analysed |
| "Out of 250 customers, 145 agreed" | one proportion z | a count out of a total |
| "Do the observed frequencies fit the claimed distribution?" | chi-square goodness of fit | one classification against a theoretical set of probabilities |
| "Is there an association between region and preference?" | chi-square independence | two classifications in a cross-table |
| "Is machine A more consistent than machine B?" | F test for variances | consistency is variability, not the mean |

The last row is the most frequently missed. A question about consistency, reliability, precision or spread concerns variances, and no amount of averaging will answer it.

### 2.2 The alternative fixes the rejection region

> **Lemma (Direction follows the alternative).** For a statistic that increases with the estimate, the alternative $H_1: \theta > \theta_0$ puts the whole rejection region in the upper tail, $H_1: \theta < \theta_0$ puts it in the lower tail, and $H_1: \theta \ne \theta_0$ splits $\alpha$ equally between the two tails.

At the $5\%$ level the three critical values are therefore $1.645$, $-1.645$ and $\pm 1.96$. The two-sided value is larger because it must guard two doors with the same total false-alarm allowance.

Two consequences are examinable. A result that is significant in a one-sided test need not be significant in the corresponding two-sided test; the boundary band between $1.645$ and $1.96$ is exactly where the verdict changes. And a one-sided alternative may never be chosen after inspecting the sign of the sample mean, because the effective error rate then doubles.

### 2.3 Duality between the interval and the test

> **Theorem (Duality).** A two-sided test of $H_0: \theta = \theta_0$ at level $\alpha$ rejects exactly when $\theta_0$ lies outside the $100\left(1 - \alpha\right)\%$ confidence interval for $\theta$.

The mechanism is a single inequality: the test rejects when

$$
\left| \frac{\hat{\theta} - \theta_0}{\text{SE}} \right| > c,
$$

and the interval collects the values satisfying the reverse inequality. The two statements are negations, so they cannot disagree.

Duality earns marks in three exam situations. It gives a free check on a computed test, because the interval is easy to compute and either contains the null value or does not. It answers questions of the form "use your interval to test the hypothesis", where the expected answer is one sentence rather than a second full computation. And it explains the apparent paradox in which a $99\%$ interval contains the null value while a $5\%$ test rejects, since the two statements are made at different levels.

### 2.4 Degrees of freedom, and why they are marked

The degrees of freedom are worth a mark on their own, and the rules are short.

For a one-sample t test, $\nu = n - 1$. For a paired design, $\nu = n - 1$ where $n$ is the number of pairs. For a two-sample pooled t test, $\nu = n_1 + n_2 - 2$. For a chi-square goodness-of-fit test, $\nu = k - 1$ less one for each parameter estimated from the data. For a chi-square independence test, $\nu = \left(r - 1\right)\left(c - 1\right)$. For an F test, the two degrees of freedom are $n_1 - 1$ and $n_2 - 1$.

The contingency-table rule deserves its one-line justification, which also earns credit: the cell probabilities must reproduce the row and column totals, so $r - 1$ row constraints and $c - 1$ column constraints are imposed, and the product counts the free cells that remain.

### 2.5 Choosing between z and t without hesitation

> **Rule (z or t).** Use z when the population standard deviation is known and either the population is normal or $n$ is large. Use t when the population standard deviation is estimated from the sample and the population is normal or nearly so.

The three situations that cause hesitation are worth settling in advance.

If the question gives a sample standard deviation and a large sample, either test gives nearly the same answer, and the t test is the safe choice because it is exact under normality.

If the question gives the population standard deviation but the sample is small and the population is clearly non-normal, neither test is exact and the answer should say so, while still applying the z test as the conventional approximation.

If the question gives a variance rather than a standard deviation, take the square root before computing, and say so, since examiners frequently plant the variance deliberately.

### 2.6 The conditions that keep chi-square valid

The chi-square reference distribution is a large-sample approximation, and three conditions govern its use.

Every expected count should be at least five; otherwise the approximation is poor and an exact or simulated test is preferable. The expected counts must add to the observed totals, both by row and by column. The observations must be independent, so that each unit contributes to exactly one cell.

A candidate who checks the expected counts and writes "all expected counts exceed five, so the approximation is valid" earns a condition mark that is often available and rarely claimed.

### 2.7 Identities connecting the two p-values

> **Lemma (One tail and two tails).** For a symmetric statistic with observed value $t_{\text{obs}} > 0$, the two-sided p-value equals twice the one-sided p-value in the direction of the observation, so $p_{\text{two}} = 2p_{\text{one}}$.

The identity is exact for the normal and t distributions, which are symmetric, and it fails for the chi-square and F distributions, which are not.

This gives two examinable facts. The p-value halves when the alternative changes from two-sided to one-sided on the same data, and the critical value falls from $1.96$ to $1.645$, so the same statistic can cross the boundary between the two conventions. A question that asks a candidate to comment on a study where the two-sided result was not significant but the one-sided result was is testing exactly this point.

### 2.8 Significance at one level and not another

Because the critical values increase as the level falls, a fixed statistic can be significant at $5\%$ and not at $1\%$. The band between $1.96$ and $2.576$ is where this happens in a two-sided normal test.

The correct language is to give the level with the verdict: "significant at the $5\%$ level but not at the $1\%$ level" is a complete and accurate statement, and "significant" alone is not. Reporting the p-value avoids the issue entirely, because any reader can apply their own level to it.

### 2.9 Summary of high-yield results

| Result | Statement | Typical exam use |
| --- | --- | --- |
| Direction lemma | alternative fixes the tails | choosing $1.645$ or $1.96$ |
| Duality | interval membership equals non-rejection | one-line check and follow-up parts |
| df rules | $n - 1$, $n_1 + n_2 - 2$, $k - 1 - m$, $\left(r - 1\right)\left(c - 1\right)$ | a standalone mark |
| z versus t | known $\sigma$ versus estimated $s$ | selecting the statistic |
| Chi-square conditions | expected counts at least five | a condition mark |
| Tail identity | two-sided p is twice one-sided p | comments on one-sided tests |
| Level sensitivity | significance depends on the level | interpretation marks |

### 2.10 The trap table

The traps below account for most of the marks lost on this topic. Each row names the trap, the wrong move it provokes, and the correct move.

| Trap | Wrong move | Correct move |
| --- | --- | --- |
| The question asks about consistency or spread | testing means | use the F test on variances |
| A sample standard deviation is given with a small sample | using $1.96$ | use the t table with $n - 1$ df |
| The sample proportion appears in the standard error | using $\hat{p}$ under the null | use $p_0$ in the denominator |
| The alternative is one-sided | using $\pm 1.96$ | use the single tail value $1.645$ |
| A paired design is described | treating the two columns as independent samples | difference each pair first |
| A $3 \times 2$ table is tested | using $6 - 1 = 5$ df | use $\left(3 - 1\right)\left(2 - 1\right) = 2$ |
| A goodness-of-fit test estimates a parameter | using $k - 1$ df | subtract one more for each estimated parameter |
| Expected counts are small | quoting the chi-square p-value | pool categories or use an exact test |
| The test is not significant | writing "the means are equal" | write "insufficient evidence of a difference" |
| The statistic is computed but not interpreted | stopping at the verdict | add a sentence about the population and the level |

## 3. Formal Proofs, Derivations, and Methods

### 3.1 The standard error, derived once and reused

Every statistic in this topic is a distance divided by a standard error, so a single derivation covers them all.

For independent observations with variance $\sigma^{2}$,

$$
\text{Var}\left(\bar{x}\right) = \frac{1}{n^{2}}\sum_{i=1}^{n}\sigma^{2} = \frac{\sigma^{2}}{n}, \qquad \text{SE}\left(\bar{x}\right) = \frac{\sigma}{\sqrt{n}} .
$$

Replacing $\sigma$ by the sample standard deviation $s$ gives the estimated standard error $s/\sqrt{n}$, and the ratio acquires a t distribution with $n - 1$ degrees of freedom instead of a normal one.

For a proportion, the observation coded one for success has variance $p\left(1 - p\right)$, so

$$
\text{SE}\left(\hat{p}\right) = \sqrt{\frac{p\left(1 - p\right)}{n}} ,
$$

and under the null this becomes $\sqrt{p_0\left(1 - p_0\right)/n}$.

For a difference of independent means,

$$
\text{Var}\left(\bar{x}_1 - \bar{x}_2\right) = \frac{\sigma_1^{2}}{n_1} + \frac{\sigma_2^{2}}{n_2},
$$

and when the two variances are equal the pooled estimate substitutes for both.

### 3.2 Turning a critical value into a region for the sample mean

Many questions ask for the rejection region in the original units, and the translation is mechanical.

Step 1. Write the rejection region for the statistic, for example $z > 1.645$.

Step 2. Substitute the definition, $\left(\bar{x} - \mu_0\right)/\text{SE} > 1.645$.

Step 3. Rearrange to isolate the sample mean, giving $\bar{x} > \mu_0 + 1.645\,\text{SE}$.

Step 4. Evaluate with the numerical standard error.

For a two-sided test the region is $\bar{x} < \mu_0 - 1.96\,\text{SE}$ or $\bar{x} > \mu_0 + 1.96\,\text{SE}$, which is also the pair of values outside the confidence interval. This is duality in its most concrete form.

### 3.3 Reading a p-value from printed tables

Printed t and chi-square tables give quantiles rather than tail areas, so a p-value is usually bracketed rather than computed exactly.

Step 1. Locate the row for the degrees of freedom.

Step 2. Find the two tabulated values that bracket the statistic.

Step 3. Read the tail probabilities attached to those values and reverse their order, because a larger statistic has a smaller tail.

Step 4. Write the bracket, for example $0.01 < p < 0.025$.

Step 5. Compare the bracket with $\alpha$ and decide.

A bracket that straddles $\alpha$ is a warning sign, and the honest answer in that case is to report the bracket and note that the decision is marginal.

### 3.4 Deriving the pooled standard error

The pooled variance is the weighted average of the two sample variances, with weights equal to the degrees of freedom.

$$
s_p^{2} = \frac{\left(n_1 - 1\right)s_1^{2} + \left(n_2 - 1\right)s_2^{2}}{n_1 + n_2 - 2} .
$$

The standard error of the difference then follows from independence,

$$
\text{SE}\left(\bar{x}_1 - \bar{x}_2\right) = \sqrt{s_p^{2}\left(\frac{1}{n_1} + \frac{1}{n_2}\right)} .
$$

The degrees of freedom are the sum of the two individual degrees of freedom, because the two samples contribute independent information about a single common variance. When the sample sizes are equal the pooled variance is simply the average of the two sample variances, a shortcut worth remembering.

### 3.5 The contingency-table recipe

The independence test is the most error-prone computation in the topic, and a fixed recipe removes the errors.

Step 1. Add the row totals and the column totals and check that both sum to the grand total.

Step 2. Compute each expected count as row total times column total divided by the grand total, and check that the expected counts reproduce both sets of totals.

Step 3. Compute each cell contribution as the squared difference divided by the expected count.

Step 4. Add the contributions.

Step 5. Compute the degrees of freedom as $\left(r - 1\right)\left(c - 1\right)$.

Step 6. Compare with the critical value and interpret, naming the cell that contributes most.

The final instruction is worth marks because the largest contribution identifies the pattern behind a significant result.

### 3.6 The arithmetic shortcuts that save time

Three shortcuts recur.

Every contribution is a square divided by a positive expected count, so every contribution is non-negative and the total can be zero only when every observed count equals its expected count. A small statistic therefore indicates good agreement with the null hypothesis, never poor agreement, and no cancellation between cells is possible; each cell must be computed and added.

For a $2 \times 2$ table the contribution can be computed once and multiplied by four when both row totals and both column totals are equal, because the four cells are then symmetric.

The variance satisfies $\sum \left(x_i - \bar{x}\right)^{2} = \sum x_i^{2} - n\bar{x}^{2}$, which avoids computing each deviation when the data are integers.

### 3.7 Earning the interpretation marks

The interpretation sentence is worth one or two marks and is frequently left out. It has a fixed shape.

It names the population, the parameter and the direction of the conclusion; it states the level; and it says what the decision does not establish.

A complete example: "At the $5\%$ level there is sufficient evidence that the mean fill differs from $500$ grams, and the sample mean lies above the target, so the evidence points to overfilling. This does not establish that every tin is overfilled, nor does it measure the size of the average excess."

### 3.8 The two-group and two-variance procedures in brief

Four formulas cover the comparisons between groups that appear in papers, and each is a variation on the standard error.

For paired data the statistic is computed on the differences.

$$
t = \frac{\bar{d}}{s_d/\sqrt{n}}, \qquad \nu = n - 1 .
$$

For two independent samples with a pooled variance the statistic is the difference of means over its standard error.

$$
t = \frac{\bar{x}_1 - \bar{x}_2}{\sqrt{s_p^{2}\left(\frac{1}{n_1} + \frac{1}{n_2}\right)}}, \qquad s_p^{2} = \frac{\left(n_1 - 1\right)s_1^{2} + \left(n_2 - 1\right)s_2^{2}}{n_1 + n_2 - 2}, \qquad \nu = n_1 + n_2 - 2 .
$$

For the comparison of two variances the statistic is a ratio, with the larger variance placed in the numerator so that only the upper critical value is needed.

$$
F = \frac{s_{\text{large}}^{2}}{s_{\text{small}}^{2}}, \qquad \nu_1 = n_{\text{large}} - 1, \qquad \nu_2 = n_{\text{small}} - 1 .
$$

A worked illustration of the third formula is short enough to state in steps.

Step 1. Take sample variances of $36$ from $25$ observations and $12$ from $16$ observations, and test at the $5\%$ level whether the population variances differ.

Step 2. Place the larger variance on top.

$$
F = \frac{36}{12} = 3.00 .
$$

Step 3. Record the degrees of freedom.

$$
\nu_1 = 24, \qquad \nu_2 = 15 .
$$

Step 4. Use the $2.5\%$ upper point, because the alternative is two-sided and the smaller tail is then covered by the reciprocal.

$$
F_{0.025, 24, 15} = 2.701 .
$$

Step 5. Since $3.00 > 2.701$, reject equality of variances at the $5\%$ level. The conclusion rests on normal populations, and the test is not robust to heavy tails.

## 4. Representative Worked Examples and Solutions

### 4.1 Problem: a z test for a mean with a known standard deviation

A factory claims that the mean mass of a pack is $100$ grams. The packing process has a standard deviation of $20$ grams, known from many years of records. A random sample of $100$ packs has a mean mass of $104.5$ grams. Test at the $5\%$ level whether the mean mass differs from $100$ grams. The question is worth $7$ marks.

### 4.2 Solution: model answer with marking points

Step 1. [1 mark] Define the parameter and state the hypotheses. Let $\mu$ be the population mean mass in grams.

$$
H_0: \mu = 100, \qquad H_1: \mu \ne 100 .
$$

Step 2. [1 mark] Name the test. The population standard deviation is known, so the one-sample z test applies, and the statistic is standard normal under $H_0$. The sample of $100$ is large enough for the central limit theorem to support the normal reference distribution.

Step 3. [1 mark] Compute the standard error.

$$
\text{SE} = \frac{\sigma}{\sqrt{n}} = \frac{20}{\sqrt{100}} = \frac{20}{10} = 2 .
$$

Step 4. [1 mark] Compute the statistic.

$$
z = \frac{104.5 - 100}{2} = \frac{4.5}{2} = 2.25 .
$$

Step 5. [1 mark] Obtain the critical value for a two-sided test at $5\%$, which is $\pm 1.96$, and compare. Since $2.25 > 1.96$, the statistic lies in the rejection region.

Step 6. [2 marks] State the decision and interpret. Reject $H_0$. At the $5\%$ level there is sufficient evidence that the mean mass differs from $100$ grams. The sample mean exceeds the target, so the evidence indicates overfilling. The test does not measure how much overfilling occurs, and it does not show that every pack is heavy.

Working check. The two-sided p-value is $2\left(1 - \Phi\left(2.25\right)\right) = 0.0244$, which is below $0.05$ and confirms the decision. The $95\%$ interval is $104.5 \pm 3.92$, that is from $100.58$ to $108.42$ grams; the null value $100$ lies outside it, which is duality at work.

### 4.3 Problem: a t test for a mean with an estimated standard deviation

A sample of $16$ batteries has a mean lifetime of $48.4$ hours and a sample standard deviation of $5.6$ hours. The manufacturer claims a mean lifetime of $45$ hours, and an inspector suspects the true mean is higher. Test the inspector's suspicion at the $5\%$ level. The question is worth $8$ marks.

### 4.4 Solution: model answer with marking points

Step 1. [1 mark] State the hypotheses. The word "higher" fixes an upper one-sided alternative.

$$
H_0: \mu = 45, \qquad H_1: \mu > 45 .
$$

Step 2. [1 mark] Name the test and the reference distribution. The population standard deviation is unknown and estimated by $s$, so the one-sample t test is required, with $16 - 1 = 15$ degrees of freedom. The lifetime is assumed approximately normal.

Step 3. [1 mark] Compute the standard error.

$$
\frac{s}{\sqrt{n}} = \frac{5.6}{\sqrt{16}} = \frac{5.6}{4} = 1.4 .
$$

Step 4. [1 mark] Compute the statistic.

$$
t = \frac{48.4 - 45}{1.4} = \frac{3.4}{1.4} = 2.429 .
$$

Step 5. [1 mark] Obtain the critical value. For a one-sided test at $5\%$ with $15$ degrees of freedom the critical value is $t_{0.05, 15} = 1.753$.

Step 6. [1 mark] Compare. Since $2.429 > 1.753$, the statistic lies in the rejection region.

Step 7. [1 mark] Report the p-value. From tables, $2.429$ lies between the $1\%$ point $2.602$ and the $2.5\%$ point $2.131$, so $0.01 < p < 0.025$; the exact value is $0.0141$.

Step 8. [1 mark] Conclude in context. Reject $H_0$. At the $5\%$ level there is sufficient evidence that the mean lifetime exceeds $45$ hours, which supports the inspector's suspicion.

Working check. Had the normal critical value $1.645$ been used, the verdict would have been the same, but the margin would have been overstated; the correct reference distribution for an estimated standard deviation with sixteen observations is the t distribution.

### 4.5 Problem: a test for a single proportion

A retailer claims that half of its customers would recommend the product. In a random sample of $250$ customers, $145$ say they would recommend it. Test at the $5\%$ level whether the population proportion differs from one half. The question is worth $7$ marks.

### 4.6 Solution: model answer with marking points

Step 1. [1 mark] State the hypotheses, with $p$ the population proportion who would recommend.

$$
H_0: p = 0.5, \qquad H_1: p \ne 0.5 .
$$

Step 2. [1 mark] Compute the sample proportion.

$$
\hat{p} = \frac{145}{250} = 0.58 .
$$

Step 3. [1 mark] Compute the null standard error, using $p_0$ rather than $\hat{p}$.

$$
\text{SE}_0 = \sqrt{\frac{0.5 \times 0.5}{250}} = \sqrt{0.001} = 0.03162 .
$$

Step 4. [1 mark] Check the approximation conditions.

$$
np_0 = 125 \ge 10, \qquad n\left(1 - p_0\right) = 125 \ge 10 .
$$

Step 5. [1 mark] Compute the statistic.

$$
z = \frac{0.58 - 0.5}{0.03162} = \frac{0.08}{0.03162} = 2.530 .
$$

Step 6. [1 mark] Compare with the two-sided critical value $1.96$. Since $2.530 > 1.96$, reject $H_0$.

Step 7. [1 mark] Interpret. The two-sided p-value is $2\left(1 - \Phi\left(2.530\right)\right) = 0.0114$, so there is sufficient evidence at the $5\%$ level that the population proportion differs from one half. The sample proportion of $0.58$ lies above one half, so the evidence suggests that more than half would recommend the product.

Working check. The interval $0.58 \pm 1.96 \times 0.03162$ runs from $0.518$ to $0.642$ and excludes $0.5$, consistent with the rejection. Using $\hat{p}$ in the denominator would have given $0.08/0.03122 = 2.562$, a small numerical difference here but a serious conceptual error.

### 4.7 Problem: a chi-square test of independence in a three-by-two table

A survey of $200$ consumers records age group and preferred brand. Among $100$ consumers aged under $40$, the preferences are Brand A $52$, Brand B $30$ and Brand C $18$. Among $100$ consumers aged $40$ and over, the preferences are Brand A $28$, Brand B $40$ and Brand C $32$. Test at the $5\%$ level whether age group and brand preference are independent. The question is worth $10$ marks.

### 4.8 Solution: model answer with marking points

Step 1. [1 mark] State the hypotheses. The null is independence of the two classifications; the alternative is that preference depends on age group.

Step 2. [2 marks] Assemble the observed table with totals and compute the expected counts from row total times column total over the grand total.

| Age group | Brand A | Brand B | Brand C | Row total |
| --- | --- | --- | --- | --- |
| Under 40 | 52 | 30 | 18 | 100 |
| 40 and over | 28 | 40 | 32 | 100 |
| Column total | 80 | 70 | 50 | 200 |

$$
E_{11} = \frac{100 \times 80}{200} = 40, \qquad E_{12} = \frac{100 \times 70}{200} = 35, \qquad E_{13} = \frac{100 \times 50}{200} = 25 ,
$$

$$
E_{21} = \frac{100 \times 80}{200} = 40, \qquad E_{22} = \frac{100 \times 70}{200} = 35, \qquad E_{23} = \frac{100 \times 50}{200} = 25 .
$$

Step 3. [2 marks] Compute the six contributions.

$$
\frac{\left(52 - 40\right)^{2}}{40} = 3.600, \qquad \frac{\left(30 - 35\right)^{2}}{35} = 0.714, \qquad \frac{\left(18 - 25\right)^{2}}{25} = 1.960 ,
$$

$$
\frac{\left(28 - 40\right)^{2}}{40} = 3.600, \qquad \frac{\left(40 - 35\right)^{2}}{35} = 0.714, \qquad \frac{\left(32 - 25\right)^{2}}{25} = 1.960 .
$$

Step 4. [1 mark] Add the contributions.

$$
\chi^{2} = 3.600 + 0.714 + 1.960 + 3.600 + 0.714 + 1.960 = 12.549 .
$$

Step 5. [2 marks] Determine the degrees of freedom and the critical value.

$$
\nu = \left(r - 1\right)\left(c - 1\right) = \left(2 - 1\right)\left(3 - 1\right) = 2, \qquad \chi^{2}_{0.05, 2} = 5.991 .
$$

Step 6. [1 mark] Check the conditions. All six expected counts are at least $25$, so the chi-square approximation is valid.

Step 7. [1 mark] Decide and interpret. Since $12.549 > 5.991$, reject $H_0$. There is sufficient evidence at the $5\%$ level that brand preference is associated with age group. The largest contributions come from Brand A, which is chosen by $52$ younger consumers against $40$ expected, and Brand C, which is chosen by $32$ older consumers against $25$ expected.

Working check. The p-value is approximately $0.0019$, well below $0.05$. The expected counts reproduce both the row totals of $100$ and the column totals of $80$, $70$ and $50$, which confirms the arithmetic.

### 4.9 Problem: a short question on duality and on the meaning of p

A student tests $H_0: \mu = 60$ against $H_1: \mu \ne 60$ at the $5\%$ level and reports $p = 0.032$. Write the two sentences the student should add, and state what the $95\%$ confidence interval must show. The question is worth $4$ marks.

### 4.10 Solution: model answer with marking points

Step 1. [1 mark] State the decision with its level. Since $0.032 \le 0.05$, reject $H_0$ at the $5\%$ level.

Step 2. [1 mark] State what the p-value means, in the conditional direction. If the population mean were $60$, a sample mean at least as far from $60$ as the one observed would occur about $3.2\%$ of the time.

Step 3. [1 mark] State what the p-value does not mean. It is not the probability that $H_0$ is true, and it does not measure the size of any departure.

Step 4. [1 mark] Apply duality. The $95\%$ confidence interval must exclude $60$, because a two-sided test at $5\%$ rejects exactly when the null value lies outside the $95\%$ interval.

## 5. Mathematical Extensions, Limits, and Common Errors

### 5.1 The error and deduction catalogue

The catalogue below lists the errors that appear most often in written answers, the deduction each typically attracts, and the correction. Marks differ between papers, but the ordering of the deductions is stable.

| Error | Typical deduction | Correction |
| --- | --- | --- |
| Hypotheses written about $\bar{x}$ instead of $\mu$ | $1$ mark | hypotheses always concern the population parameter |
| Alternative chosen to match the sign of the data | $1$ to $2$ marks | fix the direction from the wording before computing |
| Standard deviation used instead of standard error | $1$ mark and all downstream arithmetic | divide by $\sqrt{n}$ as well |
| $z$ used when $s$ is estimated and $n$ is small | $1$ mark for the test and $1$ for the critical value | use the t distribution with $n - 1$ df |
| $\hat{p}$ used in the null standard error of a proportion | $1$ mark | use $p_0$ |
| Wrong degrees of freedom | $1$ mark | $n - 1$, $n_1 + n_2 - 2$, $k - 1 - m$, $\left(r - 1\right)\left(c - 1\right)$ |
| Paired data analysed as two independent samples | $2$ marks | difference the pairs and test the mean difference |
| Continuity or expected-count condition not checked | $1$ mark | state the smallest expected count |
| Decision stated as "accept $H_0$" | $1$ mark | write "do not reject $H_0$" |
| No interpretation in context | $1$ to $2$ marks | name the population, the direction and the level |
| p-value reported as the probability that $H_0$ is true | $1$ to $2$ marks | use the conditional statement |
| Units omitted from the conclusion | a fraction of the interpretation mark | attach the measurement units |

A candidate who writes the six step labels before starting cannot easily fall into the first, ninth or tenth of these errors, because the labels impose the order the examiner is looking for.

### 5.2 The misinterpretations of the p-value

The p-value is the probability of the observed result, or something more extreme, assuming the null hypothesis is true. Every other reading is wrong, and four wrong readings appear constantly.

It is not the probability that the null hypothesis is true. The p-value conditions on the null, so it cannot report a probability about the null.

It is not the probability that the result occurred by chance. Chance is not a hypothesis in this framework, and the statement has no formal meaning.

One minus the p-value is not the probability that the result will replicate. Replication depends on the power of the original study, and a result just below the threshold is the least stable kind.

A small p-value is not evidence of a large effect. A very precise estimate of a trivial difference can produce a smaller p-value than an imprecise estimate of a large one.

The correct verbal form is worth memorising because it appears in mark schemes: "If $H_0$ were true, a result at least as extreme as that observed would occur in about $p$ of all samples."

### 5.3 Limits of the tests and the assumptions that must be stated

Every test in this topic inherits its reference distribution from a model, and a paper that asks for assumptions is asking for the model to be named.

The z and t tests require independent observations and, for exactness in small samples, a normal population. The two-sample form adds the assumption of equal population variances when a pooled estimate is used.

The chi-square tests require independent observations, mutually exclusive and exhaustive categories, and expected counts of at least about five.

The F test requires independent normal samples and is highly sensitive to departures from normality, particularly heavy tails.

A useful habit is to write one line of conditions immediately after naming the test. It costs ten seconds and is often worth a mark, and it protects the candidate from the larger error of applying a test whose assumptions plainly fail.

### 5.4 Revision checklist

The checklist below is ordered by the frequency with which each item appears in examination papers.

The five-step structure: hypotheses, test selection, standard error, statistic, decision and interpretation. Recite it until it is automatic.

The three alternatives and their critical values at $5\%$: $1.96$ two-sided, $1.645$ upper, $-1.645$ lower.

The rule for choosing z or t: known $\sigma$ means z, estimated $s$ means t.

The degrees-of-freedom rules, written out once from memory and checked against a table.

The four standard errors: $\sigma/\sqrt{n}$, $s/\sqrt{n}$, $\sqrt{p_0\left(1 - p_0\right)/n}$ and the pooled two-sample form.

The contingency-table recipe, including the expected-count check.

The definitions of Type I error, Type II error and power, with the two-by-two table.

The duality statement, with the sentence that converts an interval into a test.

The correct and incorrect readings of the p-value.

The assumptions attached to each test, in one line each.

A candidate who can write all ten items from memory in fifteen minutes has covered the examinable content of this topic.

### 5.5 Timed strategy for the examination

The allocation below assumes a paper in which this topic carries about twenty-five marks, which is typical.

Spend two minutes reading every part and marking the test each part requires, using the recognition table. Deciding the test before writing anything prevents the most expensive error of the paper, which is analysing a consistency question with a means test.

Allow six minutes for a seven-mark z or proportion question. The arithmetic is short; the marks are in the hypotheses, the standard error and the interpretation.

Allow eight minutes for an eight-mark t question, because the critical value must be looked up with the correct degrees of freedom and the p-value bracket must be read from the table.

Allow twelve minutes for a ten-mark chi-square question. Six contributions and six expected counts take time, and the totals must be checked.

Reserve three minutes at the end for the interpretation sentences and the units. These are the marks most often forfeited by candidates who run out of time.

If a computed statistic falls within a few hundredths of a critical value, say so explicitly: "the statistic is close to the critical value, so the decision is marginal". Examiners credit the observation, and the sentence protects the candidate if the arithmetic is slightly adrift.

If two parts of a question disagree, recheck the standard error first, then the degrees of freedom, then the number of tails. Those three account for nearly every internal inconsistency in this topic.

### 5.6 Where the subject extends beyond the examination

Three extensions are worth knowing because they generalise everything above and appear in later study.

The likelihood ratio test compares the maximised likelihood under the null with the maximised likelihood overall, and its statistic converges to a chi-square distribution with degrees of freedom equal to the number of restrictions. Every test in this topic is a special case, and the degrees-of-freedom rules follow from counting restrictions rather than from table conventions.

Analysis of variance generalises the two-sample comparison to three or more groups, using an F statistic that compares variability between group means with variability within groups. The two-sample t test is the two-group case, and the identity $F = t^{2}$ links the two.

Resampling methods, including the permutation test and the bootstrap, replace the theoretical reference distribution with an empirical one. They are the standard remedy when the sample is small, the distribution is unknown, or the expected counts are too small for the chi-square approximation.

All three preserve the courtroom logic that organises this topic: a claim is presumed true, the evidence must dislodge it, and the standard of proof is fixed before the evidence is examined.
