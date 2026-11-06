## 1. Foundational Concepts, Definitions, and Axioms

### 1.1 The design-based framework

Sampling theory is built on a deliberate fiction that turns out to be extremely useful. The population values are treated as fixed constants, not as random quantities. Nothing in the population is random: the value of the variable for a given unit is whatever it is. Randomness enters only through the selection rule, which decides which units are observed. This is the design-based or randomisation framework, and every result in this note is a statement about repeated application of a selection rule to a fixed population.

Three consequences follow immediately. First, an estimator is a random variable even though the population is fixed, because the estimator is a function of the random set of units selected. Second, the variance of an estimator describes the spread of its values over all samples the design could have produced, not any property of a single realised sample. Third, the expectation of an estimator is taken over the selection mechanism, so the phrase "unbiased" always means "unbiased over the randomisation distribution of the design".

The alternative, model-based framework treats the population values themselves as draws from a superpopulation. It is useful for prediction and for regression, and it produces similar formulas in large samples, but it is not the framework in which sampling designs are compared, because the whole point of a design is to control which units are observed rather than to assume anything about how they were generated.

### 1.2 Formal definitions

> **Definition (Unit and population).** A unit is a single identifiable element of the population. The population $U$ is the finite set of $N$ units about which inference is required.

> **Definition (Variable and parameter).** A variable $Y$ assigns a real value $y_i$ to every unit $i$ of $U$. A parameter is any function of the complete set of population values; the three used throughout are the population mean, the population total, and the population proportion.

$$
\mu = \frac{1}{N}\sum_{i=1}^{N} y_i, \qquad Y = \sum_{i=1}^{N} y_i = N\mu, \qquad \pi = \frac{1}{N}\sum_{i=1}^{N} a_i ,
$$

where $a_i$ is an indicator taking the value one when unit $i$ possesses the attribute and zero otherwise.

> **Definition (Sampling frame).** The sampling frame $F$ is the operational list of $N_F$ units from which the sample is drawn. Coverage error is the discrepancy between $U$ and $F$, and it is present whenever $F$ omits units of $U$, contains units not in $U$, or contains duplicates.

> **Definition (Sample and sample size).** A sample $s$ is a subset of $F$. Its size $n$ may be fixed by the design or may be a random variable, as it is in cluster sampling with unequal cluster sizes.

> **Definition (Sampling design).** A sampling design is a probability distribution $p(s)$ over the collection of all subsets of $F$, together with the rule that generates a draw from that distribution. A design is a probability design when $p(s)$ is known and every unit has a strictly positive inclusion probability.

> **Definition (Inclusion probability).** The first-order inclusion probability of unit $i$ is $\pi_i = P(i \in s)$, and the second-order inclusion probability of the pair $i, j$ is $\pi_{ij} = P(i \in s \text{ and } j \in s)$.

> **Definition (Estimator and estimate).** An estimator is a rule $\hat{\theta} = \hat{\theta}(s, y)$ that assigns a value to every possible sample. A particular value computed from the realised sample is an estimate.

The distinction between the two Greek symbols is worth fixing early. The symbol $\pi$ is used for a population proportion in some texts and for an inclusion probability in others; in this note $\pi_i$ always denotes an inclusion probability and $p$ always denotes a sample proportion.

### 1.3 Notation used throughout

The notation is conventional, and it is stated once so that every later formula can be read without ambiguity.

| Symbol | Meaning |
| --- | --- |
| $N$ | number of units in the population |
| $n$ | number of units in the sample |
| $H$ | number of strata |
| $N_h$ | number of units in stratum $h$ |
| $n_h$ | number of units sampled from stratum $h$ |
| $W_h$ | stratum weight $N_h/N$ |
| $M_c$ | number of clusters in the population |
| $m$ | number of clusters selected |
| $M$ | number of units in a cluster of equal size |
| $y_i$ | value of the variable for unit $i$ |
| $\bar{y}$ | sample mean |
| $\mu$ | population mean |
| $S^{2}$ | population variance with divisor $N-1$ |
| $S_h^{2}$ | stratum variance with divisor $N_h-1$ |
| $f$ | sampling fraction $n/N$ |
| $\rho$ | intra-cluster correlation |

The population variance is defined with divisor $N-1$ throughout, because that is the quantity for which the sample variance is unbiased.

$$
S^{2} = \frac{1}{N-1}\sum_{i=1}^{N}\left(y_i - \mu\right)^{2}
$$

Some texts use the divisor $N$ and write $\sigma^{2}$. The two are related by a factor that depends only on the population size, so no result changes in substance, but a candidate who mixes conventions will produce a variance that is wrong in the third decimal place and sometimes in the second.

$$
\sigma^{2} = \frac{1}{N}\sum_{i=1}^{N}\left(y_i - \mu\right)^{2} = \frac{N-1}{N}S^{2}
$$

### 1.4 Properties by which estimators are judged

> **Definition (Unbiasedness).** An estimator $\hat{\theta}$ is unbiased for $\theta$ when its expectation over the design equals the parameter, that is $E(\hat{\theta}) = \theta$ for every possible set of population values.

> **Definition (Variance and standard error).** The variance of an estimator is $\text{Var}(\hat{\theta}) = E\left[\left(\hat{\theta} - E(\hat{\theta})\right)^{2}\right]$, and its standard error is the square root of that variance.

> **Definition (Mean squared error).** The mean squared error is $\text{MSE}(\hat{\theta}) = E\left[\left(\hat{\theta} - \theta\right)^{2}\right]$, and it decomposes into variance plus squared bias.

$$
\text{MSE}(\hat{\theta}) = \text{Var}(\hat{\theta}) + \left[\text{Bias}(\hat{\theta})\right]^{2}
$$

The decomposition is the reason precision and accuracy are separate concepts. Increasing the sample size drives the variance term towards zero and leaves the bias term untouched, so an estimator can be made arbitrarily precise while remaining systematically wrong. Every non-probability design is biased in an amount that cannot be estimated from the data, and that is the precise sense in which such designs fail.

### 1.5 Probability designs

> **Definition (Simple random sampling).** Simple random sampling without replacement is the design in which every subset of $n$ distinct units has the same probability of selection, namely $1/\binom{N}{n}$.

The design implies equal inclusion probabilities and equal second-order probabilities.

$$
\pi_i = \frac{n}{N}, \qquad \pi_{ij} = \frac{n(n-1)}{N(N-1)}
$$

The second-order probability is needed for variance estimation under designs with unequal probabilities, and it is worth noting that it is slightly larger than the square of the first-order probability, which is the algebraic form of the negative dependence created by sampling without replacement.

> **Definition (Simple random sampling with replacement).** Each of the $n$ draws is made independently from the whole population with equal probability $1/N$, so the same unit may appear several times.

Both versions are implemented by one of two devices. The lottery device numbers the units, writes the numbers on identical slips, mixes them, and draws $n$ slips, setting each aside when replacement is not wanted. The random number table device reads groups of digits of the appropriate length from a published table, discards any group that is zero or exceeds $N$, and discards repeats when replacement is not wanted. The discarding rule is what preserves the equal-probability property: an out-of-range group corresponds to no unit, and a repeated group corresponds to a unit already in the sample, so removing both leaves every admissible set equally likely. A table in which a human has chosen the starting point with a visible pattern, or a sequence typed from memory, is not a random device, because the independence of successive digits is exactly what the table is used for.

> **Definition (Stratified sampling).** The population is partitioned into $H$ non-overlapping strata of sizes $N_h$ summing to $N$, and an independent simple random sample of size $n_h$ is drawn within each stratum.

> **Definition (Systematic sampling).** The units are placed in a list of length $N$, a random start $r$ is drawn uniformly from $\{1, 2, \dots, k\}$, and the units in positions $r, r+k, r+2k, \dots$ are selected, where $k = N/n$ is the sampling interval.

> **Definition (Cluster sampling).** The population is partitioned into $M_c$ clusters, a simple random sample of $m$ clusters is drawn, and every unit inside each selected cluster is measured.

> **Definition (Multistage sampling).** The population is partitioned into primary sampling units, a sample of them is drawn, each selected primary unit is partitioned into secondary units, a sample of those is drawn, and the process may continue to a third stage.

The five designs differ in where the randomisation acts. In the first two the randomisation acts on individual units, in the third it acts on a position in a list, in the fourth and fifth it acts on groups. That single difference generates almost every contrast that examinations test.

### 1.6 Non-probability designs

> **Definition (Convenience sampling).** Units are selected because they are accessible, near, or willing, with no chance mechanism involved.

> **Definition (Quota sampling).** The population is divided into categories, a quota is fixed for each category, and interviewers fill the quotas by whatever means they can, so the composition is controlled but the selection inside each category is not.

> **Definition (Judgement or purposive sampling).** Units are selected because the investigator judges them to be typical, representative, or especially informative.

> **Definition (Snowball sampling).** An initial set of accessible respondents is interviewed and asked to nominate further respondents, so that the sample grows along social or organisational links.

None of the four assigns a known selection probability, so none supports design-based inference. Their biases differ in mechanism and can be described quantitatively once the excluded group is characterised. Quota sampling biases the estimate towards the easy-to-interview within each quota cell, which is invisible in the marginal tabulation. Judgement sampling biases it towards the investigator's model of a typical unit. Snowball sampling biases it towards densely connected units and omits isolates, so it under-represents exactly the marginal groups that studies of hidden populations usually seek. Convenience sampling biases it towards whatever attribute makes a unit accessible, which may be unrelated to the variable studied and may be strongly related to it, and the survey cannot tell the two cases apart.

### 1.7 Sampling error and non-sampling error

> **Definition (Sampling error).** Sampling error is the deviation of an estimate from the parameter that arises solely because a subset rather than the whole population was measured. It is measured by the standard error of the estimator.

> **Definition (Non-sampling error).** Non-sampling error is every deviation that is not attributable to the selection of a subset, including coverage error, non-response error, measurement error, and processing error.

Total survey error combines the two, and the combination is not a sum of magnitudes but a mean squared error.

$$
\text{MSE}\left(\hat{\theta}\right) = \text{Var}\left(\hat{\theta}\right) + B_{\text{cov}}^{2} + B_{\text{nr}}^{2} + B_{\text{meas}}^{2}
$$

The formula explains a fact that surprises beginners: a census has zero sampling variance and can still be worse than a sample, because the three bias terms remain and are often larger when a large temporary workforce is hired and hurried.

### 1.8 Sampling with and without replacement

The distinction between the two modes of selection is not a technicality. Without replacement, each unit can appear at most once, the sample contains $n$ distinct units, and the composition of the population changes from draw to draw. With replacement, a unit may appear repeatedly, the draws are independent, and the arithmetic is that of independent observations.

The practical consequence is that without replacement is always at least as precise, and the gain is measured by the finite population correction. The theoretical consequence is that with replacement is easier to analyse, which is why several designs are defined with replacement and then improved by the correction.

### 1.9 The assumptions that the standard formulas require

Four assumptions underlie the variance formulas of Section 2, and stating them shows exactly what a scenario must satisfy before those formulas may be used.

1. The frame lists every unit of the population exactly once, so coverage error is absent.
2. Every selected unit supplies a measurement, so non-response error is absent.
3. The measured value equals the true value, so measurement error is absent.
4. The selection rule is the one described, so the inclusion probabilities are as stated.

When any assumption fails the variance formula still describes the sampling component of error, but the total error is larger, and reporting the standard error alone overstates the quality of the survey. Assumption four is the one that fails silently: a design described as systematic but carried out with a start chosen by the supervisor is no longer a probability design, and the formula no longer applies.

## 2. Theorems, Lemmas, and Analytical Properties

### 2.1 Unbiasedness of the sample mean and the expansion estimator

> **Theorem 1 (Unbiasedness under simple random sampling).** Under simple random sampling without replacement from a population with mean $\mu$, the sample mean is unbiased for the population mean and the expansion estimator is unbiased for the population total.

$$
E\left(\bar{y}\right) = \mu, \qquad E\left(N\bar{y}\right) = Y
$$

The theorem is the foundation of every later result, because the variance formulas are variances about an unbiased centre. It holds for any population whatsoever, including populations with extreme skewness or with a large proportion of zeros, and it holds for every sample size including $n = 1$.

> **Theorem 2 (Horvitz–Thompson estimator).** For any design with strictly positive inclusion probabilities $\pi_i$, the estimator

$$
\hat{Y}_{HT} = \sum_{i \in s} \frac{y_i}{\pi_i}
$$

is unbiased for the population total.

The theorem shows that unequal probability sampling is not a defect but a design choice: a unit selected with a small probability is made to stand for many population units by the reciprocal weight. Every probability design is a special case, and the simple expansion estimator is the special case in which all inclusion probabilities equal $n/N$.

> **Corollary (Horvitz–Thompson mean).** With $N$ known, $\hat{\mu}_{HT} = \hat{Y}_{HT}/N$ is unbiased for $\mu$, and under simple random sampling it reduces to the sample mean.

### 2.2 The variance of the sample mean

> **Theorem 3 (Variance under simple random sampling without replacement).** For a sample of size $n$ drawn without replacement,

$$
\text{Var}\left(\bar{y}\right) = \frac{S^{2}}{n}\left(1 - \frac{n}{N}\right) = \frac{S^{2}}{n}\cdot\frac{N-n}{N}.
$$

> **Theorem 4 (Variance under simple random sampling with replacement).** For $n$ independent draws made with replacement,

$$
\text{Var}\left(\bar{y}\right) = \frac{\sigma^{2}}{n},
$$

where $\sigma^{2}$ uses divisor $N$.

> **Corollary (Relationship between the two).** Since $\sigma^{2} = \frac{N-1}{N}S^{2}$, the with-replacement variance exceeds the without-replacement variance by the factor

$$
\frac{\sigma^{2}/n}{\left(1 - n/N\right)S^{2}/n} = \frac{N-1}{N-n},
$$

so the two coincide only when the sample is a negligible share of the population.

The factor $1 - n/N$ is the finite population correction. It is a decreasing function of the sampling fraction, equal to one at $n = 0$, equal to $(N-1)/N$ at $n = 1$, and equal to zero at $n = N$. The last value is the algebraic statement that a census has no sampling variance.

### 2.3 The stratified estimator and its variance

> **Theorem 5 (Variance of the stratified mean).** Let the population be divided into $H$ strata, and let an independent simple random sample of size $n_h$ be drawn without replacement in stratum $h$. Then the stratified estimator

$$
\bar{y}_{st} = \sum_{h=1}^{H} W_h \bar{y}_h
$$

is unbiased for $\mu$, with variance

$$
\text{Var}\left(\bar{y}_{st}\right) = \sum_{h=1}^{H} W_h^{2}\,\frac{S_h^{2}}{n_h}\left(1 - \frac{n_h}{N_h}\right).
$$

The estimator is unbiased because each stratum mean is unbiased for its stratum parameter and the weights are constants. The variance is a sum rather than a single term because the samples in different strata are independent, so no covariance terms appear. That independence is the technical source of the precision gain: a plain random sample carries covariances between the counts falling in different groups, and stratification removes them.

### 2.4 Proportional allocation and the size of the gain

> **Theorem 6 (Variance under proportional allocation).** If the sample is allocated in proportion to stratum size, so that $n_h = nW_h$, then every stratum has the same sampling fraction $f = n/N$, and the variance of the stratified mean simplifies to

$$
\text{Var}_{prop}\left(\bar{y}_{st}\right) = \frac{1-f}{n}\sum_{h=1}^{H} W_h S_h^{2}.
$$

> **Corollary (Precision gain over simple random sampling).** Under proportional allocation the ratio of the stratified variance to the variance of a simple random sample of the same size is

$$
\frac{\text{Var}_{prop}\left(\bar{y}_{st}\right)}{\text{Var}_{srs}\left(\bar{y}\right)} = \frac{\sum_{h=1}^{H} W_h S_h^{2}}{S^{2}},
$$

so the proportional reduction in variance equals the share of total variance that lies between strata. For strata of appreciable size, which is the only case that arises in practice, stratification can never increase the variance under proportional allocation, and it leaves the variance unchanged exactly when all stratum means are equal. The qualification is needed because the exact identity of Theorem 7 carries a correction of order $1/N$, and with strata of two or three units that correction can reverse the inequality by a negligible amount.

The corollary is the most useful single sentence in the theory of stratified sampling: the gain is the between-stratum share of the variance, and nothing else. A designer who stratifies on a variable unrelated to the study variable obtains no gain at all, however carefully the strata are constructed.

### 2.5 The within-and-between decomposition

> **Theorem 7 (Exact decomposition of the population variance).** Let stratum $h$ contain $N_h$ units with mean $\mu_h$ and variance $S_h^{2}$ computed with divisor $N_h - 1$, and let $B = \sum_h W_h\left(\mu_h - \mu\right)^{2}$ be the between-stratum variance. Then

$$
S^{2} = \frac{1}{N-1}\left[\sum_{h=1}^{H}\left(N_h - 1\right)S_h^{2} + N B\right].
$$

> **Corollary (Approximate additive form).** Writing $S_w^{2} = \sum_h W_h S_h^{2}$ for the weighted average of the stratum variances,

$$
S^{2} = S_w^{2} + B + \frac{S_w^{2} + B - \sum_{h=1}^{H} S_h^{2}}{N-1},
$$

so for strata of appreciable size the total variance is the sum of a within part and a between part, and the correction term is of order $1/N$.

The decomposition is what makes the precision gain intelligible rather than merely formal. Total variation has two sources: units differ from their own stratum mean, and strata differ from each other. A simple random sample must cope with both, because a random draw may over-represent a high-mean stratum. A stratified sample fixes the second source by construction, leaving only the first, and the surviving within part is exactly what Theorem 6 reports.

### 2.6 Optimum allocation

> **Theorem 8 (Neyman allocation).** For a fixed total sample size $n$, the variance in Theorem 5 is minimised by the allocation

$$
n_h = n\,\frac{N_h S_h}{\sum_{g=1}^{H} N_g S_g} = n\,\frac{W_h S_h}{\sum_{g=1}^{H} W_g S_g},
$$

and the minimum variance is

$$
\text{Var}_{opt}\left(\bar{y}_{st}\right) = \frac{1}{n}\left(\sum_{h=1}^{H} W_h S_h\right)^{2} - \frac{1}{N}\sum_{h=1}^{H} W_h S_h^{2}.
$$

The allocation gives a large share of the sample to strata that are large and internally variable, and a small share to strata that are small or homogeneous. It differs from proportional allocation by a factor $S_h$: proportional allocation treats every unit in a stratum as equally informative, whereas optimum allocation recognises that a unit drawn from a variable stratum carries more information.

> **Corollary (Comparison with proportional allocation).** Neyman allocation is never worse than proportional allocation, and the two coincide when all stratum standard deviations are equal.

### 2.7 Variance of the systematic sample mean

> **Theorem 9 (Variance over the $k$ possible systematic samples).** Suppose $N = nk$ and the list is ordered. For each start $r = 1, \dots, k$ write $\bar{y}_r$ for the mean of the resulting systematic sample. Then

$$
E\left(\bar{y}_{sys}\right) = \frac{1}{k}\sum_{r=1}^{k}\bar{y}_r = \mu, \qquad \text{Var}\left(\bar{y}_{sys}\right) = \frac{1}{k}\sum_{r=1}^{k}\left(\bar{y}_r - \mu\right)^{2}.
$$

> **Corollary (Intra-list correlation form).** Decomposing the list into $n$ consecutive blocks of $k$ units, let $\sigma_w^{2}$ be the average variance within a block and $\rho_w$ the average correlation between units in the same position of different blocks. Then

$$
\text{Var}\left(\bar{y}_{sys}\right) = \frac{\sigma_w^{2}}{n}\left[1 + (n-1)\rho_w\right].
$$

The corollary is the analytical form of the periodicity warning. When the list is randomly ordered, $\rho_w$ is close to zero and systematic sampling behaves like simple random sampling. When the list has an upward trend, units in the same position of successive blocks are similar in level only through the trend, and $\rho_w$ is negative, so systematic sampling is substantially better than simple random sampling. When the list is periodic with period $k$, units in the same position are identical, $\rho_w$ is close to one, and the variance is close to $n$ times the value it would have under random ordering.

### 2.8 Cluster sampling and the design effect

> **Theorem 10 (Variance under one-stage cluster sampling).** With $M_c$ clusters of equal size $M$, a simple random sample of $m$ clusters, and every unit in a selected cluster measured,

$$
\text{Var}\left(\bar{y}_{cl}\right) = \frac{S_b^{2}}{m}\left(1 - \frac{m}{M_c}\right),
$$

where $S_b^{2}$ is the variance of the cluster means computed with divisor $M_c - 1$.

> **Theorem 11 (Design effect).** With $\rho$ the share of total variance lying between clusters, the design effect of the cluster design relative to a simple random sample of the same number of observation units is

$$
\text{deff} = \frac{\text{Var}\left(\bar{y}_{cl}\right)}{\text{Var}_{srs}\left(\bar{y}\right)} = 1 + (M-1)\rho ,
$$

and the effective sample size is $n_{\text{eff}} = n/\text{deff}$.

The formula makes the trade explicit. Clustering costs nothing when $\rho = 0$ and costs a factor of $M$ when $\rho = 1$. The design effect is not a small correction: values between two and twenty are routine in household surveys, so a clustered sample of a thousand households may carry the information of fewer than a hundred.

### 2.9 Two-stage sampling

> **Theorem 12 (Variance under two-stage sampling).** Suppose there are $M$ primary units each containing $B$ secondary units, a sample of $m$ primary units is drawn, and within each selected primary unit a sample of $b$ secondary units is drawn. With $S_1^{2}$ the variance of the primary-unit means and $\bar{S}_2^{2}$ the average variance within primary units,

$$
\text{Var}\left(\bar{y}\right) = \frac{1-f_1}{m}S_1^{2} + \frac{1-f_2}{mb}\bar{S}_2^{2}, \qquad f_1 = \frac{m}{M}, \quad f_2 = \frac{b}{B}.
$$

The two terms are the price of the two stages. The first term is what the sample would cost if every selected primary unit were measured completely, and the second is the extra cost of measuring only part of each selected primary unit. When the first term dominates, as it usually does, adding primary units is far more valuable than adding secondary units inside existing ones.

> **Corollary (Optimum number of secondary units).** With cost $c_1$ per primary unit and $c_2$ per secondary unit, the number of secondary units per primary unit that minimises the variance for a fixed budget is

$$
b_{opt} = \sqrt{\frac{\bar{S}_2^{2}\,c_1}{S_1^{2}\,c_2}} .
$$

### 2.10 Sample size for a mean and for a proportion

> **Theorem 13 (Sample size for a mean).** To achieve a margin of error $e$ at confidence level with normal value $z$, the required sample satisfies

$$
n_0 = \frac{z^{2}S^{2}}{e^{2}}, \qquad n = \frac{n_0}{1 + \dfrac{n_0}{N}} .
$$

> **Theorem 14 (Sample size for a proportion).** For a population proportion $p$,

$$
n_0 = \frac{z^{2}p(1-p)}{e^{2}}, \qquad n = \frac{n_0}{1 + \dfrac{n_0 - 1}{N}},
$$

and the value $p = 0.5$ maximises $n_0$ and therefore gives the conservative plan when $p$ is unknown.

Both results are inversions of the variance formula rather than new theory. The correction appears twice in the arithmetic: once implicitly, in that $n_0$ is computed as though the population were infinite, and once explicitly, in the denominator that shrinks the answer. The second appearance is what makes the saving substantial when the sample would be a large share of a small population.

> **Corollary (Stratified sample size).** With a fixed variance target $V$ and proportional allocation, the required sample is

$$
n = \frac{\sum_h W_h S_h^{2}}{V + \dfrac{1}{N}\sum_h W_h S_h^{2}} .
$$

### 2.11 Non-response

> **Theorem 15 (Non-response bias identity).** Let respondents form a proportion $w_r$ of the eligible sample with mean $\bar{y}_r$ and non-respondents the remaining proportion $w_n$ with mean $\bar{y}_n$. Then

$$
\bar{y}_r - \bar{y} = w_n\left(\bar{y}_r - \bar{y}_n\right),
$$

where $\bar{y}$ is the mean that would have been obtained had every eligible unit responded.

The identity separates the two causes of non-response bias and shows that they multiply. It also shows why a high response rate is not a certificate of quality: a rate of 95 per cent with a mean difference of 40 units between respondents and non-respondents produces a bias of 2 units, while a rate of 60 per cent with a difference of 5 units produces a bias of 2 units as well.

### 2.12 Summary of the principal results

The table collects the estimators and variances that the rest of the topic uses, so that comparisons are made on a common footing.

| Design | Estimator | Variance | Controlling quantity |
| --- | --- | --- | --- |
| Simple random, without replacement | $\bar{y}$ | $\dfrac{1-f}{n}S^{2}$ | sample size and sampling fraction |
| Simple random, with replacement | $\bar{y}$ | $\dfrac{\sigma^{2}}{n}$ | sample size only |
| Stratified, general allocation | $\sum_h W_h \bar{y}_h$ | $\sum_h W_h^{2}\dfrac{1-f_h}{n_h}S_h^{2}$ | allocation across strata |
| Stratified, proportional | $\sum_h W_h \bar{y}_h$ | $\dfrac{1-f}{n}\sum_h W_h S_h^{2}$ | within-stratum variance |
| Systematic | $\bar{y}$ | $\dfrac{\sigma_w^{2}}{n}\left[1+(n-1)\rho_w\right]$ | order of the list |
| Cluster, equal clusters | $\bar{y}$ | $\dfrac{1-f}{m}S_b^{2}$ | number of clusters |
| Two-stage | $\bar{y}$ | $\dfrac{1-f_1}{m}S_1^{2} + \dfrac{1-f_2}{mb}\bar{S}_2^{2}$ | number of primary units |

## 3. Formal Proofs, Derivations, and Methods

### 3.1 Proof of unbiasedness under simple random sampling

Introduce the selection indicator $I_i$, which equals one when unit $i$ is in the sample and zero otherwise. Under simple random sampling without replacement each unit has the same chance of selection, so

$$
E\left(I_i\right) = P\left(I_i = 1\right) = \frac{n}{N}.
$$

The sample mean is a linear function of the indicators, since unselected units contribute nothing.

$$
\bar{y} = \frac{1}{n}\sum_{i=1}^{N} I_i y_i
$$

Linearity of expectation does not require independence, so the expectation can be taken term by term.

$$
E\left(\bar{y}\right) = \frac{1}{n}\sum_{i=1}^{N} y_i E\left(I_i\right) = \frac{1}{n}\sum_{i=1}^{N} y_i \frac{n}{N} = \frac{1}{N}\sum_{i=1}^{N} y_i = \mu
$$

Because $N$ is a constant, $E\left(N\bar{y}\right) = N\mu = Y$, which proves the second part of Theorem 1. The proof uses only equal inclusion probabilities, so it holds for any design with $\pi_i = n/N$, including simple random sampling with replacement when the sample mean is defined as the mean of the distinct units drawn.

### 3.2 Proof of the variance formula and the finite population correction

The variance is computed from the same indicator representation, writing the estimator as a double sum.

$$
\text{Var}\left(\bar{y}\right) = \frac{1}{n^{2}}\sum_{i=1}^{N}\sum_{j=1}^{N} \text{Cov}\left(I_i, I_j\right) y_i y_j
$$

Two cases arise. For a unit paired with itself the covariance is a variance, computed from the Bernoulli distribution with success probability $n/N$.

$$
\text{Cov}\left(I_i, I_i\right) = \frac{n}{N}\left(1 - \frac{n}{N}\right)
$$

For two distinct units the covariance is negative, because including one unit uses up one of the $n$ places available.

$$
\text{Cov}\left(I_i, I_j\right) = E\left(I_i I_j\right) - E\left(I_i\right)E\left(I_j\right) = \frac{n(n-1)}{N(N-1)} - \frac{n^{2}}{N^{2}}
$$

Combining the two fractions over a common denominator gives the compact form used below.

$$
\text{Cov}\left(I_i, I_j\right) = -\frac{n\left(N-n\right)}{N^{2}\left(N-1\right)} \qquad \left(i \ne j\right)
$$

Substituting both cases into the double sum separates the diagonal from the cross terms.

$$
\text{Var}\left(\bar{y}\right) = \frac{1}{n^{2}}\left[\frac{n(N-n)}{N^{2}}\sum_{i=1}^{N} y_i^{2} - \frac{n(N-n)}{N^{2}(N-1)}\sum_{i \ne j} y_i y_j\right]
$$

The bracket is simplified by using the identity that relates the sum of cross products to the square of the total.

$$
\sum_{i \ne j} y_i y_j = \left(\sum_{i=1}^{N} y_i\right)^{2} - \sum_{i=1}^{N} y_i^{2}
$$

Applying the identity and collecting the terms in $\sum y_i^{2}$ gives an expression in which the total appears as a single square.

$$
\text{Var}\left(\bar{y}\right) = \frac{N-n}{nN^{2}(N-1)}\left[N\sum_{i=1}^{N} y_i^{2} - \left(\sum_{i=1}^{N} y_i\right)^{2}\right]
$$

The bracket is $N$ times the sum of squared deviations from the population mean, a standard identity obtained by expanding $\sum\left(y_i - \mu\right)^{2}$ and using $\sum y_i = N\mu$.

$$
N\sum_{i=1}^{N} y_i^{2} - \left(\sum_{i=1}^{N} y_i\right)^{2} = N\sum_{i=1}^{N}\left(y_i - \mu\right)^{2}
$$

Dividing the sum of squared deviations by $N-1$ produces $S^{2}$ and leaves the correction factor.

$$
\text{Var}\left(\bar{y}\right) = \frac{N-n}{nN}\,S^{2} = \frac{S^{2}}{n}\left(1 - \frac{n}{N}\right)
$$

The negative covariance between distinct indicators is the entire source of the correction. Each unit removed from the population reduces the pool from which later units are drawn, and that depletion is information: it is why sampling nine hundred of a thousand units is very nearly a census and sampling nine hundred of a million is not.

For the with-replacement case the draws are independent, so the cross covariances vanish and only the diagonal remains, giving $\sigma^{2}/n$ with $\sigma^{2}$ computed from the empirical distribution, that is with divisor $N$. Dividing the two variances gives the factor $\left(N-1\right)/\left(N-n\right)$ of the corollary to Theorem 4.

### 3.3 Proof of the stratified variance and of the proportional-allocation result

Independence of the samples drawn in different strata means that the covariance between any two stratum means is zero, so the variance of the weighted sum is the weighted sum of the variances.

$$
\text{Var}\left(\bar{y}_{st}\right) = \text{Var}\left(\sum_{h=1}^{H} W_h \bar{y}_h\right) = \sum_{h=1}^{H} W_h^{2}\,\text{Var}\left(\bar{y}_h\right)
$$

Each stratum mean is a simple random sample mean computed inside its own stratum, so Theorem 3 applies with $n_h$, $N_h$ and $S_h^{2}$ in place of $n$, $N$ and $S^{2}$.

$$
\text{Var}\left(\bar{y}_h\right) = \frac{S_h^{2}}{n_h}\left(1 - \frac{n_h}{N_h}\right)
$$

Substituting gives Theorem 5 immediately. For the proportional case, set $n_h = n W_h$ and note that the sampling fraction is then identical in every stratum.

$$
\frac{n_h}{N_h} = \frac{n W_h}{N_h} = \frac{n \left(N_h/N\right)}{N_h} = \frac{n}{N} = f
$$

Substituting both facts into the variance gives a single common factor and a weighted sum of stratum variances.

$$
\text{Var}_{prop}\left(\bar{y}_{st}\right) = \sum_{h=1}^{H} W_h^{2}\,\frac{S_h^{2}}{n W_h}\left(1-f\right) = \frac{1-f}{n}\sum_{h=1}^{H} W_h S_h^{2}
$$

Dividing by the variance of a simple random sample of the same size, which is $\left(1-f\right)S^{2}/n$, cancels everything except the ratio of the weighted within-variance to the total variance, which is the corollary to Theorem 6.

The result that this ratio can never exceed one follows from the decomposition of Theorem 7, because $S^{2}$ exceeds $S_w^{2}$ by the between component less a term of order $1/N$. The two variances are equal exactly when $B = 0$, that is when every stratum mean equals $\mu$.

### 3.4 Proof of the exact variance decomposition

The proof is an expansion of a single square. For a unit $i$ in stratum $h$, add and subtract the stratum mean.

$$
\left(y_{hi} - \mu\right)^{2} = \left[\left(y_{hi} - \mu_h\right) + \left(\mu_h - \mu\right)\right]^{2}
$$

Expanding the square produces a cross term that vanishes because deviations from a stratum mean sum to zero inside each stratum.

$$
\left(y_{hi} - \mu\right)^{2} = \left(y_{hi} - \mu_h\right)^{2} + 2\left(y_{hi} - \mu_h\right)\left(\mu_h - \mu\right) + \left(\mu_h - \mu\right)^{2}
$$

Summing over the $N_h$ units of stratum $h$, the middle term contains the factor $\sum_i\left(y_{hi} - \mu_h\right) = 0$.

$$
\sum_{i=1}^{N_h}\left(y_{hi} - \mu\right)^{2} = \sum_{i=1}^{N_h}\left(y_{hi} - \mu_h\right)^{2} + N_h\left(\mu_h - \mu\right)^{2}
$$

Summing over strata and using the definition of the stratum variance gives the sums-of-squares identity.

$$
\sum_{h=1}^{H}\sum_{i=1}^{N_h}\left(y_{hi} - \mu\right)^{2} = \sum_{h=1}^{H}\left(N_h - 1\right)S_h^{2} + \sum_{h=1}^{H} N_h\left(\mu_h - \mu\right)^{2}
$$

Dividing by $N-1$ and recognising $\sum_h N_h\left(\mu_h - \mu\right)^{2} = NB$ yields Theorem 7. The additive form of the corollary follows by writing $N = \left(N-1\right) + 1$ in the numerator and separating the leading terms.

### 3.5 Proof that Neyman allocation is optimal

Write the objective as a sum of terms in the reciprocal of each allocation, since the finite population parts do not contain $n_h$ and therefore cannot be optimised.

$$
V\left(n_1, \dots, n_H\right) = \sum_{h=1}^{H} \frac{W_h^{2} S_h^{2}}{n_h} - \sum_{h=1}^{H} \frac{W_h^{2} S_h^{2}}{N_h}, \qquad \sum_{h=1}^{H} n_h = n
$$

Only the first sum depends on the allocation. Apply the Cauchy–Schwarz inequality to the products $W_h S_h/\sqrt{n_h}$ and $\sqrt{n_h}$.

$$
\left(\sum_{h=1}^{H} W_h S_h\right)^{2} = \left(\sum_{h=1}^{H} \frac{W_h S_h}{\sqrt{n_h}}\cdot\sqrt{n_h}\right)^{2} \le \left(\sum_{h=1}^{H}\frac{W_h^{2}S_h^{2}}{n_h}\right)\left(\sum_{h=1}^{H} n_h\right)
$$

Dividing by $n$ gives a lower bound that does not depend on the individual allocations.

$$
\sum_{h=1}^{H}\frac{W_h^{2}S_h^{2}}{n_h} \ge \frac{1}{n}\left(\sum_{h=1}^{H} W_h S_h\right)^{2}
$$

Equality in Cauchy–Schwarz requires the two vectors to be proportional, that is $W_hS_h/\sqrt{n_h} = c\sqrt{n_h}$ for a constant $c$, which rearranges to $n_h \propto W_hS_h$.

$$
n_h = n\,\frac{W_h S_h}{\sum_{g=1}^{H} W_g S_g}
$$

Substituting the bound into the objective, together with the second sum, gives the minimum variance stated in Theorem 8. The term $-\sum_h W_h^{2}S_h^{2}/N_h$ equals $-\frac{1}{N}\sum_h W_hS_h^{2}$ because $W_h^{2}/N_h = N_h/N^{2}$, which confirms the second display of the theorem.

### 3.6 Derivation of the systematic-sampling variance

Because the start is uniform on $k$ values, the expectation and variance over the design are the average and the mean squared deviation of the $k$ possible sample means.

$$
E\left(\bar{y}_{sys}\right) = \frac{1}{k}\sum_{r=1}^{k}\bar{y}_r, \qquad \text{Var}\left(\bar{y}_{sys}\right) = \frac{1}{k}\sum_{r=1}^{k}\left(\bar{y}_r - \mu\right)^{2}
$$

The first average equals $\mu$ because each unit of the list appears in exactly one of the $k$ samples, so the $k$ sample totals sum to the population total.

$$
\sum_{r=1}^{k}\sum_{j=0}^{n-1} y_{r + jk} = \sum_{i=1}^{N} y_i = N\mu \quad \text{hence} \quad \frac{1}{k}\sum_{r=1}^{k}\bar{y}_r = \frac{N\mu}{kn} = \mu
$$

For the variance, split the list into $n$ consecutive blocks of $k$ units and write $e_{jr}$ for the deviation of the $r$-th unit of block $j$ from the block mean. Then each sample mean deviates from $\mu$ by the average of one deviation per block.

$$
\bar{y}_r - \mu = \frac{1}{n}\sum_{j=1}^{n} e_{jr}
$$

Squaring and averaging over $r$ produces a diagonal part and a cross part.

$$
\text{Var}\left(\bar{y}_{sys}\right) = \frac{1}{n^{2}}\left[\sum_{j=1}^{n}\frac{1}{k}\sum_{r=1}^{k} e_{jr}^{2} + \sum_{j \ne j'}\frac{1}{k}\sum_{r=1}^{k} e_{jr}e_{j'r}\right]
$$

The diagonal terms average to the within-block variance and the cross terms to the covariance between blocks at the same position, so writing $\sigma_w^{2}$ for the first and $\rho_w\sigma_w^{2}$ for the second gives the corollary to Theorem 9.

$$
\text{Var}\left(\bar{y}_{sys}\right) = \frac{1}{n^{2}}\left[n\sigma_w^{2} + n(n-1)\rho_w\sigma_w^{2}\right] = \frac{\sigma_w^{2}}{n}\left[1 + (n-1)\rho_w\right]
$$

The formula contains the whole of the practical advice. A list that is randomly ordered has $\rho_w \approx 0$ and the design is as good as simple random sampling. A list with a trend has $\rho_w < 0$ and the design is better. A list with period equal to the interval has $\rho_w \approx 1$ and the design is very much worse.

### 3.7 Derivation of the design effect for cluster sampling

Let the population consist of $M_c$ clusters of equal size $M$. Write $\sigma_b^{2}$ for the variance of the cluster means around $\mu$ and $\sigma_w^{2}$ for the average variance within clusters, both with divisor equal to the number of terms.

$$
\sigma^{2} = \sigma_b^{2} + \sigma_w^{2}, \qquad \rho = \frac{\sigma_b^{2}}{\sigma^{2}}
$$

With every unit of a selected cluster measured, the sample mean is the mean of the selected cluster means, so its variance under simple random sampling of clusters is the between-cluster variance divided by the number of clusters, with a correction for the fraction of clusters used.

$$
\text{Var}\left(\bar{y}_{cl}\right) = \frac{\sigma_b^{2}}{m}\left(1 - \frac{m}{M_c}\right)
$$

A simple random sample of $n = mM$ units from $N = M_cM$ units has variance given by Theorem 3.

$$
\text{Var}_{srs}\left(\bar{y}\right) = \frac{S^{2}}{n}\left(1 - \frac{n}{N}\right) \approx \frac{\sigma^{2}}{mM}\left(1 - \frac{m}{M_c}\right)
$$

The correction factors cancel between the two variances, so the design effect is the ratio of the between-cluster variance to one $M$-th of the total variance.

$$
\text{deff} = \frac{\sigma_b^{2}/m}{\sigma^{2}/(mM)} = \frac{M\sigma_b^{2}}{\sigma^{2}} = M\rho
$$

The approximation lies in the treatment of the between-cluster variance of sample means, which in a finite population also contains a within-cluster term equal to $\sigma_w^{2}/M$. Inserting that term replaces $M\rho$ by a ratio whose numerator is $M\sigma_b^{2} + \sigma_w^{2}$.

$$
\text{deff} = \frac{M\sigma_b^{2} + \sigma_w^{2}}{\sigma_b^{2} + \sigma_w^{2}} = 1 + (M-1)\frac{\sigma_b^{2}}{\sigma^{2}} = 1 + (M-1)\rho
$$

The two special cases confirm the algebra. With $\rho = 0$ every cluster has the same mean and the design effect is one, so measuring more units inside a cluster is as valuable as measuring new clusters. With $\rho = 1$ every cluster is internally constant and the design effect is $M$, so only the number of clusters matters.

### 3.8 Derivation of the two-stage variance

The variance is obtained by conditioning on the set of primary units selected, using the law of total variance.

$$
\text{Var}\left(\bar{y}\right) = E\left[\text{Var}\left(\bar{y} \mid s_1\right)\right] + \text{Var}\left[E\left(\bar{y} \mid s_1\right)\right]
$$

Conditional on the selected primary units, the estimator is the average of $m$ independent sub-sample means, so its conditional variance follows from the within-unit variance.

$$
\text{Var}\left(\bar{y} \mid s_1\right) = \frac{1}{m^{2}}\sum_{j \in s_1}\frac{\bar{S}_{2j}^{2}}{b}\left(1 - f_2\right) \approx \frac{1-f_2}{mb}\bar{S}_2^{2}
$$

Taking the expectation over the first stage replaces the average of the unit variances by their population average. For the second term, the conditional expectation is the average of the selected primary-unit means, whose variance is given by Theorem 3 applied at the primary stage.

$$
E\left(\bar{y} \mid s_1\right) = \frac{1}{m}\sum_{j \in s_1}\mu_j, \qquad \text{Var}\left[E\left(\bar{y} \mid s_1\right)\right] = \frac{1-f_1}{m}S_1^{2}
$$

Adding the two terms gives Theorem 12. The corollary on the optimum number of secondary units follows by minimising the variance subject to a budget $C = c_1 m + c_2 mb$, which after substitution gives an objective linear in $b$ and in $1/b$, whose minimum occurs where the two terms balance.

$$
b_{opt} = \sqrt{\frac{\bar{S}_2^{2}\,c_1}{S_1^{2}\,c_2}}
$$

### 3.9 Derivation of the sample size formulas

Set the margin of error equal to the target and solve for the sample size, starting from the standard error of Theorem 3.

$$
e = z\sqrt{\frac{S^{2}}{n}\left(1 - \frac{n}{N}\right)}
$$

Squaring and expanding separates the terms in $n$.

$$
e^{2} = \frac{z^{2}S^{2}}{n} - \frac{z^{2}S^{2}}{N}
$$

Isolating $n$ gives a ratio whose numerator is the infinite-population sample size.

$$
n = \frac{z^{2}S^{2}}{e^{2} + \dfrac{z^{2}S^{2}}{N}} = \frac{n_0}{1 + \dfrac{n_0}{N}}
$$

For a proportion, replace $S^{2}$ by $p(1-p)$; the variance of an indicator is exactly $p(1-p)$ when computed with divisor $N$, and the refined correction $n_0 - 1$ follows from using the unbiased variance estimate $p(1-p)n/(n-1)$. The maximisation of $n_0$ over $p$ is immediate from the shape of the function.

$$
\frac{d}{dp}\,p(1-p) = 1 - 2p = 0 \quad \text{at} \quad p = 0.5, \qquad p(1-p) \le 0.25
$$

### 3.10 Proof of the non-response identity and of the Horvitz–Thompson theorem

For the non-response identity, split the eligible sample into respondents and non-respondents and apply the weighted-mean lemma.

$$
\bar{y} = w_r \bar{y}_r + w_n \bar{y}_n, \qquad w_r + w_n = 1
$$

Subtracting the respondent mean from both sides and substituting $w_r = 1 - w_n$ gives the identity after collection of terms.

$$
\bar{y} - \bar{y}_r = \left(1 - w_n\right)\bar{y}_r + w_n\bar{y}_n - \bar{y}_r = w_n\left(\bar{y}_n - \bar{y}_r\right)
$$

Multiplying by minus one produces Theorem 15. The proof shows that the bias vanishes if either factor vanishes, and that neither factor can be estimated without information about the non-respondents themselves, which is why a non-response follow-up study is the only direct remedy.

For the Horvitz–Thompson theorem, write the estimator as a sum over the whole population with selection indicators.

$$
\hat{Y}_{HT} = \sum_{i \in s}\frac{y_i}{\pi_i} = \sum_{i=1}^{N} I_i \frac{y_i}{\pi_i}
$$

Taking expectations and using $E\left(I_i\right) = \pi_i$ gives the total immediately.

$$
E\left(\hat{Y}_{HT}\right) = \sum_{i=1}^{N}\frac{y_i}{\pi_i}E\left(I_i\right) = \sum_{i=1}^{N}\frac{y_i}{\pi_i}\pi_i = \sum_{i=1}^{N} y_i = Y
$$

The proof requires only that every $\pi_i$ be strictly positive, so that no unit is impossible to select and no division by zero occurs. A design that excludes part of the population violates that condition, and no weighting can repair it, which is the formal statement of the coverage requirement.

## 4. Representative Worked Examples and Solutions

### 4.1 Problem: simple random sampling with and without replacement

A register lists 1200 households. A sample of 120 is required, and the population variance of monthly expenditure is 2500 square units. Compare the inclusion probabilities, the estimation variance and the standard error under sampling without replacement and under sampling with replacement.

### 4.2 Solution: probabilities, variances and comparison

Step 1. Compute the inclusion probability under sampling without replacement.

$$
\pi_i = \frac{n}{N} = \frac{120}{1200} = 0.1
$$

Step 2. Compute the probability that a given household appears at least once when the 120 draws are made with replacement.

$$
1 - \left(1 - \frac{1}{1200}\right)^{120} = 1 - 0.9048 = 0.0952
$$

Step 3. Compute the sampling fraction and the finite population correction.

$$
f = 0.1, \qquad 1 - f = 0.9
$$

Step 4. Compute the variance without replacement.

$$
\text{Var}_{WOR}\left(\bar{y}\right) = \frac{2500}{120}\left(0.9\right) = 20.8333\left(0.9\right) = 18.7500
$$

Step 5. Compute the standard error without replacement.

$$
\text{SE}_{WOR} = \sqrt{18.7500} = 4.3301
$$

Step 6. Compute the variance and standard error with replacement, using $\sigma^{2} = \frac{1199}{1200}\left(2500\right) = 2497.92$.

$$
\text{Var}_{WR}\left(\bar{y}\right) = \frac{2497.92}{120} = 20.8160, \qquad \text{SE}_{WR} = 4.5625
$$

Step 7. Compare the two designs.

$$
\frac{\text{Var}_{WR}}{\text{Var}_{WOR}} = \frac{20.8160}{18.7500} = 1.1102
$$

Step 8. Interpret. Sampling without replacement reduces the variance by 9.9 per cent and the standard error by 5.1 per cent, because the correction factor is 0.9. Replacement also carries a probability of about 0.0046 that a household is drawn more than once, computed as the difference between the two inclusion probabilities of 0.1 and 0.0952, so it wastes interviews as well as precision. The only reason to sample with replacement is administrative convenience, as when units are selected from a flowing population in which the same unit may legitimately recur.

### 4.3 Problem: the exact decomposition and the gain from proportional allocation

A trading population of 1000 businesses is divided into three strata. Stratum 1 holds 500 businesses with variance 64 and mean 100; stratum 2 holds 300 with variance 144 and mean 120; stratum 3 holds 200 with variance 400 and mean 150. A sample of 100 is allocated in proportion to stratum size. Compute the exact population variance, the variance of the stratified estimate, the variance of a simple random sample of the same size, and the proportional reduction in variance.

### 4.4 Solution: decomposition, variances and reduction

Step 1. Compute the stratum weights.

$$
W_1 = 0.5, \qquad W_2 = 0.3, \qquad W_3 = 0.2
$$

Step 2. Compute the population mean as the weighted average of the stratum means.

$$
\mu = 0.5(100) + 0.3(120) + 0.2(150) = 50 + 36 + 30 = 116
$$

Step 3. Compute the between-stratum variance.

$$
B = 0.5\left(100-116\right)^{2} + 0.3\left(120-116\right)^{2} + 0.2\left(150-116\right)^{2}
$$

$$
B = 0.5(256) + 0.3(16) + 0.2(1156) = 128 + 4.8 + 231.2 = 364.0
$$

Step 4. Compute the weighted within-stratum variance.

$$
S_w^{2} = 0.5(64) + 0.3(144) + 0.2(400) = 32 + 43.2 + 80 = 155.2
$$

Step 5. Apply Theorem 7 exactly, using $\sum_h\left(N_h-1\right)S_h^{2} = 499(64) + 299(144) + 199(400)$.

$$
\sum_h\left(N_h-1\right)S_h^{2} = 31936 + 43056 + 79600 = 154592
$$

$$
S^{2} = \frac{154592 + 1000(364.0)}{999} = \frac{154592 + 364000}{999} = \frac{518592}{999} = 519.111
$$

Step 6. Compare with the additive approximation of the corollary.

$$
S_w^{2} + B = 155.2 + 364.0 = 519.2, \qquad \text{error} = 519.2 - 519.111 = 0.089
$$

Step 7. Compute the proportional allocation with $n = 100$.

$$
n_1 = 50, \qquad n_2 = 30, \qquad n_3 = 20
$$

Step 8. Compute the common sampling fraction and the factor multiplying the weighted within-variance.

$$
f = \frac{100}{1000} = 0.1, \qquad \frac{1-f}{n} = \frac{0.9}{100} = 0.009
$$

Step 9. Compute the variance and standard error of the stratified estimate.

$$
\text{Var}_{prop}\left(\bar{y}_{st}\right) = 0.009(155.2) = 1.3968, \qquad \text{SE} = 1.1819
$$

Step 10. Compute the variance and standard error of a simple random sample of 100.

$$
\text{Var}_{srs}\left(\bar{y}\right) = 0.009(519.111) = 4.6720, \qquad \text{SE} = 2.1615
$$

Step 11. Compute the ratio and the percentage reduction.

$$
\frac{1.3968}{4.6720} = 0.2990, \qquad \text{reduction} = 70.1\ \text{per cent}
$$

Step 12. Interpret. Seventy per cent of the total variance lies between strata, since $B/S^{2} = 364.0/519.111 = 0.701$, and proportional allocation removes exactly that share. The stratified sample of 100 therefore behaves like a simple random sample of about 334, obtained by dividing 100 by 0.2990. The gain is large only because the stratum means are far apart; if the three means had been equal, $B$ would have been zero and the design would have bought nothing.

### 4.5 Problem: comparing proportional, equal and optimum allocation

Two strata contain 600 and 400 businesses with standard deviations 12 and 20. A total of 200 interviews is available. Compare the variance of the estimated mean under proportional allocation, equal allocation, and Neyman allocation.

### 4.6 Solution: three allocations and their variances

Step 1. Record the weights and the variance components that depend on the population only.

$$
W_1 = 0.6, \qquad W_2 = 0.4, \qquad W_1^{2}S_1^{2} = 51.84, \qquad W_2^{2}S_2^{2} = 64.00
$$

Step 2. Compute the finite population terms, which are the same for every allocation because they do not involve $n_h$.

$$
\sum_h \frac{W_h^{2}S_h^{2}}{N_h} = \frac{51.84}{600} + \frac{64.00}{400} = 0.0864 + 0.1600 = 0.2464
$$

Step 3. Compute the proportional allocation.

$$
n_1 = 0.6(200) = 120, \qquad n_2 = 0.4(200) = 80
$$

$$
\text{Var}_{prop} = \frac{51.84}{120} + \frac{64.00}{80} - 0.2464 = 0.4320 + 0.8000 - 0.2464 = 0.9856
$$

Step 4. Compute the equal allocation.

$$
n_1 = n_2 = 100
$$

$$
\text{Var}_{eq} = \frac{51.84}{100} + \frac{64.00}{100} - 0.2464 = 0.5184 + 0.6400 - 0.2464 = 0.9120
$$

Step 5. Compute the Neyman allocation from the products $N_hS_h$, which are 7200 and 8000.

$$
n_1 = 200\,\frac{7200}{15200} = 94.74, \qquad n_2 = 200\,\frac{8000}{15200} = 105.26
$$

Step 6. Compute the variance under Neyman allocation.

$$
\text{Var}_{opt} = \frac{51.84}{94.74} + \frac{64.00}{105.26} - 0.2464 = 0.5472 + 0.6080 - 0.2464 = 0.9088
$$

Step 7. Verify against the closed form of Theorem 8, using $\sum_h W_hS_h = 7.2 + 8.0 = 15.2$.

$$
\text{Var}_{opt} = \frac{\left(15.2\right)^{2}}{200} - 0.2464 = \frac{231.04}{200} - 0.2464 = 1.1552 - 0.2464 = 0.9088
$$

Step 8. Rank the three designs and state the standard errors.

$$
\text{Var}_{opt} = 0.9088 < \text{Var}_{eq} = 0.9120 < \text{Var}_{prop} = 0.9856
$$

$$
\text{SE}_{opt} = 0.9533, \qquad \text{SE}_{eq} = 0.9550, \qquad \text{SE}_{prop} = 0.9928
$$

Step 9. Interpret. Neyman allocation is best, as the theorem guarantees, but the advantage over equal allocation is negligible here because the two strata differ only modestly in standard deviation. The gain over proportional allocation is 7.8 per cent of the variance, which is typical when stratum variability differs by a factor of less than two. Neyman allocation becomes valuable when one stratum is far more variable than the others, since it then directs interviews to where the information lies. In practice the allocation must be rounded to whole interviews, and the rounded figures 95 and 105 reproduce the variance to four decimal places.

### 4.7 Problem: systematic sampling on a trended and on a periodic list

A list of 12 units is sampled systematically with interval 3, giving four units. Case one uses the values 1 to 12 in order. Case two uses the repeating pattern 0, 0, 9, 0, 0, 9, 0, 0, 9, 0, 0, 9. For each case compute the population mean, the three possible sample means, the variance over the random start, and the variance of a simple random sample of four.

### 4.8 Solution: two lists, two very different designs

Step 1. For the first list compute the population mean and variance.

$$
\mu = 6.5, \qquad S^{2} = \frac{1}{11}\left(2\sum_{j=1}^{6}\left(j - 0.5\right)^{2}\right) = \frac{143}{11} = 13.0
$$

Step 2. Enumerate the three systematic samples for the first list and their means.

$$
r=1: \ 1,4,7,10 \ \Rightarrow \ \bar{y} = 5.5; \qquad r=2: \ 2,5,8,11 \ \Rightarrow \ 6.5; \qquad r=3: \ 3,6,9,12 \ \Rightarrow \ 7.5
$$

Step 3. Compute the variance over the random start for the first list.

$$
\text{Var}_{sys} = \frac{1}{3}\left[\left(5.5-6.5\right)^{2} + 0 + \left(7.5-6.5\right)^{2}\right] = \frac{2}{3} = 0.6667
$$

Step 4. Compute the variance of a simple random sample of four from the first list.

$$
\text{Var}_{srs} = \frac{13.0}{4}\left(1 - \frac{4}{12}\right) = 3.25\left(0.6667\right) = 2.1667
$$

Step 5. For the second list compute the population mean and variance, noting that four of the twelve units take the value 9 and eight take the value 0.

$$
\mu = \frac{4(9)}{12} = 3.0, \qquad S^{2} = \frac{8(9) + 4(36)}{11} = \frac{216}{11} = 19.6364
$$

Step 6. Enumerate the three systematic samples for the second list.

$$
r=1: \ 0,0,0,0 \ \Rightarrow \ 0; \qquad r=2: \ 0,0,0,0 \ \Rightarrow \ 0; \qquad r=3: \ 9,9,9,9 \ \Rightarrow \ 9
$$

Step 7. Compute the variance over the random start for the second list.

$$
\text{Var}_{sys} = \frac{1}{3}\left[\left(0-3\right)^{2} + \left(0-3\right)^{2} + \left(9-3\right)^{2}\right] = \frac{9 + 9 + 36}{3} = 18.0
$$

Step 8. Compute the variance of a simple random sample of four from the second list.

$$
\text{Var}_{srs} = \frac{19.6364}{4}\left(0.6667\right) = 3.2727
$$

Step 9. Compare the two cases with the design effect of systematic sampling.

$$
\text{deff}_{1} = \frac{0.6667}{2.1667} = 0.308, \qquad \text{deff}_{2} = \frac{18.0}{3.2727} = 5.500
$$

Step 10. Interpret. On a list that trends steadily upwards, systematic sampling is three times as precise as simple random sampling, because each systematic sample spans the whole range of the list and therefore cannot be unrepresentative. On a list with a cycle of length equal to the interval, the design is five and a half times worse, and two of the three possible samples contain only zeros. Both designs remain unbiased over the random start, but the periodic case produces samples whose internal spread is zero and whose mean is wrong by six units, so no variance estimate computed from the sample can detect the failure. The remedy is to randomise the order of the list before sampling, or to use several random starts with a smaller interval.

### 4.9 Problem: a two-stage design and the choice of subsample size

A school survey covers 900 schools with 400 pupils each. Thirty schools are selected and twenty pupils are interviewed in each. The variance between school means is 400 and the average variance within schools is 2500. Compute the variance and standard error, then recompute with sixty schools and ten pupils each, and find the optimum number of pupils per school if a school visit costs 500 units and each pupil interview costs 4 units.

### 4.10 Solution: two-stage variance and optimal subsampling

Step 1. Compute the first-stage sampling fraction and its correction.

$$
f_1 = \frac{30}{900} = 0.0333, \qquad 1 - f_1 = 0.9667
$$

Step 2. Compute the second-stage correction.

$$
f_2 = \frac{20}{400} = 0.05, \qquad 1 - f_2 = 0.95
$$

Step 3. Compute the two variance components for the first design.

$$
\frac{1-f_1}{m}S_1^{2} = \frac{0.9667(400)}{30} = 12.889
$$

$$
\frac{1-f_2}{mb}\bar{S}_2^{2} = \frac{0.95(2500)}{30(20)} = \frac{2375}{600} = 3.958
$$

Step 4. Add the components and take the square root.

$$
\text{Var} = 12.889 + 3.958 = 16.847, \qquad \text{SE} = 4.104
$$

Step 5. Recompute for sixty schools and ten pupils, keeping the total of 600 interviews.

$$
\frac{0.9333(400)}{60} = 6.222, \qquad \frac{0.975(2500)}{600} = 4.063
$$

$$
\text{Var} = 6.222 + 4.063 = 10.285, \qquad \text{SE} = 3.207
$$

Step 6. Compute the optimum number of pupils per school from the corollary to Theorem 12.

$$
b_{opt} = \sqrt{\frac{2500(500)}{400(4)}} = \sqrt{\frac{1250000}{1600}} = \sqrt{781.25} = 27.95
$$

Step 7. Interpret. Redistributing the same 600 interviews towards more schools reduces the variance by 39 per cent, because the first component is three times the second and the first component falls with the number of schools. The optimum subsample of about 28 pupils per school is larger than the 20 actually used, which means that at these costs the survey was under-sampling inside schools and over-sampling schools. The two recommendations are consistent because the total number of interviews differs: for a fixed budget the optimum ratio is 28 pupils per school, while for a fixed number of interviews the best choice is to spread them over many schools. A designer must therefore state which constraint is binding before recommending an allocation.

### 4.11 Problem: sample sizes for a mean and for a proportion

A survey must estimate mean weekly expenditure within 2 units at 95 per cent confidence, with a standard deviation of 15, in a population of 600 households. A second objective is to estimate the proportion using a service within 0.035, with a prior guess of 0.3, in a population of 2000 households. Find both sample sizes and verify the margins of error.

### 4.12 Solution: two sample-size calculations with verification

Step 1. Compute the infinite-population sample for the mean, with $z^{2} = 3.8416$.

$$
n_0 = \frac{3.8416(225)}{4} = \frac{864.36}{4} = 216.09
$$

Step 2. Apply the finite population correction.

$$
n = \frac{216.09}{1 + \dfrac{216.09}{600}} = \frac{216.09}{1.36015} = 158.87
$$

Step 3. Round up and verify.

$$
n = 159, \qquad \text{SE} = \sqrt{\frac{225}{159}\left(1 - \frac{159}{600}\right)} = \sqrt{1.41509(0.73500)} = 1.0199
$$

$$
1.96(1.0199) = 1.999 \le 2
$$

Step 4. Confirm that the integer below would fail.

$$
n = 158: \quad \text{SE} = \sqrt{\frac{225}{158}(0.73667)} = 1.0241, \qquad 1.96(1.0241) = 2.007 > 2
$$

Step 5. Compute the infinite-population sample for the proportion.

$$
n_0 = \frac{3.8416(0.3)(0.7)}{0.001225} = \frac{0.806736}{0.001225} = 658.56
$$

Step 6. Apply the finite population correction.

$$
n = \frac{658.56}{1 + \dfrac{657.56}{2000}} = \frac{658.56}{1.32878} = 495.61
$$

Step 7. Round up and verify.

$$
n = 496, \qquad 1.96\sqrt{\frac{0.21}{496}\left(1 - \frac{496}{2000}\right)} = 1.96\sqrt{0.00042339(0.75200)} = 0.03497 \le 0.035
$$

Step 8. Confirm that 495 fails.

$$
495: \quad 1.96\sqrt{\frac{0.21}{495}(0.75250)} = 1.96(0.017867) = 0.03502 > 0.035
$$

Step 9. Interpret. The corrections removed 57 households from the first plan and 163 from the second, and the second saving is much the larger because the uncorrected sample of 659 would have been a third of a population of 2000. Both checks confirm that the rounded-up value meets the specification while the integer below it does not, and that verification is the only way to be sure the rounding went the right way. Note also that a prior guess of $p$ closer to 0.5 would have increased the requirement, since $p(1-p)$ is maximised at one half.

### 4.13 Problem: the Horvitz–Thompson estimator with unequal probabilities

Three shops have sales of 40, 60 and 100 units in a period, so the population total is 200. A design selects exactly one shop, with probabilities 0.5, 0.3 and 0.2. Compute the estimator for each possible outcome, verify unbiasedness, and compute the variance.

### 4.14 Solution: weights, expectation and variance

Step 1. Compute the weight of each shop as the reciprocal of its inclusion probability.

$$
\frac{1}{\pi_1} = 2, \qquad \frac{1}{\pi_2} = 3.3333, \qquad \frac{1}{\pi_3} = 5
$$

Step 2. Compute the estimate produced by each possible outcome.

$$
\hat{Y}_1 = 2(40) = 80, \qquad \hat{Y}_2 = 3.3333(60) = 200, \qquad \hat{Y}_3 = 5(100) = 500
$$

Step 3. Verify unbiasedness by weighting each estimate by its probability.

$$
E\left(\hat{Y}_{HT}\right) = 0.5(80) + 0.3(200) + 0.2(500) = 40 + 60 + 100 = 200
$$

Step 4. Verify that the sum of the inclusion probabilities equals the expected sample size.

$$
0.5 + 0.3 + 0.2 = 1.0
$$

Step 5. Compute the second moment of the estimator.

$$
E\left(\hat{Y}_{HT}^{2}\right) = 0.5(6400) + 0.3(40000) + 0.2(250000) = 3200 + 12000 + 50000 = 65200
$$

Step 6. Compute the variance and standard error of the estimator.

$$
\text{Var}\left(\hat{Y}_{HT}\right) = 65200 - 200^{2} = 65200 - 40000 = 25200, \qquad \text{SE} = 158.7
$$

Step 7. Compute the naive unweighted estimate if the sampling were ignored, which would be the value of the selected shop alone.

$$
\text{bias if unweighted} = E\left(y_{s}\right) - Y = \left[0.5(40) + 0.3(60) + 0.2(100)\right] - 200 = 58 - 200 = -142
$$

Step 8. Interpret. The weighted estimator is exactly unbiased, and the weights are large for the shop that is hard to select, which is correct because that shop stands for five units of the population. Ignoring the design and simply reporting the selected shop's sales would understate the total by 142 units on average, which is a 71 per cent error. The variance is large because a single draw from a population with widely differing weights is a crude design, and increasing the number of draws is what reduces it.

### 4.15 Problem: non-response bias and the corrected estimate

A survey approaches 800 households and obtains 560 responses. The respondent mean is 46.2. A follow-up study of 60 non-respondents gives a mean of 58.6, which is taken as representative of all non-respondents. Estimate the bias of the naive respondent mean, the corrected population mean, and the number of households that must be approached to obtain 400 responses at the observed rate.

### 4.16 Solution: weights, bias and planning

Step 1. Compute the response rate and the weight of the non-respondents.

$$
w_r = \frac{560}{800} = 0.70, \qquad w_n = 1 - 0.70 = 0.30
$$

Step 2. Compute the corrected mean as the weighted average of the two group means.

$$
\bar{y} = 0.70(46.2) + 0.30(58.6) = 32.34 + 17.58 = 49.92
$$

Step 3. Compute the bias of the naive respondent mean from the identity of Theorem 15.

$$
\bar{y}_r - \bar{y} = 0.30\left(46.2 - 58.6\right) = 0.30\left(-12.4\right) = -3.72
$$

Step 4. Confirm the two calculations agree.

$$
46.2 - 49.92 = -3.72
$$

Step 5. Compute the number to approach for 400 responses.

$$
n_{\text{approach}} = \frac{400}{0.70} = 571.4 \quad \text{so} \quad 572
$$

Step 6. Express the bias as a share of the corrected mean.

$$
\frac{3.72}{49.92} = 0.0745, \quad \text{that is } 7.5\ \text{per cent}
$$

Step 7. Interpret. The naive estimate understates the population mean by 3.7 units, or 7.5 per cent, and no increase in the number of respondents would remove that error, because the error is a product of the 30 per cent who did not respond and the 12.4-unit difference between the groups. The corrected figure depends on the assumption that the 60 followed-up non-respondents represent the remaining 240, an assumption that must be stated. Weighting to the known population structure is the practical alternative when the respondents can be classified by variables whose population distribution is known.

## 5. Mathematical Extensions, Limits, and Common Errors

### 5.1 Limits of the standard formulas

The formulas have well-defined limits that clarify what each quantity controls. As the sample becomes a vanishing share of the population, the finite population correction tends to one and every design reduces to its infinite-population form.

$$
\lim_{n/N \to 0}\frac{S^{2}}{n}\left(1 - \frac{n}{N}\right) = \frac{S^{2}}{n}
$$

As the sample approaches the whole population, the variance of a simple random sample mean falls to zero, while the variance of a stratified mean with fixed allocations per stratum does not, unless the allocations themselves grow in proportion to the stratum sizes. A design in which each stratum contributes a fixed number of units regardless of its size has a variance floor, and that floor is reached when the within-stratum sampling fractions approach one.

$$
\lim_{n_h \to N_h}\text{Var}\left(\bar{y}_{st}\right) = 0 \quad \text{only if } n_h/N_h \to 1 \text{ in every stratum}
$$

The design effect has two instructive limits in the cluster case. As the intra-cluster correlation tends to zero the design effect tends to one and clustering becomes free, while as the correlation tends to one the design effect tends to the cluster size and the sample carries the information of one unit per cluster.

$$
\lim_{\rho \to 0}\left[1 + (M-1)\rho\right] = 1, \qquad \lim_{\rho \to 1}\left[1 + (M-1)\rho\right] = M
$$

Finally, the ratio of stratified to simple random variance is bounded above by one under proportional allocation once the strata are of appreciable size, so stratification is a one-sided improvement. Under arbitrary allocation the ratio can exceed one, which is the formal statement that a badly allocated stratified sample is worse than no stratification at all.

### 5.2 Cost-weighted allocation and its relation to optimum allocation

When the constraint is a budget rather than a number of interviews, the cost of interviewing differs between strata and the optimum changes. Minimising the variance subject to $\sum_h c_h n_h = C$ gives an allocation proportional to $W_hS_h/\sqrt{c_h}$ rather than to $W_hS_h$.

$$
n_h \propto \frac{W_h S_h}{\sqrt{c_h}}
$$

The corresponding minimum variance for a fixed budget is stated compactly in terms of the two weighted sums.

$$
V_{cost} = \frac{1}{C}\left(\sum_{h=1}^{H} W_h S_h \sqrt{c_h}\right)\left(\sum_{h=1}^{H}\frac{W_h S_h}{\sqrt{c_h}}\right) - \frac{1}{N}\sum_{h=1}^{H} W_h S_h^{2}
$$

The distinction between the two problems matters in examinations. If the question fixes the total sample size, Neyman allocation is the answer and cost is irrelevant to the allocation, though it remains relevant to feasibility. If the question fixes the budget, the square-root-of-cost allocation is the answer. Applying the budget formula to a fixed sample size produces an allocation that is feasible but not optimal, and applying the Neyman formula to a fixed budget may produce a plan that cannot be afforded.

### 5.3 When a design gains nothing

Three situations deserve separate statement because they are commonly asserted to be improvements when they are not. Stratification gains nothing when the stratification variable is unrelated to the study variable, since the between-stratum component is then zero and the ratio of variances is one. Clustering costs nothing when the intra-cluster correlation is zero, which occurs when the variable of interest is generated within units rather than shared between them, as with an individually administered examination mark in schools that are otherwise similar. Systematic sampling costs nothing and gains nothing when the list is in random order, in which case it is merely a convenient way of drawing a simple random sample.

The converse statements are equally useful. Stratification gains most when the strata are internally homogeneous and far apart, which is why geographic and administrative strata are effective for expenditure variables. Clustering costs most when the variable is a shared characteristic of the cluster, such as the water supply of a village or the teacher of a class. Systematic sampling gains most when the list is ordered by a variable correlated with the study variable, which is the case for lists ordered by size, by date, or by geographic sequence.

### 5.4 Common errors in derivation and in reporting

The errors below are the ones that most often cost marks or, in practice, produce a wrong published figure.

- **Using the wrong divisor for the population variance.** The formulas of Theorems 3 and 5 require the $N-1$ convention. Mixing in an $N$-divisor variance shifts every subsequent number and breaks the identity $S^{2} = S_w^{2} + B$.
- **Forgetting the finite population correction.** The error is negligible when the sample is under a tenth of the population and serious when it is over a quarter. A candidate who omits the correction for a sample of half the population overstates the standard error by 41 per cent.
- **Applying the correction to a stratified design as if the fractions were equal.** The correction must be applied stratum by stratum unless proportional allocation guarantees a common fraction.
- **Computing the stratum allocation and not checking that it sums to the sample size.** Rounding each allocation independently breaks the total, and the check is a marking point.
- **Confusing the design effect with a bias correction.** The design effect inflates the variance of an unbiased estimator; it does not remove the bias of a clustered convenience sample.
- **Reporting the number of observation units as the sample size in a cluster survey.** The effective sample size is the number of clusters divided by the design effect in the limiting case, and in general the number of independent pieces of information is far below the number of interviews.
- **Rounding a sample size down.** Every sample-size formula returns a number that must be rounded upwards, and a verification of the margin of error at the chosen integer is the only way to confirm it.
- **Treating a response rate as a measure of quality.** The bias is the product of the missing share and the difference between respondents and non-respondents, so a high rate can coexist with a large bias and a low rate with a small one.
- **Assuming that a larger sample repairs coverage.** No sample size repairs a frame that omits a subgroup, because the omitted units have zero inclusion probability and the Horvitz–Thompson weights do not exist for them.
- **Using the systematic variance formula for a random sample.** The formula $\left(1-f\right)S^{2}/n$ applies to simple random sampling. For an ordered list it can understate the variance by a factor of five or more, as the periodic case of the worked example shows.
- **Interpreting a standard error as a range for the parameter.** The standard error describes the estimator over repeated samples; a statement about the parameter requires a confidence interval with a stated level.
- **Quoting a variance without stating the design.** Every variance in this topic is conditional on a design, and a figure without a design is meaningless.

### 5.5 Synthesis

The theory has a single spine. A design assigns inclusion probabilities; the Horvitz–Thompson theorem converts those probabilities into an unbiased estimator; the variance of that estimator is computed from second-order inclusion probabilities, which under simple random sampling reduce to the finite population correction. Every named design is a statement about how the inclusion probabilities are generated, and every variance formula is the general expression evaluated at those probabilities.

Stratification fixes the inclusion probabilities within strata and thereby deletes the between-stratum component of variance, leaving the within component as the only source of sampling error; the size of the deletion is the between share. Optimum allocation then distributes the fixed sample across strata in proportion to the information each stratum carries, which is its size multiplied by its standard deviation. Systematic sampling fixes the inclusion probabilities by position, so its variance depends on the order of the list and is governed by the correlation between units at the sampling interval. Cluster sampling assigns equal inclusion probabilities to units within a cluster, so all the information about the mean is carried by the number of clusters and by how much clusters differ from one another; the design effect measures the price exactly. Multistage sampling combines the last two ideas by allowing both the number of primary units and the number within each to vary, and the two variance components show which of the two choices matters more.

Sample size formulas are inversions of the variance formulas and inherit their structure: a variance divided by the target squared precision, corrected for the fraction of the population used. Non-response and coverage enter as biases rather than as variances and therefore do not appear in those formulas at all, which is precisely why a survey can be planned to a stated precision and still produce a wrong answer.
