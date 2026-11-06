## 1. Foundational Concepts, Definitions, and Axioms

### 1.1 The probability space and the random variable

A probability model has three parts. The sample space $\Omega$ is the set of all outcomes of an experiment. A collection of events $\mathcal{F}$ is a family of subsets of $\Omega$ closed under complementation and countable union. A probability measure $P$ assigns to each event a number in $\left[0, 1\right]$ such that $P(\Omega) = 1$ and $P$ is countably additive on disjoint events. Every distribution discussed in this note lives inside such a triple, and every probability statement is ultimately a statement about $P$ applied to a set of outcomes.

> **Definition (Random variable).** A random variable is a function $X : \Omega \to \mathbb{R}$ such that for every real $x$ the set $\{\omega \in \Omega : X(\omega) \le x\}$ is an event. The last condition is a technical requirement: it guarantees that statements of the form "the value is at most $x$" always carry a probability. In practice every function met in a statistics course satisfies it, so the condition is stated once and then ignored.

The value $X(\omega)$ is the number attached to the outcome $\omega$. Writing $X$ for the function and $x$ for a value it assumes is standard, and the distinction is worth preserving: $X$ is the whole random quantity, $x$ is one point in its range.

Because the random variable pushes the probability measure forward from $\Omega$ onto the real line, questions about $X$ can be answered without referring back to $\Omega$. The object that records the pushed-forward probability is the distribution of $X$, and the two standard descriptions of it are the cumulative distribution function and, depending on type, either a mass function or a density.

### 1.2 Discrete random variables and probability mass functions

> **Definition (Discrete random variable).** A random variable is discrete when its set of possible values is finite or countably infinite.

> **Definition (Probability mass function).** For a discrete random variable the probability mass function is $p(x) = P(X = x)$. It must satisfy $p(x) \ge 0$ for every $x$ and

$$
\sum_{x} p(x) = 1,
$$

the sum being over the countable set of possible values.

The mass function is the complete description of a discrete distribution: two discrete random variables have the same distribution exactly when their mass functions agree. Probabilities of sets are obtained by summing, so $P(X \in A) = \sum_{x \in A} p(x)$.

### 1.3 Continuous random variables and probability density functions

> **Definition (Continuous random variable).** A random variable is continuous when there exists a function $f$, called the probability density function, such that for every real $x$

$$
F(x) = P(X \le x) = \int_{-\infty}^{x} f(t)\,dt .
$$

A density must satisfy $f(t) \ge 0$ everywhere and

$$
\int_{-\infty}^{\infty} f(t)\,dt = 1 .
$$

Three consequences follow at once and each is a frequent examination point. First, $P(X = x) = 0$ for every single point $x$, because the integral over an interval of zero length vanishes. Second, probabilities of intervals are obtained by integration, $P(a < X < b) = \int_{a}^{b} f(t)\,dt$, and the strictness of the inequalities at the endpoints is irrelevant. Third, the density is not a probability: it may exceed one, since only its integral is constrained. A density of $2.5$ over an interval of width $0.2$ contributes $0.5$ of probability, which is perfectly legitimate.

### 1.4 The cumulative distribution function

> **Definition (Cumulative distribution function).** The cumulative distribution function of any random variable is $F(x) = P(X \le x)$.

The cumulative function is defined for every real $x$ and for both types of variable, which is why it is the natural object for unifying the theory. Its defining properties are stated in Section 2. For a discrete variable it is a step function increasing by $p(x)$ at each possible value; for a continuous variable it is continuous, and where the density exists, $F'(x) = f(x)$.

Two identities convert a cumulative value into the probabilities of other regions.

$$
P(X > x) = 1 - F(x), \qquad P(a < X \le b) = F(b) - F(a)
$$

The second is the workhorse of computation, since every interval probability reduces to a difference of two cumulative values.

### 1.5 Expectation

> **Definition (Expectation).** For a discrete random variable taking values $x_1, x_2, \dots$ with mass function $p$, the expectation is

$$
E(X) = \sum_{i} x_i\,p\left(x_i\right),
$$

provided the sum converges absolutely. For a continuous random variable with density $f$ it is

$$
E(X) = \int_{-\infty}^{\infty} x\,f(x)\,dx,
$$

again provided the integral converges absolutely.

The absolute convergence condition excludes pathological cases in which a sum or integral exists only by cancellation of infinitely large positive and negative parts. When it fails the expectation is said not to exist, and no amount of algebra will produce a meaningful answer. Every distribution treated here has a finite expectation.

Expectation is linear, and linearity does not require independence. For constants $a$, $b$ and random variables $X$, $Y$,

$$
E(aX + b) = aE(X) + b, \qquad E(X + Y) = E(X) + E(Y) .
$$

The first identity is immediate from the definition and the second follows by exchanging a finite sum with the expectation. This linearity is the most heavily used property in the whole subject, and the derivations of Section 3 depend on it.

### 1.6 Variance

> **Definition (Variance).** The variance of a random variable with finite expectation $\mu = E(X)$ is

$$
\text{Var}(X) = E\left[\left(X - \mu\right)^{2}\right],
$$

and the standard deviation is $\sigma = \sqrt{\text{Var}(X)}$.

The computational identity

$$
\text{Var}(X) = E\left(X^{2}\right) - \left[E(X)\right]^{2}
$$

follows by expanding the square and using linearity. It is the form used in almost every calculation, because it needs only the two moments $E(X)$ and $E\left(X^{2}\right)$ rather than a sum of squared deviations from an unknown centre.

Variance is not linear. For constants $a$ and $b$,

$$
\text{Var}(aX + b) = a^{2}\text{Var}(X),
$$

so an additive shift leaves the spread untouched while a multiplicative change scales the variance by the square of the factor. For independent $X$ and $Y$ the variances add. The independence hypothesis is essential: without it a covariance term appears, and that term may be negative, so the variance of a sum can be smaller than either variance.

### 1.7 The Bernoulli distribution

> **Definition (Bernoulli distribution).** A random variable $X$ has the Bernoulli distribution with parameter $p \in \left[0, 1\right]$ when $X$ takes only the values $1$ and $0$, with $P(X = 1) = p$ and $P(X = 0) = 1 - p$.

The mass function can be written in the compact form $p(x) = p^{x}\left(1 - p\right)^{1 - x}$ for $x \in \{0, 1\}$, which checks out at both points. The moments follow from the definition.

$$
E(X) = 0\left(1 - p\right) + 1\left(p\right) = p
$$

$$
E\left(X^{2}\right) = 0^{2}\left(1 - p\right) + 1^{2}\left(p\right) = p, \qquad \text{Var}(X) = p - p^{2} = p\left(1 - p\right)
$$

The Bernoulli is the atom from which the binomial is built. Each individual trial of a binomial experiment is Bernoulli, and the binomial counts how many of the Bernoullis take the value one.

### 1.8 The binomial distribution

> **Definition (Binomial distribution).** Let an experiment consist of $n$ independent trials, each with two possible outcomes called success and failure, with success probability $p$ identical on every trial. Let $X$ be the number of successes. Then $X$ has the binomial distribution with parameters $n$ and $p$, written $X \sim B(n, p)$, and

$$
P(X = x) = \binom{n}{x} p^{x}\left(1 - p\right)^{n - x}, \qquad x = 0, 1, \dots, n .
$$

Four conditions are built into the definition and each must be checked before the formula may be used: a fixed number of trials; two mutually exclusive outcomes per trial; independence between trials; and a constant success probability. The derivation of the mass function is given in Section 3.1 and the verification that it sums to one in Section 3.2.

### 1.9 The Poisson distribution

> **Definition (Poisson distribution).** A random variable has the Poisson distribution with rate $\lambda > 0$, written $X \sim \text{Poisson}(\lambda)$, when

$$
P(X = x) = \frac{e^{-\lambda}\lambda^{x}}{x!}, \qquad x = 0, 1, 2, \dots
$$

The parameter $\lambda$ is the expected number of events in the interval to which the model refers. The model describes counts of events that occur singly, independently and at a constant average rate, with no fixed upper bound on the count. Section 3.5 shows that it arises as the limit of a binomial with many trials and small success probability, and Sections 3.6 and 3.7 establish the normalisation and the moments.

### 1.10 The continuous uniform distribution

> **Definition (Uniform distribution).** A random variable has the uniform distribution on the interval $\left[a, b\right]$ when its density is constant on that interval and zero outside:

$$
f(x) = \frac{1}{b - a}, \qquad a \le x \le b .
$$

The density is constant because every subinterval of the same length is equally likely. The moments are

$$
E(X) = \frac{a + b}{2}, \qquad \text{Var}(X) = \frac{\left(b - a\right)^{2}}{12} .
$$

The uniform is the continuous analogue of "all outcomes equally likely" and is the model for a quantity known only to lie between two bounds with no further information.

### 1.11 The exponential distribution

> **Definition (Exponential distribution).** A random variable has the exponential distribution with rate $\lambda > 0$ when its density is

$$
f(x) = \lambda e^{-\lambda x}, \qquad x \ge 0,
$$

and zero for negative $x$.

It models the waiting time until the next event in a Poisson process, which is why it shares the parameter $\lambda$ with the Poisson count. Its cumulative function is $F(x) = 1 - e^{-\lambda x}$ for $x \ge 0$, and its moments are

$$
E(X) = \frac{1}{\lambda}, \qquad \text{Var}(X) = \frac{1}{\lambda^{2}} .
$$

The exponential is the only continuous distribution with the memoryless property, $P(X > s + t \mid X > s) = P(X > t)$, which is the continuous counterpart of the independence assumption behind the Poisson.

### 1.12 The normal distribution

> **Definition (Normal distribution).** A random variable has the normal distribution with mean $\mu$ and variance $\sigma^{2}$, written $X \sim N\left(\mu, \sigma^{2}\right)$, when its density is

$$
f(x) = \frac{1}{\sigma\sqrt{2\pi}}\exp\left(-\frac{\left(x - \mu\right)^{2}}{2\sigma^{2}}\right), \qquad -\infty < x < \infty .
$$

The density is symmetric about $\mu$, attains its maximum there, and has points of inflection at $\mu \pm \sigma$. The parameter $\mu$ locates the curve and $\sigma$ controls its width. The normalisation constant is verified in Section 3.10, where the Gaussian integral is invoked.

The distribution function has no closed form in elementary functions, so probabilities are obtained from a table or a numerical routine applied to the standard case.

### 1.13 The standard normal distribution

> **Definition (Standard normal distribution).** The standard normal distribution is $N(0, 1)$, with density

$$
\phi(z) = \frac{1}{\sqrt{2\pi}}e^{-z^{2}/2}
$$

and distribution function $\Phi(z) = \int_{-\infty}^{z}\phi(t)\,dt$.

The capital $\Phi$ is the conventional symbol for the standard normal distribution function. Its values cannot be written down in closed form, but they are tabulated, and every normal probability reduces to them through standardisation.

### 1.14 The vocabulary collected

| Object | Notation | Role |
|---|---|---|
| Random variable | $X$ | the uncertain quantity |
| Mass function | $p(x)$ | probability of an exact value, discrete case |
| Density | $f(x)$ | integrand of probability, continuous case |
| Distribution function | $F(x)$ | probability of being at most $x$ |
| Expectation | $E(X)$ or $\mu$ | centre of gravity of the distribution |
| Variance | $\text{Var}(X)$ or $\sigma^{2}$ | mean squared distance from the centre |
| Standard normal function | $\Phi(z)$ | tabulated area to the left of $z$ |

## 2. Theorems, Lemmas, and Analytical Properties

### 2.1 Characterising properties of the distribution function

> **Theorem 1 (Properties of $F$).** A function $F$ is the distribution function of some random variable if and only if it is non-decreasing, right-continuous, $\lim_{x \to -\infty}F(x) = 0$ and $\lim_{x \to \infty}F(x) = 1$.

The four conditions are necessary because $F(x) = P(X \le x)$ inherits monotonicity from the monotonicity of the events $\{X \le x\}$, right-continuity from continuity of probability from above, and the two limits from the fact that the events shrink to the empty set and grow to the whole space. Sufficiency is a construction not needed here. In practice the conditions are used as a check: a proposed formula for $F$ that decreases somewhere, or that does not tend to one, cannot be a distribution function.

### 2.2 The law of the unconscious statistician

> **Theorem 2.** For a discrete $X$ with mass function $p$ and any function $g$ for which the expectation exists,

$$
E\left[g(X)\right] = \sum_{x} g(x)\,p(x),
$$

and for a continuous $X$ with density $f$,

$$
E\left[g(X)\right] = \int_{-\infty}^{\infty} g(x)\,f(x)\,dx .
$$

The content of the theorem is that the distribution of $g(X)$ need never be computed. The expectation of a function of $X$ is obtained by averaging the function against the distribution of $X$ itself. Every moment calculation in this topic is an application with $g(x) = x$ or $g(x) = x^{2}$.

### 2.3 Moments under linear transformations

> **Theorem 3.** For constants $a$ and $b$, $E(aX + b) = aE(X) + b$ and $\text{Var}(aX + b) = a^{2}\text{Var}(X)$.

The first is linearity. The second follows by writing the deviation of $aX + b$ from its mean.

$$
\left(aX + b\right) - \left(a\mu + b\right) = a\left(X - \mu\right)
$$

Squaring and taking expectations multiplies the variance by $a^{2}$, and the additive constant has disappeared. Taking square roots gives $\sigma_{aX+b} = \left|a\right|\sigma_{X}$.

Theorem 3 is what makes standardisation legitimate and what makes a change of units harmless. Multiplying every measurement by a constant rescales the standard deviation by the same constant and leaves every standardised value unchanged.

### 2.4 The binomial moments

> **Theorem 4.** If $X \sim B(n, p)$ then $E(X) = np$ and $\text{Var}(X) = np\left(1 - p\right)$.

The proof in Section 3.3 uses the representation of $X$ as a sum of independent Bernoulli variables, $X = I_1 + I_2 + \dots + I_n$, where $I_j$ is one when trial $j$ succeeds. Linearity gives the mean at once, and independence gives the variance as a sum of $n$ copies of $p\left(1 - p\right)$. A second proof through the moment generating function is sketched in Section 5.1.

### 2.5 The Poisson moments and the additivity property

> **Theorem 5.** If $X \sim \text{Poisson}(\lambda)$ then $E(X) = \lambda$ and $\text{Var}(X) = \lambda$.

> **Theorem 6 (Additivity of the Poisson).** If $X$ and $Y$ are independent Poisson variables with rates $\lambda_1$ and $\lambda_2$, then $X + Y \sim \text{Poisson}\left(\lambda_1 + \lambda_2\right)$.

Theorem 6 is proved most cleanly through moment generating functions, since the generating function of a Poisson is $\exp\left(\lambda\left(e^{t} - 1\right)\right)$ and the generating function of a sum of independent variables is the product. Multiplying the two factors adds the exponents, which is exactly the generating function of a Poisson with rate $\lambda_1 + \lambda_2$. Uniqueness of the generating function then identifies the distribution. The result may also be proved directly by summing over the ways in which $X + Y$ can equal a given value.

### 2.6 The normal distribution under linear transformation

> **Theorem 7.** If $X \sim N\left(\mu, \sigma^{2}\right)$ and $Y = aX + b$ with $a \ne 0$, then $Y \sim N\left(a\mu + b, a^{2}\sigma^{2}\right)$.

> **Corollary (Standardisation).** If $X \sim N\left(\mu, \sigma^{2}\right)$ then

$$
Z = \frac{X - \mu}{\sigma} \sim N(0, 1) .
$$

Theorem 7 says the normal family is closed under affine transformations, so a change of units leaves a normal variable normal. The corollary is the operational form: every normal probability statement can be rewritten as a statement about $Z$. The proof is a change of variable in the density, carried out in Section 3.11.

### 2.7 Symmetry identities

> **Theorem 8.** For $Z \sim N(0, 1)$ and any real $z$, $\Phi(-z) = 1 - \Phi(z)$.

The identity is a consequence of the symmetry of the density about zero, since the area below $-z$ mirrors the area above $z$. It is the reason the standard tables need list only positive arguments. Three further identities follow from it and from interval arithmetic.

$$
P(Z > z) = 1 - \Phi(z), \qquad P(a < Z < b) = \Phi(b) - \Phi(a), \qquad P\left(\left\lvert Z\right\rvert < z\right) = 2\Phi(z) - 1
$$

The last is the two-sided central probability, used whenever a question asks for the chance that a value lies within a stated distance of the mean in either direction.

### 2.8 The empirical rule as a table statement

> **Theorem 9 (68-95-99.7).** For $Z \sim N(0, 1)$, $\Phi(1) - \Phi(-1) \approx 0.6827$, $\Phi(2) - \Phi(-2) \approx 0.9545$ and $\Phi(3) - \Phi(-3) \approx 0.9973$.

The three numbers are not exact probabilities but rounded areas under the standard normal curve. They follow from table values $\Phi(1) = 0.8413$, $\Phi(2) = 0.9772$ and $\Phi(3) = 0.9987$, each rounded to four decimal places. Stated for a general normal variable, the rule says that about $68.27$ per cent of the distribution lies within one standard deviation of the mean, and similarly for two and three.

### 2.9 The normal approximation to the binomial

> **Theorem 10 (De Moivre-Laplace).** Let $X \sim B(n, p)$ and let

$$
Z_n = \frac{X - np}{\sqrt{np\left(1 - p\right)}} .
$$

Then $Z_n$ converges in distribution to $N(0, 1)$ as $n \to \infty$, for every fixed $p \in \left(0, 1\right)$.

The practical content is that for large $n$ the binomial distribution is well approximated by a normal distribution with the same mean and variance. Two refinements matter.

> **Lemma (Continuity correction).** Because a binomial variable is discrete while the normal is continuous, an event such as $X \le k$ should be treated as $X < k + 0.5$ before standardising, and $X \ge k$ as $X > k - 0.5$. An interval $a \le X \le b$ becomes $a - 0.5 < X < b + 0.5$.

The correction shifts each boundary half a unit outwards, capturing the whole of the discrete bar centred at the boundary value. Ignoring it biases every one-sided answer towards the centre, and the error can reach about $0.02$ for moderate $n$, which is enough to lose a mark.

> **Conditions of validity.** The approximation is conventionally accepted when $np \ge 5$ and $n\left(1 - p\right) \ge 5$, and it is good when both exceed $10$. When either product is smaller the binomial is too skewed for a symmetric curve to describe it, and the Poisson approximation is preferred if $p$ is small.

### 2.10 The Poisson approximation to the binomial

> **Theorem 11 (Poisson limit).** Let $X_n \sim B\left(n, p_n\right)$ with $np_n \to \lambda$ as $n \to \infty$. Then for each fixed $x$,

$$
P\left(X_n = x\right) \to \frac{e^{-\lambda}\lambda^{x}}{x!} .
$$

The limit is derived in Section 3.5. The practical rule is to use the Poisson approximation when $n \ge 20$, $p \le 0.05$ and $\lambda = np$ is moderate, say between $0.1$ and $10$. Under those conditions the two sets of probabilities agree to three decimal places for the values that carry most of the mass.

### 2.11 Conditions of use, side by side

| Model | Fixed trials | Constant probability | Independence | Continuous | Parameters |
|---|---|---|---|---|---|
| Bernoulli | one trial | yes | not applicable | no | $p$ |
| Binomial | yes | yes | yes | no | $n$, $p$ |
| Poisson | no | rate constant in time | events independent | no | $\lambda$ |
| Uniform | not applicable | not applicable | not applicable | yes | $a$, $b$ |
| Exponential | not applicable | rate constant in time | events independent | yes | $\lambda$ |
| Normal | not applicable | not applicable | not applicable | yes | $\mu$, $\sigma$ |

Reading the table across the first three columns separates the two counting models, which is the discrimination most often required. Reading the fourth column separates counting from measuring. If a question mentions a fixed number of trials, the binomial row is the only candidate; if it mentions an average rate with no fixed number of trials, the Poisson row is the only candidate.

### 2.12 A distribution-free bound

> **Theorem 12 (Chebyshev's inequality).** For any random variable with finite mean $\mu$ and finite variance $\sigma^{2}$, and any $k > 0$,

$$
P\left(\left\lvert X - \mu\right\rvert \ge k\sigma\right) \le \frac{1}{k^{2}} .
$$

The inequality requires no assumption about the shape of the distribution, which is its whole point. It says that no distribution whatsoever can place more than one part in $k^{2}$ of its probability beyond $k$ standard deviations from the mean. For $k = 2$ the bound is $0.25$, far weaker than the normal value of about $0.0455$, but it holds universally. The inequality is the standard tool for showing that an average concentrates around its mean, and it is the reason the empirical rule cannot be very badly wrong for any distribution with a finite variance.

### 2.13 The moment generating function

> **Definition.** The moment generating function of $X$ is $M_X(t) = E\left(e^{tX}\right)$, defined for those $t$ where the expectation is finite.

If the generating function exists in a neighbourhood of zero, its derivatives at zero give the moments, $M_X^{(r)}(0) = E\left(X^{r}\right)$, and the function determines the distribution uniquely. Moreover, for independent $X$ and $Y$, $M_{X+Y}(t) = M_X(t)M_Y(t)$. These three facts turn many derivations into one-line calculations and are used for the binomial, the Poisson and the normal in Section 5.1.

The generating functions are

$$
M_{B(n,p)}(t) = \left(1 - p + pe^{t}\right)^{n}, \qquad M_{\text{Poisson}(\lambda)}(t) = \exp\left(\lambda\left(e^{t} - 1\right)\right), \qquad M_{N(\mu,\sigma^{2})}(t) = \exp\left(\mu t + \frac{1}{2}\sigma^{2}t^{2}\right) .
$$

Differentiating the first twice at zero produces $np$ and $np\left(1 - p\right) + n^{2}p^{2}$, the second produces $\lambda$ and $\lambda + \lambda^{2}$, and the third produces $\mu$ and $\sigma^{2} + \mu^{2}$. In each case subtracting the square of the first derivative from the second gives the stated variance.

## 3. Formal Proofs, Derivations, and Methods

### 3.1 Derivation of the binomial mass function

Let the $n$ trials be performed and label the outcome of trial $j$ by $I_j$, equal to one on success and zero on failure. The event $\{X = x\}$ occurs exactly when $x$ of the indicators equal one.

Step 1. Fix one particular arrangement of $x$ successes and $n - x$ failures, say the successes in positions $1, \dots, x$. By independence, the probability of that arrangement is the product of the individual probabilities.

$$
P\left(I_1 = 1, \dots, I_x = 1, I_{x+1} = 0, \dots, I_n = 0\right) = p^{x}\left(1 - p\right)^{n - x}
$$

Step 2. Observe that the probability depends only on the number of successes, not on their positions, because every arrangement contributes the same $x$ factors of $p$ and the same $n - x$ factors of $1 - p$.

Step 3. Count the arrangements. Choosing which $x$ of the $n$ positions carry a success is a choice of $x$ objects from $n$, and the number of such choices is

$$
\binom{n}{x} = \frac{n!}{x!\left(n - x\right)!} .
$$

Step 4. Add the probabilities of the disjoint arrangements.

$$
P(X = x) = \binom{n}{x} p^{x}\left(1 - p\right)^{n - x}
$$

The derivation shows why the coefficient is indispensable. It is the count of ways the count $x$ can be achieved, and the remaining factor is the probability of any one of those ways.

### 3.2 The binomial probabilities sum to one

Step 1. Sum the mass function over its whole support.

$$
\sum_{x=0}^{n} P(X = x) = \sum_{x=0}^{n}\binom{n}{x} p^{x}\left(1 - p\right)^{n - x}
$$

Step 2. Recognise the right side as the binomial expansion of a power of a sum. The binomial theorem states that for any numbers $a$ and $b$ and any non-negative integer $n$,

$$
\left(a + b\right)^{n} = \sum_{x=0}^{n}\binom{n}{x} a^{x} b^{n - x} .
$$

Step 3. Apply the theorem with $a = p$ and $b = 1 - p$.

$$
\sum_{x=0}^{n}\binom{n}{x} p^{x}\left(1 - p\right)^{n - x} = \left(p + 1 - p\right)^{n} = 1^{n} = 1
$$

The sum is therefore exactly one for every $n$ and every $p$, with no approximation involved. The same argument applied with $b = 1$ and $a$ arbitrary gives the identity $\sum_{x}\binom{n}{x}a^{x} = \left(1 + a\right)^{n}$, which is used again in deriving the moment generating function.

### 3.3 The mean of the binomial

Step 1. Write $X$ as a sum of indicators.

$$
X = \sum_{j=1}^{n} I_j
$$

Step 2. Apply linearity of expectation, which needs no independence assumption.

$$
E(X) = \sum_{j=1}^{n} E\left(I_j\right) = \sum_{j=1}^{n} p = np
$$

The step is short but the reasoning behind it is the important part: each trial contributes its own small expected count $p$, and the total expected count is the sum of those contributions. No distribution of $X$ was required.

### 3.4 The variance of the binomial

Step 1. Use the indicator representation and independence.

$$
\text{Var}(X) = \text{Var}\left(\sum_{j=1}^{n} I_j\right) = \sum_{j=1}^{n}\text{Var}\left(I_j\right) + 2\sum_{i < j}\text{Cov}\left(I_i, I_j\right)
$$

Step 2. Note that independence makes every covariance zero, since $\text{Cov}\left(I_i, I_j\right) = E\left(I_iI_j\right) - E\left(I_i\right)E\left(I_j\right) = p^{2} - p^{2} = 0$.

Step 3. Use the Bernoulli variance computed in Section 1.7 and add.

$$
\text{Var}(X) = \sum_{j=1}^{n} p\left(1 - p\right) = np\left(1 - p\right)
$$

The variance is largest at $p = \frac{1}{2}$, where it equals $\frac{n}{4}$, and tends to zero as $p$ approaches either endpoint. Both facts match intuition: a fair coin produces the most variability a coin can produce, and a coin with two identical faces produces none.

### 3.5 The Poisson limit of the binomial

Take $X_n \sim B\left(n, p_n\right)$ with $p_n = \frac{\lambda}{n}$, so that the expected count is $\lambda$ for every $n$. Fix $x$ and expand the mass function.

$$
P\left(X_n = x\right) = \frac{n\left(n - 1\right)\cdots\left(n - x + 1\right)}{x!}\left(\frac{\lambda}{n}\right)^{x}\left(1 - \frac{\lambda}{n}\right)^{n - x}
$$

Step 1. Separate the three factors that behave differently.

$$
P\left(X_n = x\right) = \frac{\lambda^{x}}{x!}\cdot\frac{n\left(n - 1\right)\cdots\left(n - x + 1\right)}{n^{x}}\cdot\left(1 - \frac{\lambda}{n}\right)^{n}\left(1 - \frac{\lambda}{n}\right)^{-x}
$$

Step 2. Evaluate the second factor as $n \to \infty$. It contains $x$ factors, each of the form $1 - \frac{j}{n}$ with $j$ fixed between $0$ and $x - 1$.

$$
\lim_{n \to \infty}\frac{n\left(n - 1\right)\cdots\left(n - x + 1\right)}{n^{x}} = \lim_{n \to \infty}\prod_{j=0}^{x-1}\left(1 - \frac{j}{n}\right) = 1
$$

Step 3. Evaluate the third factor using the standard limit $\left(1 + \frac{u}{n}\right)^{n} \to e^{u}$ with $u = -\lambda$.

$$
\lim_{n \to \infty}\left(1 - \frac{\lambda}{n}\right)^{n} = e^{-\lambda}, \qquad \lim_{n \to \infty}\left(1 - \frac{\lambda}{n}\right)^{-x} = 1
$$

Step 4. Multiply the limits.

$$
\lim_{n \to \infty} P\left(X_n = x\right) = \frac{\lambda^{x}}{x!}\cdot 1 \cdot e^{-\lambda}\cdot 1 = \frac{e^{-\lambda}\lambda^{x}}{x!}
$$

The result is the Poisson mass function. The derivation also explains the conditions under which the approximation is trustworthy: $p$ must be small so that $1 - \frac{\lambda}{n}$ is close to one, $n$ must be large so that the exponent $n$ can produce the exponential limit, and $\lambda$ must be moderate so that the values of $x$ that matter are small compared with $n$.

### 3.6 The Poisson probabilities sum to one

Step 1. Sum the mass function over all non-negative integers.

$$
\sum_{x=0}^{\infty}\frac{e^{-\lambda}\lambda^{x}}{x!} = e^{-\lambda}\sum_{x=0}^{\infty}\frac{\lambda^{x}}{x!}
$$

Step 2. Recognise the power series of the exponential function.

$$
e^{\lambda} = \sum_{x=0}^{\infty}\frac{\lambda^{x}}{x!}
$$

Step 3. Substitute.

$$
e^{-\lambda}\sum_{x=0}^{\infty}\frac{\lambda^{x}}{x!} = e^{-\lambda}e^{\lambda} = 1
$$

The series converges absolutely for every real $\lambda$, so the interchange of summation and the exponential factor is legitimate. This is the discrete counterpart of the Gaussian integral used for the normal: in both cases the normalising constant is exactly what makes the total mass equal one.

### 3.7 The Poisson moments

Step 1. Compute the mean by shifting the index.

$$
E(X) = \sum_{x=0}^{\infty} x\,\frac{e^{-\lambda}\lambda^{x}}{x!} = e^{-\lambda}\lambda\sum_{x=1}^{\infty}\frac{\lambda^{x-1}}{\left(x - 1\right)!} = e^{-\lambda}\lambda e^{\lambda} = \lambda
$$

The term with $x = 0$ vanishes because of the factor $x$, and for $x \ge 1$ the ratio $\frac{x}{x!}$ equals $\frac{1}{\left(x - 1\right)!}$.

Step 2. Compute the factorial moment in the same way.

$$
E\left[X\left(X - 1\right)\right] = \sum_{x=0}^{\infty} x\left(x - 1\right)\frac{e^{-\lambda}\lambda^{x}}{x!} = e^{-\lambda}\lambda^{2}\sum_{x=2}^{\infty}\frac{\lambda^{x-2}}{\left(x - 2\right)!} = \lambda^{2}
$$

Step 3. Convert the factorial moment into the second moment.

$$
E\left(X^{2}\right) = E\left[X\left(X - 1\right)\right] + E(X) = \lambda^{2} + \lambda
$$

Step 4. Subtract the square of the mean.

$$
\text{Var}(X) = \lambda^{2} + \lambda - \lambda^{2} = \lambda
$$

The equality of mean and variance is the defining numerical signature of the Poisson. In data analysis it is used as a diagnostic: a count whose sample variance greatly exceeds its sample mean is over-dispersed and the Poisson model is suspect.

### 3.8 The uniform distribution: normalisation and moments

Step 1. Check the total area.

$$
\int_{a}^{b}\frac{1}{b - a}\,dx = \frac{b - a}{b - a} = 1
$$

Step 2. Compute the mean.

$$
E(X) = \int_{a}^{b}\frac{x}{b - a}\,dx = \frac{1}{b - a}\left[\frac{x^{2}}{2}\right]_{a}^{b} = \frac{b^{2} - a^{2}}{2\left(b - a\right)} = \frac{a + b}{2}
$$

Step 3. Compute the second moment.

$$
E\left(X^{2}\right) = \frac{1}{b - a}\left[\frac{x^{3}}{3}\right]_{a}^{b} = \frac{b^{3} - a^{3}}{3\left(b - a\right)} = \frac{a^{2} + ab + b^{2}}{3}
$$

Step 4. Subtract the square of the mean and simplify.

$$
\text{Var}(X) = \frac{a^{2} + ab + b^{2}}{3} - \frac{\left(a + b\right)^{2}}{4} = \frac{4a^{2} + 4ab + 4b^{2} - 3a^{2} - 6ab - 3b^{2}}{12} = \frac{\left(b - a\right)^{2}}{12}
$$

The variance depends only on the width, as it must, since shifting the interval cannot alter the spread.

### 3.9 The exponential distribution: normalisation, moments and memorylessness

Step 1. Check the total area.

$$
\int_{0}^{\infty}\lambda e^{-\lambda x}\,dx = \left[-e^{-\lambda x}\right]_{0}^{\infty} = 0 - \left(-1\right) = 1
$$

Step 2. Derive the distribution function by integrating from zero to $x$.

$$
F(x) = \int_{0}^{x}\lambda e^{-\lambda t}\,dt = 1 - e^{-\lambda x}, \qquad x \ge 0
$$

Step 3. Compute the mean by parts, or by the substitution $u = \lambda x$.

$$
E(X) = \int_{0}^{\infty} x\lambda e^{-\lambda x}\,dx = \frac{1}{\lambda}\int_{0}^{\infty} u e^{-u}\,du = \frac{1}{\lambda}
$$

Step 4. Compute the second moment in the same way.

$$
E\left(X^{2}\right) = \frac{1}{\lambda^{2}}\int_{0}^{\infty} u^{2}e^{-u}\,du = \frac{2}{\lambda^{2}}
$$

Step 5. Subtract the square of the mean.

$$
\text{Var}(X) = \frac{2}{\lambda^{2}} - \frac{1}{\lambda^{2}} = \frac{1}{\lambda^{2}}
$$

Step 6. Establish the memoryless property.

$$
P\left(X > s + t \mid X > s\right) = \frac{P\left(X > s + t\right)}{P\left(X > s\right)} = \frac{e^{-\lambda\left(s + t\right)}}{e^{-\lambda s}} = e^{-\lambda t} = P(X > t)
$$

The conditioning makes no difference to the remaining waiting time, which is a property unique to the exponential among continuous distributions.

### 3.10 The normal density integrates to one

Step 1. Write the integral to be evaluated.

$$
I = \int_{-\infty}^{\infty}\frac{1}{\sigma\sqrt{2\pi}}\exp\left(-\frac{\left(x - \mu\right)^{2}}{2\sigma^{2}}\right)dx
$$

Step 2. Substitute $t = \frac{x - \mu}{\sigma\sqrt{2}}$, so that $dx = \sigma\sqrt{2}\,dt$.

$$
I = \frac{\sigma\sqrt{2}}{\sigma\sqrt{2\pi}}\int_{-\infty}^{\infty} e^{-t^{2}}\,dt = \frac{1}{\sqrt{\pi}}\int_{-\infty}^{\infty} e^{-t^{2}}\,dt
$$

Step 3. Invoke the Gaussian integral, a standard result that is established by squaring the integral and passing to polar coordinates.

$$
\int_{-\infty}^{\infty} e^{-t^{2}}\,dt = \sqrt{\pi}
$$

Step 4. Substitute and conclude.

$$
I = \frac{1}{\sqrt{\pi}}\cdot\sqrt{\pi} = 1
$$

The constant $\frac{1}{\sigma\sqrt{2\pi}}$ is therefore exactly the normalising factor, and no other constant would make the density integrate to one. The location $\mu$ does not appear in the final calculation because the substitution removed it; this is the analytic expression of the fact that shifting the curve cannot change its total area.

### 3.11 Derivation of standardisation

Step 1. Let $X \sim N\left(\mu, \sigma^{2}\right)$ and let $Z = \frac{X - \mu}{\sigma}$, so that $X = \mu + \sigma Z$.

Step 2. Apply Theorem 3 to obtain the moments of $Z$.

$$
E(Z) = \frac{E(X) - \mu}{\sigma} = 0, \qquad \text{Var}(Z) = \frac{\text{Var}(X)}{\sigma^{2}} = 1
$$

Step 3. Establish normality of $Z$ by a change of variable in the density. The distribution function of $Z$ is

$$
P(Z \le z) = P\left(X \le \mu + \sigma z\right) = \int_{-\infty}^{\mu + \sigma z}\frac{1}{\sigma\sqrt{2\pi}}\exp\left(-\frac{\left(x - \mu\right)^{2}}{2\sigma^{2}}\right)dx .
$$

Step 4. Substitute $x = \mu + \sigma u$, so that $dx = \sigma\,du$ and the limits become $-\infty$ and $z$.

$$
P(Z \le z) = \int_{-\infty}^{z}\frac{1}{\sqrt{2\pi}}e^{-u^{2}/2}\,du = \Phi(z)
$$

The distribution function of $Z$ is therefore the standard normal function, which proves both the normality and the parameters. The argument also shows that the standardisation is not a statistical trick but a genuine change of variable, and that it is available for any normal variable whatever its mean and variance.

### 3.12 Method: the normal approximation with continuity correction

Step 1. Confirm $np \ge 5$ and $n\left(1 - p\right) \ge 5$; otherwise stop and use the binomial or the Poisson.

Step 2. Compute $\mu = np$ and $\sigma = \sqrt{np\left(1 - p\right)}$.

Step 3. Rewrite the event as an interval on the continuous scale, applying the half-unit correction. The event $X \le k$ becomes $X < k + 0.5$; the event $X \ge k$ becomes $X > k - 0.5$; the event $a \le X \le b$ becomes $a - 0.5 < X < b + 0.5$; and the event $X = k$ becomes $k - 0.5 < X < k + 0.5$.

Step 4. Standardise each boundary with $z = \frac{x - \mu}{\sigma}$.

Step 5. Convert the standardised interval into a difference of $\Phi$ values.

Step 6. Report the answer and, where the exact binomial value is available, state the size of the approximation error.

The correction always widens the interval by half a unit at each finite end. A common error is to apply the correction only to the upper end of a two-sided interval, which breaks the symmetry and produces an answer that is too small.

### 3.13 Method: using the standard normal table

Step 1. Sketch the bell and shade the required region. The sketch decides which tail and which subtraction are needed, and it takes five seconds.

Step 2. Standardise the boundary or boundaries.

Step 3. If the required area is to the left of $z$, read $\Phi(z)$ directly. If it is to the right, compute $1 - \Phi(z)$. If it is between two values, compute $\Phi\left(z_2\right) - \Phi\left(z_1\right)$.

Step 4. Where only a positive-$z$ table is available, use $\Phi(-z) = 1 - \Phi(z)$ for negative arguments.

Step 5. Where the argument lies beyond the tabulated range, use $\Phi(z) \approx 1$ for $z > 4$ and note that the tail is negligible.

Step 6. Round the final probability to four decimal places and express it as a percentage only when the question asks for one.

## 4. Representative Worked Examples and Solutions

### 4.1 Problem: a binomial count with a full summary

A multiple-choice test has ten questions, each with five options of which exactly one is correct. A candidate guesses every answer. Let $X$ be the number of correct answers. Find $P(X = 3)$, $P(X \ge 1)$, the mean, the variance and the standard deviation, and comment on the candidate's prospects.

### 4.2 Solution: identify, compute, interpret

Step 1. Verify the four binomial conditions. There are $n = 10$ questions; each answer is right or wrong; the guesses are independent; and the chance of a correct guess is $p = \frac{1}{5} = 0.2$ on every question. Hence $X \sim B(10, 0.2)$.

Step 2. Evaluate the pieces of the formula for $x = 3$.

$$
\binom{10}{3} = 120, \qquad \left(0.2\right)^{3} = 0.008, \qquad \left(0.8\right)^{7} = 0.2097152
$$

Step 3. Multiply.

$$
P(X = 3) = 120 \times 0.008 \times 0.2097152 \approx 0.2013
$$

Step 4. Compute the chance of no correct answers, which is the whole of the failure factor.

$$
P(X = 0) = \left(0.8\right)^{10} \approx 0.1074
$$

Step 5. Apply the complement rule.

$$
P(X \ge 1) = 1 - 0.1074 = 0.8926
$$

Step 6. Compute the moments.

$$
E(X) = np = 10 \times 0.2 = 2, \qquad \text{Var}(X) = np\left(1 - p\right) = 10 \times 0.2 \times 0.8 = 1.6
$$

$$
\sigma = \sqrt{1.6} \approx 1.2649
$$

Step 7. Interpret. The candidate expects two correct answers, with a typical departure of about $1.26$, and has about a one-in-five chance of getting exactly three. There is roughly an eleven per cent chance of scoring nothing at all. The distribution is skewed to the right because $p$ is below one half, so the mean exceeds the median, a point worth stating when a question asks for a comment on shape.

### 4.3 Problem: a Poisson count with a cumulative probability

Calls arrive at a switchboard at an average of four per hour, independently. Find $P(X = 2)$, $P(X \le 3)$ and $P(X \ge 1)$ for a one-hour period, and the standard deviation of the count.

### 4.4 Solution: one rate, a recursive evaluation

Step 1. Identify the model. No fixed number of trials is mentioned and an average rate over a fixed period is given, so $X \sim \text{Poisson}(4)$.

Step 2. Compute the value at zero, which anchors the recursion.

$$
P(X = 0) = e^{-4} \approx 0.0183
$$

Step 3. Obtain the next values by the recursion $P(X = x) = \frac{\lambda}{x}P(X = x - 1)$, which is exact and avoids repeated exponentiation.

$$
P(X = 1) = \frac{4}{1}\left(0.0183\right) \approx 0.0733
$$

$$
P(X = 2) = \frac{4}{2}\left(0.0733\right) \approx 0.1465
$$

$$
P(X = 3) = \frac{4}{3}\left(0.1465\right) \approx 0.1954
$$

Step 4. Add the four values for the cumulative probability.

$$
P(X \le 3) = 0.0183 + 0.0733 + 0.1465 + 0.1954 \approx 0.4335
$$

Step 5. Use the complement for the final part.

$$
P(X \ge 1) = 1 - P(X = 0) = 1 - 0.0183 = 0.9817
$$

Step 6. Compute the standard deviation.

$$
\sigma = \sqrt{\lambda} = \sqrt{4} = 2
$$

Step 7. Interpret. About forty-three per cent of hours bring three calls or fewer, and about ninety-eight per cent bring at least one. The mean and the variance are both $4$, so the standard deviation is $2$, which is half the mean: counts with a small mean are relatively more variable than counts with a large one, since the ratio $\frac{\sigma}{\mu} = \frac{1}{\sqrt{\lambda}}$ falls as $\lambda$ grows.

### 4.5 Problem: several normal probabilities

A variable is normally distributed with mean $100$ and standard deviation $15$. Find $P(X < 120)$, $P(85 < X < 115)$ and $P(X > 130)$.

### 4.6 Solution: standardise each boundary

Step 1. Standardise the first boundary.

$$
z = \frac{120 - 100}{15} = 1.3333
$$

Step 2. Read the table at $z = 1.33$.

$$
P(X < 120) = \Phi(1.33) \approx 0.9082
$$

Step 3. Standardise the two boundaries of the central interval.

$$
z_1 = \frac{85 - 100}{15} = -1, \qquad z_2 = \frac{115 - 100}{15} = 1
$$

Step 4. Subtract.

$$
P(85 < X < 115) = \Phi(1) - \Phi(-1) = 0.8413 - 0.1587 = 0.6826
$$

Step 5. Standardise the last boundary and take the upper tail.

$$
z = \frac{130 - 100}{15} = 2, \qquad P(X > 130) = 1 - \Phi(2) = 1 - 0.9772 = 0.0228
$$

Step 6. Interpret. About ninety-one per cent of values lie below $120$, about sixty-eight per cent lie within one standard deviation of the mean, and only about two per cent exceed $130$. The central figure illustrates the empirical rule: for a normal distribution, one standard deviation either side of the mean captures roughly $68$ per cent, and the table confirms it to four decimal places.

Step 7. Check consistency. The three answers refer to overlapping and complementary regions, and their magnitudes are in the expected order: the central interval is the most likely, the moderate upper region next, and the far tail smallest.

### 4.7 Problem: the normal approximation with and without the correction

A coin is biased so that the chance of a head is $0.4$. It is tossed $100$ times. Use the normal approximation to find $P(X \le 45)$, and compare with the answer obtained without the continuity correction and with the exact binomial value.

### 4.8 Solution: correct the boundary, then standardise

Step 1. Check the conditions. Here $np = 40$ and $n\left(1 - p\right) = 60$, both far above $5$, so the approximation is justified.

Step 2. Compute the mean and standard deviation.

$$
\mu = np = 100 \times 0.4 = 40, \qquad \sigma = \sqrt{100 \times 0.4 \times 0.6} = \sqrt{24} \approx 4.8990
$$

Step 3. Apply the continuity correction, replacing $X \le 45$ by $X < 45.5$.

Step 4. Standardise.

$$
z = \frac{45.5 - 40}{4.8990} = \frac{5.5}{4.8990} \approx 1.1227
$$

Step 5. Read the table at $z = 1.12$.

$$
P(X \le 45) \approx \Phi(1.12) \approx 0.8686
$$

Step 6. Repeat without the correction, standardising $45$ itself.

$$
z = \frac{45 - 40}{4.8990} \approx 1.0206, \qquad \Phi(1.02) \approx 0.8461
$$

Step 7. Compare with the exact binomial value, which is approximately $0.8689$.

Step 8. Interpret. The corrected answer lies within about $0.0003$ of the exact value, while the uncorrected answer is too small by about $0.023$. The correction is not a cosmetic refinement; it changes the second decimal place and would cost a mark in an examination that requires four decimal places.

### 4.9 Problem: an exponential waiting time

The time between arrivals at a service desk is exponentially distributed with rate $\lambda = 0.5$ per minute. Find the chance that the wait exceeds two minutes, the chance that it is below one minute, and the mean and standard deviation of the wait.

### 4.10 Solution: use the survival function directly

Step 1. State the model and the survival function.

$$
P(X > x) = e^{-\lambda x} = e^{-0.5x}, \qquad x \ge 0
$$

Step 2. Evaluate at $x = 2$.

$$
P(X > 2) = e^{-1} \approx 0.3679
$$

Step 3. Convert to a left-hand probability for the second part.

$$
P(X < 1) = 1 - e^{-0.5} \approx 1 - 0.6065 = 0.3935
$$

Step 4. Compute the mean.

$$
E(X) = \frac{1}{\lambda} = \frac{1}{0.5} = 2 \text{ minutes}
$$

Step 5. Compute the standard deviation.

$$
\sigma = \frac{1}{\lambda} = 2 \text{ minutes}
$$

Step 6. Interpret. The mean wait is two minutes and the standard deviation is also two minutes, so the distribution is strongly skewed: waits much longer than four minutes still occur with probability about $0.135$, even though four minutes is two standard deviations above the mean. This is a case where the empirical rule must not be applied, because the distribution is not normal.

### 4.11 Problem: deriving a distribution function from a density

A continuous random variable has density $f(x) = kx$ for $0 < x < 2$ and zero elsewhere. Find $k$, the distribution function, $P(1 < X < 1.5)$, and the mean and variance.

### 4.12 Solution: normalise, integrate, then use the moments

Step 1. Impose the normalisation condition.

$$
\int_{0}^{2} kx\,dx = k\left[\frac{x^{2}}{2}\right]_{0}^{2} = 2k = 1
$$

Step 2. Solve.

$$
k = \frac{1}{2}
$$

Step 3. Integrate the density to obtain the distribution function on the support.

$$
F(x) = \int_{0}^{x}\frac{t}{2}\,dt = \frac{x^{2}}{4}, \qquad 0 \le x \le 2
$$

Step 4. Apply the interval identity.

$$
P(1 < X < 1.5) = F(1.5) - F(1) = \frac{2.25}{4} - \frac{1}{4} = \frac{1.25}{4} = 0.3125
$$

Step 5. Compute the mean.

$$
E(X) = \int_{0}^{2} x\cdot\frac{x}{2}\,dx = \left[\frac{x^{3}}{6}\right]_{0}^{2} = \frac{8}{6} = \frac{4}{3}
$$

Step 6. Compute the second moment and the variance.

$$
E\left(X^{2}\right) = \int_{0}^{2} x^{2}\cdot\frac{x}{2}\,dx = \left[\frac{x^{4}}{8}\right]_{0}^{2} = 2
$$

$$
\text{Var}(X) = 2 - \left(\frac{4}{3}\right)^{2} = 2 - \frac{16}{9} = \frac{2}{9}
$$

Step 7. Interpret. The density rises linearly from zero at the left end, so the distribution is concentrated towards the right of the interval; the mean of $1.333$ lies above the midpoint of $1$, which is consistent with that shape. The standard deviation is $\frac{\sqrt{2}}{3} \approx 0.471$, small because the support is only two units wide.

### 4.13 Problem: the Poisson approximation in a quality context

A production run contains $1000$ items, each independently defective with probability $0.003$. Find the chance that the run contains at most one defective, using the Poisson approximation, and state whether the approximation is justified.

### 4.14 Solution: compute the rate and sum the small values

Step 1. Compute the expected number of defectives.

$$
\lambda = np = 1000 \times 0.003 = 3
$$

Step 2. Evaluate the probabilities at zero and one.

$$
P(X = 0) = e^{-3} \approx 0.0498, \qquad P(X = 1) = 3e^{-3} \approx 0.1494
$$

Step 3. Add.

$$
P(X \le 1) \approx 0.0498 + 0.1494 = 0.1992
$$

Step 4. Check the conditions of Theorem 11: $n = 1000$ is large, $p = 0.003$ is small, and $\lambda = 3$ is moderate. All three hold, so the approximation is justified.

Step 5. Compare with the exact binomial value, which is $\left(0.997\right)^{1000} + 1000\left(0.003\right)\left(0.997\right)^{999} \approx 0.0496 + 0.1491 = 0.1987$. The difference is in the fourth decimal place.

Step 6. Interpret. About one run in five contains at most one defective. The Poisson calculation is far quicker than the binomial and, under these conditions, equally accurate.

## 5. Mathematical Extensions, Limits, and Common Errors

### 5.1 Uniqueness, generating functions and why the three families are special

The moment generating function determines a distribution uniquely whenever it exists in a neighbourhood of the origin. That single fact explains why the additivity results of Section 2.5 hold and why the normal approximation can be proved at all: identifying a generating function identifies the distribution. The binomial generating function is $\left(1 - p + pe^{t}\right)^{n}$, which is the $n$-th power of the Bernoulli generating function $1 - p + pe^{t}$. That algebraic coincidence is the analytic statement of the fact that a binomial variable is a sum of independent Bernoullis, and it is why the binomial exponents add when two binomials with the same $p$ are combined.

The Poisson generating function $\exp\left(\lambda\left(e^{t} - 1\right)\right)$ is the limit of the binomial generating function under the substitution $p = \frac{\lambda}{n}$, since

$$
\lim_{n \to \infty}\left(1 + \frac{\lambda\left(e^{t} - 1\right)}{n}\right)^{n} = \exp\left(\lambda\left(e^{t} - 1\right)\right) .
$$

The normal generating function $\exp\left(\mu t + \frac{1}{2}\sigma^{2}t^{2}\right)$ multiplies in a way that adds means and variances, which is the analytic form of Theorem 7 extended to sums of independent normals.

### 5.2 The central limit theorem and the standing of the normal model

The normal approximation to the binomial is a special case of the central limit theorem, which states that the standardised sum of $n$ independent, identically distributed random variables with finite variance converges to the standard normal. The binomial is a sum of $n$ independent Bernoullis, so the theorem applies with mean $np$ and variance $np\left(1 - p\right)$.

The practical consequence goes well beyond the binomial. Sample means of large samples are approximately normal whatever the shape of the underlying population, which is why the normal curve appears in every later topic on estimation and testing. The qualification is that the approximation is asymptotic: it improves as $n$ grows, and it is unreliable when $n$ is small or when the underlying distribution is extremely skewed, such as an exponential with a large mean relative to the sample size.

### 5.3 Where each approximation fails

The normal approximation to the binomial fails when $np$ or $n\left(1 - p\right)$ is small. With $n = 10$ and $p = 0.05$ the expected number of successes is $0.5$, and a symmetric bell cannot describe a distribution concentrated at zero. In that regime the Poisson approximation with $\lambda = 0.5$ is far better. The Poisson approximation in turn fails when $p$ is not small, because the limit requires the failure probability to stay close to one; with $n = 20$ and $p = 0.4$ the Poisson is a poor fit while the binomial is exact and the normal is adequate.

The continuity correction is not optional in a careful answer. It accounts for the fact that a discrete bar of width one is being replaced by a continuous strip, and its neglect introduces a systematic bias towards whatever region the boundary faces. With a two-sided interval both ends need the half-unit shift, and applying it to only one end is a frequent and costly slip.

### 5.4 Errors that recur in examinations

The first recurrent error is confusing the parameters. For the binomial the two parameters are $n$ and $p$; for the Poisson there is one, $\lambda$; for the normal there are two, $\mu$ and $\sigma$. Writing a Poisson rate where a binomial $p$ belongs, or a variance where a standard deviation belongs, invalidates every subsequent step. The normal parameter is conventionally quoted as $N\left(\mu, \sigma^{2}\right)$ with the variance second, so a question that says $N\left(50, 9\right)$ has standard deviation $3$, not $9$.

The second error is treating a density as a probability, or integrating a mass function. Mass functions are summed and densities are integrated; mixing the two produces meaningless numbers.

The third error is forgetting that the Poisson rate must match the interval. A rate of two per hour applied to a question about thirty minutes must first be halved to one. The same discipline applies to lengths and areas.

The fourth error is mishandling the tails. A question that asks for "more than" needs one minus a cumulative value, and a question that asks for "between" needs a difference. Writing the region as an inequality before consulting the table removes the difficulty.

The fifth error is ignoring the conditions of the model. A binomial with a changing success probability, a Poisson with events that arrive in bursts, and a normal applied to strongly skewed data all produce answers that are arithmetically clean and statistically wrong. The conditions are part of the answer, not a preamble to it.

The sixth error is misapplying the empirical rule outside the normal family. The rule is a statement about the normal curve, and applying it to an exponential or a heavily skewed distribution gives badly misleading percentages.

### 5.5 Summary of the results to retain

| Result | Statement |
|---|---|
| Bernoulli | mean $p$, variance $p\left(1 - p\right)$ |
| Binomial | $P(X = x) = \binom{n}{x}p^{x}\left(1 - p\right)^{n - x}$, mean $np$, variance $np\left(1 - p\right)$ |
| Poisson | $P(X = x) = \frac{e^{-\lambda}\lambda^{x}}{x!}$, mean $\lambda$, variance $\lambda$ |
| Uniform | mean $\frac{a + b}{2}$, variance $\frac{\left(b - a\right)^{2}}{12}$ |
| Exponential | mean $\frac{1}{\lambda}$, variance $\frac{1}{\lambda^{2}}$ |
| Normal | density with total area one, standardised by $z = \frac{x - \mu}{\sigma}$ |
| Standardisation | $Z \sim N(0,1)$ whenever $X \sim N\left(\mu, \sigma^{2}\right)$ |
| Approximation | binomial to normal when $np$ and $n\left(1 - p\right)$ exceed five |
| Continuity correction | shift every finite boundary half a unit outwards |
| Additivity | Poisson rates add; normal means and variances add |

These ten lines, taken with the derivations of Section 3, constitute a complete working knowledge of the topic. Everything else is an application of one of them.