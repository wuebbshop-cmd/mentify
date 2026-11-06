## 1. Foundational Concepts, Definitions, and Axioms

### 1.1 A sweet-shop picture of chance

Imagine a glass jar on a counter in a small sweet shop. Inside the jar there are ten wrapped sweets, and the wrappers tell you everything you need to know: six of them are red and four of them are green. The shopkeeper shakes the jar, looks away, and takes out one sweet at random. Nobody in the shop can say which colour will come out. That ordinary moment, a reach into a jar with an uncertain result, is exactly the situation this topic teaches us to measure.

Picture the same moment more carefully and three separate things appear. First there is the action itself, the reaching in. Second there is the complete list of results that could come out, which here is just two entries, red and green. Third there is the part of that list you happen to care about, for example the question "did I get a red sweet?". Probability is nothing more than a careful bookkeeping of these three things, with a number attached to the third one.

Now think about how confident you would feel. If the jar held six red sweets and four green ones, you would expect red more often than green, but you would never be certain. If all ten sweets were red, you would be certain. If none were red, you would know red is impossible. So the strength of a belief about an uncertain result sits somewhere between "impossible" and "certain", and the whole subject is a way of putting that strength on a numbered scale.

The scale runs from zero to one. Zero means the result cannot happen. One means the result must happen. Everything interesting lives between them. A result that is exactly as likely to happen as not sits at one half. Keep those three landmarks in mind, because every formula in this note is ultimately a machine for producing a number between zero and one.

### 1.2 Experiment, outcome, sample space, and event

The technical words for the three things in the sweet-shop picture are short, and each one is worth saying out loud.

> **Definition (Experiment).** An experiment is any procedure whose result cannot be predicted with certainty before it is carried out. The procedure may be repeated, and repeating it under the same conditions can still produce different results.

> **Definition (Outcome).** An outcome is one single possible result of the experiment. A single sweet coming out red is one outcome; the same sweet coming out green is another.

> **Definition (Sample space).** The sample space of an experiment is the set of every possible outcome. It is written with a capital letter $S$, and the number of outcomes in it is written $\lvert S\rvert$.

> **Definition (Event).** An event is a subset of the sample space, that is, a chosen collection of outcomes. We say the event occurs when the actual outcome of the experiment is one of the outcomes inside that collection.

A single coin toss has the sample space

$$
S = \{H, T\}
$$

where $H$ stands for head and $T$ stands for tail. The set is read as "the collection consisting of head and tail", and it has two outcomes, so $\lvert S\rvert = 2$.

Two tosses of the same coin give four outcomes, and it is important to write all four rather than to collapse them into "two heads, one head, no heads". The reason is that the first toss and the second toss are separate physical events, so the order matters:

$$
S = \{HH, HT, TH, TT\}
$$

The outcome $HT$ means the first toss showed a head and the second showed a tail, while $TH$ means the reverse. These are different outcomes even though both contain exactly one head, and treating them as one outcome is the first mistake beginners make.

A single roll of a fair six-sided die has six outcomes:

$$
S = \{1, 2, 3, 4, 5, 6\}
$$

Two rolls of that die have thirty-six outcomes, because each of the six results of the first roll can be paired with each of the six results of the second roll. Writing them as ordered pairs keeps the count honest:

$$
S = \{(1,1), (1,2), \dots, (6,5), (6,6)\}, \qquad \lvert S\rvert = 36
$$

A standard pack of playing cards has fifty-two outcomes when one card is drawn, because the pack has four suits of thirteen cards each.

An event is written the same way, as a set of outcomes. On one roll of the die, the event "an even number appears" is

$$
A = \{2, 4, 6\}
$$

and it contains three outcomes. The event "a number greater than four appears" is $B = \{5, 6\}$, containing two outcomes. The event "the number is seven" is the empty set, written $\varnothing$, because no face of the die carries that number.

Three pieces of set language describe how events combine, and each has a plain reading.

- The **union** $A \cup B$ is the collection of outcomes that lie in $A$, or in $B$, or in both. In words it is " $A$ happens or $B$ happens ".
- The **intersection** $A \cap B$ is the collection of outcomes that lie in both at once. In words it is " $A$ happens and $B$ happens ".
- The **complement** $A'$ is the collection of outcomes in $S$ that are not in $A$. In words it is " $A$ does not happen ".

| Experiment | Sample space | Number of outcomes |
|---|---|---|
| One coin toss | $\{H, T\}$ | $2$ |
| Two coin tosses | $\{HH, HT, TH, TT\}$ | $4$ |
| Three coin tosses | eight ordered strings of $H$ and $T$ | $8$ |
| One die roll | $\{1, 2, 3, 4, 5, 6\}$ | $6$ |
| Two die rolls | thirty-six ordered pairs | $36$ |
| One card from a pack | fifty-two named cards | $52$ |

### 1.3 The probability formula, read out loud

When every outcome in the sample space is equally likely, the probability of an event is a simple ratio.

> **Definition (Probability of an event, equally likely case).** For an event $E$ inside a sample space $S$ whose outcomes are all equally likely, the probability of $E$ is the number of outcomes favourable to $E$ divided by the number of outcomes in $S$:

$$
P(E) = \frac{\text{number of favourable outcomes}}{\text{total number of outcomes}}
$$

Every symbol in that sentence deserves a translation. The symbol $P(E)$ is read "the probability of the event $E$", and it is a single number, not a set. The word favourable does not mean pleasant or lucky; it means the outcomes that make the event happen. The word total means every outcome in the sample space, whether or not we like it.

So for the die roll with $A = \{2, 4, 6\}$, the favourable count is three and the total count is six, giving

$$
P(A) = \frac{3}{6} = \frac{1}{2}
$$

Two consequences follow immediately from the shape of a fraction. The numerator cannot be negative, so a probability cannot be negative. The numerator cannot exceed the denominator, so a probability cannot exceed one. Hence for every event $E$,

$$
0 \le P(E) \le 1
$$

Equality at zero happens only for the impossible event, and equality at one happens only for the certain event, which is the whole sample space. The value $0.5$ marks a result that is as likely to happen as not to happen.

The formula has one condition attached to it, and that condition is where most lost marks live. It requires the outcomes to be equally likely. A fair coin, a fair die, and a well-shuffled pack satisfy the condition. A loaded die, a biased coin, or a drawing rule that favours one side do not, and for those the formula is replaced by measurement or by a stated model, which is the subject of the next subsection.

### 1.4 Three ways of interpreting a probability

The number attached to an event can be justified in three different ways, and a good student can say which one is in play.

> **Definition (Classical interpretation).** When a sample space has $n$ outcomes that are all equally likely, the probability of an event is the count of favourable outcomes divided by $n$. This is the interpretation behind the probability formula, and it needs a symmetry argument to justify the equal likelihood.

> **Definition (Relative-frequency interpretation).** When an experiment can be repeated many times, the probability of an event is the value about which its observed relative frequency settles. If an event happened $f$ times in $n$ repetitions, its relative frequency is $f/n$, and the probability is the long-run limit of that ratio.

> **Definition (Subjective interpretation).** When repetition is impossible, a probability may express a reasoned degree of belief held by a particular person, together with the odds at which that person would be willing to bet. It is updated when new evidence arrives.

The three interpretations are not rivals so much as answers to different practical situations. The classical reading suits dice, cards, and urns, where symmetry makes equal likelihood defensible. The relative-frequency reading suits insurance, quality control, and medicine, where the only route to a number is a long record of similar cases. The subjective reading suits unique events such as the outcome of an election or the success of a single business venture, where neither symmetry nor repetition is available.

A useful way to keep the distinction alive is to ask what evidence would change your number. Under the classical reading nothing changes it, because the symmetry is fixed. Under the relative-frequency reading more data can change it slightly, but it settles down. Under the subjective reading any relevant news can change it at once.

### 1.5 The three axioms

Modern probability does not begin with the counting formula. It begins with three rules that every assignment of probabilities must obey, and the counting formula is then recovered as a special case.

> **Axiom 1 (Non-negativity).** For every event $A$, the probability satisfies $P(A) \ge 0$.

> **Axiom 2 (Normalisation).** The sample space is certain, so $P(S) = 1$.

> **Axiom 3 (Addition for disjoint events).** If two events $A$ and $B$ cannot happen together, then the probability that one or the other happens is the sum of their separate probabilities:

$$
P(A \cup B) = P(A) + P(B)
$$

Everything else in this note is a consequence of these three rules. The complement rule, the general addition law, the multiplication law, and Bayes' theorem are all theorems, not extra assumptions. That is why the subject feels tidy: three short sentences carry the entire structure.

The third axiom extends to any finite list of events that cannot happen together. If $A_1, A_2, \dots, A_k$ are pairwise disjoint, then

$$
P\left(A_1 \cup A_2 \cup \cdots \cup A_k\right) = P(A_1) + P(A_2) + \cdots + P(A_k)
$$

Axiom 3 is the workhorse. Whenever a complicated event can be cut into non-overlapping pieces, the probability of the whole is the sum of the probabilities of the pieces, and no further justification is needed.

### 1.6 Mutually exclusive and exhaustive events

Two adjectives describe how events sit inside the sample space, and both are used constantly.

> **Definition (Mutually exclusive).** Two events $A$ and $B$ are mutually exclusive, or disjoint, when they cannot happen at the same time. In symbols, their intersection is empty: $A \cap B = \varnothing$. For such events $P(A \cap B) = 0$.

> **Definition (Exhaustive).** A collection of events is exhaustive when their union is the whole sample space, so that at least one of them must happen. For two events this means $A \cup B = S$.

On one roll of a die, the events $A = \{1, 2\}$ and $B = \{5, 6\}$ are mutually exclusive, because no face shows a number in both sets. They are not exhaustive, because a three is in neither. The events $C = \{1, 2, 3\}$ and $D = \{4, 5, 6\}$ are both mutually exclusive and exhaustive: they share nothing, and between them they cover every face. Such a pair is called a partition of the sample space into two parts.

An exhaustive pair need not be exclusive, and an exclusive pair need not be exhaustive. On one roll of the die, the events "the number is even" and "the number is at least four" are exhaustive, since every face satisfies one of them, but they are not exclusive, because a four satisfies both. The events "the number is one" and "the number is two" are exclusive but not exhaustive.

The distinction matters because the simplified addition rule requires exclusivity, not exhaustivity. Adding two probabilities without subtracting an overlap is only legitimate when the two events cannot both occur.

### 1.7 A first look at independence

Two events are independent when knowing that one of them happened tells you nothing about whether the other happened.

> **Definition (Independent events).** Events $A$ and $B$ are independent when the probability that both occur equals the product of their separate probabilities:

$$
P(A \cap B) = P(A) \times P(B)
$$

Tossing the same coin twice produces independent events when the two events concern different tosses, because the coin has no memory. Drawing two cards from a pack without putting the first card back does not produce independent events, because the first draw changes what is left.

A warning is needed here, because the words sound similar and the ideas are opposites in one respect. Mutually exclusive events repel each other: if one happens, the other certainly does not, so knowing one occurred tells you a great deal. Independent events ignore each other: if one happens, the other is unaffected. Two events with positive probability can never be both mutually exclusive and independent, and Section 5 returns to this point because it is the most common confusion in the whole topic.

### 1.8 A first look at conditional probability

Sometimes we learn something before we finish the calculation. If a card has been drawn and someone tells you it is a heart, the chance that it is the ace of hearts changes from one in fifty-two to one in thirteen.

> **Definition (Conditional probability).** For events $A$ and $B$ with $P(B) > 0$, the conditional probability of $A$ given that $B$ has occurred is

$$
P(A \mid B) = \frac{P(A \cap B)}{P(B)}
$$

The vertical bar is read as "given". The formula says something very concrete: once we know $B$ happened, the world shrinks to the outcomes inside $B$, and within that smaller world we ask what fraction also lies in $A$. Dividing by $P(B)$ is the act of re-measuring the whole world so that the smaller world has total probability one.

### 1.9 A first look at counting

Many probability questions reduce to counting, and two counting tools do most of the work.

> **Definition (Permutation).** A permutation is an arrangement of objects in which order matters. The number of ways to arrange all $n$ distinct objects in a row is $n!$, read "$n$ factorial", where $n! = n \times (n-1) \times \cdots \times 2 \times 1$.

> **Definition (Combination).** A combination is a selection of objects in which order does not matter. The number of ways to choose $r$ objects from $n$ distinct objects is written $\binom{n}{r}$ and equals

$$
\binom{n}{r} = \frac{n!}{r!\,(n-r)!}
$$

The difference is easy to feel. Four named books on a shelf can be arranged in $4! = 24$ different orders, because swapping two books creates a new arrangement. A committee of three chosen from a class of twenty has $\binom{20}{3} = 1140$ possible compositions, and reordering the same three people does not create a new committee.

The laws collected in the next section are proved from the axioms, and every proof is short enough to reproduce in an examination.

## 2. Theorems, Lemmas, and Analytical Properties

### 2.1 The complement rule

> **Theorem (Complement rule).** For any event $A$ with complement $A'$, the two probabilities add to one:

$$
P(A') = 1 - P(A)
$$

The rule is used so often that it deserves a plain-language version: the chance that something does not happen is one minus the chance that it does. When a question says "not", "none", or "at least one", the complement rule is usually the shortest route to the answer.

On one roll of the die, the probability of not obtaining a six is

$$
P(\text{not } 6) = 1 - \frac{1}{6} = \frac{5}{6}
$$

which agrees with counting the five other faces directly.

### 2.2 The addition law for two events

> **Theorem (Addition law, two events).** For any two events $A$ and $B$ in the same sample space,

$$
P(A \cup B) = P(A) + P(B) - P(A \cap B)
$$

The subtraction is not optional. Adding $P(A)$ and $P(B)$ counts the outcomes that lie in both events twice, once as part of $A$ and once as part of $B$, so the overlap must be removed once to restore the correct count.

When the events are mutually exclusive the overlap is empty, its probability is zero, and the law collapses to the third axiom:

$$
P(A \cup B) = P(A) + P(B)
$$

That simplified form is correct only under exclusivity. Applying it to events that can occur together always overstates the answer.

### 2.3 The addition law for three events

> **Theorem (Addition law, three events).** For any three events $A$, $B$, and $C$,

$$
P(A \cup B \cup C) = P(A) + P(B) + P(C) - P(A \cap B) - P(A \cap C) - P(B \cap C) + P(A \cap B \cap C)
$$

The pattern is inclusion and exclusion. Single events are added, pairwise overlaps are subtracted because they were counted twice, and the three-way overlap is added back because it was counted three times and then subtracted three times, which left it uncounted. In a survey with three overlapping categories, forgetting the final term or one of the middle terms is a standard error.

### 2.4 The multiplication law

> **Theorem (Multiplication law, general form).** For events $A$ and $B$ with $P(B) > 0$,

$$
P(A \cap B) = P(A \mid B) \times P(B)
$$

> **Corollary (Multiplication law for independent events).** If $A$ and $B$ are independent, then

$$
P(A \cap B) = P(A) \times P(B)
$$

The general form is the ordinary way to handle two stages. To find the chance that a red sweet is drawn and then a green one, we multiply the chance of red on the first draw by the chance of green on the second draw computed inside the world where the first draw already happened.

The independent form applies when the second chance is unaffected by the first. Two independent tosses of a coin satisfy it; two draws from a small bag without replacement do not.

### 2.5 The independence test

Independence is a property to be checked, never assumed for convenience. The test is direct: compute the three quantities $P(A)$, $P(B)$, and $P(A \cap B)$, then compare the product with the intersection.

> **Test.** Events $A$ and $B$ are independent exactly when $P(A \cap B) = P(A) \times P(B)$. If the two sides differ, the events are dependent.

An equivalent test uses conditional probability: $A$ and $B$ are independent exactly when $P(A \mid B) = P(A)$, that is, when learning that $B$ happened leaves the probability of $A$ untouched. Both versions are accepted in an examination, and the product version is usually quicker because it avoids a division.

### 2.6 The law of total probability

> **Theorem (Law of total probability).** Suppose the events $A_1, A_2, \dots, A_k$ are mutually exclusive and exhaustive, so that exactly one of them must happen. Then for any event $B$,

$$
P(B) = P(B \mid A_1)\,P(A_1) + P(B \mid A_2)\,P(A_2) + \cdots + P(B \mid A_k)\,P(A_k)
$$

The theorem says that a probability can be computed by splitting the sample space into cases, finding the chance of $B$ inside each case, and averaging those chances with the case probabilities as weights. It is the formal version of the sentence "there are two ways this could happen, so work out each way and add".

### 2.7 An introduction to Bayes' theorem

> **Theorem (Bayes' theorem).** Under the same partition $A_1, \dots, A_k$ and with $P(B) > 0$, the probability of the case $A_i$ given that $B$ has occurred is

$$
P(A_i \mid B) = \frac{P(B \mid A_i)\,P(A_i)}{P(B \mid A_1)\,P(A_1) + \cdots + P(B \mid A_k)\,P(A_k)}
$$

Bayes' theorem reverses a conditional probability. The multiplication law supplies the chance of a symptom given a disease; Bayes' theorem turns it into the chance of the disease given the symptom, which is usually the question a patient actually asks. The denominator is the law of total probability, and it exists to renormalise the pieces so that the answers for all the cases add to one.

### 2.8 Counting results that support probability

> **Result (Multiplication principle).** If a first choice can be made in $m$ ways and, after it, a second choice can be made in $n$ ways, then the pair of choices can be made in $m \times n$ ways.

> **Result (Permutations of all objects).** The number of arrangements of $n$ distinct objects in a row is $n!$.

> **Result (Permutations of part of a collection).** The number of ordered arrangements of $r$ objects chosen from $n$ distinct objects is

$$
{}^{n}P_{r} = \frac{n!}{(n-r)!}
$$

> **Result (Combinations).** The number of unordered selections of $r$ objects from $n$ distinct objects is

$$
\binom{n}{r} = \frac{n!}{r!\,(n-r)!}
$$

The two formulas differ by the factor $r!$ in the denominator, which is precisely the number of ways to reorder the selected objects. When order matters, do not divide; when order does not matter, divide.

A table makes the choice concrete for a bag holding four red and two blue balls from which two balls are taken.

| Drawing rule | Order matters? | Replacement? | Total outcomes | Outcomes with both red | Probability |
|---|---|---|---|---|---|
| Ordered, with replacement | yes | yes | $36$ | $16$ | $\frac{16}{36} = \frac{4}{9}$ |
| Ordered, without replacement | yes | no | $30$ | $12$ | $\frac{12}{30} = \frac{2}{5}$ |
| Unordered, without replacement | no | no | $15$ | $6$ | $\frac{6}{15} = \frac{2}{5}$ |

The last two rows describe the same physical drawing, once listing the two balls in the order they appear and once ignoring that order, and both produce two fifths, because a decision about how to count cannot change the answer. The first row describes a genuinely different experiment, in which the drawn ball is put back, and it correctly produces the different value four ninths. A calculation that changes when only the counting method changes, without changing the experiment, has gone wrong somewhere.

### 2.9 The at-least-one result

> **Corollary (At least one).** For independent repetitions of an experiment in which an event $A$ has probability $p$ on each trial, the probability that $A$ occurs at least once in $n$ trials is

$$
P(\text{at least one}) = 1 - (1-p)^{n}
$$

The corollary follows from the complement rule applied to "none occurred", and the probability of none is the product of the separate failure probabilities. Three tosses of a fair coin therefore give a probability of at least one head equal to

$$
1 - \left(\frac{1}{2}\right)^{3} = 1 - \frac{1}{8} = \frac{7}{8}
$$

Direct counting of the seven outcomes containing at least one head confirms the value.

## 3. Formal Proofs, Derivations, and Methods

### 3.1 Why the impossible event has probability zero

Take Axiom 3 with the two events $S$ and $\varnothing$. They cannot happen together, because nothing is in the empty set, and their union is the whole sample space. The axiom therefore gives

$$
P(S) = P(S) + P(\varnothing)
$$

Subtracting $P(S)$ from both sides leaves $P(\varnothing) = 0$. The empty set is the event that cannot occur, and the axioms force its probability to be zero.

### 3.2 Why the complement rule is true

Split the sample space into the outcomes inside $A$ and the outcomes outside $A$. Those two collections have nothing in common and together they make up $S$, so Axiom 3 applies to them:

$$
P(A) + P(A') = P(S)
$$

Axiom 2 supplies $P(S) = 1$, hence

$$
P(A') = 1 - P(A)
$$

The same argument in counting language is even quicker. If the sample space has $n$ equally likely outcomes and the event $A$ contains $m$ of them, then $A'$ contains the remaining $n - m$, so

$$
P(A') = \frac{n - m}{n} = 1 - \frac{m}{n} = 1 - P(A)
$$

### 3.3 Why the addition law subtracts the overlap

Write the union as two non-overlapping pieces: everything in $A$, together with everything in $B$ that is not already in $A$. In symbols,

$$
A \cup B = A \cup \left(B \cap A'\right)
$$

and the two pieces on the right are disjoint. Axiom 3 then gives

$$
P(A \cup B) = P(A) + P\left(B \cap A'\right)
$$

Now split $B$ in the same way, into the part inside $A$ and the part outside it:

$$
P(B) = P(A \cap B) + P\left(B \cap A'\right)
$$

Rearranging the second line and substituting into the first produces the addition law:

$$
P(A \cup B) = P(A) + P(B) - P(A \cap B)
$$

The algebra says exactly what the counting argument says: the overlap is included twice when the two probabilities are added, so it must be removed once.

### 3.4 Why the multiplication law holds

The conditional probability formula is

$$
P(A \mid B) = \frac{P(A \cap B)}{P(B)}
$$

Multiplying both sides by $P(B)$, which is allowed because $P(B) > 0$, gives

$$
P(A \cap B) = P(A \mid B)\,P(B)
$$

For independent events the conditional probability equals the plain probability, so the right-hand side becomes $P(A)\,P(B)$. The whole of the multiplication law is therefore one multiplication of a definition, and no separate axiom is needed.

### 3.5 Why the law of total probability works

Take a partition $A_1, \dots, A_k$ and any event $B$. Every outcome of $B$ lies in exactly one of the parts, so $B$ can be cut into disjoint pieces:

$$
B = \left(B \cap A_1\right) \cup \left(B \cap A_2\right) \cup \cdots \cup \left(B \cap A_k\right)
$$

Axiom 3 turns the probability of that union into a sum, and the multiplication law rewrites each piece:

$$
P(B) = \sum_{i=1}^{k} P\left(B \cap A_i\right) = \sum_{i=1}^{k} P\left(B \mid A_i\right) P\left(A_i\right)
$$

### 3.6 Why Bayes' theorem follows at once

By definition of conditional probability,

$$
P(A_i \mid B) = \frac{P\left(A_i \cap B\right)}{P(B)}
$$

The numerator is rewritten by the multiplication law as $P\left(B \mid A_i\right) P\left(A_i\right)$, and the denominator is rewritten by the law of total probability. Substituting both gives the theorem. There is no new idea in the proof, only two substitutions, which is why Bayes' theorem is best remembered as "numerator is the path, denominator is all paths".

### 3.7 Deriving the combination formula

Selecting $r$ objects from $n$ in order can be done in $n(n-1)\cdots(n-r+1)$ ways, because the first slot has $n$ candidates, the second has $n-1$, and so on. That product equals $n!/(n-r)!$.

Now consider the same selection without regard to order. Each unordered selection of $r$ objects corresponds to exactly $r!$ ordered arrangements, since the chosen objects can be permuted among themselves in $r!$ ways. Dividing removes the overcount:

$$
\binom{n}{r} = \frac{n!}{r!\,(n-r)!}
$$

For four objects taken two at a time this gives $24/(2 \times 2) = 6$, which can be checked by listing the six pairs.

### 3.8 A method for any problem in this topic

Step 1. Name the experiment and write the sample space, or at least its size, before computing anything.

Step 2. Write each event as a set of outcomes in words and in symbols.

Step 3. Decide which law the question needs by listening for the joining word: "or" suggests the addition law, "and" or "both" suggests the multiplication law, "not", "none" or "at least one" suggests the complement rule.

Step 4. Check whether the events overlap before adding, and check whether they are independent before multiplying.

Step 5. Compute, then test the answer against the bounds zero and one, and against a direct count when the sample space is small.

## 4. Representative Worked Examples and Solutions

### 4.1 Problem: a single die with two overlapping events

A fair die is rolled once. Let $A$ be the event that the number is even and let $B$ be the event that the number is greater than four. Find the probability of $A$, of $B$, of $A$ or $B$, and of not $A$.

### 4.2 Solution: count, then apply the addition law

Step 1. Write the sample space and count it.

$$
S = \{1, 2, 3, 4, 5, 6\}, \qquad \lvert S\rvert = 6
$$

Step 2. Write each event as a list of outcomes.

$$
A = \{2, 4, 6\}, \qquad B = \{5, 6\}
$$

Step 3. Apply the probability formula to each event separately.

$$
P(A) = \frac{3}{6} = \frac{1}{2}, \qquad P(B) = \frac{2}{6} = \frac{1}{3}
$$

Step 4. Find the overlap, which is the set of outcomes in both lists.

$$
A \cap B = \{6\}, \qquad P(A \cap B) = \frac{1}{6}
$$

Step 5. Apply the addition law, because the question asks for one event or the other.

$$
P(A \cup B) = \frac{1}{2} + \frac{1}{3} - \frac{1}{6} = \frac{3}{6} + \frac{2}{6} - \frac{1}{6} = \frac{4}{6} = \frac{2}{3}
$$

Step 6. Confirm by direct listing. The union is $\{2, 4, 5, 6\}$, four outcomes out of six, so the probability is two thirds, as the law predicted.

Step 7. Apply the complement rule for the last part.

$$
P(A') = 1 - P(A) = 1 - \frac{1}{2} = \frac{1}{2}
$$

The odd faces $1$, $3$, and $5$ give the same value by direct counting.

### 4.3 Problem: two coins and the addition law

Two fair coins are tossed. Let $A$ be the event that at least one head appears and let $B$ be the event that the first coin shows a head. Find the probability of $A$ or $B$.

### 4.4 Solution: notice that one event sits inside the other

Step 1. List the sample space of four equally likely outcomes.

$$
S = \{HH, HT, TH, TT\}
$$

Step 2. Write the events.

$$
A = \{HH, HT, TH\}, \qquad B = \{HH, HT\}
$$

Step 3. Compute the separate probabilities.

$$
P(A) = \frac{3}{4}, \qquad P(B) = \frac{2}{4} = \frac{1}{2}
$$

Step 4. Identify the overlap. Both events contain $HH$ and $HT$, so the intersection is $B$ itself and

$$
P(A \cap B) = \frac{2}{4} = \frac{1}{2}
$$

Step 5. Apply the addition law.

$$
P(A \cup B) = \frac{3}{4} + \frac{1}{2} - \frac{1}{2} = \frac{3}{4}
$$

Step 6. Interpret. Since every outcome in $B$ is already in $A$, the event $A$ or $B$ is just $A$, and the arithmetic confirms it. The example shows why the subtraction is necessary: without it the answer would be five quarters, a probability greater than one, which is impossible.

### 4.5 Problem: one card from a pack

A card is drawn from a well-shuffled pack of fifty-two. Find the probability that it is a heart or a king.

### 4.6 Solution: subtract the card counted twice

Step 1. Reason about the pack. There are fifty-two equally likely cards.

Step 2. Count the hearts and the kings.

$$
P(\text{heart}) = \frac{13}{52}, \qquad P(\text{king}) = \frac{4}{52}
$$

Step 3. Count the overlap, which is the king of hearts, a single card.

$$
P(\text{heart and king}) = \frac{1}{52}
$$

Step 4. Apply the addition law.

$$
P(\text{heart or king}) = \frac{13}{52} + \frac{4}{52} - \frac{1}{52} = \frac{16}{52} = \frac{4}{13}
$$

Step 5. Interpret. Adding the two headline counts alone would give seventeen cards, but the king of hearts was counted in both groups; the pack contains only sixteen cards that are a heart or a king.

### 4.7 Problem: two dice and the multiplication law

Two fair dice are rolled. Find the probability that both show a six, and the probability that the total is seven.

### 4.8 Solution: independence for the pair, counting for the total

Step 1. State the sample space size, which is six times six.

$$
\lvert S\rvert = 36
$$

Step 2. Treat the two dice as independent, because neither die influences the other.

$$
P(\text{six and six}) = \frac{1}{6} \times \frac{1}{6} = \frac{1}{36}
$$

Step 3. Count the outcomes whose total is seven by listing the first die.

$$
(1,6), (2,5), (3,4), (4,3), (5,2), (6,1)
$$

Step 4. Divide the count by the size of the sample space.

$$
P(\text{total } 7) = \frac{6}{36} = \frac{1}{6}
$$

Step 5. Interpret. The multiplication law produces one thirty-sixth because there is exactly one favourable ordered pair; the sum of seven has six favourable pairs, and the counting route is the only sensible one for a condition on the total.

### 4.9 Problem: two draws from a bag without replacement

A bag holds five red and three black balls. Two balls are drawn one after another without replacement. Find the probability that both are red, and the probability that at least one is black.

### 4.10 Solution: multiply the changing chances

Step 1. Record the first draw. Five of the eight balls are red.

$$
P(\text{first red}) = \frac{5}{8}
$$

Step 2. Record the second draw inside the smaller world left behind, where four red and three black remain.

$$
P(\text{second red} \mid \text{first red}) = \frac{4}{7}
$$

Step 3. Apply the multiplication law, because both draws must be red.

$$
P(\text{both red}) = \frac{5}{8} \times \frac{4}{7} = \frac{20}{56} = \frac{5}{14}
$$

Step 4. Use the complement rule for the second question.

$$
P(\text{at least one black}) = 1 - \frac{5}{14} = \frac{9}{14}
$$

Step 5. Confirm with combinations, choosing two of the eight balls with order ignored.

$$
\frac{\binom{5}{2}}{\binom{8}{2}} = \frac{10}{28} = \frac{5}{14}
$$

Both routes agree, which is the point of the method: the ordered product and the unordered count must give the same probability.

### 4.11 Problem: a committee chosen from a class

A class has six students. Two of them, Anna and Ben, hope to be chosen for a committee of two. If the two places are filled at random, find the probability that both are chosen.

### 4.12 Solution: count the selections once

Step 1. Count the possible committees, where order does not matter.

$$
\binom{6}{2} = \frac{6 \times 5}{2} = 15
$$

Step 2. Count the favourable committees. Only one committee contains both Anna and Ben.

Step 3. Divide.

$$
P(\text{both chosen}) = \frac{1}{15}
$$

Step 4. Interpret. Counting ordered pairs would have given thirty pairs and two favourable orders, and the ratio would still be one fifteenth, which shows that the choice of counting method is free as long as it is applied consistently to the top and the bottom.

### 4.13 Problem: a conditional probability with two children

A family with two children is chosen at random, with boys and girls equally likely and independent. Given that the older child is a girl, find the probability that both children are girls.

### 4.14 Solution: shrink the sample space first

Step 1. List the four equally likely outcomes in birth order.

$$
S = \{bb, bg, gb, gg\}
$$

Step 2. Name the given event and the target event.

$$
G_1 = \{gb, gg\}, \qquad G_3 = \{gg\}
$$

Step 3. Write the intersection, which is the single outcome satisfying both conditions.

$$
G_1 \cap G_3 = \{gg\}
$$

Step 4. Apply the definition of conditional probability.

$$
P(G_3 \mid G_1) = \frac{1/4}{2/4} = \frac{1}{2}
$$

Step 5. Interpret. Once the older child is known to be a girl, only two outcomes remain possible, and one of them has two girls. The denominator is the conditional universe, and leaving it out is the error discussed next.

## 5. Mathematical Extensions, Limits, and Common Errors

### 5.1 Mutually exclusive is not the same as independent

The single most damaging confusion at this level is treating these two words as synonyms. Mutually exclusive events cannot happen together, so their intersection has probability zero. Independent events do not influence each other, so their intersection has probability equal to the product of their probabilities.

Those two statements cannot both be true for a pair of events that each have positive probability. If $P(A) > 0$ and $P(B) > 0$ and the events are mutually exclusive, then the product $P(A)P(B)$ is strictly positive while $P(A \cap B) = 0$, so the pair is dependent, indeed maximally so, because one event rules the other out. Independence is about multiplication; exclusivity is about addition. Mixing them up produces either a probability of zero where a positive product was expected, or a product where zero belongs.

### 5.2 Where the classical formula stops working

The formula of favourable over total rests on equal likelihood, and equal likelihood is an assumption about the physical setup, not a fact about the numbers. A die with a hidden weight, a coin that has been shaved, or a raffle in which one entrant holds many tickets all break the assumption. In those cases the correct move is either to count weighted outcomes, treating a doubly likely outcome as two outcomes, or to use relative frequencies from data. Writing the assumption down before computing is the habit that protects the mark.

### 5.3 Extensions worth knowing

Two extensions show how far the same ideas reach. The birthday argument asks for the probability that at least two people in a group of twenty-three share a birthday, and the complement rule answers it: the probability that all birthdays differ is the product of twenty-three decreasing fractions starting at three hundred and sixty-five over three hundred and sixty-five, and the required probability is one minus that product, approximately $0.507$. The answer surprises people because they compare a birthday with their own instead of comparing every pair, and that is a lesson in reading a question precisely.

The second extension is Bayes' theorem applied to a medical test. If a disease affects one person in a thousand and a test is ninety-nine per cent sensitive and ninety-nine per cent specific, then a positive result still leaves the probability of disease near one in eleven, because healthy people vastly outnumber sick ones. The base rate dominates, and forgetting it is the classic error of the subjective interpretation.

### 5.4 Beginner mistakes to check before submitting

- Adding two probabilities without subtracting the overlap, which inflates the answer and can push it above one.
- Using the simplified sum for events that are not mutually exclusive.
- Multiplying $P(A)$ by $P(B)$ when the two events affect each other, as in drawing without replacement.
- Dividing by the size of the original sample space instead of the conditional universe in a conditional probability.
- Treating ordered and unordered samples as if they were the same experiment, so that the numerator is counted one way and the denominator another.
- Forgetting to subtract from one when a question says "at least one" or "none".
- Leaving a final fraction unreduced, such as three sixths instead of one half.
- Reporting a probability outside the interval from zero to one without noticing.

### 5.5 Consolidation

Every question in this topic may be answered by four disciplined moves. Write the sample space, so that the total is beyond dispute. Write the event as a set, so that the favourable outcomes can be counted. Choose the law by the joining word, and verify its precondition, namely overlap for addition and independence for multiplication. Finally, check the result against zero, against one, and against a direct count where the sample space is small. The axioms guarantee that these moves always produce a legitimate probability, and the worked examples show how little else is needed.
