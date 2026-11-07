## 1. Foundational Concepts, Definitions, and Axioms

### 1.1 The object of study

The topic concerns one narrow but central class of differential equations: second-order, linear, homogeneous, with constant coefficients. Each of those four adjectives removes something from the general second-order equation, and each removal is what makes a complete solution possible.

> **Definition (Second-order linear equation).** A second-order linear differential equation in the dependent variable $y$ and the independent variable $x$ is an equation that can be written in the form
>
> $$
> a_0(x)\frac{d^{2}y}{dx^{2}}+a_1(x)\frac{dy}{dx}+a_2(x)y=F(x),
> $$
>
> where the coefficients $a_0$, $a_1$, $a_2$ and the forcing term $F$ are functions of $x$ alone, and $a_0$ is not identically zero.

The restriction that the coefficients depend on $x$ alone is what excludes products such as $y\frac{dy}{dx}$ and powers such as $\left(\frac{dy}{dx}\right)^{2}$. The restriction $a_0\neq 0$ is what keeps the order at two; if $a_0$ vanished on an interval the equation would degenerate to first order there.

> **Definition (Second-order homogeneous linear equation with constant coefficients).** When $a_0$, $a_1$ and $a_2$ are constants with $a_0\neq 0$ and $F$ is identically zero, the equation
>
> $$
> a_0\frac{d^{2}y}{dx^{2}}+a_1\frac{dy}{dx}+a_2y=0
> $$
>
> is called a second-order homogeneous linear equation with constant coefficients.

This is the object studied for the remainder of the note. Every technique below applies to it, and every theorem is stated for it.

### 1.2 The linear differential operator

The three operations of taking a multiple of the second derivative, a multiple of the first derivative, and a multiple of the function can be bundled into a single instruction.

> **Definition (Linear operator).** For constants $a_0$, $a_1$, $a_2$ the symbol $L$ defined by
>
> $$
> L[y]=a_0\frac{d^{2}y}{dx^{2}}+a_1\frac{dy}{dx}+a_2y
> $$
>
> is called a second-order linear differential operator with constant coefficients.

The defining property of such an operator is that it respects addition and scalar multiplication: for any twice differentiable functions $y_1$, $y_2$ and any constants $c_1$, $c_2$,

$$
L\left[c_1y_1+c_2y_2\right]=c_1L[y_1]+c_2L[y_2] .
$$

That single identity is the source of everything that follows, because it is exactly the statement that the equation $L[y]=0$ has a two-dimensional family of solutions closed under addition.

### 1.3 Homogeneous and non-homogeneous

> **Definition (Homogeneous).** The equation $L[y]=0$ is homogeneous. The equation $L[y]=F(x)$ with $F$ not identically zero is non-homogeneous, and $F$ is called the forcing term or the non-homogeneous part.

The terminology is a statement about the degree of each term. In $L[y]=0$ every term contains $y$ or one of its derivatives exactly once, so all terms are of degree one in the unknown; nothing is left over. Once a term free of $y$ is added, the balance is broken and the equation is non-homogeneous.

Three illustrations fix the distinction. The equation

$$
2\frac{d^{2}y}{dx^{2}}+5\frac{dy}{dx}-6y=xe^{x}
$$

is non-homogeneous because of the term $xe^{x}$. The equation

$$
\frac{d^{2}y}{dx^{2}}-3\frac{dy}{dx}+7y=\sin x+x^{2}
$$

is non-homogeneous because of the trigonometric and polynomial forcing. The equation

$$
\frac{d^{2}y}{dx^{2}}-3\frac{dy}{dx}+7y=0
$$

is homogeneous.

The consequences differ sharply. The zero function always solves a homogeneous equation, since $L[0]=0$. The zero function never solves a non-homogeneous equation, since $L[0]=0\neq F$. Moreover, the solution set of a homogeneous equation is a vector space, whereas the solution set of a non-homogeneous equation is a translated copy of that space, obtained by adding any single particular solution.

### 1.4 Linear and non-linear

> **Definition (Linearity).** An $n$-th order equation
>
> $$
> a_0(x)\frac{d^{n}y}{dx^{n}}+a_1(x)\frac{d^{n-1}y}{dx^{n-1}}+\cdots+a_n(x)y=F(x)
> $$
>
> is linear when three conditions hold simultaneously: every one of $y$ and its derivatives occurs to the first power; every coefficient, and the right-hand side, is a function of $x$ alone; and no term multiplies one derivative by another or by $y$.

Failure of any one condition makes the equation non-linear. The three examples below fail in three different ways, and each is worth recognising immediately.

The equation

$$
5x\frac{d^{3}y}{dx^{3}}+8xy\frac{d^{2}y}{dx^{2}}-9\frac{dy}{dx}+xy=xe^{x}
$$

fails the second condition, because the coefficient of the second derivative contains $y$. A coefficient is not permitted to depend on the unknown.

The equation

$$
3\frac{d^{2}y}{dx^{2}}-2\left(\frac{dy}{dx}\right)^{2}+8y=\ln x
$$

fails the first condition, because the first derivative is squared. The degree of that derivative is two rather than one.

The equation

$$
5\frac{d^{2}y}{dx^{2}}-8x\frac{dy}{dx}+2y=xy
$$

fails the second condition on the right-hand side, since $xy$ is not a function of $x$ alone. Moving the term to the left produces a coefficient of $y$ that depends on $y$, which is equally forbidden.

A fourth kind of failure is a non-linear function of the unknown, as in $\frac{d^{2}y}{dx^{2}}+\sin y=0$. Linearity is not a matter of degree of difficulty; it is a structural property that determines whether superposition is available.

### 1.5 Operator notation

> **Definition (The operator $D$).** The symbol $D$ denotes differentiation with respect to $x$, so that $Dy=\frac{dy}{dx}$, $D^{2}y=\frac{d^{2}y}{dx^{2}}$, and in general $D^{k}y=\frac{d^{k}y}{dx^{k}}$.

With this notation the equation

$$
5\frac{d^{2}y}{dx^{2}}-3\frac{dy}{dx}+8y=0
$$

is written as

$$
5D^{2}y-3Dy+8y=0 ,
$$

or, with the operator collected,

$$
\left(5D^{2}-3D+8\right)y=0 .
$$

In general,

$$
\left(a_0D^{2}+a_1D+a_2\right)y=0 ,
$$

and writing $f(D)=a_0D^{2}+a_1D+a_2$ gives the compact form

$$
f(D)y=0 .
$$

The object $f(D)$ is a polynomial in the operator $D$; it is a polynomial whose variable happens to denote differentiation. Two such polynomials may be multiplied and the order of multiplication does not matter, so $f(D)g(D)=g(D)f(D)$ whenever both have constant coefficients. That commutativity is used silently whenever the characteristic polynomial is factored.

### 1.6 The characteristic equation

> **Definition (Auxiliary or characteristic equation).** For the equation $a_0\frac{d^{2}y}{dx^{2}}+a_1\frac{dy}{dx}+a_2y=0$ with $a_0\neq 0$, the quadratic
>
> $$
> a_0m^{2}+a_1m+a_2=0
> $$
>
> is called the auxiliary equation, or characteristic equation, and its roots are called the characteristic roots.

The equation is obtained by replacing $D$ with the number $m$ in the polynomial $f(D)$. This substitution is not a formal trick with no content: Section 3.1 shows that it is exactly what the trial function $y=e^{mx}$ produces, and every characteristic root therefore corresponds to a genuine solution.

The discriminant

$$
\Delta=a_1^{2}-4a_0a_2
$$

decides which of the three cases occurs. If $\Delta>0$ the roots are real and distinct, if $\Delta=0$ there is one real root of multiplicity two, and if $\Delta<0$ the roots form a conjugate complex pair. Because $a_0$, $a_1$, $a_2$ are real, the complex case always produces a conjugate pair rather than a single complex root.

### 1.7 The solution space and the general solution

> **Definition (Solution space).** The set of all solutions of $L[y]=0$ on an interval $I$ is denoted by $S$. By superposition, $S$ is a vector space over the real numbers.

> **Definition (Fundamental set).** A pair of solutions $y_1$, $y_2$ of $L[y]=0$ is called a fundamental set on $I$ when every solution on $I$ can be written as $c_1y_1+c_2y_2$ with constant coefficients. Equivalently, the pair is fundamental when the two solutions are linearly independent.

> **Definition (General solution).** If $y_1$ and $y_2$ form a fundamental set, the expression $y=c_1y_1+c_2y_2$ with arbitrary constants $c_1$, $c_2$ is called the general solution of the equation.

The general solution therefore carries exactly two arbitrary constants, which is the number of independent solutions, which in turn equals the order. A claimed general solution with one constant is not general, and one with three constants is not a general solution of a second-order equation but of something else.

### 1.8 Linear independence and the Wronskian

> **Definition (Linear independence).** Two functions $y_1$, $y_2$ defined on an interval $I$ are linearly independent there when the identity $c_1y_1+c_2y_2=0$ on $I$ forces $c_1=c_2=0$. Otherwise they are linearly dependent, which means one is a constant multiple of the other.

> **Definition (Wronskian).** The Wronskian of two differentiable functions $y_1$, $y_2$ is the determinant
>
> $$
> W(x)=y_1y_2'-y_2y_1' .
> $$

The Wronskian converts a question about functions into a question about a single expression that can often be computed in one line. For solutions of a second-order linear equation the Wronskian is either identically zero or never zero on the interval, so its value at a single convenient point settles the matter. The precise statement is Theorem 2.4.

Two computations illustrate the idea. For $y_1=e^{2x}$ and $y_2=e^{3x}$,

$$
W=e^{2x}\cdot 3e^{3x}-e^{3x}\cdot 2e^{2x}=e^{5x} ,
$$

which is never zero, so the pair is independent. For $y_1=e^{2x}$ and $y_2=5e^{2x}$,

$$
W=e^{2x}\cdot 10e^{2x}-5e^{2x}\cdot 2e^{2x}=0 ,
$$

so the pair is dependent and the second function contributes nothing new.

### 1.9 Initial value problems

> **Definition (Initial value problem).** The problem of solving $L[y]=0$ subject to prescribed values $y(x_0)=A$ and $y'(x_0)=B$ at a single point $x_0$ is called an initial value problem.

Two conditions are imposed because two constants must be determined. The conditions must be of the values-and-slope type at one point, not values at two different points, if the standard existence theorem is to apply. A boundary value problem, which prescribes values at two different points, may have no solution or infinitely many, and is a different kind of question.

The constants are found by substitution, and the resulting pair of linear equations always has a unique solution when the Wronskian of the fundamental set is non-zero at $x_0$. In matrix form the system is

$$
\begin{aligned}
c_1y_1(x_0)+c_2y_2(x_0) &= A ,\\
c_1y_1'(x_0)+c_2y_2'(x_0) &= B ,
\end{aligned}
$$

whose determinant is precisely $W(x_0)$. This is the reason the Wronskian appears in the theory of initial value problems: it is the determinant of the system that determines the constants.

## 2. Theorems, Lemmas, and Analytical Properties

### 2.1 The superposition principle

> **Theorem (Superposition).** Let $L$ be a linear differential operator with constant coefficients. If $L[y_1]=0$ and $L[y_2]=0$, then $L[c_1y_1+c_2y_2]=0$ for all constants $c_1$, $c_2$. More generally, if $L[y_p]=F$ then $L[y_p+c_1y_1+c_2y_2]=F$.

Proof. Differentiation is linear, so for each $k$ the identity

$$
D^{k}\left(c_1y_1+c_2y_2\right)=c_1D^{k}y_1+c_2D^{k}y_2
$$

holds. Multiplying by $a_{2-k}$ and summing over $k=0,1,2$ gives

$$
L\left[c_1y_1+c_2y_2\right]=c_1L[y_1]+c_2L[y_2]=c_1\cdot 0+c_2\cdot 0=0 .
$$

For the second statement, $L[y_p+c_1y_1+c_2y_2]=F+0=F$. This completes the proof.

The theorem fails for non-linear equations, and the failure is not a technicality. For $\frac{d^{2}y}{dx^{2}}+y^{2}=0$, the function $y=0$ is a solution, but doubling a non-zero solution does not give a solution, because the squared term doubles by a factor of four while the derivative doubles by a factor of two.

### 2.2 Dimension of the solution space

> **Theorem (Dimension two).** If $p$ and $q$ are continuous on an interval $I$, the solution space of $y''+p(x)y'+q(x)y=0$ on $I$ is a two-dimensional real vector space.

Proof. For each pair of real numbers $A$, $B$ and each point $x_0$ in $I$, the standard existence and uniqueness theorem supplies exactly one solution on $I$ with $y(x_0)=A$ and $y'(x_0)=B$. Define the evaluation map $E:S\to\mathbb{R}^{2}$ by $E[y]=\left(y(x_0),y'(x_0)\right)$. The map is linear because evaluation and differentiation are linear. It is injective, since two solutions with the same value and the same derivative at $x_0$ coincide by uniqueness. It is surjective, since every pair is attained. Hence $S$ is isomorphic to $\mathbb{R}^{2}$ and has dimension two, so every fundamental set has exactly two members and every general solution exactly two constants. This completes the proof.

The theorem is stated for continuous coefficients; for constant coefficients it applies on the whole real line. Its practical content is that two independent solutions are always enough, and never fewer.

### 2.3 The three-case theorem

> **Theorem (Solution of the constant-coefficient equation).** Let $a_0\frac{d^{2}y}{dx^{2}}+a_1\frac{dy}{dx}+a_2y=0$ with $a_0\neq 0$ and real constants, and let $m_1$, $m_2$ be the roots of $a_0m^{2}+a_1m+a_2=0$.
>
> (i) If $m_1\neq m_2$ are real, the general solution is $y=c_1e^{m_1x}+c_2e^{m_2x}$.
>
> (ii) If $m_1=m_2=m$ is real, the general solution is $y=c_1e^{mx}+c_2xe^{mx}$.
>
> (iii) If $m_1=a+ib$ and $m_2=a-ib$ with $b\neq 0$, the general solution is $y=e^{ax}\left(c_1\cos bx+c_2\sin bx\right)$.

Each case is proved in Section 3. In every case the pair exhibited is a fundamental set, and the fact that no solution is lost follows from Theorem 2.2: a two-dimensional space cannot contain more than two independent members, so once two independent solutions are produced they span the whole space.

### 2.4 The Wronskian criterion

> **Theorem (Independence criterion).** Let $y_1$, $y_2$ be solutions of $y''+p(x)y'+q(x)y=0$ on an interval $I$ with $p$, $q$ continuous. Then $y_1$ and $y_2$ are linearly independent on $I$ if and only if $W(x)\neq 0$ for every $x$ in $I$.

Proof. If the pair is dependent then $y_2=ky_1$ for some constant $k$, and substitution into the determinant gives $W=y_1ky_1'-ky_1y_1'=0$ identically. Conversely, suppose $W(x_0)=0$ at some point $x_0$. Then the two vectors $\left(y_1(x_0),y_1'(x_0)\right)$ and $\left(y_2(x_0),y_2'(x_0)\right)$ are linearly dependent, so there are constants $c_1$, $c_2$ not both zero with $c_1y_1(x_0)+c_2y_2(x_0)=0$ and $c_1y_1'(x_0)+c_2y_2'(x_0)=0$. The combination $c_1y_1+c_2y_2$ is a solution with zero value and zero slope at $x_0$, so by uniqueness it is identically zero, and the pair is dependent. This completes the proof.

The two directions together show that for solutions of a linear equation the Wronskian cannot vanish at one point and be non-zero at another. It is either everywhere zero or everywhere non-zero.

### 2.5 Abel's identity

> **Lemma (Abel).** For solutions $y_1$, $y_2$ of $y''+p(x)y'+q(x)y=0$,
>
> $$
> W(x)=W(x_0)\exp\left(-\int_{x_0}^{x}p(t)\,dt\right) .
> $$

Proof. Differentiate the Wronskian and use the differential equation to replace each second derivative:

$$
W'=y_1y_2''-y_2y_1'' .
$$

Substituting $y_1''=-py_1'-qy_1$ and $y_2''=-py_2'-qy_2$ gives

$$
W'=y_1\left(-py_2'-qy_2\right)-y_2\left(-py_1'-qy_1\right)=-p\left(y_1y_2'-y_2y_1'\right)=-pW .
$$

The Wronskian therefore solves the first-order equation $W'=-pW$, whose solution is the stated exponential. This completes the proof.

For a constant-coefficient equation $p=-a_1/a_0$, so $W$ is a constant multiple of $e^{-px}=e^{a_1x/a_0}$, an exponential that never vanishes. This is an independent confirmation of the criterion in Theorem 2.4.

### 2.6 Reduction of order

> **Theorem (Reduction of order).** Let $y_1$ be a non-zero solution of $y''+py'+qy=0$ on $I$. Then a second, independent solution on $I$ is
>
> $$
> y_2=y_1\int\frac{\exp\left(-\int p\,dx\right)}{y_1^{2}}\,dx .
> $$

Proof. Seek $y=vy_1$ with $v$ to be found. Then

$$
y'=v'y_1+vy_1', \qquad y''=v''y_1+2v'y_1'+vy_1'' .
$$

Substituting and using $y_1''+py_1'+qy_1=0$ leaves

$$
v''y_1+2v'y_1'+pv'y_1=0 ,
$$

that is

$$
v''+\left(\frac{2y_1'}{y_1}+p\right)v'=0 .
$$

Put $u=v'$, so that $u'+\left(\frac{2y_1'}{y_1}+p\right)u=0$, which is separable. Its solution is

$$
u=\frac{\exp\left(-\int p\,dx\right)}{y_1^{2}} ,
$$

and integrating once gives the stated $y_2$. The two solutions are independent because $y_2/y_1=\int u\,dx$ is not constant whenever $u$ is not identically zero. This completes the proof.

The formula is the general engine behind the repeated-root case: feeding $y_1=e^{mx}$ with $p=-2m$ makes the integrand equal to one, and the integral becomes $x$.

### 2.7 The theorem for higher order

> **Theorem (Higher order).** Let $a_0y^{(n)}+a_1y^{(n-1)}+\cdots+a_ny=0$ with constant real coefficients and $a_0\neq 0$, and let the characteristic polynomial factor as a product of real linear factors $\left(m-m_i\right)^{k_i}$ and irreducible real quadratics $\left(m^{2}+bm+c\right)^{k_j}$.
>
> Each real root $m$ of multiplicity $k$ contributes the functions $e^{mx}$, $xe^{mx}$, …, $x^{k-1}e^{mx}$.
>
> Each conjugate pair $a\pm ib$ of multiplicity $k$ contributes $e^{ax}\cos bx$, $xe^{ax}\cos bx$, …, $x^{k-1}e^{ax}\cos bx$ together with the same list with $\sin bx$ in place of $\cos bx$.
>
> The functions so collected number $n$, are independent, and span the solution space.

The theorem is the natural extension of Theorem 2.3, and its proof is the same reduction of order applied once per repeated factor. Its practical use is that the total number of functions written down must equal the order, which gives an immediate check on any answer to a higher-order question.

### 2.8 Existence and uniqueness for initial value problems

> **Theorem (Unique solution).** If $p$, $q$ are continuous on an interval $I$ containing $x_0$, the problem $y''+py'+qy=0$, $y(x_0)=A$, $y'(x_0)=B$ has exactly one solution on $I$.

In the constant-coefficient case the coefficients are continuous everywhere, so the solution exists and is unique on the whole real line. The theorem is what licenses the phrase "the general solution": every solution is obtained from it by one choice of constants, and no solution is missed.

> **Theorem (Structure of the non-homogeneous solution set).** If $y_p$ is any solution of $L[y]=F$, then every solution of $L[y]=F$ has the form $y=y_p+y_h$ where $L[y_h]=0$.

Proof. Let $y$ be any solution of $L[y]=F$ and set $y_h=y-y_p$. By linearity, $L[y_h]=L[y]-L[y_p]=F-F=0$. This completes the proof.

The structure theorem is why the homogeneous problem is solved first and separately, and why the two-constant answer obtained here remains the foundation of every non-homogeneous question.

## 3. Formal Proofs, Derivations, and Methods

### 3.1 Derivation of the characteristic equation from the trial solution

Consider

$$
a_0\frac{d^{2}y}{dx^{2}}+a_1\frac{dy}{dx}+a_2y=0
$$

with $a_0\neq 0$. The derivatives of an exponential are constant multiples of the same exponential, so it is natural to ask whether a solution of that form exists. Put

$$
y=e^{mx}
$$

with $m$ a number still to be determined. Then

$$
\frac{dy}{dx}=me^{mx}, \qquad \frac{d^{2}y}{dx^{2}}=m^{2}e^{mx} .
$$

Substituting all three expressions gives

$$
a_0m^{2}e^{mx}+a_1me^{mx}+a_2e^{mx}=0 ,
$$

and factoring out the never-vanishing exponential gives

$$
\left(a_0m^{2}+a_1m+a_2\right)e^{mx}=0 .
$$

Since $e^{mx}\neq 0$ for every real $x$ and every $m$, this holds if and only if

$$
a_0m^{2}+a_1m+a_2=0 .
$$

The trial therefore succeeds precisely for the roots of the characteristic equation, and for no other values of $m$. Since a real quadratic has at least one root only when its discriminant is non-negative, the trial in this exact form produces nothing in the complex case; Section 3.4 repairs that.

Note that the derivation also shows why the method is unavailable for variable coefficients. If $a_0$ depended on $x$, the common factor would be $e^{mx}\left(a_0(x)m^{2}+a_1(x)m+a_2(x)\right)$, which cannot vanish identically for a fixed $m$ unless the coefficients conspire, and in general they do not.

### 3.2 Case one: real distinct roots, with the independence proof

Let the characteristic roots be real with $m_1\neq m_2$. By Section 3.1, $y_1=e^{m_1x}$ and $y_2=e^{m_2x}$ are solutions, and by superposition every combination is a solution. It remains to prove independence, that is, to show $W\neq 0$.

Compute

$$
W=e^{m_1x}\cdot m_2e^{m_2x}-e^{m_2x}\cdot m_1e^{m_1x}=\left(m_2-m_1\right)e^{(m_1+m_2)x} .
$$

Because $m_1\neq m_2$, the factor $m_2-m_1$ is non-zero, and the exponential is never zero, so $W\neq 0$ on the whole real line. By Theorem 2.4 the pair is independent, and by Theorem 2.2 it is a fundamental set, so the general solution is

$$
y=c_1e^{m_1x}+c_2e^{m_2x} .
$$

Two consistency checks follow from the coefficients. Writing the characteristic equation as $m^{2}+\frac{a_1}{a_0}m+\frac{a_2}{a_0}=0$ shows that $m_1+m_2=-\frac{a_1}{a_0}$ and $m_1m_2=\frac{a_2}{a_0}$. Both identities follow directly from the factorisation $a_0\left(m-m_1\right)\left(m-m_2\right)=a_0m^{2}-a_0\left(m_1+m_2\right)m+a_0m_1m_2$, and both are useful as arithmetic checks.

### 3.3 Case two: real repeated root, derived by reduction of order

Let the characteristic root be $m$, repeated, so that

$$
a_0m^{2}+a_1m+a_2=0 \qquad \text{and} \qquad 2a_0m+a_1=0 .
$$

The second identity holds because a repeated root is also a root of the derivative of the characteristic polynomial.

The known solution is $y_1=e^{mx}$. Write $y=ve^{mx}$ and compute

$$
\frac{dy}{dx}=e^{mx}\left(v'+mv\right),
$$

$$
\frac{d^{2}y}{dx^{2}}=e^{mx}\left(v''+2mv'+m^{2}v\right) .
$$

Substituting into the differential equation and factoring out $e^{mx}$ gives

$$
a_0\left(v''+2mv'+m^{2}v\right)+a_1\left(v'+mv\right)+a_2v .
$$

Collecting terms in $v$, in $v'$ and in $v''$ separately,

$$
a_0v''+\left(2a_0m+a_1\right)v'+v\left(a_0m^{2}+a_1m+a_2\right)=0 .
$$

The coefficient of $v$ is the characteristic equation, which is zero; the coefficient of $v'$ is zero because the root is repeated. What survives is

$$
a_0v''=0 ,
$$

and since $a_0\neq 0$ this means $v''=0$. Two integrations give

$$
v=c_2x+c_1 ,
$$

so

$$
y=\left(c_1+c_2x\right)e^{mx}=c_1e^{mx}+c_2xe^{mx} .
$$

The device $y=xe^{mx}$ is therefore not a guess imposed from outside; it is exactly what the substitution $y=ve^{mx}$ produces once the repeated-root identities are used.

It remains to prove independence. Compute

$$
W=e^{mx}\left(e^{mx}+mxe^{mx}\right)-xe^{mx}\cdot me^{mx}=e^{2mx} ,
$$

since the two terms containing $x$ cancel. The Wronskian is never zero, so the pair is fundamental and the general solution is complete.

The same result follows from the reduction-of-order formula of Theorem 2.6. Here $p=\frac{a_1}{a_0}=-2m$, so

$$
\exp\left(-\int p\,dx\right)=e^{2mx}, \qquad \frac{e^{2mx}}{y_1^{2}}=\frac{e^{2mx}}{e^{2mx}}=1 ,
$$

and the integral of one is $x$, giving $y_2=xe^{mx}$ directly.

### 3.4 Case three: conjugate complex roots

Let the roots be $a+ib$ and $a-ib$ with $b\neq 0$. Formally the two exponentials

$$
e^{(a+ib)x}=e^{ax}e^{ibx}, \qquad e^{(a-ib)x}=e^{ax}e^{-ibx}
$$

are solutions, and they are independent because their ratio is $e^{2ibx}$, which is not constant. Their combination is

$$
y=e^{ax}\left(c_1e^{ibx}+c_2e^{-ibx}\right) .
$$

Using Euler's formulas

$$
e^{ibx}=\cos bx+i\sin bx, \qquad e^{-ibx}=\cos bx-i\sin bx ,
$$

the bracket becomes

$$
\left(c_1+c_2\right)\cos bx+i\left(c_1-c_2\right)\sin bx .
$$

Setting $A=c_1+c_2$ and $B=i\left(c_1-c_2\right)$ produces

$$
y=e^{ax}\left(A\cos bx+B\sin bx\right) ,
$$

and since the map from $\left(c_1,c_2\right)$ to $\left(A,B\right)$ is invertible over the complex numbers, no solution is lost by this renaming.

The real form can also be verified without complex numbers. Differentiate $y_1=e^{ax}\cos bx$ twice:

$$
y_1'=e^{ax}\left(a\cos bx-b\sin bx\right),
$$

$$
y_1''=e^{ax}\left(\left(a^{2}-b^{2}\right)\cos bx-2ab\sin bx\right) .
$$

Substituting into $y''+py'+qy=0$ and separating cosine and sine gives two identities,

$$
a^{2}-b^{2}+pa+q=0, \qquad -2ab-pb=0 ,
$$

which are, up to an overall sign, the real and imaginary parts of the characteristic equation evaluated at $a+ib$. Since $a\pm ib$ are roots, both hold, so $y_1$ is a solution; the same computation with $\sin bx$ gives the same two identities with the roles of cosine and sine exchanged.

Finally, independence. Compute

$$
W=e^{2ax}\left[\cos bx\left(a\sin bx+b\cos bx\right)-\sin bx\left(a\cos bx-b\sin bx\right)\right]=be^{2ax} ,
$$

because the terms containing $a$ cancel and $\cos^{2}bx+\sin^{2}bx=1$. Since $b\neq 0$ the Wronskian never vanishes, so the pair is fundamental.

### 3.5 Higher order: the root-multiplicity rules

For order $n$ the characteristic polynomial has degree $n$, and by the fundamental theorem of algebra it factors over the complex numbers into $n$ linear factors. Real coefficients force the non-real factors to occur in conjugate pairs. Three rules then assemble the solution.

A real root $m$ of multiplicity $k$ contributes the $k$ functions $e^{mx}$, $xe^{mx}$, …, $x^{k-1}e^{mx}$. The justification is the repeated application of reduction of order: each repetition produces one further factor of $x$.

A conjugate pair $a\pm ib$ of multiplicity $k$ contributes the $2k$ functions $x^{j}e^{ax}\cos bx$ and $x^{j}e^{ax}\sin bx$ for $j=0,1,\dots,k-1$.

The total count is the sum of the multiplicities, which is $n$. Independence of the full collection follows from the Wronskian being non-zero, which in turn follows from the distinctness of the exponential rates and the triangular structure of the collection ordered by growth.

A worked instance shows the rules acting together. For

$$
\frac{d^{4}y}{dx^{4}}-2\frac{d^{3}y}{dx^{3}}+2\frac{d^{2}y}{dx^{2}}-2\frac{dy}{dx}+y=0
$$

the characteristic polynomial is $m^{4}-2m^{3}+2m^{2}-2m+1$, which factors as

$$
\left(m-1\right)^{2}\left(m^{2}+1\right) .
$$

The double root at one contributes $e^{x}$ and $xe^{x}$; the pair $\pm i$ contributes $\cos x$ and $\sin x$. Four functions for an equation of order four, so

$$
y=\left(c_1+c_2x\right)e^{x}+c_3\cos x+c_4\sin x .
$$

Checking the double-root terms: $y=e^{x}$ gives $1-2+2-2+1=0$, and $y=xe^{x}$ may be confirmed by substitution, which is the content of the multiplicity rule.

### 3.6 The method as a procedure

1. Write the equation in the standard form with zero on the right, and record $a_0$, $a_1$, $a_2$ with their signs.
2. Form the characteristic equation $a_0m^{2}+a_1m+a_2=0$.
3. Solve it exactly: factorise if the roots are rational, otherwise use the quadratic formula and keep surds.
4. Classify the roots using the sign of $\Delta=a_1^{2}-4a_0a_2$.
5. Write the general solution from the appropriate case of Theorem 2.3.
6. If initial values are given, differentiate the general solution and solve the resulting two-by-two linear system for the constants.
7. Verify by substitution, and verify the count of constants against the order.

Step 7 is not optional. Substitution catches sign errors in the characteristic equation, arithmetic errors in the roots, and algebraic errors in the constants, which together account for almost every lost mark.

### 3.7 Solving for the constants

For $y=c_1y_1+c_2y_2$ with conditions $y(x_0)=A$ and $y'(x_0)=B$, the system of Section 1.9 has determinant $W(x_0)$, which is non-zero for any fundamental set. Cramer's rule therefore gives

$$
c_1=\frac{Ay_2'(x_0)-By_2(x_0)}{W(x_0)}, \qquad c_2=\frac{By_1(x_0)-Ay_1'(x_0)}{W(x_0)} .
$$

In practice the system is small enough to solve by elimination, and the formulas are quoted only to justify uniqueness. What matters procedurally is that the two equations must involve both constants; applying both conditions to the same expression, such as using $y(x_0)=A$ twice, determines nothing.

## 4. Representative Worked Examples and Solutions

### 4.1 Problem: two distinct real roots

Solve $y''+3y'-10y=0$ and verify the answer.

### 4.2 Solution: factorise, classify, assemble, check

Step 1. Write the characteristic equation, transferring the signs exactly as they appear.

$$
m^{2}+3m-10=0
$$

Step 2. Factorise by seeking two numbers with product $-10$ and sum $3$.

$$
\left(m+5\right)\left(m-2\right)=0
$$

Step 3. Record the roots, which are real and distinct.

$$
m_1=-5, \qquad m_2=2
$$

Step 4. Write the general solution for the distinct-real case.

$$
y=c_1e^{-5x}+c_2e^{2x}
$$

Step 5. Verify with the coefficient identities: the sum of the roots is $-3$, matching $-\frac{a_1}{a_0}=-3$, and the product is $-10$, matching $\frac{a_2}{a_0}=-10$.

Step 6. Verify by substitution for the second exponential, whose derivatives are $2e^{2x}$ and $4e^{2x}$.

$$
4e^{2x}+3\left(2e^{2x}\right)-10e^{2x}=\left(4+6-10\right)e^{2x}=0
$$

Step 7. Verify for the first exponential, whose derivatives are $-5e^{-5x}$ and $25e^{-5x}$.

$$
25e^{-5x}+3\left(-5e^{-5x}\right)-10e^{-5x}=\left(25-15-10\right)e^{-5x}=0
$$

Both basic solutions satisfy the equation, so by superposition the general solution does.

### 4.3 Problem: irrational real roots

Solve $y''-4y'+2y=0$.

### 4.4 Solution: quadratic formula with exact surds

Step 1. Write the characteristic equation.

$$
m^{2}-4m+2=0
$$

Step 2. Apply the quadratic formula with $a=1$, $b=-4$, $c=2$.

$$
m=\frac{4\pm\sqrt{16-8}}{2}=\frac{4\pm\sqrt{8}}{2}
$$

Step 3. Simplify the surd, writing $\sqrt{8}=2\sqrt{2}$.

$$
m=\frac{4\pm 2\sqrt{2}}{2}=2\pm\sqrt{2}
$$

Step 4. Record both roots as exact irrational numbers.

$$
m_1=2+\sqrt{2}, \qquad m_2=2-\sqrt{2}
$$

Step 5. Check the coefficient identities: the sum is $4$, matching $-\frac{a_1}{a_0}=4$, and the product is $4-2=2$, matching $\frac{a_2}{a_0}=2$.

Step 6. Write the general solution.

$$
y=c_1e^{\left(2+\sqrt{2}\right)x}+c_2e^{\left(2-\sqrt{2}\right)x}
$$

Step 7. Verify structurally: each exponent is a root of $m^{2}-4m+2=0$, so substituting $e^{mx}$ produces $\left(m^{2}-4m+2\right)e^{mx}=0$ for each term, and superposition gives the result.

### 4.5 Problem: a repeated root with fractional value

Solve $9y''+12y'+4y=0$.

### 4.6 Solution: recognise a perfect square and use the $x$ device

Step 1. Write the characteristic equation.

$$
9m^{2}+12m+4=0
$$

Step 2. Check the discriminant.

$$
\Delta=144-4\cdot 9\cdot 4=144-144=0
$$

Step 3. A zero discriminant means a repeated root; factorise as a perfect square.

$$
\left(3m+2\right)^{2}=0
$$

Step 4. Record the root and its multiplicity.

$$
m=-\frac{2}{3} \quad \text{(twice)}
$$

Step 5. Write the general solution in the repeated-root form.

$$
y=\left(c_1+c_2x\right)e^{-2x/3}
$$

Step 6. Verify the second basic solution $y=xe^{-2x/3}$. Its first derivative is

$$
y'=e^{-2x/3}-\frac{2}{3}xe^{-2x/3} ,
$$

and its second derivative is

$$
y''=-\frac{2}{3}e^{-2x/3}-\frac{2}{3}e^{-2x/3}+\frac{4}{9}xe^{-2x/3}=-\frac{4}{3}e^{-2x/3}+\frac{4}{9}xe^{-2x/3} .
$$

Step 7. Substitute into the equation and collect the constant and the $x$-dependent parts separately.

$$
9\left(-\frac{4}{3}\right)+12\left(1\right)+4\left(0\right)=-12+12=0 ,
$$

$$
9\left(\frac{4}{9}\right)+12\left(-\frac{2}{3}\right)+4\left(1\right)=4-8+4=0 .
$$

Both parts vanish, so $xe^{-2x/3}$ is a solution and the general solution is correct.

### 4.7 Problem: conjugate complex roots

Solve $y''+4y'+29y=0$ and state the Wronskian of the fundamental set.

### 4.8 Solution: complete the square and read off the real and imaginary parts

Step 1. Write the characteristic equation.

$$
m^{2}+4m+29=0
$$

Step 2. Compute the discriminant.

$$
\Delta=16-116=-100
$$

Step 3. Apply the quadratic formula, writing $\sqrt{-100}=10i$.

$$
m=\frac{-4\pm 10i}{2}=-2\pm 5i
$$

Step 4. Identify the real part and the imaginary part; the real part is $-2$ and the imaginary part is $5$.

Step 5. Write the general solution.

$$
y=e^{-2x}\left(c_1\cos 5x+c_2\sin 5x\right)
$$

Step 6. Compute the Wronskian of the pair to confirm independence.

$$
W=\left(e^{-2x}\cos 5x\right)\left(e^{-2x}\left(-2\sin 5x+5\cos 5x\right)\right)-\left(e^{-2x}\sin 5x\right)\left(e^{-2x}\left(-2\cos 5x-5\sin 5x\right)\right)
$$

Step 7. Expand and cancel the terms containing the real part, leaving the identity $b e^{2ax}$.

$$
W=5e^{-4x}\left(\cos^{2}5x+\sin^{2}5x\right)=5e^{-4x}
$$

Step 8. Interpret. The Wronskian is never zero, so the pair is fundamental; the factor $5$ is the imaginary part, and the exponential decay reflects the negative real part. The solution therefore describes a decaying oscillation.

### 4.9 Problem: third order with one real and one complex pair

Solve $y'''-3y''+4y'-2y=0$.

### 4.10 Solution: find a root by inspection, then divide out

Step 1. Write the characteristic equation.

$$
m^{3}-3m^{2}+4m-2=0
$$

Step 2. Test $m=1$.

$$
1-3+4-2=0
$$

Step 3. Divide out the factor $m-1$ to obtain a quadratic.

$$
m^{3}-3m^{2}+4m-2=\left(m-1\right)\left(m^{2}-2m+2\right)
$$

Step 4. Solve the quadratic with the quadratic formula.

$$
m=\frac{2\pm\sqrt{4-8}}{2}=1\pm i
$$

Step 5. Record all three roots.

$$
m=1, \qquad m=1+i, \qquad m=1-i
$$

Step 6. Assemble the solution, using $e^{x}$ for the single root and an exponential factor $e^{x}$ with a cosine and a sine for the pair.

$$
y=c_1e^{x}+e^{x}\left(c_2\cos x+c_3\sin x\right)=e^{x}\left(c_1+c_2\cos x+c_3\sin x\right)
$$

Step 7. Check the count: three constants for an equation of order three.

Step 8. Verify the sine term. For $y=e^{x}\sin x$,

$$
y'=e^{x}\left(\sin x+\cos x\right), \qquad y''=2e^{x}\cos x, \qquad y'''=2e^{x}\left(\cos x-\sin x\right) .
$$

Step 9. Substitute and collect sine and cosine coefficients.

$$
2e^{x}\left(\cos x-\sin x\right)-6e^{x}\cos x+4e^{x}\left(\sin x+\cos x\right)-2e^{x}\sin x
$$

$$
=e^{x}\cos x\left(2-6+4\right)+e^{x}\sin x\left(-2+4-2\right)=0
$$

The check succeeds, so the general solution stands.

### 4.11 Problem: fourth order with a repeated complex pair

Solve $y^{(4)}+8y''+16y=0$.

### 4.12 Solution: treat the characteristic equation as a quadratic in $m^{2}$

Step 1. Write the characteristic equation.

$$
m^{4}+8m^{2}+16=0
$$

Step 2. Recognise a perfect square in $m^{2}$.

$$
\left(m^{2}+4\right)^{2}=0
$$

Step 3. Solve $m^{2}=-4$, obtaining the pair $\pm 2i$, each of multiplicity two.

Step 4. Apply the multiplicity rule for a conjugate pair, adding factors of $x$.

$$
y=\left(c_1+c_2x\right)\cos 2x+\left(c_3+c_4x\right)\sin 2x
$$

Step 5. Check the count: four constants for an equation of order four.

Step 6. Verify the awkward member $y=x\cos 2x$. Its first derivative is

$$
y'=\cos 2x-2x\sin 2x ,
$$

and its second derivative is

$$
y''=-2\sin 2x-2\sin 2x-4x\cos 2x=-4\sin 2x-4x\cos 2x .
$$

Step 7. Apply the operator $D^{2}+4$ once.

$$
y''+4y=-4\sin 2x-4x\cos 2x+4x\cos 2x=-4\sin 2x
$$

Step 8. Apply $D^{2}+4$ a second time to that result.

$$
\frac{d^{2}}{dx^{2}}\left(-4\sin 2x\right)+4\left(-4\sin 2x\right)=16\sin 2x-16\sin 2x=0
$$

The check succeeds, which confirms that the extra factor of $x$ is required and correct.

### 4.13 Problem: an initial value problem with complex roots

Solve $y''+6y'+13y=0$ subject to $y(0)=3$ and $y'(0)=-1$.

### 4.14 Solution: solve, impose both conditions, verify

Step 1. Write the characteristic equation and its roots.

$$
m^{2}+6m+13=0, \qquad m=\frac{-6\pm\sqrt{36-52}}{2}=-3\pm 2i
$$

Step 2. Write the general solution.

$$
y=e^{-3x}\left(c_1\cos 2x+c_2\sin 2x\right)
$$

Step 3. Impose $y(0)=3$. At $x=0$ the exponential and the cosine equal one and the sine equals zero.

$$
3=c_1
$$

Step 4. Differentiate the general solution.

$$
y'=e^{-3x}\left[-3\left(c_1\cos 2x+c_2\sin 2x\right)-2c_1\sin 2x+2c_2\cos 2x\right]
$$

Step 5. Impose $y'(0)=-1$.

$$
-1=-3c_1+2c_2
$$

Step 6. Substitute $c_1=3$ and solve for the second constant.

$$
-1=-9+2c_2 \qquad \text{so} \qquad c_2=4
$$

Step 7. State the particular solution.

$$
y=e^{-3x}\left(3\cos 2x+4\sin 2x\right)
$$

Step 8. Verify both conditions. At $x=0$ the value is $3$ and the derivative is $-9+8=-1$, as required.

Step 9. Verify the amplitude interpretation. Writing $3\cos 2x+4\sin 2x=5\sin\left(2x+\phi\right)$ shows the motion is an oscillation of amplitude five about zero, damped by the factor $e^{-3x}$.

### 4.15 Problem: fifth order with repeated roots at two values

Solve $y^{(5)}-2y^{(4)}+y'''=0$.

### 4.16 Solution: factor out the common power of $m$

Step 1. Write the characteristic equation.

$$
m^{5}-2m^{4}+m^{3}=0
$$

Step 2. Factor out $m^{3}$.

$$
m^{3}\left(m^{2}-2m+1\right)=0
$$

Step 3. Factorise the quadratic as a perfect square.

$$
m^{3}\left(m-1\right)^{2}=0
$$

Step 4. Record the roots with multiplicities: zero three times, one twice.

Step 5. Convert each multiplicity into the right number of functions. The root zero gives $e^{0x}=1$, then $x$, then $x^{2}$; the root one gives $e^{x}$ and $xe^{x}$.

$$
y=c_1+c_2x+c_3x^{2}+c_4e^{x}+c_5xe^{x}
$$

Step 6. Check the count: five constants for an equation of order five.

Step 7. Verify the polynomial part $y=x^{2}$. Its third derivative onwards vanish, so $y^{(5)}-2y^{(4)}+y'''=0-0+0=0$.

Step 8. Verify the repeated-root part $y=xe^{x}$. Its derivatives up to the fifth are

$$
y'=e^{x}\left(x+1\right), \quad y''=e^{x}\left(x+2\right), \quad y'''=e^{x}\left(x+3\right), \quad y^{(4)}=e^{x}\left(x+4\right), \quad y^{(5)}=e^{x}\left(x+5\right) .
$$

Step 9. Substitute.

$$
e^{x}\left(x+5\right)-2e^{x}\left(x+4\right)+e^{x}\left(x+3\right)=e^{x}\left(x+5-2x-8+x+3\right)=0
$$

The check succeeds, so the general solution is correct.

### 4.17 Problem: recover the differential equation from its general solution

Show that $y=e^{2x}\left(A\cos 3x+B\sin 3x\right)$ is the general solution of a second-order homogeneous linear equation with constant coefficients, and find that equation.

### 4.18 Solution: read the roots, then rebuild the polynomial

Step 1. Read the real and imaginary parts from the given solution: the exponential factor has rate $2$, and the trigonometric factors have frequency $3$.

Step 2. Deduce the characteristic roots.

$$
m=2\pm 3i
$$

Step 3. Rebuild the characteristic polynomial from its roots, using the sum and the product.

$$
\left(m-2-3i\right)\left(m-2+3i\right)=\left(m-2\right)^{2}+9=m^{2}-4m+13
$$

Step 4. Write the differential equation with the same coefficients.

$$
y''-4y'+13y=0
$$

Step 5. Verify by substituting $y=e^{2x}\cos 3x$, whose second derivative was computed in Section 3.4 with $a=2$ and $b=3$.

$$
y''=e^{2x}\left(\left(4-9\right)\cos 3x-12\sin 3x\right)=e^{2x}\left(-5\cos 3x-12\sin 3x\right)
$$

Step 6. Assemble the left-hand side and collect cosine and sine terms.

$$
-5-4\cdot 2+13=0, \qquad -12-4\cdot\left(-3\right)+0=0
$$

Both coefficients vanish, so the equation is correct, and the same computation with the sine term confirms the second member of the fundamental set.

## 5. Mathematical Extensions, Limits, and Common Errors

### 5.1 Where the homogeneous solution is used next

The homogeneous solution is not an end in itself. For a non-homogeneous equation the answer is the homogeneous solution plus one particular solution, so every non-homogeneous question in the course begins with the work of this note. The candidate method for the particular solution is coefficient matching: for a right-hand side built from exponentials, polynomials, sines and cosines, a trial of the same shape is substituted and its coefficients are matched.

A subtlety arises when the trial duplicates a homogeneous solution. For $y''-5y'+6y=e^{2x}$ the natural trial $ke^{2x}$ fails, because the left-hand side annihilates it. The repair is to multiply the trial by $x$, giving $kxe^{2x}$, and the reason is exactly the reduction-of-order argument of Section 3.3: a repeated root forces one extra factor of $x$.

### 5.2 The interpretation of the three cases

The three cases are not merely algebraic categories; they describe three qualitatively different behaviours, and that reading is often worth marks.

Two distinct real roots of the same sign describe a process that settles or grows without oscillating, with the slower exponential dominating eventually. Distinct real roots of opposite signs describe an unstable process, since one mode grows and the other decays.

A repeated root describes the borderline case in which the two modes have merged; the factor of $x$ shows that the borderline behaviour involves linear growth in time as well as exponential growth or decay.

A conjugate pair with a non-zero real part describes an oscillation whose amplitude changes exponentially. The imaginary part is the angular frequency and the real part is the growth or decay rate. A purely imaginary pair, where the real part is zero, describes oscillation of constant amplitude, which is the simple harmonic motion of $y''+\omega^{2}y=0$.

### 5.3 What the method cannot do

The method depends on the coefficients being constants. With even one variable coefficient the trial $y=e^{mx}$ produces a factor depending on $x$ that cannot vanish identically, and the reduction to a polynomial equation collapses.

The method produces solutions of the homogeneous equation only. It gives no particular solution for a forcing term, and the general non-homogeneous answer requires a second technique.

The method gives real solutions from complex roots by a conversion that assumes real coefficients. For an equation with complex coefficients the conjugate symmetry is lost, and the conversion into a real cosine and sine is no longer available.

Finally, the method assumes the equation is already linear. For a non-linear equation the characteristic equation has no meaning, because the substitution $y=e^{mx}$ does not produce a common factor.

### 5.4 Common errors and their diagnosis

| Error | What it looks like | Correct treatment |
| --- | --- | --- |
| Sign transfer | $m^{2}+5m+6=0$ from $y''-5y'+6y=0$ | Copy signs directly: $m^{2}-5m+6=0$ |
| Missing factor of $x$ | $y=c_1e^{mx}+c_2e^{mx}$ for a repeated root | Write $y=\left(c_1+c_2x\right)e^{mx}$ |
| Frequency confusion | $\cos 2x$ for roots $2\pm 3i$ | The frequency is the imaginary part: $\cos 3x$ |
| Lost imaginary part | $\cos 3x$ for roots $\pm 3i$ written as $e^{3x}\cos 3x$ | A zero real part gives no exponential factor |
| One constant | $y=c_1e^{2x}+e^{3x}$ | Two arbitrary constants are always required |
| Constant inside the exponential | Writing $e^{mx+C}$ as a solution | Constants multiply the basic solutions, not their exponents |
| Wrong order count | Three constants for a second-order equation | Check the count against the order |
| No verification | Final answer stated without substitution | Substitute the awkward basic solution back |

Two of these deserve expansion. The frequency confusion is the single most common arithmetic error in the complex case, and it is caught instantly by substituting the proposed answer back: the frequency of the surviving trigonometric terms must match the imaginary part of the roots. The missing factor of $x$ is caught by counting independent solutions: two equal exponentials are one function, not two, so the answer would carry one constant and be visibly incomplete.

### 5.5 Checks that catch nearly everything

The sum and product identities for the characteristic roots catch most errors in the roots themselves. For $a_0m^{2}+a_1m+a_2=0$ the roots satisfy $m_1+m_2=-\frac{a_1}{a_0}$ and $m_1m_2=\frac{a_2}{a_0}$, and both are read directly from the coefficients.

Substitution catches errors in the assembled solution. Substituting each basic solution separately is quicker than substituting the general solution and is just as conclusive, because superposition guarantees the rest.

Counting catches errors of structure. The number of arbitrary constants must equal the order; the number of independent basic solutions must equal the order; and in the complex case the frequency must equal the imaginary part.

Checking the initial conditions catches errors in the constants. Substitute the point $x_0$ into the particular solution and into its derivative and compare with the given values; the two comparisons are independent, so a single slip shows up in one of them.

### 5.6 Consolidated summary

A second-order homogeneous linear equation with constant coefficients, written in operator form as $f(D)y=0$, has a solution space of dimension two. The trial $y=e^{mx}$ converts the differential equation into the algebraic equation $f(m)=0$, whose two roots decide everything.

When the roots are real and distinct the two fundamental solutions are the two exponentials, and the Wronskian $(m_2-m_1)e^{(m_1+m_2)x}$ is never zero. When the root is repeated the second solution is obtained by reduction of order and equals $xe^{mx}$, with Wronskian $e^{2mx}$. When the roots are a conjugate pair $a\pm ib$ the fundamental solutions are $e^{ax}\cos bx$ and $e^{ax}\sin bx$, with Wronskian $be^{2ax}$.

For higher order the same three rules apply with multiplicity: a repeated root adds successive powers of $x$, and a repeated conjugate pair adds the same powers inside the trigonometric pair. The number of constants always equals the order, and two initial conditions at a single point always determine the two constants uniquely.
