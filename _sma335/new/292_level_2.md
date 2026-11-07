## 1. Foundational Concepts, Definitions, and Axioms

### 1.1 Why variable coefficients demand a different strategy

A second-order linear equation with constant coefficients is solved by algebra. Writing $a_{0}\frac{d^{2}y}{dx^{2}}+a_{1}\frac{dy}{dx}+a_{2}y=0$ with numbers $a_{0}\neq 0$, $a_{1}$, $a_{2}$, one substitutes the trial function $y=e^{mx}$ and obtains the characteristic equation

$$
a_{0}m^{2}+a_{1}m+a_{2}=0 .
$$

The two roots of that quadratic exhaust the problem: they are real and distinct, real and repeated, or complex conjugates, and in each case the complementary function is written down at once. The reason the device works is that differentiating $e^{mx}$ returns a multiple of $e^{mx}$, so every term of the equation carries the same factor and the factor can be cancelled. A single algebraic equation then contains all the information.

When the coefficients are functions of the independent variable, the cancellation fails. Differentiating a trial function no longer returns a multiple of the same function, no polynomial in a single symbol $m$ can represent two differentiations, and there is no characteristic equation to solve. The equation

$$
\frac{d^{2}y}{dx^{2}}-\frac{1}{x}\frac{dy}{dx}+4x^{2}y=0
$$

has no characteristic equation, and its solutions $\cos\left(x^{2}\right)$ and $\sin\left(x^{2}\right)$ are not built from $e^{mx}$ with a constant $m$: they are the real and imaginary parts of $e^{ix^{2}}$, in which the exponent is a multiple of $x^{2}$ rather than of $x$. Something inside the equation is measuring distance in a distorted way, and the distortion is what the coefficients record.

The whole of this topic is therefore structural rather than algebraic. Instead of hunting for a magic trial function, one looks for a change of description under which the equation becomes one that is already solvable. Three changes of description are available, and they are the subject of the note: changing the independent variable, removing the first-derivative term, and lowering the order once a single solution is known. A fourth device, recognising that the equation is the derivative of a first-order equation, is the special case in which the equation can be integrated once immediately.

### 1.2 The standard form of the equation

> **Definition (Second-order linear equation with variable coefficients).** Let $a_{0}$, $a_{1}$, $a_{2}$ and $f$ be functions of the independent variable $x$, defined on an interval $I$, with $a_{0}(x)$ never zero on $I$. An equation of the form
>
> $$
> a_{0}(x)\frac{d^{2}y}{dx^{2}}+a_{1}(x)\frac{dy}{dx}+a_{2}(x)y=f(x)
> $$
>
> is a second-order linear differential equation with variable coefficients. The unknown is the function $y$ of the single variable $x$; the order is two because the highest derivative present is the second; and the equation is linear because $y$, $\frac{dy}{dx}$ and $\frac{d^{2}y}{dx^{2}}$ each occur to the first power and are never multiplied together.

The phrase variable coefficients means that $a_{0}$, $a_{1}$ and $a_{2}$ depend on $x$. The phrase linear refers to the unknown function only: a coefficient such as $4x^{2}$ or $\sin x$ is a coefficient, not a nonlinearity, and the equation remains linear however complicated those coefficients are.

Dividing by $a_{0}(x)$, which is legitimate on any interval where $a_{0}$ does not vanish, produces the standard form used throughout the theory.

> **Definition (Standard form).** The standard form of a second-order linear equation is
>
> $$
> \frac{d^{2}y}{dx^{2}}+P(x)\frac{dy}{dx}+Q(x)y=R(x),
> $$
>
> where
>
> $$
> P=\frac{a_{1}}{a_{0}}, \qquad Q=\frac{a_{2}}{a_{0}}, \qquad R=\frac{f}{a_{0}} .
> $$

The requirement that the coefficient of the second derivative be unity is not cosmetic. Every formula in this topic is derived by matching the left side against $\frac{d^{2}y}{dx^{2}}+P\frac{dy}{dx}+Qy$, and applying a formula to a non-standard form produces coefficients that are wrong by the factor $a_{0}$; the error is systematic and silent, because the resulting solutions satisfy a different equation.

The three coefficient functions carry distinct geometric meanings. $Q$ measures the stiffness of a restoring effect and is the only coefficient that survives in the normal form of Section 2.4. $P$ measures a drift or damping effect and is the only coefficient that can be eliminated by a multiplicative change of the dependent variable. $R$ is the applied forcing and does not affect the complementary function at all. Reading an equation as a table of these three functions is the first step of every method in the topic.

### 1.3 Homogeneous and non-homogeneous equations, and the linear operator

> **Definition (Homogeneous equation).** The equation is homogeneous when $R(x)=0$ on $I$, and non-homogeneous otherwise.

The word homogeneous here refers to the right-hand side, not to the coefficients. The equation with variable coefficients

$$
\frac{d^{2}y}{dx^{2}}-\frac{2}{x}\frac{dy}{dx}+\left(25+\frac{2}{x^{2}}\right)y=0
$$

is homogeneous although its coefficients vary; the equation $\frac{d^{2}y}{dx^{2}}+y=x$ is non-homogeneous although its coefficients are constant.

It is convenient to name the operation of forming the left side. Writing $D$ for $\frac{d}{dx}$, define

$$
L[y]=\frac{d^{2}y}{dx^{2}}+P\frac{dy}{dx}+Qy=\left(D^{2}+PD+Q\right)[y] .
$$

The symbol $L$ is a linear operator: it accepts a twice differentiable function and returns a continuous function, and it satisfies

$$
L[c_{1}y_{1}+c_{2}y_{2}]=c_{1}L[y_{1}]+c_{2}L[y_{2}]
$$

for any constants $c_{1}$, $c_{2}$. Linearity in this sense is what allows solutions to be added, and every structural statement below is a statement about $L$.

### 1.4 Superposition and the shape of the general solution

> **Lemma (Superposition).** If $y_{1}$ and $y_{2}$ solve the homogeneous equation $L[y]=0$ on $I$, then every linear combination $c_{1}y_{1}+c_{2}y_{2}$ with constant coefficients solves it on $I$. If $y_{p}$ solves $L[y]=R$, then $y_{p}+c_{1}y_{1}+c_{2}y_{2}$ solves $L[y]=R$.

The proof is a two-line computation using linearity alone, and it is the reason the solution of a non-homogeneous equation splits into two independent tasks: find the complementary function, which solves the homogeneous equation, and find one particular integral, which carries the forcing.

> **Definition (Linear independence and the Wronskian).** Two functions $y_{1}$, $y_{2}$ are linearly independent on $I$ if no identity $c_{1}y_{1}+c_{2}y_{2}=0$ holds on $I$ with $c_{1}$, $c_{2}$ not both zero. Their Wronskian is the determinant
>
> $$
> W(x)=y_{1}y_{2}'-y_{1}'y_{2} .
> $$
>
> If $W(x_{0})\neq 0$ at a single point of $I$, the two functions are linearly independent there and on the whole interval.

> **Theorem (Structure of the general solution).** Let $P$, $Q$, $R$ be continuous on $I$. If $y_{1}$ and $y_{2}$ are linearly independent solutions of $L[y]=0$ on $I$, then every solution of $L[y]=R$ on $I$ has the form
>
> $$
> y=c_{1}y_{1}+c_{2}y_{2}+y_{p} ,
> $$
>
> and conversely every function of that form is a solution. In particular the general solution of a second-order equation always carries exactly two arbitrary constants.

The counting rule is the cheapest check available on any answer produced by the methods below. A second-order equation whose answer contains one constant, or three, is wrong before any substitution is attempted.

### 1.5 The four structural devices, described in words

Each device replaces the given equation by an equation that is easier, and each is a change of variable of a definite kind.

The first device changes the independent variable. A new variable $z$ is defined as a function of $x$, and the unknown is regarded as a function of $z$ rather than of $x$. Because $z$ may compress some parts of the interval and stretch others, a coefficient that varies with $x$ may become constant in the new scale. The classical instance is $z=x^{2}$, which turns $\cos\left(x^{2}\right)$-type behaviour into ordinary trigonometric behaviour.

The second device changes the dependent variable multiplicatively, writing $y=uv$ with $u$ chosen so that the first-derivative term disappears. What remains is called the normal form, $v''+Sv=T$, in which the coefficient of $v'$ is zero. The equation has been brought to the simplest second-order shape, and if $S$ turns out to be a constant the normal form is solved by the characteristic equation after all.

The third device lowers the order. If one non-zero solution $y_{1}$ of the homogeneous equation is known, the substitution $y=uy_{1}$ produces a first-order linear equation for $u'$. One known solution buys a complete solution, because the second solution is then obtained by a single quadrature.

The fourth device is exactness. Occasionally the whole left side is already the derivative of a first-order expression, in which case the equation integrates once and the second-order problem becomes first order with no guessing at all. The test for this is a single algebraic identity among the coefficients.

### 1.6 The linear equation solved for the second derivative, and the interval of validity

Every theorem below assumes that the equation has been put in standard form on an interval on which $P$, $Q$ and $R$ are continuous. That hypothesis is not a formality. The equation

$$
x^{2}\frac{d^{2}y}{dx^{2}}-3x\frac{dy}{dx}+4y=0
$$

has coefficients that are perfectly smooth for $x\neq 0$, but the standard form divides by $x^{2}$, so the interval must be either the positive half-line or the negative half-line, and a solution valid on one half-line need not extend across the origin. The general solution on $x>0$ is

$$
y=x^{2}\left(c_{1}+c_{2}\ln x\right),
$$

which is meaningful only for $x>0$ because of the logarithm. On $x<0$ the same formula with $\ln|x|$ applies. Statements about intervals are therefore part of the answer, not decoration.

## 2. Theorems, Lemmas, and Analytical Properties

### 2.1 Theorem 1: transformation by a change of the independent variable

> **Theorem 1 (change of independent variable).** Let $P$, $Q$, $R$ be continuous on an interval $I$, and let $z=z(x)$ be twice continuously differentiable on $I$ with $z'(x)\neq 0$ there, so that $z$ maps $I$ one-to-one onto an interval $J$. Put $y(x)=Y(z(x))$. Then $y$ solves
>
> $$
> \frac{d^{2}y}{dx^{2}}+P(x)\frac{dy}{dx}+Q(x)y=R(x)
> $$
>
> on $I$ if and only if $Y$ solves
>
> $$
> \frac{d^{2}Y}{dz^{2}}+P_{1}\frac{dY}{dz}+Q_{1}Y=R_{1}
> $$
>
> on $J$, where
>
> $$
> P_{1}=\frac{\frac{d^{2}z}{dx^{2}}+P\frac{dz}{dx}}{\left(\frac{dz}{dx}\right)^{2}}, \qquad Q_{1}=\frac{Q}{\left(\frac{dz}{dx}\right)^{2}}, \qquad R_{1}=\frac{R}{\left(\frac{dz}{dx}\right)^{2}} .
> $$

The three formulas say something worth memorising in words rather than symbols. The coefficient of $Y$ is the old coefficient $Q$ divided by the square of the scale factor. The forcing is divided by the same square. The new first-derivative coefficient is the old one plus the curvature of the new variable, again divided by the square of the scale factor. The square of the scale factor appears everywhere because two differentiations with respect to $x$ are being traded for two with respect to $z$.

### 2.2 Corollary: the choice that makes $Q_{1}$ equal to one

Since $Q_{1}$ is $Q$ divided by a positive quantity, $Q_{1}$ can be normalised to a prescribed constant by choosing the scale factor appropriately. The natural target is one.

> **Corollary 1 (normalising the second-derivative coefficient).** Suppose $Q(x)>0$ on $I$ and set
>
> $$
> z=\int\sqrt{Q(x)}\,dx ,
> $$
>
> so that $\frac{dz}{dx}=\sqrt{Q}$ and $\left(\frac{dz}{dx}\right)^{2}=Q$. Then $Q_{1}=1$ and
>
> $$
> P_{1}=\frac{1}{2}\frac{Q'}{Q^{3/2}}+\frac{P}{\sqrt{Q}} .
> $$
>
> If instead $Q(x)<0$ on $I$, take $z=\int\sqrt{-Q}\,dx$; then $Q_{1}=-1$ and the same computation with $Q$ replaced by $-Q$ applies.

The corollary converts the problem of finding a good change of variable into a quadrature: the scale factor is forced to be $\sqrt{Q}$ and the new variable is its integral. Whether the resulting equation has constant coefficients is then a question about $P_{1}$, which is a definite function that can be computed and inspected.

> **Proposition 1 (the clean case).** With $z=\int\sqrt{Q}\,dx$ and $Q>0$, the coefficient $P_{1}$ vanishes identically if and only if
>
> $$
> Q'+2PQ=0 \quad\text{on } I .
> $$
>
> Under that condition the transformed equation is
>
> $$
> \frac{d^{2}Y}{dz^{2}}+Y=R_{1}, \qquad R_{1}=\frac{R}{Q},
> $$
>
> a constant-coefficient equation whose complementary function is $c_{1}\cos z+c_{2}\sin z$.

The condition has an equivalent form that is often easier to check by eye. Since

$$
\frac{d}{dx}\left(Qe^{2\int P\,dx}\right)=e^{2\int P\,dx}\left(Q'+2PQ\right),
$$

the condition holds exactly when the product $Qe^{2\int P\,dx}$ is constant. For the equation with $P=-\frac{1}{x}$ and $Q=4x^{2}$, that product is $4x^{2}\cdot x^{-2}=4$, a constant, so the clean case applies; this is why the equation of Section 4.3 collapses so completely.

### 2.3 Theorem 2: removal of the first derivative and the normal form

> **Theorem 2 (reduction to normal form).** Let $P$, $Q$, $R$ be continuous on $I$ and let
>
> $$
> u(x)=\exp\left(-\frac{1}{2}\int P(x)\,dx\right),
> $$
>
> which is positive and never zero on $I$. Put $y(x)=u(x)v(x)$. Then $y$ solves
>
> $$
> \frac{d^{2}y}{dx^{2}}+P\frac{dy}{dx}+Qy=R
> $$
>
> on $I$ if and only if $v$ solves the normal form
>
> $$
> \frac{d^{2}v}{dx^{2}}+Sv=T
> $$
>
> where
>
> $$
> S=Q-\frac{1}{4}P^{2}-\frac{1}{2}\frac{dP}{dx}, \qquad T=\frac{R}{u} .
> $$

Three properties of this reduction deserve emphasis, because each of them is used in practice.

First, the normal form contains no first-derivative term, by construction. Every equation of the shape $v''+Sv=T$ is its own normal form, and the reduction is therefore idempotent: applying it twice changes nothing.

Second, the multiplier $u$ is unique up to a constant factor. If $u$ is replaced by $cu$ then $y=uv$ is replaced by $y=(cu)(v/c)$, the same $y$, so nothing is lost or gained. The convention of taking the constant of integration in $\int P\,dx$ to be zero is therefore harmless, and it keeps the working clean.

Third, $u$ never vanishes, so the correspondence between solutions $y$ and solutions $v$ is a bijection. No solution is created or destroyed, and the two arbitrary constants of $v$ become the two arbitrary constants of $y$.

> **Corollary 2 (the constant-coefficient case of the normal form).** If $S$ is a constant and $T$ is a function of $x$ alone, the normal form is a constant-coefficient equation and is solved by the characteristic equation together with a particular-integral rule.

The corollary is the reason the method is worth the algebra: many equations with forbidding variable coefficients have a normal form whose coefficient $S$ is a constant, and those equations are solved in two lines once $S$ is computed.

### 2.4 Theorem 3: the exactness condition

> **Definition (Exact equation).** The equation $L[y]=R$, with $L[y]=y''+Py'+Qy$, is exact on $I$ if there exists a continuously differentiable function $A$ such that
>
> $$
> \frac{d}{dx}\left(\frac{dy}{dx}+Ay\right)=R
> $$
>
> for every twice differentiable $y$.

> **Theorem 3 (exactness test).** The equation $y''+Py'+Qy=R$ is exact if and only if
>
> $$
> \frac{dP}{dx}=Q \quad\text{on } I .
> $$
>
> When the condition holds, the equation is equivalent to the first-order linear equation
>
> $$
> \frac{dy}{dx}+Py=\int R(x)\,dx+C ,
> $$
>
> which is solved by the integrating factor $e^{\int P\,dx}$.

For a general equation in the form $a_{0}y''+a_{1}y'+a_{2}y=R$ the same test reads

$$
\frac{d^{2}a_{0}}{dx^{2}}-\frac{da_{1}}{dx}+a_{2}=0 ,
$$

and the standard-form test is the special case $a_{0}=1$. The condition is a single identity to check, and when it holds the second-order problem has genuinely become first order.

> **Lemma (factorisation of a second-order operator).** For differentiable $A$ and $B$,
>
> $$
> \left(D+A\right)\left(D+B\right)[y]=\frac{d^{2}y}{dx^{2}}+\left(A+B\right)\frac{dy}{dx}+\left(\frac{dB}{dx}+AB\right)y .
> $$

Comparing $\frac{dB}{dx}+AB$ with $Q$ and $A+B$ with $P$ shows that exactness is the case $B=0$ of this factorisation: the operator collapses to $\left(D+P\right)D$, whose kernel is $\frac{dy}{dx}+Py=$ constant. The lemma also explains why exactness is a rare accident rather than a general property: two conditions are being imposed on two coefficient functions, and both must hold simultaneously.

### 2.5 Theorem 4: reduction of order from one known solution

> **Theorem 4 (reduction of order).** Let $y_{1}$ be a solution of the homogeneous equation $y''+Py'+Qy=0$ on $I$ with $y_{1}(x)\neq 0$ there. Put $y(x)=u(x)y_{1}(x)$. Then $y$ solves the homogeneous equation if and only if $u'$ solves the first-order linear equation
>
> $$
> \frac{dw}{dx}+\left(\frac{2y_{1}'}{y_{1}}+P\right)w=0, \qquad w=\frac{du}{dx},
> $$
>
> and consequently
>
> $$
> y=y_{1}\left(C_{1}+C_{2}\int\frac{e^{-\int P\,dx}}{y_{1}^{2}}\,dx\right) .
> $$

The hypotheses are exactly what the derivation needs: $y_{1}\neq 0$ so that the division by $y_{1}$ in forming $u=y/y_{1}$ is legitimate, and $y_{1}$ a genuine solution so that the term multiplying $u$ itself cancels. The second solution is then produced by one quadrature, and the two constants $C_{1}$, $C_{2}$ appear at the two integrations.

### 2.6 Which method applies: a diagnostic table

The methods are not interchangeable, and choosing wrongly wastes the whole answer. The signatures below are read off the standard form.

| Signature of the standard form | Structural situation | Method to use |
| --- | --- | --- |
| $Q>0$ and $Q'+2PQ=0$ | The clean case of Proposition 1 | Change of independent variable, $z=\int\sqrt{Q}\,dx$ |
| $Q>0$ and $P_{1}$ in Corollary 1 is constant | Equation is constant-coefficient in disguise | Change of independent variable, $z=\int\sqrt{Q}\,dx$ |
| $S=Q-\frac{1}{4}P^{2}-\frac{1}{2}P'$ is constant | Normal form has constant coefficients | Removal of the first derivative, $y=uv$ |
| $P'=Q$ | Left side is a perfect derivative | Exactness, integrate once |
| One non-zero solution $y_{1}$ is given | Order can be lowered | Reduction of order, $y=uy_{1}$ |
| None of the above and no solution supplied | No elementary route from the coefficients alone | Numerical or series treatment |

The table is a decision list, not a taxonomy. In a long question the same equation may be attacked in two ways, and the two answers must agree; that agreement is a powerful check on the arithmetic.

## 3. Formal Proofs, Derivations, and Methods

### 3.1 Proof of Theorem 1

Step 1. Record the two chain-rule identities that carry the whole proof. With $y(x)=Y(z(x))$,

$$
\frac{dy}{dx}=\frac{dY}{dz}\cdot\frac{dz}{dx} .
$$

Step 2. Differentiate this product with respect to $x$, treating $\frac{dY}{dz}$ as a function of $z$ and hence of $x$.

$$
\frac{d^{2}y}{dx^{2}}=\frac{d}{dx}\left(\frac{dY}{dz}\right)\cdot\frac{dz}{dx}+\frac{dY}{dz}\cdot\frac{d^{2}z}{dx^{2}}
$$

Step 3. Apply the chain rule to the first factor.

$$
\frac{d}{dx}\left(\frac{dY}{dz}\right)=\frac{d^{2}Y}{dz^{2}}\cdot\frac{dz}{dx}
$$

Step 4. Combine the two previous displays.

$$
\frac{d^{2}y}{dx^{2}}=\frac{d^{2}Y}{dz^{2}}\left(\frac{dz}{dx}\right)^{2}+\frac{dY}{dz}\cdot\frac{d^{2}z}{dx^{2}}
$$

Step 5. Substitute both derivatives into the original equation.

$$
\left(\frac{dz}{dx}\right)^{2}\frac{d^{2}Y}{dz^{2}}+\left(\frac{d^{2}z}{dx^{2}}+P\frac{dz}{dx}\right)\frac{dY}{dz}+QY=R
$$

Step 6. Divide by the positive quantity $\left(\frac{dz}{dx}\right)^{2}$, which is legitimate because $z'\neq 0$ on $I$.

$$
\frac{d^{2}Y}{dz^{2}}+\frac{\frac{d^{2}z}{dx^{2}}+P\frac{dz}{dx}}{\left(\frac{dz}{dx}\right)^{2}}\cdot\frac{dY}{dz}+\frac{Q}{\left(\frac{dz}{dx}\right)^{2}}Y=\frac{R}{\left(\frac{dz}{dx}\right)^{2}}
$$

Step 7. Read off the three coefficients and rename them. This is exactly the statement of Theorem 1, and because every step was reversible the equivalence of the two equations is established.

A practical warning belongs with the proof. The coefficients $P_{1}$, $Q_{1}$, $R_{1}$ as written are functions of $x$, and the transformed equation is only usable once they have been rewritten as functions of $z$. In the examples that follow, $z$ is a simple expression in $x$ and the rewriting is immediate; when it is not immediate, the change of variable is a poor choice.

### 3.2 Derivation of Corollary 1 and of the clean case

Step 1. Impose $Q_{1}=1$. By Theorem 1 this means

$$
\frac{Q}{\left(\frac{dz}{dx}\right)^{2}}=1, \quad\text{so}\quad \frac{dz}{dx}=\sqrt{Q}
$$

taking the positive root, which is legitimate because $Q>0$.

Step 2. Integrate to obtain the new variable.

$$
z=\int\sqrt{Q(x)}\,dx+C
$$

The constant only shifts $z$ and changes no coefficient, so it is taken as zero.

Step 3. Differentiate $\frac{dz}{dx}=\sqrt{Q}$ once more to obtain the curvature of the new variable.

$$
\frac{d^{2}z}{dx^{2}}=\frac{Q'}{2\sqrt{Q}}
$$

Step 4. Substitute into the formula for $P_{1}$.

$$
P_{1}=\frac{\frac{Q'}{2\sqrt{Q}}+P\sqrt{Q}}{Q}=\frac{Q'}{2Q^{3/2}}+\frac{P}{\sqrt{Q}}
$$

Step 5. Put $P_{1}=0$ and multiply by $2Q^{3/2}$, which is positive.

$$
Q'+2PQ=0
$$

Step 6. Record the transformed equation. With $Q_{1}=1$ and $P_{1}=0$, Theorem 1 gives $\frac{d^{2}Y}{dz^{2}}+Y=R_{1}$, and $R_{1}=R/Q$ by the third formula. Since $Q$ is itself a function of $z$ once $x$ is eliminated, $R_{1}$ is a known function of the new variable. This is Proposition 1.

### 3.3 Proof of Theorem 2

Step 1. Write $y=uv$ and differentiate once, using the product rule.

$$
\frac{dy}{dx}=u\frac{dv}{dx}+v\frac{du}{dx}
$$

Step 2. Differentiate again, applying the product rule to each of the two terms.

$$
\frac{d^{2}y}{dx^{2}}=u\frac{d^{2}v}{dx^{2}}+2\frac{du}{dx}\frac{dv}{dx}+v\frac{d^{2}u}{dx^{2}}
$$

Step 3. Substitute both into the equation $y''+Py'+Qy=R$.

$$
u\frac{d^{2}v}{dx^{2}}+\left(2\frac{du}{dx}+Pu\right)\frac{dv}{dx}+\left(\frac{d^{2}u}{dx^{2}}+P\frac{du}{dx}+Qu\right)v=R
$$

Step 4. Choose $u$ so that the coefficient of $\frac{dv}{dx}$ is zero. That is one first-order equation for $u$,

$$
2\frac{du}{dx}+Pu=0 ,
$$

whose solution is found by separating variables.

$$
\frac{1}{u}\frac{du}{dx}=-\frac{P}{2}
$$

Step 5. Integrate.

$$
\ln|u|=-\frac{1}{2}\int P\,dx , \qquad u=\exp\left(-\frac{1}{2}\int P\,dx\right)
$$

The absolute value is dropped because the exponential is positive; this is also the reason $u$ never vanishes.

Step 6. Divide the equation of Step 3 by $u$, which is allowed since $u>0$.

$$
\frac{d^{2}v}{dx^{2}}+\frac{1}{u}\left(\frac{d^{2}u}{dx^{2}}+P\frac{du}{dx}+Qu\right)v=\frac{R}{u}
$$

Step 7. Evaluate the coefficient of $v$. From Step 5,

$$
\frac{du}{dx}=-\frac{P}{2}u, \qquad \frac{d^{2}u}{dx^{2}}=-\frac{P'}{2}u+\frac{P^{2}}{4}u ,
$$

the second derivative being obtained by differentiating the product $-\frac{P}{2}u$ and substituting the known expression for $u'$.

Step 8. Substitute these into the bracket.

$$
\frac{d^{2}u}{dx^{2}}+P\frac{du}{dx}+Qu=u\left(\frac{P^{2}}{4}-\frac{P'}{2}-\frac{P^{2}}{2}+Q\right)=u\left(Q-\frac{P^{2}}{4}-\frac{P'}{2}\right)
$$

Step 9. Divide by $u$ and read off the result.

$$
\frac{d^{2}v}{dx^{2}}+\left(Q-\frac{P^{2}}{4}-\frac{P'}{2}\right)v=\frac{R}{u}
$$

This is the normal form, with $S$ and $T$ as stated in Theorem 2. Every step is reversible because $u>0$, so the two equations have exactly the same solution sets after the substitution $y=uv$.

### 3.4 Proof of Theorem 3

Step 1. Suppose the equation is exact, so that for some continuously differentiable $A$,

$$
\frac{d}{dx}\left(\frac{dy}{dx}+Ay\right)=R
$$

Step 2. Expand the derivative on the left.

$$
\frac{d^{2}y}{dx^{2}}+A\frac{dy}{dx}+\frac{dA}{dx}y=R
$$

Step 3. Compare with $y''+Py'+Qy=R$. The coefficients of $y'$ and of $y$ must agree for the identity to hold for all $y$, so

$$
A=P, \qquad \frac{dA}{dx}=Q .
$$

Step 4. Combine the two relations into the necessary condition $P'=Q$.

Step 5. Conversely, if $P'=Q$, then the derivative of $y'+Py$ is $y''+Py'+P'y=y''+Py'+Qy$, so the left side is exactly a derivative and the equation is exact. Necessity and sufficiency are both established.

Step 6. Integrate once. If $y''+Py'+Qy=R$ with $Q=P'$, then

$$
\frac{d}{dx}\left(\frac{dy}{dx}+Py\right)=R ,
$$

so

$$
\frac{dy}{dx}+Py=\int R\,dx+C ,
$$

a first-order linear equation. For the general form $a_{0}y''+a_{1}y'+a_{2}y=R$ the same comparison of coefficients with $\frac{d}{dx}\left(a_{0}y'+By\right)$ gives $B=a_{1}-a_{0}'$ and then $B'=a_{2}$, that is $a_{0}''-a_{1}'+a_{2}=0$.

### 3.5 Derivation of reduction of order

Step 1. Put $y=uy_{1}$ and differentiate twice.

$$
\frac{dy}{dx}=u'y_{1}+uy_{1}' , \qquad \frac{d^{2}y}{dx^{2}}=u''y_{1}+2u'y_{1}'+uy_{1}''
$$

Step 2. Substitute into $y''+Py'+Qy=0$.

$$
u''y_{1}+u'\left(2y_{1}'+Py_{1}\right)+u\left(y_{1}''+Py_{1}'+Qy_{1}\right)=0
$$

Step 3. Use the hypothesis that $y_{1}$ solves the homogeneous equation, so the bracket multiplying $u$ is zero.

$$
u''y_{1}+u'\left(2y_{1}'+Py_{1}\right)=0
$$

Step 4. Divide by $y_{1}$, which is legitimate because $y_{1}\neq 0$ on $I$.

$$
u''+\left(\frac{2y_{1}'}{y_{1}}+P\right)u'=0
$$

Step 5. Put $w=u'$. The equation becomes first order in $w$.

$$
\frac{dw}{dx}+\left(\frac{2y_{1}'}{y_{1}}+P\right)w=0
$$

Step 6. Separate and integrate, noting that $\frac{2y_{1}'}{y_{1}}$ is the derivative of $2\ln|y_{1}|$.

$$
\ln|w|=-2\ln|y_{1}|-\int P\,dx+\text{constant}, \qquad w=\frac{C_{2}e^{-\int P\,dx}}{y_{1}^{2}}
$$

Step 7. Integrate once more to obtain $u$.

$$
u=C_{1}+C_{2}\int\frac{e^{-\int P\,dx}}{y_{1}^{2}}\,dx
$$

Step 8. Multiply back by $y_{1}$ to obtain the general solution of the homogeneous equation.

$$
y=y_{1}\left(C_{1}+C_{2}\int\frac{e^{-\int P\,dx}}{y_{1}^{2}}\,dx\right)
$$

Step 9. Confirm the count. Two arbitrary constants appear, one at each integration, as a second-order equation requires. The integrand is a known function of $x$, so the formula is an explicit answer whenever the quadrature can be performed.

### 3.6 The standard procedure for each method

For a change of independent variable: put the equation in standard form; read off $Q$; check that $Q$ has a constant sign on the interval; set $z=\int\sqrt{|Q|}\,dx$; compute $P_{1}$, $Q_{1}$, $R_{1}$; decide whether the transformed equation has constant coefficients; solve it in $z$; then replace $z$ by its expression in $x$.

For the normal form: put the equation in standard form; read off $P$; compute $u=\exp\left(-\frac{1}{2}\int P\,dx\right)$; compute $S=Q-\frac{1}{4}P^{2}-\frac{1}{2}P'$ and $T=R/u$; solve $v''+Sv=T$; multiply by $u$. The two steps that carry the marks are the computation of $S$ and the correct expression for $T$, so both should be displayed.

For exactness: put the equation in standard form; check whether $P'=Q$; if it holds, integrate once; solve the resulting first-order equation.

For reduction of order: verify that the supplied $y_{1}$ really solves the homogeneous equation by substitution, because a misprinted $y_{1}$ destroys the rest of the answer; then apply the formula, or carry out the substitution $y=uy_{1}$ explicitly.

## 4. Representative Worked Examples and Solutions

### 4.1 Problem: reduce an equation to standard form

Write the equation

$$
2x^{2}\frac{d^{2}y}{dx^{2}}-3x\frac{dy}{dx}+5y=\ln x
$$

in standard form on the interval $x>0$ and identify the three coefficient functions.

### 4.2 Solution: divide by the coefficient of the second derivative

Step 1. Divide the whole equation by $2x^{2}$. This is legitimate on $x>0$, where the divisor does not vanish.

$$
\frac{d^{2}y}{dx^{2}}-\frac{3}{2x}\frac{dy}{dx}+\frac{5}{2x^{2}}y=\frac{\ln x}{2x^{2}}
$$

Step 2. Read off the coefficients by comparison with $y''+Py'+Qy=R$.

$$
P(x)=-\frac{3}{2x}, \qquad Q(x)=\frac{5}{2x^{2}}, \qquad R(x)=\frac{\ln x}{2x^{2}}
$$

Step 3. Note what has been gained. The coefficients are now continuous on $x>0$, the equation is in the form every formula of Section 2 assumes, and the interval of validity is stated.

Step 4. Record the two diagnostics that will be needed later, $Q>0$ on $x>0$ and $P'=\frac{3}{2x^{2}}$, so the equation is not exact because $P'\neq Q$. Exactness is therefore ruled out, and one of the remaining devices must be tried.

### 4.3 Problem: solve by changing the independent variable

Solve

$$
x\frac{d^{2}y}{dx^{2}}-\frac{dy}{dx}+4x^{3}y=x^{5}
$$

on $x>0$.

### 4.4 Solution: use $z=x^{2}$ so that the equation becomes $Y''+Y=\frac{z}{4}$

Step 1. Put the equation in standard form by dividing by $x$.

$$
\frac{d^{2}y}{dx^{2}}-\frac{1}{x}\frac{dy}{dx}+4x^{2}y=x^{4}
$$

Step 2. Identify the coefficients and test the clean-case condition of Proposition 1.

$$
P=-\frac{1}{x}, \qquad Q=4x^{2}, \qquad R=x^{4}
$$

Step 3. Compute $Q'+2PQ$ to confirm that the clean case applies.

$$
Q'=8x, \qquad Q'+2PQ=8x+2\left(-\frac{1}{x}\right)\left(4x^{2}\right)=8x-8x=0
$$

Step 4. Choose the new variable by Corollary 1, taking the positive square root of $Q$.

$$
\frac{dz}{dx}=\sqrt{Q}=2x, \qquad z=x^{2}
$$

Step 5. Compute the ingredients of the three coefficient formulas. Here $\frac{dz}{dx}=2x$ and $\frac{d^{2}z}{dx^{2}}=2$.

$$
\left(\frac{dz}{dx}\right)^{2}=4x^{2}, \qquad \frac{d^{2}z}{dx^{2}}=2
$$

Step 6. Compute $P_{1}$.

$$
P_{1}=\frac{2+\left(-\frac{1}{x}\right)\left(2x\right)}{4x^{2}}=\frac{2-2}{4x^{2}}=0
$$

Step 7. Compute $Q_{1}$.

$$
Q_{1}=\frac{4x^{2}}{4x^{2}}=1
$$

Step 8. Compute $R_{1}$ and express it in the new variable, using $x^{2}=z$.

$$
R_{1}=\frac{x^{4}}{4x^{2}}=\frac{x^{2}}{4}=\frac{z}{4}
$$

Step 9. Write the transformed equation, which by Theorem 1 is equivalent to the original.

$$
\frac{d^{2}Y}{dz^{2}}+Y=\frac{z}{4}
$$

Step 10. Solve the complementary function from the characteristic equation $m^{2}+1=0$, whose roots are $\pm i$.

$$
Y_{c}=c_{1}\cos z+c_{2}\sin z
$$

Step 11. Find a particular integral by trying a linear function $Y=az$, whose second derivative is zero.

$$
az=\frac{z}{4}\quad\text{for all }z,\qquad a=\frac{1}{4}
$$

Step 12. Assemble the general solution in $z$.

$$
Y=c_{1}\cos z+c_{2}\sin z+\frac{z}{4}
$$

Step 13. Return to the original variable by substituting $z=x^{2}$.

$$
y=c_{1}\cos\left(x^{2}\right)+c_{2}\sin\left(x^{2}\right)+\frac{x^{2}}{4}
$$

Step 14. Verify the particular integral in the original equation. With $y=\frac{x^{2}}{4}$ the derivatives are $y'=\frac{x}{2}$ and $y''=\frac{1}{2}$, so

$$
x\cdot\frac{1}{2}-\frac{x}{2}+4x^{3}\cdot\frac{x^{2}}{4}=\frac{x}{2}-\frac{x}{2}+x^{5}=x^{5},
$$

which is the required right-hand side.

Step 15. Verify one complementary solution. With $y=\cos\left(x^{2}\right)$ the chain rule gives $y'=-2x\sin\left(x^{2}\right)$ and

$$
y''=-2\sin\left(x^{2}\right)-4x^{2}\cos\left(x^{2}\right),
$$

so that

$$
x\left(-2\sin\left(x^{2}\right)-4x^{2}\cos\left(x^{2}\right)\right)+2x\sin\left(x^{2}\right)+4x^{3}\cos\left(x^{2}\right)=0 .
$$

Every term cancels in pairs, so the homogeneous equation is satisfied. The answer is confirmed, and it carries exactly two arbitrary constants as a second-order equation requires.

### 4.5 Problem: a change of variable that solves an Euler equation

Solve

$$
x^{2}\frac{d^{2}y}{dx^{2}}-3x\frac{dy}{dx}+4y=0
$$

on $x>0$ by changing the independent variable.

### 4.6 Solution: use $z=2\ln x$

Step 1. Put the equation in standard form by dividing by $x^{2}$.

$$
\frac{d^{2}y}{dx^{2}}-\frac{3}{x}\frac{dy}{dx}+\frac{4}{x^{2}}y=0
$$

Step 2. Identify $P=-\frac{3}{x}$ and $Q=\frac{4}{x^{2}}$, and note that $Q>0$ on $x>0$.

Step 3. Take the square root of $Q$ and integrate, as Corollary 1 directs.

$$
\frac{dz}{dx}=\frac{2}{x}, \qquad z=2\ln x
$$

Step 4. Compute the squared scale factor and the curvature of the new variable.

$$
\left(\frac{dz}{dx}\right)^{2}=\frac{4}{x^{2}}, \qquad \frac{d^{2}z}{dx^{2}}=-\frac{2}{x^{2}}
$$

Step 5. Compute $P_{1}$.

$$
P_{1}=\frac{-\frac{2}{x^{2}}+\left(-\frac{3}{x}\right)\left(\frac{2}{x}\right)}{\frac{4}{x^{2}}}=\frac{-\frac{2}{x^{2}}-\frac{6}{x^{2}}}{\frac{4}{x^{2}}}=-\frac{8}{4}=-2
$$

Step 6. Compute $Q_{1}$ and observe that the coefficient is a constant, so the method has succeeded.

$$
Q_{1}=\frac{\frac{4}{x^{2}}}{\frac{4}{x^{2}}}=1
$$

Step 7. Write the transformed equation.

$$
\frac{d^{2}Y}{dz^{2}}-2\frac{dY}{dz}+Y=0
$$

Step 8. Solve by the characteristic equation $m^{2}-2m+1=(m-1)^{2}=0$, which has the repeated root $m=1$.

$$
Y=\left(c_{1}+c_{2}z\right)e^{z}
$$

Step 9. Substitute $z=2\ln x$ and $e^{z}=e^{2\ln x}=x^{2}$.

$$
y=x^{2}\left(c_{1}+2c_{2}\ln x\right)
$$

Step 10. Verify the second solution $y=x^{2}\ln x$, which is the one a repeated root always produces. Its derivatives are $y'=2x\ln x+x$ and $y''=2\ln x+3$, so

$$
x^{2}\left(2\ln x+3\right)-3x\left(2x\ln x+x\right)+4x^{2}\ln x=\left(2-6+4\right)x^{2}\ln x+\left(3-3\right)x^{2}=0 .
$$

Step 11. Interpret the result. The general Euler equation $x^{2}y''+axy'+by=0$ with $b>0$ becomes, under $z=\sqrt{b}\ln x$, the constant-coefficient equation

$$
\frac{d^{2}Y}{dz^{2}}+\frac{a-1}{\sqrt{b}}\frac{dY}{dz}+Y=0 ,
$$

so the Euler equation is a constant-coefficient equation viewed through a logarithmic scale. Here $a=-3$ and $b=4$, giving $\frac{a-1}{\sqrt{b}}=-2$, exactly the coefficient found in Step 5.

### 4.7 Problem: reduce to normal form and solve

Solve

$$
\frac{d^{2}y}{dx^{2}}-4x\frac{dy}{dx}+\left(4x^{2}-3\right)y=xe^{x^{2}} .
$$

### 4.8 Solution: remove the first derivative with $u=e^{x^{2}}$

Step 1. The equation is already in standard form, so read off the coefficients.

$$
P=-4x, \qquad Q=4x^{2}-3, \qquad R=xe^{x^{2}}
$$

Step 2. Compute the exponent $-\frac{1}{2}\int P\,dx$ in the formula for $u$.

$$
-\frac{1}{2}\int\left(-4x\right)dx=\int 2x\,dx=x^{2}
$$

Step 3. Write down the multiplier.

$$
u=e^{x^{2}}
$$

Step 4. Compute $P^{2}$ and $P'$, the two ingredients of $S$.

$$
P^{2}=16x^{2}, \qquad \frac{dP}{dx}=-4
$$

Step 5. Compute $S$.

$$
S=4x^{2}-3-\frac{16x^{2}}{4}-\frac{1}{2}\left(-4\right)=4x^{2}-3-4x^{2}+2=-1
$$

Step 6. Compute $T$.

$$
T=\frac{R}{u}=\frac{xe^{x^{2}}}{e^{x^{2}}}=x
$$

Step 7. Write the normal form.

$$
\frac{d^{2}v}{dx^{2}}-v=x
$$

Step 8. Solve the complementary function from $m^{2}-1=0$, whose roots are $\pm1$.

$$
v_{c}=c_{1}e^{x}+c_{2}e^{-x}
$$

Step 9. Find a particular integral by trying $v=ax$, whose second derivative is zero.

$$
0-ax=x\quad\text{for all }x,\qquad a=-1
$$

Step 10. Assemble the general solution in $v$.

$$
v=c_{1}e^{x}+c_{2}e^{-x}-x
$$

Step 11. Multiply by $u=e^{x^{2}}$ to return to $y$.

$$
y=e^{x^{2}}\left(c_{1}e^{x}+c_{2}e^{-x}-x\right)
$$

Step 12. Verify the particular integral $y_{p}=-xe^{x^{2}}$ in the original equation. Its derivatives are

$$
y_{p}'=-e^{x^{2}}\left(1+2x^{2}\right), \qquad y_{p}''=-e^{x^{2}}\left(6x+4x^{3}\right).
$$

Step 13. Substitute the three expressions into the left-hand side.

$$
-e^{x^{2}}\left(6x+4x^{3}\right)+4xe^{x^{2}}\left(1+2x^{2}\right)-x\left(4x^{2}-3\right)e^{x^{2}}
$$

Step 14. Collect the powers of $x$ inside the bracket.

$$
\left(-6x-4x^{3}\right)+\left(4x+8x^{3}\right)+\left(-4x^{3}+3x\right)=\left(-6+4+3\right)x+\left(-4+8-4\right)x^{3}=x
$$

Step 15. Conclude. The left-hand side equals $xe^{x^{2}}$, which is the prescribed forcing, so the particular integral is correct and the general solution stands. The answer is confirmed and carries two constants.

### 4.9 Problem: normal form when the coefficients are trigonometric

Solve

$$
\frac{d^{2}y}{dx^{2}}-2\tan x\frac{dy}{dx}+5y=0
$$

on an interval where $\tan x$ is continuous.

### 4.10 Solution: the multiplier is a secant

Step 1. Read off $P=-2\tan x$, $Q=5$ and $R=0$.

Step 2. Compute the exponent of $u$, using $\int\tan x\,dx=-\ln\left(\cos x\right)$.

$$
-\frac{1}{2}\int\left(-2\tan x\right)dx=\int\tan x\,dx=-\ln\left(\cos x\right)
$$

Step 3. Write down the multiplier.

$$
u=\exp\left(-\ln\left(\cos x\right)\right)=\frac{1}{\cos x}=\sec x
$$

Step 4. Compute the two ingredients of $S$, using $\frac{d}{dx}\tan x=\sec^{2}x$.

$$
P^{2}=4\tan^{2}x, \qquad \frac{dP}{dx}=-2\sec^{2}x
$$

Step 5. Compute $S$.

$$
S=5-\frac{4\tan^{2}x}{4}-\frac{1}{2}\left(-2\sec^{2}x\right)=5-\tan^{2}x+\sec^{2}x
$$

Step 6. Use the identity $\sec^{2}x-\tan^{2}x=1$ to simplify.

$$
S=5+1=6
$$

Step 7. Write the normal form, which has constant coefficients.

$$
\frac{d^{2}v}{dx^{2}}+6v=0
$$

Step 8. Solve it from $m^{2}+6=0$, whose roots are $\pm i\sqrt{6}$.

$$
v=c_{1}\cos\left(\sqrt{6}\,x\right)+c_{2}\sin\left(\sqrt{6}\,x\right)
$$

Step 9. Multiply by $u=\sec x$.

$$
y=\sec x\left(c_{1}\cos\left(\sqrt{6}\,x\right)+c_{2}\sin\left(\sqrt{6}\,x\right)\right)
$$

Step 10. Check the value of $S$ by the alternative route, computing the bracket $\frac{u''+Pu'+Qu}{u}$ directly when $u=\sec x$. Here $u'=\sec x\tan x$ and $u''=\sec x\tan^{2}x+\sec^{3}x$, so

$$
u''+Pu'+Qu=\sec x\left(\tan^{2}x+\sec^{2}x-2\tan^{2}x+5\right)=\sec x\cdot 6 ,
$$

and dividing by $u=\sec x$ returns $6$, in agreement with Step 6. The two constants in the final answer match the order of the equation.

### 4.11 Problem: a normal form whose forcing is not zero

Solve

$$
\frac{d^{2}y}{dx^{2}}+2x\frac{dy}{dx}+\left(x^{2}+5\right)y=xe^{-x^{2}/2} .
$$

### 4.12 Solution: the multiplier is a Gaussian

Step 1. Read off $P=2x$, $Q=x^{2}+5$ and $R=xe^{-x^{2}/2}$.

Step 2. Compute the exponent of $u$.

$$
-\frac{1}{2}\int 2x\,dx=-\frac{x^{2}}{2}
$$

Step 3. Write down the multiplier.

$$
u=e^{-x^{2}/2}
$$

Step 4. Compute the ingredients of $S$.

$$
P^{2}=4x^{2}, \qquad \frac{dP}{dx}=2
$$

Step 5. Compute $S$.

$$
S=x^{2}+5-\frac{4x^{2}}{4}-\frac{1}{2}\left(2\right)=x^{2}+5-x^{2}-1=4
$$

Step 6. Compute $T$.

$$
T=\frac{xe^{-x^{2}/2}}{e^{-x^{2}/2}}=x
$$

Step 7. Write the normal form.

$$
\frac{d^{2}v}{dx^{2}}+4v=x
$$

Step 8. Solve the complementary function from $m^{2}+4=0$.

$$
v_{c}=c_{1}\cos 2x+c_{2}\sin 2x
$$

Step 9. Find a particular integral by trying $v=ax$.

$$
4ax=x\quad\text{for all }x,\qquad a=\frac{1}{4}
$$

Step 10. Assemble $v$ and multiply by $u$.

$$
y=e^{-x^{2}/2}\left(c_{1}\cos 2x+c_{2}\sin 2x+\frac{x}{4}\right)
$$

Step 11. Verify the particular integral $y_{p}=\frac{x}{4}e^{-x^{2}/2}$. Its derivatives are

$$
y_{p}'=\frac{1}{4}e^{-x^{2}/2}\left(1-x^{2}\right), \qquad y_{p}''=\frac{1}{4}e^{-x^{2}/2}\left(x^{3}-3x\right).
$$

Step 12. Substitute into the left-hand side and factor out the exponential.

$$
\frac{1}{4}e^{-x^{2}/2}\left[\left(x^{3}-3x\right)+2x\left(1-x^{2}\right)+x\left(x^{2}+5\right)\right]
$$

Step 13. Collect inside the bracket.

$$
x^{3}-2x^{3}+x^{3}+\left(-3+2+5\right)x=4x
$$

Step 14. Conclude. The left-hand side is $\frac{1}{4}e^{-x^{2}/2}\cdot 4x=xe^{-x^{2}/2}$, which is the required forcing, so the answer is confirmed.

### 4.13 Problem: exploit exactness

Solve

$$
\frac{d^{2}y}{dx^{2}}+\frac{1}{x}\frac{dy}{dx}-\frac{1}{x^{2}}y=0
$$

on $x>0$.

### 4.14 Solution: the left side is already a derivative

Step 1. Read off $P=\frac{1}{x}$ and $Q=-\frac{1}{x^{2}}$, and compute $P'$.

$$
\frac{dP}{dx}=-\frac{1}{x^{2}}
$$

Step 2. Compare $P'$ with $Q$. They are equal, so by Theorem 3 the equation is exact.

Step 3. Rewrite the equation as a single derivative, which is what exactness means.

$$
\frac{d}{dx}\left(\frac{dy}{dx}+\frac{1}{x}y\right)=0
$$

Step 4. Integrate once with respect to $x$.

$$
\frac{dy}{dx}+\frac{1}{x}y=C_{1}
$$

Step 5. Solve the first-order linear equation. The integrating factor is $e^{\int\frac{1}{x}dx}=x$.

$$
x\frac{dy}{dx}+y=C_{1}x
$$

Step 6. Recognise the left side as the derivative of a product.

$$
\frac{d}{dx}\left(xy\right)=C_{1}x
$$

Step 7. Integrate again.

$$
xy=\frac{C_{1}}{2}x^{2}+C_{2}
$$

Step 8. Divide by $x$.

$$
y=\frac{C_{1}}{2}x+\frac{C_{2}}{x}
$$

Step 9. Rename the constants to tidy the answer, since $C_{1}/2$ is itself an arbitrary constant.

$$
y=Ax+\frac{B}{x}
$$

Step 10. Verify both solutions. For $y=x$ the derivatives are $1$ and $0$, so the left side is $0+\frac{1}{x}-\frac{1}{x^{2}}\cdot x=\frac{1}{x}-\frac{1}{x}=0$. For $y=\frac{1}{x}$ the derivatives are $-\frac{1}{x^{2}}$ and $\frac{2}{x^{3}}$, so the left side is

$$
\frac{2}{x^{3}}-\frac{1}{x^{3}}-\frac{1}{x^{3}}=0 .
$$

Both are confirmed, and the two independent solutions together carry the two constants the order demands.

### 4.15 Problem: reduce the order given one solution

Given that $y_{1}=x^{3}$ is a solution of

$$
\frac{d^{2}y}{dx^{2}}-\frac{1}{x}\frac{dy}{dx}-\frac{3}{x^{2}}y=0 ,
$$

find the general solution on $x>0$.

### 4.16 Solution: substitute $y=uy_{1}$ and solve for $u'$

Step 1. Confirm the supplied solution, since everything depends on it. With $y_{1}=x^{3}$ we have $y_{1}'=3x^{2}$ and $y_{1}''=6x$, so

$$
6x-\frac{1}{x}\cdot 3x^{2}-\frac{3}{x^{2}}\cdot x^{3}=6x-3x-3x=0 ,
$$

and $y_{1}$ is indeed a solution.

Step 2. Put $y=ux^{3}$ and differentiate twice by the product rule.

$$
\frac{dy}{dx}=3x^{2}u+x^{3}\frac{du}{dx}, \qquad \frac{d^{2}y}{dx^{2}}=6xu+6x^{2}\frac{du}{dx}+x^{3}\frac{d^{2}u}{dx^{2}}
$$

Step 3. Substitute into the equation.

$$
6xu+6x^{2}u'+x^{3}u''-3xu-3x^{2}u'-\frac{3}{x^{2}}\cdot x^{3}u=0
$$

Step 4. Collect the terms in $u$, which cancel by Step 1.

$$
\left(6x-3x-3x\right)u=0
$$

Step 5. Collect the terms in $u'$, which survive.

$$
6x^{2}u'-3x^{2}u'=3x^{2}u'
$$

Step 6. Write the surviving equation and divide by $x^{3}$.

$$
x^{3}u''+3x^{2}u'=0 \quad\text{becomes}\quad u''+\frac{3}{x}u'=0
$$

Step 7. Put $w=u'$, giving a first-order linear equation.

$$
\frac{dw}{dx}+\frac{3}{x}w=0
$$

Step 8. Separate and integrate.

$$
\frac{1}{w}\frac{dw}{dx}=-\frac{3}{x}, \qquad \ln|w|=-3\ln x+\text{constant}, \qquad w=C_{2}x^{-3}
$$

Step 9. Integrate to obtain $u$.

$$
u=C_{1}-\frac{C_{2}}{2}x^{-2}
$$

Step 10. Multiply by $y_{1}=x^{3}$.

$$
y=C_{1}x^{3}-\frac{C_{2}}{2}x
$$

Step 11. Rename the constants and state the answer.

$$
y=Ax^{3}+\frac{B}{x}
$$

Step 12. Check the second solution $y=\frac{1}{x}$. Its derivatives are $-\frac{1}{x^{2}}$ and $\frac{2}{x^{3}}$, so the left side is

$$
\frac{2}{x^{3}}-\frac{1}{x}\left(-\frac{1}{x^{2}}\right)-\frac{3}{x^{2}}\cdot\frac{1}{x}=\frac{2}{x^{3}}+\frac{1}{x^{3}}-\frac{3}{x^{3}}=0 ,
$$

and the answer is confirmed. The powers $3$ and $-1$ also match the roots $m=3$, $m=-1$ of the associated indicial equation $m(m-1)-m-3=0$, which is the expected outcome for an equation of Euler type.

## 5. Mathematical Extensions, Limits, and Common Errors

### 5.1 What the methods can and cannot deliver

The three devices are unconditional in the sense that the transformed equations they produce are always correct, but they are not unconditional in the sense that the transformed equations are always solvable in elementary terms. A change of independent variable produces a correct new equation even when that equation is just as hard as the old one. The normal form always exists, but its coefficient $S$ is usually not constant, and when $S$ is a function such as $\frac{1}{x}$ or $x^{2}$ the normal form is no easier than the original equation. Exactness is a genuine shortcut but holds only for the special coefficient pairs satisfying $P'=Q$.

An instructive failure makes the point. For the equation of Section 4.3 the normal form has

$$
S=4x^{2}-\frac{3}{4x^{2}},
$$

which is not constant, so removing the first derivative there leads nowhere; the change of independent variable $z=x^{2}$ solves the same equation at once. Conversely, for the equation of Section 4.7 the clean-case test fails, because with $P=-4x$ and $Q=4x^{2}-3$ one finds $Q'+2PQ=8x-8x\left(4x^{2}-3\right)$, which is not zero, while the normal form has $S=-1$ and solves the equation immediately. The two methods are complementary, and the diagnostic table of Section 2.6 exists precisely to decide between them before any algebra is committed to paper.

A third limitation concerns elementary integrability. Even when the normal form has constant coefficients, the particular integral may require an integral that cannot be expressed in elementary functions, and even when reduction of order succeeds in principle, the quadrature $\int e^{-\int P\,dx}y_{1}^{-2}\,dx$ may be impossible in closed form. In that situation the correct answer is the integral itself; a solution written as a definite integral with variable upper limit is a complete solution of an initial value problem.

### 5.2 The interval, the sign condition, and the multiplier

Three hypotheses are easy to overlook and each has a visible consequence.

The interval hypothesis matters because the standard form involves division by $a_{0}(x)$. At a zero of $a_{0}$ the equation is singular, solutions may fail to extend across the point, and the general solution may take different forms on the two sides. The Euler example of Section 4.6 is typical: the formula containing $\ln x$ is valid on $x>0$, the formula containing $\ln|x|$ on $x<0$, and no single elementary formula covers both half-lines.

The sign condition $Q>0$ matters because the change of variable $z=\int\sqrt{Q}\,dx$ requires a real square root. When $Q<0$ on the whole interval, one uses $z=\int\sqrt{-Q}\,dx$, which gives $Q_{1}=-1$; the transformed equation is then $\frac{d^{2}Y}{dz^{2}}+P_{1}\frac{dY}{dz}-Y=R_{1}$, still with constant coefficients when $P_{1}$ is constant. What is not permitted is to ignore the sign and take a square root of a negative quantity, or to work on an interval on which $Q$ changes sign, where no single real $z$ works.

The multiplier $u$ is never zero, which is why multiplying and dividing by it is legitimate. That fact is worth stating in an answer, because it is exactly the hypothesis that makes Theorem 2 an equivalence rather than a one-way implication.

### 5.3 Extensions that follow from the same algebra

The normal form is the natural starting point for the qualitative theory of second-order equations. In the form $v''+Sv=0$ the coefficient $S$ alone decides whether solutions oscillate: on an interval where $S>0$ the solutions behave like sines and cosines and have infinitely many zeros, while where $S<0$ they behave like real exponentials and have at most one zero. Because the substitution $y=uv$ multiplies by a factor that never vanishes, the zeros of $y$ are exactly the zeros of $v$, so the oscillation of the original equation is read off from $S$.

The same substitution produces the Sturm comparison and Sturm separation theorems, and it underlies the Liouville transformation used in the theory of orthogonal polynomials. Closer to the present course, the exactness condition $P'=Q$ is the two-sided version of the observation that a first-order linear equation $y'+Py=R$ can always be integrated after multiplication by $e^{\int P\,dx}$: multiplying the second-order equation by that same factor brings it to the self-adjoint form

$$
\frac{d}{dx}\left(e^{\int P\,dx}\frac{dy}{dx}\right)+Qe^{\int P\,dx}y=Re^{\int P\,dx},
$$

in which the second and first derivative terms have been combined into a single derivative. That form is not the same as exactness, since it is available for every $P$, but it is derived by the same product-rule reasoning and is the form in which second-order equations are usually studied beyond this course.

A final extension concerns the number of solutions obtainable from one. Reduction of order shows that a single non-zero solution of a homogeneous second-order equation determines the general solution, because the second solution is a quadrature away. This is a striking economy, and it fails for third-order equations: one solution of a third-order equation still leaves a second-order equation to solve, and the reduction produces no closed formula without further information.

### 5.4 Common errors and how to avoid them

- **Applying a formula to a non-standard form.** Every formula of Section 2 assumes the coefficient of the second derivative is one. Dividing by $a_{0}$ first is not optional.
- **Forgetting to convert the transformed coefficients back to $z$.** Theorem 1 gives $P_{1}$, $Q_{1}$, $R_{1}$ as functions of $x$; the transformed equation is only useful once they are functions of $z$.
- **Using $\frac{dz}{dx}$ where $\left(\frac{dz}{dx}\right)^{2}$ is required.** The factor $Q_{1}=Q/(z')^{2}$ is squared; omitting the square produces coefficients off by a factor of $Q$.
- **Differentiating $y=Y(z)$ only once.** The second derivative needs the product rule applied to $\frac{dY}{dz}\cdot\frac{dz}{dx}$, which produces the extra term $\frac{dY}{dz}\frac{d^{2}z}{dx^{2}}$; dropping it is the commonest error in the whole topic.
- **Taking a square root without regard to sign.** If $Q<0$, the substitution is $z=\int\sqrt{-Q}\,dx$ and $Q_{1}=-1$.
- **Reporting $S$ without the $-\frac{1}{2}P'$ term.** The coefficient is $Q-\frac{1}{4}P^{2}-\frac{1}{2}P'$, and the derivative term is the one most often omitted when $P$ is not constant.
- **Computing $T$ as $R$.** The forcing must be divided by $u$; when $u=e^{x^{2}}$ the division is essential and the resulting $T$ is very different from $R$.
- **Choosing $u$ with the wrong sign.** The exponent is $-\frac{1}{2}\int P\,dx$; using $+\frac{1}{2}\int P\,dx$ doubles the first-derivative term instead of removing it.
- **Multiplying and dividing by zero.** The multiplier $u$ never vanishes, but $y_{1}$ in reduction of order may; the hypothesis $y_{1}\neq 0$ on the interval must be stated.
- **Treating exactness as generic.** The condition is $P'=Q$, one identity that usually fails; checking it takes one line and saves a page of futile work.
- **Losing a constant in reduction of order.** Two integrations produce two constants, and they must appear as the constants of the general solution.
- **Verifying by checking one point.** A solution must satisfy the equation identically on the interval; substituting $x=0$ proves nothing about the function.
- **Leaving the answer in $v$ or $Y$.** The question is asked about $y$, so the final display must be in $x$.

### 5.5 A procedure for any question in this topic

1. Put the equation in standard form and state the interval.
2. Compute the three diagnostics $Q'+2PQ$, $S=Q-\frac{1}{4}P^{2}-\frac{1}{2}P'$, and $P'-Q$.
3. If $P'-Q=0$, the equation is exact; integrate once and solve the first-order result.
4. Otherwise, if $Q'+2PQ=0$, use $z=\int\sqrt{Q}\,dx$ and solve the resulting $Y''+Y=R_{1}$.
5. Otherwise, if $S$ is constant, use $u=\exp\left(-\frac{1}{2}\int P\,dx\right)$ and solve $v''+Sv=T$.
6. Otherwise, if a single solution is supplied, use $y=uy_{1}$ and solve the first-order equation for $u'$.
7. Substitute back to the original variable and verify at least one component of the answer in the original equation.
8. Count the constants against the order before finishing.
