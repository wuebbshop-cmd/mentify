## 1. Foundational Concepts, Definitions, and Axioms

### 1.1 Why an infinite series is the right instrument here

Every method studied so far produced solutions built from a short list of elementary functions: exponentials, sines, cosines, polynomials, logarithms and their combinations. That list is adequate only while the coefficients of the equation are constants, or while the equation happens to be one of the few variable-coefficient types that admit a closed-form trick. Coefficients that vary with the independent variable generally destroy all of this. The equation

$$
\frac{d^{2}y}{dx^{2}}+x^{2}y=0
$$

has no solution expressible in elementary functions, and no amount of ingenuity will produce one. The remedy is to widen the class of acceptable answers: instead of demanding a finite combination of named functions, one accepts an infinite series and treats that series as the answer. This is the power series method, and it is the only general method available for linear equations with variable coefficients.

> **Definition (Power series solution).** Let $x_{0}$ be a real number and let $C_{0},C_{1},C_{2},\dots$ be constants. A power series solution of a differential equation about the point $x_{0}$ is a function
>
> $$
> y=\sum_{n=0}^{\infty}C_{n}\left(x-x_{0}\right)^{n}
> $$
>
> which converges on some interval $\left|x-x_{0}\right|<R$ with $R>0$ and which satisfies the differential equation at every point of that interval.

Each symbol deserves a word. The letter $n$ is the summation index, a whole number that runs upward from zero without end. The letter $C_{n}$ is the coefficient of the $n$-th term, a fixed number once the solution has been found. The number $x_{0}$ is the centre of expansion, the point about which the powers are taken. The expression $\left(x-x_{0}\right)^{n}$ is the $n$-th power of the distance from the centre, so the series is a polynomial in a shifted variable. The letter $R$ is the radius of convergence, the distance within which the infinite sum adds up to a finite number.

The word solution carries its usual meaning: substituting the series into the equation must produce an identity, not merely an approximation. Truncating the series after finitely many terms produces an approximation, and approximations are not solutions.

The method has a fixed shape, and it is worth stating the shape before any of the theory, because the theory exists only to answer the question of when the shape is legitimate.

1. Assume the solution has the form of a power series about the chosen centre, with unknown coefficients.
2. Differentiate the series term by term as many times as the equation requires.
3. Substitute the series and its derivatives into the equation.
4. Shift summation indices until every term carries the same power of $\left(x-x_{0}\right)$.
5. Equate the total coefficient of each power to zero, obtaining a recurrence relation for the coefficients.
6. Solve the recurrence, identify the two arbitrary constants, and state the radius of convergence.

A short run through the method shows how it works and how much bookkeeping it demands. Take the constant-coefficient equation

$$
\frac{d^{2}y}{dx^{2}}+y=0 .
$$

Assume $y=\sum_{n=0}^{\infty}C_{n}x^{n}$ about the centre $x_{0}=0$. Differentiating twice gives

$$
\frac{d^{2}y}{dx^{2}}=\sum_{n=2}^{\infty}n(n-1)C_{n}x^{n-2},
$$

where the sum starts at $n=2$ because the first two terms of $y$ are constant and linear, and differentiating them twice removes them. Substituting into the equation gives

$$
\sum_{n=2}^{\infty}n(n-1)C_{n}x^{n-2}+\sum_{n=0}^{\infty}C_{n}x^{n}=0 .
$$

Put $m=n-2$ in the first sum, so that it becomes a sum over powers $x^{m}$ with $m\ge0$:

$$
\sum_{m=0}^{\infty}(m+2)(m+1)C_{m+2}x^{m}+\sum_{m=0}^{\infty}C_{m}x^{m}=0 .
$$

Since the two sums now run over the same powers, the total coefficient of $x^{m}$ must vanish for every $m$, which gives the recurrence

$$
C_{m+2}=-\frac{C_{m}}{(m+2)(m+1)} .
$$

The recurrence relates each coefficient to the one two places before it, so the even coefficients are determined by $C_{0}$ and the odd coefficients by $C_{1}$, and those two numbers remain free. Choosing $C_{0}=1$ and $C_{1}=0$ produces

$$
y=1-\frac{x^{2}}{2!}+\frac{x^{4}}{4!}-\cdots=\cos x ,
$$

and choosing $C_{0}=0$ and $C_{1}=1$ produces

$$
y=x-\frac{x^{3}}{3!}+\frac{x^{5}}{5!}-\cdots=\sin x .
$$

Two free constants for a second-order equation, exactly as the order demands. The series converge for every $x$, and their sum is the known general solution.

Nothing in that computation depended on the coefficients being constant, and that is the point. The same six steps apply to equations with variable coefficients. What the six steps do not settle is whether the assumed form is available at the chosen centre. At some centres the assumption is guaranteed to succeed and produces two independent series. At other centres only a modified form works, and at a third class of centres nothing at all is guaranteed. Distinguishing those three cases is the subject of the rest of this note, and it rests on one property of the coefficient functions.

### 1.2 Analytic functions at a point

The property that decides everything is analyticity, and it is a statement about a function near a single point.

> **Definition (Analytic at a point).** A function $f$ is analytic at the point $x_{0}$ if there exist a number $R>0$ and constants $a_{0},a_{1},a_{2},\dots$ such that
>
> $$
> f(x)=\sum_{n=0}^{\infty}a_{n}\left(x-x_{0}\right)^{n}
> $$
>
> for every $x$ satisfying $\left|x-x_{0}\right|<R$.

In words: near $x_{0}$, and on a genuine interval around it, the function equals its own Taylor series about $x_{0}$. The coefficients are forced, not chosen; they are

$$
a_{n}=\frac{f^{(n)}(x_{0})}{n!},
$$

so a function has at most one power series about a given centre, and analyticity says that this unique series actually reconverges to the function.

> **Definition (Analytic on a set).** A function is analytic on an open interval if it is analytic at every point of that interval. A function analytic at every real number is called entire.

Three immediate consequences are used constantly. A function analytic at $x_{0}$ is continuous at $x_{0}$, hence has a finite value there. A function analytic at $x_{0}$ is automatically analytic at every point of some neighbourhood of $x_{0}$, because the same series serves throughout its interval of convergence. And the class of analytic functions is closed under addition, multiplication, composition, and division by a denominator that does not vanish, so every rational function is analytic wherever its denominator is nonzero.

Two tempting shortcuts are false, and both cause errors in classification questions.

The first is the claim that a function with one derivative at $x_{0}$ is analytic there. It is not. The function $f(x)=x\left|x\right|$ is differentiable at $0$, with $f'(0)=0$, but it has no second derivative at $0$, so no power series about $0$ can represent it.

The second is the claim that a function is analytic at $x_{0}$ provided it does not become infinite there. That is also false. The function defined by $f(0)=0$ and $f(x)=e^{-1/x^{2}}$ for $x\neq0$ is finite at $0$ and even infinitely differentiable there, with every derivative equal to zero at the origin; its Taylor series about $0$ is therefore the zero series, which does not reproduce the function for $x\neq0$. Such a function is said to be flat at the origin and is not analytic there.

What is true is the implication in one direction only: analytic at $x_{0}$ implies finite and continuous at $x_{0}$. A function that becomes infinite at $x_{0}$ therefore fails to be analytic there, and this single observation already identifies most singular points of the equations in this course.

The practical test for analyticity is the power series representation itself, and the practical question attached to it is the size of the radius of convergence.

> **Definition (Radius of convergence).** For the series $\sum_{n=0}^{\infty}a_{n}t^{n}$, the radius of convergence is the number $R$, possibly infinite, such that the series converges absolutely for $\left|t\right|<R$ and diverges for $\left|t\right|>R$.

> **Test (Ratio test for the radius).** If the coefficients are eventually nonzero and the limit
>
> $$
> R=\lim_{n\to\infty}\left|\frac{a_{n}}{a_{n+1}}\right|
> $$
>
> exists, then it is the radius of convergence.

Four standard expansions illustrate the test and the geometry behind it.

The geometric series

$$
\frac{1}{1-x}=\sum_{n=0}^{\infty}x^{n}
$$

has all coefficients equal to one, so the ratio is one and $R=1$. The function blows up at $x=1$, at distance one from the centre $0$.

The exponential

$$
e^{x}=\sum_{n=0}^{\infty}\frac{x^{n}}{n!}
$$

has $\left|a_{n}/a_{n+1}\right|=n+1\to\infty$, so $R=\infty$, consistent with a function that is finite everywhere.

The function

$$
\frac{1}{1+x^{2}}=\sum_{n=0}^{\infty}(-1)^{n}x^{2n}
$$

is finite for every real $x$, yet its series about $0$ has radius $1$. Comparing the nonzero coefficients gives $\left|a_{2n}/a_{2n+2}\right|=1$, so $R=1$. The restriction is invisible on the real axis and is caused by the two poles at $x=i$ and $x=-i$, each at distance one from the origin in the complex plane.

The binomial series

$$
\sqrt{1+x}=1+\frac{1}{2}x-\frac{1}{8}x^{2}+\frac{1}{16}x^{3}-\cdots
$$

has radius one about $0$, the distance to the branch point at $x=-1$.

The pattern in these four examples is general and is used later to predict radii: the radius of convergence of the expansion about $x_{0}$ equals the distance from $x_{0}$ to the nearest point where the function ceases to be analytic, measured in the complex plane. For equations with polynomial coefficients this distance is simply the distance to the nearest singular point of the equation.

### 1.3 The normalised form of a second-order equation

Classification is defined for one standard shape only, so every equation must first be forced into that shape.

> **Definition (Normalised form).** Let
>
> $$
> a_{0}(x)\frac{d^{2}y}{dx^{2}}+a_{1}(x)\frac{dy}{dx}+a_{2}(x)y=0
> $$
>
> be a second-order linear homogeneous equation with $a_{0}(x)\neq0$ on the interval under consideration. Dividing every term by $a_{0}(x)$ produces
>
> $$
> \frac{d^{2}y}{dx^{2}}+P(x)\frac{dy}{dx}+Q(x)y=0,
> $$
>
> with
>
> $$
> P(x)=\frac{a_{1}(x)}{a_{0}(x)}, \qquad Q(x)=\frac{a_{2}(x)}{a_{0}(x)} .
> $$
>
> This is the normalised form, and in it the coefficient of the second derivative is unity.

The symbols read as follows. The function $a_{0}$ multiplies the second derivative and is assumed nonzero wherever the equation is being studied; the functions $a_{1}$ and $a_{2}$ multiply the first derivative and the unknown function. The functions $P$ and $Q$ are the quotients, and they carry every feature that the classification uses. The name normalised refers to the unit coefficient on $\frac{d^{2}y}{dx^{2}}$ and to nothing else.

A worked normalisation fixes the mechanics. Take

$$
\left(x^{2}-1\right)\frac{d^{2}y}{dx^{2}}+3x\frac{dy}{dx}+xy=0 .
$$

The coefficient of the second derivative vanishes at $x=1$ and at $x=-1$, so the normalised equation is meaningful on the three intervals cut out by those points. On any one of them, division by $x^{2}-1$ gives

$$
\frac{d^{2}y}{dx^{2}}+\frac{3x}{x^{2}-1}\frac{dy}{dx}+\frac{x}{x^{2}-1}y=0,
$$

so that

$$
P(x)=\frac{3x}{x^{2}-1}, \qquad Q(x)=\frac{x}{x^{2}-1} .
$$

Both quotients are rational functions whose only bad points are $x=1$ and $x=-1$, and those two numbers are exactly the candidates for singular behaviour.

The order of operations matters. Division by $a_{0}$ is performed first, and the classification is then read off $P$ and $Q$. Reading the classification off $a_{0}$, $a_{1}$ and $a_{2}$ directly is a reliable way to obtain the wrong answer, because cancellation between numerator and denominator can remove a singularity that the raw coefficients appear to show.

### 1.4 Ordinary points and singular points

> **Definition (Ordinary point).** The point $x_{0}$ is an ordinary point of the normalised equation $y''+P(x)y'+Q(x)y=0$ if both $P$ and $Q$ are analytic at $x_{0}$.

> **Definition (Singular point).** The point $x_{0}$ is a singular point of the normalised equation if it is not an ordinary point, that is, if at least one of $P$ and $Q$ fails to be analytic at $x_{0}$.

The definitions are exact negations of one another, so every point of the interval is either ordinary or singular, never both and never neither. The word regular in the phrase regular singular point is a further subdivision of the singular case and does not create a third possibility at this level.

Two examples fix the meaning. The equation

$$
\frac{d^{2}y}{dx^{2}}+(x-2)\frac{dy}{dx}+\left(x^{2}+1\right)y=0
$$

is already normalised, with $P(x)=x-2$ and $Q(x)=x^{2}+1$. Both are polynomials, hence analytic at every real number, so the equation has no singular points at all and every point is ordinary. The equation

$$
\left(x^{2}-1\right)\frac{d^{2}y}{dx^{2}}+3x\frac{dy}{dx}+xy=0
$$

has $P(x)=\frac{3x}{x^{2}-1}$ and $Q(x)=\frac{x}{x^{2}-1}$, and both quotients become infinite at $x=1$ and at $x=-1$. Those two numbers are singular points; every other real number is an ordinary point.

A warning is needed here, because it is the most common conceptual error in this topic. A root of the coefficient $a_{0}$ is a candidate for a singular point, not a proof of one. Consider

$$
\left(x^{2}-1\right)\frac{d^{2}y}{dx^{2}}+(x-1)\frac{dy}{dx}=0 .
$$

The coefficient of the second derivative vanishes at $x=1$, yet after division

$$
P(x)=\frac{x-1}{x^{2}-1}=\frac{1}{x+1}, \qquad Q(x)=0
$$

for $x\neq1$, and the quotient $\frac{1}{x+1}$ extends to an analytic function at $x=1$ with value $\frac{1}{2}$. The function $P$ is therefore analytic at $x=1$, and $x=1$ is an ordinary point despite being a root of $a_{0}$. The root was spurious because the same factor appeared in the numerator. Conversely, an equation may have singular points that are not roots of $a_{0}$ at all, for instance when $a_{1}$ itself contains a singularity, as in

$$
\frac{d^{2}y}{dx^{2}}+\frac{1}{x-3}\frac{dy}{dx}+y=0 ,
$$

where $x=3$ is singular although $a_{0}=1$ never vanishes.

### 1.5 Regular singular points and irregular singular points

Singular points are not all equally severe, and the severity is measured by how fast the coefficients blow up.

> **Definition (Regular singular point).** Let $x_{0}$ be a singular point of $y''+P(x)y'+Q(x)y=0$. Then $x_{0}$ is a regular singular point if both of the functions
>
> $$
> \left(x-x_{0}\right)P(x) \qquad \text{and} \qquad \left(x-x_{0}\right)^{2}Q(x)
> $$
>
> are analytic at $x_{0}$.

> **Definition (Irregular singular point).** A singular point is irregular if it is not regular, that is, if at least one of $\left(x-x_{0}\right)P(x)$ and $\left(x-x_{0}\right)^{2}Q(x)$ fails to be analytic at $x_{0}$.

The two multipliers do different work. Multiplying $P$ by one factor of $\left(x-x_{0}\right)$ cancels a simple pole, so a coefficient $P$ that blows up like $\frac{1}{x-x_{0}}$ passes the first test, while a coefficient that blows up like $\frac{1}{\left(x-x_{0}\right)^{2}}$ fails it. Multiplying $Q$ by two factors cancels a double pole, so a coefficient $Q$ that blows up like $\frac{1}{\left(x-x_{0}\right)^{2}}$ passes the second test, while one that blows up like $\frac{1}{\left(x-x_{0}\right)^{3}}$ fails it.

Analyticity of these products is equivalent to a pair of finite limits, and the limit version is what one actually computes.

> **Test (Limit form of the regularity tests).** Let $x_{0}$ be a singular point. Then $x_{0}$ is a regular singular point if and only if both limits
>
> $$
> \lim_{x\to x_{0}}\left(x-x_{0}\right)P(x), \qquad \lim_{x\to x_{0}}\left(x-x_{0}\right)^{2}Q(x)
> $$
>
> exist and are finite.

The equivalence is the removable singularity principle: a function that is analytic on a punctured neighbourhood of $x_{0}$ extends analytically to $x_{0}$ exactly when it has a finite limit there. A finite limit therefore means that the product has a removable discontinuity, and filling the gap produces an analytic function.

Both limits must be finite. A single infinite limit is enough to make the point irregular, and there is no compensation between the two tests: success in one never rescues failure in the other.

The reason these particular powers appear is visible in advance. If $x_{0}$ is regular, write $t=x-x_{0}$ and let $P$ behave like $\frac{p_{0}}{t}$ and $Q$ behave like $\frac{q_{0}}{t^{2}}$ to leading order. A solution of the shape $y=t^{r}$ then gives $y''\sim r(r-1)t^{r-2}$, $Py'\sim p_{0}rt^{r-2}$ and $Qy\sim q_{0}t^{r-2}$, and all three terms carry the same power $t^{r-2}$. The three contributions can balance, which is exactly what a solution requires. If $P$ behaved like $\frac{1}{t^{2}}$ instead, the term $Py'$ would carry power $t^{r-3}$ and no choice of the other terms could cancel it. The powers one and two are therefore not conventions; they are the only powers at which the equation is balanced order by order.

### 1.6 The three kinds of point, side by side

The definitions are short, and a table makes the whole classification visible at once. In the table, $t$ abbreviates $x-x_{0}$, and the word analytic always means analytic at $x_{0}$.

| Nature of $x_{0}$ | Condition on $P$ and $Q$ | Solution guaranteed near $x_{0}$ | Standard illustration |
| --- | --- | --- | --- |
| Ordinary | $P$ and $Q$ both analytic | two independent series $\sum C_{n}t^{n}$ | $y''+xy=0$ at $x_{0}=0$ |
| Regular singular | $x_{0}$ singular, $tP$ and $t^{2}Q$ both analytic | at least one series $\sum C_{n}t^{n+r}$ | $2x^{2}y''-xy'+(x-5)y=0$ at $x_{0}=0$ |
| Irregular singular | $x_{0}$ singular, $tP$ or $t^{2}Q$ not analytic | nothing guaranteed | $x^{2}y''+y'+y=0$ at $x_{0}=0$ |

The third row is not a statement that no solution exists; it is a statement that the theory of this lesson makes no promise. An irregular singular point may admit a convergent series solution, may admit none in the permitted form, and may require solutions with exponential factors such as $e^{1/t}$ that no power series can represent.

The table also shows why the tests are arranged in the order they are. One first normalises, then locates the singular points, and only then asks whether a singular point is regular. Applying the two products at a point that is not singular is meaningless as a classification, because at an ordinary point both products are automatically analytic and every ordinary point would be misreported as regular singular. The tests presuppose that the point has already been shown to be singular.

## 2. Theorems, Lemmas, and Analytical Properties

### 2.1 Closure properties of analytic functions

The classification is applied to quotients such as $\frac{a_{1}}{a_{0}}$, so the first facts needed are the ones that allow analyticity to be recognised without expanding a series on every occasion.

> **Theorem (Closure).** Let $f$ and $g$ be analytic at $x_{0}$. Then $f+g$, $fg$ and, for any real constant $\lambda$, the multiple $\lambda f$ are analytic at $x_{0}$. If in addition $g(x_{0})\neq0$, then $\frac{f}{g}$ is analytic at $x_{0}$. If $h$ is analytic at $f(x_{0})$, then the composite $h\circ f$ is analytic at $x_{0}$.

The proof is the algebra of convergent power series carried out inside the smaller of the two intervals of convergence. Every polynomial is analytic at every point, because a polynomial is its own Taylor series about any centre. Every rational function is analytic at every point where its denominator does not vanish, by repeated use of the quotient statement.

> **Theorem (Reciprocal of a nonzero analytic function).** If $g$ is analytic at $x_{0}$ and $g(x_{0})\neq0$, then on some neighbourhood of $x_{0}$ the reciprocal $\frac{1}{g}$ is analytic, and its series about $x_{0}$ has radius at least the distance from $x_{0}$ to the nearest zero of $g$ in the complex plane.

This last clause is the quantitative half of the theorem, and it is what allows radii of convergence to be predicted without computing coefficients. A zero of the denominator is a point where the reciprocal cannot be analytic, and no expansion can reach past it.

### 2.2 The classification theorem

> **Theorem (Trichotomy of points).** Let $P$ and $Q$ be real functions which are analytic on a punctured neighbourhood of $x_{0}$, so that the normalised equation $y''+P(x)y'+Q(x)y=0$ is defined on that punctured neighbourhood. Then $x_{0}$ is exactly one of the following: an ordinary point, a regular singular point, or an irregular singular point.

The hypotheses matter. Analyticity on a punctured neighbourhood is what makes "singular" a meaningful label, and it holds automatically whenever the original coefficients $a_{0},a_{1},a_{2}$ are analytic and $a_{0}$ has an isolated zero at $x_{0}$. If $a_{0}$ vanished on a whole interval, or if $P$ failed to be analytic at points accumulating at $x_{0}$, the three labels would not exhaust the possibilities and the theory of this lesson would not apply.

The theorem is a tautology in structure and a theorem in content. It is a tautology because ordinary and singular are defined as negations, and regular and irregular are defined as negations within the singular case, so exactly one label always attaches. The content lies in the accompanying criteria, which turn the abstract labels into computations with limits and which guarantee that the regular case is genuinely less severe than the irregular one.

> **Theorem (Pole-order criterion).** Let $P$ and $Q$ be analytic on the punctured disc $0<\left|x-x_{0}\right|<\rho$. Then $x_{0}$ is a regular singular point of $y''+P(x)y'+Q(x)y=0$ if and only if $P$ has a pole of order at most one at $x_{0}$ and $Q$ has a pole of order at most two at $x_{0}$.

In the language of limits the same statement reads as follows.

> **Corollary (Computational form).** With the same hypotheses, $x_{0}$ is regular singular if and only if both numbers
>
> $$
> p_{0}=\lim_{x\to x_{0}}\left(x-x_{0}\right)P(x), \qquad q_{0}=\lim_{x\to x_{0}}\left(x-x_{0}\right)^{2}Q(x)
> $$
>
> exist and are finite.

The numbers $p_{0}$ and $q_{0}$ are not decoration. They are the leading Laurent coefficients of $P$ and $Q$, and they alone decide the exponents that the solutions can carry near $x_{0}$.

### 2.3 The existence theorem for ordinary points

> **Theorem (Ordinary-point existence).** Suppose $x_{0}$ is an ordinary point of $y''+P(x)y'+Q(x)y=0$, so that $P$ and $Q$ are analytic at $x_{0}$. Then the equation possesses two solutions
>
> $$
> y_{1}=\sum_{n=0}^{\infty}C_{n}\left(x-x_{0}\right)^{n}, \qquad y_{2}=\sum_{n=0}^{\infty}D_{n}\left(x-x_{0}\right)^{n}
> $$
>
> which are linearly independent and analytic at $x_{0}$. Every solution of the equation on the common interval of convergence is a linear combination $Ay_{1}+By_{2}$. The radius of convergence of each series is at least the distance from $x_{0}$ to the nearest singular point of the equation in the complex plane.

Three features of the statement carry the marks in an examination.

The first is the word two. At an ordinary point a full basis is guaranteed, so the general solution is a two-parameter family of power series. Nothing is lost and no logarithmic or fractional-power modification is needed.

The second is the word analytic. The solutions are not merely convergent series; they extend to analytic functions at $x_{0}$ itself, so they have finite values and all derivatives at the centre. This is the sharpest contrast with the regular singular case, where solutions typically blow up at the centre.

The third is the radius clause. The guarantee is local, and its size is governed by the distance to the nearest singular point. For Legendre's equation about $x_{0}=0$ the singular points are $\pm1$, so every power series solution about the origin converges at least for $\left|x\right|<1$ and may fail beyond that, even though the coefficients are perfectly well defined for larger $x$.

### 2.4 The existence theorem for regular singular points

> **Theorem (Frobenius existence).** Suppose $x_{0}$ is a regular singular point of $y''+P(x)y'+Q(x)y=0$, with $P$ and $Q$ analytic on $0<\left|x-x_{0}\right|<\rho$. Then the equation possesses at least one nontrivial solution of the form
>
> $$
> y=\left(x-x_{0}\right)^{r}\sum_{n=0}^{\infty}C_{n}\left(x-x_{0}\right)^{n}, \qquad C_{0}\neq0,
> $$
>
> valid on the punctured interval $0<\left|x-x_{0}\right|<R$ for some $R>0$. The exponent $r$ is a root of the indicial equation
>
> $$
> r(r-1)+p_{0}r+q_{0}=0,
> $$
>
> where $p_{0}$ and $q_{0}$ are the finite limits of the regularity tests.

> **Theorem (Second solution at a regular singular point).** With the same hypotheses, let $r_{1}$ and $r_{2}$ be the roots of the indicial equation, ordered so that $\operatorname{Re}r_{1}\ge\operatorname{Re}r_{2}$. If $r_{1}-r_{2}$ is not an integer, then the equation has two independent solutions of Frobenius form, one for each exponent. If $r_{1}-r_{2}$ is an integer, a second independent solution exists in the form
>
> $$
> y_{2}=Cy_{1}\ln\left(x-x_{0}\right)+\left(x-x_{0}\right)^{r_{2}}\sum_{n=0}^{\infty}D_{n}\left(x-x_{0}\right)^{n},
> $$
>
> where $C$ may be zero when the larger exponent itself produces two independent series.

The logarithm is not a defect of the method; it is the genuine behaviour of the second solution. The equation $x^{2}y''+3xy'+y=0$ has indicial equation $\left(r+1\right)^{2}=0$, a double root, and its two solutions are $x^{-1}$ and $x^{-1}\ln x$. Both are unbounded at the origin, and the logarithm is what distinguishes them.

The theorem is deliberately weaker than the ordinary-point theorem in two respects. It promises only one series solution for free, and it allows the exponent $r$ to be negative, fractional or complex, so the solution need not be defined at $x_{0}$ at all. That is why the interval of validity is written as a deleted interval.

> **Lemma (Indicial equation).** Let $x_{0}$ be a regular singular point and write $t=x-x_{0}$. If $y=t^{r}\sum_{n=0}^{\infty}C_{n}t^{n}$ with $C_{0}\neq0$ solves the equation, then $r$ satisfies $r(r-1)+p_{0}r+q_{0}=0$.

The lemma converts a statement about the existence of a solution into a quadratic whose roots can be computed in advance. It is derived in Section 3.4.

### 2.5 The absence of a guarantee at an irregular singular point

> **Theorem (Irregular singular points).** If $x_{0}$ is an irregular singular point of the normalised equation, then no solution of Frobenius form is guaranteed. The equation may possess a convergent series of that form, it may possess none, and it may possess solutions whose behaviour near $x_{0}$ is more violent than any power of $\left(x-x_{0}\right)$ can describe.

The reason the guarantee is lost is structural, and it is worth stating precisely because it explains why no substitute theorem exists. At a regular singular point the three terms $t^{2}y''$, $t^{2}Py'$ and $t^{2}Qy$ all carry the same lowest power $t^{r}$, so the equation can be balanced and the unknown exponent is determined by one quadratic. At an irregular singular point at least one of the products $tP$ and $t^{2}Q$ still blows up, so the three terms carry different lowest powers, the lowest of them cannot be cancelled, and no exponent can be extracted by the same device. The equation may still be balanced if the unbounded parts cancel one another in a more complicated way, which is why an irregular point sometimes admits a formal series; but such a series is a formal object whose convergence must be investigated separately, and frequently its radius of convergence is zero.

What the classification does guarantee is negative and useful: the solution cannot be assumed to have either of the two forms that the earlier theorems supply, and any answer that asserts such a form without further argument is unjustified. Solutions near an irregular singular point often involve factors such as $\exp\left(\frac{1}{x-x_{0}}\right)$, which have essential singularities there and which no power series can represent. The honest conclusion of a classification question is therefore that the point is irregular and that the existence of a power series solution is not assured.

### 2.6 Classification of the three standard equations

Three equations recur throughout the subject, and their classifications are worth recording as theorems because they are quoted constantly.

> **Theorem (Legendre's equation).** For the equation
>
> $$
> \left(1-x^{2}\right)\frac{d^{2}y}{dx^{2}}-2x\frac{dy}{dx}+p(p+1)y=0
> $$
>
> with $p$ a real constant, every point other than $x=1$ and $x=-1$ is an ordinary point, and $x=1$ and $x=-1$ are regular singular points. The point at infinity is also a regular singular point.

> **Theorem (Bessel's equation).** For the equation
>
> $$
> x^{2}\frac{d^{2}y}{dx^{2}}+x\frac{dy}{dx}+\left(x^{2}-n^{2}\right)y=0
> $$
>
> with $n$ a non-negative constant, every nonzero point is an ordinary point and $x=0$ is a regular singular point, with indicial exponents $r=n$ and $r=-n$.

> **Theorem (Hypergeometric equation).** For the equation
>
> $$
> x(1-x)\frac{d^{2}y}{dx^{2}}+\left[c-(a+b+1)x\right]\frac{dy}{dx}-aby=0
> $$
>
> with constants $a$, $b$ and $c$, where $c$ is not an integer, the points $x=0$ and $x=1$ are regular singular points and every other finite point is ordinary. The indicial exponents at $x=0$ are $0$ and $1-c$.

Each of these three statements is proved by direct computation in Section 4. The phrase regular singular point is not a description of difficulty in general; for all three equations the solutions are perfectly well behaved on the intervals between the singular points, and the singular points merely mark where the series expansions must change their exponents or acquire logarithms.

### 2.7 Consequences for the shape of the general solution

The three theorems combine into a decision procedure with an immediate payoff, because the nature of the point dictates the ansatz.

At an ordinary point the correct assumption is a plain power series; the general solution is a two-parameter family of such series and no constant term outside the series is needed.

At a regular singular point the correct assumption is a power series multiplied by $\left(x-x_{0}\right)^{r}$; the exponent is found from a quadratic, and the general solution may require one logarithmic term.

At an irregular singular point no assumption of either kind is justified, and any series obtained must be examined for convergence rather than assumed to converge.

This is the practical content of the whole lesson. The classification is not an end in itself; it selects the form of the answer before any coefficient has been computed.

## 3. Formal Proofs, Derivations, and Methods

### 3.1 Derivation of the pole-order criterion

The criterion is a statement about Laurent expansions. Suppose $P$ is analytic on the punctured disc $0<\left|t\right|<\rho$, where $t=x-x_{0}$. Then $P$ has a Laurent expansion there,

$$
P(t)=\sum_{k=-\infty}^{\infty}b_{k}t^{k},
$$

in which only finitely many negative powers appear, because the singularity at the origin is isolated. Multiplying by one power of $t$ shifts every exponent upward by one:

$$
tP(t)=\sum_{k=-\infty}^{\infty}b_{k}t^{k+1}.
$$

The product $tP$ is analytic at the origin precisely when its Laurent expansion contains no negative powers. That happens precisely when $b_{k}=0$ for every $k\le-2$, which is precisely the statement that the principal part of $P$ consists of at most the single term $\frac{b_{-1}}{t}$. In that case $P$ has a pole of order at most one, and

$$
p_{0}=\lim_{t\to0}tP(t)=b_{-1}.
$$

The same argument applied to $Q$ with two factors gives

$$
t^{2}Q(t)=\sum_{k=-\infty}^{\infty}d_{k}t^{k+2},
$$

which is analytic at the origin precisely when $d_{k}=0$ for every $k\le-3$, that is, when the principal part of $Q$ is at most $\frac{d_{-2}}{t^{2}}+\frac{d_{-1}}{t}$. In that case $Q$ has a pole of order at most two and

$$
q_{0}=\lim_{t\to0}t^{2}Q(t)=d_{-2}.
$$

Combining the two computations, the pair of products is analytic at the origin exactly when the pole orders of $P$ and $Q$ are at most one and at most two respectively. That is the criterion.

### 3.2 Derivation of the limit form

Let $f$ be analytic on $0<\left|t\right|<\rho$ and suppose $\lim_{t\to0}f(t)=L$ exists and is finite. Define $F(0)=L$ and $F(t)=f(t)$ for $t\neq0$. The function $F$ is continuous at the origin by construction, and it is analytic off the origin by hypothesis. A function analytic on a punctured disc and continuous at the centre is analytic at the centre, because its Laurent expansion has no negative powers: a negative power $\frac{b_{-k}}{t^{k}}$ would force $\left|f(t)\right|\to\infty$ along the approach to the origin, contradicting the finite limit. Hence $F$ is analytic at the origin and $f$ has a removable singularity there.

Conversely, if $f$ extends analytically to the origin, then $f$ is continuous there and the finite limit exists. The two formulations are therefore equivalent, and either may be used in a computation.

One consequence deserves emphasis. If $\lim_{t\to0}tP(t)$ does not exist or is infinite, then $tP$ is not analytic at the origin, so the first test fails and the point is irregular. There is no way in which a successful second test can repair that failure, because the two products are examined separately.

### 3.3 Why the tests presuppose a singular point

> **Proposition.** If $x_{0}$ is an ordinary point of the normalised equation, then both $\left(x-x_{0}\right)P(x)$ and $\left(x-x_{0}\right)^{2}Q(x)$ are analytic at $x_{0}$.

The proof is one line. The function $x-x_{0}$ is a polynomial, hence analytic everywhere, and the product of two functions analytic at a point is analytic at that point. Applying this to $P$ and to $Q$ gives the claim.

The proposition explains a persistent confusion. If the two tests are applied blindly at every point, then every ordinary point passes them, and a student who reports "the point is regular singular because both limits are finite" will classify all points as regular singular and never notice the error. The tests are meaningful only after the point has been shown to be singular, which is why the procedure of Section 3.6 puts normalisation and location of singular points before classification.

### 3.4 Derivation of the indicial equation

Let $x_{0}$ be a regular singular point and put $t=x-x_{0}$. By the criterion, the two products are analytic, so $P$ and $Q$ can be written as

$$
P(t)=\frac{p_{0}}{t}+P_{1}(t), \qquad Q(t)=\frac{q_{0}}{t^{2}}+\frac{q_{1}}{t}+Q_{1}(t),
$$

with $P_{1}$ and $Q_{1}$ analytic at the origin. Assume a solution of the form

$$
y=t^{r}\sum_{n=0}^{\infty}C_{n}t^{n}, \qquad C_{0}\neq0,
$$

which is precisely the Frobenius ansatz. Its derivatives are

$$
\frac{dy}{dt}=\sum_{n=0}^{\infty}(n+r)C_{n}t^{n+r-1}, \qquad \frac{d^{2}y}{dt^{2}}=\sum_{n=0}^{\infty}(n+r)(n+r-1)C_{n}t^{n+r-2}.
$$

Multiplying the whole equation by $t^{2}$ clears the two powers of $t$ that the singular terms would otherwise contribute, which is the reason those particular powers appear in the tests. The three terms become

$$
t^{2}\frac{d^{2}y}{dt^{2}}=\sum_{n=0}^{\infty}(n+r)(n+r-1)C_{n}t^{n+r},
$$

$$
t^{2}P(t)\frac{dy}{dt}=\left(p_{0}t+t^{2}P_{1}(t)\right)\sum_{n=0}^{\infty}(n+r)C_{n}t^{n+r-1}=\sum_{n=0}^{\infty}p_{0}(n+r)C_{n}t^{n+r}+\cdots
$$

and

$$
t^{2}Q(t)y=\left(q_{0}+q_{1}t+t^{2}Q_{1}(t)\right)\sum_{n=0}^{\infty}C_{n}t^{n+r}=\sum_{n=0}^{\infty}q_{0}C_{n}t^{n+r}+\cdots ,
$$

where the ellipses hide terms carrying powers $t^{n+r+1}$ and higher. Only the lowest power, namely $t^{r}$, survives when $n=0$, and its coefficient must vanish:

$$
C_{0}\left[r(r-1)+p_{0}r+q_{0}\right]=0 .
$$

Since $C_{0}\neq0$ by assumption, the bracket must vanish, which is the indicial equation. Equating the coefficient of $t^{r+1}$ to zero then determines $C_{1}$ in terms of $C_{0}$, and each further power determines the next coefficient, so the whole series is fixed up to the single constant $C_{0}$.

The mechanism is easiest to see in the Euler equation, where $P_{1}$ and $Q_{1}$ vanish identically:

$$
t^{2}\frac{d^{2}y}{dt^{2}}+p_{0}t\frac{dy}{dt}+q_{0}y=0 .
$$

Substituting $y=t^{r}$ gives

$$
\left[r(r-1)+p_{0}r+q_{0}\right]t^{r}=0,
$$

so a pure power solves the Euler equation exactly when $r$ is a root of the indicial quadratic, and the two roots give the two independent powers $t^{r_{1}}$ and $t^{r_{2}}$ whenever they differ.

### 3.5 Derivation of the coefficient recurrence at an ordinary point

The recurrence that the ordinary-point theorem relies on can be written down in general form, and doing so shows exactly where the two free constants come from.

Let $x_{0}$ be an ordinary point and put $t=x-x_{0}$. The coefficient functions have power series

$$
P(t)=\sum_{k=0}^{\infty}p_{k}t^{k}, \qquad Q(t)=\sum_{k=0}^{\infty}q_{k}t^{k},
$$

both convergent at least for $\left|t\right|<\rho$, where $\rho$ is the distance to the nearest singular point. Seek a solution $y=\sum_{n=0}^{\infty}c_{n}t^{n}$. The three ingredients of the normalised equation then have the following coefficient of $t^{n}$:

$$
\left(\frac{d^{2}y}{dt^{2}}\right)_{n}=(n+2)(n+1)c_{n+2},
$$

$$
\left(P\frac{dy}{dt}\right)_{n}=\sum_{k=0}^{n}(n-k+1)p_{k}c_{n-k+1},
$$

$$
\left(Qy\right)_{n}=\sum_{k=0}^{n}q_{k}c_{n-k}.
$$

Adding the three and equating the total to zero gives, for every $n\ge0$,

$$
(n+2)(n+1)c_{n+2}+\sum_{k=0}^{n}(n-k+1)p_{k}c_{n-k+1}+\sum_{k=0}^{n}q_{k}c_{n-k}=0 .
$$

Solving for the highest index present produces the recurrence

$$
c_{n+2}=-\frac{1}{(n+2)(n+1)}\left[\sum_{k=0}^{n}(n-k+1)p_{k}c_{n-k+1}+\sum_{k=0}^{n}q_{k}c_{n-k}\right].
$$

The structure of this formula settles the counting question immediately. When $n=0$ it determines $c_{2}$ from $c_{1}$ and $c_{0}$; when $n=1$ it determines $c_{3}$ from $c_{2},c_{1},c_{0}$; and each further step determines one new coefficient. The numbers $c_{0}$ and $c_{1}$ never appear on the left, so they are free, and every other coefficient is a definite expression in them. Hence the solution set is exactly two-dimensional, and any two solutions whose first two coefficients agree must agree in every coefficient and therefore coincide as functions.

Convergence is established by estimating the coefficients. Since the series for $P$ and $Q$ converge for $\left|t\right|<\rho$, the Cauchy estimates give a constant $M$ with

$$
\left|p_{k}\right|\le M\rho^{-k}, \qquad \left|q_{k}\right|\le M\rho^{-k}
$$

for every $k$. Substituting these bounds into the recurrence and arguing by induction gives, for each fixed $R$ with $0<R<\rho$,

$$
\left|c_{n}\right|\le K R^{-n}
$$

for a constant $K$ depending on $R$ and on the first two coefficients. The mechanism is that each of the two sums contains $n+1$ terms of size at most a fixed multiple of $R^{-n}$, so it grows at most linearly in $n$, while the factor $(n+2)(n+1)$ in the denominator grows quadratically; the ratio therefore stays bounded, which is what the induction needs. A coefficient bound of the form $K R^{-n}$ implies that the series converges absolutely for $\left|t\right|<R$, and since $R$ was any number below $\rho$, the radius of convergence is at least $\rho$.

Two conclusions follow. First, the assumed form is not merely a lucky guess at an ordinary point; it produces every solution, and the two-parameter family it generates is the general solution. Second, the radius statement in the existence theorem is a consequence of the size of the coefficients of the equation, not of anything special about the equation being solved.


### 3.6 Method: the six-step classification

Every classification question is answered by the same sequence, and marks are lost when the sequence is shortened.

1. Write the equation with the second derivative isolated, that is, in normalised form, and record the two coefficient functions $P$ and $Q$ explicitly.
2. List the points at which $P$ or $Q$ fails to be analytic. For polynomial coefficients these are the zeros of $a_{0}$ after cancellation; for coefficients involving other functions they include every point where those functions have poles.
3. Verify that each listed point is genuinely singular by confirming that at least one of $P$ and $Q$ is not analytic there.
4. At each singular point $x_{0}$, form the two products $\left(x-x_{0}\right)P(x)$ and $\left(x-x_{0}\right)^{2}Q(x)$.
5. Decide whether each product is analytic at $x_{0}$, usually by simplifying it and then evaluating the two limits.
6. Report the classification, together with the form of solution the relevant theorem guarantees.

Steps 4 and 5 are where the mathematics happens, and they must be written out. A conclusion such as "hence $x=0$ is a regular singular point" without the simplification of the two products earns nothing, because the classification is precisely the assertion that those products are analytic.

### 3.7 Method: determining the radius of a series solution

Three rules cover every case met in this course.

- **Ratio test.** For a computed series $\sum a_{n}t^{n}$ with eventually nonzero coefficients, compute $R=\lim\left|a_{n}/a_{n+1}\right|$ whenever this limit exists.
- **Distance rule.** At an ordinary point, the radius is at least the distance from the centre to the nearest singular point, with distances measured in the complex plane.
- **Denominator rule.** For a function given as a quotient of analytic functions, the radius is the distance to the nearest zero of the denominator.

The distance rule explains familiar restrictions. Legendre's equation has singular points at $\pm1$, so a series about $0$ converges at least for $\left|x\right|<1$. Bessel's equation has its only singular point at $0$, so a series about $x_{0}=1$ converges at least for $\left|x-1\right|<1$, since the distance from $1$ to $0$ is one.

### 3.8 Method: reporting the nature of the solution

A classification question is usually paired with a request to state what kind of solution exists, and the answer must be phrased in terms of the theorem that applies.

At an ordinary point: two linearly independent solutions of the form $\sum C_{n}\left(x-x_{0}\right)^{n}$ exist, and their radius is at least the distance to the nearest singular point. At a regular singular point: at least one nontrivial solution of the form $\left(x-x_{0}\right)^{r}\sum C_{n}\left(x-x_{0}\right)^{n}$ exists, with $C_{0}\neq0$, valid on a deleted interval $0<\left|x-x_{0}\right|<R$, and the exponent is a root of the indicial equation. At an irregular singular point: no solution of either form is guaranteed, and the equation may require a different kind of expansion altogether.

Notice how the three answers differ in strength. The first is the strongest, the second weaker, the third empty of guarantee. Reporting the strongest applicable answer is correct; reporting a stronger answer than the theorem supports is the error that the examination penalises most heavily.

## 4. Representative Worked Examples and Solutions

### 4.1 Problem: classify every point of Legendre's equation

Classify the points of

$$
\left(1-x^{2}\right)\frac{d^{2}y}{dx^{2}}-2x\frac{dy}{dx}+p(p+1)y=0 ,
$$

where $p$ is a real constant, and state the kind of series solution available about $x_{0}=0$.

### 4.2 Solution: normalise, locate, then test both candidate points

Step 1. Divide by $1-x^{2}$, which is legitimate except at $x=1$ and $x=-1$.

$$
\frac{d^{2}y}{dx^{2}}-\frac{2x}{1-x^{2}}\frac{dy}{dx}+\frac{p(p+1)}{1-x^{2}}y=0
$$

Step 2. Read off the two coefficient functions and factor the denominators, using $1-x^{2}=(1-x)(1+x)=-(x-1)(x+1)$.

$$
P(x)=\frac{-2x}{1-x^{2}}=\frac{2x}{(x-1)(x+1)}, \qquad Q(x)=\frac{p(p+1)}{1-x^{2}}=\frac{-p(p+1)}{(x-1)(x+1)}
$$

Step 3. Identify the candidate points. Both $P$ and $Q$ are rational with denominators vanishing only at $x=1$ and $x=-1$, so those are the only points where analyticity can fail. Both functions are analytic at every other real number, so every point other than $\pm1$ is ordinary.

Step 4. Test $x=1$, where $t=x-1$. Compute the first product and simplify.

$$
(x-1)P(x)=\frac{2x}{x+1}
$$

This is a rational function whose denominator equals $2$ at $x=1$, so it is analytic there, and its limit is $\frac{2}{2}=1$. Now the second product.

$$
(x-1)^{2}Q(x)=\frac{-p(p+1)(x-1)}{x+1}
$$

This is a polynomial divided by $x+1$, hence analytic at $x=1$, with limit $0$. Both products are analytic, so $x=1$ is a regular singular point.

Step 5. Test $x=-1$, where $t=x+1$.

$$
(x+1)P(x)=\frac{2x}{x-1}, \qquad (x+1)^{2}Q(x)=\frac{-p(p+1)(x+1)}{x-1}
$$

The first has denominator $-2$ at $x=-1$ and the second has the factor $x+1$ in its numerator, so both are analytic at $x=-1$, with limits $1$ and $0$. Hence $x=-1$ is also a regular singular point.

Step 6. Record the leading coefficients and the exponents at $x=1$. From the limits, $p_{0}=1$ and $q_{0}=0$, so the indicial equation is

$$
r(r-1)+r=r^{2}=0 ,
$$

a double root $r=0$. At $x=-1$ the same values occur, again giving the double root $r=0$.

Step 7. State the nature of the solution about $x_{0}=0$. Since $0$ is ordinary, the equation has two independent solutions of the form

$$
y=\sum_{n=0}^{\infty}C_{n}x^{n},
$$

and their radius of convergence is at least the distance from $0$ to the nearer singular point, namely $1$. The conclusion is consistent with the polynomial solutions that terminate: when $p$ is a non-negative integer one of the two solutions is a polynomial, and a polynomial is a series with radius infinity, which certainly satisfies the bound.

### 4.3 Problem: classify the points of Bessel's equation

Classify the points of

$$
x^{2}\frac{d^{2}y}{dx^{2}}+x\frac{dy}{dx}+\left(x^{2}-n^{2}\right)y=0
$$

for a non-negative constant $n$, and state the solution guaranteed at the singular point.

### 4.4 Solution: normalise, test the origin, then test a typical nonzero point

Step 1. Divide by $x^{2}$ for $x\neq0$.

$$
\frac{d^{2}y}{dx^{2}}+\frac{1}{x}\frac{dy}{dx}+\left(1-\frac{n^{2}}{x^{2}}\right)y=0
$$

Step 2. Record the coefficients.

$$
P(x)=\frac{1}{x}, \qquad Q(x)=1-\frac{n^{2}}{x^{2}}=\frac{x^{2}-n^{2}}{x^{2}}
$$

Step 3. Locate the singular points. Both functions are rational with denominators vanishing only at $x=0$, so $x=0$ is the only candidate and every nonzero point is ordinary.

Step 4. Test $x=0$ by forming the two products.

$$
xP(x)=1, \qquad x^{2}Q(x)=x^{2}-n^{2}
$$

The first is the constant $1$, analytic everywhere; the second is a polynomial, analytic everywhere. Both are analytic at $0$, so $x=0$ is a regular singular point.

Step 5. Compute the exponents from the limits $p_{0}=1$ and $q_{0}=-n^{2}$.

$$
r(r-1)+r-n^{2}=r^{2}-n^{2}=0
$$

The roots are $r=n$ and $r=-n$. If $n$ is not an integer the roots differ by a non-integer, so two independent Frobenius series exist. If $n$ is an integer the roots differ by an integer, so one series is guaranteed and the second solution may carry a logarithmic factor.

Step 6. State the guaranteed solution. The theorem supplies at least one nontrivial solution

$$
y=x^{r}\sum_{k=0}^{\infty}C_{k}x^{k}, \qquad C_{0}\neq0,
$$

valid on a deleted interval $0<\left|x\right|<R$, with $r=n$ or $r=-n$. The equation therefore has the solution known as the Bessel function of the first kind, whose leading behaviour is $x^{n}$ up to a constant multiple.

Step 7. Check the ordinary point $x_{0}=1$. Since $P$ and $Q$ are analytic at $1$ and the nearest singular point is $0$ at distance $1$, a power series solution about $x_{0}=1$ converges at least for $\left|x-1\right|<1$.

### 4.5 Problem: classify the points of the hypergeometric equation

Classify the finite singular points of

$$
x(1-x)\frac{d^{2}y}{dx^{2}}+\left[c-(a+b+1)x\right]\frac{dy}{dx}-aby=0 ,
$$

where $a$, $b$ and $c$ are constants with $c$ not a non-positive integer.

### 4.6 Solution: normalise and run both tests at both points

Step 1. Divide by $x(1-x)$.

$$
\frac{d^{2}y}{dx^{2}}+\frac{c-(a+b+1)x}{x(1-x)}\frac{dy}{dx}-\frac{ab}{x(1-x)}y=0
$$

Step 2. Record the coefficients.

$$
P(x)=\frac{c-(a+b+1)x}{x(1-x)}, \qquad Q(x)=\frac{-ab}{x(1-x)}
$$

Step 3. Locate the candidates. The denominators vanish at $x=0$ and at $x=1$, and the hypothesis $c\neq0$ ensures that the numerator of $P$ does not vanish at $x=0$, so both points are genuinely singular. Every other finite point is ordinary.

Step 4. Test $x=0$.

$$
xP(x)=\frac{c-(a+b+1)x}{1-x}, \qquad x^{2}Q(x)=\frac{-abx}{1-x}
$$

The first has denominator equal to $1$ at $x=0$ and the second has a factor $x$ in its numerator, so both are analytic at $0$, with limits $c$ and $0$. Hence $x=0$ is regular singular, and the indicial equation is

$$
r(r-1)+cr=r\left(r-1+c\right)=0,
$$

with roots $r=0$ and $r=1-c$.

Step 5. Test $x=1$. Multiply $P$ by $x-1$ and use $1-x=-(x-1)$.

$$
(x-1)P(x)=\frac{c-(a+b+1)x}{-x}
$$

The denominator equals $-1$ at $x=1$, so this is analytic there, with limit

$$
\frac{c-(a+b+1)}{-1}=a+b+1-c .
$$

For the second product, note that $(x-1)^{2}=-(x-1)(1-x)$, so

$$
(x-1)^{2}Q(x)=\frac{ab(x-1)}{x},
$$

which is analytic at $x=1$ with limit $0$. Hence $x=1$ is regular singular, with exponents $r=0$ and $r=1-(a+b+1-c)=c-a-b$.

Step 6. Interpret. Both finite singular points are regular, the exponents are read off from the leading Laurent coefficients, and the equation belongs to the class for which the Frobenius theorem applies at each of them.

### 4.7 Problem: classify a point that is regular and a point that is not

Classify the singular points of

$$
\left(x^{4}-2x^{3}+x^{2}\right)\frac{d^{2}y}{dx^{2}}+2(x-1)\frac{dy}{dx}+x^{2}y=0 .
$$

### 4.8 Solution: factor the leading coefficient completely before dividing

Step 1. Factor the coefficient of the second derivative.

$$
x^{4}-2x^{3}+x^{2}=x^{2}\left(x^{2}-2x+1\right)=x^{2}(x-1)^{2}
$$

Step 2. Divide by $x^{2}(x-1)^{2}$, valid for $x\neq0$ and $x\neq1$.

$$
\frac{d^{2}y}{dx^{2}}+\frac{2(x-1)}{x^{2}(x-1)^{2}}\frac{dy}{dx}+\frac{x^{2}}{x^{2}(x-1)^{2}}y=0
$$

Step 3. Cancel common factors, which must be done before any conclusion is drawn.

$$
P(x)=\frac{2}{x^{2}(x-1)}, \qquad Q(x)=\frac{1}{(x-1)^{2}}
$$

Step 4. Locate the singular points. Both functions fail to be analytic exactly at $x=0$ and at $x=1$, so those are the only candidates, and both are genuine because both coefficients become infinite there.

Step 5. Test $x=0$.

$$
xP(x)=\frac{2}{x(x-1)}, \qquad x^{2}Q(x)=\frac{x^{2}}{(x-1)^{2}}
$$

The second product is analytic at $0$ with limit $0$. The first is not: its denominator vanishes at $x=0$ and its numerator does not, so $\left|xP(x)\right|\to\infty$ as $x\to0$. One failed test is decisive, so $x=0$ is an irregular singular point.

Step 6. Test $x=1$.

$$
(x-1)P(x)=\frac{2}{x^{2}}, \qquad (x-1)^{2}Q(x)=1
$$

Both are analytic at $x=1$, with limits $2$ and $1$. Hence $x=1$ is a regular singular point, and its indicial equation is

$$
r(r-1)+2r+1=r^{2}+r+1=0,
$$

whose roots are $r=\frac{-1}{2}\pm i\frac{\sqrt{3}}{2}$, a complex conjugate pair. Complex exponents are permitted, and they signal oscillatory behaviour of the solution as $x\to1$ together with unboundedness.

Step 7. Report the full classification: $x=0$ irregular, $x=1$ regular singular, every other point ordinary.

### 4.9 Problem: an irregular point detected by the second test alone

Classify the point $x=0$ for

$$
\frac{d^{2}y}{dx^{2}}+\frac{1}{x}\frac{dy}{dx}+\frac{1}{x^{3}}y=0 .
$$

### 4.10 Solution: one product succeeds, the other fails

Step 1. The equation is already normalised, so read off

$$
P(x)=\frac{1}{x}, \qquad Q(x)=\frac{1}{x^{3}} .
$$

Step 2. Confirm that $x=0$ is singular, because both functions become infinite there.

Step 3. Apply the first test.

$$
xP(x)=x\cdot\frac{1}{x}=1
$$

This is the constant $1$, analytic at $0$, with limit $1$; the first test is passed.

Step 4. Apply the second test.

$$
x^{2}Q(x)=x^{2}\cdot\frac{1}{x^{3}}=\frac{1}{x}
$$

This has a pole at $0$ and its limit does not exist as a finite number, so it is not analytic at $0$. The second test fails.

Step 5. Conclude. Since one of the two required products is not analytic, $x=0$ is an irregular singular point. No power series solution of either permitted form is guaranteed, even though the first test gave a perfectly finite value.

### 4.11 Problem: classify singular points created by a trigonometric coefficient

Locate and classify the singular points of

$$
(\sin x)\frac{d^{2}y}{dx^{2}}+(\cos x)\frac{dy}{dx}+\frac{1}{x}y=0 .
$$

### 4.12 Solution: normalise with the cotangent, then test each multiple of pi

Step 1. Divide by $\sin x$, which is nonzero except at integer multiples of $\pi$.

$$
\frac{d^{2}y}{dx^{2}}+\cot x\frac{dy}{dx}+\frac{1}{x\sin x}y=0
$$

Step 2. Record the coefficients.

$$
P(x)=\cot x=\frac{\cos x}{\sin x}, \qquad Q(x)=\frac{1}{x\sin x}
$$

Step 3. Locate the singular points. The cotangent is analytic except where $\sin x=0$, and $Q$ is additionally undefined at $x=0$. Both are analytic everywhere else, so the singular points are the integer multiples of $\pi$.

Step 4. Test $x=0$, where $t=x$.

$$
xP(x)=\frac{x\cos x}{\sin x}=x\cdot\frac{1}{\sin x}\cdot\cos x
$$

Write $\frac{\sin x}{x}=1-\frac{x^{2}}{6}+\cdots$, so that $\frac{x}{\sin x}$ is the reciprocal of a series with nonzero constant term and is therefore analytic at $0$, with value $1$. Hence $xP(x)$ is analytic at $0$, with limit $1$. For the second product,

$$
x^{2}Q(x)=\frac{x^{2}}{x\sin x}=\frac{x}{\sin x},
$$

which is again analytic at $0$, with limit $1$. Both products are analytic, so $x=0$ is a regular singular point with exponents given by $r(r-1)+r+1=0$, that is $r^{2}+1=0$, so $r=\pm i$.

Step 5. Test $x=\pi$. Put $u=x-\pi$ and use $\sin(\pi+u)=-\sin u$, $\cos(\pi+u)=-\cos u$, so that $\cot x=\cot u$ near $\pi$.

$$
(x-\pi)P(x)=u\cot u=u\cdot\frac{\cos u}{\sin u}
$$

This is analytic at $u=0$ with limit $1$, by the same reciprocal argument as in Step 4. For the second product, $\sin x$ has a simple zero at $\pi$, so $Q$ has a simple pole and

$$
(x-\pi)^{2}Q(x)=\frac{u^{2}}{(\pi+u)\sin(\pi+u)}\to0 .
$$

Both products are analytic, so $x=\pi$ is regular singular. The same computation with $u=x-k\pi$ shows that every multiple of $\pi$ is regular singular.

Step 6. Report. The singular points are $x=k\pi$ for every integer $k$, and each is a regular singular point.

### 4.13 Problem: a double exponent and the logarithmic second solution

Classify $x=0$ for $x^{2}y''+3xy'+y=0$ and write down the two independent solutions.

### 4.14 Solution: test, compute the indicial roots, then verify both solutions

Step 1. Normalise.

$$
\frac{d^{2}y}{dx^{2}}+\frac{3}{x}\frac{dy}{dx}+\frac{1}{x^{2}}y=0
$$

Step 2. Record the coefficients $P(x)=\frac{3}{x}$ and $Q(x)=\frac{1}{x^{2}}$, both infinite at $x=0$.

Step 3. Apply the two tests.

$$
xP(x)=3, \qquad x^{2}Q(x)=1
$$

Both are constants, hence analytic, so $x=0$ is a regular singular point with $p_{0}=3$ and $q_{0}=1$.

Step 4. Solve the indicial equation.

$$
r(r-1)+3r+1=r^{2}+2r+1=(r+1)^{2}=0
$$

The root $r=-1$ is repeated. A repeated root is the borderline case of an integer difference, and a logarithm must be expected.

Step 5. Verify the first solution $y_{1}=x^{-1}$.

$$
y_{1}'=-x^{-2}, \qquad y_{1}''=2x^{-3}
$$

Substituting into $x^{2}y''+3xy'+y$ gives

$$
x^{2}\left(2x^{-3}\right)+3x\left(-x^{-2}\right)+x^{-1}=2x^{-1}-3x^{-1}+x^{-1}=0 .
$$

Step 6. Verify the second solution $y_{2}=x^{-1}\ln x$.

$$
y_{2}'=-x^{-2}\ln x+x^{-2}, \qquad y_{2}''=2x^{-3}\ln x-3x^{-3}
$$

Substituting gives

$$
x^{2}\left(2x^{-3}\ln x-3x^{-3}\right)+3x\left(-x^{-2}\ln x+x^{-2}\right)+x^{-1}\ln x
$$

and collecting the logarithmic terms separately from the power terms,

$$
\left(2-3+1\right)x^{-1}\ln x+\left(-3+3\right)x^{-1}=0 .
$$

Step 7. Report. The point is regular singular with repeated exponent $r=-1$, and the two independent solutions are $x^{-1}$ and $x^{-1}\ln x$. Both are unbounded at the origin, which is typical at a regular singular point and impossible at an ordinary point.

### 4.15 Problem: non-integer exponents and the resulting series

Show that $x=0$ is a regular singular point of $2x^{2}y''-xy'+(x-5)y=0$, find the exponents, and compute the first coefficients of the solution belonging to the larger exponent.

### 4.16 Solution: test the point, then run the Frobenius recurrence

Step 1. Normalise by dividing by $2x^{2}$.

$$
\frac{d^{2}y}{dx^{2}}-\frac{1}{2x}\frac{dy}{dx}+\frac{x-5}{2x^{2}}y=0
$$

Step 2. Record the coefficients and form the products.

$$
P(x)=-\frac{1}{2x}, \qquad Q(x)=\frac{x-5}{2x^{2}}, \qquad xP(x)=-\frac{1}{2}, \qquad x^{2}Q(x)=\frac{x-5}{2}
$$

Both products are analytic at $0$, with limits $-\frac{1}{2}$ and $-\frac{5}{2}$, so $x=0$ is a regular singular point.

Step 3. Write the indicial equation with $p_{0}=-\frac{1}{2}$ and $q_{0}=-\frac{5}{2}$.

$$
r(r-1)-\frac{1}{2}r-\frac{5}{2}=0
$$

Multiplying by $2$ gives $2r^{2}-3r-5=0$, and the discriminant is $9+40=49$, so

$$
r=\frac{3\pm7}{4},
$$

that is $r=\frac{5}{2}$ or $r=-1$.

Step 4. Note that the difference of the exponents is $\frac{7}{2}$, not an integer, so the theorem guarantees two independent Frobenius series, one for each exponent.

Step 5. Derive the recurrence for a general exponent by substituting $y=\sum_{n=0}^{\infty}c_{n}x^{n+r}$ into the original equation. The coefficient of $x^{n+r}$ is

$$
\left[2(n+r)(n+r-1)-(n+r)-5\right]c_{n}+c_{n-1}=0,
$$

so that

$$
c_{n}=-\frac{c_{n-1}}{2(n+r)(n+r-1)-(n+r)-5}, \qquad n\ge1 .
$$

Step 6. Take $r=\frac{5}{2}$ and $c_{0}=1$. For $n=1$ the denominator is $2\cdot\frac{7}{2}\cdot\frac{5}{2}-\frac{7}{2}-5=9$, so $c_{1}=-\frac{1}{9}$. For $n=2$ the denominator is $2\cdot\frac{9}{2}\cdot\frac{7}{2}-\frac{9}{2}-5=22$, so $c_{2}=\frac{1}{198}$.

Step 7. State the solution and check it.

$$
y_{1}=x^{5/2}\left(1-\frac{x}{9}+\frac{x^{2}}{198}-\cdots\right)
$$

Substituting the three-term truncation into $2x^{2}y''-xy'+(x-5)y$ leaves only the term involving $x^{3}$, which is precisely the first term omitted, so every computed coefficient is correct. For $r=-1$ the same recurrence gives $c_{1}=\frac{1}{5}$ and $c_{2}=\frac{1}{30}$, so the second solution begins

$$
y_{2}=x^{-1}\left(1+\frac{x}{5}+\frac{x^{2}}{30}+\cdots\right).
$$

### 4.17 Problem: an irregular point with a divergent formal series

Show that $x=0$ is an irregular singular point of $x^{2}y''+y'+y=0$, and examine the formal power series obtained by substitution.

### 4.18 Solution: test, then show the series has radius zero

Step 1. Normalise.

$$
\frac{d^{2}y}{dx^{2}}+\frac{1}{x^{2}}\frac{dy}{dx}+\frac{1}{x^{2}}y=0
$$

Step 2. Form the first product.

$$
xP(x)=x\cdot\frac{1}{x^{2}}=\frac{1}{x}
$$

This is unbounded as $x\to0$, so it is not analytic at $0$ and $x=0$ is an irregular singular point. The second product is $x^{2}Q(x)=1$, which is analytic, but one failure is enough.

Step 3. Substitute $y=\sum_{n=0}^{\infty}c_{n}x^{n}$ anyway, to see what happens. The coefficient of $x^{n}$ in $x^{2}y''+y'+y$ is

$$
n(n-1)c_{n}+(n+1)c_{n+1}+c_{n}=0,
$$

which gives

$$
c_{n+1}=-\frac{n^{2}-n+1}{n+1}c_{n} .
$$

Step 4. Compute the first few coefficients with $c_{0}=1$.

$$
c_{1}=-1, \qquad c_{2}=\frac{1}{2}, \qquad c_{3}=-\frac{1}{2}, \qquad c_{4}=\frac{7}{8}
$$

Step 5. Test the resulting series for convergence by the ratio test.

$$
\left|\frac{c_{n+1}}{c_{n}}\right|=\frac{n^{2}-n+1}{n+1}\to\infty
$$

Since the ratio of successive coefficients tends to infinity, the radius of convergence is the reciprocal of that limit, namely zero. The formal series therefore converges only at $x=0$ and represents no function on any interval.

Step 6. Conclude. The point is irregular, the expected series solution does not exist, and the formal series produced by blind substitution is worthless as a solution. This is exactly what the third clause of the existence theorem warns against: at an irregular singular point nothing may be assumed.

### 4.19 Problem: an ordinary point with an infinite radius

Find two independent power series solutions of $y''+xy=0$ about $x_{0}=0$ and state the radius of convergence.

### 4.20 Solution: check the point, then run the three-term recurrence

Step 1. The equation is normalised with $P(x)=0$ and $Q(x)=x$. Both are polynomials, hence analytic everywhere, so every point is ordinary, in particular $x_{0}=0$.

Step 2. Substitute $y=\sum_{n=0}^{\infty}c_{n}x^{n}$. The coefficient of $x^{n}$ is $(n+2)(n+1)c_{n+2}+c_{n-1}$, so

$$
c_{n+2}=-\frac{c_{n-1}}{(n+2)(n+1)}, \qquad c_{-1}=0 .
$$

Step 3. Take $c_{0}=1$ and $c_{1}=0$. Then $c_{2}=0$ from $n=0$, and $n=1$ gives $c_{3}=-\frac{1}{6}$, while $n=4$ gives $c_{6}=\frac{1}{180}$.

$$
y_{1}=1-\frac{x^{3}}{6}+\frac{x^{6}}{180}-\cdots
$$

Step 4. Take $c_{0}=0$ and $c_{1}=1$. Then $c_{2}=c_{3}=0$ and $n=2$ gives $c_{4}=-\frac{1}{12}$, while $n=5$ gives $c_{7}=\frac{1}{504}$.

$$
y_{2}=x-\frac{x^{4}}{12}+\frac{x^{7}}{504}-\cdots
$$

Step 5. Confirm independence. The first series has constant term $1$ and no term in $x$, the second has no constant term and coefficient of $x$ equal to $1$, so neither is a multiple of the other.

Step 6. State the radius. Since $P$ and $Q$ are entire, the theorem gives radius at least any number, that is, both series converge for every real $x$.

## 5. Mathematical Extensions, Limits, and Common Errors

### 5.1 What the classification assumes, and where it stops

Every statement in this topic begins with an implicit hypothesis that the coefficient functions are analytic on a punctured neighbourhood of the point being classified. That hypothesis is satisfied for all equations with analytic coefficients and an isolated zero of $a_{0}$, which covers every case in this course, including the trigonometric examples, because the zeros of the sine are isolated. It fails when a coefficient has an essential singularity, or when $a_{0}$ vanishes on a whole interval, and in those cases the words ordinary, regular and irregular lose their meaning. A student who applies the tests mechanically to an equation with a non-isolated singular set will obtain limits that do not exist and must not interpret that failure as a classification.

A second limitation is locality. Every label attaches to a point, never to an equation. The equation of Legendre has two singular points and infinitely many ordinary points; describing it as "a singular equation" is meaningless. What can legitimately be said is that the equation is Fuchsian, meaning that all of its singular points, including the point at infinity, are regular. Bessel's equation is Fuchsian in this sense, and so is the hypergeometric equation, whose three regular singular points at $0$, $1$ and infinity are the model for the entire theory.

A third limitation is that the theory is about existence, not about closed forms. Even when the existence theorem guarantees a series, the series may be the only available description of the solution. At a regular singular point the exponents can be complex, as in the worked example with a complex conjugate pair, and then the solutions are real combinations of terms involving logarithms and oscillations, which no elementary formula captures.

### 5.2 The point at infinity

For equations with polynomial coefficients it is natural to ask what happens at infinity. The question is reduced to a finite one by the substitution $x=\frac{1}{t}$ and $y(x)=Y(t)$, after which the nature of $t=0$ for the transformed equation is, by definition, the nature of $x=\infty$ for the original one.

For Legendre's equation the transformed equation is

$$
\frac{d^{2}Y}{dt^{2}}+\frac{2t}{t^{2}-1}\frac{dY}{dt}+\frac{p(p+1)}{t^{2}\left(t^{2}-1\right)}Y=0 .
$$

At $t=0$ the first coefficient is analytic, with value $0$, and the second satisfies

$$
t^{2}\cdot\frac{p(p+1)}{t^{2}\left(t^{2}-1\right)}=\frac{p(p+1)}{t^{2}-1}\to-p(p+1),
$$

a finite value with an analytic extension. Both tests pass, so infinity is a regular singular point of Legendre's equation. The same substitution applied to the hypergeometric equation shows that infinity is regular there too, with exponents $a$ and $b$; the three points $0$, $1$ and infinity are the complete singular set.

The computation at infinity is worth practising because it uses exactly the same two products, merely written in the new variable. The only care needed is in transforming the derivatives: since $\frac{dx}{dt}=-\frac{1}{t^{2}}$, the chain rule gives $\frac{dy}{dx}=-t^{2}\frac{dY}{dt}$ and $\frac{d^{2}y}{dx^{2}}=t^{4}\frac{d^{2}Y}{dt^{2}}+2t^{3}\frac{dY}{dt}$, and forgetting the second term is a common source of a wrong classification.

### 5.3 What the exponents tell you

At a regular singular point the pair of roots of the indicial equation carries real information about the solutions, and reading that information is often the point of a longer question.

If both roots are real and differ by a non-integer, two independent Frobenius series exist and the solutions behave like $x^{r_{1}}$ and $x^{r_{2}}$ near the origin. If the roots coincide, one solution has the pure power form and the other carries a logarithm. If the roots differ by an integer, the larger root always produces a series and the smaller may or may not, with a logarithmic term appearing in the remaining case. If the roots are complex conjugates, both solutions oscillate and grow or decay like $x^{\operatorname{Re}r}$, and real solutions involve logarithms of $x$ together with trigonometric functions of $\operatorname{Im}r\ln x$.

The exponents also predict boundedness. A negative real part means the solution blows up at the singular point; a positive real part means it tends to zero; a zero real part means it stays bounded but does not settle. This is the quantitative version of the statement that solutions at a regular singular point need not be defined at the point itself, and it is the sharpest contrast with an ordinary point, where every solution is analytic and therefore bounded.

### 5.4 Common errors and how to avoid them

- **Classifying before locating.** The two products must be applied only at points already proved singular. At an ordinary point both products are automatically analytic, so a careless worker reports every point as regular singular and never notices.
- **Using the roots of $a_{0}$ as the singular set.** Cancellation can remove a singularity, as in $\left(x^{2}-1\right)y''+(x-1)y'=0$, where $x=1$ is ordinary. Normalise and simplify first, then read the singular set from $P$ and $Q$.
- **Testing only one product.** Regularity requires both $\left(x-x_{0}\right)P$ and $\left(x-x_{0}\right)^{2}Q$ to be analytic. The equation $y''+\frac{1}{x}y'+\frac{1}{x^{3}}y=0$ passes the first test and fails the second, and it is irregular.
- **Forgetting the shift when $x_{0}\neq0$.** The factors are $\left(x-x_{0}\right)$ and $\left(x-x_{0}\right)^{2}$, not $x$ and $x^{2}$. At $x_{0}=2$ one must multiply by $x-2$, and using $x$ instead produces a finite limit that proves nothing.
- **Concluding that no solution exists at an irregular point.** The theorem says only that nothing is guaranteed. The equation may still have a convergent series, as some irregular points do; what fails is the guarantee, not the possibility.
- **Claiming two series at a regular singular point.** Only one Frobenius solution is guaranteed. The second may require a logarithm, and asserting two pure series is unjustified when the exponents differ by an integer.
- **Losing the exponent altogether.** Writing $y=\sum C_{n}\left(x-x_{0}\right)^{n}$ at a regular singular point discards the factor $\left(x-x_{0}\right)^{r}$, which is the whole content of the Frobenius theorem.
- **Overstating the radius.** The radius at an ordinary point is at least the distance to the nearest singular point; it is not necessarily larger, and it is limited by singularities in the complex plane, as the expansion of $\frac{1}{1+x^{2}}$ about $0$ shows.
- **Treating a complex exponent as an error.** Complex roots of the indicial equation are permitted by the theorem, and they occur in routine examples such as $x^{2}y''+y=0$ at $x=0$, where the indicial equation $r^{2}-r+1=0$ has the roots $r=\frac{1}{2}\pm i\frac{\sqrt{3}}{2}$.

### 5.5 A procedure for any question in this topic

1. Write the equation in normalised form and record $P$ and $Q$ explicitly.
2. Simplify both quotients, cancelling every common factor.
3. List the points where either quotient fails to be analytic, and check that each is genuinely singular.
4. At each singular point form $\left(x-x_{0}\right)P$ and $\left(x-x_{0}\right)^{2}Q$, simplify, and evaluate the two limits.
5. Classify the point as regular if both limits are finite and irregular otherwise.
6. At a regular point, compute the indicial exponents from $r(r-1)+p_{0}r+q_{0}=0$ and note whether a logarithm is to be expected.
7. State the form of solution guaranteed, together with its interval of validity, and state the radius when a series about an ordinary point is requested.

### 5.6 Consolidated summary

The topic rests on one question asked about one point at a time: are the two coefficient functions of the normalised equation well behaved there? If both are analytic the point is ordinary, and the equation has two independent power series solutions whose radius is at least the distance to the nearest singular point. If either fails to be analytic the point is singular, and the severity of the failure decides the rest. When the failure is no worse than a simple pole in $P$ and a double pole in $Q$, measured by the analyticity of $\left(x-x_{0}\right)P$ and $\left(x-x_{0}\right)^{2}Q$, the point is regular singular, and at least one solution of the form $\left(x-x_{0}\right)^{r}$ times a power series exists, with the exponent determined by a quadratic. When the failure is worse, the point is irregular, and no such solution is assured.

Everything else in the topic is bookkeeping around that question. The normalised form exists so that the question has a fixed target. The analyticity tests are stated as limits so that the answer can be computed rather than guessed. The indicial equation turns the qualitative promise into quantitative exponents. The three standard equations supply the working examples in which all of these ideas can be checked against known solutions, and the table of Section 1.6 summarises the whole classification in three rows. Mastery of the topic is the ability to run the seven steps of Section 5.5 on any equation, with the two products simplified and the two limits evaluated explicitly, and to state the resulting form of solution with the correct strength.




