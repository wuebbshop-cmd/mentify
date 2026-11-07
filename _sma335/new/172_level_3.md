## 1. Foundational Concepts, Definitions, and Axioms

### 1.1 What is actually being examined

Every question in this topic is one of five shapes, and the shape determines the marks.

The first shape is classification: a given equation must be labelled separable, homogeneous, reducible of intersecting type, or reducible of parallel type, usually with the test that produced the label. Two to three marks.

The second shape is a direct solve of a separable equation, most often with an initial condition attached. Six to ten marks.

The third shape is a homogeneous equation solved by the substitution $y = vx$. Eight to twelve marks, because the substitution, the separation, the integration and the back-substitution are each marked.

The fourth shape is a reducible equation, where the marks are concentrated in the decision between the two cases and in the correct shift or substitution. Ten to fourteen marks.

The fifth shape is a show-that question: prove that the substitution $y = vx$ converts a homogeneous equation into a separable one, or prove that the translation removes the constant terms. Three to five marks, and these are the cheapest marks on the paper because the argument is short and completely standard.

Nothing in this topic requires ingenuity. Marks are lost through three things only: not testing the type before choosing a method, omitting the term $x\frac{dv}{dx}$, and failing to check the answer. The whole of this note is organised to make those three failures impossible.

### 1.2 The definitions that must be reproduced exactly

> **Definition (Separable).** The equation $\frac{dy}{dx} = f(x,y)$ is separable if $f(x,y) = p(x)q(y)$ on the region of interest, equivalently if it can be written as
>
> $$
> g(y)\,\frac{dy}{dx} = h(x).
> $$

Two marks are normally given for the factored form, and one further mark for the statement of the solution as

$$
\int g(y)\,dy = \int h(x)\,dx + C .
$$

> **Definition (Homogeneous function).** A function $f$ of two variables is homogeneous of degree $n$ if
>
> $$
> f(kx,ky) = k^{n}f(x,y)
> $$
>
> for every admissible point and every admissible scale factor $k$.

> **Definition (Homogeneous equation of first order).** The equation $\frac{dy}{dx} = f(x,y)$ is homogeneous if $f$ is homogeneous of degree zero, that is if $f(kx,ky) = f(x,y)$.

The phrase "of degree zero" is worth one mark on its own in a definition question. Writing "homogeneous of degree $n$" and then setting $n$ equal to zero later is accepted, but omitting the qualification entirely is not, because it leaves the definition satisfied by every homogeneous function of every degree, which is false.

> **Definition (Homogeneous equation in differential form).** The equation $M\,dx + N\,dy = 0$ is homogeneous if $M$ and $N$ are homogeneous functions of the same degree.

> **Definition (The two reducible cases).** For $\frac{dy}{dx} = \frac{ax+by+c}{px+qy+r}$ put $D = aq-bp$. If $D \neq 0$ the two lines intersect and the equation is of intersecting type; if $D = 0$ the lines are parallel or coincident and the equation is of parallel type.

### 1.3 Notation that examiners expect to see declared

The symbols carry marks in the sense that an undeclared symbol makes a script unreadable and loses method marks even when the algebra is right.

| Symbol | Meaning in this topic | Where it first appears |
| --- | --- | --- |
| $v$ | the ratio $y/x$, a function of $x$ | substitution $y = vx$ |
| $z$ | the repeated combination $ax+by$ | parallel case |
| $X$, $Y$ | translated coordinates $x-h$ and $y-k$ | intersecting case |
| $h$, $k$ | coordinates of the intersection point | intersecting case |
| $D$ | the determinant $aq-bp$ | case decision |
| $M$, $N$ | coefficients of $dx$ and $dy$ | differential form |

The single most important entry in that table is the first. The letter $v$ is a function, so its derivative is not zero, and every occurrence of $\frac{dy}{dx}$ after the substitution must be replaced by the two-term expression derived in Section 3.1.

### 1.4 The formula sheet to carry into the hall

Nine lines cover every question in this topic. They should be reproduced from memory in the first minute of the examination, in the margin, before any question is attempted.

$$
\frac{dy}{dx} = v + x\frac{dv}{dx} \qquad \text{for } y = vx
$$

$$
x\frac{dv}{dx} = F(v)-v \qquad \text{for } \frac{dy}{dx} = F\!\left(\frac{y}{x}\right)
$$

$$
\frac{dv}{F(v)-v} = \frac{dx}{x}
$$

$$
\frac{dz}{dx} = a + b\frac{dy}{dx} \qquad \text{for } z = ax+by
$$

$$
D = aq - bp
$$

$$
h = \frac{br-cq}{aq-bp}, \qquad k = \frac{cp-ar}{aq-bp}
$$

$$
\int\frac{dv}{v} = \ln|v|, \qquad \int\frac{2v\,dv}{1+v^{2}} = \ln\left(1+v^{2}\right)
$$

$$
\int\frac{dv}{1+v^{2}} = \arctan v, \qquad \int\frac{dv}{1-v^{2}} = \frac{1}{2}\ln\left|\frac{1+v}{1-v}\right|
$$

$$
\ln A + \ln B = \ln\left(AB\right), \qquad C = \ln A \text{ is legitimate for } A>0
$$

The last line is not padding. Writing the constant as a logarithm is what turns answers such as $\ln|v| = -\ln x + c$ into the polynomial relations that examiners expect, and scripts that leave the answer in a mixture of logarithms lose presentation marks.

## 2. Theorems, Lemmas, and Analytical Properties

### 2.1 Core results with their mark values

> **Result 1 (Degree test).** If $f(kx,ky) = k^{n}f(x,y)$ for a single exponent $n$, the degree is $n$; if no single exponent works, the function has no degree. *Typical value: 2 marks.*

> **Result 2 (Two-degree test).** The equation $M\,dx + N\,dy = 0$ is homogeneous if and only if $M$ and $N$ have the same degree. *Typical value: 2 marks.*

> **Result 3 (Ratio representation).** If $f$ has degree zero then $f(x,y) = F(y/x)$ with $F(v) = f(1,v)$. *Typical value: 2 marks.*

> **Result 4 (Derivative of the substitution).** If $y = vx$ then $\frac{dy}{dx} = v + x\frac{dv}{dx}$. *Typical value: 1 mark, and it is the most frequently dropped mark in the topic.*

> **Result 5 (Reduction theorem).** A homogeneous equation reduces to $x\frac{dv}{dx} = F(v)-v$, hence to $\frac{dv}{F(v)-v} = \frac{dx}{x}$. *Typical value: 3 marks when asked as a show-that.*

> **Result 6 (Parallel criterion).** The coefficient pairs $(a,b)$ and $(p,q)$ are proportional if and only if $aq-bp = 0$; in that case the equation depends on $ax+by$ alone. *Typical value: 2 marks.*

> **Result 7 (Translation).** If $aq-bp \neq 0$ then $x = X+h$, $y = Y+k$ with $(h,k)$ on both lines reduces the equation to $\frac{dY}{dX} = \frac{aX+bY}{pX+qY}$. *Typical value: 3 marks.*

> **Result 8 (Constant count).** A first-order equation has exactly one arbitrary constant in its general solution. *Typical value: 1 mark, awarded for the check that the answer is a one-parameter family.*

The mark values are the ones that recur. They matter because they tell you where to spend time: a script that produces a beautiful integral but never writes $v + x\frac{dv}{dx}$ has lost the mark that a single line would have secured.

### 2.2 Result-to-question map

| Result | Command word used | Marks | Frequency |
| --- | --- | --- | --- |
| Degree test | show that, determine whether | 2 | very high |
| Two-degree test | test for homogeneity | 2 | high |
| Ratio representation | express as a function of $v$ | 2 | medium |
| Derivative of $y = vx$ | hence, or implied | 1 | very high |
| Reduction theorem | show that the substitution reduces | 3 | high |
| Parallel criterion | state the case | 2 | high |
| Translation | find $h$ and $k$ | 3 | high |
| Constant count | verify | 1 | medium |

The command word "hence" is a warning. When a question says "hence solve", the intended route is the one just established, and a solution by another method may lose the method marks even if the answer is correct.

### 2.3 The seven identities that do the work in the integrations

The algebra after separation is repetitive, and the following list covers essentially all of it.

$$
\int \frac{dv}{v} = \ln|v| + c
$$

$$
\int v^{n}\,dv = \frac{v^{n+1}}{n+1} + c \qquad \text{for } n \neq -1
$$

$$
\int \frac{2v}{1+v^{2}}\,dv = \ln\left(1+v^{2}\right) + c
$$

$$
\int \frac{dv}{1+v^{2}} = \arctan v + c
$$

$$
\int \frac{dv}{v^{2}-1} = \frac{1}{2}\ln\left|\frac{v-1}{v+1}\right| + c
$$

$$
\int \frac{f'(v)}{f(v)}\,dv = \ln\left|f(v)\right| + c
$$

$$
\int \frac{dv}{\left(v+r\right)^{2}+s^{2}} = \frac{1}{s}\arctan\left(\frac{v+r}{s}\right) + c
$$

The sixth line is the workhorse. Before attempting any partial fractions, check whether the numerator is a multiple of the derivative of the denominator; in a large proportion of examination questions it is, and the integration collapses to one logarithm.

### 2.4 The structural facts that prevent wrong answers

Three facts are worth memorising as prohibitions.

First, the reduced equation $x\frac{dv}{dx} = F(v)-v$ can never reduce to a constant multiple of $x$ unless the original equation was already separable; if the algebra appears to give a right-hand side independent of $v$ and equal to zero, the case $F(v) = v$ has been reached and the answer is a family of straight lines.

Second, in the intersecting case the reduced equation always has the constant terms gone. If a constant survives the substitution, either $h$ and $k$ are wrong or the substitution has been applied to one line only. This is a one-second check that catches the commonest error in the topic.

Third, in the parallel case the substitution $z = ax+by$ requires that $b \neq 0$. If $b = 0$ then $D = aq$ and $D = 0$ forces $q = 0$, so the equation involves $x$ only and is directly integrable. A question that appears to be parallel with $b = 0$ is a disguised direct integration.

### 2.5 Why the marks are distributed as they are

A twelve-mark homogeneous question is usually marked as follows: one mark for the degree test, one for the substitution including the derivative, two for simplifying to the separated form, one for correctly separating, three for the integration, two for the back-substitution and clearing of fractions, one for the constant, and one for the check.

That distribution explains a great deal of unexpected disappointment. A student who obtains the correct final relation but omits the degree test has lost one mark; a student who obtains a nearly correct relation but omits the check has lost one mark; a student who writes $y' = v$ after the substitution has lost at least four marks even if the final line happens to be right, because the simplification, the separation and the integration are all built on the wrong premise.

## 3. Formal Proofs, Derivations, and Methods

### 3.1 Show that $y = vx$ reduces a homogeneous equation to a separable one (4 marks)

Step 1 (1 mark). State the substitution and its derivative. Let $y = vx$ with $v$ a function of $x$. By the product rule,

$$
\frac{dy}{dx} = v + x\frac{dv}{dx} .
$$

Step 2 (1 mark). Use degree zero to write the right-hand side as a function of the ratio. Since $f$ is homogeneous of degree zero, taking the scale factor $1/x$ gives

$$
f(x,y) = f\!\left(1,\frac{y}{x}\right) = F(v) .
$$

Step 3 (2 marks). Substitute both facts into the equation and rearrange.

$$
v + x\frac{dv}{dx} = F(v), \qquad x\frac{dv}{dx} = F(v)-v, \qquad \frac{dv}{F(v)-v} = \frac{dx}{x} .
$$

The final form has $v$ alone on the left and $x$ alone on the right, which is the definition of separability, so the reduction is complete.

### 3.2 Show that the translation removes the constant terms (3 marks)

Step 1 (1 mark). Let $(h,k)$ be the point satisfying both $ah+bk+c = 0$ and $ph+qk+r = 0$, which exists and is unique because $aq-bp \neq 0$.

Step 2 (1 mark). Put $x = X+h$ and $y = Y+k$. Since $h$ and $k$ are constants, $dx = dX$ and $dy = dY$.

Step 3 (1 mark). Expand the numerator and use the defining property of the point.

$$
a\left(X+h\right)+b\left(Y+k\right)+c = aX+bY+\left(ah+bk+c\right) = aX+bY .
$$

The same computation applied to the denominator gives $pX+qY$, so both constant terms have disappeared and the resulting quotient is homogeneous of degree zero.

### 3.3 Derive the formulas for $h$ and $k$ (2 marks)

Step 1. Write the two conditions as a linear system in $h$ and $k$.

$$
ah + bk = -c, \qquad ph + qk = -r
$$

Step 2. The determinant of the coefficient matrix is $aq-bp = D \neq 0$, so Cramer's rule applies and gives

$$
h = \frac{\left(-c\right)q - b\left(-r\right)}{D} = \frac{br-cq}{aq-bp},
$$

and similarly

$$
k = \frac{a\left(-r\right) - \left(-c\right)p}{D} = \frac{cp-ar}{aq-bp}.
$$

### 3.4 Show that the two-degree test is equivalent to degree zero (2 marks)

Step 1. On the region where $N \neq 0$ the equation $M\,dx+N\,dy = 0$ gives

$$
\frac{dy}{dx} = -\frac{M}{N} .
$$

Step 2. If $M$ and $N$ are both homogeneous of degree $n$, then substituting the scaled point gives $k^{n}M$ and $k^{n}N$, so the quotient is multiplied by $k^{n}/k^{n} = 1$ and is therefore homogeneous of degree zero. Conversely, if the quotient has degree zero then the powers of $k$ in numerator and denominator must match, so the degrees of $M$ and $N$ are equal.

### 3.5 The full algorithm with time budget

| Phase | Action | Time guide |
| --- | --- | --- |
| Identify | scale the right-hand side, or compare the degrees of $M$ and $N$ | 1 minute |
| Case | compute $D = aq-bp$ if the right-hand side is linear over linear | 1 minute |
| Substitute | write the substitution and its derivative together | 1 minute |
| Simplify | obtain the separated form, recording excluded values | 3 minutes |
| Integrate | integrate both sides, combine logarithms | 4 minutes |
| Restore | undo every substitution, clear fractions | 3 minutes |
| Check | differentiate the answer and compare | 2 minutes |

Fifteen minutes is the budget for a twelve-mark question. The check is never the item to drop, because it is the only part of the answer that can be trusted without re-reading the whole script, and because it earns a mark on its own.

### 3.6 Decision flow for an unfamiliar equation

Step 1. Is the right-hand side a product of a piece in $x$ and a piece in $y$ after factoring? If yes, separate and integrate.

Step 2. Is the right-hand side a quotient of two linear expressions? If yes, compute $D$ and follow the appropriate cure.

Step 3. Does the right-hand side survive scaling unchanged? If yes, divide through by the appropriate power of $x$ to expose the ratio, substitute $y = vx$, and proceed.

Step 4. Does the right-hand side become a function of the ratio after dividing by a power of $x$ that is not the same in numerator and denominator? If yes, the equation is not homogeneous, and the answer should say so rather than forcing the substitution.

Step 5. If none of the above applies, state the type that does apply. A linear equation needs an integrating factor, which is a different lesson, and saying so is better than a stalled attempt.

### 3.7 Recording excluded values without losing marks

Every division excludes something, and the examiner expects the excluded values to be written down. The minimum acceptable statement is a single line listing them.

For a division by $y$ the excluded value is $y = 0$. For a division by $F(v)-v$ the excluded values are the roots of $F(v) = v$, each of which corresponds to a straight ray $y = v_{0}x$. For a division by a quadratic in $v$ the excluded values are its real roots.

After the integration, each excluded value is tested in the original equation. A value that satisfies it becomes an additional, separate solution; a value that does not is discarded. Writing both outcomes is worth a mark and prevents the silent loss of a solution.

## 4. Representative Worked Examples and Solutions

### 4.1 Problem: a separable equation with an initial condition and an integration by parts (20 marks)

Solve $\frac{dy}{dx} = \frac{x e^{x}}{y}$ subject to $y = 1$ when $x = 0$, and state the interval on which the solution is valid.

### 4.2 Solution: Model Solution 1

Step 1 (2 marks). Identify the type by factoring. The right-hand side is the product of $x e^{x}$, which depends on $x$ only, and $1/y$, which depends on $y$ only. The equation is therefore separable.

Step 2 (2 marks). Separate the variables by multiplying both sides by $y$.

$$
y\frac{dy}{dx} = x e^{x}
$$

Step 3 (1 mark). Integrate both sides with respect to $x$, using the chain rule on the left.

$$
\int y\,dy = \int x e^{x}\,dx
$$

Step 4 (4 marks). Evaluate the left integral directly and the right integral by parts with $u = x$ and $dv = e^{x}dx$, so that $du = dx$ and $v = e^{x}$.

$$
\frac{y^{2}}{2} = x e^{x} - \int e^{x}\,dx = x e^{x} - e^{x} + c
$$

Step 5 (2 marks). Clear the fraction and combine the two exponential terms, relabelling the constant.

$$
y^{2} = 2e^{x}\left(x-1\right) + C
$$

Step 6 (2 marks). Impose the initial condition $y = 1$ at $x = 0$. The exponential is one and the bracket is minus one, so the right-hand side is minus two plus the constant.

$$
1 = -2 + C, \qquad C = 3
$$

Step 7 (3 marks). Write the particular solution and select the branch. The solution passes through $y = 1$, which is positive. The quantity $2e^{x}\left(x-1\right)+3$ has derivative $2xe^{x}$, so it decreases up to $x = 0$ and increases afterwards, and its minimum is therefore $2e^{0}\left(0-1\right)+3 = 1$. Being always at least one, it never vanishes, so the positive branch is valid for all real $x$.

$$
y = \sqrt{2e^{x}\left(x-1\right)+3}
$$

Step 8 (2 marks). State the interval. Since the quantity under the root is positive for every real $x$, the solution is valid on the whole real line.

Step 9 (2 marks). Check by implicit differentiation of the squared relation.

$$
2y\frac{dy}{dx} = 2e^{x}\left(x-1\right) + 2e^{x} = 2x e^{x}, \qquad \frac{dy}{dx} = \frac{x e^{x}}{y}
$$

The recovered derivative is the original right-hand side, and at $x = 0$ the value is $\sqrt{1} = 1$, so both the equation and the condition are satisfied. The total is twenty marks.

### 4.3 Problem: a homogeneous equation with a rational right-hand side (20 marks)

Solve $\left(x^{2}+y^{2}\right)dx - 2xy\,dy = 0$.

### 4.4 Solution: Model Solution 2

Step 1 (2 marks). Test for homogeneity using the two-degree test. The coefficient of $dx$ is $x^{2}+y^{2}$, whose terms each have total degree two, so its degree is two. The coefficient of $dy$ is $-2xy$, of total degree two. The degrees are equal, so the equation is homogeneous.

Step 2 (1 mark). Solve for the derivative.

$$
\frac{dy}{dx} = \frac{x^{2}+y^{2}}{2xy}
$$

Step 3 (2 marks). Divide numerator and denominator by $x^{2}$ to expose the ratio, and substitute $y = vx$ with its derivative.

$$
\frac{dy}{dx} = \frac{1+v^{2}}{2v}, \qquad v + x\frac{dv}{dx} = \frac{1+v^{2}}{2v}
$$

Step 4 (2 marks). Subtract $v$ and simplify over the single denominator.

$$
x\frac{dv}{dx} = \frac{1+v^{2}-2v^{2}}{2v} = \frac{1-v^{2}}{2v}
$$

Step 5 (1 mark). Separate the variables, recording that $v = \pm 1$ and $v = 0$ are excluded.

$$
\frac{2v}{1-v^{2}}\,dv = \frac{dx}{x}
$$

Step 6 (3 marks). Integrate, noting that the numerator is minus the derivative of the denominator.

$$
-\ln\left|1-v^{2}\right| = \ln x + c
$$

Step 7 (2 marks). Combine the logarithms and exponentiate.

$$
1 - v^{2} = \frac{C}{x}
$$

Step 8 (3 marks). Restore $v = y/x$ and multiply through by $x$.

$$
1 - \frac{y^{2}}{x^{2}} = \frac{C}{x}, \qquad x^{2} - y^{2} = Cx
$$

Step 9 (2 marks). Check by implicit differentiation, using $C = \left(x^{2}-y^{2}\right)/x$ from the answer itself.

$$
2x - 2y\frac{dy}{dx} = C = \frac{x^{2}-y^{2}}{x}, \qquad 2y\frac{dy}{dx} = \frac{2x^{2}-x^{2}+y^{2}}{x} = \frac{x^{2}+y^{2}}{x}
$$

Dividing by $2y$ gives $\frac{dy}{dx} = \frac{x^{2}+y^{2}}{2xy}$, which is the equation, so the answer is confirmed. It contains one arbitrary constant, as a first-order general solution must.

Step 10 (2 marks). Note the lost solutions. The excluded values $v = \pm 1$ correspond to the lines $y = \pm x$, and substituting $y = x$ gives $2x^{2}dx - 2x^{2}dx = 0$, while substituting $y = -x$ gives $2x^{2}dx - 2x^{2}dx = 0$, so both lines are solutions. Each is contained in the general relation by taking $C = 0$, so neither is lost. The remaining excluded value $v = 0$ means $y = 0$, which would require $x^{2}dx = 0$ for every $x$ and is therefore not a solution. The total is twenty marks.

### 4.5 Problem: a reducible equation of intersecting type (20 marks)

Solve $\left(2x+y-3\right)dx + \left(x+2y-3\right)dy = 0$.

### 4.6 Solution: Model Solution 3

Step 1 (2 marks). Compute the determinant that decides the case, with $a = 2$, $b = 1$, $p = 1$, $q = 2$.

$$
D = aq - bp = 2\cdot 2 - 1\cdot 1 = 3 \neq 0
$$

The coefficient pairs are not proportional, so the lines intersect and the translation method applies.

Step 2 (3 marks). Find the point of intersection by solving the two equations

$$
2h + k - 3 = 0, \qquad h + 2k - 3 = 0 .
$$

Adding gives $3h+3k = 6$, so $h+k = 2$; subtracting gives $h - k = 0$, so $h = k = 1$.

Step 3 (1 mark). Verify the point in both equations: $2+1-3 = 0$ and $1+2-3 = 0$, so the point $(1,1)$ lies on both lines.

Step 4 (2 marks). Substitute $x = X+1$ and $y = Y+1$, noting that $dx = dX$ and $dy = dY$, and confirm that the constants cancel.

$$
\frac{dY}{dX} = -\frac{2X+Y}{X+2Y}
$$

Step 5 (2 marks). Divide by $X$ and substitute $Y = vX$ together with its derivative.

$$
v + X\frac{dv}{dX} = -\frac{2+v}{1+2v}
$$

Step 6 (2 marks). Subtract $v$ and simplify over the single denominator.

$$
X\frac{dv}{dX} = \frac{-2-v-v-2v^{2}}{1+2v} = -2\cdot\frac{v^{2}+v+1}{1+2v}
$$

Step 7 (1 mark). Separate the variables, moving the factor of two to the right.

$$
\frac{1+2v}{v^{2}+v+1}\,dv = -2\frac{dX}{X}
$$

Step 8 (3 marks). Integrate, using that the numerator is exactly the derivative of the denominator.

$$
\ln\left(v^{2}+v+1\right) = -2\ln X + c
$$

Step 9 (2 marks). Exponentiate to obtain a relation in $X$ and $v$, then multiply by $X^{2}$.

$$
v^{2}+v+1 = \frac{C}{X^{2}}, \qquad X^{2}v^{2} + X^{2}v + X^{2} = C
$$

Step 10 (2 marks). Restore $vX = Y$, so that $X^{2}v^{2} = Y^{2}$ and $X^{2}v = XY$, and then restore the original letters.

$$
Y^{2} + XY + X^{2} = C, \qquad \left(y-1\right)^{2} + \left(x-1\right)\left(y-1\right) + \left(x-1\right)^{2} = C
$$

Step 11 (2 marks). Expand to the polynomial form examiners prefer.

$$
x^{2} + xy + y^{2} - 3x - 3y + 3 = C
$$

Step 12 (2 marks). Check by implicit differentiation. With $F = x^{2}+xy+y^{2}-3x-3y$ the partial derivatives are $F_{x} = 2x+y-3$ and $F_{y} = x+2y-3$, so

$$
\frac{dy}{dx} = -\frac{F_{x}}{F_{y}} = -\frac{2x+y-3}{x+2y-3},
$$

which is exactly the derivative implied by the original differential equation. The answer is confirmed and carries one constant. The total is twenty marks.

### 4.7 Problem: a reducible equation of parallel type (15 marks)

Solve $\frac{dy}{dx} = \frac{x-y+1}{2x-2y+3}$.

### 4.8 Solution: Model Solution 4

Step 1 (2 marks). Decide the case. The ratio of the $x$-coefficients is $1/2$ and the ratio of the $y$-coefficients is $-1/-2 = 1/2$, so the ratios agree and $D = 1\cdot\left(-2\right) - \left(-1\right)\cdot 2 = 0$. The lines are parallel and the substitution $z = ax+by$ applies.

Step 2 (1 mark). Identify the repeated combination: both the numerator and the denominator are built from $x-y$.

Step 3 (2 marks). Substitute $z = x-y$, so that $\frac{dz}{dx} = 1 - \frac{dy}{dx}$, hence $\frac{dy}{dx} = 1 - \frac{dz}{dx}$.

Step 4 (2 marks). Substitute into the equation and solve for $\frac{dz}{dx}$.

$$
1 - \frac{dz}{dx} = \frac{z+1}{2z+3}, \qquad \frac{dz}{dx} = \frac{2z+3-z-1}{2z+3} = \frac{z+2}{2z+3}
$$

Step 5 (1 mark). Separate the variables.

$$
\frac{2z+3}{z+2}\,dz = dx
$$

Step 6 (2 marks). Divide out the fraction, since $2z+3 = 2\left(z+2\right)-1$.

$$
\int\left(2 - \frac{1}{z+2}\right)dz = \int dx
$$

Step 7 (2 marks). Integrate both sides.

$$
2z - \ln\left|z+2\right| = x + c
$$

Step 8 (2 marks). Restore $z = x-y$ and tidy the linear terms.

$$
2\left(x-y\right) - \ln\left|x-y+2\right| = x + c, \qquad x - 2y - \ln\left|x-y+2\right| = C
$$

Step 9 (2 marks). Check by implicit differentiation, using that the derivative of $\ln\left|x-y+2\right|$ is $\left(1-y'\right)/\left(x-y+2\right)$.

$$
1 - 2y' - \frac{1-y'}{x-y+2} = 0, \qquad \left(1-2y'\right)\left(x-y+2\right) = 1 - y'
$$

Step 10 (2 marks). Collect the terms in $y'$ and compare.

$$
x-y+1 = y'\left(2x-2y+3\right), \qquad \frac{dy}{dx} = \frac{x-y+1}{2x-2y+3}
$$

The recovered derivative is the original equation, so the answer is correct. The logarithm requires $x-y+2 \neq 0$, so the solution is confined to one side of that line. The total is fifteen marks.

### 4.9 Short questions and their two-mark answers

The following items are worth drilling until they take under a minute each.

For the equation $\frac{dy}{dx} = \frac{x^{2}y+y^{3}}{x^{3}+xy^{2}}$, the two-degree test gives degree three in numerator and denominator, so the equation is homogeneous. Dividing numerator and denominator by $x^{3}$ exposes the ratio: the numerator becomes $v+v^{3}$ and the denominator becomes $1+v^{2}$, so the right-hand side reduces to $v$. The reduced equation is $x\frac{dv}{dx} = 0$, so $v$ is constant and the solution is the family of straight lines $y = Cx$.

For the equation $\frac{dy}{dx} = \frac{x+y}{x^{2}+y^{2}}$, the numerator has degree one and the denominator has degree two, so the equation is not homogeneous, and the correct two-mark answer says so and gives the reason.

For the equation $\left(3x-4y+7\right)dx + \left(4x-3y-7\right)dy = 0$, the determinant is $3\cdot\left(-3\right) - \left(-4\right)\cdot 4 = -9+16 = 7 \neq 0$, so the case is intersecting. The intersection solves $3h-4k = -7$ and $4h-3k = 7$; adding gives $7h - 7k = 0$, so $h = k$, and then $-h = -7$, giving $h = k = 7$. The two-mark answer is the pair $(7,7)$ together with the conclusion.

For $\frac{dy}{dx} = \frac{5x+2y-1}{10x+4y+3}$ the determinant is $5\cdot 4 - 2\cdot 10 = 0$, so the case is parallel, and the substitution is $z = 5x+2y$.

## 5. Mathematical Extensions, Limits, and Common Errors

### 5.1 The trap table

The entries below account for almost every avoidable mark loss in this topic. Each row states the trap as it appears in a script, the cost, and the correction.

| Trap as it appears | Typical cost | What went wrong | Correct move |
| --- | --- | --- | --- |
| writing $\frac{dy}{dx} = v$ after $y = vx$ | 4 marks | $v$ treated as a constant | write $v + x\frac{dv}{dx}$ |
| writing $dy = v\,dx$ in the differential form | 3 marks | the $x\,dv$ term omitted | write $dy = v\,dx + x\,dv$ |
| substituting into the numerator only | 3 marks | substitution applied halfway | substitute in both expressions |
| leaving the answer in $v$ or in $X$ and $Y$ | 2 marks | substitution not undone | restore every letter |
| testing the degree of the fraction instead of of $M$ and $N$ | 2 marks | degree of a quotient is the difference | compare the two degrees separately |
| reading homogeneous as right-hand side zero | whole question | the two meanings confused | homogeneous means degree zero |
| applying the shift with guessed $h$ and $k$ | 3 marks | the point was not computed | solve both line equations |
| applying the shift when $D = 0$ | 4 marks | the case was not decided | compute $D$ first |
| using $z = ax+by$ when $D \neq 0$ | 4 marks | wrong cure for the case | translate the origin instead |
| ignoring $F(v) = v$ | 1 mark | excluded value not tested | test each excluded value |
| dropping the modulus in $\ln$ | 1 mark | domain narrowed silently | keep the absolute value |
| two constants in a first-order answer | 1 mark | an integration was duplicated | combine into one constant |

The first row is the most expensive single error available in the topic, and it is also the easiest to avoid: the corrected line is only four symbols longer than the wrong one.

### 5.2 Question patterns with the response they demand

Pattern one. "Solve the differential equation …" with no guidance. The response must begin with the type test, because the examiner cannot award method marks for a route that was never justified. Write one line stating the type, one line stating the substitution, then proceed.

Pattern two. "Show that the substitution $y = vx$ reduces the equation to …". The response must reach the displayed reduced form exactly as printed, algebraically, before any integration. If the printed form contains a minus sign, the sign must be tracked from the substitution step, not inserted at the end.

Pattern three. "Find the particular solution satisfying $y = a$ when $x = b$." The constant must be determined from the general solution and the final answer must be a single function. Leaving the arbitrary constant in place loses the marks for the condition.

Pattern four. "Determine whether the equation is homogeneous." A yes or no is worth nothing on its own; the test must be shown. The two-degree test is the fastest way to show it.

Pattern five. "Reduce to a homogeneous equation and hence solve." The word hence obliges the script to exhibit the reduced equation explicitly, then solve it, then translate back. Three separate stages, each marked.

### 5.3 Traps that come from the numbers rather than the method

Certain arithmetic features recur and each has a shortcut worth knowing.

When the denominator of the reduced equation is $1+v^{2}$, the integral is an arctangent plus a logarithm, and the answer will involve $\arctan\left(y/x\right)$. Recognising this before integrating saves the partial-fraction attempt that always fails.

When the numerator of the reduced equation is a constant multiple of the derivative of the denominator, the integration is one logarithm and no partial fractions are needed. In the intersecting case this happens exactly when the coefficient of $y$ in the numerator equals the coefficient of $x$ in the denominator, so the pattern can be spotted from the coefficients before any algebra is done.

When the reduced equation has the form $x\frac{dv}{dx} = cv^{2}$ with a single squared term, the integral is a single power and the answer is rational. These arise when the numerator and denominator of the original quotient differ by one power of a single term.

When the parallel case produces a linear numerator that is an exact multiple of the denominator's leading term, the integration splits into a polynomial part and one logarithm, exactly as in Model Solution 4.

### 5.4 Revision checklist

Work through the list in order; each item is a task that can be completed and ticked, not a topic to read.

1. Write from memory the nine lines of the formula sheet, and check them against Section 1.4.
2. Test five expressions for degree, including one that has no degree, and write the exponent explicitly each time.
3. Convert five homogeneous quotients into functions of the ratio by dividing by a power of $x$, without performing any integration.
4. Derive $\frac{dy}{dx} = v + x\frac{dv}{dx}$ in two lines from the product rule.
5. Reduce a homogeneous equation to $x\frac{dv}{dx} = F(v)-v$ five times, stopping before the integration.
6. Integrate the five standard forms in Section 2.3 from memory.
7. Compute $D$ and classify ten linear-over-linear equations, five of each type.
8. Solve three systems for $h$ and $k$, checking each solution in both line equations.
9. Reproduce the two show-that derivations of Sections 3.1 and 3.2 in under four minutes each.
10. Complete Model Solutions 1 to 4 from a blank page, then compare step by step against the marking points.
11. Write out the trap table from memory.
12. Check five finished answers by implicit differentiation, timing each check.

### 5.5 Time strategy for the examination

Read the whole paper first and mark each question with its shape. The classification questions take two minutes and should be taken first, because they are certain marks and they warm up the recall of the tests.

Attempt the separable question next. It is the most predictable and the most likely to be fully correct, and completing it early builds time for the harder items.

Attempt the homogeneous or reducible question third, with the fifteen-minute budget of Section 3.5. If the integration has not produced a closed form after seven minutes, the separation is probably wrong; go back to the step where the variables were separated and check that $F(v)-v$ has been simplified over a single denominator. Almost every stalled homogeneous question is stalled because the subtraction of $v$ was done term by term instead of over a common denominator.

Leave the show-that derivations until last if time is short, because they are short but their marks are small relative to their length. In the final five minutes, check only two things in each answer: that the constant count is one, and that differentiating the answer returns the equation. Those two checks catch the majority of remaining errors.

### 5.6 Consolidated summary of the high-yield content

A separable equation has a right-hand side that factors into a piece in $x$ times a piece in $y$. Moving the $y$-piece to the left and integrating both sides once, then adding one constant, solves it.

A homogeneous function of degree $n$ satisfies $f(kx,ky) = k^{n}f(x,y)$, and a homogeneous equation of first order is one whose right-hand side has degree zero. In the differential form the test is that the coefficients of $dx$ and $dy$ have equal degree.

A homogeneous equation is solved by $y = vx$, which turns it into $x\frac{dv}{dx} = F(v)-v$ and then into $\frac{dv}{F(v)-v} = \frac{dx}{x}$. The integration produces a relation in $v$ and $x$, and $v$ is then replaced by $y/x$ and the fractions cleared.

An equation whose right-hand side is a quotient of two linear expressions is decided by $D = aq-bp$. When $D$ is not zero the origin moves to the crossing point of the two lines and the equation becomes homogeneous; when $D$ is zero the repeated combination $ax+by$ is named $z$ and the equation becomes separable directly.

Every answer is checked by differentiation, every division is recorded, and every substitution is undone.
