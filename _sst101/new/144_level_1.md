## 1. Foundational Concepts, Definitions, and Axioms

### 1.1 A crowded hall and a single number

Imagine a school hall on the morning of a sports medical check. Thirty learners have just been weighed, and every mass is written on a separate card. The cards are shuffled and handed to you as a messy pile. A teacher then asks a completely reasonable question: "How heavy is a learner in this hall?" There is no single true answer, because no two learners weigh exactly the same. Yet you can still give one honest number. You can add up all thirty masses and then share that total equally among the thirty learners. The number you obtain belongs to nobody in particular, but it is the mass that every learner would have if the total were spread out perfectly evenly.

That single number is called a measure of central tendency, and producing it is the first job of descriptive statistics. A large and unwieldy pile of observations is compressed into one value that stands in for the whole pile. Such a value is called a central value or an average value, and the whole family of such values is called the family of measures of location.

Picture the same hall a second time, but now the teacher lines every learner up from lightest to heaviest and points at the learner standing in the middle of the line. That learner's mass is a different kind of average, because it depends only on position in the queue and not on how heavy the heaviest learner happens to be. Think of the hall a third time, and count how many learners share each mass; the mass that appears on the largest number of cards is a third kind of average. All three answers are legitimate summaries of the same thirty cards, and the whole subject of this topic is the disciplined use of such summaries.

### 1.2 Three everyday questions and three different answers

Suppose five friends empty their pockets and report the money they are carrying: $4$, $7$, $7$, $9$ and $13$ dollars. Three natural questions can be asked about these five numbers, and each question has its own correct answer.

The first question is a share-out question. If the five friends pooled everything and then divided it equally, how much would each receive? They hold $4 + 7 + 7 + 9 + 13 = 40$ dollars between them, and forty divided among five people is $8$ dollars each. That answer is the arithmetic mean.

The second question is a position question. Line the five amounts up from smallest to largest and look at the amount in the middle of that line. The third amount is $7$ dollars, so the median is $7$ dollars.

The third question is a popularity question. Which amount appears on the most pockets? The amount $7$ appears twice while every other amount appears once, so the mode is $7$ dollars.

| Question asked | Name of the answer | Value for $4, 7, 7, 9, 13$ |
|---|---|---|
| What is the total shared out equally? | Arithmetic mean | $8$ |
| What is the middle amount? | Median | $7$ |
| What amount appears most often? | Mode | $7$ |

The three answers differ, and the difference is informative rather than embarrassing. The single large amount, $13$ dollars, lifts the mean above the median, because the mean is built from the actual sizes of all five amounts while the median only counts positions. A summary that notices how large the largest amount is behaves differently from a summary that only notices where the middle lies. Choosing between them is a matter of asking which question the data are supposed to answer.

### 1.3 Why one number is worth the trouble

A frequency distribution can contain thousands of entries. Reading them one at a time tells a reader nothing, and comparing two such lists by eye is hopeless. An average compresses the list into a quantity that can be written in a sentence, compared with another average, plotted against time, or used inside a later calculation. That is why every branch of applied statistics begins with measures of location: the mean of a sample feeds directly into the formulas for spread, and the means of several samples are compared when treatments are judged.

The compression has a price. Once the pile of observations has been replaced by one number, the individual observations are no longer visible, and a summary that hides an important feature can mislead. A mean wage says nothing about how unequally wages are distributed. An average rainfall says nothing about the single storm that flooded the town. The measures in this topic are therefore tools of description, not substitutes for looking at the data, and the later sections of this note explain exactly which information each measure throws away.

### 1.4 The notation used from here onward

Every formula in this topic is written in a compact notation, and the notation must be understood before the formulas can be trusted.

The symbol $x_i$ stands for the $i$-th observation of a variable $X$. If a class of five learners reports masses of $40$, $42$, $45$, $51$ and $52$ kilograms, then $x_1 = 40$, $x_2 = 42$, $x_3 = 45$, $x_4 = 51$ and $x_5 = 52$. The letter $n$ always means the number of observations, so here $n = 5$.

The capital Greek letter sigma, written $\sum$, means "add up". The small expressions above and below it say where the adding starts and where it stops, so $\sum_{i=1}^{n} x_i$ means "add every observation from the first to the last".

$$
\sum_{i=1}^{n} x_i = x_1 + x_2 + \cdots + x_n
$$

When values repeat, the data are recorded as a frequency distribution rather than as a long list. The different values are named $x_1, x_2, \dots, x_k$, and each is paired with its frequency $f_i$, which is the number of times that value occurs. The total number of observations is then the sum of the frequencies, written $n = \sum_{i=1}^{k} f_i$. The letter $k$ counts the distinct values, not the observations, and confusing the two is one of the commonest beginner errors.

A small frequency table makes the notation concrete.

| Value $x_i$ | Frequency $f_i$ | Product $f_i x_i$ |
|---|---|---|
| $1$ | $3$ | $3$ |
| $2$ | $4$ | $8$ |
| $3$ | $3$ | $9$ |
| Total | $10$ | $20$ |

Here $k = 3$ distinct values occur across $n = 10$ observations, and the total of the products is $20$, so the mean of the ten observations is $2$.

### 1.5 Two specialised averages

The mean, the median and the mode are not the whole family. Two further averages appear whenever quantities multiply or whenever rates are involved, and both are required in this course.

The geometric mean answers a multiplicative question. Imagine a price that doubles in one year and then multiplies by eight in the next. The two growth factors are $2$ and $8$. The single constant factor that would produce the same overall change over the two years is the square root of their product, which is $4$, because $2 \times 8 = 16$ and $4 \times 4 = 16$. That constant factor is the geometric mean of $2$ and $8$. It is the right summary whenever successive values are linked by multiplication rather than by addition.

The harmonic mean answers a rate question. Imagine driving a fixed distance at $40$ kilometres per hour and the same distance again at $60$ kilometres per hour. The overall average speed is neither $50$ nor anything close to the arithmetic mean, because the slower leg lasts longer and therefore counts for more of the journey. The correct average speed is driven out by the total distance divided by the total time, which turns out to be $48$ kilometres per hour. That value is the harmonic mean of the two speeds, and it is worked out in full later.

### 1.6 Vocabulary of grouped data

When the data are too numerous to list, they are summarised in classes, and the vocabulary of classes must be exact because several formulas depend on it.

A class interval is the pair of numbers naming a class, such as $5\text{--}8$. Those two numbers are the class limits, the left one being the lower class limit and the right one the upper class limit. The class boundaries are the true dividing lines between neighbouring classes, and they differ from the limits whenever the classes leave a gap. The class width is the distance from the lower boundary of a class to its upper boundary. The class mark, also called the mid-value, is the midpoint of the class and is used in place of the unknown individual observations when a mean is computed from grouped data.

The relation between limits and boundaries depends on how the classes were written down. When neighbours share an endpoint, as in the classes $5\text{--}10$, $10\text{--}15$ and $15\text{--}20$, the shared number is already the boundary, so the class $15\text{--}20$ runs from $15$ to $20$ and has width $5$. When neighbours leave a gap, as in the classes $5\text{--}8$, $9\text{--}12$ and $13\text{--}16$, the boundary lies halfway across the gap, so the class $5\text{--}8$ runs from $4.5$ to $8.5$, has width $4$, and has class mark $6.5$. Reading the boundaries correctly is not a formality: a class mark taken from the wrong pair of numbers corrupts every later average computed from the table.

| Class as written | Lower boundary | Upper boundary | Class width | Class mark |
|---|---|---|---|---|
| $5\text{--}8$ | $4.5$ | $8.5$ | $4$ | $6.5$ |
| $9\text{--}12$ | $8.5$ | $12.5$ | $4$ | $10.5$ |
| $5\text{--}10$ | $5$ | $10$ | $5$ | $7.5$ |
| $10\text{--}15$ | $10$ | $15$ | $5$ | $12.5$ |

### 1.7 Scales of measurement and the averages they allow

Not every average is meaningful for every kind of data, and the deciding factor is the scale on which the variable was measured.

Nominal data record categories that differ only in name, such as blood group or religion. There is no order and no distance, so adding the coded numbers would be nonsense; only the most common category can be reported, which means only the mode is available.

Ordinal data record categories that can be ranked, such as a satisfaction rating of poor, fair and good, but the distances between neighbouring categories are not known to be equal. Ranking allows the middle observation to be found, so the median is available, but arithmetic on the codes is not trustworthy and the mean is not.

Interval data have equal distances but an arbitrary zero, such as temperature in degrees Celsius. Differences are meaningful, so the mean and the median are both legitimate, but ratios are not: $20$ degrees is not twice as warm as $10$ degrees in any physical sense.

Ratio data have equal distances and a genuine zero, such as mass, income or time. Everything is permitted here, including ratios, so the mean, the median, the mode, the geometric mean and the harmonic mean are all available whenever their other conditions are met.

### 1.8 The foundational principles an average must satisfy

Four principles are assumed throughout the topic, and each of them rules out some careless formula.

> **Principle (Use of the data).** A measure of central tendency must be computed from the observed values themselves, so that a change in any observation that changes the total or the ordering also changes the average.

> **Principle (Same units).** A measure of central tendency must be expressed in the same units as the data, so that a mean of masses in kilograms is a mass in kilograms and not a bare number.

> **Principle (Uniqueness).** A measure of central tendency should be uniquely determined by the data, so that two people who compute it correctly obtain the same value.

> **Principle (Representativeness).** A measure of central tendency should lie inside the range of the data, so that an average of values between $4$ and $13$ cannot claim to be $20$.

A fifth principle, stability, is a matter of degree rather than of logic: a good average should not swing wildly when a single observation is altered. The mean fails this test when outliers are present, the median passes it easily, and the mode is so sensitive to the pattern of repetitions that a single new value can move it from one value to a completely different one. Section 2 states this behaviour precisely, and Section 5 explains what goes wrong when it is ignored.

## 2. Theorems, Lemmas, and Analytical Properties

### 2.1 The deviations from the mean cancel out

> **Theorem (Zero sum of deviations).** If every observation is compared with the mean and the differences are added, the total is always exactly zero, so the values above the mean balance the values below it precisely.

The five amounts $4$, $7$, $7$, $9$ and $13$ have mean $8$. The deviations are $-4$, $-1$, $-1$, $1$ and $5$, and their sum is $-4 - 1 - 1 + 1 + 5 = 0$. The same cancellation happens with a frequency table, where each deviation is counted as many times as its frequency.

$$
\sum_{i=1}^{k} f_i \left(x_i - \bar{x}\right) = 0
$$

The result is what makes the mean a balance point. It is also a free check on arithmetic: after computing a mean, subtract it from each value, weight by frequency, and confirm that the running total returns to zero.

### 2.2 The mean is the point of smallest squared error

> **Theorem (Minimum sum of squares).** Among all possible reference values, the mean makes the sum of squared deviations as small as possible.

For the five amounts, the squared deviations about the mean $8$ are $16$, $1$, $1$, $1$ and $25$, which total $44$. If the median $7$ is used as the reference instead, the squared deviations are $9$, $0$, $0$, $4$ and $36$, which total $49$. The mean therefore wins, and it wins for every data set. This property is the reason the mean, and not the median, appears inside the formulas for variance and standard deviation.

> **Theorem (Minimum sum of absolute deviations).** Among all possible reference values, the median makes the sum of absolute deviations as small as possible.

For the same five amounts the absolute deviations about $7$ are $3$, $0$, $0$, $2$ and $6$, which total $11$, while about $8$ they are $4$, $1$, $1$, $1$ and $5$, which total $12$. The two theorems explain the division of labour between the two averages: the mean is optimal when errors are penalised in proportion to their squares, and the median is optimal when errors are penalised in proportion to their size.

### 2.3 Sliding the origin leaves the mean unchanged

> **Theorem (Shift of origin).** Suppose a convenient number $A$ is subtracted from every observation and the average of those differences is added back to $A$. Then the result is the true mean, whatever value of $A$ was chosen.

Subtracting $10$ from each of the five amounts gives $-6$, $-3$, $-3$, $-1$ and $3$, whose average is $-2$. Adding this back to $10$ gives $10 - 2 = 8$, exactly the mean found directly. Subtracting $8$ instead gives deviations that average to $0$, and adding back gives $8$ again. Choosing a different starting point changes the arithmetic but never the answer, which is why the method can be used safely with a rough guess.

### 2.4 Dividing by a common width can be undone

> **Theorem (Change of scale).** If every observation is first reduced by the constant $A$ and then divided by a common positive constant $h$, the mean of the resulting small numbers can be turned back into the true mean by multiplying by $h$ and adding $A$.

Suppose five masses in grams are $158$, $163$, $168$, $173$ and $185$. Take $A = 168$ and $h = 5$. The reduced values are $-2$, $-1$, $0$, $1$ and $3$, whose average is $\frac{1}{5}$. Multiplying by $5$ gives $1$, and adding $168$ gives $169$, which agrees with the direct total of $855$ grams divided by five. The theorem only holds when the same $h$ is used for every observation, so it is safe for classes of equal width and unsafe for classes of unequal width unless each class is coded with its own width.

### 2.5 Two groups can be pooled

> **Theorem (Combined mean).** If a first group of $n_1$ observations has mean $\bar{x}_1$ and a second group of $n_2$ observations has mean $\bar{x}_2$, then the mean of all $n_1 + n_2$ observations is the weighted average of the two group means, with the group sizes as weights.

For example, a class of $20$ learners has a mean mark of $54$ and a second class of $30$ learners has a mean mark of $64$. The pooled mean is not $59$, because the larger class counts for more.

$$
\bar{x}_c = \frac{n_1 \bar{x}_1 + n_2 \bar{x}_2}{n_1 + n_2} = \frac{20 \times 54 + 30 \times 64}{50} = \frac{3000}{50} = 60
$$

The unweighted average of $54$ and $64$ would be $59$, and it is wrong because it treats twenty learners as if they were thirty.

### 2.6 The three classical means are ordered

> **Theorem (Ordering of the means).** For any set of positive values, the harmonic mean is at most the geometric mean, and the geometric mean is at most the arithmetic mean. Both inequalities become equalities only when every value in the set is identical.

The values $3$, $9$ and $27$ illustrate the ordering with room to spare. Their arithmetic mean is $13$, their geometric mean is $9$, and their harmonic mean is approximately $6.23$.

$$
H \le G \le \bar{x}
$$

The ordering is not a curious coincidence. Each mean is built to answer a different question, and the question answered by the harmonic mean deliberately gives more weight to small values, while the geometric mean sits between the two.

### 2.7 Positional measures are ordered

> **Lemma (Quartiles divide the data).** When the observations are arranged in order, the first quartile leaves one quarter of them below it, the second quartile coincides with the median and leaves one half below it, and the third quartile leaves three quarters below it.

> **Lemma (Monotonicity of quantiles).** For any data set, the first quartile is no larger than the median, and the median is no larger than the third quartile. The same ordering holds across deciles and percentiles, because each is defined by a larger fraction of the ordered data.

The second quartile is not merely close to the median; it is the median, computed by the same rule with $\frac{2n}{4}$ in place of $\frac{n}{2}$. Recognising this saves work in an examination and provides a check on any interpolation.

### 2.8 The mode may fail to exist or may exist several times

> **Lemma (Multiplicity of the mode).** A data set can have one mode, several modes, or no mode at all.

The set $2, 2, 5, 8, 8, 8$ has the single mode $8$. The set $3, 5, 6, 8, 9, 10$ has no mode, because every value occurs once. The set $12.2, 12.2, 12, 14, 16, 17, 17, 18, 20$ has two modes, $12.2$ and $17$, and is called bimodal. No other average can behave in this way, and that flexibility is both the strength and the weakness of the mode.

### 2.9 The empirical relation between the three averages

> **Result (Empirical relation).** In a moderately skewed unimodal distribution, the three averages stand in an approximately fixed order, and any one of them can be estimated from the other two.

For a distribution that leans to the right, with a few large values stretching the tail, the mean is pulled furthest in the direction of the tail, the median is pulled less, and the mode stays closest to the peak. The approximate relation that captures this pattern is that the distance from the mean to the mode is about three times the distance from the mean to the median.

$$
\text{Mode} \approx 3 \times \text{Median} - 2 \times \text{Mean}
$$

If a distribution has mean $45.6$ and median $46.2$, the estimate of the mode is $3 \times 46.2 - 2 \times 45.6 = 47.4$. The relation is an approximation for moderately skewed unimodal data, not an identity, and it can fail badly for heavily skewed or U-shaped distributions.

### 2.10 One interpolation rule serves quartiles, deciles and percentiles

> **Lemma (Common structure of interior quantiles).** Every quantile of grouped data is found by the same three ingredients: the lower boundary of the class that contains the required position, the number of observations already counted below that class, and the fraction of the class frequency still needed.

For a proportion $p$ between zero and one, the class that contains the required position is the first class whose cumulative frequency reaches or passes $pn$. Inside that class the observations are assumed to be spread evenly, so the required fraction of the class width is the shortfall divided by the class frequency.

$$
Q(p) = L + \left(\frac{pn - F}{f}\right) c
$$

Setting $p = \frac{1}{2}$ gives the median, $p = \frac{1}{4}$ and $p = \frac{3}{4}$ give the quartiles, $p = \frac{i}{10}$ gives the $i$-th decile, and $p = \frac{k}{100}$ gives the $k$-th percentile.

### 2.11 A corrected observation corrects the mean by a known amount

> **Theorem (Corrected mean).** If one observation was recorded wrongly and is later replaced by its correct value, the mean changes by the difference between the correct and the wrong value, divided by the number of observations.

A mean of $50$ observations is reported as $38.6$ because the value $83$ was typed as $38$. The correction adds $83 - 38 = 45$ to the total, so the correct mean is larger by $\frac{45}{50} = 0.9$, that is $39.5$. The whole data set does not need to be added up again, and the same idea underlies the missing-frequency formulas developed in Section 3.

## 3. Formal Proofs, Derivations, and Methods

### 3.1 Why the deviations cancel: the short proof

The cancellation stated in Section 2 is proved in three lines, and the proof is worth following because the same algebra reappears in every later derivation.

Step 1. Write each deviation as a subtraction.

$$
\sum_{i=1}^{n} \left(x_i - \bar{x}\right) = \sum_{i=1}^{n} x_i - \sum_{i=1}^{n} \bar{x}
$$

Step 2. Replace the second sum by the number of observations multiplied by the mean, since a constant added $n$ times is $n$ times itself.

$$
\sum_{i=1}^{n} \left(x_i - \bar{x}\right) = \sum_{i=1}^{n} x_i - n\bar{x}
$$

Step 3. Use the definition $n\bar{x} = \sum_{i=1}^{n} x_i$ to see that the two terms are identical.

$$
\sum_{i=1}^{n} \left(x_i - \bar{x}\right) = 0
$$

The frequency version is identical in substance: each deviation is multiplied by its frequency, and the weighted total is again zero.

### 3.2 Why coding can be undone: the short proof

Step 1. Start from the coding substitution, in which every observation is written as the assumed mean plus a multiple of the common width.

$$
x_i = A + h u_i
$$

Step 2. Add over all observations and divide by $n$.

$$
\bar{x} = \frac{1}{n}\sum_{i=1}^{n}\left(A + h u_i\right) = A + h \cdot \frac{1}{n}\sum_{i=1}^{n} u_i
$$

Step 3. Name the average of the coded values $\bar{u}$, so that the mean is recovered by one multiplication and one addition.

$$
\bar{x} = A + h\bar{u}
$$

Nothing in the derivation requires $A$ to be a data value, and nothing requires $h$ to be an integer. The only requirement is that the same $A$ and the same $h$ are used for every observation.

### 3.3 Why the median interpolation formula works

Step 1. Suppose the median class begins at the boundary $L$, has frequency $f$ and width $c$, and suppose $F$ observations have already been counted in the classes below it.

Step 2. The middle observation is the one in position $\frac{n}{2}$, so the number of observations still needed inside the median class is $\frac{n}{2} - F$.

Step 3. Assume those observations are spread evenly across the class, so that the fraction of the class occupied by them is $\frac{\frac{n}{2} - F}{f}$.

Step 4. Convert that fraction into a distance by multiplying by the width $c$, and add the distance to the lower boundary.

$$
\text{Median} = L + \left(\frac{\frac{n}{2} - F}{f}\right) c
$$

Replacing $\frac{n}{2}$ by $\frac{n}{4}$, $\frac{3n}{4}$, $\frac{in}{10}$ or $\frac{kn}{100}$ produces the first quartile, the third quartile, the $i$-th decile and the $k$-th percentile respectively.

### 3.4 Method: the direct mean

1. Count the observations, or add the frequencies, to obtain $n$.
2. Form the product of each value with its frequency, or the value itself when there is no frequency column.
3. Add all the products to obtain the grand total.
4. Divide the grand total by $n$.
5. For grouped data, first replace each class by its class mark, and use that mark as the value.

$$
\bar{x} = \frac{\sum_{i=1}^{k} f_i x_i}{\sum_{i=1}^{k} f_i}
$$

### 3.5 Method: the assumed mean

1. Choose an assumed mean $A$ near the middle of the values, ideally one of the values themselves.
2. Subtract $A$ from every value, or from every class mark, to obtain the deviations $d_i$.
3. Multiply each deviation by its frequency and add the products.
4. Divide that total by $n$ to obtain the average deviation.
5. Add the average deviation to $A$.

$$
\bar{x} = A + \frac{\sum_{i=1}^{k} f_i d_i}{\sum_{i=1}^{k} f_i}
$$

### 3.6 Method: the coding method

1. Confirm that all classes have the same width $h$; if they do not, the method cannot be applied to the classes as they stand.
2. Choose an assumed mean $A$ that is a class mark.
3. Divide each deviation by $h$ to obtain the coded values $u_i$, which should be small whole numbers.
4. Multiply each coded value by its frequency, add, and divide by $n$ to obtain $\bar{u}$.
5. Multiply $\bar{u}$ by $h$ and add $A$.

$$
\bar{x} = A + h\bar{u}
$$

### 3.7 Method: the weighted mean

1. Identify the weight $w_i$ attached to each value; a weight may be a frequency, a number of credit units, an amount of money or a duration.
2. Multiply each value by its weight.
3. Add the products and add the weights separately.
4. Divide the weighted total by the total weight.

$$
\bar{x}_w = \frac{\sum_{i=1}^{k} w_i x_i}{\sum_{i=1}^{k} w_i}
$$

The ordinary mean is the special case in which every weight equals one. The frequency mean is the special case in which the weights are counts.

### 3.8 Method: the geometric mean

1. Check that every value is positive; the geometric mean is undefined when a zero or a negative value is present.
2. Multiply the values together, raising each to the power of its frequency when frequencies are given.
3. Take the $n$-th root, where $n$ is the total frequency.
4. When the numbers are large, take logarithms first, average them, and convert back by raising ten to that average.

$$
G = \sqrt[n]{x_1^{f_1} x_2^{f_2} \cdots x_k^{f_k}}
$$

### 3.9 Method: the harmonic mean

1. Check that every value is positive.
2. Take the reciprocal of every value.
3. Average the reciprocals, weighting by frequency when frequencies are given.
4. Take the reciprocal of that average.

$$
H = \frac{\sum_{i=1}^{k} f_i}{\sum_{i=1}^{k} \frac{f_i}{x_i}}
$$

### 3.10 Method: the median of ungrouped and grouped data

1. Arrange the observations in ascending order, which is essential and is the step most often skipped.
2. If $n$ is odd, read off the value in position $\frac{n+1}{2}$.
3. If $n$ is even, average the values in positions $\frac{n}{2}$ and $\frac{n}{2} + 1$.
4. For grouped data, build a cumulative frequency column.
5. Find the class in which the cumulative frequency first reaches or passes $\frac{n}{2}$; that is the median class.
6. Apply the interpolation formula with that class boundary, the frequency below it, the class frequency and the class width.

### 3.11 Method: the mode

1. For ungrouped data, count the repetitions of each value and report the value with the largest count.
2. For grouped data, find the class with the largest frequency; that is the modal class.
3. Record the frequency of the class before it and the frequency of the class after it.
4. Apply the interpolation formula, using the lower boundary and the class width.

$$
\text{Mode} = L + \left(\frac{f_m - f_1}{2f_m - f_1 - f_2}\right) c
$$

### 3.12 Method: quartiles, deciles and percentiles

1. Build the cumulative frequency column once and reuse it for every quantile.
2. Compute the required position: $\frac{n}{4}$ and $\frac{3n}{4}$ for the quartiles, $\frac{in}{10}$ for the $i$-th decile, and $\frac{kn}{100}$ for the $k$-th percentile.
3. Identify the class whose cumulative frequency first reaches or passes that position.
4. Substitute the boundary, the frequency below, the class frequency and the class width into the common interpolation formula.

### 3.13 Method: combined and corrected means

1. For two groups, multiply each group mean by its group size.
2. Add the two products and divide by the total size.
3. For a corrected observation, find the difference between the correct value and the wrong value.
4. Divide that difference by $n$ and add the result to the old mean.

$$
\bar{x}_c = \frac{n_1 \bar{x}_1 + n_2 \bar{x}_2}{n_1 + n_2}, \qquad \bar{x}_{\text{new}} = \bar{x}_{\text{old}} + \frac{x_{\text{correct}} - x_{\text{wrong}}}{n}
$$

### 3.14 Method: recovering a missing frequency

1. Write the unknown frequency as a letter, say $f$.
2. Express the total frequency as a formula in $f$.
3. Express the grand total of the products as a formula in $f$.
4. Set the ratio of the grand total to the total frequency equal to the stated mean.
5. Solve the resulting linear equation for $f$, then confirm that the recovered value makes the frequencies add up to the stated total.
6. When two frequencies are missing, use the stated total frequency as a second equation and solve the pair of simultaneous equations.

### 3.15 A checking routine that catches most slips

1. Confirm that the frequencies add up to the stated number of observations.
2. Confirm that the class marks increase by exactly one class width when the classes are of equal width.
3. Confirm that the median and the mode both lie inside their own classes.
4. Confirm that the mean by the direct method equals the mean by the coding method.
5. Confirm that the harmonic mean is no larger than the geometric mean and that the geometric mean is no larger than the arithmetic mean.
6. Confirm that the average lies between the smallest and the largest observation.

## 4. Representative Worked Examples and Solutions

### 4.1 Problem: the mean of a short list

Five learners report the number of books they read during a holiday: $3$, $6$, $9$, $13$ and $15$. Find the arithmetic mean.

### 4.2 Solution: add, then share

Step 1. Add the five values to obtain the total.

$$
3 + 6 + 9 + 13 + 15 = 46
$$

Step 2. Divide the total by the number of values.

$$
\bar{x} = \frac{46}{5} = 9.2
$$

Step 3. Check against the data. The value $9.2$ lies between $3$ and $15$, as an average must, and it lies slightly below the middle value $9$ only because the value $15$ is far above the rest.

### 4.3 Problem: the mean of a frequency table

Forty learners wrote a test out of $50$. The marks and the numbers of learners obtaining them are given in the table. Find the mean mark.

| Mark $x_i$ | $22$ | $24$ | $25$ | $27$ | $30$ | $31$ | $34$ | $36$ |
|---|---|---|---|---|---|---|---|---|
| Number $f_i$ | $2$ | $5$ | $5$ | $6$ | $7$ | $4$ | $5$ | $6$ |

### 4.4 Solution: weight each mark by its frequency

Step 1. Multiply each mark by the number of learners who obtained it.

$$
\begin{aligned}
22 \times 2 &= 44, & 24 \times 5 &= 120, & 25 \times 5 &= 125, & 27 \times 6 &= 162, \\
30 \times 7 &= 210, & 31 \times 4 &= 124, & 34 \times 5 &= 170, & 36 \times 6 &= 216
\end{aligned}
$$

Step 2. Add the products to obtain the total of all marks scored.

$$
44 + 120 + 125 + 162 + 210 + 124 + 170 + 216 = 1171
$$

Step 3. Add the frequencies to obtain the number of learners, and check that it matches the stated total.

$$
2 + 5 + 5 + 6 + 7 + 4 + 5 + 6 = 40
$$

Step 4. Divide the total of the marks by the number of learners.

$$
\bar{x} = \frac{1171}{40} = 29.275
$$

The mean mark is $29.275$, which is about $29.3$ to one decimal place.

### 4.5 Problem: one grouped mean by three methods

The table gives the classes and frequencies of a grouped distribution. Compute the mean by the direct method, by the assumed mean method with $A = 22.5$, and by the coding method with $h = 4$.

| Class | $5\text{--}8$ | $9\text{--}12$ | $13\text{--}16$ | $17\text{--}20$ | $21\text{--}24$ | $25\text{--}28$ | $29\text{--}32$ | $33\text{--}36$ | $37\text{--}40$ | $41\text{--}44$ |
|---|---|---|---|---|---|---|---|---|---|---|
| Frequency | $3$ | $9$ | $11$ | $10$ | $20$ | $16$ | $15$ | $6$ | $8$ | $2$ |

### 4.6 Solution: build one working table and read three answers from it

Step 1. Find each class mark by averaging the class limits, and confirm that the marks rise by the class width $4$.

$$
6.5,\ 10.5,\ 14.5,\ 18.5,\ 22.5,\ 26.5,\ 30.5,\ 34.5,\ 38.5,\ 42.5
$$

Step 2. Build the working columns: the product $fx$, the deviation $d = x - A$, the coded value $u = \frac{d}{4}$, and the products $fd$ and $fu$.

| Class | $f$ | $x$ | $fx$ | $d$ | $u$ | $fd$ | $fu$ |
|---|---|---|---|---|---|---|---|
| $5\text{--}8$ | $3$ | $6.5$ | $19.5$ | $-16$ | $-4$ | $-48$ | $-12$ |
| $9\text{--}12$ | $9$ | $10.5$ | $94.5$ | $-12$ | $-3$ | $-108$ | $-27$ |
| $13\text{--}16$ | $11$ | $14.5$ | $159.5$ | $-8$ | $-2$ | $-88$ | $-22$ |
| $17\text{--}20$ | $10$ | $18.5$ | $185.0$ | $-4$ | $-1$ | $-40$ | $-10$ |
| $21\text{--}24$ | $20$ | $22.5$ | $450.0$ | $0$ | $0$ | $0$ | $0$ |
| $25\text{--}28$ | $16$ | $26.5$ | $424.0$ | $4$ | $1$ | $64$ | $16$ |
| $29\text{--}32$ | $15$ | $30.5$ | $457.5$ | $8$ | $2$ | $120$ | $30$ |
| $33\text{--}36$ | $6$ | $34.5$ | $207.0$ | $12$ | $3$ | $72$ | $18$ |
| $37\text{--}40$ | $8$ | $38.5$ | $308.0$ | $16$ | $4$ | $128$ | $32$ |
| $41\text{--}44$ | $2$ | $42.5$ | $85.0$ | $20$ | $5$ | $40$ | $10$ |
| Total | $100$ | | $2390.0$ | | | $140$ | $35$ |

Step 3. Apply the direct formula to the totals.

$$
\bar{x} = \frac{2390.0}{100} = 23.9
$$

Step 4. Apply the assumed mean formula to the deviation total.

$$
\bar{x} = 22.5 + \frac{140}{100} = 22.5 + 1.4 = 23.9
$$

Step 5. Apply the coding formula to the coded total.

$$
\bar{x} = 22.5 + 4 \times \frac{35}{100} = 22.5 + 1.4 = 23.9
$$

Step 6. Interpret. All three routes give $23.9$, so the arithmetic is confirmed. The coding route used only the small integers from $-4$ to $5$, which is why it is the safest of the three by hand.

### 4.7 Problem: geometric and harmonic means of the same three numbers

Find the arithmetic, geometric and harmonic means of $3$, $9$ and $27$, and arrange them in order.

### 4.8 Solution: three different share-outs of the same product and the same reciprocals

Step 1. Compute the arithmetic mean by adding and dividing.

$$
\bar{x} = \frac{3 + 9 + 27}{3} = \frac{39}{3} = 13
$$

Step 2. Compute the geometric mean as the cube root of the product.

$$
G = \sqrt[3]{3 \times 9 \times 27} = \sqrt[3]{729} = 9
$$

Step 3. Compute the harmonic mean from the reciprocals, using the common denominator $27$.

$$
H = \frac{3}{\frac{1}{3} + \frac{1}{9} + \frac{1}{27}} = \frac{3}{\frac{9}{27} + \frac{3}{27} + \frac{1}{27}} = \frac{3}{\frac{13}{27}} = \frac{81}{13} \approx 6.23
$$

Step 4. Arrange in order and note the gap.

$$
6.23 < 9 < 13
$$

The harmonic mean is the smallest because the small value $3$ dominates its reciprocals, and the arithmetic mean is the largest because the large value $27$ dominates its total.

### 4.9 Problem: median and quartiles of a grouped distribution

The marks of $49$ learners are grouped as shown. Find the median, the lower quartile and the upper quartile.

| Marks | $5\text{--}10$ | $10\text{--}15$ | $15\text{--}20$ | $20\text{--}25$ | $25\text{--}30$ | $30\text{--}35$ | $35\text{--}40$ | $40\text{--}45$ |
|---|---|---|---|---|---|---|---|---|
| Frequency | $5$ | $6$ | $15$ | $10$ | $5$ | $4$ | $2$ | $2$ |

### 4.10 Solution: one cumulative column, three positions

Step 1. Add a cumulative frequency column and confirm that the last entry equals $49$.

| Marks | Frequency $f$ | Cumulative frequency |
|---|---|---|
| $5\text{--}10$ | $5$ | $5$ |
| $10\text{--}15$ | $6$ | $11$ |
| $15\text{--}20$ | $15$ | $26$ |
| $20\text{--}25$ | $10$ | $36$ |
| $25\text{--}30$ | $5$ | $41$ |
| $30\text{--}35$ | $4$ | $45$ |
| $35\text{--}40$ | $2$ | $47$ |
| $40\text{--}45$ | $2$ | $49$ |

Step 2. Locate the median class. Half of $49$ is $24.5$, and the first cumulative frequency to reach it is $26$, so the median class is $15\text{--}20$ with lower boundary $15$, $11$ observations below it and frequency $15$.

Step 3. Interpolate for the median, using the class width $5$.

$$
\text{Median} = 15 + \left(\frac{24.5 - 11}{15}\right) 5 = 15 + \left(\frac{13.5}{15}\right) 5 = 15 + 4.5 = 19.5
$$

Step 4. Locate the lower quartile class. One quarter of $49$ is $12.25$, and the first cumulative frequency to reach it is again $26$, so the lower quartile also lies in $15\text{--}20$.

$$
Q_1 = 15 + \left(\frac{12.25 - 11}{15}\right) 5 = 15 + \frac{6.25}{15} \approx 15.42
$$

Step 5. Locate the upper quartile class. Three quarters of $49$ is $36.75$, and the first cumulative frequency to reach it is $41$, so the class is $25\text{--}30$, with $36$ observations below it and frequency $5$.

$$
Q_3 = 25 + \left(\frac{36.75 - 36}{5}\right) 5 = 25 + 0.75 = 25.75
$$

Step 6. Interpret. Half the learners scored below $19.5$, one quarter scored below $15.42$ and three quarters scored below $25.75$. The upper quartile is far above the lower one, so the marks are spread widely on the high side.

### 4.11 Problem: the mode of the same grouped distribution

Find the mode of the distribution of the previous example.

### 4.12 Solution: read the peak and interpolate towards the heavier neighbour

Step 1. Identify the modal class as the class with the largest frequency. The frequency $15$ in the class $15\text{--}20$ is the largest, so that class is modal.

Step 2. Record the neighbouring frequencies. The class before has frequency $6$ and the class after has frequency $10$.

Step 3. Substitute into the mode formula with $L = 15$, $f_m = 15$, $f_1 = 6$, $f_2 = 10$ and $c = 5$.

$$
\text{Mode} = 15 + \left(\frac{15 - 6}{2(15) - 6 - 10}\right) 5 = 15 + \left(\frac{9}{14}\right) 5 \approx 18.21
$$

Step 4. Check that the answer lies inside the modal class, which it does, and note that it lies above the class mark $17.5$ because the following class is heavier than the preceding one.

### 4.13 Problem: a missing frequency given the mean

Five classes have frequencies $6$, $9$, $f$, $8$ and $4$, where $f$ is unknown. The mean of the distribution is $34$. Find $f$.

| Class | $10\text{--}20$ | $20\text{--}30$ | $30\text{--}40$ | $40\text{--}50$ | $50\text{--}60$ |
|---|---|---|---|---|---|
| Class mark | $15$ | $25$ | $35$ | $45$ | $55$ |
| Frequency | $6$ | $9$ | $f$ | $8$ | $4$ |

### 4.14 Solution: let the algebra carry the unknown

Step 1. Write the total frequency as an expression in $f$.

$$
n = 6 + 9 + f + 8 + 4 = 27 + f
$$

Step 2. Write the grand total of the products, leaving the unknown term as $35f$.

$$
\sum f_i x_i = 90 + 225 + 35f + 360 + 220 = 895 + 35f
$$

Step 3. Set the ratio equal to the stated mean of $34$.

$$
\frac{895 + 35f}{27 + f} = 34
$$

Step 4. Multiply both sides by $27 + f$ and solve the resulting linear equation.

$$
895 + 35f = 918 + 34f
$$

$$
f = 23
$$

Step 5. Check by substitution: the total frequency is $50$ and the grand total is $895 + 805 = 1700$, so the mean is $\frac{1700}{50} = 34$, as required.

### 4.15 Problem: combining two groups and correcting a mean

A morning class of $20$ learners has a mean mark of $54$ and an afternoon class of $30$ learners has a mean mark of $64$. Separately, the mean of $50$ readings was reported as $38.6$ because the value $83$ had been recorded as $38$. Find the pooled mean of the two classes and the corrected mean of the $50$ readings.

### 4.16 Solution: work with totals, not with averages of averages

Step 1. Convert each group mean back into a group total.

$$
20 \times 54 = 1080, \qquad 30 \times 64 = 1920
$$

Step 2. Add the totals and divide by the combined size.

$$
\bar{x}_c = \frac{1080 + 1920}{50} = \frac{3000}{50} = 60
$$

Step 3. For the corrected reading, find the change in the total.

$$
83 - 38 = 45
$$

Step 4. Divide the change by the number of readings and add it to the old mean.

$$
\bar{x}_{\text{new}} = 38.6 + \frac{45}{50} = 38.6 + 0.9 = 39.5
$$

The pooled mean is $60$, not the unweighted $59$, and the corrected mean is $39.5$, not $38.6$.

### 4.17 Problem: all three averages and the empirical check

A distribution has five classes with unequal widths. Find the mean, the median and the mode, then test the empirical relation between them.

| Class | $0\text{--}10$ | $10\text{--}20$ | $20\text{--}30$ | $30\text{--}40$ | $40\text{--}60$ |
|---|---|---|---|---|---|
| Frequency | $5$ | $12$ | $20$ | $8$ | $5$ |

### 4.18 Solution: unequal widths call for careful class marks

Step 1. Compute the class marks, noticing that the last class is twice as wide as the others and therefore has the mark $50$ rather than $45$.

$$
5,\ 15,\ 25,\ 35,\ 50
$$

Step 2. Form the products and add, then divide by the total frequency of $50$.

$$
\sum f_i x_i = 25 + 180 + 500 + 280 + 250 = 1235
$$

$$
\bar{x} = \frac{1235}{50} = 24.7
$$

Step 3. Build the cumulative frequencies $5$, $17$, $37$, $45$, $50$ and locate the median class, since half of $50$ is $25$ and the first cumulative frequency to reach it is $37$.

$$
\text{Median} = 20 + \left(\frac{25 - 17}{20}\right) 10 = 20 + 4 = 24
$$

Step 4. Locate the modal class, which is $20\text{--}30$ with frequency $20$, and interpolate.

$$
\text{Mode} = 20 + \left(\frac{20 - 12}{2(20) - 12 - 8}\right) 10 = 20 + \left(\frac{8}{20}\right) 10 = 22.5
$$

Step 5. Test the empirical relation with the computed mean and median.

$$
3 \times 24 - 2 \times 24.7 = 72 - 49.4 = 22.6
$$

The estimate $22.6$ is within one tenth of the interpolated mode $22.5$, which is unusually close and confirms that the distribution is only moderately skewed.

## 5. Mathematical Extensions, Limits, and Common Errors

### 5.1 The weighted mean when the weights are not counts

The frequency mean counts how often a value occurs. A weighted mean generalises this by allowing the weight to express importance, effort or exposure rather than repetition. A learner takes four courses with credit units and grades. The grade is not simply averaged, because a course worth four units represents twice the work of a course worth two units.

| Course | Units $w_i$ | Mark $x_i$ | Product $w_i x_i$ |
|---|---|---|---|
| A | $3$ | $62$ | $186$ |
| B | $4$ | $55$ | $220$ |
| C | $2$ | $71$ | $142$ |
| D | $1$ | $80$ | $80$ |
| Total | $10$ | | $628$ |

$$
\bar{x}_w = \frac{628}{10} = 62.8
$$

The unweighted average of the four marks is $67$, so ignoring the units would have overstated the performance by more than four marks, because the weakest mark carries the largest weight.

### 5.2 The geometric mean of ratios and growth rates

Percentages cannot simply be averaged when they describe successive changes of the same quantity. A price rises by ten per cent in the first year, by twenty per cent in the second year and by fifteen per cent in the third year. The growth factors are $1.10$, $1.20$ and $1.15$, and the overall factor over three years is their product.

$$
1.10 \times 1.20 \times 1.15 = 1.518
$$

The constant yearly factor that would produce the same three-year result is the cube root of that product.

$$
G = \sqrt[3]{1.518} \approx 1.1493
$$

The average yearly growth is therefore about $14.93$ per cent, not the arithmetic average of $15$ per cent. The geometric mean is the correct summary because the changes multiply rather than add, and it is always slightly smaller than the arithmetic average of the same factors whenever they differ.

The same reasoning applies to index numbers. If three price relatives are $120$, $150$ and $80$ on a base of $100$, the typical relative is their geometric mean, which is about $112.90$, while the arithmetic average would be $116.67$ and would overstate the general level of prices.

### 5.3 The harmonic mean for rates and for averages of speeds

A rate measures one quantity per unit of another, and averaging rates requires care because the denominators differ. A driver covers the first half of a journey at $40$ kilometres per hour and the second half at $60$ kilometres per hour. Suppose each half is $60$ kilometres long. The first half takes $1.5$ hours and the second takes $1$ hour, so the whole $120$ kilometres take $2.5$ hours.

$$
\bar{v} = \frac{120}{2.5} = 48
$$

The harmonic mean of the two speeds gives the same number without any assumption about the length of the halves.

$$
H = \frac{2}{\frac{1}{40} + \frac{1}{60}} = \frac{2}{\frac{3}{120} + \frac{2}{120}} = \frac{240}{5} = 48
$$

The arithmetic mean of $40$ and $60$ is $50$, and it is wrong because the slower half lasts longer and therefore contributes more to the journey. The same structure governs average price per unit when equal amounts of money are spent: spending 100 shillings at 5 shillings per unit and 300 shillings at 10 shillings per unit buys $20 + 30 = 50$ units for 400 shillings, so the average price is 8 shillings per unit.

$$
H_w = \frac{100 + 300}{\frac{100}{5} + \frac{300}{10}} = \frac{400}{50} = 8
$$

### 5.4 What each average refuses to do

Every measure of central tendency is a compression, and each compression discards a different part of the picture.

The mean uses every observation and therefore inherits every distortion. A single salary of a million dollars added to a list of twenty ordinary salaries moves the mean by tens of thousands of dollars and leaves the median untouched. The mean of grouped data is also only an estimate, because the individual observations inside a class are replaced by the class mark; the estimate is never wrong by more than half a class width, but it is never exact either.

The median is stable against extreme values but blind to their size. Doubling the largest observation in a data set does not change the median at all, which is a virtue when the largest observation is a recording error and a defect when it is a genuine and important feature.

The mode is the only average available for categories, but it is unstable in small samples and can be absent or multiple. A single additional observation can create a new mode or destroy the old one, and the interpolated mode of grouped data changes when the class boundaries are shifted even though the observations have not changed.

The geometric mean is undefined when any value is zero or negative, because a product containing zero is zero and a product of an even number of negatives has no real root of the required order. The harmonic mean is undefined whenever a value is zero, because the reciprocal of zero does not exist. Neither can be used for temperatures on the Celsius scale, since that scale has an arbitrary zero and negative values are possible.

The interpolation formulas for the median, the mode and the quantiles all assume that the observations are spread evenly inside each class. When the true distribution is concentrated at one end of a class, the interpolated value is biased towards the middle of the class. This is not an error in the formula but a limitation of grouped data, and it disappears only when the raw observations are available.

### 5.5 Two frequencies can sometimes be recovered at once

When a table has two missing frequencies, the stated mean supplies one equation and the stated total supplies another. A distribution has classes $0\text{--}10$, $10\text{--}20$, $20\text{--}30$ and $30\text{--}40$ with frequencies $5$, $a$, $b$ and $6$, a total of $40$ observations and a mean of $20$. The total gives $a + b = 29$, and the products give $25 + 15a + 25b + 210 = 800$, so $15a + 25b = 565$. Substituting $a = 29 - b$ gives $435 + 10b = 565$, hence $b = 13$ and $a = 16$. Checking: the total frequency is $40$ and the grand total is $800$, so the mean is $20$.

When the mean is not stated but the median and the mode are, the same strategy works with the interpolation formulas used as equations. That technique is developed in the next level, and it depends entirely on reading the median and modal classes correctly from the stated values.

### 5.6 Beginner misconceptions and their corrections

The first misconception is that an average must equal one of the observations. It need not: the mean mark of $29.275$ is not a mark that anyone scored, and a mean of $2.4$ children per family is perfectly sensible even though no family has $2.4$ children.

The second misconception is that the mean, the median and the mode are always equal. They coincide only in a perfectly symmetric distribution with a single peak. In the five amounts $4$, $7$, $7$, $9$ and $13$, the values are $8$, $7$ and $7$.

The third misconception is that the median can be found without sorting. The median of the unsorted list $13$, $4$, $9$, $7$, $7$ is not the third entry as it stands; the list must be ordered first, and only then does the middle entry mean anything.

The fourth misconception is that the class mark is the average of the class boundaries when the classes were written with a gap and are treated as if they were not. Mixing the two conventions shifts every class mark, and therefore the mean, by half a unit.

The fifth misconception is that a grouped mean can be computed from the class limits. The limits are the numbers written in the table; the class mark is the midpoint between the boundaries, and it is the mark that enters the formula.

The sixth misconception is that the mode of grouped data is the modal class. The class identifies where the mode lies, and the interpolation gives its position inside the class. Reporting the class, such as $15\text{--}20$, instead of the value $18.21$ answers a different question.

The seventh misconception is that the harmonic mean is found by averaging the reciprocals and forgetting to invert the result. Averaging the reciprocals of $40$ and $60$ gives $\frac{5}{240}$, and the average speed is its reciprocal multiplied by two, namely $48$, not $0.0208$.

The eighth misconception is that percentages may be averaged arithmetically. A rise of fifty per cent followed by a fall of fifty per cent returns to three quarters of the original value, not to the original value, and no arithmetic mean of the two percentages can detect this.

The ninth misconception is that the first quartile is a quarter of the smallest value. It is the value below which one quarter of the observations lie, which is a position in the ordered data and not a fraction of a number.

The tenth misconception is that the deviations from the mean add up to something other than zero. The total is always zero, and a non-zero total after a long calculation is proof of an arithmetic slip somewhere in the working.

### 5.7 Choosing an average in one glance

| Situation | Best choice | Reason |
|---|---|---|
| Symmetric numerical data with no outliers | Arithmetic mean | Uses every observation and supports later formulas |
| Skewed data or data with outliers | Median | Unaffected by the size of extreme values |
| Categories with no natural order | Mode | The only average defined on a nominal scale |
| Successive growth factors or index relatives | Geometric mean | Multiplicative structure is preserved |
| Speeds, rates, prices per unit | Harmonic mean | Correct when the denominators are equal |
| Several groups with different sizes | Combined mean | Weights each group by its size |

The guiding question is always the same: what operation would reconstruct the whole from the parts? If the parts add, use the arithmetic mean; if they multiply, use the geometric mean; if they are rates that must be combined through their denominators, use the harmonic mean; and if only the position of the middle matters, use the median.
