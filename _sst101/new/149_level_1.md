## 1. Foundational Concepts, Definitions, and Axioms

### 1.1 A cook tasting one spoonful of soup

Imagine a cook who has stirred a very large pot of soup and wants to know how salty the whole pot is. Tasting the whole pot is impossible, so the cook lifts one spoonful and tastes it. That spoonful is a tiny part of the pot, yet it supports a usable opinion about the whole pot. Two conditions make the opinion usable. First, the soup must be stirred, so that the spoonful is genuinely representative of everything in the pot. Second, the cook must accept that one spoonful is not a perfect instrument, so the opinion is offered with a little caution: "nicely salted, perhaps a shade strong".

Statistics works in exactly this way. A population is the whole pot; a sample is the spoonful; the sample average is the taste; and the caution in the cook's voice is the confidence level. Nothing in the subject goes beyond that picture. What the mathematics adds is precision about three things: how a good spoonful is drawn, how much a spoonful can be trusted to resemble the pot, and how to say the caution honestly with numbers attached.

### 1.2 Population, sample, parameter and statistic

Four words carry the whole framework, and they are easy to mix up.

A population is the complete collection of units about which a statement is wanted. It may be people, packets, seeds, machines or transactions. Its size is usually written as a capital letter $N$.

A sample is the part of the population that is actually observed. Its size is written as a lower-case letter $n$, and $n$ is always smaller than $N$, often very much smaller.

A parameter is a numerical summary of the whole population. The population mean is written $\mu$, the Greek letter mu, and pronounced "mew". The population standard deviation is written $\sigma$, the Greek letter sigma. A parameter is a fixed number, and in real work it is unknown; that is precisely why estimation exists.

A statistic is a numerical summary computed from the sample alone. The sample mean is written $\bar{x}$, read "x bar", and the sample standard deviation is written $s$. A statistic is known as soon as the data arrive, but it changes from sample to sample, because a different spoonful gives a different taste.

The single sentence that organises the topic is this: a statistic is used to estimate a parameter, and the gap between them is called sampling error. Sampling error is not a mistake. It is the unavoidable difference caused by looking at part of the population instead of all of it.

### 1.3 The point estimate

A point estimate is one single number offered as the best guess for an unknown parameter. The most familiar example is the sample mean used as the estimate of the population mean. If fifteen packets are weighed and their average mass is $252$ grams, then $252$ grams is the point estimate of the average mass of all packets produced that day.

Several parameters have standard point estimates, and it is worth knowing them by name because they appear in every later calculation.

> **Definition (Point estimate).** A point estimate is the value of a statistic computed from a sample and used as a single best guess for an unknown population parameter.

The sample mean is computed by adding the observations and dividing by how many there are. For observations $x_1, x_2, \dots, x_n$, where the subscript identifies which observation is meant and $n$ is the sample size,

$$
\bar{x} = \frac{1}{n}\sum_{i=1}^{n} x_i .
$$

In words: the sum symbol adds the observations, and dividing by $n$ turns a total into an average. The same number can be written with the total on top,

$$
\bar{x} = \frac{x_1 + x_2 + \cdots + x_n}{n} ,
$$

which is the form most people use when the data set is small enough to add by hand.

A point estimate has one great virtue and one great weakness. The virtue is that it is short and usable: it is the number a decision-maker asks for. The weakness is that it carries no statement about its own accuracy. "The average mass is 252 grams" looks equally confident whether it came from five packets or from five hundred, and that is misleading. A point estimate is therefore almost always followed by an interval estimate.

### 1.4 The interval estimate and the margin of error

An interval estimate replaces the single number with a range of plausible values. Instead of saying the mean is exactly $252$ grams, we say the mean lies between $248$ grams and $256$ grams. The range is built by taking the point estimate and stepping down by a certain amount and up by the same amount. That amount is the margin of error.

> **Definition (Interval estimate).** An interval estimate is a range of values, with a lower limit and an upper limit, constructed from sample data so that the unknown parameter is expected to lie inside it.

> **Definition (Margin of error).** The margin of error is the distance from the point estimate to either end of the interval. The interval is the point estimate minus the margin of error, up to the point estimate plus the margin of error.

The structure is therefore always the same shape:

$$
\text{interval} = \text{point estimate} \pm \text{margin of error} .
$$

The symbol $\pm$ is read "plus or minus", and it is a shorthand for two calculations: one that subtracts and one that adds. Written out in full, with $L$ naming the lower limit and $U$ naming the upper limit,

$$
L = \bar{x} - \text{margin}, \qquad U = \bar{x} + \text{margin} .
$$

The margin of error is not chosen freely. It is built from two ingredients: a multiplier that reflects how confident we wish to be, and the standard error, which measures how much the sample statistic typically moves from sample to sample. The next two sections explain each ingredient.

### 1.5 The confidence level

The confidence level is the reliability attached to the procedure that builds the interval. It is usually written as a percentage, and the great majority of published intervals use $95\%$. A confidence level of $95\%$ means that if the whole sampling exercise were repeated many times, with a new sample each time and a new interval built each time, then about $95$ intervals in every $100$ would contain the true parameter.

> **Definition (Confidence level).** The confidence level is the long-run success rate of the interval-building procedure: the proportion of repeated samples whose intervals would capture the true parameter.

Two consequences follow immediately, and beginners miss both.

The first consequence is that the confidence level describes the method, not the particular numbers in front of you. Once an interval has been computed, it either contains the parameter or it does not; the parameter is a fixed number and the interval is a fixed pair of numbers. There is no probability left to attach to that single pair. The $95\%$ belongs to the factory that produced the interval, not to the interval itself.

The second consequence is that a higher confidence level demands a wider interval. To be more certain of catching the parameter, the net must be thrown wider. The remaining amount, $1 - 0.95 = 0.05$, is the failure rate of the method, and it is split between the two ends of the interval in the two-sided case, giving $0.025$ at each end.

### 1.6 Why a sample statistic moves

Suppose the true average mass of all packets is $252$ grams. Take a sample of sixteen packets and average them; you might obtain $251.4$. Take another sample of sixteen and you might obtain $253.1$. Neither number is wrong. Each is a valid average of a different set of packets, and the fluctuation between them is sampling variability.

The fluctuation has a definite size, and that size is what makes an interval possible. Three facts about it can be stated in plain words before any algebra appears.

The first fact is that fluctuation is centred on the truth. Samples are as likely to land above the population mean as below it, so the average of many sample means equals the population mean.

The second fact is that fluctuation shrinks as the sample grows. Averages of large samples are more stable than averages of small samples, and they shrink in a very specific way: quadrupling the sample size halves the typical fluctuation.

The third fact is that fluctuation is smaller when the population itself is uniform. A population of packets that are nearly all the same weight yields very stable sample averages; a population with wildly varying weights yields unstable ones.

These three facts together are the reason a formula for the margin of error can be written down at all.

### 1.7 The standard error in plain words

The standard deviation of a single observation, written $\sigma$, measures how far one unit typically sits from the population mean. The standard error of the mean measures something different: how far a sample average typically sits from the population mean. It is always smaller than $\sigma$, and it is written

$$
\text{SE}(\bar{x}) = \frac{\sigma}{\sqrt{n}} .
$$

Read it aloud as "sigma divided by the square root of n". The numerator is the wobble of one unit; the denominator is the square root of how many units were averaged. The square root is what makes large samples pay off slowly: to halve the standard error you must quadruple the sample, and to cut it to one tenth you must multiply the sample by one hundred.

When the population standard deviation is unknown, and in practice it usually is, the sample standard deviation $s$ is substituted and the result is called the estimated standard error,

$$
\widehat{\text{SE}}(\bar{x}) = \frac{s}{\sqrt{n}} .
$$

The little hat over the letters means "estimated from the data".

### 1.8 What makes an estimator good

Any formula computed from a sample can be proposed as an estimator. To choose sensibly among proposals, four properties are used. They are stated here in ordinary language; precise statements belong to the next section.

An estimator is unbiased when, averaged over all possible samples, it lands exactly on the parameter. It may overshoot on one sample and undershoot on another, but the errors cancel in the long run. The sample mean is unbiased for the population mean.

An estimator is efficient when it has the smallest possible variance among the unbiased candidates. Two unbiased estimators can differ greatly in how much they jump about, and the one that jumps about less is preferred, because it is more likely to land close to the truth on the single sample actually taken.

An estimator is consistent when it converges on the parameter as the sample grows. Consistency is a statement about large samples: it says that with enough data the estimator becomes arbitrarily accurate. An estimator can be unbiased without being consistent, and the sample mean is both.

An estimator is sufficient when it uses all the information about the parameter that the sample contains, so that no further processing of the data can add anything. Sufficiency is the strongest of the four properties, and it explains why the sample mean and the sample variance, and nothing more complicated, are the natural summaries of a normal sample.

### 1.9 The bell curve and why it appears

The normal distribution is the symmetric bell-shaped curve. Its centre is the mean, and its width is controlled by the standard deviation. About $68\%$ of its area lies within one standard deviation of the centre, about $95\%$ within two, and about $99.7\%$ within three.

The remarkable fact is that sample averages are approximately normally distributed even when the population is not normal. This is the central limit theorem. It says that if you take many samples of size $n$ from almost any population, the histogram of the sample averages looks like a bell curve centred on the population mean, with spread $\sigma/\sqrt{n}$.

The theorem is what licenses the whole method. Because the sample average is approximately normal, the distance between the sample average and the population mean can be measured in standard errors and converted into a probability. A distance of $1.96$ standard errors, in either direction, is exceeded only $5\%$ of the time. That single number, $1.96$, is the bridge between the theory and the arithmetic of an interval.

### 1.10 The two great cases

Almost every examination question on this topic is one of two kinds.

The first kind asks about a mean. A sample of measurements is summarised by its average, and an interval for the population average is wanted. The ingredients are the sample mean, the standard deviation, the sample size and a multiplier taken from the normal curve or from the closely related t curve.

The second kind asks about a proportion. A sample of units is classified as success or failure, and an interval for the population proportion is wanted. The ingredients are the sample proportion, written $\hat{p}$ and read "p hat", the sample size, and the same kind of multiplier. The standard error of a proportion has its own formula because the variability of a yes-or-no variable is fixed once its mean is known.

Both cases reduce to the same three-step recipe: compute the point estimate, compute its standard error, multiply the standard error by the multiplier to obtain the margin of error, then state the interval. The differences between the cases lie entirely in the formulas for the point estimate and the standard error.

### 1.11 The notation collected

The symbols used throughout are gathered in one place so that no later formula is read cold.

| Symbol | Name | Meaning in words |
| --- | --- | --- |
| $N$ | population size | how many units exist in the whole population |
| $n$ | sample size | how many units were actually observed |
| $\mu$ | population mean | the unknown average of the whole population |
| $\sigma$ | population standard deviation | the unknown spread of single units |
| $\bar{x}$ | sample mean | the observed average of the sample |
| $s$ | sample standard deviation | the observed spread within the sample |
| $p$ | population proportion | the unknown fraction of successes in the population |
| $\hat{p}$ | sample proportion | the observed fraction of successes in the sample |
| $z$ | normal multiplier | the number of standard errors required for a stated confidence level |
| $t$ | t multiplier | the normal multiplier corrected for an estimated spread |
| $\alpha$ | error rate | one minus the confidence level, written as a proportion |
| $E$ | margin of error | the half-width of the interval |

Two conventions in the table deserve a note. The error rate $\alpha$ is written as a proportion, so a $95\%$ confidence level corresponds to $\alpha = 0.05$. And the margin of error $E$ is a half-width, so the full width of the interval is $2E$.

## 2. Theorems, Lemmas, and Analytical Properties

### 2.1 The sample mean is unbiased

> **Theorem (Unbiasedness of the sample mean).** If a sample of size $n$ is drawn from a population with mean $\mu$, then the expected value of the sample mean equals the population mean, that is $\text{E}(\bar{x}) = \mu$.

The content of the theorem is that the sample mean does not systematically overstate or understate the truth. Individual samples wander, but the wanderings are symmetric about $\mu$ and average out. A proof is given in the next section; the key step is that expectation is linear, so the expectation of a sum equals the sum of the expectations.

The theorem is why the sample mean is the default point estimate. Any estimator that was biased would be suspect, because repeating the study would not converge on the truth but on something slightly to one side of it.

### 2.2 The standard error of the mean

> **Theorem (Variance of the sample mean).** For independent observations each with variance $\sigma^{2}$, the variance of the sample mean is

$$
\text{Var}(\bar{x}) = \frac{\sigma^{2}}{n} ,
$$

and therefore the standard deviation of the sample mean is $\sigma/\sqrt{n}$.

This is the most useful formula in the whole topic. It converts the spread of single observations into the spread of an average, and it does so with a square root. The two properties it encodes are that averaging reduces variability and that the reduction is subject to diminishing returns.

For sampling from a finite population of size $N$ without replacement, the exact result carries a correction factor:

$$
\text{Var}(\bar{x}) = \frac{\sigma^{2}}{n}\left(\frac{N-n}{N-1}\right) .
$$

The factor in brackets is the finite population correction. It lies between zero and one, so it always reduces the variance, and it approaches one when the sample is a small fraction of the population, which is why it is usually ignored in that case.

### 2.3 The sample variance with the divisor n minus one is unbiased

> **Theorem (Unbiasedness of the sample variance).** For a sample of size $n$ from a population with variance $\sigma^{2}$, the estimator

$$
s^{2} = \frac{1}{n-1}\sum_{i=1}^{n}\left(x_i - \bar{x}\right)^{2}
$$

satisfies $\text{E}(s^{2}) = \sigma^{2}$.

The divisor $n-1$ is the striking feature. Dividing by $n$ would give the average squared deviation within the sample, which is a natural descriptive quantity, yet it systematically understates the population variance. The reason is that the deviations are measured from the sample mean rather than from the population mean, and the sample mean is by construction the point closest to the data, so the squared deviations from it are smaller than the squared deviations from $\mu$.

The loss of one degree of freedom is the price of having to estimate the centre. Once the sample mean is computed, only $n-1$ of the deviations are free, because the last one is fixed by the requirement that they sum to zero.

### 2.4 The central limit theorem

> **Theorem (Central limit theorem).** Let $x_1, \dots, x_n$ be independent observations from a population with mean $\mu$ and finite variance $\sigma^{2}$. Then, as $n$ grows,

$$
\frac{\bar{x} - \mu}{\sigma/\sqrt{n}} \to Z
$$

in distribution, where $Z$ is a standard normal variable with mean zero and variance one.

The theorem is the reason normal-based intervals work for data that are not themselves normal. Nothing is assumed about the shape of the population except that it has a finite variance. Skewed populations, bimodal populations and populations with heavy tails all produce approximately normal sample means once $n$ is moderately large.

A working rule of thumb is that $n$ of about thirty is enough for mildly skewed data, while strongly skewed data may need more. The approximation degrades as the population becomes more skewed and improves as $n$ grows.

### 2.5 The standard error of a proportion

> **Theorem (Standard error of a sample proportion).** If $X$ counts successes in $n$ independent trials each with success probability $p$, and $\hat{p} = X/n$, then

$$
\text{E}(\hat{p}) = p, \qquad \text{Var}(\hat{p}) = \frac{p(1-p)}{n} .
$$

The variance formula follows from the fact that a single trial has variance $p(1-p)$ and that averaging $n$ independent trials divides the variance by $n$, exactly as for the mean. A proportion is nothing but the mean of a variable that takes the value one for a success and zero for a failure, so the same machinery applies.

The quantity $p(1-p)$ has a maximum of $0.25$ at $p = 0.5$ and shrinks towards zero as $p$ approaches either end of its range. This is why a proportion near $0$ or near $1$ is estimated more precisely than a proportion near one half, and why the safe planning value $0.5$ is used when nothing is known about $p$ in advance.

### 2.6 The interval for a mean with known spread

> **Theorem (Known-variance interval).** If the population standard deviation $\sigma$ is known and the sample mean is approximately normal, then a confidence interval with confidence level $1 - \alpha$ for $\mu$ is

$$
\bar{x} \pm z_{\alpha/2}\,\frac{\sigma}{\sqrt{n}} ,
$$

where $z_{\alpha/2}$ is the value of the standard normal variable exceeded with probability $\alpha/2$ in each tail.

For the three most used confidence levels the multipliers are $1.645$, $1.96$ and $2.576$ for $90\%$, $95\%$ and $99\%$ respectively. The subscript notation records how the number was obtained: for $95\%$, $\alpha = 0.05$ and $\alpha/2 = 0.025$, so the multiplier is the point beyond which a standard normal variable falls with probability $0.025$.

The formula presumes that the sample mean is normally distributed. Strictly this requires either a normal population or a large sample, the latter supplied by the central limit theorem.

### 2.7 The t multiplier when the spread is unknown

> **Theorem (Unknown-variance interval).** If the population is normal but $\sigma$ is unknown and replaced by the sample standard deviation $s$, then

$$
\frac{\bar{x} - \mu}{s/\sqrt{n}}
$$

has a t distribution with $n-1$ degrees of freedom, and the confidence interval is

$$
\bar{x} \pm t_{\alpha/2,\,n-1}\,\frac{s}{\sqrt{n}} .
$$

The t distribution is symmetric and bell shaped like the normal, but with heavier tails. Heavier tails mean larger multipliers, which mean wider intervals, which is honest: having to estimate the spread as well as the centre costs information, and the t distribution charges for it.

The charge is severe for small samples and negligible for large ones. With five degrees of freedom the $95\%$ multiplier is $2.571$ against the normal $1.96$; with thirty degrees of freedom it is $2.042$; with a hundred it is $1.984$. As the degrees of freedom grow the t curve converges to the normal curve.

### 2.8 The interval for a proportion

> **Theorem (Wald interval for a proportion).** For a sample proportion $\hat{p}$ from a large sample,

$$
\hat{p} \pm z_{\alpha/2}\sqrt{\frac{\hat{p}(1-\hat{p})}{n}}
$$

is an approximate confidence interval for $p$ with confidence level $1-\alpha$.

This is called the Wald interval, after Abraham Wald. It is the interval that follows from inverting the familiar normal approximation to the binomial, and it is the one most often required in examinations. It has a genuine defect: when $\hat{p}$ is close to zero or one, or when $n$ is small, the interval can extend below zero or above one, which is impossible for a proportion.

> **Theorem (Wilson interval for a proportion).** The score interval obtained by solving a quadratic in $p$ is

$$
\frac{\hat{p} + \frac{z^{2}}{2n} \pm z\sqrt{\frac{\hat{p}(1-\hat{p})}{n} + \frac{z^{2}}{4n^{2}}}}{1 + \frac{z^{2}}{n}} ,
$$

where $z = z_{\alpha/2}$.

The Wilson interval shifts the centre away from $\hat{p}$ towards one half and never leaves the interval from zero to one. For large samples the two intervals almost coincide; for small samples or extreme proportions they differ substantially, and the Wilson interval is the more trustworthy of the two.

### 2.9 Choosing the sample size

> **Theorem (Sample size for a target margin of error).** To obtain a margin of error no larger than $E$ at confidence level $1-\alpha$, the required sample size for a mean is

$$
n = \left(\frac{z_{\alpha/2}\,\sigma}{E}\right)^{2} ,
$$

and for a proportion, with a planning value $p^{*}$, it is

$$
n = \frac{z_{\alpha/2}^{2}\,p^{*}(1-p^{*})}{E^{2}} .
$$

Both formulas are obtained by setting the margin of error equal to $E$ and solving for $n$. Both must be rounded up, never down, because a sample smaller than the calculated value fails to deliver the promised precision. In practice the population standard deviation is replaced by a pilot estimate, and the planning proportion is taken as $0.5$ when no information is available, since that value maximises the required sample and therefore guarantees the target.

### 2.10 One-sided bounds

> **Theorem (One-sided confidence bounds).** A lower confidence bound with confidence level $1-\alpha$ for a mean is

$$
\bar{x} - z_{\alpha}\frac{\sigma}{\sqrt{n}} ,
$$

and an upper bound is $\bar{x} + z_{\alpha}\frac{\sigma}{\sqrt{n}}$, where $z_{\alpha}$ is the standard normal point exceeded with probability $\alpha$ in a single tail.

A one-sided bound answers a one-sided question: how small could the parameter plausibly be, or how large could it plausibly be. Because all of the error probability is placed in one tail, the multiplier is smaller than the two-sided one for the same confidence level. For $95\%$ confidence the one-sided multiplier is $1.645$ and the two-sided multiplier is $1.96$. A one-sided bound is therefore closer to the point estimate than the corresponding end of a two-sided interval, and it is wrong to mix the two conventions.

The corresponding bounds for a proportion use the same structure with the proportion standard error. When the spread is unknown, $t_{\alpha,\,n-1}$ replaces $z_{\alpha}$.

### 2.11 The finite population correction

> **Theorem (Corrected interval).** When sampling without replacement from a finite population of size $N$, the standard error of the sample mean is multiplied by $\sqrt{(N-n)/(N-1)}$, so the interval becomes

$$
\bar{x} \pm z_{\alpha/2}\,\frac{\sigma}{\sqrt{n}}\sqrt{\frac{N-n}{N-1}} .
$$

The correction matters when the sample is a substantial fraction of the population. A common rule is to apply it whenever $n/N$ exceeds about one twentieth. When $n = N$, so that the whole population is measured, the factor is zero and the interval collapses to a single point, which is correct: there is no sampling error left because there is no sampling.

An equivalent and simpler-looking version, adequate when $N$ is large, uses $\sqrt{1 - n/N}$ in place of the exact factor. The two agree closely for large $N$.

### 2.12 Intervals and tests are the same statement

> **Theorem (Duality of intervals and tests).** For a two-sided test of the hypothesis that a parameter equals a particular value, conducted at significance level $\alpha$, the set of values not rejected is exactly the confidence interval for that parameter with confidence level $1-\alpha$.

The duality runs in both directions and is extremely useful in examinations. If a hypothesised value lies inside the $95\%$ interval, a two-sided test at the $5\%$ level will not reject it. If it lies outside, the test rejects it. There is no need to compute a test statistic and an interval separately, because one implies the other.

The duality extends to one-sided tests and one-sided bounds, with the same pairing: a one-sided test at level $\alpha$ corresponds to a one-sided bound at confidence level $1-\alpha$.

### 2.13 The multipliers collected

The numbers that do most of the work in this topic are few, and they are worth memorising.

| Confidence level | Two-sided multiplier | One-sided multiplier | Used for |
| --- | --- | --- | --- |
| $90\%$ | $1.645$ | $1.282$ | quick intervals, screening |
| $95\%$ | $1.960$ | $1.645$ | the standard choice |
| $98\%$ | $2.326$ | $2.054$ | cautious reporting |
| $99\%$ | $2.576$ | $2.326$ | strong evidence required |

The t multipliers depend on the degrees of freedom, and a small selection is enough for most hand calculations.

| Degrees of freedom | $t$ for $95\%$ two-sided | $t$ for $99\%$ two-sided |
| --- | --- | --- |
| $5$ | $2.571$ | $4.032$ |
| $10$ | $2.228$ | $3.169$ |
| $15$ | $2.131$ | $2.947$ |
| $20$ | $2.086$ | $2.845$ |
| $30$ | $2.042$ | $2.750$ |
| $60$ | $2.000$ | $2.660$ |

Notice how the columns converge towards $1.96$ and $2.576$. With sixty degrees of freedom the difference from the normal multiplier is already small, and beyond about a hundred it is negligible.

### 2.14 Width depends on three things

> **Theorem (Width decomposition).** For a fixed confidence level, the width of a two-sided interval for a mean is

$$
W = 2\,z_{\alpha/2}\,\frac{\sigma}{\sqrt{n}} ,
$$

and for a proportion it is $W = 2\,z_{\alpha/2}\sqrt{\hat{p}(1-\hat{p})/n}$.

Three levers therefore control the width. Raising the confidence level raises $z$ and widens the interval. Raising the sample size lowers the width in proportion to the square root of $n$, so halving the width requires four times the data. Raising the variability $\sigma$ widens the interval, and for a proportion the variability term is largest when $\hat{p}$ is near one half.

The three levers are not equally available. The variability is a property of the population and cannot be changed by the investigator. The confidence level is a policy decision that trades precision against reliability. The sample size is the only lever that can be increased, and it is the one that costs money.

## 3. Formal Proofs, Derivations, and Methods

### 3.1 Why the sample mean is unbiased

The proof rests on one property of expectation: the expectation of a sum is the sum of the expectations, and the expectation of a constant multiple is the multiple of the expectation. Nothing else is needed.

Step 1. Write the sample mean as a weighted sum of the observations, using the fact that dividing by $n$ is the same as multiplying by $1/n$.

$$
\bar{x} = \frac{1}{n}\sum_{i=1}^{n} x_i
$$

Step 2. Take expectations of both sides and move the constant factor outside.

$$
\text{E}(\bar{x}) = \frac{1}{n}\sum_{i=1}^{n} \text{E}(x_i)
$$

Step 3. Each observation is drawn from the same population, so each has expectation $\mu$.

$$
\text{E}(\bar{x}) = \frac{1}{n}\sum_{i=1}^{n} \mu = \frac{1}{n}\left(n\mu\right) = \mu
$$

The conclusion is that the sample mean is unbiased at every sample size, including $n = 1$, where the single observation is trivially unbiased for the population mean. Unbiasedness is not a large-sample property.

### 3.2 Why the standard error is sigma over root n

Step 1. Begin again with the weighted-sum form of the sample mean.

$$
\bar{x} = \frac{1}{n}\sum_{i=1}^{n} x_i
$$

Step 2. Use the rule that the variance of a sum of independent terms is the sum of their variances, and that a constant factor is squared when it is pulled out of a variance.

$$
\text{Var}(\bar{x}) = \frac{1}{n^{2}}\sum_{i=1}^{n} \text{Var}(x_i)
$$

Step 3. Each observation has variance $\sigma^{2}$, so the sum contains $n$ copies of $\sigma^{2}$.

$$
\text{Var}(\bar{x}) = \frac{1}{n^{2}}\left(n\sigma^{2}\right) = \frac{\sigma^{2}}{n}
$$

Step 4. The standard error is the square root of the variance, and taking a square root of a quotient takes the roots separately.

$$
\text{SE}(\bar{x}) = \sqrt{\frac{\sigma^{2}}{n}} = \frac{\sigma}{\sqrt{n}}
$$

This is where the square root in the formula comes from, and it is also where the diminishing returns come from: the standard error falls as one over the square root of $n$, not as one over $n$.

### 3.3 Why the divisor n minus one appears

The short argument is that the deviations from the sample mean are systematically too small, and the shortfall is exactly a factor of $(n-1)/n$.

Step 1. Write the sum of squared deviations from the sample mean, and add and subtract the population mean inside the bracket.

$$
\sum_{i=1}^{n}\left(x_i - \bar{x}\right)^{2} = \sum_{i=1}^{n}\left[\left(x_i - \mu\right) - \left(\bar{x} - \mu\right)\right]^{2}
$$

Step 2. Expand the square. Three terms appear.

$$
\sum_{i=1}^{n}\left(x_i - \mu\right)^{2} - 2\left(\bar{x} - \mu\right)\sum_{i=1}^{n}\left(x_i - \mu\right) + n\left(\bar{x} - \mu\right)^{2}
$$

Step 3. Notice that the middle sum equals $n\left(\bar{x} - \mu\right)$, because the sum of deviations from $\mu$ is $n$ times the average deviation from $\mu$.

$$
\sum_{i=1}^{n}\left(x_i - \mu\right) = n\left(\bar{x} - \mu\right)
$$

Step 4. Substitute and combine the last two terms, which have opposite signs and equal size.

$$
\sum_{i=1}^{n}\left(x_i - \bar{x}\right)^{2} = \sum_{i=1}^{n}\left(x_i - \mu\right)^{2} - n\left(\bar{x} - \mu\right)^{2}
$$

Step 5. Take expectations. The first term has expectation $n\sigma^{2}$ and the second has expectation $n\left(\sigma^{2}/n\right) = \sigma^{2}$.

$$
\text{E}\left[\sum_{i=1}^{n}\left(x_i - \bar{x}\right)^{2}\right] = n\sigma^{2} - \sigma^{2} = \left(n-1\right)\sigma^{2}
$$

Step 6. Divide by $n-1$ to obtain an estimator whose expectation is $\sigma^{2}$.

$$
\text{E}\left[\frac{1}{n-1}\sum_{i=1}^{n}\left(x_i - \bar{x}\right)^{2}\right] = \sigma^{2}
$$

The factor $(n-1)$ is exactly the amount of information spent on locating the centre. Dividing by $n$ instead would leave the expectation at $(n-1)\sigma^{2}/n$, which is too small by the fraction $1/n$.

### 3.4 Deriving the interval for a mean

The derivation uses a pivot: a quantity that combines the data and the parameter in such a way that its distribution is known and free of the parameter. Inverting the pivot produces the interval.

Step 1. Standardise the sample mean. Under the central limit theorem the standardised quantity is approximately standard normal.

$$
Z = \frac{\bar{x} - \mu}{\sigma/\sqrt{n}}
$$

Step 2. Write the probability statement that defines the central $1-\alpha$ region of the standard normal curve.

$$
\text{P}\left(-z_{\alpha/2} \le Z \le z_{\alpha/2}\right) = 1 - \alpha
$$

Step 3. Replace $Z$ by its definition.

$$
\text{P}\left(-z_{\alpha/2} \le \frac{\bar{x} - \mu}{\sigma/\sqrt{n}} \le z_{\alpha/2}\right) = 1 - \alpha
$$

Step 4. Multiply the inequality through by the standard error, which is positive and so preserves the direction of the inequalities.

$$
\text{P}\left(-z_{\alpha/2}\frac{\sigma}{\sqrt{n}} \le \bar{x} - \mu \le z_{\alpha/2}\frac{\sigma}{\sqrt{n}}\right) = 1 - \alpha
$$

Step 5. Subtract $\bar{x}$ from all three parts, which reverses the inequalities.

$$
\text{P}\left(-\bar{x} - z_{\alpha/2}\frac{\sigma}{\sqrt{n}} \le -\mu \le -\bar{x} + z_{\alpha/2}\frac{\sigma}{\sqrt{n}}\right) = 1 - \alpha
$$

Step 6. Multiply by minus one and reverse the inequalities again to isolate $\mu$.

$$
\text{P}\left(\bar{x} - z_{\alpha/2}\frac{\sigma}{\sqrt{n}} \le \mu \le \bar{x} + z_{\alpha/2}\frac{\sigma}{\sqrt{n}}\right) = 1 - \alpha
$$

Step 7. Read off the two limits. The probability statement is about the random interval, and it says that the random interval covers the fixed parameter with probability $1-\alpha$. Substituting the observed values of $\bar{x}$ gives the realised interval.

$$
\left[\bar{x} - z_{\alpha/2}\frac{\sigma}{\sqrt{n}}, \;\; \bar{x} + z_{\alpha/2}\frac{\sigma}{\sqrt{n}}\right]
$$

The step where the inequalities are reversed is where most algebraic errors occur. Writing the answer before performing that step is the commonest source of a sign mistake.

### 3.5 Deriving the interval for a proportion

Step 1. Start from the standardised sample proportion, which is approximately standard normal for large $n$ by the central limit theorem applied to the underlying zeros and ones.

$$
Z = \frac{\hat{p} - p}{\sqrt{p(1-p)/n}}
$$

Step 2. Write the central probability statement as before.

$$
\text{P}\left(-z \le Z \le z\right) = 1 - \alpha
$$

Step 3. Substituting and rearranging exactly as in the mean case gives an interval whose endpoints still contain the unknown $p$ inside the standard error.

$$
\hat{p} \pm z\sqrt{\frac{p(1-p)}{n}}
$$

Step 4. Replace the unknown $p$ inside the standard error by its estimate $\hat{p}$. This is the practical step that turns an exact but unusable expression into the Wald interval. It is justified because the standard error is a slowly varying function of $p$ when $n$ is large.

$$
\hat{p} \pm z\sqrt{\frac{\hat{p}(1-\hat{p})}{n}}
$$

Step 5. Note the consequence of the substitution. The interval is now centred exactly on $\hat{p}$, which is convenient, but the approximation degrades when $\hat{p}$ is extreme, because then the standard error is badly estimated and the normal approximation to the binomial is itself poor.

### 3.6 Deriving the sample size formula

Step 1. Write the margin of error for a mean.

$$
E = z_{\alpha/2}\frac{\sigma}{\sqrt{n}}
$$

Step 2. Multiply both sides by the square root of $n$ and divide by $E$.

$$
\sqrt{n} = \frac{z_{\alpha/2}\,\sigma}{E}
$$

Step 3. Square both sides, which removes the root and gives the required size.

$$
n = \left(\frac{z_{\alpha/2}\,\sigma}{E}\right)^{2}
$$

Step 4. For a proportion, replace the standard error by its planning form using $p^{*}$.

$$
E = z_{\alpha/2}\sqrt{\frac{p^{*}(1-p^{*})}{n}}
$$

Step 5. Square and rearrange in the same way.

$$
n = \frac{z_{\alpha/2}^{2}\,p^{*}(1-p^{*})}{E^{2}}
$$

Step 6. Round upwards. A fractional sample size is not attainable, and rounding down would leave the margin of error slightly above target.

### 3.7 The five-step recipe

Every interval question, at any level, follows the same five steps. Writing them out in order prevents most mistakes.

Step 1. Identify the parameter and the level of confidence, and write down $\alpha$ and the multiplier.

Step 2. Compute the point estimate from the data, using the mean formula for a mean question and the ratio of successes to trials for a proportion question.

Step 3. Compute the standard error, choosing the version that matches the information available: known $\sigma$ uses $z$, unknown $\sigma$ uses $s$ and $t$, a proportion uses $\hat{p}$.

Step 4. Multiply the standard error by the multiplier to obtain the margin of error.

Step 5. State the interval as estimate minus margin to estimate plus margin, and write one sentence of interpretation that mentions the confidence level and the population, not the sample.

The fifth step is where marks are lost. An answer that ends with a pair of numbers and no interpretation is incomplete.

### 3.8 Reading a bound aloud

A confidence interval must be read with the population named, the parameter named, the units stated and the confidence level attached. The template that satisfies all four is: "We are $95\%$ confident that the mean mass of all packets produced today lies between $248.1$ grams and $255.9$ grams."

Three things are wrong with the sentence "there is a $95\%$ probability that the mean is between $248.1$ and $255.9$". It omits the word confident, which is the word that carries the frequency interpretation. It applies a probability to a fixed unknown constant. And it fails to name the population, so the reader cannot tell what the statement is about.

## 4. Representative Worked Examples and Solutions

### 4.1 Problem: an interval for a mean when the spread is known

A machine fills packets of tea. The filling mass is known from long experience to have a standard deviation of $12$ grams. A sample of $36$ packets has a mean mass of $252$ grams. Construct a $95\%$ confidence interval for the population mean mass.

### 4.2 Solution: known spread, so the normal multiplier is used

Step 1. Record the ingredients and the multiplier. The sample mean is $\bar{x} = 252$, the population standard deviation is $\sigma = 12$, the sample size is $n = 36$, and the $95\%$ multiplier is $z = 1.96$.

Step 2. Compute the standard error, which is the population standard deviation divided by the square root of the sample size.

$$
\text{SE} = \frac{12}{\sqrt{36}} = \frac{12}{6} = 2
$$

Step 3. Compute the margin of error by multiplying the standard error by the multiplier.

$$
E = 1.96 \times 2 = 3.92
$$

Step 4. Form the lower limit by subtracting the margin from the mean.

$$
L = 252 - 3.92 = 248.08
$$

Step 5. Form the upper limit by adding the margin to the mean.

$$
U = 252 + 3.92 = 255.92
$$

Step 6. State the interval and interpret it. We are $95\%$ confident that the mean filling mass of all packets produced lies between $248.08$ grams and $255.92$ grams.

Step 7. Check the arithmetic for plausibility. The margin of about $4$ grams is two standard errors, which is what a $95\%$ interval should be, and the interval is symmetric about the sample mean, as it must be.

### 4.3 Problem: a small sample with an unknown spread

The marks of $16$ students in a test have a mean of $68.4$ and a standard deviation of $5.2$. Construct a $95\%$ confidence interval for the mean mark of all students who sat the test, assuming the marks are approximately normal.

### 4.4 Solution: unknown spread, so the t multiplier is used

Step 1. Record the ingredients. The sample mean is $\bar{x} = 68.4$, the sample standard deviation is $s = 5.2$, the sample size is $n = 16$, and the degrees of freedom are $n - 1 = 15$.

Step 2. Look up the t multiplier for $15$ degrees of freedom at the $95\%$ level, which is $2.131$.

Step 3. Compute the standard error, now using the sample standard deviation because the population value is unknown.

$$
\text{SE} = \frac{5.2}{\sqrt{16}} = \frac{5.2}{4} = 1.3
$$

Step 4. Compute the margin of error.

$$
E = 2.131 \times 1.3 = 2.7703
$$

Step 5. Form the two limits.

$$
L = 68.4 - 2.7703 = 65.63
$$

$$
U = 68.4 + 2.7703 = 71.17
$$

Step 6. Interpret. We are $95\%$ confident that the mean mark of the whole group lies between $65.63$ and $71.17$.

Step 7. Compare with what the normal multiplier would have given, to see the cost of not knowing the spread. Using $1.96$ instead of $2.131$ would give a margin of $2.548$ and an interval from $65.85$ to $70.95$, which is too narrow and therefore overconfident.

### 4.5 Problem: an interval for a proportion

In a random sample of $200$ students, $46$ own a bicycle. Construct a $95\%$ confidence interval for the proportion of all students who own a bicycle.

### 4.6 Solution: proportion case with the Wald form

Step 1. Compute the sample proportion, which is the number of successes divided by the sample size.

$$
\hat{p} = \frac{46}{200} = 0.23
$$

Step 2. Compute the estimated standard error using the proportion formula.

$$
\text{SE} = \sqrt{\frac{0.23 \times 0.77}{200}} = \sqrt{\frac{0.1771}{200}} = \sqrt{0.0008855} \approx 0.02976
$$

Step 3. Compute the margin of error with the $95\%$ multiplier.

$$
E = 1.96 \times 0.02976 \approx 0.05833
$$

Step 4. Form the two limits.

$$
L = 0.23 - 0.05833 = 0.17167
$$

$$
U = 0.23 + 0.05833 = 0.28833
$$

Step 5. Convert to percentages, which read better for a proportion, and interpret. We are $95\%$ confident that the proportion of all students owning a bicycle lies between $17.2\%$ and $28.8\%$.

Step 6. Check that both limits lie inside the range from zero to one, which confirms that the normal approximation is behaving sensibly at this sample size and this proportion.

### 4.7 Problem: how large a sample is needed

A survey is planned to estimate the proportion of residents who support a new policy, with a margin of error no greater than $5$ percentage points at $95\%$ confidence. Nothing is known in advance about the level of support. How many residents should be sampled?

### 4.8 Solution: use the safe planning value of one half

Step 1. Identify the target margin of error as a proportion, which is $E = 0.05$.

Step 2. Choose the planning value. With no prior information, the safe choice is $p^{*} = 0.5$, because the product $p^{*}(1-p^{*})$ is largest there and the resulting sample size therefore protects the target for any true value.

Step 3. Substitute into the sample size formula.

$$
n = \frac{1.96^{2} \times 0.5 \times 0.5}{0.05^{2}}
$$

Step 4. Evaluate the numerator and the denominator separately.

$$
1.96^{2} = 3.8416, \qquad 0.05^{2} = 0.0025
$$

Step 5. Divide.

$$
n = \frac{0.9604}{0.0025} = 384.16
$$

Step 6. Round up to the next whole number, since a fraction of a person cannot be interviewed.

$$
n = 385
$$

Step 7. Interpret and cross-check. A sample of $385$ residents delivers the promised precision whatever the true level of support turns out to be. Had a pilot study suggested that support was near $0.24$, the required sample would have been about $281$, so the safe planning value costs roughly a hundred interviews in exchange for a guarantee.

### 4.9 Problem: a one-sided bound

Using the packet data of the first example, with $\bar{x} = 252$ grams, $\sigma = 12$ grams and $n = 36$, find a $95\%$ lower confidence bound for the mean filling mass.

### 4.10 Solution: place all the error in one tail

Step 1. Recognise that a lower bound is a one-sided statement, so the one-sided multiplier is required rather than the two-sided one.

Step 2. Record the one-sided $95\%$ multiplier, which is $1.645$.

Step 3. Compute the standard error exactly as before.

$$
\text{SE} = \frac{12}{6} = 2
$$

Step 4. Compute the allowance by multiplying the one-sided multiplier by the standard error.

$$
1.645 \times 2 = 3.29
$$

Step 5. Subtract the allowance from the sample mean, since only the lower end is wanted.

$$
L = 252 - 3.29 = 248.71
$$

Step 6. Interpret. We are $95\%$ confident that the true mean filling mass is at least $248.71$ grams.

Step 7. Compare with the two-sided interval. Its lower limit was $248.08$, which is further below the sample mean than $248.71$. The one-sided bound is tighter because it does not have to reserve any error probability for the upper tail. Using the two-sided multiplier for a one-sided question is a common error that makes the bound unnecessarily weak.

### 4.11 Problem: a sample that is a large fraction of the population

A college has $500$ students. A random sample of $100$ students is weighed, giving a mean mass of $62$ kilograms. The population standard deviation is known to be $20$ kilograms. Construct a $95\%$ confidence interval, applying the finite population correction.

### 4.12 Solution: correct the standard error before building the interval

Step 1. Record the ingredients. The sample mean is $\bar{x} = 62$, the population standard deviation is $\sigma = 20$, the sample size is $n = 100$, the population size is $N = 500$, and the multiplier is $1.96$.

Step 2. Compute the uncorrected standard error.

$$
\frac{\sigma}{\sqrt{n}} = \frac{20}{10} = 2
$$

Step 3. Compute the finite population correction factor.

$$
\sqrt{\frac{N-n}{N-1}} = \sqrt{\frac{500-100}{500-1}} = \sqrt{\frac{400}{499}} \approx \sqrt{0.8016} \approx 0.8953
$$

Step 4. Multiply the standard error by the correction factor.

$$
\text{SE} = 2 \times 0.8953 = 1.7906
$$

Step 5. Compute the margin of error.

$$
E = 1.96 \times 1.7906 \approx 3.51
$$

Step 6. Form the interval.

$$
L = 62 - 3.51 = 58.49, \qquad U = 62 + 3.51 = 65.51
$$

Step 7. Interpret and compare. We are $95\%$ confident that the mean mass of all $500$ students lies between $58.49$ and $65.51$ kilograms. Without the correction the interval would run from $58.08$ to $65.92$, which is about twelve per cent wider. One fifth of the population has been measured, so it is not reasonable to pretend that the sample is a negligible fraction of it.

## 5. Mathematical Extensions, Limits, and Common Errors

### 5.1 What the confidence level really means

The most important sentence in the topic is that confidence belongs to the procedure. To see why, imagine a factory that produces intervals rather than packets. The factory draws a sample, computes an interval and ships it. The factory is well calibrated: in the long run $95$ of every $100$ intervals it ships contain the true parameter. The factory's record is a property of the factory. A single shipped interval carries no probability at all, because both its ends are fixed numbers and the parameter is also a fixed number; the parameter is either inside or outside, and nobody knows which.

This is why the correct sentence is "we are $95\%$ confident" rather than "there is a $95\%$ chance". The word confident is a compressed report about the reliability of the method. The word chance would be a claim about a random variable, and there is no random variable left once the sample has been processed.

A second consequence is that the $95\%$ is not a guarantee about the interval in hand, and it is certainly not a statement that $95\%$ of the data lie inside the interval. Data-based intervals and parameter-based intervals are different objects. A $95\%$ interval for a mean computed from a sample of $36$ packets is a few grams wide, yet the packets themselves are spread over tens of grams. Confusing the two is the single most common conceptual error in the topic.

### 5.2 What changes the width

The width is controlled by three quantities, and the direction of each effect is worth committing to memory because examination questions ask for it directly.

Increasing the confidence level widens the interval, because a larger multiplier is required to cover more of the sampling distribution. Moving from $95\%$ to $99\%$ raises the multiplier from $1.96$ to $2.576$, which enlarges the margin by about a third.

Increasing the sample size narrows the interval, but only in proportion to the square root. Quadrupling the sample halves the margin. This is why precision is expensive: the last few percentage points of precision cost the most.

Increasing the variability widens the interval, since the standard error is proportional to the standard deviation. For a proportion, variability is greatest when the sample proportion is near one half, so an interval for a proportion near $50\%$ is wider than one for a proportion near $5\%$ at the same sample size.

A fourth lever exists but is less often discussed: reducing the confidence level narrows the interval at the cost of reliability. There is no free lunch anywhere in the list, and a claim of a very narrow interval with very high confidence should always prompt the question of how large the sample was.

### 5.3 Beginner mistakes

The following errors appear again and again in scripts and in practice.

Writing the interval as an inequality in the wrong direction, usually caused by failing to reverse the inequalities when subtracting the sample mean during the derivation. The lower limit must be below the point estimate and the upper limit above it; a quick check catches the slip.

Forgetting to take the square root of the sample size, and dividing by $n$ instead of by the square root of $n$. The resulting standard error is far too small and the interval absurdly narrow.

Using the normal multiplier when the sample is small and the population standard deviation is unknown. The t multiplier is required, and using $1.96$ instead of $2.131$ at fifteen degrees of freedom understates the margin by about eight per cent.

Using the two-sided multiplier for a one-sided bound, or the reverse. The two conventions are not interchangeable, and the one-sided multiplier for $95\%$ is $1.645$, not $1.96$.

Omitting the finite population correction when the sample is a large share of the population, which makes the interval wider than it needs to be and therefore understates the precision actually achieved.

Reporting an interval without units, without naming the population, or without the confidence level. All three omissions lose marks and, worse, make the statement uninterpretable.

Treating the point estimate as the answer. A point estimate alone conceals the sampling error, which is the whole reason for computing an interval.

### 5.4 Where the method stops working

The normal-based interval for a mean relies on the sample mean being approximately normal. With small samples from a strongly skewed population, the approximation fails and the interval can be seriously wrong. The t interval helps when the population is itself normal, but it does not rescue a small sample from a heavily skewed population.

The Wald interval for a proportion fails when the sample proportion is near zero or one, and it can produce limits outside the range from zero to one. The Wilson interval repairs this. A useful working rule is that the Wald interval is acceptable when both the number of successes and the number of failures exceed about ten, and the Wilson interval should be preferred otherwise.

The finite population correction assumes that the population size is known and that sampling is without replacement. If either assumption fails, the correction should not be applied.

Nothing in the method repairs a biased sample. A convenience sample of volunteers does not produce a $95\%$ interval with $95\%$ coverage, because the probability statement presupposes that every unit had a known chance of selection. The mathematics cannot detect the bias, and this is the most dangerous limitation of all, since the arithmetic will look perfectly respectable.

### 5.5 A short self-check before submitting an answer

Six questions catch nearly every error. Is the parameter a mean or a proportion? Is the population standard deviation known, or must the sample value be used? Is the sample small enough to require the t multiplier? Is the question two-sided or one-sided? Is the sample a large fraction of a finite population? And does the final sentence mention the population, the parameter, the units and the confidence level?

If all six can be answered confidently, the arithmetic is almost certainly sound and the interpretation almost certainly complete. The mathematics of this topic is short; the discipline of checking the six questions is what separates a full-mark answer from a half-mark one.
