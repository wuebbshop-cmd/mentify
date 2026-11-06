## 1. Foundational Concepts, Definitions, and Axioms

### 1.1 What an examination on this topic demands

Questions on skewness and kurtosis are almost always of three kinds. The first kind supplies a grouped frequency distribution and asks for one or more coefficients, usually Karl Pearson's coefficient and Bowley's coefficient, sometimes with the moment coefficient as a third part. The second kind supplies a few summary numbers, such as the mean, the median, the mode and the standard deviation, or the three quartiles, and asks for a coefficient and a comment. The third kind is theoretical and asks for definitions, for the ordering of the averages, for the classification of a shape, or for a statement of what the coefficients imply about the data.

All three kinds reward the same preparation: a memorised formula sheet with the exact symbols, a practised table-building routine, a vocabulary for describing magnitude, and a habit of writing one interpretive sentence after every number. The mathematics is not difficult; the marks are lost on signs, on class boundaries, on the factor of three, and on missing comments.

### 1.2 The definitions in the form the examiner expects

> **Definition (Skewness).** Skewness measures the lack of symmetry of a distribution. A distribution is skewed to the right, or positively skewed, when its longer tail extends towards the larger values; it is skewed to the left, or negatively skewed, when its longer tail extends towards the smaller values; it is symmetric when the two tails are mirror images.

> **Definition (Kurtosis).** Kurtosis measures the degree of peakedness of a distribution relative to the normal curve, together with the weight of its tails. A curve more peaked than the normal is leptokurtic, a curve flatter than the normal is platykurtic, and the normal curve itself is mesokurtic.

Two sentences carry disproportionate marks. Under right skew the mode is less than the median, which is less than the mean; under left skew the mean is less than the median, which is less than the mode. And variation describes the amount of spread while skewness describes the direction of spread. Both sentences should be reproducible without hesitation, because they appear as one-mark parts in almost every paper.

### 1.3 The formula sheet

| Quantity | Formula | Range | Preferred when |
|---|---|---|---|
| First Pearson coefficient | $SK_P = \left(\bar{x} - \text{mode}\right)/s$ | $-3$ to $+3$ | unimodal data with a clear mode |
| Second Pearson coefficient | $SK_P = 3\left(\bar{x} - \text{median}\right)/s$ | $-3$ to $+3$ | multimodal data, or no mode available |
| Bowley's coefficient | $SK_B = \left(Q_3 + Q_1 - 2Q_2\right)/\left(Q_3 - Q_1\right)$ | $-1$ to $+1$ | open-ended classes, extreme values |
| Kelly's coefficient | $SK_K = \left(P_{90} + P_{10} - 2P_{50}\right)/\left(P_{90} - P_{10}\right)$ | $-1$ to $+1$ | emphasis needed on the tails |
| Moment coefficient | $\beta_1 = m_3^{2}/m_2^{3}$ | $0$ to $\infty$ | moments already computed |
| Signed moment coefficient | $\gamma_1 = m_3/m_2^{\frac{3}{2}}$ | unbounded | direction required from moments |
| Kurtosis | $\beta_2 = m_4/m_2^{2}$ | $1$ to $\infty$ | classification of peakedness |
| Excess kurtosis | $\gamma_2 = \beta_2 - 3$ | $-2$ to $\infty$ | comparison with the normal curve |

The conversion identities that produce $m_2$, $m_3$ and $m_4$ from working moments about an assumed origin $A$ belong on the same sheet, because no grouped question can be answered without them.

$$
m_2 = m_2' - \left(m_1'\right)^{2}, \qquad m_3 = m_3' - 3m_1'm_2' + 2\left(m_1'\right)^{3},
$$

$$
m_4 = m_4' - 4m_1'm_3' + 6\left(m_1'\right)^{2}m_2' - 3\left(m_1'\right)^{4} .
$$

### 1.4 The auxiliary formulas that the same questions need

Grouped data require the mean, the standard deviation, the mode, the quartiles and the percentiles, all of which are examinable in their own right and all of which are needed here.

$$
\bar{x} = A + c\,\frac{1}{n}\sum f_i u_i, \qquad s = \sqrt{c^{2}\left\{\frac{1}{n}\sum f_i u_i^{2} - \left(\frac{1}{n}\sum f_i u_i\right)^{2}\right\}},
$$

$$
\text{Mode} = L + \left(\frac{f_m - f_1}{2f_m - f_1 - f_2}\right)c, \qquad Q_r = L_{r} + \left(\frac{\frac{rn}{4} - F_r}{f_r}\right)c .
$$

In the mode formula $L$ is the lower boundary of the modal class, $f_m$ its frequency, $f_1$ the frequency of the class before it and $f_2$ the frequency of the class after it. In the quartile formula $F_r$ is the cumulative frequency below the class containing $Q_r$ and $f_r$ is the frequency of that class. The percentile formula is identical with $rn/100$ in place of $rn/4$.

### 1.5 Sign conventions and the ordering of the averages

| Shape | Tail | Ordering | $SK_P$ | $SK_B$ | $m_3$ | $\beta_1$ |
|---|---|---|---|---|---|---|
| Right skewed | long right | mode $<$ median $<$ mean | positive | positive | positive | positive |
| Symmetric | equal | mode $=$ median $=$ mean | zero | zero | zero | zero |
| Left skewed | long left | mean $<$ median $<$ mode | negative | negative | negative | positive |

The single entry that surprises candidates is the last one: under left skew the moment coefficient is still positive, because it is a square. The direction lives in the sign of $m_3$, not in the sign of $\beta_1$.

### 1.6 The kurtosis benchmarks

| Shape | $\beta_2$ | $\gamma_2$ | Peak | Tails |
|---|---|---|---|---|
| Platykurtic | less than $3$ | negative | flatter than normal | lighter than normal |
| Mesokurtic | equal to $3$ | zero | normal | normal |
| Leptokurtic | greater than $3$ | positive | more peaked than normal | heavier than normal |

A distribution is never described as having "kurtosis 2.6" and left there. The complete answer is "the coefficient of kurtosis is $2.6$, which is below the normal value of three, so the distribution is platykurtic: flatter topped and lighter tailed than the normal curve".

## 2. Theorems, Lemmas, and Analytical Properties

### 2.1 The high-yield results, stated for reproduction

> **Result 1 (Ordering of the averages).** Under right skew, mode $<$ median $<$ mean; under left skew, mean $<$ median $<$ mode; under symmetry all three coincide.

> **Result 2 (Direction of the mean).** The mean always lies towards the longer tail, because it is a linear functional of the observations and every observation contributes in proportion to its magnitude.

> **Result 3 (Range of the Pearson coefficients).** The theoretical range is from minus three to plus three; the practical range is usually from minus one to plus one.

> **Result 4 (Range of the quartile and percentile coefficients).** Bowley's and Kelly's coefficients lie in the closed interval from minus one to plus one, and equal zero exactly when the two half-widths are equal.

> **Result 5 (Symmetry criterion).** A symmetric distribution has $m_3 = 0$ and therefore $\beta_1 = 0$ and $\gamma_1 = 0$. The converse fails: zero moment skewness does not prove symmetry.

> **Result 6 (Kurtosis benchmarks).** $\beta_2 = 3$ and $\gamma_2 = 0$ for the normal curve; $\beta_2 < 3$ with $\gamma_2 < 0$ for platykurtic curves; $\beta_2 > 3$ with $\gamma_2 > 0$ for leptokurtic curves.

> **Result 7 (Pearson's inequality).** For every distribution with a finite fourth moment, $\beta_2 \ge \beta_1 + 1$, equivalently $\gamma_2 \ge \gamma_1^{2} - 2$. A computed pair that violates this is wrong.

> **Result 8 (Interpretive consequence).** Under marked skewness the median is the appropriate measure of location; under heavy kurtosis normal-theory intervals and tests are unreliable in small samples.

### 2.2 Relations that convert one coefficient into another

Three conversions save time in the examination and demonstrate understanding.

Given $m_3$ and $m_2$, both moment coefficients follow.

$$
\gamma_1 = \frac{m_3}{m_2^{\frac{3}{2}}}, \qquad \beta_1 = \gamma_1^{2} .
$$

Given $\beta_1$ and the sign information from the ordering of the averages, the magnitude of $\gamma_1$ follows as the signed square root.

$$
\gamma_1 = \pm\sqrt{\beta_1},
$$

with the sign chosen positive for a right skew and negative for a left skew.

Given $\beta_2$, the excess form is a subtraction.

$$
\gamma_2 = \beta_2 - 3 .
$$

The three relations are trivial algebra but they answer the common instruction "hence, or otherwise, find the remaining coefficients" without repeating the whole computation.

### 2.3 The relation between the two Pearson coefficients

The empirical relation places the mode as far below the median as the median lies below the mean.

$$
\text{mean} - \text{mode} \approx 3\left(\text{mean} - \text{median}\right) .
$$

Dividing both sides by the standard deviation gives the equivalence of the two coefficients.

$$
SK_P\left(\text{mode}\right) \approx SK_P\left(\text{median}\right) .
$$

The relation is exact for a Pearson type III curve and approximate otherwise. Its examination value is twofold: it justifies the factor of three, and it provides a cross-check. If the two versions of the coefficient differ by a factor of two, either the mode or the median has been computed wrongly, or the distribution is far from the moderate-skew family for which the relation holds.

### 2.4 The properties that make an answer defensible

| Property | Statement | Use in an answer |
|---|---|---|
| Location invariance | adding a constant changes no coefficient | justifies comparing distributions on shifted scales |
| Scale invariance | multiplying by a positive constant changes no coefficient | justifies comparing distributions in different units |
| Sign reversal | multiplying by a negative constant reverses every signed coefficient | explains why a reflected variable flips its skew |
| Boundedness | $SK_B$ and $SK_K$ lie in $\left[-1, 1\right]$ | detects arithmetic slips immediately |
| Non-negativity | $\beta_1 \ge 0$ and $\beta_2 \ge 1$ | detects arithmetic slips immediately |
| Consistency | $\beta_2 \ge \beta_1 + 1$ | detects arithmetic slips immediately |

The last three rows are the fastest error checks available in an examination. A Bowley coefficient of $1.4$, a negative $\beta_1$, or a pair with $\beta_2 = 2.1$ and $\beta_1 = 3.0$ are all impossible, and each signals a mistake that can be found and fixed before the script is handed in.

## 3. Formal Proofs, Derivations, and Methods

### 3.1 Derivation of Bowley's coefficient and of its range

Let the two half-widths be $a = Q_2 - Q_1$ and $b = Q_3 - Q_2$. A symmetric distribution has equal half-widths, so asymmetry is measured by the difference.

$$
b - a = \left(Q_3 - Q_2\right) - \left(Q_2 - Q_1\right) = Q_3 + Q_1 - 2Q_2 .
$$

To remove the units, divide by the only quantity of the same kind available, the sum of the half-widths.

$$
SK_B = \frac{b - a}{a + b} = \frac{Q_3 + Q_1 - 2Q_2}{Q_3 - Q_1} .
$$

Because $a \ge 0$ and $b \ge 0$ with $a + b > 0$, the numerator lies between $-\left(a+b\right)$ and $a+b$, so the ratio lies between minus one and plus one. Equality on the right requires $a = 0$, meaning the first quartile coincides with the median; equality on the left requires $b = 0$. Neither occurs in non-degenerate data, so for real data the inequalities are strict.

### 3.2 Derivation of the third central moment identity, step by step

The moment coefficient cannot be formed until the central moments are known, and the central moments are obtained from working moments about an assumed origin. The derivation is a single binomial expansion, and every intermediate line earns a method mark.

Step 1. Start from the definition with $d_i = x_i - A$ and write the deviation from the mean as a difference of two quantities.

$$
x_i - \bar{x} = \left(x_i - A\right) - \left(\bar{x} - A\right) = d_i - \left(\bar{x} - A\right) .
$$

Step 2. Cube both sides, using $u^{3} - 3u^{2}v + 3uv^{2} - v^{3}$ with $u = d_i$ and $v = \bar{x} - A$.

$$
\left(x_i - \bar{x}\right)^{3} = d_i^{3} - 3d_i^{2}\left(\bar{x} - A\right) + 3d_i\left(\bar{x} - A\right)^{2} - \left(\bar{x} - A\right)^{3} .
$$

Step 3. Multiply by $f_i$, sum over $i$ and divide by $n$, distributing the division across the four terms.

$$
m_3 = \frac{1}{n}\sum f_i d_i^{3} - 3\left(\bar{x} - A\right)\frac{1}{n}\sum f_i d_i^{2} + 3\left(\bar{x} - A\right)^{2}\frac{1}{n}\sum f_i d_i - \left(\bar{x} - A\right)^{3}\frac{1}{n}\sum f_i .
$$

Step 4. Identify the three working moments and the total frequency.

$$
\frac{1}{n}\sum f_i d_i^{3} = m_3', \qquad \frac{1}{n}\sum f_i d_i^{2} = m_2', \qquad \frac{1}{n}\sum f_i d_i = m_1', \qquad \frac{1}{n}\sum f_i = 1 .
$$

Step 5. Substitute, and use $\bar{x} - A = m_1'$ from the first-moment identity.

$$
m_3 = m_3' - 3m_1'm_2' + 3\left(m_1'\right)^{3} - \left(m_1'\right)^{3} .
$$

Step 6. Collect the cubic terms to obtain the final form.

$$
m_3 = m_3' - 3m_1'm_2' + 2\left(m_1'\right)^{3} .
$$

Step 7. Repeat the whole argument with the fourth power, using $u^{4} - 4u^{3}v + 6u^{2}v^{2} - 4uv^{3} + v^{4}$.

$$
m_4 = m_4' - 4m_1'm_3' + 6\left(m_1'\right)^{2}m_2' - 4\left(m_1'\right)^{3}m_1' + \left(m_1'\right)^{4} .
$$

Step 8. Collect the quartic terms.

$$
m_4 = m_4' - 4m_1'm_3' + 6\left(m_1'\right)^{2}m_2' - 3\left(m_1'\right)^{4} .
$$

The coefficient sequences to memorise are $1, -3, +2$ for the third moment and $1, -4, +6, -3$ for the fourth. Writing $1, -3, +1$ or $1, -4, +6, -4$ is the commonest arithmetic error in the topic, and it produces a third moment that is too large in magnitude by exactly $\left(m_1'\right)^{3}$.

### 3.3 Proof that a symmetric distribution has zero moment skewness

Suppose the distribution is symmetric about its mean. Group the observations into pairs equidistant from the mean, each pair consisting of $\bar{x} - h$ and $\bar{x} + h$ with the same frequency $f$, plus possibly an unpaired observation at $\bar{x}$.

The contribution of one pair to the third central moment is

$$
f\left(-h\right)^{3} + f\left(h\right)^{3} = -fh^{3} + fh^{3} = 0 .
$$

Every pair contributes zero, and any observation at the mean contributes zero, so the whole sum is zero and $m_3 = 0$. Dividing by $n$ preserves the zero. Consequently $\beta_1 = 0$ and $\gamma_1 = 0$.

The converse is false, and an examination may test it. Consider a distribution with a long thin right tail and a short thick left shoulder; the positive cubes from the tail can equal the negative cubes from the shoulder, giving $m_3 = 0$ while the shape is visibly asymmetric. The fourth central moment would reveal the difference, since $\beta_2$ would be well above three.

### 3.4 Model answer template for a grouped skewness question

1. Copy the frequency table and add a column of class marks, computed as the midpoints of the class boundaries. State that the marks are midpoints.
2. State the assumed origin $A$ and the class width $c$, then add the columns $d = x - A$, $u = d/c$, $fd$, $fd^{2}$, $fd^{3}$ and, if kurtosis is required, $fd^{4}$.
3. Total every column and verify that $\sum fd$ and $\sum fd^{3}$ carry the sign implied by the shape of the distribution.
4. Compute $\bar{x} = A + \left(\sum fd\right)/n$ and $s = \sqrt{\left(\sum fd^{2}\right)/n - \left(\left(\sum fd\right)/n\right)^{2}}$. Show one line of substitution for each.
5. Identify the modal class, state $L$, $f_m$, $f_1$, $f_2$ and $c$, and compute the mode with one line of substitution.
6. Compute $SK_P$ and write the interpretation.
7. Build the cumulative frequency column on class boundaries, with an initial zero, and verify that the last entry equals $n$.
8. Compute the target ranks $n/4$, $n/2$, $3n/4$, identify the class containing each, and interpolate. Check that $Q_1 \le Q_2 \le Q_3$.
9. Compute $SK_B$ and the percentiles required for $SK_K$ if asked, then interpret.
10. Compute $m_1'$ to $m_4'$, convert to $m_2$, $m_3$, $m_4$, and form $\beta_1$, $\gamma_1$, $\beta_2$, $\gamma_2$. Check that $\beta_1 \ge 0$, that $\beta_2 \ge 1$, and that $\beta_2 \ge \beta_1 + 1$.
11. Finish with one comparative sentence stating whether the measures agree and why their magnitudes differ.

### 3.5 The vocabulary of magnitude

| Coefficient | Slight | Moderate | Marked |
|---|---|---|---|
| $SK_P$ | $0$ to $0.2$ | $0.2$ to $0.5$ | above $0.5$ |
| $SK_B$ or $SK_K$ | $0$ to $0.1$ | $0.1$ to $0.3$ | above $0.3$ |
| $\beta_1$ | $0$ to $0.25$ | $0.25$ to $1$ | above $1$ |
| size of $\gamma_2$ | $0$ to $0.5$ | $0.5$ to $2$ | above $2$ |

The bands are conventions, not theorems, and the exact cut-offs vary between textbooks. Whatever bands are used, the answer must name the direction and the strength explicitly, since a bare number earns only the arithmetic marks.

### 3.6 The trap catalogue, with the wrong and right answers

| Trap | Wrong answer | Right answer |
|---|---|---|
| Sign of a right skew | negative coefficient | positive coefficient |
| Sign of $\beta_1$ | reported as negative | always non-negative, direction from $m_3$ |
| Factor in the second Pearson coefficient | $\left(\bar{x} - Q_2\right)/s$ | $3\left(\bar{x} - Q_2\right)/s$ |
| Class boundary | 180 used as the lower boundary | 179.5 used as the lower boundary |
| Kurtosis reference | compared with $0$ | compared with $3$ unless excess form used |
| Shape names | leptokurtic called flat | leptokurtic means peaked with heavy tails |
| Third-moment sequence | $m_3' - 3m_1'm_2' + \left(m_1'\right)^{3}$ | $m_3' - 3m_1'm_2' + 2\left(m_1'\right)^{3}$ |
| Raw moment used as central | $\beta_1 = \left(m_3'\right)^{2}/\left(m_2'\right)^{3}$ | convert to $m_3$ and $m_2$ first |
| Bowley denominator | $Q_3 + Q_1$ | $Q_3 - Q_1$ |
| Interpretation | omitted | one sentence on direction and strength required |

## 4. Representative Worked Examples and Solutions

### 4.1 Problem: model solution one, a full grouped-distribution question

The profits of one thousand companies, in thousands of shillings, are grouped in classes of width twenty.

| Profit class | 100–119 | 120–139 | 140–159 | 160–179 | 180–199 | 200–219 | 220–239 |
|---|---|---|---|---|---|---|---|
| Number of companies | 17 | 53 | 199 | 194 | 327 | 208 | 2 |

Calculate (a) Karl Pearson's first coefficient of skewness and comment on its value, (b) Bowley's coefficient of skewness, (c) the moment coefficient of skewness, (d) the coefficient of kurtosis and its excess form.

### 4.2 Solution: table first, then five standard computations

Step 1 (1 mark). Class marks are the midpoints $109.5, 129.5, 149.5, 169.5, 189.5, 209.5, 229.5$. Take $A = 169.5$ and $c = 20$.

Step 2 (3 marks). Build the working table.

| Class mark $x$ | $f$ | $d$ | $u$ | $fu$ | $fu^{2}$ | $fd$ | $fd^{2}$ | $fd^{3}$ | $fd^{4}$ |
|---|---|---|---|---|---|---|---|---|---|
| 109.5 | 17 | $-60$ | $-3$ | $-51$ | 153 | $-1020$ | 61200 | $-3672000$ | 220320000 |
| 129.5 | 53 | $-40$ | $-2$ | $-106$ | 212 | $-2120$ | 84800 | $-3392000$ | 135680000 |
| 149.5 | 199 | $-20$ | $-1$ | $-199$ | 199 | $-3980$ | 79600 | $-1592000$ | 31840000 |
| 169.5 | 194 | $0$ | $0$ | $0$ | $0$ | $0$ | $0$ | $0$ | $0$ |
| 189.5 | 327 | $20$ | $1$ | $327$ | 327 | $6540$ | 130800 | $2616000$ | 52320000 |
| 209.5 | 208 | $40$ | $2$ | $416$ | 832 | $8320$ | 332800 | $13312000$ | 532480000 |
| 229.5 | 2 | $60$ | $3$ | $6$ | 18 | $120$ | 7200 | $432000$ | 25920000 |
| Total | 1000 | | | $393$ | $1741$ | $7860$ | $696400$ | $7704000$ | $998560000$ |

Step 3 (2 marks). Compute the mean.

$$
\bar{x} = 169.5 + \frac{7860}{1000} = 169.5 + 7.86 = 177.36 .
$$

Step 4 (2 marks). Compute the standard deviation, using the $fd$ columns so that the units are already correct.

$$
s^{2} = \frac{696400}{1000} - \left(\frac{7860}{1000}\right)^{2} = 696.4 - 61.7796 = 634.6204, \qquad s = 25.19 .
$$

Step 5 (2 marks). Compute the mode. The modal class is 180–199 with $L = 179.5$, $f_m = 327$, $f_1 = 194$, $f_2 = 208$ and $c = 20$.

$$
\text{Mode} = 179.5 + \left(\frac{327 - 194}{654 - 194 - 208}\right)20 = 179.5 + \frac{2660}{252} = 190.06 .
$$

Step 6 (2 marks). Compute the first Pearson coefficient.

$$
SK_P = \frac{177.36 - 190.06}{25.19} = -0.504 .
$$

Step 7 (1 mark). Comment. The coefficient is negative, so the distribution is skewed to the left, with moderate strength; the small number of very low profits pulls the mean below the mode.

Step 8 (3 marks). Build the cumulative frequencies on class boundaries and interpolate the quartiles.

| Class boundary | 99.5 | 119.5 | 139.5 | 159.5 | 179.5 | 199.5 | 219.5 | 239.5 |
|---|---|---|---|---|---|---|---|---|
| Cumulative frequency | 0 | 17 | 70 | 269 | 463 | 790 | 998 | 1000 |

$$
Q_1 = 139.5 + \left(\frac{250 - 70}{199}\right)20 = 157.59,
$$

$$
Q_2 = 179.5 + \left(\frac{500 - 463}{327}\right)20 = 181.76,
$$

$$
Q_3 = 179.5 + \left(\frac{750 - 463}{327}\right)20 = 197.05 .
$$

Step 9 (2 marks). Compute Bowley's coefficient.

$$
SK_B = \frac{197.05 + 157.59 - 2(181.76)}{197.05 - 157.59} = \frac{-8.88}{39.46} = -0.225 .
$$

Step 10 (1 mark). Comment. The sign agrees with Pearson's, but the magnitude is smaller because the quartiles ignore the seventeen companies in the lowest class and the two hundred and ten in the two highest classes.

Step 11 (4 marks). Convert to central moments.

$$
m_1' = 7.86, \qquad m_2' = 696.4, \qquad m_3' = 7704, \qquad m_4' = 998560,
$$

$$
m_2 = 696.4 - 7.86^{2} = 634.62,
$$

$$
m_3 = 7704 - 3(7.86)(696.4) + 2(7.86)^{3} = 7704 - 16421.11 + 971.18 = -7745.94,
$$

$$
m_4 = 998560 - 4(7.86)(7704) + 6(7.86)^{2}(696.4) - 3(7.86)^{4} = 1003035.96 .
$$

Step 12 (2 marks). Form the moment coefficients.

$$
\beta_1 = \frac{\left(-7745.94\right)^{2}}{\left(634.62\right)^{3}} = \frac{60000000}{255600000} = 0.235, \qquad \gamma_1 = \frac{-7745.94}{25.19^{3}} = -0.485 .
$$

Step 13 (3 marks). Form the kurtosis coefficients.

$$
\beta_2 = \frac{1003035.96}{\left(634.62\right)^{2}} = 2.490, \qquad \gamma_2 = 2.490 - 3 = -0.510 .
$$

Step 14 (1 mark). Check consistency. The value $\beta_1 = 0.235$ is non-negative, and $\beta_2 = 2.490$ exceeds $\beta_1 + 1 = 1.235$, so Pearson's inequality is satisfied and the arithmetic is internally consistent.

Step 15 (2 marks). Interpret. The profit distribution is skewed to the left, the departure from symmetry is modest in the moment sense, and the distribution is platykurtic because its coefficient of kurtosis is below three; its peak is flatter and its tails lighter than a normal curve with the same variance, which is consistent with profits being confined to a bounded range of classes.

### 4.3 Problem: model solution two, a strongly skewed wage distribution

The daily wages of one hundred workers, in units of ten shillings, are grouped as follows.

| Wage class | 0–9 | 10–19 | 20–29 | 30–39 | 40–49 |
|---|---|---|---|---|---|
| Number of workers | 40 | 30 | 15 | 10 | 5 |

Calculate both Pearson coefficients, Bowley's coefficient, Kelly's coefficient, and the moment coefficients of skewness and kurtosis, and state which measure of location you would report.

### 4.4 Solution: verify the empirical relation as you go

Step 1 (1 mark). Class marks are $4.5, 14.5, 24.5, 34.5, 44.5$. Take $A = 24.5$ and $c = 10$.

Step 2 (3 marks). Build the coded table with $u = \left(x - 24.5\right)/10$.

| Class mark $x$ | $f$ | $u$ | $fu$ | $fu^{2}$ | $fu^{3}$ | $fu^{4}$ |
|---|---|---|---|---|---|---|
| 4.5 | 40 | $-2$ | $-80$ | 160 | $-320$ | 640 |
| 14.5 | 30 | $-1$ | $-30$ | 30 | $-30$ | 30 |
| 24.5 | 15 | $0$ | $0$ | 0 | 0 | 0 |
| 34.5 | 10 | $1$ | $10$ | 10 | 10 | 10 |
| 44.5 | 5 | $2$ | $10$ | 20 | 40 | 80 |
| Total | 100 | | $-90$ | 220 | $-300$ | 760 |

Step 3 (2 marks). Compute the mean and the variance.

$$
\bar{x} = 24.5 + 10\left(\frac{-90}{100}\right) = 15.5,
$$

$$
s^{2} = 100\left\{\frac{220}{100} - \left(\frac{-90}{100}\right)^{2}\right\} = 100\left(2.20 - 0.81\right) = 139, \qquad s = 11.79 .
$$

Step 4 (2 marks). Compute the mode from the modal class 0–9.

$$
\text{Mode} = -0.5 + \left(\frac{40 - 0}{80 - 0 - 30}\right)10 = -0.5 + 8 = 7.5 .
$$

Step 5 (2 marks). Compute the quartiles from the cumulative frequencies $40, 70, 85, 95, 100$.

$$
Q_1 = -0.5 + \frac{25}{40}\times 10 = 5.75, \qquad Q_2 = 9.5 + \frac{10}{30}\times 10 = 12.83, \qquad Q_3 = 19.5 + \frac{5}{15}\times 10 = 22.83 .
$$

Step 6 (2 marks). Compute the first Pearson coefficient.

$$
SK_P = \frac{15.5 - 7.5}{11.79} = 0.679 .
$$

Step 7 (2 marks). Compute the second Pearson coefficient.

$$
SK_P = \frac{3\left(15.5 - 12.83\right)}{11.79} = \frac{8.00}{11.79} = 0.679 .
$$

Step 8 (1 mark). Note the agreement. The two versions coincide because the mode satisfies $\text{mean} - \text{mode} = 8.00$ and $3\left(\text{mean} - \text{median}\right) = 8.00$, so the empirical relation holds exactly for this table.

Step 9 (2 marks). Compute Bowley's coefficient.

$$
SK_B = \frac{22.83 + 5.75 - 25.67}{22.83 - 5.75} = \frac{2.92}{17.08} = 0.171 .
$$

Step 10 (3 marks). Compute Kelly's coefficient, interpolating the two outer percentiles first.

$$
P_{10} = -0.5 + \frac{10}{40}\times 10 = 2.00, \qquad P_{90} = 29.5 + \frac{5}{10}\times 10 = 34.50,
$$

$$
SK_K = \frac{34.50 + 2.00 - 25.67}{34.50 - 2.00} = \frac{10.83}{32.50} = 0.333 .
$$

Step 11 (4 marks). Compute the central moments in the coded scale and rescale by powers of $c$.

$$
m_2\left(u\right) = 2.20 - 0.81 = 1.39, \qquad m_2 = 100 \times 1.39 = 139,
$$

$$
m_3\left(u\right) = -3.00 - 3\left(-0.90\right)\left(2.20\right) + 2\left(-0.90\right)^{3} = 1.482, \qquad m_3 = 1000 \times 1.482 = 1482,
$$

$$
m_4\left(u\right) = 7.60 - 4\left(-0.90\right)\left(-3.00\right) + 6\left(0.81\right)\left(2.20\right) - 3\left(0.81\right)^{2} = 5.5237, \qquad m_4 = 10000 \times 5.5237 = 55237 .
$$

Step 12 (2 marks). Form the moment coefficients.

$$
\beta_1 = \frac{1482^{2}}{139^{3}} = 0.818, \qquad \gamma_1 = \frac{1482}{11.79^{3}} = 0.904, \qquad \beta_2 = \frac{55237}{139^{2}} = 2.859 .
$$

Step 13 (2 marks). Interpret and compare. All five coefficients are positive, so the distribution is skewed to the right. The magnitudes increase steadily with the reach of the measure: $0.171$ for the middle fifty per cent, $0.333$ for the middle eighty per cent, $0.904$ for the moment measure that cubes every distance. The coefficient of kurtosis of $2.859$ is just below three, so the distribution is very mildly platykurtic.

Step 14 (2 marks). Recommend a measure of location. Because the skewness is marked and forty per cent of the workers fall in the lowest class, the median of $12.83$ units is the appropriate summary, reported with the quartiles $5.75$ and $22.83$ so that the asymmetry is visible. The mean of $15.5$ units overstates a typical wage because it is pulled upward by the five workers in the highest class.

### 4.5 Problem: model solution three, a theory question with numbers

A distribution has moment coefficient of skewness $\beta_1 = 2.25$ and coefficient of kurtosis $\beta_2 = 6.5$. Its mean is $40$, its median is $34$ and its standard deviation is $8$.

(a) Find $\gamma_1$ and $\gamma_2$ and classify the shape. (b) Verify Pearson's inequality. (c) Compute Karl Pearson's second coefficient of skewness and check the direction against the sign of $\gamma_1$. (d) State what the results imply for the choice of location and for a normal-theory confidence interval.

### 4.6 Solution: convert, classify, verify, interpret

Step 1 (2 marks). Take the signed square root of $\beta_1$.

$$
\gamma_1 = \sqrt{\beta_1} = \sqrt{2.25} = 1.50 .
$$

The sign is positive because the mean of $40$ exceeds the median of $34$, which places the long tail on the right.

Step 2 (1 mark). Convert the kurtosis coefficient to its excess form.

$$
\gamma_2 = \beta_2 - 3 = 6.5 - 3 = 3.5 .
$$

Step 3 (2 marks). Classify. The value $\beta_2 = 6.5$ exceeds three, so the distribution is leptokurtic: more sharply peaked than the normal curve and with heavier tails. The value $\gamma_1 = 1.5$ indicates marked positive skewness, since a $\beta_1$ above one corresponds to clear asymmetry.

Step 4 (2 marks). Verify Pearson's inequality.

$$
\beta_2 \ge \beta_1 + 1 \quad \text{requires} \quad 6.5 \ge 3.25,
$$

which holds, so the pair is admissible. The inequality also shows that the strong skewness requires the heavy tails, since a skewed distribution cannot be flat.

Step 5 (2 marks). Compute the second Pearson coefficient.

$$
SK_P = \frac{3\left(40 - 34\right)}{8} = \frac{18}{8} = 2.25 .
$$

Step 6 (1 mark). Check the direction. The coefficient is positive, which agrees with the positive sign of $\gamma_1$, and the ordering mean $>$ median confirms a right skew.

Step 7 (2 marks). Comment on the size. A value of $2.25$ is far outside the practical band from minus one to plus one, which is possible but unusual; it corresponds to a distribution with a very long right tail, and it is consistent with the large kurtosis already found, since the same extreme observations drive both statistics.

Step 8 (2 marks). Advise on the measure of location. With skewness this strong the mean of $40$ is not a typical value; the median of $34$ should be reported, together with an interquartile range as the measure of spread, because the standard deviation is inflated by the same tail.

Step 9 (2 marks). Advise on inference. A confidence interval built as $\bar{x} \pm t s/\sqrt{n}$ would be unreliable at any modest sample size, because the sampling distribution of the mean inherits the skewness and the standard error inherits the instability of the fourth moment. The appropriate responses are a much larger sample, a logarithmic transformation, or a bootstrap or rank-based interval.

Step 10 (1 mark). Summarise. The distribution is markedly right skewed and strongly leptokurtic; the median is the correct measure of location, and normal-theory methods should not be used without transformation or a substantial increase in sample size.

## 5. Mathematical Extensions, Limits, and Common Errors

This section collects the traps that cost marks, the extensions that separate a good script from a complete one, and a revision programme that fits the topic into a realistic number of hours. It is written to be worked through rather than read, and every item is phrased as an instruction that can be checked off.

### 5.1 The traps, explained rather than merely listed

The sign trap. A long right tail raises the mean above the mode, so the numerator of Pearson's coefficient is positive. Candidates who reason "right tail means the values are large, so the mean is small" reverse the answer. The safe procedure is always to write the ordering of the three averages first, then read the sign off the ordering, then compute the number. Two of the three steps are free marks.

The $\beta_1$ sign trap. Because $\beta_1$ squares the third moment, it can never be negative. A computed negative value means that the square has not been taken, or that $m_3$ was accidentally used with the wrong exponent. The direction must be quoted from $m_3$ or $\gamma_1$.

The factor-of-three trap. The second Pearson coefficient is $3\left(\bar{x} - Q_2\right)/s$, not $\left(\bar{x} - Q_2\right)/s$. The factor exists because the mean-median gap is about a third of the mean-mode gap, and omitting it loses the method mark even when the substitution is otherwise perfect.

The class-boundary trap. A class written as 180–199 has boundaries 179.5 and 199.5 when the data are recorded to the nearest unit. The mode and the quartiles must be interpolated from the lower boundary, and the cumulative frequencies must be attached to boundaries, not to limits. The initial cumulative frequency is zero at the boundary below the first class.

The kurtosis-reference trap. Comparing $\beta_2$ with zero makes every distribution look leptokurtic. The comparison is with three, unless the excess form has been computed, in which case the comparison is with zero. The answer must say which form is being used.

The name trap. Leptokurtic means the taller peak; platykurtic means the flatter top. A useful mnemonic is that lepto suggests a slender, tall shape and platy suggests a plate, which is flat. Reversing the two is the single most common vocabulary error in the topic.

The moment-sequence trap. The third-moment identity ends in $+2\left(m_1'\right)^{3}$, not $+\left(m_1'\right)^{3}$, and the fourth ends in $-3\left(m_1'\right)^{4}$, not $-4\left(m_1'\right)^{4}$. Both come from combining like terms, and both are frequently misremembered.

The raw-moment trap. Substituting $m_2'$ and $m_3'$ directly into the formulas for $\beta_1$ and $\beta_2$ gives a number that is not a shape coefficient at all, because the working moments depend on the arbitrary origin. The conversion must be completed first.

The interpretation trap. A script that ends with "$SK_P = -0.504$" has answered half the question. The other half is "negative, so skewed to the left, of moderate strength, with the mean pulled below the mode by a minority of low profits".

The consistency trap. Three cheap checks catch most errors: $\beta_1$ must be non-negative, $\beta_2$ must be at least one, and $\beta_2$ must be at least $\beta_1 + 1$. A script that performs these checks can find its own mistakes before submission.

### 5.2 Extensions that earn the final marks

Robustness comparisons are worth a sentence whenever two coefficients disagree. The moment coefficient weights an observation by the cube of its distance and therefore reports large values for a single outlier, while Bowley's coefficient ignores everything outside the quartiles and reports small values for the same data. A complete answer explains the discrepancy in terms of reach rather than treating it as a contradiction.

The relation between skewness and the mean-median gap can be turned into an estimate. Rearranging the empirical relation gives an approximate mode from the mean and median alone.

$$
\text{mode} \approx 3\,\text{median} - 2\,\text{mean} .
$$

For the profit data this gives $3(181.76) - 2(177.36) = 545.28 - 354.72 = 190.56$, which is within half a unit of the computed mode of $190.06$. Quoting this approximation as a check is a mark-earning habit.

Transformation is the standard remedy for skewness and can be mentioned in any interpretive part. A logarithmic transformation of right-skewed positive data pulls in the long right tail and usually reduces both skewness and kurtosis; a square-root transformation is milder and is appropriate for counts. Reflection followed by a logarithm handles left skew.

The effect of sample size belongs in any statement about kurtosis. Sample excess kurtosis has a standard error of roughly $\sqrt{24/n}$, so with a hundred observations a value of $0.5$ is indistinguishable from normal, and only values beyond about one are worth commenting on. Reporting a kurtosis of $0.2$ as evidence of a peaked distribution is an error of interpretation, not of arithmetic.

Normal-theory validity deserves a precise statement. The Berry–Esseen bound controls the error in the normal approximation to the distribution of the sample mean by $E\left|X - \mu\right|^{3}/\left(\sigma^{3}\sqrt{n}\right)$, so skewness slows convergence, and the variability of the sample variance is controlled by the fourth moment, so high kurtosis makes the standard error unreliable. Both effects shrink as the sample grows, which is why the practical advice is always "more data, transform, or use a method that does not assume normality".

### 5.3 Revision checklist

- Reproduce the five definitions from memory: skewness, right skew, left skew, kurtosis, and the three shape names.
- Reproduce the formula sheet from memory, including the two Pearson coefficients, Bowley, Kelly, $\beta_1$, $\gamma_1$, $\beta_2$ and $\gamma_2$.
- Reproduce the three conversion identities with the correct coefficient sequences.
- State the ordering of the averages under each of the three shapes without hesitation.
- State the kurtosis benchmarks with both the beta and the gamma conventions.
- Compute a grouped mean, standard deviation, mode, three quartiles and two percentiles from a table without error, using boundaries throughout.
- Complete one full grouped question, from raw table to interpreted coefficients, in under twenty-five minutes.
- Explain in one sentence why Bowley's coefficient is preferred for open-ended classes.
- Explain in one sentence why $\beta_1$ cannot indicate direction.
- Explain in one sentence what high kurtosis implies about normal-theory intervals.
- Perform the three consistency checks on every computed pair of coefficients.
- Write a comment for every coefficient, naming direction and strength.

### 5.4 Time strategy in the examination

Divide the available time for a grouped question into three parts. Spend the first third on the working table and the totals, since every later mark depends on them and a single error there propagates everywhere. Spend the second third on the derived quantities, in the order mean, standard deviation, mode, quartiles, and only then the coefficients. Spend the last third on the moment conversions, the coefficients and the interpretation.

Two habits save time throughout. Build the table with the $fd$ columns as well as the $fu$ columns when both coding and moments are needed, because the same products serve the mean, the standard deviation and all four moments. And write the cumulative frequency column once, on boundaries, with an initial zero, because the quartiles, the median and the percentiles all read from it.

If time runs short, the interpretation sentences are the cheapest marks remaining. A coefficient without a comment typically loses a mark, while a comment can be added in fifteen seconds. Never leave a numerical answer unaccompanied by a sentence.

### 5.5 Final consistency checks before submission

Check that every coefficient carries the sign implied by the ordering of the averages. Check that $\beta_1$ is non-negative and that $\beta_2$ exceeds both one and $\beta_1 + 1$. Check that $Q_1 \le Q_2 \le Q_3$ and that each quartile lies inside the class from which it was interpolated. Check that the mode lies inside the modal class. Check that the standard deviation is small relative to the range and large relative to nothing, which is to say that it is positive and plausible in the units of the data. Check that the last cumulative frequency equals $n$. Any failure of these checks points to a specific line of the working, and a correction made in the last five minutes is worth more than a new attempt at the question.
