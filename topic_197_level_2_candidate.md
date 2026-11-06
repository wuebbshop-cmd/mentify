## 1. Numerical approximation and error sources

Numerical analysis develops and assesses procedures for computing results from numerical data. The result is generally approximate: measurements are rarely exact, and finite-digit arithmetic cannot represent every real number. Let $x$ denote the exact value and $x_r$ the value used or reported. With the signed error convention $e=x-x_r$, the absolute error is $|e|$; some texts use the opposite sign, so a calculation should state its convention when the sign matters.

Two distinct computational errors are important. **Round-off error** arises when a number is represented with a finite number of digits. **Truncation error** arises when an exact mathematical process, such as an infinite expansion or limiting process, is stopped and replaced by a finite procedure. Measurement or input error is already present before arithmetic begins. During a sequence of operations, the initial errors propagate through the calculation and new round-off may be generated; the cumulative error at a step is the accumulated error.

Chopping and rounding are different finite-digit rules. Chopping discards all digits after the retained position. Symmetric rounding uses the next digit to decide whether to increase the last retained digit. For example, to four significant figures, 1.3339 becomes 1.333 by chopping and 1.334 by rounding. Rounding is usually closer, but both introduce error. Retaining guard digits in intermediate steps and rounding only the final result reduce avoidable round-off.

## 2. Absolute error, relative error, and significant figures

The absolute error is

$$
E_{abs}=|x-x_r|.
$$

It has the same units as $x$. Relative error compares the absolute error with the magnitude of the exact value:

$$
E_{rel}=\frac{|x-x_r|}{|x|},\qquad x\ne 0.
$$

Percentage error is $100E_{rel}\%$. Absolute error is useful for a direct tolerance in units; relative error is useful for comparing errors in quantities of different magnitudes. Relative error is undefined when $x=0$, so use an absolute tolerance in that case.

If $x_r$ is rounded to $n$ decimal places, the nearest-rounding error satisfies

$$
|x-x_r|\le \frac{1}{2}10^{-n}.
$$

If digits are chopped rather than rounded, the error can approach one unit in the last retained decimal place. A value reported as 2.4 to one decimal place therefore represents an exact value in the interval $2.35\le x<2.45$ under the usual nearest-rounding convention; its maximum absolute error is 0.05.

Decimal places count digits after the decimal point. Significant figures begin with the first nonzero digit. For example, 0.004568 rounded to two significant figures is 0.0046; rounded to three decimal places it is 0.005. Confusing these instructions changes the approximation. A standard significant-figure criterion is that a nonzero approximation has at least $p$ correct significant figures when

$$
E_{rel}\le \frac{1}{2}10^{1-p}.
$$

This criterion scales the error with the size of the true quantity rather than judging accuracy only by the number of printed digits.

## 3. Propagation and accumulation in arithmetic

Let the exact values be $x$ and $y$, and let the approximations used in arithmetic be $x_r$ and $y_r$. Write

$$
x=x_r+\varepsilon,\qquad y=y_r+\nu,
$$

where $\varepsilon$ and $\nu$ are signed input errors. Propagated error is the difference between the exact operation on the true inputs and the same operation on the approximate inputs. Generated error is new error from representing or rounding the result of that operation. Accumulated error includes both effects and any error already present in the inputs.

For addition and subtraction, the propagated error is exactly $\varepsilon\pm\nu$. Therefore its worst-case magnitude is bounded by

$$
|\Delta(x\pm y)|\le |\varepsilon|+|\nu|.
$$

The bound assumes the errors act in the direction that increases the result error. Cancellation can make the actual error smaller, but should not be assumed in a guaranteed bound.

For multiplication,

$$
xy-x_ry_r=x_r\nu+y_r\varepsilon+\varepsilon\nu.
$$

Consequently,

$$
|xy-x_ry_r|\le |x_r||\nu|+|y_r||\varepsilon|+|\varepsilon\nu|.
$$

When input errors are small, the second-order term $|\varepsilon\nu|$ is often omitted to obtain the first-order estimate. Dividing by $|x_ry_r|$ gives the corresponding first-order relative-error rule: the relative error in a product is approximately the sum of the relative errors in its factors.

For a quotient $q=x/y$, with $y_r\ne0$ and errors small compared with the inputs, differentiating $q$ gives

$$
\Delta q\approx \frac{\varepsilon}{y_r}-\frac{x_r\nu}{y_r^2},
\qquad
\frac{|\Delta q|}{|x_r/y_r|}\lesssim
\frac{|\varepsilon|}{|x_r|}+\frac{|\nu|}{|y_r|},
$$

provided $x_r\ne0$ for the relative form. The denominator must be safely separated from zero. If $y_r$ is small, a modest error in $y$ can produce a large quotient error.

Subtraction of nearly equal values is another warning case: the absolute errors may remain small while the result itself is tiny, making relative error large. This is why a finite-digit calculation can lose useful accuracy even when every individual input was recorded carefully.

## 4. General propagated-error formula

For a differentiable function of one variable, $z=f(x)$, a small input perturbation $\Delta x$ gives the first-order estimate

$$
\Delta z\approx f'(x)\Delta x,
\qquad
|\Delta z|\approx |f'(x)|\,|\Delta x|.
$$

For several inputs,

$$
z=f(x_1,x_2,\ldots,x_n),
$$

the total differential gives

$$
\Delta z\approx \sum_{i=1}^{n}\frac{\partial f}{\partial x_i}\Delta x_i.
$$

If only upper bounds $|\Delta x_i|\le \epsilon_i$ are known, a conservative first-order maximum-error estimate is

$$
|\Delta z|\lesssim \sum_{i=1}^{n}
\left|\frac{\partial f}{\partial x_i}\right|\epsilon_i.
$$

The partial derivatives measure sensitivity: a large magnitude means the output changes strongly when that particular input changes. The estimate assumes small perturbations and sufficient differentiability; for large input errors, higher-order terms may matter.

For a rectangular area $A=ab$, if $a=4$ m and $b=3$ m with error bounds $\epsilon_a=0.02$ m and $\epsilon_b=0.01$ m, then

$$
|\Delta A|\lesssim |b|\epsilon_a+|a|\epsilon_b
=3(0.02)+4(0.01)=0.10\text{ m}^2.
$$

Thus a first-order estimate places the area within about $0.10\text{ m}^2$ of the computed value. The same method applies to any differentiable formula once its independent inputs and their error bounds are identified.

## 5. Worked computations

### Absolute, relative, and percentage error

For $x=\pi$ and $x_r=3.14$,

$$
E_{abs}=|\pi-3.14|\approx 0.00159265,
$$

$$
E_{rel}=\frac{0.00159265}{\pi}\approx 0.000507,
\qquad E_{pct}\approx 0.0507\%.
$$

The absolute error retains the units of the quantity; the relative and percentage errors are dimensionless. Since 3.14 is a coarse approximation to $\pi$, it is not correct to call it exact even though its absolute error is small.

### Addition of rounded inputs

Suppose 3.45 and 4.87 are each rounded to the nearest 0.01. Each input error is at most 0.005, so the computed sum is 8.32 and the propagated input-error bound is

$$
|\Delta(3.45+4.87)|\le 0.005+0.005=0.01.
$$

The true sum is therefore within 0.01 of 8.32, before adding any new arithmetic round-off. This separation is important: the bound above accounts for uncertainty in the inputs, not an additional rounding performed on the sum.

### Multiplication and quotient sensitivity

For $A=s^2$, $dA/ds=2s$. At $s=10$ with $|\Delta s|\le0.01$,

$$
|\Delta A|\approx 2(10)(0.01)=0.2.
$$

For a quotient with fixed numerator $x_r=1$ and denominator $y_r=0.01$, a denominator error of $0.0001$ is a relative input error of $0.01$. The quotient is $100$; its first-order absolute change is about $100(0.01)=1$. This illustrates why small denominators demand attention even when their absolute uncertainty looks small.

## 6. Exam method and common pitfalls

Use this sequence when a problem asks for an error calculation:

1. Identify the exact value, the approximation, and the error convention.
2. Decide whether the requested result is absolute, relative, percentage, or a maximum bound.
3. Check whether the task specifies decimal places or significant figures.
4. Identify whether the error is in the input, generated by arithmetic, or caused by truncation.
5. For arithmetic operations, use absolute-error bounds for sums and differences and relative-error estimates for products and quotients.
6. For a general function, compute its partial derivatives, multiply by the corresponding input-error bounds, and sum the magnitudes.
7. State assumptions, especially small perturbations and a denominator away from zero, then round the final answer to justified precision.

Common losses of marks include using relative error at a zero exact value, treating chopping as rounding, adding relative errors for a sum without justification, omitting the input-error product term when an exact product bound is required, ignoring cancellation or a small denominator, and claiming a first-order estimate is an exact bound. Numerical accuracy is demonstrated not merely by producing digits, but by explaining which errors those digits can support.
