## 1. Core Concept Overview & Intuition

### 1.1 What this unit is really about

This unit is about **polynomials** and **interpolation**. Before any formula appears, let us build the idea with everyday pictures.

A **polynomial** is the simplest kind of "smooth curve" expression you can write down. It is built only from a variable (call it $x$), constants, and the operations of adding and multiplying. For example, $3x^2-5x+7$ is a polynomial. There are no square roots, no fractions with $x$ in the denominator, and no trigonometric functions inside it. Because polynomials are so simple, computers and calculators can evaluate them quickly and reliably.

**Interpolation** is the act of "filling in the gaps." Imagine you have measured the temperature at 8 a.m., 10 a.m., and noon, but you did not measure it at 9 a.m. Interpolation is a sensible rule for guessing the 9 a.m. value from the values you do have. The rule we use is: draw the simplest smooth polynomial curve that passes exactly through the known points, then read off the value at the missing time.

### 1.2 An everyday analogy, and where it stops being exact

Think of a bus route with stops at known towns. You know the bus is at Town A at 8:00 and at Town B at 10:00. If you want to guess where it is at 9:00, you assume it travelled steadily. That "assume it travelled steadily" is exactly what a straight-line (degree-one) polynomial does.

The analogy stops being exact in one important way: a bus can stop for tea, so the real position at 9:00 may not lie on the straight line. In the same way, an interpolating polynomial is only a *model*. It passes exactly through the known points, but between them it is a guess. This is why the course also studies the **error** of the approximation.

### 1.3 Why we need this at all

Real data is almost never available at every point we care about. Measurement devices give us a finite list of pairs: an input value and the corresponding output value. Interpolation lets us build a single formula that reproduces every measured pair and can be evaluated anywhere in between. This is the foundation for later work such as estimating derivatives and integrals from tables of numbers.

### 1.4 The two big questions of this unit

Every technique in this unit answers one of two questions:

1. **Given a polynomial, how do we handle it efficiently?** We need to find its zeros (where it equals zero) and we need to evaluate it without wasting effort. The tools are **synthetic division** and **nested (Horner) form**.
2. **Given a table of data, how do we build the polynomial that fits it?** The tools are **Taylor polynomials** (for smooth functions near one point) and the **Lagrange polynomial** (for a finite set of data points).

### 1.5 The central promise of the unit

The central promise is stated as a theorem: if you have $n+1$ distinct input values and a function value at each one, then there is **exactly one** polynomial of degree at most $n$ that passes through all of them. "Exactly one" is powerful. It means that no matter which method you use — Lagrange, or any other — if the method produces a polynomial of degree at most $n$ fitting the data, it must be the *same* polynomial. Different methods are just different routes to one unique answer.

## 2. Mathematical Formalization & Core Definitions

### 2.1 Polynomial

> **Definition (Polynomial).** A polynomial in the variable $x$ is an expression of the form

> 

$$
P(x)=a_0+a_1x+a_2x^2+\cdots+a_nx^n
$$

> where $a_0,a_1,\dots,a_n$ are constants called the **coefficients**, and $n$ is a non-negative whole number called the **degree** provided $a_n\neq 0$. The number $a_0$ is the constant term, $a_1$ multiplies $x$, and so on.

The degree is simply the highest power of $x$ that actually appears. So $P(x)=4x^3-x+2$ has degree $3$, with $a_3=4$, $a_2=0$, $a_1=-1$, and $a_0=2$. Notice that a missing power is allowed; its coefficient is just zero.

### 2.2 Zeros of a polynomial

> **Definition (Zero or root).** A number $r$ is a **zero** (also called a **root**) of the polynomial $P$ if substituting it gives zero:

> 

$$
P(r)=0
$$

For example, $r=2$ is a zero of $P(x)=x^2-4$ because $2^2-4=0$. Finding zeros is one of the most common tasks in numerical work, because many problems reduce to "solve $P(x)=0$."

### 2.3 Synthetic division

**Synthetic division** is a shortcut for dividing a polynomial by a simple factor of the form $x-r$. It uses only the coefficients, so it avoids writing out all the powers of $x$.

The procedure is:

1. Write the coefficients of $P$ in order, from the highest power down to the constant. Insert a zero for any missing power.
2. Write the number $r$ to the left.
3. Bring the first coefficient straight down.
4. Multiply that number by $r$ and write the result under the next coefficient; add.
5. Repeat step 4 until the coefficients are exhausted.

The numbers you obtain are the coefficients of the **quotient**, and the very last number is the **remainder**. By the remainder theorem, that remainder equals $P(r)$.

> **Result (Remainder Theorem).** When a polynomial $P(x)$ is divided by $x-r$, the remainder is $P(r)$. Consequently, $r$ is a zero of $P$ exactly when the remainder is zero.

This is why synthetic division is so useful: it both tests whether a number is a zero and, when it is, gives the reduced polynomial that remains after the factor $x-r$ is removed.

### 2.4 Nested form of a polynomial

Writing a polynomial in **nested form** means factoring out $x$ repeatedly so that the expression becomes a chain of brackets. For a cubic,

$$
P(x)=a_0+a_1x+a_2x^2+a_3x^3
$$

can be rewritten as

$$
P(x)=a_0+x\left(a_1+x\left(a_2+a_3x\right)\right)
$$

The advantage is practical. To evaluate the original form at a given $x$, you must compute $x^2$ and $x^3$ separately, which is many multiplications. In nested form you work from the innermost bracket outward, and each step needs only one multiplication and one addition. This is called **Horner's method**, and it is the standard way to evaluate a polynomial efficiently.

### 2.5 Approximation by polynomials

Sometimes we cannot evaluate a function directly, but we can approximate it by a polynomial. The simplest tool is the **Taylor polynomial**, which matches the function and its first few derivatives at a single point $x_0$.

> **Definition (Taylor polynomial).** The Taylor polynomial of degree $n$ for a function $f$ about the point $x_0$ is the polynomial built so that its value and its first $n$ derivatives agree with those of $f$ at $x_0$.

The key limitation, stated in the course material, is that **Taylor polynomials are accurate only over small intervals**. All the information used is concentrated at the single point $x_0$, so as you move away from $x_0$ the approximation becomes inaccurate. This motivates interpolation, which uses information spread across several points.

### 2.6 Interpolation and polynomial approximation

> **Definition (Interpolation).** Given a set of data points $(x_0,y_0),(x_1,y_1),\dots,(x_n,y_n)$ with distinct $x$-values, **interpolation** is the construction of a polynomial $P$ such that

> 

$$
P(x_k)=y_k \quad \text{for each } k=0,1,\dots,n
$$

In words: the polynomial must pass exactly through every data point. The points $x_0,x_1,\dots,x_n$ are called the **nodes** or **knots**.

### 2.7 The Lagrange polynomial

The Lagrange approach builds the answer from simple building blocks called **fundamental polynomials** (also called Lagrange basis polynomials). Each building block is designed to equal $1$ at one node and $0$ at all the other nodes.

> **Definition (Lagrange fundamental polynomial).** For nodes $x_0,x_1,\dots,x_n$, the $k$-th fundamental polynomial is

> 

$$
L_{n,k}(x)=\prod_{\substack{j=0\\ j\neq k}}^{n}\frac{x-x_j}{x_k-x_j}
$$

The product symbol means "multiply together one fraction for every node except the $k$-th one." Each fraction is a straight-line expression in $x$. Because the numerator vanishes when $x=x_j$ for $j\neq k$, the whole product is zero at every node other than $x_k$. At $x=x_k$ every fraction equals $1$, so the product equals $1$.

The interpolating polynomial is then formed by multiplying each building block by the corresponding function value and adding:

$$
P(x)=f(x_0)L_{n,0}(x)+f(x_1)L_{n,1}(x)+\cdots+f(x_n)L_{n,n}(x)
$$

The course material describes the construction in three steps: first determine the Lagrange fundamental polynomials, then multiply each by the corresponding function value, and finally add them together.

## 3. Key Theorems & Essential Results

### 3.1 Uniqueness of the interpolating polynomial

> **Theorem (Existence and uniqueness).** If $x_0,x_1,\dots,x_n$ are $n+1$ distinct numbers and $f$ is a function whose values are given at these numbers, then there exists a unique polynomial $P(x)$ of degree at most $n$ with the property

$$
P(x_k)=f(x_k) \quad \text{for each } k=0,1,\dots,n
$$

> This polynomial is given by the Lagrange formula

$$
P(x)=f(x_0)L_{n,0}(x)+f(x_1)L_{n,1}(x)+\cdots+f(x_n)L_{n,n}(x)
$$

**Why this matters.** The word "unique" is the most important word in the theorem. It tells you that the answer does not depend on the method. If two different techniques both produce a polynomial of degree at most $n$ passing through the same $n+1$ points, the two polynomials must be identical. This is a powerful check on your work: if two methods disagree, at least one calculation is wrong.

**Why the degree is "at most" $n$.** Each fundamental polynomial is a product of $n$ straight-line factors, so it has degree $n$. Multiplying by a constant and adding does not raise the degree. Hence the result has degree at most $n$. It can be lower if the data happen to lie on a simpler curve.

### 3.2 The remainder theorem and its use

> **Result (Remainder Theorem).** For a polynomial $P$ and a number $r$, the remainder on dividing $P(x)$ by $x-r$ equals $P(r)$. In particular, $r$ is a zero of $P$ if and only if that remainder is zero.

This result is the justification for using synthetic division as a zero-finding tool. It also gives a fast way to evaluate a polynomial at a point without substituting directly.

### 3.3 Accuracy improves with degree

A standard example is the sine function. Approximating $\sin x$ near zero by successively higher-degree Taylor polynomials gives progressively better values. The cubic Taylor polynomial for $\sin x$ about $x_0=0$ is obtained by truncating the Taylor series after the term in $x^3$. Since the derivatives of $\sin x$ at $0$ are $1,0,-1,0,\dots$, the series is

$$
\sin x = x - \frac{x^3}{3!} + \frac{x^5}{5!} - \frac{x^7}{7!} + \cdots
$$

so the cubic Taylor polynomial is

$$
P_3(x)=x-\frac{x^3}{6}
$$

At $x=0.1$ we obtain

$$
\begin{aligned}
P_3(0.1) &= 0.1 - \frac{(0.1)^3}{6} \\
&= 0.1 - \frac{0.001}{6} \\
&= 0.1 - 0.000166666\ldots \\
&= 0.099833333\ldots
\end{aligned}
$$

The exact value is $\sin(0.1)=0.099833416\ldots$, so the absolute error of the cubic approximation is

$$
\lvert \sin(0.1)-P_3(0.1) \rvert = 8.331\ldots \times 10^{-8}
$$

This error is less than one millionth. By contrast, the linear Taylor polynomial $P_1(x)=x$ gives $P_1(0.1)=0.1$, and its error is about $1.666\ldots \times 10^{-4}$, which is only about three decimal places of accuracy. The polynomial $x-x^3$ is not the Taylor polynomial of $\sin x$; it would give $0.099$, a much worse approximation. The correct coefficient $1/6$ comes from the third derivative of $\sin x$ at zero.

The error of the cubic Taylor polynomial can be bounded. Because the Taylor series for $\sin x$ is alternating for small $x$, the error after the cubic term is at most the magnitude of the first omitted term:

$$
\lvert \sin(0.1)-P_3(0.1) \rvert \le \frac{(0.1)^5}{120}
$$

and

$$
\begin{aligned}
\frac{(0.1)^5}{120} &= \frac{10^{-5}}{120} \\
&= 8.333\ldots \times 10^{-8}
\end{aligned}
$$

which is consistent with the observed error. In general, **accuracy increases with increase in $n$** when the Taylor polynomial is evaluated near the expansion point.

### 3.4 The limitation of Taylor approximation

> **Result (Local nature of Taylor polynomials).** A Taylor polynomial uses information concentrated at a single point $x_0$. It is accurate only over a small interval around $x_0$, and its accuracy deteriorates as one moves away from $x_0$.

This is the reason interpolation exists as a separate topic. When data is spread over a range of $x$-values, a polynomial built from all of them can represent the function across that whole range, not just near one point.

## 4. Worked Exemplar Problem with Step-by-Step Solution

### 4.1 Problem statement

Consider the data in the following table, where $x$ is the input and $f(x)$ is the corresponding function value.

| $x$ | $0$ | $1$ | $2$ |
|:---|:---|:---|:---|
| $f(x)$ | $1$ | $2$ | $5$ |

1. Construct the Lagrange fundamental polynomials for these three nodes.
2. Hence write down the interpolating polynomial of degree at most $2$.
3. Verify that the polynomial passes through all three data points.
4. Evaluate the polynomial at $x=1.5$.

### 4.2 Step 1: Identify the nodes and values

The nodes are $x_0=0$, $x_1=1$, and $x_2=2$. The corresponding values are $f(x_0)=1$, $f(x_1)=2$, and $f(x_2)=5$. There are $n+1=3$ points, so $n=2$ and the polynomial will have degree at most $2$.

### 4.3 Step 2: Build the first fundamental polynomial

The first fundamental polynomial must equal $1$ at $x_0=0$ and $0$ at $x_1=1$ and $x_2=2$. It is built from the two nodes other than $x_0$:

$$
L_{2,0}(x)=\frac{(x-x_1)(x-x_2)}{(x_0-x_1)(x_0-x_2)}
$$

Substituting the node values:

$$
L_{2,0}(x)=\frac{(x-1)(x-2)}{(0-1)(0-2)}
$$

The denominator is $(-1)(-2)=2$. So

$$
L_{2,0}(x)=\frac{(x-1)(x-2)}{2}
$$

Check: at $x=0$ the numerator is $(-1)(-2)=2$, so the value is $1$. At $x=1$ the numerator is $0$, so the value is $0$. At $x=2$ the numerator is $0$, so the value is $0$. Correct.

### 4.4 Step 3: Build the second fundamental polynomial

This one must equal $1$ at $x_1=1$ and $0$ at the other two nodes:

$$
L_{2,1}(x)=\frac{(x-x_0)(x-x_2)}{(x_1-x_0)(x_1-x_2)}
$$

Substituting:

$$
L_{2,1}(x)=\frac{(x-0)(x-2)}{(1-0)(1-2)}
$$

The denominator is $(1)(-1)=-1$. So

$$
L_{2,1}(x)=\frac{x(x-2)}{-1}=-x(x-2)
$$

Check: at $x=1$ the numerator is $(1)(-1)=-1$, divided by $-1$ gives $1$. At $x=0$ the numerator is $0$. At $x=2$ the numerator is $0$. Correct.

### 4.5 Step 4: Build the third fundamental polynomial

This one must equal $1$ at $x_2=2$ and $0$ at the other two nodes:

$$
L_{2,2}(x)=\frac{(x-x_0)(x-x_1)}{(x_2-x_0)(x_2-x_1)}
$$

Substituting:

$$
L_{2,2}(x)=\frac{(x-0)(x-1)}{(2-0)(2-1)}
$$

The denominator is $(2)(1)=2$. So

$$
L_{2,2}(x)=\frac{x(x-1)}{2}
$$

Check: at $x=2$ the numerator is $(2)(1)=2$, divided by $2$ gives $1$. At $x=0$ and $x=1$ the numerator is $0$. Correct.

### 4.6 Step 5: Assemble the interpolating polynomial

Multiply each fundamental polynomial by its function value and add:

$$
P(x)=f(x_0)L_{2,0}(x)+f(x_1)L_{2,1}(x)+f(x_2)L_{2,2}(x)
$$

Substituting the values $1$, $2$, and $5$:

$$
P(x)=1\cdot\frac{(x-1)(x-2)}{2}+2\cdot\left(-x(x-2)\right)+5\cdot\frac{x(x-1)}{2}
$$

This is the interpolating polynomial. We may simplify it to see its shape. Expanding each term:

$$
P(x)=\frac{x^2-3x+2}{2}-2x^2+4x+\frac{5x^2-5x}{2}
$$

Combining the $x^2$ terms, the $x$ terms, and the constants gives

$$
P(x)=x^2+1
$$

### 4.7 Step 6: Verify the data points

Substitute each node into $P(x)=x^2+1$:

$$
P(0)=0^2+1=1
$$

$$
P(1)=1^2+1=2
$$

$$
P(2)=2^2+1=5
$$

All three match the table exactly. The construction is correct.

### 4.8 Step 7: Evaluate at the missing point

At $x=1.5$:

$$
P(1.5)=(1.5)^2+1=2.25+1=3.25
$$

So the interpolated value is $3.25$. Notice that this lies between the neighbouring table values $2$ and $5$, which is what we expect for a smooth curve passing through the points.

### 4.9 What this example teaches

The example shows the full Lagrange workflow: build one building block per node, multiply by the corresponding value, and add. It also shows the uniqueness theorem in action. The final answer $P(x)=x^2+1$ is a simple polynomial, and no other polynomial of degree at most $2$ can pass through those three points. If a different method were used on the same data, it would have to produce the same $x^2+1$.

## 5. High-Yield Exam Takeaways & Common Pitfalls

### 5.1 High-yield takeaways

- **Know the definitions cold.** A polynomial is a sum of constant multiples of powers of $x$. A zero is a value that makes the polynomial equal zero. Interpolation is fitting a polynomial exactly through given data points. These definitions are frequently asked directly.
- **State the uniqueness theorem precisely.** It requires $n+1$ **distinct** nodes and produces a polynomial of degree **at most** $n$. Both phrases are usually worth marks.
- **Remember the three-step Lagrange recipe.** Determine the fundamental polynomials, multiply each by its function value, then add. Write the steps out explicitly in an exam.
- **Use the remainder theorem as a check.** If you divide by $x-r$ and the remainder is zero, then $r$ is a zero. If the remainder is not zero, it equals $P(r)$, which is a quick way to evaluate the polynomial.
- **Prefer nested form for evaluation.** Nested form reduces the number of multiplications and is the efficient way to evaluate a polynomial by hand or by machine.
- **Remember the local nature of Taylor polynomials.** They are accurate near the expansion point and lose accuracy away from it. This is the standard reason given for preferring interpolation when data is spread out.
- **Higher degree generally means better accuracy near the data**, as the sine example shows, but the polynomial is still only a model between the points.

### 5.2 Common pitfalls

- **Forgetting to insert zero coefficients for missing powers.** When listing coefficients for synthetic division, a missing power such as $x^2$ in $x^3+4$ must be written as a zero. Omitting it shifts every subsequent coefficient and ruins the division.
- **Mixing up the node in the denominator.** In the fundamental polynomial $L_{n,k}$, the denominator uses $x_k$ minus each *other* node. A common error is to use $x$ in the denominator, which is wrong because the denominator must be a constant.
- **Assuming the degree is exactly $n$.** The theorem guarantees degree *at most* $n$. If the data lie on a simpler curve, the degree can be lower, as in the worked example where the answer was a quadratic even though the construction used three nodes.
- **Using non-distinct nodes.** If two $x$-values are equal, the denominator in a fundamental polynomial becomes zero and the construction fails. The uniqueness theorem explicitly requires distinct nodes.
- **Confusing interpolation with extrapolation.** Interpolation estimates a value *between* the known nodes. Guessing *outside* the range of the data is a different and much less reliable activity.
- **Believing a higher-degree polynomial is always better everywhere.** A high-degree polynomial can wiggle wildly between the data points. Accuracy near the nodes does not guarantee accuracy far from them.
- **Skipping the verification step.** Always substitute the original data points back into your final polynomial. This catches arithmetic slips in the fundamental polynomials before they cost marks.
- **Treating Taylor and Lagrange as interchangeable.** Taylor uses derivative information at one point; Lagrange uses function values at many points. Choose the tool that matches the information you actually have.