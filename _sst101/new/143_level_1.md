## 1. Foundational Concepts, Definitions, and Axioms

### 1.1 A shoebox of receipts

Imagine a market trader who keeps every receipt of a busy month in a shoebox. By the end of the month the box holds four hundred thin paper slips, jumbled together in the order the sales happened. Now a customer asks a simple question: were most sales small, or were most of them large? The trader cannot answer quickly. Every sale is recorded, so nothing is missing, yet the answer is buried inside the order in which the slips were dropped into the box.

Picture what the trader actually does. The slips are tipped onto a table and sorted into piles: sales below one hundred shillings in one pile, sales from one hundred to two hundred in another, and so on. Then each pile is counted. Only after that counting can the trader say "most of my sales were between one and two hundred shillings". The sorting and counting replaced four hundred numbers with perhaps six piles and six counts.

That is the whole idea of this topic. **Data representation** means replacing a long unordered list of observations with a short ordered summary, so that a pattern which was invisible becomes obvious. Two families of tools do the work. **Tables** carry the counts in rows and columns. **Graphs** turn those counts into shapes that the eye can compare without reading any numbers at all.

Think of a librarian who wants to know which shelves are used most. Listing every borrowing event in the sequence it happened is useless for that question. Counting how many borrowings came from each shelf, and then drawing one bar per shelf, answers it immediately.

Nothing is thrown away by such a summary. A good summary is not a replacement for the data; it is the same data seen from a height, arranged so that the shape becomes visible. Everything that follows is a rule for building such a summary correctly, and a rule for checking that the building was done without error.

### 1.2 Frequency tables

Three words must be in place before a table can be read.

- An **observation** is one single recorded value. "Three goals" is one observation.
- A **variable** is the characteristic being measured, such as the number of goals scored by a team.
- The **frequency** of a value is the number of observations that take that value. The usual symbol is $f$, and it always means a count, never a proportion.

A **frequency distribution** is a table in which the observations are sorted into groups, and the number of observations falling in each group is written beside that group. The group is usually called a **class**, and the written count is the **frequency** of the class. The total number of observations is written $n$, and it is found by adding all the frequencies.

Here is a small example. A football team played fifteen matches and scored these numbers of goals, one figure per match:

$$
2,\ 1,\ 3,\ 2,\ 0,\ 4,\ 2,\ 1,\ 2,\ 3,\ 0,\ 2,\ 1,\ 5,\ 2
$$

Sorting these fifteen observations gives the following table. The tally column is a working aid: one short stroke stands for one observation, and every fifth stroke is drawn across the previous four so that groups of five can be counted at a glance.

| Goals scored | Tally marks | Frequency $f$ |
| --- | --- | --- |
| 0 | // | 2 |
| 1 | /// | 3 |
| 2 | //// / | 6 |
| 3 | // | 2 |
| 4 | / | 1 |
| 5 | / | 1 |
| **Total** | | **15** |

Two observations about that table matter more than they look. First, the frequencies add to fifteen, which is exactly the number of matches; a table whose frequencies do not add to the number of observations has lost or duplicated an observation. Second, the values are listed in order from $0$ upwards, even though the team never scored six goals. Order matters because it lets a reader scan for shape.

If a value is possible but did not occur, the honest thing is to write the value with frequency $0$ rather than to leave it out. Leaving it out makes the table look as though that value is impossible, which is a different and stronger claim.

### 1.3 Discrete and grouped frequency tables

There are two shapes a frequency table can take, and the choice between them is forced by the data.

A **discrete frequency distribution** gives one row to each distinct value that actually occurred. It suits a variable that moves in separate countable steps: the number of children in a family, the number of goals in a match, the number of letters in a word. Between two neighbouring values there is nothing at all, because a family cannot have two and a half children.

A **grouped frequency distribution** gathers neighbouring values into ranges called classes and gives one row to each range. It suits a variable measured on a continuous scale, where a finer measuring instrument would produce a different number for almost every observation. Mass in kilograms, height in centimetres, and time in seconds are all like this. If one hundred students are weighed, no two masses need agree to the nearest gram, so a table with one row per distinct mass would have one hundred rows and teach nothing.

The masses of one hundred female students were recorded and grouped as follows.

| Mass (kg) | Number of students |
| --- | --- |
| 50 – 52 | 5 |
| 53 – 55 | 18 |
| 56 – 58 | 42 |
| 59 – 61 | 27 |
| 62 – 64 | 8 |
| **Total** | **100** |

This is a grouped frequency distribution with five classes. Grouping buys compactness at a price: the table no longer records the exact mass of any individual student, only the range into which that mass fell. The price is worth paying when the shape of the whole distribution is the question, and it is not worth paying when individual values matter.

### 1.4 The words that describe a class

Six terms describe the parts of a grouped table. They are easy to confuse, so each is defined here with the same example, the class $50$–$52$ taken from the mass table.

- A **class** is one group in the table. The five groups of the mass table are its five classes.
- A **class interval** is the symbol that defines a class, written as two numbers with a dash between them, such as $50\text{–}52$. The dash is a label, not a subtraction sign.
- The **class limits** are the two numbers printed at the ends of the interval. The left-hand number, here $50$, is the **lower class limit**; the right-hand number, here $52$, is the **upper class limit**.
- The **class boundaries**, also called the **true class limits**, are the real dividing lines between neighbouring classes. They are found by splitting the gap between one class and the next. The upper limit of the first class is $52$ and the lower limit of the second class is $53$, so the true dividing line sits halfway between them, at $52.5$. Applying the same rule everywhere gives the six boundaries $49.5$, $52.5$, $55.5$, $58.5$, $61.5$ and $64.5$.
- The **class width**, also called the class size, is the distance from the lower boundary of a class to its upper boundary. For the first class the width is $52.5 - 49.5 = 3$ kilograms. Every class in this table has width $3$, which is what makes the classes directly comparable.
- The **class mark** is the midpoint of the class, found by averaging the two boundaries. For the first class the mark is $(49.5 + 52.5)/2 = 51$ kilograms, and for the last class it is $(61.5 + 64.5)/2 = 63$ kilograms.

Why do boundaries exist at all? Because masses are continuous while the labels are whole numbers. A student weighing $52.4$ kilograms must go somewhere, and only one class may hold her. The boundary at $52.5$ is the convention that decides all such cases: everything below $52.5$ goes into the first class, everything at or above $52.5$ goes into the second. The convention must be applied consistently, otherwise the frequencies will not add up.

The class mark exists because a graph needs one number to stand for a whole range. When the horizontal axis of a graph must carry five classes, it cannot carry five intervals; it carries the five marks $51$, $54$, $57$, $60$ and $63$, and each class is represented by its mark.

### 1.5 Relative frequency and cumulative frequency

Two further columns are added to a frequency table when a reader needs more than raw counts.

The **relative frequency** of a class is its frequency divided by the total number of observations. In words, it is the share of the data that fell in that class. If a class has frequency $f$ out of a total $n$, then the relative frequency is the fraction $f/n$. Multiplying by one hundred turns it into a percentage. For the mass table the relative frequency of the class $56$–$58$ is $42/100 = 0.42$, that is, forty-two per cent of the students.

The **cumulative frequency** of a class is the running total of frequencies up to and including that class. It answers a different question: not "how many are here?" but "how many are at or below this point?". Cumulative frequency is always non-decreasing as the reader moves down the table, and the last entry must equal the total number of observations. For the mass table the running totals are $5$, then $23$, then $65$, then $92$, then $100$; the final figure confirms the table.

| Mass (kg) | Frequency $f$ | Relative frequency | Cumulative frequency |
| --- | --- | --- | --- |
| 50 – 52 | 5 | 0.05 | 5 |
| 53 – 55 | 18 | 0.18 | 23 |
| 56 – 58 | 42 | 0.42 | 65 |
| 59 – 61 | 27 | 0.27 | 92 |
| 62 – 64 | 8 | 0.08 | 100 |
| **Total** | **100** | **1.00** | |

The relative frequencies add to $1.00$, which is the same check as the frequencies adding to the total, only expressed as shares.

### 1.6 The four graphs

A graph is a picture of a table. Four kinds are used most often, and each answers a different question.

A **bar chart** shows one bar per category. All bars have the same width, and they are separated by small gaps. The gaps are the visual signal that the categories are separate things and are not placed on one continuous scale. A bar chart suits qualitative data such as favourite subject or mode of travel, and it also suits discrete counts such as the number of goals per match. There are four common versions. A **simple bar chart** has one bar per category. A **component bar chart** stacks the parts of each category into a single bar, showing both the total and the breakdown. A **percentage component bar chart** rescales every bar to one hundred per cent, so that the breakdown can be compared between groups of different sizes. A **multiple bar chart** draws two or three bars side by side within each category, which is the natural choice for comparing the same categories in two different years.

A **histogram** shows the distribution of a continuous variable. It also uses rectangles, but the rectangles touch, because the classes are adjacent pieces of one continuous scale. The base of each rectangle spans the class boundaries, and its height equals the class frequency. The touching edges and the absence of gaps are the visual signal that the underlying variable runs continuously from the smallest value to the largest.

A **pie chart** shows the parts of a single whole. A circle is divided into sectors, one per category, and each sector's angle is proportional to that category's share of the total. Because a full turn is $360$ degrees, a category holding a fraction $f/n$ of the data receives an angle of $(f/n) \times 360$ degrees. Pie charts are readable when there are few categories and unreadable when there are many, because small sectors cannot be compared by eye.

A **line graph** plots a quantity against an ordered axis, usually time, and joins consecutive plotted points with straight segments. It is the natural display for change: sales by month, temperature by hour, population by year. A line graph requires the horizontal axis to have a true order, because a line drawn between two points asserts that the values in between are meaningful.

Two refinements of these four deserve mention at once. A **frequency polygon** is a line graph of frequency against class mark, obtained by joining the midpoints of the tops of the histogram rectangles; it is useful because several distributions can be drawn on one set of axes as lines instead of as overlapping shaded blocks. An **ogive** is a line graph of cumulative frequency against the upper class boundary; it is used to read off how many observations lie below a chosen value, and to estimate the median.

### 1.7 Stem-and-leaf displays and box plots

Two further displays preserve more information than a grouped table.

A **stem-and-leaf display** splits every observation into a leading part, the **stem**, and a final digit, the **leaf**. For marks out of one hundred the stem is the tens digit and the leaf is the units digit, so the mark $47$ is written as a leaf $7$ on the stem $4$. The display looks like a small table but it is not a summary that has thrown information away: every individual observation is still visible, and reading the leaves in order gives the sorted data back exactly. The display can be turned on its side to become a histogram, so it is often the first step before grouping.

A **box plot**, also called a box-and-whisker plot, shows five numbers at once: the smallest value, the lower quartile, the median, the upper quartile and the largest value. The **quartiles** cut the sorted data into four parts of roughly equal size. The box runs from the lower quartile to the upper quartile and therefore contains the middle half of the data, its length being the **interquartile range**. A line inside the box marks the median, and two whiskers run out to the smallest and largest values that are not regarded as unusually far away. A box plot is the fastest way to compare the spread of two groups, because the length of the box and the length of the whiskers can be compared directly.

### 1.8 Choosing a display from the scale of measurement

The measurements in a data set live on one of four scales, and the scale decides which arithmetic and which display are honest.

- **Nominal** data differ only by name. Blood group, religion and mode of travel are nominal. There is no order, so a line graph would invent a sequence that does not exist.
- **Ordinal** data differ by name and by order, but the gaps between neighbouring categories are not measurable. Examination grades and satisfaction ratings are ordinal.
- **Interval** data have equal distances between neighbouring values but an arbitrary zero. Temperature in degrees Celsius is the standard example: the difference between ten and twenty degrees is meaningful, but "twice as hot" is not.
- **Ratio** data have equal distances and a true zero, so ratios are meaningful. Mass, income and time are ratio measurements.

For nominal data a bar chart or a pie chart is correct. For ordinal data a bar chart is correct, and the bars are best drawn in the order of the scale. For interval and ratio data a histogram, a frequency polygon, an ogive or a box plot is correct, and a line graph is correct when the horizontal axis is time. Choosing a pie chart for a continuous variable, or a histogram for nominal categories, is not a matter of taste; it is a misstatement about the data.

## 2. Theorems, Lemmas, and Analytical Properties

### 2.1 The total-frequency identity

The first and most useful property is that the frequencies of a frequency distribution always add up to the number of observations. If there are $k$ classes with frequencies $f_1, f_2, \dots, f_k$, and $n$ observations in total, then

$$
\sum_{i=1}^{k} f_i = n
$$

In words: add every count in the frequency column and the answer must be the size of the data set. The reason is that every observation is placed in exactly one class and no observation is left out. Any table that fails this test has a counting error, and no later calculation built on it can be trusted.

### 2.2 The relative-frequency identity

The relative frequencies of the classes always add to one, and their percentages always add to one hundred. Writing the relative frequency of class $i$ as $f_i/n$,

$$
\sum_{i=1}^{k} \frac{f_i}{n} = \frac{1}{n}\sum_{i=1}^{k} f_i = \frac{n}{n} = 1
$$

In words: the shares of a whole must exhaust the whole. This identity is a second, independent check on the table, and it becomes the justification for the pie chart later.

### 2.3 The boundary rule

A class boundary is the midpoint between the upper limit of one class and the lower limit of the next class. If a class ends with upper limit $U$ and the next class begins with lower limit $L$, the boundary $b$ is

$$
b = \frac{U + L}{2}
$$

In words: take the last printed number of the lower class, take the first printed number of the upper class, add them, and halve. For the mass table the join between $50\text{–}52$ and $53\text{–}55$ gives $b = (52 + 53)/2 = 52.5$. When the printed limits differ by one unit the boundary sits a half unit past the upper limit, which is why the boundaries of that table are $49.5$, $52.5$, $55.5$, $58.5$, $61.5$ and $64.5$.

The same half-unit offset is applied to the outside ends of the table, so that the first class gets a lower boundary of $49.5$ and the last class gets an upper boundary of $64.5$. Without that step the first and last rectangles of a histogram would be the only ones whose bases were wrong.

### 2.4 The width rule

The class width is the distance between the two boundaries of a class:

$$
w = \text{upper boundary} - \text{lower boundary}
$$

For the first class of the mass table, $w = 52.5 - 49.5 = 3$. An equivalent statement is that the width is the gap between two consecutive lower boundaries, since $52.5 - 49.5 = 3$ for the first pair and $55.5 - 52.5 = 3$ for the next. The two routes agree whenever the classes are contiguous, and checking both routes is a quick way to catch a table whose classes are not in fact contiguous.

Class width must never be computed as upper limit minus lower limit plus one, nor as upper limit minus lower limit alone, unless the convention of the table has been stated. The boundary definition is the only one that always works.

### 2.5 The class-mark rule

The class mark is the average of the two boundaries:

$$
m = \frac{\text{lower boundary} + \text{upper boundary}}{2}
$$

Averaging the printed limits gives the same answer, because the half-unit offset added to one end is subtracted from the other and the midpoint does not move. For the first class of the mass table both routes give $51$; for the last class both give $63$.

The class mark is the number used in place of the whole class whenever a calculation needs a single representative value. It is also the horizontal position at which a frequency polygon is plotted.

### 2.6 The cumulative-frequency rules

Three properties of the cumulative frequency column are used constantly.

- **Monotone increase.** Cumulative frequency never falls as the reader moves down the table, because each step adds a frequency and a frequency cannot be negative.
- **Final value.** The last cumulative frequency equals the total number of observations $n$.
- **Reading off.** The cumulative frequency of a class counts all observations at or below that class's upper boundary, so it can be read as "how many observations lie below this point".

Writing $F_j$ for the cumulative frequency of class $j$, the rules are

$$
F_j = \sum_{i=1}^{j} f_i, \qquad F_k = n, \qquad F_j \ge F_{j-1}
$$

### 2.7 The histogram area rule

In a histogram with equal class widths, each rectangle has a base of length $w$ and a height equal to the class frequency $f$. The area of the rectangle is therefore $w \cdot f$. Since $w$ is the same for every class, area is proportional to frequency, so comparing the heights of the rectangles is the same as comparing the frequencies. This is why an ordinary histogram may be drawn with frequency on the vertical axis.

The vertical axis label in such a case is "frequency", and the horizontal axis is marked at the class boundaries, not at the class limits. Marking the limits would leave gaps between rectangles that do not exist in the data.

### 2.8 The frequency-density rule

When class widths differ, frequency can no longer be the height of the rectangle, because a wide class would then be drawn as both tall and wide and would dominate the picture out of all proportion to its count. The correct height is the **frequency density**, defined as frequency divided by class width:

$$
\text{frequency density} = \frac{f}{w}
$$

With that height the area of a rectangle is $(f/w) \cdot w = f$, which is exactly the class frequency. Equal areas then correspond to equal counts, whatever the widths, and the whole histogram has total area $n$.

An example makes the point. Suppose the weekly incomes, in thousands of shillings, of sixty traders are tabulated in four classes with widths $5$, $5$, $10$ and $20$. The frequencies are $8$, $16$, $24$ and $12$. The densities are $8/5 = 1.6$, $16/5 = 3.2$, $24/10 = 2.4$ and $12/20 = 0.6$. The class with the largest frequency, the third, is not the class with the tallest rectangle; the second class is taller because its frequency is packed into a narrower band. Drawing frequencies as heights would have reversed that comparison.

### 2.9 The frequency-polygon rule

A frequency polygon plots the class frequency against the class mark, one point per class, and joins consecutive points with straight segments. Because the class mark is the midpoint of the class, the plotted point sits exactly above the centre of the corresponding histogram rectangle, at a height equal to that rectangle. The polygon therefore passes through the midpoints of the tops of the rectangles, and both displays carry the same information.

The polygon is usually closed by adding one empty class at each end, drawn on the horizontal axis, so that the line returns to zero and forms a closed shape.

### 2.10 The ogive rule

An ogive plots the cumulative frequency against the **upper class boundary**, not against the class mark. The reason is that the cumulative frequency of a class counts everything at or below that class's upper boundary, so the upper boundary is the readout point. The first plotted point sits at the upper boundary of the first class with height $f_1$, and the last sits at the upper boundary of the last class with height $n$.

Because cumulative frequency only changes at boundaries, the honest shape of the cumulative distribution is a staircase. Joining the plotted points with straight lines is a smoothing device that assumes the observations within each class are spread evenly across that class. That assumption is what makes the graphical estimate of the median possible.

### 2.11 The pie-chart angle rule

If a category has frequency $f$ and the whole data set has $n$ observations, the angle $\theta$ of its sector is

$$
\theta = \frac{f}{n} \times 360^{\circ}
$$

In words: the category's share of the data is the same as its share of the full turn. Since the shares add to one, the angles add to $360^{\circ}$, which is the standard arithmetic check on a finished pie chart.

### 2.12 The bar-chart rules

Four rules separate a bar chart from a histogram.

- Bars are separated by gaps, because the categories are distinct and not neighbouring points on a scale.
- All bars have the same width, so that only the height carries information.
- The height of a bar is proportional to the frequency, and the vertical axis must start at zero; a bar truncated at the bottom misstates the ratio between two categories.
- The four variants answer four different questions: a simple bar chart compares totals, a component bar chart shows a total and its parts together, a percentage component bar chart compares the composition of groups whose totals differ, and a multiple bar chart compares the same category across two or more groups.

### 2.13 The line-graph rules

A line graph requires an ordered horizontal axis, and it claims that the quantity between two plotted points is meaningfully interpolated. Three rules follow.

- The vertical axis of a line graph should start at zero whenever the graph is meant to convey magnitude rather than mere direction of change. If it does not, the graph must say so.
- The horizontal spacing must match the spacing of the time intervals; irregular gaps drawn at equal spacing distort the apparent rate of change.
- The aspect ratio of the panel controls the apparent steepness. Stretching the vertical axis exaggerates every change, and compressing it hides real ones.

### 2.14 The stem-and-leaf and box-plot rules

A stem-and-leaf display keeps every observation, so its leaves can be counted to recover $n$, and reading down the stems with leaves in order returns the sorted data. Reversing it gives a histogram with the class width implied by the stem unit.

A box plot reports five numbers: the minimum, the lower quartile $Q_1$, the median $Q_2$, the upper quartile $Q_3$ and the maximum. The interquartile range is $Q_3 - Q_1$ and measures the spread of the middle half of the data. A value is conventionally treated as an outlier when it lies more than one and a half interquartile ranges beyond a quartile, that is when it is below $Q_1 - 1.5(Q_3 - Q_1)$ or above $Q_3 + 1.5(Q_3 - Q_1)$.

## 3. Formal Proofs, Derivations, and Methods

### 3.1 Why the frequencies add to the number of observations

The data set consists of $n$ observations. Building a frequency table means assigning each observation to exactly one class. Write $A_i$ for the set of observations placed in class $i$, and let $f_i$ be the number of observations in $A_i$.

Every observation is assigned, so the classes together contain all $n$ observations. No observation is assigned twice, so the classes do not overlap. Therefore the total number of observations is the sum of the numbers in the classes:

$$
n = f_1 + f_2 + \cdots + f_k = \sum_{i=1}^{k} f_i
$$

This is why the total row is not optional. It is the only check that detects both a missed observation and a double-counted one, and it costs nothing to perform.

### 3.2 Why the class mark is halfway

Take a class with lower boundary $L$ and upper boundary $U$. The width is $U - L$, and the midpoint is by definition the point at distance $(U - L)/2$ above $L$:

$$
m = L + \frac{U - L}{2} = \frac{2L + U - L}{2} = \frac{L + U}{2}
$$

The same value is obtained by averaging the printed limits when the class is written with integer limits, because moving each limit inward or outward by the same half unit leaves the average unchanged. That is why either route gives $51$ for the class $50$–$52$ and $63$ for the class $62$–$64$.

### 3.3 Deriving the frequency-density formula

Let a class have width $w$ and frequency $f$, and let the rectangle drawn over it have height $h$. The area of the rectangle is $w \cdot h$.

We want the picture to be read by area, so that twice the area means twice the count. That requires the area to be proportional to the frequency for every class, and the simplest choice of constant of proportionality is one:

$$
w \cdot h = f
$$

Solving for the height,

$$
h = \frac{f}{w}
$$

which is the frequency density. The total area of the whole histogram is then

$$
\sum_{i=1}^{k} w_i h_i = \sum_{i=1}^{k} f_i = n
$$

In words, the histogram encloses $n$ square units, one unit of area per observation. Any sub-interval of the horizontal axis therefore has an area equal to the number of observations lying in that sub-interval, and the proportion of the data inside the sub-interval is that area divided by $n$. This is the property that makes density histograms honest when the widths are unequal.

### 3.4 Deriving the pie-chart angle formula

The angles of all sectors must fill the circle, whose total is $360^{\circ}$. We require the angle of each sector to be proportional to its frequency, so there is a constant $c$ with

$$
\theta_i = c f_i
$$

Summing over all $k$ sectors and using the fact that the angles fill the circle,

$$
360^{\circ} = \sum_{i=1}^{k} \theta_i = c \sum_{i=1}^{k} f_i = c n
$$

Hence $c = 360^{\circ}/n$, and therefore

$$
\theta_i = \frac{360^{\circ}}{n} f_i = \frac{f_i}{n} \times 360^{\circ}
$$

Two consequences follow immediately. A category with twice the frequency of another has twice the sector angle, and the sector angles sum to $360^{\circ}$, which is the arithmetic check.

### 3.5 Method: building a grouped frequency table from raw data

The construction follows a fixed sequence, and every step has a check.

1. Find the smallest and largest observations, and subtract to get the range.
2. Decide on a number of classes, usually between five and ten. A common guide is Sturges' rule, which gives the number of classes as $1 + 3.322 \log_{10} n$ rounded up.
3. Divide the range by the number of classes and round the result **up** to a convenient number. That convenient number is the class width.
4. Set the lower boundary of the first class at or just below the smallest observation, then add the width repeatedly to generate every boundary.
5. Convert the boundaries into written class limits, using the same half-unit offset throughout.
6. Tally every observation into exactly one class, applying the rule that a value sitting on a boundary belongs to the class whose lower boundary it equals.
7. Write the frequencies, add the total, and check that the total equals the number of observations.
8. Add the class marks, then the relative frequencies, then the cumulative frequencies, checking that the last cumulative frequency equals $n$.

Rounding the width up rather than down matters. If the width is rounded down, the number of classes needed to cover the range exceeds the number planned and the last class overflows the largest observation.

### 3.6 Method: reading a median from an ogive

The median is the value that splits the data into two halves, so it corresponds to a cumulative frequency of $n/2$. The graphical procedure is as follows.

1. Compute $n/2$.
2. On the vertical axis of the ogive, mark the height $n/2$.
3. Move horizontally from that height to the plotted ogive.
4. Move vertically down to the horizontal axis and read the value there.

The result is a graphical interpolation, and it can be reproduced arithmetically. If the ogive is drawn as a straight line across a class whose lower boundary is $L$, whose width is $w$ and whose frequency is $f$, and if the cumulative frequency at $L$ is $F$, then the median $M$ satisfies

$$
M = L + \frac{n/2 - F}{f} \times w
$$

The same recipe with $n/4$ in place of $n/2$ gives the lower quartile, and with $3n/4$ it gives the upper quartile. The fraction $(n/2 - F)/f$ is the proportion of the class that must be crossed, and multiplying by $w$ converts that proportion into a distance along the horizontal axis.

### 3.7 Method: drawing a histogram with unequal widths

1. Convert every written class into its boundaries.
2. Compute the width of each class as the difference of its boundaries.
3. Compute the frequency density of each class as frequency divided by width.
4. Mark the horizontal axis at every boundary and the vertical axis in units of frequency density.
5. Draw one rectangle per class, spanning its two boundaries and rising to its density.
6. Check the picture by areas: each rectangle's area must equal its frequency, and the areas must total $n$.

The check in step six is the whole point. Without it, a wide class with a moderate count will look like a tall class with a large count, and the reader will draw the wrong conclusion about where the data are concentrated.

### 3.8 Method: building a stem-and-leaf display and a box plot

For the stem-and-leaf display:

1. Choose the stem unit. For two-digit marks out of one hundred the stem is the tens digit.
2. Write the stems in increasing order down the page, including stems with no leaves only if the gap is informative.
3. Write each leaf on its own stem, and keep the leaves in increasing order along the row.
4. Count the leaves to confirm that the total equals the number of observations.

For the box plot:

1. Sort the data.
2. Find the median, splitting the sorted list into two halves.
3. Find the lower quartile as the median of the lower half, and the upper quartile as the median of the upper half.
4. Compute the interquartile range as the upper quartile minus the lower quartile.
5. Compute the outlier fences at one and a half interquartile ranges below the lower quartile and above the upper quartile.
6. Draw the box from the lower to the upper quartile with a line at the median, then draw whiskers to the smallest and largest values that fall inside the fences.

## 4. Representative Worked Examples and Solutions

### 4.1 Problem: a discrete table for the number of children

In a survey of thirty-five families in a village the number of children per family was recorded as follows.

$$
\begin{aligned}
&1 \quad 0 \quad 2 \quad 3 \quad 4 \quad 5 \quad 6 \\
&7 \quad 2 \quad 3 \quad 4 \quad 0 \quad 2 \quad 5 \\
&8 \quad 4 \quad 5 \quad 12 \quad 6 \quad 3 \quad 2 \\
&7 \quad 6 \quad 5 \quad 3 \quad 3 \quad 7 \quad 8 \\
&9 \quad 7 \quad 9 \quad 4 \quad 5 \quad 4 \quad 3
\end{aligned}
$$

Represent the data as a discrete frequency distribution, and state the total.

### 4.2 Solution: tally, count, check

Step 1. Find the smallest and largest values. The smallest is $0$ and the largest is $12$, so the table must run from $0$ to $12$ inclusive.

Step 2. Decide the type of table. The variable is a count of children, so it can only take whole numbers, and a discrete table with one row per value is the right choice.

Step 3. Tally each value. Reading through the list and marking one stroke per occurrence, then grouping the strokes in fives, gives the frequencies below.

| Number of children | Tally marks | Frequency $f$ |
| --- | --- | --- |
| 0 | // | 2 |
| 1 | / | 1 |
| 2 | //// | 4 |
| 3 | //// / | 6 |
| 4 | //// | 5 |
| 5 | //// | 5 |
| 6 | /// | 3 |
| 7 | //// | 4 |
| 8 | // | 2 |
| 9 | // | 2 |
| 10 | — | 0 |
| 11 | — | 0 |
| 12 | / | 1 |
| **Total** | | **35** |

Step 4. Add the frequencies and check the total.

$$
2 + 1 + 4 + 6 + 5 + 5 + 3 + 4 + 2 + 2 + 0 + 0 + 1 = 35
$$

The total equals the number of families surveyed, so no observation has been lost or counted twice.

Step 5. Interpret. The most common family size is three children, with six families, and the distribution is right-skewed, because a single family with twelve children stretches the upper tail far beyond the rest of the data.

### 4.3 Problem: a grouped table from raw data

The marks of forty students in a test marked out of one hundred were recorded as follows.

$$
\begin{aligned}
&68 \quad 74 \quad 51 \quad 83 \quad 92 \quad 47 \quad 65 \quad 78 \quad 61 \quad 55 \\
&88 \quad 72 \quad 63 \quad 49 \quad 77 \quad 85 \quad 58 \quad 66 \quad 71 \quad 94 \\
&52 \quad 69 \quad 81 \quad 57 \quad 74 \quad 62 \quad 43 \quad 79 \quad 68 \quad 86 \\
&59 \quad 73 \quad 64 \quad 90 \quad 53 \quad 67 \quad 76 \quad 82 \quad 48 \quad 70
\end{aligned}
$$

Build a grouped frequency distribution, and add the relative and cumulative frequency columns.

### 4.4 Solution: five classes of width eight

Step 1. Find the range. The smallest mark is $43$ and the largest is $94$, so the range is

$$
94 - 43 = 51
$$

Step 2. Choose the number of classes. Sturges' rule gives

$$
1 + 3.322 \log_{10}(40) = 1 + 3.322 \times 1.602 = 6.32
$$

which rounds up to seven classes.

Step 3. Choose the class width. Dividing the range by seven gives

$$
\frac{51}{7} = 7.29
$$

so the width is rounded up to the convenient value $8$.

Step 4. Fix the boundaries. Starting at $40$, which is just below the smallest mark, and adding $8$ repeatedly gives the boundaries $40$, $48$, $56$, $64$, $72$, $80$, $88$ and $96$. Converting these into written limits gives the seven classes $40$–$47$, $48$–$55$, $56$–$63$, $64$–$71$, $72$–$79$, $80$–$87$ and $88$–$95$.

Step 5. Tally each mark into its class, remembering that a mark on a boundary belongs to the class that starts there.

| Marks | Tally marks | Frequency $f$ | Relative frequency | Cumulative frequency |
| --- | --- | --- | --- | --- |
| 40 – 47 | // | 2 | 0.050 | 2 |
| 48 – 55 | //// / | 6 | 0.150 | 8 |
| 56 – 63 | //// / | 6 | 0.150 | 14 |
| 64 – 71 | //// //// | 9 | 0.225 | 23 |
| 72 – 79 | //// /// | 8 | 0.200 | 31 |
| 80 – 87 | //// | 5 | 0.125 | 36 |
| 88 – 95 | //// | 4 | 0.100 | 40 |
| **Total** | | **40** | **1.000** | |

Step 6. Check the totals. The frequencies add to

$$
2 + 6 + 6 + 9 + 8 + 5 + 4 = 40
$$

the relative frequencies add to $1.000$, and the last cumulative frequency is $40$. All three checks agree.

Step 7. Add the class marks, computed as the average of each pair of boundaries.

| Marks | Class mark |
| --- | --- |
| 40 – 47 | 43.5 |
| 48 – 55 | 51.5 |
| 56 – 63 | 59.5 |
| 64 – 71 | 67.5 |
| 72 – 79 | 75.5 |
| 80 – 87 | 83.5 |
| 88 – 95 | 91.5 |

Step 8. Interpret. The tallest class is $64$–$71$, with nine students, and the distribution has a single peak with a longer tail towards the low marks. Ten of the forty students, that is one quarter, scored below $56$.

### 4.5 Problem: limits, boundaries, width and mark

For the mass table with classes $50$–$52$, $53$–$55$, $56$–$58$, $59$–$61$ and $62$–$64$, state the class limits, the class boundaries, the class width and the class marks.

### 4.6 Solution: read the join, then offset

Step 1. Read the limits. The lower limits are $50$, $53$, $56$, $59$ and $62$; the upper limits are $52$, $55$, $58$, $61$ and $64$.

Step 2. Find one boundary from a join. The upper limit of the first class is $52$ and the lower limit of the second is $53$, so

$$
\frac{52 + 53}{2} = 52.5
$$

Step 3. Apply the same half-unit offset throughout. Subtracting $0.5$ from each lower limit and adding $0.5$ to each upper limit gives the boundaries $49.5$, $52.5$, $55.5$, $58.5$, $61.5$ and $64.5$.

Step 4. Compute the width.

$$
52.5 - 49.5 = 3
$$

Step 5. Compute the marks.

$$
\frac{49.5 + 52.5}{2} = 51, \quad \frac{52.5 + 55.5}{2} = 54, \quad \frac{55.5 + 58.5}{2} = 57
$$

$$
\frac{58.5 + 61.5}{2} = 60, \quad \frac{61.5 + 64.5}{2} = 63
$$

Step 6. Interpret. Five rectangles of equal width $3$ would be drawn between the boundaries $49.5$ and $64.5$, with heights $5$, $18$, $42$, $27$ and $8$, and the polygon would pass through the five marks at those heights.

### 4.7 Problem: a pie chart of travel modes

Two hundred students were asked how they travel to school. Eighty travel by bus, fifty walk, thirty cycle, twenty-five come by car and fifteen come by train. Compute the sector angle for each category and check the total.

### 4.8 Solution: share of the whole, times three hundred sixty

Step 1. Confirm the total.

$$
80 + 50 + 30 + 25 + 15 = 200
$$

Step 2. Compute the bus sector.

$$
\frac{80}{200} \times 360^{\circ} = 144^{\circ}
$$

Step 3. Compute the walking sector.

$$
\frac{50}{200} \times 360^{\circ} = 90^{\circ}
$$

Step 4. Compute the cycling sector.

$$
\frac{30}{200} \times 360^{\circ} = 54^{\circ}
$$

Step 5. Compute the car sector.

$$
\frac{25}{200} \times 360^{\circ} = 45^{\circ}
$$

Step 6. Compute the train sector.

$$
\frac{15}{200} \times 360^{\circ} = 27^{\circ}
$$

Step 7. Check that the angles fill the circle.

$$
144 + 90 + 54 + 45 + 27 = 360
$$

The check passes, so the arithmetic is consistent.

Step 8. Interpret. The bus sector is larger than a right angle, so more than a quarter of the students travel by bus, and the train sector is smaller than a tenth of the circle, which is at the limit of what a reader can judge by eye.

### 4.9 Problem: unequal widths

The weekly incomes of sixty traders, in thousands of shillings, are grouped into the classes $0$–$4$ with frequency $8$, $5$–$9$ with frequency $16$, $10$–$19$ with frequency $24$, and $20$–$39$ with frequency $12$. Compute the frequency density of each class and identify the class with the tallest rectangle.

### 4.10 Solution: area is the frequency, height is the density

Step 1. Convert the classes into boundaries, which are $0$ to $5$, $5$ to $10$, $10$ to $20$ and $20$ to $40$.

Step 2. Compute the widths.

$$
5 - 0 = 5, \quad 10 - 5 = 5, \quad 20 - 10 = 10, \quad 40 - 20 = 20
$$

Step 3. Compute the densities.

$$
\frac{8}{5} = 1.6, \quad \frac{16}{5} = 3.2, \quad \frac{24}{10} = 2.4, \quad \frac{12}{20} = 0.6
$$

Step 4. Check the areas.

$$
5 \times 1.6 = 8, \quad 5 \times 3.2 = 16, \quad 10 \times 2.4 = 24, \quad 20 \times 0.6 = 12
$$

Every area equals its class frequency, so the picture is honest.

Step 5. Identify the tallest rectangle. It is the second class, from $5$ to $10$, with density $3.2$, even though its frequency of $16$ is smaller than the frequency of $24$ in the third class. Plotting raw frequencies as heights would have produced the opposite and wrong impression.

Step 6. Interpret. The traders are concentrated in the second and third bands, and the fourth band is spread so thinly over twenty thousand shillings that its density is lower than that of any other class.

### 4.11 Problem: stem-and-leaf and box plot

The following twenty marks were obtained in a test: $34$, $37$, $41$, $42$, $45$, $45$, $48$, $52$, $53$, $55$, $56$, $58$, $61$, $63$, $67$, $71$, $74$, $78$, $82$, $89$. Build a stem-and-leaf display and a five-number summary, and state the interquartile range.

### 4.12 Solution: leaves in order, then quartiles

Step 1. Choose the stem unit. The marks have two digits, so the stem is the tens digit and the leaf is the units digit.

Step 2. Write the leaves on their stems in increasing order.

| Stem | Leaves |
| --- | --- |
| 3 | 4 7 |
| 4 | 1 2 5 5 8 |
| 5 | 2 3 5 6 8 |
| 6 | 1 3 7 |
| 7 | 1 4 8 |
| 8 | 2 9 |

Step 3. Count the leaves to confirm the total.

$$
2 + 5 + 5 + 3 + 3 + 2 = 20
$$

Step 4. Find the median. With twenty observations the median is the average of the tenth and eleventh values in order, which are $55$ and $56$:

$$
\frac{55 + 56}{2} = 55.5
$$

Step 5. Find the lower quartile. The lower half contains the first ten values, whose fifth and sixth values are both $45$:

$$
\frac{45 + 45}{2} = 45
$$

Step 6. Find the upper quartile. The upper half contains the last ten values, whose fifth and sixth values are $67$ and $71$:

$$
\frac{67 + 71}{2} = 69
$$

Step 7. Compute the interquartile range.

$$
69 - 45 = 24
$$

Step 8. Compute the outlier fences.

$$
45 - 1.5 \times 24 = 9, \qquad 69 + 1.5 \times 24 = 105
$$

Both the minimum $34$ and the maximum $89$ lie inside these fences, so no observation is an outlier and the whiskers run to $34$ and $89$.

Step 9. Interpret. The box runs from $45$ to $69$ with a line at $55.5$, the median sits close to the centre of the box, and the two whiskers are of similar length, so the marks are close to symmetric with a slight pull towards the higher values.

### 4.13 Problem: a truncated vertical axis

A company reports revenue of $1010$ million, $1015$ million and $1020$ million in three consecutive quarters. A line graph is drawn with the vertical axis running from $1000$ to $1020$. Explain the distortion.

### 4.14 Solution: compare the true ratio with the drawn ratio

Step 1. Compute the true change across the three quarters.

$$
1020 - 1010 = 10
$$

Step 2. Compute the true ratio of the last value to the first.

$$
\frac{1020}{1010} = 1.0099
$$

So revenue rose by about one per cent.

Step 3. Compute the apparent ratio on the truncated axis. With the axis running from $1000$ to $1020$, the height above the axis is $1010 - 1000 = 10$ at the first point and $1020 - 1000 = 20$ at the last point. The drawn heights are in the ratio

$$
\frac{20}{10} = 2
$$

Step 4. State the distortion. The picture shows the last point twice as high as the first, suggesting a doubling, while the true increase is about one per cent. The whole of the exaggeration comes from cutting off the bottom of the axis.

Step 5. State the correction. A line graph intended to convey magnitude must start its vertical axis at zero. A graph intended only to show the direction of change may truncate the axis, but the truncation must be stated so that the reader does not read a ratio from the picture.

## 5. Mathematical Extensions, Limits, and Common Errors

A frequency table is a lossy compression, and the loss has consequences that must be understood rather than ignored. Once the observations inside a class are replaced by the class mark, every later calculation inherits an error, because the class mark is only an average and the individual values are gone. For a class of width $w$, no observation can lie more than half a width from the class mark, so the grouped mean can differ from the true mean by at most half a class width. That bound is the reason a grouped mean is a summary and not a measurement: it is exact as arithmetic about the substituted values, but approximate as a description of the original data. The same reasoning governs the median read from an ogive, which assumes that the observations inside each class are spread evenly across it. If they are bunched at one end of the class, the interpolated median is pulled away from the truth in a predictable direction.

The beginner errors in this topic are few but they are made by almost every learner at least once, and each one is cheap to avoid.

- *Confusing limits with boundaries.* The limits are the numbers printed in the class label, such as $50$ and $52$. The boundaries are the true dividing lines, such as $49.5$ and $52.5$. A histogram is drawn on the boundaries, and a class width is computed from the boundaries. Writing the limits on the horizontal axis of a histogram leaves fake gaps between the rectangles.
- *Computing the width from the limits.* The difference $52 - 50 = 2$ is not the class width of the class $50$–$52$; the width is $3$. The limit difference undercounts by one whole unit whenever the classes are written with integer limits, and it undercounts by the boundary gap in every other case.
- *Forgetting the zero rows in a discrete table.* If no family had ten children, the row for ten still belongs in the table, with frequency $0$. Dropping it makes the table claim that ten children is impossible.
- *Leaving out the total.* The total row is the only routine check on the tally. A table without it invites a silent counting error into every later calculation.
- *Plotting a frequency polygon against class limits.* The polygon is defined on class marks, because the mark is the point that represents the whole class.
- *Drawing a histogram of unequal classes with frequency as the height.* This exaggerates the wide classes enormously. The height must be the frequency density, and the check is that each rectangle's area equals its frequency.
- *Using separated bars for continuous data.* Gaps assert that the categories are separate. A histogram of a continuous variable must have touching rectangles, because the classes are adjacent pieces of one scale.
- *Using a histogram for nominal categories.* A histogram implies an order and a continuous scale. Blood groups have neither.
- *Forgetting to convert a share into an angle.* A pie chart sector is not labelled by the frequency or the percentage; it is drawn at the angle $(f/n) \times 360^{\circ}$.
- *Truncating the vertical axis of a bar chart.* Because a bar chart is read by the length of the bar, cutting the axis below zero makes a small difference look like a large one. This single error accounts for a large share of misleading charts in newspapers.
- *Scaling a pictogram by height but claiming proportionality by area.* If a symbol representing twice the quantity is drawn at twice the height, it must also be drawn at twice the width to keep its shape, so its area becomes four times as large. The reader perceives a fourfold increase where only a doubling occurred.

Three specific distortions deserve to be named because they recur so often in published material. The first is the **truncated axis**, already analysed in the worked example: a vertical axis that starts at a large positive number converts a one per cent change into a picture that looks like a doubling. The second is the **area-scaled pictogram**: a row of little figures or bags or coins whose sizes are doubled to represent doubled values, which multiplies the perceived quantity by four. The remedy, if a pictogram must be used, is either to repeat identical symbols, one per unit of quantity, or to scale the symbol's area rather than its linear size and to say so. The third is the **three-dimensional pie chart**. Tilting a circle compresses it into an ellipse, and a compression in one direction does not preserve angles: a sector of ninety degrees that points towards the viewer can appear as little as fifty-three degrees, while a sector of the same ninety degrees at the far edge can appear as about one hundred and twenty-seven degrees. Two categories holding equal shares then look as though one is more than twice the other. The raised rim of an extruded pie makes the distortion worse, because the visible thickness adds area to the sectors nearest the reader.

Beyond these distortions lie genuine extensions. A frequency distribution is the first member of a family of summary objects: relative frequency turns it into a probability distribution over the classes, cumulative frequency turns it into a distribution function, and the histogram turns it into a density estimate. The ogive is the empirical distribution function drawn with straight segments, and the box plot is the five-number summary drawn as a shape. Understanding that all four are views of one underlying object — the sorted data — is what lets a reader move between them without confusion, and it is what lets a reader recognise a display that has been built to mislead rather than to inform.

Two limits should be stated plainly. A summary cannot answer a question about individual values: once the data are grouped, the exact mass of the heaviest student is no longer recoverable, and no amount of arithmetic will bring it back. And a display cannot repair a bad data set: if the sample was chosen badly, then every table and every graph built from it will be precise, attractive and wrong. Representation is a tool for seeing what is in the data, never a tool for making the data say something it does not contain.
