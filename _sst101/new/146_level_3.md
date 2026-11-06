## 1. Foundational Concepts, Definitions, and Axioms

### 1.1 What an examination actually asks

Every question on this topic is a request to convert a described experiment into one of six calculations: a direct ratio of counts, a probability of a union, a probability of an intersection, a conditional probability, a probability obtained by splitting into cases, or a probability obtained by reversing a conditional. Recognising which of the six is being asked, before writing any symbol, is worth more marks than any amount of algebra, because each type has a standard opening move and a standard check.

The wording usually gives the type away. "Find the probability that a card is a heart or a king" is a union. "Find the probability that both cards are hearts" is an intersection, and the phrase "without replacement" turns it into a chain. "Given that the first ball was red" is a conditional, and the words "given that" are the formal signal that the sample space must be reduced. "Of all defective items, what proportion came from the second machine" is a reversal, which is Bayes' theorem. "At least one" is a complement. "How many ways" or "in how many orders" is a counting question that will feed one of the six.

Examiners reward structure as much as answers. A solution that states the sample space, names the events, shows the formula with the numbers substituted, and finishes with a sentence of interpretation will collect method marks even when an arithmetic slip spoils the final value. A solution that writes only a number cannot collect method marks at all, which is the practical reason for the layout discipline set out in Section 5.

### 1.2 Definitions in examination form

> **Definition (Experiment, sample space, event).** An experiment is a procedure whose outcome is not known in advance. Its sample space $S$ is the set of all outcomes. An event $A$ is a subset of $S$, and $A$ occurs when the realised outcome lies in $A$.

> **Definition (Probability formula).** When the outcomes of a finite sample space are equally likely,

$$
P(A) = \frac{\lvert A\rvert}{\lvert S\rvert} = \frac{\text{number of favourable outcomes}}{\text{total number of outcomes}}
$$

> **Axiom (Kolmogorov).** Probabilities satisfy $P(A) \ge 0$ for every event $A$; $P(S) = 1$; and $P(A \cup B) = P(A) + P(B)$ for disjoint $A$ and $B$, extended to any finite collection of pairwise disjoint events.

The immediate consequences are quoted without proof in an examination, unless the question says "prove" or "show": $P(\varnothing) = 0$, $P(A') = 1 - P(A)$, $0 \le P(A) \le 1$, $P(A \setminus B) = P(A) - P(A \cap B)$, and $A \subseteq B$ implies $P(A) \le P(B)$.

The counting formula carries a hypothesis that examiners test deliberately. Rolling a fair die satisfies it; drawing a ball from an urn in which every ball is equally likely to be chosen satisfies it; but drawing a card from a pack in which one card is bent does not, and neither does a spinner with unequal sectors. When the hypothesis fails, the question will supply either a probability distribution or relative frequencies, and the calculation moves to weighted outcomes or to the relative-frequency interpretation.

### 1.3 The three interpretations as exam material

A short-answer question may ask you to distinguish the interpretations, so keep one sentence for each. The classical interpretation assigns probability by symmetry and counting, and it is the only one that licences "$P(A) = \lvert A\rvert/\lvert S\rvert$" without further data. The relative-frequency interpretation defines probability as the stabilised value of $f_n/n$ over many independent repetitions, and it is the interpretation behind empirical statements about defect rates or mortality. The subjective interpretation treats probability as a coherent degree of belief, adjustable in the light of evidence, and it is the only one available for a single unrepeatable event.

The examination consequence is practical. If a question states "a fair die", the classical interpretation applies and counting is legitimate. If a question states "in a large consignment, $2\%$ of items are defective", the relative-frequency interpretation applies and the number $0.02$ is used as a given probability. If a question states "a doctor believes there is a $70\%$ chance", the subjective interpretation applies and Bayes' theorem is the natural tool for updating that belief.

### 1.4 Exclusive, exhaustive, and the partition

> **Definition (Mutually exclusive).** $A$ and $B$ are mutually exclusive when $A \cap B = \varnothing$, hence $P(A \cap B) = 0$. A collection is pairwise mutually exclusive when every two distinct members are disjoint.

> **Definition (Exhaustive).** A collection is exhaustive when the union of its members is $S$, hence at least one member must occur.

> **Definition (Partition).** A partition is a collection that is both pairwise mutually exclusive and exhaustive, so that exactly one member occurs on each realisation.

A partition is the structure required by the law of total probability and by Bayes' theorem, and constructing it correctly is half of any such question. The most common failure is a partition that leaves a gap, such as splitting customers into those who buy insurance and those who do not buy insurance but forgetting a third group of enquirers, or one that overlaps, such as splitting by "defective" and "from machine one" when machine one can also produce defectives.

| Pair of events | Intersection | Union | Verdict |
|---|---|---|---|
| Die shows $1$; die shows $2$ | empty | $\{1,2\}$ | exclusive, not exhaustive |
| Die shows even; die shows odd | empty | whole space | exclusive and exhaustive |
| Die shows even; die shows at least $4$ | $\{4,6\}$ | $\{2,4,5,6\}$ | neither |
| First coin head; second coin head | one outcome | three outcomes | neither |

### 1.5 Conditional probability and independence

> **Definition (Conditional probability).** For $P(B) > 0$,

$$
P(A \mid B) = \frac{P(A \cap B)}{P(B)}
$$

> **Definition (Independence).** $A$ and $B$ are independent when $P(A \cap B) = P(A)P(B)$, equivalently when $P(A \mid B) = P(A)$ provided $P(B) > 0$.

Both definitions must be reproduced accurately, because a misquoted definition loses the definition mark even when the subsequent calculation is correct. Note the asymmetry: the conditional probability is a ratio and is defined for any pair with $P(B) > 0$, while independence is an equation that may hold or fail, and is a property of the pair within a stated model.

The examiner's favourite discrimination is between exclusive and independent events. Exclusive means the intersection is empty; independent means the intersection factors. For positive probabilities the two cannot both hold, so an answer that describes a pair as "mutually exclusive and therefore independent" is wrong twice over. Section 5 lists the exact wording that should trigger a check.

### 1.6 The counting toolkit for examination questions

> **Result (Multiplication principle).** Sequential choices multiply: $m$ ways followed by $n$ ways gives $mn$ orders.

> **Result (Permutations).** The number of arrangements of $n$ distinct objects is $n!$; the number of ordered selections of $r$ from $n$ is $n!/(n-r)!$.

> **Result (Combinations).** The number of unordered selections of $r$ from $n$ is

$$
\binom{n}{r} = \frac{n!}{r!\,(n-r)!}
$$

> **Result (Arrangements with repetition).** The number of distinct arrangements of $n$ objects with $n_1$ of one kind, $n_2$ of a second kind, and so on, is $n!/(n_1! n_2! \cdots n_k!)$.

Four standard counts are worth memorising because they recur: two dice give $36$ ordered outcomes; three coins give $8$; a five-card hand from a pack gives $\binom{52}{5} = 2\,598\,960$; and a committee of three from ten gives $\binom{10}{3} = 120$.

| Question wording | Order matters? | Replacement? | Count to use |
|---|---|---|---|
| "in how many orders can the five books be arranged" | yes | not applicable | $5! = 120$ |
| "how many three-digit codes without repeated digits" | yes | no | $10 \times 9 \times 8 = 720$ |
| "how many committees of three from ten" | no | no | $\binom{10}{3} = 120$ |
| "how many selections of two sweets from six kinds, repeats allowed" | no | yes | $\binom{7}{2} = 21$ |

The final row uses the unordered-with-replacement count $\binom{n+r-1}{r}$, which for $n = 6$ sweets and $r = 2$ gives $\binom{7}{2} = 21$. The three earlier rows are the ones examined most often.

### 1.7 Notation discipline that earns marks

Write $P(A)$ not $P(A$ and $B)$ when only one event is meant. Write $P(A \mid B)$ with the conditioning event after the bar, and read it as "the probability of $A$ given $B$". Write $A \cup B$ for "or" and $A \cap B$ for "and", and avoid the words "or" and "and" inside a displayed formula, since the mathematical symbols are unambiguous while the English words are not: "or" may be inclusive or exclusive in ordinary speech, but $A \cup B$ is always inclusive.

De Morgan's laws should be quoted in the form used:

$$
\left(A \cup B\right)' = A' \cap B', \qquad \left(A \cap B\right)' = A' \cup B'
$$

The first is the algebraic form of "neither", the second of "not both". Questions about "neither event occurs" are answered by the complement of the union, not by the union of the complements, and that single confusion accounts for a large share of lost marks on multi-part questions.

## 2. Theorems, Lemmas, and Analytical Properties

### 2.1 The high-yield list

> **Theorem (Complement rule).** $P(A') = 1 - P(A)$.

> **Theorem (Addition law, two events).** $P(A \cup B) = P(A) + P(B) - P(A \cap B)$.

> **Theorem (Addition law, three events).**

$$
P(A \cup B \cup C) = P(A) + P(B) + P(C) - P(A \cap B) - P(A \cap C) - P(B \cap C) + P(A \cap B \cap C)
$$

> **Theorem (Multiplication law).** $P(A \cap B) = P(A \mid B)P(B) = P(B \mid A)P(A)$ for positive conditioning probabilities.

> **Theorem (Chain rule).**

$$
P\left(A_1 \cap \cdots \cap A_n\right) = P\left(A_1\right) P\left(A_2 \mid A_1\right) \cdots P\left(A_n \mid A_1 \cap \cdots \cap A_{n-1}\right)
$$

> **Theorem (Law of total probability).** For a partition $A_1, \dots, A_k$,

$$
P(B) = \sum_{i=1}^{k} P\left(B \mid A_i\right) P\left(A_i\right)
$$

> **Theorem (Bayes' theorem).**

$$
P\left(A_j \mid B\right) = \frac{P\left(B \mid A_j\right) P\left(A_j\right)}{\sum_{i=1}^{k} P\left(B \mid A_i\right) P\left(A_i\right)}
$$

These seven statements, together with the counting results of Section 1.6, cover every part of every question on this topic. Each is a consequence of the axioms, and each proof is short enough to reproduce under examination pressure, as Section 3 demonstrates.

### 2.2 Derived properties that shorten solutions

> **Corollary (Probability of a difference).** $P(A \setminus B) = P(A) - P(A \cap B)$, hence $P(A \cap B') = P(A) - P(A \cap B)$.

> **Corollary (Bounds on a union).** $P(A \cup B) \le P(A) + P(B)$, with equality exactly when the events are disjoint; more generally $P\left(A_1 \cup \cdots \cup A_n\right) \le \sum_i P\left(A_i\right)$.

> **Corollary (Neither occurs).** $P(A' \cap B') = 1 - P(A \cup B)$.

> **Corollary (At least one).** For independent trials with common failure probability $q$, $P(\text{at least one}) = 1 - q^{n}$; for sampling without replacement from a population of $N$ containing $K$ marked items, $P(\text{at least one marked}) = 1 - \binom{N-K}{n} / \binom{N}{n}$.

> **Corollary (Independence and complements).** If $A$ and $B$ are independent, then each of $A'$ and $B$, $A$ and $B'$, $A'$ and $B'$ is an independent pair.

> **Lemma (Exclusive versus independent).** If $P(A) > 0$, $P(B) > 0$, and $A \cap B = \varnothing$, then $A$ and $B$ are dependent, with $P(A \mid B) = 0$.

The corollary on "neither" is worth memorising as a single line, since multi-part questions very often end with the question "hence find the probability that neither event occurs". The answer is one minus the union already computed, never the product of the individual complements unless independence has been established.

### 2.3 Recognising which law applies

| Wording in the question | Law to use | Precondition to verify |
|---|---|---|
| "or", "at least one of the two" | addition law | subtract the intersection unless disjoint |
| "and", "both", "followed by" | multiplication law | conditional factors unless independent |
| "not", "neither", "none", "at least one" | complement rule | identify the complement exactly |
| "given that", "if it is known that" | conditional definition | divide by the conditioning probability |
| "of those that are defective, what fraction" | Bayes' theorem | a valid partition |
| "how many ways", "arrangements", "committees" | counting | order matters or not |

The table is a decision aid, not a substitute for reading the whole question. Many multi-part questions chain two or three rows, and the marks are allocated per part, so a wrong first part need not destroy the later ones provided the method in each is visible.

### 2.4 Bounds and sanity checks

Three inequalities catch almost every arithmetic error before it reaches the examiner. First, $0 \le P \le 1$ for every computed probability. Second, $P(A \cup B) \ge \max\left\{P(A), P(B)\right\}$, because a union contains each of its parts. Third, $P(A \cap B) \le \min\left\{P(A), P(B)\right\}$, and for independent events the intersection is the product, which is smaller than either factor when both are below one.

A fourth check applies to partitions: the probabilities of all cases, or all posterior probabilities, must sum to one. In a Bayes question this check costs five seconds and detects almost every slip in the denominator.

### 2.5 Counting identities useful in probability

> **Lemma (Symmetry).** $\binom{n}{r} = \binom{n}{n-r}$.

> **Lemma (Pascal).** $\binom{n}{r} = \binom{n-1}{r-1} + \binom{n-1}{r}$.

> **Lemma (Vandermonde).** $\sum_{k} \binom{m}{k}\binom{n}{r-k} = \binom{m+n}{r}$.

> **Lemma (Subset total).** $\sum_{r=0}^{n} \binom{n}{r} = 2^{n}$.

Vandermonde's identity is the algebraic form of splitting a group of $m + n$ people into a group of $m$ and a group of $n$ and choosing $r$ in total, and it appears whenever a question asks for the probability that a sample contains a specified mix from two sub-populations. The hypergeometric formula is exactly its probabilistic counterpart.

### 2.6 The birthday-type lemma in examination form

> **Lemma (At least one coincidence).** For $n$ independent trials each uniformly distributed over $N$ labels,

$$
P(\text{some label repeats}) = 1 - \frac{N(N-1)\cdots(N-n+1)}{N^{n}}
$$

Two special cases are examined: the birthday version with $N = 365$, where $n = 23$ already gives a probability slightly above one half, and the dice version with $N = 6$, where four rolls give

$$
1 - \left(\frac{5}{6}\right)^{4} = 1 - \frac{625}{1296} = \frac{671}{1296} \approx 0.518
$$

for at least one six. Both are complement arguments, and both are answered faster by the complement than by any direct count.

## 3. Formal Proofs, Derivations, and Methods

### 3.1 The complement rule from the axioms

The events $A$ and $A'$ are disjoint and exhaust $S$. Finite additivity followed by normalisation gives

$$
P(A) + P(A') = P\left(A \cup A'\right) = P(S) = 1
$$

so $P(A') = 1 - P(A)$. The examiner's marking point is the sentence identifying $A$ and $A'$ as disjoint and exhaustive; the algebra alone usually earns the method mark but not the reasoning mark.

### 3.2 The two-event addition law

Decompose the union into disjoint pieces:

$$
A \cup B = A \cup \left(B \cap A'\right)
$$

Additivity gives $P(A \cup B) = P(A) + P\left(B \cap A'\right)$, and the difference rule applied to $B$ gives $P\left(B \cap A'\right) = P(B) - P(A \cap B)$. Substituting produces

$$
P(A \cup B) = P(A) + P(B) - P(A \cap B)
$$

The same result follows in one line from inclusion and exclusion on the three disjoint regions $A \cap B'$, $A \cap B$, and $A' \cap B$, whose probabilities sum to $P(A) + P(B) - P(A \cap B)$.

### 3.3 The three-event addition law

Apply the two-event law to $A \cup B$ and $C$:

$$
P(A \cup B \cup C) = P(A \cup B) + P(C) - P\left((A \cup B) \cap C\right)
$$

Distributing the intersection and applying the two-event law again gives

$$
P\left((A \cup B) \cap C\right) = P(A \cap C) + P(B \cap C) - P(A \cap B \cap C)
$$

Expanding $P(A \cup B)$ and collecting terms yields the three-event law. The sign pattern, plus for singles, minus for pairs, plus for the triple, generalises by the same induction, and the alternating sequence is the reason inclusion and exclusion is described as a correction of successive overcounts.

### 3.4 The multiplication law and its independent case

The definition of conditional probability is

$$
P(A \mid B) = \frac{P(A \cap B)}{P(B)}, \qquad P(B) > 0
$$

Multiplying by $P(B)$ gives the multiplication law. When $A$ and $B$ are independent, the definition of independence replaces $P(A \mid B)$ by $P(A)$, so

$$
P(A \cap B) = P(A)P(B)
$$

For three mutually independent events the chain rule collapses all conditional bars, giving $P(A \cap B \cap C) = P(A)P(B)P(C)$. That collapse is legitimate only under mutual independence, never under pairwise independence alone.

### 3.5 The partition identity

For a partition $A_1, \dots, A_k$ and any event $B$, the identity $B = \bigcup_i \left(B \cap A_i\right)$ expresses $B$ as a disjoint union. Additivity gives $P(B) = \sum_i P\left(B \cap A_i\right)$, and the multiplication law converts each term into $P\left(B \mid A_i\right) P\left(A_i\right)$.

### 3.6 Bayes' theorem

By definition,

$$
P\left(A_j \mid B\right) = \frac{P\left(A_j \cap B\right)}{P(B)}
$$

The numerator becomes $P\left(B \mid A_j\right) P\left(A_j\right)$ by the multiplication law, and the denominator becomes the sum over all cases by the partition identity. Substituting gives the theorem, and summing over $j$ returns one, which is the check used in Section 2.4.

### 3.7 Independence passes to complements

Assume $P(A \cap B) = P(A)P(B)$. Then

$$
P\left(A \cap B'\right) = P(A) - P(A \cap B) = P(A)\left(1 - P(B)\right) = P(A)P\left(B'\right)
$$

The first equality is the difference rule, the second the independence hypothesis, and the third the complement rule. Repeating the argument gives independence of $A'$ and $B'$ as well.

### 3.8 The combination formula

Ordered selections of $r$ from $n$ number $n(n-1)\cdots(n-r+1) = n!/(n-r)!$. Each unordered selection is counted $r!$ times within that total, once per ordering of its members, so the number of unordered selections is the quotient

$$
\binom{n}{r} = \frac{n!}{r!\,(n-r)!}
$$

Every counting argument in a probability solution should state which of the two counts is being used, because the numerator and denominator must agree.

### 3.9 Method: the five-line layout that earns full marks

Step 1. Write the sample space, or its size, and say whether outcomes are equally likely.

Step 2. Define each event in words and in symbols, and list its outcomes when the space is small.

Step 3. Name the law being applied and write it in symbols before substituting numbers.

Step 4. Substitute, simplify to a single fraction or decimal, and box the result.

Step 5. Add one sentence of interpretation, and where the question has several parts, verify that the answers are consistent, for example that complementary parts sum to one.

This layout costs about thirty seconds and typically recovers two or three method marks on a six-mark question, because each marking point corresponds to one of the five lines.

### 3.10 Method: the Bayes table

For a question with three sources and one observed effect, build a table before writing any formula. Columns are the source, its prior probability, the conditional probability of the observed effect given that source, and the product of the two. The sum of the product column is the denominator, and each product divided by that sum is a posterior.

| Source | Prior | Conditional | Product | Posterior |
|---|---|---|---|---|
| $E_1$ | $0.5$ | $0.02$ | $0.010$ | $0.010 / 0.032 = 0.3125$ |
| $E_2$ | $0.3$ | $0.04$ | $0.012$ | $0.012 / 0.032 = 0.375$ |
| $E_3$ | $0.2$ | $0.05$ | $0.010$ | $0.010 / 0.032 = 0.3125$ |
| Total | $1.0$ | not summed | $0.032$ | $1.000$ |

The table makes the partition visible, prevents the error of summing the conditional column, and provides the denominator without a separate calculation. The priors must sum to one and the posteriors must sum to one; both totals are printed in the final row as a check.

### 3.11 Method: the at-least-one argument

Step 1. Write the complement of the required event explicitly: "at least one" becomes "none".

Step 2. Decide whether the trials are independent. If they are, multiply the failure probabilities; if sampling is without replacement, use the ratio of combinations.

Step 3. Subtract from one.

Step 4. Sanity-check the answer: a probability of at least one occurrence must exceed the probability of exactly one occurrence, and must approach one as the number of trials grows.

### 3.12 Method: selection without replacement

For $n$ draws from $N$ objects of which $K$ are marked, the probability of exactly $k$ marked objects is

$$
P(X = k) = \frac{\binom{K}{k}\binom{N-K}{n-k}}{\binom{N}{n}}
$$

The corresponding conditional probability, such as the probability of exactly one marked object given at least one, is a ratio of two such counts, and the conditional universe in the denominator is the probability of the conditioning event, not the probability of the whole space.

## 4. Representative Worked Examples and Solutions

### 4.1 Model solution A: three wrappers, one price tag

Three assistants wrap gifts in a shop. Helen wraps $45\%$ of the gifts and forgets to remove the price tag on $2\%$ of hers. Jane wraps $35\%$ of the gifts and forgets on $5\%$ of hers. Mary wraps the remainder and forgets on $3\%$ of hers. A gift is chosen at random.

(a) Find the probability that it still carries a price tag.

(b) Given that it carries a price tag, find the probability that each assistant wrapped it.

### 4.2 Solution A: partition, then reverse

Step 1. Define the partition. Let $H$, $J$, $M$ denote the events that Helen, Jane, Mary wrapped the gift, and let $T$ denote the event that a tag remains.

$$
P(H) = 0.45, \qquad P(J) = 0.35, \qquad P(M) = 1 - 0.45 - 0.35 = 0.20
$$

Marking point M1: the prior for Mary must be obtained by subtraction, and the three priors must be shown to sum to one.

Step 2. Record the conditional probabilities supplied by the question.

$$
P(T \mid H) = 0.02, \qquad P(T \mid J) = 0.05, \qquad P(T \mid M) = 0.03
$$

Marking point M2: the directions of these conditionals are as stated, tag given wrapper, not the reverse.

Step 3. Apply the law of total probability.

$$
P(T) = (0.45)(0.02) + (0.35)(0.05) + (0.20)(0.03)
$$

Step 4. Evaluate each product and sum them.

$$
P(T) = 0.009 + 0.0175 + 0.006 = 0.0325
$$

Marking point M3: one mark for the weighted sum, one for the correct total of $0.0325$.

Step 5. For part (b), apply Bayes' theorem to each assistant in turn, dividing the corresponding product by the total.

$$
P(H \mid T) = \frac{0.009}{0.0325} = \frac{18}{65} \approx 0.277
$$

$$
P(J \mid T) = \frac{0.0175}{0.0325} = \frac{7}{13} \approx 0.538
$$

$$
P(M \mid T) = \frac{0.006}{0.0325} = \frac{12}{65} \approx 0.185
$$

Marking point M4: each posterior needs the same denominator $P(T)$, and a solution that divides by the prior or by the conditional probability earns nothing.

Step 6. Check that the posteriors sum to one.

$$
\frac{18}{65} + \frac{7}{13} + \frac{12}{65} = \frac{18 + 35 + 12}{65} = \frac{65}{65} = 1
$$

Marking point M5: the consistency check is worth a mark when the question says "verify" or "comment", and it protects the rest of the answer.

Step 7. Interpret. Helen wraps the largest share but loses the smallest proportion of tags, so her posterior share of tagged gifts, about $28\%$, is well below her prior share of $45\%$, while Jane's rises from $35\%$ to about $54\%$. The observation of a tag therefore shifts belief towards the assistant with the highest tag rate.

### 4.3 Model solution B: a consignment of bulbs

Fifteen bulbs contain five defective ones. Three bulbs are chosen at random without replacement.

(a) Find the probability that none is defective.

(b) Find the probability that exactly one is defective.

(c) Find the probability that at least one is defective.

(d) Given that at least one is defective, find the probability that exactly one is defective.

### 4.4 Solution B: hypergeometric counts with a conditional finish

Step 1. Fix the counting convention. The three bulbs are chosen as an unordered set, so both the numerator and the denominator count unordered selections.

$$
\binom{15}{3} = \frac{15 \times 14 \times 13}{3 \times 2 \times 1} = 455
$$

Marking point M1: the denominator is the number of equally likely selections of three from fifteen.

Step 2. For part (a), all three must come from the ten sound bulbs.

$$
\binom{10}{3} = \frac{10 \times 9 \times 8}{6} = 120, \qquad P(\text{none defective}) = \frac{120}{455} = \frac{24}{91} \approx 0.264
$$

Marking point M2: the product $\binom{10}{3}\binom{5}{0}$ may be written, and the zero factor must be recognised as one.

Step 3. For part (b), choose one of the five defective bulbs and two of the ten sound ones.

$$
\binom{5}{1}\binom{10}{2} = 5 \times 45 = 225, \qquad P(\text{exactly one}) = \frac{225}{455} = \frac{45}{91} \approx 0.495
$$

Marking point M3: the two factors are multiplied, not added, because the choices are made jointly.

Step 4. For part (c), apply the complement rule to the answer of part (a).

$$
P(\text{at least one}) = 1 - \frac{24}{91} = \frac{67}{91} \approx 0.736
$$

Marking point M4: the complement of "at least one defective" is "no defective", which is exactly part (a); the question is designed so that part (a) feeds part (c).

Step 5. For part (d), restrict the sample space to the event "at least one defective", whose probability is $\frac{67}{91}$.

$$
P(\text{exactly one} \mid \text{at least one}) = \frac{45/91}{67/91} = \frac{45}{67} \approx 0.672
$$

Marking point M5: the denominator is the probability of the conditioning event, not one and not $\frac{24}{91}$.

Step 6. Interpret. Almost three quarters of consignments yield at least one defective bulb, and conditional on that event roughly two thirds contain exactly one, so the typical defective consignment in this sample is a near-miss rather than a disaster. The contrast between $0.495$ and $0.672$ measures how much the conditioning information raises the chance of exactly one.

### 4.5 Problem: a conditional probability with a reduced universe

Two fair dice are rolled. Given that at least one die shows a six, find the probability that the total is nine.

### 4.6 Solution: count inside the stated universe

Step 1. State the sample space of ordered pairs, thirty-six outcomes.

Step 2. Identify the conditioning event and count it. The pairs containing at least one six are the six pairs $(6,k)$ for $k = 1, \dots, 6$ and the six pairs $(k,6)$, with $(6,6)$ counted twice.

$$
\lvert \{\text{at least one six}\}\rvert = 6 + 6 - 1 = 11
$$

Step 3. Count the favourable outcomes inside that universe. A total of nine with a six requires $(3,6)$ or $(6,3)$.

$$
\lvert \{\text{total nine and at least one six}\}\rvert = 2
$$

Step 4. Form the conditional probability with the reduced denominator.

$$
P(\text{total 9} \mid \text{at least one six}) = \frac{2}{11}
$$

Step 5. Contrast with the unconditional value, which is $4/36 = 1/9$, and note that conditioning raises the probability because a six is a large face. A solution that writes $2/36$ has used the unconditional universe and ignored the information given.

### 4.7 Problem: exclusive or independent, decide with numbers

A card is drawn from a pack of fifty-two. Let $A$ be "the card is a spade" and $B$ be "the card is a heart". Let $C$ be "the card is a king". Decide whether $A$ and $B$ are independent, and whether $A$ and $C$ are independent.

### 4.8 Solution: compute the intersection both ways

Step 1. State the individual probabilities.

$$
P(A) = \frac{13}{52} = \frac{1}{4}, \qquad P(B) = \frac{13}{52} = \frac{1}{4}, \qquad P(C) = \frac{4}{52} = \frac{1}{13}
$$

Step 2. Examine the pair $A$ and $B$. A card cannot be both a spade and a heart, so the intersection is empty.

$$
P(A \cap B) = 0 \ne \frac{1}{16} = P(A)P(B)
$$

The pair is mutually exclusive and therefore dependent, not independent.

Step 3. Examine the pair $A$ and $C$. The intersection is the king of spades, a single card.

$$
P(A \cap C) = \frac{1}{52}, \qquad P(A)P(C) = \frac{1}{4} \times \frac{1}{13} = \frac{1}{52}
$$

Step 4. Conclude. The pair $A$ and $C$ is independent, because suit and rank are assigned independently in a well-shuffled pack, while $A$ and $B$ is exclusive and hence dependent. The two answers illustrate the discrimination the examiner is testing.

### 4.9 Problem: arrangements of a word

The ten letters of the word STATISTICS are arranged at random in a row. Find the number of distinct arrangements, and the probability that the first letter is an S.

### 4.10 Solution: multinomial count, then a ratio

Step 1. Count the letters by kind: three S, three T, two I, one A, one C, and check that they total ten.

$$
3 + 3 + 2 + 1 + 1 = 10
$$

Step 2. Divide the total number of orderings by the factorials of the repeated letters.

$$
\frac{10!}{3!\,3!\,2!} = \frac{3\,628\,800}{6 \times 6 \times 2} = \frac{3\,628\,800}{72} = 50\,400
$$

Step 3. Count the arrangements beginning with S by fixing one S in the first position and arranging the remaining nine letters.

$$
\frac{9!}{2!\,3!\,2!} = \frac{362\,880}{2 \times 6 \times 2} = \frac{362\,880}{24} = 15\,120
$$

Step 4. Divide to obtain the probability.

$$
P(\text{first letter S}) = \frac{15\,120}{50\,400} = 0.3 = \frac{3}{10}
$$

Step 5. Interpret. The answer equals the proportion of S among the ten letters, which is the general rule for a uniformly random arrangement: the first position is occupied by each letter with probability equal to its relative frequency. Agreement with that shortcut is a useful check on the factorial arithmetic.

### 4.11 Problem: a three-event union in an examination setting

In a class of $40$ students, $22$ study History, $18$ study Geography, $14$ study Economics, $9$ study History and Geography, $6$ study Geography and Economics, $7$ study History and Economics, and $3$ study all three. Find the probability that a randomly chosen student studies at least one of the three, and the probability that the student studies none.

### 4.12 Solution: inclusion and exclusion, then a complement

Step 1. Record the counts with clear symbols.

$$
\lvert H\rvert = 22, \quad \lvert G\rvert = 18, \quad \lvert E\rvert = 14, \quad \lvert H \cap G\rvert = 9, \quad \lvert G \cap E\rvert = 6, \quad \lvert H \cap E\rvert = 7, \quad \lvert H \cap G \cap E\rvert = 3
$$

Step 2. Apply the three-event law to the counts.

$$
\lvert H \cup G \cup E\rvert = 22 + 18 + 14 - 9 - 6 - 7 + 3 = 35
$$

Step 3. Convert to a probability by dividing by the class size.

$$
P(\text{at least one}) = \frac{35}{40} = \frac{7}{8}
$$

Step 4. Obtain the probability of none by the complement rule.

$$
P(\text{none}) = 1 - \frac{7}{8} = \frac{1}{8}
$$

Step 5. Interpret and check. The five students taking none are consistent with the count $40 - 35 = 5$, and the two answers sum to one as they must.

## 5. Mathematical Extensions, Limits, and Common Errors

### 5.1 Trap one: double counting in a union

The commonest arithmetic error in the topic is adding two or three probabilities and stopping. On a die roll with $A = \{2,4,6\}$ and $B = \{4,5,6\}$, adding gives $\frac{1}{2} + \frac{1}{2} = 1$, which would claim that a $1$ or a $3$ is impossible. The correct value is

$$
P(A \cup B) = \frac{1}{2} + \frac{1}{2} - \frac{1}{3} = \frac{2}{3}
$$

because the outcomes $4$ and $6$ were counted twice. In a three-category survey the error compounds: adding the three headline figures can exceed the population, and the pairwise subtractions plus the triple restoration are what repair it. Whenever an addition produces a value above one, the overlap has been ignored.

### 5.2 Trap two: confusing exclusive with independent

Exclusive events are disjoint, so their intersection has probability zero. Independent events factor, so their intersection has probability equal to a product of positive numbers. For events of positive probability the two descriptions contradict each other, and an answer that uses both is incoherent.

The discriminating question is always the same: can the two events happen together? If the answer is no, they are exclusive and dependent; the multiplication law must not be used. If the answer is yes, compute $P(A \cap B)$ and compare it with $P(A)P(B)$ before deciding anything. A pair of independent events with a non-empty intersection is entirely normal: two dice both showing six is one outcome out of thirty-six, and the events are independent even though the intersection is not empty.

### 5.3 Trap three: misreading "at least one"

"At least one" means one or more, and its complement is "none", never "not exactly one". For three tosses of a coin the probability of at least one head is

$$
1 - \left(\frac{1}{2}\right)^{3} = \frac{7}{8}
$$

while the probability of exactly one head is $\frac{3}{8}$. Confusing the two changes the answer by a factor of more than two. The same care applies to "at most one", whose complement is "at least two", and to "at least two", whose complement is "at most one".

### 5.4 Trap four: forgetting to shrink the universe

A conditional probability divides by the probability of the conditioning event. For two dice, the probability that the total is nine given that at least one die shows six is

$$
\frac{2}{11}
$$

not $\frac{2}{36}$ and not $\frac{2}{4}$, since the conditional universe contains eleven outcomes and only two of them total nine. The habit that prevents the error is to write the conditioning event as the denominator explicitly, in symbols, before substituting any number.

### 5.5 Trap five: mixing ordered and unordered counts

If the denominator counts unordered selections, the numerator must count unordered selections too. Choosing three bulbs from fifteen, the denominator is $\binom{15}{3} = 455$; a numerator written as $5 \times 10 \times 9 = 450$ counts ordered choices and is therefore wrong by a factor of two, since it treats the order of the two sound bulbs as significant while the denominator does not.

### 5.6 Trap six: reversing a conditional probability

$P(A \mid B)$ and $P(B \mid A)$ are different numbers unless the two probabilities are equal. In a test with a rare disease, the probability of a positive result given disease may be $0.99$ while the probability of disease given a positive result is about $0.09$. Bayes' theorem exists precisely to convert one into the other, and quoting the first as the answer to the second is the error the theorem is designed to prevent.

### 5.7 Limits of the methods taught here

Three limits are worth stating because examiners sometimes probe them. First, the classical formula requires equal likelihood, which is a modelling assumption rather than a theorem; where symmetry fails, the ratio of counts is meaningless. Second, the chain rule requires the conditioning events to have positive probability, so an event of probability zero cannot serve as a condition. Third, the law of total probability requires a genuine partition; a collection that overlaps or leaves a gap produces a sum that is either too large or too small, and the only defence is to verify the two defining properties explicitly.

The counting methods also have a limit of practicality. Enumeration of $36$ outcomes is reasonable; enumeration of $\binom{52}{5}$ is not, and the hypergeometric formula replaces it. Choosing between enumeration and formula is a matter of judgement, and the safe rule is to enumerate only when the sample space has at most a few dozen outcomes.

### 5.8 Revision checklist

Work through the list until every item can be done without notes.

- State the three axioms and derive the complement rule, monotonicity, and the difference rule from them.
- State and prove the two-event and three-event addition laws.
- State the multiplication law, the chain rule, the partition identity, and Bayes' theorem, and say which axiom each rests on.
- Write the definitions of mutually exclusive, exhaustive, and independent, and give one numerical example of each.
- Compute $\binom{n}{r}$ and $n!/(n-r)!$ quickly for small $n$, and explain the difference in one sentence.
- Solve one "at least one" problem by the complement rule in under two minutes.
- Complete one Bayes calculation with a three-way partition and verify that the posteriors sum to one.
- Recall the standard sample-space sizes: $2$ for a coin, $8$ for three coins, $36$ for two dice, $52$ for a pack.
- Reproduce the hypergeometric formula and use it for four cases that sum to one.
- Identify, in a written solution, the exact sentence at which the conditional universe is introduced.

### 5.9 Time strategy in the examination

Divide the available time by the marks, and spend approximately one minute per mark with a reserve of five minutes for checking. On a multi-part question, read all parts before starting, because the later parts frequently reuse the value computed in an earlier part; doing so avoids computing the same probability twice.

Allocate the first two minutes of any probability question to writing the sample space and the event definitions, and resist the urge to compute immediately. If a part stalls, leave a clearly labelled expression such as $P(A \mid B) = P(A \cap B)/P(B)$ with the substitution shown, since method marks are awarded independently of the final arithmetic. Finish by running the three checks of Section 2.4, namely bounds, union at least as large as each part, and partitions summing to one.

### 5.10 Consolidation

This topic rewards recognition over computation. Six question types account for almost every mark: direct counting, unions, intersections, conditionals, case splits, and reversals. Each has a standard opening line and a standard check, and each is derived from the same three axioms through a chain of short proofs. The two ideas that cause the most damage when confused are mutual exclusivity and independence, which are respectively additive and multiplicative conditions and incompatible for events of positive probability, and the conditional universe, which must appear in the denominator of every conditional probability. A candidate who writes the sample space first, names the events, quotes the law with its precondition, and verifies the answer against the bounds and against one will rarely lose more than a single arithmetic mark on any question in this topic.

