## 1. Foundational Concepts, Definitions, and Axioms

### 1.1 The empirical distribution as the object of study

A data set is a finite list of observations. Before any inference is attempted, the list must be reorganised into something a human being can inspect. Data representation is the systematic study of that reorganisation: it produces tables and graphs which are, in a strict sense, equivalent descriptions of the same finite set of numbers, ordered so that shape becomes visible.

The organising idea is the **empirical distribution**. Given observations $x_1, \dots, x_n$, the empirical distribution is the function that records, for each admissible value or range of values, how many observations fall there. Every table and every graph in this topic is a representation of that one function. A frequency table evaluates it at points; a histogram draws it as area; a frequency polygon draws it as a profile; an ogive draws its running sum; a box plot compresses it to five order statistics. Recognising that all six are views of a single object is what allows a reader to move between them without losing or double-counting information.

### 1.2 Definitions of the elementary terms

> **Definition (Observation and variable).** An observation is one recorded value of the characteristic under study, and a variable is that characteristic itself. The $i$-th observation is written $x_i$.

> **Definition (Frequency).** The frequency of a value or class is the number of observations taking that value or falling in that class. It is written $f$ and is always a non-negative integer.

> **Definition (Frequency distribution).** A frequency distribution is a table in which the observations are partitioned into classes, and each class is displayed alongside its frequency. If there are $k$ classes with frequencies $f_1, \dots, f_k$ and $n$ observations, then the frequencies satisfy $\sum_{j=1}^{k} f_j = n$.

The word partition is doing real work in that definition. A partition has two properties, and both are requirements rather than conveniences.

- **Exhaustiveness:** every observation lies in some class. A table that omits a class loses observations, and its total falls short of $n$.
- **Mutual exclusivity:** no observation lies in two classes. A table whose classes overlap counts observations twice, and its total exceeds $n$.

Everything in this note depends on the table being a genuine partition.

> **Definition (Relative frequency).** The relative frequency of class $j$ is $f_j/n$, the proportion of the data set lying in that class. Its percentage form is $100 f_j/n$.

> **Definition (Cumulative frequency).** For classes ordered from smallest to largest, the cumulative frequency of class $j$ is $F_j = f_1 + f_2 + \cdots + f_j$, the number of observations in class $j$ or any earlier class. Equivalently, it is the number of observations at or below the upper class boundary of class $j$.

### 1.3 Discrete and grouped distributions

A **discrete (ungrouped) frequency distribution** assigns one row to each distinct observed value. It is appropriate when the variable advances in indivisible steps: a count of goals, a number of children, a number of rooms. Between two adjacent admissible values there is nothing.

A **grouped frequency distribution** assigns one row to each of several intervals. It is appropriate when the variable is continuous, so that a finer instrument would produce a new distinct value for almost every observation. Grouping replaces each individual value by the interval that contains it.

The two forms trade detail against compactness. A discrete table of a continuous variable would have as many rows as observations and would display nothing but noise; a grouped table of a discrete variable with few distinct values would destroy information for no benefit. The decision rule is therefore about the number of distinct values relative to $n$, and about whether the underlying scale is continuous.

The loss incurred by grouping is exact and quantifiable. Once grouped, the data are described by counts per interval only, and every statistic computed from the table is a statistic of the interval midpoints rather than of the observations. Section 2.7 gives a sharp bound on the resulting error.

### 1.4 The apparatus of classes

> **Definition (Class, class interval, class limits).** A class is one group of a grouped distribution. Its label, written with two numbers separated by a dash, is the class interval, for example $50\text{–}52$. The two numbers are the class limits: the lower class limit $a$ on the left and the upper class limit $b$ on the right.

> **Definition (Class boundaries).** The class boundaries, also called the true class limits, are the points at which one class gives way to the next. The boundary between a class ending at upper limit $b$ and the next class beginning at lower limit $a'$ is
>
> $$
> b_{\text{join}} = \frac{b + a'}{2}.
> $$
>
> The half-gap $(a' - b)/2$ is applied at the two outer ends of the table as well, so that the first class acquires a lower boundary and the last class an upper boundary.

> **Definition (Class width).** The class width, or class size, of class $j$ is $h_j = u_j - \ell_j$, where $\ell_j$ and $u_j$ are its lower and upper boundaries. The classes of a table are called equal-width when all $h_j$ are the same.

> **Definition (Class mark).** The class mark of class $j$ is the midpoint of its boundaries,
>
> $$
> m_j = \frac{\ell_j + u_j}{2}.
> $$

For the classes $50\text{–}52$, $53\text{–}55$, $56\text{–}58$, $59\text{–}61$ and $62\text{–}64$ the boundaries are $49.5$, $52.5$, $55.5$, $58.5$, $61.5$ and $64.5$; every width is $3$; and the marks are $51$, $54$, $57$, $60$ and $63$.

### 1.5 The graphical vocabulary

> **Definition (Histogram).** A histogram represents a grouped frequency distribution by rectangles whose bases are the class boundaries and whose heights are equal to the class frequencies, valid when the widths are equal. Adjacent rectangles share an edge, and the total area is $n$ times the common width.

> **Definition (Density histogram).** When the class widths differ, the height of the rectangle over class $j$ is the frequency density $f_j/h_j$. The area of the rectangle is then exactly $f_j$, and the area over any interval equals the number of observations in that interval.

> **Definition (Frequency polygon).** The frequency polygon plots the point $(m_j, f_j)$ for each class and joins consecutive points by straight segments. It is the locus of the midpoints of the tops of the histogram rectangles, closed to the horizontal axis by one empty class at each end.

> **Definition (Ogive).** The ogive, or cumulative frequency curve, plots $(u_j, F_j)$ for each class, where $u_j$ is the upper boundary and $F_j$ the cumulative frequency, and joins consecutive points by straight segments.

> **Definition (Bar chart).** A bar chart represents each category by a rectangle of constant width, separated from its neighbours by gaps, whose height is proportional to the category frequency. It encodes magnitude by length and asserts nothing about adjacency on a scale.

The bar chart has four standard forms, and the choice among them is determined by the comparison the reader must make.

| Form | Construction | Appropriate when |
| --- | --- | --- |
| Simple bar chart | One bar per category, height equal to the frequency | Comparing the sizes of several categories at one point in time |
| Component bar chart | One bar per group, subdivided into segments proportional to the parts, heights equal to group totals | Showing the total of each group and its breakdown at the same time |
| Percentage component bar chart | As a component bar chart but every bar rescaled to a total of $100$ | Comparing composition between groups whose totals differ |
| Multiple bar chart | Two or more bars side by side within each category | Comparing the same categories across two or three groups or periods |

> **Definition (Pie chart).** A pie chart divides a circle into sectors, one per category, such that the area, and hence the angle, of each sector is proportional to the category frequency.

> **Definition (Line graph and time series).** A line graph plots a quantity against an ordered horizontal axis and joins consecutive plotted points. When the horizontal axis is time the data are a time series, and the graph displays the sequence, the direction of change and the speed of change.

> **Definition (Stem-and-leaf display).** A stem-and-leaf display writes each observation as a stem, formed from its leading digits, and a leaf, formed from a single trailing digit, grouping all leaves with the same stem on one row.

> **Definition (Box plot).** A box plot represents the five-number summary of a data set — minimum, lower quartile $Q_1$, median $Q_2$, upper quartile $Q_3$, maximum — by a box from $Q_1$ to $Q_3$ with a line at $Q_2$, and whiskers extending to the extreme values that are not classified as outliers.

### 1.6 Scales of measurement and admissible displays

The scale on which a variable is measured determines which arithmetic is meaningful and therefore which display is honest.

| Scale | Property | Admissible displays |
| --- | --- | --- |
| Nominal | Distinct labels only; no order | Simple bar chart, component bar chart, pie chart |
| Ordinal | Ordered labels; distances not measurable | Bar chart in scale order, percentage component bar chart |
| Interval | Equal distances; arbitrary zero | Histogram, frequency polygon, ogive, box plot, line graph |
| Ratio | Equal distances and a true zero | All of the interval displays, plus statements that use ratios |

The reasoning behind each row is the same. A display asserts a relationship, and the assertion must be supported by the measurement structure. A line graph between two nominal categories asserts that intermediate positions are meaningful, which is false. A pie chart of interval data asserts that the zero of the scale is meaningful for ratios of sector sizes, which is why ratios of temperatures in degrees Celsius are not used in that way. A histogram of ordinal categories asserts that the categories are contiguous intervals of a single scale, which may or may not be true.

### 1.7 The conventions that make a table a partition

Two conventions must be stated explicitly, because the arithmetic of the table is not defined without them.

- **Boundary convention.** An observation exactly equal to a class boundary belongs to the class whose lower boundary it is. This makes the classes half-open intervals $[\ell_j, u_j)$ and guarantees mutual exclusivity.
- **Rounding convention.** The written limits must reflect the precision of the measurements. If masses are recorded to the nearest kilogram, then the class $50\text{–}52$ covers masses from $49.5$ up to but not including $52.5$, and the half-unit offset is correct. If masses were recorded to the nearest $0.1$ kilogram, the offset would be $0.05$.

Changing either convention changes the frequencies, so a table without a stated convention is ambiguous.

## 2. Theorems, Lemmas, and Analytical Properties

### 2.1 Lemma (frequency and relative-frequency normalisation)

Let classes $1, \dots, k$ form a partition of $n$ observations, with class frequencies $f_j$. Then

$$
\sum_{j=1}^{k} f_j = n, \qquad \sum_{j=1}^{k} \frac{f_j}{n} = 1, \qquad 0 \le \frac{f_j}{n} \le 1 .
$$

The three statements are the arithmetic content of the word partition. The first says nothing has been lost or duplicated; the second says the shares exhaust the whole; the third says a share cannot exceed the whole or be negative.

### 2.2 Lemma (boundary, width and mark identities)

For a class with limits $a$ and $b$ written at precision $p$, so that the boundary offset is $\delta = p/2$, the boundaries are $\ell = a - \delta$ and $u = b + \delta$, and

$$
h = b - a + 2\delta, \qquad m = \frac{\ell + u}{2} = \frac{a + b}{2} .
$$

Two points follow. First, the width exceeds the difference of the printed limits by $2\delta$, which for integer limits at unit precision is exactly one. Second, the class mark is unchanged whether it is computed from the limits or from the boundaries, because the two offsets cancel. This is why the class mark may be reported as the average of the printed limits without error, while the class width may not be reported as their difference.

A further identity is useful when the classes are consecutive. If $\ell_1 < \ell_2 < \cdots < \ell_{k+1}$ are the boundaries and the widths are equal to $h$, then the marks form an arithmetic progression,

$$
m_j = m_1 + (j-1)h,
$$

because consecutive marks are separated by exactly one width. This is the reason a frequency polygon of an equal-width table has its plotted points uniformly spaced along the horizontal axis.

### 2.3 Theorem (cumulative frequency is a step function)

Let the boundaries of a grouped distribution be $\ell_1 < \ell_2 < \cdots < \ell_{k+1}$, with class $j$ equal to the half-open interval $[\ell_j, \ell_{j+1})$ carrying frequency $f_j$, and let $F : \mathbb{R} \to \mathbb{R}$ be defined by

$$
F(x) = \sum_{j \,:\, \ell_{j+1} \le x} f_j .
$$

Then:

1. $F(x) = 0$ for all $x < \ell_1$.
2. $F$ is non-decreasing: if $x \le y$ then $F(x) \le F(y)$.
3. $F$ is constant on each half-open interval $[\ell_j, \ell_{j+1})$, so $F$ is a step function whose only points of increase are the boundaries.
4. $F$ is right-continuous: $F(\ell_{j+1}) = \lim_{x \to \ell_{j+1}^{+}} F(x)$ for every boundary.
5. The jump at the boundary $\ell_{j+1}$ equals $f_j$, that is $F(\ell_{j+1}) - F(\ell_{j+1}^{-}) = f_j$.
6. $F(x) = n$ for all $x \ge \ell_{k+1}$.

The theorem says that the cumulative frequency column of a table is a sampling of a staircase, and that the staircase is the exact empirical description of the grouped data. The ogive in the next theorem is a smooth replacement for that staircase, and the difference between the two is the interpolation error analysed in Section 3.3.

### 2.4 Theorem (the ogive and its interpolation error)

Let $G$ be the piecewise-linear function through the points $(\ell_{j+1}, F_j)$ for $j = 1, \dots, k$, extended by $G(x) = 0$ for $x \le \ell_1$ and $G(x) = n$ for $x \ge \ell_{k+1}$. Then on class $j$,

$$
G(x) = F_{j-1} + f_j \frac{x - \ell_j}{h_j}, \qquad \ell_j \le x \le \ell_{j+1},
$$

and $G$ satisfies

$$
F_{j-1} \le G(x) \le F_j, \qquad \left| G(x) - F(x) \right| \le f_j .
$$

Consequently the ogive never leaves the band bounded by the two cumulative frequencies of the class it crosses, and its deviation from the exact step function is at most one class frequency. If the observations inside each class are spread uniformly across the class, then $G(x)$ equals the number of observations at or below $x$ exactly, and the ogive is not an approximation at all.

### 2.5 Theorem (the frequency-density rule)

Let a grouped distribution have boundaries $\ell_1 < \cdots < \ell_{k+1}$, widths $h_j = \ell_{j+1} - \ell_j$ and frequencies $f_j$. Draw a rectangle over class $j$ of height $H_j$. The area over any union of whole classes is proportional to the number of observations in that union, with the same constant of proportionality for every such union, if and only if there is a single constant $c > 0$ with

$$
H_j = c \, \frac{f_j}{h_j} \qquad \text{for every } j .
$$

The conventional choice $c = 1$ makes the height the frequency density $f_j/h_j$, and then the area over class $j$ is exactly $f_j$ and the total area is exactly $n$.

The rule is therefore not an arbitrary convention but the unique assignment of heights, up to a common scale factor, that makes area read as count. When all widths are equal the rule collapses to $H_j = c f_j / h$, so height is proportional to frequency and an ordinary histogram with frequency on the vertical axis is the special case.

### 2.6 Corollary (proportion as area)

Under the frequency-density rule with $c = 1$, for any interval $[a, b]$ that is a union of whole classes,

$$
\frac{\text{area between } a \text{ and } b}{n} = \frac{\text{number of observations in } [a, b]}{n} = \text{relative frequency of } [a, b] .
$$

This corollary is the operational reason density histograms are used: the reader can estimate a proportion by comparing a shaded area with the total area, without knowing any frequencies.

### 2.7 Theorem (bound on the error of a grouped mean)

Let class $j$ have boundaries $\ell_j, u_j$, width $h_j$, frequency $f_j$ and class mark $m_j$, let $\bar{x}$ be the mean of the $n$ original observations and let

$$
\bar{x}_g = \frac{1}{n} \sum_{j=1}^{k} f_j m_j
$$

be the grouped mean. Then

$$
\left| \bar{x} - \bar{x}_g \right| \le \frac{1}{n} \sum_{j=1}^{k} \frac{f_j h_j}{2},
$$

and when all widths equal $h$ this simplifies to $\left| \bar{x} - \bar{x}_g \right| \le h/2$.

The bound says that grouping cannot move the mean by more than half a class width, whatever the shape of the data inside the classes. It is the precise form of the statement that a grouped mean is a summary rather than a measurement, and it tells the analyst exactly how much accuracy to buy by narrowing the classes.

### 2.8 Theorem (pie-chart proportionality)

Let a data set of $n$ observations be split into $k$ categories with frequencies $f_j$, and let $\theta_j$ be the angle of the sector assigned to category $j$. If the angles are required to be proportional to the frequencies and to exhaust the circle, then

$$
\theta_j = \frac{f_j}{n} \times 360^{\circ},
$$

and this assignment is the only one satisfying both requirements. Moreover $\sum_j \theta_j = 360^{\circ}$, and a category with twice the frequency of another receives exactly twice the angle.

### 2.9 Lemma (component and percentage component consistency)

Let a group have parts with frequencies $g_1, \dots, g_r$ and total $T = \sum_i g_i$. In a component bar chart the segment lengths are proportional to $g_i$; in a percentage component bar chart they are proportional to $100 g_i / T$. The two charts differ by the common factor $100/T$ applied within each group, so within a group the segments carry identical information. Across groups they do not: the component chart compares absolute part sizes, while the percentage component chart compares composition and deliberately discards the information about group totals.

### 2.10 Lemma (stem-and-leaf is a lossless regrouping)

A stem-and-leaf display with stem unit $10^{d}$ maps each observation $x$ to the pair $\left(\lfloor x/10^{d} \rfloor, x \bmod 10^{d}\right)$ and lists the leaves grouped by stem in increasing order. The map is injective on the recorded precision, so the display can be read back to recover the sorted data exactly. Grouping the display by stem produces classes of width $10^{d}$, so the display is simultaneously a table, an ordered list and a histogram.

### 2.11 Lemma (the box plot and its fences)

For a data set with quartiles $Q_1 \le Q_2 \le Q_3$, define the interquartile range $\mathrm{IQR} = Q_3 - Q_1$ and the fences

$$
L_f = Q_1 - 1.5\,\mathrm{IQR}, \qquad U_f = Q_3 + 1.5\,\mathrm{IQR} .
$$

Then $L_f < Q_1$ and $Q_3 < U_f$ whenever $\mathrm{IQR} > 0$, the box contains exactly the middle half of the observations in the sense of order statistics, and any observation outside the fences is separated from the bulk of the data by at least one and a half box lengths. The rule is a convention for flagging candidates for inspection, not a test of any hypothesis; for data drawn from a normal distribution approximately $0.7$ per cent of observations fall outside the fences, so a moderate number of flagged points is not evidence of anything unusual.

### 2.12 Theorem (order invariance of the median under monotone transformations)

If $g$ is a strictly increasing function and $M$ is the median of $x_1, \dots, x_n$, then $g(M)$ is the median of $g(x_1), \dots, g(x_n)$. The same holds for every quantile. This is why the median read from an ogive is unaffected by a change of units and why quantiles, unlike the mean, commute with transformations such as taking logarithms. It also explains why the median of grouped data can be estimated by interpolating along an axis that carries the original units.

## 3. Formal Proofs, Derivations, and Methods

### 3.1 Proof that the cumulative frequency is a non-decreasing step function

Define $F(x) = \sum_{j : \ell_{j+1} \le x} f_j$. For the six claims of Theorem 2.3:

**Claim 1.** If $x < \ell_1$ then no upper boundary is at most $x$, so the sum is empty and equals $0$.

**Claim 2.** Let $x \le y$. Every index $j$ counted in $F(x)$ satisfies $\ell_{j+1} \le x \le y$, so it is also counted in $F(y)$. Hence the index set for $F(x)$ is contained in that for $F(y)$, and since all $f_j \ge 0$,

$$
F(y) - F(x) = \sum_{j \,:\, x < \ell_{j+1} \le y} f_j \ge 0 .
$$

**Claim 3.** Suppose $\ell_m \le x < y < \ell_{m+1}$. No boundary lies strictly between $x$ and $y$, so the index set $\{j : \ell_{j+1} \le x\}$ equals $\{j : \ell_{j+1} \le y\}$, and $F(x) = F(y)$. Hence $F$ is constant on $[\ell_m, \ell_{m+1})$.

**Claim 4.** Take $x = \ell_{m+1}$. The indices with $\ell_{j+1} \le \ell_{m+1}$ are exactly $j = 1, \dots, m$, giving $F(\ell_{m+1}) = F_m$. For any $y$ with $\ell_{m+1} < y < \ell_{m+2}$ the same index set applies, so $F(y) = F_m$ and the right limit equals $F(\ell_{m+1})$.

**Claim 5.** Approaching $\ell_{m+1}$ from below, for $\ell_m < x < \ell_{m+1}$ the indices with $\ell_{j+1} \le x$ are $j = 1, \dots, m-1$, so $F(x) = F_{m-1}$. Therefore

$$
F(\ell_{m+1}) - F(\ell_{m+1}^{-}) = F_m - F_{m-1} = f_m .
$$

**Claim 6.** For $x \ge \ell_{k+1}$ every index $1, \dots, k$ is counted, so $F(x) = F_k = n$.

The staircase is therefore exact. Its flat treads are the classes and its risers are the class frequencies.

### 3.2 Proof of the interpolation formula for medians and quartiles

Let $M$ be a quantile of order $q$, meaning that a proportion $q$ of the observations lies at or below $M$, with $q = 1/2$ for the median, $q = 1/4$ for the lower quartile and $q = 3/4$ for the upper quartile. Suppose $M$ falls in class $j$, whose lower boundary is $\ell_j$, whose width is $h_j$, whose frequency is $f_j$, and whose cumulative frequency up to the previous class is $F_{j-1}$. The target count is $qn$.

Step 1. The number of observations still to be accounted for inside class $j$ is $qn - F_{j-1}$.

Step 2. Under the uniform-spread assumption, the proportion of class $j$ that must be crossed is

$$
\frac{qn - F_{j-1}}{f_j} .
$$

Step 3. That proportion of the class width is the distance travelled from the lower boundary:

$$
M = \ell_j + \frac{qn - F_{j-1}}{f_j} \, h_j .
$$

The formula is the algebraic content of the graphical construction, and it is exact whenever the observations are uniformly spread inside the class. The error bound is equally clean.

**Error bound.** From Theorem 2.4, $|G(x) - F(x)| \le f_j$ throughout class $j$. Let $M_G$ be the solution of $G(M_G) = qn$ and $M_F$ the solution of $F(M_F) = qn$. Then $F(M_F) = G(M_G)$, so $|F(M_F) - F(M_G)| \le f_j$. Since $F$ rises by exactly $f_j$ across a distance $h_j$, and its total rise across the class is $f_j$, the horizontal distance corresponding to a vertical difference of at most $f_j$ is at most $h_j$. Hence

$$
\left| M_G - M_F \right| \le h_j .
$$

In words: the interpolated quantile is within one class width of the true quantile, so the accuracy of the estimate is bought by narrowing the classes.

### 3.3 Proof of the frequency-density rule

**Sufficiency.** Suppose $H_j = c f_j / h_j$ for a single constant $c$. The area over class $j$ is $H_j h_j = c f_j$. For a union $U$ of classes with index set $J$, the total area is

$$
\sum_{j \in J} H_j h_j = c \sum_{j \in J} f_j = c \times (\text{number of observations in } U).
$$

**Necessity.** Suppose the area over every union of whole classes is proportional to the count, with constant $c$. Applying this to the single class $j$ gives $H_j h_j = c f_j$, hence $H_j = c f_j / h_j$. Two different constants for two different classes would contradict the requirement of a single proportionality across the whole picture.

**Sub-intervals.** For $a < b$ inside class $j$, the area is $H_j (b-a)$ and, under the uniform assumption, the count is $f_j (b-a)/h_j$. Equality of proportions again gives $H_j = c f_j/h_j$, so the same rule is forced by the finer requirement.

The choice $c = 1$ is a normalisation that makes the numerical area equal the numerical count. Any other choice, such as $c = 100/n$ to make the total area one hundred, is equally valid and is used when percentages are wanted.

### 3.4 Proof of the grouped-mean error bound

Write the observations in class $j$ as $x_{j1}, \dots, x_{j f_j}$ and let

$$
\mu_j = \frac{1}{f_j} \sum_{i=1}^{f_j} x_{ji}
$$

be their mean. Then

$$
\bar{x} = \frac{1}{n} \sum_{j=1}^{k} \sum_{i=1}^{f_j} x_{ji} = \frac{1}{n} \sum_{j=1}^{k} f_j \mu_j .
$$

Subtracting the grouped mean,

$$
\bar{x} - \bar{x}_g = \frac{1}{n} \sum_{j=1}^{k} f_j \left( \mu_j - m_j \right) .
$$

Every observation in class $j$ satisfies $\ell_j \le x_{ji} \le u_j$, so their mean satisfies $\ell_j \le \mu_j \le u_j$. The class mark $m_j$ is the midpoint of that interval, so $\left| \mu_j - m_j \right| \le h_j/2$. Therefore

$$
\left| \bar{x} - \bar{x}_g \right| \le \frac{1}{n} \sum_{j=1}^{k} f_j \frac{h_j}{2} .
$$

When all widths equal $h$, the right-hand side is $\frac{h}{2n} \sum_j f_j = h/2$, which is the stated special case. The bound is sharp: it is attained when every observation sits at one of the two class boundaries, alternately at the lower and the upper.

### 3.5 Derivation of the pie-chart angle formula

Requiring proportionality gives $\theta_j = c f_j$ for a single constant $c$. Requiring the sectors to exhaust the circle gives $\sum_j \theta_j = 360^{\circ}$. Substituting,

$$
c \sum_{j=1}^{k} f_j = 360^{\circ}, \qquad c n = 360^{\circ}, \qquad c = \frac{360^{\circ}}{n} .
$$

Hence $\theta_j = 360^{\circ} f_j/n$. Uniqueness follows because the two requirements determine $c$ uniquely.

### 3.6 Derivation of the three-dimensional pie distortion

A pie chart drawn on a tilted disc is an affine image of the circle: if the disc is compressed by a factor $k$ in the vertical direction, the point at angle $\theta$ moves to $\left(\cos\theta, k\sin\theta\right)$. Compression in one direction does not preserve angles.

Let $0 < k < 1$. The apparent angle of a sector that spans true angles from $\alpha$ to $\beta$ is the angle between the image radii, namely

$$
\arccos\!\left( \frac{\cos\alpha \cos\beta + k^{2} \sin\alpha \sin\beta}{\sqrt{\cos^{2}\alpha + k^{2}\sin^{2}\alpha}\,\sqrt{\cos^{2}\beta + k^{2}\sin^{2}\beta}} \right).
$$

For a quarter circle centred on the vertical axis, the sector runs from $45^{\circ}$ to $135^{\circ}$, and with $k = 1/2$ the image radii are $\left(0.7071, 0.3536\right)$ and $\left(-0.7071, 0.3536\right)$. Their directions are $26.57^{\circ}$ and $153.43^{\circ}$ above the horizontal, so the apparent angle is

$$
153.43^{\circ} - 26.57^{\circ} = 126.87^{\circ} .
$$

For a quarter circle centred on the horizontal axis at the near side, the sector runs from $-45^{\circ}$ to $45^{\circ}$, and the image radii have directions $-26.57^{\circ}$ and $26.57^{\circ}$, giving an apparent angle of $53.13^{\circ}$.

Two sectors of exactly ninety degrees therefore appear as $126.87^{\circ}$ and $53.13^{\circ}$, a ratio of about $2.4$ to $1$. The tilted quarter at the far edge overstates its share by $41$ per cent and the near quarter understates it by the same $41$ per cent. The sums are consistent, $126.87 + 53.13 = 180$, because the near half of the disc is displayed as the visible half of the ellipse; the distortion is a redistribution of apparent size, not an addition to it.

### 3.7 Method: constructing a grouped frequency distribution from raw data

The construction is a sequence of decisions, each with an explicit check.

1. Compute the range $R = x_{\max} - x_{\min}$.
2. Choose the number of classes $k$. Sturges' rule gives $k = \left\lceil 1 + 3.322 \log_{10} n \right\rceil$; in practice any $k$ between five and twelve is acceptable, and $k$ should be chosen so that the pattern is visible without the table becoming unreadable.
3. Compute the minimum admissible width $R/k$ and round it up to a convenient round number $h$.
4. Fix $\ell_1$ at or just below $x_{\min}$, then generate $\ell_2 = \ell_1 + h$, and so on, until the last boundary exceeds $x_{\max}$. The number of classes actually obtained may exceed $k$, which is why the width is rounded up rather than down.
5. Convert boundaries to written limits using the boundary convention, subtracting $\delta$ from each lower boundary and adding $\delta$ to each upper boundary.
6. Tally each observation into exactly one half-open class $[\ell_j, \ell_{j+1})$.
7. Record frequencies, then verify $\sum_j f_j = n$.
8. Add class marks $m_j = (\ell_j + \ell_{j+1})/2$, relative frequencies $f_j/n$ and cumulative frequencies $F_j$.
9. Verify the last cumulative frequency equals $n$ and the relative frequencies total $1$.

Sturges' rule is a heuristic derived from the assumption that the data are approximately normal; it is not a theorem, and the analyst is free to override it when the data have heavy tails or several modes, both of which require more classes to display honestly.

### 3.8 Method: drawing a histogram when the widths differ

1. List the boundaries and compute each width $h_j = \ell_{j+1} - \ell_j$.
2. Compute each density $d_j = f_j/h_j$.
3. Scale the vertical axis in units of density, not of frequency.
4. Draw each rectangle from $\ell_j$ to $\ell_{j+1}$ with height $d_j$.
5. Verify that $d_j h_j = f_j$ for every class and that the areas sum to $n$.
6. Label the vertical axis "frequency density" and state the unit, for example observations per thousand shillings.

The last step is not decoration. A vertical axis labelled "frequency" on a density histogram is a factual error, and an examiner will mark it as one.

### 3.9 Method: reading quantiles from an ogive

1. Compute the target count $qn$, with $q = 1/4, 1/2, 3/4$ as required.
2. Mark $qn$ on the vertical axis.
3. Draw a horizontal line to the ogive.
4. Drop a vertical line to the horizontal axis and read the value.
5. Cross-check the answer against the interpolation formula of Section 3.2; the two methods must agree.
6. State the answer in the units of the variable, and state the assumption that within the class concerned the observations are evenly spread.

Step 6 is where marks are lost. An interpolated quantile is an estimate made under a modelling assumption, and presenting it as an exact value is an error of interpretation rather than of arithmetic.

### 3.10 Method: the five-number summary and the fences

1. Sort the data.
2. Locate the median: with $n$ odd it is the middle value, with $n$ even the average of the two middle values.
3. Split the sorted data into a lower half and an upper half, excluding the median itself when $n$ is odd.
4. Take $Q_1$ as the median of the lower half and $Q_3$ as the median of the upper half.
5. Compute $\mathrm{IQR} = Q_3 - Q_1$ and the fences $Q_1 - 1.5\,\mathrm{IQR}$ and $Q_3 + 1.5\,\mathrm{IQR}$.
6. Draw the box, the median line and whiskers to the most extreme observations inside the fences; plot observations outside the fences individually.

Different software packages compute quartiles by slightly different conventions, so the exact values of $Q_1$ and $Q_3$ may differ in the second decimal. What must be consistent is the method used within one piece of work.

### 3.11 Method: constructing and reading a time series graph

1. Plot time on the horizontal axis with spacing proportional to the time interval.
2. Plot the measured quantity on the vertical axis, starting at zero if magnitude is being conveyed.
3. Join consecutive points, or mark them and join, depending on whether the intermediate values are meaningful.
4. Identify the trend by smoothing. A moving average of order $r$ replaces each value by the mean of $r$ consecutive values; for odd $r$ the average is centred on the middle term, and for even $r$ a second averaging pass is needed to centre it.
5. Identify seasonal effects by comparing each value with the corresponding smoothed value.
6. Describe the residual irregular movement separately.

For a series $y_1, \dots, y_T$ and odd $r = 2s+1$, the centred moving average at time $t$ is

$$
\bar{y}_t = \frac{1}{r} \sum_{i=-s}^{s} y_{t+i},
$$

defined for $t = s+1, \dots, T-s$. For even $r = 2s$ the two adjacent $r$-term averages are themselves averaged, which produces

$$
\bar{y}_t = \frac{1}{2}\left( \frac{y_{t-s} + \cdots + y_{t+s-1}}{r} + \frac{y_{t-s+1} + \cdots + y_{t+s}}{r} \right).
$$

## 4. Representative Worked Examples and Solutions

### 4.1 Problem: a discrete distribution with relative and cumulative columns

Thirty-five families were surveyed and the number of children per family recorded. The observations, in the order collected, are the following.

$$
\begin{aligned}
&1 \quad 0 \quad 2 \quad 3 \quad 4 \quad 5 \quad 6 \\
&7 \quad 2 \quad 3 \quad 4 \quad 0 \quad 2 \quad 5 \\
&8 \quad 4 \quad 5 \quad 12 \quad 6 \quad 3 \quad 2 \\
&7 \quad 6 \quad 5 \quad 3 \quad 3 \quad 7 \quad 8 \\
&9 \quad 7 \quad 9 \quad 4 \quad 5 \quad 4 \quad 3
\end{aligned}
$$

Construct the discrete frequency distribution, add relative and cumulative frequencies, and compute the mean from the table.

### 4.2 Solution: tally, normalise, accumulate

Step 1. Establish the support. The smallest value is $0$ and the largest is $12$, so the table must have thirteen rows.

Step 2. Tally each distinct value, grouping strokes in fives.

| Number of children | Frequency $f$ | Relative frequency | Cumulative frequency |
| --- | --- | --- | --- |
| 0 | 2 | 0.057 | 2 |
| 1 | 1 | 0.029 | 3 |
| 2 | 4 | 0.114 | 7 |
| 3 | 6 | 0.171 | 13 |
| 4 | 5 | 0.143 | 18 |
| 5 | 5 | 0.143 | 23 |
| 6 | 3 | 0.086 | 26 |
| 7 | 4 | 0.114 | 30 |
| 8 | 2 | 0.057 | 32 |
| 9 | 2 | 0.057 | 34 |
| 10 | 0 | 0.000 | 34 |
| 11 | 0 | 0.000 | 34 |
| 12 | 1 | 0.029 | 35 |
| **Total** | **35** | **1.000** | |

Step 3. Verify the totals.

$$
2 + 1 + 4 + 6 + 5 + 5 + 3 + 4 + 2 + 2 + 0 + 0 + 1 = 35
$$

The cumulative column ends at $35$, and the relative frequencies sum to $1.000$ apart from rounding in the third decimal place.

Step 4. Compute the total number of children from the table.

$$
\sum_j f_j x_j = 2(0) + 1(1) + 4(2) + 6(3) + 5(4) + 5(5) + 3(6) + 4(7) + 2(8) + 2(9) + 1(12)
$$

$$
= 0 + 1 + 8 + 18 + 20 + 25 + 18 + 28 + 16 + 18 + 12 = 164
$$

Step 5. Divide by the number of families.

$$
\bar{x} = \frac{164}{35} = 4.686
$$

Step 6. Locate the median from the cumulative column. Since $n = 35$, the median is the eighteenth ordered value. The cumulative frequency reaches $18$ at the value $4$, so the median is $4$.

Step 7. Interpret. The mean of $4.69$ sits above the median of $4$, and the single family with twelve children accounts for a visible part of that gap, which is the signature of a right-skewed distribution.

### 4.3 Problem: a grouped distribution from raw data, with an ogive

The marks of forty students, out of one hundred, are recorded below.

$$
\begin{aligned}
&68 \quad 74 \quad 51 \quad 83 \quad 92 \quad 47 \quad 65 \quad 78 \quad 61 \quad 55 \\
&88 \quad 72 \quad 63 \quad 49 \quad 77 \quad 85 \quad 58 \quad 66 \quad 71 \quad 94 \\
&52 \quad 69 \quad 81 \quad 57 \quad 74 \quad 62 \quad 43 \quad 79 \quad 68 \quad 86 \\
&59 \quad 73 \quad 64 \quad 90 \quad 53 \quad 67 \quad 76 \quad 82 \quad 48 \quad 70
\end{aligned}
$$

Construct a grouped distribution, estimate the median and quartiles from the ogive, and compare the grouped mean with the true mean.

### 4.4 Solution: Sturges, width eight, interpolation

Step 1. Compute the range.

$$
94 - 43 = 51
$$

Step 2. Apply Sturges' rule.

$$
k = \left\lceil 1 + 3.322 \log_{10}(40) \right\rceil = \left\lceil 1 + 3.322(1.602) \right\rceil = \left\lceil 6.32 \right\rceil = 7
$$

Step 3. Compute the minimum width and round it up.

$$
\frac{51}{7} = 7.29 \quad \longrightarrow \quad h = 8
$$

Step 4. Generate the boundaries from $\ell_1 = 40$.

$$
40,\ 48,\ 56,\ 64,\ 72,\ 80,\ 88,\ 96
$$

Step 5. Convert to written limits using a half-unit offset.

$$
40\text{–}47,\ 48\text{–}55,\ 56\text{–}63,\ 64\text{–}71,\ 72\text{–}79,\ 80\text{–}87,\ 88\text{–}95
$$

Step 6. Tally the observations into the half-open classes.

| Marks | Frequency $f$ | Relative frequency | Cumulative $F$ | Class mark $m$ |
| --- | --- | --- | --- | --- |
| 40 – 47 | 2 | 0.050 | 2 | 43.5 |
| 48 – 55 | 6 | 0.150 | 8 | 51.5 |
| 56 – 63 | 6 | 0.150 | 14 | 59.5 |
| 64 – 71 | 9 | 0.225 | 23 | 67.5 |
| 72 – 79 | 8 | 0.200 | 31 | 75.5 |
| 80 – 87 | 5 | 0.125 | 36 | 83.5 |
| 88 – 95 | 4 | 0.100 | 40 | 91.5 |
| **Total** | **40** | **1.000** | | |

Step 7. Verify the totals.

$$
2 + 6 + 6 + 9 + 8 + 5 + 4 = 40
$$

Step 8. Compute the grouped mean.

$$
\sum_j f_j m_j = 2(43.5) + 6(51.5) + 6(59.5) + 9(67.5) + 8(75.5) + 5(83.5) + 4(91.5)
$$

$$
= 87 + 309 + 357 + 607.5 + 604 + 417.5 + 366 = 2748
$$

$$
\bar{x}_g = \frac{2748}{40} = 68.7
$$

Step 9. Compare with the true mean. Summing the forty raw marks gives $2750$, so

$$
\bar{x} = \frac{2750}{40} = 68.75
$$

The grouping error is $0.05$, comfortably inside the bound of $h/2 = 4$ from Theorem 2.7.

Step 10. Estimate the median from the ogive. The target count is $n/2 = 20$, which lies in the class $64\text{–}71$, where $F$ rises from $14$ to $23$. Therefore

$$
M = 63.5 + \frac{20 - 14}{9}(8) = 63.5 + \frac{48}{9} = 63.5 + 5.33 = 68.83
$$

The true median of the raw data, the average of the twentieth and twenty-first ordered marks, is $(68 + 69)/2 = 68.5$, and the difference of $0.33$ lies well inside the guaranteed bound of one class width.

Step 11. Estimate the quartiles. For $Q_1$ the target is $10$, in the class $56\text{–}63$:

$$
Q_1 = 55.5 + \frac{10 - 8}{6}(8) = 55.5 + 2.67 = 58.17
$$

For $Q_3$ the target is $30$, in the class $72\text{–}79$:

$$
Q_3 = 71.5 + \frac{30 - 23}{8}(8) = 71.5 + 7 = 78.5
$$

Step 12. Interpret. The interquartile range from the ogive is $78.5 - 58.17 = 20.33$, and the median lies slightly above the centre of that interval, indicating mild negative skew in the middle half of the marks.

### 4.5 Problem: unequal class widths and frequency density

The annual incomes, in thousands of shillings, of $450$ traders are grouped with the boundaries $0$, $5$, $10$, $20$, $40$, $60$ and $100$, and the corresponding frequencies are $40$, $100$, $150$, $100$, $40$ and $20$. Compute the density of each class, verify the area check, and estimate the proportion of traders earning below $15$ thousand.

### 4.6 Solution: heights that make area equal count

Step 1. Compute the widths.

$$
5,\ 5,\ 10,\ 20,\ 20,\ 40
$$

Step 2. Compute the densities $d_j = f_j/h_j$.

$$
\frac{40}{5} = 8, \quad \frac{100}{5} = 20, \quad \frac{150}{10} = 15, \quad \frac{100}{20} = 5, \quad \frac{40}{20} = 2, \quad \frac{20}{40} = 0.5
$$

Step 3. Verify the areas.

$$
5(8) = 40, \quad 5(20) = 100, \quad 10(15) = 150, \quad 20(5) = 100, \quad 20(2) = 40, \quad 40(0.5) = 20
$$

Every area equals its frequency, and the areas total $450$, the number of traders.

Step 4. Identify the modal class by density. The tallest rectangle is the second, from $5$ to $10$ thousand, with density $20$, although the third class carries the larger frequency of $150$. The third class is twice as wide, so its larger count is spread over twice the distance.

Step 5. Compute the area below $15$ thousand. The interval from $0$ to $15$ consists of the first two classes in full plus half of the third:

$$
40 + 100 + 15(5) = 215
$$

Step 6. Convert the area to a proportion.

$$
\frac{215}{450} = 0.4778
$$

So approximately $47.8$ per cent of the traders earn below $15$ thousand.

Step 7. Estimate the mean from the class marks. The marks are $2.5$, $7.5$, $15$, $30$, $50$ and $80$, so

$$
\sum_j f_j m_j = 40(2.5) + 100(7.5) + 150(15) + 100(30) + 40(50) + 20(80) = 9700
$$

$$
\bar{x}_g = \frac{9700}{450} = 21.56
$$

Step 8. Estimate the median. The target is $225$, which lies in the third class, whose lower boundary is $10$:

$$
M = 10 + \frac{225 - 140}{150}(10) = 10 + 5.67 = 15.67
$$

Step 9. Interpret. The mean of $21.56$ exceeds the median of $15.67$ substantially, so the distribution is strongly right-skewed, with a long tail of high earners carried by the two widest classes.

### 4.7 Problem: pie chart and component bars for the same data

Two hundred students were classified by mode of travel. In 2023, eighty travelled by bus, fifty walked, thirty cycled, twenty-five came by car and fifteen by train. In 2024 the corresponding counts were seventy, fifty-five, forty, twenty-two and thirteen. Construct the pie chart angles for 2023, the percentage composition for both years, and state which display best supports each comparison.

### 4.8 Solution: angles, shares and display choice

Step 1. Verify both totals.

$$
80 + 50 + 30 + 25 + 15 = 200, \qquad 70 + 55 + 40 + 22 + 13 = 200
$$

Step 2. Compute the 2023 sector angles with $\theta = (f/n) 360^{\circ}$.

$$
\frac{80}{200}(360) = 144^{\circ}, \quad \frac{50}{200}(360) = 90^{\circ}, \quad \frac{30}{200}(360) = 54^{\circ}
$$

$$
\frac{25}{200}(360) = 45^{\circ}, \quad \frac{15}{200}(360) = 27^{\circ}
$$

Step 3. Check the angles.

$$
144 + 90 + 54 + 45 + 27 = 360
$$

Step 4. Convert both years to percentages.

| Mode | 2023 count | 2023 per cent | 2024 count | 2024 per cent |
| --- | --- | --- | --- | --- |
| Bus | 80 | 40.0 | 70 | 35.0 |
| Walk | 50 | 25.0 | 55 | 27.5 |
| Bicycle | 30 | 15.0 | 40 | 20.0 |
| Car | 25 | 12.5 | 22 | 11.0 |
| Train | 15 | 7.5 | 13 | 6.5 |
| **Total** | **200** | **100.0** | **200** | **100.0** |

Step 5. Check the percentage columns.

$$
40.0 + 25.0 + 15.0 + 12.5 + 7.5 = 100.0, \qquad 35.0 + 27.5 + 20.0 + 11.0 + 6.5 = 100.0
$$

Step 6. Choose the display for each question. To compare the two years category by category, a multiple bar chart with two bars per mode is correct, because the totals are equal and the absolute counts are comparable. To show the composition of each year in isolation, a pie chart is correct, because each year is a single whole. Because the two totals happen to be equal, the percentage component chart and the component chart give the same visual comparison here; had the totals differed, only the percentage component chart would have permitted a fair comparison of composition.

Step 7. Interpret. The share travelling by bicycle rose from $15$ per cent to $20$ per cent while the share travelling by bus fell from $40$ per cent to $35$ per cent, and because the total is unchanged in both years, these percentage changes are also changes in the numbers of students.

### 4.9 Problem: a time series and its moving average

Monthly sales, in thousands of units, for one year were $120$, $135$, $150$, $140$, $165$, $180$, $175$, $160$, $145$, $155$, $170$ and $190$ for January to December. Construct a three-point moving average, describe the trend, and explain why an even-order moving average needs centring.

### 4.10 Solution: smoothing and centring

Step 1. Verify the annual total and mean.

$$
120 + 135 + 150 + 140 + 165 + 180 + 175 + 160 + 145 + 155 + 170 + 190 = 1885
$$

$$
\bar{y} = \frac{1885}{12} = 157.08
$$

Step 2. Compute the three-point averages, each centred on the middle month.

$$
\bar{y}_2 = \frac{120 + 135 + 150}{3} = 135.00
$$

$$
\bar{y}_3 = \frac{135 + 150 + 140}{3} = 141.67
$$

$$
\bar{y}_4 = \frac{150 + 140 + 165}{3} = 151.67
$$

$$
\bar{y}_5 = \frac{140 + 165 + 180}{3} = 161.67
$$

$$
\bar{y}_6 = \frac{165 + 180 + 175}{3} = 173.33
$$

$$
\bar{y}_7 = \frac{180 + 175 + 160}{3} = 171.67
$$

$$
\bar{y}_8 = \frac{175 + 160 + 145}{3} = 160.00
$$

$$
\bar{y}_9 = \frac{160 + 145 + 155}{3} = 153.33
$$

$$
\bar{y}_{10} = \frac{145 + 155 + 170}{3} = 156.67
$$

$$
\bar{y}_{11} = \frac{155 + 170 + 190}{3} = 171.67
$$

Step 3. Describe the trend. The smoothed series rises from $135.00$ in February to a peak of $173.33$ in June, falls to a trough of $153.33$ in September and recovers to $171.67$ in November. The underlying movement is therefore a single mid-year peak with a modest upward drift.

Step 4. Explain the loss at the ends. The first and last months have no centred average, because a three-point window cannot be centred on an end point. A twelve-point average would lose six months at each end, which is why short windows are used when the series is short.

Step 5. Explain centring for an even order. With four quarters whose values are $20$, $24$, $28$, $32$ and $30$, the first four-point average is

$$
\frac{20 + 24 + 28 + 32}{4} = 26,
$$

which belongs between quarter two and quarter three. The next is

$$
\frac{24 + 28 + 32 + 30}{4} = 28.5,
$$

between quarter three and quarter four. Averaging the two gives the centred value at quarter three:

$$
\frac{26 + 28.5}{2} = 27.25 .
$$

Without that second averaging the smoothed value would sit between the original time points and could not be compared with any observed value.

Step 6. Interpret. The moving average removes the month-to-month irregularity and reveals the trend. It does not remove seasonality unless the window is one full seasonal cycle, which for monthly data means a window of twelve.

### 4.11 Problem: stem-and-leaf, five-number summary and fences

The following twenty marks were recorded: $34$, $37$, $41$, $42$, $45$, $45$, $48$, $52$, $53$, $55$, $56$, $58$, $61$, $63$, $67$, $71$, $74$, $78$, $82$, $89$. Construct the stem-and-leaf display, the five-number summary and the fences.

### 4.12 Solution: leaves, quartiles, fences

Step 1. Group by tens digit, leaves in increasing order within each row.

| Stem | Leaves |
| --- | --- |
| 3 | 4 7 |
| 4 | 1 2 5 5 8 |
| 5 | 2 3 5 6 8 |
| 6 | 1 3 7 |
| 7 | 1 4 8 |
| 8 | 2 9 |

Step 2. Verify the count.

$$
2 + 5 + 5 + 3 + 3 + 2 = 20
$$

Step 3. Find the median.

$$
Q_2 = \frac{55 + 56}{2} = 55.5
$$

Step 4. Find the quartiles from the two halves of ten observations each.

$$
Q_1 = \frac{45 + 45}{2} = 45, \qquad Q_3 = \frac{67 + 71}{2} = 69
$$

Step 5. Compute the interquartile range.

$$
\mathrm{IQR} = 69 - 45 = 24
$$

Step 6. Compute the fences.

$$
L_f = 45 - 1.5(24) = 9, \qquad U_f = 69 + 1.5(24) = 105
$$

Step 7. Classify the extremes. The minimum $34$ exceeds $9$ and the maximum $89$ is below $105$, so no observation is flagged and the whiskers reach $34$ and $89$.

Step 8. Determine the shape from the box. The lower part of the box runs from $45$ to $55.5$, a length of $10.5$, and the upper part from $55.5$ to $69$, a length of $13.5$. The upper part is longer, so the middle half of the data is positively skewed, and the longer upper whisker, from $69$ to $89$, confirms it.

Step 9. State the five-number summary.

$$
\text{minimum} = 34, \quad Q_1 = 45, \quad Q_2 = 55.5, \quad Q_3 = 69, \quad \text{maximum} = 89
$$

### 4.13 Problem: diagnosing a misleading display

A leaflet states that "sales have doubled" and illustrates the claim with two symbols of the same bag: the first drawn at a height of $2$ centimetres for sales of $100$ units, the second at a height of $4$ centimetres for sales of $200$ units. A second leaflet shows the same two years in a bar chart whose vertical axis runs from $90$ to $210$. Identify the distortions and the correct construction in each case.

### 4.14 Solution: compare area with data, and baseline with data

Step 1. Analyse the pictogram. The two symbols are drawn to the same shape, so doubling the height doubles the width as well. The areas therefore stand in the ratio

$$
\frac{4 \times 4}{2 \times 2} = \frac{16}{4} = 4 .
$$

Step 2. Compare with the data. The data ratio is

$$
\frac{200}{100} = 2 .
$$

Step 3. Quantify the exaggeration. The eye reads a fourfold increase where the data show a twofold increase, so the visual ratio is twice the true ratio.

Step 4. State the correction. Either repeat the identical symbol once per unit of quantity, so that the count of symbols carries the ratio, or scale the symbol's area rather than its linear size, which requires a linear scale factor of $\sqrt{2} = 1.414$ for a doubling of quantity.

Step 5. Analyse the bar chart. With the axis running from $90$ to $210$, the drawn heights for $100$ and $200$ units are $100 - 90 = 10$ and $200 - 90 = 110$, a ratio of $11$ to $1$.

Step 6. Compare with the data. The true ratio is $2$ to $1$, so the truncated axis has inflated the apparent ratio by a factor of $5.5$.

Step 7. State the correction. A bar chart encodes magnitude by length and must therefore start at zero. If the difference between the bars is the point, the honest display is a bar chart of the differences, or a line graph of the two values with a stated truncated axis, not a bar chart of the raw values.

## 5. Mathematical Extensions, Limits, and Common Errors

The most important structural fact in this topic is that every display is a functional of the same empirical distribution, and the differences between displays are differences of rendering rather than of content. The frequency table evaluates the counting measure on intervals; the histogram renders that measure as area through the density transform; the polygon renders it as a profile through the class marks; the ogive renders its running sum as a staircase and then linearises the staircase; the box plot renders five order statistics. Because all of these are views of one object, a reader who understands the correspondences can move between them, and can spot a display that has been built inconsistently — a histogram whose rectangle areas do not sum to $n$, an ogive that is not monotone, a pie chart whose angles do not total $360^{\circ}$, a percentage component bar whose segments do not total one hundred.

Beyond the elementary correspondence lie several extensions. Relative frequency converts a frequency table into a discrete probability distribution on the classes, and the cumulative relative frequency converts it into a distribution function, so the ogive is the empirical distribution function of the grouped data. As the class widths shrink and $n$ grows, a density histogram converges to the probability density of the underlying variable, which is the sense in which the histogram is an estimator and not merely a picture; the convergence is in mean square under mild conditions on the density. The box plot is a robust summary because quartiles are order statistics, and order statistics have bounded influence functions, so a single wild observation moves the box very little while it can move the mean arbitrarily far. That robustness is why the box plot is preferred to a mean-and-standard-deviation plot when outliers are suspected, and why the two summaries can appear to disagree about the same data.

The limits of representation must also be stated. A grouped table cannot answer a question about an individual value, and no arithmetic recovers what grouping has discarded. A graphical quantile is an estimate made under a uniformity assumption and inherits an error of at most one class width. A mean computed from class marks can differ from the true mean by up to half a class width, and the direction of that error is not knowable from the table alone. A box plot conceals multimodality entirely: two data sets with identical five-number summaries can have completely different shapes, and only a histogram or a stem-and-leaf display reveals the difference. A pie chart cannot support fine comparisons, because human beings judge angles poorly once sectors fall below about ten per cent of the circle.

The errors that damage marks and, in published work, damage understanding, are the following.

- *Treating the class interval's dash as a subtraction.* The label $50\text{–}52$ denotes a range, and the width is $3$, not $2$.
- *Computing the width from the limits when the measurement precision is not one unit.* The width is $b - a + 2\delta$, where $\delta$ is half the last recorded decimal place. With masses recorded to the nearest kilogram, $\delta = 0.5$; with masses recorded to the nearest tenth, $\delta = 0.05$.
- *Omitting the outer boundaries.* The first class needs a lower boundary and the last class an upper boundary, formed with the same half-gap as the interior joins. Without them the first and last rectangles of a histogram have bases of the wrong length.
- *Using frequency as the height when widths differ.* The heights must be frequency densities, and the only reliable check is that each rectangle's area reproduces its frequency.
- *Using an ordinary histogram when the widths differ and then reading the tallest bar as the modal class.* The modal class of a density histogram is the class of greatest density, which need not be the class of greatest frequency.
- *Plotting an ogive against class marks instead of upper boundaries.* The cumulative frequency is defined by the upper boundary, and plotting it elsewhere shifts the whole curve by half a class and corrupts every interpolated quantile.
- *Reading a raw count from a cumulative graph.* The cumulative value at a boundary is a running total, not a class frequency; the class frequency is the vertical jump between two consecutive plotted points.
- *Forgetting that a percentage component chart discards group totals.* Two groups of very different size can have identical percentage bars, and a reader who takes the bars at face value will conclude that the groups are similar.
- *Drawing a pie chart of more than about six categories.* Small sectors cannot be distinguished, and a legend with many entries forces the reader to match colours instead of comparing lengths.
- *Truncating the vertical axis of a bar chart.* Because bars are read by length, a truncated baseline multiplies every apparent difference by an arbitrary factor. In the worked example the factor was $5.5$.
- *Scaling a pictogram by linear size while claiming proportionality of quantity.* If a symbol is doubled in height while retaining its shape, its area quadruples and the reader perceives a fourfold change where the data show a doubling.
- *Tilting a pie chart into three dimensions.* An affine compression by a factor $k$ in one direction does not preserve angles: with $k = 1/2$ a quarter circle facing the viewer appears as $53.13^{\circ}$ and a quarter circle at the far edge as $126.87^{\circ}$. Two equal shares then differ by a factor of about $2.4$ in apparent size, and the extruded rim of a solid pie adds further apparent area to the sectors nearest the reader.
- *Drawing a line graph across a gap in the data.* Joining points across a period with no observations asserts continuity that the data do not support; the gap should be left open.
- *Comparing series of different lengths on one horizontal axis without rescaling.* A twelve-month series and a six-month series plotted on the same axis invite a comparison of areas, which is meaningless.

Two further remarks close the account. First, the choice of class width is a modelling decision with visible consequences: too few classes hide bimodality, too many classes produce a spiky profile in which sampling noise masquerades as structure, and the only defence is to plot at two or three widths and check that the conclusions survive. Second, no display can repair a defective sample. A beautifully constructed histogram of a badly selected group of people is a precise picture of the wrong thing, and the distinction between a faithful representation and a valid inference is the distinction this whole topic must respect. Representation makes the data visible; it does not make them true.
