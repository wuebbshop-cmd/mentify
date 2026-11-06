## 1. Foundational Concepts, Definitions, and Axioms

### 1.1 A seesaw, a set of weights, and a pivot

Imagine a long wooden plank balanced on a single pivot. Two children of equal weight sit at equal distances on opposite sides, and the plank stays level. If one child is heavier, the plank tips towards that child. The tipping effect of each child depends on two things at once: how heavy the child is, and how far from the pivot the child sits. Move a child twice as far away and the tipping effect doubles. Put twice the weight at the same spot and the tipping effect also doubles. That combined quantity, weight multiplied by distance, is what engineers call a moment.

Now think of a set of examination marks instead of children. Each mark is like a weight. The pivot is a reference value that we choose, most often the average. The distance of a mark from the pivot is how far that mark sits above or below the reference. A statistical moment takes those distances, raises each one to a chosen power, and averages the results. That is the whole idea, and the only new ingredient compared with the seesaw is the power.

Why raise to a power at all? Because each power turns the same raw material, the distances, into a different kind of summary.

- Power one keeps the sign of each distance, so it tells us whether the data are balanced about the pivot.
- Power two removes the sign, so it tells us how far the data spread out, without caring which side.
- Power three keeps the sign but magnifies the far values, so it tells us whether the data lean to one side.
- Power four removes the sign again and magnifies the far values even more, so it tells us how much weight sits in the extremes.

Picture a description of a person. You might give their height, which is a size; their posture, which is a lean; and their build, whether they are heavy or light at the edges. Moments do exactly these three jobs for a set of numbers. The second moment gives the size of the spread, the third gives the lean, and the fourth gives the weight at the edges.

Where the seesaw picture stops being exact: a seesaw only balances or tips, while moments produce precise numbers that can be compared between data sets of different sizes and different units. The intuition of weight times distance, however, carries over without loss.

One thing must be decided before anything can be computed: where the pivot sits. We may measure distances from zero, from any convenient value we choose, or from the mean. Distances from the mean turn out to be the most useful, because they do not depend on where the data happen to sit on the number line.

### 1.2 The three reference points

There are three families of moments, and they differ only in the pivot.

The first family measures distances from zero. These are called moments about zero, or raw moments, and they are convenient for algebra but depend on the units and the location of the data.

The second family measures distances from an arbitrary chosen value, usually a round number near the middle of the data. These are called moments about an assumed origin, or working moments, and they exist because subtracting a convenient round number by hand is much easier than subtracting an awkward mean.

The third family measures distances from the arithmetic mean. These are called central moments, and they are the ones that describe shape, because moving all the data along the number line leaves them unchanged.

A single word of notation keeps the three apart. A dash, called a prime, marks a moment about an assumed origin. No dash means a moment about the mean. The prime is not decoration; it changes the meaning completely.

### 1.3 The symbols used in this unit

- $x$ is a single observation, and $x_i$ is the $i$-th observation.
- $n$ is the total number of observations, or the total frequency for grouped data.
- $f_i$ is the frequency of the $i$-th value or class.
- $\bar{x}$ is the arithmetic mean.
- $A$ is the assumed origin, a convenient round value.
- $d_i = x_i - A$ is the deviation of an observation from the assumed origin.
- $c$ is the class width for grouped data with equal classes.
- $u_i = d_i/c$ is the coded deviation, a small whole number when $A$ is a class mark.
- $m_r$ is the $r$-th moment about the mean.
- $m_r'$ is the $r$-th moment about the assumed origin.
- $\beta_1$ and $\beta_2$ are the standardised coefficients built from the third and fourth central moments.

The index $r$ is called the order of the moment. The order tells you which power is being used, and therefore which feature of the data the moment describes.

### 1.4 Working rules taken for granted

> **Axiom (Signed distances cancel about the mean).** The distances of the observations from their arithmetic mean always add up to zero.

This is why the first central moment is always zero, and it is why an average of signed distances carries no information about spread. To describe spread, the signs must be removed, either by squaring or by taking absolute values.

> **Axiom (Powers magnify distance).** Raising a distance to a higher power makes large distances count far more than small ones.

A distance of ten becomes a hundred at the second power, a thousand at the third and ten thousand at the fourth. A distance of two becomes four, eight and sixteen. The ratio between the two is multiplied by five at every step, which is why the third and fourth moments are dominated by the few observations furthest from the mean.

> **Axiom (The mean is the balance point of squared distances).** Among all possible reference points, the mean minimises the average of the squared distances.

This is the statistical version of the seesaw. The mean is the pivot at which the squared distances are as small as they can be, which is precisely why the second moment about the mean is the smallest second moment available and why it deserves the name variance.

## 2. Theorems, Lemmas, and Analytical Properties

### 2.1 Moments about zero

> **Definition (Moment about zero).** For observations $x_1, x_2, \dots, x_n$, the $r$-th moment about zero is

$$
\bar{x^{r}} = \frac{x_1^{r} + x_2^{r} + \dots + x_n^{r}}{n} = \frac{1}{n}\sum_{i=1}^{n} x_i^{r} .
$$

The symbol $\sum$ means "add up over all observations", and the division by $n$ turns the total into an average. For $r = 1$ the definition returns the arithmetic mean itself.

$$
\bar{x^{1}} = \frac{1}{n}\sum_{i=1}^{n} x_i = \bar{x} .
$$

For $r = 2$ it returns the average of the squares.

$$
\bar{x^{2}} = \frac{1}{n}\sum_{i=1}^{n} x_i^{2} .
$$

The second moment about zero is closely related to the variance but is not the variance. The difference is the square of the mean, as the conversion identity below shows.

### 2.2 Moments about the mean: the central moments

> **Definition (Central moment).** The $r$-th moment about the mean is

$$
m_r = \frac{1}{n}\sum_{i=1}^{n}\left(x_i - \bar{x}\right)^{r} .
$$

Three of these four moments carry the entire interpretation of this unit.

The first central moment is always zero, because the signed distances from the mean cancel exactly.

$$
m_1 = \frac{1}{n}\sum_{i=1}^{n}\left(x_i - \bar{x}\right) = 0 .
$$

The second central moment is the variance, the average of the squared distances. Its positive square root is the standard deviation.

$$
m_2 = \frac{1}{n}\sum_{i=1}^{n}\left(x_i - \bar{x}\right)^{2} = s^{2} .
$$

The third central moment measures the direction of lean, because the cube keeps the sign of each distance while magnifying the distant ones. A positive value means the large positive distances win, which happens when the distribution has a long right tail. A negative value means a long left tail. A value of zero is consistent with symmetry.

The fourth central moment measures the weight of the extremes, because the fourth power removes the sign and magnifies the distant values even more strongly than the cube.

### 2.3 Moments about an arbitrary value

> **Definition (Moment about an assumed origin).** For a chosen value $A$, the $r$-th moment about $A$ is

$$
m_r' = \frac{1}{n}\sum_{i=1}^{n}\left(x_i - A\right)^{r} = \frac{1}{n}\sum_{i=1}^{n} d_i^{r}, \qquad d_i = x_i - A .
$$

The first such moment has a special meaning that makes all the arithmetic worthwhile. Because the average of $x_i - A$ is the average of $x_i$ minus $A$, we obtain a direct route back to the mean.

$$
m_1' = \bar{x} - A, \qquad \text{so} \qquad \bar{x} = A + m_1' .
$$

Choosing $A$ equal to a convenient round number therefore lets the mean be recovered by one division and one addition, with no long arithmetic.

### 2.4 Moments for grouped data

When the values are summarised by frequencies, each value's contribution is repeated as many times as its frequency, and the whole sum is divided by the total frequency rather than by the number of distinct values.

$$
m_r' = \frac{1}{n}\sum_{i=1}^{k} f_i\left(x_i - A\right)^{r}, \qquad n = \sum_{i=1}^{k} f_i .
$$

The moment about zero takes the analogous form.

$$
\bar{x^{r}} = \frac{1}{n}\sum_{i=1}^{k} f_i x_i^{r} .
$$

The divisor is always the total frequency $n$, never the number of classes $k$. This is the first trap in the topic, because dividing by $k$ produces numbers that look plausible and are completely wrong.

### 2.5 Coded moments for grouped data

When the classes have a common width $c$ and the assumed origin is one of the class marks, every deviation is a whole number of class widths.

$$
d_i = x_i - A = c\,u_i .
$$

Substituting into the definition and using the fact that the constant $c^{r}$ can be taken outside the sum gives the coding rule.

$$
m_r' = \frac{1}{n}\sum_{i=1}^{k} f_i\left(c\,u_i\right)^{r} = c^{r}\left(\frac{1}{n}\sum_{i=1}^{k} f_i u_i^{r}\right) .
$$

In practice the small integer column $fu^{r}$ is totalled first, then divided by $n$, then multiplied by $c^{r}$. The power of $c$ must match the order of the moment, so the third moment is multiplied by $c^{3}$ and the fourth by $c^{4}$.

### 2.6 The conversion identities

> **Theorem (Conversion from working moments to central moments).**

$$
m_1 = 0, \qquad m_2 = m_2' - \left(m_1'\right)^{2},
$$

$$
m_3 = m_3' - 3m_1'm_2' + 2\left(m_1'\right)^{3},
$$

$$
m_4 = m_4' - 4m_1'm_3' + 6\left(m_1'\right)^{2}m_2' - 3\left(m_1'\right)^{4} .
$$

These four equations are the working heart of the topic. They say that a moment computed about a convenient point can be corrected into a moment about the mean, and the correction depends only on how far the assumed origin sits from the mean. The derivations are given in Section 3, and the pattern of coefficients is worth memorising: one and minus one for the second moment; one, minus three and plus two for the third; one, minus four, plus six and minus three for the fourth.

### 2.7 The standardised coefficients

The third and fourth central moments carry units, so they cannot be compared between data sets. Dividing each by an appropriate power of the standard deviation removes the units.

> **Definition (Moment coefficients).**

$$
\beta_1 = \frac{m_3^{2}}{m_2^{3}}, \qquad \gamma_1 = \frac{m_3}{m_2^{\frac{3}{2}}}, \qquad \beta_2 = \frac{m_4}{m_2^{2}}, \qquad \gamma_2 = \beta_2 - 3 .
$$

The coefficient of skewness is the squared third moment divided by the cube of the variance; its signed version keeps the direction. The coefficient of kurtosis is the fourth moment divided by the square of the variance; its excess version subtracts three so that the normal curve sits at zero.

The values to remember are these. A symmetric distribution has $\beta_1 = 0$. The normal curve has $\beta_2 = 3$ and $\gamma_2 = 0$. A distribution more peaked than normal has $\beta_2$ above three and is called leptokurtic. A distribution flatter than normal has $\beta_2$ below three and is called platykurtic.

### 2.8 What each moment is for

| Order | Central moment | Value for a typical data set | What it tells you |
|---|---|---|---|
| 1 | $m_1$ | always $0$ | nothing; it is a check on the arithmetic |
| 2 | $m_2$ | positive, in squared units | the variance, hence the spread |
| 3 | $m_3$ | signed, in cubed units | the direction and size of the lean |
| 4 | $m_4$ | positive, in fourth-power units | the weight of the extremes |

The first moment is included in the table only because it must be computed and reported. It is the one moment that never varies, and a non-zero value is proof of an error rather than a discovery.

### 2.9 Why the mean, and no other point, is the natural pivot

> **Lemma (The mean minimises squared distance).** Among all constants $c$, the average of the squared distances $\frac{1}{n}\sum\left(x_i - c\right)^{2}$ is smallest when $c = \bar{x}$, and the minimum value is the variance.

This lemma explains why the second central moment deserves the special name of variance, and why the conversion identity always subtracts rather than adds. Any second moment computed about a point other than the mean is too large, and the excess is exactly the square of the distance from that point to the mean. Choosing a convenient working origin therefore costs nothing in the end, because the correction puts the excess back.

The lemma also shows that the mean is the analogue of the pivot in the seesaw. Just as the balance point is the place where the plank sits level, the mean is the place where the average squared distance is as small as possible. Move the pivot away and the plank tips; move the reference point away from the mean and every second moment grows.

## 3. Formal Proofs, Derivations, and Methods

### 3.1 Why the first central moment is always zero

Write the definition and split the sum into two parts.

$$
m_1 = \frac{1}{n}\sum_{i=1}^{n}\left(x_i - \bar{x}\right) = \frac{1}{n}\sum_{i=1}^{n} x_i - \frac{1}{n}\sum_{i=1}^{n}\bar{x} .
$$

The first term is the mean itself by definition. The second term is a constant added $n$ times and then divided by $n$, so it is also the mean.

$$
m_1 = \bar{x} - \frac{n\bar{x}}{n} = \bar{x} - \bar{x} = 0 .
$$

The same argument works for grouped data, with $n = \sum f_i$ replacing the count. This is the formal statement that the mean is the balance point of the signed distances.

### 3.2 Deriving the second conversion identity

Start from the definition and write the distance from the mean as a difference of two distances from the assumed origin.

$$
x_i - \bar{x} = \left(x_i - A\right) - \left(\bar{x} - A\right) .
$$

Square both sides, using the expansion of a squared difference.

$$
\left(x_i - \bar{x}\right)^{2} = \left(x_i - A\right)^{2} - 2\left(x_i - A\right)\left(\bar{x} - A\right) + \left(\bar{x} - A\right)^{2} .
$$

Average both sides over all observations, noting that the constant $\left(\bar{x} - A\right)$ passes through the averaging.

$$
m_2 = \frac{1}{n}\sum_{i=1}^{n}\left(x_i - A\right)^{2} - 2\left(\bar{x} - A\right)\frac{1}{n}\sum_{i=1}^{n}\left(x_i - A\right) + \left(\bar{x} - A\right)^{2} .
$$

Recognise the working moments in the first two terms, and note that the third term is a constant averaged over $n$ observations, which is itself.

$$
m_2 = m_2' - 2\left(\bar{x} - A\right)m_1' + \left(\bar{x} - A\right)^{2} .
$$

Finally use the first-moment identity $m_1' = \bar{x} - A$ and collect the last two terms.

$$
m_2 = m_2' - 2\left(m_1'\right)^{2} + \left(m_1'\right)^{2} = m_2' - \left(m_1'\right)^{2} .
$$

The correction is the square of the distance between the mean and the assumed origin, and it is always subtracted. A common error is to add it.

### 3.3 Deriving the third conversion identity

The same substitution is used, with the cube of a difference.

$$
\left(x_i - \bar{x}\right)^{3} = \left(x_i - A\right)^{3} - 3\left(x_i - A\right)^{2}\left(\bar{x} - A\right) + 3\left(x_i - A\right)\left(\bar{x} - A\right)^{2} - \left(\bar{x} - A\right)^{3} .
$$

Averaging gives four terms.

$$
m_3 = m_3' - 3\left(\bar{x} - A\right)m_2' + 3\left(\bar{x} - A\right)^{2}m_1' - \left(\bar{x} - A\right)^{3} .
$$

Substituting $m_1' = \bar{x} - A$ turns the last two terms into cubes of the same quantity.

$$
m_3 = m_3' - 3m_1'm_2' + 3\left(m_1'\right)^{3} - \left(m_1'\right)^{3} = m_3' - 3m_1'm_2' + 2\left(m_1'\right)^{3} .
$$

Two cubes combine into one, which is where the coefficient two comes from. This is the single most commonly misremembered line in the topic.

### 3.4 Deriving the fourth conversion identity

The fourth power of a difference expands to five terms.

$$
\left(x_i - \bar{x}\right)^{4} = \left(x_i - A\right)^{4} - 4\left(x_i - A\right)^{3}\left(\bar{x} - A\right) + 6\left(x_i - A\right)^{2}\left(\bar{x} - A\right)^{2} - 4\left(x_i - A\right)\left(\bar{x} - A\right)^{3} + \left(\bar{x} - A\right)^{4} .
$$

Averaging and substituting the working moments gives

$$
m_4 = m_4' - 4m_1'm_3' + 6\left(m_1'\right)^{2}m_2' - 4\left(m_1'\right)^{4} + \left(m_1'\right)^{4} ,
$$

and the last two terms combine.

$$
m_4 = m_4' - 4m_1'm_3' + 6\left(m_1'\right)^{2}m_2' - 3\left(m_1'\right)^{4} .
$$

The pattern of coefficients is one, minus four, plus six and minus three. The same technique with the fifth and sixth powers produces the fifth and sixth identities, though those are rarely required.

### 3.5 Proving that the mean minimises the squared distances

Write the average squared distance about an arbitrary constant $c$ and add and subtract the mean inside the bracket.

$$
\frac{1}{n}\sum_{i=1}^{n}\left(x_i - c\right)^{2} = \frac{1}{n}\sum_{i=1}^{n}\left\{\left(x_i - \bar{x}\right) + \left(\bar{x} - c\right)\right\}^{2} .
$$

Expanding the square produces three terms.

$$
\frac{1}{n}\sum_{i=1}^{n}\left(x_i - c\right)^{2} = \frac{1}{n}\sum_{i=1}^{n}\left(x_i - \bar{x}\right)^{2} + 2\left(\bar{x} - c\right)\frac{1}{n}\sum_{i=1}^{n}\left(x_i - \bar{x}\right) + \left(\bar{x} - c\right)^{2} .
$$

The middle term vanishes because the average of the deviations from the mean is zero, and the first term is the variance by definition.

$$
\frac{1}{n}\sum_{i=1}^{n}\left(x_i - c\right)^{2} = s^{2} + \left(\bar{x} - c\right)^{2} .
$$

The right-hand side is a sum of two non-negative terms, and the second is zero exactly when $c = \bar{x}$. The minimum value is therefore $s^{2}$, attained at the mean, and any other choice of $c$ increases the average squared distance by $\left(\bar{x} - c\right)^{2}$. This is precisely the correction term that the conversion identity subtracts.

### 3.6 Method: six steps for any moment question

1. Decide whether the data are ungrouped, grouped with equal widths, or grouped with unequal widths.
2. Choose the assumed origin $A$. For grouped data choose a class mark near the middle; for ungrouped data choose a round value near the mean.
3. Build the columns of deviations, then of $fd$, $fd^{2}$, $fd^{3}$ and, if kurtosis is required, $fd^{4}$. Total every column.
4. Divide each total by $n$ to obtain $m_1'$ to $m_4'$. Verify that $m_1'$ equals the mean minus $A$.
5. Apply the conversion identities in order, from the second moment upwards, since each depends on the earlier ones.
6. If coefficients are required, divide by the appropriate power of $m_2$ and interpret the sign of $m_3$.

## 4. Representative Worked Examples and Solutions

### 4.1 Problem: the four moments of five small numbers

Compute the first four moments about the mean for the observations 2, 4, 6, 8 and 10, using the assumed origin $A = 3$.

### 4.2 Solution: one table, four conversions

Step 1. Compute the deviations from the assumed origin.

| $x$ | $d = x - 3$ | $d^{2}$ | $d^{3}$ | $d^{4}$ |
|---|---|---|---|---|
| 2 | $-1$ | 1 | $-1$ | 1 |
| 4 | $1$ | 1 | $1$ | 1 |
| 6 | $3$ | 9 | $27$ | 81 |
| 8 | $5$ | 25 | $125$ | 625 |
| 10 | $7$ | 49 | $343$ | 2401 |
| Total | $15$ | $85$ | $495$ | $3109$ |

Step 2. Divide each total by $n = 5$.

$$
m_1' = \frac{15}{5} = 3, \qquad m_2' = \frac{85}{5} = 17, \qquad m_3' = \frac{495}{5} = 99, \qquad m_4' = \frac{3109}{5} = 621.8 .
$$

Step 3. Recover the mean from the first working moment.

$$
\bar{x} = A + m_1' = 3 + 3 = 6,
$$

which agrees with direct inspection, since the five numbers are evenly spaced.

Step 4. Convert to the second central moment.

$$
m_2 = 17 - 3^{2} = 17 - 9 = 8 .
$$

Step 5. Convert to the third central moment.

$$
m_3 = 99 - 3(3)(17) + 2(3)^{3} = 99 - 153 + 54 = 0 .
$$

Step 6. Convert to the fourth central moment.

$$
m_4 = 621.8 - 4(3)(99) + 6(3)^{2}(17) - 3(3)^{4} = 621.8 - 1188 + 918 - 243 = 108.8 .
$$

Step 7. Form the coefficients.

$$
\beta_1 = \frac{0^{2}}{8^{3}} = 0, \qquad \beta_2 = \frac{108.8}{8^{2}} = \frac{108.8}{64} = 1.7 .
$$

Step 8. Interpret. The third moment is zero, which is expected because the five numbers are symmetric about six. The coefficient of kurtosis of $1.7$ is well below three, so the distribution is strongly platykurtic: it has no tail at all, because all five values lie within four units of the mean. The conversion from an assumed origin of three has nevertheless produced exactly the same moments as a direct computation about the mean.

### 4.3 Problem: an asymmetric set of four numbers

Compute the four central moments for the observations 1, 2, 3 and 10, using the assumed origin $A = 2$, and interpret the third moment.

### 4.4 Solution: the conversion recovers a non-zero third moment

Step 1. Build the table of deviations and powers.

| $x$ | $d = x - 2$ | $d^{2}$ | $d^{3}$ | $d^{4}$ |
|---|---|---|---|---|
| 1 | $-1$ | 1 | $-1$ | 1 |
| 2 | $0$ | 0 | $0$ | 0 |
| 3 | $1$ | 1 | $1$ | 1 |
| 10 | $8$ | 64 | $512$ | 4096 |
| Total | $8$ | $66$ | $512$ | $4098$ |

Step 2. Divide each total by $n = 4$.

$$
m_1' = 2, \qquad m_2' = 16.5, \qquad m_3' = 128, \qquad m_4' = 1024.5 .
$$

Step 3. Recover the mean.

$$
\bar{x} = 2 + 2 = 4 .
$$

Step 4. Convert the second moment.

$$
m_2 = 16.5 - 2^{2} = 16.5 - 4 = 12.5 .
$$

Step 5. Convert the third moment.

$$
m_3 = 128 - 3(2)(16.5) + 2(2)^{3} = 128 - 99 + 16 = 45 .
$$

Step 6. Convert the fourth moment.

$$
m_4 = 1024.5 - 4(2)(128) + 6(2)^{2}(16.5) - 3(2)^{4} = 1024.5 - 1024 + 396 - 48 = 348.5 .
$$

Step 7. Form the coefficients.

$$
\beta_1 = \frac{45^{2}}{12.5^{3}} = \frac{2025}{1953.125} = 1.037, \qquad \beta_2 = \frac{348.5}{12.5^{2}} = \frac{348.5}{156.25} = 2.230 .
$$

Step 8. Interpret. The third moment is positive, so the distribution leans to the right, which is exactly what the single value of ten does among values of one, two and three. The coefficient of skewness of $1.037$ is large, reflecting a genuinely lopsided set, and the coefficient of kurtosis of $2.230$ is below three, so the distribution is platykurtic in the fourth-moment sense even though it has one far value; the single outlier is not enough to make the fourth moment large relative to the square of the variance.

### 4.5 Problem: the four moments of a grouped frequency table

A distribution of a discrete variable has the following frequencies.

| $x$ | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
|---|---|---|---|---|---|---|---|---|---|
| $f$ | 1 | 8 | 28 | 56 | 70 | 56 | 28 | 8 | 1 |

Compute the first four moments about the mean and the coefficient of kurtosis.

### 4.6 Solution: use the symmetry and the centre as the origin

Step 1. Choose $A = 4$, the middle value, and build the working table with $d = x - 4$.

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

Step 2. Divide each total by $n = 256$.

$$
m_1' = \frac{0}{256} = 0, \qquad m_2' = \frac{512}{256} = 2, \qquad m_3' = \frac{0}{256} = 0, \qquad m_4' = \frac{2816}{256} = 11 .
$$

Step 3. Apply the conversion identities. Because the first working moment is zero, every correction term disappears.

$$
m_2 = 2 - 0 = 2, \qquad m_3 = 0 - 0 + 0 = 0, \qquad m_4 = 11 - 0 + 0 - 0 = 11 .
$$

Step 4. State the first four moments about the mean.

$$
m_1 = 0, \qquad m_2 = 2, \qquad m_3 = 0, \qquad m_4 = 11 .
$$

Step 5. Compute the coefficient of kurtosis.

$$
\beta_2 = \frac{11}{2^{2}} = \frac{11}{4} = 2.75 .
$$

Step 6. Interpret. The mean is four by symmetry, the variance is two so the standard deviation is about $1.41$, the third moment is zero so the distribution is symmetric, and the coefficient of kurtosis of $2.75$ is below three, so the distribution is platykurtic and its tails are lighter than those of a normal curve.

### 4.7 Problem: recovering the moments about the mean from moments about a point

The first four moments of a distribution about the value 5 are 2, 20, 40 and 50. Find the mean and the first four moments about the mean.

### 4.8 Solution: read the shift off the first moment, then convert

Step 1. Use the first working moment to find the mean.

$$
m_1' = \bar{x} - A \quad \text{gives} \quad 2 = \bar{x} - 5, \quad \text{so} \quad \bar{x} = 7 .
$$

Step 2. Convert the second moment.

$$
m_2 = 20 - 2^{2} = 20 - 4 = 16 .
$$

Step 3. Convert the third moment.

$$
m_3 = 40 - 3(2)(20) + 2(2)^{3} = 40 - 120 + 16 = -64 .
$$

Step 4. Convert the fourth moment.

$$
m_4 = 50 - 4(2)(40) + 6(2)^{2}(20) - 3(2)^{4} = 50 - 320 + 480 - 48 = 162 .
$$

Step 5. State the answer.

$$
m_1 = 0, \qquad m_2 = 16, \qquad m_3 = -64, \qquad m_4 = 162 .
$$

Step 6. Comment on the sign. The third moment is negative, which tells us that the distribution leans to the left, even though the mean of seven lies above the assumed origin of five. The two facts are unrelated: the shift of the origin moves every moment, while the sign of the third central moment is a property of the shape alone.

Step 7. Note on the numbers. These four values are chosen to exercise the algebra, and they are not the moments of any real data set, because a genuine set of moments must satisfy $\beta_2 \ge 1$ whereas the ratio here would be $162/256$. Whenever moments are quoted in an exercise, the arithmetic can be checked but the shape cannot necessarily be classified.

### 4.9 Problem: moments of a grouped table with coding

A distribution of marks is grouped in classes of width ten.

| Class | 0–9 | 10–19 | 20–29 | 30–39 |
|---|---|---|---|---|
| Frequency | 5 | 12 | 20 | 3 |

Compute the mean, the four central moments and both shape coefficients using coded values.

### 4.10 Solution: build the coded columns and restore the powers of the class width

Step 1. Take the class marks as the midpoints of the boundaries, so the marks are $4.5$, $14.5$, $24.5$ and $34.5$. Choose the assumed origin $A = 14.5$ and the class width $c = 10$, giving $u = \left(x - 14.5\right)/10$.

Step 2. Build the coded table.

| Class mark $x$ | $f$ | $u$ | $fu$ | $fu^{2}$ | $fu^{3}$ | $fu^{4}$ |
|---|---|---|---|---|---|---|
| 4.5 | 5 | $-1$ | $-5$ | 5 | $-5$ | 5 |
| 14.5 | 12 | $0$ | $0$ | 0 | 0 | 0 |
| 24.5 | 20 | $1$ | $20$ | 20 | 20 | 20 |
| 34.5 | 3 | $2$ | $6$ | 12 | 24 | 48 |
| Total | 40 | | $21$ | $37$ | $39$ | $73$ |

Step 3. Compute the mean from the first coded moment.

$$
\bar{x} = 14.5 + 10\left(\frac{21}{40}\right) = 14.5 + 5.25 = 19.75 .
$$

Step 4. Compute the coded working moments by dividing each total by $n = 40$.

$$
m_1' = 0.525, \qquad m_2' = 0.925, \qquad m_3' = 0.975, \qquad m_4' = 1.825 .
$$

Step 5. Convert to the coded central moments, then multiply by the appropriate powers of ten.

$$
m_2\left(u\right) = 0.925 - 0.525^{2} = 0.925 - 0.2756 = 0.6494,
$$

$$
m_3\left(u\right) = 0.975 - 3(0.525)(0.925) + 2(0.525)^{3} = 0.975 - 1.4569 + 0.2894 = -0.1925,
$$

$$
m_4\left(u\right) = 1.825 - 4(0.525)(0.975) + 6(0.2756)(0.925) - 3(0.525)^{4} = 1.0793 .
$$

Step 6. Restore the scale. The second moment needs $c^{2} = 100$, the third $c^{3} = 1000$ and the fourth $c^{4} = 10000$.

$$
m_2 = 100 \times 0.6494 = 64.94, \qquad m_3 = 1000 \times \left(-0.1925\right) = -192.47, \qquad m_4 = 10000 \times 1.0793 = 10793.1 .
$$

Step 7. Compute the standard deviation and the shape coefficients.

$$
s = \sqrt{64.94} = 8.06,
$$

$$
\beta_1 = \frac{\left(-192.47\right)^{2}}{64.94^{3}} = \frac{37044.7}{273857} = 0.135, \qquad \gamma_1 = \frac{-192.47}{8.06^{3}} = -0.368,
$$

$$
\beta_2 = \frac{10793.1}{64.94^{2}} = \frac{10793.1}{4216.9} = 2.560, \qquad \gamma_2 = 2.560 - 3 = -0.440 .
$$

Step 8. Interpret. The mean mark is $19.75$. The third moment is negative and $\gamma_1 = -0.368$, so the distribution leans to the left, with a modest tail of low marks. The coefficient of kurtosis of $2.560$ is below three, so the distribution is platykurtic: flatter topped and lighter tailed than a normal curve. The consistency conditions hold, since $\beta_1$ is non-negative and $2.560$ exceeds $0.135 + 1 = 1.135$. Note that the mean of $19.75$ is below the modal class mark of $24.5$, which is exactly what a left skew predicts.

## 5. Mathematical Extensions, Limits, and Common Errors

Moments are the algebra that underlies every shape measure in statistics, and the beginner's difficulty is almost never conceptual; it is the bookkeeping of primes, powers and divisors. This section extends the basic theory in the directions that later work requires and then lists the errors that recur in scripts.

### 5.1 Why the mean is the natural origin

The central moments are preferred over raw moments because they do not change when the data are shifted along the number line. If every observation is increased by a constant, the mean increases by the same constant, every deviation from the mean is unchanged, and therefore every central moment is unchanged. Raw moments, by contrast, change completely, since the first raw moment becomes the old mean plus the constant and higher raw moments change by the binomial expansion of a sum.

This invariance is what makes the variance, the third central moment and the fourth central moment genuine descriptions of shape. It is also why the conversion identities exist: they allow the convenience of a round working origin while preserving the invariance of the result.

There is a second reason for using the mean. Among all reference points, the mean minimises the average squared distance, so the second central moment is the smallest second moment that can be computed about any point. A variance computed about any other point would be larger, and the amount by which it is larger is exactly the square of the distance from that point to the mean. This is the content of the identity $m_2 = m_2' - \left(m_1'\right)^{2}$.

### 5.2 The moment generating function in plain words

A single function can store all the moments at once. It is defined as the average of an exponential.

$$
M_X\left(t\right) = E\left[e^{tX}\right] = \frac{1}{n}\sum_{i=1}^{n} e^{t x_i} .
$$

Expanding the exponential as a power series and averaging term by term gives

$$
M_X\left(t\right) = 1 + m_1'\frac{t}{1!} + m_2'\frac{t^{2}}{2!} + m_3'\frac{t^{3}}{3!} + \dots,
$$

so the $r$-th raw moment appears as the coefficient of $t^{r}/r!$. Differentiating $r$ times and setting $t = 0$ extracts it.

$$
m_r' = \left.\frac{d^{r}}{dt^{r}}M_X\left(t\right)\right|_{t=0} .
$$

A corresponding function for the central moments is obtained by multiplying by $e^{-t\bar{x}}$, which shifts the origin to the mean. The device is useful in probability theory because a distribution is determined by its moment generating function when the function exists in a neighbourhood of zero, so two distributions with the same moments must be the same distribution. It is also the shortest route to the normal result that the fourth central moment equals three times the square of the variance, which is the benchmark for kurtosis.

### 5.3 Moments beyond the fourth, and why they are rarely used

Higher moments exist and are perfectly well defined, but they are difficult to estimate and hard to interpret. Each additional order raises the power applied to the distance, so the fifth and sixth moments are dominated by a handful of extreme observations and their sample values fluctuate wildly from sample to sample. In practice the descriptive work is finished at the fourth moment, and the coefficients $\beta_1$ and $\beta_2$ are the standard summaries of shape.

Two further consistency conditions deserve mention. Every distribution with a finite fourth moment satisfies $\beta_2 \ge 1$, and it also satisfies $\beta_2 \ge \beta_1 + 1$. The first says that no distribution can be flatter than a two-point distribution; the second says that strong skewness forces heavy tails. A computed pair of coefficients that violates either condition contains an arithmetic error, which makes the pair a useful self-check.

### 5.4 Sampling and grouping effects

The moments computed above are descriptive moments: they divide by the total frequency $n$ and describe the data in hand. When the data are treated as a sample from a larger population and the aim is to estimate the population variance, the conventional divisor becomes $n - 1$, and the estimate is larger by the factor $n/\left(n - 1\right)$. The same distinction applies to the third and fourth moments, where bias corrections are more complicated and are usually left to software.

Grouping introduces a separate effect. Replacing every observation by its class mark adds a rounding error of up to half a class width, and the variance computed from class marks exceeds the true variance by approximately $c^{2}/12$, where $c$ is the class width. The correction is negligible when the class width is small compared with the standard deviation and becomes important when the classes are coarse.

### 5.5 Beginner misconceptions to eliminate

- The first central moment is not "the mean". It is zero, always, and it exists only as a check. The mean is the first moment about zero.
- The second moment about zero is not the variance. The variance is the second central moment, and the two differ by the square of the mean.
- Dividing by the number of classes instead of the total frequency is the commonest arithmetic error. The divisor is always $n = \sum f_i$.
- The prime matters. $m_3'$ is a moment about an assumed origin and $m_3$ is a moment about the mean; they are different numbers, and substituting one for the other produces nonsense.
- Forgetting the power of $c$ when using coded data produces moments that are wrong by a factor of $c^{r}$. The third moment needs $c^{3}$ and the fourth needs $c^{4}$, not $c$ or $c^{2}$.
- The correction term in the second identity is subtracted, not added. A variance larger than the second working moment is impossible.
- A zero third moment does not mean "no spread". It means symmetry. Spread is measured by the second moment, and a set of data can be widely spread and perfectly symmetric at the same time.
- A negative second moment is impossible, because it is an average of squares. A computed negative value means a sign has been lost in the conversion.
- The fourth central moment is always positive, so a negative value is always an error.
- Reporting a raw third moment as a skewness is wrong, because the raw value carries units and depends on the scale of the data. The standardised coefficient is the comparable quantity.
- The coefficient $\beta_1$ is a square and cannot be negative. The direction of skewness must be read from the sign of $m_3$, and the magnitude from $\beta_1$ or from the size of $\gamma_1$.
- Treating a set of quoted moments as necessarily coming from real data. Some quadruples of numbers satisfy the algebra but violate the consistency conditions $\beta_2 \ge 1$ and $\beta_2 \ge \beta_1 + 1$, and they cannot arise from any data set.
