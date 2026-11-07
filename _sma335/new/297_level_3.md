## 1. Foundational Concepts, Definitions, and Axioms

### 1.1 What this topic is worth

This topic is examined as translation plus solution. Almost every question hands you a physical description and asks you to produce a differential equation, solve it, and answer one numerical question about it. The marks are distributed across the three activities, and the last of them is where careless candidates lose ground: a correct formula with no interpretation can still lose the final mark of a part.

| Question type | Typical marks | Target time | Where the marks sit |
| --- | --- | --- | --- |
| Growth or decay with a stated half-life | 5 to 6 | 7 minutes | One for the law, one for the solution, two for the constant, one per numerical part |
| Newton's law of cooling | 5 to 6 | 7 minutes | One for the law with the correct excess, one for the solution, two for the constant, one for the interpretation |
| Tank with equal inflow and outflow rates | 7 to 8 | 9 minutes | Two for the two rates, one for the balance law, one for the condition, three for the solution, one for the limit |
| Tank with unequal rates | 8 to 10 | 11 minutes | Everything above plus the volume function and the integrating factor |
| Coil and resistor with constant supply | 6 to 7 | 8 minutes | One for Kirchhoff's law, two for the integrating factor, one for the condition, one for the steady current |
| Capacitor charging | 6 to 8 | 9 minutes | One for the loop equation, one for the relation between charge and current, two for the solution, one for each part |
| Coil or capacitor with sinusoidal supply | 7 to 9 | 12 minutes | Two for the particular integral, two for the matching, one for the transient, one for the phase |
| Second-order circuit with classification | 10 to 12 | 15 minutes | Two for the equation, two for the roots, two for the classification, three for the constants, one for the interpretation |
| Two-mass spring system | 8 to 10 | 15 minutes | Two for the equations, three for the eigenvalues, two for the eigenvectors, three for the conditions |
| Bookwork: state the governing equation of a circuit | 2 to 3 | 2 minutes | One for each term named correctly |

The pattern is stable across papers, and it dictates strategy. The bookwork marks at the start of a question are the cheapest on the paper; the last mark of each part, awarded for interpretation, is the second cheapest; the middle marks for constants and signs are where most of the losses occur.

### 1.2 The five families of question

Every question in this topic belongs to one of five families, and each family has a fixed opening move.

The first family is growth and decay. The trigger phrases are rate of change proportional to the amount present, half-life, doubling time, percentage remaining. The opening move is to write $\frac{dx}{dt}=kx$ with $k$ positive for growth and negative for decay, then to convert the half-life or doubling time into $k$.

The second family is cooling. The trigger phrase is rate of cooling proportional to the excess over the surroundings, or a body placed in a room of stated temperature. The opening move is to write $\frac{dT}{dt}=-k\left(T-T_{s}\right)$ and to introduce the excess $u=T-T_{s}$.

The third family is the tank. The trigger phrases are brine flows in, well stirred, flows out at the same rate or at a different rate, concentration of the incoming brine. The opening move is to compute the entry rate and the exit rate separately, with the exit concentration equal to $Q/V$.

The fourth family is the circuit. The trigger phrases are in series, electromotive force, resistance, inductance, capacitance, switch closed at time zero, initial charge. The opening move is to write Kirchhoff's law with the correct drops and to insert the relation between current and charge.

The fifth family is the spring system. The trigger phrases are two masses, two springs, coefficients of stiffness, displaced from equilibrium and released. The opening move is to write Newton's second law for each mass with the extension of each spring expressed in the two displacements, then to assemble the matrix.

### 1.3 The six governing results, with the marks they carry

These six results are the bookwork of the topic. Each is normally worth two or three marks when asked for on its own, and each is the first line of a longer solution.

> **High-yield result 1 (growth and decay).** The law is
>
> $$
> \frac{dx}{dt}=kx , \qquad x=x_{0}e^{kt} ,
> $$
>
> and the half-life or doubling time is $\frac{\ln 2}{|k|}$. Two marks for the equation and its solution, one for the conversion of the half-life.

> **High-yield result 2 (cooling).** The law and its solution are
>
> $$
> \frac{dT}{dt}=-k\left(T-T_{s}\right) , \qquad T=T_{s}+\left(T_{0}-T_{s}\right)e^{-kt} .
> $$
>
> Two marks for the pair, one for the correct excess.

> **High-yield result 3 (tank).** The balance law, the volume function and the constant-volume solution are
>
> $$
> \frac{dQ}{dt}=c_{in}r_{in}-\frac{Q}{V}r_{out} , \qquad V=V_{0}+\left(r_{in}-r_{out}\right)t ,
> $$
>
> $$
> Q=c_{in}V+\left(Q_{0}-c_{in}V\right)e^{-r_{out}t/V} \ \text{when} \ r_{in}=r_{out} .
> $$
>
> Two marks for the balance law with the concentration correct, one for the volume, two for the solution.

> **High-yield result 4 (first-order circuit).** With a coil and a resistor,
>
> $$
> L\frac{di}{dt}+Ri=E , \qquad i=\frac{E}{R}+\left(i_{0}-\frac{E}{R}\right)e^{-Rt/L} ,
> $$
>
> and with a capacitor and a resistor,
>
> $$
> R\frac{dq}{dt}+\frac{q}{C}=E , \qquad q=CE+\left(q_{0}-CE\right)e^{-t/(RC)} , \qquad i=\frac{dq}{dt} .
> $$
>
> One mark for each governing equation, two for each solution, one for the relation between charge and current.

> **High-yield result 5 (second-order circuit).** From Kirchhoff's law,
>
> $$
> L\frac{d^{2}q}{dt^{2}}+R\frac{dq}{dt}+\frac{q}{C}=E(t) ,
> $$
>
> with characteristic roots
>
> $$
> r=\frac{-R\pm\sqrt{R^{2}-\frac{4L}{C}}}{2L} .
> $$
>
> Two marks for the equation, two for the roots, two for naming the case, three for the constants.

> **High-yield result 6 (two masses).** The system and its matrix form are
>
> $$
> m_{1}x_{1}''+\left(k_{1}+k_{2}\right)x_{1}-k_{2}x_{2}=0 , \qquad m_{2}x_{2}''-k_{2}x_{1}+k_{2}x_{2}=0 ,
> $$
>
> $$
> x''=Ax , \qquad A=\begin{pmatrix} -\frac{k_{1}+k_{2}}{m_{1}} & \frac{k_{2}}{m_{1}} \\ \frac{k_{2}}{m_{2}} & -\frac{k_{2}}{m_{2}} \end{pmatrix} .
> $$
>
> Two marks for the equations, three for the eigenvalues, two for the eigenvectors, three for the four constants.

### 1.4 Units the examiner expects to see

A numerical answer without a unit is an incomplete answer in this topic, and the marking schemes usually attach a mark to the unit in at least one part of a long question.

| Quantity | Symbol | Unit | Typical statement in a question |
| --- | --- | --- | --- |
| time | $t$ | minutes, hours or seconds | after $t$ minutes, at time $t>0$ |
| amount, mass, population | $x$ or $Q$ | grams, kilograms, individuals | how much remains, how much is present |
| concentration | $c$ | mass per litre | kilograms of salt per litre |
| volume rate | $r$ | litres per minute | flows in at $5$ litres per minute |
| temperature | $T$ | degrees Celsius | cooled to $60$ degrees |
| current | $i$ | amperes | the current at time $t$ |
| charge | $q$ | coulombs | initial charge on the capacitor |
| electromotive force | $E$ | volts | a battery of $40$ volts |
| resistance | $R$ | ohms | a resistor of $10$ ohms |
| inductance | $L$ | henries | a coil of $0.5$ henries |
| capacitance | $C$ | farads | a capacitor of $2\times10^{-4}$ farads |
| stiffness | $k$ | newtons per metre | coefficient of stiffness $3$ |
| mass | $m$ | kilograms | masses of one unit each |
| displacement | $x$ | metres | displaced $1$ metre to the right |

Two unit facts are worth memorising because they are asked directly. The product of a resistance and a capacitance has the unit of time, and so does the quotient of an inductance by a resistance. Both are the time constants of their circuits, and both are quoted in seconds when the ohm, farad, henry and second are used consistently.

### 1.5 Conditions: how many and which

The order of the governing equation fixes the number of conditions, and the count is a marking point in its own right.

A first-order model needs one condition: the amount present at $t=0$, the temperature at $t=0$, the mass of salt at $t=0$, the initial current, or the initial charge.

A second-order model needs two. For a circuit they are the initial charge and the initial current; for a single oscillator they are the initial displacement and the initial velocity.

A system of two second-order equations needs four: two initial displacements and two initial velocities.

Three conventions recur. Unless stated otherwise the clock starts when the switch is closed or when the motion is released. A mass released from rest has zero initial velocity, so every derivative of every displacement vanishes at $t=0$. A circuit whose switch was open carries no current at the instant of closing, so the initial current is zero even when the capacitor already holds charge.

### 1.6 Vocabulary that earns marks

Definitions are marked as bookwork, so they are worth reproducing precisely rather than paraphrasing.

> **Definition (Steady state).** The steady state of a linear model with constant forcing is the solution that does not vary with time; it is found by setting every derivative to zero.

> **Definition (Transient).** The transient is the difference between the solution and the steady state, and for a stable linear model it decays to zero as time increases.

> **Definition (Time constant).** The time constant is the reciprocal of the coefficient of the unknown after the coefficient of its highest derivative has been reduced to one; after one time constant the transient has fallen to $e^{-1}$ of its initial value.

> **Definition (Damping ratio).** For the equation $Lq''+Rq'+q/C=0$ the damping ratio is $\zeta=\frac{R}{2}\sqrt{\frac{C}{L}}$ and the natural angular frequency is $\omega_{n}=\frac{1}{\sqrt{LC}}$.

> **Definition (Normal mode).** A normal mode is a motion in which every part of the system oscillates with the same frequency and with fixed amplitude ratios.

> **Definition (Concentration).** The concentration of a dissolved substance is its mass divided by the volume of solution, so the concentration in a tank holding mass $Q$ in volume $V$ is $\frac{Q}{V}$.

Each of those six statements is a one-line answer worth one or two marks, and each is also the sentence that justifies the next line of algebra.

## 2. Theorems, Lemmas, and Analytical Properties

### 2.1 Growth and decay: the results that are always examined

> **Theorem (Exponential law).** Every solution of $\frac{dx}{dt}=kx$ is $x=x_{0}e^{kt}$, with $x_{0}=x(0)$, and the doubling time or half-life is $\frac{\ln 2}{|k|}$.

Three exam corollaries follow, and each is a standard part of a question.

> **Corollary (Independence of the starting value).** The time taken to double, or to halve, or to fall to any fixed fraction does not depend on the starting amount.

> **Corollary (Fractional form).** The fraction remaining after time $t$ under decay is $e^{-kt}$, so a percentage question is answered by evaluating an exponential and multiplying by one hundred.

> **Corollary (Two-point determination).** Two observations of the amount at two times determine $k$ and $x_{0}$ uniquely, because the ratio of the observations eliminates $x_{0}$.

The last corollary is the whole technique for a question that says the amount was $A$ at one time and $B$ at another: divide the two equations and take logarithms, which gives $k$ without ever finding $x_{0}$ first.

> **Lemma (Equal ratios over equal intervals).** Under the exponential law, the ratio of the amounts at times separated by a fixed interval is the same at every stage.

This is what makes a table of values double in a recognisable pattern, and it is the fastest check on a computed answer.

### 2.2 Cooling: the results and their marking points

> **Theorem (Newton's law of cooling).** For constant surroundings $T_{s}$ the solution with initial temperature $T_{0}$ is $T=T_{s}+\left(T_{0}-T_{s}\right)e^{-kt}$.

> **Corollary (Constant half-time of the excess).** The excess over the surroundings halves in the time $\frac{\ln 2}{k}$, whatever the initial excess.

> **Corollary (Two-observation determination).** If the excess is $u_{1}$ at one time and $u_{2}$ at a later time separated by $\tau$, then $k=\frac{1}{\tau}\ln\frac{u_{1}}{u_{2}}$.

The marks in a cooling question are almost always one for the law with the correct excess, one for the general solution, two for $k$ from the second observation, and one or two for the numerical answer with its unit. The single commonest loss is a sign error in the excess, which converts a decaying solution into a growing one.

### 2.3 The tank: results for both volume regimes

> **Theorem (Constant-volume tank).** If $r_{in}=r_{out}=r$ and $c_{in}$ is constant, then $Q=c_{in}V+\left(Q_{0}-c_{in}V\right)e^{-rt/V}$ and $Q\to c_{in}V$.

> **Theorem (Variable-volume tank).** If $r_{in}\neq r_{out}$ and $\mu=r_{in}-r_{out}$, then $V=V_{0}+\mu t$ and $Q=c_{in}V+CV^{-r_{out}/\mu}$, and the concentration tends to $c_{in}$ as the volume tends to zero or to infinity, provided the model remains valid.

> **Lemma (Monotone approach).** In the constant-volume case with constant inflow concentration the mass moves monotonically toward $c_{in}V$ and never crosses it.

> **Lemma (Emptying time).** A draining tank with $r_{out}>r_{in}$ empties at $t=\frac{V_{0}}{r_{out}-r_{in}}$, and the model has no meaning beyond that time.

The two theorems differ only in the coefficient of $Q$, but the algebra differs sharply: the constant-volume case has constant coefficients and a pure exponential transient, while the variable-volume case needs the integrating factor $V^{r_{out}/\mu}$ and produces a power of $V$ instead of an exponential.

### 2.4 The first-order circuit: four results to carry into the hall

> **Theorem (Coil and resistor).** For constant $E$, $i=\frac{E}{R}+\left(i_{0}-\frac{E}{R}\right)e^{-Rt/L}$, with time constant $\frac{L}{R}$ and steady current $\frac{E}{R}$.

> **Theorem (Capacitor and resistor).** For constant $E$, $q=CE+\left(q_{0}-CE\right)e^{-t/(RC)}$ and $i=\frac{E-\frac{q_{0}}{C}}{R}e^{-t/(RC)}$, with time constant $RC$ and steady charge $CE$.

> **Theorem (Sinusoidal supply).** For $E=E_{0}\sin\omega t$ the steady current is $\frac{E_{0}}{Z}\sin\left(\omega t-\varphi\right)$ with $Z=\sqrt{R^{2}+\omega^{2}L^{2}}$ and $\tan\varphi=\frac{\omega L}{R}$, and the transient is an exponential with time constant $\frac{L}{R}$.

> **Corollary (Impedance reading).** The steady amplitude is the supply amplitude divided by the impedance, and the current lags the supply by the phase angle $\varphi$.

The phase is the part candidates forget. In a purely resistive circuit the current is in step with the voltage; a coil makes the current lag, and the lag increases with frequency because the coil's opposition grows with frequency.

### 2.5 The second-order circuit: the classification in full

> **Theorem (RLC classification).** For $Lq''+Rq'+q/C=0$ with positive constants, write $\Delta=R^{2}-\frac{4L}{C}$ and $\zeta=\frac{R}{2}\sqrt{\frac{C}{L}}$ and $\omega_{n}=\frac{1}{\sqrt{LC}}$. The solution takes one of three forms, decided by the sign of $\Delta$.

| Case | Condition | Roots | General solution |
| --- | --- | --- | --- |
| Underdamped | $R^{2}<\frac{4L}{C}$, that is $\zeta<1$ | $-a\pm ib$ with $a=\frac{R}{2L}$ and $b=\sqrt{\frac{1}{LC}-\frac{R^{2}}{4L^{2}}}$ | $e^{-at}\left(A\cos bt+B\sin bt\right)$ |
| Critically damped | $R^{2}=\frac{4L}{C}$, that is $\zeta=1$ | repeated at $-\frac{R}{2L}$ | $\left(A+Bt\right)e^{-\frac{R}{2L}t}$ |
| Overdamped | $R^{2}>\frac{4L}{C}$, that is $\zeta>1$ | two distinct real negative values | $Ae^{r_{1}t}+Be^{r_{2}t}$ |

> **Corollary (Critical resistance).** The boundary is at $R_{c}=2\sqrt{\frac{L}{C}}$, and the case is decided by comparing $R$ with $R_{c}$.

> **Corollary (Decay rate).** In the underdamped case the envelope decays at the rate $\frac{R}{2L}$, so the time constant of the envelope is $\frac{2L}{R}$, and the capacitance affects the frequency of the oscillation but not the rate at which its amplitude shrinks.

> **Lemma (Energy dissipation).** With $U=\frac{1}{2}L\left(q'\right)^{2}+\frac{q^{2}}{2C}$ the identity $\frac{dU}{dt}=-R\left(q'\right)^{2}$ holds, so the stored energy decreases whenever current flows and the resistance alone removes it.

The table is the single most useful object in this part of the topic. Classify first, then write the general solution in the row that applies, then impose the two conditions. Doing it in the other order produces a solution form that cannot satisfy the given conditions.

### 2.6 The spring system: eigenvalues, ratios and checks

> **Theorem (Normal modes of two masses).** The system $x''=Ax$ with the matrix of Section 1.3 has two negative eigenvalues $-\omega_{1}^{2}$ and $-\omega_{2}^{2}$, and its general solution is a combination of the two corresponding modes.

> **Lemma (Trace and determinant checks).** For that matrix,
>
> $$
> \lambda_{1}+\lambda_{2}=-\frac{k_{1}+k_{2}}{m_{1}}-\frac{k_{2}}{m_{2}} , \qquad \lambda_{1}\lambda_{2}=\frac{k_{1}k_{2}}{m_{1}m_{2}} .
> $$

Both identities are free checks and both are quick, so they should be applied every time the characteristic polynomial is written down. An eigenvalue computation whose sum or product disagrees with these expressions is wrong, whatever the arithmetic seems to show.

> **Corollary (Mode ratio).** An eigenvector of the matrix gives the ratio of the two amplitudes in the corresponding mode, and that ratio is a fixed number for the system.

> **Corollary (Symmetric case).** For equal masses $m$ and equal stiffnesses $k$ the eigenvalues are $\frac{k}{m}\cdot\frac{-3\pm\sqrt{5}}{2}$.

> **Lemma (Four conditions).** Two second-order equations require four conditions, and with both masses released from rest the two sine terms vanish immediately, so only two constants remain to be found.

### 2.7 Asymptotic results worth tabulating

| Model | Quantity | Limit as $t\to\infty$ | Rate of approach |
| --- | --- | --- | --- |
| Growth and decay | amount $x$ | $0$ for decay, unbounded for growth | exponential with constant $k$ in size |
| Cooling | temperature $T$ | $T_{s}$ | exponential with constant $k$ |
| Tank, constant volume | mass $Q$ | $c_{in}V$ | exponential with constant $\frac{r}{V}$ |
| Coil and resistor | current $i$ | $\frac{E}{R}$ | exponential with constant $\frac{R}{L}$ |
| Capacitor and resistor | charge $q$ | $CE$ | exponential with constant $\frac{1}{RC}$ |
| Second-order circuit | charge $q$ | $0$ when unforced, $CE$ when driven by constant $E$ | exponential with constant $\frac{R}{2L}$ |
| Two springs | displacements | bounded oscillation, no decay without friction | none |

The table answers the standard final part of a long question, which asks what happens after a long time, and it also supplies a check on any solution obtained.

### 2.8 Technique for a "show that" instruction

A question that says show that the displacement is a particular expression is asking for verification, not for a solution. The marks are awarded for the sequence differentiate, substitute, simplify, conclude, and the last step must be an explicit statement that the two sides agree identically.

The procedure is fixed. Differentiate the proposed expression the required number of times. Substitute into the governing equation. Collect the coefficients of each independent function of time. Show that every coefficient vanishes. Confirm the initial conditions. State the conclusion in one sentence.

A verification that stops at substituting without collecting the coefficients usually loses the final mark, because the examiner cannot see that the identity has been established.

## 3. Formal Proofs, Derivations, and Methods

### 3.1 Deriving the exponential law

Step 1. Start from the proportional-rate hypothesis.

$$
\frac{dx}{dt}=kx
$$

Step 2. Separate the variables.

$$
\frac{1}{x}\,dx=k\,dt
$$

Step 3. Integrate both sides.

$$
\ln\left|x\right|=kt+C
$$

Step 4. Exponentiate, writing $e^{C}$ as a positive constant and absorbing the sign into it.

$$
x=Ae^{kt}
$$

Step 5. Impose $x(0)=x_{0}$ to obtain $A=x_{0}$, hence $x=x_{0}e^{kt}$.

Step 6. Verify by differentiation and evaluate at zero. The verification is worth a mark in a show-that question even when the result is quoted from memory.

### 3.2 Deriving the cooling solution

Step 1. Introduce the excess $u=T-T_{s}$, so that $\frac{du}{dt}=\frac{dT}{dt}$ because $T_{s}$ is constant.

Step 2. Substitute into the cooling law.

$$
\frac{du}{dt}=-ku
$$

Step 3. Apply the result of Section 3.1 with the constant $-k$.

$$
u=u_{0}e^{-kt}
$$

Step 4. Translate back with $u_{0}=T_{0}-T_{s}$.

$$
T=T_{s}+\left(T_{0}-T_{s}\right)e^{-kt}
$$

Step 5. Verify by differentiating and by substituting zero.

### 3.3 Deriving the tank law and both solutions

Step 1. Balance the mass over a short interval. The mass entering is $c_{in}r_{in}h$ and the mass leaving is $c_{out}r_{out}h$, so

$$
Q(t+h)-Q(t)=c_{in}r_{in}h-c_{out}r_{out}h .
$$

Step 2. Divide by $h$, let $h\to0$, and use the well-stirred property $c_{out}=\frac{Q}{V}$.

$$
\frac{dQ}{dt}=c_{in}r_{in}-\frac{Q}{V}r_{out}
$$

Step 3. Balance the volume to obtain $V=V_{0}+\left(r_{in}-r_{out}\right)t$.

Step 4. For equal rates, solve with the integrating factor $e^{r_{out}t/V}$.

$$
Q=c_{in}V+\left(Q_{0}-c_{in}V\right)e^{-r_{out}t/V}
$$

Step 5. For unequal rates, write $\mu=r_{in}-r_{out}$ and use the integrating factor $V^{r_{out}/\mu}$.

$$
\frac{d}{dt}\left(QV^{r_{out}/\mu}\right)=c_{in}r_{in}V^{r_{out}/\mu}
$$

Step 6. Integrate, using $r_{out}+\mu=r_{in}$.

$$
QV^{r_{out}/\mu}=c_{in}V^{1+r_{out}/\mu}+C
$$

Step 7. Divide through.

$$
Q=c_{in}V+CV^{-r_{out}/\mu}
$$

Step 8. Verify by differentiating and comparing with $c_{in}r_{in}-r_{out}Q/V$. The two agree for every $C$, which confirms that the general solution has been found.

### 3.4 Deriving the coil equation and solving it

Step 1. Write Kirchhoff's law with the drops across the coil and the resistor.

$$
L\frac{di}{dt}+Ri=E(t)
$$

Step 2. Divide by $L$ and multiply by the integrating factor $e^{Rt/L}$.

$$
\frac{d}{dt}\left(ie^{Rt/L}\right)=\frac{E(t)}{L}e^{Rt/L}
$$

Step 3. Integrate from $0$ to $t$ and solve.

$$
i=e^{-Rt/L}\left(i_{0}+\frac{1}{L}\int_{0}^{t}E(s)e^{Rs/L}\,ds\right)
$$

Step 4. For constant $E$ evaluate the integral.

$$
i=\frac{E}{R}+\left(i_{0}-\frac{E}{R}\right)e^{-Rt/L}
$$

Step 5. For sinusoidal $E=E_{0}\sin\omega t$ substitute $i_{p}=A\sin\omega t+B\cos\omega t$ and match coefficients.

$$
LA\omega+RB=0 , \qquad RA-LB\omega=E_{0}
$$

Step 6. Solve and combine into a single sine with a phase lag.

$$
i_{p}=\frac{E_{0}}{Z}\sin\left(\omega t-\varphi\right) , \qquad Z=\sqrt{R^{2}+\omega^{2}L^{2}} , \qquad \tan\varphi=\frac{\omega L}{R}
$$

Step 7. Add the exponential transient and fix its coefficient from the initial current.

The transient coefficient is always the negative of the particular integral evaluated at $t=0$, because the initial current is normally zero. Writing that sentence explicitly saves a line of algebra and prevents a sign error.

### 3.5 Deriving the capacitor equation

Step 1. Write Kirchhoff's law with the capacitor's drop equal to the charge divided by the capacitance.

$$
R\frac{dq}{dt}+\frac{q}{C}=E
$$

Step 2. Divide by $R$ and identify the time constant $RC$.

$$
\frac{dq}{dt}+\frac{q}{RC}=\frac{E}{R}
$$

Step 3. Solve, then differentiate for the current.

$$
q=CE+\left(q_{0}-CE\right)e^{-t/(RC)} , \qquad i=\frac{E-\frac{q_{0}}{C}}{R}e^{-t/(RC)}
$$

Step 4. Verify by substitution and by both initial values.

### 3.6 Deriving the second-order circuit equation and its classification

Step 1. Apply Kirchhoff's law to a loop containing all three elements.

$$
L\frac{di}{dt}+Ri+\frac{q}{C}=E(t)
$$

Step 2. Replace the current by the rate of change of charge and its derivative by the second derivative of the charge.

$$
L\frac{d^{2}q}{dt^{2}}+R\frac{dq}{dt}+\frac{q}{C}=E(t)
$$

Step 3. Insert the trial solution $q=e^{rt}$ in the homogeneous equation and cancel the exponential.

$$
Lr^{2}+Rr+\frac{1}{C}=0
$$

Step 4. Solve the quadratic.

$$
r=\frac{-R\pm\sqrt{R^{2}-\frac{4L}{C}}}{2L}
$$

Step 5. Read the classification from the discriminant. A negative discriminant gives a complex conjugate pair $-a\pm ib$ with $a=\frac{R}{2L}$ and $b=\sqrt{\frac{1}{LC}-a^{2}}$, hence a decaying oscillation. A zero discriminant gives a double root and the form $\left(A+Bt\right)e^{-at}$. A positive discriminant gives two real roots, both negative.

Step 6. Convert to the engineering parameters.

$$
\omega_{n}=\frac{1}{\sqrt{LC}} , \qquad \zeta=\frac{R}{2}\sqrt{\frac{C}{L}} , \qquad b=\omega_{n}\sqrt{1-\zeta^{2}} , \qquad R_{c}=2\sqrt{\frac{L}{C}}
$$

Step 7. Verify the energy identity, which confirms the sign of the damping term.

$$
\frac{d}{dt}\left(\frac{1}{2}L\left(q'\right)^{2}+\frac{q^{2}}{2C}\right)=-R\left(q'\right)^{2}
$$

### 3.7 Deriving and solving the spring system

Step 1. Express both extensions in terms of the displacements: the first spring is stretched by $x_{1}$ and the second by $x_{2}-x_{1}$.

Step 2. Apply Newton's second law to each mass with the restoring forces directed toward the natural lengths.

$$
m_{1}x_{1}''=-\left(k_{1}+k_{2}\right)x_{1}+k_{2}x_{2} , \qquad m_{2}x_{2}''=k_{2}x_{1}-k_{2}x_{2}
$$

Step 3. Divide each equation by its mass and assemble the matrix.

$$
x''=Ax , \qquad A=\begin{pmatrix} -\frac{k_{1}+k_{2}}{m_{1}} & \frac{k_{2}}{m_{1}} \\ \frac{k_{2}}{m_{2}} & -\frac{k_{2}}{m_{2}} \end{pmatrix}
$$

Step 4. Substitute $x=ve^{st}$ and cancel the exponential to obtain the eigenvalue problem $Av=s^{2}v$, equivalent to $\left(A-\lambda I\right)v=0$ with $\lambda=s^{2}$.

Step 5. Solve $\det\left(A-\lambda I\right)=0$, checking the result against the trace and determinant identities.

Step 6. Find an eigenvector for each eigenvalue from either row of $A-\lambda I$.

Step 7. Write the general solution using cosines and sines, or cosines only when the initial velocities are zero, and impose the initial displacements.

Step 8. Verify by substituting each mode into both original equations.

### 3.8 Choosing the method

| Equation you have written | Recognise it as | Method | Solution shape |
| --- | --- | --- | --- |
| $\frac{dx}{dt}=kx$ | separable, linear | separate and integrate | single exponential |
| $\frac{dT}{dt}=-k\left(T-T_{s}\right)$ | separable after translation | translate then integrate | exponential approach to a constant |
| $\frac{dQ}{dt}=c_{in}r_{in}-\frac{r_{out}}{V}Q$ with constant $V$ | first-order linear, constant coefficients | integrating factor or steady state plus transient | exponential approach to $c_{in}V$ |
| $\frac{dQ}{dt}=c_{in}r_{in}-\frac{r_{out}}{V(t)}Q$ | first-order linear, variable coefficient | integrating factor $V^{r_{out}/\mu}$ | power of $V$ plus a linear term |
| $L\frac{di}{dt}+Ri=E$ | first-order linear, constant coefficients | integrating factor | exponential approach to $\frac{E}{R}$ |
| $Lq''+Rq'+q/C=E$ | second-order linear, constant coefficients | characteristic equation | decaying oscillation, repeated root or two exponentials |
| $x''=Ax$ | system of two second-order equations | eigenvalues and eigenvectors | sum of two normal modes |

The table is a decision aid, not a substitute for the derivations. Its value is that it converts the first ten seconds of reading a question into a named method, which is where most candidates waste time.

## 4. Representative Worked Examples and Solutions

### 4.1 Problem: a culture whose doubling time is known (7 marks)

A culture of bacteria grows at a rate proportional to the number present. The number doubles in $3$ hours. There are $500$ bacteria initially. Write the differential equation, solve it, find the number after $8$ hours, and find the time at which the number reaches $10\,000$.

### 4.2 Solution: model, solve, fit, substitute

Step 1. Name the variables and state the law. Let $x$ be the number of bacteria after $t$ hours and let $k>0$ be the growth constant. (1 mark)

$$
\frac{dx}{dt}=kx
$$

Step 2. Solve the equation with the initial number $x_{0}=500$. (1 mark)

$$
x=500e^{kt}
$$

Step 3. Use the doubling time to determine $k$. Doubling in three hours means that $x=1000$ when $t=3$. (2 marks)

$$
1000=500e^{3k} , \qquad e^{3k}=2 , \qquad k=\frac{\ln 2}{3}=0.2310
$$

Step 4. Write the particular solution. (1 mark)

$$
x=500e^{0.2310t}=500\left(2\right)^{t/3}
$$

Step 5. Evaluate at $t=8$ hours. (1 mark)

$$
x=500\left(2\right)^{8/3}=500\times6.3496=3175
$$

Step 6. Solve for the time at which $x=10\,000$, dividing by $500$ and taking logarithms to base two. (1 mark)

$$
\left(2\right)^{t/3}=20 , \qquad \frac{t}{3}=\frac{\ln 20}{\ln 2}=4.3219 , \qquad t=12.97
$$

Step 7. State the answers with units: about $3175$ bacteria after eight hours and about $12.97$ hours to reach ten thousand. The check is that eight hours is between two and three doublings, so the count must lie between $2000$ and $4000$, and $12.97$ hours is between four and five doublings, so the count must lie between $8000$ and $16\,000$; both hold.

### 4.3 Problem: a tank that drains as it is fed (9 marks)

A tank contains $100$ litres of brine in which $10$ kilograms of salt are dissolved. Brine containing $0.01$ kilograms of salt per litre enters at $4$ litres per minute, and the well-stirred mixture leaves at $5$ litres per minute. Find the mass of salt at time $t$, the mass when $50$ litres remain, and the concentration at that moment.

### 4.4 Solution: the volume falls, so the coefficient grows

Step 1. Name the unknown and write the volume balance. (1 mark)

$$
V(t)=100+\left(4-5\right)t=100-t
$$

Step 2. Compute the entry rate and the exit rate separately, using the tank concentration $Q/V$ for the outflow. (2 marks)

$$
\text{entry rate}=0.01\times4=0.04 , \qquad \text{exit rate}=\frac{Q}{100-t}\times5
$$

Step 3. Write the balance law with the initial condition. (1 mark)

$$
\frac{dQ}{dt}=0.04-\frac{5Q}{100-t} , \qquad Q(0)=10
$$

Step 4. Put the equation in standard linear form and identify the integrating factor. Since $r_{in}-r_{out}=-1$ and $r_{out}=5$, the exponent is $-5$, so the integrating factor is $\left(100-t\right)^{-5}$. (2 marks)

$$
\frac{d}{dt}\left(Q\left(100-t\right)^{-5}\right)=0.04\left(100-t\right)^{-5}
$$

Step 5. Integrate, using the fact that the derivative of $\left(100-t\right)^{-4}$ is $4\left(100-t\right)^{-5}$. (1 mark)

$$
Q\left(100-t\right)^{-5}=0.01\left(100-t\right)^{-4}+C
$$

$$
Q=0.01\left(100-t\right)+C\left(100-t\right)^{5}
$$

Step 6. Impose the initial condition. (1 mark)

$$
10=1+10^{10}C , \qquad C=9\times10^{-10}
$$

Step 7. Evaluate when $50$ litres remain, that is at $t=50$. (1 mark)

$$
Q=0.01\times50+9\times10^{-10}\times50^{5}=0.5+0.28125=0.78125
$$

Step 8. Compute the concentration and state the interpretation. (1 mark)

$$
c=\frac{0.78125}{50}=0.0156
$$

The tank holds $0.78$ kilograms of salt at that moment, at a concentration of $0.0156$ kilograms per litre, which lies between the initial strength of $0.1$ and the inflow strength of $0.01$; the tank would empty at $t=100$ minutes, beyond which the model has no meaning.

### 4.5 Problem: an underdamped circuit (10 marks)

A circuit in series contains an inductance of $1$ henry, a resistance of $6$ ohms and a capacitance of one twenty-fifth of a farad, with no source. At $t=0$ the charge on the capacitor is $0.02$ coulombs and the current is $0.2$ amperes. Classify the circuit, find the charge and the current at time $t$, and find the first instant at which the charge is zero.

### 4.6 Solution: classify first, then fit two conditions

Step 1. Write the homogeneous equation from Kirchhoff's law. (1 mark)

$$
\frac{d^{2}q}{dt^{2}}+6\frac{dq}{dt}+25q=0
$$

Step 2. Write the characteristic equation and solve it. (2 marks)

$$
r^{2}+6r+25=0 , \qquad r=-3\pm4i
$$

Step 3. Classify the circuit, both by the discriminant and by the damping ratio. (2 marks)

$$
\Delta=36-100=-64<0 , \qquad \zeta=\frac{6}{2}\sqrt{\frac{1}{25}}=0.6<1
$$

The circuit is underdamped, with natural frequency $\omega_{n}=5$ and damped frequency $4$ radians per second, and the critical resistance $2\sqrt{25}=10$ ohms is indeed larger than $6$.

Step 4. Write the general solution in the underdamped form. (1 mark)

$$
q=e^{-3t}\left(A\cos 4t+B\sin 4t\right)
$$

Step 5. Impose the initial charge. (1 mark)

$$
q(0)=A=0.02
$$

Step 6. Differentiate, then impose the initial current. (2 marks)

$$
i=e^{-3t}\left(\left(-3A+4B\right)\cos 4t+\left(-4A-3B\right)\sin 4t\right)
$$

$$
i(0)=-3\left(0.02\right)+4B=0.2 , \qquad B=0.065
$$

Step 7. State the solutions. (1 mark)

$$
q=e^{-3t}\left(0.02\cos 4t+0.065\sin 4t\right)
$$

$$
i=e^{-3t}\left(0.2\cos 4t-0.275\sin 4t\right)
$$

Step 8. Find the first zero of the charge by writing it as a single cosine. (1 mark)

$$
q=0.06801e^{-3t}\cos\left(4t-1.2723\right) , \qquad 4t-1.2723=\frac{\pi}{2} , \qquad t=0.711
$$

Step 9. Check and interpret. The two constants were built from the roots, so the equation is satisfied identically; at $t=0$ the charge is $0.02$ coulombs and the current is $0.2$ amperes, as required. The charge crosses zero at about $0.711$ seconds and thereafter swings with decreasing amplitude, one crossing every half period of $\frac{\pi}{4}$ seconds, while the current leads the charge by a quarter of a cycle.

### 4.7 Problem: a coil driven by an alternating supply (8 marks)

A circuit in series contains a resistance of $12$ ohms and an inductance of $0.2$ henries, and is connected to an alternating supply of $120\sin 60t$ volts. The current is zero when the switch is closed. Find the current at time $t$, the steady amplitude and the phase lag.

### 4.8 Solution: particular integral plus transient

Step 1. Write Kirchhoff's law with the numbers inserted. (1 mark)

$$
0.2\frac{di}{dt}+12i=120\sin 60t
$$

Step 2. Divide by $0.2$ to obtain standard linear form. (1 mark)

$$
\frac{di}{dt}+60i=600\sin 60t
$$

Step 3. Seek a particular integral of the form $A\sin 60t+B\cos 60t$ and substitute. (2 marks)

$$
60A\cos 60t-60B\sin 60t+60A\sin 60t+60B\cos 60t=600\sin 60t
$$

$$
60A+60B=0 , \qquad 60A-60B=600
$$

Step 4. Solve the pair. (1 mark)

$$
A=5 , \qquad B=-5
$$

Step 5. Write the particular integral and convert it to a single sine with a phase lag. (1 mark)

$$
i_{p}=5\sin 60t-5\cos 60t=7.071\sin\left(60t-\frac{\pi}{4}\right)
$$

Step 6. Add the transient and impose the zero initial current. (1 mark)

$$
i=7.071\sin\left(60t-\frac{\pi}{4}\right)+Ce^{-60t} , \qquad 0=-5+C , \qquad C=5
$$

Step 7. State the solution and the requested quantities. (1 mark)

$$
i=5\sin 60t-5\cos 60t+5e^{-60t}=7.071\sin\left(60t-0.785\right)+5e^{-60t}
$$

The steady amplitude is $7.07$ amperes, the phase lag is $\frac{\pi}{4}$ radians, and the time constant of the transient is $\frac{1}{60}$ seconds, so the transient has decayed to $0.012$ amperes by $t=0.1$ seconds.

Step 8. Check. Differentiating the solution gives $300\cos 60t+300\sin 60t-300e^{-60t}$, so $0.2$ times the derivative plus $12$ times the current is $60\cos 60t+60\sin 60t-60e^{-60t}+60\sin 60t-60\cos 60t+60e^{-60t}=120\sin 60t$, and the initial current is zero.

### 4.9 Problem: two masses joined by springs (9 marks)

Masses of $2$ kilograms and $1$ kilogram are joined by springs of stiffness $4$ and $2$ newtons per metre with the arrangement of Section 1.3. At $t=0$ the displacements are $0.1$ metres and $-0.2$ metres and both masses are released from rest. Find both displacements at time $t$.

### 4.10 Solution: eigenvalues, eigenvectors, four conditions

Step 1. Write the two equations of motion. (1 mark)

$$
2x_{1}''=-6x_{1}+2x_{2} , \qquad x_{2}''=2x_{1}-2x_{2}
$$

Step 2. Divide by the masses and assemble the matrix. (1 mark)

$$
x''=Ax , \qquad A=\begin{pmatrix} -3 & 1 \\ 2 & -2 \end{pmatrix}
$$

Step 3. Write the characteristic polynomial and check it against the trace and determinant. (2 marks)

$$
\lambda^{2}+5\lambda+4=0 , \qquad \text{trace}=-5 , \qquad \det=6-2=4
$$

Step 4. Factor and read the eigenvalues. (1 mark)

$$
\left(\lambda+1\right)\left(\lambda+4\right)=0 , \qquad \lambda=-1 , \quad \lambda=-4
$$

The normal frequencies are $1$ and $2$ radians per second.

Step 5. Find the eigenvectors. For $\lambda=-1$ the first row of $A-\lambda I$ gives $-2v_{1}+v_{2}=0$, so $v=\left(1,2\right)$; for $\lambda=-4$ it gives $v_{1}+v_{2}=0$, so $v=\left(1,-1\right)$. (2 marks)

Step 6. Write the general solution with cosines only, since both initial velocities are zero. (1 mark)

$$
x_{1}=a_{1}\cos t+a_{2}\cos 2t , \qquad x_{2}=2a_{1}\cos t-a_{2}\cos 2t
$$

Step 7. Impose the initial displacements. (1 mark)

$$
a_{1}+a_{2}=0.1 , \qquad 2a_{1}-a_{2}=-0.2
$$

Step 8. Solve the pair and state the answer. (1 mark)

$$
a_{1}=-\frac{1}{30} , \qquad a_{2}=\frac{2}{15}
$$

$$
x_{1}=-\frac{1}{30}\cos t+\frac{2}{15}\cos 2t , \qquad x_{2}=-\frac{1}{15}\cos t-\frac{2}{15}\cos 2t
$$

Step 9. Verify both equations and both conditions. Differentiating $x_{1}$ twice gives $\frac{1}{30}\cos t-\frac{8}{15}\cos 2t$, and $-3x_{1}+x_{2}$ equals $\frac{1}{10}\cos t-\frac{2}{5}\cos 2t-\frac{1}{15}\cos t-\frac{2}{15}\cos 2t$, which is $\frac{1}{30}\cos t-\frac{8}{15}\cos 2t$, as required; differentiating $x_{2}$ twice gives $\frac{1}{15}\cos t+\frac{8}{15}\cos 2t$, and $2x_{1}-2x_{2}$ equals the same expression. At $t=0$ the answers give $0.1$ and $-0.2$ metres, and both velocities are zero.

Step 10. Interpret. The motion is a mixture of a slow in-phase mode, in which the heavier mass moves half as far as the lighter one in the same direction, and a faster out-of-phase mode; the initial displacements excite both modes, so the motion is not periodic in general even though each mode is.

## 5. Mathematical Extensions, Limits, and Common Errors

### 5.1 The trap table

The table lists the errors that account for most lost marks in this topic, in descending order of how often they occur. Reading it before an examination is worth more than re-reading any single derivation.

| Trap | What it looks like in an answer | Correct treatment | Typical cost |
| --- | --- | --- | --- |
| Inflow concentration used in the outflow term | the exit rate written as $c_{in}r_{out}$, so the right side does not contain $Q$ | the outflow carries the tank concentration, so the rate is $\frac{Q}{V}r_{out}$ | 2 to 4 marks, and the whole answer becomes impossible |
| Initial condition ignored or applied too early | a solution still containing $C$, or $C$ fixed before the particular integral was added | finish the general solution, then substitute $t=0$ | 1 to 2 marks, plus every later numerical part |
| Charge and current confused | the charge given as the answer to a question about current, or $i(0)$ used where $q(0)$ belongs | $i=\frac{dq}{dt}$, so the current needs one differentiation and the initial current constrains the derivative | 2 to 3 marks |
| Damping classification misread | the case decided from the size of $R$ alone, or from the sign of $R^{2}-\frac{4L}{C}$ taken the wrong way | compare $R$ with $R_{c}=2\sqrt{\frac{L}{C}}$; underdamped means the discriminant is negative | 2 marks for the classification and often the form of the whole solution |
| Volume held constant when the rates differ | $V$ taken as $V_{0}$ throughout a draining tank | use $V=V_{0}+\left(r_{in}-r_{out}\right)t$ | 2 marks, and the constant cannot be found |
| Sign of the decay constant doubled | $k$ taken negative inside a formula that already carries a minus | keep $k>0$ and let the sign in the law record growth or decay | 1 to 2 marks |
| Percentage treated as a continuous rate | $k=0.02$ for a growth of two per cent per year | $k=\ln 1.02$ | 1 mark, and a small numerical error thereafter |
| Repeated-root form written as two independent exponentials | $Ae^{rt}+Be^{rt}$ at critical damping | $\left(A+Bt\right)e^{rt}$ | 2 marks |
| Eigenvalue used as a frequency | $\omega=-1$ quoted for an eigenvalue of $-1$ | $\omega=\sqrt{-\lambda}$ | 1 to 2 marks |
| Only two conditions used for two masses | two constants instead of four | add the two initial velocities | 2 marks |
| Units omitted | a bare number where a current or a temperature was asked for | state amperes, coulombs, degrees, kilograms | 0 to 1 mark per part |
| Answer left as a formula | no sentence interpreting the result | state the limiting value, the time reached, or the physical meaning | the final mark of the part |
| Verification done only at $t=0$ | the initial value checked and the equation assumed | differentiate and substitute into the equation as well | the mark for checking |

### 5.2 The four traps examined closely

The first trap is the sign and the concentration in the mixture rate. The balance law is written as rate in minus rate out, and candidates who treat the tank as if its contents were replaced instantly produce an exit term that does not depend on $Q$. The diagnostic is immediate: if $Q$ disappears from the right-hand side, the model is not a mixture model, because the outflow of a well-stirred tank must depend on what the tank contains. The correct line is

$$
\frac{dQ}{dt}=c_{in}r_{in}-\frac{Q}{V}r_{out} ,
$$

and the sign in front of the second term is negative because the substance is leaving. A second sign trap hides in the volume: with $r_{out}>r_{in}$ the coefficient of $Q$ grows as the tank empties, so the loss accelerates, which is why a draining tank can be flushed to the strength of its feed in a finite time.

The second trap is the forgotten initial condition. It appears in two forms. Sometimes the constant is never fixed and the answer is left as a family, which forfeits the numerical parts that follow. More often the constant is fixed too early: a particular integral is added to the complementary function after the constant has been determined, so the final expression satisfies the condition but not the equation. The discipline that avoids both forms is to write the general solution with all its constants, impose the condition on that complete expression, and only then simplify.

The third trap is the confusion of charge and current. The state variable of the second-order circuit is the charge, and the current is its derivative. A question that gives the initial charge and the initial current is therefore giving one condition on the function and one on its derivative, and a question that asks for the current requires one differentiation of the answer. The same distinction appears in the first-order capacitive circuit, where the charge rises from zero while the current falls from its largest value; reporting either one as the other is wrong even when both formulas are correct.

The fourth trap is the damping classification. The classification is decided by the sign of $R^{2}-\frac{4L}{C}$, equivalently by comparing $R$ with $2\sqrt{\frac{L}{C}}$, equivalently by comparing $\zeta$ with one. All three routes give the same answer when applied carefully, and all three can be misapplied. A large resistance does not by itself guarantee overdamping, because a large capacitance makes the critical resistance small; a small resistance does not by itself guarantee underdamping, because a small inductance makes the critical resistance small as well. The safe procedure is to compute $R_{c}$ explicitly and to compare numbers, and then to name the case using the word that matches the comparison.

### 5.3 Revision checklist

- I can write the growth and decay law, its solution, and convert a half-life or doubling time into the constant.
- I can explain why the doubling time does not depend on the starting amount.
- I can write Newton's law of cooling with the excess formed correctly, and solve it by translation.
- I can compute an entry rate and an exit rate separately, using the tank concentration in the exit rate.
- I can write the volume function when the inflow and outflow rates differ, and choose the integrating factor accordingly.
- I can quote the steady state and the time constant of the tank, the coil and the capacitor circuits.
- I can derive Kirchhoff's law for a loop with two elements and for a loop with three.
- I can distinguish charge from current and differentiate correctly between them.
- I can write the characteristic equation of the second-order circuit, compute its roots, and name the case from the discriminant, the damping ratio and the critical resistance.
- I can write the general solution in the three cases, including the repeated-root form.
- I can find the steady current and the phase lag for a sinusoidal supply, and add the transient.
- I can write the two equations of a two-mass spring system, assemble the matrix, find eigenvalues and eigenvectors, and fit four conditions.
- I can check every eigenvalue computation against the trace and the determinant.
- I can verify a solution by substitution, by the initial values and by the long-run behaviour.
- I can state every answer with its unit and one sentence of interpretation.

### 5.4 Time strategy

The marks in this topic are distributed evenly enough that a mechanical plan works better than intuition.

Budget roughly one minute per mark and keep a margin of ten per cent. A ten-mark second-order circuit therefore deserves eleven minutes, and a six-mark decay question seven minutes.

Read the whole paper first and identify the two or three bookwork parts, which are worth two or three marks each and take two minutes each. Do those first, because they bank marks before any long calculation can go wrong.

In a long question, spend the first thirty seconds naming variables and writing the governing equation. That line is worth a mark on its own, and having it on paper makes every later mark recoverable even if the algebra stalls.

When a numerical answer looks wrong, check it against three cheap tests before redoing the algebra: the initial value, the long-run value, and the sign of the derivative at the start. If a tank's mass is decreasing when the tank is saltier than its feed, the solution must decrease; if a current is rising toward a steady value, its derivative must be positive throughout.

If a classification is required and time is short, compute the critical resistance, compare, and name the case; that is two marks that do not depend on solving the equation.

Leave the last two minutes of the paper for units and interpretation, which are the marks most often lost by candidates who have done all the hard work correctly.

### 5.5 Where the examined models end

The models examined here are the linear ones, and it is worth knowing in one sentence what lies beyond each of them.

The exponential growth model becomes the logistic model when a carrying capacity is introduced, and the logistic solution still starts exponentially but approaches the capacity $k$ divided by $\lambda$ in the equation $\frac{dx}{dt}=kx-\lambda x^{2}$.

The constant-coefficient tank model becomes a variable-coefficient model when the volume changes, and it becomes non-linear when the dissolved substance reacts with itself.

The circuit models become non-linear when a component's characteristic is not proportional, as with an iron-cored coil, and they require Fourier methods when the supply is periodic but not sinusoidal.

The two-mass spring model becomes a general vibration problem when many masses are joined, and its normal frequencies are then the eigenvalues of a larger matrix; the mathematics is the same eigenvalue problem, only larger.

Every extension keeps the same skeleton: a physical law, a linear or nearly linear equation, a steady state, a transient, and an interpretation. The examination tests the skeleton, and the examination questions never wander far from it.