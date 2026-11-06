## 1. Foundational Concepts, Definitions, and Axioms

### 1.1 An everyday starting point

Imagine that you have been asked to tidy the lost-property cupboard at a school. Everything is piled on one table: scarves, shoes, water bottles, exercise books, a broken watch, a pair of glasses. Nobody has told you how to sort them, and if you simply start making piles at random the cupboard will be no tidier than before. So you look for differences that matter. Some things can be described by a word, such as "scarf" or "shoe". Other things can be described by an amount, such as a sixty-centimetre ruler or a water bottle holding half a litre. Within the words, some carry a natural order, such as small, medium, and large shirts, while others do not, such as red, blue, and green scarves. Within the amounts, some are counted in whole pieces, such as four shoes, while others are measured on a smooth scale, such as the length of a lace.

That is the whole subject in miniature. Data are the recorded results of looking at things, and the way you are allowed to tidy them depends on what kind of thing each recorded value is. A number that comes from counting behaves differently from a number that comes from measuring, and a word behaves differently from either. Sorting first, and calculating second, is the habit this topic teaches.

The word statistics has a formal meaning too. Statistics is the science of data. It involves collecting, classifying, summarizing, organizing, analyzing, and interpreting numerical information. Notice that classifying comes second and calculating comes later, because the classification decides what the calculating is allowed to be.

### 1.2 What a variable is

Before the types of data can be named, we need the word variable.

> **Definition (Variable).** A variable is a characteristic or property of an individual unit in the group being studied.

A unit is one member of the group: one student, one family, one shopper, one patient. The variable is the characteristic you write down about that unit, such as eye colour or height. The value you write down for one unit is called an observation. The whole collection of observations is called a data set.

Here is a small example that will be used throughout this note. A school nurse records four things about each of five learners: the learner's blood group, the learner's opinion of the school canteen on a scale of poor, fair, good, or excellent, the number of brothers and sisters the learner has, and the learner's height in centimetres. There are four variables and five units, so the data set has twenty observations in total.

### 1.3 The two big families of data

> **Definition (Quantitative data).** Quantitative data are measurements that are recorded on a naturally occurring numerical scale.

> **Definition (Qualitative data).** Qualitative data are measurements that cannot be measured on a natural numerical scale; they can only be classified into one of a group of categories.

The test is the phrase naturally occurring numerical scale. Ask one question: could this value be replaced by a completely different label without losing anything except the label itself? If the answer is yes, the data are qualitative. Blood group could be written as A, B, AB, and O, or as red, green, blue, and yellow, and nothing would be lost. Height could not be written that way, because the value carries an amount.

Qualitative data are also called categorical data, because each observation puts its unit into a category. Quantitative data are also called numerical data, because each observation is a genuine number produced by counting or by measuring.

The word naturally is doing important work. A category can be given a number by a clerk: card payment could be coded as $1$, cash as $2$, and mobile as $3$. Those digits are labels wearing a costume. They do not become measurements because they are written as figures.

### 1.4 Qualitative data part one: nominal

> **Definition (Nominal data).** Nominal data are qualitative data whose categories are only names, with no natural order among them.

Blood group is nominal. So are eye colour, religion, the brand of a phone, the region a person lives in, and the reason a patient attended a clinic. The list of categories can be written in any order at all, and the order changes nothing. You are allowed to count how many units fall in each category, and you are allowed to work out what fraction of the whole that count represents. You are not allowed to say that one category is bigger than another, because the categories are not numbers.

Nominal data also give you one kind of average, and only one: the mode, which is the category that occurs most often. If more learners in the survey are blood group O than any other, then O is the modal blood group. That sentence is meaningful. The sentence "the average blood group is B" is not.

### 1.5 Qualitative data part two: ordinal

> **Definition (Ordinal data).** Ordinal data are qualitative data whose categories have a natural order, but where the size of the step between one category and the next is not defined.

The canteen opinion is ordinal: poor, fair, good, excellent. There is clearly a direction. Excellent is better than good, and good is better than fair. But there is no reason to believe that the jump from poor to fair is the same size as the jump from good to excellent. The labels are words, and words are not spaced like the marks on a ruler.

Other examples are school grades, military ranks, stages of an illness, sizes of clothing, and star ratings given to a shop. Ordinal data allow everything nominal data allow, and in addition they allow ranking. You may say that one learner was more satisfied than another, and you may find the middle category, called the median, which is the category occupied by the learner in the middle when everyone has been lined up in order. You may also report how many learners were at least "good", which is a cumulative count.

What you may not do is treat the categories as equally spaced numbers. That is the single most common mistake in this whole topic, and Section 5 returns to it.

### 1.6 Quantitative data part one: discrete

> **Definition (Discrete data).** Discrete data are quantitative data whose possible values are separate, with no possible value in between, and which arise from counting.

The number of brothers and sisters is discrete. A learner can have $2$ siblings or $3$ siblings, but never $2.5$ siblings. The number of children in a family, the number of goals in a match, the number of cars passing a gate in an hour, and the number of pages in a book are all discrete.

Here is the quickest test, and it is worth memorising. Take two neighbouring values and find the number exactly halfway between them. If that halfway value is impossible, the data are discrete. Halfway between $2$ and $3$ is $2.5$, and $2.5$ siblings is impossible, so the count is discrete.

Discrete data can be written as a table that lists every possible value with the number of times it occurred. Nothing is lost by doing this, because the values that do not appear are impossible rather than merely unobserved. That kind of table is called a discrete frequency distribution.

### 1.7 Quantitative data part two: continuous

> **Definition (Continuous data).** Continuous data are quantitative data that can take any value in an interval, however finely the interval is divided, and which arise from measuring.

Height is continuous. Two learners might both be recorded as $160$ centimetres and $161$ centimetres, but between those two heights lies every height you can name, such as $160.4$ centimetres. The halfway test confirms it: halfway between $160$ and $161$ is $160.5$, and that is a perfectly possible height.

Other continuous examples are mass, time, temperature, distance, rainfall, and the volume of a bottle. In each case the value comes from comparing the quantity with a standard unit, which is what measuring means.

Continuous data cannot be listed value by value in practice, because two measurements are almost never exactly equal. They are placed into groups called classes, such as heights from $150$ to $154$ centimetres and from $155$ to $159$ centimetres, and each class is counted. That kind of table is called a grouped frequency distribution, and it is the standard way to summarise continuous measurements.

A warning belongs here, because it catches almost everyone once. The paperwork can make a continuous variable look discrete. If the nurse writes heights to the nearest whole centimetre, every observation is a whole number, but height has not become discrete. The measured quantity is still smooth; only the ink is coarse. Always apply the halfway test to the variable, not to the printed figures.

### 1.8 The four scales, and why they matter

The nominal and ordinal split applies to qualitative data, and the discrete and continuous split applies to quantitative data. A second and slightly deeper classification cuts across both families and asks how much information a recorded value carries. It has four levels.

- **Nominal scale.** The values are names only. The only comparison is same or different. Blood group is on this scale.
- **Ordinal scale.** The values can be put in order. Canteen opinion is on this scale.
- **Interval scale.** The values are numbers with equal spacing, but the zero point is a matter of convention. Temperature in degrees Celsius is on this scale, because the spacing between degrees is equal while zero degrees is simply the freezing point of water, not the absence of heat.
- **Ratio scale.** The values are numbers with equal spacing and a true zero, so that one value can be said to be twice another. Height, mass, income, and the number of siblings are on this scale.

The four scales form a ladder. Each rung allows everything the rung below it allows, and adds something. A name tells you only whether two things are the same. Order tells you which is more. Equal spacing tells you by how much. A true zero tells you how many times as much.

The difference between interval and ratio is worth a moment, because it is the one that sounds most academic and matters most in practice. The difference between $10$ degrees and $20$ degrees equals the difference between $20$ degrees and $30$ degrees, so on the Celsius scale you may compare gaps. But $20$ degrees is not twice as warm as $10$ degrees, because the zero was chosen by people rather than found in nature. Mass is different. Twenty kilograms really is twice ten kilograms, because zero kilograms means no mass at all.

Each rung is recognised by an everyday question and admits one more kind of average than the rung beneath it.

| Scale | What the values allow | Everyday test | Average allowed |
|---|---|---|---|
| Nominal | Same or different only | Names with no order | Mode |
| Ordinal | Same, different, and ordered | Names that can be ranked | Median category |
| Interval | Order and equal differences | Numbers with a made-up zero | Mean |
| Ratio | Order, differences, and ratios | Numbers with a true zero | Mean, geometric mean |

### 1.9 Why the scale decides the average

Averages are not interchangeable. Each one reads a different feature of the data, and each one needs a certain amount of structure before it means anything.

The mode reads only the commonest category, so it needs only names. The median reads only position in the ordered list, so it needs order. The mean reads the actual sizes of the numbers, adding them and dividing, so it needs equal spacing, because adding assumes that each unit step is worth the same as every other. The geometric mean multiplies values together, which only makes sense when the values are positive quantities with a true zero.

The same ladder applies to measures of spread. For nominal data the only sensible question is how evenly the observations are spread across the categories, and an index built from the category counts answers it. For ordinal data you can report the range of categories from the lowest quarter to the highest quarter, but you should report the two categories as a pair rather than subtract one from the other. For interval and ratio data the standard deviation is available, because it is built from differences from the mean. For ratio data alone the coefficient of variation is available, because it divides the standard deviation by the mean, and that division requires the mean to be measured from a true zero.

### 1.10 Why the scale decides the graph

Graphs carry the same information as averages, so they obey the same rules. Nominal data are drawn as bars with gaps between them, because the gaps show that the categories are separate. Ordinal data are also drawn as bars, but the bars must be arranged in their natural order, from worst to best or from smallest to largest. Continuous data are drawn as a histogram, in which the bars touch, because touching bars show that the values run smoothly into one another along the axis. Two measurements taken on the same individuals are drawn as a scatter of points. Two categorical variables recorded on the same individuals are drawn as a grid of counts called a contingency table, or as groups of bars.

Getting this wrong is not a small blemish. A histogram drawn for blood groups claims, in the language of graphs, that blood groups lie along a smooth scale, which is false. A bar chart drawn for heights with gaps between the bars claims that no height lies between the classes, which is also false.

### 1.11 Two variables at once

Sometimes two variables are recorded for the same unit, and the interesting question is how they are connected. A contingency table handles this when both variables are categories. The categories of one variable are written down the side as rows, the categories of the other are written across the top as columns, and each cell holds the number of units that have both characteristics.

| Canteen opinion | Boarder | Day scholar | Total |
|---|---|---|---|
| Poor | 6 | 4 | 10 |
| Fair | 10 | 8 | 18 |
| Good | 12 | 16 | 28 |
| Excellent | 4 | 10 | 14 |
| Total | 32 | 38 | 70 |

Reading a table like this needs three different habits. Reading across a whole row and using the right-hand total answers "how many learners gave this opinion?" Reading down a whole column and using the bottom total answers "how many learners are boarders?" Reading inside one row or one column and dividing by that row or column total answers "among boarders, what fraction said good?" The third question is the one most reports actually ask, and the third number is the one most reports forget to compute.

### 1.12 A note on symbols

Very little notation is needed for this topic, but the notation that is used must be read correctly.

The letter $n$ stands for the number of observations. If five learners are measured, then $n = 5$. The letter $x$ stands for the variable being measured, and $x_i$ stands for the value of that variable for the $i$-th unit, where $i$ is a counting label running from $1$ up to $n$. The symbol $\bar{x}$, read as "x bar", stands for the mean of the observations. The Greek capital letter $\sum$, read as "sigma", is an instruction to add up everything that follows it. The letter $f$ stands for a frequency, which is a count of how many times a value occurs.

$$
\bar{x} = \frac{1}{n}\sum_{i=1}^{n} x_i
$$

In words, this says: add all the observations together, and then divide by how many there are. The letter $k$ is used for the number of distinct categories or classes in a frequency table, and $m$ for the class mark, which is the middle value of a class.

## 2. Theorems, Lemmas, and Analytical Properties

The results in this section are the rules that connect a scale to the calculations it allows. Each is stated as a claim, and each is followed by the reason it is true in ordinary language, because a rule that is memorised without its reason is forgotten under examination pressure.

> **Result 1 (The classification test).** A variable is quantitative exactly when its observations lie on a naturally occurring numerical scale, and qualitative otherwise.

The test is applied by asking what would be lost if the observation were replaced by a different label. If nothing but the label is lost, the variable is qualitative. If an amount is lost, the variable is quantitative.

> **Result 2 (Nominal and ordinal are distinguished by order alone).** Qualitative data are nominal when the categories cannot be ranked, and ordinal when they can be ranked but the sizes of the steps are undefined.

The second clause matters. Order by itself does not promote data to the quantitative family, because order does not supply the equal spacing that arithmetic needs. An ordinal variable is still a categorical variable.

> **Result 3 (Discrete and continuous are distinguished by the halfway test).** Quantitative data are discrete when a value halfway between two possible values is impossible, and continuous when it is possible.

The test is applied to the variable rather than to the recorded digits. Age is continuous, even though it is often written in whole years.

> **Result 4 (Each scale licenses one new kind of average).** Nominal data admit the mode; ordinal data admit the mode and the median; interval data admit the mean as well; ratio data admit the geometric mean as well.

The ladder of averages matches the ladder of scales exactly, and for a reason. Each new average consumes one more piece of structure: the mode uses only counts, the median uses order, the mean uses equal spacing, and the geometric mean uses a true zero.

> **Result 5 (A change of unit must not change a summary).** Any summary that is worth reporting must survive a change in the way the data are recorded, apart from the corresponding change in its own units.

This is the deepest rule in the topic and the easiest to state informally. If converting heights from centimetres to metres destroys a comparison, then the comparison was never about height. It was about the numbers that happened to be written down.

> **Result 6 (The mean moves with a change of unit).** If every observation is converted by multiplying by a number and then adding a number, the mean is converted in exactly the same way.

This is why the mean is allowed on an interval scale. Converting degrees Celsius to degrees Fahrenheit is exactly such a conversion, and the mean temperature converts correctly along with the data.

> **Result 7 (The standard deviation moves with the unit but ignores the zero).** If every observation is multiplied by a number, the standard deviation is multiplied by the size of that number, and if a constant is added to every observation, the standard deviation does not change.

The reason is that spread is about differences, and differences are unaffected by shifting the whole data set up or down. This is why the standard deviation is allowed on an interval scale but the coefficient of variation is not.

> **Result 8 (The coefficient of variation needs a true zero).** The coefficient of variation, which is the standard deviation divided by the mean, changes if the zero point is moved, so it is only meaningful for ratio data.

Divisions compare a quantity with a quantity measured from zero. If the zero is arbitrary, the division is arbitrary too.

> **Result 9 (Frequencies must add to the sample size).** In any frequency table, whether the categories are values or classes, the frequencies add up to the total number of observations, that is $\sum f = n$.

This is the arithmetic health check for every table. If the total is wrong, an observation has been lost or counted twice, and the remedy is to retally rather than to adjust the total.

> **Result 10 (Row and column totals must agree).** In a contingency table, adding the row totals gives the same answer as adding the column totals, and both equal the sample size.

This follows from the fact that each unit contributes exactly one count to the body of the table, so it is counted once in its row and once in its column.

> **Result 11 (Grouping always loses detail).** When continuous observations are replaced by the marks of the classes into which they fall, the summary computed from the marks is an approximation, and the error cannot exceed half a class width.

The reason is that every observation in a class lies within half a class width of the class mark, so replacing it by the mark makes an error no larger than that. Making the classes narrower makes the approximation better.

> **Result 12 (Independence has a testable form).** Two categorical variables are independent when the pattern of one is the same inside every category of the other, and under independence the expected count in a cell is the row total multiplied by the column total and divided by the sample size.

The expected count answers the question "if the two variables had nothing to do with each other, how many would we expect here?", and comparing it with the observed count is how an association is first detected.

## 3. Formal Proofs, Derivations, and Methods

The demonstrations in this section are deliberately small, because the point is to see why a rule holds rather than to practise long division. Every step is written out.

### 3.1 Demonstration: the mean follows a change of unit

Take three masses of $10$, $20$, and $30$ kilograms. The mean is

$$
\bar{x} = \frac{10 + 20 + 30}{3} = \frac{60}{3} = 20
$$

Now convert every mass to grams by multiplying by $1000$. The observations become $10000$, $20000$, and $30000$, and their mean is

$$
\bar{y} = \frac{10000 + 20000 + 30000}{3} = \frac{60000}{3} = 20000
$$

The mean in grams is $1000$ times the mean in kilograms, which is exactly what converting the mean itself would have produced. Nothing about the data changed; only the unit changed, and the mean moved with it.

The same thing happens with a shift. Take temperatures of $20$ and $26$ degrees Celsius, whose mean is $23$ degrees. In degrees Fahrenheit the observations are

$$
1.8(20) + 32 = 68, \qquad 1.8(26) + 32 = 78.8
$$

and their mean is $73.4$, while converting the Celsius mean gives $1.8(23) + 32 = 73.4$. The two routes agree, which is why a mean temperature is a fair summary.

### 3.2 Demonstration: the mean breaks when the spacing is changed

Take three ratings coded $1$, $2$, and $3$. The mean is

$$
\bar{x} = \frac{1 + 2 + 3}{3} = 2
$$

Now suppose a researcher believes the top rating is much further from the middle one than the middle is from the bottom, and recodes the three categories as $1$, $2$, and $9$. The order is untouched: the first is still smallest, the second still in the middle, and the third still largest. Both codings describe the same ratings. Yet the mean of the new codes is

$$
\bar{y} = \frac{1 + 2 + 9}{3} = 4
$$

The mean has doubled, while the median has stayed at the second category in both codings and the mode has stayed the same as well. Since an ordinal scale accepts any relabelling that preserves order, and the mean changes under such a relabelling, the mean is not licensed by an ordinal scale. This is the demonstration behind Result 4.

### 3.3 Demonstration: a code average describes the code

Suppose a clinic records how patients arrived: $1$ for walk-in, $2$ for ambulance, and $3$ for referral. In one week the counts are $20$ walk-ins, $5$ ambulance arrivals, and $5$ referrals.

If someone averages the codes, the calculation is

$$
\frac{20(1) + 5(2) + 5(3)}{30} = \frac{20 + 10 + 15}{30} = \frac{45}{30} = 1.5
$$

The answer of $1.5$ is arithmetic that runs correctly and means nothing at all. Swap the codes so that walk-in is $3$ and referral is $1$, and the average becomes

$$
\frac{20(3) + 5(2) + 5(1)}{30} = \frac{60 + 10 + 5}{30} = \frac{75}{30} = 2.5
$$

The patients did not change; only the clerk's keypad did. The honest summary is the modal category, which is walk-in with $20$ out of $30$ patients, together with the proportions in each category.

### 3.4 Demonstration: why the coefficient of variation needs a true zero

Take two masses of $10$ kilograms and $30$ kilograms, so the mean is $20$ kilograms and the standard deviation, computed from the two deviations of $10$ kilograms each, is $10$ kilograms. The coefficient of variation is

$$
v = \frac{10}{20} = 0.5
$$

Now measure the same two objects with a scale that has been offset by $5$ kilograms, so the readings are $15$ and $35$. The mean is $25$ and the standard deviation is still $10$, because both readings moved together. The coefficient is now

$$
v' = \frac{10}{25} = 0.4
$$

The spread of the objects has not changed one bit, but the index has fallen from $0.5$ to $0.4$. An offset is a perfectly acceptable change of recording only when the scale is interval rather than ratio, and here it was not acceptable: mass has a true zero, and shifting it destroys the meaning. That is precisely why the coefficient belongs to ratio data, where no such offset is allowed.

### 3.5 Method: how to classify any variable in four questions

Step 1. Ask whether the observation could be replaced by a different label without losing information. If yes, the variable is qualitative and you go to Step 2. If no, it is quantitative and you go to Step 3.

Step 2. Ask whether the categories can be ranked. If they cannot, the variable is nominal. If they can, the variable is ordinal, and you should note that the sizes of the steps are still undefined. Stop here.

Step 3. Ask whether a value halfway between two possible values is possible. If it is impossible, the variable is discrete. If it is possible, the variable is continuous.

Step 4. Ask whether a true zero exists, that is whether a value of zero means none of the quantity. If it does, the scale is ratio and every average is available. If it does not, the scale is interval and ratios are unavailable.

### 3.6 Method: build a discrete frequency table without losing an observation

Step 1. Write down the smallest and the largest observed value, because the table must cover everything between them.

Step 2. List every whole-number value from the smallest to the largest, including the ones that never occur.

Step 3. Read the raw data once, in a fixed order such as left to right and top to bottom, placing one mark beside the value each time it appears.

Step 4. Convert the marks into numbers and add the numbers up.

Step 5. Compare the total with the number of observations. If the two disagree, retally rather than adjust.

### 3.7 Method: build a grouped table for continuous data

Step 1. Note the precision of the instrument, which is the smallest difference the instrument can report. A scale reading to the nearest kilogram has a precision of $1$ kilogram.

Step 2. Place boundaries half a precision step beyond each recorded value. Recorded values of $50$ and $51$ therefore acquire a boundary at $50.5$ between them.

Step 3. Choose classes of equal width, preferably starting at a boundary rather than at a recorded value.

Step 4. Compute each class mark by averaging the two boundaries of the class.

Step 5. Tally and check that the frequencies add to the number of observations.

### 3.8 Method: read a contingency table in the right direction

Step 1. Identify which variable is in the rows and which is in the columns.

Step 2. If the question asks about a subgroup, find the row or column total for that subgroup and divide each cell inside it by that total.

Step 3. If the question asks how large a group is overall, use the marginal total and do not divide.

Step 4. Check that the percentages inside any row or column add to $100$ per cent, which is the sign that the correct denominator was used.

## 4. Representative Worked Examples and Solutions

### 4.1 Problem: classify the school nurse's four variables

The nurse records blood group, canteen opinion, number of brothers and sisters, and height in centimetres for each of five learners. Classify each variable, name its scale, and say which average may be reported.

### 4.2 Solution: four questions, one variable at a time

Step 1. Blood group. The observation is a name, and replacing it with another label would lose nothing but the label, so the variable is qualitative. The categories cannot be ranked, so it is nominal. The only average available is the mode.

Step 2. Canteen opinion. The observation is a word, so the variable is qualitative. The four words poor, fair, good, and excellent can be ranked, so the variable is ordinal. But the step from poor to fair need not equal the step from good to excellent, so the scale stops at ordinal. The median category and the mode are available, and the mean is not.

Step 3. Number of brothers and sisters. The observation is a count, so the variable is quantitative. Halfway between $2$ and $3$ siblings is $2.5$ siblings, which is impossible, so the variable is discrete. Zero siblings means none, so the scale is ratio and the mean is available.

Step 4. Height in centimetres. The observation is a measurement, so the variable is quantitative. Halfway between $160$ and $161$ centimetres is $160.5$ centimetres, which is possible, so the variable is continuous. Zero height means no height, so the scale is ratio and the mean and standard deviation are available.

Step 5. Summarise.

| Variable | Family | Type or scale | Average allowed |
|---|---|---|---|
| Blood group | Qualitative | Nominal | Mode |
| Canteen opinion | Qualitative | Ordinal | Median category |
| Number of siblings | Quantitative | Discrete, ratio | Mean |
| Height | Quantitative | Continuous, ratio | Mean |

Step 6. Note the trap. If the nurse writes heights as $160$ and $161$, the figures look like counts, but height is still continuous. The digits were rounded; the variable was not changed.

### 4.3 Problem: build a discrete frequency table

A class records the number of pets owned by each of $20$ learners, with these results: $0, 1, 1, 0, 2, 3, 1, 2, 2, 0, 1, 4, 1, 2, 0, 3, 1, 1, 2, 1$. Build the frequency table and find the mode and the mean.

### 4.4 Solution: tally, check, then summarise

Step 1. Classify. The observation is a count, and $1.5$ pets is impossible, so the data are discrete and quantitative.

Step 2. Find the range. The smallest value is $0$ and the largest is $4$, so the table must run from $0$ to $4$.

Step 3. Tally each value.

| Number of pets | Tally marks | Frequency |
|---|---|---|
| 0 | //// | 4 |
| 1 | //// /// | 8 |
| 2 | //// | 5 |
| 3 | // | 2 |
| 4 | / | 1 |
| Total | | 20 |

Step 4. Check the total:

$$
4 + 8 + 5 + 2 + 1 = 20
$$

which matches the number of learners, so no observation was lost.

Step 5. Name the mode. The largest frequency is $8$, attached to the value $1$, so the modal number of pets is $1$.

Step 6. Compute the mean:

$$
\bar{x} = \frac{0(4) + 1(8) + 2(5) + 3(2) + 4(1)}{20} = \frac{0 + 8 + 10 + 6 + 4}{20} = \frac{28}{20} = 1.4
$$

Step 7. Interpret. The mean of $1.4$ pets is a legitimate summary because the variable is quantitative and ratio-scaled. The value $1.4$ is not itself an attainable number of pets, which is normal for a mean of counts, and it should not be reported as though some learner owned one and a half animals.

### 4.5 Problem: read a contingency table

The table of canteen opinion by boarding status records $70$ learners in total. Among boarders, $6$ said poor, $10$ said fair, $12$ said good, and $4$ said excellent. Among day scholars, $4$ said poor, $8$ said fair, $16$ said good, and $10$ said excellent. Find the conditional distribution of opinion among boarders, the conditional distribution among day scholars, and the overall proportion who said good.

### 4.6 Solution: fix the denominator before dividing

Step 1. Add the row of boarders to find the correct denominator:

$$
6 + 10 + 12 + 4 = 32
$$

Step 2. Divide each boarder count by $32$:

$$
\frac{6}{32} = 0.1875, \qquad \frac{10}{32} = 0.3125, \qquad \frac{12}{32} = 0.375, \qquad \frac{4}{32} = 0.125
$$

Step 3. Add the row of day scholars to find their denominator:

$$
4 + 8 + 16 + 10 = 38
$$

Step 4. Divide each day-scholar count by $38$:

$$
\frac{4}{38} \approx 0.105, \qquad \frac{8}{38} \approx 0.211, \qquad \frac{16}{38} \approx 0.421, \qquad \frac{10}{38} \approx 0.263
$$

Step 5. Check both sets of proportions by adding them:

$$
0.1875 + 0.3125 + 0.375 + 0.125 = 1
$$

and the second set also totals approximately $1$, which confirms that the correct denominators were used.

Step 6. Compare the two profiles. About $37.5$ per cent of boarders rated the canteen good and $42.1$ per cent of day scholars did, so the two groups are similar at that point, but the extremes differ: boarders are more likely to say poor and day scholars are more likely to say excellent.

Step 7. Compute the overall proportion who said good, using the grand total this time:

$$
\frac{12 + 16}{70} = \frac{28}{70} = 0.4
$$

Step 8. Note the difference between the two readings. The overall figure of $40$ per cent is a marginal percentage and describes the whole school; the figure of $37.5$ per cent is a conditional percentage and describes boarders only. Both are correct, and they answer different questions.

### 4.7 Problem: average an ordinal rating correctly

Five learners rate the library as $1$ for poor, $2$ for fair, $3$ for good, $4$ for very good, and $5$ for excellent. The ratings are $2$, $3$, $3$, $4$, and $5$. Report a defensible average and explain why a mean of the codes is not defensible.

### 4.8 Solution: rank first, then summarise

Step 1. Confirm the scale. The ratings are ordered, but the sizes of the steps between labels are undefined, so the scale is ordinal.

Step 2. Put the ratings in order:

$$
2, \quad 3, \quad 3, \quad 4, \quad 5
$$

Step 3. Find the middle position. With five observations the middle is the third, which carries the value $3$.

Step 4. Report the median as a category. The median rating is good, and it should be written as a category rather than as the number $3$ alone.

Step 5. Find the mode. The value $3$ occurs twice and every other value occurs once, so the modal rating is also good.

Step 6. Show what a mean would do. The mean of the codes is

$$
\frac{2 + 3 + 3 + 4 + 5}{5} = \frac{17}{5} = 3.4
$$

Step 7. Show that this mean is not stable. Recode the five categories as $2$, $3$, $4$, $7$, and $9$, which keeps the order intact and is therefore an acceptable relabelling on an ordinal scale. The mean is now

$$
\frac{2 + 3 + 4 + 7 + 9}{5} = \frac{25}{5} = 5
$$

Step 8. Conclude. The median stayed at the third category and the mode stayed at good under both codings, while the mean moved from $3.4$ to $5$. The mean is therefore a statement about the codes, and the median is a statement about the ratings.

### 4.9 Problem: summarise a grouped continuous table

The masses of $100$ students are grouped as $50$ to $52$ kilograms with $5$ students, $53$ to $55$ with $18$, $56$ to $58$ with $42$, $59$ to $61$ with $27$, and $62$ to $64$ with $8$. Find the class boundaries, the class marks, and the mean mass.

### 4.10 Solution: boundaries, marks, then the weighted total

Step 1. Confirm the scale. Mass is measured and can take any value in an interval, so the data are continuous and must be grouped. Because masses are given to the nearest kilogram, the boundary sits half a kilogram beyond each stated end.

Step 2. Write the boundaries in order:

$$
49.5, \quad 52.5, \quad 55.5, \quad 58.5, \quad 61.5, \quad 64.5
$$

Step 3. Compute one class width as a check:

$$
52.5 - 49.5 = 3
$$

and note that each neighbouring pair differs by the same $3$, so the classes are of equal width.

Step 4. Compute the five class marks by averaging each pair of boundaries:

$$
51, \quad 54, \quad 57, \quad 60, \quad 63
$$

Step 5. Multiply each class mark by its frequency and add:

$$
5(51) + 18(54) + 42(57) + 27(60) + 8(63) = 255 + 972 + 2394 + 1620 + 504 = 5745
$$

Step 6. Divide by the total frequency:

$$
\bar{x} = \frac{5745}{100} = 57.45
$$

Step 7. Interpret. The mean mass is about $57.5$ kilograms, and because every student was represented by the mark of her class, the answer is an approximation. The worst error in any single replacement is half a class width, that is $1.5$ kilograms, so the mean is reported with that qualification rather than as an exact figure.

### 4.11 Problem: choose an average and a graph for four situations

Four situations are described: the religion of $500$ respondents, the pain grade of $80$ patients, the waiting time in minutes of $200$ patients, and the temperatures in degrees Celsius at noon on $30$ days. For each, name the scale, the average, and a suitable graph.

### 4.12 Solution: match the summary to the structure

Step 1. Religion. The values are unordered names, so the scale is nominal. The average is the mode, and the graph is a bar chart with gaps, or a pie chart because the categories make up the whole sample.

Step 2. Pain grade. The values are ordered words, so the scale is ordinal. The average is the median category, reported as a category, and the graph is a bar chart whose bars are arranged in order from mild to severe.

Step 3. Waiting time. Time is measured with a true zero, so the scale is ratio and continuous. The mean and standard deviation are available, and the graph is a histogram, with an ogive if the cumulative picture is wanted.

Step 4. Temperature in degrees Celsius. Degrees have equal spacing but a made-up zero, so the scale is interval. The mean is available, the coefficient of variation is not, and the graph is again a histogram. A statement that one day was twice as hot as another would be meaningless on this scale.

Step 5. Summarise in a table.

| Situation | Scale | Average | Graph |
|---|---|---|---|
| Religion | Nominal | Mode | Bar chart with gaps |
| Pain grade | Ordinal | Median category | Ordered bar chart |
| Waiting time | Ratio, continuous | Mean | Histogram |
| Temperature in Celsius | Interval | Mean | Histogram |

Step 6. Note the pattern. The graph changed whenever the structure of the values changed, and the average changed at exactly the same points.

## 5. Mathematical Extensions, Limits, and Common Errors

### 5.1 What the classification does not tell you

The classification of a variable into a scale is a statement about what the recorded values can express, not a statement about how the study was designed. A nominal variable measured on a huge random sample is still nominal, and no amount of data will turn a category into a measurement. Conversely, a ratio variable measured badly is still ratio, but the measurements may be so unreliable that the extra arithmetic the scale permits is wasted. Scale and quality are two different properties, and confusing them leads to the belief that more data can repair a badly chosen summary.

A second limit is that scales are often chosen by the researcher rather than found in nature. Asking a patient to choose between five labelled boxes produces ordinal data. Asking the same patient to mark a point on a line produces something closer to interval data, because the line supplies equal spacing. The same underlying opinion can therefore be recorded on two different scales, and the choice of instrument decides which averages are lawful. This is why the classification should be recorded alongside the data rather than reconstructed afterwards from the numbers.

A third limit is that the ladder of scales is a model, and models are approximations. A careful researcher may treat a long ordinal scale as approximately interval, but only when there is evidence that respondents treat the steps as equal, and only with the median reported alongside the mean so that a sceptical reader still has an admissible summary.

### 5.2 Beginner misconceptions to unlearn

- **"It has numbers, so it is quantitative."** The digits in a code are labels. Ask whether the value could be renamed without loss. If it could, the variable is categorical no matter how numerical it looks.
- **"It has decimals, so it is continuous."** A count can be written as $3.0$ and a price can be written as $2.50$, and neither fact makes the variable continuous. Continuity is about whether values in between are possible.
- **"It is in whole numbers, so it is discrete."** Age in whole years, shoe size in whole numbers, and height in whole centimetres are all continuous quantities recorded coarsely. Test the variable, not the printout.
- **"Ordinal means I can average."** Order allows ranking, not adding. Averaging ordered labels assumes the steps are equal, and that assumption is exactly what an ordinal scale refuses to make.
- **"The mean is always the best average."** The mean is the best average only when equal spacing is available and when the distribution is not badly distorted by extreme values. For categories it is not merely inferior; it is meaningless.
- **"The median is always safe, so the mean must be too."** The median is safe on every scale from ordinal upwards because it only reads position. The mean reads magnitude, and magnitude is a stronger requirement.
- **"A zero means none."** Zero degrees Celsius does not mean no heat, and the year zero does not mean no time. A true zero is a physical fact about the quantity, not a symbol on the instrument.
- **"Percentages are always fine because they are just proportions."** Proportions are fine for categorical data, but the denominator must match the question. Dividing by the grand total when the question is about boarders produces a true number that answers the wrong question.

### 5.3 Errors that arise when a scale is misidentified

A misidentified scale produces errors that look like arithmetic mistakes but are really errors of meaning. Treating nominal codes as numbers allows a mean to be computed that changes when the code key is changed. Treating ordinal ratings as interval permits a mean that depends on the arbitrary spacing of the labels, and it also permits a standard deviation that describes the coding rather than the opinions. Treating interval data as ratio invites statements such as "twice as hot", which cannot be defended because the zero was chosen by convention.

The errors propagate. A mean computed from ordinal codes enters a report, the report is compared with another report that used different codes, and the comparison suggests a change in opinion that never occurred. Because the original number was arithmetically correct, the mistake is invisible to everyone who checks the sums, and it can only be caught by someone who asks what the numbers were allowed to represent.

The remedy is procedural rather than arithmetical. Classify the variable before computing anything, write the classification down beside the table, and check that every summary reported belongs to the rung of the ladder that the classification names.

### 5.4 Where the idea leads next

Once data are classified, they can be organised, and organising is the doorway to the rest of the subject. Discrete data become discrete frequency distributions, continuous data become grouped frequency distributions with classes, boundaries, widths, and class marks, and two categorical variables become contingency tables. From those organised forms come the summaries: means, medians, modes, standard deviations, and indices of spread. Later in the course the same classification decides which test is used, because a test of a mean and a test of a proportion are different instruments for different kinds of recorded value.

The habit worth carrying forward is the one this topic installs: before any calculation, ask what kind of value is in front of you, and let the answer choose the calculation.
