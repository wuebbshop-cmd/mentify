## 1. Foundational Concepts, Definitions, and Axioms

### 1.1 The object of study

A second-order linear differential equation with constant coefficients is an equation in which an unknown function and its first two derivatives appear linearly, each multiplied by a fixed number, and whose right-hand side is a prescribed function of the independent variable. The homogeneous case, in which that right-hand side is zero, was solved completely in the preceding work: the auxiliary equation supplies two roots, and the roots supply two independent solutions. The present topic adds the forcing term and answers the obvious question, namely what the addition does to the solution set.

> **Definition (standard form).** Let $a_{0}$, $a_{1}$, $a_{2}$ be real constants with $a_{0}\ne 0$, and let $Q$ be a real-valued function defined on an interval $I$. The equation
>
> $$
> a_{0}\frac{d^{2}y}{dx^{2}}+a_{1}\frac{dy}{dx}+a_{2}y=Q(x)
> $$
>
> is called a second-order nonhomogeneous linear equation with constant coefficients. When $Q$ is identically zero the equation is called homogeneous.

The condition $a_{0}\ne 0$ is what makes the equation second order: it guarantees that the second derivative is genuinely present and can be solved for. Throughout, the coefficients are constants and $Q$ is continuous on $I$, so every initial value problem posed on $I$ has a unique solution there.

It is convenient to name the left-hand side once and for all. Two notations are in use and both are needed.

> **Definition (the operators $L$ and $F(D)$).** For a twice differentiable function $y$,
>
> $$
> L[y]=a_{0}y''+a_{1}y'+a_{2}y ,
> $$
>
> and, writing $D$ for the operation of differentiating with respect to $x$,
>
> $$
> F(D)=a_{0}D^{2}+a_{1}D+a_{2}, \qquad F(D)y=a_{0}y''+a_{1}y'+a_{2}y .
> $$

The symbol $D$ is an operator, not a number: it acts on whatever stands to its right. Powers of $D$ mean repeated differentiation, so $D^{2}y=y''$. Because $D$ is linear and because the coefficients are constants, the operator $F(D)$ may be manipulated exactly as if it were a quadratic polynomial, except that its powers act on functions rather than multiplying numbers. In particular $F(D)$ factors, and the factors commute.

The polynomial obtained by replacing $D$ by an ordinary variable $m$ carries the information about the unforced equation.

> **Definition (auxiliary equation).** The quadratic equation
>
> $$
> a_{0}m^{2}+a_{1}m+a_{2}=0
> $$
>
> is called the auxiliary equation, or characteristic equation, of the operator $F(D)$. Its roots are called the characteristic roots.

### 1.2 The unforced equation and its three cases

The homogeneous equation $L[y]=0$ is solved by exponentials. Substituting $y=e^{mx}$ gives

$$
a_{0}m^{2}e^{mx}+a_{1}me^{mx}+a_{2}e^{mx}=e^{mx}\left(a_{0}m^{2}+a_{1}m+a_{2}\right),
$$

and since $e^{mx}$ never vanishes, the substitution is a solution precisely when $m$ satisfies the auxiliary equation. The discriminant $\Delta=a_{1}^{2}-4a_{0}a_{2}$ decides the nature of the roots, and the nature of the roots decides the shape of the solution.

**Case 1, distinct real roots.** If $\Delta>0$ the roots $m_{1}$ and $m_{2}$ are real and different, and

$$
y_{c}=c_{1}e^{m_{1}x}+c_{2}e^{m_{2}x}.
$$

**Case 2, a repeated real root.** If $\Delta=0$ there is a single root $m=-\frac{a_{1}}{2a_{0}}$, and the second independent solution is $xe^{mx}$, so

$$
y_{c}=\left(c_{1}+c_{2}x\right)e^{mx}.
$$

**Case 3, complex conjugate roots.** If $\Delta<0$ the roots are $\alpha\pm i\beta$ with $\alpha=-\frac{a_{1}}{2a_{0}}$ and $\beta=\frac{\sqrt{-\Delta}}{2a_{0}}$, and Euler's formula turns the complex exponentials into a real pair, giving

$$
y_{c}=e^{\alpha x}\left(c_{1}\cos\beta x+c_{2}\sin\beta x\right).
$$

These three formulas are the complete answer for the unforced equation, and no other shape can occur.

### 1.3 The complementary function

> **Definition (complementary function).** The complementary function, written $y_{c}$, is the general solution of the homogeneous equation $L[y]=0$ on $I$. It is a two-parameter family, one of the three shapes listed in Section 1.2, and its two parameters are arbitrary real constants.

The word complementary refers to its role: it completes the forced solution, in a sense made precise in Section 2.3.

Independence of the two solutions is what makes the two constants genuine. A pair $y_{1},y_{2}$ of solutions of a second-order linear homogeneous equation is independent exactly when neither is a constant multiple of the other, and this is detected by a determinant.

> **Definition (Wronskian).** The Wronskian of two differentiable functions $y_{1}$ and $y_{2}$ is
>
> $$
> W(x)=y_{1}(x)y_{2}'(x)-y_{1}'(x)y_{2}(x).
> $$

For the three cases of Section 1.2 the Wronskians are nonzero on the whole interval. For distinct exponents,

$$
W\left(e^{m_{1}x},e^{m_{2}x}\right)=\left(m_{2}-m_{1}\right)e^{(m_{1}+m_{2})x},
$$

which never vanishes because $m_{1}\ne m_{2}$. For the repeated case,

$$
W\left(e^{mx},xe^{mx}\right)=e^{2mx},
$$

again nonzero. For the trigonometric pair,

$$
W\left(e^{\alpha x}\cos\beta x,e^{\alpha x}\sin\beta x\right)=\beta e^{2\alpha x},
$$

and $\beta\ne 0$ in the complex case. So the two solutions are independent in every case, and the complementary function really does carry two essential constants.

### 1.4 The particular integral

> **Definition (particular integral).** A particular integral, written $y_{p}$, is any single function that satisfies $L[y]=Q$ on $I$. It contains no arbitrary constants.

The article a in that definition is deliberate. Particular integrals are never unique, because adding a solution of the homogeneous equation to one particular integral produces another. What is unique, given a forcing function of the catalogue considered here, is the particular integral of the prescribed trial shape; that is the content of Section 2.7.

A particular integral is verified by substitution and by nothing else. No appeal to a method, to a formula, or to an authority can replace the check, because the definition is a statement about the result of substituting.

### 1.5 The shape of the solution set

The solution set of the nonhomogeneous equation is not a vector space, because the sum of two solutions is not a solution. It is instead a translate of the two-dimensional solution space of the homogeneous equation, an affine plane inside the infinite-dimensional space of twice differentiable functions. This is the geometric content of the structure theorem proved in Section 3.2, and it explains several otherwise puzzling facts.

The first is that the general solution carries exactly two constants, neither more nor fewer. The translate of a two-dimensional space is a two-dimensional affine space, and a two-dimensional affine space is parametrised by two parameters.

The second is that the difference of any two solutions of the nonhomogeneous equation solves the homogeneous equation. The affine structure records exactly this.

The third is that a particular integral may be chosen in infinitely many ways, all of them equally valid, and the choice affects only which representative of the affine plane is written down first. The final general solution is the same family whichever representative is chosen.

### 1.6 The catalogue of forcing terms

The method of undetermined coefficients applies to forcing functions that are built from three elementary shapes, namely polynomials, exponentials, and the trigonometric pair, combined by addition and by multiplication. The most compact description uses a single formula.

> **Definition (forcing of exponential-polynomial type).** A forcing function $Q$ is of exponential-polynomial type when
>
> $$
> Q(x)=e^{\alpha x}\left(P(x)\cos\beta x+R(x)\sin\beta x\right)
> $$
>
> for some real numbers $\alpha$ and $\beta$ and some real polynomials $P$ and $R$.

Every case in this course is an instance. A constant $6$ is the case $\alpha=0$, $\beta=0$, $P=6$, $R=0$. A quadratic $3x^{2}-x$ is the case $\alpha=0$, $\beta=0$ with $P$ of degree two. An exponential $e^{2x}$ is $\alpha=2$, $\beta=0$, $P=1$. A cosine $\cos 3x$ is $\alpha=0$, $\beta=3$, $P=1$, $R=0$. A product such as $xe^{x}\sin 2x$ is $\alpha=1$, $\beta=2$ with $P=0$ and $R=x$. A sum is handled by splitting the sum and adding the resulting particular integrals.

The trial shape is read from $Q$ and from the characteristic roots together. Write $\mu=\alpha+i\beta$ and let $s$ be the number of times $\mu$ occurs among the characteristic roots; since the auxiliary equation is quadratic, $s$ is $0$, $1$ or $2$.

> **Definition (the index of duplication).** The integer $s$, the multiplicity of $\mu=\alpha+i\beta$ as a root of the auxiliary equation, is called the index of duplication for the forcing term $Q$.

With these two pieces of data the trial is fixed.

| Forcing $Q(x)$ | Multiplicity $s$ of $\mu$ | Trial for $y_{p}$ | Unknown numbers |
| --- | --- | --- | --- |
| $P_{m}(x)$ | $s=0$ | $A_{m}x^{m}+\cdots+A_{1}x+A_{0}$ | $m+1$ |
| $P_{m}(x)$ | $s=1$ | $x\left(A_{m}x^{m}+\cdots+A_{0}\right)$ | $m+1$ |
| $P_{m}(x)$ | $s=2$ | $x^{2}\left(A_{m}x^{m}+\cdots+A_{0}\right)$ | $m+1$ |
| $e^{ax}$ | $s=0$ | $Ae^{ax}$ | $1$ |
| $e^{ax}$ | $s=1$ | $Axe^{ax}$ | $1$ |
| $e^{ax}$ | $s=2$ | $Ax^{2}e^{ax}$ | $1$ |
| $\cos\beta x$ or $\sin\beta x$ | $s=0$ | $A\cos\beta x+B\sin\beta x$ | $2$ |
| $\cos\beta x$ or $\sin\beta x$ | $s=1$ | $x\left(A\cos\beta x+B\sin\beta x\right)$ | $2$ |
| $e^{\alpha x}P_{m}(x)\cos\beta x$ | $s=0$ | $e^{\alpha x}\left(A_{m}x^{m}+\cdots+A_{0}\right)\cos\beta x+e^{\alpha x}\left(B_{m}x^{m}+\cdots+B_{0}\right)\sin\beta x$ | $2m+2$ |

Two entries deserve comment because they are the ones students most often get wrong.

The trigonometric rows show that a forcing term containing a cosine alone still requires both a cosine and a sine in the trial. The reason is structural: the operator $F(D)$ maps the two-dimensional space spanned by $\cos\beta x$ and $\sin\beta x$ into itself, and its matrix in that basis is generally not diagonal, so a purely cosine forcing produces a sine component in the image. Supplying both basis functions is what allows the matching to succeed.

The rows for $\alpha\ne 0$ with $\beta=0$ show the doubling rule in its plainest form. A forcing term $e^{ax}$ with $a$ equal to a simple characteristic root needs a factor $x$; with $a$ equal to a double root it needs $x^{2}$. The multiplicity, not the mere presence of the exponential, controls the count.

### 1.7 Initial conditions and the initial value problem

> **Definition (initial value problem).** The initial value problem for the equation $L[y]=Q$ consists of the equation together with the two conditions
>
> $$
> y(x_{0})=y_{0}, \qquad y'(x_{0})=v_{0},
> $$
>
> where $x_{0}\in I$ and $y_{0}$, $v_{0}$ are prescribed real numbers.

Two conditions are prescribed because the general solution carries two parameters, and the conditions are imposed on the general solution, never on the particular integral alone. Section 3.9 shows that the resulting linear system always has a unique solution, the determinant being the Wronskian at $x_{0}$, which Section 1.3 proved nonzero.

## 2. Theorems, Lemmas, and Analytical Properties

### 2.1 Linearity of the operator

> **Lemma (linearity).** For constants $\lambda$ and $\mu$ and twice differentiable functions $y_{1}$ and $y_{2}$,
>
> $$
> L\left[\lambda y_{1}+\mu y_{2}\right]=\lambda L[y_{1}]+\mu L[y_{2}] .
> $$

The lemma follows from the linearity of differentiation, since each derivative of a linear combination is the corresponding linear combination of derivatives, together with the fact that the coefficients are constants and may be taken outside. It is the only structural property of the equation used in this topic, and every result below is a consequence of it.

Nonlinear equations fail the lemma, and their behaviour is correspondingly irregular. For the equation $y''+y^{2}=0$, the function $y_{1}=\sin x$ is not a solution, but a more instructive illustration is that doubling a solution is not a solution: if $y$ solves $y''+y^{2}=0$ then $2y$ satisfies $2y''+4y^{2}$, which is not zero. Superposition is not a general truth about differential equations; it is a consequence of linearity.

### 2.2 Superposition of a forced and an unforced solution

> **Theorem (superposition with forcing).** If $L[y_{p}]=Q$ and $L[y_{h}]=0$ on $I$, then $L[y_{p}+y_{h}]=Q$ on $I$.

The proof is one application of Section 2.1,

$$
L\left[y_{p}+y_{h}\right]=L[y_{p}]+L[y_{h}]=Q+0=Q,
$$

and it is written out in Section 3.1. The theorem says that the unforced solutions act as directions in which any particular integral may be moved without disturbing the match with $Q$. Those directions are exactly the two-dimensional space described in Section 1.5.

### 2.3 The structure theorem

> **Theorem (general solution of the nonhomogeneous equation).** Let $y_{p}$ be any particular integral of $L[y]=Q$ on the interval $I$. Then the general solution of $L[y]=Q$ on $I$ is
>
> $$
> y=y_{c}+y_{p},
> $$
>
> where $y_{c}$ is the general solution of the homogeneous equation $L[y]=0$ on $I$. Equivalently, every solution of the nonhomogeneous equation can be written in that form, and every function of that form is a solution.

The two halves of the statement correspond to the two inclusions proved in Section 3.2. The forward inclusion, that every function of the form $y_{c}+y_{p}$ is a solution, is Section 2.2. The reverse inclusion, that every solution is of that form, is the substantive half, and it is where the hypothesis that $y_{p}$ is a particular integral is used: the difference of two particular integrals is annihilated by $L$, hence lies in the homogeneous solution space.

> **Corollary (count of constants).** The general solution of a second-order nonhomogeneous linear equation contains exactly two arbitrary constants, and they occur only in the complementary function.

The corollary gives the cheapest available audit of a finished answer. If a proposed general solution of a second-order nonhomogeneous equation carries one constant, or three, or has a constant multiplying the particular integral, it is wrong regardless of any other merit.

### 2.4 The homogeneous solution space

> **Theorem (dimension two).** Let $a_{0}$, $a_{1}$, $a_{2}$ be constants with $a_{0}\ne 0$. The set of solutions of $L[y]=0$ on an interval $I$ is a two-dimensional real vector space, and any two solutions with nonzero Wronskian form a basis.

The dimension statement is the abstract form of the counting rule, and it is what makes the corollary above exact rather than approximate. Two independent solutions exist by Section 1.2, where they are exhibited explicitly in each of the three cases, and no third independent solution can exist because the equation determines $y''$ once $y$ and $y'$ are known.

> **Theorem (Abel's identity).** For two solutions $y_{1}$ and $y_{2}$ of $L[y]=0$,
>
> $$
> W(x)=W(x_{0})\exp\left(-\frac{a_{1}}{a_{0}}\left(x-x_{0}\right)\right).
> $$

Abel's identity shows that the Wronskian either vanishes everywhere or nowhere, so independence is a global property rather than a pointwise accident. Since the Wronskians computed in Section 1.3 never vanish, the bases exhibited there are genuine bases.

### 2.5 Existence and uniqueness

> **Theorem (existence and uniqueness for the initial value problem).** Suppose $a_{0}$, $a_{1}$, $a_{2}$ and $Q$ are continuous on an interval $I$ and $a_{0}\ne 0$ there. Then for every $x_{0}\in I$ and every pair of real numbers $y_{0}$, $v_{0}$ the initial value problem
>
> $$
> a_{0}y''+a_{1}y'+a_{2}y=Q(x), \qquad y(x_{0})=y_{0}, \qquad y'(x_{0})=v_{0}
> $$
>
> has exactly one solution on $I$.

With constant coefficients the hypotheses hold on every interval, so every initial value problem in this topic is uniquely solvable on the whole real line. The theorem is not proved here, but two consequences of it are used repeatedly. The first is that the two constants can always be determined, so no initial value problem in this topic is inconsistent. The second is that a solution found by any method whatever is the solution, so a verified guess needs no further justification.

### 2.6 The exponential shift

> **Lemma (exponential shift).** For any polynomial $F$ with constant coefficients and any real constant $a$,
>
> $$
> F(D)\left[e^{ax}w(x)\right]=e^{ax}F(D+a)\left[w(x)\right].
> $$

Here $F(D+a)$ means the polynomial $F$ evaluated at the operator $D+a$. The lemma is the main computational tool behind the theory of undetermined coefficients, and it is proved in Section 3.5. Its content is that multiplying a function by an exponential shifts the operator by the same constant, which converts a problem with a general exponential forcing term into a problem with a polynomial forcing term.

### 2.7 The theorem of undetermined coefficients

> **Theorem (existence and uniqueness of the trial).** Let $Q(x)=e^{\alpha x}\left(P(x)\cos\beta x+R(x)\sin\beta x\right)$ with $P$ and $R$ real polynomials of degree at most $m$, let $\mu=\alpha+i\beta$, and let $s\in\{0,1,2\}$ be the multiplicity of $\mu$ as a root of the auxiliary equation. Then there exist unique real polynomials $A$ and $B$ of degree at most $m$ such that
>
> $$
> y_{p}=x^{s}e^{\alpha x}\left(A(x)\cos\beta x+B(x)\sin\beta x\right)
> $$
>
> satisfies $L[y_{p}]=Q$.

The theorem does three things at once. It asserts that a trial of the tabulated shape always succeeds, so no other shape need be considered. It asserts that the trial needs exactly the number of unknown coefficients displayed, so the resulting linear system is square. And it asserts uniqueness, so the coefficients are determined by the equation and not by any choice of the solver. The proof occupies Section 3.6, and the algebraic core of it is isolated in Section 2.9.

Two corollaries are used constantly in practice.

> **Corollary (cover-up rule for a non-resonant exponential).** If $Q(x)=Ce^{ax}$ and $F(a)\ne 0$, then
>
> $$
> y_{p}=\frac{Ce^{ax}}{F(a)} .
> $$

> **Corollary (polynomial forcing when zero is a root).** If $Q$ is a polynomial of degree $m$ and $a_{2}=0$, then the auxiliary equation has the root $0$, with multiplicity one when $a_{1}\ne 0$ and multiplicity two when $a_{1}=0$. The trial must therefore be multiplied by $x$, or by $x^{2}$ in the exceptional case, even though no exponential appears in the forcing term.

The second corollary is the trap that catches most candidates in examinations, because the forcing term is a plain polynomial and the multiplying factor of $x$ seems to come from nowhere. It comes from the constant term of the operator: when $a_{2}=0$ the operator annihilates constants, so a polynomial trial of the naive shape lies partly in the kernel.

### 2.8 Resonance and the growth of the response

> **Corollary (secular growth).** If $\mu=\alpha+i\beta$ is a characteristic root and the forcing term contains $e^{\alpha x}\cos\beta x$ or $e^{\alpha x}\sin\beta x$ with a nonzero coefficient, then the particular integral contains a factor $x$, so its amplitude grows without bound as $x$ increases.

The factor $x$ is the algebraic signature of resonance. Physically it records that the forcing is applied in step with a motion the system already performs of its own accord, so each push adds energy to a motion that is already present rather than to a motion that the system would damp away. Mathematically it is forced by the impossibility of matching the forcing with any function in the homogeneous solution space: the only remaining direction is the one generated by $x$ times a natural solution, and it is precisely the direction in which the operator has a repeated root.

### 2.9 The algebraic lemma behind the trial

> **Lemma (invertibility on polynomials).** Let $G$ be a polynomial with $G(\mu)\ne 0$ and let $s$ be a non-negative integer. Define
>
> $$
> T(v)=e^{-\mu x}F(D)\left[x^{s}e^{\mu x}v(x)\right]
> $$
>
> where $F(D)=(D-\mu)^{s}G(D)$. Then $T$ maps the space of polynomials of degree at most $m$ into itself, and in the basis $1,x,\dots,x^{m}$ its matrix is upper triangular, the entry in position $j$ of the diagonal being $G(\mu)(s+j)!/j!$, which is never zero. In particular $T$ is invertible on that space.

This lemma is the engine of the whole method. It converts the analytic question, whether a trial of a given shape can match a given forcing term, into a question of linear algebra over polynomials, where the answer is decided by a single nonzero number. The proof is in Section 3.6, and the computation of the diagonal entry is the only delicate step.

### 2.10 Results at a glance

| Result | Statement in one line | Role |
| --- | --- | --- |
| Linearity | $L$ distributes over linear combinations | Foundation of everything |
| Superposition | $L[y_{p}]+L[y_{h}]=Q$ when $L[y_{h}]=0$ | Shows $y_{c}+y_{p}$ always works |
| Structure theorem | General solution is $y_{c}+y_{p}$ | Identifies the complete answer |
| Dimension two | Homogeneous solution space has dimension two | Justifies exactly two constants |
| Existence and uniqueness | Two conditions determine one solution | Justifies solving for $c_{1},c_{2}$ |
| Exponential shift | $F(D)e^{ax}w=e^{ax}F(D+a)w$ | Converts exponential problems to polynomial ones |
| Undetermined coefficients | Trial shape exists and is unique | Justifies the table |
| Cover-up rule | $y_{p}=Ce^{ax}/F(a)$ when $F(a)\ne 0$ | Fast route for simple cases |
| Secular growth | Resonant forcing produces a factor $x$ | Explains unbounded responses |

## 3. Formal Proofs, Derivations, and Methods

### 3.1 Proof of linearity and of superposition

Let $y_{1}$ and $y_{2}$ be twice differentiable on $I$ and let $\lambda$, $\mu$ be constants. Since differentiation is linear,

$$
\left(\lambda y_{1}+\mu y_{2}\right)''=\lambda y_{1}''+\mu y_{2}'', \qquad \left(\lambda y_{1}+\mu y_{2}\right)'=\lambda y_{1}'+\mu y_{2}' .
$$

Multiplying the first identity by $a_{0}$, the second by $a_{1}$, and adding $a_{2}\left(\lambda y_{1}+\mu y_{2}\right)$ gives

$$
L\left[\lambda y_{1}+\mu y_{2}\right]=\lambda\left(a_{0}y_{1}''+a_{1}y_{1}'+a_{2}y_{1}\right)+\mu\left(a_{0}y_{2}''+a_{1}y_{2}'+a_{2}y_{2}\right),
$$

that is $L\left[\lambda y_{1}+\mu y_{2}\right]=\lambda L[y_{1}]+\mu L[y_{2}]$, which is the lemma. Setting $\lambda=\mu=1$, and using $L[y_{h}]=0$ together with $L[y_{p}]=Q$, gives

$$
L\left[y_{p}+y_{h}\right]=L[y_{p}]+L[y_{h}]=Q+0=Q,
$$

which is the superposition theorem. Taking in addition $\lambda=-1$ and $\mu=1$ gives $L[y_{h}-y_{p}]=-Q$, a relation worth remembering: linear combinations of solutions solve equations whose right-hand sides combine in the same way.

### 3.2 Proof of the structure theorem

Let $y_{p}$ be a particular integral of $L[y]=Q$ and let $Y$ be any solution of the same equation on $I$. Define

$$
z(x)=Y(x)-y_{p}(x).
$$

By linearity,

$$
L[z]=L[Y]-L[y_{p}]=Q-Q=0 .
$$

So $z$ is a solution of the homogeneous equation on $I$, and by the dimension theorem of Section 2.4 it has the form $z=c_{1}y_{1}+c_{2}y_{2}$ for suitable constants. Therefore

$$
Y=y_{p}+c_{1}y_{1}+c_{2}y_{2}=y_{p}+y_{c},
$$

which proves that every solution has the required form. The converse is superposition, established in Section 3.1. Since $y_{c}$ ranges over the whole homogeneous solution space as the constants vary, the family written down is exactly the solution set, and the proof is complete.

Two remarks on the proof. First, it uses only linearity; the fact that the coefficients are constant enters not here but in the explicit form of $y_{1}$ and $y_{2}$. Second, the argument shows that the choice of $y_{p}$ is immaterial: if $y_{p}$ is replaced by $y_{p}+y_{h}$, the extra term is absorbed into $y_{c}$, and the family described is unchanged.

### 3.3 Proof of Abel's identity

Differentiate the Wronskian,

$$
W'=y_{1}y_{2}''-y_{1}''y_{2},
$$

and replace each second derivative using the equation, written as $y''=-\frac{a_{1}}{a_{0}}y'-\frac{a_{2}}{a_{0}}y$. Then

$$
W'=y_{1}\left(-\frac{a_{1}}{a_{0}}y_{2}'-\frac{a_{2}}{a_{0}}y_{2}\right)-\left(-\frac{a_{1}}{a_{0}}y_{1}'-\frac{a_{2}}{a_{0}}y_{1}\right)y_{2}.
$$

The terms containing $a_{2}$ cancel in pairs, and the remaining terms are proportional to the Wronskian itself,

$$
W'=-\frac{a_{1}}{a_{0}}\left(y_{1}y_{2}'-y_{1}'y_{2}\right)=-\frac{a_{1}}{a_{0}}W .
$$

This is a separable first-order equation for $W$, whose solution is

$$
W(x)=W\left(x_{0}\right)\exp\left(-\frac{a_{1}}{a_{0}}\left(x-x_{0}\right)\right).
$$

The exponential factor is never zero, so $W$ vanishes at one point of $I$ if and only if it vanishes at every point of $I$. Independence is therefore decided once and for all, and the Wronskians computed in Section 1.3 settle the matter in each of the three cases.

### 3.4 Derivation of the inverse operator for a single factor

The computational route to a particular integral begins from the simplest operator, a single factor $D-a$. The equation

$$
(D-a)u=Q
$$

is the first-order linear equation $u'-au=Q$. Multiplying by the integrating factor $e^{-ax}$ turns the left-hand side into an exact derivative,

$$
u'e^{-ax}-aue^{-ax}=Qe^{-ax}, \qquad \frac{d}{dx}\left(ue^{-ax}\right)=Qe^{-ax},
$$

and one integration gives the solution

$$
u=e^{ax}\int e^{-ax}Q(x)\,dx .
$$

Any antiderivative may be used, because a constant added to the integral produces a multiple of $e^{ax}$, which lies in the kernel of $D-a$ and is therefore irrelevant to the particular integral. In operator notation this reads

$$
\frac{1}{D-a}Q=e^{ax}\int e^{-ax}Q(x)\,dx .
$$

For a product of two distinct factors the particular integral is obtained by applying the two inverse factors in succession. Since operators with constant coefficients commute, the order of application does not matter, and one may write

$$
\frac{1}{(D-a)(D-b)}Q=\frac{1}{D-a}\left(\frac{1}{D-b}Q\right).
$$

Each stage is a first-order problem, so the second-order problem is reduced to two integrations. This is the operator route used in the lectures, and it agrees with the method of undetermined coefficients wherever both apply.

As a check, take the operator $(D-1)(D-2)$ and the forcing term $e^{5x}$. Since $5$ is not a characteristic root, the cover-up rule predicts $y_{p}=e^{5x}/F(5)$ with $F(5)=(5-1)(5-2)=12$. The two-stage computation reproduces this. First,

$$
u=e^{2x}\int e^{-2x}e^{5x}\,dx=e^{2x}\cdot\frac{e^{3x}}{3}=\frac{e^{5x}}{3},
$$

and then

$$
y=e^{x}\int e^{-x}\cdot\frac{e^{5x}}{3}\,dx=e^{x}\cdot\frac{e^{4x}}{12}=\frac{e^{5x}}{12}.
$$

The agreement is not an accident: the two routes are two ways of computing the same inverse operator.

### 3.5 Proof of the exponential shift

The identity is proved by induction on the power of $D$. For one derivative, the product rule gives

$$
D\left[e^{ax}w\right]=e^{ax}w'+ae^{ax}w=e^{ax}\left(D+a\right)w .
$$

Suppose the identity holds for the power $n$. Then

$$
D^{n+1}\left[e^{ax}w\right]=D\left[e^{ax}\left(D+a\right)^{n}w\right]=e^{ax}\left(D+a\right)\left(D+a\right)^{n}w=e^{ax}\left(D+a\right)^{n+1}w,
$$

where the second equality applies the one-derivative case to the function $\left(D+a\right)^{n}w$. The induction is complete for powers. For a polynomial $F(D)=\sum_{k}c_{k}D^{k}$,

$$
F(D)\left[e^{ax}w\right]=\sum_{k}c_{k}e^{ax}\left(D+a\right)^{k}w=e^{ax}\sum_{k}c_{k}\left(D+a\right)^{k}w=e^{ax}F(D+a)w,
$$

which is the lemma. The shift moves a factor of $e^{ax}$ outside the operator at the price of replacing $D$ by $D+a$ inside it.

### 3.6 Proof of the theorem of undetermined coefficients

The proof has three stages: complexification, reduction to a polynomial problem, and inversion.

**Stage 1, complexification.** Write $\mu=\alpha+i\beta$ and $S=P-iR$. By Euler's formula,

$$
e^{\mu x}S(x)=e^{\alpha x}\left(\cos\beta x+i\sin\beta x\right)\left(P(x)-iR(x)\right),
$$

whose real part is $e^{\alpha x}\left(P\cos\beta x+R\sin\beta x\right)=Q(x)$. Because the coefficients of $F$ are real, the operator commutes with taking real parts, so a solution $z$ of the complex equation $F(D)z=e^{\mu x}S$ produces the real solution $y_{p}=\text{Re}z$ of $F(D)y=Q$. It therefore suffices to solve the complex problem.

**Stage 2, reduction to a polynomial problem.** Factor the operator as

$$
F(D)=(D-\mu)^{s}G(D),
$$

where $s$ is the multiplicity of $\mu$ and $G(\mu)\ne 0$. Put $z=x^{s}e^{\mu x}v(x)$. Two applications of the exponential shift give

$$
F(D)z=e^{\mu x}F(D+\mu)\left[x^{s}v\right]=e^{\mu x}D^{s}G(D+\mu)\left[x^{s}v\right],
$$

the last step because $F(D+\mu)=D^{s}G(D+\mu)$, the variable $D+\mu$ having been shifted to $D$. Hence the complex equation is equivalent to

$$
D^{s}G(D+\mu)\left[x^{s}v\right]=S .
$$

**Stage 3, inversion on polynomials.** Write $G(D+\mu)=g_{0}+g_{1}D+g_{2}D^{2}$, with $g_{0}=G(\mu)\ne 0$. For a monomial $x^{j}$ with $0\le j\le m$,

$$
D^{s}\left[x^{s+j}\right]=\frac{(s+j)!}{j!}x^{j},
$$

and each further derivative lowers the exponent, so

$$
T\left(x^{j}\right)=g_{0}\frac{(s+j)!}{j!}x^{j}+g_{1}\frac{(s+j)!}{(j-1)!}x^{j-1}+g_{2}\frac{(s+j)!}{(j-2)!}x^{j-2},
$$

with the convention that terms of negative exponent are absent. In the basis $1,x,\dots,x^{m}$ the operator $T$ is therefore upper triangular, and every diagonal entry $g_{0}(s+j)!/j!$ is nonzero. So $T$ is invertible, and for the given polynomial $S$ there is exactly one polynomial $v$ of degree at most $m$ with $T(v)=S$.

**Conclusion.** The function $z=x^{s}e^{\mu x}v$ solves the complex equation, and

$$
y_{p}=\text{Re}z=x^{s}e^{\alpha x}\left(A(x)\cos\beta x+B(x)\sin\beta x\right),
$$

where $A=\text{Re}v$ and $B=\text{Im}v$ are real polynomials of degree at most $m$. Uniqueness follows because the difference of two admissible trials would produce a polynomial in the kernel of the invertible operator $T$, hence the zero polynomial. The theorem is proved.

The proof also explains the tabulated coefficient count. The space of polynomials of degree at most $m$ has dimension $m+1$, and two such polynomials $A$ and $B$ are required, so the trial carries $2m+2$ unknown numbers in the trigonometric case and $m+1$ in the purely exponential or polynomial cases.

### 3.7 The duplication analysis

The proof above shows exactly where the factor $x^{s}$ comes from, and it also shows why a smaller power fails. Suppose a trial of the form $x^{s-1}e^{\mu x}v$ is attempted, with $s\ge 1$. The same computation gives

$$
F(D)\left[x^{s-1}e^{\mu x}v\right]=e^{\mu x}D^{s}G(D+\mu)\left[x^{s-1}v\right].
$$

The polynomial $x^{s-1}v$ has degree at most $m+s-1$, so after $s$ differentiations the result has degree at most $m-1$. The image therefore lies in the proper subspace of polynomials of degree at most $m-1$, and a forcing polynomial of exact degree $m$ cannot be represented. In the important special case $m=0$, meaning a pure exponential or a pure sine or cosine, the polynomial $x^{s-1}v$ has degree at most $s-1$ and is annihilated outright, so the left-hand side is identically zero and the equation reduces to $0=Q$, which is impossible.

There are therefore two distinct symptoms of an insufficient power of $x$, and both are diagnostic.

The first symptom is total collapse: substituting the trial gives zero, and the equation reads $0=Q$. This happens for a pure exponential, a pure sine, or a pure cosine that duplicates a natural solution, and it demands one more factor of $x$.

The second symptom is a singular system: the trial produces a result of too low a degree, so one of the coefficient equations is inconsistent or the equations are dependent. This happens when the forcing term is a polynomial or a polynomial times a natural exponential, and it demands one more factor of $x$ as well.

A trial with too many factors of $x$ fails differently: the left-hand side then produces shapes, such as $x^{3}e^{\mu x}$, that the forcing term does not contain, and matching those shapes forces a coefficient to be zero, which contradicts the remaining equations. The correct power is exactly the multiplicity, neither more nor less.

### 3.8 The complete algorithm

The theory reduces the solution of every problem in this topic to a fixed sequence.

1. Write the equation in standard form and read off $a_{0}$, $a_{1}$, $a_{2}$ and $Q$.
2. Solve the auxiliary equation $a_{0}m^{2}+a_{1}m+a_{2}=0$ and record the roots with their multiplicities.
3. Write the complementary function in the appropriate one of the three forms.
4. Identify $\alpha$ and $\beta$ in the forcing term, form $\mu=\alpha+i\beta$, and compute the index of duplication $s$.
5. Write the trial with $m+1$ or $2m+2$ unknown coefficients, multiplied by $x^{s}$.
6. Differentiate the trial twice, substitute, and collect like terms.
7. Equate coefficients of the independent shapes and solve the resulting linear system.
8. Record $y=y_{c}+y_{p}$.
9. If conditions are given, impose them on the complete solution and solve for the two constants.
10. Verify the particular integral by substitution and the constants by the conditions.

Steps 2 and 4 cannot be interchanged, because the index of duplication is read from the roots. Step 10 is not optional, and it costs less than a minute.

### 3.9 Applying initial conditions

Write the complete solution as $y=c_{1}y_{1}+c_{2}y_{2}+y_{p}$, where $y_{1}$ and $y_{2}$ are the two basis solutions of the homogeneous equation. Differentiating,

$$
y'=c_{1}y_{1}'+c_{2}y_{2}'+y_{p}' .
$$

Imposing the two conditions at $x_{0}$ gives the linear system

$$
c_{1}y_{1}\left(x_{0}\right)+c_{2}y_{2}\left(x_{0}\right)=y_{0}-y_{p}\left(x_{0}\right),
$$

$$
c_{1}y_{1}'\left(x_{0}\right)+c_{2}y_{2}'\left(x_{0}\right)=v_{0}-y_{p}'\left(x_{0}\right).
$$

The determinant of this system is

$$
y_{1}\left(x_{0}\right)y_{2}'\left(x_{0}\right)-y_{1}'\left(x_{0}\right)y_{2}\left(x_{0}\right)=W\left(x_{0}\right),
$$

which is nonzero by Section 1.3. Cramer's rule therefore gives a unique pair $c_{1}$, $c_{2}$, and the initial value problem has exactly one solution, in agreement with Section 2.5. Note that the right-hand sides involve $y_{p}$ and $y_{p}'$: the particular integral contributes to the conditions, and ignoring it is a standard error.

### 3.10 The verification protocol

Verification has two independent parts, and a complete answer satisfies both.

For the particular integral, substitute $y_{p}$ into the left-hand side and simplify. The result must equal $Q$ identically in $x$. A practical shortcut for a trial of the form $e^{\mu x}v$ is to divide the difference by $e^{\mu x}$ and check that the remaining expression vanishes as a polynomial.

For the constants, substitute $x=x_{0}$ into the finished solution and into its derivative, and compare with the two prescribed values. If two conditions were given and both hold, the constants are correct, because the system that produced them has a nonzero determinant.

## 4. Representative Worked Examples and Solutions

### 4.1 Problem: an exponential forcing term that is not resonant

Solve $y''+5y'+6y=e^{2x}$.

### 4.2 Solution: cover-up rule, then verification

Step 1. The auxiliary equation factorises, and the roots are both different from $2$.

$$
m^{2}+5m+6=(m+2)(m+3)=0, \qquad m=-2,\quad m=-3
$$

Step 2. The complementary function.

$$
y_{c}=c_{1}e^{-2x}+c_{2}e^{-3x}
$$

Step 3. Since $F(2)=4+10+6=20\ne 0$, the index of duplication is $s=0$ and the cover-up rule applies with $C=1$.

$$
y_{p}=\frac{e^{2x}}{F(2)}=\frac{e^{2x}}{20}
$$

Step 4. Verify independently by substitution: the derivatives are $2y_{p}$ and $4y_{p}$, so the left-hand side is $(4+10+6)y_{p}=20\cdot\frac{e^{2x}}{20}=e^{2x}$, which is the forcing term.

$$
y=c_{1}e^{-2x}+c_{2}e^{-3x}+\frac{1}{20}e^{2x}
$$

Step 5. Interpretation: the forcing grows while both natural modes decay, so for large $x$ the response is dominated by the forced term $\frac{1}{20}e^{2x}$ and the natural part is a transient.

### 4.3 Problem: an exponential forcing term that is resonant with a simple root

Solve $y''-5y'+6y=e^{2x}$.

### 4.4 Solution: multiply the trial by $x$ and match

Step 1. The roots are $2$ and $3$, so $2$ is a simple characteristic root and the index of duplication is $s=1$.

$$
m^{2}-5m+6=(m-2)(m-3)=0, \qquad m=2,\quad m=3
$$

Step 2. The complementary function already contains $e^{2x}$.

$$
y_{c}=c_{1}e^{2x}+c_{2}e^{3x}
$$

Step 3. The trial is therefore $Axe^{2x}$. Differentiate with the product rule, keeping the exponential factored out.

$$
y=Axe^{2x}, \qquad y'=A(1+2x)e^{2x}, \qquad y''=A(4+4x)e^{2x}
$$

Step 4. Substitute and collect the bracket, in which the terms in $x$ cancel.

$$
A e^{2x}\left[(4+4x)-5(1+2x)+6x\right]=A e^{2x}\left(-1\right)
$$

Step 5. Match with $e^{2x}$, which gives $A=-1$.

$$
y_{p}=-xe^{2x}
$$

Step 6. Verify directly in the original equation.

$$
\left(4+4x\right)\left(-e^{2x}\right)-5\left(-(1+2x)e^{2x}\right)+6\left(-xe^{2x}\right)=e^{2x}\left[-4-4x+5+10x-6x\right]=e^{2x}
$$

Step 7. The general solution, in which the forced term has the resonant factor $x$.

$$
y=c_{1}e^{2x}+c_{2}e^{3x}-xe^{2x}
$$

### 4.5 Problem: polynomial forcing

Solve $y''+y'-2y=4x^{2}$.

### 4.6 Solution: a full quadratic trial

Step 1. The roots are $1$ and $-2$, and $\mu=0$ is not a root, so $s=0$.

$$
m^{2}+m-2=(m-1)(m+2)=0, \qquad m=1,\quad m=-2
$$

Step 2. The complementary function.

$$
y_{c}=c_{1}e^{x}+c_{2}e^{-2x}
$$

Step 3. Because $s=0$, the trial is a full quadratic with three unknown coefficients, and the constant term cannot be omitted.

$$
y=ax^{2}+bx+c, \qquad y'=2ax+b, \qquad y''=2a
$$

Step 4. Substitute and collect powers of $x$.

$$
2a+\left(2ax+b\right)-2\left(ax^{2}+bx+c\right)=-2ax^{2}+\left(2a-2b\right)x+\left(2a+b-2c\right)
$$

Step 5. Match the three coefficients against $4x^{2}$, that is against $4x^{2}+0x+0$.

$$
-2a=4, \qquad 2a-2b=0, \qquad 2a+b-2c=0
$$

Step 6. Solve in order: $a=-2$, then $b=a=-2$, then $c=\frac{2a+b}{2}=-3$.

$$
y_{p}=-2x^{2}-2x-3
$$

Step 7. Verify by substitution: the second derivative is $-4$, the first is $-4x-2$, and the left-hand side becomes

$$
-4+\left(-4x-2\right)-2\left(-2x^{2}-2x-3\right)=-4-4x-2+4x^{2}+4x+6=4x^{2},
$$

which is the forcing term. The linear terms cancel identically, as they must when the quadratic coefficient has been matched correctly.

Step 8. The general solution.

$$
y=c_{1}e^{x}+c_{2}e^{-2x}-2x^{2}-2x-3
$$

Step 9. Interpretation: a polynomial forcing term produces a polynomial response of the same degree, because the operator $F(D)$ has a nonzero constant term $a_{2}=-2$, so it does not annihilate constants.

### 4.7 Problem: trigonometric forcing at a frequency that is not natural

Solve $y''+3y'+2y=\sin x$.

### 4.8 Solution: both a cosine and a sine in the trial

Step 1. The roots are $-1$ and $-2$, and $\mu=i$ is not a root, so $s=0$.

$$
m^{2}+3m+2=(m+1)(m+2)=0, \qquad m=-1,\quad m=-2
$$

Step 2. The complementary function.

$$
y_{c}=c_{1}e^{-x}+c_{2}e^{-2x}
$$

Step 3. The trial must contain a cosine and a sine even though the forcing term contains only a sine.

$$
y=A\cos x+B\sin x, \qquad y'=-A\sin x+B\cos x, \qquad y''=-A\cos x-B\sin x
$$

Step 4. Substitute and collect the cosine and sine coefficients separately.

$$
\cos x\left(-A+3B+2A\right)+\sin x\left(-B-3A+2B\right)=\cos x\left(A+3B\right)+\sin x\left(B-3A\right)
$$

Step 5. Match against $0\cdot\cos x+1\cdot\sin x$.

$$
A+3B=0, \qquad B-3A=1
$$

Step 6. Substituting $A=-3B$ into the second equation gives $B+9B=1$, hence $B=\frac{1}{10}$ and $A=-\frac{3}{10}$.

$$
y_{p}=\frac{\sin x-3\cos x}{10}
$$

Step 7. Verify: with $A=-\frac{3}{10}$ and $B=\frac{1}{10}$ the collected form above gives $\cos x\left(A+3B\right)+\sin x\left(B-3A\right)=0\cdot\cos x+1\cdot\sin x$, as required.

Step 8. The general solution.

$$
y=c_{1}e^{-x}+c_{2}e^{-2x}+\frac{1}{10}\sin x-\frac{3}{10}\cos x
$$

### 4.9 Problem: trigonometric forcing at exactly the natural frequency

Solve $y''+4y=\sin 2x$.

### 4.10 Solution: multiply the oscillatory trial by $x$

Step 1. The characteristic roots are $\pm 2i$, and the forcing frequency is $2$, so $\mu=2i$ is a simple root and $s=1$.

$$
m^{2}+4=0, \qquad m=\pm 2i
$$

Step 2. The complementary function.

$$
y_{c}=c_{1}\cos 2x+c_{2}\sin 2x
$$

Step 3. The trial is $x\left(A\cos 2x+B\sin 2x\right)$. Differentiate twice, gathering the terms with and without a factor $x$.

$$
y'=\left(A\cos 2x+B\sin 2x\right)+x\left(-2A\sin 2x+2B\cos 2x\right)
$$

$$
y''=\left(-4A\sin 2x+4B\cos 2x\right)+x\left(-4A\cos 2x-4B\sin 2x\right)
$$

Step 4. Adding $4y$ cancels every term containing $x$, because $x\left(A\cos 2x+B\sin 2x\right)$ is multiplied by $4$ and by $-4$.

$$
y''+4y=-4A\sin 2x+4B\cos 2x
$$

Step 5. Match with $\sin 2x$: the sine coefficient gives $-4A=1$ and the cosine coefficient gives $4B=0$.

$$
A=-\frac{1}{4}, \qquad B=0
$$

Step 6. The particular integral is $y_{p}=-\frac{x}{4}\cos 2x$, and the verification is the computation of Step 4 with these values, which returns $\sin 2x$.

$$
y=c_{1}\cos 2x+c_{2}\sin 2x-\frac{x}{4}\cos 2x
$$

Step 7. Interpretation: the amplitude of the forced oscillation grows in proportion to $x$. This is resonance, and it is the reason the factor $x$ cannot be avoided.

### 4.11 Problem: a product of a polynomial and an exponential

Solve $y''-3y'+2y=xe^{3x}$.

### 4.12 Solution: keep the whole product in the trial

Step 1. The roots are $1$ and $2$, so $\mu=3$ is not a root and $s=0$.

$$
m^{2}-3m+2=(m-1)(m-2)=0, \qquad m=1,\quad m=2
$$

Step 2. The trial is the whole product with a linear factor, not a bare multiple of $xe^{3x}$.

$$
y=\left(ax+b\right)e^{3x}, \qquad y'=\left(3ax+a+3b\right)e^{3x}, \qquad y''=\left(9ax+6a+9b\right)e^{3x}
$$

Step 3. Substitute and collect.

$$
e^{3x}\left[\left(9ax+6a+9b\right)-3\left(3ax+a+3b\right)+2\left(ax+b\right)\right]=e^{3x}\left(2ax+3a+2b\right)
$$

Step 4. Match with $xe^{3x}$.

$$
2a=1, \qquad 3a+2b=0
$$

Step 5. Solve: $a=\frac{1}{2}$ and $b=-\frac{3}{4}$.

$$
y_{p}=\left(\frac{x}{2}-\frac{3}{4}\right)e^{3x}
$$

Step 6. Verify by substituting the bracket obtained in Step 3: $2\cdot\frac{1}{2}x+3\cdot\frac{1}{2}+2\cdot\left(-\frac{3}{4}\right)=x$, as required.

Step 7. The general solution.

$$
y=c_{1}e^{x}+c_{2}e^{2x}+\left(\frac{x}{2}-\frac{3}{4}\right)e^{3x}
$$

### 4.13 Problem: a forcing term that is a sum

Solve $y''+y=x+e^{2x}$.

### 4.14 Solution: split the sum and add the pieces

Step 1. The characteristic roots are $\pm i$, so the forcing term $e^{2x}$ is not resonant while the polynomial part has $\mu=0$, also not a root.

$$
m^{2}+1=0, \qquad m=\pm i
$$

Step 2. The complementary function.

$$
y_{c}=c_{1}\cos x+c_{2}\sin x
$$

Step 3. For the polynomial part, try $y=ax+b$ and substitute.

$$
0+ax+b=x
$$

Step 4. Matching gives $a=1$ and $b=0$, so the polynomial contribution is $y_{p1}=x$.

Step 5. For the exponential part, try $y=Ce^{2x}$ and substitute.

$$
4Ce^{2x}+Ce^{2x}=5Ce^{2x}=e^{2x}, \qquad C=\frac{1}{5}
$$

Step 6. Superposition adds the two contributions, and the sum is verified because each piece was verified separately.

$$
y=c_{1}\cos x+c_{2}\sin x+x+\frac{1}{5}e^{2x}
$$

### 4.15 Problem: a resonant exponential with a double root

Solve $y''-2y'+y=e^{x}$.

### 4.16 Solution: multiply by $x$ twice

Step 1. The auxiliary equation is a perfect square, so the root $1$ has multiplicity two and $s=2$.

$$
m^{2}-2m+1=(m-1)^{2}=0, \qquad m=1
$$

Step 2. The complementary function already contains both $e^{x}$ and $xe^{x}$.

$$
y_{c}=\left(c_{1}+c_{2}x\right)e^{x}
$$

Step 3. The trial must therefore carry $x^{2}$, and the correct trial is $Ax^{2}e^{x}$.

$$
y=Ax^{2}e^{x}, \qquad y'=A\left(2x+x^{2}\right)e^{x}, \qquad y''=A\left(2+4x+x^{2}\right)e^{x}
$$

Step 4. Substitute and collect.

$$
Ae^{x}\left[\left(2+4x+x^{2}\right)-2\left(2x+x^{2}\right)+x^{2}\right]=2Ae^{x}
$$

Step 5. Match with $e^{x}$, giving $A=\frac{1}{2}$, and verify by substitution, which returns $e^{x}$.

$$
y=\left(c_{1}+c_{2}x\right)e^{x}+\frac{1}{2}x^{2}e^{x}
$$

### 4.17 Problem: a product whose exponential duplicates a simple root

Solve $y''-4y=xe^{2x}$.

### 4.18 Solution: a resonant product needs the full shifted polynomial

Step 1. The roots are $\pm 2$, so $\mu=2$ is a simple root and $s=1$.

$$
m^{2}-4=0, \qquad m=2,\quad m=-2
$$

Step 2. Since $s=1$ and the forcing polynomial has degree one, the trial is $x\left(ax+b\right)e^{2x}$, that is a quadratic factor multiplying the exponential. A trial $a x^{2}e^{2x}$ alone would leave a residual multiple of $e^{2x}$.

$$
y=\left(ax^{2}+bx\right)e^{2x}, \qquad y'=\left(2ax^{2}+\left(2a+2b\right)x+b\right)e^{2x}
$$

$$
y''=\left(4ax^{2}+\left(8a+4b\right)x+2a+4b\right)e^{2x}
$$

Step 3. Subtract $4y$ and collect.

$$
e^{2x}\left[\left(4ax^{2}+\left(8a+4b\right)x+2a+4b\right)-\left(4ax^{2}+4bx\right)\right]=e^{2x}\left(8ax+2a+4b\right)
$$

Step 4. Match with $xe^{2x}$.

$$
8a=1, \qquad 2a+4b=0
$$

Step 5. Solve: $a=\frac{1}{8}$ and $b=-\frac{1}{16}$. The verification is the bracket of Step 3 with these values, which equals $x$.

$$
y_{p}=\left(\frac{x^{2}}{8}-\frac{x}{16}\right)e^{2x}
$$

Step 6. The general solution. The term $-\frac{x}{16}e^{2x}$ is part of the particular integral and may not be dropped, because $xe^{2x}$ is not a solution of the homogeneous equation, so no choice of the arbitrary constants can replace it.

$$
y=c_{1}e^{2x}+c_{2}e^{-2x}+\left(\frac{x^{2}}{8}-\frac{x}{16}\right)e^{2x}
$$

### 4.19 Problem: an initial value problem

Solve $y''+3y'+2y=e^{-x}$ subject to $y(0)=1$ and $y'(0)=0$.

### 4.20 Solution: resonant particular integral, then two conditions

Step 1. The roots are $-1$ and $-2$, and the forcing exponent $-1$ is a simple root, so $s=1$.

$$
m^{2}+3m+2=(m+1)(m+2)=0, \qquad m=-1,\quad m=-2
$$

Step 2. The trial is $Axe^{-x}$, and the derivatives require care with the signs.

$$
y=Axe^{-x}, \qquad y'=A\left(1-x\right)e^{-x}, \qquad y''=A\left(x-2\right)e^{-x}
$$

Step 3. Substitute and collect.

$$
Ae^{-x}\left[\left(x-2\right)+3\left(1-x\right)+2x\right]=Ae^{-x}
$$

Step 4. Matching gives $A=1$, so $y_{p}=xe^{-x}$.

Step 5. Write the complete solution before applying any condition.

$$
y=c_{1}e^{-x}+c_{2}e^{-2x}+xe^{-x}
$$

Step 6. Impose $y(0)=1$ and then differentiate for the second condition.

$$
c_{1}+c_{2}=1
$$

$$
y'=-c_{1}e^{-x}-2c_{2}e^{-2x}+\left(1-x\right)e^{-x}, \qquad -c_{1}-2c_{2}+1=0
$$

Step 7. The pair of equations gives $c_{1}+2c_{2}=1$ and $c_{1}+c_{2}=1$, hence $c_{2}=0$ and $c_{1}=1$.

$$
y=\left(1+x\right)e^{-x}
$$

Step 8. Verify both the equation and the conditions. The derivatives are $y'=-xe^{-x}$ and $y''=\left(x-1\right)e^{-x}$, so

$$
y''+3y'+2y=e^{-x}\left[\left(x-1\right)-3x+2+2x\right]=e^{-x},
$$

and at $x=0$ the value is $1$ while the derivative is $0$.

## 5. Mathematical Extensions, Limits, and Common Errors

### 5.1 The boundary of the method

The method of undetermined coefficients succeeds because the space spanned by the standard shapes is mapped into itself by the operator, and because the restricted operator is invertible off the kernel. Both properties are special. A function such as $\sec x$ is not mapped into any finite-dimensional space by repeated differentiation, and neither is $\ln x$, $\tan x$ or $\frac{1}{x}$. For such forcing terms no finite trial can match the equation, and the correct conclusion is not that the arithmetic is hard but that the method does not apply at all.

The structural way to describe the boundary is through annihilators. A forcing term admits a trial of the tabulated type exactly when it is annihilated by some polynomial in $D$ with constant coefficients; for instance $D-\mu$ annihilates $e^{\mu x}$, and $\left(D-\mu\right)^{2}$ annihilates $xe^{\mu x}$. Functions outside the catalogue have no constant-coefficient annihilator, which is why the trial method fails for them.

When the catalogue is exhausted, the general structure $y=y_{c}+y_{p}$ still holds, and the particular integral is found by variation of parameters, in which the constants of the complementary function are replaced by functions and a pair of first-order equations is solved. That method always works for continuous forcing, but the resulting integrals are frequently not elementary, and it is not the subject of this topic.

### 5.2 The meaning and the limits of resonance

The factor $x$ in a resonant particular integral is an idealisation. It predicts unbounded growth, and unbounded growth never happens in a physical system, because the model that produced it ignores effects that become important once the amplitude is large. In a real mechanical system, damping limits the amplitude, and nonlinear effects eventually detune the system from the forcing frequency. The prediction should therefore be read as a statement about a time interval short enough for those effects to be negligible, and the factor $x$ is the leading term of the correct asymptotic description on that interval.

Mathematically, the growth is a consequence of the double structure of the operator: a simple resonance produces one factor $x$, and a resonance with a double root produces $x^{2}$. For an equation of order $n$ the multiplicity can be as large as $n$, and the power of $x$ equals the multiplicity. This is the exact general statement, and the second-order case is the special case $n=2$.

### 5.3 Extensions to wider classes of equations

Three extensions are worth naming, because each preserves the structure theorem while changing the computational detail.

The first is higher order. For an equation of order $n$ with constant coefficients the complementary function carries $n$ constants, the auxiliary equation has degree $n$, and the trial rule is unchanged except that the index of duplication may now take the values $0$ to $n$. The theorem of undetermined coefficients is proved in exactly the same way, with $G$ of degree $n-s$ and the same triangular argument.

The second is the case of a forcing term built from several independent pieces. Superposition handles this without new theory: a particular integral for the sum is the sum of particular integrals, and the only care needed is that each piece is analysed with its own index of duplication. A common error is to compute one index for the whole right-hand side rather than one for each piece.

The third is the class of equations with non-constant coefficients of Euler type, in which the coefficients are powers of $x$ matching the order of the derivative. The substitution $x=e^{t}$ converts such an equation into a constant-coefficient equation in $t$, after which everything in this topic applies verbatim, including the trial table. The conversion is the whole content of that extension, and the structure theorem is unaffected.

### 5.4 Common errors and their diagnosis

Six errors account for nearly all lost marks in this topic, and each has a distinctive symptom that identifies it immediately.

The first is omitting the factor $x$ when the forcing term duplicates a natural solution. The symptom is a collapse of the left-hand side to zero, leaving $0=Q$, or a singular coefficient system. The cure is to compute the index of duplication before writing the trial.

The second is including a factor $x$ when there is no duplication. The symptom is a coefficient forced to zero in contradiction with the remaining equations, because the left-hand side produces shapes such as $x^{2}e^{2x}$ that the forcing term does not contain.

The third is truncating a polynomial trial. Omitting the constant term, or the linear term, when the corresponding power is present in the forcing term produces an inconsistent system, since the left-hand side generates powers that have nowhere to go. The trial must run through every power up to the degree of the forcing polynomial.

The fourth is dropping the sine when the forcing term is a cosine, or the cosine when the forcing term is a sine. The operator mixes the two, so both are required, and the missing one usually reappears as an unmatched term in the verification.

The fifth is applying the initial conditions to the particular integral alone. The symptom is a solution that satisfies the conditions but not the equation, or the reverse, and the cure is to assemble $y=y_{c}+y_{p}$ before differentiating.

The sixth is failing to verify. Verification of the particular integral is a two-line computation and it detects every one of the errors above, because the substitution reproduces the forcing term only when the coefficient matching is correct.

Two subtler errors deserve mention. Writing $s=1$ because the forcing frequency resembles a characteristic root, without checking the sign of the imaginary part, produces a trial that is not resonant when it should be, or the reverse; the test is on $\mu=\alpha+i\beta$, not on $\beta$ alone. Treating the operator factors in the wrong order in the two-stage integration is harmless, since constant-coefficient operators commute, but treating the inverse operator as an ordinary fraction is not: $\frac{1}{D-a}$ denotes integration followed by multiplication by $e^{ax}$, and nothing else.

### 5.5 Summary of the procedure and of the theory

The procedure is fixed. Solve the auxiliary equation and write the complementary function from its roots. Read $\mu=\alpha+i\beta$ from the forcing term and compute its multiplicity $s$ as a characteristic root. Write the trial of the tabulated shape multiplied by $x^{s}$. Differentiate twice, substitute, and solve the resulting square linear system for the coefficients. Add the two parts, impose any conditions on the complete solution, and verify.

The theory explains why the procedure cannot fail. Linearity makes the solution set an affine translate of the homogeneous solution space, so every solution is $y_{c}+y_{p}$ and no solution is missing. The exponential shift converts the exponential part of the forcing term into a shift of the operator, and the polynomial part into a problem of linear algebra on polynomials. On that finite-dimensional space the restricted operator is upper triangular with nonzero diagonal entries, hence invertible, so exactly one trial of the prescribed shape works. The multiplicity $s$ appears because the shift moves the operator's root structure into the count of derivatives, and a root of multiplicity $s$ costs exactly $s$ powers of $x$ before the diagonal entry becomes nonzero again.

Read in that order, the topic contains no guesswork. The word undetermined refers only to the coefficients, which are unknown until the linear system is solved; the shape is determined in advance by the structure of the operator and of the forcing term, and the coefficients are then determined uniquely by the equation itself.
