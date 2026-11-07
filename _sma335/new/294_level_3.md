## 1. Foundational Concepts, Definitions, and Axioms

### 1.1 What the examiner is actually testing

Every question on this topic is a chain with seven links, and marks are placed on the links, not on the final answer. The chain is: reduce the equation, assemble the matrix, form the characteristic equation, solve it, find eigenvectors, classify the eigenvalue case, write the general solution. A candidate who reaches the right answer by a lucky guess collects the last mark and loses the six before it, while a candidate who works the chain correctly but slips in the final arithmetic keeps almost everything. This is why the presentation of intermediate quantities matters more here than in most topics.

The second thing being tested is diagnosis. The three eigenvalue cases look identical up to the point where the characteristic equation is solved, and they diverge immediately afterwards. Recognising a defective matrix, or noticing that a pair of eigenvalues is complex, is worth more marks than any amount of algebra, because the wrong case produces an answer that cannot satisfy the system.

### 1.2 Definitions that must be reproduced exactly

> **Definition (State variables of the reduction).** For an equation of order $n$ in the unknown $y$, the state variables are
>
> $$
> x_{1}=y, \quad x_{2}=y', \quad x_{3}=y'', \quad \dots, \quad x_{n}=y^{(n-1)} .
> $$

> **Definition (Matrix form).** A homogeneous first-order system of $n$ equations is written $X'=AX$ with $A$ of order $n$; a non-homogeneous system is written $X'=AX+B$, where $B$ is a column of known functions.

> **Definition (Companion matrix).** For $y^{(n)}+a_{1}y^{(n-1)}+\cdots+a_{n-1}y'+a_{n}y=f(t)$ the coefficient matrix is
>
> $$
> A=\begin{pmatrix} 0 & 1 & 0 & \cdots & 0 \\ 0 & 0 & 1 & \cdots & 0 \\ \vdots & \vdots & \vdots & \ddots & \vdots \\ 0 & 0 & 0 & \cdots & 1 \\ -a_{n} & -a_{n-1} & -a_{n-2} & \cdots & -a_{1} \end{pmatrix}, \qquad B=\begin{pmatrix} 0 \\ 0 \\ \vdots \\ 0 \\ f(t) \end{pmatrix} .
> $$

> **Definition (Characteristic equation, eigenvalue).** The equation $\det\left(A-mI\right)=0$ is the characteristic equation of $A$; its roots are the eigenvalues.

> **Definition (Eigenvector).** A non-zero column $v$ with $Av=mv$ is an eigenvector belonging to $m$; equivalently $v$ is a non-zero solution of $\left(A-mI\right)v=0$.

> **Definition (Generalised eigenvector).** If $m$ is an eigenvalue with eigenvector $v$, a vector $u$ with $\left(A-mI\right)u=v$ is a generalised eigenvector attached to $v$.

> **Definition (Fundamental set and Wronskian).** Solutions $X_{1},\dots,X_{n}$ form a fundamental set when they are linearly independent; the Wronskian $W(t)$ is the determinant of the matrix of order $n$ whose columns are those solutions.

These seven statements are the whole vocabulary, and a question that says state the characteristic equation or define an eigenvector is asking for one of them verbatim.

### 1.3 Where the marks sit

| Stage of the solution | What is written | Typical marks |
| --- | --- | --- |
| Reduction | the $n$ first-order equations in state variables | 2 |
| Matrix form | the matrix $A$, and $B$ when present | 1 |
| Characteristic equation | the determinant set equal to zero | 1 |
| Determinant expanded | a polynomial in $m$ | 1 |
| Eigenvalues | roots with multiplicities stated | 2 |
| Eigenvectors | one column per eigenvalue, simplified | 3 |
| Verification of one pair | the multiplication $Av=mv$ | 1 |
| Independence | Wronskian evaluated at $t=0$ | 1 |
| General solution | the combination with $n$ constants | 2 |
| Particular integral | one solution of $X'=AX+B$ | 2 |
| Final scalar answer | the first component, when asked | 1 |

The table is a budget, not a guarantee, but it shows where effort pays. Eigenvectors carry the largest single block, and they are also where the majority of lost marks occur, because a sign slip there destroys the general solution even though the eigenvalues remain correct.

### 1.4 Notation discipline

Four conventions prevent most presentation errors. First, choose the order of the unknowns once and never change it; the state variables are naturally ordered $x_{1},\dots,x_{n}$, and the derivative column must follow that order. Second, the eigenvalue is written $m$ throughout, and the same letter is never reused for an index or a constant. Third, the identity matrix is written $I$ and never confused with the matrix $A$. Fourth, when a repeated eigenvalue is discussed, the two multiplicities are named separately in words, algebraic multiplicity for the root count and geometric multiplicity for the eigenvector count, so that the diagnosis is visible to the marker.

### 1.5 The decision tree after the characteristic equation

Once the eigenvalues are known, one question decides everything.

> **Definition (Case classification).** If the eigenvalues are real and distinct, each contributes one exponential solution. If some eigenvalue is repeated, count the independent eigenvectors for it: as many as its multiplicity means exponentials only, fewer means the missing solutions need factors of $t$ and generalised eigenvectors. If a pair is complex with non-zero imaginary part, split the complex solution into real and imaginary parts.

The classification is exhaustive for a real matrix, so there is no fourth case to look for. The cases can also be mixed within one matrix. A real cubic may have three real roots, or one real root together with one conjugate pair, but it cannot have two real roots and one complex root, because the complex roots of a real polynomial always occur in conjugate pairs. A matrix of order four may likewise carry two real roots and one conjugate pair, and then the answer combines two exponentials with one pair of cosine-and-sine solutions.

## 2. Theorems, Lemmas, and Analytical Properties

### 2.1 The statement bank

| Result | Content in one line | Marks when asked |
| --- | --- | --- |
| Reduction theorem | $y$ solves the equation if and only if the state vector solves the system | 3 for proof, 2 for use |
| Companion spectrum | eigenvalues of $A$ are the roots of the auxiliary polynomial | 2 |
| Distinct eigenvalue theorem | the general solution is the sum of eigenvector exponentials | 2 |
| Independence lemma | eigenvectors from distinct eigenvalues are independent | 2 |
| Defective repeated case | second solution is $vte^{mt}+ue^{mt}$ with $(A-mI)u=v$ | 3 |
| Repeated case with two directions | two exponentials, no factor of $t$ | 2 |
| Complex pair theorem | real solutions from real and imaginary parts | 3 |
| Non-homogeneous structure | general solution equals complementary plus particular | 1 |
| Variation of parameters | $X_{p}=\Phi\int\Phi^{-1}B$ | 3 |
| Trace and determinant lemma | sum and product of eigenvalues | 1 |
| Cayley–Hamilton | a matrix satisfies its characteristic equation | 2 |

### 2.2 The reduction theorem

> **Theorem (Reduction).** Let $F$ be continuous. The function $y$ solves $y^{(n)}=F\left(t,y,y',\dots,y^{(n-1)}\right)$ on an interval if and only if the column $X$ with entries $x_{i}=y^{(i-1)}$, for $i=1,\dots,n$, solves the system
>
> $$
> x_{i}'=x_{i+1}\ \ (i=1,\dots,n-1), \qquad x_{n}'=F\left(t,x_{1},\dots,x_{n}\right)
> $$
>
> on that interval. For a linear equation with constant coefficients the system takes the matrix form $X'=AX+B$ with $A$ the companion matrix.

The theorem is quoted in most examinations and proved in some, so the proof in Section 3.1 should be memorised in outline: one direction is a chain of differentiations of definitions, the other is the observation that the first $n-1$ equations identify each state variable with a derivative of the first.

### 2.3 The spectrum of the companion matrix

> **Theorem (Companion spectrum).** For the companion matrix of $y^{(n)}+a_{1}y^{(n-1)}+\cdots+a_{n}y=0$,
>
> $$
> \det\left(A-mI\right)=\left(-1\right)^{n}\left(m^{n}+a_{1}m^{n-1}+\cdots+a_{n-1}m+a_{n}\right).
> $$

> **Corollary (Checks).** The trace of $A$ equals $-a_{1}$ and also equals the sum of the eigenvalues; the determinant of $A$ equals $\left(-1\right)^{n}a_{n}$ and also equals the product of the eigenvalues. For order two the characteristic equation is $m^{2}-\left(\operatorname{tr}A\right)m+\det A=0$.

These identities convert a suspected eigenvalue error into a definite one within seconds, and they cost a single mark to state.

### 2.4 The distinct eigenvalue theorem and independence

> **Theorem (Distinct eigenvalues).** Let $m_{1},\dots,m_{n}$ be real and pairwise distinct eigenvalues of $A$ with eigenvectors $v_{1},\dots,v_{n}$. Then the general solution of $X'=AX$ is
>
> $$
> X=c_{1}v_{1}e^{m_{1}t}+\cdots+c_{n}v_{n}e^{m_{n}t} .
> $$

> **Lemma (Independence).** Eigenvectors belonging to distinct eigenvalues of one matrix are linearly independent. Consequently $\det\left(v_{1}\ \cdots\ v_{n}\right)\neq 0$ and the Wronskian at $t=0$ is non-zero.

> **Lemma (Companion eigenvector shortcut).** For the companion matrix of $y^{(n)}+a_{1}y^{(n-1)}+\cdots+a_{n}y=0$, the column with entries $1,m,m^{2},\dots,m^{n-1}$ is an eigenvector for the eigenvalue $m$, for every root $m$ of the auxiliary polynomial.

The shortcut is worth memorising because it removes an entire eigenvector computation in companion problems. Its verification takes two lines: the first $n-1$ rows shift the powers upward, and the last row reproduces the auxiliary equation evaluated at $m$.

### 2.5 The repeated eigenvalue theorems

> **Theorem (Defective case).** Let $m$ be a real eigenvalue whose algebraic multiplicity exceeds its geometric multiplicity, and let $v$ be an eigenvector for $m$. If $u$ solves $\left(A-mI\right)u=v$, then two independent solutions are $X_{1}=ve^{mt}$ and $X_{2}=\left(vt+u\right)e^{mt}$.

> **Theorem (Non-defective repeated case).** If the geometric multiplicity equals the algebraic multiplicity, with independent eigenvectors $v_{1},\dots,v_{k}$ for the repeated eigenvalue $m$, then the solutions $v_{j}e^{mt}$ are already independent and no factor of $t$ is required.

> **Lemma (Consistency of the generalised equation).** The system $\left(A-mI\right)u=v$ is solvable precisely when $v$ lies in the column space of $A-mI$. For an eigenvalue whose algebraic multiplicity exceeds its geometric multiplicity by one, every eigenvector $v$ for $m$ lies in that column space.

### 2.6 The complex pair theorem

> **Theorem (Complex eigenvalues).** Let $A$ be real with eigenvalue $m=\alpha+i\beta$, $\beta\neq 0$, and eigenvector $v=p+iq$ with $p,q$ real. Then
>
> $$
> X_{1}=e^{\alpha t}\left(p\cos\beta t-q\sin\beta t\right), \qquad X_{2}=e^{\alpha t}\left(p\sin\beta t+q\cos\beta t\right)
> $$
>
> are independent real solutions, and the conjugate eigenvalue $\alpha-i\beta$ produces their complex conjugates, so it contributes nothing new.

> **Corollary (Rotation counts).** With a conjugate pair the general solution of a system of order two contains exactly two constants and both cosine and sine; an answer with only a cosine term, or with one constant, cannot be the general solution.

### 2.7 The non-homogeneous theorems

> **Theorem (Structure).** If $X_{p}$ solves $X'=AX+B$ and $X_{c}$ is the general solution of $X'=AX$, then $X=X_{c}+X_{p}$ is the general solution of the non-homogeneous system.

> **Theorem (Undetermined coefficients).** If $B(t)=we^{\mu t}$ with $w$ constant, then a particular solution exists of the form $ze^{\mu t}$ with $\left(A-\mu I\right)z=-w$ whenever $\mu$ is not an eigenvalue. If $\mu$ is an eigenvalue, the trial must be $\left(zt+z_{1}\right)e^{\mu t}$ with $z$ an eigenvector for $\mu$.

> **Theorem (Variation of parameters).** With $\Phi$ a fundamental matrix of $X'=AX$, a particular solution is
>
> $$
> X_{p}=\Phi(t)\int\Phi^{-1}(s)B(s)\,ds .
> $$

### 2.8 The converse and Cayley–Hamilton

> **Lemma (System to scalar equation).** If $x_{1}$ is the first component of a solution of $X'=AX$ with $A$ of order $n$, then $x_{1}$ satisfies a linear equation of order $n$ whose auxiliary polynomial is $\det\left(A-mI\right)$ up to sign.

> **Theorem (Cayley–Hamilton).** Every square matrix satisfies its own characteristic equation, so $A^{n}$ is a linear combination of $I,A,\dots,A^{n-1}$.

The lemma is the justification for the companion shortcut and for the practice of checking a system answer against the scalar equation it came from.

## 3. Formal Proofs, Derivations, and Methods

### 3.1 Proof of the reduction

Suppose first that $y$ solves $y^{(n)}=F\left(t,y,\dots,y^{(n-1)}\right)$, and define $x_{i}=y^{(i-1)}$. For $i<n$,

$$
x_{i}'=\frac{d}{dt}y^{(i-1)}=y^{(i)}=x_{i+1},
$$

and for $i=n$,

$$
x_{n}'=y^{(n)}=F\left(t,x_{1},\dots,x_{n}\right).
$$

Hence the column $X$ solves the system. Conversely, if $X$ solves the system, put $y=x_{1}$. The first $n-1$ equations give successively $x_{2}=y'$, $x_{3}=y''$, and in general $x_{n}=y^{(n-1)}$, and the last equation then reads $y^{(n)}=F\left(t,y,\dots,y^{(n-1)}\right)$. Each direction is obtained from the other by differentiation alone, so the correspondence is a bijection between solutions.

### 3.2 Proof of the eigen-solution formula

Let $Av=mv$ with $v\neq 0$ and set $X=ve^{mt}$. Then

$$
X'=mve^{mt}=mve^{mt},\qquad AX=\left(Av\right)e^{mt}=mve^{mt},
$$

so $X'=AX$. Linear combinations of solutions are solutions, so $\sum c_{i}v_{i}e^{m_{i}t}$ solves the system. For independence, suppose $\sum\alpha_{i}v_{i}=0$. Applying $A-m_{n}I$ annihilates the last term and multiplies the others by $m_{i}-m_{n}$, none of which is zero, so

$$
\alpha_{1}\left(m_{1}-m_{n}\right)v_{1}+\cdots+\alpha_{n-1}\left(m_{n-1}-m_{n}\right)v_{n-1}=0 .
$$

Repeating with $A-m_{n-1}I$ and so on isolates each coefficient, so all $\alpha_{i}$ vanish. Therefore $V=\left(v_{1}\ \cdots\ v_{n}\right)$ is invertible and $W(0)=\det V\neq 0$. A fundamental set of $n$ solutions of a system of order $n$ spans the solution space, so the combination with $n$ constants is the general solution.

### 3.3 Derivation of the companion determinant identity

The eigen-solution formula rests on knowing that the eigenvalues of the companion matrix are the roots of the auxiliary polynomial, and that identity deserves a proof of its own. Write $D_{n}(m)$ for the determinant of $mI-A$ for the companion matrix of order $n$ with coefficients $a_{1},\dots,a_{n}$,

$$
mI-A=\begin{pmatrix} m & -1 & 0 & \cdots & 0 \\ 0 & m & -1 & \cdots & 0 \\ \vdots & \vdots & \vdots & \ddots & \vdots \\ 0 & 0 & 0 & \cdots & -1 \\ a_{n} & a_{n-1} & a_{n-2} & \cdots & m+a_{1} \end{pmatrix}.
$$

Expand along the first column, which has only two non-zero entries. The entry $m$ in the first row has cofactor $D_{n-1}(m)$, because deleting the first row and first column leaves the companion determinant of order $n-1$ with coefficients $a_{1},\dots,a_{n-1}$. The entry $a_{n}$ in the last row has cofactor $(-1)^{n+1}$ times the determinant of the block that remains after deleting the last row and first column, and that block is lower triangular with every diagonal entry equal to $-1$, so its determinant is $(-1)^{n-1}$. Hence

$$
D_{n}(m)=mD_{n-1}(m)+(-1)^{n+1}(-1)^{n-1}a_{n}=mD_{n-1}(m)+a_{n},
$$

because the product of the two signs is $(-1)^{2n}=1$. The base case is order one, where $mI-A$ is the single entry $m+a_{1}$ and $D_{1}(m)=m+a_{1}$. Induction therefore gives

$$
D_{n}(m)=m^{n}+a_{1}m^{n-1}+a_{2}m^{n-2}+\cdots+a_{n-1}m+a_{n},
$$

and since $\det(A-mI)=(-1)^{n}\det(mI-A)$, the two polynomials differ only by the factor $(-1)^{n}$, which has no roots and therefore leaves the eigenvalues unchanged.

An order-two check confirms the formula. For $y''+5y'+6y=0$ the companion matrix is

$$
A=\begin{pmatrix} 0 & 1 \\ -6 & -5 \end{pmatrix}, \qquad \det\left(A-mI\right)=(-m)(-5-m)+6=m^{2}+5m+6=(m+2)(m+3),
$$

so the eigenvalues $-2$ and $-3$ are exactly the roots of the auxiliary equation, as the theorem asserts.

### 3.4 Derivation of the defective repeated case

Try $X_{2}=\left(vt+u\right)e^{mt}$ with $v$ an eigenvector for $m$. Differentiating,

$$
X_{2}'=ve^{mt}+m\left(vt+u\right)e^{mt},
$$

while

$$
AX_{2}=\left(mvt+Au\right)e^{mt} .
$$

The terms in $t$ agree because $Av=mv$. Comparing the rest and cancelling $e^{mt}$,

$$
v+mu=Au \qquad \Longleftrightarrow \qquad \left(A-mI\right)u=v .
$$

So the trial succeeds exactly when this system is consistent, which it is for a defective eigenvalue of excess one. Independence follows because $u$ cannot be a multiple of $v$: if $u=\kappa v$ then $\left(A-mI\right)u=0$, contradicting $\left(A-mI\right)u=v\neq 0$. Hence the determinant of the columns $v$ and $u$ is non-zero.

### 3.5 Derivation of the real form

Write $m=\alpha+i\beta$ and $v=p+iq$. The equation $Av=mv$ splits into

$$
Ap=\alpha p-\beta q, \qquad Aq=\beta p+\alpha q .
$$

By Euler's formula,

$$
ve^{mt}=\left(p+iq\right)e^{\alpha t}\left(\cos\beta t+i\sin\beta t\right)=e^{\alpha t}\left[\left(p\cos\beta t-q\sin\beta t\right)+i\left(p\sin\beta t+q\cos\beta t\right)\right].
$$

Since $A$ is real, real and imaginary parts of a complex solution are real solutions, which gives $X_{1}$ and $X_{2}$ of Section 2.6. Independence holds because $q$ is not a multiple of $p$: if $q=\lambda p$ then $\beta p=0$, impossible.

### 3.6 Derivation of the non-homogeneous formulas

For the trial $X_{p}=ze^{\mu t}$, substitution gives $\mu ze^{\mu t}=Aze^{\mu t}+we^{\mu t}$, so $\left(A-\mu I\right)z=-w$, which has a unique solution exactly when $\mu$ is not an eigenvalue. For variation of parameters, put $X=\Phi G$ with $\Phi'=A\Phi$; then

$$
X'=\Phi'G+\Phi G'=A\Phi G+\Phi G' ,
$$

and substitution into $X'=AX+B$ leaves $\Phi G'=B$, hence $G'=\Phi^{-1}B$ and $G=\int\Phi^{-1}(s)B(s)\,ds$.

### 3.7 The question patterns

| Pattern | Usual wording | Route | Marks |
| --- | --- | --- | --- |
| A | Reduce the equation to a first-order system and write it in matrix form | definitions and companion row | 3 |
| B | Solve $X'=AX$ for a given matrix | characteristic equation, eigenvectors, case | 8 to 10 |
| C | Show that the solutions are independent and write the general solution | Wronskian at $t=0$, then combination | 4 |
| D | Solve the non-homogeneous system | complementary function plus particular integral | 6 to 8 |
| E | Solve the equation of order $n$ by the matrix method | reduce, solve, read first component | 10 to 12 |
| F | Find the particular integral only | trial and one linear system | 4 |

Pattern E is pattern A followed by pattern B followed by a read-off, and it is the most common long question. Pattern D is the one where candidates run out of time, so the particular integral should be attempted immediately after the eigenvalues are found, while the trial shape is still obvious.

### 3.8 Trap table

| Trap | How it appears in an answer | Correct handling | Cost |
| --- | --- | --- | --- |
| Last row of the companion matrix in the wrong order | coefficients copied in the order written in the equation | write them in reverse, from $a_{n}$ to $a_{1}$ | whole solution wrong |
| Signs not changed | last row $\left(6,5\right)$ for $y''+5y'+6y=0$ | last row is $\left(-6,-5\right)$ | wrong eigenvalues |
| Leading coefficient ignored | equation not divided before the last row is formed | divide every coefficient and the forcing term by $a_{0}$ | wrong eigenvalues |
| Repeated eigenvalue assumed to need a factor of $t$ | $t$ inserted when two eigenvectors exist | check the null space dimension first | redundant wrong term |
| Repeated eigenvalue assumed not to need one | plain exponentials when only one eigenvector exists | compute the null space; dimension one means defective | missing solution, constant count too low |
| Defective matrix treated with $vte^{mt}$ alone | no unknown column $u$ added | the trial must be $\left(vt+u\right)e^{mt}$ | second solution fails |
| Generalised vector chosen as a multiple of $v$ | $u=\kappa v$ giving $\left(A-mI\right)u=0$ | $u$ must satisfy $\left(A-mI\right)u=v$ with the right side non-zero | inconsistent equations |
| Generalised system not checked for consistency | inconsistent pair of equations left unresolved | the second row must be a multiple of the first; recheck $v$ if not | no answer |
| Complex answer left as a final result | exponentials with $i$ in the answer | split into real and imaginary parts | answer not real |
| Wrong pairing of real and imaginary parts | $p\sin\beta t-q\cos\beta t$ written instead of $p\sin\beta t+q\cos\beta t$ | use the derived pair exactly | fails on substitution |
| Only one eigenvalue of a conjugate pair computed | one constant instead of two | count constants against the order | lost constant |
| Imaginary part missing from the exponent | $e^{\alpha t}$ replaced by $e^{\beta t}$ | growth uses $\alpha$, oscillation uses $\beta$ | fails on substitution |
| Particular integral omitted | only the complementary function reported | add one solution of the full system | fails the system |
| Resonant trial used unchanged | $ze^{\mu t}$ with $\mu$ an eigenvalue | multiply the trial by $t$ and add a lower-order vector | no solution for $z$ |
| Wrong number of constants | two constants for a system of order three | one per order | incomplete |
| Eigenvalues never verified | no use of trace and determinant | sum and product checks | undetected arithmetic slip |
| Eigenvectors never verified | no multiplication shown | check $Av=mv$ once per eigenvalue | undetected sign slip |

### 3.9 Presentation discipline

Six habits earn marks that cost nothing. Write the characteristic determinant before expanding it, because the determinant earns a mark on its own. State the eigenvalues with their multiplicities in one line. Show one verification multiplication per eigenvector, since a marker who sees $Av=mv$ checks the rest with confidence. Name the case in words before writing the solution. State the independence check explicitly with the value of the determinant at $t=0$. Finish by substituting the answer into the system, or by differentiating a scalar answer the required number of times, and say in one sentence that the substitution is an identity.

## 4. Representative Worked Examples and Solutions

### 4.1 Problem: a complete third-order question by the matrix method

Reduce $y'''-2y''-y'+2y=0$ to a first-order system, write the matrix form, find the eigenvalues and eigenvectors, show that the solutions are independent, and write the general solution. Hence solve the initial value problem with $y(0)=3$, $y'(0)=2$ and $y''(0)=6$.

### 4.2 Solution: model solution with marking points

Step 1. (2 marks) Solve for the highest derivative and introduce three state variables.

$$
y'''=2y''+y'-2y, \qquad x_{1}=y, \quad x_{2}=y', \quad x_{3}=y'' .
$$

Step 2. (1 mark) Write the three first-order equations explicitly.

$$
x_{1}'=x_{2}, \qquad x_{2}'=x_{3}, \qquad x_{3}'=-2x_{1}+x_{2}+2x_{3} .
$$

Step 3. (1 mark) Assemble the matrix form $X'=AX$, with the unknowns ordered $x_{1},x_{2},x_{3}$.

$$
A=\begin{pmatrix} 0 & 1 & 0 \\ 0 & 0 & 1 \\ -2 & 1 & 2 \end{pmatrix}
$$

Step 4. (1 mark) Form the characteristic determinant.

$$
\det\left(A-mI\right)=\begin{vmatrix} -m & 1 & 0 \\ 0 & -m & 1 \\ -2 & 1 & 2-m \end{vmatrix}
$$

Step 5. (1 mark) Expand along the first row.

$$
\det\left(A-mI\right)=-m\left[m(2-m)-1\right]-1\left[0\cdot(2-m)-1\cdot(-2)\right]
$$

Step 6. (1 mark) Simplify.

$$
\det\left(A-mI\right)=-m\left(2m-m^{2}-1\right)-2=m^{3}-2m^{2}-m+2
$$

Step 7. (2 marks) Factor and state the eigenvalues. Grouping the terms gives

$$
m^{3}-2m^{2}-m+2=m^{2}(m-2)-(m-2)=(m-2)\left(m^{2}-1\right)=(m-2)(m-1)(m+1),
$$

so $m_{1}=1$, $m_{2}=2$ and $m_{3}=-1$, all simple. The trace is $2$ and $1+2-1=2$; the determinant is $-2$ and $1\cdot 2\cdot(-1)=-2$.

Step 8. (3 marks) Obtain the eigenvectors from the companion shortcut, taking the column with entries one, $m$ and $m^{2}$.

$$
v_{1}=\begin{pmatrix} 1 \\ 1 \\ 1 \end{pmatrix}, \qquad v_{2}=\begin{pmatrix} 1 \\ 2 \\ 4 \end{pmatrix}, \qquad v_{3}=\begin{pmatrix} 1 \\ -1 \\ 1 \end{pmatrix}
$$

Step 9. (1 mark) Verify the pair for $m=2$ by direct multiplication.

$$
Av_{2}=\begin{pmatrix} 0 & 1 & 0 \\ 0 & 0 & 1 \\ -2 & 1 & 2 \end{pmatrix}\begin{pmatrix} 1 \\ 2 \\ 4 \end{pmatrix}=\begin{pmatrix} 2 \\ 4 \\ -2+2+8 \end{pmatrix}=\begin{pmatrix} 2 \\ 4 \\ 8 \end{pmatrix}=2v_{2}
$$

Step 10. (1 mark) Verify the pair for $m=-1$.

$$
Av_{3}=\begin{pmatrix} 0 & 1 & 0 \\ 0 & 0 & 1 \\ -2 & 1 & 2 \end{pmatrix}\begin{pmatrix} 1 \\ -1 \\ 1 \end{pmatrix}=\begin{pmatrix} -1 \\ 1 \\ -2-1+2 \end{pmatrix}=\begin{pmatrix} -1 \\ 1 \\ -1 \end{pmatrix}=-1\cdot v_{3}
$$

Step 11. (1 mark) Write the general solution of the system.

$$
X=c_{1}\begin{pmatrix} 1 \\ 1 \\ 1 \end{pmatrix}e^{t}+c_{2}\begin{pmatrix} 1 \\ 2 \\ 4 \end{pmatrix}e^{2t}+c_{3}\begin{pmatrix} 1 \\ -1 \\ 1 \end{pmatrix}e^{-t}
$$

Step 12. (1 mark) Show independence using the Wronskian at $t=0$, where every exponential equals one.

$$
W(0)=\begin{vmatrix} 1 & 1 & 1 \\ 1 & 2 & -1 \\ 1 & 4 & 1 \end{vmatrix}=1\left(2+4\right)-1\left(1+1\right)+1\left(4-2\right)=6
$$

Since $6\neq 0$ the three solutions are independent, so the expression with three constants is the general solution.

Step 13. (1 mark) Read off the scalar answer, which is the first component.

$$
y=c_{1}e^{t}+c_{2}e^{2t}+c_{3}e^{-t}
$$

Step 14. (2 marks) Impose the initial conditions. At $t=0$ the vector of initial values is the column with entries $3$, $2$ and $6$, and the three components give

$$
c_{1}+c_{2}+c_{3}=3, \qquad c_{1}+2c_{2}-c_{3}=2, \qquad c_{1}+4c_{2}+c_{3}=6 .
$$

Step 15. (2 marks) Solve the linear system. Subtracting the first equation from the third gives $3c_{2}=3$, so $c_{2}=1$. Subtracting the first from the second gives $c_{2}-2c_{3}=-1$, so $2c_{3}=2$ and $c_{3}=1$. The first equation then gives $c_{1}=1$.

Step 16. (2 marks) State and verify the particular solution.

$$
y=e^{t}+e^{2t}+e^{-t}
$$

At $t=0$ this gives $1+1+1=3$. Its derivatives are $y'=e^{t}+2e^{2t}-e^{-t}$ and $y''=e^{t}+4e^{2t}+e^{-t}$, giving $y'(0)=1+2-1=2$ and $y''(0)=1+4+1=6$. Substituting into the equation gives

$$
y'''-2y''-y'+2y=\left(1-2-1+2\right)e^{t}+\left(8-8-2+2\right)e^{2t}+\left(-1-2+1+2\right)e^{-t}=0,
$$

so the answer is confirmed.

### 4.3 Problem: a defective repeated eigenvalue with an initial condition

Solve $X'=AX$ for the matrix with first row $1$ and $1$, and second row $-1$ and $3$. Verify the solution, and then satisfy $X(0)$ equal to the column with entries $1$ and $2$.

### 4.4 Solution: model solution with marking points

Step 1. (1 mark) Form the characteristic determinant.

$$
\det\left(A-mI\right)=\begin{vmatrix} 1-m & 1 \\ -1 & 3-m \end{vmatrix}=(1-m)(3-m)+1
$$

Step 2. (2 marks) Simplify and solve.

$$
(1-m)(3-m)+1=m^{2}-4m+4=(m-2)^{2}=0 \qquad \Longrightarrow \qquad m=2,
$$

a double eigenvalue. The trace is $4=2+2$ and the determinant is $4=2\cdot 2$, so the root is consistent.

Step 3. (2 marks) Compute the null space of $A-2I$.

$$
A-2I=\begin{pmatrix} -1 & 1 \\ -1 & 1 \end{pmatrix}, \qquad \left(A-2I\right)\begin{pmatrix} a \\ b \end{pmatrix}=0 \quad \Longrightarrow \quad -a+b=0 .
$$

The two rows are identical, so the null space is one-dimensional and the matrix is defective with geometric multiplicity one against algebraic multiplicity two.

Step 4. (1 mark) Record and verify the eigenvector.

$$
v=\begin{pmatrix} 1 \\ 1 \end{pmatrix}, \qquad Av=\begin{pmatrix} 1 & 1 \\ -1 & 3 \end{pmatrix}\begin{pmatrix} 1 \\ 1 \end{pmatrix}=\begin{pmatrix} 2 \\ 2 \end{pmatrix}=2v .
$$

Step 5. (2 marks) Set up the generalised eigenvector equation.

$$
\left(A-2I\right)u=v \quad \Longrightarrow \quad \begin{pmatrix} -1 & 1 \\ -1 & 1 \end{pmatrix}\begin{pmatrix} p \\ q \end{pmatrix}=\begin{pmatrix} 1 \\ 1 \end{pmatrix} \quad \Longrightarrow \quad -p+q=1 .
$$

The two equations are identical, so the system is consistent, as required for a defective eigenvalue of excess one.

Step 6. (1 mark) Choose the simplest solution and verify it.

$$
u=\begin{pmatrix} 0 \\ 1 \end{pmatrix}, \qquad \left(A-2I\right)u=\begin{pmatrix} -1 & 1 \\ -1 & 1 \end{pmatrix}\begin{pmatrix} 0 \\ 1 \end{pmatrix}=\begin{pmatrix} 1 \\ 1 \end{pmatrix}=v .
$$

Step 7. (2 marks) Write the general solution.

$$
X=c_{1}\begin{pmatrix} 1 \\ 1 \end{pmatrix}e^{2t}+c_{2}\left[\begin{pmatrix} 1 \\ 1 \end{pmatrix}t+\begin{pmatrix} 0 \\ 1 \end{pmatrix}\right]e^{2t}
$$

Step 8. (2 marks) Verify the second solution by substitution. Its components are $x_{1}=te^{2t}$ and $x_{2}=(t+1)e^{2t}$, with derivatives

$$
x_{1}'=(1+2t)e^{2t}, \qquad x_{2}'=(3+2t)e^{2t} .
$$

The first equation requires $x_{1}'=x_{1}+x_{2}$, and the right side is $te^{2t}+(t+1)e^{2t}=(2t+1)e^{2t}$, which agrees. The second requires $x_{2}'=-x_{1}+3x_{2}$, and the right side is $-te^{2t}+3(t+1)e^{2t}=(2t+3)e^{2t}$, which agrees.

Step 9. (1 mark) Apply the initial condition at $t=0$, where the general solution becomes $c_{1}v+c_{2}u$.

$$
c_{1}\begin{pmatrix} 1 \\ 1 \end{pmatrix}+c_{2}\begin{pmatrix} 0 \\ 1 \end{pmatrix}=\begin{pmatrix} 1 \\ 2 \end{pmatrix} \quad \Longrightarrow \quad c_{1}=1, \quad c_{1}+c_{2}=2 .
$$

Step 10. (1 mark) Hence $c_{1}=1$ and $c_{2}=1$, and the solution is

$$
x_{1}=(1+t)e^{2t}, \qquad x_{2}=(2+t)e^{2t} .
$$

Step 11. (1 mark) Verify the initial condition and one equation: at $t=0$ the components are $1$ and $2$ as required, and $x_{1}'=(3+2t)e^{2t}$ while $x_{1}+x_{2}=(1+t+2+t)e^{2t}=(3+2t)e^{2t}$.

### 4.5 Problem: a complex conjugate pair converted to real form

Solve $X'=AX$ for the matrix with first row $2$ and $-5$, and second row $2$ and $-4$. Express the answer with real functions only, and verify one component.

### 4.6 Solution: model solution with marking points

Step 1. (1 mark) Form the characteristic determinant.

$$
\det\left(A-mI\right)=\begin{vmatrix} 2-m & -5 \\ 2 & -4-m \end{vmatrix}=(2-m)(-4-m)+10
$$

Step 2. (2 marks) Expand and solve.

$$
(2-m)(-4-m)+10=m^{2}+2m+2=0 \qquad \Longrightarrow \qquad m=-1\pm i,
$$

so $\alpha=-1$ and $\beta=1$. The trace is $-2$, the sum of the roots, and the determinant is $2$, their product.

Step 3. (2 marks) Find an eigenvector for $m=-1+i$.

$$
\left(A-(-1+i)I\right)=\begin{pmatrix} 3-i & -5 \\ 2 & -3-i \end{pmatrix}, \qquad (3-i)a-5b=0 .
$$

Choosing $a=5$ gives $b=3-i$, so $v=(5,3-i)$.

Step 4. (2 marks) Verify the pair, including the second row.

$$
Av=\begin{pmatrix} 2 & -5 \\ 2 & -4 \end{pmatrix}\begin{pmatrix} 5 \\ 3-i \end{pmatrix}=\begin{pmatrix} -5+5i \\ -2+4i \end{pmatrix},
$$

and

$$
(-1+i)v=\begin{pmatrix} -5+5i \\ (-1+i)(3-i) \end{pmatrix}=\begin{pmatrix} -5+5i \\ -2+4i \end{pmatrix},
$$

so the two agree. Note that $(-1+i)(3-i)=-3+i+3i+1=-2+4i$.

Step 5. (1 mark) Split the eigenvector into real and imaginary parts.

$$
p=\begin{pmatrix} 5 \\ 3 \end{pmatrix}, \qquad q=\begin{pmatrix} 0 \\ -1 \end{pmatrix}
$$

Step 6. (3 marks) Apply the real-form theorem with $\alpha=-1$ and $\beta=1$.

$$
X=e^{-t}\left\{c_{1}\left[\begin{pmatrix} 5 \\ 3 \end{pmatrix}\cos t-\begin{pmatrix} 0 \\ -1 \end{pmatrix}\sin t\right]+c_{2}\left[\begin{pmatrix} 5 \\ 3 \end{pmatrix}\sin t+\begin{pmatrix} 0 \\ -1 \end{pmatrix}\cos t\right]\right\}
$$

Step 7. (1 mark) Simplify the two real solutions.

$$
X_{1}=e^{-t}\begin{pmatrix} 5\cos t \\ 3\cos t+\sin t \end{pmatrix}, \qquad X_{2}=e^{-t}\begin{pmatrix} 5\sin t \\ 3\sin t-\cos t \end{pmatrix}
$$

Step 8. (1 mark) Write the components.

$$
x_{1}=e^{-t}\left(5c_{1}\cos t+5c_{2}\sin t\right), \qquad x_{2}=e^{-t}\left[\left(3c_{1}-c_{2}\right)\cos t+\left(c_{1}+3c_{2}\right)\sin t\right]
$$

Step 9. (2 marks) Verify the first component. Differentiating it gives

$$
x_{1}'=e^{-t}\left[\left(-5c_{1}+5c_{2}\right)\cos t+\left(-5c_{1}-5c_{2}\right)\sin t\right],
$$

and the right side $2x_{1}-5x_{2}$ gives

$$
e^{-t}\left[\left(10c_{1}-15c_{1}+5c_{2}\right)\cos t+\left(10c_{2}-5c_{1}-15c_{2}\right)\sin t\right],
$$

which is identical. The answer is therefore a genuine solution and not merely a formal conjugate.

Step 10. (1 mark) Interpret. The factor $e^{-t}$ shrinks the solution, so the components spiral inwards towards the origin while rotating once every $2\pi$ units of time; the negative real part produces the shrinking and the unit imaginary part produces the rotation rate.

### 4.7 Problem: a non-homogeneous system

Solve

$$
X'=AX+B, \qquad A=\begin{pmatrix} 2 & 1 \\ 1 & 2 \end{pmatrix}, \qquad B=\begin{pmatrix} 2e^{2t} \\ 0 \end{pmatrix} .
$$

### 4.8 Solution: model solution with marking points

Step 1. (1 mark) Form the characteristic determinant.

$$
\det\left(A-mI\right)=\begin{vmatrix} 2-m & 1 \\ 1 & 2-m \end{vmatrix}=(2-m)^{2}-1
$$

Step 2. (2 marks) Expand, factor and state the eigenvalues.

$$
(2-m)^{2}-1=m^{2}-4m+3=(m-3)(m-1) \qquad \Longrightarrow \qquad m_{1}=3, \quad m_{2}=1 .
$$

The trace is $4=3+1$ and the determinant is $3=3\cdot 1$.

Step 3. (2 marks) Find and verify the eigenvectors.

$$
\left(A-3I\right)=\begin{pmatrix} -1 & 1 \\ 1 & -1 \end{pmatrix}, \quad v_{1}=\begin{pmatrix} 1 \\ 1 \end{pmatrix}, \quad Av_{1}=\begin{pmatrix} 3 \\ 3 \end{pmatrix}=3v_{1},
$$

$$
\left(A-I\right)=\begin{pmatrix} 1 & 1 \\ 1 & 1 \end{pmatrix}, \quad v_{2}=\begin{pmatrix} 1 \\ -1 \end{pmatrix}, \quad Av_{2}=\begin{pmatrix} 1 \\ -1 \end{pmatrix}=1\cdot v_{2} .
$$

Step 4. (1 mark) Write the complementary function.

$$
X_{c}=c_{1}\begin{pmatrix} 1 \\ 1 \end{pmatrix}e^{3t}+c_{2}\begin{pmatrix} 1 \\ -1 \end{pmatrix}e^{t}
$$

Step 5. (1 mark) Select the trial. The forcing is a constant column times $e^{2t}$, and $2$ is not an eigenvalue, so the trial $X_{p}=ze^{2t}$ is appropriate with $z$ a constant column.

Step 6. (2 marks) Substitute the trial into the system and cancel the exponential.

$$
2ze^{2t}=Aze^{2t}+\begin{pmatrix} 2 \\ 0 \end{pmatrix}e^{2t} \quad \Longrightarrow \quad \left(A-2I\right)z=-\begin{pmatrix} 2 \\ 0 \end{pmatrix}
$$

Step 7. (2 marks) Solve the resulting linear system, in which $A-2I$ is invertible because $2$ is not an eigenvalue, so the solution is unique.

$$
\begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}\begin{pmatrix} a \\ b \end{pmatrix}=\begin{pmatrix} -2 \\ 0 \end{pmatrix} \quad \Longrightarrow \quad b=-2, \quad a=0 .
$$

Step 8. (1 mark) Record the particular integral.

$$
X_{p}=\begin{pmatrix} 0 \\ -2 \end{pmatrix}e^{2t}
$$

Step 9. (1 mark) Verify it directly.

$$
X_{p}'=\begin{pmatrix} 0 \\ -4 \end{pmatrix}e^{2t}, \qquad AX_{p}+B=\begin{pmatrix} -2+2 \\ -4+0 \end{pmatrix}e^{2t}=\begin{pmatrix} 0 \\ -4 \end{pmatrix}e^{2t} .
$$

Step 10. (2 marks) Write the general solution and check the first equation in full.

$$
X=c_{1}\begin{pmatrix} 1 \\ 1 \end{pmatrix}e^{3t}+c_{2}\begin{pmatrix} 1 \\ -1 \end{pmatrix}e^{t}+\begin{pmatrix} 0 \\ -2 \end{pmatrix}e^{2t}
$$

The components are $x_{1}=c_{1}e^{3t}+c_{2}e^{t}$ and $x_{2}=c_{1}e^{3t}-c_{2}e^{t}-2e^{2t}$. The derivative of $x_{1}$ is $3c_{1}e^{3t}+c_{2}e^{t}$, and $2x_{1}+x_{2}+2e^{2t}$ equals $2c_{1}e^{3t}+2c_{2}e^{t}+c_{1}e^{3t}-c_{2}e^{t}-2e^{2t}+2e^{2t}$, which is the same. The second equation holds by the same computation on $x_{2}'$ against $x_{1}+2x_{2}$.

Step 11. (1 mark) Note the count: two constants for a system of order two, and one particular integral because the system is non-homogeneous.

### 4.9 Problem: reduction of a fourth-order equation, with a repeated-eigenvalue contrast

Reduce $y^{(4)}-5y''+4y=0$ to a first-order system, write the matrix form, state the characteristic equation, and write the general solution. Then state what changes if the matrix has a double eigenvalue with only one eigenvector.

### 4.10 Solution: model solution with marking points

Step 1. (2 marks) Introduce four state variables and write the equations.

$$
x_{1}=y, \quad x_{2}=y', \quad x_{3}=y'', \quad x_{4}=y''', \qquad x_{1}'=x_{2}, \quad x_{2}'=x_{3}, \quad x_{3}'=x_{4}, \quad x_{4}'=-4x_{1}+5x_{3} .
$$

The last equation follows from $y^{(4)}=5y''-4y$, and the absent terms for $y'$ and $y'''$ appear as the zeros in the last row.

Step 2. (1 mark) Write the matrix form.

$$
A=\begin{pmatrix} 0 & 1 & 0 & 0 \\ 0 & 0 & 1 & 0 \\ 0 & 0 & 0 & 1 \\ -4 & 0 & 5 & 0 \end{pmatrix}
$$

Step 3. (1 mark) State the characteristic equation from the companion rule.

$$
m^{4}+a_{1}m^{3}+a_{2}m^{2}+a_{3}m+a_{4}=m^{4}-5m^{2}+4=0
$$

Step 4. (2 marks) Factor and state the eigenvalues.

$$
m^{4}-5m^{2}+4=\left(m^{2}-1\right)\left(m^{2}-4\right)=(m-1)(m+1)(m-2)(m+2),
$$

so the eigenvalues are $1$, $-1$, $2$ and $-2$, all simple. Their sum is $0$, which equals the trace, and their product is $4$, which equals the determinant.

Step 5. (2 marks) Write the eigenvectors by the companion shortcut, with entries one, $m$, $m^{2}$ and $m^{3}$.

$$
v_{1}=\begin{pmatrix} 1 \\ 1 \\ 1 \\ 1 \end{pmatrix}, \quad v_{2}=\begin{pmatrix} 1 \\ -1 \\ 1 \\ -1 \end{pmatrix}, \quad v_{3}=\begin{pmatrix} 1 \\ 2 \\ 4 \\ 8 \end{pmatrix}, \quad v_{4}=\begin{pmatrix} 1 \\ -2 \\ 4 \\ -8 \end{pmatrix}
$$

Step 6. (1 mark) Verify one pair, for $m=2$.

$$
Av_{3}=\begin{pmatrix} 0 & 1 & 0 & 0 \\ 0 & 0 & 1 & 0 \\ 0 & 0 & 0 & 1 \\ -4 & 0 & 5 & 0 \end{pmatrix}\begin{pmatrix} 1 \\ 2 \\ 4 \\ 8 \end{pmatrix}=\begin{pmatrix} 2 \\ 4 \\ 8 \\ -4+20 \end{pmatrix}=\begin{pmatrix} 2 \\ 4 \\ 8 \\ 16 \end{pmatrix}=2v_{3}
$$

Step 7. (2 marks) Write the general solution and the scalar answer.

$$
y=c_{1}e^{t}+c_{2}e^{-t}+c_{3}e^{2t}+c_{4}e^{-2t}
$$

The four constants match the order four, as required.

Step 8. (2 marks) Verify one term in the scalar equation. For $y=e^{2t}$ the derivatives multiply by $2$, $4$, $8$ and $16$, so

$$
y^{(4)}-5y''+4y=\left(16-20+4\right)e^{2t}=0 .
$$

The term works; the same computation with $m$ in place of $2$ gives $m^{4}-5m^{2}+4$, which vanishes at each of the four eigenvalues, so all four terms work.

Step 9. (2 marks) State the contrast for a defective double eigenvalue. If a double eigenvalue $m$ has only one independent eigenvector $v$, the two solutions are $ve^{mt}$ and $\left(vt+u\right)e^{mt}$ with $u$ found from $\left(A-mI\right)u=v$; the count of constants is unchanged, but one of them multiplies a solution containing the factor $t$, and no combination of exponentials alone can replace it.

### 4.11 Problem: three equal eigenvalues but only one missing direction

Solve $X'=AX$ for the matrix with rows $(2,1,0)$, $(0,2,0)$ and $(0,0,2)$.

### 4.12 Solution: count the null space before choosing the shape

Step 1. (1 mark) Form the characteristic determinant. The matrix is upper triangular, so its eigenvalues are its diagonal entries.

$$
\det\left(A-mI\right)=(2-m)^{3} \qquad \Longrightarrow \qquad m=2 \text{ with algebraic multiplicity } 3 .
$$

Step 2. (2 marks) Compute the null space of $A-2I$ and its dimension.

$$
A-2I=\begin{pmatrix} 0 & 1 & 0 \\ 0 & 0 & 0 \\ 0 & 0 & 0 \end{pmatrix}, \qquad \left(A-2I\right)\begin{pmatrix} a \\ b \\ c \end{pmatrix}=0 \quad \Longrightarrow \quad b=0 .
$$

The first and third entries of the column are free, so the null space is two-dimensional, spanned by the columns with entries $(1,0,0)$ and $(0,0,1)$. The geometric multiplicity is two against an algebraic multiplicity of three, so exactly one direction is missing and exactly one generalised vector is needed.

Step 3. (1 mark) Record and verify the two eigenvectors.

$$
Av_{1}=\begin{pmatrix} 2 & 1 & 0 \\ 0 & 2 & 0 \\ 0 & 0 & 2 \end{pmatrix}\begin{pmatrix} 1 \\ 0 \\ 0 \end{pmatrix}=\begin{pmatrix} 2 \\ 0 \\ 0 \end{pmatrix}=2v_{1}, \qquad Av_{3}=\begin{pmatrix} 0 \\ 0 \\ 2 \end{pmatrix}=2v_{3} .
$$

Step 4. (2 marks) Find the generalised vector from the missing direction, solving $\left(A-2I\right)u=v_{1}$.

$$
\begin{pmatrix} 0 & 1 & 0 \\ 0 & 0 & 0 \\ 0 & 0 & 0 \end{pmatrix}\begin{pmatrix} p \\ q \\ r \end{pmatrix}=\begin{pmatrix} 1 \\ 0 \\ 0 \end{pmatrix} \quad \Longrightarrow \quad q=1,
$$

so the simplest choice is $u$ equal to the column with entries $(0,1,0)$.

Step 5. (1 mark) Verify it: $(A-2I)u$ is the column with entries $(1,0,0)$, which is $v_{1}$.

Step 6. (2 marks) Assemble the general solution, with one factor of $t$ and no more.

$$
X=c_{1}\begin{pmatrix} 1 \\ 0 \\ 0 \end{pmatrix}e^{2t}+c_{3}\left[\begin{pmatrix} 1 \\ 0 \\ 0 \end{pmatrix}t+\begin{pmatrix} 0 \\ 1 \\ 0 \end{pmatrix}\right]e^{2t}+c_{2}\begin{pmatrix} 0 \\ 0 \\ 1 \end{pmatrix}e^{2t}
$$

Step 7. (1 mark) Write the components.

$$
x_{1}=\left(c_{1}+c_{3}t\right)e^{2t}, \qquad x_{2}=c_{3}e^{2t}, \qquad x_{3}=c_{2}e^{2t}
$$

Step 8. (2 marks) Verify the solution containing $t$. Its components are $te^{2t}$, $e^{2t}$ and $0$, with derivatives $(1+2t)e^{2t}$, $2e^{2t}$ and $0$. The right-hand sides are $2te^{2t}+e^{2t}$ for the first equation, $2e^{2t}$ for the second, and $2\cdot 0$ for the third, and all three agree.

Step 9. (1 mark) Note the trap. A triple eigenvalue does not call for two factors of $t$; the number of factors equals the shortfall between the algebraic and geometric multiplicities, which here is one. Three constants appear, as the order three requires.

## 5. Mathematical Extensions, Limits, and Common Errors

### 5.1 The three traps that cost the most marks

The defective matrix is the first. Candidates who see a double root and immediately write down $ve^{mt}$ and $vte^{mt}$ lose the special term $ue^{mt}$, and their second solution fails on substitution. The diagnosis is one line of work: compute the null space of $A-mI$ and count its dimension. A dimension equal to the multiplicity means plain exponentials; a smaller dimension means the generalised vector is needed, and the vector must be found from $\left(A-mI\right)u=v$ with the non-zero right-hand side, never from the homogeneous equation.

The generalised vector is the second. Two errors occur: choosing $u$ as a multiple of $v$, which makes the left side zero and cannot equal $v$; and choosing $u$ so that the equations contradict one another, which signals that the eigenvector $v$ is wrong. The consistency of the two rows is a free check, since for a defective eigenvalue of excess one the second row is always a multiple of the first.

The complex conversion is the third. The safe procedure is to write the complex eigenvector as $p+iq$ with real entries, write the eigenvalue as $\alpha+i\beta$, and copy the two real solutions from the theorem without rearranging anything. Rearranging by hand is where the sign errors enter: the term $-q\sin\beta t$ belongs to the first solution, and $+q\cos\beta t$ belongs to the second, and swapping them produces a vector that fails the system. Two further slips belong here: leaving $i$ in the final answer, and computing only one eigenvalue of the pair so that the answer carries one constant instead of two.

### 5.2 Revision checklist

- Can I write the reduction for an equation of any order without hesitating over the indices, and state the number of equations before writing them?
- Can I form the companion matrix, including the reversal and the negation of the coefficients, and handle a leading coefficient that is not one?
- Can I expand a determinant of order two and three by cofactors without a sign error, and of order four along a row with zeros?
- Can I factor a cubic by testing small integer roots, and a quartic by grouping into two quadratics?
- Can I find an eigenvector and show the verification multiplication in two lines?
- Can I count the null space dimension to decide between the two repeated cases?
- Can I solve $\left(A-mI\right)u=v$, choose the simplest solution, and check it?
- Can I convert a complex pair to real form using the theorem, with $\alpha$ in the exponent and $\beta$ inside the cosine and sine?
- Can I justify independence with a Wronskian evaluated at $t=0$ and state the value?
- Can I choose a trial for a non-homogeneous system, detect resonance, and solve the resulting linear system?
- Can I read the scalar answer off the first component and verify it in the original equation?
- Can I count constants and compare with the order every time?

### 5.3 Time strategy

For a long question worth twelve marks, spend one minute reading and classifying, then four minutes on the reduction and matrix form, four on the characteristic equation and eigenvalues, five on the eigenvectors with their verifications, three on independence and the general solution, and three on any initial condition and the final check. The characteristic equation should never take more than two minutes, because a cubic that does not factor quickly has a wrong determinant, and re-expanding is faster than guessing roots.

Two disciplines save time. First, verify each eigenvector immediately after finding it, since discovering a sign error five steps later costs more than the verification. Second, write the general solution as soon as the eigenvectors are known and before attempting any initial condition or particular integral, so that partial credit is secured.

For a short question worth four marks, such as finding a particular integral only, skip the complementary function entirely and go straight to the trial, but still state why the trial shape is admissible, since that statement usually carries a mark.

### 5.4 Extensions that appear in harder papers

Three extensions are worth knowing. The first is the matrix exponential, which writes the solution of $X'=AX$ with $X(0)=X_{0}$ as $X=e^{At}X_{0}$, where the series is

$$
e^{At}=I+At+\frac{A^{2}t^{2}}{2!}+\frac{A^{3}t^{3}}{3!}+\cdots .
$$

For a defective matrix this series reproduces exactly the factor $t$ that the generalised eigenvector produced, which is why the device is not an arbitrary trick.

The second is the Jordan chain, which extends the generalised eigenvector construction to eigenvalues whose excess is greater than one: one solves $\left(A-mI\right)u_{1}=0$, then $\left(A-mI\right)u_{2}=u_{1}$, then $\left(A-mI\right)u_{3}=u_{2}$, and each successive vector contributes one more power of $t$.

The third is the limitation of the whole method. It requires a constant coefficient matrix. If the matrix depends on $t$, the eigenvectors rotate and the exponential combination is not a solution, so a fundamental matrix must be obtained by another route. The reduction, by contrast, survives both variable coefficients and non-linearity, because it uses only differentiation; what fails outside the constant linear case is the eigenvalue step.

### 5.5 Consolidated revision summary

The topic is a single procedure with three branches. Reduce by naming derivatives, one name per order, and check the count of equations against the order. Assemble the matrix by rows in a fixed order, with the companion row reversed and negated. Form and factor the characteristic equation exactly, and check the roots against the trace and the determinant. Find eigenvectors, verify each by multiplication, and count the null space dimension whenever an eigenvalue repeats. Then branch: distinct real eigenvalues give exponentials; a repeated eigenvalue with too few eigenvectors gives one solution with a factor of $t$ and a generalised vector; a complex pair gives cosine and sine multiplied by an exponential whose growth rate is the real part. Add a particular integral when the system is non-homogeneous, choosing the trial by the shape of the forcing and multiplying by $t$ at resonance. Finish by counting the constants, by showing independence at $t=0$, and by substituting the answer back into the system, which is the only step that proves the work rather than merely exhibiting it.
