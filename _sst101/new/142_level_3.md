## 1. Foundational Concepts, Definitions, and Axioms

### 1.1 What this topic is examined for

Data collection questions test a small number of things very repeatedly. Candidates are asked to name a method and justify the name, to compute a response rate from a muddled field report, to say what a design can and cannot conclude, to criticise a draft questionnaire item, and to choose between the three styles of interview. The mathematics is arithmetic rather than algebraic, so marks are lost through misread denominators, through unexplained symbols, and through unstated conclusions, not through difficult manipulation.

The whole topic hangs on one architecture, and every question is a request to locate a scenario somewhere on it.

1. A question fixes a population and a variable.
2. A route is chosen from the four routes: published source, designed experiment, survey, observational study.
3. A method is chosen from the five methods: survey, experiment, observational study, interview, questionnaire.
4. An instrument is written, piloted, and administered.
5. Responses become records, which support a descriptive summary and, if the design allows, an inference with a stated reliability.

Examiners award marks at each arrow. A script that jumps from the scenario to a conclusion without showing the arrow loses the method marks even when the conclusion is right.

### 1.2 Command words and what they require

- **Define** requires a formal statement with the defining property, not an example.
- **Distinguish** requires a stated criterion of difference and then the difference, ideally in a two-column comparison.
- **Explain why** requires a mechanism, such as the reason randomisation balances unmeasured characteristics.
- **Describe** requires the components in order, without evaluation.
- **Evaluate** or **critically assess** requires both a strength and a limitation, and a judgement.
- **Calculate** requires the formula, the substitution, the value with units, and an interpretation.
- **Recommend** requires a choice justified against the alternatives that were rejected.

### 1.3 The definitions that must be reproduced exactly

> **Definition (Population).** The set of all units, usually people, objects, transactions, or events, that we are interested in studying.

> **Definition (Variable).** A characteristic or property of an individual population unit.

> **Definition (Sample).** A subset of the units of a population.

> **Definition (Statistical inference).** An estimate, prediction, or other generalisation about a population based on information contained in a sample.

> **Definition (Measure of reliability).** A statement, usually associated with a statistical inference, that quantifies the confidence the inference deserves.

> **Definition (Descriptive statistics).** Numerical and graphical methods used to look for patterns in a data set and present that information in a convenient form.

> **Definition (Inferential statistics).** Methods that use sample data to make estimates, decisions, predictions, or other generalisations about a larger set of data.

> **Definition (Survey).** A collection method in which a standardised set of questions is administered to a defined set of respondents in order to describe their characteristics, attitudes, or behaviour.

> **Definition (Experiment).** A collection method in which the investigator deliberately imposes a treatment and controls its assignment, so that the effect of the treatment can be separated from other sources of variation.

> **Definition (Observational study).** A collection method in which the investigator records units as they occur naturally, without imposing a treatment or controlling exposure.

> **Definition (Interview).** A collection method in which a researcher questions a respondent directly, allowing clarification and follow-up.

> **Definition (Questionnaire).** A written instrument of fixed items, completed by the respondent or read out verbatim by an interviewer.

> **Definition (Primary data).** Data collected by the investigator, or under the investigator's direction, for the purpose of the study in hand.

> **Definition (Secondary data).** Data collected by another party for another purpose and subsequently used by the investigator.

> **Definition (Reliability).** The consistency of an instrument's measurements; formally, the proportion of observed variance attributable to true differences between units.

> **Definition (Validity).** The degree to which an instrument measures the construct it is intended to measure.

Each definition contains one idea that the examiner is looking for. For a survey it is "standardised questions administered to a defined set"; for an experiment it is "deliberate imposition with controlled assignment"; for an observational study it is "no imposition"; for reliability it is "consistency"; for validity it is "measures what it claims". A definition that omits the italicised idea scores nothing.

### 1.4 The four routes and the five methods, and why both lists exist

Data can be obtained from a published source, from a designed experiment, from a survey, or observationally. The five named methods are surveys, experiments, observational studies, interviews, and questionnaires. The two lists are consistent once the mapping is stated.

| Route | Corresponding method | Instrument | Strongest conclusion |
| --- | --- | --- | --- |
| Published source | Secondary analysis | Document, register, database | Description of the recorded population |
| Designed experiment | Experiment | Treatment protocol, measurement schedule | Causal effect in the studied setting |
| Survey | Survey | Questionnaire or interview schedule | Prevalence, association, opinion |
| Observational | Observational study | Observation record, routine data | Association and prediction |

Interviews and questionnaires are not separate routes. They are the two instruments by which the survey route is executed, and an examiner who asks for "the five methods" expects both to be named while acknowledging that they belong to the survey family.

### 1.5 The four design principles, stated for the exam

> **Control.** Hold every factor other than the treatment constant, or include a comparison group receiving no treatment or the standard treatment, so that the comparison isolates the treatment.

> **Randomisation.** Assign units to conditions by a random mechanism, so that every characteristic of the units, measured or unmeasured, is balanced across conditions in expectation.

> **Replication.** Apply each treatment to several independent units, so that treatment means are precise and residual variation can be estimated.

> **Blocking.** Group units that are alike in a nuisance characteristic, and randomise within each group, so that between-group variation is removed from the comparison.

The pairing of principle to threat is the standard mark scheme: control against a competing explanation, randomisation against systematic imbalance, replication against random noise, blocking against wasted precision.

### 1.6 The error taxonomy

Total survey error is decomposable into four components, and the decomposition is the organising idea behind almost every evaluation question.

> **Coverage error.** Arises because the frame omits part of the population, so some units have no chance of selection.

> **Sampling error.** Arises because a sample rather than the whole frame is measured; it falls as the sample grows and can be quantified by a standard error.

> **Non-response error.** Arises because selected units do not supply data, and it is large when the non-respondents differ from the respondents.

> **Measurement error.** Arises because the recorded answer differs from the truth, through wording, mode, interviewer behaviour, recall, or social desirability.

In symbols, with the four components named in the same order,

$$
\text{total error} = \text{coverage} + \text{sampling} + \text{non-response} + \text{measurement} .
$$

Only the second component is a function of sample size. The first, third, and fourth are functions of design, which is why "increase the sample" is almost never the correct answer to a question about bias.

### 1.7 Instrument properties and the measurement scale

Reliability is consistency; validity is correctness of purpose. Reliability is necessary and not sufficient for validity. Four kinds of validity are examined: face validity, which is appearance; content validity, which is coverage of the construct domain; criterion validity, which is correlation with an external standard; and construct validity, which is agreement with the theory of the construct.

The scale of the variable is fixed by the item format, and the scale fixes the admissible summaries.

| Scale | Property | Admissible summaries | Example |
| --- | --- | --- | --- |
| Nominal | Categories only | Frequencies, proportions, mode | Preferred transport mode |
| Ordinal | Ordered categories | Median, percentiles, ranks | Satisfaction: poor to excellent |
| Interval | Equal distances, arbitrary zero | Mean, standard deviation, differences | Temperature in degrees Celsius |
| Ratio | Equal distances, true zero | All arithmetic including ratios | Income, mass, waiting time |

### 1.8 Axioms assumed in every answer

> **Axiom 1 (Positive selection probability).** Every unit in the frame has a known probability of selection strictly greater than zero.

> **Axiom 2 (Instrument consistency).** Within a mode, every respondent meets the same instrument administered in the same way.

> **Axiom 3 (Exclusive and exhaustive classification).** Every record belongs to exactly one category of every classification, so frequencies sum to the number of records.

> **Axiom 4 (Error additivity).** The error of an estimate decomposes into the four components above.

Axiom 1 is the one most often violated in practice and most often ignored in scripts. A convenience sample has unknown selection probabilities, so no design-based standard error exists, and a margin of error quoted for such a sample is meaningless.

### 1.9 Instrument formats: the comparison examiners want

| Feature | Open question | Closed question |
| --- | --- | --- |
| Response format | Respondent's own words | Fixed options |
| Best used when | Categories unknown, reasons needed | Categories known, measurement needed |
| Analysis | Coding required, labour intensive | Direct tabulation |
| Respondent burden | Higher | Lower |
| Main risk | Coding subjectivity, item non-response | Missing options, forced choice |

The three interview styles are compared on the same dimensions, with the addition of probing, which is the mechanism that converts an interview from a spoken questionnaire into a qualitative instrument.

| Feature | Structured interview | Semi-structured interview | Unstructured interview |
| --- | --- | --- | --- |
| Schedule | Fixed, read verbatim | Topic guide, reorderable | Opening prompt only |
| Comparability | High | Moderate | Low |
| Depth | Low | Moderate to high | High |
| Probing | Forbidden | Permitted | Central |
| Typical use | Large-scale measurement | Mixed-method studies | Exploratory work |

## 2. Theorems, Lemmas, and Analytical Properties

### 2.1 The response rate

> **Result 1 (Response rate).** For $r$ usable responses from $n$ eligible units,
>
> $$
> \text{response rate} = \frac{r}{n} \times 100\% .
> $$

The eligible denominator excludes undelivered instruments, vacant dwellings, disconnected numbers, deaths, and units found to be outside the population. A returned but blank instrument is not a usable response. Examiners set this deliberately, because most lost marks in this topic come from dividing by the issued total.

### 2.2 The non-response bias identity

> **Result 2 (Non-response bias).** With respondent share $w_r$, non-respondent share $w_n = 1 - w_r$, respondent mean $\bar{y}_{r}$, and non-respondent mean $\bar{y}_{n}$,
>
> $$
> \bar{y}_{r} - \bar{y} = w_n\left(\bar{y}_{r} - \bar{y}_{n}\right).
> $$

The bias is a product of a share and a gap. It follows that a 30 per cent non-response rate with no difference between the groups is harmless, and a 5 per cent non-response rate concentrated among the extremes is not.

### 2.3 The coverage bias identity

> **Result 3 (Coverage bias).** If a fraction $q$ of the population lies outside the frame, and the frame mean exceeds the out-of-frame mean by a gap $g$,
>
> $$
> B_c = q\,g .
> $$

The algebra is identical to Result 2, which is the point: coverage and non-response are the same arithmetic applied to two different kinds of missing unit. The difference is that coverage misses units before selection, so no increase in sample size can ever reach them.

### 2.4 Unbiasedness under randomisation

> **Result 4 (Randomisation).** If units are assigned independently to treatment with probability $p \in \left(0,1\right)$, then
>
> $$
> E\left(\bar{y}_{T} - \bar{y}_{C}\right) = \bar{\tau} ,
> $$
>
> where $\bar{y}_{T}$ and $\bar{y}_{C}$ are the treated and control means and $\bar{\tau}$ is the average individual treatment effect among the units studied.

This result is the only licence for a causal sentence. It says nothing about a single experiment, only about the procedure, so the correct phrasing is that the design is unbiased, not that the estimate is certainly correct.

### 2.5 The variance of a treatment comparison

> **Result 5 (Variance of the difference).** With within-condition variance $\sigma^{2}$ and $n_T$, $n_C$ units in the two conditions,
>
> $$
> \text{Var}\left(\bar{y}_{T} - \bar{y}_{C}\right) = \sigma^{2}\left(\frac{1}{n_T} + \frac{1}{n_C}\right),
> $$
>
> so with equal allocation and total $n$ the standard error is $2\sigma/\sqrt{n}$.

The square root is why precision is expensive. Quadrupling the total number of units halves the standard error, and reducing it by a factor of ten costs a hundredfold increase.

### 2.6 The blocking efficiency

> **Result 6 (Relative efficiency of blocking).** If a proportion $\rho$ of the total variance is attributable to blocks, then blocking reduces the variance of the estimated treatment difference by the factor
>
> $$
> 1 - \rho ,
> $$
>
> and the relative efficiency is $1/\left(1-\rho\right)$.

A script that states "blocking reduces error" scores one mark; a script that states the factor and interprets $\rho$ scores the full allocation.

### 2.7 The omitted-variable bias formula

> **Result 7 (Omitted-variable bias).** For $y = \alpha + \tau T + \beta Z + \varepsilon$ with $Z = \gamma + \delta T + u$, the difference in means estimates
>
> $$
> \tau + \beta\delta .
> $$

The bias is the product of the confounder's effect on the response and its association with the treatment. Setting either factor to zero removes the bias, which is exactly what randomisation does to $\delta$.

### 2.8 Reliability, Cronbach's coefficient, and attenuation

> **Result 8 (Reliability).** For $X = T + E$ with uncorrelated truth and error,
>
> $$
> \rho_{XX} = \frac{\sigma_{T}^{2}}{\sigma_{T}^{2} + \sigma_{E}^{2}} .
> $$

> **Result 9 (Cronbach's coefficient).** For $k$ items,
>
> $$
> \alpha = \frac{k}{k-1}\left(1 - \frac{\sum_{i=1}^{k}\sigma_{i}^{2}}{\sigma_{\text{total}}^{2}}\right).
> $$

> **Result 10 (Attenuation).** An unreliable instrument shrinks every correlation in which it is used:
>
> $$
> r_{\text{obs}} = r_{\text{true}}\sqrt{\rho_{XX}} .
> $$

The square root is the detail that separates a good answer from a vague one. A reliability of $0.81$ shrinks a correlation by a factor of $0.9$, not by $0.81$.

### 2.9 Precision, design effects, and sample size

> **Result 11 (Standard error of a proportion).** With finite population correction,
>
> $$
> \text{SE}\left(p\right) = \sqrt{\frac{p\left(1-p\right)}{n}}\sqrt{1 - \frac{n}{N}} .
> $$

> **Result 12 (Design effect).** For clusters of average size $m$ with intra-class correlation $\rho$,
>
> $$
> \text{deff} = 1 + \left(m-1\right)\rho , \qquad n_{\text{eff}} = \frac{n}{\text{deff}} .
> $$

> **Result 13 (Sample size for a proportion).** For a margin $e$ and multiplier $z$,
>
> $$
> n = \frac{z^{2}\pi\left(1-\pi\right)}{e^{2}} ,
> $$
>
> rounded upwards, evaluated at $\pi = 0.5$ when the proportion is unknown.

> **Result 14 (Finite population correction on sample size).**
>
> $$
> n_{\text{adj}} = \frac{n_0}{1 + \dfrac{n_0 - 1}{N}} .
> $$

The four results form a chain used in almost every long calculation: choose the precision, compute the sample, correct for the finite population, correct for clustering, then inflate for non-response.

### 2.10 The Horvitz–Thompson estimator

> **Result 15 (Horvitz–Thompson).** For selection probabilities $\pi_i$ and selection indicators $I_i$,
>
> $$
> \hat{Y}_{HT} = \sum_{i=1}^{N} \frac{I_i y_i}{\pi_i}, \qquad E\left(\hat{Y}_{HT}\right) = Y .
> $$

Each respondent represents $1/\pi_i$ units, which is the formal basis of survey weights and of every adjustment for differential non-response.

## 3. Formal Proofs, Derivations, and Methods

### 3.1 Pattern 1: name the method and justify it

The question usually supplies a scenario and asks for the method, the route, and a justification. The template has three sentences.

Step 1. Answer the control question. Did the investigator assign the treatment? If yes, the design is an experiment; if no, it is observational or a survey.

Step 2. Answer the elicitation question. Were responses spoken by a respondent to an interviewer, or written by the respondent? The first is an interview, the second a questionnaire. If no questions were asked at all, the instrument is an observation schedule.

Step 3. Answer the provenance question. Who collected the numbers? If another party collected them earlier for another purpose, the data are secondary and the route is the published source.

Step 4. State the consequence. "Because assignment was controlled, the design supports a causal reading" or "because assignment was not controlled, the design supports association only".

The marking points are: method named, route named, the criterion of the decision stated, and the consequence stated. A bare method name earns at most a third of the available marks.

### 3.2 Pattern 2: the response rate and the bias

Every computation in this pattern begins by fixing the denominator, and the derivation shows why.

Step 1. Write the issued total and subtract ineligible units. The eligible denominator is what the response rate divides by.

Step 2. Count usable responses. Blank returns, returns after close of field, and duplicates are excluded, and the exclusions are stated.

Step 3. Compute the rate as $r/n$, and state it as a percentage to one decimal place.

Step 4. Derive the bias. Partition the eligible sample into respondents and non-respondents and take the weighted mean:

$$
\bar{y} = w_r\bar{y}_{r} + w_n\bar{y}_{n} .
$$

Step 5. Subtract the respondent mean and simplify using $w_r + w_n = 1$:

$$
\bar{y} - \bar{y}_{r} = w_n\left(\bar{y}_{n} - \bar{y}_{r}\right).
$$

Step 6. Interpret the sign and the size. A mean that overstates by 0.5 units on a variable whose mean is 6 is an eight per cent distortion and is material; the same 0.5 on a variable whose mean is 500 is negligible.

### 3.3 Pattern 3: can this design support a causal claim?

The expected answer is a decomposition plus an explicit statement of what would be required.

Step 1. Write the observed difference as $D = \bar{y}_{1} - \bar{y}_{0}$.

Step 2. Identify the candidate confounders and, for each, the association with the treatment $\delta$ and the effect on the response $\beta$.

Step 3. Compute the distortion contributed by each confounder as $\beta\delta$, and sum the contributions:

$$
D = \tau + \sum_{j} \beta_j\delta_j .
$$

Step 4. State the identification condition. The design supports a causal claim if the sum is zero: either no confounder is associated with the treatment, as under randomisation, or every confounder's effect is known to be zero.

Step 5. State what would fix it. Random assignment, a natural experiment, matching on measured confounders, or an instrumental variable. Then state the residual limitation of the fix, since measured-confounder adjustment cannot address an unmeasured confounder.

### 3.4 Pattern 4: critique a questionnaire item

Five faults account for almost every item-critique question, and each is repaired by a specific rewrite.

Step 1. Test for **leading wording**. "Do you agree that the improved service is now acceptable?" asserts the conclusion and pushes the respondent towards agreement.

Step 2. Test for **double-barrelling**. "Is the service fast and reliable?" asks two things and produces one answer that cannot be attributed to either.

Step 3. Test for **ambiguity and jargon**. "How often do you utilise the facility?" requires the respondent to interpret both "utilise" and the reference period.

Step 4. Test for **negative construction**. "Do you not think the fee is not unreasonable?" requires a double reversal and produces unreliable answers.

Step 5. Test for **missing or overlapping options**. A frequency item offering "daily, weekly, monthly, often" mixes a time frame with a judgement and leaves the options neither exclusive nor exhaustive.

Step 6. Rewrite, and say what changed. One idea per item, neutral wording, a stated reference period, mutually exclusive and exhaustive options, and a "don't know" where ignorance is a genuine answer.

### 3.5 Pattern 5: choose the interview style

Step 1. Ask whether the study needs comparison across respondents or depth within respondents. Comparison points to structured; depth points to unstructured; a study needing both points to semi-structured.

Step 2. Ask whether the relevant dimensions are known in advance. If a validated schedule exists, structure it; if the topic is unexplored, begin unstructured.

Step 3. State the trade-off explicitly. Depth costs standardisation and comparability; standardisation costs richness and the ability to pursue the unexpected.

Step 4. State the administration consequences. Structured interviews need trained interviewers reading verbatim and are cheap per case; semi-structured interviews need skilled probing and are dearer; unstructured interviews require expert interviewers and transcription, and they cannot be pre-coded.

### 3.6 Pattern 6: reliability, validity, and correlation

Step 1. Compute the reliability from the coefficient or from the variance components, and state which was used.

Step 2. Convert the reliability to the attenuation factor by taking the square root.

Step 3. Divide the observed correlation by the factor to correct for attenuation, or multiply the true correlation by it to predict what will be observed.

Step 4. State the limitation. The correction assumes classical measurement error, uncorrelated with the truth, and it is unstable when reliability is low, so a corrected correlation should always be reported with its uncorrected value and the reliability estimate.

Step 5. Distinguish reliability from validity in the conclusion. A high coefficient establishes consistency and says nothing about whether the construct is the intended one; validity requires an external criterion or a theoretical argument.

### 3.7 The trap table

| Trap | Appearance in the question | Correct handling |
| --- | --- | --- |
| Denominator error | Undelivered instruments mixed with refusals | Subtract ineligibles before dividing |
| Causal verb from observational data | "Show that the programme caused..." | Deny the causal claim, then adjust or redesign |
| Survey called a questionnaire | "Name the method" on a design with sampling and administration | Name the survey and identify the instrument |
| Reliability called validity | Coefficient of 0.9 presented as proof of good measurement | Accept consistency, demand criterion or content evidence |
| Design effect ignored | Clustered sample with a simple random sample formula | Compute deff, then the effective sample size |
| Correction applied to the wrong quantity | Attenuation computed as multiplication by reliability | Take the square root |
| Sample size presented as a cure for bias | "Increase the sample to remove the bias" | Separate variance from bias in the answer |
| Blocking claimed without a nuisance factor | "Blocking was used" with no justification | Name the nuisance factor and the variance share it explains |

## 4. Representative Worked Examples and Solutions

### 4.1 Model solution 1: a survey question (20 marks)

A district health office posts questionnaires to 2 000 households to estimate mean weekly hours of care work and the proportion satisfied with a clinic. Of the 2 000, 150 prove ineligible. Usable questionnaires are returned by 1 240 households, whose mean care hours are 6.4; a follow-up of a random subsample of the non-respondents gives a mean of 4.9 hours. The proportion satisfied is 0.44. Compute the response rate, the non-response bias, and a 95 per cent confidence interval for the proportion, and advise the office.

Step 1. Compute the eligible denominator. *(1 mark: excludes ineligible units from the denominator)*

$$
n = 2\,000 - 150 = 1\,850 .
$$

Step 2. Compute the response rate. *(1 mark: correct quotient; 1 mark: percentage stated)*

$$
\frac{1\,240}{1\,850} = 0.670 .
$$

Step 3. Compute the non-respondent share and gap. *(1 mark: share computed on the eligible denominator; 1 mark: gap identified)*

$$
w_n = \frac{1\,850 - 1\,240}{1\,850} = 0.330, \qquad \bar{y}_{r} - \bar{y}_{n} = 6.4 - 4.9 = 1.5 .
$$

Step 4. Apply the bias identity. *(2 marks: correct product and sign; 1 mark: interpretation as overstatement)*

$$
\bar{y}_{r} - \bar{y} = 0.330\left(1.5\right) = 0.50 .
$$

Step 5. State the implied full-sample mean. *(1 mark: consistent reconstruction)*

$$
\bar{y} = 6.4 - 0.50 = 5.90 .
$$

Step 6. Compute the standard error of the proportion. *(2 marks: correct standard error; 1 mark: finite population correction mentioned or justified as negligible)*

$$
\text{SE}\left(p\right) = \sqrt{\frac{0.44\left(0.56\right)}{1\,240}} = 0.0141 .
$$

Step 7. Form the interval. *(1 mark: multiplier used; 1 mark: interval stated with interpretation)*

$$
0.44 \pm 1.96\left(0.0141\right) = 0.44 \pm 0.028 .
$$

Step 8. Compare the two sources of error and advise. *(2 marks: comparison of sizes; 1 mark: recommendation; 1 mark: recommendation justified by design not by size)*

The sampling margin is about 2.8 percentage points, whereas the non-response bias on the mean is 0.5 hours against a mean of 6.4 hours, roughly eight per cent. The bias is therefore comparable in relative size to the whole sampling interval, and it will not fall if the office simply posts more questionnaires. The advice is to run a properly weighted non-response follow-up, or to convert the survey to a mixed-mode design with telephone reminders, and to report the response rate alongside every estimate. The causal language must be avoided entirely: this is a descriptive survey, so "associated with" is the strongest available verb.

### 4.2 Model solution 2: an experiment question (20 marks)

A college wishes to test whether a weekly quiz improves examination performance. It has four classes of 30 students each, and each class can be split into two groups of 15. The examination scores are known to differ substantially between classes. Design the study, state the analysis, and comment on the strength of the conclusion. Observed within-class differences, quiz minus no quiz, are 4, 6, 5, and 3 marks.

Step 1. Identify the design. *(1 mark: randomised complete block design; 1 mark: classes named as blocks)*

Because classes differ substantially in prior attainment, class is a nuisance factor known in advance, so each class is a block and the treatments are randomised within each block.

Step 2. State the randomisation. *(1 mark: random assignment within block; 1 mark: mechanism described)*

Within each class, 15 students are allocated to the quiz condition by a random draw from 30, and the remainder form the comparison group. Each block therefore admits $\binom{30}{15}$ possible allocations, and the block structure admits $2^{4} = 16$ distinct assignments of the two conditions across blocks.

Step 3. State the controls. *(1 mark: control condition specified; 1 mark: other factors held constant)*

Both groups sit the same examination, are taught by the same teacher, and follow the same syllabus; only the weekly quiz differs. Neither group is told which condition is expected to be superior.

Step 4. State the replication. *(1 mark: within-block replication; 1 mark: link to precision)*

Each condition is applied to 15 students in each of four classes, giving 60 students per condition, so the treatment means are estimated from 60 independent observations each.

Step 5. Compute the block-level differences and their mean. *(1 mark: differences listed; 1 mark: mean computed)*

$$
\bar{d} = \frac{4 + 6 + 5 + 3}{4} = 4.5 .
$$

Step 6. Compute the standard deviation of the differences. *(1 mark: deviations; 1 mark: variance; 1 mark: standard error)*

The deviations are $-0.5$, $1.5$, $0.5$, $-1.5$, whose squares sum to $5.0$, so

$$
s_d^{2} = \frac{5.0}{3} = 1.667, \qquad \text{SE} = \sqrt{\frac{1.667}{4}} = 0.646 .
$$

Step 7. Compute the test statistic and interval. *(1 mark: statistic; 1 mark: degrees of freedom; 1 mark: interval)*

$$
t = \frac{4.5}{0.646} = 6.97, \qquad \text{df} = 3 .
$$

The critical value at the 5 per cent level with three degrees of freedom is about $3.18$, so the difference is significant, and the interval is

$$
4.5 \pm 3.18\left(0.646\right) = 4.5 \pm 2.05 .
$$

Step 8. Interpret and limit. *(1 mark: causal reading justified by randomisation; 1 mark: external validity limitation; 1 mark: precision limitation from four blocks)*

Because assignment was random within blocks, the estimate of 4.5 marks is an unbiased estimate of the average effect for students of this kind, and the interval from 2.45 to 6.55 excludes zero. Three limitations must be stated. Four blocks give only three degrees of freedom, so the interval is wide relative to the sample of 120 students; the result applies to this college's students and syllabus, not to all students; and the quiz effect estimated here is the effect of this quiz design, not of quizzing in general.

### 4.3 Model solution 3: a questionnaire critique (10 marks)

A draft item reads: "How often do you not find that the new online system, which has improved access, is slow and difficult to use when you are busy?" A pilot distributes 30 copies and receives 24 usable returns. Critique the item, rewrite it, and comment on the pilot.

Step 1. Identify the negative construction. *(1 mark)* The phrase "do you not find" forces a reversal, and combined with "slow" it makes the direction of agreement ambiguous.

Step 2. Identify the leading assertion. *(1 mark)* "Which has improved access" states the conclusion before asking for it.

Step 3. Identify the double-barrelling. *(1 mark)* "Slow" and "difficult to use" are two distinct attributes.

Step 4. Identify the ambiguity. *(1 mark)* "Often" has no reference period and no defined scale.

Step 5. Identify the conditional clause. *(1 mark)* "When you are busy" makes the item applicable to an undefined subset of occasions.

Step 6. Rewrite as a closed item with a stated period. *(2 marks: neutral wording; 1 mark: exhaustive and exclusive options)* "In the past four weeks, how often was the online system difficult to use?" with options: never, rarely, sometimes, often, always. A separate item then asks about speed with the same options.

Step 7. Provide an open item where reasons are wanted. *(1 mark)* "What one change would make the online system easier to use?"

Step 8. Comment on the pilot. *(1 mark: response rate computed; 1 mark: conclusion about adequacy)*

$$
\frac{24}{30} = 0.80 .
$$

An 80 per cent pilot response is adequate for detecting ambiguity, but 24 respondents cannot support estimates of item variance, so a second pilot of at least 100 is needed before computing the coefficient. The pilot should also record every occasion on which a respondent asked what an item meant, since those queries are the evidence of ambiguity.

### 4.4 Rapid calculation drills

**Drill 1.** A frame of 9 000 covers a population of 12 000. Frame mean 3.6, out-of-frame mean 2.4. Find the coverage bias.

Step 1. Weight by the shares:

$$
\bar{y} = \frac{9\,000\left(3.6\right) + 3\,000\left(2.4\right)}{12\,000} = 3.30 .
$$

Step 2. Subtract: $3.6 - 3.30 = 0.30$, which equals the short formula $0.25\left(1.2\right) = 0.30$.

**Drill 2.** Required margin 5 percentage points at 95 per cent confidence, unknown proportion, population 2 000.

Step 1. Compute the uncorrected sample:

$$
n_0 = \frac{1.96^{2}\left(0.25\right)}{0.05^{2}} = 384.2 .
$$

Step 2. Round up to 385 and apply the correction:

$$
n_{\text{adj}} = \frac{385}{1 + \dfrac{384}{2\,000}} = 322.99 .
$$

Step 3. Round up to 323 respondents.

**Drill 3.** Five items with variances summing to 14.0, total variance 35.0, true correlation 0.60. Find the coefficient and the observed correlation.

Step 1. Apply the coefficient:

$$
\alpha = \frac{5}{4}\left(1 - \frac{14.0}{35.0}\right) = 1.25\left(0.6\right) = 0.75 .
$$

Step 2. Apply attenuation:

$$
r_{\text{obs}} = 0.60\sqrt{0.75} = 0.60\left(0.866\right) = 0.52 .
$$

**Drill 4.** A clustered sample of 1 500 with clusters of 30 and intra-class correlation 0.04. Find the design effect and the effective sample.

Step 1. Compute the design effect:

$$
\text{deff} = 1 + 29\left(0.04\right) = 2.16 .
$$

Step 2. Divide:

$$
n_{\text{eff}} = \frac{1\,500}{2.16} = 694.4 .
$$

**Drill 5.** Observed difference 8 marks; confounder association with treatment 0.25; confounder effect 12 marks per unit. Find the bias and the adjusted effect.

Step 1. Compute the bias: $12\left(0.25\right) = 3$ marks.

Step 2. Subtract: $8 - 3 = 5$ marks.

**Drill 6.** A population of five firms has values 2, 6, 7, 10, 15. A sample of two gives 6 and 15. Estimate the total and the mean.

Step 1. Compute the selection probability: $\pi_i = 2/5$ for each unit.

Step 2. Apply the estimator:

$$
\hat{Y}_{HT} = \frac{5}{2}\left(6\right) + \frac{5}{2}\left(15\right) = 15 + 37.5 = 52.5 .
$$

Step 3. Divide by the population size: $\hat{\mu} = 52.5/5 = 10.5$. The true total is 40, so this particular sample overstates by 12.5, which is expected because the sample happened to contain the largest unit.

## 5. Mathematical Extensions, Limits, and Common Errors

Marks in this topic are lost in three predictable places, and all three are avoidable by habit. The first is the denominator: candidates divide returns by the issued total, so a response rate is understated and every downstream comment about representativeness is wrong. The second is the conclusion: candidates write "the programme caused an improvement" about an observational study, which forfeits the marks for interpreting the design even when the arithmetic is perfect. The third is the missing interpretation: candidates compute 4.5 marks, 0.30 units, or 0.75 for the coefficient and then stop, when the mark scheme requires a sentence saying what the number means for the study. A disciplined answer always finishes each calculation with a sentence that names the quantity, gives its size in the units of the problem, and states its implication.

### 5.1 Extensions that appear in harder papers

**Design effects and clustering.** The design effect $\text{deff} = 1 + \left(m-1\right)\rho$ converts a nominal sample into an effective sample. A paper that supplies $m$ and $\rho$ expects the candidate to report $n/\text{deff}$ and to say that the margin of error widens by the square root of the design effect.

**Weighting and non-response adjustment.** When the respondent profile differs from known population margins, weights proportional to the reciprocal of the selection-and-response probability restore the margins. The cost is a loss of precision, measured by the variance of the weights, so weighting trades bias for variance and must be justified by the size of the discrepancy it corrects.

**Mode effects.** A change of mode changes the measurement, so a trend computed across a mode change confounds real change with instrument change. The examinable point is that a consistent mode, or an embedded mode experiment, is required before a trend can be interpreted.

**Non-probability sampling.** Quota, convenience, purposive, and snowball samples have unknown selection probabilities, so no design-based standard error exists. They support description of the respondents and hypothesis generation, and they support inference only under modelling assumptions that must be stated.

### 5.2 Limits of the four routes

The published-source route is cheap and cannot be audited beyond its documentation, so its definitions and collection date may not match the question. The designed-experiment route supports causation but may be unethical, expensive, or artificial, so external validity is a separate argument. The survey route measures what respondents say, which is not what they do, and it carries all four error components at once. The observational route is realistic and often the only ethical option, but its causal claims rest on untestable assumptions about unmeasured confounders.

### 5.3 Common errors, with the correction

- **Calling a structured observation an experiment.** Correction: without assignment by the investigator, the design is observational.
- **Treating a survey and a questionnaire as the same thing.** Correction: the survey is the design, the questionnaire is one instrument within it.
- **Reporting a response rate without the eligible denominator.** Correction: state the issued total, the ineligible units, and the eligible total.
- **Assuming non-response is harmless when the rate is low.** Correction: compute the product of share and gap; a small share with a large gap still biases.
- **Assuming a larger sample reduces bias.** Correction: separate sampling variance from coverage, non-response, and measurement bias.
- **Using the reliability rather than its square root in attenuation.** Correction: the attenuation factor is $\sqrt{\rho_{XX}}$.
- **Claiming validity from a high coefficient.** Correction: the coefficient establishes consistency only; validity needs content or criterion evidence.
- **Ignoring the finite population correction in a small institutional survey.** Correction: apply $n_{\text{adj}} = n_0/\left(1 + \left(n_0-1\right)/N\right)$ when the sample is a large fraction of the frame.
- **Forgetting to inflate the sample for non-response.** Correction: divide the required number of respondents by the anticipated response rate.
- **Stating a conclusion without units or direction.** Correction: every computed number gets a sentence naming the quantity, the size, and the implication.

### 5.4 Time strategy in the examination

1. Read the whole paper first and mark every question that mentions data collection, since method questions are quick marks and should not be left to the end.
2. Allocate roughly one minute per mark, and reserve the final ten minutes for checking denominators and interpretations.
3. For a 20-mark design question, spend four minutes planning the headings before writing: design, randomisation, controls, replication, blocking, analysis, interpretation, limitations. Each heading is worth about two marks.
4. For a calculation, write the formula before substituting, because method marks survive an arithmetic slip while a bare number does not.
5. For an evaluation question, write balanced paragraphs with an explicit judgement in the last sentence, since a one-sided answer caps the mark.
6. If time is short, write the formula and the interpretation and omit the arithmetic detail, which recovers most of the marks.

### 5.5 Revision checklist

- State the five definitions of Section 1.3 word for word, then test yourself by covering the page.
- Reproduce the four routes and map each of the five methods onto them.
- Write out the four design principles and the threat each one answers.
- Derive the non-response bias identity from the weighted-mean lemma without looking.
- Derive the omitted-variable bias expression by substitution.
- Compute the attenuation factor from a reliability and correct a correlation both ways.
- Compute a response rate with ineligible units removed, and compute the resulting bias.
- Compute a sample size, apply the finite population correction, then inflate for non-response.
- Compute a design effect and the effective sample size for a clustered design.
- Compute the standard error of a treatment difference and form a confidence interval.
- Explain in three sentences why randomisation licenses a causal claim and why an observational study does not.
- List five faults in a questionnaire item and write a repaired version of each.
- Compare structured, semi-structured, and unstructured interviews on comparability, depth, and cost.
- Recite the difference between reliability and validity, with one example of each failure.
- Practise one full 20-mark design question under timed conditions and mark it against the headings in Section 5.4.

### 5.6 Consolidation

The examination answer for this topic is a short argument with numbers in it. Identify the population, the variable, the route, and the method; state the design principles that are present and the threats they answer; compute the response rate on the eligible denominator and the bias as a share multiplied by a gap; compute precision with the standard error, the design effect, and the finite population correction; state the reliability and the attenuation it implies; and close with the strongest conclusion the design licenses, phrased as association or as cause according to whether assignment was controlled. Every one of those steps is worth marks independently, so a complete answer scores even when one step is imperfect, and an answer that skips the justification to reach a number scores only for the number.
