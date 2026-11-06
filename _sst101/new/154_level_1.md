## 1. Foundational Concepts, Definitions, and Axioms

### 1.1 A notebook that answers questions

Imagine a trader in a busy market who keeps a small exercise book. Every evening she writes down how many tins of cooking oil she sold, how much she paid for a carton of soap, how many customers complained, and how much money was left in the tin. After three months the book holds hundreds of numbers. She cannot carry those numbers in her head, and reading them one by one does not help her decide what to buy next week.

Then she starts asking sharper questions. "On a typical day, how many tins do I sell?" "Have my costs gone up more than my prices?" "Is the new supplier giving me more broken tins than the old one?" Each of these questions is answered not by more numbers but by fewer numbers: one average, one comparison, one rate. That act of turning a heap of observations into a small number of trustworthy statements is what statistics does, and that is why the subject turns up in economics, business, medicine, the social sciences and engineering. The book is the same. Only the questions change.

Statistics is the science of data. It involves collecting, classifying, summarizing, organizing, analyzing, and interpreting numerical information. Notice that the definition has six verbs, and that only two of them, summarizing and analyzing, are about arithmetic. The rest are about discipline: deciding what to count, sorting it honestly, and saying what it means without overreaching.

### 1.2 Two jobs that statistics does

The trader's questions fall into two clearly different kinds, and the difference matters more than any formula in this topic.

> **Definition (Descriptive statistics).** Descriptive statistics uses numerical and graphical methods to look for patterns in a data set and to present that information in a convenient form.

> **Definition (Inferential statistics).** Inferential statistics uses sample data to make estimates, decisions, predictions, or other generalizations about a larger set of data.

Descriptive work stays inside the data. "Last month I sold an average of 46 tins a day" is descriptive: it summarizes what was recorded, and nobody can argue with it provided the arithmetic is right. Inferential work steps outside the data. "Next month I expect to sell about 46 tins a day" is inferential: it makes a claim about days that have not happened yet, and it can be wrong even if the arithmetic was perfect. Inferential claims therefore need something descriptive claims do not need, namely a stated amount of doubt.

A useful shorthand: descriptive statistics describes what you have, and inferential statistics guesses about what you do not have. A hospital that reports "our average waiting time last month was 40 minutes" is describing. The same hospital, after testing a new booking system on 200 patients and concluding that the new system will shorten waiting times for everyone, is inferring.

### 1.3 The five ideas you meet in every study

Every applied study, whether it is a price survey or a drug trial, is built from the same five ideas. Learn them as vocabulary, because later questions are asked in these words.

> **Definition (Population).** A population is a set of units, usually people, objects, transactions, or events, that we are interested in studying.

> **Definition (Variable).** A variable is a characteristic or property of an individual population unit.

> **Definition (Sample).** A sample is a subset of the units of a population.

> **Definition (Statistical inference).** A statistical inference is an estimate, prediction, or some other generalization about a population based on information contained in a sample.

> **Definition (Measure of reliability).** A measure of reliability is a statement, usually attached to a statistical inference, that quantifies confidence in it.

Put them in one sentence and the logic becomes visible: a variable is measured on a sample drawn from a population, an inference is formed about the population, and a measure of reliability says how much the inference deserves to be trusted.

Here is the chain applied to a small clinic. The population is the 600 patients registered at the clinic. The variable is the number of days a patient waits for an appointment. The sample is the 60 patients whose files were opened. The inference is that the average wait for all 600 patients is about nine days. The measure of reliability is the phrase "give or take two days", which says how far the estimate might reasonably sit from the truth.

The last element is the one beginners skip, and it is the one that separates a statistical claim from an advertisement. Without a measure of reliability an inference is an opinion wearing a number.

### 1.4 Kinds of numbers and where they come from

Not every number can be treated the same way, so data are classified first.

> **Definition (Quantitative data).** Quantitative data are measurements recorded on a naturally occurring numerical scale.

> **Definition (Qualitative data).** Qualitative data are measurements that cannot be measured on a natural numerical scale and can only be classified into one of a group of categories.

Height in centimetres, waiting time in days, and the number of tins sold are quantitative. Blood group, sex, and the answer "yes or no" are qualitative. Averaging a qualitative variable is meaningless: the average of the blood groups A and O is not a blood group.

A finer distinction is used when deciding what arithmetic is honest. Nominal data differ only in name, with no order. Ordinal data carry a genuine order but no measurable distance, such as the five points of an opinion scale from strongly disagree to strongly agree. Interval data have equal spacing but an arbitrary zero, like degrees Celsius. Ratio data have equal spacing and a true zero, so ratios are meaningful, like mass or income. The practical consequence is that an index built by adding ordinal scores is a convenience, not a measurement, and should be reported as such.

Data can be obtained from a published source, from a designed experiment, from a survey, or observationally. The route matters, because it determines what may be concluded. A designed experiment, in which the investigator decides who receives which treatment, can support a causal statement. A survey or an observational record generally cannot, because other uncontrolled differences between the groups may be responsible for whatever is seen.

### 1.5 The six-step shape of an applied statistical study

Every serious application, from a price index to a drug trial, follows the same six steps. Recognising the pattern is most of the skill in this topic.

1. State the question in one sentence, naming the population and the variable. "What is the average monthly spend on cooking oil for households in this town?"
2. Decide what will be measured, how it will be measured, and to what accuracy. A spend measured to the nearest shilling is different from one measured to the nearest hundred shillings.
3. Collect the data by a method that does not systematically favour some units over others. Random selection, or random allocation in an experiment, is what makes the eventual inference defensible.
4. Summarise. Compute the descriptive quantities: averages, rates, indexes, tables of counts.
5. Infer, and attach a measure of reliability to the inference. This step converts a summary into a claim, and the claim must carry an interval or a stated confidence.
6. Decide and report. State the decision that the evidence supports, state the uncertainty, and state what the study could not answer.

Steps 1 and 6 are where most real failures occur, not step 4. A study that answers the wrong question with impeccable arithmetic is still a failed study, and a report that hides its uncertainty is not a report but a sales pitch.

### 1.6 The five fields, in one sentence each

The same six steps serve five very different workplaces, and the difference lies in the variable and in the cost of being wrong.

Economics measures aggregates that cannot be observed directly, such as the general price level, and therefore relies on index numbers built from a fixed basket of goods. Business measures its own operations continuously, and therefore relies on rates, forecasts and process control. Medicine measures the effect of an intervention on human beings, and therefore relies on randomised comparison, on diagnostic accuracy, and on survival analysis. A hospital register that records 45 deaths among patients followed for 1200 person-years reports a mortality rate of $45/1200 \times 1000 = 37.5$ deaths per 1000 person-years, and a survival curve reports the proportion still alive at each point in time. The social sciences measure opinions and circumstances that exist only as answers to questions, and therefore rely on survey design, scaling and inference about proportions. Engineering measures the variation of manufactured things, and therefore relies on tolerances, control charts, reliability models, designed experiments and calibration lines.

Each of these is developed in full below, always with a number attached. A field described only in adjectives teaches nothing; a field described by one worked calculation teaches the whole method.

### 1.7 Words you must be able to say out loud

A short glossary prevents most confusion later.

- An **index number** compares the cost of a fixed basket of goods in one period with its cost in a base period, expressing the comparison as a percentage.
- A **price relative** is the price of one item in the current period divided by its price in the base period, usually multiplied by 100.
- A **rate** is a count divided by an amount of exposure, such as defectives per hundred inspected or deaths per thousand person-years.
- A **proportion** is a count divided by a total count, always between zero and one.
- **Sensitivity** is the proportion of genuinely diseased people whom a test correctly calls positive.
- **Specificity** is the proportion of genuinely healthy people whom a test correctly calls negative.
- The **predictive value** of a positive test is the proportion of people who test positive and really do have the condition.
- **Prevalence** is the proportion of a population that has the condition at a given moment.
- A **control chart** is a time plot of a measured quantity with limits that show how much variation is normal.
- A **tolerance interval** is a range that is expected to contain a stated proportion of individual items produced by a process.
- **Reliability** is the probability that an item performs its function for a stated time under stated conditions.

## 2. Theorems, Lemmas, and Analytical Properties

### 2.1 Result 1: a weighted average is the heart of an index

Suppose a basket contains quantities $q_1, q_2, \dots, q_k$ of $k$ items, and the prices in the base period are $p_{0i}$ while the prices now are $p_{1i}$. The cost of the basket in the base period is the sum of price times quantity, and the cost now is the same sum with the new prices.

The comparison of the two costs is called a Laspeyres price index, and it is nothing more than a weighted average of the individual price relatives, where each item is weighted by how much of the household's money it absorbed in the base period.

> **Result (Laspeyres price index).** With base-period quantities held fixed,
> 
> $$
> I_L = \frac{\sum_{i=1}^{k} p_{1i}q_{0i}}{\sum_{i=1}^{k} p_{0i}q_{0i}} \times 100 .
> $$

The index answers a precise question: how much more money would the same shopping list cost today? It does not answer the question "how much worse off is the household", because households change what they buy when prices change.

Two relatives that will be used repeatedly: a price relative is $p_{1i}/p_{0i} \times 100$, and a simple aggregate index is the ratio of summed prices with no quantities at all. The simple aggregate index is a warning example, because it lets an expensive item with a tiny market share dominate the answer.

### 2.2 Result 2: the same idea weighted by current quantities

If the basket is allowed to change, the current quantities $q_{1i}$ replace the base quantities. The resulting index is called a Paasche index.

> **Result (Paasche price index).** With current-period quantities,
> 
> $$
> I_P = \frac{\sum_{i=1}^{k} p_{1i}q_{1i}}{\sum_{i=1}^{k} p_{0i}q_{1i}} \times 100 .
> $$

The Paasche index asks what has happened to the cost of what people buy now. It is harder to compute because the current quantities must be surveyed, and it tends to be lower than the Laspeyres index when households switch away from items whose prices have risen most. Taking the geometric mean of the two gives the Fisher index, which is the compromise used by many statistical offices.

### 2.3 Result 3: a straight line is a forecast

When a quantity such as monthly sales grows by roughly the same amount each month, the trend is captured by a straight line.

> **Result (Least squares line).** The line $y = a + bx$ that minimises the sum of squared vertical distances from the data has slope and intercept
> 
> $$
> b = \frac{S_{xy}}{S_{xx}}, \qquad a = \bar{y} - b\bar{x},
> $$
> 
> where $S_{xy}$ is the corrected sum of products and $S_{xx}$ the corrected sum of squares of the predictor.

The slope is the average change in $y$ per one-unit change in $x$, and the intercept is the fitted value when $x$ equals zero. The line is a description of past co-movement that is then used as a prediction for a future value of $x$, and the prediction inherits all the assumptions used to fit it.

### 2.4 Result 4: a two-by-two table produces four rates

Almost every diagnostic question reduces to a table of counts classified twice: by whether the condition is truly present, and by whether the test said so.

| | Condition present | Condition absent | Total |
|---|---|---|---|
| Test positive | $a$ | $b$ | $a+b$ |
| Test negative | $c$ | $d$ | $c+d$ |
| Total | $a+c$ | $b+d$ | $n$ |

Four quantities follow immediately.

> **Result (Diagnostic rates).** For the four cell counts $a$, $b$, $c$ and $d$ arranged as above,
> 
> $$
> \text{sensitivity} = \frac{a}{a+c}, \qquad \text{specificity} = \frac{d}{b+d},
> $$
> 
> $$
> \text{predictive value positive} = \frac{a}{a+b}, \qquad \text{predictive value negative} = \frac{d}{c+d} .
> $$

Sensitivity and specificity read down the columns, because they are properties of the test given the truth. Predictive values read across the rows, because they answer the patient's question: I have a positive result, so what is the chance I am ill? The asymmetry is the single most examined point in this field.

### 2.5 Result 5: Bayes turns a test property into a patient probability

Bayes' formula connects the two readings.

> **Result (Bayes for a positive test).** If $D$ denotes the presence of the disease and $T^{+}$ a positive test, then
> 
> $$
> P\left(D \mid T^{+}\right) = \frac{P\left(T^{+} \mid D\right)P(D)}{P\left(T^{+} \mid D\right)P(D) + P\left(T^{+} \mid D'\right)P(D')} .
> $$

In words: the chance of disease given a positive test equals the chance of a positive test given disease, multiplied by how common the disease is, divided by the overall chance of a positive test. The formula makes a fact that surprises everyone the first time: when a disease is rare, most positive results are false, even when the test is good.

### 2.6 Result 6: a survey proportion always wobbles

A sample proportion $\hat{p}$ computed from $n$ independent observations has a standard error, and the standard error is the natural unit of wobble.

> **Result (Standard error of a proportion).** For a sample of size $n$ drawn from a population in which the true proportion is $p$,
> 
> $$
> \text{SE}\left(\hat{p}\right) = \sqrt{\frac{p(1-p)}{n}} .
> $$

An approximate $95\%$ interval is the estimate plus and minus about two standard errors, and the width of that interval shrinks in proportion to the square root of the sample size. Four times the sample, half the width.

### 2.7 Result 7: control limits come from the same standard error

A process that is behaving normally still produces varying output. If the mean of a sample of size $n$ is plotted over time, its standard error is the process standard deviation divided by the square root of $n$.

> **Result (Three-sigma control limits).** For a process with mean $\mu$ and standard deviation $\sigma$, monitored with samples of size $n$,
> 
> $$
> \text{UCL} = \mu + \frac{3\sigma}{\sqrt{n}}, \qquad \text{LCL} = \mu - \frac{3\sigma}{\sqrt{n}} .
> $$

A point outside the limits is a signal that something has changed, because such a point would occur by chance only about three times in a thousand. This is the same machinery as a confidence interval, used for a different purpose: an interval estimates an unknown quantity, whereas a control limit classifies a stream of observations as ordinary or unusual.

### 2.8 Result 8: capability compares tolerance with natural spread

A product is acceptable if its measurement lies inside the specification. The natural spread of a stable process is about six standard deviations, so the ratio of the allowed width to the natural width is a single number describing whether the process can meet the specification at all.

> **Result (Capability ratio).** With lower specification limit $L$ and upper specification limit $U$,
> 
> $$
> C_p = \frac{U - L}{6\sigma} .
> $$

A value below one means the ordinary variation of the process is wider than the tolerance, so defective items are inevitable even when the process is centred. A value above one still does not guarantee success, because the process may be off centre, which is why the centred version of the ratio is also computed.

### 2.9 Result 9: reliability is a probability that decays

For many components the chance of surviving one more hour does not depend on how long the component has already survived. Under that assumption the survival function is exponential.

> **Result (Exponential reliability).** With constant failure rate $\lambda$,
> 
> $$
> R(t) = e^{-\lambda t}, \qquad \text{MTTF} = \frac{1}{\lambda} .
> $$

The mean time to failure is the reciprocal of the failure rate, so a component with a mean life of 5000 hours has a failure rate of 0.0002 per hour and a survival probability of about 0.82 at 1000 hours.

### 2.10 What the nine results have in common

Every result above has the same anatomy. A quantity of interest is estimated by a ratio or a weighted average, the variability of that estimator is expressed as a standard error, and a decision rule or an interval is built by adding or subtracting a multiple of that standard error. The index number divides two sums. The regression slope divides a sum of products by a sum of squares. The diagnostic rate divides one cell of a table by a margin. The capability ratio divides a tolerance by six standard deviations. Reliability exponentiates a rate. Once the anatomy is recognised, the five fields stop looking like five subjects and start looking like one subject applied five times.

## 3. Formal Proofs, Derivations, and Methods

### 3.1 Method: run an applied study without fooling yourself

The workflow of an applied statistical study is a sequence of decisions, each with a check that prevents a specific failure.

Step 1. Write the question as a statement about a population parameter, not about a sample. "The average monthly spend of households in this town exceeds 4000 shillings" is checkable; "spending is high" is not.

Step 2. Define the population and the sampling frame, which is the list from which units will actually be drawn. A frame that omits households without electricity quietly redefines the population, and the inference inherits the error.

Step 3. Choose the design. A survey for description, a randomised experiment for causation, a repeated series of measurements for process monitoring.

Step 4. Fix the sample size in advance, using the precision required at step 1. Deciding the sample size after looking at the data is a way of guaranteeing a predetermined answer.

Step 5. Collect, and record the refusals and the missing values as data in their own right. A refusal rate of one in three is a finding, not an inconvenience.

Step 6. Summarise descriptively, then estimate or test, then state the interval and the practical meaning. Report every quantity that the decision needs, including the ones that weaken the story.

Step 7. State the limits. Name the populations to which the conclusion does not extend, and name the confounders that were not measured.

### 3.2 Method: build a price index in four moves

Step 1. Fix the basket, listing a quantity for each item. The quantities must be the same ones used in both periods for a Laspeyres index.

Step 2. For each item compute the base-period expenditure $p_{0i}q_{0i}$ and the current-period expenditure at base quantities $p_{1i}q_{0i}$. Two columns of arithmetic, no shortcuts.

Step 3. Sum each column, and check that the sums are plausible: the base sum should be the household's base budget.

Step 4. Divide the second total by the first and multiply by 100. The result is a percentage, not an amount, and the words "the cost of the basket rose to 118.6 per cent of its base value" are different from "the cost rose by 118.6 per cent".

### 3.3 Method: forecast with a trend line

Step 1. Plot or list the pairs and check that a straight line is a sensible summary. Curvature, seasonal swings and a change in level all invalidate the line.

Step 2. Compute the means of the predictor and the response, and the three sums needed for the corrected sums of squares and products.

Step 3. Compute the slope as the corrected sum of products divided by the corrected sum of squares, then the intercept from the means.

Step 4. Substitute the future value of the predictor to obtain the forecast, and attach a range. A forecast without a range is a guess with decimal places.

Step 5. Ask whether the forecast is being used inside or outside the observed range of the predictor. Outside that range, the line is an extrapolation and its reliability falls away sharply.

### 3.4 Method: fill a two-by-two diagnostic table

Step 1. Decide the definition of a positive test result before seeing the data, and record it in the report.

Step 2. Establish the true status by the best available reference method, not by the test being evaluated.

Step 3. Cross-classify every subject into one of the four cells, and confirm that the cell counts add to the total in both directions.

Step 4. Compute sensitivity and specificity first, because they are properties of the test. Then compute the predictive values, which depend on the sample's prevalence.

Step 5. State the prevalence at which the predictive values hold. A predictive value quoted without its prevalence is uninterpretable.

### 3.5 Method: estimate a proportion from a survey

Step 1. Count the successes and the total, and compute the proportion.

Step 2. Compute the standard error as the square root of the product of the proportion and its complement divided by the sample size.

Step 3. Multiply the standard error by the appropriate normal multiplier, about two for 95 per cent confidence.

Step 4. Report the interval in the units of the question, in percentage points, and state the sample size and the design.

Step 5. Check that the interval is not absurd. An interval that runs outside the range from zero to one is a sign that the sample is too small for the normal approximation, and an exact method should be used instead.

### 3.6 Method: set control limits and read a chart

Step 1. Establish the process mean and standard deviation from a period known to be stable, and never from the period being judged.

Step 2. Choose the subgroup size, which is the number of items measured at each time point.

Step 3. Compute the standard error of the subgroup mean, which is the process standard deviation divided by the square root of the subgroup size.

Step 4. Place limits three standard errors either side of the mean.

Step 5. Plot the subgroup means in time order and apply the rules: one point outside a limit, or a run of seven points on one side of the centre line, or a steady drift, all indicate that the process has changed.

Step 6. Investigate the cause before adjusting anything. A chart is a diagnostic tool, and adjusting a process that is merely noisy makes it worse.

### 3.7 Method: check whether a process can meet a tolerance

Step 1. State the lower and upper specification limits, which come from the design and not from the process.

Step 2. Estimate the process standard deviation from a stable period.

Step 3. Compute the natural spread as six standard deviations, and compare it with the allowed width.

Step 4. Compute the capability ratio and, if the process is off centre, compute the ratio using the nearer limit.

Step 5. Convert to an expected defect rate by finding how many standard deviations separate the process mean from each limit, and reading the normal tail.

Step 6. Decide whether to widen the tolerance, centre the process, or reduce the variation. Only the last of these is a genuine improvement.

### 3.8 Where each field's method comes from

The methods above are not five separate inventions. The index number and the capability ratio are both ratios of sums. The standard error of a proportion and the standard error of a subgroup mean are both standard deviations divided by the square root of a count. The regression slope and the standardised deviation $z$ are both differences divided by a spread. The exponential reliability function is the solution of the statement "the chance of failing in the next instant does not depend on age".

That unity is the real content of this closing topic. A student who can see that a control limit and a confidence interval are the same construction with different intentions has understood the subject; a student who has memorised five lists of applications has not.

## 4. Representative Worked Examples and Solutions

### 4.1 Problem: the cost of a small shopping list

A household buys 10 loaves of bread and 5 litres of milk each week. Last year bread cost 40 shillings a loaf and milk cost 60 shillings a litre. This year bread costs 50 shillings and milk costs 66 shillings. Compute a price index for the household's basket, and say what it means.

### 4.2 Solution: cost the same basket twice

Step 1. Cost the basket at last year's prices:

$$
10 \times 40 + 5 \times 60 = 400 + 300 = 700 .
$$

Step 2. Cost the same basket at this year's prices:

$$
10 \times 50 + 5 \times 66 = 500 + 330 = 830 .
$$

Step 3. Form the ratio and multiply by 100:

$$
I = \frac{830}{700} \times 100 = 118.57 .
$$

Step 4. Interpret. The same weekly shopping now costs 118.57 per cent of last year's cost, so the household needs about 18.6 per cent more money to buy exactly the same goods. If the household's income rose by 12 per cent, its real income index is $112/118.57 \times 100 = 94.5$, so it can buy about 5.5 per cent less than before despite the raise.

Step 5. State the limit. The index assumes the household still buys 10 loaves and 5 litres. If it switched to a cheaper brand, the true rise in its cost of living would be smaller than 18.6 per cent.

### 4.3 Problem: how many defective bulbs

A shopkeeper inspects a sample of 200 bulbs from a new supplier and finds 8 that do not light. The supplier's contract allows at most 3 per cent defective. What is the sample defect rate, and what should the shopkeeper conclude?

### 4.4 Solution: a rate, then a comparison with the contract

Step 1. Compute the rate as a proportion:

$$
\hat{p} = \frac{8}{200} = 0.04 .
$$

Step 2. Express it as a percentage:

$$
0.04 \times 100 = 4\% .
$$

Step 3. Compute the standard error of the rate:

$$
\text{SE} = \sqrt{\frac{0.04 \times 0.96}{200}} = \sqrt{0.000192} \approx 0.01386 .
$$

Step 4. Build an approximate 95 per cent interval:

$$
0.04 \pm 2(0.01386) \quad \text{gives} \quad 0.0123 \text{ to } 0.0677 .
$$

Step 5. Conclude in plain words. The sample rate is 4 per cent, above the 3 per cent allowed, but the interval runs from about 1.2 per cent to 6.8 per cent, so the sample is too small to prove a breach. The honest statement is that the supplier is probably near or above the limit, and a larger sample is needed before rejecting a consignment.

### 4.5 Problem: reading a diagnostic test

In a clinic, 100 people are tested. Twenty of them truly have the disease, and the test is positive for 18 of those 20. Of the 80 people without the disease, the test is positive for 10. Compute the sensitivity, the specificity, the predictive value of a positive result, and the predictive value of a negative result.

### 4.6 Solution: fill the table, then read it in both directions

Step 1. Fill the four cells.

| | Disease present | Disease absent | Total |
|---|---|---|---|
| Test positive | 18 | 10 | 28 |
| Test negative | 2 | 70 | 72 |
| Total | 20 | 80 | 100 |

Step 2. Compute sensitivity, reading down the first column:

$$
\frac{18}{20} = 0.90 \quad \text{so } 90\% .
$$

Step 3. Compute specificity, reading down the second column:

$$
\frac{70}{80} = 0.875 \quad \text{so } 87.5\% .
$$

Step 4. Compute the predictive value of a positive result, reading across the first row:

$$
\frac{18}{28} = 0.643 \quad \text{so } 64.3\% .
$$

Step 5. Compute the predictive value of a negative result, reading across the second row:

$$
\frac{70}{72} = 0.972 \quad \text{so } 97.2\% .
$$

Step 6. Interpret. The test finds 90 out of every 100 ill people and clears 87.5 out of every 100 healthy people. But of 28 people told they tested positive, only about 18 really are ill, so a positive result is far from a diagnosis. The negative result is much more informative, because the disease is uncommon in this clinic.

### 4.7 Problem: how sure is a survey percentage

In a survey of 100 randomly chosen residents, 60 say they support a new market levy. Estimate the support in the whole town and give an approximate 95 per cent margin of error.

### 4.8 Solution: a proportion and its wobble

Step 1. Compute the sample proportion:

$$
\hat{p} = \frac{60}{100} = 0.60 .
$$

Step 2. Compute the standard error:

$$
\text{SE} = \sqrt{\frac{0.60 \times 0.40}{100}} = \sqrt{0.0024} \approx 0.049 .
$$

Step 3. Multiply by two for an approximate 95 per cent margin:

$$
2 \times 0.049 = 0.098 \quad \text{about } 10 \text{ percentage points} .
$$

Step 4. State the interval in words: support is probably between 50 per cent and 70 per cent. Because the interval includes 50 per cent, the survey cannot establish that a majority supports the levy.

Step 5. Note what would improve it. To halve the margin to five points, the sample must be about four times as large, that is around 400 residents, because the margin falls with the square root of the sample size.

### 4.9 Problem: a machine that fills packets

A machine fills packets with a mean of 500 grams and a standard deviation of 4 grams. Each hour, four packets are weighed and their mean is plotted. Compute three-sigma control limits for that hourly mean.

### 4.10 Solution: standard error of a mean, then three of them

Step 1. Compute the standard error of a mean of four packets:

$$
\text{SE} = \frac{4}{\sqrt{4}} = 2 \text{ grams} .
$$

Step 2. Multiply by three:

$$
3 \times 2 = 6 \text{ grams} .
$$

Step 3. Form the limits:

$$
\text{UCL} = 500 + 6 = 506, \qquad \text{LCL} = 500 - 6 = 494 .
$$

Step 4. Interpret. An hourly mean outside 494 to 506 grams would occur by chance only about three times in a thousand if the machine were unchanged, so such a point justifies stopping the line and looking for a cause. A mean of 503 grams is entirely ordinary and must not trigger an adjustment.

Step 5. Note the design point. The limits describe the behaviour of the hourly mean, not of individual packets. Individual packets vary by about 4 grams, but their average varies by only 2, which is why averaging is the basis of process monitoring.

### 4.11 Problem: is the tolerance achievable

A bolt must have a diameter between 19.5 and 20.5 millimetres. A stable process produces bolts with a standard deviation of 0.25 millimetres. Compute the capability ratio and state the conclusion.

### 4.12 Solution: compare allowed width with natural width

Step 1. Compute the allowed width:

$$
20.5 - 19.5 = 1.0 \text{ mm} .
$$

Step 2. Compute the natural width, six standard deviations:

$$
6 \times 0.25 = 1.5 \text{ mm} .
$$

Step 3. Form the ratio:

$$
C_p = \frac{1.0}{1.5} = 0.667 .
$$

Step 4. Interpret. The natural spread is half as wide again as the tolerance, so even a perfectly centred process will make defective bolts. Since the ratio is below one, the process cannot meet the specification as it stands.

Step 5. State the options. Reduce the variation, widen the tolerance, or accept a known defect rate and inspect. Statistics identifies the size of the problem; engineering chooses which remedy is affordable.

## 5. Mathematical Extensions, Limits, and Common Errors

### 5.1 Beginner misconceptions, one by one

The following mistakes appear in almost every first attempt at this topic, and each has a specific cure.

- **"Statistics is just averages."** An average is one summary among many, and it can be the most misleading one. A single extreme observation moves the mean arbitrarily far, so a mean reported without a measure of spread is an incomplete description.
- **"A big sample is always a good sample."** Size buys precision, not accuracy. A huge sample drawn only from people who own telephones estimates the telephone-owning population with great precision and the general population hardly at all.
- **"Ninety per cent accurate means ninety per cent of positive results are right."** This is the single most common misreading of a diagnostic test. Accuracy is a property of the test; the predictive value is a property of the test and the population, and in a rare disease most positives are false.
- **"Correlation proves cause."** Two quantities can move together because a third drives both. Ice-cream sales and drowning deaths rise together, and the cause is hot weather.
- **"A p-value below 0.05 proves the effect is important."** It proves the effect is unlikely to be zero. With a large sample, a trivial effect becomes statistically significant, and with a small sample a large effect may not.
- **"An index of 118.6 means prices rose by 118.6 per cent."** It means prices rose to 118.6 per cent of the base, that is by 18.6 per cent. Confusing the index with the percentage change doubles the answer.
- **"Forecasting is predicting the future."** A forecast is a statement of what the model implies if nothing changes in the relationship. It is conditional, not prophetic.
- **"If the sample had 60 per cent, the population has 60 per cent."** The sample proportion is an estimate with a standard error. Reporting it without the interval is the most common omission in student answers.
- **"Control limits are specification limits."** Control limits describe how the process currently behaves; specification limits describe what the customer will accept. Overlaying one on the other is a category mistake.
- **"A process within control limits is producing acceptable items."** A process can be perfectly stable and still be centred outside its tolerance. Stability and capability are different questions.
- **"Missing data can be ignored."** Units that fail to answer often differ systematically from those that do, so ignoring them biases the estimate rather than merely reducing the sample.
- **"More decimal places means more precision."** Precision is limited by the design, not by the arithmetic. Reporting a survey proportion as 61.372 per cent from 100 respondents claims accuracy that does not exist.

### 5.2 What statistics cannot do

Statistics cannot supply a question. It can tell you that the average spend is 4200 shillings with a margin of 200; it cannot tell you whether that is good news, because "good" requires a standard of value that data do not contain. This is worth stating plainly, because students often expect the arithmetic to deliver the decision.

Statistics also cannot remove the effect of a bad design. If the sample excluded an important subgroup, no amount of arithmetic restores them; if the treatment was assigned to whoever arrived first, no model reliably separates the treatment from the reasons for arriving first. The technical name for the second failure is confounding, and the remedy is in the design, not in the analysis.

Statistics cannot establish causation from observational data alone without additional assumptions, and those assumptions must be argued rather than computed. And statistics cannot convert a biased measurement into an unbiased one: if respondents systematically understate their income, a large sample measures the understatement precisely.

### 5.3 The cost of a statistical error, field by field

The cost of the same blunder is different in each field, and knowing the cost is part of knowing why each field uses the methods it does.

In economics, a wrong index number propagates into wage settlements, pensions and interest rates, so a bias of a few points is multiplied across an entire population and is also hard to reverse once contracts have been signed. In business, a forecast that is too optimistic ties up cash in unsold stock, while one that is too pessimistic loses sales, so the cost is asymmetric and inventory is the buffer that hides it until it is large. In medicine, a false negative in a screening programme delays treatment for a person who does have the disease, and a false positive produces anxiety and unnecessary procedures, so the two errors have unequal weight and a reporting standard that treats them as symmetric is inadequate. In the social sciences, a mismeasured survey shapes public policy for a group that never appears in the sample, and the damage is invisible because the excluded group does not complain. In engineering, a tolerance chosen without regard to process variation produces either scrap or field failures, and a field failure in a safety component is not an economic loss but a hazard.

### 5.4 Ethics and reporting

Because the cost falls on people who did not commission the study, the reporting obligations are ethical obligations and not merely stylistic.

- Report the design before the result, so that a reader can judge whether the data could answer the question at all.
- Report the sample size, the sampling method, and the number of non-responses, because these determine what the interval means.
- Report the interval, not only the point estimate, and state the confidence level.
- Report every outcome that was measured for the stated purpose, including those that showed nothing, because selective reporting is the mechanism by which a literature becomes false.
- Report the multiplicity. If twenty comparisons were made, say so, and adjust the standard accordingly.
- Do not describe a person or a group in terms that the data cannot support. A difference between group means is a statement about distributions, not a licence to describe individuals.
- Keep the data such that another analyst could reproduce the table, and state the software and the version where a computation is not elementary.
- Declare who paid for the study. The reader needs to know whose interest the conclusion might serve.

### 5.5 Confounding, selection and fishing, in everyday terms

Three failures account for most published claims that later collapse.

Confounding means that a third quantity moves with both the supposed cause and the supposed effect, so the observed association is real but misattributed. Suppose a hospital's patients on a new treatment survive at 66 per cent while those on the old treatment survive at 50 per cent. If the new treatment was given mostly to mild cases, the comparison measures severity, not treatment. Splitting the data by severity can reverse the conclusion entirely, which is why a randomised allocation is worth its cost.

Selection bias means the units observed are not a fair sample of the units of interest. A phone-in poll measures the opinions of people who telephone, and a factory that tests only the products that survive shipping measures the robust ones.

Fishing, or p-hacking, means running many analyses and reporting the one that looks impressive. If twenty independent hypotheses are tested at the 5 per cent level and nothing is really happening, the chance of at least one apparently significant result is about 64 per cent, because the chance of none is $0.95^{20} \approx 0.358$. The remedy is to state the hypothesis before the analysis, to report all analyses performed, and to divide the significance level by the number of tests when many are unavoidable.

### 5.6 Statistical significance is not practical significance

An effect can be real and simultaneously too small to matter. Suppose a new checkout layout reduces the average transaction time by 1.2 seconds, and a study with 50 000 transactions finds a $p$-value of 0.001. The effect is unlikely to be zero, so it is statistically significant, and it is also irrelevant to any customer, because 1.2 seconds is below the threshold of perception. The reverse also occurs: a large effect measured on twenty subjects may fail to reach significance and still be the most important finding in the report.

The discipline that prevents both errors is to state, before collecting data, the smallest effect that would change the decision, and to design the study so that the interval would distinguish that effect from zero. This is what "practical significance" means in practice, and it is a decision about consequences rather than a calculation.

### 5.7 A final checklist for any application

1. Name the population, the variable, the sample, the inference and the measure of reliability, and check that the five fit together coherently.
2. Say whether each step is descriptive or inferential, and never attach a causal verb to a descriptive result.
3. For an index, state the basket and the weighting; for a rate, state the denominator and the exposure; for a forecast, state the range and the assumption.
4. For a diagnostic table, read sensitivity and specificity down the columns and predictive values across the rows, and quote the prevalence.
5. For a survey proportion, quote the interval and the sample size, and check the interval against the range from zero to one.
6. For a control chart, distinguish control limits from specification limits, and distinguish stability from capability.
7. For any claim about cause, identify the design that would justify it, and if the design was observational, say what confounder could produce the same pattern.
8. State one thing the study could not answer. Every honest study has at least one.
