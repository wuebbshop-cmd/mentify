## 1. Core Concept Overview & Intuition

The dot and cross products are the two fundamental ways of multiplying vectors. They answer two different geometric questions, and the entire topic is built on keeping them apart.

The **dot (scalar) product** measures how much one vector points along another. Its output is a single number (a scalar). It is the tool for angles between vectors, projections, perpendicularity tests, and equations of planes.

The **cross (vector) product** measures the "turning" or "spread" between two vectors. Its output is a new vector, perpendicular to both inputs. It is the tool for perpendicular directions, areas of parallelograms and triangles, and the triple products.

The unifying geometric idea is the angle $\theta$ between the two vectors. Both products are built from the same three ingredients: the magnitudes $A$ and $B$, and the angle $\theta$. The dot product uses $\cos\theta$; the cross product uses $\sin\theta$. This single observation explains almost every result in the chapter:

- When $\theta=0^{\circ}$ (parallel vectors), $\cos\theta=1$ and $\sin\theta=0$, so the dot product is maximal and the cross product vanishes.
- When $\theta=90^{\circ}$ (perpendicular vectors), $\cos\theta=0$ and $\sin\theta=1$, so the dot product vanishes and the cross product is maximal.

A second unifying idea is **projection**. The dot product $A\cdot B$ equals $A$ times the projection of $B$ on $A$, and equally equals $B$ times the projection of $A$ on $B$. This is why the dot product produces distances from points to planes and equations of planes.

A third idea is **orientation**. The cross product is not symmetric: reversing the order reverses the direction of the product vector, so $B\times A=-(A\times B)$. The direction is fixed by the right-hand rule, which makes $A$, $B$, and $A\times B$ a right-handed system in that order.

## 2. Mathematical Formalization & Core Definitions

### 2.1 The Dot or Scalar Product

> **Definition (Dot Product).** If $A$ and $B$ are two vectors, the scalar product of $A$ and $B$ is defined as $AB\cos\theta$, where $A$ and $B$ are the magnitudes of the vectors $A$ and $B$, and $\theta$ is the angle between them. The scalar (dot) product is denoted by $A\cdot B$.

The definition carries two equivalent projection readings:

$$
A\cdot B=AB\cos\theta
$$

$$
A\cdot B=A\times(\text{projection of }B\text{ on }A)
$$

$$
A\cdot B=B\times(\text{projection of }A\text{ on }B)
$$

In every case the result is a scalar quantity.

**Special angles.** If the two vectors are at right angles, $\theta=90^{\circ}$, so

$$
A\cdot B=AB\cos 90^{\circ}=AB(0)=0
$$

and the vectors are called orthogonal or perpendicular. If the two vectors are in the same direction, $\theta=0^{\circ}$, so

$$
A\cdot B=AB\cos 0^{\circ}=AB
$$

**Component form.** Write

$$
A=A_1\hat{i}+A_2\hat{j}+A_3\hat{k}
$$

$$
B=B_1\hat{i}+B_2\hat{j}+B_3\hat{k}
$$

Expanding the product term by term gives nine terms:

$$
A\cdot B=(A_1\hat{i}+A_2\hat{j}+A_3\hat{k})\cdot(B_1\hat{i}+B_2\hat{j}+B_3\hat{k})
$$

$$
\begin{aligned}
A\cdot B={}&A_1B_1\,\hat{i}\cdot\hat{i}+A_1B_2\,\hat{i}\cdot\hat{j}+A_1B_3\,\hat{i}\cdot\hat{k}\\
&+A_2B_1\,\hat{j}\cdot\hat{i}+A_2B_2\,\hat{j}\cdot\hat{j}+A_2B_3\,\hat{j}\cdot\hat{k}\\
&+A_3B_1\,\hat{k}\cdot\hat{i}+A_3B_2\,\hat{k}\cdot\hat{j}+A_3B_3\,\hat{k}\cdot\hat{k}
\end{aligned}
$$

Now the basis products are fixed by the definition:

$$
\hat{i}\cdot\hat{i}=\hat{j}\cdot\hat{j}=\hat{k}\cdot\hat{k}=(1)(1)\cos 0^{\circ}=1
$$

$$
\hat{i}\cdot\hat{j}=\hat{i}\cdot\hat{k}=\hat{j}\cdot\hat{k}=(1)(1)\cos 90^{\circ}=0
$$

Only the three "matching" terms survive, so

$$
A\cdot B=A_1B_1+A_2B_2+A_3B_3
$$

This is the master computational formula for the dot product and the starting point of most exam proofs.

### 2.2 The Cross or Vector Product

> **Definition (Cross Product).** The cross or vector product of $A$ and $B$, written $A\times B$ and read "A cross B", is defined as a vector having magnitude $AB\sin\theta$, where $\theta$ is the angle between the two vectors. The product vector acts in a direction perpendicular to $A$ and $B$ in such a sense that $A$, $B$, and $A\times B$ form a right-handed system in that order.

The magnitude is

$$
\lVert A\times B\rVert=AB\sin\theta
$$

**Right-hand rule.** The axes $OX$, $OY$, $OZ$ form a right-handed set if rotation from $OX$ to $OY$ corresponds to a right-handed corkscrew action along the positive direction of $OZ$; similarly, rotation from $OY$ to $OZ$ gives right-hand corkscrew action along the positive direction of $OX$.

**Reversal of order.** The product $B\times A$ reverses the direction of rotation, so the product vector acts in the opposite direction:

$$
B\times A=-(A\times B)
$$

**Special angles.** If $\theta=0^{\circ}$, then $A\times B=AB\sin 0^{\circ}=0$. If $\theta=90^{\circ}$, then $A\times B=AB\sin 90^{\circ}=AB$.

**Component form.** Expanding as for the dot product:

$$
\begin{aligned}
A\times B={}&A_1B_1\,\hat{i}\times\hat{i}+A_1B_2\,\hat{i}\times\hat{j}+A_1B_3\,\hat{i}\times\hat{k}\\
&+A_2B_1\,\hat{j}\times\hat{i}+A_2B_2\,\hat{j}\times\hat{j}+A_2B_3\,\hat{j}\times\hat{k}\\
&+A_3B_1\,\hat{k}\times\hat{i}+A_3B_2\,\hat{k}\times\hat{j}+A_3B_3\,\hat{k}\times\hat{k}
\end{aligned}
$$

Since $\hat{i}\times\hat{i}=(1)(1)\sin 0^{\circ}=0$, we have

$$
\hat{i}\times\hat{i}=\hat{j}\times\hat{j}=\hat{k}\times\hat{k}=0
$$

Since $\hat{i}\times\hat{j}=(1)(1)\sin 90^{\circ}=1$ in the direction $OZ$, we have $\hat{i}\times\hat{j}=\hat{k}$. The complete cyclic table is

$$
\hat{i}\times\hat{j}=\hat{k},\qquad \hat{j}\times\hat{k}=\hat{i},\qquad \hat{k}\times\hat{i}=\hat{j}
$$

$$
\hat{j}\times\hat{i}=-\hat{k},\qquad \hat{k}\times\hat{j}=-\hat{i},\qquad \hat{i}\times\hat{k}=-\hat{j}
$$

Collecting terms gives

$$
A\times B=(A_2B_3-A_3B_2)\hat{i}+(A_3B_1-A_1B_3)\hat{j}+(A_1B_2-A_2B_1)\hat{k}
$$

which is recognised as the expansion of the determinant

$$
A\times B=
\begin{vmatrix}
\hat{i} & \hat{j} & \hat{k}\\
A_1 & A_2 & A_3\\
B_1 & B_2 & B_3
\end{vmatrix}
$$

### 2.3 Unit Vector and Perpendicular Direction

The unit vector in the direction of a vector $B$ is

$$
\hat{b}=\frac{B}{\lVert B\rVert}
$$

The vector $A\times B$ is perpendicular to the plane containing $A$ and $B$, and the unit vector perpendicular to that plane is

$$
\frac{A\times B}{\lVert A\times B\rVert}
$$

### 2.4 Triple Products

> **Definition (Scalar Triple Product).** If $A$, $B$, $C$ are three vectors, the scalar formed by the product $A\cdot(B\times C)$ is called the scalar triple product.

With $A=A_1\hat{i}+A_2\hat{j}+A_3\hat{k}$, $B=B_1\hat{i}+B_2\hat{j}+B_3\hat{k}$, $C=C_1\hat{i}+C_2\hat{j}+C_3\hat{k}$, the scalar triple product is the determinant

$$
A\cdot(B\times C)=
\begin{vmatrix}
A_1 & A_2 & A_3\\
B_1 & B_2 & B_3\\
C_1 & C_2 & C_3
\end{vmatrix}
$$

> **Definition (Vector Triple Product).** If $A$, $B$ and $C$ are three vectors, then $A\times(B\times C)$ and $(A\times B)\times C$ are called vector triple products.

The expansion identity is

$$
A\times(B\times C)=(A\cdot C)B-(A\cdot B)C
$$

## 3. Key Theorems & Essential Results

> **Theorem (Commutativity of the Dot Product).** For any two vectors $A=A_1\hat{i}+A_2\hat{j}+A_3\hat{k}$ and $B=B_1\hat{i}+B_2\hat{j}+B_3\hat{k}$, we have $A\cdot B=B\cdot A$.

**Proof.** By the component definition,

$$
A\cdot B=A_1B_1+A_2B_2+A_3B_3
$$

Similarly,

$$
B\cdot A=B_1A_1+B_2A_2+B_3A_3
$$

Since multiplication of real numbers is commutative, $A_1B_1=B_1A_1$, $A_2B_2=B_2A_2$ and $A_3B_3=B_3A_3$. Hence the two sums are identical and $A\cdot B=B\cdot A$. $\blacksquare$

> **Theorem (Distributive Laws).** For vectors $A$, $B$, $C$ and scalar $m$, the following laws are valid: $A\cdot(B+C)=A\cdot B+A\cdot C$; $A\times(B+C)=A\times B+A\times C$; and $m(A\cdot B)=(mA)\cdot B=A\cdot(mB)$.

> **Theorem (Anti-commutativity of the Cross Product).** For any two vectors $A$ and $B$, we have $A\times B=-(B\times A)$.

**Proof.** Reversing the order reverses the direction of rotation, so the product vector acts in the opposite direction while retaining the same magnitude $AB\sin\theta$. Hence $B\times A=-(A\times B)$. $\blacksquare$

> **Theorem (Cosine Rule).** If $A$, $B$, $C$ are the three sides of a triangle with $\theta$ the angle between the vectors $A$ and $B$, then $C^2=A^2+B^2-2AB\cos\theta$.

**Proof.** From the triangle relation $A=B+C$, equivalently $C=A-B$. Then

$$
\begin{aligned}
C\cdot C&=(A-B)\cdot(A-B)\\
&=A\cdot A-2A\cdot B+B\cdot B
\end{aligned}
$$

Since $C\cdot C=C^2$, $A\cdot A=A^2$, $B\cdot B=B^2$ and $A\cdot B=AB\cos\theta$, we obtain

$$
C^2=A^2+B^2-2AB\cos\theta
$$

$\blacksquare$

> **Theorem (Properties of the Scalar Triple Product).** The scalar triple product satisfies: (i) $A\cdot(B\times C)=B\cdot(C\times A)=C\cdot(A\times B)$; and (ii) $A\cdot(A\times B)=0$.

**Proof of (i).** Interchanging two rows of a determinant reverses its sign, so

$$
A\cdot(B\times C)=
\begin{vmatrix}
A_1 & A_2 & A_3\\
B_1 & B_2 & B_3\\
C_1 & C_2 & C_3
\end{vmatrix}
=-\begin{vmatrix}
B_1 & B_2 & B_3\\
A_1 & A_2 & A_3\\
C_1 & C_2 & C_3
\end{vmatrix}
=B\cdot(C\times A)
$$

and the same cyclic argument gives $B\cdot(C\times A)=C\cdot(A\times B)$.

**Proof of (ii).** In the determinant

$$
A\cdot(A\times B)=
\begin{vmatrix}
A_1 & A_2 & A_3\\
A_1 & A_2 & A_3\\
B_1 & B_2 & B_3
\end{vmatrix}
$$

two rows are identical, so the determinant is zero. $\blacksquare$

> **Theorem (Volume and Coplanarity).** The scalar triple product in absolute value represents the volume of a parallelepiped with sides $A$, $B$ and $C$. The scalar triple product provides a test to show whether three given vectors lie in the same plane: the vectors are coplanar if and only if $A\cdot(B\times C)=0$.

> **Theorem (Area of a Parallelogram and Triangle).** The magnitude $\lVert A\times B\rVert$ is the area of the parallelogram with adjacent sides $A$ and $B$. The area of a triangle is half the area of a parallelogram, hence the area of a triangle is $\tfrac{1}{2}\lVert A\times B\rVert$.

> **Theorem (Non-associativity of the Cross Product).** In general $A\times(B\times C)\neq(A\times B)\times C$, so parentheses are required in $A\times B\times C$ to avoid ambiguity.

> **Theorem (Equation and Distance for a Plane).** If $A$ is a vector perpendicular to a plane and $B$ is the position vector of a point $Q$ on the plane, then for the position vector $r$ of any point $P$ on the plane, $(B-r)\cdot A=0$, equivalently $r\cdot A=B\cdot A$. The distance from the origin to the plane is the projection of $B$ on $A$, namely $B\cdot\hat{a}$ where $\hat{a}=A/\lVert A\rVert$. The distance from the point $(x_1,y_1,z_1)$ to the plane $ax+by+cz=d$ is

$$
\text{distance}=\frac{\lvert ax_1+by_1+cz_1-d\rvert}{\sqrt{a^2+b^2+c^2}}
$$

> **Theorem (Angles with the Coordinate Axes).** If $\alpha$, $\beta$, $\gamma$ are the angles that $A=A_1\hat{i}+A_2\hat{j}+A_3\hat{k}$ makes with the positive $x$, $y$, $z$ axes respectively, then

$$
\cos\alpha=\frac{A_1}{\lVert A\rVert},\qquad \cos\beta=\frac{A_2}{\lVert A\rVert},\qquad \cos\gamma=\frac{A_3}{\lVert A\rVert}
$$

## 4. Worked Exemplar Problem with Step-by-Step Solution

### 4.1 Dot Product, Angle, and Perpendicularity

**Example (Dot product and angle).** If $A=2\hat{i}+2\hat{j}-\hat{k}$ and $B=6\hat{i}-3\hat{j}+2\hat{k}$, find $A\cdot B$ and the angle between $A$ and $B$.

**Step 1 — Compute the dot product by components.**

$$
A\cdot B=(2)(6)+(2)(-3)+(-1)(2)
$$

$$
A\cdot B=12-6-2=4
$$

**Step 2 — Compute the magnitudes.**

$$
\lVert A\rVert=\sqrt{2^2+2^2+(-1)^2}=\sqrt{9}=3
$$

$$
\lVert B\rVert=\sqrt{6^2+(-3)^2+2^2}=\sqrt{49}=7
$$

**Step 3 — Use $A\cdot B=AB\cos\theta$.** Here $AB=(3)(7)=21$, so

$$
\cos\theta=\frac{4}{21}
$$

$$
\theta=\cos^{-1}\!\left(\frac{4}{21}\right)\approx 79^{\circ}
$$

**Example (Perpendicularity condition).** Determine the values of $a$ so that $A=a\hat{i}-2\hat{j}+\hat{k}$ and $B=2a\hat{i}+a\hat{j}-4\hat{k}$ are perpendicular.

**Step 1 — Set the dot product to zero.**

$$
(a)(2a)+(-2)(a)+(1)(-4)=0
$$

**Step 2 — Simplify to a quadratic.**

$$
2a^2-2a-4=0
$$

$$
a^2-a-2=0
$$

**Step 3 — Factor and solve.**

$$
(a-2)(a+1)=0
$$

$$
a=2\quad\text{or}\quad a=-1
$$

**Example (Right-angled triangle).** Show that $A=3\hat{i}-2\hat{j}+\hat{k}$, $B=\hat{i}-3\hat{j}+5\hat{k}$, $C=2\hat{i}+\hat{j}-4\hat{k}$ form a right-angled triangle.

**Step 1 — Show the vectors close into a triangle.** By trial, $A=B+C$, so the three vectors do form a triangle.

**Step 2 — Test for a right angle.** Compute

$$
A\cdot C=(3)(2)+(-2)(1)+(1)(-4)=6-2-4=0
$$

Since $A\cdot C=0$, the vectors $A$ and $C$ are perpendicular, so the triangle is right-angled.

**Example (Angles with the axes).** Find the angles that $A=3\hat{i}-6\hat{j}+2\hat{k}$ makes with the coordinate axes.

**Step 1 — Compute the magnitude.**

$$
\lVert A\rVert=\sqrt{3^2+(-6)^2+2^2}=\sqrt{49}=7
$$

**Step 2 — Apply the direction cosine formulas.**

$$
\cos\alpha=\frac{3}{7}\quad\Rightarrow\quad \alpha=\cos^{-1}\!\left(\frac{3}{7}\right)\approx 64.6^{\circ}
$$

$$
\cos\beta=\frac{-6}{7}\quad\Rightarrow\quad \beta=\cos^{-1}\!\left(-\frac{6}{7}\right)\approx 149^{\circ}
$$

$$
\cos\gamma=\frac{2}{7}\quad\Rightarrow\quad \gamma=\cos^{-1}\!\left(\frac{2}{7}\right)\approx 73.4^{\circ}
$$

**Example (Projection).** Find the projection of $A=\hat{i}-2\hat{j}+\hat{k}$ on $B=4\hat{i}-4\hat{j}+7\hat{k}$.

**Step 1 — Compute the magnitude of $B$.**

$$
\lVert B\rVert=\sqrt{4^2+(-4)^2+7^2}=\sqrt{81}=9
$$

**Step 2 — Form the unit vector.**

$$
\hat{b}=\frac{4}{9}\hat{i}-\frac{4}{9}\hat{j}+\frac{7}{9}\hat{k}
$$

**Step 3 — Project using $A\cdot\hat{b}$.**

$$
A\cdot\hat{b}=(1)\frac{4}{9}+(-2)\left(-\frac{4}{9}\right)+(1)\frac{7}{9}
$$

$$
A\cdot\hat{b}=\frac{4+8+7}{9}=\frac{19}{9}
$$

**Example (Equation of a plane and distance).** Find an equation for the plane perpendicular to $A=2\hat{i}+3\hat{j}+6\hat{k}$ and passing through the terminal point of $B=\hat{i}+5\hat{j}+3\hat{k}$, and find the distance from the origin to the plane.

**Step 1 — Use the perpendicularity condition.** Let $r$ be the position vector of a general point $P$ on the plane and $Q$ the terminal point of $B$. Since $B-r$ is perpendicular to $A$,

$$
(B-r)\cdot A=0
$$

$$
r\cdot A=B\cdot A
$$

**Step 2 — Expand in rectangular coordinates.**

$$
(x\hat{i}+y\hat{j}+z\hat{k})\cdot(2\hat{i}+3\hat{j}+6\hat{k})=(\hat{i}+5\hat{j}+3\hat{k})\cdot(2\hat{i}+3\hat{j}+6\hat{k})
$$

$$
2x+3y+6z=2+15+18
$$

$$
2x+3y+6z=35
$$

**Step 3 — Compute the distance as a projection.** The unit vector in the direction of $A$ is

$$
\hat{a}=\frac{2}{7}\hat{i}+\frac{3}{7}\hat{j}+\frac{6}{7}\hat{k}
$$

since $\lVert A\rVert=\sqrt{4+9+36}=7$. Then

$$
B\cdot\hat{a}=(1)\frac{2}{7}+(5)\frac{3}{7}+(3)\frac{6}{7}=\frac{2+15+18}{7}=5
$$

The distance from the origin to the plane is $5$.

**Example (Plane through a point perpendicular to a line).** Given $A=3\hat{i}+\hat{j}+2\hat{k}$ and $B=\hat{i}-2\hat{j}-4\hat{k}$ as position vectors of points $P$ and $Q$, find an equation for the plane passing through $Q$ and perpendicular to line $PQ$, and the distance from $(-1,1,1)$ to that plane.

**Step 1 — Find the direction vector of the line.**

$$
PQ=OQ-OP=-2\hat{i}-3\hat{j}-6\hat{k}
$$

**Step 2 — Impose perpendicularity.** For a point $R$ with position vector $r$ on the plane,

$$
QR=OR-OQ=(x-1)\hat{i}+(y+2)\hat{j}+(z+4)\hat{k}
$$

Since the plane is perpendicular to $PQ$, $PQ\cdot QR=0$:

$$
(-2\hat{i}-3\hat{j}-6\hat{k})\cdot\big[(x-1)\hat{i}+(y+2)\hat{j}+(z+4)\hat{k}\big]=0
$$

**Step 3 — Expand.**

$$
-2(x-1)-3(y+2)-6(z+4)=0
$$

$$
-2x+2-3y-6-6z-24=0
$$

$$
2x+3y+6z+28=0
$$

**Step 4 — Apply the distance formula.** With $a=2$, $b=3$, $c=6$, $d=-28$ and $(x_1,y_1,z_1)=(-1,1,1)$,

$$
\text{distance}=\frac{\lvert 2(-1)+3(1)+6(1)+28\rvert}{\sqrt{2^2+3^2+6^2}}
$$

$$
\text{distance}=\frac{\lvert -2+3+6+28\rvert}{7}=\frac{35}{7}=5
$$

### 4.2 Cross Product, Areas, and Triple Products

**Example (Area of a triangle).** Find the area of the triangle with vertices $P(1,3,2)$, $Q(2,-1,1)$, $R(-1,2,3)$.

**Step 1 — Form two side vectors.**

$$
PQ=\hat{i}-4\hat{j}-\hat{k}
$$

$$
PR=-2\hat{i}-\hat{j}+\hat{k}
$$

**Step 2 — Take the cross product.**

$$
PQ\times PR=
\begin{vmatrix}
\hat{i} & \hat{j} & \hat{k}\\
1 & -4 & -1\\
-2 & -1 & 1
\end{vmatrix}
$$

$$
PQ\times PR=\big[(-4)(1)-(-1)(-1)\big]\hat{i}-\big[(1)(1)-(-1)(-2)\big]\hat{j}+\big[(1)(-1)-(-4)(-2)\big]\hat{k}
$$

$$
PQ\times PR=(-4-1)\hat{i}-(1-2)\hat{j}+(-1-8)\hat{k}
$$

$$
PQ\times PR=-5\hat{i}+\hat{j}-9\hat{k}
$$

**Step 3 — Take the magnitude and halve it.**

$$
\lVert PQ\times PR\rVert=\sqrt{(-5)^2+1^2+(-9)^2}=\sqrt{107}
$$

$$
\text{Area}=\frac{1}{2}\sqrt{107}
$$

**Example (Scalar triple product).** Evaluate $A\cdot(B\times C)$ for $A=2\hat{i}-3\hat{j}+4\hat{k}$, $B=\hat{i}-2\hat{j}-3\hat{k}$, $C=2\hat{i}+\hat{j}+2\hat{k}$.

**Step 1 — Compute $B\times C$.**

$$
B\times C=
\begin{vmatrix}
\hat{i} & \hat{j} & \hat{k}\\
1 & -2 & -3\\
2 & 1 & 2
\end{vmatrix}
$$

$$
B\times C=\big[(-2)(2)-(-3)(1)\big]\hat{i}-\big[(1)(2)-(-3)(2)\big]\hat{j}+\big[(1)(1)-(-2)(2)\big]\hat{k}
$$

$$
B\times C=-\hat{i}-8\hat{j}+5\hat{k}
$$

**Step 2 — Dot with $A$.**

$$
A\cdot(B\times C)=(2)(-1)+(-3)(-8)+(4)(5)
$$

$$
A\cdot(B\times C)=-2+24+20=42
$$

Since the result is nonzero, the three vectors are not coplanar, and the parallelepiped with sides $A$, $B$, $C$ has volume $42$.

**Example (Non-associativity).** For $A=3\hat{i}-\hat{j}+2\hat{k}$, $B=2\hat{i}+\hat{j}-\hat{k}$, $C=\hat{i}-2\hat{j}+2\hat{k}$, compare $A\times(B\times C)$ with $(A\times B)\times C$.

**Step 1 — Compute $B\times C$.**

$$
B\times C=
\begin{vmatrix}
\hat{i} & \hat{j} & \hat{k}\\
2 & 1 & -1\\
1 & -2 & 2
\end{vmatrix}
=0\hat{i}-5\hat{j}-5\hat{k}
$$

**Step 2 — Compute $A\times(B\times C)$.**

$$
A\times(B\times C)=
\begin{vmatrix}
\hat{i} & \hat{j} &
$$

A\times(B\times C)=

$$
\begin{vmatrix}
\hat{i} & \hat{j} & \hat{k}
3 & -1 & 2
0 & -5 & -5
\end{vmatrix}
$$

A\times(B\times C)=\big[(-1)(-5)-(2)(-5)\big]\hat{i}-\big[(3)(-5)-(2)(0)\big]\hat{j}+\big[(3)(-5)-(-1)(0)\big]\hat{k}

A\times(B\times C)=15\hat{i}+15\hat{j}-15\hat{k}

$$
**Step 3 — Compute $A\times B$.**
$$

A\times B=

$$
\begin{vmatrix}
\hat{i} & \hat{j} & \hat{k}
3 & -1 & 2
2 & 1 & -1
\end{vmatrix}
$$

A\times B=\big[(-1)(-1)-(2)(1)\big]\hat{i}-\big[(3)(-1)-(2)(2)\big]\hat{j}+\big[(3)(1)-(-1)(2)\big]\hat{k}

A\times B=-\hat{i}+7\hat{j}+5\hat{k}

$$
**Step 4 — Compute $(A\times B)\times C$.**
$$

(A\times B)\times C=

$$
\begin{vmatrix}
\hat{i} & \hat{j} & \hat{k}
-1 & 7 & 5
1 & -2 & 2
\end{vmatrix}
$$

(A\times B)\times C=\big[(7)(2)-(5)(-2)\big]\hat{i}-\big[(-1)(2)-(5)(1)\big]\hat{j}+\big[(-1)(-2)-(7)(1)\big]\hat{k}

(A\times B)\times C=24\hat{i}+7\hat{j}-5\hat{k}

$$
**Step 5 — Compare.** The two results differ, so
$$

A\times(B\times C)\neq(A\times B)\times C

$$
which shows the need for parentheses in $A\times B\times C$ to avoid ambiguity.
**Example (Unit vector perpendicular to a plane).** Find a unit vector perpendicular to the plane containing $A$ and $B$.
**Step 1 — Compute the cross product $A\times B$.** This vector is perpendicular to the plane on which $A$ and $B$ lie.
**Step 2 — Normalise it.**
$$

\hat{n}=\frac{A\times B}{\lVert A\times B\rVert}

$$
The direction of $A\times B$ is fixed by the right-hand thumb rule, and the three vectors $A$, $B$, $A\times B$ form a right-handed system.
### 4.3 Examination-Style Multi-Part Question
**Question.** (a) State the distributive and commutative laws for dot and vector products. (b) Define the scalar triple product $A\cdot(B\times C)$ and the vector triple product $A\times(B\times C)$. (c) Find the area of the triangle with vertices $P(2,3,5)$, $Q(4,2,-1)$, $R(3,6,4)$.
**Part (a) — Laws.**
Dot product: $A\cdot B=B\cdot A$ (commutative) and $A\cdot(B+C)=A\cdot B+A\cdot C$ (distributive).
Vector product: $A\times B=-(B\times A)$ (anti-commutative) and $A\times(B+C)=A\times B+A\times C$ (distributive).
**Part (b) — Definitions.** The scalar triple product $A\cdot(B\times C)$ is the scalar obtained by crossing $B$ with $C$ and then dotting the result with $A$; in determinant form it equals the determinant whose rows are the components of $A$, $B$, $C$. The vector triple product $A\times(B\times C)$ is the vector obtained by crossing $B$ with $C$ and then crossing $A$ with that result; it expands as $(A\cdot C)B-(A\cdot B)C$.
**Part (c) — Area of the triangle.**
**Step 1 — Form two side vectors from $P$.**
$$

PQ=(4-2)\hat{i}+(2-3)\hat{j}+(-1-5)\hat{k}=2\hat{i}-\hat{j}-6\hat{k}

PR=(3-2)\hat{i}+(6-3)\hat{j}+(4-5)\hat{k}=\hat{i}+3\hat{j}-\hat{k}

$$
**Step 2 — Take the cross product.**
$$

PQ\times PR=

$$
\begin{vmatrix}
\hat{i} & \hat{j} & \hat{k}
2 & -1 & -6
1 & 3 & -1
\end{vmatrix}
$$

PQ\times PR=\big[(-1)(-1)-(-6)(3)\big]\hat{i}-\big[(2)(-1)-(-6)(1)\big]\hat{j}+\big[(2)(3)-(-1)(1)\big]\hat{k}

PQ\times PR=(1+18)\hat{i}-(-2+6)\hat{j}+(6+1)\hat{k}

PQ\times PR=19\hat{i}-4\hat{j}+7\hat{k}

$$
**Step 3 — Take the magnitude and halve it.**
$$

\lVert PQ\times PR\rVert=\sqrt{19^2+(-4)^2+7^2}=\sqrt{361+16+49}=\sqrt{426}

Area=\frac{1}{2}\sqrt{426}

$$
## 5. High-Yield Exam Takeaways & Common Pitfalls
### 5.1 Lesson Learning Outcomes as Exam Targets
The stated outcomes of this unit are: determine the dot and cross product; determine a vector perpendicular to a plane; and evaluate scalar triple and vector triple products. Every examination question in this topic maps onto one of these three verbs, so treat them as a checklist.
- **"Determine the dot and cross product"** signals a computation question: component expansion, angle between vectors, perpendicularity condition, projection, or area.
- **"Determine a vector perpendicular to a plane"** signals a normalisation question: compute $A\times B$, then divide by its magnitude.
- **"Evaluate scalar triple and vector triple products"** signals a determinant question, often combined with a coplanarity or volume interpretation.
### 5.2 Magnitude, Unit Vector and Resultant — The Recurring Toolkit
Almost every multi-mark question in this topic is assembled from four primitive operations. Master them as reflexes.
| Operation | Formula | Typical use |
| --- | --- | --- |
| Magnitude | $\lVert A\rVert=\sqrt{A_1^2+A_2^2+A_3^2}$ | denominator in every angle or projection |
| Unit vector | $\hat{a}=A/\lVert A\rVert$ | projection, perpendicular direction, distance to plane |
| Resultant | $R=A+B$ componentwise | forming side vectors $PQ=OQ-OP$ |
| Angle | $\cos\theta=\dfrac{A\cdot B}{\lVert A\rVert\lVert B\rVert}$ | angle between vectors, direction cosines |
The single most common source of lost marks is a wrong magnitude. Compute $\lVert A\rVert$ and $\lVert B\rVert$ explicitly and write them down before substituting into the cosine formula.
### 5.3 High-Frequency Question Patterns
- **Commutativity proof (short-mark question).** Write both vectors in component form, expand both dot products, invoke commutativity of real multiplication, conclude. Do not attempt a geometric argument when the question supplies components; the marking scheme expects the component proof.
- **Perpendicularity with an unknown parameter.** Set the dot product to zero, simplify to a quadratic, factor, and state both roots. Omitting one root is a standard error.
- **Right-angled triangle verification.** Two separate marks are usually available: one for showing the vectors close into a triangle (sum of two equals the third, or total sum zero), one for showing a dot product vanishes.
- **Direction cosines.** Always divide each component by the full magnitude, and keep the sign of the component. A negative cosine correctly yields an obtuse angle.
- **Projection.** Project onto the unit vector, not onto the raw vector. The answer is a scalar, not a vector.
- **Plane equation.** Use $r\cdot A=B\cdot A$ when a normal and a point are given; use $PQ\cdot QR=0$ when the plane is perpendicular to a line through two given points.
- **Distance to a plane.** Substitute into $\lvert ax_1+by_1+cz_1-d\rvert/\sqrt{a^2+b^2+c^2}$ with the plane first written in the form $ax+by+cz=d$. Sign errors inside the absolute value are the usual failure point.
- **Area of a triangle.** Form two side vectors from a common vertex, cross them, take the magnitude, then halve. Forgetting the factor $\tfrac{1}{2}$ is the most frequent single-mark loss in the whole topic.
- **Scalar triple product.** Evaluate as a $3\times3$ determinant; interpret a zero result as coplanarity and a nonzero result as the parallelepiped volume.
- **Vector triple product.** Expand with $(A\cdot C)B-(A\cdot B)C$ rather than computing two cross products in sequence, and always retain parentheses.
### 5.4 Common Pitfalls and Traps
- **Confusing the two products.** The dot product returns a scalar; the cross product returns a vector. A scalar answer to an area question, or a vector answer to an angle question, is automatically wrong.
- **Dropping the minus signs in the cross product.** The middle component of the determinant carries a minus sign: $-(A_1B_3-A_3B_1)$. Recompute the middle term separately.
- **Assuming commutativity for the cross product.** $A\times B=-(B\times A)$; reversing order flips the direction.
- **Assuming associativity.** $A\times(B\times C)\neq(A\times B)\times C$ in general; the worked comparison above shows the two results differ.
- **Using $\cos$ where $\sin$ belongs.** The dot product uses $\cos\theta$; the cross product magnitude uses $\sin\theta$. Mixing them inverts every parallel/perpendicular conclusion.
- **Forgetting that parallel vectors give a zero cross product.** A zero cross product is a valid and often expected answer; do not treat it as an error.
- **Sign slips in the distance formula.** Write the plane as $ax+by+cz-d=0$ consistently before substituting the point.
- **Leaving the angle in the wrong form.** State both the exact value, such as $\cos^{-1}(4/21)$, and the approximate degree value when the question asks for an angle.
### 5.5 Answer Structure and Marking Rubric Tips
- **Show the component setup.** Examiners award method marks for writing $A=A_1\hat{i}+A_2\hat{j}+A_3\hat{k}$ and $B=B_1\hat{i}+B_2\hat{j}+B_3\hat{k}$ before any computation.
- **One line per logical step.** Compute the dot product, then the magnitudes, then the cosine, then the angle. Each line is a potential mark.
- **State the geometric conclusion in words.** After obtaining $A\cdot C=0$, write explicitly that $A$ and $C$ are perpendicular and hence the triangle is right-angled. The conclusion carries marks independently of the arithmetic.
- **Label determinant expansions.** Write the determinant, then the cofactor expansion, then the simplified vector. Do not collapse these into one line.
- **Carry exact surds to the end.** Keep $\sqrt{107}$ or $\sqrt{426}$ in the final area answer; premature decimal rounding loses accuracy marks.
- **Verify with a second method where cheap.** For a triangle, confirm closure by checking that the three vectors sum to zero; for a triple product, confirm the cyclic permutation gives the same value.
### 5.6 Time-Management Strategy
- **Short-mark proofs first.** The commutativity proof and the statement of distributive and commutative laws are fast, high-certainty marks. Secure them before attempting long computations.
- **Budget the determinant questions.** A cross product determinant takes roughly two minutes; a triple product roughly three. If a multi-part question carries seven marks for an area, allocate proportionally more time there.
- **Park the distance-to-plane part.** It is a single substitution once the plane equation is correct, so complete the plane equation first and return to the distance.
- **Check units of the answer type before moving on.** Scalar for dot product, vector for cross product, scalar for area and volume, angle in degrees or radians as requested.
### 5.7 Consolidated Formula Sheet
$$

A\cdot B=AB\cos\theta=A_1B_1+A_2B_2+A_3B_3

\lVert A\rVert=\sqrt{A_1^2+A_2^2+A_3^2},\qquad \hat{a}=\frac{A}{\lVert A\rVert}

\cos\theta=\frac{A\cdot B}{\lVert A\rVert\,\lVert B\rVert}

projection of A on B=A\cdot\hat{b}

A\times B=

$$
\begin{vmatrix}
\hat{i} & \hat{j} & \hat{k}
A_1 & A_2 & A_3
B_1 & B_2 & B_3
\end{vmatrix}
$$,
\qquad \lVert A\times B\rVert=AB\sin\theta

Area of parallelogram=\lVert A\times B\rVert,\qquad Area of triangle=\frac{1}{2}\lVert A\times B\rVert

A\cdot(B\times C)=

$$
\begin{vmatrix}
A_1 & A_2 & A_3
B_1 & B_2 & B_3
C_1 & C_2 & C_3
\end{vmatrix}
$$

A\times(B\times C)=(A\cdot C)B-(A\cdot B)C

Plane: r\cdot A=B\cdot A,\qquad distance=\frac{\lvert ax_1+by_1+cz_1-d\rvert}{\sqrt{a^2+b^2+c^2}}

$$
### 5.8 Assessment Practice Set
Work these under timed conditions; each mirrors a pattern already established above.
- Prove that $A\cdot B=B\cdot A$ for $A=(A_1,A_2,A_3)$ and $B=(B_1,B_2,B_3)$.
- Find the angle between $\hat{i}+\hat{j}$ and $\hat{i}-\hat{j}+\hat{k}$.
- Find the projection of $\hat{i}-2\hat{j}+\hat{k}$ on $4\hat{i}-4\hat{j}+7\hat{k}$.
- Find the area of the triangle with vertices $(2,3,5)$, $(4,2,-1)$, $(3,6,4)$.
- Determine the value of $a$ for which $a\hat{i}-2\hat{j}+\hat{k}$ and $2a\hat{i}+a\hat{j}-4\hat{k}$ are perpendicular.
- State the distributive and commutative laws for dot and vector products, and define $A\cdot(B\times C)$ and $A\times(B\times C)$.
- Find the equation of the plane perpendicular to $2\hat{i}+3\hat{j}+6\hat{k}$ through the terminal point of $\hat{i}+5\hat{j}+3\hat{k}$, and its distance from the origin.
### 5.9 Recommended Reading
The following standard references support this unit and are appropriate for further worked examples and exercises: Davis, H.; Lewis, P.; Spiegel, M.; and Tai, C. Consult them for additional determinant expansions, triple-product identities, and geometric applications beyond the worked set above.
$$