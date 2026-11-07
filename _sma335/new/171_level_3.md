## 1. Foundational Concepts, Definitions, and Axioms

### 1.1 What this topic is worth, and why it is examined first

This topic supplies the vocabulary that every later differential-equations question assumes. It is almost always examined in the opening section of a paper, it is almost always worth between eight and fifteen marks in total, and it is almost always the cheapest scoring opportunity on the paper. The questions are short, the definitions are fixed, and the computations are one or two differentiations long. Marks are lost here for three reasons only: a definition quoted imprecisely, a degree reported before radicals were cleared, and a constant of integration that has gone missing.

The distribution of marks across the standard question types is worth memorising, because it dictates how much writing each part deserves.

| Question type | Typical marks | Typical time | Where the marks sit |
| --- | --- | --- | --- |
| State the order and degree of a given equation | 2 to 3 | 2 minutes | One for order, one for degree, one for clearing a radical |
| Show that a given function is a solution | 3 to 4 | 4 minutes | Two for the derivatives, one for substitution, one for the conclusion |
| Form the differential equation of a given family | 3 to 6 | 5 minutes | One per constant, one for the elimination, one for the order check |
| Solve a directly integrable equation with conditions | 4 to 6 | 5 minutes | One per integration, one per condition, one for verification |
| Solve a separable equation with a condition | 5 to 7 | 7 minutes | Separation, integration, constant, condition, explicit form, verification |
| Explain why a degree does not exist | 1 to 2 | 1 minute | The reason, not the arithmetic |
| Distinguish general from particular solution | 2 | 2 minutes | One for each definition, one for the link to the constants |

The pattern in that table is the single most useful fact in this note. Every mark on this topic is attached either to a definition stated correctly or to one differentiation or integration performed correctly. There is no clever insight required. Precision is the whole examination technique.

### 1.2 The seven definitions to reproduce exactly

Definitions on this topic are marked as bookwork, which means they are awarded for the exact content and not for a paraphrase that merely gestures at the idea. The following wordings are safe to use.

> **Definition (Ordinary differential equation).** An ordinary differential equation is an equation containing one or more ordinary derivatives of an unknown function of a single independent variable.

Marking note: the phrase single independent variable must appear, or an equivalent such as one independent variable. Writing only "an equation containing derivatives" earns nothing, because it does not distinguish the ordinary case from the partial case.

> **Definition (Partial differential equation).** A partial differential equation is an equation containing one or more partial derivatives of an unknown function of two or more independent variables.

Marking note: the phrase two or more independent variables is the marking point. A partial derivative with respect to one variable of a function of one variable would still be an ordinary derivative.

> **Definition (Order).** The order of a differential equation is the order of the highest derivative appearing in it.

Marking note: highest derivative, not highest power. Candidates who write "the highest power of the derivative" have confused order with degree and typically lose both marks on the question.

> **Definition (Degree).** The degree of a differential equation is the power to which the highest-order derivative is raised after the equation has been cleared of radicals and of fractional powers in the derivatives.

Marking note: the qualifier after the comma is a separate marking point on most schemes. It is also the sentence that makes the whole definition true, since without it the degree of an equation such as $\sqrt{1+\left(\frac{dy}{dx}\right)^{2}}=2x$ would be ambiguous.

> **Definition (Solution).** A function $y=\phi(x)$ is a solution of a differential equation on an interval if substituting the function and its derivatives into the equation produces an identity on that interval.

Marking note: identity, or for all $x$ in the interval, is the marking word. A solution is not "a value that works".

> **Definition (General solution).** The general solution of an equation of order $n$ is the family of all solutions on the interval, parametrised by $n$ independent arbitrary constants.

> **Definition (Particular solution).** A particular solution is a single member of the general solution, obtained by assigning specific values to the arbitrary constants.

Marking note: the pair is usually worth two marks, and the examiner is looking for the words arbitrary constants and the number $n$ in the first, and the words specific values in the second.

### 1.3 The derivative ladder and the notation the examiner expects

The symbol $\frac{d}{dx}$ is an operator: it means differentiate with respect to $x$ whatever follows it. Repeated application is recorded by a raised index on both the $d$ and the $dx$.

$$
\frac{dy}{dx}=y', \qquad \frac{d^{2}y}{dx^{2}}=\frac{d}{dx}\left(\frac{dy}{dx}\right)=y'', \qquad \frac{d^{n}y}{dx^{n}}=\frac{d}{dx}\left(\frac{d^{n-1}y}{dx^{n-1}}\right)=y^{(n)}
$$

Three conventions govern the notation and are worth stating in an answer whenever a definition question mentions derivatives.

The first is that beyond the third derivative the dash notation becomes unreadable, so $y^{(4)}$, $y^{(5)}$ and $y^{(n)}$ are used. The bracketed index counts differentiations; it is not a power, and writing $y^{4}$ for the fourth derivative is an error that loses a mark and changes the meaning entirely.

The second is that the raised indices in $\frac{d^{n}y}{dx^{n}}$ are bookkeeping, not algebra. The denominator $dx^{2}$ records two differentiations with respect to $x$; it is not the square of a quantity $dx$. The whole symbol $\frac{dy}{dx}$ denotes a derivative, and while identities such as $\frac{dy}{dx}=\frac{dy}{du}\cdot\frac{du}{dx}$ are valid consequences of the chain rule, treating $\frac{dy}{dx}$ as a ratio of two independent small numbers is not justified by notation alone.

The third is the distinction between straight-$d$ and curly-$\partial$ differentiation. When a function depends on several variables, differentiating with respect to one of them while holding the others fixed produces a partial derivative, written with $\partial$. The elementary computations that appear in this topic are

$$
\frac{\partial}{\partial x}\left(3y^{2}x^{2}\right)=6xy^{2}, \qquad \frac{\partial}{\partial y}\left(7y\sin x\right)=7\sin x .
$$

In the first, the factor $3y^{2}$ is a constant because it contains no $x$. In the second, the factor $\sin x$ is a constant because it contains no $y$. An equation built from such derivatives is a partial differential equation, and its solution is a function of several variables, which is why the theory of partial equations is a separate subject rather than a chapter of this one.

### 1.4 Order: the high-yield rules

Order is the more important of the two classification numbers, because it controls the number of arbitrary constants in the general solution and therefore controls how many conditions a question must supply.

The rules are these. Order is the number of differentiations applied to the term that has been differentiated most often, read by inspection. Order is unaffected by powers, by coefficients, by the right-hand side, and by any rearrangement that does not differentiate or integrate the equation. Order is unaffected by multiplying the equation through by a function of $x$, and unaffected by how many terms the equation contains.

Two consequences are worth committing to memory because they are worth marks directly.

The equation

$$
3\frac{d^{2}y}{dx^{2}}+\left(\frac{dy}{dx}\right)^{10}+8y=0
$$

is of order two, not ten. The tenth power belongs to the degree and does nothing to the order. This precise trap appears regularly, and it is worth a mark on its own.

The equation

$$
\frac{d^{3}y}{dx^{3}}+8\frac{d^{2}y}{dx^{2}}+9\frac{dy}{dx}+8y=e^{x}
$$

is of order three. The presence of $e^{x}$ on the right changes nothing: the order is a property of the derivatives of the unknown function, not of the forcing term.

An equation can also be written in a form in which the highest derivative is not isolated, and the order is still read from the highest derivative present. The equation

$$
y\frac{d^{3}y}{dx^{3}}+\left(\frac{d^{2}y}{dx^{2}}\right)^{4}=x
$$

is of order three even though the third derivative is multiplied by $y$ and the second derivative carries a fourth power.

### 1.5 Degree: the three cases that cover every question

Degree questions are the most frequently misanswered on this topic, and they are misanswered in one of three ways. Recognising which of the three cases applies is the whole skill.

**Case one: the equation is already a polynomial in the derivatives.** Then the degree is the exponent of the highest-order derivative, read directly. The equation

$$
\left(\frac{d^{2}y}{dx^{2}}\right)^{5}+3\left(\frac{dy}{dx}\right)^{7}+8y=0
$$

is of order two and degree five. The equation

$$
\left(\frac{d^{3}y}{dx^{3}}\right)^{5}+\left(\frac{d^{2}y}{dx^{2}}\right)^{11}+\left(\frac{dy}{dx}\right)^{20}+y=x
$$

is of order three and degree five: the eye is drawn to the twenty, but the twenty sits on a first derivative, and the highest-order derivative carries the power five.

**Case two: a radical or fractional power involves a derivative.** Then the equation must be cleared first, and the degree is read from the cleared form. Taken in isolation, the equation

$$
\left(\frac{d^{2}y}{dx^{2}}\right)^{3/2}=-5\frac{dy}{dx}-3y
$$

appears to have degree three halves, which is not an admissible answer. Squaring both sides clears the fractional power.

$$
\left(\frac{d^{2}y}{dx^{2}}\right)^{3}=\left(5\frac{dy}{dx}+3y\right)^{2}
$$

The cleared equation is of order two and degree three. The apparent three halves and the true three are different numbers, which is exactly why the definition insists on clearing before reading.

**Case three: a derivative sits inside a transcendental function.** Then no degree exists. The equations

$$
\sin\left(\frac{d^{2}y}{dx^{2}}\right)=x, \qquad e^{\frac{dy}{dx}}=x
$$

have orders two and one respectively, and neither has a degree, because no algebraic rearrangement produces a polynomial in the derivatives. The correct answer is a statement that the degree is undefined, with the reason given.

A fourth situation deserves a sentence, because it is the standard follow-up question. If the radical contains $y$ rather than a derivative, clearing it is unnecessary for the purpose of finding the degree. The equation

$$
\frac{dy}{dx}+\sqrt{y}=x
$$

has order one and degree one, since the radical involves the dependent variable and not a derivative.

### 1.6 Solution, general solution, particular solution

A solution is a function that turns the equation into an identity. The general solution is the whole family, carrying one arbitrary constant per unit of order. A particular solution is one member of that family.

The count of constants is a theorem rather than a convention, and its practical form is this: an equation of order $n$ has a general solution with exactly $n$ arbitrary constants. For

$$
\frac{dy}{dx}=2x
$$

the general solution is $y=x^{2}+C$, one constant, and $C=3$ produces the particular solution $y=x^{2}+3$. For

$$
\frac{d^{2}y}{dx^{2}}=6
$$

the general solution is $y=3x^{2}+C_{1}x+C_{2}$, two constants, and the pair $C_{1}=2$, $C_{2}=-1$ produces a particular solution.

Two further points are examined under this heading and are worth a mark each.

A **singular solution** is a solution that cannot be obtained from the general solution by any assignment of the constants. The standard example is

$$
\left(\frac{dy}{dx}\right)^{2}=4y ,
$$

whose general solution is $y=(x+C)^{2}$ and which also admits $y=0$. The constant function is not a member of the family for any value of $C$, because an identically zero square would require $x=-C$ for every $x$.

A **condition** selects a particular solution from the family. An initial condition prescribes values at a single point; a boundary condition prescribes values at two or more points. For an equation of order $n$, $n$ independent conditions are needed, and the number of conditions in a question is a direct hint about the order of the equation you should be expecting.

### 1.7 The shapes of questions asked

Six stems account for almost every question on this topic. Learning to recognise the stem is worth marks because it tells you what the final line of your answer must say.

| Stem as printed | What is being tested | The final line must contain |
| --- | --- | --- |
| Find the order and degree of | Recall plus radical clearing | Two numbers, or one number plus "no degree" |
| Show that $y=\ldots$ is a solution of | Differentiation and substitution | The words "hence the equation is satisfied identically" |
| Is $y=\ldots$ a solution of | Differentiation and a judgement | Either an identity or a specific failure |
| Find the differential equation of the family | Elimination of constants | The equation, plus the order matching the constant count |
| Solve, given that $y=\ldots$ when $x=\ldots$ | Integration and use of a condition | The particular solution with the constant evaluated |
| Solve the differential equation | Integration to general solution | The family with the full complement of constants |

Two variants deserve warning. The stem "form the differential equation" with no further specification usually wants the answer in the tidiest standard form, with the highest derivative coefficient equal to one. The stem "find the particular solution" wants no arbitrary constants in the final line at all; leaving a $C$ in place costs the final accuracy mark.

### 1.8 The five-line classification answer

When a question simply asks for the order and degree of one or two equations, the answer should be a short structured paragraph, not a single number. The following template earns full marks and takes under a minute.

Line one states the highest derivative present and names it. Line two states the order. Line three states whether any radical or fractional power involves a derivative, and if so shows the clearing. Line four states the degree, or states that no degree exists and why. Line five, if the question asks, states whether the equation is linear, with the offending term identified.

The template matters because the marks are attached to the reasoning, not only to the numbers. An answer consisting of the two numbers alone typically earns half marks, since the examiner cannot see whether the degree was read or guessed.

## 2. Theorems, Lemmas, and Analytical Properties

### 2.1 The constant-count theorem and its audit role

> **Theorem (Constant count).** The general solution of an ordinary differential equation of order $n$ contains exactly $n$ independent arbitrary constants, provided the equation is solved for its highest derivative and the coefficient functions are continuous on the interval.

The hypothesis about solving for the highest derivative is what allows the equation to be integrated, one order at a time, from initial data. The hypothesis about continuity is what allows the integrations to be performed at all. Neither hypothesis can be dropped without the conclusion becoming false, and the counterexamples are the singular solutions of Section 5.2.

The theorem has two uses in an examination. The first is predictive: an order-two equation will require two integrations and will produce two constants, so a candidate who reaches the end of the working with one constant knows immediately that something has been lost, and can find the omission before the invigilator calls time. The second is diagnostic: an answer that carries three constants for an order-two equation has counted one of them twice, usually by adding a constant inside an exponential and again outside it.

> **Corollary (Determination by conditions).** If $n$ independent conditions are imposed on the solutions of an order-$n$ equation, they determine the constants uniquely, and the corresponding initial value problem has exactly one solution.

This corollary is why a question can say "find the particular solution" and expect a single answer. It is also why the number of conditions supplied always matches the order of the equation in a well-posed question; a mismatch is a signal that the equation has been read wrongly.

### 2.2 The elimination theorem and the count of equations

> **Theorem (Elimination of constants).** A family of curves depending on $n$ arbitrary constants satisfies an ordinary differential equation of order $n$, obtained by differentiating the family $n$ times and eliminating the $n$ constants among the resulting $n+1$ equations.

The arithmetic of $n+1$ is the part candidates get wrong. To eliminate one unknown from a system of equations you need at least two equations. To eliminate two unknowns you need three. In general $n$ unknowns require $n+1$ equations, and the family plus its first $n$ derivatives supplies exactly that many. A candidate who differentiates only $n-1$ times will find the constants cannot be removed, and will often respond by inventing an extra relation that is not true.

The theorem is the exact converse of the constant-count theorem, and the two together give the topic its shape: differentiation raises the order and destroys constants, integration lowers the order and creates them.

### 2.3 Order is invariant under rearrangement

> **Lemma (Order invariance).** Multiplying an equation by a non-zero function of $x$, adding the same expression to both sides, clearing denominators involving $x$ alone, and expanding brackets never change the order.

The proof is immediate from the definition. The order is a property of the set of derivatives present, and none of these operations introduces or removes a differentiation with respect to $x$. Only differentiating both sides raises the order, and only integrating both sides lowers it.

The lemma is worth quoting when a question presents an equation in a deliberately untidy form. A candidate may be tempted to say that clearing a denominator containing $\frac{d^{2}y}{dx^{2}}$ changes the order; it does not, though it may change the degree.

### 2.4 Degree depends on the form in which the equation is written

> **Lemma (Form dependence of degree).** The degree is well defined only after the equation has been written as a polynomial in the derivatives, and two algebraically equivalent arrangements of the same equation can present different powers.

The lemma follows at once from the definition, which contains the clearing clause. Its consequence is procedural: the degree must be read from the cleared form, and the cleared form must be shown in the answer. An examiner who cannot see the cleared equation cannot award the degree mark.

A second consequence is that degree is a weaker invariant than order. Order tells you how many constants to expect and therefore has structural content. Degree tells you almost nothing beyond the algebra of the particular arrangement, which is why degree questions are usually worth only one mark while order questions are worth one mark each on a list.

### 2.5 Superposition and the test for linearity

> **Theorem (Superposition).** If $y_{1}$ and $y_{2}$ both satisfy the linear homogeneous equation $L[y]=0$, where $L$ is a linear differential operator, then every combination $c_{1}y_{1}+c_{2}y_{2}$ satisfies $L[y]=0$. Moreover, if $y_{p}$ satisfies $L[y]=F$ and $y_{h}$ satisfies $L[y]=0$, then $y_{p}+y_{h}$ satisfies $L[y]=F$.

The theorem is quoted here for two reasons. It explains why the general solution of a linear equation can be assembled as a sum, which is the method used from the next topic onwards. And it supplies a test: if a proposed general solution is a sum of two independent pieces, the equation had better be linear, or the answer is suspect.

Linearity is tested mechanically. An equation is linear when it can be written with the unknown and its derivatives appearing only to the first power and never multiplied together, with coefficients depending on $x$ alone. The equation

$$
\frac{d^{2}y}{dx^{2}}+4y=\sin x
$$

is linear. The equation

$$
\frac{d^{2}y}{dx^{2}}+y^{2}=0
$$

is not, because $y$ is squared. The equation

$$
y\frac{dy}{dx}=x
$$

is not, because $y$ multiplies a derivative. The equation

$$
\frac{dy}{dx}+\sin y=x
$$

is not, because a non-linear function of $y$ appears. In each non-linear case superposition fails, and it fails visibly: if $y_{1}$ solves $y''+y^{2}=0$ then $2y_{1}$ does not, since the derivative term doubles while the squared term quadruples.

### 2.6 Verification is an identity, not a coincidence

> **Principle (Verification).** A proposed function is a solution precisely when substitution produces an identity in the independent variable, that is, when the two sides agree as algebraic expressions after simplification.

The principle has a sharp practical consequence. An equation can hold at isolated points by accident, and a candidate who checks only at $x=0$ has checked nothing. The safe procedure is to simplify the left-hand side symbolically and compare it with the right-hand side symbolically.

The principle also explains why the verification step is worth a mark on schemes that would otherwise seem to have no room for it. It is not a courtesy; it is the definition of solution applied to the candidate's own answer.

### 2.7 Existence and uniqueness, and what they buy

> **Theorem (Picard–Lindelöf, first-order form).** Consider $y'=f(x,y)$ with $y(x_{0})=y_{0}$. If $f$ and its partial derivative with respect to $y$ are continuous on a rectangle containing the point, then a solution exists and is unique on some interval about $x_{0}$.

The hypothesis on the partial derivative cannot be dropped. The classical failure is

$$
y'=3y^{2/3}, \qquad y(0)=0 ,
$$

for which both $y=0$ and $y=x^{3}$ satisfy the equation and the condition, because the right-hand side has an unbounded derivative with respect to $y$ at the origin.

For examination purposes the theorem does one job: it justifies writing "the particular solution is" rather than "a particular solution is". When the hypotheses hold and the number of conditions matches the order, the answer is unique, and the definite article is correct.

### 2.8 Results at a glance

| Result | Statement in one line | Where it earns marks |
| --- | --- | --- |
| Constant count | Order $n$ means $n$ arbitrary constants | Auditing any general solution |
| Determination | $n$ independent conditions fix $n$ constants | Justifying a unique particular solution |
| Elimination | $n$ constants means an order-$n$ equation | Forming equations from families |
| Order invariance | Rearrangement preserves order | Defending an answer against a tidier form |
| Form dependence | Degree is read only after clearing | Every degree question |
| Superposition | Linear equations allow sums of solutions | Testing a proposed general solution |
| Verification | Solution means identity | Every "show that" question |
| Existence | Smooth data gives a unique local solution | Justifying uniqueness |

## 3. Formal Proofs, Derivations, and Methods

### 3.1 The classification protocol

The protocol is five steps and should be written out in that order, because the marks follow the order.

1. List every derivative present, with the number of differentiations each has undergone.
2. Take the largest number; that is the order. Report it.
3. Inspect the highest derivative for a surrounding radical or fractional exponent. If one is present, clear it algebraically and display the cleared equation.
4. Inspect the highest derivative for a surrounding transcendental function. If one is present, state that the degree is undefined and why, then stop.
5. Otherwise read the exponent of the highest derivative; that exponent is the degree. If the question asks about linearity, test whether the unknown and its derivatives occur only to the first power and never multiplied together.

### 3.2 Clearing radicals and fractional powers in general

The clearing step is always the same two moves, applied in the right order.

If the offending expression is a single term raised to a fractional power, isolate it on one side and then raise both sides to the reciprocal power. If the offending expression is a sum under a radical, isolate the radical first and only then raise both sides, because squaring a sum that still contains a radical does not remove the radical.

The general identity that justifies the first move is

$$
\left(A^{p/q}\right)^{q}=A^{p},
$$

valid for positive $A$. Applied to the standard examination example,

$$
\left(\frac{d^{2}y}{dx^{2}}\right)^{3/2}=-5\frac{dy}{dx}-3y ,
$$

squaring both sides gives

$$
\left(\frac{d^{2}y}{dx^{2}}\right)^{3}=\left(5\frac{dy}{dx}+3y\right)^{2} ,
$$

and the degree is now readable as three.

One caution must be stated, since it is occasionally examined. Squaring both sides is not an equivalence: it can admit solutions of the negated equation. For the purpose of reading the order and degree this does not matter, because the classification is read from the polynomial form that the equation generates. But if the equation is subsequently to be solved, the sign must be restored by checking candidate solutions in the original equation.

### 3.3 The verification protocol

1. Differentiate the proposed function as many times as the order requires, displaying each derivative on its own line.
2. Substitute the function and all derivatives into the left-hand side of the equation.
3. Simplify, collecting like terms and factoring where that makes the cancellation visible.
4. Compare with the right-hand side and state that the two sides agree identically.
5. State the interval on which the identity holds, if the function has a restricted domain.

Step 5 is the step candidates omit. A function such as $x\ln x$ is defined only for positive $x$, and a solution statement that ignores this is incomplete on a strict scheme.

### 3.4 Direct integration and the proof of the constant count

For an equation of the form

$$
\frac{d^{n}y}{dx^{n}}=f(x),
$$

with $f$ continuous, each integration lowers the order by one and adds one arbitrary constant. After $n$ integrations the solution has the shape

$$
y=F(x)+\frac{c_{1}x^{n-1}}{(n-1)!}+\frac{c_{2}x^{n-2}}{(n-2)!}+\cdots+c_{n-1}x+c_{n},
$$

where $F$ is one particular $n$-fold antiderivative of $f$.

To see that this is the general solution, differentiate $n$ times. Each term $c_{k}x^{n-k}/(n-k)!$ is a polynomial of degree $n-k$, so after $n$ differentiations every one of them has been destroyed, while $F$ returns $f(x)$. Hence the expression satisfies the equation for every choice of the constants. Conversely, if $y_{1}$ and $y_{2}$ both satisfy the equation, their difference $u=y_{1}-y_{2}$ satisfies $\frac{d^{n}u}{dx^{n}}=0$, whose solutions are exactly the polynomials of degree at most $n-1$, and those are precisely the terms carrying the constants. So every solution is of the displayed form, the constants are $n$ in number, and they are independent because the powers of $x$ involved are distinct.

The last sentence is the content of the theorem, reduced to the directly integrable case, and it is worth reproducing in an answer that asks why $n$ constants appear.

### 3.5 Separation of variables, its justification, and the solution it loses

The method applies to equations that can be rearranged into the shape $g(y)\frac{dy}{dx}=h(x)$. Integrating both sides with respect to $x$ converts the left side, by the substitution rule, into an integral with respect to $y$.

The justification is not that $dy$ and $dx$ are numbers that may be moved about. It is this. If $G$ is an antiderivative of $g$, then $\frac{d}{dx}G(y)=g(y)\frac{dy}{dx}$ by the chain rule, and if $H$ is an antiderivative of $h$ then $\frac{d}{dx}H(x)=h(x)$. Two functions with the same derivative on an interval differ by a constant, so

$$
G(y)=H(x)+C
$$

on that interval. The manipulation in which $dy$ and $dx$ appear to be separated is a shorthand for this argument, and it is valid precisely because the chain rule and the mean value theorem are available.

The method loses information at one point. Dividing by $g(y)$ requires $g(y)\neq 0$, so any constant solution with $g(y)=0$ disappears from view. Those solutions must be recorded separately if they are not recovered by a limiting value of the constant. The standard illustration is

$$
\frac{dy}{dx}=2y ,
$$

whose separated form is $\frac{1}{y}\frac{dy}{dx}=2$, leading to $y=Ae^{2x}$. The function $y=0$ solves the original equation but requires $A=0$, which is why the general solution is usually written with $A$ allowed to be any real number rather than a positive one.

### 3.6 The elimination protocol

1. Count the arbitrary constants and record $n$.
2. Differentiate the family $n$ times, displaying each derivative.
3. You now hold $n+1$ equations. Choose a strategy: substitution if one equation isolates a constant cleanly, combination if the constants appear in a recognisable pattern.
4. Eliminate the constants, working systematically from the highest derivative downwards, since the highest derivatives contain the fewest terms.
5. Tidy into standard form and check that the order equals $n$.
6. Optionally verify by substituting the family into the resulting equation and confirming an identity.

The choice in step 3 is what separates a two-minute solution from a five-minute one. When the family is a sum of exponentials, combination is fastest because the exponential terms behave like independent basis vectors. When the family contains a constant added to a function, substitution is fastest because the constant has already vanished from every derivative.

### 3.7 How marks are awarded

Most schemes on this topic use three kinds of mark, and knowing which is which changes how much working to write.

A method mark, written M, is awarded for attempting the correct procedure: differentiating the right function, separating correctly, integrating the right expression. Method marks survive arithmetic slips later in the same step.

An accuracy mark, written A, is awarded for a correct value or expression and depends on the relevant method mark. Accuracy marks are lost for sign errors, for a missing constant, and for an answer left in an unsimplified form when the question asked for a standard form.

An independent mark, written B, is awarded for a correct statement that does not depend on earlier working: the value of an order, the statement that a degree does not exist, the assertion that an equation is linear.

The practical rule that follows is simple. Write one line per differentiation or integration, state each classification explicitly in words, and never let an accuracy mark depend on mental arithmetic that has not been written down.

## 4. Representative Worked Examples and Solutions

### 4.1 Problem: classify two equations, one of which needs clearing (5 marks)

Find the order and degree of

$$
\text{(a)}\quad \left(\frac{d^{3}y}{dx^{3}}\right)^{2}+x\frac{d^{2}y}{dx^{2}}+y\frac{dy}{dx}=e^{x},
$$

$$
\text{(b)}\quad \sqrt{\left(\frac{d^{2}y}{dx^{2}}\right)^{3}}=-5\frac{dy}{dx}-3y ,
$$

and state whether each equation is linear.

### 4.2 Solution: inspect, clear, read, then test linearity

Step 1. In (a) the derivatives present are the first, second and third, so the highest is the third and the order is three. *(1 mark — B)*

Step 2. In (a) the third derivative already appears as a polynomial term with exponent two, and no radical or fractional power involves a derivative, so the degree is two. *(1 mark — B)*

Step 3. In (b) the highest derivative is the second, so the order is two. *(1 mark)*

Step 4. In (b) the second derivative is trapped inside a square root, so the equation must be cleared before the degree can be read. Squaring both sides removes the root.

$$
\left(\frac{d^{2}y}{dx^{2}}\right)^{3}=\left(5\frac{dy}{dx}+3y\right)^{2}
$$

*(1 mark)*

Step 5. In (b) the highest derivative now carries exponent three in a polynomial arrangement, so the degree is three. *(1 mark)*

Step 6. For linearity, (a) contains the term $y\frac{dy}{dx}$, in which the unknown multiplies its own derivative, so (a) is non-linear. Equation (b), in its cleared form, contains $\left(\frac{dy}{dx}\right)^{2}$ and $y^{2}$ on the right and a cubed second derivative on the left, so (b) is also non-linear.

Step 7. Collect the answers. Equation (a) is of order three, degree two, non-linear. Equation (b) is of order two, degree three, non-linear. Total: 5 marks.

### 4.3 Problem: form the differential equation of a two-constant family (5 marks)

Find the differential equation satisfied by the family

$$
y=c_{1}e^{2x}+c_{2}e^{-3x}.
$$

### 4.4 Solution: differentiate twice, then combine to cancel both constants

Step 1. There are two arbitrary constants, so the required equation is of order two and three equations are available. *(1 mark)*

Step 2. Differentiate once.

$$
\frac{dy}{dx}=2c_{1}e^{2x}-3c_{2}e^{-3x}
$$

*(1 mark)*

Step 3. Differentiate again.

$$
\frac{d^{2}y}{dx^{2}}=4c_{1}e^{2x}+9c_{2}e^{-3x}
$$

*(1 mark)*

Step 4. Form the combination $\frac{d^{2}y}{dx^{2}}+\frac{dy}{dx}-6y$ and substitute all three expressions.

$$
4c_{1}e^{2x}+9c_{2}e^{-3x}+2c_{1}e^{2x}-3c_{2}e^{-3x}-6c_{1}e^{2x}-6c_{2}e^{-3x}
$$

Step 5. Collect the coefficient of $e^{2x}$ and the coefficient of $e^{-3x}$ separately.

$$
\left(4+2-6\right)c_{1}e^{2x}+\left(9-3-6\right)c_{2}e^{-3x}=0
$$

Both brackets vanish, so the combination is zero for every choice of $c_{1}$ and $c_{2}$. *(1 mark)*

Step 6. State the equation and check the order.

$$
\frac{d^{2}y}{dx^{2}}+\frac{dy}{dx}-6y=0
$$

The order is two, matching the two arbitrary constants, so the count is consistent. *(1 mark)*

Step 7. Verify the combination was chosen correctly by re-deriving the multipliers from the family. The exponents are $2$ and $-3$, whose sum is $-1$ and whose product is $-6$, so the characteristic polynomial is $r^{2}+r-6$, matching the coefficients above. Total: 5 marks.

### 4.5 Problem: solve a second-order equation with two conditions (6 marks)

Solve

$$
\frac{d^{2}y}{dx^{2}}=12x^{2}
$$

given that $y=2$ and $\frac{dy}{dx}=1$ when $x=0$.

### 4.6 Solution: integrate twice, then use the conditions in the correct order

Step 1. The equation is of order two, so two integrations and two constants are expected. *(1 mark)*

Step 2. Integrate once with respect to $x$.

$$
\frac{dy}{dx}=4x^{3}+C_{1}
$$

*(1 mark)*

Step 3. Integrate again.

$$
y=x^{4}+C_{1}x+C_{2}
$$

*(1 mark)*

Step 4. Impose the condition on the derivative first, because it involves only $C_{1}$. At $x=0$,

$$
4(0)^{3}+C_{1}=1,
$$

so $C_{1}=1$. *(1 mark)*

Step 5. Impose the condition on the function. At $x=0$,

$$
0+C_{1}(0)+C_{2}=2,
$$

so $C_{2}=2$. *(1 mark)*

Step 6. State the particular solution.

$$
y=x^{4}+x+2
$$

*(1 mark)*

Step 7. Verify. Differentiating gives $\frac{dy}{dx}=4x^{3}+1$ and $\frac{d^{2}y}{dx^{2}}=12x^{2}$, which is the original equation; at $x=0$ the function equals two and the derivative equals one, as required. The answer carries no arbitrary constant, as a particular solution must not. Total: 6 marks.

### 4.7 Problem: solve a separable equation with a condition (6 marks)

Solve

$$
\frac{dy}{dx}=\frac{3x^{2}}{2y}
$$

given that $y=2$ when $x=1$.

### 4.8 Solution: separate, integrate, apply the condition, then choose the branch

Step 1. Separate the variables by multiplying both sides by $2y$.

$$
2y\frac{dy}{dx}=3x^{2}
$$

*(1 mark)*

Step 2. Integrate both sides with respect to $x$, converting the left side into an integral with respect to $y$.

$$
\int 2y\,dy=\int 3x^{2}\,dx
$$

*(1 mark)*

Step 3. Perform the integrations, adding one constant because one integration in total has been carried out.

$$
y^{2}=x^{3}+C
$$

*(1 mark)*

Step 4. Impose the condition. At $x=1$ and $y=2$,

$$
4=1+C,
$$

so $C=3$. *(1 mark)*

Step 5. Write the relation and choose the branch. The relation is $y^{2}=x^{3}+3$, and since the given value of $y$ is positive the solution is the upper branch.

$$
y=\sqrt{x^{3}+3}
$$

The branch is valid where $x^{3}+3>0$, that is for $x>-\sqrt[3]{3}$. *(1 mark)*

Step 6. Verify by differentiating the answer.

$$
\frac{dy}{dx}=\frac{3x^{2}}{2\sqrt{x^{3}+3}}=\frac{3x^{2}}{2y}
$$

This is the original equation, and at $x=1$ the value is $\sqrt{4}=2$ as required. *(1 mark)*

Step 7. Note the discarded branch. The lower branch $y=-\sqrt{x^{3}+3}$ also satisfies the differential equation but not the condition, which is exactly why the condition determines a particular solution. Total: 6 marks.

### 4.9 Problem: verify a proposed solution (4 marks)

Show that $y=x\ln x$ is a solution of

$$
x^{2}\frac{d^{2}y}{dx^{2}}-x\frac{dy}{dx}+y=0
$$

for $x>0$.

### 4.10 Solution: differentiate twice, substitute, and simplify to zero

Step 1. Differentiate once, using the product rule.

$$
\frac{dy}{dx}=\ln x+x\cdot\frac{1}{x}=\ln x+1
$$

*(1 mark)*

Step 2. Differentiate again.

$$
\frac{d^{2}y}{dx^{2}}=\frac{1}{x}
$$

*(1 mark)*

Step 3. Substitute all three quantities into the left-hand side.

$$
x^{2}\cdot\frac{1}{x}-x\left(\ln x+1\right)+x\ln x
$$

*(1 mark)*

Step 4. Simplify term by term.

$$
x-x\ln x-x+x\ln x=0
$$

*(1 mark)*

Step 5. Conclude. The left-hand side reduces to zero identically for every $x>0$, so the function satisfies the equation on that interval and is a solution there. Total: 4 marks.

### 4.11 Problem: form an equation from a two-constant family with no additive constant (6 marks)

Show that the family

$$
y=Ax^{2}+Bx
$$

satisfies

$$
x^{2}\frac{d^{2}y}{dx^{2}}-2x\frac{dy}{dx}+2y=0 .
$$

### 4.12 Solution: differentiate twice and build the combination

Step 1. There are two arbitrary constants, so the required equation is of order two. *(1 mark)*

Step 2. Differentiate once.

$$
\frac{dy}{dx}=2Ax+B
$$

*(1 mark)*

Step 3. Differentiate again.

$$
\frac{d^{2}y}{dx^{2}}=2A
$$

*(1 mark)*

Step 4. Substitute into the proposed combination.

$$
x^{2}(2A)-2x(2Ax+B)+2\left(Ax^{2}+Bx\right)
$$

*(1 mark)*

Step 5. Expand each term.

$$
2Ax^{2}-4Ax^{2}-2Bx+2Ax^{2}+2Bx
$$

*(1 mark)*

Step 6. Collect coefficients of $A$ and of $B$.

$$
\left(2-4+2\right)Ax^{2}+\left(-2+2\right)Bx=0
$$

Both brackets vanish identically, so the family satisfies the equation. *(1 mark)*

Step 7. Check the order and interpret. The equation is of order two with $x$-dependent coefficients, matching the two constants. Its general solution is the given family, so the equation and the family are converses of one another. Total: 6 marks.

### 4.13 Problem: form an equation where substitution is the only route (4 marks)

Find the differential equation of the family

$$
y=cx^{2}+\sin x .
$$

### 4.14 Solution: differentiate once, solve for the constant, substitute back

Step 1. There is one constant, so the equation is of order one and two equations suffice. *(1 mark)*

Step 2. Differentiate once.

$$
\frac{dy}{dx}=2cx+\cos x
$$

*(1 mark)*

Step 3. Solve the original family for $c$, which requires $x\neq 0$.

$$
c=\frac{y-\sin x}{x^{2}}
$$

Step 4. Substitute this expression for $c$ into the derivative.

$$
\frac{dy}{dx}=2\left(\frac{y-\sin x}{x^{2}}\right)x+\cos x
$$

Step 5. Simplify and state the equation.

$$
\frac{dy}{dx}=\frac{2}{x}\left(y-\sin x\right)+\cos x
$$

*(1 mark)*

Step 6. Check by substitution. Putting $y=cx^{2}+\sin x$ gives $y-\sin x=cx^{2}$, so the right-hand side is $2cx+\cos x$, which equals the derivative of the family. *(1 mark)*

Step 7. Note the restriction. The elimination required division by $x^{2}$, so the equation is valid for $x\neq 0$; the original family nevertheless makes sense at $x=0$. Total: 4 marks.

### 4.15 Problem: decide whether a function is a solution, and find the family when it is not (5 marks)

Determine whether $y=\cos 2x$ is a solution of

$$
\frac{d^{2}y}{dx^{2}}+4y=0,
$$

and state the general solution of that equation.

### 4.16 Solution: substitute, then read the general solution from the two independent functions

Step 1. Differentiate twice.

$$
\frac{dy}{dx}=-2\sin 2x, \qquad \frac{d^{2}y}{dx^{2}}=-4\cos 2x
$$

*(1 mark)*

Step 2. Substitute.

$$
-4\cos 2x+4\cos 2x=0
$$

The identity holds, so $y=\cos 2x$ is a solution. *(1 mark)*

Step 3. Recognise a second independent solution by the same computation with the sine.

$$
y=\sin 2x \quad\Longrightarrow\quad \frac{d^{2}y}{dx^{2}}=-4\sin 2x
$$

so $\frac{d^{2}y}{dx^{2}}+4y=-4\sin 2x+4\sin 2x=0$ as well. *(1 mark)*

Step 4. Invoke superposition, which is available because the equation is linear and homogeneous, and combine.

$$
y=A\cos 2x+B\sin 2x
$$

*(1 mark)*

Step 5. Check the count and conclude. The equation is of order two and the combination carries two independent arbitrary constants, so it is the general solution; the proposed function is the member with $A=1$ and $B=0$. *(1 mark)*

Total: 5 marks.

## 5. Mathematical Extensions, Limits, and Common Errors

### 5.1 The trap table

The following table lists the errors that actually cost marks, in descending order of frequency. Reading it before an examination is worth more than re-reading the definitions, because the definitions are already known and these slips are not deliberate.

| Trap | What it looks like | Correct handling |
| --- | --- | --- |
| Reading the degree before clearing a radical | Reporting degree $3/2$ for an equation with a square root around the second derivative | Clear first, display the cleared equation, then read the exponent |
| Confusing order with degree | "Degree three" for $y'''+y=0$ | Order counts differentiations; degree counts the power of the highest derivative |
| Reporting a degree that does not exist | Inventing a number for $\sin\left(y''\right)=x$ | State that the degree is undefined, and say why |
| Losing a constant of integration | $y=3x^{2}+C$ from $y''=6$ | One constant per integration; count them against the order |
| Adding a constant twice | Writing $y=Ae^{2x}+C$ when $C$ is already absorbed in $A$ | Absorb redundant constants and say that you have done so |
| Treating $\frac{dy}{dx}$ as a fraction without justification | "Multiply both sides by $dx$" offered as a proof | Cite the substitution rule and the fact that equal derivatives imply functions differing by a constant |
| Losing the zero solution after division | Dividing by $y$ in $\frac{dy}{dx}=2y$ and forgetting $y=0$ | Check separately whether the divisor can vanish |
| Wrong sign in $\int\sin x\,dx$ | Writing $+\cos x$ | The integral is $-\cos x$ |
| Forgetting to differentiate the inner function | Writing $y'=-8\sin 8x$ as $-8\sin x$ | Use the chain rule; the factor $8$ survives |
| Differentiating only $n-1$ times in an elimination question | Two constants, one derivative, no elimination possible | Differentiate exactly $n$ times to obtain $n+1$ equations |
| Leaving constants in a particular solution | $y=3x^{2}+C_{1}x+1$ after using both conditions | A particular solution contains no arbitrary constant |
| Checking a solution at one point only | Substituting $x=0$ and declaring success | Verification requires an identity in $x$ |
| Assuming superposition for a non-linear equation | Adding two solutions of $y''+y^{2}=0$ | Test linearity first; the sum is not a solution unless the equation is linear |
| Ignoring the interval of validity | Stating $y=\sqrt{x^{3}+3}$ for all real $x$ | State the interval on which the expression is defined and non-zero as required |

### 5.2 The limits of the theory

Three limitations deserve a sentence each, because they are the material for the final part of a long question.

The first is that elementary solutions need not exist. The equation $\frac{dy}{dx}=e^{-x^{2}}$ is first order, first degree and linear, and its solution is a perfectly well-defined function that cannot be written in elementary terms. Recognising this and leaving the answer as an integral is a complete and correct response, not a failure.

The second is that the general solution need not contain every solution. The equation $\left(\frac{dy}{dx}\right)^{2}=4y$ has the general solution $y=(x+C)^{2}$ and the additional solution $y=0$, which no value of $C$ produces. The singular solution must be added by inspection, and it is found by asking where the hypothesis of the uniqueness theorem fails, namely where the derivative with respect to $y$ of the right-hand side is unbounded.

The third is that a boundary value problem can fail to have a solution even when the corresponding initial value problem always does. Two conditions at a single point determine the constants uniquely under the hypotheses of the theorem; two conditions at two different points may produce an inconsistent algebraic system, in which case no solution exists, or a system with infinitely many solutions, in which case the solution is not unique.

A related caution concerns the direction of implication. A family of curves determines a unique differential equation of the corresponding order, but a differential equation determines its solution family only up to the general solution, and differentiating an equation to raise its order can admit extraneous solutions. The elimination method of Section 3.6 is therefore applied with the awareness that the resulting equation is satisfied by the given family and possibly by others as well.

### 5.3 Revision checklist

Each item should be checkable in under a minute, and each corresponds to a mark that is regularly lost.

- I can state the definitions of ordinary and partial differential equation, naming the number of independent variables in each.
- I can explain what $\frac{d}{dx}$, $\frac{d^{2}y}{dx^{2}}$ and $\frac{d^{n}y}{dx^{n}}$ mean, including that the indices count differentiations.
- I can read an order from any equation, including one where a lower derivative carries a large power.
- I can read a degree, and I clear radicals before reading it.
- I know that a degree is undefined when a derivative sits inside a sine, cosine, exponential or logarithm, and I can say why.
- I can test linearity and name the offending term when an equation is non-linear.
- I can state the constant-count rule and use it to audit my own answers.
- I can verify a proposed solution by producing an identity, not by checking one point.
- I can form a differential equation from a family with one, two or three constants, differentiating exactly that many times.
- I can solve $y^{(n)}=f(x)$ by integrating $n$ times and adding one constant per integration.
- I can solve a separable equation, justify the separation, and record any solution lost by division.
- I can apply conditions to obtain a particular solution with no arbitrary constants remaining.
- I can state the interval of validity when a division or a square root restricts it.
- I know the difference between a general solution, a particular solution and a singular solution, with an example of each.

### 5.4 Time strategy

The topic is worth roughly a sixth of a typical first paper, so it should be worth roughly a sixth of the time. A workable allocation for a two-hour paper is fifteen minutes, distributed as follows.

Spend two minutes reading the whole question and marking which parts are bookwork and which are computation. Bookwork should be answered first because it is certain, and because writing a definition settles the mind.

Spend three minutes on definitions and classification. These answers are short, and the temptation is to overwrite them. One sentence per definition, one display block per cleared equation, and the numbers stated explicitly is sufficient.

Spend five minutes on verification or formation. These parts require two or three differentiations and a substitution, and the arithmetic is where time is lost. Write each derivative on its own line, and simplify symbolically rather than numerically.

Spend four minutes on solving, including the separable case. Separation, integration, constant, condition, explicit form: one line each. Do not attempt to tidy an implicit answer into an explicit one unless the algebra is immediate, and say that the answer is left implicit if it is not.

Spend the final minute checking three things: that every general solution carries the correct number of arbitrary constants, that every particular solution carries none, and that each final line answers exactly what was asked. These three checks recover more marks than any amount of re-reading.

A further piece of strategy concerns partial credit. Since the marks are attached to procedures, an unfinished solution written in clear steps usually scores more than a finished one written as a block. When time is short, write the first integration and the shape of the answer rather than nothing at all.

### 5.5 The topic in one paragraph, for the last minute before the paper

A differential equation is an equation containing derivatives of an unknown function; it is ordinary when there is one independent variable and partial when there are two or more. The highest derivative present fixes the order, and the order fixes the number of arbitrary constants in the general solution. The power of that highest derivative, after radicals and fractional powers have been cleared, is the degree, and the degree does not exist when a derivative is trapped inside a transcendental function. A function is a solution when substitution produces an identity; the general solution is the family carrying the full complement of constants; a particular solution is one member obtained by assigning values to those constants, and a singular solution is one that no assignment can produce. Forming an equation from a family is the reverse process, requiring as many differentiations as there are constants and one more equation than there are constants. Solving, in the cases examined here, is integration: directly when the highest derivative equals a function of the independent variable alone, and after separating the variables when the two sides can be disentangled, with the answer verified every time by differentiating it back into the equation from which it came.
