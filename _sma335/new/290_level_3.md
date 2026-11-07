## 1. Foundational Concepts, Definitions, and Axioms

### 1.1 What this topic is worth, and where the marks sit

This topic is one of the most predictable on the paper. The equation is always of the same shape, the forcing terms are always drawn from the same short catalogue, and the marking scheme always awards marks for the same five actions: finding the roots, writing the complementary function, choosing the trial, computing the coefficients, and applying the conditions. Nothing in the topic rewards cleverness, and almost everything rewards accuracy in the algebra.

The distribution below is typical. Use it to decide how much writing each part deserves.

| Question type | Typical marks | Typical time | Where the marks sit |
| --- | --- | --- | --- |
| Solve with a non-resonant exponential forcing term | 8 to 10 | 8 minutes | Roots, complementary function, trial, coefficients, general solution |
| Solve with a resonant exponential forcing term | 10 to 12 | 10 minutes | Detection of duplication, factor $x$, coefficients |
| Solve with polynomial forcing | 10 to 12 | 11 minutes | Full trial through the top power, three coefficient equations |
| Solve with sine or cosine forcing | 10 to 12 | 11 minutes | Both basis functions in the trial, two coefficient equations |
| Solve with a product forcing term | 12 to 14 | 13 minutes | Whole polynomial factor, possible factor $x$, careful differentiation |
| Solve with a sum forcing term | 12 to 14 | 12 minutes | Splitting, one index of duplication per piece, adding |
| Initial value problem | 13 to 15 | 14 minutes | Complete solution before conditions, two simultaneous equations |
| Find the particular integral only | 5 to 7 | 6 minutes | Trial and coefficients, no complementary function |
| Explain why a factor $x$ is needed | 2 to 3 | 3 minutes | The duplication statement, not the arithmetic |
| Verify that a given function solves the equation | 3 to 4 | 4 minutes | Two derivatives, substitution, conclusion |

Two conclusions follow from the table. First, the marks are spread evenly through the solution rather than concentrated at the end, so an unfinished attempt that has correct roots and a correct complementary function still scores. Second, the only steps worth double-checking under time pressure are the trial and the coefficient matching, because those are where a single sign error destroys the rest of the answer.

### 1.2 The definitions to reproduce exactly

Definitions in this topic are marked as bookwork. The following wordings are safe.

> **Definition (second-order nonhomogeneous linear equation with constant coefficients).** An equation of the form
>
> $$
> a_{0}\frac{d^{2}y}{dx^{2}}+a_{1}\frac{dy}{dx}+a_{2}y=Q(x),
> $$
>
> where $a_{0}$, $a_{1}$, $a_{2}$ are constants with $a_{0}\ne 0$ and $Q$ is a given function of $x$, is called a second-order nonhomogeneous linear equation with constant coefficients.

Marking note: three phrases carry the marks, namely constant coefficients, second order, and $a_{0}\ne 0$. Omitting the condition on $a_{0}$ costs a mark in strict schemes.

> **Definition (homogeneous equation).** The equation obtained by setting $Q(x)=0$ is called the corresponding homogeneous equation.

> **Definition (complementary function).** The complementary function is the general solution of the homogeneous equation. It contains two arbitrary constants.

Marking note: the count of two constants is a separate marking point, and it must be justified by the order of the equation.

> **Definition (particular integral).** A particular integral is any function which, when substituted into the nonhomogeneous equation, satisfies it identically. It contains no arbitrary constants.

> **Definition (general solution).** The general solution of the nonhomogeneous equation is the sum of the complementary function and any particular integral,
>
> $$
> y=y_{c}+y_{p}.
> $$

Marking note: the phrase any particular integral is the key. A candidate who writes "the particular integral" as though it were unique has not understood why the constants are still free.

### 1.3 The three root patterns and the marks they earn

The auxiliary equation is quadratic, so only three patterns of root can occur. Each pattern has a fixed complementary function and a fixed number of marks.

| Roots of $a_{0}m^{2}+a_{1}m+a_{2}=0$ | Complementary function | Marks for the pair |
| --- | --- | --- |
| Real and distinct, $m_{1}\ne m_{2}$ | $y_{c}=c_{1}e^{m_{1}x}+c_{2}e^{m_{2}x}$ | 2 |
| Real and equal, $m$ twice | $y_{c}=\left(c_{1}+c_{2}x\right)e^{mx}$ | 2 to 3 |
| Complex, $\alpha\pm i\beta$ | $y_{c}=e^{\alpha x}\left(c_{1}\cos\beta x+c_{2}\sin\beta x\right)$ | 3 |

The marks are not awarded for the algebra of solving the quadratic, which is worth a single mark at most, but for writing the correct form. A repeated root without the factor $x$, or complex roots without the exponential factor $e^{\alpha x}$, loses the form mark even when the roots themselves are right.

Two conventions save time. Write the roots as a pair before writing $y_{c}$, because the pair is what the scheme looks for. And keep the constants named $c_{1}$ and $c_{2}$ unless the question uses other letters, because renaming costs nothing and inconsistent naming costs marks in some schemes.

### 1.4 The trial table as an examination tool

Every forcing term in this topic is of the form $e^{\alpha x}\left(P(x)\cos\beta x+R(x)\sin\beta x\right)$. Write $\mu=\alpha+i\beta$ and let $s$ be the multiplicity of $\mu$ among the characteristic roots. Then the trial is the tabulated shape multiplied by $x^{s}$.

| Forcing term | $s=0$ | $s=1$ | $s=2$ |
| --- | --- | --- | --- |
| $C$ | $A$ | $Ax$ | $Ax^{2}$ |
| $Cx+D$ | $Ax+B$ | $x\left(Ax+B\right)$ | $x^{2}\left(Ax+B\right)$ |
| $Cx^{2}+Dx+E$ | $Ax^{2}+Bx+C_{0}$ | $x\left(Ax^{2}+Bx+C_{0}\right)$ | $x^{2}\left(Ax^{2}+Bx+C_{0}\right)$ |
| $Ce^{kx}$ | $Ae^{kx}$ | $Axe^{kx}$ | $Ax^{2}e^{kx}$ |
| $C\cos\beta x$ or $C\sin\beta x$ | $A\cos\beta x+B\sin\beta x$ | $x\left(A\cos\beta x+B\sin\beta x\right)$ | $x^{2}\left(A\cos\beta x+B\sin\beta x\right)$ |
| $Cxe^{kx}$ | $\left(Ax+B\right)e^{kx}$ | $x\left(Ax+B\right)e^{kx}$ | $x^{2}\left(Ax+B\right)e^{kx}$ |
| $e^{\alpha x}\left(Cx\cos\beta x\right)$ | $e^{\alpha x}\left(Ax+B\right)\cos\beta x+e^{\alpha x}\left(C_{1}x+D\right)\sin\beta x$ | $x$ times the $s=0$ entry | $x^{2}$ times the $s=0$ entry |

Three reading rules turn the table into marks. Read $\alpha$ and $\beta$ from the forcing term, not from the roots. Test the single complex number $\mu=\alpha+i\beta$ against the roots, with its sign. And count the multiplicity honestly, since a repeated root allows $s=2$ and nothing larger.

### 1.5 The shapes of question actually asked

Eight shapes cover the paper, and each is recognised within a few seconds.

The first asks for the general solution of an equation with a single forcing term. The answer is $y_{c}$ plus $y_{p}$, with two constants left free.

The second asks only for a particular integral. The complementary function is then unnecessary, and writing it wastes time; the marks are for the trial, the differentiation, and the coefficients.

The third gives initial conditions and asks for the solution of the initial value problem. The complete general solution must be found first, and only then are the two conditions imposed.

The fourth asks the candidate to show that a given function satisfies the equation. The marks are for differentiating twice, substituting, and stating the conclusion, and no method of solution is required.

The fifth asks why a factor of $x$ appears, or asks the candidate to explain a resonance. The marks are for the statement that the forcing term duplicates a term of the complementary function, and for the consequence that the naive trial lies in the kernel of the operator.

The sixth supplies a general solution with unknown constants and two conditions, and asks for the constants. Here the equation is not needed at all beyond its general solution.

The seventh combines a nonhomogeneous equation with a homogeneous one, for instance by asking for the solution of $L[y]=Q_{1}+Q_{2}$. Splitting the right-hand side and using superposition is the expected route.

The eighth asks for a particular integral in operator form, such as $\frac{1}{(D-a)(D-b)}Q$. The two-stage integration formula from the lectures is then the expected method, and it must be presented as two first-order problems.

### 1.6 The three-line opening that earns the method marks

Every solution should begin with the same three lines, because they are separately marked and because they organise everything that follows.

Line one states the auxiliary equation. Line two states its roots. Line three states the complementary function in the correct one of the three forms. Writing those three lines first costs about forty seconds and secures between three and five marks before any forcing term has been touched.

## 2. Theorems, Lemmas, and Analytical Properties

### 2.1 High-yield result 1: the structure of the general solution

> **Theorem (structure theorem, worth 3 marks).** If $y_{p}$ is any particular integral of $L[y]=Q$, then the general solution of the equation is
>
> $$
> y=y_{c}+y_{p},
> $$
>
> where $y_{c}$ is the general solution of $L[y]=0$.

The proof is examined as bookwork in some years. Let $Y$ be any solution and put $z=Y-y_{p}$. By linearity $L[z]=Q-Q=0$, so $z$ is a homogeneous solution and therefore equals $c_{1}y_{1}+c_{2}y_{2}$. Hence $Y=y_{p}+y_{c}$.

The marking points are the definition of $z$, the use of linearity to compute $L[z]$, and the conclusion that $z$ lies in the two-dimensional homogeneous space. A candidate who only writes the formula, with no argument, typically earns one of the three marks.

### 2.2 High-yield result 2: the cover-up rule

> **Theorem (cover-up rule, worth 2 marks).** If $Q(x)=Ce^{kx}$ and $F(k)\ne 0$, then
>
> $$
> y_{p}=\frac{Ce^{kx}}{F(k)} .
> $$

The result is immediate from the trial $Ae^{kx}$, since every derivative reproduces $e^{kx}$ and the left-hand side becomes $A F(k)e^{kx}$. Its exam value is speed: for a non-resonant exponential the particular integral can be written down in one line, and the two marks are for the correct evaluation of $F(k)$ and for the division.

Two cautions. The rule applies only when $F(k)\ne 0$; if $F(k)=0$ the denominator vanishes and the factor $x$ is required. And the rule applies to a pure exponential, not to a product such as $xe^{kx}$, for which the trial must carry a linear factor.

### 2.3 High-yield result 3: the multiplicity rule

> **Theorem (multiplicity rule, worth 4 marks).** Let $Q(x)=e^{\alpha x}\left(P(x)\cos\beta x+R(x)\sin\beta x\right)$ with $\deg P,\deg R\le m$, put $\mu=\alpha+i\beta$, and let $s$ be the multiplicity of $\mu$ as a characteristic root. Then the trial
>
> $$
> y_{p}=x^{s}e^{\alpha x}\left(A(x)\cos\beta x+B(x)\sin\beta x\right),
> $$
>
> with $A$ and $B$ of degree at most $m$, contains exactly the right number of unknown coefficients, and they are determined uniquely.

The proof in examination form has three sentences. Factor the operator as $F(D)=(D-\mu)^{s}G(D)$ with $G(\mu)\ne 0$, and apply the exponential shift to $x^{s}e^{\mu x}v$ to obtain $e^{\mu x}D^{s}G(D+\mu)\left[x^{s}v\right]$. On polynomials of degree at most $m$ the operator $D^{s}G(D+\mu)$ is upper triangular with diagonal entries $G(\mu)(s+j)!/j!$, which are nonzero, so it is invertible and the coefficients exist and are unique. The three sentences carry four marks: the factorisation, the shift, the triangularity with nonzero diagonal, and the conclusion.

### 2.4 High-yield result 4: trigonometric pairing

> **Lemma (pairing, worth 3 marks).** The operator $F(D)$ maps the space spanned by $\cos\beta x$ and $\sin\beta x$ into itself, and the trial for a forcing term containing either function must contain both.

The lemma explains a rule that is otherwise arbitrary. Differentiating a cosine produces a sine, and differentiating a sine produces a cosine with a minus sign, so the two functions are coupled and cannot be separated. A trial containing only a cosine therefore generates a sine on the left-hand side that has nothing to match it, and the coefficient of that sine is forced to zero, which is generally impossible.

The marking point is the presence of both functions in the trial. A candidate who writes only $A\cos\beta x$ for a cosine forcing term loses the trial mark even if the rest of the work is competent.

The same pairing applies when the forcing term is a product: $e^{\alpha x}x\cos\beta x$ requires both $e^{\alpha x}\left(Ax+B\right)\cos\beta x$ and $e^{\alpha x}\left(Cx+D\right)\sin\beta x$, with independent polynomial coefficients.

### 2.5 High-yield result 5: superposition over a sum

> **Theorem (superposition, worth 2 marks).** If $L[y_{1}]=Q_{1}$ and $L[y_{2}]=Q_{2}$ then $L[y_{1}+y_{2}]=Q_{1}+Q_{2}$.

For a forcing term that is a sum, the examination route is to find a particular integral for each piece separately, using a separate index of duplication for each, and then to add. The marks are for splitting the right-hand side, for correct indices, and for adding.

The error to avoid is computing one index for the whole sum. A forcing term such as $e^{2x}+\sin 3x$ has two different values of $\mu$, namely $2$ and $3i$, and each must be tested separately.

### 2.6 High-yield result 6: the operator formula

> **Theorem (inverse operator, worth 3 marks).** For a constant $a$,
>
> $$
> \frac{1}{D-a}Q=e^{ax}\int e^{-ax}Q(x)\,dx .
> $$

The derivation is a first-order integrating factor. From $u'-au=Q$, multiply by $e^{-ax}$ to obtain the exact derivative $\left(ue^{-ax}\right)'=Qe^{-ax}$, and integrate. For a repeated application,

$$
\frac{1}{(D-a)(D-b)}Q=\frac{1}{D-a}\left(\frac{1}{D-b}Q\right),
$$

the order being immaterial because constant-coefficient operators commute.

The formula is examined in two ways. It may be asked directly, as $\frac{1}{D-a}Q$ for a specified $Q$, in which case two integrations are performed. Or it may be used as a check on the undetermined-coefficients answer, since both routes must agree. For the operator $(D-1)(D-2)$ acting on $e^{5x}$ the formula gives

$$
\frac{e^{5x}}{3}\ \text{after the first stage, and}\ \frac{e^{5x}}{12}\ \text{after the second,}
$$

in agreement with the cover-up value $e^{5x}/F(5)=e^{5x}/12$.

### 2.7 Results at a glance

| Result | Statement | Marks | When it is used |
| --- | --- | --- | --- |
| Structure theorem | $y=y_{c}+y_{p}$ | 3 | Every solution; sometimes asked as bookwork |
| Cover-up rule | $y_{p}=Ce^{kx}/F(k)$ when $F(k)\ne 0$ | 2 | Pure exponential forcing, no duplication |
| Multiplicity rule | trial $=x^{s}\times$ tabulated shape | 4 | Every forcing term; marks for the index $s$ |
| Pairing lemma | cosine and sine always together | 3 | Any trigonometric forcing term |
| Superposition | sums handled piece by piece | 2 | Forcing terms with several parts |
| Inverse operator | $\frac{1}{D-a}Q=e^{ax}\int e^{-ax}Q\,dx$ | 3 | Operator-form questions and checks |
| Secular growth | resonant forcing produces a factor $x$ | 2 | Explanation questions on resonance |

### 2.8 What these results do not say

The results above are frequently over-applied, and the examiner tests the over-application as often as the application.

The cover-up rule does not apply when $F(k)=0$, and quoting it then produces a division by zero that costs both the marks for the rule and the marks for the trial.

The multiplicity rule does not say that the trial may be shortened when some coefficient turns out to be zero. The trial must contain every power up to the degree of the forcing polynomial, even if the final value of one coefficient is zero.

Superposition does not say that a sum may be handled with one trial. Each piece has its own index, and mixing them produces a trial with the wrong number of unknown coefficients.

The structure theorem does not say that a particular integral is unique. Any particular integral may be used, and the general solution is the same family in every case, because the difference is absorbed into the complementary function.

Finally, none of these results says anything about forcing terms outside the catalogue. A question involving $\sec x$ or $\ln x$ is not answered by a trial, and the correct response is to say so and to name the method that would apply.

## 3. Formal Proofs, Derivations, and Methods

### 3.1 The examination algorithm in nine lines

Every solution in this topic is produced by the same nine lines. Each line earns marks, and none may be omitted.

1. State the auxiliary equation $a_{0}m^{2}+a_{1}m+a_{2}=0$ and solve it.
2. Write the complementary function in the correct form, naming the constants $c_{1}$ and $c_{2}$.
3. Read $\alpha$ and $\beta$ from the forcing term and form $\mu=\alpha+i\beta$.
4. Compare $\mu$ with the roots and record the multiplicity $s$, adding the words "which is a root of multiplicity $s$" so the examiner can see the decision.
5. Write the trial, multiplied by $x^{s}$, with every coefficient displayed.
6. Differentiate twice, keeping any exponential factor outside the bracket.
7. Substitute, collect, and equate coefficients; write the coefficient equations explicitly.
8. Solve the equations and state the particular integral on its own line.
9. Write $y=y_{c}+y_{p}$, and if conditions are given, impose them and solve for the constants.

Line 4 is the one that candidates skip, and it is worth explicit marks. Line 7 is the one where algebra is lost, and writing the equations down separately protects against it.

### 3.2 Reading the index of duplication without error

Three tests decide $s$, and each has a trap attached.

**Test one, the exponential rate.** For a forcing term $e^{kx}$ the test is against the real number $k$. If $k$ equals a simple root, then $s=1$; if it equals a repeated root, then $s=2$; otherwise $s=0$. The trap is to compare $k$ with the modulus of a complex root, which is meaningless; a forcing term $e^{2x}$ is not resonant with roots $\pm 2i$.

**Test two, the frequency.** For a forcing term $\cos\beta x$ or $\sin\beta x$ the test is against the pair $\pm i\beta$. Resonance occurs exactly when $i\beta$ is a root, which happens when the characteristic roots are purely imaginary with modulus $\beta$, that is when $a_{1}=0$ and $\beta^{2}=\frac{a_{2}}{a_{0}}$. A forcing term $\sin 2x$ is therefore resonant with $y''+4y=0$ but not with $y''+2y'+5y=0$, whose roots are $-1\pm 2i$.

**Test three, the constant term.** A polynomial forcing term has $\mu=0$, so it is resonant exactly when $0$ is a characteristic root, which happens exactly when $a_{2}=0$. This is the trap that catches the largest number of candidates, because the forcing term contains no exponential and the factor $x$ seems unmotivated. The test is mechanical: look at $a_{2}$. If $a_{2}=0$, multiply the polynomial trial by $x$.

A worked illustration of the third trap. For

$$
y''-2y'=x+1
$$

the auxiliary equation is $m^{2}-2m=m\left(m-2\right)=0$, so the roots are $0$ and $2$. Since $\mu=0$ is a simple root, the trial is not $ax+b$ but $x\left(ax+b\right)=ax^{2}+bx$. Substituting gives

$$
2a-2\left(2ax+b\right)=-4ax+\left(2a-2b\right),
$$

and matching against $x+1$ gives $a=-\frac{1}{4}$ and $b=-\frac{3}{4}$, so the particular integral is

$$
y_{p}=-\frac{x^{2}}{4}-\frac{3x}{4}.
$$

Had the trial $ax+b$ been used, the left-hand side would have been the constant $-2a$, which cannot equal $x+1$; the symptom would have been an inconsistent equation, not a zero left-hand side.

### 3.3 Why the factor $x$ appears, in examination language

The explanation question is worth two or three marks and is answered in three sentences.

Write $F(D)=(D-\mu)^{s}G(D)$ with $G(\mu)\ne 0$. If a trial of the tabulated shape without the factor $x$ is substituted, the exponential shift produces the operator $D^{s}$ applied to a polynomial, so a term of the complementary function is produced and the left-hand side loses the degree of freedom that the forcing term needs. Multiplying by $x^{s}$ raises the degree by exactly $s$, restoring invertibility. In the pure exponential case with $m=0$ the effect is total: the naive trial is annihilated, the equation reads $0=Q$, and the factor $x$ is the only remedy.

The two failure symptoms should be named, because a marker looks for them.

The first symptom is collapse. Substituting the trial gives zero and the equation reads $0=Q$, which happens when the forcing term is a pure exponential, sine or cosine that duplicates a natural solution.

The second symptom is a singular or inconsistent system. The trial produces a result of too low a degree, so one coefficient equation contradicts another, which happens when the forcing term is a polynomial, or a polynomial multiplied by a natural exponential.

A trial with too many factors of $x$ fails by a third symptom: the left-hand side produces shapes absent from the forcing term, such as $x^{3}e^{2x}$ or $x^{2}$, and matching them forces a coefficient to vanish in contradiction with the remaining equations.

### 3.4 Matching coefficients without losing algebra

Four habits keep the algebra under control.

Keep the exponential or the trigonometric factor outside a single bracket, so that the equation reduces to an identity between polynomials or between a cosine and a sine. The factor can then be divided out, and the comparison is made on the bracket alone.

Differentiate before substituting, never after, and differentiate a factored form rather than an expanded one. For $y=\left(ax+b\right)e^{3x}$ the derivative $\left(3ax+a+3b\right)e^{3x}$ is obtained in one line; expanding first produces four terms and two chances of error.

Collect the left-hand side by shape rather than by power. For a polynomial forcing term the shapes are $1$, $x$, $x^{2}$; for a trigonometric forcing term they are $\cos\beta x$ and $\sin\beta x$; for a product they are $x^{k}e^{\alpha x}\cos\beta x$ and $x^{k}e^{\alpha x}\sin\beta x$.

Audit the answer by substituting one convenient value of $x$ into the identity obtained in the previous step. For a polynomial identity this catches almost every arithmetic slip in a few seconds, and it costs less than redoing the differentiation.

### 3.5 Applying initial conditions efficiently

Write the complete solution, differentiate it once, and only then substitute $x=x_{0}$. Doing so produces two linear equations in $c_{1}$ and $c_{2}$.

The efficient route is to compute the values of $y_{c}$ and $y_{p}$ and their derivatives at $x_{0}$ first, then move the $y_{p}$ values to the right-hand side. The system then has the form

$$
c_{1}y_{1}\left(x_{0}\right)+c_{2}y_{2}\left(x_{0}\right)=y_{0}-y_{p}\left(x_{0}\right),
$$

$$
c_{1}y_{1}'\left(x_{0}\right)+c_{2}y_{2}'\left(x_{0}\right)=v_{0}-y_{p}'\left(x_{0}\right),
$$

whose determinant is the Wronskian at $x_{0}$ and is therefore nonzero. Solving by elimination is faster than by substitution when the exponentials are all equal to one at $x_{0}$, which is the usual case because the conditions are normally given at $x=0$.

The audit is a substitution of the finished answer into both conditions. Two correct values, together with a verified particular integral, leave nothing that can be wrong.

### 3.6 Verification in fifteen seconds

Verification of the particular integral is performed on the collected form, not from scratch. Take the bracket obtained after substitution and check that it reproduces the forcing term.

Three quick audits supplement it. If the forcing term is a constant, the answer's forced part must be that constant divided by $a_{2}$, provided $a_{2}\ne 0$. If the forcing term is $Ce^{kx}$ and $F(k)\ne 0$, the forced part must be $Ce^{kx}/F(k)$. If the forcing term is a polynomial of degree $m$ and $a_{2}\ne 0$, the forced part must be a polynomial of degree $m$ whose leading coefficient is the forcing coefficient divided by $a_{2}$.

Each audit takes seconds and each detects a whole class of errors.

### 3.7 The trap table

The following table lists the errors that the marking schemes penalise most heavily, with the symptom that reveals each one.

| Trap | Why it happens | How to spot it | Correct move |
| --- | --- | --- | --- |
| No factor $x$ although the forcing duplicates a natural solution | The duplication is not checked before the trial is written | Substitution gives $0=Q$, or the coefficient system is inconsistent | Compute $\mu$ and $s$ first; multiply the trial by $x^{s}$ |
| Factor $x$ although there is no duplication | The forcing rate is confused with the modulus of a complex root | A coefficient is forced to zero in contradiction with another equation | Compare the exact value $\mu=\alpha+i\beta$ with the roots |
| Polynomial trial truncated | The constant or linear term is thought unnecessary | One power appears on the left but not on the right | Carry every power up to the degree of the forcing polynomial |
| Polynomial trial not multiplied by $x$ when $a_{2}=0$ | The forcing term contains no exponential, so no duplication is expected | The left-hand side has degree lower than the forcing polynomial | Test whether $0$ is a root, that is whether $a_{2}=0$ |
| Only a cosine in the trial for a cosine forcing term | The two functions are treated as independent | An unmatched sine appears after substitution | Always pair $\cos\beta x$ with $\sin\beta x$ |
| One index $s$ for a sum of forcing terms | Superposition is applied to the trial rather than to the particular integrals | One piece verifies, the other does not | Split the sum and use one index per piece |
| Conditions applied to $y_{p}$ alone | The particular integral is mistaken for the solution | The conditions hold but the equation fails, or the reverse | Assemble $y=y_{c}+y_{p}$ first |
| Sign of a repeated root lost | The factor $x$ is dropped from a repeated root | The complementary function contains only one independent term | Write $\left(c_{1}+c_{2}x\right)e^{mx}$ for a repeated root |
| Forgetting the exponential factor $e^{\alpha x}$ for complex roots | Complex roots are treated as purely imaginary | The complementary function does not match the roots | Include $e^{\alpha x}$ whenever the real part is nonzero |
| Cover-up rule used when $F(k)=0$ | The rule is memorised without its hypothesis | A division by zero appears | Use the factor $x$ instead |
| Operator question treated as a fraction | $1/(D-a)$ is read as an algebraic reciprocal | The answer contains no integral | Use $e^{ax}\int e^{-ax}Q\,dx$ |

### 3.8 Time allocation

The topic is worth between eight and fifteen marks, and the time should be allocated in proportion. Eight minutes for a single-forcing-term problem with no duplication, ten for a resonant one, twelve for a product or a sum, and fourteen for an initial value problem. Reserve the last ninety seconds of each question for the verification audits of Section 3.6, because a verified answer is worth more than an extra line of prose.

If time is short, the order of priority is: roots and complementary function, then the trial shape, then the general solution, then the coefficients. The first two attract marks even when the algebra is unfinished, whereas a perfect coefficient computation attached to a wrong trial attracts nothing.

## 4. Representative Worked Examples and Solutions

### 4.1 Problem: non-resonant exponential forcing (12 marks)

Solve $y''-3y'+2y=e^{5x}$.

### 4.2 Solution: cover-up route with full verification

Step 1 (2 marks). State and solve the auxiliary equation.

$$
m^{2}-3m+2=(m-1)(m-2)=0, \qquad m=1,\quad m=2
$$

Step 2 (2 marks). Write the complementary function for distinct real roots.

$$
y_{c}=c_{1}e^{x}+c_{2}e^{2x}
$$

Step 3 (2 marks). Read $\mu=5$ and compare with the roots. Since $5$ is not a root, $s=0$, and the trial is a single exponential. Evaluate the operator at $5$.

$$
F(5)=25-15+2=12, \qquad y_{p}=Ae^{5x}
$$

Step 4 (2 marks). Substitute. Every derivative of $Ae^{5x}$ contributes a factor $5$, so the left-hand side is $F(5)y_{p}$.

$$
25Ae^{5x}-15Ae^{5x}+2Ae^{5x}=12Ae^{5x}
$$

Step 5 (2 marks). Equate coefficients and solve.

$$
12A=1, \qquad A=\frac{1}{12}
$$

Step 6 (1 mark). State the general solution.

$$
y=c_{1}e^{x}+c_{2}e^{2x}+\frac{1}{12}e^{5x}
$$

Step 7 (1 mark). Verify: substituting $y_{p}$ returns $12\cdot\frac{1}{12}e^{5x}=e^{5x}$, which is the forcing term. Interpretation: the forced term dominates for large $x$ because $e^{5x}$ grows faster than either natural mode.

### 4.3 Problem: polynomial forcing (13 marks)

Solve $y''+5y'+4y=3-2x$.

### 4.4 Solution: linear trial and two coefficient equations

Step 1 (2 marks). State and solve the auxiliary equation.

$$
m^{2}+5m+4=(m+1)(m+4)=0, \qquad m=-1,\quad m=-4
$$

Step 2 (2 marks). Write the complementary function.

$$
y_{c}=c_{1}e^{-x}+c_{2}e^{-4x}
$$

Step 3 (2 marks). Here $\alpha=0$ and $\beta=0$, so $\mu=0$. Since $a_{2}=4\ne 0$, zero is not a root, so $s=0$ and the trial is linear rather than multiplied by $x$.

$$
y=ax+b, \qquad y'=a, \qquad y''=0
$$

Step 4 (2 marks). Substitute and collect by powers of $x$. The second derivative contributes nothing because the trial is linear.

$$
0+5a+4\left(ax+b\right)=4ax+\left(5a+4b\right)
$$

Step 5 (3 marks). Equate the coefficient of $x$ and the constant term separately.

$$
4a=-2, \qquad 5a+4b=3
$$

Solving: $a=-\frac{1}{2}$ and $4b=3+\frac{5}{2}=\frac{11}{2}$, so $b=\frac{11}{8}$.

Step 6 (1 mark). State the general solution.

$$
y=c_{1}e^{-x}+c_{2}e^{-4x}-\frac{x}{2}+\frac{11}{8}
$$

Step 7 (1 mark). Verify by substitution: $0+5\left(-\frac{1}{2}\right)+4\left(-\frac{x}{2}+\frac{11}{8}\right)=-2x-\frac{5}{2}+\frac{11}{2}=3-2x$, which is the forcing term.

### 4.5 Problem: resonant trigonometric forcing with initial conditions (15 marks)

Solve $y''+4y=\sin 2x$ subject to $y(0)=0$ and $y'(0)=0$.

### 4.6 Solution: factor $x$, then two conditions

Step 1 (2 marks). State and solve the auxiliary equation.

$$
m^{2}+4=0, \qquad m=\pm 2i
$$

Step 2 (1 mark but essential). Write the complementary function and record the duplication, since $\mu=2i$ is a simple root.

$$
y_{c}=c_{1}\cos 2x+c_{2}\sin 2x, \qquad s=1
$$

Step 3 (2 marks). Write the trial with both basis functions and the factor $x$.

$$
y=x\left(A\cos 2x+B\sin 2x\right)
$$

Step 4 (2 marks). Differentiate twice, collecting the terms with and without a factor $x$.

$$
y'=\left(A\cos 2x+B\sin 2x\right)+x\left(-2A\sin 2x+2B\cos 2x\right)
$$

$$
y''=\left(-4A\sin 2x+4B\cos 2x\right)+x\left(-4A\cos 2x-4B\sin 2x\right)
$$

Step 5 (2 marks). Substitute. The terms carrying $x$ cancel against $4y$ identically, because $x\left(A\cos 2x+B\sin 2x\right)$ is a natural solution.

$$
y''+4y=-4A\sin 2x+4B\cos 2x
$$

Step 6 (2 marks). Equate the sine and cosine coefficients against the forcing term $\sin 2x$.

$$
-4A=1, \qquad 4B=0, \qquad A=-\frac{1}{4}, \quad B=0
$$

Step 7 (1 mark). State the general solution.

$$
y=c_{1}\cos 2x+c_{2}\sin 2x-\frac{x}{4}\cos 2x
$$

Step 8 (3 marks). Impose the two conditions on the complete solution. The first gives $c_{1}=0$ directly.

$$
y(0)=c_{1}=0
$$

Differentiate the complete solution and evaluate at zero.

$$
y'=-2c_{1}\sin 2x+2c_{2}\cos 2x-\frac{1}{4}\cos 2x+\frac{x}{2}\sin 2x, \qquad y'(0)=2c_{2}-\frac{1}{4}
$$

Setting the derivative to zero gives $c_{2}=\frac{1}{8}$, so the solution of the initial value problem is

$$
y=\frac{1}{8}\sin 2x-\frac{x}{4}\cos 2x .
$$

Verification: at $x=0$ the value is $0$ and the derivative is $\frac{1}{4}-\frac{1}{4}=0$, so both conditions hold, and the particular integral was verified in Step 5.

### 4.7 Problem: resonant exponential-trigonometric forcing (13 marks)

Solve $y''-2y'+5y=e^{x}\cos 2x$.

### 4.8 Solution: resonance at a complex root

Step 1 (2 marks). State and solve the auxiliary equation, using the quadratic formula.

$$
m^{2}-2m+5=0, \qquad m=\frac{2\pm\sqrt{4-20}}{2}=1\pm 2i
$$

Step 2 (1 mark). Write the complementary function and record the duplication: $\mu=1+2i$ is a simple root.

$$
y_{c}=e^{x}\left(c_{1}\cos 2x+c_{2}\sin 2x\right), \qquad s=1
$$

Step 3 (2 marks). Write the trial, with both basis functions, the factor $x$ and the exponential factor.

$$
y=xe^{x}\left(A\cos 2x+B\sin 2x\right)
$$

Step 4 (3 marks). Differentiate. Write $u=A\cos 2x+B\sin 2x$ and $w=xu$, so that $y=e^{x}w$ and the derivatives are combinations of $w$, $w'$ and $w''$.

$$
y'=e^{x}\left(w+w'\right), \qquad y''=e^{x}\left(w+2w'+w''\right)
$$

Step 5 (2 marks). Substitute. The terms in $w'$ cancel between $y''$ and $-2y'$, leaving an expression involving $w''$ and $w$ only.

$$
y''-2y'+5y=e^{x}\left(w''+4w\right)
$$

Since $w=xu$ and $u''=-4u$, we have $w''+4w=2u'+xu''+4xu=2u'$, so

$$
y''-2y'+5y=2e^{x}u'=e^{x}\left(-4A\sin 2x+4B\cos 2x\right)
$$

Step 6 (2 marks). Equate coefficients against $e^{x}\cos 2x$.

$$
-4A=0, \qquad 4B=1, \qquad A=0, \quad B=\frac{1}{4}
$$

Step 7 (1 mark). State the general solution.

$$
y=e^{x}\left(c_{1}\cos 2x+c_{2}\sin 2x\right)+\frac{x}{4}e^{x}\sin 2x
$$

Verification: with $A=0$ and $B=\frac{1}{4}$ the collected form of Step 5 gives $4\cdot\frac{1}{4}e^{x}\cos 2x=e^{x}\cos 2x$, as required.

### 4.9 Problem: product forcing with duplication (13 marks)

Solve $y''-4y=xe^{2x}$.

### 4.10 Solution: shifted polynomial trial

Step 1 (2 marks). State and solve the auxiliary equation.

$$
m^{2}-4=0, \qquad m=2,\quad m=-2
$$

Step 2 (1 mark). Record the duplication: $\mu=2$ is a simple root, so $s=1$.

$$
y_{c}=c_{1}e^{2x}+c_{2}e^{-2x}, \qquad s=1
$$

Step 3 (3 marks). Since $s=1$ and the forcing polynomial has degree one, the trial is a quadratic factor multiplying the exponential. The full factor is required: a trial $ax^{2}e^{2x}$ alone would leave a residual multiple of $e^{2x}$.

$$
y=\left(ax^{2}+bx\right)e^{2x}
$$

$$
y'=\left(2ax^{2}+\left(2a+2b\right)x+b\right)e^{2x}
$$

$$
y''=\left(4ax^{2}+\left(8a+4b\right)x+2a+4b\right)e^{2x}
$$

Step 4 (2 marks). Subtract $4y$ and collect.

$$
e^{2x}\left[\left(4ax^{2}+\left(8a+4b\right)x+2a+4b\right)-\left(4ax^{2}+4bx\right)\right]=e^{2x}\left(8ax+2a+4b\right)
$$

Step 5 (3 marks). Equate coefficients against $xe^{2x}$.

$$
8a=1, \qquad 2a+4b=0, \qquad a=\frac{1}{8}, \quad b=-\frac{1}{16}
$$

Step 6 (1 mark). State the general solution.

$$
y=c_{1}e^{2x}+c_{2}e^{-2x}+\left(\frac{x^{2}}{8}-\frac{x}{16}\right)e^{2x}
$$

Step 7 (1 mark). Verify: the bracket of Step 4 with these values is $x+0$, so the left-hand side is $xe^{2x}$. Note that the term $-\frac{x}{16}e^{2x}$ cannot be dropped: it is part of the particular integral, since $xe^{2x}$ is not a solution of the homogeneous equation. Only the coefficients of the homogeneous terms $e^{2x}$ and $e^{-2x}$ are free.

### 4.11 Problem: product forcing without duplication (14 marks)

Solve $y''+9y=x\cos x$.

### 4.12 Solution: two polynomial factors

Step 1 (2 marks). State and solve the auxiliary equation.

$$
m^{2}+9=0, \qquad m=\pm 3i
$$

Step 2 (1 mark). Here $\mu=i$, which is not a root, so $s=0$; the forcing frequency $1$ differs from the natural frequency $3$.

$$
y_{c}=c_{1}\cos 3x+c_{2}\sin 3x, \qquad s=0
$$

Step 3 (2 marks). The trial carries a linear factor in front of each basis function, because the forcing term is a product of a linear expression with a cosine.

$$
y=\left(ax+b\right)\cos x+\left(cx+d\right)\sin x
$$

Step 4 (3 marks). Differentiate twice.

$$
y'=\left(a+cx+d\right)\cos x+\left(c-ax-b\right)\sin x
$$

$$
y''=\left(2c-ax-b\right)\cos x+\left(-2a-cx-d\right)\sin x
$$

Step 5 (2 marks). Add $9y$ and collect by the two shapes.

$$
y''+9y=\left(8ax+8b+2c\right)\cos x+\left(8cx+8d-2a\right)\sin x
$$

Step 6 (3 marks). Equate coefficients against $x\cos x$, that is against $1\cdot x\cos x+0\cdot\cos x+0\cdot x\sin x+0\cdot\sin x$.

$$
8a=1, \qquad 8b+2c=0, \qquad 8c=0, \qquad 8d-2a=0
$$

Solving in order: $a=\frac{1}{8}$, $c=0$, $b=0$, $d=\frac{1}{32}$.

Step 7 (1 mark). State the general solution.

$$
y=c_{1}\cos 3x+c_{2}\sin 3x+\frac{x}{8}\cos x+\frac{1}{32}\sin x
$$

Verification: substituting $a=\frac{1}{8}$, $b=c=0$, $d=\frac{1}{32}$ into the collected form of Step 5 gives $x\cos x+0\cdot\cos x+0\cdot\sin x$, which is the forcing term.

## 5. Mathematical Extensions, Limits, and Common Errors

### 5.1 Where the marks are actually lost

A review of typical scripts shows that failures cluster in five places, and each has a preventive routine.

| Loss | Frequency | Preventive routine |
| --- | --- | --- |
| Wrong complementary function form | Very common | Write the roots as a pair first, then the form; check the repeated and complex cases explicitly |
| Missing factor $x$ | Very common | Compute $\mu$ and $s$ in a separate line before writing the trial |
| Factor $x$ added without duplication | Common | Apply the test on the exact value of $\mu$, not on its modulus |
| Truncated polynomial trial | Common | Write the trial to the same degree as the forcing polynomial, then check that no power is missing |
| Arithmetic slip in the coefficient equations | Very common | Write the coefficient equations on separate lines and audit one value of $x$ |
| Conditions applied to the wrong function | Occasional | Assemble $y=y_{c}+y_{p}$ and differentiate that, never the particular integral |
| No verification | Occasional | Reserve ninety seconds for the substitution check |

The pattern is clear. Almost none of the losses come from misunderstanding the theory; they come from skipping the two decisions that the theory requires, namely the form of the complementary function and the multiplicity of $\mu$. Both decisions take a single line, and both should be written down rather than performed mentally.

### 5.2 The revision checklist

The following checklist is arranged in the order in which the ideas are used. A candidate who can tick every item is ready for any question in this topic.

- The standard form and the condition $a_{0}\ne 0$, word for word.
- The three root patterns and the complementary function belonging to each, including the factor $x$ for a repeated root and the factor $e^{\alpha x}$ for complex roots.
- The definition of a particular integral as any function satisfying the equation, with no constants.
- The statement and proof of the structure theorem in three lines.
- The complete trial table, read through $\mu=\alpha+i\beta$ and the multiplicity $s$.
- The three tests for duplication: on the exponential rate, on the frequency, and on the constant term when $a_{2}=0$.
- The two failure symptoms of an insufficient factor $x$, and the symptom of an excessive one.
- The pairing rule for sine and cosine, including products.
- Superposition for a sum, with one index per piece.
- The cover-up rule and its hypothesis $F(k)\ne 0$.
- The inverse operator formula and its two-stage use.
- The initial condition procedure, including moving the $y_{p}$ values to the right-hand side.
- The three quick audits of Section 3.6.
- The interpretation of a resonant answer as unbounded growth on the timescale of the model.

### 5.3 Time strategy

A paper rarely contains only this topic, so the strategy has to be integrated with the rest. A workable plan for a fifteen-mark question is the following.

Spend the first minute reading the forcing term and deciding the index of duplication. This decision determines everything else and costs almost no time. Spend the next two minutes on the auxiliary equation and the complementary function; those are the marks that survive even if the algebra later goes wrong. Spend the next six minutes on the trial, the differentiation, the substitution, and the coefficient equations, writing each stage on its own line. Spend the next three minutes on the conditions if they are given, and the last three minutes on the verification and on a reread of the question for any part that has been overlooked.

Three timing rules follow from the mark distribution.

The first is never to begin the trial before the roots are written, because the trial depends on them and a restart costs more than the delay.

The second is to abandon a coefficient computation that has gone inconsistent only after checking the trial, since an inconsistent system is usually a symptom of the wrong trial rather than of wrong arithmetic. If the trial is right and the system is inconsistent, an arithmetic slip has occurred, and restarting the substitution is faster than hunting for it.

The third is to keep the verification short. A full re-derivation doubles the time for no extra marks; the audits of Section 3.6 take seconds and catch the errors that actually occur.

### 5.4 The last five minutes

Four checks repay their cost when the clock is short.

Check that the number of arbitrary constants is exactly two, and that neither appears in the forced part. Check that the forced part has the shape of the forcing term, with at most a factor $x$ and a different degree only where a factor $x$ accounts for it. Check the sign of the coefficient in a resonant answer, since the most common arithmetic error in the duplication case is a lost minus sign. Check the two initial values by substitution if conditions were given.

If only one check can be made, make the substitution check on the particular integral, because it validates the largest block of marks.

### 5.5 The limits of the method, in one paragraph

The method applies exactly when the forcing term is annihilated by a polynomial in $D$ with constant coefficients, which is to say when the forcing term is built from polynomials, exponentials and sines and cosines by addition and multiplication. Outside that class the trial cannot close, and the appropriate technique is variation of parameters, which preserves the structure $y=y_{c}+y_{p}$ but replaces the constants by functions and produces integrals that are frequently not elementary. The structure theorem is therefore universal, while the trial table is not; an examiner who asks about a forcing term such as $\sec x$ is testing whether the candidate knows the difference.

A second limit is physical rather than mathematical. A resonant particular integral predicts growth proportional to $x$, which cannot continue indefinitely in any real system, because damping and nonlinear effects intervene. The correct reading is that the factor $x$ describes the response on a timescale short compared with the time over which those effects become important, and an answer that states this shows understanding beyond the algebra.

### 5.6 Consolidated summary

The topic has one idea, one table and one procedure.

The idea is that the solution set is an affine translate of the homogeneous solution space, so every solution is a complementary function plus one particular integral, and the two constants live entirely in the complementary function.

The table gives the trial for each forcing shape, with the index of duplication $s$ equal to the multiplicity of $\mu=\alpha+i\beta$ among the characteristic roots, and the trial multiplied by $x^{s}$.

The procedure is the nine-line algorithm of Section 3.1, followed by the three audits of Section 3.6. Every mark in the topic is attached to one of those lines, and every line is mechanical. The only decisions are the form of the complementary function and the value of $s$, and both are decided in a single line that should always be written down.
