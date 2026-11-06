## 1. Core Concept Overview & Intuition

### Lecture Objectives

By the end of this topic you should be able to:

- Define and calculate round-off, truncation, absolute, relative and percentage errors.
- Identify measures taken to minimize round-off errors.
- Define propagated error in addition, subtraction, multiplication and division.
- Calculate propagation errors with reference to numerical computations.
- Explain the causes of errors and how to avoid them.

### The Everyday Idea Behind Numerical Integration

Imagine you want to know the area of a field with a curved boundary. You cannot lay a perfect mathematical curve on the ground, but you can place a long measuring tape across the field and take a few readings of the boundary height at evenly spaced points. Then you join the tops of those readings with straight lines and add up the areas of the resulting simple shapes. The answer you get is close to the true area, but not exact. Numerical integration is exactly this idea: we replace a difficult area by a sum of easy areas.

The analogy stops being exact in one place. In the field, the tape readings are exact numbers. In a computer, every reading is stored with a limited number of digits, so each reading already carries a small error. That is why this topic begins with errors and only then moves to the area rules.

### Why Errors Come First

A computer has finite memory. It cannot store all real numbers exactly. So every number we type in, and every number the computer calculates, is an approximation. When we feed approximate heights into an area rule, the small errors travel through the arithmetic and grow. The error in the final answer that comes from the errors in the inputs is called the **propagated error**. The running total of all such errors at any stage is called the **accumulated error**.

### The Two Big Sources of Error

- **Round-off error**: arises because it is impossible to represent all real numbers exactly on a machine with finite memory. It involves dropping decimal places or significant figures, and can be done by chopping (truncating) or by symmetric rounding.
- **Truncation error**: arises when we replace an exact process by a shorter, finite one. For example, replacing a curve by straight lines is a truncation of the true shape.

### The Two Ways to Measure Error

- **Absolute error** tells you how far off you are, in the same units as the quantity. If you measure a length as $2.4$ m when it is really $2.43$ m, the absolute error is $0.03$ m.
- **Relative error** tells you how large that miss is compared with the size of the quantity itself. A miss of $0.03$ m is serious for a pencil but negligible for a bridge. Relative error captures this.

### The Big Picture of This Topic

The topic has two halves that fit together:

1. **Errors and approximation**: how to describe and measure the error in a single number.
2. **Propagation of errors**: how those single-number errors combine when we add, subtract, multiply or divide.

Numerical integration then uses these ideas to judge how trustworthy an area estimate is.

## 2. Mathematical Formalization & Core Definitions

### Round-off and Truncation Errors

> **Definition (Round-off error).** Round-off error arises because it is impossible to represent all real numbers exactly on a machine (computer) with finite memory. It involves dropping out decimal points or significant figures and can be done by chopping or truncating and by symmetric rounding.

Let $x$ be the exact number and let $x_r$ be an approximate number to $x$.

> **Definition (Absolute error).** The absolute error is the absolute difference between the exact number $x$ and the approximate number $x_r$:
> 

$$
e_{\text{abs}}=\lvert x-x_r\rvert
$$

Let $\Delta x$ be such that

$$
e_{\text{abs}}=\lvert x-x_r\rvert=\Delta x
$$

where $\Delta x$ is the upper bound of the error.

> **Definition (Relative error).** The relative error $e_r$ is the absolute error measured in units of the exact quantity:
> 

$$
e_r=\frac{\lvert x-x_r\rvert}{\lvert x\rvert}
$$

The relative error is a pure number (no units). Multiplying it by $100$ gives the percentage error.

### Significant Figures

A number is said to be correct to $n$ decimal places when the digit in the $n$-th decimal place is trustworthy. The key practical rule from the source is:

> **Result (Error bound for a rounded number).** If a number is correct to $n$ decimal places, then the maximum absolute error is
> 

$$
e_{\text{abs}}=0.5\times 10^{-n}
$$

For example, for the number $8.35678$ correct to five decimal places, $e_{\text{abs}}\le 0.5\times 10^{-5}$.

The logic is simple. If a number is rounded to $n$ decimal places, the true value lies within half a unit of the last kept decimal place on either side. Half of $10^{-n}$ is $0.5\times 10^{-n}$.

### Propagation Errors

> **Definition (Propagated error).** The error in the result of an arithmetic operation arising due to initial errors in the numbers used in that operation is called the propagated error. The total cumulative error at any step in the procedure is called the accumulated error.

Let $x$ and $y$ be two exact numbers, and let $x^{*}$ and $y^{*}$ be approximations with initial errors $\varepsilon$ (epsilon) and $\eta$ (eta) respectively, so that

$$
x=x^{*}+\varepsilon,\qquad y=y^{*}+\eta
$$

Let $w$ denote an arithmetic operation (addition, subtraction, multiplication or division). The exact result is $x\,w\,y$ and the computed result is $x^{*}\,w\,y^{*}$. The total error splits into two parts:

$$
(x\,w\,y-x^{*}\,w\,y^{*})=(x\,w\,y-x^{*}\,w\,y)+(x^{*}\,w\,y-x^{*}\,w\,y^{*})
$$

The first bracket is the **propagated error**: the part of the error carried over from the initial errors $\varepsilon$ and $\eta$. The second bracket is the **generated error**: the new error created by the operation itself. Their sum is the **accumulated error**.

### General Formula for Propagated Error

For a quantity $z$ that depends on measured inputs $x_1,x_2,\dots,x_n$ with small errors $\Delta x_1,\Delta x_2,\dots,\Delta x_n$, the propagated error is estimated by adding the separate contributions in absolute value:

$$
\Delta z\approx\sum_{i=1}^{n}\left\lvert\frac{\partial z}{\partial x_i}\right\rvert\Delta x_i
$$

In words: find how strongly $z$ responds to each input (the partial derivative), multiply by the size of that input's error, take absolute values so that errors cannot cancel, and add. For the four basic operations this reduces to simple rules:

| Operation | Result $z$ | Propagated error bound |
|---|---|---|
| Addition | $z=x+y$ | $\Delta z=\Delta x+\Delta y$ |
| Subtraction | $z=x-y$ | $\Delta z=\Delta x+\Delta y$ |
| Multiplication | $z=xy$ | $\Delta z\approx\lvert x\rvert\Delta y+\lvert y\rvert\Delta x$ |
| Division | $z=x/y$ | $\Delta z\approx\dfrac{\lvert x\rvert\Delta y+\lvert y\rvert\Delta x}{y^{2}}$ |

Notice that in addition and subtraction the absolute errors simply add. In multiplication and division it is the **relative** errors that add:

$$
\frac{\Delta z}{\lvert z\rvert}\approx\frac{\Delta x}{\lvert x\rvert}+\frac{\Delta y}{\lvert y\rvert}
$$

### Causes of Errors and How to Avoid Them

In point form, the main causes are:

- **Finite machine memory**: not all real numbers can be stored exactly, producing round-off.
- **Chopping or truncating**: digits are simply dropped, which biases the answer downward in magnitude.
- **Repeated rounding**: each rounding step adds a little error, and these accumulate.
- **Subtraction of nearly equal numbers**: this is the most dangerous operation, because the absolute errors add while the result becomes tiny, so the relative error explodes.
- **Division by a small number**: a small denominator magnifies both the value and its error.
- **Replacing an exact process by a finite one**: this produces truncation error.

Measures to minimize round-off errors:

- Keep more digits (guard digits) during intermediate working and round only at the end.
- Avoid subtracting nearly equal numbers; rearrange the algebra so that large numbers do not cancel.
- Avoid dividing by very small quantities where possible.
- Use symmetric rounding rather than chopping, since chopping always pushes the answer in one direction.
- Choose stable formulas and check the answer against a rough estimate.

### Key Words in the Definition of Error

In point form, the key words are:

- **Exact number**: the true value, written $x$.
- **Approximate number**: the stored or measured value, written $x_r$ or $x^{*}$.
- **Difference**: the gap between the two.
- **Absolute value**: the gap taken without sign, so direction does not matter.
- **Upper bound**: the largest the gap can possibly be, written $\Delta x$.
- **Relative**: the gap compared with the size of the exact number.

### Teaching and Learning Cycle

The lesson is delivered in a two-hour session. The cycle runs as follows: numbering, pacing and sequencing are set out at the start; the purpose is stated (to introduce errors and algorithms and to compute the different types of errors); a brief summary of the overall task is given; learners watch the assigned explanatory material and follow the worked example in it; learners then work individually, listing the key words in the definition of errors and algorithms and making short notes on the causes of errors and how to avoid them. Interaction then begins: learners post answers on the discussion forum, study what colleagues have posted, note anything new, and improve their own answers. The moderator's interventions are to direct group discussion, encourage the participation of all learners, provide feedback, and summarise the lesson. The next lesson is propagated errors.

### Self-test Questions

1. Compute the absolute error and the relative error in the approximation of $p$ by $p^{*}$:
 - (a) $p=\pi$, $p^{*}=\frac{22}{7}$
 - (b) $p=\pi$, $p^{*}=3.1416$
 - (c) $p=e$, $p^{*}=2.718$
 - (d) $p=\sqrt{2}$, $p^{*}=1.414$
 - (e) $p=e^{10}$, $p^{*}=22000$
 - (f) $p=10\pi$, $p^{*}=1400$
 - (g) $p=58$, $p^{*}=399000$

2. State the maximum absolute error when a number is correct to $n$ decimal places.

3. Explain, in your own words, the difference between propagated error and generated error.

### Further Reading

- Standard texts on numerical analysis covering errors and approximation.
- Texts on numerical methods for scientific and engineering computation.
- Outline-series texts on numerical analysis.
- Advanced engineering mathematics texts.
- Open online lecture notes on error analysis in numerical computation.

## 3. Key Theorems & Essential Results

> **Result 1 (Absolute error).** For exact $x$ and approximation $x_r$, the absolute error is $e_{\text{abs}}=\lvert x-x_r\rvert$, and its upper bound is $\Delta x$.

> **Result 2 (Relative error).** The relative error is $e_r=\dfrac{\lvert x-x_r\rvert}{\lvert x\rvert}$, a dimensionless ratio.

> **Result 3 (Rounding bound).** If a number is correct to $n$ decimal places, then $e_{\text{abs}}=0.5\times 10^{-n}$.

> **Result 4 (Propagation in sums and differences).** For $z=x\pm y$, the absolute errors add: $\Delta z=\Delta x+\Delta y$.

> **Result 5 (Propagation in products and quotients).** For $z=xy$ or $z=x/y$, the relative errors add: $\dfrac{\Delta z}{\lvert z\rvert}\approx\dfrac{\Delta x}{\lvert x\rvert}+\dfrac{\Delta y}{\lvert y\rvert}$.

> **Result 6 (Accumulated error).** The accumulated error equals the propagated error plus the generated error.

## 4. Worked Exemplar Problem with Step-by-Step Solution

### Example 1: Absolute error from a rounded positive number

Given $x=2.4$ correct to one decimal place, find the absolute error.

**Step 1. Write the interval of possible true values.** Correct to one decimal place means the true value lies within half a unit of the last place on either side:

$$
X\in(2.35,\,2.45)
$$

**Step 2. Subtract the approximation from each end.**

$$
2.35-2.4\le x-x_r\le 2.45-2.4
$$

**Step 3. Take absolute values.**

$$
\lvert -0.05\rvert\le\lvert x-x_r\rvert\le\lvert 0.05\rvert
$$

**Step 4. State the bound.**

$$
e_{\text{abs}}=0.05=5.0\times 10^{-2}
$$

This agrees with Result 3, since $0.5\times 10^{-1}=0.05$.

### Example 2: Absolute error from a rounded negative number

Let $x_r=-10.788$ correct to three decimal places.

**Step 1. Write the interval.**

$$
X\in[-10.7885,\,-10.7875]
$$

**Step 2. Subtract the approximation from each end.**

$$
-10.7885+10.788\le x-x_r\le -10.7875+10.788
$$

**Step 3. Read off the bound.**

$$
e_{\text{abs}}=0.0005=0.5\times 10^{-3}
$$

The sign of the number does not matter; only the size of the half-unit gap matters.

### Example 3: Relative error for a famous approximation

Approximate $\pi$ by $p^{*}=\frac{22}{7}$.

**Step 1. Compute the absolute error.**

$$
e_{\text{abs}}=\left\lvert\pi-\frac{22}{7}\right\rvert\approx\lvert 3.14159265-3.14285714\rvert\approx 0.00126449
$$

**Step 2. Divide by the exact value.**

$$
e_r=\frac{0.00126449}{3.14159265}\approx 0.00040250
$$

**Step 3. Interpret.** The relative error is about $4.03\times 10^{-4}$, that is roughly four parts in ten thousand. The approximation is good to about three decimal places.

### Example 4: Propagated error in a product

Suppose $x=5.0$ with error $\Delta x=0.1$ and $y=3.0$ with error $\Delta y=0.2$. Find the error in $z=xy$.

**Step 1. Compute the value.**

$$
z=5.0\times 3.0=15.0
$$

**Step 2. Apply the product rule.**

$$
\Delta z\approx\lvert x\rvert\Delta y+\lvert y\rvert\Delta x
$$

**Step 3. Substitute.**

$$
\Delta z\approx(5.0)(0.2)+(3.0)(0.1)=1.0+0.3=1.3
$$

**Step 4. Interpret.** The product is $15.0$ with an error of about $1.3$, so the relative error is about $1.3/15.0\approx 0.087$, roughly nine per cent. Notice that the relative errors of the inputs, $0.1/5.0=0.02$ and $0.2/3.0\approx 0.067$, add to about $0.087$, exactly as Result 5 predicts.

### Example 5: The danger of subtracting nearly equal numbers

Suppose $x=1.234$ with error $\Delta x=0.001$ and $y=1.233$ with error $\Delta y=0.001$. Find the error in $z=x-y$.

**Step 1. Compute the value.**

$$
z=1.234-1.233=0.001
$$

**Step 2. Apply the difference rule.**

$$
\Delta z=\Delta x+\Delta y=0.001+0.001=0.002
$$

**Step 3. Interpret.** The answer is $0.001$ but the error is $0.002$, which is twice the answer itself. The relative error is $2$, or $200$ per cent. The result is meaningless. This is why subtracting nearly equal numbers must be avoided.

### Example 6: Error bound for a rounded reading

A measurement is recorded as $8.35678$ and is correct to five decimal places. Find the maximum absolute error.

**Step 1. Identify $n$.** Here $n=5$.

**Step 2. Apply Result 3.**

$$
e_{\text{abs}}\le 0.5\times 10^{-5}=0.000005
$$

**Step 3. Interpret.** The true value lies within five millionths of the recorded value.

## 5. High-Yield Exam Takeaways & Common Pitfalls

### High-Yield Takeaways

- Absolute error is $\lvert x-x_r\rvert$; relative error divides this by $\lvert x\rvert$; percentage error multiplies the relative error by $100$.
- A number correct to $n$ decimal places has maximum absolute error $0.5\times 10^{-n}$. This single line answers many short questions.
- In addition and subtraction, absolute errors add. In multiplication and division, relative errors add.
- Propagated error plus generated error equals accumulated error.
- Round-off comes from finite memory; truncation comes from replacing an exact process by a finite one.
- The most dangerous operation is subtraction of nearly equal numbers, because the absolute errors add while the result shrinks.

### Common Pitfalls

- **Forgetting the absolute value.** Errors are sizes, not signed quantities. Always take the modulus before adding.
- **Using the approximate value in the denominator of the relative error.** The definition divides by the exact value $\lvert x\rvert$, not by $\lvert x_r\rvert$.
- **Adding relative errors in a sum.** For $x+y$ it is the absolute errors that add, not the relative errors.
- **Adding absolute errors in a product.** For $xy$ it is the relative errors that add.
- **Rounding at every step.** Each rounding adds a little error; keep guard digits and round only at the end.
- **Ignoring the sign of a negative number.** The interval method works the same way; just subtract carefully and then take absolute values.
- **Confusing propagated with generated error.** Propagated error is carried in from the inputs; generated error is created by the operation itself.
- **Reporting too many digits.** An answer cannot be more accurate than the inputs that produced it.