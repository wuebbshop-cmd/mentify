## 1. Core Concept Overview & Intuition

Numerical integration is the process of approximating the value of a definite integral

$$
I=\int_{a}^{b}f(x)\,dx
$$

when the antiderivative of $f$ is unknown, difficult to obtain, or when $f$ is known only through a table of sampled values. The definite integral represents a signed area under the curve $y=f(x)$ between $x=a$ and $x=b$; numerical methods replace this exact area by the area of simpler geometric figures (trapezoids, parabolas, or weighted point evaluations) that can be computed from finitely many ordinates.

The indefinite integral of a function is another function (or a class of functions), whereas the definite integral over a fixed interval is a number. The two are linked by the Fundamental Theorem of Calculus: the definite integral can be computed by first finding an antiderivative $F(x)$ of $f(x)$ and then evaluating $F(b)-F(a)$. When this route is unavailable, quadrature formulae are used.

Every numerical integration result carries an error. The error is the difference between the exact value and the approximation, and it is quantified in absolute, relative, or percentage form. The central practical question is therefore twofold: how to construct a good approximation, and how to measure and control the error it introduces.

The principal elementary rules are the trapezoidal rule (joining successive ordinates by straight lines to form trapezia) and Simpson's rule (approximating the curve over pairs of strips by a parabola). The trapezoidal rule generally over-estimates the area for a convex curve, and the error can be reduced by using smaller strips, that is, by increasing the number of subintervals.

## 2. Mathematical Formalization & Core Definitions

> **Definition (Round-off error).** Round-off errors arise because it is impossible to represent all real numbers exactly on a machine with finite memory. The process involves dropping decimal digits or significant figures, and may be carried out by chopping (truncation) or by symmetric rounding.

> **Definition (Absolute error).** Let $x_r$ be an approximate value of an exact number $x$. The absolute error is the absolute difference between the exact and approximate values:

> 

$$
> e_{\mathrm{abs}}=\lvert x-x_r\rvert.
>
$$

> If $\Delta x$ is an upper bound such that $e_{\mathrm{abs}}=\lvert x-x_r\rvert=\Delta x$, then $\Delta x$ is called the upper bound on the absolute error.

> **Definition (Relative error).** The relative error $e_r$ is the absolute error measured relative to the exact value:

> 

$$
> e_r=\frac{\lvert x-x_r\rvert}{\lvert x\rvert}.
>
$$

> **Definition (Propagated error).** The error in the result of an arithmetic operation arising from initial errors in the numbers used in that operation is called the propagated error. The total cumulative error at any step of a procedure is called the accumulated error.

> **Definition (Inherent error).** Inherent error is the error already present in the initial data of a problem (for example, in measured or rounded input quantities) before any arithmetic is performed.

### 2.1 Significant figures and the rounding bound

If a number is correct to $n$ decimal places, the maximum absolute error is

$$
e_{\mathrm{abs}}=0.5\times 10^{-n}.
$$

For example, if $x=8.35678$ is quoted to five decimal places, then $e_{\mathrm{abs}}\le 0.5\times 10^{-5}$.

### 2.2 Computation of absolute error from a rounded value

If $x=2.4$ is correct to one decimal place, the exact value lies in the interval

$$
2.35\le x\le 2.45,
$$

so that

$$
\lvert x-x_r\rvert\le 0.05=5.0\times 10^{-2}.
$$

If $x_r=-10.788$ is correct to three decimal places, the exact value lies in

$$
-10.7885\le x\le -10.7875,
$$

and the absolute error is

$$
e_{\mathrm{abs}}=0.0005=0.5\times 10^{-3}.
$$

### 2.3 The trapezoidal rule

Divide $[a,b]$ into $n$ equal strips of width

$$
h=\frac{b-a}{n},
$$

with ordinates $y_0,y_1,\dots,y_n$ at the equally spaced points $x_0=a,x_1,\dots,x_n=b$. Joining successive ordinates by straight lines produces trapezia, each of area $\tfrac{h}{2}(y_{i-1}+y_i)$. Summing gives the trapezoidal rule:

$$
\int_{a}^{b}f(x)\,dx\approx\frac{h}{2}\Bigl[y_0+2(y_1+y_2+\cdots+y_{n-1})+y_n\Bigr].
$$

The area obtained is generally an over-estimate for a convex curve, and the error is reduced by using smaller strips.

### 2.4 Simpson's rule

Simpson's rule estimates the area under a portion of a curve between $a$ and $b$ using three ordinates $y_0,y_1,y_2$. By translating the origin so that the middle ordinate sits at $x=0$, the curve over $[-h,h]$ is approximated by a parabola $y=ax^2+bx+c$, and the required area is

$$
\int_{-h}^{h}(ax^2+bx+c)\,dx.
$$

Carrying out the integration and expressing the result in terms of the three ordinates yields Simpson's rule:

$$
\int_{a}^{b}f(x)\,dx\approx\frac{h}{3}\Bigl[y_0+4y_1+y_2\Bigr],
$$

where $h$ is the width of each of the two equal strips. For a full interval divided into an even number of strips, the rule is applied pairwise and summed.

### 2.5 Error formulae

The maximum error in the trapezoidal rule satisfies a bound of the form

$$
\lvert E_T\rvert\le\frac{(b-a)}{12}h^{2}M_2,
$$

where $M_2$ is the maximum of $\lvert f''(x)\rvert$ on $[a,b]$.

The maximum error possible using Simpson's rule satisfies

$$
\lvert E_S\rvert\le\frac{(b-a)}{180}h^{4}M_4,
$$

where $M_4$ is the maximum of $\lvert f^{(iv)}(x)\rvert$ on $[a,b]$, with $f^{(iv)}$ denoting the fourth derivative.

### 2.6 Percentage error

The percentage error of an approximation $I_{\mathrm{approx}}$ relative to the exact value $I$ is

$$
\text{percentage error}=\frac{\lvert I-I_{\mathrm{approx}}\rvert}{\lvert I\rvert}\times 100\%.
$$

## 3. Key Theorems & Essential Results

The results collected in this section are the working tools of numerical integration. Each result states an approximation rule together with the accuracy behaviour that governs it, so that the reader can see not only how an integral is approximated but also how quickly the approximation improves when the computation is refined. The final result records how errors already present in the input data are carried through an arithmetic operation.

> **Result (Fundamental Theorem of Calculus).** If $f$ is continuous on $[a,b]$ and $F$ is any function whose derivative equals $f$ on that interval, then the definite integral of $f$ over $[a,b]$ is the change in $F$ across the interval, namely the value of $F$ at the upper limit minus the value of $F$ at the lower limit.

$$
\int_{a}^{b} f(x)\,dx = F(b)-F(a), \qquad F'(x)=f(x) \ \text{for all} \ x \in [a,b].
$$

This statement is the exact route to an integral. Every quadrature rule is an attempt to reproduce the same number using only finitely many sampled values of $f$, without ever knowing an antiderivative. Consequently a quadrature rule can never be exact in general, and the whole subject is concerned with making the discrepancy small and predictable.

> **Result (Composite trapezoidal rule).** Divide $[a,b]$ into $n$ equal strips of common width $h=(b-a)/n$ and let $y_i=f(x_i)$ at the equally spaced nodes $x_i=a+ih$, for $i=0,1,\dots,n$. Then the integral is approximated by

$$
\int_{a}^{b} f(x)\,dx \approx \frac{h}{2}\Bigl[y_0+2\bigl(y_1+y_2+\cdots+y_{n-1}\bigr)+y_n\Bigr].
$$

The structure of the rule is easy to remember: the two end ordinates carry weight one, every interior ordinate carries weight two, and the whole bracket is multiplied by half the strip width. The name comes from the fact that over each strip the integrand is replaced by the straight line joining the two neighbouring ordinates, so the area of that strip is replaced by the area of a trapezium of parallel sides $y_{i-1}$ and $y_i$ and perpendicular height $h$; adding the $n$ strip areas and collecting repeated ordinates produces the formula above. When $n=1$ the rule collapses to the single-strip form

$$
\int_{x_0}^{x_1} f(x)\,dx \approx \frac{h}{2}\bigl(y_0+y_1\bigr),
$$

where $h$ is the width of that one strip.

> **Result (Composite Simpson's rule).** Take $n$ even, put $h=(b-a)/n$, and let $y_i=f(x_i)$ at the equally spaced nodes $x_i=a+ih$, for $i=0,1,\dots,n$. Then the integral is approximated by

$$
\int_{a}^{b} f(x)\,dx \approx \frac{h}{3}\Bigl[y_0+4\bigl(y_1+y_3+\cdots+y_{n-1}\bigr)+2\bigl(y_2+y_4+\cdots+y_{n-2}\bigr)+y_n\Bigr].
$$

The multiplier pattern is $1,4,2,4,2,\dots,4,1$ read from left to right: the two end ordinates carry weight one, the ordinates at odd indices carry weight four, the ordinates at even interior indices carry weight two, and the bracket is multiplied by one third of the strip width. The rule is built by grouping the strips in pairs and replacing the integrand on each pair by the quadratic that passes through the three ordinates at its ends and its midpoint. On a single pair of equal strips, with ordinates $y_0,y_1,y_2$ and common strip width $h$, the rule reduces to

$$
\int_{x_0}^{x_2} f(x)\,dx \approx \frac{h}{3}\bigl[y_0+4y_1+y_2\bigr].
$$

Because the pairing of strips is essential, the number of strips must be even; if an odd number is required, one strip is handled by the trapezoidal rule and the remainder by Simpson's rule.

> **Result (Polynomial exactness).** The trapezoidal rule reproduces exactly the integral of every polynomial of degree at most one on each strip, and therefore on the whole interval whenever the strip widths are equal. Simpson's rule reproduces exactly the integral of every polynomial of degree at most three on each pair of strips.

Polynomial exactness is the reason the two rules behave so differently on smooth integrands. The trapezoidal rule makes no allowance for curvature, so its error on a single strip is governed by how strongly the integrand bends, that is by its second derivative. Simpson's rule matches the integrand through a quadratic, yet it integrates cubics exactly as well, which means its leading error term is governed by the fourth derivative. A function that is well approximated by low-degree polynomials is therefore integrated almost perfectly by Simpson's rule, while the same function may still leave a noticeable trapezoidal discrepancy.

> **Result (Order of accuracy).** For a twice continuously differentiable integrand, the truncation error of the composite trapezoidal rule is a fixed multiple of $h^2$ times the largest value of $\lvert f''\rvert$ on $[a,b]$. For a four times continuously differentiable integrand, the truncation error of the composite Simpson rule is a fixed multiple of $h^4$ times the largest value of $\lvert f^{(iv)}\rvert$ on $[a,b]$. In the notation of asymptotic order, with $h \to 0$,

$$
E_T(h) = \mathcal{O}(h^{2}), \qquad E_S(h) = \mathcal{O}(h^{4}).
$$

The practical content of the result is a refinement ratio. Halving the strip width multiplies the trapezoidal truncation error by roughly one quarter, and multiplies the Simpson truncation error by roughly one sixteenth. Equivalently, doubling the number of strips improves the trapezoidal approximation by about two extra correct decimal places for every factor of one hundred in the strip count, whereas Simpson's rule gains about four correct decimal places for the same effort. This is why Simpson's rule normally reaches a given tolerance with far fewer ordinates than the trapezoidal rule, at the price of requiring the integrand to be smooth enough for the fourth derivative to be controlled.

A word of caution belongs with this result. Reducing $h$ reduces truncation error but increases the number of ordinates, hence the number of arithmetic operations, hence the accumulated round-off error and the cost of evaluation. For very small $h$ the round-off contribution can dominate and the computed value stops improving or even deteriorates. The best choice of $h$ is therefore a compromise between truncation error, which decreases as $h$ shrinks, and round-off error, which grows as $h$ shrinks.

> **Result (Propagation of errors in arithmetic).** Let $x$ and $y$ be exact numbers and let $x^{*}$ and $y^{*}$ be approximations to them with initial errors $\varepsilon$ and $\eta$ respectively, so that $x=x^{*}+\varepsilon$ and $y=y^{*}+\eta$. For an exact operation $\omega$ and its computational version $\omega^{*}$, the total discrepancy splits into two parts,

$$
x\,\omega\,y - x^{*}\,\omega^{*}\,y^{*}
= \bigl(x\,\omega\,y - x^{*}\,\omega\,y^{*}\bigr) + \bigl(x^{*}\,\omega\,y^{*} - x^{*}\,\omega^{*}\,y^{*}\bigr),
$$

where the first bracket is the propagated error, that is the part of the discrepancy caused by the initial errors $\varepsilon$ and $\eta$ being carried through the operation, and the second bracket is the generated error, that is the part introduced by performing the operation itself in finite arithmetic. The two together constitute the accumulated error at that stage of the computation.

The distinction matters in quadrature because a quadrature formula is a long chain of additions and multiplications. Each ordinate $y_i$ is itself an approximation obtained from the integrand, so it carries an initial error; the weighted sum then propagates those errors and adds fresh rounding at every step. The analysis of a composite rule therefore has two separate strands, the truncation error of the formula and the accumulated round-off of its evaluation, and a reliable numerical answer must control both.

## 4. Worked Exemplar Problem with Step-by-Step Solution

### Problem

Evaluate

$$
I=\int_{0}^{6}\frac{dx}{1+x^{2}}
$$

using (i) the trapezoidal rule and (ii) Simpson's one-third rule with $h=1$. Then evaluate the exact integral by direct integration correct to five decimal places and find the percentage error in each approximation.

### Step 1: Tabulate the ordinates

With $h=1$ and $x=0,1,2,3,4,5,6$, the integrand is $f(x)=\dfrac{1}{1+x^{2}}$:

| $x$ | $0$ | $1$ | $2$ | $3$ | $4$ | $5$ | $6$ |
|---|---|---|---|---|---|---|---|
| $f(x)$ | $1.00000$ | $0.50000$ | $0.20000$ | $0.10000$ | $0.05882$ | $0.03846$ | $0.02703$ |

### Step 2: Trapezoidal rule

$$
\begin{aligned}
I_T&=\frac{h}{2}\Bigl[y_0+2(y_1+y_2+y_3+y_4+y_5)+y_6\Bigr]\\
&=\frac{1}{2}\Bigl[1.00000+2(0.50000+0.20000+0.10000+0.05882+0.03846)+0.02703\Bigr]\\
&=\frac{1}{2}\Bigl[1.00000+2(0.89728)+0.02703\Bigr]\\
&=\frac{1}{2}\bigl[2.82159\bigr]\\
&=1.41080.
\end{aligned}
$$

### Step 3: Simpson's one-third rule

With six strips (an even number), apply the rule pairwise:

$$
\begin{aligned}
I_S&=\frac{h}{3}\Bigl[(y_0+y_6)+4(y_1+y_3+y_5)+2(y_2+y_4)\Bigr]\\
&=\frac{1}{3}\Bigl[(1.00000+0.02703)+4(0.50000+0.10000+0.03846)+2(0.20000+0.05882)\Bigr]\\
&=\frac{1}{3}\Bigl[1.02703+4(0.63846)+2(0.25882)\Bigr]\\
&=\frac{1}{3}\Bigl[1.02703+2.55384+0.51764\Bigr]\\
&=\frac{1}{3}\bigl[4.09851\bigr]\\
&=1.36617.
\end{aligned}
$$

### Step 4: Exact value by direct integration

Since $\dfrac{d}{dx}\arctan x=\dfrac{1}{1+x^{2}}$,

$$
\begin{aligned}
I&=\int_{0}^{6}\frac{dx}{1+x^{2}}\\
&=\bigl[\arctan x\bigr]_{0}^{6}\\
&=\arctan 6-\arctan 0\\
&=1.40565-0\\
&=1.40565.
\end{aligned}
$$

### Step 5: Percentage errors

For the trapezoidal rule:

$$
\begin{aligned}
\text{percentage error}&=\frac{\lvert I-I_T\rvert}{\lvert I\rvert}\times 100\%\\
&=\frac{\lvert 1.40565-1.41080\rvert}{1.40565}\times 100\%\\
&=\frac{0.00515}{1.40565}\times 100\%\\
&\approx 0.366\%.
\end{aligned}
$$

For Simpson's rule:

$$
\begin{aligned}
\text{percentage error}&=\frac{\lvert I-I_S\rvert}{\lvert I\rvert}\times 100\%\\
&=\frac{\lvert 1.40565-1.36617\rvert}{1.40565}\times 100\%\\
&=\frac{0.03948}{1.40565}\times 100\%\\
&\approx 2.809\%.
\end{aligned}
$$

### Step 6: Interpretation

The trapezoidal approximation exceeds the exact value, consistent with the over-estimate expected for a convex decreasing curve. Simpson's rule is markedly more accurate on smooth integrands in general, but on this interval the integrand changes curvature rapidly near $x=0$, so the coarse step $h=1$ produces a larger Simpson discrepancy; refining $h$ reduces both errors, with the Simpson error falling faster because it is governed by $h^{4}$.

### Additional exemplar: range of a rounded expression

To obtain the range within which

$$
\frac{1.265(10.21-7.57)}{47}
$$

lies when all quantities are rounded off, note that a number quoted to $k$ decimal places has absolute error at most $0.5\times 10^{-k}$. Thus $1.265$ carries error $\pm 0.0005$, the quantities $10.21$ and $7.57$ carry error $\pm 0.005$, and $47$ carries error $\pm 0.5$. The propagated error of the product and quotient is then obtained by combining these initial errors through the arithmetic operations, giving the interval of possible exact values.

## 5. High-Yield Exam Takeaways & Common Pitfalls

- Always state the exact value obtained by direct integration before computing any percentage error; the percentage error is meaningless without the exact reference value.
- For the trapezoidal rule, the end ordinates are counted once and all interior ordinates are doubled; for Simpson's rule, ordinates are weighted $1,4,2,4,2,\dots,4,1$ and the whole sum is multiplied by $h/3$.
- Simpson's one-third rule requires an even number of strips; if the tabulation gives an odd number, the rule cannot be applied directly across the whole interval.
- The trapezoidal rule over-estimates the area for a convex curve; the error is reduced by using smaller strips, that is, a larger $n$.
- Distinguish clearly between inherent error (present in the initial data), propagated error (arising in the result of an operation from initial errors), generated error (introduced by the operation itself), and accumulated error (the running total).
- Absolute error is $\lvert x-x_r\rvert$; relative error divides this by $\lvert x\rvert$; percentage error multiplies the relative error by $100\%$. A number correct to $n$ decimal places has absolute error at most $0.5\times 10^{-n}$.
- When a quantity is quoted to $k$ decimal places, its true value lies in a symmetric interval of half-width $0.5\times 10^{-k}$; use these intervals to bound the exact value of a compound expression.
- Do not confuse the strip width $h=(b-a)/n$ with the number of strips $n$; the error bounds depend on $h^{2}$ for the trapezoidal rule and $h^{4}$ for Simpson's rule.
- Quote final numerical answers to the precision demanded by the question (for example, five decimal places) and carry full precision through intermediate steps to avoid unnecessary round-off contamination.