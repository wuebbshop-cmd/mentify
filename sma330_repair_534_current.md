## 1. Core Concept Overview & Intuition

### 1.1 Lecture Objectives

By the end of this unit you should be able to:

- Define and compute round-off errors, truncation errors, absolute errors, relative errors and percentage errors.
- Explain how errors arise in numerical work and how they can be reduced.
- State and apply the general formula for the propagation of error through the four arithmetic operations.
- Use the range method to bound the value of an expression when every number in it is rounded.
- Estimate a definite integral using the trapezoidal rule and Simpson's one-third rule, and measure the accuracy of the estimate by comparing it with the exact value obtained by direct integration.

### 1.2 A First Everyday Picture

Imagine you weigh yourself on a bathroom scale that only shows whole kilograms. Your true mass might be $62.4$ kg, but the scale says $62$ kg. The scale has not lied; it has simply been unable to store the full detail. Numerical computing behaves in exactly the same way. A computer has only a fixed amount of memory, so it cannot hold every digit of a real number. It keeps a shortened version, and that shortening is the source of what we call **error**.

The analogy stops being exact in one place: a scale rounds once, but a computer may round many times in a long calculation, and the small shortenings can add up. That accumulation is the subject of propagation of errors.

### 1.3 Round-off and Truncation Errors

> **Definition (Round-off error).** Round-off error arises because it is impossible to represent all real numbers exactly on a machine with finite memory. It involves dropping decimal digits or significant figures, and it can be done either by chopping (truncating) or by symmetric rounding.

Two ways of shortening a number appear in the source:

- **Chopping (truncation):** simply delete the unwanted digits. The number $2.3478$ chopped to two decimal places becomes $2.34$.
- **Symmetric rounding:** look at the first deleted digit; if it is $5$ or more, raise the last kept digit by one, otherwise leave it. The number $2.3478$ rounded to two decimal places becomes $2.35$.

The word **truncation** is also used for a second, related idea: replacing an infinite process (such as an infinite series or an exact curve) by a finite one. Both uses share the same spirit — we stop early and accept a small loss.

### 1.4 Absolute and Relative Errors

Let $x$ be the exact number and let $x_r$ be an approximation to it.

> **Definition (Absolute error).** The absolute error is the absolute difference between the exact number and the approximate number:
> 

$$
e_{\text{abs}}=\lvert x-x_r\rvert.
$$

> **Definition (Relative error).** The relative error is the absolute error measured as a fraction of the exact value:
> 

$$
e_r=\frac{\lvert x-x_r\rvert}{\lvert x\rvert}.
$$

The absolute error tells you *how far off* you are in the same units as the quantity. The relative error tells you *how serious* that miss is. A miss of $1$ cm is huge when measuring a pencil and tiny when measuring a football pitch. Multiplying the relative error by $100$ gives the **percentage error**.

### 1.5 Significant Figures

A number written as correct to $n$ decimal places carries a built-in uncertainty. If a number is correct to $n$ decimal places, the largest possible absolute error is

$$
e_{\text{abs}}=0.5\times 10^{-n}.
$$

For example, a value quoted as $8.35678$ correct to five decimal places has $e_{\text{abs}}\le 0.5\times 10^{-5}$. The idea is simple: the last quoted digit could have been rounded up or down by at most half of one unit in that place.

### 1.6 Propagation Errors

> **Definition (Propagated error).** The error in the result of an arithmetic operation that arises from the initial errors in the numbers used in that operation is called the propagated error. The total cumulative error at any step of a procedure is called the accumulated error.

> **Definition (Inherent error).** Inherent error is the error already present in the data before any computation begins — for instance, a measured length quoted only to the nearest centimetre.

The distinction matters in examinations: inherent error comes *with the data*, accumulated error *grows during the calculation*.

## 2. Mathematical Formalization & Core Definitions

### 2.1 The Definite Integral as a Limit of Sums

Numerical integration begins with the definition of the definite integral. Let $f$ be a bounded function on a closed interval $[a,b]$. A partition $P$ of $[a,b]$ is a finite set of points

$$
a=x_0<x_1<\cdots<x_n=b.
$$

The $i$-th subinterval is $[x_{i-1},x_i]$, its length is $\Delta x_i=x_i-x_{i-1}$, and the mesh of the partition is

$$
\lVert P\rVert=\max_{1\le i\le n}\Delta x_i.
$$

Choose a sample point $\xi_i\in[x_{i-1},x_i]$ in each subinterval. The corresponding Riemann sum is

$$
S(P,f)=\sum_{i=1}^{n}f(\xi_i)\Delta x_i.
$$

If these sums approach one and the same number as the mesh tends to zero, independently of the choice of partition and sample points, then $f$ is Riemann integrable on $[a,b]$ and that number is the definite integral:

$$
I[f]=\int_a^b f(x)\,dx=\lim_{\lVert P\rVert\to 0}\sum_{i=1}^{n}f(\xi_i)\Delta x_i.
$$

Every continuous function on a closed interval is Riemann integrable. The definition already suggests the numerical strategy: replace the limiting process by a finite weighted sum of function values.

### 2.2 Quadrature Formulae

> **Definition (Quadrature formula).** Let $x_0,x_1,\dots,x_n$ be distinct points in $[a,b]$, called nodes, and let $A_0,A_1,\dots,A_n$ be real numbers, called weights. A quadrature formula is the linear functional $Q[f]=\sum_{i=0}^{n}A_i f(x_i)$. The quadrature error is $E[f]=I[f]-Q[f]$, where $I[f]$ is the exact integral.

The weights do not depend on $f$. They are chosen so that the formula is exact for selected functions, usually polynomials up to some degree. Because both the integral and the quadrature sum are linear,

$$
Q[\alpha f+\beta g]=\alpha Q[f]+\beta Q[g],
$$

and

$$
I[\alpha f+\beta g]=\alpha I[f]+\beta I[g].
$$

Therefore the error is also linear:

$$
E[\alpha f+\beta g]=\alpha E[f]+\beta E[g].
$$

A single quadrature formula on a fixed interval produces one approximation. To improve accuracy one normally refines the interval or sums the elementary formula over subintervals, but the basic object remains a weighted sum of function values at prescribed nodes.

### 2.3 Degree of Exactness

> **Definition (Degree of exactness).** A quadrature formula $Q$ has degree of exactness $m$ if $E[p]=0$ for every polynomial $p$ of degree at most $m$, but $E[p]\ne 0$ for at least one polynomial of degree $m+1$. Equivalently, $Q[p]=I[p]$ for all polynomials of degree at most $m$, and this statement fails for degree $m+1$.

Polynomial exactness is a natural test because polynomials are easy to integrate exactly. If a rule integrates all polynomials up to degree $m$ exactly, then for a smooth function, whose Taylor polynomial of degree $m$ is close to the function, the rule is expected to be accurate. A higher degree of exactness generally indicates a more accurate rule for smooth integrands, although accuracy also depends on the size of the interval and on the derivatives of $f$.

### 2.4 Three Elementary Rules

The simplest quadrature rules use one interval $[a,b]$ and evaluate $f$ at one or more points inside it.

The midpoint rule uses the single node $c=(a+b)/2$ and the weight $b-a$:

$$
M[f]=(b-a)f\left(\frac{a+b}{2}\right).
$$

It approximates the area under the curve by the area of a rectangle whose height is the value of $f$ at the midpoint.

The trapezoidal rule uses the two endpoints $a$ and $b$, each with weight $(b-a)/2$:

$$
T[f]=\frac{b-a}{2}\bigl(f(a)+f(b)\bigr).
$$

It approximates the area by the area of the trapezoid whose top edge is the straight line joining the points $(a,f(a))$ and $(b,f(b))$.

Simpson’s rule uses the three equally spaced nodes $a$, $c=(a+b)/2$, and $b$, with weights $(b-a)/6$, $4(b-a)/6$, and $(b-a)/6$:

$$
S[f]=\frac{b-a}{6}\left(f(a)+4f\left(\frac{a+b}{2}\right)+f(b)\right).
$$

It is obtained by integrating the quadratic polynomial that passes through the three function values at $a$, $c$, and $b$. Although it is derived from a quadratic interpolant, Simpson’s rule is exact for all polynomials of degree at most three; its degree of exact

## 3. Key Theorems & Essential Results

> **Result 1 (Decimal-place bound).** If a number is correct to $n$ decimal places, then its absolute error satisfies $e_{\text{abs}}=0.5\times 10^{-n}$.

> **Result 2 (Relative error).** For exact value $x$ and approximation $x_r$, the relative error is $e_r=\lvert x-x_r\rvert/\lvert x\rvert$, and the percentage error is $100\,e_r$.

> **Result 3 (Propagation, addition and subtraction).** The absolute errors of the operands add.

> **Result 4 (Propagation, multiplication and division).** The relative errors of the operands add, to first order.

> **Result 5 (Trapezoidal rule).** For $n$ equal strips of width $h=(b-a)/n$ with ordinates $y_0,y_1,\dots,y_n$,
> 

$$
I\approx \frac{h}{2}\Bigl[y_0+2(y_1+y_2+\cdots+y_{n-1})+y_n\Bigr].
$$

> **Result 6 (Simpson's one-third rule).** For an even number $n$ of strips of width $h$,
> 

$$
I\approx \frac{h}{3}\Bigl[y_0+4(y_1+y_3+\cdots)+2(y_2+y_4+\cdots)+y_n\Bigr].
$$

> **Result 7 (Error in the trapezoidal rule).** The error satisfies a bound of the form
> 

$$
\lvert E_T\rvert\le \frac{(b-a)}{12}h^{2}M_2,
$$

> where $M_2$ is the maximum of $\lvert f''(x)\rvert$ on $[a,b]$.

> **Result 8 (Error in Simpson's rule).** The maximum error satisfies a bound of the form
> 

$$
\lvert E_S\rvert\le \frac{(b-a)}{180}h^{4}M_4,
$$

> where $M_4$ is the maximum of $\lvert f^{(4)}(x)\rvert$ on $[a,b]$.

> **Result 9 (Gauss–Legendre three-point formula).** On the standard interval $[-1,1]$,
> 

$$
I\approx \frac{5}{9}f\!\left(-\sqrt{\tfrac{3}{5}}\right)+\frac{8}{9}f(0)+\frac{5}{9}f\!\left(\sqrt{\tfrac{3}{5}}\right).
$$

> **Result 10 (Percentage error of an approximation).** If $I$ is the exact value and $I_A$ the approximation, then
> 

$$
\text{percentage error}=\frac{\lvert I-I_A\rvert}{\lvert I\rvert}\times 100\%.
$$

The trapezoidal rule joins the tops of the ordinates with straight lines, so it over-estimates the area under a curve that bends upwards. Simpson's rule fits a parabola through three consecutive ordinates and is therefore far more accurate for smooth curves. The Gauss–Legendre formula chooses its evaluation points cleverly rather than at equal spacing, which is why three points already give excellent accuracy.

## 4. Worked Exemplar Problem with Step-by-Step Solution

### 4.1 Problem

Evaluate

$$
I=\int_{0}^{6}\frac{dx}{1+x^{2}}
$$

using (i) the trapezoidal rule and (ii) Simpson's one-third rule with $h=1$. Then evaluate the integral exactly by direct integration and find the percentage error in each approximation.

### 4.2 Setting Up the Ordinates

With $a=0$, $b=6$ and $h=1$ we have $n=6$ strips and seven ordinates at $x=0,1,2,3,4,5,6$. The integrand is $f(x)=1/(1+x^{2})$.

| $x$ | $0$ | $1$ | $2$ | $3$ | $4$ | $5$ | $6$ |
|---|---|---|---|---|---|---|---|
| $y=f(x)$ | $1.00000$ | $0.50000$ | $0.20000$ | $0.10000$ | $0.05882$ | $0.03846$ | $0.02703$ |

### 4.3 Trapezoidal Rule

The formula is

$$
I_T=\frac{h}{2}\Bigl[y_0+2(y_1+y_2+y_3+y_4+y_5)+y_6\Bigr].
$$

First compute the inner sum:

$$
y_1+y_2+y_3+y_4+y_5=0.50000+0.20000+0.10000+0.05882+0.03846=0.89728.
$$

Then

$$
\begin{aligned}
I_T&=\frac{1}{2}\Bigl[1.00000+2(0.89728)+0.02703\Bigr]\\
&=\frac{1}{2}\Bigl[1.00000+1.79456+0.02703\Bigr]\\
&=\frac{1}{2}(2.82159)\\
&=1.41080.
\end{aligned}
$$

### 4.4 Simpson's One-Third Rule

The formula is

$$
I_S=\frac{h}{3}\Bigl[y_0+4(y_1+y_3+y_5)+2(y_2+y_4)+y_6\Bigr].
$$

The odd-indexed sum is

$$
y_1+y_3+y_5=0.50000+0.10000+0.03846=0.63846,
$$

and the even-indexed sum is

$$
y_2+y_4=0.20000+0.05882=0.25882.
$$

Therefore

$$
\begin{aligned}
I_S&=\frac{1}{3}\Bigl[1.00000+4(0.63846)+2(0.25882)+0.02703\Bigr]\\
&=\frac{1}{3}\Bigl[1.00000+2.55384+0.51764+0.02703\Bigr]\\
&=\frac{1}{3}(4.09851)\\
&=1.36617.
\end{aligned}
$$

### 4.5 Exact Value by Direct Integration

The antiderivative of $1/(1+x^{2})$ is $\arctan x$, so

$$
\begin{aligned}
I&=\Bigl[\arctan x\Bigr]_{0}^{6}\\
&=\arctan 6-\arctan 0\\
&=1.40565-0\\
&=1.40565.
\end{aligned}
$$

### 4.6 Percentage Errors

For the trapezoidal rule:

$$
\begin{aligned}
\text{percentage error}&=\frac{\lvert I-I_T\rvert}{\lvert I\rvert}\times 100\%\\
&=\frac{\lvert 1.40565-1.41080\rvert}{1.40565}\times 100\%\\
&=\frac{0.00515}{1.40565}\times 100\%\\
&\approx 0.37\%.
\end{aligned}
$$

For Simpson's rule:

$$
\begin{aligned}
\text{percentage error}&=\frac{\lvert I-I_S\rvert}{\lvert I\rvert}\times 100\%\\
&=\frac{\lvert 1.40565-1.36617\rvert}{1.40565}\times 100\%\\
&=\frac{0.03948}{1.40565}\times 100\%\\
&\approx 2.81\%.
\end{aligned}
$$

### 4.7 Reading the Result

The trapezoidal estimate is slightly too large, which is expected because the curve bends upwards over most of the interval. Simpson's estimate is smaller here because the curve changes shape sharply near $x=0$; with a finer step the Simpson value would improve much faster than the trapezoidal value. The important habit is to always compute the exact value where possible, so that the percentage error can be reported honestly.

### 4.8 A Second Exemplar: Gauss–Legendre Three-Point Formula

Evaluate

$$
I=\int_{-1}^{1}\frac{dx}{1+x^{2}}
$$

using the three-point Gauss–Legendre formula and find the percentage error.

The nodes are $x_1=-\sqrt{3/5}\approx -0.77460$, $x_2=0$ and $x_3=\sqrt{3/5}\approx 0.77460$. The weights are $5/9$, $8/9$ and $5/9$.

At the outer nodes,

$$
f(\pm 0.77460)=\frac{1}{1+0.60000}=\frac{1}{1.60000}=0.62500.
$$

At the centre node, $f(0)=1.00000$. Hence

$$
\begin{aligned}
I_A&=\frac{5}{9}(0.62500)+\frac{8}{9}(1.00000)+\frac{5}{9}(0.62500)\\
&=0.34722+0.88889+0.34722\\
&=1.58333.
\end{aligned}
$$

The exact value is

$$
\begin{aligned}
I&=\Bigl[\arctan x\Bigr]_{-1}^{1}\\
&=\frac{\pi}{4}-\left(-\frac{\pi}{4}\right)\\
&=\frac{\pi}{2}\\
&=1.57080.
\end{aligned}
$$

The percentage error is

$$
\begin{aligned}
\text{percentage error}&=\frac{\lvert 1.57080-1.58333\rvert}{1.57080}\times 100\%\\
&=\frac{0.01253}{1.57080}\times 100\%\\
&\approx 0.80\%.
\end{aligned}
$$

### 4.9 A Third Exemplar: Propagation of Error in a Quotient

Find the range of

$$
Q=\frac{1.265(10.21-7.57)}{47}
$$

if all numerical quantities are rounded off.

Each number is correct to the last digit shown, so each carries an absolute error of half a unit in that place: $\Delta(1.265)=0.0005$, $\Delta(10.21)=0.005$, $\Delta(7.57)=0.005$ and $\Delta(47)=0.5$.

The difference $10.21-7.57=2.64$ has error at most $0.005+0.005=0.010$, so it lies between $2.63$ and $2.65$.

The product $1.265\times 2.64$ has error at most

$$
\lvert 2.64\rvert(0.0005)+\lvert 1.265\rvert(0.010)=0.00132+0.01265=0.01397,
$$

so the numerator lies between $3.33960-0.01397=3.32563$ and $3.33960+0.01397=3.35357$.

For the quotient, the smallest value comes from the smallest numerator over the largest denominator, and the largest value from the largest numerator over the smallest denominator:

$$
\begin{aligned}
Q_{\min}&=\frac{3.32563}{47.5}=0.07001,\\
Q_{\max}&=\frac{3.35357}{46.5}=0.07212.
\end{aligned}
$$

Hence

$$
0.07001\le Q\le 0.07212.
$$

The central value is $3.33960/47=0.07106$, and the range shows that only the first two significant figures are trustworthy.

## 5. High-Yield Exam Takeaways & Common Pitfalls

### 5.1 High-Yield Takeaways

- The absolute error is $\lvert x-x_r\rvert$; the relative error divides this by $\lvert x\rvert$; the percentage error multiplies by $100$.
- A number correct to $n$ decimal places has absolute error at most $0.5\times 10^{-n}$. Quote this immediately when a question says "correct to $n$ decimal places".
- In addition and subtraction, absolute errors add. In multiplication and division, relative errors add.
- Subtraction of nearly equal numbers destroys accuracy; always mention this when asked about causes of error.
- For the trapezoidal rule, remember the pattern: half the step, first plus last, twice the middle.
- For Simpson's one-third rule, remember the pattern: one-third of the step, first plus last, four times the odd-indexed ordinates, two times the even-indexed ordinates. The number of strips must be even.
- For the Gauss–Legendre three-point formula, memorise the nodes $\pm\sqrt{3/5}$ and $0$ together with the weights $5/9$, $8/9$, $5/9$.
- Always finish an integration question by computing the exact value and then the percentage error; the marks are usually split between the approximation and the error.
- When asked for a range, use the smallest numerator with the largest denominator for the lower end, and the reverse for the upper end.

### 5.2 Common Pitfalls

- **Forgetting the absolute value.** The relative error is defined with $\lvert x\rvert$ in the denominator, so a negative exact value does not produce a negative error.
- **Using the wrong denominator.** The relative error divides by the exact value, not by the approximation.
- **Mixing up rounding and chopping.** Chopping always moves the number toward zero; rounding may move it either way.
- **Applying Simpson's rule with an odd number of strips.** The rule requires an even number of strips; if the data give an odd number, the trapezoidal rule must be used for the last strip.
- **Dropping the factor of one-half or one-third.** The trapezoidal rule uses $h/2$ and Simpson's rule uses $h/3$; swapping them is a frequent slip.
- **Reporting too many digits.** If the inputs are known to three significant figures, an answer quoted to eight figures is misleading. State the error bound and round accordingly.
- **Confusing inherent and accumulated error.** Inherent error is present in the data before computation; accumulated error is the total error built up during the computation.
- **Omitting the percentage error step.** Many past questions award separate marks for the exact value and for the percentage error, so both must be shown explicitly.
- **Ignoring loss of significance.** When a subtraction produces a very small result, warn that the relative error is large even though the absolute error looks small.