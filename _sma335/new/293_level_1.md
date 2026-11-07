## 1. Foundational Concepts, Definitions, and Axioms

### 1.1 A picture to hold on to

Imagine a machine that watches a moving object and records not only where the object is, but also how fast it is going, how fast its speed is changing, and how fast that change of speed is changing. Engineers call those four readings position, velocity, acceleration and jerk. A rule that ties one of these readings to the others is a description of motion, and the number of readings involved tells you how complicated the rule is.

Now imagine a second, different machine: a photograph being enlarged on a photocopier. If you double the width of the picture, every length doubles, but every area is multiplied by four and every volume by eight. Lengths grow like the first power of the enlargement factor, areas like the second power, volumes like the third power. The enlargement factor behaves in a very orderly way, and the different kinds of measurement grow at different rates.

Those two pictures are the whole of this topic. The first picture is what a differential equation of order three or order four is: a rule relating a quantity to its first few rates of change. The second picture is what makes one special family of such equations solvable: if the rule is built so that each rate of change is multiplied by the matching power of the distance scale, then the powers and the rates of change cancel each other beautifully, and the equation can be reduced to a simple one with constant numbers in it.

The rest of this section turns those pictures into precise definitions. Nothing in the two pictures needs to be remembered as a formula; what matters is the shape of the idea.

### 1.2 The word "order"

A differential equation is an equation containing an unknown function and one or more of its derivatives. A derivative measures a rate of change, so a differential equation is a rule about how a quantity changes.

> **Definition (Order).** The order of a differential equation is the order of the highest derivative that appears in it.

Read the order off by counting how many times the highest derivative has been differentiated. If only the first derivative appears, the order is one. If the second derivative appears but nothing higher, the order is two. If the third derivative appears, the order is three, and so on.

The order matters because it fixes how many arbitrary constants the general answer will contain. An equation of order one has one constant in its general solution, an equation of order two has two constants, and an equation of order three has three. This counting rule is used twice in every problem: once at the start, to know how many constants to expect, and once at the end, to check that none has been lost.

### 1.3 The word "linear"

Linearity is a restriction on how the unknown function and its derivatives may appear.

> **Definition (Linear equation).** A differential equation is linear when the unknown function and each of its derivatives appear only to the first power, are never multiplied together, and are never placed inside a function such as a square, a sine or a logarithm. Everything else in the equation may depend on the independent variable.

Three quick tests settle almost every case. The equation in which the unknown appears squared is not linear. The equation in which the unknown multiplies its own derivative is not linear. The equation in which the unknown appears inside a sine is not linear. An equation in which the unknown appears once per term, always to the first power, is linear even when the multiplying coefficients are complicated functions of the independent variable.

Linearity is valuable because it allows solutions to be added together. If two functions each satisfy the same linear rule with zero on the right, then their sum satisfies the rule too, and so does any constant multiple of either. That single fact is what makes it possible to build the general answer out of a few special answers.

### 1.4 The definition of a linear equation of order n

Here is the definition in full. Read it slowly, because every later method is a consequence of this shape.

> **Definition (Linear equation of order n).** A linear differential equation of order n is an equation in which the unknown function and its first n derivatives appear, each multiplied by its own coefficient, and the whole sum is set equal to a known function of the independent variable. The coefficient of the highest derivative must not be zero.

Written out, with the independent variable called x and the unknown function called y, the equation looks like this.

$$
a_{0}(x)\frac{d^{n}y}{dx^{n}}+a_{1}(x)\frac{d^{n-1}y}{dx^{n-1}}+\cdots+a_{n-1}(x)\frac{dy}{dx}+a_{n}(x)y=Q(x)
$$

Every symbol in that display has a plain meaning, and it is worth naming each one.

The letter n is a fixed whole number, the order of the equation; it might be three, or four, or twenty.

The letter y is the unknown function, and it depends on x, so y is really y of x.

The symbol $\frac{d^{k}y}{dx^{k}}$ means the result of differentiating y exactly k times with respect to x. When k is one, this is the ordinary first derivative, the rate of change of y. When k is two, it is the rate of change of the rate of change.

The symbols $a_{0}$ up to $a_{n}$ are the coefficients. Each is a function of x, or a constant, and none of them may involve y. The coefficient $a_{0}$ sits in front of the highest derivative and must never be zero, because if it were zero the highest derivative would disappear and the equation would really be of lower order.

The symbol Q is the right-hand member, also called the forcing term. It is a function of x alone, and it is the part of the equation that is not multiplied by y or by any derivative of y.

A simple example makes the definition concrete. Take n equal to three, all four coefficients equal to constants, and Q equal to zero.

$$
2\frac{d^{3}y}{dx^{3}}-5\frac{d^{2}y}{dx^{2}}+4\frac{dy}{dx}-y=0
$$

This is linear of order three. The unknown y appears three times, once with each derivative and once on its own, always to the first power, and no two of those appearances are multiplied together. The coefficient of the third derivative is the constant two, which is not zero, so the order really is three.

### 1.5 Homogeneous and non-homogeneous

> **Definition (Homogeneous).** A linear equation is homogeneous when the right-hand member is zero everywhere. It is non-homogeneous when the right-hand member is not zero.

The word describes a balance rather than a substance. In a homogeneous equation every term contains the unknown or one of its derivatives, so every term is of the same degree, namely degree one, in the unknown. Replacing y by twice y multiplies the whole left-hand side by two, and zero stays zero. In a non-homogeneous equation the extra term Q does not share that property, and the balance is broken.

The practical difference is large. A homogeneous equation produces only the family of solutions that the equation supports of its own accord. A non-homogeneous equation produces that same family plus one extra function, a function shaped by the forcing term Q. The next two subsections explain how those two pieces are found and how they are combined.

### 1.6 The letter D and the operator form

Differentiating is an operation, and operations can be written as symbols. It is convenient to write the single letter D for the instruction "differentiate with respect to x".

$$
D=\frac{d}{dx}
$$

Then the symbol $D^{2}$ means "differentiate twice", the symbol $D^{3}$ means "differentiate three times", and in general $D^{k}$ means "differentiate k times". With this shorthand the long equation of the previous subsection becomes a single short statement.

$$
\left(2D^{3}-5D^{2}+4D-1\right)y=0
$$

The expression in the bracket is called a differential operator. When all the coefficients are constants, as they are here, the operator is nothing more than a polynomial in the letter D, with ordinary numbers as coefficients. That is a considerable simplification, because polynomials can be factored and their roots can be found.

$$
2D^{3}-5D^{2}+4D-1=(D-1)(2D^{2}-3D+1)=(D-1)(2D-1)(D-1)
$$

The factorisation is the whole point. Each factor of the form $D-m$, where m is a number, corresponds to a solution of the exponential kind. Factoring the operator is exactly as useful as factoring an ordinary polynomial, and it is done in exactly the same way.

### 1.7 Every answer has two parts

The solution of a non-homogeneous linear equation is always assembled from two separate pieces, and the two pieces are found by two separate procedures.

> **Definition (Complementary function).** The complementary function is the general solution of the equation obtained by replacing the right-hand member by zero. It contains as many arbitrary constants as the order of the equation.

> **Definition (Particular integral).** A particular integral is any single function that satisfies the full non-homogeneous equation. It contains no arbitrary constants.

> **Definition (General solution).** The general solution is the complementary function plus a particular integral.

The reason the two pieces can simply be added is that differentiation is a linear operation: the operator applied to a sum gives the sum of the operator applied to each part. So if the complementary function gives zero and the particular integral gives the forcing term, the sum gives the forcing term. Nothing more is needed.

An everyday comparison may help. Suppose a shop has a regular weekly income that it earns by itself, and a special order arrives that adds a fixed extra amount each week. The total weekly income is the regular income plus the extra amount. The regular income is the complementary function, the extra amount is the particular integral, and the total is the general solution. Changing the size of the special order changes only the extra amount, not the regular income.

### 1.8 The Cauchy–Euler equation

Some equations have coefficients that are not constants but still follow a strict pattern. The pattern is worth learning because it is the one case, apart from constant coefficients, that can always be solved completely.

> **Definition (Cauchy–Euler equation).** A linear equation is of Cauchy–Euler type when each derivative is multiplied by a constant times the matching power of x. That is, the first derivative is multiplied by a constant times x, the second derivative by a constant times $x^{2}$, the third derivative by a constant times $x^{3}$, and in general the k-th derivative by a constant times $x^{k}$.

Written out, the normalised form of order n is this.

$$
x^{n}\frac{d^{n}y}{dx^{n}}+a_{1}x^{n-1}\frac{d^{n-1}y}{dx^{n-1}}+\cdots+a_{n-1}x\frac{dy}{dx}+a_{n}y=f(x)
$$

The defining feature is the marriage of a power of x with a derivative of the same order. The power tells you how many times the function has been differentiated, and the two numbers always agree. That is precisely the balance described in the photograph picture of Section 1.1: the second derivative behaves like an area and is accompanied by the second power, the third derivative behaves like a volume and is accompanied by the third power.

A small example of order two shows the pattern clearly.

$$
x^{2}\frac{d^{2}y}{dx^{2}}-2x\frac{dy}{dx}+2y=0
$$

Here the second derivative is multiplied by $x^{2}$, the first derivative by minus two times x, and the function itself by the constant two.

The pattern can also be written in operator form, which is how it is usually presented in examinations. The left-hand side is a polynomial in the combination $xD$ rather than in D alone.

$$
\left(a_{0}x^{n}D^{n}+a_{1}x^{n-1}D^{n-1}+\cdots+a_{n-1}xD+a_{n}\right)y=f(x)
$$

An equation that looks similar but breaks the pattern cannot be solved this way. If the first derivative is multiplied by the constant two instead of by two times x, the marriage between powers and derivatives is broken and the method of this note does not apply.

### 1.9 Legendre's equation

Legendre's equation is the same pattern with x replaced by a shifted and stretched copy of x.

> **Definition (Legendre's equation).** A linear equation is of Legendre type when each derivative is multiplied by a constant times the matching power of the expression ax plus b, where a is a nonzero constant and b is a constant.

$$
(ax+b)^{n}\frac{d^{n}y}{dx^{n}}+a_{1}(ax+b)^{n-1}\frac{d^{n-1}y}{dx^{n-1}}+\cdots+a_{n-1}(ax+b)\frac{dy}{dx}+a_{n}y=f(x)
$$

If a is one and b is zero, the expression ax plus b is just x, and Legendre's equation becomes exactly the Cauchy–Euler equation. So the Cauchy–Euler equation is a special case, and Legendre's equation is the general version with the origin moved and the scale changed.

Everything that works for the one works for the other, with one addition: each time a derivative is taken with respect to x, a factor of a appears, because the inner expression ax plus b changes a times as fast as x does. That factor of a is easy to forget, and forgetting it is the single most common mistake in the whole topic.

## 2. Theorems, Lemmas, and Analytical Properties

### 2.1 Adding solutions

The first property is the one that makes everything else possible.

> **Theorem (Superposition).** If two functions each satisfy the same homogeneous linear equation, then their sum satisfies it too, and so does any constant multiple of either.

The reason is that the operator is linear: applying it to a sum gives the sum of the results, and applying it to a constant multiple gives the same constant multiple of the result. Both results are zero, so the sum of the results is zero.

Applied repeatedly, the theorem says that if you know several solutions of a homogeneous equation, then any combination of them with constant multipliers is also a solution. That is why the general solution is written as a sum with constants in front of each piece.

> **Corollary (Adding a particular integral).** If one function solves the non-homogeneous equation and another solves the homogeneous equation, then their sum solves the non-homogeneous equation.

### 2.2 Counting the constants

> **Theorem (Constant count).** The general solution of a linear equation of order n contains exactly n independent arbitrary constants.

The count is not a convention; it is forced by the order. To see why, notice that solving an equation of order n amounts to integrating n times, and each integration introduces one constant. The same count holds for the two special families in this note, because the substitution used to solve them preserves the order.

This gives a reliable check. A proposed answer to an equation of order three that contains only two constants is wrong, no matter how convincing the algebra looked. A proposed answer that contains four constants for an equation of order three is also wrong, because at least one of the constants duplicates another.

### 2.3 The three kinds of root

For an equation with constant coefficients, everything depends on the roots of a polynomial called the auxiliary polynomial. The polynomial is obtained by replacing each D in the operator by a number m and setting the result equal to zero.

> **Definition (Auxiliary equation).** For the equation with operator polynomial P of D, the auxiliary equation is P of m equals zero, where m is a number, possibly complex.

The roots of that equation fall into three kinds, and each kind contributes its own shape to the answer. The table states the rule; the paragraphs after it explain it in words.

| Kind of root | What it looks like | What it contributes |
| --- | --- | --- |
| One real root, appearing once | a single number m | a constant times the exponential $e^{mx}$ |
| One real root, appearing twice | the same number m twice | a constant plus a constant times x, all multiplied by $e^{mx}$ |
| A pair of complex roots | two numbers of the form a plus or minus ib | $e^{ax}$ times a cosine of bx plus a sine of bx |

Reading the table: the word root means a number that makes the auxiliary polynomial zero. The phrase appearing twice means that the same number is a root more than once, which happens when the polynomial has a squared factor. The letters a and b in the complex row are ordinary real numbers, and the small letter i stands for the square root of minus one.

The first row is the familiar exponential. The second row is the interesting one: a doubled root forces an extra factor of x, because otherwise there would be only one solution where the order demands two. The third row says that a complex pair is converted into genuine real cosines and sines, since a real problem deserves a real answer.

### 2.4 The substitution that solves the Cauchy–Euler equation

> **Theorem (Reduction of the Cauchy–Euler equation).** If x is positive and we write x as the exponential of a new variable t, then the Cauchy–Euler equation becomes an equation with constant coefficients in t, of the same order, and it can be solved by the auxiliary-equation method.

The substitution is written like this: set x equal to $e^{t}$, which is the same as saying t is the natural logarithm of x. The new variable t is called the new independent variable. After the substitution the equation contains only t, not x.

The reason this works is the cancellation described in the photograph picture. When a power of x meets a derivative of the same order, the powers of x cancel exactly and only numbers remain. The next section derives this in detail; for now the important point is that the Cauchy–Euler equation is never solved directly. It is always converted first.

### 2.5 The letter theta

In the new variable t, differentiation is written with the Greek letter theta.

$$
\theta=\frac{d}{dt}
$$

The letter theta is used instead of D so that there is no confusion between differentiating with respect to x and differentiating with respect to t. Once the substitution has been made, the whole equation is written in theta, and it is a polynomial equation in theta with constant numbers as coefficients.

The two basic translations are short enough to memorise.

$$
x\frac{dy}{dx}=\theta y
$$

$$
x^{2}\frac{d^{2}y}{dx^{2}}=\theta(\theta-1)y
$$

The first says that multiplying the first derivative by x is the same as differentiating with respect to t. The second says that multiplying the second derivative by $x^{2}$ is the same as applying the operator theta times theta minus one. The subtraction of one in the second formula is the fingerprint of the whole method, and it is the detail most often dropped.

For higher orders the pattern continues with more subtractions.

$$
x^{3}\frac{d^{3}y}{dx^{3}}=\theta(\theta-1)(\theta-2)y
$$

The rule in words is this: the k-th derivative multiplied by $x^{k}$ becomes theta times theta minus one times theta minus two, and so on, with exactly k factors in the product, the last one being theta minus k minus one.

### 2.6 Legendre's substitution

> **Theorem (Reduction of Legendre's equation).** If ax plus b is positive and we write ax plus b as the exponential of a new variable t, then Legendre's equation becomes an equation with constant coefficients in t, in which each term carries an extra factor of a raised to the power of the derivative.

The substitution is: set ax plus b equal to $e^{t}$, which is the same as saying t is the natural logarithm of ax plus b.

The translation rules are the same as before but with the extra factor of a.

$$
(ax+b)\frac{dy}{dx}=a\theta y
$$

$$
(ax+b)^{2}\frac{d^{2}y}{dx^{2}}=a^{2}\theta(\theta-1)y
$$

$$
(ax+b)^{3}\frac{d^{3}y}{dx^{3}}=a^{3}\theta(\theta-1)(\theta-2)y
$$

Two things must be done that a student often forgets. First, every term needs its factor of a raised to the matching power. Second, the right-hand member must be rewritten in terms of t, because x itself equals $e^{t}$ minus b, all divided by a, and the forcing term depends on x.

### 2.7 Resonance in one sentence

> **Definition (Resonance).** Resonance occurs when the forcing term has the same exponential shape as one of the pieces of the complementary function.

When resonance occurs, the particular integral needs an extra factor of x, in the constant-coefficient case, or an extra factor of the natural logarithm of x, in the Cauchy–Euler case. Without the extra factor the trial function duplicates a piece already present in the complementary function, and the equations for its coefficients have no solution. The extra factor is the mathematical trace of a response that grows without bound because energy is being fed in at a rate the system already supports.

## 3. Formal Proofs, Derivations, and Methods

### 3.1 Where x times y prime equals theta y comes from

Take x positive, and write x as $e^{t}$, so that t is the natural logarithm of x. The chain rule of differentiation says that differentiating with respect to x can be replaced by differentiating with respect to t and then multiplying by the rate at which t changes as x changes.

That rate is one divided by x, because the derivative of the natural logarithm is one over the variable. So

$$
\frac{dy}{dx}=\frac{dy}{dt}\cdot\frac{1}{x} .
$$

Multiply both sides by x and the fraction disappears.

$$
x\frac{dy}{dx}=\frac{dy}{dt}=\theta y
$$

Notice carefully what this says and what it does not say. It does not say that differentiating with respect to x is the same as differentiating with respect to t. It says that multiplying the first derivative by x is the same as differentiating with respect to t. The multiplier x is doing real work, and it must never be dropped.

### 3.2 Where x squared times y double prime comes from

Apply the same chain rule to the first derivative, remembering that the first derivative is itself a function of t and therefore of x. Differentiate the product of one over x and the derivative of y with respect to t.

$$
\frac{d^{2}y}{dx^{2}}=-\frac{1}{x^{2}}\frac{dy}{dt}+\frac{1}{x}\cdot\frac{1}{x}\cdot\frac{d^{2}y}{dt^{2}}
$$

The minus sign comes from differentiating one over x. Combine the two terms over the common denominator $x^{2}$.

$$
\frac{d^{2}y}{dx^{2}}=\frac{1}{x^{2}}\left(\theta^{2}-\theta\right)y
$$

Multiply by $x^{2}$ and the identity appears.

$$
x^{2}\frac{d^{2}y}{dx^{2}}=\theta(\theta-1)y
$$

The subtraction of theta is exactly the term produced by the minus sign, and that is why the second-order identity is not simply theta squared. A student who writes theta squared has lost that term.

### 3.3 The pattern for the third and fourth orders

The same computation repeated produces the higher identities, and the result is a list worth memorising in expanded form, because examinations usually require the expanded version.

$$
x^{3}\frac{d^{3}y}{dx^{3}}=\theta^{3}-3\theta^{2}+2\theta
$$

$$
x^{4}\frac{d^{4}y}{dx^{4}}=\theta^{4}-6\theta^{3}+11\theta^{2}-6\theta
$$

Look at the numbers: one and zero, then one, three and two, then one, six, eleven and six. They are not the numbers of Pascal's triangle, and writing theta cubed minus three theta squared plus three theta minus one instead of theta cubed minus three theta squared plus two theta is a mistake that changes the whole answer.

The general statement is proved by repeating the same step. Each differentiation brings down one more multiplication by x and one more subtraction, and after k steps the product has exactly k factors.

$$
x^{k}\frac{d^{k}y}{dx^{k}}=\theta(\theta-1)(\theta-2)\cdots(\theta-k+1)y
$$

### 3.4 Why a power of x is the natural guess

For the homogeneous Cauchy–Euler equation, try a solution of the form y equals x raised to a power m, where m is a number to be determined.

Differentiate that guess k times. Each differentiation lowers the power by one and multiplies by a factor that decreases by one at each step.

$$
\frac{d^{k}y}{dx^{k}}=m(m-1)(m-2)\cdots(m-k+1)x^{m-k}
$$

Now multiply by $x^{k}$, as the equation demands, and the powers of x cancel completely.

$$
x^{k}\frac{d^{k}y}{dx^{k}}=m(m-1)(m-2)\cdots(m-k+1)x^{m}
$$

Substituting into the equation and taking out the common factor x raised to m leaves an ordinary polynomial equation in the number m. That polynomial is the auxiliary equation, and its roots give the possible values of m.

This is the payoff of the whole method: a differential equation has been converted into a polynomial equation in a single number. The polynomial equation is solved by ordinary algebra, and each of its roots produces one solution of the differential equation.

### 3.5 Six steps for a Cauchy–Euler equation

The following procedure always works when x is positive.

1. Write the equation so that the coefficient of the highest derivative is exactly the matching power of x. Divide through by any extra constant if necessary.
2. Replace each combination of a power of x with a derivative, using the list in Section 3.3. Work from the highest order downward so that no term is left in the old form.
3. Rewrite the right-hand member in the new variable t, using the fact that x equals $e^{t}$.
4. Solve the resulting equation with constant coefficients: write down the auxiliary equation, find all its roots, and build the complementary function from the three kinds of root.
5. Find one particular integral, using the fact that the exponential with exponent r divided by the value of the auxiliary polynomial at r works whenever that value is not zero.
6. Return to the original variable by replacing t with the natural logarithm of x everywhere, and then verify the answer by substitution.

### 3.6 Six steps for a Legendre equation

The procedure is the same with three small changes.

1. Identify the constants a and b in the expression ax plus b, and check that each derivative is accompanied by the matching power of that expression.
2. Set ax plus b equal to $e^{t}$, and write t as the natural logarithm of ax plus b.
3. Replace each combination by the theta expression, including the factor of a raised to the matching power in every single term.
4. Rewrite the right-hand member in t. This step cannot be skipped, and it is the step most often omitted.
5. Solve the constant-coefficient equation, then return to x using the fact that $e^{t}$ equals ax plus b.
6. Verify by substitution into the original equation, remembering that each differentiation with respect to x brings out a factor of a.

### 3.7 How to check an answer without redoing the work

A check is not a repeat of the solution; it is a targeted test that catches the errors the solution method is most likely to have produced. Three checks cover almost everything.

Check the number of constants. It must equal the order of the equation, and it must be possible to choose them independently.

Check the particular integral alone. Substitute only the particular integral into the original equation, keeping every variable coefficient attached to its derivative, and confirm that the two sides agree. This check detects wrong powers of theta, missing factors of a, and mistakes in the forcing term.

Check the shape of the answer. A repeated root must produce a logarithm, an equation with a real solution set must not contain the symbol i, and every exponent in the answer must match an exponent that appeared in the reduced equation.

## 4. Representative Worked Examples and Solutions

### 4.1 Problem: a third-order equation with three different roots

Solve

$$
\frac{d^{3}y}{dx^{3}}-6\frac{d^{2}y}{dx^{2}}+11\frac{dy}{dx}-6y=0 .
$$

### 4.2 Solution: factor the operator and read off three exponentials

Step 1. Write the equation in operator form, using the letter D for differentiation with respect to x.

$$
\left(D^{3}-6D^{2}+11D-6\right)y=0
$$

Step 2. Write the auxiliary equation by replacing D with the number m.

$$
m^{3}-6m^{2}+11m-6=0
$$

Step 3. Find one root by trial. Trying m equal to one gives one minus six plus eleven minus six, which is zero, so m equal to one is a root.

Step 4. Divide out the factor m minus one to obtain the remaining quadratic.

$$
m^{3}-6m^{2}+11m-6=(m-1)(m^{2}-5m+6)
$$

Step 5. Factor the quadratic.

$$
m^{2}-5m+6=(m-2)(m-3)
$$

Step 6. So the three roots are one, two and three, all different and all real. Each contributes one exponential.

$$
y=c_{1}e^{x}+c_{2}e^{2x}+c_{3}e^{3x}
$$

Step 7. Count the constants. There are three, and the equation is of order three, so the count is right.

Step 8. Verify the middle term by differentiating twice. For y equal to $e^{2x}$ the derivatives are two times $e^{2x}$, then four times $e^{2x}$, then eight times $e^{2x}$.

$$
8e^{2x}-6\left(4e^{2x}\right)+11\left(2e^{2x}\right)-6e^{2x}=(8-24+22-6)e^{2x}=0
$$

The bracketed number is zero, so the term really is a solution.

### 4.3 Problem: a doubled root

Solve

$$
\frac{d^{2}y}{dx^{2}}-4\frac{dy}{dx}+4y=0 .
$$

### 4.4 Solution: a repeated root forces an extra factor of x

Step 1. Write the auxiliary equation.

$$
m^{2}-4m+4=0
$$

Step 2. Recognise a perfect square.

$$
(m-2)^{2}=0
$$

Step 3. The only root is two, and it appears twice. One copy gives the exponential, and the second copy gives the exponential multiplied by x.

$$
y=\left(c_{1}+c_{2}x\right)e^{2x}
$$

Step 4. Count the constants. There are two, matching the order.

Step 5. Verify the second piece, whose derivatives are $y'=(1+2x)e^{2x}$ and $y''=(4+4x)e^{2x}$.

$$
(4+4x)e^{2x}-4(1+2x)e^{2x}+4xe^{2x}
$$

Step 6. Collect the coefficients of $e^{2x}$ and of x times $e^{2x}$ separately.

$$
e^{2x}\left(4-4\right)+xe^{2x}\left(4-8+4\right)=0
$$

Both vanish, so the doubled root really does produce the extra factor of x.

### 4.5 Problem: a pair of complex roots

Solve

$$
\frac{d^{2}y}{dx^{2}}+y=0 .
$$

### 4.6 Solution: a complex pair becomes a cosine and a sine

Step 1. Write the auxiliary equation.

$$
m^{2}+1=0
$$

Step 2. The roots are the square root of minus one and its negative, which are written as i and minus i.

Step 3. The real part of these roots is zero and the imaginary part is one, so the exponential factor $e^{0x}$ is simply one, and the cosine and sine have frequency one.

$$
y=c_{1}\cos x+c_{2}\sin x
$$

Step 4. Verify the sine term. Its second derivative is minus the sine, so the sum with the function itself is zero.

$$
-\sin x+\sin x=0
$$

Step 5. Explain the shape. The answer is a genuine real function even though the roots were complex, because the two complex exponentials combine in pairs to give a cosine and a sine.

### 4.7 Problem: a Cauchy–Euler equation of order two

Solve

$$
x^{2}\frac{d^{2}y}{dx^{2}}-2x\frac{dy}{dx}+2y=0, \qquad x>0 .
$$

### 4.8 Solution: reduce to theta and factor

Step 1. Replace the two combinations using the identities from Section 3.3.

$$
\left[\theta(\theta-1)-2\theta+2\right]y=0
$$

Step 2. Multiply out and collect.

$$
\theta^{2}-\theta-2\theta+2=\theta^{2}-3\theta+2
$$

Step 3. The reduced equation is therefore an ordinary constant-coefficient equation in the variable t.

$$
\left(\theta^{2}-3\theta+2\right)y=0
$$

Step 4. Write its auxiliary equation and factor.

$$
m^{2}-3m+2=(m-1)(m-2)=0
$$

Step 5. The roots are one and two, both different and both real, so the solution in t is a sum of two exponentials.

$$
y=c_{1}e^{t}+c_{2}e^{2t}
$$

Step 6. Return to x, using the fact that $e^{t}$ is x and $e^{2t}$ is $x^{2}$.

$$
y=c_{1}x+c_{2}x^{2}
$$

Step 7. Verify the first term, whose derivatives are one and zero.

$$
x^{2}(0)-2x(1)+2x=0
$$

Step 8. Verify the second term, whose derivatives are two times x and two.

$$
x^{2}(2)-2x(2x)+2x^{2}=2x^{2}-4x^{2}+2x^{2}=0
$$

Both checks succeed, so the general solution is correct.

### 4.9 Problem: a Legendre equation with small numbers

Solve

$$
(x+1)^{2}\frac{d^{2}y}{dx^{2}}-4(x+1)\frac{dy}{dx}+6y=0, \qquad x>-1 .
$$

### 4.10 Solution: substitute and carry the factor through

Step 1. The expression is x plus one, so a is one and b is one. Because a is one, the extra factor is one to every power, which is one, and the calculation looks exactly like a Cauchy–Euler calculation.

Step 2. Apply the identities with a equal to one.

$$
(x+1)^{2}D^{2}=\theta(\theta-1), \qquad (x+1)D=\theta
$$

Step 3. Assemble the reduced operator.

$$
\theta(\theta-1)-4\theta+6=\theta^{2}-5\theta+6
$$

Step 4. Factor the auxiliary polynomial.

$$
m^{2}-5m+6=(m-2)(m-3)
$$

Step 5. The roots two and three are different and real, so the answer is a sum of two powers.

$$
y=c_{1}(x+1)^{2}+c_{2}(x+1)^{3}
$$

Step 6. Verify the first term by writing u for x plus one, so that the first derivative is twice u and the second derivative is two.

$$
u^{2}(2)-4u(2u)+6u^{2}=2u^{2}-8u^{2}+6u^{2}=0
$$

Step 7. Verify the second term, whose first derivative is three times $u^{2}$ and whose second derivative is six times u.

$$
u^{2}(6u)-4u\left(3u^{2}\right)+6u^{3}=6u^{3}-12u^{3}+6u^{3}=0
$$

### 4.11 Problem: a Cauchy–Euler equation with complex roots

Solve

$$
x^{2}\frac{d^{2}y}{dx^{2}}+x\frac{dy}{dx}+9y=0, \qquad x>0 .
$$

### 4.12 Solution: the cosine and sine now depend on the logarithm

Step 1. Replace the combinations and collect.

$$
\left[\theta(\theta-1)+\theta+9\right]y=\left(\theta^{2}+9\right)y=0
$$

Step 2. The auxiliary equation is m squared plus nine equals zero, so the roots are three times i and minus three times i.

Step 3. The imaginary part is three, so the cosine and sine have frequency three in the variable t.

$$
y=c_{1}\cos(3t)+c_{2}\sin(3t)
$$

Step 4. Return to x by replacing t with the natural logarithm of x.

$$
y=c_{1}\cos(3\ln x)+c_{2}\sin(3\ln x)
$$

Step 5. Interpret the answer. The oscillations happen in the logarithm of x, not in x itself, so the waves become wider as x grows. That behaviour is typical of this family of equations and is the reason the reduction is worth doing carefully.

### 4.13 Problem: a Cauchy–Euler equation with a forcing term

Solve

$$
x^{2}\frac{d^{2}y}{dx^{2}}-2x\frac{dy}{dx}+2y=x, \qquad x>0 .
$$

### 4.14 Solution: recognise the resonance and add a logarithm

Step 1. From the work of Section 4.7, the reduced equation is the following, and the forcing term x becomes $e^{t}$.

$$
\left(\theta^{2}-3\theta+2\right)y=e^{t}
$$

Step 2. The complementary function is the one already found.

$$
y_{c}=c_{1}x+c_{2}x^{2}
$$

Step 3. Try the simple rule first and discover that it fails, because the exponent one is a root of the auxiliary polynomial.

$$
P(1)=1-3+2=0
$$

Step 4. Since the exponent one is a single root, the particular integral needs one factor of t, and the divisor is the derivative of the auxiliary polynomial evaluated at one.

$$
P'(m)=2m-3, \qquad P'(1)=-1
$$

Step 5. Apply the rule for a single root.

$$
y_{p}=\frac{t\,e^{t}}{P'(1)}=-t\,e^{t}
$$

Step 6. Return to x.

$$
y=c_{1}x+c_{2}x^{2}-x\ln x
$$

Step 7. Differentiate the particular integral twice, using the product rule for the first derivative.

$$
y=-x\ln x, \qquad \frac{dy}{dx}=-(\ln x+1), \qquad \frac{d^{2}y}{dx^{2}}=-\frac{1}{x}
$$

Step 8. Substitute into the left-hand side, keeping each power of x attached to its own derivative.

$$
x^{2}\left(-\frac{1}{x}\right)-2x\left(-(\ln x+1)\right)+2\left(-x\ln x\right)
$$

Step 9. Simplify term by term.

$$
-x+2x\ln x+2x-2x\ln x
$$

Step 10. The logarithmic terms cancel and the two remaining terms combine to give exactly the right-hand member.

$$
-x+2x=x
$$

Step 11. The check succeeds, so the general solution is the one in Step 6. The appearance of the natural logarithm is the signature of resonance: the forcing term had the same shape as one piece of the complementary function, so the response had to grow.

## 5. Mathematical Extensions, Limits, and Common Errors

### 5.1 Beginner misconceptions

The following list collects the mistakes that appear most often in first attempts. Each is stated as the mistaken belief, followed by the correction.

Believing that the order of an equation is the highest power of y. The order counts differentiations, not powers. The equation in which y is cubed is still of order two if the second derivative is the highest derivative present.

Believing that a homogeneous equation must have constant coefficients. Homogeneity is about the right-hand member being zero and about every term having the same degree in the unknown. The Cauchy–Euler equation with variable coefficients is perfectly capable of being homogeneous.

Believing that a doubled root needs no extra factor. Each root supplies one solution per unit of multiplicity, and a doubled root supplies only one distinct exponential unless a factor of x is added.

Believing that a complex root means the answer contains i. A real equation with real coefficients always has its complex roots in conjugate pairs, and each pair combines into a cosine and a sine with no imaginary symbol surviving.

Believing that theta and D are the same thing. They are derivatives with respect to different variables, and they differ by a factor of x. The combination x times D equals theta, but D alone does not.

Believing that x squared times the second derivative becomes theta squared. The correct operator is theta times theta minus one, and dropping the minus one changes the roots and therefore the whole answer.

Believing that the factor of a can be ignored in Legendre's equation. It cannot. Each differentiation with respect to x multiplies by a, so the factor appears to the power of the derivative order in every term.

Believing that the right-hand member can be left in terms of x after the substitution. It must be rewritten in t, because the particular integral is computed in the variable t.

Believing that a particular integral may contain an arbitrary constant. It may not; any constant that survives belongs to the complementary function and should be absorbed there.

Believing that a single trial function can handle a right-hand side made of several different pieces. Each piece is treated separately, and the results are added.

### 5.2 The case where the substitution fails

The substitution works because the powers of x and the orders of the derivatives match. When they do not match, the substitution still can be made, but it produces an equation whose coefficients depend on t, and the auxiliary-equation method no longer applies.

Consider an equation in which the second derivative is multiplied by $x^{2}$ but the first derivative is multiplied by a constant rather than by x. After the substitution the second-derivative term becomes a theta expression with constant coefficients, but the first-derivative term becomes a multiple of one over x times theta, and one over x is $e^{-t}$. The reduced equation therefore has coefficients mixing constants with exponentials of t, and it is not a constant-coefficient equation at all.

The lesson is to check the pattern before starting. Every derivative must be accompanied by the matching power of the same expression, and every coefficient in front must be a constant. If even one term breaks the pattern, this method is the wrong tool, and a series solution or a numerical method is the appropriate route.

### 5.3 The point where the equation breaks down

The Cauchy–Euler equation has a singular point at x equal to zero, and Legendre's equation has one where ax plus b is zero. At those points the coefficient of the highest derivative vanishes, so the equation stops being of the stated order, and the theory of this note does not apply.

The practical consequence is that solutions are asserted on one side of the singular point. A solution obtained with the substitution x equals $e^{t}$ is a solution for positive x. For negative x the same formulae hold with x replaced by its absolute value and the logarithm replaced by the logarithm of the absolute value.

This is not a technicality to be glossed over. Near the singular point the behaviour of solutions can be very different: some vanish, some blow up, and some oscillate infinitely often as the point is approached. Stating the interval of validity is part of a complete answer.

### 5.4 What comes next

The method of this note is the doorway to a much larger theory. Any equation whose coefficients behave like powers of the distance from a point can be attacked by assuming a solution in the form of a power series with an unknown exponent, and the exponent is found from an equation of exactly the same shape as the auxiliary equation used here. When two exponents coincide, a logarithm appears, for exactly the reason that a doubled root produces a logarithm in the Cauchy–Euler case.

The deeper reason for the logarithm is worth stating plainly. When the auxiliary equation has a repeated root, the equation fails to supply two genuinely different solutions of the expected shape; the second must be manufactured by differentiating the first with respect to the exponent. That manufacturing process always produces a logarithm, and it is the same process in every family of equations where repeated roots occur.

Finally, the identities relating powers of x to derivatives in t are a special case of a general principle of calculus: changing the independent variable changes a linear differential operator into another linear differential operator, by a definite rule involving the derivatives of the change. Only for the Cauchy–Euler and Legendre families does that rule produce constant coefficients, and that is exactly why these two families, out of all equations with variable coefficients, are the ones that can always be solved completely by elementary means.
