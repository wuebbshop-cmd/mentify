## 1. The central idea: every computed answer has a margin of error

Numerical analysis develops ways to calculate useful answers from numerical data. The data may come from a measuring device, and a computer can store only a finite number of digits. For both reasons, a computed value is usually an approximation to the true value.

Imagine measuring a table that is actually 1.237 m long with a ruler marked in centimetres. You may record 1.24 m. The recorded value is convenient, but it is not the exact length. The difference between the true value and the recorded value is the error. Error does not always mean someone made a careless mistake; it can be an unavoidable part of measurement and computation. The goal is to understand its size and keep it within an acceptable limit.

Three related ideas should stay separate:

- The exact value is the value we would know with perfect data and exact arithmetic.
- The approximation is the value available to us.
- The error describes the difference between them.

## 2. Rounding, chopping, and measuring an approximation

### Round-off and truncation

A computer cannot keep every digit of every real number. If it stores only a limited number of digits, it must shorten a value. This creates round-off error.

There are two common ways to shorten a decimal:

- **Chopping**: discard the digits after the last kept digit.
- **Rounding**: inspect the next digit and adjust the last kept digit when needed.

For example, to keep four significant digits in 1.3339, chopping gives 1.333 while rounding gives 1.334. Both are approximations, but rounding is generally closer to the original number. A cut-off can also arise in a mathematical method: if an infinite series is stopped after a finite number of terms, the omitted part creates truncation error. Round-off comes from finite representation; truncation comes from stopping an exact mathematical process early.

### Absolute, relative, and percentage error

Let $x$ be the exact value and $x_r$ the recorded or computed approximation. Absolute error is the size of their difference:

$$
E_{abs}=|x-x_r|.
$$

If the exact value is 12.50 kg and the approximation is 12.47 kg, the absolute error is 0.03 kg. The units are the same as the quantity.

Relative error compares the error with the size of the exact value:

$$
E_{rel}=\frac{|x-x_r|}{|x|},\qquad x\ne 0.
$$

Percentage error is the relative error written as a percentage:

$$
E_{pct}=100E_{rel}\%.
$$

The relative measure helps compare errors on different scales. An error of 0.03 is small for a 12.50 kg object but large for a quantity whose true value is 0.04 kg. If the exact value is zero, relative error cannot be calculated because its denominator would be zero; report absolute error instead.

### Accuracy to decimal places and significant figures

Correct to $n$ decimal places refers to digits after the decimal point. Correct to $n$ significant figures refers to the first $n$ meaningful digits, starting at the first nonzero digit. For example, 0.004568 rounded to two significant figures is 0.0046, while rounded to three decimal places it is 0.005. These are different instructions and produce different approximations.

When rounding to the nearest unit in the last decimal place, the maximum absolute rounding error is half of that unit. Thus, rounding to $n$ decimal places gives

$$
E_{abs}\le \frac{1}{2}10^{-n}.
$$

For example, a value recorded as 2.4 to one decimal place lies within 0.05 of 2.4 under the usual nearest-rounding rule. That gives the interval $2.35\le x<2.45$. This interval is useful when a question asks for upper and lower bounds rather than only the rounded value.

## 3. Where errors come from and how to reduce them

### Input error

Measurements and supplied data may already be approximate. If a length is measured only to the nearest centimetre, later calculations cannot recover the unrecorded millimetres. A careful calculation should not report more certainty than the input supports.

### Round-off error

Finite-digit arithmetic introduces round-off at each stored value and operation. Chopping and rounding can produce different answers, especially after many operations. To reduce avoidable round-off:

- keep guard digits in intermediate steps;
- delay rounding until the final answer;
- use a stable order of calculation when alternatives are available;
- do not treat calculator output as exact merely because many digits are displayed.

Subtraction of nearly equal numbers deserves special care. For example, subtracting two values close to 10 may leave a small result. Errors that were small compared with 10 can then be large compared with that small difference. Division by a very small approximate value can also magnify an absolute error.

### Truncation error

Truncation error is introduced when a formula or process is stopped early. If a method uses only the first few terms of an expansion, the omitted terms contribute error. Unlike round-off, this error can often be reduced by taking more terms or choosing a more accurate approximation, though doing so may increase the amount of computation.

## 4. How errors pass through arithmetic

Suppose the exact inputs are $x$ and $y$, while the values used in a calculation are $x_r$ and $y_r$. Write their input errors as

$$
x=x_r+\varepsilon,\qquad y=y_r+\nu,
$$

where $\varepsilon$ and $\nu$ may be positive or negative. The error in the output caused by these input errors is called **propagated error**. New rounding introduced while carrying out the operation is **generated error**. The total accumulated error at a step includes both propagated error and generated error.

For addition or subtraction, the worst-case absolute error is bounded by the sum of the input error bounds:

$$
|\Delta(x\pm y)|\le |\varepsilon|+|\nu|.
$$

This is a worst-case bound because the two errors could act in the same direction. If they happen to cancel, the actual error may be smaller, but we cannot rely on cancellation when guaranteeing accuracy.

For multiplication, expand the exact product:

$$
xy=(x_r+\varepsilon)(y_r+\nu)
=x_ry_r+x_r\nu+y_r\varepsilon+\varepsilon\nu.
$$

Therefore the product error contains two first-order terms and a smaller product of the input errors. When the input errors are small, a useful first-order bound is

$$
|\Delta(xy)|\approx |x_r|\,|\nu|+|y_r|\,|\varepsilon|.
$$

For division, provided the denominator is not zero or close to zero, the first-order relative-error estimate is

$$
\frac{|\Delta(x/y)|}{|x_r/y_r|}
\approx \frac{|\varepsilon|}{|x_r|}+\frac{|\nu|}{|y_r|}.
$$

The denominator condition matters: if $y_r$ is tiny, even a small error in $y$ can have a large effect on the quotient. Products and quotients are often easier to estimate with relative errors, while sums and differences are usually estimated with absolute errors.

## 5. The general propagated-error formula

Many calculations use several approximate inputs. If

$$
z=f(x_1,x_2,\ldots,x_n),
$$

and the input $x_i$ has a small error $\Delta x_i$, then a first-order estimate for the output error is

$$
|\Delta z|\approx \sum_{i=1}^{n}
\left|\frac{\partial f}{\partial x_i}\right|\,|\Delta x_i|.
$$

Each partial derivative measures how strongly the output responds to a small change in one input while the others are held fixed. A large derivative means that even a small input error can noticeably affect the result. The formula is an estimate for small errors; it is not an exact bound for every large change.

For a square with side length $s$, the area is $A=s^2$, so $dA/ds=2s$. If $s=10$ m and the side-length uncertainty is at most 0.1 m, then

$$
|\Delta A|\approx |2s|\,|\Delta s|=2(10)(0.1)=2\text{ m}^2.
$$

The area uncertainty is about 2 square metres. This example shows why the formula of a calculation matters: the same measurement error can have a different effect in a different quantity.

As a second illustration, suppose a rectangle has measured sides $a=4$ m and $b=3$ m, with possible errors of 0.02 m and 0.01 m. Its area is $A=ab$, so

$$
|\Delta A|\approx |b|(0.02)+|a|(0.01)
=3(0.02)+4(0.01)=0.10\text{ m}^2.
$$

This estimate helps decide whether the measurements are accurate enough for the intended use.

## 6. Worked checks and common mistakes

### Example: error in an approximation to $\pi$

Use $x=\pi$ and $x_r=3.14$.

1. Absolute error:

$$
E_{abs}=|\pi-3.14|\approx 0.00159265.
$$

2. Relative error:

$$
E_{rel}=\frac{0.00159265}{\pi}\approx 0.000507.
$$

3. Percentage error:

$$
E_{pct}\approx 100(0.000507)\%=0.0507\%.
$$

The same approximation therefore has three descriptions: an absolute difference, a scale-adjusted difference, and that scale-adjusted difference as a percentage.

### Example: adding rounded measurements

Suppose 3.45 and 4.87 are each rounded to the nearest 0.01. Each input can differ from its true value by at most 0.005. The computed sum is 8.32, and its worst-case absolute input-error bound is

$$
0.005+0.005=0.01.
$$

So the exact sum lies between 8.31 and 8.33 (with endpoint details depending on the tie-rounding convention). Reporting many extra decimal places would not be justified by these inputs.

### Check yourself before submitting

- Is the question asking for absolute error, relative error, or percentage error?
- Is the exact value nonzero before using relative error?
- Does “decimal places” or “significant figures” describe the requested rounding?
- Are input errors being propagated, or is new rounding generated during the calculation?
- Is a small denominator or subtraction of nearly equal numbers making the result sensitive?
- Have you kept extra digits during working and rounded only at the end?

The main lesson is not that every computation can be exact. It is that a good numerical answer states what was approximated, identifies where error entered, estimates how it affects the result, and reports only precision the data can support.
