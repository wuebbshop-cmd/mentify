## 1. Core Concept Overview & Intuition

Imagine you are pulling a heavy box along the floor with a rope. You pull with a certain force, and the rope makes some angle with the floor. Only the part of your pull that points along the floor actually helps move the box forward. The part of the pull pointing upward does nothing to slide the box. This everyday situation captures the central idea of this topic: when two vectors meet at an angle, we often care about how much of one vector "acts along" the other.

A vector is a quantity with both size (called magnitude) and direction. Force, displacement, and velocity are vectors. Two different products let us combine two vectors, and they answer two different questions.

The first product answers: "How much of one vector lies along the other?" The answer is a single number, a scalar, so this product is called the **dot product** or **scalar product**. In the rope example, the dot product of the force vector with the direction of the floor gives the useful forward pull.

The second product answers: "What single vector is perpendicular to both of these vectors?" The answer is a new vector, so this product is called the **cross product** or **vector product**. If you hold a screwdriver and turn it from one direction toward another, the screw advances along a line perpendicular to both turning directions. That advancing direction is exactly what the cross product produces.

Where the analogy stops being exact: a real rope has thickness and the box has friction, but vectors are pure arrows with no thickness. We treat them as ideal arrows starting from a common point.

The two products are useful because they let us measure angles between arrows, test whether arrows are at right angles, find projections, build equations of planes, and compute areas and volumes. All of these ideas are built from the same two definitions, so once the definitions are clear, the rest follows step by step.

## 2. Mathematical Formalization & Core Definitions

### 2.1 Magnitude of a Vector

The **magnitude** of a vector is its length. It is written with vertical bars, for example $\lvert A \rvert$, and is a non-negative number. If a vector is written in component form as

$$
A=A_{1}\hat{i}+A_{2}\hat{j}+A_{3}\hat{k}
$$

then its magnitude is found by the distance formula:

$$
\lvert A \rvert=\sqrt{A_{1}^{2}+A_{2}^{2}+A_{3}^{2}}
$$

Here $\hat{i}$, $\hat{j}$, $\hat{k}$ are the unit vectors pointing along the positive $x$, $y$, and $z$ axes. A **unit vector** is a vector of length one. The unit vector in the direction of $A$ is obtained by dividing $A$ by its own length:

$$
\hat{a}=\frac{A}{\lvert A \rvert}
$$

This process is called normalising the vector. It keeps the direction but rescales the length to one.

The **resultant** of two vectors is the single vector obtained by adding them. In component form, addition is done component by component:

$$
A+B=(A_{1}+B_{1})\hat{i}+(A_{2}+B_{2})\hat{j}+(A_{3}+B_{3})\hat{k}
$$

The magnitude of the resultant is then found using the magnitude formula above.

### 2.2 The Dot or Scalar Product

> If $A$ and $B$ are two vectors, the scalar product of $A$ and $B$ is defined as $AB\cos\theta$, where $A$ and $B$ are the magnitudes of the vectors $A$ and $B$, and $\theta$ is the angle between them.

The dot product is written $A\cdot B$. So

$$
A\cdot B=AB\cos\theta
$$

This can be read in two equivalent ways: it equals the magnitude of $A$ multiplied by the projection of $B$ on $A$, or the magnitude of $B$ multiplied by the projection of $A$ on $B$. In either case the result is a scalar quantity, that is, a plain number with no direction.

A **projection** is the "shadow" length of one vector cast along the direction of another. If $\hat{b}$ is the unit vector in the direction of $B$, then the projection of $A$ on $B$ is $A\cdot\hat{b}$.

Two special angles follow immediately from the definition. If the vectors are at right angles, $\theta=90^{\circ}$, then $\cos 90^{\circ}=0$, so $A\cdot B=0$. Such vectors are called **orthogonal** or **perpendicular**. If the vectors point in the same direction, $\theta=0^{\circ}$, then $\cos 0^{\circ}=1$, so $A\cdot B=AB$.

When both vectors are written in component form, expanding the product term by term and using the facts that $\hat{i}\cdot\hat{i}=\hat{j}\cdot\hat{j}=\hat{k}\cdot\hat{k}=1$ and that $\hat{i}\cdot\hat{j}=\hat{i}\cdot\hat{k}=\hat{j}\cdot\hat{k}=0$ leaves only three terms:

$$
A\cdot B=A_{1}B_{1}+A_{2}B_{2}+A_{3}B_{3}
$$

This component formula is the workhorse for all dot product calculations.

### 2.3 The Cross or Vector Product

> The cross or vector product of $A$ and $B$, written $A\times B$ and read as "$A$ cross $B$", is defined as a vector having the magnitude $AB\sin\theta$, where $\theta$ is the angle between the two vectors. The product vector acts in a direction perpendicular to $A$ and $B$ in such a sense that $A$, $B$, and $A\times B$ form a right-handed system in that order.

The magnitude is therefore

$$
\lvert A\times B \rvert=AB\sin\theta
$$

The direction is fixed by the **right-hand rule**. The axes $OX$, $OY$, $OZ$ form a right-handed set if a rotation from $OX$ to $OY$ drives a right-handed corkscrew along the positive $OZ$ direction. Reversing the order of the vectors reverses the direction of rotation, so

$$
B\times A=-(A\times B)
$$

This means the cross product is not commutative.

Two special angles again follow. If $\theta=0^{\circ}$, then $\sin 0^{\circ}=0$, so $A\times B=0$. If $\theta=90^{\circ}$, then $\sin 90^{\circ}=1$, so $\lvert A\times B \rvert=AB$.

For component form, the basis products are $\hat{i}\times\hat{i}=\hat{j}\times\hat{j}=\hat{k}\times\hat{k}=0$ and

$$
\hat{i}\times\hat{j}=\hat{k},\qquad \hat{j}\times\hat{k}=\hat{i},\qquad \hat{k}\times\hat{i}=\hat{j}
$$

with the reverse orders giving the negatives. Expanding term by term gives

$$
A\times B=(A_{2}B_{3}-A_{3}B_{2})\hat{i}+(A_{3}B_{1}-A_{1}B_{3})\hat{j}+(A_{1}B_{2}-A_{2}B_{1})\hat{k}
$$

This is exactly the expansion of the determinant

$$
A\times B=\begin{vmatrix}\hat{i}&\hat{j}&\hat{k}\A_{1}&A_{2}&A_{3}\B_{1}&B_{2}&B_{3}\end{vmatrix}
$$

The determinant form is the standard shortcut for computing a cross product.

### 2.4 Vector Perpendicular to a Plane

The vector $A\times B$ is perpendicular to the plane in which $A$ and $B$ lie. The right-hand thumb rule gives its direction. To obtain the unit vector perpendicular to that plane, divide by the magnitude:

$$
\hat{n}=\frac{A\times B}{\lvert A\times B \rvert}
$$

### 2.5 Triple Products

> If $A$, $B$, $C$ are three vectors, the scalar formed by the product $A\cdot(B\times C)$ is called the scalar triple product.

In determinant form,

$$
A\cdot(B\times C)=\begin{vmatrix}A_{1}&A_{2}&A_{3}\B_{1}&B_{2}&B_{3}\C_{1}&C_{2}&C_{3}\end{vmatrix}
$$

> If $A$, $B$, and $C$ are three vectors, then $A\times(B\times C)$ and $(A\times B)\times C$ are called vector triple products.

The vector triple product satisfies the expansion

$$
A\times(B\times C)=(A\cdot C)B-(A\cdot B)C
$$

## 3. Key Theorems & Essential Results

> **Theorem (Cosine Rule).** For a triangle with sides $A$, $B$, $C$ and angle $\theta$ between the vectors $A$ and $B$, one has $C^{2}=A^{2}+B^{2}-2AB\cos\theta$.

The proof uses the dot product. From the triangle relation $C=A-B$, taking the dot product of $C$ with itself gives

$$
\begin{aligned}C\cdot C&=(A-B)\cdot(A-B)\\&=A\cdot A-2A\cdot B+B\cdot B\end{aligned}
$$

and since $A\cdot A=A^{2}$, $B\cdot B=B^{2}$, and $A\cdot B=AB\cos\theta$, the result follows.

> **Theorem (Properties of the Scalar Triple Product).** The scalar triple product satisfies $A\cdot(B\times C)=B\cdot(C\times A)=C\cdot(A\times B)$, and $A\cdot(A\times B)=0$.

The first property holds because interchanging two rows of a determinant reverses its sign, and a cyclic rearrangement of three rows amounts to two such interchanges. The second holds because two rows of the determinant become identical.

> **Theorem (Geometric Meaning).** The absolute value of the scalar triple product represents the volume of a parallelepiped with sides $A$, $B$, and $C$.

> **Theorem (Coplanarity Test).** Three vectors lie in the same plane if and only if their scalar triple product is zero.

> **Theorem (Area of a Parallelogram and Triangle).** The area of the parallelogram with sides $A$ and $B$ is $\lvert A\times B \rvert$. The area of the triangle with the same two sides is $\tfrac{1}{2}\lvert A\times B \rvert$.

> **Theorem (Distance from a Point to a Plane).** If a plane has equation $ax+by+cz=d$, then the distance from the point $(x_{1},y_{1},z_{1})$ to the plane is

> 

$$
\frac{\lvert ax_{1}+by_{1}+cz_{1}-d \rvert}{\sqrt{a^{2}+b^{2}+c^{2}}}
$$

> **Theorem (Non-Associativity of the Cross Product).** In general $(A\times B)\times C\neq A\times(B\times C)$, so parentheses are essential in a triple cross product.

## 4. Worked Exemplar Problem with Step-by-Step Solution

**Problem.** Given $A=3\hat{i}+\hat{j}+2\hat{k}$ and $B=\hat{i}-2\hat{j}-4\hat{k}$ as position vectors of points $P$ and $Q$ respectively:

(a) find an equation for the plane passing through $Q$ and perpendicular to the line $PQ$;

(b) find the distance from the point $(-1,1,1)$ to that plane.

**Step 1. Find the direction vector of the line $PQ$.**

The vector from $P$ to $Q$ is $Q$ minus $P$:

$$
\begin{aligned}PQ&=B-A\\&=(1-3)\hat{i}+(-2-1)\hat{j}+(-4-2)\hat{k}\\&=-2\hat{i}-3\hat{j}-6\hat{k}\end{aligned}
$$

This vector is normal (perpendicular) to the required plane.

**Step 2. Set up the perpendicularity condition.**

Let $R(x,y,z)$ be any point on the plane, with position vector $r$. Then

$$
QR=r-B=(x-1)\hat{i}+(y+2)\hat{j}+(z+4)\hat{k}
$$

Because the plane is perpendicular to $PQ$, the vector $QR$ lies in the plane and must be perpendicular to $PQ$. Hence their dot product is zero:

$$
PQ\cdot QR=0
$$

**Step 3. Expand the dot product.**

$$
\begin{aligned}(-2)(x-1)+(-3)(y+2)+(-6)(z+4)&=0\\-2x+2-3y-6-6z-24&=0\\-2x-3y-6z-28&=0\end{aligned}
$$

Multiplying through by $-1$ gives the plane equation

$$
2x+3y+6z+28=0
$$

**Step 4. Apply the distance formula.**

Rewrite the plane as $2x+3y+6z=-28$, so $a=2$, $b=3$, $c=6$, $d=-28$. The distance from $(-1,1,1)$ is

$$
\begin{aligned}\text{distance}&=\frac{\lvert 2(-1)+3(1)+6(1)+28 \rvert}{\sqrt{2^{2}+3^{2}+6^{2}}}\\&=\frac{\lvert -2+3+6+28 \rvert}{7}\\&=\frac{35}{7}\\&=5\end{aligned}
$$

So the distance from the point to the plane is $5$ units.

**Step 5. Interpret the answer.** The plane is a flat sheet through $Q$ standing at right angles to the line $PQ$. The number $5$ is the shortest straight-line gap from the given point to that sheet.

## 5. High-Yield Exam Takeaways & Common Pitfalls

**Takeaways.**

- The dot product gives a scalar; the cross product gives a vector. Always check which type of answer the question expects.
- Use $A\cdot B=A_{1}B_{1}+A_{2}B_{2}+A_{3}B_{3}$ for the dot product and the determinant for the cross product. Both are fast and reliable.
- To find an angle between two vectors, use $\cos\theta=\dfrac{A\cdot B}{AB}$.
- To test perpendicularity, check whether the dot product is zero.
- To test parallelism, check whether the cross product is zero.
- To find a unit vector, divide the vector by its magnitude.
- To find a projection of $A$ on $B$, compute $A\cdot\hat{b}$ where $\hat{b}=B/\lvert B \rvert$.
- To find a plane perpendicular to a given vector, use $(r-r_{0})\cdot n=0$ where $n$ is the normal vector and $r_{0}$ is a point on the plane.
- To find the area of a triangle from three vertices, form two side vectors from one vertex and take half the magnitude of their cross product.
- To test coplanarity of three vectors, check whether the scalar triple product is zero.
- To find the volume of a parallelepiped, take the absolute value of the scalar triple product.

**Common pitfalls.**

- Forgetting that $B\times A=-(A\times B)$. Reversing the order flips the sign.
- Writing $A\times B$ as a scalar. It is a vector with three components.
- Dropping the absolute value in the distance formula. Distance is never negative.
- Mixing up the plane equation signs. Always re-derive from $(r-r_{0})\cdot n=0$ rather than memorising.
- Assuming $(A\times B)\times C=A\times(B\times C)$. The cross product is not associative, so parentheses matter.
- Using degrees and radians interchangeably in $\cos\theta$ and $\sin\theta$. Match the mode of your calculator to the units in the question.
- Forgetting to normalise before projecting. The projection formula uses the unit vector $\hat{b}$, not $B$ itself.
- Confusing the scalar triple product with the vector triple product. The first is a number; the second is a vector.
- Omitting the check that three vectors actually form a triangle before applying the cosine rule. Verify $A=B+C$ or that the sum is zero first.
- Rounding too early in multi-step problems. Keep full precision until the final answer.