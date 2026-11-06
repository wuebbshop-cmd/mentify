## 1. Core Concept Overview & Intuition

Numerical integration is the process of approximating the value of a definite integral

$$
I=\int_{a}^{b}f(x)\,dx
$$

when the antiderivative of $f$ is either unknown, difficult to obtain, or when $f$ is known only through a table of sampled values. The definite integral over a fixed interval $[a,b]$ is a number, whereas the indefinite integral of a function is another function or a class of functions. The two are linked by the Fundamental Theorem of Calculus, which states that the definite integral can be computed by first finding an antiderivative $F(x)$ of $f(x)$ and then evaluating $F(b)-F(a)$. When this route is unavailable, we replace the integrand by a simpler function (a straight line or a parabola) whose integral we can compute exactly.

The central geometric idea is to divide the interval $[a,b]$ into $n$ equal strips of width $h$, evaluate the integrand at the resulting mesh points, and combine these ordinates with fixed weights. The trapezoidal rule joins consecutive ordinates by straight lines, forming trapezia whose areas are summed. Simpson's rule instead passes a parabola through three consecutive ordinates, capturing curvature and therefore producing a markedly more accurate estimate for the same number of ordinates.

Two practical facts govern all the methods in this topic. First, the accuracy of a quadrature rule is limited by the step size $h$: reducing $h$ reduces the truncation error. Second, every ordinate $f(x_i)$ is itself a computed quantity carrying round-off error, and these initial errors propagate into the final weighted sum. Understanding both the truncation error of the rule and the propagated error from the data is essential to judging whether a computed integral can be trusted.

## 2. Mathematical Formalization & Core Definitions

> **Definition (Definite and indefinite integrals).** The indefinite integral of a function is another function or a class of functions. The definite integral of a function over a fixed interval is a number.

> **Definition (Trapezoidal rule).** Let $f$ be continuous on $[a,b]$ and let the interval be divided into $n$ equal strips of width $h=\dfrac{b-a}{n}$ with ordinates $y_0,y_1,\dots,y_n$ at the mesh points $x_i=a+ih$. The trapezoidal estimate is

> 

$$
> \int_{a}^{b}f(x)\,dx\approx \frac{h}{2}\Bigl(y_0+2y_1+2y_2+\cdots+2y_{n-1}+y_n\Bigr).
>
$$

The construction uses the area of a trapezium, $\text{Area}=\tfrac{1}{2}(a+b)h$, where $(a+b)$ denotes the sum of the parallel sides. Each interior ordinate is shared by two adjacent trapezia and therefore receives weight $2$, while the two end ordinates receive weight $1$.

> **Definition (Simpson's rule).** The Simpson's rule gives a formula for an estimate of the area under the portion of a curve between $a$ and $b$ in terms of three ordinates $y_0$, $y_1$ and $y_2$. By translation the interval is taken as $[-h,h]$ and the integrand is approximated by a parabola $ax^2+bx+c$, so that the required area is

> 

$$
> \int_{-h}^{h}\left(ax^2+bx+c\right)dx.
>
$$

Carrying out this integration and expressing the result in terms of the three ordinates yields the familiar composite form.

> **Definition (Composite Simpson's rule).** For an even number $n$ of strips of width $h=\dfrac{b-a}{n}$,

> 

$$
> \int_{a}^{b}f(x)\,dx\approx \frac{h}{3}\Bigl(y_0+4y_1+2y_2+4y_3+\cdots+4y_{n-1}+y_n\Bigr),
>
$$

> with weight $4$ on odd-indexed ordinates and weight $2$ on even-indexed interior ordinates.

> **Definition (Propagated error).** The error in the result of an arithmetic operation arising due to initial errors in the numbers used in that operation is called the propagated error. The total cumulative error at any step in the procedure is called the accumulated error.

> **Definition (Absolute error).** If $x_r$ is an approximate number to an exact number $x$, the absolute error is

> 

$$
> e_{\text{abs}}=\lvert x-x_r\rvert.
>
$$

> **Definition (Relative error).** The relative error is the absolute error measured in units of the exact quantity,

> 

$$
> e_r=\frac{\lvert x-x_r\rvert}{\lvert x\rvert}.
>
$$

> **Definition (Error bound from significant figures).** If a number is correct to $n$ decimal places, then the maximum absolute error satisfies

> 

$$
> e_{\text{abs}}\le 0.5\times 10^{-n}.
>
$$

Round-off errors arise because it is impossible to represent all real numbers exactly on a machine with finite memory; the process involves dropping decimal points or significant figures, and may be done by chopping (truncation) or by symmetric rounding.

## 3. Key Theorems & Essential Results

> **Result (Trapezoidal rule error).** The error in the trapezoidal rule is controlled by the second derivative of the integrand and the square of the step size, so that halving $h$ reduces the error by roughly a factor of four. The trapezoidal estimate of a convex integrand is an over-estimate, and the error can be reduced by using smaller strips.

> **Result (Error in Simpson's rule).** The maximum error possible using Simpson's rule satisfies a bound of the form

> 

$$
> \lvert E_S\rvert \le \frac{(b-a)}{180}h^{4}M,
>
$$

> where $M$ is the maximum of $\lvert f^{(iv)}\rvert$ on $[a,b]$ and $f^{(iv)}$ is the fourth derivative. Because the bound involves $h^4$, Simpson's rule is far more accurate than the trapezoidal rule for the same step size.

> **Result (Propagation in arithmetic operations).** Let $x$ and $y$ be exact numbers and let $x^{*}$ and $y^{*}$ be approximations with initial errors $\varepsilon$ and $\eta$ respectively, so that $x=x^{*}+\varepsilon$ and $y=y^{*}+\eta$. For an operation $\omega$, the discrepancy between the exact computation and the computed one decomposes as

> 

$$
> \left(x\,\omega\,y-x^{*}\,\omega\,y^{*}\right)=\left(x\,\omega\,y-x^{*}\,\omega\,y^{*}\right)_{\text{propagated}}+\left(x^{*}\,\omega\,y-x^{*}\,\omega\,y^{*}\right)_{\text{generated}},
>
$$

> where the first term is the propagated error and the second is the newly generated error. Their cumulative total is the accumulated error.

> **Result (General formula for propagated error).** For a differentiable function $f$ of several approximate arguments, the propagated error is estimated to first order by the total differential,

> 

$$
> \Delta f\approx \sum_{i=1}^{m}\left\lvert\frac{\partial f}{\partial x_i}\right\rvert\Delta x_i,
>
$$

> where $\Delta x_i$ is the absolute error bound in the $i$-th argument. For a quadrature sum $Q=\sum_{i}w_i y_i$ with fixed weights $w_i$, this reduces to

> 

$$
> \Delta Q\le \sum_{i}\lvert w_i\rvert\,\Delta y_i.
>
$$

> **Result (Causes of errors and their control).** Errors in numerical computation arise from round-off (finite machine representation), truncation (replacing an infinite or exact process by a finite one), and the propagation of these through successive operations. They are minimized by carrying extra guard digits, by choosing stable formulations that avoid subtraction of nearly equal quantities, by using symmetric rounding rather than chopping, and by reducing the step size where truncation dominates.

> **Result (Significant figures).** A number stated to $n$ decimal places carries an absolute error bound of $0.5\times 10^{-n}$. For example, the number $8.35678$ quoted to five decimal places satisfies $e_{\text{abs}}\le 0.5\times 10^{-5}$.

## 4. Worked Exemplar Problem with Step-by-Step Solution

**Problem.** Use the trapezoidal rule with $n=4$ to estimate

$$
\int_{1}^{2}x^{2}\,dx,
$$

and compare the estimate with the exact value.

**Step 1. Identify the data.** Here $a=1$, $b=2$, $n=4$, so the strip width is

$$
h=\frac{b-a}{n}=\frac{2-1}{4}=0.25.
$$

**Step 2. Tabulate the ordinates.** The mesh points are $x_i=1+0.25i$ for $i=0,1,2,3,4$, and $y_i=x_i^{2}$.

| $i$ | $x_i$ | $y_i=x_i^{2}$ |
|---|---|---|
| 0 | 1.000 | 1.0000 |
| 1 | 1.250 | 1.5625 |
| 2 | 1.500 | 2.2500 |
| 3 | 1.750 | 3.0625 |
| 4 | 2.000 | 4.0000 |

**Step 3. Apply the trapezoidal rule.** Substituting the weights gives

$$
\begin{aligned}
T_4 &= \frac{h}{2}\Bigl(y_0+2y_1+2y_2+2y_3+y_4\Bigr) \\
&= \frac{0.25}{2}\Bigl(1.0000+2(1.5625)+2(2.2500)+2(3.0625)+4.0000\Bigr) \\
&= 0.125\Bigl(1.0000+3.1250+4.5000+6.1250+4.0000\Bigr) \\
&= 0.125(18.7500) \\
&= 2.34375.
\end{aligned}
$$

**Step 4. Compute the exact value.** The antiderivative of $x^{2}$ is $\tfrac{x^{3}}{3}$, hence

$$
\begin{aligned}
\int_{1}^{2}x^{2}\,dx &= \left[\frac{x^{3}}{3}\right]_{1}^{2} \\
&= \frac{8}{3}-\frac{1}{3} \\
&= \frac{7}{3} \\
&\approx 2.33333.
\end{aligned}
$$

**Step 5. Assess the error.** The absolute error of the estimate is

$$
\begin{aligned}
e_{\text{abs}} &= \lvert 2.34375-2.33333\rvert \\
&\approx 0.01042,
\end{aligned}
$$

and the relative error is

$$
\begin{aligned}
e_r &= \frac{0.01042}{2.33333} \\
&\approx 0.00447.
\end{aligned}
$$

The estimate is an over-estimate, consistent with the convexity of $x^{2}$ on $[1,2]$. Refining to $8$ strips reduces the error substantially: with $h=0.125$ the ordinates are $1.000$, $1.2656$, $1.5625$, $1.890625$, $2.25$, $2.640625$, $3.0625$, $3.51625$ and $4.000$, and the trapezoidal sum moves closer to $2.33333$. The error can always be reduced by using smaller strips.

**Step 6. Propagated error in the final sum.** Suppose each ordinate is known only to four decimal places, so that $\Delta y_i\le 0.5\times 10^{-4}$ for every $i$. The weights in the trapezoidal sum are $\tfrac{h}{2}$ times $1,2,2,2,1$, and the propagated error bound is

$$
\begin{aligned}
\Delta T_4 &\le \frac{h}{2}\Bigl(1+2+2+2+1\Bigr)\left(0.5\times 10^{-4}\right) \\
&= 0.125\times 8\times 0.5\times 10^{-4} \\
&= 5.0\times 10^{-5}.
\end{aligned}
$$

This is far smaller than the truncation error of about $1.04\times 10^{-2}$, confirming that the dominant error here is the truncation error of the rule rather than the propagated round-off error of the data.

## 5. High-Yield Exam Takeaways & Common Pitfalls

**High-yield takeaways.**

- The trapezoidal rule uses weights $1,2,2,\dots,2,1$ multiplied by $\tfrac{h}{2}$; Simpson's rule uses weights $1,4,2,4,\dots,4,1$ multiplied by $\tfrac{h}{3}$ and requires an even number of strips.
- Simpson's rule is derived by translating the interval to $[-h,h]$ and integrating the parabola $ax^{2}+bx+c$ exactly over that symmetric interval; the linear term contributes nothing because of symmetry.
- The trapezoidal error scales like $h^{2}$ while the Simpson error scales like $h^{4}$; the Simpson bound involves the fourth derivative and the factor $\tfrac{b-a}{180}$.
- Absolute error is $\lvert x-x_r\rvert$; relative error divides this by $\lvert x\rvert$; a number correct to $n$ decimal places has absolute error at most $0.5\times 10^{-n}$.
- Propagated error is the part of the discrepancy inherited from initial errors; generated error is the part created by the operation itself; their sum is the accumulated error.
- For a weighted sum, the propagated error bound is $\sum_i\lvert w_i\rvert\Delta y_i$, so large weights amplify data errors.

**Common pitfalls.**

- Forgetting the factor $\tfrac{h}{2}$ (trapezoidal) or $\tfrac{h}{3}$ (Simpson) and reporting only the weighted sum of ordinates.
- Using Simpson's rule with an odd number of strips; the rule pairs ordinates and requires $n$ even.
- Double-counting interior ordinates in the trapezoidal rule instead of assigning weight $2$ to each shared ordinate.
- Confusing truncation error (from the rule itself) with round-off error (from finite representation); the two are bounded by entirely different expressions.
- Reporting a relative error without the absolute value in the denominator, which produces a meaningless negative ratio when $x<0$.
- Assuming that refining the mesh always improves the answer: once truncation error falls below the propagated round-off error of the ordinates, further refinement cannot help.