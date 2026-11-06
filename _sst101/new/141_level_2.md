## 1. Foundational Concepts, Definitions, and Axioms

### 1.1 Why the classification of data comes before every calculation

Statistics is the science of data, and its first act is never arithmetic but classification. Collecting, classifying, summarizing, organizing, analyzing, and interpreting numerical information are listed in that order for a reason: the class into which an observation falls decides which of the later operations are meaningful and which are nonsense dressed in algebra. A mean of examination marks is informative; a mean of eye colours is not, even though both can be computed from symbols that look identical. The difference is not one of arithmetic but of the structure that the numbers are permitted to carry.

This unit therefore builds a vocabulary of data types, and then a stricter vocabulary of measurement scales. The first distinguishes what kind of thing has been recorded, a category or a quantity. The second distinguishes how much structure the recorded value carries: whether it supports only a statement of sameness, or also a statement of order, or also a statement of equal spacing, or also a statement of ratio. Every legitimate summary, every legitimate graph, and every legitimate coding scheme is licensed by that second classification.

The practical importance is immediate. Two analysts who disagree about whether a satisfaction score is ordinal or interval will disagree about whether reporting a mean score is honest, and the disagreement cannot be settled by computing more carefully. It is settled by asking which transformations of the recorded values leave the information intact. That question is the organising principle of this entire note.

### 1.2 Variables, observations, and data sets

> **Definition (Variable).** A variable is a characteristic or property of an individual population unit.

> **Definition (Observation).** An observation is the value that a variable assumes for one particular unit.

> **Definition (Data set).** A data set is the collection of observations on one or more variables, recorded for a set of units.

Three terms then follow without further assumption. A population is the set of all units about which a question is asked; a sample is a subset of those units; and a data set is the record produced by measuring the units that were actually reached. A single variable measured on a sample yields a univariate data set. Two variables measured on the same units yield a bivariate data set, and it is the bivariate case that makes cross-classification possible.

The distinction between a variable and its recorded values is easy to blur and expensive to blur. The variable is the characteristic; the observation is one realisation of it. Statements about scales are statements about variables, not about the particular numbers that happen to appear in one data set. A variable whose observations all happen to be whole numbers is not thereby discrete, and a variable recorded to two decimal places is not thereby continuous.

### 1.3 The qualitative and quantitative dichotomy

> **Definition (Quantitative data).** Quantitative data are measurements that are recorded on a naturally occurring numerical scale.

> **Definition (Qualitative data).** Qualitative data are measurements that cannot be measured on a natural numerical scale; they can only be classified into one of a group of categories.

The definition turns on the phrase *naturally occurring numerical scale*. A number that arises because a unit was counted, or because a quantity was compared with a standard unit, lies on such a scale. A number that arises because a clerk typed a code beside a category does not. Category codes are labels written in digits, and the fact that they can be added is an accident of notation rather than a property of the category.

Qualitative data are also called categorical data, and the two words are interchangeable. Each observation places its unit into one of a set of categories, and the only primitive relation between two observations is whether they fall in the same category or in different ones. Quantitative data support two further primitive relations: one observation may exceed another, and the excess may be compared with the excess between a third pair.

The dichotomy is exclusive and exhaustive at this level of description. Every variable that can be recorded is either a category or a quantity, provided that the recording instrument has been described honestly.

### 1.4 The nominal scale

> **Definition (Nominal scale).** A variable is measured on a nominal scale when its values are labels that identify categories and nothing more, so that the only admissible comparison between two values is equality or inequality.

Blood group, marital status, region of residence, payment method, and species of tree are nominal. The categories may be listed in any order, and a table of counts may be sorted by frequency or alphabetically without any loss of meaning. Nominal data admit counting: the number of units in each category is a legitimate summary, and the proportion of units in each category is a legitimate summary of relative size. Nominal data do not admit ordering, so no category is high or low, and they do not admit arithmetic, so the sum of two category names has no referent.

Nominal variables are frequently recorded with numerical codes, and this is where most of the mischief begins. Coding card as 1, cash as 2, and mobile as 3 produces a column of integers that a spreadsheet will happily average. The average is a real number, but it is a number about the coding scheme and not about the customers.

### 1.5 The ordinal scale

> **Definition (Ordinal scale).** A variable is measured on an ordinal scale when its values are categories that stand in a known order, so that any two values can be compared as lower, equal, or higher, while the magnitudes of the differences between neighbouring categories are not defined.

Satisfaction ratings, examination grades, military ranks, stages of a disease, and clothing sizes are ordinal. Ordinal data admit everything nominal data admit, and in addition they admit ranking: the median category, the quartile categories, and order-based comparisons of two groups are all legitimate. What ordinal data do not admit is the assumption that the step from category one to category two equals the step from category two to category three. That assumption is an extra, empirical claim about the measuring instrument, and the scale itself supplies no evidence for it.

The absence of equal spacing is not a technicality. A respondent who moves from "dissatisfied" to "neutral" may travel much further in felt experience than a respondent who moves from "neutral" to "satisfied", because the labels are words and the words are not spaced like the rulings of a ruler. Reporting a mean of ordinal codes asserts that the spacings are equal, and the assertion is unsupported.

### 1.6 The interval scale

> **Definition (Interval scale).** A variable is measured on an interval scale when its values lie on a numerical axis with equal spacing between consecutive units, so that differences are comparable, while the zero point is chosen by convention rather than fixed by the nature of the quantity.

Temperature in degrees Celsius is the standard example, and the reason is visible in the arithmetic. The difference between ten degrees and twenty degrees equals the difference between twenty degrees and thirty degrees, so intervals can be added and subtracted and compared. But zero degrees is the freezing point of water, not the absence of temperature, so a temperature of twenty degrees is not twice as warm as ten degrees in any physical sense. Calendar years behave in the same way: the interval from 1990 to 2000 is a decade, but the year 2000 is not twice the year 1000.

Interval data admit the arithmetic mean, the standard deviation, correlation, and every summary built from differences. They do not admit ratios, so they do not admit the coefficient of variation, the geometric mean, or a statement such as "twice as hot".

### 1.7 The ratio scale

> **Definition (Ratio scale).** A variable is measured on a ratio scale when its values lie on a numerical axis with equal spacing and possess a true zero, so that the ratio of two values is meaningful.

Mass, length, duration, income, age, and the number of children in a family are ratio measurements. A mass of twenty kilograms is twice a mass of ten kilograms, and the doubling is a physical fact rather than a convention, because zero kilograms means no mass at all. Ratio data admit every summary that interval data admit, and in addition they admit multiplicative comparisons: coefficients of variation, geometric means, growth rates, and elasticities.

The distinction between interval and ratio is not academic decoration. Every statement of the form "twice as much" or "fifty per cent larger" requires a true zero. A report that one day was twice as hot as another is meaningless on the Celsius scale and meaningful on the Kelvin scale, and only because the Kelvin scale has a true zero.

### 1.8 Discrete and continuous quantitative variables

> **Definition (Discrete variable).** A quantitative variable is discrete when its possible values are separated, so that between two adjacent possible values no other possible value lies. Such variables arise from counting.

> **Definition (Continuous variable).** A quantitative variable is continuous when, between any two of its possible values, a further possible value lies. Such variables arise from measurement.

The number of children in a family is discrete because the values are the whole numbers and nothing lies between two and three. The mass of a student is continuous because a mass of fifty-two kilograms and a mass of fifty-three kilograms are separated by a continuum of possible masses. The operational test is the halfway test: compute the value halfway between two observed values and ask whether that value is possible for the variable. If it is impossible, the variable is discrete; if it is possible, the variable is continuous.

Discreteness has a second, deeper consequence that students often miss. When a variable is discrete, a table that lists each distinct value with its frequency loses no information at all, because the omitted values are impossible rather than merely unobserved. When a variable is continuous, such a table cannot be written, because no two observations can be guaranteed to coincide. Continuous data must be grouped into classes, and grouping is always a lossy operation.

### 1.9 Recording precision is not the same as scale

A continuous variable recorded to a fixed precision produces observations that look discrete. Age is continuous, yet a survey records age in completed years; mass is continuous, yet a hospital scale reports to the nearest kilogram. The recording has quantised the value, but the variable has not changed. The distinction matters because the halfway test is applied to the variable, not to the printed digits.

The correct formulation is that recording at precision $h$ replaces a true value $x$ by a reported value $x^{*}$ in a cell of width $h$ centred on $x^{*}$. The reported value is a class mark, and the class boundaries are $x^{*} - \frac{h}{2}$ and $x^{*} + \frac{h}{2}$. This is precisely why the grouped frequency table for masses reported to the nearest kilogram carries boundaries at half-kilogram positions. The grouping is not an arbitrary presentational choice; it is the structure that the recording precision imposes.

### 1.10 Cross-classification of two variables

> **Definition (Contingency table).** A contingency table cross-classifies a sample by two variables, placing the categories of one variable in the rows and the categories of the other in the columns, and recording in each cell the number of units that fall into that combination of categories.

A contingency table is the natural summary when both variables are qualitative, and it remains the natural summary when a quantitative variable has been grouped into categories for the purpose of the cross-tabulation. Each cell count is called a joint frequency; the totals at the foot and at the right margin are called marginal frequencies; and a distribution formed by fixing one category and reading across a row or down a column is called a conditional distribution.

The table licenses three distinct readings, and confusing them is the commonest error in this part of the subject. The joint distribution reports how many units fall in each combination. The marginal distribution reports how many fall in each category of one variable, ignoring the other. A conditional distribution reports the composition of one row or column, and therefore answers a question of the form "among the loyal customers, what fraction pay by card?" A rhetorical claim about a group is almost always a claim about a conditional distribution, while a headline count is almost always a joint or marginal frequency.

### 1.11 Notation

Let $x_i$, for $i = 1, 2, \dots, n$, denote the $i$-th observation of a quantitative variable $X$. The mean is written $\bar{x}$, the variance of a population $s^{2}$, and its standard deviation $s$. Frequencies are written $f_1, \dots, f_k$, so that the total number of observations is $n = \sum_{i=1}^{k} f_i$.

$$
\sum_{i=1}^{k} f_i = n
$$

For a grouped table, classes carry a lower boundary $L_j$ and an upper boundary $U_j$, a width $h_j = U_j - L_j$, and a class mark $m_j = \frac{L_j + U_j}{2}$. For a contingency table with $r$ rows and $c$ columns, the cell count is $O_{ij}$, the row total is $R_i$, the column total is $C_j$, and the grand total is $n$.

## 2. Theorems, Lemmas, and Analytical Properties

### 2.1 The principle that governs every admissible summary

The following principle is the organising theorem of the whole topic. It converts a vague instruction to "use the right average" into a test that can be applied mechanically.

> **Definition (Admissible transformation).** An admissible transformation of a scale is a relabelling of the recorded values that preserves every distinction the scale is able to express.

> **Principle (Admissibility).** A summary statistic is admissible for a scale if and only if it is equivariant under every admissible transformation of that scale, that is, if and only if applying the transformation to the data applies the same transformation to the summary.

The principle has a plain reading. If a change of labels that destroys no information nevertheless changes the summary, then the summary was reading the labels rather than the information. Under that reading, a statistic is a legitimate summary exactly when it survives every recoding that the scale treats as irrelevant.

### 2.2 The admissible transformations of the four scales

> **Theorem (Admissible transformation classes).** The admissible transformations are as follows: for a nominal scale, every one-to-one relabelling of the categories; for an ordinal scale, every strictly increasing transformation of the categories; for an interval scale, every transformation of the form $y = a + bx$ with $b > 0$; for a ratio scale, every transformation of the form $y = bx$ with $b > 0$.

The nesting is exact: the ratio class is contained in the interval class, which is contained in the ordinal class, which is contained in the nominal class. A statistic that survives a wide class of transformations survives every narrower class as well, which is why a mode, legitimate on a nominal scale, remains legitimate on all three stronger scales.

| Scale | Admissible transformations | Distinctions the scale can express |
|---|---|---|
| Nominal | Any one-to-one relabelling | Same or different |
| Ordinal | Any strictly increasing relabelling | Same, different, and ordered |
| Interval | Any $y = a + bx$, $b > 0$ | Order and equal differences |
| Ratio | Any $y = bx$, $b > 0$ | Order, differences, and ratios |

### 2.3 The mode is admissible on every scale

> **Theorem (Invariance of the mode).** Let $g$ be any one-to-one transformation of the recorded values. If $m$ is a mode of the data, then $g(m)$ is a mode of the transformed data.

The reason is that a one-to-one transformation cannot merge two distinct values or split one value into two, so the frequencies attached to the values are simply carried across to their images. The most frequent value remains the most frequent value.

The theorem is the formal licence for the only average that nominal data possess. A mode is a statement about which category is commonest, and that statement is exactly as informative after relabelling as before.

### 2.4 The median is admissible on ordinal and stronger scales

> **Theorem (Equivariance of the median).** Let $g$ be strictly increasing. Then the median of the transformed data equals $g$ applied to the median of the original data.

Because a strictly increasing transformation preserves the order of the observations, it preserves which observation occupies the middle position. The median is therefore read from the same unit before and after the transformation, and the summary moves with the record rather than with the labels. This is the formal licence for reporting a median category on an ordinal scale.

A qualification belongs with the theorem. When $n$ is even, the usual median is the arithmetic average of the two central observations, and averaging is an operation that requires equal spacing. For genuinely ordinal data the median should therefore be reported as the pair of central categories, or as the interval between them, rather than as their numerical average.

### 2.5 The mean requires an interval or ratio scale

> **Theorem (Affine equivariance of the mean).** For constants $a$ and $b$ with $b > 0$, if $y_i = a + b x_i$ for every $i$, then $\bar{y} = a + b\bar{x}$.

> **Theorem (Failure under monotone recoding).** There exists a strictly increasing transformation $g$ and a data set for which the mean of the transformed data differs from the transformation of the mean.

The second theorem is what disqualifies the mean on an ordinal scale. Order is preserved by every increasing transformation, so if the mean were admissible on an ordinal scale it would have to be equivariant under all of them. It is not. Section 3 supplies an explicit counterexample, which is enough to settle the question.

The first theorem explains why the mean is perfectly at home on an interval scale. A change of origin and unit is precisely a change of thermometer, and the mean responds to it in the only sensible way: it moves with the data.

### 2.6 Variance and standard deviation under change of scale

> **Theorem (Scaling of the variance).** If $y_i = a + b x_i$ for every $i$, then $s_y^{2} = b^{2} s_x^{2}$ and $s_y = \left| b \right| s_x$.

The variance is unaffected by the change of origin because it is built from deviations, and deviations are unchanged by a shift. It is multiplied by the square of the unit conversion because each deviation is multiplied by $b$. The standard deviation therefore behaves like a length, which is exactly what it is.

This theorem is the formal statement that the standard deviation is admissible on an interval scale: it transforms by a positive constant, so a statement such as "the standard deviations of the two groups are equal" is preserved by any change of units.

### 2.7 The coefficient of variation requires a ratio scale

> **Theorem (Invariance of the coefficient of variation under similarity).** Let $v = \frac{s}{\bar{x}}$ for positive data. If $y_i = b x_i$ with $b > 0$, then $v_y = v_x$. If instead $y_i = a + b x_i$ with $a \ne 0$, then in general $v_y \ne v_x$.

The first part shows that $v$ is a legitimate summary on a ratio scale: it is unchanged when the unit of measurement is changed, so it is genuinely unit-free. The second part shows that $v$ is illegitimate on an interval scale: it changes when the origin is moved, and the origin of an interval scale is arbitrary. Section 3 gives the algebra and a numerical illustration.

### 2.8 A dispersion measure for nominal data

> **Definition (Index of qualitative variation).** For $k$ categories with frequencies $f_1, \dots, f_k$ summing to $n$, the index of qualitative variation is

$$
\mathrm{IQV} = \frac{k\left(n^{2} - \sum_{i=1}^{k} f_i^{2}\right)}{n^{2}\left(k - 1\right)}
$$

> **Theorem (Range of the index).** The index satisfies $0 \le \mathrm{IQV} \le 1$, with equality at zero exactly when all observations fall in one category and equality at one exactly when the categories are equally frequent.

The index is admissible on a nominal scale because it is computed from the category frequencies and is therefore unchanged by any relabelling of the categories. It is the only kind of dispersion that nominal data can support, and it answers a question that nominal data can ask: how evenly is the sample spread across the available categories?

### 2.9 Independence in a contingency table

> **Definition (Statistical independence).** Two qualitative variables cross-classified in a contingency table are independent when the conditional distribution of one variable is the same in every category of the other.

> **Theorem (Expected counts under independence).** If the two variables are independent, the expected count in cell $(i,j)$ is

$$
E_{ij} = \frac{R_i C_j}{n}
$$

The theorem converts a statement about distributions into a number for each cell, and the number is the benchmark against which the observed count is judged. A cell whose observed count greatly exceeds its expected count signals an association between the two categories.

### 2.10 The class mark as a weighted mean of the class

> **Theorem (Class mark identity).** For a class with boundaries $L$ and $U$, the class mark $m = \frac{L+U}{2}$ satisfies $U - m = m - L$, so the mark is equidistant from both boundaries.

The identity is trivial and consequential. Because every observation in the class lies within half a class width of the mark, replacing each observation by the mark introduces an error of at most $\frac{h}{2}$ in any single value, and the grouped mean inherits that bound in the sense that the grouped and exact means differ by no more than $\frac{h}{2}$.

## 3. Formal Proofs, Derivations, and Methods

### 3.1 Proof of affine equivariance of the mean

Let $y_i = a + b x_i$ for $i = 1, \dots, n$. Then by linearity of summation,

$$
\bar{y} = \frac{1}{n}\sum_{i=1}^{n}\left(a + b x_i\right) = \frac{1}{n}\left(na + b\sum_{i=1}^{n} x_i\right)
$$

and since $\sum_{i=1}^{n} x_i = n\bar{x}$,

$$
\bar{y} = a + b\bar{x}
$$

The mean therefore commutes with every change of origin and unit, which is the technical content of the claim that the mean is a legitimate average on an interval scale.

### 3.2 Proof that the mean fails on an ordinal scale

Take the three observations $1$, $2$, $3$ and the strictly increasing transformation $g(x) = x^{2}$. The mean of the original data is

$$
\bar{x} = \frac{1 + 2 + 3}{3} = 2
$$

and $g\left(\bar{x}\right) = 4$. The transformed data are $1$, $4$, $9$, whose mean is

$$
\bar{y} = \frac{1 + 4 + 9}{3} = \frac{14}{3} \approx 4.67
$$

Since $4.67 \ne 4$, the mean is not equivariant under this increasing recoding. The transformation $g$ preserves the order of the three observations, so an ordinal scale regards it as an admissible relabelling; the mean changes anyway, so the mean is not licensed by an ordinal scale. The proof is complete, and a single counterexample suffices because admissibility was required for every admissible transformation.

### 3.3 Proof of median equivariance

Let $x_{(1)} \le x_{(2)} \le \cdots \le x_{(n)}$ be the ordered observations, and let $g$ be strictly increasing. Then $g\left(x_{(1)}\right) \le g\left(x_{(2)}\right) \le \cdots \le g\left(x_{(n)}\right)$, so the ordered transformed data are obtained by applying $g$ to each order statistic in place. If $n = 2k+1$ the median is $x_{(k+1)}$ and the median of the transformed data is $g\left(x_{(k+1)}\right)$ by inspection. If $n = 2k$ the median is conventionally the average of $x_{(k)}$ and $x_{(k+1)}$, and the average does not commute with $g$, which is why the median of ordinal data is reported as the central pair rather than as their average.

### 3.4 Derivation of the variance scaling law

With $y_i = a + b x_i$ the deviations satisfy

$$
y_i - \bar{y} = \left(a + b x_i\right) - \left(a + b\bar{x}\right) = b\left(x_i - \bar{x}\right)
$$

so squaring and averaging over the $n$ observations gives

$$
s_y^{2} = \frac{1}{n}\sum_{i=1}^{n} b^{2}\left(x_i - \bar{x}\right)^{2} = b^{2} s_x^{2}
$$

Taking square roots and recalling that a standard deviation cannot be negative gives $s_y = \left| b \right| s_x$. The origin $a$ has vanished entirely, which is the algebraic statement that the variance knows nothing about where the scale was zeroed.

### 3.5 Proof that the coefficient of variation is not interval-admissible

Write $v_x = \frac{s_x}{\bar{x}}$ and apply the transformation $y = a + b x$ with $b > 0$. Using the two theorems just proved,

$$
v_y = \frac{s_y}{\bar{y}} = \frac{b s_x}{a + b\bar{x}}
$$

If $a = 0$ this reduces to $v_y = \frac{b s_x}{b\bar{x}} = v_x$, so the index is invariant under a change of unit alone. If $a \ne 0$ the expression does not reduce, and putting in numbers makes the failure concrete: a sample with mean $20$ and standard deviation $2$ has $v_x = 0.1$, while the same data expressed as $y = x + 273$ have mean $293$, standard deviation $2$, and $v_y = 0.0068$. The two coefficients describe the same data and differ by a factor of fifteen.

### 3.6 Derivation of the index of qualitative variation and its bounds

The sum $\sum f_i^{2}$ is largest when the observations are concentrated, because concentrating a fixed total into one category maximises the sum of squares. It equals $n^{2}$ when all observations fall in one category and equals $\frac{n^{2}}{k}$ when the observations are spread equally. The quantity $n^{2} - \sum f_i^{2}$ therefore measures how far the distribution is from total concentration, and dividing by its maximum value $n^{2} - \frac{n^{2}}{k} = \frac{n^{2}(k-1)}{k}$ rescales the measure to the unit interval. Multiplying by $k$ and dividing by $n^{2}(k-1)$ is exactly that rescaling, which establishes both the formula and the bounds.

### 3.7 Derivation of expected counts under independence

Let $p_{ij}$ be the probability that a randomly chosen unit falls in cell $(i,j)$, let $p_{i\cdot}$ be the marginal probability of row $i$, and let $p_{\cdot j}$ be the marginal probability of column $j$. Independence is the statement $p_{ij} = p_{i\cdot} p_{\cdot j}$ for every pair $(i,j)$. Multiplying by $n$ gives the expected count

$$
E_{ij} = n p_{ij} = n p_{i\cdot} p_{\cdot j} = \frac{\left(n p_{i\cdot}\right)\left(n p_{\cdot j}\right)}{n} = \frac{R_i C_j}{n}
$$

The derivation shows that the expected count is forced once independence is assumed; it is not an arbitrary convention.

### 3.8 Method: from recorded values to class boundaries

Step 1. Establish the recording precision $h$. A mass reported to the nearest kilogram has $h = 1$; a mark reported to the nearest whole number has $h = 1$; a time reported to the nearest second has $h = 1$.

Step 2. Place a boundary at each reported value plus and minus $\frac{h}{2}$. Reported values $50, 51, 52, \dots$ therefore acquire boundaries $49.5, 50.5, 51.5, \dots$.

Step 3. Choose a class width that is a convenient multiple of $h$, and place class boundaries on the boundary grid rather than on the reported values.

Step 4. Record the class limits as the reported values that lie inside each pair of boundaries, since limits are a notational convenience for the reader while boundaries carry the mathematics.

### 3.9 Method: standardising as an affine recoding

For a quantitative variable with mean $\bar{x}$ and standard deviation $s$, the standard score of an observation is

$$
z_i = \frac{x_i - \bar{x}}{s}
$$

The transformation is affine with $a = -\frac{\bar{x}}{s}$ and $b = \frac{1}{s}$, so it is admissible on an interval scale, and the standard scores are unchanged by any prior change of origin or unit. Two laboratories that measure the same quantity in different units will report identical standard scores, which is precisely why standardisation is the routine preliminary to comparing measurements made on different instruments.

### 3.10 Method: choosing a summary and a display from the scale

Step 1. Decide whether the variable is categorical or quantitative. If categorical, no arithmetic beyond counting is available.

Step 2. If categorical, decide whether the order is meaningful. If it is not, the admissible summaries are frequencies, proportions, the mode, and the index of qualitative variation. If it is, add the median and the quartile categories.

Step 3. If quantitative, decide whether a true zero exists. If it does not, the admissible summaries are the mean, the standard deviation, and the standard score, but not the coefficient of variation or the geometric mean. If it does, all of them are available.

Step 4. Choose the display that matches the structure: a bar chart for categories, a histogram for grouped measurements, an ogive for cumulative frequencies, a scatter diagram for two measurements, and a contingency table or clustered bar chart for two categorical variables.

## 4. Representative Worked Examples and Solutions

### 4.1 Problem: classify eight variables by scale

A clinic records eight variables for each patient: blood group; severity of pain graded mild, moderate, or severe; body temperature in degrees Celsius; number of previous admissions; waiting time in minutes; mode of arrival coded 1 for walk-in, 2 for ambulance, 3 for referral; distance travelled in kilometres; and year of birth. Classify each variable and name the averages that are legitimate for it.

### 4.2 Solution: apply the transformation test to each variable

Step 1. Blood group. The values are labels with no order, so the scale is nominal. The admissible average is the mode, together with the frequency and proportion in each group.

Step 2. Severity of pain. The three grades are ordered, but the step from mild to moderate need not equal the step from moderate to severe, so the scale is ordinal. The admissible average is the median grade, reported as a category, together with the modal grade.

Step 3. Body temperature in degrees Celsius. Differences are meaningful and the zero is conventional, so the scale is interval. The mean and the standard deviation are admissible; a statement that one patient is twice as hot as another is not.

Step 4. Number of previous admissions. The values are counts, so the variable is discrete on a ratio scale. The mean, the standard deviation, and the coefficient of variation are all admissible.

Step 5. Waiting time in minutes. Time is measured, so the variable is continuous on a ratio scale. The mean and standard deviation are admissible, and so is the geometric mean, which is often preferable for a right-skewed waiting-time distribution.

Step 6. Mode of arrival. The codes 1, 2, and 3 are labels, so the scale is nominal despite the digits. Only the mode and the category frequencies are admissible, and averaging the codes to obtain $2$ would describe the coding scheme rather than the patients.

Step 7. Distance travelled in kilometres. Distance has a true zero, so the scale is ratio and continuous. Every summary in Step 5 applies.

Step 8. Year of birth. A calendar year has equal spacing but a conventional zero, so the scale is interval. Differences of years are meaningful; the mean year of birth is a legitimate summary of a cohort, but the ratio of two years is not.

Step 9. Summarise the classification in a table.

| Variable | Scale | Legitimate average |
|---|---|---|
| Blood group | Nominal | Mode |
| Pain severity | Ordinal | Median category |
| Temperature in Celsius | Interval | Mean |
| Previous admissions | Discrete ratio | Mean |
| Waiting time | Continuous ratio | Mean or geometric mean |
| Mode of arrival code | Nominal | Mode |
| Distance travelled | Continuous ratio | Mean or geometric mean |
| Year of birth | Interval | Mean |

Step 10. Interpret. Two of the eight variables look numerical and are not: the arrival code and the year of birth, one nominal and one interval. The example shows that the presence of digits is no evidence of a numerical scale, and the absence of a true zero is no obstacle to computing a mean.

### 4.3 Problem: build and analyse a contingency table

A supermarket surveys $120$ customers, recording payment method and customer category. The results are that $8$ new customers pay by card, $22$ returning customers pay by card, and $26$ loyal customers pay by card; that $14$ new, $12$ returning, and $6$ loyal customers pay cash; and that $6$ new, $14$ returning, and $12$ loyal customers pay by mobile. Construct the contingency table, compute the conditional distribution of payment method within each customer category, and compute the expected count for new customers paying by card under independence.

### 4.4 Solution: marginals, conditionals, and expected counts

Step 1. Enter the joint frequencies and form the margins.

| Payment method | New | Returning | Loyal | Total |
|---|---|---|---|---|
| Card | 8 | 22 | 26 | 56 |
| Cash | 14 | 12 | 6 | 32 |
| Mobile | 6 | 14 | 12 | 32 |
| Total | 28 | 48 | 44 | 120 |

Step 2. Check the margins against the body of the table. The row totals sum to $56 + 32 + 32 = 120$ and the column totals sum to $28 + 48 + 44 = 120$, so no observation has been lost.

Step 3. Compute the conditional distribution of payment method among new customers by dividing each cell in that column by the column total:

$$
\frac{8}{28} \approx 0.286, \qquad \frac{14}{28} = 0.500, \qquad \frac{6}{28} \approx 0.214
$$

Step 4. Compute the same conditional distribution among loyal customers:

$$
\frac{26}{44} \approx 0.591, \qquad \frac{6}{44} \approx 0.136, \qquad \frac{12}{44} \approx 0.273
$$

Step 5. Compare. Card use rises from about $28.6$ per cent among new customers to about $59.1$ per cent among loyal customers, while cash use falls from $50.0$ per cent to about $13.6$ per cent. Because both variables are nominal, these proportions are the correct form of comparison; a mean payment method would be meaningless.

Step 6. Compute the expected count for new customers paying by card under independence using the theorem of Section 2.9:

$$
E_{11} = \frac{R_1 C_1}{n} = \frac{56 \times 28}{120} \approx 13.07
$$

Step 7. Interpret. Only $8$ new customers paid by card where independence would predict about $13$, so card payment is under-represented among new customers. The comparison of observed and expected counts is the entry point to the chi-square test of independence studied later in the course, and it is licensed here only because both variables are categorical.

### 4.5 Problem: summarise ordinal ratings without abusing them

Fifteen respondents rate a service on a five-point scale from $1$ for very poor to $5$ for very good. The frequencies are $2$ respondents at $1$, $3$ at $2$, $5$ at $3$, $4$ at $4$, and $1$ at $5$. Find the median and modal rating, compute the mean of the codes, and show what happens to that mean under an equally defensible recoding.

### 4.6 Solution: order statistics, then a demonstration of the coding artefact

Step 1. Accumulate the frequencies to locate the median position. With $n = 15$ the median is the eighth ordered observation. The cumulative frequencies are $2$, $5$, $10$, $14$, and $15$, so the eighth observation falls in the third category.

Step 2. State the median. The median rating is category $3$, the neutral category, and it is reported as a category rather than as a number.

Step 3. Identify the mode. The largest frequency is $5$, attached to rating $3$, so the modal rating is also category $3$.

Step 4. Compute the mean of the conventional codes:

$$
\bar{x} = \frac{2(1) + 3(2) + 5(3) + 4(4) + 1(5)}{15} = \frac{44}{15} \approx 2.93
$$

Step 5. Recode the categories by $0, 1, 2, 4, 8$, a strictly increasing assignment that respects the order but expresses a belief that the top category is far above the fourth. The mean becomes

$$
\bar{x}' = \frac{2(0) + 3(1) + 5(2) + 4(4) + 1(8)}{15} = \frac{37}{15} \approx 2.47
$$

Step 6. Compare the two answers. Both recodings are admissible on an ordinal scale, because both are strictly increasing, yet the mean moved from about $2.93$ to about $2.47$ while the median and mode did not move at all. The mean is therefore not a property of the ratings but a property of the chosen codes.

Step 7. Compute a legitimate measure of dispersion, the index of qualitative variation, with $k = 5$, $n = 15$, and $\sum f_i^{2} = 4 + 9 + 25 + 16 + 1 = 55$:

$$
\mathrm{IQV} = \frac{5\left(225 - 55\right)}{225 \times 4} = \frac{850}{900} \approx 0.944
$$

Step 8. Interpret. The index is close to one, so the ratings are spread almost evenly across the five categories, which is consistent with the flat profile of the frequency table. Reporting the mean of $2.93$ would have concealed both the flatness and the arbitrariness.

### 4.7 Problem: means on an interval scale, and the ratio that fails

Two days have temperatures of $20$ degrees Celsius and $26$ degrees Celsius. Compute their mean, convert the observations to degrees Fahrenheit, compute the mean there, and test whether the statement that the second day was twice as warm as the first survives the conversion.

### 4.8 Solution: affine equivariance and its limits

Step 1. Compute the mean in degrees Celsius:

$$
\bar{x} = \frac{20 + 26}{2} = 23
$$

Step 2. Convert each observation using $F = 1.8C + 32$, giving

$$
1.8(20) + 32 = 68, \qquad 1.8(26) + 32 = 78.8
$$

Step 3. Compute the mean in degrees Fahrenheit and compare with the affine transform of the Celsius mean:

$$
\frac{68 + 78.8}{2} = 73.4, \qquad 1.8(23) + 32 = 73.4
$$

The two agree, which is the mean's affine equivariance in action and confirms that a mean temperature is a legitimate summary.

Step 4. Test the ratio on the Celsius scale:

$$
\frac{26}{20} = 1.3
$$

Step 5. Test the same ratio on the Fahrenheit scale:

$$
\frac{78.8}{68} \approx 1.159
$$

Step 6. Interpret. The same two days are $30$ per cent warmer in one scale and about $16$ per cent warmer in the other, so the ratio is not a property of the weather. The Celsius scale is interval, and ratios of interval measurements are not invariant under admissible transformations. A ratio statement would require the Kelvin scale, on which the two temperatures are $293.15$ and $299.15$ kelvin and the ratio is about $1.020$ in both.

### 4.9 Problem: build a discrete frequency distribution

A survey records the number of children in each of $35$ families: $1, 0, 2, 3, 4, 5, 6, 7, 2, 3, 4, 0, 2, 5, 8, 4, 5, 12, 6, 3, 2, 7, 6, 5, 3, 3, 7, 8, 9, 7, 9, 4, 5, 4, 3$. Construct the frequency distribution and compute the mean.

### 4.10 Solution: tally, verify, then summarise

Step 1. Establish the scale. The variable counts children, the halfway value between $2$ and $3$ children is impossible, so the variable is discrete on a ratio scale.

Step 2. Find the range. The smallest observation is $0$ and the largest is $12$, so the table must run from $0$ to $12$.

Step 3. Tally the observations in one systematic pass and record the frequencies.

| Number of children | Frequency |
|---|---|
| 0 | 2 |
| 1 | 1 |
| 2 | 4 |
| 3 | 6 |
| 4 | 5 |
| 5 | 5 |
| 6 | 3 |
| 7 | 4 |
| 8 | 2 |
| 9 | 2 |
| 10 | 0 |
| 11 | 0 |
| 12 | 1 |
| Total | 35 |

Step 4. Verify the total:

$$
2 + 1 + 4 + 6 + 5 + 5 + 3 + 4 + 2 + 2 + 0 + 0 + 1 = 35
$$

which matches the number of families, so the tally is complete.

Step 5. Compute the mean from the frequency table:

$$
\bar{x} = \frac{1}{35}\left(0(2) + 1(1) + 2(4) + 3(6) + 4(5) + 5(5) + 6(3) + 7(4) + 8(2) + 9(2) + 12(1)\right)
$$

Step 6. Evaluate the numerator and divide:

$$
\bar{x} = \frac{164}{35} \approx 4.69
$$

Step 7. Interpret. The mean of about $4.69$ children is legitimate because the variable is quantitative and ratio-scaled, but the value is not itself an attainable count, which is normal for a mean of discrete data. The two zero frequencies are retained because they document the gap in the distribution rather than concealing it.

### 4.11 Problem: summarise grouped continuous measurements

The masses of $100$ female students are recorded to the nearest kilogram and grouped into the classes $50$ to $52$, $53$ to $55$, $56$ to $58$, $59$ to $61$, and $62$ to $64$, with frequencies $5$, $18$, $42$, $27$, and $8$. Find the class boundaries, the class marks, the mean mass, the standard deviation, and the coefficient of variation.

### 4.12 Solution: boundaries first, then the weighted summaries

Step 1. Establish that the variable is continuous. Mass can take any value in an interval, so the data are continuous on a ratio scale and must be grouped.

Step 2. Compute the boundaries. Because each mass is reported to the nearest kilogram, the boundary between adjacent classes lies half a kilogram beyond each stated limit, giving $49.5$, $52.5$, $55.5$, $58.5$, $61.5$, and $64.5$.

Step 3. Compute the class width from the boundaries:

$$
h = 52.5 - 49.5 = 3
$$

and verify that every adjacent pair differs by $3$, so the classes are of equal width.

Step 4. Compute the class marks as the midpoints of the boundaries, obtaining $51$, $54$, $57$, $60$, and $63$.

Step 5. Compute the weighted total of the class marks:

$$
\sum_{j=1}^{5} f_j m_j = 5(51) + 18(54) + 42(57) + 27(60) + 8(63) = 5745
$$

Step 6. Divide by the total frequency to obtain the mean:

$$
\bar{x} = \frac{5745}{100} = 57.45
$$

Step 7. Compute the weighted total of the squared class marks:

$$
\sum_{j=1}^{5} f_j m_j^{2} = 5(2601) + 18(2916) + 42(3249) + 27(3600) + 8(3969) = 330903
$$

Step 8. Apply the shortcut identity for the variance, $s^{2} = \frac{1}{n}\sum f_j m_j^{2} - \bar{x}^{2}$:

$$
s^{2} = \frac{330903}{100} - \left(57.45\right)^{2} = 3309.03 - 3300.5025 = 8.5275
$$

Step 9. Take the square root and form the coefficient of variation:

$$
s = \sqrt{8.5275} \approx 2.92, \qquad v = \frac{2.92}{57.45} \approx 0.0508
$$

Step 10. Interpret. The mean mass is about $57.45$ kilograms and the standard deviation about $2.92$ kilograms, so a typical student lies within roughly three kilograms of the mean. The coefficient of variation of about $5.1$ per cent is admissible only because mass has a true zero; the same calculation on a temperature in degrees Celsius would be meaningless. All figures are approximations bounded by half a class width, that is by $1.5$ kilograms, because each observation was replaced by its class mark.

### 4.13 Problem: choose the display for four data sets

Four data sets are available: the blood groups of $200$ donors; the pain grades of $80$ patients; the masses of $100$ students grouped into five classes; and the payment method and customer category of $120$ shoppers. Recommend a display for each and justify the choice by scale.

### 4.14 Solution: match the display to the structure

Step 1. Blood groups. The scale is nominal and the categories are parts of a whole, so a bar chart with gaps between bars is appropriate, and a pie chart is acceptable because the categories exhaust the sample. A histogram would be wrong, because a histogram implies an underlying continuous axis.

Step 2. Pain grades. The scale is ordinal, so a bar chart is appropriate provided the bars are ordered from mild to severe. The ordering of the bars carries information that a pie chart, which loses order, would discard.

Step 3. Masses. The scale is continuous and the data are grouped, so a histogram with bars touching at the class boundaries is appropriate, and a frequency polygon drawn through the class marks is an equivalent line summary. An ogive, plotting cumulative frequency against the upper class boundary, displays the same data cumulatively.

Step 4. Payment method by customer category. Both variables are categorical, so a contingency table is the primary display and a clustered bar chart is the secondary display that makes the conditional distributions visible. A scatter diagram would be wrong, because both variables are categorical.

Step 5. Interpret. In each case the display was chosen from the scale rather than from taste: gaps between bars signal categorical categories, touching bars signal a continuous axis, and a grid of cells signals two categorical variables.

## 5. Mathematical Extensions, Limits, and Common Errors

### 5.1 The scales form a nested family of models

The four scales are not four unrelated labels but a nested sequence of models, each obtained from the previous one by adding a structural assumption. A nominal scale assumes only that categories can be distinguished. An ordinal scale adds an order relation. An interval scale adds a metric, that is a rule for comparing differences. A ratio scale adds a fixed origin, which is what makes multiplication meaningful. Each added assumption licenses further statistics and correspondingly narrows the class of transformations that leave the data unchanged.

The nesting has a practical reading. Any statistic that is admissible at a weaker level remains admissible at every stronger level: a mode is a legitimate summary of ratio data as well as of nominal data. The converse fails, and the failure is the source of nearly every error in this topic. The mean is not rescued by the fact that interval data are almost ratio data; it is licensed by equal spacing alone, and it is destroyed by the absence of a true zero only when a ratio rather than a difference is reported.

### 5.2 Simpson's paradox in cross-classification

A contingency table can show an association in one direction in every subpopulation and the opposite association in the pooled table. Suppose a hospital compares recovery rates for two treatments, and that the patients differ in severity. Among the mild cases treatment A recovers $81$ of $90$ and treatment B recovers $19$ of $20$; among the severe cases treatment A recovers $1$ of $10$ and treatment B recovers $3$ of $20$. Within each stratum B is the better treatment, at $95$ per cent against $90$ per cent among the mild cases and $15$ per cent against $10$ per cent among the severe cases, yet pooling gives A a rate of $82/100 = 82$ per cent against B's $22/40 = 55$ per cent.

The reconciliation is the imbalance of the two groups: $90$ of the $100$ patients given A were mild, whereas only $20$ of the $40$ patients given B were mild, so the pooled rate for A is dominated by the easy cases while the pooled rate for B is diluted by the difficult ones. Severity is associated with both the treatment received and the outcome, so the marginal comparison is confounded. The lesson for this topic is that a cross-classification is not a single summary but a family of conditional summaries, and that collapsing a table by summing over a category can reverse the association. Reporting a marginal percentage without the conditional percentages is therefore not merely incomplete; it can be actively misleading.

### 5.3 Measurement error and the continuous ideal

Continuity is an idealisation. Every instrument has a resolution, so every recorded measurement is a rounded value and therefore, strictly, a class mark. The continuous model is a limiting description that becomes accurate as the resolution becomes fine relative to the variation being studied. When the resolution is coarse, the continuous model misleads: a mass recorded to the nearest ten kilograms loses the within-class variation entirely, and the grouped standard deviation understates the true spread because it measures variation between class marks rather than variation among observations.

The appropriate response is not to abandon the continuous model but to state the resolution and to check that the class width is small relative to the standard deviation. A working rule is that the class width should not exceed roughly one quarter of the standard deviation, so that grouping error stays modest compared with genuine variation.

### 5.4 The limits of ordinal arithmetic

Ordinal data support order, and order alone supports a family of statistics: the median, the quartile categories, the modal category, rank correlation, and any summary built from counts of comparisons. They do not support the arithmetic mean, the variance, the standard deviation, the mean absolute deviation, the coefficient of variation, or the geometric mean. The mean absolute deviation is disqualified for a reason that is easy to overlook: it is defined through absolute differences from the median, and a difference requires subtraction, which requires equal spacing.

A widely used compromise is to treat a long ordinal scale with many categories as approximately interval and to report means with an explicit caveat. The compromise can be defended empirically, by evidence that respondents treat the categories as equally spaced, but it cannot be defended by the scale itself. When the compromise is adopted, the median should be reported alongside the mean so that a reader who rejects the assumption still has an admissible summary.

### 5.5 Common errors and how to avoid them

- **Reading the digits instead of the variable.** Averaging category codes, such as arrival codes $1$, $2$, and $3$, produces a number that describes the coding sheet. Ask whether the recorded value could be replaced by any other label without losing information; if the answer is yes, the value is nominal.
- **Upgrading an ordinal scale to interval by assertion.** Calling a five-point rating scale "numerical" because the responses were typed as digits does not create equal spacing. Equal spacing must be demonstrated, not assumed.
- **Treating recording precision as discreteness.** Age in whole years looks discrete, but the variable is continuous. Apply the halfway test to the variable, not to the printed values.
- **Using the sample standard deviation on a nominal variable.** Dispersion for nominal data must be measured by an index built from frequencies, such as the index of qualitative variation.
- **Reporting a coefficient of variation for interval data.** The index depends on the arbitrary origin, so it changes when the same data are expressed in a different but equally valid unit system.
- **Subtracting quartiles on an ordinal scale.** Report the quartile categories as a pair rather than their difference, because subtraction assumes equal spacing.
- **Confusing a marginal percentage with a conditional percentage.** A claim about a subgroup requires the conditional distribution, and the two can point in opposite directions.
- **Choosing a histogram for categorical data.** A histogram asserts a continuous underlying axis; categorical data require a bar chart with gaps, and ordinal data require that the bars be ordered.
- **Forgetting that grouping discards information.** A grouped mean and a grouped standard deviation are approximations bounded by the class width, and they must be reported as such.
