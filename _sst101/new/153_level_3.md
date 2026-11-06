## 1. Foundational Concepts, Definitions, and Axioms

### 1.1 What the examiner is testing

Moments questions look formula-heavy but test only four things: whether the candidate can build a working table without error, whether the conversion identities are known with the right coefficients, whether the standardised coefficients are formed correctly, and whether the numbers are interpreted in the language of skewness and kurtosis. Every mark in the topic can be traced to one of those four.

There are three recurring question types. The first supplies a frequency table and asks for the first four moments about the mean, sometimes followed by the coefficients of skewness and kurtosis. The second supplies moments about an arbitrary origin and asks for the mean, the central moments, or the moments about a different origin. The third is theoretical: state the meaning of the four central moments, prove that a symmetric distribution has zero third moment, or explain the effect of a change of origin or scale.

The routine below is designed to fit all three. It is worth rehearsing until the table columns appear without conscious thought, because the arithmetic is where marks are lost and the layout is where time is saved.

### 1.2 The definitions, stated compactly for reproduction

> **Definition (Moment about zero).** The $r$-th moment about zero is the average of the $r$-th powers of the observations.

$$
\bar{x^{r}} = \frac{1}{n}\sum_{i=1}^{n} x_i^{r} .
$$

> **Definition (Central moment).** The $r$-th moment about the mean is the average of the $r$-th powers of the deviations from the mean.

$$
m_r = \frac{1}{n}\sum_{i=1}^{n}\left(x_i - \bar{x}\right)^{r} .
$$

> **Definition (Moment about an arbitrary origin).** For a chosen origin $A$ and deviations $d_i = x_i - A$,

$$
m_r' = \frac{1}{n}\sum_{i=1}^{n} d_i^{r} .
$$

> **Definition (Standardised moment coefficients).**

$$
\gamma_1 = \frac{m_3}{m_2^{\frac{3}{2}}}, \qquad \beta_1 = \gamma_1^{2}, \qquad \beta_2 = \frac{m_4}{m_2^{2}}, \qquad \gamma_2 = \beta_2 - 3 .
$$

Four sentences carry the interpretation. The first central moment is always zero. The second central moment is the variance. The third central moment measures asymmetry, positive for a right tail and negative for a left tail. The fourth central moment measures tail weight, and when standardised against three times the square of the variance it classifies the shape as mesokurtic, leptokurtic or platykurtic.

### 1.3 The formula bank

| Quantity | Formula | Value to remember |
|---|---|---|
| Mean from coded data | $\bar{x} = A + c\,\bar{u}$ | $A + c\left(\sum fu\right)/n$ |
| Standard deviation | $s = \sqrt{m_2}$ | positive root only |
| Second central moment | $m_2 = m_2' - \left(m_1'\right)^{2}$ | always non-negative |
| Third central moment | $m_3 = m_3' - 3m_1'm_2' + 2\left(m_1'\right)^{3}$ | sign gives the direction |
| Fourth central moment | $m_4 = m_4' - 4m_1'm_3' + 6\left(m_1'\right)^{2}m_2' - 3\left(m_1'\right)^{4}$ | always positive |
| Skewness coefficient | $\beta_1 = m_3^{2}/m_2^{3}$ | zero for symmetry |
| Signed skewness | $\gamma_1 = m_3/m_2^{\frac{3}{2}}$ | keeps the sign |
| Kurtosis coefficient | $\beta_2 = m_4/m_2^{2}$ | three for the normal curve |
| Excess kurtosis | $\gamma_2 = \beta_2 - 3$ | zero for the normal curve |
| Coded central moment | $m_r = c^{r} m_r\left(u\right)$ | power of $c$ matches the order |

### 1.4 Notation as the examiner writes it

Two conventions appear in past questions and both must be recognised instantly. When the phrase is "moments about the value 5", the symbol is $m_r'$ and the deviations are $x - 5$. When the phrase is "moments about the mean", the symbol is $m_r$ and the deviations are $x - \bar{x}$. A question that begins "the first four moments of a distribution about the value 5 are 2, 20, 40 and 50" is therefore supplying $m_1' = 2$ and asking, in its second part, for the values with the prime removed.

The order of the moments is always stated in words, but the conventional assignment never varies: first is the mean or zero, second is the variance, third is skewness, fourth is kurtosis. A question that asks for "the first four moments about the mean" expects the list to begin with zero, and a script that omits the zero loses a mark even though it contains nothing of substance.

### 1.5 The interpretation bank

| Situation | Sentence to write |
|---|---|
| $m_3 = 0$ | the distribution is symmetric about its mean |
| $m_3 > 0$ | the distribution has a longer right tail, so it is positively skewed |
| $m_3 < 0$ | the distribution has a longer left tail, so it is negatively skewed |
| $\beta_2 = 3$ | the tails match those of a normal curve, so the shape is mesokurtic |
| $\beta_2 > 3$ | the tails are heavier than normal, so the shape is leptokurtic |
| $\beta_2 < 3$ | the tails are lighter than normal, so the shape is platykurtic |
| $m_4$ large relative to $m_2^{2}$ | extreme observations are unusually influential |

These sentences are worth rehearsing because they convert a computed number into a mark. A script that reports $m_3 = -192.47$ and stops has done two thirds of the work; the remaining third is the observation that the negative sign means a left tail and that the distribution is therefore skewed towards the low values.

## 2. Theorems, Lemmas, and Analytical Properties

### 2.1 The eight results to have ready

> **Result 1.** $m_1 = 0$ for every data set, because the deviations from the mean sum to zero.

> **Result 2.** $m_2 = s^{2}$, the variance, and $s = \sqrt{m_2}$ is the standard deviation.

> **Result 3.** $m_2$ is the smallest second moment about any point: for every constant $c$, the average squared deviation about $c$ equals $m_2 + \left(\bar{x} - c\right)^{2}$.

> **Result 4.** If the distribution is symmetric then every odd central moment vanishes, so $m_3 = 0$ and $\beta_1 = 0$.

> **Result 5.** $m_4 > 0$ always, and $m_4 \ge m_2^{2}$, so $\beta_2 \ge 1$.

> **Result 6.** For every distribution with a finite fourth moment, $\beta_2 \ge \beta_1 + 1$, equivalently $\gamma_2 \ge \gamma_1^{2} - 2$.

> **Result 7.** For the normal distribution $m_3 = 0$ and $m_4 = 3\sigma^{4}$, so $\beta_1 = 0$, $\beta_2 = 3$ and $\gamma_2 = 0$.

> **Result 8.** If $y = a + bx$ then $m_r\left(y\right) = b^{r}m_r\left(x\right)$, so $\beta_1$ and $\beta_2$ are unchanged by any change of origin or scale.

The last three results are the ones that turn arithmetic into a defensible answer, because they supply consistency checks. Results 5 and 6 in particular catch most computational errors before the script is submitted.

### 2.2 The conversion table with coefficient sequences

| Target | Formula | Sequence of coefficients |
|---|---|---|
| $m_1$ | $0$ | none |
| $m_2$ | $m_2' - \left(m_1'\right)^{2}$ | $1, -1$ |
| $m_3$ | $m_3' - 3m_1'm_2' + 2\left(m_1'\right)^{3}$ | $1, -3, +2$ |
| $m_4$ | $m_4' - 4m_1'm_3' + 6\left(m_1'\right)^{2}m_2' - 3\left(m_1'\right)^{4}$ | $1, -4, +6, -3$ |
| $m_5$ | $m_5' - 5m_1'm_4' + 10\left(m_1'\right)^{2}m_3' - 10\left(m_1'\right)^{3}m_2' + 4\left(m_1'\right)^{5}$ | $1, -5, +10, -10, +4$ |

The sequences are the binomial coefficients with alternating signs, modified only in the final term, where two contributions combine. For the third moment the expansion ends in $+3$ and $-1$, which combine to $+2$. For the fourth it ends in $-4$ and $+1$, which combine to $-3$. For the fifth it ends in $+5$ and $-1$, which combine to $+4$. Nothing else deviates, so any of the sequences can be reconstructed from the ordinary binomial coefficients when memory fails.

### 2.3 Behaviour under transformations

| Transformation | Effect on $m_2$ | Effect on $m_3$ | Effect on $\gamma_1$ | Effect on $\beta_2$ |
|---|---|---|---|---|
| $y = x + a$ | unchanged | unchanged | unchanged | unchanged |
| $y = bx$, $b > 0$ | multiplied by $b^{2}$ | multiplied by $b^{3}$ | unchanged | unchanged |
| $y = bx$, $b < 0$ | multiplied by $b^{2}$ | multiplied by $b^{3}$ | sign reversed | unchanged |
| $y = x^{2}$ | no simple rule | no simple rule | no simple rule | no simple rule |

The fourth row is a reminder rather than a rule: squaring changes the shape fundamentally and destroys the symmetry of a symmetric variable, mapping both tails onto the positive side.

### 2.4 Results from the moment generating function

| Distribution | Moment generating function | $m_3$ | $m_4$ | $\beta_2$ |
|---|---|---|---|---|
| Normal, mean $\mu$, variance $\sigma^{2}$ | $\exp\left(\mu t + \sigma^{2}t^{2}/2\right)$ | $0$ | $3\sigma^{4}$ | $3$ |
| Exponential, rate $\lambda$ | $\lambda/\left(\lambda - t\right)$ | $2\lambda^{-3}$ | $9\lambda^{-4}$ | $9$ |
| Two-point, values $0$ and $1$, probability $p$ | $1 - p + pe^{t}$ | $p\left(1-p\right)\left(1-2p\right)$ | see the worked example | at least $1$, equal to $1$ when $p = 0.5$ |

The table is a rapid reference for checking a computation. If a question supplies a moment generating function, the raw moments are the coefficients of $t^{r}/r!$ in its expansion, and the central moments follow by conversion. If a question supplies the raw moments directly, the same conversion applies.

### 2.5 Consistency conditions and what they detect

| Condition | What it rules out | Typical cause of failure |
|---|---|---|
| $m_2 \ge 0$ | a negative variance | a lost square or a sign error in conversion |
| $m_4 > 0$ | a negative fourth moment | a sign error in the $-3\left(m_1'\right)^{4}$ term |
| $\beta_1 \ge 0$ | a negative skewness coefficient | the square has not been taken |
| $\beta_2 \ge 1$ | an impossibly flat distribution | raw and central moments have been confused |
| $\beta_2 \ge \beta_1 + 1$ | an impossible pair of coefficients | arithmetic error, or moments that are not realisable |

The last row deserves emphasis. The condition is sharp: it holds with equality for two-point distributions, and every genuine data set satisfies it strictly. A quoted quadruple of moments that violates it is an algebraic exercise rather than a description of real data, and a computed pair that violates it contains an error.

## 3. Formal Proofs, Derivations, and Methods

### 3.1 Complete derivation of the three conversion identities

Step 1. Write the deviation from the mean as a difference of two deviations from the assumed origin.

$$
x_i - \bar{x} = \left(x_i - A\right) - \left(\bar{x} - A\right) = d_i - m_1' .
$$

Step 2. Square and average to obtain the second identity, expanding the square into three terms.

$$
m_2 = \frac{1}{n}\sum f_i d_i^{2} - 2m_1'\frac{1}{n}\sum f_i d_i + \left(m_1'\right)^{2}\frac{1}{n}\sum f_i = m_2' - 2\left(m_1'\right)^{2} + \left(m_1'\right)^{2} = m_2' - \left(m_1'\right)^{2} .
$$

Step 3. Cube and average to obtain the third identity, expanding into four terms.

$$
m_3 = m_3' - 3m_1'm_2' + 3\left(m_1'\right)^{2}m_1' - \left(m_1'\right)^{3} = m_3' - 3m_1'm_2' + 2\left(m_1'\right)^{3} .
$$

Step 4. Raise to the fourth power and average to obtain the fourth identity, expanding into five terms.

$$
m_4 = m_4' - 4m_1'm_3' + 6\left(m_1'\right)^{2}m_2' - 4\left(m_1'\right)^{3}m_1' + \left(m_1'\right)^{4} = m_4' - 4m_1'm_3' + 6\left(m_1'\right)^{2}m_2' - 3\left(m_1'\right)^{4} .
$$

Step 5. State the general form, which generates all of them and also the higher orders.

$$
m_r' = \sum_{j=0}^{r}\binom{r}{j}m_j\left(\bar{x} - A\right)^{r-j}, \qquad m_0 = 1 .
$$

Step 6. Note the two reading directions. Solving the general identity for $m_r$ gives the conversion from working moments to central moments; applying it with the roles of $A$ and $\bar{x}$ exchanged gives the conversion from central moments to moments about any other point, which is the form needed for questions of the type "find the third moment about 10".

### 3.2 Proof that a symmetric distribution has zero odd central moments

Group the observations into pairs at equal distances $h$ on either side of the mean, with equal frequencies $f$, plus any observation sitting exactly at the mean.

Step 1. Compute the contribution of one pair to the $r$-th central moment for odd $r$.

$$
f\left(-h\right)^{r} + f\left(h\right)^{r} = -f h^{r} + f h^{r} = 0 .
$$

Step 2. Sum over all pairs. Every contribution is zero, and any observation at the mean contributes zero, so the whole sum vanishes.

Step 3. Conclude that $m_r = 0$ for all odd $r$, and in particular that $m_1 = 0$ and $m_3 = 0$, so that $\gamma_1 = 0$ and $\beta_1 = 0$.

Step 4. Note the failure of the converse. A distribution may have a long thin tail on one side and a thick short shoulder on the other, so that the positive cubes and the negative cubes cancel. The third moment is then zero although the shape is not a mirror image; the fourth moment reveals the difference.

### 3.3 Proof that the variance is the smallest second moment

Step 1. Write the average squared deviation about an arbitrary constant $c$.

$$
\frac{1}{n}\sum_{i=1}^{n}\left(x_i - c\right)^{2} .
$$

Step 2. Add and subtract the mean inside the bracket and expand.

$$
\frac{1}{n}\sum_{i=1}^{n}\left[\left(x_i - \bar{x}\right) + \left(\bar{x} - c\right)\right]^{2} = m_2 + 2\left(\bar{x} - c\right)\cdot 0 + \left(\bar{x} - c\right)^{2} .
$$

Step 3. Conclude that the average squared deviation about $c$ equals $m_2 + \left(\bar{x} - c\right)^{2}$, which is at least $m_2$ and equals it only when $c = \bar{x}$.

Step 4. Apply the result to the working origin. With $c = A$ the identity becomes $m_2' = m_2 + \left(\bar{x} - A\right)^{2}$, which rearranges to $m_2 = m_2' - \left(m_1'\right)^{2}$ and shows that the correction is exactly the penalty for having measured from the wrong point.

### 3.4 Derivation of the normal value of the kurtosis coefficient

Step 1. Standardise, so that $Z = \left(X - \mu\right)/\sigma$ has mean zero and variance one.

Step 2. Integrate by parts using the identity $\varphi'\left(z\right) = -z\varphi\left(z\right)$ for the standard normal density.

$$
E\left[Z^{4}\right] = \int z^{4}\varphi\left(z\right)dz = \int z^{3}\left(-\varphi'\left(z\right)\right)dz = 3\int z^{2}\varphi\left(z\right)dz .
$$

Step 3. The boundary term vanishes because $z^{3}\varphi\left(z\right)$ tends to zero at both ends, and the remaining integral is $E\left[Z^{2}\right] = 1$, so $E\left[Z^{4}\right] = 3$.

Step 4. Rescale. Since $X - \mu = \sigma Z$, the fourth central moment of $X$ is $\sigma^{4}$ times the fourth moment of $Z$, giving $m_4 = 3\sigma^{4}$.

Step 5. Form the coefficient.

$$
\beta_2 = \frac{3\sigma^{4}}{\left(\sigma^{2}\right)^{2}} = 3, \qquad \gamma_2 = 0 .
$$

Step 6. Record the consequence. Because the normal curve sits exactly at three, the excess form is the natural scale for comparison, and the three shape names are defined by which side of three an empirical value falls on.

### 3.5 Model answer routine for a frequency-table question

1. Copy the table, add the class marks as midpoints of the class boundaries, and state the total frequency $n$.
2. Choose the assumed origin $A$ as a central class mark and record the class width $c$.
3. Add the columns $d = x - A$, $u = d/c$, $fu$, $fu^{2}$, $fu^{3}$ and $fu^{4}$, and total every column.
4. Divide each total by $n$ to obtain $m_1'$ to $m_4'$ in the coded scale, then convert to the coded central moments and multiply by powers of $c$. Alternatively work in the original units with the $fd$ columns and skip the rescaling.
5. Verify $m_1'$ against the mean, and verify that the coded and uncoded routes agree.
6. Compute $s$, $\gamma_1$, $\beta_1$, $\beta_2$ and $\gamma_2$, and apply the three consistency checks.
7. Write one interpretive sentence for the third moment and one for the fourth.

### 3.6 The trap catalogue

| Trap | Symptom | Correction |
|---|---|---|
| Sign error in an odd moment | a positive third moment for visibly left-skewed data | check each $fd^{3}$ entry, particularly the sign of $d$ |
| Raw moments used as central | $\beta_2$ depends on the arbitrary origin | complete the conversion before forming any coefficient |
| Forgetting the subtraction of three | a "huge" kurtosis of $3.2$ | excess kurtosis is $\beta_2 - 3$ |
| Leptokurtic and platykurtic reversed | a claim that heavy tails mean flat | lepto means peaked and heavy, platy means flat and light |
| Divisor wrong | moments far too large | divide by $n = \sum f$, never by the number of classes |
| Power of $c$ wrong | coded moments off by a factor | $c^{2}$, $c^{3}$, $c^{4}$ for orders two, three, four |
| Coefficient sequence wrong | third moment off by $\left(m_1'\right)^{3}$ | use $1, -3, +2$ and $1, -4, +6, -3$ |
| $\beta_1$ reported as negative | a negative squared quantity | take the square, or report $\gamma_1$ instead |
| Interpretation omitted | a list of numbers with no comment | write the direction and the tail weight in words |
| Consistency not checked | an impossible pair slips through | test $\beta_2 \ge 1$ and $\beta_2 \ge \beta_1 + 1$ |

## 4. Representative Worked Examples and Solutions

### 4.1 Problem: model solution one, a symmetric discrete distribution

Calculate the first four moments about the mean for the following distribution, and hence the coefficients of skewness and kurtosis.

| $x$ | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
|---|---|---|---|---|---|---|---|---|---|
| $f$ | 1 | 8 | 28 | 56 | 70 | 56 | 28 | 8 | 1 |

### 4.2 Solution: exploit the symmetry, then interpret

Step 1 (1 mark). Choose the assumed origin at the centre, $A = 4$, because the frequencies are symmetric about it. Then $d = x - 4$.

Step 2 (4 marks). Build the working table.

| $x$ | $f$ | $d$ | $fd$ | $fd^{2}$ | $fd^{3}$ | $fd^{4}$ |
|---|---|---|---|---|---|---|
| 0 | 1 | $-4$ | $-4$ | 16 | $-64$ | 256 |
| 1 | 8 | $-3$ | $-24$ | 72 | $-216$ | 648 |
| 2 | 28 | $-2$ | $-56$ | 112 | $-224$ | 448 |
| 3 | 56 | $-1$ | $-56$ | 56 | $-56$ | 56 |
| 4 | 70 | $0$ | $0$ | 0 | 0 | 0 |
| 5 | 56 | $1$ | $56$ | 56 | $56$ | 56 |
| 6 | 28 | $2$ | $56$ | 112 | $224$ | 448 |
| 7 | 8 | $3$ | $24$ | 72 | $216$ | 648 |
| 8 | 1 | $4$ | $4$ | 16 | $64$ | 256 |
| Total | 256 | | $0$ | $512$ | $0$ | $2816$ |

Step 3 (2 marks). Divide each total by $n = 256$.

$$
m_1' = 0, \qquad m_2' = 2, \qquad m_3' = 0, \qquad m_4' = 11 .
$$

Step 4 (3 marks). Convert to central moments, noting that every correction term vanishes because $m_1' = 0$.

$$
m_1 = 0, \qquad m_2 = 2 - 0 = 2, \qquad m_3 = 0 - 0 + 0 = 0, \qquad m_4 = 11 - 0 + 0 - 0 = 11 .
$$

Step 5 (2 marks). Compute the standard deviation and the coefficients.

$$
s = \sqrt{2} = 1.414, \qquad \beta_1 = \frac{0^{2}}{2^{3}} = 0, \qquad \beta_2 = \frac{11}{2^{2}} = 2.75, \qquad \gamma_2 = -0.25 .
$$

Step 6 (1 mark). Check. The mean is $4$, which matches $m_1' = 0$ with $A = 4$. The second moment is positive, the third is zero as symmetry requires, and the fourth is positive.

Step 7 (2 marks). Interpret. The distribution is symmetric, so its coefficient of skewness is zero and its mean, median and mode all equal four. The coefficient of kurtosis of $2.75$ is below three, so the distribution is platykurtic: its peak is flatter and its tails lighter than a normal curve of the same variance. The absence of values beyond zero and eight guarantees light tails, which is exactly what the coefficient reports.

Step 8 (1 mark). Comment on method. Because the table is symmetric about the chosen origin, the odd columns cancel and the arithmetic for $m_3$ is free. Recognising such a symmetry before starting saves several minutes and removes the risk of a sign error.

### 4.3 Problem: model solution two, a grouped distribution with kurtosis

The daily wages of one hundred workers are grouped in classes of width five.

| Wage class | 3–7 | 8–12 | 13–17 | 18–22 | 23–27 | 28–32 | 33–37 |
|---|---|---|---|---|---|---|---|
| Workers | 4 | 10 | 20 | 36 | 16 | 12 | 2 |

Calculate the first four moments about the mean, the coefficients of skewness and kurtosis, and interpret.

### 4.4 Solution: code the data, then restore the scale

Step 1 (1 mark). The class marks are $5, 10, 15, 20, 25, 30, 35$. Take $A = 20$ and $c = 5$, so $u = \left(x - 20\right)/5$.

Step 2 (4 marks). Build the coded table.

| $x$ | $f$ | $u$ | $fu$ | $fu^{2}$ | $fu^{3}$ | $fu^{4}$ |
|---|---|---|---|---|---|---|
| 5 | 4 | $-3$ | $-12$ | 36 | $-108$ | 324 |
| 10 | 10 | $-2$ | $-20$ | 40 | $-80$ | 160 |
| 15 | 20 | $-1$ | $-20$ | 20 | $-20$ | 20 |
| 20 | 36 | $0$ | $0$ | 0 | 0 | 0 |
| 25 | 16 | $1$ | $16$ | 16 | $16$ | 16 |
| 30 | 12 | $2$ | $24$ | 48 | $96$ | 192 |
| 35 | 2 | $3$ | $6$ | 18 | $54$ | 162 |
| Total | 100 | | $-6$ | $178$ | $-42$ | $874$ |

Step 3 (2 marks). Divide by $n = 100$ to obtain the coded working moments.

$$
m_1'\left(u\right) = -0.06, \qquad m_2'\left(u\right) = 1.78, \qquad m_3'\left(u\right) = -0.42, \qquad m_4'\left(u\right) = 8.74 .
$$

Step 4 (2 marks). Convert to the coded central moments.

$$
m_2\left(u\right) = 1.78 - 0.0036 = 1.7764,
$$

$$
m_3\left(u\right) = -0.42 - 3\left(-0.06\right)\left(1.78\right) + 2\left(-0.06\right)^{3} = -0.42 + 0.3204 - 0.0004 = -0.1000,
$$

$$
m_4\left(u\right) = 8.74 - 4\left(-0.06\right)\left(-0.42\right) + 6\left(0.0036\right)\left(1.78\right) - 3\left(0.0036\right)^{2} = 8.74 - 0.1008 + 0.0384 - 0.0000 = 8.6776 .
$$

Step 5 (2 marks). Restore the scale with the powers of $c = 5$.

$$
m_2 = 25 \times 1.7764 = 44.41, \qquad m_3 = 125 \times \left(-0.1000\right) = -12.50, \qquad m_4 = 625 \times 8.6776 = 5423.5 .
$$

Step 6 (1 mark). Recover the mean.

$$
\bar{x} = 20 + 5\left(-0.06\right) = 19.7 .
$$

Step 7 (2 marks). Compute the standard deviation and the coefficients.

$$
s = \sqrt{44.41} = 6.664, \qquad \gamma_1 = \frac{-12.50}{6.664^{3}} = -0.042, \qquad \beta_1 = 0.0018,
$$

$$
\beta_2 = \frac{5423.5}{44.41^{2}} = \frac{5423.5}{1972.2} = 2.750, \qquad \gamma_2 = -0.250 .
$$

Step 8 (2 marks). Check consistency. The second moment is positive, the fourth moment exceeds the square of the second since $5423.5 > 1972.2$, and $2.750$ exceeds $0.0018 + 1 = 1.0018$, so all three conditions hold.

Step 9 (2 marks). Interpret. The mean wage is $19.7$ units. The third moment is very slightly negative, so the distribution is almost symmetric with a barely perceptible left skew, and the coefficient $\beta_1 = 0.0018$ confirms that the asymmetry is negligible. The coefficient of kurtosis of $2.750$ lies below three, so the distribution is mildly platykurtic, with a flatter peak and lighter tails than a normal curve of the same variance, which is what one expects of a variable confined to a small number of wage bands.

Step 10 (1 mark). Comment on method. Coding reduced every deviation to a single-digit integer, so the fourth powers could be computed without a calculator. The final multiplication by $625$ restores the units, and the check against the uncoded route confirms that no power of $c$ was lost.

### 4.5 Problem: model solution three, moments about a different origin

The first four moments of a distribution about the value 3 are $-2$, $10$, $-25$ and $50$. Find the mean, the first four moments about the mean, and the moments about the value 5 and about zero.

### 4.6 Solution: translate, then translate again

Step 1 (1 mark). Use the first working moment.

$$
m_1' = \bar{x} - A \quad \text{gives} \quad -2 = \bar{x} - 3, \quad \text{so} \quad \bar{x} = 1 .
$$

Step 2 (2 marks). Convert the second moment.

$$
m_2 = 10 - \left(-2\right)^{2} = 10 - 4 = 6 .
$$

Step 3 (3 marks). Convert the third moment, watching the signs of the correction terms.

$$
m_3 = -25 - 3\left(-2\right)\left(10\right) + 2\left(-2\right)^{3} = -25 + 60 - 16 = 19 .
$$

Step 4 (3 marks). Convert the fourth moment.

$$
m_4 = 50 - 4\left(-2\right)\left(-25\right) + 6\left(-2\right)^{2}\left(10\right) - 3\left(-2\right)^{4} = 50 - 200 + 240 - 48 = 42 .
$$

Step 5 (2 marks). Record the moments about the mean.

$$
m_1 = 0, \qquad m_2 = 6, \qquad m_3 = 19, \qquad m_4 = 42 .
$$

Step 6 (3 marks). Translate to the origin 5, using $\bar{x} - 5 = -4$ in the general identity.

$$
m_1'\left(5\right) = -4,
$$

$$
m_2'\left(5\right) = 6 + \left(-4\right)^{2} = 22,
$$

$$
m_3'\left(5\right) = 19 + 3\left(6\right)\left(-4\right) + \left(-4\right)^{3} = 19 - 72 - 64 = -117,
$$

$$
m_4'\left(5\right) = 42 + 4\left(19\right)\left(-4\right) + 6\left(6\right)\left(16\right) + \left(-4\right)^{4} = 42 - 304 + 576 + 256 = 570 .
$$

Step 7 (3 marks). Translate to the origin zero, using $\bar{x} - 0 = 1$.

$$
m_1'\left(0\right) = 1, \qquad m_2'\left(0\right) = 6 + 1 = 7, \qquad m_3'\left(0\right) = 19 + 3\left(6\right)\left(1\right) + 1 = 38,
$$

$$
m_4'\left(0\right) = 42 + 4\left(19\right)\left(1\right) + 6\left(6\right)\left(1\right) + 1 = 42 + 76 + 36 + 1 = 155 .
$$

Step 8 (1 mark). Check the translation in the reverse direction. Returning from the origin 5 to the mean should reproduce $m_3 = 19$, and indeed $-117 - 3\left(-4\right)\left(22\right) + 2\left(-4\right)^{3} = -117 + 264 - 128 = 19$.

Step 9 (2 marks). Test whether the moments are realisable. The coefficients would be $\beta_1 = 19^{2}/6^{3} = 1.671$ and $\beta_2 = 42/6^{2} = 1.167$, and Pearson's inequality requires $\beta_2 \ge \beta_1 + 1 = 2.671$, which fails. These four numbers are therefore an algebraic exercise and not the moment set of any real data; the translation has been performed correctly, but no shape interpretation should be attached.

### 4.7 Problem: model solution four, a short theory question with two data sets

Two data sets are given. The first is $2, 4, 6, 8, 10$ and the second is $-10$ followed by eight zeros and then $10$. Show that both have zero moment skewness, compute the coefficient of kurtosis for each, and explain what the comparison shows about the relationship between the two coefficients.

### 4.8 Solution: use symmetry, then compute the fourth moment

Step 1 (2 marks). Prove that both data sets are symmetric about their means. The first is spaced evenly at intervals of two around the value six, so every observation at $6 - h$ is matched by one at $6 + h$. The second consists of a pair at equal distances sixteen units apart with eight observations at the centre, so every observation at $0 - h$ is matched by one at $0 + h$.

Step 2 (2 marks). Quote the symmetry result. A symmetric distribution has every odd central moment equal to zero, so $m_3 = 0$ for both sets, and hence $\beta_1 = \gamma_1^{2} = 0$ for both.

Step 3 (3 marks). Compute the second and fourth central moments of the first set. The mean is six.

| $x$ | $x - 6$ | squared | fourth power |
|---|---|---|---|
| 2 | $-4$ | 16 | 256 |
| 4 | $-2$ | 4 | 16 |
| 6 | $0$ | 0 | 0 |
| 8 | $2$ | 4 | 16 |
| 10 | $4$ | 16 | 256 |
| Total | $0$ | $40$ | $544$ |

$$
m_2 = \frac{40}{5} = 8, \qquad m_4 = \frac{544}{5} = 108.8, \qquad \beta_2 = \frac{108.8}{64} = 1.70 .
$$

Step 4 (3 marks). Compute the second and fourth central moments of the second set. The mean is zero.

$$
m_2 = \frac{100 + 100}{10} = 20, \qquad m_4 = \frac{10000 + 10000}{10} = 2000, \qquad \beta_2 = \frac{2000}{400} = 5.00 .
$$

Step 5 (2 marks). Classify both. The first set has $\beta_2 = 1.70$, well below three, so it is strongly platykurtic: the values are spread evenly in a bounded band with no tail at all. The second set has $\beta_2 = 5.00$, well above three, so it is strongly leptokurtic: eight observations sit exactly at the centre and two sit far away.

Step 6 (2 marks). Draw the conclusion. Both distributions have identical skewness, namely zero, but their kurtosis coefficients differ by a factor of almost three. Skewness records the balance of the two sides, while kurtosis records how the mass is divided between the centre and the extremes. Neither coefficient can be inferred from the other, and a complete description of shape must report both.

Step 7 (1 mark). Check consistency. Each value satisfies $\beta_2 \ge 1$, and each satisfies $\beta_2 \ge \beta_1 + 1$ with $\beta_1 = 0$, since $1.70$ and $5.00$ both exceed one.

## 5. Mathematical Extensions, Limits, and Common Errors

Marks in this topic are lost in a small number of predictable places, and almost all of them are curable by routine. This section names the traps, supplies counter-measures, extends the theory to the questions that appear in later parts of a paper, and closes with a revision programme and a time plan.

### 5.1 The four classic traps, in detail

The first trap is the sign error in an odd moment. Only the odd columns can carry a sign error that survives the arithmetic, because a wrong sign in an even column is impossible: an even power of a negative number is positive. The practical safeguard is to check the sign of the total in the $fd$ and $fd^{3}$ columns against the shape of the table before dividing by $n$. If most of the frequency sits on the left of the assumed origin, the total of $fd$ must be positive and the first working moment must be positive. If the table has a long right tail, the total of $fd^{3}$ must be positive. A total that contradicts the shape means a sign has been dropped in one row.

The second trap is confusing raw and central moments. The prime is small and easy to overlook, and the consequence is severe: $\beta_1 = \left(m_3'\right)^{2}/\left(m_2'\right)^{3}$ is not a shape coefficient at all, since it changes when the assumed origin changes. The safeguard is procedural: write the conversion step explicitly, with the numbers substituted, before forming any coefficient. A script that shows $m_3 = m_3' - 3m_1'm_2' + 2\left(m_1'\right)^{3}$ and then substitutes cannot fall into this trap.

The third trap is forgetting that excess kurtosis subtracts three. A distribution with $\beta_2 = 3.2$ is leptokurtic but its excess kurtosis is only $0.2$. Reporting $3.2$ as the excess value exaggerates the departure sixteen-fold in the excess scale, and describing $3.2$ as "very high kurtosis" misrepresents a distribution that is barely distinguishable from normal in its tails. The safeguard is to state explicitly which convention is in use before quoting a number.

The fourth trap is reversing leptokurtic and platykurtic. The words describe the peak: leptokurtic curves are peaked, platykurtic curves are flat. Heavy tails accompany a peaked centre because a distribution that puts mass both very near the mean and very far from it has a large fourth moment, while a distribution that spreads mass evenly in a band has a small one. The safeguard is to attach the tail description to the name whenever it is used, so that a slip in one word is caught by the other.

### 5.2 Shortcuts that save time without losing rigour

Symmetry is the most valuable shortcut. If the frequency table is symmetric about a central value, choosing that value as the assumed origin makes every odd column cancel, so $m_1' = 0$ and $m_3' = 0$, and the conversion then gives $m_1 = m_3 = 0$ without any further arithmetic. The same observation justifies writing $\beta_1 = 0$ immediately.

Coding is the second shortcut. Choosing $A$ as a class mark and $c$ as the class width turns every deviation into a single-digit integer, so the powers can be computed mentally. The cost is a final multiplication by $c^{2}$, $c^{3}$ or $c^{4}$, which must not be forgotten; the benefit is that the arithmetic in the table becomes almost free of error.

The third shortcut is the general translation identity, which replaces the memorised formulas when a question moves from one origin to another. With $\delta = \bar{x} - A$, the moments about $A$ are obtained from the central moments by

$$
m_r' = \sum_{j=0}^{r}\binom{r}{j}m_j\delta^{r-j},
$$

so a question that supplies central moments and asks for moments about an arbitrary point is answered in one line per order. Reversing the roles of $\delta$ gives the conversion in the other direction.

### 5.3 Extensions: grouping corrections, sampling and cumulants

Grouping continuous data introduces a rounding error of up to half a class width, and the variance computed from class marks exceeds the true variance by approximately $c^{2}/12$. The corrected value is

$$
s^{2}_{\text{corrected}} = s^{2}_{\text{grouped}} - \frac{c^{2}}{12},
$$

and the correction matters when the class width is a substantial fraction of the standard deviation. The same phenomenon affects the third and fourth moments, though the corrections are more complicated and are rarely applied by hand.

Sampling introduces a second kind of error. The moments defined here divide by $n$ and describe the data in hand; estimators of population moments require bias corrections, the simplest being the divisor $n - 1$ for the variance. The standardised coefficients are also noisy: for a normal population the sample skewness has standard error about $\sqrt{6/n}$ and the sample excess kurtosis about $\sqrt{24/n}$, so with a hundred observations values of $0.2$ and $0.4$ respectively are entirely consistent with normality.

Cumulants provide the elegant extension. The cumulant generating function is the logarithm of the moment generating function, its coefficients are the cumulants, and the first four are $\kappa_1 = \bar{x}$, $\kappa_2 = m_2$, $\kappa_3 = m_3$ and $\kappa_4 = m_4 - 3m_2^{2}$. The fourth cumulant is the numerator of the excess kurtosis, and every cumulant of order three and above vanishes for the normal distribution, which is the deepest reason the normal curve serves as the reference for shape.

### 5.4 Revision checklist

- Write the four definitions from memory: moment about zero, central moment, working moment, standardised coefficient.
- Write the three conversion identities with the correct coefficient sequences and no hesitation.
- State the meaning of $m_1$, $m_2$, $m_3$ and $m_4$ in one sentence each.
- State the normal benchmarks $\beta_1 = 0$, $\beta_2 = 3$, $\gamma_2 = 0$ and the three shape names.
- Derive the second identity from first principles in under two minutes.
- Derive the third identity, including the combination of the two cubic terms.
- Compute a full grouped table, from class marks to coefficients, in under twenty-five minutes.
- Convert between origins using the general identity, in both directions.
- Apply the three consistency checks to every computed set of coefficients.
- Reproduce the two standard counterexamples: a symmetric distribution with $\beta_1 = 0$ and $\beta_2 \ne 3$, and an asymmetric distribution with $m_3 \approx 0$.
- Explain in one sentence why the mean minimises the average squared deviation.
- Explain in one sentence why the fourth moment is more sensitive to outliers than the second.

### 5.5 Time strategy in the examination

For a frequency-table question, spend the first third of the allotted time on the table and its totals, because everything downstream depends on them. Spend the second third on the conversions and the coefficients, writing each substitution explicitly so that method marks are secured even if the arithmetic slips. Spend the last few minutes on the checks and the interpretation, which are the cheapest marks on the page.

For a translation question, the allocation is different: the arithmetic is short, so most of the time should go on writing the general identity and substituting carefully, since a sign error in $\delta^{r-j}$ propagates through every subsequent order.

For a theory question, answer in the examiner's vocabulary: define, state, then illustrate with a one-line example. Definitions earn the first mark, the statement of the property earns the second, and the illustration earns the third.

### 5.6 Final checks before the script is handed in

Check that the first central moment is written as zero. Check that the second and fourth central moments are positive. Check that $\beta_1$ is non-negative and that $\beta_2$ exceeds both one and $\beta_1 + 1$. Check that the sign of $m_3$ agrees with the shape of the frequency table, with the mean versus median comparison, and with any skewness coefficient computed elsewhere in the same question. Check that every coded moment has been multiplied by the correct power of the class width. Check that each quoted coefficient is accompanied by a sentence naming the direction and the tail weight. Any one of these checks takes seconds and each of them has saved a mark on countless scripts.
