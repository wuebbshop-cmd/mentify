## 1. Core Concept Overview & Intuition

The algebra of vectors admits two distinct products, distinguished by the type of quantity they return. The product of two vectors that yields a scalar is called the **dot product** or **scalar product**; the product of two vectors that yields a vector is called the **cross product** or **vector product**. Both products encode geometric information about the two vectors — their magnitudes and the angle between them — and both are indispensable for describing physical situations and the geometry of lines, planes, and triangles in space.

The central intuition for the dot product is **projection**. When a vector $\mathbf{B}$ is projected onto the line of a vector $\mathbf{A}$, the length of that projection is $B\cos\theta$, where $\theta$ is the angle between the vectors. Multiplying by $A$ gives $AB\cos\theta$, which is exactly the scalar product. Equivalently, one may project $\mathbf{A}$ onto $\mathbf{B}$ and multiply by $B$; the result is the same scalar. Thus the dot product measures the extent to which two vectors "point along" one another. When the vectors are perpendicular, the projection vanishes and the dot product is zero; when they are parallel, the projection is maximal and the dot product equals the product of magnitudes.

The central intuition for the cross product is **perpendicularity and area**. The cross product $\mathbf{A}\times\mathbf{B}$ is a vector of magnitude $AB\sin\theta$ directed perpendicular to both $\mathbf{A}$ and $\mathbf{B}$, with its sense fixed by the right-hand rule so that $\mathbf{A}$, $\mathbf{B}$, and $\mathbf{A}\times\mathbf{B}$ form a right-handed system in that order. Because $AB\sin\theta$ is the area of the parallelogram spanned by $\mathbf{A}$ and $\mathbf{B}$, the cross product is the natural tool for computing areas of parallelograms and triangles, for producing vectors normal to planes, and for testing whether vectors are parallel.

A third layer of structure emerges when three vectors are combined. The **scalar triple product** $\mathbf{A}\cdot(\mathbf{B}\times\mathbf{C})$ returns a scalar whose absolute value is the volume of the parallelepiped with sides $\mathbf{A}$, $\mathbf{B}$, $\mathbf{C}$, and which vanishes precisely when the three vectors are coplanar. The **vector triple product** $\mathbf{A}\times(\mathbf{B}\times\mathbf{C})$ returns a vector lying in the plane of $\mathbf{B}$ and $\mathbf{C}$, and it is not associative: the placement of parentheses changes the result.

Throughout, all vectors are referred to a right-handed set of mutually orthogonal unit vectors $\hat{i}$, $\hat{j}$, $\hat{k}$ along the $x$, $y$, $z$ axes respectively. The axes $OX$, $OY$, $OZ$ form a right-handed set if a rotation from $OX$ to $OY$ corresponds to a right-handed corkscrew action along the positive direction of $OZ$; similarly, a rotation from $OY$ to $OZ$ gives a right-handed corkscrew action along the positive direction of $OX$, and so on cyclically.

## 2. Mathematical Formalization & Core Definitions

### 2.1 The Dot or Scalar Product

> **Definition (Dot Product).** If $\mathbf{A}$ and $\mathbf{B}$ are two vectors, the scalar product of $\mathbf{A}$ and $\mathbf{B}$ is defined as $AB\cos\theta$, where $A$ and $B$ are the magnitudes of the vectors $\mathbf{A}$ and $\mathbf{B}$, and $\theta$ is the angle between them. The scalar (dot) product is denoted by $\mathbf{A}\cdot\mathbf{B}$.

The definition may be read in either of two equivalent ways:

$$
\mathbf{A}\cdot\mathbf{B}=AB\cos\theta
$$

$$
\mathbf{A}\cdot\mathbf{B}=A\times(\text{projection of } \mathbf{B} \text{ on } \mathbf{A})
$$

$$
\mathbf{A}\cdot\mathbf{B}=B\times(\text{projection of } \mathbf{A} \text{ on } \mathbf{B})
$$

In either case the result is a scalar quantity.

**Magnitude of a vector.** The magnitude of a vector $\mathbf{A}=A_1\hat{i}+A_2\hat{j}+A_3\hat{k}$ is the square root of the sum of the squares of its components:

$$
A=\lVert \mathbf{A}\rVert=\sqrt{A_1^{2}+A_2^{2}+A_3^{2}}
$$

**Unit vector.** The unit vector in the direction of a non-zero vector $\mathbf{A}$ is obtained by dividing the vector by its magnitude:

$$
\hat{a}=\frac{\mathbf{A}}{A}=\frac{\mathbf{A}}{\lVert \mathbf{A}\rVert}
$$

This unit vector has magnitude $1$ and points in the same direction as $\mathbf{A}$.

**Resultant.** The resultant of two vectors is their vector sum $\mathbf{A}+\mathbf{B}$, obtained by adding corresponding components. Its magnitude is computed from the components of the sum using the magnitude formula above.

### 2.2 Special Angles and Orthogonality

When two vectors are at right angles, $\theta=90^{\circ}$, so that

$$
\mathbf{A}\cdot\mathbf{B}=AB\cos 90^{\circ}=AB\cdot 0=0
$$

Thus the scalar product of any two vectors at right angles to each other is always zero, and the two vectors are said to be **orthogonal** or **perpendicular** to one another.

When two vectors are in the same direction, $\theta=0^{\circ}$, so that

$$
\mathbf{A}\cdot\mathbf{B}=AB\cos 0^{\circ}=AB
$$

### 2.3 The Dot Product in Component Form

Write the two vectors in component form as

$$
\mathbf{A}=A_1\hat{i}+A_2\hat{j}+A_3\hat{k}
$$

$$
\mathbf{B}=B_1\hat{i}+B_2\hat{j}+B_3\hat{k}
$$

Expanding the product term by term gives

$$
\begin{aligned}
\mathbf{A}\cdot\mathbf{B}={}&A_1B_1\,\hat{i}\cdot\hat{i}+A_1B_2\,\hat{i}\cdot\hat{j}+A_1B_3\,\hat{i}\cdot\hat{k}\\
&+A_2B_1\,\hat{j}\cdot\hat{i}+A_2B_2\,\hat{j}\cdot\hat{j}+A_2B_3\,\hat{j}\cdot\hat{k}\\
&+A_3B_1\,\hat{k}\cdot\hat{i}+A_3B_2\,\hat{k}\cdot\hat{j}+A_3B_3\,\hat{k}\cdot\hat{k}
\end{aligned}
$$

Now the parallel unit-vector products satisfy

$$
\hat{i}\cdot\hat{i}=\hat{j}\cdot\hat{j}=\hat{k}\cdot\hat{k}=1\cdot 1\cos 0^{\circ}=1
$$

and the perpendicular unit-vector products satisfy

$$
\hat{i}\cdot\hat{j}=\hat{i}\cdot\hat{k}=\hat{j}\cdot\hat{k}=1\cdot 1\cos 90^{\circ}=0
$$

All cross terms therefore vanish, and we are left with

$$
\mathbf{A}\cdot\mathbf{B}=A_1B_1+A_2B_2+A_3B_3
$$

This component formula is the principal computational tool for the dot product. It also yields the angle between two vectors through

$$
\cos\theta=\frac{\mathbf{A}\cdot\mathbf{B}}{AB}=\frac{A_1B_1+A_2B_2+A_3B_3}{\sqrt{A_1^{2}+A_2^{2}+A_3^{2}}\,\sqrt{B_1^{2}+B_2^{2}+B_3^{2}}}
$$

### 2.4 The Cross or Vector Product

> **Definition (Cross Product).** The cross or vector product of $\mathbf{A}$ and $\mathbf{B}$, written $\mathbf{A}\times\mathbf{B}$ and read as "$\mathbf{A}$ cross $\mathbf{B}$", is defined as a vector having the magnitude $AB\sin\theta$, where $\theta$ is the angle between the two vectors. The product vector acts in a direction perpendicular to $\mathbf{A}$ and $\mathbf{B}$ in such a sense that $\mathbf{A}$, $\mathbf{B}$, and $\mathbf{A}\times\mathbf{B}$ form a right-handed system in that order.

The magnitude is

$$
\lVert \mathbf{A}\times\mathbf{B}\rVert=AB\sin\theta
$$

Reversing the order reverses the direction of rotation, so the product vector acts downward:

$$
\mathbf{B}\times\mathbf{A}=-(\mathbf{A}\times\mathbf{B})
$$

The cross product is therefore **anticommutative**.

**Special angles.** If $\theta=0^{\circ}$, then

$$
\lVert \mathbf{A}\times\mathbf{B}\rVert=AB\sin 0^{\circ}=0
$$

so parallel vectors have zero cross product. If $\theta=90^{\circ}$, then

$$
\lVert \mathbf{A}\times\mathbf{B}\rVert=AB\sin 90^{\circ}=AB
$$

so perpendicular vectors attain the maximum magnitude $AB$.

### 2.5 The Cross Product in Component Form

With $\mathbf{A}=A_1\hat{i}+A_2\hat{j}+A_3\hat{k}$ and $\mathbf{B}=B_1\hat{i}+B_2\hat{j}+B_3\hat{k}$, expansion gives

$$
\begin{aligned}
\mathbf{A}\times\mathbf{B}={}&A_1B_1\,\hat{i}\times\hat{i}+A_1B_2\,\hat{i}\times\hat{j}+A_1B_3\,\hat{i}\times\hat{k}\\
&+A_2B_1\,\hat{j}\times\hat{i}+A_2B_2\,\hat{j}\times\hat{j}+A_2B_3\,\hat{j}\times\hat{k}\\
&+A_3B_1\,\hat{k}\times\hat{i}+A_3B_2\,\hat{k}\times\hat{j}+A_3B_3\,\hat{k}\times\hat{k}
\end{aligned}
$$

Since $\hat{i}\times\hat{i}=1\cdot 1\cdot\sin 0^{\circ}=0$, we have

$$
\hat{i}\times\hat{i}=\hat{j}\times\hat{j}=\hat{k}\times\hat{k}=0
$$

Also $\hat{i}\times\hat{j}=1\cdot 1\cdot\sin 90^{\circ}=1$ in the direction $OZ$, that is $\hat{i}\times\hat{j}=\hat{k}$. The complete set of unit-vector cross products is

$$
\hat{i}\times\hat{j}=\hat{k},\qquad \hat{j}\times\hat{i}=-\hat{k}
$$

$$
\hat{j}\times\hat{k}=\hat{i},\qquad \hat{k}\times\hat{j}=-\hat{i}
$$

$$
\hat{k}\times\hat{i}=\hat{j},\qquad \hat{i}\times\hat{k}=-\hat{j}
$$

Substituting and collecting components yields

$$
\mathbf{A}\times\mathbf{B}=(A_2B_3-A_3B_2)\,\hat{i}+(A_3B_1-A_1B_3)\,\hat{j}+(A_1B_2-A_2B_1)\,\hat{k}
$$

This is recognized as the expansion of the determinant

$$
\mathbf{A}\times\mathbf{B}=
\begin{vmatrix}
\hat{i} & \hat{j} & \hat{k}\\
A_1 & A_2 & A_3\\
B_1 & B_2 & B_3
\end{vmatrix}
$$

The determinant form is the standard computational device: expand along the first row, remembering that the middle term carries a negative sign.

### 2.6 Vector Perpendicular to a Plane

The vector $\mathbf{A}\times\mathbf{B}$ is perpendicular to the plane on which the vectors $\mathbf{A}$ and $\mathbf{B}$ lie. The right-hand thumb rule determines the direction of this perpendicular. To obtain the **unit** vector perpendicular to the plane, divide by the magnitude:

$$
\hat{n}=\frac{\mathbf{A}\times\mathbf{B}}{\lVert \mathbf{A}\times\mathbf{B}\rVert}
$$

### 2.7 Scalar Triple Product

> **Definition (Scalar Triple Product).** If $\mathbf{A}$, $\mathbf{B}$, $\mathbf{C}$ are three vectors, the scalar formed by the product $\mathbf{A}\cdot(\mathbf{B}\times\mathbf{C})$ is called the scalar triple product.

For $\mathbf{A}=A_1\hat{i}+A_2\hat{j}+A_3\hat{k}$, $\mathbf{B}=B_1\hat{i}+B_2\hat{j}+B_3\hat{k}$, $\mathbf{C}=C_1\hat{i}+C_2\hat{j}+C_3\hat{k}$, the scalar triple product is the determinant

$$
\mathbf{A}\cdot(\mathbf{B}\times\mathbf{C})=
\begin{vmatrix}
A_1 & A_2 & A_3\\
B_1 & B_2 & B_3\\
C_1 & C_2 & C_3
\end{vmatrix}
$$

### 2.8 Vector Triple Product

> **Definition (Vector Triple Product).** If $\mathbf{A}$, $\mathbf{B}$ and $\mathbf{C}$ are three vectors, then $\mathbf{A}\times(\mathbf{B}\times\mathbf{C})$ and $(\mathbf{A}\times\mathbf{B})\times\mathbf{C}$ are called vector triple products.

The expansion identity is

$$
\mathbf{A}\times(\mathbf{B}\times\mathbf{C})=(\mathbf{A}\cdot\mathbf{C})\,\mathbf{B}-(\mathbf{A}\cdot\mathbf{B})\,\mathbf{C}
$$

The result lies in the plane of $\mathbf{B}$ and $\mathbf{C}$, and the two bracketings generally differ, so parentheses are essential.

## 3. Key Theorems & Essential Results

> **Result (Perpendicularity Test).** Two non-zero vectors $\mathbf{A}$ and $\mathbf{B}$ are perpendicular if and only if $\mathbf{A}\cdot\mathbf{B}=0$.

> **Result (Parallelism Test).** Two non-zero vectors $\mathbf{A}$ and $\mathbf{B}$ are parallel if and only if $\mathbf{A}\times\mathbf{B}=\mathbf{0}$.

> **Result (Projection Formula).** The projection of $\mathbf{A}$ on $\mathbf{B}$ equals $\mathbf{A}\cdot\hat{b}$, where $\hat{b}=\mathbf{B}/\lVert \mathbf{B}\rVert$ is the unit vector in the direction of $\mathbf{B}$.

> **Result (Cosine Rule).** If $A$, $B$, $C$ are the three sides of a triangle and $\theta$ is the angle between the vectors $\mathbf{A}$ and $\mathbf{B}$, then

> 

$$
C^{2}=A^{2}+B^{2}-2AB\cos\theta
$$

*Derivation.* From the triangle relation $\mathbf{A}=\mathbf{B}+\mathbf{C}$, equivalently $\mathbf{C}=\mathbf{A}-\mathbf{B}$. Then

$$
\begin{aligned}
\mathbf{C}\cdot\mathbf{C}&=(\mathbf{A}-\mathbf{B})\cdot(\mathbf{A}-\mathbf{B})\\
&=\mathbf{A}\cdot\mathbf{A}-2\,\mathbf{A}\cdot\mathbf{B}+\mathbf{B}\cdot\mathbf{B}
\end{aligned}
$$

Since $\mathbf{C}\cdot\mathbf{C}=C^{2}$, $\mathbf{A}\cdot\mathbf{A}=A^{2}$, $\mathbf{B}\cdot\mathbf{B}=B^{2}$ and $\mathbf{A}\cdot\mathbf{B}=AB\cos\theta$, the stated identity follows.

> **Result (Equation of a Plane).** The plane perpendicular to a vector $\mathbf{A}$ and passing through the terminal point of a position vector $\mathbf{B}$ has equation $\mathbf{r}\cdot\mathbf{A}=\mathbf{B}\cdot\mathbf{A}$, where $\mathbf{r}$ is the position vector of a general point on the plane.

*Derivation.* Let $Q$ be the terminal point of $\mathbf{B}$ and $P$ a general point of the plane with position vector $\mathbf{r}$. The vector $\overrightarrow{PQ}=\mathbf{B}-\mathbf{r}$ lies in the plane and is therefore perpendicular to the normal $\mathbf{A}$, so $(\mathbf{B}-\mathbf{r})\cdot\mathbf{A}=0$, which rearranges to $\mathbf{r}\cdot\mathbf{A}=\mathbf{B}\cdot\mathbf{A}$.

> **Result (Distance from a Point to a Plane).** The distance from the point $(x_1,y_1,z_1)$ to the plane $ax+by+cz=d$ is

> 

$$
\text{distance}=\frac{\lvert ax_1+by_1+cz_1-d\rvert}{\sqrt{a^{2}+b^{2}+c^{2}}}
$$

> **Result (Area of a Parallelogram and Triangle).** The area of the parallelogram with adjacent sides $\mathbf{A}$ and $\mathbf{B}$ is $\lVert \mathbf{A}\times\mathbf{B}\rVert$. The area of a triangle is half the area of a parallelogram, hence

> 

$$
\text{area of triangle}=\tfrac{1}{2}\lVert \mathbf{A}\times\mathbf{B}\rVert
$$

> **Result (Properties of the Scalar Triple Product).** The scalar triple product satisfies

> 

$$
\mathbf{A}\cdot(\mathbf{B}\times\mathbf{C})=\mathbf{B}\cdot(\mathbf{C}\times\mathbf{A})=\mathbf{C}\cdot(\mathbf{A}\times\mathbf{B})
$$

> and

> 

$$
\mathbf{A}\cdot(\mathbf{A}\times\mathbf{B})=0
$$

> the latter because two rows of the determinant are identical. Interchanging two rows of a determinant reverses its sign, which accounts for the cyclic symmetry.

> **Result (Volume and Coplanarity).** The scalar triple product in absolute value represents the volume of a parallelepiped with sides $\mathbf{A}$, $\mathbf{B}$ and $\mathbf{C}$. The scalar triple product provides a test to show whether three given vectors lie in the same plane: the vectors are coplanar if and only if $\mathbf{A}\cdot(\mathbf{B}\times\mathbf{C})=0$.

> **Result (Non-Associativity of the Cross Product).** In general

> 

$$
\mathbf{A}\times(\mathbf{B}\times\mathbf{C})\neq(\mathbf{A}\times\mathbf{B})\times\mathbf{C}
$$

> so parentheses are required in $\mathbf{A}\times\mathbf{B}\times\mathbf{C}$ to avoid ambiguity.

## 4. Worked Exemplar Problem with Step-by-Step Solution

**Problem.** Given the position vectors $\mathbf{A}=3\hat{i}+\hat{j}+2\hat{k}$ and $\mathbf{B}=\hat{i}-2\hat{j}-4\hat{k}$ of points $P$ and $Q$ respectively:

(a) find an equation for the plane passing through $Q$ and perpendicular to the line $PQ$;

(b) find the distance from the point $(-1,1,1)$ to that plane.

**Solution.**

*Part (a).* Let the position vector of a general point $R$ on the plane be $\mathbf{r}=x\hat{i}+y\hat{j}+z\hat{k}$. The direction vector of the line $PQ$ is

$$
\begin{aligned}
\overrightarrow{PQ}&=\overrightarrow{OQ}-\overrightarrow{OP}\\
&=\mathbf{B}-\mathbf{A}\\
&=(\hat{i}-2\hat{j}-4\hat{k})-(3\hat{i}+\hat{j}+2\hat{k})\\
&=-2\hat{i}-3\hat{j}-6\hat{k}
\end{aligned}
$$

Since the plane is perpendicular to $PQ$, the vector $\overrightarrow{PQ}$ serves as a normal to the plane, and every vector lying in the plane is orthogonal to it. In particular,

$$
\overrightarrow{PQ}\cdot\overrightarrow{QR}=0
$$

Now

$$
\begin{aligned}
\overrightarrow{QR}&=\overrightarrow{OR}-\overrightarrow{OQ}\\
&=(x-1)\hat{i}+(y+2)\hat{j}+(z+4)\hat{k}
\end{aligned}
$$

Substituting,

$$
(-2\hat{i}-3\hat{j}-6\hat{k})\cdot\big[(x-1)\hat{i}+(y+2)\hat{j}+(z+4)\hat{k}\big]=0
$$

Evaluating the dot product componentwise,

$$
-2(x-1)-3(y+2)-6(z+4)=0
$$

Expanding,

$$
-2x+2-3y-6-6z-24=0
$$

which simplifies to

$$
2x+3y+6z+28=0
$$

This is the required equation of the plane.

*Part (b).* Write the plane in the form $ax+by+cz=d$ with $a=2$, $b=3$, $c=6$ and $d=-28$. The distance from $(x_1,y_1,z_1)$ to the plane is

$$
\text{distance}=\frac{\lvert ax_1+by_1+cz_1-d\rvert}{\sqrt{a^{2}+b^{2}+c^{2}}}
$$

For the point $(-1,1,1)$,

$$
\begin{aligned}
\text{distance}&=\frac{\lvert 2(-1)+3(1)+6(1)+28\rvert}{\sqrt{2^{2}+3^{2}+6^{2}}}\\
&=\frac{\lvert -2+3+6+28\rvert}{7}\\
&=\frac{35}{7}\\
&=5
\end{aligned}
$$

The distance from $(-1,1,1)$ to the plane is $5$ units.

**Supplementary exemplar (angle between two vectors).** If $\mathbf{A}=2\hat{i}+2\hat{j}-\hat{k}$ and $\mathbf{B}=6\hat{i}-3\hat{j}+2\hat{k}$, then

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

giving $\theta\approx 79^{\circ}$.

**Supplementary exemplar (perpendicularity condition).** Determine the values of $a$ such that $\mathbf{A}=a\hat{i}-2\hat{j}+\hat{k}$ and $\mathbf{B}=2a\hat{i}+a\hat{j}-4\hat{k}$ are perpendicular. Perpendicularity requires $\mathbf{A}\cdot\mathbf{B}=0$:

$$
(a)(2a)+(-2)(a)+(1)(-4)=0
$$

so that

$$
2a^{2}-2a-4=0
$$

or

$$
a^{2}-a-2=0
$$

Factoring, $(a-2)(a+1)=0$, from which $a=2$ or $a=-1$.

**Supplementary exemplar (projection).** The projection of $\mathbf{A}=\hat{i}-2\hat{j}+\hat{k}$ on $\mathbf{B}=4\hat{i}-4\hat{j}+7\hat{k}$ is $\mathbf{A}\cdot\hat{b}$. First,

$$
\hat{b}=\frac{4\hat{i}-4\hat{j}+7\hat{k}}{\sqrt{4^{2}+(-4)^{2}+7^{2}}}=\frac{4}{9}\hat{i}-\frac{4}{9}\hat{j}+\frac{7}{9}\hat{k}
$$

Then

$$
\begin{aligned}
\mathbf{A}\cdot\hat{b}&=(\hat{i}-2\hat{j}+\hat{k})\cdot\left(\frac{4}{9}\hat{i}-\frac{4}{9}\hat{j}+\frac{7}{9}\hat{k}\right)\\
&=\frac{4}{9}+\frac{8}{9}+\frac{7}{9}\\
&=\frac{19}{9}
\end{aligned}
$$

**Supplementary exemplar (direction cosines).** For $\mathbf{A}=3\hat{i}-6\hat{j}+2\hat{k}$ with magnitude $7$, the angles $\alpha$, $\beta$, $\gamma$ with the positive $x$, $y$, $z$ axes satisfy

$$
\cos\alpha=\frac{3}{7},\qquad \cos\beta=-\frac{6}{7},\qquad \cos\gamma=\frac{2}{7}
$$

so that $\alpha=\cos^{-1}(3/7)\approx 64.6^{\circ}$, $\beta=\cos^{-1}(-6/7)\approx 149^{\circ}$ and $\gamma=\cos^{-1}(2/7)\approx 73.4^{\circ}$.

**Supplementary exemplar (right-angled triangle).** The vectors $\mathbf{A}=3\hat{i}-2\hat{j}+\hat{k}$, $\mathbf{B}=\hat{i}-3\hat{j}+5\hat{k}$, $\mathbf{C}=2\hat{i}+\hat{j}-4\hat{k}$ form a triangle because $\mathbf{A}=\mathbf{B}+\mathbf{C}$, so the sum of two of them equals the third. Computing $\mathbf{A}\cdot\mathbf{C}$ gives zero, so $\mathbf{A}$ and $\mathbf{C}$ are perpendicular and the triangle is right-angled.

**Supplementary exemplar (area of a triangle).** For the triangle with vertices $P(1,3,2)$, $Q(2,-1,1)$, $R(-1,2,3)$, the side vectors are $\overrightarrow{PQ}=\hat{i}-4\hat{j}-\hat{k}$ and $\overrightarrow{PR}=-2\hat{i}-\hat{j}+\hat{k}$. The area is

$$
\text{area}=\tfrac{1}{2}\lVert \overrightarrow{PQ}\times\overrightarrow{PR}\rVert=\tfrac{1}{2}\sqrt{107}
$$

**Supplementary exemplar (scalar triple product).** For $\mathbf{A}=2\hat{i}-3\hat{j}+4\hat{k}$, $\mathbf{B}=\hat{i}+2\hat{j}-\hat{k}$ and $\mathbf{C}=3\hat{i}-\hat{j}+2\hat{k}$, first compute

$$
\mathbf{B}\times\mathbf{C}=-\hat{i}-8\hat{j}+5\hat{k}
$$

Then

$$
\begin{aligned}
\mathbf{A}\cdot(\mathbf{B}\times\mathbf{C})&=(2\hat{i}-3\hat{j}+4\hat{k})\cdot(-\hat{i}-8\hat{j}+5\hat{k})\\
&=-2+24+20\\
&=42
\end{aligned}
$$

**Supplementary exemplar (non-associativity).** For $\mathbf{A}=3\hat{i}-\hat{j}+2\hat{k}$, $\mathbf{B}=2\hat{i}+\hat{j}-\hat{k}$ and $\mathbf{C}=\hat{i}-2\hat{j}+2\hat{k}$, one finds $\mathbf{A}\times\mathbf{B}=-\hat{i}+7\hat{j}+5\hat{k}$, and hence

$$
(\mathbf{A}\times\mathbf{B})\times\mathbf{C}=15\hat{i}+15\hat{j}-15\hat{k}
$$

whereas

$$
\mathbf{A}\times(\mathbf{B}\times\mathbf{C})=15\hat{i}+15\hat{j}-15\hat{k}
$$

is obtained by a separate expansion, confirming that the two bracketings must be distinguished and that parentheses are required in $\mathbf{A}\times\mathbf{B}\times\mathbf{C}$.

## 5. High-Yield Exam Takeaways & Common Pitfalls

### Lesson Learning Outcomes

By the end of this unit the learner should be able to:

1. Determine the dot and cross product of two vectors.
2. Determine a vector perpendicular to a plane.
3. Evaluate scalar triple and vector triple products.

### Magnitude, Unit Vector and Resultant — Checklist

- Compute magnitude as $A=\sqrt{A_1^{2}+A_2^{2}+A_3^{2}}$; never omit the square root.
- Compute the unit vector as $\hat{a}=\mathbf{A}/A$; verify that its magnitude is $1$.
- Compute the resultant by adding components first, then taking the magnitude of the sum. Do not add magnitudes.
- The projection of $\mathbf{A}$ on $\mathbf{B}$ is $\mathbf{A}\cdot\hat{b}$, a scalar; the vector projection is $(\mathbf{A}\cdot\hat{b})\,\hat{b}$.

### High-Yield Results to Memorize

| Result | Formula |
| --- | --- |
| Dot product, geometric | $\mathbf{A}\cdot$\mathbf{B}=AB\cos\theta$ |
| Dot product, component | $\mathbf{A}\cdot\mathbf{B}=A_1B_1+A_2B_2+A_3B_3$ |
| Angle between vectors | $\cos\theta=\dfrac{\mathbf{A}\cdot\mathbf{B}}{AB}$ |
| Cross product, magnitude | $\lVert \mathbf{A}\times\mathbf{B}\rVert=AB\sin\theta$ |
| Cross product, determinant | $\mathbf{A}\times\mathbf{B}=

$$
\begin{vmatrix}
\hat{i}&\hat{j}&\hat{k}\A_1&A_2&A_3\B_1&B_2&B_3
\end{vmatrix}
$$

$ |
| Unit normal to a plane | $\hat{n}=\dfrac{\mathbf{A}\times\mathbf{B}}{\lVert \mathbf{A}\times\mathbf{B}\rVert}$ |
| Scalar triple product | $\mathbf{A}\cdot(\mathbf{B}\times\mathbf{C})=

$$
\begin{vmatrix}
A_1&A_2&A_3\B_1&B_2&B_3\C_1&C_2&C_3
\end{vmatrix}
$$

$ |
| Vector triple product | $\mathbf{A}\times(\mathbf{B}\times\mathbf{C})=(\mathbf{A}\cdot\mathbf{C})\,\mathbf{B}-(\mathbf{A}\cdot\mathbf{B})\,\mathbf{C}$ |
| Area of triangle | $\tfrac{1}{2}\lVert \mathbf{A}\times\mathbf{B}\rVert$ |
| Volume of parallelepiped | $\lvert \mathbf{A}\cdot(\mathbf{B}\times\mathbf{C})\rvert$ |
| Distance point to plane | $\dfrac{\lvert ax_1+by_1+cz_1-d\rvert}{\sqrt{a^{2}+b^{2}+c^{2}}}$ |

### Common Pitfalls

- **Confusing the two products.** The dot product returns a scalar; the cross product returns a vector. A question asking for an angle or a projection requires the dot product; a question asking for a normal, an area, or a perpendicular direction requires the cross product.
- **Sign errors in the determinant expansion.** The middle term of the cross-product determinant carries a negative sign. Writing $(A_1B_3-A_3B_1)\hat{j}$ instead of $(A_3B_1-A_1B_3)\hat{j}$ is the most frequent computational error.
- **Forgetting anticommutativity.** Always use $\mathbf{B}\times\mathbf{A}=-(\mathbf{A}\times\mathbf{B})$. Reversing the order reverses the normal direction.
- **Dropping parentheses in triple products.** The vector triple product is not associative; $\mathbf{A}\times(\mathbf{B}\times\mathbf{C})$ and $(\mathbf{A}\times\mathbf{B})\times\mathbf{C}$ are generally different vectors. Never write $\mathbf{A}\times\mathbf{B}\times\mathbf{C}$ without brackets.
- **Misapplying the perpendicularity test.** $\mathbf{A}\cdot\mathbf{B}=0$ tests perpendicularity; $\mathbf{A}\times\mathbf{B}=\mathbf{0}$ tests parallelism. Do not interchange them.
- **Omitting the absolute value in distance and volume.** Distance and volume are non-negative; the scalar triple product itself may be negative, so take $\lvert \mathbf{A}\cdot(\mathbf{B}\times\mathbf{C})\rvert$ for volume.
- **Normalizing incorrectly.** When forming a unit normal, divide the whole vector $\mathbf{A}\times\mathbf{B}$ by its magnitude, not by the magnitudes of $\mathbf{A}$ and $\mathbf{B}$ separately.
- **Sign slips in the plane equation.** When the normal is $\overrightarrow{PQ}=\mathbf{B}-\mathbf{A}$, the plane equation is $\mathbf{r}\cdot(\mathbf{B}-\mathbf{A})=\mathbf{B}\cdot(\mathbf{B}-\mathbf{A})$. Substituting a general point and expanding carefully avoids arithmetic errors of the kind that produce $+28$ instead of $-28$.
- **Angle range.** The inverse cosine returns a value in $[0^{\circ},180^{\circ}]$; a negative cosine correctly signals an obtuse angle, as in $\beta\approx 149^{\circ}$ above.

### Assessment

1. Find the angle between $\mathbf{A}=2\hat{i}+2\hat{j}-\hat{k}$ and $\mathbf{B}=6\hat{i}-3\hat{j}+2\hat{k}$.
2. Find the projection of the vector $\mathbf{A}=\hat{i}-2\hat{j}+\hat{k}$ on the vector $\mathbf{B}=4\hat{i}-4\hat{j}+7\hat{k}$.
3. Find the area of the triangle with vertices $P(1,3,2)$, $Q(2,-1,1)$ and $R(-1,2,3)$.
4. Determine a unit vector perpendicular to the plane containing $\mathbf{A}$ and $\mathbf{B}$.
5. Evaluate the scalar triple product $\mathbf{A}\cdot(\mathbf{B}\times\mathbf{C})$ and hence state whether the three vectors are coplanar.
6. Show that $\mathbf{A}\times(\mathbf{B}\times\mathbf{C})\neq(\mathbf{A}\times\mathbf{B})\times\mathbf{C}$ for suitable vectors, and explain why parentheses are required.

### Recommended Reading

- Davis, H. — vector algebra and the geometry of the dot and cross products.
- Lewis, P. — worked exercises on projections, normals and plane equations.
- Spiegel, M. — scalar and vector triple products, determinants and applications.
- Tai, C. — geometric interpretation of the cross product and right-handed systems.