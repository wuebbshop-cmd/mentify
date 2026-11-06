import re
import runpy

r = runpy.run_path("_sma330_repair2.py")
extras = {}

def prose_word_count(text):
    text = re.sub(r"(?s)\$\$.*?\$\$", " ", text)
    text = re.sub(r"(?s)\\\[.*?\\\]", " ", text)
    text = re.sub(r"(?s)\\\(.*?\\\)", " ", text)
    text = re.sub(r"(?s)\$[^$]*\$", " ", text)
    text = re.sub(r"(?m)^#{1,6}\s.*$", " ", text)
    text = re.sub(r"(?m)^\s*\|.*$", " ", text)
    text = re.sub(r"(?m)^\s*```.*$", " ", text)
    return len(re.findall(r"\b[\w’'-]+\b", text))

extras["205_l1"] = r'''### A worked lesson example: bisection of a cubic

The lesson's bisection table uses f(x)=x^3−5x+1 on [0,1]. The endpoint values are f(0)=1 and f(1)=−3, so continuity gives at least one root in the interval. The first midpoint is 0.5, where f(0.5)=0.125−2.5+1=−1.375. Since the sign at 0 is positive and the midpoint sign is negative, retain [0,0.5]. At the next midpoint 0.25, f(0.25)=0.015625−1.25+1=−0.234375, so retain [0,0.25].

The third midpoint is 0.125. Its function value is 0.001953125−0.625+1=0.376953125, positive, so the new interval is [0.125,0.25]. The fourth midpoint is 0.1875; its value is approximately 0.0690918, still positive, leaving [0.1875,0.25]. The fifth midpoint is 0.21875, where f is approximately −0.0831, so the interval becomes [0.1875,0.21875]. This reproduces the lesson's bracket. It demonstrates the decision rule: retain the half whose endpoint values have opposite signs, not simply the half with a smaller midpoint.

The interval widths after successive halvings are 1, 1/2, 1/4, 1/8, 1/16, and 1/32. After five midpoint evaluations, the remaining bracket has width 1/32. Its midpoint is 0.203125, and the root is known to lie within 1/64 of that midpoint. The lesson's table reports the root as lying between 0.1875 and 0.21875; the midpoint 0.203125 is a useful estimate, not an exact root. The root is approximately 0.20164, so that midpoint is consistent with the final bracket.

### Fixed-point iteration: convergence is part of the method

An equation f(x)=0 can sometimes be rearranged as x=g(x), leading to x_(n+1)=g(x_n). The fact that a rearrangement is algebraically equivalent does not establish that the generated sequence converges. A common sufficient condition is that g maps a closed interval I into itself and is a contraction there: |g'(x)|≤k<1 throughout I. The mean value theorem then gives |g(x)−g(y)|≤k|x−y|, so successive errors shrink at least geometrically when the fixed point lies in I.

If α=g(α), the mean value theorem gives |x_(n+1)−α|=|g(x_n)−g(α)|≤k|x_n−α|. Iterating this inequality yields |x_n−α|≤k^n|x_0−α|. This is a useful theoretical bound, but it requires a valid contraction interval and an initial value in that interval. Observing that two or three decimal iterates appear stable is not a substitute for checking those hypotheses.

The source example x_(n+1)=ln(2x_n+7), starting at 2.5, is a different kind of fixed-point iteration from bisection. It uses the equation e^x−2x−7=0 and the logarithmic rearrangement. Its derivative is g'(x)=2/(2x+7). On [2,3], this derivative is positive and no larger than 2/11<1, while g maps the interval into itself. Thus the contraction test supports convergence. The corresponding rearrangement g(x)=(e^x−7)/2 is not suitable on this interval: its derivative e^x/2 is greater than one near the root, so the same simple contraction guarantee fails.

### Reading a convergence calculation critically

There are three separate questions when an iterative method is used. Does a root exist in the proposed region? Does the chosen iteration converge to a fixed point or root? How close is the computed iterate to the desired answer? The intermediate value theorem answers the first question for a continuous sign-changing bracket. A contraction condition or a local convergence theorem addresses the second. An interval-width bound, residual analysis, or a justified error estimate addresses the third.

For bisection, the existence argument and the error control are connected: the sign-changing interval is maintained at every step, and its width is exactly halved. For fixed-point iteration, existence may follow from the mapping theorem, while convergence depends on the behavior of g. A fixed point might exist even if a particular starting value diverges. A convergent sequence may also converge to a fixed point other than the one intended if several are present. State the interval, starting value, and selected branch when those details matter.

An approximate residual |f(x_n)| is informative but is not automatically the same as the root error |x_n−α|. If f changes very steeply, a small residual may correspond to a modest root error; if f is nearly flat, a small residual can coexist with a larger location error. A rigorous conversion needs additional information, such as a lower bound on |f'| near the root. This is why bisection's bracket-width guarantee is especially clear: it bounds location directly without relying on a derivative estimate.

### Choosing between bracketing and iteration

Bisection is appropriate when a continuous function has opposite signs at known endpoints and reliability is more important than speed. Its principal cost is one new function evaluation per step, and its interval shrinks by a predictable factor of two. It does not use derivative information and cannot leave the bracket if signs are handled correctly. Its limitation is linear convergence: many iterations may be needed for high accuracy.

Fixed-point iteration can be more economical when a well-chosen rearrangement contracts strongly. It may also be easier to implement when a derivative is unavailable. The choice of g matters: algebraically equivalent rearrangements can have very different derivatives and convergence behavior. Before calculating many terms, examine g(I) and a bound for |g'| on the interval. If no such simple guarantee is available, monitor the sequence and use a safeguard such as a bracketing interval when appropriate.

In an examination response, write the recurrence before substituting numbers. For bisection, show the current endpoints, midpoint, sign, and retained half. For fixed-point iteration, state g, compute or bound g', identify the interval and starting value, and then tabulate iterates with enough digits. Finish by stating the error criterion used. These are mathematical parts of the method, not presentational decoration.

### A second source-aligned root exercise

The lesson's assessment also asks for bisection on a cubic over [0,1], which reinforces that the method is not limited to quadratics. For example, with f(x)=x^3−7x^2+14x−6, the endpoint values are f(0)=−6 and f(1)=2, so the IVT guarantees at least one root in the interval. A first midpoint is 0.5, where f(0.5)=0.125−1.75+7−6=−0.625. The retained interval is [0.5,1]. At 0.75, f(0.75)=0.421875−3.9375+10.5−6=0.984375, so the next bracket is [0.5,0.75].

The key point is the sign test, not memorizing a polynomial. At every stage, one endpoint has a negative value and the other a positive value. The new midpoint replaces the endpoint with the same sign as the midpoint. Consequently the bracket continues to certify the existence of a root even when the exact root is not known. Since this cubic can have more than one real root, the initial interval specifies which root is being approximated; an equation alone may not identify a unique target.

For four midpoint evaluations from an interval of width one, the final bracket width is 1/16. Its midpoint has error at most 1/32. If the task requests accuracy to two decimal places, compare the interval endpoints after rounding; if they do not round to the same value, perform further iterations. The number of iterations should be selected from a bound, not guessed from the number of printed decimals.

### Fixed-point maps as deliberate design choices

To turn f(x)=0 into x=g(x), one may rearrange terms in multiple ways. Each formula can have exactly the same fixed points yet very different numerical behavior. A practical design evaluates the map's derivative near the desired root and checks whether a chosen interval is invariant. If |g'| is comfortably below one, nearby starting values are pulled toward the fixed point. If |g'| exceeds one, perturbations may be magnified instead.

Consider the source equation e^x−2x−7=0. The map g(x)=ln(2x+7) has a derivative below one on [2,3], whereas h(x)=(e^x−7)/2 has derivative e^x/2, which is much larger than one near the root. The first map is a contraction on the interval and the second is not. It would be a mistake to say that the original equation itself is “convergent” or “divergent”; convergence belongs to a particular iteration rule together with an interval and an initial value.

A useful diagnostic is to calculate two or three iterates only after checking the map's domain. The logarithm requires positive input; a rational map may have a pole; a square root may require a nonnegative argument. Iterating outside the domain is not a harmless numerical error but an invalid operation. Domain checks and contraction checks are separate: a map may be defined but fail to converge.

### Precision and pedagogy in the final answer

When a student says that a root is “correct to four decimal places,” the intended meaning should be tied to a bound or a rounding convention. For bisection, the bracket makes this direct. For a contraction, a known constant k and an error estimate can support a bound. For an open method, the residual and step size are common practical criteria but should be described as such unless a theorem converts them to a location guarantee.

Do not confuse truncation in the method with rounding in the displayed numbers. The bisection method has an exact interval-halving property in real arithmetic; rounding a midpoint before evaluating f can change which sign is observed. Fixed-point and Newton updates can amplify rounded inputs, especially when derivatives or denominators are unfavorable. Retain guard digits, carry enough intermediate precision, and round only after selecting the final estimate.

The source's exercises encourage explaining the result, not only producing it. A strong response identifies the root interval, states the continuity/sign argument, gives the recurrence, shows a trace of the computation, and closes with an accuracy statement. If a method fails a convergence test, explain which assumption is absent rather than claiming that numerical iteration is inherently unreliable. That analysis turns arithmetic into a defensible numerical argument.

### Deriving an a posteriori bound for a contraction

The contraction condition also gives a way to estimate the remaining error from changes already observed. Suppose |g'(x)|≤k<1 on an invariant interval and x_(n+1)=g(x_n). Because the iteration is contractive, the differences satisfy

$$
|x_{n+2}-x_{n+1}|\le k|x_{n+1}-x_n|.
$$

Applying the same inequality repeatedly bounds the distance from x_(n+1) to the limit by a geometric tail:

$$
|x_{n+1}-\alpha|
\le |x_{n+1}-x_n|(k+k^2+k^3+\cdots)
=\frac{k}{1-k}|x_{n+1}-x_n|.
$$

This estimate is useful because it does not require knowing the exact root, although it still requires a valid contraction constant on the interval. If k is close to one, the factor k/(1−k) is large and a small step may not imply a small remaining error. If k is comfortably below one, the same observed step gives a more informative bound. This explains why recording only the last difference without considering the contraction rate is incomplete.

For g(x)=ln(2x+7) on [2,3], a valid bound is k=2/11. The geometric-tail factor is therefore (2/11)/(9/11)=2/9. If two consecutive iterates differ by 0.0005, the remaining error in the newer iterate is bounded by approximately 0.000111, provided the exact interval and contraction hypotheses are in force. The estimate is conservative; the actual error may be smaller. A numerical answer should distinguish a guaranteed bound from an observed comparison.

### Existence, uniqueness, and convergence are distinct

The intermediate value theorem guarantees at least one root if a continuous function changes sign. It does not guarantee that the root is unique. Uniqueness may follow from monotonicity, for example if f' keeps one strict sign on the interval. A sign-changing interval may contain several roots if the function oscillates, but bisection still retains at least one root so long as the signs remain opposite. If identifying a particular root matters, the interval should be narrow enough or additional monotonicity information should be used.

For a fixed-point equation, a contraction on a closed interval implies a unique fixed point there and convergence from every initial point in that interval. Merely showing that g is continuous and maps the interval into itself can establish existence of a fixed point under the appropriate theorem, but does not by itself give convergence of the simple iteration from every start. The derivative bound below one is the stronger condition that controls the iterates.

These distinctions prevent three common logical jumps: an equation has a root, therefore every rearrangement converges; the iteration appears to converge, therefore the intended root is unique; or the endpoints have opposite signs, therefore there is exactly one root. Each conclusion needs its own premise. In a worked solution, name the theorem that supplies the claim and verify its hypotheses.

### Why the bisection sign invariant is robust

Let a_n and b_n be the current endpoints. The invariant is f(a_n)f(b_n)≤0, with a nonzero sign change unless an endpoint is already a root. At c_n=(a_n+b_n)/2, if f(c_n)=0, the exact root has been found. If f(a_n) and f(c_n) have opposite signs, retain [a_n,c_n]; otherwise retain [c_n,b_n]. In either case the next interval contains a root by continuity, and its length is half the previous one.

This invariant does not rely on the graph being monotone. If the interval contains several roots, the particular root retained may depend on the sign pattern, but at least one remains. That reliability is the chief advantage of bisection. The price is that it uses no information about how steeply or smoothly f crosses zero, so its convergence rate does not accelerate near a simple root.

When function values are computed approximately, the sign check itself may be uncertain if f(c_n) is extremely close to zero. A rounded display of “0.0000” is not proof of an exact zero. Retain more arithmetic precision or evaluate the sign with a stable expression. If the sign cannot be resolved, do not arbitrarily choose a half; instead increase precision or use other information.

### Interpreting iteration counts and requested accuracy

Suppose the initial bisection interval has width one and the task asks for a midpoint estimate within 10^−3. After n halvings, the midpoint error is bounded by 1/2^(n+1). The inequality 1/2^(n+1)≤10^−3 requires n+1≥log_2(1000), so n=9 halvings suffice for this midpoint criterion. If the requested bracket width is 10^−3, then 1/2^n≤10^−3, so n=10 halvings are needed. The one-step difference comes entirely from whether the tolerance applies to the full bracket or to its midpoint.

The same principle applies to decimal-place requirements. A midpoint that visually displays three places may not be correct to three decimal places. A guaranteed bound should be smaller than half the unit in the last requested place, or the bracket endpoints should round identically under the chosen convention. For fixed-point iteration, use a contraction-based estimate when available; for Newton or secant, use a justified local bound or report an empirical stopping test without overclaiming.

### A classroom example of method selection

If students are given only a graph and two points with opposite signs, bisection is usually the natural first method. The available information supports continuity and bracketing, while no derivative or explicit formula may be accessible. If students are given an analytic f and can compute f', Newton's method may be introduced after a root interval and a plausible starting point are identified. If a derivative is cumbersome but two function values can be evaluated, the secant method is a reasonable alternative.

The comparison should be based on assumptions and consequences. Bisection guarantees containment but needs many halvings for tight tolerances. Fixed-point iteration can be simple but depends strongly on the rearrangement. Newton can converge rapidly but may be sensitive to the derivative and starting point. Secant avoids symbolic differentiation but may have a small denominator and can leave the root region. A strong numerical analyst can explain why a chosen formula suits the information provided, rather than merely selecting the one with the shortest recurrence.
'''

extras["205_l2"] = r'''### Correcting and interpreting the source fixed-point example

For f(x)=e^x−2x−7, the endpoint values f(2)=e²−11≈−3.610944 and f(3)=e³−13≈7.085537 have opposite signs. The continuous function therefore has a root in (2,3). With g(x)=ln(2x+7), the fixed-point equation is equivalent wherever 2x+7>0. On [2,3], g'(x)=2/(2x+7), so 0<g'(x)≤2/11<1. Also g(2)=ln 11≈2.3979 and g(3)=ln 13≈2.5649; these values lie in [2,3], so the map preserves the interval and contracts there.

Starting from x_0=2.5, the first update is x_1=ln 12≈2.48490665. The next values are approximately x_2=2.482421, x_3=2.48193, and x_4≈2.48183. The root is about 2.4818. Keep sufficient precision in intermediate steps because rounding each iterate early can alter the last reported digits. The fixed-point residual and change between successive iterates may be used as stopping indicators, but the contraction hypothesis is what supports convergence.

The lesson's bisection illustration on this equation requires careful arithmetic. At x=2.5,

$$
f(2.5)=e^{2.5}-5-7\approx12.182494-12=+0.182494,
$$

not a negative value. Starting with [2,3], the first midpoint therefore leaves [2,2.5]. The next midpoint is 2.25, and f(2.25)=e^{2.25}-4.5-7≈−2.0127, so the second retained interval is [2.25,2.5]. The bracket remains valid because its endpoint signs are negative and positive. The interval width after those two midpoint evaluations is 0.25, and its midpoint is 2.375; this gives a guaranteed location uncertainty no larger than half the width, 0.125.

### Error bounds and stopping in bisection

Let the initial bracket width be L=b_0−a_0. After n halvings, its width is L/2^n. Any point in the retained interval, including its midpoint, is at most that width from the root; the midpoint specifically is at most L/2^(n+1) away. Distinguish the two bounds because some conventions label the first midpoint as iteration one and others count the initial bracket as stage zero. The actual interval endpoints remove ambiguity.

To guarantee midpoint error at most ε, it is sufficient that L/2^(n+1)≤ε, or n≥log_2(L/(2ε)). If a task instead requires the bracket itself to have width at most ε, use L/2^n≤ε. This difference is a frequent source of off-by-one answers. Always state whether the reported guarantee concerns the bracket width or the midpoint error.

Bisection also gives a transparent table for checking arithmetic. Record a_n, b_n, c_n=(a_n+b_n)/2, f(c_n), and the new interval. A sign should be recomputed or checked before updating the bracket. Rounding f(c_n) to zero prematurely can cause the wrong half to be retained; if an exact zero is found, stop, otherwise retain enough digits to determine its sign.

### Comparing contraction and bracket guarantees

The fixed-point contraction bound is relative to the starting error: |x_n−α|≤k^n|x_0−α|. It can be sharper when k is small, but its use depends on proving that the map is self-preserving and contractive. Bisection instead supplies an absolute location bound from the interval width and a valid sign change. It does not require estimating the unknown initial error or differentiating f.

These guarantees answer different questions. A small successive difference |x_(n+1)−x_n| is not by itself a universal error bound; a slowly changing sequence can still be far from a root. Under contraction, one can relate successive differences to the remaining error, but the constant matters. In bisection, the bracket offers the direct certificate. A robust numerical report names the chosen guarantee rather than treating every stopping test as equivalent.

For the logarithmic example, one can verify both the iterate change and the residual f(x_n), but the contraction proof supplies the convergence rationale. For the cubic table example, the signs supply existence and the bracket supplies accuracy. In both cases the calculation should stop when the stated criterion is met, not merely when a rounded display looks stable.

### Proving the contraction estimate rather than assuming it

The derivative test comes from the mean value theorem. For any x,y in an interval I, if |g'(t)|≤k<1 for every t between x and y, then

$$
|g(x)-g(y)|=|g'(\xi)||x-y|\le k|x-y|
$$

for some intermediate ξ. This is the contraction inequality. If additionally g(I)⊂I, every iterate remains in the domain, and repeated application shows that distances between iterates shrink. The fixed-point theorem then guarantees a unique α in I with g(α)=α and convergence of x_(n+1)=g(x_n) from each x_0∈I.

For g(x)=ln(2x+7) on [2,3], the input 2x+7 is positive throughout. The derivative 2/(2x+7) is largest at the left endpoint and equals 2/11 there, so k=2/11 is a valid uniform bound. The endpoint images are ln 11 and ln 13, both inside [2,3]; because g is increasing, the image of the whole interval lies between those endpoint values. This checks both domain and invariance, rather than relying on a derivative calculation alone.

If only |g'(α)|<1 is known at the fixed point, the argument establishes local attraction under standard smoothness conditions, but not invariance or convergence from every point in a broad interval. If |g'|≤1 without strict inequality, a contraction theorem cannot be invoked in its usual form. Such distinctions matter when proving convergence rather than describing observed behavior.

### Error estimates from successive fixed-point differences

The contraction inequality yields an a posteriori estimate based on two computed iterates. If d_n=|x_n−x_(n−1)|, then the future differences are bounded by d_(n+1), k d_(n+1), k²d_(n+1), and so forth. Summing this geometric tail gives

$$
|x_n-\alpha|\le\frac{k}{1-k}|x_n-x_{n-1}|.
$$

For k=2/11, the factor is 2/9. If the last change is 0.0002, the remaining error is at most about 0.0000445 under the verified contraction assumptions. The bound is not the same as the observed difference; it includes all future movement. If k is close to one, the factor is large, emphasizing that slow contraction requires a much smaller step before a useful guarantee follows.

There is also a direct prior-error estimate |x_n−α|≤k^n|x_0−α|. This is theoretically simple but may be inconvenient because α is unknown, making the initial error unknown. A known interval can bound |x_0−α|, and then the estimate becomes computable. The a posteriori bound avoids that unknown distance but depends on a valid k and a measured step. State which form is used.

### Root existence for the fixed-point equation

The equation f(x)=0 and the rearranged equation x=g(x) have the same solutions only on the domain where the rearrangement is valid. For e^x−2x−7=0, taking logarithms of e^x=2x+7 requires 2x+7>0. Every x in [2,3] satisfies this, so the rearrangement neither introduces nor loses a root in that interval. In other problems, multiplication by a variable expression, squaring, or division can introduce extraneous fixed points or exclude a solution; equivalence should be checked.

The endpoint sign calculation establishes a root for f by continuity. The contraction mapping theorem establishes a fixed point of g and uniqueness in the invariant interval. Since f(x)=0 is equivalent to x=g(x) there, the fixed point is the desired root. This is a complete chain of reasoning: continuity/sign establishes root existence, map invariance and contraction establish iterative convergence, and algebraic equivalence links the two statements.

An algebraic rearrangement alone does not provide any of these convergence conclusions. For example, the map h(x)=(e^x−7)/2 is equivalent at a solution, but its derivative e^x/2 exceeds one near the root. Iterating h from x_0=2.5 gives a large next value rather than a nearby approximation. The equation has not changed; only the numerical map has.

### Bisection error bounds with an explicit interval

For the source cubic x^3−5x+1, the lesson's fifth update leaves [0.1875,0.21875]. The bracket width is 0.03125, and its midpoint is 0.203125. The root lies within 0.015625 of that midpoint. The true root is approximately 0.20164, so the bound is consistent. If three decimal places are desired, the endpoints do not yet agree in their rounding, so further bisection steps are needed.

After each extra iteration the width is halved. From width 0.03125, another five halvings give width 0.0009765625, with midpoint error at most 0.00048828125. That is sufficient to determine a value to three decimal places if the resulting endpoints round consistently. Showing the current width and the requested tolerance is more reliable than counting decimal places in the midpoint.

For a tolerance of 10^−4 on midpoint error from an initial unit interval, require 1/2^(n+1)≤10^−4. Since 2^13=8192 and 2^14=16384, n=13 gives 1/16384≈0.0000610 and suffices, while n=12 gives 1/8192≈0.0001221 and does not. This explicit comparison verifies the iteration count. If the requested tolerance is for bracket width, one additional halving is required.

### Reporting convergence evidence precisely

A numerical report should avoid using “converges” to mean only that displayed numbers are getting closer. For fixed-point iteration, give the map, interval, domain, and contraction or other convergence argument. For bisection, give the sign-changing endpoints and the interval width after the final step. If a sequence appears to converge but no theorem is applied, say that the observed iterates stabilize and state the empirical test; do not present it as a proof.

Similarly, the words “accurate to” require evidence. A narrow bisection bracket supplies a bound. A fixed-point contraction can supply an error estimate. A small residual is useful but requires a derivative bound to turn it into root-location accuracy. Keep separate the method's exact mathematical guarantee, the numerical values obtained with finite arithmetic, and the final rounding decision.
'''

extras["205_l3"] = r'''### Source-table cubic and rigorous interval updates

The lesson demonstrates bisection on f(x)=x^3−5x+1 over [0,1]. Since f(0)=1 and f(1)=−3, continuity guarantees a root in the interval. The midpoint sequence and the sign-based brackets are:

$$
\begin{array}{c|c|c|c}
n&[a_n,b_n]&c_n&\operatorname{sign} f(c_n)\\
1&[0,1]&0.5&-\\
2&[0,0.5]&0.25&-\\
3&[0,0.25]&0.125&+\\
4&[0.125,0.25]&0.1875&+\\
5&[0.1875,0.25]&0.21875&-
\end{array}
$$

The resulting interval is [0.1875,0.21875], exactly the range reported in the lesson. Its midpoint is 0.203125; the interval width is 0.03125, so the midpoint error is bounded by 0.015625. This is an accuracy statement supported by the bracket, not an inference from the apparent number of stable digits.

The table also illustrates why each function sign matters more than the direction in which a midpoint moves. The first two midpoints are negative, so the positive left endpoint is retained. The third and fourth are positive, moving the left endpoint rightward. The fifth is negative, moving the right endpoint leftward. The root remains enclosed at every stage. A table that reports midpoints but omits signs does not show why its intervals are valid.

### Fixed-point convergence and failure modes

For x=g(x), a useful local condition near a fixed point α is |g'(α)|<1. It predicts local attraction, but a theorem over an interval is stronger: if g maps a closed interval into itself and |g'|≤k<1 throughout, then the iteration converges to the unique fixed point there from every initial point in that interval. If only a derivative value at one point is checked, the conclusion is local and requires additional assumptions.

The logarithmic rearrangement of e^x−2x−7 is contractive on [2,3], while the rearrangement g(x)=(e^x−7)/2 has derivative e^x/2, whose magnitude is much larger than one near the root. The same equation can thus generate a convergent sequence under one rearrangement and a divergent or unstable sequence under another. The fixed-point form is part of the numerical method, not an inconsequential rewriting.

If |g'| is near one, convergence can be slow even when it occurs. If the derivative changes sign, iterates may alternate around the fixed point. If |g'| exceeds one, small errors can grow. These observations guide diagnosis but do not replace checking domain restrictions, interval invariance, and the actual sequence. For g(x)=ln(2x+7), the logarithm requires 2x+7>0; the chosen interval satisfies that requirement.

### Method selection and responsible stopping

Use bisection when the function is continuous and an initial sign-changing interval is known. Its guaranteed bracket contraction is valuable when a dependable answer is required. Use fixed-point iteration when a suitable rearrangement is available and its convergence can be justified or safely monitored. Compare the work per iteration as well as asymptotic speed: bisection needs function values; fixed-point iteration evaluates g; Newton's method in the next lesson adds a derivative evaluation.

Do not use the magnitude of f(x_n) as a universal root-error estimate. Near a simple root, a derivative lower bound can relate residual to distance, but absent that information the two are not interchangeable. Likewise, a small change between iterates may indicate stagnation caused by rounding rather than true convergence. State whether stopping is based on interval width, a contraction estimate, residual tolerance, or successive-iterate difference.

When reporting a root to a requested decimal accuracy, the interval should be narrow enough to force the same rounding for every possible root inside it. If the endpoints round differently, continue the iteration. This “rounding agreement” criterion is stronger than simply printing a midpoint with several decimals. It links the mathematical guarantee to the requested format.

### A complete bisection error argument for the lesson table

Let the source table's starting interval have endpoints a_0=0 and b_0=1. The endpoint signs are positive and negative. At each step, the midpoint is evaluated, and the same-sign endpoint is replaced. Inductively, if the bracket at step n contains a root and has width 2^(−n), then the retained half contains at least one root and has width 2^(−(n+1)). The induction starts with the IVT on [0,1] and proves the invariant for all subsequent steps.

After five midpoint evaluations the interval [0.1875,0.21875] has width 0.03125=1/32. The midpoint estimate 0.203125 is at most half that width from any root in the bracket. This gives the bound 0.015625. If a stricter tolerance is needed, the width formula predicts the required work before function values are computed. From the original unit interval, n midpoint evaluations guarantee midpoint error at most 2^(−(n+1)).

For four-place accuracy, the midpoint bound must be at most 0.00005 if “correct to four decimal places” is interpreted as a rounding guarantee. This requires 2^(−(n+1))≤5×10^−5, so n+1≥log_2(20000), and n=14 suffices. The exact rounding convention may handle ties separately, but the bound is safely below half a unit in the fourth decimal place. This count is not the same as simply printing fourteen digits.

### Uniqueness and the shape of the cubic

The cubic f(x)=x^3−5x+1 used in the lesson has derivative f'(x)=3x^2−5. On [0,1], f' is negative for x<√(5/3), and because √(5/3)>1, it is negative throughout this interval. Therefore f is strictly decreasing on [0,1], and the sign-changing interval contains exactly one root. This monotonicity fact strengthens the IVT existence conclusion to uniqueness for the chosen bracket.

On the larger real line, f is not globally monotone: its derivative changes sign outside [0,1], and the cubic has additional roots. Thus the uniqueness statement must remain interval-specific. Bisection started on [0,1] targets the root in that interval; a different starting interval might identify another root. This is a useful reminder that root-finding is not only about an equation but also about selecting the solution of interest.

The same reasoning applies to the source assessment polynomial x^3−7x^2+14x−6. Its derivative and sign pattern can be used to analyze how many roots lie in a chosen interval. A sign change is sufficient for at least one root, but uniqueness requires monotonicity or another argument. If the exercise asks only to find a solution on [0,1], the iteration can locate one; if it asks for all roots, interval analysis must be expanded.

### Fixed-point iteration error and interval invariance

For g(x)=ln(2x+7), the mapping interval [2,3] is invariant because g is increasing and its endpoint values lie in [2,3]. The derivative bound |g'|≤2/11 then gives a contraction. These two checks play different roles: invariance ensures every iterate remains where the function and derivative estimates are valid; contraction ensures successive errors shrink. One without the other is insufficient for the standard global-on-I conclusion.

At a fixed point α, the error relation follows directly from the mean value theorem:

$$
|x_{n+1}-\alpha|=|g(x_n)-g(\alpha)|
\le k|x_n-\alpha|.
$$

Repeated application yields |x_n−α|≤k^n|x_0−α|. The sequence from x_0=2.5 begins near the root because this starting value is already in [2,3]. A different starting value outside the interval is not covered even if the logarithm happens to be defined there. The theorem's guarantee is always tied to its stated interval.

### Why root residuals need interpretation

For a computed point x, the residual is |f(x)|, whereas the location error is |x−α|. The mean value theorem relates them through a derivative at an intermediate point, but only if a useful derivative bound is known. If |f'|≥m>0 on the segment from x to α, then |x−α|≤|f(x)|/m. If f' can be very small, a residual of 10^−6 may correspond to a much larger location error.

Bisection avoids this issue because it bounds the location by interval width. Fixed-point iteration can also produce a location bound through a contraction constant. Newton's and secant's residuals are still useful diagnostics, but they do not automatically provide an absolute root error. In source-based reporting, match the claim to the evidence: “residual below a tolerance” is not synonymous with “root correct to that tolerance.”

### Error sources in a hand-computed iteration

Three different errors should be kept separate. The method's truncation error is the difference between the exact root and the approximation produced after a finite number of steps. Round-off error enters when intermediate function values, derivatives, and corrections are rounded. Modeling error arises if the equation or function values do not accurately represent the real problem. Bisection controls the first through its bracket width, but it does not eliminate round-off or modeling error.

For bisection, a midpoint can be represented exactly in binary only for certain fractions; in general, finite arithmetic rounds it. If a function evaluation is near zero, that rounding can affect the sign decision. For Newton, the quotient f/f' can magnify small errors when f' is small. For secant, subtracting nearly equal function values can cause cancellation in the denominator. Good practice keeps guard digits, evaluates stable expressions, and avoids interpreting more digits than the inputs support.

### A compact decision framework

When solving a nonlinear equation, first locate a region where a root exists. Check continuity and endpoint signs; if possible, use monotonicity to establish uniqueness. Then choose the iteration based on available information. Bisection needs only function evaluations and a bracket. Fixed-point iteration needs a useful rearrangement and a convergence argument. Newton needs a derivative and a viable starting point. Secant needs two starting values and avoids explicit differentiation.

Next decide what constitutes completion. For bisection, derive n from the interval-width requirement. For fixed-point iteration, use a contraction bound or a justified difference estimate. For Newton and secant, monitor residual, step, and denominator; add a bracket or local error theorem if a certified location accuracy is required. The selected stopping test should appear in the final answer.

Finally, report the target root, method, main iterates, and interpretation. Do not equate method speed with reliability. Bisection's predictable interval contraction can be more valuable than a fast but unverified open iteration. Conversely, when smoothness and starting conditions are favorable, Newton or secant can reduce the evaluation cost substantially. Numerical analysis is the reasoned choice of a procedure and the interpretation of what it guarantees.
'''

extras["206_l1"] = r'''### Source Newton example: cubic equation and tangent updates

The module asks for Newton–Raphson applied to f(x)=x^3+2x^2+10x−20 with x_0=1. Differentiating gives f'(x)=3x^2+4x+10, so

$$
x_{n+1}=x_n-\frac{x_n^3+2x_n^2+10x_n-20}{3x_n^2+4x_n+10}.
$$

At x_0=1, f(1)=−7 and f'(1)=17, hence x_1=1+7/17≈1.4117647. Continuing without rounding intermediate values gives x_2≈1.3693365, x_3≈1.3688082, and x_4≈1.3688081. The updates rapidly settle near the positive root. A check substitutes the final value into f and confirms a small residual; the sequence alone does not establish the number of correct digits unless a stopping or error criterion is stated.

Geometrically, each update takes the tangent to y=f(x) at the current approximation and uses its x-intercept as the next approximation. This explains both the formula and its possible weakness. If f'(x_n) is zero or very small, the correction is undefined or extremely large. If the tangent intercept lies outside a region where the graph behaves regularly, the next iterate may move away from the desired root. Choosing a reasonable starting value and monitoring the residual are essential parts of using the method.

### Deriving the secant update from a chord

Newton's tangent uses the derivative f'(x_n). The secant method replaces that derivative by the slope through two known points (x_(n−1),f(x_(n−1))) and (x_n,f(x_n)):

$$
\frac{f(x_n)-f(x_{n-1})}{x_n-x_{n-1}}.
$$

Taking the x-intercept of this chord gives

$$
x_{n+1}=x_n-f(x_n)\frac{x_n-x_{n-1}}{f(x_n)-f(x_{n-1})}.
$$

It uses two starting approximations and avoids explicit differentiation, but requires a nonzero denominator. If the two function values are equal, the chord is horizontal and supplies no finite intercept. If they are close, the quotient can be sensitive to rounding. Unlike bisection, the secant method does not automatically preserve a sign-changing bracket.

### Correct secant arithmetic on the quadratic

For f(x)=2x^2−6x−3, choose x_0=3 and x_1=4. Then f(3)=−3 and f(4)=5. The first secant update is

$$
x_2=4-5\frac{4-3}{5-(-3)}=4-\frac58=3.375.
$$

At x_2=3.375, f(x_2)=−0.46875. Using x_1=4 and x_2=3.375 for the next chord gives

$$
x_3=3.375-(-0.46875)\frac{3.375-4}{-0.46875-5}
=3.375-\frac{0.29296875}{-5.46875}
\approx3.428571.
$$

The positive denominator sign in the final correction is important: the fraction is negative, so subtracting it increases the estimate. The exact positive root is (3+√15)/2≈3.4364917. Thus the second secant update moves toward the root but is not yet the final answer.

### Comparing the two open methods

Newton–Raphson needs one current iterate and a derivative; the secant method needs two iterates and function values only. Near a simple root with a good starting value, Newton commonly converges very rapidly, while the secant method is typically superlinear but does not have the same quadratic local rate. Neither method provides the unconditional bracketing safeguard of bisection.

The choice depends on what is available. If f' is easy and reliable to compute and a suitable starting value is known, Newton may be efficient. If derivatives are inconvenient or unavailable, the secant method can approximate the slope from two function evaluations. If guaranteed containment is the priority, retain a bracket or use a safeguarded hybrid. In all cases inspect denominators, function values, and iterate behavior rather than assuming an open method must converge.

### Establishing which root is being approximated

Before iterating, inspect the equation and the stated interval. Newton's and secant methods are open methods: their formulas do not preserve a root bracket, and different starting values can converge to different roots. For a polynomial with several real roots, the phrase “find a root” is incomplete unless a target interval, sign pattern, or initial approximation identifies the intended one. A sign-changing interval gives a reliable existence argument and helps distinguish the target even when it is not used to constrain each Newton step.

For the source cubic f(x)=x^3+2x^2+10x−20, f(1)=−7 and f(2)=16, so a root lies in (1,2). Moreover f'(x)=3x^2+4x+10 is always positive: its discriminant is negative and its leading coefficient is positive. The function is therefore strictly increasing and has at most one real root. This context makes the Newton sequence from x_0=1 meaningful. The uniqueness argument depends on the derivative sign, not on the fact that the iterates happen to settle near one value.

By contrast, the quadratic 2x^2−6x−3 has two real roots, one positive and one negative. Starting with x_0=3 and x_1=4 aims at the positive one. Its exact value (3+√15)/2 is useful for checking the secant result, but a general secant computation will not have such a closed form. Specifying a root and checking whether the computed sequence remains in a plausible region are therefore part of a complete numerical solution.

### Understanding an iteration table

An iteration table should expose the quantities that determine each update. For Newton, columns for n, x_n, f(x_n), f'(x_n), correction −f/f', and x_(n+1) make arithmetic auditable. For secant, list the two current points, both function values, the slope quotient, and the new point. Carry enough digits in x_n that later function values are reproducible; otherwise a reader cannot tell whether a discrepancy is algebraic or simply early rounding.

The correction size itself has interpretation. In Newton's method a small correction means the tangent intercept is close to the current point; it does not prove that the point is close to a root if the tangent model is poor. In the secant method a small correction may occur when both function values are nearly equal or the chord slope is very large. Inspect |f(x_n)| alongside the step. If one is small and the other is not, investigate rather than relying on a single stopping test.

The table also reveals failure. A derivative approaching zero, a secant denominator approaching zero, a sudden jump, or a residual that increases markedly warns that the local model may be unreliable. The appropriate response is not to keep reporting additional digits. Reconsider the starting values, choose an interval with a sign change, or use a safeguarded method. Numerical stability is assessed from the quantities actually used in the recurrence.

### Practical relation to bisection and fixed-point iteration

The preceding lesson's bisection method is slower but maintains an interval containing a root. Newton and secant methods can be much faster near a simple root but may leave a safe interval. A practical compromise is to maintain a bracket and accept a Newton or secant step only when it remains within that bracket and improves the situation; otherwise take a bisection step. This explains why reliable numerical software often combines methods rather than relying on a single formula.

Fixed-point iteration x_(n+1)=g(x_n) is another way to generate root approximations. It does not require derivatives at each step, but a poor rearrangement may diverge. Newton can itself be viewed as a fixed-point map g(x)=x−f(x)/f'(x) when the derivative is defined. The map's local derivative at a simple root is zero, explaining Newton's rapid local convergence; away from the root, the behavior may differ substantially.

Thus a method's formula and its convergence conditions should be taught together. Bisection relies on continuity and opposite endpoint signs; fixed-point iteration relies on mapping and contraction conditions; Newton relies on derivative regularity and a suitable starting region; secant relies on informative, distinct function values. Choosing a method is choosing both a computational recurrence and the hypotheses that make its result trustworthy.

### A short audit of intermediate arithmetic

The Newton source example can be checked without recomputing every digit. At x_0=1, the numerator is −7 and the derivative is 17, so the first correction is positive and less than one half. The next value must therefore lie between 1 and 1.5, as 1.4117647 does. In the next step f(x_1) is small and positive, while f'(x_1) remains positive, so the Newton correction is negative; x_2 should be slightly less than x_1. This sign-and-range check catches many transcription errors before detailed decimal arithmetic.

The same principle applies to secant updates. Track the signs of both function differences and the point difference before dividing. A negative correction quotient means the update increases x when the recurrence subtracts that quotient. If the computed next iterate moves in the opposite direction, revisit the signs rather than assuming a calculator mistake. Numerical reasoning includes these qualitative checks alongside exact calculations.

An independent implementation can also verify each recurrence by substituting the reported values into f and f'. Agreement with a table is useful, but a direct residual test is more transparent. Report enough precision that recomputing the residual does not produce a misleading discrepancy from early rounding.

### A close reading of the source Newton sequence

The source equation has a useful structural property in addition to its numerical iterates. Its derivative is f'(x)=3x^2+4x+10. The discriminant of this quadratic is 4^2−4(3)(10)=−104, and its leading coefficient is positive, so f'(x)>0 for every real x. Thus f is strictly increasing and can have at most one real zero. Since f(1)=−7 and f(2)=16, continuity also gives a zero between 1 and 2. Together these statements identify one unique real target for the iteration.

This structural argument makes the sequence easier to interpret. Starting from x_0=1, f is negative, so the Newton correction −f/f' is positive. At x_1≈1.4118 the function value is slightly positive, and the derivative remains positive, so the next correction is negative. The iterates cross the root and then approach it from the other side. The sign of the correction is not arbitrary: it follows from the sign of f and the positive slope.

One can check the first update exactly before using decimals. The derivative at one is 17 and the function value is −7; therefore the step is 7/17. Evaluating the full cubic at x_1 then gives the next residual. Retaining the rational value 24/17 for x_1 until the next calculation can reduce round-off compared with immediately replacing it by 1.4118. Exact symbolic simplification is not always convenient, but preserving several guard digits has the same practical purpose.

### The tangent construction and geometric limitations

Newton's formula is derived from the tangent line, but the tangent is a local approximation to the curve. If the function has large curvature over the distance to the tangent intercept, the line may predict a poor next point. A point close to a horizontal tangent makes the denominator small, creating a large correction. A point at which the derivative is zero cannot be used at all unless the function value is also zero and the root has already been found.

The geometry also explains why the sign of f alone does not determine the direction of the Newton step: the derivative's sign matters. If f(x_n)>0 and f'(x_n)>0, the correction is negative and x decreases. If f'(x_n)<0, the same positive residual gives a positive correction. When f' changes sign or the graph has several turning points, a simple intuition based only on “move toward where the function crosses” may be wrong.

An algebraic update can be well-defined but still unhelpful. A tangent may intersect the axis far from the intended root, or a later iterate may enter a region with poor derivative behavior. A practical solver can reject unusually large steps, keep a known bracket, and use a fallback. Such a safeguard changes the pure method but can make the computation more dependable.

### Secant as a derivative estimate

The secant method's divided difference is a finite-difference slope. For a differentiable function and distinct points x_(n−1),x_n, the mean value theorem says it equals f'(ξ) for some ξ between them. As the two points approach one another near a simple root, this slope can approximate the local tangent. Unlike Newton, the method does not require the derivative formula, but it does require two function evaluations and the storage of the previous iterate.

The approximation can be poor when the points are far apart or when the function bends sharply between them. The denominator f(x_n)−f(x_(n−1)) can also suffer cancellation if the function values are close. Scaling or higher precision may help with arithmetic, but cannot repair poor starting values or a chord that does not represent local behavior. Check the denominator before each update and monitor whether the new point remains in a plausible region.

The method's starting pair serves a different role from a bracketing interval. The two values need not have opposite signs for the secant formula to be evaluated; however, opposite signs can help identify a root and provide a bracket to monitor. If the iterates are allowed to leave that interval, the ordinary secant algorithm no longer has a containment guarantee. This is why a safeguarded secant method is distinct from the plain secant recurrence.

### An error budget for a reported root

The number displayed in a final answer is affected by at least three stages: the root approximation produced by a finite iteration, arithmetic rounding within each update, and rounding of the final result. If coefficients are measurements or rounded data, uncertainty in the model adds another contribution. A long decimal display addresses none of these automatically.

For the source Newton sequence, the iterate change from x_3 to x_4 is tiny, and the residual at x_4 is also small. These are strong practical indicators. To claim a rigorous location error, one could use the monotonic derivative lower bound on a known interval and the mean value theorem. Because f'(x)=3x^2+4x+10 is positive, a lower bound m on [1,2] yields |x−α|≤|f(x)|/m. The bound should be calculated explicitly and the interval named; simply saying “the derivative is positive” does not provide a numerical m.

When an exact root is not known, report what is measurable: the residual, change in iterates, and any convergence criterion used. If a method is stopped after a fixed number of steps because the source asks for that number, do not claim a stronger accuracy than the calculation supports. Correctly describing evidence is part of numerical accuracy.

### Choosing an algorithm under real constraints

If derivative evaluation is inexpensive and the starting point can be chosen near a simple root, Newton often offers the fastest local progress. If a symbolic derivative is difficult or unavailable, secant reuses two function values to estimate a slope. If the function is continuous and a sign-changing bracket is available, bisection gives predictable reduction and is robust to poor curvature. Fixed-point iteration can be attractive when a contractive rearrangement is evident.

These are not interchangeable promises. The cost of evaluating f, f', or g may dominate the number of iterations. Some applications also require that every approximation remain within a physically meaningful interval. In such settings, the fastest unconstrained recurrence may not be the best choice. A hybrid that preserves a bracket while accepting good Newton or secant steps can provide both progress and a fallback.

In an answer, explain the choice briefly: name the available data, the method's hypothesis, and the desired guarantee. For example, “A sign-changing interval is given and no derivative is supplied, so bisection guarantees a root remains bracketed,” or “A derivative is available and the initial value is near a simple root, so Newton is appropriate; the residual and step will be checked.” This makes the solution's method a reasoned decision rather than a formula selected by habit.
'''

extras["206_l2"] = r'''### Detailed Newton calculation from the approved lesson

For the approved lesson's equation f(x)=x^3+2x^2+10x−20, the derivative is f'(x)=3x^2+4x+10. With x_0=1,

$$
x_1=1-\frac{1+2+10-20}{3+4+10}
=1+\frac7{17}\approx1.4117647.
$$

Substitution into the same recurrence gives x_2≈1.3693365, x_3≈1.3688082, and x_4≈1.3688081. The latter values agree to several decimal places, and f(x_4) is correspondingly small. To justify a stated accuracy, compare successive iterates and the residual, and, where a guarantee is required, use a convergence or error bound appropriate to the function and starting interval.

Newton's update is obtained by linearizing f at x_n:

$$
f(x)\approx f(x_n)+f'(x_n)(x-x_n).
$$

Setting the linear approximation to zero and solving for x gives the tangent intercept x_(n+1)=x_n−f(x_n)/f'(x_n). This is a local model. The actual function need not follow its tangent far from x_n, which is why a distant intercept can be a poor next guess. The formula is most reliable when the current iterate is already in a region where the derivative is nonzero and the graph is sufficiently regular.

### Local convergence and the role of a simple root

For a simple root α, f(α)=0 and f'(α)≠0. Under suitable smoothness and a sufficiently close starting value, Newton's error often satisfies an approximately quadratic relation e_(n+1)≈C e_n^2, where e_n=x_n−α. This explains why the number of correct digits can grow quickly after the iterates enter the local convergence region. The statement is local, not a guarantee from every initial value.

If α is a multiple root, then f'(α)=0 and the usual simple-root argument no longer applies; convergence may become only linear. If an iterate lands where f'(x_n)=0, the standard update cannot be evaluated. If f'(x_n) is merely small, division can magnify function-evaluation and rounding errors. These conditions should be checked when a sequence behaves unexpectedly.

The secant method approximates f'(x_n) with a divided difference from two recent points. It avoids a symbolic derivative but inherits sensitivity when f(x_n)−f(x_(n−1)) is small. Its local convergence is generally faster than linear for a simple root but slower than ideal Newton convergence. These are local rate comparisons; poor starting values, multiple roots, or nearly horizontal secants can dominate actual behavior.

### Corrected secant sequence and exact root comparison

For f(x)=2x²−6x−3, the secant starts x_0=3 and x_1=4, with function values −3 and 5. Then x_2=3.375. Because f(3.375)=−0.46875, the next secant calculation is

$$
x_3=3.375-(-0.46875)
\frac{3.375-4}{-0.46875-5}
\approx3.428571.
$$

The exact positive root follows from the quadratic formula:

$$
\alpha=\frac{6+\sqrt{60}}4=\frac{3+\sqrt{15}}2\approx3.4364917.
$$

Thus |x_3−α|≈0.00792. The former value 3.32143 was caused by mishandling the negative denominator in the secant correction; the numerator divided by −5.46875 is negative, and subtracting that quantity raises x_3. Sign-checking the correction is a useful safeguard before rounding.

One can continue the secant sequence using the two most recent pairs. It converges to the positive root, but no sign bracket is preserved by the formula itself. A plot or endpoint sign check may help choose starts, but the sequence should still be monitored for small denominators, repeated iterates, or movement toward the other root. The quadratic has a negative root as well, so “the root” is ambiguous unless the target is specified.

### Stopping rules and independent checks

Stopping on |x_(n+1)−x_n|<ε is convenient, but does not alone guarantee |x_n−α|<ε. A method can stagnate because rounded values repeat, even when the residual is not sufficiently small. A stronger practical test uses both a small iterate change and a small residual |f(x_n)|, together with a known local convergence regime or bracket when available.

For Newton's method, a residual check evaluates the original equation rather than only the update formula. For the secant method, check f at the latest point and ensure the denominator is not near zero relative to the scale of the function values. If an exact root is known, calculate absolute and relative errors directly; if not, report the stopping criterion as evidence rather than claiming exact error.

Rounding should occur after the update has been computed with adequate precision. Retaining only a few digits can corrupt the next derivative, divided difference, or function value, especially when cancellation occurs. In a worked solution, display enough digits to reproduce the next iterate and reserve the requested rounding for the conclusion.

### A local error model for the secant method

The secant slope is a finite-difference approximation to the derivative. If f is differentiable and x_(n−1),x_n are close, the mean value theorem gives a point ξ_n between them such that

$$
\frac{f(x_n)-f(x_{n-1})}{x_n-x_{n-1}}=f'(\xi_n).
$$

This explains why the chord can approximate the tangent near a simple root. It also explains its limitations: when the points are far apart, the sampled slope may not represent the local derivative at the root; when their function values nearly coincide, rounding can dominate the denominator. The secant recurrence is not a derivative-free guarantee, but a derivative estimate formed from two computed values.

For Newton, Taylor expansion around a simple root explains the leading error cancellation and the quadratic local rate. For secant, the derivative estimate changes with each pair, and the typical local order is superlinear but below quadratic. These rate statements assume smoothness, a simple root, and iterates already sufficiently near it. They should not be used to predict behavior for arbitrary starting guesses or nonsmooth functions.

### Residual checks and root-distance bounds

Suppose f is differentiable between an approximation x and a root α, and |f'(t)|≥m>0 throughout that segment. The mean value theorem gives f(x)−f(α)=f'(ξ)(x−α) for some ξ, so

$$
|x-\alpha|\le\frac{|f(x)|}{m}.
$$

This converts a residual into a location bound only when the derivative lower bound is known. A small residual alone does not provide that guarantee. For the source cubic, f'(x)=3x²+4x+10 is positive; on a specified interval such as [1,2], its minimum can be bounded, allowing a conservative conversion. The interval must be named because m may vary elsewhere.

The successive-step criterion has a different role. A small |x_(n+1)−x_n| indicates that the recurrence is making little movement. Under a contraction, successive differences can be related to the remaining distance, but for Newton and secant no universal factor applies without additional analysis. Reporting both step and residual is a useful diagnostic; calling either one the true error without qualification is not.

### Handling multiple roots and flat tangents

For a root of multiplicity m>1, f(α)=f'(α)=...=f^(m−1)(α)=0. The simple-root Newton convergence derivation assumes f'(α)≠0 and therefore does not apply. In common smooth cases, ordinary Newton still converges but only linearly, with a rate that worsens as multiplicity grows. If multiplicity is known, a modified Newton step may restore faster convergence, but that is a different algorithm and its assumptions must be stated.

Even for a simple root, an iterate can encounter a small derivative far from α. The resulting correction may be enormous. One safeguard is to limit step size or reject a step that leaves a trusted interval; another is to revert to a bracketed update. A small derivative is not fixed by rounding the quotient differently. It reflects a poorly conditioned local tangent calculation.

For secant, nearly equal consecutive function values lead to a small denominator, while nearly equal x-values can make the slope estimate sensitive. Check both the denominator and the magnitude of the correction. If function values are obtained from noisy measurements, finite differences can magnify that noise. The advantage of avoiding an explicit symbolic derivative must be balanced against the stability of estimating one numerically.

### A close reading of the secant correction

The secant update is sometimes written in a form that hides its geometry:

$$
x_{n+1}=\frac{x_{n-1}f(x_n)-x_nf(x_{n-1})}
{f(x_n)-f(x_{n-1})}.
$$

This expression is algebraically equivalent to x_n−f(x_n)(x_n−x_(n−1))/(f(x_n)−f(x_(n−1))). The second form displays a correction to the current point; the first displays the chord's x-intercept. Deriving one from the other is a useful check on index placement. In either form, the denominator is the difference of function values in the same order used in the numerator.

Changing the order of the two points in both numerator and denominator leaves the result unchanged; changing only one sign does not. This is a frequent source of errors when a table labels the older point x_0 and newer point x_1 but the formula is copied with reversed indices. Write the actual ordered pair explicitly before substitution and keep a sign around every difference until the quotient is evaluated.

For the example x_0=3,x_1=4, f(x_0)=−3, f(x_1)=5, both forms give x_2=3.375. At the next step, the ordered current point is x_n=3.375 and the previous point is x_(n−1)=4. The quotient is negative, so x_3 exceeds x_2. Agreement between the correction form, intercept form, and a rough graph is a useful triangulation of the arithmetic.

### Distinguishing local rate from total work

Quadratic convergence means that, once sufficiently close, the error is roughly squared at each Newton step. It does not mean Newton always uses fewer total function evaluations from any initial value. Derivative evaluation may be costly, a poor start may require safeguards, and a single unstable step can erase the local advantage. Secant generally uses fewer derivative-related operations, but needs two starts and may take more iterations.

When comparing algorithms, count the relevant work: function evaluations, derivative evaluations, storage of prior values, and any bracketing checks. A derivative can be available analytically, estimated numerically, or supplied by automatic differentiation; those choices have different costs and error characteristics. A secant method uses existing function evaluations to estimate slope, but the subtraction can lose significant digits when values are nearly equal.

The theoretical convergence order is one part of method selection, not the whole decision. The target root, smoothness, initial approximations, computation budget, and desired reliability determine whether Newton, secant, bisection, or a hybrid is appropriate. State the reason for selecting a method in terms of these properties rather than declaring one method categorically best.

### Deriving Newton's local error equation

The local convergence claim can be made more precise by writing e_n=x_n−α. Taylor expansion at a simple root gives f(x_n)=f'(α)e_n+\tfrac12f''(α)e_n^2+O(e_n^3) and f'(x_n)=f'(α)+f''(α)e_n+O(e_n^2). Dividing these expansions yields f(x_n)/f'(x_n)=e_n−[f''(α)/(2f'(α))]e_n^2+O(e_n^3). Since the Newton update subtracts this ratio from x_n=α+e_n, the first-order error cancels:

$$
e_{n+1}=\frac{f''(\alpha)}{2f'(\alpha)}e_n^2+O(e_n^3).
$$

The coefficient explains the observed rapid convergence when the assumptions hold. If the second derivative vanishes at the root, convergence may be even faster in special cases; if the derivative at the root vanishes, this simple-root derivation fails. The formula is an asymptotic local statement, not an assurance that every early iterate improves.

This derivation also clarifies why an error that is squared can gain digits quickly: an error near 10^−2 may lead to one near 10^−4, then near 10^−8, once the sequence is in the local regime. Actual constants and rounding affect the observed values. A finite list of iterates that seems to gain digits is consistent with the theory, but verifying the hypotheses is still necessary.

### Secant convergence as an approximate derivative process

The secant method uses a slope through two approximations instead of evaluating f'(x_n). If f is twice differentiable, a divided difference approaches the derivative as the two points coalesce. The new point is therefore approximately the Newton point, but the slope itself depends on the errors in both previous iterates. This dependence produces the familiar superlinear order near a simple root, often described by the positive solution of p^2=p+1, approximately 1.618.

The order comparison is useful but should be interpreted carefully. Newton's quadratic rate is higher locally, yet it pays for a derivative evaluation. Secant has a lower order but uses function values already needed to define the chord. If a derivative is available cheaply, Newton may require fewer total operations; if it is expensive, secant may be competitive. Neither rate describes the transient behavior from arbitrary starting values.

The secant recurrence can also be viewed as an interpolation method. The linear interpolant through the two latest data points is constructed and its zero is taken as the next approximation. This viewpoint explains why the method needs two points and why a small change in function values can make its intercept remote. The function's curvature and the placement of the points determine whether the chord is informative.

### Uniqueness and conditioning of the approved cubic

For f(x)=x^3+2x^2+10x−20, the derivative is positive on the real line. The discriminant of 3x^2+4x+10 is −104, so the quadratic has no real roots and remains positive. Thus f is strictly increasing, and the sign change from f(1)=−7 to f(2)=16 identifies the unique real root. This is stronger than merely observing that Newton converges from x_0=1.

Strict monotonicity also helps diagnose the residual. On [1,2], f'(x)=3x^2+4x+10 is increasing because f''(x)=6x+4>0, so f'(x)≥17 there. If a computed x lies in [1,2], the mean value theorem gives |x−α|≤|f(x)|/17. This provides a rigorous root-distance bound from the residual for this specific interval. The bound depends on the derivative lower bound; it should not be carried over to a different function or interval without proof.

An exact root is not necessary for this bound, but the interval must contain both x and α. If the iteration leaves [1,2], the constant 17 is no longer automatically valid. One must either establish a new derivative lower bound over a larger segment or use a different estimate. This illustrates how local numerical analysis is connected to the region in which the assumptions hold.

### When a derivative is approximated numerically

In an applied computation, f' may not be supplied symbolically. A centered finite difference can approximate it using nearby function evaluations, but this introduces a step-size choice. If the difference step is too large, truncation error from curvature is significant; if too small, subtraction cancellation and round-off can dominate. The resulting Newton-like method therefore has an additional derivative-approximation error beyond ordinary function evaluation.

The secant method can be interpreted as an adaptive finite difference whose step is the distance between recent iterates. It does not require the user to select a separate fixed difference parameter, but that does not make the slope exact. If the iterates are close and function values are rounded, the divided difference may be inaccurate. In engineering applications, units and scale also matter: a step of 10^−6 may be small in one variable and large in another.

If derivative evaluation is noisy or costly, a secant or bracketed method may be preferable. If a derivative is exact and inexpensive, Newton is often more efficient near a simple root. When neither method's assumptions are secure, bisection offers a predictable fallback. The algorithm choice should account for the source of f and f', not solely the formal order of convergence.

### A reproducible iteration record

A useful Newton table contains the current iterate, function value, derivative value, correction, and next iterate. A secant table contains two current points, their function values, the slope quotient, and the new point. Keeping those columns separate prevents a common indexing mistake in which the newest point is paired with the wrong older value.

Before reporting the final root, evaluate f at the rounded answer as well as at the unrounded iterate. Rounding can noticeably change the residual if f is steep. If the task requests five significant figures, calculate internally at higher precision, then round the final value and state the residual associated with either the unrounded approximation or the displayed value. Clear reporting makes the numerical evidence reproducible.
'''

extras["206_l3"] = r'''### Newton derivation, convergence, and failure analysis

Let α be a simple root of a differentiable function f. The tangent at x_n has equation y=f(x_n)+f'(x_n)(x−x_n). Its x-intercept solves 0=f(x_n)+f'(x_n)(x_(n+1)−x_n), giving

$$
x_{n+1}=x_n-\frac{f(x_n)}{f'(x_n)}.
$$

For an error analysis, write x_n=α+e_n and expand f about α. If f is twice continuously differentiable near α and f'(α)≠0, Taylor's theorem gives f(α+e_n)=f'(α)e_n+\tfrac12 f''(α)e_n^2+O(e_n^3), and f'(α+e_n)=f'(α)+f''(α)e_n+O(e_n^2). Substitution into the Newton correction cancels the leading e_n term, leaving an error of order e_n^2. This explains quadratic local convergence under the stated smoothness and starting-near-root conditions.

The cancellation depends on a nonzero derivative at the root and a starting point in the local regime. If f'(x_n) vanishes, the formula is undefined. If it is small, the correction can be large and amplify evaluation error. For a multiple root, f'(α)=0, so the simple-root derivation cannot be used; unmodified Newton may converge more slowly. A numerical method should therefore be accompanied by checks of derivative size and iterate behavior.

The secant method replaces f'(x_n) by [f(x_n)−f(x_(n−1))]/[x_n−x_(n−1)]. This divided difference is a slope estimate, so the update is the x-intercept of a chord. For a smooth function and two sufficiently close approximations to a simple root, the slope can track the derivative and produce superlinear convergence. The method is derivative-free, but the difference f(x_n)−f(x_(n−1)) can be small, causing numerical sensitivity. Two starting values are required, and no bracket is automatically preserved.

### Source Newton iteration with a convergence check

For f(x)=x^3+2x^2+10x−20, x_0=1, compute f'(x)=3x^2+4x+10. The source sequence is approximately

$$
x_0=1,\quad x_1=1.4117647,\quad
x_2=1.3693365,\quad x_3=1.3688082,\quad
x_4=1.3688081.
$$

The first correction is substantial because f(1)=−7 while f'(1)=17. Subsequent corrections become much smaller as the tangent approaches the root. This pattern is consistent with local quadratic convergence, but a few displayed values are evidence for this example, not a proof that all starting values converge.

The equation has one real root near 1.3688081; the derivative 3x²+4x+10 is positive for every real x because its discriminant is 16−120<0 and its leading coefficient is positive. Thus f is strictly increasing and cannot have more than one real root. Since f(1)<0 and f(2)>0, continuity confirms existence between 1 and 2. These facts help identify the target and interpret the Newton sequence. They do not eliminate the need to check computed accuracy.

Evaluate the final residual using the original polynomial and retain sufficient precision. A small residual supports the approximation, while the derivative lower bound on a known interval can convert residual to a root-distance bound by the mean value theorem: if |f'(x)|≥m>0 between x and α, then |x−α|≤|f(x)|/m. The bound is only valid when that derivative condition has actually been established.

### Correct secant calculation and sign discipline

For f(x)=2x²−6x−3, take x_0=3 and x_1=4. The values are f(3)=−3 and f(4)=5, so

$$
x_2=4-5\frac{4-3}{5-(-3)}=3.375.
$$

The next step uses x_1=4, x_2=3.375, f(x_1)=5, and f(x_2)=−0.46875:

$$
\begin{aligned}
x_3&=3.375-(-0.46875)\frac{3.375-4}{-0.46875-5}\\
&=3.375-\frac{0.29296875}{-5.46875}\\
&\approx3.428571.
\end{aligned}
$$

The sign in the denominator is negative. The quotient is therefore negative, and subtracting it increases the iterate. Replacing the negative denominator by its magnitude without changing the formula incorrectly gives approximately 3.321429. Substitution back into the secant recurrence is an effective arithmetic audit.

The exact positive root is (3+√15)/2≈3.4364917, so x_3 is still about 0.00792 below it. The quadratic also has a negative root; the starting pair and target must be understood in context. A secant sequence can cross the root or move outside the initial interval because the method is not a bracketing method. If containment is required, use bisection or a safeguarded secant variant.

### Choosing starts and safeguarding open iterations

For Newton's method, a useful initial value is one where the tangent is informative and the derivative is not too small. A sign-changing interval can identify a target root and help select a start, although the Newton iterates themselves may leave it. For the secant method, choose two distinct points whose function values differ substantially enough to define a stable chord, while still lying in a region associated with the desired root.

Monitor each update for a small denominator, a very large correction, repeated rounded values, or a residual that grows. These are warning signals, not necessarily proofs of failure. A practical safeguard can reject a proposed step outside a trusted interval and fall back to bisection. This combines the speed of an open method near the root with the containment of a bracket.

The method comparison should be based on function and derivative costs, reliability needs, and available information. Newton often takes fewer iterations when derivatives and good starting values are available. Secant avoids explicit differentiation but needs two starts and can be more sensitive. Bisection converges more slowly but supplies a direct interval bound. The best choice is the one whose hypotheses match the problem and whose result can be checked.

### Distinguishing residual, step, and true error

The true error e_n=x_n−α cannot generally be computed when α is unknown. A residual |f(x_n)| measures how well the approximate point satisfies the equation. A step size |x_(n+1)−x_n| measures how much the iteration changed. They are useful indicators but not interchangeable with true error without additional conditions.

Near a simple root, f(x)≈f'(α)(x−α), so the residual is approximately |f'(α)| times the root error. A small derivative can make the residual deceptively small for a larger location error; a large derivative can yield a larger residual even when the location is close. A derivative bound and the mean value theorem provide a justified conversion. Otherwise, describe the residual and step as stopping tests, not certified error bounds.

Finite precision introduces another subtlety. When updates become smaller than the representable spacing of x_n, the stored value may stop changing. This stagnation can happen before the requested accuracy is met. Recompute with additional precision or inspect the residual and rounding interval instead of interpreting equality of successive displayed decimals as proof of convergence.

### Presenting a complete numerical solution

A complete Newton solution defines f, differentiates correctly, writes the recurrence, substitutes the initial approximation, and reports successive iterates. It also checks the derivative denominator and confirms the result in the original equation. If the task requests a specified decimal accuracy, state the stopping test and retain enough intermediate digits to support the rounding.

A complete secant solution lists both starting points and function values, writes the divided-difference formula, and carefully tracks the two most recent iterates. Showing the signs in both numerator and denominator prevents the correction error illustrated above. Conclude with a residual or comparison, and avoid calling a result “correct to” a stated number of digits unless the error evidence supports that claim.

### Conditioning of the equation versus stability of the iteration

The sensitivity of a root to a perturbation in f is different from the convergence behavior of Newton or secant. Near a simple root α, a perturbation δf in the function value corresponds approximately to a root displacement δx≈−δf/f'(α). If |f'(α)| is small, the root itself is sensitive to data or evaluation errors. Separately, the iteration may be unstable because a derivative denominator is small or a secant slope is inaccurate. A method can converge to an ill-conditioned root, and a well-conditioned root can still be approached poorly from an unsuitable starting point.

This distinction helps interpret digits. A computed sequence agreeing in many decimal places does not ensure that the mathematical root is equally insensitive to rounded coefficients or measurements. Conversely, if the polynomial coefficients are exact and the iteration converges, arithmetic error may dominate the final discrepancy. State what is known about the input and what is being estimated.

For the quadratic 2x²−6x−3, the exact positive root supplies an independent benchmark. The secant iterate x_3≈3.428571 differs from (3+√15)/2 by about 0.00792. Since the root is not especially flat—the derivative 4x−6 at the positive root is about 7.746—the residual and location error are of comparable scale. This is specific to this example; it should not be generalized without an interval derivative bound.

### A safeguarded open-method workflow

An effective workflow begins with a sign-changing interval whenever one is available. Verify continuity and endpoint signs, then choose a starting point inside the bracket. Compute a Newton or secant proposal and check that its denominator is safe and the proposal is finite. If it lies outside the bracket or fails to reduce the residual, use a bisection midpoint instead. Update the bracket by function signs after every accepted evaluation.

The safeguarded method uses the fast local model when it behaves well while retaining an interval guarantee. The method is no longer pure Newton or pure secant, so a report should name it accurately. The workflow also separates root existence from root convergence: the initial bracket supplies existence, and the controlled updates maintain containment.

Safeguarding is especially useful when the function has curvature that changes rapidly or when the starting values are only rough. It does not eliminate the need for function evaluations or careful sign handling. If a function is discontinuous inside the bracket, opposite endpoint signs do not guarantee a root, so the continuity hypothesis must still be checked.

### Why the secant sign correction matters

The source quadratic provides a compact arithmetic audit because the second secant correction is negative. At x_2=3.375, f(x_2)=−0.46875; relative to x_1=4, the change in x is −0.625 and the change in f is −5.46875. Their product in the numerator is positive, while division by the negative function difference makes the correction quotient negative. The update subtracts a negative quantity, giving x_3≈3.428571.

The erroneous value 3.321429 results from replacing the negative denominator by its magnitude but retaining the subtraction. One can catch this by checking signs before using a calculator: a secant through (4,5) and (3.375,−0.46875) crosses the x-axis near 3.43, not to the left of 3.375. A rough geometric check is not a proof, but it is a useful independent warning when an algebraic sign seems suspicious.

### Choosing and stating the stopping rule

For a bracketed process, stop when the interval is narrow enough that its endpoints round to the same requested answer. For Newton or secant, combine a small residual with a small update and, if possible, a local error bound. If a reference root is available, calculate the observed absolute error. If not, avoid declaring a number of correct digits solely from repeated decimal agreement.

The final report should identify the method, initial values, target root, stopping criterion, and approximation. For Newton, include the derivative and note how it was evaluated. For secant, include the pair of recent iterates and the divided-difference denominator. For both, a residual check in the original equation helps detect transcription errors. This information makes a numerical answer reproducible and makes its limitations visible.

### A rounding guarantee for displayed digits

If the exact root is unavailable, the display of several stable decimals is not itself a proof that those digits are correct. To certify rounding, one needs an interval known to contain the root and narrow enough that both endpoints round to the same value, or a numerical error estimate strong enough to imply that result. Open methods do not provide such an interval automatically. A bracketing method can be retained alongside Newton or secant to supply one.

For the source quadratic, an exact root is available, so the secant result can be checked directly. For a general equation, the final statement should say “approximately” and name the stopping evidence. If a method is stopped because |f(x_n)| is small, that is a residual tolerance; if stopped because consecutive iterates differ little, that is a step criterion. Neither should be relabeled as an absolute root-error guarantee unless a theorem justifies the conversion.

The distinction is especially important when results are used downstream. If an approximate root is substituted into another computation, its uncertainty may propagate. Retaining a bracket or an error estimate enables that uncertainty to be carried into the later quantity. Supplying many digits without a justified accuracy can create false confidence in all subsequent calculations.

### A method-selection summary tied to hypotheses

Newton's formula is attractive when f is differentiable, f' is inexpensive, and a starting point is near a simple root. Secant is attractive when derivatives are inconvenient and two reasonable starting points are available. Bisection is attractive when a continuous sign-changing bracket is known and predictable containment matters. A hybrid can combine the speed of an open step with the safety of a bracket.

The hypotheses are not ceremonial. Without continuity, a sign change may occur across a jump rather than a zero. Without a nonzero Newton derivative, the tangent update may fail. Without distinct secant function values, the chord intercept is undefined. Without a suitable initial region, either open method may converge to another root or diverge. A solution that states these conditions explains why its computational result should be trusted.

### Continuing the corrected secant sequence

The first corrected estimate x_3≈3.428571 is not the final answer. Continuing with the two most recent points gives x_4≈3.436619718, then x_5≈3.436491411. The exact positive root is α=(3+√15)/2≈3.436491673. The error at x_3 is about 0.00792; at x_4 it is about 0.000128; at x_5 it is about 2.62×10^−7. This short sequence illustrates the accelerated convergence after the chord points enter the local region.

The residuals show the same pattern: f(x_3)≈−0.06122449, f(x_4)≈0.00099187, and f(x_5)≈−2.03×10^−6. Their signs alternate as the iterates cross the root. The residual is not numerically equal to the location error; the derivative near the positive root is about 7.746, so the two are related by a scale factor. The exact root permits a direct error comparison here; in a problem without an exact root, a residual alone would not reveal the true error.

The secant sequence has no interval guarantee despite these favorable results. Its first two points happen to straddle the positive root, but later points are selected by chord intercepts and could in another problem leave the interval. The fact that this particular example converges does not make the secant method a bracketing method. A rigorous implementation that needs containment must test the proposal against a maintained bracket.

### Newton's source sequence and local error ratios

For the cubic example, once the iterates are close enough, one can examine the ratio |e_(n+1)|/|e_n|^2 if an accurate reference root is available. A ratio that approaches a finite nonzero constant is consistent with quadratic convergence. Without the exact root, consecutive differences can serve as an approximate error proxy, but the ratio then remains diagnostic rather than a proof.

The source iterates x_1≈1.4117647 and x_2≈1.3693365 differ substantially; later x_3≈1.3688082 and x_4≈1.3688081 are much closer. This pattern shows the transition into the local regime. It would be inaccurate to infer that Newton is quadratic from the first update alone. The local theorem requires a simple root, sufficient smoothness, and a starting point close enough that the tangent approximation is effective.

The cubic is strictly increasing, so the positive-direction root is unique. Since f'(x) stays positive, Newton's correction has the opposite sign of the residual. This explains why the first step moves right from a point with negative residual and the next step moves left when it crosses to positive residual. Such sign checks make an iteration trace easier to understand than a table of decimals alone.

### Error amplification in arithmetic operations

The Newton correction is a quotient. If the stored function value is f(x_n)+δ_f and derivative is f'(x_n)+δ_d, perturbations in either input affect the quotient. A first-order sensitivity calculation gives a correction perturbation approximately δ_f/f'−fδ_d/(f')^2. When f' is small, both terms can be magnified. This is the numerical reason to watch derivative size rather than treating division as harmless.

In the secant quotient, both numerator and denominator are differences of approximate values. If f(x_n) and f(x_(n−1)) are nearly equal, their subtraction may lose significant digits. If the points are close, the x difference can be small too. Scaling the function by a nonzero constant does not change its roots or the exact secant iterate, but it can change floating-point behavior if values overflow, underflow, or lose precision. Good implementation uses appropriate scaling and avoids unnecessary cancellation.

These are arithmetic effects distinct from convergence theory. A mathematically convergent iteration in exact arithmetic can stagnate or become noisy in finite precision. Conversely, a few stable digits in a calculator output do not establish mathematical convergence. A complete discussion distinguishes the ideal method, the computed sequence, and the precision of the data.

### An applied decision and stopping example

Suppose the goal is five significant figures for the positive root of 2x²−6x−3. The exact root here is available for audit, but an ordinary computation can stop when consecutive estimates agree to the requested rounding and the residual is small. The corrected secant value x_5≈3.436491411 rounds to 3.4365. The exact root also rounds to 3.4365, confirming the result. If the exact root were unknown, one would state the iteration and residual criterion and avoid claiming a certified five-significant-figure result absent a bound.

If a guaranteed answer is required, bracket the root first. The quadratic has f(3)=−3 and f(4)=5, so [3,4] is a valid bracket. Bisection can shrink this interval to a width small enough that every point rounds to the same five-significant-figure value. A safeguarded secant algorithm can use chord estimates when they remain inside the bracket and bisect otherwise. The extra bookkeeping buys a clear certification.

### Root-finding as a sequence of justified decisions

The analysis proceeds in order. Establish a root or a target interval; determine whether it is unique there; select a recurrence whose assumptions fit the function; calculate updates with adequate precision; monitor denominators and residuals; then justify the final rounding. Skipping the first steps can lead to convergence to the wrong root. Skipping the checks can preserve a sign mistake for several iterations. Skipping the final justification can overstate accuracy.

This sequence of decisions is shared by all methods, even though their formulas differ. Bisection emphasizes a sign invariant, fixed-point iteration emphasizes the map's contraction, Newton emphasizes the tangent and derivative, and secant emphasizes the chord and divided difference. Understanding those structures makes it possible to diagnose behavior rather than mechanically repeat a recurrence.
'''

extra2 = {}
extra2["205_l1"] = r'''### Checking a root estimate by interval and sign

After a bisection calculation, the midpoint is not the only useful output. The signed endpoint values and final interval together communicate both the location and existence guarantee. If the final interval is [a_n,b_n], state f(a_n)f(b_n)<0 and its width. The root is somewhere in that interval, so any estimate selected from it has a clear absolute bound. This is stronger than saying that a plotted curve appears to cross near the printed number.

The source cubic is strictly decreasing on [0,1], which means there is exactly one root in the initial interval. Its bisection table keeps that root enclosed. If a reader sees the midpoint 0.203125 without the interval, the number alone provides no proof that it is near the root. If the reader sees the interval and sign invariant, the accuracy claim is independently checkable. Thus the endpoints are part of the mathematical answer.

### Keeping a fixed-point calculation reproducible

For x_(n+1)=ln(2x_n+7), record the input x_n, the argument 2x_n+7, and the logarithm result before rounding. This helps distinguish a mistaken algebraic substitution from a calculator-entry error. The logarithm has a restricted domain, and the interval [2,3] ensures the argument is positive at every step. A sequence table should retain enough digits that the next argument is recomputed consistently.

If x_(n+1) and x_n agree to the displayed precision, calculate at higher precision before stopping. Two rounded iterates can appear identical because the update is smaller than the display unit, even though their unrounded values differ. The contraction bound can determine whether the remaining error is acceptable; otherwise, report the observed step as an empirical stopping test.
'''

extra2["205_l2"] = r'''### A worked contraction estimate from observed changes

For the logarithmic fixed-point map on [2,3], k=2/11 is valid. Suppose a computed iteration produces |x_n−x_(n−1)|=0.00045. The future differences decrease by at least the factor k, so their total is bounded by the geometric series k d_n+k²d_n+... . The remaining distance from x_n to the limit is at most k d_n/(1−k), which here is (2/9)(0.00045)=0.0001. This bound is valid because the entire orbit remains in the contraction interval.

If the same numerical difference were observed for a map with k=0.95, the corresponding factor would be 19, and the bound would be 0.00855. Therefore, a small consecutive change is much less convincing when the contraction is weak. Convergence rate information is necessary to interpret the difference. This calculation also shows why the stopping test should include the contraction constant rather than a universal threshold alone.

### A second look at the bisection correction

The corrected bisection values for e^x−2x−7 can be cross-checked from the exact endpoints. At x=2, f(2)=−3.610944; at x=2.5, f(2.5)=+0.182494. Therefore [2,2.5] is the bracket after the first midpoint, and its midpoint 2.25 has f(2.25)≈−2.0127. The next interval is [2.25,2.5], not [2.5,2.75]. The latter interval does not even contain the known root near 2.4818.

This correction matters beyond one sign. An invalid interval destroys the IVT-based error guarantee; further halving of an invalid bracket does not restore it. Always verify the endpoint sign invariant before calculating a width-based accuracy bound. A sequence of midpoints can be arithmetically consistent and still be mathematically irrelevant if the initial sign update is wrong.

### Monotonicity and root identity

For f(x)=e^x−2x−7, f'(x)=e^x−2. On [2,3], this derivative is positive, so f is strictly increasing there. The endpoint sign change therefore identifies exactly one root. The logarithmic fixed-point map also has a unique fixed point in [2,3] because it is a contraction. These are complementary proofs: monotonicity addresses uniqueness of the root of f, while contraction addresses uniqueness and convergence of the fixed point under g.

The two proofs should not be conflated. A function can have a unique root even when a chosen fixed-point map does not converge. Conversely, a contraction map has a unique fixed point on its invariant interval, but one must still verify that the fixed-point equation is equivalent to the original root equation there. The domain condition for the logarithmic rearrangement supplies that link in this example.

### Choosing precision from the theorem

If a target absolute error ε is given for a bisection midpoint and the starting interval width is L, choose n so that L/2^(n+1)≤ε. If a tolerance applies to the whole bracket, require L/2^n≤ε. Write the inequality first, then solve for the integer n by rounding upward. A computation that stops one iteration too early may miss the requirement even if its midpoint happens to be unusually close.

For fixed-point iteration, an a priori bound needs an upper bound on the starting error, while the a posteriori bound uses the latest step and k/(1−k). Neither should be replaced by an arbitrary count of stable decimals. The theorem supplies a relation between computed quantities and the unknown root; the numerical answer should reflect that relation precisely.
'''

extra2["205_l3"] = r'''### Detailed iteration table construction

To construct a bisection table without losing the invariant, begin by evaluating both endpoints and writing their signs. For each row, calculate the midpoint from the current endpoints, evaluate f there, and compare its sign with the left endpoint. If the signs differ, carry the left endpoint forward and replace the right endpoint by the midpoint. If the signs agree, replace the left endpoint. The two retained endpoints then have opposite signs.

For the source cubic, f(0)=1 and f(1)=−3. The first midpoint 0.5 has a negative value, so the upper endpoint becomes 0.5. At 0.25 the value is still negative, so the upper endpoint becomes 0.25. At 0.125 the value is positive, so the lower endpoint becomes 0.125. The table then follows the same rule at every stage. This procedural description is important because a table of values alone does not identify which endpoint should be replaced.

### Exact sign calculations near the source root

The values at the early dyadic midpoints can be checked exactly. At x=1/2, f=1/8−5/2+1=−11/8. At x=1/4, f=1/64−5/4+1=−15/64. At x=1/8, f=1/512−5/8+1=193/512. The signs are unambiguous. Exact fractions are especially helpful when the polynomial is evaluated near zero and a rounded decimal might obscure the sign.

At x=3/16=0.1875, the value is positive; at x=7/32=0.21875 it is negative. These rational abscissae yield the lesson's final bracket. The exact values are less important than their signs for bisection, but computing them accurately validates the retained interval. If a calculator provides a tiny residual, preserve enough precision to decide the sign reliably.

### Uniqueness proof and interpretation of the interval

On [0,1], f'(x)=3x^2−5≤−2<0. Therefore f is strictly decreasing throughout the entire bracket. This derivative bound proves uniqueness there and also makes the sign pattern intuitive: as x increases, f crosses zero once from positive to negative. The IVT alone would guarantee existence but not uniqueness.

On intervals outside [0,1], the derivative may change sign, so this simple monotonicity argument no longer applies. A cubic can have up to three real roots; the given starting interval identifies one root rather than all roots. When a question asks for all solutions, one bisection run is not enough. Analyze the function's turning points and establish separate brackets for distinct roots.

### Fixed-point iteration compared by theorem

The fixed-point map g(x)=ln(2x+7) has g'(x)=2/(2x+7), which is at most 2/11 on [2,3]. It maps the interval into itself. Thus the contraction theorem ensures a unique fixed point and convergence for every start in the interval. The error contracts by a factor no greater than 2/11 at each iteration, a strong guarantee.

The alternate map h(x)=(e^x−7)/2 is algebraically equivalent at a solution, but h'(x)=e^x/2 exceeds one throughout [2,3]. It does not satisfy the contraction condition there, and numerical iteration from 2.5 moves away rapidly. This contrast shows that the equation's algebra is not enough to determine the iterative behavior; the derivative of the chosen map matters.

### Limitations of empirical convergence evidence

An iteration sequence may appear stable because the displayed decimal precision is too low, because successive values alternate with diminishing amplitude, or because arithmetic has stagnated. These observations are not the same as a theorem. For bisection, verify the bracket and width. For contraction iteration, state k and the invariant interval. For Newton or secant, monitor residual and step and use a local convergence result only when its assumptions are met.

When an error bound is unavailable, an honest report can still be useful: list the last iterates, their difference, and the residual, and label these as empirical indicators. Avoid claiming a certified number of correct digits. Numerical analysis is strengthened, not weakened, by making the distinction between evidence and guarantee explicit.
'''

extra2["206_l1"] = r'''### A reliable stopping conversation

During an iteration, “the numbers are close” is not a complete stopping rule. Ask what is close: the last two iterates, the residual, or the true root location? For Newton on the source cubic, one can compute a residual and compare consecutive values, but exact error is unknown unless a reference or theorem is used. For the quadratic secant example, an exact root is available, so absolute error can be checked directly.

If a numerical application needs a guaranteed tolerance, maintain a bracket or establish an error bound. If it only needs a practical estimate, a combined step-and-residual threshold may be adequate, provided the result is reported as an estimate. The distinction prevents a common communication error: describing a stopping criterion as though it were a proof of accuracy.

### Units and scaling in the function

Multiplying f by a nonzero constant leaves its roots unchanged and, in exact arithmetic, leaves Newton's quotient f/f' unchanged. The secant formula is also unchanged because its function differences scale by the same constant. This algebraic invariance can be useful when rescaling a function whose values are extremely large or small.

However, finite arithmetic can react differently after scaling. Overflow, underflow, cancellation, and rounding may occur at different points. Scaling does not improve the conditioning of a root automatically, but can make evaluations numerically safer. Keep the original equation available for the final residual check so that a transformed or scaled computation is interpreted correctly.
'''

extra2["206_l2"] = r'''### A step-by-step comparison of exact and approximate information

The quadratic example has an exact positive root, so it can be used to distinguish three pieces of information. The iterate x_3≈3.428571 is the numerical result of two secant updates. The exact root α≈3.436491673 is an independent benchmark. The absolute error |x_3−α|≈0.00792 is an observed error available only because α is known. In a general equation, the first item remains available but the other two may not be.

For the source cubic, the root is not supplied in closed form. The sequence x_1 through x_4 and the residual at x_4 provide evidence, while monotonicity and a derivative lower bound can strengthen the conclusion. If x_4 lies in [1,2], f'(x)≥17 there, so |x_4−α|≤|f(x_4)|/17. This illustrates how structural analysis can provide an error bound even without a formula for α.

### Why local convergence does not resolve root selection

Newton's local theorem states that a sequence started sufficiently near a simple root converges to that root. It does not identify which root is “sufficiently near” without analysis, nor does it say that every initial point converges. A function with several roots can have separate attraction regions. A starting value near the boundary between those regions may move unpredictably or converge to a different root than intended.

The secant method has the same root-selection issue and adds dependence on two starts. The line through those two function points can intersect the axis near any root influenced by the local geometry. A sign-changing bracket is useful for identifying a target even if the pure open iteration is not constrained to it. When multiple roots are possible, specify the interval or use a safeguarded method.

### Correct use of residual-based bounds

If f is differentiable and its derivative magnitude is bounded below by m>0 on the segment from x to α, then the mean value theorem gives |x−α|≤|f(x)|/m. The lower bound matters. A derivative upper bound does not provide the same conclusion, and a derivative that vanishes between x and α invalidates the simple inequality.

For the source cubic on [1,2], f'(x)=3x²+4x+10 is increasing, so m=17 is valid. If an approximate Newton iterate has residual 10^−6 and lies in the bracket, its root error is at most about 5.9×10^−8. This bound is conservative and depends on both the interval and derivative calculation. It is not justified for a point outside [1,2] without a new bound.

### Error sources and significant figures

An iterative answer may have truncation error from stopping after finitely many steps, round-off from arithmetic, and input uncertainty from rounded coefficients or measurements. The exact polynomial examples isolate truncation and arithmetic; an applied model may include all three. Stating five significant figures should mean that the computed uncertainty supports that rounding, not merely that the calculator displays five digits.

When function values are obtained from rounded data, the root itself may shift if the data are perturbed. This is problem conditioning, not necessarily a failure of Newton or secant. If f'(α) is small, a small perturbation in f can cause a large displacement in α. Separate sensitivity of the mathematical root from numerical stability of the iteration when interpreting precision.

### Why a hybrid may be preferable

An open method proposes a root from local slope information. A bracketing method maintains a global sign invariant. A hybrid can accept a Newton or secant proposal when it is safe and informative, but use bisection when the proposal is outside the current bracket or the denominator is unreliable. The interval shrinks even if the open step is rejected.

This strategy requires additional function evaluations and bookkeeping, but gives a dependable fallback. It is useful when derivative information is available but the initial guess is not especially close, or when the cost of a failed iteration is high. The final description should name the hybrid rather than claiming the pure Newton or secant convergence guarantee applies unchanged.
'''

extra2["206_l3"] = r'''### The convergence hypotheses in operational form

The usual local Newton result can be summarized operationally: f should be sufficiently smooth near α, α should be a simple root, and x_0 should be close enough that the tangent update remains in the local region. “Close enough” depends on f and is not supplied by the recurrence. The theorem explains rapid convergence once the method enters that region, not how to choose a universally safe starting point.

For secant, two starting values should be distinct, their function values should not coincide, and the pair should be positioned so that the chord approximates the local tangent. The method is sensitive to the pair as well as to the function. If the denominator is zero, the next point is undefined; if it is tiny, rounding can dominate. A valid numerical implementation checks these conditions on every step.

### Mapping stopping criteria to the requested result

A tolerance on the iterate difference, a tolerance on the residual, and a tolerance on the root error are three different specifications. If the task says “iterate until successive approximations differ by less than 10^−4,” the step criterion is the requested stopping rule. If it says “find a root with residual below 10^−4,” evaluate |f(x_n)|. If it says “root accurate within 10^−4,” one needs a location error estimate or bracket width.

This distinction is not pedantic. For a steep f, a residual of 10^−4 may correspond to a very small x error. For a flat f, the same residual may correspond to a much larger error. A small step can also occur far from the root if a method stagnates. Read the task literally and state which computed quantity certifies its requested condition.

### An independent sign check on the quadratic

The exact positive root of 2x²−6x−3 is (3+√15)/2, between 3.43 and 3.44. The first secant point x_2=3.375 is below it, and f(x_2)<0. The next secant point x_3≈3.428571 remains below the root and has a smaller negative residual. The following point x_4≈3.436620 is slightly above the root and has a small positive residual.

This sign pattern agrees with the exact comparison and helps validate the secant arithmetic. It also shows why “moving toward the root” is not identical to “staying on one side.” A chord method can cross the root. Residual signs can be used to form a bracket after an iterate crosses, but the pure secant recurrence does not preserve that bracket automatically.

### Error order and measured progress

Quadratic convergence predicts that error ratios approximately satisfy e_(n+1)≈C e_n² near a simple root. Secant has a superlinear order p satisfying p²=p+1 under standard assumptions. These statements describe the asymptotic relation between successive errors, not a fixed number of correct digits at every iteration.

When the exact root is unavailable, one can examine ratios of successive step sizes as an informal diagnostic. Such ratios may suggest entry into an asymptotic regime, but they are not a proof because the step is only a proxy for the error. A formal analysis needs assumptions and, for certification, an error estimate. Keep convergence order as an explanation of expected local efficiency rather than a universal stopping certificate.

### Arithmetic checks for the Newton polynomial

For f(x)=x^3+2x²+10x−20, the derivative is always positive, so the Newton correction has sign opposite to f(x). At x_0=1, f<0 and the update is to the right. Once an iterate is to the right of the unique root, f>0 and the update is to the left. This sign logic matches the source sequence and is an efficient check on a computed correction.

The derivative is increasing on [1,2] because f''(x)=6x+4>0. Therefore its minimum there is f'(1)=17. If a reported iterate remains in this bracket, the residual bound |x−α|≤|f(x)|/17 is available. If the iterate leaves the bracket, do not use that bound automatically. Establish a new interval and derivative lower bound or report only the residual.

### A practical algorithm audit

Before accepting a computed root, check the following reasoning in sequence: the target root is identified; the formula is derived with consistent indices; required denominators are nonzero; the iterates remain in a sensible region; the original function has a small residual; and the stopping evidence supports the stated digits. If an exact root or sign-changing interval exists, compare against it independently.

For Newton, differentiate the original f and check the derivative at every iterate. For secant, maintain the correct previous and current pairs and evaluate both function differences in the same order. For both, preserve guard digits and round only at the end. These practical checks are the numerical counterpart of verifying hypotheses in a convergence theorem.
'''

for key,text in extra2.items():
    extras[key]=extras[key]+"\n\n"+text

def build_and_save(tid, ids, notes):
    from django.db import transaction
    from django.utils import timezone
    from prep.models import PrepTopic, PrepContentCache
    from services.prep_ai_router import (
        _cache_payload_as_dict, _note_validation_options, _note_completion_issues,
        _topic_notes_cache_signature, _course_study_profile_version,
        _topic_content_rules_version, NOTE_VALIDATION_STATE,
    )
    from services.prep_blocks import parse_markdown_to_blocks

    labels = r["LABELS"]
    topic = PrepTopic.objects.get(pk=tid, course_id=48)
    rows = {x.pk: x for x in PrepContentCache.objects.filter(
        pk__in=ids.values(), topic=topic, content_type="topic_notes")}
    if set(rows) != set(ids.values()):
        raise RuntimeError(f"Rows changed for topic {tid}: {sorted(rows)}")
    options = _note_validation_options(
        topic.course, topic.title, topic.summary, topic.subtopics, topic_obj=topic)
    signature = _topic_notes_cache_signature(
        topic.course, topic, topic.title, topic.subtopics)
    candidates = {}
    for level, rid in ids.items():
        row = rows[rid]
        payload = _cache_payload_as_dict(row.payload)
        if payload.get("level") != level:
            raise RuntimeError(f"Cache {rid} level changed")
        original = str(payload.get("content") or "")
        content = original
        if tid == 205 and level == "level_2":
            content = content.replace(
                r"f(2.5)\approx-0.817<0", r"f(2.5)\approx+0.182494>0")
            content = content.replace(
                r"f(2.75)\approx 3.07>0", r"f(2.25)\approx-2.0127<0")
            content = content.replace(
                r"[2.5,3]", r"[2,2.5]")
            content = content.replace(
                r"[2.5,2.75]", r"[2.25,2.5]")
        if tid == 206 and level in ("level_2", "level_3"):
            content = content.replace(
                r"3.375-\frac{0.29296875}{5.46875}\approx 3.32143",
                r"3.375-\frac{0.29296875}{-5.46875}\approx 3.428571")
        if tid == 205 and level == "level_2":
            for wrong in (r"f(2.5)\approx-0.817<0", r"f(2.75)\approx 3.07>0"):
                if wrong in content:
                    raise RuntimeError(f"Uncorrected bisection arithmetic in cache {rid}: {wrong}")
        if tid == 206 and level in ("level_2", "level_3") and "3.32143" in content:
            raise RuntimeError(f"Uncorrected secant arithmetic in cache {rid}")
        sec5 = r["section"](content, 5)
        content = r["replace_section"](
            content, 5, sec5 + "\n\n" + notes[level])
        content = r["norm"](content)
        count = len(re.findall(r"\b[\w’'-]+\b", content))
        prose_count = prose_word_count(content)
        if count <= 5000:
            raise RuntimeError(f"Cache {rid} only {count} words")
        issues = _note_completion_issues(
            content, topic.title, level=level,
            allow_validated_legacy_headings=False, **options)
        if issues:
            raise RuntimeError(f"Cache {rid} validation issues: {issues}")
        blocks = parse_markdown_to_blocks(content)
        if not blocks:
            raise RuntimeError(f"Cache {rid} parsed no blocks")
        candidates[rid] = (level, payload, original, content, blocks, count)
        print("CANDIDATE", rid, level, "words", count, "prose", prose_count, "blocks", len(blocks))

    import os
    if os.environ.get("SMA330_SAVE") != "1":
        print("PREFLIGHT_ONLY", tid)
        return
    with transaction.atomic():
        for rid, (level, payload, original, content, blocks, count) in candidates.items():
            row = PrepContentCache.objects.select_for_update().get(
                pk=rid, topic_id=tid, course_id=48, content_type="topic_notes")
            current = _cache_payload_as_dict(row.payload)
            if current.get("level") != level or current.get("content") != original:
                raise RuntimeError(f"Cache {rid} changed immediately before edit")
            payload.update({
                "content": content, "blocks": blocks, "source_signature": signature,
                "validation_state": NOTE_VALIDATION_STATE,
                "validated_at": timezone.now().isoformat(),
                "source_references": options.get("source_references") or [],
                "study_profile_version": _course_study_profile_version(topic.course),
                "topic_content_rules_version": _topic_content_rules_version(topic),
            })
            row.payload = payload
            row.save(update_fields=["payload", "updated_at"])
    print("UPDATED_TOPIC", tid, sorted(candidates))


build_and_save(205, {"level_1":1297, "level_2":1261, "level_3":1367}, {
    "level_1": extras["205_l1"], "level_2": extras["205_l2"], "level_3": extras["205_l3"]})
build_and_save(206, {"level_1":1360, "level_2":1262, "level_3":1338}, {
    "level_1": extras["206_l1"], "level_2": extras["206_l2"], "level_3": extras["206_l3"]})
