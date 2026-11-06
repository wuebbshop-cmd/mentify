## 1. Foundational Concepts, Definitions, and Axioms

Numerical integration is the process of approximating the value of a definite integral

$$
I=\int_{a}^{b}f(x)\,dx
$$

when the antiderivative of $f$ is unknown, difficult to obtain, or when $f$ is known only through a table of sampled values. The definite integral represents a signed area under the curve $y=f(x)$ between $x=a$ and $x=b$; numerical methods replace this exact area by the area of simpler geometric figures (trapezoids, parabolas, or weighted point evaluations) that can be computed from finitely many ordinates.

The indefinite integral of a function is another function (or a class of functions), whereas the definite integral over a fixed interval is a number. The two are linked by the Fundamental Theorem of Calculus: the definite integral can be computed by first finding an antiderivative $F(x)$ of $f(x)$ and then evaluating $F(b)-F(a)$. When this route is unavailable, quadrature formulae are used.

Every numerical integration result carries an error. The error is the difference between the exact value and the approximation, and it is quantified in absolute, relative, or percentage form. The central practical question is therefore twofold: how to construct a good approximation, and how to measure and control the error it introduces.

The principal elementary rules are the trapezoidal rule (joining successive ordinates by straight lines to form trapezia) and Simpson's rule (approximating the curve over pairs of strips by a parabola). The trapezoidal rule generally over-estimates the area for a convex curve, and the error can be reduced by using smaller strips, that is, by increasing the number of subintervals.

## 2. Theorems, Lemmas, and Analytical Properties

A quadrature rule replaces the exact integral by a weighted sum $Q[f]=\sum_i A_i f(x_i)$, where the $x_i$ are nodes and the $A_i$ are weights. Its error is $E[f]=I[f]-Q[f]$. The degree of exactness is the largest integer $m$ for which the rule integrates every polynomial of degree at most $m$ exactly, but fails for at least one polynomial of degree $m+1$. Exactness is a structural test of a rule; it does not mean that every non-polynomial integrand is integrated exactly.

The elementary equally spaced rules use geometry to choose their weights. The trapezoidal rule joins adjacent ordinates by straight segments. Simpson's one-third rule fits a quadratic through three consecutive ordinates and combines them with weights $1,4,1$; repeated application requires an even number of strips. Composite rules add contributions panel by panel, taking care not to omit shared endpoints or give the wrong coefficient to an interior ordinate. The rule definitions and the elementary derivation continue below.

### 2.3 The trapezoidal rule

Divide $[a,b]$ into $n$ equal strips of width

$$
h=\frac{b-a}{n},
$$

with ordinates $y_0,y_1,\dots,y_n$ at the equally spaced points $x_0=a,x_1,\dots,x_n=b$. Joining successive ordinates by straight lines produces trapezia, each of area $\tfrac{h}{2}(y_{i-1}+y_i)$. Summing gives the trapezoidal rule:

$$
\int_{a}^{b}f(x)\,dx\approx\frac{h}{2}\Bigl[y_0+2(y_1+y_2+\cdots+y_{n-1})+y_n\Bigr].
$$

The area obtained is generally an over-estimate for a convex curve, and the error is reduced by using smaller strips.

### 2.4 Simpson's rule

Simpson's rule estimates the area under a portion of a curve between $a$ and $b$ using three ordinates $y_0,y_1,y_2$. By translating the origin so that the middle ordinate sits at $x=0$, the curve over $[-h,h]$ is approximated by a parabola $y=ax^2+bx+c$, and the required area is

$$
\int_{-h}^{h}(ax^2+bx+c)\,dx.
$$

Carrying out the integration and expressing the result in terms of the three ordinates yields Simpson's rule:

$$
\int_{a}^{b}f(x)\,dx\approx\frac{h}{3}\Bigl[y_0+4y_1+y_2\Bigr],
$$

where $h$ is the width of each of the two equal strips. For a full interval divided into an even number of strips, the rule is applied pairwise and summed.

### 2.5 Error formulae

The maximum error in the trapezoidal rule satisfies a bound of the form

$$
\lvert E_T\rvert\le\frac{(b-a)}{12}h^{2}M_2,
$$

where $M_2$ is the maximum of $\lvert f''(x)\rvert$ on $[a,b]$.

The maximum error possible using Simpson's rule satisfies

$$
\lvert E_S\rvert\le\frac{(b-a)}{180}h^{4}M_4,
$$

where $M_4$ is the maximum of $\lvert f^{(iv)}(x)\rvert$ on $[a,b]$, with $f^{(iv)}$ denoting the fourth derivative.

### 2.6 Percentage error

The percentage error of an approximation $I_{\mathrm{approx}}$ relative to the exact value $I$ is

$$
\text{percentage error}=\frac{\lvert I-I_{\mathrm{approx}}\rvert}{\lvert I\rvert}\times 100\%.
$$

## 3. Formal Proofs, Derivations, and Methods

The results collected in this section are the working tools of numerical integration. Each result states an approximation rule together with the accuracy behaviour that governs it, so that the reader can see not only how an integral is approximated but also how quickly the approximation improves when the computation is refined. The final result records how errors already present in the input data are carried through an arithmetic operation.

> **Result (Fundamental Theorem of Calculus).** If $f$ is continuous on $[a,b]$ and $F$ is any function whose derivative equals $f$ on that interval, then the definite integral of $f$ over $[a,b]$ is the change in $F$ across the interval, namely the value of $F$ at the upper limit minus the value of $F$ at the lower limit.

$$
\int_{a}^{b} f(x)\,dx = F(b)-F(a), \qquad F'(x)=f(x) \ \text{for all} \ x \in [a,b].
$$

This statement is the exact route to an integral. Every quadrature rule is an attempt to reproduce the same number using only finitely many sampled values of $f$, without ever knowing an antiderivative. Consequently a quadrature rule can never be exact in general, and the whole subject is concerned with making the discrepancy small and predictable.

> **Result (Composite trapezoidal rule).** Divide $[a,b]$ into $n$ equal strips of common width $h=(b-a)/n$ and let $y_i=f(x_i)$ at the equally spaced nodes $x_i=a+ih$, for $i=0,1,\dots,n$. Then the integral is approximated by

$$
\int_{a}^{b} f(x)\,dx \approx \frac{h}{2}\Bigl[y_0+2\bigl(y_1+y_2+\cdots+y_{n-1}\bigr)+y_n\Bigr].
$$

The structure of the rule is easy to remember: the two end ordinates carry weight one, every interior ordinate carries weight two, and the whole bracket is multiplied by half the strip width. The name comes from the fact that over each strip the integrand is replaced by the straight line joining the two neighbouring ordinates, so the area of that strip is replaced by the area of a trapezium of parallel sides $y_{i-1}$ and $y_i$ and perpendicular height $h$; adding the $n$ strip areas and collecting repeated ordinates produces the formula above. When $n=1$ the rule collapses to the single-strip form

$$
\int_{x_0}^{x_1} f(x)\,dx \approx \frac{h}{2}\bigl(y_0+y_1\bigr),
$$

where $h$ is the width of that one strip.

> **Result (Composite Simpson's rule).** Take $n$ even, put $h=(b-a)/n$, and let $y_i=f(x_i)$ at the equally spaced nodes $x_i=a+ih$, for $i=0,1,\dots,n$. Then the integral is approximated by

$$
\int_{a}^{b} f(x)\,dx \approx \frac{h}{3}\Bigl[y_0+4\bigl(y_1+y_3+\cdots+y_{n-1}\bigr)+2\bigl(y_2+y_4+\cdots+y_{n-2}\bigr)+y_n\Bigr].
$$

The multiplier pattern is $1,4,2,4,2,\dots,4,1$ read from left to right: the two end ordinates carry weight one, the ordinates at odd indices carry weight four, the ordinates at even interior indices carry weight two, and the bracket is multiplied by one third of the strip width. The rule is built by grouping the strips in pairs and replacing the integrand on each pair by the quadratic that passes through the three ordinates at its ends and its midpoint. On a single pair of equal strips, with ordinates $y_0,y_1,y_2$ and common strip width $h$, the rule reduces to

$$
\int_{x_0}^{x_2} f(x)\,dx \approx \frac{h}{3}\bigl[y_0+4y_1+y_2\bigr].
$$

Because the pairing of strips is essential, the number of strips must be even; if an odd number is required, one strip is handled by the trapezoidal rule and the remainder by Simpson's rule.

> **Result (Polynomial exactness).** The trapezoidal rule reproduces exactly the integral of every polynomial of degree at most one on each strip, and therefore on the whole interval whenever the strip widths are equal. Simpson's rule reproduces exactly the integral of every polynomial of degree at most three on each pair of strips.

Polynomial exactness is the reason the two rules behave so differently on smooth integrands. The trapezoidal rule makes no allowance for curvature, so its error on a single strip is governed by how strongly the integrand bends, that is by its second derivative. Simpson's rule matches the integrand through a quadratic, yet it integrates cubics exactly as well, which means its leading error term is governed by the fourth derivative. A function that is well approximated by low-degree polynomials is therefore integrated almost perfectly by Simpson's rule, while the same function may still leave a noticeable trapezoidal discrepancy.

> **Result (Order of accuracy).** For a twice continuously differentiable integrand, the truncation error of the composite trapezoidal rule is a fixed multiple of $h^2$ times the largest value of $\lvert f''\rvert$ on $[a,b]$. For a four times continuously differentiable integrand, the truncation error of the composite Simpson rule is a fixed multiple of $h^4$ times the largest value of $\lvert f^{(iv)}\rvert$ on $[a,b]$. In the notation of asymptotic order, with $h \to 0$,

$$
E_T(h) = \mathcal{O}(h^{2}), \qquad E_S(h) = \mathcal{O}(h^{4}).
$$

The practical content of the result is a refinement ratio. Halving the strip width multiplies the trapezoidal truncation error by roughly one quarter, and multiplies the Simpson truncation error by roughly one sixteenth. Equivalently, multiplying the strip count by four (halving h) reduces the leading trapezoidal error by about a factor of four and the leading Simpson error by about a factor of sixteen. Those are respectively about 0.60 and 1.20 decimal digits of error reduction per halving of h, not two or four digits per hundredfold increase in strip count. The comparison follows from the orders h^2 and h^4, assumes the smoothness conditions behind those error terms, and describes truncation error rather than guaranteeing the same improvement after rounding or data errors dominate.

A word of caution belongs with this result. Reducing $h$ reduces truncation error but increases the number of ordinates, hence the number of arithmetic operations, hence the accumulated round-off error and the cost of evaluation. For very small $h$ the round-off contribution can dominate and the computed value stops improving or even deteriorates. The best choice of $h$ is therefore a compromise between truncation error, which decreases as $h$ shrinks, and round-off error, which grows as $h$ shrinks.

> **Result (Propagation of errors in arithmetic).** Let $x$ and $y$ be exact numbers and let $x^{*}$ and $y^{*}$ be approximations to them with initial errors $\varepsilon$ and $\eta$ respectively, so that $x=x^{*}+\varepsilon$ and $y=y^{*}+\eta$. For an exact operation $\omega$ and its computational version $\omega^{*}$, the total discrepancy splits into two parts,

$$
x\,\omega\,y - x^{*}\,\omega^{*}\,y^{*}
= \bigl(x\,\omega\,y - x^{*}\,\omega\,y^{*}\bigr) + \bigl(x^{*}\,\omega\,y^{*} - x^{*}\,\omega^{*}\,y^{*}\bigr),
$$

where the first bracket is the propagated error, that is the part of the discrepancy caused by the initial errors $\varepsilon$ and $\eta$ being carried through the operation, and the second bracket is the generated error, that is the part introduced by performing the operation itself in finite arithmetic. The two together constitute the accumulated error at that stage of the computation.

The distinction matters in quadrature because a quadrature formula is a long chain of additions and multiplications. Each ordinate $y_i$ is itself an approximation obtained from the integrand, so it carries an initial error; the weighted sum then propagates those errors and adds fresh rounding at every step. The analysis of a composite rule therefore has two separate strands, the truncation error of the formula and the accumulated round-off of its evaluation, and a reliable numerical answer must control both.

## 4. Representative Worked Examples and Solutions

### Problem

Evaluate

$$
I=\int_{0}^{6}\frac{dx}{1+x^{2}}
$$

using (i) the trapezoidal rule and (ii) Simpson's one-third rule with $h=1$. Then evaluate the exact integral by direct integration correct to five decimal places and find the percentage error in each approximation.

### Step 1: Tabulate the ordinates

With $h=1$ and $x=0,1,2,3,4,5,6$, the integrand is $f(x)=\dfrac{1}{1+x^{2}}$:

| $x$ | $0$ | $1$ | $2$ | $3$ | $4$ | $5$ | $6$ |
|---|---|---|---|---|---|---|---|
| $f(x)$ | $1.00000$ | $0.50000$ | $0.20000$ | $0.10000$ | $0.05882$ | $0.03846$ | $0.02703$ |

### Step 2: Trapezoidal rule

$$
\begin{aligned}
I_T&=\frac{h}{2}\Bigl[y_0+2(y_1+y_2+y_3+y_4+y_5)+y_6\Bigr]\\
&=\frac{1}{2}\Bigl[1.00000+2(0.50000+0.20000+0.10000+0.05882+0.03846)+0.02703\Bigr]\\
&=\frac{1}{2}\Bigl[1.00000+2(0.89728)+0.02703\Bigr]\\
&=\frac{1}{2}\bigl[2.82159\bigr]\\
&=1.41080.
\end{aligned}
$$

### Step 3: Simpson's one-third rule

With six strips (an even number), apply the rule pairwise:

$$
\begin{aligned}
I_S&=\frac{h}{3}\Bigl[(y_0+y_6)+4(y_1+y_3+y_5)+2(y_2+y_4)\Bigr]\\
&=\frac{1}{3}\Bigl[(1.00000+0.02703)+4(0.50000+0.10000+0.03846)+2(0.20000+0.05882)\Bigr]\\
&=\frac{1}{3}\Bigl[1.02703+4(0.63846)+2(0.25882)\Bigr]\\
&=\frac{1}{3}\Bigl[1.02703+2.55384+0.51764\Bigr]\\
&=\frac{1}{3}\bigl[4.09851\bigr]\\
&=1.36617.
\end{aligned}
$$

### Step 4: Exact value by direct integration

Since $\dfrac{d}{dx}\arctan x=\dfrac{1}{1+x^{2}}$,

$$
\begin{aligned}
I&=\int_{0}^{6}\frac{dx}{1+x^{2}}\\
&=\bigl[\arctan x\bigr]_{0}^{6}\\
&=\arctan 6-\arctan 0\\
&=1.40565-0\\
&=1.40565.
\end{aligned}
$$

### Step 5: Percentage errors

For the trapezoidal rule:

$$
\begin{aligned}
\text{percentage error}&=\frac{\lvert I-I_T\rvert}{\lvert I\rvert}\times 100\%\\
&=\frac{\lvert 1.40565-1.41080\rvert}{1.40565}\times 100\%\\
&=\frac{0.00515}{1.40565}\times 100\%\\
&\approx 0.366\%.
\end{aligned}
$$

For Simpson's rule:

$$
\begin{aligned}
\text{percentage error}&=\frac{\lvert I-I_S\rvert}{\lvert I\rvert}\times 100\%\\
&=\frac{\lvert 1.40565-1.36617\rvert}{1.40565}\times 100\%\\
&=\frac{0.03948}{1.40565}\times 100\%\\
&\approx 2.809\%.
\end{aligned}
$$

### Step 6: Interpretation

The trapezoidal approximation exceeds the exact value, consistent with the over-estimate expected for a convex decreasing curve. Simpson's rule is markedly more accurate on smooth integrands in general, but on this interval the integrand changes curvature rapidly near $x=0$, so the coarse step $h=1$ produces a larger Simpson discrepancy; refining $h$ reduces both errors, with the Simpson error falling faster because it is governed by $h^{4}$.

### Additional exemplar: range of a rounded expression

To obtain the range within which

$$
\frac{1.265(10.21-7.57)}{47}
$$

lies when all quantities are rounded off, note that a number quoted to $k$ decimal places has absolute error at most $0.5\times 10^{-k}$. Thus $1.265$ carries error $\pm 0.0005$, the quantities $10.21$ and $7.57$ carry error $\pm 0.005$, and $47$ carries error $\pm 0.5$. The propagated error of the product and quotient is then obtained by combining these initial errors through the arithmetic operations, giving the interval of possible exact values.

### 4.1 Deriving the composite trapezoidal weights

On one panel $[x_{i-1},x_i]$ of width $h$, the trapezoid has area $\frac{h}{2}(y_{i-1}+y_i)$. Summing this expression for $i=1,\ldots,n$ gives

$$
T_n=\frac{h}{2}\sum_{i=1}^n(y_{i-1}+y_i).
$$

The first ordinate occurs only in the first panel and the final ordinate only in the last panel. Each interior ordinate is shared by the panel on its left and the panel on its right, so it appears twice. Collecting like terms yields

$$
T_n=\frac{h}{2}\left[y_0+2\sum_{i=1}^{n-1}y_i+y_n\right].
$$

This derivation explains the weight pattern rather than asking the reader to memorize it. It also exposes a useful arithmetic check: when $n=1$, the interior sum is empty and the formula reduces to the area of a single trapezoid. When $n=2$, only $y_1$ is doubled.

For $f(x)=x^2$ on $[0,1]$ with $n=2$, $h=0.5$ and the values are $0,0.25,1$. Thus

$$
T_2=\frac{0.5}{2}\left[0+2\left(\frac{1}{16}\right)+1\right]=0.28125.
$$

Since the exact integral is $1/5$, the actual error is $0.08125$. With four strips, the composite estimate is $0.220703125$, whose error is $0.020703125$. The error ratio is about $0.255$, close to the predicted quarter but not exactly one quarter because higher-order terms also contribute. The example illustrates why an error-order claim must be checked against the actual rule and data rather than inferred from one pair of rounded estimates.

### 4.2 Deriving Simpson’s one-third weights

Translate the midpoint of two equal strips to the origin and use nodes $-h,0,h$ with values $y_0,y_1,y_2$. The quadratic passing through them has the Lagrange representation

$$
p(x)=y_0\frac{x(x-h)}{2h^2}
-y_1\frac{(x+h)(x-h)}{h^2}
+y_2\frac{x(x+h)}{2h^2}.
$$

Integrating each basis function from $-h$ to $h$ gives weights $h/3$, $4h/3$, and $h/3$. Therefore

$$
\int_{-h}^{h}f(x)\,dx\approx\int_{-h}^{h}p(x)\,dx
=\frac{h}{3}(y_0+4y_1+y_2).
$$

The odd basis component integrates to zero by symmetry, which is why the midpoint receives the largest coefficient. Applying this panel formula to pairs and collecting shared endpoints yields the composite pattern $1,4,2,\ldots,4,1$.

The integral of any cubic also agrees with this weighted expression, even though the fitted curve is quadratic. The odd cubic part integrates symmetrically to zero, while the even terms are reproduced by the fitted quadratic. This gives Simpson’s rule degree of exactness three and explains why its leading error for a sufficiently smooth integrand involves the fourth derivative rather than the third.

### 4.3 Interpreting refinement quantitatively

If the composite trapezoidal error behaves like $C_T h^2$, replacing $h$ by $h/2$ gives an error near $C_T h^2/4$. The reduction factor is four, and the number of correct decimal digits increases by approximately

$$
\log_{10}(4)\approx0.602.
$$

For Simpson’s rule, an error behaving like $C_S h^4$ changes by a factor $1/16$ under the same halving. The digit gain is approximately $\log_{10}(16)\approx1.204$. These are logarithmic interpretations of error ratios, not statements that a method suddenly adds exactly one or two correct digits.

Equivalently, halving $h$ doubles the panel count. Increasing the panel count by a factor of four is needed to halve $h$, so the error reductions just described correspond to quadrupling the number of strips, not merely multiplying it by one hundred. The claim is about the leading truncation term under smoothness assumptions. Round-off, measurement error, and implementation error can limit observed gains.

An estimator can use the coarse and fine trapezoidal results to infer the leading error when the asymptotic regime is credible. If $T(h)=I+Ch^2+\cdots$ and $T(h/2)=I+Ch^2/4+\cdots$, then subtracting appropriately cancels the leading term:

$$
R=\frac{4T(h/2)-T(h)}{3}.
$$

For $x^2$ on $[0,1]$, $T(1)=0.5$ and $T(0.5)=0.375$, so $R=(4(0.375)-0.5)/3=1/3$, the exact integral. This is a simple Richardson or first Romberg extrapolation check; exactness here follows from the quadratic error structure and should not be assumed for every integrand.

### 4.4 A quadrature rule with selected nodes

Gaussian quadrature chooses nodes and weights to integrate a high-degree polynomial exactly with relatively few function evaluations. For the two-point Gauss–Legendre rule on $[-1,1]$, the nodes are $-1/\sqrt{3}$ and $1/\sqrt{3}$, each with weight one:

$$
\int_{-1}^{1}f(x)\,dx\approx
f\left(-\frac{1}{\sqrt3}\right)+
f\left(\frac{1}{\sqrt3}\right).
$$

The rule integrates every polynomial through degree three exactly. It integrates $1$ to $2$, $x$ to $0$, $x^2$ to $2/3$, and $x^3$ to $0$, matching their exact integrals on the symmetric interval. These four checks determine the two equal weights and the squared node location. For an arbitrary interval $[a,b]$, transform the variable from $[-1,1]$ and include the scale factor $(b-a)/2$.

The selected nodes are generally not the endpoints or equally spaced points. This is an advantage when function evaluations are expensive and the integrand is smooth, but it may be unsuitable when only a fixed equally spaced table is supplied. A Gaussian rule must not be applied to tabulated points as if they were its required nodes; either evaluate the function at the selected nodes or choose a rule compatible with the available data.

### 4.5 Separating truncation error from other uncertainty

The classical error orders describe truncation error due to replacing the integral by a quadrature formula. If the ordinates are rounded, their errors enter through the weighted sum. For the composite trapezoidal rule, an error $\eta_i$ in ordinate $y_i$ changes the estimate by

$$
\Delta T=\frac{h}{2}\left[\eta_0+2\sum_{i=1}^{n-1}\eta_i+\eta_n\right].
$$

Thus a fine mesh reduces the ideal smooth-function truncation error but can increase the number of rounded values contributing to data uncertainty. A numerical answer should not claim the theoretical $h^2$ or $h^4$ reduction for the total error unless representation and data errors are controlled as well.

For an unknown integral, compare successive estimates and state whether they stabilize. If a derivative maximum is available, quote the corresponding theoretical bound. If only a table is known, do not claim a rigorous maximum error from a convergence pattern alone. These distinctions keep the final precision aligned with the actual evidence.

### 4.1 Why Richardson cancellation works

The Romberg idea can be derived directly from a smooth error expansion. Suppose the composite trapezoidal result has the form

$$
T(h)=I+c_2h^2+c_4h^4+\cdots,
$$

where $I$ is the exact integral and the coefficients depend on the integrand and interval. Halving the step gives

$$
T(h/2)=I+\frac{c_2h^2}{4}+\frac{c_4h^4}{16}+\cdots.
$$

Multiplying the refined estimate by four and subtracting the coarse estimate cancels the $c_2h^2$ term. Dividing by three normalizes the coefficient of $I$, which produces

$$
R_1(h)=\frac{4T(h/2)-T(h)}{3}.
$$

The first surviving error term is proportional to $h^4$. Applying the same idea to successive columns creates higher-order extrapolated values. The denominators $4^j-1$ arise because halving $h$ scales an $h^{2j}$ term by $4^{-j}$.

This reasoning is asymptotic. It assumes the function is smooth enough for the even-power error expansion and that the step is sufficiently small for the leading terms to describe the observed sequence. A coarse initial table, a derivative discontinuity, endpoint behavior outside the smoothness assumptions, or rounded data can prevent the predicted cancellation from appearing clearly.

### 4.2 Evaluating a Gaussian formula by exactness

The three-point Gauss–Legendre rule on $[-1,1]$ uses nodes $-\sqrt{3/5},0,\sqrt{3/5}$ and weights $5/9,8/9,5/9$. It integrates every polynomial through degree five exactly. The exactness can be checked by symmetry and moment calculations: odd powers integrate to zero because both the symmetric interval and the weighted nodes are symmetric; the even moments through degree four agree with the exact integral.

For $x^4$ on $[0,1]$, map the standard variable $t$ by $x=(1+t)/2$, so the integration scale is $1/2$. The transformed quadrature is

$$
\frac12\left[
\frac59\left(\left(\frac{1-\sqrt{3/5}}2\right)^4+
\left(\frac{1+\sqrt{3/5}}2\right)^4\right)
+\frac89\left(\frac12\right)^4
\right].
$$

Because $x^4$ has degree four, this expression equals its exact integral $1/5$. The example verifies the interval scale and the selected weights. If the scale factor $1/2$ were omitted, the result would be twice as large, an error immediately exposed by comparing with the exact integral.

Polynomial exactness is a property of the quadrature rule, not a claim that every smooth function is integrated exactly. For a non-polynomial integrand, the rule can still be accurate, but a separate error estimate or refinement check is needed. The chosen nodes also matter: if the problem gives only an equally spaced table, the values at Gauss nodes may be unavailable.

### 4.3 A local error budget for a quadrature result

For a complete numerical integral, distinguish at least three contributions: quadrature truncation error, uncertainty in function values, and arithmetic error in the weighted sum. The theoretical trapezoidal and Simpson bounds address the first contribution under derivative assumptions. They do not automatically include rounded or measured ordinates.

If each ordinate in a composite rule is known only within a bound $\epsilon_i$, the effect on the weighted sum can be bounded by summing the absolute weights times those bounds. For the composite trapezoidal formula this is

$$
|\Delta T|\le\frac{h}{2}
\left(\epsilon_0+2\sum_{i=1}^{n-1}\epsilon_i+\epsilon_n\right).
$$

The larger interior weights mean that interior data errors contribute twice as strongly as endpoint errors of the same size. For Simpson’s formula, use its own weights and the factor $h/3$. This data term may remain unchanged or even become more prominent as the mesh is refined.

Do not combine a theoretical truncation bound with a rounded-data uncertainty and then report the result as though the theorem alone covered the total. State each contribution and the conservative way they are combined. If the ordinate errors are random with a stated probability model, statistical propagation may be appropriate, but a probability model should never be assumed without evidence.

### 4.4 Diagnosing a refinement sequence

A refinement sequence should be audited for both arithmetic and mathematical behavior. For nested trapezoidal grids, every old node is retained and exactly one new midpoint is inserted in each old panel. The recurrence must therefore evaluate $n$ new points when refining from $n$ to $2n$ strips. An endpoint counted among those midpoints or a coefficient using the wrong half-width introduces a systematic error.

The observed ratios of successive errors, when the exact integral is known, can test the expected order. If the trapezoidal error ratio after halving $h$ is near four and the Simpson ratio near sixteen, the computations are consistent with their leading orders. If not, possibilities include a coarse pre-asymptotic grid, incorrect weights, a nonsmooth integrand, rounding, or a dominant data error. A mismatch is a diagnostic to investigate, not proof that the theoretical formula is false.

When the exact value is unknown, successive diagonal differences in a Romberg table can indicate stabilization. They remain empirical indicators. A strong answer reports the actual sequence or differences, names the assumptions behind the extrapolation, and avoids claiming a guaranteed tolerance unless a bound is available.

### 4.5 Reporting a result at defensible precision

For each quadrature computation, record the interval, step width, strip count, ordinates, rule, and final weighted sum. For Simpson’s one-third rule, make the even-strip requirement visible and label the coefficient pattern. For Gaussian quadrature, state the standard nodes and weights, the interval transformation, and the scale factor. For Romberg, label the trapezoidal column and each extrapolation column so the reader can tell which entry is being reported.

Keep extra digits in intermediate sums and round once at the end. If the exact integral is known, report the actual absolute or percentage error. If a derivative maximum yields an error bound, state its smoothness hypothesis and its maximum value. If only refinement evidence is available, describe the observed agreement rather than converting it into an unsupported certainty claim.

The key quantitative refinement facts are easy to check through logarithms. A factor of four decrease in trapezoidal error is about $\log_{10}(4)=0.60$ decimal digits; a factor of sixteen decrease in Simpson error is about $\log_{10}(16)=1.20$ digits. These are gains per halving of $h$, equivalently per fourfold increase in strip count. They are not two or four digits per hundredfold increase in strip count, and they describe truncation error under the stated assumptions.

### 4.6 Checking an error bound on a known integral

For $f(x)=x^4$ on $[0,1]$, the exact integral is $1/5=0.2$. With two strips, $h=0.5$ and the trapezoidal values are $0,1/16,1$. The estimate is $T_2=0.375$, so the actual error is $0.175$. Since $f''(x)=12x^2$ and $M_2=12$ on the interval, the composite trapezoidal bound is

$$
|E_T|\le\frac{(b-a)}{12}h^2M_2
=\frac{1}{12}(0.25)(12)=0.25.
$$

The actual error is below the bound. The bound is conservative because it uses the maximum curvature across the entire interval, not the curvature at one representative point.

Simpson’s one-third estimate with the same two strips is $S_2=5/24\approx0.20833$, so its actual error is $1/120\approx0.00833$. Here $f^{(4)}=24$, and the composite Simpson bound is

$$
|E_S|\le\frac{(b-a)}{180}h^4M_4
=\frac{1}{180}(0.5)^4(24)=\frac{1}{120}.
$$

The bound happens to equal the actual error because the leading error expression is exact for this quartic case. In other problems, an upper bound need not be attained. This comparison illustrates both the value and the limitation of an error theorem: it guarantees an enclosure under its hypotheses, but it does not generally predict the exact signed error.

### 4.7 Turning a tolerance into a panel count

If a problem asks for an error no larger than $\varepsilon$, use the relevant derivative bound to solve for $h$ before computing ordinates. For the composite trapezoidal rule,

$$
\frac{(b-a)}{12}h^2M_2\le\varepsilon
$$

implies

$$
h\le\sqrt{\frac{12\varepsilon}{(b-a)M_2}}.
$$

Since $n=(b-a)/h$ must be an integer, choose a panel count large enough to satisfy the inequality and then check any rule-specific restrictions. For Simpson’s rule, the corresponding $h^4$ inequality produces a fourth-root condition and $n$ must be even. Do not round the panel count down; doing so may violate the requested bound.

This design calculation depends on a valid maximum derivative. If the bound is too loose, the chosen panel count may be conservative. If the required derivative bound is unavailable, the tolerance cannot be guaranteed from the formula alone; refinement comparisons may guide a practical choice but must be labeled as empirical.

### 4.8 Interpreting mesh refinement in decimal terms

The order $O(h^p)$ describes how the leading truncation error scales as the mesh becomes fine. If $h$ is halved, $h^2$ is divided by four and $h^4$ by sixteen. Converting those ratios into base-ten digit changes gives

$$
\log_{10}(4)\approx0.60,\qquad
\log_{10}(16)\approx1.20.
$$

Thus a halving of $h$ corresponds to about six-tenths of a decimal digit for trapezoidal error and about 1.2 digits for Simpson error in the asymptotic regime. Because halving $h$ doubles the number of strips, a fourfold strip-count increase is needed to halve the width. The digit gains are per width-halving, not per arbitrary increase in strip count.

If the strip count instead grows by a factor of one hundred, $h$ is reduced by a factor of one hundred. The leading errors then change by $10^{-4}$ for trapezoidal and $10^{-8}$ for Simpson, corresponding to four and eight decimal digits only in the ideal asymptotic truncation term. This is a different comparison from one halving, and it still does not guarantee that total error gains those digits when round-off or input noise dominates.

## 5. Mathematical Extensions, Limits, and Common Errors

- Always state the exact value obtained by direct integration before computing any percentage error; the percentage error is meaningless without the exact reference value.
- For the trapezoidal rule, the end ordinates are counted once and all interior ordinates are doubled; for Simpson's rule, ordinates are weighted $1,4,2,4,2,\dots,4,1$ and the whole sum is multiplied by $h/3$.
- Simpson's one-third rule requires an even number of strips; if the tabulation gives an odd number, the rule cannot be applied directly across the whole interval.
- The trapezoidal rule over-estimates the area for a convex curve; the error is reduced by using smaller strips, that is, a larger $n$.
- Distinguish clearly between inherent error (present in the initial data), propagated error (arising in the result of an operation from initial errors), generated error (introduced by the operation itself), and accumulated error (the running total).
- Absolute error is $\lvert x-x_r\rvert$; relative error divides this by $\lvert x\rvert$; percentage error multiplies the relative error by $100\%$. A number correct to $n$ decimal places has absolute error at most $0.5\times 10^{-n}$.
- When a quantity is quoted to $k$ decimal places, its true value lies in a symmetric interval of half-width $0.5\times 10^{-k}$; use these intervals to bound the exact value of a compound expression.
- Do not confuse the strip width $h=(b-a)/n$ with the number of strips $n$; the error bounds depend on $h^{2}$ for the trapezoidal rule and $h^{4}$ for Simpson's rule.
- Quote final numerical answers to the precision demanded by the question (for example, five decimal places) and carry full precision through intermediate steps to avoid unnecessary round-off contamination.

### Lessons 9?10: refinement, extrapolation, and selected nodes
Composite refinement produces trapezoidal estimates at successively halved step widths. If $T_{2^k}$ denotes the estimate using $2^k$ panels, the first Romberg extrapolation is

$$R_{k,1}=T_{2^k}+\frac{T_{2^k}-T_{2^{k-1}}}{3}.$$

This combination cancels the leading $h^2$ term under the smoothness assumptions used in the error expansion. Higher columns continue the cancellation:

$$R_{k,j}=R_{k,j-1}+\frac{R_{k,j-1}-R_{k-1,j-1}}{4^j-1}.$$

The denominator follows from how an $h^{2j}$ term changes under halving. The triangular table should be filled from the two entries directly above the new entry; a numerical result must not be copied from the wrong row or column. Refinement improves the truncation component while the number of function evaluations and arithmetic operations grows.

The three-point Gauss–Legendre rule on $[-1,1]$ is

$$\int_{-1}^{1}f(t)\,dt\approx \frac{5}{9}f(-\sqrt{3/5})+\frac{8}{9}f(0)+\frac{5}{9}f(\sqrt{3/5}).$$

It is exact through degree five. For an interval $[a,b]$, use $x=m+dt$, with $m=(a+b)/2$ and $d=(b-a)/2$; the transformed integral includes the multiplier $d$. This is an example of a rule with non-equally-spaced nodes, unlike Newton–Cotes formulas. Select a method from the data and assumptions: composite rules suit tabulated equally spaced values, Romberg uses repeated trapezoidal refinements, and Gaussian quadrature reduces the node count for sufficiently smooth integrands when selected evaluation points can be computed.

### 5.3 Reading refinement ratios quantitatively

The error orders \(E_T(h)=O(h^2)\) and \(E_S(h)=O(h^4)\) describe the leading truncation behaviour under the required smoothness assumptions. If \(h\) is halved, then the leading trapezoidal error is multiplied by approximately \((1/2)^2=1/4\), while the leading Simpson error is multiplied by approximately \((1/2)^4=1/16\). In decimal terms these factors correspond to

$$
\log_{10}(4)\approx0.602,\qquad \log_{10}(16)\approx1.204
$$

decimal digits of error reduction per halving of \(h\). They are not two or four digits, and they are not guaranteed improvements in the total computed error once round-off or input-data uncertainty becomes important.

For a simple numerical illustration, suppose a smooth-problem trapezoidal truncation error is about \(0.08\) at one mesh width. A halved mesh predicts about \(0.02\), not \(0.008\), because the leading term is divided by four. If a Simpson error is about \(0.016\), halving the mesh predicts about \(0.001\), a division by sixteen. These are asymptotic predictions; the actual errors need not follow the exact ratios on a coarse mesh. A refinement table should therefore record the observed differences and compare them with the expected order rather than assuming the theoretical factor holds exactly at every step.

Increasing the number of strips by a factor of one hundred makes \(h\) one hundred times smaller. The leading terms then scale by \(100^{-2}=10^{-4}\) for the trapezoidal rule and \(100^{-4}=10^{-8}\) for Simpson's rule. That idealized calculation corresponds to four and eight decimal digits in the truncation component alone. It is a different refinement operation from halving \(h\), and it does not justify claims about the total numerical answer when arithmetic rounding and sampled-data errors are present.

### 5.4 A disciplined tolerance calculation

Suppose a composite trapezoidal rule is to satisfy an absolute error tolerance \(\tau\), and a valid bound for the second derivative is \(M_2\). The composite error estimate has the form

$$
|E_T|\le \frac{(b-a)}{12}h^2M_2.
$$

To turn this into a panel choice, require the right side to be no larger than \(\tau\), solve for \(h\), and then use \(n=(b-a)/h\). Since the strip count must be an integer, round the required count upward and recompute the bound with the actual \(h=(b-a)/n\). This last substitution is essential: a noninteger panel count is not a realizable rule.

For Simpson's rule the analogous bound uses the fourth derivative and \(h^4\). It also requires an even number of strips. After solving the inequality, increase the resulting integer count to the next even number if necessary, then verify the error bound again. A derivative maximum that is not actually valid on the full interval cannot support a guaranteed tolerance, and a bound may be conservative even when the observed error is much smaller.

### 5.5 Reporting a result when the exact integral is unknown

When an exact antiderivative is unavailable, an error estimate may still be obtained from a derivative bound or from successive refinements, but these have different logical status. A theorem-based bound is guaranteed if its smoothness and derivative assumptions hold. A difference between two approximations is an empirical indicator; it is not automatically a bound on the true error. Extrapolation methods such as Romberg use the pattern of errors across mesh widths to cancel leading terms, but their conclusions also depend on the assumed asymptotic expansion.

For a transparent numerical report, state the interval, rule, strip width, nodes or data source, and the result with units. Then state whether the error statement is a rigorous bound, an asymptotic estimate, or a comparison between refinements. If the final result is rounded, keep enough digits in intermediate sums so that the rounding of the displayed answer is not larger than the claimed tolerance. This distinction between what was calculated and what was proved is often the decisive part of a numerical-analysis answer.
