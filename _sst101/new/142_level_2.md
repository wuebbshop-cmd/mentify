## 1. Foundational Concepts, Definitions, and Axioms

### 1.1 The collection problem stated formally

Data collection is the process by which a researcher obtains measurements on one or more variables for a set of units, in such a way that the measurements can later be organised, summarised, analysed, and interpreted. Statistics is the science of data, and its descriptive branch uses numerical and graphical methods to look for patterns in a data set and present that information in a convenient form, while its inferential branch uses sample data to make estimates, decisions, predictions, or other generalisations about a larger set of data. Collection is the stage at which both branches are constrained: a descriptive summary can be no better than the records it summarises, and an inference can be no better than the design that produced those records.

It is useful to state the collection problem as a formal object, because every design decision is a decision about one of its components.

> **Definition (Collection problem).** A collection problem consists of a target population $U$, a variable $Y$ defined on each unit of $U$, a sampling frame $F$ listing the units that can actually be selected, a selection mechanism that chooses a subset $s \subseteq F$, and a measurement instrument that maps each selected unit to a recorded value.

Four objects therefore have to be distinguished even when the words sound alike: the population $U$ about which a claim is wanted, the frame $F$ from which the sample is actually drawn, the sample $s$ that is actually selected, and the set of respondents $r \subseteq s$ that actually supply data. Coverage error arises when $F$ omits part of $U$; sampling error arises because $s$ is smaller than $F$; non-response error arises because $r$ is smaller than $s$; measurement error arises because the recorded value is not the true value of $Y$.

### 1.2 Core definitions

> **Definition (Population).** A population is the set of all units, usually people, objects, transactions, or events, that we are interested in studying. It is fixed by the research question, not by geography or size.

> **Definition (Variable).** A variable is a characteristic or property of an individual population unit. It is the thing measured; a particular value of it is an observation.

> **Definition (Sample).** A sample is a subset of the units of a population.

> **Definition (Statistical inference).** A statistical inference is an estimate, prediction, or other generalisation about a population based on information contained in a sample.

> **Definition (Measure of reliability).** A measure of reliability is a statement, usually attached to a statistical inference, that quantifies the confidence the inference deserves.

> **Definition (Parameter and estimator).** A parameter is a numerical characteristic of the population, conventionally written with a Greek letter such as $\mu$ for a mean or $\pi$ for a proportion. An estimator is a rule that computes a numerical characteristic of a sample, conventionally written with a Roman letter such as $\bar{y}$ or $p$, in order to estimate the parameter.

The distinction between parameter and estimator is the formal content of the phrase "measure of reliability". An estimator is a random variable, because a different sample would produce a different value; a parameter is a fixed unknown number. A statement of reliability describes the behaviour of the estimator across repeated samples, which is why it can be quantified while the parameter itself cannot be observed.

> **Definition (Sampling frame).** A sampling frame is the concrete list, register, map, or procedure from which sample units are selected. It is the operational counterpart of the population, and the two coincide only in the best-designed studies.

> **Definition (Sampling unit and observation unit).** A sampling unit is the entity that is selected by the sampling mechanism; an observation unit is the entity on which the measurement is taken. The two differ whenever sampling is clustered, as when households are selected and every adult within each household is measured.

> **Definition (Census and sample survey).** A census measures every unit in the frame; a sample survey measures a subset. A census removes sampling error and does not remove coverage, non-response, or measurement error, which is why a census is not automatically more accurate than a well-run sample survey.

### 1.3 Primary and secondary data

> **Definition (Primary data).** Primary data are data collected by the investigator, or under the investigator's direction, for the specific purpose of the study in hand.

> **Definition (Secondary data).** Secondary data are data collected by another party for another purpose, and subsequently used by the investigator.

The distinction is about provenance and purpose, not about medium. A database purchased from a commercial supplier is secondary; a set of interview transcripts produced by the investigator's own team is primary. Three consequences follow, and each is examinable.

First, primary collection gives control over definitions. The investigator decides what counts as an unemployed person, what period a recall question covers, and which units are eligible.

Second, secondary collection gives economy but surrenders control. The definitions may not match, the collection date may be wrong for the question, and the sampling design may be undocumented, so the reliability statement that accompanies any inference from such data is correspondingly weaker.

Third, secondary data are often the only feasible source for questions about the past or about very large populations. Where a national statistical office has already run a census, re-collecting the data would be wasteful, and re-analysis is the correct scientific response.

### 1.4 The four routes by which data are obtained

Data can generally be obtained in four ways, and the classification is exhaustive because it partitions on a single question: did the investigator create the conditions of measurement?

- **From a published source.** The data already exist in a report, register, or archive. The investigator's role is selection and interpretation. Such data are secondary.
- **From a designed experiment.** The investigator assigns treatments to units and measures the response. The assignment is under the investigator's control.
- **From a survey.** The investigator questions a defined set of respondents, using a questionnaire, an interview schedule, or both.
- **Observationally.** The investigator records the units as they naturally are, without assigning any treatment.

The route determines the logical status of the conclusion. Only the designed experiment supports a direct causal claim, because only there is the assignment of the putative cause under the investigator's control. The survey and observational routes can establish association, prevalence, and change over time; they cannot, unaided, separate the effect of one factor from the effects of the others on which the groups differ.

| Route | Who creates the conditions | Typical instrument | Maximal conclusion |
| --- | --- | --- | --- |
| Published source | Another party, previously | Document or database | Description of the recorded population |
| Designed experiment | The investigator, by assignment | Treatment protocol and measurement schedule | Causal effect in the experimental setting |
| Survey | The investigator, by questioning only | Questionnaire or interview schedule | Prevalence and association in the population |
| Observational study | Nobody; conditions occur naturally | Observation record or instrument | Association and prediction |

### 1.5 The five methods

> **Definition (Survey).** A survey is a collection method in which a standardised set of questions is administered to a defined set of respondents in order to describe their characteristics, attitudes, or behaviour. The survey is the design; the questionnaire and the interview schedule are instruments used within it.

> **Definition (Experiment).** An experiment is a collection method in which the investigator deliberately imposes a treatment on the units and observes the response, with the assignment of treatments controlled so that the effect of the treatment can be separated from other sources of variation.

> **Definition (Observational study).** An observational study is a collection method in which the investigator records characteristics, exposures, or behaviours of units as they occur, without imposing any treatment and without controlling the assignment of exposure.

> **Definition (Interview).** An interview is a collection method in which a researcher questions a respondent directly, in person or by telephone, recording the spoken answers. Its defining property is that the interviewer can clarify, probe, and follow up.

> **Definition (Questionnaire).** A questionnaire is a written instrument consisting of a fixed set of items, completed by the respondent or read out verbatim by an interviewer, used to collect standardised information.

The five are related rather than opposed. A survey may be administered as a self-completed questionnaire, as a structured interview, or as a mixture in which an interviewer delivers the questionnaire to respondents who cannot read. An experiment may use a questionnaire as its measurement instrument, and an observational study may use a structured observation schedule that functions like a questionnaire addressed to behaviour rather than to opinion.

### 1.6 Measurement scales and admissible summaries

The instrument determines the scale of the variable, and the scale determines which statistics are legitimate.

- **Nominal** measurements differ only in category, with no order. The only admissible summaries are frequencies, proportions, and modes.
- **Ordinal** measurements carry a meaningful order but no meaningful distance. Medians, percentiles, and rank statistics are admissible; the arithmetic mean is not, strictly speaking.
- **Interval** measurements have equal distances and an arbitrary zero. Means, standard deviations, and differences are admissible; ratios are not.
- **Ratio** measurements have equal distances and a true zero. All arithmetic, including ratios and coefficients of variation, is admissible.

The practical consequence for design is that a coarsened item destroys information irreversibly. An income item with six broad bands produces ordinal data; a respondent recorded in the band "20 000 to 29 999" can never afterwards be located within that band. Coarsening is often justified by refusal rates on exact-income questions, which is a real trade-off between measurement error and item non-response, but it must be a deliberate trade-off.

### 1.7 The axioms of the collection stage

Four properties are assumed, rather than proved, in everything that follows.

> **Axiom 1 (Unit coverage).** Every unit in the frame is eligible for selection with a known, strictly positive probability.

Known selection probabilities are what make a design-based estimator possible, because each respondent can then be weighted by the reciprocal of its selection probability. A convenience sample violates this axiom, and the consequence is that no design-based standard error can be computed for it.

> **Axiom 2 (Instrument consistency).** The instrument is administered in the same way to every respondent within a mode, so that differences between recorded answers reflect differences between respondents rather than differences between interviews.

> **Axiom 3 (Exhaustive and exclusive classification).** Every record is assigned to exactly one category of every classification applied to it, so that frequencies sum to the number of records.

> **Axiom 4 (Error additivity).** The error of an estimate can be decomposed into components attributable to coverage, sampling, non-response, and measurement, and the components may be examined separately.

The fourth axiom is a modelling convenience rather than a law of nature; the components interact, as when non-response is concentrated among units that the frame covers poorly. It remains the organising principle of survey methodology because it tells the investigator where to look.

### 1.8 The four design principles of an experiment

> **Principle 1 (Control).** Hold constant, or deliberately vary, every factor other than the treatment that could affect the response, and include a comparison condition that receives no treatment or a standard treatment.

> **Principle 2 (Randomisation).** Assign units to treatment conditions by a random mechanism with known probabilities, so that the distribution of every characteristic of the units, measured or unmeasured, is balanced across conditions in expectation.

> **Principle 3 (Replication).** Apply each treatment to several independent units, so that the treatment means are estimated precisely and the residual variation can itself be estimated.

> **Principle 4 (Blocking).** When a nuisance characteristic is known in advance to affect the response, form homogeneous groups of units and randomise treatments within each group, so that between-group variation is removed from the comparison.

The principles are not stylistic preferences. Each closes a specific route by which a comparison can mislead: control removes competing explanations, randomisation removes systematic selection into conditions, replication removes the confusion of a real effect with random noise, and blocking removes the waste caused by a known source of heterogeneity.

### 1.9 Instrument properties: reliability and validity

> **Definition (Reliability).** The reliability of an instrument is the consistency of its measurements, formally the proportion of observed variance attributable to true differences between units.

> **Definition (Validity).** The validity of an instrument is the degree to which it measures the construct it is intended to measure.

Four kinds of validity are distinguished, and each is evidenced differently.

- **Face validity** is the judgement that the items appear to measure the construct. It is necessary for respondent cooperation and is not evidence of correctness.
- **Content validity** is the judgement that the items cover the full domain of the construct, with no important aspect omitted and no irrelevant aspect included. It is established by expert review against a specification.
- **Criterion validity** is the correlation between the instrument and an independent criterion measured at the same time, called concurrent validity, or later, called predictive validity.
- **Construct validity** is the extent to which the instrument behaves as the theory of the construct requires, correlating with measures of related constructs and not correlating with measures of unrelated ones.

Reliability is necessary but not sufficient for validity. An instrument that is perfectly consistent but systematically displaced from the truth is reliable and invalid, exactly as a scale reading two kilograms too high is reliable and invalid. The converse failure also occurs: an instrument can measure the right construct noisily, in which case it is valid in intent and unreliable in practice.

### 1.10 Notation used throughout

| Symbol | Meaning |
| --- | --- |
| $N$ | number of units in the population or frame |
| $n$ | number of units selected into the sample |
| $r$ | number of units that supply a usable record |
| $y_i$ | value of the variable for unit $i$ |
| $\bar{y}$ | sample mean of the variable |
| $\mu$ | population mean of the variable |
| $\pi$ | population proportion in a category |
| $\sigma^{2}$ | variance of a single observation |
| $\tau$ | causal effect of a treatment |
| $\rho$ | intra-class correlation, or reliability, depending on context |

## 2. Theorems, Lemmas, and Analytical Properties

### 2.1 The bias decomposition of survey error

> **Theorem 1 (Decomposition of total survey error).** Let $\hat{\theta}$ estimate a population quantity $\theta$ under a design with frame $F$, sample $s$, respondents $r$, and instrument $M$. Then the mean squared error of $\hat{\theta}$ decomposes into a variance component and a sum of squared bias components attributable to coverage, non-response, and measurement, so that
>
> $$
> \text{MSE}\left(\hat{\theta}\right) = \text{Var}\left(\hat{\theta}\right) + B_{c}^{2} + B_{n}^{2} + B_{m}^{2} ,
> $$
>
> where $B_{c}$ is coverage bias, $B_{n}$ is non-response bias, and $B_{m}$ is measurement bias.

The theorem is the formal statement that accuracy has two independent dimensions. Variance, which is the sampling component, falls as the sample grows. The three bias components do not, because they arise from units that the design systematically fails to represent or from answers that systematically misreport. A design can therefore be made arbitrarily precise while remaining wrong, which is the single most important practical lesson of the subject.

### 2.2 The non-response bias identity

> **Theorem 2 (Non-response bias).** Let respondents form a proportion $w_r$ of the eligible sample with mean $\bar{y}_{r}$, and non-respondents a proportion $w_n = 1 - w_r$ with mean $\bar{y}_{n}$. Then the respondent mean differs from the full-sample mean by
>
> $$
> \bar{y}_{r} - \bar{y} = w_n\left(\bar{y}_{r} - \bar{y}_{n}\right).
> $$

The identity shows that the damage done by non-response is the product of two quantities: how many units are missing, and how different the missing units are. Either factor alone is harmless. A survey with a 40 per cent non-response rate is unbiased if the missing units are a random subset of the sample, and a survey with a 5 per cent non-response rate can be badly biased if the missing units are the extreme ones.

### 2.3 The weighted-mean lemma

> **Lemma (Weighted decomposition).** For any partition of a set into groups $g = 1, \dots, G$ with proportions $w_g$ summing to one and means $\bar{y}_{g}$, the overall mean is
>
> $$
> \bar{y} = \sum_{g=1}^{G} w_g \bar{y}_{g} .
> $$

Every result about non-response, coverage, and standardisation is an application of this lemma. Standardisation is nothing more than the deliberate replacement of the observed weights $w_g$ by a common set of weights applied to both comparison groups, so that the groups are compared at the same mix.

### 2.4 Unbiasedness of the randomised comparison

> **Theorem 3 (Unbiasedness under randomisation).** Let unit $i$ have potential outcomes $y_i(1)$ and $y_i(0)$ under treatment and control, with individual effect $\tau_i = y_i(1) - y_i(0)$. If each of $n$ units is assigned to treatment independently with probability $p$, then the difference in sample means satisfies
>
> $$
> E\left(\bar{y}_{T} - \bar{y}_{C}\right) = \bar{\tau} ,
> $$
>
> where $\bar{\tau}$ is the average of the individual effects over the units in the study.

The theorem is the formal licence for causal language. Its content is that the comparison is unbiased for the average effect on the units studied, whatever the distribution of unmeasured characteristics, because the assignment mechanism is independent of those characteristics.

### 2.5 Variance of the randomised comparison and the replication law

> **Theorem 4 (Variance of the difference in means).** Under the same assignment mechanism with $n_T$ treated and $n_C$ control units, and with unit-level outcome variance $\sigma^{2}$ within each condition,
>
> $$
> \text{Var}\left(\bar{y}_{T} - \bar{y}_{C}\right) = \sigma^{2}\left(\frac{1}{n_T} + \frac{1}{n_C}\right).
> $$

> **Corollary (Square-root law of replication).** With equal allocation so that $n_T = n_C = n/2$, the standard error of the difference is
>
> $$
> \text{SE} = 2\sigma\sqrt{\frac{1}{n}} ,
> $$
>
> so precision improves only as the square root of the total number of units.

The corollary quantifies the cost of evidence. To halve the standard error of a treatment comparison, the number of units must be quadrupled, so an experiment that is marginally inconclusive at forty units needs about one hundred and sixty to become decisive at the same effect size.

### 2.6 The blocking efficiency theorem

> **Theorem 5 (Variance reduction by blocking).** Suppose the response has variance $\sigma^{2}$, of which a proportion $\rho$ is attributable to differences between blocks. Then the variance of the estimated treatment difference in a randomised complete block design is reduced relative to a completely randomised design by the factor
>
> $$
> 1 - \rho ,
> $$
>
> so the relative efficiency of blocking is $\frac{1}{1-\rho}$.

When blocks explain half the variation, so that $\rho = 0.5$, blocking doubles the effective precision: the same number of units yields a standard error smaller by a factor of $\sqrt{2}$. When blocks explain nothing, so that $\rho = 0$, blocking costs a few degrees of freedom and gains nothing, which is why blocking is only worth arranging when the nuisance factor is known in advance to matter.

### 2.7 The omitted-variable bias formula

> **Theorem 6 (Omitted-variable bias).** Let the response depend on a treatment $T$ and a confounder $Z$ according to $y = \alpha + \tau T + \beta Z + \varepsilon$, and let the regression of $Z$ on $T$ have slope $\delta$. Then the difference in means, or the slope from a regression of $y$ on $T$ alone, estimates
>
> $$
> \tau + \beta\delta ,
> $$
>
> so the bias is the product of the confounder's effect on the response and the confounder's association with the treatment.

The formula is the analytical form of the confounding identity. It also explains why the formula is a warning rather than a remedy: $\beta$ and $\delta$ are both unknown in an observational study, so the bias cannot be subtracted unless the confounder is measured, and unmeasured confounders leave an irreducible ambiguity.

### 2.8 The Horvitz–Thompson estimator

> **Lemma (Horvitz–Thompson unbiasedness).** Let unit $i$ be selected with probability $\pi_i > 0$ and let $I_i$ indicate selection. Then for any variable with population total $Y$,
>
> $$
> \hat{Y}_{HT} = \sum_{i=1}^{N} \frac{I_i y_i}{\pi_i}
> $$
>
> satisfies $E\left(\hat{Y}_{HT}\right) = Y$.

The lemma is the formal justification for weighting. Each sampled unit stands for $1/\pi_i$ units of the population, so a unit that was unlikely to be selected carries more weight. The same logic underlies the correction of survey data for unequal selection probabilities and for differential non-response.

### 2.9 Reliability, the reliability ratio, and attenuation

> **Theorem 7 (Classical test theory).** Let the observed score satisfy $X = T + E$ with $E(E) = 0$ and $\text{Cov}(T, E) = 0$. Then the reliability of the instrument is
>
> $$
> \rho_{XX} = \frac{\sigma_{T}^{2}}{\sigma_{T}^{2} + \sigma_{E}^{2}} ,
> $$
>
> and for any correlated variable $Y$ measured without error,
>
> $$
> r_{XY} = r_{TY}\sqrt{\rho_{XX}} .
> $$

The second statement is the attenuation formula. It says that an unreliable instrument systematically understates every relationship in which it is used, and that the understatement is governed by the square root of the reliability rather than by the reliability itself.

> **Theorem 8 (Cronbach's coefficient as a lower bound).** For $k$ items with average inter-item covariance $\bar{c}$ and average item variance $\bar{v}$,
>
> $$
> \alpha = \frac{k\bar{c}}{\bar{v} + \left(k-1\right)\bar{c}} ,
> $$
>
> and $\alpha \le \rho_{XX}$, with equality when the items are essentially parallel.

The inequality matters in practice. A reported coefficient of $0.8$ is evidence that reliability is at least $0.8$, not that it is exactly $0.8$, so a scale with a coefficient of $0.7$ may still be adequate if the items are known to be heterogeneous in difficulty.

### 2.10 Standard errors, design effects, and sample size

> **Corollary (Standard error of a proportion).** For a simple random sample of $n$ respondents and an observed proportion $p$,
>
> $$
> \text{SE}\left(p\right) = \sqrt{\frac{p\left(1-p\right)}{n}}\sqrt{1 - \frac{n}{N}} .
> $$

> **Corollary (Design effect).** For a clustered design with average cluster size $m$ and intra-class correlation $\rho$, the design effect is
>
> $$
> \text{deff} = 1 + \left(m-1\right)\rho ,
> $$
>
> and the effective sample size is $n/\text{deff}$.

> **Corollary (Sample size for a proportion).** The number of respondents needed to achieve a margin of error $e$ at confidence level determined by $z$ is
>
> $$
> n = \frac{z^{2}\pi\left(1-\pi\right)}{e^{2}} ,
> $$
>
> evaluated at the anticipated $\pi$ and rounded upwards.

These three results connect the design to the budget. The first says what precision a given sample delivers, the second says how much precision clustering destroys, and the third says what sample is required for a stated precision. Together they convert a vague intention to "survey a few hundred people" into a defensible plan.

### 2.11 Conditions under which a design supports a causal claim

A comparison licenses a causal sentence only when five conditions hold at once. They are worth stating separately because an examiner can ask for each by name, and because a design that fails any one of them fails as a whole.

1. **Exchangeability.** The treated and comparison groups must be comparable in the absence of treatment, so that the distribution of every characteristic that affects the response, measured or not, is the same in both. Randomisation establishes this by construction; an observational study must argue it from subject-matter knowledge or from measured covariates, and the argument is always conditional on the covariates being sufficient.
2. **Positivity.** Every unit must have a strictly positive probability of receiving each condition. If some units can only receive the treatment, no comparison exists for them, and the effect estimated for the remaining units does not generalise to the whole.
3. **Consistency.** The treatment received must be the treatment defined, so that "the new programme" means the same thing for every unit and the outcome is well defined under that label. Programmes delivered with variable intensity violate this condition.
4. **No interference.** One unit's outcome must not depend on another unit's treatment assignment. Vaccination and peer-learning programmes frequently violate it, because the control group is partly protected or partly taught by the treated group.
5. **Correct temporal order and outcome measurement.** The treatment must precede the outcome, and the outcome must be measured in the same way in both groups, so that a measurement difference is not mistaken for a treatment effect.

The design hierarchy follows directly from these conditions rather than from convention. A randomised experiment satisfies the first condition by construction and must be checked for the remaining four. A natural experiment or a regression-discontinuity design satisfies the first condition by an argument about the assignment mechanism and is therefore weaker but still usable. An observational comparison with measured confounders satisfies the first condition only under the assumption that nothing important was left unmeasured, which is why its conclusion is stated as an adjusted association rather than as an effect.

## 3. Formal Proofs, Derivations, and Methods

### 3.1 Proof of the non-response bias identity

Let the eligible sample of size $n$ be partitioned into respondents of size $r$ and non-respondents of size $n - r$. Write $w_r = r/n$ and $w_n = 1 - w_r$. By the weighted-mean lemma with two groups,

$$
\bar{y} = w_r \bar{y}_{r} + w_n \bar{y}_{n} .
$$

Subtracting the respondent mean from both sides,

$$
\bar{y} - \bar{y}_{r} = w_r \bar{y}_{r} + w_n \bar{y}_{n} - \left(w_r + w_n\right)\bar{y}_{r} ,
$$

where the second term uses $1 = w_r + w_n$ to rewrite $\bar{y}_{r}$ without changing its value. Collecting terms,

$$
\bar{y} - \bar{y}_{r} = w_n\left(\bar{y}_{n} - \bar{y}_{r}\right).
$$

Multiplying both sides by $-1$ gives the statement of Theorem 2. The proof reveals the exact sense in which the bias is a product: it is zero whenever $w_n = 0$, that is no non-response, and zero whenever $\bar{y}_{n} = \bar{y}_{r}$, that is non-response that is ignorable with respect to the variable studied. Since neither condition can be verified without information about the non-respondents themselves, the practical response is to collect that information on a subsample, which is what a non-response follow-up study does.

### 3.2 Proof of unbiasedness under randomisation

Let $T_i$ indicate that unit $i$ is assigned to treatment, with $P\left(T_i = 1\right) = p$ independently across units. The observed outcome is

$$
y_i^{\text{obs}} = T_i y_i(1) + \left(1 - T_i\right)y_i(0) .
$$

The treated sample mean is a random average whose denominator $n_T$ is itself random. Conditioning first on the set of treated units, the expectation of the treated mean is the average of $y_i(1)$ over that set, so unconditionally

$$
E\left(\bar{y}_{T}\right) = \frac{1}{n}\sum_{i=1}^{n} y_i(1) ,
$$

because each unit enters the treated group with probability $p$ and the sample mean over a randomly chosen subset has expectation equal to the mean over all units. The same argument gives

$$
E\left(\bar{y}_{C}\right) = \frac{1}{n}\sum_{i=1}^{n} y_i(0) .
$$

Subtracting,

$$
E\left(\bar{y}_{T} - \bar{y}_{C}\right) = \frac{1}{n}\sum_{i=1}^{n}\left(y_i(1) - y_i(0)\right) = \bar{\tau} .
$$

Linearity of expectation is the only tool used, and no assumption is made about the distribution of the potential outcomes. That is the strength of the result: randomisation buys unbiasedness without modelling.

The proof also exposes the assumptions that remain. Each unit must have a well-defined outcome under either treatment, which excludes settings where one unit's treatment affects another unit's outcome; the assignment probability must be strictly between zero and one for every unit, which excludes designs where some units can only receive one treatment; and the treatment must be delivered as defined, which excludes designs in which the intended and received treatments diverge.

### 3.3 Derivation of the variance of a randomised comparison

With independent assignment and within-condition variance $\sigma^{2}$,

$$
\text{Var}\left(\bar{y}_{T} - \bar{y}_{C}\right) = \text{Var}\left(\bar{y}_{T}\right) + \text{Var}\left(\bar{y}_{C}\right) = \frac{\sigma^{2}}{n_T} + \frac{\sigma^{2}}{n_C} ,
$$

because the two sample means are computed from disjoint sets of units and are therefore uncorrelated. Setting $n_T = n_C = n/2$ gives

$$
\text{Var} = \frac{2\sigma^{2}}{n} + \frac{2\sigma^{2}}{n} = \frac{4\sigma^{2}}{n} ,
$$

so the standard error is $2\sigma/\sqrt{n}$, which is the corollary of Theorem 4.

Now introduce blocks. Let the response of unit $i$ in block $j$ be

$$
y_{ij} = \mu + \beta_j + \tau T_{ij} + \varepsilon_{ij} ,
$$

where $\beta_j$ is the block effect, $\tau$ the treatment effect, and $\varepsilon_{ij}$ an error with variance $\sigma_{\varepsilon}^{2}$. The total variance of a single observation is then $\sigma^{2} = \sigma_{\beta}^{2} + \sigma_{\varepsilon}^{2}$, and the proportion attributable to blocks is $\rho = \sigma_{\beta}^{2}/\sigma^{2}$.

Inside a block, the block effect is common to both treatments and cancels from the difference, so the difference in a block has variance $2\sigma_{\varepsilon}^{2}$. Averaging over $b$ blocks gives

$$
\text{Var}\left(\hat{\tau}_{\text{blocked}}\right) = \frac{2\sigma_{\varepsilon}^{2}}{b} .
$$

The completely randomised design with the same $2b$ units has variance

$$
\text{Var}\left(\hat{\tau}_{\text{unblocked}}\right) = \frac{4\sigma^{2}}{2b} = \frac{2\sigma^{2}}{b} .
$$

Dividing the second by the first gives the relative efficiency

$$
\frac{\text{Var}\left(\hat{\tau}_{\text{unblocked}}\right)}{\text{Var}\left(\hat{\tau}_{\text{blocked}}\right)} = \frac{\sigma^{2}}{\sigma_{\varepsilon}^{2}} = \frac{1}{1-\rho} ,
$$

which is Theorem 5. The derivation shows the mechanism plainly: blocking removes $\sigma_{\beta}^{2}$ from the error term, and the gain is large exactly when the blocks differ greatly.

### 3.4 Derivation of the omitted-variable bias formula

Regress $y$ on $T$ alone in the model $y = \alpha + \tau T + \beta Z + \varepsilon$, and let $Z = \gamma + \delta T + u$. Substituting the second equation into the first,

$$
y = \alpha + \tau T + \beta\left(\gamma + \delta T + u\right) + \varepsilon = \left(\alpha + \beta\gamma\right) + \left(\tau + \beta\delta\right)T + \left(\beta u + \varepsilon\right).
$$

The coefficient on $T$ in the combined equation is $\tau + \beta\delta$, which is what a regression of $y$ on $T$ alone recovers. The bias is therefore $\beta\delta$: the product of how strongly the confounder moves the response and how strongly the confounder moves with the treatment.

Two corollaries follow immediately. If $\delta = 0$, so that treatment and confounder are unrelated, the bias vanishes; randomisation is a device for forcing $\delta$ to be zero in expectation. If $\beta = 0$, so that the confounder does not affect the response, the bias vanishes as well, which is why a variable that is merely correlated with treatment but causally irrelevant is not a confounder.

### 3.5 Derivation of the attenuation formula

Let $X = T + E$ with $\text{Cov}\left(T, E\right) = 0$, and let $Y$ be measured without error. Then

$$
\text{Cov}\left(X, Y\right) = \text{Cov}\left(T + E, Y\right) = \text{Cov}\left(T, Y\right) ,
$$

since $E$ is uncorrelated with both $T$ and $Y$. The variance of $X$ is $\sigma_{T}^{2} + \sigma_{E}^{2}$. Hence

$$
r_{XY} = \frac{\text{Cov}\left(X, Y\right)}{\sigma_{X}\sigma_{Y}} = \frac{\text{Cov}\left(T, Y\right)}{\sigma_{X}\sigma_{Y}} = \frac{\sigma_{T}}{\sigma_{X}} \cdot \frac{\text{Cov}\left(T, Y\right)}{\sigma_{T}\sigma_{Y}} = \sqrt{\rho_{XX}}\, r_{TY} ,
$$

because $\sigma_{T}/\sigma_{X}$ is the square root of $\sigma_{T}^{2}/\left(\sigma_{T}^{2} + \sigma_{E}^{2}\right)$, which is the square root of the reliability. The algebra confirms that unreliability attenuates rather than distorts: the sign of the correlation is unaffected and only its magnitude shrinks.

### 3.6 Derivation of the Cronbach coefficient

Take $k$ items measuring a single common factor, with item $i$ written as $X_i = \mu_i + \lambda_i F + E_i$, where $F$ is the common factor with variance $\sigma_{F}^{2}$ and the errors are mutually uncorrelated and uncorrelated with $F$. Then

$$
\text{Cov}\left(X_i, X_j\right) = \lambda_i\lambda_j\sigma_{F}^{2} \quad \text{for } i \ne j,
$$

and

$$
\text{Var}\left(\sum_{i=1}^{k} X_i\right) = \sigma_{F}^{2}\left(\sum_{i=1}^{k}\lambda_i\right)^{2} + \sum_{i=1}^{k}\sigma_{E_i}^{2} .
$$

With essentially parallel items, all $\lambda_i$ equal $\lambda$ and all error variances equal $\sigma_{E}^{2}$, so the total variance is $k^{2}\lambda^{2}\sigma_{F}^{2} + k\sigma_{E}^{2}$ and each item variance is $\lambda^{2}\sigma_{F}^{2} + \sigma_{E}^{2}$. Substituting into the coefficient,

$$
\alpha = \frac{k}{k-1}\left(1 - \frac{k\left(\lambda^{2}\sigma_{F}^{2} + \sigma_{E}^{2}\right)}{k^{2}\lambda^{2}\sigma_{F}^{2} + k\sigma_{E}^{2}}\right) = \frac{k^{2}\lambda^{2}\sigma_{F}^{2}}{k^{2}\lambda^{2}\sigma_{F}^{2} + k\sigma_{E}^{2}} ,
$$

which is the ratio of true-score variance to total variance for the sum. The coefficient therefore reproduces the reliability exactly under parallel items, and falls below it when the items differ in their loadings, which is the sense in which $\alpha$ is a lower bound.

### 3.7 Proof of the Horvitz–Thompson lemma

Since $E\left(I_i\right) = \pi_i$ and expectation is linear,

$$
E\left(\hat{Y}_{HT}\right) = E\left(\sum_{i=1}^{N} \frac{I_i y_i}{\pi_i}\right) = \sum_{i=1}^{N} \frac{y_i}{\pi_i}E\left(I_i\right) = \sum_{i=1}^{N} y_i = Y .
$$

The proof requires only that every $\pi_i$ be strictly positive, which is the content of Axiom 1. A unit with $\pi_i = 0$ can never appear in a sample, so its $y_i$ is never counted and no weighting can recover it; this is precisely the situation created by an incomplete frame, and it is why coverage error is not a weighting problem but a design problem.

### 3.8 Derivation of sample size with a finite population correction

Set the margin of error equal to $z$ standard errors and solve for $n$:

$$
e = z\sqrt{\frac{\pi\left(1-\pi\right)}{n}} \quad \Longrightarrow \quad n = \frac{z^{2}\pi\left(1-\pi\right)}{e^{2}} .
$$

When the sample is a substantial fraction of the frame, the standard error carries the factor $\sqrt{1 - n/N}$, so the required sample satisfies

$$
e = z\sqrt{\frac{\pi\left(1-\pi\right)}{n}}\sqrt{1 - \frac{n}{N}} ,
$$

whose solution is the adjusted sample size

$$
n_{\text{adj}} = \frac{n_0}{1 + \dfrac{n_0 - 1}{N}} ,
$$

where $n_0$ is the sample size computed without the correction. The correction always reduces the required sample, and the reduction is negligible when $n_0$ is small relative to $N$, which is why many national surveys ignore it and small institutional surveys should not.

### 3.9 Method: constructing the instrument

Step 1. Translate each research objective into one or more measurable constructs, and write the construct beside each item. An item with no construct is an item to delete.

Step 2. Fix the mode before writing. A self-completed questionnaire must be short, visually simple, and free of items that require an interviewer's explanation; a telephone schedule must avoid long option lists that a respondent cannot hold in memory; a face-to-face schedule may include show cards and longer batteries.

Step 3. Choose the item format. Closed items with exhaustive and mutually exclusive options produce data that are cheap to process and comparable across respondents. Open items produce the categories that a closed item would have missed, at the cost of coding effort and higher item non-response. A workable pattern is to use closed items for measurement and one or two open items for explanation.

Step 4. Draft the wording against five tests: is it short; does it ask one thing; is it free of jargon and abbreviation; is it free of leading and loaded phrasing; and would a person with the least education in the sample understand it in the same way as a person with the most?

Step 5. Fix the order. Begin with easy, salient items; place sensitive items after rapport has been established; group by topic; and avoid placing a general evaluation before the specific judgements that should inform it, because the general answer will anchor the specific ones.

Step 6. Pilot on twenty to forty respondents drawn from the target population, and record completion time, item non-response, and every occasion on which a respondent asked what a question meant. Revise, then pilot again if the revisions are substantial.

Step 7. Plan the field procedure: the number of contact attempts, the timing of reminders, the mode of return, the anonymity statement, and the record kept of ineligible units. These determine the response rate, and the response rate determines the size of the non-response component in Theorem 1.

### 3.10 Method: administering interviews

Step 1. Choose the structure. A **structured interview** uses a fixed schedule read verbatim in a fixed order, so that the encounter is standardised and the answers are comparable; it is the interview analogue of a questionnaire. A **semi-structured interview** uses a topic guide that must be covered but may be reordered, with freedom to probe; it preserves the coverage of the guide while allowing the interviewer to pursue an unexpected answer. An **unstructured interview** has no fixed schedule beyond an opening prompt, and is used to discover the relevant dimensions of a topic rather than to measure them.

Step 2. Train the interviewers on the schedule, on neutral probing, and on recording conventions. Interviewer effects, in which different interviewers obtain systematically different answers, are a measurement error component and are reduced by training and by standardised wording.

Step 3. Record consistently. Verbatim recording preserves the respondent's own words and permits later coding; summary recording is faster and loses the evidence on which coding depends.

Step 4. Allocate effort where it buys precision. When several strata are interviewed at different costs, the allocation that minimises variance for a fixed budget is proportional to $N_h\sigma_h/\sqrt{c_h}$ for stratum $h$, where $N_h$ is the stratum size, $\sigma_h$ its standard deviation, and $c_h$ the cost per interview.

### 3.11 Method: deciding which error dominates

Step 1. Compare the frame with the population. If the frame omits a definable group, coverage error is present and no sample size repairs it.

Step 2. Compute the response rate on the eligible denominator. If it is low, examine whether the non-respondents differ on the study variable, using a follow-up subsample, a proxy measure available for the whole sample, or external benchmarks.

Step 3. Compare the respondent profile with known population margins. A large discrepancy on an auxiliary variable such as age or region is evidence of non-response or coverage bias, and it justifies weighting.

Step 4. Examine the instrument for reliability and for mode effects. A coefficient below about $0.7$ for a multi-item scale, or a large discrepancy between modes, indicates that measurement error is material.

Step 5. Report the decomposition rather than a single number. A statement that the estimate is subject to a sampling error of about three percentage points and an unquantified non-response bias is honest; a statement that the estimate is accurate to three percentage points is not.

## 4. Representative Worked Examples and Solutions

### 4.1 Problem: response rate, non-response bias, and precision in one survey

A survey selects 1 500 households. Of these, 120 prove ineligible because the dwelling is vacant or the address is wrong. Of the remaining, 966 return usable questionnaires. The respondents report a mean of 4.2 visits to a clinic in the past year; a follow-up of a random subsample of the non-respondents yields a mean of 3.1 visits. The proportion reporting that they were satisfied with waiting times is 0.38. Compute the response rate, the non-response bias in the mean, and the 95 per cent margin of error for the proportion.

Step 1. Compute the eligible sample:

$$
n = 1\,500 - 120 = 1\,380 .
$$

Step 2. Compute the response rate:

$$
\frac{966}{1\,380} = 0.70 .
$$

Step 3. Compute the non-respondent share:

$$
w_n = \frac{1\,380 - 966}{1\,380} = \frac{414}{1\,380} = 0.30 .
$$

Step 4. Apply Theorem 2 to obtain the bias in the respondent mean:

$$
\bar{y}_{r} - \bar{y} = w_n\left(\bar{y}_{r} - \bar{y}_{n}\right) = 0.30\left(4.2 - 3.1\right) = 0.33 .
$$

Step 5. Reconstruct the full-sample mean as a check:

$$
\bar{y} = 4.2 - 0.33 = 3.87 .
$$

Step 6. Compute the standard error of the proportion:

$$
\text{SE}\left(p\right) = \sqrt{\frac{0.38\left(0.62\right)}{966}} = \sqrt{0.000244} = 0.0156 .
$$

Step 7. Multiply by the normal multiplier for 95 per cent confidence:

$$
1.96\left(0.0156\right) = 0.0306 .
$$

Step 8. Interpret. The response rate is 70 per cent; the reported mean overstates the full-sample mean by about 0.33 visits, which is roughly a tenth of the mean itself and therefore material; and the sampling margin of about three percentage points is smaller than the likely bias. In this survey, adding respondents would sharpen the sampling error while leaving the bias untouched, so the correct recommendation is a non-response follow-up rather than a larger sample.

### 4.2 Problem: coverage error and standardisation

A city has 15 000 households. A frame built from an electricity billing register covers 12 000 of them. Households on the frame average 4.2 visits to a health centre, and households off the frame average 2.9 visits. Find the coverage bias of the frame mean and explain what standardisation would be needed to compare two districts with different frame coverage.

Step 1. Compute the population mean using the weighted-mean lemma:

$$
\bar{y} = \frac{12\,000\left(4.2\right) + 3\,000\left(2.9\right)}{15\,000} = \frac{50\,400 + 8\,700}{15\,000} = 3.94 .
$$

Step 2. Compute the coverage bias:

$$
B_c = 4.2 - 3.94 = 0.26 .
$$

Step 3. Check with the short formula, weighting the gap by the omitted share:

$$
\frac{3\,000}{15\,000}\left(4.2 - 2.9\right) = 0.2\left(1.3\right) = 0.26 .
$$

Step 4. Interpret the consequence for comparison. If district A is covered by the frame for 80 per cent of its households and district B for 60 per cent, then the observed difference between districts mixes a real difference with a difference in coverage. Both districts must be reported at a common coverage, or both must be weighted to the same household distribution, before the comparison means anything.

### 4.3 Problem: sample size with a finite population correction and non-response inflation

A university wishes to estimate the proportion of its 8 000 students who use a particular service to within three percentage points at 95 per cent confidence, assuming the proportion may be as high as one half. The expected response rate is 62 per cent. How many students must be approached?

Step 1. Compute the sample size without the correction, using the worst case $\pi = 0.5$:

$$
n_0 = \frac{1.96^{2}\left(0.5\right)\left(0.5\right)}{0.03^{2}} = \frac{0.9604}{0.0009} = 1\,067.1 .
$$

Step 2. Round upwards to $n_0 = 1\,068$ respondents.

Step 3. Apply the finite population correction:

$$
n_{\text{adj}} = \frac{1\,068}{1 + \dfrac{1\,067}{8\,000}} = \frac{1\,068}{1.1334} = 942.3 .
$$

Step 4. Round upwards to 943 respondents.

Step 5. Inflate for non-response:

$$
n_{\text{approach}} = \frac{943}{0.62} = 1\,521.0 .
$$

Step 6. Interpret. About 1 521 students must be approached to obtain 943 responses, and the correction for the finite population saved 125 respondents relative to the uncorrected figure. Reporting the uncorrected figure as the plan would over-sample by about 13 per cent and reporting 943 as the number to approach would under-sample by nearly 40 per cent.

### 4.4 Problem: a complete analysis of a randomised experiment

A study assigns 80 volunteers at random, 40 to a new training programme and 40 to the existing programme. The outcome is a test score. The new group has mean 78.2 and standard deviation 8.4; the existing group has mean 74.1 and standard deviation 7.9. Estimate the effect, its standard error, and a 95 per cent confidence interval, and state what the design licenses.

Step 1. Compute the observed difference:

$$
\hat{\tau} = 78.2 - 74.1 = 4.1 .
$$

Step 2. Pool the two variances, weighting by degrees of freedom:

$$
s_p^{2} = \frac{39\left(8.4^{2}\right) + 39\left(7.9^{2}\right)}{78} = \frac{39\left(70.56\right) + 39\left(62.41\right)}{78} = \frac{2\,751.84 + 2\,433.99}{78} = 66.49 .
$$

Step 3. Compute the standard error of the difference:

$$
\text{SE} = \sqrt{66.49\left(\frac{1}{40} + \frac{1}{40}\right)} = \sqrt{3.324} = 1.823 .
$$

Step 4. Compute the test statistic:

$$
t = \frac{4.1}{1.823} = 2.25 .
$$

Step 5. Compare with the critical value for 78 degrees of freedom at the 5 per cent level, which is about $1.99$. Since $2.25 > 1.99$, the difference is statistically significant.

Step 6. Form the confidence interval:

$$
4.1 \pm 1.99\left(1.823\right) = 4.1 \pm 3.63 ,
$$

so the interval is from $0.47$ to $7.73$ score points.

Step 7. Interpret. Because assignment was random, Theorem 3 licenses the causal reading: the programme raised the mean score by about 4.1 points among volunteers of this kind, with a plausible range from about half a point to about eight points. The interval excludes zero, so an effect of no consequence is not consistent with the data, but the lower end of the interval is small enough that a policy decision should weigh the cost of the programme.

### 4.5 Problem: measuring the gain from blocking

Five shops each stock a new product and the old product in successive periods. The differences in units sold, new minus old, are 2, 4, 3, 6, and 5. The variance of sales within a shop across periods is 16 square units. Compute the blocked standard error, the standard error of an unblocked comparison with the same number of units, and the relative efficiency.

Step 1. Compute the mean difference:

$$
\bar{d} = \frac{2 + 4 + 3 + 6 + 5}{5} = 4 .
$$

Step 2. Compute the squared deviations: $4$, $0$, $1$, $4$, $1$, summing to $10$. Hence

$$
s_d^{2} = \frac{10}{4} = 2.5 .
$$

Step 3. Compute the blocked standard error:

$$
\text{SE}_{\text{blocked}} = \sqrt{\frac{2.5}{5}} = 0.707 .
$$

Step 4. Compute the unblocked standard error with five units per condition and within-condition variance 16:

$$
\text{SE}_{\text{unblocked}} = \sqrt{\frac{2\left(16\right)}{5}} = \sqrt{6.4} = 2.53 .
$$

Step 5. Compute the relative efficiency as the ratio of variances:

$$
\frac{6.4}{0.5} = 12.8 .
$$

Step 6. Interpret. The blocked design is nearly thirteen times as efficient, because the shops differ so much that an unblocked comparison would be dominated by shop-to-shop variation. Two conclusions follow: the paired difference of 4 units is estimated far more precisely than the same number of shops could achieve unpaired, and the price paid is that the conclusion applies only to shops used as blocks, so the design must be repeated across a spread of shop types before generalising.

### 4.6 Problem: separating a school effect from a socioeconomic confounder

An observational comparison finds that schools with small classes average 68 points and schools with large classes average 62 points. Small-class schools have a high-socioeconomic share of 0.70, large-class schools 0.40, and each unit of socioeconomic share is associated with 9 additional points. Estimate the causal effect of small classes under the assumption that socioeconomic composition is the only confounder.

Step 1. Record the observed difference and the confounder difference:

$$
D = 68 - 62 = 6, \qquad \Delta = 0.70 - 0.40 = 0.30 .
$$

Step 2. Compute the bias using Theorem 6 with $\beta = 9$ and $\delta = 0.30$:

$$
\beta\delta = 9\left(0.30\right) = 2.7 .
$$

Step 3. Subtract to obtain the adjusted effect:

$$
\tau = 6 - 2.7 = 3.3 .
$$

Step 4. Interpret with care. The adjusted estimate of 3.3 points is conditional on the assumption that socioeconomic composition is the only confounder, an assumption that no observational design can verify. If a second confounder, such as parental involvement, also differs between the groups, the estimate remains biased and its direction is unknown. The honest conclusion is that the association is about half explained by composition, and that a randomised assignment of pupils to class sizes would be required before the remaining 3.3 points could be called an effect.

### 4.7 Problem: reliability, attenuation, and correction

A six-item scale has item variances summing to 18.6 and a total score variance of 48.0. Its correlation with an observed outcome is 0.43, and the outcome itself is measured without error. Compute the coefficient, the attenuation, and the corrected correlation.

Step 1. Apply Theorem 8 with $k = 6$:

$$
\alpha = \frac{6}{5}\left(1 - \frac{18.6}{48.0}\right) = 1.2\left(1 - 0.3875\right) = 1.2\left(0.6125\right) = 0.735 .
$$

Step 2. Compute the square root of the reliability, which is the attenuation factor:

$$
\sqrt{0.735} = 0.857 .
$$

Step 3. Divide the observed correlation by the attenuation factor to recover the true correlation:

$$
r_{TY} = \frac{0.43}{0.857} = 0.50 .
$$

Step 4. Interpret. The scale is about 74 per cent reliable, and the observed correlation of 0.43 understates a true correlation of about 0.50. Reporting the corrected value is defensible only when the reliability is estimated from the same sample and reported alongside the correction, since the correction is unstable when reliability is low.

### 4.8 Problem: the cost of clustering

A survey of 1 200 employees is drawn by selecting 50 workplaces and interviewing 24 employees in each. The intra-class correlation for the study variable is 0.06. Compute the design effect, the effective sample size, and the inflation of the standard error.

Step 1. Apply the design effect formula:

$$
\text{deff} = 1 + \left(24 - 1\right)\left(0.06\right) = 1 + 1.38 = 2.38 .
$$

Step 2. Compute the effective sample size:

$$
n_{\text{eff}} = \frac{1\,200}{2.38} = 504.2 .
$$

Step 3. Compute the inflation of the standard error:

$$
\sqrt{2.38} = 1.543 .
$$

Step 4. Interpret. The clustered sample of 1 200 carries the information of about 504 independent respondents, so the margin of error is about 54 per cent wider than a simple random sample of the same size would give. Reducing the cluster size to 8 employees would lower the design effect to $1 + 7(0.06) = 1.42$ and raise the effective sample to about 845, at the cost of recruiting more workplaces.

### 4.9 Problem: allocating interview effort across strata

A study interviews traders in two market strata. Stratum A has 600 traders with standard deviation 12 and a cost of 40 per interview; stratum B has 400 traders with standard deviation 20 and a cost of 75 per interview. Allocate a total of 200 interviews to minimise the variance of the estimated mean.

Step 1. Compute the allocation index $N_h\sigma_h/\sqrt{c_h}$ for each stratum:

$$
\frac{600\left(12\right)}{\sqrt{40}} = \frac{7\,200}{6.325} = 1\,138.4, \qquad \frac{400\left(20\right)}{\sqrt{75}} = \frac{8\,000}{8.660} = 923.8 .
$$

Step 2. Sum the indices:

$$
1\,138.4 + 923.8 = 2\,062.2 .
$$

Step 3. Allocate in proportion:

$$
n_A = 200\left(\frac{1\,138.4}{2\,062.2}\right) = 110.4, \qquad n_B = 200\left(\frac{923.8}{2\,062.2}\right) = 89.6 .
$$

Step 4. Round to 110 and 90, which sum to the available 200.

Step 5. Interpret. Although stratum B is smaller in population and dearer per interview, it receives nearly half the effort, because its greater variability and lower cost-efficiency trade-off in its favour. A proportional allocation of 120 and 80 would have been easier to justify administratively but would have produced a less precise overall mean.

### 4.10 Problem: estimation under unequal selection probabilities

A population of six firms has values 3, 5, 8, 11, 14, and 19 for a variable of interest. A sample of two firms is drawn without replacement, and the firms with values 8 and 14 are selected. Estimate the population total and the population mean, and compute the standard error of the mean under simple random sampling.

Step 1. Compute the population total and mean for reference: the total is $60$ and the mean is $10$.

Step 2. Apply the Horvitz–Thompson estimator with $\pi_i = 2/6 = 1/3$ for every unit:

$$
\hat{Y}_{HT} = \frac{8}{1/3} + \frac{14}{1/3} = 3\left(8\right) + 3\left(14\right) = 66 .
$$

Step 3. Convert to a mean estimate by dividing by the population size:

$$
\hat{\mu} = \frac{66}{6} = 11 .
$$

Step 4. Compute the population variance of the values about the mean:

$$
S^{2} = \frac{49 + 25 + 4 + 1 + 16 + 81}{5} = \frac{176}{5} = 35.2 .
$$

Step 5. Compute the variance and standard error of the sample mean:

$$
\text{Var}\left(\bar{y}\right) = \left(1 - \frac{2}{6}\right)\frac{35.2}{2} = 11.73, \qquad \text{SE} = \sqrt{11.73} = 3.43 .
$$

Step 6. Interpret. The estimate of 11 exceeds the true mean of 10 by one unit, which is well inside one standard error, so the outcome is unremarkable. The calculation also shows why the finite population correction matters here: without it the variance would be $17.6$ rather than $11.73$, and the standard error would be overstated by about 22 per cent.

## 5. Mathematical Extensions, Limits, and Common Errors

The most consequential error in this topic is the belief that a good collection method is one that produces a large data set. Size governs only the sampling component of Theorem 1, and it governs that component weakly, through the square root. The other three components are properties of the design: a frame that omits a group, a field procedure that loses a distinctive part of the sample, and an instrument that invites a particular answer will each bias the estimate in a direction that more data will not correct. Every serious methodological judgement in this topic therefore reduces to asking which of the four components dominates, and then spending the available budget on the component that does.

### 5.1 Non-probability sampling and the loss of inference

Quota, convenience, purposive, and snowball samples are widely used because they are cheap, and they can support descriptive statements about the respondents themselves. They cannot support design-based inference, because Axiom 1 fails: selection probabilities are unknown, so the Horvitz–Thompson estimator cannot be formed and no design-based standard error exists. Reporting a margin of error for a quota sample as though it were a probability sample is a category error, and the error is common in commercial and journalistic reporting.

### 5.2 Mode effects and social desirability

Different modes produce different answers from the same people. Face-to-face interviews obtain higher reported rates of socially approved behaviour and lower rates of socially disapproved behaviour than self-completed questionnaires; telephone interviews obtain shorter answers than face-to-face interviews; web questionnaires obtain more item non-response on sensitive items but more honest reporting of some behaviours. Because the mode changes the measurement, a trend computed across a change of mode confounds a real change with a change of instrument. Maintaining a consistent mode, or embedding a mode-experiment, is the defence.

In addition to mode effects, three measurement problems recur. **Social desirability** is the tendency to report behaviour that will be approved. **Acquiescence** is the tendency to agree with statements regardless of content, which is why balanced scales that include reverse-worded items are used. **Recall error** is the tendency to misreport the frequency of ordinary events, which is why diaries or short recall windows are preferred to annual recall questions.

### 5.3 The limits of each method

A survey measures what respondents say, which is not the same as what they do, and it is exposed to coverage, non-response, and measurement error simultaneously. An experiment identifies a causal effect for the units and conditions studied, and its external validity is a separate question that the experiment itself cannot answer. An observational study can describe a population and follow change over time, but its causal claims rest on assumptions about unmeasured confounders that no amount of data can test. An interview produces depth and the reasoning behind answers, at the cost of standardisation and of interviewer effects. A questionnaire standardises the stimulus and reaches many respondents cheaply, at the cost of depth and of a dependence on literacy and goodwill.

### 5.4 Common errors and how to avoid them

- **Dividing returns by the issued total rather than the eligible total.** Undelivered instruments are not refusals, and including them understates the response rate.
- **Treating a high response rate as proof of representativeness.** A high response rate from a narrow frame is still biased, and a low response rate from a frame that covers everyone can be corrected by weighting if the non-respondents can be characterised.
- **Calling any structured study an experiment.** Without assignment by the investigator, the design is observational, however standardised the measurement.
- **Reporting a causal verb from an observational comparison.** "Associated with" is the correct verb until the design excludes confounding.
- **Confusing reliability with validity.** A consistent instrument can be consistently wrong; report both properties, and evidence each with the appropriate procedure.
- **Correcting a correlation for attenuation without reporting the reliability.** The correction is a division by a square root, and it is unstable when reliability is low.
- **Ignoring clustering when computing a margin of error.** The design effect multiplies the variance, and a clustered sample of 1 200 can carry the information of 500 independent respondents.
- **Assuming that a larger sample cures bias.** Bias is a property of the design; sample size is a property of the budget.
- **Piloting on colleagues rather than respondents.** The pilot exists to discover what the target population does not understand, so it must use the target population.
- **Writing double-barrelled items.** A respondent who is asked whether a service is fast and reliable can only produce an answer that cannot be attributed to either attribute.

### 5.5 Synthesis

The topic has one architecture. A question fixes a population and a variable; a route is chosen, and the route fixes the strongest conclusion available; a method and an instrument are chosen, and the instrument fixes the scale of the data; the field procedure fixes the response rate; and the four components of Theorem 1 fix the accuracy of the estimate. Randomisation, replication, control, and blocking are the four devices that make an experiment informative, and each maps onto a specific threat. Reliability and validity are the two properties that make an instrument usable, and attenuation is the price paid when reliability is neglected. Every examination question in this topic can be answered by locating the scenario on that architecture and stating which component of error the design controls and which it does not.