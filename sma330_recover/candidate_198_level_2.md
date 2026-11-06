## 1. Foundational Concepts, Definitions, and Axioms

### 1.1 What this unit is really about

This unit is about **polynomials** and **interpolation**. Before any formula appears, let us build the idea with everyday pictures.

A **polynomial** is the simplest kind of "smooth curve" expression you can write down. It is built only from a variable (call it $x$), constants, and the operations of adding and multiplying. For example, $3x^2-5x+7$ is a polynomial. There are no square roots, no fractions with $x$ in the denominator, and no trigonometric functions inside it. Because polynomials are so simple, computers and calculators can evaluate them quickly and reliably.

**Interpolation** is the act of "filling in the gaps." Consider you have measured the temperature at 8 a.m., 10 a.m., and noon, but you did not measure it at 9 a.m. Interpolation is a sensible rule for guessing the 9 a.m. value from the values you do have. The rule we use is: draw the simplest smooth polynomial curve that passes exactly through the known points, then read off the value at the missing time.

### 1.2 An everyday analogy, and where it stops being exact

Regard a bus route with stops at known towns. You know the bus is at Town A at 8:00 and at Town B at 10:00. If you want to guess where it is at 9:00, you assume it travelled steadily. That "assume it travelled steadily" is exactly what a straight-line (degree-one) polynomial does.

The analogy stops being exact in one important way: a bus can stop for tea, so the real position at 9:00 may not lie on the straight line. In the same way, an interpolating polynomial is only a *model*. It passes exactly through the known points, but between them it is a guess. This is why the course also studies the **error** of the approximation.

### 1.3 Why we need this at all

Real data is almost never available at every point we care about. Measurement devices give us a finite list of pairs: an input value and the corresponding output value. Interpolation lets us build a single formula that reproduces every measured pair and can be evaluated anywhere in between. This is the foundation for later work such as estimating derivatives and integrals from tables of numbers.

### 1.4 The two big questions of this unit

Every technique in this unit answers one of two questions:

1. **Given a polynomial, how do we handle it efficiently?** We need to find its zeros (where it equals zero) and we need to evaluate it without wasting effort. The tools are **synthetic division** and **nested (Horner) form**.
2. **Given a table of data, how do we build the polynomial that fits it?** The tools are **Taylor polynomials** (for smooth functions near one point) and the **Lagrange polynomial** (for a finite set of data points).

### 1.5 The central promise of the unit

The central promise is stated as a theorem: if you have $n+1$ distinct input values and a function value at each one, then there is **exactly one** polynomial of degree at most $n$ that passes through all of them. "Exactly one" is powerful. It means that no matter which method you use — Lagrange, or any other — if the method produces a polynomial of degree at most $n$ fitting the data, it must be the *same* polynomial. Different methods are just different routes to one unique answer.

## 2. Theorems, Lemmas, and Analytical Properties

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

## 3. Formal Proofs, Derivations, and Methods

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

## 4. Representative Worked Examples and Solutions

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

### 4.1 An interpolation table worked in two forms

Take four equally spaced nodes $x=0,1,2,3$ with tabulated values $1,2,5,10$. The difference table begins with the observations, then subtracts neighboring values:

$$
\begin{array}{c|c|c|c|c}
x&y&\Delta y&\Delta^2y&\Delta^3y\\
0&1&1&2&0\\
1&2&3&2&\\
2&5&5&&\\
3&10&&&
\end{array}
$$

The constant second differences suggest a quadratic fit. With step size $h=1$, the normalized variable is $u=(x-x_0)/h=x$. Newton’s forward polynomial is

$$
P(x)=y_0+u\Delta y_0+\frac{u(u-1)}{2!}\Delta^2y_0
=1+u+\frac{u(u-1)}{2}(2)=x^2+1.
$$

At $x=1.5$, the forward form gives $1+1.5+1.5(0.5)=3.25$. This agrees with the Lagrange result because both polynomials have degree at most three and fit the same four data points; in this example the zero third difference reveals that the polynomial reduces to degree two. The agreement is a useful check, not an expectation that all arithmetic paths will look identical.

The factor $u(u-1)/2$ is not decoration. It makes the second-difference contribution vanish at the first two nodes and equal the required scaled amount at the next node. Higher-order terms continue the same pattern with products of consecutive shifted variables. Omitting the factorial or using $x$ instead of $u$ when the spacing is not one changes the result.

### 4.2 Unequal spacing requires divided differences

Now use nodes $0,1,3$ with values $1,2,10$. These are not equally spaced, so the ordinary forward-difference table with a fixed $h$ is not the appropriate tool. Divided differences retain the actual node gaps. The first slopes are

$$
f[0,1]=\frac{2-1}{1-0}=1,\qquad
f[1,3]=\frac{10-2}{3-1}=4.
$$

The second divided difference is

$$
f[0,1,3]=\frac{f[1,3]-f[0,1]}{3-0}=1.
$$

The Newton form is therefore

$$
P(x)=f[0]+f[0,1](x-0)+f[0,1,3](x-0)(x-1)
=1+x+x(x-1)=x^2+1.
$$

It reproduces all three observed values. At $x=2$, it gives five, the value consistent with this quadratic. A common error is to apply a constant step formula to irregular nodes; that silently changes the geometry of the data. A second error is to divide a second-difference row by two without checking whether the intended Newton basis already includes its factorial scaling.

### 4.3 Taylor approximation and the point of expansion

For a smooth function, the Taylor polynomial about $x_0$ uses derivatives at that point. For example, the degree-two Taylor polynomial for $e^x$ about zero is

$$
T_2(x)=1+x+\frac{x^2}{2}.
$$

At $x=0.1$, this gives $1.105$, close to $e^{0.1}\approx1.10517$. The omitted terms begin with $x^3/3!$, so their size is small at $0.1$. At $x=2$, the same short polynomial gives $5$, whereas $e^2\approx7.389$. The formula has not become algebraically wrong; the point is simply farther from the expansion point, and the omitted terms matter more.

The example shows why “Taylor is local” is a practical warning rather than a statement that every Taylor polynomial must fail outside a fixed interval. The error depends on the function, the degree, the expansion point, and the evaluation point. If an explicit remainder bound is available, use it to assess the range; otherwise, compare the approximation with other information and avoid claiming unsupported accuracy.

Interpolation distributes information across nodes. It exactly fits the chosen values, which is an advantage when a table is the only data. It does not automatically dominate Taylor approximation: noisy observations can make an exact fit undesirable, and a high-degree polynomial can oscillate between data points. Choose the method that matches the information and objective, then discuss its limitation.

### 4.4 Synthetic division and Horner evaluation as complementary tools

Synthetic division and Horner’s method share a coefficient recurrence, but they answer different questions. Synthetic division divides by $x-r$, and its remainder tests the value $P(r)$. Horner evaluation computes $P(r)$ efficiently whether or not $r$ is a root. If the remainder is zero, the quotient gives a factorization step; if it is not, the polynomial still has a well-defined value at $r$.

For $P(x)=2x^3-3x^2+4x-5$, the Horner recurrence at $x=2$ gives the sequence $2$, $2(2)-3=1$, $1(2)+4=6$, and $6(2)-5=7$. The last value equals the remainder when dividing by $x-2$. Since it is nonzero, $x=2$ is not a root. The quotient coefficients are $2,1,6$, so

$$
P(x)=(x-2)(2x^2+x+6)+7.
$$

Multiplying out verifies the identity. This remainder check is especially useful after synthetic division because a single arithmetic error can corrupt every quotient coefficient.

### 4.5 Diagnostic checks before interpreting a fitted curve

An interpolating polynomial is defined by the nodes and ordinates, so its first check is exact reproduction of those pairs. The second check is structural: do the differences correspond to equally spaced nodes, and does the selected formula match the spacing? The third check is interpretive: is the requested point inside the convex span of the nodes or outside it?

For data from measurement, exact reproduction is a property of the constructed polynomial, not proof that the underlying physical process passes through each measured point exactly. The observations may already be rounded or noisy. A degree-$n$ interpolant through $n+1$ points can pass through that noise as well as through the signal. If the purpose is to explain a trend rather than reproduce every datum, interpolation and approximation are different tasks.

When presenting a result, keep unrounded intermediate differences and coefficients long enough to avoid avoidable arithmetic drift. Then substitute the nodes into the final expression, evaluate the target point, and round once at the end. Include a sentence saying what the estimate represents. This separates algebraic correctness from the real-world assumptions behind the input data.

### 4.6 Forward and backward differences near opposite ends

Forward differences are convenient when the desired point is near the first node; backward differences organize the same data from the final node and are convenient near the end. Consider equally spaced inputs $0,1,2,3$ with values $1,2,5,10$. The forward polynomial begins from $x_0=0$ and uses the first differences $1$, then second difference $2$. At $x=2.5$, the forward coordinate is $u=2.5$:

$$
P(2.5)=1+2.5+\frac{2.5(1.5)}{2}(2)=7.25.
$$

The backward form starts at $x_3=3$ and uses $v=(x-x_3)/h=-0.5$. The last first difference is $5$ and the last second difference is $2$, giving

$$
P(x)=y_3+v\nabla y_3+\frac{v(v+1)}{2}\nabla^2y_3.
$$

At $x=2.5$, this gives $10+(-0.5)(5)+((-0.5)(0.5)/2)(2)=7.25$. Both forms produce the same quadratic; the choice of direction keeps the normalized variable near zero, which can make the arithmetic more convenient.

The exercise highlights a common notation trap. The backward operator $\nabla y_i=y_i-y_{i-1}$ uses a different indexing convention from the forward operator $\Delta y_i=y_{i+1}-y_i$. Their values may have matching patterns in a table but must be paired with the corresponding basis factors. Mixing backward differences with forward factors generally gives an incorrect polynomial.

### 4.7 Handling a table with a suspected misprint

Suppose equal-spaced data are expected to follow a quadratic trend, but the second-difference column reads $2,2.4,2$. The isolated mismatch may be a transcription error, a rounded measurement, or evidence that the function is not exactly quadratic. Do not silently replace $2.4$ by $2$. Recompute the differences from the original ordinates, check the spacing, and see whether the mismatch persists.

If all ordinates are exact and the underlying model is known to be quadratic, the constant second differences provide a constraint that can help locate an error. If observations are measured, exact constancy is not expected, and the pattern is only a diagnostic. Report the discrepancy and the assumption needed to use it as a correction.

This decision parallels the use of an interpolation polynomial. A table with $n+1$ entries always defines an interpolant of degree at most $n$, but that fact cannot distinguish a genuine trend from a mistyped ordinate. Algebraic existence is automatic for distinct nodes; data quality is a separate question.

### 4.8 Exact fit versus prediction quality

The Lagrange and Newton constructions agree because each is a representation of the unique polynomial through the nodes. A good cross-check is to evaluate both forms at the same intermediate point and compare results before rounding. If they differ, likely causes include an incorrect basis denominator, a missing factorial, the wrong spacing, or an arithmetic error.

Agreement between two algebraic forms does not certify the prediction. Both forms use the same nodes and values, so both inherit any measurement error and any limitation of the polynomial model. To discuss prediction quality, identify the requested point, whether it is inside the node range, the smoothness of the underlying function if known, and any remainder or error estimate available.

Rounding should happen after the polynomial has been evaluated. If coefficients are rounded early, a small coefficient error can be magnified by a large power of $x$. Horner form can reduce repeated operations, but the best practice is still to preserve guard digits and compare against an independent evaluation when feasible.

### 4.9 Exam-ready sequence

An orderly solution can be written in six steps. First, record the node-value pairs and verify that the nodes are distinct. Second, decide whether the spacing is uniform. Third, select the representation: direct Lagrange for a general set, divided differences for a Newton form with arbitrary nodes, or finite differences for equally spaced data. Fourth, calculate the coefficients or difference table with the node labels visible.

Fifth, verify the fit by substitution at each node, or at least at enough nodes to expose a likely indexing mistake. Sixth, evaluate the requested point and state whether it is interpolation or extrapolation. If an error estimate is requested, list the smoothness and derivative information used; do not infer a guaranteed error from a successful node-fit check.

This sequence earns credit for both method and interpretation. It also makes the answer reproducible: a reader can identify which data produced each coefficient and whether the algebra matches the geometry of the nodes.

### 4.10 Uniform versus nonuniform sampling

Uniform spacing means every consecutive node gap has the same value $h$. In that case the forward or backward difference operators and their familiar factorial-scaled formulas apply. If the gaps differ, the raw differences still exist, but treating them as coefficients of an equal-step formula is invalid. The actual intervals belong in the divided-difference denominators.

For example, points $0,1,3$ have gaps $1$ and $2$. A table that merely lists $y_0,y_1,y_2$ does not make the inputs equally spaced. Check the $x$-column before constructing the difference table. If the data are nonuniform, a Newton divided-difference form remains incremental and uses each true node separation.

This node check also affects the direction of a method. Forward and backward formulas are useful for equally spaced data near an endpoint; Lagrange and divided differences handle general distinct nodes. Selecting the wrong method can produce plausible-looking arithmetic while representing a different set of interpolation conditions.

### 4.11 Structural checks for a difference table

Every entry in a forward-difference table is obtained by subtracting adjacent entries in the row above. If the first row is $1,2,5,10$, the first differences are $1,3,5$, the second differences are $2,2$, and the third difference is zero. Recomputing these values from left to right is a quick check on signs and indexing.

The last row of an exact polynomial table may become constant or zero, but real data often have rounding noise. A small nonzero high-order difference may reflect measurement precision rather than a new, meaningful degree. Conversely, an apparent zero in a rounded table does not prove that the underlying continuous function is exactly polynomial.

When solving an exam problem, keep a row label for each order and include the step size. If using Newton’s forward polynomial, identify $u=(x-x_0)/h$; if using the backward version, identify $v=(x-x_n)/h$. This removes ambiguity about which endpoint anchors the basis.

## 5. Mathematical Extensions, Limits, and Common Errors

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

### Lessons 5–6: finite differences and Newton interpolation
The interpolation sequence continues from values at nodes to differences between neighboring values. For equally spaced arguments, write the step as $h$ and use $\Delta y_i=y_{i+1}-y_i$; repeated differences are formed by taking differences of the preceding row. The pattern in the table reveals whether a lower-degree polynomial is plausible: constant first differences indicate a linear pattern, constant second differences a quadratic pattern, and constant third differences a cubic pattern. This is a diagnostic for a table, not a claim that every data set must have constant differences.

For the source table $x=1,2,3,4,5,6$ with $y=-4,-2,2,14,40,86$, the first differences are $2,4,12,26,46$; the second differences are $2,8,14,20$; and the third differences are $6,6,6$. Hence Newton's forward polynomial through these equally spaced data is cubic. At $x=2.5$, $h=1$ and $u=(x-x_0)/h=1.5$. Substituting the leading forward differences gives

$$
P(x)=-4+2u+\frac{2}{2!}u(u-1)+\frac{6}{3!}u(u-1)(u-2),\qquad P(2.5)=-0.625.
$$

The formula's factors are not decorative: each new term vanishes at all earlier nodes, so adding a new difference term corrects the polynomial to fit the next data value without undoing previous matches. Near the last tabulated point, Newton's backward form uses $v=(x-x_n)/h$ and backward differences, arranging its products as $v(v+1)$, $v(v+1)(v+2)$, and so forth. For the same table, at $x=5.5$, $v=-0.5$, $\nabla y_6=46$, $\nabla^2 y_6=20$, and $\nabla^3 y_6=6$, so the cubic backward expression gives $P(5.5)=60.125$. The forward and backward forms are two organizations of the same unique interpolating polynomial; choose the one whose origin is near the requested $x$ to keep the dimensionless parameter small.

These later lessons complement, rather than replace, the earlier representations. Synthetic division efficiently tests a candidate linear factor and supplies a quotient; Lagrange's basis constructs a polynomial directly from node/value pairs; finite differences expose regular spacing and successive changes; Newton's forward/backward forms then make those differences the coefficients of a progressively built interpolant. Keeping these roles distinct prevents the common error of treating an interpolation formula as a division algorithm or assuming an equally spaced difference table applies to irregular nodes.

### A full forward-difference construction

Consider equally spaced data at \(x=0,1,2,3\) with ordinates \(1,4,9,16\). The step is \(h=1\). Form the table by subtracting adjacent entries at each level:

| \(x_i\) | \(y_i\) | \(\Delta y_i\) | \(\Delta^2y_i\) | \(\Delta^3y_i\) |
|---:|---:|---:|---:|---:|
| 0 | 1 | 3 | 2 | 0 |
| 1 | 4 | 5 | 2 | |
| 2 | 9 | 7 | | |
| 3 | 16 | | | |

The first differences are \(3,5,7\), the second differences are \(2,2\), and the third difference is zero. For equally spaced nodes, the forward Newton expression through these data is

$$
P(x_0+uh)=y_0+u\Delta y_0
+\frac{u(u-1)}{2!}\Delta^2y_0
+\frac{u(u-1)(u-2)}{3!}\Delta^3y_0+\cdots,
\qquad u=\frac{x-x_0}{h}.
$$

Here \(x_0=0\), \(h=1\), \(y_0=1\), \(\Delta y_0=3\), and \(\Delta^2y_0=2\); the third-difference term vanishes. Thus

$$
P(x)=1+3x+\frac{x(x-1)}{2}(2)
=1+2x+x^2.
$$

At \(x=1.5\), the normalized coordinate is \(u=1.5\), and the same result is obtained directly from the forward form:

$$
P(1.5)=1+1.5(3)
+\frac{1.5(0.5)}{2}(2)=6.25.
$$

The independent coefficient form \(1+2x+x^2=(x+1)^2\) gives the same value and is a useful check. Substitution at all four nodes reproduces the table, while the vanishing third difference is consistent with the data coming from a quadratic.

### What the difference table does and does not establish

For equally spaced data generated by a polynomial of degree \(m\), the \(m\)-th differences are constant and the next differences vanish in exact arithmetic. Measured values may be rounded, so a table can show small nonzero higher differences even when a lower-degree trend is plausible. Do not declare an exact degree from noisy decimal data without considering the precision of the ordinates. Also do not use the equal-spacing forward formula for nonuniform nodes: the divided-difference construction is the corresponding Newton approach when the node spacing varies.

The forward form is most convenient near the beginning of a table, where \(x\) is represented relative to \(x_0\). Near the final node, the backward form organizes terms relative to the endpoint and uses backward differences. These are not competing interpolating polynomials; they are different representations of the same polynomial determined by the nodes and values. Agreement at a test point is a strong arithmetic check. If two correctly formed representations disagree, inspect the difference-table indexing, the factorial denominator, and the definition of the normalized variable before changing the data.

### Distinguishing exact fit from reliable prediction

In the example, four data points determine a polynomial of degree at most three in general, but the difference table reveals that the particular data fit a quadratic. The model exactly reproduces the four ordinates, yet the value \(6.25\) at \(1.5\) remains a prediction. Its reliability depends on whether the underlying quantity is well represented by a low-degree polynomial over that interval and on the accuracy of the tabulated ordinates. Interpolation is appropriate for a target bracketed by the nodes; evaluating the same polynomial beyond \(x=3\) is extrapolation and can magnify small data or coefficient changes.

For an exam response, show the nodes and spacing first, construct differences with the operation stated, write the formula in the matching convention, substitute the normalized coordinate, and verify against at least one original data value. Finish by identifying the model's limitation. This sequence gives a marker evidence of method selection, not just a final decimal.
