## 1. Foundational Concepts, Definitions, and Axioms

### 1.1 What the examiner is testing

Every question on this topic asks for one of five things, and recognising which one is being asked is worth more than any formula. The five patterns are: decide whether a given form is exact; find the potential and hence the implicit solution; find the value of an unknown constant that makes a form exact; produce an integrating factor and then solve; and solve a form that is a combination of standard differentials. Each pattern has a fixed opening move and a fixed closing move, and the middle is mechanical.

The opening move in every case is to write the equation in the form $M\,dx+N\,dy=0$ and to compute the two cross partial derivatives. The closing move in every case is to differentiate the claimed potential and show that the two partial derivatives reproduce the coefficients. Between those two moves the work is integration, and integration is where marks are lost rather than where ideas are missed.

### 1.2 The differential form

A first order equation may be written as $M(x,y)\,dx+N(x,y)\,dy=0$, where $M$ is the coefficient of $dx$ and $N$ is the coefficient of $dy$. Dividing by $dx$ recovers the slope form $\frac{dy}{dx}=-M/N$, so the two descriptions carry the same information on any region where $N\neq 0$. The differential form is preferred here because it treats the variables symmetrically and because exactness is a property of the pair of coefficients.

The notation $M_{y}$ abbreviates the partial derivative $\frac{\partial M}{\partial y}$, computed with $x$ held constant, and $N_{x}$ abbreviates $\frac{\partial N}{\partial x}$, computed with $y$ held constant. The letters $x_{0}$ and $y_{0}$ denote a chosen base point of the domain, used when a potential is written as a line integral.

### 1.3 The total differential

> **Definition (Total differential).** If $F$ is differentiable on a domain, its total differential is

$$
dF=\frac{\partial F}{\partial x}\,dx+\frac{\partial F}{\partial y}\,dy .
$$

Three instances are used constantly and should be memorised in both directions:

$$
d\left(xy\right)=y\,dx+x\,dy, \qquad d\left(\frac{y}{x}\right)=\frac{x\,dy-y\,dx}{x^{2}}, \qquad d\left(\frac{x^{2}+y^{2}}{2}\right)=x\,dx+y\,dy .
$$

Reading each identity from right to left is the skill being tested: the combination $y\,dx+x\,dy$ is not a random expression, it is the differential of $xy$.

### 1.4 Exact differential and exact equation

> **Definition (Exact differential).** The form $M\,dx+N\,dy$ is exact on a domain $D$ if some differentiable $F$ on $D$ satisfies

$$
\frac{\partial F}{\partial x}=M \qquad \text{and} \qquad \frac{\partial F}{\partial y}=N .
$$

The function $F$ is called a potential function, and the equation $M\,dx+N\,dy=0$ is called exact when its left-hand side is an exact differential.

The geometrical reading is the fastest way to remember what the solution means. If $F$ is the height of a surface, the curves $F(x,y)=C$ are its contours, and moving along a contour changes no height, so $dF=0$ along it. Hence every solution curve of an exact equation is a contour of its potential, and the general solution is $F(x,y)=C$ with $C$ the arbitrary constant that the first order of the equation entitles it to.

### 1.5 Integrating factors

> **Definition (Integrating factor).** A function $\mu(x,y)$, not identically zero, is an integrating factor for $M\,dx+N\,dy=0$ if

$$
\mu M\,dx+\mu N\,dy
$$

is exact on the domain.

Where $\mu$ is finite and non-zero, multiplying by $\mu$ does not change which points satisfy the equation, so the solution curves are unchanged; where $\mu$ vanishes or blows up, solutions may be gained or lost, and those places must be reported. This single sentence accounts for most of the marks awarded for a remark at the end of an integrating-factor question.

### 1.6 The three routes to an integrating factor

There are exactly three routes in the syllabus, and they are tried in a fixed order because each is cheaper than the next.

The first route applies when the ratio $\left(M_{y}-N_{x}\right)/N$ is a function of $x$ alone; the factor is then the exponential of the integral of that function. The second applies when the ratio $\left(N_{x}-M_{y}\right)/M$ is a function of $y$ alone; the factor is again an exponential of an integral. The third applies when $M$ and $N$ are homogeneous of the same degree; the factor is then $1/\left(Mx+Ny\right)$, with no integration required at all.

A fourth route is not a test but a skill: when the form contains a recognisable piece such as $y\,dx+x\,dy$ or $x\,dy-y\,dx$, regrouping and dividing by the matching denominator produces an exact equation directly.

### 1.7 The standard differentials

| Differential form | Integrating factor | Potential | Identity |
|---|---|---|---|
| $y\,dx+x\,dy$ | $1$ | $xy$ | $d(xy)=y\,dx+x\,dy$ |
| $y\,dx+x\,dy$ | $\frac{1}{xy}$ | $\ln(xy)$ | $d\left(\ln(xy)\right)=\frac{y\,dx+x\,dy}{xy}$ |
| $x\,dy-y\,dx$ | $\frac{1}{x^{2}}$ | $\frac{y}{x}$ | $d\left(\frac{y}{x}\right)=\frac{x\,dy-y\,dx}{x^{2}}$ |
| $y\,dx-x\,dy$ | $\frac{1}{y^{2}}$ | $\frac{x}{y}$ | $d\left(\frac{x}{y}\right)=\frac{y\,dx-x\,dy}{y^{2}}$ |
| $x\,dy-y\,dx$ | $\frac{1}{x^{2}+y^{2}}$ | $\arctan\left(\frac{y}{x}\right)$ | $d\left(\arctan\frac{y}{x}\right)=\frac{x\,dy-y\,dx}{x^{2}+y^{2}}$ |
| $x\,dy-y\,dx$ | $\frac{1}{xy}$ | $\ln\left(\frac{y}{x}\right)$ | $d\left(\ln\frac{y}{x}\right)=\frac{x\,dy-y\,dx}{xy}$ |
| $x\,dx+y\,dy$ | $1$ | $\frac{1}{2}\left(x^{2}+y^{2}\right)$ | $d\left(\frac{x^{2}+y^{2}}{2}\right)=x\,dx+y\,dy$ |
| $x\,dx+y\,dy$ | $\frac{1}{x^{2}+y^{2}}$ | $\frac{1}{2}\ln\left(x^{2}+y^{2}\right)$ | $d\left(\ln\sqrt{x^{2}+y^{2}}\right)=\frac{x\,dx+y\,dy}{x^{2}+y^{2}}$ |
| $y\,dx+x\,dy$ | $-\frac{1}{x^{2}y^{2}}$ | $\frac{1}{xy}$ | $d\left(\frac{1}{xy}\right)=-\frac{y\,dx+x\,dy}{x^{2}y^{2}}$ |

The rows are grouped by the differential they concern. The first and last rows and the second row all treat $y\,dx+x\,dy$ and differ only in the potential produced. The four middle rows treat the antisymmetric differential $x\,dy-y\,dx$ and produce the ratio, the reciprocal ratio, the polar angle and the logarithm of the ratio. The two remaining rows treat the radial differential $x\,dx+y\,dy$.

## 2. Theorems, Lemmas, and Analytical Properties

### 2.1 The exactness theorem

> **Theorem (Exactness criterion).** Let $M$, $N$, $\frac{\partial M}{\partial y}$ and $\frac{\partial N}{\partial x}$ be continuous on a rectangle $D$. Then $M\,dx+N\,dy=0$ is exact on $D$ if and only if

$$
\frac{\partial M}{\partial y}=\frac{\partial N}{\partial x}
$$

at every point of $D$. When the condition holds, the solution is $F(x,y)=C$, where $F$ is any potential.

This is the highest-yield result in the topic. A question that says show that the equation is exact is worth two or three marks and is answered entirely by computing the two cross partials and comparing them; a question that says solve the equation is worth six or seven and needs the criterion plus the two integration steps.

The hypothesis that $D$ is a rectangle matters. On a region with a hole the criterion can hold without a single-valued potential existing, the standard example being the angle form on the punctured plane. Exam questions avoid this subtlety, but a remark that the condition is sufficient on a region without holes earns credit in a proof question.

> **Corollary (Solution from a potential).** If the criterion holds on $D$, the general solution of the equation is

$$
F(x,y)=C ,
$$

and it is the only arbitrary constant available, since the equation is of first order.

### 2.2 Symmetry of the mixed partials

> **Lemma (Clairaut and Schwarz).** If $F_{xy}$ and $F_{yx}$ exist and are continuous near a point, they are equal there.

This lemma is the whole of the necessity direction: a potential has both cross partials of the coefficients as its own mixed second derivative, so the two must agree. It is quoted rather than proved in most examinations, but a one-line statement of it is expected inside a proof of the criterion.

### 2.3 The consistency lemma

> **Lemma (The leftover term is a function of $y$).** If $M_{y}=N_{x}$, then

$$
N(x,y)-\frac{\partial}{\partial y}\int M(x,y)\,dx
$$

does not involve $x$.

The lemma is the reason the standard two-step method terminates, and it supplies a diagnostic: if the equation for $\varphi'(y)$ still contains $x$, then either the equation was not exact or the integration with respect to $x$ was performed incorrectly. Examiners reward the observation that all $x$-terms cancel, because it shows the method is understood rather than imitated.

### 2.4 The two one-variable tests

> **Theorem (Factor depending on $x$ alone).** If $N\neq 0$ on $D$ and

$$
\frac{M_{y}-N_{x}}{N}=f(x)
$$

is a function of $x$ alone, then

$$
\mu(x)=\exp\left(\int f(x)\,dx\right)
$$

is an integrating factor for $M\,dx+N\,dy=0$ on $D$.

> **Theorem (Factor depending on $y$ alone).** If $M\neq 0$ on $D$ and

$$
\frac{N_{x}-M_{y}}{M}=g(y)
$$

is a function of $y$ alone, then

$$
\mu(y)=\exp\left(\int g(y)\,dy\right)
$$

is an integrating factor for $M\,dx+N\,dy=0$ on $D$.

Both tests are sufficient and neither is necessary. When a ratio depends on both variables, the corresponding factor does not exist in that shape, but some other factor may well exist. An answer that concludes no integrating factor exists because a single test failed is marked wrong even if the arithmetic is perfect.

### 2.5 The homogeneous factor

> **Theorem (Factor for a homogeneous equation).** If $M$ and $N$ are homogeneous of the same degree and $Mx+Ny$ is not identically zero, then

$$
\mu=\frac{1}{Mx+Ny}
$$

is an integrating factor for $M\,dx+N\,dy=0$.

Homogeneity of degree $n$ means that replacing $x$ by $tx$ and $y$ by $ty$ multiplies the function by $t^{n}$. Euler's relation $xf_{x}+yf_{y}=nf$ for such a function is what makes the verification work. The theorem is worth four to five marks in a question that also asks for the solution, and the safest way to answer is to compute $Mx+Ny$ explicitly, state the factor, and verify the new exactness condition.

### 2.6 Non-uniqueness of the factor

> **Lemma (Scaling by a function of the potential).** If $\mu$ is an integrating factor with potential $F$ and $H$ is differentiable with $H'(F)\neq 0$, then $\mu H'(F)$ is an integrating factor with potential $H(F)$.

Because of this lemma there is no such thing as the integrating factor, and no answer can be checked by comparing it with a printed key. The check is always the exactness condition. A useful corollary is that when two different factors are found by two different routes, both answers are right provided the level curves they produce are the same; if they are not, one of the routes contains an error.

## 3. Formal Proofs, Derivations, and Methods

### 3.1 Proof of necessity

Assume the form is exact, so there is $F$ with $F_{x}=M$ and $F_{y}=N$. Differentiating the first relation with respect to $y$ and the second with respect to $x$ gives

$$
M_{y}=\frac{\partial^{2}F}{\partial y\,\partial x} \qquad \text{and} \qquad N_{x}=\frac{\partial^{2}F}{\partial x\,\partial y} .
$$

By the symmetry lemma the two mixed partials agree, hence $M_{y}=N_{x}$. This direction is worth two marks in a proof question: one for identifying the two mixed derivatives and one for quoting the symmetry.

### 3.2 Proof of sufficiency

Assume $M_{y}=N_{x}$ on a rectangle containing a base point $(x_{0},y_{0})$, and define

$$
F(x,y)=\int_{x_{0}}^{x}M(t,y)\,dt+\int_{y_{0}}^{y}N(x_{0},s)\,ds .
$$

Step 1. Differentiate with respect to $x$. The second integral is independent of $x$, so only the first contributes, and the fundamental theorem of calculus gives

$$
F_{x}=M(x,y) .
$$

Step 2. Differentiate with respect to $y$. The second integration produces $N(x_{0},y)$, and the first produces the integral of $M_{y}$ at fixed $y$.

$$
F_{y}=\int_{x_{0}}^{x}M_{y}(t,y)\,dt+N(x_{0},y)
$$

Step 3. Use the hypothesis to replace $M_{y}$ by $N_{x}$.

$$
F_{y}=\int_{x_{0}}^{x}N_{x}(t,y)\,dt+N(x_{0},y)
$$

Step 4. Integrate the derivative of $N$ with respect to its first argument.

$$
F_{y}=N(x,y)-N(x_{0},y)+N(x_{0},y)=N(x,y)
$$

Steps 1 and 4 establish both required identities, so the form is exact. The construction is explicit, which is why the sufficiency direction can be called constructive; the rectangle hypothesis is used exactly here, to guarantee that the two straight-line segments stay inside the domain.

### 3.3 Derivation of the two one-variable tests

Let $\mu$ be an integrating factor, so that

$$
\frac{\partial}{\partial y}\left(\mu M\right)=\frac{\partial}{\partial x}\left(\mu N\right) .
$$

Expanding both products gives the governing equation for $\mu$:

$$
\mu_{y}M+\mu M_{y}=\mu_{x}N+\mu N_{x} .
$$

Case 1. Suppose $\mu=\mu(x)$. Then $\mu_{y}=0$ and $\mu_{x}=\mu'$, so

$$
\mu M_{y}=\mu' N+\mu N_{x}, \qquad \mu\left(M_{y}-N_{x}\right)=\mu' N ,
$$

and division by $\mu N$ gives

$$
\frac{\mu'}{\mu}=\frac{M_{y}-N_{x}}{N} .
$$

The left side is a function of $x$ alone, so a factor of this shape exists exactly when the right side is a function of $x$ alone. Separating variables and integrating,

$$
\mu(x)=\exp\left(\int\frac{M_{y}-N_{x}}{N}\,dx\right) .
$$

Case 2. Suppose $\mu=\mu(y)$. Then $\mu_{x}=0$ and $\mu_{y}=\mu'$, so

$$
\mu' M+\mu M_{y}=\mu N_{x}, \qquad \mu' M=\mu\left(N_{x}-M_{y}\right) ,
$$

and division by $\mu M$ gives

$$
\frac{\mu'}{\mu}=\frac{N_{x}-M_{y}}{M}, \qquad \mu(y)=\exp\left(\int\frac{N_{x}-M_{y}}{M}\,dy\right) .
$$

The sign difference between the two numerators is the single most examinable detail in the derivation. It disappears if the ratio is read off from the correct intermediate equation rather than from memory.

### 3.4 Verification of the homogeneous factor

Let $M$ and $N$ be homogeneous of degree $n$, let $D=Mx+Ny$ and let $\mu=1/D$. Then

$$
\mu_{x}=-\frac{D_{x}}{D^{2}}, \qquad \mu_{y}=-\frac{D_{y}}{D^{2}}, \qquad D_{x}=M+xM_{x}+yN_{x}, \qquad D_{y}=xM_{y}+N+yN_{y} .
$$

The condition to be verified is $\mu_{y}M+\mu M_{y}=\mu_{x}N+\mu N_{x}$. Multiplying by $D^{2}$ turns it into

$$
-M D_{y}+D M_{y}=-N D_{x}+D N_{x} ,
$$

that is

$$
D\left(M_{y}-N_{x}\right)-M D_{y}+N D_{x}=0 .
$$

Substituting the three expressions and expanding,

$$
\left(Mx+Ny\right)\left(M_{y}-N_{x}\right)-M\left(xM_{y}+N+yN_{y}\right)+N\left(M+xM_{x}+yN_{x}\right) .
$$

The terms $MN$ and $-MN$ cancel, and the terms $xMM_{y}$ and $-xMM_{y}$ cancel, leaving

$$
x\left(N M_{x}-M N_{x}\right)+y\left(N M_{y}-M N_{y}\right) .
$$

Euler's relation gives $xNM_{x}+yNM_{y}=nMN$ and $xMN_{x}+yMN_{y}=nMN$, and subtracting the second identity from the first produces exactly zero. The condition holds, so the factor is genuine.

### 3.5 Method: solving an exact equation

1. Write $M\,dx+N\,dy=0$ and compute $M_{y}$ and $N_{x}$; confirm equality.
2. Integrate $M$ with respect to $x$ at fixed $y$, adding an arbitrary function $\varphi(y)$ rather than a constant.
3. Differentiate the result with respect to $y$, equate to $N$, and confirm that all $x$-terms cancel.
4. Integrate $\varphi'(y)$, substitute back, and write $F(x,y)=C$.
5. Differentiate the final $F$ with respect to each variable and check that $M$ and $N$ are recovered.

Step 5 is not optional in an examination. It costs two lines and it protects every mark earned in steps 2 to 4.

### 3.6 Method: finding an integrating factor

1. Compute $M_{y}-N_{x}$. If it is zero the equation is already exact and no factor is needed.
2. Divide by $N$ and simplify. If the result contains no $y$, use the $x$-test and exponentiate the integral with respect to $x$.
3. Otherwise divide $N_{x}-M_{y}$ by $M$ and simplify. If the result contains no $x$, use the $y$-test and exponentiate the integral with respect to $y$.
4. Otherwise inspect $M$ and $N$ for homogeneity of a common degree and use $1/\left(Mx+Ny\right)$.
5. Otherwise regroup the form into standard differentials and divide by the denominator suggested by the table in Section 1.7.
6. In every case, multiply out and verify the new exactness condition before integrating, then solve the exact equation and report any excluded points.

The order is fixed by cost: the first two steps are divisions, the third is one multiplication, and only the fourth requires judgement. Attempting the fourth first is the commonest cause of running out of time.

### 3.7 Method: regrouping into standard differentials

1. Split the form into groups, one of which is a listed differential or a multiple of one.
2. Divide the whole equation by the quantity that converts that group into a pure differential, and record where that quantity vanishes.
3. Replace the group by the differential of its potential, and integrate once.
4. Solve for the arbitrary constant, or for $y$ if the question demands an explicit form.

The method produces an integrating factor without any test, and it is the fastest route whenever the coefficients contain $x\,dy-y\,dx$ or $y\,dx+x\,dy$ visibly.

### 3.8 Why the level curves are exactly the solutions

A question sometimes asks for a proof that the solution of an exact equation is $F(x,y)=C$ rather than merely a statement to that effect. The argument is implicit differentiation, and it is short enough to be worth memorising.

Suppose $F_{x}=M$ and $F_{y}=N$, and let $y=y(x)$ be a differentiable function whose graph lies on the level curve $F(x,y)=C$. Differentiating the identity $F\left(x,y(x)\right)=C$ with respect to $x$ by the chain rule gives

$$
F_{x}+F_{y}\frac{dy}{dx}=0 .
$$

Substituting the two definitions of the coefficients,

$$
M+N\frac{dy}{dx}=0 ,
$$

which is the equation in slope form on any interval where $N\neq 0$. Hence every differentiable branch of a level curve solves the equation.

The converse needs one more line. If a curve solves $M+N\frac{dy}{dx}=0$ and if $F$ is a potential, then along that curve

$$
\frac{d}{dx}F\left(x,y(x)\right)=F_{x}+F_{y}\frac{dy}{dx}=M+N\frac{dy}{dx}=0 ,
$$

so $F$ is constant along the curve and the curve lies on a single level set. The two implications together say that the solutions of the exact equation and the level curves of the potential are the same curves, which is the statement to be proved.

Two qualifications belong in the answer. The argument covers only the part of a level curve where $N\neq 0$, so vertical pieces of a level curve, where the curve is not the graph of a function of $x$, must be added by symmetry or by treating $x$ as a function of $y$. And the level curves must be genuinely one-dimensional, which fails at a critical point of $F$ where both partial derivatives vanish; such a point is a single solution rather than a curve.

## 4. Representative Worked Examples and Solutions

### 4.1 Problem: exact equation with an initial condition

Show that

$$
\left(2xy+3x^{2}\right)dx+\left(x^{2}+4y^{3}\right)dy=0
$$

is exact, and solve it subject to $y=2$ when $x=1$.

### 4.2 Solution: criterion, potential, condition

Step 1. Identify the coefficients and compute the cross partials. [2 marks]

$$
M=2xy+3x^{2}, \qquad N=x^{2}+4y^{3}, \qquad M_{y}=2x, \qquad N_{x}=2x
$$

Step 2. Since the two cross partials agree identically, the equation is exact and a potential exists. [1 mark]

Step 3. Integrate $M$ with respect to $x$ at fixed $y$, adding an arbitrary function of $y$. [2 marks]

$$
F(x,y)=\int\left(2xy+3x^{2}\right)dx=x^{2}y+x^{3}+\varphi(y)
$$

Step 4. Differentiate with respect to $y$ and equate to $N$. [1 mark]

$$
x^{2}+\varphi'(y)=x^{2}+4y^{3}
$$

Step 5. Cancel the $x$-terms, which is the consistency check, and integrate. [2 marks]

$$
\varphi'(y)=4y^{3}, \qquad \varphi(y)=y^{4}
$$

Step 6. Write the potential and the general solution. [1 mark]

$$
F(x,y)=x^{2}y+x^{3}+y^{4}, \qquad x^{2}y+x^{3}+y^{4}=C
$$

Step 7. Impose the condition at $(1,2)$. [1 mark]

$$
1\cdot 2+1+16=19
$$

Step 8. State the particular solution and verify. [1 mark]

$$
x^{2}y+x^{3}+y^{4}=19, \qquad F_{x}=2xy+3x^{2}, \qquad F_{y}=x^{2}+4y^{3}
$$

Both partial derivatives reproduce the coefficients, and the point $(1,2)$ gives $19$, so the answer is complete.

### 4.3 Problem: integrating factor of the form $x^{n}$

Solve

$$
\left(3x+2y^{2}\right)dx+2xy\,dy=0 .
$$

### 4.4 Solution: test, exponentiate, solve

Step 1. Identify the coefficients and test exactness. [2 marks]

$$
M=3x+2y^{2}, \qquad N=2xy, \qquad M_{y}=4y, \qquad N_{x}=2y
$$

Since $4y\neq 2y$ away from $y=0$, the equation is not exact.

Step 2. Form the ratio for a factor depending on $x$ alone and simplify. [2 marks]

$$
\frac{M_{y}-N_{x}}{N}=\frac{4y-2y}{2xy}=\frac{2y}{2xy}=\frac{1}{x}
$$

Step 3. The ratio is a function of $x$ alone, so an integrating factor of that shape exists; exponentiate the integral. [2 marks]

$$
\mu=\exp\left(\int\frac{1}{x}\,dx\right)=x
$$

Step 4. Multiply the equation through and write the new coefficients. [1 mark]

$$
\left(3x^{2}+2xy^{2}\right)dx+2x^{2}y\,dy=0
$$

Step 5. Verify exactness of the new equation, which is the step that earns the method marks even when the factor is wrong. [2 marks]

$$
\frac{\partial}{\partial y}\left(3x^{2}+2xy^{2}\right)=4xy, \qquad \frac{\partial}{\partial x}\left(2x^{2}y\right)=4xy
$$

Step 6. Integrate the new coefficient of $dx$ with respect to $x$. [2 marks]

$$
F(x,y)=\int\left(3x^{2}+2xy^{2}\right)dx=x^{3}+x^{2}y^{2}+\varphi(y)
$$

Step 7. Differentiate with respect to $y$, equate to the new coefficient of $dy$, and conclude that $\varphi$ is constant. [2 marks]

$$
2x^{2}y+\varphi'(y)=2x^{2}y, \qquad \varphi'(y)=0
$$

Step 8. State the solution and verify. [1 mark]

$$
x^{3}+x^{2}y^{2}=C, \qquad F_{x}=3x^{2}+2xy^{2}=\mu M, \qquad F_{y}=2x^{2}y=\mu N
$$

Both partial derivatives agree with the multiplied coefficients, so the factor and the solution are both correct.

### 4.5 Problem: the same equation by both one-variable tests

Solve

$$
y\,dx-x\,dy=0
$$

by an integrating factor depending on $y$ alone, and confirm the answer by the factor depending on $x$ alone.

### 4.6 Solution: two routes, one family

Step 1. Identify the coefficients and test exactness. [2 marks]

$$
M=y, \qquad N=-x, \qquad M_{y}=1, \qquad N_{x}=-1
$$

The cross partials differ, so the equation is not exact.

Step 2. Form the ratio for a factor depending on $y$ alone. [2 marks]

$$
\frac{N_{x}-M_{y}}{M}=\frac{-1-1}{y}=-\frac{2}{y}
$$

Step 3. Exponentiate the integral with respect to $y$. [2 marks]

$$
\mu=\exp\left(\int-\frac{2}{y}\,dy\right)=y^{-2}
$$

Step 4. Multiply through by $1/y^{2}$ and verify exactness. [2 marks]

$$
\frac{1}{y}\,dx-\frac{x}{y^{2}}\,dy=0, \qquad \frac{\partial}{\partial y}\left(\frac{1}{y}\right)=-\frac{1}{y^{2}}=\frac{\partial}{\partial x}\left(-\frac{x}{y^{2}}\right)
$$

Step 5. Integrate the coefficient of $dx$ with respect to $x$. [2 marks]

$$
F(x,y)=\frac{x}{y}+\varphi(y)
$$

Step 6. Differentiate with respect to $y$, equate to the coefficient of $dy$, and conclude. [2 marks]

$$
-\frac{x}{y^{2}}+\varphi'(y)=-\frac{x}{y^{2}}, \qquad \varphi'(y)=0, \qquad \frac{x}{y}=C
$$

Step 7. Present the explicit solution. [1 mark]

$$
x=Cy
$$

Step 8. Confirm by the other test. With the ratio

$$
\frac{M_{y}-N_{x}}{N}=\frac{2}{-x}=-\frac{2}{x},
$$

the factor depending on $x$ alone is $x^{-2}$, and with that factor the potential is $-y/x$, whose level curves are the same curves $y/x=\text{constant}$. Hence the second route gives $y=C'x$. Since $x=Cy$ and $y=C'x$ are the same family with $C'=1/C$, the two routes agree. [2 marks]

Step 9. Report the excluded sets. The factor $1/y^{2}$ excludes $y=0$, and the factor $1/x^{2}$ excludes $x=0$; both excluded lines do satisfy the original equation, so the general solution is completed by them. [1 mark]

### 4.7 Problem: homogeneous equation

Solve

$$
\left(x+y\right)dx+\left(y-x\right)dy=0
$$

using the integrating factor $1/\left(Mx+Ny\right)$.

### 4.8 Solution: Euler's relation, then two standard differentials

Step 1. Identify the coefficients and test exactness. [2 marks]

$$
M=x+y, \qquad N=y-x, \qquad M_{y}=1, \qquad N_{x}=-1
$$

The equation is not exact.

Step 2. Note that both coefficients are homogeneous of degree one, and compute the denominator. [2 marks]

$$
Mx+Ny=x\left(x+y\right)+y\left(y-x\right)=x^{2}+xy+y^{2}-xy=x^{2}+y^{2}
$$

Step 3. State the integrating factor. [1 mark]

$$
\mu=\frac{1}{x^{2}+y^{2}}
$$

Step 4. Multiply through and verify exactness. [3 marks]

$$
\frac{x+y}{x^{2}+y^{2}}\,dx+\frac{y-x}{x^{2}+y^{2}}\,dy=0
$$

For the coefficient of $dx$,

$$
\frac{\partial}{\partial y}\left(\frac{x+y}{x^{2}+y^{2}}\right)=\frac{\left(x^{2}+y^{2}\right)-2y\left(x+y\right)}{\left(x^{2}+y^{2}\right)^{2}}=\frac{x^{2}-2xy-y^{2}}{\left(x^{2}+y^{2}\right)^{2}} ,
$$

and for the coefficient of $dy$,

$$
\frac{\partial}{\partial x}\left(\frac{y-x}{x^{2}+y^{2}}\right)=\frac{-\left(x^{2}+y^{2}\right)-2x\left(y-x\right)}{\left(x^{2}+y^{2}\right)^{2}}=\frac{x^{2}-2xy-y^{2}}{\left(x^{2}+y^{2}\right)^{2}} .
$$

The two agree, so the multiplied equation is exact.

Step 5. Integrate the coefficient of $dx$ with respect to $x$. Rather than a single integration, split into standard differentials, which is legitimate because the sum of two exact forms is exact. [3 marks]

$$
\frac{x+y}{x^{2}+y^{2}}\,dx+\frac{y-x}{x^{2}+y^{2}}\,dy=\frac{x\,dx+y\,dy}{x^{2}+y^{2}}+\frac{y\,dx-x\,dy}{x^{2}+y^{2}}
$$

Step 6. Recognise the two table entries. [2 marks]

$$
\frac{x\,dx+y\,dy}{x^{2}+y^{2}}=d\left(\frac{1}{2}\ln\left(x^{2}+y^{2}\right)\right), \qquad \frac{y\,dx-x\,dy}{x^{2}+y^{2}}=-d\left(\arctan\frac{y}{x}\right)
$$

Step 7. Combine into one differential. [1 mark]

$$
d\left(\frac{1}{2}\ln\left(x^{2}+y^{2}\right)-\arctan\frac{y}{x}\right)=0
$$

Step 8. State the solution. [1 mark]

$$
\frac{1}{2}\ln\left(x^{2}+y^{2}\right)-\arctan\frac{y}{x}=C, \qquad \ln\left(x^{2}+y^{2}\right)-2\arctan\frac{y}{x}=C'
$$

Step 9. Verify by differentiating the potential. [2 marks]

$$
F_{x}=\frac{x}{x^{2}+y^{2}}+\frac{y}{x^{2}+y^{2}}=\frac{x+y}{x^{2}+y^{2}}=\mu M, \qquad F_{y}=\frac{y}{x^{2}+y^{2}}-\frac{x}{x^{2}+y^{2}}=\frac{y-x}{x^{2}+y^{2}}=\mu N
$$

Both identities hold, so the potential is correct.

### 4.9 Problem: determine a constant and solve

If

$$
\left(\frac{1}{x^{2}}+\frac{1}{y^{2}}\right)dx+\frac{Ax+1}{y^{3}}\,dy=0
$$

is exact, find $A$ and solve the equation.

### 4.10 Solution: equate the cross partials, then integrate

Step 1. Identify the coefficients. [1 mark]

$$
M=\frac{1}{x^{2}}+\frac{1}{y^{2}}, \qquad N=\frac{Ax+1}{y^{3}}
$$

Step 2. Compute both cross partials. [2 marks]

$$
\frac{\partial M}{\partial y}=-\frac{2}{y^{3}}, \qquad \frac{\partial N}{\partial x}=\frac{A}{y^{3}}
$$

Step 3. Impose exactness as an identity in $y$, valid for every $y\neq 0$. [2 marks]

$$
-\frac{2}{y^{3}}=\frac{A}{y^{3}} \qquad \text{for all } y, \qquad A=-2
$$

Step 4. Substitute $A$ and integrate $M$ with respect to $x$ at fixed $y$. [2 marks]

$$
F(x,y)=\int\left(\frac{1}{x^{2}}+\frac{1}{y^{2}}\right)dx=-\frac{1}{x}+\frac{x}{y^{2}}+\varphi(y)
$$

Step 5. Differentiate with respect to $y$ and equate to $N$ with $A=-2$. [2 marks]

$$
-\frac{2x}{y^{3}}+\varphi'(y)=\frac{1-2x}{y^{3}}
$$

Step 6. Cancel the terms in $x$ and integrate the remainder. [2 marks]

$$
\varphi'(y)=\frac{1}{y^{3}}, \qquad \varphi(y)=-\frac{1}{2y^{2}}
$$

Step 7. State the potential and the solution. [1 mark]

$$
F(x,y)=-\frac{1}{x}+\frac{x}{y^{2}}-\frac{1}{2y^{2}}, \qquad -\frac{1}{x}+\frac{x}{y^{2}}-\frac{1}{2y^{2}}=C
$$

Step 8. Verify. [2 marks]

$$
F_{x}=\frac{1}{x^{2}}+\frac{1}{y^{2}}=M, \qquad F_{y}=-\frac{2x}{y^{3}}+\frac{1}{y^{3}}=\frac{1-2x}{y^{3}}=N \quad \text{with } A=-2
$$

Both derivatives reproduce the coefficients with the computed value of $A$, so the constant and the solution are both correct.

### 4.11 Problem: regrouping with the angle differential

Solve

$$
x\,dy-y\,dx=\left(x^{2}+y^{2}\right)dy .
$$

### 4.12 Solution: divide by $x^{2}+y^{2}$ and integrate

Step 1. Move every term to the left. [1 mark]

$$
x\,dy-y\,dx-\left(x^{2}+y^{2}\right)dy=0
$$

Step 2. Identify the coefficients and confirm that the equation is not exact. [2 marks]

$$
M=-y, \qquad N=x-x^{2}-y^{2}, \qquad M_{y}=-1, \qquad N_{x}=1-2x
$$

Step 3. Divide the equation by $x^{2}+y^{2}$, which is positive away from the origin, and record the restriction. [2 marks]

$$
\frac{x\,dy-y\,dx}{x^{2}+y^{2}}-dy=0, \qquad (x,y)\neq(0,0)
$$

Step 4. Replace the first group by the differential of the polar angle. [2 marks]

$$
d\left(\arctan\frac{y}{x}\right)-dy=0
$$

Step 5. Integrate once. [2 marks]

$$
\arctan\frac{y}{x}-y=C
$$

Step 6. Solve for $y$ if an explicit form is required. [1 mark]

$$
\frac{y}{x}=\tan\left(y+C\right), \qquad y=x\tan\left(y+C\right)
$$

Step 7. Verify by implicit differentiation. Differentiating $\arctan\frac{y}{x}=y+C$ with respect to $x$ and writing $u=y/x$,

$$
\frac{u'}{1+u^{2}}=\frac{dy}{dx}, \qquad \frac{xy'-y}{x^{2}+y^{2}}=\frac{dy}{dx} .
$$

Multiplying through by $x^{2}+y^{2}$ gives

$$
xy'-y=\left(x^{2}+y^{2}\right)y', \qquad y'=\frac{y}{x-x^{2}-y^{2}} ,
$$

which is the original equation solved for the slope. [2 marks]

Step 8. Note the factor used. The division by $x^{2}+y^{2}$ is the integrating factor, and the multiplied coefficients satisfy the exactness condition because

$$
\frac{\partial}{\partial y}\left(-\frac{y}{x^{2}+y^{2}}\right)=\frac{y^{2}-x^{2}}{\left(x^{2}+y^{2}\right)^{2}}=\frac{\partial}{\partial x}\left(\frac{x-x^{2}-y^{2}}{x^{2}+y^{2}}\right) .
$$

[2 marks]

### 4.13 Problem: an exact equation with trigonometric coefficients

Show that

$$
\left(y\sec^{2}x+\sec x\tan x\right)dx+\left(\tan x+2y\right)dy=0
$$

is exact, and solve it subject to $y=1$ when $x=0$.

### 4.14 Solution: differentiate, integrate, impose

Step 1. Identify the coefficients. [1 mark]

$$
M=y\sec^{2}x+\sec x\tan x, \qquad N=\tan x+2y
$$

Step 2. Compute the cross partials, using $\frac{d}{dx}\tan x=\sec^{2}x$ and $\frac{d}{dx}\sec x=\sec x\tan x$. [2 marks]

$$
\frac{\partial M}{\partial y}=\sec^{2}x, \qquad \frac{\partial N}{\partial x}=\sec^{2}x
$$

Step 3. The cross partials agree, so the equation is exact. [1 mark]

Step 4. Integrate $M$ with respect to $x$ at fixed $y$. The term $y\sec^{2}x$ integrates to $y\tan x$ and the term $\sec x\tan x$ integrates to $\sec x$. [3 marks]

$$
F(x,y)=y\tan x+\sec x+\varphi(y)
$$

Step 5. Differentiate with respect to $y$ and equate to $N$. [1 mark]

$$
\tan x+\varphi'(y)=\tan x+2y
$$

Step 6. Cancel and integrate. [2 marks]

$$
\varphi'(y)=2y, \qquad \varphi(y)=y^{2}
$$

Step 7. Write the general solution. [1 mark]

$$
y\tan x+\sec x+y^{2}=C
$$

Step 8. Impose the condition at $x=0$, $y=1$, using $\tan 0=0$ and $\sec 0=1$. [1 mark]

$$
1\cdot 0+1+1=2
$$

Step 9. State the particular solution and verify. [1 mark]

$$
y\tan x+\sec x+y^{2}=2, \qquad F_{x}=y\sec^{2}x+\sec x\tan x, \qquad F_{y}=\tan x+2y
$$

Both partial derivatives reproduce the coefficients, so exactness, potential and constant are all confirmed.

### 4.15 Problem: an equation given in slope form

Solve

$$
\frac{dy}{dx}=-\frac{2x+y}{x+4y}
$$

subject to $y=1$ when $x=0$.

### 4.16 Solution: clear the fraction, then follow the standard pattern

Step 1. Clear the fraction to obtain a differential form. Multiplying the equation by $x+4y$ gives

$$
\left(2x+y\right)dx+\left(x+4y\right)dy=0 .
$$

[1 mark]

Step 2. Identify the coefficients and compute the cross partials. [2 marks]

$$
M=2x+y, \qquad N=x+4y, \qquad M_{y}=1, \qquad N_{x}=1
$$

Step 3. The cross partials agree, so the equation is exact. [1 mark]

Step 4. Integrate $M$ with respect to $x$ at fixed $y$, adding an arbitrary function of $y$. [2 marks]

$$
F(x,y)=\int\left(2x+y\right)dx=x^{2}+xy+\varphi(y)
$$

Step 5. Differentiate with respect to $y$ and equate to $N$. [1 mark]

$$
x+\varphi'(y)=x+4y
$$

Step 6. Cancel and integrate. [2 marks]

$$
\varphi'(y)=4y, \qquad \varphi(y)=2y^{2}
$$

Step 7. Write the general solution. [1 mark]

$$
x^{2}+xy+2y^{2}=C
$$

Step 8. Impose the condition at $x=0$, $y=1$. [1 mark]

$$
0+0+2\cdot 1=2
$$

Step 9. State the particular solution and verify. [2 marks]

$$
x^{2}+xy+2y^{2}=2, \qquad F_{x}=2x+y, \qquad F_{y}=x+4y
$$

Both partial derivatives reproduce the coefficients. Differentiating the solution implicitly,

$$
2x+y+\left(x+4y\right)\frac{dy}{dx}=0, \qquad \frac{dy}{dx}=-\frac{2x+y}{x+4y},
$$

which is the equation that was given, so the solution is confirmed independently of the potential.

Step 10. Note the general lesson. A slope-form question is converted by moving the denominator to the left as a multiplier, and the resulting form must be tested like any other; the conversion does not guarantee exactness, and if the test fails the integrating factor must be found in the usual way.

## 5. Mathematical Extensions, Limits, and Common Errors

### 5.1 The trap table

The table collects the errors that lose the most marks in this topic. The middle column describes what the mistake looks like on paper, so that it can be recognised while writing rather than afterwards.

| Trap | How it appears | Correct move |
|---|---|---|
| Wrong cross partials | $M_{x}$ compared with $N_{y}$ | Compare $M_{y}$ with $N_{x}$; the $dx$-coefficient is differentiated with respect to $y$ |
| Wrong variable held constant | $3x^{2}y$ differentiated to $6xy$ when computing $M_{y}$ | Treat $x$ as a constant, so the derivative is $3x^{2}$ |
| Constant instead of function | $F=\int M\,dx+C$ then failure to match $N$ | Write $\varphi(y)$; any function of $y$ alone disappears under $\frac{\partial}{\partial x}$ |
| Second constant added | Answer contains $C_{1}$ and $C_{2}$ | The final answer carries one constant; $\varphi$ contributes none |
| Exactness proved, then stop | Two cross partials, then a full stop | Continue to the potential and the constant; exactness is worth about a third of the marks |
| Failed test read as no factor | Both ratios depend on two variables, so the answer ends | Look for homogeneity, then for standard differentials |
| Sign slip in the $y$-test | $(M_{y}-N_{x})/M$ used instead of $(N_{x}-M_{y})/M$ | Derive from $\mu' M=\mu\left(N_{x}-M_{y}\right)$ |
| Homogeneous factor misused | $M$ of degree two and $N$ of degree one | Both coefficients must share the same degree |
| Division without restriction | Answer contains $1/x^{2}$ and no comment | State the excluded set, usually $x=0$ or $y=0$ |
| Unverified potential | No differentiation at the end | Check $F_{x}=M$ and $F_{y}=N$; two lines, and they catch almost every slip |

### 5.2 High-yield facts and what they are worth

The criterion itself is worth two or three marks and takes two lines. The potential is worth four or five and takes two integrations. The constant of an initial condition is worth one or two and takes one substitution. The final verification is worth one or two and takes two differentiations. A full six-mark or eight-mark solution therefore has a predictable shape, and the shape is worth rehearsing until it is automatic.

Three results are worth memorising as exact formulas because they appear in questions that give no hint. The factor $1/x^{2}$ makes $x\,dy-y\,dx$ exact with potential $y/x$. The factor $1/\left(x^{2}+y^{2}\right)$ makes it exact with potential $\arctan\left(\frac{y}{x}\right)$. The factor $1/(xy)$ makes $y\,dx+x\,dy$ exact with potential $\ln(xy)$. Every regrouping question in the syllabus is a combination of these three, sometimes with the radial differential $x\,dx+y\,dy$ divided by $x^{2}+y^{2}$.

A fourth fact is structural rather than formulaic: an equation that is linear in $y$ has the integrating factor $\exp\left(\int P\,dx\right)$, and that factor is a special case of the $x$-test. Recognising the linear equation underneath an exactness question often gives a second route to the same answer, and a second route is the best available check when time permits.

### 5.3 Limits of the method

The tests are sufficient, not necessary, and the equality of cross partials is local unless the domain has no holes. On a domain with a hole the criterion can hold while no single-valued potential exists; the classical case is the angle form on the plane with the origin deleted. No examination in this course requires the topological argument, but a remark that the domain is assumed simply connected earns credit in a proof.

There is also a limit to what integration can produce. Even when a potential exists, the answer is usually an implicit relation that cannot be solved for $y$. Attempting to isolate $y$ from a relation such as $y\tan x+\sec x+y^{2}=2$ wastes time and can introduce errors; the implicit form is the answer, and an explicit form should be attempted only when the relation is linear or quadratic in $y$.

### 5.4 Revision checklist

The following list is ordered by frequency of examination and should be worked through in this order during revision.

1. State the criterion in words and in symbols, including the continuity hypothesis and the rectangular domain.
2. Prove necessity in three lines, naming the symmetry of mixed partials.
3. Reproduce the sufficiency construction and verify both partial derivatives.
4. Derive the $x$-test from $\mu' N=\mu\left(M_{y}-N_{x}\right)$, and the $y$-test from $\mu' M=\mu\left(N_{x}-M_{y}\right)$.
5. Compute $Mx+Ny$ for a homogeneous pair and verify the resulting factor once in full.
6. Reproduce the table of standard differentials from memory, differentiating each potential.
7. Solve one exact equation with an initial condition from start to verified finish without notes.
8. Solve one equation by each of the three integrating-factor routes, checking the new exactness condition in each case.
9. Solve one regrouping question that ends in an arctangent.
10. Recite the trap table from Section 5.1, and in particular the two numerators in the tests.

### 5.5 Time strategy in the examination

Allocate the marks before allocating the minutes. An exactness-and-solution question is worth roughly seven marks and should take about ten minutes: two minutes for the criterion, five for the two integrations, two for the condition and the verification. An integrating-factor question is worth eight to nine marks and should take about twelve minutes: three to identify and justify the factor, two to multiply out and verify exactness, five for the integration, two for the final check.

If a factor is not found within three minutes of testing both ratios, abandon the search and try regrouping into standard differentials, because that route needs no algebra beyond division. If the equation for $\varphi'(y)$ still contains $x$ after the first attempt, do not re-solve from the beginning; instead re-differentiate $\int M\,dx$ with respect to $y$, since the error is almost always in that derivative rather than in the integration.

Always leave two minutes at the end of a question to differentiate the claimed potential. That check is the difference between a solution that looks finished and one that is. And always write the final answer as an equation rather than an expression: $x^{2}y-3x+2y^{2}=7$ is an answer, while $x^{2}y-3x+2y^{2}$ is a fragment.

### 5.6 One-paragraph summary of the topic

The topic converts a first order equation into a statement about a single function of two variables. If the form $M\,dx+N\,dy$ is the total differential of a potential $F$, the equation reads $dF=0$, and its solutions are the level curves $F=C$; the test for this is the equality of the cross partials, which is necessary because a potential has equal mixed partials and sufficient because the equality permits the potential to be constructed by two integrations. When the test fails, multiplication by an integrating factor repairs the form, and the three routes to such a factor are the ratio depending on $x$, the ratio depending on $y$, and the homogeneous denominator $Mx+Ny$. The standard differentials convert the same theory into pattern recognition, and the check at the end, namely differentiating the potential back to the coefficients, is the one step that should never be omitted.
