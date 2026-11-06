## 1. Core Concept Overview & Intuition

The algebra of vectors admits two distinct multiplicative operations. The first, the **dot (scalar) product**, consumes two vectors and returns a single real number. The second, the **cross (vector) product**, consumes two vectors and returns a third vector. These two products are the analytical engine for measuring lengths, angles, projections, areas, volumes, perpendicularity, coplanarity, and the geometry of planes and triangles in three-dimensional space.

The intuition behind the dot product is **projection**. When two vectors are placed tail-to-tail, the component of one vector lying along the direction of the other is obtained by multiplying its length by the cosine of the included angle. The dot product is precisely the product of one vector's magnitude with the signed projection of the other onto it. Consequently, the dot product is largest (equal to the product of magnitudes) when the vectors are parallel, and it vanishes when they are perpendicular, because a perpendicular vector casts no shadow along the other's direction.

The intuition behind the cross product is **area and orientation**. Two non-parallel vectors span a parallelogram; the cross product has magnitude equal to the area of that parallelogram and direction normal (perpendicular) to the plane containing the two vectors. The sense of that normal is fixed by the right-hand rule: if the fingers of the right hand curl from the first vector toward the second, the thumb points along the product vector. This orientation dependence is why the cross product is **anti-commutative**: reversing the order of the factors reverses the normal.

Both products are built from the same geometric data — the magnitudes of the two vectors and the angle between them — but they respond to that angle in complementary ways: the dot product tracks $\cos\theta$ and the cross product tracks $\sin\theta$. Because $\cos^2\theta+\sin^2\theta=1$, the two products together encode the full geometry of a pair of vectors.![the two vectors are orthogonal or perpendicular to one another.](/cdn/cloudflare/prep/visual-crops/2026/10/document-d0c6c84b-5e48-4773-a688-196f76ad7045-page-22-830af1aa.jpg)

## 2. Mathematical Formalization & Core Definitions

### 2.1 The Dot (Scalar) Product

> **Definition (Dot Product).** If $A$ and $B$ are two vectors, the scalar product of $A$ and $B$ is defined as $AB\cos\theta$, where $A$ and $B$ are the magnitudes of the vectors $A$ and $B$, and $\theta$ is the angle between them. The scalar (dot) product is denoted $A\cdot B$.

Thus



$$
A\cdot B=AB\cos\theta
$$



and this quantity equals either $A$ times the projection of $B$ on $A$, or $B$ times the projection of $A$ on $B$. In either case the result is a scalar quantity.

**Geometric reading of the definition.** Consider two position vectors drawn from a common origin $O$, with $OA=7$ units and $OB=5$ units and an included angle of $45^{\circ}$. Then



$$
OA\cdot OB=OA\cdot OB\cos\theta=7\cdot 5\cos 45^{\circ}=35.2
$$



to three significant figures. The product is a pure number carrying the units of the product of the two lengths.

**Special angles.** The definition immediately yields three structural facts.

- If $\theta=90^{\circ}$, then $a\cdot b=ab\cos 90^{\circ}=ab\cdot 0=0$. The scalar product of any two vectors at right angles is always zero, and the vectors are said to be **orthogonal** or **perpendicular**.

- If the two vectors point in the same direction, then $\theta=0^{\circ}$ and $a\cdot b=ab\cos 0^{\circ}=ab$.
- If the two vectors point in opposite directions, then $\theta=180^{\circ}$ and $a\cdot b=-ab$.

### 2.2 The Dot Product in Component Form

Write the two vectors in component form as



$$
A=A_1\hat{i}+A_2\hat{j}+A_3\hat{k}
$$





$$
B=B_1\hat{i}+B_2\hat{j}+B_3\hat{k}
$$



Expanding the product bilinearly gives nine elementary products:



$$
\begin{aligned}
A\cdot B={}&A_1B_1\,\hat{i}\cdot\hat{i}+A_1B_2\,\hat{i}\cdot\hat{j}+A_1B_3\,\hat{i}\cdot\hat{k}\\
&+A_2B_1\,\hat{j}\cdot\hat{i}+A_2B_2\,\hat{j}\cdot\hat{j}+A_2B_3\,\hat{j}\cdot\hat{k}\\
&+A_3B_1\,\hat{k}\cdot\hat{i}+A_3B_2\,\hat{k}\cdot\hat{j}+A_3B_3\,\hat{k}\cdot\hat{k}
\end{aligned}
$$



Now $\hat{i}\cdot\hat{i}=\hat{j}\cdot\hat{j}=\hat{k}\cdot\hat{k}=1\cdot 1\cos 0^{\circ}=1$, while $\hat{i}\cdot\hat{j}=\hat{i}\cdot\hat{k}=\hat{j}\cdot\hat{k}=1\cdot 1\cos 90^{\circ}=0$. The six cross terms vanish and we are left with



$$
A\cdot B=A_1B_1+A_2B_2+A_3B_3
$$



This is the working formula for every dot-product computation.

### 2.3 The Cross (Vector) Product

> **Definition (Cross Product).** The cross or vector product of $A$ and $B$, written $A\times B$ and read " $A$ cross $B$ ", is defined as a vector having magnitude $AB\sin\theta$, where $\theta$ is the angle between the two vectors. The product vector acts in a direction perpendicular to $A$ and $B$ in such a sense that $A$, $B$, and $(A\times B)$ form a right-handed system in that order.

Thus



$$
\lvert A\times B\rvert=AB\sin\theta
$$



**Right-handed axes.** For vectors in space, axes of reference are normally defined by the right-hand rule. The axes $OX$, $OY$, $OZ$ form a right-handed set if rotation from $OX$ to $OY$ takes a right-handed corkscrew action along the positive direction of $OZ$; similarly, rotation from $OY$ to $OZ$ gives right-hand corkscrew action along the positive direction of $OX$, and so on cyclically.

**Anti-commutativity.** The product $B\times A$ reverses the direction of rotation, so the product vector acts downward; hence



$$
B\times A=-(A\times B)
$$



**Special angles.** If $\theta=0^{\circ}$, then $A\times B=AB\sin 0^{\circ}=0$, so parallel vectors have zero cross product. If $\theta=90^{\circ}$, then $A\times B=AB\sin 90^{\circ}=AB$, so the magnitude is maximal for perpendicular vectors.

### 2.4 The Cross Product in Component Form

Expanding bilinearly as before,



$$
\begin{aligned}
A\times B={}&A_1B_1\,\hat{i}\times\hat{i}+A_1B_2\,\hat{i}\times\hat{j}+A_1B_3\,\hat{i}\times\hat{k}\\
&+A_2B_1\,\hat{j}\times\hat{i}+A_2B_2\,\hat{j}\times\hat{j}+A_2B_3\,\hat{j}\times\hat{k}\\
&+A_3B_1\,\hat{k}\times\hat{i}+A_3B_2\,\hat{k}\times\hat{j}+A_3B_3\,\hat{k}\times\hat{k}
\end{aligned}
$$



Since $\hat{i}\times\hat{i}=1\cdot 1\sin 0^{\circ}=0$, we have $\hat{i}\times\hat{i}=\hat{j}\times\hat{j}=\hat{k}\times\hat{k}=0$. Also $\hat{i}\times\hat{j}=1\cdot 1\sin 90^{\circ}=1$ in the direction $OZ$, that is $\hat{i}\times\hat{j}=\hat{k}$. The complete multiplication table of the basis vectors is



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



which is recognized as the expansion of the determinant



$$
A\times B=
\begin{vmatrix}
\hat{i} & \hat{j} & \hat{k}\\
A_1 & A_2 & A_3\\
B_1 & B_2 & B_3
\end{vmatrix}
$$



The determinant form is the standard computational device: expand along the first row, remembering the alternating signs $+,-,+$.

## 3. Key Theorems & Essential Results

> **Theorem (Commutativity of the Dot Product).** For any two vectors $A=A_1\hat{i}+A_2\hat{j}+A_3\hat{k}$ and $B=B_1\hat{i}+B_2\hat{j}+B_3\hat{k}$, we have $A\cdot B=B\cdot A$.

*Proof.* By the component definition,



$$
A\cdot B=A_1B_1+A_2B_2+A_3B_3
$$



and similarly



$$
B\cdot A=B_1A_1+B_2A_2+B_3A_3
$$



Since multiplication of real numbers is commutative, $A_iB_i=B_iA_i$ for each $i=1,2,3$, hence the two sums are identical and $A\cdot B=B\cdot A$. $\blacksquare$

> **Theorem (Distributive Laws).** For vectors $A$, $B$, $C$ and scalar $\lambda$: $A\cdot(B+C)=A\cdot B+A\cdot C$; $A\times(B+C)=A\times B+A\times C$; and $\lambda(A\cdot B)=(\lambda A)\cdot B=A\cdot(\lambda B)$.

These follow by expanding both sides in components and regrouping terms.

> **Theorem (Cosine Rule).** If $A$, $B$, $C$ are the three sides of a triangle and $\theta$ is the angle between the vectors $A$ and $B$, then $C^2=A^2+B^2-2AB\cos\theta$.

*Proof.* From the vector triangle, $A=B+C$, equivalently $C=A-B$. Then



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



which is the cosine rule for plane triangles. $\blacksquare$

> **Theorem (Equation of a Plane).** The plane perpendicular to a vector $A$ and passing through the terminal point of a position vector $B$ consists of all points with position vector $r$ satisfying $(B-r)\cdot A=0$, equivalently $r\cdot A=B\cdot A$.

> **Theorem (Distance from a Point to a Plane).** The distance from the point $(x_1,y_1,z_1)$ to the plane $ax+by+cz=d$ is



$$
\text{distance}=\frac{ax_1+by_1+cz_1-d}{\sqrt{a^2+b^2+c^2}}
$$



## 4. Worked Exemplar Problem with Step-by-Step Solution

**Problem.** For the vectors $A=2\hat{i}+2\hat{j}-\hat{k}$ and $B=6\hat{i}-3\hat{j}+2\hat{k}$:

(a) compute $A\cdot B$ and hence the angle between them;

(b) find a unit vector perpendicular to the plane containing $A$ and $B$;

(c) find the area of the parallelogram with adjacent sides $A$ and $B$.

**Solution.**

**(a) Dot product and angle.** By the component formula,



$$
A\cdot B=(2)(6)+(2)(-3)+(-1)(2)=12-6-2=4
$$



The magnitudes are



$$
\lvert A\rvert=\sqrt{2^2+2^2+(-1)^2}=\sqrt{9}=3
$$





$$
\lvert B\rvert=\sqrt{6^2+(-3)^2+2^2}=\sqrt{49}=7
$$



Hence



$$
\cos\theta=\frac{A\cdot B}{\lvert A\rvert\lvert B\rvert}=\frac{4}{21}
$$



so



$$
\theta=\cos^{-1}\!\left(\frac{4}{21}\right)\approx 79^{\circ}
$$



**(b) Unit normal to the plane.** The vector $A\times B$ is perpendicular to both $A$ and $B$, hence normal to the plane they span. Expanding the determinant,



$$
A\times B=
\begin{vmatrix}
\hat{i} & \hat{j} & \hat{k}\\
2 & 2 & -1\\
6 & -3 & 2
\end{vmatrix}
$$





$$
=\big((2)(2)-(-1)(-3)\big)\hat{i}-\big((2)(2)-(-1)(6)\big)\hat{j}+\big((2)(-3)-(2)(6)\big)\hat{k}
$$





$$
A\times B=\hat{i}-10\hat{j}-18\hat{k}
$$



Its magnitude is



$$
\lvert A\times B\rvert=\sqrt{1^2+(-10)^2+(-18)^2}=\sqrt{1+100+324}=\sqrt{425}=5\sqrt{17}
$$



so the required unit vector is



$$
\hat{n}=\frac{1}{5\sqrt{17}}\big(\hat{i}-10\hat{j}-18\hat{k}\big)
$$



and its negative is the equally valid unit normal in the opposite sense.

**(c) Area of the parallelogram.** The area of the parallelogram with adjacent sides $A$ and $B$ is the magnitude of their cross product, already computed in part (b):



$$
\text{Area}=\lvert A\times B\rvert=5\sqrt{17}\approx 20.6
$$



## 5. Common Pitfalls & Exam Strategy

**Dot versus cross: which product answers which question.** The dot product returns a scalar and is the tool for angles, projections, orthogonality tests and plane equations. The cross product returns a vector and is the tool for perpendicular directions, areas and the orientation of a plane. A frequent error is to reach for the cross product when only an angle is wanted, or to reach for the dot product when a normal direction is required. Decide first whether the answer must be a number or a vector.

**Sign discipline in the determinant expansion.** The middle term of the determinant expansion carries a minus sign:



$$
A\times B=(A_2B_3-A_3B_2)\hat{i}-(A_1B_3-A_3B_1)\hat{j}+(A_1B_2-A_2B_1)\hat{k}
$$



Dropping this minus sign is the single most common computational slip. A reliable safeguard is to check the result against the basis table: for $A=\hat{i}$ and $B=\hat{j}$ the formula must return $\hat{k}$, and for $A=\hat{j}$ and $B=\hat{i}$ it must return $-\hat{k}$.

**Order matters in the cross product.** Because $B\times A=-(A\times B)$, the order of the factors fixes the sense of the normal. When a problem asks for "the" unit normal, state that either sign is acceptable, or choose the sign dictated by the geometry of the question.

**Zero products carry information.** A vanishing dot product certifies perpendicularity; a vanishing cross product certifies parallelism, since $\lvert A\times B\rvert=AB\sin\theta$ vanishes exactly when $\theta=0^{\circ}$ or $\theta=180^{\circ}$. In a right-angled-triangle problem, computing the three pairwise dot products and finding one of them zero is a complete and rigorous proof of the right angle.

**Angles with the coordinate axes.** The angle $\alpha$ that $A$ makes with the positive $x$-axis is obtained from $A\cdot\hat{i}=A\cos\alpha$, so $\cos\alpha=A_1/\lvert A\rvert$; the other two angles follow by cyclic replacement of the component. Always divide by the full magnitude $\lvert A\rvert$, not by a single component, and expect an obtuse angle whenever the corresponding component is negative.

**Projections.** The projection of $A$ on $B$ is $A\cdot\hat{b}$, where $\hat{b}=B/\lvert B\rvert$ is the unit vector along $B$. Forgetting to normalize $B$ produces $A\cdot B$, which is the projection scaled by $\lvert B\rvert$ and is dimensionally wrong for a length.

**Planes and distances.** For a plane through the terminal point of $B$ with normal $A$, the equation is $r\cdot A=B\cdot A$; in coordinates this reads $A_1x+A_2y+A_3z=A_1B_1+A_2B_2+A_3B_3$. The distance from the origin to that plane is the projection of $B$ on the unit normal, namely $B\cdot A/\lvert A\rvert$. When applying the point-to-plane distance formula, substitute the coordinates with their signs intact and divide by $\sqrt{a^2+b^2+c^2}$, the magnitude of the normal vector.

**Checking magnitudes.** A quick sanity check on any cross product is the identity $\lvert A\times B\rvert^2=\lvert A\rvert^2\lvert B\rvert^2-(A\cdot B)^2$, which follows from $\sin^2\theta+\cos^2\theta=1$. If the computed cross product and the computed dot product fail this relation, an arithmetic error has occurred.