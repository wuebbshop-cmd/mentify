## 1. Foundational Concepts, Definitions, and Axioms

### 1.1 Two archers on the same practice range

Imagine two archers practising on the same range. At the end of the morning, each has shot twenty arrows, and each reports that the arrows landed, on average, one metre to the right of the gold. On the strength of that single number the two archers look identical. Then you look at the targets. The first archer's twenty arrows are packed into a tight circle the size of a saucer, all of them about a metre right of centre. The second archer's arrows are scattered across the whole face of the target: some in the gold, some in the outer ring, three of them off the board entirely. The averages agree, but the performances are completely different.

The number that separates the two archers is a measure of spread. It does not describe where the arrows landed on average; it describes how far they strayed from that average. The first archer has a small spread, the second a large spread, and any honest reporting of the morning's work has to say so.

That is exactly the problem this topic solves, but with numbers instead of arrows. A single average, whether it is a mean, a median or a mode, tells you where the middle of a set of measurements lies. It tells you nothing at all about whether the measurements are clustered tightly around that middle or flung widely on either side. Every measurement you will meet in business, agriculture, medicine or examination results comes with both questions attached: where is the centre, and how far from the centre do things generally sit. The second question is dispersion.

A useful way to hold the two ideas together is to picture a flock of birds settling on a long straight fence. The centre of the flock might be the tenth post. But a centre of the tenth post could mean twenty birds packed shoulder to shoulder at posts nine, ten and eleven, or it could mean ten birds at post one and ten at post nineteen. The centre is the same; the flock is nothing like the same. Dispersion is the width of the flock.

### 1.2 Why the average on its own is misleading

Two shops in the same street each employ five assistants. In the first shop every assistant earns about the same wage. In the second shop the owner pays one assistant a very large salary and the remaining four a small one, in such a way that the average comes out the same as in the first shop. If a job seeker is told only the average wage, that person cannot tell whether the offer will be fair or whether they will be the poorly paid one. The average conceals the whole question of fairness, and it is the spread that reveals it.

The same point appears in quality control. Two machines fill bottles with a stated volume. Both deliver the same average volume over a shift. One fills every bottle within a millilitre of the target; the other alternates between overfilled and underfilled bottles that average out. The first machine is acceptable, the second will generate complaints and fines. Again the average agrees and the spread disagrees.

Three consequences follow, and they are the reasons this topic is examined so heavily.

- A summary of data that reports only a centre is incomplete, because it can be produced by wildly different data sets.
- Decisions about consistency, reliability, risk and quality are decisions about spread, not about centre.
- When two data sets have different centres, or are measured in different units, the comparison of their spreads needs a special tool, which is the coefficient of variation.

### 1.3 The range and the coefficient of range

The simplest possible description of spread uses only two numbers: the largest observation and the smallest observation. Everything else in the data set is ignored.

> **Definition (Range).** If $x_g$ is the greatest observation and $x_l$ is the smallest observation in a distribution, the range is $x_g - x_l$.

Read the symbols in words. The symbol $x_g$ is a single number, the largest value you can find in the list. The symbol $x_l$ is the other extreme, the smallest value in the list. The subscript letters are only labels reminding you of "greatest" and "lowest". The range is the answer to the question "how wide is the whole list from end to end".

An example makes this concrete. Suppose the daily takings of a market stall, in shillings, over eight days are $20$, $21$, $15$, $10$, $7$, $4$, $51$ and $49$. The greatest value is $51$ and the smallest is $4$, so the range is

$$
x_g - x_l = 51 - 4 = 47 .
$$

The takings therefore vary across a band of $47$ shillings from the quietest day to the best day.

The range has one clear virtue and one clear vice. The virtue is speed: it takes two comparisons and one subtraction, so it can be read off a table almost instantly. The vice is fragility. Because only two observations enter the calculation, every other observation is ignored, and a single freak value moves the answer as much as it likes. If the stallholder had one exceptional day of $400$ shillings, the range would leap to $396$ while seven of the eight days had barely changed. A measure that can be rewritten by one unusual value cannot be trusted as a summary of typical behaviour.

### 1.4 The coefficient of range

A bare range cannot be used to compare two lists measured in different units or sitting at very different levels. The range of wages in shillings and the range of heights in centimetres are both numbers, but subtracting one from the other, or declaring one "bigger", is meaningless. The remedy is to divide the range by something with the same units, so that the units cancel.

> **Definition (Coefficient of range).** The coefficient of range of a distribution is the ratio of the range to the sum of the extremes, that is $\frac{x_g - x_l}{x_g + x_l}$.

For the takings above, the coefficient of range is

$$
\frac{x_g - x_l}{x_g + x_l} = \frac{51 - 4}{51 + 4} = \frac{47}{55} \approx 0.855 .
$$

The answer carries no units, because shillings divided by shillings cancel. It says that the width of the list is about eighty-five per cent of the level of the list. A coefficient near zero would describe a list whose extremes are close together; a coefficient near one would describe a list whose smallest value is negligible beside its largest.

### 1.5 Quartiles, the interquartile range and quartile deviation

The range is distorted because it depends on the two most extreme observations, and those are precisely the observations most likely to be freak values. A natural repair is to trim the extremes off before measuring the width. If you cut away the lowest quarter of the data and the highest quarter, the width of what remains is a measurement of spread that no single outlier can destroy.

> **Definition (Quartiles).** The first quartile $Q_1$ is the value below which one quarter of the observations lie. The third quartile $Q_3$ is the value below which three quarters of the observations lie. The second quartile $Q_2$ is the median, the value that halves the data.

> **Definition (Interquartile range and quartile deviation).** The interquartile range is $Q_3 - Q_1$. The quartile deviation, also called the semi-interquartile range, is half of it, that is $Q = \frac{1}{2}\left(Q_3 - Q_1\right)$.

In words: $Q_1$ is the marker below which the bottom quarter of the data sits, and $Q_3$ is the marker below which the bottom three quarters sit. The distance between the two markers is the width of the middle half of the data, and the quartile deviation is half that width, so it behaves like a typical distance from the middle of the data to the edge of the middle half.

The quartile deviation is a better measure than the range for two reasons. First, it uses half of the observations, because three quarters of the data lie below $Q_3$ and one quarter below $Q_1$, so half the data lie between them. Second, extreme values cannot affect it: if the largest observation became ten times larger, $Q_1$ and $Q_3$ would not move. Its weakness is the mirror image of its strength. Because it deliberately ignores the outer quarters, it says nothing about them, so two data sets with identical quartile deviations can be quite different in the tails.

The quartile deviation, like the range, carries the units of the data. Its unit-free companion is the coefficient of quartile deviation.

> **Definition (Coefficient of quartile deviation).** The coefficient of quartile deviation is $\frac{Q_3 - Q_1}{Q_3 + Q_1}$.

Dividing by the sum of the quartiles cancels the units, exactly as the coefficient of range did, and the result is a pure number that can be compared across different data sets.

### 1.6 The mean absolute deviation

Both measures so far throw information away. The range discards everything except two values; the quartile deviation discards the outer quarters. A measure that uses every single observation is wanted, and the most obvious way to build one is to ask how far each observation sits from the mean, then average those distances.

There is one obstacle. The distances from the mean, taken with their signs, always cancel to zero, because the mean is the balance point of the data. Positive gaps exactly offset negative gaps, and the average of the signed gaps is therefore always zero, no matter how spread out the data are. To measure spread you must prevent that cancellation. There are two ways of doing so: ignore the signs, or square the gaps. Ignoring the signs gives the mean absolute deviation; squaring gives the variance.

> **Definition (Mean absolute deviation).** The mean absolute deviation about the mean of $n$ observations is $\frac{1}{n}\sum_{i=1}^{n}\left|x_i - \bar{x}\right|$.

Read the symbols in words. The symbol $n$ is the number of observations. The symbol $x_i$ is the $i$-th observation, so $x_1$ is the first, $x_2$ the second, and so on. The symbol $\bar{x}$, read "x bar", is the arithmetic mean. The two vertical bars mean "take the size of whatever is inside and forget its sign", so $\left|-6\right|$ is $6$ and $\left|6\right|$ is $6$. The capital sigma $\sum$ means "add up all the terms of this pattern as the index $i$ runs from $1$ to $n$", and the fraction $\frac{1}{n}$ in front turns that total into an average. The whole expression therefore says: find how far each observation is from the mean, throw away the signs, add the distances, and divide by how many there are.

A small example shows the idea. Take the five observations $4$, $8$, $10$, $12$ and $16$. Their mean is $10$. The distances from the mean are $6$, $2$, $0$, $2$ and $6$, which add to $16$, so the mean absolute deviation is $16$ divided by $5$, which is $3.2$. The typical observation sits about $3.2$ units away from the mean.

### 1.7 The variance

Squaring the gaps is the second way to stop the cancellation, and it is the one the whole subject is built on.

> **Definition (Variance).** The variance of $n$ observations is the average of the squared deviations from the mean, that is $s^2 = \frac{1}{n}\sum_{i=1}^{n}\left(x_i - \bar{x}\right)^2$. For frequency data with $n = \sum_{i=1}^{k} f_i$, the variance is $s^2 = \frac{1}{n}\sum_{i=1}^{k} f_i\left(x_i - \bar{x}\right)^2$.

Each symbol has a plain reading. The letter $s$ stands for the standard deviation, so $s^2$, read "s squared", stands for the variance. The term $x_i - \bar{x}$ is one gap: an observation minus the mean. The square of that gap is never negative, so no cancellation can occur when the squares are added. The sigma adds the squared gaps, and division by $n$ averages them. For frequency data the letter $k$ is the number of distinct values, $f_i$ is how many times the $i$-th value occurs, and multiplication by $f_i$ gives a repeated value the weight it deserves.

Squaring does more than remove signs. It punishes large gaps far more severely than small ones: a gap of $6$ contributes $36$, while a gap of $2$ contributes only $4$, so the contribution of the large gap is nine times as large rather than three times. This is why the variance is sensitive to outliers, and why it responds so strongly to a single observation that has broken loose from the rest.

### 1.8 The standard deviation

The variance has an awkward property. If the data are measured in shillings, the squared gaps are measured in shillings squared, and a quantity in shillings squared cannot be compared with the data themselves. A variance of $36$ means nothing to a shopkeeper. The repair is to undo the squaring.

> **Definition (Standard deviation).** The standard deviation is the positive square root of the variance, that is $s = \sqrt{\frac{1}{n}\sum_{i=1}^{n}\left(x_i - \bar{x}\right)^2}$.

The square root returns the measure to the original units. If wages are in shillings, the variance is in shillings squared and the standard deviation is in shillings, so a standard deviation of $12$ shillings can be said out loud: a typical wage sits about twelve shillings away from the average wage.

The standard deviation is the most used measure of dispersion in the whole of statistics, for three reasons. It uses every observation, so no information is thrown away. It is measured in the same units as the data, so it can be interpreted directly. And it has the algebraic properties developed in Section 2, which make it combine correctly when data sets are added together or rescaled.

### 1.9 The coefficient of variation

One problem survives. Suppose the mean wage in one factory is $180$ with a standard deviation of $11$, and the mean examination mark in a school is $60$ with a standard deviation of $9$. Which group is more variable? Comparing $11$ with $9$ is meaningless, because the two numbers are in different units and are measured against different centres. What is needed is a measure of spread expressed as a fraction of the level of the data.

> **Definition (Coefficient of variation).** The coefficient of variation is the standard deviation expressed as a percentage of the arithmetic mean, that is $C.V = \frac{s}{\bar{x}} \times 100\%$.

The formula divides one quantity in shillings by another quantity in shillings, so the units cancel and the answer is a percentage. For the factory the coefficient of variation is $11$ divided by $180$, which is about $6.1$ per cent. For the school it is $9$ divided by $60$, which is $15$ per cent. The school marks are therefore relatively far more variable, even though the factory's standard deviation is the larger number.

The interpretation rule is short and must be memorised in both directions. A larger coefficient of variation means more variable, less consistent, less homogeneous, more risky. A smaller coefficient of variation means less variable, more consistent, more homogeneous, less risky.

### 1.10 Notation used throughout

The following symbols recur in every formula and are worth fixing in memory before any calculation is attempted.

| Symbol | What it names | Plain reading |
|---|---|---|
| $n$ | Number of observations | How many values there are |
| $x_i$ | The $i$-th observation | One particular value in the list |
| $\bar{x}$ | Arithmetic mean | The total divided by the count |
| $f_i$ | Frequency of the $i$-th value | How many times that value occurs |
| $k$ | Number of distinct values or classes | How many rows the table has |
| $x_g$ | Greatest observation | The largest value |
| $x_l$ | Smallest observation | The smallest value |
| $Q_1, Q_3$ | First and third quartiles | Quarter and three-quarter markers |
| $s^2$ | Variance | Average of the squared gaps |
| $s$ | Standard deviation | Square root of the variance |
| $C.V$ | Coefficient of variation | Spread as a percentage of the mean |
| $h$ | Class width | Width of one class of grouped data |
| $m_j$ | Class mark | Midpoint of a class |

### 1.11 The measures side by side

Each measure answers a slightly different question, and choosing the right one is part of the skill being tested.

| Measure | What it measures | Units | Uses all the data | Effect of one outlier |
|---|---|---|---|---|
| Range | Full width from smallest to largest | Original units | No, only two values | Very large |
| Quartile deviation | Half the width of the middle half | Original units | No, ignores outer quarters | None |
| Mean absolute deviation | Average distance from the mean | Original units | Yes | Moderate |
| Variance | Average squared distance from the mean | Squared units | Yes | Very large |
| Standard deviation | Typical distance from the mean | Original units | Yes | Large |
| Coefficient of variation | Spread as a fraction of the mean | None | Yes | Large |

## 2. Theorems, Lemmas, and Analytical Properties

### 2.1 The deviations from the mean always cancel

The first property is the reason the naive "average the gaps" idea fails, and it is worth stating as a result because it is used constantly.

> **Theorem (Zero-sum of deviations).** For any set of observations with mean $\bar{x}$, the signed deviations satisfy $\sum_{i=1}^{n}\left(x_i - \bar{x}\right) = 0$.

The content is simple. The mean is the balance point of the data, so the amount by which the data exceed the mean is exactly balanced by the amount by which they fall short. Averaging the signed gaps therefore always produces zero, whatever the data are, which is why a measure of spread must either discard signs or square the gaps.

### 2.2 The short formula for the variance

Computing every deviation and squaring it is slow and error-prone by hand. An equivalent formula uses only two totals.

> **Theorem (Computational form of the variance).** For $n$ observations, $s^2 = \frac{1}{n}\sum_{i=1}^{n} x_i^2 - \bar{x}^2$. For frequency data, $s^2 = \frac{1}{n}\sum_{i=1}^{k} f_i x_i^2 - \bar{x}^2$.

In words, the variance equals the mean of the squares of the observations minus the square of the mean. The order of the subtraction matters and is the source of a very common mistake: it is the mean of the squares minus the square of the mean, not the other way round, and it is the mean that is squared, not the sum. A negative answer is proof that the subtraction has been done backwards or that the mean was not squared.

### 2.3 Moving the origin changes nothing

Subtracting a constant from every observation slides the whole data set along the number line without altering its shape.

> **Theorem (Invariance under translation).** If $y_i = x_i - c$ for a constant $c$, then $\bar{y} = \bar{x} - c$ and the variance and standard deviation are unchanged: $s_y^2 = s_x^2$ and $s_y = s_x$.

This is why the definition of the variance can be computed about any convenient origin. It is also why the variance is described as independent of the origin while the mean is dependent on it. Adding a bonus of $500$ shillings to every wage raises the mean by $500$ and leaves the spread exactly as it was.

### 2.4 Changing the scale changes the spread predictably

Multiplying every observation by a constant stretches or shrinks the data, and the spread responds in a way that can be predicted exactly.

> **Theorem (Equivariance under scaling).** If $y_i = c x_i$ for a constant $c$, then $\bar{y} = c\bar{x}$, $s_y^2 = c^2 s_x^2$ and $s_y = \left|c\right| s_x$.

The standard deviation is multiplied by the size of the constant, ignoring its sign, because a standard deviation can never be negative. Doubling every wage doubles the standard deviation and quadruples the variance. Converting a set of lengths from metres to centimetres multiplies both the mean and the standard deviation by one hundred.

### 2.5 Grouped data: class marks and class width

When data are presented in classes, the individual observations are no longer available. Each class is represented by its midpoint, called the class mark, and every observation in the class is treated as if it sat at that midpoint.

> **Theorem (Grouped variance from class marks).** If class $j$ has mark $m_j$ and frequency $f_j$, and $n = \sum_{j=1}^{k} f_j$, then the grouped variance is $s^2 = \frac{1}{n}\sum_{j=1}^{k} f_j m_j^2 - \bar{x}^2$ with $\bar{x} = \frac{1}{n}\sum_{j=1}^{k} f_j m_j$.

The theorem is an exact statement about the substituted values, but only an approximation to the original data, because all variation inside a class has been erased. The error is bounded by the class width: the finer the classes, the closer the grouped variance is to the true variance of the raw observations.

### 2.6 Two groups combined: the mean

When two separate groups are merged, the mean of the merged group is not the simple average of the two group means. It is a weighted average, weighted by the sizes of the groups.

> **Theorem (Combined mean).** For two groups of sizes $n_1$ and $n_2$ with means $\bar{x}_1$ and $\bar{x}_2$, the combined mean is $\bar{x} = \frac{n_1\bar{x}_1 + n_2\bar{x}_2}{n_1 + n_2}$.

The reason is that the larger group contributes more observations to the total, so its mean deserves more weight. A group of $600$ workers must influence the overall average more than a group of $40$.

### 2.7 Two groups combined: the variance

The combined variance is the result that separates strong students from weak ones, because it is not the weighted average of the two variances.

> **Theorem (Combined variance).** For two groups as above with variances $s_1^2$ and $s_2^2$,
>
> $$s^2 = \frac{1}{n_1 + n_2}\left[n_1\left\{s_1^2 + \left(\bar{x}_1 - \bar{x}\right)^2\right\} + n_2\left\{s_2^2 + \left(\bar{x}_2 - \bar{x}\right)^2\right\}\right]$$

Each group contributes two things. The first is its own internal variance, which measures the spread inside the group. The second is the squared distance from the group's own mean to the combined mean, which measures how far the group as a whole sits from the overall centre. That second term is called the between-group contribution, and it is the term that careless candidates leave out.

The consequence is easy to see. If two groups have very different means, the combined variance is much larger than either group's variance, because merging them creates a spread that neither group had on its own. If the two group means are identical, the between-group term vanishes and the combined variance is just the size-weighted average of the two variances.

With more than two groups the same pattern continues: each group contributes its internal variance plus the squared gap between its own mean and the overall mean.

### 2.8 The second moment about any origin

There is a single identity that unifies the definition of the variance, the computational formula and the coding method. It connects the average squared distance from an arbitrary point to the average squared distance from the mean.

> **Theorem (Shift identity for the second moment).** For any constant $A$, $\frac{1}{n}\sum_{i=1}^{n}\left(x_i - A\right)^2 = s^2 + \left(\bar{x} - A\right)^2$.

Read the statement in words. On the left is the average squared distance from the arbitrary point $A$. On the right is the average squared distance from the mean, plus the squared distance from $A$ to the mean. The average squared distance from any point other than the mean is always larger, and the excess is exactly the squared gap between that point and the mean.

The formula is used in both directions. Solving for the variance gives $s^2 = \frac{1}{n}\sum_{i=1}^{n}\left(x_i - A\right)^2 - \left(\bar{x} - A\right)^2$, which is the assumed-mean method. Setting $A$ equal to zero gives the ordinary computational formula, because the average squared distance from zero is the mean of the squares and the squared gap from zero to the mean is the square of the mean.

### 2.9 Properties of the coefficient of variation

The coefficient of variation behaves differently from the other measures when the data are shifted or rescaled, and these differences are exactly why it is useful.

> **Theorem (Behaviour of the coefficient of variation).** The coefficient of variation is unchanged when every observation is multiplied by a positive constant. It is changed when a constant is added to every observation, and it is undefined when the mean is zero.

Multiplying all wages by a factor of two doubles both the standard deviation and the mean, so the ratio is untouched; the relative spread is genuinely the same. Adding a bonus to every wage raises the mean and leaves the standard deviation alone, so the ratio falls; the data really have become relatively less spread out.

The requirement that the mean be non-zero is not a technicality. If the mean is zero the ratio is either infinite or undefined, and its sign becomes meaningless. The requirement that the data be measured on a scale with a true zero is equally serious: temperatures in degrees Celsius have an arbitrary zero, so a coefficient of variation computed from them would change if the same temperatures were expressed in degrees Fahrenheit.

### 2.10 What a zero spread means

> **Theorem (Vanishing spread characterises constant data).** The variance, the standard deviation and the mean absolute deviation of a set of observations are all zero if and only if every observation has the same value.

All three measures are built from quantities that cannot be negative, namely squares and absolute values. A sum of non-negative terms can be zero only if every term is zero, and a term is zero only when the observation equals the mean. Therefore a zero spread forces every observation to equal the mean, which is to say that the data are constant. The converse is immediate: constant data have mean equal to the constant, so every deviation is zero.

### 2.11 The results collected

| Result | Statement | Where it is used |
|---|---|---|
| Zero-sum of deviations | Signed gaps from the mean add to zero | Justifies squaring or absolute values |
| Computational form | Variance is mean of squares minus square of mean | Fast hand computation |
| Translation invariance | Shifting all values leaves spread unchanged | Choosing a convenient origin |
| Scaling equivariance | Multiplying by $c$ multiplies the standard deviation by the size of $c$ | Changing units |
| Combined mean | Size-weighted average of the group means | Merging groups |
| Combined variance | Weighted sum of internal and between-group terms | Merging groups |
| Shift identity | Second moment about any point equals variance plus squared gap | Assumed-mean and coding methods |
| Vanishing spread | Zero spread if and only if all values are equal | Interpreting a zero answer |

## 3. Formal Proofs, Derivations, and Methods

### 3.1 Proof that the signed deviations sum to zero

Let the observations be $x_1, x_2, \dots, x_n$ with mean $\bar{x}$, which by definition satisfies $n\bar{x} = \sum_{i=1}^{n} x_i$. Adding a collection of terms can be split, so

$$
\sum_{i=1}^{n}\left(x_i - \bar{x}\right) = \sum_{i=1}^{n} x_i - \sum_{i=1}^{n}\bar{x} .
$$

The first sum on the right is $n\bar{x}$ by the definition of the mean. The second sum adds the same constant $\bar{x}$ exactly $n$ times, so it equals $n\bar{x}$. Therefore

$$
\sum_{i=1}^{n}\left(x_i - \bar{x}\right) = n\bar{x} - n\bar{x} = 0 .
$$

The proof shows why the mean is called the balance point: the positive gaps and the negative gaps are equal in total size. It also shows that averaging the signed gaps can never produce anything except zero, which rules that idea out as a measure of spread.

### 3.2 Derivation of the computational formula for the variance

Begin with the definition and expand the square inside the sum.

$$
s^2 = \frac{1}{n}\sum_{i=1}^{n}\left(x_i - \bar{x}\right)^2
$$

Expanding the bracket gives three terms, and summing each separately is legitimate because the sum of a total is the total of the sums.

$$
s^2 = \frac{1}{n}\sum_{i=1}^{n} x_i^2 - \frac{2\bar{x}}{n}\sum_{i=1}^{n} x_i + \frac{1}{n}\sum_{i=1}^{n}\bar{x}^2
$$

Now substitute the two known totals. The middle sum is $n\bar{x}$, and the last sum is $n\bar{x}^2$ because the constant $\bar{x}^2$ is added $n$ times. Hence

$$
s^2 = \frac{1}{n}\sum_{i=1}^{n} x_i^2 - 2\bar{x}^2 + \bar{x}^2 = \frac{1}{n}\sum_{i=1}^{n} x_i^2 - \bar{x}^2 .
$$

The same steps with frequencies in place of repeated observations give the frequency version, because a value repeated $f_i$ times contributes $f_i x_i^2$ to the first sum and $f_i x_i$ to the middle sum.

### 3.3 Derivation of the assumed-mean and coding formulas

Let $A$ be any chosen constant, called the assumed mean. Expand the average squared distance from $A$ in the same way as before.

$$
\frac{1}{n}\sum_{i=1}^{n}\left(x_i - A\right)^2 = \frac{1}{n}\sum_{i=1}^{n} x_i^2 - 2A\bar{x} + A^2
$$

Add and subtract $\bar{x}^2$ on the right-hand side so that the computational formula appears.

$$
\frac{1}{n}\sum_{i=1}^{n}\left(x_i - A\right)^2 = \left(\frac{1}{n}\sum_{i=1}^{n} x_i^2 - \bar{x}^2\right) + \bar{x}^2 - 2A\bar{x} + A^2
$$

The bracket is the variance, and the remaining three terms form a perfect square. Therefore

$$
\frac{1}{n}\sum_{i=1}^{n}\left(x_i - A\right)^2 = s^2 + \left(\bar{x} - A\right)^2 .
$$

Rearranging gives the assumed-mean formula for the variance.

$$
s^2 = \frac{1}{n}\sum_{i=1}^{n}\left(x_i - A\right)^2 - \left(\bar{x} - A\right)^2
$$

For the coding method, put $u_i = \frac{x_i - A}{h}$ with $h$ the class width, so that $x_i = A + h u_i$. Then every deviation scales and shifts together, and the standard deviation of the coded values is related to the original by $s_x = \left|h\right| s_u$, hence

$$
s_x^2 = h^2\left[\frac{1}{n}\sum_{i=1}^{n} u_i^2 - \bar{u}^2\right] .
$$

Because the coded values are usually small integers such as $-2$, $-1$, $0$, $1$ and $2$, the arithmetic is far lighter than squaring numbers in the hundreds.

### 3.4 Derivation of the combined variance

Write the combined mean as $\bar{x}$ and consider the squared deviations of the first group from that combined mean. Insert and subtract the first group's own mean inside the bracket.

$$
\sum_{i=1}^{n_1}\left(x_{1i} - \bar{x}\right)^2 = \sum_{i=1}^{n_1}\left[\left(x_{1i} - \bar{x}_1\right) + \left(\bar{x}_1 - \bar{x}\right)\right]^2
$$

Expanding the square produces three pieces: a squared term, a cross term and a constant term.

$$
\sum_{i=1}^{n_1}\left(x_{1i} - \bar{x}\right)^2 = \sum_{i=1}^{n_1}\left(x_{1i} - \bar{x}_1\right)^2 + 2\left(\bar{x}_1 - \bar{x}\right)\sum_{i=1}^{n_1}\left(x_{1i} - \bar{x}_1\right) + n_1\left(\bar{x}_1 - \bar{x}\right)^2
$$

The middle sum is zero by the zero-sum property, and the first sum equals $n_1 s_1^2$ by the definition of the first group's variance. Therefore

$$
\sum_{i=1}^{n_1}\left(x_{1i} - \bar{x}\right)^2 = n_1\left[s_1^2 + \left(\bar{x}_1 - \bar{x}\right)^2\right] .
$$

Repeating the argument for the second group and dividing the total by $n_1 + n_2$ gives the combined variance formula. The algebra also explains the name: the total sum of squares about the combined mean splits cleanly into a within-group part and a between-group part, with no leftover cross term.

### 3.5 Derivation of the rule for constants

Suppose every observation is transformed to $y_i = a + b x_i$. The mean transforms the same way, because averaging is linear.

$$
\bar{y} = \frac{1}{n}\sum_{i=1}^{n}\left(a + b x_i\right) = a + b\bar{x}
$$

Each deviation from the new mean is therefore $b$ times the old deviation.

$$
y_i - \bar{y} = \left(a + b x_i\right) - \left(a + b\bar{x}\right) = b\left(x_i - \bar{x}\right)
$$

Squaring multiplies by $b^2$, and averaging preserves that factor.

$$
s_y^2 = \frac{1}{n}\sum_{i=1}^{n} b^2\left(x_i - \bar{x}\right)^2 = b^2 s_x^2
$$

Taking square roots gives $s_y = \left|b\right| s_x$, with the absolute value needed because a standard deviation is never negative. The constant $a$ has vanished entirely, which is the algebraic statement that shifting data does not change its spread.

### 3.6 Method: variance of grouped data by coding

The following sequence is the standard examination route for grouped data and should be followed in this order every time.

1. Write the classes in order and confirm that they have a common width $h$; if they do not, the data are not suitable for the coding method.
2. Compute each class mark as the average of the class boundaries, not as the average of the printed limits when those differ from the boundaries.
3. Choose an assumed mean $A$ equal to a class mark near the middle of the distribution, and a scale $h$ equal to the common class width.
4. Form the coded values $u_j = \frac{m_j - A}{h}$, which should be small whole numbers running from a negative value to a positive value.
5. Compute the three totals: the total frequency $n$, the total $\sum f_j u_j$ and the total $\sum f_j u_j^2$.
6. Compute the coded mean $\bar{u} = \frac{1}{n}\sum f_j u_j$ and the coded variance $s_u^2 = \frac{1}{n}\sum f_j u_j^2 - \bar{u}^2$.
7. Convert back with $\bar{x} = A + h\bar{u}$ and $s_x^2 = h^2 s_u^2$, then take the positive square root for the standard deviation.
8. Check that the answer is plausible: a grouped standard deviation is usually between one fifth and one half of the class width multiplied by the number of classes that actually carry data, and it can never exceed half the range.

### 3.7 Method: quartiles and quartile deviation for grouped data

1. Accumulate the frequencies to obtain the cumulative frequency of each class, and confirm that the final total equals $n$.
2. Locate the class containing the first quartile by finding the first class whose cumulative frequency reaches $\frac{n}{4}$.
3. Locate the class containing the third quartile by finding the first class whose cumulative frequency reaches $\frac{3n}{4}$.
4. Apply the interpolation formula to each, using the lower boundary of the class, the cumulative frequency of the classes below it, the frequency of the class itself and the class width.
5. Subtract to obtain the interquartile range, halve it for the quartile deviation, and divide the difference by the sum of the quartiles for the coefficient.
6. Check that $Q_1$ is below the median and the median below $Q_3$; an ordering error means a cumulative frequency was misread.

### 3.8 Method: comparing two data sets with the coefficient of variation

1. Compute the mean of each data set separately, keeping at least three decimal places.
2. Compute the standard deviation of each data set separately, using the computational formula.
3. Divide each standard deviation by its own mean and multiply by one hundred to obtain two percentages.
4. Compare the two percentages, never the two standard deviations, because the means differ.
5. State the conclusion in words, naming the data set with the smaller coefficient of variation as the more consistent or less variable one.
6. State what the comparison does not show, since a coefficient of variation says nothing about the shape of the distribution or about the size of the values themselves.

## 4. Representative Worked Examples and Solutions

### 4.1 Problem: the range and the coefficient of range

Find the range and the coefficient of range of the daily takings, in shillings, given as $20$, $21$, $15$, $10$, $7$, $4$, $51$ and $49$.

### 4.2 Solution: identify the two extremes and subtract

Step 1. Scan the list for the greatest value. The largest number present is $51$, so $x_g = 51$.

Step 2. Scan the list for the smallest value. The smallest number present is $4$, so $x_l = 4$.

Step 3. Subtract the smallest from the greatest.

$$
R = x_g - x_l = 51 - 4 = 47
$$

Step 4. Divide the range by the sum of the extremes to obtain the unit-free version.

$$
\frac{x_g - x_l}{x_g + x_l} = \frac{47}{55} \approx 0.855
$$

Step 5. Interpret. The takings span a band of $47$ shillings, and that band is about eighty-five per cent as wide as the combined level of the best and worst days. Because only two days entered the calculation, the figure says nothing about the other six.

### 4.3 Problem: standard deviation from the definition

Compute the standard deviation of the eight observations $120$, $60$, $70$, $30$, $150$, $100$, $180$ and $50$.

### 4.4 Solution: average the squared gaps and take the root

Step 1. Add the observations.

$$
\sum_{i=1}^{8} x_i = 120 + 60 + 70 + 30 + 150 + 100 + 180 + 50 = 760
$$

Step 2. Divide by the count to obtain the mean.

$$
\bar{x} = \frac{760}{8} = 95
$$

Step 3. Form each gap from the mean and square it.

$$
\begin{aligned}
(120-95)^2 &= 625, & (60-95)^2 &= 1225, \\
(70-95)^2 &= 625, & (30-95)^2 &= 4225, \\
(150-95)^2 &= 3025, & (100-95)^2 &= 25, \\
(180-95)^2 &= 7225, & (50-95)^2 &= 2025 .
\end{aligned}
$$

Step 4. Add the eight squared gaps.

$$
\sum_{i=1}^{8}\left(x_i - \bar{x}\right)^2 = 625 + 1225 + 625 + 4225 + 3025 + 25 + 7225 + 2025 = 19000
$$

Step 5. Divide by the count to obtain the variance.

$$
s^2 = \frac{19000}{8} = 2375
$$

Step 6. Take the positive square root to return to the original units.

$$
s = \sqrt{2375} \approx 48.73
$$

Step 7. Interpret. A typical observation sits about $48.7$ units from the mean of $95$, which is a very wide spread relative to the centre, and the range of $130$ confirms that the data are widely scattered.

### 4.5 Problem: variance by the computational formula

Find the variance and standard deviation of $12$, $6$, $7$, $9$, $15$, $13$, $18$ and $11$.

### 4.6 Solution: two totals and one subtraction

Step 1. Add the observations.

$$
\sum_{i=1}^{8} x_i = 12 + 6 + 7 + 9 + 15 + 13 + 18 + 11 = 91
$$

Step 2. Divide by the count.

$$
\bar{x} = \frac{91}{8} = 11.375
$$

Step 3. Square the mean, keeping the full precision.

$$
\bar{x}^2 = 11.375^2 = 129.390625
$$

Step 4. Square each observation and add the squares.

$$
\sum_{i=1}^{8} x_i^2 = 144 + 36 + 49 + 81 + 225 + 169 + 324 + 121 = 1149
$$

Step 5. Divide the sum of squares by the count.

$$
\frac{1}{8}\sum_{i=1}^{8} x_i^2 = \frac{1149}{8} = 143.625
$$

Step 6. Subtract the square of the mean.

$$
s^2 = 143.625 - 129.390625 = 14.234375
$$

Step 7. Take the positive square root.

$$
s = \sqrt{14.234375} \approx 3.77
$$

Step 8. Interpret. The variance is about $14.23$ in squared units and the standard deviation is about $3.77$ in the original units, so a typical observation lies within about four units of the mean of $11.4$.

### 4.7 Problem: a frequency distribution

The marks of $30$ students in a quiz marked out of $20$ are recorded as follows: $2$ students scored $8$, $3$ scored $9$, $4$ scored $10$, $4$ scored $11$, $5$ scored $12$, $3$ scored $14$, $3$ scored $15$, $3$ scored $17$, $2$ scored $18$ and $1$ scored $20$. Find the variance and the standard deviation.

### 4.8 Solution: build the working table

Step 1. Set out the marks, their frequencies, the products of frequency and mark, and the products of frequency and squared mark.

| Mark $x$ | Frequency $f$ | $fx$ | $fx^2$ |
|---|---|---|---|
| $8$ | $2$ | $16$ | $128$ |
| $9$ | $3$ | $27$ | $243$ |
| $10$ | $4$ | $40$ | $400$ |
| $11$ | $4$ | $44$ | $484$ |
| $12$ | $5$ | $60$ | $720$ |
| $14$ | $3$ | $42$ | $588$ |
| $15$ | $3$ | $45$ | $675$ |
| $17$ | $3$ | $51$ | $867$ |
| $18$ | $2$ | $36$ | $648$ |
| $20$ | $1$ | $20$ | $400$ |
| Total | $30$ | $381$ | $5153$ |

Step 2. Read the totals from the table and confirm that the frequencies sum to the stated number of students.

$$
n = \sum f = 30, \qquad \sum fx = 381, \qquad \sum fx^2 = 5153
$$

Step 3. Compute the mean.

$$
\bar{x} = \frac{381}{30} = 12.7
$$

Step 4. Compute the mean of the squared marks.

$$
\frac{1}{n}\sum fx^2 = \frac{5153}{30} = 171.7667
$$

Step 5. Subtract the square of the mean.

$$
s^2 = 171.7667 - 12.7^2 = 171.7667 - 161.29 = 10.4767
$$

Step 6. Take the positive square root.

$$
s = \sqrt{10.4767} \approx 3.24
$$

Step 7. Interpret. The standard deviation of about $3.24$ marks means that a typical student's mark lies roughly three marks away from the average mark of $12.7$ out of $20$.

### 4.9 Problem: grouped data by the coding method

A distribution has the classes $5\text{–}9$, $10\text{–}14$, $15\text{–}19$, $20\text{–}24$, $25\text{–}29$ and $30\text{–}34$ with frequencies $3$, $4$, $6$, $5$, $4$ and $3$. Using an assumed mean of $17$ and the common class width, find the mean and the standard deviation.

### 4.10 Solution: code, compute, convert back

Step 1. Compute the class marks, which are the midpoints of the classes: $7$, $12$, $17$, $22$, $27$ and $32$.

Step 2. Confirm the common class width. Consecutive marks differ by $5$, so $h = 5$, and the assumed mean $A = 17$ is the third class mark.

Step 3. Form the coded values $u = \frac{m - 17}{5}$, obtaining $-2$, $-1$, $0$, $1$, $2$ and $3$.

Step 4. Accumulate the three totals.

| Class | Mark $m$ | $f$ | $u$ | $fu$ | $fu^2$ |
|---|---|---|---|---|---|
| $5\text{–}9$ | $7$ | $3$ | $-2$ | $-6$ | $12$ |
| $10\text{–}14$ | $12$ | $4$ | $-1$ | $-4$ | $4$ |
| $15\text{–}19$ | $17$ | $6$ | $0$ | $0$ | $0$ |
| $20\text{–}24$ | $22$ | $5$ | $1$ | $5$ | $5$ |
| $25\text{–}29$ | $27$ | $4$ | $2$ | $8$ | $16$ |
| $30\text{–}34$ | $32$ | $3$ | $3$ | $9$ | $27$ |
| Total | | $25$ | | $12$ | $64$ |

Step 5. Compute the coded mean.

$$
\bar{u} = \frac{12}{25} = 0.48
$$

Step 6. Convert to the original scale.

$$
\bar{x} = A + h\bar{u} = 17 + 5(0.48) = 17 + 2.4 = 19.4
$$

Step 7. Compute the coded variance.

$$
s_u^2 = \frac{64}{25} - 0.48^2 = 2.56 - 0.2304 = 2.3296
$$

Step 8. Convert to the original scale by multiplying by the square of the class width.

$$
s_x^2 = h^2 s_u^2 = 25(2.3296) = 58.24
$$

Step 9. Take the positive square root.

$$
s_x = \sqrt{58.24} \approx 7.63
$$

Step 10. Interpret. The average of the distribution is about $19.4$ and a typical class mark lies about $7.63$ units from that average, which is roughly one and a half class widths.

### 4.11 Problem: quartiles and quartile deviation

A distribution of the marks of $100$ candidates uses the classes $10\text{–}20$, $20\text{–}30$, $30\text{–}40$, $40\text{–}50$, $50\text{–}60$, $60\text{–}70$ and $70\text{–}80$ with frequencies $8$, $14$, $22$, $26$, $16$, $10$ and $4$. Find the quartile deviation and its coefficient.

### 4.12 Solution: locate the classes and interpolate

Step 1. Accumulate the frequencies: $8$, $22$, $44$, $70$, $86$, $96$ and $100$. The total is $n = 100$.

Step 2. Locate the first quartile. One quarter of $100$ is $25$, and the first cumulative frequency reaching $25$ is $44$, so $Q_1$ lies in the class $30\text{–}40$.

Step 3. Interpolate for $Q_1$, using the lower boundary $30$, the cumulative frequency $22$ below the class, the class frequency $22$ and the class width $10$.

$$
Q_1 = 30 + \frac{25 - 22}{22}\left(10\right) = 30 + 1.36 = 31.36
$$

Step 4. Locate the third quartile. Three quarters of $100$ is $75$, and the first cumulative frequency reaching $75$ is $86$, so $Q_3$ lies in the class $50\text{–}60$.

Step 5. Interpolate for $Q_3$, using the lower boundary $50$, the cumulative frequency $70$ below the class, the class frequency $16$ and the class width $10$.

$$
Q_3 = 50 + \frac{75 - 70}{16}\left(10\right) = 50 + 3.125 = 53.125
$$

Step 6. Compute the interquartile range.

$$
Q_3 - Q_1 = 53.125 - 31.36 = 21.765
$$

Step 7. Halve it for the quartile deviation.

$$
Q = \frac{21.765}{2} \approx 10.88
$$

Step 8. Divide by the sum of the quartiles for the coefficient.

$$
\frac{Q_3 - Q_1}{Q_3 + Q_1} = \frac{21.765}{84.485} \approx 0.258
$$

Step 9. Interpret. The middle half of the candidates spans about $21.8$ marks, the quartile deviation is about $10.9$ marks, and the coefficient of about $0.258$ is unit-free, so it could be compared directly with the coefficient of quartile deviation of a different examination.

### 4.13 Problem: two groups combined

A class of $40$ students in one school has a mean score of $60$ with a standard deviation of $8$. A class of $60$ students in another school has a mean score of $70$ with a standard deviation of $6$. Find the mean and the standard deviation of the combined group of $100$ students.

### 4.14 Solution: weight the means, then decompose the variance

Step 1. Write down the four given quantities.

$$
n_1 = 40, \quad \bar{x}_1 = 60, \quad s_1^2 = 64, \qquad n_2 = 60, \quad \bar{x}_2 = 70, \quad s_2^2 = 36
$$

Step 2. Compute the combined mean as the size-weighted average.

$$
\bar{x} = \frac{40(60) + 60(70)}{40 + 60} = \frac{2400 + 4200}{100} = 66
$$

Step 3. Compute the two gaps between the group means and the combined mean.

$$
\bar{x}_1 - \bar{x} = 60 - 66 = -6, \qquad \bar{x}_2 - \bar{x} = 70 - 66 = 4
$$

Step 4. Build each group's contribution, which is its internal variance plus the square of its gap.

$$
s_1^2 + \left(\bar{x}_1 - \bar{x}\right)^2 = 64 + 36 = 100
$$

$$
s_2^2 + \left(\bar{x}_2 - \bar{x}\right)^2 = 36 + 16 = 52
$$

Step 5. Weight each contribution by the group size and add.

$$
40(100) + 60(52) = 4000 + 3120 = 7120
$$

Step 6. Divide by the combined size.

$$
s^2 = \frac{7120}{100} = 71.2
$$

Step 7. Take the positive square root.

$$
s = \sqrt{71.2} \approx 8.44
$$

Step 8. Interpret. The combined variance of $71.2$ exceeds both group variances of $64$ and $36$, even though each group on its own is fairly tight. The excess is the between-group contribution, created by the ten-mark gap between the two school means.

### 4.15 Problem: which group is more consistent

In an examination the mean mark of a group of $125$ students in English was $75$ with a standard deviation of $6$, while in mathematics the mean was $70$ with a standard deviation of $7$. In which subject was there greater variability?

### 4.16 Solution: compare percentages, not raw spreads

Step 1. Compute the coefficient of variation for English.

$$
C.V_{\text{E}} = \frac{6}{75}\left(100\%\right) = 8\%
$$

Step 2. Compute the coefficient of variation for mathematics.

$$
C.V_{\text{M}} = \frac{7}{70}\left(100\%\right) = 10\%
$$

Step 3. Compare the two percentages. Since $10\%$ exceeds $8\%$, mathematics shows the greater relative variability.

Step 4. Interpret carefully. The raw standard deviation is also larger in mathematics, but that alone would not settle the question, because the two means differ. The coefficient of variation shows that the difference survives the adjustment for the level of the marks, so mathematics is genuinely the more variable and English the more consistent subject.

### 4.17 Problem: the mean absolute deviation

Find the mean absolute deviation about the mean of the observations $4$, $8$, $10$, $12$ and $16$, and compare it with the standard deviation.

### 4.18 Solution: absolute gaps, then average

Step 1. Compute the mean.

$$
\bar{x} = \frac{4 + 8 + 10 + 12 + 16}{5} = \frac{50}{5} = 10
$$

Step 2. Write down each gap and take its absolute value: $-6$ becomes $6$, $-2$ becomes $2$, $0$ stays $0$, $2$ stays $2$ and $6$ stays $6$.

Step 3. Add the absolute gaps.

$$
\sum_{i=1}^{5}\left|x_i - \bar{x}\right| = 6 + 2 + 0 + 2 + 6 = 16
$$

Step 4. Divide by the count.

$$
\text{M.A.D.} = \frac{16}{5} = 3.2
$$

Step 5. Compute the variance for comparison, using the squares of the same gaps, which are $36$, $4$, $0$, $4$ and $36$.

$$
s^2 = \frac{36 + 4 + 0 + 4 + 36}{5} = \frac{80}{5} = 16
$$

Step 6. Take the square root.

$$
s = \sqrt{16} = 4
$$

Step 7. Compare. The mean absolute deviation is $3.2$ and the standard deviation is $4$. The standard deviation is larger, as it must be, because squaring gives the two large gaps of $6$ disproportionate weight. Both are measured in the original units and both describe a typical distance from the mean, but neither is numerically equal to the other.

## 5. Mathematical Extensions, Limits, and Common Errors

### 5.1 Where each measure stops being useful

Every measure of dispersion has a domain in which it is the right tool and a boundary beyond which it misleads. The range is useful as a first look at a set of numbers and as a check when reading a table, but it stops being useful the moment the data are known to contain recording errors or genuine extreme values, because it will report those errors as the whole story. It is also useless for comparing two data sets whose levels differ, since a range of $50$ on a mean of $100$ and a range of $50$ on a mean of $5000$ say nothing about one another until each is divided by a comparable quantity.

The quartile deviation is the right tool when the data are skewed or when the tails are unreliable, because it deliberately ignores the outer quarters. It stops being useful when the behaviour of the tails is exactly the question being asked, as it is in the study of extreme losses, worst-case waiting times or the spread of the very largest incomes. It also requires the data to be ordered and, for grouped data, requires interpolation, so it is slower to compute than the range and more exposed to mistakes in the cumulative frequency column.

The variance is the right tool whenever data sets are to be combined, transformed or used in later theory, because it obeys the clean algebraic rules derived in Section 3. It stops being useful when the answer has to be spoken about in the units of the data, since squared shillings mean nothing, and when the data contain a few huge values, since squaring exaggerates them out of all proportion. The standard deviation repairs the units but inherits the sensitivity to extremes. The coefficient of variation repairs the units problem across data sets but requires a genuine ratio scale with a positive mean, so it cannot be applied to temperatures measured in degrees Celsius or to data whose mean is near zero.

### 5.2 The mistakes beginners make most often

The following errors account for most of the lost marks in this topic, and each is worth reading twice.

- **Averaging the signed gaps.** The signed gaps always add to zero, so this produces zero for every data set. Nothing has been measured; the arithmetic has simply proved the zero-sum theorem.
- **Subtracting in the wrong order in the short formula.** The variance is the mean of the squares minus the square of the mean. Writing the square of the mean first produces a negative number, which is impossible for a variance and is an immediate signal that the subtraction is reversed.
- **Squaring the sum instead of the mean.** In the short formula the quantity to be squared is $\bar{x}$, the mean, not $\sum x_i$, the total.
- **Forgetting the square root.** A variance of $144$ is not a standard deviation of $144$. The standard deviation is $12$.
- **Reporting the variance in the units of the data.** A variance is in squared units. A variance of $144$ square marks cannot be described as $144$ marks.
- **Using the printed class limits as though they were class boundaries.** For classes written as $10\text{–}19$, $20\text{–}29$, the width is $10$, not $9$, because the boundaries are $9.5$ and $19.5$. Using $19 - 10 = 9$ understates every subsequent quantity.
- **Dividing by the number of classes instead of the number of observations.** The divisor in every formula in this topic is $n$, the total frequency, not $k$, the number of rows.
- **Omitting the between-group term in a combined variance.** The weighted average of the two variances alone is always too small whenever the group means differ, and it can be very much too small.
- **Inverting the coefficient of variation.** The formula is the standard deviation divided by the mean, not the mean divided by the standard deviation, and the interpretation is that a larger value means more variability, not less.
- **Comparing raw standard deviations across data sets with different means.** This is the single most common error in comparison questions, and the coefficient of variation exists precisely to prevent it.

### 5.3 Saying what the numbers mean

A number without a sentence is only half an answer. The standard deviation is best read as the size of a typical gap between an observation and the mean, so a standard deviation of $3.24$ marks means that a typical student's mark sits about three marks from the class average. The variance is best read as the same quantity squared, so it is useful for calculation and for comparison but not for description. The range is best read as the width of the whole list, which is useful for a quick impression of how far the data stretch. The quartile deviation is best read as the half-width of the band that contains the middle half of the observations, so it tells you how tightly the typical middle is packed. The coefficient of variation is best read as the spread expressed as a percentage of the mean, so a value of $15$ per cent means that the typical distance from the centre is about fifteen per cent of the centre itself.

### 5.4 How the topic fits together

The five measures in this topic are not five unrelated formulas but a single idea approached at five levels of refinement. The range is the crudest reading of spread, taking the whole width of the data and trusting two values to represent it. The quartile deviation is a trimmed version of the same width, trusting the middle half instead of the two extremes. The mean absolute deviation is the first measure that uses every observation, and it measures spread as an average distance. The variance measures the same average distance but squares before averaging, which buys the algebraic properties that make combination and transformation possible at the cost of a distorted unit. The standard deviation restores the unit, and the coefficient of variation removes it altogether so that different data sets can be placed on a common footing.

Seen this way, the examinable skill is not the ability to recite seven formulas but the ability to choose the right one and to read the number back into the situation. A question that asks which of two firms pays more evenly is asking for a comparison of relative spread and therefore for the coefficient of variation. A question that asks how much a combined group varies is asking for the decomposition into internal and between-group parts. A question that asks for the spread of a skewed income distribution is asking for the quartile deviation, because the extreme incomes would destroy a standard deviation. A question that asks for the width of a production tolerance is asking for a range or a standard deviation depending on whether the extremes or the typical deviation is meant. Every one of these choices is a decision about which measure answers the question actually asked, and that decision is where most of the marks in this topic are won or lost.
