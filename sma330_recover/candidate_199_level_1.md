## 1. Foundational Concepts, Definitions, and Axioms

### Everyday picture before notation
Imagine estimating the amount of water in a shallow pond by laying a grid over a map. The shoreline is curved, so no small set of rectangles follows it perfectly. Narrower grid cells give a more faithful estimate, while a different shape, such as a sloping-sided strip, can follow the boundary better with fewer measurements. Numerical integration uses the same idea for the area under a curve: replace a curved shape with simple pieces whose areas can be calculated from sampled heights.

This picture has limits. The mathematical integral is a signed accumulated quantity, not always a positive geometric area, and the sample values may come from a formula or a table. Still, the map analogy explains the three recurring questions: where to sample, how to combine the samples, and how to judge the result.

A definite integral is the exact total associated with a function over an interval. If an antiderivative is available, direct integration and endpoint substitution may give the exact value. Numerical quadrature is useful when that route is unavailable, inconvenient, or when only tabulated ordinates are supplied. A rule replaces the integral with a finite weighted sum of function values. The trapezoidal rule joins neighboring samples by straight segments; Simpson's one-third rule uses a parabolic fit across pairs of equal strips; Gaussian quadrature chooses nodes and weights for high polynomial exactness.

The course sequence builds these ideas rather than treating one rule as a universal answer. Lesson 8 establishes the elementary trapezoidal and Simpson rules and error comparisons. Lesson 9 refines composite rules and combines refinements with Romberg extrapolation. Lesson 10 introduces quadrature with deliberately selected nodes. When a direct value is known, compare the approximation with it; when it is not, state the rule, nodes, weights, step size, and any refinement evidence instead of claiming an exact answer.

## 2. Theorems, Lemmas, and Analytical Properties

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

## 3. Formal Proofs, Derivations, and Methods

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

## 4. Representative Worked Examples and Solutions

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

### 4.1 A small table compared by two basic rules

Estimate the area under $f(x)=x^2$ from $0$ to $2$ using two equal strips. The nodes are $0,1,2$ and the heights are $0,1,4$. The exact integral is $8/3$, but a numerical rule needs only the listed heights.

The trapezoidal rule joins each adjacent pair of points with a straight segment. Each segment creates a trapezium of width one, so the estimate is

$$
T_2=\frac{1}{2}\bigl[0+2(1)+4\bigr]=3.
$$

The result is above $8/3$. That direction is expected here because $x^2$ bends upward and the chords lie above the curve. The rule has replaced a curved boundary by straight sides, so the geometric construction explains the sign of the discrepancy.

Simpson’s one-third rule uses the same three heights but fits a parabola through them:

$$
S_2=\frac{1}{3}\bigl[0+4(1)+4\bigr]=\frac{8}{3}.
$$

It is exact in this example because the function itself is a quadratic. This does not mean Simpson’s rule is exact for every function. It does mean that a rule that reproduces low-degree polynomials exactly can outperform a straight-line approximation when the integrand is smooth and well represented by such a polynomial.

The comparison also guards against a common formula error. In the one-panel Simpson expression, the distance between the first and last nodes is $2h$; the coefficient is $h/3$ where $h$ is the width of one strip. Using the full interval width in place of $h$ doubles the result. Write down the nodes and identify the strip width before substituting the ordinates.

### 4.2 What happens when the mesh is refined

For the same function on $[0,2]$, use four strips of width $h=0.5$. The trapezoidal values at the nodes are $0,0.25,1,2.25,4$. The composite formula gives

$$
T_4=\frac{0.5}{2}\bigl[0+2(0.25+1+2.25)+4\bigr]=2.75.
$$

The exact integral remains $8/3\approx2.6667$, so the error has fallen from about $0.3333$ to about $0.0833$, one quarter of its earlier size. This matches the leading $h^2$ behavior when the strip width is halved. It is an approximate scaling law for truncation error under the smoothness assumptions, not a promise that every calculator output will improve by exactly four after rounding or noisy data are included.

Simpson’s rule with four strips applies the one-third rule to two adjacent pairs and combines the panel contributions. It integrates every cubic polynomial exactly, and in this particular case it remains exact because $x^2$ has lower degree. For a function that is not a cubic or lower, Simpson’s error normally decreases more quickly with refinement because its leading term is proportional to $h^4$.

“More strips” also means more function evaluations, unless a nested refinement reuses previous nodes. A fair comparison of two methods therefore considers both the accuracy target and the cost of obtaining new ordinates. If values are already supplied in a table, the available spacing may determine which composite formula can be applied without interpolation.

### 4.3 A smooth function that is not integrated exactly

Use Simpson’s one-third rule on $f(x)=x^4$ from $0$ to $1$, with two strips of width $h=0.5$. The ordinates are $0$, $1/16$, and $1$. Simpson’s estimate is

$$
S_2=\frac{0.5}{3}\left[0+4\left(\frac{1}{16}\right)+1\right]
=\frac{5}{24}\approx0.20833.
$$

The exact integral is $1/5=0.2$, so the error is $1/120\approx0.00833$. The rule is accurate but not exact because a quartic is one degree beyond the class it integrates exactly. Halving the strip width on a composite Simpson calculation reduces the leading error by approximately a factor of sixteen when the fourth derivative is bounded and the asymptotic error term dominates.

The calculation shows why the words “polynomial exactness” must be used carefully. Simpson’s formula is not a general antiderivative; its exactness on polynomials of degree at most three is a property of the weighted sum. A quartic introduces a nonzero fourth-derivative contribution. If an exact integral is available, compare the approximation directly and compute an absolute or percentage error. If it is unavailable, state the smoothness conditions and error estimate instead of inventing an exact answer.

### 4.4 Reading a composite Simpson weight pattern

For six strips, there are seven ordinates $y_0,\ldots,y_6$. The composite Simpson weights are

$$
1,\ 4,\ 2,\ 4,\ 2,\ 4,\ 1.
$$

The endpoints appear once, odd interior indices have weight four, and even interior indices have weight two. The entire sum is multiplied by $h/3$. The pattern results from adding three pairwise Simpson panels: every shared boundary ordinate is counted in two neighboring panels, while an odd midpoint belongs to one pair and receives its factor four.

A reliable hand calculation writes the coefficients under the data row before adding. For example, with $y_0=1,y_1=2,\ldots,y_6=7$, the bracket is $1+4(2)+2(3)+4(4)+2(5)+4(6)+7=70$. The approximation is $70h/3$. This bookkeeping check prevents using the trapezoidal pattern in a Simpson expression or assigning coefficient two to the wrong index.

The number of strips must be even because Simpson’s rule needs pairs of equal-width strips. If an odd count is supplied, do not silently apply the rule to the entire interval. The course may specify a mixed approach for an unmatched strip; otherwise explain that the requested composite one-third rule does not directly cover the table as given.

### 4.5 Exact answer, error bound, and convergence evidence

There are three different statements that can be made about a computed integral. If an antiderivative provides the exact value, the actual error is the difference between that value and the quadrature result. If a derivative bound is known, a theorem can give a guaranteed maximum error. If neither is known, agreement between successive refinements is evidence of stabilization, but it is not automatically a proof that the answer lies within a specified tolerance.

For example, the trapezoidal estimate may change from $2.75$ to $2.6875$ as the number of strips doubles. The smaller change suggests convergence toward a limiting value. It does not by itself prove the true integral is within that difference of the newest estimate, because both approximations could share bias. The smoothness assumptions and error formula supply the theoretical explanation for why the change is informative.

When reporting a result, say which kind of evidence is available. A phrase such as “the numerical estimates stabilize to four decimal places” is an empirical observation. “The error is at most…” requires a valid error bound and the relevant derivative maximum. “The exact error is…” requires the exact integral value. These statements should not be used interchangeably.

Round only after the weighted sum has been computed. Premature rounding of every ordinate can create extra error that is not part of the quadrature truncation formula. If the ordinates themselves are approximate, mention that data uncertainty is another source and may dominate the improvement from a finer mesh.

### 4.6 A practical checklist for a numerical integral

First identify the interval and the available ordinates. Compute $h=(b-a)/n$ and check that the spacing is actually uniform if the composite formula assumes equal strips. Next select a rule appropriate to the data and verify any parity requirement. Write the coefficient pattern, substitute the ordinates, and preserve enough digits during summation.

Then interpret the answer. Check whether the sign and rough magnitude make sense; for a nonnegative integrand, a negative result usually signals an arithmetic or sign mistake. If curvature is known, use it only as a qualitative guide unless the precise hypotheses of an error theorem are met. If an exact integral or a derivative bound is available, use it to assess accuracy. Otherwise compare refinements but label the comparison as evidence rather than a guarantee.

The final line should include units when the integrand and variable carry units, state the method and number of strips, and give the requested precision. A numerical value without its step size, rule, or error interpretation is difficult to reproduce and may hide a mistaken assumption.

### 4.9 A refinement-and-extrapolation example

Consider approximating $\int_0^1 e^x\,dx=e-1\approx1.71828$. The one-strip trapezoidal estimate uses the endpoint values:

$$
T_1=\frac{1}{2}(1+e)\approx1.85914.
$$

With two strips, the midpoint value is $e^{1/2}$, so

$$
T_2=\frac{1}{4}\bigl[1+2e^{1/2}+e\bigr]\approx1.75393.
$$

The refined estimate is closer to the exact integral. If the smooth trapezoidal error has leading form $T(h)=I+Ch^2+\cdots$, then $T(h/2)=I+Ch^2/4+\cdots$. The weighted combination

$$
R=\frac{4T(h/2)-T(h)}{3}
$$

cancels the leading $h^2$ term. Substituting these two trapezoidal estimates gives approximately $1.71886$, much closer to $e-1$. The extrapolated result is not automatically exact; it relies on a smooth error expansion and sufficiently fine grids.

The method uses the same endpoint and midpoint data rather than guessing a new rule. It is called extrapolation because the two error-contaminated estimates are combined to infer the limiting value at zero step size. The name does not mean that we are estimating outside the interval of integration; that is a different use of extrapolation.

### 4.10 Mapping Gaussian nodes to an ordinary interval

Gaussian rules are often tabulated on the standard interval $[-1,1]$. To use one on $[a,b]$, set $x=m+dt$, with midpoint $m=(a+b)/2$ and half-width $d=(b-a)/2$. Then $dx=d\,dt$ and

$$
\int_a^b f(x)\,dx=d\int_{-1}^{1}f(m+dt)\,dt.
$$

For the three-point Gauss–Legendre rule, the nodes in $t$ are $-\sqrt{3/5},0,\sqrt{3/5}$ and the weights are $5/9,8/9,5/9$. The transformed formula therefore evaluates the original function at three points inside $[a,b]$ and multiplies the weighted sum by $d$. Omitting this scale factor gives a result with the wrong interval size.

On the interval $[0,1]$, the midpoint is $1/2$ and the half-width is $1/2$. The three original-variable nodes are $1/2-\frac12\sqrt{3/5}$, $1/2$, and $1/2+\frac12\sqrt{3/5}$. They are not equally spaced in the same pattern as a uniform grid, so an equally spaced table does not automatically provide the needed values. Gaussian quadrature is most useful when the function can be evaluated at the selected nodes.

### 4.11 Choosing a rule from the information available

When values are supplied at equally spaced points, composite trapezoidal or Simpson formulas use those observations directly. Simpson’s one-third rule needs an even number of strips. Romberg integration needs a sequence of nested trapezoidal refinements, so the function must be evaluable at additional midpoint nodes or the needed values must already exist. Gaussian quadrature chooses special nodes and is useful when those evaluations can be obtained.

The choice also depends on the function. A smooth curve with bounded higher derivatives supports the standard error-order discussion. A sharp corner, discontinuity, or endpoint singularity can weaken the expected behavior. If the interval contains a known feature, splitting the interval there may make the local approximation more credible. If only noisy tabular observations are available, a high-order formula may not help because data error can dominate.

The method should therefore be named together with its requirements: “composite Simpson with six equal strips,” “Romberg extrapolation from nested trapezoidal estimates,” or “three-point Gauss–Legendre after interval mapping.” This makes it possible to check the node pattern, strip count, scale factor, and error claim.

### 4.12 Reading accuracy evidence carefully

An exact comparison is the strongest simple check when the integral can be evaluated directly. If the exact value is known, compute absolute error and, when meaningful, percentage error. If a derivative maximum is supplied, use the relevant theorem to state an upper bound. If neither is available, compare successive refinements and describe the observed stabilization without calling it a proof.

For example, if two successive diagonal entries in a Romberg table differ by $0.00002$, one may report that the sequence has stabilized to the shown precision under that refinement. This does not certify that the true integral is within $0.00002$; both approximations may share a residual bias. The asymptotic error model and smoothness assumptions explain why the comparison is informative but do not erase those conditions.

Keep approximation error separate from arithmetic and data error. A table of rounded ordinates introduces uncertainty into the weighted sum. Repeated refinement may reduce the quadrature truncation term while leaving the data uncertainty unchanged. Reporting many decimal places is not a substitute for tracking these sources.

### 4.13 Signed area and cancellation

A definite integral is signed. If the curve lies below the horizontal axis, its contribution is negative, even though a drawn geometric area would be positive. Consider $f(x)=1-2x$ on $[0,1]$. The endpoint values are $1$ and $-1$, so the single trapezoidal estimate is zero. Direct integration also gives zero because the positive and negative contributions cancel.

When the exact integral is zero, relative error and percentage error relative to that exact value are undefined. The absolute error remains meaningful. A numerical method might return a small nonzero number due to rounding or an asymmetric grid; report the absolute discrepancy instead of dividing by zero.

Cancellation can also occur in a nonzero integral. A small final integral may be the difference of two large signed contributions. In that case, relative error can be large even when each panel is approximated well in absolute terms. Inspect the sign pattern of the ordinates and do not assume that “area under the curve” is always positive.

### 4.14 Uncertain ordinates in a composite formula

Suppose the equally spaced ordinates have individual errors $\eta_i$. The trapezoidal estimate is a weighted sum, so its data-induced change is the same weighted sum of those errors. Interior ordinates receive twice the endpoint weight. A coarse bound is obtained by multiplying each maximum ordinate error by the magnitude of its weight and adding:

$$
|\Delta T|\le\frac{h}{2}
\left(|\eta_0|+2\sum_{i=1}^{n-1}|\eta_i|+|\eta_n|\right).
$$

This contribution is different from the smooth-function truncation error. A derivative-based theorem measures the effect of replacing the curve by a quadrature formula; the weighted uncertainty formula measures the effect of imperfect supplied or computed heights. Refining the mesh may reduce one contribution while leaving the other unchanged.

For Simpson’s rule, use its own weights $1,4,2,\ldots,4,1$ and multiplier $h/3$. A midpoint ordinate with weight four contributes more strongly to data uncertainty than an endpoint with weight one. If the table entries are rounded, this effect should be acknowledged before claiming that a higher-order rule guarantees greater accuracy.

### 4.15 Choosing between a proof and a practical check

If $f$ is twice differentiable and a maximum for $|f''|$ is known, the trapezoidal error bound gives a guaranteed ceiling. Simpson’s theorem instead requires four derivatives and a bound on $|f^{(4)}|$. These hypotheses are stronger than simply knowing several function values. If those derivative facts are not supplied or cannot be proved, do not manufacture a guaranteed error from a table alone.

A practical alternative is to calculate with a finer mesh and compare the results. This is a useful diagnostic because the leading error orders predict a characteristic change under refinement. However, the comparison is empirical: two estimates can agree because the remaining error is small, or because they share a bias. State which evidence supports the chosen precision.

In the final answer, separate the estimate from the confidence statement. For example, “the composite Simpson estimate is $I_h$, using $n$ equal strips; the next refinement changes the value by $\delta$” reports the computation. “The error is at most $M$” is a stronger statement and requires a valid theorem and derivative bound.

### 4.16 A method-selection summary

Use a single trapezoid for a simple geometric baseline or when only two endpoints are known. Use composite trapezoidal integration when equally spaced data are supplied and a transparent rule is desired. Use composite Simpson’s one-third rule when the nodes are equally spaced and the strip count is even. Use Romberg when nested trapezoidal refinements are available and the smooth error expansion is plausible. Use Gaussian quadrature when the selected nodes can be evaluated and fewer function calls are valuable.

The choice is constrained by data, not just by formal order. A table with fixed equally spaced observations may not contain the nonuniform Gauss nodes. A nonsmooth integrand may not satisfy the standard order assumptions. A noisy table can make a fine grid less useful. State what is known, select a compatible rule, and identify any limitation instead of announcing a universal best method.

## 5. Mathematical Extensions, Limits, and Common Errors

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

### From elementary rules to the full lesson sequence
If a single trapezoid or one Simpson panel is not sufficiently accurate, divide the interval into equal strips and sum the local contributions. The composite trapezoidal rule uses each interior ordinate twice in its endpoint-pair sum, while composite Simpson weights alternating interior ordinates by 4 and 2 and requires an even strip count. Refinement means halving the strip width and recomputing, not merely adding extra digits to the same estimate.

Romberg integration organizes a sequence of trapezoidal refinements in a triangle. Its key idea is that the leading trapezoidal error changes predictably as the step is halved, so a weighted combination cancels that leading error. Gaussian quadrature takes another route: on the standard interval it uses the three nodes $-\sqrt{3/5},0,\sqrt{3/5}$ with weights $5/9,8/9,5/9$; the transformed rule on a general interval also includes the interval scale. These methods are not interchangeable labels: composite/Romberg uses a refining grid, while Gaussian uses selected nodes. A careful answer tells which method was used and preserves its assumptions.

### One curve, two area estimates

Let the curve be \(y=x^2\) from \(x=0\) to \(x=2\). The exact area is \(\int_0^2x^2\,dx=8/3\), which is useful here as a check. Use two equal strips, each of width \(h=1\). The sampled heights are \(y_0=0\), \(y_1=1\), and \(y_2=4\).

For the trapezoidal rule, each strip is replaced by a straight-edged trapezium. The combined formula gives

$$
T=\frac{1}{2}[y_0+2y_1+y_2]
=\frac12[0+2(1)+4]=3.
$$

For Simpson's one-third rule, the same three heights determine a parabolic arc over the two strips:

$$
S=\frac{1}{3}[y_0+4y_1+y_2]
=\frac13[0+4(1)+4]=\frac83.
$$

The trapezoidal estimate is \(1/3\) greater than the exact integral, while Simpson's result is exact for this quadratic example. This is not a universal promise that Simpson's result is always exact; it reflects the fact that the fitted parabola is the curve itself in this particular case. The example also shows why the methods use different weights: the middle ordinate has a different role in a parabolic fit than in two neighbouring straight-line trapezia.

### A sign check and a practical decision

Numerical integration measures signed area. If the curve lies below the horizontal axis, its contribution is negative, even though a geometric picture of “area” may suggest a positive number. If positive and negative portions cancel, the net integral can be close to zero while each portion is large. In that case a relative error based on the small net result can look large; report absolute error as well and explain the cancellation.

Before choosing a rule, ask what information is available. If an antiderivative is accessible, the Fundamental Theorem of Calculus gives an exact route in principle. If only a table of ordinates is supplied, use a composite rule that matches the spacing and panel requirements. The trapezoidal rule accepts any positive number of equal strips. Composite Simpson's one-third rule groups strips in pairs and therefore requires an even strip count. Check that the endpoints and every required interior ordinate are included exactly once with the prescribed weights.

Finally, compare an approximation with any available exact value or independent method, but do not call agreement proof of exactness. Report the rule, the strip width, the computed sum, and a sensible precision. If no exact result is available, the curvature and the method's error behaviour explain why refinement may improve the answer; an unexplained extra decimal place does not.

### When positive and negative areas balance

Take the simple line \(f(x)=x-1\) on \([0,2]\). It is below the horizontal axis from \(0\) to \(1\), and above the axis from \(1\) to \(2\). The signed integral is

$$
\int_0^2(x-1)\,dx
=\left[\frac{x^2}{2}-x\right]_0^2=0.
$$

The two geometric pieces each have area \(1/2\), but one is negative in the signed integral and the other is positive. A numerical rule applied symmetrically to the line can also return zero. That does not mean there was no area under the curve; it means the signed contributions cancel. Relative error with the exact integral in the denominator is undefined here, so absolute error or separate positive and negative contributions are more informative.

This example gives two practical checks. First, sketch or reason about the sign of the ordinates before summing weights; a negative ordinate must remain negative. Second, do not interpret a small net integral as evidence that the curve itself was small throughout the interval. When cancellation is strong, report the sign and the scale of the separate contributions where the problem asks for accuracy.

### From geometry to a justified final value

For a curved graph, the trapezoidal rule uses straight segments and Simpson's rule uses a quadratic over pairs of equal strips. The approximation may lie above or below the true curve depending on its curvature and the rule; the direction should not be guessed from one example and applied to every function. A numerical answer becomes more convincing when each part is traceable: list the strip width, record the ordinates, apply the weights in their proper order, check the endpoints, and only then round.

If a result is stated to a certain number of decimal places, compare the estimated error or available error bound with half a unit in the last displayed place. If that uncertainty is larger, reduce the number of displayed digits or refine the calculation. If only a table is supplied, use the data as given and avoid inventing additional ordinates. In all cases the method's assumptions, such as equal spacing and an even Simpson strip count, are part of the solution rather than optional notes.
