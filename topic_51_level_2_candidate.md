## 1. Purpose and Statistical Context

### 1.1 Where minimum-variance estimation fits

Statistical estimation uses sample information to estimate an unknown population parameter. A parameter such as a population mean or variance is fixed but unknown; an estimator is a statistic calculated from a random sample. Different estimators can target the same parameter, and they may differ in bias and variability.

The method of minimum variance studies the best estimator within the class of unbiased estimators. It asks: among all estimators whose expected value equals the target parameter, which one has the smallest variance? This restriction matters. An estimator with a smaller variance is not automatically preferable if it is biased, and minimum variance among unbiased estimators is not the same objective as minimizing mean squared error over every possible estimator.

A minimum-variance unbiased estimator (MVUE) is defined relative to a specified parameter and model. A uniformly minimum-variance unbiased estimator (UMVUE) has minimum variance among unbiased estimators for every permitted value of the parameter. The course uses likelihoods, Fisher information, the Cramér–Rao inequality, and the equality condition in that inequality to identify cases where an unbiased estimator reaches the lower variance limit.

### 1.2 Learning goals

After this lesson, a learner should be able to:

- Define an MVUE and distinguish it from a UMVUE.
- Explain the role of unbiasedness in a minimum-variance comparison.
- Form the likelihood and score for a random sample.
- State the regularity conditions needed for the score and information calculations.
- Derive the Cramér–Rao lower bound using the score identity and the Cauchy–Schwarz (Schwartz) inequality.
- Recognize the equality condition that identifies an estimator attaining that bound.
- Calculate Fisher information and use it to assess an estimator's variance.
- Compare the variances of several unbiased estimators of the same parameter.

## 2. Definitions and Assumptions

### 2.1 Random sample, likelihood, and score

Let $X_1,\ldots,X_n$ be a random sample from a model with density or mass function $f(x;\theta)$, where $\theta$ is an unknown scalar parameter. The joint likelihood is

$$
L(\theta;\mathbf x)=\prod_{i=1}^{n} f(x_i;\theta),
$$

and the log-likelihood is $\ell(\theta;\mathbf x)=\log L(\theta;\mathbf x)$. The score is the derivative of the log-likelihood with respect to the parameter:

$$
U_\theta(\mathbf X)=\frac{\partial}{\partial\theta}\ell(\theta;\mathbf X).
$$

The score describes how the log-likelihood changes locally as $\theta$ changes. Under the regularity conditions used in this lesson, $E_\theta[U_\theta]=0$ and its variance is the sample Fisher information

$$
I_n(\theta)=E_\theta[U_\theta^2]
=-E_\theta\!\left[\frac{\partial^2}{\partial\theta^2}\ell(\theta;\mathbf X)\right].
$$

The equality of these two information expressions depends on the regularity conditions; it should not be used automatically when those conditions fail.

### 2.2 MVUE and UMVUE

An estimator $T$ is unbiased for $\theta$ if

$$
E_\theta[T]=\theta
$$

for every allowed value of $\theta$. It is an MVUE when it is unbiased and has variance no greater than any other unbiased estimator of the same target under the model:

$$
\operatorname{Var}_\theta(T)\leq \operatorname{Var}_\theta(T')
$$

for every competing unbiased estimator $T'$. A UMVUE has this minimum-variance property uniformly over the parameter space. The target must be held fixed in the comparison; one cannot compare variances of estimators of different quantities and call the smallest one best.

Bias and variance are separate properties. An estimator may have small variance but be systematically centered away from the target. An MVUE must first satisfy unbiasedness, then minimize variance within the unbiased class.

### 2.3 Conditions used for the score identities

The lecture states regularity requirements so that differentiation and integration can be interchanged. In practical use, check that:

- The parameter is a real scalar in the permitted parameter range.
- The density or mass function and its parameter derivative exist on the relevant support.
- The support does not introduce parameter-dependent boundary terms in the calculation.
- Differentiation under the integral or sum is justified.
- The score and Fisher information are well defined and finite.

Under these conditions, differentiating $\int L(\theta;\mathbf x)\,d\mathbf x=1$ gives $E_\theta[U_\theta]=0$. If $T$ is unbiased for $g(\theta)$, differentiating $E_\theta[T]=g(\theta)$ gives the score identity

$$
E_\theta\!\left[(T-g(\theta))U_\theta\right]=g'(\theta).
$$

This identity is the link between the estimator's error and the score that makes the lower-bound proof work.

## 3. Methods and Interpretation

### 3.1 Deriving the Cramér–Rao lower bound

Suppose $T$ is unbiased for $g(\theta)$ and the score identities above are valid. Since $E_\theta[U_\theta]=0$ and $E_\theta[T]=g(\theta)$, the score identity can be written as a covariance:

$$
\operatorname{Cov}_\theta(T,U_\theta)=g'(\theta).
$$

The Cauchy–Schwarz inequality for covariance states

$$
\operatorname{Cov}_\theta(T,U_\theta)^2
\leq \operatorname{Var}_\theta(T)\operatorname{Var}_\theta(U_\theta).
$$

The score has mean zero, so $\operatorname{Var}_\theta(U_\theta)=E_\theta[U_\theta^2]=I_n(\theta)$. Substituting the covariance identity gives

$$
[g'(\theta)]^2
\leq \operatorname{Var}_\theta(T)I_n(\theta).
$$

Therefore

$$
\boxed{\operatorname{Var}_\theta(T)\geq \frac{[g'(\theta)]^2}{I_n(\theta)}}.
$$

For estimating $\theta$ itself, set $g(\theta)=\theta$, so $g'(\theta)=1$:

$$
\operatorname{Var}_\theta(T)\geq \frac{1}{I_n(\theta)}.
$$

This is a lower bound for unbiased estimators under the stated model and regularity conditions. It is not a universal bound for biased estimators.

### 3.2 Equality condition and the likelihood form

Equality in the Cauchy–Schwarz inequality holds exactly when the centered estimator and score are linearly related almost surely. For an unbiased estimator of $g(\theta)$ that reaches the bound, the relation is

$$
T-g(\theta)=\frac{g'(\theta)}{I_n(\theta)}U_\theta.
$$

For estimating $\theta$ itself, this becomes

$$
T-\theta=\frac{1}{I_n(\theta)}\frac{\partial}{\partial\theta}\log L(\theta;\mathbf X).
$$

The multiplier depends on the parameter but not on the observed sample. This is the score/likelihood condition given in the lecture for an unbiased estimator to attain the minimum variance bound. When an unbiased estimator satisfies it and the regularity assumptions hold, its variance equals the Cramér–Rao bound; no unbiased estimator can have a smaller variance.

If the equality condition does not hold, the Cramér–Rao bound may still be a valid lower bound, but it does not prove that a particular estimator is minimum variance. A lower bound need not be attained by an estimator in every model.

### 3.3 Fisher information for independent observations

For independent observations, the sample log-likelihood is a sum:

$$
\ell_n(\theta)=\sum_{i=1}^{n}\log f(X_i;\theta).
$$

The sample score is the sum of the individual scores. Under independence, the information adds:

$$
I_n(\theta)=nI_1(\theta),
$$

where $I_1(\theta)$ is the Fisher information in one observation. Keeping the sample information distinct from single-observation information avoids a common missing factor of $n$ in the bound.

### 3.4 Comparing unbiased estimators directly

When several unbiased estimators are supplied, a direct comparison is often simpler than finding the likelihood. First verify each expectation equals the target. Then calculate each variance under the same model. The estimator with the smallest variance is the best among that stated collection. This establishes a minimum only within the candidates compared unless a general theorem proves it is minimum over the full class.

## 4. Worked Applications

### 4.1 Choosing among three unbiased estimators

Let $X_1,X_2,X_3$ be independent observations with common mean $\mu$ and variance $\sigma^2$. Consider

$$
T_1=\frac{X_1+X_2+X_3}{3},\qquad
T_2=\frac{1}{2}X_1+\frac{1}{3}X_2+\frac{1}{6}X_3,
$$

$$
T_3=\frac{1}{4}X_1+\frac{1}{2}X_2+\frac{1}{4}X_3.
$$

**Step 1: Check unbiasedness.** For a linear estimator $T=\sum a_iX_i$, its expectation is $E(T)=\mu\sum a_i$. Each set of weights sums to one:

$$
\frac13+\frac13+\frac13=1,\qquad
\frac12+\frac13+\frac16=1,\qquad
\frac14+\frac12+\frac14=1.
$$

Thus $E(T_1)=E(T_2)=E(T_3)=\mu$.

**Step 2: Calculate the variances.** Independence means the variance of a weighted sum is the sum of squared weights times $\sigma^2$:

$$
\operatorname{Var}(T_1)=\sigma^2\left(\frac19+\frac19+\frac19\right)=\frac{\sigma^2}{3}.
$$

$$
\operatorname{Var}(T_2)=\sigma^2\left(\frac14+\frac19+\frac1{36}\right)=\frac{14\sigma^2}{36}=\frac{7\sigma^2}{18}.
$$

$$
\operatorname{Var}(T_3)=\sigma^2\left(\frac1{16}+\frac14+\frac1{16}\right)=\frac{6\sigma^2}{16}=\frac{3\sigma^2}{8}.
$$

**Step 3: Compare.** The coefficients are approximately $0.3333\sigma^2$, $0.3889\sigma^2$, and $0.3750\sigma^2$. Therefore $T_1$ has the smallest variance among these three unbiased estimators. This comparison alone establishes that $T_1$ is best among the three candidates; a claim that it is the UMVUE among all unbiased estimators requires a broader theorem or a bound argument.

### 4.2 Normal mean with known variance

Let $X_1,\ldots,X_n$ be a random sample from $N(\mu,\sigma^2)$ with known $\sigma^2$. The log-likelihood, apart from constants not involving $\mu$, is

$$
\ell(\mu)=-\frac{1}{2\sigma^2}\sum_{i=1}^{n}(X_i-\mu)^2.
$$

The score is

$$
U_\mu=\frac{\partial\ell}{\partial\mu}
=\frac{1}{\sigma^2}\sum_{i=1}^{n}(X_i-\mu).
$$

Its variance is $I_n(\mu)=n/\sigma^2$. The Cramér–Rao lower bound for an unbiased estimator of $\mu$ is therefore $\sigma^2/n$. The sample mean

$$
\bar X=\frac{1}{n}\sum_{i=1}^{n}X_i
$$

is unbiased and has variance $\sigma^2/n$. It also satisfies

$$
\bar X-\mu=\frac{\sigma^2}{n}U_\mu.
$$

Thus it attains the Cramér–Rao bound and is an MVUE of $\mu$ under this model.

### 4.3 Normal variance with known mean

Now suppose $X_i\sim N(\mu,\sigma^2)$ and $\mu$ is known while $\sigma^2$ is unknown. Write $v=\sigma^2$. The log-likelihood is

$$
\ell(v)=-\frac{n}{2}\log(2\pi v)-\frac{1}{2v}\sum_{i=1}^{n}(X_i-\mu)^2.
$$

The score is

$$
U_v=-\frac{n}{2v}+\frac{1}{2v^2}\sum_{i=1}^{n}(X_i-\mu)^2.
$$

The information is $I_n(v)=n/(2v^2)$, so the Cramér–Rao lower bound for an unbiased estimator of $v$ is $2v^2/n$. Consider

$$
T=\frac{1}{n}\sum_{i=1}^{n}(X_i-\mu)^2.
$$

Since each squared deviation has expectation $v$, $E(T)=v$. For a normal variable, the variance of $(X_i-\mu)^2$ is $2v^2$, so independence gives $\operatorname{Var}(T)=2v^2/n$. The estimator reaches the lower bound and is an MVUE of $\sigma^2$ when the mean is known.

### 4.4 Bernoulli parameter and the lower bound

For a Bernoulli sample with success probability $\theta$, the sum $T=\sum_{i=1}^{n}X_i$ has expectation $n\theta$, so $\bar X=T/n$ is unbiased for $\theta$. The information in one observation is $1/[\theta(1-\theta)]$, hence the sample information is $n/[\theta(1-\theta)]$. The Cramér–Rao bound is

$$
\operatorname{Var}(\bar X)\geq\frac{\theta(1-\theta)}{n}.
$$

But $\operatorname{Var}(\bar X)=\theta(1-\theta)/n$, so the bound is attained. This verifies that the sample proportion is minimum variance among unbiased estimators under the Bernoulli model and the regularity assumptions.

## 5. Revision Summary and Common Errors

### 5.1 Core results

- An MVUE is unbiased and has the smallest variance among unbiased estimators of the same target. A UMVUE has that property for every parameter value.
- For an unbiased estimator $T$ of $g(\theta)$, the regular-model Cramér–Rao bound is $\operatorname{Var}(T)\geq[g'(\theta)]^2/I_n(\theta)$.
- Equality in the bound requires $T-g(\theta)$ to be proportional to the sample score. For estimating $\theta$, the proportionality factor is $1/I_n(\theta)$.
- For independent observations, sample Fisher information is $n$ times the information in one observation.
- Under normal sampling with known variance, $\bar X$ is an MVUE for $\mu$. With known mean, $n^{-1}\sum(X_i-\mu)^2$ is an MVUE for $\sigma^2$.

### 5.2 Common errors

- Comparing variances before checking that every candidate is unbiased for the same target.
- Calling the smallest-variance estimator among three supplied candidates the UMVUE without proving a result over the full unbiased class.
- Omitting the factor $n$ when converting single-observation Fisher information to sample information.
- Reversing the score identity or forgetting that the score has mean zero under the regularity conditions.
- Treating the Cramér–Rao bound as automatically attainable. It is a lower bound; equality requires the score condition.
- Using $I_1(\theta)$ where the formula requires $I_n(\theta)$.
- Applying the score/information identity when the support depends on the parameter or differentiation under the integral is not justified.
- Confusing the MVUE's minimum variance among unbiased estimators with minimum mean squared error over biased and unbiased estimators alike.
- Stating that an estimator is unbiased without naming the model and parameter for which its expectation is calculated.'''}