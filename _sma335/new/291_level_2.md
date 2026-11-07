## 1. Foundational Concepts, Definitions, and Axioms

### 1.1 The class of equations

The topic concerns linear ordinary differential equations with constant coefficients, written in operator form as

$$
f(D)y=Q,
$$

where $Q=Q(x)$ is a prescribed function called the non-homogeneous term or the forcing term, and

$$
f(D)=a_{0}D^{m}+a_{1}D^{m-1}+\cdots+a_{m-1}D+a_{m}
$$

is a polynomial of degree $m$ in the differentiation operator $D$, with constant real coefficients and $a_{0}\neq 0$. The symbol $D$ acts on functions of $x$ by $Dy=\frac{dy}{dx}$, and powers of $D$ mean repeated differentiation. Because the coefficients are constant, $D$ may be manipulated algebraically inside $f(D)$ exactly as a symbol, and the polynomial $f$ may be factored, expanded, differentiated with respect to $D$, and evaluated at numbers.

Throughout, the constant term $a_{m}$ is written $f(0)$, since setting $D=0$ in the polynomial leaves precisely $a_{m}$. This number governs the whole of the power rule, and the roots of $f$ govern the exponential and wave rules, so the coefficients must never be used before the polynomial has been collected in this standard form.

### 1.2 The complementary function

> **Definition (Homogeneous equation, nullspace).** The homogeneous equation associated with $f(D)y=Q$ is $f(D)y=0$. Its solution set is a vector space of dimension $m$, called the nullspace or kernel of $f(D)$, written $\ker f(D)$.

> **Definition (Complementary function).** A complementary function is a general element of $\ker f(D)$, that is, a formula containing $m$ independent arbitrary constants from which every solution of the homogeneous equation is obtained.

The dimension statement is the fundamental theorem for constant-coefficient equations: if the polynomial factors as

$$
f(D)=a_{0}\left(D-m_{1}\right)^{r_{1}}\left(D-m_{2}\right)^{r_{2}}\cdots\left(D-m_{s}\right)^{r_{s}},
$$

with distinct roots $m_{1},\dots,m_{s}$ and multiplicities summing to $m$, then each real root $m$ of multiplicity $r$ contributes $e^{mx},xe^{mx},\dots,x^{r-1}e^{mx}$, and each conjugate pair $\alpha\pm i\beta$ of multiplicity $r$ contributes $e^{\alpha x}\cos\beta x,e^{\alpha x}\sin\beta x$ and their multiples by $x$ up to $x^{r-1}$. The count of independent functions is exactly $m$.

### 1.3 The particular integral

> **Definition (Particular integral).** A particular integral of $f(D)y=Q$ is any single function $y_{p}$, free of arbitrary constants, that satisfies the equation identically.

> **Theorem (Structure of the general solution).** Every solution of $f(D)y=Q$ has the form $y=y_{c}+y_{p}$, where $y_{c}$ is a complementary function and $y_{p}$ is a particular integral; conversely every function of that form is a solution.

The proof is one line and is given in Section 3. Two consequences are used constantly. First, a particular integral is never unique: if $y_{p}$ and $\tilde y_{p}$ both work, then their difference satisfies the homogeneous equation, so the two differ by an element of the nullspace. Any particular integral is therefore acceptable, and a printed answer that differs from a student's by a complementary function is still correct. Second, the particular integral carries no arbitrary constants, so the count of constants in a finished answer must come entirely from the complementary function, and that count must equal the order.

### 1.4 The inverse operator

The particular integral is written symbolically as

$$
y_{p}=\frac{Q}{f(D)} .
$$

> **Definition (Inverse operator).** For a function $Q$ and a polynomial $f$, the symbol $\frac{1}{f(D)}Q$ denotes some function $y$ with $f(D)y=Q$; that is, $\frac{1}{f(D)}$ denotes a right inverse of the operator $f(D)$ acting on the class of functions under consideration.

The definition is honest about the ambiguity. A right inverse is determined only modulo $\ker f(D)$, since adding any element of the nullspace leaves $f(D)y$ unchanged. Every rule established below produces one such right inverse, and each rule is validated the same way: by applying $f(D)$ to the claimed answer and recovering $Q$.

Three properties follow immediately from linearity of $D$ and are used without comment. If $\frac{Q_{1}}{f(D)}=y_{1}$ and $\frac{Q_{2}}{f(D)}=y_{2}$, then $\frac{Q_{1}+Q_{2}}{f(D)}=y_{1}+y_{2}$, so a forcing term that is a finite sum is handled term by term. If $c$ is a constant, then $\frac{cQ}{f(D)}=c\,y$. And if $g(D)$ is another polynomial, the order of two inverse operators may be interchanged, since $f(D)g(D)=g(D)f(D)$ for constant coefficients.

### 1.5 The five admissible forcing families

Only five shapes of $Q$ are treated by the short methods, and each is closed under the action of $f(D)$ in a precise sense.

The exponential family $e^{ax}$ is mapped to itself, scaled by $f(a)$, because differentiating an exponential returns a multiple of the same exponential. The trigonometric family spanned by $\sin(ax+b)$ and $\cos(ax+b)$ is mapped into itself, because two differentiations return a multiple of the same wave; this is the reason the second derivative may be replaced by $-a^{2}$. The polynomial family of degree at most $n$ is mapped into itself, because differentiation lowers degree, so the machine can never produce a power higher than the input. The family $e^{ax}u$ is mapped into $e^{ax}$ times the image of $u$ under a shifted polynomial, which reduces the problem to whatever $u$ is. The family $xu$ is mapped into $x$ times the image of $u$ plus a correction, which again reduces the problem to $u$.

Because each family is mapped into itself, the answer can be sought inside the family, and the search collapses to determining finitely many coefficients. This is the structural reason the short methods exist, and it is also the reason they fail outside these families: a forcing term such as $\ln x$ or $\frac{1}{x}$ is not carried into a finite-dimensional family, so no amount of algebra will produce a reply of the same shape.

### 1.6 Resonance

> **Definition (Resonance).** The forcing term $Q$ is said to be resonant with $f(D)$ when $Q$ belongs to $\ker f(D)$, that is, when $Q$ itself satisfies the homogeneous equation.

For $Q=e^{ax}$ this happens exactly when $f(a)=0$; for $Q=\sin(ax+b)$ or $Q=\cos(ax+b)$ it happens exactly when $f(-a^{2})=0$, equivalently when $\pm ia$ are roots of $f$; for $Q=x^{n}$ it happens exactly when $f(0)=0$, because then the polynomial forcing already contains a constant, which is a solution of the homogeneous equation.

In a resonant case the naive rule divides by zero, and no function of the original shape can serve, since the machine annihilates that shape. The reply then lies one family further out, multiplied by $x$, and the number of factors of $x$ equals the depth of the resonance. The algebraic mechanism is examined in Section 2.3, and its interpretation as a limit is examined in Section 5.1.

### 1.7 Notation for the rules

Two abbreviations keep the statements readable. The first is the derivative of the polynomial, $f'(D)$, obtained by differentiating $f$ with respect to the symbol $D$ and then reading the result as an operator; for $f(D)=D^{2}-1$ this gives $f'(D)=2D$. The second is the notation $f^{(r)}$ for the $r$-th derivative of $f$ with respect to $D$.

Where a wave is involved, the phrase replace $D^{2}$ by $-a^{2}$ is used in a precise sense. Write the polynomial split into its even and odd parts,

$$
f(D)=f_{1}\left(D^{2}\right)+D f_{2}\left(D^{2}\right),
$$

where $f_{1}$ collects the coefficients of the even powers and $f_{2}$ those of the odd powers after a factor of $D$ has been removed. Then replacing $D^{2}$ by $-a^{2}$ means forming the first-degree expression

$$
A+BD, \qquad A=f_{1}\left(-a^{2}\right), \qquad B=f_{2}\left(-a^{2}\right).
$$

The number $A^{2}+B^{2}a^{2}$ is the quantity that must not vanish; it vanishes exactly when $A=B=0$, that is, exactly in the resonant case.

## 2. Theorems, Lemmas, and Analytical Properties

### 2.1 The exponential rule

> **Lemma (Action on an exponential).** For every whole number $k$ and every number $a$, $D^{k}e^{ax}=a^{k}e^{ax}$.

> **Theorem 1 (Exponential forcing).** Let $f$ be a polynomial with constant coefficients. Then $f(D)e^{ax}=f(a)e^{ax}$. Consequently, if $f(a)\neq 0$, a particular integral of $f(D)y=e^{ax}$ is

$$
y_{p}=\frac{e^{ax}}{f(a)} .
$$

The hypothesis is exactly the non-resonance condition of Section 1.6. When it holds, the reply has the same shape as the forcing and its size is the reciprocal of the machine's response at that rate.

> **Example of the statement.** For $f(D)=D^{2}-5D+6$ and $a=4$ the value is $16-20+6=2$, so the particular integral of $\left(D^{2}-5D+6\right)y=e^{4x}$ is $\frac{e^{4x}}{2}$.

### 2.2 The exponential rule under resonance

> **Theorem 1' (Repeated root).** Let $\lambda$ be a root of $f$ of multiplicity $r$, so that $f(D)=(D-\lambda)^{r}g(D)$ with $g(\lambda)\neq 0$. Then

$$
\frac{e^{\lambda x}}{f(D)}=\frac{x^{r}e^{\lambda x}}{f^{(r)}(\lambda)} .
$$

Since $f^{(r)}(\lambda)=r!\,g(\lambda)$, the formula may also be written $\frac{x^{r}e^{\lambda x}}{r!\,g(\lambda)}$, which is the version usually quoted in examinations. For a real exponential the statement reads: if $a$ is a root of multiplicity $r$, then

$$
\frac{e^{ax}}{f(D)}=\frac{x^{r}e^{ax}}{f^{(r)}(a)} .
$$

Taking $r=1$ recovers the familiar rule of thumb that when $f(a)=0$ one multiplies by $x$ and divides by $f'(a)$; taking $r=2$ gives the rule that when $f(a)=f'(a)=0$ one multiplies by $x^{2}$ and divides by $f''(a)$. There is no factorial in these displayed forms because the factorial is already contained in $f^{(r)}(a)$; a student who writes $\frac{x^{2}e^{ax}}{2f''(a)}$ has counted the factorial twice.

### 2.3 The wave rule

> **Lemma (Even and odd decomposition).** Every polynomial $f$ can be written uniquely as $f(D)=f_{1}\left(D^{2}\right)+D f_{2}\left(D^{2}\right)$ with $f_{1}$ and $f_{2}$ polynomials.

> **Theorem 2 (Trigonometric forcing).** Let $Q$ be $\sin(ax+b)$ or $\cos(ax+b)$, let $A=f_{1}\left(-a^{2}\right)$ and $B=f_{2}\left(-a^{2}\right)$ be the values obtained by replacing $D^{2}$ by $-a^{2}$ in the even and odd parts. If $A^{2}+B^{2}a^{2}\neq 0$, then

$$
\frac{Q}{f(D)}=\frac{\left(A-BD\right)Q}{A^{2}+B^{2}a^{2}} .
$$

When $B=0$, which is the case for a polynomial in even powers only, the statement reduces to the familiar form

$$
\frac{\sin(ax+b)}{f(D)}=\frac{\sin(ax+b)}{f\left(-a^{2}\right)} ,
$$

and the same formula holds with a cosine in place of the sine. The sign in the replacement is the whole content of the rule: two differentiations of a wave of rate $a$ multiply it by $-a^{2}$, not by $+a^{2}$.

The general form of Theorem 2 is worth memorising as a single sentence: replace $D^{2}$ by $-a^{2}$, and if a bare $D$ survives, clear it by multiplying above and below by the companion expression in which the sign of that $D$ is reversed.

> **Theorem 2' (Trigonometric resonance).** Let $\pm ia$ be roots of $f$. Taking real and imaginary parts of the exponential identity of Theorem 1' with $\lambda=ia$ gives, for $r$ the multiplicity of $ia$ as a root,

$$
\frac{\sin(ax+b)}{f(D)}=\operatorname{Im}\frac{x^{r}e^{i(ax+b)}}{f^{(r)}(ia)}, \qquad \frac{\cos(ax+b)}{f(D)}=\operatorname{Re}\frac{x^{r}e^{i(ax+b)}}{f^{(r)}(ia)} .
$$

For the common case $r=1$ the rule takes the practical form

$$
\frac{\sin(ax+b)}{f(D)}=x\,\frac{\sin(ax+b)}{f'(D)},
$$

where the right-hand side is evaluated by replacing $D^{2}$ by $-a^{2}$ in $f'(D)$ and clearing any surviving $D$ as in Theorem 2. The factor $x$ is not optional and is not accompanied by any factorial divisor when written in this operator form, because the derivative of the polynomial already supplies the correct constant.

### 2.4 The power rule

> **Lemma (Nilpotence on polynomials).** If $p$ is a polynomial of degree at most $n$, then $D^{n+1}p=0$.

> **Theorem 3 (Polynomial forcing).** Let $Q=x^{n}$ and suppose $f(0)=a_{m}\neq 0$. Write $c_{k}$ for the coefficient of $D^{k}$ in $f$, so that $f(D)=c_{0}+c_{1}D+\cdots+c_{m}D^{m}$ with $c_{0}=f(0)$. Then

$$
\frac{1}{f(D)}=\frac{1}{c_{0}}\left(1+\frac{c_{1}}{c_{0}}D+\cdots+\frac{c_{m}}{c_{0}}D^{m}\right)^{-1},
$$

and the bracket is expanded in ascending powers of $D$ by the binomial theorem. Every term containing $D^{k}$ with $k>n$ annihilates $x^{n}$, so the expansion is truncated at $D^{n}$ and the result is exact, not approximate:

$$
\frac{x^{n}}{f(D)}=\frac{1}{c_{0}}\left[1-\left(\frac{c_{1}}{c_{0}}D+\cdots\right)+\left(\frac{c_{1}}{c_{0}}D+\cdots\right)^{2}-\cdots\right]x^{n} .
$$

The answer is a polynomial of degree $n$. Three points of technique decide most marks. The constant term $c_{0}$ is the number multiplying $y$ in the original equation, not the coefficient of the highest derivative. The expansion must proceed in ascending powers of $D$, since the higher powers are the ones that vanish. And the truncation index must be at least $n$, because the $n$-th derivative of $x^{n}$ is the constant $n!$, which survives.

> **Theorem 3' (Polynomial forcing when $f(0)=0$).** Suppose $f(D)=D^{s}g(D)$ with $g(0)\neq 0$ and $s\ge 1$. Then

$$
\frac{x^{n}}{f(D)}=\frac{1}{D^{s}}\left(\frac{x^{n}}{g(D)}\right),
$$

where the inner quotient is computed by Theorem 3 and the outer symbol means integrate $s$ times, discarding the constants of integration since each of them lies in the nullspace of $f(D)$.

### 2.5 The exponential shift rule

> **Theorem 4 (Exponential multiplied by a function).** For any differentiable function $u$ and any number $a$,

$$
f(D)\left[e^{ax}u\right]=e^{ax}f(D+a)u, \qquad \text{hence} \qquad \frac{e^{ax}u}{f(D)}=e^{ax}\frac{u}{f(D+a)} .
$$

The rule moves the exponential outside the operator and adds $a$ to every occurrence of $D$ inside. The residual problem has the same five rules available, applied to $u$ with the shifted polynomial; in particular, if $u$ is a polynomial the residual problem is a power problem, and if $u$ is a wave the residual problem is a wave problem.

> **Corollary (Polynomial times exponential).** If $u=x^{n}$, then

$$
\frac{x^{n}e^{ax}}{f(D)}=e^{ax}\frac{x^{n}}{f(D+a)},
$$

which reduces a mixed forcing to the power rule of Theorem 3 applied to the shifted polynomial.

### 2.6 The multiplier rule

> **Theorem 5 (Variable multiplied by a function).** For any differentiable function $u$,

$$
f(D)\left[xu\right]=x f(D)u+f'(D)u, \qquad \text{hence} \qquad \frac{xu}{f(D)}=x\frac{u}{f(D)}-\frac{f'(D)}{\left[f(D)\right]^{2}}u .
$$

The first identity is Leibniz's rule summed over the polynomial: differentiating a product $k$ times produces the term $xD^{k}u$ together with $kD^{k-1}u$, and the coefficients $k$ reproduce the derivative of the polynomial. The second identity is the first one solved for the inverse operator, and it is verified in Section 3 by applying $f(D)$ to the claimed answer.

Two warnings attach to the theorem. The correction term contains the square of the operator in the denominator, not the operator itself, and it contains $f'(D)$, not $f(D)$. And the two inverse operators appearing on the right must each be evaluated by the earlier rules on the function $u$; if $u$ is resonant with $f$, the failure remedies must be applied first, since otherwise the expression is meaningless.

> **Corollary (Exponential times the variable).** If $u=e^{bx}$ and $f(b)\neq 0$, then

$$
\frac{xe^{bx}}{f(D)}=x\frac{e^{bx}}{f(b)}-\frac{f'(b)e^{bx}}{\left[f(b)\right]^{2}} .
$$

This is the form in which the multiplier rule is most often examined, and it may be checked against Theorem 4, which gives the same answer by a different route whenever $u$ is an exponential.

### 2.7 Superposition

> **Theorem (Additivity in the forcing).** If $y_{1}$ is a particular integral of $f(D)y=Q_{1}$ and $y_{2}$ is a particular integral of $f(D)y=Q_{2}$, then $y_{1}+y_{2}$ is a particular integral of $f(D)y=Q_{1}+Q_{2}$.

The statement is immediate from linearity and licenses the standard practice of splitting a composite forcing into its shapes, solving each separately, and adding. It also licenses the reverse manoeuvre, used in the worked example on the hyperbolic cosine: a forcing which is a combination of exponentials may be split into its exponential pieces, each of which may be resonant or not.

## 3. Formal Proofs, Derivations, and Methods

### 3.1 Proof of the exponential rule

For $k$ a whole number, differentiating $e^{ax}$ once multiplies it by $a$, and repeating the operation $k$ times multiplies by $a^{k}$:

$$
D^{k}e^{ax}=a^{k}e^{ax} .
$$

Multiplying by the coefficient of $D^{k}$ and summing over $k$ gives

$$
f(D)e^{ax}=\sum_{k=0}^{m}c_{k}a^{k}e^{ax}=f(a)e^{ax} .
$$

If $f(a)\neq 0$, dividing by that number shows that $\frac{e^{ax}}{f(a)}$ is turned into $e^{ax}$, so it is a particular integral. If $f(a)=0$ the division is impossible and the argument establishes nothing; that case is settled next.

### 3.2 Proof of the repeated-root rule

Suppose $f(D)=(D-\lambda)^{r}g(D)$ with $g(\lambda)\neq 0$, and set

$$
y=e^{\lambda x}\frac{x^{r}}{r!\,g(\lambda)} .
$$

The identity of Theorem 4, applied with the number $-\lambda$, gives $(D-\lambda)\left[e^{\lambda x}w\right]=e^{\lambda x}Dw$ for every differentiable $w$, and iterating it $r$ times gives $(D-\lambda)^{r}\left[e^{\lambda x}w\right]=e^{\lambda x}D^{r}w$. Hence

$$
f(D)y=(D-\lambda)^{r}g(D)\left[e^{\lambda x}\frac{x^{r}}{r!\,g(\lambda)}\right]=(D-\lambda)^{r}\left[e^{\lambda x}g(D+\lambda)\frac{x^{r}}{r!\,g(\lambda)}\right],
$$

where the second equality again uses Theorem 4, now with the number $\lambda$. Applying the first identity completes the reduction:

$$
f(D)y=e^{\lambda x}D^{r}\left[g(D+\lambda)\frac{x^{r}}{r!\,g(\lambda)}\right].
$$

Expand $g$ about $\lambda$ by Taylor's theorem in the operator variable: $g(D+\lambda)=g(\lambda)+D\,h(D)$ for some polynomial $h$. Then

$$
g(D+\lambda)\frac{x^{r}}{r!\,g(\lambda)}=\frac{x^{r}}{r!}+\frac{1}{g(\lambda)}D\,h(D)\frac{x^{r}}{r!} .
$$

The second summand is a polynomial of degree at most $r-1$, because one differentiation has been applied to a polynomial of degree $r$. Therefore $D^{r}$ of the second summand is zero by the nilpotence lemma, while $D^{r}$ of the first summand is one. Hence $f(D)y=e^{\lambda x}$, which is what a particular integral must satisfy.

It remains to identify the constant. Differentiating $f(D)=(D-\lambda)^{r}g(D)$ exactly $r$ times and setting $D=\lambda$ leaves only the term in which all $r$ differentiations act on the factor $(D-\lambda)^{r}$, so $f^{(r)}(\lambda)=r!\,g(\lambda)$, which is the denominator appearing in the statement.

### 3.3 Proof of the wave rule

Differentiating a wave twice returns the same wave multiplied by $-a^{2}$:

$$
D^{2}\sin(ax+b)=-a^{2}\sin(ax+b), \qquad D^{2}\cos(ax+b)=-a^{2}\cos(ax+b) .
$$

By induction, every even power of $D$ acts on such a wave as multiplication by the corresponding power of $-a^{2}$, and every odd power acts as that same number multiplied by one further $D$. Splitting the polynomial as $f(D)=f_{1}\left(D^{2}\right)+Df_{2}\left(D^{2}\right)$ therefore gives, for either wave,

$$
f(D)Q=A\,Q+B\,DQ,
$$

with $A=f_{1}\left(-a^{2}\right)$ and $B=f_{2}\left(-a^{2}\right)$. Now multiply the quotient by the companion expression $A-BD$:

$$
\frac{Q}{A+BD}=\frac{\left(A-BD\right)Q}{\left(A+BD\right)\left(A-BD\right)}=\frac{\left(A-BD\right)Q}{A^{2}-B^{2}D^{2}} .
$$

In the denominator $D^{2}$ may again be replaced by $-a^{2}$, giving the real number $A^{2}+B^{2}a^{2}$, which is non-zero precisely when $A$ and $B$ are not both zero. What remains is

$$
\frac{Q}{f(D)}=\frac{\left(A-BD\right)Q}{A^{2}+B^{2}a^{2}},
$$

and the numerator is now a combination of a sine and a cosine of the same argument, because $DQ$ is again such a wave. This proves Theorem 2. When $B=0$ the formula collapses to $\frac{AQ}{A^{2}}=\frac{Q}{A}$, which is the elementary version of the rule.

### 3.4 Proof of the trigonometric resonance rule

Let $\lambda=ia$, and let $r$ be the multiplicity of $\lambda$ as a root. Theorem 1' gives

$$
\frac{e^{i(ax+b)}}{f(D)}=\frac{x^{r}e^{i(ax+b)}}{f^{(r)}(ia)} .
$$

The left-hand side is a complex-valued particular integral of $f(D)y=e^{i(ax+b)}$, and since $f$ has real coefficients, the real and imaginary parts of a complex solution are separately solutions of the equations with forcings $\cos(ax+b)$ and $\sin(ax+b)$ respectively. Taking those parts term by term proves Theorem 2'. In particular, for $r=1$, writing $Z$ for the complex particular integral,

$$
Z=\frac{xe^{i(ax+b)}}{f'(ia)},\qquad \frac{\cos(ax+b)}{f(D)}=\operatorname{Re}Z,\qquad \frac{\sin(ax+b)}{f(D)}=\operatorname{Im}Z ,
$$

so the two wave cases are read from one computation. The operator form quoted in Theorem 2' is the same statement written without complex numbers, because for any polynomial $p$ whose even and odd collapses are $A$ and $B$, the operator $\frac{A-BD}{A^{2}+B^{2}a^{2}}$ acts on $e^{iax}$ as multiplication by $\frac{A-iBa}{A^{2}+B^{2}a^{2}}$, which is exactly $\frac{1}{p(ia)}$, since $p(ia)=A+iBa$ and $A^{2}+B^{2}a^{2}=\left|p(ia)\right|^{2}$.

### 3.5 Proof of the power rule

Write $f(D)=c_{0}+c_{1}D+\cdots+c_{m}D^{m}$ with $c_{0}\neq 0$ and factor out the constant term:

$$
f(D)=c_{0}\left(1+U\right), \qquad U=\frac{c_{1}}{c_{0}}D+\cdots+\frac{c_{m}}{c_{0}}D^{m} .
$$

The formal identity $\frac{1}{1+U}=1-U+U^{2}-U^{3}+\cdots$ is valid as an operator identity on polynomials, because $U$ raises the order of differentiation by at least one, so $U^{k}p=0$ for every polynomial $p$ once $k$ exceeds its degree. Applying the series to $x^{n}$ therefore gives an exact finite sum:

$$
\frac{x^{n}}{f(D)}=\frac{1}{c_{0}}\left(1-U+U^{2}-\cdots+\left(-U\right)^{n}\right)x^{n} .
$$

Every term with $k>n$ vanishes, which justifies the truncation, and the surviving terms are polynomials, so the answer is a polynomial of degree at most $n$. If $c_{0}=0$, write $f(D)=D^{s}g(D)$ with $g(0)\neq 0$ and observe that

$$
f(D)\left[\frac{1}{D^{s}}\frac{x^{n}}{g(D)}\right]=D^{s}g(D)\frac{1}{D^{s}}\frac{x^{n}}{g(D)}=x^{n},
$$

because the factor $D^{s}$ and the operator $\frac{1}{D^{s}}$ commute, the latter being $s$ successive integrations. This proves Theorem 3'.

### 3.6 Proof of the exponential shift

The identity $D\left[e^{ax}u\right]=e^{ax}\left(D+a\right)u$ follows from the product rule:

$$
\frac{d}{dx}\left(e^{ax}u\right)=ae^{ax}u+e^{ax}\frac{du}{dx}=e^{ax}\left(a+ D\right)u .
$$

Suppose inductively that $D^{k}\left[e^{ax}u\right]=e^{ax}\left(D+a\right)^{k}u$. Then

$$
D^{k+1}\left[e^{ax}u\right]=D\left[e^{ax}\left(D+a\right)^{k}u\right]=e^{ax}\left(D+a\right)\left(D+a\right)^{k}u=e^{ax}\left(D+a\right)^{k+1}u,
$$

so the identity holds for every $k$ and hence for every polynomial combination. Dividing the resulting identity $f(D)\left[e^{ax}u\right]=e^{ax}f(D+a)u$ by the operator gives Theorem 4.

### 3.7 Proof of the multiplier rule and verification of its formula

Differentiating the product $xu$ exactly $k$ times by Leibniz's rule gives

$$
D^{k}\left[xu\right]=xD^{k}u+kD^{k-1}u ,
$$

the second term because every differentiation can hit the factor $x$ at most once, contributing a factor of one, and there are $k$ choices of which differentiation does so. Multiplying by $c_{k}$ and summing,

$$
f(D)\left[xu\right]=x\sum_{k}c_{k}D^{k}u+\sum_{k}kc_{k}D^{k-1}u=xf(D)u+f'(D)u,
$$

since the coefficient $k c_{k}$ is precisely the coefficient of $D^{k-1}$ in the derivative of the polynomial.

To verify the formula for the quotient, write $v=\frac{u}{f(D)}$, so that $f(D)v=u$, and set

$$
y=xv-\frac{f'(D)}{\left[f(D)\right]^{2}}u .
$$

Applying $f(D)$ to the first term with the identity just proved gives $xf(D)v+f'(D)v=u+f'(D)\frac{u}{f(D)}$. Applying $f(D)$ to the second term cancels one factor of $f(D)$ and gives $\frac{f'(D)}{f(D)}u$. Subtracting,

$$
f(D)y=u+\frac{f'(D)}{f(D)}u-\frac{f'(D)}{f(D)}u=u,
$$

so $y$ is indeed a particular integral of $f(D)y=xu$.

### 3.8 Method: the decision procedure

The rules are applied in a fixed order.

Step 1. Collect $f(D)$ in standard form and record $f(0)$, the constant term.

Step 2. Factor $f$ and write the complementary function with $m$ arbitrary constants.

Step 3. Inspect $Q$. If it is a sum, split it into its shapes and treat each separately by Theorem 2.7.

Step 4. Match the shape. An exponential calls for $f(a)$; a wave calls for the collapse at $-a^{2}$; a polynomial calls for the ascending expansion; a product calls for the shift or the multiplier rule.

Step 5. Test the condition attached to the matched rule. A zero result is not an error but a resonance, and the remedy is the appropriate factor of $x$.

Step 6. Add the particular integral to the complementary function and verify by substitution, collecting coefficients of the independent pieces.

## 4. Representative Worked Examples and Solutions

### 4.1 Problem: an exponential forcing away from resonance

Solve $\left(D^{2}-5D+6\right)y=e^{4x}$.

### 4.2 Solution: evaluate the polynomial at four

Step 1. Write the polynomial and factor it, to display both the ordinary rule and the complementary function.

$$
f(D)=D^{2}-5D+6=(D-3)(D-2)
$$

Step 2. Evaluate at the exponent's number.

$$
f(4)=16-20+6=2
$$

Step 3. Since the value is not zero, apply Theorem 1.

$$
y_{p}=\frac{e^{4x}}{2}
$$

Step 4. Record the complementary function.

$$
y_{c}=c_{1}e^{3x}+c_{2}e^{2x}
$$

Step 5. Add and verify.

$$
y=c_{1}e^{3x}+c_{2}e^{2x}+\frac{e^{4x}}{2}
$$

Substituting the particular integral gives $\frac{e^{4x}}{2}\left(16-20+6\right)=e^{4x}$, so the equation is satisfied. The answer carries two constants, matching the order two.

### 4.3 Problem: an exponential forcing at resonance

Solve $\left(D^{2}-5D+6\right)y=e^{3x}$.

### 4.4 Solution: the simple root case, one factor of $x$

Step 1. Evaluate the polynomial at three and observe the failure.

$$
f(3)=9-15+6=0
$$

Step 2. Identify the multiplicity of the root three. Since $f(D)=(D-3)(D-2)$ and the factor $D-2$ does not vanish at three, the multiplicity is one, so $r=1$.

Step 3. Compute the derivative of the polynomial and evaluate it at three.

$$
f'(D)=2D-5, \qquad f'(3)=6-5=1
$$

Step 4. Apply Theorem 1' with $r=1$.

$$
y_{p}=\frac{xe^{3x}}{f'(3)}=xe^{3x}
$$

Step 5. Add the complementary function, then verify.

$$
y=c_{1}e^{3x}+c_{2}e^{2x}+xe^{3x}
$$

Verification, collecting the two independent pieces:

$$
y_{p}'=e^{3x}\left(1+3x\right), \qquad y_{p}''=e^{3x}\left(6+9x\right),
$$

$$
y_{p}''-5y_{p}'+6y_{p}=e^{3x}\left(6+9x-5-15x+6x\right)=e^{3x} .
$$

The coefficient of $xe^{3x}$ vanishes and the constant coefficient is one, so the reply is correct. Note that the particular integral duplicates the shape of a member of the complementary function multiplied by $x$, which is the signature of resonance.

### 4.5 Problem: a double resonance

Solve $\left(D-2\right)^{2}y=4e^{2x}$.

### 4.6 Solution: the double root case, $x$ squared and $f''(2)$

Step 1. Identify the root and its multiplicity. The polynomial is $\left(D-2\right)^{2}$, so $2$ is a double root and $r=2$.

Step 2. Compute the second derivative of the polynomial and evaluate it at two.

$$
f(D)=D^{2}-4D+4, \qquad f''(D)=2, \qquad f''(2)=2
$$

Step 3. Apply Theorem 1' with $r=2$ and the forcing $4e^{2x}$.

$$
y_{p}=\frac{4x^{2}e^{2x}}{f''(2)}=\frac{4x^{2}e^{2x}}{2}=2x^{2}e^{2x}
$$

Step 4. Verify by applying the operator twice, in two separate displays.

$$
\left(D-2\right)\left(2x^{2}e^{2x}\right)=e^{2x}\left(4x+4x^{2}\right)-2e^{2x}\left(2x^{2}\right)=4xe^{2x}
$$

$$
\left(D-2\right)\left(4xe^{2x}\right)=e^{2x}\left(4+8x\right)-2e^{2x}\left(4x\right)=4e^{2x}
$$

Step 5. Add the complementary function, which carries a factor of $x$ on its second member for the same reason.

$$
y=c_{1}e^{2x}+c_{2}xe^{2x}+2x^{2}e^{2x}
$$

The verification shows why the divisor by $f''(2)$ is needed: without it the answer would be four times too large.

### 4.7 Problem: a hyperbolic forcing split into exponentials

Solve $\left(D-1\right)\left(D+3\right)\left(D-5\right)y=\cosh x$.

### 4.8 Solution: linearity, one resonant piece and one ordinary piece

Step 1. Rewrite the forcing using the definition of the hyperbolic cosine.

$$
\cosh x=\frac{e^{x}+e^{-x}}{2}
$$

Step 2. Record the polynomial and the complementary function; the roots are one, minus three and five.

$$
y_{c}=c_{1}e^{x}+c_{2}e^{-3x}+c_{3}e^{5x}
$$

Step 3. Handle the first piece $\frac{e^{x}}{2}$. The value $f(1)$ is zero because one is a root, so the multiplicity is one and the derivative is required.

$$
f'(D)=\left(D+3\right)\left(D-5\right)+\left(D-1\right)\left(D-5\right)+\left(D-1\right)\left(D+3\right),
$$

$$
f'(1)=\left(4\right)\left(-4\right)+0+0=-16
$$

Step 4. Apply Theorem 1' to the first piece.

$$
y_{1}=\frac{x e^{x}}{2\cdot\left(-16\right)}=-\frac{xe^{x}}{32}
$$

Step 5. Handle the second piece $\frac{e^{-x}}{2}$ by Theorem 1, since minus one is not a root.

$$
f(-1)=\left(-2\right)\left(2\right)\left(-6\right)=24, \qquad y_{2}=\frac{e^{-x}}{2\cdot 24}=\frac{e^{-x}}{48}
$$

Step 6. Add everything and verify the resonant piece.

$$
y=c_{1}e^{x}+c_{2}e^{-3x}+c_{3}e^{5x}-\frac{xe^{x}}{32}+\frac{e^{-x}}{48}
$$

Verification of $y_{1}$ proceeds by applying the three factors in turn, starting from the easy observation that $D-1$ annihilates the exponential and leaves the derivative of the multiplier:

$$
\left(D-1\right)\left(-\frac{xe^{x}}{32}\right)=-\frac{e^{x}}{32}\left(1+x-x\right)=-\frac{e^{x}}{32},
$$

$$
\left(D+3\right)\left(-\frac{e^{x}}{32}\right)=-\frac{e^{x}}{32}-\frac{3e^{x}}{32}=-\frac{e^{x}}{8},
$$

$$
\left(D-5\right)\left(-\frac{e^{x}}{8}\right)=-\frac{e^{x}}{8}+\frac{5e^{x}}{8}=\frac{e^{x}}{2},
$$

which is the first piece of the forcing. The verification of $y_{2}$ is immediate, since $f(-1)=24$ and the forcing there is $\frac{e^{-x}}{2}$.

### 4.9 Problem: a wave forcing with an even polynomial

Solve $\left(D^{2}+9\right)y=\sin 5x$.

### 4.10 Solution: replace $D^{2}$ by minus twenty-five

Step 1. Note the rate and collapse the polynomial.

$$
D^{2}\to -25, \qquad -25+9=-16
$$

Step 2. Apply Theorem 2 in its elementary form.

$$
y_{p}=-\frac{\sin 5x}{16}
$$

Step 3. Add the complementary function, whose roots are $\pm 3i$.

$$
y=c_{1}\cos 3x+c_{2}\sin 3x-\frac{\sin 5x}{16}
$$

Step 4. Verify using $y_{p}''=-25y_{p}$.

$$
y_{p}''+9y_{p}=-25y_{p}+9y_{p}=-16y_{p}=\sin 5x
$$

The check is complete and uses no differentiation beyond the double-differentiation identity for a wave.

### 4.11 Problem: a wave forcing with a surviving first derivative

Solve $\left(D^{2}+3D-10\right)y=\sin 2x$.

### 4.12 Solution: collapse, then clear the surviving operator

Step 1. Split the polynomial into even and odd parts and collapse at $-a^{2}=-4$.

$$
f_{1}\left(D^{2}\right)=D^{2}-10, \qquad f_{2}\left(D^{2}\right)=3, \qquad A=-14, \qquad B=3
$$

Step 2. Form the denominator of Theorem 2 and check that it does not vanish.

$$
A^{2}+B^{2}a^{2}=196+9\cdot 4=232
$$

Step 3. Apply the formula with $Q=\sin 2x$ and $DQ=2\cos 2x$.

$$
y_{p}=\frac{\left(A-BD\right)\sin 2x}{232}=\frac{-14\sin 2x-6\cos 2x}{232}
$$

Step 4. Simplify by dividing by two.

$$
y_{p}=-\frac{7\sin 2x}{116}-\frac{3\cos 2x}{116}
$$

Step 5. Verify by substitution. Let $y=A_{1}\cos 2x+B_{1}\sin 2x$ with the coefficients just found and compute the operator's action on a general wave.

$$
\left(D^{2}+3D-10\right)\left(A_{1}\cos 2x+B_{1}\sin 2x\right)=\left(-14A_{1}+6B_{1}\right)\cos 2x+\left(-6A_{1}-14B_{1}\right)\sin 2x
$$

With $A_{1}=-\frac{3}{116}$ and $B_{1}=-\frac{7}{116}$ the cosine coefficient is $\frac{42}{116}-\frac{42}{116}=0$ and the sine coefficient is $\frac{18}{116}+\frac{98}{116}=1$. The reply is correct, and the sign of the sine coefficient is the place where a slip in the collapse would show.

### 4.13 Problem: a wave forcing at resonance

Solve $\left(D^{2}+4\right)y=\cos 2x$.

### 4.14 Solution: multiply by $x$ and divide by the derivative

Step 1. Collapse the polynomial and observe that it vanishes.

$$
D^{2}\to -4, \qquad -4+4=0
$$

Step 2. The resonance is of multiplicity one, since $\left(D^{2}+4\right)$ is the whole polynomial. Record the derivative.

$$
f'(D)=2D
$$

Step 3. Apply Theorem 2' in operator form, remembering that one integration of a cosine produces a sine divided by the rate.

$$
y_{p}=x\cdot\frac{\cos 2x}{2D}=x\cdot\frac{\sin 2x}{4}=\frac{x\sin 2x}{4}
$$

Step 4. Verify.

$$
y_{p}'=\frac{\sin 2x}{4}+\frac{x\cos 2x}{2}, \qquad y_{p}''=\cos 2x-x\sin 2x,
$$

$$
y_{p}''+4y_{p}=\cos 2x-x\sin 2x+x\sin 2x=\cos 2x
$$

Step 5. Add the complementary function.

$$
y=c_{1}\cos 2x+c_{2}\sin 2x+\frac{x\sin 2x}{4}
$$

The amplitude of the reply grows with $x$, which is the analytic signature of resonance.

### 4.15 Problem: a polynomial forcing

Solve $\left(2D^{2}+2D+3\right)y=x^{2}$.

### 4.16 Solution: expand in ascending powers to $D^{2}$

Step 1. Factor out the constant term three.

$$
\frac{1}{2D^{2}+2D+3}=\frac{1}{3}\left(1+\frac{2}{3}D+\frac{2}{3}D^{2}\right)^{-1}
$$

Step 2. Expand the bracket to second order, keeping every product that contributes a power no higher than $D^{2}$.

$$
\left(1+U\right)^{-1}=1-U+U^{2}-\cdots, \qquad U=\frac{2}{3}D+\frac{2}{3}D^{2},
$$

$$
1-\frac{2}{3}D-\frac{2}{3}D^{2}+\frac{4}{9}D^{2}=1-\frac{2}{3}D-\frac{2}{9}D^{2}
$$

Step 3. Apply the truncated operator to $x^{2}$, using $D x^{2}=2x$ and $D^{2}x^{2}=2$.

$$
y_{p}=\frac{1}{3}\left[x^{2}-\frac{2}{3}\left(2x\right)-\frac{2}{9}\left(2\right)\right]=\frac{x^{2}}{3}-\frac{4x}{9}-\frac{4}{27}
$$

Step 4. Find the complementary function from the roots of $2m^{2}+2m+3=0$, whose discriminant is $4-24=-20$.

$$
m=-\frac{1}{2}\pm\frac{\sqrt{5}}{2}i, \qquad y_{c}=e^{-x/2}\left(c_{1}\cos\frac{\sqrt{5}}{2}x+c_{2}\sin\frac{\sqrt{5}}{2}x\right)
$$

Step 5. Verify by substitution.

$$
y_{p}'=\frac{2x}{3}-\frac{4}{9}, \qquad y_{p}''=\frac{2}{3},
$$

$$
2y_{p}''+2y_{p}'+3y_{p}=\frac{4}{3}+\frac{4x}{3}-\frac{8}{9}+x^{2}-\frac{4x}{3}-\frac{4}{9}=x^{2}
$$

The $x$ terms cancel and the constants combine to zero, so the reply is correct. Note that the coefficients of the answer are not the coefficients of the forcing: the machine tilts and shifts the polynomial, and only the leading coefficient is simply related to the constant term of the polynomial.

### 4.17 Problem: a polynomial forcing when the constant term vanishes

Solve $\left(D^{2}-D\right)y=x$.

### 4.18 Solution: divide out $D$, then integrate once

Step 1. Observe that $f(0)=0$, so Theorem 3 does not apply directly. Factor the polynomial.

$$
f(D)=D\left(D-1\right)
$$

Step 2. Apply Theorem 3' with $s=1$ and $g(D)=D-1$.

$$
\frac{x}{D\left(D-1\right)}=\frac{1}{D}\left(\frac{x}{D-1}\right)
$$

Step 3. Evaluate the inner quotient by the ascending expansion.

$$
\frac{1}{D-1}=-\left(1-D\right)^{-1}=-\left(1+D+\cdots\right), \qquad \frac{x}{D-1}=-\left(x+1\right)
$$

Step 4. Integrate once, dropping the constant since constants solve the homogeneous equation.

$$
y_{p}=\frac{1}{D}\left(-x-1\right)=-\frac{x^{2}}{2}-x
$$

Step 5. Verify.

$$
y_{p}'=-x-1, \qquad y_{p}''=-1, \qquad y_{p}''-y_{p}'=-1+x+1=x
$$

Step 6. Add the complementary function, $y_{c}=c_{1}+c_{2}e^{x}$.

$$
y=c_{1}+c_{2}e^{x}-\frac{x^{2}}{2}-x
$$

### 4.19 Problem: an exponential multiplied by a power

Solve $\left(D-4\right)y=x^{2}e^{3x}$.

### 4.20 Solution: pass the exponential through and shift the dials

Step 1. Apply Theorem 4 with $a=3$.

$$
\frac{x^{2}e^{3x}}{D-4}=e^{3x}\frac{x^{2}}{D+3-4}=e^{3x}\frac{x^{2}}{D-1}
$$

Step 2. Rewrite the residual quotient in the standard factored form.

$$
\frac{1}{D-1}=-\left(1-D\right)^{-1}=-\left(1+D+D^{2}+\cdots\right)
$$

Step 3. Apply the truncated expansion to $x^{2}$.

$$
\frac{x^{2}}{D-1}=-\left(x^{2}+2x+2\right)
$$

Step 4. Multiply the exponential back and record the complementary function.

$$
y_{p}=-e^{3x}\left(x^{2}+2x+2\right), \qquad y=c_{1}e^{4x}-e^{3x}\left(x^{2}+2x+2\right)
$$

Step 5. Verify by substitution, collecting the three independent pieces.

$$
y_{p}'=-e^{3x}\left(3x^{2}+8x+8\right), \qquad y_{p}'-4y_{p}=e^{3x}\left(-3x^{2}-8x-8+4x^{2}+8x+8\right)=x^{2}e^{3x}
$$

All three coefficients match, so the shift has been applied with the correct sign.

### 4.21 Problem: an exponential multiplied by a wave

Solve $\left(D^{2}+1\right)y=e^{2x}\sin x$.

### 4.22 Solution: shift, then use the wave rule on the residual problem

Step 1. Apply Theorem 4 with $a=2$.

$$
\frac{e^{2x}\sin x}{D^{2}+1}=e^{2x}\frac{\sin x}{\left(D+2\right)^{2}+1}=e^{2x}\frac{\sin x}{D^{2}+4D+5}
$$

Step 2. Collapse the residual polynomial at $D^{2}=-1$, keeping the surviving derivative.

$$
D^{2}+4D+5\to -1+4D+5=4D+4
$$

Step 3. Clear the surviving operator by multiplying by its companion.

$$
\frac{\sin x}{4D+4}=\frac{\left(4D-4\right)\sin x}{16D^{2}-16}=\frac{4\cos x-4\sin x}{-16-16}=\frac{\sin x-\cos x}{8}
$$

Step 4. Multiply the exponential back on.

$$
y_{p}=\frac{e^{2x}\left(\sin x-\cos x\right)}{8}
$$

Step 5. Verify with $w=\sin x-\cos x$, so that $w''=-w$.

$$
y_{p}'=\frac{e^{2x}\left(2w+w'\right)}{8}, \qquad y_{p}''=\frac{e^{2x}\left(4w+4w'+w''\right)}{8}=\frac{e^{2x}\left(3w+4w'\right)}{8},
$$

$$
y_{p}''+y_{p}=\frac{e^{2x}\left(4w+4w'\right)}{8}=\frac{e^{2x}\left(w+w'\right)}{2}=e^{2x}\sin x,
$$

since $w+w'=2\sin x$. The verification confirms both the shift and the collapse.

### 4.23 Problem: the variable multiplied by an exponential

Solve $\left(D^{2}-1\right)y=xe^{3x}$.

### 4.24 Solution: Theorem 5 with one correction term

Step 1. Record the ingredients of Theorem 5.

$$
f(D)=D^{2}-1, \qquad f'(D)=2D, \qquad u=e^{3x}, \qquad f(3)=8
$$

Step 2. Evaluate the first piece of the rule.

$$
x\frac{e^{3x}}{f(3)}=\frac{xe^{3x}}{8}
$$

Step 3. Evaluate the correction, using $\left[f(3)\right]^{2}=64$ and $f'(D)e^{3x}=6e^{3x}$.

$$
\frac{f'(D)}{\left[f(D)\right]^{2}}e^{3x}=\frac{6e^{3x}}{64}=\frac{3e^{3x}}{32}
$$

Step 4. Subtract, and add the complementary function.

$$
y=c_{1}e^{x}+c_{2}e^{-x}+\frac{xe^{3x}}{8}-\frac{3e^{3x}}{32}
$$

Step 5. Verify.

$$
y_{p}'=e^{3x}\left(\frac{3x}{8}-\frac{5}{32}\right), \qquad y_{p}''=e^{3x}\left(\frac{9x}{8}-\frac{3}{32}\right),
$$

$$
y_{p}''-y_{p}=e^{3x}\left(\frac{9x}{8}-\frac{3}{32}-\frac{x}{8}+\frac{3}{32}\right)=xe^{3x}
$$

Step 6. Confirm by the alternative route of Theorem 4, which must give the same answer.

$$
\frac{xe^{3x}}{D^{2}-1}=e^{3x}\frac{x}{D^{2}+6D+8}=\frac{e^{3x}}{8}\left(1+\frac{6D+D^{2}}{8}\right)^{-1}x=\frac{e^{3x}}{8}\left(x-\frac{3}{4}\right)
$$

The two answers agree, since $\frac{e^{3x}}{8}\left(x-\frac{3}{4}\right)=\frac{xe^{3x}}{8}-\frac{3e^{3x}}{32}$.

### 4.25 Problem: the variable multiplied by a wave

Solve $\left(D-2\right)y=x\sin x$.

### 4.26 Solution: Theorem 5 with a wave in the correction

Step 1. Apply the formula of Theorem 5 with $f(D)=D-2$, so that $f'(D)=1$.

$$
y_{p}=x\frac{\sin x}{D-2}-\frac{1}{\left(D-2\right)^{2}}\sin x
$$

Step 2. Evaluate the first inverse operator by clearing the surviving derivative.

$$
\frac{\sin x}{D-2}=\frac{\left(D+2\right)\sin x}{D^{2}-4}=\frac{\cos x+2\sin x}{-5}
$$

Step 3. Evaluate the second inverse operator by squaring and clearing in the same way.

$$
\left(D+2\right)^{2}\sin x=D^{2}\sin x+4D\sin x+4\sin x=-\sin x+4\cos x+4\sin x=3\sin x+4\cos x,
$$

$$
\frac{\sin x}{\left(D-2\right)^{2}}=\frac{3\sin x+4\cos x}{\left(-5\right)^{2}}=\frac{3\sin x+4\cos x}{25}
$$

Step 4. Assemble the particular integral.

$$
y_{p}=-\frac{x\left(\cos x+2\sin x\right)}{5}-\frac{3\sin x+4\cos x}{25}
$$

Step 5. Verify by computing the operator's action on the two parts.

$$
\left(D-2\right)\left[-\frac{x\left(\cos x+2\sin x\right)}{5}\right]=x\sin x-\frac{\cos x+2\sin x}{5},
$$

$$
\left(D-2\right)\left[-\frac{3\sin x+4\cos x}{25}\right]=\frac{\cos x+2\sin x}{5},
$$

so the sum is $x\sin x$. The correction term cancels the residue of the first term exactly, which is the purpose of the theorem.

## 5. Mathematical Extensions, Limits, and Common Errors

### 5.1 Resonance as a limit

The resonant formulas are not a separate theory; they are the limit of the ordinary formulas as the forcing rate approaches a root. Suppose $f(a)=0$ and let $\epsilon\neq 0$. The function

$$
y_{\epsilon}=\frac{e^{\left(a+\epsilon\right)x}-e^{ax}}{f\left(a+\epsilon\right)}
$$

has the following property. The first term divided by $f(a+\epsilon)$ is the ordinary particular integral for the forcing $e^{\left(a+\epsilon\right)x}$, and the second term is a multiple of $e^{ax}$, which lies in the nullspace because $f(a)=0$. Hence $f(D)y_{\epsilon}=e^{\left(a+\epsilon\right)x}$, and as $\epsilon\to 0$ the right-hand side tends to $e^{ax}$ while

$$
y_{\epsilon}=\frac{e^{\left(a+\epsilon\right)x}-e^{ax}}{\epsilon}\cdot\frac{\epsilon}{f\left(a+\epsilon\right)}\longrightarrow x e^{ax}\cdot\frac{1}{f'(a)} .
$$

The limit is therefore $\frac{xe^{ax}}{f'(a)}$, which is Theorem 1' with $r=1$. Repeating the argument differentiates once more with respect to the parameter and produces the second-order case with its divisor $f''(a)$. The factor of $x$ is thus not a device but the derivative of the exponential with respect to its own rate, and the divisors are the derivatives of the response function.

### 5.2 Why particular integrals are not unique

Any two particular integrals of the same equation differ by an element of the nullspace, and every rule in this note therefore returns one answer out of an $m$-dimensional family. This has three practical consequences. Answers that look different may both be right, so a printed solution is not the standard of correctness; substitution is. The constants of integration produced by the integrations in Theorem 3' may be set to zero, because they lie in the nullspace. And when the forcing is resonant, the rule of thumb produces a particular integral that itself contains a term of the complementary function, which does no harm.

### 5.3 Where the operator algebra stops being valid

The whole method rests on treating $D$ as an algebraic symbol, and that is legitimate only because the coefficients are constants. With a variable coefficient the symbol does not commute: if $x$ denotes multiplication by the independent variable, then

$$
D\left(xy\right)=xDy+y, \qquad \text{so} \qquad Dx-xD=1 .
$$

Consequently a polynomial in $D$ cannot be factored, evaluated at numbers, or expanded by the binomial theorem in the presence of variable coefficients, and none of the five theorems applies. Equations such as $x^{2}y''+xy'+y=Q$ require series methods or a change of variable, not short methods.

A second limit is the class of forcings. The five families are the ones mapped into themselves by a constant-coefficient operator; a forcing such as $\ln x$, $\frac{1}{x}$ or $\tan x$ is not, so the answer must be obtained by variation of parameters and will usually involve an integral that cannot be evaluated in elementary terms.

### 5.4 The complex route as a unifying device

All five rules can be derived from one identity, the action on a complex exponential, together with the observation that a real operator applied to a complex function separates into real and imaginary parts. For instance

$$
\frac{e^{\left(\alpha+i\beta\right)x}}{f(D)}=\frac{e^{\left(\alpha+i\beta\right)x}}{f\left(\alpha+i\beta\right)}
$$

whenever the denominator is non-zero, and its real and imaginary parts are particular integrals for $e^{\alpha x}\cos\beta x$ and $e^{\alpha x}\sin\beta x$. This is why the exponential shift and the wave rule are really the same rule, and why a forcing such as $e^{2x}\cos 3x$ can be handled either by shifting and then collapsing, or by a single complex evaluation. The complex route is also the shortest justification of the sign in the wave rule, since $D^{2}$ acting on $e^{iax}$ multiplies by $\left(ia\right)^{2}=-a^{2}$.

### 5.5 Common errors

- **Replacing $D^{2}$ by $+a^{2}$.** The correct value is $-a^{2}$, since $\left(ia\right)^{2}=-a^{2}$. The error reverses the sign of the whole particular integral and is caught at once by substitution.
- **Replacing the surviving $D$ as well.** In a polynomial such as $D^{2}+3D-10$ only the even part may be collapsed; the term $3D$ becomes the operator $3D$ at the collapsed stage and must then be cleared by multiplying by its companion.
- **Dividing by zero instead of recognising resonance.** A vanishing $f(a)$ or $f\left(-a^{2}\right)$ announces that the forcing lies in the nullspace; the remedy is a factor of $x$, not a larger denominator.
- **Applying the multiplier when nothing fails.** A factor of $x$ introduced without resonance produces a function that the operator does not map to the forcing.
- **Counting the factorial twice.** The divisor in the repeated-root formula is $f^{(r)}(a)$, which already contains $r!$; writing $\frac{x^{2}e^{ax}}{2f''(a)}$ halves the answer.
- **Using the wrong multiplicity.** The exponent of $x$ equals the multiplicity of the root, which must be read from the factorisation and not guessed from the order of the equation.
- **Truncating the polynomial expansion too early.** Terms up to $D^{n}$ are required for the forcing $x^{n}$; the $n$-th derivative supplies the constant that makes the substitution work.
- **Expanding in descending powers.** Only the ascending expansion is valid, because it is the higher powers of $D$ that annihilate the polynomial.
- **Forgetting that $c_{0}$ is $f(0)$.** The divisor in the polynomial rule is the coefficient of $y$, not the coefficient of the highest derivative.
- **Using Theorem 5 without first inverting $f(D)$ on $u$.** If $u$ is resonant, the terms $x\frac{u}{f(D)}$ and $\frac{f'(D)}{\left[f(D)\right]^{2}}u$ are meaningless until the resonance is resolved.
- **Omitting the square in the correction term.** The denominator is $\left[f(D)\right]^{2}$, and the numerator is $f'(D)$, not $f(D)$.
- **Dropping the complementary function.** The particular integral never supplies the arbitrary constants, and an answer with too few constants cannot be the general solution.

### 5.6 Summary of the theory

The note establishes five rules and one structure. The structure is that every solution of $f(D)y=Q$ is a complementary function plus a particular integral, so the work splits into two independent tasks. The rules are the inverses of $f(D)$ on the five families that a constant-coefficient operator carries into themselves: the exponentials, the waves, the polynomials, the products of an exponential with a function, and the products of the variable with a function.

Each rule has the same logical shape: a candidate answer is proposed from within the family, the operator is applied to it, and the coefficients are matched. Theorem 1 evaluates the polynomial at the rate; Theorem 1' differentiates the polynomial when that evaluation vanishes. Theorem 2 collapses the even part of the polynomial at $-a^{2}$ and clears whatever first-order operator survives; Theorem 2' multiplies by $x$ when the collapse vanishes. Theorem 3 expands the reciprocal in ascending powers and truncates; Theorem 3' divides out the factor $D$ and integrates. Theorem 4 shifts the polynomial; Theorem 5 corrects for the product rule. Every statement is proved by applying $f(D)$ to the answer, and every worked example is confirmed by substitution, which is the only check that cannot be satisfied by a wrong sign.
