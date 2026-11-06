## 1. Foundational Concepts, Definitions, and Axioms

### 1.1 The mathematical setting

Probability theory is built on three objects: a set of possible results, a collection of subsets of that set that we are allowed to measure, and a function that assigns each measurable subset a number between zero and one. For the finite experiments of this course the middle object causes no difficulty, because every subset of a finite set can be measured, so events may simply be defined as arbitrary subsets.

> **Definition (Experiment and outcome).** An experiment is a procedure with a well-defined set of possible results that cannot be predicted in advance. Each single result is an outcome, written $\omega$, and the set of all outcomes is the sample space $S$.

> **Definition (Event).** An event is a subset $A \subseteq S$. The event occurs when the realised outcome $\omega$ belongs to $A$. The certain event is $S$ itself, and the impossible event is the empty set $\varnothing$.

The set-theoretic dictionary is used without further comment throughout: $A \cup B$ is " $A$ or $B$ ", $A \cap B$ is " $A$ and $B$ ", $A' = S \setminus A$ is "not $A$", and $A \subseteq B$ means that the occurrence of $A$ forces the occurrence of $B$. Two events are disjoint, or mutually exclusive, when $A \cap B = \varnothing$. A collection $A_1, \dots, A_k$ is a partition of $S$ when the events are pairwise disjoint and their union is $S$; equivalently, exactly one of them occurs on every realisation.

De Morgan's laws transfer negation across a combination and are used constantly when a complement of a compound event is required:

$$
\left(A \cup B\right)' = A' \cap B', \qquad \left(A \cap B\right)' = A' \cup B'
$$

The first identity says that "neither $A$ nor $B$" is the same statement as "not $A$ and not $B$". The second says that failing to have both is the same as lacking at least one.

### 1.2 The axioms

Probabilities are numbers attached to events by a function $P$ defined on the events of $S$.

> **Axiom 1 (Non-negativity).** For every event $A$, $P(A) \ge 0$.

> **Axiom 2 (Normalisation).** $P(S) = 1$.

> **Axiom 3 (Countable additivity).** If $A_1, A_2, \dots$ are pairwise disjoint events, then

$$
P\left(\bigcup_{i=1}^{\infty} A_i\right) = \sum_{i=1}^{\infty} P\left(A_i\right)
$$

The triple is due to Kolmogorov and replaces every earlier attempt to define probability by a formula. Nothing else is assumed. Finite additivity is the special case in which only finitely many of the events are non-empty, and it is the form used in every calculation in this note.

From the axioms several properties follow immediately, and each is proved in Section 3 rather than asserted.

- $P(\varnothing) = 0$, so impossibility has probability zero.
- $P(A') = 1 - P(A)$ for every event $A$.
- $0 \le P(A) \le 1$ for every event $A$.
- If $A \subseteq B$ then $P(A) \le P(B)$.
- $P(A \setminus B) = P(A) - P(A \cap B)$.
- $P(A \cup B) = P(A) + P(B) - P(A \cap B)$.

### 1.3 The classical formula and its justification

The classical definition is the one that makes counting sufficient.

> **Definition (Equally likely outcomes).** A finite sample space $S$ has equally likely outcomes when $P(\{\omega\}) = 1/\lvert S\rvert$ for every outcome $\omega$.

Under that assumption, additivity gives the counting formula at once, because an event is the disjoint union of its individual outcomes:

$$
P(A) = \sum_{\omega \in A} P\left(\{\omega\}\right) = \sum_{\omega \in A} \frac{1}{\lvert S\rvert} = \frac{\lvert A\rvert}{\lvert S\rvert}
$$

Hence, for a finite equiprobable space,

$$
P(A) = \frac{\text{number of favourable outcomes}}{\text{total number of outcomes}} = \frac{\lvert A\rvert}{\lvert S\rvert}
$$

The formula is a theorem under the equal-likelihood assumption, not a definition, and the assumption must be justified by a symmetry argument: a fair die has six congruent faces, a well-shuffled pack treats every card alike, and a well-mixed urn gives every ball the same chance. When no symmetry argument is available the classical formula does not apply, and one of the other interpretations must be used.

### 1.4 Three interpretations of the number $P(A)$

> **Definition (Classical interpretation).** Probability is the ratio of favourable to total outcomes in an equiprobable space. Its scope is limited to situations with a demonstrable symmetry.

> **Definition (Relative-frequency interpretation).** For an event $A$ observed $f_n$ times in $n$ independent repetitions, the relative frequency is $f_n/n$, and the probability is interpreted as the value that this ratio approaches as $n$ grows:

$$
P(A) = \lim_{n \to \infty} \frac{f_n}{n}
$$

> **Definition (Subjective interpretation).** Probability is a degree of belief held by an agent, required to be coherent: the agent's odds must not permit a bet that loses whatever happens. Coherence forces the belief to obey the same three axioms, so the mathematics is unchanged while the source of the number becomes judgement rather than counting.

The relative-frequency reading needs a limiting statement, and the precise form of that statement is provided later by the law of large numbers, which says that under independence the relative frequency converges to the true probability in a suitable sense. The subjective reading is the one that licenses probability statements about single unrepeatable events, and it is updated by Bayes' theorem when evidence arrives. All three readings share the same algebra, which is exactly why the axiomatic approach is worth the abstraction.

### 1.5 Conditional probability

> **Definition (Conditional probability).** For events $A$ and $B$ with $P(B) > 0$,

$$
P(A \mid B) = \frac{P(A \cap B)}{P(B)}
$$

The definition is not a convention chosen for convenience; it is forced by the requirement that, once $B$ is known, the conditional probabilities should themselves be probabilities on the reduced sample space. Define $Q(A) = P(A \mid B)$ for events $A$. Then $Q(A) \ge 0$, and

$$
Q(S) = \frac{P(S \cap B)}{P(B)} = \frac{P(B)}{P(B)} = 1
$$

and for disjoint $A_1, A_2$ the identity $(A_1 \cup A_2) \cap B = (A_1 \cap B) \cup (A_2 \cap B)$ is a disjoint union, so additivity passes through the division. Thus $Q$ satisfies the three axioms and deserves the name of a probability.

In an equiprobable finite space the definition reduces to a ratio of counts, which is the computational form used in almost every exercise:

$$
P(A \mid B) = \frac{\lvert A \cap B\rvert / \lvert S\rvert}{\lvert B\rvert / \lvert S\rvert} = \frac{\lvert A \cap B\rvert}{\lvert B\rvert}
$$

The denominator is the size of the conditional universe. Replacing it by $\lvert S\rvert$ is the single most frequent error in conditional-probability questions, and it produces a number that is too small whenever $B$ is a proper subset of $S$.

### 1.6 Independence

> **Definition (Independence of two events).** Events $A$ and $B$ are independent when

$$
P(A \cap B) = P(A)\,P(B)
$$

When $P(B) > 0$ this is equivalent to $P(A \mid B) = P(A)$, and when $P(A) > 0$ it is equivalent to $P(B \mid A) = P(B)$. The product form is preferred as the definition because it remains meaningful when one of the probabilities is zero.

Three remarks prevent most errors. First, independence is a property of the probability assignment, not of the physical arrangement: two events may be independent under one model and dependent under another, so it must be verified or justified, never assumed because the events look unrelated. Second, an event of probability zero or one is independent of every event, since the product identity then holds automatically. Third, independence of a whole collection is stronger than pairwise independence, and the difference is illustrated in Section 5.

> **Definition (Mutual independence).** Events $A_1, \dots, A_n$ are mutually independent when, for every sub-collection $A_{i_1}, \dots, A_{i_r}$ with $r \ge 2$,

$$
P\left(A_{i_1} \cap \cdots \cap A_{i_r}\right) = P\left(A_{i_1}\right) \cdots P\left(A_{i_r}\right)
$$

For three events this requires four identities: the three pairwise products and the triple product. Satisfying only the pairwise ones is called pairwise independence, and it does not imply mutual independence.

### 1.7 Counting: the tools that feed the formula

> **Principle (Multiplication principle).** If a first stage can be completed in $m$ ways and, for each of them, a second stage in $n$ ways, then the two stages together can be completed in $mn$ ways. Applied repeatedly it gives $n_1 n_2 \cdots n_k$ for $k$ stages.

> **Definition (Permutation).** A permutation of $n$ distinct objects is an arrangement in a definite order. The number of such arrangements is

$$
n! = n(n-1)(n-2)\cdots 2 \cdot 1, \qquad 0! = 1
$$

> **Definition (Ordered selection).** The number of ordered arrangements of $r$ objects chosen from $n$ distinct objects is

$$
{}^{n}P_{r} = \frac{n!}{(n-r)!} = n(n-1)\cdots(n-r+1)
$$

> **Definition (Combination).** The number of unordered selections of $r$ objects from $n$ distinct objects is

$$
\binom{n}{r} = \frac{n!}{r!\,(n-r)!}
$$

The combination symbol counts sets, not sequences. The factor $r!$ in the denominator is exactly the number of orders in which a fixed set of $r$ objects can be listed, so dividing converts ordered arrangements into sets.

| Sampling scheme | Ordered? | Replacement? | Number of outcomes |
|---|---|---|---|
| Ordered, with replacement | yes | yes | $n^{r}$ |
| Ordered, without replacement | yes | no | $\frac{n!}{(n-r)!}$ |
| Unordered, without replacement | no | no | $\binom{n}{r}$ |
| Unordered, with replacement | no | yes | $\binom{n+r-1}{r}$ |

Only the first three rows are needed in this course, but the fourth completes the pattern and is useful when identical items are distributed among distinct boxes.

Two identities are used repeatedly. The symmetry identity states that choosing $r$ objects to keep is the same as choosing $n-r$ objects to discard:

$$
\binom{n}{r} = \binom{n}{n-r}
$$

Pascal's identity splits the selections according to whether one distinguished object is included:

$$
\binom{n}{r} = \binom{n-1}{r-1} + \binom{n-1}{r}
$$

Both are proved in Section 3 by counting the same collection in two ways, which is the standard technique of combinatorial proof.

### 1.8 Structured sample spaces

A compound experiment built from independent stages has a product sample space whose size is the product of the stage sizes. Two dice give $6 \times 6 = 36$ outcomes, three coins give $2^{3} = 8$, and a two-card deal from a pack of fifty-two gives $52 \times 51 = 2652$ ordered outcomes.

The choice between describing a sample space as ordered or unordered is free, but it must be consistent. If the denominator counts unordered selections then the numerator must also count unordered selections, because the ratio is only meaningful when the same convention governs both. The next section states the results that convert these counts into probabilities, and each statement is followed by a derivation from the axioms.

## 2. Theorems, Lemmas, and Analytical Properties

### 2.1 Elementary consequences of the axioms

> **Theorem (Probability of the impossible event).** $P(\varnothing) = 0$.

> **Theorem (Complement rule).** For every event $A$,

$$
P(A') = 1 - P(A)
$$

> **Theorem (Bounds).** For every event $A$, $0 \le P(A) \le 1$.

> **Theorem (Monotonicity).** If $A \subseteq B$ then $P(A) \le P(B)$.

> **Theorem (Difference rule).** For any events $A$ and $B$,

$$
P(A \setminus B) = P(A) - P(A \cap B)
$$

The difference rule is the tool for questions of the form " $A$ but not $B$ ", and its immediate corollary is that $P(A \cap B') = P(A) - P(A \cap B)$.

### 2.2 The addition law

> **Theorem (Addition law for two events).** For any events $A$ and $B$ in the same sample space,

$$
P(A \cup B) = P(A) + P(B) - P(A \cap B)
$$

> **Theorem (Addition law for three events).** For any events $A$, $B$, $C$,

$$
P(A \cup B \cup C) = P(A) + P(B) + P(C) - P(A \cap B) - P(A \cap C) - P(B \cap C) + P(A \cap B \cap C)
$$

> **Theorem (Inclusion and exclusion, general form).** For events $A_1, \dots, A_n$,

$$
P\left(\bigcup_{i=1}^{n} A_i\right) = \sum_{i} P\left(A_i\right) - \sum_{i<j} P\left(A_i \cap A_j\right) + \sum_{i<j<k} P\left(A_i \cap A_j \cap A_k\right) - \cdots + (-1)^{n-1} P\left(A_1 \cap \cdots \cap A_n\right)
$$

> **Corollary (Boole's inequality).** For any events $A_1, \dots, A_n$,

$$
P\left(\bigcup_{i=1}^{n} A_i\right) \le \sum_{i=1}^{n} P\left(A_i\right)
$$

with equality when the events are pairwise disjoint. Boole's inequality is the workhorse of the union-bound arguments used in reliability and in the birthday problem.

### 2.3 The multiplication law and the chain rule

> **Theorem (Multiplication law).** For events $A$ and $B$ with $P(B) > 0$,

$$
P(A \cap B) = P(B)\,P(A \mid B)
$$

> **Theorem (Chain rule).** For events $A_1, \dots, A_n$ with $P\left(A_1 \cap \cdots \cap A_{n-1}\right) > 0$,

$$
P\left(A_1 \cap A_2 \cap \cdots \cap A_n\right) = P\left(A_1\right) P\left(A_2 \mid A_1\right) P\left(A_3 \mid A_1 \cap A_2\right) \cdots P\left(A_n \mid A_1 \cap \cdots \cap A_{n-1}\right)
$$

The chain rule is the correct instrument for sequential drawing without replacement, because each factor is computed in the world left by the preceding draws. Every factor after the first has a conditional bar, and omitting the conditioning is the error that produces the "with replacement" answer for a "without replacement" question.

### 2.4 The partition identity

> **Theorem (Law of total probability).** Let $A_1, \dots, A_k$ be a partition of $S$ with $P\left(A_i\right) > 0$ for every $i$. Then for any event $B$,

$$
P(B) = \sum_{i=1}^{k} P\left(B \mid A_i\right) P\left(A_i\right)
$$

Two-event and three-event versions are the ones used in exercises. The identity converts an unconditional probability into a weighted average of conditional probabilities, with the probabilities of the cases as weights. Whenever a problem describes a two-stage experiment, with a first stage that selects a case and a second stage that produces an observation, the partition identity computes the probability of the observation.

### 2.5 Bayes' theorem

> **Theorem (Bayes' theorem).** Under the hypotheses of the partition identity, and with $P(B) > 0$,

$$
P\left(A_j \mid B\right) = \frac{P\left(B \mid A_j\right) P\left(A_j\right)}{\sum_{i=1}^{k} P\left(B \mid A_i\right) P\left(A_i\right)}
$$

The numerator is the probability of reaching $B$ through the particular case $A_j$, and the denominator is the total probability of reaching $B$ by any route. Because the denominator is a sum over all cases, the posterior probabilities computed for every $j$ add to one, which is the standard check on a Bayes calculation.

### 2.6 Properties of independence

> **Theorem (Independence of the complement).** If $A$ and $B$ are independent, then $A$ and $B'$ are independent, as are $A'$ and $B$, and $A'$ and $B'$.

> **Lemma (Independence passes to sub-events).** If $A$ is independent of $B$, and $C \subseteq A$, then $C$ need not be independent of $B$; independence is not inherited by subsets in general. What is inherited is independence of the events $A$ and $B$ under the replacement of either by its complement.

> **Lemma (Disjoint events with positive probability are dependent).** If $A \cap B = \varnothing$ with $P(A) > 0$ and $P(B) > 0$, then

$$
P(A \cap B) = 0 \ne P(A)P(B)
$$

so the pair is dependent. In fact $P(A \mid B) = 0$, meaning that $B$ rules $A$ out entirely.

That last lemma is the formal statement of the confusion discussed at length in Section 5: mutual exclusivity is a statement about impossibility of joint occurrence, independence is a statement about multiplicative structure, and the two can coexist only in the degenerate case where one of the probabilities is zero.

### 2.7 Counting theorems

> **Theorem (Combination formula).** The number of $r$-element subsets of an $n$-element set is $n!/(r!(n-r)!)$.

> **Theorem (Binomial theorem).** For any real $x$ and $y$ and any non-negative integer $n$,

$$
(x+y)^{n} = \sum_{r=0}^{n} \binom{n}{r} x^{r} y^{n-r}
$$

> **Corollary (Total number of subsets).** A set with $n$ elements has $2^{n}$ subsets, since setting $x = y = 1$ gives $\sum_{r} \binom{n}{r} = 2^{n}$.

> **Theorem (Multinomial count).** The number of distinct arrangements of $n$ objects of which $n_1$ are of one kind, $n_2$ of a second kind, and so on, is

$$
\frac{n!}{n_1!\,n_2! \cdots n_k!}
$$

where $n_1 + n_2 + \cdots + n_k = n$.

The multinomial count is the right tool for questions about the letters of a word or the arrangements of indistinguishable balls, and it reduces to the binomial coefficient when there are only two kinds.

### 2.8 A lemma behind the birthday argument

> **Lemma (Complement of a repeated-event condition).** Let $E$ be the event that some coincidence occurs among $n$ independent trials. If $E'$ denotes the event that all $n$ results are distinct, then

$$
P(E) = 1 - P(E') = 1 - \prod_{j=0}^{n-1} \frac{N-j}{N}
$$

where $N$ is the number of equally likely labels available.

The lemma is simply the complement rule combined with the chain rule, and it is the standard route whenever a question contains the words "at least two alike" or "at least one". Direct enumeration of $E$ would require counting every possible pattern of coincidences, whereas $E'$ has a product structure and is therefore easy.

## 3. Formal Proofs, Derivations, and Methods

### 3.1 Proof that the empty set has probability zero

The events $S$ and $\varnothing$ are disjoint and their union is $S$. Applying Axiom 3 to the two-term sequence $S, \varnothing, \varnothing, \dots$ gives

$$
P(S) = P(S \cup \varnothing) = P(S) + P(\varnothing)
$$

and since $P(S) = 1$ by Axiom 2, subtracting the finite quantity $P(S)$ from both sides yields $P(\varnothing) = 0$. Note that the argument needs $P(S)$ to be finite, which Axiom 2 guarantees.

### 3.2 Finite additivity by induction

> **Proposition.** If $A_1, \dots, A_n$ are pairwise disjoint then $P\left(A_1 \cup \cdots \cup A_n\right) = \sum_{i=1}^{n} P\left(A_i\right)$.

For $n = 2$ the statement is Axiom 3. Suppose it holds for $n - 1$. The union of the first $n - 1$ events is disjoint from $A_n$, because disjointness is pairwise, so Axiom 3 applies to the pair consisting of that union and $A_n$:

$$
P\left(A_1 \cup \cdots \cup A_n\right) = P\left(A_1 \cup \cdots \cup A_{n-1}\right) + P\left(A_n\right)
$$

Applying the induction hypothesis to the first term gives the sum of all $n$ probabilities. The result is therefore established for every finite $n$.

### 3.3 Proof of the complement rule

The events $A$ and $A'$ are disjoint, since no outcome can lie both inside and outside $A$, and their union is $S$. Finite additivity gives

$$
P(A) + P(A') = P\left(A \cup A'\right) = P(S) = 1
$$

Rearranging,

$$
P(A') = 1 - P(A)
$$

Two corollaries follow at once. Since $P(A') \ge 0$ by Axiom 1, we obtain $P(A) \le 1$, which with Axiom 1 gives the bounds $0 \le P(A) \le 1$. And since $A \subseteq B$ implies $B = A \cup \left(B \cap A'\right)$ with the two pieces disjoint,

$$
P(B) = P(A) + P\left(B \cap A'\right) \ge P(A)
$$

which is monotonicity.

### 3.4 Proof of the difference rule

The event $A$ splits into the part inside $B$ and the part outside $B$:

$$
A = \left(A \cap B\right) \cup \left(A \cap B'\right)
$$

The two pieces are disjoint, so additivity applies:

$$
P(A) = P(A \cap B) + P\left(A \cap B'\right)
$$

Hence $P\left(A \cap B'\right) = P(A) - P(A \cap B)$, which is the difference rule written in the form used most often.

### 3.5 Proof of the two-event addition law

Decompose the union into two disjoint pieces, namely the whole of $A$ and the part of $B$ that lies outside $A$:

$$
A \cup B = A \cup \left(B \cap A'\right)
$$

Additivity gives

$$
P(A \cup B) = P(A) + P\left(B \cap A'\right)
$$

and the difference rule applied to $B$ gives $P\left(B \cap A'\right) = P(B) - P(A \cap B)$. Substituting,

$$
P(A \cup B) = P(A) + P(B) - P(A \cap B)
$$

A second proof uses inclusion and exclusion on the three disjoint pieces $A \cap B'$, $A \cap B$, and $A' \cap B$, whose union is $A \cup B$ and whose probabilities sum to $P(A) + P(B) - P(A \cap B)$ after regrouping. Both arguments are accepted; the first is shorter.

### 3.6 Proof of the three-event addition law

Apply the two-event law to the pair $A \cup B$ and $C$:

$$
P(A \cup B \cup C) = P(A \cup B) + P(C) - P\left((A \cup B) \cap C\right)
$$

Distributivity of intersection over union converts the last term:

$$
(A \cup B) \cap C = (A \cap C) \cup (B \cap C)
$$

so the two-event law applies once more to that union:

$$
P\left((A \cup B) \cap C\right) = P(A \cap C) + P(B \cap C) - P(A \cap B \cap C)
$$

Substituting both expressions and expanding $P(A \cup B)$ gives the three-event law. The pattern of signs, add single events, subtract pairs, add the triple, is the general inclusion and exclusion rule, which is proved by the same induction step for any number of events.

### 3.7 Proof of the chain rule

The multiplication law states $P(A \cap B) = P(B) P(A \mid B)$. Apply it to the pair consisting of $A_1 \cap \cdots \cap A_{n-1}$ and $A_n$:

$$
P\left(A_1 \cap \cdots \cap A_n\right) = P\left(A_1 \cap \cdots \cap A_{n-1}\right) P\left(A_n \mid A_1 \cap \cdots \cap A_{n-1}\right)
$$

Repeating the substitution on the first factor produces the full product of conditional probabilities. The hypothesis that $P\left(A_1 \cap \cdots \cap A_{n-1}\right) > 0$ ensures that every conditional probability in the product is defined, since each conditioning event then also has positive probability by monotonicity.

### 3.8 Proof of the law of total probability

Because $A_1, \dots, A_k$ partition $S$, every outcome of $B$ lies in exactly one $A_i$, so

$$
B = \left(B \cap A_1\right) \cup \left(B \cap A_2\right) \cup \cdots \cup \left(B \cap A_k\right)
$$

is a union of pairwise disjoint events. Finite additivity and then the multiplication law give

$$
P(B) = \sum_{i=1}^{k} P\left(B \cap A_i\right) = \sum_{i=1}^{k} P\left(B \mid A_i\right) P\left(A_i\right)
$$

The identity remains valid when some $P\left(A_i\right) = 0$ provided the corresponding conditional probability is defined arbitrarily, or the term is omitted, since that term then contributes nothing.

### 3.9 Proof of Bayes' theorem

By the definition of conditional probability,

$$
P\left(A_j \mid B\right) = \frac{P\left(A_j \cap B\right)}{P(B)}
$$

The multiplication law rewrites the numerator as $P\left(B \mid A_j\right) P\left(A_j\right)$, and the partition identity rewrites the denominator as the sum over $i$. Substituting,

$$
P\left(A_j \mid B\right) = \frac{P\left(B \mid A_j\right) P\left(A_j\right)}{\sum_{i=1}^{k} P\left(B \mid A_i\right) P\left(A_i\right)}
$$

Summing the right-hand side over $j$ returns $P(B)/P(B) = 1$, which is the algebraic reason the posteriors form a probability distribution over the cases.

### 3.10 Proof that independence is preserved by complements

Assume $P(A \cap B) = P(A)P(B)$. The difference rule gives

$$
P\left(A \cap B'\right) = P(A) - P(A \cap B) = P(A) - P(A)P(B) = P(A)\left(1 - P(B)\right) = P(A)P\left(B'\right)
$$

so $A$ and $B'$ are independent. Applying the same argument with the roles reversed gives independence of $A'$ and $B$, and applying it twice gives independence of $A'$ and $B'$. The proof uses only the difference rule and the complement rule, so it inherits the axioms directly.

### 3.11 Derivation of the combination formula and two identities

Count the ordered selections of $r$ objects from $n$ in two ways. Directly, there are $n(n-1)\cdots(n-r+1) = n!/(n-r)!$ of them. Alternatively, first choose the set of $r$ objects and then order it; if $C$ denotes the number of sets, then

$$
\frac{n!}{(n-r)!} = C \cdot r!
$$

because each set can be ordered in $r!$ ways. Dividing gives

$$
C = \binom{n}{r} = \frac{n!}{r!\,(n-r)!}
$$

Pascal's identity follows by classifying the $r$-element subsets of an $n$-element set according to whether a distinguished element $x$ is included. Subsets containing $x$ correspond to choosing $r-1$ further elements from the remaining $n-1$, giving $\binom{n-1}{r-1}$; subsets excluding $x$ are $r$-element subsets of the remaining $n-1$, giving $\binom{n-1}{r}$. The two classes are disjoint and exhaustive, so the counts add.

The binomial theorem follows by counting the choices that produce $x^{r} y^{n-r}$ in the expansion of $(x+y)^{n}$: each of the $n$ factors contributes either an $x$ or a $y$, and the term arises from exactly those choices in which $r$ factors contribute $x$, of which there are $\binom{n}{r}$.

### 3.12 Method: selection without replacement

When $n$ objects are drawn without replacement from a population of $N$ objects of which $K$ possess a property, the number of draws possessing the property follows the hypergeometric count. The probability of exactly $k$ successes is

$$
P(X = k) = \frac{\binom{K}{k}\binom{N-K}{n-k}}{\binom{N}{n}}
$$

The numerator counts unordered favourable selections: choose $k$ of the $K$ marked objects and $n-k$ of the $N-K$ unmarked ones. The denominator counts all unordered selections of $n$. The same answer is obtained from the chain rule, and checking one route against the other is the best defence against arithmetic error.

### 3.13 Method: the at-least-one argument

For any event $E$ described as "at least one occurrence", the complement $E'$ is "no occurrence". The complement is a conjunction of independent failures, so the chain rule applies to it as a product. Hence

$$
P(\text{at least one}) = 1 - P(\text{none}) = 1 - \prod_{j=1}^{n} P\left(\text{failure on trial } j\right)
$$

With constant failure probability $q$ the product is $q^{n}$, giving $1 - q^{n}$. For sampling without replacement from a finite population the product is a ratio of combinations instead, and the rule is applied as

$$
P(\text{at least one marked}) = 1 - \frac{\binom{N-K}{n}}{\binom{N}{n}}
$$

Both forms are consequences of the same complement identity; only the computation of $P(\text{none})$ changes.

## 4. Representative Worked Examples and Solutions

### 4.1 Problem: completing a probability table from three values

Events $A$ and $B$ satisfy $P(A) = \frac{1}{3}$, $P(B) = \frac{1}{4}$, and $P(A \cup B) = \frac{1}{2}$. Find $P(A \cap B)$, $P(A \mid B)$, $P(B \mid A)$, and $P(A \mid B')$, and decide whether $A$ and $B$ are independent.

### 4.2 Solution: recover the intersection, then condition

Step 1. Rearrange the addition law to isolate the intersection.

$$
P(A \cap B) = P(A) + P(B) - P(A \cup B)
$$

Step 2. Substitute with a common denominator of twelve.

$$
P(A \cap B) = \frac{4}{12} + \frac{3}{12} - \frac{6}{12} = \frac{1}{12}
$$

Step 3. Apply the definition of conditional probability in the direction $A$ given $B$.

$$
P(A \mid B) = \frac{P(A \cap B)}{P(B)} = \frac{1/12}{1/4} = \frac{1}{3}
$$

Step 4. Apply it in the other direction.

$$
P(B \mid A) = \frac{P(A \cap B)}{P(A)} = \frac{1/12}{1/3} = \frac{1}{4}
$$

Step 5. Prepare the pieces for $P(A \mid B')$, using the difference rule and the complement rule.

$$
P\left(A \cap B'\right) = P(A) - P(A \cap B) = \frac{1}{3} - \frac{1}{12} = \frac{1}{4}, \qquad P(B') = 1 - \frac{1}{4} = \frac{3}{4}
$$

Step 6. Divide.

$$
P\left(A \mid B'\right) = \frac{1/4}{3/4} = \frac{1}{3}
$$

Step 7. Test independence by comparing the product with the intersection.

$$
P(A)P(B) = \frac{1}{3} \times \frac{1}{4} = \frac{1}{12} = P(A \cap B)
$$

The events are independent, which explains the identical values in Steps 3, 4, and 6: conditioning on $B$, on $A$, or on the failure of $B$ leaves the probability of $A$ unchanged at one third.

### 4.3 Problem: testing independence on two dice

Two fair dice are rolled. Let $A$ be the event that the total is odd, and let $B$ be the event that the total is $9$, $11$, or $12$. Are $A$ and $B$ independent?

### 4.4 Solution: count all three quantities

Step 1. State the sample space as ordered pairs, with thirty-six equally likely outcomes.

Step 2. Count the odd totals. A total is odd exactly when the two faces have opposite parity, so there are $3 \times 3 = 9$ pairs with an odd first face and an even second, and $9$ with an even first and an odd second.

$$
P(A) = \frac{18}{36} = \frac{1}{2}
$$

Step 3. Count the totals in $B$. A total of $9$ arises from $(3,6)$, $(4,5)$, $(5,4)$, $(6,3)$; a total of $11$ from $(5,6)$, $(6,5)$; a total of $12$ from $(6,6)$. That is seven outcomes.

$$
P(B) = \frac{7}{36}
$$

Step 4. Count the intersection. Of the seven outcomes in $B$, those with an odd total are the four giving $9$ and the two giving $11$, since $12$ is even.

$$
P(A \cap B) = \frac{6}{36} = \frac{1}{6}
$$

Step 5. Compare the product with the intersection.

$$
P(A)P(B) = \frac{1}{2} \times \frac{7}{36} = \frac{7}{72}, \qquad P(A \cap B) = \frac{12}{72}
$$

Step 6. Conclude. Since $\frac{7}{72} \ne \frac{12}{72}$, the events are dependent. The direction of the dependence is also readable: conditional on a large total, an odd total is more likely than one half, because the two largest qualifying totals are odd.

### 4.5 Problem: conditioning on the age of a child

A family with two children is chosen at random, with the sex of each child independent and equally likely. Compute the probability that both children are girls, given that the older child is a girl, and given instead that at least one child is a girl.

### 4.6 Solution: two different conditional universes

Step 1. Write the sample space in birth order.

$$
S = \{bb, bg, gb, gg\}
$$

Step 2. Name the events.

$$
E_1 = \{\text{older child is a girl}\} = \{gb, gg\}, \qquad E_2 = \{\text{at least one girl}\} = \{bg, gb, gg\}, \qquad E_3 = \{gg\}
$$

Step 3. Compute the conditional probability given $E_1$, whose size is two.

$$
P(E_3 \mid E_1) = \frac{\lvert E_3 \cap E_1\rvert}{\lvert E_1\rvert} = \frac{1}{2}
$$

Step 4. Compute the conditional probability given $E_2$, whose size is three.

$$
P(E_3 \mid E_2) = \frac{\lvert E_3 \cap E_2\rvert}{\lvert E_2\rvert} = \frac{1}{3}
$$

Step 5. Interpret. Both questions have the same numerator and different denominators, because the information received differs. "The older child is a girl" removes two outcomes; "at least one child is a girl" removes only one, since it permits either order. The conditional universe, not the intersection, decides the answer.

### 4.7 Problem: defective items from three stores

Three stores each supply a batch of items in equal quantity, and $10\%$, $20\%$, and $30\%$ of the batches respectively are defective. A customer chooses a store at random and then an item at random from that store. Find the probability that the item is defective, and the probability that a defective item came from each store.

### 4.8 Solution: partition identity followed by Bayes' theorem

Step 1. Define the partition. Let $E_i$ be the event that store $i$ is chosen, for $i = 1, 2, 3$, and let $D$ be the event that the item is defective.

$$
P\left(E_1\right) = P\left(E_2\right) = P\left(E_3\right) = \frac{1}{3}
$$

Step 2. Record the conditional defect probabilities.

$$
P\left(D \mid E_1\right) = 0.1, \qquad P\left(D \mid E_2\right) = 0.2, \qquad P\left(D \mid E_3\right) = 0.3
$$

Step 3. Apply the partition identity.

$$
P(D) = \frac{1}{3}(0.1) + \frac{1}{3}(0.2) + \frac{1}{3}(0.3) = \frac{0.6}{3} = 0.2
$$

Step 4. Apply Bayes' theorem to the first store.

$$
P\left(E_1 \mid D\right) = \frac{(0.1)(1/3)}{0.2} = \frac{1}{6}
$$

Step 5. Apply it to the second and third stores.

$$
P\left(E_2 \mid D\right) = \frac{(0.2)(1/3)}{0.2} = \frac{1}{3}, \qquad P\left(E_3 \mid D\right) = \frac{(0.3)(1/3)}{0.2} = \frac{1}{2}
$$

Step 6. Check that the posteriors sum to one.

$$
\frac{1}{6} + \frac{1}{3} + \frac{1}{2} = 1
$$

Step 7. Interpret. The prior probabilities were equal, so the posteriors are proportional to the defect rates, and no store is favoured beyond what its own rate justifies.

### 4.9 Problem: two urns and a posterior probability

Urn $A$ contains three red and one white ball; urn $B$ contains one red and three white balls. An urn is selected with probability $\frac{2}{3}$ for $A$ and $\frac{1}{3}$ for $B$, and one ball is drawn. A red ball appears. Find the probability that urn $A$ was used.

### 4.10 Solution: weighted average in the denominator

Step 1. State the priors and the conditional probabilities of red.

$$
P(A) = \frac{2}{3}, \quad P(B) = \frac{1}{3}, \quad P(R \mid A) = \frac{3}{4}, \quad P(R \mid B) = \frac{1}{4}
$$

Step 2. Compute the joint probabilities of each route to red.

$$
P(R \cap A) = \frac{3}{4} \times \frac{2}{3} = \frac{1}{2}, \qquad P(R \cap B) = \frac{1}{4} \times \frac{1}{3} = \frac{1}{12}
$$

Step 3. Add them to obtain the total probability of red.

$$
P(R) = \frac{1}{2} + \frac{1}{12} = \frac{7}{12}
$$

Step 4. Divide the route through $A$ by the total.

$$
P(A \mid R) = \frac{1/2}{7/12} = \frac{6}{7}
$$

Step 5. Check the complement.

$$
P(B \mid R) = 1 - \frac{6}{7} = \frac{1}{7} = \frac{1/12}{7/12}
$$

Step 6. Interpret. The prior for urn $A$ was two thirds, and observing red, which is three times more likely under $A$, raises the posterior to six sevenths.

### 4.11 Problem: choosing three bulbs from a consignment

Fifteen bulbs contain five defective ones. Three are chosen at random without replacement. Find the probability that none, exactly one, exactly two, and all three are defective, and the probability that at least one is defective.

### 4.12 Solution: the hypergeometric count

Step 1. Count all equally likely unordered selections of three from fifteen.

$$
\binom{15}{3} = \frac{15 \times 14 \times 13}{6} = 455
$$

Step 2. Count the selection with no defective bulb, which must come from the ten sound bulbs.

$$
\binom{10}{3} = \frac{10 \times 9 \times 8}{6} = 120, \qquad P(\text{none}) = \frac{120}{455} = \frac{24}{91}
$$

Step 3. Count the selections with exactly one defective bulb.

$$
\binom{5}{1}\binom{10}{2} = 5 \times 45 = 225, \qquad P(\text{one}) = \frac{225}{455} = \frac{45}{91}
$$

Step 4. Count the selections with exactly two defective bulbs.

$$
\binom{5}{2}\binom{10}{1} = 10 \times 10 = 100, \qquad P(\text{two}) = \frac{100}{455} = \frac{20}{91}
$$

Step 5. Count the selections with three defective bulbs.

$$
\binom{5}{3} = 10, \qquad P(\text{three}) = \frac{10}{455} = \frac{2}{91}
$$

Step 6. Verify that the four cases exhaust the sample space.

$$
\frac{24 + 45 + 20 + 2}{91} = \frac{91}{91} = 1
$$

Step 7. Apply the complement rule for the last part.

$$
P(\text{at least one}) = 1 - \frac{24}{91} = \frac{67}{91} \approx 0.736
$$

### 4.13 Problem: a birthday coincidence

Find the probability that among twenty-three people at least two share a birthday, treating the three hundred and sixty-five days as equally likely and ignoring leap years.

### 4.14 Solution: complement of all-distinct

Step 1. Write the probability that all twenty-three birthdays differ as a product of conditional probabilities, each computed in the world where the earlier people have distinct birthdays.

$$
P(\text{all distinct}) = \prod_{j=0}^{22} \frac{365 - j}{365}
$$

Step 2. Evaluate the first few factors to see the pattern.

$$
\frac{365}{365} \times \frac{364}{365} \times \frac{363}{365} \times \cdots \times \frac{343}{365}
$$

Step 3. Evaluate the product numerically.

$$
P(\text{all distinct}) \approx 0.4927
$$

Step 4. Apply the complement rule.

$$
P(\text{at least one shared birthday}) = 1 - 0.4927 = 0.5073
$$

Step 5. Interpret. The probability exceeds one half with only twenty-three people because the condition concerns every pair, of which there are $\binom{23}{2} = 253$, not merely the pairs formed with one chosen person. The complement route is the only practicable one, since the event "some pair coincides" is a union of hundreds of overlapping events.

### 4.15 Problem: three overlapping categories in a survey

In a survey of one hundred students, sixty study Mathematics, fifty study Physics, forty study Chemistry, thirty study Mathematics and Physics, twenty study Physics and Chemistry, twenty-five study Mathematics and Chemistry, and ten study all three. Find the number studying at least one subject and the number studying none.

### 4.16 Solution: inclusion and exclusion

Step 1. Record the counts.

$$
\lvert M\rvert = 60, \quad \lvert P\rvert = 50, \quad \lvert C\rvert = 40, \quad \lvert M \cap P\rvert = 30, \quad \lvert P \cap C\rvert = 20, \quad \lvert M \cap C\rvert = 25
$$

Step 2. Apply the three-event law with the triple overlap restored.

$$
\lvert M \cup P \cup C\rvert = 60 + 50 + 40 - 30 - 20 - 25 + 10 = 85
$$

Step 3. Subtract from the total to obtain those studying none.

$$
100 - 85 = 15
$$

Step 4. Interpret. Adding the three headline figures alone gives one hundred and fifty, which overcounts every student taking two subjects and overcounts a student taking three subjects by two more. The alternating signs of inclusion and exclusion are exactly what removes those excess counts.

## 5. Mathematical Extensions, Limits, and Common Errors

### 5.1 Mutual exclusivity and independence are incompatible for positive probabilities

The distinction deserves a formal statement because it is the most common conceptual error in the subject.

> **Proposition.** Let $P(A) > 0$ and $P(B) > 0$. If $A$ and $B$ are mutually exclusive then they are not independent.

The proof is one line: exclusivity gives $P(A \cap B) = 0$, while positivity gives $P(A)P(B) > 0$, so the product identity fails. The same argument in conditional language shows $P(A \mid B) = 0$, which is as far from $P(A)$ as a probability can be.

Numerically the two conditions pull in opposite directions. On a single die roll, $A = \{1,2\}$ and $B = \{5,6\}$ are exclusive, and knowing $B$ occurred reduces the probability of $A$ from one third to zero. Tossing two coins, the events "first coin head" and "second coin head" are independent, and knowing one occurred leaves the probability of the other at one half. In the first case the events compete for the same outcomes; in the second they occupy different stages and do not interact.

### 5.2 Pairwise independence is weaker than mutual independence

Three events can be pairwise independent without being mutually independent, and this shows why the definition of mutual independence lists every sub-collection.

Take two independent fair coin tosses and define $A$ as "the first toss is a head", $B$ as "the second toss is a head", and $C$ as "exactly one head appears". Each event has probability one half. The three pairwise intersections each contain a single outcome, so each has probability one quarter:

$$
P(A \cap B) = P(A)P(B) = \frac{1}{4}, \qquad P(A \cap C) = P(A)P(C) = \frac{1}{4}, \qquad P(B \cap C) = P(B)P(C) = \frac{1}{4}
$$

But the triple intersection is empty, since $C$ excludes the two-head outcome that $A \cap B$ requires, so

$$
P(A \cap B \cap C) = 0 \ne \frac{1}{8} = P(A)P(B)P(C)
$$

The three events are pairwise independent and not mutually independent. Any argument that multiplies three probabilities must therefore be justified by mutual independence, not by a quick check of pairs.

### 5.3 The base-rate limit of Bayes' theorem

Bayes' theorem is arithmetically simple and psychologically difficult, because the posterior is dominated by the prior whenever the evidence is weak. Suppose a disease affects one person in one thousand, a test detects it with probability $0.99$ when present, and it produces a false positive with probability $0.01$ when absent. For a random person with a positive test,

$$
P(D \mid +) = \frac{(0.99)(0.001)}{(0.99)(0.001) + (0.01)(0.999)} = \frac{0.00099}{0.01098} \approx 0.090
$$

so fewer than one positive result in eleven corresponds to genuine disease. The reason is that the healthy group is roughly a thousand times larger, and even a small false-positive rate applied to a huge group produces more positives than the true cases do. Ignoring the base rate, or confusing $P(+ \mid D)$ with $P(D \mid +)$, is the prosecutor's fallacy, and both versions of the error appear in applied questions.

### 5.4 The limits of each interpretation

The classical interpretation requires a symmetry that can rarely be demonstrated outside games of chance; when outcomes are not equiprobable the formula must be abandoned rather than patched. The relative-frequency interpretation requires the repetitions to be independent and identically distributed, and it says nothing useful about a single unrepeatable event. The subjective interpretation requires only coherence, but two coherent agents may legitimately hold different probabilities for the same event, so the number is personal rather than universal.

The axiomatic framework accommodates all three because it abstracts away from the source of the numbers and retains only their structure. Its own limitation is that it cannot tell you which model to adopt: the axioms constrain the arithmetic of probabilities but say nothing about whether a particular die is fair. Choosing the model, and defending it, remains a modelling judgement that no axiom can supply.

### 5.5 Common errors and how to avoid them

- **Adding probabilities of overlapping events without subtracting the intersection.** The result can exceed one, which is an immediate signal of the error.
- **Applying the simplified addition law to exclusive-looking but overlapping events.** Check $A \cap B$ explicitly before dropping the correction term.
- **Multiplying unconditional probabilities in a without-replacement problem.** Every factor after the first must carry a conditional bar.
- **Dividing by $\lvert S\rvert$ in a conditional probability.** The denominator is the size of the conditioning event.
- **Treating pairwise independence as mutual independence.** Verify the triple product when three probabilities are multiplied.
- **Confusing $P(A \mid B)$ with $P(B \mid A)$.** These are different numbers unless the two events have equal probability.
- **Counting ordered outcomes in the numerator and unordered in the denominator.** Fix one convention and apply it to both.
- **Reading "at least one" as "exactly one".** The complement of "at least one" is "none", never "not exactly one".
- **Forgetting that the four hypergeometric cases must sum to one.** Doing so converts a silent arithmetic slip into a visible one.

### 5.6 Consolidation

The whole structure of the topic is deductive. Three axioms generate the complement rule, monotonicity, the difference rule, the two- and three-event addition laws, and, through the definition of conditional probability, the multiplication law, the chain rule, the partition identity and Bayes' theorem. Counting enters only to evaluate the ratios that the axioms leave abstract, and the classical formula is recovered as a theorem under the hypothesis of equal likelihood. Independence is a multiplicative condition on intersections, exclusivity an additive condition on unions, and the two cannot both hold for events of positive probability. A student who can state that chain, prove each link in two or three lines, and compute the counts reliably has mastered the topic at this level.

