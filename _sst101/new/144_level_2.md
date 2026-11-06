## 1. Foundational Concepts, Definitions, and Axioms

### 1.1 The reduction problem

A frequency table can hold thousands of entries, and a raw list of observations can hold more. Neither can be read, compared with another such list, or carried into a later calculation. The first task of descriptive statistics is therefore to replace the whole mass of observations by one number that stands in for it, and the whole family of such numbers is called the family of measures of location, or measures of central tendency.

Any candidate for the position must satisfy four requirements before it deserves the name of an average. It must be defined by a rule that can be applied to any data set of the relevant kind, so that two analysts working independently obtain the same value. It must depend on the observations rather than on the order in which they happen to be listed. It must be expressed in the same units as the observations, so that a mean mass is a mass. And it must be representative, in the sense that it lies within the range of the data and is not wildly displaced by a single unusual value. No single measure satisfies all four requirements equally well, which is why several are taught and why the choice among them is part of the subject rather than an afterthought.

Three of the measures are arithmetic in character and are built from sums: the arithmetic mean, the geometric mean and the harmonic mean. Two are positional and are built from the order of the observations: the median, together with its relatives the quartiles, deciles and percentiles, and the mode. The arithmetic family answers a share-out question, the positional family answers a ranking question, and the mode answers a popularity question. The same data set usually gives three different answers, and the differences are informative because each answer notices a different feature of the data.

### 1.2 Notation and the summation operator

The observations of a variable $X$ are written $x_1, x_2, \dots, x_n$, where $x_i$ is the $i$-th observation and $n$ is the number of observations. The capital Greek letter sigma denotes a sum, with the limits written above and below it.

$$
\sum_{i=1}^{n} x_i = x_1 + x_2 + \cdots + x_n
$$

When values repeat, the data are recorded as a frequency distribution. The $k$ distinct values are $x_1, \dots, x_k$, with frequencies $f_1, \dots, f_k$, and the total number of observations is the sum of the frequencies.

$$
n = \sum_{i=1}^{k} f_i
$$

The letters $n$ and $k$ count different things, and confusing them is a frequent error: $k$ counts the distinct values or the classes, while $n$ counts the observations. Three further symbols recur. The mean is written $\bar{x}$, an assumed mean $A$, a deviation $d_i = x_i - A$, a coded value $u_i = d_i/c$ for a common width $c$, and a class mark $m_i$ for grouped data. The $p$-th quantile of a distribution is written $Q(p)$, so that the median is $Q(0.5)$, the first quartile $Q(0.25)$ and the $k$-th percentile $Q(k/100)$.

The summation operator obeys three rules that are used constantly in the derivations that follow. A constant factor may be taken outside a sum, a sum of two terms is the sum of the two sums, and a constant summed $n$ times equals $n$ times the constant.

$$
\sum_{i=1}^{n} c x_i = c\sum_{i=1}^{n} x_i, \qquad \sum_{i=1}^{n}\left(x_i + y_i\right) = \sum_{i=1}^{n} x_i + \sum_{i=1}^{n} y_i, \qquad \sum_{i=1}^{n} c = nc
$$

### 1.3 The arithmetic mean

The arithmetic mean of $n$ observations is their total divided by their number.

$$
\bar{x} = \frac{1}{n}\sum_{i=1}^{n} x_i = \frac{x_1 + x_2 + \cdots + x_n}{n}
$$

For the five observations $3$, $6$, $9$, $13$, $15$ the total is $46$ and the mean is $46/5 = 9.2$. When the distinct values $x_1, \dots, x_k$ occur with frequencies $f_1, \dots, f_k$, each value contributes itself once for every occurrence, so the sum of all the observations is the sum of the products $f_i x_i$.

$$
\bar{x} = \frac{f_1 x_1 + f_2 x_2 + \cdots + f_k x_k}{f_1 + f_2 + \cdots + f_k} = \frac{\sum_{i=1}^{k} f_i x_i}{\sum_{i=1}^{k} f_i} = \frac{\sum_{i=1}^{k} f_i x_i}{n}
$$

For a grouped frequency distribution the individual observations are no longer available, so each class is represented by its class mark $m_i$ and the same weighted formula is applied.

$$
\bar{x} \approx \frac{\sum_{i=1}^{k} f_i m_i}{n}
$$

The symbol of approximation is deliberate. The grouped mean is exact only when the observations within each class average exactly to the class mark, which occurs when each class is symmetric about its mark; in every other case the grouped mean differs from the true mean, although the difference is bounded, as Section 2 shows.

### 1.4 The weighted mean

A weight is a number attached to each value to express how much it counts. When the weights are counts the weighted mean reduces to the frequency mean; when they are credit units, monetary amounts, durations or land areas, the weighted mean answers a different question from the unweighted one.

$$
\bar{x}_w = \frac{\sum_{i=1}^{k} w_i x_i}{\sum_{i=1}^{k} w_i}
$$

A learner takes four courses with marks $62$, $55$, $71$ and $80$ and credit units $3$, $4$, $2$ and $1$. The weighted mean is $628/10 = 62.8$, while the unweighted average of the four marks is $268/4 = 67$. The weighted value is lower because the weakest mark carries the largest weight, and the difference of more than four marks is a real difference in achievement rather than a rounding artefact.

### 1.5 The geometric mean

The geometric mean of $n$ positive values is the $n$-th root of their product.

$$
G = \sqrt[n]{x_1 x_2 \cdots x_n}
$$

When the distinct positive values $x_1, \dots, x_k$ occur with frequencies $f_1, \dots, f_k$, each value enters the product as many times as it occurs, so it enters as a power.

$$
G = \sqrt[n]{x_1^{f_1} x_2^{f_2} \cdots x_k^{f_k}}, \qquad n = \sum_{i=1}^{k} f_i
$$

Because products of many numbers overflow a calculator, the computation is carried out in logarithms, which turn the product into a weighted sum of logarithms.

$$
\log G = \frac{1}{n}\sum_{i=1}^{k} f_i \log x_i
$$

The geometric mean is the correct summary whenever successive values are linked multiplicatively: growth factors, price relatives, index numbers, and ratios of quantities measured on ratio scales. It is defined only for positive values, since a product containing zero is zero and an even root of a negative product is not real.

### 1.6 The harmonic mean

The harmonic mean of $n$ positive values is the reciprocal of the arithmetic mean of their reciprocals.

$$
H = \frac{1}{\frac{1}{n}\sum_{i=1}^{n}\frac{1}{x_i}} = \frac{n}{\sum_{i=1}^{n}\frac{1}{x_i}}
$$

With frequencies the formula weights the reciprocals.

$$
H = \frac{\sum_{i=1}^{k} f_i}{\sum_{i=1}^{k}\frac{f_i}{x_i}}
$$

The harmonic mean is the correct summary whenever a fixed quantity is divided into parts and the parts are described by rates. A journey of two equal distances covered at $40$ and $60$ kilometres per hour has an average speed of $48$, not $50$, because the slower half occupies more of the travelling time. The harmonic mean weights each rate by the time or the quantity it governs, which is exactly what the arithmetic mean of the rates fails to do.

### 1.7 The median and the other quantiles

The median of $n$ observations, arranged in ascending order, is the middle value when $n$ is odd and the average of the two middle values when $n$ is even. In positional notation, the median is the observation in position $(n+1)/2$ when $n$ is odd, and the average of the observations in positions $n/2$ and $n/2 + 1$ when $n$ is even. For $4, 7, 7, 7, 9, 10, 10, 12, 15$ the median is the fifth value, $9$. For $6, 7, 8, 10, 11, 12$ it is the average of the third and fourth values, $(8 + 10)/2 = 9$.

A quantile of order $p$ is the value below which a proportion $p$ of the observations lie. The quartiles are the quantiles of orders $1/4$, $1/2$ and $3/4$; the deciles are the quantiles of orders $1/10, \dots, 9/10$; the percentiles are the quantiles of orders $1/100, \dots, 99/100$. The second quartile, the fifth decile and the fiftieth percentile are all the median.

For grouped data the quantiles are obtained by interpolation inside the class that contains the required position. With $L$ the lower boundary of that class, $F$ the cumulative frequency below it, $f$ its frequency, $c$ its width and $n$ the total frequency,

$$
Q(p) = L + \left(\frac{pn - F}{f}\right) c .
$$

The median is the case $p = 1/2$, the first quartile $p = 1/4$, the third quartile $p = 3/4$, the $i$-th decile $p = i/10$ and the $k$-th percentile $p = k/100$. The formula rests on the assumption that the observations are spread uniformly within each class, and that assumption is stated explicitly in Section 3.

### 1.8 The mode

The mode is the value that occurs with the greatest frequency. A data set may be unimodal, as with $2, 2, 5, 8, 8, 8$, whose mode is $8$; it may have no mode, as with $3, 5, 6, 8, 9, 10$, where every value occurs once; and it may be bimodal, as with $14, 16, 12.2, 12.2, 12, 17, 17, 18, 20$, whose modes are $12.2$ and $17$.

For a grouped distribution the modal class is the class with the greatest frequency, and the mode is estimated inside it by an interpolation that leans towards the heavier neighbouring class.

$$
\text{Mode} = L + \left(\frac{f_m - f_1}{2f_m - f_1 - f_2}\right) c
$$

Here $L$ is the lower boundary of the modal class, $f_m$ its frequency, $f_1$ the frequency of the class before it, $f_2$ the frequency of the class after it and $c$ the width of the modal class. The interpolated mode is a property of the grouping as much as of the data: change the class boundaries and the value changes, even though no observation has changed.

### 1.9 Which average for which data

The measurement scale restricts the choice before any consideration of shape arises.

| Scale | Meaningful arithmetic | Admissible averages |
|---|---|---|
| Nominal | counting only | mode |
| Ordinal | order, no distances | mode, median, quartiles |
| Interval | differences, arbitrary zero | mean, median, mode, quantiles |
| Ratio | differences and ratios, true zero | all of the above, plus geometric and harmonic means |

Within the admissible set, shape decides. A symmetric unimodal distribution has mean, median and mode close together, and the mean is preferred because it uses every observation and is arithmetically convenient. A skewed distribution or one containing outliers is better summarised by the median, which is unaffected by the size of the extreme values. A distribution with two clear peaks is best described by reporting both modes, since no single centre describes it. Multiplicative data such as growth rates call for the geometric mean, and rate data such as speeds, prices per unit and work rates call for the harmonic mean. When the mean, median and mode differ substantially, that difference is itself evidence about the shape of the distribution, and reporting all three is more informative than reporting one.

### 1.10 Merits and demerits of each average

| Average | Merits | Demerits |
|---|---|---|
| Arithmetic mean | uses every observation; unique; easy algebra; basis of variance and of most inference | pulled by outliers; not usable for nominal data; grouped value only an estimate |
| Weighted mean | allows unequal importance; exact when weights are known | the weights must be justified and can be manipulated |
| Geometric mean | correct for multiplicative change and index numbers | undefined for zero or negative values; less familiar; slightly below the arithmetic mean |
| Harmonic mean | correct for average rates and for averaging ratios with fixed numerators | undefined at zero; dominated by the smallest values; easily confused with the arithmetic mean |
| Median | resistant to outliers; exists for ordinal data; always inside the range | ignores the magnitudes of most observations; less amenable to algebra; grouped value depends on interpolation |
| Mode | the only average for nominal data; identifies the most typical category | may not exist or may be multiple; unstable in small samples; grouped value depends on class boundaries |

### 1.11 Summary of the symbols

The nine symbols used from here onward are collected once, because every later formula is written in them: $x_i$ is an observation or a class mark, $f_i$ a frequency, $k$ the number of distinct values or classes, $n$ the total frequency, $w_i$ a weight, $A$ an assumed mean, $d_i = x_i - A$ a deviation, $u_i = d_i/c$ a coded deviation for common width $c$, and $L$, $F$, $f$, $c$ the boundary, cumulative frequency below, frequency and width of the class containing a required position.

## 2. Theorems, Lemmas, and Analytical Properties

### 2.1 Lemma: the deviations from the mean sum to zero

For any data set with mean $\bar{x}$,

$$
\sum_{i=1}^{n}\left(x_i - \bar{x}\right) = 0, \qquad \sum_{i=1}^{k} f_i\left(x_i - \bar{x}\right) = 0 .
$$

The first identity says that the positive deviations exactly balance the negative ones, so the mean is a genuine centre of gravity of the observations. The second says the same thing for a frequency distribution. Both are proved in Section 3.

### 2.2 Theorem: the mean minimises the sum of squared deviations

For any real constant $c$,

$$
\sum_{i=1}^{n}\left(x_i - c\right)^{2} = \sum_{i=1}^{n}\left(x_i - \bar{x}\right)^{2} + n\left(c - \bar{x}\right)^{2} \ge \sum_{i=1}^{n}\left(x_i - \bar{x}\right)^{2},
$$

with equality only when $c = \bar{x}$. The mean is therefore the best constant predictor of the observations under a squared-error criterion, which is the property that makes it the foundation of the variance, of least squares and of most of statistical inference. For $2$, $4$, $9$ the mean is $5$ and the sum of squares about it is $26$; about $4.5$ it is $26.75$; about $7$ it is $25 + 9 + 4 = 38$. The minimum is attained exactly at the mean.

### 2.3 Theorem: change of origin and change of scale

Let $y_i = a + b x_i$ for constants $a$ and $b$. Then

$$
\bar{y} = a + b\bar{x}, \qquad \text{median}(y) = a + b\,\text{median}(x)\ \ (b > 0), \qquad \text{mode}(y) = a + b\,\text{mode}(x)\ \ (b \neq 0).
$$

The mean transforms exactly under every linear transformation, which is what licenses the assumed-mean and coding methods: subtracting $A$ shifts the mean by $-A$, and dividing by $c$ rescales it by $1/c$, so both operations can be undone. The median transforms in the same way only when $b$ is positive, because a negative $b$ reverses the order of the observations.

### 2.4 Theorem: the combined mean

Let a sample be split into groups with sizes $n_1, \dots, n_g$ and means $\bar{x}_1, \dots, \bar{x}_g$. Then the mean of the whole sample is the weighted mean of the group means with the group sizes as weights.

$$
\bar{x} = \frac{n_1\bar{x}_1 + n_2\bar{x}_2 + \cdots + n_g\bar{x}_g}{n_1 + n_2 + \cdots + n_g}
$$

Two consequences deserve memorising. The combined mean always lies between the smallest and the largest group mean. And the combined mean equals the unweighted average of the group means only when the group sizes are equal, so averaging averages is wrong in general. A morning class of $20$ learners with mean $54$ and an afternoon class of $30$ learners with mean $64$ have a combined mean of $60$, not the unweighted $59$.

### 2.5 Theorem: the arithmetic mean dominates the geometric mean

For positive values $x_1, \dots, x_n$,

$$
\frac{1}{n}\sum_{i=1}^{n} x_i \ge \left(x_1 x_2 \cdots x_n\right)^{1/n},
$$

with equality if and only if all the values are equal. For $3$, $9$, $27$ the arithmetic mean is $13$ and the geometric mean is $9$. The inequality explains a familiar fact about growth: a quantity that grows by factors whose arithmetic mean is fixed grows more slowly than that arithmetic mean, because the compounding uses the geometric mean.

### 2.6 Theorem: the geometric mean dominates the harmonic mean

For positive values,

$$
G \ge H,
$$

with equality if and only if all the values are equal. Combined with the previous theorem, the three averages are ordered.

$$
H \le G \le \bar{x}
$$

For $3$, $9$, $27$ the three values are $81/13 \approx 6.23$, $9$ and $13$, and the chain of inequalities is strict because the values differ. The width of the chain measures the dispersion of the values on a multiplicative scale: when all values coincide, all three averages coincide.

### 2.7 Proposition: the median minimises the sum of absolute deviations

For any real $c$,

$$
\sum_{i=1}^{n}\left| x_i - c \right| \ge \sum_{i=1}^{n}\left| x_i - \text{median} \right|,
$$

with equality for every $c$ between the two middle order statistics when $n$ is even. For $1$, $2$, $10$ the median is $2$ and the sum of absolute deviations about it is $9$; about the mean $13/3$ the sum is $11.33$. The median is therefore the best constant predictor under an absolute-error criterion, just as the mean is the best under a squared-error criterion, and the contrast between the two criteria is the deepest reason for preferring one measure of location over the other.

### 2.8 Theorem: the error of a grouped mean is bounded by half a class width

If every observation in class $j$ lies within half a width of the class mark $m_j$, then

$$
\left| \bar{x} - \bar{x}_g \right| \le \frac{h}{2},
$$

where $\bar{x}$ is the mean of the raw observations, $\bar{x}_g$ the mean computed from the class marks, and $h$ the common class width. The bound is attained in the worst case, for example when every observation sits at one end of its class. The theorem justifies the standard advice to narrow the classes when a grouped mean must be accurate, and it quantifies what has been lost by grouping.

### 2.9 Lemma: the mode interpolation factor lies strictly between zero and one

In the modal-class formula the factor is

$$
\frac{f_m - f_1}{2f_m - f_1 - f_2} = \frac{d_1}{d_1 + d_2}, \qquad d_1 = f_m - f_1 > 0,\ d_2 = f_m - f_2 > 0 .
$$

Since both $d_1$ and $d_2$ are positive, the factor lies strictly between zero and one, so the interpolated mode always lies strictly inside the modal class. A candidate whose answer falls outside the modal class has made an arithmetic error, and the check costs nothing. The factor also shows that the mode is closer to the neighbouring class with the larger frequency, since a large $d_2$ makes the fraction small.

### 2.10 Proposition: the quantile formula is internally consistent

Applying the interpolation formula with $p = 1/2$ returns the median, with $p = 1/4$ the lower quartile and with $p = 3/4$ the upper quartile, and the values are ordered $Q(0.25) \le Q(0.5) \le Q(0.75)$ because the cumulative frequency is non-decreasing and the position $pn$ increases with $p$. The same formula with $p = i/10$ returns the $i$-th decile and with $p = k/100$ the $k$-th percentile, so one memorised expression serves for all nine named quantiles.

### 2.11 The empirical relation between the three averages

For a moderately skewed unimodal distribution,

$$
\text{mode} \approx 3\,\text{median} - 2\,\text{mean}.
$$

The relation was proposed by Pearson as a working approximation and is exact only for a particular family of skew distributions. It is used in two ways: to estimate a missing average when two are given, and as a consistency check on three computed values. A distribution with mean $37$, median $36.875$ and mode $36$ satisfies it to within $0.6$, which is the kind of agreement to be expected. A distribution in which the relation fails by a large margin is usually strongly skewed or bimodal, and the failure is itself worth reporting.

### 2.12 The sensitivity of the mean and the median to one observation

Replacing an observation $x_j$ by $x_j + \delta$ changes the mean by $\delta/n$ and leaves the median unchanged unless the change crosses the middle of the ordered list. For the five values $4$, $7$, $7$, $9$, $13$ the mean is $8$ and the median is $7$; replacing $13$ by $113$ raises the mean to $28$ and leaves the median at $7$. The mean moves by the whole displacement divided by $n$, so a large error in one observation contaminates the mean in a way that no amount of care elsewhere can repair.

The same calculation in reverse is useful in examinations: correcting a mis-recorded observation changes the mean by the difference divided by $n$, which gives a one-line method for correcting a reported mean without re-adding the whole list.

## 3. Formal Proofs, Derivations, and Methods

### 3.1 Proof of the zero-sum lemma

Step 1. Write the sum of deviations and expand the bracket by the distributive rule.

$$
\sum_{i=1}^{n}\left(x_i - \bar{x}\right) = \sum_{i=1}^{n} x_i - \sum_{i=1}^{n} \bar{x}
$$

Step 2. Replace the second sum by the number of terms multiplied by the constant, since the mean does not depend on $i$.

$$
\sum_{i=1}^{n}\left(x_i - \bar{x}\right) = \sum_{i=1}^{n} x_i - n\bar{x}
$$

Step 3. Substitute the definition $n\bar{x} = \sum_{i=1}^{n} x_i$.

$$
\sum_{i=1}^{n}\left(x_i - \bar{x}\right) = \sum_{i=1}^{n} x_i - \sum_{i=1}^{n} x_i = 0
$$

Step 4. Repeat with each observation repeated $f_i$ times, which multiplies every term by its frequency and leaves the conclusion unchanged.

$$
\sum_{i=1}^{k} f_i\left(x_i - \bar{x}\right) = \sum_{i=1}^{k} f_i x_i - \bar{x}\sum_{i=1}^{k} f_i = n\bar{x} - \bar{x}n = 0
$$

### 3.2 Derivation of the assumed-mean formula

Step 1. Choose a convenient constant $A$ and define $d_i = x_i - A$, so that $x_i = A + d_i$.

Step 2. Sum over all observations.

$$
\sum_{i=1}^{n} x_i = \sum_{i=1}^{n}\left(A + d_i\right) = nA + \sum_{i=1}^{n} d_i
$$

Step 3. Divide by $n$.

$$
\bar{x} = A + \frac{1}{n}\sum_{i=1}^{n} d_i = A + \bar{d}
$$

Step 4. For frequency data, multiply each identity by $f_i$ before summing.

$$
\sum_{i=1}^{k} f_i x_i = A\sum_{i=1}^{k} f_i + \sum_{i=1}^{k} f_i d_i = nA + \sum_{i=1}^{k} f_i d_i
$$

Step 5. Divide by $n$ to obtain the working formula.

$$
\bar{x} = A + \frac{\sum_{i=1}^{k} f_i d_i}{n}
$$

The derivation uses nothing about $A$ except that it is constant, so any convenient value may be chosen. The saving is arithmetic rather than theoretical: deviations are small numbers, and small numbers are easier to multiply and add than the observations themselves.

### 3.3 Derivation of the coding formula

Step 1. Suppose every class has the same width $c$, choose $A$ to be a class mark, and write $d_i = c u_i$ with $u_i = d_i/c$.

Step 2. Substitute into the assumed-mean formula.

$$
\bar{x} = A + \frac{\sum_{i=1}^{k} f_i \left(c u_i\right)}{n}
$$

Step 3. Take the common factor $c$ outside the sum.

$$
\bar{x} = A + c \cdot \frac{\sum_{i=1}^{k} f_i u_i}{n} = A + c\,\bar{u}
$$

Step 4. Note that the coded values are consecutive integers when $A$ is one of the class marks, so the products $f_i u_i$ are small and the division is easy. Two operations have been performed: a change of origin, which subtracted $A$, and a change of scale, which divided by $c$. Both are undone at the end, in the reverse order.

### 3.4 Proof that the mean minimises the sum of squared deviations

Step 1. Define the function of the trial centre $c$.

$$
S(c) = \sum_{i=1}^{n}\left(x_i - c\right)^{2}
$$

Step 2. Expand the square and split the sum.

$$
S(c) = \sum_{i=1}^{n} x_i^{2} - 2c\sum_{i=1}^{n} x_i + nc^{2}
$$

Step 3. Differentiate with respect to $c$, treating the data as constants.

$$
S'(c) = -2\sum_{i=1}^{n} x_i + 2nc
$$

Step 4. Set the derivative to zero and solve.

$$
c = \frac{1}{n}\sum_{i=1}^{n} x_i = \bar{x}
$$

Step 5. The second derivative is $2n$, which is positive, so the stationary point is a minimum.

Step 6. Obtain the identity quoted in Section 2 by completing the square.

$$
S(c) = \sum_{i=1}^{n}\left(x_i - \bar{x}\right)^{2} + n\left(c - \bar{x}\right)^{2}
$$

The second term is a square multiplied by a positive number, so it vanishes only at $c = \bar{x}$ and is otherwise strictly positive. That single line contains the whole proof of optimality.

### 3.5 Proof of the arithmetic-geometric mean inequality

Step 1. Prove the case of two numbers from a perfect square.

$$
\left(\sqrt{a} - \sqrt{b}\right)^{2} \ge 0 \implies a + b \ge 2\sqrt{ab} \implies \frac{a + b}{2} \ge \sqrt{ab}
$$

Step 2. Show that the truth of the inequality for $n$ numbers implies its truth for $2n$. Split the $2n$ numbers into two blocks of $n$, with arithmetic means $A_1$ and $A_2$. By the hypothesis applied inside each block, and then to the pair $A_1, A_2$,

$$
\frac{1}{2n}\sum_{i=1}^{2n} x_i = \frac{A_1 + A_2}{2} \ge \sqrt{A_1 A_2} \ge \left[\left(\prod_{\text{block }1} x_i\right)^{1/n}\left(\prod_{\text{block }2} x_i\right)^{1/n}\right]^{1/2} = \left(\prod_{i=1}^{2n} x_i\right)^{1/(2n)}
$$

so the inequality holds for $2n$.

Step 3. Show that the truth for $n$ numbers implies the truth for $n - 1$. Given $x_1, \dots, x_{n-1}$, set the extra value equal to their arithmetic mean $A$. The arithmetic mean of the $n$ numbers is still $A$, so by hypothesis

$$
A \ge \left(x_1 \cdots x_{n-1} A\right)^{1/n} \implies A^{n} \ge \left(\prod_{i=1}^{n-1} x_i\right) A \implies A^{n-1} \ge \prod_{i=1}^{n-1} x_i \implies A \ge \left(\prod_{i=1}^{n-1} x_i\right)^{1/(n-1)} .
$$

Step 4. Combine the three steps. The inequality holds for $n = 2$; doubling carries it to $4, 8, 16, \dots$; and the backward step carries it down from any power of two to every smaller integer. Every $n \ge 2$ is at most some power of two, so the inequality holds for all $n$.

Step 5. Equality in the base case requires $a = b$. Equality in the doubling step requires the two block means to be equal and the means within each block to be equal, so equality throughout forces every observation to take the same value, as claimed.

### 3.6 Proof that the geometric mean dominates the harmonic mean

Step 1. Apply the arithmetic-geometric inequality to the reciprocals of the observations.

$$
\frac{1}{n}\sum_{i=1}^{n}\frac{1}{x_i} \ge \left(\frac{1}{x_1}\cdots\frac{1}{x_n}\right)^{1/n} = \frac{1}{G}
$$

Step 2. Take reciprocals of both sides, which reverses the inequality because both sides are positive.

$$
H = \frac{1}{\frac{1}{n}\sum_{i=1}^{n}\frac{1}{x_i}} \le G
$$

Step 3. Combine with the previous theorem to obtain the chain $H \le G \le \bar{x}$, with equality throughout only when all observations coincide.

### 3.7 Proof that the median minimises the sum of absolute deviations

Step 1. Define the objective.

$$
f(c) = \sum_{i=1}^{n}\left| x_i - c \right|
$$

Step 2. Between two consecutive data values the function is linear, and its slope is the number of observations below $c$ minus the number above $c$.

$$
f'(c) = \#\left\{i : x_i < c\right\} - \#\left\{i : x_i > c\right\}
$$

Step 3. The slope is negative while fewer than half of the observations lie below $c$, and positive once more than half lie below $c$. The minimum therefore occurs where the two counts balance, which is the median, and for even $n$ the whole interval between the two middle observations gives the same minimum.

Step 4. Conclude that the median is the optimal centre under an absolute-error loss, and note that the mean is optimal under a squared-error loss by the previous proof. The two averages are therefore not rivals but answers to two different loss functions.

### 3.8 Derivation of the grouped quantile formula

Step 1. Let the required position be $pn$ and let the class containing it have lower boundary $L$, width $c$, frequency $f$ and cumulative frequency $F$ below it.

Step 2. Assume the observations are spread uniformly inside the class, so that the fraction of the class needed to reach the position is the fraction of the class frequency still required.

$$
\text{fraction of the class} = \frac{pn - F}{f}
$$

Step 3. Convert the fraction into a distance along the axis by multiplying by the class width, and add it to the lower boundary.

$$
Q(p) = L + \left(\frac{pn - F}{f}\right) c
$$

Step 4. Specialise to the named quantiles by substituting $p = 1/4$, $1/2$, $3/4$, $i/10$ and $k/100$. The formula is linear in $p$ inside a class, so two quantiles inside the same class can be obtained from one another by proportion rather than by a fresh interpolation.

### 3.9 Derivation of the grouped mode formula

Step 1. Inside the modal class the frequency density rises from the neighbouring frequency $f_1$ at the lower boundary to the peak $f_m$, and then falls to $f_2$ at the upper boundary. Model the profile as two straight segments meeting at the peak.

Step 2. Let the peak be at distance $x$ from the lower boundary $L$. The rise on the left is $f_m - f_1 = d_1$ over the distance $x$, and the fall on the right is $f_m - f_2 = d_2$ over the distance $c - x$.

Step 3. Equate the two gradients, which is the condition that the peak be a single apex rather than a plateau.

$$
\frac{d_1}{x} = \frac{d_2}{c - x}
$$

Step 4. Cross-multiply and solve for $x$.

$$
d_2 x = d_1 c - d_1 x \implies x\left(d_1 + d_2\right) = d_1 c \implies x = \frac{d_1}{d_1 + d_2} c
$$

Step 5. Add the distance to the lower boundary and expand $d_1 + d_2$.

$$
\text{Mode} = L + \frac{f_m - f_1}{2f_m - f_1 - f_2} c
$$

Step 6. Note the two limiting cases. If $f_2 = f_m$ the mode sits at the lower boundary of the class, and if $f_1 = f_m$ it sits at the upper boundary; in both cases the neighbouring class is as heavy as the modal class and the peak is not interior.

### 3.10 Derivation of the combined mean and its corollaries

Step 1. Let group $j$ contain $n_j$ observations with total $T_j = n_j \bar{x}_j$.

Step 2. The total of the whole sample is the sum of the group totals, and the size is the sum of the group sizes.

$$
\bar{x} = \frac{\sum_{j=1}^{g} T_j}{\sum_{j=1}^{g} n_j} = \frac{\sum_{j=1}^{g} n_j \bar{x}_j}{\sum_{j=1}^{g} n_j}
$$

Step 3. For the first corollary, let $m$ and $M$ be the smallest and largest group means. Then every group mean lies between them, so the weighted average of the group means does too.

$$
m \le \bar{x} \le M
$$

Step 4. For the second corollary, set all $n_j$ equal to $n_0$; then the weights are equal and the combined mean is the unweighted average of the group means. When the sizes differ, the unweighted average is wrong by an amount that grows with the disparity in size.

### 3.11 Derivation of the missing-frequency equation

Step 1. Write the unknown frequency as a letter $f$.

Step 2. Write the total frequency as a linear expression in $f$.

$$
n = \sum_{\text{known}} f_i + f
$$

Step 3. Write the grand total of the products as a linear expression in $f$, using the known class mark of the unknown class.

$$
\sum f_i m_i = \sum_{\text{known}} f_i m_i + f m
$$

Step 4. Impose the stated mean, which gives one equation in one unknown.

$$
\frac{\sum_{\text{known}} f_i m_i + f m}{\sum_{\text{known}} f_i + f} = \bar{x}
$$

Step 5. Multiply through by the denominator, collect the terms in $f$ and solve. The equation is linear, so there is exactly one solution unless the coefficient of $f$ vanishes, which happens only when the unknown class mark equals the stated mean; in that case every frequency satisfies the equation and the problem is under-determined.

Step 6. With two unknowns, use the stated total frequency as a second linear equation and solve the pair simultaneously.

### 3.12 Proof of the bound on the grouping error

Step 1. Write the true mean as a weighted average of the class means.

$$
\bar{x} = \frac{1}{n}\sum_{j=1}^{k} f_j \bar{x}_j
$$

Step 2. Write the grouped mean as a weighted average of the class marks with the same weights.

$$
\bar{x}_g = \frac{1}{n}\sum_{j=1}^{k} f_j m_j
$$

Step 3. Subtract and take absolute values, using the triangle inequality.

$$
\left| \bar{x} - \bar{x}_g \right| = \left| \frac{1}{n}\sum_{j=1}^{k} f_j\left(\bar{x}_j - m_j\right) \right| \le \frac{1}{n}\sum_{j=1}^{k} f_j \left| \bar{x}_j - m_j \right|
$$

Step 4. Every observation in class $j$ lies between the boundaries, whose midpoint is $m_j$, so the class mean lies in the same interval and therefore within $h/2$ of the mark.

$$
\left| \bar{x}_j - m_j \right| \le \frac{h}{2}
$$

Step 5. Substitute the bound and use the normalisation of the frequencies.

$$
\left| \bar{x} - \bar{x}_g \right| \le \frac{1}{n} \cdot \frac{h}{2}\sum_{j=1}^{k} f_j = \frac{h}{2}
$$

The bound is sharp: if every observation sits at the lower boundary of its class, the grouped mean exceeds the true mean by exactly $h/2$.

### 3.13 Method: the direct mean

1. Count the observations, or add the frequency column, to obtain $n$.
2. Form the product of each value with its frequency, or the value itself when there is no frequency column.
3. For grouped data, first replace each class by its class mark, computed from the boundaries.
4. Add the products to obtain the grand total.
5. Divide the grand total by $n$.

$$
\bar{x} = \frac{\sum_{i=1}^{k} f_i x_i}{n}
$$

### 3.14 Method: the assumed mean

1. Choose $A$ near the middle of the values, preferably one of the observations or class marks.
2. Compute each deviation $d_i = x_i - A$, which should be small in magnitude.
3. Multiply each deviation by its frequency and add the products.
4. Divide by $n$ to obtain the average deviation.
5. Add the average deviation to $A$.

$$
\bar{x} = A + \frac{\sum_{i=1}^{k} f_i d_i}{n}
$$

### 3.15 Method: the coding method

1. Confirm that all classes have the same width $c$; if they do not, the method must be applied with a weighted correction or abandoned.
2. Choose $A$ to be a class mark and compute $u_i = (x_i - A)/c$, which should be consecutive integers.
3. Multiply each coded value by its frequency, add and divide by $n$ to obtain $\bar{u}$.
4. Multiply $\bar{u}$ by $c$ and add $A$.
5. Check the answer against the direct method, which must agree exactly.

### 3.16 Method: the weighted mean

1. Identify the weight of each value and state in words what the weight measures.
2. Multiply each value by its weight.
3. Add the products and add the weights separately.
4. Divide the weighted total by the total weight.
5. Note that a weight of zero removes a value from the calculation entirely, and that doubling every weight leaves the mean unchanged.

### 3.17 Method: the geometric mean by logarithms

1. Confirm that every value is positive.
2. Take the logarithm of every value, and multiply each logarithm by its frequency.
3. Add the products and divide by the total frequency, which gives the logarithm of the geometric mean.
4. Raise ten to that power to recover the geometric mean.
5. Check that the answer lies between the smallest and the largest value, and that it is no larger than the arithmetic mean.

### 3.18 Method: the harmonic mean

1. Confirm that every value is positive.
2. Take the reciprocal of every value.
3. Average the reciprocals, weighting by frequency when frequencies are given.
4. Take the reciprocal of that average.
5. Check that the answer is no larger than the geometric mean of the same values.

### 3.19 Method: the quantiles of grouped data

1. Build one cumulative frequency column and reuse it for every quantile.
2. Compute the position: $n/4$, $n/2$, $3n/4$, $in/10$ or $kn/100$.
3. Identify the class in which the cumulative frequency first reaches or passes that position.
4. Substitute the lower boundary, the cumulative frequency below the class, the class frequency and the class width into the interpolation formula.
5. Confirm that the answer lies inside the class, and that the quantiles are in the correct order.

### 3.20 Method: missing frequencies and corrected means

1. Insert a letter for each unknown frequency.
2. Write the total frequency and the grand total of the products as expressions in the unknowns.
3. Impose the stated mean, and impose the stated total frequency if it is given separately.
4. Solve the resulting linear system.
5. Verify by recomputing the mean from the recovered frequencies.
6. For a corrected observation, compute the difference between the correct and the recorded value, divide by $n$, and add the result to the reported mean.

### 3.21 A verification routine that catches most slips

1. Confirm that the frequencies sum to the stated total.
2. Confirm that the class marks increase by exactly one width each time.
3. Confirm that the median and the mode both lie inside their own classes.
4. Confirm that the three methods of computing the mean agree.
5. Confirm that $H \le G \le \bar{x}$ for any set of positive values on which all three have been computed.
6. Confirm that the empirical relation between mode, median and mean holds to within about one unit for a moderately skewed distribution.
7. Confirm that a recovered frequency is a positive integer and reproduces the stated mean.

## 4. Representative Worked Examples and Solutions

### 4.1 Problem: one distribution, three routes to the mean

A grouped distribution records the marks of $100$ learners in classes of equal width.

| Class | $5\text{–}8$ | $9\text{–}12$ | $13\text{–}16$ | $17\text{–}20$ | $21\text{–}24$ | $25\text{–}28$ | $29\text{–}32$ | $33\text{–}36$ | $37\text{–}40$ | $41\text{–}44$ |
|---|---|---|---|---|---|---|---|---|---|---|
| Frequency | $3$ | $9$ | $11$ | $10$ | $20$ | $16$ | $15$ | $6$ | $8$ | $2$ |

Compute the mean by the direct method, by the assumed-mean method with $A = 22.5$, and by the coding method. Then find the median and the mode.

### 4.2 Solution: build one working table, read three totals from it

Step 1. Compute the class marks. The limits differ by one from class to class, so the half-gap is $0.5$ and the marks are $6.5$, $10.5$, $14.5$, $18.5$, $22.5$, $26.5$, $30.5$, $34.5$, $38.5$ and $42.5$, spaced by the common width $c = 4$.

Step 2. Build the working table with the product $f_i x_i$, the deviation $d_i = x_i - 22.5$, the coded value $u_i = d_i/4$, and both weighted sums.

| Class | $f$ | $x$ | $f x$ | $d$ | $u$ | $f d$ | $f u$ |
|---|---|---|---|---|---|---|---|
| $5\text{–}8$ | $3$ | $6.5$ | $19.5$ | $-16$ | $-4$ | $-48$ | $-12$ |
| $9\text{–}12$ | $9$ | $10.5$ | $94.5$ | $-12$ | $-3$ | $-108$ | $-27$ |
| $13\text{–}16$ | $11$ | $14.5$ | $159.5$ | $-8$ | $-2$ | $-88$ | $-22$ |
| $17\text{–}20$ | $10$ | $18.5$ | $185.0$ | $-4$ | $-1$ | $-40$ | $-10$ |
| $21\text{–}24$ | $20$ | $22.5$ | $450.0$ | $0$ | $0$ | $0$ | $0$ |
| $25\text{–}28$ | $16$ | $26.5$ | $424.0$ | $4$ | $1$ | $64$ | $16$ |
| $29\text{–}32$ | $15$ | $30.5$ | $457.5$ | $8$ | $2$ | $120$ | $30$ |
| $33\text{–}36$ | $6$ | $34.5$ | $207.0$ | $12$ | $3$ | $72$ | $18$ |
| $37\text{–}40$ | $8$ | $38.5$ | $308.0$ | $16$ | $4$ | $128$ | $32$ |
| $41\text{–}44$ | $2$ | $42.5$ | $85.0$ | $20$ | $5$ | $40$ | $10$ |
| Total | $100$ | | $2390.0$ | | | $140$ | $35$ |

Step 3. Apply the direct formula to the grand total.

$$
\bar{x} = \frac{2390.0}{100} = 23.9
$$

Step 4. Apply the assumed-mean formula to the deviation total.

$$
\bar{x} = 22.5 + \frac{140}{100} = 22.5 + 1.4 = 23.9
$$

Step 5. Apply the coding formula to the coded total.

$$
\bar{x} = 22.5 + 4\left(\frac{35}{100}\right) = 22.5 + 1.4 = 23.9
$$

Step 6. All three routes agree, which confirms the arithmetic and illustrates that the choice of method is a matter of convenience, not of substance. The coding route involves only the integers from $-4$ to $5$ and is therefore the safest to perform by hand.

Step 7. Build the cumulative column: $3$, $12$, $23$, $33$, $53$, $69$, $84$, $90$, $98$, $100$. The median class is the class containing the fiftieth observation, namely $21\text{–}24$, whose lower boundary is $20.5$ and whose cumulative frequency below is $33$.

$$
\text{Median} = 20.5 + \left(\frac{50 - 33}{20}\right) 4 = 20.5 + 3.4 = 23.9
$$

Step 8. The modal class is also $21\text{–}24$, since its frequency of $20$ is the largest. With $f_1 = 10$ and $f_2 = 16$,

$$
\text{Mode} = 20.5 + \left(\frac{20 - 10}{40 - 10 - 16}\right) 4 = 20.5 + \left(\frac{10}{14}\right) 4 = 20.5 + 2.857 \approx 23.36
$$

Step 9. Interpret. The three averages are almost identical, with the mean and median both at $23.9$ and the mode at $23.36$, which is the signature of a nearly symmetric distribution. The mode lies above the class mark $22.5$ of the modal class, because the following class with frequency $16$ is heavier than the preceding class with frequency $10$ and the interpolation leans towards the heavier neighbour.

### 4.3 Problem: a weighted mean with unequal credit units

A learner's four courses carry marks $62$, $55$, $71$ and $80$ with credit units $3$, $4$, $2$ and $1$ respectively. Compute the weighted mean and compare it with the unweighted average.

### 4.4 Solution: weight by the units, not by the count of courses

Step 1. Form the products of mark and units.

| Course | Units $w_i$ | Mark $x_i$ | $w_i x_i$ |
|---|---|---|---|
| A | $3$ | $62$ | $186$ |
| B | $4$ | $55$ | $220$ |
| C | $2$ | $71$ | $142$ |
| D | $1$ | $80$ | $80$ |
| Total | $10$ | | $628$ |

Step 2. Divide the weighted total by the total weight.

$$
\bar{x}_w = \frac{628}{10} = 62.8
$$

Step 3. Compute the unweighted average for comparison.

$$
\frac{62 + 55 + 71 + 80}{4} = \frac{268}{4} = 67
$$

Step 4. Interpret. The weighted mean is $4.2$ marks lower, because the weakest mark of $55$ carries the largest weight of four units while the strongest mark of $80$ carries a single unit. Reporting the unweighted average would flatter the learner by ignoring the fact that the weakest performance was in the heaviest course.

### 4.5 Problem: geometric and harmonic means of the same values

For the values $3$, $9$ and $27$, compute the arithmetic, geometric and harmonic means, arrange them in order, and compute the geometric mean of the same values when each occurs twice.

### 4.6 Solution: three answers to three different questions

Step 1. Compute the arithmetic mean.

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

Step 4. Arrange the three values and note that the chain of inequalities is strict.

$$
6.23 < 9 < 13
$$

Step 5. For the frequency version, each value occurs twice, so the total frequency is $6$ and every value enters the product as a square.

$$
G = \sqrt[6]{3^{2} \times 9^{2} \times 27^{2}} = \sqrt[6]{\left(3 \times 9 \times 27\right)^{2}} = \left(729\right)^{1/3} = 9
$$

Step 6. Interpret. Duplicating every value leaves the geometric mean unchanged, which is the expected behaviour: the geometric mean responds to the ratio of the values, not to how many copies of each there are, provided the copies are made equally.

### 4.7 Problem: quantiles and the mode of a grouped distribution

The marks of $49$ learners are grouped in classes of width five.

| Marks | $5\text{–}10$ | $10\text{–}15$ | $15\text{–}20$ | $20\text{–}25$ | $25\text{–}30$ | $30\text{–}35$ | $35\text{–}40$ | $40\text{–}45$ |
|---|---|---|---|---|---|---|---|---|
| Frequency | $5$ | $6$ | $15$ | $10$ | $5$ | $4$ | $2$ | $2$ |

Find the median, the quartiles, the seventh decile, the ninetieth percentile and the mode.

### 4.8 Solution: one cumulative column, six positions

Step 1. Build the cumulative column and verify the total.

| Marks | Frequency | Cumulative |
|---|---|---|
| $5\text{–}10$ | $5$ | $5$ |
| $10\text{–}15$ | $6$ | $11$ |
| $15\text{–}20$ | $15$ | $26$ |
| $20\text{–}25$ | $10$ | $36$ |
| $25\text{–}30$ | $5$ | $41$ |
| $30\text{–}35$ | $4$ | $45$ |
| $35\text{–}40$ | $2$ | $47$ |
| $40\text{–}45$ | $2$ | $49$ |

Step 2. The median position is $24.5$, which is first reached in the class $15\text{–}20$ with $11$ observations below it.

$$
\text{Median} = 15 + \left(\frac{24.5 - 11}{15}\right) 5 = 15 + 4.5 = 19.5
$$

Step 3. The lower quartile position is $12.25$, which is again reached in $15\text{–}20$.

$$
Q_1 = 15 + \left(\frac{12.25 - 11}{15}\right) 5 = 15 + \frac{6.25}{15} \approx 15.42
$$

Step 4. The upper quartile position is $36.75$, which is first reached in the class $25\text{–}30$ with $36$ below it.

$$
Q_3 = 25 + \left(\frac{36.75 - 36}{5}\right) 5 = 25 + 0.75 = 25.75
$$

Step 5. The seventh decile position is $0.7 \times 49 = 34.3$, which lies in the class $20\text{–}25$ with $26$ below it.

$$
D_7 = 20 + \left(\frac{34.3 - 26}{10}\right) 5 = 20 + 4.15 = 24.15
$$

Step 6. The ninetieth percentile position is $0.9 \times 49 = 44.1$, which lies in the class $30\text{–}35$ with $41$ below it.

$$
P_{90} = 30 + \left(\frac{44.1 - 41}{4}\right) 5 = 30 + 3.875 = 33.875
$$

Step 7. The modal class is $15\text{–}20$, with $f_m = 15$, $f_1 = 6$ and $f_2 = 10$.

$$
\text{Mode} = 15 + \left(\frac{15 - 6}{30 - 6 - 10}\right) 5 = 15 + \left(\frac{9}{14}\right) 5 \approx 18.21
$$

Step 8. Check the ordering: $15.42 < 19.5 < 24.15 < 25.75 < 33.875$, which is correct since the orders increase. The mean computed from the class marks is $1027.5/49 \approx 20.97$, so the three averages are ordered mean above median above mode, which is the signature of a positively skewed distribution with a tail of high marks.

Step 9. Interpret. A quarter of the class scored below $15.42$ and three quarters below $25.75$, so half the class lies between those two marks. The seventh decile of $24.15$ means that seventy per cent of the learners scored below that mark, and the ninetieth percentile of $33.875$ means that the top ten per cent scored above it.

### 4.9 Problem: a missing frequency given the mean

A distribution has classes $10\text{–}20$, $20\text{–}30$, $30\text{–}40$, $40\text{–}50$ and $50\text{–}60$ with frequencies $6$, $9$, $f$, $8$ and $4$, and its mean is $34$. Find $f$.

### 4.10 Solution: let the algebra carry the unknown

Step 1. Write the total frequency.

$$
n = 6 + 9 + f + 8 + 4 = 27 + f
$$

Step 2. The class marks are $15$, $25$, $35$, $45$ and $55$, so the grand total of the products is

$$
\sum f_i x_i = 90 + 225 + 35f + 360 + 220 = 895 + 35f
$$

Step 3. Impose the stated mean.

$$
\frac{895 + 35f}{27 + f} = 34
$$

Step 4. Multiply both sides by the denominator.

$$
895 + 35f = 918 + 34f
$$

Step 5. Collect the terms.

$$
f = 23
$$

Step 6. Verify. The total frequency is $50$ and the grand total is $895 + 805 = 1700$, so the mean is $1700/50 = 34$, as required.

### 4.11 Problem: two missing frequencies given the total and the mean

A distribution has classes $0\text{–}10$, $10\text{–}20$, $20\text{–}30$ and $30\text{–}40$ with frequencies $5$, $a$, $b$ and $6$. There are $40$ observations and the mean is $20$. Find $a$ and $b$.

### 4.12 Solution: two unknowns, two equations

Step 1. Use the stated total to obtain the first equation.

$$
5 + a + b + 6 = 40 \implies a + b = 29
$$

Step 2. The class marks are $5$, $15$, $25$ and $35$, so the grand total of the products is

$$
25 + 15a + 25b + 210 = 235 + 15a + 25b
$$

Step 3. Impose the stated mean, which multiplies the total frequency by $20$.

$$
235 + 15a + 25b = 800 \implies 15a + 25b = 565
$$

Step 4. Substitute $a = 29 - b$ into the second equation.

$$
15\left(29 - b\right) + 25b = 565 \implies 435 + 10b = 565
$$

Step 5. Solve for $b$ and then for $a$.

$$
b = 13, \qquad a = 29 - 13 = 16
$$

Step 6. Verify. The frequencies are $5$, $16$, $13$, $6$, totalling $40$, and the grand total is $25 + 240 + 325 + 210 = 800$, so the mean is $800/40 = 20$.

### 4.13 Problem: a combined mean and a corrected mean

A morning class of $20$ learners has a mean mark of $54$ and an afternoon class of $30$ learners has a mean mark of $64$. Separately, the mean of $50$ readings was reported as $38.6$ because the value $83$ had been entered as $38$. Find the combined mean of the classes and the corrected mean of the readings.

### 4.14 Solution: convert to totals, then repair the total

Step 1. Convert each group mean back into a group total.

$$
20 \times 54 = 1080, \qquad 30 \times 64 = 1920
$$

Step 2. Add the totals and divide by the combined size.

$$
\bar{x} = \frac{1080 + 1920}{50} = \frac{3000}{50} = 60
$$

Step 3. Note that the answer is neither $59$ nor $54$; the unweighted average of the two means is $59$, and it is wrong because the two classes are of different sizes.

Step 4. For the correction, compute the change in the total.

$$
83 - 38 = 45
$$

Step 5. Divide the change by the number of readings and add it to the reported mean.

$$
\bar{x}_{\text{corrected}} = 38.6 + \frac{45}{50} = 38.6 + 0.9 = 39.5
$$

Step 6. Verify by reconstructing the total: the reported mean corresponds to a total of $50 \times 38.6 = 1930$, and the corrected total is $1930 + 45 = 1975$, whose mean is $1975/50 = 39.5$.

### 4.15 Problem: all three averages and the empirical relation

A distribution has classes $10\text{–}20$, $20\text{–}30$, $30\text{–}40$, $40\text{–}50$ and $50\text{–}60$ with frequencies $4$, $10$, $16$, $12$ and $8$. Compute the mean, the median and the mode, and test the empirical relation between them.

### 4.16 Solution: compute, then test

Step 1. The class marks are $15$, $25$, $35$, $45$ and $55$ and the total frequency is $50$.

$$
\sum f_i x_i = 60 + 250 + 560 + 540 + 440 = 1850, \qquad \bar{x} = \frac{1850}{50} = 37
$$

Step 2. The cumulative frequencies are $4$, $14$, $30$, $42$ and $50$, so the median class is $30\text{–}40$.

$$
\text{Median} = 30 + \left(\frac{25 - 14}{16}\right) 10 = 30 + 6.875 = 36.875
$$

Step 3. The modal class is $30\text{–}40$ with $f_m = 16$, $f_1 = 10$ and $f_2 = 12$.

$$
\text{Mode} = 30 + \left(\frac{16 - 10}{32 - 10 - 12}\right) 10 = 30 + \left(\frac{6}{10}\right) 10 = 36
$$

Step 4. Test the empirical relation using the computed mean and median.

$$
3\left(36.875\right) - 2\left(37\right) = 110.625 - 74 = 36.625
$$

Step 5. The estimate $36.625$ differs from the interpolated mode of $36$ by $0.625$, which is small enough to confirm a moderately skewed distribution with a single peak. The ordering mean above median above mode indicates positive skew, and the skew is mild because the three values lie within one mark of one another.

Step 6. For completeness, the quartiles follow from the same cumulative column. The lower quartile position is $12.5$, giving $Q_1 = 20 + (12.5 - 4) = 28.5$; the upper quartile position is $37.5$, giving $Q_3 = 40 + (7.5/12) \times 10 = 46.25$.

## 5. Mathematical Extensions, Limits, and Common Errors

### 5.1 Weights that are not counts

The frequency mean counts how often a value occurs. A weighted mean generalises this by allowing the weight to express importance, effort or exposure rather than repetition, and once that step is taken the arithmetic is identical but the interpretation changes completely. A portfolio's return is the weighted mean of the returns of its holdings with the amounts invested as weights; a consumer price index is a weighted mean of price relatives with expenditure shares as weights; a final grade is a weighted mean of examination marks with the marks available as weights. In each case the answer changes if the weights change, so the weights must be stated, justified and kept consistent between two comparisons. A weighted mean whose weights are chosen after the result is known is not a summary but an argument.

The frequency mean is the special case in which every weight equals one, and the grouped mean is the special case in which each weight equals the number of observations in the class. Both are therefore instances of one formula, which is why a single table of working columns serves for all of them.

### 5.2 The geometric mean in growth and index numbers

Percentages cannot be averaged arithmetically when they describe successive changes of the same quantity. A price rises by ten per cent, then by twenty per cent, then by fifteen per cent. The growth factors are $1.10$, $1.20$ and $1.15$, and the factor over the three years is their product.

$$
1.10 \times 1.20 \times 1.15 = 1.518
$$

The constant yearly factor producing the same result is the cube root of that product.

$$
G = \sqrt[3]{1.518} \approx 1.1493
$$

The average yearly growth is therefore about $14.93$ per cent, not the arithmetic average of $15$ per cent. The geometric mean is smaller whenever the factors differ, and the gap widens as the factors become more unequal.

The same reasoning governs index numbers. If three price relatives are $120$, $150$ and $80$ on a base of $100$, the typical relative is their geometric mean.

$$
G = \sqrt[3]{120 \times 150 \times 80} = \sqrt[3]{1440000} \approx 112.9
$$

The arithmetic average of the three relatives is $116.67$, which overstates the general level of prices because the fall of $20$ per cent is proportionally larger than the arithmetic average suggests. A geometric mean of relatives is the standard construction for an unweighted index, and the arithmetic mean of relatives is used only when the relatives are combined with value weights.

### 5.3 The harmonic mean in rate problems

A rate measures one quantity per unit of another, and averaging rates requires care because the denominators differ. A driver covers the first half of a journey at $40$ kilometres per hour and the second half at $60$. If each half is $60$ kilometres, the first takes $1.5$ hours and the second takes $1$ hour, so $120$ kilometres take $2.5$ hours.

$$
\bar{v} = \frac{120}{2.5} = 48
$$

The harmonic mean of the two speeds gives the same number without any assumption about the length of the halves.

$$
H = \frac{2}{\frac{1}{40} + \frac{1}{60}} = \frac{2}{\frac{3}{120} + \frac{2}{120}} = \frac{240}{5} = 48
$$

The arithmetic mean of $40$ and $60$ is $50$ and it is wrong, because the slower half lasts longer and therefore contributes more to the journey. The same structure governs the average price paid per unit when equal amounts of money are spent: spending $100$ shillings at $5$ shillings per unit and $300$ shillings at $10$ shillings per unit buys $20 + 30 = 50$ units for $400$ shillings, so the average price is $8$ shillings per unit.

$$
H_w = \frac{100 + 300}{\frac{100}{5} + \frac{300}{10}} = \frac{400}{50} = 8
$$

The rule of thumb that makes these problems safe is to ask what is held constant. When the numerator of the rate is held constant across the parts, the harmonic mean applies; when the denominator is held constant, the arithmetic mean of the rates applies. A journey of two equal times at $40$ and $60$ has an average speed of $50$, and that is not a contradiction but a different question.

### 5.4 What each average refuses to do

The mean uses every observation and therefore inherits every distortion. One salary of a million shillings added to twenty ordinary salaries moves the mean by tens of thousands and leaves the median untouched. The grouped mean is an estimate, exact only when each class is symmetric about its mark, and the error can be as large as half a class width.

The median is stable against extreme values but blind to their size. Doubling the largest observation does not change the median at all, which is a virtue when that observation is a recording error and a defect when it is a genuine and important feature of the data.

The mode is the only average available for categories, but it can be absent, and it can be multiple. A single additional observation can create a mode or destroy the existing one, and the interpolated mode of grouped data changes when the class boundaries are moved even though the observations have not changed.

The geometric mean is undefined when any value is zero or negative, because a product containing zero is zero and an even root of a negative product is not real. The harmonic mean is undefined whenever a value is zero, because the reciprocal does not exist. Neither can be used for temperatures on the Celsius scale, since that scale has an arbitrary zero.

All the grouped formulas assume that the observations are spread uniformly within each class. When the true distribution is concentrated at one end of a class, the interpolated median, quartiles and mode are all biased towards the middle of the class, and no refinement of the arithmetic removes the bias.

### 5.5 When the median and the mode supply the equations

Missing frequencies need not be recovered from the mean. A question may state the total frequency and the median, in which case the median supplies a second equation. A distribution has classes $0\text{–}10$, $10\text{–}20$, $20\text{–}30$, $30\text{–}40$ and $40\text{–}50$ with frequencies $4$, $10$, $a$, $b$ and $6$, a total of $50$ observations and a median of $25$. The total gives $a + b = 30$. The median must lie in the class $20\text{–}30$, because the cumulative frequency reaches $25$ there, and the interpolation equation is

$$
20 + \left(\frac{25 - 14}{a}\right) 10 = 25 \implies \frac{110}{a} = 5 \implies a = 22, \qquad b = 8 .
$$

Checking: the cumulative frequencies are $4$, $14$, $36$, $44$ and $50$, so the median class is indeed $20\text{–}30$, and the median is $20 + (11/22) \times 10 = 25$ as required.

When the mode is stated instead, the modal class is identified from the stated value and the mode formula becomes the second equation. With three unknowns the system is usually under-determined, which is why examination questions supply either the total or one of the frequencies explicitly.

### 5.6 Misconceptions that recur

The first misconception is that an average must equal one of the observations. It need not: a mean mark of $29.275$ is not a mark that anyone scored, and a mean of $2.4$ children per family is perfectly sensible.

The second is that the mean, median and mode are always equal. They coincide only in a perfectly symmetric unimodal distribution. In the five amounts $4$, $7$, $7$, $9$, $13$ they are $8$, $7$ and $7$.

The third is that the median can be found without sorting. The median of the list $13$, $4$, $9$, $7$, $7$ is not the third entry as it stands; the list must be ordered first.

The fourth is that the class mark is the average of the class limits when the classes have unequal gaps. The mark is the midpoint of the boundaries, and a table whose gaps differ from class to class needs the boundaries computed before the marks.

The fifth is that averaging two group means gives the mean of the combined group. It does so only when the groups are the same size, and the correct procedure always passes through the group totals.

The sixth is that the harmonic mean is a curiosity. It is the only correct answer to a whole family of rate questions, and an answer that uses the arithmetic mean of speeds is wrong by a predictable amount that grows as the speeds diverge.

The seventh is that a calculated mode is the value with the highest frequency. For ungrouped data that is true; for grouped data the modal class is the class with the highest frequency, and the mode is an interpolated value inside it that need not coincide with any observation or with the class mark.

### 5.7 Where the topic leads

Every measure of location is the first half of a description, and the second half is a measure of dispersion. The mean pairs naturally with the variance and the standard deviation, the median with the interquartile range and the quartile deviation, and the mode with the frequency profile of the distribution. The identities proved here — the zero sum of deviations, the minimising property of the mean, the chain of inequalities between the three means — reappear unchanged in the algebra of the variance, in the coding method for the standard deviation, and in the coefficients of skewness that compare the three averages. A candidate who can derive the coding formula from the definition can also derive the corresponding variance formula, and a candidate who knows why the median resists outliers can explain why the interquartile range does too.
