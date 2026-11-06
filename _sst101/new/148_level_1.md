## 1. Foundational Concepts, Definitions, and Axioms

### 1.1 A pot of soup, a spoonful, and a whole village

Imagine a cook who has just finished a very large pot of soup for a wedding. To decide whether the soup needs more salt, the cook does not drink the pot. The cook stirs the soup thoroughly, lifts one spoonful, and tastes it. Because the soup was stirred, the spoonful is a fair picture of the pot, and a single taste is enough to make a decision. Now imagine that the cook forgot to stir. The spoonful may be almost pure salt from the bottom or almost pure water from the top, and the decision will be wrong no matter how many spoonfuls are taken from that same unlucky place.

Picture now a district officer who must report the average number of rooms per house in a district of eight thousand houses. Visiting every house would take months and would cost far more than the report is worth. The officer visits a few hundred houses instead and uses what is found there to speak about all eight thousand. The few hundred houses form the sample; the eight thousand houses form the population. Deciding which houses to visit, and by what rule, is the whole of this topic.

The soup analogy carries the central idea and then stops being exact, in a way that matters. Soup is a liquid, and stirring really does mix it, so one spoonful is as informative as any other. People and households are not like that. They live in streets, they belong to villages, they work in particular places, and some of them are much easier to reach than others. Because a real population is lumpy and unevenly reachable, no single act of stirring works for every survey. Several selection rules exist instead, each with its own guarantee, its own cost, and its own characteristic way of going wrong. Five of those rules are studied here: random sampling, stratified sampling, systematic sampling, cluster sampling, and convenience sampling.

### 1.2 The four objects every survey must keep apart

Most confusion in this subject comes from using one word for two different things. Four objects have to be distinguished at the start.

> **Definition (Population).** The population is the complete set of units about which a statement is wanted. The units may be people, households, shops, farms, transactions, or events, and the population is fixed by the question asked rather than by a map or a register.

> **Definition (Sampling frame).** The sampling frame is the concrete list, register, map, or procedure from which the sample is actually drawn, such as a register of licensed traders, a roll of registered students, a map of building plots, or a shelf of patient files.

> **Definition (Sample).** The sample is the subset of units that is actually selected by the chosen rule.

> **Definition (Respondents).** The respondents are the selected units that actually supply usable information.

The four objects are rarely identical, and each gap between them produces its own kind of error. A register of licensed traders omits the unlicensed ones, so the frame is smaller than the population and the gap is called coverage error. The sample is smaller than the frame, and the gap is called sampling error. The respondents are fewer than the sample, because some selected traders cannot be found or refuse, and that gap is called non-response error. Finally the answers given may not be the truth, and that gap is called measurement error. A survey is accurate only when all four gaps are small, and a very large sample does nothing at all about three of them.

### 1.3 The sampling unit and the observation unit

Two more words deserve separate definitions, because examination questions turn on them.

> **Definition (Sampling unit).** The sampling unit is the entity that the selection rule chooses, and it is the unit that carries a known chance of selection.

> **Definition (Observation unit).** The observation unit is the entity on which the measurement is actually taken.

The two coincide in a simple list of people, where one person is chosen and that same person is measured. They separate as soon as groups are selected. If a village is chosen and then every household in it is visited, the sampling unit is the village and the observation unit is the household. If a household is chosen and one adult inside it is interviewed, the sampling unit is the household and the observation unit is the adult. Recognising this separation is what allows a reader to see immediately whether a described design is stratified, clustered, or multistage.

### 1.4 The symbols, explained in words

A small amount of notation makes every later statement shorter. Each symbol is described in words before it is used.

| Symbol | What it stands for, in words |
| --- | --- |
| $N$ | the number of units in the population or frame |
| $n$ | the number of units selected into the sample |
| $y_i$ | the value of the measured variable for unit $i$ |
| $\bar{y}$ | the average of the selected values, called the sample mean |
| $\mu$ | the average of all population values, called the population mean |
| $\sigma^{2}$ | the population variance, a measure of how spread out the population values are |
| $f$ | the sampling fraction, the share of the population that enters the sample |

The sampling fraction is the first quantity to compute in almost every question, because it measures how much of the population has been looked at.

$$
f = \frac{n}{N}
$$

A fraction near zero describes a small sample from a large population, and a fraction close to one describes a sample that is almost a full count. The quantity $1 - f$ appears so often that it has its own name, the finite population correction factor, and it will be explained carefully in Section 2.

### 1.5 Why a sample is used instead of a count of everybody

A complete count of a population is called a census. A census is occasionally the right choice, for example when the population is small or when the law requires every unit to be recorded. For most questions a sample is better, for five separate reasons.

The first reason is cost. Interviewing every household in a district requires an enumerator for every few dozen households, and the wage bill grows in direct proportion to the population size, while the accuracy of the estimate improves only in proportion to the square root of the sample size. Money spent on the last few thousand households buys almost no additional precision.

The second reason is speed. A census of a large population takes months, and by the time the results appear the situation being described may have changed. A sample can be completed in weeks and can therefore describe the population as it currently is.

The third reason is feasibility. For some populations no complete list exists and none can be constructed at reasonable cost. Traders in an open market, users of a footpath, and vehicles passing a junction have no register, so a complete count is not merely expensive but impossible.

The fourth reason is quality. A small survey can afford well-trained enumerators, careful supervision, and a pilot test of the questionnaire. A census employs a large temporary workforce, and the additional errors introduced by an untrained workforce can easily exceed the sampling error that the census was supposed to eliminate.

The fifth reason is that some measurements destroy the unit measured. Testing whether a batch of lamps meets a brightness specification may require burning the lamp until it fails, and no manufacturer destroys every lamp in a consignment. In such cases a sample is not a compromise but a necessity.

### 1.6 Probability designs and non-probability designs

Every selection rule in this topic belongs to one of two families, and the family determines what can honestly be claimed from the data.

> **Definition (Probability sampling).** A design is a probability design when every unit in the frame has a known, non-zero probability of selection, and that probability is fixed by the design before the sample is drawn.

> **Definition (Non-probability sampling).** A design is a non-probability design when the chance that any particular unit enters the sample is unknown, because selection depends on the judgement, the convenience, or the contacts of the person doing the selecting.

The distinction is not a matter of taste. If the selection probabilities are known, then each selected unit can be made to stand for a known number of population units, and the standard error of any estimate can be computed from the data. If the probabilities are unknown, no such arithmetic is available, and the survey cannot say how far its answer might be from the truth. Non-probability designs are still used, because they are cheap and fast, but the honest description of their output is a description of the people who answered, not of the population.

Of the five methods in this topic, random, stratified, systematic, and cluster sampling are probability designs, and convenience sampling is a non-probability design. Three further non-probability designs are studied in Section 3, namely quota sampling, judgement sampling, and snowball sampling, because they appear constantly in practice and in examinations.

### 1.7 The five methods, one at a time

Each method is defined first in words, then illustrated with a small picture of how the selection would actually be carried out.

> **Definition (Simple random sampling).** Simple random sampling selects units in such a way that every unit has the same chance of selection and every possible sample of the required size has the same chance of being the sample obtained.

The practical version is the lottery. Number all $N$ units, write the numbers on identical slips, mix them thoroughly, and draw $n$ slips. The modern version replaces the box with a table of random digits or a computer generator, but the logic is identical: the order in which numbers emerge is not influenced by anything about the units.

> **Definition (Stratified sampling).** Stratified sampling first divides the population into non-overlapping groups called strata, formed so that units inside a group resemble one another, and then draws a separate sample inside every stratum.

A survey of household income might stratify a town into three income belts and sample households inside each belt. Every belt contributes, so no belt can be missed by an unlucky draw, and the estimate is usually more precise than a plain random sample of the same size.

> **Definition (Systematic sampling).** Systematic sampling arranges the population in a list, chooses a random starting point among the first few positions, and then takes every unit at a fixed gap after that start.

Selecting every twentieth house along a street after a random start among the first twenty is systematic sampling. It is quick, it spreads the sample evenly through the list, and it needs no random-number machinery once the start has been fixed.

> **Definition (Cluster sampling).** Cluster sampling divides the population into groups called clusters, selects a sample of whole clusters, and then measures every unit inside each selected cluster.

Selecting twenty villages at random and interviewing every household in those villages is cluster sampling. It is cheap when travel between distant places is the main cost, because the enumerators visit a small number of locations, but it is less precise than a plain random sample of the same number of households whenever neighbouring households resemble one another.

A cluster design is often applied in more than one step, and then it is called multistage sampling. The survey first chooses villages at random, then chooses a street inside each chosen village, then chooses households inside each chosen street. Each step has its own sampling unit and its own selection rule, and the chance that a given household enters the sample is the product of the chances at the three steps. The practical reason for the extra steps is that visiting every household in a chosen village may still be too expensive, so the survey takes a sample inside the village instead of a complete count.

> **Definition (Convenience sampling).** Convenience sampling selects units because they are easy, near, or willing, without any chance mechanism at all.

Interviewing the shoppers who happen to pass the interviewer's table, or the households nearest the field office, is convenience sampling. It is fast and cheap and it cannot support a statement about the population.

### 1.8 Sampling error and non-sampling error

Two kinds of error affect every survey, and confusing them is the most common conceptual mistake in the topic.

> **Definition (Sampling error).** Sampling error is the difference between an estimate and the population value that arises because only part of the population was measured.

> **Definition (Non-sampling error).** Non-sampling error is every error that would remain even if the whole population were measured, including coverage error from an incomplete frame, non-response error from units that cannot be reached, measurement error from faulty questions or faulty recording, and processing error from mistakes in data entry.

Sampling error shrinks as the sample grows, and it can be reduced to zero by taking a census. Non-sampling error does not shrink in that way and is often made worse by a census, because a census is large and hurried. This is why a well-run sample of a few thousand units routinely produces better figures than a badly run count of millions, and why the phrase "the sample was large, so the result must be right" is a fallacy.

## 2. Theorems, Lemmas, and Analytical Properties

### 2.1 The equal-chance property and the number of possible samples

The first property of simple random sampling is the one that gives it its name, and it is worth stating as a result because every later property depends on it.

> **Result (Equal chance).** Under simple random sampling without replacement, every unit has the same probability of appearing in the sample, namely $n/N$, and every distinct sample of size $n$ is equally likely.

The number of distinct samples of size $n$ that can be formed from $N$ units is the binomial coefficient, and the probability of any one of them is its reciprocal.

$$
\binom{N}{n} = \frac{N!}{n!\,(N-n)!}, \qquad P(\text{a given sample}) = \frac{1}{\binom{N}{n}}
$$

The formula is alarming in size but simple in meaning. The numerator counts the ways of arranging all units in a queue; the denominator removes the arrangements that produce the same set, once for the order inside the sample and once for the order of the units left out. For the small case of four households numbered one to four, choosing two at random gives six possible samples, because

$$
\binom{4}{2} = \frac{4!}{2!\,2!} = 6,
$$

and each of the six pairs has probability one sixth.

When selection is with replacement, the unit drawn is put back before the next draw, so the population is unchanged between draws and a unit can appear twice. The number of possible ordered selections becomes $N^{n}$, and the chance that a particular unit appears at least once is found by complement.

$$
P(\text{unit appears at least once}) = 1 - \left(1 - \frac{1}{N}\right)^{n}
$$

Replacement is convenient in theory and rare in practice, because re-interviewing the same household wastes a visit. The distinction still matters in examinations, where the phrase "with replacement" changes both the probability and the variance.

### 2.2 The variance of the sample mean and the finite population correction

The sample mean is unbiased for the population mean, and its variance under simple random sampling without replacement is the single most used formula in the topic.

> **Result (Variance of the sample mean).** For a sample of size $n$ drawn without replacement from a population of size $N$ with population variance $\sigma^{2}$,

$$
\text{Var}(\bar{y}) = \frac{\sigma^{2}}{n}\left(1 - \frac{n}{N}\right).
$$

Throughout this note the population variance is computed with divisor one less than the population size, which is the convention that makes the sample variance an unbiased estimator of it. The formula has two factors and each has a plain reading. The factor $\sigma^{2}/n$ says that the average of $n$ independent values is $n$ times as precise as a single value, which is the ordinary averaging effect that makes larger samples better. The factor $1 - n/N$ is the finite population correction: it says that sampling without replacement is better than sampling with replacement, because every unit taken out removes one more unit from the remaining pool and therefore reduces the remaining uncertainty.

The correction is negligible when the sample is a small share of the population and decisive when it is a large share. Its size for several sampling fractions is shown here.

| Sampling fraction $f = n/N$ | Finite population correction $1 - f$ |
| --- | --- |
| 0.05 | 0.95 |
| 0.10 | 0.90 |
| 0.20 | 0.80 |
| 0.50 | 0.50 |
| 0.80 | 0.20 |
| 0.95 | 0.05 |

Two lessons follow directly. First, when $n$ is small relative to $N$ the correction can be ignored without harm, which is why national surveys of millions of people ignore it. Second, when the sample is a large share of a small population, ignoring the correction overstates the standard error badly and leads to a sample larger than necessary. A common examination trap is to compute the standard error of a sample that is one half of the population and to report a figure that is too large by a factor of the square root of two.

When selection is with replacement, the correction disappears and the variance is simply

$$
\text{Var}(\bar{y}) = \frac{\sigma^{2}}{n}.
$$

### 2.3 Proportional allocation in stratified sampling

In stratified sampling the total sample size must be shared among the strata, and the simplest sharing rule is to give each stratum the same share of the sample that it has of the population.

> **Result (Proportional allocation).** If stratum $h$ contains $N_h$ units and the population contains $N$ units in total, the proportional allocation gives that stratum a sample of

$$
n_h = n\,\frac{N_h}{N} = n W_h,
$$

where $W_h = N_h/N$ is the stratum weight, and the allocations satisfy $n_1 + n_2 + \cdots + n_H = n$.

The property that makes the rule attractive is that the sample then mirrors the population. If a stratum holds 30 per cent of the population it holds 30 per cent of the sample, so every subgroup is represented in its correct proportion without any weighting at the analysis stage. The estimate itself is the weighted average of the stratum means.

$$
\bar{y}_{st} = \sum_{h=1}^{H} W_h \bar{y}_h
$$

The arithmetic of the check is as important as the arithmetic of the allocation. Because the parts must add to the whole, a candidate who obtains allocations summing to something other than $n$ has made an error, usually by rounding each part downwards without adjusting the remainder.

### 2.4 The sampling interval in systematic sampling

Systematic sampling replaces a random draw per unit with a single random start followed by a fixed step.

> **Result (Sampling interval).** Let the list of $N$ units be divided into $n$ consecutive blocks of $k$ units each, so that $N = nk$. A starting position $r$ is chosen at random from the first $k$ positions, and the units in positions $r$, $r+k$, $r+2k$, and so on are selected. Exactly one unit is taken from each block.

The interval is therefore

$$
k = \frac{N}{n},
$$

and when the division is not exact the interval is rounded down and the realised sample is slightly larger than planned, or a fractional-interval method is used. The important structural point is that the sample is spread through the whole list: no long stretch of the list can be missed, which is a real advantage when the list is ordered by time, by geography, or by an identifier that the survey wishes to cover evenly.

The structural weakness is equally clear. Because the same position is taken from every block, any feature that repeats with the same period as the interval is either over-represented or entirely missed.

> **Result (Periodicity risk).** If the list has a cycle of length $k$, systematic sampling with interval $k$ selects only one phase of the cycle, and the sample can be severely biased even though the start was chosen at random.

### 2.5 Why stratification improves precision

Stratified sampling gains precision because it separates two kinds of variation that a plain random sample mixes together.

> **Result (Variance decomposition).** If the population is divided into strata with weights $W_h$, within-stratum variances $\sigma_h^{2}$, and stratum means $\mu_h$, then the population variance splits exactly into a part coming from variation inside strata and a part coming from differences between stratum means:

$$
\sigma^{2} = \sum_{h=1}^{H} W_h \sigma_h^{2} + \sum_{h=1}^{H} W_h \left(\mu_h - \mu\right)^{2}.
$$

Read in words, the total spread of the population is the average spread inside the groups plus the spread of the group averages around the overall average. A plain random sample has to cope with both parts, because a random sample can by bad luck contain too many units from one group. A stratified sample copes only with the first part, because the group mix is fixed by the design and cannot vary from sample to sample. The second part is removed, and the precision gained is exactly the removed part.

When proportional allocation is used, the variance of the stratified estimate is

$$
\text{Var}(\bar{y}_{st}) = \frac{1-f}{n}\sum_{h=1}^{H} W_h \sigma_h^{2},
$$

so the gain over a plain random sample of the same size is measured by the ratio of the within part to the whole. If the strata differ greatly in their means, most of the total variation is between strata, the within part is small, and the gain is large. If the strata are formed on a variable unrelated to the one measured, the stratum means are nearly equal, the between part is nearly zero, and stratification gains almost nothing.

### 2.6 Cluster sampling and the design effect

Cluster sampling trades precision for cost, and the size of the trade is measured by a single number.

> **Definition (Design effect).** The design effect of a sampling design is the ratio of the variance of the estimate under that design to the variance of a simple random sample of the same number of observation units.

> **Result (Design effect for equal clusters).** For one-stage cluster sampling with clusters of equal size $M$ and intra-cluster correlation $\rho$, the design effect is

$$
\text{deff} = 1 + (M-1)\rho .
$$

The intra-cluster correlation $\rho$ is the share of the total variation of the variable that lies between clusters rather than within them. When $\rho$ is zero, neighbours are no more alike than strangers, and the design effect is one: clustering costs nothing. When $\rho$ is one, every member of a cluster is identical and the sample contains no more information than one unit per cluster, so the design effect is $M$.

The effective sample size is the number of independent units that a simple random sample would have needed to match the precision actually obtained.

$$
n_{\text{eff}} = \frac{n}{\text{deff}}
$$

A clustered sample of 300 households with a design effect of 12 carries the information of 25 independently chosen households. Reporting 300 as the sample size is arithmetically true and statistically misleading, and the distinction is exactly what examiners test.

### 2.7 Non-response and its arithmetic

Non-response changes the value of an estimate, and the size of the change has a simple form.

> **Result (Non-response bias).** Let respondents form a proportion $w_r$ of the eligible sample with mean $\bar{y}_r$, and non-respondents a proportion $w_n = 1 - w_r$ with mean $\bar{y}_n$. Then the respondent mean differs from the full-sample mean by

$$
\bar{y}_r - \bar{y} = w_n \left(\bar{y}_r - \bar{y}_n\right).
$$

The bias is a product of two numbers: how many units are missing, and how different the missing units are. Either factor alone is harmless. A survey that misses 40 per cent of a sample is unbiased if the missing units are a random subset, and a survey that misses 2 per cent is badly biased if those 2 per cent are the extremes. This is why response rate alone is a poor certificate of quality.

The arithmetic also governs planning. If the analysis needs $n$ completed interviews and experience suggests a response rate $q$, the number that must be approached is larger than $n$.

$$
n_{\text{approach}} = \frac{n}{q}
$$

### 2.8 How large should the sample be?

Sample size is chosen to achieve a required margin of error, and the formula for a mean is built from the variance formula of Section 2.2.

> **Result (Sample size for a mean).** To estimate a population mean so that the estimate is within $e$ units of the truth with confidence level giving standard normal value $z$, the required sample is the smaller of the two figures obtained from

$$
n_0 = \frac{z^{2}\sigma^{2}}{e^{2}} \quad \text{and} \quad n = \frac{n_0}{1 + \dfrac{n_0}{N}} .
$$

The first figure, $n_0$, is the sample needed from an infinite population. The second divides it by a quantity larger than one, so the finite population correction always reduces the required sample, and the reduction is large exactly when the sample would have been a large share of the population.

For a proportion the same structure applies with the variance of a proportion in place of the variance of a mean.

> **Result (Sample size for a proportion).** To estimate a population proportion so that the estimate is within $e$ of the truth,

$$
n_0 = \frac{z^{2}p(1-p)}{e^{2}}, \qquad n = \frac{n_0}{1 + \dfrac{n_0 - 1}{N}},
$$

and when nothing is known about $p$ the safe choice $p = 0.5$ is used, which maximises $p(1-p)$ and therefore gives the largest and most conservative sample.

### 2.9 The five methods compared

The five methods differ in the unit that carries the randomness, in what they guarantee, and in how they fail. The comparison below sets out the contrasts that questions most often ask for.

| Method | Selection unit | What is guaranteed | Characteristic weakness |
| --- | --- | --- | --- |
| Simple random | the individual unit | equal chance for every unit and every sample | needs a complete frame and is costly to spread |
| Stratified | the individual within each stratum | every stratum represented in a fixed share | needs reliable stratum information before sampling |
| Systematic | the individual at a fixed interval | even spread through the list with a random start | periodic lists produce biased and badly estimated samples |
| Cluster | the whole group | cheap coverage of a scattered population | large design effect when neighbours resemble one another |
| Convenience | whoever is available | nothing | selection bias of unknown size |

## 3. Formal Proofs, Derivations, and Methods

### 3.1 Why the sample mean is unbiased under simple random sampling

Unbiasedness means that if the same design were repeated many times, the average of the sample means would equal the population mean. The proof uses one idea only: an indicator variable that records whether a unit was selected.

Let $I_i$ take the value one when unit $i$ is selected and zero otherwise. Under simple random sampling without replacement, the chance that a particular unit is selected is the sample size divided by the population size, so

$$
P(I_i = 1) = \frac{n}{N} = E(I_i).
$$

The sample mean can be written as a sum over the whole population, with unselected units contributing nothing.

$$
\bar{y} = \frac{1}{n}\sum_{i=1}^{N} I_i\,y_i
$$

Taking expectations and using linearity, which allows the expectation of a sum to be computed term by term, gives

$$
E(\bar{y}) = \frac{1}{n}\sum_{i=1}^{N} E(I_i)\,y_i = \frac{1}{n}\sum_{i=1}^{N} \frac{n}{N}\,y_i = \frac{1}{N}\sum_{i=1}^{N} y_i = \mu .
$$

The final equality says that the average of all population values is the population mean, so the sample mean is unbiased. Nothing was assumed about the shape of the population, and that is the strength of the result: unbiasedness is a property of the selection rule, not of the data.

The same argument gives an unbiased estimator of the population total. Since the sample mean stands for the population mean, multiplying it by the number of population units estimates the total.

$$
\hat{Y} = N \bar{y}, \qquad E(\hat{Y}) = N\mu = Y
$$

### 3.2 Where the finite population correction comes from

The variance formula is proved by writing the variance of the sample mean as a sum of covariance terms between the indicators of different units. Start from the expression of the previous subsection and expand.

$$
\text{Var}(\bar{y}) = \frac{1}{n^{2}}\sum_{i=1}^{N}\sum_{j=1}^{N} \text{Cov}(I_i, I_j)\,y_i\,y_j
$$

Two kinds of term appear. For the same unit twice, the covariance is the variance of an indicator with success probability $n/N$.

$$
\text{Cov}(I_i, I_i) = \frac{n}{N}\left(1 - \frac{n}{N}\right)
$$

For two different units, sampling without replacement makes their indicators negatively related: if one unit is in the sample the other is slightly less likely to be, so

$$
\text{Cov}(I_i, I_j) = -\frac{n}{N}\cdot\frac{N-n}{N}\cdot\frac{1}{N-1} \quad \text{for } i \ne j .
$$

Substituting both into the double sum and grouping the squared terms separately from the cross terms gives

$$
\text{Var}(\bar{y}) = \frac{N-n}{nN^{2}(N-1)}\left[(N-1)\sum_{i=1}^{N} y_i^{2} - \sum_{i \ne j} y_i y_j\right].
$$

The bracket simplifies because the sum of all cross products is the square of the total minus the sum of squares, and after collecting terms it becomes the sum of squared deviations from the population mean multiplied by $N$.

$$
(N-1)\sum_{i=1}^{N} y_i^{2} - \sum_{i \ne j} y_i y_j = N\sum_{i=1}^{N}\left(y_i - \mu\right)^{2}
$$

Dividing by $N-1$ turns the sum of squared deviations into the population variance $\sigma^{2}$, and the remaining factor is recognised as the correction.

$$
\text{Var}(\bar{y}) = \frac{N-n}{nN}\,\sigma^{2} = \frac{\sigma^{2}}{n}\left(1 - \frac{n}{N}\right)
$$

The negative covariance between indicators is the whole content of the correction. Without replacement, choosing one unit makes the others slightly less likely to be chosen, and that mild negative dependence is precisely the extra information that a finite population provides.

A small population can be checked by direct enumeration. Take the six values 2, 4, 6, 8, 10 and 12, whose mean is 7 and whose sum of squared deviations is 70, so that $\sigma^{2} = 70/6$. For samples of size two without replacement there are fifteen possible samples, and their means are 3, 4, 5, 6, 7, 5, 6, 7, 8, 7, 8, 9, 9, 10 and 11. The average of those fifteen means is 7, confirming unbiasedness, and the average of their squared deviations from 7 is

$$
\frac{70}{15} = 4.667,
$$

which agrees with the formula, since $70/15$ equals the product of $4/12$ with $14$, and $14$ is the population variance computed with divisor five.

### 3.3 Why proportional allocation keeps the shares

The rule $n_h = nN_h/N$ is chosen because it makes the sample a scaled copy of the population. The derivation is one line, and the check is the useful part.

$$
\frac{n_h}{n} = \frac{N_h}{N} = W_h .
$$

Because the share of the sample taken from stratum $h$ equals the share of the population in stratum $h$, the weighted average of the stratum means computed from the sample reproduces the population structure exactly. Summing the allocations confirms that nothing is lost or gained in the sharing.

$$
\sum_{h=1}^{H} n_h = \sum_{h=1}^{H} n\frac{N_h}{N} = \frac{n}{N}\sum_{h=1}^{H} N_h = \frac{n}{N}\,N = n
$$

When the products $nN_h/N$ are not whole numbers they must be rounded, and the usual procedure is to round each to the nearest integer and then adjust the largest stratum by the difference so that the total returns to $n$. Presenting the check is worth marks, because it demonstrates that the allocation has been understood rather than merely copied.

### 3.4 The lottery method and the random number table

Simple random sampling needs a device that is genuinely indifferent to the units. Two devices are used, and each has a procedure that can be described in numbered form.

The lottery method is as follows.

1. Assign every unit in the frame a distinct number from 1 to $N$, and write the numbers on slips of identical size, colour, and weight.
2. Place all slips in a container and mix them so that no slip can be identified by touch or position.
3. Draw one slip without looking, record its number, and set the slip aside if sampling is without replacement.
4. Repeat until $n$ distinct numbers have been drawn.
5. Match the recorded numbers to the frame and list the selected units.

The random number table method replaces the container with a printed grid of digits in which every digit from 0 to 9 appears with equal frequency in every position and no pattern links one digit to the next. The procedure is as follows.

1. Decide how many digits are needed to label the largest unit number, which is the number of digits in $N$.
2. Choose a starting row and column by pointing at the table without looking, or by using a further random device.
3. Read the digits in groups of the required length, moving along the row and then to the next row, and treat each group as a candidate number.
4. Discard any group that is zero or exceeds $N$, since no such unit exists in the frame, and discard repeats when sampling without replacement.
5. Stop when $n$ usable numbers have been collected.

A common error is to think that discarding unusable numbers introduces bias. It does not, because the discarded groups correspond to no unit at all and the remaining groups are still equally likely. A second error is to use a table of digits that has been printed with a visible pattern, or a sequence that a human has typed from memory, since human choices are never random.

### 3.5 Selecting a systematic sample from an ordered list

The systematic procedure is short enough to memorise, but each step carries a marking point.

1. Obtain the frame and decide on an order, such as alphabetical, by street, or by date of registration.
2. Compute the interval $k = N/n$, rounding down if necessary.
3. Choose the random start $r$ from the integers 1 to $k$, using a random number table or a computer generator.
4. Select the units in positions $r$, $r+k$, $r+2k$, and continue until $n$ units have been taken, which happens at position $r + (n-1)k$.
5. Check that the last selected position does not exceed $N$, which it cannot if $k$ was computed correctly.

The reason the method is a probability design is the random start. Without it the sample is fixed by the investigator's choice, the design has no known selection probability, and the method degenerates into something closer to judgement sampling. The reason the method can fail is periodicity. If the list repeats a pattern over exactly $k$ positions, the start determines which phase of the pattern is sampled, so the sample is either unusually high or unusually low, and the sample itself contains no trace of the problem.

### 3.6 Where the design effect comes from

The design effect formula follows from splitting total variation into a between-cluster part and a within-cluster part. Let the population consist of $M_c$ clusters of equal size $M$, so that $N = M_cM$, and let $\sigma^{2}$ be the total variance of the variable, with $\sigma_b^{2}$ the part attributable to differences between cluster means and $\sigma_w^{2}$ the part attributable to differences within clusters.

$$
\sigma^{2} = \sigma_b^{2} + \sigma_w^{2}, \qquad \rho = \frac{\sigma_b^{2}}{\sigma^{2}}
$$

When $m$ clusters are selected and every unit inside them is measured, the sample mean is the average of the selected cluster means, so its variance depends only on the between-cluster part.

$$
\text{Var}(\bar{y}_{cl}) = \frac{\sigma_b^{2}}{m}
$$

A simple random sample of the same $n = mM$ units would have variance $\sigma^{2}/n$. Dividing the first by the second gives the design effect, and substituting the definition of $\rho$ simplifies it.

$$
\text{deff} = \frac{\sigma_b^{2}/m}{\sigma^{2}/(mM)} = \frac{M\sigma_b^{2}}{\sigma^{2}} = M\rho
$$

This form is slightly too crude, because the variance between sample cluster means also contains a within-cluster contribution of size $\sigma_w^{2}/M$ whenever cluster sizes are finite; adding that contribution changes $M\rho$ into the familiar expression.

$$
\text{deff} = 1 + (M - 1)\rho
$$

The two extremes confirm the reading. With $\rho = 0$ the design effect is one and clustering is free. With $\rho = 1$ the design effect is $M$, so measuring extra units inside a cluster adds nothing at all.

### 3.7 Deriving the sample size formula

The sample size for a mean follows from setting the margin of error equal to the required precision and solving for $n$. Begin with the standard error including the correction and multiply by the normal value that corresponds to the chosen confidence level.

$$
e = z\sqrt{\frac{\sigma^{2}}{n}\left(1 - \frac{n}{N}\right)}
$$

Squaring both sides removes the root, and expanding the bracket separates the terms containing $n$.

$$
e^{2} = \frac{z^{2}\sigma^{2}}{n} - \frac{z^{2}\sigma^{2}}{N}
$$

Moving the second term to the left and solving for $n$ gives a ratio in which the infinite-population sample appears explicitly.

$$
n = \frac{z^{2}\sigma^{2}}{e^{2} + \dfrac{z^{2}\sigma^{2}}{N}} = \frac{n_0}{1 + \dfrac{n_0}{N}}
$$

The same steps with $p(1-p)$ in place of $\sigma^{2}$ give the formula for a proportion. The only difference is the refined version of the correction, in which $n_0 - 1$ replaces $n_0$, and the difference is immaterial in practice.

Three conventions are worth stating because they are examined. First, $z = 1.96$ corresponds to 95 per cent confidence and $z = 2.58$ to 99 per cent. Second, the computed $n$ is always rounded up, never down, because rounding down misses the target. Third, the population standard deviation $\sigma$ must come from a pilot study, a previous survey, or a range rule in which the range is divided by four or six; a guessed value must be reported, because the sample size is only as trustworthy as the guess.

### 3.8 The four non-probability methods and the bias in each

Four non-probability methods are used widely enough to be examined.

> **Definition (Quota sampling).** Quota sampling fixes the number of respondents required in each category, such as a stated number of young men and older women, and leaves the interviewer to find respondents who fit each quota.

> **Definition (Judgement sampling).** Judgement sampling selects units that the investigator believes are typical, expert, or informative, on the basis of subject knowledge.

> **Definition (Snowball sampling).** Snowball sampling begins with a small group of accessible respondents and asks each of them to name further respondents, so that the sample grows along social links.

> **Definition (Convenience sampling).** Convenience sampling selects whatever units are easiest to reach.

Each method fails in a different way, and the failure can be described precisely. Quota sampling controls the visible composition but not the selection inside each cell, so the interviewer fills quotas with people who are easy to interview, and the resulting bias is invisible in the tabulation. Judgement sampling fails when the investigator's idea of a typical unit is wrong, which is most likely exactly when the population is unfamiliar. Snowball sampling fails because people name people like themselves, so the sample concentrates in dense social clusters and rare or isolated groups are absent. Convenience sampling fails because accessibility is usually related to the variable studied, as when a health survey conducted at a clinic finds more illness than the population contains.

The magnitude of each bias can be computed once the missing group is characterised, and that computation is the only honest way to discuss a non-probability sample.

## 4. Representative Worked Examples and Solutions

### 4.1 Problem: one village, five possible designs

A researcher wishes to study the number of children per family in a village of 350 families and can afford to visit 35 families. Describe how the sample would be chosen under each of the five techniques, and state what each design would allow the researcher to claim.

### 4.2 Solution: five designs and their claims

Step 1. Record the population size and the sample size, and compute the sampling fraction.

$$
\frac{n}{N} = \frac{35}{350} = 0.1
$$

Step 2. For simple random sampling, number the families from 1 to 350 and draw 35 distinct numbers by lottery or from a random number table. Each family then has probability $35/350 = 0.1$ of selection, and the number of possible samples is enormous, so the estimate can be treated as approximately normal.

Step 3. For stratified sampling, suppose the village has three areas with 140, 140 and 70 families. Apply proportional allocation to each area.

$$
n_1 = 35 \times \frac{140}{350} = 14, \qquad n_2 = 35 \times \frac{140}{350} = 14, \qquad n_3 = 35 \times \frac{70}{350} = 7
$$

The three parts sum to $14 + 14 + 7 = 35$, as required. Draw a separate random sample inside each area.

Step 4. For systematic sampling, compute the interval and draw a random start.

$$
k = \frac{350}{35} = 10
$$

If the random start is the fourth family, the selected families occupy positions 4, 14, 24, and so on up to position 344. Exactly one family is taken from each block of ten.

Step 5. For cluster sampling, suppose the village consists of ten hamlets of about 35 families each. Select one hamlet at random and visit every family inside it. The realised sample size is whatever that hamlet contains, and the design is a probability design at the level of hamlets, not families.

Step 6. For convenience sampling, visit the families nearest the field base, or those at home in the afternoon, until 35 responses have been collected. Nothing about the selection is random.

Step 7. Interpret the claims. The random, stratified and systematic designs each give a known selection probability and therefore support an estimate with a computable standard error. The cluster design supports an estimate of the village mean but with a standard error computed from the variation between hamlets, which is larger than the arithmetic suggests. The convenience design supports only a description of the families interviewed, because no probability of selection is known and the bias cannot be quantified.

### 4.3 Problem: a stratified sample and the precision it buys

A trading survey covers 600 businesses in three strata: 300 small businesses with stratum standard deviation 6, 200 medium businesses with stratum standard deviation 10, and 100 large businesses with stratum standard deviation 16. The budget allows 60 interviews. Compute the proportional allocation, the variance of the stratified estimate, the variance of a simple random sample of the same size, and the size of the gain, taking the population variance as 207.89.

### 4.4 Solution: allocation, variances and gain

Step 1. Compute the stratum weights, which are the shares of the population in each stratum.

$$
W_1 = \frac{300}{600} = 0.5, \qquad W_2 = \frac{200}{600} = 0.3333, \qquad W_3 = \frac{100}{600} = 0.1667
$$

Step 2. Apply proportional allocation with $n = 60$.

$$
n_1 = 60(0.5) = 30, \qquad n_2 = 60(0.3333) = 20, \qquad n_3 = 60(0.1667) = 10
$$

The parts sum to 60, so the allocation is complete.

Step 3. Compute the weighted within-stratum variance, which is the quantity that drives the stratified variance.

$$
\sum_{h=1}^{3} W_h \sigma_h^{2} = 0.5(36) + 0.3333(100) + 0.1667(256) = 18 + 33.33 + 42.67 = 94.00
$$

Step 4. Compute the finite population correction, which is common to all strata because proportional allocation gives every stratum the same sampling fraction.

$$
1 - f = 1 - \frac{60}{600} = 1 - 0.1 = 0.9
$$

Step 5. Compute the variance and standard error of the stratified estimate.

$$
\text{Var}(\bar{y}_{st}) = \frac{0.9}{60}(94.00) = 0.015(94.00) = 1.41, \qquad \text{SE} = \sqrt{1.41} = 1.187
$$

Step 6. Compute the variance of a simple random sample of 60, using the population variance of 207.89.

$$
\text{Var}(\bar{y}_{srs}) = \frac{0.9}{60}(207.89) = 0.015(207.89) = 3.118, \qquad \text{SE} = \sqrt{3.118} = 1.766
$$

Step 7. Compute the gain as the ratio of the two variances.

$$
\frac{\text{Var}(\bar{y}_{st})}{\text{Var}(\bar{y}_{srs})} = \frac{94.00}{207.89} = 0.452
$$

Step 8. Interpret. The stratified estimate has 45.2 per cent of the variance of the plain random sample, so the variance is reduced by 54.8 per cent, and the standard error by about one third. The reduction is large because the stratum means differ considerably, so most of the population variation lies between strata and is eliminated by the design. The remaining variation, 94.00 out of 207.89, is the variation inside strata, which no allocation can remove.

### 4.5 Problem: a systematic sample on a list with a repeating pattern

A list holds 2000 households in 100 blocks of 20 positions each. In every block, the household in position 20 is a corner shop with monthly expenditure of 900 units, and the other nineteen households each spend 300 units. A systematic sample of 100 households is drawn with interval 20. Find the population mean, the sample mean for each possible start, and the consequence for the reported standard error.

### 4.6 Solution: an unbiased design with a hopeless estimate

Step 1. Compute the population mean by averaging the block pattern.

$$
\mu = \frac{19(300) + 900}{20} = \frac{5700 + 900}{20} = \frac{6600}{20} = 330
$$

Step 2. Enumerate the possible samples. The interval 20 equals the block length, so a start of 20 selects only corner shops, and every other start selects only ordinary households.

$$
\bar{y}_{r=20} = 900, \qquad \bar{y}_{r \ne 20} = 300
$$

Step 3. Average over the random start to check for bias.

$$
E(\bar{y}) = \frac{19(300) + 900}{20} = 330 = \mu
$$

Step 4. Compute the variance over the random start.

$$
E(\bar{y}^{2}) = \frac{19(300^{2}) + 900^{2}}{20} = \frac{19(90000) + 810000}{20} = \frac{1710000 + 810000}{20} = 126000
$$

$$
\text{Var}(\bar{y}_{sys}) = 126000 - 330^{2} = 126000 - 108900 = 17100, \qquad \text{SE} = 130.8
$$

Step 5. Inspect what the sample itself reports. When the start is 20, all hundred selected households spend exactly 900 units, so the sample standard deviation is zero and any standard error computed from the sample is also zero, while the sample mean is 570 units away from the truth.

Step 6. Interpret. The design is unbiased in the long run, since the average over starts equals the population mean, but a single realised sample can be catastrophically wrong and, worse, gives no warning. The remedy is to break the period: randomise the order of the list, use several random starts with a smaller interval, or switch to a stratified or random design. A periodic list makes the variance formula for simple random sampling invalid, and quoting its standard error would be a serious error.

### 4.7 Problem: the cost of clustering

A household survey selects 15 villages at random from 300 villages and interviews all 20 households in each selected village, giving 300 households. The variance between village means is 900 and the population variance of household expenditure is 1500. Compute the variance under the cluster design, the variance of a simple random sample of 300 households, the design effect and the effective sample size.

### 4.8 Solution: variance, design effect and effective sample size

Step 1. Compute the correction for the number of villages selected.

$$
1 - \frac{m}{M_c} = 1 - \frac{15}{300} = 1 - 0.05 = 0.95
$$

Step 2. Compute the variance of the cluster sample mean from the between-village variance, because all households in a selected village are measured.

$$
\text{Var}(\bar{y}_{cl}) = \frac{0.95(900)}{15} = \frac{855}{15} = 57.00, \qquad \text{SE} = 7.55
$$

Step 3. Compute the variance of a simple random sample of the same 300 households.

$$
\text{Var}(\bar{y}_{srs}) = \frac{1500}{300}\left(1 - \frac{300}{6000}\right) = 5(0.95) = 4.75, \qquad \text{SE} = 2.18
$$

Step 4. Compute the design effect as the ratio of the two variances.

$$
\text{deff} = \frac{57.00}{4.75} = 12.0
$$

Step 5. Compute the effective sample size.

$$
n_{\text{eff}} = \frac{300}{12.0} = 25
$$

Step 6. Recover the intra-cluster correlation from the design effect, using cluster size 20.

$$
1 + 19\rho = 12.0 \quad \text{so} \quad \rho = \frac{11}{19} = 0.579
$$

Step 7. Interpret. Nearly 58 per cent of the variation in expenditure lies between villages, so village members resemble one another strongly. The 300 interviews carry the information of 25 independent interviews, and the honest description of the survey is that its sample size is 15 villages, not 300 households. To improve precision the survey should add villages rather than households, since a twenty-first household in an already selected village adds almost nothing.

### 4.9 Problem: sample size for a mean with a finite population

A survey must estimate mean monthly transport spending so that the estimate is within 50 units of the truth with 95 per cent confidence. The standard deviation is believed to be 200 units and the population contains 1200 households. Find the required sample, and check the answer.

### 4.10 Solution: two stages and a verification

Step 1. Compute the sample required from an infinite population, using $z = 1.96$.

$$
n_0 = \frac{z^{2}\sigma^{2}}{e^{2}} = \frac{3.8416(40000)}{2500} = \frac{153664}{2500} = 61.47
$$

Step 2. Apply the finite population correction.

$$
n = \frac{n_0}{1 + \dfrac{n_0}{N}} = \frac{61.47}{1 + \dfrac{61.47}{1200}} = \frac{61.47}{1.0512} = 58.47
$$

Step 3. Round up, since a fraction of a household cannot be interviewed.

$$
n = 59
$$

Step 4. Verify by substituting the chosen sample into the standard error formula.

$$
\text{SE} = \sqrt{\frac{40000}{59}\left(1 - \frac{59}{1200}\right)} = \sqrt{678.0(0.9508)} = \sqrt{644.6} = 25.39
$$

Step 5. Compute the margin of error and compare it with the requirement.

$$
1.96(25.39) = 49.8 \le 50
$$

Step 6. Interpret. Fifty-nine households meet the specification, and the check confirms that 58 would have failed, since it gives a margin of about 50.2. The correction saved only three households because the sample is a small share of the population, which is the usual situation and the usual size of the saving.

### 4.11 Problem: sample size for a proportion with a finite population

A survey must estimate the proportion of households using a particular service to within 0.05 with 95 per cent confidence. Nothing is known about the proportion, and the population contains 800 households. Find the sample and verify it.

### 4.12 Solution: the conservative choice of proportion

Step 1. Choose the value of $p$ that maximises the variance, since nothing is known.

$$
p = 0.5, \qquad p(1-p) = 0.25
$$

Step 2. Compute the infinite-population sample.

$$
n_0 = \frac{3.8416(0.25)}{0.0025} = \frac{0.9604}{0.0025} = 384.16
$$

Step 3. Apply the finite population correction.

$$
n = \frac{384.16}{1 + \dfrac{384.16 - 1}{800}} = \frac{384.16}{1 + 0.4790} = \frac{384.16}{1.4790} = 259.7
$$

Step 4. Round up to 260.

Step 5. Verify the margin of error obtained.

$$
1.96\sqrt{\frac{0.25}{260}\left(1 - \frac{260}{800}\right)} = 1.96\sqrt{0.0009615(0.675)} = 1.96(0.02548) = 0.0499
$$

Step 6. Interpret. The margin is 0.0499, just inside the requirement, and 259 would have produced 0.0501 and failed. The correction removed about 124 households, close to a third of the uncorrected figure, because the sample was planned to be a large share of a small population.

### 4.13 Problem: planning around non-response

A survey needs 400 completed interviews. Experience in similar studies suggests that 68 per cent of approached households cooperate, and that non-respondents spend on average 10 units more than respondents. Find the number of households to approach and the size of the non-response bias.

### 4.14 Solution: response rate and bias arithmetic

Step 1. Inflate the required number of completions by the expected response rate.

$$
n_{\text{approach}} = \frac{400}{0.68} = 588.2
$$

Step 2. Round up, since a fraction of a household cannot be approached.

$$
n_{\text{approach}} = 589
$$

Step 3. Compute the weight of the non-respondents in the eligible sample.

$$
w_n = 1 - 0.68 = 0.32
$$

Step 4. Compute the bias in the respondent mean.

$$
\bar{y}_r - \bar{y} = w_n\left(\bar{y}_r - \bar{y}_n\right) = 0.32\left(-10\right) = -3.2
$$

Step 5. Interpret. The respondent mean understates the population mean by about 3.2 units, which is a quarter of a standard deviation in many expenditure surveys and is not removable by enlarging the sample. Reducing the bias requires raising the response rate, for example by call-backs, or measuring a subsample of non-respondents so that the correction can be estimated.

## 5. Mathematical Extensions, Limits, and Common Errors

### 5.1 Two limits of the finite population correction

The correction factor behaves in two instructive ways at the boundaries of its range. As the sampling fraction goes to zero, which describes a small sample from a very large population, the correction goes to one and the variance formula reduces to the familiar form for independent observations.

$$
\lim_{n/N \to 0} \frac{\sigma^{2}}{n}\left(1 - \frac{n}{N}\right) = \frac{\sigma^{2}}{n}
$$

As the sampling fraction goes to one, which describes a census, the correction goes to zero and the variance vanishes, so the sample mean equals the population mean with certainty.

$$
\lim_{n \to N} \frac{\sigma^{2}}{n}\left(1 - \frac{n}{N}\right) = 0
$$

The second limit is the formal statement that a census has no sampling error. It is also the source of a common misunderstanding, because a census still has coverage, non-response and measurement error, and a surveyor who reports "no error" after a census has confused one component of total error with the whole of it.

### 5.2 What each design cannot do

Each design has a limit that no amount of arithmetic can overcome, and stating the limit is often the most valuable sentence in an answer.

Simple random sampling cannot be implemented without a complete frame, and it becomes impractical when the population is scattered over a wide area, because the selected units are spread across the whole territory and travel costs dominate the budget. Stratified sampling cannot correct a frame that omits a stratum entirely, and it loses its advantage when the stratification variable is unrelated to the variable of interest, in which case the extra administrative work buys nothing. Systematic sampling cannot protect against a periodicity that matches the interval, and it cannot be used at all on a list whose order is unknown or changing during the survey. Cluster sampling cannot deliver the precision of a random sample of the same size when clusters are internally homogeneous, and it cannot estimate the design effect at all when only a handful of clusters has been selected, which is why cluster surveys aim for at least thirty clusters. Convenience sampling cannot support an inference about the population, although it can be useful for piloting a questionnaire, for testing field procedures, and for studying a group that is hard to reach by any other route.

### 5.3 Beginner misconceptions worth correcting now

Several beliefs are so natural that they recur every year, and each is stated here with the correction that removes it.

- **"A bigger sample is always more accurate."** Size reduces sampling error only. A huge convenience sample from a narrow place is a precise measurement of the wrong population, and a huge sample with a faulty question is a precise measurement of the wrong thing.
- **"A sample is only valid if it is a fixed percentage of the population."** There is no rule of that kind. A sample of 1000 from a population of one million and a sample of 1000 from a population of ten thousand have almost the same precision, because precision depends on the number selected, not on the share selected, once the share is small.
- **"Random means haphazard."** Random selection is a specific procedure in which every unit has a known chance. Choosing units "at random" by eye, or asking for volunteers, produces no known chance at all.
- **"Stratified and cluster sampling are the same because both use groups."** In stratified sampling every group is sampled and only part of each group is measured. In cluster sampling only some groups are selected and every unit in the selected groups is measured.
- **"The sample mean is the population mean plus or minus the standard error."** The standard error describes the spread of the estimate over repeated samples. A single sample gives a range of plausible values, and the range must be stated as an interval with a confidence level, not as a certainty.
- **"Non-response is cured by a larger sample."** A larger sample raises the number of respondents and the number of non-respondents in the same proportion, so a bias caused by the difference between them is unchanged.
- **"A census has no error."** A census has no sampling error and can have every other kind, often in larger measure because it is large and hurried.
- **"Rounding the stratum allocations in any direction is acceptable."** Rounding must be reconciled so that the allocations sum exactly to the planned sample, and the reconciliation must be shown.
- **"The design effect is a technicality."** In cluster surveys the design effect is often between two and twenty, so a survey that ignores it can overstate its precision by a factor of four or more.
- **"Any ordered list can be sampled systematically."** A list ordered in a cycle, such as a register that repeats a pattern every week or every street block, can produce a sample that is entirely from one phase of the cycle.

### 5.4 A synthesis of the topic

The topic has a single architecture, and every question about it can be answered by locating the scenario on that architecture. A question fixes a population and a variable. A frame makes the population reachable, and the gap between population and frame is coverage error. A selection rule turns the frame into a sample, and the rule determines whether the design is a probability design with computable error or a non-probability design with unquantified bias. The sample yields respondents, and the gap between sample and respondents is non-response error. The respondents yield measurements, and the gap between measurement and truth is measurement error.

The five syllabus designs are five answers to the question of how to turn a frame into a sample. Simple random sampling answers it with equal chances and serves as the benchmark against which the others are measured. Stratified sampling answers it by fixing the composition of the sample and removing the between-group variation. Systematic sampling answers it with a cheap, evenly spread rule that is excellent on a well-ordered list and dangerous on a periodic one. Cluster sampling answers it by buying cheap coverage at the price of the design effect. Convenience sampling answers it by abandoning the question altogether, which is sometimes the only affordable option and never a basis for inference.

The arithmetic follows from that architecture rather than standing beside it. The variance of a sample mean has the form of a variance divided by the number of independent observations, multiplied by a correction that records how much of the population has been used, and multiplied again by a design effect that records how much the observations resemble one another. Sample size formulas invert that variance to discover how many observations are needed. Non-response arithmetic shows what happens when the observations that were planned do not arrive. Once those four ideas are in place, the formulas reduce to substitutions, and the judgements that examinations test reduce to identifying which of the four ideas a particular scenario has disturbed.
