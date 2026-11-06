## 1. Foundational Concepts, Definitions, and Axioms

### 1.1 A bakery that never knows the morning

Imagine a small bakery that opens at six in the morning and has no idea how many loaves it will sell before noon. The baker cannot say "we will sell forty-three loaves today", because that is not knowable in advance. What the baker can say is something much more useful: "most days we sell between thirty and fifty; about one day in ten we sell fewer than twenty-five; almost never do we sell more than sixty." That kind of statement is a probability distribution. It is a description of all the values a quantity might take, together with how likely each value is. It is a map of the possible, not a prediction of the actual.

Think of a second everyday situation. A courier company weighs parcels all day. Most parcels weigh around two kilograms, a few are very light, a few are heavy, and the weights thin out smoothly in both directions from the middle. If you drew a picture of how many parcels fall into each weight band, you would get a smooth hump, highest in the middle and sloping away on both sides. That hump is the normal curve, and it is one of the three shapes this topic studies.

Picture a third situation. A call centre records how many complaints arrive in each hour. Most hours bring none or one, a few bring three, and an hour with eight is remarkable. The counts are whole numbers, they cannot be negative, and they pile up near zero with a long thin tail to the right. That shape is the Poisson distribution. Again nothing has been calculated yet; the point is that the shapes of uncertainty have names, and once you can recognise the shape you can answer quantitative questions about it.

The whole topic is therefore built on one idea: quantities that vary at random have recognisable patterns, and each pattern has a formula that turns "how likely is this?" into arithmetic. The three patterns studied here are the binomial, the Poisson and the normal. Between them they cover most counting questions and most measuring questions met in practice.

### 1.2 Random variables

Before any formula, three words must be fixed.

An experiment is any process whose result is not known in advance: tossing a coin, counting complaints in an hour, weighing a parcel.

An outcome is one possible result of that experiment: the coin shows a head, exactly two complaints arrive, the parcel weighs 2.3 kilograms.

A random variable is a rule that attaches a number to each outcome. The number is the thing we actually want to talk about: the count of heads, the count of complaints, the weight of the parcel. The capital letter $X$ is used for the random variable itself, and the small letter $x$ for a particular value it might take. So the sentence "the probability that the count equals two" is written $P(X = 2)$, and the symbol $P$ stands for probability, the bracket means "of the event inside", and the equals sign picks out one particular value.

The distinction between $X$ and $x$ matters more than it looks. The capital letter is the whole uncertain quantity, with all its possible values and their chances. The small letter is one value being examined. When a question says "find the probability that $X$ is at most three", it means: add up the chances of every value of the random variable that is three or smaller.

### 1.3 Discrete and continuous random variables

There are two kinds of random variable, and telling them apart decides which formulas you may use.

A discrete random variable takes values that can be listed one at a time, usually whole numbers. The number of heads in ten tosses can be nought, one, two, and so on up to ten, and nothing in between. The number of complaints in an hour is a whole number. Between two and three complaints there is no possible value, because a complaint is a whole event.

A continuous random variable takes any value in a range, with no gaps. A weight can be 2.31 kilograms, or 2.314, or 2.3147, depending on how finely you measure. There is no "next" weight after 2.31, because you can always name a weight closer to it. Height, time, temperature and length behave this way.

The practical consequence is that a discrete variable is described by a list of chances and a continuous variable is described by an area under a curve. For a continuous variable, the chance of one exact value is zero. "The parcel weighs exactly 2.300000 kilograms" has probability zero, because the measuring instrument would have to land on that one point out of infinitely many. This is not a paradox; it means that for continuous variables we always ask about intervals, such as "between 2.2 and 2.4 kilograms". The chance is then the area under the curve between those two weights.

### 1.4 Probability mass and probability density

For a discrete random variable the description of chance is a list called the probability mass function. It gives, for each possible value $x$, the number $P(X = x)$, which is the chance of that exact value. The word "mass" is used because the chances behave like weights piled on the number line: a value with probability $0.4$ carries forty per cent of the total weight.

For a continuous random variable the description is a curve called the probability density function, written $f(x)$. The curve is not itself a probability. The height of the curve at a point is a density, and the probability of an interval is the area under the curve above that interval. This is the single most common source of confusion in the topic, so it is worth stating plainly: for a continuous variable you integrate the density over an interval to get a probability, and a bare density value is not a probability. A density can exceed one, whereas a probability never can.

Both kinds of description obey the same two rules. Every chance is at least zero and at most one, and the total chance over all possible values is exactly one. For a discrete variable the total is a sum of the listed probabilities. For a continuous variable the total is the whole area under the curve, and the curve is drawn so that this whole area equals one.

### 1.5 The cumulative distribution function

A second description of the same information is the cumulative distribution function, written $F(x)$. It is defined as the chance that the random variable is at most $x$, that is $F(x) = P(X \le x)$. The symbol $\le$ means "less than or equal to", so $F$ answers questions of the form "how much chance lies to the left of this point?".

The cumulative function starts at zero far to the left, rises as you move right, and finishes at one far to the right. For a discrete variable it rises in steps, one step at each possible value. For a continuous variable it rises smoothly, and its slope at a point is the density at that point. Reading a "less than" question from the cumulative function is immediate; reading a "greater than" question needs the complement rule, which says that the chance of more than $x$ is one minus the chance of at most $x$.

### 1.6 Expectation and variance of a random variable

Two numbers summarise a distribution, and they correspond exactly to the mean and the variance of a data set.

The expectation, also called the mean or the expected value, is the long-run average of the random variable. It is written $E(X)$ and spoken "the expectation of $X$". For a discrete variable it is calculated by multiplying each value by its probability and adding the products. The symbol $\mu$, the Greek letter mu, is the conventional name for this quantity. The expectation is not a value you expect to see; it is the balance point of the distribution. A fair die has expectation $3.5$, a number that can never be thrown.

The variance is the average squared distance from the expectation, written $\text{Var}(X)$ and often denoted $\sigma^{2}$, where $\sigma$ is the Greek letter sigma. Its square root $\sigma$ is the standard deviation, and it is in the same units as the random variable. A small $\sigma$ means the values cluster tightly around the mean; a large $\sigma$ means they are widely scattered. The word "average" in the definition is a probability-weighted average, so values that are unlikely count for little.

### 1.7 The three distributions in one paragraph each

The binomial distribution counts successes. Suppose an experiment is repeated a fixed number of times, each repetition has exactly two possible outcomes, the repetitions do not influence each other, and the chance of the outcome we are counting is the same every time. Then the total number of successes has a binomial distribution. The number of trials is written $n$ and the chance of success on one trial is written $p$. Tossing a coin ten times and counting heads is the standard picture, with $n = 10$ and $p = 0.5$.

The Poisson distribution counts rare events in a stretch of time, length, area or volume. It needs only one number: the average count in the stretch, written $\lambda$, the Greek letter lambda. If complaints arrive at an average of three per hour and the arrivals do not cluster, then the number in one hour has a Poisson distribution with $\lambda = 3$. The Poisson is the natural model when the count has no fixed upper limit and the events are individually unlikely.

The normal distribution describes measurements that cluster around a central value and thin out symmetrically on both sides. It needs two numbers: the centre $\mu$ and the spread $\sigma$. Its curve is the bell. Heights, weights, measurement errors, and the averages of large samples all tend to follow it.

### 1.8 Two more shapes: flat and decaying

Two further continuous shapes appear often enough to name.

A uniform distribution describes a quantity known only to lie between two limits, with no reason to prefer any part of the range. Picture a bus that is equally likely to arrive at any moment in the next ten minutes: the chance of arriving in any particular one-minute stretch is the same as for any other stretch of the same length. The picture is a rectangle, flat across the range and zero outside it. The average of a uniform on the interval from $a$ to $b$ is the midpoint $\frac{a + b}{2}$, which is what "no preference" ought to give.

An exponential distribution describes a waiting time until the next rare event. Picture the time until the next customer arrives at an otherwise quiet counter: short waits are common, long waits are rare, and the chance of waiting more than a given time falls away smoothly. The picture is a curve that is highest at zero and decays towards the right, never quite reaching the axis. Its one parameter is a rate, written $\lambda$, and it shares that parameter with the Poisson distribution, because a rate of arrivals and a waiting time between arrivals are two views of the same process.

### 1.9 The symbols used in this note

| Symbol | Spoken as | Meaning in words |
|---|---|---|
| $X$ | capital X | the random variable, the uncertain quantity |
| $x$ | small x | one particular value the variable might take |
| $P(X = x)$ | probability that X equals x | chance of that exact value |
| $n$ | n | number of trials in a binomial setting |
| $p$ | p | chance of success on a single trial |
| $1 - p$ | one minus p | chance of failure on a single trial |
| $\lambda$ | lambda | average number of events in a Poisson setting |
| $\mu$ | mu | mean or centre of a distribution |
| $\sigma$ | sigma | standard deviation, the typical distance from the centre |
| $z$ | z | number of standard deviations from the mean |
| $e$ | e | the constant about 2.71828, the base of natural growth |

Every symbol in that table is a name for something concrete. Nothing in the topic is more abstract than that table, and a reader who keeps the table in view can follow every formula below.

## 2. Theorems, Lemmas, and Analytical Properties

### 2.1 The rule that every distribution obeys

The first property is not a theorem about any particular shape but a condition that every shape must satisfy.

> **Property 1 (Total probability one).** For any discrete random variable, the probabilities of all possible values add to exactly one. For any continuous random variable, the total area under the density curve is exactly one.

This property is the arithmetic form of the statement "something must happen". It is also the fastest check on any calculation: if a set of probabilities adds to $0.9$ or to $1.1$, either a value has been missed or a probability has been calculated wrongly. Nearly every examination question that asks you to "find the constant" in a distribution is really asking you to impose this condition and solve for the unknown.

### 2.2 The binomial formula and what each piece does

> **Result 2 (Binomial probability).** If $X$ counts the successes in $n$ independent trials with constant success chance $p$, then

$$
P(X = x) = \binom{n}{x} p^{x}\left(1 - p\right)^{n - x}, \qquad x = 0, 1, \dots, n .
$$

The symbol $\binom{n}{x}$, read "n choose x", counts the number of different orders in which the successes could appear. Its value is the number of ways of choosing which $x$ of the $n$ positions are the successes.

The factor $p^{x}$ is the chance of those particular $x$ successes, one factor of $p$ for each of them. The factor $\left(1 - p\right)^{n - x}$ is the chance of the remaining $n - x$ failures. Multiplying the three pieces gives the chance of exactly $x$ successes in any one specified order, and multiplying by the number of orders gives the total.

A worked miniature makes the structure visible. With three tosses of a fair coin, the chance of exactly two heads is the chance of the sequences head-head-tail, head-tail-head and tail-head-head, three sequences, each with chance one eighth.

$$
P(X = 2) = \binom{3}{2}\left(\frac{1}{2}\right)^{2}\left(\frac{1}{2}\right)^{1} = 3 \times \frac{1}{8} = \frac{3}{8} = 0.375
$$

### 2.3 The mean and variance of a binomial variable

> **Result 3 (Binomial moments).** For $X$ binomial with $n$ trials and success chance $p$,

$$
E(X) = np, \qquad \text{Var}(X) = np\left(1 - p\right), \qquad \sigma = \sqrt{np\left(1 - p\right)} .
$$

The mean statement is the intuitive one: if a coin has a one-in-two chance of a head and you toss it ten times, you expect five heads, and $np = 10 \times 0.5 = 5$. The variance statement says that the spread is largest when $p = 0.5$ and shrinks to nothing as $p$ approaches zero or one, which is right: a coin that always lands heads produces no variation at all.

### 2.4 The Poisson formula and its single parameter

> **Result 4 (Poisson probability).** If $X$ counts events occurring at average rate $\lambda$ in a fixed interval, then

$$
P(X = x) = \frac{e^{-\lambda}\lambda^{x}}{x!}, \qquad x = 0, 1, 2, \dots
$$

The symbol $e$ is a fixed constant about $2.71828$, and $x!$, read "x factorial", is the product of all whole numbers from one up to $x$, with $0!$ defined as one. The formula has no upper limit on $x$, because in principle any number of events could occur.

> **Result 5 (Poisson moments).** For a Poisson variable with rate $\lambda$,

$$
E(X) = \lambda, \qquad \text{Var}(X) = \lambda, \qquad \sigma = \sqrt{\lambda} .
$$

The mean and the variance are the same number. That is the signature of the Poisson and the quickest way to recognise it in a question: if a single average is given and nothing else, the model is Poisson, and its spread is fixed by its centre.

### 2.5 The Poisson as a limit of the binomial

> **Result 6 (Poisson limit).** When $n$ is very large, $p$ is very small, and the product $np$ stays at a moderate value $\lambda$, the binomial probability of $x$ successes is closely approximated by the Poisson probability with rate $\lambda$.

The practical statement is that a binomial with many trials and a tiny success chance behaves like a Poisson with rate equal to the expected count. A thousand components each with a one-in-a-thousand chance of failing give an expected $1$ failure, and the Poisson with $\lambda = 1$ describes the count of failures well. The rule of thumb is that the approximation is good when $n$ is at least twenty and $p$ is at most $0.05$.

### 2.6 The normal density and its two parameters

> **Result 7 (Normal density).** A random variable is normally distributed with mean $\mu$ and standard deviation $\sigma$ when its density is

$$
f(x) = \frac{1}{\sigma\sqrt{2\pi}}\exp\left(-\frac{\left(x - \mu\right)^{2}}{2\sigma^{2}}\right),
$$

written $X \sim N\left(\mu, \sigma^{2}\right)$, where the symbol $\sim$ means "is distributed as" and $\pi$ is the constant about $3.14159$.

The curve has its peak at $x = \mu$ and is symmetric about that line. The constant in front is there purely to make the total area under the curve equal one. Changing $\mu$ slides the curve sideways without altering its shape. Changing $\sigma$ widens or narrows it: a larger $\sigma$ gives a lower and wider bell, a smaller $\sigma$ a taller and narrower one, and the area always stays at one.

### 2.7 The two named properties of the normal curve

The two properties that the examination names explicitly are the ones to quote in words.

Symmetrical means that the left half of the curve is the mirror image of the right half. The vertical line through the mean cuts the total area into two equal halves of $0.5$ each. A consequence is that the chance of being more than a given distance above the mean equals the chance of being that distance below it. Another consequence is that the mean, the median and the mode all sit at the same point.

Bell-shaped means the curve rises smoothly to a single rounded peak at the mean and falls away smoothly on both sides, flattening towards the horizontal axis without ever touching it. There is one hump, not two, and no sharp corners anywhere. Data that are bell-shaped have most of their values near the middle and progressively fewer as you move outwards.

### 2.8 Standardisation

> **Result 8 (Standardisation).** If $X \sim N\left(\mu, \sigma^{2}\right)$ and

$$
z = \frac{x - \mu}{\sigma},
$$

then $z$ has the standard normal distribution with mean zero and standard deviation one.

The formula subtracts the centre and divides by the spread. Subtracting moves the centre to zero; dividing rescales the spread to one. The result is a pure number with no units, which is why a weight in kilograms and a mark out of a hundred can be compared once both are standardised. A positive $z$ means the value is above the mean, a negative $z$ means below, and $z = 0$ means exactly at the mean. A value of $z = 2$ means two standard deviations above the mean, which is far out in the right tail.

### 2.9 The empirical rule

> **Result 9 (The 68-95-99.7 rule).** For a normally distributed variable, approximately $68$ per cent of the values lie within one standard deviation of the mean, approximately $95$ per cent within two standard deviations, and approximately $99.7$ per cent within three.

The rule converts a standard deviation into a picture. A class of heights with mean $170$ centimetres and standard deviation $8$ centimetres has about $68$ per cent of its members between $162$ and $178$ centimetres, about $95$ per cent between $154$ and $186$, and essentially everyone between $146$ and $194$. It also gives a quick judgement about how unusual a value is: beyond two standard deviations is uncommon, beyond three is very rare.

### 2.10 Recognising which distribution applies

| What the question describes | Distribution | Parameters |
|---|---|---|
| Fixed number of independent two-outcome trials, count successes | Binomial | $n$ and $p$ |
| Count of rare events in a time, length or area, average given | Poisson | $\lambda$ |
| Measurement clustering symmetrically about a centre | Normal | $\mu$ and $\sigma$ |
| One single trial with two outcomes | Bernoulli | $p$ only |

The table is the fastest route through a "state the distribution" question. Read the description, look for a fixed number of trials, an average rate, or a continuous measurement, and the row follows. Justifying the choice takes one sentence, but that sentence is usually worth a mark.

### 2.11 The additive property

> **Result 10 (Additivity).** If $X$ and $Y$ are independent Poisson variables with rates $\lambda_1$ and $\lambda_2$, then $X + Y$ is Poisson with rate $\lambda_1 + \lambda_2$. If $X$ and $Y$ are independent normal variables with means $\mu_1$, $\mu_2$ and variances $\sigma_1^{2}$, $\sigma_2^{2}$, then $X + Y$ is normal with mean $\mu_1 + \mu_2$ and variance $\sigma_1^{2} + \sigma_2^{2}$.

The word independent means that the two quantities do not influence each other. For the Poisson the property is intuitive: two counters counting different kinds of rare event in the same hour simply add their averages. For the normal the property is stronger than it looks, because variances add while standard deviations do not; two independent sources of error with standard deviations $3$ and $4$ combine to a variance of $9 + 16 = 25$ and hence a standard deviation of $5$, not of $7$.

Note that the binomial has a similar property in a narrower form: if two independent binomial variables share the same $p$, their sum is binomial with the trials added.

## 3. Formal Proofs, Derivations, and Methods

### 3.1 Checking that the binomial probabilities add to one

The claim is that the binomial formula always produces a set of probabilities that sums to one. The check is easiest on a case small enough to write out.

Step 1. Write down the four probabilities for three tosses of a fair coin, using the formula with $n = 3$ and $p = \frac{1}{2}$.

$$
P(X = 0) = \binom{3}{0}\left(\frac{1}{2}\right)^{0}\left(\frac{1}{2}\right)^{3} = 1 \times 1 \times \frac{1}{8} = 0.125
$$

$$
P(X = 1) = \binom{3}{1}\left(\frac{1}{2}\right)^{1}\left(\frac{1}{2}\right)^{2} = 3 \times \frac{1}{8} = 0.375
$$

$$
P(X = 2) = \binom{3}{2}\left(\frac{1}{2}\right)^{2}\left(\frac{1}{2}\right)^{1} = 3 \times \frac{1}{8} = 0.375
$$

$$
P(X = 3) = \binom{3}{3}\left(\frac{1}{2}\right)^{3}\left(\frac{1}{2}\right)^{0} = 1 \times \frac{1}{8} = 0.125
$$

Step 2. Add the four values.

$$
0.125 + 0.375 + 0.375 + 0.125 = 1.000
$$

The total is exactly one, as Property 1 requires.

The general reason is a single algebraic identity called the binomial theorem, which states that the expansion of the power of a sum produces exactly the binomial coefficients as multipliers.

$$
\left(a + b\right)^{n} = \sum_{x=0}^{n}\binom{n}{x} a^{x} b^{n - x}
$$

Putting $a = p$ and $b = 1 - p$ makes the left side equal $\left(p + 1 - p\right)^{n} = 1^{n} = 1$, and makes each term on the right identical to the binomial probability of $x$. The sum of all the binomial probabilities is therefore exactly one for every admissible $n$ and $p$, with no approximation anywhere.

### 3.2 Where the binomial mean comes from

The result $E(X) = np$ is best seen first on the three-toss example, where every value and probability is known.

Step 1. Multiply each value by its probability.

$$
0 \times 0.125 = 0, \qquad 1 \times 0.375 = 0.375, \qquad 2 \times 0.375 = 0.75, \qquad 3 \times 0.125 = 0.375
$$

Step 2. Add the four products.

$$
E(X) = 0 + 0.375 + 0.75 + 0.375 = 1.5
$$

Step 3. Compare with the formula.

$$
np = 3 \times 0.5 = 1.5
$$

The two agree. The structural reason is that the total count is the sum of $n$ separate indicators, one for each trial, each contributing one with probability $p$ and zero otherwise. Each indicator has mean $p$, and expectations add whether or not the trials are independent, so the total has mean $np$.

Step 4. Compute the variance in the same way and compare.

$$
E\left(X^{2}\right) = 0 + 1\left(0.375\right) + 4\left(0.375\right) + 9\left(0.125\right) = 0.375 + 1.5 + 1.125 = 3
$$

$$
\text{Var}(X) = E\left(X^{2}\right) - \left[E(X)\right]^{2} = 3 - 2.25 = 0.75
$$

Step 5. Compare with the formula.

$$
np\left(1 - p\right) = 3 \times 0.5 \times 0.5 = 0.75
$$

Again the two agree. The symbols $E\left(X^{2}\right)$ mean "the expectation of the square of $X$", which is not the same as the square of the expectation; the variance formula subtracts the square of the mean from the mean of the square, and the order matters.

### 3.3 Where the Poisson mean comes from

The same multiplication-by-probability rule applies to the Poisson, but the sum has infinitely many terms. The first few terms are enough to see the pattern with $\lambda = 2$.

Step 1. Compute the probabilities for the first four values.

$$
P(X = 0) = e^{-2} \approx 0.1353, \qquad P(X = 1) = 2e^{-2} \approx 0.2707
$$

$$
P(X = 2) = \frac{4e^{-2}}{2} = 2e^{-2} \approx 0.2707, \qquad P(X = 3) = \frac{8e^{-2}}{6} \approx 0.1804
$$

Step 2. Multiply each value by its probability and add, over the first four values only.

$$
0\left(0.1353\right) + 1\left(0.2707\right) + 2\left(0.2707\right) + 3\left(0.1804\right) = 0 + 0.2707 + 0.5414 + 0.5412 = 1.3533
$$

Step 3. Note that the remaining values add further positive contributions, so the full sum exceeds $1.3533$ and approaches $2$. The value $2$ is exactly $\lambda$, which is the general result.

Step 4. The algebraic reason is that the sum simplifies to a single term.

$$
E(X) = \sum_{x=0}^{\infty} x\,\frac{e^{-\lambda}\lambda^{x}}{x!} = e^{-\lambda}\lambda\sum_{x=1}^{\infty}\frac{\lambda^{x-1}}{\left(x - 1\right)!} = e^{-\lambda}\lambda\,e^{\lambda} = \lambda
$$

The step that removes the factor $x$ works because the term with $x = 0$ vanishes and every remaining term contains $\frac{x}{x!} = \frac{1}{\left(x - 1\right)!}$. The final sum over the shifted index is the power series for $e^{\lambda}$, so the two exponentials cancel. Repeating the calculation for $E\left(X^{2}\right)$ produces $\lambda^{2} + \lambda$, and subtracting $\lambda^{2}$ leaves a variance of exactly $\lambda$.

### 3.4 Why the normal density has total area one

The constant in front of the normal density is not arbitrary; it is chosen so that the total area equals one. The relevant integral is a standard result.

$$
\int_{-\infty}^{\infty} e^{-t^{2}}\,dt = \sqrt{\pi}
$$

This is the Gaussian integral, and it cannot be evaluated by finding an antiderivative; it is proved by squaring the integral and evaluating the resulting double integral in polar coordinates. Substituting $t = \frac{x - \mu}{\sigma\sqrt{2}}$ changes the variable and produces a factor of $\sigma\sqrt{2}$.

$$
\int_{-\infty}^{\infty}\exp\left(-\frac{\left(x - \mu\right)^{2}}{2\sigma^{2}}\right)dx = \sigma\sqrt{2\pi}
$$

Dividing by that factor gives the density of Result 7, and its total area is therefore exactly one for every choice of $\mu$ and $\sigma$. This is why the shape can be widened or narrowed without changing the total chance: the area is fixed at one and the curve redistributes it.

### 3.5 Method: computing a binomial probability

Step 1. Confirm the four conditions: a fixed number of trials $n$, two outcomes per trial, independence between trials, and a constant success chance $p$. Write down $n$ and $p$ explicitly.

Step 2. Identify the value $x$ asked for.

Step 3. Evaluate the binomial coefficient $\binom{n}{x}$ by counting orders or by using factorials.

Step 4. Evaluate $p^{x}$ and $\left(1 - p\right)^{n - x}$.

Step 5. Multiply the three pieces.

Step 6. Check that the answer lies between zero and one and that it is plausible by comparison with the mean $np$; a value far from the mean should carry a small probability.

### 3.6 Method: questions of the form at least one

Step 1. Recognise that "at least one" is the complement of "none", so the direct calculation is long and the complement is short.

Step 2. Compute the chance of none, which is the binomial probability with $x = 0$.

Step 3. Subtract from one.

$$
P(X \ge 1) = 1 - P(X = 0) = 1 - \left(1 - p\right)^{n}
$$

The same device answers "at least two", by subtracting the chances of none and of exactly one, and generally "at least $r$" by subtracting the chances of $0, 1, \dots, r-1$. The symbol $\ge$ means "greater than or equal to".

### 3.7 Method: computing a Poisson probability

Step 1. Identify the interval over which the average is quoted. If the question quotes a rate per hour and asks about two hours, multiply the rate by two before doing anything else.

Step 2. Write $\lambda$ for the average count in the interval the question actually asks about.

Step 3. Substitute the required $x$ into the formula, remembering that $0! = 1$ and that any number to the power zero is one.

Step 4. Evaluate $e^{-\lambda}$ with a calculator, keeping at least four decimal places.

Step 5. Multiply and round to four decimal places at the end, not in the middle.

### 3.8 Method: standardising and reading the table

Step 1. Write down $\mu$ and $\sigma$ from the question.

Step 2. Draw the bell and shade the region asked about.

Step 3. Convert each boundary to a $z$-value using $z = \frac{x - \mu}{\sigma}$.

Step 4. Look the $z$-value up in the standard normal table, which gives the area to the left of $z$.

Step 5. If the question asks for a right-hand tail, subtract the table value from one. If it asks for a region between two values, subtract the smaller area from the larger.

Step 6. Report the probability as a proportion, and as a percentage only if the question asks for one.

### 3.9 Method: deciding which distribution to use

Step 1. Ask whether the variable is a count or a measurement. A count leads to binomial or Poisson; a measurement leads to normal.

Step 2. If it is a count, ask whether there is a fixed number of trials. A fixed number of trials with a success chance leads to binomial.

Step 3. If there is no fixed number of trials and only an average rate is given, the model is Poisson.

Step 4. If the counts are large and no average rate is quoted, consider the normal approximation to the binomial, with $\mu = np$ and $\sigma = \sqrt{np\left(1 - p\right)}$.

Step 5. Write the model in the standard notation and state the parameters, then proceed with the corresponding formula.

## 4. Representative Worked Examples and Solutions

### 4.1 Problem: three tosses of a coin

A fair coin is tossed three times. Let $X$ be the number of heads. Find the distribution of $X$, its mean and its standard deviation, and the chance of at least two heads.

### 4.2 Solution: list the values, then use the formulas

Step 1. Check the four binomial conditions. There are $n = 3$ tosses, each toss gives a head or a tail, the tosses do not affect each other, and the chance of a head is $p = 0.5$ every time. So $X$ is binomial with $n = 3$ and $p = 0.5$.

Step 2. Compute the four probabilities, as in the earlier check.

$$
P(X = 0) = 0.125, \qquad P(X = 1) = 0.375, \qquad P(X = 2) = 0.375, \qquad P(X = 3) = 0.125
$$

Step 3. Confirm that they sum to one.

$$
0.125 + 0.375 + 0.375 + 0.125 = 1
$$

Step 4. Compute the mean.

$$
E(X) = np = 3 \times 0.5 = 1.5
$$

Step 5. Compute the variance and the standard deviation.

$$
\text{Var}(X) = np\left(1 - p\right) = 3 \times 0.5 \times 0.5 = 0.75
$$

$$
\sigma = \sqrt{0.75} \approx 0.866
$$

Step 6. Compute the chance of at least two heads by adding the two relevant probabilities.

$$
P(X \ge 2) = P(X = 2) + P(X = 3) = 0.375 + 0.125 = 0.5
$$

Step 7. Interpret. On average one and a half heads appear in three tosses, the typical distance from that average is about $0.87$ heads, and exactly half of all sequences contain two or more heads. The last figure can be checked by listing the eight sequences: four of them contain at least two heads.

### 4.3 Problem: defective items on a production line

A machine produces items of which one in five is defective, independently of all others. A sample of five items is taken. Find the chance that exactly two are defective, and the chance that at least one is defective.

### 4.4 Solution: two applications of one formula

Step 1. Identify the parameters. There are $n = 5$ items, each is defective or not, the items are independent, and $p = 0.2$.

Step 2. Compute the binomial coefficient and the two powers for $x = 2$.

$$
\binom{5}{2} = \frac{5 \times 4}{2 \times 1} = 10, \qquad \left(0.2\right)^{2} = 0.04, \qquad \left(0.8\right)^{3} = 0.512
$$

Step 3. Multiply.

$$
P(X = 2) = 10 \times 0.04 \times 0.512 = 0.2048
$$

Step 4. Compute the chance of none for the second part.

$$
P(X = 0) = \left(0.8\right)^{5} = 0.32768
$$

Step 5. Use the complement rule.

$$
P(X \ge 1) = 1 - 0.32768 = 0.67232
$$

Step 6. Interpret. About one sample in five contains exactly two defectives, and about two samples in three contain at least one. The answer to the second part is large because five independent chances of one in five accumulate quickly.

### 4.5 Problem: complaints arriving at a call centre

Complaints arrive at a call centre at an average of two per hour, independently. Find the chance of no complaints in an hour, of exactly three complaints, and of at least one complaint.

### 4.6 Solution: one parameter, three questions

Step 1. Choose the model. There is no fixed number of trials and only an average rate is given, so the count is Poisson with $\lambda = 2$.

Step 2. Compute the chance of none, using $0! = 1$ and $2^{0} = 1$.

$$
P(X = 0) = \frac{e^{-2}2^{0}}{0!} = e^{-2} \approx 0.1353
$$

Step 3. Compute the chance of exactly three.

$$
P(X = 3) = \frac{e^{-2}2^{3}}{3!} = \frac{8e^{-2}}{6} \approx \frac{8 \times 0.1353}{6} \approx 0.1804
$$

Step 4. Compute the chance of at least one by complement.

$$
P(X \ge 1) = 1 - e^{-2} \approx 1 - 0.1353 = 0.8647
$$

Step 5. Interpret. About thirteen hours in a hundred bring no complaints, about eighteen in a hundred bring exactly three, and about eighty-six in a hundred bring at least one.

Step 6. State the mean and spread for completeness.

$$
E(X) = 2, \qquad \text{Var}(X) = 2, \qquad \sigma = \sqrt{2} \approx 1.414
$$

### 4.7 Problem: a normal measurement

The mass of a packaged item is normally distributed with mean $70$ grams and standard deviation $10$ grams. Find the chance that an item has mass below $80$ grams, above $90$ grams, and between $60$ and $90$ grams.

### 4.8 Solution: standardise, then read the table

Step 1. Standardise the first boundary.

$$
z = \frac{80 - 70}{10} = \frac{10}{10} = 1
$$

Step 2. Read the standard normal table for $z = 1$, which gives the area to the left.

$$
P(X < 80) = P(Z < 1) \approx 0.8413
$$

Step 3. Standardise the second boundary.

$$
z = \frac{90 - 70}{10} = 2
$$

Step 4. Convert the left-hand area into a right-hand tail.

$$
P(X > 90) = 1 - P(Z < 2) \approx 1 - 0.9772 = 0.0228
$$

Step 5. Standardise both boundaries for the final part.

$$
z = \frac{60 - 70}{10} = -1, \qquad z = \frac{90 - 70}{10} = 2
$$

Step 6. Subtract the smaller area from the larger.

$$
P(60 < X < 90) = P(-1 < Z < 2) \approx 0.9772 - 0.1587 = 0.8185
$$

Step 7. Interpret. About eighty-four per cent of items are lighter than $80$ grams, only about two per cent exceed $90$ grams, and about eighty-two per cent lie between $60$ and $90$ grams. The third answer is consistent with the first two, since it excludes both tails.

### 4.9 Problem: using the empirical rule without a table

The heights of a large group of students are normally distributed with mean $170$ centimetres and standard deviation $8$ centimetres. Use the 68-95-99.7 rule to describe the spread, and state how unusual a height of $190$ centimetres is.

### 4.10 Solution: turn standard deviations into distances

Step 1. Compute one standard deviation either side of the mean.

$$
170 - 8 = 162, \qquad 170 + 8 = 178
$$

Step 2. Compute two standard deviations either side.

$$
170 - 16 = 154, \qquad 170 + 16 = 186
$$

Step 3. Compute three standard deviations either side.

$$
170 - 24 = 146, \qquad 170 + 24 = 194
$$

Step 4. Attach the percentages.

$$
P(162 < X < 178) \approx 0.68, \qquad P(154 < X < 186) \approx 0.95, \qquad P(146 < X < 194) \approx 0.997
$$

Step 5. Standardise the height in question.

$$
z = \frac{190 - 170}{8} = \frac{20}{8} = 2.5
$$

Step 6. Interpret. The height is two and a half standard deviations above the mean. By the rule, about ninety-five per cent of heights lie within two standard deviations, so a height beyond two and a half is fairly rare; and since ninety-nine and seven tenths per cent lie within three, it is not extraordinary. Roughly one student in a hundred would be that tall or taller.

### 4.11 Problem: choosing the model

For each situation, name the distribution and its parameters.

(a) A die is rolled twelve times and the number of sixes is counted.

(b) A switchboard receives calls at an average of five per hour and the number in one hour is recorded.

(c) The length of a machined bolt is measured.

(d) A single component either works or fails, with a one per cent chance of failure.

### 4.12 Solution: read the description, then match the row

Step 1. For (a), there are twelve fixed trials, each gives a six or not, the rolls are independent, and the chance of a six is constant. The model is binomial with $n = 12$ and $p = \frac{1}{6}$.

Step 2. For (b), there is no fixed number of trials and only an average rate per hour is given. The model is Poisson with $\lambda = 5$.

Step 3. For (c), the length is a continuous measurement clustering about a target. The model is normal, with the mean set to the target length and the standard deviation reflecting the precision of the machine.

Step 4. For (d), there is one trial only. The model is Bernoulli with $p = 0.01$ for failure, which is the binomial with $n = 1$.

Step 5. State the general principle. A fixed number of trials points to the binomial; an average rate over an interval points to the Poisson; a continuous measurement points to the normal; and a single trial is the degenerate binomial case.

### 4.13 Problem: a rare defect in a large batch

A factory produces a thousand components, each independently defective with probability $0.003$. Use the Poisson approximation to find the chance that exactly two are defective, and compare with the exact binomial value.

### 4.14 Solution: compute the rate, then apply the limit

Step 1. Compute the expected number of defectives.

$$
\lambda = np = 1000 \times 0.003 = 3
$$

Step 2. Apply the Poisson formula with $x = 2$.

$$
P(X = 2) = \frac{e^{-3}3^{2}}{2!} = \frac{9e^{-3}}{2} \approx 4.5 \times 0.04979 \approx 0.2240
$$

Step 3. Compute the exact binomial value for comparison.

$$
\binom{1000}{2}\left(0.003\right)^{2}\left(0.997\right)^{998} \approx 499500 \times 0.000009 \times 0.04986 \approx 0.2242
$$

Step 4. Compare. The two values agree to three decimal places, which is the expected outcome: a thousand trials with a success chance of three in a thousand is exactly the regime where the Poisson limit applies.

Step 5. Comment on the conditions. The number of trials is large, the success chance is small, and the product is moderate. All three conditions of Result 6 hold, so the approximation is justified rather than merely convenient.

## 5. Mathematical Extensions, Limits, and Common Errors

### 5.1 Mistakes beginners make most often

The first mistake is treating the density as a probability. A normal density can be greater than one when $\sigma$ is small, and reading a density value as "the chance of that value" produces impossible answers. For a continuous variable the chance of any single value is zero, and only areas carry probability.

The second mistake is forgetting that the binomial needs a fixed number of trials. The question "how many customers arrive before the shop closes" has no fixed upper limit, so it is not binomial even though each arrival is a success or failure.

The third mistake is using $p$ where $1 - p$ belongs, or the reverse. In the formula $p^{x}\left(1 - p\right)^{n - x}$ the exponent $x$ counts the successes, so $p$ must be the chance of the thing being counted. If the question asks for the number of non-defective items, then the chance of a non-defective item is the $p$ of the calculation.

The fourth mistake is forgetting the binomial coefficient. The term $p^{x}\left(1 - p\right)^{n - x}$ is the chance of one particular ordering of the successes, not of the count. Without the coefficient the answer is too small by the number of orderings, which for ten trials and three successes is a factor of one hundred and twenty.

The fifth mistake is mis-scaling the Poisson rate. If the average is three per hour and the question asks about two hours, the rate is six, not three. The rate must always match the interval in the question.

The sixth mistake is subtracting the wrong quantity from one. The complement of "at least one" is "none", the complement of "more than five" is "five or fewer", and the complement of "between two and four" is "below two or above four". Writing the complement down in words before computing prevents most errors of this kind.

The seventh mistake is standardising in the wrong direction, computing $\frac{\mu - x}{\sigma}$ instead of $\frac{x - \mu}{\sigma}$. The sign of $z$ then reverses and the tail is taken from the wrong end. A quick check is that a value above the mean must produce a positive $z$.

The eighth mistake is adding standard deviations instead of variances. Two independent errors with standard deviations $3$ and $4$ combine to a standard deviation of $5$, because $9 + 16 = 25$ and the square root of $25$ is $5$.

### 5.2 Where each model stops working

The binomial requires independence and a constant success chance. If items are drawn from a small batch without replacement, the chance changes after each draw and the correct model is the hypergeometric, which is not covered here but which the binomial approximates when the batch is large compared with the sample. If the trials influence each other, the binomial does not apply at all.

The Poisson requires a constant average rate and independence between events. If complaints arrive in bursts because one fault generates many calls, the events are not independent and the Poisson understates the frequency of large counts. The Poisson also fails when the rate changes over the interval, for example when a call centre is busier at midday than at midnight.

The normal requires approximate symmetry. Income, waiting times and claim sizes are strongly skewed and are not well described by a bell. The normal also fails for counts when the mean is small, because a normal curve assigns positive probability to negative values whereas a count cannot be negative. The usual guard is that the normal approximation to the binomial needs both $np$ and $n\left(1 - p\right)$ to be at least five, and preferably at least ten.

### 5.3 Reading a question for its model

A reliable habit is to underline three things in every question: whether the variable is a count or a measurement, whether a fixed number of trials is mentioned, and whether an average is quoted. Those three marks of the text determine the model almost every time. A second habit is to write the model in symbols before computing anything, because a stated model earns a mark and also exposes errors early: if the parameters written down do not match the numbers in the question, the mistake is caught before the arithmetic begins.

### 5.4 What comes next

The three distributions here are the foundation of all later statistical work. The binomial and the Poisson reappear in quality control and in the analysis of counts. The normal supplies the reference curve for confidence intervals and hypothesis tests, where a sample mean is standardised in exactly the way this topic standardises a single observation. The idea of a random variable, of a probability mass or density, and of expectation and variance as summaries of a distribution generalises to every model met later, so the vocabulary learned here is used unchanged throughout the rest of the subject.
