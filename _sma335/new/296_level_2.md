## 1. Foundational Concepts, Definitions, and Axioms

### 1.1 Why a new method is needed

The methods of the earlier lessons - separation of variables, exact equations, integrating factors, and the auxiliary equation for constant coefficients - all end with a formula built from elementary functions. That class of methods is now exhausted. The equation

$$
\frac{d^{2}y}{dx^{2}}-xy=0
$$

has variable coefficients, and neither substitution nor an integrating factor reduces it. Its solutions exist, are smooth, and are perfectly well behaved, but they are not expressible in terms of powers, roots, exponentials, logarithms, trigonometric functions or their inverses. The same is true of Legendre's equation

$$
\left(1-x^{2}\right)\frac{d^{2}y}{dx^{2}}-2x\frac{dy}{dx}+n(n+1)y=0 ,
$$

whose solutions are the Legendre polynomials and the Legendre functions of the second kind, and of Bessel's equation in its many forms.

A power series solution abandons the search for a closed formula and instead represents the unknown function as an infinite sum of powers of the independent variable. The representation is exact, not approximate: a convergent power series is the function. The method replaces a differential equation by an infinite system of algebraic equations, one for each coefficient, and that system is solved recursively. Nothing about the equation needs to be guessed except the shape of the answer, and the shape is dictated by the classification of the point about which the expansion is made.

### 1.2 Power series, convergence, and analytic functions

> **Definition (power series about a point).** A power series about the point $x_{0}$ is an expression of the form
>
> $$
> \sum_{n=0}^{\infty}a_{n}\left(x-x_{0}\right)^{n}=a_{0}+a_{1}\left(x-x_{0}\right)+a_{2}\left(x-x_{0}\right)^{2}+\cdots ,
> $$
>
> where the coefficients $a_{0},a_{1},a_{2},\dots$ are fixed numbers and $x$ is the variable.

> **Definition (radius of convergence).** The series has radius of convergence $R$, where $0\le R\le\infty$, if it converges absolutely for every $x$ with $\left|x-x_{0}\right|<R$ and diverges for every $x$ with $\left|x-x_{0}\right|>R$. The open interval $\left|x-x_{0}\right|<R$ is the interval of convergence.

Three familiar series show the range of possibilities. The exponential series

$$
e^{x}=\sum_{n=0}^{\infty}\frac{x^{n}}{n!}=1+x+\frac{x^{2}}{2}+\frac{x^{3}}{6}+\cdots
$$

converges for every real $x$, so its radius is infinite. The geometric series

$$
\frac{1}{1-x}=\sum_{n=0}^{\infty}x^{n}=1+x+x^{2}+x^{3}+\cdots
$$

converges only for $\left|x\right|<1$, so its radius is one, and the obstruction is the pole of the function at $x=1$. The series $\sum n!\,x^{n}$ converges only at $x=0$, so its radius is zero, and such a series is useless for representing a function on an interval.

> **Definition (analytic function).** A function $f$ is analytic at $x_{0}$ if it equals its own power series about $x_{0}$ on some interval: there are numbers $a_{n}$ and a radius $R>0$ such that
>
> $$
> f(x)=\sum_{n=0}^{\infty}a_{n}\left(x-x_{0}\right)^{n}\qquad\text{for }\left|x-x_{0}\right|<R .
> $$

Polynomials, exponentials, sines, cosines and rational functions are analytic at every point where their denominator does not vanish. The quotient of two analytic functions is analytic wherever the denominator is non-zero, which is the fact used to classify the points of a differential equation in the next subsection.

### 1.3 The normalised form and the classification of points

Every second-order linear equation can be written with the second derivative carrying coefficient one, by dividing by the coefficient of that derivative.

> **Definition (normalised form).** Let
>
> $$
> a_{0}(x)\frac{d^{2}y}{dx^{2}}+a_{1}(x)\frac{dy}{dx}+a_{2}(x)y=0
> $$
>
> be a second-order linear homogeneous equation with $a_{0}$ not identically zero. On any interval where $a_{0}$ does not vanish, division by $a_{0}$ produces the normalised form
>
> $$
> \frac{d^{2}y}{dx^{2}}+p(x)\frac{dy}{dx}+q(x)y=0 ,
> $$
>
> with $p$ equal to $a_{1}$ divided by $a_{0}$ and $q$ equal to $a_{2}$ divided by $a_{0}$.

> **Definition (ordinary and singular points).** A point $x_{0}$ is an ordinary point of the normalised equation if both $p$ and $q$ are analytic at $x_{0}$. A point that is not ordinary is a singular point.

The classification is made on the normalised form and not on the original equation, and this is the first place where candidates lose marks: the coefficient $a_{0}$ may vanish at a point where $p$ and $q$ are nevertheless perfectly regular, or the reverse. Three examples show the mechanics.

For the equation

$$
\left(x^{2}-1\right)\frac{d^{2}y}{dx^{2}}+3x\frac{dy}{dx}+xy=0 ,
$$

normalising gives

$$
\frac{d^{2}y}{dx^{2}}+\frac{3x}{x^{2}-1}\frac{dy}{dx}+\frac{x}{x^{2}-1}y=0 .
$$

The coefficient functions are $p$ equal to $3x$ divided by $x^{2}-1$ and $q$ equal to $x$ divided by $x^{2}-1$. Both are rational with denominator $\left(x-1\right)\left(x+1\right)$, so both are analytic except at $x=1$ and $x=-1$. Every other point, and in particular $x=0$, is ordinary. The distance from $0$ to the nearer singular point is one, so a series about $0$ is guaranteed to converge at least for $\left|x\right|<1$.

For the equation

$$
2x^{2}\frac{d^{2}y}{dx^{2}}-x\frac{dy}{dx}+\left(1-x^{2}\right)y=0 ,
$$

normalising gives

$$
\frac{d^{2}y}{dx^{2}}-\frac{1}{2x}\frac{dy}{dx}+\frac{1-x^{2}}{2x^{2}}y=0 .
$$

Here $p$ is $-1$ divided by $2x$, which is not analytic at $0$, so $0$ is singular. Nevertheless the two products $xp(x)$ and $x^{2}q(x)$ are

$$
xp(x)=-\frac{1}{2},\qquad x^{2}q(x)=\frac{1-x^{2}}{2},
$$

and both are analytic at $0$, indeed analytic everywhere. The singularity is of the mild kind that the Frobenius method handles.

For the equation

$$
x^{3}\frac{d^{2}y}{dx^{2}}+xy=0 ,
$$

normalising gives $p$ equal to zero and $q$ equal to $1$ divided by $x^{2}$, so

$$
xp(x)=0,\qquad x^{2}q(x)=\frac{1}{x} .
$$

The second product is not analytic at $0$ and tends to infinity there, so the singularity is severe. No series of either template describes the solution near $0$.

### 1.4 Regular and irregular singular points

> **Definition (regular singular point).** A singular point $x_{0}$ is regular if the two products $\left(x-x_{0}\right)p(x)$ and $\left(x-x_{0}\right)^{2}q(x)$ are analytic at $x_{0}$. Equivalently, writing
>
> $$
> p_{0}=\lim_{x\to x_{0}}\left(x-x_{0}\right)p(x),\qquad q_{0}=\lim_{x\to x_{0}}\left(x-x_{0}\right)^{2}q(x),
> $$
>
> both limits exist and are finite, and the products are analytic.

> **Definition (irregular singular point).** A singular point that is not regular is irregular.

The two numbers $p_{0}$ and $q_{0}$ are not decoration. They are the only data about the coefficients that enter the indicial equation, and therefore they alone decide the powers $x^{r}$ that can appear in a solution.

The classification is a table worth memorising in the form of a test rather than a definition.

| Equation | $p$ | $q$ | $xp$ | $x^{2}q$ | Point $x=0$ |
| --- | --- | --- | --- | --- | --- |
| $y''+xy'+y=0$ | $x$ | $1$ | $0$ | $0$ | ordinary |
| $2x^{2}y''-xy'+(1-x^{2})y=0$ | $-\frac{1}{2x}$ | $\frac{1-x^{2}}{2x^{2}}$ | $-\frac{1}{2}$ | $\frac{1-x^{2}}{2}$ | regular singular |
| $x^{2}y''+3xy'+(1-x)y=0$ | $\frac{3}{x}$ | $\frac{1-x}{x^{2}}$ | $3$ | $1-x$ | regular singular |
| $x^{3}y''+xy=0$ | $0$ | $\frac{1}{x^{2}}$ | $0$ | $\frac{1}{x}$ | irregular singular |
| $x^{2}y''+y=0$ | $0$ | $\frac{1}{x^{2}}$ | $0$ | $1$ | regular singular |

In the first row the products are polynomials, which is the strongest possible form of regularity, and the point is ordinary rather than singular. In the last row the equation is Euler's equation, whose solutions are pure powers; the products are constants, so the regularity is also maximal in its class.

### 1.5 The first-order equation and its three existence conditions

For a first-order equation written in the solved form

$$
\frac{dy}{dx}=f(x,y),
$$

the classical existence and uniqueness statement is local and needs three hypotheses.

> **Definition (the three conditions).** The equation $\frac{dy}{dx}=f(x,y)$ has a unique solution through each point of a domain $D$ of the $xy$-plane when the following hold:
>
> (i) $f(x,y)$ is continuous and single valued on $D$;
>
> (ii) $f(x,y)$ is bounded on $D$, that is $\left|f(x,y)\right|\le M$ for a fixed number $M$;
>
> (iii) the partial derivative $\frac{\partial f}{\partial y}$ exists and is continuous at every point of $D$.

The first condition makes the slope well defined at every point, so that a direction field exists. The second prevents the slope from becoming infinite anywhere in the domain, which would allow a solution to turn vertically. The third is the Lipschitz-type condition that rules out the branching behaviour seen in $y'$ equal to three times $y$ to the power two thirds, where two solutions pass through the same point. When all three hold, exactly one solution curve passes through each point of $D$.

A polynomial $f$ satisfies all three conditions on the whole plane, so every equation whose right-hand side is a polynomial in $x$ and $y$ has a unique local solution through every point. The interesting case for this topic is the linear one, where the right-hand side is $Q(x)-P(x)y$ with $P$ and $Q$ analytic; then the solution is itself analytic and its series can be computed coefficient by coefficient.

### 1.6 The two templates for a series solution

There are exactly two shapes of answer in this topic, and choosing the wrong one is fatal.

The first template belongs to an ordinary point:

$$
y=\sum_{n=0}^{\infty}c_{n}x^{n}=c_{0}+c_{1}x+c_{2}x^{2}+c_{3}x^{3}+\cdots .
$$

Here every power present is a non-negative integer and the two lowest coefficients $c_{0}$ and $c_{1}$ are free. They are the values of $y$ and of $y'$ at the expansion point, so the general solution appears as $c_{0}$ times one series plus $c_{1}$ times another.

The second template belongs to a regular singular point and carries the name of Frobenius:

$$
y=x^{r}\sum_{n=0}^{\infty}c_{n}x^{n}=c_{0}x^{r}+c_{1}x^{r+1}+c_{2}x^{r+2}+\cdots ,
$$

where $c_{0}$ is non-zero and $r$ is a number still to be found. The factor $x^{r}$ allows the first power to be fractional or negative, which is exactly what the mild singularity requires. The condition $c_{0}\neq 0$ is a normalisation: if $c_{0}$ were zero the whole series could be divided by a higher power of $x$ and rewritten with a different, larger $r$.

### 1.7 What the method actually does

Every calculation in this topic is the same five moves in the same order.

1. Classify the expansion point, using the normalised form, and choose the template accordingly.
2. Differentiate the template term by term as many times as the equation requires.
3. Substitute into the equation and multiply out, so that the equation becomes a single sum of powers of $x$ equal to a known right-hand side.
4. Align the indices, so that every term is written as a coefficient times the same power $x^{m}$; then equate coefficients.
5. Solve the resulting recurrence from the bottom upwards, and write the answer both as a list of terms and as a sum.

Only one step is conceptually delicate, and it is step four. The alignment of indices is pure bookkeeping with no mathematics beyond a change of summation letter, yet almost every error in the topic is an alignment error. Step five is mechanical once the recurrence is right. The two roles of the free coefficients are decided at the very first alignment: the coefficient of the lowest power in the equation produces either a determination of $c_{2}$ in the ordinary case, or the indicial equation in the Frobenius case.

## 2. Theorems, Lemmas, and Analytical Properties

### 2.1 Term-by-term differentiation

> **Lemma (differentiation of a power series).** If $f(x)=\sum c_{n}\left(x-x_{0}\right)^{n}$ on the interval $\left|x-x_{0}\right|<R$ with $R>0$, then $f$ is differentiable there and
>
> $$
> f'(x)=\sum_{n=1}^{\infty}n\,c_{n}\left(x-x_{0}\right)^{n-1},
> $$
>
> the differentiated series having the same radius of convergence $R$.

The lemma is what allows the template to be substituted into a differential equation at all. Differentiating $k$ times multiplies the coefficient $c_{n}$ by the falling product $n(n-1)\cdots(n-k+1)$ and lowers the exponent by $k$; that product vanishes for $n<k$, which is why the differentiated sum may start at $n=k$ instead of $n=0$.

> **Corollary.** The $k$-th derivative of the template at the expansion point is $k!$ times the coefficient of $\left(x-x_{0}\right)^{k}$, so
>
> $$
> c_{k}=\frac{f^{(k)}(x_{0})}{k!} .
> $$

The corollary identifies the coefficients of a series solution with the Taylor coefficients of the solution, so a power series solution and a Taylor expansion are the same object; the differential equation is merely a device for computing the Taylor coefficients without knowing the function.

### 2.2 Uniqueness of the coefficients

> **Lemma (identity theorem for power series).** Suppose $\sum_{n=0}^{\infty}a_{n}\left(x-x_{0}\right)^{n}=0$ for every $x$ in some interval $\left|x-x_{0}\right|<R$ with $R>0$. Then $a_{n}=0$ for every $n$.

> **Corollary (matching of coefficients).** If two power series agree on an interval, then their coefficients agree term by term.

This is the licence to equate coefficients, and it is the step that converts one differential equation into infinitely many algebraic equations. It fails for ordinary functions: two different functions can agree on an interval without being equal, and two different trigonometric sums can agree at infinitely many points. For power series, agreement on any interval is agreement everywhere the series converge.

### 2.3 The index-shifting lemma

> **Lemma (shift of index).** Let $k$ be an integer. Then, as formal series,
>
> $$
> \sum_{n=N}^{\infty}A_{n}x^{n+k}=\sum_{m=N+k}^{\infty}A_{m-k}x^{m},
> $$
>
> and
>
> $$
> \sum_{n=N}^{\infty}A_{n}x^{n-k}=\sum_{m=N-k}^{\infty}A_{m+k}x^{m}.
> $$

The lemma says only that relabelling the summation letter changes the range of summation in a dictated way. Its content is entirely in the range: the lower limit moves with the exponent, and a reader who shifts the exponent but not the lower limit silently deletes or invents terms. The proof is given in Section 3.1.

> **Corollary (alignment rule).** A term of the form $x^{k}y$ contributes to the coefficient of $x^{m}$ the value $c_{m-k}$, and a term of the form $x^{k}y'$ contributes $\left(m-k+1\right)c_{m-k+1}$, with the understanding that a coefficient with negative index is zero.

The corollary is the working form of the lemma, and it is worth deriving once by hand for the two cases $x^{2}y''$ and $xy$, which are the two that appear in almost every question.

### 2.4 Existence of a series solution for a first-order equation

> **Theorem (first-order linear equation with analytic coefficients).** Let $P$ and $Q$ be analytic at $x_{0}$, with power series convergent for $\left|x-x_{0}\right|<R$. Then the equation
>
> $$
> \frac{dy}{dx}+P(x)y=Q(x)
> $$
>
> has exactly one solution analytic at $x_{0}$ with any prescribed value $y(x_{0})=y_{0}$, and its power series converges for $\left|x-x_{0}\right|<R$.

The theorem converts the local existence statement of Section 1.5 into a statement about series, and it adds the information that the radius is at least as large as the smaller radius of the two coefficient series. The proof is the recurrence of Section 3.3, together with an estimate showing that the coefficients so produced do not grow too fast; the estimate is not needed for computation.

### 2.5 Existence of two series solutions at an ordinary point

> **Theorem (ordinary point).** Let $x_{0}$ be an ordinary point of the normalised equation $y''+p(x)y'+q(x)y=0$, so that $p$ and $q$ are analytic at $x_{0}$ with series convergent for $\left|x-x_{0}\right|<R$. Then there are two solutions
>
> $$
> y_{1}=\sum_{n=0}^{\infty}a_{n}\left(x-x_{0}\right)^{n},\qquad y_{2}=\sum_{n=0}^{\infty}b_{n}\left(x-x_{0}\right)^{n},
> $$
>
> analytic at $x_{0}$ and linearly independent there, and every solution on the interval is a combination $A y_{1}+B y_{2}$. Both series converge at least for $\left|x-x_{0}\right|<R$.

The freedom is exactly two-dimensional because the recurrence determines $c_{2},c_{3},c_{4},\dots$ from $c_{0}$ and $c_{1}$ and never determines $c_{0}$ and $c_{1}$ themselves. The pair is conveniently normalised by taking $\left(c_{0},c_{1}\right)=\left(1,0\right)$ for $y_{1}$ and $\left(0,1\right)$ for $y_{2}$.

> **Corollary (radius bound).** If the only singular points of the equation are at distances $d_{1},d_{2},\dots$ from $x_{0}$, then $R$ is at least the smallest of these distances. The radius is a property of the coefficients, not of the solution.

The corollary explains why the series for the equation with singular points at $1$ and $-1$ is guaranteed only for $\left|x\right|<1$ even though the solution may be perfectly smooth beyond that point. The guarantee is local, and the true radius may be larger.

### 2.6 Existence of a Frobenius solution

> **Theorem (Frobenius, regular singular point).** Let $x_{0}$ be a regular singular point of $y''+p(x)y'+q(x)y=0$, and let $p_{0}$ and $q_{0}$ be the limits of $\left(x-x_{0}\right)p$ and $\left(x-x_{0}\right)^{2}q$ at $x_{0}$. Then the equation has at least one solution of the form
>
> $$
> y=x^{r}\sum_{n=0}^{\infty}c_{n}x^{n},\qquad c_{0}\neq 0,
> $$
>
> where $r$ is a root of the indicial equation of Section 2.7 and the series converges for $0<\left|x\right|<R$ with $R$ the distance to the next singular point.

The theorem promises one solution, not two. The second solution may require a logarithmic factor, and that is the content of Section 2.8. At an irregular singular point the theorem fails outright: no power of $x$ times an analytic function can reproduce the behaviour of a solution there.

### 2.7 The indicial equation

> **Lemma (indicial equation).** Let $x_{0}$ be a regular singular point and write the coefficients in the form
>
> $$
> \left(x-x_{0}\right)p(x)=\sum_{m=0}^{\infty}p_{m}\left(x-x_{0}\right)^{m},\qquad \left(x-x_{0}\right)^{2}q(x)=\sum_{m=0}^{\infty}q_{m}\left(x-x_{0}\right)^{m}.
> $$
>
> Then the admissible exponents $r$ in the Frobenius template are the roots of
>
> $$
> r\left(r-1\right)+p_{0}r+q_{0}=0 .
> $$

The polynomial on the left is called the indicial polynomial, and its two roots are the indicial roots. For the equation $2x^{2}y''-xy'+\left(1-x^{2}\right)y=0$ the coefficients are $p_{0}$ equal to $-\frac{1}{2}$ and $q_{0}$ equal to $\frac{1}{2}$, so the indicial equation is

$$
r\left(r-1\right)-\frac{r}{2}+\frac{1}{2}=0 ,
$$

which is $2r^{2}-3r+1=0$, that is $\left(2r-1\right)\left(r-1\right)=0$. The roots are $r=1$ and $r=\frac{1}{2}$.

### 2.8 The three cases for the second solution

> **Theorem (form of the second solution).** Let $r_{1}$ and $r_{2}$ be the indicial roots with $\operatorname{Re}r_{1}\ge\operatorname{Re}r_{2}$.
>
> (a) If $r_{1}-r_{2}$ is not an integer, there are two independent solutions of Frobenius type,
>
> $$
> y_{1}=x^{r_{1}}\sum_{n=0}^{\infty}a_{n}x^{n},\qquad y_{2}=x^{r_{2}}\sum_{n=0}^{\infty}b_{n}x^{n}.
> $$
>
> (b) If $r_{1}=r_{2}=r$, the first solution is of Frobenius type and the second has the form
>
> $$
> y_{2}=y_{1}\ln x+x^{r}\sum_{n=0}^{\infty}b_{n}x^{n}.
> $$
>
> (c) If $r_{1}-r_{2}=N$ is a positive integer, the second solution has the form
>
> $$
> y_{2}=C\,y_{1}\ln x+x^{r_{2}}\sum_{n=0}^{\infty}b_{n}x^{n},
> $$
>
> where $C$ is a constant that may turn out to be zero.

Case (c) is the one that costs marks, because the constant $C$ is not always non-zero and because the recurrence for the coefficients $b_{n}$ breaks down at the step $n=N$. The appearance of $\ln x$ is not an accident of algebra; it reflects the fact that between two roots differing by an integer the two solution families merge, in the same way that a repeated root of the auxiliary equation in the constant-coefficient case produces a factor $x$.

### 2.9 Superposition and the non-homogeneous problem

> **Theorem (superposition).** If $L$ denotes the operator $L[y]=y''+p y'+q y$, if $L[y_{h}]=0$ and $L[y_{p}]=F$, then $L[y_{p}+y_{h}]=F$. Consequently the general solution of $L[y]=F$ is $y_{p}$ plus the general solution of $L[y]=0$.

> **Corollary (series forcing).** If $F$ is analytic at $x_{0}$, so that $F=\sum f_{n}\left(x-x_{0}\right)^{n}$, then a series of the ordinary template may be substituted into $L[y]=F$ and coefficients matched against the coefficients $f_{n}$. The homogeneous coefficients remain free, and the particular solution is fixed once the free coefficients are assigned any convenient values.

The corollary is the practical form of the theorem: the presence of a right-hand side changes the equation for finitely or infinitely many coefficients, but it never changes the shape of the recurrence for large $n$. That is why the same bookkeeping, and the same control of indices, serves both the homogeneous and the non-homogeneous problem.

### 2.10 Identification with a known solution

> **Corollary (identification).** If a series solution has been computed and the resulting series is recognised as the expansion of an elementary function, then that function is the solution, by uniqueness.

This corollary is the cheapest possible check on a long computation. A first-order calculation that produces $1+x+\frac{x^{2}}{2}+\frac{x^{3}}{6}+\cdots$ must be the expansion of $e^{x}$, and a second-order calculation on $y''-y=0$ that produces $1+\frac{x^{2}}{2}+\frac{x^{4}}{24}+\cdots$ must be the expansion of $\cosh x$. If the computed terms do not match a series that is known to solve the equation, the recurrence is wrong.

## 3. Formal Proofs, Derivations, and Methods

### 3.1 Proof of the index-shift lemma

Let $k$ be a fixed integer and consider the series $\sum_{n=N}^{\infty}A_{n}x^{n+k}$. Define a new summation letter by $m=n+k$. As $n$ runs through the integers from $N$ upwards, $m$ runs through the integers from $N+k$ upwards, and the correspondence is one to one. Moreover $n=m-k$, so $A_{n}=A_{m-k}$ and $x^{n+k}=x^{m}$. Therefore

$$
\sum_{n=N}^{\infty}A_{n}x^{n+k}=\sum_{m=N+k}^{\infty}A_{m-k}x^{m} .
$$

Replacing $k$ by $-k$ gives the second identity,

$$
\sum_{n=N}^{\infty}A_{n}x^{n-k}=\sum_{m=N-k}^{\infty}A_{m+k}x^{m} .
$$

The proof contains no analysis, and that is the point: the shift is a relabelling, so it can never change the value of the series. It can, however, change the *appearance* of the series, and the lower limit must move with the exponent. If a term $x^{2}y''$ is written as

$$
x^{2}\sum_{n=0}^{\infty}n(n-1)c_{n}x^{n-2}=\sum_{n=0}^{\infty}n(n-1)c_{n}x^{n},
$$

the shift has not been performed at all and the lower limit is still $0$; the exponent is now $n$, so the coefficient of $x^{0}$ is $0\cdot(-1)c_{0}$, which is zero. Writing instead

$$
x^{2}\sum_{n=2}^{\infty}n(n-1)c_{n}x^{n-2}=\sum_{m=0}^{\infty}(m+2)(m+1)c_{m+2}x^{m}
$$

performs the shift and adjusts the limit. The two expressions are equal; the second is the one that can be added to another series. The difference between them is invisible for the term $x^{2}y''$, whose $n=0$ and $n=1$ contributions vanish anyway, but it is not invisible for $xy$, where

$$
x\sum_{n=0}^{\infty}c_{n}x^{n}=\sum_{n=0}^{\infty}c_{n}x^{n+1}=\sum_{m=1}^{\infty}c_{m-1}x^{m},
$$

and the sum now starts at $m=1$. Deleting the term $m=1$ from this series would delete $c_{0}x$, a genuine term of the solution.

### 3.2 Proof of the identity theorem

The claim is that a power series vanishing on an interval has all coefficients zero. The proof is an induction on the index.

The constant term is the value at the centre, since every other term contains a positive power of $x$; hence $a_{0}=0$. Suppose now that $a_{0}=a_{1}=\cdots=a_{k-1}=0$. Then for $x$ in the interval the series reduces to

$$
\sum_{n=k}^{\infty}a_{n}x^{n}=x^{k}\sum_{n=k}^{\infty}a_{n}x^{n-k}=0 .
$$

For $x\neq 0$ we may divide by $x^{k}$, obtaining

$$
\sum_{n=k}^{\infty}a_{n}x^{n-k}=0\qquad\text{for }0<\left|x\right|<R .
$$

The left-hand side is a continuous function of $x$ on the whole interval, by the lemma of Section 2.1, so letting $x\to 0$ gives $a_{k}=0$. This completes the induction, and with it the proof that two series agreeing on an interval agree coefficient by coefficient.

The theorem is used on every page of this topic. Once the differential equation has been converted into a single series equal to another series, equality on an interval licenses the conclusion that the coefficient of each power vanishes separately, and that is what produces the recurrence.

### 3.3 Legitimacy of term-by-term differentiation

Term-by-term differentiation of a power series is valid inside the radius of convergence, and the differentiated series has the same radius. The reason is that the coefficients $n c_{n}$ grow only polynomially faster than $c_{n}$, while convergence of $\sum c_{n}r^{n}$ at a radius $r<R$ is governed by geometric decay, which is fast enough to absorb a polynomial factor. Applying the result $k$ times justifies differentiating the templates as often as the order of the equation requires, and it also justifies the statement that a solution analytic at $x_{0}$ has derivatives of all orders there.

### 3.4 Derivation of the recurrence for a first-order equation

Consider

$$
\frac{dy}{dx}+P(x)y=Q(x)
$$

with $P$ and $Q$ analytic at $0$, say $P=\sum_{k\ge 0}p_{k}x^{k}$ and $Q=\sum_{n\ge 0}q_{n}x^{n}$. Write the unknown as $y=\sum_{n\ge 0}c_{n}x^{n}$.

Step 1. Differentiate the template, shifting the index so that the result is a sum of powers $x^{n}$.

$$
\frac{dy}{dx}=\sum_{n=0}^{\infty}(n+1)c_{n+1}x^{n}
$$

Step 2. Form the product $Py$ by collecting, for each power $x^{n}$, all pairwise products whose exponents add to $n$.

$$
P(x)y=\left(\sum_{k=0}^{\infty}p_{k}x^{k}\right)\left(\sum_{n=0}^{\infty}c_{n}x^{n}\right)=\sum_{n=0}^{\infty}\left(\sum_{k=0}^{n}p_{k}c_{n-k}\right)x^{n}
$$

Step 3. Substitute both into the equation and equate the coefficient of $x^{n}$ to $q_{n}$.

$$
(n+1)c_{n+1}+\sum_{k=0}^{n}p_{k}c_{n-k}=q_{n}
$$

Step 4. Separate the $k=0$ term, which is the only one containing the unknown $c_{n+1}$, and solve.

$$
c_{n+1}=\frac{q_{n}-p_{0}c_{n}-\sum_{k=1}^{n}p_{k}c_{n-k}}{n+1}
$$

The division by $n+1$ is always legitimate, because $n+1$ is a positive integer. This is the structural reason a first-order equation at an ordinary point always has one analytic solution: no coefficient in the recurrence ever vanishes, so no obstruction can occur.

Step 5. Specialise to $P$ equal to $-1$ and $Q$ equal to $0$, which is the equation $y'=y$. Then $p_{0}=-1$ and every $q_{n}$ is zero, so

$$
(n+1)c_{n+1}-c_{n}=0\qquad\Longrightarrow\qquad c_{n+1}=\frac{c_{n}}{n+1}.
$$

Step 6. Specialise instead to $P$ equal to $-2x$ and $Q$ equal to $0$, which is $y'=2xy$. Then $p_{0}=0$ and $p_{1}=-2$, so the general relation becomes

$$
(n+1)c_{n+1}-2c_{n-1}=0 ,
$$

with the understanding that $c_{-1}=0$. The vanishing of $p_{0}$ has removed $c_{n}$ from the relation and replaced it by $c_{n-1}$, which is why odd and even coefficients decouple.

### 3.5 Derivation of the recurrence at an ordinary point

Now consider the second-order equation in normalised form

$$
\frac{d^{2}y}{dx^{2}}+p(x)\frac{dy}{dx}+q(x)y=0 ,
$$

with $p=\sum_{k\ge 0}p_{k}x^{k}$ and $q=\sum_{k\ge 0}q_{k}x^{k}$ analytic at $0$, and with $y=\sum_{n\ge 0}c_{n}x^{n}$.

Step 1. Differentiate twice, shifting both times.

$$
\frac{d^{2}y}{dx^{2}}=\sum_{n=0}^{\infty}(n+2)(n+1)c_{n+2}x^{n}
$$

Step 2. Multiply $p$ by $y'$ and $q$ by $y$, collecting by powers of $x$.

$$
p(x)\frac{dy}{dx}=\sum_{n=0}^{\infty}\left(\sum_{k=0}^{n}p_{k}(n-k+1)c_{n-k+1}\right)x^{n}
$$

$$
q(x)y=\sum_{n=0}^{\infty}\left(\sum_{k=0}^{n}q_{k}c_{n-k}\right)x^{n}
$$

Step 3. Add the three series, equate the coefficient of $x^{n}$ to zero, and isolate the three terms belonging to $k=0$.

$$
(n+2)(n+1)c_{n+2}+p_{0}(n+1)c_{n+1}+q_{0}c_{n}+\sum_{k=1}^{n}\left[p_{k}(n-k+1)c_{n-k+1}+q_{k}c_{n-k}\right]=0
$$

Step 4. Solve for $c_{n+2}$.

$$
c_{n+2}=-\frac{p_{0}(n+1)c_{n+1}+q_{0}c_{n}+\sum_{k=1}^{n}\left[p_{k}(n-k+1)c_{n-k+1}+q_{k}c_{n-k}\right]}{(n+2)(n+1)}
$$

Step 5. Read off the consequences. The divisor $(n+2)(n+1)$ is never zero for $n\ge 0$, so the relation determines $c_{2}$ from $c_{0}$ and $c_{1}$, then $c_{3}$ from $c_{0},c_{1},c_{2}$, and so on indefinitely. No relation ever contains $c_{0}$ or $c_{1}$ as the isolated unknown, so neither is ever determined. That is precisely the two-parameter freedom asserted in the theorem of Section 2.5, and it is the reason the ordinary-point method delivers the general solution and not merely one solution.

Step 6. Note the role of $p_{0}$ and $q_{0}$. They enter the first three terms and therefore shape the low-order coefficients, but they do not affect the solubility of the recurrence. At a singular point the divisor gains a factor depending on $n$ in such a way that it can vanish, and that is the entire difference between the two cases.

### 3.6 Derivation of the indicial equation

At a regular singular point the normalised coefficients are singular, so the device of Section 3.5 cannot be applied directly. Multiply the equation through by $x^{2}$ instead, which clears the singularity.

$$
x^{2}\frac{d^{2}y}{dx^{2}}+x^{2}p(x)\frac{dy}{dx}+x^{2}q(x)y=0
$$

By hypothesis $xp(x)$ and $x^{2}q(x)$ are analytic at $0$, so write

$$
xp(x)=\sum_{m=0}^{\infty}p_{m}x^{m},\qquad x^{2}q(x)=\sum_{m=0}^{\infty}q_{m}x^{m}.
$$

Step 1. Substitute the Frobenius template $y=\sum_{n\ge 0}c_{n}x^{n+r}$ and differentiate.

$$
x^{2}\frac{d^{2}y}{dx^{2}}=\sum_{n=0}^{\infty}(n+r)(n+r-1)c_{n}x^{n+r}
$$

$$
x^{2}p(x)\frac{dy}{dx}=x\left(xp(x)\right)\frac{dy}{dx}=\sum_{m=0}^{\infty}\sum_{n=0}^{\infty}p_{m}(n+r)c_{n}x^{n+r+m}
$$

$$
x^{2}q(x)y=\sum_{m=0}^{\infty}\sum_{n=0}^{\infty}q_{m}c_{n}x^{n+r+m}
$$

Step 2. Collect the lowest power, which is $x^{r}$ and arises only from $m=0$ in the double sums together with $n=0$ in the first sum.

$$
\left[r(r-1)+p_{0}r+q_{0}\right]c_{0}x^{r}+\left(\text{terms of higher degree}\right)=0
$$

Step 3. Equate the coefficient of $x^{r}$ to zero. Because $c_{0}\neq 0$ by the normalisation of the template, the bracket itself must vanish.

$$
r(r-1)+p_{0}r+q_{0}=0
$$

This is the indicial equation. Its two roots are the only exponents for which a Frobenius series can begin, and the reason is visible in the calculation: $r$ was chosen precisely so that the lowest power in $x^{2}y''$ cancels the lowest powers contributed by $x^{2}py'$ and $x^{2}qy$.

Step 4. Record the general coefficient relation for later use. Collecting $x^{n+r}$ for $n\ge 1$ gives

$$
F(n+r)c_{n}+\sum_{m=1}^{n}\left[p_{m}(n+r-m)+q_{m}\right]c_{n-m}=0 ,
$$

where $F$ is the indicial polynomial

$$
F(s)=s(s-1)+p_{0}s+q_{0}=(s-r_{1})(s-r_{2}).
$$

The factorisation is the key to everything that follows: the coefficient multiplying $c_{n}$ is the indicial polynomial evaluated at the shifted exponent $n+r$, and it vanishes exactly when $n+r$ equals one of the roots.

### 3.7 The three cases of indicial roots

Assume $r_{1}$ and $r_{2}$ are the roots with $r_{1}-r_{2}$ not a negative number, and take the larger root first. Put $r=r_{1}$ in the relation of Step 4. The coefficient of $c_{n}$ is $F(n+r_{1})=n\left(n+r_{1}-r_{2}\right)$. For $n\ge 1$ this is non-zero unless $n=r_{2}-r_{1}$, which is negative and therefore impossible. Hence every $c_{n}$ with $n\ge 1$ is determined by $c_{0}$, and one Frobenius solution exists.

The second solution is best obtained from reduction of order, which handles all three cases at once and shows exactly where a logarithm comes from.

> **Lemma (reduction of order).** If $y_{1}$ is a non-zero solution of $y''+py'+qy=0$ on an interval, then a second independent solution is
>
> $$
> y_{2}=y_{1}\int\frac{\exp\left(-\int p\,dx\right)}{y_{1}^{2}}\,dx .
> $$

The lemma is proved by writing $y_{2}=vy_{1}$ and substituting; the equation for $v$ loses its $v$ term and becomes $\left(v'y_{1}^{2}\right)'=-p\,v'y_{1}^{2}$, which integrates directly.

Now apply the lemma with $y_{1}=x^{r_{1}}u(x)$, where $u$ is analytic with $u(0)=1$. Since $p=p_{0}x^{-1}+\left(\text{analytic}\right)$, we have $\exp\left(-\int p\,dx\right)=x^{-p_{0}}v(x)$ with $v$ analytic and $v(0)\neq 0$. The indicial roots satisfy $r_{1}+r_{2}=1-p_{0}$, so the exponent in the integrand is

$$
-p_{0}-2r_{1}=r_{2}-r_{1}-1 .
$$

Writing $g=v/u^{2}$, which is analytic with $g(0)\neq 0$, the integrand is

$$
\frac{\exp\left(-\int p\,dx\right)}{y_{1}^{2}}=x^{r_{2}-r_{1}-1}g(x).
$$

Step 1. Case of non-integer difference. If $r_{1}-r_{2}$ is not an integer then $r_{2}-r_{1}-1$ is not a negative integer, so the integral of $x^{r_{2}-r_{1}-1}g(x)$ is $x^{r_{2}-r_{1}}$ times an analytic function, and $y_{2}=x^{r_{2}}$ times an analytic function. No logarithm appears, and both solutions are of Frobenius type.

Step 2. Case of equal roots. Put $r_{1}=r_{2}=\rho$, so the exponent is $-1$ and the integrand is $g(0)x^{-1}$ plus an analytic function. The integral is $g(0)\ln x$ plus an analytic function, and therefore

$$
y_{2}=g(0)\,y_{1}\ln x+x^{\rho}\left(\text{analytic}\right),
$$

with $g(0)\neq 0$. The logarithm is unavoidable, its coefficient is non-zero, and the second solution is not of Frobenius type. This is the analytic explanation of the rule that equal indicial roots force a term $y_{1}\ln x$.

Step 3. Case of integer difference. Let $r_{1}-r_{2}=N$ with $N$ a positive integer. The exponent is $-N-1$, and expanding the analytic part gives

$$
x^{-N-1}g(x)=\frac{g_{0}}{x^{N+1}}+\frac{g_{1}}{x^{N}}+\cdots+\frac{g_{N}}{x}+g_{N+1}+\cdots .
$$

Every term integrates to a power of $x$ except the term $g_{N}/x$, which integrates to $g_{N}\ln x$. Hence

$$
y_{2}=g_{N}\,y_{1}\ln x+x^{r_{2}}\left(\text{analytic}\right),
$$

and the coefficient of the logarithm is $g_{N}$, which may be zero. When $g_{N}=0$ no logarithm survives, as happens for Euler's equation $x^{2}y''+xy'-4y=0$, whose roots $2$ and $-2$ differ by an integer and whose solutions are the pure powers $x^{2}$ and $x^{-2}$.

Step 4. Record the practical test. At an integer difference one does not assume a logarithm; one computes $y_{2}$ from the reduction formula, or one attempts the Frobenius series with the smaller root and observes whether the coefficient $c_{N}$ is forced or free. If the recurrence at $n=N$ reads $0\cdot c_{N}=0$, the constant is free and the family is larger than the single series; if it reads $0\cdot c_{N}=(\text{non-zero})$, no Frobenius solution with that root exists and the logarithm is present.

### 3.8 The method at an ordinary point

The algorithm is fixed, and every ordinary-point question in the course follows it.

1. Normalise the equation and identify the singular points; confirm that the chosen expansion point is ordinary, and record the guaranteed radius.
2. Write the template $y=\sum_{n\ge 0}c_{n}x^{n}$ and state that $c_{0}$ and $c_{1}$ are arbitrary.
3. Differentiate twice, shifting indices so that every series is a sum of powers $x^{n}$.
4. Substitute and multiply out; collect into a single series together with any terms that stand outside the common range of summation.
5. Equate the coefficient of each power to zero and solve the lowest two or three relations separately, because they usually differ from the general relation.
6. State the general recurrence for the remaining coefficients.
7. Compute the coefficients up to the requested order, group them by $c_{0}$ and by $c_{1}$, and write the answer both as two explicit series and as a sum.
8. Check the answer by substituting the first few terms back, or by identifying the series with a known function.

The separate treatment of the lowest relations is where marks are lost. The coefficient of $x^{0}$ typically determines $c_{2}$ and contains no $c_{1}$; the coefficient of $x^{1}$ typically determines $c_{3}$ and contains $c_{1}$ but not $c_{2}$. Applying the general recurrence at $n=0$ or $n=1$ gives nonsense, because the general recurrence was derived by collecting all contributions to $x^{n}$ and the lowest powers receive fewer contributions.

### 3.9 The method at a regular singular point

1. Normalise, confirm that the point is singular, and verify regularity by computing $xp$ and $x^{2}q$.
2. Compute $p_{0}$ and $q_{0}$ as the constant terms of those two products.
3. Write the indicial equation $r(r-1)+p_{0}r+q_{0}=0$ and solve it, naming the roots $r_{1}$ and $r_{2}$ with $r_{1}-r_{2}$ not a negative real number.
4. Substitute $y=x^{r}\sum c_{n}x^{n}$ and align indices, keeping the factor $x^{r}$ throughout.
5. Read the coefficient of $x^{r}$ as the indicial equation, which confirms the roots but adds no new information.
6. Read the coefficient of $x^{n+r}$ for $n\ge 1$ as the recurrence, and note that the divisor contains $F(n+r)$; if the divisor vanishes for some $n$ at the chosen root, record the obstruction instead of dividing.
7. Compute the coefficients for the larger root first, since those are always available; then handle the smaller root according to the case.
8. Write the general solution and, for a regular singular point at $0$, state the interval $0<\left|x\right|<R$.

A useful bookkeeping device is to keep the factor $x^{r}$ outside every display until the very last line. The coefficient recurrence is then a relation among numbers $c_{n}$ only, and the powers of $x$ never have to be tracked twice.

### 3.10 The non-homogeneous equation

There are two routes, and both are examined.

Route one is to substitute the ordinary template directly into $L[y]=F$ with $F=\sum f_{n}x^{n}$ and match coefficients including the $f_{n}$. The homogeneous recurrence is recovered for every $n$ at which $f_{n}=0$, and is modified only where the forcing is non-zero. If the forcing is a polynomial of degree $d$, only the relations for $n\le d$ are modified.

Route two uses the homogeneous solutions and variation of parameters.

> **Lemma (variation of parameters).** If $y_{1}$ and $y_{2}$ are independent solutions of $y''+py'+qy=0$ with Wronskian $W=y_{1}y_{2}'-y_{1}'y_{2}$, then a particular solution of $y''+py'+qy=F$ is
>
> $$
> y_{p}=-y_{1}\int\frac{y_{2}F}{W}\,dx+y_{2}\int\frac{y_{1}F}{W}\,dx .
> $$

Route two is preferable when the homogeneous solutions are known in closed form and the forcing is a single function such as $x$ or $e^{x}$; route one is preferable when the forcing is itself a series, or when the answer is required in the same series form as the homogeneous solution. The two routes must agree, and comparing them is a strong check, since a particular solution found by one method must differ from a particular solution found by the other only by a homogeneous solution.

### 3.11 A worked skeleton of the bookkeeping

Before any specific example, it is worth doing the bookkeeping once in the abstract, because the same three alignments recur. Take the equation

$$
\left(1-x^{2}\right)y''-2xy'+\lambda y=0
$$

at the ordinary point $0$. The three terms contribute as follows: $y''$ contributes $(m+2)(m+1)c_{m+2}$ to the power $x^{m}$; the term $-x^{2}y''$ contributes $-m(m-1)c_{m}$; the term $-2xy'$ contributes $-2mc_{m}$; and $\lambda y$ contributes $\lambda c_{m}$. All four contributions are written against the same power $x^{m}$, so the coefficient relation is

$$
(m+2)(m+1)c_{m+2}-\left[m(m-1)+2m-\lambda\right]c_{m}=0 ,
$$

that is

$$
c_{m+2}=\frac{m(m+1)-\lambda}{(m+2)(m+1)}c_{m} .
$$

The alignment has produced a two-term recurrence linking $c_{m+2}$ to $c_{m}$, so the odd and even coefficients separate. That separation is the reason Legendre's equation has one polynomial solution and one infinite solution for each integer $\lambda$ of the form $n(n+1)$: the parity that does not terminate produces the infinite series. The derivation is included here as a model of the alignment step, and the same Legendre relation is used again in the exercises of Section 5.

## 4. Representative Worked Examples and Solutions

### 4.1 Problem: the first-order equation $y'=y$ by power series

Obtain the power series solution of

$$
\frac{dy}{dx}=y
$$

in ascending powers of $x$, and verify that it agrees with the solution obtained by separation of variables.

### 4.2 Solution: check the hypotheses, recur, then identify

Step 1. Check the three conditions for the right-hand side $f(x,y)=y$. The function is a polynomial, hence continuous and single valued on the whole plane; it is bounded on every bounded domain; and $\frac{\partial f}{\partial y}=1$ is continuous everywhere. The existence theorem therefore applies, and a power series solution exists with radius of convergence at least the distance to the nearest obstruction, of which there is none.

Step 2. Write the template and differentiate it.

$$
y=\sum_{n=0}^{\infty}c_{n}x^{n},\qquad \frac{dy}{dx}=\sum_{n=0}^{\infty}(n+1)c_{n+1}x^{n}
$$

Step 3. Substitute both sides and equate the coefficients of $x^{n}$.

$$
(n+1)c_{n+1}=c_{n}
$$

Step 4. Iterate the recurrence from $n=0$ upwards.

$$
c_{1}=c_{0},\qquad c_{2}=\frac{c_{1}}{2}=\frac{c_{0}}{2},\qquad c_{3}=\frac{c_{2}}{3}=\frac{c_{0}}{6},\qquad c_{4}=\frac{c_{3}}{4}=\frac{c_{0}}{24},\qquad c_{5}=\frac{c_{0}}{120}
$$

Step 5. Assert and prove the general pattern by induction: if $c_{n}=\frac{c_{0}}{n!}$ then $c_{n+1}=\frac{c_{n}}{n+1}=\frac{c_{0}}{(n+1)!}$, so the pattern holds for every $n$.

Step 6. Write the answer in expanded form and then in summation form.

$$
y=c_{0}\left(1+x+\frac{x^{2}}{2}+\frac{x^{3}}{6}+\frac{x^{4}}{24}+\frac{x^{5}}{120}+\cdots\right)
$$

$$
y=c_{0}\sum_{n=0}^{\infty}\frac{x^{n}}{n!}
$$

Step 7. Identify the series. The bracket is the exponential series, so $y=c_{0}e^{x}$, which is exactly the result of separating the variables.

Step 8. Verify by substitution. Differentiating the series term by term returns the same series shifted by one index, which is the original equation; and evaluating at $x=0$ gives $y(0)=c_{0}$, so $c_{0}$ is the prescribed value.

Step 9. Note the interpretation: the free coefficient is the value of the solution at the expansion point, and the series converges for every $x$.

### 4.3 Problem: a first-order equation with a prescribed value

Solve $y'=2xy$ subject to $y(0)=3$, giving at least five non-zero terms.

### 4.4 Solution: the recurrence separates the odd and even coefficients

Step 1. Record the initial condition as a statement about the constant term: $y(0)=c_{0}=3$.

Step 2. Substitute the template and its derivative.

$$
\sum_{n=0}^{\infty}(n+1)c_{n+1}x^{n}=2x\sum_{n=0}^{\infty}c_{n}x^{n}=\sum_{n=0}^{\infty}2c_{n}x^{n+1}
$$

Step 3. Shift the right-hand side so that both sides are sums of powers $x^{n}$, using the lemma of Section 2.3.

$$
\sum_{n=0}^{\infty}(n+1)c_{n+1}x^{n}=\sum_{n=1}^{\infty}2c_{n-1}x^{n}
$$

Step 4. Equate the coefficient of $x^{0}$ separately, because the right-hand side has no term of degree zero.

$$
c_{1}=0
$$

Step 5. Equate the coefficient of $x^{n}$ for $n\ge 1$.

$$
(n+1)c_{n+1}=2c_{n-1}
$$

Step 6. Compute from the bottom, using $c_{0}=3$ and $c_{1}=0$.

$$
c_{2}=\frac{2c_{0}}{2}=3,\qquad c_{3}=\frac{2c_{1}}{3}=0,\qquad c_{4}=\frac{2c_{2}}{4}=\frac{3}{2},\qquad c_{5}=\frac{2c_{3}}{5}=0
$$

Step 7. Continue to the next two non-zero coefficients.

$$
c_{6}=\frac{2c_{4}}{6}=\frac{1}{2},\qquad c_{7}=0,\qquad c_{8}=\frac{2c_{6}}{8}=\frac{1}{8}
$$

Step 8. State the answer.

$$
y=3+3x^{2}+\frac{3}{2}x^{4}+\frac{1}{2}x^{6}+\frac{1}{8}x^{8}+\cdots
$$

Step 9. Identify the pattern: the coefficient of $x^{2k}$ is $\frac{3}{k!}$, so

$$
y=3\sum_{k=0}^{\infty}\frac{x^{2k}}{k!}=3e^{x^{2}} .
$$

Step 10. Verify. Differentiating gives $y'=6xe^{x^{2}}$, while $2xy=2x\cdot 3e^{x^{2}}=6xe^{x^{2}}$, so the equation holds; and $y(0)=3$, so the initial condition holds. The odd coefficients vanish because the equation contains only even powers of $x$ apart from the derivative, which is the parity argument of Step 6.

### 4.5 Problem: a second-order equation at an ordinary point

Show that $x=0$ is an ordinary point of

$$
\left(x^{2}-1\right)\frac{d^{2}y}{dx^{2}}+3x\frac{dy}{dx}+xy=0 ,
$$

and find the general power series solution up to and including the term in $x^{7}$.

### 4.6 Solution: normalise, classify, then align three series

Step 1. Divide by $x^{2}-1$ to obtain the normalised form and read off the coefficients.

$$
\frac{d^{2}y}{dx^{2}}+\frac{3x}{x^{2}-1}\frac{dy}{dx}+\frac{x}{x^{2}-1}y=0
$$

Step 2. Classify the point. The two coefficients are rational with denominator $\left(x-1\right)\left(x+1\right)$, so the only singular points are $1$ and $-1$, and $x=0$ is ordinary. The distance from $0$ to the nearer singular point is one, so the two series solutions are guaranteed to converge for $\left|x\right|<1$.

Step 3. Write the template with its first two derivatives.

$$
y=\sum_{n=0}^{\infty}c_{n}x^{n},\qquad y'=\sum_{n=0}^{\infty}(n+1)c_{n+1}x^{n},\qquad y''=\sum_{n=0}^{\infty}(n+2)(n+1)c_{n+2}x^{n}
$$

Step 4. Multiply out the three terms of the equation, writing each against the power $x^{m}$.

$$
x^{2}y''=\sum_{m=0}^{\infty}m(m-1)c_{m}x^{m}
$$

$$
-y''=-\sum_{m=0}^{\infty}(m+2)(m+1)c_{m+2}x^{m}
$$

$$
3xy'=\sum_{m=0}^{\infty}3m\,c_{m}x^{m}
$$

$$
xy=\sum_{m=1}^{\infty}c_{m-1}x^{m}
$$

Step 5. Add the four contributions and equate the coefficient of $x^{m}$ to zero, noting that the last sum begins at $m=1$.

$$
m(m+2)c_{m}+c_{m-1}-(m+2)(m+1)c_{m+2}=0
$$

Step 6. Treat $m=0$ separately, because the term $c_{m-1}$ is absent there.

$$
-2c_{2}=0\qquad\Longrightarrow\qquad c_{2}=0
$$

Step 7. State the general recurrence for $m\ge 1$.

$$
c_{m+2}=\frac{m(m+2)c_{m}+c_{m-1}}{(m+1)(m+2)}
$$

Step 8. Compute the coefficients with $c_{0}$ and $c_{1}$ left symbolic.

$$
c_{3}=\frac{1\cdot 3\,c_{1}+c_{0}}{2\cdot 3}=\frac{3c_{1}+c_{0}}{6},\qquad c_{4}=\frac{2\cdot 4\,c_{2}+c_{1}}{3\cdot 4}=\frac{c_{1}}{12}
$$

$$
c_{5}=\frac{3\cdot 5\,c_{3}+c_{2}}{4\cdot 5}=\frac{15c_{3}}{20}=\frac{3c_{1}+c_{0}}{8}
$$

Step 9. Continue two steps further, to obtain the coefficients of $x^{6}$ and $x^{7}$.

$$
c_{6}=\frac{4\cdot 6\,c_{4}+c_{3}}{5\cdot 6}=\frac{24\cdot\frac{c_{1}}{12}+\frac{3c_{1}+c_{0}}{6}}{30}=\frac{15c_{1}+c_{0}}{180}
$$

$$
c_{7}=\frac{5\cdot 7\,c_{5}+c_{4}}{6\cdot 7}=\frac{35\cdot\frac{3c_{1}+c_{0}}{8}+\frac{c_{1}}{12}}{42}=\frac{105c_{0}+317c_{1}}{1008}
$$

Step 10. Assemble the general solution by collecting the terms in $c_{0}$ and in $c_{1}$ separately.

$$
y=c_{0}\left(1+\frac{x^{3}}{6}+\frac{x^{5}}{8}+\frac{x^{6}}{180}+\frac{5x^{7}}{48}+\cdots\right)+c_{1}\left(x+\frac{x^{3}}{2}+\frac{x^{4}}{12}+\frac{3x^{5}}{8}+\frac{x^{6}}{12}+\frac{317x^{7}}{1008}+\cdots\right)
$$

Step 11. Check the two lowest relations directly against the equation. The coefficient of $x^{0}$ in the left-hand side is $-2c_{2}$, which vanishes; the coefficient of $x^{1}$ is $3c_{1}+c_{0}-6c_{3}$, which vanishes by the computed value of $c_{3}$; the coefficient of $x^{2}$ is $8c_{2}+c_{1}-12c_{4}$, which vanishes by $c_{2}=0$ and $c_{4}=\frac{c_{1}}{12}$. Three independent checks confirm the recurrence.

Step 12. Interpret the answer. The two brackets are linearly independent: the first begins with $1$ and the second with $x$, so neither is a multiple of the other. The solution therefore has the required two arbitrary constants, and the radius of convergence is at least one.

### 4.7 Problem: Airy's equation at the origin

Find the general solution of

$$
\frac{d^{2}y}{dx^{2}}-xy=0
$$

in powers of $x$, giving four non-zero terms of each independent solution.

### 4.8 Solution: a recurrence with a gap of three

Step 1. The equation is already normalised, with $p=0$ and $q=-x$; both are analytic everywhere, so every point is ordinary and the radius of convergence is infinite.

Step 2. Substitute the template.

$$
\sum_{n=0}^{\infty}(n+2)(n+1)c_{n+2}x^{n}-\sum_{n=0}^{\infty}c_{n}x^{n+1}=0
$$

Step 3. Shift the second sum to the power $x^{n}$.

$$
\sum_{n=0}^{\infty}(n+2)(n+1)c_{n+2}x^{n}-\sum_{n=1}^{\infty}c_{n-1}x^{n}=0
$$

Step 4. Equate the coefficient of $x^{0}$.

$$
2c_{2}=0\qquad\Longrightarrow\qquad c_{2}=0
$$

Step 5. Equate the coefficient of $x^{n}$ for $n\ge 1$.

$$
(n+2)(n+1)c_{n+2}=c_{n-1}
$$

Step 6. Replace $n$ by $n-1$ to obtain the cleanest form, valid for $n\ge 0$.

$$
c_{n+3}=\frac{c_{n}}{(n+2)(n+3)}
$$

Step 7. Compute the even family with $c_{0}=1$ and $c_{1}=0$. Since $c_{2}=0$, the relation with $n=0$ gives $c_{3}=\frac{1}{6}$, and then $c_{6}=\frac{c_{3}}{4\cdot 5}=\frac{1}{180}$ and $c_{9}=\frac{c_{6}}{7\cdot 8}=\frac{1}{12960}$.

$$
y_{1}=1+\frac{x^{3}}{6}+\frac{x^{6}}{180}+\frac{x^{9}}{12960}+\cdots
$$

Step 8. Compute the odd family with $c_{0}=0$ and $c_{1}=1$. Then $c_{4}=\frac{c_{1}}{2\cdot 3}=\frac{1}{12}$, $c_{7}=\frac{c_{4}}{5\cdot 6}=\frac{1}{504}$ and $c_{10}=\frac{c_{7}}{8\cdot 9}=\frac{1}{45360}$.

$$
y_{2}=x+\frac{x^{4}}{12}+\frac{x^{7}}{504}+\frac{x^{10}}{45360}+\cdots
$$

Step 9. Write the general solution.

$$
y=A\left(1+\frac{x^{3}}{6}+\frac{x^{6}}{180}+\cdots\right)+B\left(x+\frac{x^{4}}{12}+\frac{x^{7}}{504}+\cdots\right)
$$

Step 10. Verify $y_{1}$ by substitution, keeping four terms.

$$
y_{1}''=x+\frac{x^{4}}{6}+\frac{72x^{7}}{12960}=x+\frac{x^{4}}{6}+\frac{x^{7}}{180}
$$

$$
xy_{1}=x+\frac{x^{4}}{6}+\frac{x^{7}}{180}+\frac{x^{10}}{12960}
$$

The two expressions agree through the power $x^{9}$, so the residual begins at $x^{10}$ and the retained coefficients are confirmed. The same substitution for $y_{2}$ gives $y_{2}''=x^{2}+\frac{x^{5}}{12}+\frac{x^{8}}{504}$ against $xy_{2}=x^{2}+\frac{x^{5}}{12}+\frac{x^{8}}{504}+\frac{x^{11}}{45360}$, and again the residual begins only at the first omitted power.

Step 11. Interpret. Each family contains only every third power, because the recurrence links $c_{n+3}$ to $c_{n}$. The two families are independent, the even one being even under $x\mapsto -x$ only in the sense that it is a series in $x^{3}$, and together they span the solution space.

### 4.9 Problem: Frobenius at a regular singular point

Show that $x=0$ is a regular singular point of

$$
2x^{2}\frac{d^{2}y}{dx^{2}}-x\frac{dy}{dx}+\left(1-x^{2}\right)y=0 ,
$$

find the indicial equation, and obtain four non-zero terms of each Frobenius solution.

### 4.10 Solution: two roots, two series

Step 1. Normalise the equation.

$$
\frac{d^{2}y}{dx^{2}}-\frac{1}{2x}\frac{dy}{dx}+\frac{1-x^{2}}{2x^{2}}y=0
$$

Step 2. Compute the two products and their limits.

$$
xp(x)=-\frac{1}{2},\qquad x^{2}q(x)=\frac{1-x^{2}}{2},\qquad p_{0}=-\frac{1}{2},\qquad q_{0}=\frac{1}{2}
$$

Both products are polynomials, hence analytic, so $0$ is a regular singular point.

Step 3. Write and solve the indicial equation.

$$
r(r-1)-\frac{r}{2}+\frac{1}{2}=0\qquad\Longrightarrow\qquad 2r^{2}-3r+1=0\qquad\Longrightarrow\qquad r=1\text{ or }r=\frac{1}{2}
$$

Step 4. Substitute the Frobenius template and its derivatives, keeping the factor $x^{r}$ throughout.

$$
y=\sum_{n=0}^{\infty}c_{n}x^{n+r},\qquad y'=\sum_{n=0}^{\infty}(n+r)c_{n}x^{n+r-1},\qquad y''=\sum_{n=0}^{\infty}(n+r)(n+r-1)c_{n}x^{n+r-2}
$$

Step 5. Multiply out and collect the three terms that carry the power $x^{n+r}$.

$$
2x^{2}y''=\sum_{n=0}^{\infty}2(n+r)(n+r-1)c_{n}x^{n+r},\qquad -xy'=-\sum_{n=0}^{\infty}(n+r)c_{n}x^{n+r}
$$

$$
y=\sum_{n=0}^{\infty}c_{n}x^{n+r},\qquad -x^{2}y=-\sum_{n=0}^{\infty}c_{n}x^{n+r+2}
$$

Step 6. Combine the first three sums and simplify the bracket.

$$
2(n+r)(n+r-1)-(n+r)+1=\left(2(n+r)-1\right)\left((n+r)-1\right)
$$

Step 7. Shift the last sum, which supplies the term $c_{n-2}$, and write the whole equation.

$$
\sum_{n=0}^{\infty}\left(2(n+r)-1\right)(n+r-1)c_{n}x^{n+r}-\sum_{n=2}^{\infty}c_{n-2}x^{n+r}=0
$$

Step 8. Read the coefficient of $x^{r}$ and confirm the indicial equation.

$$
\left(2r-1\right)(r-1)c_{0}=0
$$

Step 9. Read the coefficient of $x^{r+1}$, which is the first relation with no contribution from the shifted sum.

$$
\left(2r+1\right)r\,c_{1}=0\qquad\Longrightarrow\qquad c_{1}=0
$$

The factor $r$ is non-zero at both roots and the factor $2r+1$ is non-zero at both roots, so $c_{1}$ vanishes for each root separately.

Step 10. Read the coefficient of $x^{n+r}$ for $n\ge 2$.

$$
c_{n}=\frac{c_{n-2}}{\left(2(n+r)-1\right)(n+r-1)}
$$

Step 11. Put $r=1$ and compute.

$$
c_{2}=\frac{c_{0}}{5\cdot 2}=\frac{c_{0}}{10},\qquad c_{4}=\frac{c_{2}}{9\cdot 4}=\frac{c_{0}}{360},\qquad c_{6}=\frac{c_{4}}{13\cdot 6}=\frac{c_{0}}{28080},\qquad c_{8}=\frac{c_{0}}{3818880}
$$

$$
y_{1}=x\left(1+\frac{x^{2}}{10}+\frac{x^{4}}{360}+\frac{x^{6}}{28080}+\frac{x^{8}}{3818880}+\cdots\right)
$$

Step 12. Put $r=\frac{1}{2}$ and compute, this time with the denominators $\left(2n\right)\left(n-\frac{1}{2}\right)$.

$$
c_{2}=\frac{c_{0}}{6},\qquad c_{4}=\frac{c_{2}}{8\cdot\frac{7}{2}}=\frac{c_{0}}{168},\qquad c_{6}=\frac{c_{4}}{12\cdot\frac{11}{2}}=\frac{c_{0}}{11088}
$$

$$
y_{2}=x^{1/2}\left(1+\frac{x^{2}}{6}+\frac{x^{4}}{168}+\frac{x^{6}}{11088}+\cdots\right)
$$

Step 13. State the general solution, valid for $x>0$.

$$
y=Ax\left(1+\frac{x^{2}}{10}+\frac{x^{4}}{360}+\cdots\right)+Bx^{1/2}\left(1+\frac{x^{2}}{6}+\frac{x^{4}}{168}+\cdots\right)
$$

Step 14. Verify $y_{1}$ by substitution, keeping three terms. With $y=x+\frac{x^{3}}{10}+\frac{x^{5}}{360}$ the three pieces are

$$
2x^{2}y''=\frac{6x^{3}}{5}+\frac{x^{5}}{9},\qquad -xy'=-x-\frac{3x^{3}}{10}-\frac{x^{5}}{72},\qquad \left(1-x^{2}\right)y=x+\frac{x^{3}}{10}+\frac{x^{5}}{360}-x^{3}-\frac{x^{5}}{10}
$$

The coefficient of $x$ in the total is $-1+1=0$, the coefficient of $x^{3}$ is $\frac{6}{5}-\frac{3}{10}-\frac{9}{10}=0$, and the coefficient of $x^{5}$ is $\frac{1}{9}-\frac{1}{72}+\frac{1}{360}-\frac{1}{10}=0$. The lowest surviving power is therefore higher than any retained, which confirms the recurrence.

Step 15. Verify $y_{2}$ in the same way, with $y=x^{1/2}+\frac{x^{5/2}}{6}+\frac{x^{9/2}}{168}$. The three contributions are

$$
2x^{2}y''=-\frac{1}{2}x^{1/2}+\frac{5}{4}x^{5/2}+\frac{3}{16}x^{9/2},\qquad -xy'=-\frac{1}{2}x^{1/2}-\frac{5}{12}x^{5/2}-\frac{3}{112}x^{9/2}
$$

$$
\left(1-x^{2}\right)y=x^{1/2}-\frac{5}{6}x^{5/2}-\frac{27}{168}x^{9/2}
$$

and the totals at $x^{1/2}$, at $x^{5/2}$ and at $x^{9/2}$ are $-\frac{1}{2}-\frac{1}{2}+1=0$, $\frac{5}{4}-\frac{5}{12}-\frac{5}{6}=0$ and $\frac{3}{16}-\frac{3}{112}-\frac{9}{56}=0$, so the second series is confirmed to the same order.

Step 16. Interpret the result. The two roots differ by $\frac{1}{2}$, which is not an integer, so this is case (a) of the theorem and both solutions are pure Frobenius series without logarithms. The next singular point is at infinity only, since the only denominator in the normalised coefficients is $x$, so both series converge for every $x\neq 0$.

### 4.11 Problem: equal indicial roots

(a) Solve $4x^{2}y''+y=0$ about $x=0$. (b) Solve $x^{2}y''+3xy'+\left(1-x\right)y=0$ about $x=0$, giving three non-zero terms of each solution.

### 4.12 Solution: the logarithm appears, and the general theory predicts it

Step 1. Normalise the first equation and compute the products.

$$
y''+\frac{1}{4x^{2}}y=0,\qquad xp(x)=0,\qquad x^{2}q(x)=\frac{1}{4}
$$

Step 2. Write the indicial equation.

$$
r(r-1)+\frac{1}{4}=0\qquad\Longrightarrow\qquad \left(r-\frac{1}{2}\right)^{2}=0\qquad\Longrightarrow\qquad r=\frac{1}{2}\ \text{(double)}
$$

Step 3. Compute the single Frobenius solution with $r=\frac{1}{2}$. The coefficient relation is $\left(n+\frac{1}{2}\right)\left(n-\frac{1}{2}\right)c_{n}+\frac{1}{4}c_{n}=n^{2}c_{n}=0$, so every $c_{n}$ with $n\ge 1$ vanishes and $y_{1}=x^{1/2}$.

Step 4. Obtain the second solution from the reduction formula of Section 3.7. Here $p=0$, so $\exp\left(-\int p\,dx\right)=1$ and

$$
y_{2}=x^{1/2}\int\frac{1}{x}\,dx=x^{1/2}\ln x .
$$

Step 5. Confirm both solutions directly.

$$
y=x^{1/2}\quad\Longrightarrow\quad y''=-\frac{1}{4}x^{-3/2}\quad\Longrightarrow\quad 4x^{2}y''+y=-x^{1/2}+x^{1/2}=0
$$

$$
y=x^{1/2}\ln x\quad\Longrightarrow\quad y''=-\frac{1}{4}x^{-3/2}\ln x\quad\Longrightarrow\quad 4x^{2}y''+y=-x^{1/2}\ln x+x^{1/2}\ln x=0
$$

Step 6. State the answer to part (a): $y=x^{1/2}\left(A+B\ln x\right)$, and observe that the coefficient of the logarithm is non-zero, exactly as the theorem predicts for equal roots.

Step 7. Turn to part (b). Normalise and compute.

$$
y''+\frac{3}{x}y'+\frac{1-x}{x^{2}}y=0,\qquad xp(x)=3,\qquad x^{2}q(x)=1-x,\qquad p_{0}=3,\ q_{0}=1
$$

Step 8. Write the indicial equation.

$$
r(r-1)+3r+1=r^{2}+2r+1=\left(r+1\right)^{2}=0\qquad\Longrightarrow\qquad r=-1\ \text{(double)}
$$

Step 9. Substitute the template. The three non-shifted terms combine into a perfect square, and the shifted term supplies $c_{n-1}$.

$$
\sum_{n=0}^{\infty}\left(n+r+1\right)^{2}c_{n}x^{n+r}-\sum_{n=1}^{\infty}c_{n-1}x^{n+r}=0
$$

Step 10. Put $r=-1$ and read the recurrence.

$$
n^{2}c_{n}=c_{n-1}\qquad\Longrightarrow\qquad c_{n}=\frac{c_{0}}{\left(n!\right)^{2}}
$$

Step 11. Write the first solution.

$$
y_{1}=\frac{1}{x}\left(1+x+\frac{x^{2}}{4}+\frac{x^{3}}{36}+\frac{x^{4}}{576}+\cdots\right)
$$

Step 12. Obtain the second solution by the derivative device of Section 3.7. The coefficients of the general-root solution are $c_{n}(r)=c_{0}\prod_{k=1}^{n}\left(k+r+1\right)^{-2}$, so differentiating with respect to $r$ and then putting $r=-1$ multiplies $c_{n}$ by $-2\left(1+\frac{1}{2}+\cdots+\frac{1}{n}\right)$. Denoting the harmonic sum by $H_{n}$,

$$
y_{2}=y_{1}\ln x-2x^{-1}\sum_{n=1}^{\infty}\frac{H_{n}}{\left(n!\right)^{2}}x^{n} .
$$

Step 13. Expand the second solution.

$$
y_{2}=y_{1}\ln x-2-\frac{3}{4}x-\frac{11}{108}x^{2}-\frac{25}{3456}x^{3}-\frac{137}{432000}x^{4}-\cdots
$$

Step 14. Verify. Substituting $y_{1}$ into $x^{2}y''+3xy'+y-xy$ gives, for the coefficients of $x^{-1}$, $x^{0}$, $x^{1}$ and $x^{2}$,

$$
2-3+1=0,\qquad 1-1=0,\qquad \frac{3}{4}+\frac{1}{4}-1=0,\qquad \frac{1}{18}+\frac{1}{6}+\frac{1}{36}-\frac{1}{4}=0
$$

so the recurrence is confirmed at the first four stages. The leading coefficient $-2$ of the non-logarithmic part of $y_{2}$ is the limit $g(0)$ of Section 3.7, which is non-zero, so no choice of normalisation removes the logarithm.

Step 15. Interpret. Part (a) is Euler's equation in disguise, so its solutions are exact; part (b) is not, so the second solution is genuinely an infinite series plus a logarithm. In both cases the double root is the signal that a logarithm is present.

### 4.13 Problem: indicial roots differing by an integer

Solve

$$
x^{2}\frac{d^{2}y}{dx^{2}}-2x\frac{dy}{dx}+\left(2-x\right)y=0
$$

about $x=0$, and explain why the smaller indicial root yields no new series.

### 4.14 Solution: an obstruction at the step $n=N$

Step 1. Normalise and compute the products.

$$
y''-\frac{2}{x}y'+\frac{2-x}{x^{2}}y=0,\qquad xp(x)=-2,\qquad x^{2}q(x)=2-x,\qquad p_{0}=-2,\ q_{0}=2
$$

Step 2. Write the indicial equation and factor it.

$$
r(r-1)-2r+2=r^{2}-3r+2=\left(r-1\right)\left(r-2\right)=0\qquad\Longrightarrow\qquad r=2,\ r=1
$$

Step 3. Substitute the template and collect.

$$
\sum_{n=0}^{\infty}\left(n+r-1\right)\left(n+r-2\right)c_{n}x^{n+r}-\sum_{n=1}^{\infty}c_{n-1}x^{n+r}=0
$$

Step 4. Read the recurrence for $n\ge 1$.

$$
\left(n+r-1\right)\left(n+r-2\right)c_{n}=c_{n-1}
$$

Step 5. Put $r=2$, the larger root, and simplify.

$$
n\left(n+1\right)c_{n}=c_{n-1}\qquad\Longrightarrow\qquad c_{n}=\frac{c_{0}}{n!\,(n+1)!}
$$

Step 6. Write the first solution.

$$
y_{1}=x^{2}\left(1+\frac{x}{2}+\frac{x^{2}}{12}+\frac{x^{3}}{144}+\frac{x^{4}}{2880}+\frac{x^{5}}{86400}+\cdots\right)
$$

Step 7. Put $r=1$, the smaller root, and examine the step $n=1$, where the difference of the roots shows up.

$$
n\left(n-1\right)c_{n}=c_{n-1}\qquad\Longrightarrow\qquad 0\cdot c_{1}=c_{0}
$$

Since $c_{0}\neq 0$ by the normalisation of the Frobenius template, the relation cannot be satisfied: no Frobenius series with $r=1$ exists. This is the integer-difference obstruction, and it occurs at $n=N=1$.

Step 8. If $c_{0}$ is set to zero the obstruction disappears, but then the series is merely a multiple of $y_{1}$: the recurrence becomes $c_{n}=c_{n-1}/\left(n(n-1)\right)$ and produces $x^{2}\left(c_{1}+c_{1}\frac{x}{2}+\cdots\right)$, which is $c_{1}y_{1}$.

Step 9. Obtain the second solution from the reduction formula. With $y_{1}=x^{2}u$ and $p=-2x^{-1}$, the integrand is $x^{-2}u^{-2}$ and its expansion begins $x^{-2}-x^{-1}+\cdots$, so the logarithm survives with coefficient $-1$.

$$
y_{2}=-y_{1}\ln x-x-\frac{x^{2}}{2}+\frac{x^{3}}{2}+\frac{11x^{4}}{72}+\frac{29x^{5}}{1728}+\cdots
$$

Step 10. Verify $y_{1}$ by substitution, keeping four terms. With $y_{1}=x^{2}+\frac{x^{3}}{2}+\frac{x^{4}}{12}+\frac{x^{5}}{144}$ the four pieces are

$$
x^{2}y_{1}''=2x^{2}+3x^{3}+x^{4}+\frac{5x^{5}}{36},\qquad -2xy_{1}'=-4x^{2}-3x^{3}-\frac{2x^{4}}{3}-\frac{5x^{5}}{72}
$$

$$
2y_{1}=2x^{2}+x^{3}+\frac{x^{4}}{6}+\frac{x^{5}}{72},\qquad -xy_{1}=-x^{3}-\frac{x^{4}}{2}-\frac{x^{5}}{12}
$$

and the totals at $x^{2}$, $x^{3}$, $x^{4}$ and $x^{5}$ are all zero, which confirms the recurrence at the first four stages.

Step 11. Interpret. The two roots differ by exactly one, and at the corresponding step the coefficient of $c_{N}$ vanishes while the right-hand side does not. That is the diagnostic for case (c): one Frobenius solution, one logarithmic solution, and the constant $C$ of the theorem turns out to be non-zero.

## 5. Mathematical Extensions, Limits, and Common Errors

### 5.1 Where the series is valid, and why the radius is what it is

The radius of convergence of a series solution is fixed by the coefficients of the equation, not by the solution. The governing fact is that the radius about $x_{0}$ is at least the distance from $x_{0}$ to the nearest singular point, and that distance may be complex. The equation

$$
\left(1+x^{2}\right)y''+y=0
$$

has no real singular point at all, yet its series about $0$ cannot converge beyond $\left|x\right|=1$, because the normalised coefficient $1/\left(1+x^{2}\right)$ blows up at $x=\pm i$. A real-variable computation therefore produces a series with radius one for a reason invisible on the real line. This is not a defect of the method; it is a genuine boundary of the analytic continuation, and it warns the student that a wide interval of definition of the solution does not imply a wide interval of convergence of its Taylor series about a particular point.

For an equation with a regular singular point at $0$ and no other finite singular point, such as the Bessel-type equation of Section 4.9, the Frobenius series converge for every $x\neq 0$, and the only restriction is the sign of $x$ when the exponent $r$ is not an integer. The function $x^{1/2}$ is not real for $x<0$, so a solution containing it is a solution on $\left(0,\infty\right)$ only, or on $\left(-\infty,0\right)$ with a different branch.

### 5.2 Where the method fails

At an irregular singular point the Frobenius template is inadequate, and no amount of coefficient computation repairs it. The equation

$$
x^{3}y''+y=0
$$

has $p=0$ and $q=x^{-3}$, so $x^{2}q=x^{-1}$ is not analytic and the point is irregular. Substituting $y=x^{r}\sum c_{n}x^{n}$ produces a lowest power $x^{r-1}$, whose coefficient is $c_{0}$, and the only way to kill it is $c_{0}=0$, contradicting the normalisation. The true solutions behave like $\exp\left(\pm x^{-1/2}\right)$ near the origin, which no power series can represent. The standard treatment of such points uses asymptotic expansions, which are not convergent series but truncated series whose error is small for small $x$; that theory lies outside a first course.

A second limitation is that a power series is a local object. A solution obtained about $0$ need not extend to a point beyond the nearest singularity, and if it does, the extension is by analytic continuation rather than by the same series. Problems that require a solution on a prescribed interval therefore require the interval to be checked against the singular points before the series is trusted.

### 5.3 The meaning of the free constants

At an ordinary point the two free constants are $y(0)$ and $y'(0)$, so an initial value problem is solved by reading them off and substituting. At a regular singular point the free constants are not values of the function, because the function may be singular there; they are simply the multipliers of the two independent solutions. This is why a Frobenius problem is almost never posed with initial conditions at the singular point itself, and why an initial condition given at a nearby regular point requires solving a linear system in the two constants, not a direct substitution.

### 5.4 Extensions that the same machinery produces

Three classical families are obtained directly from the recurrence technology of this note. Legendre's equation, whose recurrence was derived in Section 3.11, produces a polynomial solution whenever the parameter equals $n(n+1)$ with $n$ a non-negative integer, because one parity of the recurrence then terminates; the terminating solution is the Legendre polynomial. Bessel's equation produces the Bessel functions, whose Frobenius exponents are $\pm\nu$ and whose second solution acquires a logarithm precisely when $2\nu$ is an integer. Hermite's equation produces the Hermite polynomials by the same termination mechanism as Legendre's. In each case the differential equation is the definition and the series is the function; the special functions are not new objects but solutions already obtained.

A further extension is the use of the series to compute numerically. Truncating after $N$ terms gives an approximation whose error is controlled by the next term, and for equations without closed-form solutions this is the standard way to evaluate the solution. The same truncation is what a computer algebra system does when it returns a series solution, and the coefficient recurrence derived here is the algorithm it uses.

### 5.5 Common errors, with their diagnoses

The following errors account for nearly all lost marks in this topic, and each is recognisable from its symptom.

1. Shifting the exponent without shifting the lower limit. The symptom is a series that begins with a term inconsistent with the previous line, or a solution that fails the substitution check at the lowest power. The cure is to write the shift explicitly with a new letter, as in Section 3.1, every time.
2. Applying the general recurrence at $n=0$ or $n=1$. The symptom is a wrong $c_{2}$ or $c_{3}$, typically a factor-of-two error. The cure is to write the coefficient of $x^{0}$ and of $x^{1}$ as separate equations before stating the general recurrence.
3. Dividing the indicial equation away. The symptom is a single exponent where two are expected, or a division by zero. The cure is to read the coefficient of $x^{r}$ first and to record the indicial equation before any division.
4. Forgetting that $c_{0}\neq 0$ in the Frobenius template. The symptom is a spurious root or a lost indicial equation, because the argument that the bracket vanishes uses $c_{0}\neq 0$.
5. Assuming the smaller root always gives a second series. The symptom is a recurrence that produces a contradiction at the step $n=N$. The cure is to check the coefficient $\left(n+r_{1}\right)\left(n+r_{2}\right)$ at each step, and to switch to the logarithmic form when it vanishes while the right-hand side does not.
6. Assuming an integer difference always gives a logarithm. The symptom is a superfluous log term in an Euler equation. The cure is to compute the constant $C$ rather than to assume it is non-zero.
7. Mixing the two roots in one recurrence. The symptom is a recurrence containing both $r_{1}$ and $r_{2}$. The cure is to fix one root and finish that series completely before starting the other.
8. Dropping the factor $x^{r}$ from the final answer. The symptom is a solution that satisfies the equation only when $r=0$. The cure is to keep the factor outside every display until the last line.
9. Treating $x^{1/2}$ as analytic at the origin. The symptom is a claim that a solution is differentiable at a singular point. The cure is to state the interval as $x>0$ whenever the exponent is not an integer.
10. Claiming an infinite radius of convergence when a complex singular point exists. The symptom is a series used outside its interval. The cure is to locate all singularities, real and complex, before quoting a radius.

### 5.6 A closing comparison of the two methods

The ordinary-point method and the Frobenius method differ in exactly one respect: the ordinary-point recurrence has a divisor that can never vanish, while the Frobenius recurrence has a divisor that vanishes at the indicial roots. Everything else - the template, the differentiation, the alignment, the matching, the recursion - is identical. A student who understands the alignment of indices has understood both methods, and a student who has memorised two separate procedures has understood neither. The three cases of indicial roots are not three techniques but three outcomes of one arithmetic question: whether the divisor of the recurrence ever reaches zero on the way up.
