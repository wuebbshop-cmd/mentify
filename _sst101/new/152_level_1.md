## 1. Foundational Concepts, Definitions, and Axioms

### 1.1 A village where almost everybody earns the same

Imagine a village of ten households. Nine of them earn twenty thousand shillings a month, and the tenth household is a shop owner who earns four hundred thousand shillings a month. Now imagine a second village where the ten households earn amounts that are all fairly close to one another, say between eighty thousand and one hundred and twenty thousand shillings. The two villages might well report a similar average income, yet they feel completely different to anybody who lives in them. In the first village, almost everybody sits at the low end and one single value drags the average upward. In the second village the values are balanced on both sides of the average.

That difference is the whole idea of skewness. A set of numbers is **skewed** when it is not balanced, when one side of it stretches out much further than the other side. The word itself simply means slanted or leaning. A skewed set of data leans, and the direction of the lean is decided by the long tail, not by the crowd of values near the middle.

Now picture three piles of sand, each made from exactly the same total amount of sand. The first pile is tall and narrow with steep sides. The second is a gentle rounded mound. The third is low and wide with a broad flat top. All three piles hold the same sand, so they are not different in "amount". They are different in shape: one is sharp, one is normal-looking, one is flat. That difference of sharpness is **kurtosis**. It compares the height and sharpness of a peak, and the weight of the two tails, against a smooth bell-shaped reference curve.

So the two words in this unit answer two separate questions. Skewness asks which side the data lean towards. Kurtosis asks how sharp or flat the peak is, and how much weight sits in the tails. A short way to remember the difference: dispersion tells you the amount of spread, skewness tells you the direction of spread, and kurtosis tells you how the spread is arranged between the middle and the ends.

Where the sand analogy stops being exact: real data are summarised by a frequency table or a smoothed curve, not by sand, and the "height" of the peak is measured by a ratio of averages rather than by a ruler. The intuition still carries over completely.

### 1.2 Leaning to the right, leaning to the left, and not leaning at all

A distribution leans to the right when its longer tail stretches towards the large values. Such a distribution contains a large number of relatively low scores and a few extremely high scores. Think of incomes in a poor district, waiting times at a clinic where most patients are seen quickly but one patient waits all afternoon, or house prices in a town with three mansions. This is called **positive skewness**, or skewness to the right.

A distribution leans to the left when its longer tail stretches towards the small values. Such a distribution contains a large number of relatively high scores and a few extremely low scores. Think of marks in a class where nearly everybody scores above eighty but three students score below twenty, or the ages at death in a wealthy country where almost everybody lives past seventy but a few die young. This is called **negative skewness**, or skewness to the left.

A distribution with **zero skewness** is symmetric. Its left half is a mirror image of its right half, so for every value a certain distance below the centre there is a matching value the same distance above it. The normal curve, the familiar bell shape, is the standard symmetric reference.

The words positive and negative are easy to reverse by accident, so fix them with a picture. Positive skew means the long tail points towards the bigger numbers, which is to the right on a number line, which is the positive direction of the axis. Negative skew means the long tail points towards the smaller numbers, which is the negative direction. The tail points at the sign.

### 1.3 Where the mean, the median and the mode sit

Every one of the three averages responds differently to a long tail, and that difference is the quickest diagnostic available.

When the data lean to the right, the few extremely high values pull the arithmetic mean upward, because the mean adds up every value and divides by the count, so a single huge value contributes fully. The median only cares about position, so it hardly moves. The mode stays where the crowd is. The result is the ordering: the mode is less than the median, which in turn is less than the mean.

When the data lean to the left, the few extremely low values pull the mean downward, while the median and the mode stay near the crowd. The result is the reversed ordering: the mean is less than the median, which in turn is less than the mode.

For perfectly symmetric data all three averages coincide. For skewed data the mean is different from the median, which in turn is different from the mode. This is the single most examined sentence in the whole topic, so it is worth restating slowly: under right skew the mean is the largest of the three, and under left skew the mean is the smallest of the three. The mean always sits closest to the tail, because the mean is the average that is dragged.

### 1.4 How sharp is the peak: kurtosis

Kurtosis is the degree of peakedness of a distribution, usually taken relative to a normal distribution. A curve that is more sharply peaked than the normal curve, with a tall narrow centre and comparatively thin shoulders, is called **leptokurtic**. A curve that is flatter on top than the normal curve, with its mass spread more evenly and comparatively heavy tails, is called **platykurtic**. The normal curve itself, which is the reference, is called **mesokurtic**.

The reference value comes from the mathematics of the normal curve, where the fourth moment about the mean equals three times the square of the variance. Every distribution is therefore judged by how its own fourth moment compares with three times the square of its variance. If the ratio equals three the curve is mesokurtic, if the ratio is larger the curve is leptokurtic, and if the ratio is smaller the curve is platykurtic.

A warning that saves marks: kurtosis is not only about the height of a peak. A distribution with heavy tails and a tall peak has a large fourth moment, but so does a distribution whose peak is not especially tall yet whose tails contain very extreme values. The measuring instrument is the fourth power of the distance from the mean, so extreme values count enormously. It is safest to describe kurtosis as peakedness together with tail weight, and to say that leptokurtic curves are peaked with heavy tails while platykurtic curves are flat-topped with light tails.

### 1.5 The symbols used in this unit

Before any formula is written, every symbol must be fixed.

- $n$ is the total number of observations, or the total frequency when the data are grouped.
- $x$ is an individual observation, and $\bar{x}$ is the arithmetic mean of the observations.
- $s$ is the standard deviation, the square root of the variance.
- $Q_1$, $Q_2$ and $Q_3$ are the first quartile, the median and the third quartile.
- $P_{10}$, $P_{50}$ and $P_{90}$ are the tenth, fiftieth and ninetieth percentiles.
- $D_1$ and $D_9$ are the first and ninth deciles.
- $m_2$, $m_3$ and $m_4$ are the second, third and fourth moments about the mean.
- $\beta_1$ is the moment coefficient of skewness, and $\beta_2$ is the moment coefficient of kurtosis.
- $\gamma_1$ and $\gamma_2$ are the signed square root of $\beta_1$ and the excess kurtosis respectively.

A percentile is a value below which a stated percentage of the observations lie, so the tenth percentile is the value that beats only ten per cent of the data. A quartile is a special percentile, since the first quartile is the twenty-fifth percentile and the third quartile is the seventy-fifth percentile.

### 1.6 Working axioms

Three simple facts are used so often that they deserve to be stated as rules.

> **Axiom (Balance of signed deviations).** For any set of observations, the sum of the deviations from the arithmetic mean is exactly zero.

This is why the first moment about the mean is always zero, and it is why any measure built on signed deviations must square them or take absolute values before averaging.

> **Axiom (Monotone response of the mean).** If one observation is increased while all others are held fixed, the arithmetic mean increases, and the size of the increase is the size of the change divided by the number of observations.

The mean responds to every observation in proportion to its share of the total, which is precisely why it is the average that follows a long tail.

> **Axiom (Positional insensitivity of the median).** The median depends only on the ranks of the observations, so changing the largest value while keeping the order of the data unchanged leaves the median exactly where it was.

These three axioms together explain the whole ordering of averages under skewness without any further mathematics.

## 2. Theorems, Lemmas, and Analytical Properties

### 2.1 Skewness as a formal property

> **Definition (Skewness).** Skewness is a measure of the asymmetry of a distribution. A distribution is symmetric when its two halves are mirror images; when the longer tail extends to the right the distribution has positive skewness, and when the longer tail extends to the left it has negative skewness.

Skewness is not a measure of how wide the data are. Two distributions can have exactly the same variance and still lean in opposite directions, because variance destroys the sign of every deviation while skewness keeps it. This is the meaning of the statement that variation tells us about the amount of spread while skewness tells us about the direction of spread.

### 2.2 Karl Pearson's first coefficient of skewness

> **Definition (Karl Pearson's first coefficient).** Karl Pearson's first coefficient of skewness is

$$
SK_P = \frac{\text{mean} - \text{mode}}{\text{standard deviation}} = \frac{\bar{x} - \text{mode}}{s}.
$$

The numerator measures how far the mean has been dragged away from the crowd, because the mode is where the crowd is. Dividing by the standard deviation makes the number free of units, so two distributions measured in different units can be compared. A positive value means the mean is above the mode, which happens when the tail points right.

### 2.3 Karl Pearson's second coefficient of skewness

> **Definition (Karl Pearson's second coefficient).** Karl Pearson's second coefficient of skewness is

$$
SK_P = \frac{3\left(\text{mean} - \text{median}\right)}{\text{standard deviation}} = \frac{3\left(\bar{x} - \text{median}\right)}{s}.
$$

The factor of three is an empirical correction. For moderately skewed distributions the distance between the mean and the median is roughly one third of the distance between the mean and the mode, so multiplying by three brings the two versions of the coefficient onto the same scale. The second version is valuable when a distribution has more than one mode, because the median is always well defined while the mode may not be unique.

Theoretically the value of either version can lie between minus three and plus three. In practice it usually lies between minus one and plus one, so a value near zero is nearly symmetric, a value near plus or minus half is moderate, and a value near plus or minus one is marked.

### 2.4 Bowley's quartile coefficient of skewness

> **Definition (Bowley's coefficient).** Bowley's coefficient of skewness, also called the quartile coefficient of skewness, is

$$
SK_B = \frac{Q_3 + Q_1 - 2Q_2}{Q_3 - Q_1} = \frac{Q_3 + Q_1 - 2\left(\text{median}\right)}{Q_3 - Q_1}.
$$

The numerator compares the two half-widths of the distribution. The distance from the median up to the third quartile is $Q_3 - Q_2$ and the distance from the first quartile up to the median is $Q_2 - Q_1$. Their difference is $Q_3 + Q_1 - 2Q_2$. When the upper half is stretched by a long right tail, this quantity is positive; when the lower half is stretched by a long left tail, it is negative. Dividing by the interquartile range turns it into a proportion, so Bowley's coefficient always lies between minus one and plus one.

### 2.5 Kelly's percentile coefficient of skewness

> **Definition (Kelly's coefficient).** Kelly's coefficient of skewness is

$$
SK_K = \frac{P_{90} + P_{10} - 2P_{50}}{P_{90} - P_{10}} = \frac{P_{90} + P_{10} - 2\left(\text{median}\right)}{P_{90} - P_{10}}.
$$

The structure is identical to Bowley's, with the quartiles replaced by the tenth and ninetieth percentiles. Because the two outer percentiles sit further from the centre than the quartiles, Kelly's coefficient uses more of the data than Bowley's and is therefore a little more sensitive to asymmetry, while still ignoring the most extreme five per cent at each end. Written with deciles the same quantity becomes

$$
SK_K = \frac{D_9 + D_1 - 2\left(\text{median}\right)}{D_9 - D_1}.
$$

### 2.6 The moment coefficient of skewness

> **Definition (Moment coefficient of skewness).** The moment coefficient of skewness is

$$
\beta_1 = \frac{m_3^{2}}{m_2^{3}},
$$

where $m_2$ is the second moment about the mean and $m_3$ is the third moment about the mean.

The third moment about the mean keeps the sign of the deviations after cubing them, because an odd power preserves sign. A positive $m_3$ therefore means the cubed positive deviations outweigh the cubed negative ones, which can only happen when the right tail is longer. Cubing also makes each observation count in proportion to the cube of its distance, so $m_3$ is dominated by the far tail. The signed standardised version is

$$
\gamma_1 = \frac{m_3}{m_2^{\frac{3}{2}}},
$$

and squaring it gives back $\beta_1$, so the two versions carry the same information except that $\gamma_1$ keeps the sign of the direction.

For perfectly symmetrical curves such as the normal curve, both $m_3$ and $\beta_1$ are zero. Because the numerator of $\beta_1$ is squared, $\beta_1$ itself can never be negative; it measures the amount of skewness while the sign of $m_3$ or of $\gamma_1$ gives the direction. Coefficients of skewness are used mainly to compare two or more distributions, and comparisons are described as slight, moderate or marked.

### 2.7 Kurtosis and excess kurtosis

> **Definition (Coefficient of kurtosis).** Kurtosis is measured by the coefficient

$$
\beta_2 = \frac{m_4}{m_2^{2}},
$$

and its excess form is

$$
\gamma_2 = \beta_2 - 3.
$$

The fourth moment about the mean is a sum of fourth powers, so it is always positive and is dominated by the most extreme observations. Dividing by the square of the variance standardises it, so that a distribution's shape can be compared with the normal shape regardless of its spread.

The subtraction of three is what creates the excess form. For the normal curve the fourth central moment is exactly three times the square of the variance, so $\beta_2 = 3$ and $\gamma_2 = 0$. Subtracting three simply moves the reference point to zero, which is convenient because the sign of $\gamma_2$ then tells at a glance which side of normal the distribution lies on.

### 2.8 The three shapes and their interpretation

| Coefficient | Mesokurtic | Leptokurtic | Platykurtic |
|---|---|---|---|
| $\beta_2$ | equals $3$ | greater than $3$ | less than $3$ |
| $\gamma_2$ | equals $0$ | greater than $0$ | less than $0$ |
| Peak | normal | more peaked | flatter topped |
| Tails | normal | heavier | lighter |
| Typical example | normal curve | returns on shares, income | marks in a bounded test |

The interpretation of leptokurtic data is that extreme values are more common than the normal curve would predict, because the heavy tails carry probability mass far from the centre. The interpretation of platykurtic data is the opposite: values cluster in a broad band around the centre and very large deviations are rare, which is typical of variables that cannot take extreme values because they are bounded, such as examination marks out of one hundred.

### 2.9 What the two measures imply for practical work

Two decisions depend directly on skewness and kurtosis, and both appear in examination questions.

The first is the choice of a measure of location. When a distribution is markedly skewed, the mean is pulled towards the tail and stops being a typical value, so the median is the better summary of the centre. This is exactly why house prices, incomes and waiting times are usually reported with medians. When a distribution is nearly symmetric, the mean is the better summary because it uses every observation and is more stable from sample to sample. The mode is used when the data are categorical or when the most common value is itself of interest.

The second is the validity of methods built on the normal assumption. Many confidence intervals and tests, including the familiar interval for a mean built from the standard error, rely on the sampling distribution of the mean being approximately normal. Strong skewness in the data makes that approximation poor in small samples, and heavy tails from high kurtosis make it worse, because a single extreme observation can move the mean a long way. When skewness and kurtosis are large, the safer route is a larger sample, a transformation such as taking logarithms of right-skewed positive data, or a method that does not assume normality, such as one based on ranks or on the median.

## 3. Formal Proofs, Derivations, and Methods

### 3.1 Why the mean follows the tail and the median does not

Take five weekly amounts spent on transport by five students: 10, 12, 12, 14 and 52 units of currency. The total is 100, so the mean is 20. The ordered data are 10, 12, 12, 14, 52, so the median is the third value, 12. The mode is 12, because it appears twice.

Now change the largest value from 52 to 92 and repeat.

$$
\bar{x} = \frac{10 + 12 + 12 + 14 + 92}{5} = \frac{140}{5} = 28.
$$

The mean rose from 20 to 28, a change of eight, which is exactly the change of forty in the observation divided by the five observations. The median is still 12 and the mode is still 12, because the order of the data did not change.

This single calculation contains the proof of the ordering result. An increase confined to the largest observation must raise the mean, because the mean is a sum divided by a count. It cannot raise the median, because the median only looks at which rank the observation occupies, and the largest observation occupies the last rank whatever its value. It cannot raise the mode, because the mode only counts how often each value occurs, and the value 92 occurs once just as 52 occurred once.

### 3.2 Why the three averages coincide under symmetry

Suppose the observations are 8, 10, 12, 14 and 16. The total is 60 and the mean is 12. The ordered middle value is 12, so the median is 12. Pairing each observation with its mirror image, the pair 8 and 16 has mean 12, and the pair 10 and 14 has mean 12, so the mean of all five values must also be 12.

The general argument is the same. In a symmetric distribution every observation at a distance $d$ below the centre is matched by an observation at the same distance $d$ above it, so the deviations cancel in pairs and the mean falls exactly at the centre of symmetry. The median also falls at that centre, because exactly half the observations lie on each side. Therefore the mean, the median and the mode agree, and every coefficient of skewness built from differences between them must be zero.

### 3.3 Why Bowley's coefficient must lie between minus one and plus one

Let $a = Q_2 - Q_1$ be the lower half-width and let $b = Q_3 - Q_2$ be the upper half-width. Both are non-negative because the quartiles are ordered, and the denominator of Bowley's coefficient is $a + b$, which is positive unless all the quartiles coincide.

The numerator can be rewritten exactly.

$$
Q_3 + Q_1 - 2Q_2 = \left(Q_3 - Q_2\right) - \left(Q_2 - Q_1\right) = b - a.
$$

So Bowley's coefficient is

$$
SK_B = \frac{b - a}{a + b}.
$$

Because $a$ and $b$ are non-negative, the numerator lies between $-\left(a+b\right)$ and $a+b$, so the ratio lies between minus one and plus one. The coefficient reaches plus one only in the impossible extreme where $a = 0$, meaning that the first quartile and the median coincide and the upper half carries all the width. It reaches minus one only when $b = 0$. Both extremes are limits, not attainable values for real data with distinct quartiles.

This derivation also reveals the exact meaning of the coefficient: it is the difference between the upper half-width and the lower half-width, expressed as a fraction of the total interquartile width. A value of plus one half would mean the upper half is three times as wide as the lower half.

### 3.4 Why Karl Pearson's coefficient cannot exceed three in absolute value

The argument has three short links. First, the absolute value of an average never exceeds the average of the absolute values, so the gap between the mean and the median is bounded by the mean absolute deviation about the median.

$$
\left|\bar{x} - Q_2\right| = \left|\frac{1}{n}\sum_{i=1}^{n}\left(x_i - Q_2\right)\right| \le \frac{1}{n}\sum_{i=1}^{n}\left|x_i - Q_2\right|.
$$

Second, the median minimises the mean absolute deviation among all constants, so the right-hand side is no larger than the mean absolute deviation about the mean.

$$
\frac{1}{n}\sum_{i=1}^{n}\left|x_i - Q_2\right| \le \frac{1}{n}\sum_{i=1}^{n}\left|x_i - \bar{x}\right|.
$$

Third, by the Cauchy–Schwarz inequality applied to the vectors of absolute deviations and of ones, the mean absolute deviation about the mean is at most the standard deviation.

$$
\frac{1}{n}\sum_{i=1}^{n}\left|x_i - \bar{x}\right| \le \left(\frac{1}{n}\sum_{i=1}^{n}\left(x_i - \bar{x}\right)^{2}\right)^{\frac{1}{2}} = s.
$$

Chaining the three inequalities gives the bound on the gap between the mean and the median in units of the standard deviation.

$$
\left|\bar{x} - Q_2\right| \le s, \qquad \text{so} \qquad \left|\frac{3\left(\bar{x} - Q_2\right)}{s}\right| \le 3.
$$

The first Pearson coefficient inherits the same bound through the empirical relation between the three averages, which places the mode about as far below the median as the median lies below the mean, so that the gap between the mean and the mode is roughly three times the gap between the mean and the median. Substituting that relation into the bound just proved gives the same interval from minus three to plus three. The practical message is simpler than the proof: a coefficient far outside the interval from minus one to plus one signals an arithmetic slip, not an exceptionally skewed distribution.

### 3.5 Why the moment coefficient is never negative

The third central moment can be positive, negative or zero, because it is an average of cubes and cubes keep the sign of their arguments. The moment coefficient squares it.

$$
\beta_1 = \frac{m_3^{2}}{m_2^{3}} \ge 0.
$$

A square is never negative and the cube of a positive variance is positive, so $\beta_1$ is non-negative for every data set. A negative value would be arithmetically impossible. What $\beta_1$ measures is the size of the asymmetry; the sign of $m_3$ or of $\gamma_1$ carries the direction. When a question asks for the direction of skewness and only $\beta_1$ is available, the honest answer is that the direction cannot be recovered, and a signed measure such as $SK_P$, $SK_B$ or $\gamma_1$ must be used.

### 3.6 Method for any skewness question

1. Decide what information the question gives: averages, quartiles, percentiles or moments.
2. If averages and the standard deviation are given, compute $SK_P$ with the mode if a single mode exists, and with the median version if the distribution is multimodal.
3. If quartiles are given, or if the distribution has open-ended classes, compute $SK_B$.
4. If the tenth and ninetieth percentiles are given, compute $SK_K$.
5. If central moments are given, compute $\beta_1$ for the amount and read the sign of $m_3$ for the direction.
6. State the sign, the magnitude and the interpretation in words, using the ordering of the averages as a cross-check.

The cross-check matters. If the three averages imply a right skew but the computed coefficient is negative, one of the two is wrong, and the error is usually a reversed subtraction.

## 4. Representative Worked Examples and Solutions

### 4.1 Problem: skewness of the profits of one thousand companies

The profits of one thousand companies, in thousands of shillings, are grouped as follows.

| Profit class | 100–119 | 120–139 | 140–159 | 160–179 | 180–199 | 200–219 | 220–239 |
|---|---|---|---|---|---|---|---|
| Number of companies | 17 | 53 | 199 | 194 | 327 | 208 | 2 |

Calculate Karl Pearson's first coefficient of skewness, Bowley's coefficient of skewness and the moment coefficient of skewness, and comment on each value.

### 4.2 Solution: build one working table and answer all three parts

Step 1. Fix the class marks and choose a working origin. The class width is 20, the assumed mean is the middle class mark 169.5, and the coded value is $u = \left(x - 169.5\right)/20$.

| Class mark $x$ | $f$ | $d = x - 169.5$ | $u = d/20$ | $fu$ | $fu^{2}$ | $fd$ | $fd^{2}$ | $fd^{3}$ |
|---|---|---|---|---|---|---|---|---|
| 109.5 | 17 | $-60$ | $-3$ | $-51$ | 153 | $-1020$ | 61200 | $-3672000$ |
| 129.5 | 53 | $-40$ | $-2$ | $-106$ | 212 | $-2120$ | 84800 | $-3392000$ |
| 149.5 | 199 | $-20$ | $-1$ | $-199$ | 199 | $-3980$ | 79600 | $-1592000$ |
| 169.5 | 194 | $0$ | $0$ | $0$ | $0$ | $0$ | $0$ | $0$ |
| 189.5 | 327 | $20$ | $1$ | $327$ | 327 | $6540$ | 130800 | $2616000$ |
| 209.5 | 208 | $40$ | $2$ | $416$ | 832 | $8320$ | 332800 | $13312000$ |
| 229.5 | 2 | $60$ | $3$ | $6$ | 18 | $120$ | 7200 | $432000$ |
| Total | 1000 | | | $393$ | $1741$ | $7860$ | $696400$ | $7704000$ |

Step 2. Compute the mean from the coded column.

$$
\bar{x} = 169.5 + \left(\frac{393}{1000}\right)20 = 169.5 + 7.86 = 177.36.
$$

Step 3. Compute the standard deviation from the coded second moment.

$$
s = \sqrt{20^{2}\left\{\frac{1741}{1000} - \left(\frac{393}{1000}\right)^{2}\right\}} = \sqrt{400 \times 1.586551} = 25.19.
$$

Step 4. Locate the modal class and compute the mode. The highest frequency is 327, in the class 180–199, so the lower boundary is 179.5, the modal frequency is 327, the preceding frequency is 194 and the following frequency is 208.

$$
\text{Mode} = 179.5 + \left(\frac{327 - 194}{2(327) - 194 - 208}\right)20 = 179.5 + \frac{133 \times 20}{252} = 190.06.
$$

Step 5. Compute Karl Pearson's first coefficient.

$$
SK_P = \frac{177.36 - 190.06}{25.19} = \frac{-12.70}{25.19} = -0.504.
$$

The value is negative, so the distribution is skewed to the left, and the size of about one half is described as moderate skewness.

Step 6. Build the cumulative frequencies on class boundaries.

| Class boundary | 99.5 | 119.5 | 139.5 | 159.5 | 179.5 | 199.5 | 219.5 | 239.5 |
|---|---|---|---|---|---|---|---|---|
| Cumulative frequency | 0 | 17 | 70 | 269 | 463 | 790 | 998 | 1000 |

Step 7. Interpolate the three quartiles. For the first quartile the target rank is 250, which falls in the class 140–159.

$$
Q_1 = 139.5 + \left(\frac{250 - 70}{199}\right)20 = 139.5 + 18.09 = 157.59.
$$

Step 8. For the median the target rank is 500, which falls in the class 180–199.

$$
Q_2 = 179.5 + \left(\frac{500 - 463}{327}\right)20 = 179.5 + 2.26 = 181.76.
$$

Step 9. For the third quartile the target rank is 750, which also falls in the class 180–199.

$$
Q_3 = 179.5 + \left(\frac{750 - 463}{327}\right)20 = 179.5 + 17.55 = 197.05.
$$

Step 10. Substitute into Bowley's coefficient.

$$
SK_B = \frac{197.05 + 157.59 - 2(181.76)}{197.05 - 157.59} = \frac{354.64 - 363.52}{39.46} = \frac{-8.88}{39.46} = -0.225.
$$

The sign again indicates left skew, but the magnitude is smaller than Pearson's because the quartiles ignore the two hundred and ten companies in the two highest classes and the seventeen in the lowest class.

Step 11. Convert the working moments to central moments.

$$
m_2 = m_2' - \left(m_1'\right)^{2} = 696.4 - 7.86^{2} = 696.4 - 61.78 = 634.62,
$$

$$
m_3 = m_3' - 3m_1'm_2' + 2\left(m_1'\right)^{3} = 7704 - 3(7.86)(696.4) + 2(485.59) = -7745.94.
$$

Step 12. Form the moment coefficient.

$$
\beta_1 = \frac{\left(-7745.94\right)^{2}}{\left(634.62\right)^{3}} = \frac{60000000}{255600000} = 0.235.
$$

Step 13. Interpret. All three coefficients agree that the distribution leans to the left, because all three are negative once the sign is read from $m_3$ for the moment version. The moment coefficient is small, which says only that the departure from symmetry is slight in the weighted sense of cubed deviations; it says nothing about direction, because it has been squared.

### 4.3 Problem: recovering skewness from three averages

A set of examination scores has mean 72, median 75 and mode 78, with standard deviation 10. Determine the direction of skewness and compute both versions of Karl Pearson's coefficient.

### 4.4 Solution: compare the averages, then standardise

Step 1. Compare the three averages. Here the mean of 72 is the smallest, the median of 75 is in the middle and the mode of 78 is the largest.

$$
\text{mean} < \text{median} < \text{mode}.
$$

Step 2. Read off the direction. The mean sits at the low end, so the long tail must stretch towards the small values. The distribution is skewed to the left.

Step 3. Compute the first coefficient using the mode.

$$
SK_P = \frac{72 - 78}{10} = \frac{-6}{10} = -0.60.
$$

Step 4. Compute the second coefficient using the median.

$$
SK_P = \frac{3\left(72 - 75\right)}{10} = \frac{-9}{10} = -0.90.
$$

Step 5. Comment. Both values are negative and both lie in the moderate to marked range, and the median version is larger in size because the gap between the mean and the median has been multiplied by three. The two versions agree on direction, which is the answer the examiner wants.

### 4.5 Problem: Bowley's coefficient from quartiles

A distribution of monthly rents has first quartile 20 units, median 25 units and third quartile 35 units. Compute Bowley's coefficient and interpret it.

### 4.6 Solution: apply the half-width form

Step 1. Write the two half-widths. The lower half-width is $25 - 20 = 5$ units and the upper half-width is $35 - 25 = 10$ units.

Step 2. Apply the definition directly.

$$
SK_B = \frac{35 + 20 - 2(25)}{35 - 20} = \frac{55 - 50}{15} = \frac{5}{15} = 0.333.
$$

Step 3. Interpret. The value is positive, so the distribution is skewed to the right. The upper half of the middle fifty per cent is twice as wide as the lower half, and the coefficient of one third is exactly the difference of five units divided by the interquartile range of fifteen units.

### 4.7 Problem: Kelly's coefficient from percentiles

For the same distribution the tenth percentile is 12 units and the ninetieth percentile is 36 units, with the median still 25 units. Compute Kelly's coefficient and compare it with Bowley's.

### 4.8 Solution: replace quartiles by percentiles

Step 1. Substitute into the definition.

$$
SK_K = \frac{36 + 12 - 2(25)}{36 - 12} = \frac{48 - 50}{24} = \frac{-2}{24} = -0.083.
$$

Step 2. Compare with Bowley's value of $0.333$. The two coefficients disagree in sign, and the reason is instructive: the lower tail of this distribution carries a long thin stretch between the tenth percentile and the first quartile, while the upper tail carries its stretch between the third quartile and the ninetieth percentile. Kelly's coefficient reaches further into both tails and therefore notices the pull to the left that Bowley's coefficient, confined to the middle fifty per cent, does not see.

Step 3. Comment on which to report. When two quartile-based measures disagree, the honest report describes both and explains that asymmetry is not uniform across the distribution. Reaching for the moment coefficient settles the question, because it uses every observation.

### 4.9 Problem: classifying a distribution by its moments

A sample of ten delivery times in minutes is 1, 1, 1, 1, 2, 2, 2, 2, 2 and 9. Its central moments have been computed as $m_2 = 5.21$, $m_3 = 29.18$ and $m_4 = 202.66$. Classify the shape of the distribution.

### 4.10 Solution: standardise the third and fourth moments

Step 1. Compute the moment coefficient of skewness.

$$
\beta_1 = \frac{m_3^{2}}{m_2^{3}} = \frac{29.18^{2}}{5.21^{3}} = \frac{851.71}{141.42} = 6.02.
$$

Step 2. Read the direction from the sign of the third moment. Because $m_3$ is positive, the distribution is skewed to the right, which matches the single long delivery of nine minutes among nine short ones.

Step 3. Compute the coefficient of kurtosis.

$$
\beta_2 = \frac{m_4}{m_2^{2}} = \frac{202.66}{5.21^{2}} = \frac{202.66}{27.14} = 7.47.
$$

Step 4. Convert to excess form.

$$
\gamma_2 = \beta_2 - 3 = 7.47 - 3 = 4.47.
$$

Step 5. Classify. Because $\beta_2$ exceeds three, the distribution is leptokurtic. Because $\beta_1$ is well above zero, it is also strongly skewed. The interpretation is that most deliveries are quick, one is extremely slow, and extreme values are far more common than a normal curve would suggest.

### 4.11 Problem: a symmetric distribution with heavy tails

Ten observations are $-10$, $0$, $0$, $0$, $0$, $0$, $0$, $0$, $0$ and $10$. Compute both moment coefficients and explain what the answer shows about the relationship between skewness and kurtosis.

### 4.12 Solution: compute the second and fourth moments by hand

Step 1. The mean is zero by symmetry, so the central moments are simply the averages of the powers themselves.

Step 2. Compute the second moment.

$$
m_2 = \frac{100 + 100}{10} = 20.
$$

Step 3. Compute the third moment.

$$
m_3 = \frac{-1000 + 1000}{10} = 0.
$$

Step 4. Compute the fourth moment.

$$
m_4 = \frac{10000 + 10000}{10} = 2000.
$$

Step 5. Form the coefficients.

$$
\beta_1 = \frac{0^{2}}{20^{3}} = 0, \qquad \beta_2 = \frac{2000}{20^{2}} = 5.
$$

Step 6. Interpret. The coefficient of skewness is zero, so the distribution is perfectly symmetric, yet its coefficient of kurtosis is five, far above the normal value of three, so it is strongly leptokurtic. Skewness and kurtosis are therefore independent descriptions: a distribution can be perfectly balanced and still have extremely heavy tails.

## 5. Mathematical Extensions, Limits, and Common Errors

Skewness and kurtosis are the first two shape summaries beyond location and spread, and like every summary they have a domain in which they are informative and a domain in which they mislead. This section extends the theory to the questions that arise once the basic formulas are secure, and then collects the mistakes that beginners make most often.

### 5.1 Robustness: why four different skewness measures exist

The four coefficients are not interchangeable, and the reason is resistance to extreme values. Karl Pearson's coefficients use the mean, which is moved by every observation and therefore by any single wild value. The moment coefficient uses the third power of the distance, which makes the most extreme observation count enormously. Bowley's coefficient uses only the three quartiles, so it is unchanged by anything that happens outside the middle fifty per cent. Kelly's coefficient uses the tenth and ninetieth percentiles, so it is unchanged by the extreme five per cent at each end but does respond to changes between the fifth and twenty-fifth percentiles.

For open-ended frequency distributions, where the top class is recorded only as "and above", the mean and the standard deviation cannot be computed at all, but the quartiles can, so Bowley's coefficient is the only one of the four that remains available. For distributions with more than one mode, the mode itself is ambiguous, so the median version of Pearson's coefficient or Bowley's coefficient is preferred. For distributions contaminated by recording errors, the moment coefficient is the least trustworthy because a single mis-keyed value can change its magnitude enormously and can even reverse the sign of the third moment on which its direction depends.

### 5.2 Transformations and the reduction of skewness

Right skewness in positive data is often removed by taking logarithms, because a multiplicative spread becomes an additive one. If a variable has a long right tail, the logarithms of its values are pulled in at the top, and the transformed data are often close to symmetric. The practical consequence is that a mean computed on the log scale exponentiates back to a geometric mean, which is a more sensible summary of the original data than the arithmetic mean. Left-skewed data can be reflected before transformation, for instance by subtracting every value from a constant that exceeds the maximum.

Kurtosis behaves differently under transformation. Taking logarithms of heavy-tailed positive data usually reduces kurtosis as well as skewness, which is one reason transformed data are easier to model with normal-based methods. Squaring a symmetric variable, by contrast, creates strong right skewness from a distribution that had none, because squaring maps both tails onto the positive side and stretches the large magnitudes furthest.

### 5.3 Skewness, kurtosis and the sampling distribution of the mean

The central limit theorem says that the mean of a large sample is approximately normal whatever the shape of the population. The word approximately is doing real work here. When the population is strongly skewed, the approximation is poor for small samples and improves slowly as the sample grows; when the population has heavy tails, a single extreme observation can dominate a small sample mean and produce a sampling distribution that is itself skewed and heavy-tailed.

The practical rules that follow are worth memorising. First, with strong skewness, report the median and an interquartile range rather than the mean and standard deviation, because the median is stable and the standard deviation is not. Second, when a normal-theory interval for a mean is unavoidable, increase the sample size until the skewness has little influence, or transform the data first. Third, when kurtosis is high, use a method that does not assume normal tails, such as a bootstrap interval or a rank-based test, because heavy tails inflate the true error rate of tests that assume normality.

A convenient summary statistic for both departures at once is the Jarque–Bera statistic, which combines the sample skewness and the sample excess kurtosis.

$$
JB = \frac{n}{6}\left(\gamma_1^{2} + \frac{\gamma_2^{2}}{4}\right).
$$

Under normality the sample skewness and the sample excess kurtosis are both approximately zero, so a large value of $JB$ is evidence against normality. The statistic is a screening device rather than a proof, and with small samples it has little power.

### 5.4 Limits of the coefficients

Every coefficient in this unit is a single number summarising a whole shape, and a single number cannot be a complete description. Two distributions can share the same $\beta_1$ and the same $\beta_2$ and still differ in the arrangement of their mass, because higher moments carry the information that the first four discard. A bimodal distribution may have zero skewness because its two humps are placed symmetrically, even though no single central value describes it well.

The moment coefficients are also sensitive to the divisor convention. Dividing the sums by $n$ rather than by $n-1$ gives slightly smaller values of the variance and of every higher moment, and the difference matters in small samples. Published sample skewness and sample kurtosis are often bias-corrected, so values computed from a textbook formula and from software may differ in the third decimal place. In an examination the divisor is always the total frequency, and the answer should say so.

Finally, kurtosis is often described loosely as peakedness, and the description is only half true. The fourth moment is dominated by the tails, so a distribution with heavy tails and a modest peak can be strongly leptokurtic. The safe phrasing is that leptokurtic distributions are more peaked and have heavier tails than the normal curve, while platykurtic distributions are flatter and have lighter tails.

### 5.5 Beginner misconceptions to eliminate

- Skewness is not the same as dispersion. A distribution can be widely spread and perfectly symmetric, and it can be tightly bunched and strongly skewed.
- A long right tail gives a positive coefficient, not a negative one. Check the ordering of the averages before writing a sign.
- The median never moves when the largest observation changes, so a large change in the mean with no change in the median is evidence of skewness, not of an arithmetic error.
- $\beta_1$ cannot be negative. A negative value means the arithmetic has gone wrong, because the numerator is squared.
- The direction of skewness comes from the sign of $m_3$ or $\gamma_1$, never from $\beta_1$, which has lost the sign.
- Kurtosis is compared with three, not with zero, unless the excess form is used. A $\beta_2$ of 2.75 is platykurtic and is not "nearly normal but slightly low"; the comparison is strict.
- Leptokurtic means more peaked, platykurtic means flatter. Reversing these two words is the commonest single error in the topic, so attach them to the tails as well: leptokurtic means heavy tails, platykurtic means light tails.
- Forgetting to subtract three gives an excess kurtosis that looks alarming when the distribution is only mildly non-normal.
- The factor of three in the second Pearson coefficient is part of the formula, not a decoration. Omitting it halves or triples the answer and loses the method marks.
- Class boundaries, not stated class limits, must be used in the mode and quartile formulas. A class written as 180–199 has a lower boundary of 179.5.
- Quartile-based coefficients ignore the tails by construction, so they are small whenever the bulk of the data is nearly symmetric even if one extreme value is enormous. A small Bowley coefficient therefore does not prove symmetry.
- A single coefficient without a sentence of interpretation is an incomplete answer. State the sign, the magnitude and what they mean for the data.
