[[1]]
### 1.7 Coordinate representation as a computational model

The introductory unit treats a vector geometrically as a directed segment and algebraically as a triple of real components. The two representations are equivalent in a rectangular coordinate system: the coordinates of the terminal point of a vector whose initial point is the origin are its components. A component is signed. It is the coefficient of one coordinate-axis unit vector, not an unsigned length.

This distinction explains why a vector is not in general determined by its magnitude alone. All vectors of a fixed nonzero magnitude lie on a sphere centred at the origin; they differ by direction. Conversely, specifying the three components fixes both magnitude and direction. A unit vector retains the direction of a nonzero vector but discards its original scale, which is why normalisation is a useful operation in later topics.

Vector addition is translation-invariant. If the tail of a representative arrow is moved, its components and vector value do not change. Therefore the graphical head-to-tail construction and the componentwise addition rule are not competing definitions: one describes the geometric resultant, and the other computes the same resultant in coordinates.

### 1.8 Component and geometric interpretations

For $A=(a_1,a_2,a_3)$, the component vectors are $a_1\hat i$, $a_2\hat j$, and $a_3\hat k$. Their sum is $A$. Since the coordinate axes are mutually perpendicular, the squared length is the sum of their squared component lengths. Thus the magnitude formula is a direct consequence of Euclidean distance, not an independent convention.

The position vector of $P(x,y,z)$ is $r=x\hat i+y\hat j+z\hat k$. If $P$ and $Q$ have position vectors $r_P$ and $r_Q$, then $\overrightarrow{PQ}=r_Q-r_P$. This follows from the chain relation $r_P+\overrightarrow{PQ}=r_Q$. It is a useful derivation because it fixes the subtraction order without relying on a picture.

### 1.9 Scope and progression

The first lesson's stated learning target is to find magnitude, unit vector, and resultant. Component representation, point displacement, and direction cosines provide precise tools for reaching that target. The algebra of these objects becomes input to the second lesson, where the dot product introduces angles and projections and the cross product introduces perpendicular directions. In this lesson, those product operations should not be used as shortcuts unless a later topic is explicitly being invoked.

[[2]]
### 2.10 Vector algebra in components

Let $A=(a_1,a_2,a_3)$, $B=(b_1,b_2,b_3)$, and let $\lambda$ be a real scalar. The component rules are

$$A+B=(a_1+b_1,a_2+b_2,a_3+b_3),\quad A-B=(a_1-b_1,a_2-b_2,a_3-b_3),\quad \lambda A=(\lambda a_1,\lambda a_2,\lambda a_3).$$

These rules follow from writing each vector in the basis $\{\hat i,\hat j,\hat k\}$ and collecting like basis directions. They also show that the zero vector is $(0,0,0)$ and that $-A=(-a_1,-a_2,-a_3)$ is the additive inverse. The laws of real-number addition then establish the vector identities component by component.

For example, the first component of $A+(B+C)$ is $a_1+(b_1+c_1)$, equal to $(a_1+b_1)+c_1$ by associativity of real addition. Repeating for the other components proves vector addition is associative. Similarly, $a_i+b_i=b_i+a_i$ for each index proves commutativity. This coordinate proof agrees with the geometric fact that changing the order in a head-to-tail chain does not change the final displacement.

### 2.11 Magnitude, direction, and normalization

For a nonzero vector $A$, write $r=\lVert A\rVert=\sqrt{a_1^2+a_2^2+a_3^2}$. The vector $\widehat A=A/r$ has magnitude

$$\lVert \widehat A\rVert=\sqrt{\frac{a_1^2+a_2^2+a_3^2}{r^2}}=1.$$

The restriction $A\ne0$ is essential. The zero vector has no direction, and the formula would divide by zero. A negative scalar multiple of $A$ has the opposite direction; a positive scalar multiple has the same direction. Normalizing a negative multiple therefore gives the negative unit vector, not the original unit vector.

The direction cosines are the components of $\widehat A$: $l=a_1/r$, $m=a_2/r$, $n=a_3/r$. Squaring and adding gives $l^2+m^2+n^2=1$. Conversely, if $r$ and the three direction cosines are known, then $A=r(l,m,n)$. This inverse relation is useful for converting between angular and component descriptions.

### 2.12 Vector between points and distance

If $P=(x_1,y_1,z_1)$ and $Q=(x_2,y_2,z_2)$, their position vectors are $r_P$ and $r_Q$. The displacement is

$$\overrightarrow{PQ}=r_Q-r_P=(x_2-x_1,y_2-y_1,z_2-z_1).$$

Its magnitude yields the distance formula. Reversing the points gives $r_P-r_Q=-\overrightarrow{PQ}$, and the norm is unchanged. The distinction between displacement and distance is important: displacement is a vector and depends on endpoint order, whereas distance is a nonnegative scalar and does not.

### 2.13 Direction-cosine consistency

If $A$ has direction angles $\alpha,\beta,\gamma$ with the positive axes, projection onto each axis gives $a_1=r\cos\alpha$, $a_2=r\cos\beta$, and $a_3=r\cos\gamma$. Squaring and summing yields

$$r^2(\cos^2\alpha+\cos^2\beta+\cos^2\gamma)=a_1^2+a_2^2+a_3^2=r^2.$$

For $r>0$, division by $r^2$ proves the direction-cosine identity. The proof explains why all three signed cosines are needed and why their squares—not their absolute values—form the normalization condition.

### 2.14 Resultants as coordinate sums

For a finite collection $A^{(1)},\ldots,A^{(n)}$, write the $i$th component of the $k$th vector as $a_i^{(k)}$. The resultant has components $\sum_{k=1}^{n}a_i^{(k)}$ for each coordinate index $i$. This compact form is simply repeated two-vector addition. It makes explicit that each component column is summed independently and that order can be changed without affecting the result.

The grouping of the sum can be chosen to reduce arithmetic risk. Pair vectors with opposite signs in a coordinate, then combine the partial sums. The algebra permits this regrouping by associativity and commutativity. It does not permit adding the magnitudes in place of components; magnitude is a nonlinear operation because of the square and square root. In general, $|A+B|$ is not $|A|+|B|$.

### 2.15 Connection between position coordinates and displacement

An absolute coordinate depends on the chosen origin, while a displacement between two fixed points does not depend on translating the entire coordinate system. If both position vectors are shifted by the same vector $c$, the difference becomes $(r_Q+c)-(r_P+c)=r_Q-r_P$. Thus the endpoint formula expresses a relative change and the common origin cancels.

This is why the vector between points is formed by subtraction rather than by adding their position vectors. The equation $r_P+\overrightarrow{PQ}=r_Q$ is the directed chain rule. It establishes both the subtraction order and its independence from how the points are positioned in the coordinate frame.

### 2.16 Direction angles and component projections

The angle a vector makes with an axis is determined by its projection on the corresponding unit vector. For example, the projection of $A$ on $\hat i$ is $a_1$, while its length is $r$. Consequently, $\cos\alpha=a_1/r$. The same reasoning gives the other two direction cosines. An angle with a positive axis is measured between zero and $180^\circ$; therefore its cosine can be negative, zero, or positive.

The signs of the three cosines locate the vector in a coordinate octant. Three positive cosines indicate positive projections on all axes. If exactly one is negative, the vector points opposite to that positive axis while retaining positive projections on the others. A zero cosine indicates a right angle to that axis, hence a zero component in that direction. This interpretation is more informative than treating direction cosines as three unrelated fractions.

### 2.17 Algebraic closure of vector addition

Component addition preserves the set of three-component vectors: adding two such vectors gives another three-component vector, and scalar multiplication does as well. This closure is why a long sum can be calculated entirely in components. The zero vector acts as the additive identity, and every vector has an additive inverse. These facts give the vector operations a consistent algebraic structure while remaining tied to directed geometry.

[[3]]
### 3.12 The resultant and the chain rule

For points $A,B,C$, the identity $\overrightarrow{AB}+\overrightarrow{BC}=\overrightarrow{AC}$ is the geometric chain rule. In coordinates, write the point vectors as $r_A,r_B,r_C$. The left side is $(r_B-r_A)+(r_C-r_B)$, and the intermediate $r_B$ terms cancel, leaving $r_C-r_A$. Thus the component sum equals the direct endpoint displacement. The cancellation explains why intermediate locations affect the route but not the final resultant.

For a closed chain, the final point is the initial point, so the endpoint difference is zero. This supplies a coordinate proof that the vector sum around a closed polygon is the zero vector. It does not imply the path length is zero; only the net displacement vanishes.

[[4]]
### 4.17 Worked example: combine vectors, then report three distinct quantities

Let $A=(2,4,-5)$ and $B=(1,2,3)$. The resultant is $R=(3,6,-2)$; its length is seven; its unit vector is $(3/7,6/7,-2/7)$. These outputs answer different requests. The first is a directed displacement, the second is a nonnegative scalar, and the third is a normalized directed vector. The direction cosines happen to equal the components of the unit vector, so they are the same triple in this case.

The sign in the third component should be explained if direction is being interpreted: $-2/7$ corresponds to an angle greater than $90^\circ$ with the positive third axis. The first two direction cosines are positive. As a consistency check their squares sum to one. The vector can also be recovered by multiplying the unit vector by its magnitude, which returns $(3,6,-2)$.

### 4.18 Worked example: derive a vector from its length and direction angles

Suppose a vector of length seven makes direction cosines $3/7$, $-2/7$, and $6/7$. Multiplying its length by the cosines gives components $(3,-2,6)$. The norm is $\sqrt{9+4+36}=7$. If an answer instead used $(3,2,6)$, it would have the right magnitude but the wrong orientation relative to the second axis. This illustrates why signs belong to direction data.

The angles could be recovered with inverse cosine if required. The second angle is obtuse because its cosine is negative. The first and third angles are acute because their cosines are positive. There is no need to evaluate these angles if the problem asks only for the vector or the direction cosines.

### 4.19 Worked example: separating path and displacement

A two-stage path has vectors $U=(5,0,0)$ and $V=(-2,0,0)$. Its resultant is $(3,0,0)$ with magnitude three, while the path length is $|U|+|V|=7$. The difference comes from partial cancellation along the common axis. If instead $V=(-5,0,0)$, the resultant is zero even though the path length is ten. These collinear examples make clear why adding magnitudes is not a general vector-sum operation.

For non-collinear addends, cancellation occurs separately in each component and the final vector need not align with either input. Component arithmetic remains exact; a diagram is a useful directional check rather than a replacement for it.

[[5]]
### 5.8 A compact answer audit

Before finalizing a vector-algebra solution, confirm that a vector answer has three ordered components, a magnitude is nonnegative, a unit vector has length one, and a point-to-point vector has the stated orientation. Check whether a direction cosine or an angle is requested; the two are related but are not the same form of answer. These checks cover the likely sources of lost accuracy without adding unrelated procedures.

### 5.9 A final consistency example

For $(3,-2,6)$, the norm is seven, not the sum of the components. The direction cosines are $(3/7,-2/7,6/7)$ and their squares sum to one. The vector itself has one negative component, its magnitude is positive, and its unit vector preserves the negative sign. Each statement follows from a different definition, so checking all of them is a concise way to ensure that the answer has not mixed scalar and vector data.
[[3]]
### 3.10 Deriving the squared-distance relation

Let $P$ and $Q$ have coordinate vectors $p$ and $q$. Their displacement is $d=q-p$. Since the coordinate basis is orthonormal, $d\cdot d$—interpreted componentwise as the sum of squared coordinates—equals $(x_2-x_1)^2+(y_2-y_1)^2+(z_2-z_1)^2$. Distance is the nonnegative square root of that quantity. Reversing the direction gives $-d$, but $(-d)\cdot(-d)=d\cdot d$, which proves the endpoint symmetry of distance.

### 3.11 Reconstructing the direction from cosines

The coordinate projections of a vector with magnitude $r$ are $rl$, $rm$, and $rn$. Hence $A=r(l,m,n)$. Its magnitude is

$$\sqrt{r^2l^2+r^2m^2+r^2n^2}=r\sqrt{l^2+m^2+n^2}=r,$$

provided $r>0$ and the cosines satisfy their identity. This proves that direction cosines and magnitude jointly recover the vector. The identity alone admits sign combinations, so orientation information remains necessary when components are reconstructed.

[[4]]
### 4.13 Worked example: the source resultant, with a proof check

Let $r_1=2\hat i+4\hat j-5\hat k$ and $r_2=\hat i+2\hat j+3\hat k$. Their sum is

$$R=(2+1)\hat i+(4+2)\hat j+(-5+3)\hat k=3\hat i+6\hat j-2\hat k.$$

Then $|R|=\sqrt{3^2+6^2+(-2)^2}=7$ and $\widehat R=(3/7)\hat i+(6/7)\hat j-(2/7)\hat k$. The reverse check $R-r_1=r_2$ confirms that the component sum is correct. The unit check gives $(9+36+4)/49=1$. This example combines the three stated target operations without confusing them.

### 4.14 Worked example: direction cosines including a negative projection

For $r=3\hat i-2\hat j+6\hat k$, the magnitude is $\sqrt{9+4+36}=7$. Its direction cosines are $3/7,-2/7,6/7$. The negative second cosine means the vector makes an obtuse angle with the positive $y$ axis. Squaring these values yields $9/49+4/49+36/49=1$.

If a question asks for the angles themselves, calculate $\alpha=\cos^{-1}(3/7)$, $\beta=\cos^{-1}(-2/7)$, and $\gamma=\cos^{-1}(6/7)$. Do not replace the negative cosine by its positive value; that would give an acute rather than an obtuse angle for $\beta$. A decimal angle is approximate and should be identified as such.

### 4.15 Worked example: a vector between coordinates and its magnitude

Let $P=(1,-2,3)$ and $Q=(4,2,-1)$. Then

$$\overrightarrow{PQ}=(4-1,2-(-2),-1-3)=(3,4,-4).$$

Its magnitude is $\sqrt{9+16+16}=\sqrt{41}$. The reverse vector is $(-3,-4,4)$ and has the same magnitude. The coordinate subtraction can be checked by adding the displacement to the initial position: $(1,-2,3)+(3,4,-4)=(4,2,-1)$, the required terminal point.

### 4.16 Worked example: solving for an unknown component

Suppose $A=(t,-3,4)$ is a vector of magnitude $\sqrt{50}$. Then $t^2+9+16=50$, so $t^2=25$ and $t=5$ or $t=-5$. Both choices produce the stated length. If the vector is also known to have a positive first direction cosine, then $t>0$ selects $t=5$. The magnitude condition alone cannot determine a sign because the norm is unchanged when a component sign is reversed.

This pattern is worth recognizing in examinations: translate a magnitude condition into a sum-of-squares equation, solve for the square, retain both roots, then apply any orientation condition. Substitution of both candidate values into the original norm provides a final check.

[[5]]
### 5.7 Limits of coordinate and direction data

Coordinates represent vectors relative to a specified basis. The simple magnitude formula depends on the axes being rectangular and unit directions being mutually perpendicular. If a problem changes the basis or describes oblique axes, the ordinary component-square formula must not be assumed without justification.

Direction cosines describe the orientation of a nonzero vector, but they do not supply its length. Multiplying all components by the same positive constant preserves the direction cosines while changing magnitude. Multiplying by a negative constant reverses all direction cosines. Therefore a complete answer must respond to both the scale and the orientation requested by the problem.
[[3]]
### 3.7 Proof of the magnitude and unit-vector results

The component vectors $a_1\hat i$, $a_2\hat j$, and $a_3\hat k$ are pairwise perpendicular because the coordinate axes are perpendicular. Apply the Pythagorean theorem to the first two components to obtain a planar diagonal of squared length $a_1^2+a_2^2$. This diagonal is perpendicular to the third component, so a second application gives

$$\lVert A\rVert^2=(a_1^2+a_2^2)+a_3^2.$$

Taking the nonnegative square root gives the magnitude formula. The derivation depends on a rectangular orthogonal coordinate system; in an oblique basis the component squares alone would not represent the Euclidean norm.

For $A\ne0$, define $\widehat A=A/\lVert A\rVert$. By homogeneity of length, $\lVert cA\rVert=|c|\lVert A\rVert$, so

$$\lVert\widehat A\rVert=\left\lVert\frac{A}{\lVert A\rVert}\right\rVert=\frac{\lVert A\rVert}{\lVert A\rVert}=1.$$

The denominator is positive because $A$ is nonzero. The direction is unchanged because the scaling factor is positive. These two claims are separate: magnitude one follows from scaling, while same direction follows from the sign of the scale factor.

### 3.8 Proof of the displacement relation

Let $r_P$ and $r_Q$ be the position vectors of $P$ and $Q$. The directed-segment chain begins at the origin, reaches $P$ by $r_P$, and then reaches $Q$ by $\overrightarrow{PQ}$. Therefore $r_P+\overrightarrow{PQ}=r_Q$. Subtracting $r_P$ from both sides gives $\overrightarrow{PQ}=r_Q-r_P$. This proof prevents a common endpoint-order error and generalizes immediately to any dimension where coordinates are used.

### 3.9 Triangle inequality as a diagnostic

The geometric triangle inequality states $\lVert A+B\rVert\le \lVert A\rVert+\lVert B\rVert$. It reflects the fact that the direct segment joining the start and finish of a two-step path cannot be longer than the path itself. Equality holds when the vectors are parallel in the same sense, or one vector is zero. For opposite collinear vectors, the magnitude of the sum is the difference of the lengths, not their sum.

This result is useful as a check on arithmetic. If a computed resultant is longer than the sum of the lengths of its addends, at least one component or magnitude has been calculated incorrectly. It is not a replacement for component addition because it provides only a bound, not the exact resultant.

[[4]]
### 4.9 Worked example: resultant of four component vectors

Let $A=(3,-2,1)$, $B=(-1,4,2)$, $C=(2,1,-5)$, and $D=(-3,-1,4)$. Compute $R=A+B+C+D$, its length, its unit vector, and its direction cosines.

First collect the first components: $3-1+2-3=1$. The second components give $-2+4+1-1=2$. The third components give $1+2-5+4=2$. Therefore $R=(1,2,2)$. The length is $r=\sqrt{1+4+4}=3$. The unit vector is $(1/3,2/3,2/3)$ and the direction cosines are the same three numbers.

Now verify the result independently. The unit vector's squared magnitude is $1/9+4/9+4/9=1$. The direction cosines also satisfy the identity. The resultant length is less than or equal to $|A|+|B|+|C|+|D|$, as it must be. Each check addresses a different stage: component addition, normalization, and geometric plausibility.

### 4.10 Worked example: endpoint order and distance

Take $P=(2,-3,1)$ and $Q=(-1,5,4)$. The directed vector from $P$ to $Q$ is

$$\overrightarrow{PQ}=(-1-2,5-(-3),4-1)=(-3,8,3).$$

The reverse is $(3,-8,-3)$. Its length, and hence the distance, is $\sqrt{9+64+9}=\sqrt{82}$. The displacement vector changes sign when the order changes, but distance does not. This is a useful opportunity to distinguish vector notation from scalar distance notation.

### 4.11 Worked example: recovering components from magnitude and direction

Suppose a vector has magnitude $6$ and direction cosines $1/3$, $-2/3$, and an unknown positive third cosine. The identity gives $n^2=1-1/9-4/9=4/9$. The stated positive orientation selects $n=2/3$, not $-2/3$. Thus the components are $6(1/3,-2/3,2/3)=(2,-4,4)$. Their magnitude is $\sqrt{4+16+16}=6$. If the sign of the third direction were not stated, two vectors would satisfy the same squared identity.

### 4.12 Worked example: testing a proposed unit vector

Consider $u=(2/3,-1/3,2/3)$. Its squared magnitude is $4/9+1/9+4/9=1$, so it is a unit vector. If $v=9u$, then $v=(6,-3,6)$, $|v|=9$, and normalizing $v$ returns $u$. If instead $v=-9u$, the magnitude is still nine but normalization gives $-u$. This confirms that magnitude alone does not determine orientation.

[[5]]
### 5.5 Separating related quantities

The most frequent conceptual confusion is between a path's total length, its resultant vector, and the resultant's magnitude. The resultant vector is signed component addition and preserves direction. Its magnitude is a nonnegative scalar. Total path length adds the lengths of each leg and disregards cancellation. These quantities agree only in special cases, such as a path made of vectors all pointing in the same direction.

Likewise, a position vector and a point are related but not identical concepts. A point is a location; its position vector is the directed segment from the chosen origin to that location. Changing the origin changes position vectors but does not change the displacement between fixed points. In coordinate exercises the origin is fixed, so the distinction is handled by explicitly naming the endpoints.

### 5.6 Domain limits and common errors

The formula for a unit vector requires a nonzero vector. The direction-cosine description also requires a nonzero magnitude. A vector diagram without a scale cannot determine a numerical magnitude. A three-dimensional magnitude formula assumes mutually perpendicular coordinate axes. Respecting these conditions keeps correct formulas from being misapplied.

When simplifying expressions, keep parentheses around components and endpoint differences. For example, $-2-5=-7$ while $-2-(-5)=3$; dropping the second pair of parentheses reverses a displacement component. Keep exact radicals when possible, and round only after the magnitude and any unit-vector components have been formed. Premature rounding can make the final direction cosines fail their unit identity by more than ordinary rounding error.

The useful stopping point for this topic is a complete component description of each vector, a verified resultant, and the requested magnitude or unit direction. Dot products, cross products, projections, and reciprocal sets build on these results but answer different questions; introducing them prematurely can obscure a straightforward vector-algebra solution.
