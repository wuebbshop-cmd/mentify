## 1. Foundational Concepts, Definitions, and Axioms

### 1.1 A bucket under a dripping tap

Imagine a bucket standing under a dripping tap, and suppose you are not allowed to look inside it. A friend tells you one fact: the water level is climbing by two centimetres every minute. That sentence describes how fast the level changes, not how much water is present. It tells you a speed and leaves the amount unknown.

To recover the amount you need one extra piece of information, namely where the level stood when you started watching. If the level was four centimetres at the start, then after one minute it is six centimetres, after three minutes ten centimetres, and after ten minutes twenty-four centimetres. You built the quantity by adding the rate repeatedly to the starting value.

That little calculation is the whole shape of this topic. The sentence about the rate is called a differential equation. The starting value is called a condition. The recipe that turns the rate and the condition into a description of the level is called the solution. A rule about change, plus a starting point, produces knowledge of the quantity itself.

Now picture a second bucket, where the tap is not steady. The level rises faster when there is already more water pressing down, so the rate of rise is proportional to the amount present. If the level is $y$ centimetres and the rate is twice the current level, the rule reads

$$
\frac{dy}{dx}=2y ,
$$

where $x$ counts minutes. This is the same kind of sentence as before, except that the right-hand side mentions the unknown quantity itself. The answer is no longer a straight line but a rising curve, and we shall meet it again in Example 4.17.

Think of a third situation: a bill that grows by a fixed amount each month. The rule for the growth is easy to state; the balance at any date needs a starting balance. Every one of these stories has the same structure, and every one of them is a differential equation in disguise.

### 1.2 Naming the object: ordinary differential equations

Let $y$ stand for the unknown quantity, whether a water level, a balance, a distance or a temperature. Let $x$ stand for the variable that drives the change, usually time or a distance along a line. The letter $y$ is called the dependent variable because its value depends on $x$, and $x$ is called the independent variable because it is chosen freely.

> **Definition (Ordinary differential equation).** An ordinary differential equation is an equation that contains one or more ordinary derivatives of an unknown function of a single independent variable.

Every word in that sentence does work. Ordinary describes the kind of derivative: it is taken with respect to one variable only, and the symbol for it is a straight letter $d$ rather than a curly $\partial$. Single independent variable describes the driver: there is exactly one of them. Unknown function reminds us that the answer being sought is a function, not a number.

Here are four examples, with the meaning of each spelled out in words.

The equation

$$
\frac{dy}{dx}=5x
$$

says that the slope of the unknown curve at the point with coordinate $x$ equals five times $x$. The equation

$$
\frac{dy}{dx}+3x+5=0
$$

says that the slope equals minus three times $x$ minus five, which is again completely determined once $x$ is known. The equation

$$
\frac{d^{2}y}{dx^{2}}+8\frac{dy}{dx}+9y=0
$$

mentions the slope, the rate at which the slope changes, and the value of the function, and asserts that a particular combination of the three is zero. The equation

$$
\frac{d^{2}y}{dx^{2}}+y=\sin x
$$

compares the second derivative with the function itself, with the difference forced to follow a wave.

All four are ordinary, because only the single variable $x$ drives the change and only straight-$d$ derivatives appear. The notation will be unpacked properly in Section 1.4.

It is worth pausing on how different this is from ordinary algebra. The equation $3x^{2}-5x+2=0$ asks for a number, and you find it by isolating $x$. A differential equation asks for a whole function, and no amount of rearranging will isolate a function, because a function is not a single unknown quantity that can be moved across an equals sign. Instead you recognise the type of equation, guess the shape of the answer, and then fit whatever constants remain. That is why the subject feels different rather than merely harder.

### 1.3 When two things vary at once: partial differential equations

Sometimes the quantity you care about depends on two separate drivers. Picture a metal plate that is heated at one end. The temperature at a point depends on where the point is — its distance along the plate — and also on how long the plate has been heating. Two independent variables, one unknown quantity.

If we call the temperature $u$, the position $x$ and the time $t$, then $u$ is a function of both $x$ and $t$. We can ask how fast the temperature rises at a fixed position, written $\frac{\partial u}{\partial t}$, and we can ask how the temperature varies from point to point at a fixed instant, written $\frac{\partial u}{\partial x}$. The curly symbol $\partial$ is used precisely to signal that one variable is being varied while the other is held still.

> **Definition (Partial differential equation).** A partial differential equation is an equation involving one or more partial derivatives of an unknown function of two or more independent variables.

A typical example is

$$
\frac{\partial u}{\partial t}=3\frac{\partial^{2}u}{\partial x^{2}} ,
$$

which says that the rate at which the temperature rises at a point is three times the amount by which the temperature profile is curving at that point.

The practical difference between the two kinds of derivative is simple to state. When you differentiate with respect to $x$, you treat $y$ as an ordinary number, a constant that happens to be carried along. When you differentiate with respect to $y$, you treat $x$ as a constant. Two small computations show the rule at work.

$$
\frac{\partial}{\partial x}\left(3y^{2}x^{2}\right)=3y^{2}\cdot 2x=6xy^{2}
$$

$$
\frac{\partial}{\partial y}\left(7y\sin x\right)=7\sin x\cdot 1=7\sin x
$$

In the first line the factor $3y^{2}$ is untouched because it contains no $x$. In the second the factor $\sin x$ is untouched because it contains no $y$.

The remainder of this topic, and the whole of the early part of the subject, is concerned with the ordinary case only. Whenever a single independent variable is in play, the derivatives are ordinary, the equation is ordinary, and the machinery of integration applies directly. The partial case becomes important much later, when functions of several variables are studied in their own right.

### 1.4 Reading the notation of repeated differentiation

The symbol $\frac{d}{dx}$ is an instruction rather than a quantity. It means: differentiate whatever follows with respect to $x$. The instruction can be applied once, twice, or any number of times, and each repetition is recorded in the symbol.

Applied once to $y$, the instruction produces $\frac{dy}{dx}$, read as "dee why by dee ex". Applied to that result, it produces the second derivative

$$
\frac{d^{2}y}{dx^{2}}=\frac{d}{dx}\left(\frac{dy}{dx}\right) .
$$

The small raised $2$ on the $d$ in the numerator counts how many times the instruction has been carried out, and the small raised $2$ on the $dx$ in the denominator records the same count for the variable. Applied $n$ times, the symbol is $\frac{d^{n}y}{dx^{n}}$, and by definition

$$
\frac{d^{n}y}{dx^{n}}=\frac{d}{dx}\left(\frac{d^{n-1}y}{dx^{n-1}}\right)
$$

for every whole number $n$ greater than one. The third derivative is therefore the derivative of the second derivative, and so on indefinitely.

A shorter notation is used constantly. Instead of $\frac{dy}{dx}$ one writes $y'$, instead of $\frac{d^{2}y}{dx^{2}}$ one writes $y''$, and beyond the third dash the dashes become hard to count, so one writes $y^{(4)}$ for the fourth derivative, $y^{(5)}$ for the fifth, and $y^{(n)}$ in general. The dash and the fraction are two spellings of one object.

A concrete run of derivatives makes the ladder visible. Take the function $y=x^{4}$. Differentiating repeatedly gives

$$
y'=4x^{3}, \qquad y''=12x^{2}, \qquad y'''=24x, \qquad y^{(4)}=24, \qquad y^{(5)}=0 .
$$

Each step lowers the power of $x$ by one and multiplies by the current power, which is the ordinary power rule. After four differentiations the function has become the constant $24$, and a further differentiation gives zero.

One warning about the denominator. The expression $dx^{2}$ in $\frac{d^{2}y}{dx^{2}}$ is a bookkeeping device recording two differentiations with respect to $x$. It is not the square of a quantity called $dx$, and the whole symbol $\frac{dy}{dx}$ is a single object denoting a derivative, not a fraction made of two small numbers. Later, when we separate variables in Section 3.5, we shall appear to move $dx$ and $dy$ around. That step is legitimate, but the reason is that both sides can be integrated, not that $dx$ and $dy$ are numbers with a life of their own.

### 1.5 The order of a differential equation

> **Definition (Order).** The order of a differential equation is the order of the highest derivative that appears in it.

The order is found by looking at the equation and asking which derivative has been differentiated the most times. Nothing else about the equation matters for this count: not the powers, not the coefficients, not the right-hand side.

The equation $\frac{dy}{dx}=3x^{2}$ contains the first derivative and nothing higher, so its order is one. The equation

$$
\frac{d^{2}y}{dx^{2}}-5\frac{dy}{dx}+6y=0
$$

contains a second derivative and a first derivative, so the highest is the second and the order is two. The equation

$$
7\frac{d^{3}y}{dx^{3}}+8\frac{d^{2}y}{dx^{2}}+9\frac{dy}{dx}+8y=e^{x}
$$

contains derivatives of orders one, two and three, so its order is three.

Powers do not change the order. The equation

$$
3\frac{d^{2}y}{dx^{2}}+\left(\frac{dy}{dx}\right)^{10}+8y=0
$$

looks violent because of the tenth power, but the tenth power is applied to a first derivative, so the highest derivative is still the second and the order is two. A large exponent never raises the order; only a genuinely higher derivative does.

The order matters because of one counting rule, stated now and justified later: the general solution of an equation of order $n$ carries exactly $n$ arbitrary constants. An order-one equation needs one constant, an order-two equation needs two, and an order-three equation needs three. This is the single most useful self-check in the topic, because a claimed solution with the wrong number of constants is immediately suspect.

### 1.6 The degree of a differential equation

> **Definition (Degree).** The degree of a differential equation is the power to which the highest-order derivative is raised, after the equation has been cleared of radicals and of fractional powers in the derivatives.

The words after the comma do the real work. Before the power can be read off, the equation must be written as a polynomial in the derivatives, with no square roots, cube roots or fractional exponents attached to them. Only then is the exponent of the highest derivative the degree.

Four examples show how the reading goes.

The equation

$$
\left(\frac{d^{2}y}{dx^{2}}\right)^{5}+3\left(\frac{dy}{dx}\right)^{7}+8y=0
$$

is already free of radicals. The highest derivative is the second, and it carries the power five, so the order is two and the degree is five. The seventh power on the first derivative is irrelevant, exactly as it was for the order.

The equation

$$
7\frac{d^{3}y}{dx^{3}}+8\frac{d^{2}y}{dx^{2}}+9\frac{dy}{dx}+8y=e^{x}
$$

has the highest derivative, of order three, appearing to the first power, so the order is three and the degree is one. An equation in which every derivative appears plainly, with no exponent written, always has degree one.

The equation

$$
\left(\frac{dy}{dx}\right)^{2}+y=x
$$

has order one and degree two, because the only derivative present is raised to the power two.

Some equations have no degree at all. The equation

$$
\sin\left(\frac{d^{2}y}{dx^{2}}\right)=x
$$

has order two but cannot be rearranged so that the second derivative appears as a polynomial, because a sine of a derivative cannot be undone by algebra without introducing infinitely many branches. Similarly

$$
e^{\frac{dy}{dx}}=x
$$

has order one and no degree. When the highest derivative sits inside a transcendental function such as a sine, a cosine, an exponential or a logarithm, the degree is undefined, and the correct answer is to say so.

A gentle example of clearing shows the mechanic. Suppose the equation is

$$
\sqrt{1+\left(\frac{dy}{dx}\right)^{2}}=2x .
$$

A square root of a derivative expression is present, so the degree cannot be read yet. Squaring both sides removes it.

$$
1+\left(\frac{dy}{dx}\right)^{2}=4x^{2}
$$

Now the first derivative appears squared, and no radical remains, so the order is one and the degree is two. Had the squaring been skipped, a careless reader might have reported a fractional degree, which is not permitted.

The two labels are therefore found by separate inspections, and they answer different questions. Order asks how many differentiations are involved. Degree asks what power the most differentiated term carries once the equation has been tidied. An equation can be of order three and degree one, or of order one and degree two, and neither number predicts the other.

### 1.7 What it means to be a solution

> **Definition (Solution).** A function $y=\phi(x)$ defined on an interval is a solution of a differential equation if substituting the function and its derivatives into the equation makes the two sides agree for every $x$ in that interval.

The words for every $x$ in that interval are the important ones. A proposed function is not a solution merely because the equation happens to hold at one or two convenient values of $x$. It must hold identically, that is, as an algebraic identity after simplification.

A small check makes this concrete. Consider the equation

$$
3\frac{d^{2}y}{dx^{2}}+5\frac{dy}{dx}=10x+6
$$

and the proposed function $y=x^{2}$. Differentiating twice gives

$$
\frac{dy}{dx}=2x, \qquad \frac{d^{2}y}{dx^{2}}=2 .
$$

Substituting both into the left-hand side gives

$$
3(2)+5(2x)=6+10x ,
$$

which is exactly the right-hand side. The two sides agree for every value of $x$, so $y=x^{2}$ is a solution on the whole real line.

Now try $y=x^{2}+7$ instead. The derivatives are identical to those of $x^{2}$, because the constant $7$ differentiates to zero. The left-hand side is therefore again $6+10x$, and the equation is again satisfied. This shows that solutions are not unique: adding a constant to a solution of this particular equation produces another solution.

### 1.8 General solution and particular solution

The previous paragraph discovered something structural. Because differentiating destroys additive constants, an equation involving derivatives cannot pin down the value of a constant, and every solution brings a family of solutions with it.

> **Definition (General solution).** The general solution of an equation of order $n$ is a family of solutions containing $n$ independent arbitrary constants, from which every solution on the interval can be obtained by assigning values to those constants.

> **Definition (Particular solution).** A particular solution is a single member of that family, obtained by giving specific values to the arbitrary constants.

The simplest illustration uses the equation

$$
\frac{dy}{dx}=2 .
$$

The slope of the unknown function is constantly two, so the unknown function is a straight line of slope two. Integrating both sides with respect to $x$ gives

$$
y=\int 2\,dx=2x+c ,
$$

where $c$ is an arbitrary constant. The general solution is the whole family of parallel lines $y=2x+c$. Choosing $c=3$ gives the particular solution $y=2x+3$, the line of slope two passing through the point with coordinates zero and three.

A second illustration shows the count rising with the order. For

$$
\frac{dy}{dx}=3x^{2}
$$

integration gives

$$
y=x^{3}+c ,
$$

a family of curves differing only by a vertical shift. Choosing $c=2$ gives the particular curve $y=x^{3}+2$. For the second-order equation

$$
\frac{d^{2}y}{dx^{2}}=6
$$

two integrations are needed. The first gives $y'=6x+c_{1}$, and the second gives

$$
y=3x^{2}+c_{1}x+c_{2} ,
$$

which carries two arbitrary constants, exactly as the order predicts.

The geometric reading is worth keeping. The general solution is a family of curves, and each choice of constants selects one curve of the family. An extra condition, such as requiring the curve to pass through a stated point, is what selects the particular curve.

## 2. Theorems, Lemmas, and Analytical Properties

### 2.1 The counting rule for constants

The first result is the one everything else leans on.

> **Theorem (Constant count).** The general solution of an ordinary differential equation of order $n$ contains exactly $n$ independent arbitrary constants, provided the equation can be solved for its highest derivative and the functions involved are smooth enough.

Only three things in that statement need explanation for present purposes. Independent means no constant can be absorbed into another by renaming; the pair $c_{1}$ and $c_{2}$ in $y=c_{1}x+c_{2}$ is independent, whereas the pair $c$ and $2c$ in $y=cx+2c$ is not. Smooth enough means the integrations can actually be performed. And solved for the highest derivative means the equation can be written with the highest derivative alone on the left, which is the situation in every example of this topic.

The practical force of the theorem is twofold. It predicts how many integrations to expect, which tells you in advance how long the answer should be. And it audits the answer afterwards: an order-two equation whose solution carries one constant has lost something.

> **Corollary (Determination by conditions).** If $n$ independent conditions are imposed on a solution of an order-$n$ equation, they determine the $n$ constants and hence select one particular solution.

This corollary explains a rule of thumb about examination questions. A first-order equation is usually paired with one condition, a second-order equation with two, and the conditions are normally supplied as values of the function, or of the function and its derivative, at a single point.

### 2.2 Forming an equation is the reverse process

> **Theorem (Elimination of constants).** A family of curves that depends on $n$ arbitrary constants satisfies an ordinary differential equation of order $n$, obtained by differentiating the family $n$ times and eliminating the constants between the resulting $n+1$ equations.

The count of equations is the point that beginners miss. To eliminate one constant you need two equations, because a single equation cannot remove an unknown. To eliminate two constants you need three. In general, $n$ constants require $n+1$ equations, and after differentiating $n$ times you have exactly $n+1$ equations at your disposal: the original family and its $n$ derivatives.

The theorem is precisely the converse of the counting rule. Given a family, differentiation raises the order one step at a time until the constants have nowhere to hide. Given an equation, integration lowers the order one step at a time and introduces one constant at each step. Forming and solving are the same relation read in two directions.

### 2.3 Order is robust, degree is fragile

Two small lemmas explain an asymmetry that confuses many students.

> **Lemma (Order survives rearrangement).** Multiplying an equation by a non-zero function of $x$, adding the same expression to both sides, or clearing denominators that involve $x$ alone, never changes the order.

The reason is that none of these operations creates a new differentiation. Only differentiating both sides raises the order, and only integrating both sides lowers it.

> **Lemma (Degree depends on the form written).** The degree is read from one particular algebraic arrangement of the equation, namely the arrangement in which all derivatives appear as a polynomial. A rearrangement that requires raising both sides to a power can change the number that is read off.

The example from Section 1.6 shows this in action. Before squaring, the equation $\sqrt{1+\left(\frac{dy}{dx}\right)^{2}}=2x$ presents a square root and no sensible degree. After squaring, the same equation presents a second power and degree two. The equation did not change; only its clothing did.

The consequence for practice is clear. Always report the degree of the tidied form, and always tidy before reporting.

### 2.4 Adding solutions of a linear equation

> **Theorem (Addition of solutions).** If $y_{1}$ and $y_{2}$ both satisfy a linear homogeneous equation, meaning one in which $y$ and its derivatives appear only to the first power and are never multiplied together, then every combination $c_{1}y_{1}+c_{2}y_{2}$ also satisfies it.

The reason is that differentiation is linear: the derivative of a sum is the sum of the derivatives, and a constant factor passes through untouched. So each term of the combination behaves exactly as its ingredients did, and the total is zero plus zero.

The theorem fails badly for non-linear equations. If $y_{1}$ solves $\frac{d^{2}y}{dx^{2}}+y^{2}=0$, then doubling it does not give a solution, because the squared term quadruples while the derivative term merely doubles. Whenever a solution is squared, multiplied by another solution, or placed inside a sine or an exponential, addition of solutions stops working, and each equation must be attacked on its own terms.

For the elementary equations of this topic, which are solved by direct integration, the addition property shows up in a harmless form: the constant of integration is itself an arbitrary multiple of the constant function one, so the general solution is a particular solution plus a constant.

### 2.5 Families of curves and the geometry of solutions

A first-order equation assigns a slope to each point of the plane, because its right-hand side is a formula in $x$ and $y$. The graph of any solution must have exactly that slope wherever it passes. The general solution is therefore a one-parameter family of curves, all of them threading through the plane in a way consistent with the assigned slopes.

For the equation $\frac{dy}{dx}=2$ the assigned slope is two everywhere, and the family is the collection of parallel straight lines of slope two. For the equation $\frac{dy}{dx}=2x$ the assigned slope grows with $x$, and the family is the collection of parabolas $y=x^{2}+c$, all identical in shape and shifted vertically. For the equation connected with circles, treated in Example 4.15, the family is a collection of concentric circles.

This picture gives a cheap sanity check. Two distinct curves from the same one-parameter family should not cross, because at a crossing point they would demand two different slopes from the same formula. If a proposed family contains crossing curves, something has gone wrong.

### 2.6 Existence, in plain terms

> **Theorem (Existence and uniqueness, stated loosely).** If the right-hand side of $y'=f(x,y)$ is a well-behaved function near a starting point, then a solution passing through that point exists and is unique on some interval around the point.

Well-behaved here means continuous, together with its rate of change with respect to $y$. The theorem is quoted rather than proved, and its role in this topic is to justify the practice of hunting for one particular solution when a condition is given: under the stated hypotheses there is exactly one to find, so a solution that satisfies both the equation and the condition is the solution.

The hypotheses matter. The equation $y'=3y^{2/3}$ with the condition $y=0$ when $x=0$ has two solutions through the same point, namely the constant zero function and the function $x^{3}$, because the right-hand side fails the smoothness test at the origin. Such examples are exceptional, but they explain why textbooks state the theorem with care.

## 3. Formal Proofs, Derivations, and Methods

### 3.1 Method: reading off the order and the degree

The two labels are found in a fixed sequence, and following the sequence prevents the commonest mistakes.

1. Locate every derivative that appears in the equation and note how many times each has been differentiated.
2. The largest of those counts is the order. Report it first.
3. Clear any square root, cube root or fractional exponent that involves a derivative, by raising both sides to a suitable power or by isolating the offending term before raising.
4. After clearing, check that no derivative remains inside a sine, cosine, exponential or logarithm. If one does, the degree is undefined and that is the answer.
5. Otherwise read the exponent of the highest-order derivative; that exponent is the degree.

The sequence is short but the order of the steps is essential. Step 5 must never be performed before step 3, and step 4 must never be skipped.

### 3.2 Method: checking that a function is a solution

Verification is mechanical, which is why it is the safest source of marks in the whole topic.

1. Differentiate the proposed function as many times as the order of the equation requires.
2. Write the function and all its derivatives out clearly, so that a slip in one line does not infect the next.
3. Substitute them into the left-hand side of the equation and simplify, keeping the right-hand side in view as a target.
4. If the two sides become the same expression, the function is a solution. State the interval on which the simplification is valid.
5. If the simplification produces something that is not identically zero, the function is not a solution, and the failure is itself the answer.

The last point is worth emphasising. A question that begins "show that" wants a verification, but a question that begins "is it true that" may well have a negative answer, and a clean demonstration of failure earns the marks.

### 3.3 Method: solving by direct integration

When the equation presents the highest derivative alone on one side and a function of $x$ alone on the other, the solution is obtained by integrating the required number of times.

1. Confirm the shape: the equation reads $\frac{d^{n}y}{dx^{n}}=f(x)$ with $f$ containing no $y$.
2. Integrate both sides once with respect to $x$ and add one arbitrary constant.
3. Repeat until the $n$-th derivative has been reduced to $y$, adding one new constant at each integration.
4. Collect the result, which will be a function of $x$ together with a linear combination of the constants.
5. Count the constants and compare with the order; if the numbers disagree, an integration has been missed.
6. Impose any conditions and state the particular solution.

The reason each integration contributes exactly one constant is simple. Integrating a function produces an antiderivative, and any two antiderivatives differ by a constant. That constant cannot be recovered from the derivative, so it must be carried forward. When a later integration is performed, the earlier constant is a constant, so its integral contributes a term proportional to $x$ plus a genuinely new constant. The constants therefore accumulate and never merge.

A short proof of the count makes the last remark precise. For the equation $\frac{d^{n}y}{dx^{n}}=f(x)$ with $f$ continuous, integrating once gives

$$
\frac{d^{n-1}y}{dx^{n-1}}=\int f(x)\,dx+c_{1} .
$$

Integrating again gives a term involving a double integral, a term $c_{1}x$, and a new constant $c_{2}$. After $n$ steps the answer is a particular function of $x$ plus a polynomial of degree at most $n-1$ whose coefficients are the constants. Differentiating that polynomial $n$ times destroys it completely, which is exactly why the constants are free, and why exactly $n$ of them appear.

### 3.4 Method: solving by separation of variables

Many first-order equations are not directly integrable but can be rearranged so that all the $y$ dependence sits on one side and all the $x$ dependence on the other.

1. Rewrite the equation so that it has the shape $g(y)\frac{dy}{dx}=h(x)$.
2. Integrate both sides with respect to $x$. On the left, use the substitution rule to convert the integral into $\int g(y)\,dy$.
3. Perform both integrations and add a single constant, because only one integration in total has been carried out.
4. Solve for $y$ if the algebra allows; otherwise leave the answer in implicit form and say so.
5. Impose any condition to fix the constant.
6. Verify by differentiating the answer and recovering the original equation.

The justification of step 1 deserves a sentence, since it is where beginners are told to move $dx$ about as though it were a number. The honest argument is this. If $g(y)\frac{dy}{dx}=h(x)$ holds, then the function of $x$ on the left is the derivative with respect to $x$ of an antiderivative of $g$ composed with $y$. Two functions with the same derivative differ by a constant, so integrating both sides and equating the antiderivatives up to a constant is valid. The manipulation with $dy$ and $dx$ is a memory aid for that argument, not a proof of it.

One caution belongs here. Dividing by $g(y)$ is only legitimate where $g(y)$ is non-zero. If $g$ vanishes at some value, the constant function taking that value may be a solution that the division has thrown away, and it should be checked separately. The phenomenon is illustrated in Section 5.3.

### 3.5 Method: forming an equation by eliminating constants

1. Count the constants in the given family. Call that number $n$.
2. Differentiate the family once, twice, and so on, up to $n$ times.
3. You now hold $n+1$ equations linking $x$, $y$, the derivatives and the constants.
4. Solve the simplest of them for one constant and substitute into the others, or form a combination of the equations in which the constants cancel.
5. Repeat until no constant remains, and tidy the result into a standard form.
6. Check that the order of the resulting equation equals $n$.

The check in step 6 is the audit that makes the method reliable. A family with two constants must produce a second-order equation; a second-order equation produced from a one-constant family means an error has crept in.

## 4. Representative Worked Examples and Solutions

### 4.1 Problem: find the order and degree of three equations

Find the order and the degree of each of the following.

$$
\text{(a)}\quad \left(\frac{d^{2}y}{dx^{2}}\right)^{5}+3\left(\frac{dy}{dx}\right)^{7}+8y=0
$$

$$
\text{(b)}\quad \left(\frac{dy}{dx}\right)^{2}+y=x
$$

$$
\text{(c)}\quad \sin\left(\frac{d^{2}y}{dx^{2}}\right)=x
$$

### 4.2 Solution: inspect, clear if necessary, then read the exponent

Step 1. For equation (a), list the derivatives present. They are the first derivative and the second derivative, so the highest is the second and the order is two.

Step 2. For equation (a), check that no radical or fractional power touches a derivative. None does, so the degree can be read directly from the highest derivative. The second derivative carries the power five, so the degree is five.

Step 3. For equation (b), the only derivative present is the first, so the order is one. It carries the power two, and no radical is present, so the degree is two.

Step 4. For equation (c), the highest derivative is the second, so the order is two. The second derivative sits inside a sine, and no algebraic rearrangement can turn a sine into a polynomial in its argument, so no degree exists.

Step 5. Report the three answers. Equation (a) is of order two and degree five. Equation (b) is of order one and degree two. Equation (c) is of order two and has no degree.

Step 6. Check the reasoning against the definitions. In (a) and (b) the degree was read from a polynomial arrangement, as the definition demands. In (c) the arrangement is not polynomial, which is precisely the situation in which the degree is said not to exist.

### 4.3 Problem: show that a given function is a solution

Show that $y=x^{2}$ is a solution of

$$
3\frac{d^{2}y}{dx^{2}}+5\frac{dy}{dx}=10x+6 ,
$$

and state whether $y=x^{2}+4$ is also a solution.

### 4.4 Solution: differentiate, substitute, compare

Step 1. Differentiate the proposed function once.

$$
\frac{dy}{dx}=2x
$$

Step 2. Differentiate again, which is the highest derivative the equation needs.

$$
\frac{d^{2}y}{dx^{2}}=2
$$

Step 3. Substitute the three quantities into the left-hand side.

$$
3(2)+5(2x)
$$

Step 4. Simplify.

$$
6+10x
$$

Step 5. Compare with the right-hand side. The right-hand side is $10x+6$, which is the same expression with the terms written in the other order, so the two sides agree for every $x$ and the function is a solution.

Step 6. Test the second function. Its derivatives are again $2x$ and $2$, because the added constant $4$ differentiates to zero, so the left-hand side is again $6+10x$ and the equation is again satisfied.

Step 7. Interpret. Both functions are solutions, which shows that a first-order-like dependence on $x$ alone leaves an additive constant free. The equation is of order two, so its general solution will eventually carry two constants, and further solutions can be built by adding terms.

### 4.5 Problem: solve a directly integrable equation

Find the general solution of

$$
\frac{dy}{dx}=2x^{2}+3x+5 .
$$

### 4.6 Solution: integrate once and add one constant

Step 1. Note the order. Only the first derivative appears, so the order is one and the answer must carry exactly one arbitrary constant.

Step 2. Integrate both sides with respect to $x$.

$$
y=\int\left(2x^{2}+3x+5\right)dx
$$

Step 3. Integrate term by term, using the power rule on each term.

$$
y=\frac{2x^{3}}{3}+\frac{3x^{2}}{2}+5x+c
$$

Step 4. Verify by differentiating. The derivative of the right-hand side is $2x^{2}+3x+5$, because the constant differentiates to zero, and this matches the original equation.

Step 5. State the answer and count the constants. The general solution is

$$
y=\frac{2x^{3}}{3}+\frac{3x^{2}}{2}+5x+c ,
$$

one arbitrary constant for an equation of order one, as required.

### 4.7 Problem: solve a second-order equation with two conditions

Solve

$$
\frac{d^{2}y}{dx^{2}}=6
$$

subject to $y(0)=1$ and $y'(0)=2$.

### 4.8 Solution: integrate twice, then impose both conditions

Step 1. Note the order. The second derivative is the highest present, so the order is two and two constants are expected.

Step 2. Integrate once.

$$
\frac{dy}{dx}=6x+c_{1}
$$

Step 3. Integrate again.

$$
y=3x^{2}+c_{1}x+c_{2}
$$

Step 4. Impose the condition on the derivative at $x=0$. Substituting $x=0$ into the expression for $y'$ gives $c_{1}$, so $c_{1}=2$.

Step 5. Impose the condition on the function at $x=0$. Substituting $x=0$ into the expression for $y$ gives $c_{2}$, so $c_{2}=1$.

Step 6. Write the particular solution.

$$
y=3x^{2}+2x+1
$$

Step 7. Verify. Differentiating once gives $y'=6x+2$, so $y'(0)=2$. Differentiating again gives $y''=6$, which is the equation. Evaluating at zero gives $y(0)=1$. All three requirements hold, so the solution is correct.

### 4.9 Problem: distinguish the general solution from a particular one

For the equation

$$
\frac{dy}{dx}=2 ,
$$

write down the general solution, describe its geometry, and give one particular solution.

### 4.10 Solution: integrate, then choose a value for the constant

Step 1. Note the order. The equation is of order one, so the general solution carries one constant.

Step 2. Integrate both sides with respect to $x$.

$$
y=2x+c
$$

Step 3. Describe the family. For each value of $c$ the graph is a straight line of slope two, so the family consists of all parallel lines of slope two, shifted vertically from one another.

Step 4. Choose a value. Taking $c=3$ gives the member

$$
y=2x+3 ,
$$

which passes through the point with coordinates $x=0$ and $y=3$. This is a particular solution.

Step 5. Verify. The derivative of $2x+3$ is $2$, matching the equation, and the value at $x=0$ is $3$, matching the choice of constant.

### 4.11 Problem: form a differential equation from a one-constant family

Find the differential equation whose general solution is

$$
y=3x^{2}+5x+c .
$$

### 4.12 Solution: differentiate until the constant disappears

Step 1. Count the constants. Only $c$ is arbitrary, so the equation will be of order one.

Step 2. Differentiate once.

$$
\frac{dy}{dx}=6x+5
$$

Step 3. Observe that $c$ has already vanished. The constant disappeared on the first differentiation because it was added to the function, so no elimination step is needed.

Step 4. State the equation.

$$
\frac{dy}{dx}=6x+5
$$

Step 5. Check the order. The equation is of order one, matching the single arbitrary constant, so the count agrees.

Step 6. Check the direction. Integrating $6x+5$ gives $3x^{2}+5x+c$, which recovers the family, so the equation and the family are consistent with each other.

### 4.13 Problem: form an equation from a two-constant family

Find the differential equation whose general solution is

$$
y=A\cos 8x+B\sin 8x .
$$

### 4.14 Solution: differentiate twice and eliminate both constants

Step 1. Count the constants. There are two, namely $A$ and $B$, so the equation will be of order two and three equations will be needed to eliminate them.

Step 2. Differentiate once, using the chain rule on each term.

$$
\frac{dy}{dx}=-8A\sin 8x+8B\cos 8x
$$

Step 3. Differentiate again.

$$
\frac{d^{2}y}{dx^{2}}=-64A\cos 8x-64B\sin 8x
$$

Step 4. Factor the second derivative, noticing that the bracket is exactly the original function.

$$
\frac{d^{2}y}{dx^{2}}=-64\left(A\cos 8x+B\sin 8x\right)
$$

Step 5. Replace the bracket by $y$.

$$
\frac{d^{2}y}{dx^{2}}=-64y
$$

Step 6. Tidy into standard form.

$$
\frac{d^{2}y}{dx^{2}}+64y=0
$$

Step 7. Check the order and verify. The equation is of order two, matching the two constants, and substituting the family back gives $-64y+64y=0$, so the equation is satisfied by every member of the family.

### 4.15 Problem: solve a separable equation describing a family of circles

Find the family of curves satisfying

$$
\frac{dy}{dx}=-\frac{x}{y},
$$

and find the particular curve that passes through the point whose coordinates are $x=1$ and $y=2$.

### 4.16 Solution: separate, integrate, then impose the point

Step 1. Separate the variables by multiplying both sides by $y$.

$$
y\frac{dy}{dx}=-x
$$

Step 2. Integrate both sides with respect to $x$, converting the left side into an integral with respect to $y$.

$$
\int y\,dy=-\int x\,dx
$$

Step 3. Perform the integrations, adding one constant.

$$
\frac{y^{2}}{2}=-\frac{x^{2}}{2}+c
$$

Step 4. Multiply by two and rearrange.

$$
x^{2}+y^{2}=2c
$$

Step 5. Rename the constant. Writing $A$ for the positive quantity $2c$, the family is the collection of circles

$$
x^{2}+y^{2}=A
$$

centred at the origin, one for each positive value of $A$.

Step 6. Impose the condition. At the point with $x=1$ and $y=2$ we need $1+4=A$, so $A=5$.

Step 7. State the particular solution.

$$
x^{2}+y^{2}=5
$$

Step 8. Verify. Differentiating $x^{2}+y^{2}=5$ implicitly gives $2x+2y\frac{dy}{dx}=0$, hence $\frac{dy}{dx}=-\frac{x}{y}$, and the point with coordinates one and two satisfies $1+4=5$. Both requirements hold.

### 4.17 Problem: solve a separable equation with an initial condition

Solve

$$
\frac{dy}{dx}=2xy
$$

subject to $y=3$ when $x=0$.

### 4.18 Solution: separate, integrate, exponentiate, then fix the constant

Step 1. Divide both sides by $y$, which is legitimate on any interval where $y$ is not zero.

$$
\frac{1}{y}\frac{dy}{dx}=2x
$$

Step 2. Integrate both sides with respect to $x$.

$$
\int\frac{1}{y}\,dy=\int 2x\,dx
$$

Step 3. Perform the integrations, adding one constant.

$$
\ln|y|=x^{2}+c
$$

Step 4. Exponentiate both sides and write the constant in a more convenient form.

$$
|y|=e^{c}e^{x^{2}}
$$

Step 5. Remove the absolute value by allowing the multiplier to carry the sign, writing $K$ for a constant that may be positive or negative.

$$
y=Ke^{x^{2}}
$$

Step 6. Impose the condition. At $x=0$ the exponential equals one, so $3=K$.

Step 7. State the particular solution.

$$
y=3e^{x^{2}}
$$

Step 8. Verify. Differentiating gives $y'=6xe^{x^{2}}$, while $2xy=2x\cdot 3e^{x^{2}}=6xe^{x^{2}}$, so the two sides agree. At $x=0$ the value is three, as required.

## 5. Mathematical Extensions, Limits, and Common Errors

### 5.1 What the labels do and do not promise

Order, degree and the ordinary or partial distinction are labels that tell you which method to attempt. They do not promise that the answer will be expressible in familiar functions. The equation

$$
\frac{dy}{dx}=e^{-x^{2}}
$$

is first order, first degree, ordinary and linear, and perfectly well posed, yet its solution cannot be written in terms of powers, exponentials, sines, cosines and logarithms. The solution exists, and it is a genuine function, but the best description of it is an integral.

This is not a failure of the theory. It is a fact about integration, and recognising it early saves a great deal of pointless effort. The label routes you to the correct method; the attempt tells you whether a tidy answer is available.

Degree is the weakest of the three labels. It carries almost no structural information, it depends on how the equation happens to be written, and it does not exist at all for equations in which a derivative sits inside a transcendental function. Order and linearity are the labels that matter, because order fixes the number of constants and linearity makes the addition of solutions legitimate.

### 5.2 Beginner misconceptions to unlearn

- **Order is not the number of terms.** An equation with four terms can be of order one, and an equation with two terms can be of order three. Count differentiations, not terms.
- **A large power does not raise the order.** The power belongs to the degree. A tenth power on a first derivative leaves the order at one.
- **Degree is not read before radicals are cleared.** A square root around a derivative hides a genuine power, and the reported degree is wrong unless the equation has been tidied first.
- **Degree does not always exist.** If a derivative appears inside a sine, a cosine, an exponential or a logarithm, say that the degree is undefined rather than inventing a number.
- **The constant of integration is not optional.** Losing it turns a general solution into a particular one and destroys the family.
- **The number of constants must equal the order.** An order-two equation solved with one constant is incomplete, however neat the answer looks.
- **A solution is not a number.** The answer to a differential equation is a function or a relation between the variables, never a single value of $x$.
- **A general solution is not a single curve.** It is a whole family, and a particular solution is one member of it.
- **Superposition needs linearity.** Adding two solutions of a non-linear equation does not produce a solution, and assuming otherwise invalidates the whole argument.
- **The minus sign in the integral of the sine matters.** The integral of $\sin x$ is minus $\cos x$, and dropping that sign spoils an otherwise perfect answer.
- **Dividing by $y$ can lose a solution.** The constant function zero solves $\frac{dy}{dx}=2xy$, but the division by $y$ in the solution process removes it from view, so it must be restored by inspection.
- **Verification is not optional decoration.** Substituting the answer back is the only reliable check, and it catches sign errors, missing constants and mis-integrated terms immediately.

### 5.3 Where the counting rule needs care

The rule that an order-$n$ equation carries $n$ arbitrary constants is reliable for the equations of this topic, but it has three honest exceptions worth knowing.

The first is the singular solution. The equation

$$
\left(\frac{dy}{dx}\right)^{2}=4y
$$

has the one-parameter family $y=(x+c)^{2}$ as its general solution, because differentiating gives $\frac{dy}{dx}=2(x+c)$ and squaring gives four times the function. Yet the constant function $y=0$ also satisfies the equation, since both sides vanish. No value of $c$ makes $(x+c)^{2}$ identically zero, so this solution lies outside the family. Such a solution is called singular.

The second is the loss caused by division. In Example 4.17 the division by $y$ assumed $y$ was non-zero. The function $y=0$ solves the original equation, and it reappears in the answer only if the multiplier $K$ is allowed to be zero. Allowing $K$ to be zero is a legitimate way to recover it.

The third is the failure of existence. An equation can have solutions locally yet none on a longer interval, typically because a coefficient in the equation vanishes somewhere and the solution runs into that point. The solution formulas of this topic are local descriptions, and intervals of validity should be stated when a division has been performed.

### 5.4 The checks that should always be performed

Four checks catch almost every error in this material.

The first is a differentiation check: differentiate the claimed solution and see whether the original equation returns. This is direct and decisive.

The second is a constant count: compare the number of arbitrary constants in the answer with the order of the equation. If the numbers differ, work has been lost.

The third is a condition check: substitute the stated conditions into the final answer and confirm they hold. A condition that fails means either the constant was solved for incorrectly or the algebra afterwards was spoiled.

The fourth is a units-and-shape check: ask whether the answer makes qualitative sense. A slope of two should produce straight lines, not curves. A rate proportional to the amount present should produce growth that accelerates, not growth at a constant rate. When the shape of the answer contradicts the story, the algebra deserves a second look.

### 5.5 The whole topic in one paragraph

A differential equation is a sentence about how fast something changes, and its solution is a description of the thing itself. If only one variable drives the change the equation is ordinary; if several do, it is partial, and this topic stays with the ordinary case. The notation $\frac{dy}{dx}$, $\frac{d^{2}y}{dx^{2}}$ and in general $\frac{d^{n}y}{dx^{n}}$ records how many times the instruction to differentiate has been carried out. The highest such count is the order, and it fixes the number of arbitrary constants in the general solution. The power carried by that highest derivative, once radicals have been cleared and provided the derivative is not trapped inside a transcendental function, is the degree. A function is a solution when substitution turns the equation into an identity, the general solution is the whole family with its full complement of constants, and a particular solution is one member of the family selected by giving the constants specific values. Forming an equation from a family is the same counting argument run backwards: differentiate as many times as there are constants and eliminate them. Solving, for the elementary cases, is integration — performed directly when the right-hand side depends on $x$ alone, and performed after separating the variables when the two sides can be disentangled — and the answer is always checked by differentiating it back into the equation it came from.
