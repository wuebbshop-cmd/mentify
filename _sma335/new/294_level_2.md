## 1. Foundational Concepts, Definitions, and Axioms

### 1.1 One equation of order n, and the idea of a state

A single equation of order four is a statement about a function and four of its derivatives at once. Such an equation is not intractable, but it is awkward: the standard theory of differential equations is developed in greatest depth for systems of first-order equations, one equation per unknown, and numerical solvers are written for exactly that form. The technique of this topic removes the awkwardness by replacing one equation of order $n$ with $n$ equations of order one, coupled to one another, and then solving the coupled collection by linear algebra.

The gain is not merely cosmetic. Once the equation is a first-order system, the whole problem becomes an eigenvalue problem for a square matrix, and the classification of solutions becomes a classification of eigenvalues: distinct real, repeated real, or complex conjugate. Every case that was handled separately in the scalar theory reappears as one line of matrix algebra.

### 1.2 The new variables

The reduction rests on a single observation. If the function $y$ is known, then its derivatives are determined, so nothing is lost by giving each derivative its own name and then asking what equation each name satisfies.

> **Definition (State variables).** Let $y$ be a function of the independent variable $t$. The state variables of the reduction are
>
> $$
> x_{1}=y, \qquad x_{2}=\frac{dy}{dt}, \qquad x_{3}=\frac{d^{2}y}{dt^{2}}, \qquad \dots, \qquad x_{n}=\frac{d^{n-1}y}{dt^{n-1}} .
> $$

The name state variable is used because the list carries the complete state of the unknown function at a single instant: from the list one can reconstruct the value of $y$ and of its first $n-1$ derivatives, and the differential equation then supplies the rate of change of the last entry. Nothing about the future behaviour of $y$ is missing from that list.

Differentiating the definitions one at a time produces a chain of first-order relations. The first $n-1$ of them are trivial tautologies, because each state variable was defined as the derivative of the one before it.

$$
\frac{dx_{1}}{dt}=x_{2}, \qquad \frac{dx_{2}}{dt}=x_{3}, \qquad \dots, \qquad \frac{dx_{n-1}}{dt}=x_{n} .
$$

The last relation is the original equation in disguise. If the equation of order $n$ can be solved for its highest derivative, say

$$
\frac{d^{n}y}{dt^{n}}=F\left(t, y, \frac{dy}{dt}, \dots, \frac{d^{n-1}y}{dt^{n-1}}\right),
$$

then substituting the state variables gives

$$
\frac{dx_{n}}{dt}=F\left(t, x_{1}, x_{2}, \dots, x_{n}\right).
$$

Together these $n$ relations are a first-order system: each derivative of a state variable is expressed in terms of the state variables themselves and of $t$.

> **Definition (First-order system).** A first-order system of $n$ equations in $n$ unknown functions $x_{1},\dots,x_{n}$ is a collection of relations
>
> $$
> \frac{dx_{i}}{dt}=f_{i}\left(t, x_{1}, \dots, x_{n}\right), \qquad i=1,\dots,n ,
> $$
>
> in which only first derivatives appear.

### 1.3 Linear systems and the matrix form

The systems that arise from linear equations of order $n$ are themselves linear, and a linear system can always be written as a single matrix equation. This is the step that makes the eigenvalue machinery available.

> **Definition (Homogeneous linear system in matrix form).** Let $A$ be a constant $n\times n$ matrix and let $X$ be the column vector of the unknown functions. The homogeneous linear system is
>
> $$
> X'=AX ,
> $$
>
> where $X'$ denotes the column vector obtained by differentiating every entry of $X$.

> **Definition (Non-homogeneous linear system).** If $B$ is a column vector whose entries are known functions of $t$, then
>
> $$
> X'=AX+B
> $$
>
> is a non-homogeneous linear system, and $B$ is called the forcing vector.

The rule for assembling $A$ is mechanical and worth stating explicitly, because most algebraic errors in this topic occur at this step. Choose an order for the unknowns, and keep that order in every row, in the unknown vector, and in the derivative vector. Row $i$ of $A$ holds the coefficients of $x_{1},\dots,x_{n}$ in the equation for $x_{i}'$, written in the chosen order, with a zero wherever a variable is absent.

> **Definition (Companion matrix).** Consider the linear equation of order $n$ with constant coefficients,
>
> $$
> a_{0}\frac{d^{n}y}{dt^{n}}+a_{1}\frac{d^{n-1}y}{dt^{n-1}}+\cdots+a_{n-1}\frac{dy}{dt}+a_{n}y=f(t),
> $$
>
> with $a_{0}\neq 0$. After division by $a_{0}$ and reduction, the coefficient matrix is
>
> $$
> A=\begin{pmatrix} 0 & 1 & 0 & \cdots & 0 \\ 0 & 0 & 1 & \cdots & 0 \\ \vdots & \vdots & \vdots & \ddots & \vdots \\ 0 & 0 & 0 & \cdots & 1 \\ -a_{n} & -a_{n-1} & -a_{n-2} & \cdots & -a_{1} \end{pmatrix},
> $$
>
> and it is called the companion matrix of the equation.

The entries $a_{1},\dots,a_{n}$ in the definition are the coefficients after division by $a_{0}$, so the equation reads $y^{(n)}+a_{1}y^{(n-1)}+\cdots+a_{n}y=f(t)/a_{0}$. The companion matrix has ones immediately above the diagonal, zeros everywhere else in the first $n-1$ rows, and the negated coefficients in the last row, in reverse order. For a non-homogeneous equation the forcing vector is

$$
B=\begin{pmatrix} 0 \\ 0 \\ \vdots \\ 0 \\ f(t)/a_{0} \end{pmatrix},
$$

because only the last equation carries the forcing term.

### 1.4 The eigenvalue problem

> **Definition (Characteristic equation and eigenvalues).** Let $A$ be a square matrix and let $I$ be the identity matrix of the same order. The equation
>
> $$
> \det\left(A-mI\right)=0
> $$
>
> is the characteristic equation of $A$. Its roots $m$ are the eigenvalues of $A$, and the set of them is the spectrum of $A$.

The symbol $m$ is used for the eigenvalue throughout this topic; many texts write $\lambda$ for the same object, and the two letters mean exactly the same thing. The determinant $\det(A-mI)$ is a polynomial in $m$ of degree equal to the order of $A$, so a matrix of order $n$ has exactly $n$ eigenvalues counted with multiplicity, and those eigenvalues may be real and distinct, real and repeated, or complex.

> **Definition (Eigenvector).** A non-zero column vector $v$ is an eigenvector of $A$ belonging to the eigenvalue $m$ if
>
> $$
> Av=mv .
> $$

The definition excludes the zero vector deliberately. Every matrix sends the zero vector to zero, so admitting it would make the definition vacuous. Geometrically, an eigenvector is a direction that the matrix does not turn: multiplication by $A$ stretches or shrinks the vector but leaves its line through the origin unchanged. The number $m$ is the factor by which the stretching occurs, and a negative $m$ reverses the direction along that line.

To compute an eigenvector one solves the homogeneous linear system

$$
\left(A-mI\right)v=0 .
$$

Because $m$ was chosen to make the determinant vanish, the matrix $A-mI$ is singular, so this system has non-zero solutions; the solution set is the null space of $A-mI$, and any non-zero member of it is an eigenvector. It is conventional to report one convenient non-zero vector, since any non-zero multiple is equally valid.

### 1.5 Multiplicity, and the defective case

Two different counts attach to an eigenvalue, and confusing them is the single most common source of error in the repeated case.

> **Definition (Algebraic and geometric multiplicity).** The algebraic multiplicity of an eigenvalue $m$ is its multiplicity as a root of the characteristic polynomial. The geometric multiplicity is the dimension of the null space of $A-mI$, that is, the number of linearly independent eigenvectors belonging to $m$.

> **Definition (Defective matrix).** A matrix is defective if, for some eigenvalue, the geometric multiplicity is strictly smaller than the algebraic multiplicity.

For a matrix of order two with a double eigenvalue there are only two possibilities. Either the null space of $A-mI$ is one-dimensional, in which case there is a single eigenvector direction and the matrix is defective, or the null space is two-dimensional, in which case $A-mI$ is the zero matrix and $A$ is a scalar multiple of the identity. For matrices of order three and higher a repeated eigenvalue may have geometric multiplicity two while its algebraic multiplicity is three, and then the matrix is defective but two genuine eigenvectors exist.

A defective matrix cannot be diagonalised, and the corresponding system cannot be solved using eigenvectors alone. The remedy is a generalised eigenvector, defined by one extra equation.

> **Definition (Generalised eigenvector).** Let $m$ be an eigenvalue of $A$ with eigenvector $v$. A vector $u$ satisfying
>
> $$
> \left(A-mI\right)u=v
> $$
>
> is a generalised eigenvector of $A$ belonging to $m$ and attached to $v$.

The equation is solvable precisely when $v$ lies in the column space of $A-mI$, which is guaranteed for a defective eigenvalue of algebraic multiplicity two. The vector $u$ is not an eigenvector, since $(A-mI)u=v\neq 0$; it is the next object in a chain that begins with $v$.

### 1.6 Fundamental sets, the Wronskian, and the matrix of solutions

> **Definition (Fundamental set).** A set of $n$ solutions $X_{1},\dots,X_{n}$ of the system $X'=AX$ is a fundamental set on an interval if the vectors are linearly independent at every point of the interval. Their linear combination with arbitrary constant coefficients is then the general solution.

> **Definition (Wronskian).** If $X_{1},\dots,X_{n}$ are solutions, the Wronskian is the determinant of the matrix whose columns are those solutions,
>
> $$
> W(t)=\det\begin{pmatrix} X_{1} & X_{2} & \cdots & X_{n} \end{pmatrix}.
> $$

For solutions of a linear system with continuous coefficients the Wronskian is either zero everywhere or non-zero everywhere, so testing independence at a single convenient value of $t$ decides the question on the whole interval. The value $t=0$ is almost always the easiest, because every exponential factor becomes $1$ and the determinant reduces to a determinant of eigenvectors.

> **Definition (Fundamental matrix).** A matrix $\Phi(t)$ whose columns form a fundamental set is called a fundamental matrix of the system, and it satisfies $\Phi'=A\Phi$ together with $\det\Phi(t)\neq 0$.

### 1.7 Equivalent problems

> **Definition (Equivalence of a scalar equation and a system).** A scalar equation of order $n$ and a first-order system of $n$ equations are equivalent if the first component of every solution of the system solves the scalar equation, and every solution of the scalar equation arises as the first component of exactly one solution of the system.

Equivalence is the mathematical content of the reduction, and it is proved in Section 3.1 rather than assumed. The word exactly is what makes the correspondence useful: no solution is invented and none is lost, so the two problems have the same solution set described in two languages.

## 2. Theorems, Lemmas, and Analytical Properties

### 2.1 The reduction theorem

> **Theorem (Reduction of an equation of order n).** Suppose the scalar equation of order $n$ can be written as $y^{(n)}=F\left(t,y,y',\dots,y^{(n-1)}\right)$ with $F$ continuous. Let $x_{1}=y$, $x_{2}=y'$, and in general $x_{i}=y^{(i-1)}$ for $i=1,\dots,n$. Then $y$ solves the scalar equation on an interval if and only if the vector $X$ with entries $x_{1},\dots,x_{n}$ solves the system
>
> $$
> X'=AX+B
> $$
>
> on that interval, where $A$ and $B$ are the companion matrix and forcing vector of the equation.

The theorem is the licence for everything that follows. Its two directions are proved in Section 3.1; one direction is a chain of differentiations of definitions, and the other is a single differentiation of the first component.

### 2.2 The spectrum of the companion matrix

> **Theorem (Companion spectrum).** Let $A$ be the companion matrix of the linear equation $y^{(n)}+a_{1}y^{(n-1)}+\cdots+a_{n}y=0$. Then
>
> $$
> \det\left(A-mI\right)=\left(-1\right)^{n}\left(m^{n}+a_{1}m^{n-1}+\cdots+a_{n-1}m+a_{n}\right),
> $$
>
> so the eigenvalues of $A$ are exactly the roots of the auxiliary equation of the scalar problem, each with the same multiplicity.

This is the statement that makes the matrix method a genuine method rather than a repackaging. The auxiliary equation of the scalar theory and the characteristic equation of the companion matrix are the same polynomial up to the sign factor $(-1)^{n}$, which vanishes nowhere and therefore has no effect on the roots.

> **Corollary (Trace and determinant checks).** For a companion matrix of order $n$, the sum of the eigenvalues equals the trace, the product of the eigenvalues equals the determinant, and the coefficient $a_{1}$ equals the negative of the trace. For order two the characteristic equation reads
>
> $$
> m^{2}-(\operatorname{tr}A)\,m+\det A=0 ,
> $$
>
> which gives an immediate arithmetic check on every computed pair of eigenvalues.

### 2.3 The distinct real eigenvalue case

> **Theorem (General solution for distinct real eigenvalues).** Let $A$ be a constant $n\times n$ matrix with real eigenvalues $m_{1},\dots,m_{n}$, no two equal, and let $v_{1},\dots,v_{n}$ be corresponding eigenvectors. Then the general solution of $X'=AX$ is
>
> $$
> X=c_{1}v_{1}e^{m_{1}t}+c_{2}v_{2}e^{m_{2}t}+\cdots+c_{n}v_{n}e^{m_{n}t},
> $$
>
> with $c_{1},\dots,c_{n}$ arbitrary constants, and this expression gives every solution on the whole real line.

> **Lemma (Independence of eigenvectors from distinct eigenvalues).** Eigenvectors belonging to distinct eigenvalues of a single matrix are linearly independent.

The lemma supplies the hypothesis that the theorem needs and is proved in Section 3.3. It is the reason the distinct case is the easy case: independence is automatic, so no Wronskian computation is required to justify the general solution, although computing one is still a sensible check.

### 2.4 The repeated real eigenvalue case

> **Theorem (Defective repeated eigenvalue).** Suppose $A$ has a real eigenvalue $m$ of algebraic multiplicity two whose null space is one-dimensional, with eigenvector $v$. Let $u$ solve $\left(A-mI\right)u=v$. Then two linearly independent solutions of $X'=AX$ are
>
> $$
> X_{1}=ve^{mt}, \qquad X_{2}=\left(vt+u\right)e^{mt},
> $$
>
> and the general solution is $X=c_{1}X_{1}+c_{2}X_{2}$.

> **Theorem (Repeated eigenvalue with two independent eigenvectors).** If $A$ has a real eigenvalue $m$ of algebraic multiplicity two and the null space of $A-mI$ is two-dimensional, with independent eigenvectors $v_{1}$ and $v_{2}$, then the general solution is
>
> $$
> X=c_{1}v_{1}e^{mt}+c_{2}v_{2}e^{mt},
> $$
>
> and no term containing $t$ is needed.

The contrast between the two theorems is the heart of the repeated case. The factor $t$ in the second solution of the defective theorem is not a decoration: it is the price paid for the missing eigenvector direction. When nothing is missing, nothing is paid.

### 2.5 The complex conjugate case

> **Theorem (Complex eigenvalues give real solutions).** Let $A$ be a real matrix with eigenvalue $m=\alpha+i\beta$, where $\beta\neq 0$, and eigenvector $v=p+iq$ with $p$ and $q$ real vectors. Then the real and imaginary parts of $ve^{mt}$ are two linearly independent real solutions of $X'=AX$, namely
>
> $$
> X_{1}=e^{\alpha t}\left(p\cos\beta t-q\sin\beta t\right), \qquad X_{2}=e^{\alpha t}\left(p\sin\beta t+q\cos\beta t\right).
> $$

Because $A$ is real, the conjugate $\bar{m}=\alpha-i\beta$ is also an eigenvalue with conjugate eigenvector $\bar{v}=p-iq$, and the two complex solutions are conjugates of one another. Taking real and imaginary parts therefore produces two real solutions from one complex eigenvector, and no separate computation for the conjugate eigenvalue is required.

### 2.6 The non-homogeneous case

> **Theorem (Structure of the non-homogeneous solution).** If $X_{p}$ is any particular solution of $X'=AX+B$ and $X_{c}$ is the general solution of the associated homogeneous system $X'=AX$, then
>
> $$
> X=X_{c}+X_{p}
> $$
>
> is the general solution of the non-homogeneous system.

> **Theorem (Variation of parameters).** Let $\Phi$ be a fundamental matrix of $X'=AX$. Then a particular solution of $X'=AX+B$ is
>
> $$
> X_{p}=\Phi(t)\int\Phi^{-1}(s)B(s)\,ds ,
> $$
>
> and the integral is taken entry by entry, with one arbitrary constant vector absorbed into $X_{c}$.

> **Theorem (Undetermined coefficients for resonant forcing).** Suppose $B(t)=we^{\mu t}$ where $w$ is a constant vector. If $\mu$ is not an eigenvalue of $A$, a particular solution has the form $X_{p}=ze^{\mu t}$ with $z$ found from $\left(A-\mu I\right)z=-w$. If $\mu$ is an eigenvalue of $A$, no such $z$ exists and the correct trial is $X_{p}=\left(zt+z_{1}\right)e^{\mu t}$, with $z$ an eigenvector for $\mu$ and $z_{1}$ a generalised eigenvector.

The second clause is the resonance phenomenon of the scalar theory appearing in matrix language. The system $\left(A-\mu I\right)z=-w$ is singular exactly when $\mu$ is an eigenvalue, so the trial of the first clause fails precisely in that case.

### 2.7 The converse direction

> **Lemma (From a system back to one equation).** Let $A$ be a constant matrix of order $n$ and let $x_{1}$ be the first component of a solution of $X'=AX$. Then $x_{1}$ satisfies a scalar linear equation of order $n$ whose auxiliary polynomial is $\det\left(A-mI\right)$ up to sign.

> **Theorem (Cayley–Hamilton).** Every square matrix satisfies its own characteristic equation, so the powers $I,A,A^{2},\dots,A^{n}$ are linearly dependent.

The lemma is what allows a system to be answered in the language in which the question was asked, and it provides an independent check: if a system is claimed to be equivalent to a certain scalar equation, the characteristic polynomials must agree.

## 3. Formal Proofs, Derivations, and Methods

### 3.1 Proof of the reduction theorem

Let $y$ be a solution of $y^{(n)}=F\left(t,y,y',\dots,y^{(n-1)}\right)$ on an interval. Define $x_{i}=y^{(i-1)}$ for $i=1,\dots,n$. For each $i$ from $1$ to $n-1$, differentiating the definition gives

$$
x_{i}'=\frac{d}{dt}y^{(i-1)}=y^{(i)}=x_{i+1},
$$

which is the $i$-th equation of the system. Differentiating the definition of $x_{n}$ gives

$$
x_{n}'=y^{(n)}=F\left(t,y,y',\dots,y^{(n-1)}\right)=F\left(t,x_{1},x_{2},\dots,x_{n}\right),
$$

which is the last equation. Hence $X$ solves the system. When the scalar equation is linear with constant coefficients, the right-hand side is a linear combination of $x_{1},\dots,x_{n}$ plus the forcing term, and the coefficients assemble into the companion matrix and forcing vector.

Conversely, let $X$ solve the system. Put $y=x_{1}$. The first $n-1$ equations give, one after another,

$$
x_{2}=x_{1}'=y', \qquad x_{3}=x_{2}'=y'', \qquad \dots, \qquad x_{n}=x_{n-1}'=y^{(n-1)} .
$$

Substituting these identifications into the last equation gives $y^{(n)}=F\left(t,y,y',\dots,y^{(n-1)}\right)$, so $y$ solves the scalar equation. The correspondence is a bijection because each side determines the other by differentiation or by the definitions, and because the value of $X$ at a single point determines the value of $y$ and its first $n-1$ derivatives there.

### 3.2 Derivation of the companion characteristic polynomial

Write $D_{n}(m)$ for the determinant of $mI-A$ when $A$ is the companion matrix of order $n$ with coefficients $a_{1},\dots,a_{n}$. The first column of $mI-A$ has the single non-zero entry $m$ in the first row, and the entry $a_{n}$ in the last row,

$$
mI-A=\begin{pmatrix} m & -1 & 0 & \cdots & 0 \\ 0 & m & -1 & \cdots & 0 \\ \vdots & \vdots & \vdots & \ddots & \vdots \\ 0 & 0 & 0 & \cdots & -1 \\ a_{n} & a_{n-1} & a_{n-2} & \cdots & m+a_{1} \end{pmatrix}.
$$

Expand $D_{n}$ along that column. The entry $m$ at position $(1,1)$ has cofactor $D_{n-1}$, since deleting the first row and first column leaves exactly the companion determinant of order $n-1$ with coefficients $a_{1},\dots,a_{n-1}$. The entry $a_{n}$ at position $(n,1)$ has cofactor $(-1)^{n+1}$ times the determinant of the remaining block, and that block is lower triangular with diagonal entries all equal to $-1$, so its determinant is $(-1)^{n-1}$. Therefore

$$
D_{n}(m)=mD_{n-1}(m)+(-1)^{n+1}(-1)^{n-1}a_{n}=mD_{n-1}(m)+a_{n},
$$

because $(-1)^{n+1}(-1)^{n-1}=(-1)^{2n}=1$. The base case is order one, where the matrix is the single entry $-a_{1}$ and $D_{1}(m)=m+a_{1}$. Induction now gives

$$
D_{n}(m)=m^{n}+a_{1}m^{n-1}+a_{2}m^{n-2}+\cdots+a_{n-1}m+a_{n}.
$$

Since $\det(mI-A)=(-1)^{n}\det(A-mI)$, the two determinants differ only by the factor $(-1)^{n}$, and the roots are identical.

A direct check for order two confirms the formula. For the equation $y''+5y'+6y=0$ the companion matrix is

$$
A=\begin{pmatrix} 0 & 1 \\ -6 & -5 \end{pmatrix},
$$

and $\det\left(A-mI\right)=(-m)(-5-m)+6=m^{2}+5m+6=(m+2)(m+3)$, whose roots $-2$ and $-3$ are exactly the roots of the auxiliary equation.

### 3.3 Derivation of the eigen-solution formula

Suppose $Av=mv$ with $v\neq 0$, and set $X=ve^{mt}$. Then

$$
X'=mve^{mt}, \qquad AX=Ave^{mt}=mve^{mt},
$$

so $X'=AX$ and $X$ is a solution. Because the system is linear and homogeneous, any finite sum of solutions with constant coefficients is again a solution, so

$$
X=c_{1}v_{1}e^{m_{1}t}+\cdots+c_{n}v_{n}e^{m_{n}t}
$$

solves the system for all choices of the constants.

It remains to show that this is the general solution, and that requires independence. Suppose a linear combination of the eigenvectors vanishes,

$$
\alpha_{1}v_{1}+\alpha_{2}v_{2}+\cdots+\alpha_{n}v_{n}=0 .
$$

Multiply by $A-m_{n}I$. The last term is annihilated, because $\left(A-m_{n}I\right)v_{n}=0$, while every other term survives with its vector rescaled by a non-zero difference: $\left(A-m_{n}I\right)v_{j}=\left(m_{j}-m_{n}\right)v_{j}$ for $j\neq n$. Hence

$$
\alpha_{1}\left(m_{1}-m_{n}\right)v_{1}+\cdots+\alpha_{n-1}\left(m_{n-1}-m_{n}\right)v_{n-1}=0 .
$$

Repeating the device with $A-m_{n-1}I$, and so on, isolates each coefficient in turn, and since all the differences $m_{i}-m_{j}$ with $i\neq j$ are non-zero, every $\alpha_{i}$ must vanish. The eigenvectors are therefore independent, and the matrix $V$ with those eigenvectors as columns is invertible. Evaluating the $n$ solutions at $t=0$ gives columns $v_{1},\dots,v_{n}$, so

$$
W(0)=\det V\neq 0 ,
$$

and the solutions form a fundamental set. A fundamental set of $n$ solutions of a system of order $n$ spans the solution space, so the combination displayed above with arbitrary constants is the general solution.

### 3.4 Derivation of the repeated-eigenvalue device

Let $m$ be a defective eigenvalue with eigenvector $v$, so that $\left(A-mI\right)v=0$ but the null space is one-dimensional. Try a second solution of the form

$$
X_{2}=\left(vt+u\right)e^{mt},
$$

where $u$ is a vector still to be found. Differentiating and using the product rule gives

$$
X_{2}'=ve^{mt}+m\left(vt+u\right)e^{mt},
$$

whereas multiplying by $A$ and using $Av=mv$ gives

$$
AX_{2}=\left(Avt+Au\right)e^{mt}=\left(mvt+Au\right)e^{mt}.
$$

The terms containing $t$ agree automatically, since both equal $mvt\,e^{mt}$. Comparing the remaining terms and cancelling the common factor $e^{mt}$ leaves

$$
v+mu=Au,
$$

which is the same statement as

$$
\left(A-mI\right)u=v .
$$

So the trial succeeds exactly when this linear system is solvable, and it is solvable because $v$ lies in the column space of $A-mI$ for a defective eigenvalue of algebraic multiplicity two. Any solution $u$ will do, since adding a multiple of $v$ to $u$ merely changes $X_{2}$ by a multiple of $X_{1}$, which is already in the general solution.

Independence of $X_{1}=ve^{mt}$ and $X_{2}=\left(vt+u\right)e^{mt}$ follows from evaluating at $t=0$: the Wronskian is the determinant of the matrix with columns $v$ and $u$, and that determinant is non-zero because $u$ is not a multiple of $v$. Indeed, if $u$ were a multiple of $v$ then $\left(A-mI\right)u$ would be zero, contradicting $\left(A-mI\right)u=v\neq 0$.

### 3.5 Derivation of the real form in the complex case

Let $m=\alpha+i\beta$ with $\beta\neq 0$ and let $v=p+iq$ be a complex eigenvector, with $p$ and $q$ real vectors. Substituting into $Av=mv$ and separating real and imaginary parts gives the pair of real equations

$$
Ap=\alpha p-\beta q, \qquad Aq=\beta p+\alpha q .
$$

Euler's formula writes the complex solution as

$$
ve^{mt}=\left(p+iq\right)e^{\alpha t}\left(\cos\beta t+i\sin\beta t\right)=e^{\alpha t}\left[\left(p\cos\beta t-q\sin\beta t\right)+i\left(p\sin\beta t+q\cos\beta t\right)\right].
$$

Because $A$ is real and the system is linear, both the real part and the imaginary part of a complex solution are real solutions. Therefore

$$
X_{1}=e^{\alpha t}\left(p\cos\beta t-q\sin\beta t\right), \qquad X_{2}=e^{\alpha t}\left(p\sin\beta t+q\cos\beta t\right)
$$

both solve the system, and they are independent because $p$ and $q$ are independent: if $q$ were a multiple of $p$, the two equations displayed at the start of this subsection would force $\beta p=0$, which is impossible for $\beta\neq 0$ and $p\neq 0$.

### 3.6 Derivation of variation of parameters

Let $\Phi$ be a fundamental matrix, so that $\Phi'=A\Phi$ and $\Phi$ is invertible. Seek a particular solution of $X'=AX+B$ in the form $X=\Phi(t)G(t)$ for an unknown vector function $G$. Differentiating the product gives

$$
X'=\Phi'G+\Phi G'=A\Phi G+\Phi G'.
$$

Substituting into the system and cancelling the common term $A\Phi G$ leaves

$$
\Phi G'=B, \qquad \text{so} \qquad G'=\Phi^{-1}B .
$$

Integrating entry by entry gives $G(t)=\int\Phi^{-1}(s)B(s)\,ds$, and therefore $X_{p}=\Phi(t)\int\Phi^{-1}(s)B(s)\,ds$. The arbitrary constant vector produced by the integration reproduces the complementary solution when multiplied by $\Phi$, which is why it may be set to zero without loss.

### 3.7 Method: solving a system by the matrix method

1. Write the system in the form $X'=AX+B$, fixing one order for the unknowns and using it in every row.
2. Form the characteristic equation $\det\left(A-mI\right)=0$ and solve it exactly, factoring rather than guessing.
3. Compute one eigenvector for each eigenvalue by solving $\left(A-mI\right)v=0$, taking a convenient non-zero solution and clearing fractions.
4. Verify each pair by direct multiplication, checking that $Av=mv$ entry by entry.
5. Select the case. For distinct real eigenvalues use exponentials; for a repeated defective eigenvalue use a generalised eigenvector and one factor of $t$; for a complex conjugate pair convert to real form.
6. Assemble the general solution as a linear combination with $n$ arbitrary constants, and confirm that the count equals the order.
7. Justify independence with a Wronskian evaluated at $t=0$, and verify the final answer by differentiation and substitution.

### 3.8 Method: reducing an equation of order n and solving it

1. Solve the equation algebraically for its highest derivative, then list the coefficients in the order in which the companion matrix needs them, that is $a_{n},a_{n-1},\dots,a_{1}$ with signs negated.
2. Write the system explicitly, one line per state variable, before writing the matrix; the explicit form catches ordering errors that the matrix hides.
3. Assemble $A$ and, for a non-homogeneous equation, the forcing vector whose last entry is $f(t)$ divided by the leading coefficient.
4. Solve by the matrix method, then read the answer off as the first component of $X$, or use the whole vector if the question asks for the derivatives as well.
5. Check the result against the auxiliary equation: the eigenvalues of the companion matrix must be the roots of the auxiliary polynomial, and the scalar answer must satisfy the original equation.

### 3.9 Method: verification protocol

Differentiate the claimed solution vector and substitute into $X'=AX+B$. Every entry of the residual must simplify to zero identically in $t$; a residual that vanishes only at isolated values of $t$ indicates an error. For a scalar answer obtained from the first component, differentiate it $n$ times and substitute into the original equation. Confirm the number of constants equals $n$, and if an initial condition was given, confirm it by evaluating at the initial time.

## 4. Representative Worked Examples and Solutions

### 4.1 Problem: reduce a second-order equation and solve the system

Reduce $y''+5y'+6y=0$ to a first-order system, write it in matrix form, and solve it by the matrix method.

### 4.2 Solution: companion matrix, spectrum, eigenvectors

Step 1. Introduce the state variables. Set $x_{1}=y$ and $x_{2}=y'$. Then $x_{1}'=x_{2}$, and the equation, solved for $y''$, gives $x_{2}'=-6x_{1}-5x_{2}$.

Step 2. Write the system explicitly.

$$
x_{1}'=x_{2}, \qquad x_{2}'=-6x_{1}-5x_{2} .
$$

Step 3. Assemble the matrix form $X'=AX$ with the unknowns ordered $x_{1}$ then $x_{2}$.

$$
A=\begin{pmatrix} 0 & 1 \\ -6 & -5 \end{pmatrix}
$$

Step 4. Form the characteristic equation.

$$
\det\left(A-mI\right)=\begin{vmatrix} -m & 1 \\ -6 & -5-m \end{vmatrix}=(-m)(-5-m)+6=m^{2}+5m+6=0
$$

Step 5. Factor and read off the eigenvalues.

$$
m^{2}+5m+6=(m+2)(m+3)=0, \qquad m_{1}=-2, \quad m_{2}=-3 .
$$

The trace is $-5$ and the determinant is $6$, and indeed $-2+(-3)=-5$ while $(-2)(-3)=6$.

Step 6. Find the eigenvector for $m_{1}=-2$.

$$
\left(A+2I\right)v=\begin{pmatrix} 2 & 1 \\ -6 & -3 \end{pmatrix}\begin{pmatrix} a \\ b \end{pmatrix}=0 \quad \Longrightarrow \quad 2a+b=0 .
$$

Choose $a=1$ and $b=-2$, giving $v_{1}=(1,-2)$.

Step 7. Verify the first pair.

$$
Av_{1}=\begin{pmatrix} 0 & 1 \\ -6 & -5 \end{pmatrix}\begin{pmatrix} 1 \\ -2 \end{pmatrix}=\begin{pmatrix} -2 \\ 4 \end{pmatrix}=-2\begin{pmatrix} 1 \\ -2 \end{pmatrix}=-2v_{1} .
$$

Step 8. Find the eigenvector for $m_{2}=-3$.

$$
\left(A+3I\right)v=\begin{pmatrix} 3 & 1 \\ -6 & -2 \end{pmatrix}\begin{pmatrix} a \\ b \end{pmatrix}=0 \quad \Longrightarrow \quad 3a+b=0 .
$$

Choose $a=1$ and $b=-3$, giving $v_{2}=(1,-3)$.

Step 9. Verify the second pair.

$$
Av_{2}=\begin{pmatrix} 0 & 1 \\ -6 & -5 \end{pmatrix}\begin{pmatrix} 1 \\ -3 \end{pmatrix}=\begin{pmatrix} -3 \\ 9 \end{pmatrix}=-3\begin{pmatrix} 1 \\ -3 \end{pmatrix}=-3v_{2} .
$$

Step 10. Write the general solution.

$$
X=c_{1}\begin{pmatrix} 1 \\ -2 \end{pmatrix}e^{-2t}+c_{2}\begin{pmatrix} 1 \\ -3 \end{pmatrix}e^{-3t}
$$

Step 11. Read off the scalar answer, which is the first component.

$$
y=c_{1}e^{-2t}+c_{2}e^{-3t}
$$

Step 12. Check the scalar answer against the original equation. With $y=e^{-2t}$ the derivatives are $y'=-2e^{-2t}$ and $y''=4e^{-2t}$, so $y''+5y'+6y=(4-10+6)e^{-2t}=0$. With $y=e^{-3t}$ they are $y'=-3e^{-3t}$ and $y''=9e^{-3t}$, so $y''+5y'+6y=(9-15+6)e^{-3t}=0$. Both basis functions satisfy the equation, and two constants appear as required by order two.

Step 13. Confirm independence.

$$
W(0)=\begin{vmatrix} 1 & 1 \\ -2 & -3 \end{vmatrix}=-3+2=-1\neq 0 .
$$

### 4.3 Problem: reduce and solve a third-order equation

Reduce $y'''-6y''+11y'-6y=0$ to a first-order system, write the matrix form, and solve.

### 4.4 Solution: companion matrix of order three

Step 1. Introduce three state variables.

$$
x_{1}=y, \qquad x_{2}=y', \qquad x_{3}=y'' .
$$

Step 2. Write the system. The equation solved for $y'''$ is $y'''=6y-11y'+6y''$, so

$$
x_{1}'=x_{2}, \qquad x_{2}'=x_{3}, \qquad x_{3}'=6x_{1}-11x_{2}+6x_{3} .
$$

Step 3. Assemble the matrix.

$$
A=\begin{pmatrix} 0 & 1 & 0 \\ 0 & 0 & 1 \\ 6 & -11 & 6 \end{pmatrix}
$$

Step 4. Expand the characteristic determinant along the first column.

$$
\det\left(A-mI\right)=-m\begin{vmatrix} -m & 1 \\ -11 & 6-m \end{vmatrix}+6\begin{vmatrix} 1 & 0 \\ -m & 1 \end{vmatrix}
$$

Step 5. Evaluate both minors.

$$
\det\left(A-mI\right)=-m\left(m^{2}-6m+11\right)+6=-\left(m^{3}-6m^{2}+11m-6\right)
$$

Step 6. Factor the cubic.

$$
m^{3}-6m^{2}+11m-6=(m-1)(m-2)(m-3)
$$

so the eigenvalues are $m_{1}=1$, $m_{2}=2$, $m_{3}=3$. The sum is $6$, which equals the trace, and the product is $6$, which equals the determinant.

Step 7. Record the eigenvectors. For a companion matrix with last row $\left(-a_{n},\dots,-a_{1}\right)$, the vector $\left(1,m,m^{2}\right)$ is an eigenvector for the eigenvalue $m$, because the first two rows reproduce the shift and the last row reproduces the auxiliary equation. Hence

$$
v_{1}=\begin{pmatrix} 1 \\ 1 \\ 1 \end{pmatrix}, \qquad v_{2}=\begin{pmatrix} 1 \\ 2 \\ 4 \end{pmatrix}, \qquad v_{3}=\begin{pmatrix} 1 \\ 3 \\ 9 \end{pmatrix} .
$$

Step 8. Verify each pair by direct multiplication. For $m=1$,

$$
Av_{1}=\begin{pmatrix} 0 & 1 & 0 \\ 0 & 0 & 1 \\ 6 & -11 & 6 \end{pmatrix}\begin{pmatrix} 1 \\ 1 \\ 1 \end{pmatrix}=\begin{pmatrix} 1 \\ 1 \\ 1 \end{pmatrix}=1\cdot v_{1} .
$$

For $m=2$,

$$
Av_{2}=\begin{pmatrix} 0 & 1 & 0 \\ 0 & 0 & 1 \\ 6 & -11 & 6 \end{pmatrix}\begin{pmatrix} 1 \\ 2 \\ 4 \end{pmatrix}=\begin{pmatrix} 2 \\ 4 \\ 8 \end{pmatrix}=2\cdot v_{2} .
$$

For $m=3$,

$$
Av_{3}=\begin{pmatrix} 0 & 1 & 0 \\ 0 & 0 & 1 \\ 6 & -11 & 6 \end{pmatrix}\begin{pmatrix} 1 \\ 3 \\ 9 \end{pmatrix}=\begin{pmatrix} 3 \\ 9 \\ 27 \end{pmatrix}=3\cdot v_{3} .
$$

Step 9. Write the general solution.

$$
X=c_{1}\begin{pmatrix} 1 \\ 1 \\ 1 \end{pmatrix}e^{t}+c_{2}\begin{pmatrix} 1 \\ 2 \\ 4 \end{pmatrix}e^{2t}+c_{3}\begin{pmatrix} 1 \\ 3 \\ 9 \end{pmatrix}e^{3t}
$$

Step 10. Read off the first component.

$$
y=c_{1}e^{t}+c_{2}e^{2t}+c_{3}e^{3t}
$$

Step 11. Check one basis function completely. For $y=e^{2t}$ the derivatives are $y'=2e^{2t}$, $y''=4e^{2t}$ and $y'''=8e^{2t}$, so

$$
y'''-6y''+11y'-6y=(8-24+22-6)e^{2t}=0 .
$$

Step 12. Confirm independence at $t=0$.

$$
W(0)=\begin{vmatrix} 1 & 1 & 1 \\ 1 & 2 & 3 \\ 1 & 4 & 9 \end{vmatrix}=1(18-12)-1(9-3)+1(4-2)=6-6+2=2\neq 0 .
$$

### 4.5 Problem: a repeated eigenvalue that is defective

Solve $X'=AX$ for

$$
A=\begin{pmatrix} 0 & 1 \\ -4 & 4 \end{pmatrix} .
$$

### 4.6 Solution: one eigenvector, one generalised eigenvector

Step 1. Form the characteristic equation.

$$
\det\left(A-mI\right)=\begin{vmatrix} -m & 1 \\ -4 & 4-m \end{vmatrix}=m^{2}-4m+4=(m-2)^{2}=0
$$

so $m=2$ is a double eigenvalue. The trace is $4$ and the determinant is $4$, consistent with $2+2$ and $2\cdot 2$.

Step 2. Compute the null space of $A-2I$.

$$
A-2I=\begin{pmatrix} -2 & 1 \\ -4 & 2 \end{pmatrix}
$$

Both rows reduce to the single equation $-2a+b=0$, so the null space is one-dimensional and the matrix is defective. With $a=1$ we get $b=2$, hence

$$
v=\begin{pmatrix} 1 \\ 2 \end{pmatrix} .
$$

Step 3. Verify the eigenvector.

$$
Av=\begin{pmatrix} 0 & 1 \\ -4 & 4 \end{pmatrix}\begin{pmatrix} 1 \\ 2 \end{pmatrix}=\begin{pmatrix} 2 \\ 4 \end{pmatrix}=2v .
$$

Step 4. Solve the generalised eigenvector equation $\left(A-2I\right)u=v$.

$$
\begin{pmatrix} -2 & 1 \\ -4 & 2 \end{pmatrix}\begin{pmatrix} a \\ b \end{pmatrix}=\begin{pmatrix} 1 \\ 2 \end{pmatrix} \quad \Longrightarrow \quad -2a+b=1 .
$$

The second row is twice the first, so the system is consistent, as the theory requires. Taking $a=0$ gives $b=1$, hence

$$
u=\begin{pmatrix} 0 \\ 1 \end{pmatrix} .
$$

Step 5. Verify the generalised eigenvector.

$$
\left(A-2I\right)u=\begin{pmatrix} -2 & 1 \\ -4 & 2 \end{pmatrix}\begin{pmatrix} 0 \\ 1 \end{pmatrix}=\begin{pmatrix} 1 \\ 2 \end{pmatrix}=v .
$$

Step 6. Write the general solution.

$$
X=c_{1}\begin{pmatrix} 1 \\ 2 \end{pmatrix}e^{2t}+c_{2}\left[\begin{pmatrix} 1 \\ 2 \end{pmatrix}t+\begin{pmatrix} 0 \\ 1 \end{pmatrix}\right]e^{2t}
$$

Step 7. Verify the second solution satisfies the system. Its components are $x_{1}=te^{2t}$ and $x_{2}=(2t+1)e^{2t}$, with derivatives

$$
x_{1}'=(1+2t)e^{2t}, \qquad x_{2}'=(4+4t)e^{2t} .
$$

The right-hand sides are

$$
x_{2}=(2t+1)e^{2t}, \qquad -4x_{1}+4x_{2}=(-4t+8t+4)e^{2t}=(4t+4)e^{2t},
$$

and both agree with the derivatives.

Step 8. State the general solution in full.

$$
x_{1}=c_{1}e^{2t}+c_{2}te^{2t}, \qquad x_{2}=2c_{1}e^{2t}+c_{2}(2t+1)e^{2t}
$$

Step 9. Note the scalar interpretation. The first component is $(c_{1}+c_{2}t)e^{2t}$, which is exactly the solution of $y''-4y'+4y=0$ with a double root $2$, as the auxiliary equation predicts.

### 4.7 Problem: a repeated eigenvalue in a third-order companion matrix

Solve the system obtained from $y'''-5y''+8y'-4y=0$.

### 4.8 Solution: one simple eigenvalue and one double eigenvalue

Step 1. Write the companion matrix.

$$
A=\begin{pmatrix} 0 & 1 & 0 \\ 0 & 0 & 1 \\ 4 & -8 & 5 \end{pmatrix}
$$

Step 2. Form and factor the characteristic polynomial.

$$
\det\left(A-mI\right)=-\left(m^{3}-5m^{2}+8m-4\right)=-(m-1)(m-2)^{2}
$$

Step 3. Record the eigenvalues with multiplicities: $m_{1}=1$ simple, and $m_{2}=2$ double. The trace is $5$ and $1+2+2=5$; the determinant is $4$ and $1\cdot 2\cdot 2=4$.

Step 4. Take the eigenvector for $m=1$.

$$
v_{1}=\begin{pmatrix} 1 \\ 1 \\ 1 \end{pmatrix}, \qquad Av_{1}=\begin{pmatrix} 1 \\ 1 \\ 4-8+5 \end{pmatrix}=\begin{pmatrix} 1 \\ 1 \\ 1 \end{pmatrix}=v_{1} .
$$

Step 5. Take the eigenvector for $m=2$.

$$
v_{2}=\begin{pmatrix} 1 \\ 2 \\ 4 \end{pmatrix}, \qquad Av_{2}=\begin{pmatrix} 2 \\ 4 \\ 4-16+20 \end{pmatrix}=\begin{pmatrix} 2 \\ 4 \\ 8 \end{pmatrix}=2v_{2} .
$$

Step 6. Test the null space of $A-2I$ for a second independent eigenvector.

$$
A-2I=\begin{pmatrix} -2 & 1 & 0 \\ 0 & -2 & 1 \\ 4 & -8 & 3 \end{pmatrix}
$$

The first two rows are independent, so the rank is at least two and the null space has dimension at most one. Since $v_{2}$ already spans that null space, the geometric multiplicity is one and the matrix is defective.

Step 7. Solve $\left(A-2I\right)u=v_{2}$ for a generalised eigenvector. The three equations are

$$
-2a+b=1, \qquad -2b+c=2, \qquad 4a-8b+3c=4 .
$$

The first two give $b=1+2a$ and $c=2+2b=4+4a$; substituting into the third gives $4a-8-16a+12+12a=4$, an identity. Hence any $a$ works, and taking $a=0$ gives

$$
u=\begin{pmatrix} 0 \\ 1 \\ 4 \end{pmatrix} .
$$

Step 8. Verify the generalised eigenvector.

$$
\left(A-2I\right)u=\begin{pmatrix} -2 & 1 & 0 \\ 0 & -2 & 1 \\ 4 & -8 & 3 \end{pmatrix}\begin{pmatrix} 0 \\ 1 \\ 4 \end{pmatrix}=\begin{pmatrix} 1 \\ 2 \\ -8+12 \end{pmatrix}=\begin{pmatrix} 1 \\ 2 \\ 4 \end{pmatrix}=v_{2} .
$$

Step 9. Write the general solution.

$$
X=c_{1}\begin{pmatrix} 1 \\ 1 \\ 1 \end{pmatrix}e^{t}+c_{2}\begin{pmatrix} 1 \\ 2 \\ 4 \end{pmatrix}e^{2t}+c_{3}\left[\begin{pmatrix} 1 \\ 2 \\ 4 \end{pmatrix}t+\begin{pmatrix} 0 \\ 1 \\ 4 \end{pmatrix}\right]e^{2t}
$$

Step 10. Read off the first component.

$$
y=c_{1}e^{t}+c_{2}e^{2t}+c_{3}te^{2t}
$$

Step 11. Verify the term $te^{2t}$ in the scalar equation. Its derivatives are

$$
y'=(1+2t)e^{2t}, \quad y''=(4+4t)e^{2t}, \quad y'''=(12+8t)e^{2t},
$$

so

$$
y'''-5y''+8y'-4y=\left[(12+8t)-5(4+4t)+8(1+2t)-4t\right]e^{2t},
$$

and the bracket equals $(12-20+8)+(8-20+16-4)t=0$. The term is genuinely needed, which confirms that the repeated root required a $t$ factor.

### 4.9 Problem: a complex conjugate pair

Solve $X'=AX$ for

$$
A=\begin{pmatrix} 1 & -1 \\ 1 & 1 \end{pmatrix} .
$$

### 4.10 Solution: Euler's formula and the real form

Step 1. Form the characteristic equation.

$$
\det\left(A-mI\right)=\begin{vmatrix} 1-m & -1 \\ 1 & 1-m \end{vmatrix}=(1-m)^{2}+1=m^{2}-2m+2=0
$$

Step 2. Solve the quadratic.

$$
m=\frac{2\pm\sqrt{4-8}}{2}=1\pm i
$$

so $\alpha=1$ and $\beta=1$. The trace is $2$ and the determinant is $2$, consistent with the pair summing to $2$ and multiplying to $2$.

Step 3. Find the eigenvector for $m=1+i$.

$$
\left(A-(1+i)I\right)v=\begin{pmatrix} -i & -1 \\ 1 & -i \end{pmatrix}\begin{pmatrix} a \\ b \end{pmatrix}=0 \quad \Longrightarrow \quad -ia-b=0 .
$$

Choose $a=1$ and $b=-i$, giving $v=(1,-i)$.

Step 4. Verify the complex pair.

$$
Av=\begin{pmatrix} 1 & -1 \\ 1 & 1 \end{pmatrix}\begin{pmatrix} 1 \\ -i \end{pmatrix}=\begin{pmatrix} 1+i \\ 1-i \end{pmatrix}, \qquad (1+i)v=(1+i)\begin{pmatrix} 1 \\ -i \end{pmatrix}=\begin{pmatrix} 1+i \\ 1-i \end{pmatrix} .
$$

Step 5. Separate the eigenvector into real and imaginary parts.

$$
v=p+iq, \qquad p=\begin{pmatrix} 1 \\ 0 \end{pmatrix}, \qquad q=\begin{pmatrix} 0 \\ -1 \end{pmatrix} .
$$

Step 6. Apply the real-form formulas with $\alpha=1$ and $\beta=1$.

$$
X=c_{1}e^{t}\left[\begin{pmatrix} 1 \\ 0 \end{pmatrix}\cos t-\begin{pmatrix} 0 \\ -1 \end{pmatrix}\sin t\right]+c_{2}e^{t}\left[\begin{pmatrix} 1 \\ 0 \end{pmatrix}\sin t+\begin{pmatrix} 0 \\ -1 \end{pmatrix}\cos t\right]
$$

Step 7. Simplify the two real solutions.

$$
X_{1}=e^{t}\begin{pmatrix} \cos t \\ \sin t \end{pmatrix}, \qquad X_{2}=e^{t}\begin{pmatrix} \sin t \\ -\cos t \end{pmatrix}
$$

Step 8. Verify the first real solution by substitution. Its derivatives are

$$
X_{1}'=e^{t}\begin{pmatrix} \cos t-\sin t \\ \sin t+\cos t \end{pmatrix}, \qquad AX_{1}=e^{t}\begin{pmatrix} \cos t-\sin t \\ \cos t+\sin t \end{pmatrix},
$$

and the two columns agree.

Step 9. State the general solution in components.

$$
x_{1}=e^{t}\left(c_{1}\cos t+c_{2}\sin t\right), \qquad x_{2}=e^{t}\left(c_{1}\sin t-c_{2}\cos t\right)
$$

Step 10. Interpret. The pair describes a spiral: the factor $e^{t}$ expands the radius while the sine and cosine rotate the direction, and the real part of the eigenvalue controls the expansion while the imaginary part controls the rotation.

### 4.11 Problem: a complex pair with decay

Solve $X'=AX$ for

$$
A=\begin{pmatrix} 2 & -5 \\ 2 & -4 \end{pmatrix} .
$$

### 4.12 Solution: conjugate eigenvalue, conjugate eigenvector

Step 1. Form the characteristic equation.

$$
\det\left(A-mI\right)=\begin{vmatrix} 2-m & -5 \\ 2 & -4-m \end{vmatrix}=(2-m)(-4-m)+10=m^{2}+2m+2=0
$$

Step 2. Solve it.

$$
m=-1\pm i
$$

so the real part is $-1$, which will produce decay, and the imaginary part is $1$.

Step 3. Find the eigenvector for $m=-1+i$.

$$
\left(A-(-1+i)I\right)v=\begin{pmatrix} 3-i & -5 \\ 2 & -3-i \end{pmatrix}\begin{pmatrix} a \\ b \end{pmatrix}=0
$$

The first row gives $(3-i)a-5b=0$. Choose $a=5$ and $b=3-i$.

Step 4. Verify the complex pair, including the second row.

$$
Av=\begin{pmatrix} 2 & -5 \\ 2 & -4 \end{pmatrix}\begin{pmatrix} 5 \\ 3-i \end{pmatrix}=\begin{pmatrix} 10-15+5i \\ 10-12+4i \end{pmatrix}=\begin{pmatrix} -5+5i \\ -2+4i \end{pmatrix}
$$

and

$$
(-1+i)v=\begin{pmatrix} -5+5i \\ (-1+i)(3-i) \end{pmatrix}=\begin{pmatrix} -5+5i \\ -3+i+3i+1 \end{pmatrix}=\begin{pmatrix} -5+5i \\ -2+4i \end{pmatrix},
$$

so the two agree.

Step 5. Separate into real and imaginary parts.

$$
p=\begin{pmatrix} 5 \\ 3 \end{pmatrix}, \qquad q=\begin{pmatrix} 0 \\ -1 \end{pmatrix}
$$

Step 6. Apply the real-form formulas with $\alpha=-1$ and $\beta=1$.

$$
X=e^{-t}\left\{c_{1}\left[\begin{pmatrix} 5 \\ 3 \end{pmatrix}\cos t-\begin{pmatrix} 0 \\ -1 \end{pmatrix}\sin t\right]+c_{2}\left[\begin{pmatrix} 5 \\ 3 \end{pmatrix}\sin t+\begin{pmatrix} 0 \\ -1 \end{pmatrix}\cos t\right]\right\}
$$

Step 7. State the components.

$$
x_{1}=e^{-t}\left(5c_{1}\cos t+5c_{2}\sin t\right), \qquad x_{2}=e^{-t}\left[(3c_{1}-c_{2})\cos t+(c_{1}+3c_{2})\sin t\right]
$$

Step 8. Verify by substitution. Differentiating $x_{1}$ gives

$$
x_{1}'=e^{-t}\left[\left(-5c_{1}+5c_{2}\right)\cos t+\left(-5c_{1}-5c_{2}\right)\sin t\right],
$$

and the right-hand side $2x_{1}-5x_{2}$ equals

$$
e^{-t}\left[\left(10c_{1}-15c_{1}+5c_{2}\right)\cos t+\left(10c_{2}-5c_{1}-15c_{2}\right)\sin t\right],
$$

which is the same expression.

Step 9. Verify the second component in the same way. Differentiating $x_{2}$ gives

$$
x_{2}'=e^{-t}\left[\left(-2c_{1}+4c_{2}\right)\cos t+\left(-4c_{1}-2c_{2}\right)\sin t\right],
$$

and the right-hand side $2x_{1}-4x_{2}$ equals

$$
e^{-t}\left[\left(10c_{1}-12c_{1}+4c_{2}\right)\cos t+\left(10c_{2}-4c_{1}-12c_{2}\right)\sin t\right],
$$

which again agrees. Both components satisfy the system, so the real form is correct and not merely plausible.

### 4.13 Problem: solve a non-homogeneous system

Solve

$$
X'=AX+B, \qquad A=\begin{pmatrix} 1 & 1 \\ 4 & 1 \end{pmatrix}, \qquad B=\begin{pmatrix} 0 \\ 3e^{2t} \end{pmatrix} .
$$

### 4.14 Solution: complementary function plus particular integral

Step 1. Form the characteristic equation of $A$.

$$
\det\left(A-mI\right)=\begin{vmatrix} 1-m & 1 \\ 4 & 1-m \end{vmatrix}=(1-m)^{2}-4=m^{2}-2m-3=0
$$

Step 2. Factor and record the eigenvalues.

$$
(m-3)(m+1)=0, \qquad m_{1}=3, \quad m_{2}=-1 .
$$

The trace is $2=3-1$ and the determinant is $-3=3\cdot(-1)$.

Step 3. Find and verify the eigenvector for $m=3$.

$$
\left(A-3I\right)=\begin{pmatrix} -2 & 1 \\ 4 & -2 \end{pmatrix}, \qquad v_{1}=\begin{pmatrix} 1 \\ 2 \end{pmatrix}, \qquad Av_{1}=\begin{pmatrix} 3 \\ 6 \end{pmatrix}=3v_{1} .
$$

Step 4. Find and verify the eigenvector for $m=-1$.

$$
\left(A+I\right)=\begin{pmatrix} 2 & 1 \\ 4 & 2 \end{pmatrix}, \qquad v_{2}=\begin{pmatrix} 1 \\ -2 \end{pmatrix}, \qquad Av_{2}=\begin{pmatrix} -1 \\ 2 \end{pmatrix}=-1\cdot v_{2} .
$$

Step 5. Write the complementary function.

$$
X_{c}=c_{1}\begin{pmatrix} 1 \\ 2 \end{pmatrix}e^{3t}+c_{2}\begin{pmatrix} 1 \\ -2 \end{pmatrix}e^{-t}
$$

Step 6. Choose a trial for the particular integral. The forcing is a constant vector times $e^{2t}$, and $2$ is not an eigenvalue, so no resonance occurs and the trial $X_{p}=ze^{2t}$ is appropriate.

$$
z=\begin{pmatrix} a \\ b \end{pmatrix}, \qquad X_{p}'=2ze^{2t}, \qquad AX_{p}+B=\left(Az+\begin{pmatrix} 0 \\ 3 \end{pmatrix}\right)e^{2t}
$$

Step 7. Cancel the exponential and solve the resulting algebraic system.

$$
2z=Az+\begin{pmatrix} 0 \\ 3 \end{pmatrix} \quad \Longrightarrow \quad \left(A-2I\right)z=-\begin{pmatrix} 0 \\ 3 \end{pmatrix}
$$

Step 8. Write the system out.

$$
\begin{pmatrix} -1 & 1 \\ 4 & -1 \end{pmatrix}\begin{pmatrix} a \\ b \end{pmatrix}=\begin{pmatrix} 0 \\ -3 \end{pmatrix} \quad \Longrightarrow \quad -a+b=0, \quad 4a-b=-3 .
$$

Step 9. Solve it. The first equation gives $a=b$, and the second then gives $3a=-3$, so $a=-1$ and $b=-1$.

$$
X_{p}=\begin{pmatrix} -1 \\ -1 \end{pmatrix}e^{2t}
$$

Step 10. Verify the particular integral directly.

$$
X_{p}'=\begin{pmatrix} -2 \\ -2 \end{pmatrix}e^{2t}, \qquad AX_{p}+B=\begin{pmatrix} -1-1 \\ -4-1+3 \end{pmatrix}e^{2t}=\begin{pmatrix} -2 \\ -2 \end{pmatrix}e^{2t} .
$$

Step 11. Write the general solution.

$$
X=c_{1}\begin{pmatrix} 1 \\ 2 \end{pmatrix}e^{3t}+c_{2}\begin{pmatrix} 1 \\ -2 \end{pmatrix}e^{-t}-\begin{pmatrix} 1 \\ 1 \end{pmatrix}e^{2t}
$$

Step 12. Verify the full solution by substitution in components.

$$
x_{1}=c_{1}e^{3t}+c_{2}e^{-t}-e^{2t}, \qquad x_{2}=2c_{1}e^{3t}-2c_{2}e^{-t}-e^{2t}
$$

The first equation requires $x_{1}'=x_{1}+x_{2}$, and indeed $3c_{1}e^{3t}-c_{2}e^{-t}-2e^{2t}$ equals $(3c_{1})e^{3t}+(c_{2}-c_{2})e^{-t}+(-1-1)e^{2t}$. The second requires $x_{2}'=4x_{1}+x_{2}+3e^{2t}$, and indeed $6c_{1}e^{3t}+2c_{2}e^{-t}-2e^{2t}$ equals $(4c_{1}+2c_{1})e^{3t}+(4c_{2}-2c_{2})e^{-t}+(-4-1+3)e^{2t}$.

### 4.15 Problem: an initial value problem

Solve the system of Section 4.13 subject to $x_{1}(0)=1$ and $x_{2}(0)=0$ with no forcing term, that is for $X'=AX$ with the same matrix.

### 4.16 Solution: impose the conditions on the general solution

Step 1. Start from the complementary function.

$$
X=c_{1}\begin{pmatrix} 1 \\ 2 \end{pmatrix}e^{3t}+c_{2}\begin{pmatrix} 1 \\ -2 \end{pmatrix}e^{-t}
$$

Step 2. Evaluate at $t=0$, where both exponentials equal one.

$$
c_{1}\begin{pmatrix} 1 \\ 2 \end{pmatrix}+c_{2}\begin{pmatrix} 1 \\ -2 \end{pmatrix}=\begin{pmatrix} 1 \\ 0 \end{pmatrix}
$$

Step 3. Read off the two scalar equations.

$$
c_{1}+c_{2}=1, \qquad 2c_{1}-2c_{2}=0 .
$$

Step 4. Solve them. The second gives $c_{1}=c_{2}$, and the first then gives $c_{1}=c_{2}=1/2$.

Step 5. State the solution.

$$
x_{1}=\frac{1}{2}e^{3t}+\frac{1}{2}e^{-t}, \qquad x_{2}=e^{3t}-e^{-t}
$$

Step 6. Verify the solution against the system. The two components are

$$
x_{1}=\frac{1}{2}e^{3t}+\frac{1}{2}e^{-t}, \qquad x_{2}=e^{3t}-e^{-t},
$$

with derivatives

$$
x_{1}'=\frac{3}{2}e^{3t}-\frac{1}{2}e^{-t}, \qquad x_{2}'=3e^{3t}+e^{-t}.
$$

Step 7. Check the first equation. The matrix $A$ has first row $(1,1)$, so the right-hand side is

$$
x_{1}+x_{2}=\frac{1}{2}e^{3t}+\frac{1}{2}e^{-t}+e^{3t}-e^{-t}=\frac{3}{2}e^{3t}-\frac{1}{2}e^{-t},
$$

which equals $x_{1}'$. The second row is $(4,1)$, so the right-hand side is

$$
4x_{1}+x_{2}=2e^{3t}+2e^{-t}+e^{3t}-e^{-t}=3e^{3t}+e^{-t},
$$

which equals $x_{2}'$. The solution is confirmed, and the initial condition was already checked in Step 5.

### 4.17 Problem: reduce a fourth-order equation to matrix form

Reduce $y^{(4)}-5y'''+7y''+9y'-6y=e^{t}$ to a first-order system and write it in matrix form, then state its characteristic equation without solving it.

### 4.18 Solution: four state variables and a forcing vector

Step 1. Solve for the highest derivative.

$$
y^{(4)}=5y'''-7y''-9y'+6y+e^{t}
$$

Step 2. Introduce four state variables.

$$
x_{1}=y, \qquad x_{2}=y', \qquad x_{3}=y'', \qquad x_{4}=y''' .
$$

Step 3. Write the four equations explicitly.

$$
x_{1}'=x_{2}, \qquad x_{2}'=x_{3}, \qquad x_{3}'=x_{4}, \qquad x_{4}'=6x_{1}-9x_{2}-7x_{3}+5x_{4}+e^{t} .
$$

Step 4. Assemble the matrix and the forcing vector, keeping the order $x_{1},x_{2},x_{3},x_{4}$ in every row.

$$
A=\begin{pmatrix} 0 & 1 & 0 & 0 \\ 0 & 0 & 1 & 0 \\ 0 & 0 & 0 & 1 \\ 6 & -9 & -7 & 5 \end{pmatrix}, \qquad B=\begin{pmatrix} 0 \\ 0 \\ 0 \\ e^{t} \end{pmatrix}
$$

Step 5. State the characteristic equation from the companion rule.

$$
m^{4}-5m^{3}+7m^{2}+9m-6=0
$$

Step 6. Confirm the signs by checking the two coefficients that are easy to get wrong. The trace of $A$ is $5$, and the coefficient of $m^{3}$ is $-5$, which must equal the negative trace. The determinant of $A$ is $-6$, obtained by expanding along the first column, and the constant term is $-6$, which must equal the determinant up to the sign $(-1)^{4}=1$. Both checks pass, so the assembled matrix is consistent with the polynomial.

## 5. Mathematical Extensions, Limits, and Common Errors

### 5.1 What the reduction preserves and what it does not

The reduction preserves the solution set exactly, but it changes the shape of the answer. A scalar equation of order $n$ produces one function; the equivalent system produces a vector of $n$ functions, whose entries are that function and its first $n-1$ derivatives. When a question asks for the vector, all components must be reported, and when it asks for the scalar, only the first component is the answer. Reporting the whole vector when only the scalar was requested is untidy but correct; reporting the first component when the question asked for the vector is incomplete.

The reduction also preserves the number of arbitrary constants, since the general solution of the system carries $n$ constants and the general solution of the scalar equation carries the same $n$. This invariance is the most reliable check on any answer produced by the matrix method.

### 5.2 Where the method stops

The method as developed requires $A$ to be a constant matrix. If the coefficients depend on $t$, the eigenvector computation still produces eigenvalues and eigenvectors at each instant, but those eigenvectors generally rotate with $t$, and the simple exponential combination is no longer a solution. Systems with variable coefficients require a fundamental matrix obtained by other means, and no eigenvalue formula replaces it.

The reduction itself works for non-linear equations, since the chain of definitions uses nothing but differentiation. What fails for non-linear equations is the matrix method, because a non-linear system has no coefficient matrix at all. The reduction is therefore the general-purpose step, while the eigenvalue solution is the special-purpose step that requires linearity and constant coefficients.

### 5.3 Beyond the course: the matrix exponential and Jordan chains

For a constant matrix $A$ the solution of $X'=AX$ with $X(0)=X_{0}$ is $X=e^{At}X_{0}$, where the exponential is defined by the power series

$$
e^{At}=I+At+\frac{A^{2}t^{2}}{2!}+\frac{A^{3}t^{3}}{3!}+\cdots .
$$

For a diagonalisable matrix this series collapses to the eigenvector expansion already derived, and for a defective matrix it produces exactly the polynomial factor $t$ that the generalised eigenvector device produced. The device is therefore not an ad hoc trick but the first term of a systematic construction called a Jordan chain: one solves $\left(A-mI\right)u_{1}=0$, then $\left(A-mI\right)u_{2}=u_{1}$, then $\left(A-mI\right)u_{3}=u_{2}$, and each new vector contributes one more power of $t$ to the solution.

### 5.4 Common errors

- **Writing the last row of the companion matrix in the wrong order.** The coefficients appear in reverse, from $a_{n}$ to $a_{1}$, each negated. Writing them in the order in which the equation is displayed produces a matrix whose spectrum is wrong.
- **Forgetting to negate.** For $y''+5y'+6y=0$ the last row is $(-6,-5)$, not $(6,5)$.
- **Dividing the equation but not the forcing term.** If the leading coefficient is not one, every coefficient in the last row must be divided by it, and the forcing vector must contain $f(t)$ divided by the same number.
- **Assuming the factor $t$ is always needed for a repeated eigenvalue.** It is needed only when the geometric multiplicity is smaller than the algebraic multiplicity. When two independent eigenvectors exist for a double eigenvalue, the general solution is a plain combination of exponentials.
- **Inserting the eigenvector instead of a generalised eigenvector.** For the defective case, writing $X_{2}=vte^{mt}$ alone fails, because the trial must also carry an unknown vector $u$ found from $\left(A-mI\right)u=v$.
- **Trying to solve $\left(A-mI\right)u=v$ without checking consistency.** The system is solvable only because $v$ lies in the column space of $A-mI$. If a computation produces an inconsistent pair of equations, the eigenvector is wrong.
- **Using a complex eigenvector as a final answer.** The system is real, so the answer must be real. The complex eigenvector is an intermediate object; the real and imaginary parts, combined as in Section 3.5, are the answer.
- **Pairing the real part with the wrong imaginary part.** The formula uses $p\cos\beta t-q\sin\beta t$ and $p\sin\beta t+q\cos\beta t$. Dropping the minus sign, or using $\alpha\cos$ instead of $\beta$, produces a vector that does not satisfy the system.
- **Computing only one eigenvalue in a conjugate pair.** The conjugate eigenvalue contributes no new real solution, so computing it is unnecessary, but its existence must be acknowledged so that the count of constants comes out right.
- **Forgetting the particular integral.** The general solution of a non-homogeneous system is the complementary function plus a particular integral; omitting the second part leaves an answer that fails the original system.
- **Using the non-resonant trial at resonance.** If the exponent in the forcing matches an eigenvalue, the trial $ze^{\mu t}$ cannot work because $A-\mu I$ is singular, and the trial must gain a factor of $t$.
- **Reporting fewer constants than the order.** A system of order three needs three constants. Two constants indicate a missed eigenvalue or a missed generalised eigenvector.
- **Skipping the verification.** Direct multiplication $Av=mv$ and direct differentiation of the final answer catch essentially every algebraic error in this topic, and both take under a minute.

### 5.5 Consolidated procedure

Every question in this topic follows the same path: reduce by naming the derivatives as state variables, assemble the matrix by listing coefficients in a fixed order, solve the characteristic equation exactly, find and verify eigenvectors, select the case and its formula, assemble the general solution with the correct number of constants, add a particular integral for a non-homogeneous system, and verify by substitution. The three cases are distinguished only by step five, and each case has one diagnostic question: are the eigenvalues distinct, is the repeated eigenvalue accompanied by enough eigenvectors, and is the eigenvalue complex. Answers to those questions determine the rest of the work, and the verification at the end confirms that the diagnosis was right.
