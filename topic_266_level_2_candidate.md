## 1. Model, assumptions, and stationarity question

An autoregressive process of order one, AR(1), relates the current observation to the immediately preceding observation and a new innovation:

$$
X_t=\alpha X_{t-1}+e_t.
$$

The source assumes a purely random innovation process with $E(e_t)=0$, constant variance $\operatorname{Var}(e_t)=\sigma^2$, and zero covariance across distinct times:

$$
\operatorname{Cov}(e_t,e_{t'})=
\begin{cases}
\sigma^2,&t=t',\\
0,&t\ne t'.
\end{cases}
$$

The stationary AR(1) condition is $|\alpha|<1$. Under this condition, the influence of a shock from $j$ periods ago is scaled by $\alpha^j$ and decays in magnitude. The lesson derives the infinite moving-average representation, mean, variance, autocovariance, and autocorrelation function (ACF).

The source’s “purely random” innovation assumption is a second-order assumption: each innovation has mean zero, the same finite variance, and zero covariance with innovations at other times. This is enough for the mean, variance, and autocovariance derivations below. Independence is stronger and is not required for these particular second-order formulas. The model contains no intercept, so its stationary mean is zero; if the model were written with an intercept, its mean would have to be derived from that different equation.

These formulas use the zero-mean specification in the source. If an AR(1) is written with an intercept, its mean and centered representation must be handled separately; do not insert an intercept into the source equations and then quote the zero-mean results without adjustment.

## 2. Infinite moving-average representation

Repeated substitution gives

$$
X_t=\alpha X_{t-1}+e_t
=\alpha(\alpha X_{t-2}+e_{t-1})+e_t
=e_t+\alpha e_{t-1}+\alpha^2X_{t-2}.
$$

Continuing for $m$ steps,

$$
X_t=e_t+\alpha e_{t-1}+\cdots+\alpha^{m-1}e_{t-m+1}+\alpha^mX_{t-m}.
$$

When $|\alpha|<1$ and the stationary process has finite variance, the remainder term vanishes in mean square as $m\to\infty$. The causal stationary solution is therefore

$$
X_t=\sum_{j=0}^{\infty}\alpha^je_{t-j}
=e_t+\alpha e_{t-1}+\alpha^2e_{t-2}+\cdots.
$$

The same result can be written with the backward-shift operator $B$, defined by $BX_t=X_{t-1}$:

$$
(1-\alpha B)X_t=e_t,
\qquad
X_t=(1-\alpha B)^{-1}e_t
=(1+\alpha B+\alpha^2B^2+\cdots)e_t.
$$

This is the geometric-series expansion of the inverse operator. The coefficient on the shock $e_{t-j}$ is $\alpha^j$. The convergence condition is essential: if $|\alpha|\ge1$, the geometric coefficients do not decay and this stationary finite-variance representation does not apply.

The finite substitution formula shows exactly what is being discarded when the infinite representation is used:

$$
X_t=\sum_{j=0}^{m-1}\alpha^je_{t-j}+\alpha^mX_{t-m}.
$$

If the process has a finite stationary variance, the remainder has second moment proportional to $\alpha^{2m}\operatorname{Var}(X_{t-m})$. Since $|\alpha|<1$, this tends to zero as $m$ grows. Thus the infinite MA representation is the limit of finite substitutions, not an assumption that all future innovations affect the present value.

The mean can also be checked directly from the recursion. Under stationarity let $\mu=E(X_t)=E(X_{t-1})$. Taking expectations in $X_t=\alpha X_{t-1}+e_t$ gives

$$
\mu=\alpha\mu+0.
$$

Since $|\alpha|<1$ implies $\alpha\ne1$, the only solution is $\mu=0$, agreeing with the infinite-sum calculation.

## 3. Mean, variance, autocovariance, and ACF

### 3.1 Mean and variance

Taking expectations in the infinite representation gives

$$
E(X_t)=\sum_{j=0}^{\infty}\alpha^jE(e_{t-j})=0.
$$

Because innovations at different times are uncorrelated, all cross-covariance terms in the variance vanish. Hence

$$
\operatorname{Var}(X_t)
=\sigma^2\sum_{j=0}^{\infty}\alpha^{2j}
=\frac{\sigma^2}{1-\alpha^2}.
$$

The variance depends on the innovation variance and on the persistence coefficient. As $|\alpha|$ approaches 1 from below, $1-\alpha^2$ approaches zero and the stationary variance grows. The denominator is not $1-\alpha$ because variances use squared coefficients.

To see why the cross terms disappear, expand the variance of a finite partial sum. Terms such as $\alpha^j\alpha^k\operatorname{Cov}(e_{t-j},e_{t-k})$ vanish whenever $j\ne k$ by the white-noise covariance assumption. The diagonal terms are $\alpha^{2j}\sigma^2$, which form the geometric series

$$
\sigma^2(1+\alpha^2+\alpha^4+\cdots).
$$

Only after identifying the nonzero terms should the geometric-series formula be applied. Summing $1+\alpha+\alpha^2+\cdots$ for the variance would incorrectly use the covariance weights rather than their squares.

### 3.2 Autocovariance at lag $h$

For $h\ge0$, write both variables using the moving-average representation:

$$
X_t=\sum_{j=0}^{\infty}\alpha^je_{t-j},
\qquad
X_{t+h}=\sum_{k=0}^{\infty}\alpha^ke_{t+h-k}.
$$

Innovations are uncorrelated unless their time indices match. The terms match when $t-j=t+h-k$, so $k=j+h$. Therefore

$$
\gamma(h)=\operatorname{Cov}(X_t,X_{t+h})
=\sigma^2\sum_{j=0}^{\infty}\alpha^j\alpha^{j+h}
=\sigma^2\alpha^h\sum_{j=0}^{\infty}\alpha^{2j}
=\frac{\sigma^2\alpha^h}{1-\alpha^2}.
$$

This depends on the lag $h$ but not on time $t$. By covariance symmetry, $\gamma(-h)=\gamma(h)$, so for any integer lag,

$$
\gamma(h)=\frac{\sigma^2\alpha^{|h|}}{1-\alpha^2}.
$$

The matching-index step in the double sum is the key covariance argument. A pair $e_{t-j}$ and $e_{t+h-k}$ has nonzero covariance only if their time subscripts are equal. Solving $t-j=t+h-k$ gives $k=j+h$, so the surviving coefficient product is $\alpha^j\alpha^{j+h}=\alpha^{2j+h}$. Summing over $j\ge0$ gives $\alpha^h/(1-\alpha^2)$, then multiplying by the innovation variance yields $\gamma(h)$. All other cross-products contribute zero.

### 3.3 Autocorrelation function

The autocorrelation is the autocovariance divided by the variance at lag zero:

$$
\rho(h)=\frac{\gamma(h)}{\gamma(0)}=\alpha^{|h|}.
$$

Thus the AR(1) is weakly (second-order) stationary: its mean is constant and its autocovariance depends only on lag. The ACF decays geometrically in magnitude. If $0<\alpha<1$, the correlations are positive and decrease toward zero. If $-1<\alpha<0$, their signs alternate while their magnitudes decrease. The correlation at lag zero is always 1.

The ACF removes the measurement scale: multiplying the innovation variance changes $\gamma(h)$ and $\gamma(0)$ by the same factor, so it leaves $\rho(h)$ unchanged. For example, with $\alpha=0.6$, the ACF starts $1,0.6,0.36,0.216,\ldots$. With $\alpha=-0.5$, it starts $1,-0.5,0.25,-0.125,\ldots$. These patterns are useful when interpreting a correlogram: positive persistence gives a same-sign gradual decay, while negative persistence gives an alternating decay.

## 4. Alternative derivation and numerical example

The source also derives the ACF by multiplying the AR(1) equation by a lagged value. For $h>0$,

$$
\gamma(h)=\operatorname{Cov}(X_t,X_{t-h})
=\alpha\gamma(h-1)+\operatorname{Cov}(e_t,X_{t-h}).
$$

The last covariance is zero because $e_t$ is uncorrelated with earlier innovations and $X_{t-h}$ is built from those earlier shocks. Therefore

$$
\gamma(h)=\alpha\gamma(h-1)=\alpha^h\gamma(0),
$$

which gives $\rho(h)=\alpha^h$ for nonnegative $h$. This recursion is shorter than the full double-sum calculation, but it relies on the same stationarity and innovation assumptions.

For a numerical check, take $\alpha=0.6$ and $\sigma^2=4$. Then

$$
\gamma(0)=\frac{4}{1-0.6^2}=6.25,
\qquad
\gamma(1)=0.6(6.25)=3.75,
\qquad
\gamma(2)=0.6^2(6.25)=2.25.
$$

The corresponding autocorrelations are $\rho(0)=1$, $\rho(1)=0.6$, and $\rho(2)=0.36$. This confirms both the normalization by $\gamma(0)$ and the geometric decay.

For a negative coefficient, say $\alpha=-0.5$, the ACF begins $1,-0.5,0.25,-0.125,\ldots$. The signs alternate because the coefficient is negative, but the magnitudes still decay. The variance depends on $\alpha^2$, so it is unchanged if $\alpha$ is replaced by $-\alpha$ while $\sigma^2$ stays fixed.

The negative-coefficient example also separates variance from correlation behavior. At $\alpha=0.5$ or $\alpha=-0.5$ with the same innovation variance, $\gamma(0)=\sigma^2/(1-0.25)$ is identical. The lag-one covariance changes sign because it contains one factor of $\alpha$; the lag-two covariance is positive in both cases because it contains $\alpha^2$. Thus the sign pattern of the ACF identifies direction of serial dependence, while the variance reflects the squared persistence magnitude.

## 5. Exam method and common errors

1. State the model and innovation assumptions before using stationary formulas.
2. Check $|\alpha|<1$.
3. Obtain the MA representation by repeated substitution or the backward-shift geometric expansion.
4. Calculate the mean, then use zero cross-covariances to sum the variance series.
5. For $h\ge0$, match equal innovation time indices to derive $\gamma(h)$, or use the covariance recursion.
6. Normalize by $\gamma(0)$ to get $\rho(h)$ and use symmetry for negative lags.
7. Interpret the sign and decay pattern, especially when $\alpha<0$.

Common errors include confusing the innovation variance $\sigma^2$ with the process variance $\sigma^2/(1-\alpha^2)$; forgetting to square the MA weights in the variance; claiming the ACF equals the autocovariance; using $\alpha^h$ for negative lags without an absolute value; applying the stationary formulas when $|\alpha|\ge1$; and assuming independence where the derivation only needs zero covariance. The source’s “purely random” innovation assumption should be stated precisely as mean zero, constant variance, and zero covariance across time for these second-order calculations.

When writing a final solution, distinguish the three outputs and their units: $\operatorname{Var}(X_t)$ is measured in squared units of the series, $\gamma(h)$ is a covariance in squared units, and $\rho(h)$ is dimensionless and lies between -1 and 1. State the lag convention, usually $h\ge0$ followed by symmetry for negative lags. If a formula is quoted without its assumptions, it is not yet a complete answer: identify the zero-mean model, white-noise covariance, finite variance, and $|\alpha|<1$ before using the stationary results.