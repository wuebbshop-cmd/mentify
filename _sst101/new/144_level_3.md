## 1. Foundational Concepts, Definitions, and Axioms

### 1.1 What an examination in this topic actually asks

Every examination question on measures of central tendency belongs to one of six patterns, and each pattern has a fixed opening move. The first pattern supplies a raw list and asks for the mean, the median and the mode, which tests sorting and counting as much as arithmetic. The second supplies a grouped table and asks for the mean by three named methods, which tests the coding algebra and rewards a single well-built working table. The third supplies a table with one or two blank frequencies and a stated mean, median or total, which tests the setting up and solution of a linear equation. The fourth supplies two or more groups with their means and sizes, which tests the refusal to average averages. The fifth supplies values that are rates or growth factors, which tests whether the harmonic and geometric means can be told apart from the arithmetic mean. The sixth asks for an interpretation, a comparison of merits, or a choice of average for a stated measurement scale, which tests vocabulary rather than computation.

The marks are distributed in a way that punishes haste. A grouped-mean question usually carries twelve to fifteen marks split between three methods, and the three answers must agree; a candidate who makes one arithmetic slip in the working table loses all three parts at once. A quantile question carries marks separately for locating the class, substituting into the formula, and stating the interpretation, so an answer that gives only the final number leaves two thirds of the marks behind. Throughout the topic, the mathematics is elementary and the discipline is everything.

### 1.2 The formula bank

| Quantity | Formula | Condition or note |
|---|---|---|
| Mean, raw | $\bar{x} = \frac{1}{n}\sum x_i$ | always |
| Mean, frequency | $\bar{x} = \frac{\sum f_i x_i}{\sum f_i}$ | class marks for grouped data |
| Assumed mean | $\bar{x} = A + \frac{\sum f_i d_i}{n}$ | $d_i = x_i - A$ |
| Coding | $\bar{x} = A + c\,\bar{u}$ | classes of equal width $c$ |
| Weighted mean | $\bar{x}_w = \frac{\sum w_i x_i}{\sum w_i}$ | weights justified in words |
| Geometric mean | $G = \left(\prod x_i^{f_i}\right)^{1/n}$ | all values positive |
| Harmonic mean | $H = \frac{n}{\sum \frac{f_i}{x_i}}$ | all values positive |
| Quantile | $Q(p) = L + \frac{pn - F}{f} c$ | grouped data |
| Mode, grouped | $L + \frac{f_m - f_1}{2f_m - f_1 - f_2} c$ | modal class |
| Combined mean | $\frac{n_1\bar{x}_1 + n_2\bar{x}_2}{n_1 + n_2}$ | groups of unequal size |
| Corrected mean | $\bar{x}_{\text{new}} = \bar{x}_{\text{old}} + \frac{x_{\text{true}} - x_{\text{recorded}}}{n}$ | one observation repaired |
| Empirical relation | $\text{mode} \approx 3\,\text{median} - 2\,\text{mean}$ | moderately skewed unimodal |

Every entry in the bank is a special case of two ideas: a weighted average, and an interpolation along a cumulative count. Recognising which of the two an unfamiliar formula belongs to is faster than memorising the formula itself.

### 1.3 Notation discipline that earns marks

The symbol $n$ is the total frequency and is obtained by adding the frequency column; the symbol $k$ counts classes or distinct values. Writing $n = 100$ when the table in fact contains ten classes is the commonest single error in the topic, and it is fatal to every later part because the quantile positions are computed from $n$.

The class mark is the midpoint of the class boundaries and not of the limits. For the class $20\text{–}29$ recorded to the nearest unit, the boundaries are $19.5$ and $29.5$ and the mark is $24.5$; the average of the limits gives the same number here, but the habit of averaging limits fails whenever the gaps between classes are unequal.

The assumed mean $A$ and the class width $c$ must be stated explicitly before they are used, and the coded values $u_i$ must be defined as $(x_i - A)/c$ rather than left to be inferred. A marker awards the method marks for the definition and the table, and cannot award them for an answer whose provenance is invisible.

The lower boundary of the class containing a quantile is written $L$, the cumulative frequency below that class $F$, its frequency $f$ and its width $c$. The same four letters serve the median, the quartiles, the deciles and the percentiles, which is why one memorised formula covers all of them. Confusing $f$ with $F$ is the second commonest error in the topic, and it produces answers that are usually far outside the class and therefore easy to detect.

### 1.4 The arithmetic mean in its three examinable forms

The direct form is the definition and is always available.

$$
\bar{x} = \frac{\sum_{i=1}^{k} f_i x_i}{n}
$$

The assumed-mean form subtracts a convenient origin before averaging and adds it back afterwards.

$$
\bar{x} = A + \frac{\sum_{i=1}^{k} f_i d_i}{n}, \qquad d_i = x_i - A
$$

The coding form divides the deviations by the common class width as well, and is available only when every class has the same width.

$$
\bar{x} = A + c\left(\frac{\sum_{i=1}^{k} f_i u_i}{n}\right), \qquad u_i = \frac{x_i - A}{c}
$$

The three forms are algebraically identical, so they must give identical answers, and the examiner frequently says so by asking for the mean "by the direct method, by an assumed mean of $A$, and by the coding method" in three separate parts. The intended strategy is one table with eight columns, from which all three totals are read, rather than three separate computations.

A weighted mean replaces the frequency by a general weight and is used when the weights are credit units, expenditure shares or areas rather than counts.

$$
\bar{x}_w = \frac{\sum_{i=1}^{k} w_i x_i}{\sum_{i=1}^{k} w_i}
$$

### 1.5 The median and the quantile ladder in examinable form

For a raw list the median is the observation in position $(n+1)/2$ when $n$ is odd, and the average of the observations in positions $n/2$ and $n/2 + 1$ when $n$ is even. For a grouped table the median is obtained by interpolation inside the class whose cumulative frequency first reaches or passes $n/2$.

The quartiles, deciles and percentiles use the same interpolation with positions $n/4$, $3n/4$, $in/10$ and $kn/100$. The unified statement is worth writing once and using everywhere.

$$
Q(p) = L + \left(\frac{pn - F}{f}\right) c, \qquad p \in \left\{\frac{1}{4}, \frac{1}{2}, \frac{3}{4}, \frac{i}{10}, \frac{k}{100}\right\}
$$

Three checks are expected and each is usually worth a mark. The quantile must lie inside the class that was identified. The quantiles must appear in increasing order of $p$. And the median computed as $Q(1/2)$ must equal the median computed directly, which is a tautology unless the cumulative column has been misread, in which case the discrepancy exposes the error.

For a raw list the quartiles may be read by any stated convention, provided the convention is stated. The two common conventions split the ordered list into halves and take the median of each half, or use positions $(n+1)/4$ and $3(n+1)/4$. For the twelve values $2, 3, 3, 4, 4, 4, 5, 5, 6, 7, 7, 8$ the halves convention gives a median of $4.5$, a lower quartile of $3.5$ and an upper quartile of $6.5$.

### 1.6 The mode in examinable form

For ungrouped data the mode is the most frequent value; a data set may have one mode, several, or none. For grouped data the modal class is the class with the greatest frequency, and the mode is interpolated inside it.

$$
\text{Mode} = L + \left(\frac{f_m - f_1}{2f_m - f_1 - f_2}\right) c
$$

The interpolation factor can be rewritten as $d_1/(d_1 + d_2)$ with $d_1 = f_m - f_1$ and $d_2 = f_m - f_2$, which shows at a glance that the factor lies between zero and one and that the mode leans towards the heavier neighbour. A mode that falls outside the modal class is arithmetically impossible and signals a slip.

The empirical relation connects the three averages and is used both to estimate a missing one and to check a computed set.

$$
\text{mode} \approx 3\,\text{median} - 2\,\text{mean}
$$

### 1.7 The geometric and harmonic means in examinable form

The geometric mean is the $n$-th root of the product, and with frequencies each value enters as a power.

$$
G = \left(x_1^{f_1} x_2^{f_2} \cdots x_k^{f_k}\right)^{1/n}, \qquad \log G = \frac{1}{n}\sum_{i=1}^{k} f_i \log x_i
$$

The harmonic mean is the reciprocal of the mean of the reciprocals.

$$
H = \frac{n}{\sum_{i=1}^{k}\frac{f_i}{x_i}}
$$

Both require positive values. Both are smaller than the arithmetic mean whenever the values differ, and they are ordered $H \le G \le \bar{x}$, a fact that provides a free check on any computation of all three. The geometric mean answers questions about successive multiplication: growth factors, price relatives, index numbers, average rates of change. The harmonic mean answers questions about fixed totals divided by varying rates: average speed over equal distances, average price per unit for equal expenditures, average output per worker for equal work done.

### 1.8 Which average the examiner expects

| Wording of the question | Average indicated | Reason |
|---|---|---|
| "typical value" of symmetric numerical data | arithmetic mean | uses every observation |
| "middle", "half scored less than" | median | positional |
| "most common", "most popular" | mode | frequency |
| categorical data such as blood group | mode only | no arithmetic on labels |
| average growth, average inflation | geometric mean | multiplicative |
| average speed for equal distances | harmonic mean | rate with fixed numerator |
| data with one extreme value | median | resistant to outliers |
| data with open-ended classes | median or mode | the mean needs class marks |

An answer that computes the arithmetic mean when the question asks for a "typical" value of heavily skewed data is not wrong in arithmetic but wrong in judgement, and the interpretation mark is lost.

### 1.9 Sanity bounds that cost nothing

Four bounds can be checked in seconds and together they catch most arithmetic errors. The mean lies between the smallest and the largest observation. The median lies between the lower and upper quartiles. The mode lies inside the modal class. And for positive data the chain $H \le G \le \bar{x}$ holds. A fifth check is specific to grouped data: the grouped mean must lie between the smallest and largest class marks, and a mean outside that interval has certainly been computed from a misread column.

## 2. Theorems, Lemmas, and Analytical Properties

### 2.1 The high-yield list

| Result | Statement | Where it is used |
|---|---|---|
| Zero-sum lemma | $\sum f_i(x_i - \bar{x}) = 0$ | correcting a mean, deriving the variance |
| Coding theorem | $\bar{y} = a + b\bar{x}$ for $y = a + bx$ | assumed mean, coding, change of units |
| Weighted combination | $\bar{x} = \sum n_j \bar{x}_j / \sum n_j$ | pooled and combined means |
| Mean ordering | $H \le G \le \bar{x}$ | choosing between means, checking |
| Median optimality | the median minimises the sum of absolute deviations | justification of robustness |
| Mean optimality | mean minimises $\sum (x_i - c)^{2}$ | foundation of the variance |
| Mode factor | $0 < \frac{d_1}{d_1 + d_2} < 1$ | checking the interpolated mode |
| Grouping bound | the grouped mean is within half a class width of the true mean | accuracy of grouped means |
| Empirical relation | mode $\approx 3$ median $- 2$ mean | estimating a missing average |
| Outlier shift | mean moves by $\delta/n$, median does not | interpreting a contaminated mean |

### 2.2 The zero-sum lemma and its two consequences

For any data set, the deviations from the mean sum to zero, and the same holds with frequencies.

$$
\sum_{i=1}^{k} f_i\left(x_i - \bar{x}\right) = 0
$$

The first consequence is that the mean depends only on the two totals $\sum f_i x_i$ and $n$, so a single erroneous observation can be repaired without re-adding the list: the total changes by the difference between the true and the recorded value, and the mean changes by that difference divided by $n$. The second consequence is that any claimed mean can be tested against the total it implies, since $n\bar{x}$ must equal the sum of the observations.

### 2.3 The coding theorem

If every observation is transformed by the same linear rule $y_i = a + b x_i$, then the means transform by the same rule.

$$
\bar{y} = a + b\bar{x}
$$

Reading the rule backwards gives both working methods at once: the assumed-mean method uses $a = -A$ and $b = 1$, and the coding method uses $a = -A/c$ and $b = 1/c$. The theorem also covers a change of units, which is why a mean recorded in shillings converts to a mean in thousands of shillings by division, and why the median and the mode convert in exactly the same way provided the transformation is increasing.

### 2.4 The combined-mean theorem

For groups of sizes $n_1, \dots, n_g$ with means $\bar{x}_1, \dots, \bar{x}_g$,

$$
\bar{x} = \frac{\sum_{j=1}^{g} n_j \bar{x}_j}{\sum_{j=1}^{g} n_j} .
$$

The combined mean lies between the smallest and the largest group mean, and equals the unweighted average of the group means only when the group sizes are equal. The theorem is the reason a question that supplies "twenty learners with mean $54$ and thirty learners with mean $64$" cannot be answered with $59$. It also gives the standard trick for a missing group size: with two groups, the combined mean determines the ratio of the sizes by linear interpolation between the two means.

### 2.5 The chain of means

For positive values the three classical means satisfy

$$
H \le G \le \bar{x},
$$

with equality throughout only when all the values are equal. The gap between the arithmetic and geometric means grows with the dispersion of the values, which is why the chain doubles as a crude measure of relative spread. The inequality is strict as soon as two values differ, so a computation that returns $G = \bar{x}$ for unequal data is wrong.

### 2.6 The optimality of the median and of the mean

The mean minimises the sum of squared deviations about a point, and the median minimises the sum of absolute deviations about a point.

$$
\sum_{i=1}^{n}\left(x_i - \bar{x}\right)^{2} \le \sum_{i=1}^{n}\left(x_i - c\right)^{2}, \qquad \sum_{i=1}^{n}\left| x_i - m \right| \le \sum_{i=1}^{n}\left| x_i - c \right|
$$

The two statements explain the whole contrast between the measures. A squared criterion punishes a single large deviation severely, so the mean is dragged towards outliers; an absolute criterion punishes it in proportion, so the median ignores how far away the outliers are. Neither is more correct; they answer different questions about what "best" means.

### 2.7 The bounds on the mode factor and on the grouping error

The mode interpolation factor lies strictly between zero and one whenever the modal class is a genuine maximum, so the interpolated mode lies inside the modal class. Separately, the grouped mean differs from the true mean by at most half a class width.

$$
0 < \frac{f_m - f_1}{2f_m - f_1 - f_2} < 1, \qquad \left| \bar{x} - \bar{x}_g \right| \le \frac{h}{2}
$$

The first bound is a check on a single answer. The second is a statement about the method: it says that a grouped mean is reliable to within half a class width, so classes of width ten give a mean reliable to about five units, which is why grouped means are conventionally reported to one decimal place and no more.

### 2.8 The empirical relation and its limits

The relation

$$
\text{mode} \approx 3\,\text{median} - 2\,\text{mean}
$$

holds closely for moderately skewed unimodal distributions and fails for bimodal ones, for heavily skewed ones and for distributions with very few observations. Its correct use in an examination is either to estimate the third average when two are given and the distribution is described as moderately skewed, or to test three computed values for consistency. It must not be used to replace a required calculation, because the interpolation formula is what the question is testing.

### 2.9 The quantile formula is one formula

The identity

$$
Q(p) = L + \left(\frac{pn - F}{f}\right) c
$$

returns the median at $p = 1/2$, the quartiles at $p = 1/4$ and $p = 3/4$, the $i$-th decile at $p = i/10$ and the $k$-th percentile at $p = k/100$. Because the expression is linear in $p$ within a class, two quantiles lying in the same class can be obtained one from the other without a fresh interpolation, and the spacing between successive quantiles in the same class is proportional to the spacing of their positions. This is the fastest route through the common question that asks for three or four quantiles from one table.

### 2.10 The effect of a single observation

Replacing $x_j$ by $x_j + \delta$ changes the mean by $\delta/n$ and leaves the median unchanged unless the change crosses the middle of the ordered list. For twenty observations a single change of $54$ moves the mean by $2.7$ and leaves the median untouched. The same identity is the whole content of the "corrected mean" question type, and it is worth memorising as a sentence rather than as a formula: the mean moves by the change divided by the number of observations.

## 3. Formal Proofs, Derivations, and Methods

### 3.1 The question-pattern map

| Pattern | What is given | The opening move | Typical marks |
|---|---|---|---|
| Raw list | twenty to fifty observations | sort, then count | $6$ to $10$ |
| Grouped mean | a table and an assumed mean | one eight-column working table | $9$ to $15$ |
| Quantiles | a grouped table | one cumulative column | $8$ to $12$ |
| Missing frequency | a table with blanks and a mean, median or total | one linear equation per unknown | $5$ to $8$ |
| Combined groups | two or three groups with means and sizes | convert means into totals | $4$ to $6$ |
| Rates and growth | speeds, prices per unit, growth factors | decide which mean applies | $4$ to $6$ |
| Interpretation | computed averages or a stated scale | name the scale and the shape | $2$ to $6$ |

### 3.2 Proof of the coding theorem

Step 1. Let $y_i = a + b x_i$ and sum over all observations.

$$
\sum_{i=1}^{n} y_i = \sum_{i=1}^{n}\left(a + b x_i\right) = na + b\sum_{i=1}^{n} x_i
$$

Step 2. Divide by $n$ and substitute the definition of $\bar{x}$.

$$
\bar{y} = a + b \cdot \frac{1}{n}\sum_{i=1}^{n} x_i = a + b\bar{x}
$$

Step 3. Specialise to the assumed-mean method by taking $a = -A$ and $b = 1$, which gives $\bar{x} - A = \overline{(x - A)}$ and hence $\bar{x} = A + \bar{d}$.

Step 4. Specialise to the coding method by taking $a = -A/c$ and $b = 1/c$, which gives $\bar{u} = (\bar{x} - A)/c$ and hence $\bar{x} = A + c\bar{u}$.

Step 5. Specialise to a change of units by taking $b = 1/1000$, which shows that a mean in shillings converts to a mean in thousands of shillings by division alone. The same steps with $b$ replaced by its reciprocal prove that the median and the mode convert in the same way, provided $b$ is positive.

### 3.3 Derivation of the quantile formula

Step 1. Let $p$ be the required proportion and let class $j$ be the first class whose cumulative frequency reaches $pn$, so that $F < pn \le F + f$, where $F$ is the cumulative frequency below the class.

Step 2. The number of observations still required inside the class is $pn - F$, and the class contains $f$ observations spread over a width $c$.

Step 3. Assume the observations are uniformly spread within the class, so that the fraction of the width needed is the same as the fraction of the frequency needed.

$$
\frac{x - L}{c} = \frac{pn - F}{f}
$$

Step 4. Solve for $x$.

$$
x = L + \left(\frac{pn - F}{f}\right) c
$$

Step 5. Substitute the five named positions to obtain the median, the quartiles, the deciles and the percentiles. The median corresponds to $p = 1/2$ and therefore to the position $n/2$; the lower quartile corresponds to $p = 1/4$ and the position $n/4$; the upper quartile corresponds to $p = 3/4$ and the position $3n/4$.

### 3.4 Derivation of the mode formula

Step 1. Inside the modal class the frequency rises from $f_1$ at the lower boundary to $f_m$ at the peak and falls to $f_2$ at the upper boundary. Model the rise and the fall as straight lines.

Step 2. Let $x$ be the distance from the lower boundary to the peak. The gradient on the left is $(f_m - f_1)/x$ and the gradient on the right, taken with its sign reversed, is $(f_m - f_2)/(c - x)$.

Step 3. Equate the two magnitudes, which makes the peak a single apex.

$$
\frac{f_m - f_1}{x} = \frac{f_m - f_2}{c - x}
$$

Step 4. Cross-multiply and solve.

$$
\left(f_m - f_1\right)\left(c - x\right) = \left(f_m - f_2\right) x \implies x = \frac{f_m - f_1}{2f_m - f_1 - f_2} c
$$

Step 5. Add the distance to the lower boundary. The denominator is positive because $f_m$ exceeds both neighbours in a genuine modal class, so the factor is positive, and it is less than one because $f_m - f_1$ is less than the denominator.

### 3.5 Proof of the combined-mean theorem

Step 1. Write the total of group $j$ as $T_j = n_j \bar{x}_j$, which follows from the definition of the group mean.

Step 2. The total of the combined sample is the sum of the group totals, and its size is the sum of the group sizes.

$$
\bar{x} = \frac{\sum_{j=1}^{g} T_j}{\sum_{j=1}^{g} n_j} = \frac{\sum_{j=1}^{g} n_j \bar{x}_j}{\sum_{j=1}^{g} n_j}
$$

Step 3. Bound the result between the extreme group means. Since each $\bar{x}_j$ lies between $m$ and $M$, so does the weighted average, because the weights are positive and sum to the denominator.

Step 4. Set all sizes equal to see that the unweighted average of the means is correct only in that special case. When the sizes differ, the error of the unweighted average is the covariance between the group means and the group sizes, divided by the mean size.

### 3.6 Proof of the chain of means

Step 1. Prove the two-value case of the arithmetic-geometric inequality from a perfect square.

$$
\left(\sqrt{a} - \sqrt{b}\right)^{2} \ge 0 \implies \frac{a + b}{2} \ge \sqrt{ab}
$$

Step 2. Extend to $n$ values by the doubling and backward steps: the inequality for $n$ values implies it for $2n$ by applying it inside two blocks of $n$ and then to the two block means, and it implies the case $n - 1$ by adjoining one extra value equal to the arithmetic mean of the $n - 1$ values. Every integer is reached from the base case of two.

Step 3. Obtain the second inequality by applying the first to the reciprocals.

$$
\frac{1}{n}\sum_{i=1}^{n}\frac{1}{x_i} \ge \left(\prod_{i=1}^{n}\frac{1}{x_i}\right)^{1/n} = \frac{1}{G} \implies H \le G
$$

Step 4. Combine the two inequalities and note that equality in either requires all the values to coincide, so a strict chain is the expected outcome for any genuine data set.

### 3.7 Method: the eight-column working table

1. List the classes in the first column and the frequencies in the second.
2. Compute the class marks from the boundaries and place them in the third column.
3. Form the products $f_i x_i$ and add them, which gives the direct-method total.
4. Choose $A$ as one of the class marks and compute $d_i = x_i - A$ in a fourth column.
5. Form $f_i d_i$ and add, which gives the assumed-mean total.
6. Divide each deviation by the common width $c$ to obtain $u_i$, form $f_i u_i$ and add, which gives the coding total.
7. Confirm that the frequencies sum to $n$ and that the three derived means agree.
8. Write the three formulas with their substitutions in full, since the method marks are attached to the formulas and not to the final number.

### 3.8 Method: the quantile ladder from one cumulative column

1. Build the cumulative column once and confirm that its last entry equals $n$.
2. For each required quantile, compute the position $pn$ and write it beside the table.
3. Identify the class in which the cumulative frequency first reaches that position, and record $L$, $F$, $f$ and $c$ for that class.
4. Substitute into the single quantile formula and evaluate, keeping at least four significant figures until the final rounding.
5. Check that each answer lies inside its own class and that the answers increase with $p$.
6. Where several quantiles fall in the same class, interpolate between them by proportion rather than repeating the whole calculation.

### 3.9 Method: missing-frequency algebra

1. Insert a letter for each unknown frequency and state the unknowns in a line.
2. Write the total frequency as an expression in the unknowns and equate it to any stated total.
3. Write the grand total of the products as an expression in the unknowns, using the class marks.
4. Impose the stated mean by multiplying it by the total frequency.
5. Solve the linear system, and reject any solution that is negative or non-integral when the frequencies must be counts.
6. Verify by recomputing the mean from the recovered table, and verify any stated median or mode as well.
7. When the median supplies the second equation, first confirm which class the stated median lies in, since that identification converts the median into a statement about the cumulative frequencies.

### 3.10 Method: repairing a mean

1. Reconstruct the total implied by the reported mean, multiplying it by the number of observations.
2. Compute the difference between the true value and the recorded value.
3. Add the difference to the implied total, with its sign.
4. Divide the repaired total by the number of observations.
5. State the direction of the change in words, since a correction that raises the total must raise the mean.

### 3.11 Method: rates and growth factors

1. Decide what is held constant across the parts. If the distance, the expenditure or the product is fixed, the harmonic or geometric mean applies; if the time or the number of items is fixed, the arithmetic mean applies.
2. For a speed or a price per unit with fixed numerator, take reciprocals, average them, and invert.
3. For successive growth, convert each percentage change into a factor such as $1.15$, multiply the factors, and take the $n$-th root.
4. Report the result in the same units as the question, converting a factor back into a percentage change by subtracting one.
5. Check the ordering $H \le G \le \bar{x}$ when more than one mean has been computed.

### 3.12 The layout that earns full marks

Every mean should be written as a formula, then as a substitution, then as a value. Every quantile should be preceded by a sentence naming the class and the position. Every interpretation should name the measure, state its value with units, and say what it means for a reader of the data. The three sentences below are worth memorising as templates.

$$
\bar{x} = \frac{\sum f_i x_i}{n} = \frac{2420}{50} = 48.4
$$

$$
Q(0.5) = L + \left(\frac{\frac{n}{2} - F}{f}\right) c = 40 + \left(\frac{25 - 15}{14}\right) 10 = 47.14
$$

$$
\text{Mode} = L + \left(\frac{f_m - f_1}{2f_m - f_1 - f_2}\right) c = 40 + \left(\frac{14 - 10}{28 - 10 - 10}\right) 10 = 45
$$

## 4. Representative Worked Examples and Solutions

### 4.1 Model solution A: the standard twelve-mark mean question

The marks of $50$ learners are grouped as follows.

| Class | $20\text{–}30$ | $30\text{–}40$ | $40\text{–}50$ | $50\text{–}60$ | $60\text{–}70$ | $70\text{–}80$ |
|---|---|---|---|---|---|---|
| Frequency | $5$ | $10$ | $14$ | $10$ | $6$ | $5$ |

(a) Compute the mean by the direct method, by the assumed-mean method with $A = 45$, and by the coding method.

(b) Compute the median, the lower quartile and the upper quartile.

(c) Compute the mode and comment on the shape of the distribution.

### 4.2 Solution A: one table, six answers

Step 1. The limits differ by one between consecutive classes, so the half-gap is $0.5$ and the boundaries of the first class are $19.5$ and $29.5$. The marks are $25$, $35$, $45$, $55$, $65$ and $75$, spaced by $c = 10$.

Marking point M1: the boundary offset must be derived from the gap between the limits, and the common width must be identified before any coding is attempted.

Step 2. Build the working table.

| Class | $f$ | $x$ | $f x$ | $d$ | $f d$ | $u$ | $f u$ |
|---|---|---|---|---|---|---|---|
| $20\text{–}30$ | $5$ | $25$ | $125$ | $-20$ | $-100$ | $-2$ | $-10$ |
| $30\text{–}40$ | $10$ | $35$ | $350$ | $-10$ | $-100$ | $-1$ | $-10$ |
| $40\text{–}50$ | $14$ | $45$ | $630$ | $0$ | $0$ | $0$ | $0$ |
| $50\text{–}60$ | $10$ | $55$ | $550$ | $10$ | $100$ | $1$ | $10$ |
| $60\text{–}70$ | $6$ | $65$ | $390$ | $20$ | $120$ | $2$ | $12$ |
| $70\text{–}80$ | $5$ | $75$ | $375$ | $30$ | $150$ | $3$ | $15$ |
| Total | $50$ | | $2420$ | | $170$ | | $17$ |

Marking point M2: the frequency column must be shown to sum to $50$, and each derived column is worth a mark only if it is complete.

Step 3. Direct method.

$$
\bar{x} = \frac{2420}{50} = 48.4
$$

Step 4. Assumed-mean method with $A = 45$ and $d_i = x_i - 45$.

$$
\bar{x} = 45 + \frac{170}{50} = 45 + 3.4 = 48.4
$$

Step 5. Coding method with $u_i = (x_i - 45)/10$.

$$
\bar{x} = 45 + 10\left(\frac{17}{50}\right) = 45 + 3.4 = 48.4
$$

Marking point M3: the three answers must be identical; a candidate who obtains three different values has made an arithmetic error and should re-add the columns rather than discard two of the answers.

Step 6. Cumulative frequencies are $5$, $15$, $29$, $39$, $45$ and $50$. The median position is $n/2 = 25$, first reached in the class $40\text{–}50$.

$$
\text{Median} = 40 + \left(\frac{25 - 15}{14}\right) 10 = 40 + 7.14 = 47.14
$$

Step 7. The lower quartile position is $n/4 = 12.5$, first reached in the class $30\text{–}40$.

$$
Q_1 = 30 + \left(\frac{12.5 - 5}{10}\right) 10 = 30 + 7.5 = 37.5
$$

Step 8. The upper quartile position is $3n/4 = 37.5$, first reached in the class $50\text{–}60$.

$$
Q_3 = 50 + \left(\frac{37.5 - 29}{10}\right) 10 = 50 + 8.5 = 58.5
$$

Marking point M4: each quantile earns a mark for the position, a mark for the correct class and its four parameters, and a mark for the substitution. An answer that gives only $47.14$ has left two thirds of the available marks untouched.

Step 9. The modal class is $40\text{–}50$ with $f_m = 14$, and the neighbouring frequencies are $f_1 = 10$ and $f_2 = 10$.

$$
\text{Mode} = 40 + \left(\frac{14 - 10}{28 - 10 - 10}\right) 10 = 40 + \frac{4}{8} \times 10 = 45
$$

Step 10. Comment on the shape. The mean exceeds the median by $1.26$ and the median exceeds the mode by $2.14$, so the distribution is positively skewed, with a tail of low marks pulling the mode below the median and the mean above it. The empirical relation gives $3(47.14) - 2(48.4) = 44.62$, which is within $0.4$ of the interpolated mode of $45$ and therefore supports the same conclusion.

Marking point M5: the comment earns its mark only if it names a direction and a reason; "the distribution is roughly symmetric" would be wrong here, because the three averages are ordered.

### 4.3 Model solution B: recovering missing frequencies

(a) A distribution has classes $0\text{–}20$, $20\text{–}40$, $40\text{–}60$, $60\text{–}80$ and $80\text{–}100$ with frequencies $8$, $12$, $f$, $10$ and $6$. Its mean is $47$. Find $f$.

(b) A distribution has classes $10\text{–}30$, $30\text{–}50$, $50\text{–}70$ and $70\text{–}90$ with frequencies $6$, $a$, $b$ and $8$. It contains $40$ observations and its mean is $50$. Find $a$ and $b$.

### 4.4 Solution B: one equation per unknown

Step 1. For part (a), write the total frequency and the grand total of the products, using the class marks $10$, $30$, $50$, $70$ and $90$.

$$
n = 8 + 12 + f + 10 + 6 = 36 + f
$$

$$
\sum f_i x_i = 80 + 360 + 50f + 700 + 540 = 1680 + 50f
$$

Step 2. Impose the stated mean and clear the fraction.

$$
\frac{1680 + 50f}{36 + f} = 47 \implies 1680 + 50f = 1692 + 47f
$$

Step 3. Solve for the unknown.

$$
3f = 12 \implies f = 4
$$

Marking point M6: the equation must be formed with $n$ as the denominator; a candidate who divides by $36$ forgets that the unknown class contributes observations.

Step 4. Verify part (a). The total frequency is $40$ and the grand total is $1680 + 200 = 1880$, so the mean is $1880/40 = 47$, as stated.

Step 5. For part (b), the stated total gives the first equation.

$$
6 + a + b + 8 = 40 \implies a + b = 26
$$

Step 6. With class marks $20$, $40$, $60$ and $80$, the grand total is

$$
120 + 40a + 60b + 640 = 760 + 40a + 60b
$$

Step 7. Impose the stated mean of $50$ over $40$ observations, which gives a grand total of $2000$.

$$
760 + 40a + 60b = 2000 \implies 40a + 60b = 1240 \implies 2a + 3b = 62
$$

Step 8. Substitute $a = 26 - b$ and solve.

$$
2\left(26 - b\right) + 3b = 62 \implies 52 + b = 62 \implies b = 10, \qquad a = 16
$$

Marking point M7: the second equation must be simplified before substitution, and both unknowns must be reported with their verification.

Step 9. Verify part (b). The frequencies are $6$, $16$, $10$ and $8$, totalling $40$, and the grand total is $120 + 640 + 600 + 640 = 2000$, whose mean is $50$.

### 4.5 Model solution C: rates, growth and an unknown weight

(a) A courier covers the first half of a route at $30$ kilometres per hour and the second half at $20$. Find the average speed for the whole route.

(b) A price triples over four years. Find the equivalent constant annual growth factor and the annual percentage growth.

(c) The weighted geometric mean of $2$, $8$ and $32$ with weights $1$, $3$ and $w$ is $16$. Find $w$.

### 4.6 Solution C: choose the mean before computing it

Step 1. For part (a), the two halves are equal distances, so the total time is the sum of the two times and the average speed is total distance over total time. Take each half to be $60$ kilometres.

$$
\frac{120}{\frac{60}{30} + \frac{60}{20}} = \frac{120}{2 + 3} = 24
$$

Step 2. Obtain the same value from the harmonic mean, which does not require a chosen distance.

$$
H = \frac{2}{\frac{1}{30} + \frac{1}{20}} = \frac{2}{\frac{5}{60}} = \frac{120}{5} = 24
$$

Marking point M8: the answer $25$, obtained by averaging $30$ and $20$ arithmetically, earns no marks, because equal distances are not equal times.

Step 3. For part (b), the growth over four years is a factor of $3$, so the constant annual factor is the fourth root.

$$
G = 3^{1/4} \approx 1.3161
$$

Step 4. Convert the factor into a percentage change.

$$
1.3161 - 1 = 0.3161 \approx 31.61\%
$$

Marking point M9: the factor and the percentage must both be reported, and the percentage must be obtained by subtracting one rather than by multiplying by a hundred alone.

Step 5. For part (c), write each value as a power of two so that the products and roots collapse.

$$
2^{1} \times 8^{3} \times 32^{w} = 2^{1} \times 2^{9} \times 2^{5w} = 2^{10 + 5w}
$$

Step 6. The total weight is $4 + w$, so the weighted geometric mean is the corresponding root.

$$
G = 2^{\frac{10 + 5w}{4 + w}} = 16 = 2^{4}
$$

Step 7. Equate the exponents and solve.

$$
\frac{10 + 5w}{4 + w} = 4 \implies 10 + 5w = 16 + 4w \implies w = 6
$$

Marking point M10: the denominator of the exponent is the total weight, not the number of values, and this is the point on which the question turns.

Step 8. Verify part (c). With weights $1$, $3$ and $6$ the total weight is $10$ and the product is $2^{1} \times 2^{9} \times 2^{30} = 2^{40}$, whose tenth root is $2^{4} = 16$.

### 4.7 Model solution D: combining, repairing and completing a mean

(a) A class of $25$ learners has a mean mark of $62$ and a second class of $15$ learners has a mean mark of $70$. Find the mean of the two classes together.

(b) The mean of $40$ readings was reported as $65$, but the value $82$ had been entered as $28$. Find the corrected mean.

(c) The mean of nine observations is $12$, and the mean of the first five of them is $10$. Find the mean of the remaining four.

### 4.8 Solution D: always return to the total

Step 1. For part (a), convert both means into totals.

$$
25 \times 62 = 1550, \qquad 15 \times 70 = 1050
$$

Step 2. Add the totals and divide by the combined size.

$$
\bar{x} = \frac{1550 + 1050}{40} = \frac{2600}{40} = 65
$$

Marking point M11: the unweighted average of $62$ and $70$ is $66$, and it is wrong because the classes differ in size; the totals must appear in the working.

Step 3. For part (b), reconstruct the reported total and compute the correction.

$$
40 \times 65 = 2600, \qquad 82 - 28 = 54
$$

Step 4. The recorded value was too small, so the corrected total is larger by $54$.

$$
\bar{x}_{\text{corrected}} = \frac{2600 + 54}{40} = \frac{2654}{40} = 66.35
$$

Marking point M12: the sign of the correction must match the direction of the error; a correction that increases the total must increase the mean.

Step 5. For part (c), convert both stated means into totals.

$$
9 \times 12 = 108, \qquad 5 \times 10 = 50
$$

Step 6. Subtract to obtain the total of the remaining four observations and divide.

$$
\frac{108 - 50}{4} = \frac{58}{4} = 14.5
$$

Marking point M13: the subtraction works because the nine observations are the union of the first five and the remaining four, with no overlap and no omission.

Step 7. Interpret the three answers together. The combined mean of $65$ lies between $62$ and $70$ as it must, the correction raised the reported mean by $1.35$, and the mean of the remaining four exceeds the overall mean because the first five lie well below it.

## 5. Mathematical Extensions, Limits, and Common Errors

### 5.1 The trap table

| Trap | The wrong move | The correct move |
|---|---|---|
| Denominator | divides by the number of classes $k$ | divides by the total frequency $n$ |
| Class mark | averages the limits of a table with unequal gaps | averages the boundaries |
| Coding width | uses the limit difference when the table has gaps | uses the boundary difference, $10$ not $9$ |
| Three methods | computes each method separately and gets three answers | builds one table and reads three totals |
| Position | uses $n/2$ as the class number | uses $n/2$ as the observation position |
| Symbols | substitutes the class frequency $f$ for the cumulative frequency $F$ | keeps $F$ below the class and $f$ inside it |
| Quartile order | reports $Q_3$ below $Q_1$ | checks that quantiles increase with $p$ |
| Mode | reports the class mark of the modal class | interpolates inside the modal class |
| Mode factor | divides by $2f_m$ only | divides by $2f_m - f_1 - f_2$ |
| Combined mean | averages the group means | weights the group means by the group sizes |
| Correction | changes the mean by the whole difference | divides the difference by $n$ |
| Rates | averages speeds arithmetically | uses the harmonic mean |
| Growth | averages percentage changes arithmetically | multiplies factors and takes a root |
| Missing frequency | solves for $f$ but never verifies | substitutes back and reproduces the stated mean |
| Empirical relation | uses it instead of the formula | uses it only as a check or when two averages are given |
| Geometric mean | applies it to a list containing zero | reports that it is undefined |

### 5.2 The four traps that cost the most

The denominator trap is the most destructive because it corrupts the mean, every quantile and the missing-frequency equation at once. The cure is to write $n = \sum f_i$ on its own line at the top of the answer and to use that symbol everywhere afterwards, so the number of classes never enters the arithmetic.

The symbol trap between $f$ and $F$ produces quantiles that are usually far outside their classes, which is why the check that the answer lies inside the class is worth performing every time. In the standard median calculation, $F$ is the cumulative frequency of the classes below the median class and $f$ is the frequency of the median class itself; reversing them gives an answer that is either below the lower boundary or above the upper boundary, and the check catches it immediately.

The rate trap is conceptual rather than arithmetical. A question about a journey at two speeds over equal distances is a harmonic-mean question, and the arithmetic average of the speeds overstates the answer by an amount that grows with the difference between them. In the example of $30$ and $20$ the truth is $24$ and the error of the arithmetic average is $1$, which is more than four per cent. The discriminating question is always what is held constant across the two parts of the journey.

The missing-frequency trap is one of omission: the algebra is usually right and the verification is usually absent. Since the verification takes one line and reproduces the stated mean, it is the cheapest mark in the paper and the most frequently forgone.

### 5.3 Where each method stops working

The coding method requires a common class width. When the widths differ, the coded values are not consecutive integers, and applying the formula with a single $c$ produces a mean that is wrong by an amount that cannot be foreseen. The correct response is to use the assumed-mean method, which needs no common width, or to work directly from the class marks.

All three grouped formulas presuppose that the classes are exhaustive, mutually exclusive and of a stated width. A table with an open-ended first or last class, such as "under $10$" or "above $60$", has no class mark for that class, so the mean cannot be computed without an assumption about the missing boundary; the median and the quartiles, by contrast, can still be computed if the open class is not the one containing the required position. A question that supplies an open-ended class usually wants the median precisely because the mean is unavailable.

The empirical relation is a convenience, not a theorem. It fails for bimodal distributions, where the mode is one of two peaks and the mean lies between them, and it fails for heavily skewed distributions, where the interpolation formulas themselves are unreliable because the uniform-within-class assumption is badly violated.

The geometric and harmonic means require positive values, so neither is available for data containing zero or for measurements on scales with an arbitrary zero, such as temperature in degrees Celsius. A question that asks for the "average temperature" of several readings wants the arithmetic mean, and a question that asks for the "average growth rate" of a series of temperatures in degrees Celsius is not well posed at all.

### 5.4 Revision checklist

Work through the list until every item can be performed from memory.

- State the definitions of the arithmetic mean, the weighted mean, the geometric mean, the harmonic mean, the median, the quartiles, the deciles, the percentiles and the mode.
- Write the three formulas for the grouped mean and explain what each one saves.
- Compute a grouped mean by all three methods from a single table in under eight minutes.
- Explain why the three methods must agree, quoting the coding theorem.
- Compute the median, both quartiles, one decile and one percentile from one cumulative column.
- State the position formula for each of those quantiles.
- Compute the grouped mode and check that it lies inside the modal class.
- Derive the mode formula from two straight lines, and the quantile formula from similar triangles.
- Set up and solve a one-unknown missing-frequency equation, and a two-unknown system.
- Combine the means of two groups of unequal size, and prove the formula.
- Correct a reported mean after one observation is repaired.
- Distinguish arithmetic, geometric and harmonic means by the constraint that is held constant, and give one example of each.
- Prove that $H \le G \le \bar{x}$, and give the equality condition.
- Test three computed averages against the empirical relation.
- State the merits and demerits of each average in one sentence each.

### 5.5 Time strategy in the examination

Allow about one minute per mark, and begin every question of this topic by reading the whole question, because the parts are cumulative: the frequency table built for part (a) is used again in parts (b) and (c), and a wrong table costs the whole question.

On a grouped-mean question, spend four minutes on the working table and two on the three substitutions. Write the table with ruled columns and a totals row, and total every derived column even when only one is needed, because the totals are the cheapest check available and because a partially completed table usually means a repeated calculation later. If the arithmetic begins to drift, re-add the frequency column before anything else, since a wrong $n$ invalidates every division.

On a quantile question, write the position beside the table first, then the class, then the four parameters, then the substitution. This order means that a candidate who runs out of time still has the method marks on paper. Never leave a quantile question blank: the cumulative column and the positions alone typically carry half the marks.

On a rates or growth question, decide in the first ten seconds which mean applies and write the reason in one clause, since the reasoning often carries a mark of its own. Reserve the final three minutes of the paper for the checks of Section 1.9: the mean between the extremes, the quantiles in order, the mode inside its class, and the chain of means.

### 5.6 Consolidation

This topic is small in content and large in consequence. Two ideas generate everything: a weighted average, which covers the frequency mean, the grouped mean, the weighted mean and the combined mean; and an interpolation along a cumulative count, which covers the median, the quartiles, the deciles, the percentiles and the mode. The assumed-mean and coding methods are the weighted average applied to shifted and rescaled data, and their justification is a single line of algebra. The geometric and harmonic means are the weighted average applied to logarithms and to reciprocals, and their justification is the inequality chain. A candidate who can state which of the two ideas a question requires, write the corresponding formula, substitute with the symbols defined and check the answer against the bounds will score consistently, because the examiners of this topic reward structure far more than ingenuity.
