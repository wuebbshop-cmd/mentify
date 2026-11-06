## 1. Foundational Concepts, Definitions, and Axioms

Numerical analysis is the discipline concerned with the development and evaluation of methods for computing required numerical results from given numerical data. Because input information is rarely exact — it ordinarily comes from measurement devices of some sort — and because machines possess only finite memory, every computed result is an approximation of the true value. The quantity

$$
\text{error}=\text{true value}-\text{approximate value}
$$

is the central object of study in this unit. The purpose of the lecture is to expose the possibilities of error occurrence and the measures taken to safeguard against them.

The lecture objectives are stated as follows:

> By the end of this lecture the learner should be able to:

> i) Define and calculate round-off and truncation errors.

> ii) Identify measures taken to minimize round-off errors.

> iii) Define and calculate absolute, relative and percentage errors.

> iv) Calculate propagated errors with reference to numerical computations.

The conceptual map of the unit is therefore:

- **Source of error.** Errors enter through inexact data (inherent error), through the finite representation of real numbers on a machine (round-off error), through the replacement of an infinite process by a finite one (truncation error), and through the accumulation of these effects across arithmetic operations (propagation).
- **Measure of error.** The absolute error measures the raw size of the discrepancy; the relative error measures the discrepancy as a fraction of the true value and is the meaningful measure of accuracy because it accounts for the magnitude of the quantity; the percentage error expresses the relative error on a scale of one hundred.
- **Control of error.** Rounding to a stated number of decimal places or significant figures, and the correct counting of significant digits, are the practical instruments by which the size of the error is bounded and communicated.

The essential intuition is that a small absolute error can coexist with a large relative error, and vice versa. A discrepancy of $0.1$ is negligible when the true value is of order $10^{6}$ but catastrophic when the true value is of order $10^{-3}$. Accuracy statements must therefore always be attached to the size of the quantity being approximated.

## 2. Theorems, Lemmas, and Analytical Properties

### 2.1 Round-off and Truncation Errors

> **Definition (Round-off error).** Round-off errors arise because it is impossible to represent all real numbers exactly on a machine (computer) with finite memory. Rounding involves dropping out decimal points or significant figures and can be done by chopping (discarding digits) and by symmetric rounding.

Two distinct procedures must be distinguished:

- **Chopping (digit deletion).** All digits beyond the retained position are discarded without adjustment. The retained digits are unchanged.
- **Symmetric rounding.** The retained digit is increased by one unit whenever the first discarded digit is $5$ or greater, and left unchanged otherwise.

The source illustrates both procedures on a set of real numbers, rounded to four significant figures, rounded to four decimal places, and chopped to four significant figures:

| Real number | Rounded to 4 sf | Rounded to 4 dp | Chopped to 4 sf |
|---|---|---|---|
| $1.333$ | $1.333$ | $1.3333$ | $1.333$ |
| $0.03333$ | $0.03333$ | $0.0333$ | $0.03333$ |
| $0.6667$ | $0.6667$ | $0.6667$ | $0.6666$ |
| $3.142$ | $3.142$ | $3.1416$ | $3.141$ |

The fourth row is the most instructive: the value $3.142$ rounded to four decimal places becomes $3.1416$ because the discarded tail exceeds one half of the last retained place, whereas chopping to four significant figures yields $3.141$ because the digit $2$ is simply dropped. The third row shows the opposite behaviour: chopping $0.6667$ to four significant figures gives $0.6666$, while rounding gives $0.6667$.

> **Result (error introduced by rounding).** When rounding to $n$ decimal places, the error introduced satisfies

> 

$$
\lvert \text{error} \rvert \le 0.5\times 10^{-n}.
$$

This bound is the reason the half-unit appears throughout the unit: a number rounded to $n$ decimal places is uncertain by at most half a unit in the last retained place.

### 2.2 Absolute and Relative Errors

> **Definition (Absolute error).** Let $\bar{x}$ be an approximate number to an exact number $x$. The absolute error is the absolute difference between the exact number and the approximate number,

> 

$$
e_a=\lvert x-\bar{x}\rvert.
$$

> **Definition (Relative error).** The relative error is the absolute error divided by the magnitude of the exact value,

> 

$$
e_r=\frac{\lvert x-\bar{x}\rvert}{\lvert x\rvert},\qquad x\neq 0.
$$

> **Definition (Percentage error).** The percentage error is the relative error expressed on a scale of one hundred,

> 

$$
e_p=100\,e_r=100\,\frac{\lvert x-\bar{x}\rvert}{\lvert x\rvert}.
$$

The source stresses the interpretive point: the same relative error occurs for widely varying absolute errors. As a measure of accuracy the absolute error can be misleading; the relative error is more meaningful since it takes into consideration the size of the value.

### 2.3 Bounding the Error from a Decimal Representation

> **Result (maximum absolute error from correct decimal places).** In general, if a number is correct to $n$ decimal places, then the maximum absolute error is

> 

$$
\lvert e_a\rvert_{\max}=0.5\times 10^{-n}.
$$

Consequently, if $\bar{x}$ is correct to $n$ decimal places, the exact value lies in the interval

$$
\bar{x}-0.5\times 10^{-n}\le x\le \bar{x}+0.5\times 10^{-n}.
$$

The corresponding maximum relative error is obtained by dividing by the magnitude of the approximate value:

$$
\lvert e_r\rvert_{\max}=\frac{0.5\times 10^{-n}}{\lvert \bar{x}\rvert}.
$$

This is the mechanism used to answer interval questions: a number quoted as correct to a stated number of decimal places is not a point but an interval of half-width $0.5\times 10^{-n}$.

### 2.4 Significant Figures

> **Definition (Significant digits via relative error).** The relative error $e_r$ can be used to give a measure of the significant digits of an approximation. If the relative error satisfies

> 

$$
e_r\le 0.5\times 10^{-k},
$$

> then the approximation is said to be correct to $k$ significant digits.

The logic mirrors the decimal-place rule: the half-unit bound is applied at the level of the leading significant digit rather than at the level of the decimal point. This is why relative error, not absolute error, is the natural currency of significant-figure statements.

### 2.5 Propagation Errors

> **Definition (Propagation of error).** Propagation error is the error in a computed result that arises from the errors already present in the input quantities, transmitted through the arithmetic operations performed on them.

The source identifies the arithmetic situations in which error behaviour is dangerous:

- **Subtraction of nearly equal numbers.** The difference $x-u$ of two close numbers results in a small absolute error but a large relative error, because the relative error is measured against a small result.
- **Division by a small number or multiplication by a large number.** The subsequent division by the small number or multiplication by the large number magnifies the absolute error without modifying the relative error.
- **Addition of a large and a small number.** The addition of the large and small numbers $v$ and $u$ produces a large absolute error but not a large relative error.

These three observations constitute the standard diagnosis of ill-conditioned arithmetic and are frequently examined as short-answer items.

### 2.6 General Formula for Propagated Error

> **Theorem (General formula for propagated error).** Let $f(x_1,x_2,\dots,x_n)$ be a differentiable function of the variables $x_1,\dots,x_n$, and suppose each $x_i$ is known with absolute error at most $\Delta x_i$. Then the maximum absolute error in $f$ is

> 

$$
\Delta f\approx \sum_{i=1}^{n}\left\lvert \frac{\partial f}{\partial x_i}\right\rvert \Delta x_i.
$$

> The corresponding maximum relative error is

> 

$$
\frac{\Delta f}{\lvert f\rvert}\approx \sum_{i=1}^{n}\left\lvert \frac{\partial f}{\partial x_i}\right\rvert \frac{\Delta x_i}{\lvert f\rvert}.
$$

The formula is the first-order (total differential) estimate: each input error is weighted by the sensitivity of $f$ to that input, and the absolute values ensure that the worst case — all errors acting in the least favourable direction simultaneously — is captured. For the elementary operations the formula specialises as follows.

| Operation | First-order absolute-error estimate | First-order relative-error estimate |
|---|---|---|
| $f=x\pm y$ | $\Delta x+\Delta y$ | $\dfrac{\Delta x+\Delta y}{\lvert x\pm y\rvert}$ |
| $f=xy$ | $\lvert x\rvert \Delta y+\lvert y\rvert \Delta x$ | $\dfrac{\Delta x}{\lvert x\rvert}+\dfrac{\Delta y}{\lvert y\rvert}$ |
| $f=\dfrac{x}{y}$ | $\dfrac{\lvert x\rvert \Delta y+\lvert y\rvert \Delta x}{y^{2}}$ | $\dfrac{\Delta x}{\lvert x\rvert}+\dfrac{\Delta y}{\lvert y\rvert}$ |

The table gives total-differential estimates for small input errors, not exact finite-error identities. For example, if the computed inputs are $\bar{x},\bar{y}$ and the exact inputs are $\bar{x}+\delta x,\bar{y}+\delta y$, then the product error contains the additional term $\delta x\,\delta y$. For a quotient, the exact difference has denominator $\bar{y}(\bar{y}+\delta y)$, so the estimate requires the denominator to stay away from zero. The familiar rule is useful when these higher-order effects are negligible; otherwise retain them or use interval endpoints.

## 3. Formal Proofs, Derivations, and Methods

> **Result 1 (Rounding bound).** Rounding to $n$ decimal places introduces an error of magnitude at most $0.5\times 10^{-n}$; chopping to $n$ decimal places introduces an error of magnitude less than $10^{-n}$.

> **Result 2 (Interval from correct digits).** If $\bar{x}$ is correct to $n$ decimal places, then the exact value satisfies $\lvert x-\bar{x}\rvert\le 0.5\times 10^{-n}$, so $x$ lies in the closed interval $\left[\bar{x}-0.5\times 10^{-n},\ \bar{x}+0.5\times 10^{-n}\right]$.

> **Result 3 (Interval of the sum).** If $a$ and $b$ are each correctly rounded to the number of digits shown, with maximum absolute errors $\Delta a$ and $\Delta b$, then the exact sum lies in the interval

> 

$$
(a+b)-(\Delta a+\Delta b)\le a+b\le (a+b)+(\Delta a+\Delta b).
$$

> **Result 4 (Interval from a relative-error bound).** If $\bar{x}\neq 0$ is an approximation to $x$ with relative error bounded by $\rho$, that is

> 

$$
\frac{\lvert x-\bar{x}\rvert}{\lvert x\rvert}\le \rho,
$$

> then the exact value lies in the interval

> 

$$
\frac{\bar{x}}{1+\rho}\le x\le \frac{\bar{x}}{1-\rho}\qquad (\bar{x}>0,\ 0<\rho<1).
$$

> The endpoints are obtained by solving $\lvert x-\bar{x}\rvert=\rho\lvert x\rvert$ for $x$ on either side of $\bar{x}$.

> **Result 5 (Significant-digit criterion).** An approximation is correct to $k$ significant digits precisely when its relative error does not exceed $0.5\times 10^{-k}$.

> **Result 6 (General propagated-error formula).** For $f(x_1,\dots,x_n)$ differentiable, the maximum absolute error is $\Delta f\approx\sum_{i}\left\lvert \partial f/\partial x_i\right\rvert \Delta x_i$, and the maximum relative error is $\Delta f/\lvert f\rvert$.

> **Result 7 (Linear function).** For $f(x,y,z)=ax+by+cz$ with constant coefficients, the partial derivatives are the coefficients themselves, so

> 

$$
\Delta f=\lvert a\rvert \Delta x+\lvert b\rvert \Delta y+\lvert c\rvert \Delta z.
$$

> **Result 8 (Diagnosis of ill-conditioning).** Subtraction of nearly equal numbers produces a small absolute error but a large relative error; division by a small number or multiplication by a large number magnifies the absolute error while leaving the relative error unchanged; addition of a large and a small number produces a large absolute error but not a large relative error.

## 4. Representative Worked Examples and Solutions

### 4.1 Absolute and relative error in approximating $\pi$

**Problem.** Find the absolute and relative errors in approximating $\pi$ by $\bar{x}=3.14$.

**Solution.** Take the exact value to be $\pi=3.14159265\ldots$ and the approximation $\bar{x}=3.14$.

Step 1 — absolute error:

$$
\begin{aligned}
e_a&=\lvert \pi-\bar{x}\rvert\\
&=\lvert 3.14159265\ldots-3.14\rvert\\
&=0.00159265\ldots\\
&\approx 1.593\times 10^{-3}.
\end{aligned}
$$

Step 2 — relative error:

$$
\begin{aligned}
e_r&=\frac{e_a}{\lvert \pi\rvert}\\
&=\frac{0.00159265\ldots}{3.14159265\ldots}\\
&\approx 5.07\times 10^{-4}.
\end{aligned}
$$

Step 3 — percentage error (optional but often demanded):

$$
\begin{aligned}
e_p&=100\,e_r\\
&\approx 0.0507\%.
\end{aligned}
$$

**Interpretation.** The approximation is correct to about three significant digits, since $e_r\approx 5.07\times 10^{-4}$ is only slightly above $0.5\times 10^{-3}$ and well below $0.5\times 10^{-2}$.

### 4.2 Smallest interval containing the exact sum

**Problem.** Let $65.43$ and $17.0591$ be correctly rounded to the number of digits shown. Find the smallest interval in which the exact sum of the two numbers must lie.

**Solution.** Determine the maximum absolute error of each number from the number of decimal places displayed.

Step 1 — first number. The value $65.43$ is given to two decimal places, so

$$
\begin{aligned}
\Delta a&=0.5\times 10^{-2}\\
&=0.005.
\end{aligned}
$$

Step 2 — second number. The value $17.0591$ is given to four decimal places, so

$$
\begin{aligned}
\Delta b&=0.5\times 10^{-4}\\
&=0.00005.
\end{aligned}
$$

Step 3 — computed sum:

$$
\begin{aligned}
a+b&=65.43+17.0591\\
&=82.4891.
\end{aligned}
$$

Step 4 — total uncertainty:

$$
\begin{aligned}
\Delta a+\Delta b&=0.005+0.00005\\
&=0.00505.
\end{aligned}
$$

Step 5 — interval:

$$
82.4891-0.00505\le a+b\le 82.4891+0.00505,
$$

that is

$$
82.48405\le a+b\le 82.49415.
$$

**Answer.** The exact sum lies in $\left[82.48405,\ 82.49415\right]$.

**Marking note.** The examiner awards the method marks for identifying the half-unit bound at the correct decimal place for each number and for adding the two uncertainties; the accuracy mark is for the correct endpoints.

### 4.3 Interval of possible values from a relative-error bound

**Problem.** If a real number $x$ is approximated by $\bar{x}=456.123$ with relative error bounded by $0.1$, find the endpoints of the interval of possible values of $x$.

**Solution.** Let $\rho=0.1$. The condition is

$$
\frac{\lvert x-\bar{x}\rvert}{\lvert x\rvert}\le \rho.
$$

Step 1 — solve the two boundary equations. The endpoints occur where equality holds, once with $x>\bar{x}$ and once with $x<\bar{x}$.

For $x>\bar{x}$:

$$
\begin{aligned}
x-\bar{x}&=\rho x\\
x(1-\rho)&=\bar{x}\\
x&=\frac{\bar{x}}{1-\rho}.
\end{aligned}
$$

For $x<\bar{x}$:

$$
\begin{aligned}
\bar{x}-x&=\rho x\\
\bar{x}&=x(1+\rho)\\
x&=\frac{\bar{x}}{1+\rho}.
\end{aligned}
$$

Step 2 — substitute $\bar{x}=456.123$ and $\rho=0.1$.

Lower endpoint:

$$
\begin{aligned}
x_{\min}&=\frac{456.123}{1+0.1}\\
&=\frac{456.123}{1.1}\\
&=414.65727\ldots
\end{aligned}
$$

Upper endpoint:

$$
\begin{aligned}
x_{\max}&=\frac{456.123}{1-0.1}\\
&=\frac{456.123}{0.9}\\
&=506.80333\ldots
\end{aligned}
$$

**Answer.** The exact value satisfies

$$
414.657\le x\le 506.803
$$

to three decimal places.

**Pitfall.** A common error is to write $\bar{x}(1\pm\rho)$, which corresponds to bounding the error relative to the approximation rather than relative to the exact value. The correct endpoints divide by $1\pm\rho$.

### 4.4 Propagated error for a linear function

**Problem.** Let $f(x,y,z)=3x+y-z$. Determine the absolute and relative error in evaluating $f$ when $x=2.0\pm 0.005$, $y=3.0\pm 0.005$, and $z$ is known with absolute error $\Delta z$.

**Solution.** Apply the general propagated-error formula with the partial derivatives of the linear function.

Step 1 — partial derivatives:

$$
\begin{aligned}
\frac{\partial f}{\partial x}&=3,\\
\frac{\partial f}{\partial y}&=1,\\
\frac{\partial f}{\partial z}&=-1.
\end{aligned}
$$

Step 2 — first-order absolute-error estimate:

$$
\begin{aligned}
\Delta f&=\left\lvert \frac{\partial f}{\partial x}\right\rvert \Delta x+\left\lvert \frac{\partial f}{\partial y}\right\rvert \Delta y+\left\lvert \frac{\partial f}{\partial z}\right\rvert \Delta z\\
&=3(0.005)+1(0.005)+1(\Delta z)\\
&=0.015+0.005+\Delta z\\
&=0.020+\Delta z.
\end{aligned}
$$

Step 3 — computed value at the central estimates:

$$
\begin{aligned}
f(2.0,3.0,z)&=3(2.0)+3.0-z\\
&=9.0-z.
\end{aligned}
$$

Step 4 — maximum relative error:

$$
\frac{\Delta f}{\lvert f\rvert}=\frac{0.020+\Delta z}{\lvert 9.0-z\rvert}.
$$

**Answer.** The absolute error is $0.020+\Delta z$ and the relative error is $\dfrac{0.020+\Delta z}{\lvert 9.0-z\rvert}$.

**Marking note.** The coefficient $3$ on $x$ is the trap: the error in $x$ is amplified threefold, so the contribution of $x$ is $0.015$, not $0.005$. Students who simply add the three input errors lose the accuracy mark.

### 4.5 Propagation through a product

**Problem.** A rectangle is measured as $a=5\pm 1\ \text{cm}$ and $b=18\pm 2\ \text{cm}$. Estimate the absolute and relative error in the computed area $A=ab$.

**Solution.** Apply the product rule for propagated error.

Step 1 — computed area:

$$
\begin{aligned}
A&=ab\\
&=5\times 18\\
&=90\ \text{cm}^{2}.
\end{aligned}
$$

Step 2 — maximum absolute error:

$$
\begin{aligned}
\Delta A&=\lvert a\rvert \Delta b+\lvert b\rvert \Delta a\\
&=5(2)+18(1)\\
&=10+18\\
&=28\ \text{cm}^{2}.
\end{aligned}
$$

Step 3 — first-order relative-error estimate:

$$
\begin{aligned}
\frac{\Delta A}{\lvert A\rvert}&=\frac{28}{90}\\
&\approx 0.3111\\
&\approx 31.1\%.
\end{aligned}
$$

**First-order estimate.** The linearized calculation gives an area error of about $28\ \text{cm}^{2}$, or $31.1\%$ of the computed area. Because the input uncertainties are not especially small compared with the side lengths, check the exact bounds as well. The sides lie in $[4,6]$ cm and $[16,20]$ cm, so the area lies in $[64,120]\ \text{cm}^{2}$. Its largest deviation from $90$ is $30\ \text{cm}^{2}$, or $33.3\%$. The cross term accounts for the difference between the differential estimate and this finite-error bound.

**Cross-check by the first-order relative rule.** The relative input-error bounds are $1/5=0.2$ and $2/18\approx 0.1111$; their sum is $0.3111$, agreeing with the differential estimate, not the exact finite-error bound. Labeling it this way prevents a first-order estimate from being presented as a guarantee for large uncertainties.

### 4.6 Accuracy of a sum of measurements

**Problem.** Evaluate as accurately as possible $3.45+4.87$, where both numbers are correctly rounded to two decimal places.

**Solution.** The exact sum is $8.32$. Each addend carries a maximum absolute error of $0.005$, so the maximum absolute error of the sum is

$$
\begin{aligned}
\Delta s&=0.005+0.005\\
&=0.01.
\end{aligned}
$$

Hence the sum is $8.32\pm 0.01$, and the relative error is

$$
\begin{aligned}
\frac{\Delta s}{\lvert s\rvert}&=\frac{0.01}{8.32}\\
&\approx 1.2\times 10^{-3}.
\end{aligned}
$$

The result is therefore reliable to about three significant digits.

### 4.7 Demonstrating the three propagation pathologies

**Problem.** Using five-digit chopping arithmetic, illustrate the behaviour of the three operations identified in the source.

**Solution.** The three cases are treated separately.

Case 1 — subtraction of nearly equal numbers. If $x$ and $u$ are close, the computed difference $x-u$ has a small absolute error but a large relative error, because the relative error is measured against the small difference rather than against the large operands.

Case 2 — division by a small number or multiplication by a large number. The subsequent division by the small number or multiplication by the large number magnifies the absolute error without modifying the relative error.

Case 3 — addition of a large and a small number. The addition of the large and small numbers $v$ and $u$ produces a large absolute error but not a large relative error.

**Answer structure.** For full marks, each case must be named, the operation displayed symbolically, and the qualitative conclusion stated in terms of both absolute and relative error. The examiner is testing whether the student can distinguish the two error measures, not merely perform arithmetic.

### 4.7 Exact product and quotient error bounds

The total-differential formula is local. For a finite perturbation, its omitted terms can be written explicitly, which makes the assumptions testable instead of merely asserted. Let $\bar{x}$ and $\bar{y}$ be the values used in a computation, and suppose the exact values are $x=\bar{x}+\delta x$ and $y=\bar{y}+\delta y$, with $|\delta x|\le a$ and $|\delta y|\le b$.

For a product, expansion gives the exact signed error

$$
xy-\bar{x}\bar{y}=\bar{x}\delta y+\bar{y}\delta x+\delta x\delta y.
$$

Consequently,

$$
|xy-\bar{x}\bar{y}|
\le |\bar{x}|b+|\bar{y}|a+ab.
$$

The first two terms are the linearized estimate; the last term is a second-order contribution. Dividing by $|\bar{x}\bar{y}|$ when both approximations are nonzero gives the exact relative-error bound

$$
\frac{|xy-\bar{x}\bar{y}|}{|\bar{x}\bar{y}|}
\le \frac{a}{|\bar{x}|}+\frac{b}{|\bar{y}|}
+\frac{ab}{|\bar{x}\bar{y}|}.
$$

Thus adding relative-error magnitudes is a first-order approximation, while including their product gives this simple exact upper bound.

For a quotient, direct subtraction gives

$$
\frac{x}{y}-\frac{\bar{x}}{\bar{y}}
=\frac{\bar{y}\delta x-\bar{x}\delta y}
{\bar{y}(\bar{y}+\delta y)}.
$$

If $b<|\bar{y}|$, the denominator is separated from zero and

$$
\left|\frac{x}{y}-\frac{\bar{x}}{\bar{y}}\right|
\le \frac{|\bar{y}|a+|\bar{x}|b}
{|\bar{y}|(|\bar{y}|-b)}.
$$

Without the condition $b<|\bar{y}|$, the denominator interval may include zero; then a finite quotient bound need not exist. This condition is not a technical footnote. It determines whether the output can be bounded at all.

### 4.8 Cancellation, relative accuracy, and input intervals

Suppose two measured quantities are $u=100.02\pm0.01$ and $v=100.00\pm0.01$. The central difference is $0.02$. The maximum absolute error in the difference is $0.02$, so a worst-case relative error measured against the central result is $100\%$. Every individual measurement is accurate to roughly one part in ten thousand, yet their small difference is not. This does not contradict the accuracy of the inputs; subtraction has discarded most of the common leading digits.

The same phenomenon appears algebraically when computing $x-y$ for nearly equal numbers. The absolute perturbations remain tied to the operands, but the result in the denominator of the relative-error ratio is small. This is often described as loss of significance. The right response is to report the absolute error and the relative error, recognize that the subtraction is sensitive, and seek an algebraically stable reformulation only when a valid equivalent expression is available and permitted by the problem.

Input intervals show this effect without relying on a differential approximation. If $u\in[100.01,100.03]$ and $v\in[99.99,100.01]$, then the difference lies in $[0,0.04]$. The central value $0.02$ is only one possible value in this interval; zero is also possible. A relative-error statement against the central difference is therefore not a uniform finite bound over all allowed inputs. This is why a denominator or result that can approach zero requires interval analysis rather than a routine percentage calculation.

For a sum, the same input intervals produce $u+v\in[200.00,200.04]$. The absolute uncertainty is again $0.02$ on either side of the central value $200.02$, but the relative uncertainty is roughly $0.01\%$. Pairing the sum and difference examples makes the role of scale explicit: absolute-error bounds can be identical even when the practical significance is dramatically different.

### 4.9 An error budget for a multi-step computation

Consider a quantity computed as $Q=(a+b)c$, where $a$, $b$, and $c$ are measured and the final multiplication is rounded. There are several distinct contributions: the original data tolerances, propagation through the sum, propagation through the product, and new rounding of the computed result. Listing them separately avoids counting one source twice or overlooking another.

Let $\bar{a}=12.30$ with error at most $0.005$, $\bar{b}=0.70$ with error at most $0.005$, and $\bar{c}=2.0$ with error at most $0.05$. The central sum is $13.00$, and its input uncertainty is at most $0.010$ by the triangle inequality. The central product is $26.0$. The first-order contribution from the sum is about $|c|(0.010)=0.020$, and the contribution from $c$ is about $|a+b|(0.05)=0.650$. The dominant uncertainty comes from $c$.

For a rigorous product bound, include the cross term $0.010(0.05)=0.0005$, so the product uncertainty before final rounding is at most $0.6705$. If the result is then rounded to one decimal place, the output representation adds at most $0.05$. A conservative total is $0.7205$. This bound is intentionally cautious: it assumes the input errors and final rounding all take the direction that increases the discrepancy. If uncertainty distributions or correlations are supplied, a different statistical model may be appropriate, but no such assumptions should be invented.

The calculation also shows why the smallest displayed increment is not automatically the largest source of uncertainty. The numbers $a$ and $b$ have more decimal digits than $c$, but the relevant factors in the product and their tolerances determine the contributions. An error budget should list each contribution in common output units, rank them by size, and preserve the distinction between a first-order estimate and a conservative finite bound.

### 4.10 Stable reporting and final checks

A useful report states the central computed value, the error measure, the assumptions, and the final precision. For example, “the first-order propagated absolute error is approximately $0.02$ units under small input perturbations” is more informative than “the answer is accurate to two decimal places” when no rounding criterion has been established. If a rigorous range is available, report its endpoints and explain which input limits attain them.

The error calculation itself should be audited independently. Check that the absolute difference is nonnegative; that the relative-error denominator is the stated reference value; that units cancel only in the relative ratio; and that a percentage includes multiplication by $100$. For formulas with products, check whether cross terms matter. For quotients, verify the denominator interval excludes zero. For sums, ensure uncertainty bounds have been added rather than canceled without evidence.

Finally, distinguish numerical stability from input accuracy. A stable sequence of operations does not make imprecise measurements exact, while precise inputs can still be damaged by an unstable calculation. The purpose of an error analysis is not to guarantee a small answer in every problem. It is to identify where error originates, determine how the chosen computation transmits it, and communicate what the resulting digits can genuinely support.

### 4.11 Relative error after subtracting and dividing

The expression $r=(a-b)/c$ combines two sources of sensitivity: cancellation in the numerator and possible amplification from the denominator. A first-order absolute bound, when $c$ is bounded away from zero, is

$$
|\Delta r|\approx
\frac{\Delta a+\Delta b}{|c|}
+\frac{|a-b|\,\Delta c}{|c|^2}.
$$

The first term grows relative to $r$ when $a$ and $b$ nearly cancel. The second grows if $|c|$ is small. A formula can therefore be sensitive even when each input has a small absolute error.

If $a=50.02\pm0.01$, $b=50.00\pm0.01$, and $c=2.0\pm0.02$, the central value is $0.01$. The numerator uncertainty can equal its central value, so the percentage uncertainty is not small. Direct interval propagation gives a numerator in $[0,0.04]$ and a positive denominator in $[1.98,2.02]$, hence $r\in[0,0.0202]$ approximately. The interval is more informative than a differential percentage centered at a value close to zero.

This example shows that a derivative formula can correctly flag high sensitivity without providing the best finite bound. When an intermediate interval touches zero, move to interval reasoning before assigning a relative error.

### 4.12 Reproducible error reporting

A clear numerical report records the central values, input error bounds, operation, and error convention. In a multi-step derivation, retain an intermediate bound rather than recomputing it from rounded displayed digits. If the task requests a maximum, use worst-case signs; if it requests an expected uncertainty, use a stated statistical model. These conventions should not be mixed.

For products and quotients, state whether the reported relative-error sum is first order. For interval results, identify the monotonicity or endpoint argument. For a general differentiable function, list the derivatives and the point at which the sensitivities were evaluated. This documentation lets another reader distinguish a theorem-backed guarantee from a useful approximation.

Finally, report digits that are consistent with the uncertainty. A numerical value can be carried to many digits internally for reproducibility, but the interpreted answer should not imply more knowledge of the true quantity than the data or method supports.

## 5. Mathematical Extensions, Limits, and Common Errors

### 5.1 Definitions that are examined verbatim

> **Inherent error.** Error present in the initial data before any computation begins, arising from the measurement or source of the data rather than from the arithmetic.

> **Numerical stability.** The property of an algorithm whereby small perturbations in the input, or small errors introduced during the computation, produce only correspondingly small perturbations in the output; an unstable algorithm amplifies such errors.

> **Iteration.** A procedure that generates a sequence of successive approximations, each derived from the previous one, with the intention of approaching the required solution.

These three definitions appear as short two-mark items and must be reproduced precisely, with the distinction between data error, algorithmic behaviour, and repeated approximation kept explicit.

### 5.2 Formula sheet to memorise

- Absolute error: $e_a=\lvert x-\bar{x}\rvert$.
- Relative error: $e_r=\dfrac{\lvert x-\bar{x}\rvert}{\lvert x\rvert}$.
- Percentage error: $e_p=100\,e_r$.
- Rounding to $n$ decimal places: $\lvert e_a\rvert\le 0.5\times 10^{-n}$.
- Correct to $k$ significant digits: $e_r\le 0.5\times 10^{-k}$.
- Interval from a relative-error bound $\rho$: $\dfrac{\bar{x}}{1+\rho}\le x\le \dfrac{\bar{x}}{1-\rho}$.
- General propagated error: $\Delta f\approx\sum_{i}\left\lvert \dfrac{\partial f}{\partial x_i}\right\rvert \Delta x_i$.
- Sum or difference: absolute errors add.
- Product or quotient: relative-error magnitudes add only as a first-order estimate when the inputs have small relative errors and the quotient denominator is safely nonzero; the exact product and quotient include higher-order terms.

### 5.3 High-frequency question patterns

- **Compute absolute and relative error for a given approximation** (for example $\pi\approx 3.14$). Always state the exact value to more digits than the approximation, compute the difference, then divide by the exact value.
- **Find the interval containing an exact quantity** from correctly rounded data. Identify the number of decimal places of each datum, attach the half-unit bound, and add the bounds for sums.
- **Find the interval from a relative-error bound.** Solve the two boundary equations and divide by $1\pm\rho$; never multiply the approximation by $1\pm\rho$.
- **Propagated error for a linear or polynomial function.** Differentiate, take absolute values of the partial derivatives, and weight each input error.
- **Propagated error for a product or quotient.** State the nonzero-input and small-relative-error assumptions before using the first-order relative-error estimate; for larger errors, retain the higher-order product term or the quotient denominator.
- **Explain the three propagation pathologies** (subtraction of nearly equal numbers, division by a small number, addition of a large and a small number) in terms of absolute versus relative error.
- **Define inherent error, numerical stability, and iteration.**
- **Explain why numerical analysis is important and outline the steps of a numerical solution**, indicating the sources of error at each stage: formulation of the mathematical model, selection of a numerical method, implementation, and interpretation of output. Errors may enter through the model (inherent), through representation (round-off), through finite processes (truncation), and through accumulation (propagation).

### 5.4 Common pitfalls that cost marks

- **Confusing absolute and relative error.** The relative error divides by the exact value, not by the error and not by the approximation.
- **Using the wrong half-unit.** A number given to two decimal places has uncertainty $0.005$, not $0.01$; a number given to four decimal places has uncertainty $0.00005$.
- **Forgetting the coefficient in a linear function.** In $f=3x+y-z$ the error in $x$ is tripled; the partial derivative, not the variable, is the weight.
- **Applying relative-error addition without its assumptions.** For sums and differences, bound absolute errors. For products and quotients, the sum of relative-error magnitudes is a first-order small-error estimate, not an exact identity for arbitrary errors; use the exact expansion when the error is not negligible.
- **Writing $\bar{x}(1\pm\rho)$ for a relative-error interval.** The correct endpoints are $\bar{x}/(1\pm\rho)$.
- **- **Quoting too many digits.** A result cannot be more accurate than its least accurate input; report the sum $65.43+17.0591$ as $82.49$ with a stated uncertainty, not as $82.4891$ presented as exact.
- **Treating a rounded number as a point.** Every quoted decimal is an interval of half-width $0.5\times 10^{-n}$; interval questions are lost when the student substitutes the central value only.
- **Omitting the percentage conversion.** When the question says percentage error, multiply the relative error by $100$ and attach the percent sign.
- **Sign errors in the propagated-error formula.** The absolute values on the partial derivatives are mandatory; without them the worst-case contributions can cancel and the bound becomes too small.

### 5.5 Answer-structure templates

For an error-computation item, present the work in four labelled stages: state the exact value and the approximation; compute the absolute error; compute the relative error; convert to a percentage if requested. Each stage earns a method mark, so a slip in arithmetic still leaves partial credit.

For an interval item, present the work in three stages: identify the number of decimal places and hence the half-unit bound for each datum; compute the central value; add the bounds and write the closed interval with both endpoints. State the interval with the inequality signs in the same direction as the question.

For a propagated-error item, present the work in four stages: write the function and its partial derivatives; substitute the given absolute errors into the general formula; evaluate the maximum absolute error; divide by the magnitude of the computed function value to obtain the relative error. Where the function is a product or quotient, add the relative-error cross-check as a verification line.

For a definition item, give the definition in one sentence, then one sentence of contrast or example. Definitions of inherent error, numerical stability, and iteration are each worth their full marks only when the distinguishing feature is stated.

### 5.6 Time-management strategy

Allocate roughly one minute per mark. The definition items are the fastest marks and should be answered first and in full sentences. The interval and propagated-error items carry the heaviest mark weighting and deserve the bulk of the time; leave the arithmetic of the final division to the end so that the method marks are already secured. Always finish by checking that every computed error is non-negative, that every interval has its lower endpoint below its upper endpoint, and that every relative error is dimensionless while every absolute error carries the units of the quantity.

### 5.7 Self-test questions

1. Define round-off error and truncation error, and state one measure taken to minimise round-off error in computation.
2. Round $0.6667$ to four significant figures and chop it to four significant figures; state the error introduced in each case.
3. Find the absolute, relative, and percentage errors in approximating $\pi$ by $3.14$.
4. Let $65.43$ and $17.0591$ be correctly rounded to the number of digits shown. Find the smallest interval in which the exact sum must lie.
5. If $x$ is approximated by $\bar{x}=456.123$ with relative error bounded by $0.1$, find the endpoints of the interval of possible values of $x$.
6. Let $f(x,y,z)=3x+y-z$ with $x=2.0\pm 0.005$ and $y=3.0\pm 0.005$. Determine the absolute and relative error in $f$.
7. A rectangle has sides $a=5\pm 1\ \text{cm}$ and $b=18\pm 2\ \text{cm}$. Estimate the absolute and relative error in the area.
8. Explain why the subtraction of two nearly equal numbers produces a small absolute error but a large relative error, and why the addition of a large and a small number produces a large absolute error but not a large relative error.
9. Define inherent error, numerical stability, and iteration.
10. Outline the steps involved in the numerical solution of a real-life problem using digital computers, indicating clearly the possible sources of error at each step.

### 5.8 Further reading

### 5.9 Extended error-budget exemplar

**Question.** A rectangular plate is measured as \(L_r=12.4\) cm by \(W_r=5.8\) cm, each to the nearest \(0.1\) cm. Find the recorded area and a worst-case bound for its error. Then explain which digits are defensible.

**Model and bounds.** Nearest-tenth rounding gives \(|\varepsilon_L|\le 0.05\) cm and \(|\varepsilon_W|\le0.05\) cm. Begin with the exact identity, not only the linearized formula:

$$
(L_r+\varepsilon_L)(W_r+\varepsilon_W)-L_rW_r
=L_r\varepsilon_W+W_r\varepsilon_L+\varepsilon_L\varepsilon_W.
$$

The triangle inequality then gives

$$
|\Delta A|\le |L_r|(0.05)+|W_r|(0.05)+(0.05)^2
=0.9125\text{ cm}^2.
$$

Since \(A_r=12.4(5.8)=71.92\text{ cm}^2\), the absolute error is bounded by about \(0.913\text{ cm}^2\). A relative estimate based on the recorded area is \(0.9125/71.92\approx0.01269\), or about \(1.27\%\). Because the exact area is unknown, describe this ratio as an estimate relative to \(A_r\), not the exact relative error defined with the true area. The reported area should not imply hundredths of a square centimetre of measurement accuracy merely because multiplication produced two decimal places. A practical report is approximately \(71.9\text{ cm}^2\), together with the error bound.

**Check by intervals.** The dimensions lie in \(12.35\le L<12.45\) and \(5.75\le W<5.85\), assuming the usual nearest-rounding convention. Since both are positive, multiplying endpoints gives an enclosing interval for the area:

$$
12.35(5.75)\le LW<12.45(5.85),
\qquad 71.0125\le LW<72.8325.
$$

This interval is a coarse independent check, not the same tight symmetric first-order bound. It also illustrates why inequalities and assumptions must be explicit: endpoint order would need reconsideration if an interval crossed zero.

### 5.10 Separating propagated error from arithmetic error

If the area product were evaluated with a fixed-precision system, the product operation could introduce an additional round-off contribution. The measurement bound above is present even with exact multiplication; it is a propagated input error. A computed product might then be rounded from \(71.92\) to \(71.9\), introducing a separate representation error of at most \(0.05\text{ cm}^2\) if rounded to the nearest tenth. A complete error budget may combine conservative bounds, but it should keep the source labels visible:

$$
\text{total bound}\ \le\ \text{measurement-propagation bound}
+\text{arithmetic-rounding bound}.
$$

The inequality is a worst-case sum, not a claim that the two errors always point in the same direction. If exact arithmetic is used on the recorded numbers, the second term is zero for this particular multiplication; if the stored input values were themselves rounded, the first term remains. This distinction prevents a common remedy error: increasing calculator precision cannot reduce the original measurement uncertainty.

### 5.11 A final exam-answer audit

Before submitting a propagation calculation, check the sign convention for signed error, then use absolute values for any magnitude bound. Confirm that a decimal-place instruction has been converted into half a unit in the last place; do not substitute a significant-figure rule. State when the first-order Taylor approximation is being used and identify nonzero denominators required for a relative estimate. Keep dimensions consistent through each derivative: a partial derivative carries units that convert the input uncertainty into the output unit. Finish with a sensible number of digits and an interpretation such as “the output is estimated within this bound,” rather than merely copying a calculator display.

The unit is developed in the lecture sequence on errors and approximations, with the treatment of round-off and truncation errors, absolute and relative errors, significant figures, propagation errors, and the general formula for propagated error forming the foundation for all later work on polynomials, finite differences, numerical differentiation, numerical integration, and iterative techniques. Students should consolidate the definitions and the propagated-error formula before proceeding to those later units, since every subsequent algorithm inherits the error analysis established here.
