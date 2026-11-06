## 1. Core Concept Overview & Intuition

The algebra of vectors admits two distinct multiplicative operations. The first combines two vectors to produce a single real number, and is therefore called the **dot product** or **scalar product**. The second combines two vectors to produce a new vector, and is therefore called the **cross product** or **vector product**. Both operations encode geometric information about the pair of vectors: the dot product measures the extent to which two vectors point along one another, while the cross product measures the extent to which they fail to be parallel and records the orientation of the plane they span.

The central intuition for the dot product is **projection**. If $\mathbf{A}$ and $\mathbf{B}$ are vectors with magnitudes $A$ and $B$ and $\theta$ is the angle between them, then $B\cos\theta$ is the signed length of the shadow that $\mathbf{B}$ casts on the line of $\mathbf{A}$. Multiplying this shadow length by $A$ gives the scalar $AB\cos\theta$. Equivalently, one may project $\mathbf{A}$ onto $\mathbf{B}$ and multiply by $B$. The result is the same scalar either way, and this symmetry is the defining feature of the operation.

The central intuition for the cross product is **perpendicularity and orientation**. The magnitude $AB\sin\theta$ is the area of the parallelogram whose adjacent sides are $\mathbf{A}$ and $\mathbf{B}$. The direction of $\mathbf{A}\times\mathbf{B}$ is perpendicular to both factors, and the sense of that direction is fixed by the right-hand rule: if the fingers of the right hand curl from $\mathbf{A}$ toward $\mathbf{B}$, the thumb points along $\mathbf{A}\times\mathbf{B}$. Reversing the order of the factors reverses the sense of rotation, so the product vector points the opposite way. This is the geometric origin of the anti-commutative law $\mathbf{B}\times\mathbf{A}=-(\mathbf{A}\times\mathbf{B})$.

A coordinate frame $\mathrm{OX}$, $\mathrm{OY}$, $\mathrm{OZ}$ is called a **right-handed set** when a rotation from $\mathrm{OX}$ to $\mathrm{OY}$ corresponds to the advance of a right-handed corkscrew along the positive direction of $\mathrm{OZ}$; similarly, a rotation from $\mathrm{OY}$ to $\mathrm{OZ}$ corresponds to a right-handed corkscrew advance along the positive direction of $\mathrm{OX}$, and so on cyclically. All component formulas below presuppose such a frame.

The two products interact with the angle between vectors in complementary ways. When two vectors are parallel, the dot product is maximal and the cross product vanishes. When two vectors are perpendicular, the dot product vanishes and the cross product is maximal. These two extreme cases are the most frequently tested facts in the entire topic, and they supply the standard tests for orthogonality and parallelism.![action along the positive direction of OZ.](/cdn/cloudflare/prep/visual-crops/2026/10/document-d0c6c84b-5e48-4773-a688-196f76ad7045-page-27-fdf224e7.jpg)

## 2. Mathematical Formalization & Core Definitions

### 2.1 The Dot or Scalar Product

> **Definition (Dot Product).** If $\mathbf{A}$ and $\mathbf{B}$ are two vectors, the scalar product of $\mathbf{A}$ and $\mathbf{B}$ is defined as $AB\cos\theta$, where $A$ and $B$ are the magnitudes of $\mathbf{A}$ and $\mathbf{B}$ respectively, and $\theta$ is the angle between them. The scalar product is denoted $\mathbf{A}\cdot\mathbf{B}$.

Thus



$$
\mathbf{A}\cdot\mathbf{B}=AB\cos\theta
$$



with the equivalent projection interpretation



$$
\mathbf{A}\cdot\mathbf{B}=A\times(\text{projection of } \mathbf{B} \text{ on } \mathbf{A})=B\times(\text{projection of } \mathbf{A} \text{ on } \mathbf{B})
$$



and in either case the result is a scalar quantity.

The magnitude of a vector $\mathbf{A}=A_1\hat{\imath}+A_2\hat{\jmath}+A_3\hat{k}$ is obtained from the dot product of the vector with itself, since the angle between a vector and itself is zero:



$$
A=\lVert\mathbf{A}\rVert=\sqrt{A_1^2+A_2^2+A_3^2}
$$



The **unit vector** in the direction of $\mathbf{A}$ is the vector of unit magnitude parallel to $\mathbf{A}$, namely



$$
\hat{a}=\frac{\mathbf{A}}{A}=\frac{\mathbf{A}}{\sqrt{A_1^2+A_2^2+A_3^2}}
$$



The **resultant** of two vectors is their vector sum, and its magnitude is recovered from the dot product of the resultant with itself, which produces the cosine rule derived in Section 3.

### 2.2 Special Angles

When the two vectors are at right angles, $\theta=90^{\circ}$ and



$$
\mathbf{a}\cdot\mathbf{b}=ab\cos 90^{\circ}=ab\cdot 0=0
$$



so the scalar product of any two vectors at right angles to each other is always zero, and the two vectors are said to be **orthogonal** or **perpendicular**.

When the two vectors point in the same direction, $\theta=0^{\circ}$ and



$$
\mathbf{a}\cdot\mathbf{b}=ab\cos 0^{\circ}=ab
$$



so the dot product equals the product of the magnitudes.

### 2.3 Component Form of the Dot Product

Write the two vectors in component form as



$$
\mathbf{A}=A_1\hat{\imath}+A_2\hat{\jmath}+A_3\hat{k}
$$





$$
\mathbf{B}=B_1\hat{\imath}+B_2\hat{\jmath}+B_3\hat{k}
$$



Expanding the product term by term gives



$$
\begin{aligned}
\mathbf{A}\cdot\mathbf{B}={}&A_1B_1\,\hat{\imath}\cdot\hat{\imath}+A_1B_2\,\hat{\imath}\cdot\hat{\jmath}+A_1B_3\,\hat{\imath}\cdot\hat{k}\\
&+A_2B_1\,\hat{\jmath}\cdot\hat{\imath}+A_2B_2\,\hat{\jmath}\cdot\hat{\jmath}+A_2B_3\,\hat{\jmath}\cdot\hat{k}\\
&+A_3B_1\,\hat{k}\cdot\hat{\imath}+A_3B_2\,\hat{k}\cdot\hat{\jmath}+A_3B_3\,\hat{k}\cdot\hat{k}
\end{aligned}
$$



Now the parallel basis products satisfy



$$
\hat{\imath}\cdot\hat{\imath}=\hat{\jmath}\cdot\hat{\jmath}=\hat{k}\cdot\hat{k}=1\cdot 1\cos 0^{\circ}=1
$$



and the mixed basis products satisfy



$$
\hat{\imath}\cdot\hat{\jmath}=\hat{\imath}\cdot\hat{k}=\hat{\jmath}\cdot\hat{k}=1\cdot 1\cos 90^{\circ}=0
$$



so all cross terms vanish and one is left with



$$
\mathbf{A}\cdot\mathbf{B}=A_1B_1+A_2B_2+A_3B_3
$$



This is the computational workhorse of the topic: the scalar product is the sum of the products of corresponding components.

### 2.4 The Cross or Vector Product

> **Definition (Cross Product).** The cross or vector product of $\mathbf{A}$ and $\mathbf{B}$, written $\mathbf{A}\times\mathbf{B}$ and read "$\mathbf{A}$ cross $\mathbf{B}$", is defined as a vector having magnitude $AB\sin\theta$, where $\theta$ is the angle between the two vectors. The product vector acts in a direction perpendicular to $\mathbf{A}$ and $\mathbf{B}$ in such a sense that $\mathbf{A}$, $\mathbf{B}$ and $(\mathbf{A}\times\mathbf{B})$ form a right-handed system in that order.

Thus



$$
\lVert\mathbf{A}\times\mathbf{B}\rVert=AB\sin\theta
$$



Reversing the order reverses the direction of rotation, and the product vector acts downward, so that



$$
\mathbf{B}\times\mathbf{A}=-(\mathbf{A}\times\mathbf{B})
$$



If $\theta=0^{\circ}$, then $\mathbf{A}\times\mathbf{B}=AB\sin 0^{\circ}=0$, and if $\theta=90^{\circ}$, then $\mathbf{A}\times\mathbf{B}=AB\sin 90^{\circ}=AB$.

### 2.5 Component Form of the Cross Product

With $\mathbf{A}=A_1\hat{\imath}+A_2\hat{\jmath}+A_3\hat{k}$ and $\mathbf{B}=B_1\hat{\imath}+B_2\hat{\jmath}+B_3\hat{k}$, expanding term by term gives



$$
\begin{aligned}
\mathbf{A}\times\mathbf{B}={}&A_1B_1\,\hat{\imath}\times\hat{\imath}+A_1B_2\,\hat{\imath}\times\hat{\jmath}+A_1B_3\,\hat{\imath}\times\hat{k}\\
&+A_2B_1\,\hat{\jmath}\times\hat{\imath}+A_2B_2\,\hat{\jmath}\times\hat{\jmath}+A_2B_3\,\hat{\jmath}\times\hat{k}\\
&+A_3B_1\,\hat{k}\times\hat{\imath}+A_3B_2\,\hat{k}\times\hat{\jmath}+A_3B_3\,\hat{k}\times\hat{k}
\end{aligned}
$$



Since $\hat{\imath}\times\hat{\imath}=1\cdot 1\cdot\sin 0^{\circ}=0$, the parallel products vanish:



$$
\hat{\imath}\times\hat{\imath}=\hat{\jmath}\times\hat{\jmath}=\hat{k}\times\hat{k}=0
$$



Also $\hat{\imath}\times\hat{\jmath}=1\cdot 1\cdot\sin 90^{\circ}=1$ in the direction $\mathrm{OZ}$, that is $\hat{\imath}\times\hat{\jmath}=\hat{k}$. The complete cyclic table of basis products is



$$
\hat{\imath}\times\hat{\jmath}=\hat{k},\qquad \hat{\jmath}\times\hat{k}=\hat{\imath},\qquad \hat{k}\times\hat{\imath}=\hat{\jmath}
$$





$$
\hat{\jmath}\times\hat{\imath}=-\hat{k},\qquad \hat{k}\times\hat{\jmath}=-\hat{\imath},\qquad \hat{\imath}\times\hat{k}=-\hat{\jmath}
$$



Collecting terms yields



$$
\mathbf{A}\times\mathbf{B}=(A_2B_3-A_3B_2)\hat{\imath}+(A_3B_1-A_1B_3)\hat{\jmath}+(A_1B_2-A_2B_1)\hat{k}
$$



which is recognized as the expansion of the determinant



$$
\mathbf{A}\times\mathbf{B}=
\begin{vmatrix}
\hat{\imath} & \hat{\jmath} & \hat{k}\\
A_1 & A_2 & A_3\\
B_1 & B_2 & B_3
\end{vmatrix}
$$



The determinant form is the standard computational device: expand along the first row, remembering that the middle term carries a negative sign.

### 2.6 Vector Perpendicular to a Plane

The vector $\mathbf{A}\times\mathbf{B}$ is perpendicular to the plane on which the vectors $\mathbf{A}$ and $\mathbf{B}$ lie, and the three vectors form a right-handed system. The right-hand thumb rule determines the direction of the perpendicular. To obtain the **unit vector perpendicular to the plane**, one normalizes:



$$
\hat{n}=\frac{\mathbf{A}\times\mathbf{B}}{\lVert\mathbf{A}\times\mathbf{B}\rVert}
$$



### 2.7 Triple Products

> **Definition (Scalar Triple Product).** If $\mathbf{A}$, $\mathbf{B}$, $\mathbf{C}$ are three vectors, the scalar formed by the product $\mathbf{A}\cdot(\mathbf{B}\times\mathbf{C})$ is called the scalar triple product.

For $\mathbf{A}=A_1\hat{\imath}+A_2\hat{\jmath}+A_3\hat{k}$, $\mathbf{B}=B_1\hat{\imath}+B_2\hat{\jmath}+B_3\hat{k}$ and $\mathbf{C}=C_1\hat{\imath}+C_2\hat{\jmath}+C_3\hat{k}$,



$$
\mathbf{A}\cdot(\mathbf{B}\times\mathbf{C})=
\begin{vmatrix}
A_1 & A_2 & A_3\\
B_1 & B_2 & B_3\\
C_1 & C_2 & C_3
\end{vmatrix}
$$



> **Definition (Vector Triple Product).** If $\mathbf{A}$, $\mathbf{B}$ and $\mathbf{C}$ are three vectors, then $\mathbf{A}\times(\mathbf{B}\times\mathbf{C})$ and $(\mathbf{A}\times\mathbf{B})\times\mathbf{C}$ are called vector triple products.

## 3. Key Theorems & Essential Results

> **Theorem (Orthogonality Test).** Two non-null vectors $\mathbf{A}$ and $\mathbf{B}$ are perpendicular if and only if $\mathbf{A}\cdot\mathbf{B}=0$.

This follows directly from $\mathbf{A}\cdot\mathbf{B}=AB\cos\theta$: for non-null vectors $A\neq 0$ and $B\neq 0$, the product vanishes exactly when $\cos\theta=0$, that is $\theta=90^{\circ}$.

> **Theorem (Parallelism Test).** Two non-null vectors are parallel if and only if $\mathbf{A}\times\mathbf{B}=\mathbf{0}$.

This follows from $\lVert\mathbf{A}\times\mathbf{B}\rVert=AB\sin\theta$: the magnitude vanishes exactly when $\sin\theta=0$, that is $\theta=0^{\circ}$ or $\theta=180^{\circ}$.

> **Theorem (Cosine Rule).** If $A$, $B$, $C$ are the three sides of a triangle and $\theta$ is the angle between the vectors $\mathbf{A}$ and $\mathbf{B}$, then



$$
C^2=A^2+B^2-2AB\cos\theta
$$



**Proof.** From the triangle relation $\mathbf{A}=\mathbf{B}+\mathbf{C}$, equivalently $\mathbf{C}=\mathbf{A}-\mathbf{B}$. Forming the dot product of $\mathbf{C}$ with itself,



$$
\begin{aligned}
\mathbf{C}\cdot\mathbf{C}&=(\mathbf{A}-\mathbf{B})\cdot(\mathbf{A}-\mathbf{B})\\
&=\mathbf{A}\cdot\mathbf{A}-2\,\mathbf{A}\cdot\mathbf{B}+\mathbf{B}\cdot\mathbf{B}
\end{aligned}
$$



Since $\mathbf{C}\cdot\mathbf{C}=C^2$, $\mathbf{A}\cdot\mathbf{A}=A^2$, $\mathbf{B}\cdot\mathbf{B}=B^2$ and $\mathbf{A}\cdot\mathbf{B}=AB\cos\theta$, the result follows. $\blacksquare$

> **Theorem (Properties of the Scalar Triple Product).** The scalar triple product satisfies



$$
\mathbf{A}\cdot(\mathbf{B}\times\mathbf{C})=\mathbf{B}\cdot(\mathbf{C}\times\mathbf{A})=\mathbf{C}\cdot(\mathbf{A}\times\mathbf{B})
$$



> and



$$
\mathbf{A}\cdot(\mathbf{A}\times\mathbf{B})=0
$$



**Proof.** The first identity holds because interchanging two rows of a determinant reverses its sign, and a cyclic permutation of three rows amounts to two interchanges, so the determinant is unchanged. The second holds because two rows of the determinant are identical, and a determinant with two identical rows is zero. $\blacksquare$

> **Theorem (Geometric Meaning of the Scalar Triple Product).** The scalar triple product in absolute value represents the volume of a parallelepiped with sides $\mathbf{A}$, $\mathbf{B}$ and $\mathbf{C}$.

> **Theorem (Coplanarity Test).** Three vectors lie in the same plane if and only if their scalar triple product is zero.

The scalar triple product therefore provides a test to show whether three given vectors are coplanar.

> **Theorem (Vector Triple Product Expansion).** For any three vectors,



$$
\mathbf{A}\times(\mathbf{B}\times\mathbf{C})=\mathbf{B}(\mathbf{A}\cdot\mathbf{C})-\mathbf{C}(\mathbf{A}\cdot\mathbf{B})
$$



This is the standard expansion, often remembered as "middle vector times dot of the outer pair, minus outer vector times dot of the other pair". The expansion is verified by writing out components and collecting terms.

> **Theorem (Non-Associativity of the Cross Product).** In general,



$$
(\mathbf{A}\times\mathbf{B})\times\mathbf{C}\neq\mathbf{A}\times(\mathbf{B}\times\mathbf{C})
$$



Parentheses are therefore mandatory in any expression involving a vector triple product, since omitting them renders the expression ambiguous.

> **Theorem (Area Interpretations).** The magnitude $\lVert\mathbf{A}\times\mathbf{B}\rVert$ is the area of the parallelogram with adjacent sides $\mathbf{A}$ and $\mathbf{B}$. The area of a triangle with two of its sides given by $\mathbf{A}$ and $\mathbf{B}$ is half the area of that parallelogram, namely



$$
\text{Area of triangle}=\tfrac{1}{2}\lVert\mathbf{A}\times\mathbf{B}\rVert
$$



> **Theorem (Equation of a Plane).** The equation of the plane perpendicular to a vector $\mathbf{A}$ and passing through the terminal point of a position vector $\mathbf{B}$ is



$$
\mathbf{r}\cdot\mathbf{A}=\mathbf{B}\cdot\mathbf{A}
$$



> where $\mathbf{r}$ is the position vector of a general point on the plane.

**Proof.** Let $\mathbf{r}$ be the position vector of a general point $P$ on the plane and let $Q$ be the terminal point of $\mathbf{B}$. The vector $\overrightarrow{QP}=\mathbf{B}-\mathbf{r}$ lies in the plane and is therefore perpendicular to the normal $\mathbf{A}$, so $(\mathbf{B}-\mathbf{r})\cdot\mathbf{A}=0$, which rearranges to $\mathbf{r}\cdot\mathbf{A}=\mathbf{B}\cdot\mathbf{A}$. $\blacksquare$

> **Theorem (Distance from a Point to a Plane).** The perpendicular distance from the point $(x_1,y_1,z_1)$ to the plane $ax+by+cz=d$ is



$$
\text{distance}=\frac{\lvert ax_1+by_1+cz_1-d\rvert}{\sqrt{a^2+b^2+c^2}}
$$



The distance from the origin to the plane is the projection of the position vector of any point on the plane onto the unit normal, which is the special case $x_1=y_1=z_1=0$.

> **Theorem (Direction Cosines).** If $\alpha$, $\beta$, $\gamma$ are the angles that a vector $\mathbf{A}$ makes with the positive $x$, $y$, $z$ axes respectively, then



$$
\cos\alpha=\frac{A_1}{A},\qquad \cos\beta=\frac{A_2}{A},\qquad \cos\gamma=\frac{A_3}{A}
$$



**Proof.** Since $\mathbf{A}\cdot\hat{\imath}=A\cos\alpha$ and also $\mathbf{A}\cdot\hat{\imath}=A_1$, division by $A$ gives the first relation; the others follow identically. $\blacksquare$

## 4. Worked Exemplar Problem with Step-by-Step Solution

**Problem.** Given $\mathbf{A}=3\hat{\imath}+\hat{\jmath}+2\hat{k}$ and $\mathbf{B}=\hat{\imath}-2\hat{\jmath}-4\hat{k}$ as position vectors of points $P$ and $Q$ respectively:

(a) find an equation for the plane passing through $Q$ and perpendicular to the line $PQ$;

(b) find the distance from the point $(-1,1,1)$ to that plane.

**Solution.**

**Step 1 — Identify the normal to the plane.** The plane passes through $Q$ and is perpendicular to the line $PQ$, so the direction vector $\overrightarrow{PQ}$ serves as the normal. Compute



$$
\overrightarrow{PQ}=\overrightarrow{OQ}-\overrightarrow{OP}=\mathbf{B}-\mathbf{A}
$$





$$
\begin{aligned}
\overrightarrow{PQ}&=(\hat{\imath}-2\hat{\jmath}-4\hat{k})-(3\hat{\imath}+\hat{\jmath}+2\hat{k})\\
&=-2\hat{\imath}-3\hat{\jmath}-6\hat{k}
\end{aligned}
$$



**Step 2 — Set up the perpendicularity condition.** Let $R(x,y,z)$ be a general point on the plane with position vector $\mathbf{r}=x\hat{\imath}+y\hat{\jmath}+z\hat{k}$. Since the plane is perpendicular to $PQ$, the vector $\overrightarrow{QR}$ lies in the plane and must satisfy



$$
\overrightarrow{PQ}\cdot\overrightarrow{QR}=0
$$



Now



$$
\overrightarrow{QR}=\overrightarrow{OR}-\overrightarrow{OQ}=(x-1)\hat{\imath}+(y+2)\hat{\jmath}+(z+4)\hat{k}
$$



**Step 3 — Evaluate the dot product.** Substituting,



$$
(-2\hat{\imath}-3\hat{\jmath}-6\hat{k})\cdot\big[(x-1)\hat{\imath}+(y+2)\hat{\jmath}+(z+4)\hat{k}\big]=0
$$



Using the component formula for the dot product,



$$
-2(x-1)-3(y+2)-6(z+4)=0
$$



**Step 4 — Simplify to standard form.** Expanding,



$$
-2x+2-3y-6-6z-24=0
$$





$$
-2x-3y-6z-28=0
$$



Multiplying through by $-1$,



$$
2x+3y+6z+28=0
$$



This is the required equation of the plane. Written in the form $ax+by+cz=d$ with $a=2$, $b=3$, $c=6$, it reads $2x+3y+6z=-28$.

**Step 5 — Compute the distance from the given point.** For the point $(x_1,y_1,z_1)=(-1,1,1)$ and the plane $ax+by+cz=d$,



$$
\text{distance}=\frac{\lvert ax_1+by_1+cz_1-d\rvert}{\sqrt{a^2+b^2+c^2}}
$$



Here $d=-28$, so



$$
\begin{aligned}
\text{distance}&=\frac{\lvert 2(-1)+3(1)+6(1)+28\rvert}{\sqrt{2^2+3^2+6^2}}\\
&=\frac{\lvert -2+3+6+28\rvert}{\sqrt{4+9+36}}\\
&=\frac{35}{7}\\
&=5
\end{aligned}
$$



The distance from $(-1,1,1)$ to the plane is $5$ units.

**Supplementary exemplar — angle between two vectors.** For $\mathbf{A}=2\hat{\imath}+2\hat{\jmath}-\hat{k}$ and $\mathbf{B}=6\hat{\imath}-3\hat{\jmath}+2\hat{k}$, the component formula gives



$$
\begin{aligned}
\mathbf{A}\cdot\mathbf{B}&=A_1B_1+A_2B_2+A_3B_3\\
&=(2)(6)+(2)(-3)+(-1)(2)\\
&=12-6-2\\
&=4
\end{aligned}
$$



The magnitudes are $A=\sqrt{4+4+1}=3$ and $B=\sqrt{36+9+4}=7$, so $AB=21$ and



$$
\cos\theta=\frac{4}{21}
$$



giving $\theta\approx 79^{\circ}$. This illustrates the standard two-step procedure: compute the dot product by components, then divide by the product of the magnitudes.

**Supplementary exemplar — perpendicularity with an unknown parameter.** Determine the values of $a$ for which $\mathbf{A}=a\hat{\imath}-2\hat{\jmath}+\hat{k}$ and $\mathbf{B}=2a\hat{\imath}+a\hat{\jmath}-4\hat{k}$ are perpendicular. The vectors are perpendicular exactly when their dot product is zero:



$$
(a\hat{\imath}-2\hat{\jmath}+\hat{k})\cdot(2a\hat{\imath}+a\hat{\jmath}-4\hat{k})=0
$$





$$
2a^2-2a-4=0
$$





$$
a^2-a-2=0
$$



Factoring gives $(a-2)(a+1)=0$, hence $a=2$ or $a=-1$.

**Supplementary exemplar — projection onto a direction.** To find the projection of $\mathbf{A}=\hat{\imath}-2\hat{\jmath}+\hat{k}$ on $\mathbf{B}=4\hat{\imath}-4\hat{\jmath}+7\hat{k}$, first normalize $\mathbf{B}$:



$$
\hat{b}=\frac{\mathbf{B}}{\lVert\mathbf{B}\rVert}=\frac{4\hat{\imath}-4\hat{\jmath}+7\hat{k}}{\sqrt{16+16+49}}=\frac{4}{9}\hat{\imath}-\frac{4}{9}\hat{\jmath}+\frac{7}{9}\hat{k}
$$



Then the projection is the scalar $\mathbf{A}\cdot\hat{b}$:



$$
\begin{aligned}
\mathbf{A}\cdot\hat{b}&=(\hat{\imath}-2\hat{\jmath}+\hat{k})\cdot\left(\frac{4}{9}\hat{\imath}-\frac{4}{9}\hat{\jmath}+\frac{7}{9}\hat{k}\right)\\
&=\frac{4}{9}+\frac{8}{9}+\frac{7}{9}\\
&=\frac{19}{9}
\end{aligned}
$$



**Supplementary exemplar — area of a triangle.** For the triangle with vertices $P(1,3,2)$, $Q(2,-1,1)$ and $R(-1,2,3)$, form two side vectors:



$$
\overrightarrow{PQ}=\hat{\imath}-4\hat{\jmath}-\hat{k},\qquad \overrightarrow{PR}=-2\hat{\imath}-\hat{\jmath}+\hat{k}
$$



The area of the triangle is half the magnitude of the cross product of these sides:



$$
\text{Area}=\tfrac{1}{2}\lVert\overrightarrow{PQ}\times\overrightarrow{PR}\rVert=\tfrac{1}{2}\sqrt{107}
$$



**Supplementary exemplar — non-associativity.** For $\mathbf{A}=3\hat{\imath}-\hat{\jmath}+2\hat{k}$, $\mathbf{B}=2\hat{\imath}+\hat{\jmath}-\hat{k}$ and $\mathbf{C}=\hat{\imath}-2\hat{\jmath}+2\hat{k}$, one computes $\mathbf{A}\times\mathbf{B}=-\hat{\imath}+7\hat{\jmath}+5\hat{k}$ and then



$$
(\mathbf{A}\times\mathbf{B})\times\mathbf{C}=15\hat{\imath}+15\hat{\jmath}-15\hat{k}
$$



while the alternative bracketing gives a different vector. Hence $(\mathbf{A}\times\mathbf{B})\times\mathbf{C}\neq\mathbf{A}\times(\mathbf{B}\times\mathbf{C})$, which demonstrates the need for parentheses in any vector triple product.

## 5. High-Yield Exam Takeaways & Common Pitfalls

### 5.1 Lesson Learning Outcomes

By the end of this unit the learner should be able to:

1. Determine the dot and cross product of two vectors.
2. Determine a vector perpendicular to a plane.
3. Evaluate scalar triple and vector triple products.

Every examination question in this topic maps onto one of these three outcomes, and the worked exemplars are organized to match them.

### 5.2 Magnitude, Unit Vector and Resultant — the Computational Core

The magnitude, unit vector and resultant subtopic supplies the numerical machinery on which every other calculation depends. The essential chain is:

- Magnitude: $A=\sqrt{A_1^2+A_2^2+A_3^2}$, obtained as $\sqrt{\mathbf{A}\cdot\mathbf{A}}$.
- Unit vector: $\hat{a}=\mathbf{A}/A$, which always has magnitude $1$ and points in the direction of $\mathbf{A}$.
- Resultant: $\mathbf{R}=\mathbf{A}+\mathbf{B}$, with magnitude $R=\sqrt{\mathbf{R}\cdot\mathbf{R}}$ and direction $\hat{r}=\mathbf{R}/R$.

The resultant's magnitude satisfies $\mathbf{R}\cdot\mathbf{R}=A^2+B^2+2AB\cos\theta$. This is the same identity as the cosine rule with the sign of the cross term reversed, and it is the standard route to the magnitude of a sum of two vectors given their magnitudes and the angle between them.

### 5.3 Assessment Checklist

The assessment items for this unit are of three standard types, and each has a fixed procedure:

- **Angle between two vectors.** Compute $\mathbf{A}\cdot\mathbf{B}$ by components, compute $A$ and $B$, then use $\cos\theta=\dfrac{\mathbf{A}\cdot\mathbf{B}}{AB}$ and take the inverse cosine. Always report the angle in the range $0^{\circ}$ to $180^{\circ}$.
- **Projection of one vector on another.** Normalize the target vector to obtain $\hat{b}$, then evaluate the scalar $\mathbf{A}\cdot\hat{b}$. Do not confuse the scalar projection with the vector projection; the scalar projection is a number, the vector projection is $(\mathbf{A}\cdot\hat{b})\hat{b}$.
- **Area of a triangle from three vertices.** Form two side vectors from a common vertex, take their cross product, and halve the magnitude. For vertices $P,Q,R$, one convenient choice is



$$
\text{Area}=\frac{1}{2}\left\lVert(Q-P)\times(R-P)\right\rVert.
$$



Choosing a different common vertex gives the same area. A quoted numerical area must equal this value; if the cross product of the chosen side vectors does not have the required magnitude, the quoted value is wrong and must be recomputed.

### 5.4 Pitfalls to Avoid

- **Sign errors in the determinant expansion.** The middle component of $\mathbf{A}\times\mathbf{B}$ carries a negative sign. Writing the determinant and expanding carefully along the first row prevents the most common arithmetic error in the entire topic.
- **Confusing the two products.** The dot product returns a scalar; the cross product returns a vector. A question asking for "the product" without qualification is ambiguous, and the expected answer is determined by whether the requested quantity is a number or a vector.
- **Forgetting anti-commutativity.** $\mathbf{B}\times\mathbf{A}=-(\mathbf{A}\times\mathbf{B})$, not $\mathbf{A}\times\mathbf{B}$. The magnitude is unchanged but the direction reverses.
- **Omitting parentheses in triple products.** Since $(\mathbf{A}\times\mathbf{B})\times\mathbf{C}\neq\mathbf{A}\times(\mathbf{B}\times\mathbf{C})$, an unparenthesized triple product is meaningless. State the bracketing explicitly.
- **Using the wrong distance formula sign.** The distance formula uses $\lvert ax_1+by_1+cz_1-d\rvert$ with the plane written as $ax+by+cz=d$. If the plane is written as $ax+by+cz+d=0$, the constant must be moved to the right-hand side before substitution, or the sign convention must be adjusted consistently.
- **Treating a zero dot product as "no answer".** A zero dot product is a definite conclusion: the vectors are perpendicular. Similarly, a zero cross product means the vectors are parallel, not that the calculation has failed.
- **Normalizing before projecting.** The projection onto $\mathbf{B}$ uses the unit vector $\hat{b}$, not $\mathbf{B}$ itself. Projecting onto $\mathbf{B}$ without normalizing gives a result scaled by $\lVert\mathbf{B}\rVert$.
- **Stating an area without verifying it.** For a triangle with vertices $P,Q,R$, the area must be $\frac{1}{2}\lVert(Q-P)\times(R-P)\rVert$. Any quoted value, such as a value involving $\sqrt{107}$, is correct only if that cross product magnitude is exactly the value used.

### 5.5 Reference Sources

The standard references supporting this unit are the texts by H. Davis, P. Lewis, M. Spiegel and C. Tai. These are cited as the approved reading for the topic; the definitions, component formulas, triple-product identities and geometric interpretations developed above are consistent with the treatment in those sources. Students should consult them for additional exercises on the dot product, cross product, scalar triple product, vector triple product, and the geometric applications to planes, distances and areas.

### 5.6 Summary of Essential Formulas

| Quantity | Formula |
| --- | --- |
| Dot product (geometric) | $\mathbf{A}\cdot\mathbf{B}=AB\cos\theta$ |
| Dot product (components) | $\mathbf{A}\cdot\mathbf{B}=A_1B_1+A_2B_2+A_3B_3$ |
| Magnitude | $A=\sqrt{A_1^2+A_2^2+A_3^2}$ |
| Unit vector | $\hat{a}=\mathbf{A}/A$ |
| Angle between vectors | $\cos\theta=\dfrac{\mathbf{A}\cdot\mathbf{B}}{AB}$ |
| Cross product (geometric) | $\lVert\mathbf{A}\times\mathbf{B}\rVert=AB\sin\theta$ |
| Cross product (components) | $\mathbf{A}\times\mathbf{B}=(A_2B_3-A_3B_2)\hat{\imath}-(A_1B_3-A_3B_1)\hat{\jmath}+(A_1B_2-A_2B_1)\hat{k}$ |
| Unit normal to plane spanned by two vectors | $\hat{n}=\dfrac{\mathbf{A}\times\mathbf{B}}{\lVert\mathbf{A}\times\mathbf{B}\rVert}$ |
| Scalar triple product (components) | $\mathbf{A}\cdot(\mathbf{B}\times\mathbf{C})=A_1(B_2C_3-B_3C_2)-A_2(B_1C_3-B_3C_1)+A_3(B_1C_2-B_2C_1)$ |
| Vector triple product | $\mathbf{A}\times(\mathbf{B}\times\mathbf{C})=\mathbf{B}(\mathbf{A}\cdot\mathbf{C})-\mathbf{C}(\mathbf{A}\cdot\mathbf{B})$ |
| Area of parallelogram | $\lVert\mathbf{A}\times\mathbf{B}\rVert$ |
| Area of triangle | $\tfrac{1}{2}\lVert\mathbf{A}\times\mathbf{B}\rVert$ |
| Volume of parallelepiped | $\lvert\mathbf{A}\cdot(\mathbf{B}\times\mathbf{C})\rvert$ |
| Plane through terminal point of $\mathbf{B}$ perpendicular to $\mathbf{A}$ | $\mathbf{r}\cdot\mathbf{A}=\mathbf{B}\cdot\mathbf{A}$ |
| Distance from point to plane | $\dfrac{\lvert ax_1+by_1+cz_1-d\rvert}{\sqrt{a^2+b^2+c^2}}$ |
| Cosine rule | $C^2=A^2+B^2-2AB\cos\theta$ |

Equivalently, the cross product and scalar triple product can be written as determinants:



$$
\mathbf{A}\times\mathbf{B}=
\begin{vmatrix}
\hat{\imath} & \hat{\jmath} & \hat{k} \\
A_1 & A_2 & A_3 \\
B_1 & B_2 & B_3
\end{vmatrix}
$$





$$
\mathbf{A}\cdot(\mathbf{B}\times\mathbf{C})=
\begin{vmatrix}
A_1 & A_2 & A_3 \\
B_1 & B_2 & B_3 \\
C_1 & C_2 & C_3
\end{vmatrix}
$$



These formulas, together with the orthogonality test $\mathbf{A}\cdot\mathbf{B}=0$, the parallelism test $\mathbf{A}\times\mathbf{B}=\mathbf{0}$, and the coplanarity test $\mathbf{A}\cdot(\mathbf{B}\times\mathbf{C})=0$, constitute the complete toolkit required for the assessment items of this unit.