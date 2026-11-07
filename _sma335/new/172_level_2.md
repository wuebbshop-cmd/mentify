## 1. Foundational Concepts, Definitions, and Axioms

### 1.1 The two normal forms of a first-order equation

A first-order ordinary differential equation in two variables may be presented in derivative form,

$$
\frac{dy}{dx} = f(x,y),
$$

or in differential form,

$$
M(x,y)\,dx + N(x,y)\,dy = 0 .
$$

The two presentations carry the same information on any region where $N \neq 0$, since dividing the differential form by $N\,dx$ returns $\frac{dy}{dx} = -M/N$ with $f = -M/N$. The differential form is often the more flexible of the two, because it does not force a decision about which variable is the independent one and because both coefficients enter symmetrically. Every method in this topic can be applied in either form, and a good working habit is to move to whichever form makes the structure visible.

Throughout, $y$ denotes the unknown function, $x$ the independent variable, and primes or the operator notation denote differentiation with respect to $x$. A solution on an interval $I$ is a differentiable function $y = \phi(x)$ for which the substitution of $\phi$ and $\phi'$ produces an identity on $I$. A general solution of a first-order equation carries exactly one arbitrary constant, and a particular solution is a member of that one-parameter family selected by a prescribed condition.

### 1.2 Separable equations

> **Definition (Separable equation).** The first-order equation $\frac{dy}{dx} = f(x,y)$ is separable on a rectangle $R$ if there exist functions $p$ of $x$ alone and $q$ of $y$ alone such that
>
> $$
> f(x,y) = p(x)\,q(y)
> $$
>
> for every point of $R$.

The definition is a statement about the algebraic shape of the right-hand side, not about the variables themselves. The word separable refers to the fact that the dependence on $x$ and the dependence on $y$ occur in separate multiplicative factors, so that the equation can be rearranged into a form in which one side contains only $x$ and the other only $y$.

Equivalently, and in the notation most often used in practice, a separable equation is one that can be written as

$$
g(y)\,\frac{dy}{dx} = h(x),
$$

where $g = 1/q$ and $h = p$ on the region where $q \neq 0$. The passage between the two descriptions is purely algebraic.

Two warnings belong here, because both are the source of most lost marks in this topic. First, not every function of two variables factors. The function $x^{2}+y^{2}$ does not factor into a function of $x$ times a function of $y$, and neither does $x+y$; an equation whose right-hand side is one of these is not separable no matter how it is rearranged. Second, a function that appears to mix the variables may still be separable after simplification: the quotient

$$
\frac{xy^{2}+x}{yx^{2}+y} = \frac{x\left(1+y^{2}\right)}{y\left(1+x^{2}\right)}
$$

mixes the variables in its written form but factors once the common terms are collected, so the equation $\frac{dy}{dx} = \frac{xy^{2}+x}{yx^{2}+y}$ is separable. Factorisation is the test, and it must be attempted before separability is denied.

### 1.3 Homogeneous functions of a given degree

> **Definition (Homogeneous function).** A function $f$ of two variables is homogeneous of degree $n$ on a region closed under scaling if
>
> $$
> f(kx,ky) = k^{n}f(x,y)
> $$
>
> for every admissible point $(x,y)$ and every admissible scale factor $k$.

The scale factor $k$ is a positive number, so that the scaled point $(kx,ky)$ moves along the ray from the origin through $(x,y)$ without crossing the origin. The exponent $n$ need not be a positive integer; it may be zero, negative, or fractional, provided the powers are defined on the region under consideration. What matters is that one single exponent works for all points and all scales. This single-exponent requirement is the whole content of the definition.

Three worked identifications make the test concrete.

For $f(x,y) = x^{2}+3xy$, replacing $x$ by $kx$ and $y$ by $ky$ gives

$$
f(kx,ky) = k^{2}x^{2} + 3k^{2}xy = k^{2}\left(x^{2}+3xy\right) = k^{2}f(x,y),
$$

so the degree is two, the exponent carried by every term.

For $f(x,y) = \frac{xy}{x^{2}+y^{2}}$, the same replacement gives

$$
f(kx,ky) = \frac{k^{2}xy}{k^{2}x^{2}+k^{2}y^{2}} = \frac{k^{2}xy}{k^{2}\left(x^{2}+y^{2}\right)} = \frac{xy}{x^{2}+y^{2}} = k^{0}f(x,y),
$$

so the degree is zero. The two powers of $k$ cancel because numerator and denominator are homogeneous of the same degree.

For $f(x,y) = x + y^{2}$ the replacement gives $kx + k^{2}y^{2}$, and no single power of $k$ can be extracted from that expression, since the two terms demand different exponents. The function is therefore not homogeneous at all, and it is important to say so rather than to assign it a degree.

A convenient bookkeeping rule follows immediately from the definition: a polynomial is homogeneous of degree $n$ precisely when every one of its terms has total degree $n$. Thus $x^{3}+y^{3}$ has degree three, $x^{2}y - 2xy^{2}$ has degree three, and $x^{3}+y^{2}$ has no degree.

### 1.4 Homogeneous equations of the first order

> **Definition (Homogeneous equation).** The first-order equation $\frac{dy}{dx} = f(x,y)$ is homogeneous if $f$ is homogeneous of degree zero, that is if
>
> $$
> f(kx,ky) = f(x,y)
> $$
>
> for every admissible point and every admissible scale factor $k$.

The condition is degree zero and not degree $n$, and the reason is structural rather than conventional. A first-order equation relates a slope to a position. Slopes are unchanged when the whole plane is scaled about the origin, because scaling multiplies both the rise and the run by the same factor. An equation whose right-hand side also survives scaling unchanged is therefore an equation of the same type at every distance from the origin: the direction field it defines is constant along each ray. That ray-invariance is exactly what the substitution $y = vx$ exploits.

> **Definition (Homogeneous equation in differential form).** The equation
>
> $$
> M(x,y)\,dx + N(x,y)\,dy = 0
> $$
>
> is homogeneous if $M$ and $N$ are homogeneous functions of the same degree.

The two definitions agree, and the agreement is the content of the next theorem. The practical test is worth stating separately because it is the one used most often in exercises.

> **Test (The $M\,dx + N\,dy$ test).** Compute the degree of $M$ and the degree of $N$ separately. If both exist and are equal, the equation is homogeneous. If the two degrees differ, the equation is not homogeneous.

The word separately matters. The equation $(x^{3}+y^{3})\,dx - 3xy^{2}\,dy = 0$ has $M = x^{3}+y^{3}$ of degree three and $N = -3xy^{2}$ of degree three, so it passes the test. The equation $(x^{2}+y)\,dx + xy\,dy = 0$ has $M$ of no degree at all, so it fails immediately, and no amount of algebra will repair it.

### 1.5 Equations reducible to homogeneous form

The last family in this topic consists of equations whose right-hand side is a quotient of two linear expressions,

$$
\frac{dy}{dx} = \frac{ax+by+c}{px+qy+r},
$$

with $a,b,c,p,q,r$ constants and at least one of $a,b$ and one of $p,q$ non-zero. Such a quotient is generally not homogeneous, because the constant terms $c$ and $r$ break the scaling: replacing $x$ by $kx$ and $y$ by $ky$ changes $ax+by+c$ into $k(ax+by)+c$, which is not a multiple of the original unless $c = 0$.

The family splits into two cases according to the coefficient vectors $(a,b)$ and $(p,q)$.

> **Definition (The two reducible cases).** Let $D = aq - bp$ be the determinant of the coefficient matrix. If $D \neq 0$ the two straight lines $ax+by+c=0$ and $px+qy+r=0$ meet in a single point, and the equation is said to be of intersecting type. If $D = 0$ the two lines are parallel or coincident, and the equation is said to be of parallel type.

The two cases require different substitutions, and the criterion that decides between them is the single number $D = aq-bp$. The phrase "ratio of the coefficients of $x$ equals the ratio of the coefficients of $y$" is the informal version of the same test, since $a/p = b/q$ is equivalent to $aq = bp$ whenever the denominators are non-zero.

### 1.6 Declared notation for the substitutions

Four symbols are introduced by the methods and must be declared before use, because confusing them with the original variables is a common error.

The symbol $v$ always denotes the ratio $y/x$ in the substitution $y = vx$ for a homogeneous equation; it is a function of $x$, not a constant. The symbol $z$ denotes the combination $ax+by$ in the parallel case; it too is a function of $x$. The capital letters $X$ and $Y$ denote the translated coordinates $X = x-h$ and $Y = y-k$ in the intersecting case, and $h$ and $k$ are the constants locating the point of intersection of the two lines. Keeping these four letters distinct from $x$ and $y$ prevents the single most frequent algebraic slip in the topic, which is to treat $v$ as a constant while differentiating.

### 1.7 The arbitrary constant and the logarithmic device

Every solution produced here ends with one arbitrary constant, because exactly one integration is performed. Two conventions about that constant are legitimate and worth understanding rather than memorising.

The first is that a constant may be relabelled at any stage: replacing $C$ by $3C$, by $C/2$, or by $C-10$ changes nothing, because the set of values taken by the symbol is the same set of real numbers. This freedom is what allows the final answer to be tidied into a polynomial relation.

The second concerns equations whose integration produces logarithms. When the answer reads $\ln|y| = \ln|x| + C$, it is convenient to write $C = \ln A$ with $A>0$ and then to combine the logarithms. The replacement is legitimate because the logarithm maps the positive reals onto the whole real line, so every real constant is the logarithm of some positive constant. The device reduces two logarithmic terms to one and frequently turns the answer into a simple algebraic relation.

## 2. Theorems, Lemmas, and Analytical Properties

### 2.1 Elementary algebra of homogeneous functions

> **Lemma 2.1 (Products, quotients and sums).** Let $f$ be homogeneous of degree $m$ and $g$ homogeneous of degree $n$ on a common region. Then $fg$ is homogeneous of degree $m+n$, the quotient $f/g$ is homogeneous of degree $m-n$ wherever $g \neq 0$, and the sum $f+g$ is homogeneous of degree $m$ whenever $m = n$.

**Proof.** For the product, substituting the scaled point gives

$$
(fg)(kx,ky) = f(kx,ky)\,g(kx,ky) = k^{m}f(x,y)\cdot k^{n}g(x,y) = k^{m+n}(fg)(x,y).
$$

For the quotient, the same computation gives $k^{m}/k^{n} = k^{m-n}$ as the surviving factor. For the sum with $m = n$,

$$
(f+g)(kx,ky) = k^{m}f(x,y) + k^{m}g(x,y) = k^{m}(f+g)(x,y).
$$

The hypothesis $m = n$ cannot be dropped from the sum: if $f$ has degree two and $g$ has degree three, the sum $k^{2}f + k^{3}g$ admits no common factor of the required kind. This is precisely why a polynomial such as $x^{3}+y^{2}$ has no degree. $\square$

### 2.2 Degree zero is dependence on a single ratio

> **Theorem 2.2 (Ratio representation).** Let $f$ be homogeneous of degree zero on a region containing the points $(x,y)$ with $x>0$. Then there is a function $F$ of one variable such that
>
> $$
> f(x,y) = F\!\left(\frac{y}{x}\right)
> $$
>
> for all such points, namely $F(v) = f(1,v)$.

**Proof.** Fix a point with $x>0$. Apply the definition of homogeneity with the positive scale factor $k = 1/x$. Then

$$
f(x,y) = f\!\left(x\cdot 1,\; x\cdot \frac{y}{x}\right) = x^{0} f\!\left(1,\frac{y}{x}\right) = F\!\left(\frac{y}{x}\right).
$$

The scale factor is positive, which is why the argument is restricted to $x>0$; on the left half-plane the same conclusion is obtained by writing $k = -1/x$ and using the ratio $y/x$ with its sign, and the two halves agree on the formulas produced in every example of this topic. $\square$

The theorem is the mechanism of the whole method. It says that a homogeneous equation is not really an equation in two independent quantities at all: along each ray through the origin the right-hand side is constant, so the equation constrains only the ratio $y/x$. The substitution $y = vx$ rewrites the equation in terms of exactly that ratio, and that is why it must succeed.

### 2.3 The $M\,dx + N\,dy$ test justified

> **Theorem 2.3 (Equivalence of the two definitions).** Let $M$ and $N$ be homogeneous of the same degree $n$, with $N \neq 0$ on the region. Then the equation $M\,dx + N\,dy = 0$ is homogeneous in the sense of Definition 1.4.

**Proof.** On the region where $N \neq 0$ the equation is equivalent to

$$
\frac{dy}{dx} = -\frac{M(x,y)}{N(x,y)} .
$$

By Lemma 2.1 the quotient of two homogeneous functions of the same degree $n$ is homogeneous of degree $n-n = 0$. Hence the right-hand side is homogeneous of degree zero, which is the definition. $\square$

The converse also holds in the useful direction: if the degrees of $M$ and $N$ differ by a non-zero amount $m-n$, the quotient has degree $m-n \neq 0$ and the equation fails the degree-zero test. This is the justification for reading the degrees of $M$ and $N$ off separately and comparing them, which is the fastest available test in an examination.

### 2.4 The substitution $y = vx$ converts a homogeneous equation to a separable one

> **Lemma 2.4 (Derivative under the substitution).** If $v$ is differentiable and $y = vx$, then
>
> $$
> \frac{dy}{dx} = v + x\frac{dv}{dx} .
> $$

**Proof.** Apply the product rule to $y = v\cdot x$, treating $v$ as a function of $x$:

$$
\frac{dy}{dx} = \frac{dv}{dx}\cdot x + v\cdot 1 = v + x\frac{dv}{dx} .
$$

$\square$

The lemma is where the error of treating $v$ as a constant is punished: if $v$ were constant the derivative would be $v$, the term $x\frac{dv}{dx}$ would vanish, and the resulting equation would be an identity rather than a differential equation.

> **Theorem 2.5 (Reduction theorem).** Let $F$ be continuous on an open interval $I$ and consider the homogeneous equation
>
> $$
> \frac{dy}{dx} = F\!\left(\frac{y}{x}\right)
> $$
>
> on the region $x>0$. The substitution $y = vx$ transforms it into the separable equation
>
> $$
> x\frac{dv}{dx} = F(v) - v .
> $$
>
> Consequently, on any subinterval where $F(v)-v$ does not vanish, the general solution is given implicitly by
>
> $$
> \int \frac{dv}{F(v)-v} = \ln x + C .
> $$

**Proof.** By Theorem 2.2 the right-hand side is a function of the ratio alone, so writing it as $F(y/x)$ loses no generality. Substituting $y = vx$ and Lemma 2.4 into the equation gives

$$
v + x\frac{dv}{dx} = F(v).
$$

Subtracting $v$ from both sides isolates the derivative term:

$$
x\frac{dv}{dx} = F(v) - v .
$$

The right-hand side now depends on $v$ only and the left-hand side carries the factor $x$ only, so on a subinterval where $F(v)-v \neq 0$ the variables separate as

$$
\frac{dv}{F(v)-v} = \frac{dx}{x} .
$$

Both sides are continuous, so both may be integrated, and the result is the stated implicit relation with one arbitrary constant. $\square$

> **Theorem 2.6 (Differential-form version).** Let $M$ and $N$ be homogeneous of degree $n$ and suppose $y = vx$. Then $M\,dx + N\,dy = 0$ becomes
>
> $$
> \left[M(1,v) + vN(1,v)\right]dx + xN(1,v)\,dv = 0 ,
> $$
>
> which is separable.

**Proof.** Scaling with $k = 1/x$ gives $M(x,vx) = x^{n}M(1,v)$ and $N(x,vx) = x^{n}N(1,v)$. Differentiating $y = vx$ gives $dy = v\,dx + x\,dv$, so

$$
x^{n}M(1,v)\,dx + x^{n}N(1,v)\left(v\,dx + x\,dv\right) = 0 .
$$

Dividing by the non-zero factor $x^{n}$ and collecting the $dx$ terms gives the stated equation. Solving it for $\frac{dv}{dx}$ produces a right-hand side that depends on $v$ alone divided by $x$, which is the definition of separability. $\square$

Theorem 2.6 is the version to quote when the equation arrives in differential form and no division by $N$ has been performed, since it avoids the case discussion that dividing by $N$ would require.

### 2.5 The two cases of the reducible equation

> **Theorem 2.7 (Parallel criterion).** For the equation $\frac{dy}{dx} = \frac{ax+by+c}{px+qy+r}$ with $D = aq-bp$, the two coefficient vectors are proportional if and only if $D = 0$. In that case there is a constant $\lambda \neq 0$ with $p = \lambda a$ and $q = \lambda b$, so the denominator is $\lambda(ax+by)+r$ and the right-hand side depends on $ax+by$ alone.

**Proof.** The vectors $(a,b)$ and $(p,q)$ are proportional exactly when the $2\times 2$ determinant formed from them vanishes, and that determinant is $aq-bp = D$. When $D = 0$ and $(a,b) \neq (0,0)$, the proportionality constant $\lambda$ satisfies $p = \lambda a$ and $q = \lambda b$, so $px+qy = \lambda(ax+by)$. Substituting into the quotient,

$$
\frac{ax+by+c}{px+qy+r} = \frac{ax+by+c}{\lambda(ax+by)+r},
$$

whose right-hand side is a function of the single combination $ax+by$. $\square$

> **Theorem 2.8 (Translation to the point of intersection).** Suppose $D = aq-bp \neq 0$. Then the system
>
> $$
> ah + bk + c = 0, \qquad ph + qk + r = 0
> $$
>
> has the unique solution
>
> $$
> h = \frac{br-cq}{aq-bp}, \qquad k = \frac{cp-ar}{aq-bp} .
> $$
>
> Under the translation $x = X+h$, $y = Y+k$ the equation becomes
>
> $$
> \frac{dY}{dX} = \frac{aX+bY}{pX+qY},
> $$
>
> which is homogeneous of degree zero.

**Proof.** The coefficient matrix of the system has determinant $aq-bp = D \neq 0$, so Cramer's rule applies and gives the two displayed formulas. Now substitute $x = X+h$ and $y = Y+k$, using that $dx = dX$ and $dy = dY$ because $h$ and $k$ are constants:

$$
a(X+h) + b(Y+k) + c = aX + bY + (ah+bk+c) = aX + bY,
$$

and likewise $p(X+h)+q(Y+k)+r = pX + qY$. The constant terms therefore disappear, and the equation reduces to the quotient of two linear forms with no constant terms. Each of $aX+bY$ and $pX+qY$ is homogeneous of degree one, so by Lemma 2.1 their quotient is homogeneous of degree zero. $\square$

The two theorems together exhaust the family: either $D \neq 0$, in which case the translation of Theorem 2.8 applies, or $D = 0$, in which case the reduction of Theorem 2.7 applies. There is no third possibility, because a determinant is either zero or non-zero.

> **Theorem 2.9 (Parallel reduction).** Suppose $D = 0$, so the equation is $\frac{dy}{dx} = G(ax+by)$ for some function $G$ of one variable. Put $z = ax+by$. Then
>
> $$
> \frac{dz}{dx} = a + b\,G(z),
> $$
>
> and the equation is separable.

**Proof.** Since $z = ax+by$ and $b \neq 0$ in the parallel case with a genuine $y$-dependence, differentiating gives

$$
\frac{dz}{dx} = a + b\frac{dy}{dx} = a + b\,G(z).
$$

The right-hand side involves $z$ alone, so separating produces $\frac{dz}{a+bG(z)} = dx$, which is integrable whenever the denominator does not vanish. If instead $b = 0$, then $D = aq$ and $D = 0$ forces $q = 0$ as well, and the equation is already a function of $x$ alone; it is then directly integrable and the substitution is unnecessary. $\square$

### 2.6 What the substitutions do not do

Three limitations deserve statement as properties of the method rather than as footnotes.

First, the reduction theorems convert one equation into another of a different type; they do not produce an answer. After the reduction, an integration must still be performed, and that integration may be impossible in elementary terms. The method guarantees a separable equation, not an elementary solution.

Second, the division that separates the variables is valid only where the divisor is non-zero. Divisions by $F(v)-v$, by $v$, by $x$, by $1-2v^{3}$ and by similar expressions each exclude a set of points, and the excluded points sometimes carry genuine solutions that the general formula does not contain. These are the solutions lost in the division, and they must be examined separately.

Third, the constant of integration is attached once, at the single integration. Attaching it earlier, for instance at the stage of separating the differentials, produces answers that differ by a factor and that fail the substitution check.

## 3. Formal Proofs, Derivations, and Methods

### 3.1 Why integration of both sides is legitimate

The step from $\frac{dy}{dx} = p(x)q(y)$ to $\int \frac{dy}{q(y)} = \int p(x)\,dx$ is often described as multiplying by $dx$, and that description is a shorthand for an argument that should be understood once.

Let $y = \phi(x)$ be a solution and put $Q(y) = \int dy/q(y)$ and $P(x) = \int p(x)\,dx$. Differentiating $Q(\phi(x))$ with respect to $x$ by the chain rule gives

$$
\frac{d}{dx}Q(\phi(x)) = Q'(\phi(x))\,\phi'(x) = \frac{1}{q(\phi(x))}\,p(x)q(\phi(x)) = p(x),
$$

so $Q(\phi(x))$ and $P(x)$ have the same derivative on the interval and therefore differ by a constant. This is the content of the separated formula, obtained without ever treating $dy$ and $dx$ as separate numbers. The chain rule, not a fraction, is what licenses the manipulation.

### 3.2 Method: separation of variables

1. Write the equation in the form $\frac{dy}{dx} = f(x,y)$ and factor the right-hand side completely, so that the dependence on $x$ and the dependence on $y$ are visible.
2. If the factorisation produces $f = p(x)q(y)$, divide by $q(y)$ and multiply by $dx$ in the differential sense, arriving at $\frac{dy}{q(y)} = p(x)\,dx$. Record the excluded set $q(y) = 0$.
3. Integrate both sides, introducing exactly one constant.
4. Solve for $y$ if the resulting relation is algebraically invertible; otherwise leave the answer in implicit form and say that it is implicit.
5. Impose any initial condition to fix the constant.
6. Verify by differentiating the answer implicitly and comparing with the original equation.
7. Check whether any member of the excluded set $q(y) = 0$ is a solution that the family does not contain.

### 3.3 Method: homogeneous equations

1. Test the equation for homogeneity, either by computing $f(kx,ky)$ and extracting a single power, or by computing the degrees of $M$ and $N$ separately and comparing them.
2. Write the right-hand side as a function $F$ of the ratio, that is set $F(v) = f(1,v)$.
3. Substitute $y = vx$ and $\frac{dy}{dx} = v + x\frac{dv}{dx}$.
4. Simplify to the form $x\frac{dv}{dx} = F(v)-v$.
5. Separate as $\frac{dv}{F(v)-v} = \frac{dx}{x}$ and record the excluded set $F(v) = v$.
6. Integrate both sides, and where logarithms appear combine them using the device of Section 1.7.
7. Back-substitute $v = y/x$, then clear fractions to obtain a polynomial relation between $x$ and $y$.
8. Check the solution by implicit differentiation, and examine the excluded set for solutions lost in the division.

### 3.4 Method: the intersecting case

1. Compute $D = aq-bp$. If $D = 0$, abandon this method and use the parallel reduction.
2. Solve $ah+bk+c = 0$ and $ph+qk+r = 0$ for $h$ and $k$, using the formulas of Theorem 2.8 or by elimination.
3. Substitute $x = X+h$ and $y = Y+k$; note that $dx = dX$ and $dy = dY$.
4. Confirm that the constant terms cancel and rewrite the equation as a quotient of two linear forms in $X$ and $Y$ with no constant terms.
5. Solve the resulting homogeneous equation by $Y = vX$ as in Section 3.3.
6. Restore $X = x-h$ and $Y = y-k$ and expand if a polynomial form is required.
7. Check by implicit differentiation of the final relation in the original variables.

### 3.5 Method: the parallel case

1. Confirm $D = 0$ and identify the common combination $ax+by$ appearing in both numerator and denominator.
2. Put $z = ax+by$, so that $\frac{dz}{dx} = a + b\frac{dy}{dx}$, and solve for $\frac{dy}{dx}$ in terms of $\frac{dz}{dx}$.
3. Substitute to obtain $\frac{dz}{dx} = a + b\,G(z)$ where $G$ is the function of one variable describing the quotient.
4. Separate as $\frac{dz}{a+bG(z)} = dx$ and integrate.
5. Back-substitute $z = ax+by$ and simplify.
6. Where the integration produces a logarithm of a linear expression, retain the absolute value until the final step.
7. Check by differentiating the answer.

### 3.6 Why the logarithmic device is safe

The step from $\ln|y| = \ln x + C$ to $\ln|y| = \ln x + \ln A$ is often presented as a trick. It is an identity in disguise. Since $\ln$ is a bijection from $(0,\infty)$ onto $\mathbb{R}$, each real $C$ corresponds to exactly one positive $A$ with $C = \ln A$. Writing the constant in that form and then applying the addition law for logarithms gives

$$
\ln|y| = \ln x + \ln A = \ln(Ax),
$$

so that $|y| = Ax$ and hence $y = \pm Ax$. Absorbing the sign into the constant yields $y = Kx$ with $K \neq 0$ an arbitrary real number, and the omitted value $K = 0$ is usually recovered as a solution lost in a division. The device therefore changes nothing and saves algebra; the sign bookkeeping must still be done.

### 3.7 The degenerate case $F(v) = v$

Suppose $F(v_{0}) = v_{0}$ for some constant $v_{0}$. Then the line $y = v_{0}x$ satisfies the homogeneous equation exactly, because along it $\frac{dy}{dx} = v_{0}$ and $F(y/x) = F(v_{0}) = v_{0}$. The separation step divides by $F(v)-v$, which vanishes at $v_{0}$, so this line is excluded from the integral and must be recorded separately. Geometrically these are the rays along which the direction field is radial: the solution curves crossing them do so with the slope of the ray itself.

The simplest illustration is $\frac{dy}{dx} = \frac{y}{x}$, for which $F(v) = v$. The reduction gives $x\frac{dv}{dx} = 0$, hence $v$ is constant and $y = Cx$ for every $C$, and here the degenerate value $v_{0}$ is not exceptional at all but is the whole family. Comparing this with the general case shows why the degenerate rays must be checked rather than automatically discarded.

## 4. Representative Worked Examples and Solutions

### 4.1 Problem: a separable equation with an initial condition

Solve $\frac{dy}{dx} = \frac{x}{y}$ subject to $y(2) = 3$.

### 4.2 Solution: separate, integrate, fix the constant, verify

Step 1. Factor the right-hand side. It is already a product of a function of $x$ and a function of $y$, with $p(x) = x$ and $q(y) = 1/y$, so the equation is separable.

Step 2. Multiply both sides by $y$ to bring all the $y$-dependence to the left.

$$
y\frac{dy}{dx} = x
$$

Step 3. Integrate both sides with respect to $x$, using the chain rule on the left as in Section 3.1.

$$
\int y\,dy = \int x\,dx
$$

Step 4. Perform the integrations, adding one constant because one integration in total has been carried out.

$$
\frac{y^{2}}{2} = \frac{x^{2}}{2} + c
$$

Step 5. Clear the fractions by multiplying by two and relabel the constant.

$$
y^{2} = x^{2} + C
$$

Step 6. Apply the initial condition. At $x = 2$ the value is $y = 3$, so $9 = 4 + C$, giving $C = 5$.

$$
y^{2} = x^{2} + 5
$$

Step 7. Select the branch. Since $y(2) = 3$ is positive and a solution cannot cross $y = 0$ without violating the equation, the relevant branch is the positive one.

$$
y = \sqrt{x^{2}+5}
$$

Step 8. Verify. Differentiating gives $2y\frac{dy}{dx} = 2x$, hence $\frac{dy}{dx} = \frac{x}{y}$, which is the original equation, and at $x = 2$ the value is $\sqrt{9} = 3$ as required. The solution is valid for all real $x$, since $x^{2}+5$ never vanishes.

### 4.3 Problem: a separable equation whose solution is logarithmic

Solve $\frac{dy}{dx} = e^{x-y}$ subject to $y(0) = \ln 2$.

### 4.4 Solution: split the exponential, then integrate

Step 1. Use the law of indices to expose the separation. Since $e^{x-y} = e^{x}e^{-y}$, the right-hand side is the product of $p(x) = e^{x}$ and $q(y) = e^{-y}$.

Step 2. Multiply by $e^{y}$ to move the $y$-dependence to the left.

$$
e^{y}\frac{dy}{dx} = e^{x}
$$

Step 3. Integrate both sides with respect to $x$.

$$
\int e^{y}\,dy = \int e^{x}\,dx
$$

Step 4. Perform the integrations with one constant.

$$
e^{y} = e^{x} + C
$$

Step 5. Apply the initial condition. At $x = 0$ the value is $y = \ln 2$, so $e^{\ln 2} = 2 = 1 + C$, giving $C = 1$.

$$
e^{y} = e^{x} + 1
$$

Step 6. Solve for $y$ by taking logarithms; the right-hand side is positive for every real $x$, so no restriction arises.

$$
y = \ln\left(e^{x}+1\right)
$$

Step 7. Verify. Differentiating gives $\frac{dy}{dx} = \frac{e^{x}}{e^{x}+1}$, while

$$
e^{x-y} = \frac{e^{x}}{e^{y}} = \frac{e^{x}}{e^{x}+1},
$$

so the two sides agree, and $y(0) = \ln 2$ as required.

### 4.5 Problem: a separable equation whose answer simplifies by trigonometry

Solve $\frac{dy}{dx} = \frac{1+y^{2}}{1+x^{2}}$ subject to $y(0) = 1$.

### 4.6 Solution: separate, integrate to arctangents, then use the tangent addition formula

Step 1. Separate. Dividing by $1+y^{2}$ and multiplying by $dx$ gives

$$
\frac{dy}{1+y^{2}} = \frac{dx}{1+x^{2}} .
$$

Step 2. Integrate both sides, recognising the standard antiderivatives.

$$
\arctan y = \arctan x + C
$$

Step 3. Apply the initial condition. At $x = 0$ the value is $y = 1$, so $\arctan 1 = \pi/4 = 0 + C$, giving $C = \pi/4$.

$$
\arctan y = \arctan x + \frac{\pi}{4}
$$

Step 4. Invert using the tangent addition formula, valid while the total angle lies in $(-\pi/2,\pi/2)$.

$$
y = \tan\left(\arctan x + \frac{\pi}{4}\right) = \frac{x+1}{1-x}
$$

Step 5. Record the interval. The expression $1-x$ vanishes at $x = 1$, and the total angle $\arctan x + \pi/4$ approaches $\pi/2$ from below as $x$ approaches $1$, so the interval containing the initial point is $x < 1$. The formula itself satisfies the equation on each side of $x = 1$, but only the side containing $x = 0$ carries the initial condition.

Step 6. Verify. Differentiating the quotient gives

$$
\frac{dy}{dx} = \frac{(1)(1-x) - (x+1)(-1)}{(1-x)^{2}} = \frac{2}{(1-x)^{2}} .
$$

Step 7. Verify the right-hand side of the equation. Since

$$
1+y^{2} = 1 + \frac{(x+1)^{2}}{(1-x)^{2}} = \frac{(1-x)^{2}+(x+1)^{2}}{(1-x)^{2}} = \frac{2\left(1+x^{2}\right)}{(1-x)^{2}},
$$

dividing by $1+x^{2}$ returns $2/(1-x)^{2}$, matching Step 6. The initial value is $y(0) = 1$, so the solution is confirmed.

### 4.7 Problem: a homogeneous equation of degree zero

Solve $\frac{dy}{dx} = \frac{xy}{x^{2}+y^{2}}$.

### 4.8 Solution: test homogeneity, substitute, separate in $v$, restore $y/x$

Step 1. Test for homogeneity. Replacing $x$ by $kx$ and $y$ by $ky$ gives

$$
f(kx,ky) = \frac{k^{2}xy}{k^{2}x^{2}+k^{2}y^{2}} = \frac{k^{2}xy}{k^{2}\left(x^{2}+y^{2}\right)} = f(x,y),
$$

so $f$ is homogeneous of degree zero and the equation is homogeneous.

Step 2. Express the right-hand side as a function of the ratio. Dividing numerator and denominator by $x^{2}$ gives

$$
f(x,y) = \frac{y/x}{1+(y/x)^{2}} = F(v) \quad \text{with} \quad v = \frac{y}{x} .
$$

Step 3. Substitute $y = vx$ and $\frac{dy}{dx} = v + x\frac{dv}{dx}$.

$$
v + x\frac{dv}{dx} = \frac{v}{1+v^{2}}
$$

Step 4. Subtract $v$ and simplify over a common denominator.

$$
x\frac{dv}{dx} = \frac{v - v\left(1+v^{2}\right)}{1+v^{2}} = \frac{-v^{3}}{1+v^{2}}
$$

Step 5. Separate the variables, dividing by $v^{3}$ and multiplying by $dx$.

$$
\frac{1+v^{2}}{v^{3}}\,dv = -\frac{dx}{x}
$$

Step 6. Split the left-hand side into two elementary powers.

$$
\int\left(v^{-3} + v^{-1}\right)dv = -\int\frac{dx}{x}
$$

Step 7. Integrate both sides.

$$
-\frac{1}{2v^{2}} + \ln|v| = -\ln x + c
$$

Step 8. Combine the logarithms on the left.

$$
\ln|vx| = \frac{1}{2v^{2}} + c
$$

Step 9. Absorb the constant into a logarithm. Writing $c = -\ln A$ and using $vx = y$ gives

$$
\ln|Ay| = \frac{1}{2v^{2}}
$$

Step 10. Restore $v = y/x$.

$$
\ln|Ay| = \frac{x^{2}}{2y^{2}}
$$

Step 11. Verify by implicit differentiation. Differentiating the relation with respect to $x$, treating $y$ as a function of $x$, gives

$$
\frac{y'}{y} = \frac{x}{y^{2}} - \frac{x^{2}y'}{y^{3}} .
$$

Step 12. Collect the terms in $y'$ and simplify.

$$
y'\left(\frac{1}{y}+\frac{x^{2}}{y^{3}}\right) = \frac{x}{y^{2}}, \qquad y'\cdot\frac{x^{2}+y^{2}}{y^{3}} = \frac{x}{y^{2}}, \qquad y' = \frac{xy}{x^{2}+y^{2}} .
$$

The recovered derivative is exactly the right-hand side of the original equation, so the implicit solution is correct. It contains one arbitrary constant $A$, as a first-order equation requires.

### 4.9 Problem: a homogeneous equation with cubic terms

Solve $\left(x^{3}+y^{3}\right)dx - 3xy^{2}\,dy = 0$.

### 4.10 Solution: degree test in differential form, then $y = vx$

Step 1. Apply the $M\,dx + N\,dy$ test. Here $M = x^{3}+y^{3}$ has degree three and $N = -3xy^{2}$ has degree three; the degrees agree, so the equation is homogeneous.

Step 2. Solve for the derivative to place the equation in the form used by the substitution.

$$
\frac{dy}{dx} = \frac{x^{3}+y^{3}}{3xy^{2}}
$$

Step 3. Substitute $y = vx$, so that $y^{3} = v^{3}x^{3}$ and the right-hand side becomes a function of $v$ alone.

$$
v + x\frac{dv}{dx} = \frac{x^{3}+v^{3}x^{3}}{3x\cdot v^{2}x^{2}} = \frac{1+v^{3}}{3v^{2}}
$$

Step 4. Subtract $v$ and simplify.

$$
x\frac{dv}{dx} = \frac{1+v^{3}-3v^{3}}{3v^{2}} = \frac{1-2v^{3}}{3v^{2}}
$$

Step 5. Separate the variables.

$$
\frac{3v^{2}}{1-2v^{3}}\,dv = \frac{dx}{x}
$$

Step 6. Recognise the left-hand side as a logarithmic derivative. Since $\frac{d}{dv}\left(1-2v^{3}\right) = -6v^{2}$, the substitution $u = 1-2v^{3}$ converts the integral into $-\frac{1}{2}\int du/u$.

$$
-\frac{1}{2}\ln\left|1-2v^{3}\right| = \ln x + c
$$

Step 7. Rearrange to isolate the logarithm of the $v$-expression.

$$
\ln\left|1-2v^{3}\right| = -2\ln x + c' = \ln\left(\frac{C}{x^{2}}\right)
$$

Step 8. Exponentiate.

$$
1 - 2v^{3} = \frac{C}{x^{2}}
$$

Step 9. Restore $v = y/x$ and multiply through by $x^{3}$.

$$
x^{3} - 2y^{3} = Cx
$$

Step 10. Verify by implicit differentiation. Differentiating gives $3x^{2} - 6y^{2}y' = C$, and substituting $C = \left(x^{3}-2y^{3}\right)/x$ from the solution itself produces

$$
6y^{2}y' = 3x^{2} - \frac{x^{3}-2y^{3}}{x} = \frac{2x^{3}+2y^{3}}{x}, \qquad y' = \frac{x^{3}+y^{3}}{3xy^{2}} .
$$

The derivative matches the equation, so the answer is confirmed, and the single constant $C$ matches the order.

### 4.11 Problem: a homogeneous equation with a quadratic numerator

Solve $\left(x^{2}-3y^{2}\right)dx + 2xy\,dy = 0$.

### 4.12 Solution: degree test, substitution, logarithmic integration

Step 1. Test the degrees. The coefficient $M = x^{2}-3y^{2}$ has degree two and $N = 2xy$ has degree two, so the equation is homogeneous.

Step 2. Solve for the derivative.

$$
\frac{dy}{dx} = \frac{3y^{2}-x^{2}}{2xy}
$$

Step 3. Substitute $y = vx$ and reduce the right-hand side to a function of $v$.

$$
v + x\frac{dv}{dx} = \frac{3v^{2}x^{2}-x^{2}}{2x\cdot vx} = \frac{3v^{2}-1}{2v}
$$

Step 4. Subtract $v$ and simplify.

$$
x\frac{dv}{dx} = \frac{3v^{2}-1-2v^{2}}{2v} = \frac{v^{2}-1}{2v}
$$

Step 5. Separate the variables.

$$
\frac{2v}{v^{2}-1}\,dv = \frac{dx}{x}
$$

Step 6. Integrate, noting that the numerator is the derivative of the denominator.

$$
\ln\left|v^{2}-1\right| = \ln x + c
$$

Step 7. Combine into a single logarithm and exponentiate.

$$
v^{2} - 1 = Cx
$$

Step 8. Restore $v = y/x$ and multiply by $x^{2}$.

$$
y^{2} - x^{2} = Cx^{3}
$$

Step 9. Verify. Differentiating implicitly gives $2yy' - 2x = 3Cx^{2}$, and using $C = \left(y^{2}-x^{2}\right)/x^{3}$,

$$
2yy' = 2x + \frac{3\left(y^{2}-x^{2}\right)}{x} = \frac{3y^{2}-x^{2}}{x}, \qquad y' = \frac{3y^{2}-x^{2}}{2xy} .
$$

The derivative agrees with the equation, so the solution stands.

### 4.13 Problem: a homogeneous equation that integrates to an arctangent

Solve $\frac{dy}{dx} = \frac{x+y}{x-y}$.

### 4.14 Solution: substitution, partial split of the $v$-integral, compact final form

Step 1. Confirm homogeneity. Numerator and denominator are each homogeneous of degree one, so the quotient has degree zero.

Step 2. Substitute $y = vx$ and divide numerator and denominator by $x$.

$$
v + x\frac{dv}{dx} = \frac{1+v}{1-v}
$$

Step 3. Subtract $v$ and simplify.

$$
x\frac{dv}{dx} = \frac{1+v-v\left(1-v\right)}{1-v} = \frac{1+v^{2}}{1-v}
$$

Step 4. Separate the variables.

$$
\frac{1-v}{1+v^{2}}\,dv = \frac{dx}{x}
$$

Step 5. Split the left-hand side into two standard integrals.

$$
\int\frac{dv}{1+v^{2}} - \int\frac{v\,dv}{1+v^{2}} = \int\frac{dx}{x}
$$

Step 6. Integrate.

$$
\arctan v - \frac{1}{2}\ln\left(1+v^{2}\right) = \ln x + c
$$

Step 7. Absorb the logarithmic term into the right-hand side, using $\frac{1}{2}\ln\left(1+v^{2}\right) = \frac{1}{2}\ln\left(x^{2}+y^{2}\right) - \ln x$.

$$
\arctan v = \frac{1}{2}\ln\left(x^{2}+y^{2}\right) + c
$$

Step 8. Restore $v = y/x$ to obtain the solution in compact form.

$$
\arctan\left(\frac{y}{x}\right) = \frac{1}{2}\ln\left(x^{2}+y^{2}\right) + c
$$

Step 9. Verify. Differentiating the left side by the chain rule gives

$$
\frac{d}{dx}\arctan\left(\frac{y}{x}\right) = \frac{1}{1+\left(y/x\right)^{2}}\cdot\frac{xy'-y}{x^{2}} = \frac{xy'-y}{x^{2}+y^{2}},
$$

and differentiating the right side gives $\left(x+yy'\right)/\left(x^{2}+y^{2}\right)$. Equating the two numerators,

$$
xy' - y = x + yy', \qquad y'\left(x-y\right) = x+y, \qquad y' = \frac{x+y}{x-y},
$$

which is the original equation. The implicit relation therefore solves it.

### 4.15 Problem: a reducible equation of intersecting type

Solve $\left(3x+2y-5\right)dx + \left(2x+3y-5\right)dy = 0$.

### 4.16 Solution: locate the intersection, translate, then solve homogeneously

Step 1. Compute the determinant that decides the case.

$$
D = aq - bp = 3\cdot 3 - 2\cdot 2 = 9-4 = 5 \neq 0
$$

The coefficient vectors are not proportional, so the lines intersect in a single point and the translation method applies.

Step 2. Solve for the point of intersection.

$$
3h + 2k - 5 = 0, \qquad 2h + 3k - 5 = 0
$$

Step 3. Subtract the second equation from the first, which gives $h - k = 0$, so $h = k$. Substituting $h = k$ into the first equation gives $5h = 5$, hence $h = 1$ and $k = 1$.

Step 4. Substitute $x = X+1$ and $y = Y+1$; the differentials satisfy $dx = dX$ and $dy = dY$. The numerator becomes $3X+2Y$ and the denominator becomes $2X+3Y$.

$$
\frac{dY}{dX} = -\frac{3X+2Y}{2X+3Y}
$$

Step 5. Substitute $Y = vX$ and divide by $X$.

$$
v + X\frac{dv}{dX} = -\frac{3+2v}{2+3v}
$$

Step 6. Subtract $v$ and simplify over a common denominator.

$$
X\frac{dv}{dX} = \frac{-3-2v-2v-3v^{2}}{2+3v} = -\frac{3v^{2}+4v+3}{2+3v}
$$

Step 7. Separate the variables, moving the minus sign to the $X$ side.

$$
\frac{3v+2}{3v^{2}+4v+3}\,dv = -\frac{dX}{X}
$$

Step 8. Integrate, noting that $3v+2$ is exactly half the derivative of $3v^{2}+4v+3$.

$$
\frac{1}{2}\ln\left(3v^{2}+4v+3\right) = -\ln X + c
$$

Step 9. Multiply by two and exponentiate.

$$
3v^{2}+4v+3 = \frac{C}{X^{2}}
$$

Step 10. Multiply by $X^{2}$ and restore $v = Y/X$, so that $v^{2}X^{2} = Y^{2}$ and $vX^{2} = XY$.

$$
3Y^{2} + 4XY + 3X^{2} = C
$$

Step 11. Restore $X = x-1$ and $Y = y-1$.

$$
3(y-1)^{2} + 4(x-1)(y-1) + 3(x-1)^{2} = C
$$

Step 12. Expand and relabel the constant.

$$
3\left(x^{2}+y^{2}\right) + 4xy - 10\left(x+y\right) = C'
$$

Step 13. Verify. Write $F = 3x^{2}+3y^{2}+4xy-10x-10y$. Then $F_{x} = 6x+4y-10$ and $F_{y} = 4x+6y-10$, so implicit differentiation of $F = C'$ gives

$$
\frac{dy}{dx} = -\frac{F_{x}}{F_{y}} = -\frac{6x+4y-10}{4x+6y-10} = -\frac{3x+2y-5}{2x+3y-5},
$$

which is the derivative implied by the original differential equation. The solution is confirmed.

### 4.17 Problem: a reducible equation of parallel type

Solve $\frac{dy}{dx} = \frac{x-y+3}{2x-2y+5}$.

### 4.18 Solution: recognise the repeated combination, use $z = x-y$

Step 1. Test the case. The ratio of the $x$-coefficients is $1/2$ and the ratio of the $y$-coefficients is $-1/(-2) = 1/2$. The ratios agree, so $D = 1\cdot(-2) - (-1)\cdot 2 = 0$ and the lines are parallel.

Step 2. Note that both numerator and denominator depend on $x-y$ alone: the numerator is $(x-y)+3$ and the denominator is $2(x-y)+5$.

Step 3. Substitute $z = x-y$, so that $\frac{dz}{dx} = 1 - \frac{dy}{dx}$.

$$
\frac{dy}{dx} = 1 - \frac{dz}{dx}
$$

Step 4. Substitute into the equation.

$$
1 - \frac{dz}{dx} = \frac{z+3}{2z+5}
$$

Step 5. Solve for $\frac{dz}{dx}$.

$$
\frac{dz}{dx} = 1 - \frac{z+3}{2z+5} = \frac{2z+5-z-3}{2z+5} = \frac{z+2}{2z+5}
$$

Step 6. Separate the variables.

$$
\frac{2z+5}{z+2}\,dz = dx
$$

Step 7. Divide out the fraction, since the numerator has twice the leading term of the denominator.

$$
2z + 5 = 2\left(z+2\right) + 1, \qquad \frac{2z+5}{z+2} = 2 + \frac{1}{z+2}
$$

Step 8. Integrate.

$$
2z + \ln\left|z+2\right| = x + c
$$

Step 9. Restore $z = x-y$.

$$
2(x-y) + \ln\left|x-y+2\right| = x + c
$$

Step 10. Simplify by collecting the linear terms.

$$
x - 2y + \ln\left|x-y+2\right| = c
$$

Step 11. Verify. Differentiate the relation implicitly, remembering that the derivative of $\ln\left|x-y+2\right|$ is $\left(1-y'\right)/\left(x-y+2\right)$.

$$
1 - 2y' + \frac{1-y'}{x-y+2} = 0
$$

Step 12. Clear the denominator and collect the terms in $y'$.

$$
\left(x-y+2\right)\left(1-2y'\right) + 1 - y' = 0, \qquad x-y+3 = y'\left(2x-2y+5\right)
$$

Step 13. Solve for the derivative and compare.

$$
\frac{dy}{dx} = \frac{x-y+3}{2x-2y+5}
$$

This is the original equation, so the implicit solution is correct. The logarithm requires $x-y+2 \neq 0$, and the excluded point must be noted when the interval of validity is stated.

### 4.19 Problem: a second intersecting example with unequal coefficients

Solve $\left(x-2y+1\right)dx + \left(4x-3y-6\right)dy = 0$.

### 4.20 Solution: Cramer's rule for the translation, then the homogeneous method

Step 1. Compute the determinant with $a = 1$, $b = -2$, $p = 4$, $q = -3$.

$$
D = aq - bp = 1\cdot(-3) - (-2)\cdot 4 = -3+8 = 5 \neq 0
$$

So the intersecting case applies.

Step 2. Locate the intersection using the formulas of Theorem 2.8, with $c = 1$ and $r = -6$.

$$
h = \frac{br-cq}{D} = \frac{(-2)(-6) - (1)(-3)}{5} = \frac{12+3}{5} = 3
$$

Step 3. Compute the second coordinate.

$$
k = \frac{cp-ar}{D} = \frac{(1)(4) - (1)(-6)}{5} = \frac{4+6}{5} = 2
$$

Step 4. Check both equations. With $h = 3$ and $k = 2$: $3 - 4 + 1 = 0$ and $12 - 6 - 6 = 0$, so the point is correct.

Step 5. Substitute $x = X+3$, $y = Y+2$ and confirm that the constants cancel.

$$
\frac{dY}{dX} = -\frac{X-2Y}{4X-3Y}
$$

Step 6. Substitute $Y = vX$.

$$
v + X\frac{dv}{dX} = -\frac{1-2v}{4-3v} = \frac{2v-1}{4-3v}
$$

Step 7. Subtract $v$ and simplify.

$$
X\frac{dv}{dX} = \frac{2v-1-4v+3v^{2}}{4-3v} = \frac{3v^{2}-2v-1}{4-3v}
$$

Step 8. Factor the quadratic, since $3v^{2}-2v-1 = (3v+1)(v-1)$.

$$
\frac{4-3v}{(3v+1)(v-1)}\,dv = \frac{dX}{X}
$$

Step 9. Decompose into partial fractions. Writing $\frac{4-3v}{(3v+1)(v-1)} = \frac{A}{3v+1} + \frac{B}{v-1}$ and clearing denominators gives $4-3v = A(v-1) + B(3v+1)$; setting $v = 1$ gives $B = 1/4$, and setting $v = -1/3$ gives $A = -15/4$. Hence

$$
\frac{4-3v}{(3v+1)(v-1)} = -\frac{15}{4}\cdot\frac{1}{3v+1} + \frac{1}{4}\cdot\frac{1}{v-1} .
$$

Step 10. Integrate both sides.

$$
-\frac{5}{4}\ln\left|3v+1\right| + \frac{1}{4}\ln\left|v-1\right| = \ln X + c
$$

Step 11. Multiply by four to clear the fractions.

$$
-5\ln\left|3v+1\right| + \ln\left|v-1\right| = 4\ln X + c'
$$

Step 12. Combine the logarithms and exponentiate.

$$
\frac{v-1}{\left(3v+1\right)^{5}} = CX^{4}
$$

Step 13. Restore $v = Y/X$. The numerator is $\left(Y-X\right)/X$ and the denominator is $\left(X+3Y\right)^{5}/X^{5}$, so the ratio is $\left(Y-X\right)X^{4}/\left(X+3Y\right)^{5}$.

$$
\frac{\left(Y-X\right)X^{4}}{\left(X+3Y\right)^{5}} = CX^{4}, \qquad Y - X = C\left(X+3Y\right)^{5}
$$

Step 14. Restore $X = x-3$ and $Y = y-2$.

$$
y - x + 1 = C\left(x+3y-9\right)^{5}
$$

Step 15. Verify. Put $u = x+3y-9$, so that the relation reads $y-x+1 = Cu^{5}$ and differentiation gives $y'-1 = 5Cu^{4}\left(1+3y'\right)$. Replacing $5Cu^{4}$ by $5\left(y-x+1\right)/u$,

$$
y' - 1 = \frac{5\left(y-x+1\right)}{u}\left(1+3y'\right).
$$

Step 16. Collect the terms in $y'$ and simplify the two combinations.

$$
y'\left[u - 15\left(y-x+1\right)\right] = u + 5\left(y-x+1\right)
$$

Step 17. Evaluate both brackets. The first is $x+3y-9-15y+15x-15 = 16x-12y-24 = 4\left(4x-3y-6\right)$, and the second is $x+3y-9+5y-5x+5 = -4x+8y-4 = -4\left(x-2y+1\right)$.

$$
y' = \frac{-4\left(x-2y+1\right)}{4\left(4x-3y-6\right)} = -\frac{x-2y+1}{4x-3y-6}
$$

The derivative agrees with the differential equation, so the solution is confirmed.

## 5. Mathematical Extensions, Limits, and Common Errors

### 5.1 Reducible equations whose lines are coincident

If $D = 0$ and the two lines are not merely parallel but coincident, then $\frac{ax+by+c}{px+qy+r}$ is a constant and the equation reduces to $\frac{dy}{dx} = \text{constant}$, whose solutions are straight lines. This happens when $(p,q,r)$ is a multiple of $(a,b,c)$, for instance in

$$
\frac{dy}{dx} = \frac{2x+4y-6}{x+2y-3} = 2 .
$$

The parallel reduction still applies formally, since $z = x+2y$ gives $\frac{dz}{dx} = 1 + 2\cdot 2 = 5$, hence $z = 5x + C$ and $y = \left(5x + C - x\right)/2$, which is the same family of straight lines. Recognising the coincidence early saves the integration, and forgetting to look for it wastes time without producing an error.

### 5.2 When separation gives an integral that cannot be evaluated

Separability is a statement about form, not about integrability. The equation

$$
\frac{dy}{dx} = e^{-y^{2}}
$$

is separable, but the separated integral $\int e^{y^{2}}dy$ has no elementary antiderivative. The correct response is to state the solution as

$$
\int_{y_{0}}^{y} e^{s^{2}}ds = x - x_{0},
$$

which is a perfectly definite solution implicitly, and to say plainly that no elementary closed form is available. Claiming a formula in terms of standard functions would be false.

The same caution applies to the homogeneous method. After the reduction, the integral $\int dv/\left(F(v)-v\right)$ may be intractable even though the reduction itself was flawless. The method has done its work when it has produced a separable equation; whether that equation can be integrated in closed form is a separate question.

### 5.3 Solutions lost in a division

Each separation step divides by something, and each such division can lose a solution. The list of divisors encountered in this topic is short: $q(y)$ when separating a general separable equation, $x$ when separating after the $y = vx$ substitution, $F(v)-v$ when dividing the reduced equation, and the denominators produced by the parallel case.

The remedy is uniform. Before integrating, note the values at which the divisor vanishes, and afterwards test whether the corresponding function satisfies the original equation. For the equation $\frac{dy}{dx} = \frac{x}{y}$ the divisor is $y$, and $y = 0$ does not solve the equation, so nothing is lost. For the equation $\frac{dy}{dx} = \frac{v^{2}-1}{2v}$ in the reduced variable, the value $v = 0$ corresponds to $y = 0$; checking it in the original equation shows whether it must be included.

### 5.4 Equations that imitate the homogeneous form

A frequent error is to test homogeneity by counting the terms of the written expression without scaling. The two genuine tests are the substitution test $f(kx,ky) = k^{n}f(x,y)$ and the two-degree comparison for $M\,dx + N\,dy = 0$. Applied to

$$
\left(x^{2}+y^{2}+1\right)dx + xy\,dy = 0,
$$

the substitution test fails because the constant term survives scaling, so the equation is not homogeneous and $y = vx$ will not separate it. Applied to

$$
\left(x^{2}+y\right)dx + xy\,dy = 0,
$$

the two-degree test fails because $x^{2}+y$ has no degree, so again the method does not apply. Attempting the substitution anyway produces an equation in which $v$ and $x$ remain entangled, and the resulting algebra is a signal that the test was skipped.

### 5.5 Common errors and how to avoid them

- **Treating $v$ as a constant.** The derivative of $y = vx$ is $v + x\frac{dv}{dx}$, and omitting the second term collapses the whole method. Every occurrence of $\frac{dy}{dx}$ after the substitution must be replaced by that two-term expression.
- **Forgetting the factor in $dy$ when the equation is in differential form.** With $y = vx$, the differential is $dy = v\,dx + x\,dv$; writing $dy = v\,dx$ omits an essential term and produces answers that fail the check.
- **Testing homogeneity on the ratio instead of on the functions.** The degree-zero test applies to $f$, or to each of $M$ and $N$ separately. Comparing the numerator's degree with the denominator's degree is correct only through the quotient rule of Lemma 2.1.
- **Confusing the two meanings of homogeneous.** In this topic a homogeneous equation is one whose right-hand side has degree zero. In the theory of linear equations, homogeneous means that the right-hand side is zero. The two usages are unrelated, and an answer that confuses them cannot be rescued.
- **Mixing up the two reducible cases.** The decision is made by $D = aq-bp$, not by the shape of the numbers. A quick mental test is to compare $a/p$ with $b/q$; equality means the parallel case, and inequality means the translation case.
- **Forgetting to translate back.** An answer left in $X$ and $Y$, or in $v$, is not a solution of the original problem. Every substitution introduced must be undone explicitly, and the final answer must be written in the original variables.
- **Dropping the constant or adding two.** One integration means one constant. A second constant appearing usually means that an integral was split into two parts and each part was given its own constant, which is legitimate only if the two are then combined.
- **Losing absolute values and signs.** Integrals of the form $\int dv/v$ give $\ln|v|$, and dropping the modulus silently restricts the domain. When the modulus is removed at the end, the sign must be accounted for in the constant.
- **Skipping the verification.** Every answer in this topic can be checked by differentiating implicitly. The check catches sign errors, mis-integrated powers, and algebraic slips in the partial fractions, and it costs less than a minute.
- **Ignoring the interval of validity.** A solution containing $\ln(x-y+2)$ is confined to the side of the line $x-y+2 = 0$ on which the argument is positive, and a solution containing $1/(1-x)$ excludes $x = 1$. The interval is part of the answer.

### 5.6 A decision procedure for any first-order equation

The methods of this topic form a cascade, and the cascade is best applied in a fixed order.

First, check whether the right-hand side factors into a function of $x$ times a function of $y$. If it does, separate and integrate, and stop.

Second, if it does not factor, check homogeneity by scaling. If $f(kx,ky)$ collapses to a single power of $k$ with exponent zero, apply $y = vx$, separate in $v$, integrate, and restore the ratio.

Third, if the equation is a quotient of two linear expressions, compute $D = aq-bp$. If $D \neq 0$, find the intersection point, translate, and then treat the result by the homogeneous method. If $D = 0$, set $z = ax+by$ and separate directly.

Fourth, if none of these applies, the equation is of a type not covered by this topic, and a different technique, such as an integrating factor for a linear equation, is required. Recognising that boundary honestly is better than forcing a substitution that cannot work.

### 5.7 Where the ideas lead

The reduction of a homogeneous equation to a separable one is the prototype of every later substitution method in the subject. The same pattern, in which a clever change of variable converts an unfamiliar equation into one already solved, reappears in the Bernoulli equation, where $z = y^{1-n}$ linearises the equation, and in equations homogeneous in a weighted sense, where a substitution of the form $y = x^{m}v$ is used.

The reduction of the linear-fraction equation is a first example of a change of coordinates, and the translation $X = x-h$, $Y = y-k$ is precisely a change of origin. Recognising that the constants in a linear expression can be removed by moving the origin is a habit that pays off in the study of linear systems and in the classification of plane curves, where the same translation is used to eliminate linear terms.

Finally, the degree-zero condition is the first appearance of a scaling symmetry. An equation that is unchanged when both variables are scaled by the same factor has solutions that are determined by a single ratio, and the substitution $y = vx$ is the algebraic expression of that symmetry. Seeing the symmetry is what tells you which substitution to attempt before any algebra is done.
