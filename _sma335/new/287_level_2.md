## 1. Foundational Concepts, Definitions, and Axioms

### 1.1 The shape of the problem

A first order equation written as

$$
\frac{dy}{dx}=f(x,y)
$$

is solved by finding a function $y$ of $x$. The topic of this note begins with a change of bookkeeping: instead of solving for the slope, the equation is written as a balance between two coefficients attached to the two infinitesimal increments of the plane. That is, the equation is written in the differential form

$$
M(x,y)\,dx+N(x,y)\,dy=0 ,
$$

where $M$ and $N$ are known functions of two variables. The word form is used because the left-hand side is not a derivative and not a function; it is a formal sum of two terms, one carrying $dx$ and one carrying $dy$. Solving the equation means finding a relation between $x$ and $y$ that makes that sum vanish along the curve.

The two notations describe the same objects. Dividing the differential form by $dx$ gives $M+N\frac{dy}{dx}=0$, which is the slope form with $f=-M/N$ on the set where $N\neq 0$. The advantage of the differential form is that it treats the two variables on an equal footing, and that symmetry is exactly what the technique of this note exploits.

### 1.2 Functions of two variables and partial derivatives

A function $F$ of two variables assigns a single number $F(x,y)$ to each ordered pair $(x,y)$ in some region of the plane. The region on which $F$ is defined and differentiable is called its domain.

> **Definition (Partial derivative).** The partial derivative of $F$ with respect to $x$ at the point $(x,y)$ is the ordinary derivative of the one-variable function obtained by freezing $y$ at its given value:

$$
\frac{\partial F}{\partial x}(x,y)=\lim_{h\to 0}\frac{F(x+h,y)-F(x,y)}{h} .
$$

The partial derivative with respect to $y$ is defined in the same way, freezing $x$ instead:

$$
\frac{\partial F}{\partial y}(x,y)=\lim_{k\to 0}\frac{F(x,y+k)-F(x,y)}{k} .
$$

The short notation $F_{x}$ stands for $\frac{\partial F}{\partial x}$ and $F_{y}$ for $\frac{\partial F}{\partial y}$. Both notations appear in every page that follows, and they always mean the same thing. When a coefficient such as $M$ is being differentiated, the same shorthand is used: $M_{y}$ means $\frac{\partial M}{\partial y}$ and $N_{x}$ means $\frac{\partial N}{\partial x}$.

Repeated partial differentiation produces the four second partial derivatives $F_{xx}$, $F_{xy}$, $F_{yx}$ and $F_{yy}$. The two mixed derivatives $F_{xy}$ and $F_{yx}$ are the ones that matter here, because the whole theory of exact equations is built on the fact that they agree.

### 1.3 The total differential

If $x$ changes by a small amount $h$ and $y$ changes by a small amount $k$ simultaneously, the change in $F$ is, to first order in the two increments,

$$
F(x+h,y+k)-F(x,y)\approx F_{x}(x,y)h+F_{y}(x,y)k .
$$

That first order approximation is the reason for the following definition.

> **Definition (Total differential).** Let $F$ be differentiable on a domain $D$. The total differential of $F$ at $(x,y)$ is the expression

$$
dF=\frac{\partial F}{\partial x}\,dx+\frac{\partial F}{\partial y}\,dy .
$$

The total differential is a linear function of the two increments $dx$ and $dy$; its coefficients are the two partial derivatives evaluated at the point. It changes from point to point because the coefficients change from point to point.

Two computations fix the idea. Take $F(x,y)=x^{2}y$. Then $F_{x}=2xy$ and $F_{y}=x^{2}$, so

$$
d\left(x^{2}y\right)=2xy\,dx+x^{2}\,dy .
$$

Take $G(x,y)=xy$, whose partial derivatives are $G_{x}=y$ and $G_{y}=x$, so

$$
d\left(xy\right)=y\,dx+x\,dy .
$$

The second identity is used a dozen times later in the note. Notice how it reads backwards: the combination $y\,dx+x\,dy$ is not merely an expression, it is the total differential of a specific function, namely the product $xy$. Recognising such combinations is the central skill of the topic.

### 1.4 Exact differentials

> **Definition (Exact differential).** The expression $M\,dx+N\,dy$ is an exact differential on a domain $D$ if there exists a differentiable function $F$ on $D$ such that

$$
\frac{\partial F}{\partial x}=M \qquad \text{and} \qquad \frac{\partial F}{\partial y}=N
$$

at every point of $D$. The function $F$ is called a potential function for the form, or a primitive.

When it exists, the potential is far from unique. If $F$ is a potential then so is $F+C$ for any constant $C$, since constants have zero partial derivatives. Adding a function of $y$ alone to $F$ is not allowed, because that would change $F_{x}$ only if it depended on $x$; adding a function of $x$ alone is not allowed either, for the symmetric reason. This flexibility is examined carefully in Section 3.

> **Definition (Exact differential equation).** The equation $M(x,y)\,dx+N(x,y)\,dy=0$ is exact on a domain $D$ if the left-hand side is an exact differential on $D$.

An exact equation therefore carries a hidden structure: there is a function $F$ whose total differential is precisely the left-hand side. Once $F$ is known, the equation reads $dF=0$, and the solution follows at once.

### 1.5 The geometric meaning: level curves of a height function

The clearest way to hold the whole topic in mind is to think of $F(x,y)$ as the height of a surface above the plane, so that $F(x,y)=C$ is the contour line at height $C$. Moving along a contour, the height does not change, and therefore the total differential vanishes along that curve. In symbols, if $y=y(x)$ traces the contour $F(x,y)=C$, then differentiating the identity $F(x,y(x))=C$ with respect to $x$ by the chain rule gives

$$
F_{x}+F_{y}\frac{dy}{dx}=0 .
$$

With $F_{x}=M$ and $F_{y}=N$ this becomes

$$
M+N\frac{dy}{dx}=0 ,
$$

which is exactly the differential equation. The two statements

$$
M\,dx+N\,dy=0 \qquad \text{and} \qquad F(x,y)=C
$$

are therefore equivalent: every solution curve of the exact equation is a level curve of the potential, and every level curve of the potential is a solution curve. The constant $C$ labels which contour is being followed, and it is the single arbitrary constant that a first order equation is entitled to.

This picture is also the reason the answer is stated implicitly. An exact equation hands over $F(x,y)=C$ directly, without solving for $y$, and in most cases that implicit form is the final answer because isolating $y$ is either impossible or unhelpful.

### 1.6 Domains and regularity hypotheses

Every statement in this note assumes that the coefficients $M$ and $N$ possess continuous first partial derivatives on a domain $D$ that is a rectangle, or more generally a region with no holes. Continuity of $M_{y}$ and $N_{x}$ is needed so that the mixed second partial derivatives of a potential may be interchanged, and the absence of holes is needed so that a local potential can be extended to a global one.

The topological hypothesis is not a decoration. On the punctured plane, obtained by deleting the origin from the plane, the form

$$
\frac{x\,dy-y\,dx}{x^{2}+y^{2}}
$$

has coefficients whose cross partial derivatives agree everywhere on the punctured plane, yet no single-valued potential exists there; the natural candidate is the angle $\arctan\left(\frac{y}{x}\right)$, which can only be defined continuously on a plane cut along a ray. Section 5 returns to this point, because it is the standard counterexample to the naive reading of the criterion.

### 1.7 Integrating factors

Most differential forms are not exact. The next idea is to repair a non-exact form by multiplication.

> **Definition (Integrating factor).** A function $\mu(x,y)$, not identically zero on the domain, is an integrating factor for $M\,dx+N\,dy=0$ if the form

$$
\mu M\,dx+\mu N\,dy
$$

is exact on that domain. Equivalently, $\mu$ is an integrating factor if there exists a function $F$ with

$$
\frac{\partial F}{\partial x}=\mu M \qquad \text{and} \qquad \frac{\partial F}{\partial y}=\mu N .
$$

Multiplying an equation by a function changes the equation, so it may appear that the solution set has been altered. It has not. If $\mu$ is finite and non-zero on a region, then $\mu(M\,dx+N\,dy)=0$ at a point of that region exactly when $M\,dx+N\,dy=0$ at that point, so the two equations have the same solution curves there. The only losses occur at points where $\mu$ is zero or infinite, and those points must be examined separately.

The search for an integrating factor is in general harder than solving the original equation, because the condition on $\mu$ is itself a first order partial differential equation,

$$
\mu_{y}M+\mu M_{y}=\mu_{x}N+\mu N_{x} .
$$

The practical content of this topic is that for two important classes the search can be reduced to a single integration in one variable, and that for a third class the factor can be written down by inspection from the homogeneity of the coefficients. Those three reductions are proved in Section 3 and applied in Section 4.

### 1.8 A dictionary of the symbols

Before the theorems, the vocabulary of the note is collected in one place. The letter $x$ denotes the first independent variable and $y$ the second; the pair $(x,y)$ is a point of the plane. The function $M(x,y)$ is the coefficient of $dx$ and the function $N(x,y)$ is the coefficient of $dy$. The symbol $F(x,y)$, or occasionally $\Phi(x,y)$, denotes the unknown potential function whose existence is the whole question. The letters $\mu$ and sometimes $\varphi$ denote an integrating factor. A subscript denotes partial differentiation, so $M_{y}$ is the partial derivative of $M$ with respect to $y$, computed by treating $x$ as a constant, and $N_{x}$ is the partial derivative of $N$ with respect to $x$, computed by treating $y$ as a constant. The constant $C$ denotes the arbitrary constant of the solution family.

## 2. Theorems, Lemmas, and Analytical Properties

### 2.1 Equality of mixed partial derivatives

> **Lemma (Symmetry of second partial derivatives).** Let $F$ be defined on an open set containing the point $(x,y)$. If $F_{xy}$ and $F_{yx}$ both exist and are continuous in a neighbourhood of $(x,y)$, then

$$
F_{xy}(x,y)=F_{yx}(x,y) .
$$

The result is often called Clairaut's theorem or Schwarz's theorem. Its content is that, for a sufficiently smooth function, the order in which the two differentiations are performed is irrelevant. Every function met in this course satisfies the hypothesis, since it is built from polynomials, exponentials, logarithms and trigonometric functions composed with smooth expressions.

The lemma is the engine of the necessity half of the exactness criterion. If a potential exists at all, the two cross partial derivatives of the coefficients must agree, because both of them are the same mixed second derivative of the potential written in different orders. There is no way around this: exactness forces the equality.

### 2.2 The exactness criterion

> **Theorem (Necessary and sufficient condition for exactness).** Let $M$, $N$, $M_{y}$ and $N_{x}$ be continuous functions of $(x,y)$ on a rectangle $D$. Then

$$
M\,dx+N\,dy=0
$$

is exact on $D$ if and only if

$$
\frac{\partial M}{\partial y}=\frac{\partial N}{\partial x}
$$

at every point of $D$.

The theorem has two halves that are proved by entirely different arguments. Necessity is a differentiation argument and fits in five lines. Sufficiency is a construction: the equality of the cross partials is used to build the potential explicitly, and the construction is what makes the criterion usable rather than merely descriptive.

The hypotheses matter in two ways. Continuity of the four functions guarantees that the mixed derivative lemma applies in the necessity direction and that the fundamental theorem of calculus applies in the sufficiency direction. The rectangular shape of $D$ guarantees that the integrals in the construction stay inside the domain, so that no path has to leave the region.

> **Corollary (Solution of an exact equation).** If the criterion holds on $D$, there is a potential $F$ on $D$, and the solution of the equation is

$$
F(x,y)=C ,
$$

where $C$ is an arbitrary constant.

The corollary is stated separately because students routinely prove exactness and then stop, as though the label exact were the answer. The label is a licence to integrate, not an answer.

### 2.3 The consistency lemma behind the two-step method

Suppose the equation is exact and $F$ is a potential. Then

$$
F(x,y)=\int M(x,y)\,dx+\varphi(y) ,
$$

where the integral is taken with respect to $x$ alone, treating $y$ as a constant, and where $\varphi$ is the arbitrary function of $y$ that plays the role of the constant of integration.

> **Lemma (The remainder is a function of $y$ alone).** If $M_{y}=N_{x}$ on $D$ and $F$ is defined by the integral above, then the quantity

$$
N(x,y)-\frac{\partial}{\partial y}\int M(x,y)\,dx
$$

is independent of $x$.

The lemma is the reason the two-step method terminates. After integrating $M$ with respect to $x$, the partial derivative $F_{y}$ is computed and set equal to $N$. The equation obtained is

$$
\frac{\partial}{\partial y}\int M(x,y)\,dx+\varphi'(y)=N(x,y) ,
$$

and the lemma guarantees that everything except $\varphi'(y)$ cancels, leaving an equation in $y$ alone that can be integrated. If a proposed solution leaves an $x$ in the equation for $\varphi'(y)$, then either the equation was not exact or the integration of $M$ was performed incorrectly. Section 3.3 supplies the proof.

### 2.4 The two classical tests for an integrating factor of one variable

> **Theorem (Integrating factor depending on $x$ alone).** Suppose $N\neq 0$ on $D$ and the ratio

$$
\frac{M_{y}-N_{x}}{N}
$$

is a function of $x$ alone, say $f(x)$. Then

$$
\mu(x)=\exp\left(\int f(x)\,dx\right)
$$

is an integrating factor for $M\,dx+N\,dy=0$ on $D$.

> **Theorem (Integrating factor depending on $y$ alone).** Suppose $M\neq 0$ on $D$ and the ratio

$$
\frac{N_{x}-M_{y}}{M}
$$

is a function of $y$ alone, say $g(y)$. Then

$$
\mu(y)=\exp\left(\int g(y)\,dy\right)
$$

is an integrating factor for $M\,dx+N\,dy=0$ on $D$.

The two theorems are deliberately asymmetric in appearance and completely symmetric in content. In each case the numerator is the cross-partial difference, and the denominator is the coefficient that would be differentiated with respect to the other variable. The first test divides by $N$ and produces a function of $x$; the second divides by $M$ and produces a function of $y$. Both produce a factor obtained by exponentiating one integral.

The tests are sufficient, not necessary. When the first ratio depends on both variables, an integrating factor may still exist; it simply does not depend on $x$ alone. Saying that the test fails is a statement about the shape of the factor, never a statement that no factor exists. This distinction is the source of a great many lost marks.

The hypotheses $N\neq 0$ and $M\neq 0$ are not cosmetic. They are exactly the conditions under which the divisions defining the ratios make sense, and they must be recorded whenever the theorems are applied. On a region where $N$ vanishes the first ratio is undefined and the test cannot be run at all.

### 2.5 Homogeneous equations and the factor built from $Mx+Ny$

> **Definition (Homogeneous function).** A function $f(x,y)$ is homogeneous of degree $n$ if

$$
f(tx,ty)=t^{n}f(x,y)
$$

for every $t>0$ and every point of the domain.

> **Theorem (Integrating factor for a homogeneous equation).** Let $M$ and $N$ be homogeneous of the same degree $n$ and suppose $Mx+Ny$ is not identically zero. Then

$$
\mu=\frac{1}{Mx+Ny}
$$

is an integrating factor for $M\,dx+N\,dy=0$.

The proof uses Euler's theorem on homogeneous functions, which states that a homogeneous function $f$ of degree $n$ satisfies

$$
x f_{x}+y f_{y}=n f .
$$

Applied to $M$ and to $N$, Euler's relation converts the algebra of the exactness test into a cancellation. The verification is carried out in full in Section 3.6, because the two denominators that appear there are the usual place where errors creep in.

The factor produced by this theorem is not usually the simplest one. For the equation with $M=x^{2}-y^{2}$ and $N=2xy$, the theorem gives $\mu=1/\left(x\left(x^{2}+y^{2}\right)\right)$, while the test for a factor depending on $x$ gives $\mu=1/x^{2}$. Both are correct, and both lead to the same solution family. Section 4 exhibits this coincidence explicitly, since it is the most instructive illustration of the non-uniqueness recorded next.

### 2.6 Integrating factors are never unique

> **Lemma (Multiplication of an integrating factor by a function of the potential).** If $\mu$ is an integrating factor with potential $F$, and if $H$ is any differentiable function of one variable with $H'(F)\neq 0$, then $\mu H'(F)$ is also an integrating factor, with potential $H(F)$.

The lemma follows by the chain rule. From $F_{x}=\mu M$ and $F_{y}=\mu N$,

$$
\frac{\partial}{\partial x}H(F)=H'(F)F_{x}=H'(F)\mu M , \qquad \frac{\partial}{\partial y}H(F)=H'(F)F_{y}=H'(F)\mu N ,
$$

so the new form has the potential $H(F)$. Two consequences follow. First, any question that asks for the integrating factor without further specification has infinitely many correct answers, so an answer must be checked by verifying the exactness condition rather than by comparison with a printed key. Second, the solution family is unaffected: the level curves of $H(F)$ are the same curves as the level curves of $F$, merely relabelled.

### 2.7 The standard differentials and their integrating factors

A short list of exact differentials, memorised, turns a large class of problems into pattern recognition. The table records the differential form, an integrating factor for it, a potential, and the identity that justifies the entry.

| Differential form | Integrating factor | Potential | Identity |
|---|---|---|---|
| $y\,dx+x\,dy$ | $1$ | $xy$ | $d(xy)=y\,dx+x\,dy$ |
| $y\,dx+x\,dy$ | $\frac{1}{xy}$ | $\ln(xy)$ | $d\left(\ln(xy)\right)=\frac{y\,dx+x\,dy}{xy}$ |
| $y\,dx+x\,dy$ | $-\frac{1}{x^{2}y^{2}}$ | $\frac{1}{xy}$ | $d\left(\frac{1}{xy}\right)=-\frac{y\,dx+x\,dy}{x^{2}y^{2}}$ |
| $x\,dy-y\,dx$ | $\frac{1}{x^{2}}$ | $\frac{y}{x}$ | $d\left(\frac{y}{x}\right)=\frac{x\,dy-y\,dx}{x^{2}}$ |
| $y\,dx-x\,dy$ | $\frac{1}{y^{2}}$ | $\frac{x}{y}$ | $d\left(\frac{x}{y}\right)=\frac{y\,dx-x\,dy}{y^{2}}$ |
| $x\,dy-y\,dx$ | $\frac{1}{x^{2}+y^{2}}$ | $\arctan\left(\frac{y}{x}\right)$ | $d\left(\arctan\frac{y}{x}\right)=\frac{x\,dy-y\,dx}{x^{2}+y^{2}}$ |
| $x\,dy-y\,dx$ | $\frac{1}{xy}$ | $\ln\left(\frac{y}{x}\right)$ | $d\left(\ln\frac{y}{x}\right)=\frac{x\,dy-y\,dx}{xy}$ |
| $x\,dx+y\,dy$ | $1$ | $\frac{1}{2}\left(x^{2}+y^{2}\right)$ | $d\left(\frac{x^{2}+y^{2}}{2}\right)=x\,dx+y\,dy$ |
| $x\,dx+y\,dy$ | $\frac{1}{x^{2}+y^{2}}$ | $\frac{1}{2}\ln\left(x^{2}+y^{2}\right)$ | $d\left(\ln\sqrt{x^{2}+y^{2}}\right)=\frac{x\,dx+y\,dy}{x^{2}+y^{2}}$ |
| $x\,dy+y\,dx$ | $1$ | $xy$ | $d(xy)=x\,dy+y\,dx$ |

The table is short enough to memorise and rich enough to solve most textbook problems. Its structure is worth naming. The first three rows concern the same differential $y\,dx+x\,dy$ and differ only in the price paid to make it exact; multiplying by $1$ costs nothing, multiplying by $1/(xy)$ converts the potential from $xy$ to $\ln(xy)$, and multiplying by $-1/(x^{2}y^{2})$ converts it to $1/(xy)$. The next four rows concern $x\,dy-y\,dx$, the antisymmetric companion of the product differential, and each of its four standard factors produces one of the four most useful combinations in the subject: the ratio $y/x$, the reciprocal ratio $x/y$, the polar angle, and the logarithm of the ratio. The last three rows concern the radial differential $x\,dx+y\,dy$.

Two remarks prevent misapplication. First, the entries are statements about the combination as a whole, not about the individual terms, so a form must be rearranged into the listed shape before a factor is read off. Second, each entry must be used with its own validity conditions: the logarithmic potentials require positive arguments, and the arctangent potential requires $x\neq 0$.

## 3. Formal Proofs, Derivations, and Methods

### 3.1 Proof of necessity

Assume that $M\,dx+N\,dy$ is exact on the rectangle $D$. By definition there is a function $F$ on $D$ with

$$
F_{x}=M \qquad \text{and} \qquad F_{y}=N .
$$

Differentiate the first identity with respect to $y$ and the second with respect to $x$. This is legitimate because $M_{y}$ and $N_{x}$ are assumed continuous, so the mixed partials of $F$ exist and are continuous. The two results are

$$
M_{y}=\frac{\partial^{2}F}{\partial y\,\partial x} \qquad \text{and} \qquad N_{x}=\frac{\partial^{2}F}{\partial x\,\partial y} .
$$

By the symmetry lemma of Section 2.1 the two mixed partials are equal, hence

$$
M_{y}=N_{x} .
$$

That is the whole of the necessity direction. It says that the equality is a fingerprint left by the potential: if a potential exists, its two mixed partials are forced to agree, and those mixed partials are precisely the cross partials of the coefficients.

### 3.2 Proof of sufficiency: constructing the potential

Assume now that $M_{y}=N_{x}$ on the rectangle $D$, and fix a base point $(x_{0},y_{0})$ in $D$. Define

$$
F(x,y)=\int_{x_{0}}^{x}M(t,y)\,dt+\int_{y_{0}}^{y}N(x_{0},s)\,ds .
$$

The first integral is taken along a horizontal segment at fixed height $y$, and the second along a vertical segment at the fixed abscissa $x_{0}$. Both segments lie in $D$ because $D$ is a rectangle, which is exactly where the rectangular hypothesis is used.

Step 1. Differentiate with respect to $x$. The second integral does not involve $x$, so it contributes nothing, and the fundamental theorem of calculus applied to the first integral gives

$$
F_{x}=M(x,y) .
$$

Step 2. Differentiate with respect to $y$. Both integrals must now be differentiated. The first integration limit does not depend on $y$, only the integrand does, and the second integral is differentiated by the fundamental theorem. Hence

$$
F_{y}=\int_{x_{0}}^{x}M_{y}(t,y)\,dt+N(x_{0},y) .
$$

Step 3. Replace $M_{y}$ by $N_{x}$, which the hypothesis permits.

$$
F_{y}=\int_{x_{0}}^{x}N_{x}(t,y)\,dt+N(x_{0},y)
$$

Step 4. Evaluate the integral of a derivative. The integrand is the $t$-derivative of $N(t,y)$ at fixed $y$, so the fundamental theorem of calculus gives

$$
\int_{x_{0}}^{x}N_{x}(t,y)\,dt=N(x,y)-N(x_{0},y) .
$$

Step 5. Add and simplify.

$$
F_{y}=N(x,y)-N(x_{0},y)+N(x_{0},y)=N(x,y)
$$

Steps 1 and 5 together show that $F_{x}=M$ and $F_{y}=N$, so $F$ is a potential and the form is exact. The construction is explicit, so the sufficiency direction is constructive rather than merely existential.

### 3.3 The two-step method produces the same construction

The method of Section 3.4 integrates $M$ with respect to $x$ and then determines an arbitrary function of $y$. It is worth seeing that this is the same potential as the one just constructed.

Let

$$
F(x,y)=\int M(x,y)\,dx+\varphi(y) ,
$$

where the indefinite integral is taken at fixed $y$. Differentiating with respect to $y$ and imposing $F_{y}=N$ gives

$$
\int M_{y}(x,y)\,dx+\varphi'(y)=N(x,y) .
$$

If $M_{y}=N_{x}$ then $M_{y}$ is the $x$-derivative of $N$, so the integral on the left is $N$ plus a function of $y$ alone:

$$
\int M_{y}(x,y)\,dx=N(x,y)+\psi(y) .
$$

Substituting this into the previous line produces $\psi(y)+\varphi'(y)=0$, so $\varphi'(y)=-\psi(y)$ depends on $y$ only, which is the content of the consistency lemma. The two-step method therefore terminates for every exact equation, and the role of the lemma is to certify that the left-over term cannot involve $x$.

### 3.4 The method for solving an exact equation

The method has four steps, and the fourth is the one that students omit.

1. Write the equation in the form $M\,dx+N\,dy=0$ and compute $M_{y}$ and $N_{x}$. If they are equal on the domain, the equation is exact and the remaining steps are justified; if they are not equal, stop and look for an integrating factor.
2. Integrate $M$ with respect to $x$ at fixed $y$, adding an arbitrary function $\varphi(y)$ in place of a constant of integration.
3. Differentiate the result with respect to $y$, set it equal to $N$, and solve the resulting equation for $\varphi'(y)$. The equation must reduce to a statement about $y$ alone.
4. Integrate $\varphi'(y)$ to obtain $\varphi(y)$, substitute back, and write the answer as $F(x,y)=C$. No constant of integration is needed for $\varphi$, because the constant of the final answer absorbs it.

Two checks complete the work. The first is to differentiate the claimed $F$ with respect to $x$ and to $y$ and confirm that the results are $M$ and $N$. The second is to differentiate the implicit solution $F(x,y)=C$ with respect to $x$ and confirm that the resulting slope agrees with $-M/N$.

### 3.5 Derivation of the test for a factor depending on $x$ alone

Let $\mu=\mu(x)$ and require $\mu M\,dx+\mu N\,dy$ to be exact. By the criterion,

$$
\frac{\partial}{\partial y}\left(\mu M\right)=\frac{\partial}{\partial x}\left(\mu N\right) .
$$

Expand both sides by the product rule. Since $\mu$ depends on $x$ alone, $\mu_{y}=0$, and $\mu_{x}$ is the ordinary derivative $\mu'$.

$$
\mu M_{y}=\mu' N+\mu N_{x}
$$

Collect the terms containing $\mu$ and the terms containing $\mu'$.

$$
\mu\left(M_{y}-N_{x}\right)=\mu' N
$$

Divide by $\mu N$, which is legitimate on a region where $\mu\neq 0$ and $N\neq 0$.

$$
\frac{\mu'}{\mu}=\frac{M_{y}-N_{x}}{N}
$$

The left side is a function of $x$ alone because $\mu$ depends on $x$ alone. Hence the right side must be a function of $x$ alone, which is the hypothesis of the test; and conversely, when the right side is a function of $x$ alone, the ordinary differential equation for $\mu$ can be solved by separating variables. Integrating both sides with respect to $x$,

$$
\ln\mu=\int\frac{M_{y}-N_{x}}{N}\,dx ,
$$

and exponentiating gives

$$
\mu(x)=\exp\left(\int\frac{M_{y}-N_{x}}{N}\,dx\right) .
$$

The derivation shows exactly where the hypothesis enters: if the ratio depended on $y$, the equation for $\mu$ would be inconsistent with the assumption that $\mu$ is a function of $x$ alone.

### 3.6 Derivation of the test for a factor depending on $y$ alone

Let $\mu=\mu(y)$. Now $\mu_{x}=0$ and $\mu_{y}=\mu'$, and the exactness condition reads

$$
\mu' M+\mu M_{y}=\mu N_{x} .
$$

Collecting terms,

$$
\mu' M=\mu\left(N_{x}-M_{y}\right) ,
$$

and dividing by $\mu M$ gives

$$
\frac{\mu'}{\mu}=\frac{N_{x}-M_{y}}{M} .
$$

If the right side is a function $g(y)$ of $y$ alone, then separating variables and integrating with respect to $y$ produces

$$
\mu(y)=\exp\left(\int\frac{N_{x}-M_{y}}{M}\,dy\right) .
$$

Comparing the two tests, the second is the first with the roles of $x$ and $y$ exchanged and the sign of the cross-partial difference reversed. That reversal is why the second test is so often mis-remembered. A reliable way to avoid the error is to derive the ratio from the equation $\mu\left(M_{y}-N_{x}\right)=\mu'N$ in the $x$ case and from $\mu\left(N_{x}-M_{y}\right)=\mu'M$ in the $y$ case, rather than to memorise two fractions.

### 3.7 Verification of the homogeneous factor

Let $M$ and $N$ be homogeneous of degree $n$, and put $D=Mx+Ny$ and $\mu=1/D$. Since $\mu$ is the reciprocal of $D$,

$$
\mu_{x}=-\frac{D_{x}}{D^{2}}, \qquad \mu_{y}=-\frac{D_{y}}{D^{2}} ,
$$

where

$$
D_{x}=M+xM_{x}+yN_{x}, \qquad D_{y}=xM_{y}+N+yN_{y} .
$$

The exactness condition for $\mu M$ and $\mu N$ is

$$
\mu_{y}M+\mu M_{y}=\mu_{x}N+\mu N_{x} .
$$

Multiply through by $D^{2}$ and substitute. The left side becomes $-M D_{y}+D M_{y}$, and the right side becomes $-N D_{x}+D N_{x}$, so the condition to be proved is

$$
D\left(M_{y}-N_{x}\right)-M D_{y}+N D_{x}=0 .
$$

Insert the expressions for $D$, $D_{x}$ and $D_{y}$.

$$
\left(Mx+Ny\right)\left(M_{y}-N_{x}\right)-M\left(xM_{y}+N+yN_{y}\right)+N\left(M+xM_{x}+yN_{x}\right)
$$

Expand the first product and cancel the terms that appear with both signs. The products $MN$ and $-MN$ cancel, and the products $xMM_{y}$ and $-xMM_{y}$ cancel.

$$
-xM N_{x}+yN M_{y}-yM N_{y}+xN M_{x}
$$

Group the four surviving terms by the variable that multiplies them.

$$
x\left(N M_{x}-M N_{x}\right)+y\left(N M_{y}-M N_{y}\right)
$$

Now apply Euler's theorem. Homogeneity of $M$ of degree $n$ gives $xM_{x}+yM_{y}=nM$, and homogeneity of $N$ of the same degree gives $xN_{x}+yN_{y}=nN$. Multiply the first relation by $N$ and the second by $M$.

$$
xN M_{x}+yN M_{y}=nMN, \qquad xM N_{x}+yM N_{y}=nMN .
$$

Subtracting the second identity from the first cancels $nMN$ and produces

$$
x\left(N M_{x}-M N_{x}\right)+y\left(N M_{y}-M N_{y}\right)=0 ,
$$

which is exactly the expression obtained above. The exactness condition is therefore satisfied, and $1/\left(Mx+Ny\right)$ is an integrating factor.

### 3.8 Verification of the standard differentials

Each row of the table in Section 2.7 is a statement that can be confirmed by differentiating the claimed potential. Four verifications fix the method; the rest are identical in style.

For $F=xy$, the partial derivatives are $F_{x}=y$ and $F_{y}=x$, hence $d(xy)=y\,dx+x\,dy$ and the factor $1$ works for $y\,dx+x\,dy$.

For $F=\ln(xy)=\ln x+\ln y$ on the region $x>0$, $y>0$, the partial derivatives are $F_{x}=1/x$ and $F_{y}=1/y$, hence

$$
d\left(\ln(xy)\right)=\frac{dx}{x}+\frac{dy}{y}=\frac{y\,dx+x\,dy}{xy} ,
$$

which shows that $1/(xy)$ is a factor for the same differential.

For $F=\arctan\left(\frac{y}{x}\right)$ with $x\neq 0$, the chain rule gives

$$
F_{x}=\frac{1}{1+\left(\frac{y}{x}\right)^{2}}\cdot\left(-\frac{y}{x^{2}}\right)=-\frac{y}{x^{2}+y^{2}},
$$

and

$$
F_{y}=\frac{1}{1+\left(\frac{y}{x}\right)^{2}}\cdot\frac{1}{x}=\frac{x}{x^{2}+y^{2}} .
$$

Combining the two,

$$
d\left(\arctan\frac{y}{x}\right)=\frac{-y\,dx+x\,dy}{x^{2}+y^{2}} ,
$$

so $1/\left(x^{2}+y^{2}\right)$ is an integrating factor for $x\,dy-y\,dx$.

For $F=\frac{1}{2}\ln\left(x^{2}+y^{2}\right)$ on the region where $x^{2}+y^{2}>0$, the partial derivatives are $F_{x}=x/\left(x^{2}+y^{2}\right)$ and $F_{y}=y/\left(x^{2}+y^{2}\right)$, hence

$$
d\left(\frac{1}{2}\ln\left(x^{2}+y^{2}\right)\right)=\frac{x\,dx+y\,dy}{x^{2}+y^{2}} ,
$$

which is the last row of the table.

### 3.9 The method of regrouping

When a form can be split into pieces that are already standard differentials, no test is needed. The method is to rearrange, to divide by a common quantity, and to read the answer from the table.

1. Split the form into groups, each of which resembles a row of the table.
2. Divide the whole equation by whatever quantity turns each group into a standard differential, and record the restriction that this quantity is not zero.
3. Replace each group by the differential of its potential.
4. Integrate once in the combined variable and solve for the constant.

The method is legitimate because dividing an equation by a non-vanishing function does not change its solution curves, and because the table entries are identities, not approximations. Section 4.7 applies it to an equation whose integrating factor is $1/\left(x^{2}+y^{2}\right)$ and whose potential is a combination of a logarithm and an arctangent.

## 4. Representative Worked Examples and Solutions

### 4.1 Problem: test exactness and solve

Show that

$$
\left(3x^{2}+4xy\right)dx+\left(2x^{2}+2y\right)dy=0
$$

is exact and solve it.

### 4.2 Solution: apply the criterion, then integrate

Step 1. Read off the coefficients.

$$
M=3x^{2}+4xy, \qquad N=2x^{2}+2y
$$

Step 2. Compute the cross partials. Differentiating $M$ with respect to $y$ treats $x$ as a constant, and differentiating $N$ with respect to $x$ treats $y$ as a constant.

$$
\frac{\partial M}{\partial y}=4x, \qquad \frac{\partial N}{\partial x}=4x
$$

Step 3. Since the two are equal for all $(x,y)$, the equation is exact and a potential exists.

Step 4. Integrate $M$ with respect to $x$ at fixed $y$, adding an arbitrary function of $y$.

$$
F(x,y)=\int\left(3x^{2}+4xy\right)dx=x^{3}+2x^{2}y+\varphi(y)
$$

Step 5. Differentiate with respect to $y$ and set the result equal to $N$.

$$
2x^{2}+\varphi'(y)=2x^{2}+2y
$$

Step 6. Solve for $\varphi'$. The $x$-terms cancel, as the consistency lemma predicts.

$$
\varphi'(y)=2y
$$

Step 7. Integrate with respect to $y$; no constant is required.

$$
\varphi(y)=y^{2}
$$

Step 8. Assemble the potential and state the solution.

$$
F(x,y)=x^{3}+2x^{2}y+y^{2}, \qquad x^{3}+2x^{2}y+y^{2}=C
$$

Step 9. Verify both partial derivatives of the claimed potential.

$$
F_{x}=3x^{2}+4xy=M, \qquad F_{y}=2x^{2}+2y=N
$$

Both agree with the coefficients of the original equation, so the solution is correct.

### 4.3 Problem: solve an exact equation with a product coefficient

Solve

$$
\left(x-xy^{2}\right)dx+\left(8y-x^{2}y\right)dy=0 .
$$

### 4.4 Solution: exactness first, then the two integration steps

Step 1. Identify the coefficients.

$$
M=x-xy^{2}, \qquad N=8y-x^{2}y
$$

Step 2. Compute the cross partials.

$$
\frac{\partial M}{\partial y}=-2xy, \qquad \frac{\partial N}{\partial x}=-2xy
$$

Step 3. The cross partials agree, so the equation is exact.

Step 4. Integrate $M$ with respect to $x$.

$$
F(x,y)=\int\left(x-xy^{2}\right)dx=\frac{x^{2}}{2}-\frac{x^{2}y^{2}}{2}+\varphi(y)
$$

Step 5. Differentiate with respect to $y$ and equate to $N$.

$$
-x^{2}y+\varphi'(y)=-x^{2}y+8y
$$

Step 6. The $x$-terms cancel, leaving an equation in $y$ alone.

$$
\varphi'(y)=8y
$$

Step 7. Integrate.

$$
\varphi(y)=4y^{2}
$$

Step 8. Write the potential and the solution.

$$
F(x,y)=\frac{x^{2}}{2}-\frac{x^{2}y^{2}}{2}+4y^{2}, \qquad x^{2}-x^{2}y^{2}+8y^{2}=C
$$

The second form is obtained by multiplying the equation $F=C$ by $2$ and relabelling the constant.

Step 9. Verify.

$$
F_{x}=x-xy^{2}=M, \qquad F_{y}=-x^{2}y+8y=N
$$

Both partial derivatives match the coefficients, so the implicit solution is confirmed.

### 4.5 Problem: exactness with a cubic term

Solve

$$
\left(3x^{2}y-6x\right)dx+\left(x^{3}+2y\right)dy=0 .
$$

### 4.6 Solution: the same two steps with a mixed cubic

Step 1. Identify the coefficients.

$$
M=3x^{2}y-6x, \qquad N=x^{3}+2y
$$

Step 2. Compute the cross partials.

$$
\frac{\partial M}{\partial y}=3x^{2}, \qquad \frac{\partial N}{\partial x}=3x^{2}
$$

Step 3. The equation is exact.

Step 4. Integrate $M$ with respect to $x$.

$$
F(x,y)=\int\left(3x^{2}y-6x\right)dx=x^{3}y-3x^{2}+\varphi(y)
$$

Step 5. Differentiate with respect to $y$ and equate to $N$.

$$
x^{3}+\varphi'(y)=x^{3}+2y
$$

Step 6. Cancel and solve.

$$
\varphi'(y)=2y, \qquad \varphi(y)=y^{2}
$$

Step 7. State the solution.

$$
x^{3}y-3x^{2}+y^{2}=C
$$

Step 8. Verify.

$$
F_{x}=3x^{2}y-6x=M, \qquad F_{y}=x^{3}+2y=N
$$

Both match, so the answer is correct.

### 4.7 Problem: a non-exact equation with a factor depending on $x$

Solve

$$
\left(4x+3y^{2}\right)dx+2xy\,dy=0 .
$$

### 4.8 Solution: show failure, apply the $x$-test, integrate

Step 1. Identify the coefficients and test exactness.

$$
M=4x+3y^{2}, \qquad N=2xy, \qquad M_{y}=6y, \qquad N_{x}=2y
$$

Step 2. Since $6y\neq 2y$ except on the line $y=0$, the equation is not exact.

Step 3. Form the ratio of the $x$-test.

$$
\frac{M_{y}-N_{x}}{N}=\frac{6y-2y}{2xy}=\frac{4y}{2xy}=\frac{2}{x}
$$

Step 4. The ratio depends on $x$ alone, namely $f(x)=2/x$, so an integrating factor depending on $x$ alone exists.

Step 5. Exponentiate the integral of $f$.

$$
\mu=\exp\left(\int\frac{2}{x}\,dx\right)=\exp\left(2\ln x\right)=x^{2}
$$

Step 6. Multiply the equation through by $x^{2}$ and record the new coefficients.

$$
\left(4x^{3}+3x^{2}y^{2}\right)dx+2x^{3}y\,dy=0
$$

Step 7. Verify that the new equation is exact.

$$
\frac{\partial}{\partial y}\left(4x^{3}+3x^{2}y^{2}\right)=6x^{2}y, \qquad \frac{\partial}{\partial x}\left(2x^{3}y\right)=6x^{2}y
$$

The two agree, so the multiplication has achieved its purpose.

Step 8. Integrate the new coefficient of $dx$ with respect to $x$.

$$
F(x,y)=\int\left(4x^{3}+3x^{2}y^{2}\right)dx=x^{4}+x^{3}y^{2}+\varphi(y)
$$

Step 9. Differentiate with respect to $y$ and equate to the new coefficient of $dy$.

$$
2x^{3}y+\varphi'(y)=2x^{3}y, \qquad \varphi'(y)=0
$$

Step 10. A zero derivative means $\varphi$ is constant, and the constant is absorbed into the answer.

$$
x^{4}+x^{3}y^{2}=C
$$

Step 11. Verify the potential against the multiplied equation.

$$
F_{x}=4x^{3}+3x^{2}y^{2}=\mu M, \qquad F_{y}=2x^{3}y=\mu N
$$

Both agree, and dividing the identity $dF=\mu\left(M\,dx+N\,dy\right)$ by the non-zero factor $x^{2}$ shows that the original equation has the same solution curves.

### 4.9 Problem: a non-exact equation with a factor depending on $y$

Solve

$$
dx+\left(\frac{x}{y}+2\right)dy=0
$$

for $y>0$.

### 4.10 Solution: the second test, then integration

Step 1. Identify the coefficients.

$$
M=1, \qquad N=\frac{x}{y}+2
$$

Step 2. Compute the cross partials.

$$
\frac{\partial M}{\partial y}=0, \qquad \frac{\partial N}{\partial x}=\frac{1}{y}
$$

The equation is not exact.

Step 3. Try the $x$-test first, to show that it fails and that the choice of test is a decision rather than a guess.

$$
\frac{M_{y}-N_{x}}{N}=\frac{-\frac{1}{y}}{\frac{x}{y}+2}=-\frac{1}{x+2y}
$$

Step 4. The ratio depends on both variables, so no integrating factor of the form $\mu(x)$ is produced by this route.

Step 5. Try the $y$-test.

$$
\frac{N_{x}-M_{y}}{M}=\frac{\frac{1}{y}-0}{1}=\frac{1}{y}
$$

Step 6. The ratio depends on $y$ alone, so the factor exists and is obtained by exponentiating its integral.

$$
\mu=\exp\left(\int\frac{1}{y}\,dy\right)=y
$$

Step 7. Multiply through by $y$.

$$
y\,dx+\left(x+2y\right)dy=0
$$

Step 8. Verify exactness of the new equation.

$$
\frac{\partial}{\partial y}\left(y\right)=1, \qquad \frac{\partial}{\partial x}\left(x+2y\right)=1
$$

Both are $1$, so the new equation is exact.

Step 9. Integrate the coefficient of $dx$ with respect to $x$.

$$
F(x,y)=\int y\,dx=xy+\varphi(y)
$$

Step 10. Differentiate with respect to $y$ and equate to the coefficient of $dy$.

$$
x+\varphi'(y)=x+2y, \qquad \varphi'(y)=2y, \qquad \varphi(y)=y^{2}
$$

Step 11. State and verify the solution.

$$
xy+y^{2}=C, \qquad F_{x}=y=\mu M, \qquad F_{y}=x+2y=\mu N
$$

Step 12. Interpret. The original equation is linear when read as an equation for $x$ as a function of $y$, since $\frac{dx}{dy}+\frac{x}{y}=-2$; multiplying by $y$ is exactly the integrating factor used in that method. The two techniques agree, as they must.

### 4.11 Problem: a factor that is exponential in $y$

Solve

$$
dx+2xy\,dy=0 .
$$

### 4.12 Solution: a $y$-test whose integral is $y^{2}$

Step 1. Identify the coefficients and test exactness.

$$
M=1, \qquad N=2xy, \qquad M_{y}=0, \qquad N_{x}=2y
$$

The cross partials differ, so the equation is not exact.

Step 2. Form the ratio of the $y$-test.

$$
\frac{N_{x}-M_{y}}{M}=\frac{2y-0}{1}=2y
$$

Step 3. The ratio depends on $y$ alone, so the factor is the exponential of its integral.

$$
\mu=\exp\left(\int 2y\,dy\right)=e^{y^{2}}
$$

Step 4. Multiply through.

$$
e^{y^{2}}dx+2xye^{y^{2}}dy=0
$$

Step 5. Verify exactness.

$$
\frac{\partial}{\partial y}\left(e^{y^{2}}\right)=2ye^{y^{2}}, \qquad \frac{\partial}{\partial x}\left(2xye^{y^{2}}\right)=2ye^{y^{2}}
$$

Step 6. Integrate the coefficient of $dx$ with respect to $x$.

$$
F(x,y)=xe^{y^{2}}+\varphi(y)
$$

Step 7. Differentiate with respect to $y$ and equate to the coefficient of $dy$.

$$
2xye^{y^{2}}+\varphi'(y)=2xye^{y^{2}}, \qquad \varphi'(y)=0
$$

Step 8. State the solution and verify it twice.

$$
xe^{y^{2}}=C, \qquad F_{x}=e^{y^{2}}=\mu M, \qquad F_{y}=2xye^{y^{2}}=\mu N
$$

Step 9. Cross-check by separation of variables on the original equation. Dividing by $x$ and integrating gives $\ln x=-y^{2}+c$, which is $xe^{y^{2}}=C$ with $C=e^{c}$. The integrating factor has delivered the same family.

### 4.13 Problem: a homogeneous equation solved with $1/\left(Mx+Ny\right)$

Solve

$$
\left(x^{2}-y^{2}\right)dx+2xy\,dy=0
$$

by the homogeneous rule, and compare with the $x$-test.

### 4.14 Solution: Euler's relation, then the two-step method

Step 1. Identify the coefficients and test exactness.

$$
M=x^{2}-y^{2}, \qquad N=2xy, \qquad M_{y}=-2y, \qquad N_{x}=2y
$$

The equation is not exact.

Step 2. Observe that both coefficients are homogeneous of degree two: replacing $x$ by $tx$ and $y$ by $ty$ multiplies each coefficient by $t^{2}$.

Step 3. Compute the denominator of the homogeneous factor.

$$
Mx+Ny=x\left(x^{2}-y^{2}\right)+y\left(2xy\right)=x^{3}-xy^{2}+2xy^{2}=x^{3}+xy^{2}=x\left(x^{2}+y^{2}\right)
$$

Step 4. Write the factor.

$$
\mu=\frac{1}{x\left(x^{2}+y^{2}\right)}
$$

Step 5. Multiply through and verify exactness of the result.

$$
\mu M=\frac{x^{2}-y^{2}}{x\left(x^{2}+y^{2}\right)}, \qquad \mu N=\frac{2xy}{x\left(x^{2}+y^{2}\right)}=\frac{2y}{x^{2}+y^{2}}
$$

Step 6. Compute the two cross partials of the new coefficients. For the first,

$$
\frac{\partial}{\partial y}\left(\frac{x^{2}-y^{2}}{x^{3}+xy^{2}}\right)=\frac{-2y\left(x^{3}+xy^{2}\right)-\left(x^{2}-y^{2}\right)\left(2xy\right)}{\left(x^{3}+xy^{2}\right)^{2}}=\frac{-4x^{3}y}{\left(x^{3}+xy^{2}\right)^{2}}=-\frac{4xy}{\left(x^{2}+y^{2}\right)^{2}} .
$$

For the second,

$$
\frac{\partial}{\partial x}\left(\frac{2y}{x^{2}+y^{2}}\right)=-\frac{4xy}{\left(x^{2}+y^{2}\right)^{2}} .
$$

The two agree, so the factor is genuine.

Step 7. Integrate the coefficient of $dy$ with respect to $y$, which is easier here than integrating the coefficient of $dx$.

$$
F(x,y)=\int\frac{2y}{x^{2}+y^{2}}\,dy=\ln\left(x^{2}+y^{2}\right)+\psi(x)
$$

Step 8. Differentiate with respect to $x$ and equate to the coefficient of $dx$.

$$
\frac{2x}{x^{2}+y^{2}}+\psi'(x)=\frac{x^{2}-y^{2}}{x\left(x^{2}+y^{2}\right)}
$$

Step 9. Solve for $\psi'$ by subtracting the first term.

$$
\psi'(x)=\frac{x^{2}-y^{2}}{x\left(x^{2}+y^{2}\right)}-\frac{2x}{x^{2}+y^{2}}=\frac{x^{2}-y^{2}-2x^{2}}{x\left(x^{2}+y^{2}\right)}=\frac{-x^{2}-y^{2}}{x\left(x^{2}+y^{2}\right)}=-\frac{1}{x}
$$

Step 10. Integrate with respect to $x$.

$$
\psi(x)=-\ln x
$$

Step 11. Assemble the potential and the solution for $x>0$.

$$
F(x,y)=\ln\left(x^{2}+y^{2}\right)-\ln x=\ln\frac{x^{2}+y^{2}}{x}, \qquad x^{2}+y^{2}=Cx
$$

Step 12. Verify. Differentiating the potential,

$$
F_{x}=\frac{2x}{x^{2}+y^{2}}-\frac{1}{x}=\frac{2x^{2}-x^{2}-y^{2}}{x\left(x^{2}+y^{2}\right)}=\frac{x^{2}-y^{2}}{x\left(x^{2}+y^{2}\right)}=\mu M,
$$

and

$$
F_{y}=\frac{2y}{x^{2}+y^{2}}=\mu N .
$$

Step 13. Compare with the $x$-test. The ratio

$$
\frac{M_{y}-N_{x}}{N}=\frac{-2y-2y}{2xy}=-\frac{2}{x}
$$

depends on $x$ alone, so the first theorem gives

$$
\mu=\exp\left(\int-\frac{2}{x}\,dx\right)=x^{-2} .
$$

With this factor the coefficients are $1-y^{2}/x^{2}$ and $2y/x$, and the potential is

$$
\tilde{F}(x,y)=\frac{x^{2}+y^{2}}{x},
$$

whose partials are $1-y^{2}/x^{2}$ and $2y/x$. The two potentials differ by a logarithm, that is $\tilde{F}=\exp(F)$, and by the lemma of Section 2.6 they define the same level curves. The solution family $x^{2}+y^{2}=Cx$ is therefore confirmed by two independent routes.

### 4.15 Problem: solve by regrouping into standard differentials

Solve

$$
\left(x^{2}+y^{2}-y\right)dx+x\,dy=0 .
$$

### 4.16 Solution: recognise $x\,dy-y\,dx$ and divide by $x^{2}+y^{2}$

Step 1. Identify the coefficients and confirm that the equation is not exact.

$$
M=x^{2}+y^{2}-y, \qquad N=x, \qquad M_{y}=2y-1, \qquad N_{x}=1
$$

Since $2y-1\neq 1$ in general, no integrating factor of size one is available.

Step 2. Regroup the form, separating the antisymmetric part $x\,dy-y\,dx$.

$$
\left(x\,dy-y\,dx\right)+\left(x^{2}+y^{2}\right)dx=0
$$

Step 3. Divide the whole equation by $x^{2}+y^{2}$, which is positive away from the origin, and record the restriction.

$$
\frac{x\,dy-y\,dx}{x^{2}+y^{2}}+dx=0, \qquad (x,y)\neq(0,0)
$$

Step 4. Substitute the standard differential from the table.

$$
d\left(\arctan\frac{y}{x}\right)+dx=0
$$

Step 5. Integrate once, since the left side is now a total differential.

$$
\arctan\frac{y}{x}+x=C
$$

Step 6. Solve for $y$ where possible.

$$
y=x\tan\left(C-x\right)
$$

Step 7. Verify by differentiating the explicit form. With $y=x\tan\left(C-x\right)$,

$$
\frac{dy}{dx}=\tan\left(C-x\right)-x\sec^{2}\left(C-x\right)=\frac{y}{x}-x\left(1+\frac{y^{2}}{x^{2}}\right)=\frac{y}{x}-\frac{x^{2}+y^{2}}{x} .
$$

Rearranging gives $x\frac{dy}{dx}=y-x^{2}-y^{2}$, which is precisely the original equation written in slope form.

Step 8. Confirm that the division used is an integrating factor. Multiplying the original coefficients by $1/\left(x^{2}+y^{2}\right)$ produces

$$
\mu M=1-\frac{y}{x^{2}+y^{2}}, \qquad \mu N=\frac{x}{x^{2}+y^{2}} ,
$$

and the cross partials of these two functions are both $\left(y^{2}-x^{2}\right)/\left(x^{2}+y^{2}\right)^{2}$, so the multiplied equation is exact.

### 4.17 Problem: a right-hand side that is not zero

Solve

$$
y\,dx-x\,dy=x^{2}\,dx .
$$

### 4.18 Solution: move everything to one side, then use the ratio differential

Step 1. Rewrite in the standard form with zero on the right.

$$
\left(y-x^{2}\right)dx-x\,dy=0
$$

Step 2. Identify the coefficients and test exactness.

$$
M=y-x^{2}, \qquad N=-x, \qquad M_{y}=1, \qquad N_{x}=-1
$$

The equation is not exact.

Step 3. Apply the $x$-test.

$$
\frac{M_{y}-N_{x}}{N}=\frac{1-\left(-1\right)}{-x}=-\frac{2}{x}
$$

Step 4. Exponentiate the integral.

$$
\mu=\exp\left(\int-\frac{2}{x}\,dx\right)=x^{-2}
$$

Step 5. Multiply through and verify.

$$
\left(\frac{y}{x^{2}}-1\right)dx-\frac{1}{x}\,dy=0, \qquad \frac{\partial}{\partial y}\left(\frac{y}{x^{2}}-1\right)=\frac{1}{x^{2}}=\frac{\partial}{\partial x}\left(-\frac{1}{x}\right)
$$

Step 6. Integrate the coefficient of $dx$ with respect to $x$ at fixed $y$.

$$
F(x,y)=-\frac{y}{x}-x+\varphi(y)
$$

Step 7. Differentiate with respect to $y$ and equate to the coefficient of $dy$.

$$
-\frac{1}{x}+\varphi'(y)=-\frac{1}{x}, \qquad \varphi'(y)=0
$$

Step 8. State the solution.

$$
-\frac{y}{x}-x=C \qquad \text{equivalently} \qquad y=C'x-x^{2}
$$

Step 9. Verify by substitution into the original equation. With $y=C'x-x^{2}$ the derivative is $C'-2x$, so

$$
y-x\frac{dy}{dx}=\left(C'x-x^{2}\right)-x\left(C'-2x\right)=C'x-x^{2}-C'x+2x^{2}=x^{2},
$$

which is the required identity.

Step 10. Note the shortcut. Since $y\,dx-x\,dy=-x^{2}\,d\left(\frac{y}{x}\right)$, the equation divided by $x^{2}$ reads $d\left(\frac{y}{x}\right)=-dx$, and one integration gives $\frac{y}{x}=-x+C$, which is the same family. The regrouping and the formal test agree.

### 4.19 Problem: determine a constant so that the equation is exact

If

$$
\left(x^{2}+3xy\right)dx+\left(Ax^{2}+4y\right)dy=0
$$

is exact, find $A$ and solve the equation.

### 4.20 Solution: impose the criterion, then integrate

Step 1. Identify the coefficients.

$$
M=x^{2}+3xy, \qquad N=Ax^{2}+4y
$$

Step 2. Compute the cross partials, remembering that $A$ is a constant.

$$
\frac{\partial M}{\partial y}=3x, \qquad \frac{\partial N}{\partial x}=2Ax
$$

Step 3. Impose the exactness condition as an identity in $x$.

$$
3x=2Ax \qquad \text{for all } x, \qquad A=\frac{3}{2}
$$

Step 4. Substitute $A$ and integrate $M$ with respect to $x$.

$$
F(x,y)=\int\left(x^{2}+3xy\right)dx=\frac{x^{3}}{3}+\frac{3x^{2}y}{2}+\varphi(y)
$$

Step 5. Differentiate with respect to $y$ and equate to $N$.

$$
\frac{3x^{2}}{2}+\varphi'(y)=\frac{3x^{2}}{2}+4y
$$

Step 6. Cancel and integrate.

$$
\varphi'(y)=4y, \qquad \varphi(y)=2y^{2}
$$

Step 7. Write the solution and clear fractions.

$$
\frac{x^{3}}{3}+\frac{3x^{2}y}{2}+2y^{2}=C, \qquad 2x^{3}+9x^{2}y+12y^{2}=C'
$$

Step 8. Verify the potential.

$$
F_{x}=x^{2}+3xy=M, \qquad F_{y}=\frac{3x^{2}}{2}+4y=Ax^{2}+4y \quad \text{with } A=\frac{3}{2}
$$

Both agree, so the value of $A$ and the solution are both correct.

### 4.21 Problem: an initial value problem

Solve $\left(2xy-3\right)dx+\left(x^{2}+4y\right)dy=0$ subject to $y=2$ when $x=1$.

### 4.22 Solution: general solution first, constant afterwards

Step 1. Identify the coefficients and test exactness.

$$
M=2xy-3, \qquad N=x^{2}+4y, \qquad M_{y}=2x, \qquad N_{x}=2x
$$

The equation is exact.

Step 2. Integrate $M$ with respect to $x$.

$$
F(x,y)=\int\left(2xy-3\right)dx=x^{2}y-3x+\varphi(y)
$$

Step 3. Differentiate with respect to $y$ and equate to $N$.

$$
x^{2}+\varphi'(y)=x^{2}+4y
$$

Step 4. Cancel and integrate.

$$
\varphi'(y)=4y, \qquad \varphi(y)=2y^{2}
$$

Step 5. Write the general solution.

$$
x^{2}y-3x+2y^{2}=C
$$

Step 6. Impose the condition at $(1,2)$.

$$
1\cdot 2-3\cdot 1+2\cdot 4=2-3+8=7
$$

Step 7. State the particular solution.

$$
x^{2}y-3x+2y^{2}=7
$$

Step 8. Verify. The partial derivatives of the left side are $2xy-3$ and $x^{2}+4y$, matching the coefficients of the equation, and the point $(1,2)$ satisfies $2-3+8=7$, so the initial condition is met.

## 5. Mathematical Extensions, Limits, and Common Errors

### 5.1 What the criterion does not say

The criterion is a statement about a rectangle. It asserts that on a region with no holes, agreement of the cross partials is equivalent to the existence of a potential; it does not assert that agreement always produces a potential, and the difference is visible on the punctured plane. The form

$$
\frac{x\,dy-y\,dx}{x^{2}+y^{2}}
$$

has cross partials that agree at every point away from the origin, and its local potentials are the angles $\arctan\left(\frac{y}{x}\right)$ shifted by constants. No single-valued differentiable potential exists on the whole punctured plane, because a closed loop around the origin increases the angle by a full turn. The exactness condition is therefore a local statement whose global validity requires a topological hypothesis, and the hypothesis is invisible in the algebra.

A second limitation is that the criterion tests exactness and nothing else. It says nothing about whether the potential can be written in elementary functions, and nothing about whether the implicit solution $F(x,y)=C$ can be solved for $y$. Many correct answers to examination questions are implicit relations that cannot be rearranged.

### 5.2 Integrating factors that depend on a combination of the variables

The two classical tests are the beginning of a family. If an integrating factor is assumed to be a function of $x+y$ alone, write $u=x+y$ and $\mu=\mu(u)$, so that $\mu_{x}=\mu_{y}=\mu'(u)$. The exactness condition $\mu_{y}M+\mu M_{y}=\mu_{x}N+\mu N_{x}$ becomes

$$
\mu'\left(M-N\right)+\mu\left(M_{y}-N_{x}\right)=0 ,
$$

so a factor of this type exists whenever

$$
\frac{M_{y}-N_{x}}{N-M}
$$

is a function of $x+y$ alone, and it is then the exponential of the integral of that function with respect to $u$.

If instead $\mu$ is assumed to be a function of the product $xy$, write $u=xy$ and $\mu=\mu(u)$, so that $\mu_{x}=y\mu'(u)$ and $\mu_{y}=x\mu'(u)$. The condition becomes

$$
x\mu' M+\mu M_{y}=y\mu' N+\mu N_{x} ,
$$

which rearranges to

$$
\frac{\mu'}{\mu}=\frac{N_{x}-M_{y}}{xM-yN} .
$$

A factor of the form $\mu(xy)$ therefore exists whenever the right-hand side is a function of $xy$ alone. The pattern is general: an assumption about the shape of $\mu$ converts the partial differential equation for $\mu$ into an ordinary one, and the assumption is usable exactly when the resulting coefficient depends on the assumed combination alone. This is the reason the two classical tests are worth memorising and the rest are worth deriving on the spot.

### 5.3 The cost of multiplying by an integrating factor

Multiplying by $\mu$ preserves the solution curves only where $\mu$ is finite and non-zero. Where $\mu$ vanishes, the multiplied equation is satisfied automatically, so points or curves at which $\mu=0$ can enter the solution set although they did not satisfy the original equation. Where $\mu$ blows up, genuine solutions of the original equation can be lost. The classical example is the equation

$$
y\,dx-x\,dy=0 ,
$$

for which the factor $1/x^{2}$ is standard. The resulting solution $y=Cx$ omits the vertical line $x=0$, which solves the original equation in the sense that $dx=0$ there. Similarly, the factor $1/y^{2}$ produces $x=Cy$ and omits the horizontal line $y=0$. The general lesson is that any factor involving a division must be accompanied by a statement of the excluded set, and any question about the complete solution set must consider those exclusions.

A second cost is that the factor is not unique, as Section 2.6 showed. Different correct choices produce different potentials, sometimes looking quite unlike each other, as the logarithm and the rational function of Section 4.14 illustrate. Since the two potentials are related by a function of the potential itself, their level curves coincide and the answers are equivalent.

### 5.4 The same idea in other language

An exact form is what a physicist calls a conservative field written in two dimensions, with $M$ and $N$ playing the roles of the two components of a force field and $F$ playing the role of the potential energy. The condition $M_{y}=N_{x}$ is the vanishing of the curl of a two-dimensional field, and the statement that the work done depends only on the endpoints is the statement that the field has a potential. The solution curves $F=C$ are the curves of constant potential energy, along which a particle subject to the field does no work. This is not a different theory; it is the same identities read in a different vocabulary, and the vocabulary is useful because it explains why exactness is a property worth having.

A second extension is the relation between an integrating factor and an equation that is linear in one variable. When an equation is linear in $x$ as a function of $y$, the integrating factor $y$ of Section 4.9 appears; when it is linear in $y$ as a function of $x$, the factor is an exponential of an integral of a coefficient. The exactness machinery therefore contains the linear theory as a special case, and the two routes to a given answer can be used as mutual checks.

### 5.5 Common errors

- **Confusing $M_{y}$ with $M_{x}$.** The test compares the derivative of the $dx$-coefficient with respect to $y$ against the derivative of the $dy$-coefficient with respect to $x$. Writing $M_{x}=N_{y}$ is a different condition, satisfied by many non-exact equations.
- **Differentiating with the wrong variable held constant.** In computing $M_{y}$, the variable $x$ is treated as a constant. A term such as $3x^{2}y$ differentiates to $3x^{2}$, not to $6xy$.
- **Forgetting the arbitrary function of $y$.** After integrating $M$ with respect to $x$, the constant of integration must be written as a function $\varphi(y)$, because any function of $y$ alone has zero $x$-derivative. Writing a plain constant and then discovering that $N$ cannot be matched is a symptom of this omission.
- **Adding a second constant at the end.** The function $\varphi$ contributes no constant of its own, because the final answer already carries an arbitrary constant $C$.
- **Stopping after proving exactness.** Exactness is a licence to integrate, not a solution. Marks are awarded for the potential and for the constant.
- **Applying a test without checking its denominator.** The ratio $(M_{y}-N_{x})/N$ requires $N\neq 0$, and the ratio $(N_{x}-M_{y})/M$ requires $M\neq 0$. Dividing by a quantity that vanishes somewhere on the domain invalidates the conclusion there.
- **Concluding that no integrating factor exists when a test fails.** A failed test rules out a factor of one particular shape, not every factor.
- **Sign errors in the $y$-test.** The correct numerator is $N_{x}-M_{y}$, which is the negative of the numerator in the $x$-test. Deriving the ratio from the condition $\mu\left(N_{x}-M_{y}\right)=\mu'M$ prevents the error.
- **Using the homogeneous factor when the coefficients have different degrees.** The theorem requires $M$ and $N$ homogeneous of the same degree, and it requires $Mx+Ny$ not to vanish identically.
- **Dividing by an expression without recording the restriction.** Every factor of the form $1/x^{2}$ or $1/\left(x^{2}+y^{2}\right)$ excludes a set of points, and those exclusions belong in the answer.
- **Failing to verify.** Substituting the claimed potential into $F_{x}=M$ and $F_{y}=N$ catches almost every algebraic slip, and it costs two lines.

### 5.6 A reliable procedure

1. Write the equation as $M\,dx+N\,dy=0$ and identify $M$ and $N$ explicitly.
2. Compute $M_{y}$ and $N_{x}$. If they are equal on the domain, proceed to step 6.
3. If they differ, compute both ratios $(M_{y}-N_{x})/N$ and $(N_{x}-M_{y})/M$ and see whether either reduces to a function of one variable. Use the first if it reduces to a function of $x$, the second if it reduces to a function of $y$, and exponentiate the integral of the reduced function.
4. If neither reduces, look at the coefficients for homogeneity of a common degree, and if they are homogeneous use $1/\left(Mx+Ny\right)$.
5. If the coefficients contain the combinations $y\,dx+x\,dy$, $x\,dy-y\,dx$ or $x\,dx+y\,dy$, regroup and divide by the corresponding denominator from the table in Section 2.7.
6. Integrate the coefficient of $dx$ with respect to $x$, adding $\varphi(y)$; differentiate with respect to $y$, equate to the coefficient of $dy$, and integrate $\varphi'$.
7. State the answer as $F(x,y)=C$, impose any initial condition, and verify by differentiating the potential.

The procedure is written in the order that minimises wasted work: exactness is tested before any integrating factor is sought, and the cheapest factor, namely $1$, is tried first. Students who begin by guessing a factor frequently spend a page on an equation that was exact from the start.
