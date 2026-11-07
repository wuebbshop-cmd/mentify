## 1. Foundational Concepts, Definitions, and Axioms

### 1.1 The shape of a linear equation of order n

A differential equation of order $n$ is one in which the highest derivative present is the $n$-th. Requiring the equation to be linear imposes a further, very restrictive condition: the unknown function and each of its derivatives may appear only to the first power, and no term may multiply two of them together. What remains is a sum in which every derivative is multiplied by a coefficient that depends on the independent variable alone.

> **Definition (Linear equation of order n).** Let $a_{0},a_{1},\dots,a_{n}$ and $Q$ be functions of $x$ alone on an interval $I$, with $a_{0}$ never zero on $I$. The equation is linear of order $n$ when it can be written as a sum of the unknown function and its first $n$ derivatives, each multiplied by its own coefficient, equal to a prescribed function of $x$.

The displayed form of that sum is the object every method in this topic acts upon.

$$
a_{0}(x)\frac{d^{n}y}{dx^{n}}+a_{1}(x)\frac{d^{n-1}y}{dx^{n-1}}+\cdots+a_{n-1}(x)\frac{dy}{dx}+a_{n}(x)y=Q(x)
$$

Each symbol carries a precise meaning. The letter $n$ is a fixed positive whole number, the order. The letter $y$ is the unknown function of the single variable $x$, so $y=y(x)$. The symbol $\frac{d^{k}y}{dx^{k}}$ is the result of differentiating $y$ exactly $k$ times with respect to $x$. The functions $a_{0},a_{1},\dots,a_{n}$ are the coefficients, and they are permitted to vary with $x$ but never with $y$. The function $Q$, called the forcing term or the right-hand member, is also a function of $x$ alone. The condition $a_{0}(x)\neq 0$ is not pedantry: it guarantees that the equation genuinely involves the $n$-th derivative and therefore genuinely has order $n$.

Three consequences follow immediately from the definition, and each is used constantly.

The first is that a sum of solutions is a solution whenever the right-hand member vanishes. The second is that the difference of two solutions of the same non-homogeneous equation solves the corresponding equation with zero right-hand member. The third is that the coefficient functions cannot depend on $y$, so no amount of algebraic rearrangement will ever turn a non-linear equation into a linear one. These three facts are the whole reason the topic is organised the way it is.

### 1.2 Homogeneous and non-homogeneous

> **Definition (Homogeneous equation).** The linear equation of order $n$ is homogeneous when $Q(x)=0$ identically on the interval of interest. Otherwise it is non-homogeneous, and $Q$ is called the non-homogeneous term.

The word homogeneous here does not mean that the coefficients are constant; it means that every term has the same degree in the unknown, namely degree one, so that replacing $y$ by a constant multiple $\lambda y$ multiplies the whole left-hand side by that same constant. That is exactly the property needed for sums of solutions to remain solutions.

A concrete comparison makes the distinction visible. The equation

$$
x^{3}\frac{d^{3}y}{dx^{3}}-8x^{2}\frac{d^{2}y}{dx^{2}}+10x\frac{dy}{dx}+8y=0
$$

is homogeneous of order three with variable coefficients, because every term involves $y$ to the first degree and the right-hand side is zero. The equation

$$
2x^{4}\frac{d^{4}y}{dx^{4}}-5x^{3}\frac{dy}{dx}+9xy=xe^{x}
$$

is non-homogeneous of order four with variable coefficients. In the second equation the right-hand member $xe^{x}$ destroys homogeneity, and the solution will consequently carry an extra ingredient beyond the family of solutions of the homogeneous equation.

### 1.3 The operator notation and the polynomial $P(D)$

Differentiation is a linear operation, so it can be treated as an algebraic symbol. Writing $D$ for $\frac{d}{dx}$, the notation $D^{k}$ means differentiation performed $k$ times, so $D^{k}y=\frac{d^{k}y}{dx^{k}}$. A linear equation then becomes a single statement about a polynomial in $D$ applied to $y$.

> **Definition (Linear differential operator).** For an equation of order $n$ with coefficients $a_{0},\dots,a_{n}$, the associated operator is the combination of derivatives applied to the unknown.

$$
L=a_{0}(x)D^{n}+a_{1}(x)D^{n-1}+\cdots+a_{n-1}(x)D+a_{n}(x)
$$

The equation is then written compactly as $L[y]=Q(x)$. When the coefficients are constants the operator is a genuine polynomial in $D$ with numerical coefficients, and this is the decisive advantage: such a polynomial can be factored, its roots can be found, and its factorisation translates directly into solutions. Writing $P$ for that polynomial,

$$
P(D)=a_{0}D^{n}+a_{1}D^{n-1}+\cdots+a_{n-1}D+a_{n}
$$

so that the equation reads $P(D)y=Q(x)$. For example the third-order equation with constant coefficients

$$
\frac{d^{3}y}{dx^{3}}-6\frac{d^{2}y}{dx^{2}}+11\frac{dy}{dx}-6y=0
$$

is written $(D^{3}-6D^{2}+11D-6)y=0$, and the polynomial $P(D)=D^{3}-6D^{2}+11D-6$ factors as $(D-1)(D-2)(D-3)$.

The distinction between constant and variable coefficients is the great dividing line of the subject. With constant coefficients the operator is a polynomial and the whole problem reduces to finding roots. With variable coefficients no such factorisation is generally available, and one looks instead for a change of the independent variable that converts the equation into one with constant coefficients. The Cauchy–Euler equation and Legendre's equation are the two families for which that change of variable is known explicitly, and they are the subject of the rest of this note.

### 1.4 Complementary function and particular integral

Every solution of a linear equation of order $n$ is built from two separate pieces, and the two pieces are found by two separate procedures.

> **Definition (Complementary function).** The complementary function, written $y_{c}$, is the general solution of the homogeneous equation obtained by replacing $Q(x)$ by zero. It contains exactly $n$ arbitrary constants.

> **Definition (Particular integral).** A particular integral, written $y_{p}$, is any single function that satisfies the full non-homogeneous equation, with no arbitrary constants attached.

> **Definition (General solution).** The general solution of the non-homogeneous equation is the sum of the two pieces.

$$
y=y_{c}+y_{p}
$$

The logic of the addition is a one-line computation. If $L[y_{c}]=0$ and $L[y_{p}]=Q$, then by linearity of $L$

$$
L[y_{c}+y_{p}]=L[y_{c}]+L[y_{p}]=0+Q=Q .
$$

So the sum solves the equation. The converse is equally important: if $y$ is any solution and $y_{p}$ is one known solution, then $y-y_{p}$ solves the homogeneous equation, hence lies in the family $y_{c}$. Therefore the sum captures every solution and nothing else.

The counting rule that accompanies this structure is the single most useful check in the subject: an equation of order $n$ produces a complementary function with exactly $n$ essential arbitrary constants, so a proposed answer carrying fewer constants is wrong regardless of how it was obtained.

### 1.5 The Cauchy–Euler equation

A Cauchy–Euler equation, also called an Euler equation or an equidimensional equation, is a linear equation in which the power of $x$ multiplying each derivative equals the order of that derivative.

> **Definition (Cauchy–Euler equation of order n).** A linear equation is of Cauchy–Euler type when each derivative is multiplied by a constant times the matching power of $x$, the right-hand member depending on $x$ alone.

$$
x^{n}\frac{d^{n}y}{dx^{n}}+a_{1}x^{n-1}\frac{d^{n-1}y}{dx^{n-1}}+\cdots+a_{n-1}x\frac{dy}{dx}+a_{n}y=f(x)
$$

Here $a_{1},\dots,a_{n}$ are constants, $n$ is the order, and $f$ is a function of $x$ alone. Every term has the shape constant multiplied by $x^{k}$ multiplied by the $k$-th derivative. In operator form the left-hand side is written as a polynomial in $x D$ rather than in $D$ alone, and the standard abbreviation is

$$
\left(a_{0}x^{n}D^{n}+a_{1}x^{n-1}D^{n-1}+\cdots+a_{n-1}xD+a_{n}\right)y=f(x),
$$

with $a_{0}=1$ in the normalised form above. The defining structural feature is the matching of powers and derivative orders. The equation

$$
x^{2}\frac{d^{2}y}{dx^{2}}+2x\frac{dy}{dx}-6y=x^{3}
$$

is of Cauchy–Euler type, because the second derivative is accompanied by $x^{2}$ and the first derivative by $x$. The superficially similar equation

$$
x^{2}\frac{d^{2}y}{dx^{2}}+2\frac{dy}{dx}-6y=x^{3}
$$

is not, because the first derivative is accompanied by a constant rather than by $x$. The difference looks small and is decisive: the substitution that solves the first equation leaves the second with variable coefficients and no elementary route forward.

Two reasons make this family important. First, it is the standard model for physical problems posed on a domain that has no preferred length scale, where the physics is unchanged by rescaling the unit of measurement, and such problems produce exactly this balance of powers. Second, and more immediately, the family is completely solvable: a change of the independent variable, followed by the standard constant-coefficient machinery, always produces the answer.

### 1.6 Legendre's linear equation

Legendre's equation is the same idea with the variable replaced by an affine expression.

> **Definition (Legendre's linear equation of order n).** A linear equation is of Legendre type when each derivative is multiplied by a constant times the matching power of the affine expression $ax+b$, with $a\neq 0$ and $b$ constants.

$$
(ax+b)^{n}\frac{d^{n}y}{dx^{n}}+a_{1}(ax+b)^{n-1}\frac{d^{n-1}y}{dx^{n-1}}+\cdots+a_{n-1}(ax+b)\frac{dy}{dx}+a_{n}y=f(x)
$$

Setting $a=1$ and $b=0$ recovers the Cauchy–Euler equation exactly, so Legendre's equation contains the Euler equation as a special case and is in that sense the more general of the two. The extra generality is mild: the substitution that works for Euler's equation works here too, after the affine expression is treated as a single new variable.

$$
u=ax+b, \qquad t=\ln u=\ln(ax+b)
$$

The only new feature is a scale factor $a^{k}$ attached to the $k$-th derivative term, and forgetting that factor is one of the most common errors in the whole topic.

### 1.7 The single idea behind both reductions

Both families are solved by the same device: replace the independent variable $x$ by a new independent variable $t$ defined through a logarithm, and then differentiate with respect to $t$ instead of $x$.

For the Euler equation the substitution is $x=e^{t}$, that is $t=\ln x$. For Legendre's equation the substitution is $ax+b=e^{t}$, that is $t=\ln(ax+b)$. In both cases the variable combination $x\frac{d}{dx}$, or $(ax+b)\frac{d}{dx}$, becomes a pure differentiation in $t$. Writing

$$
\theta=\frac{d}{dt}
$$

the two fundamental identities are

$$
x\frac{dy}{dx}=\theta y, \qquad (ax+b)\frac{dy}{dx}=a\theta y .
$$

The remarkable feature is that the first identity iterates: the operator $x^{k}D^{k}$ becomes a polynomial in $\theta$ with constant integer coefficients. That is why an equation whose coefficients are powers of $x$ turns into an equation whose coefficients are constants, and why the whole apparatus of auxiliary equations and root cases becomes available.

## 2. Theorems, Lemmas, and Analytical Properties

### 2.1 Superposition and its converse

> **Theorem (Superposition for the homogeneous equation).** Let $L$ be a linear operator of order $n$ with coefficients continuous on an interval $I$. If $y_{1},\dots,y_{m}$ all satisfy $L[y]=0$ on $I$, then every linear combination with constant coefficients also satisfies $L[y]=0$ on $I$.

The proof is the computation already given in Section 1.4, extended to $m$ terms: linearity distributes $L$ over the sum and over the constant multipliers, and each surviving term vanishes.

> **Theorem (Structure of the solution set).** If $y_{p}$ solves $L[y]=Q$, then the complete solution set of $L[y]=Q$ consists exactly of the functions $y_{p}+y_{h}$ where $L[y_{h}]=0$.

Both directions were argued in Section 1.4. The practical content is that finding a particular integral is a search for one function, not for a family, and any convenient one will do.

### 2.2 Independence and the Wronskian

A complementary function needs $n$ solutions that are genuinely different, not merely scalar multiples of one another.

> **Definition (Linear dependence of functions).** The functions $y_{1},\dots,y_{n}$ are linearly dependent on an interval $I$ when there exist constants $c_{1},\dots,c_{n}$, not all zero, with $c_{1}y_{1}+\cdots+c_{n}y_{n}=0$ identically on $I$. Otherwise they are linearly independent.

> **Definition (Wronskian).** For two differentiable functions the Wronskian is the determinant of the array formed by the functions and their first derivatives.

$$
W(y_{1},y_{2})=y_{1}y_{2}'-y_{1}'y_{2}
$$

For $n$ functions the definition extends to the determinant of the $n$ by $n$ array whose rows are the functions and their successive derivatives up to order $n-1$.

> **Theorem (Wronskian test).** If $y_{1},\dots,y_{n}$ are solutions of an $n$-th order linear homogeneous equation with continuous coefficients on $I$, and if $W$ is not zero at some point of $I$, then the functions are linearly independent and every solution on $I$ is a linear combination of them.

The hypothesis that the functions are solutions matters. Two arbitrary functions can have a Wronskian that vanishes at a point and still be independent, so the test is a sufficient condition, not a universal criterion, unless the functions come from a linear equation.

### 2.3 The auxiliary equation and the three root cases

For an equation with constant coefficients the complementary function is read off from the roots of a polynomial.

> **Definition (Auxiliary equation).** For the constant-coefficient equation $P(D)y=0$ with $P(D)=a_{0}D^{n}+\cdots+a_{n}$, the auxiliary equation is $P(m)=0$. Its roots are complex numbers counted with multiplicity, and there are $n$ of them.

> **Theorem (Complementary function of a constant-coefficient equation).** The complementary function is the sum of the contributions of the distinct roots of the auxiliary equation, where a root $m$ of multiplicity $r$ contributes a block of $r$ independent solutions and the total number of constants is $n$.

The three cases of the theorem are the following.

If $m$ is a real root of multiplicity one, the contribution is $c e^{mx}$.

If $m$ is a real root of multiplicity $r$, the contribution is a polynomial of degree $r-1$ in $x$ multiplying the exponential.

$$
\left(c_{1}+c_{2}x+c_{3}x^{2}+\cdots+c_{r}x^{r-1}\right)e^{mx}
$$

If $\alpha\pm i\beta$ is a complex conjugate pair, each of multiplicity $r$, the contribution is a polynomial of degree $r-1$ in $x$ multiplying the exponential $e^{\alpha x}$ and a cosine-sine pair with frequency $\beta$.

$$
e^{\alpha x}\left[\left(A_{0}+A_{1}x+\cdots+A_{r-1}x^{r-1}\right)\cos\beta x+\left(B_{0}+B_{1}x+\cdots+B_{r-1}x^{r-1}\right)\sin\beta x\right]
$$

The cases compound. An order-four equation with auxiliary roots $0,0,2\pm 3i$ has complementary function $c_{1}+c_{2}x+e^{2x}(c_{3}\cos 3x+c_{4}\sin 3x)$, four constants in total.

### 2.4 The key operator identity

> **Lemma (Euler operator identity).** Let $x>0$, let $t=\ln x$ and let $\theta=\frac{d}{dt}$. Then for every whole number $k\ge 1$,

$$
x^{k}D^{k}=\theta(\theta-1)(\theta-2)\cdots(\theta-k+1),
$$

where the product on the right contains exactly $k$ factors and the last factor is $\theta-k+1$.

The identity is an identity of operators: it says that applying the left side to any sufficiently differentiable function of $x$ gives the same result as applying the right side. Written out for small $k$ it gives the table that every computation uses.

$$
x D=\theta, \qquad x^{2}D^{2}=\theta^{2}-\theta, \qquad x^{3}D^{3}=\theta^{3}-3\theta^{2}+2\theta
$$

$$
x^{4}D^{4}=\theta^{4}-6\theta^{3}+11\theta^{2}-6\theta
$$

The coefficients in these expansions are the unsigned Stirling numbers of the first kind, and they are not the binomial coefficients. This is exactly where a careless student loses marks: $x^{3}D^{3}$ is $\theta^{3}-3\theta^{2}+2\theta$, not $\theta^{3}-3\theta^{2}+3\theta-1$.

### 2.5 Reduction theorem for the Cauchy–Euler equation

> **Theorem (Cauchy–Euler reduction).** Suppose $x>0$ and set $x=e^{t}$, $t=\ln x$, $\theta=\frac{d}{dt}$. Then the Cauchy–Euler equation of order $n$ is transformed into a linear equation with constant coefficients in the variable $t$, of the same order $n$, whose right-hand member is $f(e^{t})$.

The transformed equation is obtained by replacing each operator $x^{k}D^{k}$ by its $\theta$-polynomial from Section 2.4.

$$
\left[\theta(\theta-1)\cdots(\theta-n+1)+a_{1}\theta(\theta-1)\cdots(\theta-n+2)+\cdots+a_{n-1}\theta+a_{n}\right]y=f(e^{t})
$$

Two remarks make the theorem usable. First, the transformation is invertible: a solution $y=Q(t)$ of the transformed equation yields the solution $y=Q(\ln x)$ of the original, because $t=\ln x$. Second, the theorem converts a variable-coefficient problem into a constant-coefficient problem, so the auxiliary-equation machinery of Section 2.3 applies without further work.

### 2.6 The Euler indicial equation and its three cases

> **Theorem (Euler complementary function).** For the homogeneous Cauchy–Euler equation, the substitution $y=x^{m}$ produces the indicial equation

$$
m(m-1)(m-2)\cdots(m-n+1)+a_{1}m(m-1)\cdots(m-n+2)+\cdots+a_{n-1}m+a_{n}=0 ,
$$

and the complementary function is assembled from the roots of that polynomial exactly as in the constant-coefficient theorem, with $x^{m}$ replacing $e^{mt}$ and $\ln x$ replacing $t$.

Explicitly, a real root $m$ of multiplicity $r$ contributes

$$
\left(c_{1}+c_{2}\ln x+c_{3}(\ln x)^{2}+\cdots+c_{r}(\ln x)^{r-1}\right)x^{m},
$$

and a complex conjugate pair $\alpha\pm i\beta$ of multiplicity $r$ contributes

$$
x^{\alpha}\left[\left(A_{0}+A_{1}\ln x+\cdots\right)\cos(\beta\ln x)+\left(B_{0}+B_{1}\ln x+\cdots\right)\sin(\beta\ln x)\right].
$$

The structure is identical to Section 2.3 with the dictionary $e^{mt}\leftrightarrow x^{m}$ and $t\leftrightarrow \ln x$. That dictionary is the reason the two theories are taught together.

### 2.7 Reduction theorem for Legendre's equation

> **Theorem (Legendre reduction).** Suppose $ax+b>0$ and set $ax+b=e^{t}$, $t=\ln(ax+b)$, $\theta=\frac{d}{dt}$. Then Legendre's equation of order $n$ becomes a constant-coefficient equation in $t$, in which the $k$-th derivative term carries the extra factor $a^{k}$.

$$
\left[a^{n}\theta(\theta-1)\cdots(\theta-n+1)+a_{1}a^{n-1}\theta(\theta-1)\cdots(\theta-n+2)+\cdots+a_{n-1}a\theta+a_{n}\right]y=f\!\left(\frac{e^{t}-b}{a}\right)
$$

The transformed right-hand member deserves attention. Since $ax+b=e^{t}$, the value of $x$ is $\frac{e^{t}-b}{a}$, and the forcing term must be rewritten in terms of $t$ before any particular integral is attempted. The factor $a^{k}$ is the only structural difference from the Euler case, and the factor is easy to justify: differentiating $y$ with respect to $x$ brings out a factor $a$ each time, because $t=\ln(ax+b)$ gives $\frac{dt}{dx}=\frac{a}{ax+b}$.

### 2.8 The exponential shift and particular integrals

> **Theorem (Exponential shift).** For a polynomial operator $P(D)$ with constant coefficients and a constant $\lambda$,

$$
P(D)\left[e^{\lambda x}u(x)\right]=e^{\lambda x}P(D+\lambda)u(x).
$$

The theorem is the main tool for particular integrals. Applied to $u=1$ it shows that $P(D)e^{\lambda x}=P(\lambda)e^{\lambda x}$, so an exponential is an eigenfunction of every constant-coefficient operator. Applied to $u=x$ it gives the modification needed when $P(\lambda)=0$.

> **Corollary (Particular integral for an exponential).** If $P(\lambda)\neq 0$, a particular integral of $P(D)y=e^{\lambda x}$ is $e^{\lambda x}/P(\lambda)$. If $\lambda$ is a root of $P$ of multiplicity $s$, a particular integral is $x^{s}e^{\lambda x}/P^{(s)}(\lambda)$, where $P^{(s)}$ is the $s$-th derivative of $P$.

The corollary translates immediately into the language of Euler equations, because $x^{r}=e^{rt}$ under the substitution. That translation is the content of the next result and is the single most useful computational shortcut in the topic.

> **Lemma (Particular integral for a power).** Consider the Cauchy–Euler equation with left-hand operator corresponding to the polynomial $P(\theta)$ in the variable $t$. If the forcing term is $x^{r}$, and $r$ is a root of $P$ of multiplicity $s$, then a particular integral is

$$
y_{p}=\frac{x^{r}(\ln x)^{s}}{P^{(s)}(r)} .
$$

When $s=0$, meaning $r$ is not a root at all, the formula reduces to $x^{r}/P(r)$ with no logarithmic factor. The factorial that appears in the constant-coefficient version of the rule is absent here only because it has been absorbed into the derivative $P^{(s)}$; the two statements agree, as the next worked example demonstrates.

### 2.9 The interval of validity

> **Lemma (Location of the singular point).** The Cauchy–Euler equation has a singular point at $x=0$, and Legendre's equation has one where $ax+b=0$. On an interval not containing that point the coefficients are continuous and the theory of Section 2.2 applies; across the point the equation must be treated separately on each side.

The practical consequence is that the substitution $x=e^{t}$ is a substitution for $x>0$, and a solution obtained that way is asserted on $(0,\infty)$. On $(-\infty,0)$ one writes $x=-e^{t}$ and obtains the same formulae with $x$ replaced by $|x|$ and $\ln x$ replaced by $\ln|x|$. Many textbooks abbreviate this by writing $\ln|x|$ throughout; the abbreviation is harmless provided one remembers what it stands for.

## 3. Formal Proofs, Derivations, and Methods

### 3.1 Derivation of the first identity

Take $x>0$ and $t=\ln x$, so $x=e^{t}$ and $\frac{dt}{dx}=\frac{1}{x}$. By the chain rule, differentiating with respect to $x$ is differentiating with respect to $t$ and then multiplying by $\frac{dt}{dx}$.

$$
\frac{dy}{dx}=\frac{dy}{dt}\cdot\frac{dt}{dx}=\frac{1}{x}\frac{dy}{dt}
$$

Multiplying both sides by $x$ removes the fraction.

$$
x\frac{dy}{dx}=\frac{dy}{dt}=\theta y
$$

That is the first identity. It is worth noting what it does not say: it does not say that $D=\theta$; it says that $xD=\theta$, and the factor $x$ is essential.

### 3.2 Derivation of the second identity

Apply the same chain rule to the first derivative, remembering that $\frac{dy}{dt}$ is itself a function of $t$ and hence of $x$.

$$
\frac{d^{2}y}{dx^{2}}=\frac{d}{dx}\left(\frac{1}{x}\frac{dy}{dt}\right)
$$

Differentiate the product, treating $\frac{dy}{dt}$ as a function of $x$ through $t$.

$$
\frac{d^{2}y}{dx^{2}}=-\frac{1}{x^{2}}\frac{dy}{dt}+\frac{1}{x}\cdot\frac{d}{dt}\left(\frac{dy}{dt}\right)\cdot\frac{dt}{dx}
$$

Since $\frac{dt}{dx}=\frac{1}{x}$ and $\frac{d}{dt}\left(\frac{dy}{dt}\right)=\frac{d^{2}y}{dt^{2}}=\theta^{2}y$, this becomes

$$
\frac{d^{2}y}{dx^{2}}=\frac{1}{x^{2}}\left(\theta^{2}-\theta\right)y .
$$

Multiplying by $x^{2}$ gives the second identity.

$$
x^{2}\frac{d^{2}y}{dx^{2}}=\left(\theta^{2}-\theta\right)y=\theta(\theta-1)y
$$

The derivation shows where the correction term $-\theta$ comes from: it is the derivative of the factor $\frac{1}{x}$, and it is exactly what distinguishes the Euler operator from a naive replacement of $D$ by $\theta$.

### 3.3 Induction proof of the general identity

> **Claim.** For every $k\ge 1$ the operator identity $x^{k}D^{k}=\theta(\theta-1)\cdots(\theta-k+1)$ holds on $x>0$.

Write $\theta^{\underline{k}}$ for the falling factorial $\theta(\theta-1)\cdots(\theta-k+1)$. The claim is that $x^{k}D^{k}=\theta^{\underline{k}}$, equivalently that $D^{k}=x^{-k}\theta^{\underline{k}}$.

The base case $k=1$ is Section 3.1. Assume the claim for $k$, so $D^{k}=x^{-k}\theta^{\underline{k}}$. Then $D^{k+1}=D\left(x^{-k}\theta^{\underline{k}}\right)$, and the product rule applied to the function $x^{-k}$ and the function $\theta^{\underline{k}}y$ gives

$$
D^{k+1}y=-kx^{-k-1}\theta^{\underline{k}}y+x^{-k}D\left(\theta^{\underline{k}}y\right).
$$

Now $\theta^{\underline{k}}$ is a polynomial in $\theta$ with constant coefficients, so it commutes with $\theta$, and $D=\frac{1}{x}\theta$ on such an expression. Hence

$$
x^{-k}D\left(\theta^{\underline{k}}y\right)=x^{-k}\cdot\frac{1}{x}\theta\,\theta^{\underline{k}}y=x^{-k-1}\theta^{\underline{k}+1}y .
$$

Adding the two contributions,

$$
D^{k+1}y=x^{-k-1}\left(\theta-k\right)\theta^{\underline{k}}y=x^{-k-1}\theta^{\underline{k+1}}y ,
$$

because $\theta^{\underline{k}}(\theta-k)$ is precisely the product of $k+1$ consecutive descending factors. Multiplying by $x^{k+1}$ completes the induction. The identity is therefore established for every $k\ge 1$.

The same induction run in reverse explains why the coefficients are not binomial coefficients: each step multiplies by a factor $(\theta-k)$ which is linear in $\theta$ with a constant term, and repeated multiplication of such factors produces the Stirling numbers.

### 3.4 Reduction of the Cauchy–Euler equation in full

Consider the normalised equation of order $n$ with constant coefficients $a_{1},\dots,a_{n}$.

$$
x^{n}y^{(n)}+a_{1}x^{n-1}y^{(n-1)}+\cdots+a_{n-1}xy'+a_{n}y=f(x)
$$

On $x>0$ substitute $x=e^{t}$ and apply the identity of Section 3.3 term by term. The term $x^{n}y^{(n)}$ becomes $\theta^{\underline{n}}y$, the term $a_{1}x^{n-1}y^{(n-1)}$ becomes $a_{1}\theta^{\underline{n-1}}y$, and so on down to $a_{n-1}\theta y$ and $a_{n}y$. The right-hand member $f(x)$ becomes $f(e^{t})$ because $x=e^{t}$. Collecting,

$$
\left[\theta^{\underline{n}}+a_{1}\theta^{\underline{n-1}}+\cdots+a_{n-1}\theta+a_{n}\right]y=f(e^{t}).
$$

Every coefficient in the bracket is now a constant, and the bracket is a polynomial in $\theta$ of degree $n$. Denote that polynomial by $P(\theta)$. The transformed equation is $P(\theta)y=f(e^{t})$, which is precisely the constant-coefficient problem solved by the auxiliary equation $P(m)=0$. Once $y$ is known as a function of $t$, the answer to the original problem is obtained by replacing $t$ by $\ln x$, because the substitution is invertible on $x>0$.

### 3.5 Derivation of the indicial equation by the power substitution

The reduction of Section 3.4 is the systematic route, but the homogeneous equation admits a shorter route that also explains the name indicial equation. Try a power function.

$$
y=x^{m}, \qquad y'=mx^{m-1}, \qquad y''=m(m-1)x^{m-2}
$$

In general the $k$-th derivative of $x^{m}$ is the falling factorial of $m$ of length $k$ multiplied by $x^{m-k}$.

$$
y^{(k)}=m(m-1)\cdots(m-k+1)x^{m-k}
$$

Multiply the $k$-th derivative by $x^{k}$, as the equation demands, and the powers of $x$ cancel exactly.

$$
x^{k}y^{(k)}=m(m-1)\cdots(m-k+1)x^{m}
$$

Substituting into the homogeneous equation and factoring out $x^{m}$, which never vanishes for $x>0$, leaves

$$
\left[m^{\underline{n}}+a_{1}m^{\underline{n-1}}+\cdots+a_{n-1}m+a_{n}\right]x^{m}=0 .
$$

The bracket is $P(m)$, the very polynomial obtained from $P(\theta)$ by replacing $\theta$ with the number $m$. The substitution therefore succeeds exactly when $m$ is a root of $P$, and it produces $n$ roots counted with multiplicity, matching the order. This is also the cleanest explanation of why the powers of $x$ must match the derivative orders: the cancellation above happens only because $x^{k}$ meets $x^{m-k}$.

### 3.6 Derivation of the repeated-root rule

Suppose $m_{0}$ is a root of $P$ of multiplicity $r$, so that $P(m)=(m-m_{0})^{r}R(m)$ with $R(m_{0})\neq 0$. In the $t$ variable the equation is $P(\theta)y=0$, and the constant-coefficient theory says the contribution of the root is $t^{j}e^{m_{0}t}$ for $j=0,1,\dots,r-1$. Translating with $t=\ln x$ and $e^{m_{0}t}=x^{m_{0}}$ gives $x^{m_{0}}(\ln x)^{j}$, which is the rule stated in Section 2.6.

The same conclusion can be reached without leaving the $x$ variable, and the second route is instructive. Consider the family $y=x^{m}$ and apply the operator: the result is $P(m)x^{m}$. Differentiate this identity with respect to the parameter $m$. The left side differentiates to $\frac{\partial}{\partial m}$ of the operator applied to $x^{m}$, and since the operator does not involve $m$, the derivative passes through it and acts on $x^{m}$, producing $x^{m}\ln x$. The right side differentiates by the product rule to $P'(m)x^{m}+P(m)x^{m}\ln x$. At $m=m_{0}$, where $P(m_{0})=0$, the identity collapses to

$$
P(\theta)\left(x^{m_{0}}\ln x\right)=P'(m_{0})\,x^{m_{0}} .
$$

When $m_{0}$ is a simple root, $P'(m_{0})\neq 0$, so $x^{m_{0}}\ln x$ solves the homogeneous equation. When $m_{0}$ is a double root, $P'(m_{0})=0$ as well, and one differentiates a second time to obtain $x^{m_{0}}(\ln x)^{2}$ up to a numerical factor. Continuing in this way produces exactly $r$ independent solutions, and the numerical factors are absorbed into the arbitrary constants.

### 3.7 Derivation of the complex-root rule

Suppose the indicial polynomial has the conjugate pair $\alpha\pm i\beta$ with $\beta\neq 0$. Formally the two solutions are $x^{\alpha+i\beta}$ and $x^{\alpha-i\beta}$, but a complex-valued solution is not acceptable for a real problem, so the pair is recombined.

$$
x^{\alpha+i\beta}=e^{(\alpha+i\beta)t}=e^{\alpha t}e^{i\beta t}=x^{\alpha}\left[\cos(\beta\ln x)+i\sin(\beta\ln x)\right]
$$

The real and imaginary parts of a complex solution of a real linear homogeneous equation are themselves solutions, so the real pair is

$$
x^{\alpha}\cos(\beta\ln x), \qquad x^{\alpha}\sin(\beta\ln x).
$$

The two are independent whenever $\beta\neq 0$, since their Wronskian equals $\beta x^{2\alpha-1}$, which is nonzero on any interval of positive $x$. When the pair has multiplicity $r$, the same differentiation-with-respect-to-parameter device of Section 3.6 inserts the powers $(\ln x)^{j}$ alongside each of the two real solutions.

### 3.8 Derivation of the Legendre identity

Let $u=ax+b$ with $a\neq 0$, $u>0$, and set $t=\ln u$. Then $\frac{dt}{dx}=\frac{dt}{du}\cdot\frac{du}{dx}=\frac{a}{u}$, so by the chain rule

$$
\frac{dy}{dx}=\frac{a}{u}\frac{dy}{dt}=\frac{a}{ax+b}\theta y .
$$

Multiplying by $ax+b$ gives the first Legendre identity.

$$
(ax+b)\frac{dy}{dx}=a\theta y
$$

For the second derivative, differentiate $\frac{a}{u}\theta y$ with respect to $x$, using the product rule.

$$
\frac{d^{2}y}{dx^{2}}=\frac{d}{dx}\left(\frac{a}{u}\right)\theta y+\frac{a}{u}\cdot\frac{d}{dx}\left(\theta y\right)
$$

Since $u=ax+b$ gives $\frac{du}{dx}=a$, the derivative of $a/u$ is $-a^{2}/u^{2}$, and the derivative of $\theta y$ is $\frac{a}{u}\theta^{2}y$.

$$
\frac{d^{2}y}{dx^{2}}=-\frac{a^{2}}{u^{2}}\theta y+\frac{a^{2}}{u^{2}}\theta^{2}y
$$

Multiplying by $u^{2}$ gives the clean statement for the second order.

$$
(ax+b)^{2}\frac{d^{2}y}{dx^{2}}=a^{2}\theta(\theta-1)y
$$

The pattern in the two lines above is the whole mechanism: each differentiation produces one factor $a$ from the chain rule and one factor $1/u$ from the derivative of the inner expression, and the factor $1/u$ is exactly what the power $u^{2}$ on the left removes.

The general identity follows by the same induction as Section 3.3, with each step picking up one further factor of $a$.

$$
(ax+b)^{k}\frac{d^{k}y}{dx^{k}}=a^{k}\theta(\theta-1)\cdots(\theta-k+1)y
$$

Substituting these into Legendre's equation of order $n$ produces the constant-coefficient equation of Section 2.7, and the right-hand member must be rewritten using $x=\frac{e^{t}-b}{a}$.

An equivalent way to see the same result is to set $u=ax+b$ as a new independent variable first. Then $\frac{d}{dx}=a\frac{d}{du}$, so $D_{x}^{k}=a^{k}D_{u}^{k}$, and the equation becomes a Cauchy–Euler equation in $u$ with coefficients $a^{k}$ attached to $u^{k}D_{u}^{k}$. Solving it by $u=e^{t}$ reproduces the factor $a^{k}$ and shows that Legendre's equation is nothing but an Euler equation in a shifted and rescaled variable.

### 3.9 Method: solving a Cauchy–Euler equation

The following procedure is complete and always works on $x>0$.

1. Write the equation in the normalised form, with the coefficient of $y^{(n)}$ exactly $x^{n}$. If the given leading coefficient is a constant multiple of $x^{n}$, divide through by that constant; if the leading coefficient is $x^{m}$ with $m\neq n$, the equation is not of Euler type.
2. Replace each operator $x^{k}D^{k}$ by its $\theta$-polynomial from the table in Section 2.4, working from the highest order downward so that no term is missed.
3. Rewrite the right-hand member as a function of $t$, using $x=e^{t}$.
4. Solve the resulting constant-coefficient equation: form the auxiliary equation $P(m)=0$, assemble the complementary function by the three root cases, and find one particular integral by the exponential-shift rule or by undetermined coefficients.
5. Return to $x$ by substituting $t=\ln x$ everywhere, using $e^{mt}=x^{m}$ and $e^{\alpha t}\cos\beta t=x^{\alpha}\cos(\beta\ln x)$.
6. Check the answer: the number of constants must equal the order, and the particular integral alone must satisfy the original equation when substituted, with the power of $x$ handled correctly.

### 3.10 Method: solving a Legendre equation

1. Identify $a$ and $b$ in the affine expression $ax+b$, and confirm that each derivative is accompanied by the matching power of that expression.
2. Set $ax+b=e^{t}$, so $t=\ln(ax+b)$, and record $\theta=\frac{d}{dt}$.
3. Replace $(ax+b)^{k}D^{k}$ by $a^{k}\theta(\theta-1)\cdots(\theta-k+1)$, including the factor $a^{k}$ in every term.
4. Rewrite the forcing term in $t$; this is the step most often omitted, and it cannot be skipped because the particular integral depends on it.
5. Solve the constant-coefficient problem, then return to $x$ by $e^{mt}=(ax+b)^{m}$ and $t=\ln(ax+b)$.
6. Verify by substituting the particular integral back into the original equation, differentiating with the chain rule and remembering the factor $a$ at each differentiation.

### 3.11 Method: particular integral by the power rule

When the forcing term is a power $x^{r}$ or a power of an affine expression, do not expand anything.

1. Convert the forcing term to $t$: $x^{r}=e^{rt}$, and $(ax+b)^{r}=e^{rt}$.
2. Compute $P(m)$, the auxiliary polynomial of the reduced equation.
3. If $P(r)\neq 0$, the particular integral is $e^{rt}/P(r)$, that is $x^{r}/P(r)$ or $(ax+b)^{r}/P(r)$.
4. If $P(r)=0$, find the multiplicity $s$ of $r$ as a root, and use $t^{s}e^{rt}/P^{(s)}(r)$; the $t^{s}$ becomes $(\ln x)^{s}$ or $(\ln(ax+b))^{s}$ on returning.
5. If the forcing term is a sum, treat each summand separately and add the results, by linearity.
6. Check the particular integral by substitution; a sign error in $P^{(s)}(r)$ is invisible in the algebra and fatal in the answer.

## 4. Representative Worked Examples and Solutions

### 4.1 Problem: an order-four equation with a repeated complex pair

Solve the homogeneous equation

$$
\frac{d^{4}y}{dx^{4}}+2\frac{d^{2}y}{dx^{2}}+y=0 .
$$

### 4.2 Solution: factor the operator as a perfect square

Step 1. Write the equation in operator form and recognise the left-hand side as a perfect square in $D^{2}$.

$$
\left(D^{4}+2D^{2}+1\right)y=0
$$

Step 2. Factor.

$$
\left(D^{2}+1\right)^{2}y=0
$$

Step 3. Read the auxiliary equation and its roots, with multiplicity.

$$
(m^{2}+1)^{2}=0 \qquad\Longrightarrow\qquad m=\pm i \text{ each of multiplicity } 2
$$

Step 4. Apply the complex-root rule with multiplicity two: each of $\cos x$ and $\sin x$ is accompanied by a polynomial of degree one in $x$.

$$
y_{c}=\left(c_{1}+c_{2}x\right)\cos x+\left(c_{3}+c_{4}x\right)\sin x
$$

Step 5. Count the constants. The equation is of order four and the answer carries four constants, so the count is consistent.

Step 6. Verify the hardest member, $y=x\cos x$. Differentiate twice.

$$
y'=\cos x-x\sin x, \qquad y''=-2\sin x-x\cos x
$$

Step 7. Apply $D^{2}+1$ to $y$. Since $y''+y=-2\sin x$, the first application gives $-2\sin x$.

$$
\left(D^{2}+1\right)\left(x\cos x\right)=-2\sin x
$$

Step 8. Apply $D^{2}+1$ a second time. Because $\left(-2\sin x\right)''+(-2\sin x)=2\sin x-2\sin x=0$, the double application annihilates the function.

$$
\left(D^{2}+1\right)^{2}\left(x\cos x\right)=0
$$

Step 9. Conclude. The four functions $\cos x$, $x\cos x$, $\sin x$, $x\sin x$ are independent, and $y_{c}$ above is the general solution.

### 4.3 Problem: a third-order Cauchy–Euler equation with a repeated root

Solve

$$
x^{3}\frac{d^{3}y}{dx^{3}}-2x^{2}\frac{d^{2}y}{dx^{2}}+4x\frac{dy}{dx}-4y=x^{3}, \qquad x>0 .
$$

### 4.4 Solution: reduce with $\theta$, then treat the resonance

Step 1. Substitute the operator identities, working from the top down.

$$
x^{3}D^{3}=\theta^{3}-3\theta^{2}+2\theta, \qquad x^{2}D^{2}=\theta^{2}-\theta, \qquad xD=\theta
$$

Step 2. Assemble the reduced left-hand side.

$$
\left(\theta^{3}-3\theta^{2}+2\theta\right)-2\left(\theta^{2}-\theta\right)+4\theta-4
$$

Step 3. Simplify by collecting powers of $\theta$.

$$
\theta^{3}-5\theta^{2}+8\theta-4
$$

Step 4. Rewrite the forcing term in $t$, using $x=e^{t}$ so that $x^{3}=e^{3t}$.

$$
\left(\theta^{3}-5\theta^{2}+8\theta-4\right)y=e^{3t}
$$

Step 5. Factor the auxiliary polynomial by testing the root $m=1$.

$$
m^{3}-5m^{2}+8m-4=(m-1)(m-2)^{2}
$$

Step 6. Since $m=2$ is a double root, the complementary function in $t$ carries both $e^{2t}$ and $t e^{2t}$.

$$
y_{c}=c_{1}e^{t}+\left(c_{2}+c_{3}t\right)e^{2t}
$$

Step 7. For the particular integral, note that the exponent $3$ is not a root of the auxiliary polynomial, so no logarithmic factor is needed.

$$
y_{p}=\frac{e^{3t}}{P(3)}=\frac{e^{3t}}{27-45+24-4}=\frac{e^{3t}}{2}
$$

Step 8. Return to $x$ with $e^{t}=x$ and $t=\ln x$.

$$
y=c_{1}x+\left(c_{2}+c_{3}\ln x\right)x^{2}+\frac{x^{3}}{2}
$$

Step 9. Verify the particular integral by direct substitution, which is essential here because the coefficients are variable. For $y=\frac{1}{2}x^{3}$ the derivatives are $y'=\frac{3}{2}x^{2}$, $y''=3x$ and $y'''=3$.

$$
x^{3}(3)-2x^{2}(3x)+4x\left(\frac{3}{2}x^{2}\right)-4\left(\frac{x^{3}}{2}\right)=3x^{3}-6x^{3}+6x^{3}-2x^{3}=x^{3}
$$

Step 10. Verify the repeated-root member $y=x^{2}\ln x$, whose derivatives are $y'=2x\ln x+x$, $y''=2\ln x+3$ and $y'''=\frac{2}{x}$.

$$
x^{3}\cdot\frac{2}{x}-2x^{2}\left(2\ln x+3\right)+4x\left(2x\ln x+x\right)-4x^{2}\ln x
$$

Step 11. Collect the coefficients of $x^{2}$ and of $x^{2}\ln x$ separately; both vanish.

$$
x^{2}\left(2-6+4\right)+x^{2}\ln x\left(-4+8-4\right)=0
$$

Step 12. Conclude that the general solution is the one stated in Step 8, with three constants for an equation of order three.

### 4.5 Problem: Legendre's equation with a repeated root and a logarithmic forcing

Solve

$$
(x+2)^{2}\frac{d^{2}y}{dx^{2}}-(x+2)\frac{dy}{dx}+y=\ln(x+2), \qquad x>-2 .
$$

### 4.6 Solution: reduce with $ax+b=e^{t}$ and find the particular integral by undetermined coefficients

Step 1. Identify the affine expression $u=x+2$, so $a=1$ and $b=2$, and set $x+2=e^{t}$ with $\theta=\frac{d}{dt}$.

Step 2. Apply the Legendre identities with $a=1$.

$$
(x+2)^{2}D^{2}=\theta(\theta-1), \qquad (x+2)D=\theta
$$

Step 3. Assemble the reduced operator.

$$
\theta(\theta-1)-\theta+1=\theta^{2}-2\theta+1=(\theta-1)^{2}
$$

Step 4. Rewrite the right-hand member, since $\ln(x+2)=t$.

$$
(\theta-1)^{2}y=t
$$

Step 5. The auxiliary equation is $(m-1)^{2}=0$, a double root at $m=1$, so the complementary function in $t$ is linear in $t$ times $e^{t}$.

$$
y_{c}=\left(c_{1}+c_{2}t\right)e^{t}
$$

Step 6. For the particular integral look for a linear function of $t$, since the right-hand side is linear and the operator is a repeated first-degree factor. Write $y=At+B$.

$$
(\theta-1)(At+B)=A-At-B=-At+(A-B)
$$

Step 7. Apply the operator a second time.

$$
(\theta-1)\left[-At+(A-B)\right]=-A-\left[-At+(A-B)\right]=At+(-2A+B)
$$

Step 8. Match coefficients against $t$, which is $1\cdot t+0$.

$$
A=1, \qquad -2A+B=0 \qquad\Longrightarrow\qquad A=1,\quad B=2
$$

Step 9. So the particular integral is $y_{p}=t+2$, and returning to $x$ gives the general solution.

$$
y=\left(c_{1}+c_{2}\ln(x+2)\right)(x+2)+\ln(x+2)+2
$$

Step 10. Verify the particular integral by differentiating with respect to $x$. For $y=\ln(x+2)+2$,

$$
y'=\frac{1}{x+2}, \qquad y''=-\frac{1}{(x+2)^{2}} .
$$

Step 11. Substitute, keeping every power of $x+2$ attached to its derivative.

$$
(x+2)^{2}\left(-\frac{1}{(x+2)^{2}}\right)-(x+2)\cdot\frac{1}{x+2}+\ln(x+2)+2
$$

Step 12. Simplify; the three constants combine to leave only the required logarithmic term.

$$
-1-1+\ln(x+2)+2=\ln(x+2)
$$

The verification confirms both the particular integral and the two constants $2$ that were carried along with it.

### 4.7 Problem: a Cauchy–Euler equation with complex roots and a logarithmic forcing

Solve

$$
x^{2}\frac{d^{2}y}{dx^{2}}+x\frac{dy}{dx}+y=\ln x, \qquad x>0 .
$$

### 4.8 Solution: complex roots plus a particular integral that is linear in $t$

Step 1. Reduce the left-hand side.

$$
\left[\theta(\theta-1)+\theta+1\right]y=\left(\theta^{2}+1\right)y
$$

Step 2. Rewrite the right-hand member as $t$.

$$
\left(\theta^{2}+1\right)y=t
$$

Step 3. The auxiliary equation $m^{2}+1=0$ has roots $\pm i$, so the complementary function is a cosine-sine pair in $t$.

$$
y_{c}=c_{1}\cos t+c_{2}\sin t
$$

Step 4. Look for a particular integral that is linear in $t$, writing $y=At+B$. Since the second derivative of a linear function is zero,

$$
\left(\theta^{2}+1\right)(At+B)=0+(At+B)=At+B .
$$

Step 5. Match against $t$ to obtain $A=1$ and $B=0$, so $y_{p}=t$.

Step 6. Return to $x$.

$$
y=c_{1}\cos(\ln x)+c_{2}\sin(\ln x)+\ln x
$$

Step 7. Verify the particular integral $y=\ln x$, whose derivatives are $y'=\frac{1}{x}$ and $y''=-\frac{1}{x^{2}}$.

$$
x^{2}\left(-\frac{1}{x^{2}}\right)+x\cdot\frac{1}{x}+\ln x=-1+1+\ln x=\ln x
$$

Step 8. Interpret. The cosine-sine pair oscillates in $\ln x$, meaning that the oscillations become slower as $x$ grows; the term $\ln x$ grows without bound. Both features are typical of an equidimensional equation and both would be missed if the reduced variable $t$ were not interpreted.

### 4.9 Problem: a third-order Legendre equation with a power forcing

Solve

$$
(2x+1)^{3}\frac{d^{3}y}{dx^{3}}-6(2x+1)^{2}\frac{d^{2}y}{dx^{2}}+24(2x+1)\frac{dy}{dx}-48y=(2x+1)^{4}.
$$

### 4.10 Solution: carry the factor $a^{3}=8$ through every term

Step 1. Identify $a=2$ and $b=1$, and set $2x+1=e^{t}$ with $\theta=\frac{d}{dt}$.

Step 2. Apply the Legendre identities with $a=2$, noting the factors $2$, $4$ and $8$.

$$
(2x+1)D=2\theta, \qquad (2x+1)^{2}D^{2}=4\theta(\theta-1), \qquad (2x+1)^{3}D^{3}=8\theta(\theta-1)(\theta-2)
$$

Step 3. Substitute into the left-hand side.

$$
8\theta(\theta-1)(\theta-2)-6\cdot 4\theta(\theta-1)+24\cdot 2\theta-48
$$

Step 4. Expand the first product and collect.

$$
8\left(\theta^{3}-3\theta^{2}+2\theta\right)-24\left(\theta^{2}-\theta\right)+48\theta-48
$$

$$
8\theta^{3}-48\theta^{2}+88\theta-48
$$

Step 5. Factor out $8$ and factor the cubic, testing $m=1$.

$$
8\left(\theta^{3}-6\theta^{2}+11\theta-6\right)=8(\theta-1)(\theta-2)(\theta-3)
$$

Step 6. Rewrite the forcing term, since $(2x+1)^{4}=e^{4t}$.

$$
8(\theta-1)(\theta-2)(\theta-3)y=e^{4t}
$$

Step 7. The complementary function has three distinct real roots, so it is a sum of three powers of $2x+1$.

$$
y_{c}=c_{1}(2x+1)+c_{2}(2x+1)^{2}+c_{3}(2x+1)^{3}
$$

Step 8. The exponent $4$ is not a root, so the particular integral follows the simple rule with the polynomial evaluated at $4$.

$$
P(4)=8(3)(2)(1)=48, \qquad y_{p}=\frac{e^{4t}}{48}=\frac{(2x+1)^{4}}{48}
$$

Step 9. State the general solution.

$$
y=c_{1}(2x+1)+c_{2}(2x+1)^{2}+c_{3}(2x+1)^{3}+\frac{(2x+1)^{4}}{48}
$$

Step 10. Verify the particular integral directly, writing $u=2x+1$ and $y=\frac{u^{4}}{48}$. Then $y'=\frac{4u^{3}\cdot 2}{48}=\frac{u^{3}}{6}$, $y''=\frac{3u^{2}\cdot 2}{6}=u^{2}$ and $y'''=2u\cdot 2=4u$.

Step 11. Substitute into the original left-hand side.

$$
u^{3}(4u)-6u^{2}\left(u^{2}\right)+24u\left(\frac{u^{3}}{6}\right)-48\left(\frac{u^{4}}{48}\right)
$$

Step 12. Simplify term by term; the total is exactly the required power.

$$
4u^{4}-6u^{4}+4u^{4}-u^{4}=u^{4}=(2x+1)^{4}
$$

The verification also confirms the three factors of $a$ that were inserted in Step 2: omitting them would have produced a mismatch by a factor of $8$ in the leading term.

### 4.11 Problem: verify a repeated-root solution of an Euler equation

Show that $y=x^{2}\ln x$ satisfies $x^{2}y''-3xy'+4y=0$ and state the general solution.

### 4.12 Solution: differentiate and substitute

Step 1. Reduce the equation to check which auxiliary polynomial it corresponds to.

$$
\theta(\theta-1)-3\theta+4=\theta^{2}-4\theta+4=(\theta-2)^{2}
$$

Step 2. The auxiliary equation has the double root $m=2$, so the general solution should be $\left(c_{1}+c_{2}\ln x\right)x^{2}$. That prediction is what the verification must confirm.

Step 3. Differentiate the proposed solution twice.

$$
y=x^{2}\ln x, \qquad y'=2x\ln x+x, \qquad y''=2\ln x+3
$$

Step 4. Substitute into the left-hand side, attaching the correct power of $x$ to each derivative.

$$
x^{2}\left(2\ln x+3\right)-3x\left(2x\ln x+x\right)+4x^{2}\ln x
$$

Step 5. Expand.

$$
2x^{2}\ln x+3x^{2}-6x^{2}\ln x-3x^{2}+4x^{2}\ln x
$$

Step 6. Collect the coefficients of $x^{2}\ln x$ and of $x^{2}$; both are zero.

$$
x^{2}\ln x\left(2-6+4\right)+x^{2}\left(3-3\right)=0
$$

Step 7. Confirm that $y=x^{2}$ also solves the equation, by the same computation with $y'=2x$ and $y''=2$.

$$
2x^{2}-3x(2x)+4x^{2}=2x^{2}-6x^{2}+4x^{2}=0
$$

Step 8. State the general solution, with two constants for an equation of order two.

$$
y=\left(c_{1}+c_{2}\ln x\right)x^{2}
$$

Step 9. Interpret. The presence of $\ln x$ rather than a second power such as $x^{3}$ is the signature of the repeated root; a student who writes $c_{1}x^{2}+c_{2}x^{3}$ has used the distinct-root rule in a situation where it does not apply.

## 5. Mathematical Extensions, Limits, and Common Errors

### 5.1 What the reduction does and does not achieve

The substitution $x=e^{t}$ is exact and reversible on $x>0$; it is not an approximation, an expansion, or a guess. It changes the independent variable and nothing else, so every solution of the reduced equation corresponds to exactly one solution of the original and conversely. What the substitution does not do is enlarge the class of solvable equations. It works precisely because the coefficients are powers of $x$ matching the derivative orders; applied to any other equation it produces a new equation with variable coefficients in $t$, and the constant-coefficient machinery does not apply.

A useful way to see the limitation is to ask what makes the cancellation in Section 3.5 happen. The power $x^{k}$ meets the factor $x^{m-k}$ produced by differentiating $x^{m}$, and the product is $x^{m}$ regardless of $k$. If any coefficient fails to be a constant multiple of $x^{k}$, the resulting expression retains a power of $x$, the auxiliary polynomial acquires coefficients depending on $x$, and the method collapses.

### 5.2 Behaviour near the singular point

The point $x=0$ is a singular point of every Cauchy–Euler equation, and the point $x=-b/a$ is a singular point of every Legendre equation. Solutions may blow up, oscillate infinitely often, or remain bounded as the singular point is approached, depending on the real parts of the indicial roots. A root with positive real part produces a solution that vanishes at the origin; a root with negative real part produces one that blows up; a purely imaginary root produces one that oscillates without limit as $\ln x\to-\infty$. None of these statements can be inferred from the constant-coefficient theory alone, because the map from $t$ to $x$ compresses the whole negative half-line of $t$ into the interval $(0,1)$.

This is also why the interval of validity must be stated as part of the answer. A solution asserted for all $x$ of an Euler equation is usually a solution only on one side of the origin.

### 5.3 Resonance: when the forcing matches a root

The most common source of lost marks in this topic is a particular integral proposed in the wrong form because the forcing term matches a root of the auxiliary polynomial. In the constant-coefficient setting the rule is that the trial function must be multiplied by $x^{s}$, where $s$ is the multiplicity of the exponent as a root. In the Euler setting the multiplier is $(\ln x)^{s}$, and the divisor becomes the derivative $P^{(s)}$ rather than $P$ itself.

The rule has a physical reading. Resonance means that the forcing is applied at a frequency the system already supports freely, so the response grows in amplitude rather than settling; the unbounded factor is the mathematical trace of that growth. A trial function without the extra factor will produce an equation with no solution, and the failure is easy to spot if one always substitutes the trial function back before solving for the constants.

### 5.4 Errors in the operator identities

The identities of Section 2.4 are the point at which most errors are introduced, and nearly all of them come from confusing the falling factorial with a binomial expansion. The correct expansions are the following, and they should be memorised in this form.

$$
x^{2}D^{2}=\theta^{2}-\theta
$$

$$
x^{3}D^{3}=\theta^{3}-3\theta^{2}+2\theta
$$

$$
x^{4}D^{4}=\theta^{4}-6\theta^{3}+11\theta^{2}-6\theta
$$

Writing $x^{3}D^{3}=\theta^{3}-3\theta^{2}+3\theta-1$ is writing $(\theta-1)^{3}$, which is a different operator and belongs to a different equation. Writing $x^{2}D^{2}=\theta^{2}$ omits the first-derivative term entirely and changes the order of the reduced equation's characteristic polynomial.

A second family of errors concerns the right-hand member. It must be converted to $t$ before the particular integral is computed, and the conversion is not cosmetic: the value of the particular integral is $e^{rt}/P(r)$, and the exponent $r$ depends on that conversion. Leaving the right-hand side as $\ln x$ while the operator is written in $\theta$ produces a meaningless expression.

A third family concerns the factor $a^{k}$ in Legendre's equation. Writing $(2x+1)^{2}y''=\theta(\theta-1)y$ instead of $4\theta(\theta-1)y$ introduces an error of a factor of four in one term only, which then propagates into wrong roots and a wrong answer that still looks plausible. Substituting the final answer back into the original equation catches this error immediately, which is why the substitution check is part of every worked example in this note.

### 5.5 A checklist of errors, stated positively

The auxiliary polynomial must be formed from the reduced operator, not from the given operator with $\theta$ replaced by $m$ in the original variable-coefficient expression.

The number of constants in the complementary function must equal the order of the equation, and a repeated root of multiplicity $r$ supplies $r$ of them.

A complex pair contributes two real functions, never a complex exponential left in the answer.

The particular integral carries no arbitrary constant; if a constant survives the determination of the coefficients, something has been included that belongs to the complementary function.

When the forcing term is a sum, each term is treated separately and the particular integrals are added; a single trial function covering a sum of a power and a logarithm will not work.

The final answer must be checked by substitution into the original equation, with the variable coefficients preserved. Checking against the reduced equation alone verifies the algebra of the reduction but not the correctness of the operator identities, and it is the identities that are most often wrong.

### 5.6 Extension: what lies beyond this family

The idea behind the Euler reduction generalises. An equation is called Fuchsian at a point when its coefficients behave like powers of the distance to that point, and for such equations a solution in the form of a power series with an unknown exponent can be attempted. The exponent is determined by an indicial equation of exactly the kind encountered in Section 2.6, and the powers $(\ln x)^{j}$ appear when the indicial equation has repeated roots. Bessel's equation and the hypergeometric equation are the classical examples, and both are solved by this method.

There is also a structural reason for the recurrence of logarithms. When the indicial equation has a repeated root, the two solutions that the differential equation ought to provide are degenerate, and the second must be manufactured by differentiating the first with respect to the exponent. That device, introduced in Section 3.6, is the same device used in the Frobenius method, and the logarithm is its universal signature.

Finally, the operator identity of Section 2.4 is a special case of a general principle: a change of the independent variable transforms a linear differential operator into another linear differential operator, and the coefficient functions transform by a definite rule involving the derivatives of the change of variable. The Euler and Legendre substitutions are the two cases in which that rule produces constant coefficients, which is precisely why these two families, among all variable-coefficient equations, are the ones that can always be solved in closed form.
