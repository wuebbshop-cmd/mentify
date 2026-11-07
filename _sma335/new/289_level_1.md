## 1. Foundational Concepts, Definitions, and Axioms

### 1.1 A picture to hold on to

Imagine a machine that is fed a moving signal and answers by combining three measurements of that signal: its current size, its speed of change, and the speed at which that speed is itself changing. Suppose the machine has fixed dials set to the numbers one, five and six, and suppose we ask a single question of it. Which signals make the machine answer exactly zero, always, no matter what the input clock reads?

That question is the whole subject of this note. The answer is not a number but a function: a rule that turns an input into an output. Picture a car driving along a straight road, where the dials measure position, velocity and acceleration. If the machine must always give zero, the position of the car cannot be arbitrary; it must evolve in a very particular pattern, and in fact there are only two basic patterns available, with every valid motion being a blend of those two.

Think of a recipe with fixed proportions. The cook is told to combine one part of the current amount of dough, five parts of the rate at which dough is being added, and six parts of the rate at which that rate is changing, and to make the mixture come out to nothing. A cook who follows the recipe exactly produces one specific kind of dough, and there are exactly two starting mixtures that work, so every acceptable dough is a blend of them.

The mathematical name for such a recipe is a second-order homogeneous linear differential equation with constant coefficients. The rest of this section explains each word in that name, and explains why the recipe behaves so predictably.

### 1.2 The shape of the equation

We write the unknown function as $y$ and the input variable as $x$. The symbol $y$ therefore stands for a rule, not for a number, and the equation will be satisfied by some rules and not by others. The first derivative $\frac{dy}{dx}$ records how fast $y$ changes as $x$ changes, and the second derivative $\frac{d^{2}y}{dx^{2}}$ records how fast the first derivative itself changes.

With those three quantities the standard shape is

$$
a_0\frac{d^{2}y}{dx^{2}}+a_1\frac{dy}{dx}+a_2y=0 .
$$

Each letter with a subscript is a fixed number, called a coefficient. The number $a_0$ multiplies the second derivative, the number $a_1$ multiplies the first derivative, and the number $a_2$ multiplies the function itself. The condition $a_0\neq 0$ is essential: if $a_0$ were zero the second derivative would disappear and we would be dealing with a first-order problem instead.

A concrete instance makes the shape familiar. Taking $a_0=1$, $a_1=-5$ and $a_2=6$ gives

$$
\frac{d^{2}y}{dx^{2}}-5\frac{dy}{dx}+6y=0 ,
$$

and the question becomes: which functions $y$ make this combination vanish for every value of $x$?

### 1.3 What "second order" means

The order of a differential equation is the order of the highest derivative that appears in it. In the equation above the highest derivative is the second derivative, so the order is two. In words: the equation involves how a function changes twice over.

The order is not a detail. It decides how many free choices the answer contains. A first-order equation leaves one free choice, called an arbitrary constant. A second-order equation leaves two. A third-order equation leaves three. This is the most reliable check available to a beginner, because a second-order answer that contains only one constant is always wrong, no matter how convincing it looks.

Here is a first-order example for contrast. The equation

$$
\frac{dy}{dx}=2x
$$

has order one and its answer is $y=x^{2}+C$, with one free choice $C$. The second-order example

$$
\frac{d^{2}y}{dx^{2}}=6x
$$

has order two and its answer is $y=x^{3}+C_1x+C_2$, with two free choices. Each integration raises the count of free choices by one, and two integrations produce two of them.

### 1.4 What "constant coefficients" means

A coefficient is constant when it is a plain fixed number such as $1$, $-5$ or $6$, and not a formula involving the input variable. The equation

$$
x^{2}\frac{d^{2}y}{dx^{2}}+x\frac{dy}{dx}+y=0
$$

is second order and linear, but its coefficients are the expressions $x^{2}$ and $x$, which change as $x$ changes, so it is not an equation with constant coefficients. The equation

$$
\frac{d^{2}y}{dx^{2}}-5\frac{dy}{dx}+6y=0
$$

has the constant coefficients $1$, $-5$ and $6$, so it is. The distinction matters because the solution method in this note depends entirely on the coefficients being fixed numbers; a single occurrence of $x$ in a coefficient breaks the method and requires a different technique.

### 1.5 What "linear" means

An equation is linear when the unknown function and each of its derivatives appear only to the first power, are never multiplied by one another, and are never hidden inside a function such as a square root, a sine or a logarithm. The coefficients may involve the input variable, but they may never involve the unknown function.

The equation

$$
\frac{d^{2}y}{dx^{2}}-5\frac{dy}{dx}+6y=0
$$

is linear. Reading it term by term, the quantities $\frac{d^{2}y}{dx^{2}}$, $\frac{dy}{dx}$ and $y$ each appear once, each to the first power, and none multiplies another.

The equation

$$
3\frac{d^{2}y}{dx^{2}}-2\left(\frac{dy}{dx}\right)^{2}+8y=\ln x
$$

is not linear, because the first derivative is squared. The equation

$$
5x\frac{d^{3}y}{dx^{3}}+8xy\frac{d^{2}y}{dx^{2}}-9\frac{dy}{dx}+xy=xe^{x}
$$

is not linear, because the second derivative is multiplied by $y$. The equation

$$
5\frac{d^{2}y}{dx^{2}}-8x\frac{dy}{dx}+2y=xy
$$

is not linear either, because the right-hand side contains $y$ multiplied by $x$, and the right-hand side of a linear equation is allowed to depend on the input variable only.

Linearity is worth this much attention because it delivers a free bonus: solutions may be added together and multiplied by numbers, and the result is still a solution. That bonus is used constantly in the rest of the note.

### 1.6 What "homogeneous" means

The word homogeneous, in this context, means that every term is of the same first degree in the unknown function and its derivatives, and that nothing is left over on the right-hand side. Practically, a second-order linear equation is homogeneous exactly when it can be written with zero on the right.

So

$$
a_0\frac{d^{2}y}{dx^{2}}+a_1\frac{dy}{dx}+a_2y=0
$$

is homogeneous, while

$$
a_0\frac{d^{2}y}{dx^{2}}+a_1\frac{dy}{dx}+a_2y=F(x)
$$

is non-homogeneous, provided the extra term $F(x)$ is genuinely present. The word describes the left-hand side; the equation as a whole is homogeneous or non-homogeneous according to whether that extra term is zero.

Three examples of non-homogeneous second-order equations are

$$
2\frac{d^{2}y}{dx^{2}}+5\frac{dy}{dx}-6y=xe^{x} ,
$$

$$
\frac{d^{2}y}{dx^{2}}-3\frac{dy}{dx}+7y=\sin x+x^{2} ,
$$

and

$$
\frac{d^{2}y}{dx^{2}}+4y=8 .
$$

In each case the right-hand side is a function of the input variable alone, which is what makes the equation non-homogeneous but still linear.

The practical difference is large. A homogeneous equation can always be satisfied by the function that is identically zero, because zero of everything is zero. A non-homogeneous equation cannot, since its right-hand side is not zero. This single observation explains why the homogeneous problem is solved first and separately, and why its answer is later combined with one extra solution of the full problem.

### 1.7 A shorthand: operator notation

Writing the derivative symbols over and over is tiring, so a shorthand is used. The letter $D$ stands for the instruction differentiate with respect to $x$. Then $D^{2}$ means differentiate twice, $D^{3}$ means differentiate three times, and so on.

With this shorthand the equation

$$
5\frac{d^{2}y}{dx^{2}}-3\frac{dy}{dx}+8y=0
$$

is written as

$$
5D^{2}y-3Dy+8y=0 ,
$$

or, collecting the instructions in a bracket,

$$
\left(5D^{2}-3D+8\right)y=0 .
$$

In general the equation

$$
a_0\frac{d^{2}y}{dx^{2}}+a_1\frac{dy}{dx}+a_2y=0
$$

becomes

$$
\left(a_0D^{2}+a_1D+a_2\right)y=0 ,
$$

and the bracket is often named $f(D)$, so that the equation reads

$$
f(D)y=0 .
$$

The bracket is not a number, it is a recipe made of differentiations and multiplications, but it behaves algebraically like a quadratic expression in the symbol $D$. That resemblance is the reason the whole method works.

### 1.8 What counts as a solution

A solution is a function that, when substituted into the equation together with its derivatives, makes the two sides equal for every value of the input variable. Equality at one or two isolated points is not enough; the equation must be satisfied identically on an interval.

Take the equation

$$
\frac{d^{2}y}{dx^{2}}-5\frac{dy}{dx}+6y=0
$$

and test the function $y=e^{3x}$. Its first derivative is $3e^{3x}$ and its second derivative is $9e^{3x}$. Substituting,

$$
9e^{3x}-5\left(3e^{3x}\right)+6e^{3x}=\left(9-15+6\right)e^{3x}=0 ,
$$

so the function is a solution on the whole real line. Testing $y=e^{2x}$ instead gives

$$
4e^{2x}-5\left(2e^{2x}\right)+6e^{2x}=\left(4-10+6\right)e^{2x}=0 ,
$$

so that is a solution too. Testing $y=x$ gives first derivative one and second derivative zero, so the combination is $-5+6x$, which is not zero for every $x$, and $y=x$ is not a solution.

### 1.9 The guess that unlocks everything

The equation asks for a function whose derivatives recombine into nothing. The exponential function is the natural candidate, because differentiating it returns a constant multiple of itself. If $y=e^{mx}$ for some fixed number $m$, then

$$
\frac{dy}{dx}=me^{mx} \qquad \text{and} \qquad \frac{d^{2}y}{dx^{2}}=m^{2}e^{mx} .
$$

Substituting these three expressions into the equation gives

$$
\left(a_0m^{2}+a_1m+a_2\right)e^{mx}=0 .
$$

The exponential factor is never zero, so the bracket must be zero. All that remains is an ordinary quadratic equation in the number $m$, and quadratics are something we can always handle. This is the central idea of the note, and everything that follows is bookkeeping around it.

The quadratic is called the auxiliary equation, or the characteristic equation, of the differential equation. For the example with coefficients $1$, $-5$ and $6$ it reads

$$
m^{2}-5m+6=0 .
$$

Factorising gives

$$
\left(m-2\right)\left(m-3\right)=0 ,
$$

so the two acceptable numbers are $m=2$ and $m=3$. Those two numbers produce the two basic solutions $e^{2x}$ and $e^{3x}$ discovered by trial in the previous section, and the general solution is any blend of them.

## 2. Theorems, Lemmas, and Analytical Properties

### 2.1 The three-case theorem

The quadratic $a_0m^{2}+a_1m+a_2=0$ can behave in exactly three ways, and each way gives a different general solution. The statement below is the one result that must be memorised.

Suppose the differential equation is

$$
a_0\frac{d^{2}y}{dx^{2}}+a_1\frac{dy}{dx}+a_2y=0
$$

with $a_0$, $a_1$ and $a_2$ constants and $a_0\neq 0$.

If the auxiliary equation has two different real roots $m_1$ and $m_2$, then every solution has the form

$$
y=c_1e^{m_1x}+c_2e^{m_2x} .
$$

If the auxiliary equation has one repeated real root $m$, then every solution has the form

$$
y=c_1e^{mx}+c_2xe^{mx} .
$$

If the auxiliary equation has conjugate complex roots written as $a+ib$ and $a-ib$, with $b\neq 0$, then every solution has the form

$$
y=e^{ax}\left(c_1\cos bx+c_2\sin bx\right) .
$$

In each case $c_1$ and $c_2$ are arbitrary constants, and each case supplies exactly two of them, matching the order two of the equation.

The three cases are exhaustive. A quadratic with real coefficients has a discriminant, the number $a_1^{2}-4a_0a_2$. If the discriminant is positive there are two different real roots, if it is zero there is one repeated root, and if it is negative there are two conjugate complex roots. Nothing else can happen.

### 2.2 Adding solutions together

The superposition principle says that if two functions both solve a linear homogeneous equation, then any combination of them with constant multipliers also solves it.

The reason is short. Differentiation is additive, so the derivative of a sum is the sum of the derivatives, and a constant multiplier slides through a derivative untouched. Applying the whole recipe $f(D)$ to the combination $c_1y_1+c_2y_2$ therefore gives

$$
f(D)\left(c_1y_1+c_2y_2\right)=c_1f(D)y_1+c_2f(D)y_2 .
$$

If both $f(D)y_1$ and $f(D)y_2$ are zero, the right-hand side is zero as well, so the combination is a solution. This is exactly why a general solution is written as a blend rather than as a single function.

Superposition can fail badly for non-linear equations. The equation

$$
\frac{d^{2}y}{dx^{2}}+y^{2}=0
$$

is not linear, and doubling a solution does not produce another solution. The property must be earned by linearity before it may be used.

### 2.3 Are the two solutions really independent?

Two solutions are called independent when neither is a constant multiple of the other. The pair $e^{2x}$ and $e^{3x}$ is independent, because no single number can turn one into the other. The pair $e^{2x}$ and $5e^{2x}$ is not independent, and blending them achieves nothing new, since the blend collapses to one constant times a single exponential.

A standard test for independence is the Wronskian, a small determinant built from the two functions and their first derivatives,

$$
W=y_1\frac{dy_2}{dx}-y_2\frac{dy_1}{dx} .
$$

If the Wronskian is non-zero the two functions are independent. For the pair $e^{2x}$ and $e^{3x}$ the calculation is

$$
W=e^{2x}\cdot 3e^{3x}-e^{3x}\cdot 2e^{2x}=3e^{5x}-2e^{5x}=e^{5x} ,
$$

which is never zero, so the pair is independent. For the dependent pair $e^{2x}$ and $5e^{2x}$ the same calculation gives

$$
W=e^{2x}\cdot 10e^{2x}-5e^{2x}\cdot 2e^{2x}=10e^{4x}-10e^{4x}=0 ,
$$

confirming that the second function adds nothing.

The Wronskian is the reason each of the three cases in Section 2.1 really does deliver two usable solutions. In the repeated-root case the pair is $e^{mx}$ and $xe^{mx}$, and its Wronskian works out to $e^{2mx}$, which is never zero. In the complex case the pair is $e^{ax}\cos bx$ and $e^{ax}\sin bx$, whose Wronskian is $be^{2ax}$, again never zero because $b$ is not zero.

### 2.4 Two conditions fix two constants

Each of the three general solutions contains two arbitrary constants, so two pieces of information are needed to pin down one particular solution. The usual information is a pair of values at a single point: the value of the function and the value of its derivative at some chosen input. Such a demand is called an initial value problem.

Take the equation

$$
\frac{d^{2}y}{dx^{2}}-3\frac{dy}{dx}+2y=0
$$

with the demands $y=1$ and $\frac{dy}{dx}=0$ at $x=0$. The auxiliary equation is

$$
m^{2}-3m+2=0 ,
$$

which factorises as

$$
\left(m-1\right)\left(m-2\right)=0 ,
$$

so the general solution is

$$
y=c_1e^{x}+c_2e^{2x} .
$$

Substituting $x=0$ into the function gives $c_1+c_2=1$, and substituting $x=0$ into the derivative gives $c_1+2c_2=0$. Subtracting the first equation from the second gives $c_2=-1$, and then $c_1=2$. The particular solution is

$$
y=2e^{x}-e^{2x} .
$$

Checking, at $x=0$ the value is $2-1=1$ and the derivative is $2-2=0$, as required.

### 2.5 Higher order obeys the same rules

Nothing in the method is peculiar to order two. For an equation of order $n$ with constant coefficients, the auxiliary equation has degree $n$, and each real root contributes an exponential, each repeated root contributes extra factors of $x$, and each conjugate pair contributes a damped or amplified sine and cosine. The count of arbitrary constants always equals the order.

The third-order equation

$$
\frac{d^{3}y}{dx^{3}}-6\frac{d^{2}y}{dx^{2}}+11\frac{dy}{dx}-6y=0
$$

has auxiliary equation

$$
m^{3}-6m^{2}+11m-6=0 ,
$$

which factorises as

$$
\left(m-1\right)\left(m-2\right)\left(m-3\right)=0 .
$$

Three different real roots give three independent exponentials, so

$$
y=c_1e^{x}+c_2e^{2x}+c_3e^{3x}
$$

is the general solution, with three constants for an equation of order three.

The fifth-order equation

$$
\frac{d^{5}y}{dx^{5}}-2\frac{d^{4}y}{dx^{4}}+\frac{d^{3}y}{dx^{3}}=0
$$

has auxiliary equation

$$
m^{5}-2m^{4}+m^{3}=0 ,
$$

which factorises as

$$
m^{3}\left(m-1\right)^{2}=0 .
$$

The roots are $0$ repeated three times and $1$ repeated twice. A zero root contributes a constant, because $e^{0x}=1$; repeating it three times contributes $x$ and $x^{2}$ as well. The double root at one contributes $e^{x}$ and $xe^{x}$. The general solution is therefore

$$
y=c_1+c_2x+c_3x^{2}+c_4e^{x}+c_5xe^{x} ,
$$

with five constants for an equation of order five.

## 3. Formal Proofs, Derivations, and Methods

### 3.1 The recipe in five steps

Every question of this type is answered by the same five moves, and writing them down in order prevents nearly all mistakes.

Step one: write the auxiliary equation by replacing each derivative with the corresponding power of $m$, so that the second derivative becomes $m^{2}$, the first derivative becomes $m$, and the function itself becomes one.

Step two: solve the auxiliary equation exactly, by factorising where possible and by the quadratic formula otherwise. Keep surds and imaginary parts exact rather than rounding.

Step three: name the case. Two different real roots, one repeated real root, or a conjugate complex pair.

Step four: write the general solution using the pattern for that case, with two arbitrary constants.

Step five: if initial values are given, substitute them to find the two constants, and then check the answer by substituting back.

### 3.2 Where the auxiliary equation comes from

Take the equation

$$
a_0\frac{d^{2}y}{dx^{2}}+a_1\frac{dy}{dx}+a_2y=0
$$

and try the exponential $y=e^{mx}$, where $m$ is a number still to be found. The derivatives are

$$
\frac{dy}{dx}=me^{mx} \qquad \text{and} \qquad \frac{d^{2}y}{dx^{2}}=m^{2}e^{mx} .
$$

Substituting all three expressions gives

$$
a_0m^{2}e^{mx}+a_1me^{mx}+a_2e^{mx}=0 ,
$$

and factoring out the exponential gives

$$
\left(a_0m^{2}+a_1m+a_2\right)e^{mx}=0 .
$$

Because the exponential is never zero, the bracket must vanish:

$$
a_0m^{2}+a_1m+a_2=0 .
$$

This quadratic is the auxiliary equation. It is worth noticing what has happened: a problem about functions has been converted into a problem about numbers, and the conversion is reversible, because every number $m$ that satisfies the quadratic produces a genuine solution of the differential equation.

### 3.3 Case one: two different real roots

Suppose the auxiliary equation has two different real roots $m_1$ and $m_2$. Then $e^{m_1x}$ and $e^{m_2x}$ are both solutions by construction, and they are independent because their ratio is $e^{(m_1-m_2)x}$, which is not constant when the two roots differ. By superposition every blend

$$
y=c_1e^{m_1x}+c_2e^{m_2x}
$$

is a solution, and because the blend contains two independent constants it is the general solution.

An example makes the arithmetic concrete. For the equation

$$
\frac{d^{2}y}{dx^{2}}+2\frac{dy}{dx}-3y=0
$$

the auxiliary equation is

$$
m^{2}+2m-3=0 ,
$$

which factorises as

$$
\left(m+3\right)\left(m-1\right)=0 .
$$

The roots are $-3$ and $1$, so the general solution is

$$
y=c_1e^{-3x}+c_2e^{x} .
$$

Checking the first exponential, its second derivative is $9e^{-3x}$, its first derivative is $-3e^{-3x}$, and the combination is $9-6-3=0$. Checking the second, the second derivative is $e^{x}$, the first derivative is $e^{x}$, and the combination is $1+2-3=0$. Both checks succeed, so the general solution is correct.

### 3.4 Case two: one repeated root and the extra factor x

Suppose the auxiliary equation has a single repeated root $m$. Then only one exponential is produced, namely $e^{mx}$, and one solution is not enough for an equation of order two. Something else is needed.

The standard device is to try $y=xe^{mx}$, that is, the known solution multiplied by the input variable. Its derivatives are

$$
\frac{dy}{dx}=e^{mx}+mxe^{mx}
$$

and

$$
\frac{d^{2}y}{dx^{2}}=me^{mx}+me^{mx}+m^{2}xe^{mx}=2me^{mx}+m^{2}xe^{mx} .
$$

Substituting into the differential equation gives

$$
a_0\left(2me^{mx}+m^{2}xe^{mx}\right)+a_1\left(e^{mx}+mxe^{mx}\right)+a_2xe^{mx} .
$$

Collecting the terms without a factor of $x$ and the terms with one gives

$$
\left(2a_0m+a_1\right)e^{mx}+x\left(a_0m^{2}+a_1m+a_2\right)e^{mx} .
$$

The bracket multiplying $x$ is the auxiliary equation evaluated at the repeated root, so it is zero. What remains must also vanish, and it does, because a repeated root satisfies $2a_0m+a_1=0$ alongside $a_0m^{2}+a_1m+a_2=0$. Hence $xe^{mx}$ is a solution, and it is independent of $e^{mx}$ because it carries a factor of $x$ that no constant can reproduce.

The general solution in this case is therefore

$$
y=c_1e^{mx}+c_2xe^{mx} ,
$$

often written as

$$
y=\left(c_1+c_2x\right)e^{mx} .
$$

A concrete instance is

$$
\frac{d^{2}y}{dx^{2}}+2\frac{dy}{dx}+y=0 ,
$$

whose auxiliary equation is

$$
m^{2}+2m+1=0 ,
$$

that is

$$
\left(m+1\right)^{2}=0 ,
$$

so $m=-1$ is a double root. The general solution is

$$
y=\left(c_1+c_2x\right)e^{-x} .
$$

Check the second basic solution $y=xe^{-x}$. Its first derivative is $e^{-x}-xe^{-x}$ and its second derivative is $-e^{-x}-\left(e^{-x}-xe^{-x}\right)=xe^{-x}-2e^{-x}$. The combination is

$$
\left(xe^{-x}-2e^{-x}\right)+2\left(e^{-x}-xe^{-x}\right)+xe^{-x} ,
$$

and collecting the coefficients of $e^{-x}$ gives $x-2+2-2x+x=0$. The check succeeds.

### 3.5 Case three: complex roots and where sine and cosine come from

Suppose the auxiliary equation has no real roots. Then its roots are a conjugate pair, written $a+ib$ and $a-ib$, where $a$ and $b$ are real numbers and $b$ is not zero.

Taken at face value, the two solutions would be $e^{(a+ib)x}$ and $e^{(a-ib)x}$. Splitting the exponent gives

$$
e^{(a+ib)x}=e^{ax}e^{ibx} \qquad \text{and} \qquad e^{(a-ib)x}=e^{ax}e^{-ibx} .
$$

The blend is then

$$
y=e^{ax}\left(c_1e^{ibx}+c_2e^{-ibx}\right) .
$$

Complex exponentials are awkward in a real problem, so they are converted. The two identities

$$
e^{ibx}=\cos bx+i\sin bx \qquad \text{and} \qquad e^{-ibx}=\cos bx-i\sin bx
$$

turn the bracket into

$$
\left(c_1+c_2\right)\cos bx+i\left(c_1-c_2\right)\sin bx .
$$

Renaming the two combinations of constants as fresh constants $A$ and $B$ gives

$$
y=e^{ax}\left(A\cos bx+B\sin bx\right) .
$$

The renaming is legitimate because $c_1$ and $c_2$ were arbitrary to begin with, so the two combinations $c_1+c_2$ and $i\left(c_1-c_2\right)$ are equally arbitrary.

A concrete instance is

$$
\frac{d^{2}y}{dx^{2}}+y=0 ,
$$

whose auxiliary equation is

$$
m^{2}+1=0 ,
$$

with roots $m=i$ and $m=-i$. Here the real part $a$ is zero and the imaginary part $b$ is one, so the general solution is

$$
y=A\cos x+B\sin x .
$$

This equation describes simple harmonic motion, and the answer says exactly that: every motion of this kind is a combination of a cosine wave and a sine wave of the same frequency.

A second instance is

$$
\frac{d^{2}y}{dx^{2}}-4\frac{dy}{dx}+13y=0 ,
$$

whose auxiliary equation is

$$
m^{2}-4m+13=0 .
$$

The quadratic formula gives

$$
m=\frac{4\pm\sqrt{16-52}}{2}=\frac{4\pm\sqrt{-36}}{2}=\frac{4\pm 6i}{2}=2\pm 3i .
$$

The real part is two and the imaginary part is three, so

$$
y=e^{2x}\left(A\cos 3x+B\sin 3x\right) .
$$

### 3.6 Third and higher order

For order three the auxiliary equation is a cubic, and it is solved by finding one root by inspection and then dividing out the corresponding factor. For order four or more the same idea is repeated until only quadratics remain.

The operating rules for roots are uniform. A real root $m$ contributes $e^{mx}$. A real root repeated $k$ times contributes $e^{mx}$, $xe^{mx}$, up to $x^{k-1}e^{mx}$. A conjugate pair $a\pm ib$ each repeated $k$ times contributes $e^{ax}\cos bx$, $xe^{ax}\cos bx$, up to $x^{k-1}e^{ax}\cos bx$, together with the matching sine terms. The total count of arbitrary constants always equals the degree of the auxiliary equation.

A fourth-order instance is

$$
\frac{d^{4}y}{dx^{4}}+8\frac{d^{2}y}{dx^{2}}+16y=0 .
$$

Its auxiliary equation is

$$
m^{4}+8m^{2}+16=0 ,
$$

which is a quadratic in $m^{2}$ and factorises as

$$
\left(m^{2}+4\right)^{2}=0 .
$$

The roots are $2i$ and $-2i$, each repeated twice. The conjugate pair with $a=0$ and $b=2$ gives a cosine and a sine of $2x$, and the repetition adds factors of $x$, so

$$
y=\left(c_1+c_2x\right)\cos 2x+\left(c_3+c_4x\right)\sin 2x .
$$

Four constants appear, as the order four requires.

### 3.7 Checking an answer properly

The check is always the same: differentiate the claimed solution the required number of times, substitute every piece into the left-hand side, and simplify. If the result is zero for all values of the input, the answer is correct.

For a claimed general solution the check can be done one basic solution at a time, because superposition guarantees that if both basic solutions pass, every blend passes. That is faster than substituting the whole blend, and it isolates mistakes.

A second, cheaper check uses the coefficients. For the equation with coefficients $1$, $-5$ and $6$ the sum of the roots must be $5$ and their product must be $6$, since the auxiliary equation is $m^{2}-5m+6=0$. Getting roots $2$ and $3$ satisfies both conditions. In general, for $a_0m^{2}+a_1m+a_2=0$ the sum of the roots is $-\frac{a_1}{a_0}$ and the product is $\frac{a_2}{a_0}$, and those two facts catch most arithmetic slips immediately.

## 4. Representative Worked Examples and Solutions

### 4.1 Problem: verify that an exponential solves a given equation

Show that $y=e^{3x}$ is a solution of

$$
\frac{d^{2}y}{dx^{2}}-5\frac{dy}{dx}+6y=0 .
$$

### 4.2 Solution: differentiate twice, substitute, simplify

Step 1. Compute the first derivative, using the rule that the derivative of $e^{3x}$ is three times itself.

$$
\frac{dy}{dx}=3e^{3x}
$$

Step 2. Compute the second derivative by differentiating again.

$$
\frac{d^{2}y}{dx^{2}}=9e^{3x}
$$

Step 3. Substitute the function and both derivatives into the left-hand side.

$$
9e^{3x}-5\left(3e^{3x}\right)+6e^{3x}
$$

Step 4. Collect the numerical coefficients and factor out the exponential.

$$
\left(9-15+6\right)e^{3x}=0\cdot e^{3x}=0
$$

Step 5. Conclude. The left-hand side is zero for every value of $x$, so the function is a solution on the whole real line.

### 4.3 Problem: solve a second-order equation with two different real roots

Solve

$$
\frac{d^{2}y}{dx^{2}}-5\frac{dy}{dx}+6y=0 .
$$

### 4.4 Solution: build the auxiliary equation and factorise

Step 1. Write the auxiliary equation by replacing the second derivative with $m^{2}$, the first derivative with $m$, and the function with one.

$$
m^{2}-5m+6=0
$$

Step 2. Factorise, looking for two numbers whose product is six and whose sum is five.

$$
\left(m-2\right)\left(m-3\right)=0
$$

Step 3. Read off the roots, which are two different real numbers.

$$
m_1=2 \qquad \text{and} \qquad m_2=3
$$

Step 4. Write the general solution for the case of two different real roots, with one constant for each root.

$$
y=c_1e^{2x}+c_2e^{3x}
$$

Step 5. Check by substitution. The first basic solution gives $4-10+6=0$ and the second gives $9-15+6=0$, so both pass and therefore every blend passes.

### 4.5 Problem: solve an equation with a repeated root

Solve

$$
\frac{d^{2}y}{dx^{2}}-6\frac{dy}{dx}+9y=0 .
$$

### 4.6 Solution: recognise a perfect square

Step 1. Write the auxiliary equation.

$$
m^{2}-6m+9=0
$$

Step 2. Recognise the perfect square, since nine is three squared and six is twice three.

$$
\left(m-3\right)^{2}=0
$$

Step 3. Record that the root three occurs twice, so the case is a repeated root and the second solution needs an extra factor of $x$.

Step 4. Write the general solution in the repeated-root pattern.

$$
y=\left(c_1+c_2x\right)e^{3x}
$$

Step 5. Check the second basic solution $y=xe^{3x}$. Its first derivative is $e^{3x}+3xe^{3x}$ and its second derivative is $3e^{3x}+3e^{3x}+9xe^{3x}=6e^{3x}+9xe^{3x}$. Substituting,

$$
\left(6e^{3x}+9xe^{3x}\right)-6\left(e^{3x}+3xe^{3x}\right)+9xe^{3x}=e^{3x}\left(6-6\right)+xe^{3x}\left(9-18+9\right)=0 .
$$

The check succeeds, so the general solution is correct.

### 4.7 Problem: solve an equation with complex roots

Solve

$$
\frac{d^{2}y}{dx^{2}}+9y=0 .
$$

### 4.8 Solution: a negative discriminant gives a conjugate pair

Step 1. Write the auxiliary equation.

$$
m^{2}+9=0
$$

Step 2. Solve it, noting that no real number squares to minus nine.

$$
m=\pm 3i
$$

Step 3. Identify the real part and the imaginary part. The real part is zero and the imaginary part is three.

Step 4. Write the general solution in the complex-case pattern, with no exponential factor because the real part is zero.

$$
y=A\cos 3x+B\sin 3x
$$

Step 5. Check the sine term. Its first derivative is $3\cos 3x$ and its second derivative is $-9\sin 3x$, so the combination is $-9\sin 3x+9\sin 3x=0$. The cosine term behaves in exactly the same way, so the general solution is correct.

### 4.9 Problem: solve an initial value problem

Solve

$$
\frac{d^{2}y}{dx^{2}}-3\frac{dy}{dx}+2y=0
$$

subject to $y=1$ and $\frac{dy}{dx}=0$ when $x=0$.

### 4.10 Solution: general solution first, then two equations for two constants

Step 1. Write and factorise the auxiliary equation.

$$
m^{2}-3m+2=0
$$

$$
\left(m-1\right)\left(m-2\right)=0
$$

Step 2. Record the roots one and two, which are different and real.

Step 3. Write the general solution.

$$
y=c_1e^{x}+c_2e^{2x}
$$

Step 4. Apply the value of the function at zero, where both exponentials equal one.

$$
c_1+c_2=1
$$

Step 5. Differentiate the general solution, ready for the condition on the derivative.

$$
\frac{dy}{dx}=c_1e^{x}+2c_2e^{2x}
$$

Step 6. Apply the value of the derivative at zero.

$$
c_1+2c_2=0
$$

Step 7. Subtract the first equation from the second to eliminate $c_1$.

$$
c_2=-1
$$

Step 8. Substitute back to find the other constant.

$$
c_1=2
$$

Step 9. State the particular solution.

$$
y=2e^{x}-e^{2x}
$$

Step 10. Check both conditions. At $x=0$ the value is $2-1=1$ and the derivative is $2-2=0$, as demanded, and the equation itself was built from the correct auxiliary equation, so the answer is complete.

### 4.11 Problem: solve a third-order equation

Solve

$$
\frac{d^{3}y}{dx^{3}}-6\frac{d^{2}y}{dx^{2}}+11\frac{dy}{dx}-6y=0 .
$$

### 4.12 Solution: find one root by inspection, then factor out

Step 1. Write the auxiliary equation, which is a cubic.

$$
m^{3}-6m^{2}+11m-6=0
$$

Step 2. Try small whole numbers. Substituting $m=1$ gives $1-6+11-6=0$, so one is a root.

Step 3. Divide out the factor $m-1$ to leave a quadratic.

$$
m^{3}-6m^{2}+11m-6=\left(m-1\right)\left(m^{2}-5m+6\right)
$$

Step 4. Factorise the quadratic.

$$
m^{2}-5m+6=\left(m-2\right)\left(m-3\right)
$$

Step 5. Record all three roots, which are different and real.

$$
m=1,\quad m=2,\quad m=3
$$

Step 6. Write the general solution with one constant per root.

$$
y=c_1e^{x}+c_2e^{2x}+c_3e^{3x}
$$

Step 7. Check by substitution for the root three. Its second and third derivatives are $9e^{3x}$ and $27e^{3x}$, and

$$
27-6\cdot 9+11\cdot 3-6=27-54+33-6=0 ,
$$

so the check succeeds.

### 4.13 Problem: solve a non-homogeneous equation by separating the two parts

Find the general solution of

$$
\frac{d^{2}y}{dx^{2}}-5\frac{dy}{dx}+6y=e^{x} .
$$

### 4.14 Solution: homogeneous part first, then one extra solution

Step 1. Solve the homogeneous equation, which is the same equation with zero on the right.

$$
y_h=c_1e^{2x}+c_2e^{3x}
$$

Step 2. Look for one function that reproduces $e^{x}$ on the right. Try $y=ke^{x}$ for an unknown number $k$.

Step 3. Substitute, remembering that every derivative of $ke^{x}$ is $ke^{x}$.

$$
ke^{x}-5ke^{x}+6ke^{x}=2ke^{x}
$$

Step 4. Choose $k$ so that the result equals $e^{x}$.

$$
2k=1 \qquad \text{so} \qquad k=\frac{1}{2}
$$

Step 5. Add the two parts, since the sum of a homogeneous solution and one solution of the full equation solves the full equation.

$$
y=c_1e^{2x}+c_2e^{3x}+\frac{1}{2}e^{x}
$$

Step 6. Check the extra term alone. Its derivatives are all $\frac{1}{2}e^{x}$, so the left-hand side is $\frac{1}{2}-\frac{5}{2}+3=\frac{1}{2}$ times $e^{x}$, which is $e^{x}$ as required. The two constants still number two, matching the order.

## 5. Mathematical Extensions, Limits, and Common Errors

### 5.1 The beginner misconceptions worth naming

The list below collects the mistakes that appear most often in first attempts. Each is paired with the correct idea, because naming the error is what prevents it.

**Misconception one: the answer is a number.** A differential equation is solved by a function, not by a value. Writing $y=3$ as the answer to a second-order equation is a category error, since a constant cannot carry the two arbitrary constants the order demands.

**Misconception two: one solution is the whole answer.** Finding $e^{2x}$ for the equation with roots two and three is only half the work. The general solution must contain every independent basic solution and therefore two arbitrary constants.

**Misconception three: the repeated root needs no adjustment.** When the auxiliary equation has a single repeated root, writing $y=c_1e^{mx}+c_2e^{mx}$ is worthless, because the two terms merge into one and only one arbitrary constant survives. The second solution must be $xe^{mx}$.

**Misconception four: complex roots mean complex answers.** Complex roots never require a complex-valued final answer. They signal that the real answer is built from a cosine and a sine multiplied by an exponential.

**Misconception five: the imaginary part vanishes.** For roots $2\pm 3i$ the answer uses $\cos 3x$ and $\sin 3x$, not $\cos 2x$ and $\sin 2x$. The real part becomes the exponential factor and the imaginary part becomes the frequency.

**Misconception six: signs are dropped when moving terms.** The auxiliary equation must be written with the coefficients carrying their own signs. For

$$
\frac{d^{2}y}{dx^{2}}-5\frac{dy}{dx}+6y=0
$$

the quadratic is $m^{2}-5m+6=0$ and not $m^{2}+5m+6=0$. Reversing a sign changes the roots from two and three to minus two and minus three.

**Misconception seven: superposition is assumed where it does not hold.** For a non-linear equation the blend of two solutions is not a solution. Linearity must be checked before any adding is done.

**Misconception eight: an initial value problem is finished once the constants are found.** The constants must then be substituted back and the two given conditions re-checked. That final substitution catches nearly every slip.

### 5.2 Where the method stops working

The method rests on the coefficients being constants. Introduce a single factor of the input variable and the guess $y=e^{mx}$ no longer works, because the derivatives no longer recombine into a multiple of the same exponential. The equation

$$
x\frac{d^{2}y}{dx^{2}}+\frac{dy}{dx}+xy=0
$$

is linear and homogeneous but has variable coefficients, and its solutions are not available in elementary form.

The method also says nothing about non-homogeneous equations beyond the trick shown in Section 4.13. For a general right-hand side the extra solution must be found by a separate technique, and the homogeneous solution found here becomes only one half of the answer.

Finally, the method gives all solutions of the equation but says nothing about the interval on which a solution is wanted. For constant coefficients the solutions are valid on the whole real line unless a condition restricts attention to part of it.

### 5.3 Where these ideas lead next

Three extensions grow directly out of this note. The first is the treatment of non-homogeneous equations, where the homogeneous solution is combined with one particular solution, and the coefficient-matching trick of Section 4.13 is generalised.

The second is the case of variable coefficients, where a change of the input variable sometimes converts the equation into one with constant coefficients, after which the method of this note applies unchanged.

The third is the description of oscillations. The complex case with a negative real part describes a vibration whose amplitude decays, which is why the same mathematics appears in the study of springs, circuits and sound. The real part of the root controls the decay and the imaginary part controls the pitch.

### 5.4 A short checklist for any question

1. Write the equation in the standard shape with zero on the right, and note whether it is homogeneous.
2. Confirm that the coefficients are constants, and note the order.
3. Write the auxiliary equation with the signs exactly as they appear in the differential equation.
4. Solve it exactly, keeping surds and imaginary parts rather than rounding.
5. Decide which of the three cases applies.
6. Write the general solution with the correct number of arbitrary constants.
7. If conditions are given, solve for the constants and then re-check them.
8. Substitute the answer back into the differential equation, at least for the awkward basic solution.

### 5.5 Summary of the whole note

A second-order homogeneous linear equation with constant coefficients is a recipe that combines a function, its first derivative and its second derivative, with fixed numerical dials, and demands nothing. It is called second order because the highest derivative is the second, linear because the function and its derivatives appear only to the first power and never multiplied together, homogeneous because there is no extra term on the right, and constant coefficient because the dials do not change with the input.

The operator shorthand writes the whole recipe as a bracket applied to the unknown function, and the bracket looks exactly like a quadratic in the symbol standing for differentiation.

Guessing an exponential converts the problem into that quadratic, called the auxiliary equation. Two different real roots give two distinct exponentials. One repeated root gives an exponential and the same exponential multiplied by the input variable. A conjugate complex pair gives an exponential factor times a blend of a cosine and a sine. In every case the two constants are fixed by two conditions, and in every case substituting the answer back into the equation is the check that settles the matter.
