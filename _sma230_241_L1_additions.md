[[1]]
### 1.7 A careful reading of a vector drawing

A vector drawing carries more information than an ordinary line segment. If a diagram shows an arrow from point $P$ to point $Q$, the arrow is not merely the distance between the points. It records the directed change from the first point to the second. Reversing the arrow keeps the length but changes the direction. This distinction matters whenever a journey returns along the same road: walking east for three blocks and then west for three blocks gives zero net displacement, although the total distance travelled is six blocks. The resultant records the net directed effect, not the amount of path covered.

The scale of a drawing is a separate choice from the vector itself. A drawn arrow might be two centimetres long because the paper uses one centimetre for five metres, while the actual displacement has magnitude ten metres. A different drawing scale changes the picture length but not the represented displacement. Before measuring a diagram, read the scale; without it, the drawing gives direction and relative size, not a physical magnitude.

Position is also separate from vector equality. Two arrows at different locations can represent the same vector if both have equal length and point in the same direction. This freedom lets us slide an arrow without rotating or stretching it. It is the geometric reason the tip-to-tail addition method works: the second arrow may be translated until its initial point meets the first arrow's terminal point, while its vector value remains unchanged.

### 1.8 Choosing a coordinate description

The drawing is useful for seeing the operation, while components are useful for calculating it. In a rectangular three-dimensional coordinate system, the coordinate axes meet at right angles. The basic unit vectors point along the positive axes. The components tell how far the vector moves in each axis direction, with a negative component indicating movement opposite to the chosen positive direction.

A vector with components $(3,-2,4)$ means a movement of three units in the positive $x$ direction, two units in the negative $y$ direction, and four units in the positive $z$ direction. The three movements are combined, not performed as alternatives. If a point is given instead of a displacement, its position vector starts at the origin and ends at that point. Do not confuse the coordinates of a point with the vector joining two arbitrary points: the latter is found by subtracting the initial position from the terminal position.

There are two complementary ways to check component addition. First, combine the coordinates separately, since movements along different perpendicular axes do not interfere. Second, draw the arrows in a chain and check that the resulting direction is plausible. A graphical sketch will not generally give an exact length, but it can reveal a sign error. For example, adding a large westward component to a small eastward component should leave a westward resultant, not an eastward one.

### 1.9 Seeing why components simplify a drawing

Imagine trying to find the net change after walking through several streets that include turns north, south, east, west, up, and down a staircase. A sketch can become difficult to read, but the signed net change in each perpendicular direction remains easy to track. Vector components do exactly that: they keep a separate account for each coordinate direction. An eastward displacement and a westward displacement contribute to the same horizontal component with opposite signs; a vertical displacement contributes to a different component and cannot cancel the horizontal one.

The coordinate method does not erase the geometry. It records it in a form that can be added accurately. A positive first component means the arrow has a positive projection on the first axis; a negative first component means the projection points in the opposite direction. A zero component means the vector has no movement in that axis direction. The same interpretation applies to the second and third components.

When vectors are displayed on paper, it is easy to confuse an arrow's location with its value. A vector anchored at the origin and a matching arrow drawn elsewhere are equal if they have the same length and orientation. For addition, the arrow can be slid, but it cannot be reversed. Reversing it creates the negative vector. Sliding changes only the drawing location; reversing changes the mathematical object.

[[2]]
### 2.13 A two-dimensional check inside three-dimensional work

The formula for a planar vector is a special case of the three-dimensional one. If $A=(6,8,0)$, then $|A|=\sqrt{6^2+8^2+0^2}=10$. The zero third component says the vector lies in the coordinate plane. This is the familiar right-triangle calculation with legs six and eight and hypotenuse ten. In a spatial vector, the same reasoning is repeated with the third component: each coordinate direction is perpendicular to the plane made by the other two, so the resulting length satisfies the three-dimensional Pythagorean relation.

A negative component does not make the vector length negative. For $A=(6,-8,0)$ the length is still ten. The sign tells the direction of the projection along the second axis, while magnitude measures the total distance from the origin to the endpoint. These are different kinds of information, and the formula preserves the first only in the vector components while it squares signs away in the scalar magnitude.

### 2.14 Why the unit-vector formula preserves orientation

Dividing a nonzero vector by a positive number shortens or lengthens it without turning it. The magnitude of a vector is positive whenever the vector is nonzero, so the normalizing divisor is positive. For example, $A=(6,-8,0)$ is divided by ten to obtain $(3/5,-4/5,0)$. The second component remains negative, showing that the unit vector still points partly opposite to the positive second axis. Its length is $\sqrt{9/25+16/25}=1$.

The unit vector is not a new magnitude measurement; it is a direction written as a vector. It can later be used to express a direction independently of the size of a force or displacement. In this lesson it is enough to recognize its length and its preserved orientation.

[[3]]
### 3.10 A full verification of the resultant example

Use the vectors $r_1=(2,4,-5)$ and $r_2=(1,2,3)$. Their resultant is found by component addition: $R=(2+1,4+2,-5+3)=(3,6,-2)$. The squared magnitude is $9+36+4=49$, so $|R|=7$. The corresponding unit vector is $u=(3/7,6/7,-2/7)$.

The calculation can be checked in three independent ways. First, adding $R-r_1$ recovers $r_2$, because $(3,6,-2)-(2,4,-5)=(1,2,3)$. Second, the squared unit-vector components sum to $9/49+36/49+4/49=1$. Third, the third component is negative because the positive three contributed by $r_2$ did not fully cancel the negative five in $r_1$. These checks confirm both the arithmetic and its directional meaning.

[[4]]
### 4.12 Worked example: the familiar right-triangle magnitude

Let $b=(6,8)$. The endpoint lies six units along the first axis and eight along the second, so the vector forms the hypotenuse of a right triangle. Its magnitude is

$$|b|=\sqrt{6^2+8^2}=\sqrt{36+64}=10.$$

The unit vector in its direction is $b/10=(3/5,4/5)$. Its length is $\sqrt{9/25+16/25}=1$. This small example is a convenient check of the general method: if the component signs were changed to $(6,-8)$, the length would remain ten but the unit vector would point into a different quadrant.

### 4.13 Worked example: combining a resultant and a separate displacement

Suppose a person first moves by $A=(2,4,-5)$ and then by $B=(1,2,3)$. The net displacement is $R=(3,6,-2)$. The negative final component means the person ends below the initial height even though the second movement was upward: the upward contribution of three does not fully cancel the first downward contribution of five. The net distance from start to finish is $|R|=7$.

The route length is different. The first leg has length $\sqrt{4+16+25}=\sqrt{45}$ and the second has length $\sqrt{1+4+9}=\sqrt{14}$. The person travelled a path of length $\sqrt{45}+\sqrt{14}$, but the direct separation of endpoints is seven. The route length describes the full travel; the resultant magnitude describes the shortest straight displacement between endpoints. This contrast explains why one should not add lengths to find a vector resultant.

[[5]]
### 5.7 A practice check built from the definitions

For $A=(3,-2,6)$, the magnitude is seven and the direction cosines are $3/7,-2/7,6/7$. They satisfy the squared identity because $9+4+36=49$. For $B=(-3,2,-6)$, the magnitude is also seven, but each direction cosine has the opposite sign. The vectors have equal lengths and opposite directions. A question asking for magnitude cannot distinguish them; a question asking for the vector or its direction can.

This distinction between length and orientation is the most useful final check for the first lesson. Read the requested answer type before calculating: a scalar magnitude, a directed vector, a unit direction, or a distance. Each is related to the others, but none substitutes for the others.
[[2]]
### 2.10 Component arithmetic and the three-dimensional length

Let $A=(a_1,a_2,a_3)$ and $B=(b_1,b_2,b_3)$. Their sum is obtained by adding like components:

$$A+B=(a_1+b_1,\ a_2+b_2,\ a_3+b_3).$$

The reason is geometric: the total change along the first axis is the first change from $A$ followed by the first change from $B$, and the same statement applies independently to the other two axes. Subtraction is addition of the opposite vector:

$$A-B=(a_1-b_1,\ a_2-b_2,\ a_3-b_3).$$

If a real number $m$ multiplies a vector, every component is multiplied by $m$. A positive multiplier changes the length but preserves direction; a negative multiplier changes both the length scale and the sense. Multiplication by zero produces the zero vector, which has zero magnitude and no defined direction.

The magnitude follows by applying the Pythagorean theorem twice. In a plane, the first two perpendicular components have combined length $\sqrt{a_1^2+a_2^2}$. That horizontal-plane length is perpendicular to the third component, so the full length is

$$\lVert A\rVert=\sqrt{a_1^2+a_2^2+a_3^2}.$$

Squaring removes the square root: $\lVert A\rVert^2=a_1^2+a_2^2+a_3^2$. This squared form is often the convenient one when checking a unit vector or solving a condition. A magnitude cannot be negative, even when one or more components are negative, because the components are squared before they are added.

### 2.11 Unit vectors and direction cosines

For a nonzero vector $A$, its unit vector is $\widehat{A}=A/\lVert A\rVert$. This operation separates direction from length. Multiplying the original vector by $1/\lVert A\rVert$ scales its magnitude to one without changing its orientation. The zero vector has no unit vector because division by its magnitude would require division by zero and because it has no direction to preserve.

If a vector makes angles $\alpha$, $\beta$, and $\gamma$ with the positive coordinate axes, its direction cosines are $l=\cos\alpha$, $m=\cos\beta$, and $n=\cos\gamma$. For $A=(a_1,a_2,a_3)$ they are

$$l=\frac{a_1}{\lVert A\rVert},\qquad m=\frac{a_2}{\lVert A\rVert},\qquad n=\frac{a_3}{\lVert A\rVert}.$$

These are exactly the components of the unit vector. Since that vector has magnitude one, its components satisfy $l^2+m^2+n^2=1$. The signs carry directional meaning: an angle greater than $90^\circ$ with an axis has a negative cosine, so a negative component must not be changed to its absolute value.

### 2.12 Position vectors, displacement, and distance

Let the position vectors of points $P$ and $Q$ be $p$ and $q$. The directed vector from $P$ to $Q$ is $q-p$, because moving by $p$ reaches $P$ from the origin, and then adding the displacement $q-p$ reaches $Q$. In coordinates, for $P(x_1,y_1,z_1)$ and $Q(x_2,y_2,z_2)$,

$$\overrightarrow{PQ}=(x_2-x_1,\ y_2-y_1,\ z_2-z_1).$$

The order is important. Reversing the endpoints gives $\overrightarrow{QP}=-\overrightarrow{PQ}$. The distance between the points is the magnitude of either directed vector, so it is unchanged by reversing the order:

$$PQ=\sqrt{(x_2-x_1)^2+(y_2-y_1)^2+(z_2-z_1)^2}.$$

The coordinate differences must be squared as differences. It is incorrect to square each coordinate separately and then subtract the results.

[[3]]
### 3.7 Why the component rules agree with vector laws

The commutative law $A+B=B+A$ follows component by component. The first coordinate of either sum is $a_1+b_1=b_1+a_1$, and the same equality holds for the second and third coordinates. The order of placing arrows in a diagram therefore changes the route used to draw the sum but not the final resultant. The associative law follows similarly: each component of $A+(B+C)$ is $a_i+(b_i+c_i)$, which equals $(a_i+b_i)+c_i$ for ordinary real numbers.

The negative vector is $-A=(-a_1,-a_2,-a_3)$. Then $A+(-A)=(0,0,0)$, which explains algebraically why a closed tip-to-tail path has zero resultant. The magnitude check also agrees: $|-A|=|A|$ because squaring each sign removes it.

The direction-cosine identity can be derived directly rather than memorized. Substitute $l=a_1/r$, $m=a_2/r$, and $n=a_3/r$, where $r=\sqrt{a_1^2+a_2^2+a_3^2}$. Then

$$l^2+m^2+n^2=\frac{a_1^2+a_2^2+a_3^2}{r^2}=1.$$

This derivation also gives a diagnostic: if computed direction cosines do not satisfy the identity within rounding accuracy, then a component, magnitude, or sign has been mishandled.

### 3.8 What the magnitude formula does and does not mean

The formula for magnitude is the three-dimensional distance from the origin to the vector's endpoint. It depends on all three components, not on their sum. For example, components that partly cancel in a resultant are first added algebraically; only after the resultant components have been formed should the squares be added to find its length. Computing the magnitude of each vector first and adding those lengths would generally give the total path length rather than the magnitude of the resultant.

The triangle inequality describes the difference between these two quantities. The magnitude of a sum cannot exceed the sum of the magnitudes, because a bent path is at least as long as the straight resultant between its endpoints. Equality occurs when the vectors point in the same direction or one is zero. This statement is a useful reasonableness check, not a substitute for calculating the components.

[[4]]
### 4.9 Worked example: a three-dimensional resultant and its direction

Suppose three successive displacements are $A=(2,1,-1)$, $B=(-3,4,2)$, and $C=(1,-2,3)$. Find the resultant, its magnitude, and a unit vector in its direction.

**Step 1: Add corresponding components.** The first components give $2-3+1=0$. The second give $1+4-2=3$. The third give $-1+2+3=4$. Thus $R=A+B+C=(0,3,4)$. A sketch should show that the resultant has no $x$ component, positive $y$ and positive $z$ components.

**Step 2: Find the length after adding.** The resultant length is $|R|=\sqrt{0^2+3^2+4^2}=5$. Do not add $|A|$, $|B|$, and $|C|$; those lengths describe the total route, while $|R|$ describes the direct displacement from start to finish.

**Step 3: Normalize.** Divide each component by five: $\widehat R=(0,3/5,4/5)$. Its squared length is $0+9/25+16/25=1$, so it is a unit vector and has the same direction as $R$.

**Step 4: Interpret signs.** The zero component means the final displacement is perpendicular to the $x$ axis. Both remaining components are positive, so the vector points in the positive $y$ and positive $z$ directions. If one of those signs had been negative, taking absolute values during normalization would have pointed the answer into a different octant.

### 4.10 Worked example: vector and distance between two points

Take $P=(-2,1,3)$ and $Q=(4,-1,5)$. First find the vector directed from $P$ to $Q$:

$$\overrightarrow{PQ}=Q-P=(4-(-2),-1-1,5-3)=(6,-2,2).$$

The reverse vector is $\overrightarrow{QP}=(-6,2,-2)$, which is the negative of the first. Both have the same length:

$$PQ=\sqrt{6^2+(-2)^2+2^2}=\sqrt{44}=2\sqrt{11}.$$

Check the result in two ways. The length is positive, as a distance must be. Also, reversing the endpoints changed every component's sign but not the squares, so the distance remained unchanged. If a computation produces different distances for $PQ$ and $QP$, it contains an error.

### 4.11 Worked example: reconstructing a vector from direction data

Suppose a vector has magnitude ten and direction cosines $3/5$, $-4/5$, and $0$. The vector components are its magnitude times the direction cosines, so $A=(6,-8,0)$. Its length is $\sqrt{36+64}=10$, confirming the data. The negative second direction cosine indicates that the vector points opposite to the positive $y$ axis. The zero third cosine means it is perpendicular to the $z$ axis and lies in the $xy$ plane.

If instead a question supplies only two direction cosines, do not assume the third is zero. Use $l^2+m^2+n^2=1$ to find the possible magnitude of $n$, then determine its sign from the stated direction or diagram. Without a sign condition there can be two vectors reflected across the $xy$ plane.

[[5]]
### 5.5 Error diagnosis through the result

Several errors can be detected before an answer is submitted. A magnitude must be nonnegative; a unit vector must have length one; the distance from $P$ to $Q$ must equal the distance from $Q$ to $P$; and the components of a resultant must equal the signed component totals. These checks are directly tied to the definitions, rather than being arbitrary habits.

If the calculated unit vector has length two, the likely error is dividing by the squared magnitude rather than by the magnitude, or failing to divide every component. If its length is not one, recompute the original magnitude independently. If a resultant's direction contradicts the diagram, inspect negative components before changing any signs. If a point-to-point vector appears too large, verify endpoint order and subtraction before computing the distance.

### 5.6 A compact decision guide

When asked for a resultant, add components first and then decide whether the question also asks for its length or direction. When asked for a magnitude, use the sum of component squares and take the nonnegative square root. When asked for a unit vector, confirm that the original vector is nonzero and divide every component by the same magnitude. When asked for a vector between points, write terminal point minus initial point. When asked for a distance, take the magnitude of that difference. These distinctions keep related but different requests from being conflated.

The principal boundary of this lesson is that vector algebra provides the components, magnitudes, unit directions, and resultants used later for products; it does not yet use dot or cross products to measure angles or areas. A problem involving only addition, subtraction, scalar multiplication, and length should be completed with these methods. A problem asking for perpendicularity, a projection, or a plane normal belongs to the later dot-and-cross-product treatment.
