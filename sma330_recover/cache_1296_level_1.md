## 1. Foundational Concepts, Definitions, and Axioms

### 1.1 What "Quadrature" Means in Plain Words

The word *quadrature* comes from an old idea: finding a square with the same area as a given shape. In numerical analysis, quadrature simply means **finding the value of a definite integral by calculation rather than by an exact symbolic formula**. When an exact antiderivative is hard or impossible to write down, we approximate the area under a curve by adding up the areas of simple shapes (rectangles, trapezoids, or curved pieces).

A familiar everyday picture: imagine you must find the area of an irregular garden plot. You cannot use a single neat formula. Instead, you lay down many thin rectangular strips side by side, measure each strip, and add the areas. The thinner the strips, the closer your total is to the true area. Quadrature methods are the mathematical version of this strip-laying idea.

The analogy stops being exact in one important way: in the garden you can always make strips thinner and thinner by hand, but on a computer you must stop at some finite number of strips. That stopping point is exactly where **errors** enter, and this lesson is as much about measuring and controlling those errors as it is about the area itself.

### 1.2 Why Errors Are Central to Quadrature

Every quadrature result is an *approximation*. The exact integral is some number $I$; the computed value is some number $I_r$. The gap between them is the error. Because quadrature is built from many small arithmetic steps, errors can arise in two distinct ways:

- **Initial (round-off) errors** — each measured function value is stored on a machine with finite memory, so it is slightly wrong to begin with.
- **Propagated (accumulated) errors** — those small initial errors travel through the additions and multiplications of the method and grow into a larger total error in the final answer.

Understanding both is the heart of this unit. The lesson material introduces the vocabulary of errors first, then shows how errors combine when numbers are added, subtracted, multiplied, or divided.

### 1.3 The Learning Journey of This Unit

The approved lesson material organises the work as a short guided activity. The learner is asked to:

- watch a worked demonstration of the definitions and computations;
- list, in point form, the **key words** in the definition of errors and algorithms;
- make short notes on the **causes of errors** and how to avoid them;
- post answers on a discussion forum, read colleagues' posts, and improve their own answer.

The moderator's role is to direct discussion, **encourage participation of all learners**, **provide feedback**, and **summarise the lesson**. The lesson is scheduled for two hours, and the next topic is propagated errors. These activity notes matter for exam preparation because they tell you exactly which ideas the examiner expects you to be able to state and compute.

## 2. Theorems, Lemmas, and Analytical Properties

### 2.1 Definition of Round-Off and Truncation Errors

> **Definition (Round-off error).** Round-off errors arise because it is impossible to represent all real numbers exactly on a machine (computer) with finite memory. Rounding involves dropping decimal points or significant figures, and can be done by chopping (truncating) or by symmetric rounding.

Two distinct actions are named here:

- **Chopping / truncation** — simply discard the extra digits. For example, $2.34789$ chopped to three decimal places becomes $2.347$.
- **Symmetric rounding** — look at the next digit and move up or down to the nearest representable value. For example, $2.34789$ rounded to three decimal places becomes $2.348$.

### 2.2 Absolute Error

> **Definition (Absolute error).** Let $x_r$ be an approximate number to an exact number $x$. The absolute error is the absolute difference between the exact number and the approximate number:



$$
e_{\text{abs}}=\lvert x-x_r\rvert
$$



The symbol $\lvert\cdot\rvert$ means "size without sign". So an error of $-0.05$ and an error of $+0.05$ both count as $0.05$. We care about *how far off* we are, not which direction.

> **Definition (Error bound).** Let $\Delta x$ be a number such that



$$
e_{\text{abs}}=\lvert x-x_r\rvert=\Delta x
$$



> where $\Delta x$ is the upper bound of the error.

In words: $\Delta x$ is the largest the error could possibly be. If we only know that $x$ was rounded to a certain number of decimal places, we cannot know the exact error, but we can always state a guaranteed ceiling for it.

### 2.3 Relative Error

> **Definition (Relative error).** The relative error $e_r$ is the absolute error measured as a fraction of the size of the exact number:



$$
e_r=\frac{\lvert x-x_r\rvert}{\lvert x\rvert}
$$



Why bother? Because an absolute error of $0.5$ is enormous when the true answer is $2$, but tiny when the true answer is $2{,}000{,}000$. Relative error puts the mistake on a common scale. The source also writes the relative error in the equivalent form $\dfrac{e_{\text{abs}}\text{ in }x_r}{\lvert x\rvert}$.

### 2.4 The Standard Error Bound for a Rounded Number

> **Result (Error bound from decimal places).** If a number is correct to $n$ decimal places, then the maximum absolute error is



$$
e_{\text{abs}}=0.5\times 10^{-n}
$$



This is the single most useful shortcut in the whole lesson. It says: count the decimal places, raise $10$ to the negative of that count, and halve it. For example, a number given correct to five decimal places has



$$
e_{\text{abs}}\le 0.5\times 10^{-5}
$$



The reasoning is simple. If a number is correct to $n$ decimal places, the true value lies within half of one unit in the last decimal place. Half of $10^{-n}$ is $0.5\times 10^{-n}$.

### 2.5 Key Words in the Definition of Errors (Point Form)

The lesson explicitly asks for the key words of the definition in point form. The essential words, drawn directly from the source, are:

- **Approximate number** $x_r$ — the value we actually use.
- **Exact number** $x$ — the true value we cannot store perfectly.
- **Absolute difference** — the size of the gap, written $\lvert x-x_r\rvert$.
- **Upper bound** $\Delta x$ — the largest possible size of that gap.
- **Relative error** — the gap divided by the size of the exact number.
- **Finite memory** — the machine limitation that makes exact storage impossible.
- **Chopping / truncating** — dropping digits without adjusting.
- **Symmetric rounding** — adjusting to the nearest representable value.

### 2.6 Causes of Errors and How to Avoid Them (Short Notes)

The source identifies the root cause clearly: a machine has **finite memory**, so most real numbers cannot be stored exactly. From this root cause flow the practical causes and remedies:

- **Cause: limited storage of digits.** Remedy: keep track of how many decimal places or significant figures are trustworthy, and state the error bound using $0.5\times 10^{-n}$.
- **Cause: chopping instead of rounding.** Chopping always pushes the value in one direction and can bias a long sum. Remedy: use symmetric rounding, which balances errors above and below the true value.
- **Cause: careless loss of significant figures in intermediate steps.** Remedy: carry more digits through intermediate work than you report in the final answer.
- **Cause: unchecked accumulation over many operations.** Remedy: estimate the propagated error (Section 2.7) before trusting the final result.

### 2.7 Propagation of Errors in Arithmetic Operations

> **Definition (Propagated error).** The error in the result of an arithmetic operation arising due to initial errors in the numbers used in that operation is called the propagated error. The total cumulative error at any step in the procedure is called the accumulated error.

The source sets this up as follows. Let $x$ and $y$ be two exact numbers, and let $x^{*}$ and $y^{*}$ be approximations with initial errors $\varepsilon$ (epsilon) and $n$ (nill) respectively, so that



$$
x=x^{*}+\varepsilon,\qquad y=y^{*}+n
$$



Let $w$ stand for an operation (addition, subtraction, multiplication, or division). The difference between the exact operation and the operation performed on the approximations is split into two parts:



$$
\left(x\,w\,y-x^{*}\,w\,y^{*}\right)=\underbrace{\left(x\,w\,y-x^{*}\,w\,y\right)}_{\text{propagated error}}+\underbrace{\left(x^{*}\,w\,y-x^{*}\,w\,y^{*}\right)}_{\text{generated error}}
$$



Read this slowly, because it is the key structural idea of the lesson:

- The **propagated error** is the part caused by the initial error $\varepsilon$ in $x$ alone, carried through the operation.
- The **generated error** is the part caused by the initial error $n$ in $y$ alone.
- Their sum is the **accumulated error** — the total cumulative error at that step.

In practice, for the four basic operations, the accumulated error is estimated by the standard rules:

- **Addition and subtraction:** the absolute errors add. If $z=x\pm y$, then the error in $z$ is at most the error in $x$ plus the error in $y$.
- **Multiplication:** the relative errors add. If $z=xy$, then the relative error in $z$ is at most the relative error in $x$ plus the relative error in $y$.
- **Division:** the relative errors add. If $z=x/y$, then the relative error in $z$ is at most the relative error in $x$ plus the relative error in $y$.

The practical warning that follows: subtraction of two nearly equal numbers is dangerous, because the absolute errors add while the result becomes tiny, so the relative error explodes.

## 3. Formal Proofs, Derivations, and Methods
### Deriving the three-node Gauss–Legendre rule

The lesson's three-point rule is built on the reference interval from −1 to 1. Because the interval is symmetric, choose three symmetric nodes: −r, 0, r. Seek a weighted sum whose end nodes have the same weight A and whose center has weight B. Symmetry automatically makes the rule exact for odd functions: both the integral and the quadrature sum are zero. To determine A, B, and r, require exactness for the even monomials 1 and x² as well.

For f(x)=1, the exact integral is 2. The weighted sum is 2A+B, so 2A+B=2. For f(x)=x², the exact integral is 2/3 and the weighted sum is 2Ar², so 2Ar²=2/3. To ensure the highest possible degree for three nodes, also use the x⁴ moment: its integral is 2/5 and the rule gives 2Ar⁴=2/5. Dividing the x⁴ equation by the x² equation yields r²=3/5. Substituting into the x² moment gives A=5/9, and the constant equation gives B=8/9.

The resulting nodes and weights are

$$
\begin{aligned}
x_1&=-\sqrt{3/5},&x_2&=0,&x_3&=\sqrt{3/5},\\
A_1&=5/9,&A_2&=8/9,&A_3&=5/9.
\end{aligned}
$$

Thus

$$
\int_{-1}^{1}f(x)\,dx\approx\frac59f\!\left(-\sqrt{3/5}\right)+\frac89f(0)+\frac59f\!\left(\sqrt{3/5}\right).
$$

This simple moment calculation explains why the weights are not equal: the central point represents a different share of the interval's polynomial area than either outer point. It also shows how an undetermined-coefficient method works. Propose a formula with unknown nodes and weights, apply it to a set of test polynomials, and solve the resulting equations. A symmetric choice reduces the algebra because odd moments vanish.

### Why three nodes give precision through degree five

The three weights and three nodes are selected so that the rule integrates polynomial test functions exactly up to degree five. In general, an n-node Gauss–Legendre rule is exact for every polynomial through degree 2n−1. For three nodes, that means degree five. Exactness for all such polynomials follows from the construction based on the orthogonal polynomial whose roots are the nodes; it is stronger than merely matching three or six isolated examples.

A quick check uses symmetry. The rule is exact for x, x³, and x⁵ because each is odd and integrates to zero on the symmetric interval. It is exact for 1, x², and x⁴ because the moment equations were chosen to match those integrals. These six monomials form a basis for all polynomials of degree at most five, so linearity implies exactness for every polynomial in that space. The statement says nothing that all non-polynomial functions will be integrated exactly. For them, the rule remains an approximation, though a smooth function may be approximated effectively by polynomials.

The standard three-point rule uses interior nodes, not interval endpoints. This is different from the composite trapezoidal rule, which uses endpoint values and evenly spaced samples. The Gaussian nodes are chosen to maximize polynomial exactness for a given node count; they are not selected simply because they are convenient points on a uniform grid. If function values are supplied only at equally spaced points, a Gaussian rule may not be usable without evaluating or interpolating at its nodes.

## 4. Representative Worked Examples and Solutions
### Worked example: evaluate x^6 with the three-point rule

Use the Gaussian formula on [−1,1] for f(x)=x^6. Its three nodes are −r, 0, r where r=√(3/5); the weights are 5/9, 8/9, 5/9. At the middle node the function value is zero. At either outer node, x^6=(3/5)^3=27/125. Therefore

$$
Q_3=\frac59\left(\frac{27}{125}\right)+\frac89(0)+\frac59\left(\frac{27}{125}\right)=\frac{6}{25}=0.24.
$$

The exact integral is 2/7≈0.285714. The absolute difference is about 0.0457143, so the estimate is not exact. This is expected: x^6 has degree six, while a three-node Gauss–Legendre formula guarantees exactness only through degree five. For comparison, applying the same rule to x^4 gives 2/5 exactly. The pair of examples shows how the degree-of-precision statement guides interpretation.

### Worked example: map the exponential to [−1,1]

Estimate the integral of e^x from 0 to 1. The midpoint and half-width are both 1/2, so the reference point t maps to x=(1+t)/2. The Jacobian contributes a factor 1/2. Substitute the three nodes and weights:

$$
Q=\frac12\left[\frac59e^{(1-\sqrt{3/5})/2}+\frac89e^{1/2}+\frac59e^{(1+\sqrt{3/5})/2}\right]\approx1.7182810.
$$

The exact integral e−1 is approximately 1.7182818. The estimate is close, but not exact because the exponential is not a polynomial of degree at most five. Notice the order of work: transform the nodes, evaluate the function, weight and add the values, then multiply by the half-width. Omitting that last factor would produce about twice the correct integral.

## 5. Mathematical Extensions, Limits, and Common Errors
### 5.1 High-Yield Takeaways

- **Know the three error measures by name and formula:** absolute error $\lvert x-x_r\rvert$, relative error $\lvert x-x_r\rvert/\lvert x\rvert$, and the bound $\Delta x$.
- **Memorise the decimal-place shortcut:** correct to $n$ decimal places means $e_{\text{abs}}=0.5\times 10^{-n}$. This answers most short questions instantly.
- **Distinguish chopping from symmetric rounding.** Chopping discards digits; symmetric rounding moves to the nearest representable value.
- **State the two causes clearly:** finite machine memory, and the choice of chopping versus rounding.
- **Define propagated versus accumulated error precisely.** Propagated error comes from initial errors carried through an operation; accumulated error is the total cumulative error at a step.
- **Remember the operation rules:** absolute errors add under addition and subtraction; relative errors add under multiplication and division.
- **Be ready to list key words in point form** — approximate number, exact number, absolute difference, upper bound, relative error, finite memory, chopping, symmetric rounding.
- **Be ready to describe the lesson activity:** watch the demonstration, list key words, note causes and remedies, post on the forum, read colleagues' posts, improve your answer. The moderator directs discussion, encourages participation of all learners, provides feedback, and summarises the lesson.

### 5.2 Common Pitfalls

- **Forgetting the absolute value.** An error of $-0.05$ is reported as $0.05$, not $-0.05$.
- **Using the wrong $n$.** Count decimal places, not significant figures, when applying $0.5\times 10^{-n}$.
- **Letting the sign of the number confuse you.** The bound depends only on the number of decimal places, as the negative example shows.
- **Confusing absolute and relative error.** Absolute error carries units; relative error is a pure fraction.
- **Assuming errors cancel.** Under addition and subtraction they add in size; they do not cancel.
- **Ignoring the subtraction danger.** Subtracting nearly equal numbers produces a tiny result with a large relative error.
- **Treating an approximation as exact.** Always report the error bound alongside a computed value.
- **Skipping the interval step.** Writing the interval $2.35\le x\le 2.45$ first makes the error bound obvious and prevents sign mistakes.

### Using the three-point rule on a new interval

Once the reference nodes and weights are known, an integral on another interval becomes a substitution task. Find the midpoint c=(a+b)/2 and half-width d=(b−a)/2. Replace each reference node t_i by x_i=c+dt_i, evaluate f at the three new x values, add each value times its weight, and finally multiply by d. The node locations move with the interval, but the weights 5/9, 8/9, 5/9 do not change. The outside factor d accounts for the change in interval length.

For [0,1], c=d=1/2. The outer nodes lie at about 0.1127 and 0.8873, while the central node is 0.5. These are not equally spaced: Gaussian quadrature chooses them to give high polynomial exactness, not to make a uniform table. A learner should not substitute the endpoints 0 and 1 into the rule. Nor should the factor one half be omitted; doing so would double the result on this interval.

A useful routine is to write a small table with columns for the reference node t_i, the mapped point x_i, the weight A_i, and the weighted function value A_i f(x_i). That table keeps the interval transformation visible. After the weighted sum is formed, multiply by d and check the scale. If f is the constant one, the result must be b−a, since the weights sum to two and d=(b−a)/2. This constant-function check catches a missing Jacobian immediately.

### Exactness as a practical test

The three-point Gauss–Legendre formula exactly integrates every polynomial of degree at most five on the reference interval. This is a powerful check but not a promise that all functions are exact. A polynomial x^4 should be reproduced exactly; x^6 is outside the guaranteed range and can show a difference. A smooth exponential is also not a polynomial, so its result is an approximation that can be compared with its known integral if one is available.

The guarantee helps choose a rule. If the function is a polynomial of degree five or less, one application of the three-point formula is exact in exact arithmetic. For a higher-degree polynomial or a non-polynomial integrand, the rule still gives a useful weighted estimate but there is truncation error. If the interval is long or the function changes rapidly, using subintervals can improve resolution. For each subinterval, map the same three reference nodes and add the resulting estimates. A single high-degree exactness statement does not eliminate the need to examine the function's behavior.

### How to explain the answer

In a written solution, identify the three-point Gaussian rule, list its nodes and weights, show the interval map, and substitute the function values. Keep the final factor (b−a)/2 visible. Then state whether the calculation is exact by polynomial degree or is an approximation. When an exact integral is known, compare the two; otherwise avoid unsupported claims about the number of correct digits.

The nodes are selected in advance for the rule; the weights describe how much each sampled function value contributes. Their sum is two on [−1,1], the area under the constant function one. The outer weights sum to 10/9 and the central weight is 8/9, so the center carries a little less than half of the total weight. These checks make the formula easier to remember and help detect a copied weight or node with the wrong sign.


### What a Gaussian node represents

A node is a location where the function is sampled; a weight tells how strongly that sample contributes to the approximate integral. The three-point rule gives the central value weight 8/9 and each outer value weight 5/9. The total is two, which is exactly the integral of the constant one over [−1,1]. The nodes and weights are not arbitrary: they are chosen together so that polynomial moments match the true integral as far as possible with three evaluations.

This explains why the rule may use fewer function evaluations than a uniform composite rule for smooth functions. It does not mean the Gaussian rule always wins. Its sample points are generally nonuniform and interior, so it requires the ability to evaluate f at those locations. If a data set contains only fixed equally spaced ordinates, the prescribed Gaussian samples may be unavailable. A Newton–Cotes rule may then be more practical even though its degree of precision per point is lower.

### Interpreting accuracy rather than guessing it

A polynomial exactness guarantee is a precise statement: all polynomials up to the stated degree give zero truncation error in exact arithmetic. For functions outside that class, accuracy depends on the function, interval, and node choice. Testing one integrand gives an example, not a universal bound. A value that is close to an exact answer can be described as accurate for that example; it should not be used to claim that all smooth functions have the same number of correct digits.

The three-point rule's error on x^6 illustrates the distinction. Its degree-six error is known exactly in the source exercise, and the exact integral can be computed independently. In a real problem without an exact antiderivative, one might compare against a higher-resolution or composite calculation, but that comparison is evidence, not proof. Report both the approximation and how its accuracy was assessed.


### A practical checklist for a first Gaussian calculation

The three-node formula is easiest to use when the calculation is separated into four jobs. First identify the interval and the reference rule. Second map the nodes from [−1,1] to the interval. Third evaluate the integrand at those mapped nodes and form the weighted sum. Fourth multiply by the half-width. Writing these stages separately keeps the geometric transformation visible instead of hiding it inside a long substitution.

On an interval [a,b], let c=(a+b)/2 and d=(b−a)/2. The reference nodes −r,0,r become c−dr,c,c+dr. The value of the integral is d times the reference weighted sum. Before using a decimal calculator, preserve r=√(3/5) and the weights as exact fractions. Only after the function values are obtained should the terms be combined and rounded. This approach makes a wrong node, an omitted factor, or premature rounding much easier to locate.

A useful unit check follows from integrating f(x)=1. The reference formula gives

$$
\frac59+\frac89+\frac59=2,
$$

and scaling by d gives 2d=b−a. Thus the formula returns the interval length, as any quadrature formula for the constant should. The check is short enough to include in a solution and catches a common mistake: applying a reference-interval formula directly to a different interval without the Jacobian.

Symmetry offers another check. For an odd function on [−1,1], the exact integral is zero. Symmetric nodes and equal outer weights cancel the two outer terms, and the center term is zero for an odd function. For an even function, the two outer function values agree, so the sum can be simplified by doubling one outer contribution. These observations are not shortcuts that replace the rule; they are ways to verify that its symmetry has been used consistently.

### Reading a tabulated rule correctly

A Gauss–Legendre table gives nodes and weights for the reference interval with weight function one. The entries are paired: each weight belongs to the node in the same position. Sorting nodes from left to right is harmless only if the corresponding weights are kept with them. In the three-node case the symmetry makes the two outer weights equal, but that visual symmetry should not lead to an assumption that all weights are equal.

The number of nodes is not the same as the number of subintervals. A single three-node application uses three function values over one panel. A composite calculation divides the original interval into several panels and repeats the three-node rule on each panel, using a distinct midpoint and half-width for each. If there are m panels, the computation uses 3m evaluations unless points happen to coincide and are reused. The local estimates are added; the weights from separate panels are not pooled before their own scale factors have been applied.

This distinction also clarifies when the method is practical. If a function is available as a callable expression, evaluations at the Gaussian points can usually be made. If only observations at an equally spaced grid are supplied, those three interior points might not appear in the table. Interpolating a table to create new ordinates introduces a separate approximation and should be stated. A composite trapezoidal or Simpson rule may be the honest choice when the problem explicitly provides uniform data.

### Precision is not a promise about every function

The three-node rule exactly integrates any polynomial through degree five. That statement follows from the construction and is independent of the particular coefficients of the polynomial. It does not say that the rule gives six correct digits for every function, nor that an arbitrary smooth function has a known error from the degree alone. A student should use the precision theorem to decide whether exactness is guaranteed for a polynomial, not to guess the rounded accuracy of other integrands.

The source exercise with x^6 is a useful boundary test. The result 6/25 is not 2/7 because degree six lies just outside the guaranteed range. By contrast, x^4 is inside the range and is integrated exactly. The example is stronger than merely repeating the theorem: it makes clear that “one degree higher” can already produce a nonzero error.

For e^x on [0,1], the three-point result is close to e−1, but closeness is a property of that example and interval. The exact integral allows an observed error to be calculated. If an antiderivative is unavailable, an analyst can compare composite estimates or use a more detailed error theorem when its hypotheses are known. A comparison is a diagnostic rather than an automatic proof. In a written solution, make the distinction explicit: state exactness when the polynomial hypothesis applies; otherwise call the numerical result an approximation.

### Arithmetic discipline and final interpretation

The node √(3/5) is approximately 0.7745966692. On [0,1], the mapped nodes are approximately 0.1127016654, 0.5, and 0.8872983346. These values show that Gaussian sampling is not the same as evaluating at the endpoints and midpoint. Entering 0, 0.5, and 1 into the function would instead correspond to a different rule.

Keep the function values and weighted terms distinguishable in a calculation. The outer node values need not be equal unless the transformed integrand is symmetric about the interval midpoint. When they are not equal, each must be multiplied by its own weight before addition. After applying d, round the final estimate to a sensible number of places; reporting many digits from rounded exponentials would suggest unjustified precision.

A concise conclusion should name the interval, node count, result, and status of the result. For example, “The three-point Gauss–Legendre estimate on [0,1] is approximately 1.7182810; comparison with e−1 gives an observed absolute error of about 8.24×10⁻⁷.” This says what was computed and what evidence supports the accuracy claim. It does not elevate an observed comparison into a universal guarantee.

### A two-panel mapping exercise

Consider applying the three-point rule to [0,2] using two equal panels, [0,1] and [1,2]. Each panel has half-width 1/2, but the midpoints are different: 1/2 for the first and 3/2 for the second. The first panel's nodes are approximately 0.1127, 0.5, and 0.8873; the second panel's are approximately 1.1127, 1.5, and 1.8873. The global interval's endpoints, 0 and 2, are not sampled. Each local weighted sum is multiplied by 1/2, and the two results are added.

This layout helps students distinguish panel subdivision from increasing the node count of a single rule. A two-panel composite three-point calculation uses six evaluations, with three located inside each panel. It is not the six-point Gaussian rule on the full interval: the node locations, weights, and exactness argument differ. The composite construction retains the same local three-point exactness on each panel, while the global six-point Gaussian construction would have a different reference table and degree guarantee.

For a constant function, each panel estimate is 1, since its width is one. Their sum is 2, matching the total interval length. For any polynomial of degree at most five, each local panel is integrated exactly after the affine change of variable, so the sum of panel integrals is also exact. This follows panel by panel and does not require the polynomial to be centered around either midpoint.

### Deciding whether subdivision is useful

Subdivision is a way to control where information is gathered. If the function bends more strongly in one region than another, separate panels place local nodes around that behavior. A uniform partition is simple, while a nonuniform partition can allocate more panels to a region of rapid variation if the problem and accuracy strategy allow it. In either case, the total integral is the sum of panel estimates, and every panel must use its own mapping.

Subdivision increases the number of function evaluations. One should not subdivide mechanically without considering the cost or whether the integrand is already well represented over the full interval. A comparison between a one-panel and a two-panel estimate can be useful evidence of stability, but without an error theorem it remains a diagnostic. Agreement may happen accidentally, and a feature missed by both approximations may still be present.

If there is a known discontinuity, split the interval at that point rather than asking one smooth approximation to cross it. If the function has a narrow peak, choose panel boundaries so that the peak lies within a panel and then check that the node locations resolve it. The basic Gaussian formula does not remove the need to understand the function's behavior; it organizes the weighted sampling once the interval has been chosen.

### Explaining the formula in words

For a clear written explanation, state that Gaussian quadrature chooses sample locations and weights jointly so that polynomial moments match the integral to high degree. In the three-node Legendre rule, the nodes are symmetric, the outer nodes lie at ±√(3/5), and the center is zero. The central weight is 8/9 and each outer weight is 5/9. On an arbitrary finite interval, the affine map moves the nodes and the half-width scales the sum.

Then distinguish the rule's guaranteed property from the numerical outcome. The degree-five exactness means that a polynomial integrand of degree at most five is integrated exactly in exact arithmetic. For another integrand, the weighted sum is an approximation whose quality depends on its behavior and the interval. This two-part explanation is more informative than simply presenting a decimal answer or calling Gaussian quadrature “very accurate.”

Finally, connect the result to the task. If the problem asks for an approximation, give the weighted sum and a sensible rounded value. If it asks why an answer is not exact, identify whether the integrand exceeds degree five or is not a polynomial in that class. If it asks for method choice, mention node availability and function smoothness as well as the formal precision. These habits produce answers that show both the calculation and its meaning.

