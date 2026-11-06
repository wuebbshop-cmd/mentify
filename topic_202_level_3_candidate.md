## 1. Exam target: differentiate an approximation, then assess its error

Numerical differentiation is needed when a function is complicated or known only at tabulated points. The exact definition is

$$
f'(x)=\lim_{h\to0}\frac{f(x+h)-f(x)}{h}.
$$

A table does not supply the limiting process, so the course method first constructs or uses an interpolating polynomial $P_n(x)$ and then differentiates it. The resulting $P_n'(x)$ and $P_n''(x)$ approximate $f'(x)$ and $f''(x)$; they are not automatically exact. The lecture objectives are to obtain derivatives with finite differences and compute the errors involved.

High-yield distinction: interpolation approximates the function values over the data range, but differentiation magnifies local approximation error. A small difference $f-P_n$ does not guarantee a small derivative difference $f'-P_n'$, and higher derivatives generally become less accurate.

## 2. Interpolation-based differentiation

One route is to construct a polynomial $P_n$ through the tabulated data and differentiate it the required number of times. For equally spaced values, Newton’s difference polynomial is convenient. For unequally spaced nodes, use an interpolation formula such as Lagrange’s polynomial, differentiate the resulting polynomial, and evaluate at the requested point.

For three points, a quadratic interpolant can represent curvature while a linear interpolant has constant slope. This is why the lecture compares derivatives from linear and quadratic interpolation and notes that the quadratic estimate is generally more accurate when the data support the curvature. That does not make it exact: its error still depends on the omitted higher-degree behavior of the original function.

If the derivative requested is at a non-tabular point, substitute that point into the differentiated interpolating polynomial. Always identify which data points define the polynomial and which derivative order is being evaluated. Differentiating a fitted polynomial once estimates slope; differentiating twice estimates curvature and is usually more sensitive to data rounding.

## 3. Newton forward differences at and between tabular points

Assume equally spaced data with spacing $h$, values $f_i=f(x_i)$, and forward differences

$$
\Delta f_i=f_{i+1}-f_i,\qquad
\Delta^2 f_i=\Delta f_{i+1}-\Delta f_i,
$$

with higher differences formed by repeating the same operation. Write a non-tabular point as $x=x_i+sh$. Newton’s forward polynomial is

$$
P(s)=f_i+s\Delta f_i+\frac{s(s-1)}{2!}\Delta^2f_i
+\frac{s(s-1)(s-2)}{3!}\Delta^3f_i+\cdots.
$$

Because $ds/dx=1/h$, differentiating with respect to $x$ introduces a factor $1/h$ for the first derivative and $1/h^2$ for the second. The first-derivative expansion is

$$
f'(x_i+sh)=\frac{1}{h}\left[
\Delta f_i+(s-\tfrac12)\Delta^2f_i
+\frac{3s^2-6s+2}{6}\Delta^3f_i+\cdots\right].
$$

The second-derivative expansion begins

$$
f''(x_i+sh)=\frac{1}{h^2}\left[
\Delta^2f_i+(s-1)\Delta^3f_i
+\frac{6s^2-18s+11}{12}\Delta^4f_i+\cdots\right].
$$

These are not unrelated memorized formulas: they follow by differentiating the same interpolation polynomial and applying the chain rule. At the starting tabular point $s=0$,

$$
f'(x_i)=\frac{1}{h}\left(\Delta f_i-\frac12\Delta^2f_i+\frac13\Delta^3f_i-\frac14\Delta^4f_i+\cdots\right),
$$

$$
f''(x_i)=\frac{1}{h^2}\left(\Delta^2f_i-\Delta^3f_i+\frac{11}{12}\Delta^4f_i+\cdots\right).
$$

At the next tabular point $s=1$, the first terms are

$$
f'(x_i+h)=\frac{1}{h}\left(\Delta f_i+\frac12\Delta^2f_i-\frac16\Delta^3f_i+\cdots\right).
$$

At the midpoint $s=\tfrac12$,

$$
f'(x_i+\tfrac12h)=\frac{1}{h}\left(\Delta f_i-\frac{1}{24}\Delta^3f_i+\cdots\right),
$$

which shows a useful cancellation of the second-difference term. Use the full expansion when higher accuracy is required; the one-term formulas $f'(x_i)\approx\Delta f_i/h$ and $f''(x_i)\approx\Delta^2f_i/h^2$ are lower-order approximations.

## 4. Worked table calculation for $e^x$

The approved lecture uses tabulated values at spacing $h=0.05$:

| $x_i$ | $f_i=e^{x_i}$ | $\Delta f_i$ | $\Delta^2 f_i$ | $\Delta^3 f_i$ | $\Delta^4 f_i$ |
|---:|---:|---:|---:|---:|---:|
| 0.10 | 1.10517 | 0.05666 | 0.00291 | 0.00015 | -0.00001 |
| 0.15 | 1.16183 | 0.05957 | 0.00306 | 0.00014 | |
| 0.20 | 1.22140 | 0.06263 | 0.00320 | | |
| 0.25 | 1.28403 | 0.06583 | | | |
| 0.30 | 1.34986 | | | | |

At $x_0=0.10$, the first derivative using differences through $\Delta^3$ is

$$
f'(0.10)\approx \frac{1}{0.05}\left(0.05666-\frac12(0.00291)+\frac13(0.00015)\right)
=1.1051.
$$

The analytic value is $e^{0.1}\approx1.10517$, so the observed absolute difference is about $0.00007$. If the fourth difference is treated as nearly constant, the first omitted term estimates the truncation contribution as

$$
\left|\frac{\Delta^4 f_0}{4h}\right|
=\frac{0.00001}{4(0.05)}=0.00005.
$$

For the second derivative, retaining differences through $\Delta^3$ gives

$$
f''(0.10)\approx \frac{0.00291-0.00015}{(0.05)^2}=1.104.
$$

Since the exact value is also $e^{0.1}\approx1.10517$, the observed absolute difference is about $0.00117$. The next term in the expansion has magnitude

$$
\left|\frac{11\Delta^4 f_0}{12h^2}\right|
=\frac{11(0.00001)}{12(0.05)^2}\approx0.00367.
$$

This illustrates both the calculation and the greater sensitivity of the second derivative. Do not confuse an estimated omitted-term contribution with the observed error against a known exact derivative.

## 5. Errors, accuracy, and method selection

There are two main error sources in this calculation. **Truncation error** comes from omitting higher finite differences or using a polynomial of insufficient degree. Estimate it from the first neglected term when the difference pattern and smoothness justify that estimate. **Data and round-off error** enter through the tabulated values and arithmetic. Since differentiation divides by powers of $h$, small data errors can be amplified by $1/h$ for the first derivative and $1/h^2$ for the second.

Choose the method to fit the data:

- At the start of an equally spaced table, Newton forward differences use values beginning at that endpoint.
- Near the end, a backward-difference expansion is usually more appropriate.
- At an interior point, use a centered formula or an interpolation polynomial based on points on both sides when the course method and data permit it.
- For unequally spaced nodes, do not apply equal-spacing difference formulas; construct and differentiate the appropriate Lagrange or other interpolation polynomial.

If a function is known analytically, compare the numerical derivative with the exact derivative to compute observed absolute and relative errors. If only a table is available, report an estimate based on omitted differences and state the smoothness/equal-spacing assumptions. Smaller $h$ does not automatically guarantee a better result because amplified data or round-off error may offset reduced truncation error.

## 6. Exam-mode checklist and common traps

For a table problem:

1. Check that the $x$-values are equally spaced and calculate $h$.
2. Build the forward or backward difference table carefully; each new column is the difference of adjacent entries in the previous column.
3. Identify whether the requested point is tabular, between nodes, or near an endpoint.
4. Select the corresponding interpolation/finite-difference expansion and state how many terms are retained.
5. For derivatives of order $r$, track the factor $h^{-r}$ from the chain rule.
6. Estimate truncation error from the first omitted term where justified, and distinguish that estimate from an observed error against a known exact value.
7. Round only after the calculation and do not claim more accuracy for $f''$ than the data support.

Typical traps are mixing up $\Delta f_i$ and $\Delta^2f_i$, omitting the $1/h$ or $1/h^2$ factor, using forward differences at the wrong end of a table, applying equal-step formulas to uneven nodes, treating a differentiated interpolant as the exact derivative, and assuming that a small interpolation error means a small derivative error. The exam-ready answer shows the table, formula, substitutions, retained order, and error interpretation.
