## 1. Core Concept Overview & Intuition

The reciprocal set of vectors is a construction that answers a natural question: given three vectors that are not coplanar, can we manufacture a second set of three vectors that "interrogates" the first set one vector at a time? The answer is yes, and the construction is unique.

The intuition is best captured by the phrase used in the course material: a reciprocal vector is formed by choosing a vector perpendicular to two of the lattice (given) vectors and of length reciprocal to the third. Concretely, if the given set is $\vec{a},\vec{b},\vec{c}$, then the reciprocal partner of $\vec{a}$ must be perpendicular to both $\vec{b}$ and $\vec{c}$ (so it is parallel to $\vec{b}\times\vec{c}$) and must have a magnitude adjusted so that its dot product with $\vec{a}$ equals exactly $1$. The same logic applies cyclically to $\vec{b}$ and $\vec{c}$.

The defining behavioural property is a "perfect matching" dot-product pattern: each reciprocal vector dots to $1$ with its own partner and to $0$ with the other two. This is the continuous analogue of an orthonormal basis, and it is the reason reciprocal sets appear whenever one needs to extract a single component of a vector relative to a skew (non-orthogonal) basis. In examinations this topic is tested almost exclusively through one task: given three explicit vectors, compute the reciprocal set. The marks are awarded for the correct scalar triple product in the denominator, the correct cross products in the numerators, and the correct final components.

The topic sits entirely within vector algebra and the dot and cross product, so every tool required is already available: determinants for cross products, the scalar triple product for volumes, and dot products for verification.

## 2. Mathematical Formalization & Core Definitions

> **Definition (Reciprocal of a single vector).** The vector which has the same direction as a given vector but has magnitude reciprocal to that of the given vector is called the reciprocal of that vector.

Thus if $\vec{a}$ has magnitude $\lVert\vec{a}\rVert$, its reciprocal in this elementary sense is the vector $\dfrac{\vec{a}}{\lVert\vec{a}\rVert^{2}}$, which points along $\vec{a}$ and satisfies $\vec{a}\cdot\dfrac{\vec{a}}{\lVert\vec{a}\rVert^{2}}=1$.

> **Definition (Reciprocal set of vectors).** Let $\vec{a},\vec{b},\vec{c}$ be three non-coplanar vectors, so that the scalar triple product $\vec{a}\cdot(\vec{b}\times\vec{c})\neq 0$. The reciprocal set $\vec{a}',\vec{b}',\vec{c}'$ is defined by



$$
\vec{a}'=\frac{\vec{b}\times\vec{c}}{\vec{a}\cdot(\vec{b}\times\vec{c})},\qquad \vec{b}'=\frac{\vec{c}\times\vec{a}}{\vec{a}\cdot(\vec{b}\times\vec{c})},\qquad \vec{c}'=\frac{\vec{a}\times\vec{b}}{\vec{a}\cdot(\vec{b}\times\vec{c})}.
$$



The denominator $V=\vec{a}\cdot(\vec{b}\times\vec{c})$ is the scalar triple product, equal to the signed volume of the parallelepiped with edges $\vec{a},\vec{b},\vec{c}$. The condition $V\neq 0$ is exactly the condition that the three vectors are non-coplanar; if $V=0$ the reciprocal set does not exist.

> **Definition (Kronecker delta characterization).** The reciprocal set is equivalently the unique set of vectors $\vec{b}_1,\vec{b}_2,\vec{b}_3$ satisfying



$$
\vec{a}_i\cdot\vec{b}_j=\delta_{ij}=\begin{cases}1, & i=j,\\ 0, & i\neq j.\end{cases}
$$



This characterization is the one most often quoted in marking schemes, because it converts the problem into a system of nine scalar equations in nine unknowns. Writing $A$ for the matrix whose rows are $\vec{a}_1,\vec{a}_2,\vec{a}_3$ and $B$ for the matrix whose rows are the reciprocal vectors, the condition $\vec{a}_i\cdot\vec{b}_j=\delta_{ij}$ is equivalent to the matrix equation $AB^{\mathsf{T}}=I$, hence $B^{\mathsf{T}}=A^{-1}$ and $B=(A^{-1})^{\mathsf{T}}$. This gives a second, purely algebraic route to the same answer and is an excellent independent check.

The cyclic structure of the definition is worth memorising as a rule: the numerator for the reciprocal of the first vector is the cross product of the second and third in cyclic order, and the denominator is always the same triple product. Cyclic order is $\vec{a}\to\vec{b}\to\vec{c}\to\vec{a}$; reversing the order of a cross product changes the sign and is a common source of lost marks.

## 3. Key Theorems & Essential Results

> **Theorem (Perfect matching).** If $\vec{a}',\vec{b}',\vec{c}'$ is the reciprocal set of $\vec{a},\vec{b},\vec{c}$, then



$$
\vec{a}'\cdot\vec{a}=1,\quad \vec{a}'\cdot\vec{b}=0,\quad \vec{a}'\cdot\vec{c}=0,
$$



> and similarly for $\vec{b}'$ and $\vec{c}'$.

*Justification.* Since $\vec{a}'$ is a scalar multiple of $\vec{b}\times\vec{c}$, and a cross product is orthogonal to each of its factors, $\vec{a}'\cdot\vec{b}=0$ and $\vec{a}'\cdot\vec{c}=0$. Also



$$
\vec{a}'\cdot\vec{a}=\frac{\vec{a}\cdot(\vec{b}\times\vec{c})}{\vec{a}\cdot(\vec{b}\times\vec{c})}=1.
$$



The other two cases follow by cyclic relabelling.

> **Theorem (Existence and uniqueness).** A reciprocal set exists if and only if $\vec{a}\cdot(\vec{b}\times\vec{c})\neq 0$, that is, if and only if the three vectors are non-coplanar. When it exists, it is unique.

*Justification.* Existence is exhibited by the explicit formula. Uniqueness follows from the Kronecker delta characterization: the nine conditions $\vec{a}_i\cdot\vec{b}_j=\delta_{ij}$ form a linear system whose coefficient matrix is the non-singular matrix $A$, so the solution is unique.

> **Theorem (Reciprocity is symmetric).** The original set is the reciprocal set of the reciprocal set; that is, the relation "is reciprocal to" is symmetric.

*Justification.* The defining dot-product pattern $\vec{a}_i\cdot\vec{b}_j=\delta_{ij}$ is symmetric in the two sets, so each set satisfies the defining conditions for the other, and uniqueness forces the conclusion.

> **Theorem (Volume reciprocity).** If $V=\vec{a}\cdot(\vec{b}\times\vec{c})$ and $V'=\vec{a}'\cdot(\vec{b}'\times\vec{c}')$, then $V'=1/V$.

*Justification.* Each reciprocal vector carries one factor of $1/V$, and the triple product is trilinear, so the three factors together contribute $1/V^{3}$ times the triple product of the three cross products, which equals $V^{2}$ by the vector triple product identity. Hence $V'=V^{2}/V^{3}=1/V$.

> **Theorem (Component extraction).** Any vector $\vec{r}$ can be written in the skew basis $\vec{a},\vec{b},\vec{c}$ as



$$
\vec{r}=(\vec{r}\cdot\vec{a}')\,\vec{a}+(\vec{r}\cdot\vec{b}')\,\vec{b}+(\vec{r}\cdot\vec{c}')\,\vec{c}.
$$



*Justification.* Dot the proposed expansion with $\vec{a}'$; by the perfect matching theorem only the first term survives, giving $\vec{r}\cdot\vec{a}'$ as the first coefficient. Repeat with $\vec{b}'$ and $\vec{c}'$. This result is the practical reason reciprocal sets are constructed and is the standard follow-up part of examination questions on this topic.

## 4. Worked Exemplar Problem with Step-by-Step Solution

**Problem.** Find a set of vectors reciprocal to the set



$$
\vec{a}=2\hat{\imath}+3\hat{\jmath}-\hat{k},\qquad \vec{b}=\hat{\imath}-\hat{\jmath}-2\hat{k},\qquad \vec{c}=-\hat{\imath}+2\hat{\jmath}+2\hat{k}.
$$



**Step 1: Compute the scalar triple product $V=\vec{a}\cdot(\vec{b}\times\vec{c})$.**

First form $\vec{b}\times\vec{c}$:



$$
\vec{b}\times\vec{c}=
\begin{vmatrix}
\hat{\imath} & \hat{\jmath} & \hat{k}\\
1 & -1 & -2\\
-1 & 2 & 2
\end{vmatrix}
=\hat{\imath}\big[(-1)(2)-(-2)(2)\big]-\hat{\jmath}\big[(1)(2)-(-2)(-1)\big]+\hat{k}\big[(1)(2)-(-1)(-1)\big].
$$



Evaluating each bracket:



$$
\vec{b}\times\vec{c}=\hat{\imath}(-2+4)-\hat{\jmath}(2-2)+\hat{k}(2-1)=2\hat{\imath}+0\hat{\jmath}+\hat{k}.
$$



Now dot with $\vec{a}$:



$$
V=\vec{a}\cdot(\vec{b}\times\vec{c})=(2)(2)+(3)(0)+(-1)(1)=4-1=3.
$$



Since $V=3\neq 0$, the vectors are non-coplanar and the reciprocal set exists.

**Step 2: Compute $\vec{c}\times\vec{a}$.**



$$
\vec{c}\times\vec{a}=
\begin{vmatrix}
\hat{\imath} & \hat{\jmath} & \hat{k}\\
-1 & 2 & 2\\
2 & 3 & -1
\end{vmatrix}
=\hat{\imath}\big[(2)(-1)-(2)(3)\big]-\hat{\jmath}\big[(-1)(-1)-(2)(2)\big]+\hat{k}\big[(-1)(3)-(2)(2)\big].
$$





$$
\vec{c}\times\vec{a}=\hat{\imath}(-2-6)-\hat{\jmath}(1-4)+\hat{k}(-3-4)=-8\hat{\imath}+3\hat{\jmath}-7\hat{k}.
$$



**Step 3: Compute $\vec{a}\times\vec{b}$.**



$$
\vec{a}\times\vec{b}=
\begin{vmatrix}
\hat{\imath} & \hat{\jmath} & \hat{k}\\
2 & 3 & -1\\
1 & -1 & -2
\end{vmatrix}
=\hat{\imath}\big[(3)(-2)-(-1)(-1)\big]-\hat{\jmath}\big[(2)(-2)-(-1)(1)\big]+\hat{k}\big[(2)(-1)-(3)(1)\big].
$$





$$
\vec{a}\times\vec{b}=\hat{\imath}(-6-1)-\hat{\jmath}(-4+1)+\hat{k}(-2-3)=-7\hat{\imath}+3\hat{\jmath}-5\hat{k}.
$$



**Step 4: Divide each numerator by $V=3$.**



$$
\vec{a}'=\frac{\vec{b}\times\vec{c}}{3}=\frac{2}{3}\hat{\imath}+\frac{1}{3}\hat{k},
$$





$$
\vec{b}'=\frac{\vec{c}\times\vec{a}}{3}=-\frac{8}{3}\hat{\imath}+\hat{\jmath}-\frac{7}{3}\hat{k},
$$





$$
\vec{c}'=\frac{\vec{a}\times\vec{b}}{3}=-\frac{7}{3}\hat{\imath}+\hat{\jmath}-\frac{5}{3}\hat{k}.
$$



**Step 5: Verify the perfect matching.** Check the diagonal entries:



$$
\vec{a}'\cdot\vec{a}=\frac{1}{3}\big[(2)(2)+(0)(3)+(1)(-1)\big]=\frac{1}{3}(4-1)=1,
$$





$$
\vec{b}'\cdot\vec{b}=\frac{1}{3}\big[(-8)(1)+(3)(-1)+(-7)(-2)\big]=\frac{1}{3}(-8-3+14)=1,
$$





$$
\vec{c}'\cdot\vec{c}=\frac{1}{3}\big[(-7)(-1)+(3)(2)+(-5)(2)\big]=\frac{1}{3}(7+6-10)=1.
$$



Check one off-diagonal entry:



$$
\vec{a}'\cdot\vec{b}=\frac{1}{3}\big[(2)(1)+(0)(-1)+(1)(-2)\big]=\frac{1}{3}(2-2)=0.
$$



The remaining off-diagonal entries vanish by the same orthogonality argument, so the set is correct.

**Second exemplar (shorter, for practice).** For



$$
\vec{a}=2\mathbf{i}-\mathbf{j}+\mathbf{k},\qquad \vec{b}=3\mathbf{i}+3\mathbf{j}+2\mathbf{k},\qquad \vec{c}=\mathbf{i}+2\mathbf{j}+\mathbf{k},
$$



the triple product is



$$
V=\vec{a}\cdot(\vec{b}\times\vec{c})=2(3-4)-(-1)(3-2)+1(6-3)=-2+1+3=2.
$$



The three cross products are



$$
\vec{b}\times\vec{c}=-\mathbf{i}-\mathbf{j}+3\mathbf{k},\qquad \vec{c}\times\vec{a}=-3\mathbf{i}+\mathbf{j}+5\mathbf{k},\qquad \vec{a}\times\vec{b}=-5\mathbf{i}-\mathbf{j}+9\mathbf{k},
$$



so the reciprocal set is



$$
\vec{a}'=-\frac{1}{2}\mathbf{i}-\frac{1}{2}\mathbf{j}+\frac{3}{2}\mathbf{k},\qquad \vec{b}'=-\frac{3}{2}\mathbf{i}+\frac{1}{2}\mathbf{j}+\frac{5}{2}\mathbf{k},\qquad \vec{c}'=-\frac{5}{2}\mathbf{i}-\frac{1}{2}\mathbf{j}+\frac{9}{2}\mathbf{k}.
$$



A quick check gives $\vec{a}'\cdot\vec{a}=\frac{1}{2}(-2+1+3)=1$, confirming the scale factor.

**Assessment-style task.** Find a set of vectors reciprocal to the set $\hat{\imath},\hat{\jmath},\hat{k}$. Because the standard basis is already orthonormal, the reciprocal set is the standard basis itself: each vector is perpendicular to the other two and has unit length, so $\hat{\imath}'=\hat{\imath}$, $\hat{\jmath}'=\hat{\jmath}$, $\hat{k}'=\hat{k}$. This is the degenerate "easy" case and is worth recognising instantly in an examination.

## 5. High-Yield Exam Takeaways & Common Pitfalls

**High-frequency question patterns.** The dominant pattern is a six-mark or five-mark question of the form "find a set of vectors reciprocal to the set $\vec{a},\vec{b},\vec{c}$" with explicit components. A second pattern embeds the definition in a longer question, for example asking for the volume of a parallelepiped first and then using that volume as the denominator of the reciprocal vectors. A third pattern asks you to state the defining dot-product conditions and then verify them, which is a proof-style variant of the same computation.

**Answer structure that earns full marks.** Present the work in four clearly labelled stages: (i) state the definition with the triple product in the denominator; (ii) compute the scalar triple product and explicitly note that it is non-zero; (iii) compute the three cross products in cyclic order; (iv) divide and state the final set. Finish with a one-line verification such as $\vec{a}'\cdot\vec{a}=1$. Marking schemes award marks separately for the triple product, for each cross product, and for the final division, so a single arithmetic slip early costs several marks; the verification line protects you by exposing the slip.

**Common pitfalls and traps.**

- Reversing a cross product. The numerator for $\vec{a}'$ is $\vec{b}\times\vec{c}$, not $\vec{c}\times\vec{b}$. Reversing introduces a spurious minus sign on the whole vector.
- Using the wrong denominator. The denominator is always the same triple product $\vec{a}\cdot(\vec{b}\times\vec{c})$ for all three reciprocal vectors; do not recompute a different triple product for each.
- Forgetting the non-coplanarity check. If the triple product is zero the reciprocal set does not exist, and stating this earns credit rather than losing it.
- Sign errors in the $\hat{\jmath}$ term of a determinant. The middle term of a $3\times 3$ determinant carries a minus sign; this is the single most frequent arithmetic error in this topic.
- Confusing the elementary reciprocal of a single vector with the reciprocal set. The single-vector reciprocal is $\vec{a}/\lVert\vec{a}\rVert^{2}$; the reciprocal set is a different construction involving cross products.
- Leaving the answer unnormalised or unverified. Always check at least one diagonal dot product equals $1$ and one off-diagonal equals $0$.

**Time-management strategy.** Budget roughly one minute for the triple product, one minute per cross product, and one minute for the division and check, giving about five to six minutes for a six-mark question. Compute the triple product first: if it is zero you can stop and state non-existence, saving time. Keep all three cross products in a single column of working so the common denominator is visually obvious and cannot be misapplied.

**Source-grounding note.** The definitions, the cyclic formula, the Kronecker delta characterization, and the assessment task on the standard basis all follow the approved lesson material; the worked exemplars and the verification strategy reflect the standard examination marking criteria for this topic.