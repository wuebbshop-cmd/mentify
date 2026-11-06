## 1. Foundational Concepts, Definitions, and Axioms

### 1.1 An everyday picture of the whole subject

Imagine a market trader who keeps a notebook of every sale she makes in one morning. By noon the notebook holds a long column of figures. On its own that column is useless: nobody can see at a glance whether the morning went well. So she sits down and does five things with her figures. She gathers them from the notebook, which is collecting. She sorts them into groups, such as sales below ten shillings and sales between ten and fifty shillings, which is organizing. She writes the groups on a card and hangs the card on her stall, which is presenting. She works out the average sale and the largest sale, which is analyzing. She then says "mornings are quiet and afternoons are busy", which is interpreting.

That sequence of five actions is exactly what is meant by the word statistics. The subject is not a heap of formulas; it is a careful, repeatable way of handling data so that a decision can be defended in front of somebody who disagrees with you. Everything else in the topic is an elaboration of one of those five actions, or of the second half of the topic, which is probability. Probability asks a different kind of question: not "what do my figures show?" but "how likely is it that something will happen?". The two halves fit together, because every honest claim about a group larger than the one you measured has to be stated with a probability attached to it.

### 1.2 Statistics is five jobs done to data

Here is the working definition, written out in full because every word of it earns credit in an examination.

> **Definition (Statistics).** Statistics is the science of collecting, organizing, presenting, analyzing, and interpreting data in order to support decisions.

The definition names five jobs. It is worth seeing each job separately, because questions often describe an activity and ask which job it belongs to.

- **Collecting** means going out and obtaining the raw observations. Writing down the number of children in each household, reading a thermometer every hour, or asking shoppers a question are all collecting.
- **Organizing** means putting the raw observations into a shape where they can be read. Counting how often each value repeats, and writing those counts in a table, is organizing.
- **Presenting** means showing the organized data so that a human eye can take it in. A table, a bar chart, a histogram, or a pie chart is a presentation.
- **Analyzing** means computing summaries: an average, a spread, a percentage, a comparison between two groups.
- **Interpreting** means saying what the summaries mean for the real situation, including what they do not mean.

| Job | What it means in plain words | Example from the market stall |
|---|---|---|
| Collecting | Writing down each observation as it happens | Recording the value of every sale |
| Organizing | Counting how often each value or group occurs | Sorting sales into low, medium, and high |
| Presenting | Showing the counts so they can be read quickly | Writing the three groups on a hanging card |
| Analyzing | Computing a summary number | Average sale, largest sale, total takings |
| Interpreting | Explaining the summary in context | "Mornings are quieter than afternoons" |

A trap to notice immediately: organizing and presenting are different jobs, even though they usually happen one after the other. A frequency table organizes the data, because it does the counting. The same table, hung on a wall, also presents it, because it displays the result. When a question asks which job is being described, look for the verb in the sentence: counting, sorting, and grouping point to organizing, while drawing, displaying, and charting point to presenting.

### 1.3 Two kinds of statistical work: describing and inferring

Statistics is divided into two branches whose difference is one of intention, not of technique.

> **Definition (Descriptive statistics).** Descriptive statistics uses numerical and graphical methods to look for patterns in a data set, and to present that information in a convenient form.

> **Definition (Inferential statistics).** Inferential statistics uses sample data to make estimates, decisions, predictions, or other generalizations about a larger set of data.

Think of a coffee farmer with twenty coffee bushes in one row. If he weighs the cherries from all twenty bushes and reports "the twenty bushes in my row produced an average of nine kilograms each", he has described exactly what he measured. Nothing has been claimed about any other bush anywhere. That is descriptive work. If instead he weighs the cherries from five bushes and then says "the whole plantation of two hundred bushes probably averages about nine kilograms per bush", he has gone beyond his measurements. That is inferential work, and the verb "probably" is the giveaway.

The distinction matters because the two branches carry different risks. A descriptive statement can still be arithmetic-wrong, but it cannot be wrong about a group it never mentioned. An inferential statement can be wrong even when every calculation is perfect, because the five bushes he happened to choose may not resemble the other one hundred and ninety-five. This is why inference always travels with a measure of reliability.

A useful way to remember the difference is to ask what the sentence is about. If the sentence is about the numbers actually in front of you, it is descriptive. If the sentence is about a group you did not fully measure, it is inferential.

### 1.4 The five words every question uses

Five elements recur throughout the topic. Learn them as a chain rather than as five separate definitions, because the chain is what the questions test.

> **Definition (Population).** A population is the set of all units, usually people, objects, transactions, or events, that we are interested in studying.

> **Definition (Variable).** A variable is a characteristic or property of an individual population unit.

> **Definition (Sample).** A sample is a subset of the units of a population.

> **Definition (Statistical inference).** A statistical inference is an estimate, prediction, or other generalization about a population based on information contained in a sample.

> **Definition (Measure of reliability).** A measure of reliability is a statement, attached to a statistical inference, that says how much confidence the inference deserves.

Here is the chain in one small story. A head teacher wants to know the average amount of pocket money carried by the two hundred learners in her school. The two hundred learners are the population. The amount of pocket money is the variable, because each learner has a value of it. She cannot question two hundred learners in one afternoon, so she asks ten of them, and those ten are the sample. When she says "the average for the whole school is about four hundred shillings", that sentence is the statistical inference. When she adds "give or take one hundred shillings", that addition is the measure of reliability.

Two subtleties are worth stating plainly at the start. First, a population is defined by the question, not by its size. The population in the story is two hundred learners because the question is about that school; a different question about all schools in the district would have a different population and a different sample. Second, the measure of reliability is not decoration. Without it, an inference is only an opinion wearing a number. The words that usually carry it are "with ninety-five per cent confidence", "plus or minus", "give or take", or "there is about a one in twenty chance of being wrong".

### 1.5 The types of data

Data are of two broad types, and the type decides which summaries and which pictures are legitimate.

> **Definition (Quantitative data).** Quantitative data are measurements recorded on a naturally occurring numerical scale.

> **Definition (Qualitative data).** Qualitative data are measurements that cannot be placed on a natural numerical scale and can only be classified into one of a group of categories.

The number of children in a family is quantitative, because counting produces a genuine number and the difference between two and three children means something. Eye colour is qualitative, because the values are names. A code number given to eye colour, such as brown equals one and blue equals two, does not turn it into quantitative data; the number is a label that happens to be written with a digit. This is one of the most common beginner errors in the whole topic.

Within each broad type there is a finer classification into four measurement scales. The scale tells you which arithmetic is meaningful.

- **Nominal** data are qualitative values that differ only by name. Sex, religion, and blood group are nominal. Counting them is meaningful; averaging them is not.
- **Ordinal** data are qualitative values that carry a genuine order but no genuine distance. Examination grades, army ranks, and satisfaction ratings from poor to excellent are ordinal. You may say that a credit is better than a pass, but you may not say that the gap from pass to credit equals the gap from credit to distinction.
- **Interval** data are quantitative values with equal distances but an arbitrary zero. Temperature in degrees Celsius is the standard example: the step from ten to twenty degrees is the same size as the step from twenty to thirty, but zero degrees does not mean "no heat".
- **Ratio** data are quantitative values with equal distances and a true zero, so that ratios make sense. Mass, height, income, and time are ratio measurements. A mass of twenty kilograms really is twice a mass of ten kilograms.

| Scale | Type | Example | Meaningful arithmetic |
|---|---|---|---|
| Nominal | Qualitative | Blood group | Counting only |
| Ordinal | Qualitative | Grade A to E | Counting and ordering |
| Interval | Quantitative | Temperature in Celsius | Counting, ordering, adding |
| Ratio | Quantitative | Mass in kilograms | All four operations including ratios |

A second division cuts across the quantitative side. **Discrete** data take separate, countable values, usually whole numbers, such as the number of children in a family. **Continuous** data can take any value in an interval, limited only by how finely you can measure, such as mass or height. The division matters when you present the data: discrete counts are naturally tabulated value by value, while continuous measurements must be grouped into classes.

### 1.6 Where the data come from

Data can be obtained in four ways, and the route matters because it limits what may be concluded afterwards.

- **From a published source.** Figures already gathered by somebody else, such as a statistical abstract, a company report, or a hospital register. This is quick and cheap, but the question you can answer is limited to the questions somebody else asked, and you inherit whatever errors they made.
- **From a designed experiment.** The investigator deliberately sets the conditions and decides who or what receives each treatment. Because the assignment is under control, only a designed experiment can support a statement that one thing caused another.
- **From a survey.** The investigator asks questions of a chosen group of units. Surveys are efficient for opinions, habits, and facts that people can report about themselves, but they are vulnerable to people giving the answer they think is expected.
- **From observation.** The investigator watches and records without interfering. This captures behaviour as it really happens, but uncontrolled factors can move together, so a pattern seen this way usually cannot be called a cause.

The distinction between the second route and the last two is the one examiners press hardest. If a study finds that learners who eat breakfast score higher, the finding may be an association only, because learners who eat breakfast may also sleep better, or come from wealthier homes. If the investigator instead assigns breakfast to one randomly chosen half of a group and withholds it from the other half, the difference in scores can be attributed to the breakfast. That single sentence, that control of assignment is what licenses a causal claim, is worth remembering.

### 1.7 How data are presented: the frequency table family

Raw data are hard to read. A **frequency distribution** is a table in which the data are grouped into classes and the number of cases falling in each class is recorded; that count is called the **frequency**.

When the variable is discrete and takes few values, every distinct value is listed with its tally and frequency, and the result is a **discrete frequency distribution**. When the variable is continuous, or when a discrete variable takes many values, the values are gathered into classes, and the result is a **grouped frequency distribution**.

Grouped data bring their own vocabulary, and each word has a precise meaning.

- A **class interval** is the symbol that defines a class, written as a pair of numbers such as forty to forty-nine.
- The two numbers in the symbol are the **class limits**: the left one is the **lower class limit** and the right one the **upper class limit**.
- A **class boundary** is the true dividing line between one class and the next. It sits half a unit beyond each limit, so the classes forty to forty-nine and fifty to fifty-nine are separated by the boundary at forty-nine point five. Boundaries are also called true class limits.
- The **class width**, also called the class size, is the difference between the upper and the lower boundary of a class. For the class forty to forty-nine the width is ten, whether it is measured as forty-nine point five minus thirty-nine point five or as fifty-nine point five minus forty-nine point five.
- The **class mark** is the midpoint of the class, computed as the average of its two boundaries. For the class forty to forty-nine the class mark is forty-four point five.
- The **cumulative frequency** up to a given class is the total of all frequencies at or below that class.
- The **relative frequency** of a class is its frequency divided by the total number of observations, so it is a proportion between zero and one.

Here is a small grouped table of the masses of twenty parcels, with all of those quantities worked out.

| Mass (kilograms) | Frequency | Class mark | Cumulative frequency | Relative frequency |
|---|---|---|---|---|
| 40 to 49 | 4 | 44.5 | 4 | 0.20 |
| 50 to 59 | 9 | 54.5 | 13 | 0.45 |
| 60 to 69 | 7 | 64.5 | 20 | 0.35 |
| Total | 20 | not applicable | 20 | 1.00 |

Reading across one row is a complete exercise in the vocabulary. The second row's class interval is fifty to fifty-nine, its limits are fifty and fifty-nine, its boundaries are forty-nine point five and fifty-nine point five, its width is ten, its mark is fifty-four point five, nine parcels fall in it, thirteen parcels fall at or below it, and nine parcels out of twenty is a relative frequency of zero point four five.

Three standard pictures are built directly on such a table, and each one is described here in words rather than drawn. A **histogram** is a set of rectangles standing side by side on the class boundaries, each rectangle's height equal to the frequency of its class, so the total area of the rectangles represents all the observations. A **frequency polygon** joins the midpoints of the tops of those rectangles, plotting frequency against class mark, and it is useful when two distributions must be compared because two polygons can be drawn on one pair of axes without the rectangles hiding each other. A **cumulative frequency curve**, often called an ogive, plots the cumulative frequency against the upper class boundary and always rises, never falls.

### 1.8 Probability: measuring uncertainty

Probability is the study of uncertainty and of the likelihood of events. Its vocabulary is small but must be exact.

- An **experiment** is any process whose outcome cannot be predicted with certainty in advance. Rolling a die and choosing a learner at random are experiments.
- The **sample space**, written with a capital S, is the set of all possible outcomes. For a single die it holds six outcomes: one, two, three, four, five, six.
- An **event** is a subset of the sample space. "The die shows an even number" is the event containing three outcomes: two, four, and six.
- An event **occurs** when the outcome of the experiment is one of the outcomes inside it.
- Two events are **mutually exclusive** when they have no outcome in common, so they cannot both happen on the same run. "The die shows two" and "the die shows five" are mutually exclusive.
- Events are **exhaustive** when together they cover the whole sample space, so at least one of them must happen.
- Outcomes are **equally likely** when the model gives each of them the same chance. A fair coin and a fair die are the standard examples.

When the outcomes of an experiment are equally likely and the sample space is finite, the probability of an event is the number of outcomes inside the event divided by the number of outcomes in the whole sample space.

$$
P(A) = \frac{\text{number of outcomes in } A}{\text{number of outcomes in } S}
$$

In that expression the letter A stands for the event, the letter S stands for the sample space, the two vertical bars around a set mean "the number of outcomes in", and the whole symbol on the left is read "the probability of A". For a fair die, the probability of an even number is three outcomes out of six, which is one half.

### 1.9 The three axioms of probability

Everything else in probability is deduced from three starting statements, called axioms, which are accepted without proof. They are stated for a sample space S and events inside it.

> **Axiom 1 (Non-negativity).** The probability of any event is never negative, so the probability of A is greater than or equal to zero.

> **Axiom 2 (Normalisation).** The probability of the whole sample space is one, so the probability of S equals one.

> **Axiom 3 (Additivity).** If two or more events are mutually exclusive, the probability that one of them occurs is the sum of their separate probabilities.

Read in plain words, the three axioms say that a probability is a number that cannot be negative, that the certain event has probability one, and that probabilities of separate possibilities add up. Nothing else is assumed. In particular, the rule that the probability of an event not happening is one minus the probability that it does happen is not an axiom; it is a consequence, and it is proved in Section 3. The addition law for two events that overlap is a consequence as well.

### 1.10 Putting the vocabulary together

The whole of Section 1 can be held in the mind as a single chain. A question is asked about a population. A variable is chosen as the characteristic to be measured, and its scale is checked so that the right arithmetic is used. A sample is selected, and data are collected by one of the four routes. The observations are organized into a frequency distribution, presented as a table or a picture, and analyzed into summaries. If the summaries are used only for the sample, the work is descriptive. If they are used to speak about the population, the work is inferential, and the inference must carry a measure of reliability, which is itself a probability statement. Probability therefore supplies both the language of uncertainty and the machinery that makes an honest inference possible.

## 2. Theorems, Lemmas, and Analytical Properties

The results in this section are the tools used in every later calculation. Each is stated plainly, then explained in words, because a formula that is remembered without its meaning is easily misapplied.

### 2.1 Facts about the summation sign

The capital Greek letter sigma, written as a large S-like symbol, is an instruction to add. If a variable has observations labelled from the first to the n-th, then the sum of all the observations is written with the sigma sign and an index below and above it.

$$
\sum_{i=1}^{n} x_i = x_1 + x_2 + \cdots + x_n
$$

The letter i below the sigma is a counter that starts at one, the letter n above it is where the counting stops, and each x with a subscript is one observation. Two facts about this instruction are used constantly.

> **Lemma (Adding a constant many times).** If the same number is added n times, the result is that number multiplied by n.

> **Lemma (Splitting and scaling a sum).** A sum of terms that each contain a constant multiplier can be split, with the constant pulled outside the sigma sign.

In words, the second lemma says that doubling every observation doubles the total, and that the total of two lists added value by value equals the total of the first list plus the total of the second. These two facts are what allow every clever shortcut in the topic, including the coded method for computing a mean from grouped data.

### 2.2 Facts about the arithmetic mean

The mean of n observations is the total divided by the count.

$$
\bar{x} = \frac{1}{n}\sum_{i=1}^{n} x_i
$$

The symbol with a bar over it is read "x bar" and denotes the mean of the sample. Three properties follow at once.

> **Property (Deviations cancel).** The deviations of the observations from their own mean add up to zero.

> **Property (Shifting all values).** If the same number is subtracted from every observation, the mean falls by exactly that number, so the mean can be recovered by adding it back.

> **Property (Weighted mean).** When values repeat, the mean of all the observations equals the sum of each value multiplied by its frequency, divided by the total frequency.

The first property says the mean is a balance point: the observations above it pull up exactly as hard as the observations below it pull down. The second property is the reason a long list of large numbers can be reduced to a short list of small ones without changing the answer. The third property is the reason a frequency table is enough to compute a mean; the individual observations do not have to be kept.

### 2.3 Facts about frequency tables

> **Property (Total of the frequencies).** The frequencies of all the classes add up to the total number of observations.

> **Property (Relative frequencies add to one).** The relative frequencies of all the classes add up to exactly one.

> **Property (Cumulative frequencies never fall).** The cumulative frequency of a class is at least as large as the cumulative frequency of the class before it, and the last cumulative frequency equals the total number of observations.

These three properties are free checks. Any table in which the frequencies do not add to the stated total, or in which the relative frequencies do not add to one, contains a counting error somewhere, and no amount of later arithmetic will repair it.

### 2.4 Facts about class intervals

> **Property (Constant width).** In a well-constructed grouped table the classes all have the same width, so the boundaries advance by a fixed step from one class to the next.

> **Property (Marks in step).** When the widths are equal, the class marks also advance by a fixed step, and the step equals the class width.

> **Property (Mark from boundaries).** The class mark is the average of the two boundaries of its class, not the average of the two limits, although the two averages coincide whenever the gap between adjacent limits is one unit.

The reason for insisting on boundaries is that the limits of one class and the limits of the next leave a gap. In the classes forty to forty-nine and fifty to fifty-nine there is no observation possible between forty-nine and fifty if the variable is recorded in whole numbers, but the underlying variable is continuous, so the true dividing line has to be placed halfway across the gap. Every calculation that uses a boundary inherits the accuracy of that placement.

### 2.5 Facts about probability

> **Theorem (Probability of the empty event).** An event that contains no outcomes has probability zero.

> **Theorem (Complement rule).** For any event A, the probability that A does not occur is one minus the probability that it does occur.

> **Theorem (Monotonicity).** If every outcome of an event A is also an outcome of an event B, then the probability of A is at most the probability of B.

> **Theorem (Addition law for two events).** For any two events A and B, the probability that at least one of them occurs equals the sum of their separate probabilities minus the probability that both occur.

> **Theorem (Addition law for three events).** For any three events, the probability that at least one occurs equals the sum of the three separate probabilities, minus the three pairwise joint probabilities, plus the probability that all three occur together.

> **Theorem (Boole's inequality).** For any collection of events, the probability that at least one of them occurs is at most the sum of their separate probabilities.

The subtraction in the addition law repairs a double count. If a learner is counted once as a mathematics student and once as a physics student, then adding the two headline figures counts the learners who take both subjects twice. Subtracting the number who take both restores the correct total. The addition in the three-event law repairs a triple count in the same spirit: the three pairwise subtractions each remove the centre region once too often, so the centre is added back at the end.

### 2.6 Facts about inference and reliability

> **Property (Sampling error cannot be removed by arithmetic).** A summary computed from a sample differs from the corresponding summary of the population in a way that no formula applied to the sample alone can detect.

> **Property (Reliability shrinks with the sample).** Other things being equal, a larger sample supports a narrower interval of plausible values for the population summary.

> **Property (Bias is not the same as imprecision).** A sample can be large and still systematically unrepresentative, in which case the reliability statement describes a precisely wrong answer.

These three properties explain why the topic begins with vocabulary and only later becomes computational. A number computed from a badly chosen sample is not repaired by being computed carefully.

### 2.7 A summary of the key formulas in words

For quick reference, here is the whole toolkit stated in ordinary language, with no symbols at all. The mean of a list is the total divided by the count. The mean of a frequency table is each value times its frequency, added, divided by the total frequency. The class width is the upper boundary minus the lower boundary. The class mark is the average of the two boundaries. A relative frequency is a class frequency divided by the total. A cumulative frequency is a running total of the class frequencies. The probability of an event with equally likely outcomes is its number of outcomes divided by the total number of outcomes. The probability of a complement is one minus the probability of the event. The probability of a union is the sum of the two probabilities minus the probability of the intersection. Every one of those sentences is proved or derived in Section 3, and every one of them is used in Section 4.

## 3. Formal Proofs, Derivations, and Methods

This section shows where the standard results come from, using the smallest possible numbers. Nothing here is a new idea; every step is an application of the definitions in Section 1 and the properties in Section 2.

### 3.1 Why the deviations from the mean always cancel

Take three observations: two, four, and nine. Their total is fifteen and their count is three, so their mean is five. Now compare each observation with the mean, subtracting the mean from the observation to get what is called a deviation.

- The deviation of two from five is minus three, because two is three below the mean.
- The deviation of four from five is minus one.
- The deviation of nine from five is plus four.

Written with the sigma sign, the sum of those deviations is as follows.

$$
\sum_{i=1}^{3}\left(x_i - \bar{x}\right) = (2 - 5) + (4 - 5) + (9 - 5) = -3 - 1 + 4 = 0
$$

The sum is zero because of the way the mean was defined. The mean takes the total of fifteen and shares it equally among the three observations, so the amount by which the small observations fall short of the mean must exactly equal the amount by which the large observations exceed it. In general, if every deviation is added, the total is the total of the observations minus three copies of the mean, and three copies of the mean is exactly the total of the observations. The two quantities cancel.

This is why a check on any computed mean is available for free. Subtract the mean from each observation, add the results, and if the sum is not zero then either the mean or the arithmetic is wrong.

### 3.2 Why a frequency table gives the same mean as the raw list

Suppose the raw list is one, one, two, one, two. There are five observations and their total is seven, so the mean is one point four. Now count how often each value repeats: the value one appears three times and the value two appears twice. Instead of adding the list term by term, add each value as many times as it appears.

$$
\bar{x} = \frac{1(3) + 2(2)}{3 + 2} = \frac{3 + 4}{5} = 1.4
$$

The two answers agree because multiplication is only repeated addition. Three copies of one is the same quantity as one plus one plus one, so grouping the repetitions cannot change the total. The frequency column is therefore not a different method; it is the same method with the repeated additions already done. The only thing lost when the table is built is the identity of the individual observations, which is exactly the information a mean does not need.

### 3.3 How the class width and the class mark are obtained

The method for both quantities is short, but the order of the steps matters because the class mark depends on the boundaries rather than on the limits.

1. Write down the class interval exactly as it appears in the table, for example forty to forty-nine.
2. Find the lower boundary by subtracting half the gap between adjacent classes from the lower limit. When the limits are whole numbers and consecutive classes are separated by a gap of one, half the gap is one half, so the lower boundary is thirty-nine point five.
3. Find the upper boundary the same way, by adding one half to the upper limit, giving forty-nine point five.
4. Subtract the lower boundary from the upper boundary to obtain the class width, which is ten in this example.
5. Add the two boundaries and halve the result to obtain the class mark, which is forty-four point five.

The fifth step is the one beginners most often skip. The class mark is not the midpoint of the two limits; it is the midpoint of the two boundaries. In this example the two midpoints happen to agree because the gap is one unit and the limits are whole numbers, but they disagree whenever the gap is different, and an examiner who chooses a decimal gap will catch the shortcut.

### 3.4 Method for building a grouped frequency table

1. Find the smallest and the largest observation, and subtract the smaller from the larger to obtain the range.
2. Decide how many classes to use. A rough guide is to take the square root of the number of observations and round it, so twenty observations suggest about four or five classes.
3. Divide the range by the number of classes to obtain a trial class width, then round it up to a convenient number such as five, ten, or twenty.
4. Place the lower boundary of the first class at or just below the smallest observation, and generate the remaining classes by adding the width repeatedly.
5. Tally each observation into exactly one class. A value sitting exactly on a boundary goes into the class whose lower boundary it equals.
6. Write the frequency of each class, then add the frequencies and check that the total equals the number of observations.
7. Add the class marks, the cumulative frequencies, and the relative frequencies, and check that the last cumulative frequency equals the total and that the relative frequencies add to one.

Step six is the step that protects everything else. A grouped table whose frequencies do not total correctly is not a slightly wrong table; it is a table with no guarantee at all, because the error may sit in any class.

### 3.5 Deriving the complement rule from the axioms

The complement of an event A is the event that A does not occur, written with a dash after the letter. The derivation needs only the three axioms and one observation about sets.

1. An event and its complement can never occur together, so they are mutually exclusive.
2. Together they cover every possible outcome, so their union is the whole sample space.
3. By the third axiom, the probability of their union is the sum of their separate probabilities, so the probability of A plus the probability of its complement equals the probability of the union.
4. The probability of the union is the probability of the whole sample space, which is one by the second axiom.

Putting those four statements into symbols gives the following.

$$
P(A) + P(A') = P\left(A \cup A'\right) = P(S) = 1
$$

Rearranging the left equality gives the complement rule.

$$
P(A') = 1 - P(A)
$$

The rule is a deduction, not an extra assumption. It also explains why a probability can never exceed one: if the probability of A were greater than one, the probability of its complement would be negative, which the first axiom forbids.

### 3.6 Deriving the addition law for two events

The addition law is needed whenever two events can overlap. The derivation splits the union into two parts that do not overlap.

1. The event "A or B occurs" contains everything in A, plus everything in B that is not already in A. Those two pieces are mutually exclusive by construction.
2. Apply the third axiom to those two pieces, so the probability of the union is the probability of A plus the probability of the part of B outside A.
3. Now split B in the same way, into the part inside A and the part outside A. Those two pieces are also mutually exclusive, so the probability of B equals the probability of the overlap plus the probability of the part outside A.
4. Rearrange the third step to express the probability of the part of B outside A as the probability of B minus the probability of the overlap.
5. Substitute that expression into the second step.

The result is the addition law.

$$
P(A \cup B) = P(A) + P(B) - P(A \cap B)
$$

The symbol shaped like a cup means "or", the symbol shaped like an upside-down cup means "and", so the law reads: the probability of A or B equals the probability of A plus the probability of B minus the probability of A and B. The subtraction exists because the overlap was counted in both of the first two terms.

### 3.7 Method for computing a probability by counting

1. Write the experiment in one sentence, and decide what a single outcome of it looks like.
2. List the sample space, or at least count its outcomes, and check that every outcome really is equally likely.
3. Write the event of interest as a set of outcomes, or describe it precisely in words.
4. Count the outcomes in the event, and divide by the number of outcomes in the sample space.
5. Check the answer against the axioms: it must lie between zero and one, and it must be sensible in the situation.
6. If the event is described by a negation, such as "not a six" or "at least one", compute the probability of the opposite event and subtract from one.

Step six is a strategy rather than a rule, but it saves a great deal of counting. The event "at least one head in three tosses" contains seven of the eight possible outcomes, while its opposite, "no heads at all", contains only one, so the complement route is far shorter.

### 3.8 From relative frequency to probability

The classical formula in Section 1.8 needs equally likely outcomes, which a real data set rarely provides. A second route to probability uses observed data. Toss a drawing pin two hundred times and suppose it lands point up one hundred and four times. The relative frequency of landing point up is then the following.

$$
\frac{104}{200} = 0.52
$$

This number is an estimate of the probability, not the probability itself, because a different two hundred tosses would give a slightly different value. What makes the estimate respectable is that the relative frequency settles down as the number of repetitions grows: the wobble between successive estimates shrinks even though it never disappears. That stability is the empirical foundation of the whole subject, and it is the bridge between the descriptive half of the topic, which reports what happened, and the probability half, which models what is likely.

## 4. Representative Worked Examples and Solutions

Every example below is worked as a numbered sequence of steps. Read each step as an instruction that could be repeated on a different set of numbers.

### 4.1 Problem: the mean of five observations

Find the arithmetic mean of the observations four, eight, ten, twelve, and sixteen.

### 4.2 Solution: add, count, divide, then check

Step 1. Add the observations using the sigma sign, where the counter runs from one to five.

$$
\sum_{i=1}^{5} x_i = 4 + 8 + 10 + 12 + 16 = 50
$$

Step 2. Count the observations, which gives five.

Step 3. Divide the total by the count.

$$
\bar{x} = \frac{50}{5} = 10
$$

Step 4. Check with the deviation property. The deviations from ten are minus six, minus two, zero, plus two, and plus six, and their sum is zero, so the answer is consistent.

Step 5. Say what the answer means. Each observation replaced by the single value ten would leave the total unchanged, which is the sense in which the mean summarises the list.

### 4.3 Problem: a discrete frequency table from raw counts

Twenty learners were asked how many textbooks they own. Their answers were one, three, two, two, zero, four, one, two, five, three, two, one, four, two, zero, three, two, one, four, and two. Present the data as a frequency distribution.

### 4.4 Solution: tally each value once, then total

Step 1. Find the range of values. The smallest is zero and the largest is five, so the table must run from zero to five inclusive.

Step 2. Count the occurrences of each value, reading the list once from left to right. Zero occurs twice, one occurs four times, two occurs seven times, three occurs three times, four occurs three times, and five occurs once.

Step 3. Write the counts as a table, and add the relative frequency column, which is each count divided by twenty.

| Textbooks owned | Frequency | Relative frequency |
|---|---|---|
| 0 | 2 | 0.10 |
| 1 | 4 | 0.20 |
| 2 | 7 | 0.35 |
| 3 | 3 | 0.15 |
| 4 | 3 | 0.15 |
| 5 | 1 | 0.05 |
| Total | 20 | 1.00 |

Step 4. Check the totals. The frequencies add to twenty, which matches the twenty learners, and the relative frequencies add to one point zero zero, so no learner has been lost or double counted.

Step 5. Interpret the table in one sentence. The most common answer is two textbooks, chosen by seven learners out of twenty, which is thirty-five per cent of the group.

### 4.5 Problem: turning a grouped table into its full vocabulary

Sixteen parcels have masses recorded in the classes one to five, six to ten, eleven to fifteen, and sixteen to twenty kilograms, with frequencies three, six, five, and two. Find the class boundaries, the class width, the class marks, the cumulative frequencies, and the relative frequencies.

### 4.6 Solution: boundaries first, everything else afterwards

Step 1. Note that consecutive limits differ by one, so half of that gap is one half, and each boundary lies one half beyond its limit. The boundaries are therefore zero point five, five point five, ten point five, fifteen point five, and twenty point five.

Step 2. Subtract the lower boundary from the upper boundary of any class to obtain the width. For the first class the calculation is five point five minus zero point five, which gives five, and the same figure is obtained from every other class, so the widths are equal.

Step 3. Average the two boundaries of each class to obtain the class marks, which are three, eight, thirteen, and eighteen.

Step 4. Accumulate the frequencies: three, then three plus six equals nine, then nine plus five equals fourteen, then fourteen plus two equals sixteen.

Step 5. Divide each frequency by sixteen to obtain the relative frequencies zero point one eight seven five, zero point three seven five, zero point three one two five, and zero point one two five.

Step 6. Check that the last cumulative frequency equals sixteen and that the four relative frequencies add to one. Both checks pass, so the table is internally consistent.

### 4.7 Problem: the mean of grouped data

Using the sixteen parcels of the previous example, compute the mean mass.

### 4.8 Solution: treat each class mark as the class representative

Step 1. Record the class marks found earlier, which are three, eight, thirteen, and eighteen, together with the frequencies three, six, five, and two.

Step 2. Multiply each class mark by its frequency and add the products.

$$
\sum_{j=1}^{4} f_j m_j = 3(3) + 6(8) + 5(13) + 2(18) = 9 + 48 + 65 + 36 = 158
$$

In that expression the letter f with a subscript stands for a class frequency, the letter m with a subscript stands for a class mark, and the sigma sign adds the four products.

Step 3. Divide by the total frequency, which is sixteen.

$$
\bar{x} = \frac{158}{16} = 9.875
$$

Step 4. Round sensibly and state the qualification. The mean is about nine point nine kilograms, and it is an approximation because every parcel in a class was treated as if it had exactly the mass of the class mark.

Step 5. Bound the possible error. Half a class width is two point five kilograms, so the true mean could differ from the computed mean by at most that much, which is why the result should be quoted as roughly ten kilograms rather than as nine point eight seven five exactly.

### 4.9 Problem: a probability from a bag of numbered balls

A bag contains ten balls numbered one to ten, and one ball is drawn at random. Find the probability that the number drawn is greater than seven.

### 4.10 Solution: count the sample space, then count the event

Step 1. Identify the experiment, which is drawing one ball, and the sample space, which is the ten numbers one to ten.

Step 2. Write the event of interest as the set of numbers eight, nine, and ten, and note that it contains three outcomes.

Step 3. Divide the size of the event by the size of the sample space.

$$
P(\text{greater than seven}) = \frac{3}{10} = 0.3
$$

Step 4. Check against the axioms. The answer lies between zero and one, and it agrees with intuition, since three of the ten equally likely numbers qualify.

### 4.11 Problem: an addition law where the events overlap

The same bag of ten balls is used. Let A be the event that the number drawn is even, and let B be the event that the number is a multiple of three. Find the probability that the number is even or a multiple of three.

### 4.12 Solution: subtract the overlap once

Step 1. List the even numbers, which are two, four, six, eight, and ten, so the probability of A is five tenths.

Step 2. List the multiples of three, which are three, six, and nine, so the probability of B is three tenths.

Step 3. Identify the overlap, which is the number six alone, so the probability of both events is one tenth.

Step 4. Apply the addition law.

$$
P(A \cup B) = \frac{5}{10} + \frac{3}{10} - \frac{1}{10} = \frac{7}{10}
$$

Step 5. Verify by direct counting. The numbers that qualify are two, three, four, six, eight, nine, and ten, which is seven numbers out of ten, in agreement with the law. Adding five tenths and three tenths without the subtraction would have produced eight tenths, which overcounts the number six.

### 4.13 Problem: naming the elements of a small study

A shopkeeper wants to know the average amount spent per customer on a Saturday. She records the amounts spent by eight of her forty customers, obtains an average of four hundred and fifty shillings, and reports that the Saturday average for all her customers is between three hundred and eighty and five hundred and twenty shillings, with ninety per cent confidence. Identify the population, the variable, the sample, the inference, and the measure of reliability, and say whether the work is descriptive or inferential.

### 4.14 Solution: match each phrase to a definition

Step 1. The population is the set of all forty customers who shopped on that Saturday, because the question is about them.

Step 2. The variable is the amount spent, which is quantitative and measured on a ratio scale, because zero spending means no money spent and doubling an amount doubles the quantity.

Step 3. The sample is the eight customers whose amounts were recorded.

Step 4. The inference is the claim that the Saturday average for all forty customers lies between three hundred and eighty and five hundred and twenty shillings. The figure of four hundred and fifty shillings on its own is a descriptive summary of the eight customers.

Step 5. The measure of reliability is the phrase "with ninety per cent confidence", which states how often a procedure of this kind gives an interval that contains the true average.

Step 6. Classify the work. Computing the average of the eight amounts is descriptive; the interval quoted for all forty customers is inferential, so the study as a whole is an example of inferential statistics built on a descriptive summary.

## 5. Mathematical Extensions, Limits, and Common Errors

### 5.1 What an average does not tell you

An average is a single number standing in for a whole list, and a single number cannot carry the whole story. Consider two small groups of five learners whose weekly pocket money in hundreds of shillings is recorded. The first group has amounts two, three, four, five, and six. The second group has amounts zero, one, four, seven, and eight. Both totals are twenty, so both means are four, yet the groups are not alike at all: in the first the amounts sit close together, while in the second they are spread from nothing to eight.

The mean cannot distinguish those cases, and it is also not resistant, which means a single extreme observation can move it a long way. Add one learner with forty to the second group and the mean of six learners rises to ten, even though five of the six learners have less than ten. Whenever a distribution is strongly lopsided, the median, which is the middle value when the observations are put in order, describes a typical member better than the mean does. The lesson is not that the mean is bad, but that a mean quoted without any measure of spread is an incomplete summary.

### 5.2 A grouped mean is always an approximation

When observations are replaced by class marks, all the variation inside a class is thrown away. The size of the resulting error is bounded: because every observation in a class lies within half a class width of the class mark, the grouped mean differs from the true mean by at most half a class width. In the parcel example the class width was five kilograms, so the computed mean of nine point eight seven five could be out by two and a half kilograms in the worst case. That bound is worth more than the extra decimal places: it tells a reader exactly how much trust the number deserves.

The bound also shows what to do about it. Halving the class width halves the maximum error, so a table with many narrow classes gives a grouped mean closer to the true mean than a table with a few wide classes. The price is a longer table and more classes with small frequencies, which is why the choice of width is a judgement rather than a rule.

### 5.3 A probability computed from data is an estimate

The classical formula needs equally likely outcomes, and real data almost never provide them. When a probability is estimated by relative frequency, the estimate carries a sampling wobble. Two hundred tosses of a drawing pin gave a relative frequency of zero point five two, but four hundred tosses might give zero point four nine. The estimate is still useful because the wobble shrinks as the count grows, and because the estimate is anchored by the axioms: it can never leave the interval from zero to one, and the estimates of a set of mutually exclusive and exhaustive events still add to one.

The practical consequence is that a probability statement about a population should always be read as a statement about a procedure. Saying that a ninety per cent confidence interval contains the true average does not mean that this particular interval certainly does; it means that the procedure, repeated many times, produces intervals that contain the true average in about ninety per cent of cases.

### 5.4 Mutually exclusive is not the same as independent

Two words in this topic are constantly confused, so they are separated here. Two events are mutually exclusive when they cannot both happen on the same run, so the probability of both is zero. Two events are independent when the occurrence of one does not change the probability of the other. Mutually exclusive events with positive probabilities are in fact strongly dependent, because if one has happened then the other certainly has not. On a single roll of a die, showing an odd number and showing an even number are mutually exclusive; showing an odd number and showing a number greater than four are not mutually exclusive, because five satisfies both.

This extension is where the topic leads next. Once independence is available, the probability of two events happening together becomes the product of their separate probabilities when the events are independent, and the multiplication rule replaces the addition law as the main tool. Understanding the distinction now prevents a whole family of later errors.

### 5.5 Beginner misconceptions, and what is true instead

1. **"Statistics is just the study of numbers."** The subject is defined by the five jobs done to data, and by the discipline that keeps those jobs honest. A correct answer names collecting, organizing, presenting, analyzing, and interpreting.
2. **"A sample is a small population."** A sample is a subset drawn from a population. Calling it a small population hides the essential point, which is that a sample is used to say something about a larger group it was drawn from.
3. **"Any number computed from data is an inference."** A sample mean describes the sample. It becomes an inference only when it is used to make a claim about the population, and that claim needs a measure of reliability.
4. **"Qualitative data become quantitative if you code them with numbers."** Assigning the code one to brown eyes and two to blue eyes does not create a numerical scale. Qualitative data stay qualitative until a genuine measured quantity is recorded.
5. **"A higher average always means a better group."** An average says nothing about spread, nothing about the shape of the distribution, and nothing about how the data were collected.
6. **"Class limits and class boundaries are the same thing."** The boundary is the true dividing line, placed halfway across the gap between adjacent limits. Using a limit where a boundary is required shifts every later calculation.
7. **"The class width is the upper limit minus the lower limit."** The width is the upper boundary minus the lower boundary. For the class forty to forty-nine with a one-unit gap, the width is ten and not nine.
8. **"The total row is optional."** The total row is the only check that every observation was counted exactly once. Without it, a tallying error stays hidden until the mean comes out wrong.
9. **"Probabilities can be added freely."** Probabilities may be added directly only when the events are mutually exclusive. Overlapping events need the addition law, with the overlap subtracted once.
10. **"A complement means the opposite outcome of the experiment."** The complement is the set of all outcomes not in the event. Its probability is one minus the probability of the event, which is why it can never be negative.

### 5.6 How to check your own work

Four checks catch most errors in this topic, and each takes seconds. First, check the frequency total against the number of observations. Second, check that the relative frequencies add to one. Third, check that the class marks advance by exactly one class width from class to class. Fourth, check that every computed probability lies between zero and one, and that the probabilities of a set of separate possibilities add to one. A candidate who performs those four checks in an examination will find almost every slip before the invigilator does.

A fifth check is worth adding for written answers. Read the final sentence and ask whether it distinguishes description from inference. If the sentence speaks about the data in hand, it should not carry a confidence phrase; if it speaks about a wider group, it must carry one.

### 5.7 Consolidation

The topic rests on one chain of reasoning. A population is studied through a variable measured on a sample, and the data collected are organized into a frequency distribution whose vocabulary of limits, boundaries, width, marks, and cumulative frequencies makes the table readable and checkable. Summaries such as the mean reduce the table to one number, with a known approximation cost when classes have been used. Probability then supplies the language of uncertainty, built on three axioms from which the complement rule and the addition law follow as deductions. Inference joins the two halves, converting a sample summary into a population claim whose reliability is itself a probability statement. Every later technique in the subject, from sampling designs to confidence intervals and hypothesis tests, is an extension of one of those steps, so a learner who can state the chain accurately and compute the small examples in Section 4 has the foundation the rest of the course assumes.
