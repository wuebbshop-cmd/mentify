## 1. Foundational Concepts, Definitions, and Axioms

### 1.1 What statistics is, and the two purposes it serves

Statistics is the science of data. In its full operational sense it involves collecting, classifying, summarizing, organizing, analyzing, and interpreting numerical information. The subject is applied across medicine, biology, sociology, engineering, and commerce precisely because each of these disciplines generates unwieldy masses of observations that must be reduced to intelligible form before any decision can be defended.

The discipline serves two genuinely different purposes, and the distinction is one of intent rather than of technique.

> **Definition (Descriptive statistics).** Descriptive statistics uses numerical and graphical methods to look for patterns in a data set, and to present that information in a convenient form.

> **Definition (Inferential statistics).** Inferential statistics uses sample data to make estimates, decisions, predictions, or other generalizations about a larger set of data.

Descriptive work stops at the data in hand: it tabulates, averages, and displays. Inferential work reaches beyond the data in hand: it extrapolates from a measured subset to an unmeasured whole, and every such extrapolation carries an explicit statement of how much confidence the extrapolation deserves. A single sentence that reports a sample mean is descriptive; a sentence that claims the mean of an entire population lies between two numbers, with a stated confidence, is inferential.

### 1.2 The five fundamental elements

Five elements recur throughout the unit and must be mastered as vocabulary, because every later problem is posed in these terms.

- A **population** is the set of all units — usually people, objects, transactions, or events — that we are interested in studying. A population is defined by the question asked, not by its physical size; it may be the 42 learners in one class or every registered voter in a country.
- A **variable** is a characteristic or property of an individual population unit. Age, mass, income, and opinion are variables; a specific age is an observation of a variable.
- A **sample** is a subset of the units of a population. The sample is what is actually measured when measuring everything is impossible, too costly, or destructive.
- A **statistical inference** is an estimate, prediction, or some other generalization about a population based on information contained in a sample.
- A **measure of reliability** is a statement, usually attached to a statistical inference, that quantifies confidence in it. Without a measure of reliability an inference is an unsupported assertion.

The logical chain joining these elements is fixed: a variable is measured on a sample drawn from a population, an inference is formed about the population, and a measure of reliability states how much trust the inference merits.

### 1.3 Probability as the companion discipline

Probability is the study of uncertainty and the likelihood of events. Where statistics summarizes and generalizes from observed data, probability quantifies how likely outcomes are before or beyond observation. The two subjects are bound together because inference is impossible without a probability model: the measure of reliability that qualifies every inference is a probability statement, and the sampling distributions that make inference possible are products of probability theory.

The elementary vocabulary of probability is used from the first lesson onward.

- An **experiment** is any process whose outcome cannot be predicted with certainty in advance.
- The **sample space**, denoted $S$, is the set of all possible outcomes of an experiment.
- An **event** is a subset of the sample space. An event occurs when the outcome of the experiment lies in that subset.
- Two events are **mutually exclusive** when they cannot occur together, that is, when their intersection is empty.
- A collection of events is **exhaustive** when their union is the whole sample space.
- Two events are **equally likely** when the model assigns them the same probability; the classical definition of probability depends on this assumption.

### 1.4 The axioms of probability

Modern probability rests on three axioms stated for a sample space $S$ and events $A$, $B$ within it. Probabilities are numbers assigned to events, written $P(A)$.

> **Axiom 1 (Non-negativity).** For every event $A$, the probability satisfies $P(A) \ge 0$.

> **Axiom 2 (Normalisation).** The probability of the certain event is one, so $P(S) = 1$.

> **Axiom 3 (Countable additivity).** If the events $A_1, A_2, \dots$ are mutually exclusive, then the probability of their union is the sum of their probabilities, that is $P\left(\bigcup_{i=1}^{\infty} A_i\right) = \sum_{i=1}^{\infty} P(A_i)$.

From these three axioms every other rule of probability is derived; nothing further is assumed. In particular the complement rule, the addition law, and the monotonicity property proved in Section 3 are all consequences, not independent assumptions.

### 1.5 Types of data and sources of data

Data are of two types, and the distinction governs which summaries and which methods are legitimate.

- **Quantitative data** are measurements recorded on a naturally occurring numerical scale. Mass, number of children, and examination mark are quantitative.
- **Qualitative data** are measurements that cannot be measured on a natural numerical scale and can only be classified into one of a group of categories. Sex, religion, and employment status are qualitative.

A finer classification of measurement scales is used when deciding what arithmetic is meaningful.

- **Nominal** data are qualitative measurements that differ only in name or category, with no order; averaging them is meaningless.
- **Ordinal** data are qualitative measurements that carry a meaningful order but not a meaningful distance; ranks and grades are ordinal.
- **Interval** data are quantitative measurements with equal distances between consecutive values but an arbitrary zero point; temperatures in degrees Celsius are interval.
- **Ratio** data are quantitative measurements with equal distances and a true zero, so that ratios are meaningful; mass and income are ratio measurements.

Data may be obtained in four ways: from a published source, from a designed experiment, from a survey, and observationally. The route by which data were obtained determines what may be concluded. A designed experiment can support a causal statement because the investigator controls the assignment of treatments; a survey or an observational study generally cannot, because uncontrolled factors may be confounded with the variable of interest.

### 1.6 Notation: summation and frequencies

The unit fixes a notation that every subsequent formula relies upon. Let $x_i$ for $i = 1, 2, 3, \dots, n$ denote the values assumed by a variable $X$; thus $x_i$ represents the $i$-th observation. The symbol $\sum_{i=1}^{n} x_i$ denotes the sum of all the $x_i$ from the first to the last.

$$
\sum_{i=1}^{n} x_i = x_1 + x_2 + \cdots + x_n
$$

When values repeat, the data are recorded as a frequency distribution: the distinct values $x_1, \dots, x_k$ are listed with their frequencies $f_1, \dots, f_k$, and the total number of observations is $n = \sum_{i=1}^{k} f_i$.

### 1.7 The vocabulary of grouping

Grouped data are summarised in classes, and the vocabulary of classes must be exact because several formulas depend on it.

- A **class interval** is the symbol defining a class, such as $50\text{–}52$.
- The numbers $50$ and $52$ are the **class limits**; the left figure is the **lower class limit** and the right figure the **upper class limit**.
- The true dividing lines between adjacent classes, such as $49.5$ and $52.5$, are the **class boundaries**, also called the true class limits.
- The **class width** is the difference between the upper and lower class boundaries of a class.
- The **class mark** is the midpoint of the class interval, computed as the average of the two class boundaries.
- The **cumulative frequency** up to and including a class is the total frequency of all values below the upper class boundary of that class.

Two computational settings therefore recur. In **ungrouped** or simple series data each observation is listed individually and the mean is the total divided by the count. In **grouped** data the observations are compressed into classes, each class is represented by its class mark, and the resulting summaries are approximations whose accuracy depends on how well the class mark represents the values it stands for.

## 2. Theorems, Lemmas, and Analytical Properties

### 2.1 Linearity of the summation operator

> **Lemma (Linearity of summation).** For constants $a$ and $b$, and sequences $x_i$ and $y_i$ of equal length,
> 
> $$
> \sum_{i=1}^{n}\left(a x_i + b y_i\right) = a\sum_{i=1}^{n} x_i + b\sum_{i=1}^{n} y_i .
> $$

This lemma is the single algebraic tool behind every shortcut in the unit. It permits a constant to be pulled through a sum, allows a sum to be split, and makes the assumed-mean and coding methods possible.

Two immediate corollaries are used constantly.

> **Corollary (Sum of a constant).** For a constant $c$ taken $n$ times, $\sum_{i=1}^{n} c = nc$.

> **Corollary (Scaling).** If every observation is multiplied by $b$, then $\sum_{i=1}^{n} b x_i = b\sum_{i=1}^{n} x_i$, so the total scales by the same factor.

### 2.2 Properties of the arithmetic mean

Let $\bar{x} = \frac{1}{n}\sum_{i=1}^{n} x_i$ be the arithmetic mean of $x_1, \dots, x_n$.

> **Theorem (Zero sum of deviations).** The sum of the deviations of the observations from their own arithmetic mean is zero, that is
> 
> $$
> \sum_{i=1}^{n}\left(x_i - \bar{x}\right) = 0 .
> $$

> **Theorem (Minimum sum of squares).** Among all constants $c$, the sum of squared deviations $\sum_{i=1}^{n}\left(x_i - c\right)^2$ is smallest when $c = \bar{x}$.

The first theorem says the mean is the balance point of the data. The second says the mean is the best constant predictor under a squared-error criterion, which is why the mean rather than the median appears in the definitions of variance and of the least-squares regression line.

> **Theorem (Shift of origin).** If a constant $A$ is subtracted from every observation, the mean is reduced by exactly $A$, so
> 
> $$
> \bar{x} = A + \frac{1}{n}\sum_{i=1}^{n}\left(x_i - A\right).
> $$

> **Theorem (Change of scale).** If every observation is divided by a constant $h$ after subtracting $A$, then
> 
> $$
> \bar{x} = A + h \cdot \frac{1}{n}\sum_{i=1}^{n}\frac{x_i - A}{h}.
> $$

These two theorems are precisely the assumed-mean method and the coding method. They are not separate formulas to be memorised; they are the same identity, applied with different choices of $A$ and $h$.

### 2.3 Properties of class marks and cumulative frequencies

> **Lemma (Midpoint property).** For a class with lower boundary $L$ and upper boundary $U$, the class mark equals $\frac{L+U}{2}$, and consecutive class marks differ by exactly one class width when the classes are of equal width.

> **Theorem (Monotonicity of cumulative frequency).** The cumulative frequency function is non-decreasing and attains the total number of observations at the last class boundary, that is
> 
> $$
> F_j = \sum_{i=1}^{j} f_i, \qquad F_j \le F_{j+1}, \qquad F_k = n .
> $$

This theorem provides the arithmetic check that protects every grouped frequency table: if the final cumulative frequency differs from $n$, the tally is wrong.

### 2.4 Consequences of the axioms of probability

> **Theorem (Probability of the impossible event).** The empty event has probability zero, so $P(\varnothing) = 0$.

> **Theorem (Complement rule).** For any event $A$ with complement $A'$,
> 
> $$
> P(A') = 1 - P(A).
> $$

> **Theorem (Monotonicity).** If $A \subseteq B$ then $P(A) \le P(B)$.

> **Theorem (Addition law for two events).** For any two events $A$ and $B$,
> 
> $$
> P(A \cup B) = P(A) + P(B) - P(A \cap B).
> $$

> **Theorem (Addition law for three events).** For any three events $A$, $B$, and $C$,
> 
> $$
> P(A \cup B \cup C) = P(A) + P(B) + P(C) - P(A \cap B) - P(A \cap C) - P(B \cap C) + P(A \cap B \cap C).
> $$

The subtraction in the two-event law removes the double counting of the overlap; the final addition in the three-event law restores the triple overlap, which the three pairwise subtractions removed once too often. This alternating pattern is the inclusion–exclusion principle.

> **Theorem (Boole's inequality).** For any finite collection of events,
> 
> $$
> P\left(\bigcup_{i=1}^{k} A_i\right) \le \sum_{i=1}^{k} P(A_i).
> $$

> **Theorem (Law of total probability).** If $A_1, \dots, A_k$ are mutually exclusive and exhaustive, then for any event $B$,
> 
> $$
> P(B) = \sum_{i=1}^{k} P\left(B \mid A_i\right) P\left(A_i\right).
> $$

The law of total probability is the property that makes partitioning arguments work, and it is the step immediately preceding Bayes' theorem in the later lessons of the course.

### 2.5 Analytical properties of grouped summaries

> **Lemma (Uniform-width class marks).** When all classes share width $h$ and the first class mark is $m_1$, the class marks form an arithmetic progression $m_j = m_1 + (j-1)h$, so the total $\sum_j f_j m_j$ can be evaluated as a weighted sum of an arithmetic progression.

> **Theorem (Grouped mean as a weighted mean).** If each observation in class $j$ is replaced by the class mark $m_j$, then the grouped mean is the weighted average
> 
> $$
> \bar{x} = \frac{\sum_{j=1}^{k} f_j m_j}{\sum_{j=1}^{k} f_j}.
> $$

The theorem is exact as an identity about the substituted values, but only approximate as an estimate of the original data, because within-class variation is discarded. The size of that approximation error is governed by the within-class spread and shrinks as the class width shrinks, an idea formalised in Section 3.

## 3. Formal Proofs, Derivations, and Methods

### 3.1 Proof that the deviations from the mean sum to zero

Let $x_1, \dots, x_n$ be observations with mean $\bar{x} = \frac{1}{n}\sum_{i=1}^{n} x_i$. Then

$$
\sum_{i=1}^{n}\left(x_i - \bar{x}\right) = \sum_{i=1}^{n} x_i - \sum_{i=1}^{n} \bar{x}
$$

by linearity of summation. The first term is $n\bar{x}$ by definition of the mean, and the second is $n\bar{x}$ by the sum-of-a-constant corollary. Hence

$$
\sum_{i=1}^{n}\left(x_i - \bar{x}\right) = n\bar{x} - n\bar{x} = 0 .
$$

Since the sum of deviations is zero, the mean acts as the point at which positive and negative deviations balance, which is the mathematical content of calling the mean a measure of location.

### 3.2 Proof that the mean minimises the sum of squared deviations

Define $g(c) = \sum_{i=1}^{n}\left(x_i - c\right)^2$ and expand the square.

$$
g(c) = \sum_{i=1}^{n} x_i^2 - 2c\sum_{i=1}^{n} x_i + nc^2
$$

This is a quadratic in $c$ with a positive coefficient on $c^2$, so it has a unique minimum where its derivative vanishes. Differentiating,

$$
g'(c) = -2\sum_{i=1}^{n} x_i + 2nc
$$

Setting $g'(c) = 0$ gives $nc = \sum_{i=1}^{n} x_i$, hence $c = \bar{x}$. Because the second derivative is $2n > 0$, this stationary point is the global minimum.

### 3.3 Derivation of the shift-of-origin and coding formulas

Start from any constant $A$. By linearity,

$$
\frac{1}{n}\sum_{i=1}^{n}\left(x_i - A\right) = \frac{1}{n}\sum_{i=1}^{n} x_i - \frac{1}{n}\sum_{i=1}^{n} A = \bar{x} - A .
$$

Rearranging gives the shift-of-origin identity

$$
\bar{x} = A + \frac{1}{n}\sum_{i=1}^{n}\left(x_i - A\right).
$$

Now set $u_i = \frac{x_i - A}{h}$ for a non-zero constant $h$. Then $x_i = A + h u_i$, so by linearity

$$
\frac{1}{n}\sum_{i=1}^{n} x_i = \frac{1}{n}\sum_{i=1}^{n}\left(A + h u_i\right) = A + h \cdot \frac{1}{n}\sum_{i=1}^{n} u_i ,
$$

which is the coding identity

$$
\bar{x} = A + h\bar{u} .
$$

The practical consequence is that a large set of grouped data can be reduced to small integers $u_i$, averaged, and then transformed back, with no change in the final answer and far less arithmetic risk.

### 3.4 Derivation of the complement rule from the axioms

The events $A$ and $A'$ are mutually exclusive, since no outcome belongs to both, and they are exhaustive, since every outcome lies in one of them. Therefore $A \cup A' = S$ and $A \cap A' = \varnothing$. By Axiom 3,

$$
P(A) + P(A') = P\left(A \cup A'\right) = P(S) = 1 ,
$$

using Axiom 2 for the last equality. Hence $P(A') = 1 - P(A)$.

### 3.5 Derivation of the two-event addition law

Write the union as a disjoint union in two pieces, namely $A \cup B = A \cup \left(B \cap A'\right)$, where $A$ and $B \cap A'$ are mutually exclusive. By Axiom 3,

$$
P(A \cup B) = P(A) + P\left(B \cap A'\right).
$$

Similarly $B = \left(B \cap A\right) \cup \left(B \cap A'\right)$ is a disjoint union, so

$$
P(B) = P(A \cap B) + P\left(B \cap A'\right).
$$

Solving the second identity for $P\left(B \cap A'\right)$ and substituting into the first gives

$$
P(A \cup B) = P(A) + P(B) - P(A \cap B).
$$

### 3.6 Derivation of the three-event addition law

Apply the two-event law twice. First,

$$
P(A \cup B \cup C) = P(A \cup B) + P(C) - P\left((A \cup B) \cap C\right).
$$

Distributing the intersection over the union,

$$
(A \cup B) \cap C = (A \cap C) \cup (B \cap C),
$$

so the two-event law gives

$$
P\left((A \cup B) \cap C\right) = P(A \cap C) + P(B \cap C) - P(A \cap B \cap C).
$$

Substituting both pieces yields

$$
P(A \cup B \cup C) = P(A) + P(B) - P(A \cap B) + P(C) - P(A \cap C) - P(B \cap C) + P(A \cap B \cap C),
$$

which is the stated law.

### 3.7 Method: constructing a grouped frequency distribution

The construction follows a fixed sequence, and each step has a check.

1. Find the minimum and the maximum of the raw data and compute the range as their difference.
2. Choose the number of classes $k$, commonly by Sturges' rule with $k = 1 + 3.322\log_{10} n$ rounded up, and choose a convenient class width $h$ at least as large as the range divided by $k$.
3. Fix the lower boundary of the first class at or just below the minimum, then generate consecutive classes of width $h$.
4. Tally each observation into exactly one class, using the convention that a value on a boundary belongs to the class whose lower boundary it equals.
5. Record the frequency of each class, then verify that the frequencies sum to $n$ and that every observation has been counted exactly once.
6. Add the class marks, and if required the cumulative frequencies, and re-verify that the last cumulative frequency equals $n$.

### 3.8 Method: computing a grouped mean by three routes

Given classes with frequencies, the mean can be obtained by the direct method, the assumed-mean method, or the coding method. All three are the same identity from Section 3.3.

- **Direct method.** Multiply each class mark by its frequency, sum the products, and divide by $n$, using the formula for the weighted mean of class marks.
- **Assumed-mean method.** Choose a class mark near the middle as $A$, form the deviations $d_j = m_j - A$, then compute the mean as $A$ plus the mean deviation.
- **Coding method.** With $A$ as above and $h$ the common class width, set $u_j$ equal to the deviation divided by $h$, then compute the mean as $A + h\bar{u}$.

The assumed-mean and coding routes reduce the size of the numbers being multiplied, which is why they are preferred in examinations where arithmetic slips are costly.

### 3.9 Method: bounding the error introduced by grouping

Let the true observations in class $j$ have mean $\mu_j$ and let the class mark be $m_j$. The grouped mean and the true mean differ by

$$
\bar{x}_{\text{grouped}} - \bar{x}_{\text{true}} = \frac{1}{n}\sum_{j=1}^{k} f_j\left(m_j - \mu_j\right).
$$

Because each $m_j$ and each observation in its class lie within half a class width of each other, the deviation satisfies $\left|m_j - \mu_j\right| \le \frac{h}{2}$, and therefore

$$
\left|\bar{x}_{\text{grouped}} - \bar{x}_{\text{true}}\right| \le \frac{h}{2}.
$$

The bound states the practically important fact that the grouped mean is never wrong by more than half a class width, so halving the class width halves the worst-case error.

## 4. Representative Worked Examples and Solutions

### 4.1 Problem: a discrete frequency distribution from raw observations

In a survey of $35$ families in a certain village, the number of children per family was recorded.

| 1 | 0 | 2 | 3 | 4 | 5 | 6 |
|---|---|---|---|---|---|---|
| 7 | 2 | 3 | 4 | 0 | 2 | 5 |
| 8 | 4 | 5 | 12 | 6 | 3 | 2 |
| 7 | 6 | 5 | 3 | 3 | 7 | 8 |
| 9 | 7 | 9 | 4 | 5 | 4 | 3 |

### 4.2 Solution: tally each distinct value once

Step 1. Identify the range. The smallest recorded value is $0$ and the largest is $12$, so the table must cover every integer from $0$ to $12$.

Step 2. Tally in a single systematic pass, reading row by row.

Step 3. Record the frequencies and total them.

| Number of children | Tally marks | Frequency |
|---|---|---|
| 0 | // | 2 |
| 1 | / | 1 |
| 2 | //// | 4 |
| 3 | //// / | 6 |
| 4 | //// | 5 |
| 5 | //// | 5 |
| 6 | /// | 3 |
| 7 | //// | 4 |
| 8 | // | 2 |
| 9 | // | 2 |
| 10 | – | 0 |
| 11 | – | 0 |
| 12 | / | 1 |
| Total | | 35 |

Step 4. Check the total. Adding the frequencies gives a sum of $35$, which agrees with the stated number of families, so no observation has been lost or double counted.

Step 5. Interpret. Values $10$ and $11$ appear with frequency zero because the table spans the full range from the minimum to the maximum; their presence makes the gap in the distribution explicit rather than concealing it.

### 4.3 Problem: grouping vocabulary from a grouped distribution

The masses of $100$ female students at a certain school are presented as a grouped frequency distribution.

| Mass (Kg.) | Number of students |
|---|---|
| 50 – 52 | 5 |
| 53 – 55 | 18 |
| 56 – 58 | 42 |
| 59 – 61 | 27 |
| 62 – 64 | 8 |
| Total | 100 |

### 4.4 Solution: extract boundaries, width, marks, and cumulative frequencies

Step 1. Count the classes. There are five classes, with total frequency $100$.

Step 2. Compute the class boundaries. The gap between the upper limit of one class and the lower limit of the next is one unit, so each boundary lies half a unit beyond the limit, giving $49.5$, $52.5$, $55.5$, $58.5$, $61.5$, $64.5$.

Step 3. Compute the class width from boundaries rather than from limits:

$$
h = 52.5 - 49.5 = 3 .
$$

The same value is obtained from every adjacent pair, which confirms that the classes are of equal width.

Step 4. Compute the class mark of the last class as the average of its boundaries:

$$
m_5 = \frac{61.5 + 64.5}{2} = 63 .
$$

Step 5. Accumulate the frequencies to obtain cumulative frequencies $0$, $5$, $23$, $65$, $92$, $100$. The final cumulative frequency equals the total of $100$ students, which verifies the table.

Step 6. Interpret. The class mark $63$ is the representative value used for every student in the class $62\text{–}64$ when the mean is computed from this table; the accuracy of that substitution is bounded by half a class width, that is by $1.5$ kg.

### 4.5 Problem: the mean of a simple series

Compute the arithmetic mean of the observations $3$, $6$, $9$, $13$, $15$.

### 4.6 Solution: sum, count, divide

Step 1. Sum the observations using the summation notation:

$$
\sum_{i=1}^{5} x_i = 3 + 6 + 9 + 13 + 15 = 46 .
$$

Step 2. Count the observations, obtaining $n = 5$.

Step 3. Divide the total by the count:

$$
\bar{x} = \frac{46}{5} = 9.2 .
$$

Step 4. Verify using the zero-sum property. The deviations are $-6.2$, $-3.2$, $-0.2$, $3.8$, and $5.8$, and their sum is zero, confirming the computed mean.

### 4.7 Problem: a grouped mean by all three methods

A distribution has classes $10\text{–}19$, $20\text{–}29$, $30\text{–}39$, $40\text{–}49$, $50\text{–}59$ with frequencies $5$, $8$, $15$, $12$, and $10$. Compute the mean.

### 4.8 Solution: direct, assumed-mean, and coding routes

Step 1. Compute the class marks as midpoints of the boundaries $9.5, 19.5, \dots, 59.5$, obtaining $14.5$, $24.5$, $34.5$, $44.5$, and $54.5$.

Step 2. Apply the direct method. Form the products of frequency and class mark:

$$
\sum_{j=1}^{5} f_j m_j = 5(14.5) + 8(24.5) + 15(34.5) + 12(44.5) + 10(54.5) = 1865 .
$$

Since the total frequency is $50$,

$$
\bar{x} = \frac{1865}{50} = 37.3 .
$$

Step 3. Apply the assumed-mean method with $A = 34.5$. The deviations are $-20$, $-10$, $0$, $10$, and $20$, so

$$
\sum_{j=1}^{5} f_j d_j = 5(-20) + 8(-10) + 15(0) + 12(10) + 10(20) = 140 ,
$$

and therefore

$$
\bar{x} = 34.5 + \frac{140}{50} = 34.5 + 2.8 = 37.3 .
$$

Step 4. Apply the coding method with $A = 34.5$ and $h = 10$. The coded values are $-2$, $-1$, $0$, $1$, and $2$, so

$$
\sum_{j=1}^{5} f_j u_j = 5(-2) + 8(-1) + 15(0) + 12(1) + 10(2) = 14 ,
$$

and hence

$$
\bar{x} = 34.5 + 10\left(\frac{14}{50}\right) = 34.5 + 2.8 = 37.3 .
$$

Step 5. Compare. All three routes agree at $37.3$, which is the expected outcome because the three formulas are algebraic identities. In an examination the coding route is the least error-prone, since its multiplications involve single-digit integers.

### 4.9 Problem: a probability from the complement rule

A fair die is rolled once. Find the probability that the outcome is not a multiple of $3$.

### 4.10 Solution: define the event, then use the complement

Step 1. Define the sample space and the event of interest:

$$
S = \{1, 2, 3, 4, 5, 6\}, \qquad A = \{3, 6\} .
$$

Step 2. Compute the probability of $A$ from equally likely outcomes:

$$
P(A) = \frac{|A|}{|S|} = \frac{2}{6} = \frac{1}{3} .
$$

Step 3. Apply the complement rule derived in Section 3.4:

$$
P(A') = 1 - P(A) = 1 - \frac{1}{3} = \frac{2}{3} .
$$

Step 4. Interpret. The complement rule converted a question about six outcomes into a subtraction, which is the standard reason it is preferred whenever the required event is described by a negation.

### 4.11 Problem: an addition law with overlap

Two events are defined on the same die roll, with $A = \{2, 4, 6\}$ the outcome being even and $B = \{3, 6\}$ the outcome being a multiple of $3$. Find the probability of the union.

### 4.12 Solution: subtract the double-counted overlap

Step 1. Compute the individual probabilities:

$$
P(A) = \frac{3}{6} = \frac{1}{2}, \qquad P(B) = \frac{2}{6} = \frac{1}{3} .
$$

Step 2. Identify the intersection and its probability:

$$
A \cap B = \{6\}, \qquad P(A \cap B) = \frac{1}{6} .
$$

Step 3. Apply the addition law:

$$
P(A \cup B) = P(A) + P(B) - P(A \cap B) = \frac{1}{2} + \frac{1}{3} - \frac{1}{6} = \frac{2}{3} .
$$

Step 4. Verify by direct enumeration. The union is $\{2, 3, 4, 6\}$, which contains four of the six outcomes, so its probability is $\frac{4}{6} = \frac{2}{3}$, in agreement with the addition law.

### 4.13 Problem: three overlapping categories

In a survey of $100$ students, $60$ study Mathematics, $50$ study Physics, $40$ study Chemistry, $30$ study both Mathematics and Physics, $20$ study both Physics and Chemistry, $25$ study both Mathematics and Chemistry, and $10$ study all three. How many study at least one of the three, and how many study none?

### 4.14 Solution: apply inclusion and exclusion

Step 1. Write the counts as set sizes:

$$
|M| = 60,\quad |P| = 50,\quad |C| = 40,\quad |M \cap P| = 30,\quad |P \cap C| = 20,\quad |M \cap C| = 25,\quad |M \cap P \cap C| = 10 .
$$

Step 2. Apply the three-event inclusion–exclusion identity proved in Section 3.6:

$$
|M \cup P \cup C| = 60 + 50 + 40 - 30 - 20 - 25 + 10 = 85 .
$$

Step 3. Subtract from the total to obtain the number studying none, which is $15$.

Step 4. Interpret. Ninety-five would be obtained by adding the three headline figures and subtracting nothing, which overcounts every student in two categories; the pairwise subtractions and the final restoration of the triple overlap are what make the count exact.

### 4.15 Problem: identifying the elements of a study

A researcher wishes to know the mean monthly income of the $1\,200$ traders in a market. She selects $80$ traders at random, records their incomes, obtains a mean of $18\,400$, and reports that the market-wide mean income is believed to lie between $16\,900$ and $19\,900$ with $95\%$ confidence. Identify the population, the variable, the sample, the inference, and the measure of reliability.

### 4.16 Solution: name each element against its definition

Step 1. The **population** is the set of all $1\,200$ traders in the market, because that is the group about which the question is asked.

Step 2. The **variable** is monthly income, a quantitative ratio measurement, because it is the characteristic measured on each unit.

Step 3. The **sample** is the $80$ traders actually selected and measured.

Step 4. The **statistical inference** is the statement that the market-wide mean income lies between $16\,900$ and $19\,900$; the sample mean of $18\,400$ is a descriptive summary, whereas the interval is the generalisation beyond the sample.

Step 5. The **measure of reliability** is the phrase "with $95\%$ confidence", which quantifies how often a procedure of this kind produces an interval containing the true mean.

## 5. Mathematical Extensions, Limits, and Common Errors

### 5.1 What the mean does not tell you

The arithmetic mean is a location summary, not a description of the data. Two data sets can share a mean and differ completely in spread, and the mean alone cannot distinguish them. The mean is also not resistant, since a single extreme observation can move it arbitrarily far because every observation enters the total with equal weight. When a distribution is strongly skewed the median is usually the more informative summary of a typical value, and the mean should be reported alongside a measure of dispersion rather than alone.

Grouped summaries add a second limitation. Replacing each observation by its class mark discards all within-class variation, so the grouped mean is an approximation, bounded by half a class width as shown in Section 3.9. Reporting a grouped mean without stating the class width conceals the size of the possible error.

### 5.2 Sturges' rule and the choice of class width

The number of classes is a modelling decision, not a fact about the data. Sturges' rule offers a starting point, and for $n = 50$ observations it evaluates as

$$
k = 1 + 3.322\log_{10}(50) \approx 6.64 ,
$$

so seven classes are appropriate. With a range of, say, $61$, the raw class width would be $61/7 \approx 8.7$, and a convenient rounded width of $10$ would then be adopted. Too few classes hide the shape of the distribution, while too many produce a sparse table dominated by sampling noise; both failures are failures of judgement rather than of arithmetic.

### 5.3 The reliability of an inference depends on the sampling method

A measure of reliability is only as trustworthy as the sampling that produced the data. If the $80$ traders were selected by standing at the market gate on one morning, traders who arrive late are systematically excluded, and the resulting interval may be precise while being biased. Precision and accuracy are different properties: a confidence statement describes precision under a stated sampling design, and it cannot repair a design that selects a non-representative subset. This is the conceptual bridge from descriptive summaries to the sampling techniques studied later in the course.

### 5.4 Chebyshev-type reasoning as an extension of location

Once a mean and a standard deviation are available, a distribution-free statement about spread becomes possible. Chebyshev's inequality states that for any distribution with mean $\mu$ and finite standard deviation $\sigma$,

$$
P\left(\left|X - \mu\right| \ge k\sigma\right) \le \frac{1}{k^2} \quad \text{for } k > 1 .
$$

For $k = 2$ the inequality guarantees that at least three quarters of the observations lie within two standard deviations of the mean, whatever the shape of the distribution. The result is weak compared with the normal-distribution approximations used later, but it requires no assumption beyond a finite variance, which is precisely its value as a first reliability statement.

### 5.5 Common errors and how to avoid them

- **Confusing class limits with class boundaries.** The boundary lies midway between adjacent limits, and using a limit where a boundary is required shifts every subsequent calculation.
- **Computing class width from limits.** The width is the difference between boundaries; for limits $50$ and $52$ with a one-unit gap, the width is $3$ rather than $2$.
- **Treating the class mark as the midpoint of the limits.** The definition is in terms of boundaries, and the two midpoints coincide only when the gap between limits is a single unit.
- **Reporting a grouped mean without qualification.** State that class marks were used as representatives and give the class width, so the reader can judge the approximation.
- **Omitting the total row.** The total is the check that the frequencies sum to $n$, and without it a tallying error remains invisible.
- **Adding probabilities of overlapping events.** The addition law requires subtraction of the intersection, and adding headline figures in a three-category survey systematically overcounts.
- **Calling a descriptive summary an inference.** A sample mean describes the sample; a claim about the population is an inference and requires a measure of reliability.

### 5.6 A procedure for any question in this unit

1. Identify the type of each variable as quantitative or qualitative, and note its measurement scale, because the scale determines which summaries are legitimate.
2. If raw data are to be presented, state the range, choose classes, tally in one pass, and verify that the frequencies sum to $n$.
3. If a mean is required from grouped data, compute the class marks from boundaries, then choose the direct, assumed-mean, or coding route and state which was used.
4. If a probability is required, write the sample space and the events explicitly before applying an axiom, the complement rule, or an addition law.
5. If a claim about a population is made, separate the descriptive statement from the inferential statement and attach the measure of reliability to the latter.

### 5.7 Consolidation

The unit established one chain of reasoning that every later topic extends. Data are classified by type and scale, so that the summaries applied to them are meaningful. Grouped presentation replaces observations by class marks, which makes computation tractable at a stated cost in accuracy. The arithmetic mean emerges as the balance point and as the minimiser of squared error, and the assumed-mean and coding methods are deductions from its linearity. Probability supplies the language of uncertainty through three axioms from which the complement rule, the addition law, and the law of total probability follow as theorems. Inferential statistics then stands on both pillars at once, using a probability model to convert a sample summary into a population claim carrying a measure of reliability.
