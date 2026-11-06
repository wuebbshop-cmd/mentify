## 1. Foundational Concepts, Definitions, and Axioms

### 1.1 The gap that location and dispersion leave open

A measure of central tendency reduces a data set to one representative value, and a measure of dispersion reduces it to one number describing how far the observations sit from that value. Between them they answer the questions "where is the bulk of the data?" and "how widely is it spread?". They do not answer a third question that decides how the first two should be interpreted: is the spread symmetrical on the two sides of the centre? Two variables can share a mean and a standard deviation while one is balanced and the other is lopsided, and the practical consequences of that difference are large. A lopsided variable has a mean that is not a typical value, a standard deviation that is inflated by a minority of observations, and a sampling distribution of the mean that approaches normality slowly.

Skewness is the formal measure of that lopsidedness. Kurtosis is the formal measure of a different shape feature: how much of the spread is carried by the centre of the distribution and how much by the tails. The two together, with location and dispersion, form a four-part description of any distribution, and each of the four parts is computable from the same moment machinery.

### 1.2 Symmetry as a formal property

> **Definition (Symmetric distribution).** A distribution is symmetric about a value $c$ if, for every $h$, the density or relative frequency at $c - h$ equals that at $c + h$.

For a finite data set the analogous statement is that the observations can be arranged in pairs equidistant from $c$, with any unpaired observation equal to $c$ itself. The centre of symmetry $c$ is then simultaneously the mean, the median and the mode. Symmetry is a property of the whole shape, not of a summary, and it can fail in two directions.

> **Definition (Skewness).** Skewness is the degree of asymmetry of a distribution. A distribution whose longer tail extends towards the larger values is positively skewed, or skewed to the right. A distribution whose longer tail extends towards the smaller values is negatively skewed, or skewed to the left. A distribution with no asymmetry has zero skewness.

The tail is what carries the sign, and the reason is arithmetic. The bulk of a right-skewed distribution sits low, with a minority of large observations pulling the mean upward; the mean therefore exceeds the median, which exceeds the mode. The reverse holds on the left. The ordering of the three averages is not an extra assumption but a consequence of the way each average weights the data: the mean weights by magnitude, the median by rank, the mode by local frequency.

### 1.3 The five coefficients of skewness

Five coefficients are in standard use. Each standardises a difference between two location measures by a measure of scale, and each therefore carries no units.

> **Definition (Karl Pearson's first coefficient).** The first Pearson coefficient is

$$
SK_P = \frac{\bar{x} - \text{mode}}{s}.
$$

> **Definition (Karl Pearson's second coefficient).** The second Pearson coefficient replaces the mode by the median and inserts a factor of three:

$$
SK_P = \frac{3\left(\bar{x} - \text{median}\right)}{s}.
$$

> **Definition (Bowley's coefficient).** The quartile coefficient of skewness is

$$
SK_B = \frac{Q_3 + Q_1 - 2Q_2}{Q_3 - Q_1}.
$$

> **Definition (Kelly's coefficient).** The percentile coefficient of skewness is

$$
SK_K = \frac{P_{90} + P_{10} - 2P_{50}}{P_{90} - P_{10}} = \frac{D_9 + D_1 - 2\left(\text{median}\right)}{D_9 - D_1}.
$$

> **Definition (Moment coefficient).** The moment coefficient of skewness is

$$
\beta_1 = \frac{m_3^{2}}{m_2^{3}}, \qquad \gamma_1 = \frac{m_3}{m_2^{\frac{3}{2}}}.
$$

The five are not equivalent. They differ in which observations influence the answer and in the shape of the influence function: whether a distant observation counts in proportion to its distance, to the cube of its distance, or not at all. That single fact explains almost every discrepancy between them.

### 1.4 The ordering of the averages

> **Theorem (Ordering under skewness).** For a right-skewed distribution the mode is less than the median, which is less than the mean. For a left-skewed distribution the mean is less than the median, which is less than the mode.

The mechanism has three parts. The mean is a linear functional of the data, so a displacement of the largest observation by an amount $\delta$ displaces the mean by $\delta/n$ and leaves it displaced permanently. The median is an order statistic, so a displacement that does not change ranks leaves it untouched. The mode depends only on local frequency, so a displacement of a unique extreme value leaves it untouched as well. In a right-skewed distribution the extreme values are large and there are few of them, so the mean is dragged towards the large side while the other two stay put. The ordering follows.

The converse caution also belongs here. The ordering is a property of the population shape, and it can fail in small samples or in distributions with two modes of unequal height, where the unique mode is a local feature of one hump rather than a description of the whole distribution. This is one reason the median version of Pearson's coefficient exists.

### 1.5 Kurtosis, excess kurtosis, and the three shapes

> **Definition (Coefficient of kurtosis).** Kurtosis is measured by

$$
\beta_2 = \frac{m_4}{m_2^{2}}, \qquad \gamma_2 = \beta_2 - 3 .
$$

The subtraction of three in the excess form reflects the value taken by the coefficient at the normal distribution, where the fourth central moment equals three times the square of the variance.

> **Definition (Mesokurtic, leptokurtic, platykurtic).** A distribution with $\beta_2 = 3$ is mesokurtic, one with $\beta_2 > 3$ is leptokurtic and one with $\beta_2 < 3$ is platykurtic. Equivalently, $\gamma_2$ is zero, positive and negative respectively.

Leptokurtic distributions are more sharply peaked than the normal curve and carry heavier tails; platykurtic distributions are flatter on top and carry lighter tails. The two features travel together because both are consequences of where the fourth-power weight falls: a distribution that concentrates mass very near the centre and simultaneously places appreciable mass very far away has a large fourth moment, while a distribution that spreads mass evenly in a bounded band has a small one.

The beta and gamma coefficients are related by a simple algebra. For skewness, $\gamma_1 = m_3/m_2^{3/2}$ is signed and $\beta_1 = \gamma_1^{2}$ is not. For kurtosis, $\gamma_2 = \beta_2 - 3$ is signed and $\beta_2$ is not. In both cases the signed version distinguishes the two directions, and the squared or unshifted version measures only the size. A question that asks for a direction can only be answered from $\gamma_1$, $SK_P$, $SK_B$ or $SK_K$.

### 1.6 Axioms of the coefficient family

> **Axiom (Location invariance).** Adding a constant $a$ to every observation leaves every coefficient in this unit unchanged.

A shift moves the mean, the median, the mode, the quartiles and every moment about the mean in a way that cancels in each ratio: differences of location measures are unchanged, and central moments are unchanged by construction.

> **Axiom (Scale invariance).** Multiplying every observation by a positive constant $b$ leaves every coefficient unchanged; multiplying by a negative constant reverses every sign and leaves every magnitude unchanged.

A change of scale multiplies the mean, the median, the mode and the standard deviation by $b$, so each ratio is unchanged; under a negative multiplier the order of the data is reversed, so a right skew becomes a left skew.

> **Axiom (Sign preservation of odd moments).** The third central moment carries the sign of the dominant tail, because an odd power preserves the sign of each deviation.

These three axioms are what make the coefficients comparable across variables measured in different units, and they are also the fastest way to check an answer: a coefficient that changes when the units are changed has been computed wrongly.

### 1.7 What the two measures imply for practice

The first implication concerns the choice of a measure of location. Under marked skewness the mean is displaced towards the tail, so it ceases to describe a typical observation and becomes a description of the total divided by the count. The median, which is defined by rank, remains typical, and the mode remains the most common value. The rule of practice is therefore: use the mean for symmetric or nearly symmetric data, use the median for markedly skewed data, use the mode for categorical data or when the most frequent value itself matters, and report the quartiles alongside the median so that the reader learns the shape as well as the centre.

The second implication concerns normal-theory inference. Intervals and tests for a mean are built from the sampling distribution of $\bar{x}$, and their nominal coverage holds only when that sampling distribution is close to normal. Skewness makes the sampling distribution skewed in small samples, and heavy tails make convergence slow and make the standard error itself unstable. When skewness and kurtosis are large, the honest options are to increase the sample, to transform the data, or to use inference that does not require normality, such as a bootstrap or a rank-based procedure.

## 2. Theorems, Lemmas, and Analytical Properties

### 2.1 Theorem: symmetry forces every odd central moment to vanish

> **Theorem 1.** If a distribution is symmetric about its mean then $m_r = 0$ for every odd $r$.

For grouped data with values $x_i$ arranged in pairs equidistant from $\bar{x}$, each pair contributes $\left(\bar{x} - h\right)^{r} + \left(\bar{x} + h\right)^{r}$ times a common frequency. For odd $r$ the two terms are equal in magnitude and opposite in sign, so every pair vanishes, and any unpaired observation at the centre contributes zero. Therefore the whole sum vanishes and $m_3 = 0$, which forces $\beta_1 = 0$ and $\gamma_1 = 0$.

The converse is false, and the failure matters in practice. A distribution can have $m_3 = 0$ while being strongly asymmetric, provided the asymmetry is balanced in the cubed sense: a long thin right tail and a shorter thicker left shoulder can cancel in the third moment. Zero moment skewness is therefore evidence of balance in a weighted sense, not proof of mirror symmetry.

### 2.2 Theorem: the structure and range of Bowley's coefficient

> **Theorem 2.** Let $a = Q_2 - Q_1$ and $b = Q_3 - Q_2$. Then Bowley's coefficient equals $\left(b - a\right)/\left(a + b\right)$, lies in the closed interval from minus one to plus one, is zero exactly when the two half-widths are equal, and has the sign of $b - a$.

The identity follows by regrouping the numerator, and the bound follows because $a$ and $b$ are non-negative. The sign criterion follows immediately: a positive coefficient means the upper half-width exceeds the lower, which is the quartile signature of a right skew. The coefficient is invariant under any monotone increasing transformation of the data, since such a transformation moves the three quartiles without changing their order or the ratios of their spacings. That invariance is why Bowley's coefficient is the natural choice for open-ended classes and for data with extreme values.

### 2.3 Theorem: invariance and equivariance

> **Theorem 3.** For $y_i = a + b x_i$ with $b > 0$, every skewness and kurtosis coefficient in this unit is unchanged. For $b < 0$ every signed coefficient changes sign and every squared coefficient is unchanged.

Central moments transform as $m_r\left(y\right) = b^{r} m_r\left(x\right)$. Hence

$$
\beta_1\left(y\right) = \frac{b^{6} m_3^{2}}{b^{6} m_2^{3}} = \beta_1\left(x\right), \qquad \beta_2\left(y\right) = \frac{b^{4} m_4}{b^{4} m_2^{2}} = \beta_2\left(x\right),
$$

and the location differences in $SK_P$ are multiplied by $b$ in the numerator and by $\left|b\right|$ in the denominator, so the magnitude is unchanged and the sign flips exactly when $b < 0$. This is the formal justification for describing the coefficients as pure shape measures.

### 2.4 Theorem: boundedness of the Pearson coefficients

> **Theorem 4.** For any data set, $\left|SK_P\right| \le 3$ when the median version is used, and the same bound holds for the mode version under the empirical relation between the three averages.

The proof for the median version is given in Section 3. In practice the coefficient usually lies between minus one and plus one, so a value near the theoretical bound is a signal either of an extremely lopsided distribution or of an arithmetic error.

### 2.5 Lemma: the empirical relation between the three averages

> **Lemma 5.** For moderately skewed unimodal distributions, the mode is approximately as far below the median as the median is below the mean, so that

$$
\text{mean} - \text{mode} \approx 3\left(\text{mean} - \text{median}\right).
$$

The lemma is empirical rather than exact, and it fails for strongly skewed or multimodal distributions. Its role in the theory is to explain the factor of three in the second Pearson coefficient and to allow the two versions to be used interchangeably in routine work.

### 2.6 Theorem: Pearson's inequality for kurtosis

> **Theorem 6.** For every distribution with finite fourth moment, $\beta_2 \ge \beta_1 + 1$, and consequently $\gamma_2 \ge \gamma_1^{2} - 2$.

This is the sharpest general restriction linking the two shape coefficients. It says that a distribution cannot be strongly skewed while remaining flat: strong skewness forces a fourth moment large enough to make the distribution leptokurtic. The inequality is proved in Section 3 and is useful as an arithmetic check, because a computed pair that violates it must contain an error.

### 2.7 Summary of analytical properties

| Property | $SK_P$ | $SK_B$ | $SK_K$ | $\beta_1$ | $\beta_2$ |
|---|---|---|---|---|---|
| Uses the mean | yes | no | no | yes | yes |
| Uses every observation | yes | no | no | yes | yes |
| Bounded range | $\pm 3$ | $\pm 1$ | $\pm 1$ | $0$ to $\infty$ | $1$ to $\infty$ |
| Carries a direction | yes | yes | yes | no | no |
| Defined for open-ended data | no | yes | yes | no | no |
| Defined for multimodal data | median form only | yes | yes | yes | yes |
| Unchanged by a shift | yes | yes | yes | yes | yes |
| Unchanged by a rescaling | yes | yes | yes | yes | yes |

### 2.8 Theorem: the moment coefficients under the normal reference

> **Theorem 7.** For a normal distribution with mean $\mu$ and variance $\sigma^{2}$, $m_2 = \sigma^{2}$, $m_3 = 0$, $m_4 = 3\sigma^{4}$, so $\beta_1 = 0$, $\beta_2 = 3$ and $\gamma_2 = 0$.

The normal distribution is therefore the fixed point of the kurtosis scale, which is exactly why the excess form subtracts three and why the three shape names are defined relative to it. Any distribution with $\gamma_2 = 0$ is described as having normal tail weight, even if it is not itself normal, because the coefficient is a single number and cannot certify a whole shape.

## 3. Formal Proofs, Derivations, and Methods

### 3.1 Derivation of Bowley's coefficient from the half-widths

The quartiles divide the data into a lower half and an upper half with a common median. The natural measure of the shape of each half is its width measured from the median.

$$
a = Q_2 - Q_1, \qquad b = Q_3 - Q_2 .
$$

A symmetric distribution has $a = b$. The amount of asymmetry is the difference $b - a$, but a raw difference carries units and grows with the scale of the data, so it must be divided by a measure of the same kind. The only scale in sight that is built from the same three quantities is the interquartile range $a + b$, so the standardised asymmetry is

$$
SK_B = \frac{b - a}{a + b}.
$$

Substituting the definitions of $a$ and $b$ recovers the familiar form.

$$
SK_B = \frac{\left(Q_3 - Q_2\right) - \left(Q_2 - Q_1\right)}{\left(Q_3 - Q_2\right) + \left(Q_2 - Q_1\right)} = \frac{Q_3 + Q_1 - 2Q_2}{Q_3 - Q_1}.
$$

Three properties follow from this construction rather than from inspection of the formula. The coefficient is zero precisely when the two half-widths agree; it is positive precisely when the upper half is the wider; and it changes by a factor of at most one in either direction because the numerator cannot exceed the denominator. Kelly's coefficient is the same construction with the middle eighty per cent in place of the middle fifty per cent, which is why it takes the same bound and differs only in reach.

### 3.2 Complete proof that Bowley's coefficient lies between minus one and plus one

Suppose the data have distinct quartiles, so that the interquartile range is strictly positive. Then $a \ge 0$ and $b \ge 0$ with $a + b > 0$.

Because $a \ge 0$, the inequality $b - a \le b + a$ holds, and because $b \ge 0$, the inequality $a - b \le a + b$ holds. Dividing both by the positive quantity $a + b$ gives

$$
-1 \le \frac{b - a}{a + b} \le 1 .
$$

Equality on the right requires $a = 0$, which means $Q_1 = Q_2$; equality on the left requires $b = 0$, which means $Q_2 = Q_3$. Both are degenerate cases in which at least half the observations coincide, so for genuine data the inequalities are strict. The proof also shows that the coefficient is the signed proportion of the interquartile range contributed by the excess width of the longer half, which is the interpretation to quote in an examination.

### 3.3 Complete proof of the bound on the second Pearson coefficient

Let $n$ be the number of observations. Three inequalities are chained.

The first is the triangle inequality for averages, applied to the deviations from the median.

$$
\left|\bar{x} - Q_2\right| = \left|\frac{1}{n}\sum_{i=1}^{n}\left(x_i - Q_2\right)\right| \le \frac{1}{n}\sum_{i=1}^{n}\left|x_i - Q_2\right| .
$$

The second is the minimising property of the median: among all constants $c$, the function $c \mapsto \frac{1}{n}\sum\left|x_i - c\right|$ is minimised at the median, so

$$
\frac{1}{n}\sum_{i=1}^{n}\left|x_i - Q_2\right| \le \frac{1}{n}\sum_{i=1}^{n}\left|x_i - \bar{x}\right| .
$$

The third is the Cauchy–Schwarz inequality applied to the vectors whose entries are $\left|x_i - \bar{x}\right|$ and $1$.

$$
\frac{1}{n}\sum_{i=1}^{n}\left|x_i - \bar{x}\right| \le \left(\frac{1}{n}\sum_{i=1}^{n}\left(x_i - \bar{x}\right)^{2}\right)^{\frac{1}{2}} = s .
$$

Combining the three gives $\left|\bar{x} - Q_2\right| \le s$, and multiplying by three and dividing by $s$ gives the bound.

$$
\left|SK_P\right| = \frac{3\left|\bar{x} - Q_2\right|}{s} \le 3 .
$$

The bound is attained only in the degenerate case in which all the mass sits at two points with equal frequencies, for which the mean absolute deviation about the median is twice the mean absolute deviation about the mean. This is the precise sense in which the theoretical range from minus three to plus three is an outer limit that real data rarely approach.

### 3.4 Derivation of the second central moment identity

The moment coefficients cannot be computed until the central moments are available, and the central moments are almost never computed directly because the deviations from the mean are awkward numbers. The conversion identities solve this problem, and their derivations are all instances of one trick: write the deviation from the mean as a deviation from a convenient origin minus a constant.

Begin with the second central moment for grouped data, where $n = \sum f_i$ and $d_i = x_i - A$.

$$
m_2 = \frac{1}{n}\sum_{i=1}^{k} f_i\left(x_i - \bar{x}\right)^{2} .
$$

Insert and subtract $A$ inside the bracket, noting that $x_i - \bar{x} = \left(x_i - A\right) - \left(\bar{x} - A\right)$.

$$
m_2 = \frac{1}{n}\sum_{i=1}^{k} f_i\left\{d_i - \left(\bar{x} - A\right)\right\}^{2} .
$$

Expand the square, using $\left(u - v\right)^{2} = u^{2} - 2uv + v^{2}$ with $u = d_i$ and $v = \bar{x} - A$.

$$
m_2 = \frac{1}{n}\sum_{i=1}^{k} f_i d_i^{2} - 2\left(\bar{x} - A\right)\frac{1}{n}\sum_{i=1}^{k} f_i d_i + \left(\bar{x} - A\right)^{2}\frac{1}{n}\sum_{i=1}^{k} f_i .
$$

Recognise the three pieces. The first is $m_2'$, the second contains $m_1'$, and the third contains the total frequency $n$ divided by $n$, which is one.

$$
m_2 = m_2' - 2\left(\bar{x} - A\right)m_1' + \left(\bar{x} - A\right)^{2} .
$$

Finally use the first-moment identity $m_1' = \bar{x} - A$, which follows because the average of $x_i - A$ is $\bar{x} - A$.

$$
m_2 = m_2' - 2\left(m_1'\right)^{2} + \left(m_1'\right)^{2} = m_2' - \left(m_1'\right)^{2} .
$$

This is the shift-of-origin correction. It says that the second moment about an arbitrary origin overstates the variance by exactly the square of the distance between that origin and the mean, which is why choosing an origin near the centre of the data keeps the correction small and the arithmetic stable.

### 3.5 Derivation of the third central moment identity

The same substitution is applied to the third central moment, with the cube of a difference expanded as $u^{3} - 3u^{2}v + 3uv^{2} - v^{3}$.

$$
m_3 = \frac{1}{n}\sum_{i=1}^{k} f_i\left\{d_i - \left(\bar{x} - A\right)\right\}^{3} .
$$

Expanding term by term gives four sums.

$$
m_3 = \frac{1}{n}\sum f_i d_i^{3} - 3\left(\bar{x} - A\right)\frac{1}{n}\sum f_i d_i^{2} + 3\left(\bar{x} - A\right)^{2}\frac{1}{n}\sum f_i d_i - \left(\bar{x} - A\right)^{3}\frac{1}{n}\sum f_i .
$$

Identify $m_3'$, $m_2'$, $m_1'$ and the unit multiplier on the last term.

$$
m_3 = m_3' - 3\left(\bar{x} - A\right)m_2' + 3\left(\bar{x} - A\right)^{2}m_1' - \left(\bar{x} - A\right)^{3} .
$$

Replace $\bar{x} - A$ by $m_1'$ throughout and collect the cubic terms.

$$
m_3 = m_3' - 3m_1'm_2' + 3\left(m_1'\right)^{3} - \left(m_1'\right)^{3} = m_3' - 3m_1'm_2' + 2\left(m_1'\right)^{3} .
$$

The pattern to remember is the binomial coefficient sequence $1, -3, +2$; the last coefficient is not minus one because two of the cubic terms combine. Forgetting that combination is the commonest single error in the whole computation.

### 3.6 Derivation of the fourth central moment identity

For the fourth central moment the expansion uses $u^{4} - 4u^{3}v + 6u^{2}v^{2} - 4uv^{3} + v^{4}$.

$$
m_4 = \frac{1}{n}\sum_{i=1}^{k} f_i\left\{d_i - \left(\bar{x} - A\right)\right\}^{4} .
$$

Expanding produces five sums, of which the fifth is a constant.

$$
m_4 = m_4' - 4m_1'm_3' + 6\left(m_1'\right)^{2}m_2' - 4\left(m_1'\right)^{3}m_1' + \left(m_1'\right)^{4} .
$$

The fourth and fifth terms combine, because $-4\left(m_1'\right)^{3}m_1' = -4\left(m_1'\right)^{4}$ and adding the fifth term gives $-3\left(m_1'\right)^{4}$.

$$
m_4 = m_4' - 4m_1'm_3' + 6\left(m_1'\right)^{2}m_2' - 3\left(m_1'\right)^{4} .
$$

The coefficient sequence $1, -4, +6, -3$ is the one to memorise for kurtosis questions. Together with the sequences above it forms a complete set for the first four moments.

### 3.7 Derivation of the general origin-change identity

The four identities are special cases of one statement. Write $x_i - A = \left(x_i - \bar{x}\right) + \left(\bar{x} - A\right)$ and expand the $r$-th power by the binomial theorem.

$$
\left(x_i - A\right)^{r} = \sum_{j=0}^{r} \binom{r}{j}\left(x_i - \bar{x}\right)^{j}\left(\bar{x} - A\right)^{r-j} .
$$

Averaging with frequencies and using the definition of the central moments, with the convention $m_0 = 1$, gives

$$
m_r' = \sum_{j=0}^{r} \binom{r}{j} m_j \left(\bar{x} - A\right)^{r-j} .
$$

This single identity generates every conversion formula in either direction. Setting $r = 2$ and using $m_1 = 0$ gives $m_2' = m_2 + \left(\bar{x} - A\right)^{2}$, which rearranges to the second identity. Setting $r = 3$ gives $m_3' = m_3 + 3m_2\left(\bar{x} - A\right) + \left(\bar{x} - A\right)^{3}$, which rearranges to the third. The identity is also the fastest way to move moments from one origin to another, which is exactly what a question of the form "the moments about 5 are given, find the moments about 10" requires.

### 3.8 Proof that the normal distribution has coefficient of kurtosis three

Let $Z$ be standard normal with density $\varphi$ and distribution function $\Phi$, and note that $\varphi'\left(z\right) = -z\varphi\left(z\right)$. Integrating by parts,

$$
E\left[Z^{4}\right] = \int_{-\infty}^{\infty} z^{4}\varphi\left(z\right)\,dz = \int_{-\infty}^{\infty} z^{3}\left(-\varphi'\left(z\right)\right)dz .
$$

The boundary term vanishes because $z^{3}\varphi\left(z\right)$ tends to zero at both ends, so

$$
E\left[Z^{4}\right] = 3\int_{-\infty}^{\infty} z^{2}\varphi\left(z\right)\,dz = 3E\left[Z^{2}\right] = 3 .
$$

For a normal variable with standard deviation $\sigma$ we have $X - \mu = \sigma Z$, so the fourth central moment is $\sigma^{4}E\left[Z^{4}\right] = 3\sigma^{4}$, and the second central moment is $\sigma^{2}$. Therefore

$$
\beta_2 = \frac{3\sigma^{4}}{\left(\sigma^{2}\right)^{2}} = 3, \qquad \gamma_2 = 0 .
$$

The same integration by parts with $z^{3}$ in place of $z^{4}$ gives $E\left[Z^{3}\right] = 2E\left[Z\right] = 0$, so the normal distribution has zero skewness and zero excess kurtosis simultaneously.

### 3.9 Proof of Pearson's inequality

Standardise the variable so that $Z = \left(X - \mu\right)/\sigma$ has mean zero, variance one, third moment $\gamma_1$ and fourth moment $\beta_2$. For any real numbers $c$ and $d$, the square $\left(Z^{2} + cZ + d\right)^{2}$ is non-negative, so its expectation is non-negative.

$$
E\left[\left(Z^{2} + cZ + d\right)^{2}\right] = \beta_2 + c^{2} + d^{2} + 2c\gamma_1 + 2d \ge 0 .
$$

The expression is a quadratic in $c$ and $d$ and is minimised where the two partial derivatives vanish, that is at $c = -\gamma_1$ and $d = -1$. Substituting those values gives

$$
\beta_2 + \gamma_1^{2} + 1 - 2\gamma_1^{2} - 2 \ge 0,
$$

which simplifies to

$$
\beta_2 \ge \gamma_1^{2} + 1 = \beta_1 + 1 .
$$

Subtracting three from both sides gives $\gamma_2 \ge \gamma_1^{2} - 2$. Equality holds exactly for distributions whose standardised variable satisfies $Z^{2} - \gamma_1 Z - 1 = 0$ almost surely, that is for two-point distributions. The inequality is therefore sharp, and its practical use is as a consistency check: a reported pair with $\beta_2 < \beta_1 + 1$ is impossible.

### 3.10 Method: computing every skewness and kurtosis coefficient from a grouped table

1. Verify that the classes have a common width and compute each class mark as the midpoint of the class boundaries.
2. Choose a working origin $A$ equal to a central class mark and record the class width $c$.
3. Build the columns $f$, $d = x - A$, $u = d/c$, $fd$, $fd^{2}$, $fd^{3}$, $fd^{4}$, and total each one. Check that the totals of $fd$ and $fd^{3}$ have the sign implied by the visual shape of the table.
4. Compute the raw moments $m_1'$ to $m_4'$ by dividing each total by $n$.
5. Compute the mean as $A + m_1'$ and the variance as $m_2' - \left(m_1'\right)^{2}$.
6. Convert to $m_3$ and $m_4$ with the identities of Sections 3.5 and 3.6, or, for coded data, compute the central moments in the coded scale and multiply by $c^{3}$ and $c^{4}$ at the end.
7. Compute the coefficients $\beta_1$, $\gamma_1$, $\beta_2$ and $\gamma_2$, and read the direction from the sign of $m_3$.
8. Build the cumulative frequency column on class boundaries, interpolate the quartiles and the required percentiles, and compute $SK_B$ and $SK_K$.
9. Compute the mode and both Pearson coefficients.
10. Compare the four answers, state the direction and the magnitude, and explain any disagreement in terms of the reach of each measure.

### 3.11 Method: judging the magnitude of a coefficient

A numerical answer without a description is incomplete. The following conventions are standard in practice and are accepted in examinations. A Pearson coefficient between minus one half and plus one half is slight to moderate; between one half and one is marked; beyond one is extreme and should prompt a check. A Bowley or Kelly coefficient below one fifth in size is slight, between one fifth and one half is moderate, and above one half is marked. For the moment coefficient, a $\beta_1$ below about one quarter corresponds to a nearly symmetric shape, values near one correspond to clear asymmetry, and values above four correspond to a distribution dominated by a single tail. For kurtosis, $\gamma_2$ within about one unit of zero is described as close to normal tail weight, and larger magnitudes are described as clearly leptokurtic or clearly platykurtic.

## 4. Representative Worked Examples and Solutions

### 4.1 Problem: three coefficients for the profits of one thousand companies

The profits of one thousand companies, in thousands of shillings, are grouped in classes of width twenty.

| Profit class | 100–119 | 120–139 | 140–159 | 160–179 | 180–199 | 200–219 | 220–239 |
|---|---|---|---|---|---|---|---|
| Number of companies | 17 | 53 | 199 | 194 | 327 | 208 | 2 |

Compute Karl Pearson's first coefficient, Bowley's coefficient, the moment coefficient of skewness and the coefficient of kurtosis, and interpret each.

### 4.2 Solution: one table, four coefficients

Step 1. Choose the working origin $A = 169.5$, the central class mark, with class width $c = 20$, and build the working columns.

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

Step 2. Compute the mean and the standard deviation.

$$
\bar{x} = 169.5 + \left(\frac{393}{1000}\right)20 = 177.36,
$$

$$
s^{2} = 20^{2}\left\{\frac{1741}{1000} - \left(\frac{393}{1000}\right)^{2}\right\} = 400 \times 1.586551 = 634.62, \qquad s = 25.19 .
$$

Step 3. Compute the mode from the modal class 180–199.

$$
\text{Mode} = 179.5 + \frac{133}{252}\times 20 = 190.06 .
$$

Step 4. Compute the first Pearson coefficient.

$$
SK_P = \frac{177.36 - 190.06}{25.19} = -0.504 .
$$

Step 5. Interpolate the quartiles from the cumulative frequencies $0, 17, 70, 269, 463, 790, 998, 1000$.

$$
Q_1 = 139.5 + \frac{250 - 70}{199}\times 20 = 157.59, \qquad Q_2 = 179.5 + \frac{500 - 463}{327}\times 20 = 181.76,
$$

$$
Q_3 = 179.5 + \frac{750 - 463}{327}\times 20 = 197.05 .
$$

Step 6. Compute Bowley's coefficient.

$$
SK_B = \frac{197.05 + 157.59 - 363.52}{197.05 - 157.59} = \frac{-8.88}{39.46} = -0.225 .
$$

Step 7. Convert the working moments to central moments.

$$
m_1' = 7.86, \qquad m_2' = 696.4, \qquad m_3' = 7704, \qquad m_4' = 998560,
$$

$$
m_2 = 696.4 - 7.86^{2} = 634.62,
$$

$$
m_3 = 7704 - 3\left(7.86\right)\left(696.4\right) + 2\left(7.86\right)^{3} = 7704 - 16421.11 + 971.18 = -7745.94,
$$

$$
m_4 = 998560 - 4\left(7.86\right)\left(7704\right) + 6\left(7.86\right)^{2}\left(696.4\right) - 3\left(7.86\right)^{4} = 1003035.96 .
$$

Step 8. Compute the two shape coefficients.

$$
\beta_1 = \frac{\left(-7745.94\right)^{2}}{\left(634.62\right)^{3}} = 0.235, \qquad \beta_2 = \frac{1003035.96}{\left(634.62\right)^{2}} = 2.490 .
$$

Step 9. Interpret. All the signed measures are negative, so the distribution is skewed to the left: a small number of companies earn unusually little, and that short left tail pulls the mean below the mode and the median. The moment coefficient of $0.235$ records a modest amount of asymmetry in the cubed sense, and the coefficient of kurtosis of $2.490$ is below three, so the distribution is platykurtic, with lighter tails and a flatter top than the normal curve. The absence of very large profits explains the lightness of the right tail, since the highest class contains only two companies.

### 4.3 Problem: five coefficients for a wage distribution

The daily wages of one hundred workers, in units of ten shillings, are grouped as follows.

| Wage class | 0–9 | 10–19 | 20–29 | 30–39 | 40–49 |
|---|---|---|---|---|---|
| Number of workers | 40 | 30 | 15 | 10 | 5 |

Compute the mean, the standard deviation, the mode, all four coefficients of skewness and the coefficient of kurtosis, and comment on the relationship between the mode and the median.

### 4.4 Solution: a strongly right-skewed distribution

Step 1. Take class marks $4.5, 14.5, 24.5, 34.5, 44.5$, working origin $A = 24.5$ and class width $c = 10$, with $u = \left(x - 24.5\right)/10$.

| Class mark $x$ | $f$ | $u$ | $fu$ | $fu^{2}$ | $fu^{3}$ | $fu^{4}$ |
|---|---|---|---|---|---|---|
| 4.5 | 40 | $-2$ | $-80$ | 160 | $-320$ | 640 |
| 14.5 | 30 | $-1$ | $-30$ | 30 | $-30$ | 30 |
| 24.5 | 15 | $0$ | $0$ | 0 | 0 | 0 |
| 34.5 | 10 | $1$ | $10$ | 10 | 10 | 10 |
| 44.5 | 5 | $2$ | $10$ | 20 | 40 | 80 |
| Total | 100 | | $-90$ | 220 | $-300$ | 760 |

Step 2. Compute the mean and the standard deviation from the coded columns.

$$
\bar{x} = 24.5 + 10\left(\frac{-90}{100}\right) = 15.5,
$$

$$
s^{2} = 100\left\{\frac{220}{100} - \left(\frac{-90}{100}\right)^{2}\right\} = 100\left(2.20 - 0.81\right) = 139, \qquad s = 11.79 .
$$

Step 3. Compute the mode from the modal class 0–9, whose lower boundary is $-0.5$.

$$
\text{Mode} = -0.5 + \left(\frac{40 - 0}{2(40) - 0 - 30}\right)10 = -0.5 + \frac{400}{50} = 7.5 .
$$

Step 4. Interpolate the quartiles from the cumulative frequencies $40, 70, 85, 95, 100$.

$$
Q_1 = -0.5 + \frac{25}{40}\times 10 = 5.75, \qquad Q_2 = 9.5 + \frac{10}{30}\times 10 = 12.83, \qquad Q_3 = 19.5 + \frac{5}{15}\times 10 = 22.83 .
$$

Step 5. Compute the first Pearson coefficient.

$$
SK_P = \frac{15.5 - 7.5}{11.79} = 0.679 .
$$

Step 6. Compute the second Pearson coefficient and note the coincidence.

$$
SK_P = \frac{3\left(15.5 - 12.83\right)}{11.79} = \frac{8.00}{11.79} = 0.679 .
$$

The two versions agree exactly here because the mode of $7.5$ satisfies the empirical relation $\text{mean} - \text{mode} = 15.5 - 7.5 = 8.00$ and $3\left(\text{mean} - \text{median}\right) = 3 \times 2.67 = 8.00$. When a grouped distribution happens to satisfy the relation, the two formulas reinforce each other and the answer is safe.

Step 7. Compute Bowley's coefficient.

$$
SK_B = \frac{22.83 + 5.75 - 25.67}{22.83 - 5.75} = \frac{2.92}{17.08} = 0.171 .
$$

Step 8. Compute Kelly's coefficient from the tenth and ninetieth percentiles.

$$
P_{10} = -0.5 + \frac{10}{40}\times 10 = 2.00, \qquad P_{90} = 29.5 + \frac{5}{10}\times 10 = 34.50,
$$

$$
SK_K = \frac{34.50 + 2.00 - 25.67}{34.50 - 2.00} = \frac{10.83}{32.50} = 0.333 .
$$

Step 9. Compute the central moments in the coded scale and rescale.

$$
m_2\left(u\right) = 2.20 - 0.81 = 1.39, \qquad m_3\left(u\right) = -3.00 - 3\left(-0.90\right)\left(2.20\right) + 2\left(-0.729\right) = 1.482,
$$

$$
m_4\left(u\right) = 7.60 - 4\left(-0.90\right)\left(-3.00\right) + 6\left(0.81\right)\left(2.20\right) - 3\left(0.81\right)^{2} = 5.5237 .
$$

Multiplying by $c^{3} = 1000$ and $c^{4} = 10000$ gives $m_3 = 1482$ and $m_4 = 55237$.

Step 10. Form the moment coefficients.

$$
\beta_1 = \frac{1482^{2}}{139^{3}} = 0.818, \qquad \gamma_1 = \frac{1482}{11.79^{3}} = 0.904, \qquad \beta_2 = \frac{55237}{139^{2}} = 2.859 .
$$

Step 11. Interpret and cross-check. Every signed measure is positive, so the distribution is skewed to the right: forty per cent of workers earn less than ten units while a few earn more than forty. The three skewness measures increase in size as their reach increases, from Bowley's $0.171$ over the middle fifty per cent, through Kelly's $0.333$ over the middle eighty per cent, to the moment-based $0.904$ which uses every observation and cubes the distances. The coefficient of kurtosis of $2.859$ is just below three, so the distribution is mildly platykurtic, which is consistent with the bounded wage classes; and the Pearson inequality is respected because $2.859$ exceeds $0.818 + 1 = 1.818$.

### 4.5 Problem: skewness from three averages and a decision about location

A quality-control sample of times to failure, in hours, has mean 72, median 75, mode 78 and standard deviation 10. Compute both Pearson coefficients, state the direction and magnitude of the skewness, and advise whether the mean or the median should be reported as the typical lifetime.

### 4.6 Solution: standardise the gaps and interpret

Step 1. Compare the three averages.

$$
\text{mean} = 72 < \text{median} = 75 < \text{mode} = 78 .
$$

Step 2. Read the direction. The mean is the smallest of the three, so the mean has been dragged towards the small values and the long tail lies to the left. The distribution is negatively skewed.

Step 3. Compute the first Pearson coefficient.

$$
SK_P = \frac{72 - 78}{10} = -0.60 .
$$

Step 4. Compute the second Pearson coefficient.

$$
SK_P = \frac{3\left(72 - 75\right)}{10} = -0.90 .
$$

Step 5. Judge the magnitude. Both values are negative and lie beyond one half in size, so the skewness is marked rather than slight.

Step 6. Advise on the measure of location. Under marked left skewness the mean of seventy-two hours understates the typical lifetime, because it has been pulled down by a small number of very early failures. The median of seventy-five hours is the better summary, and the report should give the median with the quartiles so that the asymmetry is visible to the reader.

### 4.7 Problem: kurtosis and the limits of normal theory

A sample of ten delivery times in minutes is 1, 1, 1, 1, 2, 2, 2, 2, 2 and 9. Compute the four central moments, both shape coefficients, and state what the results imply for a confidence interval for the mean built on the normal approximation.

### 4.8 Solution: compute the moments, then interpret the consequences

Step 1. Compute the mean.

$$
\bar{x} = \frac{1 + 1 + 1 + 1 + 2 + 2 + 2 + 2 + 2 + 9}{10} = \frac{23}{10} = 2.3 .
$$

Step 2. Form the deviations and their powers.

| Observation | Frequency | Deviation | Squared | Cubed | Fourth power |
|---|---|---|---|---|---|
| 1 | 4 | $-1.3$ | 1.69 | $-2.197$ | 2.8561 |
| 2 | 5 | $-0.3$ | 0.09 | $-0.027$ | 0.0081 |
| 9 | 1 | $6.7$ | 44.89 | 300.763 | 2015.1121 |

Step 3. Average each column to obtain the central moments.

$$
m_1 = 0, \qquad m_2 = \frac{4(1.69) + 5(0.09) + 44.89}{10} = 5.21,
$$

$$
m_3 = \frac{4(-2.197) + 5(-0.027) + 300.763}{10} = 29.184,
$$

$$
m_4 = \frac{4(2.8561) + 5(0.0081) + 2015.1121}{10} = 202.66 .
$$

Step 4. Compute the shape coefficients.

$$
\beta_1 = \frac{29.184^{2}}{5.21^{3}} = \frac{851.71}{141.42} = 6.02, \qquad \beta_2 = \frac{202.66}{5.21^{2}} = \frac{202.66}{27.14} = 7.47 .
$$

Step 5. Convert to the signed and excess forms.

$$
\gamma_1 = \frac{29.184}{5.21^{\frac{3}{2}}} = 2.45, \qquad \gamma_2 = 7.47 - 3 = 4.47 .
$$

Step 6. Interpret the shape. The positive third moment and the positive $\gamma_1$ show strong right skewness: nine deliveries are quick and one is very slow. The excess kurtosis of $4.47$ shows very heavy tails and a sharp peak, so the distribution is strongly leptokurtic and a normal curve would badly understate the chance of an extreme delivery.

Step 7. State the consequence for inference. A confidence interval for the mean built as $\bar{x} \pm t s/\sqrt{n}$ assumes an approximately normal sampling distribution. With skewness of this size in a sample of ten, that interval is unreliable: the sample mean is pulled by the single nine-minute delivery, and the standard error computed from $s$ is itself unstable. The defensible options are to report the median with a rank-based interval, to collect a much larger sample, or to model the logarithms of the times, which reduces both skewness and kurtosis.

## 5. Mathematical Extensions, Limits, and Common Errors

### 5.1 Mixtures, contamination and the behaviour of the moment coefficients

Real data are often contaminated: a measuring instrument sticks, a respondent misreads a scale, a payment is entered with an extra zero. Contamination of a single observation with value $x$ displaced to $x + \delta$ changes the third central moment by roughly $3\delta\left(x - \bar{x}\right)^{2}/n$ and the fourth by roughly $4\delta\left(x - \bar{x}\right)^{3}/n$, so a large displacement can dominate both. This is the sense in which the moment coefficients have unbounded influence functions: no matter how large the sample, one sufficiently wild observation can change the answer by an arbitrary amount. Bowley's coefficient, by contrast, has a bounded influence function, because a change that does not cross a quartile changes nothing at all.

The practical consequence is a division of labour. Moment coefficients are the right tool for describing a distribution that is believed to be clean, and for theoretical work where the moment machinery can be pushed through. Quartile and percentile coefficients are the right tool for screening data whose tails are suspect, and for summarising distributions with open-ended classes.

Mixtures deserve separate mention. A mixture of two symmetric distributions with different means is asymmetric, and the sign of its skewness is governed by the relative sizes and separation of the two components. A mixture of a tight central component with a small widely dispersed component produces strong leptokurtosis, which is the mathematical signature of the contamination described above. Recognising that a large kurtosis is evidence of a mixture rather than of a genuinely peaked single population is an important skill in applied work.

### 5.2 Grouping, and the correction for grouped moments

When continuous data are grouped into classes, every observation is replaced by its class mark, which adds an error of up to half a class width. The variance computed from class marks therefore overstates the true variance by approximately $c^{2}/12$, where $c$ is the class width, and this is the classical Sheppard correction. The third and fourth grouped moments are biased in more complicated ways, and the corrections are only valid when the underlying distribution is smooth and the classes are numerous and of equal width.

In an examination the grouped moments are reported without correction, because the grouped distribution is the data. In applied work the correction matters when the class width is a substantial fraction of the standard deviation. A useful rule of thumb is that grouping is harmless when the class width is below a tenth of the standard deviation, and that the reported moments should be interpreted cautiously when the class width approaches half the standard deviation.

### 5.3 Sampling variation of the shape coefficients

Sample skewness and sample kurtosis are themselves random variables, and their sampling distributions are wide. For a normal population of size $n$, the sample coefficient of skewness has standard error approximately $\sqrt{6/n}$ and the sample excess kurtosis has standard error approximately $\sqrt{24/n}$. For a sample of a hundred normal observations these are about $0.245$ and $0.490$, so an observed skewness of $0.3$ and an observed excess kurtosis of $0.6$ are entirely unremarkable. Reporting such values as evidence of non-normality, without a sample size in view, is one of the commonest errors in applied statistics.

The bias of the uncorrected estimators is also worth knowing. The estimator $\hat{\beta}_1$ computed with divisor $n$ is biased downwards in small samples, and the corresponding kurtosis estimator is biased towards three. Software usually applies corrections based on the sample size, which is why a value taken from a textbook formula and a value taken from a statistics package can differ in the second decimal place while both being correct for their own definition.

### 5.4 Skewness, kurtosis and the choice of inferential method

The classical confidence interval for a mean and the classical $t$-test rest on the sampling distribution of $\bar{x}$ being approximately normal. Two features of the population determine how fast that approximation is reached. Skewness enters through the third absolute moment: the Berry–Esseen bound states that the largest discrepancy between the exact distribution of the standardised mean and the standard normal is at most a constant times $E\left|X - \mu\right|^{3}/\left(\sigma^{3}\sqrt{n}\right)$, so a distribution with large third absolute moment needs a much larger sample before the bound becomes small. Kurtosis enters through the variance of the sample variance, which is governed by the fourth moment; when $\beta_2$ is large, the estimated standard error is highly variable and intervals built from it have coverage that differs substantially from the nominal level.

The remedies are standard. Transform right-skewed positive data with logarithms, and left-skewed data by reflecting first. Use the median and a bootstrap or rank-based interval when transformation is inappropriate. Increase the sample when the shape is fixed by the nature of the variable. And when a summary must be reported, report the shape coefficients alongside the location and spread so that the reader can judge the reliability of the rest.

For the choice of location the rule is equally concrete. With $\left|SK_P\right|$ below about one half the mean is safe and is more efficient than the median, because it uses all the information in the data. With $\left|SK_P\right|$ above one half the median should be reported, and with open-ended classes it is the only option. For a variable whose distribution is strongly bimodal, neither alone is adequate and the two modes should be reported with the proportions falling in each.

### 5.5 The exact sense in which kurtosis measures peakedness

The description of kurtosis as peakedness is a shorthand that becomes misleading when pushed. For distributions that can be reordered in the partial order of peakedness, the fourth standardised moment does order them correctly: a distribution obtained by pushing mass from the shoulders towards both the centre and the tails has a larger $\beta_2$. But two distributions can have the same $\beta_2$ and differ in the height of the peak, because the fourth moment also responds to the tails.

A precise statement is available through the excess form. A positive $\gamma_2$ means that the standardised fourth moment exceeds the normal value, which in turn means that the combined effect of centre and tails is heavier than normal. The safest interpretation combines two statements: leptokurtic distributions are both more peaked and longer tailed than the normal, and platykurtic distributions are both flatter and shorter tailed. Any statement that mentions only the peak, or only the tails, is incomplete and can be contradicted by a counterexample.

### 5.6 Common errors and how to avoid them

- Reporting $\beta_1$ as a signed quantity. It is a square and cannot be negative; direction comes from $m_3$ or $\gamma_1$.
- Forgetting to cube $\left(m_1'\right)$ in the third-moment identity. The correct coefficient sequence is $1, -3, +2$, not $1, -3, +1$.
- Using the class limits instead of the class boundaries in the mode and quartile interpolation. A class stated as 180–199 begins at 179.5.
- Confusing the two Pearson formulas and using the median without the factor of three, or the mode when the distribution is multimodal.
- Comparing $\beta_2$ with zero instead of three. A value of $2.7$ is platykurtic, not "slightly positive kurtosis".
- Reversing leptokurtic and platykurtic. Leptokurtic means a taller peak and heavier tails; platykurtic means a flatter top and lighter tails.
- Subtracting the mean from the wrong quantity. The Pearson numerator is mean minus mode, and reversing it reverses every sign in the answer.
- Assuming that a small Bowley coefficient proves symmetry. The quartiles are blind to everything outside the middle fifty per cent, so an enormous outlier leaves the coefficient untouched.
- Treating a kurtosis value computed with divisor $n$ as identical to one computed with divisor $n-1$. The difference is small but real, and the divisor must be stated.
- Interpreting an unstandardised moment. The third and fourth central moments carry the units of the variable raised to those powers and are not comparable across data sets.
- Omitting the interpretation. State the direction, the magnitude and the practical consequence, and check the sign against the ordering of the averages.
