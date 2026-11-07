## 1. Foundational Concepts, Definitions, and Axioms

Imagine a delivery van travelling along a straight road, and imagine that a dispatcher wants to know where the van will be in one minute. Knowing only where the van is now is not enough: a parked van and a van at speed could be in the same place at this instant and in very different places a minute later. Two numbers are needed, the position and the speed, and once those two numbers are known the future is determined by the rule that says how speed changes.

Think of the same idea with three numbers. Picture a small drone hovering in a room; to predict its path one needs its position in three directions and its velocity in those three directions. Again the description of the present moment needs several numbers, and the rule that governs the future is stated in terms of all of them at once.

A differential equation of order four is like that drone. It talks about one quantity, but the quantity comes with three companions, namely the three derivatives that describe how it is changing. The companions are not extra unknowns; they are determined by the main quantity. The trick in this topic is to give each companion its own name, so that the single complicated statement becomes four simple statements, each about one rate of change. That is what reduction means: one heavy instruction becomes a short list of light instructions.

### 1.1 The letters used, and what each one means

Before any formulas, here is a plain description of every symbol that appears in this topic.

The letter $t$ stands for the independent variable, and in almost every application it means time. The letter $y$ stands for the unknown function, the quantity whose behaviour we want to describe. The dash written after $y$ means differentiation with respect to $t$: the symbol $y'$ is the first derivative, the rate at which $y$ changes; the symbol $y''$ is the second derivative, the rate at which $y'$ changes; and $y'''$ and $y^{(4)}$ continue the pattern. A number written in brackets after $y$, as in $y^{(4)}$, is a count of differentiations and not an exponent.

The small letters $x_{1}, x_{2}, x_{3}$ are names we invent for the quantity and its derivatives. The letter $A$ stands for a rectangular array of numbers, called a matrix, and the letter $X$ stands for a list of unknown functions written as a column. The letter $m$ stands for an eigenvalue, which is a number attached to a matrix, and the letter $v$ stands for an eigenvector, which is a list of numbers attached to that eigenvalue. The letters $c_{1}, c_{2}, c_{3}$ stand for arbitrary constants, the numbers that are fixed only when extra information is supplied.

### 1.2 One equation with a hidden list

Consider the small equation

$$
y''=5y'-6y .
$$

Read it in words: the rate at which the slope changes equals five times the slope minus six times the height. It is a single statement, but it mentions three related quantities, namely $y$, $y'$ and $y''$. The reduction gives the second and third of these their own names.

> **Definition (State variables).** For the equation above, put $x_{1}=y$ and $x_{2}=y'$. The two new letters are called state variables, because together they describe the present state of the quantity completely.

Now differentiate the two definitions. Differentiating $x_{1}=y$ gives $x_{1}'=y'$, and $y'$ is exactly $x_{2}$, so $x_{1}'=x_{2}$. Differentiating $x_{2}=y'$ gives $x_{2}'=y''$, and the original equation says that $y''$ equals $5y'-6y$, which in the new letters is $5x_{2}-6x_{1}$. So the second statement is $x_{2}'=5x_{2}-6x_{1}$.

The single equation has become two statements,

$$
x_{1}'=x_{2}, \qquad x_{2}'=-6x_{1}+5x_{2},
$$

and each of them mentions only first derivatives. That is the whole reduction. Nothing was assumed and nothing was lost: the two new statements say exactly what the old one said, just spread over two lines.

The same device works at any order. For an equation of order four we introduce four names, one for the quantity and one for each of its first three derivatives, and the result is four statements about first derivatives.

> **Definition (First-order system).** A first-order system is a collection of equations in which every unknown appears differentiated exactly once. The number of equations equals the number of unknowns, and the number of unknowns equals the order of the equation from which the system came.

### 1.3 Writing the list as a box of numbers

The second step is bookkeeping. A system such as the one above is built from additions and multiplications by fixed numbers, so the numbers can be collected into a rectangular array.

> **Definition (Matrix form).** The system $x_{1}'=x_{2}$ and $x_{2}'=-6x_{1}+5x_{2}$ is written as $X'=AX$, where $X$ is the column of unknowns, $X'$ is the column of their derivatives, and $A$ is the array of coefficients,

$$
A=\begin{pmatrix} 0 & 1 \\ -6 & 5 \end{pmatrix} .
$$

Read the array by rows. Its first row is $0$ and $1$, and it reproduces the first statement: zero times $x_{1}$ plus one times $x_{2}$ is $x_{2}$, which is $x_{1}'$. Its second row is $-6$ and $5$, and it reproduces the second statement: minus six times $x_{1}$ plus five times $x_{2}$ is $x_{2}'$. A zero appears in the first row because $x_{1}$ does not appear on the right-hand side of the first statement, and a zero is written rather than left as a blank so that every row has the same length.

The order of the entries must be consistent everywhere. If the unknowns are listed as $x_{1}$ then $x_{2}$, then every row of $A$ must give the coefficient of $x_{1}$ first and the coefficient of $x_{2}$ second. Getting this order wrong is the most frequent mistake in the topic, and it is invisible unless the matrix is multiplied back out and compared with the original statements.

When the equation has a term that does not involve the unknown at all, such as a known function of $t$, that term is collected into a second column called the forcing vector, and the system is written $X'=AX+B$. Such a system is called non-homogeneous, while a system with no extra term is called homogeneous.

> **Definition (Companion matrix).** The matrix that comes from a single equation of order $n$ always has the same shape: ones just above the diagonal, zeros elsewhere in the first rows, and the coefficients of the equation, with signs changed, in the last row. A matrix of this shape is called a companion matrix.

### 1.4 Eigenvalues in words

The next idea is the one that makes the whole method work, and it is best met first in plain language.

> **Definition (Eigenvalue and eigenvector).** Let $A$ be a matrix and let $v$ be a list of numbers written as a column. If multiplying $A$ by $v$ gives exactly the same column as multiplying $v$ by a single number $m$, that is if
>
> $$
> Av=mv ,
> $$
>
> then $m$ is called an eigenvalue of $A$ and $v$ is called an eigenvector belonging to $m$.

In words: most directions are turned when a matrix acts on them, but a few special directions are only stretched or squashed. An eigenvector points along one of those special directions, and the eigenvalue reports how much stretching happened. An eigenvalue of $3$ stretches the special direction threefold; an eigenvalue of $1$ leaves it alone; an eigenvalue of $0$ crushes it to nothing; an eigenvalue of $-1$ flips it backwards without changing its length.

The word eigenvector always refers to a direction, so any non-zero multiple of an eigenvector is again an eigenvector for the same eigenvalue. If the column with entries $1$ and $2$ is an eigenvector, then the column with entries $3$ and $6$ and the column with entries $-5$ and $-10$ are also eigenvectors, and all three describe the same direction.

> **Definition (Characteristic equation).** To find the eigenvalues of $A$ one solves the equation $\det\left(A-mI\right)=0$, in which $I$ is the identity matrix, the matrix with ones down the diagonal and zeros elsewhere. This equation is called the characteristic equation of $A$, and its solutions are exactly the eigenvalues.

### 1.5 Why eigenvalues solve the system

Here is the payoff, stated without proof for the moment. Suppose $m$ is an eigenvalue of $A$ and $v$ is a matching eigenvector. Then the list of functions obtained by multiplying $v$ by the growing factor $e^{mt}$ solves the system, where $e$ is the fixed number approximately equal to $2.718$ and $e^{mt}$ is the exponential function.

The reason is short. Differentiating $ve^{mt}$ with respect to $t$ multiplies it by $m$, and multiplying it by $A$ also multiplies it by $m$, because $Av=mv$. The two operations give the same answer, which is exactly what the system demands. For a matrix of order two with two different eigenvalues this gives two independent solutions, and the general solution is their sum with two constants attached.

> **Definition (General solution).** The general solution of a system is an expression containing as many arbitrary constants as there are equations, from which every solution can be obtained by choosing the constants.

The count of constants is the simplest possible check. A system of two equations must produce two constants; a system of three equations must produce three. An answer with too few constants is always wrong, even if part of it is right.

### 1.6 The three cases, named

The eigenvalues of a real matrix fall into three kinds, and each kind needs its own small adjustment.

> **Definition (Distinct real eigenvalues).** The eigenvalues are different real numbers. Each contributes one exponential solution, and the work is finished.

> **Definition (Repeated real eigenvalue).** The same real number appears twice as a solution of the characteristic equation. Sometimes two independent eigenvectors are available for it, and then the answer is still a plain sum of exponentials. Sometimes only one direction is available, and then a second solution containing the factor $t$ is required.

> **Definition (Complex conjugate eigenvalues).** The eigenvalues are complex numbers of the form a real part plus or minus a multiple of the imaginary unit $i$. A real system cannot end with complex answers, so the complex solutions are converted into real ones containing cosine and sine.

### 1.7 The vocabulary collected

The words used in this topic are few, and each has a one-line meaning. A system is the list of first-order statements. The matrix form packs that list into one array equation. The characteristic equation is the polynomial whose roots are the eigenvalues. An eigenvector is a direction that the matrix does not turn. A fundamental set is a group of solutions that are genuinely different from one another. The Wronskian is a single determinant that tests whether solutions are genuinely different. The complementary function is the general solution of the homogeneous system, and the particular integral is one solution of the non-homogeneous system. With these seven phrases the entire topic can be read.

## 2. Theorems, Lemmas, and Analytical Properties

### 2.1 The reduction works in both directions

> **Theorem (Reduction).** Let $y$ be a function of $t$ and let $x_{1}=y$, $x_{2}=y'$, and so on up to $x_{n}=y^{(n-1)}$. Then $y$ solves an equation of order $n$ if and only if the column of the $x$ letters solves the corresponding first-order system.

The force of the word if and only if is that the two problems have exactly the same solutions. Reducing an equation therefore cannot change the answer; it only changes the language in which the answer is written. The first entry of the solution column is the original unknown function, and the other entries are its derivatives.

### 2.2 The companion matrix remembers the equation

> **Theorem (Companion spectrum).** For a linear equation with constant coefficients, the eigenvalues of the companion matrix are exactly the roots of the auxiliary equation of the equation.

This is a strong statement. In the older method one writes down the auxiliary equation by inspection and solves it. In the matrix method one writes down a matrix, forms a determinant, and solves the resulting polynomial. The theorem says that these two polynomials have the same roots, so the matrix method cannot disagree with the older method. The matrix route is longer, but it also delivers the eigenvectors, and those are what the answer needs.

> **Lemma (Two free checks).** For a matrix of order two, the sum of the eigenvalues equals the sum of the two diagonal entries, and the product of the eigenvalues equals the determinant. For a companion matrix, the coefficient of the second highest power is minus the sum of the diagonal entries.

These two checks cost a few seconds and catch most arithmetic slips. If the eigenvalues of a matrix are claimed to be $2$ and $3$, then the diagonal entries must add to $5$ and the determinant must be $6$.

### 2.3 Different eigenvalues give the easy answer

> **Theorem (Distinct eigenvalues).** If a matrix of order $n$ has $n$ eigenvalues that are all different, and if $v_{1},\dots,v_{n}$ are matching eigenvectors, then the general solution of the system is a sum of terms, each term being a constant times an eigenvector times the matching exponential.

> **Lemma (Distinct eigenvalues give independent eigenvectors).** Eigenvectors belonging to different eigenvalues can never be multiples of one another.

The lemma explains why the distinct case needs no extra work. The solutions are automatically independent, so the general solution is simply the sum with one constant per solution.

### 2.4 The doubled eigenvalue

> **Theorem (Repeated eigenvalue with two directions).** If a repeated eigenvalue comes with two independent eigenvectors, the general solution is a sum of two exponential terms with that same eigenvalue, one for each eigenvector.

> **Theorem (Repeated eigenvalue with one direction).** If a repeated eigenvalue comes with only one independent eigenvector, a second solution is needed in the form of the eigenvector multiplied by $t$ and by the exponential, plus an extra constant column multiplied by the exponential alone. The extra column is found by solving one further linear system.

The extra column is called a generalised eigenvector. It is not an eigenvector, because the matrix does turn it, but it is exactly the amount of turning needed to produce the missing solution.

### 2.5 Complex eigenvalues give waves

> **Theorem (Complex pair).** If a real matrix has eigenvalues $a+bi$ and $a-bi$ with $b$ not zero, then the two real solutions are built from the real part and the imaginary part of a single complex solution, and they contain cosine and sine multiplied by the exponential with growth rate $a$.

The real part $a$ controls whether the solution grows, decays, or stays at constant size, and the imaginary part $b$ controls how fast the solution oscillates. A pair of pure imaginary eigenvalues, where $a$ is zero, gives a solution that circulates forever without growing or shrinking.

### 2.6 Systems with a forcing term

> **Theorem (Complementary plus particular).** If one solution of a non-homogeneous system is known, then adding to it the general solution of the homogeneous system gives the general solution of the non-homogeneous system.

> **Theorem (Trial solutions).** If the forcing term is a constant column times an exponential $e^{kt}$, one tries a particular solution of the same shape. The trial works unless $k$ happens to be an eigenvalue, in which case the trial must be multiplied by $t$.

The exception is the same resonance that appears in the scalar theory: a forcing term that matches a natural mode of the system cannot be matched by a solution of the same shape, because the matrix cannot be inverted at that value.

### 2.7 The trace and determinant identities

> **Lemma (Trace and determinant).** The trace of a matrix is the sum of its diagonal entries, and it equals the sum of the eigenvalues counted with multiplicity. The determinant equals the product of the eigenvalues counted with multiplicity.

This lemma is the standard way to detect a wrong eigenvalue before any further work is done. It also explains the form of the characteristic equation in the repeated case: a double eigenvalue $2$ forces a trace of $4$ and a determinant of $4$.

## 3. Formal Proofs, Derivations, and Methods

### 3.1 Why naming the derivatives works

Let $y$ solve an equation of order two, written as $y''=F\left(t,y,y'\right)$ where $F$ is some rule combining its three inputs. Put $x_{1}=y$ and $x_{2}=y'$.

Differentiating the first definition gives $x_{1}'=y'$, and $y'$ is the second name, so $x_{1}'=x_{2}$. Differentiating the second definition gives $x_{2}'=y''$, and the equation says that $y''$ is $F\left(t,y,y'\right)$, so $x_{2}'=F\left(t,x_{1},x_{2}\right)$. Both statements are first order, and together they say exactly what the original equation said.

For the reverse direction, suppose a column of two functions solves the pair. Take its first entry and call it $y$. Then the first statement says $x_{1}'=x_{2}$, so the second entry is the derivative of the first. The second statement then says that the derivative of $y'$ equals $F$ evaluated at $y$ and $y'$, which is the original equation. Nothing has been added and nothing removed, so the two problems are the same problem.

### 3.2 Why an eigenvalue gives a solution

Let $m$ be an eigenvalue of $A$ with eigenvector $v$, and consider the column of functions $X=ve^{mt}$. The derivative of an exponential multiplies it by the constant in the exponent, so

$$
X'=mve^{mt} .
$$

On the other hand, the matrix acts on the column without touching the exponential factor, so

$$
AX=\left(Av\right)e^{mt}=mve^{mt},
$$

where the last step is the eigenvalue property. The two expressions are equal, so $X$ solves the system. This is the entire derivation, and it explains why the method is so short: the eigenvalue property is precisely the statement that the two sides of the system agree.

### 3.3 Method: reducing an equation to a system

1. Solve the equation for its highest derivative, so that the highest derivative is alone on one side.
2. Name the unknown and its derivatives up to one order below the highest.
3. Differentiate each name to get one statement per name.
4. Use the rearranged equation for the statement about the highest derivative.
5. Count the statements: there must be as many as the order of the equation.

### 3.4 Method: writing the system as a matrix

1. Fix an order for the unknowns and write it down once.
2. Take the first statement and list the coefficients of the unknowns in that order, using zero for any unknown that does not appear.
3. Repeat for each statement, producing one row of the matrix per statement.
4. Move any term that does not involve the unknowns to the right-hand side and collect it as the forcing column.
5. Multiply the matrix back by the column of unknowns to confirm that the rows reproduce the statements.

### 3.5 Method: finding eigenvalues

1. Write the matrix and subtract $m$ from each diagonal entry.
2. Form the determinant of the result, expanding carefully for order two and order three.
3. Set the determinant equal to zero and simplify to a polynomial in $m$.
4. Factor the polynomial by inspection or by the formula for quadratics.
5. Check the roots against the trace and the determinant.

### 3.6 Method: finding eigenvectors

1. Substitute one eigenvalue into the matrix, so that the diagonal entries become numbers.
2. Multiply the resulting matrix by an unknown column and set the product equal to zero.
3. Write out the equations; for a correct eigenvalue they always reduce to fewer independent equations than unknowns.
4. Choose a convenient value for one unknown, avoiding the value that makes the column zero.
5. Clear any fractions, then verify by direct multiplication that the matrix times the column equals the eigenvalue times the column.

### 3.7 Method: assembling the solution

1. Write one term for each eigenvalue, of the form constant times eigenvector times exponential.
2. If an eigenvalue is repeated with only one direction, add the special term containing $t$ and the generalised eigenvector.
3. If the eigenvalues are complex, convert the complex terms into real terms containing cosine and sine.
4. Count the constants, and compare with the number of equations.
5. If the question asks for the original unknown function, take the first entry of the column.

### 3.8 Method: checking the answer

1. Differentiate the claimed column of solutions.
2. Multiply the matrix by the claimed column.
3. Compare entry by entry, and simplify. The difference must be zero for every value of $t$, not merely at one point.
4. If the original equation was a scalar equation, substitute the first entry into it as well.

## 4. Representative Worked Examples and Solutions

### 4.1 Problem: reduce a small equation and solve it

Reduce $y''=5y'-6y$ to a first-order system, write it in matrix form, and solve it.

### 4.2 Solution: two names, a small matrix, two eigenvalues

Step 1. The equation already has its highest derivative alone, so nothing needs rearranging.

Step 2. Name the unknown and its first derivative, using $x_{1}$ for the unknown and $x_{2}$ for the derivative.

$$
x_{1}=y, \qquad x_{2}=y' .
$$

Step 3. Differentiate both names. The first gives $x_{1}'=x_{2}$. The second gives $x_{2}'=y''$, and the equation says $y''$ is $5y'-6y$, which in the new names is $5x_{2}-6x_{1}$.

$$
x_{1}'=x_{2}, \qquad x_{2}'=-6x_{1}+5x_{2}
$$

Step 4. Write the matrix, keeping the order $x_{1}$ then $x_{2}$.

$$
A=\begin{pmatrix} 0 & 1 \\ -6 & 5 \end{pmatrix}
$$

Step 5. Subtract $m$ from the diagonal entries.

$$
A-mI=\begin{pmatrix} -m & 1 \\ -6 & 5-m \end{pmatrix}
$$

Step 6. Form the determinant.

$$
\det\left(A-mI\right)=(-m)(5-m)-(-6)(1)=m^{2}-5m+6
$$

Step 7. Factor.

$$
m^{2}-5m+6=(m-2)(m-3)
$$

so the eigenvalues are $2$ and $3$. The diagonal entries add to $5$ and the determinant is $6$, matching the sum and product of the eigenvalues.

Step 8. Find the eigenvector for $m=2$ by replacing $m$ with $2$ in the matrix minus $m$ times the identity.

$$
\begin{pmatrix} -2 & 1 \\ -6 & 3 \end{pmatrix}\begin{pmatrix} a \\ b \end{pmatrix}=0 \quad \Longrightarrow \quad -2a+b=0
$$

The second row is three times the first, so it adds nothing. Choosing $a=1$ gives $b=2$, and the eigenvector is the column with entries $1$ and $2$.

Step 9. Verify it by multiplication.

$$
\begin{pmatrix} 0 & 1 \\ -6 & 5 \end{pmatrix}\begin{pmatrix} 1 \\ 2 \end{pmatrix}=\begin{pmatrix} 2 \\ 4 \end{pmatrix}=2\begin{pmatrix} 1 \\ 2 \end{pmatrix}
$$

The first row gives one times two, which is two; the second row gives minus six plus ten, which is four. Both entries are twice the original, so the verification succeeds.

Step 10. Find the eigenvector for $m=3$.

$$
\begin{pmatrix} -3 & 1 \\ -6 & 2 \end{pmatrix}\begin{pmatrix} a \\ b \end{pmatrix}=0 \quad \Longrightarrow \quad -3a+b=0
$$

Choosing $a=1$ gives $b=3$.

Step 11. Verify the second pair.

$$
\begin{pmatrix} 0 & 1 \\ -6 & 5 \end{pmatrix}\begin{pmatrix} 1 \\ 3 \end{pmatrix}=\begin{pmatrix} 3 \\ 9 \end{pmatrix}=3\begin{pmatrix} 1 \\ 3 \end{pmatrix}
$$

Step 12. Write the general solution of the system.

$$
X=c_{1}\begin{pmatrix} 1 \\ 2 \end{pmatrix}e^{2t}+c_{2}\begin{pmatrix} 1 \\ 3 \end{pmatrix}e^{3t}
$$

Step 13. Read off the unknown function, which is the first entry.

$$
y=c_{1}e^{2t}+c_{2}e^{3t}
$$

Step 14. Check the answer in the original equation. For the first term, the first derivative is twice the term and the second derivative is four times it, so the left side is four times the term while the right side is five times two minus six times one, which is also four times the term. For the second term, the derivatives multiply by three and by nine, and nine equals fifteen minus six. Both terms work, and there are two constants, matching the order two.

### 4.3 Problem: solve a system given only as a matrix

Solve $X'=AX$ where $A$ has first row $1$ and $1$, and second row $2$ and $0$.

### 4.4 Solution: read the equations, then the eigenvalues

Step 1. Read the two equations from the rows. The first row gives $x_{1}'=x_{1}+x_{2}$ and the second gives $x_{2}'=2x_{1}$.

Step 2. Subtract $m$ from the diagonal and form the determinant.

$$
\det\left(A-mI\right)=(1-m)(-m)-2=m^{2}-m-2
$$

Step 3. Factor.

$$
m^{2}-m-2=(m-2)(m+1)
$$

so the eigenvalues are $2$ and $-1$. The diagonal entries add to $1$ and the determinant is $-2$, matching $2-1$ and $2$ times $-1$.

Step 4. Find the eigenvector for $m=2$.

$$
\begin{pmatrix} -1 & 1 \\ 2 & -2 \end{pmatrix}\begin{pmatrix} a \\ b \end{pmatrix}=0 \quad \Longrightarrow \quad -a+b=0
$$

Choose $a=1$ and $b=1$.

Step 5. Verify the first pair.

$$
\begin{pmatrix} 1 & 1 \\ 2 & 0 \end{pmatrix}\begin{pmatrix} 1 \\ 1 \end{pmatrix}=\begin{pmatrix} 2 \\ 2 \end{pmatrix}=2\begin{pmatrix} 1 \\ 1 \end{pmatrix}
$$

Step 6. Find the eigenvector for $m=-1$.

$$
\begin{pmatrix} 2 & 1 \\ 2 & 1 \end{pmatrix}\begin{pmatrix} a \\ b \end{pmatrix}=0 \quad \Longrightarrow \quad 2a+b=0
$$

Choose $a=1$ and $b=-2$.

Step 7. Verify the second pair.

$$
\begin{pmatrix} 1 & 1 \\ 2 & 0 \end{pmatrix}\begin{pmatrix} 1 \\ -2 \end{pmatrix}=\begin{pmatrix} -1 \\ 2 \end{pmatrix}=-1\cdot\begin{pmatrix} 1 \\ -2 \end{pmatrix}
$$

Step 8. Write the general solution and check the first equation.

$$
X=c_{1}\begin{pmatrix} 1 \\ 1 \end{pmatrix}e^{2t}+c_{2}\begin{pmatrix} 1 \\ -2 \end{pmatrix}e^{-t}
$$

The first component is $c_{1}e^{2t}+c_{2}e^{-t}$ and the second is $c_{1}e^{2t}-2c_{2}e^{-t}$. Adding them gives $2c_{1}e^{2t}-c_{2}e^{-t}$, while the derivative of the first component is $2c_{1}e^{2t}-c_{2}e^{-t}$. They agree.

Step 9. Check the second equation in the same way. The derivative of the second component is $2c_{1}e^{2t}+2c_{2}e^{-t}$, and twice the first component is $2c_{1}e^{2t}+2c_{2}e^{-t}$. They agree, so the answer is confirmed.

### 4.5 Problem: a doubled eigenvalue that needs help

Solve $X'=AX$ where $A$ has first row $2$ and $1$, and second row $0$ and $2$.

### 4.6 Solution: one direction only, so a generalised eigenvector

Step 1. Form the characteristic determinant.

$$
\det(A-mI)=(2-m)(2-m)-0=(2-m)^{2}
$$

so the only eigenvalue is $2$, counted twice.

Step 2. Substitute $m=2$ to look for eigenvectors.

$$
\begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix}\begin{pmatrix} a \\ b \end{pmatrix}=0 \quad \Longrightarrow \quad b=0
$$

Any column with second entry zero works, and the simplest is the column with entries $1$ and $0$. There is only one direction, so the matrix is defective and one more column is needed.

Step 3. Verify the eigenvector.

$$
\begin{pmatrix} 2 & 1 \\ 0 & 2 \end{pmatrix}\begin{pmatrix} 1 \\ 0 \end{pmatrix}=\begin{pmatrix} 2 \\ 0 \end{pmatrix}=2\begin{pmatrix} 1 \\ 0 \end{pmatrix}
$$

Step 4. Solve the extra system, in which the matrix minus twice the identity acts on an unknown column and produces the eigenvector.

$$
\begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix}\begin{pmatrix} p \\ q \end{pmatrix}=\begin{pmatrix} 1 \\ 0 \end{pmatrix} \quad \Longrightarrow \quad q=1
$$

The first entry of the unknown column is free, and the simplest choice is zero, giving the column with entries $0$ and $1$.

Step 5. Verify the extra column.

$$
\begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix}\begin{pmatrix} 0 \\ 1 \end{pmatrix}=\begin{pmatrix} 1 \\ 0 \end{pmatrix}
$$

Step 6. Assemble the general solution, with the special term for the doubled eigenvalue.

$$
X=c_{1}\begin{pmatrix} 1 \\ 0 \end{pmatrix}e^{2t}+c_{2}\left[\begin{pmatrix} 1 \\ 0 \end{pmatrix}t+\begin{pmatrix} 0 \\ 1 \end{pmatrix}\right]e^{2t}
$$

Step 7. Read off the two components.

$$
x_{1}=(c_{1}+c_{2}t)e^{2t}, \qquad x_{2}=c_{2}e^{2t}
$$

Step 8. Check the second equation, which is the shortcut equation $x_{2}'=2x_{2}$. The derivative of the second component is twice itself, so that equation holds.

Step 9. Check the first equation, which is $x_{1}'=2x_{1}+x_{2}$. The derivative of the first component is $c_{2}e^{2t}$ plus twice the component itself, and twice the component plus the second component is $2(c_{1}+c_{2}t)e^{2t}+c_{2}e^{2t}$. The two agree.

Step 10. Notice the meaning. The first component is a constant plus a multiple of $t$, all multiplied by the exponential. That is exactly the shape that a doubled root produces in the older method, and the factor $t$ was forced by the shortage of eigenvectors.

### 4.7 Problem: a pair of complex eigenvalues

Solve $X'=AX$ where $A$ has first row $0$ and $-1$, and second row $1$ and $0$.

### 4.8 Solution: two imaginary eigenvalues, and cosine with sine

Step 1. Form the characteristic determinant. The diagonal entries are both $0$, so the matrix minus $m$ times the identity has $-m$ in both diagonal positions.

$$
\det(A-mI)=(-m)(-m)-(-1)(1)=m^{2}+1
$$

Step 2. Solve it. The equation $m^{2}+1=0$ has the two roots $i$ and $-i$, where $i$ is the imaginary unit whose square is $-1$. The trace is $0$ and the determinant is $1$, matching the sum and the product of these roots.

Step 3. Read the equations from the rows before doing more algebra. The first row gives $x_{1}'=-x_{2}$ and the second gives $x_{2}'=x_{1}$.

Step 4. Guess from the equations. Differentiating the first equation gives $x_{1}''=-x_{2}'=-x_{1}$, whose solutions are cosine and sine. So $x_{1}$ is a combination of cosine and sine, and $x_{2}$ is minus the derivative of $x_{1}$.

Step 5. Write the answer using the eigenvalue method to confirm the guess. For the eigenvalue $i$, the real part of the eigenvector is the column with entries $1$ and $0$, and the imaginary part is the column with entries $0$ and $-1$.

$$
X=c_{1}\left[\begin{pmatrix} 1 \\ 0 \end{pmatrix}\cos t-\begin{pmatrix} 0 \\ -1 \end{pmatrix}\sin t\right]+c_{2}\left[\begin{pmatrix} 1 \\ 0 \end{pmatrix}\sin t+\begin{pmatrix} 0 \\ -1 \end{pmatrix}\cos t\right]
$$

Step 6. Simplify.

$$
X=c_{1}\begin{pmatrix} \cos t \\ \sin t \end{pmatrix}+c_{2}\begin{pmatrix} \sin t \\ -\cos t \end{pmatrix}
$$

Step 7. Verify the first solution. Its components are cosine and sine. The derivative of the first component is minus sine, and the right side of the first equation is minus the second component, which is minus sine. The derivative of the second component is cosine, and the right side of the second equation is the first component, which is cosine. Both equations hold.

Step 8. Verify the second solution. Its components are sine and minus cosine. The derivative of the first is cosine, and minus the second component is also cosine. The derivative of the second is sine, and the first component is sine. Both equations hold.

Step 9. Interpret. The two components trace a circle of radius depending on the constants, because the sum of their squares is constant. A pair of pure imaginary eigenvalues always produces this circulating behaviour, and a real part would make the circle spiral outwards or inwards.

### 4.9 Problem: a system with a forcing term

Solve $X'=AX+B$, where $A$ has first row $1$ and $1$, second row $2$ and $0$, and the forcing column has entries $0$ and $2$.

### 4.10 Solution: solve the homogeneous part first, then add one more solution

Step 1. Write the two equations with their extra terms. The first is $x_{1}'=x_{1}+x_{2}$ and the second is $x_{2}'=2x_{1}+2$.

Step 2. Record the homogeneous solution found in Section 4.4.

$$
X_{c}=c_{1}\begin{pmatrix} 1 \\ 1 \end{pmatrix}e^{2t}+c_{2}\begin{pmatrix} 1 \\ -2 \end{pmatrix}e^{-t}
$$

Step 3. Look for one solution of the full system that does not contain any exponential. Try a constant column with entries $p$ and $q$.

Step 4. Substitute the trial. A constant column has zero derivative, so the left side is the zero column and the right side is the matrix times the trial plus the forcing column.

$$
\begin{pmatrix} 0 \\ 0 \end{pmatrix}=\begin{pmatrix} p+q \\ 2p+2 \end{pmatrix}
$$

Step 5. Solve the two small equations. The first says $q=-p$ and the second says $p=-1$, so $q=1$ and the trial column has entries $-1$ and $1$.

Step 6. Verify the particular solution by substitution. Its derivative is zero, and the matrix times it plus the forcing column is the column with entries $-1+1$ and $-2+2$, which is the zero column. The verification succeeds.

Step 7. Write the general solution by adding the two parts.

$$
X=c_{1}\begin{pmatrix} 1 \\ 1 \end{pmatrix}e^{2t}+c_{2}\begin{pmatrix} 1 \\ -2 \end{pmatrix}e^{-t}+\begin{pmatrix} -1 \\ 1 \end{pmatrix}
$$

Step 8. Check the first equation with the full answer. The components are $x_{1}=c_{1}e^{2t}+c_{2}e^{-t}-1$ and $x_{2}=c_{1}e^{2t}-2c_{2}e^{-t}+1$. Their sum is $2c_{1}e^{2t}-c_{2}e^{-t}$, and the derivative of the first component is $2c_{1}e^{2t}-c_{2}e^{-t}$. They agree.

Step 9. Check the second equation. The derivative of the second component is $2c_{1}e^{2t}+2c_{2}e^{-t}$, while twice the first component plus two is $2c_{1}e^{2t}+2c_{2}e^{-t}-2+2$. They agree, so the general solution is correct.

Step 10. Count the constants. There are two, matching the two equations, and the answer contains both a homogeneous part and a forcing part as the theory requires.

### 4.11 Problem: reduce an equation of order three

Reduce $y'''=6y-11y'+6y''$ to a first-order system and write the matrix form.

### 4.12 Solution: three names and the companion shape

Step 1. The highest derivative is already alone, so the equation needs no rearrangement.

Step 2. Name the unknown and its first two derivatives.

$$
x_{1}=y, \qquad x_{2}=y', \qquad x_{3}=y'' .
$$

Step 3. Differentiate each name and use the equation for the last statement.

$$
x_{1}'=x_{2}, \qquad x_{2}'=x_{3}, \qquad x_{3}'=6x_{1}-11x_{2}+6x_{3}
$$

Step 4. Assemble the matrix, with one row per statement.

$$
A=\begin{pmatrix} 0 & 1 & 0 \\ 0 & 0 & 1 \\ 6 & -11 & 6 \end{pmatrix}
$$

Step 5. Note the companion shape. The first two rows have a single one just after the diagonal, and the last row holds the coefficients of the equation with the signs changed, in reverse order relative to the equation as first written.

Step 6. State the characteristic polynomial by the theorem of Section 2.2, and check two coefficients. The polynomial is $m^{3}-6m^{2}+11m-6$. The sum of the diagonal entries is $6$, which matches the coefficient $6$ with the sign changed, and the determinant of the matrix is $6$, which matches the constant term.

Step 7. Factor the polynomial by trying small values. At $m=1$ the polynomial is $1-6+11-6=0$, so $1$ is a root. Dividing out the factor $m-1$ leaves $m^{2}-5m+6$, which factors as $(m-2)(m-3)$. The eigenvalues are $1$, $2$ and $3$.

Step 8. Record the three eigenvectors by the standard shortcut for companion matrices, which is the column with entries one, the eigenvalue, and the eigenvalue squared.

$$
v_{1}=\begin{pmatrix} 1 \\ 1 \\ 1 \end{pmatrix}, \qquad v_{2}=\begin{pmatrix} 1 \\ 2 \\ 4 \end{pmatrix}, \qquad v_{3}=\begin{pmatrix} 1 \\ 3 \\ 9 \end{pmatrix}
$$

Step 9. Verify one of them, for $m=2$, by multiplication.

$$
\begin{pmatrix} 0 & 1 & 0 \\ 0 & 0 & 1 \\ 6 & -11 & 6 \end{pmatrix}\begin{pmatrix} 1 \\ 2 \\ 4 \end{pmatrix}=\begin{pmatrix} 2 \\ 4 \\ 6-22+24 \end{pmatrix}=\begin{pmatrix} 2 \\ 4 \\ 8 \end{pmatrix}
$$

The result is twice the original column, so the verification succeeds.

Step 10. Write the general solution of the system and the original function.

$$
y=c_{1}e^{t}+c_{2}e^{2t}+c_{3}e^{3t}
$$

Step 11. Check one term in the original equation. For the term with $e^{2t}$ the successive derivatives multiply by $2$, by $4$ and by $8$. The right side of the equation is six times one minus eleven times two plus six times four, which is $6-22+24=8$, the same as the third derivative. The term works, and three constants appear as the order requires.

## 5. Mathematical Extensions, Limits, and Common Errors

### 5.1 Beginner misconceptions

- **Thinking the new letters are extra unknowns.** The letters $x_{1}$ and $x_{2}$ are not new information; they are names for the unknown and its derivative. The reduction renames, it does not enlarge the problem.
- **Thinking the system is a different problem.** The system and the equation of order $n$ have exactly the same solutions, written in different order. If a system answer and a scalar answer disagree, one of them is wrong.
- **Believing the matrix rows may be written in any order.** The unknown column fixes the order, and every row must follow it. A row that lists the coefficients in a different order describes a different system.
- **Forgetting the zeros.** A missing coefficient is a zero, and it must be written. Leaving a gap in a row makes the matrix ambiguous when it is multiplied back out.
- **Believing that a repeated eigenvalue always needs a factor of $t$.** It needs one only when there is a single eigenvector direction. When two independent directions exist, the plain sum of exponentials is complete.
- **Believing that a factor of $t$ is never needed.** The opposite error. When the matrix is defective, no combination of exponentials without a factor of $t$ can produce the general solution.
- **Taking the zero column as an eigenvector.** Every matrix sends the zero column to zero, so allowing it would make the definition meaningless. The eigenvector must be non-zero.
- **Forgetting that eigenvectors may be rescaled.** A column of entries $1$ and $2$ and a column of entries $3$ and $6$ describe the same direction, and both are acceptable answers. Only the direction is determined.
- **Stopping at a complex column.** A real system needs a real answer, so the complex column must be split into its real and imaginary parts using cosine and sine.
- **Mixing up the real and imaginary parts of the eigenvector.** The real part belongs with the cosine of the first solution and with the sine of the second, and the imaginary part carries the minus sign in the first solution. Writing the pair without care produces an answer that fails on substitution.
- **Omitting the forcing part.** A non-homogeneous system needs both a complementary function and a particular integral. An answer with only one of them fails the original system.
- **Using the wrong trial at resonance.** If the exponential in the forcing matches an eigenvalue, the plain trial cannot work, and it must be multiplied by $t$.
- **Reporting the wrong number of constants.** Two equations need two constants, three need three. A count that does not match the number of equations signals a missing case.
- **Not checking.** Multiplication of the matrix by the claimed column, and differentiation of the claimed solution, catch nearly every mistake in this topic within a minute.

### 5.2 Where this idea leads

The reduction is used far beyond this topic. Large computer programs that solve differential equations almost never accept an equation of order four; they accept systems of first-order equations, because a first-order system is exactly what a numerical stepper needs. Every higher-order equation handed to such a program is reduced first, and the reduction is the one described here.

The eigenvalue method also extends. When the coefficient matrix depends on time, the eigenvectors rotate and the simple exponential answer fails, but the idea of diagonalising the problem survives in more elaborate forms. When the equation is non-linear, the reduction still works but the matrix method does not, because there is no matrix. Knowing which half of the technique survives is part of understanding it.

### 5.3 A short recipe to remember

Reduce by naming the derivatives, taking one name per order, and count the statements against the order. Write the matrix by rows, keeping one order for the unknowns everywhere. Find the eigenvalues by making the determinant zero, and check them against the sum of the diagonal entries and the determinant. Find the eigenvectors by making the matrix minus the eigenvalue times the identity act on a column and give zero, and always verify by multiplication. Then read the answer from the eigenvalues: different numbers give plain exponentials, a doubled number with one direction gives an extra term containing $t$, a doubled number with two directions needs nothing extra, and a complex pair gives cosine and sine. Add a particular integral when a forcing term is present, and finish by substituting the answer back into the system.
