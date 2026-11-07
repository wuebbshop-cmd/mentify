## 1. Foundational Concepts, Definitions, and Axioms

### 1.1 The standard form and the linear operator

Throughout this note the independent variable is $x$ and the unknown is a real-valued function $y$ of $x$, defined and differentiable on an interval $I$.

> **Definition (First-order linear equation).** A first-order ordinary differential equation is linear if it can be written in the form
>
> $$
> \frac{dy}{dx}+P(x)\,y=Q(x),
> $$
>
> where $P$ and $Q$ are given functions of $x$ alone, defined and continuous on $I$.

The equation is first order because the only derivative present is the first, and linear because the map $y\mapsto \frac{dy}{dx}+Py$ is linear over the reals. The latter statement is worth making explicit, since it is the property that all later structure theorems exploit.

> **Definition (The linear operator).** For a differentiable function $y$ and a continuous coefficient $P$, define
>
> $$
> L[y]=\frac{dy}{dx}+P(x)\,y .
> $$
>
> Then $L$ satisfies $L[\alpha y_{1}+\beta y_{2}]=\alpha L[y_{1}]+\beta L[y_{2}]$ for all constants $\alpha,\beta$ and all differentiable $y_{1},y_{2}$.

The operator notation compresses the equation to $L[y]=Q$ and makes the superposition principle a one-line consequence of the linearity of differentiation. It also makes the vocabulary of the topic precise: $L[y]=Q$ is the non-homogeneous equation, $L[y]=0$ is the homogeneous equation, and a solution of the non-homogeneous equation is often called a particular integral while a solution of the homogeneous equation is called a complementary function.

Any equation that can be brought to the standard form by algebra is linear, and the reduction is part of the solution. The equation $a(x)\frac{dy}{dx}+b(x)y=c(x)$ with $a$ never zero on $I$ is linear, because division by $a(x)$ produces

$$
\frac{dy}{dx}+\frac{b(x)}{a(x)}\,y=\frac{c(x)}{a(x)},
$$

which is standard form with $P=\frac{b}{a}$ and $Q=\frac{c}{a}$. The equation $\frac{dy}{dx}=f(x)-g(x)y$ is linear with $P=g$ and $Q=f$, obtained by moving the $y$ term to the left. The equation $y\frac{dy}{dx}+y^{2}=x$ is not linear in $y$, but it is linear in $z=y^{2}$, since it becomes $\frac{1}{2}\frac{dz}{dx}+z=x$. This last observation is the germ of the substitution methods developed in Sections 1.6 and 1.7.

### 1.2 The recognition criterion

The classification is decidable by inspection, and it is worth reducing to a checklist that can be applied without hesitation.

> **Criterion (Test for linearity).** An equation is first-order linear if and only if, after clearing denominators that involve only $x$ and after collecting terms, it can be written as $A(x)\frac{dy}{dx}+B(x)y=C(x)$ with $A(x)\neq 0$ on the interval of interest. Equivalently, the equation is linear exactly when it is a polynomial of degree at most one in the pair $\left(y,\frac{dy}{dx}\right)$, with coefficients depending on $x$ alone.

Three consequences follow immediately. First, no product of $y$ with $\frac{dy}{dx}$ may appear. Second, no power of $y$ other than the first may appear. Third, $y$ may not appear as the argument of a non-linear function, so $\sin y$, $e^{y}$ and $\sqrt{y}$ are all excluded. The criterion is about the unknown only; arbitrarily complicated functions of $x$ are permitted, so an equation such as

$$
\frac{dy}{dx}+x^{3}e^{x}\cos x\;y=\frac{\ln x}{1+x^{2}}
$$

is perfectly linear, with $P(x)=x^{3}e^{x}\cos x$ and $Q(x)=\frac{\ln x}{1+x^{2}}$.

The four canonical non-linear obstructions are worth naming, because recognising them tells the reader whether a substitution is likely to help. A power $y^{n}$ with $n\neq 0,1$ signals a Bernoulli equation and yields to $v=y^{1-n}$. A product $y\frac{dy}{dx}$ signals an equation that is often linear in $y^{2}$, since $y\frac{dy}{dx}=\frac{1}{2}\frac{d}{dx}\left(y^{2}\right)$. A function such as $\sin y$ or $e^{y}$ signals an equation that is linear in a new variable only if the other occurrences cooperate, which is rare. An occurrence of $y$ inside the coefficient of $\frac{dy}{dx}$ signals an equation that may be linear in $x$ as a function of $y$, which is the reciprocal trick of Section 1.7.

### 1.3 Homogeneous and non-homogeneous equations

> **Definition (Homogeneous equation).** The equation $L[y]=Q$ is homogeneous on $I$ if $Q(x)=0$ for every $x\in I$, and non-homogeneous otherwise. In the homogeneous case the equation is written $L[y]=0$.

The distinction is not a labelling convenience; it separates two different solution structures. The homogeneous equation has the property that its solution set is a one-dimensional vector space, so every solution is a constant multiple of a single non-zero solution. The non-homogeneous equation has the property that its solution set is an affine line, obtained by adding one particular solution to the whole homogeneous space. Both statements are proved in Section 2.5.

> **Definition (General solution).** The general solution of a first-order equation on $I$ is a one-parameter family $y=\phi(x,C)$ that contains every solution on $I$ as $C$ ranges over the reals.

> **Definition (Particular solution, initial-value problem).** A particular solution is a single member of the family. An initial-value problem consists of the equation together with a condition $y(x_{0})=y_{0}$ with $x_{0}\in I$.

The phrase "on $I$" is part of the definition. A formula that solves the equation on one side of a singularity but not on the other does not solve it on an interval that straddles the singularity, and the interval must be stated.

### 1.4 The integrating factor

> **Definition (Integrating factor).** A function $\mu$, positive and differentiable on $I$, is an integrating factor for $L[y]=Q$ if multiplication of the equation by $\mu$ makes the left-hand side the derivative of a single product, that is, if
>
> $$
> \mu\left(\frac{dy}{dx}+P y\right)=\frac{d}{dx}\left(\mu y\right)
> $$
>
> for every differentiable $y$.

Expanding the right-hand side by the product rule and comparing coefficients gives the equivalent condition $\mu'=P\mu$. Since $\mu>0$, this is separable and has the solution

$$
\mu(x)=e^{\int P(x)\,dx},
$$

where the integral denotes any fixed antiderivative. The definition is therefore constructive: for a linear equation an integrating factor always exists, is unique up to a positive multiplicative constant, and can be written explicitly.

Two elementary properties follow from the definition and are used constantly. Because $\mu$ is an exponential, it never vanishes, so multiplying by $\mu$ and dividing by $\mu$ are both reversible operations and the solution set is unchanged. And because $\mu$ is positive, the sign of $\mu y$ is the sign of $y$, which is what makes positivity arguments possible.

> **Lemma (Normalisation).** If $\mu_{1}$ and $\mu_{2}$ both satisfy $\mu'=P\mu$ on $I$, then $\mu_{1}=k\mu_{2}$ for some constant $k$. Consequently the general solution obtained from either choice is the same family.

The proof is the standard uniqueness argument for a first-order linear homogeneous equation applied to the ratio, and it is given in Section 3.1. In computations the constant is discarded by taking the simplest antiderivative of $P$, which amounts to choosing $k=1$.

### 1.5 Exact equations and the second derivation of the integrating factor

There is a second, coordinate-free way to understand the integrating factor, and it explains the name.

> **Definition (Exact equation).** The differential form $M(x,y)\,dx+N(x,y)\,dy=0$ is exact on a rectangle if there exists a function $F(x,y)$ with $\frac{\partial F}{\partial x}=M$ and $\frac{\partial F}{\partial y}=N$. In that case the solutions are the level curves $F(x,y)=c$.

> **Criterion (Test for exactness).** If $M,N$ and their first partial derivatives are continuous on a simply connected region, the form is exact if and only if
>
> $$
> \frac{\partial M}{\partial y}=\frac{\partial N}{\partial x} .
> $$

The linear equation $\frac{dy}{dx}+Py=Q$ can be written as the form

$$
\left(Py-Q\right)dx+dy=0,
$$

so $M=Py-Q$ and $N=1$. Then $\frac{\partial M}{\partial y}=P$ and $\frac{\partial N}{\partial x}=0$, and the form is exact only when $P$ vanishes identically. Multiplication by $\mu$ changes the data to $M=\mu\left(Py-Q\right)$ and $N=\mu$, and the exactness test becomes

$$
\frac{\partial M}{\partial y}=\mu P,\qquad \frac{\partial N}{\partial x}=\mu' ,
$$

so the multiplied form is exact exactly when $\mu'=\mu P$. This is the same condition as before, and it shows that an integrating factor is precisely a multiplier that repairs a failure of exactness. The construction of $F$ in that case is carried out in Section 3.2 and yields the solution formula directly.

### 1.6 Bernoulli's equation

> **Definition (Bernoulli equation).** Let $n$ be a real constant. An equation of the form
>
> $$
> \frac{dy}{dx}+P(x)\,y=Q(x)\,y^{n}
> $$
>
> with $P,Q$ continuous on $I$ is called a Bernoulli equation, or an equation reducible to linear form.

The definition deliberately allows every real $n$, including the degenerate values. For $n=0$ the equation reads $\frac{dy}{dx}+Py=Q$ and is linear. For $n=1$ it reads $\frac{dy}{dx}+\left(P-Q\right)y=0$ and is both linear and separable. For all other $n$ the presence of $y^{n}$ destroys linearity, and the equation is genuinely non-linear even though it looks close to the linear form.

The three values $n=2$, $n=-1$ and $n=\frac{1}{2}$ deserve separate mention because they occur most often. When $n=2$ the substitution is $v=y^{-1}$, and the equation becomes linear in the reciprocal of the unknown; the resulting family includes the logistic curve. When $n=-1$ the substitution is $v=y^{2}$, so the equation becomes linear in the square of the unknown. When $n=\frac{1}{2}$ the substitution is $v=y^{1/2}$, so the equation becomes linear in the square root of the unknown.

> **Definition (Bernoulli substitution).** For $n\neq 1$ the Bernoulli substitution is $v=y^{1-n}$, defined on any subinterval on which $y$ has a constant sign.

The restriction to a constant-sign subinterval is not cosmetic. The power $y^{1-n}$ is defined by the real power function only for positive bases when the exponent is irrational, and the transformation presupposes that the division by $y^{n}$ in its derivation is legitimate. Both requirements are met on any interval where $y$ does not vanish.

### 1.7 Equations that become linear when $x$ is the unknown

> **Definition (Reciprocal form).** An equation is in reciprocal linear form on an interval if it can be written as
>
> $$
> \frac{dx}{dy}+A(y)\,x=B(y),
> $$
>
> with $A,B$ continuous functions of $y$.

The passage between the two forms uses the reciprocal relation $\frac{dx}{dy}=1\big/\frac{dy}{dx}$, valid wherever $\frac{dy}{dx}\neq 0$. If the original equation is $\frac{dy}{dx}=f(x,y)$ with $f\neq 0$, then

$$
\frac{dx}{dy}=\frac{1}{f(x,y)},
$$

and if this expression happens to be of the form $B(y)-A(y)x$, the equation is linear in $x$. The class of equations soluble this way is not small: every equation in which $y$ appears only in the combination $x+\phi(y)$, or in which $y$ appears through a power that becomes linear after the swap, falls into it.

The definition also clarifies what is being assumed. Linearity is a property of a chosen pair of variables, and the same equation may be non-linear in $y$ and linear in $x$. Deciding which variable to treat as unknown is part of the analysis, not a preliminary formality.

## 2. Theorems, Lemmas, and Analytical Properties

### 2.1 Equivalence under multiplication

> **Lemma (Reversibility).** Let $\mu$ be continuous, positive and differentiable on $I$. Then $y$ solves $L[y]=Q$ on $I$ if and only if $y$ solves $\mu L[y]=\mu Q$ on $I$.

If $y$ solves the first equation then multiplying the identity by $\mu(x)$ gives the second at every point. Conversely if $y$ solves the second then dividing by $\mu(x)$ gives the first, and division is legitimate because $\mu>0$. The positivity is what licenses the converse, and it is the reason the integrating factor is taken to be an exponential rather than an arbitrary antiderivative-based function that might vanish.

A corollary is that the integrating factor is only determined up to a positive constant, since replacing $\mu$ by $k\mu$ with $k>0$ multiplies both sides by $k$ and preserves the solution set. This is the content of the normalisation lemma of Section 1.4.

### 2.2 The exact-derivative identity

> **Theorem (Integrating-factor identity).** Let $P$ be continuous on $I$ and let $\mu(x)=e^{\int P\,dx}$. Then for every differentiable $y$ on $I$,
>
> $$
> \mu(x)\left(\frac{dy}{dx}+P(x)y\right)=\frac{d}{dx}\left(\mu(x)\,y\right).
> $$

The theorem is an identity in $y$, valid for every differentiable function, and it is the engine of the whole method. Its content is that the two-term expression on the left, which cannot be integrated directly, is exactly the derivative of a single product once the correct multiplier is inserted. The proof occupies Section 3.1.

### 2.3 The solution formula

> **Theorem (General solution).** Let $P,Q$ be continuous on an interval $I$. Then the general solution of $\frac{dy}{dx}+Py=Q$ on $I$ is given by
>
> $$
> y(x)=e^{-\int P\,dx}\left(\int Q(x)\,e^{\int P\,dx}\,dx+C\right),
> $$
>
> where each displayed integral denotes a fixed antiderivative and $C\in\mathbb{R}$.

> **Theorem (Definite-integral form).** With the same hypotheses, the unique solution of the initial-value problem with $y(x_{0})=y_{0}$ is
>
> $$
> y(x)=e^{-\int_{x_{0}}^{x}P(t)\,dt}\left(y_{0}+\int_{x_{0}}^{x}Q(s)\,e^{\int_{x_{0}}^{s}P(t)\,dt}\,ds\right),\qquad x\in I .
> $$

The two forms are equivalent, and each has its use. The indefinite form is convenient when the integrals are elementary and the answer is wanted as a formula; the definite form is safer for initial-value problems, since no constant has to be determined and no sign ambiguity arises from the choice of antiderivative. The definite form also displays the two contributions to the solution: the term $y_{0}e^{-\int P}$ is the decaying (or growing) memory of the initial state, and the integral term is the accumulated effect of the forcing, each increment weighted by the factor $e^{\int_{x_{0}}^{s}P}$ and then discounted back to $x$.

### 2.4 Existence and uniqueness

> **Theorem (Existence and uniqueness for the linear problem).** Let $P,Q$ be continuous on an interval $I$ containing $x_{0}$, and let $y_{0}\in\mathbb{R}$. Then the initial-value problem $\frac{dy}{dx}+Py=Q$, $y(x_{0})=y_{0}$, has exactly one solution on $I$.

The proof is short because the formula is explicit: the right-hand side of the definite-integral formula is defined for every $x\in I$, is differentiable by the fundamental theorem of calculus, and satisfies both the equation and the condition; and any two solutions differ by a solution of the homogeneous equation, which must be a constant multiple of $e^{-\int P}$ and hence vanishes identically if it vanishes at one point. Section 3.3 records the details.

The theorem should be contrasted with the corresponding statement for non-linear equations, where continuity of $f$ alone is insufficient and a Lipschitz condition in $y$ is required. For linear equations continuity of the coefficients is enough, which is why linear problems never exhibit the branching of solutions that the equation $y'=3y^{2/3}$ displays at the origin.

### 2.5 Structure of the solution set

> **Theorem (Structure theorem).** Let $y_{p}$ be any particular solution of $L[y]=Q$ on $I$, and let $y_{h}$ be the general solution of $L[y]=0$ on $I$. Then the general solution of $L[y]=Q$ is $y=y_{p}+y_{h}$.

The theorem has two halves. The first is that $y_{p}+y_{h}$ always solves the non-homogeneous equation, which follows from linearity: $L[y_{p}+y_{h}]=L[y_{p}]+L[y_{h}]=Q+0=Q$. The second is that every solution arises this way, which follows by subtracting: if $y$ is any solution, then $L[y-y_{p}]=Q-Q=0$, so $y-y_{p}$ is a homogeneous solution. The structure theorem is what justifies the phrase "particular integral plus complementary function" in the standard treatment of linear equations.

> **Corollary (Superposition).** If $Q=Q_{1}+Q_{2}$ and $y_{j}$ solves $L[y]=Q_{j}$ for $j=1,2$, then $y_{1}+y_{2}$ solves $L[y]=Q$.

This is the practical form of the theorem for forcing functions that are sums, and it allows a complicated right-hand side to be broken into simpler pieces, each solved separately. It fails for non-linear equations, which is one reason the Bernoulli substitution is valuable: it converts a problem to which superposition does not apply into one to which it does.

### 2.6 The homogeneous solution and its decay

> **Lemma (Homogeneous solution).** The general solution of $L[y]=0$ on $I$ is
>
> $$
> y_{h}(x)=C\,e^{-\int P(x)\,dx},
> $$
>
> and the solution satisfying $y(x_{0})=y_{0}$ is $y_{0}e^{-\int_{x_{0}}^{x}P(t)\,dt}$.

> **Corollary (Monotonicity of the modulus).** If $P(x)\ge 0$ on $I$ and $x\ge x_{0}$, then $\left|y_{h}(x)\right|\le\left|y_{h}(x_{0})\right|$, with equality only if $P$ vanishes on the interval between. If $P(x)\le 0$ then the modulus is non-decreasing.

The corollary is immediate from the formula, since the exponent $-\int_{x_{0}}^{x}P$ is non-positive in the first case. It gives a qualitative reading of the sign of $P$: a positive coefficient damps the homogeneous part, and a negative coefficient amplifies it.

### 2.7 Positivity and comparison

> **Lemma (Positivity).** Suppose $Q(x)\ge 0$ on $I$ and $y(x_{0})\ge 0$. Then $y(x)\ge 0$ for every $x\ge x_{0}$ in $I$.

The proof uses the definite-integral form. The prefactor $e^{-\int_{x_{0}}^{x}P}$ is positive, and the bracket is $y_{0}$ plus an integral whose integrand $Q(s)e^{\int_{x_{0}}^{s}P(t)dt}$ is a product of a non-negative and a positive quantity, hence non-negative. This is a comparison principle: a non-negative forcing cannot drive a non-negative initial state negative, no matter how the coefficient $P$ varies. The principle is used in applications to argue that concentrations, populations and probabilities remain non-negative.

### 2.8 The Bernoulli reduction theorem

> **Theorem (Reduction).** Let $n\neq 1$ and let $P,Q$ be continuous on $I$. On any subinterval $J\subseteq I$ on which $y$ never vanishes, the substitution $v=y^{1-n}$ is a bijection between solutions of
>
> $$
> \frac{dy}{dx}+P(x)y=Q(x)y^{n}
> $$
>
> on $J$ and solutions of
>
> $$
> \frac{dv}{dx}+(1-n)P(x)v=(1-n)Q(x)
> $$
>
> on $J$.

The word bijection is the precise claim, and it is what makes the method complete rather than merely a way of finding some solutions. The map $y\mapsto v=y^{1-n}$ is invertible on a constant-sign interval, and the chain rule converts derivatives in one direction into derivatives in the other. The full computation is in Section 3.4.

> **Corollary (Integrating factor of the reduced equation).** If $\mu=e^{\int P\,dx}$ is the integrating factor of the original coefficient, then the integrating factor of the reduced equation is
>
> $$
> \mu^{1-n}=e^{(1-n)\int P\,dx}.
> $$

The corollary is a useful shortcut in examinations, since it removes the need to recompute an integral that has already been performed. It also explains why the reduced equation is often easier than it looks: the exponential that appears is a power of the one already found.

### 2.9 The degenerate exponents and the lost solution

> **Lemma (Cases $n=0$ and $n=1$).** If $n=0$ the Bernoulli equation is the linear equation $\frac{dy}{dx}+Py=Q$. If $n=1$ it is separable, and on any interval where $y\neq 0$ its general solution is $y=C e^{\int(Q-P)dx}$.

> **Lemma (The zero solution).** If $n>0$ then $y\equiv 0$ is a solution of the Bernoulli equation. If $n<0$ it is not a solution, and if $n=0$ it is a solution only when $Q\equiv 0$.

For $n>0$ the substitution of $y=0$ gives $0=Q(x)\cdot 0$, which holds identically. For $n<0$ the right-hand side contains $y^{n}=1/y^{|n|}$, which is undefined at $y=0$, so the equation has no meaning there. For $n=0$ the equation at $y=0$ reads $0=Q(x)$, which holds only if the forcing vanishes. This lemma is the reason a complete Bernoulli answer states the zero solution separately when $n>0$.

### 2.10 Asymptotics for constant coefficients

> **Theorem (Constant coefficients).** Let $P=p\neq 0$ and $Q=q$ be constants. Then every solution of $y'+py=q$ has the form
>
> $$
> y(x)=\frac{q}{p}+\left(y_{0}-\frac{q}{p}\right)e^{-p(x-x_{0})},
> $$
>
> and therefore
>
> $$
> \left|y(x)-\frac{q}{p}\right|=\left|y_{0}-\frac{q}{p}\right|e^{-p(x-x_{0})} .
> $$

The quantity $\frac{q}{p}$ is the unique constant solution, obtained by setting the derivative to zero. The theorem says that the distance from the equilibrium decays exponentially at rate $p$ when $p>0$, so the equilibrium is exponentially attracting, and grows exponentially when $p<0$. The estimate is sharp, in the sense that equality holds for every $x$, so no better bound depending only on the initial distance is possible.

### 2.11 The reciprocal-form theorem

> **Theorem (Reciprocal form).** Let $A,B$ be continuous on an interval $J$ of $y$-values, and consider
>
> $$
> \frac{dx}{dy}+A(y)x=B(y).
> $$
>
> Then the general solution is
>
> $$
> x(y)=e^{-\int A\,dy}\left(\int B(y)e^{\int A\,dy}\,dy+C\right).
> $$

The theorem is Theorem 2.3 with the names of the variables exchanged, and its proof requires nothing new. What does require care is the passage from an equation in $\frac{dy}{dx}$ to one in $\frac{dx}{dy}$: the reciprocal relation holds only where $\frac{dy}{dx}\neq 0$, so the resulting family describes the solution curve on arcs where $y$ is a strictly monotone function of $x$. On arcs where $\frac{dy}{dx}=0$ the curve has a horizontal tangent, and those points must be examined separately.

## 3. Formal Proofs, Derivations, and Methods

### 3.1 Derivation of the integrating factor

Let $P$ be continuous on $I$ and define

$$
\mu(x)=\exp\left(\int_{x_{0}}^{x}P(t)\,dt\right),
$$

which is positive and differentiable on $I$, with $\mu(x_{0})=1$. Differentiating by the fundamental theorem of calculus gives

$$
\mu'(x)=P(x)\exp\left(\int_{x_{0}}^{x}P(t)\,dt\right)=P(x)\mu(x).
$$

Now let $y$ be any differentiable function on $I$ and expand the derivative of the product $\mu y$ by the product rule:

$$
\frac{d}{dx}\left(\mu y\right)=\mu\frac{dy}{dx}+\mu' y .
$$

Substituting $\mu'=P\mu$ into the second term gives

$$
\frac{d}{dx}\left(\mu y\right)=\mu\frac{dy}{dx}+\mu P y=\mu\left(\frac{dy}{dx}+Py\right),
$$

which is the identity of Theorem 2.2. The proof has used nothing about $y$, which is exactly the point: the identity holds for every differentiable function, so it may be applied to an unknown function without any prior knowledge of it.

The normalisation claim is now easy. If $\mu_{1}$ and $\mu_{2}$ are positive solutions of $\mu'=P\mu$ on $I$, consider the ratio $\rho=\frac{\mu_{1}}{\mu_{2}}$. Then

$$
\rho'=\frac{\mu_{1}'\mu_{2}-\mu_{1}\mu_{2}'}{\mu_{2}^{2}}=\frac{P\mu_{1}\mu_{2}-\mu_{1}P\mu_{2}}{\mu_{2}^{2}}=0,
$$

so $\rho$ is constant and $\mu_{1}=k\mu_{2}$ with $k>0$. Consequently the choice of antiderivative affects $\mu$ only by a positive constant, and by Lemma 2.1 the solution family is unaffected.

### 3.2 Proof that the integrating factor makes the equation exact

Write the equation as the differential form

$$
\left(Py-Q\right)dx+dy=0,
$$

so that $M=Py-Q$ and $N=1$. The exactness test fails in general, since

$$
\frac{\partial M}{\partial y}=P,\qquad \frac{\partial N}{\partial x}=0,
$$

and these agree only when $P$ vanishes identically. Multiply the form by $\mu$, obtaining the new coefficients

$$
\widetilde{M}=\mu\left(Py-Q\right),\qquad \widetilde{N}=\mu .
$$

Their partial derivatives are

$$
\frac{\partial \widetilde{M}}{\partial y}=\mu P,\qquad \frac{\partial \widetilde{N}}{\partial x}=\mu' ,
$$

and these agree precisely when $\mu'=P\mu$, which is the defining condition of the integrating factor. Hence the multiplied form is exact, and by the exactness criterion there exists a potential $F$ with

$$
\frac{\partial F}{\partial x}=\mu\left(Py-Q\right),\qquad \frac{\partial F}{\partial y}=\mu .
$$

The second equation can be integrated with respect to $y$ at fixed $x$, giving

$$
F(x,y)=\mu(x)\,y+g(x),
$$

because $\mu$ does not depend on $y$. Substituting this expression into the first equation gives

$$
\mu' y+g'(x)=\mu P y-\mu Q .
$$

Using $\mu'=\mu P$, the terms $\mu P y$ cancel from both sides, leaving

$$
g'(x)=-\mu(x)Q(x).
$$

Hence $g(x)=-\int\mu Q\,dx$ and the potential is

$$
F(x,y)=\mu(x)y-\int\mu(x)Q(x)\,dx .
$$

The solutions of an exact form are the level curves $F=c$, so

$$
\mu y-\int\mu Q\,dx=c,
$$

which rearranges to

$$
\mu y=\int\mu Q\,dx+C,
$$

and division by the positive function $\mu$ gives the solution formula of Theorem 2.3. This derivation is worth studying because it explains the otherwise mysterious placement of $\mu$: the factor multiplies $y$ on the left because it is the coefficient $\widetilde{N}$ in the exact form, and it multiplies $Q$ inside the integral because it is what remains of $\widetilde{M}$ after the cancellation.

### 3.3 Proof that the formula gives every solution

Let $P,Q$ be continuous on $I$, fix $x_{0}\in I$, and define

$$
\Phi(x)=y_{0}+\int_{x_{0}}^{x}Q(s)\exp\left(\int_{x_{0}}^{s}P(t)\,dt\right)ds,\qquad y(x)=e^{-\int_{x_{0}}^{x}P(t)\,dt}\,\Phi(x).
$$

Two things must be checked: that $y$ solves the equation with the stated initial condition, and that no other solution exists.

For the first, note that $\Phi$ is differentiable with

$$
\Phi'(x)=Q(x)\exp\left(\int_{x_{0}}^{x}P(t)\,dt\right)=Q(x)\mu(x),
$$

by the fundamental theorem of calculus, and that $\Phi(x_{0})=y_{0}$. Differentiating the product defining $y$ gives

$$
y'=-\mu^{-1}\mu P\,\Phi+\mu^{-1}\Phi'=-Py+\mu^{-1}\mu Q=-Py+Q,
$$

where the last step uses $\Phi'=\mu Q$ and $\mu^{-1}\mu=1$. Hence $y'+Py=Q$. Moreover $y(x_{0})=e^{0}\Phi(x_{0})=y_{0}$, so the initial condition is satisfied.

For the second, let $y_{1}$ and $y_{2}$ be two solutions on $I$ with the same value at $x_{0}$, and put $w=y_{1}-y_{2}$. By linearity,

$$
w'+Pw=\left(y_{1}'+Py_{1}\right)-\left(y_{2}'+Py_{2}\right)=Q-Q=0,
$$

and $w(x_{0})=0$. Multiplying the homogeneous equation by the integrating factor $\mu$ gives

$$
\frac{d}{dx}\left(\mu w\right)=\mu\left(w'+Pw\right)=0,
$$

so $\mu w$ is constant on $I$, and the constant is $\mu(x_{0})w(x_{0})=0$. Since $\mu$ never vanishes, $w=0$ identically, hence $y_{1}=y_{2}$. This proves uniqueness, and it also proves that the general solution is obtained by letting $y_{0}$ vary, since every solution must agree with one member of the family at $x_{0}$.

### 3.4 Derivation of the Bernoulli substitution

Let $n\neq 1$ and suppose $y$ is a solution of

$$
\frac{dy}{dx}+P(x)y=Q(x)y^{n}
$$

on an interval $J$ where $y$ never vanishes. Dividing by $y^{n}$ is then legitimate, and gives

$$
y^{-n}\frac{dy}{dx}+P(x)y^{1-n}=Q(x).
$$

Define $v=y^{1-n}$ on $J$. Because $1-n\neq 0$, the map $y\mapsto v$ is a bijection from the constant-sign interval containing the values of $y$ onto an interval of values of $v$, with inverse $y=v^{1/(1-n)}$. Differentiating $v$ with respect to $x$ by the chain rule gives

$$
\frac{dv}{dx}=(1-n)y^{-n}\frac{dy}{dx},
$$

and since $1-n\neq 0$ this can be solved for the combination appearing in the equation:

$$
y^{-n}\frac{dy}{dx}=\frac{1}{1-n}\frac{dv}{dx}.
$$

Substituting into the divided equation yields

$$
\frac{1}{1-n}\frac{dv}{dx}+P(x)v=Q(x),
$$

and multiplying through by $1-n$, which is a non-zero constant, gives

$$
\frac{dv}{dx}+(1-n)P(x)v=(1-n)Q(x).
$$

This is a first-order linear equation in $v$, and its coefficient $(1-n)P$ and forcing $(1-n)Q$ are continuous because $P$ and $Q$ are. By Theorem 2.3 it has a unique solution for each prescribed value of $v$ at a point, and by the bijectivity of the substitution each such solution corresponds to exactly one solution $y$ of the original equation on $J$. That establishes the bijection asserted in Theorem 2.8.

The reverse direction is worth spelling out, since it is what a check uses. Given a solution $v$ of the linear equation, define $y=v^{1/(1-n)}$ on the interval where $v$ has the sign compatible with the branch. Then $y^{1-n}=v$ and, by the same chain rule applied backwards,

$$
y^{-n}y'=\frac{1}{1-n}v' .
$$

Substituting both into the divided Bernoulli equation returns $Q$, and multiplying by $y^{n}$ returns the original equation. No step has used anything beyond differentiability, so the correspondence is exact.

The integrating factor of the reduced equation is

$$
\exp\left(\int (1-n)P\,dx\right)=\left(\exp\left(\int P\,dx\right)\right)^{1-n}=\mu^{1-n},
$$

which is the corollary of Section 2.8. For $n=2$ it equals $\mu^{-1}$; for $n=3$ it equals $\mu^{-2}$; for $n=-1$ it equals $\mu^{2}$. These are the factors that appear in the worked examples of Section 4.

### 3.5 The degenerate exponents and the division by $y$

The derivation above fails when $n=1$, because then $1-n=0$ and the map $y\mapsto y^{0}=1$ is constant, carrying no information. That case is handled directly. With $n=1$ the equation is

$$
\frac{dy}{dx}+Py=Qy,
$$

which rearranges to $\frac{dy}{dx}=\left(Q-P\right)y$. Dividing by $y$ on an interval where $y\neq 0$ gives

$$
\frac{1}{y}\frac{dy}{dx}=Q-P,
$$

and integrating gives $\ln|y|=\int\left(Q-P\right)dx+k$, hence $y=C e^{\int(Q-P)dx}$ with $C=\pm e^{k}$, together with the zero solution.

The case $n=0$ needs no substitution, since the equation is already linear. It is worth noting, however, that the Bernoulli formula with $n=0$ would give $v=y$ and the reduced equation $v'+Pv=Q$, which is consistent; the formula merely does nothing.

The division by $y^{n}$ deserves a precise statement. On an interval where $y$ has a fixed sign, $y^{n}$ is never zero, so the division is reversible and the transformation is a bijection onto its image. On an interval where $y$ vanishes at some interior point $x_{1}$, the division is invalid at $x_{1}$ and the transformed equation describes the solution only on the two subintervals on either side. The original equation may then have a solution that passes through zero at $x_{1}$, and such a solution is not obtained from the general family. When $n>0$ this is exactly the zero solution and the solutions that touch it, and the lemma of Section 2.9 records it.

### 3.6 Derivation of the reciprocal form

Suppose the equation is given as $\frac{dy}{dx}=f(x,y)$ with $f$ continuous and non-zero on a region. On any arc where $\frac{dy}{dx}\neq 0$, the inverse function theorem applied to $x\mapsto y(x)$ gives

$$
\frac{dx}{dy}=\frac{1}{f(x,y)} .
$$

If the right-hand side can be written as $B(y)-A(y)x$ with $A,B$ continuous, then

$$
\frac{dx}{dy}+A(y)x=B(y),
$$

which is a linear equation with independent variable $y$. Its integrating factor is $\nu(y)=e^{\int A\,dy}$, and Theorem 2.11 gives

$$
x(y)=\nu(y)^{-1}\left(\int B(y)\nu(y)\,dy+C\right).
$$

The solution curve is then described parametrically by this relation between $x$ and $y$, and it may be converted to $y$ as a function of $x$ on any arc where the relation is invertible. The hypothesis $\frac{dy}{dx}\neq 0$ is essential at the derivation step, but the resulting family usually extends across points where $\frac{dy}{dx}=0$ by continuity, and that extension should be checked rather than assumed.

### 3.7 The solution algorithm in definitive form

The algorithm below is the version to use when marks depend on presentation.

1. Rearrange to $\frac{dy}{dx}+Py=Q$. Divide by the coefficient of $\frac{dy}{dx}$ if necessary, and record the points where that coefficient vanishes; these points delimit the intervals on which the answer is claimed.
2. Identify $P$ and $Q$ explicitly as functions, not merely as expressions, and note any points where either fails to be continuous.
3. Compute $\int P\,dx$, choosing the simplest antiderivative and adding no constant.
4. Form $\mu=e^{\int P\,dx}$ and simplify it, using $e^{\ln a}=a$ for $a>0$ and $e^{k\ln a}=a^{k}$.
5. Write $\mu y=\int \mu Q\,dx+C$, evaluate the integral, and divide by $\mu$.
6. If an initial condition is given, either substitute it into the general solution or, preferably, use the definite-integral form with the condition built in.
7. State the interval of validity, then verify by substitution.

Step 4 is where absolute values arise. If $\int P\,dx$ produces $\ln|x|$, then on an interval where $x>0$ the integrating factor simplifies to $x$, and on an interval where $x<0$ it simplifies to $-x$; since the two differ by the constant $-1$, either choice gives the same family, and one may write $\mu=x$ on the positive side and $\mu=-x$ on the negative side. What may not be done is to write $\mu=x$ on an interval that contains both signs, because $x$ is then negative on part of the interval while the exponential is positive.

### 3.8 The verification protocol

Verification has four parts, and a complete answer performs all of them.

First, differentiate the proposed solution and confirm that the derivative is what the differentiation rules give; this catches algebraic slips in the answer itself. Second, form $\frac{dy}{dx}+Py$ and simplify, confirming that all terms involving the arbitrary constant cancel and that the remainder is exactly $Q$. Third, if an initial condition was given, substitute the initial abscissa and confirm the stated value. Fourth, confirm that the answer is defined on the claimed interval, in particular that no denominator vanishes and no logarithm or square root is taken outside its domain.

For a Bernoulli equation the same protocol is applied to the original equation, and the presence of the non-linear power makes the check more informative than usual: if the substitution was wrong, the powers of $y$ will not match, and the failure is visible immediately.

## 4. Representative Worked Examples and Solutions

### 4.1 Problem: solve $\frac{dy}{dx}+2xy=4x$

### 4.2 Solution: a variable coefficient with constant forcing structure

Step 1. The equation is in standard form with $P(x)=2x$ and $Q(x)=4x$. Both are continuous on the whole real line, so the answer will be claimed for all real $x$.

Step 2. Compute the integral of the coefficient.

$$
\int P\,dx=\int 2x\,dx=x^{2}
$$

Step 3. Form the integrating factor.

$$
\mu=e^{x^{2}}
$$

Step 4. Multiply through and recognise the left side as a derivative.

$$
\frac{d}{dx}\left(y e^{x^{2}}\right)=4x e^{x^{2}}
$$

Step 5. Integrate the right-hand side. Since $\frac{d}{dx}\left(2e^{x^{2}}\right)=4xe^{x^{2}}$, the integral is elementary.

$$
y e^{x^{2}}=2e^{x^{2}}+C
$$

Step 6. Divide by the integrating factor.

$$
y=2+C e^{-x^{2}}
$$

Step 7. Verify. With $\frac{dy}{dx}=-2Cxe^{-x^{2}}$ we obtain

$$
\frac{dy}{dx}+2xy=-2Cxe^{-x^{2}}+2x\left(2+Ce^{-x^{2}}\right)=4x ,
$$

so the equation holds for all $x$. Interpret the result: the particular part is the constant $2$, which is the equilibrium of the equation when the coefficient $2x$ is frozen at a typical value, and the homogeneous part decays because the coefficient is positive for $x>0$.

### 4.3 Problem: solve $\frac{dy}{dx}+y\cot x=\csc x$ on $0<x<\pi$

### 4.4 Solution: a trigonometric coefficient

Step 1. In standard form, $P(x)=\cot x$ and $Q(x)=\csc x$. Both are continuous on the interval $0<x<\pi$, where $\sin x>0$.

Step 2. Compute the integral of the coefficient by writing $\cot x$ as a logarithmic derivative.

$$
\int \cot x\,dx=\int\frac{\cos x}{\sin x}\,dx=\ln\left(\sin x\right)
$$

The absolute value is unnecessary on $0<x<\pi$, because $\sin x$ is positive there.

Step 3. Form the integrating factor.

$$
\mu=e^{\ln\left(\sin x\right)}=\sin x
$$

Step 4. Multiply through. The left side becomes the derivative of $y\sin x$, and the right side becomes $\csc x\cdot\sin x=1$.

$$
\frac{d}{dx}\left(y\sin x\right)=1
$$

Step 5. Integrate.

$$
y\sin x=x+C
$$

Step 6. Divide by $\sin x$.

$$
y=\frac{x+C}{\sin x}=x\csc x+C\csc x
$$

Step 7. Verify. Differentiating by the quotient rule,

$$
\frac{dy}{dx}=\frac{\sin x-\left(x+C\right)\cos x}{\sin^{2}x},
$$

and

$$
y\cot x=\frac{\left(x+C\right)\cos x}{\sin^{2}x},
$$

so

$$
\frac{dy}{dx}+y\cot x=\frac{\sin x}{\sin^{2}x}=\frac{1}{\sin x}=\csc x .
$$

The solution is valid on $0<x<\pi$, and it blows up at both endpoints, which is consistent with the coefficient being unbounded there.

### 4.5 Problem: solve $\frac{dy}{dx}+\frac{2x}{1+x^{2}}y=\frac{1}{\left(1+x^{2}\right)^{2}}$

### 4.6 Solution: a coefficient that is an exact logarithmic derivative

Step 1. Read off $P(x)=\frac{2x}{1+x^{2}}$ and $Q(x)=\left(1+x^{2}\right)^{-2}$, both continuous everywhere.

Step 2. Notice that the numerator of $P$ is the derivative of its denominator, so the integral is a logarithm.

$$
\int\frac{2x}{1+x^{2}}\,dx=\ln\left(1+x^{2}\right)
$$

No absolute value is needed, since $1+x^{2}>0$ for all real $x$.

Step 3. Form the integrating factor.

$$
\mu=e^{\ln\left(1+x^{2}\right)}=1+x^{2}
$$

Step 4. Multiply through. The right-hand side simplifies because the two factors cancel.

$$
\frac{d}{dx}\left(y\left(1+x^{2}\right)\right)=\frac{1}{\left(1+x^{2}\right)^{2}}\cdot\left(1+x^{2}\right)=\frac{1}{1+x^{2}}
$$

Step 5. Integrate.

$$
y\left(1+x^{2}\right)=\arctan x+C
$$

Step 6. Divide by $1+x^{2}$.

$$
y=\frac{\arctan x+C}{1+x^{2}}
$$

Step 7. Verify. The derivative is

$$
\frac{dy}{dx}=\frac{\frac{1}{1+x^{2}}\left(1+x^{2}\right)-\left(\arctan x+C\right)2x}{\left(1+x^{2}\right)^{2}}=\frac{1-2x\left(\arctan x+C\right)}{\left(1+x^{2}\right)^{2}},
$$

and

$$
\frac{2x}{1+x^{2}}y=\frac{2x\left(\arctan x+C\right)}{\left(1+x^{2}\right)^{2}},
$$

so the sum is $\left(1+x^{2}\right)^{-2}$, as required. The solution is defined for all real $x$ and tends to zero as $x\to\pm\infty$, because the arctangent is bounded and the denominator grows.

### 4.7 Problem: solve $\frac{dy}{dx}+\frac{1}{x}y=\cos x$ subject to $y(\pi)=1$

### 4.8 Solution: an initial condition at a point away from the origin

Step 1. In standard form, $P(x)=\frac{1}{x}$ and $Q(x)=\cos x$. The coefficient is continuous on $x>0$ and on $x<0$ separately; because the condition is imposed at $x=\pi$, the relevant interval is $x>0$.

Step 2. Compute the integrating factor on $x>0$.

$$
\int\frac{1}{x}\,dx=\ln x, \qquad \mu=e^{\ln x}=x
$$

Step 3. Multiply through.

$$
\frac{d}{dx}\left(xy\right)=x\cos x
$$

Step 4. Integrate by parts with $u=x$ and $dv=\cos x\,dx$, so that $du=dx$ and $v=\sin x$.

$$
\int x\cos x\,dx=x\sin x-\int\sin x\,dx=x\sin x+\cos x
$$

Step 5. Assemble the general solution.

$$
xy=x\sin x+\cos x+C, \qquad y=\sin x+\frac{\cos x+C}{x}
$$

Step 6. Impose the condition at $x=\pi$, where $\sin\pi=0$ and $\cos\pi=-1$.

$$
1=0+\frac{-1+C}{\pi} \quad\text{so}\quad C=\pi+1
$$

Step 7. State the particular solution and verify the condition.

$$
y=\sin x+\frac{\cos x+\pi+1}{x}, \qquad y(\pi)=0+\frac{-1+\pi+1}{\pi}=1
$$

Step 8. Verify the equation. Since

$$
\frac{dy}{dx}=\cos x-\frac{\sin x}{x}-\frac{\cos x+\pi+1}{x^{2}},
$$

adding $\frac{y}{x}=\frac{\sin x}{x}+\frac{\cos x+\pi+1}{x^{2}}$ leaves exactly $\cos x$. The solution is valid on $x>0$.

### 4.9 Problem: solve $\frac{dy}{dx}+2y=x^{2}$

### 4.10 Solution: repeated integration by parts

Step 1. Here $P=2$ and $Q=x^{2}$, both continuous everywhere, so the answer holds for all real $x$.

Step 2. The integrating factor is

$$
\mu=e^{2x}.
$$

Step 3. Multiply through.

$$
\frac{d}{dx}\left(y e^{2x}\right)=x^{2}e^{2x}
$$

Step 4. Integrate by parts twice. First with $u=x^{2}$ and $dv=e^{2x}dx$, so that $du=2x\,dx$ and $v=\frac{1}{2}e^{2x}$.

$$
\int x^{2}e^{2x}\,dx=\frac{1}{2}x^{2}e^{2x}-\int x e^{2x}\,dx
$$

Step 5. Integrate the remaining term by parts with $u=x$ and $dv=e^{2x}dx$.

$$
\int x e^{2x}\,dx=\frac{1}{2}xe^{2x}-\frac{1}{2}\int e^{2x}\,dx=\frac{1}{2}xe^{2x}-\frac{1}{4}e^{2x}
$$

Step 6. Combine the two results.

$$
\int x^{2}e^{2x}\,dx=\frac{1}{2}x^{2}e^{2x}-\frac{1}{2}xe^{2x}+\frac{1}{4}e^{2x}
$$

Step 7. Insert into the product form and divide by $e^{2x}$.

$$
y e^{2x}=e^{2x}\left(\frac{x^{2}}{2}-\frac{x}{2}+\frac{1}{4}\right)+C
$$

$$
y=\frac{x^{2}}{2}-\frac{x}{2}+\frac{1}{4}+C e^{-2x}
$$

Step 8. Verify. Differentiating gives $\frac{dy}{dx}=x-\frac{1}{2}-2Ce^{-2x}$, so

$$
\frac{dy}{dx}+2y=x-\frac{1}{2}-2Ce^{-2x}+x^{2}-x+\frac{1}{2}+2Ce^{-2x}=x^{2},
$$

as required. The particular part is a quadratic with the same leading coefficient pattern as the forcing, and the homogeneous part decays because $P=2>0$.

### 4.11 Problem: solve $\frac{dy}{dx}+y=\frac{e^{-x}}{1+x^{2}}$

### 4.12 Solution: forcing that cancels the integrating factor

Step 1. In standard form, $P=1$ and $Q(x)=\frac{e^{-x}}{1+x^{2}}$, continuous everywhere.

Step 2. The integrating factor is $\mu=e^{x}$.

Step 3. Multiply through; the exponential factors cancel on the right.

$$
\frac{d}{dx}\left(y e^{x}\right)=\frac{e^{-x}}{1+x^{2}}\cdot e^{x}=\frac{1}{1+x^{2}}
$$

Step 4. Integrate, recognising the arctangent.

$$
y e^{x}=\arctan x+C
$$

Step 5. Divide.

$$
y=e^{-x}\left(\arctan x+C\right)
$$

Step 6. Verify. The derivative is

$$
\frac{dy}{dx}=e^{-x}\left(\frac{1}{1+x^{2}}-\arctan x-C\right),
$$

and adding $y=e^{-x}\left(\arctan x+C\right)$ leaves $e^{-x}\left(1+x^{2}\right)^{-1}$, which is the forcing. The example shows that a forcing function which is a multiple of the reciprocal of the integrating factor produces an integral of the unadorned remaining factor, which is often much simpler than the original expression suggests.

### 4.13 Problem: solve $\frac{dy}{dx}-y=4y^{5}$

### 4.14 Solution: a Bernoulli equation with $n=5$

Step 1. Identify $P=-1$, $Q=4$ and $n=5$. Since $n\neq 0,1$, the substitution is required.

Step 2. Divide the equation by $y^{5}$, valid where $y\neq 0$.

$$
y^{-5}\frac{dy}{dx}-y^{-4}=4
$$

Step 3. Put $v=y^{1-5}=y^{-4}$. Then

$$
\frac{dv}{dx}=-4y^{-5}\frac{dy}{dx}, \qquad\text{so}\qquad y^{-5}\frac{dy}{dx}=-\frac{1}{4}\frac{dv}{dx}.
$$

Step 4. Substitute into the divided equation.

$$
-\frac{1}{4}\frac{dv}{dx}-v=4
$$

Step 5. Multiply by $-4$ to reach standard form.

$$
\frac{dv}{dx}+4v=-16
$$

Step 6. Solve the linear equation in $v$. The integrating factor is $e^{4x}$, so

$$
\frac{d}{dx}\left(v e^{4x}\right)=-16e^{4x}.
$$

Step 7. Integrate, using $\int -16e^{4x}dx=-4e^{4x}$.

$$
v e^{4x}=-4e^{4x}+C
$$

Step 8. Divide by $e^{4x}$.

$$
v=-4+C e^{-4x}
$$

Step 9. Translate back with $v=y^{-4}$.

$$
\frac{1}{y^{4}}=Ce^{-4x}-4, \qquad y^{4}=\frac{1}{Ce^{-4x}-4}
$$

Step 10. Verify in the original equation. Let $u=y^{-4}=Ce^{-4x}-4$. Then

$$
\frac{du}{dx}=-4Ce^{-4x}=-4\left(u+4\right),
$$

while differentiating $u=y^{-4}$ gives $\frac{du}{dx}=-4y^{-5}\frac{dy}{dx}$, hence $y^{-5}\frac{dy}{dx}=u+4=y^{-4}+4$. Multiplying the original equation by $y^{-5}$ gives $y^{-5}\frac{dy}{dx}-y^{-4}=4$, which is now confirmed. The zero solution, which was excluded by the division, also satisfies the equation because $n=5>0$.

### 4.15 Problem: solve $\frac{dy}{dx}+y=xy^{3}$

### 4.16 Solution: a Bernoulli equation with $n=3$ and variable forcing

Step 1. Here $P=1$, $Q=x$ and $n=3$, so the substitution is $v=y^{-2}$.

Step 2. Divide by $y^{3}$ on an interval where $y\neq 0$.

$$
y^{-3}\frac{dy}{dx}+y^{-2}=x
$$

Step 3. Differentiate $v=y^{-2}$ to obtain $\frac{dv}{dx}=-2y^{-3}\frac{dy}{dx}$, hence $y^{-3}\frac{dy}{dx}=-\frac{1}{2}\frac{dv}{dx}$.

Step 4. Substitute.

$$
-\frac{1}{2}\frac{dv}{dx}+v=x
$$

Step 5. Clear the fraction.

$$
\frac{dv}{dx}-2v=-2x
$$

Step 6. The coefficient is $-2$ and the forcing is $-2x$, so the integrating factor is $e^{-2x}$ and

$$
\frac{d}{dx}\left(v e^{-2x}\right)=-2x e^{-2x}.
$$

Step 7. Integrate by parts with $u=x$ and $dv=e^{-2x}dx$, so $du=dx$ and $v_{\text{int}}=-\frac{1}{2}e^{-2x}$.

$$
\int x e^{-2x}\,dx=-\frac{1}{2}xe^{-2x}+\frac{1}{2}\int e^{-2x}\,dx=-\frac{1}{2}xe^{-2x}-\frac{1}{4}e^{-2x}
$$

Step 8. Multiply by $-2$ and add the constant.

$$
v e^{-2x}=xe^{-2x}+\frac{1}{2}e^{-2x}+C
$$

Step 9. Divide by $e^{-2x}$.

$$
v=x+\frac{1}{2}+C e^{2x}
$$

Step 10. Translate back.

$$
\frac{1}{y^{2}}=x+\frac{1}{2}+C e^{2x}
$$

Step 11. Verify. Differentiating $v=x+\frac{1}{2}+Ce^{2x}$ gives $v'=1+2Ce^{2x}$, so

$$
v'-2v=1+2Ce^{2x}-2x-1-2Ce^{2x}=-2x,
$$

which is the equation for $v$ and hence, by the derivation of Section 3.4, the original equation is satisfied. The solution is real only where the right-hand side is positive, and $y=0$ is again a solution lost in the division.

### 4.17 Problem: solve $\frac{dy}{dx}+\frac{1}{x}y=\frac{1}{y}$

### 4.18 Solution: a Bernoulli equation with $n=-1$

Step 1. Rewrite the right-hand side as $Qy^{n}$ with $Q=1$ and $n=-1$; the coefficient is $P=\frac{1}{x}$. The negative exponent means the unknown appears in the denominator, so the equation is non-linear and the substitution is needed.

Step 2. Divide by $y^{-1}$, which is the same as multiplying by $y$, on an interval where $y\neq 0$.

$$
y\frac{dy}{dx}+\frac{1}{x}y^{2}=1
$$

Step 3. Put $v=y^{1-(-1)}=y^{2}$. Then $\frac{dv}{dx}=2y\frac{dy}{dx}$, so $y\frac{dy}{dx}=\frac{1}{2}\frac{dv}{dx}$.

Step 4. Substitute.

$$
\frac{1}{2}\frac{dv}{dx}+\frac{1}{x}v=1
$$

Step 5. Multiply by $2$ to reach standard form.

$$
\frac{dv}{dx}+\frac{2}{x}v=2
$$

Step 6. The integrating factor is $e^{\int\frac{2}{x}dx}=e^{2\ln x}=x^{2}$ on $x>0$, so

$$
\frac{d}{dx}\left(v x^{2}\right)=2x^{2}.
$$

Step 7. Integrate.

$$
v x^{2}=\frac{2x^{3}}{3}+C
$$

Step 8. Divide.

$$
v=\frac{2x}{3}+\frac{C}{x^{2}}
$$

Step 9. Translate back to $y$.

$$
y^{2}=\frac{2x}{3}+\frac{C}{x^{2}}
$$

Step 10. Verify. With $v=\frac{2x}{3}+Cx^{-2}$ we have $v'=\frac{2}{3}-2Cx^{-3}$ and $\frac{2v}{x}=\frac{4}{3}+2Cx^{-3}$, so $v'+\frac{2v}{x}=2$. By the reduction theorem this is equivalent to the original equation on the region where $y\neq 0$. The solution is real only where $\frac{2x}{3}+\frac{C}{x^{2}}\ge 0$.

### 4.19 Problem: solve $\frac{dy}{dx}+y=\sqrt{y}$

### 4.20 Solution: a Bernoulli equation with a fractional exponent

Step 1. The equation is Bernoulli with $P=1$, $Q=1$ and $n=\frac{1}{2}$. Then $1-n=\frac{1}{2}$, so the substitution is $v=y^{1/2}$.

Step 2. Divide by $y^{1/2}$ on an interval where $y>0$, which is required for the square root to be real and differentiable.

$$
y^{-1/2}\frac{dy}{dx}+y^{1/2}=1
$$

Step 3. Since $v=y^{1/2}$, we have $\frac{dv}{dx}=\frac{1}{2}y^{-1/2}\frac{dy}{dx}$, hence $y^{-1/2}\frac{dy}{dx}=2\frac{dv}{dx}$.

Step 4. Substitute.

$$
2\frac{dv}{dx}+v=1
$$

Step 5. Divide by $2$ to reach standard form.

$$
\frac{dv}{dx}+\frac{1}{2}v=\frac{1}{2}
$$

Step 6. The integrating factor is $e^{x/2}$, so

$$
\frac{d}{dx}\left(v e^{x/2}\right)=\frac{1}{2}e^{x/2}.
$$

Step 7. Integrate, using $\int\frac{1}{2}e^{x/2}dx=e^{x/2}$.

$$
v e^{x/2}=e^{x/2}+C
$$

Step 8. Divide by $e^{x/2}$.

$$
v=1+C e^{-x/2}
$$

Step 9. Translate back.

$$
\sqrt{y}=1+C e^{-x/2}, \qquad y=\left(1+C e^{-x/2}\right)^{2}
$$

Step 10. Verify, remembering that $\sqrt{y}=\left|1+Ce^{-x/2}\right|$ and choosing the branch on which $1+Ce^{-x/2}>0$. Put $u=1+Ce^{-x/2}$, so that $y=u^{2}$ and $\frac{dy}{dx}=2u\left(-\frac{C}{2}e^{-x/2}\right)=-Cu e^{-x/2}$. Then

$$
\frac{dy}{dx}+y=-Cu e^{-x/2}+u^{2}=u\left(u-Ce^{-x/2}\right)=u=\sqrt{y},
$$

which confirms the equation on that branch. On the other branch the same calculation produces $-\sqrt{y}$, and those solutions belong to the equation with the sign of the forcing reversed.

### 4.21 Problem: solve $\frac{dy}{dx}=\frac{y}{x+y^{2}}$

### 4.22 Solution: linear after exchanging the variables

Step 1. The right-hand side has $x$ and $y^{2}$ in the denominator, so the equation is not linear in $y$ and no power of $y$ alone multiplies a linear left-hand side.

Step 2. Take reciprocals, valid where $\frac{dy}{dx}\neq 0$.

$$
\frac{dx}{dy}=\frac{x+y^{2}}{y}=\frac{x}{y}+y
$$

Step 3. Rearrange into standard form with $x$ as the unknown.

$$
\frac{dx}{dy}-\frac{1}{y}x=y
$$

Step 4. Identify $A(y)=-\frac{1}{y}$ and $B(y)=y$, and compute the integrating factor on $y>0$.

$$
e^{\int -\frac{1}{y}\,dy}=e^{-\ln y}=\frac{1}{y}
$$

Step 5. Multiply through; the left side becomes a derivative with respect to $y$.

$$
\frac{d}{dy}\left(\frac{x}{y}\right)=1
$$

Step 6. Integrate with respect to $y$.

$$
\frac{x}{y}=y+C
$$

Step 7. Multiply by $y$.

$$
x=y^{2}+Cy
$$

Step 8. Verify. Differentiating with respect to $y$ gives $\frac{dx}{dy}=2y+C$, and

$$
\frac{x}{y}+y=\frac{y^{2}+Cy}{y}+y=y+C+y=2y+C,
$$

so the transformed equation holds. Hence the family $x=y^{2}+Cy$ solves the original equation on arcs where $y$ is a monotone function of $x$.

### 4.23 Problem: solve $\frac{dy}{dx}=\frac{1}{x+y^{2}}$

### 4.24 Solution: a reciprocal form needing integration by parts

Step 1. The equation is not linear in $y$; the unknown appears squared inside the denominator.

Step 2. Take reciprocals, valid where $\frac{dy}{dx}\neq 0$.

$$
\frac{dx}{dy}=x+y^{2}
$$

Step 3. Rearrange.

$$
\frac{dx}{dy}-x=y^{2}
$$

Step 4. Identify $A(y)=-1$ and $B(y)=y^{2}$, so the integrating factor is

$$
e^{\int(-1)\,dy}=e^{-y}.
$$

Step 5. Multiply through.

$$
\frac{d}{dy}\left(x e^{-y}\right)=y^{2}e^{-y}
$$

Step 6. Integrate by parts twice. With $u=y^{2}$ and $dv=e^{-y}dy$ we get $du=2y\,dy$ and $v_{\text{int}}=-e^{-y}$, so

$$
\int y^{2}e^{-y}\,dy=-y^{2}e^{-y}+2\int y e^{-y}\,dy .
$$

Step 7. Integrate the remaining term by parts with $u=y$ and $dv=e^{-y}dy$.

$$
\int y e^{-y}\,dy=-ye^{-y}+\int e^{-y}\,dy=-ye^{-y}-e^{-y}
$$

Step 8. Combine.

$$
\int y^{2}e^{-y}\,dy=-y^{2}e^{-y}-2ye^{-y}-2e^{-y}
$$

Step 9. Insert into the product form and divide by $e^{-y}$.

$$
x e^{-y}=-e^{-y}\left(y^{2}+2y+2\right)+C
$$

$$
x=-\left(y^{2}+2y+2\right)+C e^{y}
$$

Step 10. Verify. Differentiating with respect to $y$ gives

$$
\frac{dx}{dy}=-\left(2y+2\right)+Ce^{y},
$$

and

$$
x+y^{2}=-\left(y^{2}+2y+2\right)+Ce^{y}+y^{2}=-\left(2y+2\right)+Ce^{y},
$$

so the two sides agree, and the transformed equation is satisfied. The family describes the solution curves with $x$ as a function of $y$, valid on arcs where the original derivative is finite and non-zero.

### 4.25 Problem: solve $\frac{dy}{dx}+y\tan x=0$ on $-\frac{\pi}{2}<x<\frac{\pi}{2}$

### 4.26 Solution: the homogeneous case with a variable coefficient

Step 1. Here $Q(x)=0$, so the equation is homogeneous. The integrating factor is computed exactly as in the non-homogeneous case.

$$
\int\tan x\,dx=-\ln\left(\cos x\right), \qquad \mu=e^{-\ln\left(\cos x\right)}=\sec x
$$

The simplification uses the fact that $\cos x>0$ on the stated interval, so no absolute value is required.

Step 2. Multiply through; the right-hand side stays zero.

$$
\frac{d}{dx}\left(y\sec x\right)=0
$$

Step 3. Integrate once.

$$
y\sec x=C
$$

Step 4. Multiply by $\cos x$.

$$
y=C\cos x
$$

Step 5. Check. The derivative is $\frac{dy}{dx}=-C\sin x$, and

$$
\frac{dy}{dx}+y\tan x=-C\sin x+C\cos x\cdot\frac{\sin x}{\cos x}=0,
$$

so the equation holds on the whole interval. The result also agrees with the general lemma: the homogeneous solution is $Ce^{-\int P\,dx}=Ce^{\ln\left(\cos x\right)}=C\cos x$.

The example matters because the same calculation supplies the complementary function for every equation with the same coefficient. If the forcing were $\sec x$ rather than zero, the product form would read $\frac{d}{dx}\left(y\sec x\right)=\sec^{2}x$, and integrating would give $y\sec x=\tan x+C$, that is $y=\sin x+C\cos x$.

### 4.27 Problem: solve $\frac{dy}{dx}+3y=12$ with $y(0)=-1$

### 4.28 Solution: constant coefficient and constant forcing

Step 1. Both $P=3$ and $Q=12$ are constants, so the equilibrium value is $\frac{Q}{P}=4$ and the solution is expected to be that constant plus a decaying exponential.

Step 2. The integrating factor is $e^{3x}$, so

$$
\frac{d}{dx}\left(y e^{3x}\right)=12e^{3x}.
$$

Step 3. Integrate, using $\int 12e^{3x}dx=4e^{3x}$.

$$
y e^{3x}=4e^{3x}+C, \qquad y=4+C e^{-3x}
$$

Step 4. Impose the condition at $x=0$.

$$
-1=4+C \quad\Longrightarrow\quad C=-5
$$

Step 5. State the solution and verify both the equation and the condition.

$$
y=4-5e^{-3x}, \qquad y(0)=4-5=-1
$$

Since $\frac{dy}{dx}=15e^{-3x}$, we get

$$
\frac{dy}{dx}+3y=15e^{-3x}+12-15e^{-3x}=12,
$$

so the equation holds for all $x$. The solution increases from $-1$ towards the equilibrium $4$, which it approaches exponentially at rate $3$, in agreement with the asymptotic theorem of Section 2.10.

## 5. Mathematical Extensions, Limits, and Common Errors

### 5.1 Singular points of the coefficients and maximal intervals

The theorem of existence and uniqueness is local in appearance only: it gives a solution on the whole interval on which $P$ and $Q$ are continuous. When one of them fails to be continuous at a point, that point must be removed, and the solution is then claimed on the largest interval of continuity containing the initial abscissa. The point removed is a singular point of the coefficient, not necessarily a point where the solution fails, but in practice the solution usually does fail there.

A simple illustration is the equation

$$
\frac{dy}{dx}+\frac{1}{x}y=1
$$

with the initial condition $y(1)=0$. The coefficient is continuous on $x>0$ and on $x<0$ but not across the origin. Solving by the integrating factor $x$ gives $xy=x^{2}-1$, that is $y=x-\frac{1}{x}$, which indeed blows up as $x\to 0^{+}$. The solution exists on the maximal interval $x>0$, and it cannot be continued through the origin, so a claim that the solution holds for all $x\neq 0$ would be false.

A second illustration shows that the interval is not always limited by a blow-up of the solution. The equation

$$
\frac{dy}{dx}+y=\frac{1}{1+x^{2}}
$$

has a coefficient that is continuous everywhere, so its solution exists for all real $x$. An equation whose coefficient contains $\ln x$ or $\sqrt{x}$ restricts the interval to $x>0$ from the outset, because the coefficient itself is not defined on the whole line. In each case the rule is the same: the interval of the answer is the largest interval of continuity of the coefficients that contains the data.

### 5.2 Resonance and repeated factors

When the forcing function is a constant multiple of the homogeneous solution, the integral in the solution formula produces a factor of $x$ rather than another exponential. Take $P=1$ and $Q=e^{-x}$, so that the homogeneous solution is $e^{-x}$ and the forcing is exactly that function. Then $\mu=e^{x}$ and

$$
y e^{x}=\int e^{x}e^{-x}\,dx=\int 1\,dx=x+C,
$$

so

$$
y=e^{-x}\left(x+C\right).
$$

The general rule is that if $Q=ke^{-\int P\,dx}$ then the solution contains $kxe^{-\int P\,dx}$ in place of a constant multiple of the homogeneous solution. This is the first-order analogue of the resonant case in the theory of second-order linear equations, and the mechanism is identical: the forcing is tuned to the natural mode of the system, so its effect accumulates linearly instead of cancelling.

A mixed example combines resonance with a genuine integration. For

$$
\frac{dy}{dx}+y=xe^{-x},
$$

the integrating factor is $e^{x}$ and the right-hand side of the product form is $x$, so

$$
y e^{x}=\frac{x^{2}}{2}+C, \qquad y=e^{-x}\left(\frac{x^{2}}{2}+C\right).
$$

Substitution confirms the answer: the derivative is $e^{-x}\left(x-\frac{x^{2}}{2}-C\right)$, and adding $y$ leaves $xe^{-x}$. The lesson is that resonance does not make the equation harder; it makes the integral easier, because the exponential factor disappears.

### 5.3 Connections with the logistic equation and with Riccati equations

The Bernoulli equation with $n=2$ and constant coefficients is the logistic equation. In the form

$$
\frac{dy}{dx}=ay-by^{2}
$$

with $a,b>0$ constants, the substitution $v=y^{-1}$ gives

$$
\frac{dv}{dx}+av=b,
$$

whose solution is $v=\frac{b}{a}+Ce^{-ax}$, hence

$$
y=\frac{1}{\frac{b}{a}+Ce^{-ax}}=\frac{a}{b+Ka e^{-ax}}
$$

for a constant $K$. This function increases from a small positive value towards the carrying capacity $\frac{a}{b}$ and is the standard model of a population with unlimited resources at small size and competition at large size. The Bernoulli substitution is therefore not a trick confined to exercises; it is the standard route from the logistic model to an explicit formula.

The Bernoulli equation with $n=2$ is also a special case of a Riccati equation, which has the general form

$$
\frac{dy}{dx}=A(x)+B(x)y+C(x)y^{2}.
$$

A Riccati equation cannot in general be solved by quadratures, but if one particular solution $y_{1}$ is known, the substitution $y=y_{1}+\frac{1}{u}$ linearises it. The Bernoulli case is the special Riccati equation in which $A=0$, and for that case the particular solution $y=0$ is known, so the substitution $y=\frac{1}{u}$ is exactly the Bernoulli substitution. This is the structural reason why Bernoulli equations are solvable while general Riccati equations are not: the missing constant term supplies a known solution.

### 5.4 What fails when continuity is dropped

For the linear equation continuity of $P$ and $Q$ is enough for uniqueness, and no condition on the derivative with respect to $y$ is required. For a non-linear equation that is not the case, and the contrast is instructive. The equation

$$
\frac{dy}{dx}=2\sqrt{|y|}, \qquad y(0)=0
$$

has the zero solution and also the solution $y=x^{2}$ for $x\ge 0$, and infinitely many others obtained by waiting before starting. The right-hand side is continuous but not Lipschitz in $y$, and uniqueness fails. A linear equation can never behave this way: its right-hand side $Q-Py$ is Lipschitz in $y$ with constant $\max|P|$ on any bounded interval, because the dependence on $y$ is linear.

The practical consequence is that a linear initial-value problem has exactly one answer, so any two correct-looking solutions must be the same function. If a check produces two different expressions, at least one of them contains an algebraic error, and no appeal to a second branch is available.

### 5.5 Absolute values, logarithms, and the sign of the interval

The integration of $\frac{1}{x}$ produces $\ln|x|$, and the subsequent exponential produces $|x|$. Students often write $x$ without comment, which is correct only on a positive interval. The correct statement is that the integrating factor is $|x|$, and that on an interval of fixed sign one may replace $|x|$ by $x$ or by $-x$, since the two differ by the constant factor $-1$ and the solution family is unchanged.

The same care is needed with $P=\tan x$. Since

$$
\int\tan x\,dx=-\ln\left|\cos x\right|,
$$

the integrating factor is $\left|\cos x\right|^{-1}$, and on an interval where $\cos x>0$ it is $\sec x$. A solution derived as $y\sec x=\int Q\sec x\,dx+C$ is therefore valid on any interval between consecutive zeros of the cosine, and the answer must name such an interval.

A third source of sign trouble is the Bernoulli substitution with a fractional exponent. The identity $\left(y^{2}\right)^{1/2}=|y|$ means that solving for $y$ from $v^{2}=y^{2}$ introduces two branches, and only one of them satisfies the original equation when the right-hand side is a square root. The branch must be selected from the equation, not from convenience.

### 5.6 Limiting behaviour and periodic forcing

The constant-coefficient theorem of Section 2.10 describes the limit of the solution as $x\to\infty$ when the forcing is constant. When the forcing is periodic, the solution also settles into a periodic response, and the transient is the homogeneous part. For the equation

$$
\frac{dy}{dx}+y=\sin x,
$$

the integrating factor is $e^{x}$, and the product form is

$$
\frac{d}{dx}\left(ye^{x}\right)=e^{x}\sin x .
$$

Since $\int e^{x}\sin x\,dx=\frac{e^{x}}{2}\left(\sin x-\cos x\right)$, the general solution is

$$
y=\frac{1}{2}\left(\sin x-\cos x\right)+Ce^{-x}.
$$

The first term is periodic with the same frequency as the forcing, and the second decays. As $x\to\infty$ the solution approaches the periodic term regardless of the initial state, which is the phenomenon of a stable steady-state oscillation. The amplitude $\frac{1}{\sqrt{2}}$ of that term is smaller than the amplitude of the forcing, and the phase is shifted; both facts follow from the algebra of the integral.

These asymptotic statements are limits in the ordinary sense, and they require $p>0$ in the constant-coefficient case. When $p<0$ no such limit exists, because the homogeneous part grows and dominates every bounded particular solution.

### 5.7 A consolidated table of errors

| Error | What goes wrong | Correction |
| --- | --- | --- |
| Using $e^{P}$ as the factor | The factor does not satisfy $\mu'=P\mu$ unless $P$ is constant | Compute $\int P\,dx$ first, then exponentiate |
| Forgetting to divide by the coefficient of the derivative | The coefficient used for $P$ is wrong, so the factor is wrong | Write the equation in standard form before identifying $P$ |
| Integrating $Q$ alone | The product form requires $\int \mu Q\,dx$, not $\mu\int Q\,dx$ | Multiply the forcing by $\mu$ inside the integral |
| Adding a constant inside the exponent of $\mu$ | The constant cancels and can be double counted later | Use the simplest antiderivative of $P$ |
| Omitting the constant after integrating | The family loses a parameter and cannot fit general data | Write $+C$ at the integration step |
| Dividing by $y^{n}$ without a restriction | The solution is asserted where the division is invalid | State $y\neq 0$ and record the interval |
| Losing $y=0$ in a Bernoulli problem with $n>0$ | The answer is incomplete | Add the zero solution explicitly |
| Dropping the factor $1-n$ | The reduced equation has the wrong coefficient of $v$ | Differentiate $v=y^{1-n}$ carefully and carry the factor |
| Applying the substitution with $n=1$ | The variable $v$ collapses to a constant | Solve the separable equation instead |
| Reporting a formula with no interval | The answer is false across a singularity | Name the largest interval of continuity |
| Checking in the reduced equation only | An error in the substitution survives the check | Substitute into the original equation |

### 5.8 The limits of the method

The method of integrating factors solves every first-order linear equation, and it solves every equation that a substitution can bring to that form. It does not solve equations in which the unknown appears non-linearly in a way that no substitution removes, such as $y'+\sin y=x$ or $y'=x^{2}+y^{3}$; such equations require numerical or qualitative methods. It does not solve equations in which the coefficient of $y'$ vanishes identically, because then the equation is not a differential equation for $y$ at all but an algebraic constraint. And it does not, by itself, produce solutions beyond a singular point of the coefficients, because the formula is derived under a continuity hypothesis that fails there.

Within those limits, however, the method is complete and exact. The integrating factor is not an approximation, the solution formula is an identity, and the initial-value problem has exactly one solution. That combination of generality and explicitness is unusual in the theory of differential equations, and it is the reason the linear first-order equation is the model against which every other solvable class is measured.
