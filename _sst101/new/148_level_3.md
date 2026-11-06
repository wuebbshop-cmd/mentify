## 1. Foundational Concepts, Definitions, and Axioms

### 1.1 What this topic asks you to do

Questions on sampling are rarely about isolated formulas. They present a scenario, sometimes two pages of it, and ask a small number of standard things: name the design, justify the name, compute an allocation or an interval, compute a variance or a standard error, compute a sample size, and comment on the weakness of the design. Every one of those tasks has a fixed answer shape, and the marks are awarded for the shape as much as for the arithmetic.

The scenarios fall into a small number of patterns. One pattern describes a list and a mechanical selection rule and asks for the interval, the start and the selected positions. A second describes a population already divided into groups and asks how many units to take from each, then whether the design is stratified or clustered. A third gives a variance, a margin of error and a population size and asks for the sample size. A fourth gives a response rate and a difference between respondents and non-respondents and asks for the bias. A fifth describes a survey already carried out and asks what its sample size is really worth once clustering is allowed for.

The five core designs are simple random, stratified, systematic, cluster and convenience sampling, but a full answer also needs the vocabulary of the wider subject: the sampling frame, the sampling unit, inclusion probability, proportional and optimum allocation, the design effect, multistage sampling, quota and snowball sampling, and the distinction between sampling and non-sampling error. A candidate who knows only the five definitions can answer at most a third of the available marks.

### 1.2 The definitions, in the wording that earns marks

> **Definition (Population).** The population is the complete set of units about which a conclusion is required, and it is fixed by the research question rather than by geography.

> **Definition (Sampling frame).** The sampling frame is the list, register, map or procedure from which the sample is drawn, and it is the operational version of the population.

> **Definition (Sampling unit).** The sampling unit is the entity that the selection rule chooses, and it may be a group even when the measurements are taken on individuals inside the group.

> **Definition (Observation unit).** The observation unit is the entity on which the measurement is taken.

> **Definition (Simple random sampling).** Every unit has an equal chance of selection and every possible sample of size $n$ has an equal chance of being the sample obtained.

> **Definition (Stratified sampling).** The population is divided into non-overlapping strata that are internally similar, and an independent sample is drawn inside every stratum.

> **Definition (Systematic sampling).** The units are listed in an order, a random start is taken among the first $k$ positions, and every $k$-th unit thereafter is selected.

> **Definition (Cluster sampling).** The population is divided into groups, a sample of whole groups is selected, and every unit in each selected group is measured.

> **Definition (Convenience sampling).** Units are selected because they are accessible or willing, with no chance mechanism and therefore no known selection probability.

> **Definition (Quota sampling).** Fixed numbers of respondents are required in each category, and interviewers choose respondents to fill those numbers, so the composition is controlled but the selection inside each category is not.

> **Definition (Judgement sampling).** Units are chosen because the investigator considers them typical or informative.

> **Definition (Snowball sampling).** Respondents are asked to nominate further respondents, so that the sample grows along social links from an initial accessible group.

> **Definition (Sampling error).** Sampling error is the deviation of an estimate from the parameter that arises solely because a subset rather than the whole population was measured.

> **Definition (Non-sampling error).** Non-sampling error is every other deviation, including coverage error, non-response error, measurement error and processing error.

Two definitions usually decide a classification question. The first is the sampling unit: if the randomisation chooses groups, the design is clustered however the measurements are described. The second is whether every group contributes: if every group contributes a sample, the design is stratified, and if only some groups contribute, it is clustered.

### 1.3 Signal words in the question

Examiners rarely name the design they want. They describe a procedure, and the description contains a phrase that identifies it. The mapping below is the fastest route to the correct name.

| Phrase in the question | Design it signals |
| --- | --- |
| "every household has an equal chance" | simple random |
| "drawn from a table of random digits" | simple random |
| "the town is divided into three income areas and a sample is taken from each" | stratified |
| "proportional to the number of businesses in each district" | stratified, proportional allocation |
| "every tenth house after a random start" | systematic |
| "the register is in alphabetical order and every fiftieth name is taken" | systematic |
| "twenty villages are chosen and every household in those villages is interviewed" | cluster |
| "all pupils in the selected classes are tested" | cluster |
| "schools are chosen, then classes within schools, then pupils within classes" | multistage |
| "whoever was available at the market on the day" | convenience |
| "interviewers were told to obtain fifty men and fifty women" | quota |
| "the sample was restricted to the ten largest firms" | judgement |
| "each respondent was asked to name two others" | snowball |

When the wording mentions groups, the deciding question is whether all groups are used or only some. If every group contributes, the design is stratified even when the word "group" rather than "stratum" appears. If some groups are selected and then measured exhaustively, the design is clustered even when the groups are called districts, villages, classes or blocks.

### 1.4 Probability designs against non-probability designs

The sorting rule is simple: can the selection probability of every unit be written down before the sample is drawn? If yes, the design is a probability design, and an unbiased estimate with a computable standard error follows. If no, the design is a non-probability design, and the only defensible output is a description of the respondents.

Simple random, stratified, systematic and cluster sampling are probability designs. Multistage sampling is a probability design when every stage uses a probability rule at every level. Convenience, quota, judgement and snowball sampling are non-probability designs. Convenience and quota are the two that appear most often in scenarios, and the usual trap is to accept quota sampling as a probability design because it produces the right proportions of each category. The proportions are right and the selection inside each category is still arbitrary, so the design is non-probability.

| Feature | Probability design | Non-probability design |
| --- | --- | --- |
| Selection probability | known and non-zero for every unit | unknown |
| Bias | absent from the selection mechanism | present and unquantified |
| Standard error | computable from the sample | not computable |
| Inference to the population | supported | not supported |
| Typical use | official statistics, research | piloting, rapid assessment, hidden populations |
| Examples | simple random, stratified, systematic, cluster | convenience, quota, judgement, snowball |

### 1.5 The quantities you must be able to produce

Almost every numerical part of a sampling question asks for one of the quantities in the list below. Being able to write each one immediately, with its symbols defined, is worth more than memorising worked examples.

| Quantity | Expression | What it needs |
| --- | --- | --- |
| Sampling fraction | $f = n/N$ | two counts |
| Inclusion probability | $\pi_i = n/N$ | two counts |
| Number of possible samples | $\binom{N}{n}$ | two counts |
| Systematic interval | $k = N/n$ | two counts |
| Proportional allocation | $n_h = nN_h/N$ | stratum sizes |
| Optimum allocation | $n_h = nN_hS_h/\sum_g N_gS_g$ | stratum sizes and spreads |
| Stratified variance | $\sum_h W_h^{2}\left(1-f_h\right)S_h^{2}/n_h$ | allocation and spreads |
| Variance of a mean | $\left(1-f\right)S^{2}/n$ | spread and fraction |
| Cluster variance | $\left(1-m/M_c\right)S_b^{2}/m$ | clusters and their spread |
| Design effect | $1 + \left(M-1\right)\rho$ | cluster size and correlation |
| Effective sample size | $n/\text{deff}$ | the two above |
| Sample size for a mean | $n_0/\left(1+n_0/N\right)$ | precision and spread |
| Sample size for a proportion | $n_0/\left(1+\left(n_0-1\right)/N\right)$ | precision and proportion |
| Non-response bias | $w_n\left(\bar{y}_r-\bar{y}_n\right)$ | response rate and difference |
| Number to approach | $n/q$ | target and response rate |

### 1.6 The architecture of a full-mark answer

A design question carries marks for identification, for justification, for computation and for comment. The five moves below cover all four, and they should be written in this order even when the question does not prescribe an order.

1. Name the design explicitly, using its technical name and no hedging.
2. Justify the name by quoting the defining feature from the scenario, such as the random start, the exhaustive measurement of selected groups, or the independent draw inside every group.
3. Compute the quantities the design implies, showing the formula, the substitution and the result, and checking any total that must reconcile.
4. State one advantage and one disadvantage that are specific to this scenario rather than generic.
5. State what the design licenses: an estimate with a computable standard error, or only a description of the respondents.

Step five is the one most often omitted, and it is the step that distinguishes a candidate who understands probability sampling from one who has memorised five definitions.

## 2. Theorems, Lemmas, and Analytical Properties

### 2.1 The five results that carry the most marks

> **Result 1 (Variance of a sample mean).** For simple random sampling without replacement,

$$
\text{Var}\left(\bar{y}\right) = \frac{S^{2}}{n}\left(1 - \frac{n}{N}\right),
$$

and the factor $1 - n/N$ is the finite population correction.

> **Result 2 (Stratified variance under proportional allocation).** With $n_h = nN_h/N$,

$$
\text{Var}_{prop}\left(\bar{y}_{st}\right) = \frac{1-f}{n}\sum_{h=1}^{H} W_h S_h^{2},
$$

so the ratio to the variance of a simple random sample of the same size is the share of variance lying within strata.

> **Result 3 (Optimum allocation).** For a fixed total sample,

$$
n_h = n\,\frac{N_h S_h}{\sum_{g=1}^{H} N_g S_g}, \qquad \text{Var}_{opt} = \frac{1}{n}\left(\sum_{h=1}^{H} W_h S_h\right)^{2} - \frac{1}{N}\sum_{h=1}^{H} W_h S_h^{2}.
$$

> **Result 4 (Design effect).** For clusters of equal size $M$ with intra-cluster correlation $\rho$,

$$
\text{deff} = 1 + \left(M-1\right)\rho, \qquad n_{\text{eff}} = \frac{n}{\text{deff}}, \qquad \text{SE inflation} = \sqrt{\text{deff}}.
$$

> **Result 5 (Sample size with the finite population correction).**

$$
n_0 = \frac{z^{2}S^{2}}{e^{2}}, \qquad n = \frac{n_0}{1 + \dfrac{n_0}{N}}, \qquad n_0 = \frac{z^{2}p\left(1-p\right)}{e^{2}}, \qquad n = \frac{n_0}{1 + \dfrac{n_0 - 1}{N}} .
$$

These five cover the computational core. A candidate who can write them from memory, define every symbol, and state what each symbol must be supplied from the scenario will rarely lose a method mark.

### 2.2 The decomposition that explains the gain

> **Result 6 (Within-and-between decomposition).** With stratum weights $W_h$, stratum means $\mu_h$ and stratum variances $S_h^{2}$ computed with divisor $N_h-1$,

$$
S^{2} = \frac{1}{N-1}\left[\sum_{h=1}^{H}\left(N_h-1\right)S_h^{2} + N\sum_{h=1}^{H} W_h\left(\mu_h-\mu\right)^{2}\right].
$$

The consequence to quote in an answer is that stratification removes the between-stratum component and leaves the within component, so the gain is the between share of the total variance. When a question supplies stratum means and variances, the between share can be computed and the gain predicted before any allocation is made.

> **Result 7 (Non-response bias).**

$$
\bar{y}_r - \bar{y} = w_n\left(\bar{y}_r - \bar{y}_n\right)
$$

The result shows that bias is a product of a missing share and a difference in means, so a question that supplies both can be answered in one line and a question that supplies only one cannot be answered at all.

### 2.3 Properties that decide a comparison question

> **Result 8 (Stratification never hurts under proportional allocation).** For strata of appreciable size the ratio of the stratified variance to the simple random variance is at most one under proportional allocation, with equality exactly when all stratum means are equal.

> **Result 9 (Ordering of allocations).** For a fixed sample size, Neyman allocation has variance no greater than proportional allocation, with equality when all stratum standard deviations are equal.

> **Result 10 (Clustering never helps).** The design effect is at least one for any cluster size above one and any non-negative intra-cluster correlation, and it equals one only when clusters are internally identical in mean.

> **Result 11 (Systematic sampling is not automatically like simple random sampling).** The variance depends on the order of the list through the correlation between units one interval apart, so no general inequality in either direction holds.

Three of these results are one-sided and can be quoted without computation. Clustering always costs precision when units within a cluster resemble one another, stratification under proportional allocation never costs precision, and systematic sampling may do either. An answer that states which of the three applies, and why, earns the comment marks that most candidates lose.

### 2.4 Traps and their repairs

The table below is the distilled form of the errors that examiners report most often. Each row names the trap, shows how it appears, and states the repair.

| Trap | How it appears | The repair |
| --- | --- | --- |
| Confusing stratified with cluster | a scenario mentions districts, classes or villages | ask whether every group is sampled or only some |
| Choosing the wrong design from a description | "every fifth invoice after a random start" | the random start plus the fixed step is systematic |
| Forgetting the finite population correction | sample is a quarter of a small population | compute $1-n/N$ and multiply |
| Applying one correction in a stratified design | unequal stratum fractions | apply $1-n_h/N_h$ stratum by stratum |
| Systematic sampling on a periodic list | interval equals the cycle length | state the danger and propose randomising the order |
| Treating quota sampling as a probability design | quotas match the population proportions | quotas fix composition, not selection |
| Ignoring the design effect in a cluster survey | "1200 households in 60 villages" | compute deff and the effective sample size |
| Omitting the random start in systematic sampling | "starting from the fifth name" | a fixed start is not a probability design |
| Rounding a sample size down | $n = 158.9$ reported as 158 | always round up and verify |
| Reporting the respondent mean as the population mean | 70 per cent response, no adjustment | apply the non-response identity or weight |
| Confusing sampling with non-sampling error | "the sample was large so the estimate is reliable" | size controls sampling error only |
| Adding the design effect instead of multiplying the variance | "add 20 per cent for clustering" | the variance is multiplied by deff |

### 2.5 What a scenario can and cannot tell you

Three questions decide whether a numerical answer is possible at all, and a good answer states that decision explicitly.

The first is whether the frame is described. Without a frame, simple random sampling cannot be carried out, because there is nothing to number and no list to draw from, and the correct answer to "how would you draw the sample" is to say that a frame must first be constructed.

The second is whether the population size is given. Without $N$, the finite population correction cannot be computed, and the answer must be given for an infinite population with the correction omitted and that omission stated.

The third is whether the spread is given. Without a standard deviation, a variance or a pilot estimate, a sample size cannot be computed from first principles, and the approved route is to use a range rule or a prior study and to say so. Examiners award the mark for the stated assumption, not for the number.

## 3. Formal Proofs, Derivations, and Methods

### 3.1 The proof to reproduce in full: unbiasedness and the finite population correction

This derivation appears in some form in most examination papers on the topic, and it takes eight lines.

Step 1. Introduce the selection indicator $I_i$, equal to one when unit $i$ is selected.

Step 2. Record the inclusion probability and its expectation.

$$
E\left(I_i\right) = \frac{n}{N}
$$

Step 3. Write the sample mean as a linear function of the indicators.

$$
\bar{y} = \frac{1}{n}\sum_{i=1}^{N} I_i y_i
$$

Step 4. Take expectations term by term.

$$
E\left(\bar{y}\right) = \frac{1}{n}\sum_{i=1}^{N} y_i\frac{n}{N} = \frac{1}{N}\sum_{i=1}^{N} y_i = \mu
$$

Step 5. Write the variance as a double sum of covariances.

$$
\text{Var}\left(\bar{y}\right) = \frac{1}{n^{2}}\sum_{i=1}^{N}\sum_{j=1}^{N}\text{Cov}\left(I_i,I_j\right)y_iy_j
$$

Step 6. Insert the two covariance forms, the diagonal and the off-diagonal.

$$
\text{Cov}\left(I_i,I_i\right) = \frac{n}{N}\left(1-\frac{n}{N}\right), \qquad \text{Cov}\left(I_i,I_j\right) = -\frac{n\left(N-n\right)}{N^{2}\left(N-1\right)}
$$

Step 7. Collect terms using the identity relating the cross products to the square of the total.

$$
N\sum_{i=1}^{N} y_i^{2} - \left(\sum_{i=1}^{N} y_i\right)^{2} = N\sum_{i=1}^{N}\left(y_i-\mu\right)^{2}
$$

Step 8. Divide by $N-1$ to obtain the population variance and read off the correction.

$$
\text{Var}\left(\bar{y}\right) = \frac{S^{2}}{n}\left(1-\frac{n}{N}\right)
$$

The examining point is the off-diagonal covariance. It is negative because sampling without replacement depletes the pool, and it is the algebraic origin of the finite population correction. A candidate who writes that the correction "accounts for the population being finite" without displaying the negative covariance has given the conclusion without the argument.

### 3.2 The exam version of the stratified variance

Step 1. State that the samples in different strata are independent, so no covariance terms survive.

Step 2. Write the variance of the weighted sum.

$$
\text{Var}\left(\bar{y}_{st}\right) = \sum_{h=1}^{H} W_h^{2}\text{Var}\left(\bar{y}_h\right)
$$

Step 3. Insert the within-stratum variance from Result 1.

$$
\text{Var}\left(\bar{y}_h\right) = \frac{S_h^{2}}{n_h}\left(1-\frac{n_h}{N_h}\right)
$$

Step 4. For proportional allocation, substitute $n_h = nW_h$ and note that $n_h/N_h = n/N$ in every stratum.

$$
\text{Var}_{prop}\left(\bar{y}_{st}\right) = \frac{1-f}{n}\sum_{h=1}^{H} W_hS_h^{2}
$$

Step 5. Divide by the simple random variance $\left(1-f\right)S^{2}/n$ and interpret the ratio as the within-stratum share.

The step that earns the method mark is Step 4, because it shows why proportional allocation is convenient: it makes the correction common to all strata, which is exactly what allows the sum to be taken outside.

### 3.3 The proof of optimum allocation in three lines

Step 1. Write the part of the variance that depends on the allocation.

$$
V = \sum_{h=1}^{H}\frac{W_h^{2}S_h^{2}}{n_h}, \qquad \sum_{h=1}^{H} n_h = n
$$

Step 2. Apply Cauchy–Schwarz to the two vectors $W_hS_h/\sqrt{n_h}$ and $\sqrt{n_h}$.

$$
\left(\sum_{h=1}^{H} W_hS_h\right)^{2} \le \left(\sum_{h=1}^{H}\frac{W_h^{2}S_h^{2}}{n_h}\right)\left(\sum_{h=1}^{H} n_h\right)
$$

Step 3. Divide by $n$ and note that equality requires proportionality of the two vectors.

$$
n_h = n\,\frac{W_hS_h}{\sum_{g=1}^{H} W_gS_g}
$$

The interpretation to add is that the allocation gives more interviews to strata that are large and internally variable, since both facts increase the information a single interview carries.

### 3.4 Using the decomposition inside a question

Step 1. Compute the population mean as the weighted average of the stratum means.

Step 2. Compute the between component as the weighted average of squared deviations of the stratum means from the population mean.

Step 3. Compute the weighted average of the stratum variances, which is the within component.

Step 4. Add the two components to obtain the population variance, or use the exact form with the degrees-of-freedom weights when the strata are small.

Step 5. Quote the ratio of the within component to the total as the proportional reduction in variance from stratification.

The five steps answer the whole family of questions that ask "how much does stratification help". When the stratum means are close together the between component is small and the gain is small; when they are far apart the between component dominates and the gain is large.

### 3.5 The design effect in three lines

Step 1. Write the variance of the cluster sample mean, which depends only on the between-cluster variance because every unit in a selected cluster is measured.

$$
\text{Var}\left(\bar{y}_{cl}\right) = \frac{S_b^{2}}{m}\left(1-\frac{m}{M_c}\right)
$$

Step 2. Write the variance of a simple random sample of the same number of observation units.

$$
\text{Var}_{srs}\left(\bar{y}\right) = \frac{S^{2}}{mM}\left(1-\frac{m}{M_c}\right)
$$

Step 3. Divide, cancel the corrections, and substitute $\rho = \sigma_b^{2}/\sigma^{2}$.

$$
\text{deff} = \frac{MS_b^{2}}{S^{2}} = 1 + \left(M-1\right)\rho
$$

The point to state explicitly is that the two correction factors are identical because both designs use the same fraction of the population, so the design effect is purely a ratio of variance components and has nothing to do with sample size.

### 3.6 The sample size derivation in four lines

Step 1. Set the margin of error equal to the required precision.

$$
e = z\sqrt{\frac{S^{2}}{n}\left(1-\frac{n}{N}\right)}
$$

Step 2. Square and expand.

$$
e^{2} = \frac{z^{2}S^{2}}{n} - \frac{z^{2}S^{2}}{N}
$$

Step 3. Solve for $n$.

$$
n = \frac{z^{2}S^{2}}{e^{2} + \dfrac{z^{2}S^{2}}{N}} = \frac{n_0}{1 + \dfrac{n_0}{N}}
$$

Step 4. Round up and verify by substituting the chosen integer back into the standard error.

Step 4 is not decoration. A formula that returns 158.9 gives 159, and the only way to demonstrate that 159 rather than 158 meets the specification is to evaluate the margin of error at both integers.

### 3.7 The decision procedure for naming a design

Step 1. Ask whether the scenario contains a chance mechanism at all. If the answer is no, the design is non-probability, and the specific name follows from how respondents were chosen: availability gives convenience, fixed category counts give quota, expert choice gives judgement, and nomination by respondents gives snowball.

Step 2. If a chance mechanism exists, ask what it selects. If it selects individual units from a list, the design is simple random or systematic depending on whether the rule is a draw or a step.

Step 3. If it selects groups, ask whether every group contributes. If every group contributes a sample of its members, the design is stratified. If only some groups are selected and all their members are measured, the design is clustered.

Step 4. If the selection happens in successive stages at different levels, the design is multistage, and the answer should name each stage and the rule used at each.

Step 5. State the consequence: a known inclusion probability for every unit, or no known probability and therefore no design-based inference.

### 3.8 The procedure for each design, in the form an answer should take

For simple random sampling: number the frame, choose a random device, draw distinct numbers, discard numbers outside the range and repeats, and match the survivors to the frame.

For stratified sampling: define the strata so that they are mutually exclusive and exhaustive, compute the weights, apply the allocation rule, reconcile the rounded allocations to the total, check the sum, and draw independently inside each stratum.

For systematic sampling: fix the order of the list, compute the interval, choose the start at random from the first interval, list the selected positions, verify that the last position does not exceed the population size, and state the periodicity risk with the specific feature of the list that might repeat.

For cluster sampling: define the clusters so that they cover the population, select clusters by a probability rule, measure every unit inside the selected clusters, compute the design effect, and report the effective sample size alongside the number of interviews.

For multistage sampling: name each stage, state the rule at each stage, compute the fraction at each stage, and give the variance as the sum of a component for each stage, noting which component dominates.

For a non-probability design: name it, state that no selection probability is known, identify the specific direction of the bias from the scenario, and state what the data can and cannot support.

## 4. Representative Worked Examples and Solutions

### 4.1 Model solution 1: identifying a design and allocating a stratified sample

A district has 2400 households in three areas: 1200 in the trading centre with standard deviation 10, 800 in the peri-urban area with standard deviation 15, and 400 in the rural area with standard deviation 25. A sample of 240 households is required, and the areas are to contribute in proportion to their size. Identify the design, compute the allocation, compute the variance of the estimate, compare it with a simple random sample of the same size, and state the allocation that would minimise the variance.

### 4.2 Solution: allocation, variance and comparison

Step 1. Name the design and justify the name. The population is divided into three internally similar areas and an independent sample is drawn inside every area, so the design is stratified sampling with the areas as strata.

Step 2. Compute the stratum weights.

$$
W_1 = \frac{1200}{2400} = 0.5, \qquad W_2 = \frac{800}{2400} = 0.3333, \qquad W_3 = \frac{400}{2400} = 0.1667
$$

Step 3. Apply proportional allocation.

$$
n_1 = 240(0.5) = 120, \qquad n_2 = 240(0.3333) = 80, \qquad n_3 = 240(0.1667) = 40
$$

Step 4. Check that the allocation reconciles to the total.

$$
120 + 80 + 40 = 240
$$

Step 5. Compute the weighted within-stratum variance.

$$
\sum_{h=1}^{3} W_hS_h^{2} = 0.5(100) + 0.3333(225) + 0.1667(625) = 50 + 75 + 104.17 = 229.17
$$

Step 6. Compute the sampling fraction and the multiplier.

$$
f = \frac{240}{2400} = 0.1, \qquad \frac{1-f}{n} = \frac{0.9}{240} = 0.00375
$$

Step 7. Compute the variance and standard error of the stratified estimate.

$$
\text{Var}_{prop} = 0.00375(229.17) = 0.8594, \qquad \text{SE} = 0.9270
$$

Step 8. Compute the population mean, which is needed for the between component.

$$
\mu = 0.5(60) + 0.3333(80) + 0.1667(115) = 30 + 26.67 + 19.17 = 75.83
$$

Step 9. Compute the between component from the stratum means.

$$
B = 0.5\left(60-75.83\right)^{2} + 0.3333\left(80-75.83\right)^{2} + 0.1667\left(115-75.83\right)^{2}
$$

$$
B = 0.5(250.69) + 0.3333(17.36) + 0.1667(1534.03) = 125.35 + 5.79 + 255.67 = 386.81
$$

Step 10. Compute the population variance exactly from the decomposition.

$$
\sum_h\left(N_h-1\right)S_h^{2} = 1199(100) + 799(225) + 399(625) = 119900 + 179775 + 249375 = 549050
$$

$$
S^{2} = \frac{549050 + 2400(386.81)}{2399} = \frac{549050 + 928344}{2399} = \frac{1477394}{2399} = 615.83
$$

Step 11. Compute the variance of a simple random sample of 240.

$$
\text{Var}_{srs} = 0.00375(615.83) = 2.3094, \qquad \text{SE} = 1.5197
$$

Step 12. Compute the ratio and the reduction.

$$
\frac{0.8594}{2.3094} = 0.3721, \qquad \text{reduction} = 62.8\ \text{per cent}
$$

Step 13. Compute the optimum allocation from the products $N_hS_h$, which are 12000, 12000 and 10000 and sum to 34000.

$$
n_1 = 240\,\frac{12000}{34000} = 84.71, \qquad n_2 = 84.71, \qquad n_3 = 240\,\frac{10000}{34000} = 70.59
$$

Step 14. Compute the variance under optimum allocation, starting from the weighted sum of stratum standard deviations.

$$
\sum_{h=1}^{3} W_hS_h = 0.5(10) + 0.3333(15) + 0.1667(25) = 14.167, \qquad \left(14.167\right)^{2} = 200.694
$$

$$
\text{Var}_{opt} = \frac{200.694}{240} - \frac{229.17}{2400} = 0.8362 - 0.0955 = 0.7407
$$

Step 15. Interpret. Proportional allocation removes 62.8 per cent of the variance of a simple random sample, which matches the between share of 386.81 out of 615.83, or 62.8 per cent. Optimum allocation removes a further 13.8 per cent of the stratified variance, because the rural stratum is much more variable and receives 70.59 interviews instead of 40. The standard errors are 0.9270 under proportional allocation and 0.8607 under optimum allocation, against 1.5197 for a simple random sample.

Marking points: naming and justifying the design (2 marks); the three weights (1 mark); the three allocations with the reconciliation check (3 marks); the weighted within-variance (2 marks); the fraction and the stratified variance (2 marks); the between component and the population variance (3 marks); the simple random variance and the ratio (2 marks); the optimum allocation formula applied correctly (2 marks); a conclusion that links the numerical gain to the between share (2 marks). A solution that computes everything but does not reconcile the allocation to 240 loses one method mark even when the arithmetic is right.

### 4.3 Model solution 2: systematic sampling and a periodic register

A register lists 600 stock items in 60 rows of ten. In every row the tenth item is a returned item valued at 70 units, and the other nine are valued at 20 units. A systematic sample of 60 items is taken with interval 10. Compute the population mean, the sample mean for each possible start, the variance over the random start, the variance of a simple random sample of the same size, and the design effect, and state what the sample itself would report.

### 4.4 Solution: an unbiased design with a useless estimate

Step 1. Name the design and compute the interval.

$$
k = \frac{N}{n} = \frac{600}{60} = 10
$$

Step 2. Compute the population mean from the row pattern.

$$
\mu = \frac{9(20) + 70}{10} = \frac{180 + 70}{10} = 25
$$

Step 3. Enumerate the ten possible samples. Because the interval equals the row length, each start selects the same position in every row.

$$
\bar{y}_{r=10} = 70, \qquad \bar{y}_{r \ne 10} = 20
$$

Step 4. Verify unbiasedness over the random start.

$$
E\left(\bar{y}_{sys}\right) = \frac{9(20) + 70}{10} = 25 = \mu
$$

Step 5. Compute the variance over the random start.

$$
\text{Var}\left(\bar{y}_{sys}\right) = \frac{1}{10}\left[9\left(20-25\right)^{2} + \left(70-25\right)^{2}\right] = \frac{9(25) + 2025}{10} = \frac{2250}{10} = 225
$$

Step 6. Compute the population variance, noting that 540 items take the value 20 and 60 take the value 70.

$$
S^{2} = \frac{540\left(20-25\right)^{2} + 60\left(70-25\right)^{2}}{599} = \frac{13500 + 121500}{599} = \frac{135000}{599} = 225.38
$$

Step 7. Compute the variance of a simple random sample of 60.

$$
\text{Var}_{srs} = \frac{225.38}{60}\left(1-\frac{60}{600}\right) = 3.7563(0.9) = 3.3806, \qquad \text{SE} = 1.8387
$$

Step 8. Compute the design effect of the systematic design.

$$
\text{deff} = \frac{225}{3.3806} = 66.56
$$

Step 9. State what the sample reports. When the start is 10, every selected item is valued at 70, so the sample mean is 70, the sample standard deviation is zero, and any standard error computed from the sample is zero, although the estimate is 45 units above the truth.

Step 10. Interpret and propose the repair. The design is unbiased in the long run and worthless in practice, because one start in ten produces a completely unrepresentative sample and the sample contains no internal evidence of the failure. The repair is to randomise the order of the register before sampling, to use several random starts with a smaller interval, or to replace the design with a simple random or stratified sample.

Marking points: the interval (1 mark); the population mean (1 mark); the enumeration of the possible samples (2 marks); the unbiasedness check (1 mark); the variance over starts (2 marks); the simple random variance with the correction (2 marks); the design effect (1 mark); the statement that the sample variance collapses to zero (2 marks); the repair (1 mark). The last two are the discriminating marks: a candidate who computes a variance of 225 and stops has shown that the design is bad but not why the badness is undetectable from the sample.

### 4.5 Model solution 3: a clustered survey and its effective sample size

A household survey covers 5000 households in 250 villages of 20 households each. Twenty-five villages are selected and all households in them are interviewed. The intra-cluster correlation is 0.2 and the population variance of the study variable is 900. Compute the design effect, the effective sample size, the variance and standard error of the estimate, compare with a simple random sample of 500 households, and evaluate a proposal to select fifty villages and interview ten households in each.

### 4.6 Solution: design effect, precision and redesign

Step 1. Name the design. Whole villages are selected at random and every household in a selected village is interviewed, so the design is one-stage cluster sampling with villages as clusters.

Step 2. Compute the design effect with cluster size 20 and correlation 0.2.

$$
\text{deff} = 1 + \left(20-1\right)(0.2) = 1 + 3.8 = 4.8
$$

Step 3. Compute the effective sample size.

$$
n_{\text{eff}} = \frac{500}{4.8} = 104.17
$$

Step 4. Compute the inflation of the standard error.

$$
\sqrt{4.8} = 2.191
$$

Step 5. Compute the variance of a simple random sample of 500 from a population of 5000.

$$
\text{Var}_{srs} = \frac{900}{500}\left(1-\frac{500}{5000}\right) = 1.8(0.9) = 1.62, \qquad \text{SE} = 1.2728
$$

Step 6. Multiply by the design effect to obtain the variance of the cluster design.

$$
\text{Var}_{cl} = 1.62(4.8) = 7.776, \qquad \text{SE} = 2.7885
$$

Step 7. Verify the cluster variance directly from the between-village variance, which is $S_b^{2} = \text{deff}\times S^{2}/M = 4.8(900)/20 = 216$.

$$
\text{Var}_{cl} = \frac{216}{25}\left(1-\frac{25}{250}\right) = 8.64(0.9) = 7.776
$$

Step 8. Evaluate the proposal of fifty villages of ten households, which keeps the total at 500 interviews.

$$
\text{deff} = 1 + \left(10-1\right)(0.2) = 2.8
$$

$$
\text{Var} = 1.62(2.8) = 4.536, \qquad \text{SE} = 2.1298
$$

Step 9. Quantify the improvement.

$$
\frac{7.776 - 4.536}{7.776} = 0.4167, \qquad \text{that is } 41.7\ \text{per cent}
$$

Step 10. Interpret. The clustered sample of 500 households carries the information of about 104 independently chosen households, so the margin of error is more than twice what the number 500 suggests. Halving the cluster size at the same total number of interviews cuts the variance by 41.7 per cent, because the design effect falls from 4.8 to 2.8. The cost of the change is more villages to visit, which is the trade that cluster designs always face: precision is bought by adding clusters, not by adding households inside clusters.

Marking points: naming the design (1 mark); the design effect (2 marks); the effective sample size (1 mark); the standard error inflation (1 mark); the simple random variance with the correction (2 marks); the cluster variance and the direct verification (2 marks); the redesign computation (2 marks); the percentage improvement (1 mark); a conclusion about adding clusters rather than households (2 marks).

### 4.7 Model solution 4: sample size, finite population correction and non-response

A survey must estimate the proportion of households holding a bank account to within 0.04 at 95 per cent confidence. A prior study suggests a proportion of 0.45 and the population contains 4000 households. Experience suggests that 80 per cent of approached households cooperate. Find the number of completed interviews required, the number of households to approach, and the effect on the plan of discovering that the prior proportion was in fact 0.5.

### 4.8 Solution: three stages of planning

Step 1. Compute the infinite-population sample with $p = 0.45$ and $z = 1.96$.

$$
n_0 = \frac{3.8416(0.45)(0.55)}{0.0016} = \frac{0.950796}{0.0016} = 594.25
$$

Step 2. Apply the finite population correction.

$$
n = \frac{594.25}{1 + \dfrac{594.25 - 1}{4000}} = \frac{594.25}{1.148313} = 517.50
$$

Step 3. Round up to the next whole household.

$$
n = 518
$$

Step 4. Verify the margin of error at the chosen value and at the value below it.

$$
n = 518: \quad 1.96\sqrt{\frac{0.2475}{518}\left(1-\frac{518}{4000}\right)} = 0.03997 \le 0.04
$$

$$
n = 517: \quad 1.96\sqrt{\frac{0.2475}{517}\left(1-\frac{517}{4000}\right)} = 0.04002 > 0.04
$$

Step 5. Inflate for non-response to obtain the number to approach.

$$
n_{\text{approach}} = \frac{518}{0.80} = 647.5 \quad \text{so} \quad 648
$$

Step 6. Recompute the sample for the revised proportion of 0.5.

$$
n_0 = \frac{3.8416(0.25)}{0.0016} = 600.25
$$

$$
n = \frac{600.25}{1 + \dfrac{599.25}{4000}} = \frac{600.25}{1.149813} = 522.04
$$

Step 7. State the revised plan and its consequence for the field budget.

$$
n = 523, \qquad n_{\text{approach}} = \frac{523}{0.80} = 653.75 \quad \text{so} \quad 654
$$

Step 8. Interpret. The uncorrected sample would have been 595, so the correction saved 77 completed interviews, and the non-response inflation adds 130 approaches on top of the completed requirement. A prior proportion of 0.5 rather than 0.45 adds only 5 completed interviews, because $p(1-p)$ changes from 0.2475 to 0.25, a difference of one per cent. The costly assumptions are the response rate and the frame, not the prior proportion, which is why a planning answer should state all three and identify which is the most fragile.

Marking points: the infinite-population formula (2 marks); the corrected sample (2 marks); rounding up (1 mark); the verification at both integers (2 marks); the non-response inflation (2 marks); the recomputation at 0.5 (2 marks); a conclusion identifying the fragile assumption (2 marks).

### 4.9 Model solution 5: precision, the correction, and a target standard error

A simple random sample of 400 is drawn from a population of 8000 with population variance 1600. Compute the standard error with and without the finite population correction, compute the sample needed to achieve a standard error of 1.5 with the correction, and state what would be needed without it.

### 4.10 Solution: correction, target and comparison

Step 1. Compute the sampling fraction and the correction.

$$
f = \frac{400}{8000} = 0.05, \qquad 1 - f = 0.95
$$

Step 2. Compute the variance and standard error with the correction.

$$
\text{Var} = \frac{1600}{400}(0.95) = 4(0.95) = 3.8, \qquad \text{SE} = 1.9494
$$

Step 3. Compute the standard error without the correction.

$$
\text{SE} = \sqrt{\frac{1600}{400}} = 2.0000
$$

Step 4. Compute the infinite-population sample for a standard error of 1.5.

$$
n_0 = \frac{1600}{1.5^{2}} = \frac{1600}{2.25} = 711.11
$$

Step 5. Apply the finite population correction.

$$
n = \frac{711.11}{1 + \dfrac{711.11}{8000}} = \frac{711.11}{1.088889} = 653.06
$$

Step 6. Round up and verify.

$$
n = 654: \quad \text{SE} = \sqrt{\frac{1600}{654}\left(1-\frac{654}{8000}\right)} = 1.4988 \le 1.5
$$

$$
n = 653: \quad \text{SE} = \sqrt{\frac{1600}{653}\left(1-\frac{653}{8000}\right)} = 1.5001 > 1.5
$$

Step 7. Compare the corrected and uncorrected plans.

$$
\frac{711 - 654}{711} = 0.0802, \qquad \text{that is } 8.0\ \text{per cent}
$$

Step 8. Interpret. Ignoring the correction overstates the standard error of the 400-unit sample by 2.6 per cent and overstates the sample needed for a standard error of 1.5 by 57 interviews, or 8.0 per cent. Both errors are small here because the sample is under a tenth of the population; the same mistakes at a sampling fraction of one half would overstate the standard error by 41 per cent and the required sample by a factor of two.

Marking points: the fraction and correction (1 mark); the corrected variance and standard error (2 marks); the uncorrected standard error (1 mark); the infinite-population sample (2 marks); the corrected sample (2 marks); rounding up with verification at both integers (2 marks); a quantified comparison (2 marks).

## 5. Mathematical Extensions, Limits, and Common Errors

### 5.1 The five traps, examined in detail

The first trap is choosing the design from a description. The cue that decides most cases is the fate of the groups. If the description says that every district, class or ward contributes a sample, the design is stratified, and the fact that the groups are geographic is irrelevant. If the description says that some groups are selected and then examined completely, the design is clustered, and the fact that the groups are called districts does not make it stratified. The mixed case, in which some groups are selected and then a sample is taken inside each, is multistage sampling, and the answer should name both stages.

The second trap is confusing stratification with clustering when the question asks for the variance. In a stratified design the variance is a weighted sum of within-stratum variances and falls as the strata become more internally homogeneous. In a cluster design the variance is driven by the variation between cluster means and rises as the clusters become more internally homogeneous. The two designs therefore respond in opposite directions to exactly the same feature of the population, and an answer that treats them as interchangeable will have the sign of the effect wrong.

The third trap is forgetting the finite population correction. The symptom is a variance computed as $S^{2}/n$ when the question has supplied a population size and a sample that is a substantial share of it. The correction matters little below a sampling fraction of about one tenth, becomes noticeable at a quarter, and dominates at one half, where it halves the variance and reduces the standard error by 29 per cent. Whenever a question supplies both $n$ and $N$ and the fraction exceeds one tenth, the correction should be applied and its size stated.

The fourth trap is a systematic sample on a list that repeats. The interval defines a phase, and if the list has a cycle of the same length the sample is drawn entirely from one phase. The signature of this problem in an examination question is a description that mentions a regular pattern, such as rows of ten items, weeks of seven days, or classes of equal size, together with an interval equal to the pattern length. The answer must show that the design is still unbiased over the random start and that a single realised sample can nevertheless be badly wrong and can report a standard error of zero.

The fifth trap is accepting a non-probability design as a probability design. Quota sampling is the usual offender, because the quotas reproduce the population proportions and the tabulation therefore looks representative. The composition is representative and the selection inside each quota cell is not, so the design has no inclusion probabilities and no computable standard error. The same applies to a survey that reports a very large response rate from a convenience sample: the size does not create a probability mechanism.

### 5.2 Limits and quick checks

Several limits give instant checks on an answer. The finite population correction lies between zero and one, so a computed variance must be no larger than $S^{2}/n$ and no smaller than zero. The design effect must be at least one whenever units within a cluster resemble one another, so a computed value below one signals either an arithmetic slip or a negative intra-cluster correlation that should be justified explicitly. The ratio of the stratified variance to the simple random variance must lie between zero and one under proportional allocation, so a ratio above one signals that the allocation was not proportional. The optimum allocation must give a variance no greater than proportional allocation, and the effective sample size must not exceed the number of interviews.

A further check is dimensional. A variance has the units of the variable squared, so a variance of 3.8 for an expenditure measured in hundreds of units is plausible while a variance of 380000 for the same variable signals a missed division. A standard error is always smaller than the standard deviation of the population whenever the sample exceeds one, and a standard error larger than the population standard deviation is impossible under any of the designs in this topic.

The sample size formulas have their own checks. The corrected sample must be smaller than the uncorrected one, and the ratio must equal $1/\left(1+n_0/N\right)$, which is about 0.9 when $n_0$ is a tenth of $N$. If a computed corrected sample exceeds the uncorrected one, the correction has been applied upside down.

### 5.3 Revision checklist

The checklist below is ordered by the frequency with which each item appears in examination papers. Ticking an item means being able to write it from memory, define every symbol, and state one scenario in which it applies.

- Definitions of population, frame, sample, sampling unit, observation unit, and the distinction between a census and a sample survey.
- The five designs, each with a one-line definition and a one-line justification phrase.
- The classification of the five designs as probability or non-probability, and the three additional non-probability designs with their characteristic biases.
- Inclusion probability under simple random sampling, and the number of possible samples as a binomial coefficient.
- The variance of a sample mean with the finite population correction, and the version without it.
- The finite population correction evaluated at sampling fractions of 0.1, 0.25, 0.5 and 0.9.
- Proportional allocation, with the reconciliation check, and the stratified variance under proportional allocation.
- Optimum allocation, the closed-form optimum variance, and the comparison with proportional allocation.
- The within-and-between decomposition, and the statement that the gain equals the between share.
- The systematic interval, the random start, the set of selected positions, and the periodicity warning.
- The cluster variance, the design effect, the effective sample size and the standard error inflation.
- The two-stage variance and the direction of the trade between primary and secondary units.
- The sample size formulas for a mean and for a proportion, with the correction and the rounding rule.
- The non-response identity, the response-rate inflation, and the reason a larger sample cannot repair non-response.
- The distinction between sampling and non-sampling error, with examples of each.
- The four derivations that can be asked for: unbiasedness, the variance with the correction, the stratified variance under proportional allocation, and optimum allocation.
- One worked example of each type: allocation, interval, design effect, sample size, non-response.
- The traps table of Section 2.4, reproduced mentally as a list of symptoms.

### 5.4 Time strategy in the examination

Allocate the time in proportion to the marks and protect the computational marks first, because they are the ones that can be checked. A practical division for a twenty-mark sampling question is one quarter for identification and definitions, one half for computation, and one quarter for comment and evaluation.

Read the whole scenario before writing anything, and underline every quantity that is given: the population size, the number of groups, the group sizes, the sample size, the spread, the response rate, the costs. Most lost marks in this topic come from using a number that was supplied for a different purpose, such as using the number of households when the question asks about the number of villages.

Write the formula before the substitution, every time. A method mark survives an arithmetic slip only if the formula is visible, and an answer that begins with numbers cannot be diagnosed.

Reconcile every allocation before moving on. If the stratum allocations do not sum to the sample size, the subsequent variance is wrong however carefully it is computed, and the reconciliation takes five seconds.

State the design effect and the effective sample size whenever a cluster design appears, even if the question does not ask for them. They are frequently worth a mark on their own and they demonstrate that the number of interviews is not the number of independent observations.

Finish with two sentences of evaluation that are specific to the scenario: what the design controls, and what it does not. Generic sentences about cost and convenience earn nothing, while a sentence naming the particular subgroup that the frame omits, or the particular feature of the list that might repeat, earns the comment marks.

If time runs short, answer in order of marks per minute: the definitional parts first, then the allocation, then the variance, then the sample size, then the evaluation. A partially completed answer that reaches the allocation earns more than a complete essay on advantages and disadvantages.

### 5.5 Synthesis

The examination rewards a fixed pattern of thought. A scenario is first located on the map of designs by asking what the randomisation selects and whether every group contributes. The name of the design then determines which of the five variance formulas applies, and the formula determines which quantities must be extracted from the scenario. The arithmetic is a substitution, guarded by three checks: the correction factor, the reconciliation of any allocation, and the size of the design effect. The evaluation is a statement of what the design controls and what it leaves to non-sampling error.

The mathematical content that must be secure is small and highly connected. One inclusion probability, one variance formula, one correction factor, one decomposition, one allocation rule, one design effect and one sample-size inversion generate every result in the topic, and each of the five designs is a different evaluation of the same general expression. A candidate who can derive the variance of a sample mean from the covariance of selection indicators, and who can say in one sentence why each design changes that covariance, can answer any question on this topic without memorising a single worked example.
