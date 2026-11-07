## 1. Foundational Concepts, Definitions, and Axioms

### 1.1 What an equation of this kind actually asserts

An algebraic equation such as $3x^{2}-5x+2=0$ asserts a relationship among unknown numbers, and its solution is a number. A differential equation asserts a relationship among an unknown function and one or more of its derivatives, and its solution is a function. This change of the unknown, from a number to a function, is the single fact that explains every technique in the subject: one cannot isolate a function by arithmetic, so one identifies the type of equation, recognises the form of the solution, and then determines the constants that remain.

The course treats the unknown function as depending on a single variable in the first twelve lessons, writing it either as $y=y(x)$ or in the operator notation where $\frac{dy}{dx}$ denotes the derivative of $y$ with respect to $x$.

> **Definition (Ordinary differential equation).** An ordinary differential equation is an equation containing one or more ordinary derivatives of an unknown function of a single independent variable.

The word ordinary is not decorative. It distinguishes the case of one independent variable from the case of several, and the two cases behave very differently.

> **Definition (Partial differential equation).** A partial differential equation is an equation containing one or more partial derivatives of an unknown function of two or more independent variables.

For example, if $u=u(x,t)$ represents the temperature at position $x$ and time $t$, then

$$
\frac{\partial u}{\partial t}=k\frac{\partial^{2}u}{\partial x^{2}}
$$

is a partial differential equation, because $u$ depends on both $x$ and $t$ and the derivatives taken are partial. The ordinary equation

$$
\frac{d^{2}y}{dx^{2}}+4y=0
$$

involves only the single independent variable $x$, so it is ordinary. The subject of this course is confined to the ordinary case, and the abbreviation ODE is used throughout.

### 1.2 The notation of repeated differentiation

The symbols $\frac{dy}{dx}$, $\frac{d^{2}y}{dx^{2}}$, and in general $\frac{d^{n}y}{dx^{n}}$ mean that the operation of differentiating with respect to $x$ has been performed once, twice, and $n$ times respectively. Written out, they are

$$
\frac{dy}{dx}=y', \qquad \frac{d^{2}y}{dx^{2}}=\frac{d}{dx}\left(\frac{dy}{dx}\right)=y'', \qquad \frac{d^{n}y}{dx^{n}}=y^{(n)} .
$$

The dash notation is a shorthand for the same objects: $y'$ is the first derivative, $y''$ the second, and beyond the third dash one writes $y^{(4)}$, $y^{(5)}$ and so on. The operator $\frac{d}{dx}$ therefore acts on functions, and writing $\frac{d}{dx}$ twice is written $\frac{d^{2}}{dx^{2}}$.

It is essential to read these symbols as operations rather than as fractions. The expression $\frac{dy}{dx}$ is a single symbol denoting the derivative, and although the chain rule legitimately produces identities such as $\frac{dy}{dx}=\frac{dy}{du}\cdot\frac{du}{dx}$, treating $\frac{dy}{dx}$ as a quotient of two independent quantities without justification is a source of error. When a manipulation is legitimate, such as separating variables, the justification is that the equation can be integrated, not that $dx$ and $dy$ are numbers.

### 1.3 Order

> **Definition (Order).** The order of a differential equation is the order of the highest derivative that appears in it.

The order is read off by inspection and is the first classification a student should make. The equation $\frac{dy}{dx}=3x^{2}$ is of order one, because the highest derivative present is the first. The equation $\frac{d^{2}y}{dx^{2}}-5\frac{dy}{dx}+6y=0$ is of order two. The equation $\frac{d^{3}y}{dx^{3}}+y=0$ is of order three.

The order determines how many arbitrary constants a general solution carries, and therefore how many conditions are needed to pin down a single solution. This is the content of the next two sections.

### 1.4 Degree

> **Definition (Degree).** The degree of a differential equation is the power to which the highest-order derivative is raised, after the equation has been cleared of radicals and fractions in the derivatives.

The clause after the comma does the real work, and it is the reason that degree questions are the most frequently misanswered in the topic. The equation must first be written as a polynomial in the derivatives, with no fractional or radical expressions involving derivatives, and only then is the exponent of the highest derivative read off.

Consider four examples.

The equation

$$
\left(\frac{d^{2}y}{dx^{2}}\right)^{3}+x\left(\frac{dy}{dx}\right)^{2}=y
$$

has order two and degree three, because the highest derivative is the second and it is raised to the power three.

The equation

$$
\frac{d^{2}y}{dx^{2}}=\left[1+\left(\frac{dy}{dx}\right)^{2}\right]^{3/2}
$$

appears at first to have degree three halves, but a degree must be a positive integer, so the fractional power must be removed. Squaring both sides gives

$$
\left(\frac{d^{2}y}{dx^{2}}\right)^{2}=1+\left(\frac{dy}{dx}\right)^{2}\cdot 3+\cdots
$$

and the equation is then of order two and degree two. The moral is that the operation of clearing radicals is performed before the degree is read.

The equation $\frac{dy}{dx}+\sqrt{y}=x$ has order one and degree one, because the radical involves $y$ and not a derivative; clearing it is unnecessary for the purpose of finding the degree.

The equation $\sin\left(\frac{d^{2}y}{dx^{2}}\right)=x$ has order two but no degree, because a transcendental function of a derivative cannot be expressed as a polynomial in that derivative.

### 1.5 Linear and non-linear

A third classification, used constantly in the later lessons, distinguishes equations in which the unknown function and its derivatives appear only to the first power and are not multiplied together.

> **Definition (Linear equation).** A differential equation is linear if it can be written in the form
>
> $$
> a_{0}(x)\frac{d^{n}y}{dx^{n}}+a_{1}(x)\frac{d^{n-1}y}{dx^{n-1}}+\cdots+a_{n-1}(x)\frac{dy}{dx}+a_{n}(x)y=F(x),
> $$
>
> where the coefficients $a_{0},\dots,a_{n}$ depend on $x$ alone and not on $y$.

An equation that cannot be put in this form is non-linear. The equation $\frac{d^{2}y}{dx^{2}}+y^{2}=0$ is non-linear because $y$ is squared. The equation $y\frac{dy}{dx}=x$ is non-linear because $y$ multiplies a derivative. The equation $\frac{dy}{dx}+\sin y=x$ is non-linear because a non-linear function of $y$ appears. Linearity is the property that makes the superposition principle available, and the whole of Lessons 5 to 9 depends upon it.

### 1.6 Solution, general solution, particular solution

> **Definition (Solution).** A function $y=\phi(x)$ defined on an interval is a solution of a differential equation if, when $\phi$ and its derivatives are substituted into the equation, the two sides agree identically on that interval.

The phrase identically matters. A solution must satisfy the equation for every $x$ in the interval, not merely at selected points.

> **Definition (General solution).** The general solution of an $n$-th order differential equation is a family of solutions containing $n$ independent arbitrary constants, from which every solution on the interval can be obtained by assigning values to those constants.

> **Definition (Particular solution).** A particular solution is any single member of the family, obtained by assigning specific values to the arbitrary constants.

> **Definition (Singular solution).** A singular solution is a solution that cannot be obtained from the general solution by any assignment of the constants.

The count of constants is not a convention but a consequence of the order, and it gives the single most useful self-check in the subject: an $n$-th order equation whose general solution carries fewer than $n$ arbitrary constants is wrong.

The equation

$$
\frac{dy}{dx}=2x
$$

has order one, and its general solution is

$$
y=x^{2}+C ,
$$

one arbitrary constant. Choosing $C=3$ gives the particular solution $y=x^{2}+3$.

The equation

$$
\frac{d^{2}y}{dx^{2}}=6x
$$

has order two. Integrating once gives $\frac{dy}{dx}=3x^{2}+C_{1}$ and integrating again gives

$$
y=x^{3}+C_{1}x+C_{2},
$$

two arbitrary constants, which is the general solution. Assigning $C_{1}=2$ and $C_{2}=-1$ gives a particular solution.

The equation $\left(\frac{dy}{dx}\right)^{2}-4y=0$ has the general solution $y=(x+C)^{2}$, one constant, but it also has the solution $y=0$, which no choice of $C$ produces. That solution is singular.

### 1.7 Initial and boundary conditions

To select a particular solution from a family, one imposes conditions. An **initial condition** prescribes the value of the function and of enough of its derivatives at a single point, such as $y(0)=1$ and $y'(0)=0$. A **boundary condition** prescribes values at two or more points, such as $y(0)=0$ and $y(1)=2$.

For an $n$-th order equation, $n$ independent conditions are required. An initial value problem consists of the equation together with conditions at one point; its solution is generally unique. A boundary value problem may have no solution, one solution, or infinitely many, which is why the two kinds of problem are treated separately.

## 2. Theorems, Lemmas, and Analytical Properties

### 2.1 Order, constants, and degrees of freedom

> **Theorem (Constant count).** The general solution of an $n$-th order ordinary differential equation contains exactly $n$ essential arbitrary constants, provided the equation can be solved for the highest derivative and the relevant functions are sufficiently smooth.

The theorem is the formal statement of the counting rule used in Section 1.6. Its practical force is twofold: it tells the student how many integrations to expect, and it provides a check on the answer.

> **Corollary (Uniqueness under initial conditions).** If $n$ conditions are prescribed at a single point and are independent, they determine the $n$ constants uniquely, so the corresponding initial value problem has at most one solution.

### 2.2 The superposition principle for linear equations

> **Theorem (Superposition for the homogeneous equation).** If $y_{1}$ and $y_{2}$ both satisfy the linear homogeneous equation $L[y]=0$, where
>
> $$
> L[y]=a_{0}(x)y^{(n)}+a_{1}(x)y^{(n-1)}+\cdots+a_{n}(x)y,
> $$
>
> then every linear combination $c_{1}y_{1}+c_{2}y_{2}$ also satisfies $L[y]=0$.

> **Theorem (Superposition with a forcing term).** If $y_{p}$ satisfies the non-homogeneous equation $L[y]=F$ and $y_{h}$ satisfies the homogeneous equation $L[y]=0$, then $y_{p}+y_{h}$ satisfies $L[y]=F$.

The second theorem is the structural reason why the later lessons split the work into finding a complementary function and a particular integral, and adding them. The property fails for non-linear equations: if $y_{1}$ solves $y''+y^{2}=0$, then $2y_{1}$ does not, because $(2y_{1})''+(2y_{1})^{2}=2y_{1}''+4y_{1}^{2}$, which is not zero.

### 2.3 Existence and uniqueness

> **Theorem (Picard–Lindelöf, stated for first order).** Consider the initial value problem $y'=f(x,y)$ with $y(x_{0})=y_{0}$. If $f$ and $\frac{\partial f}{\partial y}$ are continuous in a rectangle containing $(x_{0},y_{0})$, then there is an interval about $x_{0}$ on which a solution exists and is unique.

The hypothesis on $\frac{\partial f}{\partial y}$ is a Lipschitz-type condition and cannot be dropped. The classical counterexample is

$$
y'=3y^{2/3}, \qquad y(0)=0 ,
$$

for which $y=0$ and $y=x^{3}$ are both solutions on every interval containing the origin, so uniqueness fails. This is precisely why the statement of the theorem mentions the partial derivative rather than merely continuity of $f$.

### 2.4 Geometric meaning of a first-order equation

> **Lemma (Slope field).** A first-order equation $y'=f(x,y)$ assigns to each point $(x,y)$ of the plane the slope $f(x,y)$, and its solution curves are exactly the curves whose tangent at each point has that slope.

> **Theorem (No crossings).** If $f$ and $\frac{\partial f}{\partial y}$ are continuous, two distinct solution curves of $y'=f(x,y)$ cannot cross.

The no-crossing theorem gives a cheap graphical test: a proposed family of curves that intersect cannot be the full solution family of a first-order equation satisfying the hypotheses.

### 2.5 Properties of the degree and order under elementary operations

> **Lemma (Order is not changed by rearrangement).** Multiplying an equation by a non-zero function of $x$, differentiating or integrating both sides with respect to $x$, or clearing denominators that involve $x$ alone, does not change the order.

> **Lemma (Degree can change under rearrangement).** The degree is not invariant under arbitrary manipulation, because clearing radicals and fractions can require raising both sides to a power. It is well defined only after the equation has been written as a polynomial in the derivatives.

Together these two lemmas explain an asymmetry that confuses many students: order is a robust property of the equation, whereas degree is a property of the particular algebraic form in which the equation is written, and must always be reported for the cleared form.

### 2.6 Formation of differential equations

> **Theorem (Elimination of constants).** A family of curves depending on $n$ arbitrary constants satisfies an $n$-th order differential equation obtained by differentiating the family $n$ times and eliminating the $n$ constants between the resulting $n+1$ equations.

The theorem is the exact converse of the constant-count theorem: as constants are eliminated, the order rises one at a time, and the differential equation obtained is the one whose general solution is the given family.

## 3. Formal Proofs, Derivations, and Methods

### 3.1 Proof of the superposition principle

Let $L$ be the linear operator of Section 2.2, so that $L[c_{1}y_{1}+c_{2}y_{2}]$ can be expanded term by term. Because differentiation is linear, for each $k$

$$
\frac{d^{k}}{dx^{k}}\left(c_{1}y_{1}+c_{2}y_{2}\right)=c_{1}\frac{d^{k}y_{1}}{dx^{k}}+c_{2}\frac{d^{k}y_{2}}{dx^{k}} .
$$

Multiplying by $a_{n-k}(x)$ and summing over $k$ gives

$$
L[c_{1}y_{1}+c_{2}y_{2}]=c_{1}L[y_{1}]+c_{2}L[y_{2}] .
$$

If $y_{1}$ and $y_{2}$ both satisfy $L[y]=0$, the right-hand side is $c_{1}\cdot 0+c_{2}\cdot 0=0$, so the combination satisfies the homogeneous equation. If $y_{h}$ satisfies $L[y]=0$ and $y_{p}$ satisfies $L[y]=F$, then

$$
L[y_{p}+y_{h}]=L[y_{p}]+L[y_{h}]=F+0=F,
$$

which is the second statement.

### 3.2 Method: forming a differential equation from a primitive

The method has four steps, and the order of the resulting equation equals the number of independent constants.

1. Differentiate the given relation with respect to the independent variable as many times as there are constants.
2. Write the original relation and its derivatives as a system of simultaneous equations in the constants.
3. Eliminate the constants between the equations, usually by solving one equation for a constant and substituting into the others.
4. Simplify until only the dependent variable, its derivatives, and functions of the independent variable remain.

A worked illustration of the method is given in Section 4.6.

### 3.3 Method: verifying that a given function is a solution

Verification is mechanical and should be performed in a fixed order.

1. Compute every derivative that appears in the equation, differentiating as many times as the order requires.
2. Substitute the function and the derivatives into the left-hand side.
3. Simplify using algebra and the standard identities, treating the right-hand side as a target.
4. Confirm that the two sides agree identically, that is for all values of the independent variable, and state the interval if one is specified.

If the substitution produces something that vanishes only at isolated points, the function is not a solution.

### 3.4 Method: solving a directly integrable equation

When the equation has the form $\frac{d^{n}y}{dx^{n}}=f(x)$, the solution is obtained by integrating $n$ times, introducing one constant at each integration.

1. Integrate both sides once with respect to $x$, adding a constant $C_{1}$.
2. Repeat until the $n$-th derivative has been reduced to $y$, adding $C_{2},\dots,C_{n}$ at the successive steps.
3. Collect the result as a polynomial in $x$ plus a linear combination of the constants, which is the general solution.
4. Apply any prescribed conditions to determine the constants, and state the particular solution.

The count of constants at the end must equal the order at the start; if it does not, an integration has been missed.

### 3.5 Method: solving a separable first-order equation

An equation is separable when it can be written with all occurrences of $y$ on one side and all occurrences of $x$ on the other.

1. Rewrite the equation in the form $g(y)\frac{dy}{dx}=h(x)$.
2. Integrate both sides with respect to $x$, using the substitution rule to convert the left side into $\int g(y)\,dy$.
3. Add a single constant of integration, since one integration is performed in total.
4. Solve for $y$ where this is possible; if it is not, leave the solution in implicit form and say so.
5. Impose any initial condition to fix the constant, and verify by differentiation.

### 3.6 Proof that the number of constants equals the order for a directly integrable equation

Consider $\frac{d^{n}y}{dx^{n}}=f(x)$ with $f$ continuous. Integrating once gives $\frac{d^{n-1}y}{dx^{n-1}}=\int f(x)\,dx+C_{1}$. Each further integration introduces exactly one new additive constant and never removes one, because the integral of a constant is a constant times $x$ plus a new constant. After $n$ integrations the solution is

$$
y=\underbrace{\int\cdots\int}_{n}f(x)\,dx^{n}+C_{1}\frac{x^{n-1}}{(n-1)!}+C_{2}\frac{x^{n-2}}{(n-2)!}+\cdots+C_{n-1}x+C_{n},
$$

which contains exactly $n$ constants. Differentiating this expression $n$ times returns $f(x)$ and removes every term involving a constant, since each such term is of degree at most $n-1$ in $x$; hence the expression is indeed the general solution.

### 3.7 Method: reducing a second-order equation that is missing a variable

Two reductions are used repeatedly in later lessons.

- **Missing dependent variable.** If the equation contains $x$, $y'$ and $y''$ but not $y$, put $p=y'$, so that $y''=\frac{dp}{dx}$, and the equation becomes first order in $p$.
- **Missing independent variable.** If the equation contains $y$, $y'$ and $y''$ but not $x$, put $p=y'$ and use $\frac{dy}{dx}=p$ together with $y''=\frac{dp}{dx}=\frac{dp}{dy}\cdot\frac{dy}{dx}=p\frac{dp}{dy}$, which turns the equation into first order in $p$ with $y$ as the independent variable.

Both reductions lower the order by one, so the number of arbitrary constants in the final answer is unchanged.

## 4. Representative Worked Examples and Solutions

### 4.1 Problem: classify an equation by order, degree and linearity

Classify the equation

$$
\left(\frac{d^{3}y}{dx^{3}}\right)^{2}+x\frac{d^{2}y}{dx^{2}}+y\frac{dy}{dx}=e^{x} .
$$

### 4.2 Solution: read each property in turn

Step 1. Identify the highest derivative present. The derivatives appearing are $\frac{dy}{dx}$, $\frac{d^{2}y}{dx^{2}}$ and $\frac{d^{3}y}{dx^{3}}$, so the highest is the third, and the order is three.

Step 2. Determine the degree. The highest-order derivative $\frac{d^{3}y}{dx^{3}}$ appears raised to the power two, and the equation is already free of radicals and fractional powers in the derivatives, so the degree is two.

Step 3. Test for linearity. The term $y\frac{dy}{dx}$ multiplies the unknown function by its derivative, which the linear form of Section 1.5 does not permit, so the equation is non-linear.

Step 4. Report the classification. The equation is of order three, degree two, and non-linear.

Step 5. Note the consequence. Because the equation is non-linear, superposition does not apply, and the general solution cannot be assembled from separately found solutions; it must contain three arbitrary constants obtained by successive integration.

### 4.3 Problem: clear a radical and state the degree

Find the order and degree of

$$
\frac{dy}{dx}=x+\sqrt{1+\left(\frac{dy}{dx}\right)^{2}} .
$$

### 4.4 Solution: isolate the radical, then square

Step 1. Isolate the radical so that squaring removes it. Subtracting $x$ from both sides gives

$$
\frac{dy}{dx}-x=\sqrt{1+\left(\frac{dy}{dx}\right)^{2}} .
$$

Step 2. Square both sides, which is legitimate provided the left side is non-negative, a condition that the equation itself imposes.

$$
\left(\frac{dy}{dx}-x\right)^{2}=1+\left(\frac{dy}{dx}\right)^{2}
$$

Step 3. Expand the left side.

$$
\left(\frac{dy}{dx}\right)^{2}-2x\frac{dy}{dx}+x^{2}=1+\left(\frac{dy}{dx}\right)^{2}
$$

Step 4. Cancel the squared derivative, which appears on both sides.

$$
-2x\frac{dy}{dx}+x^{2}=1
$$

Step 5. Read the degree. The surviving derivative is the first, raised to the first power, so the equation is of order one and degree one. This is a case where clearing the radical lowered the apparent degree from two to one, and it shows why the degree must be read from the cleared form.

### 4.5 Problem: verify a proposed solution

Show that $y=e^{-2x}$ is a solution of $\frac{d^{2}y}{dx^{2}}+5\frac{dy}{dx}+6y=0$.

### 4.6 Solution: differentiate, substitute, simplify

Step 1. Compute the first derivative.

$$
\frac{dy}{dx}=-2e^{-2x}
$$

Step 2. Compute the second derivative.

$$
\frac{d^{2}y}{dx^{2}}=4e^{-2x}
$$

Step 3. Substitute all three quantities in the left-hand side.

$$
4e^{-2x}+5\left(-2e^{-2x}\right)+6e^{-2x}
$$

Step 4. Collect the terms in $e^{-2x}$.

$$
\left(4-10+6\right)e^{-2x}=0\cdot e^{-2x}=0
$$

Step 5. Conclude. The left-hand side vanishes identically for every real $x$, so the function satisfies the equation on the whole real line and is a solution.

### 4.7 Problem: solve a second-order equation with two initial conditions

Solve $\frac{d^{2}y}{dx^{2}}=6x$ subject to $y(0)=1$ and $y'(0)=-2$.

### 4.8 Solution: integrate twice, then impose the conditions

Step 1. Integrate once to lower the order.

$$
\frac{dy}{dx}=3x^{2}+C_{1}
$$

Step 2. Integrate again to obtain $y$.

$$
y=x^{3}+C_{1}x+C_{2}
$$

Step 3. Apply the condition on the derivative at $x=0$. Since $y'(0)=C_{1}$ and $y'(0)=-2$, we get $C_{1}=-2$.

Step 4. Apply the condition on the function at $x=0$. Since $y(0)=C_{2}$ and $y(0)=1$, we get $C_{2}=1$.

Step 5. Write the particular solution.

$$
y=x^{3}-2x+1
$$

Step 6. Verify. Differentiating twice gives $y'=3x^{2}-2$ and $y''=6x$, which is the original equation, and $y(0)=1$, $y'(0)=-2$ as required. The order was two and exactly two constants were determined, so the solution is complete.

### 4.9 Problem: solve a separable first-order equation with an initial condition

Solve $\frac{dy}{dx}=2xy$ subject to $y(0)=3$.

### 4.10 Solution: separate, integrate, then fix the constant

Step 1. Separate the variables by dividing both sides by $y$, which is legitimate on any interval where $y\neq 0$.

$$
\frac{1}{y}\frac{dy}{dx}=2x
$$

Step 2. Integrate both sides with respect to $x$.

$$
\int\frac{1}{y}\,dy=\int 2x\,dx
$$

Step 3. Perform the integrations, adding one constant because one integration in total has been carried out.

$$
\ln|y|=x^{2}+C
$$

Step 4. Exponentiate to solve for $y$, writing $A=e^{C}$ for a positive constant and allowing for the sign.

$$
y=Ae^{x^{2}}
$$

Step 5. Apply the initial condition. At $x=0$ we need $y=3$, so $3=Ae^{0}=A$, giving $A=3$.

Step 6. State the particular solution.

$$
y=3e^{x^{2}}
$$

Step 7. Verify. Differentiating gives $y'=6xe^{x^{2}}$, while $2xy=2x\cdot 3e^{x^{2}}=6xe^{x^{2}}$, so the two sides agree, and $y(0)=3$ as required.

### 4.11 Problem: form the differential equation of a family of parabolas

Find the differential equation of the family $y=Ax^{2}+Bx+C$.

### 4.12 Solution: differentiate three times and eliminate

Step 1. Count the constants. There are three independent constants, so the differential equation is of order three.

Step 2. Differentiate once.

$$
\frac{dy}{dx}=2Ax+B
$$

Step 3. Differentiate again.

$$
\frac{d^{2}y}{dx^{2}}=2A
$$

Step 4. Differentiate a third time, which eliminates the last constant.

$$
\frac{d^{3}y}{dx^{3}}=0
$$

Step 5. Conclude. All three constants have disappeared by the third differentiation, so no elimination step is needed, and the required equation is $\frac{d^{3}y}{dx^{3}}=0$, of order three as predicted.

Step 6. Interpret. Every cubic-free result is consistent with the general solution of $\frac{d^{3}y}{dx^{3}}=0$, whose general solution is a quadratic polynomial with three arbitrary constants, exactly the original family.

### 4.13 Problem: form a differential equation where elimination is required

Show that the differential equation associated with the primitive $y=Ae^{2x}+Be^{x}$ is $\frac{d^{2}y}{dx^{2}}-3\frac{dy}{dx}+2y=0$.

### 4.14 Solution: differentiate and substitute

Step 1. Differentiate once.

$$
\frac{dy}{dx}=2Ae^{2x}+Be^{x}
$$

Step 2. Differentiate again.

$$
\frac{d^{2}y}{dx^{2}}=4Ae^{2x}+Be^{x}
$$

Step 3. Look for a combination that cancels both constants. Form the expression $\frac{d^{2}y}{dx^{2}}-3\frac{dy}{dx}+2y$ and substitute the three expressions.

$$
4Ae^{2x}+Be^{x}-3\left(2Ae^{2x}+Be^{x}\right)+2\left(Ae^{2x}+Be^{x}\right)
$$

Step 4. Collect the coefficients of $Ae^{2x}$ and $Be^{x}$ separately. For the first,

$$
4A-6A+2A=0 ,
$$

and for the second,

$$
B-3B+2B=0 .
$$

Step 5. Conclude. Both coefficients vanish identically, so

$$
\frac{d^{2}y}{dx^{2}}-3\frac{dy}{dx}+2y=0
$$

is satisfied by every member of the family, and it is of order two, matching the number of constants.

### 4.15 Problem: a singular solution

Consider the equation $\left(\frac{dy}{dx}\right)^{2}-4y=0$. Verify that $y=(x+C)^{2}$ is a solution, and examine whether $y=0$ belongs to the family.

### 4.16 Solution: substitute, then compare families

Step 1. Differentiate the proposed family.

$$
\frac{dy}{dx}=2(x+C)
$$

Step 2. Substitute into the equation.

$$
\left[2(x+C)\right]^{2}-4(x+C)^{2}=4(x+C)^{2}-4(x+C)^{2}=0
$$

The equation is satisfied identically, so the family is a solution family with one constant, as the first order requires.

Step 3. Test $y=0$. Its derivative is zero, so substitution gives $0-0=0$, and $y=0$ is a solution.

Step 4. Ask whether any $C$ produces $y=0$. The equation $(x+C)^{2}=0$ holds only at the single point $x=-C$, not on any interval, so no member of the family is identically zero.

Step 5. Conclude. The function $y=0$ is a singular solution: it satisfies the equation but is not obtainable from the general solution by choosing a constant.

### 4.17 Problem: a first-order equation whose solution is implicit

Solve $\frac{dy}{dx}=\frac{x^{2}}{1+y^{2}}$.

### 4.18 Solution: separate and integrate, leaving the answer implicit

Step 1. Separate the variables by multiplying both sides by $1+y^{2}$.

$$
\left(1+y^{2}\right)\frac{dy}{dx}=x^{2}
$$

Step 2. Integrate both sides with respect to $x$.

$$
\int\left(1+y^{2}\right)dy=\int x^{2}\,dx
$$

Step 3. Perform the integrations, adding one constant.

$$
y+\frac{y^{3}}{3}=\frac{x^{3}}{3}+C
$$

Step 4. Attempt to solve for $y$. The left-hand side is a cubic in $y$ of the form $\frac{1}{3}y^{3}+y$, whose derivative $y^{2}+1$ is never zero, so the cubic is strictly increasing and defines $y$ uniquely as a function of $x$. An explicit formula nevertheless requires the cubic formula, which is not illuminating here.

Step 5. State the answer in the clearest available form and note that it is a complete solution.

$$
3y+y^{3}=x^{3}+C'
$$

with $C'=3C$. Differentiating implicitly confirms the equation, and the single arbitrary constant matches the order one.

### 4.19 Problem: verify a two-parameter family by elimination

Find the differential equation whose general solution is $y=c_{1}e^{x}+c_{2}e^{-x}$.

### 4.20 Solution: differentiate twice and eliminate both constants

Step 1. Count the constants. There are two, so the equation is of order two.

Step 2. Differentiate once.

$$
\frac{dy}{dx}=c_{1}e^{x}-c_{2}e^{-x}
$$

Step 3. Differentiate again, which returns the original combination.

$$
\frac{d^{2}y}{dx^{2}}=c_{1}e^{x}+c_{2}e^{-x}=y
$$

Step 4. Rearrange into the standard form.

$$
\frac{d^{2}y}{dx^{2}}-y=0
$$

Step 5. Check the count. The equation is of order two and its solutions

$$
y=c_{1}e^{x}+c_{2}e^{-x}
$$

carry exactly two constants, so the general solution has been recovered.

Step 6. Interpret. The pair $e^{x}$ and $e^{-x}$ are independent, and the equation is linear and homogeneous, which is why the general solution is the full linear combination of them rather than a single exponential.

## 5. Mathematical Extensions, Limits, and Common Errors

### 5.1 What the classification does and does not tell you

Order, degree and linearity are labels that route an equation to a method. They do not, by themselves, guarantee that an elementary solution exists. The equation $\frac{dy}{dx}=e^{-x^{2}}$ is first order, first degree and linear, and its solution is perfectly well defined, but the integral cannot be expressed in elementary functions, so the answer must be left as a definite or indefinite integral. Recognising this early prevents a great deal of wasted effort: the classification tells you which method to attempt, and the attempt tells you whether a closed form is available.

Degree is the weakest of the three labels. It carries almost no structural information, is not invariant under rearrangement, and exists only for equations polynomial in the derivatives. Order and linearity are the labels that matter, because the order fixes the number of constants and linearity makes superposition available.

### 5.2 Where the counting rule fails

The rule that an $n$-th order equation has $n$ arbitrary constants in its general solution is reliable for equations solved for the highest derivative with continuous coefficients, which is the setting of the course. It can fail in three ways worth knowing. First, an equation may admit a singular solution outside the family, as in Section 4.15. Second, an equation may have no solution at all on a required interval even though solutions exist locally, as happens when a solution curve reaches a point where the leading coefficient vanishes. Third, for a boundary value problem rather than an initial value problem, the count of constants no longer guarantees a solution, because the resulting algebraic system in the constants may be inconsistent or may be satisfied by infinitely many values.

### 5.3 Extensions that appear later in the course

Three ideas introduced here are used continuously in the remaining lessons. The reduction of order in Section 3.7 becomes the standard technique for second-order equations missing a variable. The superposition principle becomes the reason the complementary function and the particular integral are found separately and added. The elimination-of-constants method is inverted in Lesson 5, where a linear equation with constant coefficients is solved by writing down its characteristic equation and reading off the complementary function from the roots.

A further extension concerns the relationship between an equation and its differential consequences. Differentiating an equation can raise the order and introduce spurious solutions, which is why the elimination method of Section 3.2 is applied with care: the differential equation obtained is satisfied by the given family, but it may be satisfied by other curves as well. The direction of implication matters. A family of curves determines a unique differential equation, but a differential equation determines a family only through its general solution, and that general solution may be smaller than the set of all solutions.

### 5.4 Common errors and how to avoid them

- **Reporting the degree before clearing radicals.** The degree of $\frac{dy}{dx}=\sqrt{1+\left(\frac{dy}{dx}\right)^{2}}$-type equations must be read after squaring, and the cleared form often has a different degree from the apparent one.
- **Confusing order with degree.** Order counts differentiations; degree counts the power of the highest derivative. An equation can be of order three and degree one, or order one and degree two, and the two numbers are found by separate inspections.
- **Counting constants carelessly.** A second-order equation must produce two arbitrary constants. Writing $y=x^{3}+C$ for $\frac{d^{2}y}{dx^{2}}=6x$ is wrong because one integration has been omitted.
- **Treating $\frac{dy}{dx}$ as a fraction without justification.** Separating variables is valid because both sides can be integrated, not because $dy$ and $dx$ are numbers that may be moved about freely.
- **Losing the absolute value or the sign constant when exponentiating.** The step from $\ln|y|=x^{2}+C$ to $y=Ae^{x^{2}}$ must allow $A$ to be negative, since $y$ may be negative on the interval of validity.
- **Forgetting to verify.** Substituting the answer back is the only reliable check, and it detects sign errors, missing constants, and mis-integrated terms immediately.
- **Assuming superposition for non-linear equations.** The sum of two solutions of a non-linear equation is not a solution, and using superposition where linearity has not been established invalidates the argument.
- **Ignoring the interval of validity.** A solution is a function on an interval. Where a division by $y$ or by a coefficient has been performed, the interval must exclude the points where that quantity vanishes.

### 5.5 A procedure for any question in this topic

1. Read the equation and state its order by locating the highest derivative.
2. Clear radicals and fractions involving derivatives, then state the degree, or state that no degree exists.
3. Test linearity by checking whether $y$ and its derivatives appear only to the first power and never multiplied together.
4. If a family of curves is given, count its constants and differentiate that many times, eliminating as required; the order of the answer must equal the count.
5. If a solution is given, differentiate it the required number of times, substitute, and simplify to zero.
6. If an equation is to be solved and it is directly integrable or separable, integrate introducing one constant per integration, and impose any conditions.
7. Verify the final answer by substitution, and state the interval on which it holds.

### 5.6 Consolidated summary of the topic

The topic establishes the vocabulary on which the remaining twelve lessons depend, and the vocabulary is best remembered as four questions asked in a fixed order.

The first question is what the equation contains. If it contains ordinary derivatives of a function of one variable it is an ordinary differential equation; if it contains partial derivatives of a function of several variables it is a partial differential equation, and the remainder of this course is concerned only with the ordinary case.

The second question is how many differentiations the equation involves. The highest derivative present fixes the order, and the order fixes the number of arbitrary constants carried by the general solution. This count is the most reliable check available to a student: any claimed general solution carrying fewer constants than the order is incomplete.

The third question is what power the highest derivative carries once radicals and fractional powers have been cleared. That power is the degree, a weaker property than the order because it depends on the algebraic form in which the equation is written and can change under rearrangement.

The fourth question is whether the unknown function and its derivatives appear only to the first power and never multiplied together. If they do, the equation is linear, superposition applies, and the complementary-function-plus-particular-integral strategy of the later lessons becomes available. If they do not, the equation is non-linear and each such equation must be attacked on its own terms.

Around these four questions sit three operations that the examination tests directly. Verification substitutes a proposed function and its derivatives and simplifies to an identity. Formation differentiates a given family as many times as it has constants and eliminates them. Solution of the elementary types integrates as many times as the order requires, introducing one constant per integration, and then fixes those constants from the prescribed conditions. A differential equation and its solution are checked against each other by differentiation and substitution, and that check is the only defence against the errors catalogued in Section 5.4.

