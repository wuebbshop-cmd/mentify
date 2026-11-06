## 1. Foundational Concepts, Definitions, and Axioms

### 1.1 What an examination in this topic actually asks

Data representation is examined as a craft rather than as a body of doctrine. The examiner supplies something unfinished — a raw list of observations, a table with a blank cell, a description of a diagram, or a graph that has been drawn badly on purpose — and asks for the finished object or for a judgement about it. Three question families recur with almost mechanical regularity. The first is construction: tally a raw list into classes, or complete a table whose frequencies, boundaries, marks or cumulative entries are partly missing. The second is translation: convert a frequency table into a histogram, a frequency polygon, an ogive, a bar chart or a pie chart, and read values back off the result. The third is judgement: choose the display appropriate to a stated measurement scale, or diagnose what is dishonest about a display that has already been produced.

Almost every mark in the first family is won or lost at the counting stage, and almost every mark in the third family is won by naming precisely the mismatch between the visual encoding used and the measurement structure of the data. Computation is light throughout the topic. What is being tested is whether the candidate can keep a table internally consistent, convert counts into lengths, areas and angles without distorting them, and recognise the standard distortions that advertisers, journalists and careless draughtsmen introduce.

### 1.2 Variables, data types and the four measurement scales

A variable is a characteristic measured on the units of a population or sample. A qualitative variable records a category, such as mode of transport or blood group. A quantitative variable records a number, and is discrete when its possible values are separated by gaps that no observation can occupy, as with the number of children in a family, and continuous when between any two possible values a third is possible, as with mass, height, time and temperature. The distinction matters because it decides whether the horizontal axis of a diagram carries an ordered scale or merely a list of labels.

The scale on which a variable is measured decides which arithmetic is meaningful, and therefore which displays and which averages are honest.

| Scale | What the numbers support | Honest displays | Averages available |
|---|---|---|---|
| Nominal | distinguishing labels only; no order | simple bar chart, component bar chart, pie chart | mode only |
| Ordinal | order without measurable distance | bar chart in rank order, percentage component bar | mode, median, quartiles |
| Interval | equal differences, arbitrary zero | histogram, polygon, ogive, line graph, box plot | mean, median, mode |
| Ratio | equal differences and a true zero | all of the interval displays, plus ratio statements | all averages, including geometric and harmonic means |

The rows are not decoration. A line graph drawn between nominal categories asserts that intermediate positions on the axis are meaningful, and they are not, because there is nothing between "walking" and "bicycle". A pie chart of temperatures in degrees Celsius asserts that the ratios of sector sizes are meaningful, which fails because the zero of that scale is arbitrary, so a sector twice as large does not represent twice the heat. A histogram of an ordinal variable asserts that the categories are contiguous stretches of one scale, which may happen to be true for examination grades but is never guaranteed. When a question asks "which display is appropriate", the marks are awarded for naming the scale, naming the encoding the display imposes, and stating whether the data support it.

### 1.3 The frequency distribution table

A frequency distribution is a table that lists each distinct value, or each class of values, together with the number of observations falling in it. That number is the frequency, written $f$. The sum of the frequencies is the number of observations.

$$
\sum_{j=1}^{k} f_j = n
$$

Three derived columns are used throughout the topic. The relative frequency of a value or class is $f_j/n$, the proportion of the data it contains. The percentage frequency is $100 f_j/n$. The cumulative frequency up to and including a class is the total frequency of all classes whose upper boundary does not exceed the upper boundary of that class.

A discrete frequency distribution lists each distinct observed value separately. The numbers of children recorded for $35$ families give the values $0$ to $9$ and $12$ with frequencies $2$, $1$, $4$, $6$, $5$, $5$, $3$, $4$, $2$, $2$ and $1$. Adding the frequencies gives $35$, so the table is a complete account of the data, and the two extreme values $10$ and $11$ are simply absent rather than zero. The relative frequencies start $2/35 \approx 0.057$ and $1/35 \approx 0.029$.

A grouped frequency distribution collects the observations into classes. It is the only practical form when the variable is continuous or when there are many distinct values, because a table with two hundred rows communicates nothing. The price of that compression is loss of detail: once the observations have been put into classes, the individual values are no longer recoverable, and every later calculation from the table is an estimate rather than an exact result. That single sentence explains why grouped means, medians and modes are reported as estimates and why questions about grouped data accept answers that differ slightly from an answer computed from the raw list.

Two further forms of the table are examined. The less-than cumulative distribution replaces each class by its upper boundary and its cumulative frequency, producing a table of the form "less than $52.5$: $5$ observations". The more-than cumulative distribution replaces each class by its lower boundary and the number of observations at or above it, producing "more than $49.5$: $100$ observations". The two forms are mirror images, and the more-than frequency of a boundary is $n$ minus the less-than frequency of the same boundary.

### 1.4 The apparatus of classes: limits, boundaries, width and marks

Five words describe a class, and an examination answer must use them exactly.

The class interval is the label of a class, written as two numbers separated by a dash. The two numbers are the class limits: the lower class limit on the left and the upper class limit on the right. The class boundaries, also called the true class limits, are the points at which one class gives way to the next. Where the classes have been written with a gap, the boundary between a class ending at upper limit $b$ and the next class beginning at lower limit $a'$ is the midpoint of the gap.

$$
b_{\text{join}} = \frac{b + a'}{2}
$$

The same half-gap is applied at the two ends of the table, so the first class acquires a lower boundary and the last class an upper boundary. The class width, or class size, is the distance between the boundaries of a class, $h_j = u_j - \ell_j$. The class mark, or mid-value, is the midpoint of the boundaries, $m_j = (\ell_j + u_j)/2$.

For the masses of $100$ female students the classes $50\text{–}52$, $53\text{–}55$, $56\text{–}58$, $59\text{–}61$, $62\text{–}64$, $65\text{–}67$ and $68\text{–}70$ have frequencies $5$, $12$, $20$, $28$, $18$, $11$ and $6$.

| Class | Boundaries | Width | Mark | Frequency |
|---|---|---|---|---|
| $50\text{–}52$ | $49.5$ to $52.5$ | $3$ | $51$ | $5$ |
| $53\text{–}55$ | $52.5$ to $55.5$ | $3$ | $54$ | $12$ |
| $56\text{–}58$ | $55.5$ to $58.5$ | $3$ | $57$ | $20$ |
| $59\text{–}61$ | $58.5$ to $61.5$ | $3$ | $60$ | $28$ |
| $62\text{–}64$ | $61.5$ to $64.5$ | $3$ | $63$ | $18$ |
| $65\text{–}67$ | $64.5$ to $67.5$ | $3$ | $66$ | $11$ |
| $68\text{–}70$ | $67.5$ to $70.5$ | $3$ | $69$ | $6$ |

The half-gap is $0.5$ kilogram because the masses were recorded to the nearest kilogram; a class written $50\text{–}52$ therefore covers everything from $49.5$ up to but not including $52.5$. Had the masses been recorded to the nearest tenth of a kilogram, the same class label would have described the interval from $49.95$ to $52.45$, and the half-gap would have been $0.05$. The written limits must always be read against the stated precision of measurement, and the single commonest source of lost marks in this section is an assumed half-gap that contradicts the precision of the data.

### 1.5 The axioms a grouped table must satisfy

A grouped table is a partition of the observations, and a partition has three requirements. It is exhaustive: every observation belongs to some class. It is mutually exclusive: no observation belongs to two classes. Its classes are contiguous in the sense that the upper boundary of one equals the lower boundary of the next, so the horizontal axis of a histogram is unbroken. A table that violates any of the three is not merely untidy; every frequency in it becomes ambiguous.

Two conventions make the partition precise. The boundary convention states that an observation exactly equal to a boundary belongs to the class whose lower boundary it is, so that each class is the half-open interval $[\ell_j, u_j)$ and the classes cannot overlap. The rounding convention ties the written limits to the precision of measurement, as described above. A table without a stated convention is ambiguous, and an examination answer that states the convention earns a mark that is otherwise unavailable.

Equal widths are a convenience rather than a requirement. When widths differ, the histogram must encode frequency by area and not by height, and that rule is the single most examined piece of theory in the topic.

### 1.6 The display catalogue

A histogram represents a grouped distribution by rectangles whose bases are the class boundaries and whose heights are the class frequencies. Adjacent rectangles share an edge because the classes are contiguous, and the heights are meaningful only when all widths are equal, since only then is area proportional to frequency with a common constant of proportionality.

A density histogram replaces the height by the frequency density $f_j/h_j$. The area of the rectangle over class $j$ is then exactly $f_j$, and the area over any sub-interval equals the number of observations in that sub-interval. The density histogram is the correct display whenever the class widths differ, and it reduces to the ordinary histogram when they do not.

A frequency polygon plots the point $(m_j, f_j)$ for each class and joins consecutive points with straight segments, closing the figure to the horizontal axis at one empty class width beyond each end. It is the locus of the midpoints of the tops of the histogram rectangles, and its advantage over the histogram is that two distributions can be superimposed on the same axes.

An ogive, or cumulative frequency curve, plots $(u_j, F_j)$ for each class, where $u_j$ is the upper boundary and $F_j$ the cumulative frequency, and joins consecutive points with straight segments. Its final ordinate is $n$ and its final abscissa is the upper boundary of the last class. Reading across from $n/2$ to the curve and down to the axis estimates the median; the same construction with $n/4$ and $3n/4$ estimates the quartiles.

A bar chart represents each category by a rectangle of constant width, separated from its neighbours by gaps, whose height is proportional to the category frequency. The gaps encode the fact that the categories are distinct rather than contiguous, and the heights encode magnitude along a common baseline. Four forms are examined.

| Form | Construction | Appropriate when |
|---|---|---|
| Simple | one bar per category, height proportional to frequency | comparing category sizes at one time |
| Component | one bar per group, subdivided in proportion to its parts | showing a total and its breakdown together |
| Percentage component | as component, but each bar rescaled to a total of $100$ | comparing composition across groups of different size |
| Multiple | two or more bars side by side within each category | comparing the same categories across two or three groups |

A pie chart divides a circle into sectors whose angles are proportional to the category frequencies. A line graph plots a quantity against an ordered axis, usually time, and joins consecutive points; when the horizontal axis is time the data form a time series, and the graph displays sequence, direction and speed of change. A stem-and-leaf display writes each observation as a stem formed from its leading digits and a leaf formed from one trailing digit, grouping all leaves sharing a stem on one row. A box plot represents the five-number summary — minimum, lower quartile, median, upper quartile, maximum — by a box from $Q_1$ to $Q_3$ with a line at the median and whiskers reaching the extreme values that survive the outlier rule.

### 1.7 Choosing the display from the measurement scale and from the question

The choice is decided by two questions asked in order. First, what is the measurement scale? Nominal data admit bar charts, component bars and pie charts, and refuse histograms, line graphs and box plots. Ordinal data admit the same three plus a bar chart ordered by rank. Interval and ratio data admit histograms, polygons, ogives, line graphs and box plots, and refuse a pie chart whenever the ratios of the values matter, because a zero that is arbitrary makes ratios meaningless.

Second, what comparison must the reader make? To compare magnitudes across categories, use a bar chart. To compare composition, use a component or percentage component bar chart. To show the shape of a distribution of continuous data, use a histogram, and add a polygon if two distributions must be compared. To read quantiles, use an ogive. To track a quantity over time, use a line graph. To show the ordered detail of a small batch of two-digit numbers, use a stem-and-leaf display, which keeps every observation visible. To compare several batches on location, spread and outliers simultaneously, use box plots side by side.

## 2. Theorems, Lemmas, and Analytical Properties

### 2.1 The formula bank

Every computation in the topic is one of the following, and each is stated with the condition under which it is valid.

| Quantity | Formula | Condition |
|---|---|---|
| Relative frequency | $f_j/n$ | always |
| Class boundary | $(b + a')/2$ | classes written with a gap |
| Class width | $u_j - \ell_j$ | always |
| Class mark | $(\ell_j + u_j)/2$ | always |
| Frequency density | $f_j/h_j$ | widths unequal |
| Pie sector angle | $(f_j/n) \cdot 360^{\circ}$ | parts of one whole |
| Ogive quantile | $L + \frac{(pn - F)}{f} h$ | grouped data |
| Outlier fences | $Q_1 - 1.5\,\text{IQR}$ and $Q_3 + 1.5\,\text{IQR}$ | box plot convention |

In the ogive entry, $p$ is the required proportion of the data, $L$ the lower boundary of the class containing the $pn$-th observation, $F$ the cumulative frequency below that class, $f$ its frequency and $h$ its width. The same expression with $p = 1/4$, $1/2$, $3/4$ returns the quartiles, and with $p = i/10$ returns the $i$-th decile.

### 2.2 Lemma: normalisation of frequencies and relative frequencies

Let classes $1, \dots, k$ partition $n$ observations with frequencies $f_j$. Then

$$
\sum_{j=1}^{k} f_j = n, \qquad \sum_{j=1}^{k} \frac{f_j}{n} = 1, \qquad 0 \le \frac{f_j}{n} \le 1 .
$$

The first statement is the definition of a partition applied to counts, the second follows by dividing the first by $n$, and the third holds because a frequency cannot be negative and cannot exceed the total. The lemma is the primary self-check on any constructed table: a frequency column that does not sum to the stated total is wrong, and every downstream part of the answer inherits the error.

### 2.3 Lemma: boundary, width and mark identities

For classes written with equal gaps $g$ between consecutive limits, the boundaries are obtained by shifting the limits by $g/2$, every width equals the limit difference plus $g$, and the class mark is the average of the two limits as well as the average of the two boundaries.

$$
h_j = u_j - \ell_j = (b + g/2) - (a - g/2) = (b - a) + g, \qquad m_j = \frac{a + b}{2} = \frac{\ell_j + u_j}{2}
$$

Three consequences are worth memorising. The marks of equal-width classes form an arithmetic progression with common difference $h$, which is exactly what licenses the coding method for the mean. The width is a property of the boundaries and not of the limits, so a table whose classes have equal limit differences but unequal gaps does not have equal widths. The mark is unaffected by the gap, because the same half-gap is added at both ends of the class.

### 2.4 Theorem: the frequency-density rule

Let class $j$ have frequency $f_j$ and width $h_j$. If the rectangle over class $j$ is drawn with height $y_j = f_j/h_j$, then its area equals $f_j$. Conversely, if the heights are proportional to $f_j$ alone and the widths differ, the areas are not proportional to the frequencies.

The proof is immediate, since the area of a rectangle is base times height, and it is set out in Section 3 because the corollary matters more than the theorem.

### 2.5 Corollary: proportion equals area

Under the density rule, the area over any interval equals the number of observations falling in that interval, and the total area equals $n$. The proportion of observations in any interval is therefore the ratio of the area over that interval to the total area. This is the principle that allows an exam candidate to estimate a frequency or a proportion from a described histogram without any table, and it is also the principle that exposes a dishonest density histogram, whose areas do not stand in the ratio of the underlying counts.

### 2.6 Theorem: the cumulative frequency function is non-decreasing and ends at $n$

Let $F_j = f_1 + \cdots + f_j$. Then $0 \le F_1 \le F_2 \le \cdots \le F_k = n$, and $F$ is constant on each class and jumps by $f_j$ at each upper boundary. The cumulative frequency is therefore a step function of the variable, and the less-than table records its values at the jump points.

Two practical consequences follow. A cumulative column that decreases anywhere contains an arithmetic slip, and a final entry different from $n$ invalidates the table. Both checks take seconds and both are habitually omitted.

### 2.7 Theorem: the ogive reproduces the grouped quantile formula

Suppose the cumulative curve is drawn by joining the points $(u_j, F_j)$ with straight segments, and suppose the required position $pn$ falls in class $j$, so that $F_{j-1} < pn \le F_j$. Then the horizontal coordinate at which the curve reaches height $pn$ is exactly

$$
L + \frac{pn - F_{j-1}}{f_j} h_j ,
$$

which is the interpolation formula for the quantile of grouped data. The linear segment of the ogive and the uniform-within-class assumption of the formula are the same assumption written in two notations, so a graphical estimate and a computed estimate must agree, and any disagreement signals an arithmetic error rather than a defect of the method.

### 2.8 Theorem: pie-chart proportionality

If a circle is divided into sectors whose angles are $\theta_j = 360^{\circ} f_j/n$, then each sector angle is proportional to its frequency, the ratio of two angles equals the ratio of the two frequencies, and the angles sum to a full turn.

$$
\sum_{j=1}^{k} \theta_j = \frac{360^{\circ}}{n}\sum_{j=1}^{k} f_j = 360^{\circ}
$$

The proportionality is exact in angle. It is also exact in area, because the area of a sector is $\tfrac{1}{2} r^{2}\theta$ with the same radius for every sector, so areas are proportional to angles with a common factor. That factor is precisely what a three-dimensional drawing destroys, since the sectors of a disc drawn in perspective are not all drawn with the same radius.

### 2.9 Lemma: component and percentage component bars are consistent

In a component bar chart the segments of a bar are proportional to the parts and the bar height equals the group total. In a percentage component bar chart each segment is rescaled to $100 f_{ij}/T_i$, where $T_i$ is the total of group $i$, so every bar has height $100$ and the segments of one bar sum to $100$. Consequently percentage component bars compare composition only, and they deliberately destroy the information about group totals; a reader who compares bar heights in such a chart learns nothing, because all bars are equal by construction.

### 2.10 Lemma: a stem-and-leaf display is lossless

Every observation contributes exactly one leaf, and the stem of that leaf is fixed by the observation's magnitude, so the multiset of leaves together with their stems determines the multiset of observations uniquely. The display is therefore a complete record of the data, unlike a histogram, and the observations remain sorted, which allows the median and the quartiles to be read by counting leaves. The display is also a crude histogram turned on its side, with the leaf counts playing the role of frequencies.

### 2.11 Proposition: the fence rule for box plots

With $R = Q_3 - Q_1$, an observation is flagged as a suspected outlier when it lies below $Q_1 - 1.5R$ or above $Q_3 + 1.5R$. For a symmetric distribution with no outliers, roughly $99$ per cent of the observations lie inside those fences, which is why the rule is used as a screen rather than as a test. The rule is a convention, not a theorem, and a flagged observation is a candidate for inspection rather than a proven error.

### 2.12 Theorem: order statistics are invariant under increasing transformations

Let $g$ be strictly increasing and let $y_i = g(x_i)$. Then the sorted order of the $y$ values is the sorted order of the $x$ values, so the median of the $y$ values is $g$ applied to the median of the $x$ values, and the quartiles correspond in the same way. Distances, however, are not preserved: the interquartile range of the $y$ values is not $g$ applied to the interquartile range of the $x$ values unless $g$ is linear.

The theorem justifies drawing a stem-and-leaf display or a box plot after any change of units, because the picture is the same picture with relabelled axes. It also warns against comparing interquartile ranges across two variables measured on different scales, and against reading a box plot as though equal visual distances meant equal numerical differences when the axis has been transformed logarithmically.

### 2.13 Proposition: three distortions that can be quantified

A truncated vertical axis that begins at $c$ rather than zero draws a bar of value $v$ with length $v - c$, so the apparent ratio of two bars is $(v_1 - c)/(v_2 - c)$ rather than $v_1/v_2$. An area-scaled pictogram whose icon is enlarged in both dimensions by a factor $k$ multiplies the area by $k^{2}$, so a doubling of the underlying value drawn as a doubling of both dimensions overstates the comparison by a factor of two. A three-dimensional pie chart whose front sectors are drawn with radius multiplied by $k$ multiplies their areas by $k^{2}$ while leaving the remaining sectors unchanged, so the front sectors are systematically exaggerated. Each distortion has a number attached to it, and an examination answer that supplies the number earns more than one that merely says "misleading".

## 3. Formal Proofs, Derivations, and Methods

### 3.1 Proof of the density rule and its area corollary

Step 1. Fix class $j$ with boundaries $\ell_j$ and $u_j$, width $h_j = u_j - \ell_j$, and frequency $f_j$.

Step 2. Draw a rectangle on the base $[\ell_j, u_j]$ with height $y_j$. Its area is the product of base and height.

$$
A_j = h_j y_j
$$

Step 3. Choose the height $y_j = f_j/h_j$ and substitute.

$$
A_j = h_j \cdot \frac{f_j}{h_j} = f_j
$$

Step 4. Sum over the classes, using the normalisation of frequencies.

$$
\sum_{j=1}^{k} A_j = \sum_{j=1}^{k} f_j = n
$$

Step 5. For a sub-interval of width $w$ inside class $j$, the area is $w y_j = w f_j/h_j$. Under the assumption that the observations are spread evenly inside the class, the expected count in that sub-interval is $n_j w/h_j$, so the area equals the expected count. This is the exact sense in which area encodes frequency.

Step 6. Suppose instead that heights are proportional to $f_j$ alone, so that $y_j = cf_j$ for a common constant $c$. Then the area is $c f_j h_j$, which is not proportional to $f_j$ unless all $h_j$ are equal. The equal-height convention therefore fails precisely when the widths differ.

### 3.2 Proof that the cumulative frequency is a non-decreasing step function

Step 1. Define $F(t)$ as the number of observations less than $t$, so that $F(t) = \sum_{j:\, u_j \le t} f_j$.

Step 2. Let $s < t$. Every observation below $s$ is below $t$, so the count at $s$ cannot exceed the count at $t$.

$$
F(s) \le F(t)
$$

Step 3. Between two consecutive boundaries the set of classes satisfying $u_j \le t$ does not change, so $F$ is constant on every interval $[u_j, u_{j+1})$.

Step 4. At $t = u_j$ the class $j$ enters the sum, so $F$ jumps by $f_j$ and is right-continuous.

Step 5. At $t$ beyond the last boundary every class has entered the sum, so $F(t) = n$ there.

The function is therefore a non-decreasing right-continuous step function with total rise $n$, and the less-than table is nothing more than a list of its values at the jumps. An ogive replaces the step function by the polygon through the same jump points, which is why the ogive and the step function differ only in the interior of each class.

### 3.3 Derivation of the ogive interpolation identity

Step 1. Let the required position be $pn$, with $0 < p < 1$, and let class $j$ be the first class whose cumulative frequency reaches it, so that $F_{j-1} < pn \le F_j$.

Step 2. The ogive segment over class $j$ runs from $(L, F_{j-1})$ to $(U, F_j)$, where $L$ and $U$ are the boundaries and $U - L = h_j$.

Step 3. Write the equation of the straight segment in point-slope form.

$$
\frac{y - F_{j-1}}{x - L} = \frac{F_j - F_{j-1}}{U - L} = \frac{f_j}{h_j}
$$

Step 4. Set $y = pn$ and solve for $x$.

$$
x = L + \frac{pn - F_{j-1}}{f_j} h_j
$$

Step 5. Recognise the right-hand side as the interpolation formula for the quantile of grouped data. The geometry of the ogive therefore encodes exactly the uniform-within-class assumption, and a graphical reading and a computed value must coincide when both are correct.

### 3.4 Derivation of the pie-chart angle formula and of the three-dimensional distortion

Step 1. Require the sector angle to be proportional to the frequency, so that $\theta_j = cf_j$ for a constant $c$ independent of $j$.

Step 2. Require the sectors to fill the circle and use the normalisation of frequencies.

$$
360^{\circ} = \sum_{j=1}^{k} \theta_j = c\sum_{j=1}^{k} f_j = cn
$$

Step 3. Solve for the constant and substitute back.

$$
c = \frac{360^{\circ}}{n}, \qquad \theta_j = \frac{360^{\circ} f_j}{n}
$$

Step 4. For the distortion, note that the area of a sector of radius $r$ and angle $\theta$ is $A = \tfrac{1}{2} r^{2} \theta$. If every sector carries the same radius $r$, areas are proportional to angles and the display is faithful.

Step 5. Let the drawing multiply the radius of one sector by $k$ while leaving its angle unchanged. Its area becomes

$$
A' = \tfrac{1}{2} (kr)^{2} \theta = k^{2} \cdot \tfrac{1}{2} r^{2} \theta = k^{2} A ,
$$

so that sector is exaggerated by the factor $k^{2}$ while every other sector keeps its true area. With $k = 1.4$ the exaggeration is $1.96$, and a sector representing $10$ per cent of the data occupies almost $20$ per cent of the apparent area.

### 3.5 Derivation of the percentage component bar segments

Step 1. Let group $i$ have total $T_i = \sum_j f_{ij}$ and part $j$ of that group have count $f_{ij}$.

Step 2. In an ordinary component bar the segment height is proportional to $f_{ij}$, and the bar height is proportional to $T_i$. Two bars of different heights cannot be compared segment by segment without mental rescaling.

Step 3. Rescale each group by its own total, so the segment height is $100 f_{ij}/T_i$.

Step 4. Verify that each bar now totals $100$.

$$
\sum_{j} 100\frac{f_{ij}}{T_i} = \frac{100}{T_i}\sum_{j} f_{ij} = \frac{100 T_i}{T_i} = 100
$$

Step 5. Note what has been lost: the factor $T_i$ no longer appears, so all information about the size of each group has been removed by construction. The chart compares composition only.

### 3.6 Proof of order-statistic invariance under increasing transformations

Step 1. Let $g$ be strictly increasing and let $x_{(1)} \le x_{(2)} \le \cdots \le x_{(n)}$ be the ordered observations.

Step 2. If $x_{(i)} \le x_{(i+1)}$ then $g(x_{(i)}) \le g(x_{(i+1)})$ because $g$ is increasing, so the transformed values are already in the same order.

Step 3. The $i$-th smallest transformed value is therefore $g(x_{(i)})$, and any statistic defined as a single order statistic transforms by $g$.

Step 4. The median of an odd sample is the middle order statistic, so it transforms by $g$. For an even sample the median is the average of two order statistics, and an average is not preserved by a nonlinear $g$; the invariance therefore holds exactly only for the odd case, and only approximately in general.

Step 5. Differences of order statistics are not preserved, since $g(x_{(j)}) - g(x_{(i)})$ need not equal $g(x_{(j)} - x_{(i)})$. The interquartile range therefore changes under a nonlinear change of scale, which is why a box plot may be redrawn after a change of units only when the change is linear.

### 3.7 Method: constructing a grouped frequency distribution from raw data

Step 1. Find the smallest and largest observations and compute the range.

Step 2. Choose the number of classes, usually between five and fifteen, and divide the range by that number to obtain a provisional width.

Step 3. Round the width up to a convenient value, and choose the first lower limit at or just below the smallest observation so that no observation is stranded.

Step 4. Write the classes in ascending order with equal limit differences and a stated gap convention.

Step 5. Tally each observation into exactly one class, crossing off the raw list as it is counted.

Step 6. Add the frequencies and confirm that the total equals the number of observations.

Step 7. Compute the boundaries by adding and subtracting half the gap, verify that consecutive boundaries coincide, and insert the class marks.

Step 8. Add the relative frequency and cumulative frequency columns and confirm that the last cumulative entry equals $n$.

### 3.8 Method: the histogram when the widths differ

Step 1. Compute every class width from the boundaries and list the widths.

Step 2. Divide each frequency by its own width to obtain the frequency density.

Step 3. Draw rectangles on the boundary scale with those heights, so that adjacent rectangles touch.

Step 4. Verify by area: multiply each height by its width and confirm that the products reproduce the frequencies and sum to $n$.

Step 5. If a question asks for a frequency over part of a class, multiply the density by the width of that part.

### 3.9 Method: the frequency polygon and its closure

Step 1. Compute the class marks, which are the midpoints of the boundaries.

Step 2. Plot the point $(m_j, f_j)$ for each class, using density instead of frequency only if the widths differ and the polygon is meant to be read as a density curve.

Step 3. Join consecutive points with straight segments.

Step 4. Close the polygon by adding one fictitious class of zero frequency at each end, at the marks one width beyond the first and last classes.

Step 5. Check that the polygon encloses the same area as the histogram, since each triangular corner that the polygon adds is matched by a triangle that it removes.

### 3.10 Method: reading quantiles from an ogive

Step 1. Convert the table to a less-than cumulative table with upper boundaries and cumulative frequencies, beginning with the lower boundary of the first class and zero.

Step 2. Plot the cumulative frequency against the upper boundary, and join with straight segments.

Step 3. Compute the required position: $n/2$ for the median, $n/4$ and $3n/4$ for the quartiles, $in/10$ for the $i$-th decile.

Step 4. Draw a horizontal line from that position on the vertical axis to the curve, then a vertical line down to the axis, and read the value.

Step 5. Confirm that the reading lies within the class identified by the interpolation formula, and state both the graphical and the computed value when the question asks for a check.

### 3.11 Method: pie chart construction with the angle check

Step 1. Total the frequencies and confirm the total against the stated number of units.

Step 2. Compute each angle as $360^{\circ} f_j/n$, keeping exact fractions where possible so that the arithmetic is verifiable.

Step 3. Lay out the sectors in a stated order, usually from the largest to the smallest or in a natural sequence, and label each with its category and either its frequency or its percentage.

Step 4. Add the angles and confirm that they total $360^{\circ}$; a total of $359^{\circ}$ or $361^{\circ}$ is a rounding slip that must be reported as such rather than hidden.

Step 5. Never draw the chart in perspective, and never vary the radius; either change destroys the proportionality the chart is supposed to display.

### 3.12 Method: stem-and-leaf, five-number summary and fences

Step 1. Order the observations and choose the stem unit so that each stem carries a manageable number of leaves.

Step 2. Write the stems in ascending order and append each leaf to its stem, arranging leaves in ascending order within each row.

Step 3. Read the median by counting to the middle leaf, or between the two middle leaves.

Step 4. Read the quartiles by counting to the quarter positions, using the convention stated in the question.

Step 5. Compute the interquartile range, then the lower fence $Q_1 - 1.5R$ and the upper fence $Q_3 + 1.5R$.

Step 6. Draw the box from $Q_1$ to $Q_3$ with a line at the median, and the whiskers to the smallest and largest observations that remain inside the fences.

Step 7. Plot any observation outside the fences individually, and say that it is a suspected outlier rather than an error.

### 3.13 Method: the time-series line graph and a moving average

Step 1. Plot the quantity on the vertical axis against time on the horizontal axis, with the axes labelled and the units stated.

Step 2. Join consecutive points, keeping the horizontal spacing proportional to the time interval; unequal spacing of equally spaced periods is a distortion.

Step 3. Describe the trend, the turning points and the size of the year-to-year changes in words, since the marks are usually for the description rather than for the drawing.

Step 4. To smooth short-term fluctuation, compute a moving average of odd order by averaging each run of consecutive values and placing the result at the centre of the run.

Step 5. Note that a moving average of order $m$ loses $m - 1$ values, one at each end, which is why a short series cannot support a long moving average.

### 3.14 Method: diagnosing a misleading display

Step 1. Identify what is encoded: length, area, angle or position.

Step 2. Identify what the encoding should be: frequency, proportion, or rate.

Step 3. Check the baseline. A bar chart whose vertical axis does not begin at zero encodes length as $v - c$ rather than as $v$, and the ratio it displays is therefore $(v_1 - c)/(v_2 - c)$.

Step 4. Check the dimensionality. If both dimensions of a picture are scaled by the value, area scales as the square, so the visual impression is the square of the truthful ratio.

Step 5. Check the widths. A histogram with equal bar widths and unequal classes overstates every wide class.

Step 6. Check the perspective. A three-dimensional pie chart exaggerates the sectors drawn nearest the viewer, and any chart drawn across a sloping surface distorts area.

Step 7. State the correction numerically: give the true ratio, the apparent ratio and the factor by which the display exaggerates.

### 3.15 The question-pattern map

| Pattern | What is given | The opening move | Typical marks |
|---|---|---|---|
| Tally | a raw list and a class width | count the range and fix the classes | $5$ to $8$ |
| Completion | a table with blanks in the boundary or mark columns | derive the half-gap from the limits | $3$ to $5$ |
| Equal-width histogram | a table of equal classes | height equals frequency, bases touch | $3$ to $4$ |
| Unequal-width histogram | classes of two or three different widths | divide each frequency by its own width | $4$ to $6$ |
| Polygon | any frequency table | plot marks against frequencies and close to the axis | $3$ |
| Ogive | any frequency table | plot upper boundaries against cumulative frequencies | $4$ to $6$ |
| Pie chart | categorical frequencies | angle equals $360^{\circ}$ times the share | $3$ to $5$ |
| Bar chart family | categories, sometimes two groups | choose the form that matches the comparison asked for | $4$ |
| Stem-and-leaf and box plot | a short raw list | order the observations, then count | $5$ to $7$ |
| Diagnosis | a described or drawn display | name the encoding and quantify the distortion | $4$ to $6$ |

## 4. Representative Worked Examples and Solutions

### 4.1 Problem A: a raw list, a grouped table and three graphs

The marks of $40$ learners in a statistics test, out of $80$, are recorded below as a raw list.

| 22 | 41 | 55 | 35 | 71 | 48 | 26 | 59 |
|---|---|---|---|---|---|---|---|
| 33 | 45 | 61 | 52 | 28 | 44 | 74 | 58 |
| 37 | 50 | 46 | 65 | 31 | 49 | 53 | 68 |
| 39 | 42 | 56 | 77 | 36 | 47 | 51 | 63 |
| 45 | 54 | 38 | 58 | 69 | 43 | 49 | 66 |

(a) Construct a grouped frequency distribution with classes of width ten beginning at $20$.

(b) Add the boundaries, the marks and the cumulative frequency.

(c) State the heights of the histogram rectangles and the coordinates of the frequency polygon.

(d) Estimate the median and the quartiles, and state which class contains each.

### 4.2 Solution A: tally, translate, interpolate

Step 1. The smallest mark is $22$ and the largest is $77$, so the range is $55$ and six classes of width ten span it from $20$ to $79$.

Marking point M1: the range must be computed from the extreme observations, and the number of classes must be justified rather than guessed.

Step 2. Tally the observations into the six classes, crossing each mark off the list as it is counted.

| Class | Tally count | Frequency |
|---|---|---|
| $20\text{–}29$ | $22$, $26$, $28$ | $3$ |
| $30\text{–}39$ | $31$, $33$, $35$, $36$, $37$, $38$, $39$ | $7$ |
| $40\text{–}49$ | $41$ to $49$, eleven marks | $11$ |
| $50\text{–}59$ | $50$ to $59$, ten marks | $10$ |
| $60\text{–}69$ | $61$, $63$, $65$, $66$, $68$, $69$ | $6$ |
| $70\text{–}79$ | $71$, $74$, $77$ | $3$ |
| Total | | $40$ |

Marking point M2: the frequencies must sum to $40$; a total other than $40$ means a mark has been counted twice or missed.

Step 3. The gap between consecutive limits is one, so the half-gap is $0.5$ and the boundaries run from $19.5$ to $79.5$. Every width is $10$, and the marks are the midpoints.

| Class | Boundaries | Mark | Frequency | Cumulative |
|---|---|---|---|---|
| $20\text{–}29$ | $19.5$ to $29.5$ | $24.5$ | $3$ | $3$ |
| $30\text{–}39$ | $29.5$ to $39.5$ | $34.5$ | $7$ | $10$ |
| $40\text{–}49$ | $39.5$ to $49.5$ | $44.5$ | $11$ | $21$ |
| $50\text{–}59$ | $49.5$ to $59.5$ | $54.5$ | $10$ | $31$ |
| $60\text{–}69$ | $59.5$ to $69.5$ | $64.5$ | $6$ | $37$ |
| $70\text{–}79$ | $69.5$ to $79.5$ | $74.5$ | $3$ | $40$ |

Marking point M3: the first lower boundary is $19.5$ and not $20$, because the half-gap must be applied at the ends of the table as well as between the classes.

Step 4. Because the widths are equal, the histogram heights are the frequencies $3$, $7$, $11$, $10$, $6$ and $3$, drawn on bases of width $10$ that touch one another.

Marking point M4: the rectangles must touch, and the axis must be labelled with boundaries rather than with class labels.

Step 5. The polygon passes through the marks with those frequencies, and is closed to the axis one width beyond each end.

$$
(14.5,\, 0),\ (24.5,\, 3),\ (34.5,\, 7),\ (44.5,\, 11),\ (54.5,\, 10),\ (64.5,\, 6),\ (74.5,\, 3),\ (84.5,\, 0)
$$

Step 6. The median is in the class containing the twentieth observation, since $n/2 = 20$, and the cumulative frequency first reaches $20$ in the class $40\text{–}49$.

$$
\text{Median} = 39.5 + \frac{20 - 10}{11} \times 10 = 39.5 + 9.09 = 48.59
$$

Step 7. The lower quartile is in the class containing the tenth observation, which is again the boundary between the second and third classes, so the interpolation is exact.

$$
Q_1 = 29.5 + \frac{10 - 3}{7} \times 10 = 29.5 + 10 = 39.5
$$

Step 8. The upper quartile is in the class containing the thirtieth observation, which is the class $50\text{–}59$.

$$
Q_3 = 49.5 + \frac{30 - 21}{10} \times 10 = 49.5 + 9 = 58.5
$$

Marking point M5: each quantile needs its class identified with the position $0.25n$, $0.5n$ or $0.75n$ shown explicitly, because method marks are awarded for the positions even when the arithmetic slips.

Step 9. Check the answer. The three values satisfy $39.5 < 48.59 < 58.5$, the median lies inside its own class, and reading the same three positions off the ogive gives the same values. The marks are positively skew, since the mean mark computed from the class marks is $49.0$ and exceeds the median $48.59$, and both exceed the modal mark $47.5$.

### 4.3 Problem B: unequal class widths

A variable is grouped into the classes $0\text{–}10$, $10\text{–}20$, $20\text{–}40$, $40\text{–}60$ and $60\text{–}100$ with frequencies $8$, $12$, $20$, $16$ and $4$. Draw the histogram and estimate the proportion of observations above $50$.

### 4.4 Solution B: encode by area

Step 1. Record the widths, which are $10$, $10$, $20$, $20$ and $40$, and confirm that they differ so the equality of heights with frequencies is not available.

Step 2. Compute the frequency density of each class.

| Class | Frequency | Width | Density |
|---|---|---|---|
| $0\text{–}10$ | $8$ | $10$ | $0.8$ |
| $10\text{–}20$ | $12$ | $10$ | $1.2$ |
| $20\text{–}40$ | $20$ | $20$ | $1.0$ |
| $40\text{–}60$ | $16$ | $20$ | $0.8$ |
| $60\text{–}100$ | $4$ | $40$ | $0.1$ |

Marking point M6: every density must be the frequency divided by that class's own width, and a candidate who divides every frequency by the smallest width loses the whole of the drawing marks.

Step 3. Verify by area that the drawing represents the data.

$$
8 + 12 + 20 + 16 + 4 = 60
$$

Step 4. For the proportion above $50$, split the class $40\text{–}60$ at $50$. Its density is $0.8$, so the strip from $50$ to $60$ carries an area of $0.8 \times 10 = 8$.

Step 5. Add the observations above $50$ and divide by the total.

$$
\frac{8 + 4}{60} = \frac{12}{60} = 0.20
$$

Marking point M7: the area of a part of a class is density times the width of that part, not frequency times a guessed fraction.

Step 6. Interpret. The tallest rectangle is the one over $10\text{–}20$, of height $1.2$, even though the class $20\text{–}40$ contains more observations, because the second class is twice as wide. A drawing with heights equal to frequencies would have made the class $20\text{–}40$ look like the peak of the distribution and would have reversed the truth about the local concentration of the data.

### 4.5 Problem C: bar charts and a pie chart for one set of categories

The modes of transport used by $120$ students are walking $30$, bicycle $24$, matatu $45$, motorcycle $6$ and car $15$. Compute the pie chart angles and the percentage component bar heights, and state which display best answers the question "what share of students walk".

### 4.6 Solution C: angles, shares and the choice of display

Step 1. Confirm the total.

$$
30 + 24 + 45 + 6 + 15 = 120
$$

Step 2. Express each frequency as a fraction of the total and convert to an angle.

$$
\theta_{\text{walk}} = \frac{30}{120} \times 360^{\circ} = 90^{\circ}, \qquad \theta_{\text{bicycle}} = \frac{24}{120} \times 360^{\circ} = 72^{\circ}
$$

$$
\theta_{\text{matatu}} = \frac{45}{120} \times 360^{\circ} = 135^{\circ}, \qquad \theta_{\text{motorcycle}} = \frac{6}{120} \times 360^{\circ} = 18^{\circ}
$$

$$
\theta_{\text{car}} = \frac{15}{120} \times 360^{\circ} = 45^{\circ}
$$

Step 3. Check the total, since the sectors must exhaust the circle.

$$
90 + 72 + 135 + 18 + 45 = 360^{\circ}
$$

Marking point M8: the check that the angles total $360^{\circ}$ is worth an explicit line of working.

Step 4. Convert the same fractions to percentages for the component bar.

$$
25\%,\ 20\%,\ 37.5\%,\ 5\%,\ 12.5\%
$$

Step 5. Confirm that the percentages total $100$, which they do exactly, so no rounding adjustment is needed.

Step 6. Choose the display. For the single question "what share walks", the pie chart is the natural answer because a share of one whole is exactly what a sector encodes, and the sector is a quarter of the circle. The same data drawn as a simple bar chart would emphasise the ranking of the categories rather than their shares of the whole, and a component bar would be preferable only if a second campus were added, in which case two percentage component bars would allow the compositions to be compared without being confused by the different totals.

### 4.7 Problem D: a stem-and-leaf display, a five-number summary and an outlier

The marks of $21$ learners, out of $50$, are $21$, $30$, $42$, $4$, $33$, $25$, $36$, $46$, $28$, $31$, $40$, $24$, $34$, $48$, $26$, $32$, $38$, $27$, $44$, $29$ and $35$. Construct a stem-and-leaf display, find the five-number summary, and test for outliers.

### 4.8 Solution D: leaves, quartiles and fences

Step 1. Order the observations and split each into a tens digit and a units digit.

$$
4,\ 21,\ 24,\ 25,\ 26,\ 27,\ 28,\ 29,\ 30,\ 31,\ 32,\ 33,\ 34,\ 35,\ 36,\ 38,\ 40,\ 42,\ 44,\ 46,\ 48
$$

Step 2. Group the leaves by stem, which gives the display.

| Stem | Leaves | Count |
|---|---|---|
| $0$ | $4$ | $1$ |
| $2$ | $1\ 4\ 5\ 6\ 7\ 8\ 9$ | $7$ |
| $3$ | $0\ 1\ 2\ 3\ 4\ 5\ 6\ 8$ | $8$ |
| $4$ | $0\ 2\ 4\ 6\ 8$ | $5$ |

Step 3. The counts are $1$, $7$, $8$ and $5$, which total $21$ as required, and they also describe the shape: a single isolated low value, then a broad middle, then a modest falling off.

Marking point M9: the leaf counts must be shown, because they are the frequencies of the corresponding histogram and they verify that no observation has been lost.

Step 4. The median is the eleventh ordered value.

$$
\text{Median} = 32
$$

Step 5. With the convention that the lower quartile lies at position $(n+1)/4 = 5.5$, average the fifth and sixth ordered values.

$$
Q_1 = \frac{26 + 27}{2} = 26.5
$$

Step 6. The upper quartile lies at position $3(n+1)/4 = 16.5$, which are the sixteenth and seventeenth ordered values.

$$
Q_3 = \frac{38 + 40}{2} = 39
$$

Step 7. The five-number summary is $4$, $26.5$, $32$, $39$, $48$, and the interquartile range is $39 - 26.5 = 12.5$.

Step 8. Compute the fences.

$$
Q_1 - 1.5(12.5) = 26.5 - 18.75 = 7.75, \qquad Q_3 + 1.5(12.5) = 39 + 18.75 = 57.75
$$

Step 9. The observation $4$ lies below $7.75$, so it is a suspected outlier; no observation exceeds $57.75$.

Marking point M10: the outlier must be named with the fence it violates, and the box plot must show it as a separate point with the lower whisker drawn to $21$ rather than to $4$.

Step 10. Interpret the effect of the outlier. The mean of the $21$ marks is $673/21 = 32.05$, while the median is $32$; replacing $4$ by $0$ would lower the mean by $4/21 \approx 0.19$ and leave the median untouched. The median and the quartiles describe the bulk of the class, and the stem-and-leaf display is what reveals the single unusual value that the summary alone would conceal.

### 4.9 Problem E: three displays that lie

A newspaper prints three graphics. The first compares two schools with $30$ and $34$ prizes using a vertical bar chart whose axis begins at $28$. The second compares two enrolment figures of $200$ and $400$ using a picture of a student whose height and width are both doubled for the larger school. The third is a three-dimensional pie chart in which the sector for $10$ per cent is drawn at the front with its radius enlarged by a factor of $1.4$. Quantify the exaggeration in each case.

### 4.10 Solution E: measure the distortion rather than describe it

Step 1. For the truncated axis, the drawn lengths are the values minus the axis minimum.

$$
30 - 28 = 2, \qquad 34 - 28 = 6
$$

Step 2. Compare the apparent ratio with the true ratio.

$$
\frac{6}{2} = 3, \qquad \frac{34}{30} \approx 1.13
$$

The first school's lead appears threefold when it is really about one eighth, and the axis must begin at zero for the bar lengths to mean anything.

Step 3. For the pictogram, the area of the icon scales as the product of the two linear dimensions.

$$
2 \times 2 = 4
$$

Step 4. The area ratio is four while the data ratio is two, so the comparison is overstated by a factor of two. A correct pictogram enlarges one dimension only, or repeats a unit icon once per fixed number of units.

Step 5. For the three-dimensional pie chart, the area of the enlarged sector is multiplied by the square of the radius factor.

$$
(1.4)^{2} = 1.96
$$

Step 6. A sector representing $10$ per cent therefore occupies about $19.6$ per cent of the apparent area of the disc, nearly double its true share, while the remaining sectors keep their correct areas and are consequently squeezed.

Step 7. State the general lesson. Length encodes magnitude honestly only from a zero baseline; area encodes magnitude honestly only when one dimension varies; angle encodes proportion honestly only on a flat disc with a common radius.

### 4.11 Problem F: a time series and its moving average

The output of a workshop, in tonnes, was $120$, $132$, $128$, $150$, $165$ and $180$ in the six consecutive years from $2019$ to $2024$. Describe the movement, compute the three-point moving average and the year-on-year percentage changes, and state the equivalent constant annual growth rate.

### 4.12 Solution F: smooth the series, then summarise the growth

Step 1. Plot the quantity against the year, keeping the horizontal spacing between consecutive years equal and starting the vertical axis at zero, since a line graph that uses a truncated vertical axis exaggerates every rise.

Step 2. Describe the movement in words before computing anything. The series rises in four of the five intervals, with a single small fall between $2020$ and $2021$; the largest rise is between $2021$ and $2022$; and the general trend is upward throughout.

Step 3. Compute the year-on-year percentage changes by dividing each change by the previous value.

$$
\frac{12}{120} = 10\%, \quad \frac{-4}{132} \approx -3.03\%, \quad \frac{22}{128} \approx 17.19\%, \quad \frac{15}{150} = 10\%, \quad \frac{15}{165} \approx 9.09\%
$$

Step 4. Compute the three-point moving averages, placing each result at the centre of the three years it covers.

$$
\frac{120 + 132 + 128}{3} = 126.67, \qquad \frac{132 + 128 + 150}{3} = 136.67
$$

$$
\frac{128 + 150 + 165}{3} = 147.67, \qquad \frac{150 + 165 + 180}{3} = 165.00
$$

Step 5. Note that the moving average has four values against the six original observations, because a three-point average loses one value at each end. The smoothed series rises without interruption, which confirms that the single fall in $2021$ was a short-term fluctuation rather than a change of direction.

Step 6. Compute the equivalent constant annual growth rate. The overall growth factor is $180/120 = 1.5$ over five years, so the constant factor is the fifth root.

$$
G = 1.5^{1/5} \approx 1.0845
$$

Step 7. Convert the factor into a percentage and compare it with the arithmetic mean of the five annual changes, which is $(10 - 3.03 + 17.19 + 10 + 9.09)/5 = 8.65$ per cent. The compounding rate of $8.45$ per cent is the smaller of the two, as the geometric mean must be whenever the annual factors differ.

Marking point M11: the geometric mean is the correct summary of successive growth, and the arithmetic mean of the percentage changes overstates it.

Step 8. Interpret. Output grew by half again over five years, the growth was concentrated in the year $2022$, and the underlying rate was close to eight and a half per cent a year.

## 5. Mathematical Extensions, Limits, and Common Errors

### 5.1 The trap table

| Trap | What the candidate does | The correct handling |
|---|---|---|
| Counting | tallies an observation into two classes, or misses one at a boundary | cite the boundary convention and confirm the total equals $n$ |
| Half-gap | uses $0.5$ for data recorded to the nearest $0.1$ | read the precision from the data, not from habit |
| First boundary | begins the axis at the first lower limit | subtract the half-gap at both ends of the table |
| Equal heights | draws frequencies as heights although the widths differ | divide each frequency by its own width |
| Area check | never verifies that heights times widths return the frequencies | multiply back and add to $n$ |
| Polygon closure | leaves the polygon hanging above the axis | add a zero-frequency class one width beyond each end |
| Ogive axis | plots frequencies against class marks | plot cumulative frequencies against upper boundaries |
| Pie total | adds angles to $359^{\circ}$ or $361^{\circ}$ and ignores it | keep exact fractions, and report any rounding residual |
| Percentage bars | reads bar heights as group sizes | note that all bars are $100$ by construction |
| Median without order | takes the middle entry of an unsorted list | sort first, always |
| Quartile convention | mixes two conventions within one answer | state the convention once and apply it throughout |
| Box plot whisker | draws the whisker to the outlier | stop the whisker at the last value inside the fence |
| Scale mismatch | draws a histogram of nominal categories | match the display to the measurement scale |

### 5.2 The traps that cost the most marks

The counting trap is the most expensive because it contaminates every later part: a table with a total of $39$ instead of $40$ produces a histogram, an ogive and three quantiles that are all wrong, and the marker cannot award method marks for a wrong frequency column. The remedy is mechanical and cheap: cross off the raw list as each observation is tallied, and add the column twice, once upwards and once downwards.

The half-gap trap is the commonest conceptual error. It arises because candidates memorise "subtract $0.5$" as a ritual rather than deriving the gap from the recorded precision. When the data are recorded to the nearest kilogram the half-gap is $0.5$; when they are recorded to the nearest tenth it is $0.05$; when the classes are written without a gap, as in $0\text{–}10$, $10\text{–}20$, there is no gap to halve and the boundaries are the limits themselves. A candidate who states the precision and derives the gap cannot make the error, and the statement itself earns a mark.

The equal-heights trap is the one the topic exists to test. A histogram of unequal classes drawn with frequencies as heights misrepresents the data in a specific direction: wide classes are exaggerated and narrow classes are compressed. The density rule removes the distortion, and the area check proves that it has been removed.

### 5.3 What each representation refuses to tell you

A grouped table destroys the individual observations, so every statistic computed from it is an estimate. The mean computed from class marks is exact only when the observations in each class average exactly to the mark, which happens when each class is symmetric about its mark; otherwise the error is bounded by half a class width, and the bound shrinks as the classes narrow.

A histogram with equal widths shows the shape of the distribution but not the individual values, and a density histogram shows rates rather than counts, so its heights are not frequencies and cannot be read as such. A frequency polygon smooths the profile and is convenient for comparison, but its peaks and troughs are an artefact of the class marks chosen, and shifting the class boundaries by half a width can move a peak by half a class.

An ogive estimates quantiles under the uniform-within-class assumption. Where the data are concentrated at one end of a class, the computed quantile is pulled towards the centre of that class, and no amount of care in the drawing will recover the truth, because the information has already been discarded.

A pie chart compares parts of one whole and nothing else. It cannot display a negative value, it becomes unreadable beyond about six categories, and it cannot be used to compare two wholes of different sizes, since the two circles are usually drawn with different radii and the reader then compares areas rather than angles.

A box plot shows five numbers and therefore conceals the shape. Two data sets with the same five-number summary can have completely different histograms, one unimodal and one bimodal, and the box plot looks identical in both cases. A stem-and-leaf display, which keeps every leaf, is the honest companion to a box plot whenever the sample is small.

### 5.4 The three classic dishonest displays, with numbers

A truncated axis is dishonest in exact proportion to the distance of the baseline from zero. With bars of $30$ and $34$ drawn from a baseline of $28$, the apparent lengths are $2$ and $6$, so the apparent ratio is $3$ while the true ratio is $34/30 \approx 1.13$. Moving the baseline closer to the smaller value makes the distortion larger without limit: from a baseline of $29$ the lengths are $1$ and $5$.

An area-scaled pictogram is dishonest in proportion to the square of the linear enlargement. Doubling both dimensions of a picture multiplies its area by four, so a twofold difference in the data is presented as a fourfold difference in ink. The same error appears in three dimensions, where enlarging all three dimensions by $k$ multiplies volume by $k^{3}$ and turns a twofold difference into an eightfold one.

A three-dimensional pie chart is dishonest because the foreshortening applies unevenly. Sectors drawn at the front of the ellipse gain apparent area, sectors at the back lose it, and the radius factor applied to the front sectors raises their areas by its square. A sector of $36^{\circ}$, which is $10$ per cent of the data, becomes almost $20$ per cent of the apparent area when its radius is enlarged by $1.4$. The only safe pie chart is a flat one with a single radius.

A fourth distortion deserves mention because it appears in otherwise careful work: unequal class widths drawn as equal bars. Classes $0\text{–}10$ with $10$ observations and $10\text{–}30$ with $12$ observations look almost equal in height, yet the second class covers twice the range and its density of $0.6$ is little more than half the density of $1.0$ in the first. The vertical axis of an equal-width drawing is frequency, and the vertical axis of a density drawing is frequency per unit of the variable; confusing the two reverses the ranking of concentrations.

### 5.5 Revision checklist

Work through the list until each item can be performed without notes.

- Write the four measurement scales and, for each, one admissible and one inadmissible display.
- Define class limits, boundaries, width and mark, and compute all four for a table with a stated gap.
- Derive the half-gap from a stated recording precision, and state the boundary convention.
- Tally a list of forty observations into six classes and verify the total.
- State the frequency-density rule and prove that areas equal frequencies.
- Convert a table of unequal classes into a density table and check the areas sum to $n$.
- Locate the five points of a polygon and of an ogive, including the closing points.
- Compute a pie chart angle from a frequency, and check the total of the angles.
- Construct each of the four bar chart forms and say what each one compares.
- Build a stem-and-leaf display for twenty observations and read the median from it.
- Compute the five-number summary, the interquartile range and both fences.
- Compute the apparent and true ratios for a truncated axis, and the area factor for an enlarged pictogram.
- Explain in one sentence why a three-dimensional pie chart exaggerates its front sectors.

### 5.6 Time strategy in the examination

Allocate roughly one minute per mark. On a construction question, spend the first minute computing the range and choosing the class width, because a wrong width invalidates the whole table. Draw the axes before writing any table, label them with boundaries and units, and plot the rectangles or points as soon as the frequencies are known; a drawing that exists earns marks even if the last frequency is wrong.

On a multi-part question, complete the table once and use it for every later part. Do not recompute the cumulative column separately for the median, the quartiles and the ogive, since each recomputation is a fresh chance to introduce an error. Where a graphical reading and a computed value are both possible, do the computation first and use the graph as the check, because the computation is faster and the graph is the check the examiner expects.

Leave two minutes at the end for three checks that catch most losses: the frequencies sum to $n$, the final cumulative entry is $n$, and the pie angles sum to $360^{\circ}$. On a diagnostic question about a misleading display, budget four sentences: name the encoding, name the correct encoding, give the two ratios, and state the correction.

### 5.7 Consolidation

Representation is a translation exercise with a strict standard of fidelity. A table records counts; a histogram records counts per unit of the variable; an ogive records accumulated counts; a pie chart records shares of a whole; a bar chart records magnitudes across distinct categories; a box plot records five ordered positions. Each of these encodings is exact under conditions that can be stated in one line, and each becomes misleading the moment those conditions are violated — equal widths for heights-as-frequencies, a zero baseline for bar lengths, a common radius and a flat disc for sector angles, and a stated boundary convention for every table. A candidate who writes the convention, computes the density, checks the total and quantifies the distortion will rarely lose a mark in this topic, because the topic contains little algebra and almost all of its difficulty lies in discipline.

