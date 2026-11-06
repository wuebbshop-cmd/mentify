## 1. Foundational Concepts, Definitions, and Axioms

### 1.1 What the examiner is asking for

Questions on probability distributions are marked against four things: a correctly identified model with its parameters stated in symbols, a correctly quoted formula, correct arithmetic, and an interpreted answer. The identification step carries a mark in almost every question, and it is the step that decides whether the rest of the answer can be right. A candidate who writes $X \sim B(10, 0.2)$ before computing anything has already secured part of the credit and has protected the remaining steps from the commonest error on the topic, which is using the right formula with the wrong parameters.

The topic divides into three computational templates — binomial, Poisson, normal — and two bridging results, the Poisson approximation to the binomial and the normal approximation to the binomial. Each template has a fixed opening move, a fixed set of intermediate steps and a fixed check. Learning the templates as procedures rather than as isolated formulas is what turns a four-minute question into a two-minute one.

### 1.2 The definition set in examinable form

> **Definition (Random variable).** A random variable $X$ is a numerical quantity determined by the outcome of an experiment. It is discrete when its possible values can be listed, and continuous when they form an interval.

> **Definition (Probability mass function).** For a discrete $X$, the mass function is $p(x) = P(X = x)$, with $p(x) \ge 0$ and $\sum_{x} p(x) = 1$.

> **Definition (Probability density function).** For a continuous $X$, the density $f$ satisfies $f(x) \ge 0$, $\int_{-\infty}^{\infty} f(x)\,dx = 1$, and

$$
P(a < X < b) = \int_{a}^{b} f(x)\,dx .
$$

> **Definition (Distribution function).** For any $X$, $F(x) = P(X \le x)$, and $P(a < X \le b) = F(b) - F(a)$.

> **Definition (Expectation and variance).** $E(X) = \mu$ is the probability-weighted average of the values and $\text{Var}(X) = E\left[\left(X - \mu\right)^{2}\right] = E\left(X^{2}\right) - \mu^{2}$ is the probability-weighted average of the squared deviations.

The single sentence to remember about the density is that it is not a probability. The probability of an exact value of a continuous variable is zero, and only areas carry probability. Every year some candidates report a density as a probability and every year that answer is wrong.

### 1.3 The four models and their parameters

> **Bernoulli.** One trial, success probability $p$; $P(X = 1) = p$, $P(X = 0) = 1 - p$; mean $p$, variance $p\left(1 - p\right)$.

> **Binomial.** $n$ independent trials with constant success probability $p$; the count of successes $X$ satisfies

$$
P(X = x) = \binom{n}{x}p^{x}\left(1 - p\right)^{n - x}, \qquad E(X) = np, \qquad \text{Var}(X) = np\left(1 - p\right) .
$$

> **Poisson.** Count of events at average rate $\lambda$ in a stated interval;

$$
P(X = x) = \frac{e^{-\lambda}\lambda^{x}}{x!}, \qquad E(X) = \lambda, \qquad \text{Var}(X) = \lambda .
$$

> **Normal.** Continuous measurement with mean $\mu$ and variance $\sigma^{2}$; the density is

$$
f(x) = \frac{1}{\sigma\sqrt{2\pi}}\exp\left(-\frac{\left(x - \mu\right)^{2}}{2\sigma^{2}}\right),
$$

written $X \sim N\left(\mu, \sigma^{2}\right)$; standardised values $z = \frac{x - \mu}{\sigma}$ are read from the standard normal table.

> **Uniform and exponential.** The uniform on $\left[a, b\right]$ has mean $\frac{a + b}{2}$ and variance $\frac{\left(b - a\right)^{2}}{12}$. The exponential with rate $\lambda$ has density $\lambda e^{-\lambda x}$ on $x \ge 0$, mean $\frac{1}{\lambda}$ and variance $\frac{1}{\lambda^{2}}$.

### 1.4 The notation that appears in every question

| Symbol | Meaning | Typical exam phrasing |
|---|---|---|
| $X$ | the random variable | "let $X$ denote the number of..." |
| $n$ | number of trials | "twelve independently chosen items" |
| $p$ | success probability per trial | "probability $0.25$ of a defective" |
| $\lambda$ | average count per interval | "on average six per hour" |
| $\mu$ | mean of a distribution | "mean of $64$" |
| $\sigma$ | standard deviation | "standard deviation of $4$" |
| $z$ | standardised value | "find the $z$-value corresponding to $70$" |
| $\Phi(z)$ | area to the left of $z$ | "use the standard normal table" |

The distinction between $\lambda$ and $n$ is the one that decides the model. Lambda is an average count over an interval; it has no ceiling and is not a number of trials. If a question says "on average six per hour", the parameter is $\lambda = 6$ and the model is Poisson. If it says "twelve items are examined", the parameter is $n = 12$ and the model is binomial.

### 1.5 The five-step routine for every distribution question

Step 1. Identify the variable and decide whether it is a count or a measurement.

Step 2. For a count, look for a fixed number of trials. A fixed number means binomial with parameters $n$ and $p$; the absence of a fixed number and the presence of an average rate means Poisson with parameter $\lambda$.

Step 3. For a measurement, standardise with $z = \frac{x - \mu}{\sigma}$ and work from the standard normal table.

Step 4. Translate the words of the question into an inequality or a set of inequalities before computing: "at least one" becomes $X \ge 1$, "at most four" becomes $X \le 4$, "between eight and twelve" becomes $8 \le X \le 12$, and "more than three" becomes $X \ge 4$ for a discrete variable.

Step 5. State the answer in the units and context of the question and, where a comparison or judgement is requested, say what the number means.

Most lost marks on this topic come from skipping Step 4. A candidate who computes $P(X = 3)$ when the question asked for $P(X \ge 3)$ has done all the hard work and none of the credit.

### 1.6 The three inequalities that recur

The complement rule handles every "at least" question:

$$
P(X \ge r) = 1 - P(X \le r - 1) .
$$

For the binomial the special case $r = 1$ gives the neat closed form

$$
P(X \ge 1) = 1 - \left(1 - p\right)^{n},
$$

and for the Poisson it gives

$$
P(X \ge 1) = 1 - e^{-\lambda} .
$$

The interval identity handles every "between" question:

$$
P(a < X < b) = F(b) - F(a) .
$$

The symmetry identity handles every "greater than" question about a normal variable when only the left-hand table is available:

$$
P(Z > z) = 1 - \Phi(z), \qquad \Phi(-z) = 1 - \Phi(z) .
$$

### 1.7 Model recognition in one table

| Phrase in the question | Model | Parameters to state |
|---|---|---|
| fixed number of trials, count of successes | binomial | $n$ and $p$ |
| independently, constant probability | binomial | $n$ and $p$ |
| average rate per hour, per metre, per page | Poisson | $\lambda$ for the stated interval |
| no upper limit on the count | Poisson | $\lambda$ |
| mean and standard deviation given, continuous measurement | normal | $\mu$ and $\sigma$ |
| normally distributed with mean and variance stated | normal | $\mu$ and $\sigma$ |
| count with large $n$, moderate $p$, asked for an approximate probability | normal approximation | $np$ and $\sqrt{np\left(1 - p\right)}$ |
| count with large $n$ and very small $p$ | Poisson approximation | $\lambda = np$ |

The two rows at the bottom of the table are the bridging results, and they are examined as often as the basic models. When a question says "use a suitable approximation", it is telling you that the exact calculation is either impossible by hand or is not what is being tested.

### 1.8 The standard normal table values worth memorising

| $z$ | $\Phi(z)$ | Standard use |
|---|---|---|
| $1.00$ | $0.8413$ | one standard deviation above the mean |
| $1.645$ | $0.9500$ | lower boundary of the central ninety per cent |
| $1.96$ | $0.9750$ | two-sided ninety-five per cent boundary |
| $2.00$ | $0.9772$ | two standard deviations above the mean |
| $2.58$ | $0.9951$ | two-sided ninety-nine per cent boundary |
| $3.00$ | $0.9987$ | three standard deviations above the mean |

The symmetry identity converts each of these into a value for the negative argument: $\Phi(-1) = 0.1587$, $\Phi(-2) = 0.0228$, and so on. Memorising the five or six entries above saves table-reading time in a multiple-choice paper and provides a check on any interpolated value, which should always lie between its neighbours in the table.

### 1.9 What a complete answer looks like

A complete answer to a distribution question has four visible parts, and each of them is separately creditable. First, a statement of the model with its parameters in symbols. Second, a statement of the formula being applied, either quoted or clearly implied by substitution. Third, the substitution with the numbers visible, so that an arithmetic slip can be distinguished from a method error. Fourth, an interpretation in words, which for a comparison question names the smaller or larger quantity and says what it means in context.

Answers that omit the first and fourth parts typically lose two marks out of six even when every number is correct. Answers that include them can earn most of the marks even when the final arithmetic is wrong, because method marks are awarded for the substituted formula. The examination rewards structure, and the structure is entirely within the candidate's control.

## 2. Theorems, Lemmas, and Analytical Properties

### 2.1 The results that generate every question

> **Result 1 (Normalisation).** Every mass function sums to one and every density integrates to one. Any unknown constant in a proposed mass function or density is therefore determined by this condition alone.

> **Result 2 (Binomial moments).** For $X \sim B(n, p)$, $E(X) = np$ and $\text{Var}(X) = np\left(1 - p\right)$.

> **Result 3 (Poisson moments).** For $X \sim \text{Poisson}(\lambda)$, $E(X) = \lambda$ and $\text{Var}(X) = \lambda$, so the mean and the variance are equal.

> **Result 4 (Symmetry of the normal).** For $X \sim N\left(\mu, \sigma^{2}\right)$, $\Phi(-z) = 1 - \Phi(z)$, and consequently

$$
P(X < \mu - a) = P(X > \mu + a)
$$

for every positive $a$.

> **Result 5 (Standardisation).** If $X \sim N\left(\mu, \sigma^{2}\right)$ then $Z = \frac{X - \mu}{\sigma} \sim N(0, 1)$ and every probability about $X$ becomes a probability about $Z$.

> **Result 6 (Empirical rule).** For a normal variable, about $68.3$ per cent of values lie within one standard deviation of the mean, $95.4$ per cent within two, and $99.7$ per cent within three.

> **Result 7 (Poisson approximation).** If $n$ is large and $p$ is small, $B(n, p)$ is approximated by $\text{Poisson}(np)$.

> **Result 8 (Normal approximation).** If $np \ge 5$ and $n\left(1 - p\right) \ge 5$, $B(n, p)$ is approximated by $N\left(np, np\left(1 - p\right)\right)$, with a continuity correction of half a unit at each finite boundary.

> **Result 9 (Additivity).** Independent Poisson variables add their rates; independent normal variables add their means and their variances. Independent binomial variables with a common $p$ add their trial counts.

### 2.2 The conditions, stated as tests

Each model carries conditions that must be verified before the model may be applied. The verification is a sentence, and that sentence is frequently worth a mark.

> **Binomial conditions.** A fixed number $n$ of trials; exactly two outcomes per trial; independence between trials; and the same success probability $p$ throughout.

> **Poisson conditions.** Events occur one at a time; the average rate is constant over the interval; events occur independently of one another; and the count has no fixed upper limit.

> **Normal conditions.** The variable is continuous and its distribution is approximately symmetric and unimodal. For the approximation to the binomial, both $np$ and $n\left(1 - p\right)$ must be at least five.

A useful diagnostic for the Poisson is the ratio of variance to mean. The theory demands equality; data in which the sample variance greatly exceeds the sample mean are over-dispersed and a Poisson answer, however tidy, is not defensible.

### 2.3 Where each standardisation comes from

Two standardisations are used on this topic and they must not be confused.

For a single observation from a normal distribution the standardised value is

$$
z = \frac{x - \mu}{\sigma},
$$

and it measures how many standard deviations the observation lies from the mean.

For a count being approximated by a normal distribution the standardised value is

$$
z = \frac{x - np}{\sqrt{np\left(1 - p\right)}},
$$

and it measures how many standard deviations the observed count lies from its expected value.

The two formulas are the same formula with different symbols, since $\mu = np$ and $\sigma = \sqrt{np\left(1 - p\right)}$ for the binomial. The trap is to substitute $p$ for $\sigma$ in the second, or to divide by $n$ instead of by the standard deviation of the count. Writing the two parameters $\mu$ and $\sigma$ explicitly before standardising prevents both errors.

### 2.4 Continuity correction: the rule and the reason

> **Lemma (Continuity correction).** Let $X$ be integer-valued and let $Y$ be a continuous normal variable used to approximate it. Then, for integers $a$ and $b$,

$$
P(X \le k) \approx P(Y < k + 0.5), \qquad P(X \ge k) \approx P(Y > k - 0.5),
$$

$$
P(a \le X \le b) \approx P(a - 0.5 < Y < b + 0.5), \qquad P(X = k) \approx P(k - 0.5 < Y < k + 0.5) .
$$

The reason is that the integer $k$ stands for the whole interval from $k - 0.5$ to $k + 0.5$ on the continuous scale, because every continuous value in that interval rounds to $k$. Including the whole interval is what makes the discrete bar and the continuous strip cover the same region. The correction always moves a finite boundary away from the region of interest, so the probability of a one-sided event increases in magnitude: $P(X \le k)$ is slightly larger than the uncorrected normal value, and $P(X \ge k)$ is also slightly larger.

The magnitude of the correction is about $\frac{0.5}{\sigma}$ in $z$-units. It is negligible when $\sigma$ is large and decisive when $\sigma$ is small, which is exactly the regime where the approximation itself is marginal.

### 2.5 The two approximation regimes side by side

| Regime | Model | Parameter | Reason |
|---|---|---|---|
| large $n$, $p$ small, $np$ moderate | Poisson approximation | $\lambda = np$ | binomial tends to Poisson |
| large $n$, $p$ near one half, both products large | normal approximation | $\mu = np$, $\sigma^{2} = np\left(1 - p\right)$ | binomial is nearly symmetric |
| large $n$, $p$ extreme, count small | Poisson approximation retained | $\lambda = np$ | normal assigns mass below zero |

The third row is worth emphasising because it is the case candidates get wrong. With $n = 500$ and $p = 0.004$ the expected count is two; a normal curve with mean two and standard deviation about $1.41$ places appreciable probability on negative counts, which is impossible. The Poisson handles the same case correctly, and the normal approximation to the binomial is invalid despite the large $n$.

### 2.6 Probability statements translated into inequalities

| Words in the question | Discrete model | Continuous model |
|---|---|---|
| at most four | $X \le 4$ | $X < 4$ |
| fewer than four | $X \le 3$ | $X < 4$ |
| at least four | $X \ge 4$ | $X > 4$ |
| more than four | $X \ge 5$ | $X > 4$ |
| exactly four | $X = 4$ | probability zero |
| between four and seven inclusive | $4 \le X \le 7$ | $3.5 < Y < 7.5$ with correction |
| within two of the mean | $\mu - 2 \le X \le \mu + 2$ | $\mu - 2 < X < \mu + 2$ |

The translation column is the one to write down before touching a calculator. Note in particular the difference between "fewer than four" and "at most four" for a discrete variable: they differ by the whole probability of four, which in a small sample can be several per cent.

### 2.7 Bounds that do not need a distribution

> **Result 10 (Chebyshev).** For any random variable with finite mean $\mu$ and finite standard deviation $\sigma$,

$$
P\left(\left\lvert X - \mu\right\rvert \ge k\sigma\right) \le \frac{1}{k^{2}} .
$$

The bound is distribution-free, so it may be quoted when a question gives a mean and a standard deviation and no distributional shape. For $k = 2$ it guarantees at least $75$ per cent of the probability lies within two standard deviations, which is weaker than the normal figure of $95.4$ per cent but valid without any normality assumption. Multiple-choice items that offer a bound rather than an exact probability are usually testing this result.

### 2.8 The assumptions behind the standard solutions

Three assumptions do most of the work. Independence makes the probability of a sequence the product of the individual probabilities, which is what produces the $p^{x}\left(1 - p\right)^{n - x}$ factor. A constant rate makes the Poisson formula applicable and makes $\lambda$ proportional to the length of the interval. Approximate symmetry is what allows a bell curve to stand in for a discrete distribution, and the two-product condition $np \ge 5$, $n\left(1 - p\right) \ge 5$ is the operational way of verifying it.

Every one of these assumptions can be checked in the wording of a question. "Independently" in the text licenses independence. "On average, at a constant rate" licenses the constant rate. "The probability is the same for each item" licenses the constant $p$. A question that says "items are drawn without replacement from a box of ten" explicitly denies both independence and a constant probability, and the binomial answer is then wrong even if the arithmetic is perfect.

## 3. Formal Proofs, Derivations, and Methods

### 3.1 Derivation of the binomial mass function

Step 1. Fix one arrangement with $x$ successes followed by $n - x$ failures. Independence makes its probability the product of the individual factors.

$$
p^{x}\left(1 - p\right)^{n - x}
$$

Step 2. Note that every arrangement with the same number of successes has the same probability, so only the number of arrangements is needed.

Step 3. Count the arrangements by choosing which $x$ of the $n$ positions are successes.

$$
\binom{n}{x} = \frac{n!}{x!\left(n - x\right)!}
$$

Step 4. Multiply to obtain the mass function.

$$
P(X = x) = \binom{n}{x}p^{x}\left(1 - p\right)^{n - x}
$$

Step 5. Verify normalisation with the binomial theorem.

$$
\sum_{x=0}^{n}\binom{n}{x}p^{x}\left(1 - p\right)^{n - x} = \left(p + 1 - p\right)^{n} = 1
$$

The verification is exact, so the binomial mass function is normalised for every admissible $n$ and $p$ without any approximation.

### 3.2 Moments of the binomial

Write $X = I_1 + \dots + I_n$ where $I_j$ is the indicator of success on trial $j$. Then $E\left(I_j\right) = p$ and $\text{Var}\left(I_j\right) = p\left(1 - p\right)$. Linearity of expectation gives

$$
E(X) = \sum_{j=1}^{n} E\left(I_j\right) = np,
$$

and independence kills every covariance, so

$$
\text{Var}(X) = \sum_{j=1}^{n}\text{Var}\left(I_j\right) = np\left(1 - p\right) .
$$

Both statements are exact. In an examination the derivation is required only when the question says "prove" or "show"; otherwise the results may be quoted.

### 3.3 The Poisson limit

Let $X \sim B\left(n, \frac{\lambda}{n}\right)$ and fix $x$. Then

$$
P(X = x) = \frac{n\left(n - 1\right)\cdots\left(n - x + 1\right)}{x!}\left(\frac{\lambda}{n}\right)^{x}\left(1 - \frac{\lambda}{n}\right)^{n - x},
$$

which separates into three factors.

$$
P(X = x) = \frac{\lambda^{x}}{x!}\cdot\prod_{j=0}^{x-1}\left(1 - \frac{j}{n}\right)\cdot\left(1 - \frac{\lambda}{n}\right)^{n}\left(1 - \frac{\lambda}{n}\right)^{-x}
$$

The product tends to one because each factor tends to one and there are only finitely many of them for fixed $x$. The power tends to $e^{-\lambda}$ by the standard limit, and the final factor tends to one. Hence

$$
P(X = x) \to \frac{e^{-\lambda}\lambda^{x}}{x!} .
$$

The derivation identifies the three conditions of the approximation: $n$ large makes the power converge, $p = \frac{\lambda}{n}$ small makes each factor of the product close to one, and $\lambda$ moderate keeps the relevant values of $x$ small relative to $n$.

### 3.4 Normalisation of the normal density

The defining integral is evaluated by the substitution $t = \frac{x - \mu}{\sigma\sqrt{2}}$ and the Gaussian integral

$$
\int_{-\infty}^{\infty} e^{-t^{2}}\,dt = \sqrt{\pi},
$$

which is proved by squaring the integral and passing to polar coordinates. Applying the substitution,

$$
\int_{-\infty}^{\infty}\exp\left(-\frac{\left(x - \mu\right)^{2}}{2\sigma^{2}}\right)dx = \sigma\sqrt{2\pi},
$$

so dividing by $\sigma\sqrt{2\pi}$ gives total area one. This is the derivation of the constant in front of the density, and it is the answer expected when a question asks why the constant takes that value.

### 3.5 Method: the binomial template

Step 1. Extract $n$ and $p$ from the wording and write $X \sim B(n, p)$.

Step 2. Translate the question into an inequality in $X$.

Step 3. If the value is a single point, substitute directly into the mass function.

Step 4. If the region has several points, either add the individual probabilities or use the complement, choosing whichever is shorter. For "at least $r$" the complement involves $r$ terms, so a complement is cheaper whenever $r$ is small.

Step 5. Where a computation has more than three terms, use the recursion

$$
P(X = x) = \frac{n - x + 1}{x}\cdot\frac{p}{1 - p}\cdot P(X = x - 1),
$$

which is exact and avoids repeated exponentiation.

Step 6. Compute the mean and variance only if asked, using $np$ and $np\left(1 - p\right)$.

### 3.6 Method: the Poisson template with a possible rate change

Step 1. Identify the interval to which the quoted rate applies, and the interval the question asks about.

Step 2. Rescale the rate by direct proportion. Two hours at three per hour gives six; thirty minutes at four per hour gives two; a hundred metres at one per ten metres gives ten.

Step 3. Write $X \sim \text{Poisson}(\lambda)$ with the rescaled rate.

Step 4. Compute the anchor value $P(X = 0) = e^{-\lambda}$ and build upwards with the recursion $P(X = x) = \frac{\lambda}{x}P(X = x - 1)$.

Step 5. Convert the required region into a sum or a complement.

Step 6. State the mean and the variance, both equal to $\lambda$, if asked.

### 3.7 Method: the normal template

Step 1. Write $X \sim N\left(\mu, \sigma^{2}\right)$ with the numbers from the question, taking care that a stated second parameter may be a variance rather than a standard deviation.

Step 2. Sketch the bell, mark the mean, and shade the region asked about.

Step 3. Standardise each boundary with $z = \frac{x - \mu}{\sigma}$.

Step 4. Convert the region into one of three forms: $\Phi(z)$, $1 - \Phi(z)$, or $\Phi\left(z_2\right) - \Phi\left(z_1\right)$.

Step 5. Read the table and compute.

Step 6. Check that the answer lies between zero and one, and that a central region is larger than a one-sided region of the same width.

### 3.8 Method: the normal approximation template

Step 1. Check $np \ge 5$ and $n\left(1 - p\right) \ge 5$. If either fails, use the binomial or the Poisson instead.

Step 2. Write $\mu = np$ and $\sigma = \sqrt{np\left(1 - p\right)}$ and record both.

Step 3. Rewrite the discrete event with the half-unit correction.

Step 4. Standardise the corrected boundary with $z = \frac{x - \mu}{\sigma}$.

Step 5. Read the table and compute.

Step 6. Compare with any exact value the question supplies, and comment on the size of the error.

The order of Steps 2 and 3 matters only in presentation, but Step 1 must come first: a correct continuity correction applied to an invalid approximation is worth nothing.

### 3.9 Method: justifying an approximation in one sentence

An approximation justification has three clauses and each names a condition. For the normal approximation the sentence is: the number of trials is large, and both $np$ and $n\left(1 - p\right)$ exceed five, so the binomial is approximately normal with the stated mean and variance. For the Poisson approximation the sentence is: the number of trials is large, the success probability is small, and the expected count is moderate, so the binomial is approximately Poisson with rate equal to the expected count.

A justification that merely says "the approximation is valid" earns nothing. A justification that quotes the numerical values of $np$ and $n\left(1 - p\right)$ earns the mark even when the subsequent arithmetic fails.

### 3.10 Method: recovering a missing parameter

Some questions give a probability and ask for a parameter. The technique is to write the probability in terms of the unknown, take logarithms, and solve.

For a binomial, the condition $P(X = 0) = \alpha$ gives $\left(1 - p\right)^{n} = \alpha$, hence $p = 1 - \alpha^{1/n}$. For a Poisson, $P(X = 0) = \alpha$ gives $e^{-\lambda} = \alpha$, hence $\lambda = -\ln \alpha$. For a normal, a stated probability determines a $z$-value from the table, and the standardisation formula is then solved for whichever of $\mu$ or $\sigma$ is unknown.

$$
\sigma = \frac{x - \mu}{z}, \qquad \mu = x - z\sigma
$$

Always check the sign of $z$ before solving: a probability greater than one half corresponds to a positive $z$, and a probability less than one half to a negative $z$. A sign error here produces a plausible-looking but wrong answer, and it is not detectable from the arithmetic alone.

## 4. Representative Worked Examples and Solutions

### 4.1 Model solution 1: a binomial count

In a manufacturing process each item is defective with probability $0.25$, independently of all others. A random sample of twelve items is inspected. Let $X$ be the number of defectives.

(a) State the distribution of $X$ and justify the choice of model.

(b) Find the probability that exactly three items are defective.

(c) Find the probability that at least two items are defective.

(d) Find the mean and standard deviation of $X$.

### 4.2 Solution with marking points

Step 1. Identify the model. There are twelve items, so the number of trials is fixed at $n = 12$. Each item is defective or not, giving two outcomes. The items are independent by the wording, and the defect probability is the same for every item at $p = 0.25$. Therefore

$$
X \sim B\left(12, 0.25\right) .
$$

Marking point: one mark for the notation with both parameters correct and one mark for naming the four conditions. Stating the distribution without justification typically loses the second mark.

Step 2. Substitute into the mass function for $x = 3$.

$$
P(X = 3) = \binom{12}{3}\left(0.25\right)^{3}\left(0.75\right)^{9}
$$

Step 3. Evaluate the three factors separately, which is where arithmetic marks are earned.

$$
\binom{12}{3} = \frac{12 \times 11 \times 10}{3 \times 2 \times 1} = 220, \qquad \left(0.25\right)^{3} = 0.015625, \qquad \left(0.75\right)^{9} \approx 0.075085
$$

Step 4. Multiply.

$$
P(X = 3) = 220 \times 0.015625 \times 0.075085 \approx 0.2581
$$

Marking point: one mark for the correct coefficient, one for the powers, one for the product.

Step 5. Begin the second probability with the complement, since the complement of "at least two" has only two terms.

$$
P(X \ge 2) = 1 - P(X = 0) - P(X = 1)
$$

Step 6. Compute the two terms.

$$
P(X = 0) = \left(0.75\right)^{12} \approx 0.031676
$$

$$
P(X = 1) = \binom{12}{1}\left(0.25\right)\left(0.75\right)^{11} = 12 \times 0.25 \times 0.042235 \approx 0.126705
$$

Step 7. Subtract.

$$
P(X \ge 2) = 1 - 0.031676 - 0.126705 \approx 0.8416
$$

Marking point: one mark for the complement structure and one for the evaluation. A candidate who computes $P(X = 2)$ only has answered the wrong question and forfeits both.

Step 8. Compute the moments.

$$
E(X) = np = 12 \times 0.25 = 3
$$

$$
\text{Var}(X) = np\left(1 - p\right) = 12 \times 0.25 \times 0.75 = 2.25, \qquad \sigma = \sqrt{2.25} = 1.5
$$

Step 9. Interpret. The process produces three defectives per twelve on average, with a typical departure of one and a half items. About twenty-six per cent of samples contain exactly three defectives, and about eighty-four per cent contain at least two. Since $p < 0.5$ the distribution is skewed to the right and the mean exceeds the median, which is worth one sentence if the question asks for a comment on shape.

Marking points for part (d): one mark for the mean, one for the variance, one for the standard deviation, one for the interpretation.

### 4.3 Model solution 2: a Poisson count with a rate change

Calls reach a helpline at an average of $1.5$ per half hour, independently and at a constant rate. Let $X$ be the number of calls in a two-hour period.

(a) State the distribution of $X$, showing the value of the parameter.

(b) Find the probability of no calls in the two-hour period.

(c) Find the probability of at least four calls.

### 4.4 Solution with marking points

Step 1. Establish the rate for the interval in the question. The quoted rate is per half hour, and two hours contain four half hours, so the rate must be multiplied by four.

$$
\lambda = 1.5 \times 4 = 6
$$

Marking point: one mark for the rescaling. Substituting $1.5$ directly is the single most common error on this topic and loses every subsequent mark.

Step 2. State the model and the conditions.

$$
X \sim \text{Poisson}(6)
$$

The conditions are: calls arrive singly, the average rate is constant over the period, arrivals are independent, and there is no fixed upper limit on the count.

Step 3. Compute the anchor probability.

$$
P(X = 0) = \frac{e^{-6}6^{0}}{0!} = e^{-6} \approx 0.0025
$$

Step 4. Build the next three values with the exact recursion $P(X = x) = \frac{\lambda}{x}P(X = x - 1)$.

$$
P(X = 1) = \frac{6}{1}\left(0.002479\right) \approx 0.014873
$$

$$
P(X = 2) = \frac{6}{2}\left(0.014873\right) \approx 0.044618
$$

$$
P(X = 3) = \frac{6}{3}\left(0.044618\right) \approx 0.089235
$$

Step 5. Use the complement for the third part.

$$
P(X \ge 4) = 1 - P(X \le 3) = 1 - \left(0.002479 + 0.014873 + 0.044618 + 0.089235\right)
$$

$$
P(X \ge 4) \approx 1 - 0.151205 = 0.8488
$$

Step 6. State the moments for completeness.

$$
E(X) = \lambda = 6, \qquad \text{Var}(X) = 6, \qquad \sigma = \sqrt{6} \approx 2.449
$$

Step 7. Interpret. A two-hour period brings six calls on average, with a standard deviation of about $2.45$. Periods with no calls at all are rare, about one in four hundred, while about eighty-five per cent of periods bring four calls or more.

Marking points: one for the model with the rescaled parameter, one for $P(X = 0)$, one for the recursion or the individual terms, one for the complement, one for the final value, one for the interpretation.

### 4.5 Model solution 3: a normal probability with three regions

The mass of a component is normally distributed with mean $64$ grams and standard deviation $4$ grams.

(a) Find the probability that a component has mass below $70$ grams.

(b) Find the probability that a component has mass above $58$ grams.

(c) Find the probability that a component has mass between $60$ and $68$ grams.

### 4.6 Solution with marking points

Step 1. Record the model.

$$
X \sim N\left(64, 16\right)
$$

Note that the standard deviation is $4$ and the variance is $16$; the notation quotes the variance second, so a question stated as $N\left(64, 16\right)$ must never be read as having standard deviation $16$.

Step 2. Standardise the first boundary.

$$
z = \frac{70 - 64}{4} = 1.5
$$

Step 3. Read the table.

$$
P(X < 70) = \Phi(1.5) \approx 0.9332
$$

Step 4. Standardise the second boundary.

$$
z = \frac{58 - 64}{4} = -1.5
$$

Step 5. Convert to an upper tail, using symmetry.

$$
P(X > 58) = 1 - \Phi(-1.5) = \Phi(1.5) \approx 0.9332
$$

Marking point: one mark for recognising that the two answers are equal by symmetry. Computing the second probability from scratch and reporting a different value reveals an arithmetic rather than a conceptual slip.

Step 6. Standardise both boundaries of the third part.

$$
z_1 = \frac{60 - 64}{4} = -1, \qquad z_2 = \frac{68 - 64}{4} = 1
$$

Step 7. Subtract.

$$
P(60 < X < 68) = \Phi(1) - \Phi(-1) = 0.8413 - 0.1587 = 0.6826
$$

Step 8. Interpret and cross-check. About ninety-three per cent of components lie below $70$ grams and the same proportion above $58$ grams, which is consistent with the symmetry of the curve about $64$. The central interval spanning one standard deviation either side of the mean contains about sixty-eight per cent of components, which is exactly the empirical rule and therefore a check on the table reading.

Marking points: one per standardisation, one per table value, one for the subtraction, one for the interpretation. Where a question asks for a percentage, convert only at the end.

### 4.7 Model solution 4: the normal approximation with continuity correction

A fair spinner has three equally likely colours, one of which is red. The spinner is spun $200$ times. Let $X$ be the number of reds.

(a) Justify the use of a normal approximation.

(b) Use the approximation to find $P(X \le 70)$.

(c) Use the approximation to find $P(55 \le X \le 65)$.

### 4.8 Solution with marking points

Step 1. Identify the exact model first.

$$
X \sim B\left(200, \frac{1}{3}\right)
$$

Step 2. Compute the parameters and check the conditions.

$$
\mu = np = 200 \times \frac{1}{3} \approx 66.667, \qquad \sigma = \sqrt{np\left(1 - p\right)} = \sqrt{200 \times \frac{1}{3} \times \frac{2}{3}} = \sqrt{\frac{400}{9}} \approx 6.667
$$

Both $np \approx 66.7$ and $n\left(1 - p\right) \approx 133.3$ greatly exceed $5$, so the approximation is justified.

Marking point: one mark for computing both products and comparing them with $5$. The sentence "the sample is large" alone does not earn the mark.

Step 3. Apply the continuity correction, replacing $X \le 70$ by $X < 70.5$.

Step 4. Standardise.

$$
z = \frac{70.5 - 66.667}{6.667} = \frac{3.833}{6.667} \approx 0.575
$$

The table gives

$$
P(X \le 70) \approx \Phi(0.575) \approx 0.7174
$$

Step 5. Repeat without the correction for comparison.

$$
z = \frac{70 - 66.667}{6.667} \approx 0.500, \qquad \Phi(0.50) \approx 0.6915
$$

The exact binomial value is about $0.7192$, so the corrected answer is within $0.002$ while the uncorrected answer is too small by about $0.028$.

Marking point: one mark for the corrected boundary, one for the correct $z$, one for the table value, one for the comparison.

Step 6. Correct both boundaries for the two-sided part.

$$
X = 55 \text{ becomes } 54.5, \qquad X = 65 \text{ becomes } 65.5
$$

Step 7. Standardise both.

$$
z_1 = \frac{54.5 - 66.667}{6.667} \approx -1.825, \qquad z_2 = \frac{65.5 - 66.667}{6.667} \approx -0.175
$$

Step 8. Subtract the table values.

$$
P(55 \le X \le 65) \approx \Phi(-0.175) - \Phi(-1.825) = 0.4305 - 0.0340 = 0.3965
$$

The exact binomial value is about $0.4014$, so the approximation is accurate to within $0.005$.

Step 9. Interpret. About seventy-two per cent of runs contain at most seventy reds and about forty per cent contain between fifty-five and sixty-five. The second region lies entirely below the mean, which is why its probability is below one half; checking this against the mean of about $66.7$ is a useful guard against a sign error in the standardisation.

Marking point: one mark for correcting both boundaries, one for each $z$-value, one for the subtraction. Applying the correction to only one end is the commonest failure here.

### 4.9 Model solution 5: choosing the model

For each situation, state the distribution and its parameters, and compute the probability asked for.

(a) Eight multiple-choice questions each have four options, one correct. A candidate guesses every answer. Find the probability of at least two correct.

(b) Accidents occur at a junction at an average of two per week, independently. Find the probability of no accident in a week.

(c) The length of a machined part is normally distributed with mean $50$ millimetres and standard deviation $0.4$ millimetres. Find the probability that a part is longer than $50.9$ millimetres.

(d) A batch of $200$ components has a defect probability of $0.01$ each. Use a Poisson approximation to find the probability that exactly two are defective.

### 4.10 Solution with marking points

Step 1. For (a), there are eight fixed trials, two outcomes each, independence and a constant chance of one quarter. Hence

$$
X \sim B\left(8, 0.25\right) .
$$

Step 2. Compute the two excluded terms.

$$
P(X = 0) = \left(0.75\right)^{8} \approx 0.1001, \qquad P(X = 1) = 8 \times 0.25 \times \left(0.75\right)^{7} \approx 0.2670
$$

Step 3. Subtract from one.

$$
P(X \ge 2) \approx 1 - 0.1001 - 0.2670 = 0.6329
$$

Step 4. For (b), there is no fixed number of trials and only an average rate is quoted, so

$$
X \sim \text{Poisson}(2), \qquad P(X = 0) = e^{-2} \approx 0.1353 .
$$

Step 5. For (c), standardise the boundary.

$$
z = \frac{50.9 - 50}{0.4} = 2.25
$$

Step 6. Take the upper tail.

$$
P(X > 50.9) = 1 - \Phi(2.25) \approx 1 - 0.9878 = 0.0122
$$

Step 7. For (d), compute the rate for the approximation.

$$
\lambda = np = 200 \times 0.01 = 2
$$

Step 8. Apply the Poisson formula.

$$
P(X = 2) \approx \frac{e^{-2}2^{2}}{2!} \approx 2 \times 0.1353 = 0.2707
$$

Step 9. Justify the approximation and compare. Here $n = 200$ is large, $p = 0.01$ is small and $\lambda = 2$ is moderate, so all three conditions hold. The exact binomial value is about $0.2720$, so the approximation is accurate to two decimal places.

Step 10. Summarise the four models in a sentence each: a fixed number of trials gives the binomial, an average rate gives the Poisson, a symmetric measurement gives the normal, and a large sample with a small success chance gives the Poisson approximation.

Marking points: one mark per correctly identified model with its parameters, one per computed probability, one for the approximation justification.

## 5. Mathematical Extensions, Limits, and Common Errors

### 5.1 The seven traps in order of cost

The first trap is mis-scaling the Poisson rate. A rate quoted per half hour, per week, per metre or per page must be converted to the interval in the question before anything else is done. This error is costly because every subsequent number is wrong. The safeguard is to write the conversion as an explicit line: four half hours in two hours, therefore the rate is multiplied by four.

The second trap is forgetting the continuity correction. The uncorrected normal approximation to a binomial is biased towards the centre, and for moderate $n$ the bias reaches the second decimal place. The safeguard is to write the corrected boundary as a separate line before standardising, and to correct every finite boundary in a two-sided question.

The third trap is mis-standardising. Writing $\frac{\mu - x}{\sigma}$ instead of $\frac{x - \mu}{\sigma}$ reverses every sign and produces the complementary tail. The safeguard is the sketch: a value above the mean must give a positive $z$, and the sketch makes the mismatch visible before the table is consulted.

The fourth trap is confusing $\lambda$ with $n$. Lambda is an average count with no ceiling; $n$ is a fixed number of trials. A question that says "on average" is a Poisson question, and a question that says "a sample of twelve" is a binomial question, even when both mention the same numerical value.

The fifth trap is using the normal approximation when $n$ is small or $p$ is extreme. If either $np$ or $n\left(1 - p\right)$ is below five, the bell curve does not describe the discrete distribution and the answer will be materially wrong. In that regime the exact binomial, or the Poisson approximation when $p$ is small, is required.

The sixth trap is quoting a variance where a standard deviation belongs. The normal notation $N\left(\mu, \sigma^{2}\right)$ places the variance second, so $N\left(64, 16\right)$ has standard deviation four. Dividing by sixteen instead of four produces a $z$-value four times too small and an answer that looks precise and is wrong.

The seventh trap is misreading "fewer than" as "at most". For a discrete variable the boundary value itself carries probability, and dropping or adding it changes the answer by a visible amount. The safeguard is to rewrite the phrase as an inequality in the standard form before computing, using the translation table of Section 2.6.

### 5.2 How the marks are distributed

A typical six-mark question breaks down as one mark for the model statement with parameters, one for the correct formula, two for the substitution and evaluation, one for the correct final value, and one for the interpretation or the justification. A typical eight-mark question adds a second required probability and a comment on the conditions.

The practical consequence is that a candidate who runs out of time mid-calculation should still write the model statement, the formula and the substitution, because those three lines may earn three of the six marks. Conversely, a candidate who writes only a numerical answer, however correct, forgoes the interpretation mark and risks losing the method marks if the answer is wrong.

### 5.3 A revision checklist

Work through the following list and tick an item only when it can be done from memory in under two minutes.

1. State the four binomial conditions and the four Poisson conditions without notes.
2. Write the binomial mass function and evaluate it for a given $n$, $p$ and $x$ without a calculator for the coefficient.
3. Derive $E(X) = np$ and $\text{Var}(X) = np\left(1 - p\right)$ using indicators.
4. Write the Poisson mass function and use the recursion to obtain successive values.
5. Derive the Poisson limit of the binomial in four lines.
6. State the normal density, explain the role of each constant, and quote the Gaussian integral.
7. Standardise any normal variable and read the table, including negative $z$ by symmetry.
8. State and apply the empirical rule, and explain why it does not apply to skewed data.
9. Apply the continuity correction to one-sided, two-sided and exact-value events.
10. Justify the Poisson and normal approximations with the numerical conditions.
11. State the additivity properties of the Poisson and the normal, and explain why variances rather than standard deviations add.
12. Recognise the four models from a description in words and name the parameters.

### 5.4 Time strategy

Allow roughly one minute per mark and reserve the last minute of any distribution question for the interpretation and the plausibility check. The three templates have very different costs: a Poisson calculation with three terms takes about two minutes, a binomial with a large coefficient takes about three, and a normal approximation with two boundaries takes about four. In a paper with a choice, a Poisson question is the most efficient source of marks per minute and a multi-part binomial the least.

Where a question is worth eight or more marks, write the model statement and the formula first, before any arithmetic, so that a later interruption cannot cost the method marks. Where a question offers no calculator for one part, look for a probability that can be read directly from a standard table value: $0.8413$, $0.9772$ and $0.9987$ appear so often that recognising them saves a full minute.

### 5.5 Where the topic leads

The three models here underpin everything that follows. The binomial becomes the model for proportions in large samples, and the normal approximation to it becomes the basis of the test for a single proportion. The Poisson becomes the model for rates, and its additivity property becomes the basis of tests for comparing two rates. The normal becomes the reference distribution for sample means through the central limit theorem, which states that the standardised mean of a large sample is approximately standard normal whatever the shape of the population, provided the population has a finite variance. The empirical rule quoted here as a description of one curve reappears as the logic of confidence intervals, where a two-standard-error interval is built from exactly the same area calculation. A candidate who can standardise a single observation and read $\Phi$ has, in effect, learned the central computational skill of the whole of the rest of the subject.