## 1. Error measures and numerical reporting

Let $x$ be the exact value and $x_r$ the computed approximation. Use the signed convention $e=x-x_r$ unless the question specifies another. The error measures used in computations are

$$
E_{abs}=|x-x_r|,\qquad
E_{rel}=\frac{|x-x_r|}{|x|}\ (x\ne0),\qquad
E_{pct}=100E_{rel}\%.
$$

Absolute error is measured in the original units. Relative error compares error with scale, and percentage error is the relative error expressed as a percent. If $x=0$, relative error is undefined and an absolute tolerance is required. Do not confuse accuracy (closeness to the true value) with precision (repeatability or displayed digits).

For nearest rounding to $n$ decimal places,

$$
|x-x_r|\le \frac12 10^{-n}.
$$

For $p$ significant figures, the standard relative-error criterion is $E_{rel}\le \frac12 10^{1-p}$. Chopping instead of rounding may incur almost a full unit in the last retained place. When asked for bounds, translate the rounding unit into an interval; for example, 2.4 to one decimal place represents $2.35\le x<2.45$.

## 2. Round-off, truncation, and significant-figure control

Round-off error comes from finite-digit representation and arithmetic. Chopping discards later digits; symmetric rounding uses the first discarded digit to select the retained result. For instance, four significant digits from 1.3339 give 1.333 by chopping and 1.334 by rounding. Preserve guard digits during intermediate work and round once at the end.

Truncation error comes from replacing an exact process with a finite one: stopping an infinite expansion, using a finite approximation to a limit, or omitting higher-order terms. These errors have different remedies. Increasing precision or changing the arithmetic strategy addresses round-off; adding terms or using a higher-order method addresses truncation.

Repeated operations can produce accumulated error: propagated input errors plus newly generated arithmetic error. A small absolute error is not automatically harmless. Subtracting nearly equal numbers can leave a small result whose relative error is large; dividing by a small number can magnify an absolute error. These are exam cues to examine scale and conditioning before declaring an answer accurate.

## 3. Propagation in addition, subtraction, multiplication, and division

Let $x=x_r+\varepsilon$ and $y=y_r+\nu$, where $\varepsilon$ and $\nu$ are signed input errors. For addition and subtraction,

$$
(x\pm y)-(x_r\pm y_r)=\varepsilon\pm\nu,
$$

so the worst-case absolute propagated error is bounded by $|\varepsilon|+|\nu|$. Report a bound, not an assumed cancellation.

For multiplication,

$$
xy-x_ry_r=x_r\nu+y_r\varepsilon+\varepsilon\nu.
$$

The exact absolute bound is therefore

$$
|xy-x_ry_r|\le |x_r||\nu|+|y_r||\varepsilon|+|\varepsilon\nu|.
$$

For small input errors the last term is second order. Dividing the first-order bound by $|x_ry_r|$ shows that relative errors approximately add:

$$
E_{rel,xy}\approx \frac{|\varepsilon|}{|x_r|}+\frac{|\nu|}{|y_r|}.
$$

For $q=x/y$ with $y_r\ne0$, linearization gives

$$
\Delta q\approx \frac{\varepsilon}{y_r}-\frac{x_r\nu}{y_r^2},
\qquad E_{rel,q}\lesssim \frac{|\varepsilon|}{|x_r|}+\frac{|\nu|}{|y_r|}.
$$

The relative quotient estimate also assumes $x_r\ne0$ and small perturbations; the denominator must be well away from zero. In numerical work, state these assumptions instead of presenting a first-order estimate as an unconditional exact bound.

## 4. General formula, sensitivity, and conditioning

For $z=f(x)$, Taylor expansion about the approximation gives, to first order,

$$
\Delta z\approx f'(x)\Delta x,
\qquad |\Delta z|\approx |f'(x)|\,|\Delta x|.
$$

For $z=f(x_1,\ldots,x_n)$,

$$
\Delta z\approx \sum_{i=1}^n\frac{\partial f}{\partial x_i}\Delta x_i,
\qquad
|\Delta z|\lesssim \sum_{i=1}^n\left|\frac{\partial f}{\partial x_i}\right|\epsilon_i,
$$

when $|\Delta x_i|\le\epsilon_i$ and perturbations are small. Each partial derivative identifies how strongly the output responds to one input. A problem is ill-conditioned when small relative input changes can cause large relative output changes; an unstable computation can additionally amplify error through its chosen operations. Report both the estimate and its assumptions.

For $f(x_1,x_2,x_3)=x_1x_2^2/\sqrt{x_3}$, the sensitivity terms are

$$
\frac{\partial f}{\partial x_1}=\frac{x_2^2}{\sqrt{x_3}},\qquad
\frac{\partial f}{\partial x_2}=\frac{2x_1x_2}{\sqrt{x_3}},\qquad
\frac{\partial f}{\partial x_3}=-\frac{x_1x_2^2}{2x_3^{3/2}}.
$$

At $(x_1,x_2,x_3)=(2,3,1)$, $f=18$ and the derivative magnitudes are $9$, $12$, and $9$. If the input error bounds are $0.1$, $0.2$, and $0.1$, respectively, then

$$
|\Delta f|\lesssim 9(0.1)+12(0.2)+9(0.1)=4.2.
$$

Thus the first-order result is approximately $18\pm4.2$. This illustrates why each input needs its own partial derivative and its own error bound; multiplying one uncertainty by an arbitrary count is not a valid general method.

## 5. Worked exam calculations

### Approximation to $\pi$

For $x=\pi$ and $x_r=3.14$,

$$
E_{abs}=|\pi-3.14|\approx0.00159265,
\quad E_{rel}\approx\frac{0.00159265}{\pi}=0.000507,
\quad E_{pct}\approx0.0507\%.
$$

The correct order is absolute error, divide by the exact magnitude for relative error, then multiply by 100 for percentage error. Keep sufficient digits in the quotient before rounding.

### Propagated error in a product

If $x_r=3.45$ and $y_r=4.87$ are each rounded to the nearest 0.01, then $|\varepsilon|,|\nu|\le0.005$. Their product estimate is $x_ry_r=16.8015$. The exact first-order-plus-cross-term bound is

$$
|xy-x_ry_r|\le3.45(0.005)+4.87(0.005)+(0.005)^2
=0.041625.
$$

Dropping the cross term is a first-order approximation, not the exact bound. A response should label it accordingly.

### General formula check

For $A=s^2$ at $s=10$ with $|\Delta s|\le0.01$, $|\Delta A|\approx|2s|0.01=0.2$. A larger derivative magnitude would imply greater sensitivity to the same input error.

## 6. Exam-mode procedure and traps

1. Write down the exact quantity, approximation, and error convention.
2. Check whether the question requests an absolute error, relative error, percentage error, or guaranteed bound.
3. Convert the stated decimal-place or significant-figure precision into an input-error bound.
4. Classify each contribution as input, propagated, generated round-off, or truncation error.
5. For $+$ and $-$, bound absolute errors; for $\times$ and $\div$, use the correct first-order relative relation only when the operands are nonzero and the denominator is safe.
6. For a function, compute every partial derivative and evaluate it at the stated approximation.
7. State whether the result is exact, a first-order estimate, or a conservative bound; then report sensible digits.

Frequent traps: using relative error at zero; mixing decimal places with significant figures; calling all error round-off; adding relative errors for sums; dropping a cross term while claiming an exact product bound; ignoring near-cancellation or a small denominator; and reporting unsupported digits. Marks are earned by identifying the model and assumptions as clearly as by doing the arithmetic.
